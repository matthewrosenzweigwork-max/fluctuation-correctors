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
