#!/usr/bin/env python3
"""Read-only AUD062 membership and byte verifier. Never extracts an archive."""
from pathlib import Path, PurePosixPath
from io import BytesIO
import hashlib
import json
import re
import stat
import sys
import warnings
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ART = 'AUDITS/HOSTILE/ROUND_021_CRITICAL_CUBIC_HOSTILE_ARTIFACTS'
REPORT = 'AUDITS/HOSTILE/ROUND_021_CRITICAL_CUBIC_REVIEW.md'
INPUT_HASH = '1e0082cbce0d36476c5ffabf71f21e7f4af8efbfcd1ed181dadef9ed68d3f13e'
PAYLOAD = {REPORT} | {ART+'/'+n for n in (
    'INPUT_SHA256SUMS.txt', 'EXPOSURE.md', 'SOURCE_PREFLIGHT.md',
    'exact_diagnostic.py', 'RESULTS.json', 'README.md', 'VERIFICATION.md', 'verify_packet.py')}
META = {'OUTPUT_SHA256SUMS.txt', 'ARCHIVE_MEMBERS_SHA256SUMS.txt', 'SEAL.json', 'AUD062_PACKET.zip'}


def require(truth, message):
    if not truth:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and str(p) == name
            and all(a not in ('', '.', '..') for a in p.parts)
            and '\\' not in name and not any(ord(c) < 32 for c in name), 'unsafe member/path: '+repr(name))
    return name


def manifest(data):
    require(data.endswith(b'\n'), 'manifest lacks terminal newline')
    out = {}
    for line in data.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'malformed manifest line')
        value, name = match.groups()
        safe(name)
        require(name not in out, 'duplicate manifest path: '+name)
        out[name] = value
    return out


def regular(path):
    require(path.is_file() and not path.is_symlink(), 'not a regular non-symlink file: '+str(path))
    require(all(not p.is_symlink() for p in path.parents if p == HERE or HERE in p.parents), 'symlink ancestor')
    return path.read_bytes()


def archive_check(data, expected):
    with zipfile.ZipFile(BytesIO(data), 'r') as archive:
        infos = archive.infolist()
        names = [i.filename for i in infos]
        require(len(names) == len(set(names)), 'duplicate archive name')
        for info in infos:
            safe(info.filename)
            mode = (info.external_attr >> 16) & 0xffff
            require(not info.is_dir() and not stat.S_ISLNK(mode)
                    and stat.S_IFMT(mode) in (0, stat.S_IFREG), 'nonregular archive member')
            require(not (info.flag_bits & 1), 'encrypted member')
            require(info.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED), 'unsupported compression')
            require(info.file_size <= 8_000_000, 'oversized member')
        require(sum(i.file_size for i in infos) <= 16_000_000, 'oversized archive')
        require(set(names) == set(expected), 'incomplete or extra archive membership')
        require(archive.testzip() is None, 'archive CRC failure')
        for name in names:
            require(digest(archive.read(name)) == expected[name], 'archive byte mismatch: '+name)
    return len(names)


