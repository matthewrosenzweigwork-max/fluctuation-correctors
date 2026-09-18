#!/usr/bin/env python3
"""Read-only complete byte/membership verification of the issued TASK090 packet.

No archive extraction is performed. Input and output lists must account for
every packet file. Archive members must be regular files at exactly those safe
relative names, without duplicate entries, with identical lengths and bytes.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(name):
    if not name or "\\" in name or "\x00" in name:
        raise ValueError("Unsafe member name: " + repr(name))
    p = PurePosixPath(name)
    if p.is_absolute() or any(part in ("", ".", "..") for part in name.split("/")):
        raise ValueError("Unsafe relative path: " + repr(name))
    return p


def read_manifest(path):
    out = {}
    for line in path.read_text().splitlines():
        d, name = line.split("  ", 1)
        safe_relative(name)
        if len(d) != 64 or any(c not in "0123456789abcdef" for c in d) or name in out:
            raise ValueError("Malformed or duplicate manifest record")
        out[name] = d
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--memo", type=Path)
    parser.add_argument("--rerun-diagnostic", action="store_true")
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    input_map = read_manifest(packet / "INPUT_SHA256SUMS.txt")
    output_map = read_manifest(packet / "OUTPUT_SHA256SUMS.txt")
    if len(input_map) != 14:
        raise ValueError("Expected exactly fourteen frozen inputs")
    expected = {"INPUTS/" + rel: d for rel, d in input_map.items()}
    for rel, d in output_map.items():
        if rel in expected or rel == "OUTPUT_SHA256SUMS.txt":
            raise ValueError("Overlapping or self-referential manifest entry")
        expected[rel] = d
    expected["OUTPUT_SHA256SUMS.txt"] = digest((packet / "OUTPUT_SHA256SUMS.txt").read_bytes())

    actual = {}
    for p in packet.rglob("*"):
        if p.is_symlink():
            raise ValueError("Packet symlink is forbidden: " + str(p))
        if p.is_file():
            rel = p.relative_to(packet).as_posix()
            safe_relative(rel)
            actual[rel] = p.read_bytes()
        elif not p.is_dir():
            raise ValueError("Special packet file is forbidden: " + str(p))
    if set(actual) != set(expected):
        raise ValueError("Packet membership mismatch: " + repr({
            "missing": sorted(set(expected) - set(actual)),
            "extra": sorted(set(actual) - set(expected))}))
    for rel, data in actual.items():
        if digest(data) != expected[rel]:
            raise ValueError("Packet hash mismatch: " + rel)

    result = {
        "status": "PASS", "packet_files": len(actual), "frozen_inputs": len(input_map),
        "manifested_outputs": len(output_map), "packet_bytes": sum(map(len, actual.values())),
        "input_manifest_sha256": digest((packet / "INPUT_SHA256SUMS.txt").read_bytes()),
        "output_manifest_sha256": expected["OUTPUT_SHA256SUMS.txt"],
        "all_packet_files_read_only": all((packet / rel).stat().st_mode & 0o222 == 0 for rel in actual),
    }
    diagnostic = json.loads(actual["round020_path_diagnostic_results.json"])
    if diagnostic["program_sha256"] != digest(actual["round020_path_diagnostic.py"]):
        raise ValueError("Diagnostic result does not match the included program bytes")
    if diagnostic["status"] != "PASS" or diagnostic["assertions"] != 4255:
        raise ValueError("Unexpected diagnostic outcome")
    if args.rerun_diagnostic:
        rerun = subprocess.run([sys.executable, str(packet / "round020_path_diagnostic.py")],
                               check=True, capture_output=True, timeout=30)
        if rerun.stdout != actual["round020_path_diagnostic_results.json"]:
            raise ValueError("Fresh diagnostic output differs byte-for-byte")
        result["diagnostic_rerun"] = "PASS / exact output byte match"
    if args.memo:
        memo_bytes = args.memo.read_bytes()
        if memo_bytes != actual["PROOF/ROUND_020_CONTINUOUS_PATH_GAUSSIAN.md"]:
            raise ValueError("Sibling memorandum differs from packet proof")
        result["sibling_memo_sha256"] = digest(memo_bytes)
        result["sibling_memo_read_only"] = args.memo.stat().st_mode & 0o222 == 0
    if args.archive:
        prefix = packet.name + "/"
        expected_zip = {prefix + rel: data for rel, data in actual.items()}
        with zipfile.ZipFile(args.archive) as z:
            infos = z.infolist()
            names = [i.filename for i in infos]
            if len(names) != len(set(names)) or set(names) != set(expected_zip):
                raise ValueError("Archive duplicate or membership mismatch")
            for info in infos:
                safe_relative(info.filename)
                mode = info.external_attr >> 16
                if info.is_dir() or not stat.S_ISREG(mode) or info.flag_bits & 1:
                    raise ValueError("Archive contains a directory, nonregular, or encrypted member")
                data = expected_zip[info.filename]
                if info.file_size != len(data):
                    raise ValueError("Archive declared length mismatch")
                with z.open(info) as stream:
                    archived = stream.read(len(data) + 1)
                if archived != data:
                    raise ValueError("Archive byte mismatch: " + info.filename)
                if digest(archived) != expected[info.filename[len(prefix):]]:
                    raise ValueError("Archive digest mismatch: " + info.filename)
        result["archive_members"] = len(expected_zip)
        result["archive_sha256"] = digest(args.archive.read_bytes())
        result["archive_read_only"] = args.archive.stat().st_mode & 0o222 == 0
        result["archive_safety"] = "PASS / exact safe regular-file membership, lengths, CRC reads, bytes and SHA256; no extraction"
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
