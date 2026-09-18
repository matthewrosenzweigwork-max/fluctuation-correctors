#!/usr/bin/env python3
"""Portable read-only AUD067 verifier. No extraction, writes, chmod or caches."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    p=PurePosixPath(name)
    assert name and '\\' not in name and not p.is_absolute(), ('unsafe path',name)
    assert p.as_posix()==name and all(x not in ('','.','..') for x in p.parts), ('noncanonical path',name)
    return p


def regular_readonly(path):
    mode=path.lstat().st_mode
    assert stat.S_ISREG(mode) and not path.is_symlink(), ('not regular',str(path))
    assert mode & 0o222 == 0, ('writable member',str(path))


def located(root,name):
    pp=safe_name(name)
    p=root
    for part in pp.parts:
        p=p/part
        assert not p.is_symlink(), ('symlink component',str(p))
    return p


def manifest(path):
    rows={}
    for line in path.read_text(encoding='utf-8').splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        assert match, ('bad manifest row',line)
        sha,name=match.groups()
        safe_name(name)
        assert name not in rows, ('duplicate manifest member',name)
        rows[name]=sha
    assert rows, ('empty manifest',str(path))
    return rows


def verify():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    args=parser.parse_args()
    root=args.root.resolve()
    own=Path(__file__).resolve().parent
    layout=json.loads((own/'PACKET_LAYOUT.json').read_text())
    art=located(root,layout['artifact_directory'])
    assert art.resolve()==own, 'verifier must run from its own relocated packet'
    report=layout['report']
    input_rows=manifest(art/'INPUT_SHA256SUMS.txt')
    assert len(input_rows)==21
    inventory=json.loads((art/'INPUT_INVENTORY.json').read_text())
    assert len(inventory)==21 and {v['path']:v['sha256'] for v in inventory}==input_rows
    for row in inventory:
        p=located(art/'dossier',row['path'])
        regular_readonly(p)
        data=p.read_bytes()
        assert len(data)==row['bytes'] and digest(data)==row['sha256'], ('input mismatch',row['path'])
    output_rows=manifest(art/'OUTPUT_SHA256SUMS.txt')
    output_manifest_name=layout['artifact_directory']+'/OUTPUT_SHA256SUMS.txt'
    expected_members=dict(output_rows)
    expected_members[output_manifest_name]=digest((art/'OUTPUT_SHA256SUMS.txt').read_bytes())
    members_path=located(root,layout['membership'])
    regular_readonly(members_path)
    archive_rows=manifest(members_path)
    assert archive_rows==expected_members, 'membership/output manifest disagreement'
    actual={report}
    for p in art.rglob('*'):
        assert not p.is_symlink(), ('symlink in owned packet',str(p))
        if p.is_dir(): continue
        regular_readonly(p)
        actual.add(p.relative_to(root).as_posix())
    assert actual==set(archive_rows), ('scoped file-set mismatch',sorted(actual^set(archive_rows)))
    for name,sha in archive_rows.items():
        p=located(root,name)
        regular_readonly(p)
        assert digest(p.read_bytes())==sha, ('output mismatch',name)
    archive=located(root,layout['archive'])
    regular_readonly(archive)
    with zipfile.ZipFile(archive) as z:
        infos=z.infolist()
        assert len(infos)==len({i.filename for i in infos})==len(archive_rows), 'duplicate/count archive member'
        assert {i.filename for i in infos}==set(archive_rows), 'archive membership differs'
        for info in infos:
            safe_name(info.filename)
            mode=info.external_attr>>16
            assert info.create_system==3 and stat.S_ISREG(mode), ('nonregular archived member',info.filename)
            assert not info.is_dir() and mode & 0o222 == 0, ('unsafe archived member mode',info.filename)
            assert info.flag_bits & 1 == 0, 'encrypted member'
            p=located(root,info.filename)
            assert info.file_size==p.stat().st_size, ('archive size mismatch',info.filename)
            assert digest(z.read(info))==archive_rows[info.filename], ('archive digest mismatch',info.filename)
        assert z.testzip() is None, 'CRC failure'
    run=subprocess.run([sys.executable,'-B',str(art/'exact_checks.py')],cwd=str(art),capture_output=True,text=True,check=False)
    assert run.returncode==0 and not run.stderr, ('checker failed',run.returncode,run.stderr)
    actual_result=json.loads(run.stdout)
    expected_result=json.loads((art/'RESULTS.json').read_text())
    assert actual_result==expected_result, 'checker result differs from issued JSON'
    assert actual_result['status']=='PASS' and actual_result['assertions']==593
    assert len(actual_result['categories'])==19 and len(actual_result['mutation_witnesses'])==11
    return {'status':'PASS','input_count':21,'output_digest_rows':len(output_rows),'archive_member_count':len(archive_rows),'archive_sha256':digest(archive.read_bytes()),'report_sha256':digest(located(root,report).read_bytes()),'diagnostic_assertions':593,'diagnostic_categories':19,'nonzero_mutation_witnesses':11,'read_only_verifier':True,'archive_safety':'unique canonical names; regular read-only Unix files; exact byte digests; no extraction; CRC passed','source_scope':'entire THM047 reconstruction relative to explicitly supplied prior modules; current constructor withheld; THM046 remains open'}


if __name__=='__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
