# TASK-074 sealed independent reconstruction

The report is `../ROUND_014_LOWER_DRIFT_RECONSTRUCTION.md`. It proves the
complete frozen THM-035 implication with the supplied R8 domain and R12
gradient results retained as conditional premises. The new estimate is
pathwise, so no uniform evolving-law density estimate enters. The exact
coefficient calculation and critical-range inclusion are included. Cubic
smallness remains unproved; root alone compares the construction and audit
and decides promotion.

This directory belongs to the isolated branch
`codex/hocf-r014-lower-blind` at the assigned published R10 base
`1df1805ed7cd8f7c295945f99273c8ffdb598e74`.
`EXPOSURE.md` discloses the permitted dossier, ambient generic context and
the filenames-only Git status preflight. No current proof comparison preceded
sealing.

## Contents

- `INPUT_SHA256SUMS.txt`: the exact original 25-input hash manifest.
- `inputs/`: a read-only copy of exactly those 25 inputs, retaining their paths.
- `input_verification.json`: source/worktree input-copy hash checks.
- `lower_blind_exact.py`: independently written standard-library diagnostic.
- `exact_results.json` and `exact_rerun.json`: deterministic exact-arithmetic
  results from two executions of the final checker.
- `verification.json`: successful input, result, range, coefficient,
  scope and deterministic-rerun checks recorded before payload sealing.
- `environment.json`: Python/platform and isolated branch/base metadata.
- `EXPOSURE.md`: full isolation and status qualification.
- `OUTPUT_SHA256SUMS.txt`: seal of the report and every payload file, including
  every preserved input and these records. It excludes only itself to avoid a
  self-hash cycle.

The unique timestamped `.tar.gz` archive sits next to this directory. Its
companion `.sha256` seals the archive. The archive includes the report, this
directory and the output manifest. It contains only regular files at relative
paths, no absolute paths, parent traversals or symbolic links. Successful
verification of the archive checks its exact file list and each payload hash
against the included output manifest. The archive's `.verification.json`
sidecar records these final checks; a timestamped final seal manifest also
hashes this sidecar, the archive, its checksum and the output manifest.

## Reproduction

From the isolated worktree root, the original diagnostic commands were:

```sh
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_014_LOWER_BLIND_ARTIFACTS/lower_blind_exact.py > AUDITS/BLIND_RECONSTRUCTION/ROUND_014_LOWER_BLIND_ARTIFACTS/exact_results.json
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_014_LOWER_BLIND_ARTIFACTS/lower_blind_exact.py > AUDITS/BLIND_RECONSTRUCTION/ROUND_014_LOWER_BLIND_ARTIFACTS/exact_rerun.json
shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_014_LOWER_BLIND_ARTIFACTS/OUTPUT_SHA256SUMS.txt
```

The first two commands document the pre-seal runs. To rerun after sealing,
redirect the checker output to a new file outside this immutable payload, then
compare it byte-for-byte to `exact_results.json`. Do not overwrite the sealed
results. No package installation or special runtime is required.

For the preserved inputs, enter `inputs/` and run
`shasum -a 256 -c ../INPUT_SHA256SUMS.txt`. For an extracted archive, run the
output-manifest command from the extraction root; all names in that manifest
are relative to it. The archive's companion hash can be checked in its parent
directory with `shasum -a 256 -c <archive-name>.sha256`.

The diagnostic uses exact rational arithmetic with no random seed, tolerance
or statistical inference. Its Fourier probes concern finite smooth generator
coefficients and deliberately wrong alternatives. Its rational parameter grid
checks strict intervals and limiting exponents as a falsification aid. The
continuous-parameter inequalities, genuine singular representatives,
uniform estimate and scaled L1 equivalence are proved in the report; finite
tests do not certify them. The final result counts and mutation witnesses are
recorded in the result JSON files.

No canonical mathematical/source/state file was edited, and no TeX file was
created or changed. The assigned branch/worktree creation was expressly
authorized by TASK-074. There was no commit, push, merge, installation or child
agent. This handoff is bounded: compare the sealed proof and its conditional
premises, obtain any further hostile review required by the root protocol,
then decide the THM-035 disposition. The open genuine cubic estimate remains
the next mathematical step.
