# TASK-056 sealed reconstruction packet

Issued 20260918_022218_UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r009-energy-blind`. Branch: `codex/hocf-r009-energy-blind`. Base HEAD: `4171be9839feb8acf4c70e1dda014458fdb44490`.

Verdict: THM029 is proved conditional on the complete provisional THM028 domain and the supplied earlier pair/particle modules. This is a fresh statement-only reconstruction of the new assertion; a separate hostile audit remains required. The R8 proof itself was not audited. All nineteen allowlisted inputs were verified and copied. No withheld R9 construction, seed or checker was read, and no root edits, commits, pushes, dependency installations or child agents were used.

The report supplies the uniform energy proof, including the Coulomb collision-tube passage without a trace; all exact finite-label and physical noise coefficients; timewise and time-integrated reference bounds; the exact two-/three-marginal law discrepancies; and the symmetry proof for the actual particle law. The actual-law discrepancy bounds remain open. The uniform L1 time-derivative argument is derived from the earlier source's singular measure domination; the allowed R8 time-differentiation identity is explicitly attributed, without importing its N-dependent constants.

Files:

- `ROUND_009_ENERGY_RECONSTRUCTION.md`: complete proof, source/exposure boundary, per-claim verdicts and remaining unsupported line.
- `round009_energy_exact_checks.py`: fresh exact standard-library checker, independent of the withheld R9 checker.
- `round009_energy_exact_results.json`: PASS, 4,994 exact assertions. These support algebra and do not replace analytic proof or independent audit.
- `ROUND_009_INPUTS/`: exactly nineteen copied permitted files.
- `ROUND_009_ENERGY_BLIND_INPUT_SHA256SUMS.txt`: original nineteen-file input manifest.
- `ROUND_009_COPIED_INPUT_SHA256SUMS.txt`: hashes with local copied-input paths.
- `ROUND_009_OUTPUT_SHA256SUMS.txt`: output hashes; excludes itself.
- `ROUND_009_ENERGY_RECONSTRUCTION_20260918_022218_UTC.zip`: report/checker/results/README/manifests and all nineteen inputs, with no other inherited files.
- `ROUND_009_PACKET_SEAL_SHA256SUMS.txt`: hashes of the archive and output manifest.

Reproduce the algebra checks from the worktree:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/round009_energy_exact_checks.py
```

Check the manifests from this packet directory:

```text
shasum -a 256 -c ROUND_009_COPIED_INPUT_SHA256SUMS.txt
shasum -a 256 -c ROUND_009_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c ROUND_009_PACKET_SEAL_SHA256SUMS.txt
```

Verification at issuance: all input hashes, 4,994 exact assertions, all output hashes, ZIP CRC, exact archive member set, member-by-member SHA-256 comparison, and prescribed base/branch checks passed. The checker is deterministic and uses no random seed or tolerance. Its Laurent-polynomial convention and restored physical factors are recorded in the report and JSON.

The report is immutable after issuance. Root comparison with the withheld constructor and any further audit occur after this seal. Any correction must be a separately named report, with a new seal. No canonical state has been changed by this worker.
