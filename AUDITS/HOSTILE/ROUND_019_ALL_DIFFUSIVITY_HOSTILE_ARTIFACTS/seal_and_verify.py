#!/usr/bin/env python3
"""Create or read-only verify the bounded AUD058 packet; never extract archives."""
from pathlib import Path, PurePosixPath
import argparse
import gzip
import hashlib
import io
import json
import os
import stat
import subprocess
import sys
import tarfile

PACKET = Path(__file__).resolve().parent
EXTERNAL_REPORT = PACKET.parent / 'ROUND_019_ALL_DIFFUSIVITY_REVIEW.md'
PREFIX = 'ROUND_019_ALL_DIFFUSIVITY_HOSTILE_ARTIFACTS/'
GENERATED = {
    'OUTPUT_SHA256SUMS.txt', 'SEALED_PACKET.tar.gz',
    'ARCHIVE_SHA256SUMS.txt', 'SEAL_VERIFICATION.json', 'HANDOFF_SHA256SUMS.txt'
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or str(p) != name or '\\' in name:
        raise AssertionError('Unsafe or noncanonical name: ' + name)
    if not p.parts or any(part in ('', '.') for part in p.parts):
        raise AssertionError('Empty path component: ' + name)
    return name


def files():
    found = []
    for p in PACKET.rglob('*'):
        if p.is_symlink():
            raise AssertionError('Symlink in packet: ' + str(p))
        if p.is_file():
            if not stat.S_ISREG(p.stat().st_mode):
                raise AssertionError('Nonregular payload: ' + str(p))
            found.append(safe_name(p.relative_to(PACKET).as_posix()))
        elif not p.is_dir():
            raise AssertionError('Special filesystem entry: ' + str(p))
    return sorted(found)


def parse_manifest(data):
    rows = {}
    for line in data.decode('utf-8').splitlines():
        digest, name = line.split('  ', 1)
        safe_name(name)
        if len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
            raise AssertionError('Invalid digest')
        if name in rows:
            raise AssertionError('Duplicate manifest name: ' + name)
        rows[name] = digest
    return rows


def manifest_for(names):
    return ''.join(sha((PACKET / name).read_bytes()) + '  ' + name + '\n'
                   for name in sorted(names)).encode('utf-8')


def verify_inputs(check_overlay=False):
    rows = parse_manifest((PACKET / 'INPUT_SHA256SUMS.txt').read_bytes())
    assert len(rows) == 15
    copied = sorted(name[7:] for name in files() if name.startswith('INPUTS/'))
    assert copied == sorted(rows)
    for name, digest in rows.items():
        assert sha((PACKET / 'INPUTS' / name).read_bytes()) == digest, name
        if check_overlay:
            assert sha((PACKET.parents[2] / name).read_bytes()) == digest, name
    return rows


def verify_payload():
    rows = parse_manifest((PACKET / 'OUTPUT_SHA256SUMS.txt').read_bytes())
    payload = sorted(name for name in files() if name not in GENERATED)
    assert sorted(rows) == payload
    for name, digest in rows.items():
        assert sha((PACKET / name).read_bytes()) == digest, name
    assert EXTERNAL_REPORT.is_file() and not EXTERNAL_REPORT.is_symlink()
    assert (PACKET / 'REPORT.md').read_bytes() == EXTERNAL_REPORT.read_bytes()
    return rows


def verify_archive(payload_rows):
    expected = sorted(list(payload_rows) + ['OUTPUT_SHA256SUMS.txt'])
    archive = PACKET / 'SEALED_PACKET.tar.gz'
    seen = set()
    total = 0
    with tarfile.open(archive, 'r:gz') as tf:
        for member in tf:
            safe_name(member.name)
            assert member.name.startswith(PREFIX)
            rel = safe_name(member.name[len(PREFIX):])
            assert rel not in seen, rel
            assert member.isfile() and not member.issym() and not member.islnk()
            assert member.mode == 0o444
            assert member.uid == member.gid == member.mtime == 0
            assert set(member.pax_headers) <= {'path'}
            if 'path' in member.pax_headers:
                assert member.pax_headers['path'] == member.name
            assert rel in expected, rel
            actual = tf.extractfile(member).read()
            desired = (PACKET / rel).read_bytes()
            assert member.size == len(desired) and actual == desired, rel
            seen.add(rel)
            total += len(actual)
    assert sorted(seen) == expected
    seal = parse_manifest((PACKET / 'ARCHIVE_SHA256SUMS.txt').read_bytes())
    assert seal == {'SEALED_PACKET.tar.gz': sha(archive.read_bytes())}
    return len(seen), total


def reproduce():
    result = subprocess.run([sys.executable, str(PACKET / 'fresh_exact_diagnostic.py')],
                            capture_output=True, check=True, timeout=60)
    assert result.stderr == b''
    assert result.stdout == (PACKET / 'DIAGNOSTIC_RESULTS.json').read_bytes()
    parsed = json.loads(result.stdout)
    assert parsed['assertions'] == 7564
    assert len(parsed['assertions_by_category']) == 40
    assert parsed['mutation_rejections'] == 879 and parsed['mutation_families'] == 24
    return parsed


def verification_record(check_overlay=False):
    inputs = verify_inputs(check_overlay)
    payload = verify_payload()
    members, total = verify_archive(payload)
    diagnostic = reproduce()
    return {
        'audit': 'AUD058 / TASK089',
        'status': 'PASS complete byte, archive-safety, and exact reproduction checks',
        'base_commit': 'e75f8b780682a7e9fb0715b5e8b5873be684a2e8',
        'input_count': len(inputs),
        'payload_count': len(payload),
        'archive_regular_file_count': members,
        'archive_payload_bytes': total,
        'source_overlay_hashes_checked_at_issuance': True,
        'archive_safety': 'Exact safe complete member set; regular files only; no extraction; every byte compared',
        'reproduction': 'Byte-identical stdout; empty stderr; Python ' + diagnostic['python'],
        'exact_assertions': diagnostic['assertions'],
        'assertion_categories': len(diagnostic['assertions_by_category']),
        'mutation_rejections': diagnostic['mutation_rejections'],
        'mutation_families': diagnostic['mutation_families'],
        'report_sha256': sha(EXTERNAL_REPORT.read_bytes()),
        'input_manifest_sha256': sha((PACKET / 'INPUT_SHA256SUMS.txt').read_bytes()),
        'output_manifest_sha256': sha((PACKET / 'OUTPUT_SHA256SUMS.txt').read_bytes()),
        'archive_sha256': sha((PACKET / 'SEALED_PACKET.tar.gz').read_bytes()),
        'diagnostic_program_sha256': sha((PACKET / 'fresh_exact_diagnostic.py').read_bytes()),
        'diagnostic_result_sha256': sha((PACKET / 'DIAGNOSTIC_RESULTS.json').read_bytes()),
        'readonly': 'Every final artifact file and external report has mode 0444; every artifact directory has mode 0555; checked after sealing',
        'scope': 'Hostile handoff only; no source-gate matching, separate-axis comparison, or canonical integration'
    }


def verify_readonly():
    assert stat.S_IMODE(EXTERNAL_REPORT.stat().st_mode) == 0o444
    assert stat.S_IMODE(PACKET.stat().st_mode) == 0o555
    for p in PACKET.rglob('*'):
        mode = stat.S_IMODE(p.stat().st_mode)
        assert mode == (0o555 if p.is_dir() else 0o444), str(p)


def verify_outer():
    rows = parse_manifest((PACKET / 'HANDOFF_SHA256SUMS.txt').read_bytes())
    expected = sorted(name for name in files() if name != 'HANDOFF_SHA256SUMS.txt')
    assert sorted(rows) == expected
    for name, digest in rows.items():
        assert sha((PACKET / name).read_bytes()) == digest, name


def seal():
    assert not any((PACKET / name).exists() for name in GENERATED), 'An issued seal already exists'
    verify_inputs(check_overlay=True)
    assert (PACKET / 'REPORT.md').read_bytes() == EXTERNAL_REPORT.read_bytes()
    payload = files()
    (PACKET / 'OUTPUT_SHA256SUMS.txt').write_bytes(manifest_for(payload))
    members = sorted(payload + ['OUTPUT_SHA256SUMS.txt'])
    with (PACKET / 'SEALED_PACKET.tar.gz').open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode='w', format=tarfile.PAX_FORMAT) as tf:
                for name in members:
                    data = (PACKET / name).read_bytes()
                    info = tarfile.TarInfo(PREFIX + name)
                    info.size, info.mode, info.mtime = len(data), 0o444, 0
                    info.uid = info.gid = 0
                    info.uname = info.gname = ''
                    tf.addfile(info, io.BytesIO(data))
    (PACKET / 'ARCHIVE_SHA256SUMS.txt').write_bytes(manifest_for(['SEALED_PACKET.tar.gz']))
    record = verification_record(check_overlay=True)
    (PACKET / 'SEAL_VERIFICATION.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    (PACKET / 'HANDOFF_SHA256SUMS.txt').write_bytes(manifest_for(files()))
    for name in files():
        (PACKET / name).chmod(0o444)
    directories = [p for p in PACKET.rglob('*') if p.is_dir()]
    for p in sorted(directories, key=lambda p: len(p.parts), reverse=True):
        p.chmod(0o555)
    PACKET.chmod(0o555)
    EXTERNAL_REPORT.chmod(0o444)
    verify_outer()
    verify_readonly()
    emit(record)


def emit(record):
    print(json.dumps({**record,
                      'handoff_manifest_sha256': sha((PACKET / 'HANDOFF_SHA256SUMS.txt').read_bytes()),
                      'final_file_count': len(files()),
                      'readonly_modes_verified': True}, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--seal', action='store_true')
    mode.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    if args.seal:
        seal()
    else:
        record = verification_record()
        assert json.loads((PACKET / 'SEAL_VERIFICATION.json').read_text()) == record
        verify_outer()
        verify_readonly()
        emit(record)


if __name__ == '__main__':
    main()
