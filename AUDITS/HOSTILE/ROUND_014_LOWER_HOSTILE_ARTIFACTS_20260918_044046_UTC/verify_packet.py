#!/usr/bin/env python3
"""Verify TASK-076 frozen inputs, sealed outputs, and optional external archive."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rows(path):
    parsed = []
    for line in path.read_text().splitlines():
        expected, name = line.split('  ', 1)
        relative = PurePosixPath(name)
        assert not relative.is_absolute() and '..' not in relative.parts, name
        assert len(expected) == 64 and all(ch in '0123456789abcdef' for ch in expected)
        parsed.append((expected, name))
    assert len({name for _, name in parsed}) == len(parsed)
    return parsed


def main(require_archive, output):
    packet = Path(__file__).resolve().parent
    root = packet.parents[2]
    inputs = rows(packet/'INPUT_SHA256SUMS.txt')
    assert len(inputs) == 27
    for expected, name in inputs:
        assert digest((packet/'INPUTS'/name).read_bytes()) == expected, name
    outputs = rows(packet/'OUTPUT_SHA256SUMS.txt')
    for expected, name in outputs:
        assert digest((root/name).read_bytes()) == expected, name
    archive = packet/'SEALED_PACKET.zip'
    archive_checked = archive.exists()
    archive_members = 0
    archive_digest = None
    if require_archive:
        assert archive_checked, 'External archive is required but absent.'
    if archive_checked:
        archive_digest = digest(archive.read_bytes())
        expected_members = {name for _, name in outputs}
        expected_members.add((packet/'OUTPUT_SHA256SUMS.txt').relative_to(root).as_posix())
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
            assert len(names) == len(set(names)), 'Duplicate archive members'
            assert set(names) == expected_members, 'Unexpected or missing archive members'
            assert bundle.testzip() is None, 'Archive CRC failure'
            for name in names:
                relative = PurePosixPath(name)
                assert not relative.is_absolute() and '..' not in relative.parts, name
                assert not bundle.getinfo(name).is_dir()
                assert digest(bundle.read(name)) == digest((root/name).read_bytes()), name
            archive_members = len(names)
    seal = packet/'SEAL_SHA256SUMS.txt'
    seal_checked = seal.exists()
    seal_entries = 0
    if seal_checked:
        sealed = rows(seal)
        for expected, name in sealed:
            assert digest((root/name).read_bytes()) == expected, name
        seal_entries = len(sealed)
    result = {
        'status': 'PASS', 'task': 'TASK-076', 'frozen_inputs_verified': len(inputs),
        'sealed_outputs_verified': len(outputs), 'archive_checked': archive_checked,
        'archive_member_count': archive_members, 'archive_sha256': archive_digest,
        'external_seal_checked': seal_checked, 'external_seal_entries': seal_entries,
        'checks': ['safe relative paths', 'no duplicate manifest entries',
                   'input SHA-256', 'output SHA-256', 'exact archive membership when present',
                   'archive CRC when present', 'all archive member SHA-256 when present',
                   'external seal SHA-256 when present'],
    }
    if output is not None:
        assert not output.exists(), 'Verification output must be a new file.'
        output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--require-archive', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    main(args.require_archive, args.output)
