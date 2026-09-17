# Theorem ledger

| ID | Statement | Regime | Law/centering | Math | Audit | Source | Proof location |
|---|---|---|---|---|---|---|---|
| THM-001 | Exact all-order smooth drift and full bracket contraction hierarchy | every finite k,N; fixed smooth g | arbitrary initial law, mean-field centered | EXACT_IDENTITY | HOSTILE_REVIEW_PASS and ISOLATED_RECONSTRUCTION_PASS (AUD-004) | self-contained proof, no external theorem imported | THEOREMS/THM-001_SMOOTH_RECURSION.md |
| THM-002 | Smooth-kernel subcritical and critical fluctuation theorem | \(\lambda_N\to0\) or \(\lambda\) | separate rows required | OPEN | UNAUDITED | UNCHECKED | — |
| THM-003 | Singular full microscopically subcritical theorem | \(\lambda_N\to0\) | separate iid/Gibbs and centerings | OPEN | UNAUDITED | UNCHECKED | — |
| THM-004 | Singular microscopically critical theorem | \(\lambda_N\to\lambda\in(0,\infty)\) | to determine | OPEN | UNAUDITED | UNCHECKED | — |
| THM-005 | Sharpness/obstruction beyond target range | supercritical and bad centerings | multiple | OPEN | UNAUDITED | UNCHECKED | — |
| THM-006 | One-dimensional ordered positive-temperature theorem | subcritical/critical | separate law rows | OPEN | UNAUDITED | UNCHECKED | — |
| THM-007 | Extensions | after flagship | to determine | OPEN | UNAUDITED | UNCHECKED | — |

Every theorem must eventually have a separate card under `THEOREMS/` or `CANDIDATES/` with exact quantifiers and logical negation.

## Round 001 additions and audit scope

| ID | Statement | Math | Audit | Source/proof |
|---|---|---|---|---|
| THM-008 | Exact smooth one-body and pair drift, trace cancellation, martingale and cross brackets | EXACT_IDENTITY | ISOLATED_RECONSTRUCTION_PASS (AUD-001) and HOSTILE_REVIEW_PASS (AUD-002) | frozen card, algebra and BBGKY memoranda |
| THM-009 | Explicit backward pair C^m estimate, uniform N>=2 and nu>=0 given displayed fixed-smooth norms | PROVED_CANDIDATE | ISOLATED_RECONSTRUCTION_PASS and HOSTILE_REVIEW_PASS (AUD-003, same fresh reviewer in two documented phases) | card and smooth memorandum |

AUD-002 is AUDITS/HOSTILE/ROUND_001_HOSTILE.md, hash d0a03745045f4a7e647c6a175dd803fbbbe2c990943ff29a49f090da3d20325d. It also accepts the two explicit counterexamples in the falsification memorandum. It is a fresh context with exact hashed inputs. THM-001's hostile proof review does not imply a separate blind reconstruction of the general recursion. M0 and M1 now pass for the frozen smooth starting model. M2 remains OPEN because critical power counting is not proved; THM-002 through THM-007 remain OPEN, not conditional theorems merely from this algebra.

Frozen submitted cards and issued worker/audit reports retain their original status-at-submission wording and hashes. This ledger and the dated round report record subsequent promotion; no audit input was rewritten to reflect its own verdict.

AUD-003 consists of ROUND_001_ANALYTIC_RECONSTRUCTION.md, ROUND_001_ANALYTIC_REVIEW.md and its identifier addendum. One fresh reviewer saved a statement-only reconstruction before reading the constructor proof, then performed hostile review. The candidate constants were visible; these are not two separately staffed audits. Both phases PASS; the cutoff diagnostic also passes in the explicit Fourier-sequence scope. Candidate card/report bytes remain frozen. The canonical analytic identifier is THM-009. No author acceptance, publication permission, or singular theorem promotion is implied.

## Round 002 candidates and reconstruction

THM-010, THEOREMS/THM-010_SMOOTH_IID_RESIDUAL.md: PROVED_CANDIDATE for the precise fixed-smooth iid PO-001 subclaim. Independent constructions are sealed in ROUND_002_COUPLING.md and ROUND_002_FALSIFICATION.md. AUD-005 comparison gives ISOLATED_RECONSTRUCTION_PASS for the assertion and quantitative orders; constructor constants and root smooth-data qualification subsequently passed AUD-006. Both constructions use synchronous coupling with different moment/norm implementations; no independent BBGKY closure is claimed. The singular PO-001 extension and M2 critical power counting remain OPEN.

AUD-004 (Round 002) now supplies the previously pending isolated general reconstruction of THM-001. Frozen submission cards and historical Round 001 wording remain unchanged. M2 still requires critical power counting.

AUD-006, AUDITS/HOSTILE/ROUND_002_RESIDUAL_REVIEW.md (hash 7e541f928f15236c15cd44572ac4d6f28abcbfde8ecd86cf616de14a586f8ca9), grants HOSTILE_REVIEW_PASS for THM-010 including its explicit constants, both residual proofs, root fixed-data qualification (D1)-(D3), and the separate Gibbs obstruction. Together with AUD-005, the precise fixed-smooth iid PO-001 subclaim is discharged. The root qualification has hostile review only, not a separately staffed blind reconstruction. One cosmetic form-feed defect is corrected by a separate rendering erratum; original inputs remain frozen.

THM-011, THEOREMS/THM-011_SMOOTH_GAUSSIAN_CRITERION.md: complete bounded proof, HOSTILE_REVIEW_PASS (AUD-007), with statement-only comparison PASS (AUD-008; prerequisite context reused, not a fresh session). Finite-dimensional Gaussian limit under convergent explicit initial/noise covariances; uniform characteristic approximation, O(N^-1) mean-field bias, beta->0 degenerate limit. No field or singular statement; zero-diffusivity kernel convergence is now proved separately in THM-013, hostile PASS (AUD-010).

## Round 002 final qualifications

- THM-012: original all-order submission preserved. Its unrestricted compact first-slot derivative identity is DISPROVED / HOSTILE_REVIEW_FAIL by AUD-009 and OBS-010. The quantitative bounds and symmetric interpretation pass. No unconditional use of this submitted identity is allowed; repaired claim has new ID THM-014.
- THM-013: complete fixed-smooth diffusivity-continuity proof with explicit constants and constructed inviscid reference; HOSTILE_REVIEW_PASS (AUD-010). Positive-diffusivity existence remains the model assumption. No separate blind reconstruction has been staffed.
- THM-014: replacement of THM-012 using explicit averaged symmetrization in rooted identities; original moment/bracket constants and conditional series/cutoff criteria retained. HOSTILE_REVIEW_PASS in the separate AUD-009 repair review, hash ecf88eb3262d203352ef84c7a547837dbca0b16866752ba41eccb3211cc2579e. No blind all-order quantitative reconstruction is claimed.
- The independent Gaussian statement-only report uses a direct quadratic-source estimate, whereas the constructor uses pair correction. AUD-008 confirms the same limit and centering; it does not separately audit the constructor's stronger L2 remainder/constants. Audit contexts reused for new claims are disclosed, and the strict fresh-session publication gate is not represented as passed.
- THM-002 has a proved fixed-smooth iid finite-list subclaim under the stated mean-field existence/regularity hypotheses and identified physical-temperature limits. The broader frozen law-class and gate scope remain OPEN. THM-003/004 and M2 remain OPEN; field/path tightness remains unclaimed.
