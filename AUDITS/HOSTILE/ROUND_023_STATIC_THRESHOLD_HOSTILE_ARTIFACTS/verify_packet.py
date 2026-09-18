#!/usr/bin/env python3
"""Read-only AUD066 packet verifier. Never extracts an archive."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile

EXPECTED_INPUT_MANIFEST_SHA256 = '5d586a805f690d07113b351da22ae08f29f7b65d96dfb7e60987c874380744ba'
ARTIFACT_NAME = 'ROUND_023_STATIC_THRESHOLD_HOSTILE_ARTIFACTS'
REVIEW_NAME = 'ROUND_023_STATIC_THRESHOLD_REVIEW.md'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_relative(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute(), 'absolute or empty path')
    require('\\' not in name and ':' not in name, 'nonportable path')
    require(all(ord(c) >= 32 and ord(c) != 127 for c in name), 'control character in path')
    require(all(x not in ('', '.', '..') for x in name.split('/')), 'unsafe path component')
    require(str(p) == name, 'noncanonical path')
    return p


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_manifest(path):
    require(path.is_file() and not path.is_symlink(), 'missing/linked manifest')
    out = {}
    for line in path.read_text().splitlines():
        require(len(line) >= 67 and line[64:66] == '  ', 'bad manifest format')
        sha, rel = line[:64], line[66:]
        require(re.fullmatch('[0-9a-f]{64}', sha) is not None, 'bad digest')
        safe_relative(rel)
        require(rel not in out, 'duplicate manifest record')
        out[rel] = sha
    return out


def verify(artifact, require_sealed=True):
    artifact = Path(artifact)
    require(artifact.name == ARTIFACT_NAME, 'wrong artifact directory')
    require(artifact.is_dir() and not artifact.is_symlink(), 'missing/linked artifact directory')
    output_manifest = artifact/'OUTPUT_SHA256SUMS.txt'
    inputs_manifest = artifact/'INPUT_SHA256SUMS.txt'
    require(digest(inputs_manifest.read_bytes()) == EXPECTED_INPUT_MANIFEST_SHA256,
            'original prescribed input manifest mismatch')
    inputs = read_manifest(inputs_manifest)
    require(len(inputs) == 11, 'input count is not eleven')
    outputs = read_manifest(output_manifest)
    actual_files = set()
    actual_dirs = [artifact]
    for path in artifact.rglob('*'):
        require(not path.is_symlink(), 'symlink in artifact')
        if path.is_dir():
            actual_dirs.append(path)
        else:
            require(path.is_file() and stat.S_ISREG(path.stat().st_mode), 'nonregular payload')
            actual_files.add(path.relative_to(artifact).as_posix())
    require(actual_files == set(outputs)|{'OUTPUT_SHA256SUMS.txt'}, 'output membership mismatch')
    require({p for p in actual_files if p.startswith('INPUTS/')} ==
            {'INPUTS/'+p for p in inputs}, 'exact input copy membership mismatch')
    for rel, sha in inputs.items():
        data = (artifact/'INPUTS'/rel).read_bytes()
        require(digest(data) == sha, 'input hash mismatch: '+rel)
        require(outputs['INPUTS/'+rel] == sha, 'input/output manifest disagreement')
    for rel, sha in outputs.items():
        require(digest((artifact/rel).read_bytes()) == sha, 'output hash mismatch: '+rel)

    standalone = artifact.parent/REVIEW_NAME
    require(standalone.is_file() and not standalone.is_symlink(), 'missing/linked standalone review')
    require(standalone.read_bytes() == (artifact/'REVIEW.md').read_bytes(), 'standalone review differs')
    archive = artifact.with_suffix('.zip')
    archive_checksum = Path(str(archive)+'.sha256')
    require(archive.is_file() and not archive.is_symlink(), 'missing/linked archive')
    require(archive_checksum.is_file() and not archive_checksum.is_symlink(), 'missing/linked archive checksum')
    archive_hash = digest(archive.read_bytes())
    require(archive_checksum.read_text() == archive_hash+'  '+archive.name+'\n', 'archive digest mismatch')
    expected_members = {ARTIFACT_NAME+'/'+p for p in actual_files}
    total_bytes = 0
    with zipfile.ZipFile(archive, 'r') as zf:
        members = zf.infolist()
        names = [i.filename for i in members]
        require(len(names) == len(set(names)), 'duplicate archive member')
        for info in members:
            safe_relative(info.filename)
            require(not info.is_dir(), 'unexpected directory member')
            require(not (info.flag_bits & 1), 'encrypted archive member')
            require(info.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED), 'unsupported compression')
            mode = info.external_attr >> 16
            require(stat.S_ISREG(mode), 'nonregular archive member')
            require(not mode & 0o222, 'writable archive member')
        require(set(names) == expected_members, 'archive membership mismatch')
        for info in members:
            rel = info.filename[len(ARTIFACT_NAME)+1:]
            expected = (artifact/rel).read_bytes()
            require(info.file_size == len(expected), 'archive declared size mismatch')
            # zipfile verifies the CRC while reading. No extraction is performed.
            actual = zf.read(info)
            require(actual == expected, 'archive byte mismatch: '+rel)
            total_bytes += len(actual)
    sealed_paths = [artifact/p for p in actual_files]+actual_dirs+[standalone,archive,archive_checksum]
    if require_sealed:
        for path in sealed_paths:
            require(not path.stat().st_mode & 0o222, 'writable sealed path: '+str(path))
    return {'status':'PASS','audit':'AUD066','exact_input_count':len(inputs),
            'input_manifest_sha256':digest(inputs_manifest.read_bytes()),
            'output_manifest_sha256':digest(output_manifest.read_bytes()),
            'output_payload_files':len(outputs),'artifact_files_including_manifest':len(actual_files),
            'archive_members':len(expected_members),'archive_uncompressed_bytes':total_bytes,
            'archive_sha256':archive_hash,'archive_bytes':archive.stat().st_size,
            'standalone_review_sha256':digest(standalone.read_bytes()),
            'byte_comparison':'every member equals its corresponding disk bytes',
            'archive_extracted':False,'safe_paths_and_types':True,
            'read_only_checked':require_sealed,'read_only_paths':len(sealed_paths)}


if __name__ == '__main__':
    artifact = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
    print(json.dumps(verify(artifact),indent=2,sort_keys=True))
