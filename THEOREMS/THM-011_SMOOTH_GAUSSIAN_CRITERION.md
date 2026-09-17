# THM-011 — fixed-smooth finite-dimensional Gaussian covariance criterion

Version 1.0, 2026-09-17. Mathematical status PROVED_CANDIDATE; audit SELF_CHECKED at submission. Later verdicts belong in the theorem ledger. Full proof: MEMORANDA/ROUND_002_SMOOTH_GAUSSIAN.md, SHA-256 7c581d5d9a34f7e0fd277c183321e4b789f10fe11e265e27cc461a2a2352438e.

Use exactly the iid fixed-smooth model, full backward kernels and uniform C^(4d+12) assumptions from PO-001_RESIDUAL.md. Fix any finite list of terminal times t_a in [0,T] and real smooth terminal tests phi_a. For each terminal time use its own backward f_a^N and zero-terminal pair corrector on [0,t_a]. Write a_N=sigma_N/sqrt N and c_N=sigma_N^2/(N beta_N), with sigma_N=min(sqrt(N beta_N),sqrt N).

Let I_N^{ab}=a_N^2 Cov_mu0(f_a^N(0),f_b^N(0)) and D_N^{ab}=2 c_N integral_0^min(t_a,t_b) mu_r^N(grad f_a^N(r).grad f_b^N(r)) dr. If these deterministic matrices converge entrywise to I,D, the vector (sigma_N rho_(t_a)^N(phi_a))_a converges in distribution to the centered, possibly degenerate Gaussian with covariance I+D. More precisely the initial linearized vector and its leading martingale vector converge jointly to independent Gaussian vectors of covariance I and D.

The proof provides an L2 corrected remainder O(N^-1/2), mean-field bias O(N^-1) before fluctuation scaling, L1 bracket replacement O(N^-1/2), and a joint characteristic-function approximation with O(N^-1/2) error for each fixed pair of arguments before covariance convergence is taken. True bounded complex exponential martingales justify factorization against every bounded initial-measurable variable. The initial triangular iid characteristic expansion and the final smoothing passage are displayed rather than imported as a martingale CLT.

Exact negation: permitted fixed smooth data and a temperature sequence with the stated uniform bounds and convergent I_N,D_N for which that convergence or joint independence conclusion fails. Arbitrarily oscillating temperatures need not produce convergent covariances; the free time-zero cosine example in the proof gives distinct subsequential limits.

For beta_N->0, the full-response backward energy identity forces I_N,D_N->0 under the stated bounds, and the vector converges to zero in L2. For beta_N->infinity, the dynamical noise covariance tends to zero; identification of I still needs convergence of the backward kernels or covariance. No zero-diffusivity PDE limit is part of this submitted theorem.

This theorem concerns a fixed finite list and fixed smooth kernels. No field/path tightness, growing list, singular cutoff passage, Gibbs preparation, effective critical power counting, or complete M3 gate is claimed. No unavailable private or unverified literature theorem is used. The proof uses the independently constructed residual estimate of TASK-011; this new theorem itself still requires independent review.
