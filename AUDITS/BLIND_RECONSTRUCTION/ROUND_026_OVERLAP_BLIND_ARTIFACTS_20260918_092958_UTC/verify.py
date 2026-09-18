#!/usr/bin/env python3
"""Portable read-only AUD073 verifier. No extraction, network or writes.

The internal payload manifest excludes only itself. REGULAR_MEMBERS.txt includes
itself and the payload manifest. A sibling archive inventory hashes every
regular member, including both internal controls. The sibling SHA256SUMS seals
the issued report, archive, complete archive inventory, and validation receipt.
The seal's own externally communicated digest closes the final trust boundary.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path,PurePosixPath
import stat
import subprocess
import sys
import tarfile

def digest(data):return hashlib.sha256(data).hexdigest()
def safe(name):
    p=PurePosixPath(name)
    if not name or '\\' in name or p.is_absolute() or str(p)!=name or any(x in ('','.','..') for x in p.parts):
        raise ValueError('unsafe relative path: '+repr(name))
    return name

def sha_lines(path):
    out={}
    for line in path.read_text().splitlines():
        h,n=line.split('  ',1);safe(n)
        if len(h)!=64 or any(x not in '0123456789abcdef' for x in h):raise ValueError('bad SHA256')
        if n in out:raise ValueError('duplicate manifest path '+n)
        out[n]=h
    return out

def require(flag,message):
    if not flag:raise AssertionError(message)

def run(args):
    root=Path(__file__).absolute().parent
    require(not root.is_symlink(),'packet root is a symlink')
    regular={}
    for p in root.rglob('*'):
        mode=p.lstat().st_mode
        require(not stat.S_ISLNK(mode),'symlink: '+str(p))
        if stat.S_ISDIR(mode):continue
        require(stat.S_ISREG(mode),'nonregular object: '+str(p))
        n=safe(p.relative_to(root).as_posix())
        regular[n]=p
    initial_digests={n:digest(p.read_bytes()) for n,p in regular.items()}
    names=(root/'REGULAR_MEMBERS.txt').read_text().splitlines()
    require(len(names)==len(set(names)),'duplicate regular-member entry')
    for n in names:safe(n)
    require(names==sorted(regular),'regular-member inventory is incomplete or unsorted')
    payload=sha_lines(root/'PAYLOAD_SHA256SUMS.txt')
    require(set(payload)==set(regular)-{'PAYLOAD_SHA256SUMS.txt'},'payload membership mismatch')
    for n,h in payload.items():require(digest(regular[n].read_bytes())==h,'payload hash mismatch: '+n)
    inputs=sha_lines(root/'INPUT_SHA256SUMS.txt')
    require(len(inputs)==12,'input count is not twelve')
    for n,h in inputs.items():require(digest((root/'inputs'/n).read_bytes())==h,'input mismatch: '+n)
    iv=json.loads((root/'INPUT_VERIFICATION.json').read_text())
    require(iv['all_12_passed'] is True,'input receipt not PASS')
    require(iv['manifest_sha256']==digest((root/'INPUT_SHA256SUMS.txt').read_bytes()),'input manifest receipt mismatch')
    require({x['path']:x['sha256'] for x in iv['inputs']}==inputs,'input receipt member mismatch')
    env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
    comp=subprocess.run([sys.executable,str(root/'diagnostics.py')],capture_output=True,text=True,env=env,check=False)
    require(comp.returncode==0,'diagnostics failure: '+comp.stderr)
    actual=json.loads(comp.stdout)
    expected=json.loads((root/'results'/'diagnostics_run_001.json').read_text())
    require(actual==expected,'diagnostics do not reproduce the entire saved result')
    require(actual['status']=='PASS','saved diagnostics are not PASS')
    archive_count=None
    if args.archive or args.inventory:
        require(args.archive and args.inventory,'archive and inventory must be given together')
        archive=Path(args.archive);inventory=Path(args.inventory)
        require(not archive.is_symlink() and not inventory.is_symlink(),'sibling symlink')
        spec=json.loads(inventory.read_text())
        require(spec['archive']==archive.name,'archive name mismatch')
        require(spec['sha256']==digest(archive.read_bytes()),'archive digest mismatch')
        members={x['path']:x for x in spec['regular_members']}
        require(len(members)==len(spec['regular_members']),'duplicate archive inventory paths')
        seen=set()
        with tarfile.open(archive,'r:gz') as tar:
            for item in tar:
                n=safe(item.name)
                require(item.isfile(),'nonregular tar member: '+n)
                require(n not in seen,'duplicate tar member: '+n);seen.add(n)
                require(n in members,'unlisted tar member: '+n)
                require(n.startswith(root.name+'/'),'unexpected archive prefix: '+n)
                rel=safe(n[len(root.name)+1:])
                require(rel in regular,'archive file not in packet: '+rel)
                f=tar.extractfile(item);require(f is not None,'unreadable tar member')
                content=f.read()
                require(len(content)==item.size==members[n]['size'],'member size mismatch: '+n)
                require(digest(content)==members[n]['sha256'],'member digest mismatch: '+n)
                require(content==regular[rel].read_bytes(),'archive and directory differ: '+rel)
                require(item.mode==0o444,'archive member is not read-only: '+n)
        require(seen==set(members),'missing archive member')
        require(len(seen)==len(regular),'archive/packet count mismatch')
        archive_count=len(seen)
    if args.report:
        report=Path(args.report)
        require(not report.is_symlink() and report.is_file(),'unsafe issued report')
        require(report.read_bytes()==(root/'RECONSTRUCTION.md').read_bytes(),'issued report differs')
    if args.seal:
        seal=Path(args.seal)
        require(not seal.is_symlink(),'seal symlink')
        for n,h in sha_lines(seal).items():
            p=seal.parent/n
            require(p.is_file() and not p.is_symlink(),'unsafe sealed sibling: '+n)
            require(digest(p.read_bytes())==h,'sibling hash mismatch: '+n)
    # Re-inventory after the diagnostic subprocess to confirm no writes/additions.
    after={p.relative_to(root).as_posix():digest(p.read_bytes()) for p in root.rglob('*') if p.is_file()}
    require(after==initial_digests,'verification created, removed or changed files')
    return {'status':'PASS','packet_regular_files':len(regular),'exact_inputs_verified':12,'diagnostic_checks':actual['check_count'],'nonzero_mutations_rejected':actual['mutation_count'],'full_diagnostic_output_reproduced':True,'archive_regular_members_verified':archive_count,'read_only':True,'scope':'integrity and reproducibility; mathematical verdict is in RECONSTRUCTION.md'}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive');parser.add_argument('--inventory');parser.add_argument('--seal');parser.add_argument('--report')
    args=parser.parse_args()
    try:
        print(json.dumps(run(args),indent=2,sort_keys=True))
    except Exception as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)},indent=2),file=sys.stderr)
        raise SystemExit(1)
