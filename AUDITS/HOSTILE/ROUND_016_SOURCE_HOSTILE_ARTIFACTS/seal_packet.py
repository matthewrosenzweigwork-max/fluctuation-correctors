#!/usr/bin/env python3
"""Construct once, or verify read-only, the literal AUD052 audit packet."""
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tarfile


ART = Path(__file__).resolve().parent
BASE = ART.parents[2]
ART_REL = 'AUDITS/HOSTILE/ROUND_016_SOURCE_HOSTILE_ARTIFACTS'
REPORT_REL = 'AUDITS/HOSTILE/ROUND_016_SOURCE_EXTENSION_REVIEW.md'
ARCHIVE_NAME = 'ROUND_016_SOURCE_HOSTILE_AUD052_20260918_053542_UTC.tar.gz'
FROZEN_MANIFEST_SHA256 = '06919322a00bd6d2aea0e27ca05f76d745dbdf022d585183656af038d6d62b8c'
INPUT_NAMES = [
    'AGENTS.md',
    'TASKS/ACTIVE/ROUND_001_MODEL.md',
    'MEMORANDA/ROUND_001_ALGEBRA.md',
    'MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md',
    'THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md',
    'MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md',
    'MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md',
    'THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md',
    'TASKS/ACTIVE/TASK-081_ROUND016_SOURCE_EXTENSION_HOSTILE.md',
    'MEMORANDA/ROUND_016_SOURCE_EXTENSION.md',
    'MEMORANDA/ROUND_016_SOURCE_EXTENSION_ARTIFACTS/EXPOSURE.md',
]
DATA_NAMES = sorted([REPORT_REL] + [ART_REL + '/' + x for x in [
    'README.md', 'EXPOSURE.md', 'SOURCE_PREFLIGHT.md',
    'independent_diagnostic.py', 'independent_diagnostic_results.json',
    'INPUT_SHA256SUMS.txt', 'seal_packet.py',
]] + [ART_REL + '/INPUTS/' + x for x in INPUT_NAMES])
OUTPUT_REL = ART_REL + '/OUTPUT_SHA256SUMS.txt'
MEMBERS_REL = ART_REL + '/ARCHIVE_MEMBERS.txt'
MEMBERS = sorted(DATA_NAMES + [OUTPUT_REL, MEMBERS_REL])
EXTERNAL = sorted([ARCHIVE_NAME, 'ARCHIVE_SHA256SUMS.txt',
                   'SEAL_REPORT.json', 'SEAL_SHA256SUMS.txt'])
SEAL_TARGETS = sorted([ARCHIVE_NAME, 'ARCHIVE_SHA256SUMS.txt', 'SEAL_REPORT.json',
                       'OUTPUT_SHA256SUMS.txt', 'ARCHIVE_MEMBERS.txt', 'INPUT_SHA256SUMS.txt'])


class InvalidPacket(Exception):
    pass


def require(condition, message):
    if not condition:
        raise InvalidPacket(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_name(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and '..' not in p.parts and
            '.' not in p.parts and str(p) == name and chr(0) not in name,
            'unsafe or nonliteral path: ' + repr(name))
    return name


def regular_bytes(path):
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1,
            'expected an unlinked regular file: ' + str(path))
    return path.read_bytes()


def parse_manifest(raw):
    entries = {}
    for line in raw.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'invalid digest line')
        sha, name = match.groups()
        safe_name(name)
        require(name not in entries, 'duplicate digest path')
        entries[name] = sha
    return entries


def check_inputs(worktree=False):
    raw = regular_bytes(ART / 'INPUT_SHA256SUMS.txt')
    require(digest(raw) == FROZEN_MANIFEST_SHA256, 'frozen input manifest mismatch')
    entries = parse_manifest(raw)
    require(list(entries) == INPUT_NAMES and len(entries) == 11, 'input allowlist mismatch')
    for name, sha in entries.items():
        require(digest(regular_bytes(ART / 'INPUTS' / name)) == sha,
                'packet input byte mismatch: ' + name)
        if worktree:
            require(digest(regular_bytes(BASE / name)) == sha,
                    'worktree input byte mismatch: ' + name)
    return entries


