# CAMPAIGN PROTOCOLS

## HOCF-RIESZ — higher-order correctors to Coulomb/Riesz fluctuations

These protocols govern autonomous execution of `MASTER_PROMPT.md`. They are operational rules, not mathematical assumptions.

---

## Protocol 1. Boot sequence and baseline preservation

1. Read files in the order specified by `README_FIRST.md`.
2. Run `python3 scripts/verify_campaign.py`; investigate every failure.
3. Record operating system, Codex version, model selection, Python, TeX, symbolic packages, and Git state in `STATE/ENVIRONMENT.md`.
4. Preserve `INPUTS/` and `BASELINE/` unchanged. If a source requires annotation, create a versioned note under `SOURCES/`.
5. Record the imported note’s SHA-256 before mathematical use.
6. If the repository contains pre-existing work, reconcile authority and notation before merging.
7. Create or verify an atomic frozen-baseline commit only when authorized.
8. Start `REPORTS/ROUND_REPORTS/ROUND_001.md` and record the repository hash.

---

## Protocol 2. Authority and amendments

Authority order is given in `README_FIRST.md`.

A campaign amendment must:

- identify the exact rule or target changed;
- state why the old version is insufficient;
- list downstream files and claims affected;
- receive a new version/date;
- preserve the superseded text;
- be recorded in `STATE/DECISION_LOG.md`.

Do not silently modify a frozen theorem target to match a proof.

---

## Protocol 3. Status vocabulary

Use the multi-axis vocabulary in `STATE/STATUS_VOCABULARY.md`.

Every substantive claim has three independent fields:

1. mathematical status;
2. audit status;
3. source status.

Optional fields include computation status and manuscript status. Never compress these to “done,” “verified,” or “promising.”

---

## Protocol 4. Durable campaign state

Maintain:

- `STATE/CAMPAIGN_STATE.md`;
- `STATE/THEOREM_LEDGER.md`;
- `STATE/PROOF_OBLIGATION_LEDGER.md`;
- `STATE/NORMALIZATION_AND_SCALING_LEDGER.md`;
- `STATE/CORRECTOR_LEDGER.md`;
- `STATE/COUNTERTERM_AND_CONTRACTION_LEDGER.md`;
- `STATE/ASSUMPTIONS_AND_CONSTANTS_LEDGER.md`;
- `STATE/BIAS_AND_CENTERING_LEDGER.md`;
- `STATE/OPERATOR_AND_SEMIGROUP_LEDGER.md`;
- `STATE/DIAGRAM_AND_POWER_COUNTING_LEDGER.md`;
- `STATE/MARTINGALE_AND_QUADRATIC_VARIATION_LEDGER.md`;
- `STATE/STATIC_DYNAMIC_INTERFACE_LEDGER.md`;
- `STATE/REGULARIZATION_LEDGER.md`;
- `STATE/LAW_CLASS_AND_GEOMETRY_LEDGER.md`;
- `STATE/SOURCE_LEDGER.md`;
- `STATE/COMPUTATION_LEDGER.md`;
- `STATE/DECISION_LOG.md`;
- `STATE/RETRACTION_LEDGER.md`;
- `APPROACHES/ROUTE_REGISTRY.md`;
- `APPROACHES/OBSTRUCTION_LEDGER.md`.

`CAMPAIGN_STATE.md` must fit on a few screens and state:

- current phase and gate;
- flagship theorem candidate and exact status;
- strongest proved positive statement;
- strongest proved negative statement;
- first open load-bearing assertion;
- active routes and owners;
- current singularity and temperature ranges;
- centering and law class;
- regularization status;
- source-audit status;
- audit status;
- next three executable actions;
- canonical memorandum path;
- last verified commit and package hash.

No claim is durable until it appears in a ledger with a proof location or exact source citation.

---

## Protocol 5. Round structure

A substantive round must:

1. freeze one primary assertion and its exact negation;
2. identify all dependencies and nondependencies;
3. run a source preflight;
4. run a proof sprint;
5. run a falsification sprint isolated from the proof narrative when possible;
6. test at least one solvable or limiting model;
7. audit powers of \(N\), \(\beta_N\), \(\lambda_N\), \(\sigma_N\), and every combinatorial coefficient;
8. test diagonal, Itô, and martingale terms;
9. run a hostile review;
10. decide: promote, repair, demote, disprove, retract, or exact reduction;
11. update all ledgers and the round report;
12. make an atomic commit when authorized.

