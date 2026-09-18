#!/usr/bin/env python3
"""Record one diagnostic execution without overwriting earlier attempts."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

packet = Path(__file__).resolve().parents[1]
outputs = packet / 'OUTPUTS'
index = 1
while (outputs / ('run_%03d' % index)).exists():
    index += 1
run = outputs / ('run_%03d' % index)
run.mkdir()
source = packet / 'CODE/diagnostic.py'
snapshot = run / 'diagnostic_source.py'
snapshot.write_bytes(source.read_bytes())
command = [sys.executable, str(source)]
start = datetime.now(timezone.utc).isoformat()
tick = time.monotonic()
result = subprocess.run(command, capture_output=True, text=True, cwd=packet)
(run / 'stdout.txt').write_text(result.stdout)
(run / 'stderr.txt').write_text(result.stderr)
record = {'run': index, 'started_utc': start, 'seconds': time.monotonic()-tick,
          'command': command, 'returncode': result.returncode,
          'source_sha256': hashlib.sha256(snapshot.read_bytes()).hexdigest()}
if result.returncode == 0:
    parsed = json.loads(result.stdout)
    record.update({k: parsed[k] for k in ['status', 'check_count', 'mutation_count']})
    (run / 'result.json').write_text(json.dumps(parsed, indent=2, sort_keys=True)+'\n')
(run / 'execution.json').write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
print(json.dumps(record, indent=2))
if result.returncode:
    print(result.stderr)
raise SystemExit(result.returncode)
