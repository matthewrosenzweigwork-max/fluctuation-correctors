# TASK047 supplemental review outputs

The supplemental recheck discharges TASK044-D1 and D2 for the original THM-025 candidate together with the separately hashed source-and-constant addendum. It reuses the TASK044 reviewer context and is not a new blind audit. The original report and both original seals remain unchanged.

- `ROUND_005_INTERFACE_SOURCE_RECHECK.md`: scoped verdict, source verification, dispositions, and provenance limits.
- `ROUND_005_INTERFACE_SOURCE_RECHECK_VERIFY.py`: integrity, source-location, and exact scalar checks.
- `ROUND_005_INTERFACE_SOURCE_RECHECK_CHECK_RESULTS.json`: issued verification results.
- `ROUND_005_INTERFACE_SOURCE_RECHECK_INPUT_SHA256SUMS.txt`: the five supplemental inputs.
- `ROUND_005_INTERFACE_SOURCE_RECHECK_OUTPUT_SHA256SUMS.txt`: the new issued outputs, excluding that manifest itself.

Run from the isolated worktree root:

    python3 AUDITS/HOSTILE/ROUND_005_INTERFACE_SOURCE_RECHECK_VERIFY.py

Verify the new output seal:

    shasum -a 256 -c AUDITS/HOSTILE/ROUND_005_INTERFACE_SOURCE_RECHECK_OUTPUT_SHA256SUMS.txt

The original TASK044 report retains its historical REPAIR_REQUIRED verdict. Any change to this supplemental report after issuance requires a further separately sealed document.
