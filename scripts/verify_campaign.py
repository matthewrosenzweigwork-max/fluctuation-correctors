#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "README_FIRST.md",
    "AGENTS.md",
    "MASTER_PROMPT.md",
    "CAMPAIGN_PROTOCOLS.md",
    "MODEL_ORCHESTRATION.md",
    "KICKOFF_PROMPT_ULTRA.md",
    "PLANS.md",
    "INPUTS/note_v2.pdf",
    "INPUTS/SOURCE_MANIFEST.md",
    "BASELINE/INITIAL_MATHEMATICAL_STATE.md",
    "BASELINE/INITIAL_CRITICAL_ASSESSMENT.md",
    "STATE/CAMPAIGN_STATE.md",
    "STATE/STATUS_VOCABULARY.md",
    "STATE/THEOREM_LEDGER.md",
    "STATE/PROOF_OBLIGATION_LEDGER.md",
    "STATE/NORMALIZATION_AND_SCALING_LEDGER.md",
    "STATE/CORRECTOR_LEDGER.md",
    "STATE/COUNTERTERM_AND_CONTRACTION_LEDGER.md",
    "STATE/ASSUMPTIONS_AND_CONSTANTS_LEDGER.md",
    "STATE/BIAS_AND_CENTERING_LEDGER.md",
    "STATE/OPERATOR_AND_SEMIGROUP_LEDGER.md",
    "STATE/DIAGRAM_AND_POWER_COUNTING_LEDGER.md",
    "STATE/MARTINGALE_AND_QUADRATIC_VARIATION_LEDGER.md",
    "STATE/STATIC_DYNAMIC_INTERFACE_LEDGER.md",
    "APPROACHES/ROUTE_REGISTRY.md",
    "APPROACHES/OBSTRUCTION_LEDGER.md",
]
failures = []
for rel in required:
    p = root / rel
    if not p.is_file():
        failures.append(f"missing required file: {rel}")

note = root / "INPUTS/note_v2.pdf"
expected_note = "a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76"
if note.is_file():
    actual = hashlib.sha256(note.read_bytes()).hexdigest()
    if actual != expected_note:
        failures.append(f"source note hash mismatch: expected {expected_note}, got {actual}")

manifest = root / "SHA256SUMS.txt"
if not manifest.is_file():
    failures.append("missing SHA256SUMS.txt")
else:
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        expected, rel = raw.split("  ", 1)
        p = root / rel
        if not p.is_file():
            failures.append(f"manifest file missing: {rel}")
            continue
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != expected:
            failures.append(f"manifest hash mismatch: {rel}")

# Guard central scaling strings against accidental corruption.
master = (root / "MASTER_PROMPT.md").read_text(encoding="utf-8") if (root / "MASTER_PROMPT.md").is_file() else ""
for token in [
    r"\lambda_N:=\beta_NN^{s/d-1}",
    r"\beta_NN^{2s/d-1}",
    "Do not assume the answer",
    "critical power counting",
]:
    if token not in master:
        failures.append(f"master prompt guard missing: {token}")

if failures:
    print("CAMPAIGN VERIFICATION FAILED", file=sys.stderr)
    for f in failures:
        print(f"- {f}", file=sys.stderr)
    raise SystemExit(1)

print("CAMPAIGN VERIFICATION PASSED")
print(f"Repository root: {root}")
print(f"Imported note SHA-256: {expected_note}")
