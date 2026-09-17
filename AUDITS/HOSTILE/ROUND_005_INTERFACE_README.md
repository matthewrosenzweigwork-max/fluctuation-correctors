# TASK044 review outputs

This is a sealed, full-proof hostile review of the frozen THM-025 candidate. It is not a blind review and does not recertify earlier module proofs.

- `ROUND_005_INTERFACE_REVIEW.md`: complete verdict, precise source-interface defects, per-claim review, independent kernel bridge and analytic checks.
- `ROUND_005_INTERFACE_CHECKS.py`: deterministic standard-library verification script.
- `ROUND_005_INTERFACE_CHECK_RESULTS.json`: exact iid results and numerical diagnostics from the issued run.
- `ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt`: the unchanged supplied nine-file input manifest.
- `ROUND_005_INTERFACE_OUTPUT_SHA256SUMS.txt`: issued output hashes, excluding that manifest itself.

Verdict: source/interface repair required; no endpoint counterexample found. The two required clarifications and the strongest surviving conclusion are recorded in the review. Candidate input files were not edited. No commit or push was made.

To reproduce the checks from the worktree root:

    python3 AUDITS/HOSTILE/ROUND_005_INTERFACE_CHECKS.py

To verify the output hashes from the worktree root:

    shasum -a 256 -c AUDITS/HOSTILE/ROUND_005_INTERFACE_OUTPUT_SHA256SUMS.txt

Treat the issued report as immutable. Any source clarification or changed verdict belongs in a separate addendum.
