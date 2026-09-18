#!/usr/bin/env python3
"""Final issuance of this AUD080 packet; writes only named evidence outputs.
Executed after history/report/records are finalized. No input/canonical edit.
"""
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tarfile

p=Path(__file__).resolve().parent
parent=p.parent
report=parent/"ROUND_028_MOMENT_TAIL_REVIEW.md"
def sha(b): return hashlib.sha256(b).hexdigest()
(p/"REPORT.md").write_bytes(report.read_bytes())
# Verify original twenty sources at their frozen assigned locations once more.
# The initial input copies are independently checked again too.
worktree=parent.parent.parent
for line in (p/"INPUT_MANIFEST.txt").read_text().splitlines():
    expected,rel=line.split("  ",1)
    for f in (worktree/rel,p/"INPUTS"/rel):
        assert not f.is_symlink() and stat.S_ISREG(f.lstat().st_mode),str(f)
        assert sha(f.read_bytes())==expected,str(f)
files={}
for f in p.rglob("*"):
    assert not f.is_symlink(),str(f)
    if f.is_file(): files[f.relative_to(p).as_posix()]=f
    else: assert f.is_dir()
assert "SHA256SUMS.json" not in files and "MEMBER_INVENTORY.txt" not in files
names=sorted(set(files)|{"SHA256SUMS.json","MEMBER_INVENTORY.txt"})
(p/"MEMBER_INVENTORY.txt").write_text("\n".join(names)+"\n")
files["MEMBER_INVENTORY.txt"]=p/"MEMBER_INVENTORY.txt"
manifest={"schema":"AUD080-SHA256-1","packet_name":p.name,"self_exclusion":"SHA256SUMS.json is sealed externally; all other regular members are included.","files":{name:{"size":len(path.read_bytes()),"sha256":sha(path.read_bytes())} for name,path in sorted(files.items())}}
(p/"SHA256SUMS.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
files["SHA256SUMS.json"]=p/"SHA256SUMS.json"
for f in files.values():f.chmod(0o444)
for d in sorted([x for x in p.rglob("*") if x.is_dir()],key=lambda x:len(x.parts),reverse=True):d.chmod(0o555)
p.chmod(0o555)
report.chmod(0o444)
archive=parent/(p.name+".tar.gz")
archive_inv=parent/(p.name+".ARCHIVE_MEMBERS.json")
seal=parent/(p.name+".SEALS.json")
log=parent/(p.name+".VERIFY.log")
receipt=parent/(p.name+".VERIFY.sha256")
for f in (archive,archive_inv,seal,log,receipt):assert not f.exists(),str(f)
members=[]
timestamp=int(datetime.datetime.now(datetime.timezone.utc).timestamp())
with tarfile.open(archive,"w:gz",format=tarfile.PAX_FORMAT) as tf:
    for name,f in sorted(files.items()):
        content=f.read_bytes()
        member_name=p.name+"/"+name
        info=tarfile.TarInfo(member_name)
        info.size=len(content);info.mode=0o444;info.mtime=timestamp
        info.uid=0;info.gid=0;info.uname="";info.gname=""
        tf.addfile(info,io.BytesIO(content))
        members.append({"name":member_name,"size":len(content),"sha256":sha(content)})
archive_inv.write_text(json.dumps({"count":len(members),"members":members},indent=2,sort_keys=True)+"\n")
def rec(f):
    b=f.read_bytes()
    return {"name":f.name,"size":len(b),"sha256":sha(b)}
seals={"schema":"AUD080-SEALS-1","packet_name":p.name,"report_sha256":sha(report.read_bytes()),"packet_manifest_sha256":sha((p/"SHA256SUMS.json").read_bytes()),"packet_inventory_sha256":sha((p/"MEMBER_INVENTORY.txt").read_bytes()),"archive":rec(archive),"archive_inventory":rec(archive_inv)}
seal.write_text(json.dumps(seals,indent=2,sort_keys=True)+"\n")
for f in (archive,archive_inv,seal):f.chmod(0o444)
cmd=[sys.executable,str(p/"verify.py"),"--archive",str(archive),"--seal",str(seal),"--report",str(report)]
r=subprocess.run(cmd,text=True,capture_output=True)
verification={"argv":cmd,"returncode":r.returncode,"stdout":r.stdout,"stderr":r.stderr,"seal_sha256":sha(seal.read_bytes()),"note":"Final issuance receipt. All packet content and seals were already frozen before this read-only verification."}
log.write_text(json.dumps(verification,indent=2,sort_keys=True)+"\n")
log.chmod(0o444)
receipt.write_text(sha(log.read_bytes())+"  "+log.name+"\n"+sha(seal.read_bytes())+"  "+seal.name+"\n")
receipt.chmod(0o444)
print(json.dumps({"status":"PASS" if r.returncode==0 else "VERIFIER_FAILED_ISSUANCE_PRESERVED","packet":str(p),"report":str(report),"archive":str(archive),"seals":str(seal),"verification_log":str(log),"verifier_returncode":r.returncode,"verifier_stdout":r.stdout,"verifier_stderr":r.stderr,"files":len(files)},sort_keys=True))
sys.exit(r.returncode)

