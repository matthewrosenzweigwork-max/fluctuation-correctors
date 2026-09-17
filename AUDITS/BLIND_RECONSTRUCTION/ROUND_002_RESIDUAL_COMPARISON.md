# AUD-005 — isolated residual reconstruction comparison

2026-09-17. Root Astra Ultra compares independently sealed constructions; this is not a root certification of its own proof. Input checkpoint a06178658d1e3d458536ff312ca793947212ec67. The frozen statement is PO-001_RESIDUAL.md; THM-010 is its quantitative candidate card. Mathematical scope is exactly the fixed-smooth iid residual, not its singular extension.

## Isolation and immutable inputs

- Constructor /root/r002_coupling received TASK-010 in a separate worktree at the published checkpoint. Sealed report MEMORANDA/ROUND_002_COUPLING.md, SHA-256 7eb57c1f4e8f6da9c80a2f53a95349153605467532afb33b269938b242761852.
- Independent falsifier/reconstructor /root/r002_falsification received only TASK-011, the same frozen statement/model and earlier audited algebra. It did not receive or read the constructor report. Its independent full proof was sealed before any later task: MEMORANDA/ROUND_002_FALSIFICATION.md, SHA-256 125317981b543cf83a47a64efc1455453fbd942e476a52b15e64ec984c216856.
- These are separate fresh Astra Max contexts and worktrees. Both chose synchronous coupling after receiving the available route options. Thus they are independent constructions using related probabilistic mechanisms; they are not two unrelated proof strategies, and no closed BBGKY estimate has been proved by this comparison.

## Decisive comparison

Both constructions use iid nonlinear comparison particles with deterministic drift b+K*mu and identical Brownian paths to their interacting partners. Constructor (4.6)–(4.9) controls the empirical H^(-q) norm using a pathwise average displacement and an iid Hilbert sixth moment. Reconstructor (3.2)–(3.7) instead uses conditional centered finite sums for each root particle, a sixth-moment displacement estimate, and Fourier-mode moments. Neither assumes evolved independence of the interacting law. All constants are independent of beta because the Brownian parts cancel exactly. Neither estimates a time supremum inside expectation uniformly in diffusion.

Both derive the same exact cubic identity: rho^3[F] minus 3/N times (eta tensor rho)[F(x,x,y)] plus 2/N^2 eta[F(x,x,x)]. Both retain the random partial diagonal and root-exclusion subtraction in the pair gradient. Constructor treats the cubic by tensor Sobolev duality with q=floor(d/2)+2; reconstructor uses absolutely summable Fourier coefficients at total derivative order 3d+4. Both are within the frozen 4d+12 assumption. The reconstructor additionally obtains L2 cubic and pair bounds; agreement of rates does not assert equality of the two different explicit constants.

Both derive pair bracket 2/(beta N^2) sum_i integral |H_i|^2 and cross bracket with grad f(X_i). Both get raw rates N^-1, N^-3/2, beta^-1 N^-2 and beta^-1 N^-3/2. After the precise sigma scaling they are uniformly vanishing for every beta_N>0. The identity sigma^2/(beta N)=min(1,beta^-1) is recomputed in both reports. The lower drift remains O(sigma/N). Iid expectation centering is never substituted for mean-field centering.

The two report-specific solvable batteries include nonzero interaction, moving nonuniform backgrounds, N=2,3 and beta endpoints. Root reran the independent exact rational falsification battery: 116 checks PASS. These tests support but do not replace the general proofs.

## Disposition and limits

ISOLATED_RECONSTRUCTION_PASS for the exact asymptotic assertion in PO-001_RESIDUAL.md and the shared quantitative orders of THM-010. Constructor-specific numerical constants still require the separate hostile review. The root norm-qualification lemma is not part of this reconstruction. A separate reviewer must also audit the new equilibrium law-class obstruction before its independent promotion.

No singular uniformity, critical power-counting theorem, finite/infinite critical closure, covariance limit, field tightness, or source normalization is certified here. Hostile review remains pending in this issued comparison. This report is immutable; subsequent verdicts belong in a new report and the canonical ledgers.