If no theorem is proved or disproved, the round must still produce one of:

- a strictly smaller first open lemma;
- a coefficient barrier;
- a source theorem ruled in or out;
- a counterexample;
- an exact reduction to a static/dynamic interface;
- a certified computation;
- a route demotion.

---

## Protocol 6. Task cards

Every active task must contain:

- stable identifier;
- exact question;
- exact negation when applicable;
- model, geometry, kernel, dynamics, law class, centering, and temperature regime;
- permitted inputs;
- forbidden shortcuts;
- required output files;
- acceptance tests;
- falsification tests;
- status on failure;
- dependencies and nondependencies;
- owner model/agent/worktree;
- expected merge gate.

Do not assign “investigate X” as a task.

---

## Protocol 7. Model and worktree allocation

Follow `MODEL_ORCHESTRATION.md`.

- Use Astra Ultra for campaign direction, hard synthesis, critical scaling decisions, and promotion-gate review.
- Use Astra Max for the default proof, source, counterexample, computation, and writing workstreams.
- Prefer four to eight genuinely distinct active lanes over many redundant agents.
- Parallelize read-heavy and independent mathematical work.
- Avoid concurrent edits to canonical ledgers and cumulative memoranda.
- Use one branch/worktree per route and a single integration owner.
- Record exact prompts and input dossiers for audit work.

---

## Protocol 8. Exact finite-\(N\) algebra

For every generator identity:

1. begin from explicit sums over distinct indices;
2. state ordered versus unordered tuple conventions;
3. record falling factorials and normalization;
4. separate particle-particle, particle-background, and background-background terms;
5. display each diagonal deletion or contraction;
6. include Itô traces and martingales;
7. compute quadratic and cross variations;
8. symmetrize only after coefficients are visible;
9. test \(N=2,3\) directly;
10. compare the U-statistic, empirical-measure, and cumulant forms.

A formal empirical-measure derivation cannot be the sole proof of a load-bearing coefficient.

---

## Protocol 9. Corrector hierarchy

Every corrector receives a `COR-###` card recording:

- order \(k\);
- source term canceled;
- backward/final-value equation;
- exact operator;
- symmetry and mean-zero constraints;
- diagonal behavior;
- regularity and singularity class;
- deterministic counterterm;
- martingale contribution;
- scaling in \(N,\beta_N,\lambda_N,\sigma_N\);
- interaction with adjacent hierarchy levels;
- proof status and audit status.

At critical scaling, maintain a truncation-error table uniform in the corrector order. If no order gain exists, immediately open a resummation task.

---

## Protocol 10. Counterterms and renormalization

For each counterterm:

1. derive it from an exact finite-\(N\) contraction or a controlled regularization limit;
2. state whether it is scalar, spatially dependent, test-dependent, density-dependent, or random;
3. distinguish diagonal/Wick, free-energy/pressure, and dynamic Itô counterterms;
4. prove compatibility with the selected centering;
5. prove regularization-scheme independence or state the scheme as part of the theorem;
6. record it in `COUNTERTERM_AND_CONTRACTION_LEDGER.md`;
7. verify signs and coefficients in at least two representations.

Never introduce an “infinite constant” without a finite-\(N\) origin and a cancellation statement.

---

## Protocol 11. Scaling and regime audit

For each claimed error \(R_N\), record:

- its raw size;
- its size after multiplying by \(\sigma_N\);
- its dependence on \(\lambda_N\);
- the worst admissible subcritical sequence \(\lambda_N\downarrow0\);
- its critical limit at fixed \(\lambda\);
- uniformity in time, test function, regularization, and background;
- whether it is deterministic, in expectation, in probability, in \(L^p\), or pathwise.

A little-\(o\) statement with no uniformity or rate cannot be used to enlarge a temperature range.

Every theorem proof must include a final scaling table showing exactly which term closes in each regime.

---

## Protocol 12. Centering audit

Before stating convergence, compute:

1. \(\mathbb E\mu_N^t-\mu^t\) at the required scale;
2. each deterministic pressure/free-energy correction;
3. each diagonal/Wick counterterm;
4. the difference between exact first-marginal and proposed explicit centering;
5. any initial preparation bias;
6. the centering error after multiplication by \(\sigma_N\).

Exact-centered results and explicit-centered results receive separate theorem identifiers.

---

## Protocol 13. Singular regularization

Every singular proof must use a named regularization parameter and maintain a regularization ledger.

