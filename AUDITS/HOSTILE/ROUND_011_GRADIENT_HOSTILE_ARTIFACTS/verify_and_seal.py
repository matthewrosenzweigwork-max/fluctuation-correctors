#!/usr/bin/env python3
"""One-shot, explicit-member integrity seal for the isolated TASK069 review."""
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import subprocess
import tarfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REL = HERE.relative_to(ROOT).as_posix()
REPORT = 'AUDITS/HOSTILE/ROUND_011_RESCALED_GRADIENT_REVIEW.md'
ASSIGNED = 'AUDITS/ROUND_011_RESCALED_GRADIENT_HOSTILE_INPUT_SHA256SUMS.txt'
BASE = '29d7ce427ad7a98739b18d07781e71c4598b3579'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_new(path, data):
    with path.open('xb') as stream:
        stream.write(data)


def json_bytes(data):
    return (json.dumps(data, indent=2)+'\n').encode()


def safe_relative(name):
    path = PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts and name == path.as_posix(), name
    assert name and not name.startswith('./'), name


def input_check():
    assigned_bytes = (ROOT/ASSIGNED).read_bytes()
    assert (HERE/'INPUT_SHA256SUMS.txt').read_bytes() == assigned_bytes
    rows = []
    for line in assigned_bytes.decode().splitlines():
        expected, relative = line.split('  ', 1)
        safe_relative(relative)
        path = ROOT/relative
        assert path.is_file() and not path.is_symlink(), relative
        actual = digest(path.read_bytes())
        assert actual == expected, (relative, expected, actual)
        rows.append({'path': relative, 'sha256': actual, 'verified': True})
    assert len(rows) == 22 and len({row['path'] for row in rows}) == 22
    first_verification = json.loads((HERE/'INPUT_VERIFICATION.json').read_text())
    assert first_verification['base_commit'] == BASE
    assert first_verification['manifest_sha256'] == digest(assigned_bytes)
    assert first_verification['input_count'] == 22
    assert all(row['match'] for row in first_verification['files'])
    return rows


