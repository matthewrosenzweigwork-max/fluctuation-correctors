# Corrector ledger

| ID | Order | Source canceled | Operator | Counterterm | Scaling | Status | Location |
|---|---:|---|---|---|---|---|---|
| COR-001 | 2 | P_N[J_f] | L_2+B/N | explicit lower drift, no singular subtraction claimed | sigma_N; residual estimates open | EXACT_REDUCTION / smooth analytic candidate | THEOREMS/COR-001_PAIR_CORRECTOR.md |
| COR-002 | 3 | source created by COR-001/nonlinear generator | to derive | to derive | to audit | OPEN | — |

Each corrector card must record final data, symmetry, mean-zero constraints, diagonal behavior, regularity, martingale, contractions, and adjacent-level coupling.


## Round 001 pair reduction

COR-001 uses the full operator L_2=A_x+A_y+R_x+R_y, optionally including B/N in its principal pair transport; exact definitions and finite-N terms are frozen in THM-008. With forcing -J_f and zero terminal data, rho(f)+P[Phi] cancels the intended quadratic source. Its remaining drift is the explicit U_3 interaction plus lower contractions (or the raw D_2[B Phi]/(2N) term if B/N is not incorporated). Status: EXACT_REDUCTION at fixed smooth g, ISOLATED_RECONSTRUCTION_PASS for the algebra; endpoint, residual, bracket, singular and limiting estimates are distinct obligations. COR-002 remains open analytically; its generator couplings are now explicit in THM-001.

The bounded smooth construction is THM-009 (formerly activated PO-001a). It has two proof mechanisms and exact model tests, with separate analytic audit. The corrected identity and precise first residual assertion are frozen in THEOREMS/COR-001_PAIR_CORRECTOR.md and TASKS/ACTIVE/PO-001_RESIDUAL.md. The cubic source is not declared negligible at microscopic criticality.

## Round 002 COR-001 residual

The fixed-smooth iid pair corrector has negligible endpoint, cubic/lower residual, self bracket and one-body cross bracket at the frozen sigma scale for every beta_N>0 (THM-010 candidate; AUD-005 isolated pass, hostile pending). The pair PDE and its full operator remain unchanged. This does not say the singular critical pair corrector or all higher corrections vanish. Order/cutoff bounds and singular model comparison are separate open tasks.

Round 002 review update: AUD-006 now grants HOSTILE_REVIEW_PASS for the bounded residual estimates, fixed-data norm qualification and Gibbs law-class obstruction in the precise scopes above. The singular and other open interfaces are unchanged.

## Round 002 final integration

Round 002: the pair corrector residual closes in the fixed-smooth iid class (THM-010). The direct one-body reconstruction of THM-011 needs no pair correction once the same fixed-smooth second moment is available; it does not eliminate the singular campaign's corrector problem. All-order root formulas must use symmetric kernels or averaged symmetrization (THM-014). Kernel growth sufficient for an infinite hierarchy is still unproved.

## Round 003 initial corrector interface

The exact iid bound (THM-015) reduces the actual initial endpoint to b_N||Phi_0^N||_L2(mu_0^2)^2/N->0 when L2 is available. This sufficient premise is not proved for COR-001's singular full solution. Bare-potential THM-016/018/019 are diagnostics, not replacements for Phi.

THM-017 retains internal B/N exactly in a zero-diffusion quadratic-source Euclidean model and exhibits a finite radial core. Its explicit periodic-cutoff diagnostic has a negligible iid endpoint for every s<d. COR-001 still includes the full L_2 and the actual source. The specific missing comparison is PO-017; no new full-corrector order is closed by the toy solution, and no finite critical truncation is inferred.

## Round 004 retained diffusion

THM020 retains 2nu Delta together with internal B/N in a local relative-coordinate auxiliary model. Its inverse is constructed in a bounded Borel true-martingale class; no classical diagonal trace or gradient/bracket regularity is supplied. The periodic cutoff diagnostic remains separate from COR001. Both response terms, ordinary transport, true test/source and periodic remainder are still required. No new hierarchy order is closed.

R5 THM025 supplies the genuine second-order full pair inverse under prescribed uniform data and actual homogeneous data, with both responses and exact J. Its initial iid endpoint now passes AUD028/029. It remains a bounded Borel/Haar L2 inverse, not yet a particle Ito test. PO022 weighted first derivatives and PO023 full domain are separate; no higher-order corrector tail is controlled.

THM027 adds genuine weighted C1 derivatives and global weak Haar H1 to the full COR001 inverse, retaining both responses and exact source. Fresh AUD032/033 pass, with fixed-N constants. THM028's C1time/C2space and exact actual-particle identity remain a separately submitted candidate under fresh review. No extra corrector order or critical tail has closed.

R8 THM028 passes the actual homogeneous COR001 particle domain. The true full inverse, both responses and exact source appear in a justified singular Ito identity with its true square-integrable martingale. This adds no higher corrector or critical tail closure. Uniform self/cross noise and the evolved cubic residual remain PO024/PO001.
