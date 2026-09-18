#!/usr/bin/env python3
"""Read-only full original-byte and safe archive verification for AUD059."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import zipfile


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_name(name):
    require(bool(name) and "\\" not in name and "\x00" not in name, "Unsafe path text")
    p = PurePosixPath(name)
    require(not p.is_absolute() and p.as_posix() == name, "Noncanonical or absolute path")
    require(all(part not in ("", ".", "..") for part in name.split("/")), "Unsafe path part")
    return p


def read_manifest(path):
    result = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"Malformed manifest line in {path.name}")
        sha, name = match.groups()
        safe_name(name)
        require(name not in result, "Duplicate manifest path")
        result[name] = sha
    return result


def verify():
    packet = Path(__file__).resolve().parent
    base = packet.parent
    archive = base / (packet.name + ".zip")
    seal_path = base / (packet.name + ".SEAL.json")
    report = base / "ROUND_020_CONTINUOUS_PATH_RECONSTRUCTION.md"
    manifest = packet / "PACKET_SHA256SUMS.txt"
    control = packet / "CONTROL/ROUND_020_CONTINUOUS_PATH_BLIND_INPUT_SHA256SUMS.txt"
    seal = json.loads(seal_path.read_text())
    require(seal["audit"] == "AUD059" and seal["task"] == "TASK091", "Wrong seal identity")
    files = {}
    directories = [packet]
    for path in sorted(packet.rglob("*")):
        require(not path.is_symlink(), "Packet contains a symlink")
        if path.is_dir():
            directories.append(path)
        else:
            require(path.is_file() and stat.S_ISREG(path.stat().st_mode), "Nonregular packet member")
            relative = path.relative_to(packet).as_posix()
            safe_name(relative)
            files[relative] = path
    payload = read_manifest(manifest)
    require(set(payload) == set(files) - {"PACKET_SHA256SUMS.txt"}, "Incomplete payload manifest")
    for name, sha in payload.items():
        require(digest(files[name].read_bytes()) == sha, f"Payload hash mismatch: {name}")
    original_inputs = read_manifest(control)
    require(len(original_inputs) == 14, "Wrong original input count")
    for name, sha in original_inputs.items():
        p = packet / "INPUTS" / name
        require(p.is_file() and digest(p.read_bytes()) == sha, f"Input mismatch: {name}")
    copied_inputs = {name[len("INPUTS/"):] for name in files if name.startswith("INPUTS/")}
    require(copied_inputs == set(original_inputs), "Missing or extra input copy")
    require((packet / "PROOF.md").read_bytes() == report.read_bytes(), "Report copy differs")
    for key, path in (("report", report), ("archive", archive),
                      ("payload_manifest", manifest), ("input_manifest", control)):
        raw = path.read_bytes()
        require(digest(raw) == seal[key]["sha256"], f"Seal hash mismatch: {key}")
        require(len(raw) == seal[key]["bytes"], f"Seal size mismatch: {key}")
    require(len(files) == seal["packet_file_count"], "Packet count mismatch")
    require(sum(p.stat().st_size for p in files.values()) == seal["packet_bytes"], "Packet byte count mismatch")
    for path in list(files.values()) + directories + [report, archive, seal_path]:
        require((path.stat().st_mode & 0o222) == 0, f"Not read-only: {path}")

    expected_members = {f"{packet.name}/{name}": path for name, path in files.items()}
    with zipfile.ZipFile(archive, "r") as zf:
        infos = zf.infolist()
        require(len(infos) == len(expected_members), "ZIP count mismatch")
        require(len({info.filename for info in infos}) == len(infos), "Duplicate ZIP path")
        require({info.filename for info in infos} == set(expected_members), "Incomplete ZIP member set")
        total = 0
        for info in infos:
            safe_name(info.filename)
            mode = info.external_attr >> 16
            require(not info.is_dir() and stat.S_ISREG(mode), "ZIP member is not a regular file")
            require(not (info.flag_bits & 1), "Encrypted ZIP member")
            require(info.compress_type == zipfile.ZIP_STORED, "Unexpected ZIP compression")
            source = expected_members[info.filename].read_bytes()
            require(info.file_size == len(source) <= 10_000_000, "ZIP size mismatch or oversize")
            require(info.compress_size == info.file_size, "Stored ZIP size mismatch")
            total += info.file_size
            require(total <= 100_000_000, "ZIP total size limit")
            member = zf.read(info)  # CRC is checked by ZipFile.
            require(member == source, f"ZIP byte mismatch: {info.filename}")
            require(digest(member) == digest(source), "ZIP SHA mismatch")
        require(total == seal["packet_bytes"], "ZIP total differs")

    script = packet / "diagnostics/continuous_path_diagnostic.py"
    result = packet / "diagnostics/results.json"
    checked = subprocess.run([sys.executable, str(script), "--verify", str(result)],
                             capture_output=True, text=True, check=True)
    diagnostic = json.loads(checked.stdout)
    require(diagnostic["status"] == "PASS", "Diagnostic failed")
    require(diagnostic["assertion_count"] == 2508 and diagnostic["mutations_rejected"] == 13,
            "Unexpected diagnostic coverage")
    return {
        "status": "PASS", "audit": "AUD059", "input_files": len(original_inputs),
        "packet_files": len(files), "packet_bytes": seal["packet_bytes"],
        "safe_complete_zip_byte_verification": True, "read_only_modes": True,
        "diagnostic_assertions": diagnostic["assertion_count"],
        "mutations_rejected": diagnostic["mutations_rejected"],
        "report_sha256": digest(report.read_bytes()),
        "archive_sha256": digest(archive.read_bytes()),
        "seal_sha256": digest(seal_path.read_bytes()),
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
