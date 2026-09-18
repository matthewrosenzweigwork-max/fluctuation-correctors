#!/usr/bin/env python3
"""Portable read-only byte/member verifier. No extraction or filesystem writes."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tarfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_name(name):
    require(isinstance(name, str) and name, 'empty member name')
    require('\\' not in name and '\x00' not in name, 'unsafe member spelling')
    path = PurePosixPath(name)
    require(not path.is_absolute(), 'absolute member path')
    require(all(part not in ('', '.', '..') and ':' not in part for part in path.parts),
            'unsafe member component')
    require(path.as_posix() == name, 'noncanonical member path')
    return name


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rows(data):
    result = {}
    for line in data.decode('utf-8').splitlines():
        require(bool(line), 'blank digest row')
        pieces = line.split('  ', 1)
        require(len(pieces) == 2 and re.fullmatch('[0-9a-f]{64}', pieces[0]),
                'malformed digest row')
        name = safe_name(pieces[1])
        require(name not in result, 'duplicate digest name: ' + name)
        result[name] = pieces[0]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('packet', type=Path)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--seal', type=Path)
    parser.add_argument('--allow-writable', action='store_true',
                        help='pre-issuance check only; final checks omit this')
    parser.add_argument('--negative-control', choices=['digest', 'unsafe-member'])
    args = parser.parse_args()
    require(args.packet.is_dir() and not args.packet.is_symlink(),
            'packet is not a regular directory')
    root = args.packet.resolve()
    if args.negative_control == 'unsafe-member':
        safe_name('../escape')
        raise ValueError('unsafe-member control was not rejected')
    actual = {}
    for path in sorted(root.rglob('*')):
        require(not path.is_symlink(), 'symlink in packet: ' + str(path))
        if path.is_dir():
            continue
        require(path.is_file(), 'nonregular packet object: ' + str(path))
        name = safe_name(path.relative_to(root).as_posix())
        require(name not in actual, 'duplicate packet member')
        if not args.allow_writable:
            require(stat.S_IMODE(path.stat().st_mode) & 0o222 == 0,
                    'writable issued member: ' + name)
        actual[name] = path.read_bytes()
    require('MEMBERS.txt' in actual and 'PAYLOAD_SHA256SUMS.txt' in actual,
            'missing inventories')
    listed = actual['MEMBERS.txt'].decode('utf-8').splitlines()
    require(all(safe_name(x) == x for x in listed), 'invalid inventory')
    require(len(set(listed)) == len(listed), 'duplicate inventory row')
    require(set(listed) == set(actual), 'packet inventory membership mismatch')
    manifest = rows(actual['PAYLOAD_SHA256SUMS.txt'])
    require(set(manifest) == set(actual) - {'PAYLOAD_SHA256SUMS.txt'},
            'payload digest coverage mismatch')
    if args.negative_control == 'digest':
        first = sorted(manifest)[0]
        manifest[first] = ('0' if manifest[first][0] != '0' else '1') + manifest[first][1:]
    for name, expected in manifest.items():
        require(digest(actual[name]) == expected, 'payload digest mismatch: ' + name)
    inputs = rows(actual['INPUT_SHA256SUMS.txt'])
    require(len(inputs) == 17, 'expected exactly 17 permitted inputs')
    input_members = {name for name in actual if name.startswith('INPUTS/')}
    require(input_members == {'INPUTS/' + name for name in inputs},
            'copied input membership mismatch')
    for name, expected in inputs.items():
        require(digest(actual['INPUTS/' + name]) == expected,
                'source-copy digest mismatch: ' + name)
    archive_hash = None
    if args.archive:
        require(args.archive.is_file() and not args.archive.is_symlink(), 'invalid archive file')
        if not args.allow_writable:
            require(stat.S_IMODE(args.archive.stat().st_mode) & 0o222 == 0,
                    'writable issued archive')
        archive_hash = digest(args.archive.read_bytes())
        extracted_names = set()
        prefix = root.name + '/'
        with tarfile.open(args.archive, 'r:gz') as archive:
            for member in archive.getmembers():
                safe_name(member.name)
                require(member.isfile(), 'archive member is not regular: ' + member.name)
                require(member.name.startswith(prefix), 'wrong archive root')
                name = safe_name(member.name[len(prefix):])
                require(name not in extracted_names, 'duplicate archive member: ' + name)
                extracted_names.add(name)
                require(name in actual, 'unexpected archive member: ' + name)
                if not args.allow_writable:
                    require(member.mode & 0o222 == 0, 'writable archived member: ' + name)
                stream = archive.extractfile(member)
                require(stream is not None, 'unreadable archive member')
                contents = stream.read()
                require(contents == actual[name], 'archive byte mismatch: ' + name)
        require(extracted_names == set(actual), 'archive member coverage mismatch')
    if args.seal:
        require(args.seal.is_file() and not args.seal.is_symlink(), 'invalid seal')
        if not args.allow_writable:
            require(stat.S_IMODE(args.seal.stat().st_mode) & 0o222 == 0, 'writable issued seal')
        seal = json.loads(args.seal.read_text())
        require(seal['packet_directory'] == root.name, 'seal packet mismatch')
        require(seal['member_count'] == len(actual), 'seal member count mismatch')
        require(seal['payload_manifest_sha256'] == digest(actual['PAYLOAD_SHA256SUMS.txt']),
                'sealed payload-manifest mismatch')
        require(seal['member_inventory_sha256'] == digest(actual['MEMBERS.txt']),
                'sealed inventory mismatch')
        require(seal['report_sha256'] == digest(actual['REPORT.md']), 'sealed report mismatch')
        require(seal['claim_card_sha256'] == digest(actual['CLAIM_CARD.md']), 'sealed claim mismatch')
        if args.archive:
            require(seal['archive_filename'] == args.archive.name, 'sealed archive name mismatch')
            require(seal['archive_sha256'] == archive_hash, 'sealed archive digest mismatch')
    print(json.dumps({'status': 'PASS', 'packet_files': len(actual), 'input_files': len(inputs),
                      'payload_files_hashed': len(manifest),
                      'readonly_checked': not args.allow_writable,
                      'archive_checked': bool(args.archive), 'seal_checked': bool(args.seal),
                      'archive_sha256': archive_hash}, sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}, sort_keys=True))
        sys.exit(1)
