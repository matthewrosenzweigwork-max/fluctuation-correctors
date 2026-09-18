# AUD070 hostile review packet

Whole THM048: PASS. Whole THM049: PASS. Joint conjunction: PASS. THM046 and its actual signed-correlation cancellation remain OPEN. This is the hostile gate; root still owns comparison with the withheld fresh reconstruction, exact accepted-source matching and canonical promotion.

Read REPORT.md first. It is an exact copy of the issued `AUDITS/HOSTILE/ROUND_025_SOURCE_UI_REVIEW.md`. The source/exposure record distinguishes full, partial and hash/copy-only reading. The packet contains all 15 exact frozen input files and the original manifest. The candidate's hash-matched 687-line complete contents were reviewed; the task's old 663-line count is an administrative discrepancy only.

The fresh exact diagnostic passed 1,906 assertions in 33 categories and detected 20 deliberately incorrect variants with nonzero witnesses. DIAGNOSTIC_RESULT.json is the full first-run result, and RUN_HISTORY.md records the complete run history. The diagnostic is coefficient and solvable-model support, not a substitute for the analytic singular stochastic audit.

Run without modifying the packet:

    python3 VERIFY_READ_ONLY.py

By default this verifies the payload, the sibling archive named after this directory with suffix `.tar.gz`, and its sibling `.SEAL.json`. It never extracts an archive, changes permissions, executes another file or writes output files. It reports JSON to stdout. `--payload-only` checks an extracted packet if the sibling archive/seal are unavailable; that mode is explicitly weaker and reports its mode. An optional `--archive PATH` selects an archive, and `--seal PATH` selects its corresponding seal.

To rerun the mathematical diagnostic without changing the sealed result:

    python3 hostile_exact_diagnostic.py

It prints deterministic JSON to stdout and reads no file. Do not redirect over the issued DIAGNOSTIC_RESULT.json. No dependency beyond the Python standard library is required.

MEMBERS.txt lists all payload file paths, including itself and CONTENT_SHA256SUMS.txt. CONTENT_SHA256SUMS.txt hashes every payload file except itself, including MEMBERS.txt and this verifier. The sibling `.SEAL.json` hashes both inventories, the report and the complete archive; the sibling `.SHA256SUMS.txt` also hashes the completed `.VERIFICATION_RESULT.json`. This explicit layering avoids circular hashes. The archive contains only those unique safe relative regular members, with mode 0444 and no directory, link, device, absolute or traversal entry. The verifier compares every archived file to its exact payload bytes without extraction.

All issued payload, report, archive and seal files are read-only. A correction requires a separately named superseding issuance. These are content-integrity and read-only seals, not a cryptographic signature or a claim of protection against a privileged writer. No other source, audit narrative, current state, history, memory, private input or other worktree was accessed. No source/canonical edits, children, installation, commits, pushes or remote changes occurred.
