#!/usr/bin/env python3
"""Portable read-only AUD080 packet verifier. Does not extract or modify files."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import tarfile

def sha(data): return hashlib.sha256(data).hexdigest()
def safe(name):
    p=PurePosixPath(name)
    return bool(name) and not p.is_absolute() and "\\" not in name and all(x not in ("", ".", "..") for x in name.split("/"))
def regular(path):
    assert not path.is_symlink() and stat.S_ISREG(path.lstat().st_mode),str(path)
def data(path):
    regular(path)
    return path.read_bytes()
def scan(root):
    result={}
    for x in root.rglob("*"):
        assert not x.is_symlink(),"symlink: "+str(x)
        mode=x.lstat().st_mode
        assert stat.S_ISDIR(mode) or stat.S_ISREG(mode),"special member: "+str(x)
        if stat.S_ISREG(mode):
            name=x.relative_to(root).as_posix()
            assert safe(name),name
            result[name]=x
    return result

ap=argparse.ArgumentParser()
ap.add_argument("--packet",default=str(Path(__file__).resolve().parent))
ap.add_argument("--archive")
ap.add_argument("--seal")
ap.add_argument("--report")
args=ap.parse_args()
root=Path(args.packet)
assert not root.is_symlink(),"packet root is symlink"
files=scan(root)
manifest=json.loads(data(root/"SHA256SUMS.json"))
assert manifest["schema"]=="AUD080-SHA256-1"
expected=manifest["files"]
assert all(safe(n) for n in expected)
assert set(files)==set(expected)|{"SHA256SUMS.json"},"inexact packet member set"
for name,rec in expected.items():
    b=data(files[name])
    assert len(b)==rec["size"] and sha(b)==rec["sha256"],name
inventory=data(root/"MEMBER_INVENTORY.txt").decode().splitlines()
assert inventory==sorted(files),"inexact or duplicate member inventory"
assert manifest["packet_name"]==root.name
allowed={}
for line in data(root/"INPUT_MANIFEST.txt").decode().splitlines():
    digest,name=line.split("  ",1)
    assert safe(name) and name not in allowed
    assert sha(data(root/"INPUTS"/name))==digest,name
    allowed[name]=digest
assert len(allowed)==20
iv=json.loads(data(root/"INPUT_VERIFICATION.json"))
assert iv["status"]=="PASS" and iv["count"]==20
assert {x["path"]:x["sha256"] for x in iv["inputs"]}==allowed
assert set(n for n in files if n.startswith("INPUTS/"))=={"INPUTS/"+n for n in allowed}

cr=json.loads(data(root/"CHECK_RESULTS.json"))
assert cr["status"]=="PASS"
baseline=cr["baseline"]
assert baseline["status"]=="PASS"
program_sha=sha(data(root/"fresh_checks.py"))
labels=set()
for run in cr["runs"]:
    label=run["label"]
    assert label not in labels
    labels.add(label)
    assert run["program_sha256"]==program_sha
    assert run["returncode"]==run["expected_returncode"]
    assert safe(run["stdout_path"]) and safe(run["stderr_path"])
    output=json.loads(data(root/run["stdout_path"]))
    assert data(root/run["stderr_path"])==b""
    if label=="baseline":
        assert run["returncode"]==0 and output==baseline
    else:
        name=label.removeprefix("mutation_")
        assert label.startswith("mutation_") and name in baseline["mutations"]
        assert run["returncode"]==7
        assert output["status"]=="DELIBERATE_MATHEMATICAL_MUTATION_REJECTED"
        assert output["witness"]==baseline["mutations"][name]
assert labels=={"baseline"}|{"mutation_"+n for n in baseline["mutations"]}
assert len(baseline["mutations"])==21
assert sum(baseline["categories"].values())==baseline["assertions"]

seal=None
if args.seal:
    sealpath=Path(args.seal)
    seal=json.loads(data(sealpath))
    assert seal["schema"]=="AUD080-SEALS-1"
    assert seal["packet_name"]==root.name
    assert sha(data(root/"SHA256SUMS.json"))==seal["packet_manifest_sha256"]
    assert sha(data(root/"MEMBER_INVENTORY.txt"))==seal["packet_inventory_sha256"]
    assert sha(data(root/"REPORT.md"))==seal["report_sha256"]
    for key in ("archive","archive_inventory"):
        record=seal[key]
        assert safe(record["name"]) and "/" not in record["name"]
        path=sealpath.parent/record["name"]
        content=data(path)
        assert sha(content)==record["sha256"] and len(content)==record["size"]
    if args.archive:
        assert sha(data(Path(args.archive)))==seal["archive"]["sha256"]
    else:
        args.archive=str(sealpath.parent/seal["archive"]["name"])
if args.report:
    assert data(Path(args.report))==data(root/"REPORT.md"),"standalone report differs"

archive_members=[]
if args.archive:
    archive=Path(args.archive)
    regular(archive)
    seen=set()
    with tarfile.open(archive,"r:gz") as tf:
        for member in tf:
            name=member.name
            assert safe(name) and name not in seen,"unsafe/duplicate archive member"
            seen.add(name)
            assert member.isfile() and not member.issym() and not member.islnk(),"nonregular archive member"
            prefix=root.name+"/"
            assert name.startswith(prefix),"wrong archive root"
            rel=name[len(prefix):]
            assert rel in files,"unlisted archive file"
            b=data(files[rel])
            assert member.size==len(b),"archive size mismatch"
            f=tf.extractfile(member)
            assert f is not None
            content=f.read(len(b)+1)
            assert content==b,"archive byte mismatch"
            archive_members.append({"name":name,"size":len(b),"sha256":sha(b)})
    assert seen=={root.name+"/"+n for n in files},"archive member set mismatch"
    if seal:
        ai=json.loads(data(Path(args.seal).parent/seal["archive_inventory"]["name"]))
        assert ai["members"]==archive_members
        assert ai["count"]==len(archive_members)
for path in files.values():
    assert path.stat().st_mode & 0o222==0,"writable packet file: "+str(path)
for path in [root]+[x for x in root.rglob("*") if x.is_dir()]:
    assert path.stat().st_mode & 0o222==0,"writable packet directory: "+str(path)
if args.report:
    assert Path(args.report).stat().st_mode & 0o222==0
print(json.dumps({"status":"PASS","packet_files":len(files),"input_files":len(allowed),"safe_regular_archive_members":len(archive_members),"exact_checks":baseline["assertions"]-baseline["categories"]["floating_heat_envelope"],"floating_checks":baseline["categories"]["floating_heat_envelope"],"nonzero_mutation_runs":len(baseline["mutations"]),"read_only":True,"note":"Integrity and diagnostic consistency only; mathematical verdict is in REPORT.md."},sort_keys=True))

