# TASK059 hostile review packet

Verdict: **PASS_CONDITIONAL** for the full frozen THM029 implication with complete THM028 as a premise. The review finds no unsupported new line. Actual-law bracket smallness and independent prerequisite certification remain outside this result.

Base: published R7 `4171be9839feb8acf4c70e1dda014458fdb44490`. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r009-energy-hostile`. Branch: `codex/hocf-r009-energy-hostile`.

## Files

- `AUDITS/HOSTILE/ROUND_009_ENERGY_REVIEW.md`: complete per-claim hostile verdict and analytic checks.
- `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/EXPOSURE.md`: permitted and excluded exposure, including startup context.
- `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact.py`: independent standard-library exact Fourier/rational checker.
- `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact_result.json`: issued first-run result, **3,832 exact assertions passed**.
- `AUDITS/ROUND_009_ENERGY_HOSTILE_INPUT_SHA256SUMS.txt`: original twenty-file input manifest.
- `AUDITS/HOSTILE/ROUND_009_ENERGY_HOSTILE_OUTPUT_SHA256SUMS.txt`: hashes of the five issued review/checker/README/result/exposure outputs; excludes itself.
- `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/ROUND_009_ENERGY_HOSTILE_20260918_022909_UTC.zip`: exact permitted inputs, their manifest, the five outputs, and the output manifest.
- `AUDITS/HOSTILE/ROUND_009_ENERGY_HOSTILE_SEAL_20260918_022909_UTC.txt`: hashes the archive, input manifest, and output manifest; outside the archive to avoid self-reference.

All paths are relative to the isolated worktree or the archive root. The archive includes no other inherited repository files. SHA-256 seals and read-only output permissions preserve issued bytes. Any correction must be a newly named superseding output.

## Reproduce

From the worktree or an extracted archive root, with existing Python 3 and no installation:

```sh
shasum -a 256 -c AUDITS/ROUND_009_ENERGY_HOSTILE_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_009_ENERGY_HOSTILE_OUTPUT_SHA256SUMS.txt
python3 AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact.py --output /tmp/round009_energy_hostile_reproduction.json
```

The chosen reproduction result path must not already exist; the checker intentionally refuses to overwrite any result. Compare its JSON with the issued result: the diagnostic is deterministic, uses no random seed, and records input and checker hashes. The absolute output path is not written inside the JSON, so the result bytes reproduce exactly. For a second run choose a fresh result path.

From the original worktree, verify the outer seal with:

```sh
shasum -a 256 -c AUDITS/HOSTILE/ROUND_009_ENERGY_HOSTILE_SEAL_20260918_022909_UTC.txt
```

The outer seal refers to the archive alongside the files, so retain that archive when checking it. The archive does not contain itself or its outer seal.

## Verification record

- Initial copy: all twenty input SHA-256 checks passed before mathematical inspection; copied bytes were checked again.
- Exact run: `python3 AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact.py --output AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact_result.json` exited successfully; **3,832 assertions** passed on its first execution.
- Final `shasum -a 256 -c` checks for input manifest, output manifest, and outer seal passed.
- Scoped `git diff --check` passed. Since new outputs are untracked, a separate Python scan verified final newline, no trailing whitespace, and no unexpected control characters in all five output text files.
- Python ZIP inspection verified the exact allowlisted archive member set, CRC integrity, and every archived input/output/manifest byte against its sealed source.
- No TeX was changed or required by this handoff. No compilation, dependency installation, commit, or push was performed.

The checker is corroboration of the analytic review, not independent certification of the singular domain. It uses rational complex Fourier arithmetic and restores or explicitly states normalization factors; it is not a floating-point simulation or a proof by sampling.
