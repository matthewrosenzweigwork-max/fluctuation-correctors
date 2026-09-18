#!/usr/bin/env python3
"""Read-only AUD060 byte verifier. Archives are streamed, never extracted.

The SHA-256 of FINAL_SHA256SUMS.txt is the external handoff anchor; this program
cannot authenticate a replacement of itself together with every seal. The
prepare-only option exists to record core verification before the final list.
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


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    require(isinstance(name, str) and name and '\\' not in name and '\x00' not in name,
            'Unsafe empty, backslash or NUL path')
    p = PurePosixPath(name)
    require(bool(p.parts) and not p.is_absolute() and str(p) == name and
            all(part not in ('', '.', '..') for part in p.parts), 'Unsafe/noncanonical path: ' + name)
    return name


def regular_bytes(path, readonly=False):
    st = path.lstat()
    require(stat.S_ISREG(st.st_mode) and not path.is_symlink(), 'Nonregular/link file: ' + str(path))
    if readonly:
        require(st.st_mode & 0o222 == 0, 'Issued file remains writable: ' + str(path))
    return path.read_bytes()


def files_under(root):
    require(root.is_dir() and not root.is_symlink(), 'Unsafe packet directory')
    found = {}
    for dirname, subdirs, files in os.walk(root, followlinks=False):
        for name in subdirs:
            p = Path(dirname)/name
            require(not p.is_symlink(), 'Symlink directory: ' + str(p))
        for name in files:
            p = Path(dirname)/name
            relative = safe_name(p.relative_to(root).as_posix())
            st = p.lstat()
            require(stat.S_ISREG(st.st_mode) and not p.is_symlink(), 'Nonregular packet member: '+relative)
            found[relative] = p
    return found


def parse_manifest(data):
    result = {}
    for line in data.decode('utf-8').splitlines():
        require(re.fullmatch(r'[0-9a-f]{64}  .+', line) is not None, 'Invalid hash-manifest line')
        expected, name = line.split('  ', 1)
        safe_name(name)
        require(name not in result, 'Duplicate hash-manifest path: '+name)
        result[name] = expected
    require(result, 'Empty hash manifest')
    return result


def verify_archive(source, expected):
    """expected maps exact canonical member names to (size, sha256)."""
    seen = set()
    with tarfile.open(fileobj=source, mode='r:gz') as archive:
        for member in archive:
            require(len(seen) < len(expected), 'Extra archive member')
            name = safe_name(member.name)
            require(name not in seen, 'Duplicate archive member: '+name)
            require(member.type in (tarfile.REGTYPE, tarfile.AREGTYPE) and member.isfile()
                    and not member.linkname and not member.pax_headers,
                    'Link, special, directory or extended archive member: '+name)
            require(name in expected, 'Unexpected archive member: '+name)
            size, expected_hash = expected[name]
            require(member.size == size, 'Archive size mismatch: '+name)
            handle = archive.extractfile(member)  # Read stream only; never extract/extractall.
            require(handle is not None, 'Unreadable regular member')
            actual_hash = hashlib.sha256()
            read = 0
            while True:
                block = handle.read(min(65536, size-read+1))
                if not block:
                    break
                read += len(block)
                require(read <= size, 'Archive member exceeds exact size')
                actual_hash.update(block)
            require(read == size and actual_hash.hexdigest() == expected_hash,
                    'Archive byte mismatch: '+name)
            seen.add(name)
    require(seen == set(expected), 'Missing archive members')
    return len(seen)


def make_test_archive(entries):
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode='w:gz', format=tarfile.USTAR_FORMAT) as archive:
        for name, body, kind, link in entries:
            member = tarfile.TarInfo(name)
            member.type = kind
            member.linkname = link
            member.size = len(body) if kind == tarfile.REGTYPE else 0
            archive.addfile(member, io.BytesIO(body) if kind == tarfile.REGTYPE else None)
    return buffer.getvalue()


def rejection_controls():
    body = b'exact byte control\n'
    normal = ('packet/ok.txt', body, tarfile.REGTYPE, '')
    expected = {'packet/ok.txt': (len(body), digest(body))}
    verify_archive(io.BytesIO(make_test_archive([normal])), expected)
    cases = {
        'wrong_byte_same_length': [('packet/ok.txt', b'X'+body[1:], tarfile.REGTYPE, '')],
        'wrong_size': [('packet/ok.txt', body+b'!', tarfile.REGTYPE, '')],
        'missing_member': [],
        'extra_member': [normal, ('packet/extra.txt', b'x', tarfile.REGTYPE, '')],
        'duplicate_member': [normal, normal],
        'parent_traversal': [('packet/../ok.txt', body, tarfile.REGTYPE, '')],
        'absolute_path': [('/packet/ok.txt', body, tarfile.REGTYPE, '')],
        'dot_path': [('./packet/ok.txt', body, tarfile.REGTYPE, '')],
        'repeated_separator': [('packet//ok.txt', body, tarfile.REGTYPE, '')],
        'backslash_path': [('packet\\ok.txt', body, tarfile.REGTYPE, '')],
        'symbolic_link': [('packet/ok.txt', b'', tarfile.SYMTYPE, '/outside')],
        'hard_link': [('packet/ok.txt', b'', tarfile.LNKTYPE, '/outside')],
        'fifo': [('packet/ok.txt', b'', tarfile.FIFOTYPE, '')],
        'directory': [('packet/ok.txt', b'', tarfile.DIRTYPE, '')],
    }
    result = {}
    for label, entries in cases.items():
        try:
            verify_archive(io.BytesIO(make_test_archive(entries)), expected)
        except (ValueError, tarfile.TarError, EOFError) as error:
            result[label] = str(error)
        else:
            raise ValueError('Archive mutation accepted: '+label)
    for label, data in {
        'duplicate_manifest_path': ('a'*64+'  safe\n'+'b'*64+'  safe\n').encode(),
        'manifest_traversal': ('a'*64+'  ../unsafe\n').encode(),
        'manifest_malformed_digest': b'short  safe\n',
    }.items():
        try:
            parse_manifest(data)
        except ValueError as error:
            result[label] = str(error)
        else:
            raise ValueError('Manifest mutation accepted: '+label)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rerun-diagnostic', action='store_true')
    parser.add_argument('--self-test-rejections', action='store_true')
    parser.add_argument('--prepare-seal', action='store_true',
                        help='Only the initial recording step: skip the not-yet-built final output list.')
    args = parser.parse_args()
    script = Path(__file__).absolute()
    require(not script.is_symlink(), 'Verifier is a symlink')
    packet = script.parent
    top = packet.parent
    require(packet.name == 'packet' and top.name == 'ROUND_020_CONTINUOUS_PATH_HOSTILE_ARTIFACTS',
            'Unexpected packet layout')
    report = top.parent/'ROUND_020_CONTINUOUS_PATH_REVIEW.md'
    readonly = not args.prepare_seal
    seal_bytes = regular_bytes(top/'SEAL.json', readonly)
    seal = json.loads(seal_bytes)
    require(seal['audit'] == 'AUD060' and seal['input_count'] == 16, 'Wrong audit/input seal')
    paths = files_under(packet)
    payload_manifest = regular_bytes(packet/'PAYLOAD_SHA256SUMS.txt', readonly)
    require(digest(payload_manifest) == seal['payload_manifest_sha256'], 'Payload manifest seal mismatch')
    payload = parse_manifest(payload_manifest)
    require(set(payload) == set(paths)-{'PAYLOAD_SHA256SUMS.txt'}, 'Incomplete payload inventory')
    archive_expected = {}
    for name, path in sorted(paths.items()):
        data = regular_bytes(path, readonly)
        if name in payload:
            require(digest(data) == payload[name], 'Payload byte mismatch: '+name)
        archive_expected['packet/'+name] = (len(data), digest(data))
    report_bytes = regular_bytes(report, readonly)
    require(report_bytes == regular_bytes(packet/'REVIEW.md', readonly), 'Sibling review differs from packet review')
    require(digest(report_bytes) == seal['report_sha256'] and len(report_bytes) == seal['report_bytes'],
            'Review external seal mismatch')
    manifest_bytes = regular_bytes(packet/'INPUT_SHA256SUMS.txt', readonly)
    require(digest(manifest_bytes) == seal['input_manifest_sha256'], 'Input manifest seal mismatch')
    inputs = parse_manifest(manifest_bytes)
    require(len(inputs) == 16, 'Expected exactly sixteen frozen inputs')
    require(set(files_under(packet/'INPUTS')) == set(inputs), 'Incomplete/extra input copy')
    for name, expected in inputs.items():
        require(digest(regular_bytes(packet/'INPUTS'/name, readonly)) == expected, 'Frozen input mismatch: '+name)
    archive_path = top/'ROUND_020_CONTINUOUS_PATH_HOSTILE_PACKET.tar.gz'
    archive_bytes = regular_bytes(archive_path, readonly)
    require(digest(archive_bytes) == seal['archive_sha256'] and len(archive_bytes) == seal['archive_bytes'],
            'Archive external digest/size mismatch')
    count = verify_archive(io.BytesIO(archive_bytes), archive_expected)
    require(count == seal['archive_members'], 'Archive count seal mismatch')
    diagnostic = json.loads(regular_bytes(packet/'diagnostic_results.json', readonly))
    code = regular_bytes(packet/'hostile_exact_diagnostic.py', readonly)
    require(diagnostic['script_sha256'] == digest(code) and diagnostic['status'] == 'PASS',
            'Diagnostic code/result provenance mismatch')
    rerun_status = 'not requested'
    if args.rerun_diagnostic:
        environment = dict(os.environ)
        environment['PYTHONDONTWRITEBYTECODE'] = '1'
        process = subprocess.run([sys.executable, str(packet/'hostile_exact_diagnostic.py')],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment,
                                 timeout=60, check=False)
        require(process.returncode == 0 and not process.stderr, 'Diagnostic rerun failed')
        require(process.stdout == regular_bytes(packet/'diagnostic_results.json', readonly),
                'Diagnostic rerun differs byte-for-byte')
        rerun_status = 'PASS: exact stdout reproduction'
    rejected = rejection_controls() if args.self_test_rejections else {}
    final_status = 'not checked during initial seal preparation'
    final_hash = None
    if not args.prepare_seal:
        final_file = top/'FINAL_SHA256SUMS.txt'
        final_bytes = regular_bytes(final_file, True)
        final = parse_manifest(final_bytes)
        all_outputs = {p.relative_to(top.parent).as_posix(): p for p in files_under(top).values()
                       if p != final_file}
        all_outputs[report.name] = report
        require(set(final) == set(all_outputs), 'Final output inventory is incomplete or has extras')
        for name, path in all_outputs.items():
            require(digest(regular_bytes(path, True)) == final[name], 'Final output byte mismatch: '+name)
        final_hash = digest(final_bytes)
        final_status = 'PASS: exact complete final inventory and read-only files'
    result = {
        'audit': 'AUD060',
        'status': 'PASS',
        'verification_class': 'Read-only exact-byte provenance; no analytic theorem certification.',
        'input_files_verified': len(inputs),
        'payload_files_verified_including_manifest': len(paths),
        'archive_members_verified_without_extraction': count,
        'archive_sha256': seal['archive_sha256'],
        'report_sha256': seal['report_sha256'],
        'diagnostic_assertions': diagnostic['assertions'],
        'diagnostic_mutations_rejected': diagnostic['mutation_count'],
        'diagnostic_rerun': rerun_status,
        'verifier_mutations_rejected': len(rejected),
        'verifier_rejection_reasons': rejected,
        'final_output_seal': final_status,
        'final_manifest_sha256': final_hash,
        'archive_extracted': False,
        'writes_performed': False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, json.JSONDecodeError, tarfile.TarError) as error:
        print('VERIFICATION FAILED: '+str(error), file=sys.stderr)
        raise SystemExit(1)