Required checks:

- regularized generator identity;
- bounds uniform in \(N,\beta_N\), and regularization on the claimed regime;
- partial-diagonal analysis for every hierarchy order;
- order of the \(N\to\infty\) and cutoff-removal limits;
- tightness/uniform integrability needed to pass martingales and quadratic variations;
- independence or dependence on regularization scheme;
- Coulomb/log distributional terms;
- torus smooth remainder and coordinate issues.

Do not write “by approximation” without a complete passage.

---

## Protocol 14. Static input qualification

A static theorem may enter the dynamic proof only after `STATE/SOURCE_LEDGER.md` records:

- exact citation/version;
- theorem/lemma number;
- model normalization;
- geometry and boundary conditions;
- inverse-temperature convention;
- background regularity;
- law class;
- constant dependence;
- whether the needed uniformity is stated or must be proved;
- mapping into campaign notation.

If the input is model-generated or unpublished, treat it as an open proof obligation unless supplied as a frozen, independently audited package.

---

## Protocol 15. Solvable-model battery

Before promoting a general identity or estimate, test as applicable:

- smooth bounded interaction;
- Fourier-truncated Riesz kernel;
- homogeneous torus background;
- one Fourier mode;
- affine velocity field;
- stationary equilibrium;
- iid initial law;
- \(N=2\) and \(N=3\);
- one-dimensional ordered particles;
- \(s<d/2\), \(s=d/2\), and \(s>d/2\);
- \(\lambda_N\to0\), \(\lambda_N\to\lambda\), and \(\lambda_N\to\infty\);
- gradient and conservative matrices when the statement claims both.

A failed test immediately demotes the claim and opens a retraction/repair record.

---

## Protocol 16. Computation

Every computation must include:

- source code;
- exact command;
- environment and package versions;
- input or generation procedure;
- random seed if applicable;
- expected output;
- tolerance;
- interpretation and limitations;
- independent verifier when it supports a proof gate.

Use only these computation statuses:

- `EXPLORATORY`;
- `REPRODUCED`;
- `RIGOROUSLY_ENCLOSED`;
- `CERTIFICATE_VERIFIED`.

A plot or floating-point agreement is not a proof.

Appropriate uses include:

- index/combinatorial checks for \(k=2,3,4\);
- Fourier coefficient and trace calculations;
- divergent-diagram detection;
- symbolic Itô contraction checks;
- exact finite-\(N\) tests;
- interval bounds for a finite operator or radius of convergence;
- independent verification of generated recursions.

---

## Protocol 17. Falsification

The falsifier receives the exact claim, definitions, and permitted assumptions, but not the constructor’s persuasive explanation when isolation is feasible.

Required falsification axes:

- off-diagonal weights and loss of positive definiteness;
- concentrated and separated supports;
- high-frequency test functions;
- partial-diagonal collision patterns;
- inhomogeneous backgrounds;
- nonzero traceless strain;
- iid versus Gibbs preparation;
- endpoint temperature sequences;
- critical diagrams at arbitrarily high order;
- failure of uniformity in the cutoff or time horizon;
- noncommutation of limits;
- exact-centered versus mean-field-centered discrepancy.

A counterexample must state the precise class it disproves and the strongest surviving repair.

---

## Protocol 18. Audit independence

Use the following audit levels:

1. `UNAUDITED` — construction only.
2. `SELF_CHECKED` — constructor reran calculations and tests.
3. `ISOLATED_RECONSTRUCTION_PASS/FAIL` — fresh agent/session receives only frozen statement, definitions, permitted inputs, and conventions, reconstructs decisive steps before seeing the candidate proof.
4. `HOSTILE_REVIEW_PASS/FAIL` — separate referee sees the proof and actively searches for defects.
5. `EXTERNAL_AUDIT_PASS/FAIL` — reviewer outside the construction process.

A root coordinator that participated in construction cannot grant independent status. Role labels inside one uninterrupted context do not create independence.

Every audit report records:

- input dossier;
- isolation mechanism;
- repository commit/hash;
- exact claim reviewed;
- recomputed load-bearing equations;
- verdict;
- defects ordered by severity;
- scope not reviewed.

---

## Protocol 19. Retractions

When a promoted claim fails:

1. mark it `RETRACTED` immediately;
2. identify the exact failing line or assumption;
3. list every downstream claim affected;
4. remove it from current theorem summaries;
5. preserve the failed proof and audit report;
6. add the strongest correct negative conclusion to the obstruction ledger;
7. assign a new identifier to any repaired theorem;
8. state whether an external/public correction is needed.

