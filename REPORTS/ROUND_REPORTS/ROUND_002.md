# Round 002 — smooth iid residuals, Gaussian limits and explicit cutoff boundary

2026-09-17 UTC. Input checkpoint a06178658d1e3d458536ff312ca793947212ec67, published at the owner's explicit request. The output checkpoint is the atomic commit containing this report; its exact local/tracking/live-remote hashes are recorded after publication under .git/campaign-records and in the next tracked checkpoint. No self-referential commit hash is inserted into its own tree.

The primary frozen assertion and exact negation are TASKS/ACTIVE/PO-001_RESIDUAL.md: in the fixed-smooth iid model with the displayed uniform norms, every positive temperature sequence has vanishing scaled pair endpoint, integrated absolute cubic residual, pair bracket and cross bracket. The negation is an admissible sequence with positive limsup for one of those targets. Two independent proofs establish the assertion; separate hostile review accepts the explicit constants. The singular extension remains open.

## Executed routes and mathematical dispositions

| Claim | Result | Audit and precise limit |
|---|---|---|
| THM-001 all-order algebra | General drift and every bracket matching independently reconstructed, with the same coefficients after convention mapping | AUD-004; prior hostile pass retained. No effective singular power counting inferred |
| THM-010 smooth iid residual | Actual-law negative-Sobolev/Fourier moments, all deleted-label terms and uniform positive-temperature residual rates | AUD-005 isolated comparison and AUD-006 hostile pass; fixed smooth data only |
| Root smooth-data qualification | Explicit density, full one-body and pair bounds uniform in N and diffusivity in the existing smooth class | AUD-006 hostile pass; no separately staffed blind proof and no cutoff uniformity |
| THM-011 Gaussian criterion | Finite-list centered Gaussian limit with covariance I+D whenever its explicit matrices converge; initial/noise asymptotic independence; O(N^-1) mean-field bias | AUD-007 hostile pass and AUD-008 statement-only comparison; reused prerequisite context disclosed, not a fresh-session publication gate |
| THM-013 diffusivity continuity | Constructed inviscid reference and full backward response; explicit parameter-Lipschitz constants with two extra derivatives; identified covariance for finite positive/infinite inverse temperature | AUD-010 hostile pass; positive-diffusivity mean-field existence is assumed, no blind audit claimed |
| THM-012 original power-count submission | Quantitative estimates pass, but unrestricted first-slot gradient identity is false without symmetry | AUD-009 mixed verdict; original report/card preserved, unrestricted identity prohibited |
| THM-014 repaired all-order theorem | Symmetrization repairs the exact identity without enlarging any displayed norm constant; explicit partition, root, series and heat-cutoff bounds retained | Separate AUD-009 repair disposition; no actual hierarchy-growth or singular-model comparison theorem |

The constructor's empirical-moment proof uses synchronous coupling to independent nonlinear particles, with the same Brownian motions; it never assumes iid law for evolved interacting particles. The independent residual route uses conditional moments and absolute Fourier sums. They are distinct executions of related coupling mechanisms, not an independent BBGKY correlation closure. Root did not upgrade its own checking to independent certification.

For q=floor(d/2)+2, the actual empirical negative-Sobolev p-moment is O(N^-1/2), with explicit constants. Pair deletion retains the empirical diagonal; cubic deletion retains all double and triple contractions. Endpoint and integrated cubic raw sizes are O(N^-1) and O(N^-3/2). Pair and leading/pair cross brackets are O(beta^-1 N^-2) and O(beta^-1 N^-3/2). With sigma=min(sqrt(N beta),sqrt N), their scaled sizes are respectively O(N^-1/2), O(N^-1), O(N^-1), O(N^-1/2). Lower drifts are O(N^-1). These estimates are absolute or in the explicitly stated Lp modes, not signed-mean concentration claims.

The Gaussian proof retains the full response operator. Its leading bracket is replaced in L1 under the actual law, and a bounded complex exponential martingale proves factorization against every bounded initial-measurable variable. The independent Gaussian reconstruction uses the zero-diagonal quadratic one-body source directly and proves an L1 remainder. The constructor's stronger L2 corrected remainder is independently hostile-reviewed, not reconstructed by that shorter proof. Both initial and dynamic covariances retain the temperature factors min(beta,1) and min(1,beta^-1), the noise factor two, and the unequal-time overlap interval.

THM-013 identifies these covariances using a self-contained characteristic fixed point, smooth positive pushforward, response Volterra series and differentiated comparison equations. Both the changing transport velocity and changing response density occur in the backward difference. No inverse diffusivity is used. Inverse temperature tending to infinity yields the initial covariance of the full inviscid backward tests and zero dynamic covariance. Inverse temperature tending to zero gives a zero limit under the iid normalization. Finite positive limits use the corresponding full reference/backward kernels. Oscillating temperatures can produce different subsequential laws; an explicit free example does so.

## All-order and singular-interface boundary

