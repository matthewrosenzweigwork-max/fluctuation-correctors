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
