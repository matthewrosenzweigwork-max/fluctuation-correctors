# AUD068 / TASK106 immutable hostile handoff

Whole-claim verdict: HOSTILE PASS for the unchanged THM047 conjunction, with
the exact source qualification in `REVIEW.md`. THM046 remains open. No
mathematical repair was made. The report gives separate ancillary dispositions;
constructor diagnostics and other contexts' attestations are not authenticated.

Contents:

- `REVIEW.md`: exact copy of the assigned sibling review report.
- `inputs/`: all 24 exact allowlisted input copies.
- `INPUT_SHA256SUMS.txt`, `INPUT_CHECKS.json`: frozen manifest and copy checks.
- `SOURCE_READS.md`, `EXPOSURE.md`: complete read/use/isolation boundaries.
- `hostile_diagnostic.py`, `RESULTS.json`: new exact diagnostic, 889 assertions,
  18 nonzero mutation witnesses.
- `DIAGNOSTIC_HISTORY.md`, `history/UNISSUED_DRAFT_v0.py`: retained development
  history, with the draft explicitly separated from the issued diagnostic.
- `verify_packet.py`: portable, read-only standard-library verifier.
- `ARCHIVE_MEMBERS.txt`: closed list of every file permitted in the archive.
- `OUTPUT_SHA256SUMS.txt`: every packet-file digest except this manifest's
  own digest, which is covered by the external seal. The member inventory
  itself is in the output manifest; this prevents a self-hash cycle.

The sibling ZIP has exactly the listed regular files, with no directories,
absolute paths, traversal, backslashes, duplicate names, links, or writable
members. The external `*_SEAL.json` covers the archive, output manifest,
member inventory and assigned report. The issued packet files, sibling report,
ZIP and seal are read-only. These are integrity checks, not a digital signature
or authentication of external chronology or model selection.

From this directory, run:

```text
python3 verify_packet.py
python3 hostile_diagnostic.py --check RESULTS.json
```

The verifier's default archive/seal/report paths are the named siblings. If
these are moved, use `--archive`, `--seal`, and `--report` explicitly. It never
extracts an archive or writes a file. No dependency installation is needed.

The next mathematical obligation remains the combined retained dynamic L1
limit in R24 (7.5). Root must independently compare whole-claim axes and match
the exact prerequisite modules to current accepted gates before promotion.
This packet supplies neither that dynamic limit nor a full campaign theorem.
