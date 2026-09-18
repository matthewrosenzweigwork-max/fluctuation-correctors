#!/usr/bin/env python3
"""Read-only exact ZIP verifier. Never extracts archive members."""
from __future__ import annotations

import argparse
from copy import deepcopy
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

BASE = "4ab1d492c3bb9bb3537732f2d75502971f5ee6da"
PACKET = "MEMORANDA/ROUND_024_THRESHOLD_FALSIFICATION_ARTIFACTS/"
MEMO = "MEMORANDA/ROUND_024_THRESHOLD_DYNAMIC_FALSIFICATION.md"
MANIFEST = PACKET + "OUTPUT_MANIFEST.json"
INPUT_MANIFEST = PACKET + "INPUT_SHA256SUMS.txt"
MAX_ARCHIVE = 128 * 1024 * 1024
MAX_FILE = 32 * 1024 * 1024
MAX_TOTAL = 128 * 1024 * 1024
MAX_MEMBERS = 200


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return sha256(data).hexdigest()


def safe_name(name):
    require(isinstance(name, str) and name and "\x00" not in name, "invalid name")
    require("\\" not in name and ":" not in name, "non-POSIX or drive path")
    p = PurePosixPath(name)
    require(not p.is_absolute(), "absolute member")
    require(all(x not in ("", ".", "..") for x in name.split("/")), "unsafe path component")
    require(str(p) == name, "noncanonical member")
    return name


def pairs_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def json_bytes(data):
    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs_no_duplicates)


def verify_bytes(blob, seal):
    require(seal.get("schema") == "hocf-task103-seal-v1", "seal schema")
    require(seal.get("base") == BASE, "wrong base")
    require(seal.get("read_only_issued") is True, "missing read-only issuance")
    require(len(blob) <= MAX_ARCHIVE and len(blob) == seal["archive_bytes"], "archive size")
    require(digest(blob) == seal["archive_sha256"], "archive digest")
    require(seal.get("manifest_path") == MANIFEST, "manifest path")
    with zipfile.ZipFile(BytesIO(blob)) as archive:
        infos = archive.infolist()
        names = [safe_name(i.filename) for i in infos]
        require(len(names) == len(set(names)), "duplicate ZIP member")
        require(0 < len(infos) <= MAX_MEMBERS, "member count limit")
        require(len(infos) == seal["member_count"], "sealed member count")
        require(sum(i.file_size for i in infos) <= MAX_TOTAL, "expanded size limit")
        for i in infos:
            require(not i.is_dir(), "directory member")
            require(not (i.flag_bits & 1), "encrypted member")
            require(i.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED), "compression")
            require(0 <= i.file_size <= MAX_FILE, "member size limit")
            require(i.create_system == 3, "missing Unix file type")
            mode = (i.external_attr >> 16) & 0xffff
            require(stat.S_ISREG(mode), "nonregular member")
            require(stat.S_IMODE(mode) == 0o444, "writable or wrong member mode")
            require(i.filename == MEMO or i.filename.startswith(PACKET), "outside packet scope")
        require(MANIFEST in names, "missing manifest")
        manifest_bytes = archive.read(MANIFEST)
        require(len(manifest_bytes) <= 1024 * 1024, "manifest size limit")
        require(digest(manifest_bytes) == seal["manifest_sha256"], "manifest digest")
        manifest = json_bytes(manifest_bytes)
        require(manifest.get("schema") == "hocf-task103-payload-v1", "manifest schema")
        require(manifest.get("base") == BASE, "manifest base")
        members = manifest["members"]
        require(isinstance(members, dict) and MANIFEST not in members, "manifest self-cycle")
        require(set(names) == set(members) | {MANIFEST}, "exact membership")
        require(MEMO in members and INPUT_MANIFEST in members, "required members")
        payload = {}
        for name, record in members.items():
            safe_name(name)
            require(name == MEMO or name.startswith(PACKET), "manifest scope")
            require(record.get("mode") == "0444", "manifest mode")
            data = archive.read(name)  # zipfile verifies CRC; bytes never become paths.
            require(len(data) == record["bytes"], "payload byte count: " + name)
            require(digest(data) == record["sha256"], "payload digest: " + name)
            payload[name] = data
        input_bytes = payload[INPUT_MANIFEST]
        require(digest(input_bytes) == seal["input_manifest_sha256"], "input manifest pin")
        lines = input_bytes.decode("utf-8").splitlines()
        require(len(lines) == 20 and seal.get("input_count") == 20, "exact 20 inputs")
        inputs = set()
        for line in lines:
            match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            require(match is not None, "input manifest syntax")
            source_digest, relative = match.groups()
            safe_name(relative)
            require(relative not in inputs, "duplicate input")
            inputs.add(relative)
            name = PACKET + "INPUTS/" + relative
            require(name in payload and digest(payload[name]) == source_digest, "input bytes: " + relative)
        copied_inputs = {name[len(PACKET+"INPUTS/"):] for name in payload if name.startswith(PACKET+"INPUTS/")}
        require(copied_inputs == inputs, "exact input-copy membership")
        payload[MANIFEST] = manifest_bytes
        return payload


