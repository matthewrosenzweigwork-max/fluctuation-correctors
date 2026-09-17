# Corrector ledger

| ID | Order | Source canceled | Operator | Counterterm | Scaling | Status | Location |
|---|---:|---|---|---|---|---|---|
| COR-001 | 2 | P_N[J_f] | L_2+B/N | explicit lower drift, no singular subtraction claimed | sigma_N; residual estimates open | EXACT_REDUCTION / smooth analytic candidate | THEOREMS/COR-001_PAIR_CORRECTOR.md |
| COR-002 | 3 | source created by COR-001/nonlinear generator | to derive | to derive | to audit | OPEN | — |

Each corrector card must record final data, symmetry, mean-zero constraints, diagonal behavior, regularity, martingale, contractions, and adjacent-level coupling.


## Round 001 pair reduction

COR-001 uses the full operator L_2=A_x+A_y+R_x+R_y, optionally including B/N in its principal pair transport; exact definitions and finite-N terms are frozen in THM-008. With forcing -J_f and zero terminal data, rho(f)+P[Phi] cancels the intended quadratic source. Its remaining drift is the explicit U_3 interaction plus lower contractions (or the raw D_2[B Phi]/(2N) term if B/N is not incorporated). Status: EXACT_REDUCTION at fixed smooth g, ISOLATED_RECONSTRUCTION_PASS for the algebra; endpoint, residual, bracket, singular and limiting estimates are distinct obligations. COR-002 remains open analytically; its generator couplings are now explicit in THM-001.

The bounded smooth construction is THM-009 (formerly activated PO-001a). It has two proof mechanisms and exact model tests, with separate analytic audit. The corrected identity and precise first residual assertion are frozen in THEOREMS/COR-001_PAIR_CORRECTOR.md and TASKS/ACTIVE/PO-001_RESIDUAL.md. The cubic source is not declared negligible at microscopic criticality.
