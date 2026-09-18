#!/usr/bin/env python3
"""Portable read-only verifier for this issued packet, Python standard library.

No extraction, installation, network access, repository access or file writes.
The diagnostic children also make no writes and use no nonstandard modules.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tarfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe(name):
    path=PurePosixPath(name)
    return (bool(name) and not path.is_absolute() and '\\' not in name
            and '\x00' not in name and all(p not in ('','.', '..') for p in name.split('/'))
            and str(path)==name)


def sha_manifest(path):
    result={}
    for line in path.read_text().splitlines():
        value,name=line.split('  ',1)
        assert re.fullmatch('[0-9a-f]{64}',value), ('invalid hash',name)
        assert safe(name) and name not in result, ('unsafe or duplicate path',name)
        result[name]=value
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive',type=Path)
    parser.add_argument('--seal',type=Path)
    parser.add_argument('--report',type=Path)
    parser.add_argument('--require-readonly',action='store_true')
    args=parser.parse_args()
    packet=Path(__file__).resolve().parent.parent
    inventory=json.loads((packet/'INVENTORY.json').read_text())
    payload={e['path']:e for e in inventory['payload_files']}
    assert len(payload)==len(inventory['payload_files'])
    assert set(inventory['control_files'])=={'INVENTORY.json','SHA256SUMS.txt'}
    actual_files=set()
    actual_dirs=set()
    for item in packet.rglob('*'):
        rel=item.relative_to(packet).as_posix()
        assert safe(rel),('unsafe disk path',rel)
        mode=item.lstat().st_mode
        assert not stat.S_ISLNK(mode),('symlink',rel)
        if stat.S_ISDIR(mode):
            actual_dirs.add(rel)
        else:
            assert stat.S_ISREG(mode),('nonregular file',rel)
            actual_files.add(rel)
        if args.require_readonly:
            assert mode & 0o222 == 0,('writable issued path',rel)
    if args.require_readonly:
        assert packet.stat().st_mode & 0o222 == 0
    assert actual_files==set(payload)|set(inventory['control_files']), 'inventory file-set mismatch'
    assert actual_dirs==set(inventory['directories']), 'inventory directory-set mismatch'
    for name,entry in payload.items():
        assert safe(name)
        data=(packet/name).read_bytes()
        assert len(data)==entry['bytes'] and digest(data)==entry['sha256'],('payload mismatch',name)
    hashes=sha_manifest(packet/'SHA256SUMS.txt')
    assert set(hashes)==actual_files-{'SHA256SUMS.txt'}, 'manifest coverage mismatch'
    for name,value in hashes.items():
        assert digest((packet/name).read_bytes())==value,('manifest mismatch',name)

    inputs={}
    for name in ('ROUND_028_FLUX_BLIND_INPUT_SHA256SUMS.txt',
                 'ROUND_028_FLUX_BLIND_ADDENDUM_SHA256SUMS.txt'):
        for rel,value in sha_manifest(packet/'ADMIN'/name).items():
            assert rel not in inputs,('duplicate admitted input',rel)
            assert digest((packet/'INPUTS'/rel).read_bytes())==value,('admitted input mismatch',rel)
            inputs[rel]=value
    assert len(inputs)==18
    declared=json.loads((packet/'ADMIN/INPUT_VERIFICATION.json').read_text())
    assert declared['verified_count']==18
    assert {r['path']:r['sha256'] for r in declared['records']}==inputs

    code_hashes=sha_manifest(packet/'ADMIN/EXECUTED_CODE_SHA256SUMS.txt')
    for name,value in code_hashes.items():
        assert digest((packet/name).read_bytes())==value,('executed code changed',name)
    runs=[]
    for record in sorted((packet/'LOGS').glob('run_*.json')):
        meta=json.loads(record.read_text())
        assert meta['matched_expected_exit']
        assert meta['exit_code']==meta['expected_exit_code']
        for kind in ('stdout','stderr'):
            assert safe(meta[kind])
            assert digest((packet/meta[kind]).read_bytes())==meta[kind+'_sha256']
        runs.append(meta)
    assert len(runs)==15,('unexpected logged execution count',len(runs))
    assert sum(r['exit_code']==0 for r in runs)==1
    assert sum(r['exit_code']==1 for r in runs)==14

    env=dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE']='1'
    command=[sys.executable,str(packet/'CODE/diagnostic.py')]
    result=subprocess.run(command,capture_output=True,text=True,env=env)
    assert result.returncode==0 and not result.stderr, ('diagnostic failure',result.stdout,result.stderr)
    reproduced=[{'argv':command,'exit_code':result.returncode,
                 'stdout_sha256':digest(result.stdout.encode()),
                 'stderr_sha256':digest(result.stderr.encode())}]
    fresh=json.loads(result.stdout)
    stored=json.loads((packet/'RESULTS/DIAGNOSTIC_RESULT.json').read_text())
    assert fresh==stored
    mutation_results=json.loads((packet/'RESULTS/MUTATION_SUMMARY.json').read_text())
    assert mutation_results['count']==14 and mutation_results['all_detected_nonzero']
    assert {m['mutation'] for m in mutation_results['runs']}==set(fresh['mutations_available'])
    for entry in mutation_results['runs']:
        result=subprocess.run(command+['--mutation',entry['mutation']],
                              capture_output=True,text=True,env=env)
        assert result.returncode==1 and not result.stderr,('mutation did not fail',entry['mutation'])
        assert json.loads(result.stdout)==entry['witness'],('changed mutation witness',entry['mutation'])
        reproduced.append({'argv':command+['--mutation',entry['mutation']],
                           'exit_code':result.returncode,
                           'stdout_sha256':digest(result.stdout.encode()),
                           'stderr_sha256':digest(result.stderr.encode())})

    archive_members=None
    if args.archive:
        expected={packet.name+'/'+rel for rel in actual_files}
        seen=set()
        with tarfile.open(args.archive,'r:gz') as archive:
            for member in archive:
                assert safe(member.name),('unsafe archive name',member.name)
                assert member.name not in seen,('duplicate archive name',member.name)
                assert member.isfile() and not member.issym() and not member.islnk(),('nonregular archive member',member.name)
                assert member.name in expected,('unexpected archive member',member.name)
                assert member.mode & 0o222 == 0,('writable archive member',member.name)
                rel=member.name[len(packet.name)+1:]
                stream=archive.extractfile(member)
                assert stream is not None
                archived=stream.read()
                assert archived==(packet/rel).read_bytes(),('archive bytes differ',member.name)
                seen.add(member.name)
        assert seen==expected, 'archive coverage mismatch'
        archive_members=len(seen)

    if args.report:
        assert args.report.read_bytes()==(packet/'REPORT.md').read_bytes(), 'assigned report differs from packet'
    if args.seal:
        seal=json.loads(args.seal.read_text())
        assert seal['packet_name']==packet.name
        assert seal['file_count']==len(actual_files)
        assert seal['directory_count']==len(actual_dirs)+1
        assert seal['input_count']==18
        assert seal['diagnostic_checks']==fresh['checks']
        assert seal['mutation_count']==14
        for rel,key in (('REPORT.md','report_sha256'),('INVENTORY.json','inventory_sha256'),
                        ('SHA256SUMS.txt','payload_manifest_sha256')):
            assert digest((packet/rel).read_bytes())==seal[key],('seal mismatch',key)
        if args.archive:
            data=args.archive.read_bytes()
            assert len(data)==seal['archive_bytes'] and digest(data)==seal['archive_sha256']

    print(json.dumps({'status':'PASS','read_only_verifier':True,
                      'input_count':len(inputs),'packet_file_count':len(actual_files),
                      'packet_directory_count':len(actual_dirs)+1,
                      'payload_manifest_entries':len(hashes),
                      'archive_regular_member_count':archive_members,
                      'diagnostic_checks':fresh['checks'],
                      'diagnostic_categories':fresh['category_count'],
                      'mutation_nonzero_exits_reproduced':14,
                      'reproduced_executions':reproduced,
                      'original_logged_runs':len(runs),
                      'report_sha256':digest((packet/'REPORT.md').read_bytes()),
                      'payload_manifest_sha256':digest((packet/'SHA256SUMS.txt').read_bytes())},
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