def verify_workspace(payload, workspace):
    root = Path(workspace).resolve(strict=True)
    for relative, expected in payload.items():
        current = root
        for part in PurePosixPath(relative).parts:
            current = current / part
            require(not current.is_symlink(), "workspace symlink: " + relative)
        require(current.is_file(), "missing workspace file: " + relative)
        require(not (current.stat().st_mode & 0o222), "writable workspace file: " + relative)
        require(current.read_bytes() == expected, "workspace bytes: " + relative)
    packet_root = root / PACKET
    require(packet_root.is_dir() and not (packet_root.stat().st_mode & 0o222), "writable packet directory")
    actual_files = set()
    for item in packet_root.rglob("*"):
        require(not item.is_symlink(), "extra workspace symlink")
        if item.is_file():
            actual_files.add(item.relative_to(root).as_posix())
        else:
            require(item.is_dir() and not (item.stat().st_mode & 0o222), "unsafe extra directory")
    require(actual_files == {n for n in payload if n.startswith(PACKET)}, "exact workspace packet files")
    for name in payload:
        if not name.startswith(PACKET):
            continue
        parent = (root / name).parent
        while parent != packet_root:
            require(parent.is_dir() and not parent.is_symlink(), "unsafe packet directory")
            require(not (parent.stat().st_mode & 0o222), "writable packet subdirectory")
            parent = parent.parent


def zip_blob(entries):
    stream = BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data, mode in entries:
            info = zipfile.ZipInfo(name, (2026, 9, 18, 0, 0, 0))
            info.create_system = 3
            info.external_attr = mode << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)
    return stream.getvalue()


def seal_for(blob, manifest, input_manifest, count):
    return {
        "schema": "hocf-task103-seal-v1", "base": BASE, "read_only_issued": True,
        "archive_bytes": len(blob), "archive_sha256": digest(blob),
        "manifest_path": MANIFEST, "manifest_sha256": digest(manifest),
        "input_manifest_sha256": digest(input_manifest),
        "member_count": count, "input_count": 20,
    }


