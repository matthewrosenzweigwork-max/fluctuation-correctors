#!/usr/bin/env python3
"""Read-only root verification of AUD065's already issued packet.

Does not execute the issuance builder, extract members, or mutate evidence.
Paths in output/member/seal manifests are relative to the report directory;
input paths are relative to the campaign root, also checked in frozen copies.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import stat
import tarfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'AUDITS/BLIND_RECONSTRUCTION'
PACKET = BASE / 'ROUND_023_STATIC_THRESHOLD_BLIND_ARTIFACTS'
sha = lambda b: hashlib.sha256(b).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def manifest(path, base):
    rows = {}
    for line in path.read_text().splitlines():
        digest, name = line.split('  ', 1)
        rel = PurePosixPath(name)
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'bad digest')
        require(not rel.is_absolute() and '..' not in rel.parts and name not in rows, 'unsafe/duplicate path')
        target = base / name
        require(target.is_file() and not target.is_symlink(), 'nonregular path: ' + name)
        require(sha(target.read_bytes()) == digest, 'digest mismatch: ' + name)
        rows[name] = digest
    return rows

inputs = manifest(PACKET / 'INPUT_SHA256SUMS.txt', ROOT)
require(len(inputs) == 8, 'input count')
for name, digest in inputs.items():
    require(sha((PACKET / 'inputs' / name).read_bytes()) == digest, 'frozen input: ' + name)
outputs = manifest(PACKET / 'OUTPUT_SHA256SUMS.txt', BASE)
members = manifest(PACKET / 'ARCHIVE_MEMBER_SHA256SUMS.txt', BASE)
archives = manifest(PACKET / 'ARCHIVE_SHA256SUMS.txt', BASE)
seal = manifest(PACKET / 'SEAL_SHA256SUMS.txt', BASE)
require(len(archives) == 1 and len(members) == 20 and len(outputs) == 19 and len(seal) == 4, 'manifest counts')
require(set(members) == set(outputs) | {str((PACKET / 'OUTPUT_SHA256SUMS.txt').relative_to(BASE))}, 'member/output coverage')
archive = BASE / next(iter(archives))
with tarfile.open(archive, 'r:gz') as tf:
    records = tf.getmembers()
    require(len(records) == len({m.name for m in records}) == 20, 'archive duplicate/count')
    require({m.name for m in records} == set(members), 'archive membership')
    for member in records:
        rel = PurePosixPath(member.name)
        require(member.isfile() and not rel.is_absolute() and '..' not in rel.parts, 'unsafe archive member')
        require(member.mode == 0o444, 'archive writable member')
        data = tf.extractfile(member).read()
        require(sha(data) == members[member.name], 'archive digest')
        require(data == (BASE / member.name).read_bytes(), 'archive/extracted bytes')
files = [p for p in PACKET.rglob('*') if p.is_file()] + [archive, BASE / 'ROUND_023_STATIC_THRESHOLD_RECONSTRUCTION.md']
require(len(files) == 25, 'issued file count')
for path in files:
    require(stat.S_IMODE(path.stat().st_mode) == 0o444, 'issued writable file')
for path in [PACKET] + [p for p in PACKET.rglob('*') if p.is_dir()]:
    require(stat.S_IMODE(path.stat().st_mode) == 0o555, 'issued writable directory')
sealed = json.loads((PACKET / 'SEAL_VERIFICATION.json').read_text())
require(sealed['archive_sha256'] == sha(archive.read_bytes()), 'seal archive')
require({x['path']: x['sha256'] for x in sealed['inputs']} == inputs, 'seal inputs')
result = json.loads((PACKET / 'results_v2.json').read_text())
require(result['script_sha256'] == sha((PACKET / 'diagnostic_v2.py').read_bytes()), 'diagnostic source binding')
require(result['exact']['exact_assertions'] == 230 and len(result['exact']['mutations']) == 8, 'diagnostic counts')
print(json.dumps({'status': 'PASS', 'inputs': 8, 'outputs': 19, 'archive_members': 20,
 'issued_files': 25, 'safe_unique_regular_readonly_members': True, 'all_bytes_equal': True,
 'archive_sha256': sha(archive.read_bytes()),
 'proof_sha256': sha((BASE / 'ROUND_023_STATIC_THRESHOLD_RECONSTRUCTION.md').read_bytes()),
 'issuance_builder_executed': False, 'verifier_sha256': sha(Path(__file__).read_bytes())}, indent=2) + '\n', end='')
