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


R12 uses the previously proved fixed-N genuine derivative and particle-energy/domain passages before applying its uniform estimates. The actual Laplacian occupation follows from the exact unstopped energy identity and deterministic sharp floor; no new singular Ito formula or N/cutoff interchange is presumed. Both fresh audits retain those prerequisite histories.

R11 tube tails give global W1,1 only after uniform local C1 and in the declared order; no diagonal trace. R13 actual w_(s+2) occupation is proved at fixed N by singular energy/domain passages before uniform estimates. A quantitative actual tail at the moving clipping threshold supplies the missing uniformity; fixed-N density approximation alone is not used. All issued source/archive bytes remain unchanged.


Round014 final gate,2026-09-18 UTC. R14 new bound uses the genuine off-diagonal product dominated by |K|w_q, with s+1+q<d. Moving-ball/complement convergence identifies continuous contractions at every remaining coordinate before empirical evaluation. No true diagonal derivative or new singular Ito limit is assigned; the accepted R8 full-domain passage is the explicit premise.


Round015 final gate,2026-09-18 UTC. R15 particle heat regularization is removed at fixed N using same-noise paths and shifted Fatou for expected energy. A different positive heat-integral observable splitting is then used at r=N^-2/d, with exact omitted positive remainder and retained smooth energy. Arbitrary smooth-test passage is explicit. The genuine inverse/domain are never replaced by a cutoff inverse; R8 supplies full fixed-N drift/martingale passages.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R16 removes particle heat regularization at each fixed N before positive observable heat decomposition/scales. R17 root uses actual collision-stopped identity and L1 drift/L2 noise passage; fresh reconstruction uses exact heat backward tests and pathwise source convergence on separated coupled paths, then actual L1 control. Neither interchanges N/cutoff limits nor assigns a singular diagonal.


R17 final gate,2026-09-18 UTC. R17 actual first-order identity has two independently justified fixed-N singular passages; both precede the uniform critical limit. No cutoff/N interchange or inferred convergence of source expectations from path convergence. Current source gate supplies actual L1 separately.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 full reconstructions perform fixed-N,finite-nu same-noise heat/noncollision passage first, then uniform actual inequalities. Source diagonal remains deleted and all Haar contractions genuine. No uniform particle-cutoff convergence rate or source L2 passage is inferred.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.


R22 pending extension,2026-09-18 UTC. New THM044/PO031 freezes distribution-valued path convergence in C([0,T],H^-r) for the same bounded-convergent-noise homogeneous iid-Haar row d>=3,0<s<=d-2,s<d/2, with explicit sufficient r>2d+5-s/2. Required source remainder is expected Hilbert path supremum C sqrt(b)N^(s/d-1/2), and linear Fourier-tail second moment is bounded by C sum_(|k|>K)(1+|k|^2)^(-r)(1+|k|^2). No optimality or full hierarchy claim. Root TASK096 complete exposed construction is sealed SELF_CHECKED, expressly conditional on the full R20 source pending its gate.16inputs25members47437 exact checks19categories12 mutation witnesses reproduce byte-identically. ProofSHAaeb80c4b794fc8433faeefcbd5d244b48b26aa776e50f4294b677b050d501bd2; archiveSHA7a74dec907e0be0024c177d8b64273c04b9451bcda88999643816370d878fe5f. Exact proof MEMORANDA/ROUND_022_DISTRIBUTION_PATH_GAUSSIAN.md. TASK097/AUD063 statement-only Max dossier prepared16inputs, not dispatched; TASK098/AUD064 hostile reserved. Next freeTASK099,AUD065,THM045,PO032. No independent promotion; root previously read full R20 constructor and only current reviewer progress summaries.


R20 accepted gate,2026-09-18 UTC. Entire THM042/PO029 passes fresh whole reconstruction AUD059 and separate hostile AUD060; root full642/601/234-line comparison, exact accepted R4/R6/R10/R16/R18 source matching, and4255/2508/3316 supporting-check reproduction are complete. All14/14/16 input and22/23/25 archive-member packets verify unchanged/read-only; diagnostic reruns byte-identical. Genuine common source-family domination yields expected supremum remainder C sqrt(b)N^(s/d-1/2); adapted fourth moments and finite-prefix modulus sets give actual uniform-path tightness; continuous Gaussian existence and full weak passage are proved. Scope d>=3,0<s<=d-2,s<d/2,actual homogeneous iid-Haar preparation,bounded convergent noise,fixed finite smooth test list; all frozen zero/degenerate cases included. Mathematical label PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS/HOSTILE_REVIEW_PASS; no field/higher-exponent/hierarchy promotion. Exact records AUDITS/ROUND_020_GATE_INTEGRATION.md and ROUND_020_RECONSTRUCTION_COMPARISON.md. Constructor le typo and hostile tar-versus-ZIP wording are separately recorded, originals unchanged.

