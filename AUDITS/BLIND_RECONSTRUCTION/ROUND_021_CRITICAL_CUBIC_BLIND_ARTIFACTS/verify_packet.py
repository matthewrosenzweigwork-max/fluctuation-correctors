#!/usr/bin/env python3
"""Read-only AUD061 packet verifier. Never extracts or writes archive members."""
from pathlib import Path, PurePosixPath
from io import BytesIO
import argparse
import hashlib
import json
import re
import stat
import warnings
import zipfile

EXPECTED_INPUT_MANIFEST_SHA256 = "03b7096962cd368eda6fc69bacb9fdbc0a99fe309f6433782e34a73c4e1cf5b2"
OUTPUTS = {
    "README.md", "REPORT.md", "SOURCE_EXPOSURE.md", "exact_diagnostic.py",
    "RESULTS.json", "verify_packet.py", "VERIFICATION.md",
    "PRESCRIBED_INPUT_SHA256SUMS.txt",
}
ARCHIVE_NAME = "ROUND_021_CRITICAL_CUBIC_BLIND_PACKET.zip"
AUX = {"OUTPUT_SHA256SUMS.txt", "ARCHIVE_MEMBERS_SHA256SUMS.txt", "SEAL.json", ARCHIVE_NAME}
REPORT_NAME = "ROUND_021_CRITICAL_CUBIC_RECONSTRUCTION.md"

def require(ok,message):
    if not ok:
        raise ValueError(message)
def digest(data):
    return hashlib.sha256(data).hexdigest()
def safe_name(name):
    require(isinstance(name,str) and name, "empty/nonstring member name")
    require("\\" not in name and "\x00" not in name, "unsafe backslash/NUL")
    p=PurePosixPath(name)
    require(not p.is_absolute(), "absolute member path")
    require(name==p.as_posix() and all(x not in ("", ".", "..") for x in p.parts),
            "noncanonical/traversal member path")
    require(not name.endswith("/"), "directory member forbidden")
    return name
def parse_manifest(data):
    out={}
    for line in data.decode("utf-8").splitlines():
        require(re.fullmatch(r"[0-9a-f]{64}  .+",line) is not None, "malformed manifest line")
        sha,name=line.split("  ",1)
        safe_name(name)
        require(name not in out, "duplicate manifest path")
        out[name]=sha
    return out
def read_regular(base,name):
    safe_name(name)
    current=base
    require(not base.is_symlink(),"symlink packet directory")
    for part in PurePosixPath(name).parts:
        current=current/part
        require(not current.is_symlink(),"symlink filesystem path: "+name)
    mode=current.stat().st_mode
    require(stat.S_ISREG(mode), "not regular: "+name)
    require(mode & 0o222 == 0, "issued file is writable: "+name)
    return current.read_bytes()
def checked_zip(blob,expected):
    require(sum(len(x) for x in expected.values())<=4_000_000, "oversized expected packet")
    with zipfile.ZipFile(BytesIO(blob),"r") as archive:
        infos=archive.infolist()
        names=[info.filename for info in infos]
        require(len(names)==len(set(names)), "duplicate archive member")
        for info in infos:
            safe_name(info.filename)
            require(info.orig_filename==info.filename and "\x00" not in info.orig_filename,
                    "altered/NUL archive name")
            require(not info.is_dir(), "archive directory entry")
            require(stat.S_ISREG(info.external_attr>>16), "nonregular/symlink archive member")
            require((info.external_attr>>16)&0o222==0, "writable archive member")
            require(not info.flag_bits&1, "encrypted archive member")
            require(info.compress_type in (zipfile.ZIP_STORED,zipfile.ZIP_DEFLATED),
                    "unsupported archive compression")
        require(set(names)==set(expected), "archive membership mismatch")
        for info in infos:
            require(info.file_size==len(expected[info.filename]),"archive size mismatch")
            actual=archive.read(info)  # CRC checked by zipfile; no extraction.
            require(actual==expected[info.filename],"archive byte mismatch: "+info.filename)
    return len(expected)
def archive_fixture(entries):
    target=BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore",UserWarning)
        with zipfile.ZipFile(target,"w",compression=zipfile.ZIP_STORED) as archive:
            for name,data,mode in entries:
                info=zipfile.ZipInfo(name,(2026,9,18,0,0,0))
                info.create_system=3
                info.external_attr=mode<<16
                archive.writestr(info,data)
    return target.getvalue()
def self_tests():
    reg=stat.S_IFREG|0o444
    expected={"a.txt":b"unit"}
    good=[("a.txt",b"unit",reg)]
    require(checked_zip(archive_fixture(good),expected)==1,"valid fixture failed")
    cases={
        "duplicate":good+good,
        "traversal":[("../a.txt",b"unit",reg)],
        "absolute":[("/a.txt",b"unit",reg)],
        "backslash":[("d\\a.txt",b"unit",reg)],
        "symlink":[("a.txt",b"unit",stat.S_IFLNK|0o777)],
        "wrong_bytes":[("a.txt",b"evil",reg)],
        "unexpected_member":good+[("b.txt",b"extra",reg)],
        "missing_member":[],
        "writable_member":[("a.txt",b"unit",stat.S_IFREG|0o644)],
    }
    detected={}
    for name,entries in cases.items():
        try:
            checked_zip(archive_fixture(entries),expected)
        except (ValueError,zipfile.BadZipFile) as exc:
            detected[name]=str(exc)
        else:
            raise AssertionError("vacuous/undetected verifier mutation: "+name)
    return detected

