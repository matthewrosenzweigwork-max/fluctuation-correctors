#!/usr/bin/env python3
"""One-time local issuance recipe, preserved for traceability.

The separate verify_readonly.py is the portable read-only verifier.
This recipe refuses to overwrite any previously issued outer artifact.
"""
from datetime import datetime, timezone
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
import time


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True)+'\n').encode()


p = Path(__file__).resolve().parents[1]
out = p.parent
report = out/'ROUND_028_MOMENT_TAIL_RECONSTRUCTION.md'
archive = out/(p.name+'.tar.gz')
receipt = out/(p.name+'.VERIFICATION.json')
seals = out/(p.name+'.SEALS.json')
sha_file = out/(p.name+'.sha256')
for path in [archive, receipt, seals, sha_file, p/'INVENTORY.json', p/'PAYLOAD_SHA256.json']:
    assert not path.exists(), ('refusing replacement', str(path))
assert report.read_bytes() == (p/'REPORT.md').read_bytes()
payload = {}
for path in sorted(p.rglob('*')):
    assert not path.is_symlink(), str(path)
    if path.is_file():
        assert stat.S_ISREG(path.stat().st_mode)
        data = path.read_bytes()
        payload[path.relative_to(p).as_posix()] = {'bytes': len(data), 'sha256': sha(data)}
members = sorted(list(payload)+['INVENTORY.json', 'PAYLOAD_SHA256.json'])
(p/'PAYLOAD_SHA256.json').write_bytes(encode(payload))
(p/'INVENTORY.json').write_bytes(encode({'packet': p.name, 'archive_member_type': 'regular',
                                      'file_mode': '0444', 'regular_members': members}))
for relative in members:
    (p/relative).chmod(0o444)
report.chmod(0o444)
with archive.open('xb') as output:
    with gzip.GzipFile(filename='', mode='wb', fileobj=output, mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode='w', format=tarfile.PAX_FORMAT) as tf:
            for relative in members:
                data = (p/relative).read_bytes()
                info = tarfile.TarInfo(p.name+'/'+relative)
                info.size = len(data)
                info.mode = 0o444
                info.uid = info.gid = info.mtime = 0
                info.uname = info.gname = ''
                tf.addfile(info, io.BytesIO(data))
archive.chmod(0o444)
for directory in sorted((x for x in p.rglob('*') if x.is_dir()), key=lambda x: len(x.parts), reverse=True):
    directory.chmod(0o555)
p.chmod(0o555)
command = [sys.executable, str(p/'verify_readonly.py'), '--archive', str(archive), '--replay']
start = datetime.now(timezone.utc).isoformat()
tick = time.monotonic()
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
checked = subprocess.run(command, capture_output=True, text=True, env=env, cwd=p)
execution = {'started_utc': start, 'seconds': time.monotonic()-tick, 'command': command,
             'returncode': checked.returncode, 'stdout': checked.stdout, 'stderr': checked.stderr,
             'packet_writes_performed_by_verifier': False,
             'verifier_sha256': sha((p/'verify_readonly.py').read_bytes())}
if checked.returncode == 0:
    execution['result'] = json.loads(checked.stdout)
receipt.write_bytes(encode(execution))
receipt.chmod(0o444)
assert checked.returncode == 0, checked.stderr
result = execution['result']
outer = {'audit': 'AUD079', 'task': 'TASK124', 'verdict': 'ISOLATED_RECONSTRUCTION_PASS',
         'issued_utc': datetime.now(timezone.utc).isoformat(), 'packet': p.name,
         'regular_member_count': len(members), 'payload_hash_count': len(payload),
         'exact_input_count': 18, 'report_lines': len(report.read_text().splitlines()),
         'check_count': result['fresh_replay_check_count'],
         'nonzero_mutation_count': result['fresh_replay_nonzero_mutation_count'],
         'development_execution_count': 1, 'development_failure_count': 0,
         'fresh_readonly_verification': 'PASS',
         'open_assertion': 'Actual raw force-tail cancellation or an admitted same-fixed-data witness.',
         'artifacts': {}}
for path in [archive, report, p/'INVENTORY.json', p/'PAYLOAD_SHA256.json', receipt]:
    data = path.read_bytes()
    outer['artifacts'][path.relative_to(out).as_posix()] = {'bytes': len(data), 'sha256': sha(data)}
seals.write_bytes(encode(outer))
seals.chmod(0o444)
lines = []
for path in [archive, report, p/'INVENTORY.json', p/'PAYLOAD_SHA256.json', receipt, seals]:
    lines.append(sha(path.read_bytes())+'  '+path.relative_to(out).as_posix())
sha_file.write_text('\n'.join(lines)+'\n')
sha_file.chmod(0o444)
print(json.dumps(outer, indent=2, sort_keys=True))
