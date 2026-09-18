# TASK055 — sealed homogeneous Haar energy construction

**Status: CONDITIONAL / SELF_CHECKED.** The complete THM029 implication is proved conditional on the complete THM028 domain assertion. That prerequisite remains conditional in this dossier. This is the disclosed continuation constructor that produced the R8 candidate, and the root seed was disclosed. This packet is not an independent audit or certification.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r009-haar-energy-20260918`

Branch: `codex/hocf-r009-haar-energy`

Base: published R6 `3aa91391516f35afe5317a287b4f0e2e93e6384c`

The nineteen paths and exact input hashes are in `ROUND_009_ENERGY_INPUT_SHA256SUMS.txt`. They were copied and verified before construction. Only this permitted dossier was read. Prior R5 and R8 worktrees and seals were preserved; no ongoing audits, state/history, memory, prior checkers, or outside literature were read. No root or canonical file edits, commits, pushes, dependency installations, or child agents were used.

## Mathematical result and boundary

The proof is `../ROUND_009_HAAR_NOISE_ENERGY.md`. It verifies the exact source constants from the full R5 proof, keeps the Coulomb collision-boundary flux with its sign without imposing a diagonal trace, proves the nonpositive quadratic form of both actual homogeneous response operators, and obtains the uniform-in-N energy constant without an N-dependent derivative constant. It then proves the exact deleted-label Haar identity, the two scaled reference-noise rates, and the complete four-term exchangeable-law identity, including N=2.

For actual iid-Haar-prepared particles, uniqueness and equivariance establish exchangeability and one-body Haar marginals. These symmetries do not establish product higher marginals. Equations (10.2) and (10.3) isolate the remaining signed pair/triple/mixed marginal error and a sufficient absolute law-transfer obligation. Neither its uniform estimate nor actual bracket smallness is proved. Fixed-N exponential density domination is retained explicitly and is insufficient for that transfer. No fluctuation theorem, full subcritical beta-to-zero theorem, or critical hierarchy closure is asserted.

There is no unresolved line in the claimed conditional THM029 implication. Its domain prerequisite is externally conditional; the next open estimate beyond this gate is the law error in (10.2), or the stronger sufficient bound in (10.3).

## Contents

- `../ROUND_009_HAAR_NOISE_ENERGY.md`: full conditional proof, source constants, falsification checks, exact law reduction, and claim dispositions.
- `round009_haar_energy_exact.py`: new exact diagnostic with no prior checker import.
- `ROUND_009_ENERGY_EXACT_RESULTS.json`: issued result, **PASS, 52,103 exact assertions**, Python 3.9.6.
- `README.md`: this handoff and verification procedure.
- `ROUND_009_ENERGY_INPUT_SHA256SUMS.txt`: nineteen root-relative input hashes.
- `ROUND_009_ENERGY_OUTPUT_SHA256SUMS.txt`: five root-relative output hashes, excluding itself.
- `ROUND_009_ENERGY_SEALED.zip`: the nineteen exact inputs, five named outputs, and output manifest, 25 members total; no inherited unrelated worktree files.
- `ROUND_009_ENERGY_SEAL_SHA256SUMS.txt`: artifact-directory-relative archive/output-manifest hashes, excluding itself.

The diagnostic enumerates N=2,3,4 for exact four-node trigonometric quadrature, correlated invariant densities and finite-label contractions, with separate Fourier-orthogonality and biased-law checks for the mixed coefficient. It checks source/energy exponents, physical normalization, backward Fourier and energy signs, zero noise, constant h, both response slots, and the Coulomb flux. The absolute-cross quadrature checks discrete Cauchy–Schwarz only; the continuous absolute bound is proved in the memorandum. No random seed or floating-point tolerance is used.

A pre-seal checker attempt failed a coverage assertion because the initial first-frequency invariant test family annihilated the mixed contraction. The test suite was enlarged, not the theorem weakened: it now exercises nonzero mixed terms, including a separate common-translation-invariant example with Haar one-body marginals. This was a diagnostic coverage failure and is disclosed in the proof. The final issued run passes.

These calculations support the exact algebra; they do not independently certify the analytic argument, the domain prerequisite, or the unproved actual-law transfer.

## Reproduce and verify

From the worktree root, first verify the issued bytes:

```sh
shasum -a 256 -c MEMORANDA/ROUND_009_ENERGY_ARTIFACTS/ROUND_009_ENERGY_INPUT_SHA256SUMS.txt
shasum -a 256 -c MEMORANDA/ROUND_009_ENERGY_ARTIFACTS/ROUND_009_ENERGY_OUTPUT_SHA256SUMS.txt
```

From this artifact directory, verify the outer seal:

```sh
shasum -a 256 -c ROUND_009_ENERGY_SEAL_SHA256SUMS.txt
```

After preserving or verifying the issued result bytes, rerun from the worktree root:

```sh
python3 MEMORANDA/ROUND_009_ENERGY_ARTIFACTS/round009_haar_energy_exact.py
```

The checker writes the result JSON beside itself. A different interpreter version can change its metadata and hence its digest without changing the assertion count. Prefer extracting a separate reproduction copy if the issued sealed worktree must remain byte-identical.

The archive CRC, all 25 member hashes against their corresponding loose files, all nineteen input hashes, all five output hashes, the branch/base, and the proof display delimiters were verified before handoff. The output manifest excludes itself; the outer seal is deliberately outside the archive to avoid a hash cycle. A later correction must be a new superseding artifact, not an edit of this issued proof or seal.
