# Martingale and quadratic-variation ledger

| ID | Origin | Integrand | Scale | Quadratic variation | Cross-variation | Limit | Status |
|---|---|---|---|---|---|---|---|
| MG-001 | one-body fluctuation | \(\nabla f(x_i)\) | to freeze | known form to rederive | with corrector martingales | Gaussian baseline | OPEN |
| MG-002 | pair corrector | pair gradient/force discrepancy | to derive | to derive | MG-001 and MG-003 | may survive | OPEN |
| MG-003 | k-body corrector | k-body gradient | to derive | to derive | all adjacent levels | critical resummation | OPEN |

Every martingale theorem must prove:

- exact finite-N normalization;
- predictable quadratic and cross variations;
- tightness/Lindeberg or martingale-problem conditions;
- cutoff removal and uniform integrability;
- whether correction martingales alter covariance or create higher chaos;
- compatibility with initial fluctuations.


## Round 001 formulas

Write H_i[Phi]=N^{-1}sum_{j!=i}grad_x Phi(x_i,x_j)-integral grad_x Phi(x_i,y)mu(dy).

- MG-001: dM_f=sqrt(2nu) N^{-1}sum_i grad f(x_i).dW_i; bracket 2nu N^{-1}eta(grad f.grad q)dt.
- MG-002 in P=U_2/2 convention: dM_Phi=sqrt(2nu)N^{-1}sum_i H_i[Phi].dW_i; pair bracket 2nu N^{-2}sum_i H_i[Phi].H_i[Psi]dt; cross bracket with MG-001 replaces first H by grad f.
- Corrected bracket is 2nu N^{-2}sum_i |grad f(x_i)+H_i[Phi]|^2dt. A cross term may affect the limiting covariance.
- Exact label contractions are displayed in algebra (5.2)-(5.3) and BBGKY (3.9)-(3.10); their coefficients independently agree. Finite-smooth identities exact; limiting brackets, tightness and cutoff passage OPEN.

## General bracket

For U_k, Gamma_{k,i}=grad_{x_i}U_k=(k/N)V_{k-1}^{(i)}[grad_1 Phi(x_i,.)], with denominator N and label i excluded. M_k=sqrt(2/beta_N) sum_i integral Gamma_{k,i} dW_i. Every predictable cross bracket is 2/beta_N sum_i Gamma_{k,i} dot Gamma_{ell,i}; all partial shared-label bijections are expanded in recursion report (R5). Square integrability follows from fixed-smooth bounded kernels on finite time. These bounds do not establish vanishing of sigma_N-scaled correction brackets or cross variations under a singular cutoff.

## Round 002 bounded noise estimates

THM-010 gives E[M_Phi]<=2TH^2/(beta N^2) and E TV([M_f,M_Phi])<=2TL_fH/(beta N^(3/2)) under the actual iid-prepared interacting smooth law. Sigma^2 scaling therefore gives O(N^-1) and O(N^-1/2), uniformly for every beta>0. Root exclusion remains in H_i, and signed mean zero is not used. Isolated comparison AUD-005 passes; hostile constants review pending. TASK-014 now addresses the one-body martingale limit with explicit deterministic covariance convergence.

AUD-004 independently reconstructs every all-order shared-label bracket. Its centered formula (20)/(23) is equivalent to the R1 factorial/subset formula: p total shared edges, one distinguished Brownian edge, coefficient 2/(beta N^p), multiplicity p binomial(k,p) binomial(ell,p) p!, followed by every subset of the shared quotient slots integrated once against mu. It implies no positivity of individual centered terms and no critical summability.

Round 002 review update: AUD-006 now grants HOSTILE_REVIEW_PASS for the bounded residual estimates, fixed-data norm qualification and Gibbs law-class obstruction in the precise scopes above. The singular and other open interfaces are unchanged.

## Round 002 final integration

Round 002 final: THM-011 replaces the actual leading bracket by its deterministic mean-field counterpart in L1 with error O(N^-1/2); the positive-sign complex exponential has bounded modulus and proves factorization against every bounded initial-measurable variable. AUD-007 hostile PASS, AUD-008 statement-only comparison PASS with disclosed context reuse. All-order bracket inequalities use THM-014 symmetrized rooted identities; original unrestricted THM-012 identity is prohibited. At inverse temperature tending to infinity the leading noise covariance vanishes; at inverse temperature tending to zero both limiting covariance components vanish under iid normalization. No singular bracket passage or path tightness follows.

## Round 004 auxiliary martingale class

THM020's martingale is the conditional expectation of an integrable source occupation from each starting point. Smooth Ito is used only before finite annular exit; bounded stopped derivatives justify zero-mean stochastic integrals. Source integrability is proved before the limit. This establishes the bounded Borel inverse's true-martingale identity, not gradients or quadratic/cross variations of the full N-particle corrector. Those PO001 obligations remain OPEN.

The R5 probabilistic inverse has a true/UI source martingale along the auxiliary base-pair process. This does not give the corrector martingale along the interacting N-particle process. Its gradients, self/cross quadratic variations and passage to the exact particle identity remain PO022/023/PO001. The candidate fixed-N density estimate cannot make an unproved derivative integrable.
