# Martingale and quadratic-variation ledger

| ID | Origin | Integrand | Scale | Quadratic variation | Cross-variation | Limit | Status |
|---|---|---|---|---|---|---|---|
| MG-001 | one-body fluctuation | \(\nabla f(x_i)\) | to freeze | known form to rederive | with corrector martingales | Gaussian baseline | OPEN |
| MG-002 | pair corrector | pair gradient/force discrepancy | to derive | to derive | MG-001 and MG-003 | may survive | OPEN |
| MG-003 | k-body corrector | k-body gradient | to derive | to derive | all adjacent levels | critical resummation | OPEN |

Every martingale theorem must prove:

- exact finite-N normalization;
- predictable quadratic and cross variations;
- tightness/Lindeberg or martingale-problem conditions;
- cutoff removal and uniform integrability;
- whether correction martingales alter covariance or create higher chaos;
- compatibility with initial fluctuations.


## Round 001 formulas

Write H_i[Phi]=N^{-1}sum_{j!=i}grad_x Phi(x_i,x_j)-integral grad_x Phi(x_i,y)mu(dy).

- MG-001: dM_f=sqrt(2nu) N^{-1}sum_i grad f(x_i).dW_i; bracket 2nu N^{-1}eta(grad f.grad q)dt.
- MG-002 in P=U_2/2 convention: dM_Phi=sqrt(2nu)N^{-1}sum_i H_i[Phi].dW_i; pair bracket 2nu N^{-2}sum_i H_i[Phi].H_i[Psi]dt; cross bracket with MG-001 replaces first H by grad f.
- Corrected bracket is 2nu N^{-2}sum_i |grad f(x_i)+H_i[Phi]|^2dt. A cross term may affect the limiting covariance.
- Exact label contractions are displayed in algebra (5.2)-(5.3) and BBGKY (3.9)-(3.10); their coefficients independently agree. Finite-smooth identities exact; limiting brackets, tightness and cutoff passage OPEN.

## General bracket

For U_k, Gamma_{k,i}=grad_{x_i}U_k=(k/N)V_{k-1}^{(i)}[grad_1 Phi(x_i,.)], with denominator N and label i excluded. M_k=sqrt(2/beta_N) sum_i integral Gamma_{k,i} dW_i. Every predictable cross bracket is 2/beta_N sum_i Gamma_{k,i} dot Gamma_{ell,i}; all partial shared-label bijections are expanded in recursion report (R5). Square integrability follows from fixed-smooth bounded kernels on finite time. These bounds do not establish vanishing of sigma_N-scaled correction brackets or cross variations under a singular cutoff.

## Round 002 bounded noise estimates

THM-010 gives E[M_Phi]<=2TH^2/(beta N^2) and E TV([M_f,M_Phi])<=2TL_fH/(beta N^(3/2)) under the actual iid-prepared interacting smooth law. Sigma^2 scaling therefore gives O(N^-1) and O(N^-1/2), uniformly for every beta>0. Root exclusion remains in H_i, and signed mean zero is not used. Isolated comparison AUD-005 passes; hostile constants review pending. TASK-014 now addresses the one-body martingale limit with explicit deterministic covariance convergence.

AUD-004 independently reconstructs every all-order shared-label bracket. Its centered formula (20)/(23) is equivalent to the R1 factorial/subset formula: p total shared edges, one distinguished Brownian edge, coefficient 2/(beta N^p), multiplicity p binomial(k,p) binomial(ell,p) p!, followed by every subset of the shared quotient slots integrated once against mu. It implies no positivity of individual centered terms and no critical summability.

Round 002 review update: AUD-006 now grants HOSTILE_REVIEW_PASS for the bounded residual estimates, fixed-data norm qualification and Gibbs law-class obstruction in the precise scopes above. The singular and other open interfaces are unchanged.

## Round 002 final integration

Round 002 final: THM-011 replaces the actual leading bracket by its deterministic mean-field counterpart in L1 with error O(N^-1/2); the positive-sign complex exponential has bounded modulus and proves factorization against every bounded initial-measurable variable. AUD-007 hostile PASS, AUD-008 statement-only comparison PASS with disclosed context reuse. All-order bracket inequalities use THM-014 symmetrized rooted identities; original unrestricted THM-012 identity is prohibited. At inverse temperature tending to infinity the leading noise covariance vanishes; at inverse temperature tending to zero both limiting covariance components vanish under iid normalization. No singular bracket passage or path tightness follows.