def make_archive(entries):
    """In-memory deterministic archive; entries are name, bytes, type, link, mode."""
    target = io.BytesIO()
    with gzip.GzipFile(filename='', mode='wb', fileobj=target, mtime=0) as zipped:
        with tarfile.open(fileobj=zipped, mode='w', format=tarfile.PAX_FORMAT) as output:
            for name, raw, kind, link, mode in entries:
                info = tarfile.TarInfo(name)
                info.type = kind
                info.linkname = link
                info.mode = mode
                info.uid = info.gid = 0
                info.uname = info.gname = ''
                info.mtime = 0
                info.size = len(raw) if kind == tarfile.REGTYPE else 0
                output.addfile(info, io.BytesIO(raw) if kind == tarfile.REGTYPE else None)
    return target.getvalue()


def validate_archive(raw, expected):
    require(raw[4:8] == bytes(4), 'nondeterministic gzip timestamp')
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:gz') as packet:
        listed = packet.getmembers()
        names = [m.name for m in listed]
        require(len(names) == len(set(names)), 'duplicate archive member')
        for name in names:
            safe_name(name)
        require(names == sorted(expected), 'literal archive member order/set mismatch')
        for item in listed:
            require(item.type == tarfile.REGTYPE and item.isreg() and not item.linkname,
                    'archive member is not an ordinary regular file')
            require(item.mode == 0o444 and item.uid == item.gid == 0 and
                    item.uname == item.gname == '' and item.mtime == 0,
                    'archive member metadata mismatch')
            require(set(item.pax_headers) <= {'path'}, 'unexpected PAX metadata')
            if 'path' in item.pax_headers:
                require(item.pax_headers['path'] == item.name, 'PAX path disagreement')
            member = packet.extractfile(item)
            require(member is not None, 'missing member bytes')
            contents = member.read()
            require(item.size == len(expected[item.name]) and contents == expected[item.name],
                    'archive member bytes mismatch: ' + item.name)


def archive_negative_controls():
    good = ('safe/data.txt', b'safe\n', tarfile.REGTYPE, '', 0o444)
    expected = {'safe/data.txt': b'safe\n'}
    validate_archive(make_archive([good]), expected)
    cases = {
        'traversal': [('../safe/data.txt', *good[1:])],
        'absolute path': [('/safe/data.txt', *good[1:])],
        'duplicate member': [good, good],
        'symlink': [('safe/data.txt', b'', tarfile.SYMTYPE, '../outside', 0o444)],
        'hard link': [('safe/data.txt', b'', tarfile.LNKTYPE, 'outside', 0o444)],
        'unexpected member': [('other/data.txt', *good[1:])],
        'altered bytes': [('safe/data.txt', b'changed\n', tarfile.REGTYPE, '', 0o444)],
        'writable member': [('safe/data.txt', b'safe\n', tarfile.REGTYPE, '', 0o644)],
    }
    for name, entries in cases.items():
        try:
            validate_archive(make_archive(entries), expected)
        except InvalidPacket:
            continue
        raise InvalidPacket('negative archive control not rejected: ' + name)
    return sorted(cases)


def diagnostic_checks():
    outcome = json.loads(regular_bytes(ART / 'independent_diagnostic_results.json'))
    require(outcome['audit'] == 'AUD052' and outcome['status'] == 'PASS', 'diagnostic status mismatch')
    require(outcome['script_sha256'] == digest(regular_bytes(ART / 'independent_diagnostic.py')),
            'diagnostic script digest mismatch')
    require(outcome['assertions'] == 1700 and len(outcome['categories']) == 37 and
            sum(outcome['categories'].values()) == 1700, 'diagnostic totals mismatch')
    require(len(outcome['mutation_witness_counts']) == 8 and
            all(n > 0 for n in outcome['mutation_witness_counts'].values()),
            'missing diagnostic mutation witness')
    return outcome


