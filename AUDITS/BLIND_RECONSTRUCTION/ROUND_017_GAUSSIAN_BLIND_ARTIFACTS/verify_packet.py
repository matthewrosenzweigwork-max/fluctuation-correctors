#!/usr/bin/env python3
"""Read-only verifier for AUD053 input/output seals and optional safe archive."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, tarfile

def digest(data): return hashlib.sha256(data).hexdigest()
def manifest(path):
    rows={}
    for line in path.read_text().splitlines():
        if not line: continue
        sha,rel=line.split('  ',1)
        p=PurePosixPath(rel)
        assert len(sha)==64 and all(c in '0123456789abcdef' for c in sha)
        assert not p.is_absolute() and '..' not in p.parts and rel not in rows
        rows[rel]=sha
    return rows

def verify(base,archive=None,expected_sha256=None,worktree=None):
    inputs=manifest(base/'INPUT_SHA256SUMS.txt');assert len(inputs)==11
    for rel,sha in inputs.items():
        p=base/'INPUTS'/rel
        assert p.is_file() and not p.is_symlink() and digest(p.read_bytes())==sha
        if worktree:
            q=worktree/rel
            assert q.is_file() and not q.is_symlink() and digest(q.read_bytes())==sha
    outputs=manifest(base/'OUTPUT_SHA256SUMS.txt')
    actual={str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}
    assert actual==set(outputs)|{'OUTPUT_SHA256SUMS.txt'}
    for p in base.rglob('*'): assert not p.is_symlink()
    for rel,sha in outputs.items():
        p=base/rel
        assert p.is_file() and digest(p.read_bytes())==sha
    result={'status':'PASS','inputs':len(inputs),'manifest_payload_files':len(outputs),'packet_files':len(actual),'worktree_input_comparison':bool(worktree),'packet_files_read_only':all(not ((base/rel).stat().st_mode & 0o222) for rel in actual)}
    if archive:
        archive_sha=digest(archive.read_bytes())
        if expected_sha256: assert archive_sha==expected_sha256
        seen=set()
        with tarfile.open(archive,'r:gz') as tf:
            for member in tf.getmembers():
                p=PurePosixPath(member.name)
                assert not p.is_absolute() and '..' not in p.parts
                assert len(p.parts)>=2 and p.parts[0]==base.name
                assert member.isfile() and not member.issym() and not member.islnk()
                rel=str(PurePosixPath(*p.parts[1:]))
                assert rel in actual and rel not in seen
                seen.add(rel)
                assert member.size==(base/rel).stat().st_size
                data=tf.extractfile(member).read()
                assert member.size==len(data) and data==(base/rel).read_bytes()
        assert seen==actual
        result.update({'archive':str(archive),'archive_sha256':archive_sha,'archive_regular_files':len(seen),'archive_safe_members':True,'archive_disk_payload_identical':True})
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--packet',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--archive',type=Path)
    p.add_argument('--expected-sha256')
    p.add_argument('--worktree',type=Path)
    args=p.parse_args()
    print(json.dumps(verify(args.packet,args.archive,args.expected_sha256,args.worktree),indent=2))
