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

## Round 004 local diffusion gate

THM-020: complete local diffusion-retaining construction for d>=3,0<s<=d-2 and every finite nu>=0. Bounded Borel true-martingale inverse, global collision-free pathwise realization, annular killing/exhaustion and coefficient-one radial domination are constructed. Its cutoff diagnostic has the all-N initial iid endpoint. Fresh AUD-020 reconstruction PASS includes a separate all-N addendum, preserving the original large-N wording. Fresh hostile TASK035 is pending; no hostile status yet. Classical regularity, full periodic operator, actual test/background uniformity and evolved-law estimates remain unclaimed. Complete constructor and reconstruction reports are under MEMORANDA/ROUND_004_DIFFUSIVE_*.md.

THM020 final local verdict: fresh AUD021 (AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_REVIEW.md,07f61e5fc8aed7f2a6a7b2dbfbcb8dce174a433b0db8bd684db62908717f85b2) grants HOSTILE_REVIEW_PASS to all 16 mathematical claims, including class/domain construction and all-N endpoint. AUD020 independently reconstructed the same submitted scope. TASK035-E01 is rendering-only, corrected by a separate erratum without changing proof bytes. Extra claims in the reconstruction outside THM020 retain their separate constructed status. The local proof gates are passed; classical/full-operator/evolved-law gates are not.

## Round 004 response and range dispositions

THM-021: PROVED_CANDIDATE / fresh ISOLATED_RECONSTRUCTION_PASS (AUD024) and HOSTILE_REVIEW_PASS (AUD023) / VERSION_LOCKED. Exact finite-measure divergence and compensated responses, Borel/Haar operators, heat convergence and its two exclusions, smooth-cutoff pair propagation and prescribed-forcing mild equation pass in the frozen scope. Full constructor and fresh statement-only reports were read and compared; fresh hostile review passes all17 scoped claims. The differential-spacing typo is preserved with a separate erratum. No singular propagator or actual forcing theorem follows.

THM-022: PROVED_CANDIDATE / fresh HOSTILE_REVIEW_PASS (AUD022) / VERSION_LOCKED. V2 proves strict small-time killed-annular reverse comparison for every fixed admissible tuple in s>d-2,nu>0. V1 Taylor-bound error is preserved, with the V2 correction and separate logical-wording erratum. A fresh statement-only TASK042 is active; no blind pass yet. This disproves extension of the same coefficient-one radial majorant, not a full singular inverse.

THM-023/024: R5 submitted periodic-base and conditional-composition cards, respectively PROVED_CANDIDATE and CONDITIONAL, SELF_CHECKED / VERSION_LOCKED. Fresh separate TASK040/041 reconstruction/hostile reviews are active; no passed R5 gate inferred.

THM022 final bounded verdict: fresh AUD025 comparison reads the independent two-route TASK042 reconstruction in full and matches every fixed-tuple/every-small-time quantifier to V2. ISOLATED_RECONSTRUCTION_PASS plus prior AUD022 HOSTILE_REVIEW_PASS, with original coefficient error and wording/source qualifications preserved. THM023/024 have fresh hostile PASS from TASK041/AUD026; their just-sealed blind report has not yet been root-compared. THM025 interface/homogeneous candidate has fresh TASK043/044 active; no pass yet.

Round005 module gate: THM023 now PROVED_CANDIDATE with fresh ISOLATED_RECONSTRUCTION_PASS(AUD027) and HOSTILE_REVIEW_PASS(AUD026); THM024 has both statuses as a CONDITIONAL implication. All finite-N/time/representative/heat-passage claims were root-compared after both seals. Actual-data/full-interface THM025 remains pending; its reviewer flags a card-only local-kernel source bridge and common lower-divergence constant qualification. No theorem or issued report is edited to hide those findings.

## Round005 full-interface gate

