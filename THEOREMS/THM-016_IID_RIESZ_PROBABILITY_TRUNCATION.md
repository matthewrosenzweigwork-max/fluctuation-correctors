# THM-016 — an initial iid Riesz pair estimate beyond the L2 range

2026-09-17. Frozen statement from the independently constructing TASK-022 route. Mathematical status PROVED_CANDIDATE, audit pending. The assertions below require the complete self-contained heat representation and truncation proof; this card is not itself evidence of a proof.

On the unit d-torus let X_i be iid Haar, N>=2, and let 0<s<d. Define the mean-zero Riesz potential by the frozen Fourier coefficient and its off-origin heat representation. It has local principal singularity |x|^(-s) and a bounded smooth remainder near the origin. The ordered pair statistic is P_N[g]=(2N^2)^(-1) sum_(i!=j) g(X_i-X_j), finite almost surely and integrable. Its expectation is zero. Its second moment is finite exactly when 2s<d; at 2s>=d it is infinite for every finite N>=2.

Nevertheless sqrt(N) P_N[g] tends to zero in probability when 0<s<3d/4. More generally, for d/2<s<d, sigma_N P_N[g] tends to zero in probability whenever b_N N^(4s/d-3) tends to zero, where b_N=min(beta_N,1) and sigma_N=sqrt(N b_N). For s<=d/2 the conclusion at sigma_N holds for every positive beta_N sequence. The endpoint s=d/2 requires truncation; its infinite variance does not preclude convergence in probability.

The proof must separately bound the probability of a pair within distance r, the deterministic mean discarded by truncation, and the variance of the centered truncated statistic; it must exhibit a valid r_N and the order of limits. Exact negation: an admissible iid instance or sequence satisfying these conditions violates the stated integrability or probability conclusion. No converse, sharp probability threshold, stable law, or endpoint nonconvergence is claimed.

This is an initial iid bare-potential result. It neither identifies g with the actual backward corrector nor transfers to positive-time interacting/Gibbs laws. It does not compare singular and heat-regularized particle dynamics. These conditions are not replacements for the campaign's old energy-floor, full-subcritical lambda_N, or critical lambda_N regimes. The logarithmic model is excluded.
