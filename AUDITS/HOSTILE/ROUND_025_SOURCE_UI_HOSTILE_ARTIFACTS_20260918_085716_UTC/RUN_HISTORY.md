# AUD070 full execution and verification history

The audit used the assigned hostile worktree only. Commands below are relative to that worktree unless a packet-local form is shown. No prior checker was opened. Mathematical diagnostics had one implementation and one execution, with no failure or rerun before issuance.

1. Read `TASKS/ACTIVE/TASK-109_ROUND025_SOURCE_UI_HOSTILE.md`, then `AUDITS/ROUND_025_SOURCE_UI_HOSTILE_INPUT_SHA256SUMS.txt`.
2. Ran `shasum -a 256 -c AUDITS/ROUND_025_SOURCE_UI_HOSTILE_INPUT_SHA256SUMS.txt`. Outcome: all 15 rows OK, exit 0.
3. Read the full administrative/model/theorem cards. Counted lines of the supplied mathematical files. The candidate has 687 lines, not the 663 in the task prose. Read its complete numbered contents. No input altered.
4. Read constructor CLAIM_CARD and exposure record. A combined display of the two older full reports was truncated; dedicated untruncated reads recovered complete R16 and R6. Read R1 lines 1–250, R4 lines 1–190 and R10 lines 1–240. Exact source exposure is in the separate record.
5. Reported the line-count discrepancy to root. Root confirmed the exact hash controls and identified the old count as administrative. No mathematical narrative or other audit result was supplied.
6. Recomputed the full analytic assertions and negations, singular stochastic passages, pointwise majorant, clipping, UI and modal/full-target equivalences. No mathematical defect found; report retains THM046 as open.
7. At 2026-09-18 08:57:16 UTC, created the unique artifact directory with exclusive creation. Reverified all 15 source hashes and regular-file status, copied their exact bytes plus the original manifest, and wrote INPUT_VERIFICATION.json. Runtime: Python 3.9.6. Verified the assigned report did not already exist.
8. Wrote `hostile_exact_diagnostic.py` afresh. It reads no input or previous checker and writes only JSON to stdout.
9. Ran:

       python3 AUDITS/HOSTILE/ROUND_025_SOURCE_UI_HOSTILE_ARTIFACTS_20260918_085716_UTC/hostile_exact_diagnostic.py > AUDITS/HOSTILE/ROUND_025_SOURCE_UI_HOSTILE_ARTIFACTS_20260918_085716_UTC/DIAGNOSTIC_RESULT.json

   Outcome: exit 0 in approximately 1.6 seconds; no stderr; first execution PASS. Full result was read and checked: 1,906 exact assertions, 33 categories, 20 nonzero mutation witnesses. There were no failed diagnostic runs, code corrections or hidden numerical tolerances. All mutation records are in the JSON, including their exact nonzero values.
10. Wrote the complete hostile report with separate whole THM048, whole THM049, joint, ancillary, evidence and typesetting dispositions. Wrote the read/exposure record, README and read-only verifier.
    Root then reported only that its blind-packet verification and comparison had completed, without disclosing that verdict or any mathematical detail. This arrived after the hostile mathematics and report were complete and is recorded in the exposure file.
11. Issuance constructs the exact REPORT.md copy, complete member inventory and content digest inventory, validates every payload file, sets all issued files read-only, and creates a sibling USTAR/gzip archive with only unique safe relative regular read-only members. The archive and outer seal authenticate the inventories and report. The final sibling VERIFICATION_RESULT.json records the actual complete issued-archive verifier result, so it does not claim that result before the archive exists.

No TeX files were changed or compiled. No rendered PDF verification is claimed. The mathematical final handoff is the Markdown report; the conversational final response contains no mathematical LaTeX. No canonical/state/source file was modified. No children, external reads, dependencies, commits, pushes or remote changes occurred.

The content digest inventory covers every payload file except itself. The member inventory also lists that digest inventory. The external seal hashes both inventories and the completed archive, avoiding a circular self-hash claim. The final external checksum file additionally covers the actual verifier-result file. These bootstrap exclusions are explicit, not omitted members.
