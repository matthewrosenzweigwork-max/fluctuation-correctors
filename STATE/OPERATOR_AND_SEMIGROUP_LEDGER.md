# Operator and semigroup ledger

| ID | Operator | Space/domain | Final-value problem | Bounds needed | Status |
|---|---|---|---|---|---|
| OP-001 | one-body backward linearized operator | smooth/negative Sobolev dual | terminal \(\phi\) | existing input to re-audit | OPEN |
| OP-002 | full pair L_2+B/N | symmetric smooth pair kernels, including diagonal | source -J_f, terminal zero | fixed-smooth C^m bound proved candidate; cutoff uniformity open | EXACT_IDENTITY / analytic PROVED_CANDIDATE |
| OP-003 | k-body linearized operator | symmetric k-body kernels off partial diagonals | recursive source | order growth and summability | OPEN |
| OP-004 | critical resummed operator | Fock/cumulant/pair-field state | terminal corrected observable | generation, uniqueness, radius in \(\lambda\) | OPEN |
| OP-005 | one-dimensional gap operator | ordered/gap coordinates | route-specific | discrete elliptic/HS bounds | OPEN |

For each operator record:

- exact derivation from finite-N algebra;
- adjoint conventions and invariant constraints;
- smoothing/derivative gain and loss;
- singular behavior near all partial diagonals;
- dependence on \(k\), cutoff, time, and \(\lambda\);
- semigroup/propagator composition;
- compatibility with contractions;
- source and proof locations.


## Round 001 exact operator identification

OP-001=A+R with A=u.grad+nu Delta and Rf(y)=integral K(x-y).grad f(x)mu(dx). OP-002=L_2=A_x+A_y+R_x+R_y with both integrated-variable response derivatives. The finite-N pair operator also includes B/N, B=K(x-y).(grad_x-grad_y). See THM-008 for complete domains/definitions. Formula status EXACT_IDENTITY with isolated reconstruction; bounded fixed-smooth propagator estimate is THM-009, while cutoff-uniform bounds remain OPEN. Independent transport alone omits quadratic response and is not the correct pair operator.

## Round 001 analytic bound

THM-009: for m>=2, set kappa_m=||K||_{C^m}, b_m=||b||_{C^m}, M_1(t)=sum_a||partial_a mu_t||_1. With A_m=b_m+3 kappa_m/2 and c_m(t)=2d(2^m-1)A_m+2(d kappa_m+kappa_0 M_1(t)), the backward solution satisfies ||Phi_t||_{C^m} <= integral_t^T exp(integral_t^s c_m(r)dr)||F_s||_{C^m}ds. Uniform in N>=2 and nu>=0 provided these data norms are uniform. The response is bounded on C^m by splitting integrated-variable derivatives; B/N is unbounded on C^m as a separate perturbation and must be included in transport. Flow/Volterra and differentiated PDE proofs are in the smooth memorandum. Neither a Markov contraction for the response nor singular cutoff uniformity is claimed.

OP-005 now has an exact stopped generator and bracket in ordered report (G1)–(G6). A=DD^T has nonzero eigenvalues 4 sin^2(pi k/N), hence slow modes; its physical mobility differs from the source static Euclidean gap operator. For non-translation-invariant observables add the rotation coordinate and its nonzero cross variation with gaps. Uniform inverse, endpoint and martingale estimates remain OPEN.

## Round 002 final integration

Round 002: the root fixed-data bounds and THM-013 give explicit uniform finite-spatial-order estimates for the existing positive-diffusivity reference and the full backward test, construct the zero-diffusivity reference/response by characteristics and Volterra series, and prove Lipschitz dependence in diffusivity with two additional derivatives. Both transport and response density differences are retained. AUD-006 reviews the root qualification; AUD-010 reviews THM-013. Constants depend on the actual smooth data; singular inverse and order-uniform corrector estimates remain OPEN.

## OP-006 — Round 003 internal transport diagnostic

Punctured Euclidean relative coordinate, v_N=(2s/N)|z|^(-s-2)z, source s|z|^-s theta.A.theta and zero terminal data. The unique solution in the explicitly absolutely-continuous forward characteristic class is (N/4)(theta.A.theta)[(r^(s+2)+2s(s+2)tau/N)^(2/(s+2))-r^2]. Its finite-amplitude core can be angularly discontinuous; no equation is imposed at coincidence. Full proof THM-017 memorandum; separate review status recorded in the theorem ledger.

