# Diagram and power-counting ledger

Create one row for each algebraically distinct term/diagram.

| ID | Corrector order | Vertices | Contractions | Partial-diagonal degree | Raw N/beta factor | Lambda factor | Subcritical | Critical | Counterterm | Status |
|---|---:|---:|---:|---|---|---|---|---|---|---|
| DG-001 | 2 | 1 | 0 | to derive | to derive | to derive | ? | ? | ? | OPEN |
| DG-002 | 2 | 1 | 1 Itô | to derive | to derive | to derive | ? | ? | CT-002 | OPEN |
| DG-003 | 3 | 2 | 0 | to derive | to derive | to derive | ? | ? | ? | OPEN |

Required columns for every completed row:

- exact combinatorial multiplicity;
- deterministic/centered/martingale type;
- time integration gain or lack thereof;
- trace/Schatten class;
- dependence on corrector order;
- uniform bound sufficient to sum the critical series;
- solvable-model verification and independent computation ID.


## Round 001 coefficient information

For P=U_2/2 the cubic term has coefficient 1 with C=average over six permutations of K(x-z).grad_x Phi(x,y). Internal interaction and its lower contractions have coefficients 1/N, 1/N, 1/(2N) in front of P[B Phi], rho((B Phi)_mu), mu^2(B Phi). The full-product Ito contraction has coefficient nu/N and cancels in the deleted drift. Martingales retain their exact bracket coefficients. These are raw finite-N coefficients, not lambda_N sizes: the kernels, law and partial-diagonal norms still determine their asymptotic magnitude. DG-001/003 critical survival and uniform corrector-order summability remain OPEN; finite-order truncation has not been justified.

## Round 001 exact coefficients versus unknown effective scaling

MEMORANDA/ROUND_001_RECURSION.md (R1) gives U_k transport/response/internal C_k/N, upward U_{k+1}[A_k^+], downward k U_{k-1}[Q_k]/N and binomial(k,2) U_{k-2}[R_k]/N. Every bracket pattern with q common nonroot labels has raw factor 2 k ell/(beta_N N^{q+1}) times its explicit subset sign and injective factorial statistic (R5). All internal four subset survivors have coefficient +1. These coefficients are exact for fixed smooth kernels and every finite k,N, including k>N.

The singular degree, effective lambda power, corrector-order growth, integrated residual decay, and survival classification are OPEN. No Riesz exponent occurs in the smooth combinatorics. Neither an upward term at every order nor its formal lambda assignment proves that all levels survive at criticality. M2 remains open after the algebraic advance.
