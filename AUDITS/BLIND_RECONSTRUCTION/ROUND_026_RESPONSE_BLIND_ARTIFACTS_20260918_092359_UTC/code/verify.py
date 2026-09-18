#!/usr/bin/env python3
"""Portable read-only integrity/reproduction verifier for this audit packet.

It never extracts the archive, writes files, accesses a repository, imports
project modules, installs dependencies, or uses the network. Python 3.8+.
"""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tarfile


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and '\\' not in name,
            'unsafe relative name: '+repr(name))
    require(all(part not in ('', '.', '..') for part in p.parts),
            'unsafe relative component: '+repr(name))
    require(str(p) == name, 'noncanonical relative name: '+repr(name))
    return name


def hash_manifest(path):
    require(stat.S_ISREG(path.lstat().st_mode), 'manifest is not a regular file')
    rows = {}
    for line in path.read_text().splitlines():
        h, name = line.split('  ', 1)
        safe_relative(name)
        require(len(h) == 64 and all(c in '0123456789abcdef' for c in h),
                'invalid SHA256 digest')
        require(name not in rows, 'duplicate manifest name')
        rows[name] = h
    return rows


def verify():
    packet = Path(__file__).absolute().parent.parent
    require(not packet.is_symlink(), 'packet root must not be a symlink')
    parent, stem = packet.parent, packet.name
    inventory_path = parent/(stem+'.FILES.json')
    archive_path = parent/(stem+'.tar.gz')
    outer_manifest = parent/(stem+'.SHA256SUMS.txt')
    report_path = parent/'ROUND_026_RESPONSE_RECONSTRUCTION.md'
    external = hash_manifest(outer_manifest)
    required = {stem+'.FILES.json', stem+'.tar.gz', stem+'.SEAL.md', report_path.name}
    allowed = required | {stem+'.VERIFY.json'}
    require(required <= set(external) <= allowed, 'external manifest membership differs')
    for name, expected in external.items():
        require('/' not in name, 'external member must be a sibling basename')
        path = parent/name
        require(stat.S_ISREG(path.lstat().st_mode), 'external member is not regular: '+name)
        require(digest(path.read_bytes()) == expected, 'external hash mismatch: '+name)

    inventory = json.loads(inventory_path.read_text())
    require(inventory['packet'] == stem, 'packet name differs from inventory')
    entries = inventory['regular_members']
    expected = {}
    for entry in entries:
        name = safe_relative(entry['path'])
        require(name not in expected, 'duplicate inventory member')
        require(entry['mode'] == '0444', 'inventory member must be read-only')
        expected[name] = entry
    actual = set()
    for base, dirs, files in os.walk(packet, followlinks=False):
        base_path = Path(base)
        require(stat.S_ISDIR(base_path.lstat().st_mode), 'non-directory in packet walk')
        require((base_path.stat().st_mode & 0o222) == 0, 'packet directory is writable')
        for name in dirs:
            require(stat.S_ISDIR((base_path/name).lstat().st_mode), 'directory link in packet')
        for name in files:
            path = base_path/name
            metadata = path.lstat()
            require(stat.S_ISREG(metadata.st_mode), 'nonregular filesystem member')
            rel = safe_relative(path.relative_to(packet).as_posix())
            require(rel in expected, 'unexpected filesystem member: '+rel)
            entry = expected[rel]
            require(stat.S_IMODE(metadata.st_mode) == 0o444, 'member is not mode 0444: '+rel)
            require(metadata.st_size == entry['bytes'], 'filesystem size mismatch: '+rel)
            require(digest(path.read_bytes()) == entry['sha256'], 'filesystem hash mismatch: '+rel)
            actual.add(rel)
    require(actual == set(expected), 'filesystem member set is incomplete')

    inner = hash_manifest(packet/'SHA256SUMS.txt')
    require(set(inner) == actual-{'SHA256SUMS.txt'}, 'inner manifest completeness failed')
    for name, expected_hash in inner.items():
        require(expected[name]['sha256'] == expected_hash, 'inner manifest hash mismatch: '+name)
    inputs = hash_manifest(packet/'INPUT_SHA256SUMS.txt')
    require(len(inputs) == 8, 'expected exactly eight sealed inputs')
    for name, input_hash in inputs.items():
        require(expected['inputs/'+name]['sha256'] == input_hash,
                'sealed input mismatch: '+name)

    # Read every member; no extraction, symbolic links, hardlinks or directories.
    archive_names = set()
    with tarfile.open(archive_path, 'r:gz') as archive:
        for member in archive:
            name = safe_relative(member.name)
            require(name.startswith(stem+'/'), 'archive member has unexpected root')
            rel = safe_relative(name[len(stem)+1:])
            require(rel not in archive_names, 'duplicate archive member')
            require(member.type == tarfile.REGTYPE and member.isfile(),
                    'archive member is not a plain regular file')
            require(not member.linkname, 'archive member contains a link target')
            require(rel in expected, 'unexpected archive member: '+rel)
            require(member.mode == 0o444, 'archive mode differs')
            data = archive.extractfile(member).read()
            require(len(data) == member.size == expected[rel]['bytes'], 'archive size mismatch')
            require(digest(data) == expected[rel]['sha256'], 'archive content hash mismatch: '+rel)
            archive_names.add(rel)
    require(archive_names == actual, 'archive does not contain every regular member')
    require(report_path.read_bytes() == (packet/'RECONSTRUCTION.md').read_bytes(),
            'assigned report and packet report differ')

    env = dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    result = subprocess.run([sys.executable, '-B', str(packet/'code'/'diagnostic.py')],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, env=env, check=False)
    require(result.returncode == 0 and result.stderr == '', 'fresh diagnostic execution failed')
    observed = json.loads(result.stdout)
    recorded = json.loads((packet/'results'/'diagnostic.json').read_text())
    require(observed == recorded, 'diagnostic result not exactly reproducible')
    require(observed['status'] == 'PASS' and observed['baseline_failures'] == [],
            'diagnostic baseline failed')
    require(observed['all_mutants_nonzero'] and observed['mutant_count'] > 0,
            'missing mutation controls')
    return {'status':'PASS', 'packet':stem, 'input_count':len(inputs),
            'regular_member_count':len(actual), 'archive_member_count':len(archive_names),
            'safe_regular_only_archive':True, 'complete_inventory':True,
            'packet_read_only':True, 'verifier_writes_files':False,
            'diagnostic_checks':observed['check_count'],
            'detected_nonzero_mutants':observed['mutant_count'],
            'archive_sha256':digest(archive_path.read_bytes()),
            'inventory_sha256':digest(inventory_path.read_bytes()),
            'report_sha256':digest(report_path.read_bytes())}


if __name__ == '__main__':
    try:
        print(json.dumps(verify(), indent=2, sort_keys=True))
    except Exception as error:
        print(json.dumps({'status':'FAIL','error':str(error)},indent=2),file=sys.stderr)
        raise SystemExit(1)
