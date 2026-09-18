# TASK-049 constructor handoff

2026-09-17 UTC. Status: **PROVED_CANDIDATE / SELF_CHECKED**, pending fresh independent reconstruction and hostile review.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r007-weighted-gradient`.
Branch: `codex/hocf-r007-weighted-gradient`.
Base commit: `93c20daa45aad455a95437b1dc6beed2883afada`.
Constructor: `/root/r006_particle_domain`.

The complete construction is `MEMORANDA/ROUND_007_WEIGHTED_PAIR_GRADIENT.md`. It proves THM-027's fixed-N weighted first-derivative assertion for the genuine full pair inverse, including the Coulomb endpoint, zero diffusivity, and uniformity over the stated bounded diffusivity interval. It gives explicit coefficient choices for the weight inequalities, source occupation, response derivatives, Volterra series, and Haar H1 norm. The disclosed root route is identified as a construction seed rather than an independent audit.

The mathematical points requiring special care are handled explicitly:

- The principal pair Jacobian has positive transverse and negative radial eigenvalues. The proof uses its largest eigenvalue, not its larger absolute norm.
- A negative repulsive term absorbs the possibly positive diffusion term through an explicit finite maximum. The remaining negative term controls the derivative-source occupation.
- Higher moments and truncated path maxima yield a simultaneous local flow for nearby starts through a directly proved Morrey-type estimate. Uniform integrability then justifies finite-difference expectation derivatives and continuity. Pointwise path differentiation is not used as a substitute for this passage.
- The response convolution estimate treats both distinct singular points and their complement, and permits the two exponents to sum above the dimension. The Coulomb atom and compensation remain explicit.
- Response differentiation acts on both translated products, uses the second density derivatives, proves the global weak derivative first, and then proves continuity off diagonal.
- The pointwise Volterra series converges locally uniformly in derivatives. Its bounded Borel uniqueness identifies it with the existing full inverse without assuming a separable weighted sup space.

Exactly the fourteen source files in `AUDITS/ROUND_007_WEIGHTED_GRADIENT_INPUT_SHA256SUMS.txt` were copied and hash-checked before work. The task and THM-027 were read in full. No unlisted state/history, memory, other worker output, or external mathematical source was used. The earlier TASK-045 worktree and report seal were preserved.

Created outputs:

- `MEMORANDA/ROUND_007_WEIGHTED_PAIR_GRADIENT.md` — complete construction, hypotheses, constants, source preflight, falsification checks, and exclusions.
- `VERIFICATION_CODE/round007_weighted_gradient_exact.py` — standard-library rational checker for pair blocks, generators, diffusion absorption, response derivatives, Fourier/Coulomb factors, and exponent conditions.
- `VERIFICATION_CODE/round007_weighted_gradient_exact_output.json` — **5,992 passing exact checks**.
- `AUDITS/ROUND_007_WEIGHTED_GRADIENT_VERIFICATION.json` — source integrity and structural verification.
- `AUDITS/ROUND_007_WEIGHTED_GRADIENT_OUTPUT_SHA256SUMS.txt` — output seal, excluding itself.
- This README.

Verification commands, from this worktree:

```sh
python3 VERIFICATION_CODE/round007_weighted_gradient_exact.py
shasum -a 256 -c AUDITS/ROUND_007_WEIGHTED_GRADIENT_INPUT_SHA256SUMS.txt
git diff --check
shasum -a 256 -c AUDITS/ROUND_007_WEIGHTED_GRADIENT_OUTPUT_SHA256SUMS.txt
```

The checker uses rational/integer arithmetic only, with no tolerance, random seed, installed dependency, or numerical SDE inference. Its finite Fourier checks use dimensionless angle coordinates and divide out a common positive Riesz constant. The written source preflight retains the actual frozen torus/Fourier normalization. This checker and the structural checks are same-context evidence, not an independent audit.

Because new files are untracked, direct scans also verify terminal newlines, trailing whitespace, control characters, balanced display delimiters, unique equation labels, and all numbered in-memorandum equation references. The checker source is parsed without producing bytecode. No TeX file is created or modified, and the final handoff contains no mathematical LaTeX.

No first unsupported line remains in the frozen weighted first-derivative assertion as constructed, subject to independent audit. The next unresolved line is the full interacting particle Itô drift: the crude force-times-gradient majorant is nonintegrable at Coulomb for the permitted weights, and neither second/time derivatives nor the required directional cancellation or extended generator identity has been proved. The constants can deteriorate exponentially in a positive power of N; H1 therefore supplies no N-uniform bracket decay or evolved residual estimate.

No canonical identifier or state ledger was assigned or changed. No root edits, commits, pushes, dependency installation, or child agents were used. Root integration and independent review remain separate steps.