def self_test():
    """Adversarial in-memory fixtures; mutated outer hashes are refreshed."""
    payload = {MEMO: b"bounded mathematical report\n"}
    lines = []
    for i in range(20):
        source = "SOURCE_" + str(i).zfill(2) + ".md"
        data = ("exact input " + str(i) + "\n").encode()
        payload[PACKET + "INPUTS/" + source] = data
        lines.append(digest(data) + "  " + source)
    inputs = ("\n".join(lines) + "\n").encode()
    payload[INPUT_MANIFEST] = inputs
    manifest = json.dumps({
        "schema": "hocf-task103-payload-v1", "base": BASE,
        "members": {k: {"sha256": digest(v), "bytes": len(v), "mode": "0444"}
                    for k, v in sorted(payload.items())},
    }, sort_keys=True).encode()
    entries = [(k, v, stat.S_IFREG | 0o444) for k, v in sorted(payload.items())]
    entries.append((MANIFEST, manifest, stat.S_IFREG | 0o444))
    original = zip_blob(entries)
    good_seal = seal_for(original, manifest, inputs, len(entries))
    require(len(verify_bytes(original, good_seal)) == len(entries), "baseline verification")
    tests = {}

    variants = {}
    variants["unsafe_parent"] = entries + [(PACKET + "../escape", b"x", stat.S_IFREG | 0o444)]
    variants["absolute"] = entries + [("/absolute", b"x", stat.S_IFREG | 0o444)]
    variants["backslash"] = entries + [(PACKET + "a\\b", b"x", stat.S_IFREG | 0o444)]
    variants["extra_member"] = entries + [(PACKET + "unexpected", b"x", stat.S_IFREG | 0o444)]
    variants["missing_member"] = entries[1:]
    variants["symlink"] = [(n, d, stat.S_IFLNK | 0o444 if i == 0 else m)
                           for i, (n, d, m) in enumerate(entries)]
    variants["writable"] = [(n, d, stat.S_IFREG | 0o644 if i == 0 else m)
                            for i, (n, d, m) in enumerate(entries)]
    variants["payload_digest"] = [(n, b"x"+d[1:] if i == 0 else d, m)
                                  for i, (n, d, m) in enumerate(entries)]
    # The duplicate constructor is intentionally explicit; no extraction occurs.
    variants["duplicate"] = entries + [entries[0]]
    for name, items in variants.items():
        blob = zip_blob(items)
        seal = seal_for(blob, manifest, inputs, len(items))
        try:
            verify_bytes(blob, seal)
        except (ValueError, zipfile.BadZipFile) as error:
            tests[name] = {"rejected": True, "reason": str(error)}
        else:
            raise AssertionError("vacuous verifier mutation: " + name)
    bad_seal = deepcopy(good_seal)
    bad_seal["archive_sha256"] = "0" * 64
    try:
        verify_bytes(original, bad_seal)
    except ValueError as error:
        tests["outer_digest"] = {"rejected": True, "reason": str(error)}
    else:
        raise AssertionError("outer digest mutation accepted")
    result = {
        "status": "PASS", "baseline": "accepted", "rejected_mutations": tests,
        "scope": "in-memory safety/byte verifier fixtures; final packet verified separately",
        "script_sha256": digest(Path(__file__).read_bytes()),
    }
    Path(__file__).with_name("VERIFIER_SELF_TEST_RESULT.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("PASS: valid exact-member fixture plus " + str(len(tests)) + " rejected mutations")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seal", type=Path)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        require(args.seal is None and args.workspace is None, "self-test arguments")
        self_test()
        return
    require(args.seal is not None, "--seal required")
    require(not args.seal.is_symlink() and args.seal.is_file(), "unsafe seal")
    require(args.seal.stat().st_size < 1024 * 1024, "seal size limit")
    seal = json_bytes(args.seal.read_bytes())
    filename = seal["archive_filename"]
    require(safe_name(filename) == Path(filename).name, "archive must be sibling basename")
    archive = args.seal.parent / filename
    require(archive.is_file() and not archive.is_symlink(), "unsafe archive")
    require(archive.stat().st_size <= MAX_ARCHIVE, "archive too large")
    payload = verify_bytes(archive.read_bytes(), seal)
    if args.workspace is not None:
        require(not (args.seal.stat().st_mode & 0o222), "writable seal")
        require(not (archive.stat().st_mode & 0o222), "writable archive")
        verify_workspace(payload, args.workspace)
    print(json.dumps({
        "status": "PASS", "members": len(payload), "inputs": 20,
        "archive_sha256": seal["archive_sha256"],
        "workspace_read_only_verified": args.workspace is not None,
        "extraction": "none",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
