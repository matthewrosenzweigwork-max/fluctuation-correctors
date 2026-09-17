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
