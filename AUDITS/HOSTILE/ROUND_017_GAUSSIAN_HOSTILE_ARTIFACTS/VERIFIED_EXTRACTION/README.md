# AUD054 sealed hostile-audit packet

This packet reviews the entire frozen THM039 and its complete R17 candidate. Verdict: **PASS as the complete conditional implication stated by the candidate.** The separate THM038 and historical source gates are not promoted here. Read `ROUND_017_FINITE_DIMENSIONAL_REVIEW.md` for the full proof audit, per-claim verdicts, edge cases and limitations.

The task-owned worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r017-gaussian-hostile`, branch `codex/hocf-r017-gaussian-hostile`, based exactly at `072cab684b9ce41855ead6c48f435c8fc184ec35`. Root alone integrates or promotes. This worker made no canonical edits or commits.

Contents:

- `ROUND_017_FINITE_DIMENSIONAL_REVIEW.md`: byte-identical copy of the assigned audit report one directory above this packet.
- `INPUTS/`: the fourteen exact allowed inputs, preserving their paths.
- `INPUT_SHA256SUMS.txt`: original supplied manifest; `INPUT_COPY_SHA256SUMS.txt`: the same digests at their packet locations; `INPUT_VERIFICATION.json`: initial base/branch/count verification.
- `SOURCE_PREFLIGHT.md` and `EXPOSURE.md`: the source and isolation boundary, with the full detailed map in the report.
- `hostile_exact_diagnostics.py`, `DIAGNOSTIC_RESULTS.json` and `REPRODUCED_DIAGNOSTIC_RESULTS.json`: a fresh exact standard-library battery and two byte-identical executions.
- `REPRODUCTION_VERIFICATION.json`: exact commands, runtime, comparison, and development-harness disclosure.
- `OUTPUT_SHA256SUMS.txt`: the report/program/result/documentation output seal. Input copies have their separate manifest.
- `verify_sealed_packet.py`: standalone safe membership, hash, and extraction verifier.
- `AUD054_20260918_055644_UTC.zip` and its `.sha256` sidecar: the sealed payload archive.
- `ARCHIVE_MEMBERS_SHA256SUMS.txt` and `ARCHIVE_VERIFICATION.json`: exact archive member seal and completed verification. `VERIFIED_EXTRACTION/` is the fresh verification extraction, retained as evidence and excluded from the payload itself.

The final diagnostic passed 1,031 exact assertions, compared 4,974 polynomial coefficients, and rejected 15 deliberately incorrect mutations. These finite smooth probes support the analytic audit; they do not certify singular passage or weak convergence computationally. There are no random seeds, floating-point tolerances, third-party modules or installations. Python 3.9.6 was used.

From any extracted packet directory, verify the input/output hashes:

    python3 verify_sealed_packet.py --directory .

Reproduce the diagnostic with a new output path outside the sealed packet:

    python3 hostile_exact_diagnostics.py --output /absolute/path/to/new-results.json

Compare those bytes with `DIAGNOSTIC_RESULTS.json`. The program reads only its own source to compute its digest; it reads no candidate, earlier checker, state file or archive. It is deterministic.

To recheck the archive against this packet and perform a new safe exact-byte extraction, choose an extraction directory that does not already exist:

    python3 verify_sealed_packet.py --directory . --archive AUD054_20260918_055644_UTC.zip --extract-to /absolute/path/to/new-extraction

The archive verifier rejects absolute or parent paths, symlinks, directory members, duplicate entries, extra/missing members and byte/hash mismatches. It verifies the ZIP digest and all extracted input/output bytes. Sidecar records are external to the ZIP to avoid circular hash claims. Issued files are read-only; a correction must supersede this packet rather than modify it.

No TeX source was created, so no TeX compilation was applicable. The mathematical audit is the Markdown report, with precise equations in plain-text displays. The final bounded handoff contains no mathematical LaTeX.
