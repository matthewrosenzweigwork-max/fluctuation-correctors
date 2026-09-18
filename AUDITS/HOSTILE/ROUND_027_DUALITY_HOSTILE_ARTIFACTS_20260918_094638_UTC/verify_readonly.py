#!/usr/bin/env python3
"""Portable AUD076 integrity/replay verifier. Reads only; never extracts/writes.

Requires this packet, the assigned sibling report and named archive/seals.
Python 3.8+ standard library. --pre-receipt is the one issuance-time phase before
the verification receipt and detached final digest file are written.
"""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tarfile


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    p = PurePosixPath(name)
    return (bool(name) and not p.is_absolute() and '\\' not in name
            and all(part not in ('', '.', '..') for part in name.split('/'))
            and p.as_posix() == name)


def check_regular(path):
    mode = path.lstat().st_mode
    require(stat.S_ISREG(mode), 'not a regular file: ' + str(path))
    require(not mode & 0o222, 'issued file is writable: ' + str(path))


def walk_packet(base):
    rows = []
    for folder, directories, files in os.walk(str(base), followlinks=False):
        folder_path = Path(folder)
        mode = folder_path.lstat().st_mode
        require(stat.S_ISDIR(mode) and not mode & 0o222,
                'packet directory is not a read-only real directory: ' + str(folder_path))
        for name in directories:
            mode = (folder_path/name).lstat().st_mode
            require(stat.S_ISDIR(mode), 'linked/non-directory child: ' + str(folder_path/name))
        for name in files:
            path = folder_path/name
            check_regular(path)
            relative = path.relative_to(base).as_posix()
            require(safe_relative(relative), 'unsafe directory-relative name')
            raw = path.read_bytes()
            rows.append({'path': relative, 'size': len(raw), 'sha256': digest(raw)})
    return sorted(rows, key=lambda row: row['path'])


