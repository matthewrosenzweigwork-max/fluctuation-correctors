#!/usr/bin/env python3
"""Preserve the imported baseline while verifying documented mutable state.

DEC-005 defines the only entries whose working checksums may be refreshed.
This never modifies the shipped verifier or the frozen baseline manifest.
"""
import argparse
import hashlib
from pathlib import Path
import subprocess

BASELINE = "475a5399828bc6e2ccbade08c59b8778638df14a"
ROOT = Path(__file__).resolve().parents[1]


def mutable(path):
    return ((path.startswith("STATE/") and path != "STATE/STATUS_VOCABULARY.md")
            or path.startswith("APPROACHES/") or path == "TASKS/QUEUE.md")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh-mutable", action="store_true")
    args = parser.parse_args()
    original = subprocess.check_output(
        ["git", "show", BASELINE + ":SHA256SUMS.txt"], cwd=ROOT)
    saved = ROOT / "REPORTS/INSTALLATION/OVERLAY_SHA256SUMS_BASELINE.txt"
    if saved.read_bytes() != original:
        raise SystemExit("FAIL: preserved overlay manifest differs from baseline")
    refreshed = []
    changed = []
    immutable_count = 0
    for line in original.decode().splitlines():
        expected, rel = line.split("  ", 1)
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit("FAIL: missing baseline path " + rel)
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if not mutable(rel):
            immutable_count += 1
            if actual != expected:
                raise SystemExit("FAIL: protected baseline changed: " + rel)
        elif actual != expected:
            changed.append(rel)
        refreshed.append(actual + "  " + rel)
    if args.refresh_mutable:
        (ROOT / "SHA256SUMS.txt").write_text("\n".join(refreshed) + "\n")
    print("PROTECTED BASELINE PASS:", immutable_count, "immutable entries")
    print("Documented mutable paths differing from baseline:", len(changed))
    for rel in changed:
        print("  " + rel)
    subprocess.run(["python3", "scripts/verify_campaign.py"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
