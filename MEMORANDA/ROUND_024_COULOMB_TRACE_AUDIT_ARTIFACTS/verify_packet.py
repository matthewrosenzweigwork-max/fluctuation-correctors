#!/usr/bin/env python3
"""Read-only safe verifier. Never extracts archive members or follows symlinks."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import tarfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    p = PurePosixPath(name)
    if not name or p.is_absolute() or any(s in ("", ".", "..") for s in p.parts):
        raise ValueError("unsafe member name: " + repr(name))
    if str(p) != name or "\\" in name or "\x00" in name:
        raise ValueError("noncanonical member name: " + repr(name))
    return p


def parse_manifest(data):
    out = {}
    for line in data.decode("utf-8").splitlines():
        value, name = line.split("  ", 1)
        safe_name(name)
        if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
            raise ValueError("invalid digest")
        if name in out:
            raise ValueError("duplicate manifest name")
        out[name] = value
    return out


def no_symlink_path(root, relative):
    p = root
    for part in safe_name(relative).parts:
        p = p / part
        if p.is_symlink():
            raise ValueError("symlink in local path: " + str(p))
    return p


def verify_archive(source, entries, manifest_name, manifest_bytes):
    expected_names = set(entries) | {manifest_name}
    seen = set()
    kwargs = {"fileobj": source} if hasattr(source, "read") else {"name": source}
    with tarfile.open(mode="r:gz", **kwargs) as tf:
        for member in tf:
            safe_name(member.name)
            if member.name in seen or member.name not in expected_names:
                raise ValueError("duplicate or unexpected archive member")
            if not member.isfile() or member.issym() or member.islnk():
                raise ValueError("archive contains a nonregular member")
            if member.size < 0 or member.size > 10_000_000:
                raise ValueError("member size outside packet bound")
            stream = tf.extractfile(member)
            if stream is None:
                raise ValueError("missing member data")
            data = stream.read(10_000_001)
            if len(data) != member.size:
                raise ValueError("member size mismatch")
            expected = digest(manifest_bytes) if member.name == manifest_name else entries[member.name]
            if digest(data) != expected:
                raise ValueError("archive digest mismatch: " + member.name)
            seen.add(member.name)
        if seen != expected_names:
            raise ValueError("archive missing members")
    return len(seen)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--require-read-only", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest_name = "MEMORANDA/ROUND_024_COULOMB_TRACE_AUDIT_ARTIFACTS/BUNDLE_SHA256SUMS.txt"
    manifest_path = no_symlink_path(root, manifest_name)
    manifest_bytes = manifest_path.read_bytes()
    entries = parse_manifest(manifest_bytes)
    if manifest_name in entries:
        raise ValueError("manifest must exclude itself")
    if len(entries) < 25:
        raise ValueError("incomplete packet")
    artifact_dir = manifest_path.parent
    local_names = {"MEMORANDA/ROUND_024_COULOMB_TRACE_SOURCE_AUDIT.md"}
    for p in artifact_dir.rglob("*"):
        if p.is_symlink():
            raise ValueError("symlink in packet inventory")
        if p.is_file() and p != manifest_path:
            local_names.add(p.relative_to(root).as_posix())
    if local_names != set(entries):
        raise ValueError("local packet inventory differs from manifest")
    total = 0
    for relative, expected in entries.items():
        p = no_symlink_path(root, relative)
        if not p.is_file() or not stat.S_ISREG(p.stat().st_mode):
            raise ValueError("nonregular local file: " + relative)
        data = p.read_bytes()
        if digest(data) != expected:
            raise ValueError("local digest mismatch: " + relative)
        if args.require_read_only and p.stat().st_mode & 0o222:
            raise ValueError("writable issued file: " + relative)
        total += len(data)
    if args.require_read_only and manifest_path.stat().st_mode & 0o222:
        raise ValueError("writable manifest")
    archived = 0
    if args.archive:
        if args.archive.is_symlink() or not args.archive.is_file():
            raise ValueError("archive must be a regular nonsymlink file")
        if args.require_read_only and args.archive.stat().st_mode & 0o222:
            raise ValueError("writable archive")
        archived = verify_archive(args.archive, entries, manifest_name, manifest_bytes)
    print(json.dumps({
        "status": "PASS",
        "local_files": len(entries),
        "local_payload_bytes": total,
        "archive_members": archived,
        "manifest_sha256": digest(manifest_bytes),
        "archive_sha256": digest(args.archive.read_bytes()) if args.archive else None,
        "read_only_required": args.require_read_only,
        "extracted": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