def main():
    require(sys.version_info >= (3, 8), 'Python 3.8+ required')
    require(sys.argv[1:] in ([], ['--pre-receipt']), 'unknown command option')
    pre_receipt = sys.argv[1:] == ['--pre-receipt']
    base = Path(__file__).resolve().parent
    parent, stem = base.parent, base.name
    seal_path = parent/(stem + '.SEAL.json')
    archive_path = parent/(stem + '.tar.gz')
    receipt_path = parent/(stem + '.VERIFY.json')
    digest_path = parent/(stem + '.SEAL.sha256')
    report_path = parent/'ROUND_027_DUALITY_REVIEW.md'
    check_regular(seal_path)
    seal_raw = seal_path.read_bytes()
    seal = json.loads(seal_raw)
    require(seal['schema'] == 'AUD076-READONLY-EVIDENCE-1', 'wrong seal schema')
    require(seal['packet_name'] == stem, 'packet name mismatch')

    rows = walk_packet(base)
    require(rows == seal['files'], 'packet complete inventory or digest mismatch')
    internal = json.loads((base/'INVENTORY.json').read_text())
    require(internal['self_exclusion'] == ['INVENTORY.json'], 'unexpected inventory exclusions')
    require(internal['files'] == [r for r in rows if r['path'] != 'INVENTORY.json'],
            'internal complete inventory mismatch')

    raw_manifest = (base/'INPUT_SHA256SUMS.txt').read_bytes()
    require(digest(raw_manifest) == seal['input_manifest_sha256'], 'input manifest digest mismatch')
    names = []
    for line in raw_manifest.decode('utf-8').splitlines():
        expected, name = line.split('  ', 1)
        require(safe_relative(name), 'unsafe frozen input path')
        require(name not in names, 'duplicate frozen input')
        require(digest((base/'INPUTS'/name).read_bytes()) == expected,
                'frozen input copy mismatch: ' + name)
        names.append(name)
    require(len(names) == 11 == seal['input_count'], 'not exactly eleven inputs')
    copied_paths = sorted(r['path'][len('INPUTS/'):] for r in rows if r['path'].startswith('INPUTS/'))
    require(copied_paths == sorted(names), 'extra/missing frozen input copy')
    source_verification = json.loads((base/'INPUT_VERIFICATION.json').read_text())
    require(source_verification['input_count'] == 11 and source_verification['all_match'],
            'initial input-verification record failed')
    for entry in source_verification['entries']:
        raw = (base/'INPUTS'/entry['path']).read_bytes()
        require(entry['source_match'] and entry['copy_match'], 'bad source/copy record')
        require(entry['sha256'] == digest(raw) and entry['size'] == len(raw),
                'source-verification record mismatch')

    check_regular(report_path)
    report_raw = report_path.read_bytes()
    require(report_raw == (base/'REVIEW.md').read_bytes(), 'assigned report differs from packet report')
    require(seal['report'] == {'name': report_path.name, 'size': len(report_raw),
                               'sha256': digest(report_raw)}, 'report seal mismatch')

    check_regular(archive_path)
    archive_raw = archive_path.read_bytes()
    require(seal['archive']['name'] == archive_path.name, 'wrong archive name')
    require(seal['archive']['sha256'] == digest(archive_raw), 'archive digest mismatch')
    require(seal['archive']['size'] == len(archive_raw), 'archive size mismatch')
    expected_members = {stem + '/' + row['path']: row for row in rows}
    observed = set()
    with tarfile.open(str(archive_path), 'r:gz') as archive:
        for member in archive.getmembers():
            require(member.isfile() and not member.issym() and not member.islnk(),
                    'nonregular/link archive member: ' + member.name)
            require(safe_relative(member.name), 'unsafe archive member: ' + member.name)
            require(member.name.startswith(stem + '/'), 'archive prefix mismatch')
            require(member.name not in observed, 'duplicate archive member')
            require(member.name in expected_members, 'unlisted archive member')
            require(not member.mode & 0o222, 'writable archived member')
            require(not member.pax_headers, 'unneeded archive metadata override')
            expected = expected_members[member.name]
            raw = archive.extractfile(member).read()
            require(member.size == expected['size'] == len(raw), 'archive member size mismatch')
            require(digest(raw) == expected['sha256'], 'archive member digest mismatch')
            observed.add(member.name)
    require(observed == set(expected_members), 'missing archived regular member')
    require(len(observed) == seal['archive']['regular_member_count'], 'archive member count mismatch')

    diagnostic = base/'DIAGNOSTICS/fresh_exact_diagnostic.py'
    saved_stdout = (base/'DIAGNOSTICS/run_001.stdout.json').read_bytes()
    saved_stderr = (base/'DIAGNOSTICS/run_001.stderr.txt').read_bytes()
    saved_status = json.loads((base/'DIAGNOSTICS/run_001.status.json').read_text())
    require(saved_status['returncode'] == 0 and saved_stderr == b'', 'recorded diagnostic failed')
    env = dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    replay = subprocess.run([sys.executable, '-B', str(diagnostic)], capture_output=True,
                            timeout=60, env=env)
    require(replay.returncode == 0, 'fresh diagnostic replay failed: ' + replay.stderr.decode())
    require(replay.stdout == saved_stdout and replay.stderr == saved_stderr,
            'fresh diagnostic replay bytes differ')
    diagnostic_result = json.loads(replay.stdout)
    require(diagnostic_result['status'] == 'PASS', 'diagnostic status not PASS')
    require(diagnostic_result['checks_passed'] == 1239, 'unexpected check count')
    require(diagnostic_result['mutations_rejected'] == 14, 'unexpected mutation count')
    require(all(str(row['nonzero_difference']) not in ('0', '0/1')
                for row in diagnostic_result['mutations']), 'zero mutation witness')

    if not pre_receipt:
        check_regular(receipt_path)
        check_regular(digest_path)
        receipt = json.loads(receipt_path.read_text())
        require(receipt['returncode'] == 0 and receipt['stderr'] == '', 'issued verifier receipt failed')
        require(receipt['seal_sha256'] == digest(seal_raw), 'receipt points at another seal')
        require(receipt['archive_sha256'] == digest(archive_raw), 'receipt points at another archive')
        pre_result = json.loads(receipt['stdout'])
        require(pre_result['status'] == 'PASS' and pre_result['phase'] == 'pre-receipt',
                'invalid pre-issuance verification receipt')
        expected_anchors = {report_path.name, seal_path.name, archive_path.name, receipt_path.name}
        anchored = set()
        for line in digest_path.read_text().splitlines():
            expected, name = line.split('  ', 1)
            require(safe_relative(name) and '/' not in name, 'unsafe detached anchor path')
            require(name in expected_anchors and name not in anchored, 'unexpected/duplicate anchor')
            check_regular(parent/name)
            require(digest((parent/name).read_bytes()) == expected, 'detached anchor digest mismatch')
            anchored.add(name)
        require(anchored == expected_anchors, 'incomplete detached anchors')

    print(json.dumps({'status': 'PASS', 'phase': 'pre-receipt' if pre_receipt else 'final',
                      'packet_name': stem, 'regular_packet_files': len(rows),
                      'regular_archive_members': len(observed), 'exact_inputs': len(names),
                      'diagnostic_checks': diagnostic_result['checks_passed'],
                      'nonzero_mutations': diagnostic_result['mutations_rejected'],
                      'read_only_permissions': 'PASS', 'unsafe_archive_members': 0,
                      'diagnostic_byte_replay': 'PASS',
                      'seal_sha256': digest(seal_raw), 'archive_sha256': digest(archive_raw),
                      'report_sha256': digest(report_raw)}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
