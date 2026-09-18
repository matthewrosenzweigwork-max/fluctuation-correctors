# AUD057 / TASK088 sealed reconstruction packet

The accompanying report reconstructs the entire frozen two-part THM041 assertion, without narrowing its all-finite-diffusivity supremum or fixed-list bounded-Lipschitz metric. It includes original singular actual-law passage and source contractions, the uniform source and bracket estimates, exact initial/martingale dependence treatment, covariance and every stated sequence/degenerate consequence. This is a fresh reconstruction result, not root promotion or the separately required hostile/source-gate certification.

Report: `AUDITS/BLIND_RECONSTRUCTION/ROUND_019_ALL_DIFFUSIVITY_RECONSTRUCTION.md` relative to the worktree or archive root.

The `inputs/` directory contains exact copies of all eleven allowlisted byte strings; `INPUT_SHA256SUMS.txt` is their original manifest with source-relative names. `OUTPUT_SHA256SUMS.txt` hashes the report and issued supporting outputs, using worktree-relative paths. `ARCHIVE_MEMBERS.txt` is the exact archive regular-file member list. The archive contains the report, input copies, manifests, this README, exposure record, new diagnostic and its result, and verification script. It excludes itself, its external digest file and the final seal-result file, avoiding self-reference. `ARCHIVE_SHA256SUMS.txt` fixes the archive bytes. The archive is created with regular files only and verified without extracting unsafe paths.

Verification from the isolated worktree:

    python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_019_ALL_DIFFUSIVITY_BLIND_ARTIFACTS/round019_blind_exact_diagnostic.py

Observed result before seal: PASS — 4,380 exact assertions in 19 categories and 271 mutation rejections in 7 classes. All arithmetic is exact rational, with no random seed, floating-point tolerance or third-party dependency. These finite diagnostics test coefficients and reject specific bad proof mutations; the analytic proof establishes the continuum assertions.

Seal verification, which performs read-only checks and does not rerun/rewrite the diagnostic:

    python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_019_ALL_DIFFUSIVITY_BLIND_ARTIFACTS/verify_packet.py

The verifier checks the eleven original working copies and packet copies, all output hashes, the external archive digest, exact member names, absence of unsafe paths/symlinks/hardlinks, and byte equality of every archive member with its sealed working-tree counterpart. The result is recorded in `SEAL_VERIFICATION.json`.

Report and issued files are set read-only after the final checks. The hashes, safe member list and external archive digest fix the issued bytes; read-only permissions provide a local editing guard, not a claim of an unalterable storage service. Do not rerun the writing diagnostic inside the sealed packet. A correction must be separately issued and must not rewrite these files.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r019-all-diffusivity-blind`.
Branch: `codex/hocf-r019-all-diffusivity-blind`.
Published base: `faf6f775a55579722319795cd9a9921e5829a903`.
Inputs, source/status boundaries and exposure are detailed in the report and `EXPOSURE_AND_SOURCE_RECORD.md`. No commit or canonical ledger edit was made. The bounded task ends at this sealed handoff. Root comparison, the separate hostile review and exact source gating remain the next actions.