def main():
    # These names must not exist before issuance. Re-running would require a
    # separately named superseding report, rather than rewriting the seal.
    final_names = ['REVIEW_CHECKS.json','OUTPUT_SHA256SUMS.txt',
                   'OUTPUT_VERIFICATION.json','ARCHIVE_SEAL.json',
                   'ARCHIVE_SHA256SUMS.txt','SEAL_SHA256SUMS.txt']
    assert all(not (HERE/name).exists() for name in final_names), 'already sealed or partially sealed'
    inputs = input_check()
    head = subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    branch = subprocess.check_output(['git','rev-parse','--abbrev-ref','HEAD'],cwd=ROOT,text=True).strip()
    assert head == BASE
    assert branch == 'codex/hocf-r011-gradient-hostile'
    result = json.loads((HERE/'rescaled_gradient_hostile_exact_results.json').read_text())
    assert result['status'] == 'PASS' and result['total_checks'] == 6927
    assert sum(result['counts'].values()) == result['total_checks']
    assert result['floating_point_tolerance'] is None and result['random_seed'] is None
    for name in ('check_rescaled_gradient_hostile.py','verify_and_seal.py'):
        compile((HERE/name).read_text(), name, 'exec')
    initial_payload = [REPORT] + [REL+'/'+name for name in
        ('README.md','INPUT_SHA256SUMS.txt','INPUT_VERIFICATION.json',
         'check_rescaled_gradient_hostile.py','rescaled_gradient_hostile_exact_results.json',
         'verify_and_seal.py')]
    text_checks = []
    for relative in initial_payload:
        data = (ROOT/relative).read_bytes()
        assert data.endswith(b'\n'), relative
        content = data.decode('utf-8')
        assert not any(line.rstrip() != line for line in content.splitlines()), relative
        assert not any(ord(char) < 32 and char not in '\n\t' for char in content), relative
        text_checks.append({'path':relative, 'terminal_newline':True,
                            'no_trailing_whitespace':True, 'no_control_bytes':True})
    report = (ROOT/REPORT).read_text()
    assert report.count('\\[') == report.count('\\]')
    assert report.count('\\(') == report.count('\\)')
    assert not any(line.endswith('\\') and not line.endswith('\\\\')
                   for line in report.splitlines())
    diff = subprocess.run(['git','diff','--check','--',REPORT,REL],
                          cwd=ROOT,text=True,capture_output=True)
    assert diff.returncode == 0, (diff.stdout, diff.stderr)
    now = datetime.now(timezone.utc)
    stamp = now.strftime('%Y%m%d_%H%M%S_UTC')
    checks = {'status':'PASS','time_utc':now.isoformat(),'base_commit':head,
              'branch':branch,'worktree':str(ROOT),'verified_inputs':inputs,
              'input_count':len(inputs),'exact_diagnostic_status':result['status'],
              'exact_diagnostic_count':result['total_checks'],
              'python_syntax':'both new scripts compiled in memory; no bytecode generated',
              'text_checks':text_checks,
              'markdown_display_pairs':report.count('\\['),
              'markdown_inline_math_pairs':report.count('\\('),
              'dangling_single_backslash_lines':0,
              'git_diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr},
              'commands':[
                  'python3 '+REL+'/check_rescaled_gradient_hostile.py',
                  'python3 '+REL+'/verify_and_seal.py',
                  'git rev-parse HEAD','git rev-parse --abbrev-ref HEAD',
                  'git diff --check -- '+REPORT+' '+REL],
              'scope':'Only explicitly listed input and output files inspected; no canonical state/history read.'}
    write_new(HERE/'REVIEW_CHECKS.json',json_bytes(checks))
    payload = initial_payload + [REL+'/REVIEW_CHECKS.json']
    output_rows = [{'path':relative,'sha256':digest((ROOT/relative).read_bytes())}
                   for relative in sorted(payload)]
    output_manifest = ''.join(row['sha256']+'  '+row['path']+'\n' for row in output_rows).encode()
    write_new(HERE/'OUTPUT_SHA256SUMS.txt',output_manifest)
    for row in output_rows:
        assert digest((ROOT/row['path']).read_bytes()) == row['sha256']
    output_verification = {'status':'PASS','payload_count':len(output_rows),
                           'output_manifest_sha256':digest(output_manifest),
                           'files':output_rows,
                           'manifest_exclusions':['itself','OUTPUT_VERIFICATION.json',
                              'archive and detached archive seal records']}
    write_new(HERE/'OUTPUT_VERIFICATION.json',json_bytes(output_verification))
    members = [row['path'] for row in inputs] + [ASSIGNED] + payload + [
               REL+'/OUTPUT_SHA256SUMS.txt',REL+'/OUTPUT_VERIFICATION.json']
    assert len(members) == len(set(members))
    for relative in members:
        safe_relative(relative)
        assert (ROOT/relative).is_file() and not (ROOT/relative).is_symlink()
    archive_name = 'ROUND_011_RESCALED_GRADIENT_HOSTILE_'+stamp+'.tar.gz'
    archive_path = HERE/archive_name
    with tarfile.open(archive_path,'x:gz',format=tarfile.PAX_FORMAT) as archive:
        for relative in sorted(members):
            data = (ROOT/relative).read_bytes()
            info = tarfile.TarInfo(relative)
            info.size = len(data)
            info.mtime = 0
            info.mode = 0o444
            info.uid = info.gid = 0
            info.uname = info.gname = ''
            archive.addfile(info,io.BytesIO(data))
    recovered = []
    with tarfile.open(archive_path,'r:gz') as archive:
        actual = archive.getmembers()
        assert len(actual) == len(members)
        assert {entry.name for entry in actual} == set(members)
        for entry in actual:
            safe_relative(entry.name)
            assert entry.isfile() and not entry.issym() and not entry.islnk()
            extracted = archive.extractfile(entry)
            assert extracted is not None
            data = extracted.read()
            expected = digest((ROOT/entry.name).read_bytes())
            assert digest(data) == expected
            recovered.append({'path':entry.name,'sha256':expected,'bytes':len(data)})
    archive_digest = digest(archive_path.read_bytes())
    seal = {'status':'SEALED_AND_VERIFIED','time_utc':now.isoformat(),
            'archive_name':archive_name,'archive_path':str(archive_path),
            'archive_sha256':archive_digest,'archive_bytes':archive_path.stat().st_size,
            'member_count':len(recovered),'members':recovered,
            'allowed_input_count':22,'input_manifest_sha256':digest((ROOT/ASSIGNED).read_bytes()),
            'output_manifest_sha256':digest(output_manifest),
            'archive_verification':'all unique safe regular members re-read in memory and hash-matched',
            'mathematical_verdict':'CONDITIONAL PASS of frozen THM032; no repair implemented',
            'source_condition':'Earlier full-source prerequisites remain conditional as issued.',
            'exposure_record':REL+'/README.md',
            'no_canonical_edits':True,'no_commits':True,'no_pushes':True,'no_installations':True,
            'immutability':'Issued outputs set read-only; corrections require a separately named superseding report.'}
    write_new(HERE/'ARCHIVE_SEAL.json',json_bytes(seal))
    write_new(HERE/'ARCHIVE_SHA256SUMS.txt',(archive_digest+'  '+archive_name+'\n').encode())
    detached_names = ['ARCHIVE_SEAL.json','ARCHIVE_SHA256SUMS.txt',
                      'OUTPUT_SHA256SUMS.txt','OUTPUT_VERIFICATION.json','REVIEW_CHECKS.json']
    detached = ''.join(digest((HERE/name).read_bytes())+'  '+name+'\n' for name in detached_names)
    write_new(HERE/'SEAL_SHA256SUMS.txt',detached.encode())
    for relative in payload + [REL+'/'+name for name in final_names[1:]]:
        (ROOT/relative).chmod(0o444)
    archive_path.chmod(0o444)
    assert digest(archive_path.read_bytes()) == archive_digest
    print(json.dumps({'status':'SEALED_AND_VERIFIED','inputs':22,
                      'payload_outputs':len(output_rows),'archive_members':len(recovered),
                      'exact_checks':6927,'archive':str(archive_path),
                      'archive_sha256':archive_digest},indent=2))


if __name__ == '__main__':
    main()
