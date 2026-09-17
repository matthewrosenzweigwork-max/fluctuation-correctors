# Round 001 analytic audit: sealed statement-only reconstruction

- Audit component: independent analytic reconstruction for `TASK-009`, `THM-008`.
- Baseline: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Worktree: `/private/tmp/hocf-round001-analytic-audit-20260917`.
- Reconstruction saved: 2026-09-17T18:35:37.190838+00:00.
- The model and `MEMORANDA/ROUND_001_SMOOTH.md` through Section 1 were read before this document was written. Section 2 and every subsequent section had not been read when this document was saved. No other constructor output or constructor conversation was read.
- Isolation is **statement-only isolation**. The statement disclosed the proposed constants, their definitions, the claimed estimate and the stated scope. This is not a reconstruction made without knowledge of those constants. The argument below was reconstructed without the candidate proof narrative.
- The frozen input manifest was checked with `shasum -a 256 -c AUDITS/HOSTILE/ROUND_001_ANALYTIC_INPUT_SHA256SUMS.txt`: four files passed. The candidate memorandum hash is `934538be3fdb83d5949d5059abb65d9834064539a4d3006d2ca99a528089eb1f`.
- This document is sealed before candidate-proof comparison. It is not a final hostile verdict and will not be edited after comparison.

## 1. Exact assertion and alternative

For the smooth frozen periodic model, prescribed nonnegative mass-one background, every integer N at least two, and every nonnegative diffusion coefficient, the terminal pair equation in statement (1.3) has a unique mild C^m solution, smooth in space, with the claimed componentwise C^m estimate (1.4). Symmetric forcing produces a symmetric solution. Parameter uniformity means that only the explicitly displayed actual coefficient, background and forcing norms enter the bound.

A failure would be permitted smooth data for which this existence, uniqueness, symmetry, or precise bound fails. No assertion about removal of a singular cutoff is part of this alternative.

## 2. Local operator and derivative count

Write the pair variable as Z=(x,y) on the 2d-dimensional torus and set

\[
 a_t(Z)=\bigl(u_t(x)+N^{-1}K(x-y),\;
                 u_t(y)-N^{-1}K(x-y)\bigr),\qquad
 A_t=a_t\cdot\nabla_Z+\nu\Delta_Z.
\]

All component derivatives of a_t of total order at most m are bounded by

\[
 A_m=b_m+(1+1/N)\kappa_m\le b_m+\tfrac32\kappa_m.
\]

Indeed, derivatives of K*mu can be placed entirely on K; nonnegativity and unit mass give the bound kappa_m without derivatives of mu. A mixed derivative of K(x-y) is one signed derivative of K of the same total order. The estimate includes order zero.

For each multiindex alpha of order at most m,

\[
 [\partial^\alpha,a_t\cdot\nabla]h
 =\sum_{j=1}^{2d}\sum_{0<\delta\le\alpha}
  {\alpha\choose\delta}(\partial^\delta a_{t,j})
              \partial^{\alpha-\delta+e_j}h.
\]

Every derivative of h on the right has order at most m. Since the sum of the indicated multinomial coefficients is 2^{|alpha|}-1,

\[
 \|[\partial^\alpha,a_t\cdot\nabla]h\|_\infty
 \le 2d(2^m-1)A_m\|h\|_{C^m}.
\]

There is no commutator with the constant diffusion coefficient.

## 3. Response bound, including all mixed derivatives

Let beta be the x multiindex and gamma the y multiindex, with |beta|+|gamma| at most m. For the x-response there are two distinct cases.

If |beta| is positive, differentiate under the integral without integration by parts:

\[
 \partial_x^\beta\partial_y^\gamma R_{x,t}h
 =(-1)^{|\beta|}\sum_{j=1}^d\int
 (\partial^\beta K_j)(z-x)
 (\partial_{z_j}\partial_y^\gamma h)(z,y)\mu_t(z)\,dz.
\]

The derivative of h has order 1+|gamma| at most m. Thus this case is bounded by d kappa_m times the C^m norm of h, with no derivative of mu.

If beta is zero, gamma can have order m and the preceding expression would lose a derivative. Instead integrate by parts in z before estimating:

\[
 \partial_y^\gamma R_{x,t}h
 =-\sum_{j=1}^d\int \partial_y^\gamma h(z,y)
 \bigl[(\partial_jK_j)(z-x)\mu_t(z)
                  +K_j(z-x)\partial_j\mu_t(z)\bigr]dz.
\]

This case is bounded by

\[
 (d\kappa_1+\kappa_0M_1(t))\|h\|_{C^m}
 \le(d\kappa_m+\kappa_0M_1(t))\|h\|_{C^m}.
\]

Interchanging x and y gives the same bound for R_y. Hence, with R=R_x+R_y,

\[
 \|R_th\|_{C^m}
 \le 2(d\kappa_m+\kappa_0M_1(t))\|h\|_{C^m}.
\]

It is essential not to integrate by parts indiscriminately after beta derivatives: that would unnecessarily introduce derivatives of K of order m+1 and higher kernel derivatives multiplied by M_1. The two-case calculation verifies the smaller stated constant, including mixed derivatives.