Do not quietly weaken a theorem under the same identifier.

---

## Protocol 20. Git and file hygiene

- Preserve unrelated files.
- Use descriptive branches such as `algebra/k-body-generator`, `route/pair-poisson`, `route/cumulants`, `route/local-gibbs`, `renorm/uv-borderline`, `model/one-dimensional`, `audit/blind-thm-003`, `obstruction/weighted-positivity`.
- Do not rewrite history, force-push, or delete failed work.
- Keep build products under `BUILD/` and scratch under `SCRATCH/`.
- Put canonical proof documents under `MEMORANDA/`.
- Put immutable verdicts under `AUDITS/`.
- Put resumable state under `REPORTS/CHECKPOINTS/`.
- Put handoff archives under `PACKAGES/` with `SHA256SUMS.txt`.
- Record exact commands used to reproduce artifacts.
- Use UTC timestamps `YYYYMMDDTHHMMSSZ` in versioned output names.
- `CURRENT` files are pointers, never sole authoritative artifacts.
- Commit messages must state the mathematical gate changed.
- No push or remote mutation without owner authorization.

---

## Protocol 21. Mathematical writing

- Use standard terminology and the project’s canonical notation.
- Use \([N]:=\{1,\ldots,N\}\).
- Use uppercase \(X_N\) for a full configuration and lowercase \(x_i\) for one particle.
- Refer to the thermal equilibrium measure or density, not a “thermal profile.”
- Use precise limit variables and indexing parameters in uniformity statements.
- Distinguish “canonical Gibbs ensemble,” “modulated Gibbs law,” and iid product law.
- State short displayed computations proving centering and convergence claims.
- Reserve `Theorem` for headline results.
- Avoid promotional novelty language before source audit.
- A manuscript-ready proof must expose all regularization and coefficient dependencies.

---

## Protocol 22. TeX build and visual inspection

For every canonical TeX memorandum:

1. compile with `latexmk -pdf -interaction=nonstopmode -halt-on-error`;
2. resolve references and bibliography;
3. inspect logs for undefined/multiply defined labels, missing citations, overfull boxes, and font substitutions;
4. render every PDF page to images;
5. inspect for clipped text, broken glyphs, missing equations, and bad page breaks;
6. record the build command and result;
7. keep only final deliverables outside `BUILD/`.

Compilation is not mathematical verification.

---

## Protocol 23. Round reports

At the end of each substantive round create `REPORTS/ROUND_REPORTS/ROUND_XXX.md` using the template. Include:

- date and repository hash before/after;
- primary assertion and exact negation;
- routes executed;
- source claims checked;
- mathematical advances;
- falsifications;
- solvable-model and computation results;
- promotions/demotions/retractions;
- audit results;
- scaling and centering changes;
- current flagship;
- first open load-bearing assertion;
- next three executable actions.

User-facing updates should be shorter than the internal report.

---

## Protocol 24. Checkpoint and handoff

Before context compaction, model handoff, platform stop, or long interruption, create a versioned checkpoint containing:

- exact campaign state;
- active theorem/corrector cards;
- first open assertion for each route;
- most recent complete proof attempt;
- decisive equations, constants, and scaling tables;
- regularization and source status;
- failed tests and counterexamples;
- retractions;
- exact commands and outputs;
- canonical paths;
- repository hash and SHA-256 manifest;
- next three executable actions;
- paste-ready continuation prompt.

A successor must not need chat history.

---

## Protocol 25. User escalation

Continue autonomously without routine questions. Ask Matthew only under the stop conditions in `AGENTS.md`.

Promptly report material changes:

- a flagship lemma is proved/disproved;
- the critical law changes character;
- a finite hierarchy is ruled out;
- a new counterterm is load-bearing;
- a theorem range changes;
- an audit changes status;
- a source/publication issue requires a decision.

---

## Protocol 26. Publication and integration gate

No claim is ready for manuscript integration or public release until:

- the theorem statement and proof are frozen by hash;
- at least an isolated reconstruction and hostile review pass;
- every imported source is primary-verified;
- computations have independent certificates where used;
- the singular-limit and centering audits close;
- known limitations are stated;
- Matthew authorizes integration or release.

The campaign may prepare a manuscript-ready memorandum before this gate, but it must display the actual status.
