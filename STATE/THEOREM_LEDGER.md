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

## Round 003 initial iid interface

- THM-015: exact arbitrary-law iid L2 pair projection identity and sharp universal second-moment constant, with frozen Haar Riesz heat-cutoff powers. ISOLATED_RECONSTRUCTION_PASS (AUD-011) and HOSTILE_REVIEW_PASS (AUD-012). Universal sharpness does not imply optimality on a one-point probability space. Numerical heat constants have hostile review; their exact constants were not independently reconstructed blind.
- THM-016: unregularized integrability/infinite second-moment boundary, sufficient probability convergence including 2s=d, and the temperature condition above it. Statement-only ISOLATED_RECONSTRUCTION_PASS (AUD-013) and HOSTILE_REVIEW_PASS (AUD-012). All results are initial iid Haar assertions. The frozen sufficient statement remains unchanged even though later cards strengthen it.
- THM-017: exact zero-diffusion internal-pair transport model, collision behavior and separately defined compact periodic diagnostic endpoint. Complete proof; separate hostile TASK-027 pending at this entry. It is not the full corrector.
- THM-018: independent TASK-024 Section 7 L1 extension with explicit constants. Complete proof; separate hostile TASK-026 supplement pending at this entry. THM-016 has not been silently edited.
- THM-019: root sharp lower-probability bound, matching absolute-moment order, necessary-and-sufficient temperature criterion, tightness/non-tightness classification. Complete proof; hostile TASK-026 and statement-only TASK-028 pending at this entry. No endpoint distribution or dynamic counterexample is asserted.

All R3 claim-specific independent reviews reuse contexts with disclosed prerequisite history. None supplies the strict fresh-session publication gate. Submitted cards/proofs preserve their status-at-submission and hashes; subsequent dispositions appear below and in the round report.

### Round 003 subsequent sealed verdicts

AUD-015, AUDITS/HOSTILE/ROUND_003_SHARP_IID_REVIEW.md (ba52e9f7267690d657affc0a52d2554d07f19b579fc2d115f9fc4717b6ea35d5), gives separate HOSTILE_REVIEW_PASS for THM-018 and THM-019, including explicit constants and all consequences. Note SH-01 completes the further-subsequence extraction needed by one sentence in the root proof; theorem/card, constants and hypotheses are unchanged, and original proof bytes remain sealed. The review is new-claim independent with context reuse disclosed. A genuinely fresh statement-only THM-019 reconstruction is now active after an earlier worker completed (DEC-016); no completed verdict is inferred from its dispatch.

AUD-014, AUDITS/HOSTILE/ROUND_003_PAIR_TRANSPORT_REVIEW.md (efdf3a67f17b66e751680183baad8062ef8429b0be4bb851cdd2f7f118b950ce), gives HOSTILE_REVIEW_PASS for THM-017. It explicitly supplies the finite-N constant enlargement needed by the card's all-N reading, using the original global amplitude bound. All candidates remain unchanged. Its additional punctured Laplacian observation rules out a separate L2 diffusion forcing estimate for the anisotropic transport profile in dimensions 2–4; it is not a full-solution nonexistence result. AUD-016 gives the prior-context statement-only reconstruction PASS for THM-019. Newly accepted fresh TASK029/030/031 provide a separate pending audit lane, with their own seals required before any fresh-pass claim.

Fresh evidence now issued: AUD-017 is the root comparison of fresh TASK029 (report 2c94d999d2508e1acb105930f4b32149358e08f547bf85cf95cea1bbdd58b480), granting FRESH ISOLATED_RECONSTRUCTION_PASS for THM019 in d/2<s<d. AUD-018, AUDITS/HOSTILE/ROUND_003_FRESH_HOSTILE_REVIEW.md (ab53a9b6e542ef6c7009ca6e4c83b823766a6c5f6c91d9701707250817a2014a), grants fresh HOSTILE_REVIEW_PASS for THM017/018/019 and checks the used exact iid/local normalization prerequisites directly. FH-C01 and FH-C02 supply the same all-N and subsequence clarifications independently. FH-D01 fails only the overbroad subcritical clause in the separate unpromoted root rescaling note; its explicit correction is RET002/the separate erratum. THM019's specific fresh reconstruction/hostile gates are closed. THM018 has fresh hostile review and a constructed extension, not a separately staffed fresh full-range blind proof. Fresh THM017 reconstruction remains pending until its seal.

Fresh TASK031 is now sealed: AUD-019 records FRESH ISOLATED_RECONSTRUCTION_PASS for THM017 in its pointwise forward absolutely-continuous characteristic class, all-N norm bounds and deterministic-time iid endpoint. Different explicit cutoffs realize the same declared cutoff family; no identity of those examples is claimed. The extra Hessian/Laplacian/annular-source observations retain separate fresh hostile evidence rather than this reconstruction status.
