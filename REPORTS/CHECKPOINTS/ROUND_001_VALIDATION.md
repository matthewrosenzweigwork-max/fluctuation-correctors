# Round 001 final validation

UTC checkpoint: 20260917T184919Z. Commands below were executed in the root repository after canonical integration. All returned exit 0.

## python3 scripts/check_campaign_provenance.py

Exit 0.

```text
CAMPAIGN VERIFICATION PASSED
Repository root: /Users/matthewrosenzweig/Library/CloudStorage/GoogleDrive-mrosenz2@andrew.cmu.edu/My Drive/Git/fluctuation-correctors
Imported note SHA-256: a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76
PROTECTED BASELINE PASS: 51 immutable entries
Documented mutable paths differing from baseline: 23
  APPROACHES/DEPENDENCY_GRAPH.md
  APPROACHES/OBSTRUCTION_LEDGER.md
  APPROACHES/ROUTE_REGISTRY.md
  STATE/ASSUMPTIONS_AND_CONSTANTS_LEDGER.md
  STATE/BIAS_AND_CENTERING_LEDGER.md
  STATE/CAMPAIGN_STATE.md
  STATE/COMPUTATION_LEDGER.md
  STATE/CORRECTOR_LEDGER.md
  STATE/COUNTERTERM_AND_CONTRACTION_LEDGER.md
  STATE/DECISION_LOG.md
  STATE/DIAGRAM_AND_POWER_COUNTING_LEDGER.md
  STATE/ENVIRONMENT.md
  STATE/LAW_CLASS_AND_GEOMETRY_LEDGER.md
  STATE/MARTINGALE_AND_QUADRATIC_VARIATION_LEDGER.md
  STATE/NORMALIZATION_AND_SCALING_LEDGER.md
  STATE/OPERATOR_AND_SEMIGROUP_LEDGER.md
  STATE/PROOF_OBLIGATION_LEDGER.md
  STATE/REGULARIZATION_LEDGER.md
  STATE/RETRACTION_LEDGER.md
  STATE/SOURCE_LEDGER.md
  STATE/STATIC_DYNAMIC_INTERFACE_LEDGER.md
  STATE/THEOREM_LEDGER.md
  TASKS/QUEUE.md
```

## python3 scripts/verify_campaign.py

Exit 0.

```text
CAMPAIGN VERIFICATION PASSED
Repository root: /Users/matthewrosenzweig/Library/CloudStorage/GoogleDrive-mrosenz2@andrew.cmu.edu/My Drive/Git/fluctuation-correctors
Imported note SHA-256: a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76
```

## git diff --check

Exit 0.

```text
(no output)
```

## git diff --cached --stat

Exit 0.

```text
(no output)
```

## git rev-parse HEAD

Exit 0.

```text
475a5399828bc6e2ccbade08c59b8778638df14a
```

## git rev-list --all --count

Exit 0.

```text
1
```

## Additional exact checks

PASS: all 13 owner-required paths exist and are readable. PASS: source PDF and original ZIP digests equal the verified package values. PASS: pair, recursion/falsification and analytic audit input manifests match frozen bytes; analytic output manifest matches issued reports. PASS: index empty, HEAD remains the sole baseline commit. No push command, remote mutation, history rewrite, dependency install or cleanup deletion was performed.

Artifact format scan: the first broad scan flagged intentional Markdown hard breaks in BBGKY report lines 3–6 and absent terminal newlines in three raw PDF text extractions. These hashed evidence bytes remain unchanged. The subsequent scoped scan accepts exactly those formats and passes: no accidental control characters or other new trailing whitespace/missing newline. Original imported hard-break warnings remain documented in the immutable installation report. No working tracked diff whitespace error.

Exact finite test outcomes, source evidence, resolved extraction/build failures and final six-page PDF QA are in CERTIFICATES/ROUND_001_VERIFICATION.md and immutable audit reports. The full working status/file inventory is recorded separately. Checkpoint and ZIP hashes are generated after these records and verified independently to avoid self-reference. These checks do not certify an open mathematical assertion.
