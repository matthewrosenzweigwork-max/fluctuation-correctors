# Decision log

## DEC-001 — regime terminology

- Date: 17 September 2026
- Decision: distinguish the old condition \(\beta_NN^{2s/d-1}\to0\), full subcriticality \(\lambda_N\to0\), and criticality \(\lambda_N\to\lambda\in(0,\infty)\).
- Reason: prevent the central scaling objective from being misstated.
- Status: frozen baseline.

## DEC-002 — critical closure is not presumed finite

- Date: 17 September 2026
- Decision: require a power-counting theorem before truncating the corrector hierarchy at critical coupling.
- Reason: all corrector orders may survive when \(\lambda_N\) has a nonzero limit.
- Status: frozen baseline.

## DEC-003 — model allocation

- Date: 17 September 2026
- Decision: Astra Ultra coordinates and synthesizes; Astra Max performs most bounded workstreams; independent audit requires isolated context.
- Status: frozen baseline.

## DEC-004 — verified installation and literal baseline provenance

- Date/version: 2026-09-17, operational v1.1.
- Clean unborn repository; zero collisions. All imported overlay files were frozen byte-for-byte at 475a5399828bc6e2ccbade08c59b8778638df14a. No pre-existing mathematical work or instructions needed reconciliation.
- The literal hash was recorded immediately in .git/HOCF_INSTALLATION_BASELINE.json without tracked-tree mutation. Round 001 records cite it as historical provenance. No self-reference, amendment, second baseline commit or push.
- Ten imported Markdown hard-break whitespace warnings were retained and disclosed in the installation report.

## DEC-005 — mutable checksum lifecycle

- Date/version: 2026-09-17, operational v1.1; scientific specification unchanged.
- Issue: shipped SHA256SUMS.txt covers mutable STATE, APPROACHES and task queue files, while Protocol 4 requires their continual updates. Shipped verifier has no mutable-state mode.
- Decision: preserve the original manifest both in the immutable baseline commit and REPORTS/INSTALLATION/OVERLAY_SHA256SUMS_BASELINE.txt. Refresh only declared mutable entries in the working manifest after explicit state updates. Keep scripts/verify_campaign.py unchanged. Independently verify every nonmutable original path against the frozen baseline manifest. New artifacts receive a separate checkpoint manifest.
- Mutable scope: STATE except STATUS_VOCABULARY.md; APPROACHES; TASKS/QUEUE.md. Nothing under INPUTS, BASELINE, root authority documents, templates, or shipped scripts may be rehashed to conceal a change.
- Downstream: working SHA256SUMS.txt, state/route/queue updates, installation evidence, checkpoint manifest. Original text and all hashes preserved by baseline.
- Basis: Protocols 1, 2, 4 and 24; independently reviewed by Astra Max installation_audit. This is an operational reconciliation, not a weakened scientific gate.

## DEC-006 — Round 001 scope and sequencing

- Date/version: 2026-09-17, operational v1.1.
- Freeze TASKS/ACTIVE/ROUND_001_MODEL.md. The owner-requested read order takes precedence over the slightly different README order; all listed files were read before mathematical work.
- The master/kickoff requirement to issue ROUND_001.md only after a mathematical gate changes takes precedence over Protocol 1's instruction to start the report at boot. Task cards hold initial assertions meanwhile.
- Four available total agent slots require batches of three Max workers, not eight simultaneous workers. Each writable lane has its own worktree and root alone integrates.
- Full campaign remains unresolved; the current invocation installs/freezes and executes the initial round. No singular local-equilibrium closure begins before exact smooth hierarchy and power-counting gates.
- Current direct instruction authorizes one baseline commit. Round outputs remain reviewable working-tree changes unless further commit authorization is supplied; no automatic extra commit.

## DEC-007 — source identifier collision and bounded source authority

- Date: 2026-09-17. The imported INPUTS manifest calls the provisional baseline assessment SRC-002, while STATE/SOURCE_LEDGER.md already uses SRC-002 for Rosenzweig–Serfaty commutators. Preserve both frozen originals; use full path for the assessment and the state-ledger namespace for new literature records. No input is silently merged or promoted.
- The source-note Fact/Hope/Missing ingredient/Obstruction labels remain source labels. The package's source intake is not a proof certificate.

