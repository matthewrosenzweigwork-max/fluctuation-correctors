# Route registry

| ID | Route | Core mechanism | First obligation | Status | Owner |
|---|---|---|---|---|---|
| R-001 | Hoeffding–Fock/U-statistic | exact generator/chaos recursion | PO-002 | OPEN | — |
| R-002 | Pair/multi-particle Poisson | backward correctors | PO-002 | OPEN | — |
| R-003 | BBGKY/cumulant | independent hierarchy derivation | PO-002 | OPEN | — |
| R-004 | Local Gibbs pressure/stress | deterministic response and critical cell problem | PO-010 | OPEN | — |
| R-005 | Singular renormalization | heat/Fourier/finite-particle cutoff removal | PO-007–009 | OPEN | — |
| R-006 | One-dimensional ordered | gap/quantile and discrete elliptic tools | PO-013 | OPEN | — |
| R-007 | Solvable models | exact checks and coefficient audit | supports all | OPEN | — |
| R-008 | Counterexample/obstruction | falsify closures and uniformity | supports all | OPEN | — |
| R-009 | Source/novelty audit | primary theorem verification | supports all | OPEN | — |

A route is demoted when it repeats the same unproved step, loses the target scale irreparably, relies on a disproved estimate, or is subsumed by a stronger mechanism.

## Round 001 disposition

- R-001: exact finite-smooth all-order drift and bracket recursion obtained, HOSTILE_REVIEW_PASS. First open line: order/cutoff/law-dependent power counting and tails (PO-004/001).
- R-002: full pair operator and bounded smooth inverse obtained as THM-008/009; first open line: scaled cubic and bracket control, then a singular-compatible inverse norm. Bare independent-particle transport and bounded-perturbation treatment of B/N are rejected.
- R-003: separate BBGKY and pathwise reconstruction passes for pair algebra; first open line: quantitative connected-marginal estimates under the actual evolved law.
- R-004: remains OPEN; no local-equilibrium closure begun. First open line: actual moving-law centering/response bridge, not an expectation heuristic.
- R-005: remains OPEN; C^m cutoff-uniform shortcut disproved in OBS-007. First open line: appropriate singular norm or proved joint regularization/model comparison.
- R-006: exact Gibbs map and stopped physical gap generator/reduction; first open line: mobility-aware, temperature/cutoff-controlled dynamic inverse estimate. Numerical source covariance quarantined, all-temperature bounded constant disproved.
- R-007: exact Fourier, small-N, degenerate, coincident-label-position and k>N checks pass; further tests should target new claims rather than repeat these batteries.
- R-008: OBS-001 and OBS-002 are explicit hostile-reviewed counterexamples; OBS-008 is an additional SELF_CHECKED temperature-interface obstruction. Restricted positivity/diagonal-constraint routes remain possible.
- R-009: note labels and primary kernel/source maps completed for this round; numerical covariance normalization and broader source/novelty claims remain OPEN. No novelty claim is made.

The original OPEN route table describes the global theorem routes; these scoped advances do not declare those routes complete. Owners of integrated outputs are recorded in TASKS/QUEUE.md; next proof owner is root until a new bounded task is dispatched.

## Round 002 progress

R-001 now has independent all-order reconstruction (AUD-004) in addition to hostile review; quantitative singular power counting remains OPEN. R-002's first fixed-smooth iid residual has two sealed independent constructions and AUD-005 isolated comparison PASS, with hostile review active. These two constructions share synchronous coupling but use different Hilbert/Fourier implementations; R-003's connected-marginal closure is not thereby proved. R-007 adds nonzero-interaction and moving-background exact tests. R-008 has a new smooth attractive-Gibbs obstruction to law-class transfer awaiting hostile review. R-005 still needs a singular-compatible estimate or joint regularization plus fluctuation-scale model comparison. No source/quarantined-covariance status changes.

## Round 002 final integration

Round 002: fixed-smooth coupling residual and finite-list Gaussian routes close their bounded tasks. All-order moments supply explicit constants and sufficient tails only under separate growth hypotheses; symmetrization repair THM-014 is mandatory. Slow cutoff estimates control their own regularized model. Next active route is the initial iid singular pair interface (TASK-021/022), while fluctuation-scale singular-model comparison, actual higher-corrector norms and physical-gap estimates remain OPEN.

## Round 003 disposition

R-001/R-005: initial iid projection, heat-cutoff and probability interfaces have separate constructions and reviews. R-008: raw-pair variance obstruction and the sharp probability-converse candidate distinguish norm failure from probability failure. R-007/R-002: the exact internal-pair transport model retains B/N, produces a shrinking finite-amplitude core and quantifies the omitted angular diffusion. The natural next line is PO-017, a full-operator comparison controlling that core; no route may substitute g for the actual corrector. R-003 positive-time marginals, R-004 moving static response, R-006 mobility-aware gap estimates and R-009 quarantined source constant remain open as previously recorded.

Round004 disposition: the diffusion-retaining local pair route passes THM020/AUD020/021 for d>=s+2. The same coefficient-one majorant above that range has the precisely scoped THM022 obstruction (hostile pass; blind pending). The finite-measure nonlocal response route passes THM021/AUD023/024. R5 now attempts a direct periodic full-response initial norm via a constructed singular Markov base and bounded-response composition, with separate fresh audits, prescribed uniform data and bounded diffusivity. Actual-data regularity, domain/gradient passage and positive-time law control remain the next unproved interfaces; the mission is unchanged.

R5 direct-norm route has passed periodic base and conditional composition modules (THM023/024,AUD026/027). The full prescribed-data/actual homogeneous interface remains under fresh review with explicit source and common-constant qualifications. This sharpens PO017 toward the pair-kernel domain and evolved-law residual/bracket interface; it does not solve the singular flagship.

R5 direct norm route passes the prescribed/homogeneous initial gate via THM023–025/AUD026–029, bypassing any need to compare with the toy diagnostic. Literal diagnostic closeness remains unproved. Continue exact finite-N particle construction and weighted-gradient/domain route; keep evolved residuals/brackets and critical infinite-order control open.

R6 full-energy route passes THM026/AUD030/031, including simultaneous collisions,global energy integrability,actual heat paths and bounded-density domination. Continue weighted derivative and homogeneous particle-domain construction; the gradient seed may support higher variations but neither proof nor asymptotic estimates are assumed. Exact source/response and centering conventions remain.
