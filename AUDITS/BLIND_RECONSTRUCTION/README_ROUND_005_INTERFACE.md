# TASK043 sealed interface reconstruction

This packet is a statement-only reconstruction of THM025's module composition, actual homogeneous reference/test, and initial iid endpoint. The disposition is PASS conditional on the analytic modules explicitly accepted in the assigned task. It does not independently certify the undisclosed THM021/THM023 proofs or a dynamic fluctuation theorem.

Main report: `ROUND_005_INTERFACE_RECONSTRUCTION.md`.

Reproduce the exact checks from the isolated worktree root:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/round005_interface_checks.py
shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt
```

The checker returns PASS with 2,672 exact assertions. It uses Python's standard library only and writes `ROUND_005_INTERFACE_CHECK_RESULTS.json`. Its checks include all eight frozen input digests, exact iid enumeration, both response slots, inhomogeneous density terms, pair exchange, the internal `1/N`, Fourier source and backward signs, normalization recurrences, and temperature/endpoint powers.

From the audit output directory, verify the issued output packet:

```text
shasum -a 256 -c ROUND_005_INTERFACE_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c ROUND_005_INTERFACE_SEAL_SHA256SUMS.txt
```

The ZIP contains the eight frozen source files at their original relative paths, and the report, checker, recorded results, README, and input/output manifests in `AUDITS/BLIND_RECONSTRUCTION/`. The ZIP excludes its own seal manifest. The seal manifest hashes the ZIP and the output manifest. The seal binds the recorded results; rerunning under another Python version may alter the recorded Python version, so verify the original packet before reproducing in a separate extracted copy.

Read boundary: only the assigned task and seven other listed input files were read. No root proof, other audit, state/history document, memory, dependency installation, commit, push, or child-agent delegation was used. No root files or canonical state were edited. All generated artifacts are local to this isolated worktree's assigned audit output directory.
