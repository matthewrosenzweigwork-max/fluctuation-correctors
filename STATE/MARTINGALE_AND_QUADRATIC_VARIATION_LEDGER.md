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