def verify():
    input_bytes = regular(HERE/'INPUT_SHA256SUMS.txt')
    require(digest(input_bytes) == INPUT_HASH, 'frozen input manifest changed')
    inputs = manifest(input_bytes)
    require(len(inputs) == 32, 'not exactly 32 prescribed inputs')
    for name, sha in inputs.items():
        require(digest(regular(HERE/'inputs'/name)) == sha, 'input byte mismatch: '+name)
    output_bytes = regular(HERE/'OUTPUT_SHA256SUMS.txt')
    outputs = manifest(output_bytes)
    require(set(outputs) == PAYLOAD, 'incomplete or extra output manifest membership')
    for name, sha in outputs.items():
        require(digest(regular(ROOT/name)) == sha, 'output byte mismatch: '+name)
    expected_local = {'inputs/'+n for n in inputs} | {n[len(ART)+1:] for n in PAYLOAD if n.startswith(ART+'/')} | META
    actual_local = {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if not p.is_dir()}
    require(actual_local == expected_local, 'extra or missing local packet member')
    expected_dirs = {str(parent) for name in expected_local for parent in PurePosixPath(name).parents if str(parent) != '.'}
    actual_dirs = {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_dir()}
    require(actual_dirs == expected_dirs, 'extra or missing local packet directory')
    require(all(not p.is_symlink() for p in HERE.rglob('*')), 'symlink in packet')
    expected = {'inputs/'+n: sha for n,sha in inputs.items()}
    expected.update({'outputs/'+n: sha for n,sha in outputs.items()})
    expected['outputs/'+ART+'/OUTPUT_SHA256SUMS.txt'] = digest(output_bytes)
    member_bytes = regular(HERE/'ARCHIVE_MEMBERS_SHA256SUMS.txt')
    require(manifest(member_bytes) == expected, 'archive member manifest mismatch')
    archive_bytes = regular(HERE/'AUD062_PACKET.zip')
    members = archive_check(archive_bytes, expected)
    seal = json.loads(regular(HERE/'SEAL.json'))
    exact_seal = {
        'audit':'AUD062', 'task':'TASK095', 'version':1,
        'base':'64ac0538dff37a37d0883661b401ad04c311a5e5',
        'branch':'codex/hocf-r021-critical-cubic-hostile',
        'inputs':32, 'payload_outputs':len(PAYLOAD), 'archive_members':members,
        'input_manifest_sha256':INPUT_HASH,
        'output_manifest_sha256':digest(output_bytes),
        'archive_member_manifest_sha256':digest(member_bytes),
        'archive_sha256':digest(archive_bytes),
    }
    require(seal == exact_seal, 'outer seal mismatch')
    results = json.loads(regular(HERE/'RESULTS.json'))
    require(results['status'] == 'PASS' and results['audit'] == 'AUD062', 'diagnostic did not pass')
    require(results['script_sha256'] == digest(regular(HERE/'exact_diagnostic.py')), 'diagnostic script/result mismatch')
    return {'status':'PASS','input_files':32,'payload_outputs':len(PAYLOAD),
            'local_packet_files':len(expected_local),'archive_members':members,
            'archive_sha256':digest(archive_bytes),'report_sha256':outputs[REPORT],
            'diagnostic_assertions':results['total_assertions']}, archive_bytes, expected


def self_test(data, expected):
    with zipfile.ZipFile(BytesIO(data)) as original:
        entries = [(i.filename, original.read(i.filename), None) for i in original.infolist()]
    first = entries[0]
    variants = {
        'duplicate':entries+[first],
        'missing':entries[1:],
        'unexpected':entries+[('unlisted.txt',b'extra',None)],
        'traversal':entries+[('../escape',b'x',None)],
        'absolute':entries+[('/escape',b'x',None)],
        'modified_bytes':[(first[0],first[1]+b'x',None)]+entries[1:],
        'symlink':[(first[0],first[1],stat.S_IFLNK | 0o777)]+entries[1:],
        'directory':entries+[('empty/',b'',stat.S_IFDIR | 0o755)],
    }
    rejected = []
    for label, items in variants.items():
        buf = BytesIO()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(buf,'w',compression=zipfile.ZIP_DEFLATED) as z:
                for name,value,mode in items:
                    info=zipfile.ZipInfo(name)
                    info.external_attr=(mode if mode is not None else stat.S_IFREG | 0o444)<<16
                    z.writestr(info,value)
        try:
            archive_check(buf.getvalue(),expected)
        except (ValueError,zipfile.BadZipFile):
            rejected.append(label)
        else:
            raise ValueError('mutation unexpectedly accepted: '+label)
    for label, value in (
        ('duplicate_manifest', (('0'*64+'  x\n')*2).encode()),
        ('unsafe_manifest', ('0'*64+'  ../x\n').encode()),
    ):
        try:
            manifest(value)
        except ValueError:
            rejected.append(label)
        else:
            raise ValueError('manifest mutation unexpectedly accepted')
    return rejected


if __name__ == '__main__':
    require(sys.argv[1:] in ([],['--self-test']), 'Use no arguments or --self-test')
    result,data,expected=verify()
    if sys.argv[1:]:
        result['rejected_in_memory_mutations']=self_test(data,expected)
    print(json.dumps(result,indent=2,sort_keys=True))