OP-002 is unchanged. The missing full-operator comparison must retain relative diffusion 2nu Delta_z, ordinary pair transport, both R terms, actual source, periodic force correction and the cutoff annular term. For nonscalar A the punctured Laplacian has leading -2d F_0 a_0(theta)/r^2; low diffusivity alone cannot justify omitting it. OP-006 does not provide a singular Markov/response propagator or justify Ito across collision.

AUD-014 makes the anisotropic diffusion limitation explicit: Delta Phi is not locally L2 for d=2,3,4 and is not absolutely locally L1 for d=2, when A has nonzero traceless part and tau>0. A strictly positive scalar nu does not cure infinite norms. A full generator may have cancellation between terms; no nonexistence is inferred.

Root's separately sealed ROUND_003_DIFFUSION_RESCALING.md supplies a SELF_CHECKED punctured chain-rule identity, now submitted to fresh hostile review. Under y=N^(1/(s+2))z and Phi=N^(s/(s+2))F, the local operator has diffusion 2 chi_N Delta_y, chi_N=N^(2/(s+2))/beta_N, internal drift 2s|y|^(-s-2)y.grad, and source s|y|^-s a(theta). At critical lambda, chi_N=lambda_N^-1 N^[s(s+2-d)/(d(s+2))]. This classifies only a coefficient, not operator/solution limits or domains.

## Round 004 local probabilistic realization

THM020 constructs the punctured operator 2nu Delta+(2s/N)r^-s-2 z.grad for d>=s+2 via locally Lipschitz additive-noise Picard flow, annular exit bounds, and measurable deterministic-time Markov conditioning. Its source potential is the unique bounded Borel terminal-zero true-martingale solution. Killing is specified probabilistically; any classical solution satisfying stopped-Ito hypotheses is identified, but classical existence is not asserted. The radial amplitude has Delta F=(N/2)[q^(s/(s+2))(d+s-sq)-d]<=0; comparison is uniform in nu even though exit constants need not be. Fresh reconstruction AUD020 passes; hostile pending.

## Round 004 full response interface

Fresh AUD021 completes THM020 hostile review. THM021 passes fresh AUD023/024: D=div K is a finite signed measure; each exact response equals minus translation integration of mu Phi against D and of grad mu Phi against K. Each has Borel sup/Haar L2 norm <=M0 TV(D)+M1||K||1. At Coulomb D=c_d(delta0-Haar); the atom multiplies Phi(x,y), requiring no diagonal trace. The two-slot sum has twice this bound and preserves symmetry. Heat acts outside the entire response with fixed mu. Smooth pair divergence has 2D_epsilon/N and norm exponent a+kappa/N. Singular semigroup passage and both-response composition remain separate R5 submissions, not consequences of this smooth estimate.

Round005 THM023 constructs the actual periodic base pair G_N with source J_f, a bounded Borel martingale inverse, Haar L2 norm C rho_N and semigroup norm exp[(D_u+C0/N)(a-t)]. Local pathwise heat passage plus averaged endpoint-measure domination justifies Haar equivalence classes and strong terminal-data convergence; joint two-time continuity is proved. Fresh AUD026/027 pass. THM024 conditionally adds both responses with norm multiplier exp[(c+C_R)T], separately in pointwise Borel and Haar L2 classes. Symmetry means pair exchange, not self-adjointness. No derivatives or N-particle Ito domain follow.

THM025 with AUD028/029 now combines the genuine periodic singular base and both exact responses into a terminal-zero bounded Borel martingale inverse and consistent Haar L2 mild solution. Pointwise and Haar uniqueness are separate. The Coulomb atom remains at the current off-diagonal state. Common singular propagation constant is explicitly justified by the addendum. No classical derivative/PDE or N-particle domain follows; PO022/023 isolate those next obligations.

THM026 constructs the actual jointly Borel N-particle transition kernels and deterministic-time conditional Markov laws via measurable cutoff paths and independent-increment restart. No universal exceptional set or imported singular SDE theorem is used. Its smooth random-flow Jacobian is used only before the heat limit; no global invertibility of the singular flow is claimed.

