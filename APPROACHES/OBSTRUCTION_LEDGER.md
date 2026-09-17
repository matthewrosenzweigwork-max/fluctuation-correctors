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
