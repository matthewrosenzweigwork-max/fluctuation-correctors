#!/usr/bin/env python3
"""Portable read-only packet/byte/archive verifier. Python >=3.9, stdlib only."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tarfile

ROOT_NAME = 'ROUND_025_ULTRA_CRITICAL_THRESHOLD_ARTIFACTS'
MEMO_NAME = 'ROUND_025_ULTRA_CRITICAL_THRESHOLD_ATTEMPT.md'

def require(condition, message):
    if not condition:
        raise ValueError(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def safe_name(name):
    require(isinstance(name,str) and name != '', 'empty/nontext member')
    require('\\' not in name and '\x00' not in name, 'unsafe member characters')
    p=PurePosixPath(name)
    require(not p.is_absolute(), 'absolute member')
    require(all(x not in ('','..','.') for x in name.split('/')), 'unsafe member components')
    require(p.parts[0] == ROOT_NAME and len(p.parts)>1,'wrong archive root')
    return name

def metadata(data):
    return {'sha256':digest(data),'bytes':len(data)}

def self_controls():
    controls=0
    for bad in ['', '/etc/passwd', ROOT_NAME+'/../x', ROOT_NAME+'/./x',
                ROOT_NAME+'//x', 'OTHER/x', ROOT_NAME+'/x\\y']:
        try: safe_name(bad)
        except ValueError: controls+=1
        else: raise AssertionError('unsafe-name control accepted '+bad)
    good=ROOT_NAME+'/README.md'
    require(safe_name(good)==good,'safe positive control')
    try: require(len([good,good]) == len(set([good,good])),'duplicate control')
    except ValueError: controls+=1
    else: raise AssertionError('duplicate control accepted')
    try: require(digest(b'alpha')==digest(b'alphb'),'digest control')
    except ValueError: controls+=1
    else: raise AssertionError('digest control accepted')
    info=tarfile.TarInfo(good); info.type=tarfile.SYMTYPE; info.linkname='elsewhere'
    try: require(info.isreg(),'nonregular control')
    except ValueError: controls+=1
    else: raise AssertionError('symlink control accepted')
    return controls

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--packet',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--archive',type=Path)
    parser.add_argument('--seal',type=Path)
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--run-diagnostic',action='store_true')
    args=parser.parse_args()
    packet=args.packet.resolve()
    archive=args.archive or packet.parent/(ROOT_NAME+'.tar.gz')
    seal_path=args.seal or packet.parent/(ROOT_NAME+'.SEAL.json')
    seal=json.loads(seal_path.read_text())
    require(seal['packet_root']==ROOT_NAME,'packet root in seal')
    require(metadata(archive.read_bytes())==seal['archive'],'archive digest or size mismatch')
    expected=seal['members']
    require(len(expected)>26,'implausible inventory')
    for n in expected: safe_name(n)
    actual={}
    for path in packet.rglob('*'):
        require(not path.is_symlink(),'local symlink: '+str(path))
        if path.is_dir(): continue
        require(path.is_file(),'local nonregular file: '+str(path))
        relative=path.relative_to(packet).as_posix()
        name=ROOT_NAME+'/'+relative
        safe_name(name)
        actual[name]=metadata(path.read_bytes())
        require(stat.S_IMODE(path.stat().st_mode)&0o222 == 0,'local writable file: '+relative)
    require(actual==expected,'local file/member inventory mismatch')
    archive_members={}
    with tarfile.open(archive,'r:gz') as tar:
        for member in tar:
            safe_name(member.name)
            require(member.isreg(),'archive nonregular member '+member.name)
            require(member.name not in archive_members,'archive duplicate member '+member.name)
            require(member.mode&0o222 == 0,'archive writable mode '+member.name)
            data=tar.extractfile(member).read()
            require(len(data)==member.size,'archive declared size mismatch')
            archive_members[member.name]=metadata(data)
    require(archive_members==expected,'archive exact byte/member inventory mismatch')
    lines=(packet/'INPUT_SHA256SUMS.txt').read_text().splitlines()
    require(len(lines)==26,'input allowlist count changed')
    seen=set()
    input_inventory=[]
    for line in lines:
        sha,rel=line.split('  ',1)
        require(rel not in seen,'duplicate input'); seen.add(rel)
        safe_name(ROOT_NAME+'/INPUTS/'+rel)
        data=(packet/'INPUTS'/rel).read_bytes()
        require(digest(data)==sha,'input digest mismatch: '+rel)
        input_inventory.append({'path':rel,**metadata(data)})
        if args.source_root:
            require(digest((args.source_root/rel).read_bytes())==sha,'original source changed: '+rel)
    require(input_inventory==json.loads((packet/'INPUT_INVENTORY.json').read_text()),'input inventory mismatch')
    payload_lines=(packet/'PAYLOAD_SHA256SUMS.txt').read_text().splitlines()
    payload_paths=[]
    for line in payload_lines:
        sha,rel=line.split('  ',1)
        require(digest((packet/rel).read_bytes())==sha,'payload digest mismatch '+rel)
        payload_paths.append(rel)
    expected_payload=sorted(n.split('/',1)[1] for n in expected
                            if n.split('/',1)[1] not in ('PAYLOAD_SHA256SUMS.txt','PAYLOAD_INVENTORY.json'))
    require(payload_paths==expected_payload,'payload manifest completeness mismatch')
    payload_json=json.loads((packet/'PAYLOAD_INVENTORY.json').read_text())
    require(payload_json==[{'path':p,**metadata((packet/p).read_bytes())} for p in payload_paths],
            'payload inventory mismatch')
    report=(packet/'REPORT.md').read_bytes()
    require(metadata(report)==seal['memorandum'],'memorandum packet mismatch')
    sibling=packet.parent/MEMO_NAME
    if sibling.exists():
        require(sibling.read_bytes()==report,'sibling memorandum differs')
        require(stat.S_IMODE(sibling.stat().st_mode)&0o222==0,'sibling memorandum writable')
    require(stat.S_IMODE(archive.stat().st_mode)&0o222==0,'archive writable')
    require(stat.S_IMODE(seal_path.stat().st_mode)&0o222==0,'seal writable')
    result=json.loads((packet/'DIAGNOSTIC_RESULT.json').read_text())
    require(result['script_sha256']==digest((packet/'round025_tail_diagnostic.py').read_bytes()),'diagnostic script mismatch')
    diagnostic='recorded result verified'
    if args.run_diagnostic:
        completed=subprocess.run([sys.executable,str(packet/'round025_tail_diagnostic.py')],
                                 check=True,text=True,capture_output=True)
        rerun=json.loads(completed.stdout)
        require(rerun=={'status':'PASS','assertions':result['assertions'],
                       'categories':len(result['categories']),'mutation_types':result['mutation_types']},
                'diagnostic rerun mismatch')
        diagnostic=rerun
    print(json.dumps({'status':'PASS','inputs':26,'regular_archive_members':len(expected),
                      'payload_files':len(payload_paths),'malformed_or_corruption_controls':self_controls(),
                      'diagnostic':diagnostic,'archive_sha256':seal['archive']['sha256'],
                      'original_sources_checked':bool(args.source_root)},sort_keys=True))

if __name__=='__main__':
    main()
