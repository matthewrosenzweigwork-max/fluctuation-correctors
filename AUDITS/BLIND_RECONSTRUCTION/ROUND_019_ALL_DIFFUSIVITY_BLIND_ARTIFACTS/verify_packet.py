#!/usr/bin/env python3
"""Read-only safe byte verification of the sealed AUD057 reconstruction."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import tarfile

art=Path(__file__).resolve().parent
root=art.parents[2]
def sha(data):
    return hashlib.sha256(data).hexdigest()
def safe(name):
    p=PurePosixPath(name)
    return not p.is_absolute() and '..' not in p.parts and '\\' not in name and str(p)==name

def manifest(path):
    rows=[]
    for line in path.read_text().splitlines():
        digest,name=line.split(maxsplit=1)
        assert len(digest)==64 and all(c in '0123456789abcdef' for c in digest)
        assert safe(name),name
        rows.append((digest,name))
    assert len({n for _,n in rows})==len(rows)
    return rows

inputs=manifest(art/'INPUT_SHA256SUMS.txt')
assert len(inputs)==11
for digest,name in inputs:
    assert sha((root/name).read_bytes())==digest,('working input',name)
    assert sha((art/'inputs'/name).read_bytes())==digest,('packet input',name)
outputs=manifest(art/'OUTPUT_SHA256SUMS.txt')
for digest,name in outputs:
    assert sha((root/name).read_bytes())==digest,('output',name)
archives=manifest(art/'ARCHIVE_SHA256SUMS.txt')
assert len(archives)==1
archive_digest,archive_name=archives[0]
archive=art/archive_name
assert sha(archive.read_bytes())==archive_digest,'archive digest'
expected=(art/'ARCHIVE_MEMBERS.txt').read_text().splitlines()
assert len(expected)==len(set(expected)) and all(safe(name) for name in expected)
with tarfile.open(archive,'r:gz') as packet:
    members=packet.getmembers()
    assert [x.name for x in members]==expected,'archive member list'
    for item in members:
        assert safe(item.name) and item.isfile() and not item.issym() and not item.islnk(),item.name
        data=packet.extractfile(item).read()
        local=root/item.name
        assert local.is_file() and not local.is_symlink(),item.name
        assert data==local.read_bytes(),('archive bytes',item.name)
result={'status':'PASS','input_files':len(inputs),'output_files':len(outputs),
        'archive_members':len(expected),'archive_sha256':archive_digest,
        'safe_regular_files_only':True,'all_archive_bytes_match':True,
        'report_sha256':sha((root/'AUDITS/BLIND_RECONSTRUCTION/ROUND_019_ALL_DIFFUSIVITY_RECONSTRUCTION.md').read_bytes())}
print(json.dumps(result,indent=2))