## DEC-008 — bounded analytic and algebraic status are distinct

- Date/version: 2026-09-17, scientific work under frozen v1.0 model; operational v1.1 unchanged.
- THM-008 remains the frozen pair algebra statement. The smooth worker initially referred to that identifier as its candidate context; root assigns its distinct analytic statement THM-009, preserving the worker report verbatim. Theorem cards and ledgers make the distinction explicit.
- The complete smooth all-order recursion is THM-001. It does not close M2, which also requires proved critical power counting. Finite exact arithmetic batteries are supporting computation, not independent universal proof certificates.
- The next bounded assertion is TASKS/ACTIVE/PO-001_RESIDUAL.md: a fixed-smooth iid residual/endpoint/bracket estimate with explicit high-regularity bounds. The singular mission, other preparations and critical survival alternatives remain separate open obligations. This first test does not silently narrow the flagship.
- No workflow is left running as an implied background promise at the final handoff. Completed reports are integrated; open work is recorded as open.

## DEC-009 — publication and continued campaign authorized

- Date: 2026-09-17. The owner explicitly requested committing and pushing research outputs, increasing allocation to ten concurrent workers, and resuming through the gates. This supersedes the earlier no-further-commit/no-push instruction for this campaign work; it does not authorize history rewriting, unrelated edits, dependency installation, or remote configuration changes.
- Round 001 research checkpoint committed as a06178658d1e3d458536ff312ca793947212ec67 and pushed to the existing origin/main. Local HEAD, origin/main and live remote main were independently read and equal. Staged diff had only preserved evidence-format warnings: four BBGKY Markdown hard breaks and one final blank line in the verbatim TeX build log. No evidence normalization performed.
- All Round 001 reports/manifests remain historical snapshots of that checkpoint. Current state and NEXT_INVOCATION will advance; future verification of old mutable-state hashes must use the historical commit/archive rather than overwrite the old manifest.

## DEC-010 — requested and runtime worker capacities differ

- Created project-local .codex/config.toml with [agents], enabled=true, max_concurrent_threads_per_session=10, excluding the root. This exact key is documented and accepted by installed Codex; no global config changed. No prior live project config existed, so no replacement/backup was needed.
- The running collaboration contract still advertises four total agents (root plus three workers). A further fresh worker spawn was actually rejected with agent thread limit reached. The configured desired cap is ten; actual activation at ten is not verified. No workaround processes/threads or claims of ten live workers.
- Continue useful scientific work within the present limit, reusing operational-only context for proof-blind reconstruction with that provenance disclosed. A reinitialized client/session may be needed; official sources do not establish hot-reload semantics, so no restart guarantee is made.
- Evidence: official https://learn.chatgpt.com/docs/agent-configuration/subagents and https://learn.chatgpt.com/docs/config-file/config-reference; installed CLI accepted numeric key and rejected a string at that key. Config parser succeeded again after file creation. Worker /root/capacity performed read-only investigation.

## DEC-011 — bounded Round 002 promotions and immutable rendering erratum

- AUD-004 completes isolated all-order smooth algebra reconstruction; M2 remains OPEN because critical power counting is separate.
- THM-010 fixed-smooth iid residual has complete independent constructions, AUD-005 isolated comparison, and AUD-006 hostile pass for explicit constants. The precise bounded task is closed; singular PO-001 is not. Root (D1)-(D3) fixed-data qualification and OBS-009 attractive-Gibbs obstruction also pass hostile review, with no additional blind audit implied.
- AUD-006 found a literal form-feed in one fraction command in the sealed falsification report. Preserve its original hash and use AUDITS/ROUND_002_FALSIFICATION_RENDERING_ERRATUM.md for the readable coefficient. This is a rendering repair, not a mathematical retraction or changed theorem.
- THM-011 is a new bounded Gaussian covariance criterion in independent hostile review. Its covariance-convergence assumptions and field/singular exclusions are explicit. TASK-016 separately investigates finite/zero diffusivity identification; no frozen target is silently broadened or narrowed.

## DEC-012 — preserve and repair the power-counting symmetry defect

