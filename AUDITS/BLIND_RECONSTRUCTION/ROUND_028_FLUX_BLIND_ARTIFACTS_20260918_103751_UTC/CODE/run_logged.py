#!/usr/bin/env python3
"""Run one explicitly supplied local command and retain every outcome."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import platform
import subprocess
import sys

parser=argparse.ArgumentParser()
parser.add_argument('--label',required=True)
parser.add_argument('--expected-exit',type=int,default=0)
parser.add_argument('command',nargs=argparse.REMAINDER)
args=parser.parse_args()
command=args.command[1:] if args.command[:1]==['--'] else args.command
assert command
packet=Path(__file__).resolve().parent.parent
logs=packet/'LOGS'
number=len(list(logs.glob('run_*.json')))+1
stem='run_%03d_%s'%(number,args.label)
record=logs/(stem+'.json')
assert not record.exists()
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
env=dict(os.environ)
env['PYTHONDONTWRITEBYTECODE']='1'
result=subprocess.run(command,cwd=str(packet),env=env,capture_output=True)
out=logs/(stem+'.stdout.txt')
err=logs/(stem+'.stderr.txt')
out.write_bytes(result.stdout)
err.write_bytes(result.stderr)
payload={'number':number,'label':args.label,'argv':command,
         'cwd':str(packet),'started_utc':start,
         'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'exit_code':result.returncode,'expected_exit_code':args.expected_exit,
         'matched_expected_exit':result.returncode==args.expected_exit,
         'stdout':out.relative_to(packet).as_posix(),
         'stderr':err.relative_to(packet).as_posix(),
         'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),
         'stderr_sha256':hashlib.sha256(result.stderr).hexdigest(),
         'python':sys.version,'platform':platform.platform()}
record.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps({'record':str(record),'exit_code':result.returncode,
                  'expected_exit_code':args.expected_exit,
                  'matched_expected_exit':payload['matched_expected_exit']}))
sys.stdout.flush()
sys.stdout.buffer.write(result.stdout)
sys.stderr.buffer.write(result.stderr)
sys.exit(0 if payload['matched_expected_exit'] else 1)
