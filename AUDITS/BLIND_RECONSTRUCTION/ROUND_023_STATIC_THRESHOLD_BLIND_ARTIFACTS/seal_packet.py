#!/usr/bin/env python3
"""Build and verify the bounded AUD065 handoff without archive extraction."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import io
import json
import os
import stat
import tarfile

WORK = Path("/Users/matthewrosenzweig/.codex/worktrees/hocf-r023-static-threshold-blind")
BASE = WORK / "AUDITS/BLIND_RECONSTRUCTION"
ART = BASE / "ROUND_023_STATIC_THRESHOLD_BLIND_ARTIFACTS"
REPORT = BASE / "ROUND_023_STATIC_THRESHOLD_RECONSTRUCTION.md"
ARCHIVE = BASE / "ROUND_023_STATIC_THRESHOLD_BLIND_HANDOFF_20260918_075328_UTC.tar.gz"
POST = {
    "OUTPUT_SHA256SUMS.txt",
    "ARCHIVE_MEMBER_SHA256SUMS.txt",
    "ARCHIVE_SHA256SUMS.txt",
    "SEAL_VERIFICATION.json",
    "SEAL_SHA256SUMS.txt",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def line_for(path, data=None):
    return digest(path.read_bytes() if data is None else data) + "  " + path.relative_to(BASE).as_posix()


def check(condition, label):
    if not condition:
        raise RuntimeError(label)


def main():
    check(not ARCHIVE.exists(), "Do not replace a previously issued archive.")
    for name in POST:
        check(not (ART/name).exists(), "Do not replace a previously issued seal.")
    rows = [line.split("  ", 1) for line in
            (ART/"INPUT_SHA256SUMS.txt").read_text().splitlines() if line.strip()]
    check(len(rows) == 8 and len({name for _, name in rows}) == 8,
          "Exactly eight unique inputs required.")
    input_records = []
    for expected, name in rows:
        rel = PurePosixPath(name)
        check(not rel.is_absolute() and ".." not in rel.parts, "Unsafe input path.")
        source = WORK/name
        check(source.is_file() and not source.is_symlink(), "Input is not a regular file.")
        data = source.read_bytes()
        check(digest(data) == expected, "Input changed: " + name)
        target = ART/"inputs"/name
        target.parent.mkdir(parents=True, exist_ok=True)
        check(not target.exists(), "Do not replace an existing input snapshot.")
        target.write_bytes(data)
        check(target.read_bytes() == data, "Snapshot differs: " + name)
        input_records.append({"path": name, "sha256": expected, "bytes": len(data)})

    results = json.loads((ART/"results_v2.json").read_text())
    check(results["script_sha256"] == digest((ART/"diagnostic_v2.py").read_bytes()),
          "Final diagnostic/result bytes differ.")
    check(results["exact"]["status"] == "PASS", "Exact diagnostic did not pass.")
    check(results["exact"]["exact_assertions"] == 230, "Exact check count differs.")
    check(len(results["exact"]["mutations"]) == 8 and
          all(r["detected"] for r in results["exact"]["mutations"].values()),
          "Mutation suite did not detect all cases.")
    check(results["approximate"]["status"] == "PASS_SUPPORTING_ONLY",
          "Final supporting probe did not pass.")
    check(results["approximate"]["rows"][-1]["m"] == 192, "Wrong final numerical row.")

    payload = [REPORT] + sorted(
        p for p in ART.rglob("*") if p.is_file() and p.name not in POST
    )
    check(all(not p.is_symlink() for p in payload), "Payload contains a symlink.")
    check(len(payload) == len(set(payload)), "Duplicate payload path.")
    output_manifest = ART/"OUTPUT_SHA256SUMS.txt"
    output_manifest.write_text("\n".join(line_for(p) for p in payload)+"\n")
    payload.append(output_manifest)
    expected_members = {
        p.relative_to(BASE).as_posix(): p.read_bytes() for p in payload
    }

    with ARCHIVE.open("xb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.USTAR_FORMAT) as tar:
                for name, data in sorted(expected_members.items()):
                    info = tarfile.TarInfo(name)
                    info.size = len(data)
                    info.mode = 0o444
                    info.mtime = 0
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    tar.addfile(info, io.BytesIO(data))

    actual_members = {}
    with tarfile.open(ARCHIVE, "r:gz") as tar:
        for member in tar.getmembers():
            rel = PurePosixPath(member.name)
            check(not rel.is_absolute() and ".." not in rel.parts and
                  "\\" not in member.name and rel.as_posix() == member.name,
                  "Unsafe archive path.")
            check(member.isfile() and not member.issym() and not member.islnk(),
                  "Nonregular archive member.")
            check(member.name not in actual_members, "Duplicate archive member.")
            check(member.mode == 0o444, "Archive member is writable.")
            check(member.name in expected_members, "Unexpected archive member.")
            stream = tar.extractfile(member)  # Reads bytes; never extracts to the filesystem.
            check(stream is not None, "Unreadable member.")
            data = stream.read()
            check(data == expected_members[member.name], "Member bytes differ.")
            check(member.size == len(data), "Member size differs.")
            actual_members[member.name] = data
    check(set(actual_members) == set(expected_members), "Missing archive members.")
    member_manifest = ART/"ARCHIVE_MEMBER_SHA256SUMS.txt"
    member_manifest.write_text("\n".join(
        digest(data)+"  "+name for name, data in sorted(actual_members.items())
    )+"\n")
    archive_digest = digest(ARCHIVE.read_bytes())
    archive_manifest = ART/"ARCHIVE_SHA256SUMS.txt"
    archive_manifest.write_text(archive_digest+"  "+ARCHIVE.name+"\n")

    # Verify the archived output manifest, not merely the source copy.
    archived_manifest = actual_members[output_manifest.relative_to(BASE).as_posix()]
    for row in archived_manifest.decode().splitlines():
        expected, name = row.split("  ", 1)
        check(name in actual_members and digest(actual_members[name]) == expected,
              "Archived output manifest mismatch.")
    for expected, name in rows:
        key = (ART.relative_to(BASE)/"inputs"/name).as_posix()
        check(digest(actual_members[key]) == expected, "Archived input mismatch.")

    verification = {
        "audit": "AUD065", "task": "TASK100",
        "base": "64ac0538dff37a37d0883661b401ad04c311a5e5",
        "archive": ARCHIVE.name, "archive_sha256": archive_digest,
        "archive_bytes": ARCHIVE.stat().st_size,
        "members": len(actual_members),
        "all_members_regular_safe_unique": True,
        "all_member_bytes_compared_without_extraction": True,
        "all_eight_inputs_exact": True,
        "archived_output_manifest_verified": True,
        "exact_diagnostic_assertions": 230,
        "detecting_mutations": 8,
        "final_diagnostic_script_and_result_match": True,
        "inputs": input_records,
        "manifest_self_exclusions": [
            "OUTPUT_SHA256SUMS.txt excludes its own digest; the member manifest covers it.",
            "Archive member/digest/verification/seal sidecars are external to the archive.",
            "SEAL_SHA256SUMS.txt excludes its own digest to avoid a recursive hash.",
        ],
        "permissions_on_success": "All issued files 0444; artifact directories 0555.",
        "corrections": "Any post-issuance correction must be a new artifact.",
        "epistemic_scope": "Reconstructed whole claim; root comparison and separate hostile gate pending.",
    }
    verification_path = ART/"SEAL_VERIFICATION.json"
    verification_path.write_text(json.dumps(verification, indent=2, sort_keys=True)+"\n")
    seal_manifest = ART/"SEAL_SHA256SUMS.txt"
    seal_manifest.write_text("\n".join(line_for(p) for p in [
        ARCHIVE, member_manifest, archive_manifest, verification_path
    ])+"\n")

    issued = [REPORT, ARCHIVE] + [p for p in ART.rglob("*") if p.is_file()]
    for path in issued:
        path.chmod(0o444)
    for path in sorted((p for p in ART.rglob("*") if p.is_dir()),
                       key=lambda p: len(p.parts), reverse=True):
        path.chmod(0o555)
    ART.chmod(0o555)
    check(all(stat.S_IMODE(p.stat().st_mode) == 0o444 for p in issued),
          "Issued files were not frozen.")
    check(all(stat.S_IMODE(p.stat().st_mode) == 0o555
              for p in [ART]+[q for q in ART.rglob("*") if q.is_dir()]),
          "Artifact directories were not frozen.")
    for row in seal_manifest.read_text().splitlines():
        expected, name = row.split("  ", 1)
        check(digest((BASE/name).read_bytes()) == expected, "Final seal sidecar mismatch.")
    print(json.dumps({
        "status": "SEALED_VERIFIED_READ_ONLY",
        "archive": str(ARCHIVE), "archive_sha256": archive_digest,
        "archive_bytes": ARCHIVE.stat().st_size,
        "verified_members": len(actual_members), "exact_inputs": 8,
        "issued_readonly_files": len(issued),
        "report_sha256": digest(REPORT.read_bytes()),
        "no_extraction": True,
    }, indent=2))


if __name__ == "__main__":
    main()
