#!/usr/bin/env python3
"""Verify an AUD079 packet and optional tar.gz without modifying either.

Usage: python3 verify_readonly.py [--archive PATH] [--replay]
No extraction, network, installation, cache creation or packet writes.
An external SHA256 seal must be compared independently for authentication.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tarfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    p = PurePosixPath(name)
    assert name and not p.is_absolute() and str(p) == name
    assert all(part not in ('', '.', '..') for part in p.parts)
    assert '\\' not in name and '\x00' not in name
    return p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    inventory_bytes = (root/'INVENTORY.json').read_bytes()
    manifest_bytes = (root/'PAYLOAD_SHA256.json').read_bytes()
    inventory = json.loads(inventory_bytes)
    manifest = json.loads(manifest_bytes)
    members = inventory['regular_members']
    assert members == sorted(set(members))
    for path in members:
        safe_relative(path)
    observed = []
    for current, dirs, files in os.walk(root, followlinks=False):
        for directory in dirs:
            assert not (Path(current)/directory).is_symlink(), 'directory symlink'
        for filename in files:
            path = Path(current)/filename
            info = path.lstat()
            assert stat.S_ISREG(info.st_mode), str(path)
            assert not (info.st_mode & 0o222), ('writable evidence', str(path))
            observed.append(path.relative_to(root).as_posix())
    assert sorted(observed) == members, 'incomplete or unexpected regular-member inventory'
    assert set(manifest) == set(members)-{'INVENTORY.json', 'PAYLOAD_SHA256.json'}
    for relative, record in manifest.items():
        data = (root/relative).read_bytes()
        assert len(data) == record['bytes'] and digest(data) == record['sha256'], relative
    exact_inputs = 0
    for line in (root/'RECORDS/INPUT_SHA256SUMS.txt').read_text().splitlines():
        expected, relative = line.split('  ', 1)
        safe_relative(relative)
        assert digest((root/'INPUTS'/relative).read_bytes()) == expected, relative
        exact_inputs += 1
    assert exact_inputs == 18
    result = {'status': 'PASS', 'regular_member_count': len(members),
              'payload_hash_count': len(manifest), 'exact_input_count': exact_inputs,
              'inventory_sha256': digest(inventory_bytes),
              'payload_manifest_sha256': digest(manifest_bytes),
              'report_sha256': digest((root/'REPORT.md').read_bytes()),
              'writes_performed': False}
    if args.archive:
        archive_members = {}
        with tarfile.open(args.archive, 'r:gz') as tf:
            for member in tf:
                assert member.isfile() and not member.issym() and not member.islnk()
                path = safe_relative(member.name)
                assert path.parts[0] == root.name and len(path.parts) > 1
                relative = PurePosixPath(*path.parts[1:]).as_posix()
                assert relative not in archive_members, ('duplicate', relative)
                assert not (member.mode & 0o222), ('writable archive member', relative)
                stream = tf.extractfile(member)
                assert stream is not None
                data = stream.read()
                assert len(data) == member.size
                archive_members[relative] = (len(data), digest(data))
        assert sorted(archive_members) == members, 'archive inventory mismatch'
        for relative, (size, sha) in archive_members.items():
            local = (root/relative).read_bytes()
            assert len(local) == size and digest(local) == sha, relative
        result.update({'archive_regular_member_count': len(archive_members),
                       'archive_sha256': digest(args.archive.read_bytes())})
    if args.replay:
        env = dict(os.environ)
        env['PYTHONDONTWRITEBYTECODE'] = '1'
        execution = subprocess.run([sys.executable, str(root/'CODE/diagnostic.py')],
                                   capture_output=True, text=True, env=env, cwd=root)
        assert execution.returncode == 0, execution.stderr
        fresh = json.loads(execution.stdout)
        expected = json.loads((root/'OUTPUTS/expected_result.json').read_text())
        for key in ['status', 'check_count', 'checks_by_category', 'mutation_count']:
            assert fresh[key] == expected[key], key
        actual_mutations = fresh['nonzero_mutations']
        expected_mutations = expected['nonzero_mutations']
        assert [x['name'] for x in actual_mutations] == [x['name'] for x in expected_mutations]
        for actual, old in zip(actual_mutations, expected_mutations):
            if actual['kind'] == 'exact':
                assert actual == old
        result.update({'fresh_replay_status': fresh['status'],
                       'fresh_replay_check_count': fresh['check_count'],
                       'fresh_replay_nonzero_mutation_count': fresh['mutation_count']})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