def literal_inventory(require_readonly):
    expected_files = {str(PurePosixPath(p).relative_to(ART_REL))
                      for p in MEMBERS if p.startswith(ART_REL + '/')} | set(EXTERNAL)
    expected_dirs = {'.'}
    for rel in expected_files:
        parent = PurePosixPath(rel).parent
        while str(parent) != '.':
            expected_dirs.add(str(parent))
            parent = parent.parent
    actual_files, actual_dirs = set(), set()
    for path, dirs, files in os.walk(ART, followlinks=False):
        directory = Path(path)
        require(stat.S_ISDIR(directory.lstat().st_mode), 'non-directory in packet tree')
        actual_dirs.add(str(directory.relative_to(ART)))
        if require_readonly:
            require(stat.S_IMODE(directory.lstat().st_mode) == 0o555,
                    'packet directory is not mode 0555: ' + str(directory))
        for item in dirs:
            require(not (directory / item).is_symlink(), 'symlink directory in packet')
        for item in files:
            full = directory / item
            regular_bytes(full)
            actual_files.add(str(full.relative_to(ART)))
            if require_readonly:
                require(stat.S_IMODE(full.lstat().st_mode) == 0o444,
                        'packet file is not mode 0444: ' + str(full))
    require(actual_files == expected_files, 'literal artifact file inventory mismatch')
    require(actual_dirs == expected_dirs, 'literal artifact directory inventory mismatch')
    if require_readonly:
        require(stat.S_IMODE((BASE / REPORT_REL).lstat().st_mode) == 0o444,
                'report is not read-only')
    return len(actual_files), len(actual_dirs)


def verify():
    inputs = check_inputs()
    diagnostic_checks()
    negatives = archive_negative_controls()
    member_bytes = regular_bytes(BASE / MEMBERS_REL)
    require(member_bytes == ('\n'.join(MEMBERS) + '\n').encode(), 'literal member list mismatch')
    output_entries = parse_manifest(regular_bytes(BASE / OUTPUT_REL))
    require(list(output_entries) == sorted(DATA_NAMES + [MEMBERS_REL]), 'literal output manifest mismatch')
    for name, sha in output_entries.items():
        require(digest(regular_bytes(BASE / name)) == sha, 'output byte mismatch: ' + name)
    payload = {name: regular_bytes(BASE / name) for name in MEMBERS}
    archive = regular_bytes(ART / ARCHIVE_NAME)
    validate_archive(archive, payload)
    archive_manifest = parse_manifest(regular_bytes(ART / 'ARCHIVE_SHA256SUMS.txt'))
    require(archive_manifest == {ARCHIVE_NAME: digest(archive)}, 'archive byte seal mismatch')
    seal = json.loads(regular_bytes(ART / 'SEAL_REPORT.json'))
    expected_hashes = {name: digest(regular_bytes(BASE / name)) for name in
                       [REPORT_REL, OUTPUT_REL, MEMBERS_REL, ART_REL + '/INPUT_SHA256SUMS.txt']}
    require(seal['audit'] == 'AUD052' and seal['status'] == 'PASS' and seal['input_count'] == len(inputs) and
            seal['archive_member_count'] == len(MEMBERS) == 21 and
            seal['payload_hashes'] == expected_hashes and
            seal['archive_sha256'] == digest(archive) and
            seal['archive_negative_controls'] == negatives and
            seal['read_only_files'] == '0444' and seal['read_only_packet_directories'] == '0555',
            'seal report mismatch')
    final_manifest = parse_manifest(regular_bytes(ART / 'SEAL_SHA256SUMS.txt'))
    require(list(final_manifest) == SEAL_TARGETS, 'external seal inventory mismatch')
    for name, sha in final_manifest.items():
        require(digest(regular_bytes(ART / name)) == sha, 'external seal byte mismatch: ' + name)
    files, directories = literal_inventory(require_readonly=True)
    return {'audit': 'AUD052', 'status': 'PASS', 'input_count': len(inputs),
            'archive_member_count': len(MEMBERS), 'artifact_file_count': files,
            'artifact_directory_count': directories, 'archive_negative_controls': len(negatives),
            'diagnostic_assertions': 1700,
            'report_sha256': digest(payload[REPORT_REL]),
            'archive_sha256': digest(archive),
            'final_seal_manifest_sha256': digest(regular_bytes(ART / 'SEAL_SHA256SUMS.txt'))}