## Round 004 auxiliary martingale class

THM020's martingale is the conditional expectation of an integrable source occupation from each starting point. Smooth Ito is used only before finite annular exit; bounded stopped derivatives justify zero-mean stochastic integrals. Source integrability is proved before the limit. This establishes the bounded Borel inverse's true-martingale identity, not gradients or quadratic/cross variations of the full N-particle corrector. Those PO001 obligations remain OPEN.

The R5 probabilistic inverse has a true/UI source martingale along the auxiliary base-pair process. This does not give the corrector martingale along the interacting N-particle process. Its gradients, self/cross quadratic variations and passage to the exact particle identity remain PO022/023/PO001. The candidate fixed-N density estimate cannot make an unproved derivative integrable.

THM026 exact energy martingale has bracket2nu int|B_total|^2; bounded stopping precedes expectation,Fatou supplies global square occupation,then the unstopped martingale is square integrable and the exact global energy identity follows. No separate pair-force-square coercivity is asserted. The corrector martingale/bracket and particle Ito identity remain THM028/PO023 targets.

THM027's H1 bound is a spatial prerequisite only; its constants may grow rapidly with N. Inserting its gradient into the singular particle generator remains unjustified without PO023. THM028's full Ito and true corrector martingale are submitted under separate review. THM029/TASK055 targets a new uniform Haar noise-energy functional and exact two-/three-marginal identity. Reference-law averaging cannot be substituted for an expected bracket under the interacting law.

R8 actual corrector martingale M2=sqrt(2nu) sum_i integral grad_i P.dW_i is true square integrable, with bracket2nu integral sum_i |grad_i P|^2. The exact background gradient is retained. Collision localization passes by absolute expected drift integrability and L2 noise; all statements fixed N. No fluctuation-scale smallness follows. R9's reference energy/rates are pending fresh audit; actual self/cross transfer is PO024.

R9 reference functional sigma_N^2 integral Haar^N[2nu sum_i|grad_iP|^2]dt<=C b_N N^(-2/(s+2)). The leading functional is2nu b_N integral||grad f||2^2<=C, and the integrated absolute cross density is<=C sqrt(b_N)N^(-1/(s+2)). These retain physical2nu and pair-symmetry2 exactly. Actual leading expectation equals reference by one-body Haar; actual corrector self/cross smallness remains open pending the exact law error. A bound for the actual self-bracket would yield the actual absolute cross bound by Cauchy–Schwarz.

TASK062 final supplemental disposition: PASS_CONDITIONAL_EXTENSION, report AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK.md,209 lines,SHA25621ce79223857d09784121cf0b50b1d3befa30f9efd571f217cca2b2932277560. Root read the entire supplement, verified22 inputs,25 archive members and new output/outer seals, and rechecked all original hostile seals. No new diagnostic count is claimed. The precise additional corollary is sup_(t,N,nu)||partial_t Phi_t||1<=C_dot and nu||grad_pair Phi_t||2^2<=C_* N^(s/(s+2)) at every deterministic time, with corresponding timewise Haar self/absolute-cross rates. The original integrated theorem passes its two fresh-context gates; the additional corollary has a separate independent review in the reused hostile context after its original seal. It is not another fresh audit or certification of the whole blind report. No actual-law smallness, diagonal trace or uniform unweighted gradient follows.


R10 controls actual clipped and smoothed bracket functionals with the physical2nu N b_N unchanged. Radial clipping need not be a potential gradient; its predictable field defines the approximate martingale. Exact Hilbert-space triangle inequalities give original Q->0 iff the corresponding actual residual-tail Q->0. The smoothed trace exists and is retained; no trace is assigned to the unsmoothed gradient. These reductions have fresh hostile passes but pending whole-card blind. R12 genuine full-noise estimate C b_N N^(s/(s+2))(N^(-(1-s/d))+nu) has a conditional fresh Ultra reconstruction pass and pending hostile review, not a full-scope PO024 pass.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 accepted actual-noise gate: THM033 passes fresh AUD040 reconstruction and AUD041 hostile review. In the homogeneous strict sub-Coulomb bounded-chi family, Q_N<=C b_N N^(s/(s+2))(N^(-(1-s/d))+nu). Critical decay holds when s(s+2)<2d; bounded-chi decay also holds for s<min(2,d-2), and the exact other sufficient conditions remain in the card. The accepted R8 domain and R10 sharp floor separately supply the conditional premises. Outside these ranges PO024 is OPEN; within them PO001's actual integrated cubic/lower drift is the first open assertion. No fluctuation law or hierarchy closure follows.

