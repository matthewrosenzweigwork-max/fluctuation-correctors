# Assumptions and constants ledger

No theorem may use an unnamed “regularity constant” or “uniform constant.” Add one row per theorem/lemma.

| ID | Object | Exact assumption | Constant/symbol | Depends on | Uniform in | Status |
|---|---|---|---|---|---|---|
| AC-001 | mean-field density | smooth and strictly positive on \([0,T]\) | \(m_T,M_T\) | initial data, potential, kernel, temperature, \(T\) | not assumed | explicit smooth hypothesis only |
| AC-002 | backward one-body propagator | regularity sufficient for tested commutator | \(C_{T,k}\) | mean-field trajectory | \(N\) | OPEN |
| AC-003 | pair propagator | smooth data and displayed finite norms | c_m(t), A_m | d,m,T, ||K||C^m, ||b||C^m, ||grad mu||L1, forcing | N>=2, nu>=0 conditional on those uniform norms | PROVED_CANDIDATE THM-009 |
| AC-004 | k-body propagator | order-uniform or quantified growth | \(C^{(k)}_T\) | \(k,T\), cutoff | \(N\) | OPEN |
| AC-005 | local static response | moving-background uniformity | \(C_{\mathrm{stat}}\) | law, \(\lambda\), density | \(N,t\) | OPEN |

For every constant state:

- whether it depends on \(s,d,T,\lambda\), density lower/upper bounds, confinement, test norms, corrector order, and regularization;
- whether dependence is polynomial, exponential, factorial, or unknown;
- whether the dependence permits summation at criticality;
- whether it is stable at endpoints and under cutoff removal.


## Round 001 frozen hypotheses

AC-001 is an explicit smooth-positive finite-horizon reference hypothesis; uniform bounds across beta_N and cutoff are not proved. At fixed smooth g all derivatives needed by Ito and integration by parts are finite. The planned pair propagator estimate must display dependence on the C^m norms of K,b, the time-uniform L1 norm of grad mu, time horizon, and forcing; uniformity in N or diffusivity is conditional on these quantities being uniform. No symbol hides epsilon dependence.

The THM-009 solution constant is exponential in the time integral of c_m(t), as recorded in OP-002 and smooth report (1.1)–(1.7). Source J_f costs d 2^{m+1} kappa_m ||f||_{C^{m+1}}. No density lower bound enters this analytic constant; it uses probability mass and ||grad mu||L1. No corrector-order summability or endpoint singular uniformity is established. The heat-cutoff derivative and source divergence are explicit in REG-001.
