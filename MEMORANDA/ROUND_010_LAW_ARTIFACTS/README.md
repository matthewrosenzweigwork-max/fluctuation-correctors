# TASK060 — sealed actual-law entropy transfer and gradient-tail reduction

**Status: RIGOROUS SHARPER REDUCTION / SELF_CHECKED. The full expected actual-noise assertion remains OPEN.** THM028 and the supplied R9 energy construction remain conditional prerequisites in this dossier. This is the disclosed continuation constructor of TASK051/055, with the earlier seed disclosed; it is not a fresh audit or independent certification.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r010-law-transfer-20260918`

Branch: `codex/hocf-r010-law-transfer`

Base: published R7 `4171be9839feb8acf4c70e1dda014458fdb44490`

The exact twenty-file allowlist is `ROUND_010_LAW_INPUT_SHA256SUMS.txt`. Every supplied input was copied and verified before construction and again before sealing. No ongoing audits, other current worker reports, canonical state/history, memory, old checkers, or outside literature were read. No root/canonical file edits, commits, pushes, installations or children were used. Prior worktrees and immutable seals were preserved.

## Substantive result

The full proof attempt is `../ROUND_010_ACTUAL_NOISE_LAW_TRANSFER.md`.

- Equations (2.8) and (3.4) prove a uniform interaction-energy lower bound and an actual-law free-energy/entropy bound. The argument starts with the true smooth gradient dynamics from iid Haar data and passes to the supplied singular realization using the uniform lower bound and specified lower semicontinuity mechanisms. Coulomb compensation and the deleted self-energy are retained.
- Equations (4.1)–(4.4) give quantitative marginal entropy and bounded-test estimates, including the exact one-body-Haar improvement in the finite-N entropy factor.
- Equations (5.7)–(5.10) prove vanishing noise for an explicitly clipped part of the actual corrector martingale over the full stipulated bounded-noise range. Equation (5.11) allows a weaker threshold condition on a specified temperature sequence.
- Equations (6.4)–(6.5) reduce the original assertion, necessarily and sufficiently, to the large-gradient martingale tail. Equation (7.1) retains every pair, ordered distinct-triple, mixed and one-body coefficient; no third marginal is invoked for N=2.
- Equation (8.3) is an additional actual tail estimate for exponents above two, retaining the domain constant's N dependence. Equation (8.4) is a sufficient criterion whose needed N control is not supplied.

The **first unproved load-bearing line is (9.1)**: the actual expected tail bracket at the specified growing threshold tends to zero. No counterexample to the stipulated dynamics is claimed. The packet completes the task's permitted sharper-reduction alternative; it does not promote the full bracket assertion, a fluctuation theorem, or a critical closure. The three campaign temperature conditions remain distinct.

## Contents

- `../ROUND_010_ACTUAL_NOISE_LAW_TRANSFER.md`: full proof attempt, constants, singular passage, actual clipped result, exact tail reduction, and first unproved line.
- `round010_law_transfer_exact.py`: newly written exact diagnostic, importing no prior checker.
- `ROUND_010_LAW_EXACT_RESULTS.json`: issued result, **PASS, 20,300 exact assertions**, Python 3.9.6.
- `README.md`: this handoff.
- `ROUND_010_LAW_INPUT_SHA256SUMS.txt`: twenty root-relative input hashes.
- `ROUND_010_LAW_OUTPUT_SHA256SUMS.txt`: five root-relative output hashes, excluding itself.
- `ROUND_010_LAW_SEALED.zip`: exactly twenty inputs, five outputs and the output manifest, 26 members total.
- `ROUND_010_LAW_SEAL_SHA256SUMS.txt`: artifact-directory-relative hashes of the archive and output manifest, excluding itself.

The checker uses new three-symbol exchangeable laws, rational clipping, exact field/bracket contractions, finite positive-Fourier energy identities, and certified rational logarithm intervals from a 40-term atanh series with an explicit remainder. There is no random seed, floating-point tolerance or new dependency. N=2,3,4, nonzero mixed/triple/tail cross terms, initial Haar entropy, Coulomb compensation, free-energy noise factors, constant h and zero noise are covered. The finite laws and finite-group kernels are algebraic diagnostics, not numerical simulations or asserted laws of the singular dynamics. The first checker execution and the final issued execution both passed; no failed test was suppressed.

## Verify and reproduce

From the worktree root, verify the issued bytes first:

```sh
shasum -a 256 -c MEMORANDA/ROUND_010_LAW_ARTIFACTS/ROUND_010_LAW_INPUT_SHA256SUMS.txt
shasum -a 256 -c MEMORANDA/ROUND_010_LAW_ARTIFACTS/ROUND_010_LAW_OUTPUT_SHA256SUMS.txt
```

From this artifact directory:

```sh
shasum -a 256 -c ROUND_010_LAW_SEAL_SHA256SUMS.txt
```

After preserving or verifying the issued result bytes, run from the worktree root:

```sh
python3 MEMORANDA/ROUND_010_LAW_ARTIFACTS/round010_law_transfer_exact.py
```

The checker writes the JSON beside itself. A different interpreter version may alter its metadata and digest without changing the assertions. Extract a separate reproduction copy if the issued loose-file state must remain byte-identical.

Before handoff, the branch/base, all twenty input hashes, all five output hashes, the proof's 48 display pairs and environment delimiters, archive CRC and every one of its 26 member hashes were checked. No inherited unrelated file is included in the archive. The outer seal remains outside the archive to avoid a digest cycle. Later corrections must be issued as new superseding artifacts.
