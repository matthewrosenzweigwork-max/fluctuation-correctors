#!/usr/bin/env python3
"""Verify AUD051 payload hashes and, optionally, exact safe ZIP contents."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    path = PurePosixPath(name)
    return (not path.is_absolute() and bool(path.parts)
            and all(part not in ('', '.', '..') for part in path.parts)
            and '\\' not in name and '\x00' not in name
            and str(path) == name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    checksum_file = folder / 'OUTPUT_SHA256SUMS.txt'
    listed = {}
    for line in checksum_file.read_text().splitlines():
        expected, rel = line.split('  ', 1)
        assert safe_relative(rel), 'unsafe output manifest path: ' + rel
        assert rel not in listed, 'duplicate output manifest path: ' + rel
        assert len(expected) == 64 and all(c in '0123456789abcdef' for c in expected)
        listed[rel] = expected
    actual_paths = {}
    for path in folder.rglob('*'):
        assert not path.is_symlink(), 'symlink in packet: ' + str(path)
        if path.is_file():
            rel = path.relative_to(folder).as_posix()
            assert safe_relative(rel), 'unsafe actual output path: ' + rel
            actual_paths[rel] = path
    assert set(actual_paths) == set(listed) | {'OUTPUT_SHA256SUMS.txt'}, 'payload member mismatch'
    for rel, expected in listed.items():
        assert digest(actual_paths[rel].read_bytes()) == expected, 'payload hash mismatch: ' + rel

    input_count = 0
    for line in (folder / 'INPUT_SHA256SUMS.txt').read_text().splitlines():
        expected, rel = line.split('  ', 1)
        assert safe_relative(rel), 'unsafe input path: ' + rel
        assert digest((folder / 'inputs' / rel).read_bytes()) == expected, 'input mismatch: ' + rel
        input_count += 1
    assert input_count == 9
    expected_manifest, manifest_name = (folder / 'INPUT_MANIFEST_SHA256.txt').read_text().strip().split('  ', 1)
    assert manifest_name == 'INPUT_SHA256SUMS.txt'
    assert digest((folder / manifest_name).read_bytes()) == expected_manifest
    result = {'status': 'PASS', 'payload_file_count': len(actual_paths),
              'hashed_payload_file_count': len(listed), 'input_count': input_count,
              'output_manifest_sha256': digest(checksum_file.read_bytes())}
    if args.archive:
        archive = args.archive.resolve()
        expected_names = {folder.name + '/' + rel for rel in actual_paths}
        with zipfile.ZipFile(archive) as zf:
            infos = zf.infolist()
            names = [info.filename for info in infos]
            assert len(names) == len(set(names)), 'duplicate ZIP member'
            assert set(names) == expected_names, 'ZIP member set mismatch'
            assert zf.testzip() is None, 'ZIP CRC failure'
            for info in infos:
                assert safe_relative(info.filename), 'unsafe ZIP member'
                assert not info.is_dir(), 'unexpected directory entry'
                mode = info.external_attr >> 16
                assert not stat.S_ISLNK(mode), 'symlink ZIP member'
                rel = info.filename[len(folder.name) + 1:]
                data = zf.read(info)
                assert data == actual_paths[rel].read_bytes(), 'ZIP byte mismatch: ' + rel
                assert info.file_size == len(data), 'ZIP size mismatch: ' + rel
        result.update({'archive': str(archive), 'archive_member_count': len(names),
                       'archive_sha256': digest(archive.read_bytes()),
                       'archive_bytes': archive.stat().st_size,
                       'safe_paths': True, 'exact_members': True,
                       'exact_bytes': True, 'crc_pass': True, 'no_symlinks': True})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
