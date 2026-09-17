# Assumptions and constants ledger

No theorem may use an unnamed “regularity constant” or “uniform constant.” Add one row per theorem/lemma.

| ID | Object | Exact assumption | Constant/symbol | Depends on | Uniform in | Status |
|---|---|---|---|---|---|---|
| AC-001 | mean-field density | smooth and strictly positive on \([0,T]\) | \(m_T,M_T\) | initial data, potential, \(T\) | \(N,\beta_N\) | TO FREEZE |
| AC-002 | backward one-body propagator | regularity sufficient for tested commutator | \(C_{T,k}\) | mean-field trajectory | \(N\) | OPEN |
| AC-003 | pair propagator | well-posedness and diagonal regularity | \(C^{(2)}_{T}\) | kernel cutoff, background | to determine | OPEN |
| AC-004 | k-body propagator | order-uniform or quantified growth | \(C^{(k)}_T\) | \(k,T\), cutoff | \(N\) | OPEN |
| AC-005 | local static response | moving-background uniformity | \(C_{\mathrm{stat}}\) | law, \(\lambda\), density | \(N,t\) | OPEN |

For every constant state:

- whether it depends on \(s,d,T,\lambda\), density lower/upper bounds, confinement, test norms, corrector order, and regularization;
- whether dependence is polynomial, exponential, factorial, or unknown;
- whether the dependence permits summation at criticality;
- whether it is stable at endpoints and under cutoff removal.
