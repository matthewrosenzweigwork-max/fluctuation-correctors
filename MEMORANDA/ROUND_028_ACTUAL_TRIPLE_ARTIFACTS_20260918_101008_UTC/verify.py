#!/usr/bin/env python3
"""Portable read-only verifier. Never extracts an archive or writes a file."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tarfile


def need(condition, message):
    if not condition:
        raise ValueError(message)


def safe_name(name):
    need(isinstance(name, str) and bool(name), 'empty or non-string member')
    need('\\' not in name and '\x00' not in name, 'unsafe member separator')
    path = PurePosixPath(name)
    need(not path.is_absolute() and all(p not in ('', '.', '..') for p in name.split('/')),
         'unsafe member path: '+name)
    need(str(path) == name, 'noncanonical member path: '+name)
    return name


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rows_map(rows):
    result = {}
    need(isinstance(rows, list), 'inventory must be a list')
    for row in rows:
        name = safe_name(row['path'])
        need(name not in result, 'duplicate member: '+name)
        need(re.fullmatch(r'[0-9a-f]{64}', row['sha256']) is not None, 'invalid SHA-256')
        need(isinstance(row['size'], int) and row['size'] >= 0, 'invalid size')
        result[name] = row
    return result


def read_tree(packet):
    result = {}
    need(packet.is_dir() and not packet.is_symlink(), 'packet is not a real directory')
    for directory, dirs, names in os.walk(packet, followlinks=False):
        for name in dirs:
            path = Path(directory)/name
            need(not path.is_symlink(), 'symlink directory forbidden')
        for name in names:
            path = Path(directory)/name
            mode = path.lstat().st_mode
            need(stat.S_ISREG(mode), 'nonregular directory member forbidden')
            need(not mode & 0o222, 'issued member is writable: '+str(path))
            rel = safe_name(path.relative_to(packet).as_posix())
            result[rel] = path.read_bytes()
    return result


def check_rows(rows, contents, label):
    need(set(rows) == set(contents), label+' exact-member mismatch')
    for name, row in rows.items():
        data = contents[name]
        need(len(data) == row['size'], label+' size mismatch: '+name)
        need(digest(data) == row['sha256'], label+' digest mismatch: '+name)


def parse_sums(data):
    result = {}
    for line in data.decode('utf-8').splitlines():
        value, name = line.split('  ', 1)
        safe_name(name)
        need(name not in result, 'duplicate digest row')
        need(re.fullmatch(r'[0-9a-f]{64}', value) is not None, 'invalid digest row')
        result[name] = value
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('packet', nargs='?', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--members', type=Path)
    parser.add_argument('--run-diagnostic', action='store_true')
    parser.add_argument('--mutant', choices=('corrupt_digest', 'unsafe_member', 'duplicate_member'))
    args = parser.parse_args()
    packet = args.packet.resolve()
    archive = args.archive or Path(str(packet)+'.tar.gz')
    members = args.members or Path(str(packet)+'.MEMBERS.json')
    data = read_tree(packet)
    rows = json.loads(members.read_text())['files']
    if args.mutant == 'unsafe_member':
        safe_name('../escape')
    if args.mutant == 'duplicate_member':
        rows.append(dict(rows[0]))
    if args.mutant == 'corrupt_digest':
        rows[0]['sha256'] = '0'*64
    complete = rows_map(rows)
    check_rows(complete, data, 'complete inventory')
    inner = json.loads(data['INVENTORY.json'])
    control = {'INVENTORY.json', 'SHA256SUMS.txt'}
    check_rows(rows_map(inner['payload']), {k:v for k,v in data.items() if k not in control},
               'payload inventory')
    sums = parse_sums(data['SHA256SUMS.txt'])
    need(set(sums) == set(data)-{'SHA256SUMS.txt'}, 'complete internal digest coverage mismatch')
    for name, value in sums.items():
        need(digest(data[name]) == value, 'internal digest mismatch: '+name)
    sources = parse_sums(data['INPUT_SHA256SUMS.txt'])
    need(len(sources) == 21, 'input count differs from frozen 21')
    need({name[7:] for name in data if name.startswith('INPUTS/')} == set(sources),
         'input member set mismatch')
    for name, value in sources.items():
        need(digest(data['INPUTS/'+name]) == value, 'frozen input mismatch: '+name)
    archived = {}
    with tarfile.open(archive, 'r:gz') as handle:
        for member in handle.getmembers():
            name = safe_name(member.name)
            prefix = packet.name+'/'
            need(name.startswith(prefix), 'archive root differs from packet name')
            rel = safe_name(name[len(prefix):])
            need(rel not in archived, 'duplicate archive member')
            need(member.isreg() and not member.issym() and not member.islnk(),
                 'archive contains nonregular member')
            need(member.size <= 20*1024*1024, 'unexpectedly large archive member')
            need(not member.mode & 0o222, 'archive member writable')
            stream = handle.extractfile(member)
            need(stream is not None, 'archive member unreadable')
            archived[rel] = stream.read()
    need(set(archived) == set(data), 'archive exact-member mismatch')
    for name, contents in data.items():
        need(archived[name] == contents, 'archive/directory byte mismatch: '+name)
    diagnostic = None
    if args.run_diagnostic:
        run = subprocess.run([sys.executable, str(packet/'diagnostic.py')], cwd=packet,
                             capture_output=True, text=True)
        need(run.returncode == 0, 'fresh diagnostic failed: '+run.stderr)
        diagnostic = json.loads(run.stdout)
        need(diagnostic == json.loads(data['OUTPUTS/baseline.stdout']),
             'fresh diagnostic differs from saved exact result')
    print(json.dumps({'status': 'PASS', 'inputs': 21, 'regular_members': len(data),
                      'archive_regular_members': len(archived),
                      'diagnostic_assertions': diagnostic['assertions'] if diagnostic else None,
                      'read_only': True, 'archive_extracted': False}, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('VERIFICATION_REJECTED: '+str(exc), file=sys.stderr)
        sys.exit(1)