Round007 THM027 passes fresh AUD032/033. The pair Jacobian's largest symmetric eigenvalue, weighted occupation and higher moments justify nearby-start completeness and expectation derivatives. The two independent proofs use Morrey control and Holder-path non-downcrossing, respectively. Both responses preserve the weighted C1 class by finite-measure convolution and weak differentiation; the pointwise factorial Volterra series identifies the actual inverse. No weighted-space strong continuity, time/second derivative or particle-generator domain is inferred. THM028 supplies a separate pending construction for those homogeneous domain questions.

R8 accepted homogeneous domain: weighted higher flow moments and two variations, both finite-measure responses, and a pointwise factorial series identify the genuine C2 inverse. A separate autonomous weighted evolution yields the time derivative from differentiated source/terminal integral, without weighted-sup strong continuity. The base-pair martingale identifies the classical PDE. Solving it for B Phi proves Haar L1 through cancellation. The independent signed-jump route uses fixed-segment avoidance, not a universal collision-free flow for all starting points. No stronger background-gradient derivatives are certified.

R9 energy sign is specific to actual homogeneous responses: R=-D convolution in each slot, Fourier quadratic form -sum_(k,l)(d_k+d_l)|Phi_hat|^2<=0 with d_k>=0 bounded. Finite-measure L2 continuity justifies Fourier approximation; general inhomogeneous response and base-pair evolution are not asserted dissipative. Internal B instead obeys only integral Phi B Phi<=kappa||Phi||2^2. The blind extension derives a strongly continuous L1 full evolution from R5 measure domination, not an L2-to-L1 shortcut; its additional timewise claim is under TASK062 review.

TASK062 final supplemental disposition: PASS_CONDITIONAL_EXTENSION, report AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK.md,209 lines,SHA25621ce79223857d09784121cf0b50b1d3befa30f9efd571f217cca2b2932277560. Root read the entire supplement, verified22 inputs,25 archive members and new output/outer seals, and rechecked all original hostile seals. No new diagnostic count is claimed. The precise additional corollary is sup_(t,N,nu)||partial_t Phi_t||1<=C_dot and nu||grad_pair Phi_t||2^2<=C_* N^(s/(s+2)) at every deterministic time, with corresponding timewise Haar self/absolute-cross rates. The original integrated theorem passes its two fresh-context gates; the additional corollary has a separate independent review in the reused hostile context after its original seal. It is not another fresh audit or certification of the whole blind report. No actual-law smallness, diagonal trace or uniform unweighted gradient follows.


R10 uniform L1 uses the genuine Borel measure bound for S, bounded signed-measure responses in both slots and an absolutely summable ordered Volterra series. Common translations act equivariantly and differentiate through the actual Fourier test, yielding uniformly smooth one-variable projections; these are not separate relative-coordinate derivative estimates. The orbit average vanishes. THM030/031 hostile passes; full new blind gate pending. R11 bounded-chi value/gradient and response-only limit remain distinct submitted claims under fresh reconstruction/hostile gates.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 proves |grad_pair Phi|/w_q<=C_q N^((s+1-q)/(s+2)) for1<q<d/2,q<=s+1 at bounded chi. The source split cancels the occupation factor N. Both homogeneous finite signed-measure responses act on the derivative only, with no extra value norm. Root Gronwall and fresh Ultra full differentiated-series constructions identify the same existing inverse. THM032 spatial convergence is not a premise.

R11 passes the full weighted-space assertion and response-only limit integral exp((a-t)R)J_a^0 da, uniquely in uniformly weighted-value bounded pointwise mild class. Both responses remain. Uniform local C1 convergence passes through separated singularity convolution and factorial tails; no weighted-sup/H1/time-derivative convergence is asserted. R13 improves only the derivative norm using simultaneous diffusion/repulsion occupation and derivative-only homogeneous response bounds.


Round014 final gate,2026-09-18 UTC. R14 uses only the complete R8 genuine-domain and R12 smaller-weight uniform-gradient implications for the same full two-response inverse. Force-gradient product and Haar slice identification are audited separately. R10 energy/noise and R11 spatial limit are not needed for this bound.