R21 whole reconstruction AUD061 now root-read527lines and byte-reproduced117352 assertions/72 whole finite identities/18 mutations;29-input38-member immutable packet verified. Comparison AUDITS/ROUND_021_RECONSTRUCTION_COMPARISON.md. TASK095/AUD062 fresh Max hostile dispatched32inputs, still pending sealed verdict. Root proof independent status is not inflated. R22 TASK097/AUD063 fresh Max blind16inputs and TASK098/AUD064 fresh Max hostile19inputs are both dispatched in separate worktrees at64ac0538, pending. Current active workers095/097/098; cap10 configured versus3 available plus root. Next freeTASK099,AUD065,THM045,PO032.


R23 new static-law gate,2026-09-18 UTC. THM045/PO032 freezes insufficiency of energy/Haar inputs at d4,s2: bounded smooth exchangeable common-translation-invariant static densities with exact Haar one-body marginals, support separation c N^-1/4 and pointwise energy at most -c N^1/2, yet sqrt(N) E|P[J_cos(4pi x1)]| tends to16 pi^3 a^2>0 along N=m^4. This is NOT an actual iid-prepared dynamical counterexample or mission change. Root TASK099 proves a negative grid regular part, exact grid energy, small coherent deformation, low-order frequency selection, uniformly controlled second variation/Riemann passage and smooth jitter realization. Complete exposed root proof MEMORANDA/ROUND_023_STATIC_THRESHOLD_INPUT_OBSTRUCTION.md is sealed SELF_CHECKED,8inputs17members1549 exact assertions24categories10 detecting mutations; fresh code-only root rerun byte-identical and safe member/byte verifier passes. ProofSHA4cf376ce886714eb2de2d1c100d10c1e5b29db4510bd5684cca60f4d9af51855; archiveSHAa7c6ddf00043fa4df3fc702dccfa195704a4e27973abc9fed432050c99e38a23. Fresh TASK100/AUD065 blind8-input and TASK101/AUD066 hostile11-input dossiers prepared, neither dispatched. Next freeTASK102,AUD067,THM046,PO033. Actual iid-flow threshold cancellation, integrated source bounds and higher hierarchy remain open. No new external citation/private input.


R21 final whole gate accepted,2026-09-18 UTC. THM043/PO030 is PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS (AUD061) and HOSTILE_REVIEW_PASS (AUD062), with exact published source/gate matching. The full strict range d>=3,0<s<d-2,s(s+2)<2d at finite positive microscopic critical lambda is retained. The actual integrated cubic residual obeys sigma E|integral U3[C Phi]dt| <= C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa] ->0. Absolute value remains after time integration; the genuine pair inverse retains both responses, the exact R8 domain, full true martingale and both lower contractions rho[g]/N+c/(2N). No instantaneous cubic estimate, Coulomb endpoint, Gaussian law or hierarchy is inferred. Root complete source/candidate/527-line blind/249-line hostile reading and twelve-item comparison are AUDITS/ROUND_021_GATE_INTEGRATION.md and ROUND_021_RECONSTRUCTION_COMPARISON.md. All29/29/32-input38/38/42-member packets verify unchanged; fresh diagnostics12531/117352/137147 reproduce saved bytes. The hostile stdout-only extra newline is explicitly recorded and no evidence normalized. All-real exponent implications are proved analytically; finite computations support but do not certify them. Earlier pending entries are chronological history.


R22 gate,2026-09-18 UTC: R22 constructs actual Hilbert paths after the fixed-N singular particle passage. Positive minimum separation is used only for pathwise continuity, never a uniform constant. Countable modes/rational times plus continuous Hilbert versions give one simultaneous event. Exact acceptance/source/scope: AUDITS/ROUND_022_GATE_INTEGRATION.md.


## R23 gate / R24 resumption — 2026-09-18 UTC

R23 heat subtraction defines the lattice regular part with integrable endpoint majorants. Moving-scale source limit passes second derivatives after a C delta^2 diagonal-tube estimate, before inserting a/m. Final static densities use collision-free smooth jitter and compact group averaging; no singular diagonal value or stochastic Ito passage is claimed. Original line153 is corrected separately before use.
