# Counterterm and contraction ledger

| ID | Origin | Order | Formula | Regime | Regularization | Status | Cross-check |
|---|---|---:|---|---|---|---|---|
| CT-001 | deleted diagonal / iid quadratic bias | 2 | to derive | all | finite-N | OPEN | U-statistic vs empirical measure |
| CT-002 | Itô trace for pair corrector | 2 | to derive | positive temperature | cutoff-dependent initially | OPEN | explicit sum vs generator |
| CT-003 | critical UV/Wick term | 2+ | to determine | \(2s\ge d\) | heat/Fourier | OPEN | two schemes required |
| CT-004 | local pressure/free-energy centering | deterministic | to determine | moving background | local Gibbs | OPEN | static derivative vs dynamic stress |

Do not combine counterterms of different origins under one symbol.


## Exact smooth pair entries (Round 001)

- CT-001: U_2[Phi]=rho^2(Phi)-eta(Phi_diag)/N, P=U_2/2. At iid preparation E U_2[Phi]=-mu^2(Phi)/N. Exact diagonal subtraction is not automatically Wick centering or pressure renormalization.
- CT-002: the full-product P convention has the Ito drift nu*eta(tr D_xy Phi)/N. Differentiation of -eta(Phi_diag)/(2N) cancels it exactly. The pair martingale and all brackets remain. Scope is fixed smooth g/Phi, independent particle noises.
- Internal interaction: B Phi=K(x-y).(grad_x-grad_y)Phi. Its raw term D_2[B Phi]/(2N) equals P[B Phi]/N+rho((B Phi)_mu)/N+mu^2(B Phi)/(2N). No scalar contribution may be dropped.
- Proofs: algebra report (3.6)-(3.8), (4.9)-(4.16); independent BBGKY report (3.4)-(3.8), (5.1)-(5.6). Pair audit: AUD-001 isolated reconstruction passes; hostile pending. CT-003/004 singular and pressure terms remain OPEN.

## All-order accounting

The finite-subset derivation and full partial-bijection bracket expansion are equations (R1)–(R5) of MEMORANDA/ROUND_001_RECURSION.md. Drift has no separate Brownian lowering term under ordered distinct-label centering; the full-product contraction cancels the subtracted diagonal. Brackets retain all shared-label contractions, with root excluded from the nonroot matching. For k=2, the deterministic U_0 contraction is mu^2(B Phi)/(2N) in P=U_2/2. These are smooth identities. Singular Wick/diagonal counterterms remain OPEN.
