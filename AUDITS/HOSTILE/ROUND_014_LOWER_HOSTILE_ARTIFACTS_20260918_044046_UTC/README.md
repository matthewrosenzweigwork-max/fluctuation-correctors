# TASK-076 sealed lower-drift hostile packet

Verdict: **CONDITIONAL PASS** for THM-035 and all stronger mathematical assertions in the entire supplied R14 constructor. The separate ordered-distinct-sum rendering erratum is accepted. The original constructor remains byte-identical. Earlier R8/R12 premises remain conditional; cubic smallness and campaign promotion are not established by this packet.

The full report is `AUDITS/HOSTILE/ROUND_014_LOWER_DRIFT_REVIEW.md`, relative to the worktree or an extracted archive root. The report supplies exact source locations, per-claim verdicts, complete coefficient and estimate derivations, falsification cases, the rendering finding, and the exact remaining obligation.

## Contents

- `INPUTS/`: exactly the 27 allowed evidence inputs, copied byte-for-byte.
- `INPUT_SHA256SUMS.txt`: the controlling 27-input manifest, unchanged.
- `SOURCE_EXPOSURE_PREFLIGHT.md`: source inventory, conditional boundaries, and ambient exposure.
- `exact_hostile_diagnostic.py`, `RESULTS.json`, and `REPLAY_RESULTS.json`: independently written exact diagnostic, final results, and the byte-identical replay launched from outside the worktree.
- `VERIFICATION.md`: performed checks, outcomes, scope, and limits.
- `verify_packet.py`: portable input/output/archive integrity verification.
- `OUTPUT_SHA256SUMS.txt`: seals the report, all copied inputs, and the packet's substantive output files; paths are relative to the worktree/archive root.
- `SEALED_PACKET.zip`: only the named sealed inputs and outputs, preserving those relative paths; it contains the output manifest but cannot contain its own archive seal.
- `SEAL_VERIFICATION.json` and `SEAL_SHA256SUMS.txt`: external archive-verification results and hashes of the archive, output manifest, and verification result.

The assigned worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r014-lower-hostile`, branch `codex/hocf-r014-lower-hostile`, base `072cab684b9ce41855ead6c48f435c8fc184ec35`. This packet creates no commit or canonical-state update. Root alone compares the independent reports and determines promotion.

## Reproduction and exact arithmetic

From the worktree or a fresh archive extraction root, execute the diagnostic with a new output path so the issued result is not overwritten:

```text
python3 AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/exact_hostile_diagnostic.py --output /path/to/new-replay-results.json
```

The diagnostic locates its adjacent frozen `INPUTS/` and input manifest, so it does not need a Git checkout or files outside the archive. It requires only Python's standard library. The final result is PASS with 236,686 assertions and all nine wrong coefficient alternatives detected. The recorded JSON also includes exact witnesses, boundary values, assertion categories, runtime version, and all 27 input hashes.

The coefficient checks use rational Laurent polynomials in unit-torus Fourier characters. The formal derivative multiplies each coefficient by its integer frequency; physical differentiation restores a factor `2 pi i`. The physical odd real force is `i` times the formal odd Laurent force. Thus every force-drift identity restores the same factor `-2 pi`, while the separately tested diffusion identity restores `-4 pi^2`. The force is a smooth even-potential gradient diagnostic, not a replacement for the actual Riesz force.

The program directly differentiates the full empirical observable, computes the responses by minus-divergence convolution, and forms every statistic using literal subsets and injective particle-label maps. It does not read or import any earlier checker. Rational exponent probes and finite signed-function probes test only their stated algebraic inequalities. No finite diagnostic certifies the singular-domain premise, analytic limits, cubic smallness, or a fluctuation law.

For integrity verification, run:

```text
python3 AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/verify_packet.py
```

This verifies every frozen input and sealed output. If the external `SEALED_PACKET.zip` is present it also checks exact archive membership, safe names, CRC, and member-by-member digests. Add `--require-archive` when verifying the full issued packet rather than only an extraction. If the external seal is present, it verifies its entries too. The verifier reports explicitly which components were present and checked.

Issued files are read-only and hash-sealed. Reproduce into a new output path. Any correction must be a separately named superseding artifact; do not edit this report, the constructor, its erratum, copied inputs, results, or seals.
