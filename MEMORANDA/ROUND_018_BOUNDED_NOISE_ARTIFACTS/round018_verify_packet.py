#!/usr/bin/env python3
"""Verify TASK-084 inputs, every packet byte, and safe exact archive membership.

No archive extraction is performed. Optional diagnostic reruns require an
explicit output path outside the sealed packet.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import zipfile

PACKET = "ROUND_018_BOUNDED_NOISE_ARTIFACTS"
MEMORANDUM = "ROUND_018_BOUNDED_NOISE_GAUSSIAN.md"
OUTPUT_MANIFEST = "OUTPUT_SHA256SUMS.txt"
INPUT_MANIFEST = "INPUT_SHA256SUMS.txt"
BASE = "faf6f775a55579722319795cd9a9921e5829a903"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def safe_relative(name):
    if not isinstance(name,str) or not name or "\\" in name or ":" in name:
        raise ValueError("Unsafe member spelling")
    if any(ord(c)<32 or ord(c)==127 for c in name):
        raise ValueError("Control character in member")
    p=PurePosixPath(name)
    if p.is_absolute() or any(c in ("",".","..") for c in p.parts) or str(p)!=name:
        raise ValueError("Unsafe or noncanonical relative member")
    return p

def manifest(data):
    rows={}
    for line in data.decode("utf-8").splitlines():
        match=re.fullmatch(r"([0-9a-f]{64})  (.+)",line)
        if match is None:
            raise ValueError("Malformed manifest line")
        sha,name=match.groups()
        safe_relative(name)
        if name in rows:
            raise ValueError("Duplicate manifest member")
        rows[name]=sha
    if not rows:
        raise ValueError("Empty manifest")
    return rows

def packet_files(packet):
    if packet.is_symlink() or not packet.is_dir():
        raise ValueError("Packet must be a nonsymlink directory")
    out={}
    for path in packet.rglob("*"):
        mode=path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise ValueError("Symlink inside packet")
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise ValueError("Nonregular packet file")
        name=path.relative_to(packet).as_posix()
        safe_relative(name)
        out[name]=path.read_bytes()
    return out

def verify(packet,seal_path,source_root=None,memorandum=None):
    seal=json.loads(seal_path.read_text())
    if seal["schema"]!="hocf.round018.construction-seal.v1":
        raise ValueError("Unknown seal schema")
    if seal["base_commit"]!=BASE or seal["packet_basename"]!=PACKET:
        raise ValueError("Unexpected base or packet")
    files=packet_files(packet)
    output=manifest(files[OUTPUT_MANIFEST])
    if set(files)!=(set(output)|{OUTPUT_MANIFEST}):
        raise ValueError("Packet output membership differs from manifest")
    for name,sha in output.items():
        if digest(files[name])!=sha:
            raise ValueError("Output hash mismatch: "+name)
    if digest(files[OUTPUT_MANIFEST])!=seal["output_manifest_sha256"]:
        raise ValueError("Output manifest seal mismatch")
    if digest(files[INPUT_MANIFEST])!=seal["input_manifest_sha256"]:
        raise ValueError("Input manifest seal mismatch")
    inputs=manifest(files[INPUT_MANIFEST])
    if len(inputs)!=14:
        raise ValueError("Expected exactly fourteen source inputs")
    actual_inputs={name[len("inputs/"):] for name in files if name.startswith("inputs/")}
    if set(inputs)!=actual_inputs:
        raise ValueError("Input copy membership differs")
    for name,sha in inputs.items():
        if digest(files["inputs/"+name])!=sha:
            raise ValueError("Input copy hash mismatch: "+name)
        if source_root is not None:
            path=source_root/name
            if path.is_symlink() or not path.is_file() or digest(path.read_bytes())!=sha:
                raise ValueError("Source-root hash mismatch: "+name)
    if digest(files[MEMORANDUM])!=seal["memorandum_sha256"]:
        raise ValueError("Memorandum seal mismatch")
    if memorandum is not None and memorandum.read_bytes()!=files[MEMORANDUM]:
        raise ValueError("Authoritative memorandum differs from packet copy")
    for key,name in [
        ("diagnostic_script_sha256","round018_exact_diagnostic.py"),
        ("diagnostic_result_sha256","round018_exact_diagnostic_results.json")
    ]:
        if digest(files[name])!=seal[key]:
            raise ValueError("Diagnostic seal mismatch")
    recorded=json.loads(files["round018_exact_diagnostic_results.json"])
    if recorded["status"]!="PASS" or recorded["script_sha256"]!=seal["diagnostic_script_sha256"]:
        raise ValueError("Diagnostic result/program mismatch")
    archive_name=seal["archive_basename"]
    p=safe_relative(archive_name)
    if len(p.parts)!=1:
        raise ValueError("Archive must be a sibling basename")
    archive=seal_path.parent/archive_name
    if archive.is_symlink() or not archive.is_file():
        raise ValueError("Archive must be a regular file")
    raw=archive.read_bytes()
    if len(raw)!=seal["archive_bytes"] or digest(raw)!=seal["archive_sha256"]:
        raise ValueError("Archive size/hash mismatch")
    expected={PACKET+"/"+name for name in files}
    listed=files["ARCHIVE_CONTENTS.txt"].decode().splitlines()
    if len(listed)!=len(set(listed)) or set(listed)!=expected:
        raise ValueError("Declared archive membership mismatch")
    with zipfile.ZipFile(archive,"r") as z:
        infos=z.infolist()
        names=[i.filename for i in infos]
        if len(names)!=len(set(names)):
            raise ValueError("Duplicate zip entries")
        if set(names)!=expected or len(names)!=seal["archive_members"]:
            raise ValueError("Archive member set mismatch")
        if sum(i.file_size for i in infos)>20_000_000:
            raise ValueError("Archive uncompressed size cap exceeded")
        for info in infos:
            safe_relative(info.filename)
            if info.orig_filename!=info.filename or info.is_dir() or info.flag_bits&1:
                raise ValueError("Unsafe, directory, or encrypted archive entry")
            mode=(info.external_attr>>16)&0xFFFF
            if mode and not stat.S_ISREG(mode):
                raise ValueError("Nonregular zip entry")
            if info.compress_type not in (zipfile.ZIP_STORED,zipfile.ZIP_DEFLATED):
                raise ValueError("Unsupported archive compression")
            if info.file_size>5_000_000:
                raise ValueError("Per-file archive cap exceeded")
            name=info.filename[len(PACKET)+1:]
            if not info.filename.startswith(PACKET+"/") or z.read(info)!=files[name]:
                raise ValueError("Archive bytes differ from packet")
    # Negative controls for member-name validation, without creating/extracting files.
    rejected=[]
    for name in ["../escape","/absolute","a/../escape","a//b","a/./b","C:/escape",
                 "bad\\name","null\x00name","line\nbreak",""]:
        try:
            safe_relative(name)
        except ValueError:
            rejected.append(repr(name))
        else:
            raise ValueError("Member safety negative control survived")
    return {
        "status":"PASS","base_commit":BASE,"inputs":len(inputs),
        "packet_files":len(files),"output_hashes":len(output),
        "archive_members":len(expected),"archive_sha256":seal["archive_sha256"],
        "exact_archive_bytes_match":True,"archive_extracted":False,
        "unsafe_name_negative_controls_rejected":len(rejected),
        "source_root_compared":str(source_root) if source_root is not None else None,
        "authoritative_memorandum_compared":memorandum is not None,
        "diagnostic_assertions":recorded["assertions"],
        "diagnostic_categories":len(recorded["categories"]),
        "mutation_families_rejected":len(recorded["mutation_rejections"]),
        "independent_certification":False
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--packet",type=Path,default=Path(__file__).parent)
    parser.add_argument("--seal",type=Path,required=True)
    parser.add_argument("--source-root",type=Path)
    parser.add_argument("--memorandum",type=Path)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--rerun-output",type=Path)
    args=parser.parse_args()
    result=verify(args.packet,args.seal,args.source_root,args.memorandum)
    if args.rerun_output is not None:
        # Protect immutable files, including against an output alias through symlinks.
        destination=args.rerun_output.resolve()
        if destination==args.packet.resolve() or args.packet.resolve() in destination.parents:
            raise ValueError("Diagnostic rerun output must be outside the sealed packet")
        if destination.exists():
            raise ValueError("Refusing to overwrite an existing rerun output")
        completed=subprocess.run(
            [sys.executable,str(args.packet/"round018_exact_diagnostic.py"),
             "--output",str(destination)],check=True,capture_output=True,text=True)
        rerun=json.loads(destination.read_text())
        recorded=json.loads((args.packet/"round018_exact_diagnostic_results.json").read_text())
        if rerun!=recorded:
            raise ValueError("Diagnostic rerun record differs")
        result["diagnostic_rerun_matches"]=True
    rendered=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        if args.output.exists():
            raise ValueError("Refusing to overwrite verification report")
        args.output.write_text(rendered)
    print(rendered,end="")

if __name__=="__main__":
    main()