def verify(base):
    require(base.is_dir() and not base.is_symlink(),"invalid packet directory")
    seal=json.loads(read_regular(base,"SEAL.json"))
    require(set(seal)=={"schema","base_commit","branch","input_count","archive_members",
                       "archive_sha256","input_manifest_sha256","output_manifest_sha256",
                       "archive_manifest_sha256","report_sha256"},"unexpected seal schema")
    require(seal["schema"]=="AUD061-v1","wrong schema")
    require(seal["base_commit"]=="e75f8b780682a7e9fb0715b5e8b5873be684a2e8","wrong base")
    require(seal["branch"]=="codex/hocf-r021-critical-cubic-blind","wrong branch")
    indata=read_regular(base,"PRESCRIBED_INPUT_SHA256SUMS.txt")
    require(digest(indata)==EXPECTED_INPUT_MANIFEST_SHA256==seal["input_manifest_sha256"],
            "prescribed input manifest digest mismatch")
    inputs=parse_manifest(indata)
    require(len(inputs)==seal["input_count"]==29,"input count mismatch")
    files={}
    for name,sha in inputs.items():
        rel="INPUTS/"+name
        data=read_regular(base,rel)
        require(digest(data)==sha,"input bytes mismatch: "+name)
        files[rel]=data
    outdata=read_regular(base,"OUTPUT_SHA256SUMS.txt")
    require(digest(outdata)==seal["output_manifest_sha256"],"output manifest digest mismatch")
    outputs=parse_manifest(outdata)
    require(set(outputs)==OUTPUTS,"output membership mismatch")
    for name,sha in outputs.items():
        data=read_regular(base,name)
        require(digest(data)==sha,"output bytes mismatch: "+name)
        files[name]=data
    files["OUTPUT_SHA256SUMS.txt"]=outdata
    membersdata=read_regular(base,"ARCHIVE_MEMBERS_SHA256SUMS.txt")
    require(digest(membersdata)==seal["archive_manifest_sha256"],
            "archive member manifest digest mismatch")
    members=parse_manifest(membersdata)
    require(set(members)==set(files),"archive manifest membership mismatch")
    require(all(members[name]==digest(data) for name,data in files.items()),
            "archive manifest bytes mismatch")
    blob=read_regular(base,ARCHIVE_NAME)
    require(digest(blob)==seal["archive_sha256"],"archive digest mismatch")
    number=checked_zip(blob,files)
    require(number==seal["archive_members"]==38,"archive member count mismatch")
    present=set()
    allowed_dirs=set()
    expected_names=set(files)|AUX
    for name in expected_names:
        pp=PurePosixPath(name).parent
        while pp.as_posix()!=".":
            allowed_dirs.add(pp.as_posix())
            pp=pp.parent
    for path in base.rglob("*"):
        name=path.relative_to(base).as_posix()
        require(not path.is_symlink(),"unexpected filesystem symlink")
        if path.is_file():
            present.add(name)
        else:
            require(path.is_dir() and name in allowed_dirs,"unexpected directory")
            require(path.stat().st_mode&0o222==0,"issued directory writable")
    require(present==expected_names,"disk packet membership mismatch")
    require(base.stat().st_mode&0o222==0,"packet directory writable")
    external=base.parent/REPORT_NAME
    require(external.is_file() and not external.is_symlink(),"missing or symlink report")
    require(external.stat().st_mode&0o222==0,"external report writable")
    report=external.read_bytes()
    require(report==files["REPORT.md"] and digest(report)==seal["report_sha256"],
            "external report byte mismatch")
    require(json.loads(files["RESULTS.json"])["status"]=="PASS","diagnostic status mismatch")
    return {"status":"PASS","input_files":29,"archive_members":number,
            "disk_packet_files":len(present),"all_issued_files_read_only":True,
            "archive_sha256":seal["archive_sha256"],"report_sha256":seal["report_sha256"],
            "extraction_performed":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("packet",nargs="?",type=Path,default=Path(__file__).absolute().parent)
    parser.add_argument("--self-test-only",action="store_true")
    args=parser.parse_args()
    try:
        controls=self_tests()
        if args.self_test_only:
            result={"status":"PASS","nonvacuous_integrity_mutations":controls,
                    "extraction_performed":False}
        else:
            result=verify(args.packet.absolute())
            result["nonvacuous_integrity_mutation_count"]=len(controls)
        print(json.dumps(result,indent=2,sort_keys=True))
    except (ValueError,OSError,zipfile.BadZipFile,json.JSONDecodeError) as exc:
        raise SystemExit("FAIL: "+str(exc))