THM025 is PROVED_CANDIDATE / ISOLATED_RECONSTRUCTION_PASS(AUD029) and HOSTILE_REVIEW_PASS(AUD028, candidate plus separate source/constant addendum) / VERSION_LOCKED. Fresh TASK043 reconstructs every interface, Fourier actual-data and iid claim; root read and compared all577 lines and reran2672 exact checks. Fresh TASK044 originally gives REPAIR_REQUIRED for a card-only local-kernel premise and implicit constant identification. The original report remains unchanged. Supplemental TASK047, the same reviewer after seal, checks the exact pre-existing R4 sources and common maximum constant, discharging D1/D2 for the candidate-plus-addendum; report62046b559ab5f922bde4dd568aa9420ef96c5f6ee9428beeb38a5d857b25f87d. This is a reused-context source recheck, not another fresh blind review. Underlying THM021/023 have their own fresh gates. Symmetry means coordinate exchange; the source-local C0 names are distinguished. No theorem range, normalization, centering, rate or law class changes.

THM023/024 and THM025 now give the true prescribed-data bounded Borel full pair inverse and initial iid endpoint; homogeneous actual data meet the hypotheses. The initial endpoint's uniform beta lower bound is explicit. The finite-particle corrector domain and evolved-law/critical gates remain OPEN. THM026 particle candidate is complete with fresh AUD031 reconstruction PASS; fresh TASK048 hostile pending. THM027 weighted gradient assertion is frozen OPEN, with separate construction and fresh blind tasks active. These next-gate candidates are not promoted by R5.

## Round006 finite-particle gate

THM026: PROVED_CANDIDATE / fresh ISOLATED_RECONSTRUCTION_PASS(AUD031) and HOSTILE_REVIEW_PASS(AUD030) / VERSION_LOCKED. AUD030 is AUDITS/HOSTILE/ROUND_006_PARTICLE_REVIEW.md, SHA256888687713aa9d87b4af6ac6d13b4db76380e2f80ca12d85fadc0cc95d3307fef. It passes all21 claims and accompanying global finite-mean energy identities, no failed line/repair. Root read237 hostile lines and the complete constructor/blind proofs, verified all seals and reproduced4910 hostile exact checks in a fresh writable directory, byte-identical to the read-only issued result. THM026's card/candidate remain unchanged. The density exponent and fixed-start heat quantifiers remain exactly scoped; no corrector-domain or uniform-N law result.

THM027 remains OPEN with construction/fresh reconstruction active. THM028 freezes a new homogeneous full-corrector domain assertion, OPEN/UNAUDITED, before TASK051 constructor work. Its higher derivatives,time derivative,internal-drift L1 cancellation and exact particle identity are targets, not consequences already inferred from THM026 or an unreviewed gradient lemma.

## Round007 first-gradient gate

THM027: PROVED_CANDIDATE / fresh ISOLATED_RECONSTRUCTION_PASS(AUD033) and HOSTILE_REVIEW_PASS(AUD032) / VERSION_LOCKED. Constructor eb65ed8680416032ca2667db1cab9b39b493fcb1c578985c632a8bbfd1e9953a; blind3ea53ef66a94ab1eb1217debd5dcdd106cb14e8a3aa6c95f8f76b56549f837a7; hostile eefb435655439df4e5c13f5aada458c9ece4cd9c80faaafa421faa3468f765c9. Root read/compared the complete proofs and reran5992/10327/5468 exact checks. All19 hostile groups pass with no mathematical repair; the line427 spacing token receives a separate erratum. Weights and common-flow routes differ validly. All prescribed-data, bounded-noise and fixed-N limitations remain. H1 supplies no particle Ito identity by itself.

THM028 is PROVED_CANDIDATE / SELF_CHECKED / VERSION_LOCKED at submission, with fresh TASK053/054 reconstruction/hostile reviews active. Root read798 lines and reproduced4405 checks including18 input hashes; no independent verdict yet. THM029 is OPEN/UNAUDITED at freeze, conditional on the THM028 domain premise, with TASK055 constructing uniform Haar noise energy and the exact interacting-law reduction. No actual evolved bracket estimate is asserted.
