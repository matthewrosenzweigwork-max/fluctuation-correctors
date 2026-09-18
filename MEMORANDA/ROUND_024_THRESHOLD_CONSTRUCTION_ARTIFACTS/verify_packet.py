#!/usr/bin/env python3
"""Read-only verifier of R24 archive, frozen dossier, results, and seal.

Uses a separate implementation from the mathematical diagnostic. It never
extracts an archive or trusts member paths for filesystem writes.
"""
import argparse
import hashlib
import io
import json
import stat
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath


class IntegrityError(Exception):
    pass


def require(ok, message):
    if not ok:
        raise IntegrityError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    p = PurePosixPath(name)
    return (bool(name) and not p.is_absolute() and '\\' not in name
            and all(x not in ('', '.', '..') for x in name.split('/'))
            and not name.endswith('/'))


def parse_manifest(data):
    out = {}
    for line in data.decode().splitlines():
        require(len(line) > 66 and line[64:66] == '  ', 'manifest syntax')
        value, name = line[:64], line[66:]
        require(len(value) == 64 and all(c in '0123456789abcdef' for c in value), 'manifest digest')
        require(safe_name(name) and name not in out, 'unsafe/duplicate manifest name')
        out[name] = value
    return out


def verify_bytes(raw):
    files = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        entries = archive.infolist()
        require(len(entries) <= 100, 'unexpected archive member count')
        for item in entries:
            require(safe_name(item.filename), 'unsafe member name')
            require(item.filename not in files, 'duplicate member')
            mode = item.external_attr >> 16
            require(stat.S_IFMT(mode) in (0, stat.S_IFREG), 'member is not a regular file')
            require(item.file_size <= 10_000_000, 'unexpected member size')
            files[item.filename] = archive.read(item)
        require(archive.testzip() is None, 'CRC failure')
    require('ARCHIVE_INVENTORY.json' in files, 'missing inventory')
    inventory = json.loads(files['ARCHIVE_INVENTORY.json'])
    records = inventory['members_except_this_inventory']
    expected = {item['path'] for item in records} | {'ARCHIVE_INVENTORY.json'}
    require(len(records)+1 == len(expected), 'duplicate inventory records')
    require(set(files) == expected, 'archive exact inventory mismatch')
    for item in records:
        require(safe_name(item['path']), 'unsafe inventory name')
        data = files[item['path']]
        require(len(data) == item['size'] and digest(data) == item['sha256'],
                'inventory byte mismatch: '+item['path'])
    outputs = parse_manifest(files['OUTPUT_SHA256SUMS.txt'])
    require(set(outputs) == set(files)-{'OUTPUT_SHA256SUMS.txt', 'ARCHIVE_INVENTORY.json'},
            'output manifest exact set mismatch')
    for name, expected_digest in outputs.items():
        require(digest(files[name]) == expected_digest, 'output hash mismatch: '+name)
    inputs = parse_manifest(files['INPUT_SHA256SUMS.txt'])
    require(len(inputs) == 20, 'frozen dossier count is not 20')
    require({name for name in files if name.startswith('inputs/')} ==
            {'inputs/'+name for name in inputs}, 'input copy inventory mismatch')
    for name, expected_digest in inputs.items():
        require(digest(files['inputs/'+name]) == expected_digest, 'input hash mismatch: '+name)
    result = json.loads(files['RESULTS.json'])
    require(result['status'] == 'PASS' and result['assertions'] == 1446, 'unexpected result status/count')
    require(result['script_sha256'] == digest(files['exact_diagnostic.py']), 'stale diagnostic result')
    require(len(result['detecting_mutations']) == 15 and
            all(value > 0 for value in result['detecting_mutations'].values()), 'vacuous mutation evidence')
    return files


def make_zip(files, extra=None, link=None):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in files.items():
            item = zipfile.ZipInfo(name)
            item.external_attr = (stat.S_IFREG | 0o444) << 16
            if name == link:
                item.external_attr = (stat.S_IFLNK | 0o777) << 16
            z.writestr(item, data)
        if extra is not None:
            z.writestr(extra[0], extra[1])
    return stream.getvalue()


def mutation_tests(files):
    tests = []
    changed = dict(files)
    changed['REPORT.md'] += b'\ncorruption\n'
    tests.append(('changed_report', make_zip(changed)))
    removed = dict(files)
    del removed['SOURCE_PREFLIGHT.md']
    tests.append(('missing_member', make_zip(removed)))
    tests.append(('path_traversal', make_zip(files, ('../escape', b'x'))))
    tests.append(('absolute_path', make_zip(files, ('/escape', b'x'))))
    tests.append(('unexpected_member', make_zip(files, ('unlisted.txt', b'x'))))
    tests.append(('symlink_member', make_zip(files, link='REPORT.md')))
    found = []
    for name, raw in tests:
        try:
            verify_bytes(raw)
        except IntegrityError as error:
            found.append({'mutation': name, 'detected': True, 'reason': str(error)})
        else:
            raise IntegrityError('verifier mutation was not detected: '+name)
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive', required=True, type=Path)
    parser.add_argument('--seal', type=Path)
    parser.add_argument('--source-root', type=Path)
    parser.add_argument('--rerun-diagnostic', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    raw = args.archive.read_bytes()
    files = verify_bytes(raw)
    if args.seal:
        seal = json.loads(args.seal.read_text())
        require(seal['archive_sha256'] == digest(raw), 'archive seal mismatch')
        require(seal['report_sha256'] == digest(files['REPORT.md']), 'report seal mismatch')
        require(seal['output_manifest_sha256'] == digest(files['OUTPUT_SHA256SUMS.txt']), 'manifest seal mismatch')
        require(seal['inventory_sha256'] == digest(files['ARCHIVE_INVENTORY.json']), 'inventory seal mismatch')
    if args.source_root:
        inputs = parse_manifest(files['INPUT_SHA256SUMS.txt'])
        for name, expected in inputs.items():
            require(digest((args.source_root/name).read_bytes()) == expected, 'live input changed: '+name)
        require((args.source_root/'MEMORANDA/ROUND_024_THRESHOLD_DYNAMIC_CONSTRUCTION.md').read_bytes()
                == files['REPORT.md'], 'external report differs from archive')
    mutation_results = mutation_tests(files) if args.self_test else []
    if args.rerun_diagnostic:
        here = Path(__file__).resolve().parent
        require((here/'exact_diagnostic.py').read_bytes() == files['exact_diagnostic.py'], 'local checker mismatch')
        require((here/'RESULTS.json').read_bytes() == files['RESULTS.json'], 'local result mismatch')
        subprocess.run([sys.executable, str(here/'exact_diagnostic.py'), '--check'],
                       check=True, stdout=subprocess.DEVNULL)
    print(json.dumps({'status': 'PASS', 'archive_sha256': digest(raw),
                      'members': len(files), 'frozen_inputs': 20,
                      'mathematical_checks': 1446, 'mathematical_mutation_categories': 15,
                      'verifier_mutations': mutation_results,
                      'diagnostic_reexecuted': args.rerun_diagnostic,
                      'evidence_class': 'SELF_CHECKED packet integrity and reproducibility'}, indent=2))


if __name__ == '__main__':
    main()
