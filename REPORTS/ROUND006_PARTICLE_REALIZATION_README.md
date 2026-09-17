# TASK-045 constructor handoff

2026-09-17 UTC. Status: **PROVED_CANDIDATE / SELF_CHECKED**, awaiting fresh reconstruction and hostile review.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r006-particle-domain`.
Branch: `codex/hocf-r006-particle-domain`.
Base commit: `52bda5d0d24067b051c6fe9763f2a78e7599e593`.
Constructor: `/root/r006_particle_domain`.

The complete mathematical construction is `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`. It proves the stated finite-N singular particle realization and heat passage for the frozen periodic Riesz normalization, smooth gradient background, d at least 3, positive s at or below Coulomb, and every finite nonnegative diffusivity. It includes exact stopped and global energy identities, collision-distance exit bounds, joint measurable Markov laws, and the density exponent `N a+(N-1) kappa`. Every partial collision is controlled by a nonnegative shifted pair-energy summand. No individual-force-square estimate or false sign assumption on triple cross terms is used.

The source dossier consists of exactly the six files in `AUDITS/ROUND_006_PARTICLE_REALIZATION_INPUT_SHA256SUMS.txt`. The task, AGENTS, frozen R1 model, THM-021 card, sealed R4 response proof, and sealed R5 periodic-pair proof were copied byte-for-byte from the assigned root and checked before and after copying. R5 is explicitly credited as an analogous method, not an N-particle theorem. No unlisted state, history, memory, or worker output was read. The parent/root worktree remains untouched by this worker.

Created construction outputs:

- `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md` — complete proof, exact constants, law class, source preflight, falsification checks, exclusions, and the next unsupported domain line.
- `VERIFICATION_CODE/round006_particle_realization_exact.py` — standard-library exact rational coefficient and solvable-model checks.
- `VERIFICATION_CODE/round006_particle_realization_exact_output.json` — 2,631 passing checks across 96 differentiated local models; N=2,3,4, additional counting values, zero diffusivity, Coulomb and sub-Coulomb exponents, triple cancellation, and disjoint close pairs.
- `AUDITS/ROUND_006_PARTICLE_REALIZATION_VERIFICATION.json` — input integrity, output structure, Python parse, equation-label/reference, and whitespace verification.
- `AUDITS/ROUND_006_PARTICLE_REALIZATION_OUTPUT_SHA256SUMS.txt` — output seal; it does not include itself.
- This README.

Verification commands, run from this worktree:

```sh
python3 VERIFICATION_CODE/round006_particle_realization_exact.py
shasum -a 256 -c AUDITS/ROUND_006_PARTICLE_REALIZATION_INPUT_SHA256SUMS.txt
git diff --check
shasum -a 256 -c AUDITS/ROUND_006_PARTICLE_REALIZATION_OUTPUT_SHA256SUMS.txt
```

The exact checker uses no floating-point arithmetic, random seed, tolerance, new dependency, or numerical simulation. It independently differentiates a raw local energy using rational jets and compares that result with an explicitly assembled force, divergence, and full square including all triple terms. Its Euclidean powers and polynomial backgrounds are differential-coefficient tests; periodic compensation and the singular construction require the written proof. It is supporting same-context evidence, not an independent mathematical certificate.

Because new files are untracked, an additional direct scan verifies terminal newlines, trailing whitespace, control characters, balanced display delimiters, unique equation labels, and all in-memorandum numbered equation references. The checker source is parsed without writing bytecode. Those checks are recorded in the verification JSON. No TeX is modified or created, and the final handoff contains no mathematical LaTeX, so there is no TeX build in this lane.

No unsupported line remains in the finite-N assertion as constructed, subject to fresh audit. The next unresolved mathematical line is interacting N-particle Itô calculus for the empirical pair statistic of a merely bounded Borel or Haar-L2 pair inverse. This task does not supply its derivatives, differentiated background contractions, extended generator identity, bracket convergence, or N-uniform evolved residual estimates. No corrector-domain or fluctuation-theorem promotion is authorized by the finite-N result alone.

No canonical identifier or state ledger was changed. No root edit, commit, merge, push, dependency installation, or child agent was used. Root should integrate only after the sealed construction has undergone the required separate reconstruction and hostile review.
