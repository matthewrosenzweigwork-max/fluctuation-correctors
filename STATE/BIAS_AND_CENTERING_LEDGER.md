# Bias and centering ledger

| ID | Observable/law | Raw centering | Correction scale | Formula/status | Required accuracy | Proof |
|---|---|---|---|---|---|---|
| BC-001 | linear statistic, iid initial law | mean field | finite-N diagonal bias | to derive | \(o(\sigma_N^{-1})\) after residual centering | — |
| BC-002 | moving modulated Gibbs law | mean field | pressure/free-energy response | to derive | theorem-dependent | — |
| BC-003 | exact exchangeable law | exact first marginal | zero by definition | exact | baseline comparison | — |
| BC-004 | pair statistic | product-background centering | Wick/diagonal contraction | to derive | finite at cutoff removal | — |
| BC-005 | critical hierarchy | lower-order cumulant counterterms | all orders possible | to derive/resum | uniform in truncation order | — |

Every convergence theorem must identify its row and prove the difference from any more explicit centering at the stated fluctuation scale.


## Round 001 exact distinctions

For iid mu_0 data, E rho_0(f)=0, E U_2[Phi]=-mu_0^2(Phi)/N and E U_3[F]=2mu_0^3(F)/N^2. These are preparation-time identities; interacting evolution does not preserve iid sampling. For the exact marginal m, with delta=m-mu, U_2^mu=U_2^m+2(eta-m) tensor delta+delta tensor delta, tested against the same symmetric Phi. Exact-marginal centering therefore cannot be substituted without recomputing dynamics. The dynamic mean-field bias (BC-001), pressure response (BC-002), and critical centering (BC-005) remain OPEN. Evidence: BBGKY (4.7)-(4.9).

## All-order finite iid bias

For iid mu at a single instant, E U_k[Phi] equals mu^k[Phi] times sum_{r=0}^k (-1)^{k-r} binomial(k,r) (N)_r/N^r. The first four coefficients are 0, -1/N, 2/N^2, 3/N^2-6/N^3. This is not a dynamic iid assertion. For exchangeable evolved law replace mu^r in each occupied term by its actual r-point marginal f_r. Exact first-marginal centering and moving Gibbs centering remain separate OPEN bridges.

## Round 002 fixed-smooth iid centering

THM-010 retains the initial pair bias and proves its absolute O(N^-1) bound. The two lower drift contractions also have integrated absolute O(N^-1) bounds, so multiplying by sigma<=sqrt N makes them vanish. Evolved particles are not assumed iid: the nonzero-interaction diagnostic in ROUND_002_FALSIFICATION.md (7.1) creates pair bias instantly at order N^-1 despite a uniform first marginal. TASK-014 will identify the resulting mean-field-centered finite-dimensional limit under explicit covariance convergence. Moving Gibbs, singular and critical pressure centering remain OPEN.

Round 002 review update: AUD-006 now grants HOSTILE_REVIEW_PASS for the bounded residual estimates, fixed-data norm qualification and Gibbs law-class obstruction in the precise scopes above. The singular and other open interfaces are unchanged.

## Round 002 final integration

Round 002 THM-011/AUD-007 and statement-only AUD-008 both prove O(N^-1) mean-field bias for a fixed finite smooth test list, with uniform temperature constants; scaling by sigma_N leaves O(N^-1/2). The independent reconstruction uses the zero-diagonal quadratic one-body source directly. Initial/martingale asymptotic independence comes from conditional characteristic functions, not merely zero cross covariance. THM-013 identifies initial limiting backward covariances at zero diffusivity. Singular, Gibbs and exact-marginal centering comparisons remain OPEN.

## Round 003 exact pair centering

For symmetric Phi=theta+h(x)+h(y)+H(x,y), theta=mu^2(Phi), mu(h)=0 and H canonical, P_N[Phi]=-theta/(2N)-N^-2 sum_i h(X_i)+N^-2 sum_(i<j)H(X_i,X_j). The first projection and deterministic mean do not vanish merely from iid sampling. The exact second moment is theta^2/(4N^2)+||h||_2^2/N^3+(N-1)||H||_2^2/(2N^3). THM-015, AUD-011/012.

For hard spatial truncation h_r=g 1_(dist>=r), m_r=int h_r=-tau_r, k_r=h_r-m_r, the no-close-pair identity is P_N[g]=P_N[k_r]+(N-1)m_r/(2N). The full background-centered statistic P_N[h_r] instead differs from the centered sum by -m_r/(2N). THM-016/AUD-012/013 retains both distinctions. THM-017 retains nonzero density-dependent mean and first projection in its endpoint estimate; radial/traceless mean cancellation is used only in its explicitly Haar case.

