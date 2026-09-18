#!/usr/bin/env python3
"""One-use AUD072 issuance, retained as the exact packaging provenance.

Writes only the assigned packet and its named sibling artifacts. Refuses
existing sibling outputs; do not rerun on an issued packet. Verification
after issuance is performed by verify_read_only.py, which never writes.
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


packet=Path(__file__).absolute().parent
parent=packet.parent
prefix=packet.name
external_report=parent/'ROUND_026_RESPONSE_REVIEW.md'
archive=parent/(prefix+'.tar.gz')
inventory_path=parent/(prefix+'.INVENTORY.json')
core_path=parent/(prefix+'.CORE_VERIFICATION.json')
seal_path=parent/(prefix+'.SHA256SUMS')
for path in (archive,inventory_path,core_path,seal_path,packet/'REPORT.md'):
    if path.exists() or path.is_symlink():
        raise SystemExit('Refusing to replace existing issuance artifact: '+str(path))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_new(path,data):
    with path.open('xb') as handle:
        handle.write(data)
    path.chmod(0o444)


def json_bytes(obj):
    return (json.dumps(obj,indent=2,ensure_ascii=False)+'\n').encode('utf-8')


source_rows=[]
for line in (packet/'INPUT_SHA256SUMS.txt').read_text().splitlines():
    value,rel=line.split('  ',1)
    assert sha((packet/'INPUTS'/rel).read_bytes())==value,rel
    source_rows.append(rel)
assert len(source_rows)==13
write_new(packet/'REPORT.md',external_report.read_bytes())
external_report.chmod(0o444)

files=[]
directories=[]
for base,subdirs,names in os.walk(str(packet),followlinks=False):
    base=Path(base)
    for name in subdirs:
        path=base/name
        assert stat.S_ISDIR(path.lstat().st_mode),path
        directories.append(path.relative_to(packet).as_posix())
    for name in names:
        path=base/name
        assert stat.S_ISREG(path.lstat().st_mode),path
        path.chmod(0o444)
        data=path.read_bytes()
        files.append({'path':path.relative_to(packet).as_posix(),
                      'bytes':len(data),'mode':'0444','sha256':sha(data)})
files.sort(key=lambda row:row['path'])
directories.sort()
inventory={'format':'AUD072-portable-regular-inventory-v1',
           'packet_name':prefix,'directories':directories,'files':files}
write_new(inventory_path,json_bytes(inventory))

with archive.open('xb') as raw:
    with gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as compressed:
        with tarfile.open(fileobj=compressed,mode='w',format=tarfile.PAX_FORMAT) as handle:
            for row in files:
                data=(packet/row['path']).read_bytes()
                info=tarfile.TarInfo(prefix+'/'+row['path'])
                info.type=tarfile.REGTYPE
                info.mode=0o444
                info.uid=info.gid=0
                info.uname=info.gname=''
                info.mtime=0
                info.size=len(data)
                handle.addfile(info,io.BytesIO(data))
archive.chmod(0o444)

command=[sys.executable,str(packet/'verify_read_only.py'),'--skip-seal']
core=subprocess.run(command,capture_output=True,text=True)
if core.returncode!=0:
    print(core.stdout)
    print(core.stderr,file=sys.stderr)
    raise SystemExit('Core verification failed before issuance seal; no success claim.')
result=json.loads(core.stdout)
result['executed_command']=command
result['exit_code']=core.returncode
result['stderr']=core.stderr
result['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
write_new(core_path,json_bytes(result))

seal_rows={prefix+'/'+row['path']:row['sha256'] for row in files}
for path in (archive,inventory_path,core_path,external_report):
    seal_rows[path.name]=sha(path.read_bytes())
seal_data=''.join('{}  {}\n'.format(value,name) for name,value in sorted(seal_rows.items()))
write_new(seal_path,seal_data.encode('utf-8'))
for rel in sorted(directories,key=lambda s:s.count('/'),reverse=True):
    (packet/rel).chmod(0o555)
packet.chmod(0o555)

final_command=[sys.executable,str(packet/'verify_read_only.py')]
final=subprocess.run(final_command,capture_output=True,text=True)
print(final.stdout,end='')
if final.stderr:
    print(final.stderr,file=sys.stderr,end='')
if final.returncode!=0:
    raise SystemExit('Final verification failed; immutable bytes require a superseding artifact.')
print('assigned_report_sha256='+sha(external_report.read_bytes()))
print('archive_sha256='+sha(archive.read_bytes()))
print('inventory_sha256='+sha(inventory_path.read_bytes()))
print('seal_sha256='+sha(seal_path.read_bytes()))
