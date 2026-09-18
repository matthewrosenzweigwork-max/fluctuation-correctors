#!/usr/bin/env python3
"""Read-only exact packet/archive verification for AUD064. Never extracts."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import stat
import subprocess
import sys
import tarfile


CONTROL_SHA256='5d890a38e495176aa4efccae2c10f7ff0098aa17ee028448ec42815d7b7003ec'
REPORT_NAME='ROUND_022_DISTRIBUTION_PATH_REVIEW.md'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def digest_file(path):
    require(path.is_file() and not path.is_symlink(), f'Not a regular local file: {path}')
    return digest_bytes(path.read_bytes())


def safe_name(name):
    require(isinstance(name,str) and name and '\x00' not in name and '\\' not in name,
            f'Unsafe name: {name!r}')
    p=PurePosixPath(name)
    require(not p.is_absolute() and all(part not in ('','..','.') for part in p.parts)
            and p.as_posix()==name, f'Unsafe relative name: {name!r}')
    return p


def read_manifest(path):
    data=path.read_bytes()
    require(data.endswith(b'\n'),f'Missing manifest final newline: {path}')
    parsed={}
    for line in data.decode('utf-8').splitlines():
        require('  ' in line, f'Invalid manifest line: {line!r}')
        digest,name=line.split('  ',1)
        safe_name(name)
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),
                f'Invalid digest: {digest!r}')
        require(name not in parsed,f'Duplicate manifest member: {name}')
        parsed[name]=digest
    return parsed


def regular_tree(root):
    require(root.is_dir() and not root.is_symlink(),f'Invalid packet root: {root}')
    files={}
    for path in root.rglob('*'):
        require(not path.is_symlink(),f'Link in packet: {path}')
        if path.is_dir():
            continue
        require(path.is_file(),f'Nonregular packet member: {path}')
        rel=path.relative_to(root).as_posix()
        safe_name(rel)
        files[rel]=path
    return files


def readonly(path):
    require(stat.S_IMODE(path.stat().st_mode)&0o222==0,f'Writable issued path: {path}')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive',type=Path,required=True)
    parser.add_argument('--members',type=Path,required=True)
    parser.add_argument('--seal',type=Path)
    args=parser.parse_args()
    packet=Path(__file__).resolve().parent
    files=regular_tree(packet)
    inputs=read_manifest(packet/'INPUT_SHA256SUMS.txt')
    require(len(inputs)==19,'Input count must be exactly nineteen')
    require(digest_file(packet/'INPUT_SHA256SUMS.txt')==CONTROL_SHA256,'Control manifest differs')
    input_local={name[len('inputs/'):]:path for name,path in files.items() if name.startswith('inputs/')}
    require(set(input_local)==set(inputs),'Input copy member set differs')
    for name,expected in inputs.items():
        require(digest_file(input_local[name])==expected,f'Input copy byte mismatch: {name}')

    outputs=read_manifest(packet/'OUTPUT_SHA256SUMS.txt')
    require(set(outputs)==set(files)-{'OUTPUT_SHA256SUMS.txt'},'Output manifest member set differs')
    for name,expected in outputs.items():
        require(digest_file(files[name])==expected,f'Output byte mismatch: {name}')
    standalone=packet.parent/REPORT_NAME
    require(standalone.read_bytes()==(packet/REPORT_NAME).read_bytes(),'Standalone report differs from packet')

    expected_members=read_manifest(args.members)
    archive_names={f'{packet.name}/{name}' for name in files}
    require(set(expected_members)==archive_names,'Archive manifest must list exact complete packet')
    seen=set(); total_bytes=0
    with tarfile.open(args.archive,'r:gz') as archive:
        for member in archive:
            safe_name(member.name)
            require(member.name not in seen,f'Duplicate archive member: {member.name}')
            seen.add(member.name)
            require(member.isfile() and not member.islnk() and not member.issym(),
                    f'Nonregular archive member: {member.name}')
            require(member.name in expected_members,f'Unexpected archive member: {member.name}')
            require(0<=member.size<=1_000_000,f'Unexpected archive size: {member.name}')
            require(member.mode&0o222==0,f'Writable archive member: {member.name}')
            stream=archive.extractfile(member)
            require(stream is not None,f'Unreadable regular member: {member.name}')
            with stream:
                data=stream.read(member.size+1)
            require(len(data)==member.size,f'Archive size mismatch: {member.name}')
            require(digest_bytes(data)==expected_members[member.name],
                    f'Archive digest mismatch: {member.name}')
            rel=member.name[len(packet.name)+1:]
            require(data==files[rel].read_bytes(),f'Archive/local byte mismatch: {member.name}')
            total_bytes+=len(data)
    require(seen==archive_names,'Missing archive members')

    saved=(packet/'diagnostic_results.json').read_bytes()
    replay=subprocess.run([sys.executable,str(packet/'round022_hostile_exact.py')],
                          check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    require(replay.stdout==saved,'Diagnostic result is not an exact reproducible byte string')
    result=json.loads(saved)
    require(result['status']=='PASS' and result['assertions']==28182
            and len(result['categories'])==17 and result['mutation_count']==17,
            'Unexpected diagnostic result')
    require(result['program_sha256']==digest_file(packet/'round022_hostile_exact.py'),
            'Diagnostic program digest differs')

    component_digests={
        'archive':digest_file(args.archive),
        'archive_members_manifest':digest_file(args.members),
        'output_manifest':digest_file(packet/'OUTPUT_SHA256SUMS.txt'),
        'input_manifest':digest_file(packet/'INPUT_SHA256SUMS.txt'),
        'standalone_report':digest_file(standalone),
    }
    seal_digest=None
    if args.seal:
        seal=json.loads(args.seal.read_bytes())
        require(seal['component_sha256']==component_digests,'Seal component hashes differ')
        require(seal['input_files']==19 and seal['packet_files']==len(files)
                and seal['archive_members']==len(seen),'Seal counts differ')
        require(seal['archive_uncompressed_bytes']==total_bytes,'Seal archive byte count differs')
        require(seal['audit']=='AUD064' and seal['task']=='TASK098','Seal role differs')
        require(seal['verification_status']=='PASS','Seal verification status differs')
        for path in list(files.values())+[packet,standalone,args.archive,args.members,args.seal]:
            readonly(path)
        for path in packet.rglob('*'):
            if path.is_dir():
                readonly(path)
        seal_digest=digest_file(args.seal)
    print(json.dumps({
        'status':'PASS','audit':'AUD064','input_files':19,
        'packet_files':len(files),'archive_members':len(seen),
        'archive_uncompressed_bytes':total_bytes,
        'checks':['nineteen input bytes','exact local output member set and bytes',
                  'standalone and packet report equality','safe regular archive names',
                  'no archive duplicates or links','exact archive membership and bytes',
                  'archive/local byte equality','exact read-only diagnostic replay']
                 +(['seal hashes/counts','read-only issuance modes'] if args.seal else []),
        'component_sha256':component_digests,
        'seal_sha256':seal_digest,
        'archive_extracted':False,
        'diagnostic_assertions':result['assertions'],
        'diagnostic_categories':len(result['categories']),
        'diagnostic_mutations':result['mutation_count'],
    },indent=2,sort_keys=True))


if __name__=='__main__':
    main()
