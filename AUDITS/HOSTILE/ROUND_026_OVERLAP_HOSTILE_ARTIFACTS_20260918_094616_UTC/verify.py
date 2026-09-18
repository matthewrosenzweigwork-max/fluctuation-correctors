#!/usr/bin/env python3
"""Portable AUD074 verifier: reads only, never extracts or writes."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tarfile

def need(test,message):
    if not test:
        raise ValueError(message)

def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()

def digest_file(path):
    hh=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            hh.update(block)
    return hh.hexdigest()

def safe_relative(name,allow_dot=False):
    need(isinstance(name,str) and name,'empty or nonstring path')
    need('\\' not in name and '\x00' not in name,'unsafe path character')
    pp=PurePosixPath(name)
    need(not pp.is_absolute(),'absolute path')
    need('..' not in pp.parts,'parent traversal')
    if name=='.' and allow_dot:
        return
    need(pp.parts and '.' not in pp.parts and name==pp.as_posix(),
         'noncanonical relative path: '+name)

def regular(path):
    st=path.lstat()
    need(stat.S_ISREG(st.st_mode) and not path.is_symlink(),
         'not an independent regular file: '+str(path))
    need(st.st_nlink==1,'hard-linked file: '+str(path))
    need(st.st_mode & 0o222 == 0,'writable file: '+str(path))
    return st

def mathematical_equal(a,b):
    if isinstance(a,float) or isinstance(b,float):
        return (isinstance(a,(float,int)) and isinstance(b,(float,int))
                and math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12))
    if type(a) is not type(b):
        return False
    if isinstance(a,dict):
        return set(a)==set(b) and all(mathematical_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(mathematical_equal(x,y) for x,y in zip(a,b))
    return a==b

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rerun-diagnostic',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).absolute().parent
    parent=root.parent
    stem=root.name
    invpath=parent/(stem+'_INVENTORY.json')
    archive=parent/(stem+'.tar.gz')
    seals=parent/(stem+'_SHA256SUMS.txt')
    report=parent/'ROUND_026_OVERLAP_REVIEW.md'
    need(root.is_dir() and not root.is_symlink(),'packet root is not a real directory')
    for path in (invpath,archive,seals,report):
        regular(path)
    inventory=json.loads(invpath.read_text())
    need(inventory['format']=='AUD074 complete regular-member inventory v1',
         'unexpected inventory format')
    need(inventory['packet_name']==stem,'packet name differs')
    expected_files={}
    for rec in inventory['regular_files']:
        safe_relative(rec['path'])
        need(rec['path'] not in expected_files,'duplicate file inventory')
        need(rec['mode']==0o444,'unexpected file mode in inventory')
        expected_files[rec['path']]=rec
    expected_dirs={}
    for rec in inventory['directories']:
        safe_relative(rec['path'],True)
        need(rec['path'] not in expected_dirs,'duplicate directory inventory')
        need(rec['mode']==0o555,'unexpected directory mode in inventory')
        expected_dirs[rec['path']]=rec
    seen_files=set()
    seen_dirs=set()
    for base,dirnames,filenames in os.walk(root,followlinks=False):
        base=Path(base)
        rel=base.relative_to(root).as_posix()
        st=base.lstat()
        need(stat.S_ISDIR(st.st_mode) and not base.is_symlink(),'unsafe directory')
        need(stat.S_IMODE(st.st_mode)==0o555,'directory mode differs')
        seen_dirs.add(rel)
        for d in dirnames:
            need(not (base/d).is_symlink(),'symlink directory')
        for f in filenames:
            path=base/f
            relf=path.relative_to(root).as_posix()
            safe_relative(relf)
            need(relf in expected_files,'unexpected file: '+relf)
            st=regular(path)
            rec=expected_files[relf]
            need(stat.S_IMODE(st.st_mode)==rec['mode'],'file mode differs: '+relf)
            need(st.st_size==rec['size'],'file size differs: '+relf)
            need(digest_file(path)==rec['sha256'],'file digest differs: '+relf)
            seen_files.add(relf)
    need(seen_files==set(expected_files),'missing file inventory members')
    need(seen_dirs==set(expected_dirs),'directory inventory differs')
    rrec=inventory['external_report']
    need(rrec['name']==report.name,'report name differs')
    need(report.stat().st_size==rrec['size'],'report size differs')
    need(digest_file(report)==rrec['sha256'],'report digest differs')
    need((root/'REPORT.md').read_bytes()==report.read_bytes(),'report copy differs')
    # Seal every externally referenced object; the seal itself is later
    # covered by the separately issued verification attestation.
    sealrows={}
    for line in seals.read_text().splitlines():
        expected,name=line.split('  ',1)
        safe_relative(name)
        need(len(PurePosixPath(name).parts)==1,'seal escapes sibling directory')
        need(name not in sealrows,'duplicate seal path')
        sealrows[name]=expected
    need(set(sealrows)=={invpath.name,archive.name,report.name},
         'incomplete or extra seal inventory')
    for name,expected in sealrows.items():
        need(digest_file(parent/name)==expected,'sibling seal mismatch: '+name)
    # Exact original allowlist and copy hashes, without reading live workspace.
    rows=(root/'INPUTS_ORIGINAL_SHA256SUMS.txt').read_text().splitlines()
    need(len(rows)==15,'not exactly 15 original inputs')
    allowed=set()
    for line in rows:
        expected,name=line.split('  ',1)
        safe_relative(name)
        need(name not in allowed,'duplicate original input')
        allowed.add(name)
        need(digest_file(root/'INPUTS'/name)==expected,'input-copy mismatch')
    actual_inputs={name[len('INPUTS/'):] for name in expected_files
                   if name.startswith('INPUTS/')}
    need(allowed==actual_inputs,'input-copy inventory differs from allowlist')
    # Validate all archive member names, types, sizes and content in memory.
    archive_expected={}
    for rel,rec in expected_dirs.items():
        name=stem if rel=='.' else stem+'/'+rel
        archive_expected[name]=('directory',rec)
    for rel,rec in expected_files.items():
        archive_expected[stem+'/'+rel]=('file',rec)
    seen=set()
    with tarfile.open(archive,'r:gz') as tar:
        for member in tar:
            name=member.name.rstrip('/') if member.isdir() else member.name
            safe_relative(name)
            need(name not in seen,'duplicate archive member')
            need(name in archive_expected,'unexpected archive member: '+name)
            kind,rec=archive_expected[name]
            need(not member.issym() and not member.islnk(),'archive link')
            need(not member.isdev() and not member.isfifo(),'archive special file')
            if kind=='directory':
                need(member.isdir() and member.size==0,'archive directory type/size')
                need(member.mode==0o555,'archive directory mode')
            else:
                need(member.isreg(),'archive regular-member type')
                need(member.mode==0o444,'archive regular-member mode')
                need(member.size==rec['size'],'archive member size')
                stream=tar.extractfile(member)
                need(stream is not None,'unreadable archive regular member')
                hh=hashlib.sha256()
                total=0
                for block in iter(lambda:stream.read(1024*1024),b''):
                    total+=len(block)
                    hh.update(block)
                need(total==rec['size'],'archive byte count')
                need(hh.hexdigest()==rec['sha256'],'archive digest differs')
            seen.add(name)
    need(seen==set(archive_expected),'archive member inventory incomplete')
    rerun='not requested'
    result=json.loads((root/'RUN_001_STDOUT.json').read_text())
    need(result['verdict']=='PASS','recorded diagnostic did not pass')
    need(result['assertion_count']==187032 and result['mutation_count']==20,
         'recorded diagnostic count differs')
    need(len(result['categories'])==25,'recorded category count differs')
    process=json.loads((root/'RUN_001_PROCESS.json').read_text())
    need(process['returncode']==0,'saved process exit differs')
    need((root/'RUN_001_STDERR.txt').read_bytes()==b'','saved diagnostic stderr')
    if args.rerun_diagnostic:
        run=subprocess.run([sys.executable,'-B',str(root/'diagnostic.py')],
                           capture_output=True,text=True)
        need(run.returncode==0,'diagnostic rerun failed: '+run.stderr)
        need(not run.stderr,'diagnostic rerun stderr')
        current=json.loads(run.stdout)
        saved=dict(result)
        current.pop('python',None)
        saved.pop('python',None)
        need(mathematical_equal(current,saved),'diagnostic mathematical output differs')
        rerun='PASS; every recorded mathematical output reproduced'
    print(json.dumps({
        'verdict':'PASS','packet':stem,
        'regular_files':len(expected_files),'directories':len(expected_dirs),
        'archive_members':len(archive_expected),'allowed_inputs':15,
        'complete_digest_inventory':'PASS','archive_no_extraction':'PASS',
        'report_copy':'PASS','read_only_modes':'PASS',
        'diagnostic_rerun':rerun,
        'assertions':result['assertion_count'],'categories':len(result['categories']),
        'nonzero_mutations':result['mutation_count'],
        'writes_performed':False
    },indent=2,sort_keys=True))

if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        print(json.dumps({'verdict':'FAIL','error':str(exc)},indent=2),file=sys.stderr)
        sys.exit(1)
