# TASK100 / AUD065 sealed handoff

The sibling report ROUND_023_STATIC_THRESHOLD_RECONSTRUCTION.md supplies
the complete analytic reconstruction of every THM045 clause and its
exact negation. Its verdict is reconstructed, pending root comparison
and a separate hostile gate. It is a static-law construction only.

## Contents

- inputs/: all eight exact frozen inputs, preserving relative paths.
- INPUT_SHA256SUMS.txt: the supplied input manifest, exact bytes.
- input_verification.json: initial overlay verification.
- SOURCE_EXPOSURE.md: complete source, isolation, and ambient-exposure record.
- diagnostic_v2.py and results_v2.json: accepted final diagnostic and results.
- diagnostic.py, preseal_probe_inspection.json, DIAGNOSTIC_HISTORY.md:
  retained pre-seal failure/inspection history; the inspection result is
  explicitly not accepted as validation.
- OUTPUT_SHA256SUMS.txt: complete archived payload manifest, excluding
  only that manifest's own self-hash.
- ARCHIVE_MEMBER_SHA256SUMS.txt: every actual regular archive member,
  including the output manifest itself.
- ARCHIVE_SHA256SUMS.txt: the exact compressed archive digest.
- SEAL_VERIFICATION.json and SEAL_SHA256SUMS.txt: verification record
  and external seal metadata digests.

The archive contains the report, all eight inputs, source/exposure
records, diagnostic code, outputs/history, and the output manifest.
External archive-member and seal records are created after the archive
and are siblings of this README. They are therefore not recursively
embedded into the archive they hash. SEAL_SHA256SUMS.txt excludes its
own self-hash, as required to avoid a circular digest.

Every archive member is a safe relative regular-file path. The seal
procedure reads and compares all member bytes without extraction,
rejecting symlinks, hardlinks, devices, absolute paths, parent traversal,
duplicate paths, and missing or extra members. Every issued file is
made read-only after verification. Any later correction must be a
new artifact.

## Reproduction

To reproduce in a writable copy, use Python 3 with its standard library:

python3 diagnostic_v2.py --output /an/existing/writable/path/results.json

No dependencies or random seed are needed. The exact phase uses
fractions.Fraction Gaussian rationals; the numerical phase uses
binary64 and has an analytic truncation bound but no certified
floating-point roundoff bound. Finite checks do not certify the proof.
The accepted result is 230 exact checks, eight detected mutations,
and passed supporting numerical checks through m=192.

No canonical edits, commits, pushes, installations, children, or
outside sources were used. The isolated worktree is:

/Users/matthewrosenzweig/.codex/worktrees/hocf-r023-static-threshold-blind

The bounded handoff ends here. Root alone compares the withheld
construction, resolves source-gate history matching, and decides
whether the separate hostile gate permits promotion.