The exact partition formula has signed cycle weights and is valid also for k>N and coincident positions of distinct labels. A block of size r>=2 contributes N^(-(r-2)/2) beyond the common N^(-k/2) scale: a pair block has no extra gain. Root omission and its mass deficit remain explicit. The k-to-k-2 drift row stays at the same N^(-k/2) order, not a new decay power. Finite partition constants, derivative counts and every bracket factor are displayed in the power-count memorandum.

The sufficient infinite-series/tail criteria require the actual coefficient and kernel norm sequences. A concrete model lemma assumes geometric kernel growth and coefficients 1/k!; neither is asserted for the real corrector hierarchy. The positive-power heat cutoff has explicit derivative upper bounds and a Lipschitz lower divergence. The particular coupling constant grows exponentially in epsilon^(-(s+2)/2) at positive horizon. For fixed orders, epsilon_N^(-(s+2)/2)+log(1+A_Phi(N)+A_f(N))=o(log N) suffices for its own regularized-model residuals. A sufficiently slow diagonal cutoff exists under uniform fixed-cutoff norm envelopes. No comparison to a singular particle/reference pair follows.

Thus M0/M1 remain passed in the smooth model, while M2 remains OPEN at actual critical singular power counting and hierarchy survival/summability. M3 has a complete bounded iid finite-list subclaim, but its full scope and strict fresh-session gate are not claimed. THM-003/004 remain OPEN. No field/path tightness is proved.

## Falsifications, repair and evidence preservation

OBS-009 is a complete attractive smooth Gibbs example: despite uniform one-point marginals, the pair Fourier statistic tends to one at diverging inverse temperature. It disproves an unqualified iid-to-Gibbs transfer, not a positive-Riesz theorem. AUD-006 passes its proof.

OBS-010 uses Phi(x,y)=h(y): U_2=-eta(h)/N, whose particle gradient is nonzero while its first-slot kernel derivative vanishes. The original unrestricted identity in THM-012 therefore fails. RET-001 records this unpromoted candidate defect. THM-014 explicitly uses averaged symmetrization; it preserves U_k and contracts C^m norms. Every original proof/audit byte is retained. The defect does not affect prior symmetric corrector, residual or Gaussian results. No previously promoted theorem is retracted.

The sealed independent residual report contains one form-feed byte in the rendering of equation (2.5). Its SHA-256 remains unchanged. AUDITS/ROUND_002_FALSIFICATION_RENDERING_ERRATUM.md supplies the correct displayed formulas; AUD-006 records mathematical PASS and a rendering-only defect. No verified evidence is silently normalized to make formatting checks pass.

## Sources, computation and allocation

No new external quantitative theorem is imported. Smooth identities, elementary iid moment expansions, exact finite sums, Fourier duality, maximum-norm estimates and directly justified characteristic functions are the inputs. Existing source normalization quarantine remains unchanged, private [N] remains absent and unused, and no novelty assertion is made. The old condition beta_N N^(2s/d-1)->0, full-subcritical lambda_N=beta_N N^(s/d-1)->0, and critical lambda_N->positive finite remain distinct; logarithmic normalization remains separate.

CERTIFICATES/ROUND_002_VERIFICATION.md records exact commands, counts, environment, output files and limits. Independent rational batteries test moments, deletions, rooted gradients, contractions, free heat, unequal times, temperature factors, degenerate limits and the symmetry counterexample. They support the full analytic proofs and do not replace them. TeX compiles cleanly; every page of the final seven-page PDF was visually inspected. Protected baseline and frozen audit hashes are checked independently of mutable state.

Actual allocation is root gpt-6-astra ultra and three gpt-6-astra max worker contexts, with separate worktrees for new mathematical routes. The project setting requests up to ten spawned workers, excluding root. The active runtime still limits the session to four total slots and actually rejected an additional spawn. No hot reload, ten active workers or fresh context beyond that capacity is claimed. Exact reuse/isolation histories appear in each audit. Publication of a research checkpoint does not label every candidate a fully certified theorem or satisfy the separate manuscript-release gate.

## Next executable work

Round 003 starts with TASK-021 and TASK-022 in separate worktrees: prove/reconstruct the exact initial iid pair projection formula, establish heat-cutoff L2 orders, and test the close-pair probability/mean/truncated-variance terms. The purpose is to distinguish valid initial-law estimates from an unjustified singular passage. The bare Riesz potential must not be substituted for the actual backward corrector.

The first open load-bearing assertion is fluctuation-scale singular/regularized model comparison with justified well-posedness and a cutoff compatible with the corrector estimates. Its initial-law interface is now a bounded executable task. Next: compare the two sealed R3 proofs, obtain a separate hostile verdict, then attack the actual backward singular kernel and positive-time comparison. No broad plan-only round is needed.

Files inspected/created and exact changed paths are recorded in the R2 inventory and manifest. Recovery begins at REPORTS/CHECKPOINTS/NEXT_INVOCATION.md. R1 versioned reports remain historical; their original no-push statements are superseded operationally by the owner's latest authorization and DEC-009.
