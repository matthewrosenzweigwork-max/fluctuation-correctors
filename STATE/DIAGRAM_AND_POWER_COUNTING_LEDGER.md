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

R9 now proves a reference-Haar second-corrector self-noise upper rate b_N N^(-2/(s+2)) and integrated absolute cross rate sqrt(b_N)N^(-1/(s+2)), in the homogeneous bounded-diffusivity range. These arise from the full inverse and energy sign, not a guessed lambda vertex factor. The actual centered triple law error has coefficient ordernu b_N, unlike pair/mixed errors of ordernu b_N/N. This exact distinction leaves PO024 and the critical hierarchy open.


R10 approximation powers follow exact label coefficients and entropy/Fourier bounds. Clipping L_N=N^(1/(4p)) and smoothing delta_N=N^(-theta/(5d-s+2)) are explicit chosen scales. Their actual residual tails remain load-bearing. R12/R13 proposed sufficient subranges do not settle higher-order survival, infinite critical resummation or cubic drift power counting.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 proves a genuine actual-noise sufficient power from a smaller gradient weight and the actual divergence occupation. It is not a general lambda-per-vertex rule or a critical truncation theorem. The cubic drift and lower contractions still require explicit independent power/law control.

R13 accepted rate: p=s+2,a=s/p,theta=1-s/d; small-noise cutoff N^-1/(6p^2), radial clipping N^1/(4p), tail weight q_-=1+s/4,r=4(s+2)/(s+4)>2. Decay exponents are theta-a,(2-s)/(12p^2),s/(4p(s+4)),1/(2p),2/p. All are strictly positive for d>=4,0<s<2. This closes noise diagrams only; critical integrated cubic and all-order truncation table remain open.


Round014 final gate,2026-09-18 UTC. R14 discharges the lower/scalar contraction contribution at scaled rate N^-kappa in its strict range and identifies exact residual equivalences. This supplies no higher-order order gain, critical diagram truncation, or cubic-smallness theorem; PO004 remains OPEN.


Round015 final gate,2026-09-18 UTC. R15 critical integrated U3 smallness is accepted only in its exact range, from the terminal integrated identity and actual source estimate. This does not provide a bound uniform in hierarchy order, an instantaneous cubic estimate or infinite resummation. PO004 remains OPEN.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R17 source exponent s/d-1/2 is strictly negative in its frozen range; thermal error exponent at criticality is(s/d-1)/2. The finite-dimensional route does not control order-uniform higher diagrams or give any decay at s=d/2. THM040 retains a thermal contribution when nu_bar>0 rather than asserting it small.


R17 final gate,2026-09-18 UTC. R17 closes its finite-dimensional critical source residual only at strict s<d/2. This does not turn fixed-order power counting into a proof for s>=d/2 or an order-uniform critical hierarchy.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 source residual N^(s/d-1/2), actual smooth bracket deviation N^(-(1-s/d)/2), initial iid characteristic error N^-1/2. R18 adds arbitrary vanishing diffusivity-difference term; R19 avoids replacing triangular tests and is uniform over all finite nu. Equality s=d/2 still not decay.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.


2026-09-18 UTC. R24 whole THM047/PO034 accepted: PROVED_CANDIDATE; ISOLATED_RECONSTRUCTION_PASS(AUD067), HOSTILE_REVIEW_PASS(AUD068); VERSION_LOCKED. Complete constructor/blind/hostile and all source/code/evidence root-read; no repair. Exact averaged trace and contraction integral K.D Phi+2c(q-tau), all Cj bounds C sqrt(N), source-specific scalar0, actual absolute scaled lower drift O(N^-1/4), iid endpoint O(sqrt((1+logN)/N)) and smooth true-noise O(N^-3/8) give the entire cubic-plus-residual-martingale L1 equivalence. Both responses, all backgrounds, N2 and fixed-N singular limits retained. THM046/PO033 remains OPEN. See AUDITS/ROUND_024_GATE_INTEGRATION.md and ROUND_024_RECONSTRUCTION_COMPARISON.md.
