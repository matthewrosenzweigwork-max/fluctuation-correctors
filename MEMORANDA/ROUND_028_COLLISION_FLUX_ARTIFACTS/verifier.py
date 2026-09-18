#!/usr/bin/env python3
"""Portable read-only integrity/reproduction verifier for the TASK121 packet.

Uses only the Python standard library. Never extracts an archive and never
writes a file. Integrity and exact diagnostic reproduction are not a proof
certificate or an independent mathematical audit.
"""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tarfile


class IntegrityError(Exception):
    pass


def need(condition, message):
    if not condition:
        raise IntegrityError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    need(isinstance(name, str) and bool(name), 'Empty or nonstring member name')
    need(not any(c in name for c in ('\\', '\x00', '\n', '\r', ':')),
         'Nonportable character in member name: ' + repr(name))
    p = PurePosixPath(name)
    need(not p.is_absolute(), 'Absolute member name: ' + name)
    need(all(part not in ('', '.', '..') for part in name.split('/')),
         'Unsafe path component: ' + name)
    need(p.as_posix() == name, 'Noncanonical member name: ' + name)
    return name


def parse_manifest(data):
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError as exc:
        raise IntegrityError('Manifest is not UTF-8') from exc
    need(text.endswith('\n'), 'Manifest lacks final newline')
    result = {}
    for row in text.splitlines():
        need('  ' in row, 'Malformed manifest row')
        hexdigest, name = row.split('  ', 1)
        need(re.fullmatch(r'[0-9a-f]{64}', hexdigest) is not None,
             'Malformed digest for ' + name)
        safe_name(name)
        need(name not in result, 'Duplicate manifest member: ' + name)
        result[name] = hexdigest
    need(bool(result), 'Empty manifest')
    return result


def regular_tree(root):
    need(not root.is_symlink(), 'Packet root is a symlink')
    need(root.is_dir(), 'Packet root is not a directory')
    files = {}
    directories = []

    def descend(folder):
        mode = folder.stat().st_mode
        need(stat.S_ISDIR(mode), 'Non-directory in traversal')
        need(not mode & 0o222, 'Writable issued directory: ' + str(folder))
        directories.append(folder)
        with os.scandir(str(folder)) as iterator:
            entries = sorted(iterator, key=lambda item: item.name)
        for entry in entries:
            path = Path(entry.path)
            need(not entry.is_symlink(), 'Symlink in packet: ' + str(path))
            mode = entry.stat(follow_symlinks=False).st_mode
            if stat.S_ISDIR(mode):
                descend(path)
            else:
                need(stat.S_ISREG(mode), 'Nonregular member: ' + str(path))
                need(not mode & 0o222, 'Writable issued file: ' + str(path))
                relative = path.relative_to(root).as_posix()
                safe_name(relative)
                need(relative not in files, 'Duplicate tree name')
                files[relative] = path.read_bytes()

    descend(root)
    return files, directories


def read_regular_archive(fileobj, prefix):
    safe_name(prefix)
    need('/' not in prefix, 'Archive prefix must be one component')
    payload = {}
    with tarfile.open(fileobj=fileobj, mode='r:*') as archive:
        for member in archive:
            safe_name(member.name)
            need(member.name.startswith(prefix + '/'), 'Wrong archive prefix')
            relative = member.name[len(prefix)+1:]
            safe_name(relative)
            need(member.type in (tarfile.REGTYPE, tarfile.AREGTYPE),
                 'Nonregular archive member: ' + member.name)
            need(not member.mode & 0o222, 'Writable archive member: ' + member.name)
            need(member.name not in payload, 'Duplicate archive member: ' + member.name)
            handle = archive.extractfile(member)
            need(handle is not None, 'Unreadable regular archive member')
            data = handle.read()
            need(len(data) == member.size, 'Archive member size mismatch')
            payload[member.name] = data
    need(bool(payload), 'Empty archive')
    return payload


