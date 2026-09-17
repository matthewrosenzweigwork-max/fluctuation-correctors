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
