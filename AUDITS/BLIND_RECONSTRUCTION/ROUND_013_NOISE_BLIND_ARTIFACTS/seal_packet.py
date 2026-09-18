#!/usr/bin/env python3
"""Seal TASK-071 exactly once, with an allowlisted archive and no circular hash."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    rel = here.relative_to(root)
    report = Path("AUDITS/BLIND_RECONSTRUCTION/ROUND_013_BOUNDED_NOISE_RECONSTRUCTION.md")
    output_names = [report] + [rel / name for name in (
        "round013_noise_blind_exact.py", "EXACT_RESULT.json", "README.md", "EXPOSURE.md",
        "INPUT_SHA256SUMS.txt", "INPUT_VERIFICATION.json", "seal_packet.py")]
    manifest = here / "OUTPUT_SHA256SUMS.txt"
    archive = here / "ROUND_013_NOISE_BLIND_SEALED.zip"
    verification = here / "PACKET_VERIFICATION.json"
    final_seal = here / "FINAL_SHA256SUMS.txt"
    for target in (manifest, archive, verification, final_seal):
        if target.exists():
            raise RuntimeError(f"Refusing to replace issued package record: {target.name}")
    expected_base = "29d7ce427ad7a98739b18d07781e71c4598b3579"
    expected_branch = "codex/hocf-r013-noise-blind"
    observed_base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    observed_branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=root, text=True).strip()
    assert observed_base == expected_base
    assert observed_branch == expected_branch
    input_rows = []
    for line in (here / "INPUT_SHA256SUMS.txt").read_text().splitlines():
        expected, name = line.split("  ", 1)
        assert digest(root / name) == expected, name
        input_rows.append((expected, Path(name)))
    assert len(input_rows) == 27
    result = json.loads((here / "EXACT_RESULT.json").read_text())
    assert result["status"] == "PASS" and result["assertions"] == 2513
    assert result["checker_sha256"] == digest(here / "round013_noise_blind_exact.py")
    output_rows = [(digest(root / name), name) for name in output_names]
    manifest.write_text("".join(f"{sha}  {name.as_posix()}\n" for sha, name in output_rows))
    members = [name for _, name in input_rows] + output_names + [manifest.relative_to(root)]
    assert len(members) == len(set(members))
    expected_digests = {name.as_posix(): digest(root / name) for name in members}
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for name in sorted(members, key=lambda p: p.as_posix()):
            package.write(root / name, arcname=name.as_posix())
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None
        assert sorted(package.namelist()) == sorted(expected_digests)
        for name, expected in expected_digests.items():
            assert hashlib.sha256(package.read(name)).hexdigest() == expected, name
            assert not Path(name).is_absolute() and ".." not in Path(name).parts
    for expected, name in input_rows + output_rows:
        assert digest(root / name) == expected, name
    verification_data = {
        "status": "PASS",
        "sealed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "worktree": str(root), "base": observed_base, "branch": observed_branch,
        "candidate_comparison_before_seal": False,
        "input_count": 27, "output_count_excluding_manifest": len(output_names),
        "archive_member_count": len(members), "archive_crc_verified": True,
        "archive_member_set_exact": True, "all_member_sha256_verified": True,
        "inputs_reverified_after_archiving": True, "outputs_reverified_after_archiving": True,
        "exact_assertions": result["assertions"],
        "report_sha256": digest(root / report),
        "output_manifest_sha256": digest(manifest), "archive_sha256": digest(archive),
        "members": expected_digests,
    }
    verification.write_text(json.dumps(verification_data, indent=2, sort_keys=True) + "\n")
    final_records = [(digest(path), path.relative_to(root)) for path in (manifest, archive, verification)]
    final_seal.write_text("".join(f"{sha}  {name.as_posix()}\n" for sha, name in final_records))
    for expected, name in final_records:
        assert digest(root / name) == expected
    for path in [root / name for name in output_names] + [manifest, archive, verification, final_seal]:
        path.chmod(0o444)
    print(json.dumps({"status": "PASS", "input_count": 27, "archive_member_count": len(members),
                      "report_sha256": verification_data["report_sha256"],
                      "archive_sha256": verification_data["archive_sha256"],
                      "final_seal": str(final_seal)}, indent=2))


if __name__ == "__main__":
    main()
