#!/usr/bin/env python3
"""Verify this issued packet without extracting, modifying or installing."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tarfile

BASE=Path(__file__).resolve().parent
HEX=re.compile(r"^[0-9a-f]{64}$")

def require(condition,message):
    if not condition:
        raise ValueError(message)

def safe_rel(name):
    require(isinstance(name,str) and bool(name),"empty/non-string member")
    require("\\" not in name and "\x00" not in name,"backslash/NUL member")
    p=PurePosixPath(name)
    require(not p.is_absolute(),"absolute member")
    require(all(z not in ("",".","..") for z in name.split("/")),
            "empty/dot/parent member")
    require(str(p)==name,"noncanonical member")
    require(not (len(name)>=2 and name[1]==":"),"drive-like member")
    return name

def sha(data):
    return hashlib.sha256(data).hexdigest()

def unique_object(pairs):
    result={}
    for key,value in pairs:
        require(key not in result,"duplicate JSON key: "+key)
        result[key]=value
    return result

def read_json(p):
    return json.loads(p.read_text(),object_pairs_hook=unique_object)

def regular_bytes(p,readonly=False):
    st=p.lstat()
    require(stat.S_ISREG(st.st_mode),"nonregular file: "+str(p))
    require(st.st_nlink==1,"multiply linked file: "+str(p))
    if readonly:
        require(st.st_mode & 0o222 == 0,"writable file: "+str(p))
    return p.read_bytes()

def member_info_ok(member,expected):
    name=safe_rel(member.name)
    require(member.isreg(),"nonregular archive member: "+name)
    require(name in expected,"unexpected archive member: "+name)
    require(member.size==expected[name]["size"],"archive size mismatch: "+name)
    require(member.mode & 0o222 == 0,"writable archived member: "+name)
    return name

def safety_selftest():
    rejected=0
    for name in ("../bad","/absolute","a/../b","./a","a//b",
                 "a\\b","C:/drive","","a/./b"):
        try:
            safe_rel(name)
        except ValueError:
            rejected+=1
        else:
            raise AssertionError("unsafe path accepted: "+repr(name))
    for kind in (tarfile.SYMTYPE,tarfile.LNKTYPE,tarfile.DIRTYPE,
                 tarfile.FIFOTYPE,tarfile.CHRTYPE):
        info=tarfile.TarInfo("x")
        info.type=kind
        info.mode=0o444
        try:
            member_info_ok(info,{"x":{"size":0}})
        except ValueError:
            rejected+=1
        else:
            raise AssertionError("unsafe member type accepted")
    try:
        json.loads('{"a":1,"a":2}',object_pairs_hook=unique_object)
    except ValueError:
        rejected+=1
    else:
        raise AssertionError("duplicate JSON key accepted")
    return rejected

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive",type=Path)
    parser.add_argument("--report",type=Path)
    parser.add_argument("--outer-seal",type=Path)
    parser.add_argument("--require-readonly",action="store_true")
    parser.add_argument("--replay",action="store_true")
    args=parser.parse_args()
    safety=safety_selftest()
    inventory=read_json(BASE/"INVENTORY.json")
    require(inventory["schema"]==1,"inventory schema")
    payload=inventory["files"]
    require(isinstance(payload,list),"inventory file list")
    names=[safe_rel(row["path"]) for row in payload]
    require(names==sorted(set(names)),"unsorted/duplicate inventory paths")
    expected={}
    for row in payload:
        require(HEX.fullmatch(row["sha256"]) is not None,"invalid SHA")
        require(isinstance(row["size"],int) and row["size"]>=0,"invalid size")
        require(row["path"] not in ("INVENTORY.json","OUTPUT_SHA256SUMS.txt"),
                "self-referential inventory")
        expected[row["path"]]=row
    actual={}
    directories=0
    for p in BASE.rglob("*"):
        st=p.lstat()
        if stat.S_ISDIR(st.st_mode):
            directories+=1
            if args.require_readonly:
                require(st.st_mode & 0o222 == 0,"writable packet directory")
            continue
        name=safe_rel(p.relative_to(BASE).as_posix())
        data=regular_bytes(p,args.require_readonly)
        actual[name]={"path":name,"size":len(data),"sha256":sha(data)}
    if args.require_readonly:
        require(BASE.stat().st_mode & 0o222 == 0,"writable packet root")
    all_names=set(expected)|{"INVENTORY.json","OUTPUT_SHA256SUMS.txt"}
    require(set(actual)==all_names,"packet missing or extra regular files")
    for name,row in expected.items():
        require(actual[name]==row,"payload mismatch: "+name)

    manifest={}
    for line in (BASE/"OUTPUT_SHA256SUMS.txt").read_text().splitlines():
        digest,name=line.split("  ",1)
        safe_rel(name)
        require(HEX.fullmatch(digest) is not None,"output digest syntax")
        require(name not in manifest,"duplicate output manifest member")
        manifest[name]=digest
    require(set(manifest)==set(actual)-{"OUTPUT_SHA256SUMS.txt"},
            "output manifest incomplete or extra")
    for name,digest in manifest.items():
        require(actual[name]["sha256"]==digest,"output digest mismatch: "+name)

    input_manifest=(BASE/"INPUT_SHA256SUMS.txt").read_text().splitlines()
    require(len(input_manifest)==17,"input count not 17")
    for line in input_manifest:
        digest,name=line.split("  ",1)
        safe_rel(name)
        require(HEX.fullmatch(digest) is not None,"input digest syntax")
        require(actual["INPUTS/"+name]["sha256"]==digest,
                "input copy differs: "+name)

    archive_count=0
    archive_sha=None
    if args.archive is not None:
        archive_bytes=regular_bytes(args.archive,args.require_readonly)
        archive_sha=sha(archive_bytes)
        seen=set()
        # Stream checks only: no disk extraction and no link following.
        with tarfile.open(fileobj=io.BytesIO(archive_bytes),mode="r|gz") as archive:
            for member in archive:
                require(len(seen)<len(actual),"too many archive members")
                name=member_info_ok(member,actual)
                require(name not in seen,"duplicate archive member")
                seen.add(name)
                stream=archive.extractfile(member)
                require(stream is not None,"missing regular-member stream")
                data=stream.read(member.size+1)
                require(len(data)==member.size,"archive content size mismatch")
                require(sha(data)==actual[name]["sha256"],
                        "archive byte mismatch: "+name)
        require(seen==set(actual),"archive omits packet files")
        archive_count=len(seen)
    report_sha=None
    if args.report is not None:
        data=regular_bytes(args.report,args.require_readonly)
        report_sha=sha(data)
        require(data==regular_bytes(BASE/"REPORT.md",args.require_readonly),
                "canonical report/copy byte mismatch")

    result=read_json(BASE/"DIAGNOSTIC_RESULT.json")
    require(result["status"]=="PASS","recorded diagnostic did not pass")
    require(result["diagnostic_sha256"]==actual["diagnostic.py"]["sha256"],
            "diagnostic source/version mismatch")
    require(result["checks"]==3845 and result["mutation_count"]==20,
            "unexpected issued diagnostic result")
    if args.replay:
        env=dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"]="1"
        proc=subprocess.run([sys.executable,"-B",str(BASE/"diagnostic.py")],
                            cwd=str(BASE),env=env,stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,text=True,check=False)
        require(proc.returncode==0,"diagnostic replay failed: "+proc.stderr)
        require(json.loads(proc.stdout,object_pairs_hook=unique_object)==result,
                "diagnostic replay differs from full recorded result")

    outer_count=0
    if args.outer_seal is not None:
        outer_data=regular_bytes(args.outer_seal,args.require_readonly)
        outer=json.loads(outer_data,object_pairs_hook=unique_object)
        require(outer["schema"]==1,"outer seal schema")
        seen=set()
        for row in outer["siblings"]:
            name=safe_rel(row["path"])
            require("/" not in name,"outer sibling must be a basename")
            require(name not in seen,"duplicate outer sibling")
            seen.add(name)
            data=regular_bytes(args.outer_seal.parent/name,args.require_readonly)
            require(len(data)==row["size"] and sha(data)==row["sha256"],
                    "outer sibling mismatch: "+name)
        outer_count=len(seen)
        require(outer["packet_name"]==BASE.name,"outer packet name")
        require(outer["packet_manifest_sha256"]==
                actual["OUTPUT_SHA256SUMS.txt"]["sha256"],"outer manifest mismatch")

    print(json.dumps({
        "status":"PASS",
        "input_copies":17,
        "payload_members":len(payload),
        "packet_regular_members":len(actual),
        "packet_directories":directories,
        "archive_regular_members":archive_count,
        "archive_sha256":archive_sha,
        "report_sha256":report_sha,
        "diagnostic_checks":result["checks"],
        "diagnostic_categories":len(result["categories"]),
        "nonzero_mutation_witnesses":result["mutation_count"],
        "diagnostic_replayed":args.replay,
        "safety_rejections":safety,
        "readonly_required":args.require_readonly,
        "outer_siblings_verified":outer_count,
        "writes":0,
        "extractions":0,
        "independent_mathematical_certification":False
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
