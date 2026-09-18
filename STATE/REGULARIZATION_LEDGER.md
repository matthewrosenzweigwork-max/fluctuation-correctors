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

## Round 002 fixed-smooth boundary

The new coupling/moment estimate has explicit exponential dependence on the Lipschitz norm of K and derivative dependence in the cubic source. The fixed-data qualification supplies finite smooth constants but does not remove this dependence for g_epsilon. TASK-013 is active on order/cutoff power counting and a sufficient joint-cutoff condition. Any slowly removed regularization estimate for its own model must remain distinct from fluctuation-scale comparison to singular dynamics. No limit exchange is authorized by the residual proof.

Round 002 review update: AUD-006 now grants HOSTILE_REVIEW_PASS for the bounded residual estimates, fixed-data norm qualification and Gibbs law-class obstruction in the precise scopes above. The singular and other open interfaces are unchanged.

## Round 002 final integration

Round 002: repaired THM-014 proves heat derivative upper exponents (s+m+1)/2, a Lipschitz lower divergence exponent (s+2)/2, and exponential growth of the particular coupling constant at positive horizon. A sufficient fixed-order regularized-model condition is epsilon_N^(-(s+2)/2)+log(1+A_Phi(N)+A_f(N))=o(log N). The fixed-data envelope permits a sufficiently slow diagonal cutoff. None compares the singular and regularized particle models. Round 003 examines the initial iid pair interface and close-pair errors, leaving all positive-time singular passages OPEN.

## Round 003: initial iid heat and spatial cutoffs

For REG-001 the exact Haar squared norm is c_ds^2 sum_(k!=0)|k|^(2s-2d) exp(-8 pi^2 epsilon |k|^2), and the scaled pair variance is b_N(N-1)/(2N^2) times that norm. At epsilon=N^(-2/d), its super-L2 order is b_N N^(2s/d-2); at epsilon=N^(-4/d), it is b_N N^(4s/d-3). These are different length scales, not interchangeable regularizations. THM-015/AUD-012 gives explicit two-sided constants.

REG-002 initial diagnostic only: hard spatial cutoff g_r=g 1_(dist>=r), with its nonzero mean retained and then explicitly centered. THM-016 proves a probability comparison without any stochastic generator passage. The separately centered inner/outer L1 split in THM-018 requires no no-close-pair event. The unregularized g and g-g_epsilon have infinite L2 pair moment for every finite N>=2 when 2s>=d; fixed-N L1/a.s. cutoff convergence alone supplies no fluctuation-scale joint rate. For actual singular dynamics all limit exchanges remain open.

THM-017 uses a different fixed radial compact cutoff of an exact internal-transport profile, with the annular source (v_N.grad chi)Phi retained explicitly. It does not regularize or solve the full periodic pair problem. Its core length is (2s(s+2)tau/N)^(1/(s+2)), not either heat length above.

## Round 004 annular domain passage

THM020 uses nested finite annuli for the auxiliary local diffusion, not a singular-particle cutoff comparison. Exit probabilities go to zero from each fixed nonzero point; positive source integrals pass by monotone convergence, signed ones by domination with the integrable full source. No derivative compactness or spatially uniform convergence is inferred. At nu=0 use only the characteristic convention; finite annular all-boundary transport data are not imposed. Classical regularity and heat-cutoff compatibility of the actual full generator remain open.

Round004 response gate (THM021,AUD023/024): below Coulomb, D and K are L1 and heat-response convergence is operator norm; at Coulomb only strong L2 convergence on fixed inputs or compact input families holds, uniformly under common C1 background bounds. Exact homogeneous difference norm is2c_d at every positive cutoff. Pointwise Borel diagonal-indicator convergence fails; this is compatible with its zero Haar class. A cutoff-dependent bounded L2 family need not be compact. No pair propagator/source convergence is inferred. R5 directly constructs the singular periodic source potential and separately claims strong terminal-data semigroup passage, now under fresh review.

Round005 singular pair passage (THM023,AUD026/027): heat force converges locally C1, same-noise regularized paths remain near each noncolliding singular path for small cutoff, and terminal-data operators converge strongly in Haar L2 for each fixed parameter/time pair. The measure-extension step is explicit. This does not prove operator-norm convergence or convergence of heat-regularized source potentials. The full-response construction uses the singular base directly, and singular finite-particle Ito passage remains open.

R5 full interface passes with terminal-data-only heat propagation and exact finite-measure response. No regularized source-potential convergence, global Borel sup convergence at Coulomb, or operator norm convergence at Coulomb is inferred. THM026 proposes fixed-start same-noise N-particle path convergence; its new audit is separate. The singular corrector identity still needs its own derivative/domain and residual/bracket passage.

THM026 with AUD030/031 proves full-family same-noise N-particle heat convergence at each fixed start/tuple/horizon, using local C1 force convergence and a path-dependent collision-excluded region. It first constructs singular paths and then passes continuous-test density domination; no arbitrary-Borel terminal convergence,uniform-N rate,singular Jacobian or corrector-source convergence is inferred. All collision patterns are covered by the full energy.

R7 passes the first-gradient source passage independently of heat terminal-data convergence. Constructor uses direct weighted occupation/UI and a common compact-start flow; blind uses a separate source cutoff whose weighted derivative tail is O(epsilon^(q+1)). Deleted tubes identify global weak gradients without a trace. Original Coulomb response/heat exclusions remain. R8's proposed actual-particle passage uses direct collision localization; it remains pending fresh audit and is not called heat-source convergence.

R8 singular particle identity passes by direct compact collision stops. Deleted-tube errors for weak first/second derivatives vanish by bounded Phi and q1<d-1; q2<d and2q1<d give W2,1/H1. Moving-tube contractions justify background derivatives. Already-integrable drifts pass in L1 and stopped martingales in L2 using fixed-N density domination. No corrector heat-source convergence or diagonal trace is asserted; earlier heat exclusions remain.

R9 constructor retains the nonpositive Coulomb inner flux and sends collision-tube radius to zero at fixed N before uniform estimates. Below Coulomb it vanishes. Blind proof uses increasing radial cutoffs with ||grad theta_epsilon||2=O(epsilon^((d-2)/2)), fixed-N H1 diffusion error, and B theta>=0. No diagonal trace, force-gradient absolute majorant, corrector heat-source convergence or N/regularization interchange. Both routes retain the full domain prerequisite.


R10 proves actual free-energy passage at fixed N using same-noise convergence, positive minimum separation on compact times, local convergence of the heat kernel potential, a common lower energy bound with Fatou, and entropy variational lower semicontinuity. The sharper heat-integral energy floor is a separate positive Fourier truncation, not convolution. True-inverse smoothing occurs after construction; only the explicit actual residual-tail estimate would allow its N-uniform removal. No fixed-N H1/density limit is exchanged with N by assumption.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.
