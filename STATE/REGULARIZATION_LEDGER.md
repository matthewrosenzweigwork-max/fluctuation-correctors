# Regularization ledger

REG-001 is frozen below. Other listed schemes remain candidates.

For each scheme record:

- ID and exact kernel \(g_\varepsilon\);
- Fourier/real-space convention;
- collision behavior;
- derivatives and operator bounds;
- order of limits;
- uniformity in \(N,\beta_N,\lambda_N\), time, and corrector order;
- counterterms generated;
- comparison with other schemes;
- proof and audit locations.

Candidate schemes:

1. heat regularization;
2. Fourier cutoff;
3. real-space truncation with smooth matching;
4. screened/Bessel regularization;
5. finite-particle deleted-diagonal renormalization without a continuum kernel.


## REG-001 — heat regularization, Round 001

For positive-power Riesz, g_hat(0)=0 and g_hat(k)=c_{d,s}|k|^{s-d}, c_{d,s}=pi^{s-d/2}Gamma((d-s)/2)/Gamma(s/2). Set g_epsilon=e^{epsilon Delta}g, multiplier exp(-4pi^2 epsilon |k|^2), epsilon>0. Fourier/local-singularity normalization checked in the source report. Every stochastic identity in Round 001 is first a fixed-smooth-kernel assertion. The order of the N limit and epsilon removal is not exchanged. No uniformity in epsilon, comparison of two renormalization schemes, or Coulomb distributional passage is established. Log model separately OPEN.

### Round 001 quantitative obstruction

MEMORANDA/ROUND_001_SMOOTH.md Section 7 proves for the prescribed heat Fourier sequence: ||K_epsilon||_{C^m} <= C epsilon^{-(s+m+1)/2}; div K_epsilon(0) is comparable to epsilon^{-(s+2)/2}. With the fixed terminal test cos(2 pi x_1), the relative-coordinate second derivative of J_f at the diagonal is -8 pi^2 a_epsilon, where DK_epsilon(0)=a_epsilon I. Thus the forcing C^2 norm diverges, and no uniform small-time estimate ||Phi_{T-tau}||_{C^2} <= C tau holds over all cutoffs. This disproves that strong uniform bound, not weaker norms or a justified joint cutoff limit. Audit status is recorded in the separate analytic review when issued. No singular limit taken.

The singular one-dimensional ordered gap energy has nonnegative interior Hessian by its explicit sum of g_s''>0. Heat regularization has g_epsilon''(0)<0 and loses that convexity near collisions. No uniform transfer of singular ordered convexity to REG-001 is permitted. Ordered report G1–G7 is stopped before crossings/collisions; removing that stop is an independent obligation.
