#!/usr/bin/env python3
"""Read-only exact-byte verifier; archive members are never extracted."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe(name):
    p=PurePosixPath(name)
    assert name and not p.is_absolute() and str(p)==name
    assert all(c not in ('.','..','') for c in p.parts)
    assert '\\' not in name and ':' not in name
    assert not any(ord(c)<32 or ord(c)==127 for c in name)


def rows(data):
    result={}
    for line in data.decode().splitlines():
        digest,name=line.split('  ',1)
        safe(name)
        assert len(digest)==64 and all(c in '0123456789abcdef' for c in digest)
        assert name not in result
        result[name]=digest
    return result


def main():
    a=Path(__file__).resolve().parent
    seal=json.loads((a/'OUTER_SEAL.json').read_text())
    manifest=(a/'OUTPUT_SHA256SUMS.txt').read_bytes()
    assert sha(manifest)==seal['output_manifest_sha256']
    expected=rows(manifest)
    excluded={'OUTPUT_SHA256SUMS.txt','OUTER_SEAL.json',seal['archive_name']}
    actual={p.relative_to(a).as_posix() for p in a.rglob('*') if p.is_file()}
    assert actual==set(expected)|excluded
    for name,digest in expected.items():
        p=a/name
        assert not p.is_symlink() and stat.S_ISREG(p.stat().st_mode)
        assert sha(p.read_bytes())==digest,name
    inputs=rows((a/'INPUT_SHA256SUMS.txt').read_bytes())
    assert len(inputs)==16
    for name,digest in inputs.items():
        assert sha((a/'INPUTS'/name).read_bytes())==digest
    proof='ROUND_022_DISTRIBUTION_PATH_GAUSSIAN.md'
    assert (a/proof).read_bytes()==(a.parent/proof).read_bytes()
    result=json.loads((a/'EXACT_RESULTS.json').read_text())
    assert result['status']=='PASS' and result['assertions']==47437
    assert result['script_sha256']==sha((a/'round022_hilbert_checks.py').read_bytes())
    archive=a/seal['archive_name']
    assert sha(archive.read_bytes())==seal['archive_sha256']
    members=set(expected)|{'OUTPUT_SHA256SUMS.txt'}
    with zipfile.ZipFile(archive) as z:
        infos=z.infolist()
        assert len(infos)==len(members)==seal['archive_members']
        assert {i.filename for i in infos}==members
        assert sum(i.file_size for i in infos)<20000000
        for info in infos:
            safe(info.filename)
            assert info.orig_filename==info.filename
            assert not info.is_dir() and not info.flag_bits&1
            assert stat.S_ISREG(info.external_attr>>16)
            assert z.read(info)==(a/info.filename).read_bytes()
    rejected=0
    for name in ['../escape','/absolute','a/../b','a//b','a/./b','C:/x','a\\b','a\x00b','']:
        try: safe(name)
        except AssertionError: rejected+=1
        else: raise AssertionError('unsafe-name control survived')
    print(json.dumps({'status':'PASS','inputs':len(inputs),'output_hashes':len(expected),
                      'archive_members':len(members),'unsafe_controls_rejected':rejected,
                      'archive_sha256':seal['archive_sha256'],'proof_sha256':sha((a/proof).read_bytes())},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