def seal():
    require(BASE / ART_REL == ART, 'unexpected artifact location')
    inputs = check_inputs(worktree=True)
    outcome = diagnostic_checks()
    negatives = archive_negative_controls()
    require(len(DATA_NAMES) == 19 and len(MEMBERS) == 21, 'internal payload count mismatch')
    for name in [MEMBERS_REL, OUTPUT_REL] + [ART_REL + '/' + x for x in EXTERNAL]:
        require(not (BASE / name).exists(), 'refusing to replace an issued/control file: ' + name)
    for name in DATA_NAMES:
        regular_bytes(BASE / name)
    (BASE / MEMBERS_REL).write_text('\n'.join(MEMBERS) + '\n')
    output_lines = [digest(regular_bytes(BASE / name)) + '  ' + name
                    for name in sorted(DATA_NAMES + [MEMBERS_REL])]
    (BASE / OUTPUT_REL).write_text('\n'.join(output_lines) + '\n')
    payload = {name: regular_bytes(BASE / name) for name in MEMBERS}
    archive = make_archive([(name, payload[name], tarfile.REGTYPE, '', 0o444) for name in MEMBERS])
    validate_archive(archive, payload)
    with (ART / ARCHIVE_NAME).open('xb') as output:
        output.write(archive)
    (ART / 'ARCHIVE_SHA256SUMS.txt').write_text(digest(archive) + '  ' + ARCHIVE_NAME + '\n')
    metadata = {
        'audit': 'AUD052', 'status': 'PASS', 'mathematical_verdict': 'whole frozen THM038 and stronger candidate claims PASS',
        'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
        'published_base': '072cab684b9ce41855ead6c48f435c8fc184ec35',
        'worktree': str(BASE), 'branch': 'codex/hocf-r016-source-hostile',
        'input_count': len(inputs), 'archive_member_count': len(MEMBERS),
        'archive_filename': ARCHIVE_NAME, 'archive_sha256': digest(archive),
        'payload_hashes': {name: digest(regular_bytes(BASE / name)) for name in
                           [REPORT_REL, OUTPUT_REL, MEMBERS_REL, ART_REL + '/INPUT_SHA256SUMS.txt']},
        'archive_checks': ['exact literal member order and set', 'all member bytes',
                           'relative canonical paths only', 'no duplicate names',
                           'regular files only; no symlinks or hard links',
                           'fixed owner, mode, timestamp and gzip metadata'],
        'archive_negative_controls': negatives,
        'read_only_files': '0444', 'read_only_packet_directories': '0555',
        'original_worktree_inputs_rechecked': True,
        'diagnostic_assertions': outcome['assertions'], 'diagnostic_categories': len(outcome['categories']),
        'diagnostic_mutation_controls_detected': len(outcome['mutation_witness_counts']),
        'canonical_edit_commit_push_install_external_search_children': False,
        'earlier_complete_modules_promoted': False, 'withheld_reconstruction_read': False,
    }
    (ART / 'SEAL_REPORT.json').write_text(json.dumps(metadata, indent=2, sort_keys=True) + '\n')
    final_lines = [digest(regular_bytes(ART / name)) + '  ' + name for name in SEAL_TARGETS]
    (ART / 'SEAL_SHA256SUMS.txt').write_text('\n'.join(final_lines) + '\n')
    literal_inventory(require_readonly=False)
    for name in MEMBERS:
        (BASE / name).chmod(0o444)
    for name in EXTERNAL:
        (ART / name).chmod(0o444)
    for name in INPUT_NAMES:
        (BASE / name).chmod(0o444)
    for path, dirs, files in os.walk(ART, topdown=False, followlinks=False):
        Path(path).chmod(0o555)
    return verify()


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--seal', action='store_true')
    group.add_argument('--verify', action='store_true')
    group.add_argument('--preflight', action='store_true')
    args = parser.parse_args()
    if args.preflight:
        check_inputs(worktree=True)
        diagnostic_checks()
        controls = archive_negative_controls()
        for name in DATA_NAMES:
            regular_bytes(BASE / name)
        result = {'audit': 'AUD052', 'status': 'PREFLIGHT_PASS',
                  'input_count': 11, 'planned_archive_member_count': len(MEMBERS),
                  'archive_negative_controls': len(controls)}
    else:
        result = seal() if args.seal else verify()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
