#!/usr/bin/env python3
"""Verify this AUD054 packet without importing any mathematical source."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    p = PurePosixPath(name)
    if (not name or p.is_absolute() or str(p) != name or ".." in p.parts
            or "." in p.parts or "\\" in name or ":" in name or "\x00" in name):
        raise ValueError("unsafe member path: " + repr(name))
    return p


def entries(data):
    out = {}
    for line in data.decode("utf-8").splitlines():
        d, name = line.split("  ", 1)
        safe_name(name)
        if len(d) != 64 or any(c not in "0123456789abcdef" for c in d):
            raise ValueError("invalid digest")
        if name in out:
            raise ValueError("duplicate manifest name")
        out[name] = d
    return out


def regular_bytes(root, name):
    p = root
    for part in safe_name(name).parts:
        p = p / part
        if p.is_symlink():
            raise ValueError("symlink in input/output path: " + name)
    if not p.is_file():
        raise ValueError("missing regular file: " + name)
    return p.read_bytes()


def verify_directory(root):
    original = entries(regular_bytes(root, "INPUT_SHA256SUMS.txt"))
    inputs = entries(regular_bytes(root, "INPUT_COPY_SHA256SUMS.txt"))
    outputs = entries(regular_bytes(root, "OUTPUT_SHA256SUMS.txt"))
    if len(original) != 14 or inputs != {"INPUTS/"+k:v for k,v in original.items()}:
        raise ValueError("input copy map does not reproduce fourteen original seals")
    if set(inputs) & set(outputs):
        raise ValueError("input/output manifest overlap")
    payload = dict(inputs)
    payload.update(outputs)
    payload["OUTPUT_SHA256SUMS.txt"] = digest(regular_bytes(root, "OUTPUT_SHA256SUMS.txt"))
    for name, want in payload.items():
        if digest(regular_bytes(root, name)) != want:
            raise ValueError("file hash mismatch: " + name)
    return payload


def verify_archive(root, archive, payload, extraction):
    side = archive.with_name(archive.name + ".sha256")
    sealed = entries(side.read_bytes())
    if sealed != {archive.name:digest(archive.read_bytes())}:
        raise ValueError("archive byte digest mismatch")
    member_seal = entries(regular_bytes(root, "ARCHIVE_MEMBERS_SHA256SUMS.txt"))
    if member_seal != payload:
        raise ValueError("archive member manifest differs from exact payload")
    if extraction is not None:
        if extraction.exists() or extraction.is_symlink():
            raise ValueError("extraction directory must not exist")
        extraction.mkdir(parents=True)
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        names = [i.filename for i in infos]
        if len(names) != len(set(names)) or set(names) != set(payload):
            raise ValueError("duplicate, extra or missing archive members")
        if z.testzip() is not None:
            raise ValueError("ZIP CRC test failed")
        for info in infos:
            safe_name(info.filename)
            mode = info.external_attr >> 16
            if info.is_dir() or stat.S_IFMT(mode) != stat.S_IFREG:
                raise ValueError("non-regular archive member")
            data = z.read(info)
            if digest(data) != payload[info.filename]:
                raise ValueError("archive member digest mismatch")
            if data != regular_bytes(root, info.filename):
                raise ValueError("archive member bytes differ from packet")
            if extraction is not None:
                target = extraction.joinpath(*safe_name(info.filename).parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                if target.read_bytes() != data:
                    raise ValueError("extraction byte mismatch")
    if extraction is not None:
        if verify_directory(extraction) != payload:
            raise ValueError("extracted input/output verification mismatch")
    return {"archive_sha256":digest(archive.read_bytes()),
            "archive_members":len(payload),"all_members_regular":True,
            "exact_member_set":True,"all_member_bytes_match":True,
            "safe_fresh_extraction_verified":extraction is not None}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--directory",type=Path,default=Path(__file__).parent)
    p.add_argument("--archive",type=Path)
    p.add_argument("--extract-to",type=Path)
    args = p.parse_args()
    root = args.directory.resolve()
    payload = verify_directory(root)
    result = {"status":"PASS","input_count":14,"payload_files":len(payload),
              "all_input_output_hashes_match":True}
    if args.archive:
        result.update(verify_archive(root,args.archive.resolve(),payload,args.extract_to))
    elif args.extract_to:
        raise ValueError("extraction requires an archive")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
