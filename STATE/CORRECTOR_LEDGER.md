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

R9 THM029 adds an N-uniform nu-weighted Haar gradient-energy bound for the same genuine COR001. It retains source, both responses and full domain. This closes reference self/cross-noise functionals only. Actual-law tail/correlation control, evolved cubic residual and all higher-corrector closure remain separate open tasks.


The same genuine COR001 now has R10 actual bounded-field approximation reductions, keeping both response terms and exact source. No new higher corrector is constructed. R11 spatial limit, R12 strict sub-Coulomb noise, and R13 bounded-noise small-s candidates are separate modules awaiting their own remaining audit gates; no approximate vector-field martingale is silently substituted for COR001.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 accepted actual-noise gate: THM033 passes fresh AUD040 reconstruction and AUD041 hostile review. In the homogeneous strict sub-Coulomb bounded-chi family, Q_N<=C b_N N^(s/(s+2))(N^(-(1-s/d))+nu). Critical decay holds when s(s+2)<2d; bounded-chi decay also holds for s<min(2,d-2), and the exact other sufficient conditions remain in the card. The accepted R8 domain and R10 sharp floor separately supply the conditional premises. Outside these ranges PO024 is OPEN; within them PO001's actual integrated cubic/lower drift is the first open assertion. No fluctuation law or hierarchy closure follows.

THM032 spatial and THM034 actual-noise gates now pass both fresh axes. They concern the same full terminal-zero pair inverse with both response slots, not a new corrector or truncated construction. R11 weighted local C1/global W1,1 response-only limit is a separate module; R13 uses earlier fixed-N derivative/domain modules and does not require R11. Cubic C Phi and the next hierarchy remain open.


Round014 final gate,2026-09-18 UTC. R14 THM035 preserves the genuine full pair inverse and terminal source, both responses and R8 representatives. The lower-plus-scalar drift now has accepted uniform scaled decay in its exact bounded-chi range. Cubic smallness, general evolved endpoints and higher orders are separate claims. No cutoff inverse is substituted.


Round015 final gate,2026-09-18 UTC. R15 genuine full pair inverse remains unchanged. The terminal-zero exact R8 identity plus accepted actual source bound, initial endpoint, lower contractions and whole martingale give actual integrated cubic smallness in the critical restricted range. This neither bounds the instantaneous absolute cubic nor certifies all higher correctors.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R17 first-order route, conditional on the separate actual source bound, needs no pair inverse, pair-domain,cubic or corrector-noise module. This nondependency does not erase accepted corrector results or close the higher hierarchy. THM040 is a new finite-list probability target, not a new corrector or silent hierarchy truncation.


R17 final gate,2026-09-18 UTC. R17 is accepted by a direct first-order actual-source route, without pair inverse or higher-corrector hypotheses. Earlier corrector results remain accepted in their scopes. No all-order hierarchy truncation is inferred.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 finite-list candidates use genuine first-order source control and bounded smooth one-body martingales. Pair inverse/noise/cubic modules remain valid independent earlier work, not prerequisites or deleted routes.


R21 root synthesis,2026-09-18 UTC. New THM043/PO030 freezes actual integrated critical U3 decay throughout the entire strict R12 noise-decay range d>=3,0<s<d-2,s(s+2)<2d. Root TASK093 complete exposed working proof MEMORANDA/ROUND_021_CRITICAL_CUBIC_SYNTHESIS.md is UNSEALED/UNAUDITED. It composes accepted R5 initial endpoint, R8 actual domain/identity, R12 whole bracket, R14 both lower contractions and R16 source. The conditions imply s<d/2 and3s<2d-2; critical chi tends to0. Exact four-term bound is C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa], with p=s+2,a=s/p,theta=1-s/d and R14 midpoint q,kappa=(2q-s)/(2p)>0. No instantaneous absolute U3 claim. Root fresh diagnostic12531 assertions/18categories/4mutationfamilies passes but full source/exposure/seal packet and both independent gates remain outstanding. TASK094/AUD061 reserved fresh R21blind andTASK095/AUD062 reserved separate hostile, not yet written. Next freeTASK096,AUD063,THM044,PO031. R20 TASK091/AUD059 prepared blind retains next available worker priority; TASK092/AUD060 reserved R20hostile. No earlier card changed or independent status assigned.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.

R20/R21 subsequent status at R18/R19 acceptance: R20 constructor sealed; independent blind and hostile active. R21 root source/exposure/diagnostic packet is now sealed SELF_CHECKED (29 inputs,38 archive members); fresh TASK094/AUD061 whole reconstruction active, TASK095/AUD062 hostile still reserved. Earlier unsealed entries above are chronological history. Neither new theorem is promoted. Current exact pointers/hashes are STATE/CAMPAIGN_STATE.md.


R21 final whole gate accepted,2026-09-18 UTC. THM043/PO030 is PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS (AUD061) and HOSTILE_REVIEW_PASS (AUD062), with exact published source/gate matching. The full strict range d>=3,0<s<d-2,s(s+2)<2d at finite positive microscopic critical lambda is retained. The actual integrated cubic residual obeys sigma E|integral U3[C Phi]dt| <= C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa] ->0. Absolute value remains after time integration; the genuine pair inverse retains both responses, the exact R8 domain, full true martingale and both lower contractions rho[g]/N+c/(2N). No instantaneous cubic estimate, Coulomb endpoint, Gaussian law or hierarchy is inferred. Root complete source/candidate/527-line blind/249-line hostile reading and twelve-item comparison are AUDITS/ROUND_021_GATE_INTEGRATION.md and ROUND_021_RECONSTRUCTION_COMPARISON.md. All29/29/32-input38/38/42-member packets verify unchanged; fresh diagnostics12531/117352/137147 reproduce saved bytes. The hostile stdout-only extra newline is explicitly recorded and no evidence normalized. All-real exponent implications are proved analytically; finite computations support but do not certify them. Earlier pending entries are chronological history.
