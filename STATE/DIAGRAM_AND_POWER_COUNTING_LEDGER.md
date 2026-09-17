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

## Round 002 final integration

Round 002 repaired THM-014: for a partition pi with j singletons and nonsingleton blocks B, raw moment exponent is -k/2 minus one half of sum_B(|B|-2). Pair blocks cost no further N gain. The exact cycle weight is product_B (|B|-1)!, and the finite sum C_(k,p)(N) is retained. Root omission replaces R_p by R_p+B; all bracket bounds retain 2 nu T d k ell N^(-(k+ell)/2) times displayed derivative and root constants. Averaged symmetrization is mandatory in compact first-slot identities (AUD-009 repair). Drift statistical powers for upward/internal/single/double lowering are -(k+1)/2, -(k+2)/2, -(k+1)/2 and -k/2. Sufficient infinite series criteria are conditional on actual kernel growth; the concrete 1/k! model lemma is not an asserted hierarchy normalization. No lambda factor or critical singular survival decision has been proved.

## Round 003 local scales, not a hierarchy closure

Initial iid bare-pair scale u_N=N^(2s/d-2) and the sharp scalar b_N N^(4s/d-3) come from closest-pair statistics, not an assumed lambda vertex factor. Retaining internal transport produces the different profile core N^(-1/(s+2)) at fixed positive horizon and a squared-norm factor N^((2s-d)/(s+2)). Its initial diagnostic endpoint vanishes for all s<d. The diffusion-retaining local rescaling has coefficient chi_N=N^(2/(s+2))/beta_N, with a degree-two angular term -4d chi_N/r^2. These are exact local/formal power identifications with separate declared domain limits; no full response, evolving-law contraction estimate, higher-order survival classification or summability conclusion follows. Use the separate root scope erratum for the subcritical coefficient trichotomy.
