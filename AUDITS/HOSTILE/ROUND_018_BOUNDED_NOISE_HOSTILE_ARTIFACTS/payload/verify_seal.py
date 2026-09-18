#!/usr/bin/env python3
"""Read-only, no-extraction exact-byte AUD056 packet verification."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import stat
import sys
import tarfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    if not name or "\\" in name or name.startswith("/"):
        raise AssertionError("unsafe path: " + repr(name))
    if any(part in ("", ".", "..") for part in name.split("/")):
        raise AssertionError("unsafe path component: " + repr(name))
    if str(PurePosixPath(name)) != name:
        raise AssertionError("noncanonical path: " + repr(name))
    return name


def manifest(path):
    out = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            raise AssertionError("malformed manifest line")
        sha, name = match.groups()
        safe_name(name)
        if name in out:
            raise AssertionError("duplicate manifest name")
        out[name] = sha
    return out


def check_files(root, entries):
    for name, sha in entries.items():
        path = root / name
        if not stat.S_ISREG(path.lstat().st_mode):
            raise AssertionError("nonregular or linked file: " + name)
        if digest(path.read_bytes()) != sha:
            raise AssertionError("hash mismatch: " + name)


def verify():
    unsafe_controls = [
        "", "/absolute", "../escape", "payload/../escape",
        "payload//empty", "payload/./dot", "payload\\backslash"
    ]
    for candidate in unsafe_controls:
        try:
            safe_name(candidate)
        except AssertionError:
            pass
        else:
            raise AssertionError("unsafe-name mutation survived")
    payload = Path(__file__).resolve().parent
    outer = payload.parent
    workspace = outer.parents[2]
    portable = "--portable" in sys.argv[1:]
    inputs = manifest(payload / "INPUT_SHA256SUMS.txt")
    if len(inputs) != 17:
        raise AssertionError("input count is not exactly seventeen")
    check_files(payload / "inputs", inputs)
    outputs = manifest(payload / "OUTPUT_SHA256SUMS.txt")
    if any(name.startswith("inputs/") for name in outputs):
        raise AssertionError("overlapping input/output manifests")
    check_files(payload, outputs)
    expected = {"inputs/" + name: sha for name, sha in inputs.items()}
    expected.update(outputs)
    expected["OUTPUT_SHA256SUMS.txt"] = digest(
        (payload / "OUTPUT_SHA256SUMS.txt").read_bytes())
    actual = set()
    for path in payload.rglob("*"):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode) or not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
            raise AssertionError("unsafe payload object")
        if stat.S_ISREG(mode):
            actual.add(path.relative_to(payload).as_posix())
            if mode & 0o222:
                raise AssertionError("payload file is not read-only")
    if actual != set(expected):
        raise AssertionError("payload contains missing or untracked files")
    member_manifest = manifest(outer / "ARCHIVE_MEMBERS_SHA256SUMS.txt")
    archive_expected = {"payload/" + name: sha for name, sha in expected.items()}
    if member_manifest != archive_expected:
        raise AssertionError("archive member manifest differs from exact payload")
    archive_name = "ROUND_018_BOUNDED_NOISE_HOSTILE_PACKET.tar.gz"
    archive_hash = manifest(outer / "ARCHIVE_SHA256SUMS.txt")
    if set(archive_hash) != {archive_name}:
        raise AssertionError("unexpected archive digest entries")
    check_files(outer, archive_hash)
    seen = set()
    with tarfile.open(outer / archive_name, "r:gz") as archive:
        for member in archive.getmembers():
            name = safe_name(member.name)
            if name in seen:
                raise AssertionError("duplicate archive member")
            seen.add(name)
            if not member.isreg() or member.pax_headers or member.linkname:
                raise AssertionError("nonregular or extended archive member")
            if member.mode != 0o444 or name not in archive_expected:
                raise AssertionError("unsealed or unexpected archive member")
            stream = archive.extractfile(member)
            data = stream.read()
            if len(data) != member.size or digest(data) != archive_expected[name]:
                raise AssertionError("archive member byte/hash mismatch")
            relative = name[len("payload/"):]
            if data != (payload / relative).read_bytes():
                raise AssertionError("archive does not reproduce exact file bytes")
    if seen != set(archive_expected):
        raise AssertionError("inexact archive membership")
    if not portable:
        check_files(workspace, inputs)
        standalone = outer.parent / "ROUND_018_BOUNDED_NOISE_REVIEW.md"
        if standalone.read_bytes() != (payload / standalone.name).read_bytes():
            raise AssertionError("standalone review differs from packet")
        if standalone.stat().st_mode & 0o222:
            raise AssertionError("standalone review is not read-only")
    outer_seal = outer / "SEAL_SHA256SUMS.txt"
    if outer_seal.exists():
        check_files(outer, manifest(outer_seal))
    return {
        "audit": "AUD056 / TASK-086",
        "status": "PASS",
        "input_files": len(inputs),
        "payload_output_files": len(outputs),
        "archive_regular_file_members": len(seen),
        "archive_sha256": archive_hash[archive_name],
        "archive_exact_bytes": True,
        "unsafe_or_duplicate_members": 0,
        "unsafe_name_mutations_rejected": len(unsafe_controls),
        "untracked_payload_files": 0,
        "payload_and_report_readonly": True,
        "workspace_overlay_and_standalone_checked": not portable,
        "extraction_performed": False
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