Round015 final gate,2026-09-18 UTC. R15 new source bound uses positive heat coefficients and a Fourier commutator cancellation with polynomial cost; it does not need the pair inverse. Cubic closure additionally invokes the exact genuine full inverse and both responses through accepted R5/R8/R12 sources. Complete current R11/R13/R14 results are nondependencies.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R17 zero-noise response S_t multiplier exp(-tD_s(k)), backward f_r=S_(t-r)exp(nu(t-r)Delta)h. Uniform Fourier smooth seminorms and L2 contraction are used; no positivity-preserving claim for S_t is required. Its covariance has timesum damping. THM040 proposed Q_t uses L_k=D_s(k)+nu_bar4pi^2|k|^2 and explicitly adds thermal covariance; this extension is OPEN.


R17 final gate,2026-09-18 UTC. R17 accepted finite-dimensional limit uses the genuine zero-noise response S_t and covariance with sum of times. No high-frequency smoothing or positivity-preserving property of S_t is assumed, including Coulomb. Broader temperature Q_t^nu limits are separately frozen.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. Q_t^nu has multiplier exp(-t(D_k+nu*a_k)) and preserves constants. All spatial Fourier seminorms contract for every finite nu. R19 requires no uniform time derivative as nu diverges. New THM042 asks a continuous-path statement beyond current finite-list gates.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.


R22 pending extension,2026-09-18 UTC. New THM044/PO031 freezes distribution-valued path convergence in C([0,T],H^-r) for the same bounded-convergent-noise homogeneous iid-Haar row d>=3,0<s<=d-2,s<d/2, with explicit sufficient r>2d+5-s/2. Required source remainder is expected Hilbert path supremum C sqrt(b)N^(s/d-1/2), and linear Fourier-tail second moment is bounded by C sum_(|k|>K)(1+|k|^2)^(-r)(1+|k|^2). No optimality or full hierarchy claim. Root TASK096 complete exposed construction is sealed SELF_CHECKED, expressly conditional on the full R20 source pending its gate.16inputs25members47437 exact checks19categories12 mutation witnesses reproduce byte-identically. ProofSHAaeb80c4b794fc8433faeefcbd5d244b48b26aa776e50f4294b677b050d501bd2; archiveSHA7a74dec907e0be0024c177d8b64273c04b9451bcda88999643816370d878fe5f. Exact proof MEMORANDA/ROUND_022_DISTRIBUTION_PATH_GAUSSIAN.md. TASK097/AUD063 statement-only Max dossier prepared16inputs, not dispatched; TASK098/AUD064 hostile reserved. Next freeTASK099,AUD065,THM045,PO032. No independent promotion; root previously read full R20 constructor and only current reviewer progress summaries.


R20 accepted gate,2026-09-18 UTC. Entire THM042/PO029 passes fresh whole reconstruction AUD059 and separate hostile AUD060; root full642/601/234-line comparison, exact accepted R4/R6/R10/R16/R18 source matching, and4255/2508/3316 supporting-check reproduction are complete. All14/14/16 input and22/23/25 archive-member packets verify unchanged/read-only; diagnostic reruns byte-identical. Genuine common source-family domination yields expected supremum remainder C sqrt(b)N^(s/d-1/2); adapted fourth moments and finite-prefix modulus sets give actual uniform-path tightness; continuous Gaussian existence and full weak passage are proved. Scope d>=3,0<s<=d-2,s<d/2,actual homogeneous iid-Haar preparation,bounded convergent noise,fixed finite smooth test list; all frozen zero/degenerate cases included. Mathematical label PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS/HOSTILE_REVIEW_PASS; no field/higher-exponent/hierarchy promotion. Exact records AUDITS/ROUND_020_GATE_INTEGRATION.md and ROUND_020_RECONSTRUCTION_COMPARISON.md. Constructor le typo and hostile tar-versus-ZIP wording are separately recorded, originals unchanged.

R21 whole reconstruction AUD061 now root-read527lines and byte-reproduced117352 assertions/72 whole finite identities/18 mutations;29-input38-member immutable packet verified. Comparison AUDITS/ROUND_021_RECONSTRUCTION_COMPARISON.md. TASK095/AUD062 fresh Max hostile dispatched32inputs, still pending sealed verdict. Root proof independent status is not inflated. R22 TASK097/AUD063 fresh Max blind16inputs and TASK098/AUD064 fresh Max hostile19inputs are both dispatched in separate worktrees at64ac0538, pending. Current active workers095/097/098; cap10 configured versus3 available plus root. Next freeTASK099,AUD065,THM045,PO032.


