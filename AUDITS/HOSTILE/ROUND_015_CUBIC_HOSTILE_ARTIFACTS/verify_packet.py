#!/usr/bin/env python3
"""Read-only integrity verification of the issued AUD050 packet."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import tarfile

artifact=Path(__file__).resolve().parent
work=artifact.parents[2]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def rows(path):
    result=[]
    for line in path.read_text().splitlines():
        wanted,name=line.split('  ',1)
        p=PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts
        assert len(wanted)==64 and all(c in '0123456789abcdef' for c in wanted)
        result.append((wanted,name))
    assert len({name for _,name in result})==len(result)
    return result

inputs=rows(artifact/'INPUT_SHA256SUMS.txt')
assert len(inputs)==30
for wanted,name in inputs:
    assert digest((artifact/'PERMITTED_INPUTS'/name).read_bytes())==wanted, name
outpath=artifact/'OUTPUT_SHA256SUMS.txt'
outputs=rows(outpath)
for wanted,name in outputs:
    assert digest((work/name).read_bytes())==wanted, name
seal=json.loads((artifact/'ARCHIVE_SEAL.json').read_text())
archive=artifact/seal['archive_basename']
assert digest(archive.read_bytes())==seal['archive_sha256']
assert digest(outpath.read_bytes())==seal['output_manifest_sha256']
assert len(inputs)==seal['permitted_input_count']
expected=sorted([name for _,name in outputs]+[outpath.relative_to(work).as_posix()])
with tarfile.open(archive,'r:gz') as tf:
    members=tf.getmembers()
    assert len(members)==len(expected)==seal['archive_member_count']
    assert len({m.name for m in members})==len(members)
    assert sorted(m.name for m in members)==expected
    for member in members:
        assert member.isfile() and not member.issym() and not member.islnk()
        assert tf.extractfile(member).read()==(work/member.name).read_bytes(), member.name
print(json.dumps({'status':'PASS','permitted_input_count':len(inputs),'output_manifest_file_count':len(outputs),'archive_member_count':len(expected),'archive_sha256':seal['archive_sha256']},indent=2))
