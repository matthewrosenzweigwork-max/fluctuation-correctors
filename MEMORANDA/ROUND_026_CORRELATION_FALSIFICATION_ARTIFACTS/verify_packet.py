#!/usr/bin/env python3
"""Portable standard-library read-only verifier. Never extracts archive files."""
import hashlib, json, stat, sys, tarfile
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parent
STEM=ROOT.name
PARENT=ROOT.parent
REPORT=PARENT/'ROUND_026_CORRELATION_FALSIFICATION.md'

def require(ok,message):
    if not ok: raise ValueError(message)
def safe(name):
    require(isinstance(name,str) and bool(name),'empty/nonstring path')
    p=PurePosixPath(name)
    require(not p.is_absolute() and '\\' not in name and '\x00' not in name,'unsafe path: '+name)
    require(all(x not in ('','.','..') for x in name.split('/')),'unsafe component: '+name)
    require(str(p)==name,'noncanonical path: '+name)
    return p
def reg(path):
    require(stat.S_ISREG(path.lstat().st_mode),'not a regular file: '+str(path))
def digest(data): return hashlib.sha256(data).hexdigest()
def sha(path):
    reg(path); return digest(path.read_bytes())
def manifest(path):
    values={}
    for row in path.read_text().splitlines():
        h,name=row.split('  ',1); safe(name)
        require(len(h)==64 and all(x in '0123456789abcdef' for x in h),'bad digest')
        require(name not in values,'duplicate manifest member: '+name)
        values[name]=h
    return values

def main():
    files={}
    for p in ROOT.rglob('*'):
        mode=p.lstat().st_mode
        require(not stat.S_ISLNK(mode),'symlink in directory packet: '+str(p))
        if stat.S_ISDIR(mode):
            require(not mode & 0o222,'writable packet directory: '+str(p))
            continue
        require(stat.S_ISREG(mode),'nonregular packet member: '+str(p))
        require(not mode & 0o222,'writable packet file: '+str(p))
        name=p.relative_to(ROOT).as_posix(); safe(name); files[name]=p
    require(not ROOT.stat().st_mode & 0o222,'writable packet root')
    inputs=manifest(ROOT/'INPUT_SHA256SUMS.txt')
    require(len(inputs)==17,'input row count is not 17')
    for name,h in inputs.items():
        require(sha(ROOT/'INPUTS'/name)==h,'source hash mismatch: '+name)
    inventory=json.loads((ROOT/'INPUT_INVENTORY.json').read_text())
    require(len(inventory)==17,'input inventory count')
    iv={x['path']:x for x in inventory}
    require(set(iv)==set(inputs),'input inventory member set')
    for name,h in inputs.items():
        p=ROOT/'INPUTS'/name
        require(iv[name]['sha256']==h and iv[name]['size']==p.stat().st_size,'input size/hash inventory: '+name)
    actual_inputs={x[len('INPUTS/'):] for x in files if x.startswith('INPUTS/')}
    require(actual_inputs==set(inputs),'extra/missing source copy')
    excluded={'FILE_INVENTORY.json','PAYLOAD_SHA256SUMS.txt'}
    fi=json.loads((ROOT/'FILE_INVENTORY.json').read_text())
    fmap={x['path']:x for x in fi}
    require(len(fmap)==len(fi),'duplicate payload inventory path')
    require(set(fmap)==set(files)-excluded,'payload inventory member set')
    for name,x in fmap.items():
        safe(name)
        require(x['size']==files[name].stat().st_size and x['sha256']==sha(files[name]),'payload inventory mismatch: '+name)
    payload=manifest(ROOT/'PAYLOAD_SHA256SUMS.txt')
    require(set(payload)==set(files)-{'PAYLOAD_SHA256SUMS.txt'},'payload manifest member set')
    for name,h in payload.items(): require(sha(files[name])==h,'payload hash mismatch: '+name)
    archive=PARENT/(STEM+'.tar.gz')
    memberpath=PARENT/(STEM+'.MEMBERS.json')
    memberlist=json.loads(memberpath.read_text())
    expected={x['path']:x for x in memberlist}
    require(len(expected)==len(memberlist),'duplicate external member inventory')
    expected_names={STEM+'/'+x for x in files}
    require(set(expected)==expected_names,'external member set differs from directory')
    seen=set()
    with tarfile.open(archive,'r:gz') as tar:
        for member in tar.getmembers():
            safe(member.name)
            require(member.name not in seen,'duplicate archive member')
            seen.add(member.name)
            require(member.isreg() and not member.issym() and not member.islnk(),'nonregular archive member')
            require(not member.mode & 0o222,'writable archive member')
            require(member.name in expected,'unexpected archive member')
            data=tar.extractfile(member).read()
            x=expected[member.name]
            require(member.size==len(data)==x['size'],'archive size mismatch')
            require(digest(data)==x['sha256'],'archive digest mismatch')
            localname=member.name[len(STEM)+1:]
            require(data==files[localname].read_bytes(),'archive/local byte mismatch')
    require(seen==expected_names,'missing archive member')
    require(REPORT.read_bytes()==(ROOT/'REPORT.md').read_bytes(),'main report differs from packet')
    sealpath=PARENT/(STEM+'.SHA256SUMS.txt')
    seals=manifest(sealpath)
    required={REPORT.name,archive.name,memberpath.name,STEM+'.VERIFICATION.json'}
    require(set(seals)==required,'sibling seal member set')
    for name,h in seals.items():
        p=PARENT/name; require(sha(p)==h,'sibling digest mismatch: '+name)
        require(not p.stat().st_mode & 0o222,'writable sibling: '+name)
    require(not sealpath.stat().st_mode & 0o222,'writable sibling seal')
    print(json.dumps({'status':'PASS','input_rows':len(inputs),'regular_archive_members':len(seen),
      'payload_files':len(files),'unique_safe_regular_members':True,'all_member_digests_checked':True,
      'source_copies_match':True,'local_archive_bytes_match':True,'main_report_matches':True,
      'read_only_permissions':True,'archive_extracted':False,'writes_performed':False},sort_keys=True))
if __name__=='__main__': main()
