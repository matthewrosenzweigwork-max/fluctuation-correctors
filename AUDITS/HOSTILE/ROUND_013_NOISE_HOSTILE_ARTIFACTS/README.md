# TASK072 hostile-review handoff

The report at AUDITS/HOSTILE/ROUND_013_BOUNDED_NOISE_REVIEW.md gives a CONDITIONAL PASS for every frozen THM034 claim. It is a hostile review of the complete sealed R13 constructor, not a statement-only reconstruction and not a promotion of earlier conditional modules.

The lane used the requested worktree /Users/matthewrosenzweig/.codex/worktrees/hocf-r013-noise-hostile and branch codex/hocf-r013-noise-hostile, created from published R9 commit 29d7ce427ad7a98739b18d07781e71c4598b3579. No commits, pushes, installations, children, root edits, or canonical-state edits were made. The 28 mathematical/administrative source files named in the task manifest were copied and hash-checked before their mathematics was read.

## Files

All auxiliary names are confined to ROUND_013_NOISE_HOSTILE_ARTIFACTS.

- hostile_exact_checker.py: independently written exact supporting diagnostics, using Python's standard library only.
- exact_results.json: deterministic issued results, 56,353 exact checks passing.
- verified_inputs.json: all 28 input paths, byte lengths, and verified SHA-256 values.
- INPUT_SHA256SUMS.txt: byte-identical copy of the supplied input manifest.
- OUTPUT_SHA256SUMS.txt: SHA-256 inventory of the report and auxiliary payload files. As usual, the manifest does not hash itself.
- EXPOSURE.md: deliberate reads, unavoidable context exposure, source boundaries, and administrative actions.
- verification.json: verification scope, commands, and outcomes before sealing.

The report identifies every imported premise, recomputes every new load-bearing estimate, and gives a per-claim disposition. There is no theorem repair hidden in this package.

## Reproduce the exact checks

From the package root, use the existing Python 3 runtime:

    python3 AUDITS/HOSTILE/ROUND_013_NOISE_HOSTILE_ARTIFACTS/hostile_exact_checker.py --verify-results AUDITS/HOSTILE/ROUND_013_NOISE_HOSTILE_ARTIFACTS/exact_results.json

The issued local runtime was Python 3.9.6. The program reads only the input files in the manifest and its own issued results when verification is requested. It writes nothing unless an explicit output path is supplied. It uses fractions and integers, no floating tolerances, no randomness, no external package, and no previous checker.

The finite-state dependent laws, discrete convolution modes, and local polynomial/radial probes are diagnostics of factors and inequalities. They are not claimed to realize the actual singular dynamics, prove expectation derivatives, establish entropy passage, or certify any continuum theorem. The mathematical verdict comes from the written analytic audit with its explicit conditional source assumptions.

## Integrity and immutable seal

The sealed archive is ROUND_013_BOUNDED_NOISE_HOSTILE_20260918_040707_UTC.tar.gz in AUDITS/HOSTILE. It contains the exact 28-file permitted dossier at its repository-relative paths, the original supplied input manifest, the complete review, and every auxiliary payload listed by OUTPUT_SHA256SUMS.txt, together with that output manifest. It contains no current canonical state, non-allowlisted audit, Git internals, archive of earlier work, or prior checker.

The archive's adjacent .sha256 file and .verification.json file are external seal records; including a digest of the archive inside itself would be self-referential. The external verification record records safe-member inspection, exact equality of archived and worktree payload bytes, input/output-manifest checks, and a fresh checker run from an extracted sealed package. The archive and issued payload files are made read-only after verification. Later corrections must use a new superseding report and archive.

The input and output manifests can also be checked with the existing SHA-256 utility from the extracted package root:

    shasum -a 256 -c AUDITS/ROUND_013_BOUNDED_NOISE_HOSTILE_INPUT_SHA256SUMS.txt
    shasum -a 256 -c AUDITS/HOSTILE/ROUND_013_NOISE_HOSTILE_ARTIFACTS/OUTPUT_SHA256SUMS.txt

No TeX or PDF is part of this handoff; the required report is Markdown. No compilation is claimed.

## Remaining scope

Acceptance is conditional on exactly the earlier modules named in the report. Their unseen audit status was not consulted or used. The root coordinator must compare the separate current reviews and decide canonical promotion. The actual cubic drift residual, lower-contraction control, other dimension/exponent ranges, and a fluctuation law remain separate obligations.
