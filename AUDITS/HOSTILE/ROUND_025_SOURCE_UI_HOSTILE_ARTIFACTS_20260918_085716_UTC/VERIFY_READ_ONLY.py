#!/usr/bin/env python3
"""Portable standard-library verifier. Read-only, no extraction or execution."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import tarfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and str(p) == name,
            "unsafe or non-normalized member: " + repr(name))
    require(not any(x in ("", ".", "..") for x in p.parts) and "\\" not in name,
            "unsafe path component: " + repr(name))
    return p


def digest(data):
    return hashlib.sha256(data).hexdigest()


def regular_readonly(path):
    mode = path.lstat().st_mode
    require(stat.S_ISREG(mode) and not stat.S_ISLNK(mode), "not a regular file: " + str(path))
    require(mode & 0o222 == 0, "writable file: " + str(path))
    return path.read_bytes()


def parse_hashes(data):
    rows = {}
    for line in data.decode("utf-8").splitlines():
        hashed, name = line.split("  ", 1)
        safe(name)
        require(len(hashed) == 64 and all(c in "0123456789abcdef" for c in hashed), "bad digest")
        require(name not in rows, "duplicate digest member: " + name)
        rows[name] = hashed
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--payload-only", action="store_true")
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--seal", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    files = {}
    for parent, dirs, names in os.walk(root, followlinks=False):
        for name in dirs:
            p = Path(parent) / name
            mode = p.lstat().st_mode
            require(stat.S_ISDIR(mode) and not stat.S_ISLNK(mode), "non-directory or symlink inside packet")
        for name in names:
            p = Path(parent) / name
            relative = p.relative_to(root).as_posix()
            safe(relative)
            files[relative] = regular_readonly(p)
    members = files["MEMBERS.txt"].decode("utf-8").splitlines()
    require(len(members) == len(set(members)), "duplicate inventory member")
    require(members == sorted(members), "member inventory not sorted")
    for name in members:
        safe(name)
    require(set(members) == set(files), "payload/member inventory mismatch")
    hashes = parse_hashes(files["CONTENT_SHA256SUMS.txt"])
    require(set(hashes) == set(files) - {"CONTENT_SHA256SUMS.txt"}, "content hash inventory coverage mismatch")
    for name, hashed in hashes.items():
        require(digest(files[name]) == hashed, "payload digest mismatch: " + name)
    inputs = parse_hashes(files["INPUT_SHA256SUMS.txt"])
    require(len(inputs) == 15, "expected exactly 15 frozen inputs")
    require({name for name in files if name.startswith("INPUTS/")} == {"INPUTS/"+name for name in inputs}, "input copy set mismatch")
    for name, hashed in inputs.items():
        require(digest(files["INPUTS/"+name]) == hashed, "input digest mismatch: " + name)
    result = {
        "audit": "AUD070", "status": "PASS", "mode": "payload-only" if args.payload_only else "complete-issued-archive",
        "payload_file_count": len(files), "content_digest_count": len(hashes), "frozen_input_count": len(inputs),
        "report_sha256": digest(files["REPORT.md"]),
        "content_manifest_sha256": digest(files["CONTENT_SHA256SUMS.txt"]),
        "member_inventory_sha256": digest(files["MEMBERS.txt"]),
        "all_payload_files_regular_readonly": True,
        "no_writes_extraction_or_code_execution": True,
    }
    if not args.payload_only:
        archive = args.archive or root.with_name(root.name + ".tar.gz")
        seal_path = args.seal or root.with_name(root.name + ".SEAL.json")
        archive_bytes = regular_readonly(archive)
        seal = json.loads(regular_readonly(seal_path))
        require(seal["archive_name"] == archive.name, "seal archive name mismatch")
        require(seal["archive_sha256"] == digest(archive_bytes), "archive digest mismatch")
        require(seal["archive_bytes"] == len(archive_bytes), "archive size mismatch")
        require(seal["report_sha256"] == result["report_sha256"], "sealed report mismatch")
        require(seal["content_manifest_sha256"] == result["content_manifest_sha256"], "sealed manifest mismatch")
        require(seal["member_inventory_sha256"] == result["member_inventory_sha256"], "sealed member inventory mismatch")
        require(seal["payload_file_count"] == len(files), "sealed file count mismatch")
        seen = set()
        with tarfile.open(archive, "r:gz") as tar:
            for member in tar.getmembers():
                safe(member.name)
                require(member.name not in seen, "duplicate archive member")
                seen.add(member.name)
                require(member.isreg() and not member.issym() and not member.islnk(), "nonregular archive member")
                require(member.mode & 0o222 == 0, "writable archive member")
                require(not member.pax_headers, "unexpected PAX metadata")
                require(member.name in files, "unexpected archive member")
                stream = tar.extractfile(member)
                require(stream is not None, "missing member bytes")
                archived = stream.read()
                require(member.size == len(archived), "member size mismatch")
                require(archived == files[member.name], "archive/payload byte mismatch: " + member.name)
        require(seen == set(files), "archive member set mismatch")
        result.update({"archive_name": archive.name, "archive_sha256": digest(archive_bytes),
                       "archive_bytes": len(archive_bytes), "safe_unique_regular_readonly_archive_members": len(seen)})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
