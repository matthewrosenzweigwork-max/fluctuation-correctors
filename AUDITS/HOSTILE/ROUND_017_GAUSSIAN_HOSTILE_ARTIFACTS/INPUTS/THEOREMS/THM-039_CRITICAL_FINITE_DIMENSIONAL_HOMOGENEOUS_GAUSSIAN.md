# THM-039 — critical finite-dimensional homogeneous Gaussian fluctuations

2026-09-18 UTC. OPEN / UNAUDITED at statement freeze. This is a new bounded limiting-law target, not the campaign flagship and not inferred from a source estimate without the first-order identity and a probability limit proof.

Fix integer d>=3, 0<s<=d-2 with s<d/2, finite T>=0, and the frozen coefficient-one periodic Riesz kernel on the unit-Haar torus. Actual particles have zero external drift, K=-grad g_s, interaction coefficient 1/N and noise sqrt(2/beta_N), start iid Haar independently of their Brownian drivers, and beta_N is positive finite with lambda_N=beta_N N^(s/d-1) tending to lambda in (0,infinity). Write nu_N=1/beta_N, b_N=min(beta_N,1), sigma_N=sqrt(N b_N), eta_N(t)=N^-1 sum_i delta_(X_i(t)).

For every fixed positive integer m, deterministic t_1,...,t_m in[0,T], and fixed real smooth h_1,...,h_m, the R^m vector

    Z_N,j = sigma_N (eta_N(t_j)[h_j] - integral h_j dx)

converges in distribution to a centered (possibly degenerate) real Gaussian vector with covariance

    C_ij = integral (S_(t_i) h_i - integral h_i)(S_(t_j) h_j - integral h_j) dx,

where S_t preserves constants and multiplies nonzero Fourier mode k by exp(-t D_s(k)), D_s(k)=4 pi^2 c_(d,s)|k|^(s+2-d), c_(d,s)=pi^(s-d/2) Gamma((d-s)/2)/Gamma(s/2). Equivalently the covariance is the sum over k!=0 of hhat_i(k) conjugate(hhat_j(k)) exp(-(t_i+t_j)D_s(k)). The real-space formula fixes the real covariance even if the Fourier notation is complex.

The deterministic mean-field centering must be justified: the actual one-body marginal is exactly Haar at every deterministic time by common-translation equivariance and uniqueness. No pressure, Wick, free-energy or other counterterm is inserted. Joint convergence for different times, constant tests, repeated times, zero time and degenerate covariance is included. The limit is driven by the initial Haar Gaussian field propagated by S_t; no positive limiting thermal martingale is asserted at this critical scaling.

A quantitative sufficient approximation required within the proof is, for each j on every eventual critical tail,

    E |Z_N,j - N^-1/2 sum_(i=1)^N [S_(t_j)h_j(X_i(0))-integral h_j]| 
      <= C (N^(s/d-1/2) + sqrt(nu_N) + nu_N).

Constants may depend on the fixed tuple and on positive upper/lower bounds for lambda_N on its tail, but not N. Prove the genuine singular first-order identity from ordered sums and its fixed-N passage, bound the actual source rather than a product-law surrogate, retain the martingale coefficient, and justify the joint Gaussian limit of the initial iid vector. THM038 may be used only as an explicit conditional complete-source premise until its own gate passes; its construction is not presumed here.

Exact negation: an admitted fixed tuple/critical sequence violates any stated centering, approximation or weak-limit assertion. A failed proof or upper bound is not an admitted counterexample. No convergence in path space or distribution-valued topology, process tightness, growing list of tests, s=d/2, s>d/2, nonhomogeneous data, arbitrary preparation, logarithmic kernel, full subcritical law or higher hierarchy is asserted. Both response/corrector constructions and noise gates are nondependencies if the first-order route closes directly. Wider claims require new identifiers and gates.
