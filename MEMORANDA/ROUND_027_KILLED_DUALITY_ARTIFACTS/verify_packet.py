#!/usr/bin/env python3
"""Read-only exact issued-packet checks; no extraction or code execution."""
from pathlib import Path, PurePosixPath
import hashlib,json,stat,tarfile
p=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def safe(n):
    q=PurePosixPath(n)
    assert n and not q.is_absolute() and str(q)==n and '\\' not in n and '\x00' not in n
    assert all(x not in ('','.','..') and ':' not in x for x in n.split('/'))
def read(f):
    m=f.lstat().st_mode;assert stat.S_ISREG(m) and not m&0o222,str(f)
    return f.read_bytes()
assert not p.stat().st_mode&0o222
files={}
for f in p.rglob('*'):
    m=f.lstat().st_mode;assert not stat.S_ISLNK(m) and not m&0o222,str(f)
    if stat.S_ISDIR(m):continue
    rel=f.relative_to(p).as_posix();safe(rel);files[rel]=read(f)
mdata=read(p/'PAYLOAD_MANIFEST.json');manifest=json.loads(mdata)
assert set(files)==set(manifest)|{'PAYLOAD_MANIFEST.json'}
for n,d in manifest.items():
    safe(n);assert len(files[n])==d['bytes'] and sha(files[n])==d['sha256'],n
inputs={}
for line in files['INPUT_SHA256SUMS.txt'].decode().splitlines():
    h,n=line.split('  ',1);safe(n);assert n not in inputs;inputs[n]=h
    assert sha(files['INPUTS/'+n])==h,n
assert len(inputs)==10 and {n[7:] for n in files if n.startswith('INPUTS/')}==set(inputs)
seal=json.loads(read(p.with_name(p.name+'.SEAL.json')))
archive=p.with_name(p.name+'.tar.gz');assert sha(read(archive))==seal['archive_sha256']
assert sha(mdata)==seal['manifest_sha256']
report=read(p.parent/'ROUND_027_KILLED_ATTRACTIVE_DUALITY.md');assert report==files['REPORT.md'] and sha(report)==seal['report_sha256']
seen=set()
with tarfile.open(archive,'r:gz') as tar:
    for mem in tar.getmembers():
        safe(mem.name);assert mem.name not in seen;seen.add(mem.name)
        assert mem.isfile() and not mem.mode&0o222 and not mem.pax_headers
        assert mem.name.startswith(p.name+'/');n=mem.name[len(p.name)+1:]
        assert n in files;data=tar.extractfile(mem).read();assert data==files[n] and mem.size==len(data)
assert seen=={p.name+'/'+n for n in files}
assert seal['member_count']==len(files)
print(json.dumps({'status':'PASS','input_count':len(inputs),'archive_members':len(seen),'read_only_modes':True,'archive_local_bytes_match':True,'safe_unique_regular_members':True,'report_sha256':sha(report),'archive_sha256':sha(read(archive))},indent=2,sort_keys=True))
