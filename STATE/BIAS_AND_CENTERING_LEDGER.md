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