2026-09-17. The independent reviewer disproved the unrestricted compact first-slot identity in unpromoted THM-012. Preserve submitted report/card/audit; record RET-001 and OBS-010; issue new THM-014 with explicit averaged symmetrization, which preserves the statistic and contracts the displayed norms. Obtain a separately sealed repair verdict. No scope change to the mission or previously audited symmetric corrector class.

## DEC-013 — audit-context capacity and precise gate status

2026-09-17. The initialized tool runtime cannot create an additional fresh worker despite the accepted ten-worker project setting. Reuse existing workers only for new claims they did not construct, with a new isolated worktree/dossier and explicit context history. A statement-only reconstruction of a new claim is recorded as such, and hostile reviews identify prior related work. This operational choice does not waive or claim satisfaction of the stricter fresh-agent/session publication gate. Broad M2/M3 and singular gates remain open. Do not call reused roles independent reviews of their own prior constructions.

## DEC-014 — continue at the singular initial pair interface

2026-09-17. Start R3 construction and independent falsification after their R2 outputs are sealed, while root finalizes the atomic R2 checkpoint. Their separate worktrees use published a061786 and statement/model inputs only. Bound the task to iid initial L2/probability pair statistics, heat-cutoff orders and collision errors. Do not equate a bare Riesz kernel with the actual backward corrector or extend initial estimates to interacting positive time.

## DEC-015 — sharp initial-law statements and full-operator separation

2026-09-17. Preserve THM-015/016 frozen submitted bytes and issue distinct cards for the stronger L1 upper bound (THM-018), root sharp lower-probability/converse (THM-019), and exact internal-transport model (THM-017). Infinite variance cannot establish probability nonconvergence; the new lower bound uses a positive-probability close-pair event and a controlled centered outer field. A raw-potential threshold is not assigned to the actual backward corrector. Root's construction goes to a separate hostile reviewer and a statement-only reconstructor before promotion. Model proposal participation is disclosed for the toy proof; root does not certify it.

R2 publication is 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2, checked equal to local/tracking/live remote main. The literal receipt is carried into R3. The ten-worker project setting remains unchanged, while the initialized three-worker capacity continues to limit fresh-session certification. All issued proof/audit artifacts stay byte-identical; mathematical clarifications belong in separate reviews and canonical state.

## DEC-016 — fresh contexts can be allocated after completed workers

2026-09-17T2045Z. After TASK026 completed, collaboration.list_agents showed only two running workers and one completed worker. A new fork_turns=none gpt-6-astra/max worker /root/r003_fresh_sharp was then accepted. Thus the earlier rejected spawn established the three-concurrent-worker limit while occupied, not a permanent inability to create fresh contexts. Fresh independent contexts are available by sequential allocation. Preserve earlier reports' truthful reuse histories, but supersede any inference that strict fresh review is permanently blocked. The requested ten-concurrent cap is still not active in this initialized runtime. Root has assigned a fresh statement-only THM019 reconstruction in a new isolated worktree, with its permitted prerequisites explicit.

## DEC-017 — fresh R3 proof gates and continued diffusion work

2026-09-17. Fresh TASK029 and TASK030 establish a separately staffed reconstruction/hostile pass for THM019, with the statement's method hints disclosed. TASK030 also passes THM017/018 and identifies the root rescaling scope error FH-D01, preserved and corrected by erratum. No original reused audit is relabeled fresh. After TASK029 sealed, its Max worker moved to an isolated R4 constructor worktree with a hashed new dossier. A different fork_turns=none Max worker independently reconstructs the same bounded diffusion assertion from the root's explicitly unproved seed. R3 publication and R4 construction remain separate, and root alone writes canonical state.

## DEC-018 — local diffusion and periodic continuation

2026-09-17. Preserve THM020's precise probabilistic class and all-N endpoint as a separate bounded theorem; no classical regularity label is inferred. Independent TASK033 adds an explicitly sealed all-N extension before any new-task exposure. After that seal its worker starts TASK036 in a new periodic-pair worktree with prescribed C1 background/C2 test and bounded nu interval. TASK034 separately constructs the singular response measure/L2 module. Root alone integrates, with fresh hostile review before promotion. R3 is published as 52bda5d0d24067b051c6fe9763f2a78e7599e593 with local/tracking/live remote equality.