## 4. Existence independent of the derivative estimate

For a fixed diffusion coefficient, the local transition operator P_{t,s} associated with A_t exists via

\[
 dZ_r=a_r(Z_r)dr+\sqrt{2\nu}\,dW_r,\qquad Z_t=Z.
\]

One can construct it directly: lift the periodic coefficients to Euclidean space, subtract the continuous Brownian translation, and solve the resulting random integral equation with a uniformly Lipschitz drift. Picard iteration converges on short intervals, uniqueness follows from the elementary integral inequality, and concatenation covers the finite horizon. At nu=0 this is the deterministic characteristic flow. Spatial derivatives of the flow solve differentiated integral equations; smooth coefficient bounds on the compact time-space cylinder give every finite derivative needed, so differentiating expectations of smooth test functions is justified by deterministic bounds. This yields spatial regularity without using smoothing or inverse powers of nu.

A smooth solution of the local backward equation, reversed to forward time, satisfies the maximum-principle estimate

\[
 \|P_{t,s}h\|_{C^m}
 \le e^{\ell_m(s-t)}\|h\|_{C^m},\qquad
 \ell_m=2d(2^m-1)A_m.
\]

The justification for the exact value of ell_m is the commutator calculation above and the maximum-principle argument below. For general C^m data, periodic smooth approximation extends P continuously with the same bound.

The full equation is the Volterra equation

\[
 \Phi_t=\int_t^T P_{t,s}(F_s+R_s\Phi_s)\,ds.
\]

The response is a bounded operator on C^m with integrable norm bound R_m(s). Repeated substitution gives a convergent time-ordered series: after factoring the local exponential, the n-th response insertion is bounded by the n-th power of the integrated response bound divided by n factorial, times the corresponding forcing integral. This constructs a unique continuous C^m mild solution. Applying the construction in each larger integer C^q space and using uniqueness in C^m shows that the same solution is spatially smooth. With continuous coefficient and forcing derivatives, the integral equation gives the classical time equation in any fixed lower spatial norm. The argument works for every fixed finite nu, and the displayed norm bounds contain no nu.

## 5. Maximum principle and the direction of time

Set tau=T-t and psi_tau=Phi_{T-t}. Then

\[
 \partial_\tau\psi=A_{T-\tau}\psi+R_{T-\tau}\psi+F_{T-\tau},
 \qquad\psi_0=0.
\]

Thus the diffusion has the nonnegative forward sign. For each spatial derivative w_alpha, the differentiated equation has local drift and diffusion applied to w_alpha, plus the commutator, differentiated response and differentiated forcing. At a maximum of the signed component w_alpha, the drift contribution vanishes and the diffusion contribution is nonpositive. The same applies to its negative. Compactness and the finite number of alpha show that the upper right Dini derivative of H(tau)=max_alpha ||w_alpha||_infinity obeys

\[
 D^+H(\tau)\le c_m(T-\tau)H(\tau)+\|F_{T-\tau}\|_{C^m}.
\]

This argument applies also at nu=0; no strict ellipticity is invoked. The scalar integrating-factor comparison gives

\[
 \|\Phi_t\|_{C^m}
 \le\int_t^T\exp\left(\int_t^s c_m(r)dr\right)
                \|F_s\|_{C^m}ds.
\]

The bounds from the local evolution and the response Volterra equation give the same formula. In both methods the exponent is integrated from t to the forcing time s, not from s to T.

## 6. Symmetry and campaign forcing

Under the swap (x,y)->(y,x), the two background drifts exchange. Oddness of K makes the internal drift equivariant under the same swap, and the two response terms exchange. Uniqueness therefore implies pair symmetry for symmetric forcing and zero terminal data.

For J_f=K(x-y) dot (gradient f(x)-gradient f(y)), total-order Leibniz differentiation gives at most 2^m terms weighted by binomial coefficients, d component terms, and a bound 2||f||_{C^{m+1}} on the differentiated gradient difference. Thus

\[
 \|J_f\|_{C^m}\le d2^{m+1}\kappa_m\|f\|_{C^{m+1}}.
\]

It is symmetric and vanishes on the coordinate diagonal. Symmetrization of the quadratic pairing against a signed measure gives one half of the J_f pairing because K is odd. For this particular kernel deleted-label and full-product quadratic pairings agree because J_f(x,x)=0. This verifies the stated factor of two at the level needed for the forcing bound; it is not an audit of the full particle hierarchy.

## 7. Reconstruction outcome before proof comparison

The proposed fixed-smooth estimate and its exact constants are recovered from the frozen definitions. No extra restriction on nu, positive lower bound on mu, higher background derivative norm, or hidden N-dependent coefficient was necessary. Higher smoothness of the prescribed data is used to construct classical solutions, while only the displayed low-order norms enter the C^m estimate.

This does not certify the candidate proof, its solvable-model test, or the singular cutoff diagnostic; those sections were not read before this reconstruction was sealed. It also does not establish cutoff-uniform estimates, a fluctuation theorem, closure of a corrector hierarchy, or an estimate for an unspecified one-body test.
