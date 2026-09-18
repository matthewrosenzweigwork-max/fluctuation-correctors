# TASK-052 sealed hostile-review handoff

Issued 2026-09-18 UTC from `/Users/matthewrosenzweig/Library/CloudStorage/GoogleDrive-mrosenz2@andrew.cmu.edu/My Drive/Git/fluctuation-correctors-r007-gradient-hostile` on branch `codex/hocf-r007-gradient-hostile`.
Base commit: `3aa91391516f35afe5317a287b4f0e2e93e6384c`.

Verdict: PASS for the complete frozen THM-027 assertion. No failed mathematical line was identified. The candidate's literal rendering token on line 427 is preserved and recorded separately. This review does not certify a particle Itô domain, evolved residual, uniform-N bracket, or critical limit.

## Files

- `ROUND_007_GRADIENT_REVIEW.md`: complete independent hostile verdict, exact scope, per-claim dispositions, source preflight, and the detailed common-flow, expectation, response and Volterra checks.
- `ROUND_007_GRADIENT_REVIEW_CHECKS.py`: independently written standard-library exact checker; it does not import the constructor checker.
- `ROUND_007_GRADIENT_REVIEW_CHECKS.json`: actual PASS result for 5,468 exact assertions under Python 3.9.6, with the checker digest and explicit evidence scope.
- `ROUND_007_GRADIENT_INPUT_SHA256SUMS.txt`: the exact fifteen-file permitted input seal, copied from the supplied dossier manifest. Its SHA-256 is `cb0e4f20b38735c4d41ab0613c18434a9f947177317b6071a1b8d514a9c85523`.
- `ROUND_007_GRADIENT_OUTPUT_SHA256SUMS.txt`: immutable output seal for the report, checker, JSON, this README, and input seal. It excludes itself.

All paths above are relative to `AUDITS/HOSTILE/`. The seal paths themselves are relative to the worktree root. No input, root working file, canonical ledger, or previous audit report was edited. Only the requested worktree registration changed root Git metadata. No commit, push, merge, additional source lookup, dependency installation, or child worker was used.

## Executed verification

From the worktree root:

```sh
python3 AUDITS/HOSTILE/ROUND_007_GRADIENT_REVIEW_CHECKS.py
shasum -a 256 -c AUDITS/HOSTILE/ROUND_007_GRADIENT_INPUT_SHA256SUMS.txt
git diff --check
git rev-parse HEAD
shasum -a 256 -c AUDITS/HOSTILE/ROUND_007_GRADIENT_OUTPUT_SHA256SUMS.txt
```

Outcomes: 5,468 exact assertions passed; all fifteen input hashes matched; the whitespace check returned success without output; HEAD matched the base commit above; every output hash matched. The output hash check was run after this README and the output seal were written.

A direct standard-library artifact check additionally verified terminal newlines, absence of trailing whitespace and control characters, balanced standalone display/fence delimiters in the review, the JSON status and assertion count, the checker digest recorded by the JSON, and the fifteen-row input count. These checks passed. The report's analytic conclusions are justified in prose and are not inferred from the arithmetic assertion count.

The checker uses exact fractions only. It includes local rational-jet force/source differentiation, matrix eigenvector checks, a zero-noise radial model, inhomogeneous Fourier response identities, Coulomb atom/compensation, and exponent thresholds. It does not approximate the stochastic flow or numerically prove an expectation interchange. The local diagnostics do not replace the periodic kernel, prescribed ordinary transport, or the two exact responses.

No TeX source or PDF is part of this Markdown/code review handoff. No TeX source was modified, and the final handoff contains no mathematical LaTeX. No unrelated campaign test was run because TASK-052 restricts the input boundary.

## Reproduction and integration

Preserve the sealed bytes. Hash verification is read-only. To rerun the checker without altering the sealed JSON, copy the checker to a separate review directory and execute that copy; it writes a JSON file next to itself. A different Python version changes its recorded environment field.

Root should compare this immutable hostile review with the separately isolated reconstruction, then assign any canonical audit/status disposition. The source candidate's rendering token can receive a separate explicit erratum. This lane made no mathematical repair, changed no range, and did not inspect the other review.
