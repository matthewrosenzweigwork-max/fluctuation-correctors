# Obstruction ledger

## OBS-001 — pointwise weight positivity is insufficient

- Claim threatened: universal weighted Riesz lower bound for every smooth symmetric \(w\ge0\).
- Mechanism: choose a weight supported between two separated regions and a mean-zero signed perturbation; the diagonal term vanishes while the weighted quadratic form can be strictly negative.
- Status: DISPROVED universal claim / HOSTILE_REVIEW_PASS, Round 001 falsification Section 2 and AUD-002 Section 5. Explicit quantile configurations even converge to the reference; strictly positive-weight extension included.
- Consequence: restrict weights by positive-semidefinite structure or carry nonlocal signed error.

## OBS-002 — weighted remainder can retain original singularity

- Claim threatened: all weighted corrector remainders are less singular than \(g\).
- Mechanism: Taylor expansion of midpoint-type weights can leave an \(a'(x)g(x-y)\) leading term.
- Status: DISPROVED generic improvement / HOSTILE_REVIEW_PASS, Round 001 falsification Section 3 and AUD-002 Section 6. Exact leading coefficient is (1+s) d'(x)/2; constant diagonal restores the local gain.

## OBS-003 — self-energy subtraction does not close centered dynamics

- Claim threatened: cancellation of compression forcing yields coercive residual control.
- Mechanism: local-energy fluctuation and traceless stress remain; endpoint lower bounds do not control a difference without preparation/upper information.
- Status: structural warning.

## OBS-004 — critical finite-order truncation may fail

- Claim threatened: second-order corrector alone resolves \(\lambda_N\to\lambda>0\).
- Mechanism: each additional interaction vertex may carry a factor \(\lambda_N\), so every order can survive at criticality.
- Status: open; Phase 2 power counting decides.

## OBS-005 — ultraviolet field-only quadratic functional

- Claim threatened: same quadratic-chaos limit for all \(s<d\).
- Mechanism: tested kernel may fail Hilbert–Schmidt at \(2s\ge d\); divergent contractions require counterterm or pair field.
- Status: open; split by singularity.

## OBS-006 — conditional isotropy

- Claim threatened: local stress vanishes from rotational invariance.
- Mechanism: conditioning on exterior data or inhomogeneous background breaks exact rotational invariance; expectation cancellation does not give concentration.
- Status: structural warning.

Add proved obstructions and exact scope as the campaign proceeds.

## OBS-007 — fixed-smooth C^m estimate is not cutoff uniform

Smooth report Section 7: positive Riesz heat Fourier coefficients give DK_epsilon(0)=a_epsilon I, a_epsilon comparable to epsilon^{-(s+2)/2}. A fixed cosine terminal test has relative-diagonal second derivative -8 pi^2 a_epsilon in J_f. Uniform small-time C^2 corrector slope is false. Weaker norms and justified joint limits remain OPEN; this is not an impossibility theorem for all singular correctors. HOSTILE_REVIEW_PASS in AUD-003 for this explicit Fourier-sequence diagnostic.

## OBS-008 — same gap correlation bound cannot be temperature uniform

Ordered report Section 6: source b->0 at fixed N yields uniform-simplex gaps with Cov(y_i,y_j)=-1/(N+1). For cyclic separation of order N this contradicts a bound C distance^{-(2-s-epsilon)} with one C for all N,b when epsilon<1-s. DISPROVED / SELF_CHECKED; not yet separately hostile-reviewed. A diagonal b_N->0 gives a subcritical witness. It does not disprove a different temperature-dependent bound or every growing-beta subclass.

## Source and interface traps encountered

- Supplied note Fact 3.2 omits a finite-temperature martingale: source report witness. No imported deterministic identity promoted.
- The pointwise comparison of two negative-valued mean-zero periodic kernels in the stated order is inconsistent: source report. Global Euclidean midpoint/homogeneity is not a torus formula.
- Iid inverse-gap moments of order >=1 are infinite at time zero; fixed positive-temperature Gibbs moments are finite. No preparation transfer without an initial layer.
- Ordered singular convexity is lost near the diagonal by heat cutoff. Stopped gap identities do not prove global collision avoidance.
- Source static Euclidean gap mobility differs from the physical cycle-Laplacian mobility, and gap-only variables omit rotation. Static spatial correlation decay is not temporal mixing.
- SRC-005 printed c_s is inconsistent with its actual real-space/Fourier kernel; numerical covariance is quarantined, not silently corrected.

OBS-003, OBS-004, OBS-005 and OBS-006 retain their original unproved/structural status. No proof of critical survival, Hilbert–Schmidt endpoint classification, or conditional isotropy was supplied in Round 001.

## OBS-009 — iid moment control does not transfer to arbitrary smooth Gibbs preparation

DISPROVED / HOSTILE_REVIEW_PASS (AUD-006) for the unqualified transfer. On T^1 with g=a cos(2pi x), a<0, canonical Gibbs law has density proportional to exp(beta |a| N |eta(e_1)|^2/2). Its one-point marginal is uniform by translation invariance, while the arc lower bound gives P(|eta(e_1)|^2<=1-delta)<=p_delta^(-N) exp(-beta |a| N delta/4). For every beta_N->infinity, |eta(e_1)|^2->1 in probability and U2[cos(2pi(x-y))]->1. Exact first-marginal centering does not restore the iid moment bounds. Proof: ROUND_002_FALSIFICATION.md Section 8. This is outside iid preparation and is a fixed smooth attractive kernel; it is not a disproof of a positive-Riesz singular theorem. No retraction of a promoted campaign claim is required.

## OBS-010 — compact first-slot differentiation requires symmetry

COUNTEREXAMPLE / HOSTILE_REVIEW_PASS: Phi(x,y)=h(y) gives U_2=-eta(h)/N and nonzero particle gradient, but grad_1 Phi=0. Therefore the unrestricted compact first-slot formula in submitted THM-012 is false. AUD-009 provides the exact counterexample. Symmetrization preserves U_k and contracts C^m norms, repairing all quantitative estimates with no larger constant; new THM-014. This is a scope repair, not a singular-kernel obstruction.

## OBS-011 — infinite initial bare-pair variance is not probability failure

THM-015/016 and AUD-012 prove infinite unregularized pair second moment for 2s>=d at every finite N, but probability convergence below 3d/4, including the infinite-variance boundary. Therefore an L2 route to the unregularized bare statistic fails in that range; a probability/L1 route can succeed. Heat-cutoff second-moment divergence alone is not a converse. The new THM-019 lower-probability argument is a distinct claim with separately recorded audits.

## OBS-012 — raw-potential and actual-corrector thresholds cannot be identified

The sharp initial bare-potential converse in THM-019, if promoted, is not a singular fluctuation counterexample. THM-017 explicitly retains internal pair transport and yields a different, vanishing initial diagnostic endpoint for every s<d. Angular traceless modes have positive squared norm despite zero mean, and a nonscalar matrix has direction-dependent collision limits; dropping diffusion or angular response requires proof. The full-operator comparison remains PO-017. This isolates a failed inference, not a failure of the flagship mission.

AUD-014 confirms the anisotropic transport profile's punctured Laplacian is not L2 in dimensions 2–4 (and not absolutely L1 in dimension 2). Therefore estimating its omitted diffusion as a separate unregularized L2 forcing cannot work in those dimensions. A different profile/domain, regularized passage, cancellation-compatible norm or direct solution estimate remains possible.

## OBS-013 — coefficient-one radial comparison fails above Coulomb

THM022/V2 and fresh AUD022 prove, for every fixed finite annular tuple with s>d-2 and nu>0, strict reverse comparison for all sufficiently small positive times. Fresh blind reconstruction pending. Leading difference is nu s^2(s+2-d)r0^(-s-2) tau^2, with explicit cubic remainder. Original V1 missing factor s in the transport third derivative is preserved; V2 corrects it to4s^4(2s+2)/N^2. This excludes this same coefficient-one majorant, including arbitrarily small fixed positive diffusivity; it excludes neither a modified majorant nor the full inverse. Logical-wording/source qualifications are separately recorded.

OBS013 final R4 gate: fresh AUD025 now closes the withheld-proof reconstruction, independently controlling killed boundary terms in two ways. Prior AUD022 hostile verdict and wording/source qualifications remain; no stronger full-inverse disproof follows.


R10 accepted exact reduction: complete THM030/031 pass AUD038/039/042. Actual clipped and smoothed approximations vanish, and original singular-noise smallness is equivalent to their actual complementary tail. Positive fixed-time tail smallness remains open. R12 THM033 and R13 THM034 target sufficient subranges using actual Laplacian occupation; their remaining gates must finish before those ranges are accepted. R11 weighted spatial convergence is a separate module and does not itself transfer to the interacting law. No new obstruction to full-inverse existence or the scientific mission is claimed.


## R23 gate / R24 resumption — 2026-09-18 UTC

R23/THM045 is an accepted explicit counterexample to the implication from the stated energy/Haar/separation static class to threshold instantaneous absolute quadratic-source decay. It is not a counterexample to actual iid dynamics or integrated cancellation. Full construction, independent gates and corrected root proof: AUDITS/ROUND_023_GATE_INTEGRATION.md.


2026-09-18 UTC. R24 whole THM047/PO034 accepted: PROVED_CANDIDATE; ISOLATED_RECONSTRUCTION_PASS(AUD067), HOSTILE_REVIEW_PASS(AUD068); VERSION_LOCKED. Complete constructor/blind/hostile and all source/code/evidence root-read; no repair. Exact averaged trace and contraction integral K.D Phi+2c(q-tau), all Cj bounds C sqrt(N), source-specific scalar0, actual absolute scaled lower drift O(N^-1/4), iid endpoint O(sqrt((1+logN)/N)) and smooth true-noise O(N^-3/8) give the entire cubic-plus-residual-martingale L1 equivalence. Both responses, all backgrounds, N2 and fixed-N singular limits retained. THM046/PO033 remains OPEN. See AUDITS/ROUND_024_GATE_INTEGRATION.md and ROUND_024_RECONSTRUCTION_COMPARISON.md.