def safety_selftests():
    rejected = []

    def reject(label, action):
        try:
            action()
        except IntegrityError:
            rejected.append(label)
            return
        raise IntegrityError('Safety mutation was accepted: ' + label)

    for bad in ('../bad', '/bad', 'a/../bad', 'a//bad', 'a/./bad',
                'a\\bad', 'a\x00bad', 'C:/bad', '', 'a/..'):
        reject('unsafe_name_' + repr(bad), lambda value=bad: safe_name(value))
    duplicate = ('a'*64 + '  x\n' + 'b'*64 + '  x\n').encode()
    reject('duplicate_manifest', lambda: parse_manifest(duplicate))
    reject('bad_manifest_digest', lambda: parse_manifest(b'abc  x\n'))

    def fake_archive(names_types):
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode='w', format=tarfile.USTAR_FORMAT) as archive:
            for name, kind in names_types:
                member = tarfile.TarInfo(name)
                member.mode = 0o444
                member.type = kind
                if kind == tarfile.REGTYPE:
                    data = b'test'
                    member.size = len(data)
                    archive.addfile(member, io.BytesIO(data))
                else:
                    member.linkname = 'target'
                    archive.addfile(member)
        buffer.seek(0)
        return read_regular_archive(buffer, 'packet')

    need(fake_archive([('packet/x', tarfile.REGTYPE)]) == {'packet/x': b'test'},
         'Valid in-memory archive was rejected')
    bad_cases = [
        ('archive_traversal', [('packet/../x', tarfile.REGTYPE)]),
        ('archive_absolute', [('/packet/x', tarfile.REGTYPE)]),
        ('archive_wrong_prefix', [('other/x', tarfile.REGTYPE)]),
        ('archive_symlink', [('packet/x', tarfile.SYMTYPE)]),
        ('archive_hardlink', [('packet/x', tarfile.LNKTYPE)]),
        ('archive_directory', [('packet/x', tarfile.DIRTYPE)]),
        ('archive_device', [('packet/x', tarfile.CHRTYPE)]),
        ('archive_duplicate', [('packet/x', tarfile.REGTYPE), ('packet/x', tarfile.REGTYPE)]),
    ]
    for label, members in bad_cases:
        reject(label, lambda values=members: fake_archive(values))
    return rejected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, help='Explicit issued archive to inspect without extraction')
    parser.add_argument('--memo', type=Path, help='Explicit separately delivered memorandum to compare')
    args = parser.parse_args()
    root = Path(__file__).absolute().parent
    files, directories = regular_tree(root)
    manifest_name = 'CONTENT_SHA256SUMS.txt'
    need(manifest_name in files, 'Missing complete content manifest')
    expected = parse_manifest(files[manifest_name])
    need(set(files) == set(expected) | {manifest_name},
         'Regular-file inventory mismatch; missing=%r extra=%r' %
         (sorted(set(expected)-set(files)), sorted(set(files)-set(expected)-{manifest_name})))
    for name, hexdigest in expected.items():
        need(digest(files[name]) == hexdigest, 'Payload digest mismatch: ' + name)

    inputs = parse_manifest(files['INPUT_SHA256SUMS.txt'])
    need(len(inputs) == 12, 'Input manifest must contain exactly twelve entries')
    input_payloads = {name[len('INPUTS/'):] for name in files if name.startswith('INPUTS/')}
    need(input_payloads == set(inputs), 'Copied input inventory mismatch')
    for name, hexdigest in inputs.items():
        need(digest(files['INPUTS/' + name]) == hexdigest, 'Input digest mismatch: ' + name)
    preflight = json.loads(files['INPUT_PREFLIGHT.json'])
    need(preflight['count'] == 12 and preflight['all_pass'], 'Failed recorded preflight')
    need(preflight['manifest_sha256'] == digest(files['INPUT_SHA256SUMS.txt']),
         'Recorded input manifest digest mismatch')
    need({entry['path'] for entry in preflight['inputs']} == set(inputs),
         'Preflight input inventory mismatch')
    for entry in preflight['inputs']:
        need(entry['sha256'] == inputs[entry['path']] and entry['original_pass'] and entry['copy_pass'],
             'Preflight record mismatch')
        need(entry['bytes'] == len(files['INPUTS/' + entry['path']]), 'Preflight size mismatch')

    memo_name = 'ROUND_028_FIRST_COLLISION_FLUX.md'
    need(memo_name in files, 'Missing portable complete proof copy')
    if args.memo is not None:
        need(not args.memo.is_symlink() and args.memo.is_file(), 'Memo is not a regular nonlink file')
        need(not args.memo.stat().st_mode & 0o222, 'Issued memorandum is writable')
        need(args.memo.read_bytes() == files[memo_name], 'Separate memorandum differs from packet copy')

    process = subprocess.run([sys.executable, '-B', str(root/'diagnostics.py'), '--json'],
                             capture_output=True, text=True, check=False)
    need(process.returncode == 0, 'Diagnostic rerun failed: ' + process.stderr)
    need(process.stderr == '', 'Diagnostic rerun emitted stderr')
    reproduced = json.loads(process.stdout)
    saved = json.loads(files['DIAGNOSTICS_STDOUT.json'])
    need(files['DIAGNOSTICS_STDERR.txt'] == b'', 'Recorded diagnostic stderr is nonempty')
    # The portable check allows a different supported Python runtime version,
    # but requires every mathematical input/result and all statuses to match.
    reproduced.pop('runtime_python', None)
    saved.pop('runtime_python', None)
    need(reproduced == saved, 'Exact diagnostic output differs')
    need(saved['all_pass'] and saved['baseline_count'] == 1480 and saved['mutation_count'] == 11,
         'Unexpected diagnostic status or counts')
    safety_rejections = safety_selftests()

    archive_sha = None
    archive_members = None
    if args.archive is not None:
        need(not args.archive.is_symlink() and args.archive.is_file(), 'Archive is not a regular nonlink file')
        need(not args.archive.stat().st_mode & 0o222, 'Issued archive is writable')
        with args.archive.open('rb') as source:
            archived = read_regular_archive(source, root.name)
        target_names = {root.name + '/' + name for name in files}
        need(set(archived) == target_names, 'Archive member inventory mismatch')
        for name, data in files.items():
            need(archived[root.name + '/' + name] == data, 'Archive bytes differ: ' + name)
        archive_sha = digest(args.archive.read_bytes())
        archive_members = len(archived)

    result = {
        'status': 'PASS',
        'meaning': 'Read-only integrity and exact diagnostic reproduction only; no independent mathematical certification',
        'regular_file_count_including_manifest': len(files),
        'read_only_directory_count': len(directories),
        'payload_digests_verified': len(expected),
        'frozen_inputs_verified': len(inputs),
        'baseline_checks_reproduced': saved['baseline_count'],
        'nonzero_mathematical_mutations_reproduced': saved['mutation_count'],
        'in_memory_safety_mutations_rejected': len(safety_rejections),
        'safety_rejections': safety_rejections,
        'content_manifest_sha256': digest(files[manifest_name]),
        'input_manifest_sha256': digest(files['INPUT_SHA256SUMS.txt']),
        'memorandum_sha256': digest(files[memo_name]),
        'separate_memorandum_checked': args.memo is not None,
        'archive_checked': args.archive is not None,
        'archive_regular_members': archive_members,
        'archive_sha256': archive_sha,
        'file_writes_performed': False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (IntegrityError, OSError, ValueError, KeyError, tarfile.TarError) as exc:
        print('VERIFICATION FAILED: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
