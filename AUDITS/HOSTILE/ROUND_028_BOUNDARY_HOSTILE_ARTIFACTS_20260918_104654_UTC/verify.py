#!/usr/bin/env python3
"""Portable read-only AUD078 verifier. No extraction or filesystem writes.

Run with Python 3.9 or newer and -B. The packet directory defaults to this
script's parent. Optional named siblings are explicit CLI arguments.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tarfile


def require(ok, message):
    if not ok: raise ValueError(message)


def digest(data): return hashlib.sha256(data).hexdigest()


def safe_name(name):
    require(isinstance(name,str) and bool(name),'empty/nonstring member')
    require('\\' not in name and '\x00' not in name,'backslash/NUL member')
    p=PurePosixPath(name)
    require(not p.is_absolute(),'absolute member')
    require(all(x not in ('','..','.') for x in name.split('/')),'unsafe member component')
    require(str(p)==name,'noncanonical member name')
    return name


def scan_tree(root):
    require(not root.is_symlink(),'packet directory is symlink')
    files={}
    for base, dirs, names in os.walk(root,followlinks=False):
        d=Path(base)
        require(not (stat.S_IMODE(d.stat().st_mode)&0o222),'writable packet directory')
        for name in dirs:
            q=d/name
            require(not q.is_symlink() and q.is_dir(),'unsafe packet subdirectory')
        for name in names:
            q=d/name; st=q.lstat()
            require(stat.S_ISREG(st.st_mode),'nonregular packet member')
            require(not (stat.S_IMODE(st.st_mode)&0o222),'writable packet member')
            rel=safe_name(q.relative_to(root).as_posix())
            files[rel]={'bytes':st.st_size,'sha256':digest(q.read_bytes())}
    return files


def check_diagnostic(root):
    env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
    run=subprocess.run([sys.executable,'-B',str(root/'diagnostics.py')],capture_output=True,env=env)
    require(run.returncode==0,'diagnostic rerun failed: '+run.stderr.decode(errors='replace'))
    require(not run.stderr,'diagnostic stderr is nonempty')
    actual=json.loads(run.stdout); expected=json.loads((root/'DIAGNOSTIC_RESULT.json').read_text())
    for field in ('status','assertions','categories','counts','mutation_count','mutations','arithmetic','randomness','continuum_certification'):
        require(actual[field]==expected[field],'diagnostic mismatch: '+field)
    a=actual['examples']['layer_cake_at_17'];e=expected['examples']['layer_cake_at_17']
    for field in ('second','residual'):
        require(abs(a[field]-e[field])<=1e-12*max(1,abs(e[field])),'floating diagnostic mismatch')
    return {k:actual[k] for k in ('status','assertions','categories','mutation_count')}


def validate_archive(archive, inventory, root, files):
    require(not archive.is_symlink() and archive.is_file(),'unsafe archive path')
    inv=json.loads(inventory.read_text())
    prefix=root.name+'/'
    expected={prefix+key:value for key,value in files.items()}
    listed={row['name']:{'bytes':row['bytes'],'sha256':row['sha256']} for row in inv['members']}
    require(len(listed)==len(inv['members']),'duplicate inventory member')
    require(listed==expected,'inventory is incomplete or mismatched')
    seen=set();actual=[]
    with tarfile.open(archive,'r:gz') as tar:
        for member in tar:
            name=safe_name(member.name)
            require(name not in seen,'duplicate archive member');seen.add(name)
            require(member.isreg(),'archive contains a nonregular member')
            require(name in expected,'unexpected archive member')
            require(not (member.mode&0o222),'writable archive member')
            require(member.size==expected[name]['bytes'],'archive size mismatch')
            stream=tar.extractfile(member)
            require(stream is not None,'missing regular archive data')
            data=stream.read(member.size+1)
            got={'bytes':len(data),'sha256':digest(data)}
            require(got==expected[name],'archive content mismatch')
            actual.append({'name':name,**got})
    require(seen==set(expected),'archive missing members')
    return {'regular_members':len(actual),'bytes':archive.stat().st_size,'sha256':digest(archive.read_bytes()),'inventory_sha256':digest(inventory.read_bytes())}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet',type=Path,default=Path(__file__).absolute().parent)
    parser.add_argument('--archive',type=Path)
    parser.add_argument('--inventory',type=Path)
    parser.add_argument('--seal',type=Path)
    parser.add_argument('--report',type=Path)
    parser.add_argument('--sha256sums',type=Path)
    args=parser.parse_args();root=args.packet.absolute()
    for sibling in (args.archive,args.inventory,args.seal,args.report,args.sha256sums):
        if sibling:
            require(not sibling.is_symlink() and sibling.is_file(),'unsafe named sibling')
            require(not (stat.S_IMODE(sibling.stat().st_mode)&0o222),'writable named sibling')
    # Negative lexical tests require no intentionally malformed file writes.
    bad=['','/abs','../x','a/../b','a//b','./a','a/./b','a\\b','a/','a\x00b']
    for name in bad:
        try: safe_name(name)
        except ValueError: pass
        else: raise ValueError('unsafe-name negative test failed')
    files=scan_tree(root)
    manifest=json.loads((root/'CONTENT_MANIFEST.json').read_text())
    expected=manifest['files']
    require(set(files)==set(expected)|{'CONTENT_MANIFEST.json'},'unexpected/missing packet file')
    for name,item in expected.items():
        safe_name(name);require(files[name]==item,'packet digest mismatch: '+name)
    input_rows=[]
    for line in (root/'INPUT_SHA256SUMS.txt').read_text().splitlines():
        sha,name=line.split('  ',1);safe_name(name)
        require(files['INPUTS/'+name]['sha256']==sha,'frozen input mismatch: '+name)
        input_rows.append(name)
    require(len(input_rows)==21 and len(set(input_rows))==21,'wrong frozen input count')
    preflight=json.loads((root/'INPUT_PREFLIGHT.json').read_text())
    require({r['path'] for r in preflight['inputs']}==set(input_rows),'preflight input set')
    for r in preflight['inputs']:
        require(r['original_match'] and r['copy_match'],'failed input preflight')
        require(files['INPUTS/'+r['path']]=={'bytes':r['bytes'],'sha256':r['sha256']},'preflight input digest')
    diagnostics=check_diagnostic(root)
    result={'status':'PASS','inputs':len(input_rows),'packet_files':len(files),'payload_members':len(expected),'packet_manifest_sha256':files['CONTENT_MANIFEST.json']['sha256'],'review_sha256':files['REVIEW.md']['sha256'],'unsafe_name_negative_tests':len(bad),'diagnostics':diagnostics}
    if args.report:
        require(not args.report.is_symlink() and args.report.is_file(),'unsafe external report')
        require(not (stat.S_IMODE(args.report.stat().st_mode)&0o222),'external report writable')
        require(args.report.read_bytes()==(root/'REVIEW.md').read_bytes(),'external report differs')
        result['external_report']='MATCH'
    require(bool(args.archive)==bool(args.inventory),'archive and inventory must be supplied together')
    if args.archive: result['archive']=validate_archive(args.archive,args.inventory,root,files)
    if args.seal:
        require(args.archive and args.report,'seal check needs archive/inventory/report')
        seal=json.loads(args.seal.read_text())
        for field in ('packet_files','payload_members','packet_manifest_sha256','review_sha256','inputs','diagnostics'):
            require(seal['verification'][field]==result[field],'seal mismatch: '+field)
        require(seal['verification']['archive']==result['archive'],'seal archive mismatch')
        require(seal['verification']['status']=='PASS','unpassed seal')
        result['external_seal']='MATCH'
    if args.sha256sums:
        allowed={p.name:p for p in (args.archive,args.inventory,args.seal,args.report) if p}
        observed=set()
        for line in args.sha256sums.read_text().splitlines():
            sha,name=line.split('  ',1);safe_name(name)
            require('/' not in name and name in allowed and name not in observed,'unsafe/unexpected sibling digest')
            observed.add(name)
            require(digest(allowed[name].read_bytes())==sha,'sibling digest mismatch')
        require(observed==set(allowed),'incomplete sibling digest file')
        result['sibling_digests']='MATCH'
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
