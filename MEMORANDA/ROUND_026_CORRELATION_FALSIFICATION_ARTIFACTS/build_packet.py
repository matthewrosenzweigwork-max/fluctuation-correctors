#!/usr/bin/env python3
"""One-time pre-issuance packaging. Do not run against already sealed evidence."""
import gzip, hashlib, io, json, os, stat, subprocess, sys, tarfile
from pathlib import Path

root=Path(__file__).resolve().parent
parent=root.parent
stem=root.name
report=parent/'ROUND_026_CORRELATION_FALSIFICATION.md'
archive=parent/(stem+'.tar.gz')
members_path=parent/(stem+'.MEMBERS.json')
verification=parent/(stem+'.VERIFICATION.json')
seal=parent/(stem+'.SHA256SUMS.txt')
for p in (archive,members_path,verification,seal):
    if p.exists(): raise SystemExit('Refusing to overwrite existing packet sibling: '+str(p))
(root/'REPORT.md').write_bytes(report.read_bytes())

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def files():
    out=[]
    for p in root.rglob('*'):
        mode=p.lstat().st_mode
        if stat.S_ISLNK(mode) or not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
            raise SystemExit('Nonregular/symlink packet item: '+str(p))
        if stat.S_ISREG(mode): out.append(p)
    return sorted(out,key=lambda x:x.relative_to(root).as_posix())

excluded={'FILE_INVENTORY.json','PAYLOAD_SHA256SUMS.txt'}
base=[p for p in files() if p.name not in excluded]
fi=[{'path':p.relative_to(root).as_posix(),'size':p.stat().st_size,'sha256':sha(p)} for p in base]
(root/'FILE_INVENTORY.json').write_text(json.dumps(fi,indent=2)+'\n')
manifest_files=[p for p in files() if p.name!='PAYLOAD_SHA256SUMS.txt']
(root/'PAYLOAD_SHA256SUMS.txt').write_text(''.join(sha(p)+'  '+p.relative_to(root).as_posix()+'\n' for p in manifest_files))
allfiles=files()
member_inventory=[]
with archive.open('wb') as af:
    with gzip.GzipFile(filename='',mode='wb',fileobj=af,mtime=0) as gz:
        with tarfile.open(mode='w',fileobj=gz,format=tarfile.USTAR_FORMAT) as tar:
            for p in allfiles:
                data=p.read_bytes(); name=stem+'/'+p.relative_to(root).as_posix()
                ti=tarfile.TarInfo(name)
                ti.size=len(data); ti.mode=0o444; ti.mtime=0; ti.uid=ti.gid=0
                ti.uname=ti.gname=''
                tar.addfile(ti,io.BytesIO(data))
                member_inventory.append({'path':name,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()})
members_path.write_text(json.dumps(member_inventory,indent=2)+'\n')
# Temporary honest record for the first full read-only integrity check.
# Its replacement below occurs before issuance and is followed by a second check.
verification.write_text(json.dumps({'status':'PENDING_PRE_ISSUANCE_CHECK'},sort_keys=True)+'\n')
def write_seal():
    seal.write_text(''.join(sha(p)+'  '+p.name+'\n' for p in (report,archive,members_path,verification)))
write_seal()
for p in allfiles+[report,archive,members_path,verification,seal]: p.chmod(0o444)
for p in sorted([p for p in root.rglob('*') if p.is_dir()],key=lambda x:len(x.parts),reverse=True): p.chmod(0o555)
root.chmod(0o555)
cmd=[sys.executable,str(root/'verify_packet.py')]
first=subprocess.run(cmd,text=True,capture_output=True)
if first.returncode: raise SystemExit(first.stdout+first.stderr)
result=json.loads(first.stdout)
verification.chmod(0o644); seal.chmod(0o644)
verification.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
write_seal()
verification.chmod(0o444); seal.chmod(0o444)
final=subprocess.run(cmd,text=True,capture_output=True)
if final.returncode: raise SystemExit(final.stdout+final.stderr)
if json.loads(final.stdout)!=result: raise SystemExit('Final verification differed')
print(final.stdout.strip())
print(json.dumps({'archive_sha256':sha(archive),'seal_sha256':sha(seal),'archive_bytes':archive.stat().st_size},sort_keys=True))
