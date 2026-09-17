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
