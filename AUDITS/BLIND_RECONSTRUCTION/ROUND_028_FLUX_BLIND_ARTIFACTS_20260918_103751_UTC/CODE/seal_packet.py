#!/usr/bin/env python3
"""One-time deterministic safe-archive issuance; only this lane's outputs."""
from pathlib import Path
import ast
import datetime
import gzip
import hashlib
import io
import json
import os
import re
import stat
import subprocess
import sys
import tarfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path,value):
    path.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    packet=Path(__file__).resolve().parent.parent
    worktree=packet.parent.parent.parent
    report=packet.parent/'ROUND_028_FLUX_RECONSTRUCTION.md'
    archive=packet.with_name(packet.name+'.tar.gz')
    sealpath=packet.with_name(packet.name+'.SEAL.json')
    receiptpath=packet.with_name(packet.name+'.RECEIPT.json')
    checksumspath=packet.with_name(packet.name+'.SHA256SUMS.txt')
    failurepath=packet.with_name(packet.name+'.ISSUANCE_FAILURE.json')
    for name in (archive,sealpath,receiptpath,checksumspath,failurepath):
        assert not name.exists(),('never overwrite an issuance',str(name))
    assert not (packet/'INVENTORY.json').exists()
    assert report.is_file() and not report.is_symlink()
    started=now()
    execution={'started_utc':started,'argv':sys.argv,'executable':sys.executable,
               'cwd':str(Path.cwd()),'packet':str(packet),
               'script_sha256':sha(Path(__file__).read_bytes()),
               'outcome_record':'sibling .RECEIPT.json or .ISSUANCE_FAILURE.json'}
    write_json(packet/'ADMIN/ISSUANCE_EXECUTION.json',execution)

    verified=[]
    for manifest in ('ROUND_028_FLUX_BLIND_INPUT_SHA256SUMS.txt',
                     'ROUND_028_FLUX_BLIND_ADDENDUM_SHA256SUMS.txt'):
        original_manifest=worktree/'AUDITS'/manifest
        assert original_manifest.read_bytes()==(packet/'ADMIN'/manifest).read_bytes()
        for line in original_manifest.read_text().splitlines():
            expected,rel=line.split('  ',1)
            original=(worktree/rel).read_bytes()
            copied=(packet/'INPUTS'/rel).read_bytes()
            assert original==copied and sha(original)==expected,rel
            verified.append({'path':rel,'sha256':expected,'bytes':len(original),
                             'original_matches_frozen':True,'copy_matches_original':True})
    assert len(verified)==18 and len({r['path'] for r in verified})==18
    write_json(packet/'ADMIN/FINAL_INPUT_VERIFICATION.json',
               {'time_utc':now(),'count':18,'records':verified})
    final_report=report.read_bytes()
    (packet/'REPORT.md').write_bytes(final_report)
    text=final_report.decode()
    tags=[int(x) for x in re.findall(r'\\tag\{([0-9]+)\}',text)]
    assert tags==list(range(1,37)),tags
    assert text.count('ISOLATED_RECONSTRUCTION_PASS, whole unchanged claim.')==2
    scripts=[]
    for script in sorted((packet/'CODE').glob('*.py')):
        data=script.read_bytes()
        ast.parse(data,filename=script.name)
        scripts.append({'path':script.relative_to(packet).as_posix(),'sha256':sha(data)})
    write_json(packet/'RESULTS/STATIC_CHECK.json',
               {'status':'PASS','scope':'Administrative syntax, equation labels and coverage markers only; no mathematical claim.',
                'report_lines':len(text.splitlines()),'report_bytes':len(final_report),
                'report_sha256':sha(final_report),'equation_tags':tags,
                'whole_verdict_count':2,'python_ast_parses':scripts})

    payload=[]
    directories=[]
    for path in sorted(packet.rglob('*')):
        rel=path.relative_to(packet).as_posix()
        assert not path.is_symlink(),rel
        if path.is_dir():
            directories.append(rel)
        else:
            assert stat.S_ISREG(path.stat().st_mode),rel
            data=path.read_bytes()
            payload.append({'path':rel,'bytes':len(data),'sha256':sha(data)})
    inventory={'schema':'AUD077-complete-inventory-v1','payload_files':payload,
               'directories':directories,
               'control_files':{'INVENTORY.json':'Self-listed; digest bound by SHA256SUMS and outer seal.',
                                'SHA256SUMS.txt':'Self-excluded hash list; digest bound by outer seal.'}}
    write_json(packet/'INVENTORY.json',inventory)
    hashes={r['path']:r['sha256'] for r in payload}
    hashes['INVENTORY.json']=sha((packet/'INVENTORY.json').read_bytes())
    (packet/'SHA256SUMS.txt').write_text(''.join(hashes[name]+'  '+name+'\n' for name in sorted(hashes)))
    files=sorted(path for path in packet.rglob('*') if path.is_file())
    assert len(files)==len(payload)+2
    with archive.open('xb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as compressed:
            with tarfile.open(fileobj=compressed,mode='w',format=tarfile.USTAR_FORMAT) as tar:
                for path in files:
                    rel=path.relative_to(packet).as_posix()
                    data=path.read_bytes()
                    info=tarfile.TarInfo(packet.name+'/'+rel)
                    info.size=len(data)
                    info.mode=0o444
                    info.mtime=0
                    info.uid=info.gid=0
                    info.uname=info.gname=''
                    info.type=tarfile.REGTYPE
                    tar.addfile(info,io.BytesIO(data))
    for path in files:
        path.chmod(0o444)
    for path in sorted((p for p in packet.rglob('*') if p.is_dir()),
                       key=lambda p:len(p.parts),reverse=True):
        path.chmod(0o555)
    packet.chmod(0o555)
    report.chmod(0o444)
    archive.chmod(0o444)
    diagnostic=json.loads((packet/'RESULTS/DIAGNOSTIC_RESULT.json').read_text())
    seal={'schema':'AUD077-outer-seal-v1','issued_utc':now(),'packet_name':packet.name,
          'file_count':len(files),'directory_count':len(directories)+1,
          'payload_manifest_entries':len(hashes),'input_count':18,
          'diagnostic_checks':diagnostic['checks'],'diagnostic_categories':diagnostic['category_count'],
          'mutation_count':14,'archive_name':archive.name,
          'archive_bytes':archive.stat().st_size,'archive_sha256':sha(archive.read_bytes()),
          'report_name':report.name,'report_sha256':sha(final_report),
          'inventory_sha256':sha((packet/'INVENTORY.json').read_bytes()),
          'payload_manifest_sha256':sha((packet/'SHA256SUMS.txt').read_bytes()),
          'verdicts':{'THM053(A)-(B)':'ISOLATED_RECONSTRUCTION_PASS',
                      'THM055(A)-(E)':'ISOLATED_RECONSTRUCTION_PASS'},
          'scope':'Complete unchanged joint conjunction; no critical-profile limit decided.',
          'historical_source_gate_authentication':'Separate root responsibility.'}
    write_json(sealpath,seal)
    sealpath.chmod(0o444)
    command=[sys.executable,str(packet/'CODE/verify.py'),'--archive',str(archive),
             '--seal',str(sealpath),'--report',str(report),'--require-readonly']
    env=dict(os.environ)
    env['PYTHONDONTWRITEBYTECODE']='1'
    checked=subprocess.run(command,capture_output=True,text=True,env=env)
    receipt={'schema':'AUD077-issuance-receipt-v1','started_utc':started,'finished_utc':now(),
             'issuance_execution':execution,'verifier_argv':command,'verifier_exit_code':checked.returncode,
             'verifier_stdout':checked.stdout,'verifier_stderr':checked.stderr,
             'verifier_stdout_sha256':sha(checked.stdout.encode()),
             'verifier_stderr_sha256':sha(checked.stderr.encode()),
             'all_original_diagnostic_runs':15,'original_expected_nonzero_mutations':14,
             'canonical_edits':0,'input_edits':0,'commits':0,'pushes':0,'children':0,
             'created_paths':{'report':str(report),'packet':str(packet),'archive':str(archive),
                              'seal':str(sealpath),'receipt':str(receiptpath),
                              'outer_checksums':str(checksumspath)},
             'seal_sha256':sha(sealpath.read_bytes())}
    if checked.returncode!=0:
        write_json(failurepath,receipt)
        failurepath.chmod(0o444)
        print(json.dumps({'status':'ISSUANCE_FAILURE','receipt':str(failurepath),
                          'stdout':checked.stdout,'stderr':checked.stderr},indent=2))
        return 1
    receipt['status']='PASS'
    receipt['verification']=json.loads(checked.stdout)
    write_json(receiptpath,receipt)
    receiptpath.chmod(0o444)
    external_members=[report,archive,sealpath,receiptpath,
                      packet/'INVENTORY.json',packet/'SHA256SUMS.txt',packet/'CODE/verify.py']
    outer={p.relative_to(packet.parent).as_posix():sha(p.read_bytes()) for p in external_members}
    checksumspath.write_text(''.join(outer[name]+'  '+name+'\n' for name in sorted(outer)))
    checksumspath.chmod(0o444)
    for line in checksumspath.read_text().splitlines():
        expected,rel=line.split('  ',1)
        assert sha((packet.parent/rel).read_bytes())==expected,('outer checksum mismatch',rel)
    print(json.dumps({'status':'ISSUED_AND_VERIFIED','paths':receipt['created_paths'],
                      'counts':{'inputs':18,'packet_files':len(files),'packet_directories':len(directories)+1,
                                'safe_archive_regular_members':len(files),'checks':diagnostic['checks'],
                                'categories':diagnostic['category_count'],'mutations':14,
                                'original_runs':15,'read_only_reexecutions':15},
                      'sha256':{'report':sha(final_report),'archive':seal['archive_sha256'],
                                'seal':sha(sealpath.read_bytes()),'receipt':sha(receiptpath.read_bytes()),
                                'inventory':seal['inventory_sha256'],
                                'payload_manifest':seal['payload_manifest_sha256'],
                                'outer_checksums':sha(checksumspath.read_bytes())}},indent=2,sort_keys=True))
    return 0


if __name__=='__main__':
    sys.exit(main())