## Round 004 diffusive diagnostic centering

THM020's initial iid endpoint keeps -m/(2N), the first projection -N^-2 sum q(X_i), and the canonical unordered pair sum. Its exact second moment is the THM015 identity; arbitrary finite spatial-diagonal assignment is irrelevant only because this iid law has bounded density. Supremum over deterministic remaining times and finite nu is outside expectation. No exact expectation-centering or evolved law is substituted.

Round004 response integration does not change mean-field centering or N^2 normalization. Coulomb negative Haar compensation is part of divK, not a new fluctuation centering. Root R5 conditional composition retains the exact THM015 mean and first projection; its iid estimate is conditional pending independent audit/input verification. No exact-centered law is silently substituted.

R5 actual full-inverse initial estimate retains deterministic -theta/(2N), first projection and canonical pair components from THM015. It is mean-field centered, with M0^2 in the Haar-to-product L2 comparison. No exact-first-marginal or dynamic corrected centering has been substituted.

R8 exact particle identity retains mean-field centering with q(x)=integral Phi(x,y)dy and r=integral Phi. P[Phi]=(2N^2)^-1 sum_(i!=j)Phi_ij-N^-1 sum_i q_i+r/2. No exact-law recentering or new counterterm. Its gradient is N^-2 sum_(j!=i) grad_x Phi_ij-N^-1 grad q_i, including the finite-N background deletion.

R9 keeps the exact finite-N deletion in grad_iP=N^-2[sum_(j!=i)H_ij-A_i], H=G-A and A=integral Gdy. Haar conditional centering cancels only distinct H products and mixed H-A averages under product Haar. Additive kernels leave ||A||2^2/N^3 in the summed gradient square. Actual one-body Haar cancels the A-square difference between laws, not the pair/triple/mixed differences. No centering or denominator changes.


R10 proves exact actual E P[Phi]=0 using the vanishing common-translation orbit average of the genuine full inverse and the actual invariant law; scalar Haar mean zero alone is insufficient. This exact expectation is not concentration. Radial clipping uses its own mean A^L, and the residual uses A-A^L. Fourier smoothing retains the exact smooth self-diagonal term. No renormalization, denominator or centering convention changes.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 changes no centering: mean-field Haar background remains. One-body Haar controls only its actual background square; the full pair is not assumed independent. An actual noise estimate does not upgrade R10 exact zero mean to endpoint concentration. Initial terminal-zero-corrector contribution is separately controlled at iid time zero by R5.

R13 preserves exactly P_N=U2/2 and mean-field Haar centering. Radially clipped and tail fields each use their own row A; full gradient is N^-2(sum G-N A), retaining the missing-self subtraction after centering. Noise smallness proves no evolved residual centering. THM035 now freezes both lower and scalar drift terms; neither may be silently dropped.


Round014 final gate,2026-09-18 UTC. R14 lower bound is pathwise for any empirical probability measure once the same genuine contractions are fixed; actual dynamics enter the separate R8 domain identity. Both mean-field-centered/scalar terms are retained, even if special structural cancellation exists. One-body Haar equivariance is true but does not imply higher-marginal independence. No centering change.


Round015 final gate,2026-09-18 UTC. R15 keeps mean-field Haar centering and all explicit scalar/linear contractions. Actual source bound uses E|PJ|, not signed mean-zero symmetry. Initial iid pair second moment includes m^2/(4N^2) bias, first projection/N^3 and degenerate pair coefficient(N-1)/(2N^3). Product sampling is used only initially; no evolved iid endpoint.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R17 conditional finite-list implication derives exact one-body Haar centering from common translations and unique measurable actual realization. Initial iid is used only for zero-mean triangular-test replacement and initial Gaussian vector. No correction or positive-time factorization. THM040 separately requires the same exact centering and retains dependence between thermal martingale and initial data until its limit is proved.


R17 final gate,2026-09-18 UTC. R17 exact actual Haar centering and absence of additional counterterm are accepted in its finite-dimensional critical scope. Initial triangular-test mean is exactly zero. Higher marginals are not independent, and no new centering in THM040/041 is approved by this gate.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 independently reconstruct exact one-body Haar centering from common translations and uniqueness. Positive-time product Haar is not claimed; no deterministic counterterm added.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.


2026-09-18 R21 acceptance: R21 retains exact Haar one-body centering and every cubic/background and lower contraction. It changes neither centering nor deterministic counterterms. R23 pending static-law construction preserves Haar one-body marginals but is not an iid-flow law. See AUDITS/ROUND_021_GATE_INTEGRATION.md.
