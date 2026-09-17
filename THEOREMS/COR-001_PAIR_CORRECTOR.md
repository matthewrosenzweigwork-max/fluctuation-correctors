# COR-001 — second-order smooth corrector

Date/version: 2026-09-17 UTC / 1.0. Algebraic status EXACT_REDUCTION; analytic candidate THM-009. Audit scope: AUD-001 isolated pair reconstruction; AUD-002 hostile pair review; AUD-003 independent analytic reconstruction and hostile review.

- Statistic: P_N[Phi]=U_2[Phi]/2, ordered distinct labels, denominator N^2, deterministic mean-field centering. No exact-expectation centering is imposed.
- Source: P_N[J_f], where J_f=(grad f(x)-grad f(y)) dot K(x-y), from the one-body backward observable.
- Equation: (partial_t+L_2+B/N)Phi=-J_f, Phi_T=0. Full response terms belong to L_2; B/N belongs to principal transport. Definitions are in THM-008 and the frozen model.
- Symmetry: preserved by operator and uniqueness. No separate mean-zero constraint is needed. J_f vanishes on the spatial diagonal; no diagonal vanishing of Phi is assumed or inferred.
- Generator output after correction: U_3[C Phi]+rho((B Phi)_mu)/N+mu^2(B Phi)/(2N). Initial endpoint P_N[Phi_0] remains.
- Martingale: sqrt(2/beta_N)/N sum_i integral H_i[Phi] dW_i; exact pair and one-body cross brackets are in THM-008. Deleted-label Brownian trace cancels; martingale does not.
- Scale: sigma_N=min(sqrt(N beta_N),kappa_N), iid kappa_N=sqrt N. Explicit lower drifts have deterministic bound O(sigma_N/N) at fixed uniformly smooth kernels. Cubic, endpoint and bracket bounds require the actual evolved law.
- Regularity: the explicit fixed-smooth C^m estimate is THM-009; no cutoff uniformity. Singular contractions and order of limits remain OPEN.
- Adjacent levels: COR-002 would cancel the U_3 source using the exact THM-001 hierarchy; its construction and tail estimates remain OPEN.
- Tests: N=2,3; nonuniform mu; constant and separable kernels; free heat/Fourier; full signed Fourier interaction; exact drift/gradient/bracket checks.
- First remaining estimate: TASKS/ACTIVE/PO-001_RESIDUAL.md. No finite truncation is assumed sufficient at critical scaling.