R21 final whole gate accepted,2026-09-18 UTC. THM043/PO030 is PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS (AUD061) and HOSTILE_REVIEW_PASS (AUD062), with exact published source/gate matching. The full strict range d>=3,0<s<d-2,s(s+2)<2d at finite positive microscopic critical lambda is retained. The actual integrated cubic residual obeys sigma E|integral U3[C Phi]dt| <= C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa] ->0. Absolute value remains after time integration; the genuine pair inverse retains both responses, the exact R8 domain, full true martingale and both lower contractions rho[g]/N+c/(2N). No instantaneous cubic estimate, Coulomb endpoint, Gaussian law or hierarchy is inferred. Root complete source/candidate/527-line blind/249-line hostile reading and twelve-item comparison are AUDITS/ROUND_021_GATE_INTEGRATION.md and ROUND_021_RECONSTRUCTION_COMPARISON.md. All29/29/32-input38/38/42-member packets verify unchanged; fresh diagnostics12531/117352/137147 reproduce saved bytes. The hostile stdout-only extra newline is explicitly recorded and no evidence normalized. All-real exponent implications are proved analytically; finite computations support but do not certify them. Earlier pending entries are chronological history.


R22 gate,2026-09-18 UTC: R22 constructs strongly continuous modal contractions and genuine continuous Hilbert source, linear and Gaussian paths by summable coordinate envelopes; no assumed infinite stochastic integral. Sufficient r>2d+5-s/2; frequency damping need not have a uniform positive lower bound. Exact acceptance/source/scope: AUDITS/ROUND_022_GATE_INTEGRATION.md.


2026-09-18 UTC. R24 whole THM047/PO034 accepted: PROVED_CANDIDATE; ISOLATED_RECONSTRUCTION_PASS(AUD067), HOSTILE_REVIEW_PASS(AUD068); VERSION_LOCKED. Complete constructor/blind/hostile and all source/code/evidence root-read; no repair. Exact averaged trace and contraction integral K.D Phi+2c(q-tau), all Cj bounds C sqrt(N), source-specific scalar0, actual absolute scaled lower drift O(N^-1/4), iid endpoint O(sqrt((1+logN)/N)) and smooth true-noise O(N^-3/8) give the entire cubic-plus-residual-martingale L1 equivalence. Both responses, all backgrounds, N2 and fixed-N singular limits retained. THM046/PO033 remains OPEN. See AUDITS/ROUND_024_GATE_INTEGRATION.md and ROUND_024_RECONSTRUCTION_COMPARISON.md.


R25 accepted bounded update,2026-09-18 UTC: exact scope is AUDITS/ROUND_025_GATE_INTEGRATION.md. THM048's auxiliary initial-energy clipping and time-zero conditional isometry establish squared UI without altering dynamics or squaring instantaneous source; full THM049 converts the original L1 target to the actual signed modal correlation cancellation using degree10 L1 Fourier domination. Neither original cancellation nor its positive-limsup negation is proved. The dependence uses exact R4/R6/R10/R16 sources, with both fresh whole AUD069/070 passes and no pair-inverse/THM047 premise. No prior immutable statement is rewritten.


2026-09-18 UTC. THM050 accepted whole A-C after AUD071/072 and root646/423/521-line comparison. Actual P_t at fixedN,nu admits the exact conditional endpoint/noise decomposition and fixed-N limit of smooth backward Dirichlet costs. Target one-body weighting exp[-(c+nu ell)(T-s)] is distinguished from heat-linearized damping c exp(-epsilon ell)+nu ell. No singular gradient limit or uniform-N sensitivity theorem follows. For the real first mode, every sufficiently small positive time at each fixedN,nu has no full Haar W1,4 response; no W1,2 conclusion. R27 killed-attractive duality is separately SELF_CHECKED, awaiting both fresh axes.


2026-09-18 UTC — R26 whole acceptance. THM051 retains the actual singular flow, exact smooth heat cutoff of the kernel and all-frequency coefficient bound with r/8 heat scale. No replacement Gibbs, static or mollified flow enters the signed overlap reduction.


2026-09-18 UTC — R27 whole acceptance. Exact Haar bilinear adjoint P_t*=exp[kappa t]Q_t, kappa=c(N-1), with Q minimal killed attractive semigroup. Fixed-domain Girsanov and symmetric Brownian killing, followed by monotone exhaustion with strict t<zeta, justify the actual domains. Independent flow Jacobian gives the same full path law.
