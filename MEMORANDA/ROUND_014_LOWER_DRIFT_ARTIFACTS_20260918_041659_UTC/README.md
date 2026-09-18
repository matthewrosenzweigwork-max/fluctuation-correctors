# TASK-073 bounded construction packet

Created 2026-09-18 UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r014-lower-drift`. Branch: `codex/hocf-r014-lower-drift`. Base remains `1df1805ed7cd8f7c295945f99273c8ffdb598e74`.

The entire frozen THM-035 card is proved as a conditional implication from its supplied smaller-gradient and complete-domain premises. The new lower-drift estimate is pathwise, retains the genuine inverse and both exact contractions, and includes the requested critical-range and integrated-cubic reduction. The actual cubic remains open. This is a constructor packet, self-checked only; root alone integrates or promotes after the required separate reviews.

## Files

- `../ROUND_014_LOWER_DRIFT_CONTRACTIONS.md`: complete proof, source/normalization preflight, explicit dependence of the new constant on the admitted gradient constant, domain and actual-law reasoning, exact coefficient reconstruction, critical inclusion, reduction, adversarial analysis, and per-item dispositions.
- `dossier/`: exactly the 25 authorized input files, unchanged. Their original repository-relative paths are preserved beneath this directory.
- `INPUT_SHA256SUMS.txt`: the original assigned 25-file input seal, byte-identical to the coordinator's seal.
- `EXPOSURE.md`: complete construction-context and ambient-exposure disclosure.
- `exact_diagnostic.py`: newly written standard-library exact diagnostic. It reads no previous checker, campaign state, or unlisted mathematical input.
- `RESULTS.json`: deterministic successful output, including exact input hashes, 57,186 assertions, range rows, and mutation detection.
- `VERIFICATION.md`: checks, command outcomes, limitations, and final handoff boundary.
- `OUTPUT_SHA256SUMS.txt`: root-relative SHA-256 hashes of the memo and every other packet file except this output seal itself.

The archive is the sibling `ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC.tar.gz`. It contains the memo plus this full directory and its output seal. The sibling archive `.sha256` file hashes the archive separately. The output seal does not hash itself or the archive; this avoids a circular seal. Both archive and archive hash are made read-only after verification.

## Reproduce without changing a sealed file

Run from the original worktree root or the root of an extracted archive:

```text
python3 MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/exact_diagnostic.py --verify-results MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/RESULTS.json
shasum -a 256 -c MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/OUTPUT_SHA256SUMS.txt
```

The first command rechecks all 25 embedded input hashes and recomputes the exact diagnostic, then compares its deterministic result with the sealed result. It requires Python 3.9 or newer and no external dependency. Original execution used Python 3.9.6. There is no floating tolerance, random seed, network request, or simulation of the actual singular law.

To verify the archive itself from the worktree root:

```text
shasum -a 256 -c MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC.tar.gz.sha256
```

The algebraic probes are smooth and periodic in one dimension and test exact universal coefficients. They are not substituted for the genuine singular inverse. The rational parameter mesh is diagnostic support; the memorandum proves the exponent assertions for every real admitted exponent.

## Scope and resumption

No canonical root files, root state, immutable inputs, commits, pushes, installations, or child agents were changed or created. The new branch/worktree and the authorized input overlay are the instructed isolation setup. This packet does not revise the frozen statement or decide the audit status of R8/R12. No TeX file was created; the complete proof is Markdown and no TeX build is claimed.

The next bounded action is an independent reconstruction and hostile review of this packet according to the root coordinator's protocol. The first remaining analytic target, after accepting the conditional inputs and lower-drift argument, is the actual integrated cubic residual. The constructor stops after sealing this packet rather than beginning that separate target.
