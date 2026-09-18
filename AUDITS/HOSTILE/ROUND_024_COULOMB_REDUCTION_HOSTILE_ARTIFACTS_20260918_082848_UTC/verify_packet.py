#!/usr/bin/env python3
"""Read-only AUD068 packet verifier; stdlib only; never extracts or writes."""
from pathlib import Path, PurePosixPath
from fractions import Fraction
import argparse
import hashlib
import json
import os
import re
import stat
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    p = PurePosixPath(name)
    if not name or '\\' in name or p.is_absolute() or '..' in p.parts or '.' in p.parts:
        raise AssertionError(f"Unsafe member/path: {name!r}")
    if str(p) != name:
        raise AssertionError(f"Noncanonical member/path: {name!r}")
    return p


def regular_bytes(path):
    mode = path.lstat().st_mode
    assert stat.S_ISREG(mode), f"Not a regular file: {path}"
    assert stat.S_IMODE(mode) == 0o444, f"Not mode 0444: {path}"
    return path.read_bytes()


def parse_manifest(data):
    rows = {}
    for line in data.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, f"Malformed digest row: {line!r}"
        checksum, name = match.groups()
        safe_name(name)
        assert name not in rows, f"Duplicate digest entry: {name}"
        rows[name] = checksum
    assert rows, "Empty manifest"
    return rows


def walk_files(directory):
    members = set()
    for here, dirs, files in os.walk(directory, followlinks=False):
        here = Path(here)
        mode = here.lstat().st_mode
        assert stat.S_ISDIR(mode) and stat.S_IMODE(mode) == 0o555, f"Nonregular/writable directory: {here}"
        for item in dirs:
            p = here/item
            assert not p.is_symlink(), f"Symlink directory: {p}"
        for item in files:
            p = here/item
            regular_bytes(p)
            rel = p.relative_to(directory).as_posix()
            safe_name(rel)
            assert rel not in members
            members.add(rel)
    return members


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--seal', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    parent = packet.parent
    archive = args.archive or parent/(packet.name+'.zip')
    seal_path = args.seal or parent/(packet.name+'_SEAL.json')
    report = args.report or parent/'ROUND_024_COULOMB_REDUCTION_REVIEW.md'
    seal = json.loads(regular_bytes(seal_path))
    assert seal['format'] == 'AUD068_SHA256_SEAL_V1'
    assert seal['artifact_directory'] == packet.name
    assert seal['archive_name'] == archive.name
    assert seal['report_name'] == report.name

    manifest_data = regular_bytes(packet/'OUTPUT_SHA256SUMS.txt')
    member_data = regular_bytes(packet/'ARCHIVE_MEMBERS.txt')
    report_data = regular_bytes(report)
    archive_data = regular_bytes(archive)
    expected_seal = {
        'archive_sha256': digest(archive_data),
        'output_manifest_sha256': digest(manifest_data),
        'member_inventory_sha256': digest(member_data),
        'report_sha256': digest(report_data),
    }
    for key, value in expected_seal.items():
        assert seal[key] == value, f"External seal mismatch: {key}"

    hashes = parse_manifest(manifest_data)
    assert 'OUTPUT_SHA256SUMS.txt' not in hashes
    listed = member_data.decode('utf-8').splitlines()
    for name in listed:
        safe_name(name)
    assert listed == sorted(set(listed)), "Unsorted or duplicate archive inventory"
    expected = set(hashes) | {'OUTPUT_SHA256SUMS.txt'}
    assert set(listed) == expected, "Inventory/manifest membership mismatch"
    assert walk_files(packet) == expected, "Unexpected or missing packet members"
    for name, checksum in hashes.items():
        assert digest(regular_bytes(packet/name)) == checksum, f"Payload digest mismatch: {name}"
    assert regular_bytes(packet/'REVIEW.md') == report_data, "Report copy mismatch"

    inputs = parse_manifest(regular_bytes(packet/'INPUT_SHA256SUMS.txt'))
    assert len(inputs) == 24, "Wrong number of frozen inputs"
    assert {name for name in expected if name.startswith('inputs/')} == {'inputs/'+name for name in inputs}
    for name, checksum in inputs.items():
        assert digest(regular_bytes(packet/'inputs'/name)) == checksum, f"Frozen input mismatch: {name}"
    input_checks = json.loads(regular_bytes(packet/'INPUT_CHECKS.json'))
    assert input_checks['input_count'] == 24
    assert {x['path']:x['sha256'] for x in input_checks['inputs']} == inputs

    results = json.loads(regular_bytes(packet/'RESULTS.json'))
    assert results['code_sha256'] == digest(regular_bytes(packet/'hostile_diagnostic.py'))
    assert results['assertions'] == sum(results['counts'].values()) == 889
    assert results['mutation_count'] == len(results['mutations']) == 18
    for name, mutation in results['mutations'].items():
        witness = mutation['nonzero_residual']
        value = witness.get('coefficient', witness.get('value'))
        assert value is not None and Fraction(value) != 0, f"Vacuous mutation: {name}"

    with zipfile.ZipFile(archive) as z:
        entries = z.infolist()
        names = [x.filename for x in entries]
        assert len(names) == len(set(names)), "Duplicate archive members"
        assert set(names) == expected, "Unexpected/missing archive members"
        assert z.testzip() is None, "Archive CRC failure"
        for info in entries:
            safe_name(info.filename)
            assert not info.is_dir(), "Directory archive member"
            assert not info.flag_bits & 1, "Encrypted archive member"
            assert info.create_system == 3, "Missing Unix regular-file metadata"
            mode = info.external_attr >> 16
            assert stat.S_ISREG(mode) and stat.S_IMODE(mode) == 0o444, "Nonregular or writable archive member"
            data = z.read(info)
            assert len(data) == info.file_size
            assert data == regular_bytes(packet/info.filename), f"Archive byte mismatch: {info.filename}"

    print(json.dumps({
        'verdict': 'PASS_READ_ONLY_PACKET_VERIFICATION',
        'frozen_input_count': len(inputs),
        'packet_and_archive_member_count': len(expected),
        'recorded_diagnostic_assertions': results['assertions'],
        'nonzero_mutation_count': results['mutation_count'],
        'archive_sha256': expected_seal['archive_sha256'],
        'report_sha256': expected_seal['report_sha256'],
        'limitations': 'Integrity and recorded-witness verification; run hostile_diagnostic.py --check RESULTS.json separately to recompute diagnostic arithmetic. No source-gate or chronology authentication.'
    }, sort_keys=True))


if __name__ == '__main__':
    main()
