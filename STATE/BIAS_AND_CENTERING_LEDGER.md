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
