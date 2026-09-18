#!/usr/bin/env python3
"""Read-only portable verifier for this issued reconstruction packet."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import os
import stat
import subprocess
import sys
import tarfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    p = PurePosixPath(name)
    return (bool(name) and not p.is_absolute() and '\\' not in name
            and all(part not in ('', '.', '..') for part in name.split('/')))


def read_regular(path):
    info = path.lstat()
    assert stat.S_ISREG(info.st_mode), 'Not a regular file: '+str(path)
    assert info.st_mode & 0o222 == 0, 'Writable issued file: '+str(path)
    return path.read_bytes()


def main():
    if len(sys.argv) != 1:
        raise SystemExit('Run this verifier with no arguments beside its sealed packet.')
    packet = Path(__file__).resolve().parent
    parent = packet.parent
    stem = packet.name
    manifest_path = packet/'PAYLOAD_MANIFEST.json'
    manifest_bytes = read_regular(manifest_path)
    manifest = json.loads(manifest_bytes)
    listed = manifest['files']
    expected = set(listed) | {'PAYLOAD_MANIFEST.json'}
    observed = set()
    for path in packet.rglob('*'):
        mode = path.lstat().st_mode
        assert not stat.S_ISLNK(mode), 'Symlink: '+str(path)
        assert mode & 0o222 == 0, 'Writable issued path: '+str(path)
        if stat.S_ISDIR(mode):
            continue
        assert stat.S_ISREG(mode), 'Special file: '+str(path)
        observed.add(path.relative_to(packet).as_posix())
    assert observed == expected, 'Missing or unexpected payload member'
    assert packet.stat().st_mode & 0o222 == 0, 'Writable packet directory'
    for rel, metadata in listed.items():
        assert safe_relative(rel), 'Unsafe payload path'
        content = read_regular(packet/rel)
        assert digest(content) == metadata['sha256'], 'Payload hash mismatch: '+rel
        assert len(content) == metadata['bytes'], 'Payload length mismatch: '+rel

    input_paths = set()
    for filename, expected_count in (
        ('ROUND_025_SOURCE_UI_BLIND_INPUT_SHA256SUMS.txt', 11),
        ('ROUND_025_SOURCE_UI_BLIND_ADDENDUM_SHA256SUMS.txt', 2)):
        lines = (packet/'PERMITTED_INPUTS'/filename).read_text().splitlines()
        assert len(lines) == expected_count
        for line in lines:
            checksum, rel = line.split('  ', 1)
            assert safe_relative(rel) and rel not in input_paths
            input_paths.add(rel)
            assert digest(read_regular(packet/'PERMITTED_INPUTS'/rel)) == checksum
    assert len(input_paths) == 13

    external_report = parent/'ROUND_025_SOURCE_UI_RECONSTRUCTION.md'
    report = read_regular(external_report)
    assert report == read_regular(packet/'REPORT.md'), 'External report differs'
    archive_path = parent/(stem+'.tar.gz')
    inventory_path = parent/(stem+'_ARCHIVE_MEMBERS.json')
    seal_path = parent/(stem+'_SEAL.json')
    seal = json.loads(read_regular(seal_path))
    archive_bytes = read_regular(archive_path)
    inventory_bytes = read_regular(inventory_path)
    assert digest(archive_bytes) == seal['archive_sha256'], 'Archive seal mismatch'
    assert digest(inventory_bytes) == seal['archive_inventory_sha256'], 'Inventory seal mismatch'
    assert digest(manifest_bytes) == seal['payload_manifest_sha256'], 'Manifest seal mismatch'
    assert digest(report) == seal['external_report_sha256'], 'Report seal mismatch'
    inventory = json.loads(inventory_bytes)
    actual_inventory = []
    member_names = set()
    with tarfile.open(archive_path, 'r:gz') as archive:
        members = archive.getmembers()
        for member in members:
            assert safe_relative(member.name), 'Unsafe archive name'
            assert member.name not in member_names, 'Duplicate archive member'
            member_names.add(member.name)
            assert member.isfile(), 'Nonregular archive member'
            assert not (member.mode & 0o222), 'Writable archived member'
            prefix = stem+'/'
            assert member.name.startswith(prefix), 'Wrong archive prefix'
            rel = member.name[len(prefix):]
            assert rel in expected, 'Unexpected archive member'
            extracted = archive.extractfile(member)
            assert extracted is not None
            content = extracted.read()
            assert content == read_regular(packet/rel), 'Archive bytes differ: '+rel
            assert member.size == len(content)
            actual_inventory.append({'name':member.name, 'bytes':len(content), 'sha256':digest(content)})
    actual_inventory.sort(key=lambda row:row['name'])
    assert member_names == {stem+'/'+rel for rel in expected}, 'Incomplete archive'
    assert actual_inventory == inventory['members'], 'Archive inventory mismatch'

    environment = dict(os.environ)
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    run = subprocess.run([sys.executable, '-B', str(packet/'fresh_exact_diagnostic.py')],
                         cwd=packet, text=True, capture_output=True, check=True, env=environment)
    replay = json.loads(run.stdout)
    recorded = json.loads(read_regular(packet/'diagnostic_results.json'))
    assert replay == recorded, 'Diagnostic replay differs'
    assert replay['status'] == 'PASS'
    assert replay['total_assertions'] == 2203
    assert len(replay['mutation_nonzero_case_counts']) == 16
    assert min(replay['mutation_nonzero_case_counts'].values()) > 0
    verdict = json.loads(read_regular(packet/'verdict.json'))
    assert verdict['THM048'] == verdict['THM049'] == verdict['joint'] == 'RECONSTRUCTED'
    assert verdict['THM046'] == 'OPEN'
    print(json.dumps({
        'status':'PASS', 'permitted_input_count':len(input_paths),
        'payload_member_count':len(expected), 'archive_member_count':len(member_names),
        'archive_sha256':digest(archive_bytes), 'report_sha256':digest(report),
        'diagnostic_assertions':replay['total_assertions'], 'nonzero_mutation_families':16,
        'read_only_issued_modes':True, 'archive_safe_unique_regular_members':True,
        'diagnostic_replay_equal':True, 'mathematical_promotion':'None; integrity and diagnostic checks only'
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
