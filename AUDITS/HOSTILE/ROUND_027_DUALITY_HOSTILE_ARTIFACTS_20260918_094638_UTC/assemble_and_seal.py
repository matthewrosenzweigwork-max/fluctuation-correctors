#!/usr/bin/env python3
"""One-time AUD076 issuance. Run only while this evidence is unissued/writable.

Writes only this unique packet and its assigned sibling report/archive/seals.
Reads only the eleven frozen sources, its supplied manifest and worker outputs.
The resulting normal verifier is portable and read-only; this assembler is not.
"""
import datetime
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tarfile


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def list_rows(base):
    rows = []
    for folder, directories, files in os.walk(str(base), followlinks=False):
        for name in directories:
            assert stat.S_ISDIR((Path(folder)/name).lstat().st_mode)
        for name in files:
            path = Path(folder)/name
            assert stat.S_ISREG(path.lstat().st_mode)
            raw = path.read_bytes()
            rows.append({'path': path.relative_to(base).as_posix(),
                         'size': len(raw), 'sha256': sha(raw)})
    return sorted(rows, key=lambda item: item['path'])


def main():
    base = Path(__file__).resolve().parent
    parent, stem = base.parent, base.name
    root = base.parents[2]
    report = parent/'ROUND_027_DUALITY_REVIEW.md'
    archive = parent/(stem + '.tar.gz')
    seal = parent/(stem + '.SEAL.json')
    receipt = parent/(stem + '.VERIFY.json')
    anchors = parent/(stem + '.SEAL.sha256')
    assert not any(path.exists() for path in (archive, seal, receipt, anchors,
                                               base/'INVENTORY.json', base/'REVIEW.md'))
    # Last exact source check; do not silently refresh a changed frozen input.
    manifest = (base/'INPUT_SHA256SUMS.txt').read_bytes()
    assert manifest == (root/'AUDITS/ROUND_027_DUALITY_HOSTILE_INPUT_SHA256SUMS.txt').read_bytes()
    lines = manifest.decode().splitlines()
    assert len(lines) == 11
    for line in lines:
        expected, name = line.split('  ', 1)
        assert sha((root/name).read_bytes()) == expected
        assert sha((base/'INPUTS'/name).read_bytes()) == expected
    raw_report = report.read_bytes()
    (base/'REVIEW.md').write_bytes(raw_report)
    rows = list_rows(base)
    write_json(base/'INVENTORY.json', {'schema': 'AUD076-INTERNAL-INVENTORY-1',
                                      'self_exclusion': ['INVENTORY.json'], 'files': rows})
    all_rows = list_rows(base)
    # No extraction and no links/metadata overrides: regular USTAR file members.
    with archive.open('wb') as stream:
        with gzip.GzipFile(filename='', mode='wb', fileobj=stream, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode='w', format=tarfile.USTAR_FORMAT) as tar:
                for row in all_rows:
                    raw = (base/row['path']).read_bytes()
                    member = tarfile.TarInfo(stem + '/' + row['path'])
                    member.size = len(raw)
                    member.mode = 0o444
                    member.uid = member.gid = 0
                    member.uname = member.gname = ''
                    member.mtime = 0
                    member.type = tarfile.REGTYPE
                    tar.addfile(member, io.BytesIO(raw))
    raw_archive = archive.read_bytes()
    write_json(seal, {'schema': 'AUD076-READONLY-EVIDENCE-1',
                      'issued_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      'packet_name': stem, 'input_count': 11,
                      'input_manifest_sha256': sha(manifest),
                      'report': {'name': report.name, 'size': len(raw_report), 'sha256': sha(raw_report)},
                      'archive': {'name': archive.name, 'size': len(raw_archive),
                                  'sha256': sha(raw_archive), 'regular_member_count': len(all_rows)},
                      'files': all_rows,
                      'scope': 'Hostile-axis evidence only; no gate promotion or modal decay claim.'})
    for row in all_rows:
        (base/row['path']).chmod(0o444)
    for folder, directories, files in os.walk(str(base), topdown=False, followlinks=False):
        Path(folder).chmod(0o555)
    for path in (report, archive, seal):
        path.chmod(0o444)
    command = [sys.executable, '-B', str(base/'verify_readonly.py'), '--pre-receipt']
    result = subprocess.run(command, capture_output=True, text=True, timeout=60,
                            env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    # Preserve a nonzero result if one occurs. Do not modify a frozen packet to
    # conceal failure; a distinct superseding packet would then be necessary.
    write_json(receipt, {'command': command, 'returncode': result.returncode,
                         'stdout': result.stdout, 'stderr': result.stderr,
                         'seal_sha256': sha(seal.read_bytes()),
                         'archive_sha256': sha(raw_archive)})
    receipt.chmod(0o444)
    anchors.write_text(''.join(sha(path.read_bytes()) + '  ' + path.name + '\n'
                              for path in (report, archive, seal, receipt)))
    anchors.chmod(0o444)
    print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, file=sys.stderr, end='')
    print('DETACHED_SEAL_SHA256 ' + sha(anchors.read_bytes()))
    print('VERIFY_RECEIPT ' + str(receipt))
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
