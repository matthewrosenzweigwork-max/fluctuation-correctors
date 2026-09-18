#!/usr/bin/env python3
"""Read-only verification of the issued AUD055 packet, without extracting ZIPs."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

EXPECTED_INPUTS = {
    "AGENTS.md": "cc3a478358f1fcb3ccf472615c715acfdef575d9a80b5aa49417593a25825ed3",
    "TASKS/ACTIVE/ROUND_001_MODEL.md": "3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57",
    "MEMORANDA/ROUND_001_ALGEBRA.md": "e5db5923ba82bf929218e23fe641ed5a7387c106220e6374f37bd06b80c3e4de",
    "MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md": "135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be",
    "THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md": "aaaec9f6e10be3b5b6e82473ce11a441ad67c6c9b03c17254c144270e0103c7a",
    "MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md": "d4d1eae9f18d5796e8e99aa4b5e364b39321167f48eb27fa764bc7e327272017",
    "MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md": "f8d0b7a47d1cf7456dc3e877f3e6cb0b3396fa0ad8a184b650de9afc1cb97d1b",
    "THEOREMS/THM-031_ACTUAL_FOURIER_SMOOTHING_AND_TAIL.md": "2b8ffeae89b33742353c06e9e975b726f4b705ab7f1ef2bb8d830675d6195ba4",
    "THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md": "257260a31d299f2d22d38deb0aea4add7b183b739d83d1031705d5d31f9982cb",
    "MEMORANDA/ROUND_016_SOURCE_EXTENSION.md": "62fc121556fa2cb08f0ec3e2c7d1813f40bce6a86a2f5ea07ed2d616c6ce9a26",
    "THEOREMS/THM-040_BOUNDED_DIFFUSIVITY_FINITE_DIMENSIONAL_GAUSSIAN.md": "eda23360683cb9545d4d0fe7bcc8c32e36ca6aa6e670c6bcf38609317332efdc",
    "TASKS/ACTIVE/TASK-085_ROUND018_BOUNDED_NOISE_GAUSSIAN_BLIND.md": "7681e1068ceaebf382a33ffa7f8097bd8e4165b9242f9429dbc4a892ff7a9727",
}
REPORT = "ROUND_018_BOUNDED_NOISE_RECONSTRUCTION.md"
ARTIFACTS = "ROUND_018_BOUNDED_NOISE_BLIND_ARTIFACTS"
PREFIX = "AUD055_ROUND018_BOUNDED_NOISE/"
ARCHIVE = "AUD055_ROUND018_BOUNDED_NOISE_IMMUTABLE.zip"


def safe_relative(name: str) -> PurePosixPath:
    assert name and "\\" not in name and "\x00" not in name, name
    assert all(p not in ("", ".", "..") for p in name.split("/")), name
    path = PurePosixPath(name)
    assert not path.is_absolute() and str(path) == name, name
    return path


def regular_file(base: Path, name: str) -> Path:
    rel = safe_relative(name)
    current = base
    for component in rel.parts:
        current = current / component
        assert not current.is_symlink(), current
    assert stat.S_ISREG(current.stat().st_mode), current
    return current


def read_manifest(path: Path):
    result = {}
    for line in path.read_text().splitlines():
        digest, name = line.split("  ", 1)
        assert len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
        safe_relative(name)
        assert name not in result
        result[name] = digest
    assert result
    return result


def digest(path: Path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    here = Path(__file__).resolve().parent
    base = here.parent
    assert here.name == ARTIFACTS
    for p in here.rglob("*"):
        assert not p.is_symlink(), ("symlink in packet", str(p))
        assert p.is_file() or p.is_dir(), ("nonregular packet entry", str(p))
    input_manifest = regular_file(here, "INPUT_SHA256SUMS.txt")
    inputs = read_manifest(input_manifest)
    assert inputs == EXPECTED_INPUTS
    for name, expected in inputs.items():
        assert digest(regular_file(here / "INPUTS", name)) == expected, name
    actual_inputs = {p.relative_to(here / "INPUTS").as_posix()
                     for p in (here / "INPUTS").rglob("*") if p.is_file()}
    assert actual_inputs == set(inputs)

    output_manifest = regular_file(here, "OUTPUT_SHA256SUMS.txt")
    outputs = read_manifest(output_manifest)
    mandatory = {REPORT} | {ARTIFACTS+"/"+p for p in (
        "README.md", "EXPOSURE.json", "INPUT_SHA256SUMS.txt", "ARCHIVE_MEMBERS.txt",
        "round018_exact_diagnostic.py", "round018_exact_diagnostic_output.json",
        "verify_sealed_packet.py")}
    mandatory |= {ARTIFACTS+"/INPUTS/"+p for p in inputs}
    assert set(outputs) == mandatory, set(outputs) ^ mandatory
    readonly = []
    for name, expected in outputs.items():
        p = regular_file(base, name)
        assert digest(p) == expected, name
        readonly.append(p)

    diagnostic = json.loads((here / "round018_exact_diagnostic_output.json").read_text())
    assert diagnostic["status"] == "PASS"
    assert diagnostic["assertions"] == 4575
    assert diagnostic["mutation_rejections"] == 2172
    assert len(diagnostic["categories"]) == 36
    assert len(diagnostic["mutation_categories"]) == 17
    assert diagnostic["script_sha256"] == digest(here / "round018_exact_diagnostic.py")

    members_file = regular_file(here, "ARCHIVE_MEMBERS.txt")
    members = members_file.read_text().splitlines()
    expected_members = sorted(PREFIX+name for name in sorted(outputs))
    expected_members.append(PREFIX+ARTIFACTS+"/OUTPUT_SHA256SUMS.txt")
    expected_members.sort()
    assert members == expected_members
    assert len(members) == len(set(members))
    for name in members:
        safe_relative(name)

    archive_seal = regular_file(here, "ARCHIVE_SHA256SUMS.txt")
    seal = read_manifest(archive_seal)
    assert set(seal) == {ARCHIVE}
    archive = regular_file(here, ARCHIVE)
    assert digest(archive) == seal[ARCHIVE]
    total_size = 0
    with zipfile.ZipFile(archive) as zf:
        infos = zf.infolist()
        assert [z.filename for z in infos] == members
        for info in infos:
            safe_relative(info.filename)
            assert info.filename.startswith(PREFIX)
            assert not info.is_dir()
            assert stat.S_IFMT(info.external_attr >> 16) == stat.S_IFREG
            assert not ((info.external_attr >> 16) & 0o222)
            assert not (info.flag_bits & 1), "encrypted archive entry"
            assert info.file_size <= 8_000_000
            assert info.file_size <= 2000*max(1, info.compress_size)
            total_size += info.file_size
            assert total_size < 32_000_000
            local_name = info.filename[len(PREFIX):]
            local = regular_file(base, local_name)
            assert zf.read(info.filename) == local.read_bytes(), info.filename
        assert zf.testzip() is None
    assert total_size < 32_000_000

    readonly += [output_manifest, archive_seal, archive]
    for p in readonly:
        assert not (p.stat().st_mode & 0o222), ("writable issued file", str(p))
    # The report directory may contain unrelated inherited audits. Only this
    # packet directory is inventoried, and every file in it must be declared.
    declared_local = {p for p in outputs if p.startswith(ARTIFACTS+"/")}
    declared_local |= {ARTIFACTS+"/OUTPUT_SHA256SUMS.txt",
                       ARTIFACTS+"/ARCHIVE_SHA256SUMS.txt", ARTIFACTS+"/"+ARCHIVE}
    actual_local = {p.relative_to(base).as_posix() for p in here.rglob("*") if p.is_file()}
    assert actual_local == declared_local, actual_local ^ declared_local
    print(json.dumps({"status": "PASS", "audit": "AUD055", "inputs": len(inputs),
                      "payload_files": len(outputs), "archive_members": len(members),
                      "archive_uncompressed_bytes": total_size,
                      "archive_sha256": seal[ARCHIVE],
                      "report_sha256": outputs[REPORT],
                      "readonly_files_checked": len(readonly)}, sort_keys=True))


if __name__ == "__main__":
    main()