## DEC-019 — root small-time coefficient correction before audit

Root's separately sealed proposed range obstruction omitted one factor s in both displays of its third time derivative bound. Self-check caught it before external review or promotion. Preserve original ROUND_004_SUPERHARMONIC_RANGE_OBSTRUCTION.md and its hash; use separate V2 with 4s^4(2s+2)/N^2 in the third derivative bound. The annular lower expansion and strict s>d-2 range are unchanged. Neither version has an independent verdict at this entry; V2 alone is submitted for later audit. This is not retraction of a promoted theorem.

## DEC-020 — preserve fresh response and range audit boundaries

2026-09-17. Fresh AUD023 hostile and AUD024 statement-only comparison pass THM021 without mathematical repair. Preserve issued files, separately record the harmless differential-spacing typo and distinct execution-history evidence. Fresh AUD022 passes the V2 local range obstruction, while rejecting literal equivalence with a logical negation; separate wording erratum states the stronger implication and explicit annulus. Its THM020 source-exposure limit remains part of the report even though root verified the cross-reference. Dispatch fresh TASK042 for the still-missing range reconstruction; no fresh mode is inferred from full-proof hostile algebra.

## DEC-021 — direct full-pair initial estimate as the next bounded gate

2026-09-17. Freeze THM023 periodic-base and THM024 abstract-composition submissions after their complete proofs are sealed. Fresh TASK040 receives only statements and sealed R4 local prerequisites; fresh TASK041 receives candidate proofs. Separate isolated worktrees on R3, Astra Max, no shared narrative before reconstruction. Uniform prescribed data and bounded diffusivity remain explicit hypotheses; proving this direct norm implication would advance the initial endpoint without requiring closeness to a particular diagnostic. It would not discharge actual-data regularity, finite-particle Ito/domain, evolved-law residuals or critical hierarchy. No mission amendment or normalization change.

## DEC-022 — explicit R5 source repair and direct endpoint promotion

2026-09-17. Preserve TASK044's original REPAIR_REQUIRED report, candidate and both original seals. Add a separate exact reference to the coefficient-one smooth local remainder proved in the already sealed R4 response memorandum and independently reconstructed/audited there. Choose kappa=max(kappa21,C0_23) to justify the singular growth constant without identifying source-local constants. Supplemental TASK047 reads/checks the new source generation after the original hostile seal, discharges D1/D2 and passes only the candidate-plus-addendum. This is accurately reused-context source checking, not independent certification of its own reviewer-added bridge. Root read the supplement and reran its27 exact comparisons; historical chronology/manifests were outside that worker's supplement, although preserved and checked by root in earlier R4 integration. The theorem and all scientific scopes remain unchanged.

THM025's direct norm bound meets the initial-endpoint objective without proving closeness to a chosen diagnostic; retain PO017's literal comparison as unproved rather than silently changing it. The actual homogeneous Fourier data are a proved subcase, not a replacement mission. Next gates are finite-N particle realization, weighted first derivatives and the full corrector Ito domain. Frozen THM026/027 cards predate their respective constructor outputs. After TASK045 sealed, its constructor moved to a new R7 worktree; no audit context is relabeled fresh. Fresh TASK046/048 and TASK050 have separate restricted dossiers.

## DEC-023 — audited finite-N particle gate and explicit domain continuation

2026-09-18. THM026 passes fresh AUD030 hostile without repair and AUD031 reconstruction comparison. Preserve original status-at-submission cards/proofs and both independent shifts/stopping constructions. The fixed-N density bound is not used as an N-uniform law estimate. The worker sealed its checker result read-only; preserve that evidence and reproduce the identical checker in a new writable directory rather than changing its modes or contents. R5 publication32d17afba1ddb3c4198fb9a45e912907629618ce was independently matched to local/tracking/live remote. R6 now freezes the particle gate. New THM028/TASK051 attempts the homogeneous full corrector domain while THM027 gradient construction and fresh reconstruction run; its root seed and conditional prerequisite limits are explicit. No root construction is self-certified, no mission/regime changes.
