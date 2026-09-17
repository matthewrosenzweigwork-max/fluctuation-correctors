# Round 001 handoff

This local package preserves the verified installation plus uncommitted Round 001 research. Read NEXT_INVOCATION.md, the round report and the multi-axis theorem ledger. The scientific mission remains OPEN.

The archive contains a repository snapshot, the checkpoint SHA-256 manifest, and REPRODUCTION/BASELINE.bundle. To recover in a new directory, clone that bundle into a fresh repository, then copy the snapshot files over that baseline checkout. This yields the original baseline commit with the current research changes uncommitted. Do not reinstall the original overlay over the research snapshot. Do not copy a .git directory from a different checkout.

Run the protected provenance check, installed verifier and checkpoint checksum check shown in NEXT_INVOCATION.md. Primary source PDFs and relevant page/text evidence are retained. Detailed mathematical proofs and immutable audits accompany the compiled six-page summary and its TeX source. The archive omits .git, worker worktrees, transient build pages and scratch files; every integrated canonical artifact is retained. Worker prompts, input hashes and verdicts preserve isolation provenance. Baseline has not been pushed; no subsequent research commit was made.

PACKAGES contains the timestamped ZIP and its separate SHA-256 receipt. The ZIP's internal PACKAGE_SHA256SUMS.txt also checks the bundled baseline and all snapshot files, avoiding a self-referential checksum. The checkpoint manifest covers the repository artifacts independently of the ZIP.