R13 THM034 now passes fresh AUD045/046: Q_N=2nu Nb E integral sum_i|grad_i P_N[Phi]|^2 tends uniformly to zero over0<=nu<=nu_* for d>=4,0<s<2, with the exact five-term rate. The leading bracket is uniformly bounded and expected integral of absolute scaled cross-variation<=C sqrt(Q_N). Zero-noise bracket is identically zero. Entire actual bracket, not just smooth/clipped/reference component. PO024 is still open outside accepted R12/R13 union; drift remains separate.


Round014 final gate,2026-09-18 UTC. R14 verifies the existing full Ito coefficient identity and absence of extra mixed-particle thermal trace using R8. Its new estimate concerns lower drift only, neither a new bracket estimate nor cubic decay. Prior accepted R12/R13 actual-noise ranges remain exactly unchanged.


Round015 final gate,2026-09-18 UTC. R15 uses the exact actual R12 whole bracket Q<=C b N^a(N^-theta+nu), full four-term particle-gradient square and true R8 martingale. At criticality isometry gives sigma E|M_T^2|<=C N^((a-theta)/2). No signed component is independently discarded and no Haar-to-law transfer is presumed. Full first-order limiting noise/finite-dimensional law remains separately open THM039.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R17 conditional first-order actual martingale is sqrt(2nu)/N sum_i integral grad f(X_i)dW_i, bracket2nu/N integral eta|grad f|^2. Scaled cross bracket2nu b integral_0^min(ti,tj) eta[grad fi dot grad fj]. At finite positive criticality it vanishes as nu_N->0; pair-corrector noise estimates are nondependencies. THM040 must prove a generally nonzero deterministic thermal bracket limit and joint law, without finite-N independence.


R17 final gate,2026-09-18 UTC. R17 whole first-order thermal vector vanishes in L2 on critical tails using its exact physical bracket. Conditional source expectation gives the other L1 residual. Neither finite-N independence from initial data nor pair-corrector bracket inputs are used. Surviving thermal covariance remains the new THM040/041 gate.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 full comparisons check actual bracket concentration via smooth gradient products and true initial-sigma-field weighted exponential exp(iM+<M>/2). Zero covariance is not finite-N independence. Positive limiting noise retains thermal covariance; critical cooling removes it. Hostile gates pending.


R21 root synthesis,2026-09-18 UTC. New THM043/PO030 freezes actual integrated critical U3 decay throughout the entire strict R12 noise-decay range d>=3,0<s<d-2,s(s+2)<2d. Root TASK093 complete exposed working proof MEMORANDA/ROUND_021_CRITICAL_CUBIC_SYNTHESIS.md is UNSEALED/UNAUDITED. It composes accepted R5 initial endpoint, R8 actual domain/identity, R12 whole bracket, R14 both lower contractions and R16 source. The conditions imply s<d/2 and3s<2d-2; critical chi tends to0. Exact four-term bound is C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa], with p=s+2,a=s/p,theta=1-s/d and R14 midpoint q,kappa=(2q-s)/(2p)>0. No instantaneous absolute U3 claim. Root fresh diagnostic12531 assertions/18categories/4mutationfamilies passes but full source/exposure/seal packet and both independent gates remain outstanding. TASK094/AUD061 reserved fresh R21blind andTASK095/AUD062 reserved separate hostile, not yet written. Next freeTASK096,AUD063,THM044,PO031. R20 TASK091/AUD059 prepared blind retains next available worker priority; TASK092/AUD060 reserved R20hostile. No earlier card changed or independent status assigned.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.

R20/R21 subsequent status at R18/R19 acceptance: R20 constructor sealed; independent blind and hostile active. R21 root source/exposure/diagnostic packet is now sealed SELF_CHECKED (29 inputs,38 archive members); fresh TASK094/AUD061 whole reconstruction active, TASK095/AUD062 hostile still reserved. Earlier unsealed entries above are chronological history. Neither new theorem is promoted. Current exact pointers/hashes are STATE/CAMPAIGN_STATE.md.
