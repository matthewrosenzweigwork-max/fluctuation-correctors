# Failed shortcuts, negative tests and scope

No attempted counterexample refuted the actual frozen THM053(A)–(B). The construction did identify and retain the following failures of possible proof routes.

| Attempt | First invalid inference | Repair or strongest justified statement |
|---|---|---|
| Use only the punctured constant Laplacian as a global distribution | Its integral is nonzero on the compact torus | Retain every negative collision atom and the positive Haar compensation |
| Read the exit law from the exact surviving marginal alone | A terminal limit and terminal observable identity have not yet been established | Prove first-power drift action, convergence of the lift and stopped smooth-test Itô |
| Infer convergence from compactness | Subsequence limits need not coincide | Use absolute drift variation and continuous Brownian displacement |
| Apply the repulsive energy identity to attractive H at collision | The sign changes and the force-square control is absent | Work with globally smooth bounded test functions whose gradients are bounded |
| Exclude higher collisions by a binary radial heuristic | Other singular forces in a collapsing cluster were not bounded | Identify the actual exit measure first, then exclude diagonal intersections by its support |
| Replace the full force square by the sum of pair squares | Cross terms need not vanish or be nonnegative | Retain the full force; only first-power triangle bounds are needed here |
| Derive full time/configuration independence from correct marginals | Coupled laws can have the same two marginals | Identify all time/configuration rectangles; an explicit positive coupled perturbation is tested |
| Infer the singular killing from a smooth attractive cutoff | The smooth process is conservative and has no genuine first-collision exit | Start with killed collision-free domains and prove exhaustion to the maximal singular lifetime |
| Use a global torus center of mass by dividing the coordinate sum by two | Division by two is not single-valued on the torus | Use full configuration-space tests; no global center choice is needed |

The complete analytic proof is in the memorandum. A distinct-form falsification route computed Fourier moments of the pair potential and the diagonal laws, transverse flux in orthonormal normal coordinates, derivatives in all configuration coordinates, the two-particle radial generator, and the temporal Laplace resolvent. No probabilistic simulation is used.

The exact executed mutation residuals are:

| Mutation | Exact nonzero residual |
|---|---:|
| Missing pair-coordinate factor two | -1/2 |
| Flipped collision atom | 4/3 |
| Omitted torus compensation | -2 |
| Wrong rate cN | -1/3 |
| Spurious diffusivity factor at diffusivity 3/7 | -4/7 |
| Halved relative diffusion at diffusivity 1/7 | 8/7 |
| Added triple-diagonal mass | 1/3 |
| Same marginals, wrong joint law | 1/24 |
| Deleted cross terms in the force square | -235298/3 |
| Surface measure mistaken for probability diagonal measure | 1/2 |
| Ordered pairs inserted into the unordered formula | 1 |

The coupled-law mutation uses the N equals 2 candidate product law, multiplied by the positive density `1 + (1/2)(2 exp(-kappa t)-1) cos(2 pi U_1)`. Each factor has zero mean in its respective marginal, so both marginals are retained. The joint test `exp(-kappa t) cos(2 pi U_1)` acquires value 1/24. This is a surrogate measure demonstrating a failed inference, not the law of the frozen SDE and not a counterexample to the theorem.

The triple mutation mixes in probability 1/3 of the full three-particle diagonal with a Haar common point. The three active Fourier frequencies `(e,e,-2e)` detect it although the genuine pair-diagonal exit law has zero such moment. This specifically challenges premature assumptions about binary support.

The deterministic Euclidean two-particle model has an explicit finite first-power action and divergent squared-force action at its collision. It has zero diffusivity and no periodic compensation and is outside the frozen hypotheses. The local polynomial compensation used for differential jets is also not the periodic kernel. Both are coefficient and false-strengthening diagnostics only. No analytic or asymptotic claim rests on the finite test count.

There were no failed executable mathematical tests: the first complete run returned exit 0 with 1,480 baseline checks and 11 detected mutations. The initial combined input display was truncated by the tool; bounded re-reads recovered every omitted portion, as recorded in the read history. No unavailable private source, external citation or mathematical premise is concealed.
