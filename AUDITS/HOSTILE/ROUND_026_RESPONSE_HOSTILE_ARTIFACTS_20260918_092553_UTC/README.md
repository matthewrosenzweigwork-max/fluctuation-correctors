# AUD072 hostile evidence packet

This is the immutable TASK113 hostile review of the entire frozen THM050 /
PO037 conjunction. A/B/C and the whole conjunction received hostile PASS;
no first failing mathematical line was found. Root owns comparison with
the separate blind axis, historical gate authentication and promotion.
Neither the actual critical source nor its negation is proved here.

`REPORT.md` is byte-identical to the assigned sibling
`ROUND_026_RESPONSE_REVIEW.md`. It contains the exact scope and negation,
complete mathematical dispositions, source qualifications, whole-report
coverage, evidence limitations and remaining obligations.

Contents:

- `INPUTS/`: all 13 exact permitted input files, retaining their relative names.
- `INPUT_SHA256SUMS.txt`: exact copy of the supplied allowlist manifest.
- `INPUT_VERIFICATION.json`: digest, size and line-count verification.
- `EXPOSURE_AND_HISTORY.md`: complete read, role, communication and run history.
- `hostile_diagnostic.py`: fresh standard-library supporting diagnostic.
- `DIAGNOSTIC_RESULTS.json`: final baseline and every mathematical mutation,
  with complete commands, stdout, stderr and exit codes.
- `verify_read_only.py`: portable verifier; reads only and never extracts.
- `VERIFIER_CONTROL_RESULTS.json`: all four deliberate verifier failures.
- `issue_packet.py`: exact issuance procedure, retained for provenance.
  It refuses to replace existing sibling artifacts; do not reissue this packet.

The final diagnostic passed 283 assertions in 13 categories. All 13
mathematical mutations exited 1. Exact rational arithmetic is used except
for 36 explicitly bounded deterministic cosine calculations, with absolute
roundoff slack 2e-15. No random sampling or SDE discretization is used.
The proof of the singular process, the stopped estimates and the weak
Sobolev passage is analytical; these computations do not certify it.

All four verifier controls exited 1: digest corruption, parent traversal,
symlink member, and an extra inventory member. The invalid archive controls
are in-memory objects, not extracted files or hidden unsafe archives.

The sibling delivery set uses this packet directory's complete name as its
prefix:

- `.tar.gz`: safe regular-file archive of exactly the packet's files.
- `.INVENTORY.json`: complete directory list and every regular file's relative
  path, size, mode and SHA-256, including this README and all code files.
- `.CORE_VERIFICATION.json`: actual core check result before the outer seal.
- `.SHA256SUMS`: every payload file plus the archive, inventory, core result
  and assigned external report. The seal excludes itself to avoid a hash cycle.

The packet and payload directories are mode 0555; every payload, report,
archive and sibling metadata file is mode 0444. No source or canonical
file is made read-only by this procedure. Corrections must be distinct
superseding artifacts, never edits to this issued packet.

To verify, retain the complete sibling set together and run:

```sh
python3 ROUND_026_RESPONSE_HOSTILE_ARTIFACTS_20260918_092553_UTC/verify_read_only.py
```

The verifier checks exact member sets, all 13 input hashes, file sizes and
digests, safe relative regular archive members, no links or duplicates,
archive/directory equality, assigned-report equality, modes and the outer
seal. It does not need the original checkout, Git, network access or any
third-party package. Do not use `--skip-seal` for ordinary verification;
that flag exists only for the recorded pre-seal issuance stage.

The supporting diagnostic can be rerun read-only:

```sh
python3 ROUND_026_RESPONSE_HOSTILE_ARTIFACTS_20260918_092553_UTC/hostile_diagnostic.py
```

Example deliberate failures, both expected to exit 1:

```sh
python3 ROUND_026_RESPONSE_HOSTILE_ARTIFACTS_20260918_092553_UTC/hostile_diagnostic.py --mutation halve_relative_drift
python3 ROUND_026_RESPONSE_HOSTILE_ARTIFACTS_20260918_092553_UTC/verify_read_only.py --control unsafe_archive_path
```

The parent-provided branch/base metadata was not verified by a Git read.
The task card's pre-issuance count of 643 lines differs from the complete
646-line hashed candidate; all 646 lines were reviewed. Constructor code,
results, other audits, source archives, canonical state, history, memory,
other worktrees and nonallowlisted references were not inspected. No
constructor result count or older gate status is authenticated by this
packet. The root's complete comparison remains a separate action.
