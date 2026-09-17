# Proof-obligation ledger

| ID | Obligation | Depends on | Status | Owner | Evidence |
|---|---|---|---|---|---|
| PO-001 | Scaled cubic residual, endpoint and correction brackets under stated law | PO-002, PO-001a | OPEN | root, next worktree unassigned | TASKS/ACTIVE/PO-001_RESIDUAL.md |
| PO-002 | Exact full pair linearized operator | duality normalization | EXACT_IDENTITY / isolated and hostile pass | root integrates algebra+BBGKY | THM-008; AUD-001/002 |
| PO-003 | Exact all-order generator recursion and bracket matchings | PO-002 | EXACT_IDENTITY / HOSTILE_REVIEW_PASS | recursion + hostile | THM-001, recursion report R1–R5 |
| PO-004 | Critical power-counting theorem | PO-003 | OPEN | unassigned | — |
| PO-005 | Smooth-kernel subcritical tail control for arbitrary \(\lambda_N\to0\) | PO-003, PO-004 | OPEN | unassigned | — |
| PO-006 | Smooth-kernel critical resummation/closure | PO-004 | OPEN | unassigned | — |
| PO-007 | Hilbert–Schmidt singular cutoff removal | PO-005 | OPEN | unassigned | — |
| PO-008 | Borderline logarithmic counterterm | PO-003 | OPEN | unassigned | — |
| PO-009 | Ultraviolet pair-field/finite-particle closure | PO-003 | OPEN | unassigned | — |
| PO-010 | Moving-background centering accuracy | static response | OPEN | unassigned | — |
| PO-011 | Static-to-dynamic local response input | source/new proof | OPEN | unassigned | — |
| PO-012 | Field/path tightness for corrected observable | finite-dimensional theorem | OPEN | unassigned | — |
| PO-013 | One-dimensional positive-temperature closure | ordered route | OPEN | unassigned | — |

Add exact statements, negations, and proof locations as obligations are activated.

## Round 001 activated assertions

- PO-002: exact full pair operator reconstructed in THM-008 and independent BBGKY report. Coefficients agree after mapping the triple symmetrization conventions. ISOLATED_RECONSTRUCTION_PASS for smooth finite N; hostile review passed in AUD-002.
- PO-001a: complete fixed-smooth backward pair estimate, in fact uniform for every nu>=0 and N>=2 conditional on the explicitly displayed norms. Two proof mechanisms and three solvable tests completed in THM-009/smooth memorandum; separate analytic review AUD-003 passes both the statement-only reconstruction and hostile review, with exact scope disclosed.
- PO-001 (remaining target after algebra): law-specific scaled corrected-observable residual control. A sufficient assertion must control in probability or L1 the integrated cubic/lower-order drift, the endpoint corrector and corrector/cross brackets, uniformly in the particle and temperature regimes and Riesz cutoff. Reference: independent BBGKY report equations (7.1)-(7.3). An expectation estimate alone is insufficient.
- PO-003: exact general recursion and all shared-label bracket contractions proved and hostile-reviewed. PO-004 critical power counting remains OPEN and is not inferred from fixed-smooth algebra.
- No private source theorem is a dependency of these exact smooth calculations.

PO-001a is discharged within its fixed-smooth scope by THM-009 and AUD-003. The next first open line is item 2 of TASKS/ACTIVE/PO-001_RESIDUAL.md, with companion endpoint/bracket bounds. Its singular extension and PO-004 are not discharged.
