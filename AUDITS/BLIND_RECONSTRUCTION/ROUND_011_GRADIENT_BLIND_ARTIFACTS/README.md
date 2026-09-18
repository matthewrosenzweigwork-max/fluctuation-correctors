# TASK-068 blind reconstruction packet

This packet reconstructs frozen THM-032 from exactly twenty-one allowlisted inputs, without reading the current candidate, root seed, R10/R12 current proofs, current audits/state/history, memory files, or prior checkers. The report records the ambient platform/global-summary exposure.

Verdict: every frozen analytic assertion is reconstructed, conditional on the existing singular base-process and bounded-full-inverse inputs in their issued scopes. No new failed line inside THM-032 was found. This is a statement-only reconstruction; root comparison and a separate hostile review are still required. It does not assign current canonical acceptance to earlier modules or prove an actual-law bracket, residual, or fluctuation statement.

The report is AUDITS/BLIND_RECONSTRUCTION/ROUND_011_RESCALED_GRADIENT_RECONSTRUCTION.md. All auxiliary files use the unique directory AUDITS/BLIND_RECONSTRUCTION/ROUND_011_GRADIENT_BLIND_ARTIFACTS.

## Reproducibility

Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r011-gradient-blind.

Branch: codex/hocf-r011-gradient-blind.

Verified base: 29d7ce427ad7a98739b18d07781e71c4598b3579.

Run from the worktree or a disposable extracted copy:

    /usr/bin/python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_011_GRADIENT_BLIND_ARTIFACTS/round011_gradient_blind_exact.py

The fresh checker passed 16,207 exact assertions. It uses only the Python standard library, integer and rational arithmetic, no random seed, and no tolerance. Its JSON gives the complete group counts and evidence limitations. Re-running changes the result timestamp; use a disposable copy if preserving the issued packet.

To verify the issued packet without modifying it:

    /usr/bin/python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_011_GRADIENT_BLIND_ARTIFACTS/verify_packet.py

The verifier checks all input and output hashes, exact archive membership, archive CRC, member digests, and the external seal. The archive stores paths relative to the worktree root. It contains the twenty-one allowed inputs, seven output files, and the output manifest: twenty-nine members, with no unrelated inherited worktree files.

## Files and evidence

- INPUT_SHA256SUMS.txt is byte-identical to the assigned twenty-one-entry input manifest.
- input_verification.json records the checked source digests and base.
- round011_gradient_blind_exact.py is newly written for this reconstruction.
- round011_gradient_blind_exact_result.json records all 16,207 passing exact assertions.
- verify_packet.py performs read-only packet verification.
- OUTPUT_SHA256SUMS.txt seals the report, checker, result, README, input manifest, input verification record, and packet verifier.
- The timestamped ZIP is the immutable reconstruction archive.
- SEAL_SHA256SUMS.txt seals that archive and the output manifest.

The analytic proof treats expectation derivatives, exceptional starts, singular stopping, finite signed-measure convolution, classical contraction derivatives, and uniform local/global limits separately. A direct Coulomb calculation falsifies the excluded weighted-supremum and H1 strengthenings.

All created text outputs were checked for terminal newline, trailing whitespace, control characters, and balanced display/inline mathematical delimiters in the report. No TeX was edited or generated, and no build, installation, commit, push, canonical ledger update, or child worker was used. After issuance, corrections require a separately named superseding report.

