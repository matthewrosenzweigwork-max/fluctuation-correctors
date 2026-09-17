# Read first: higher-order correctors to Coulomb/Riesz fluctuations

**Campaign code:** `HOCF-RIESZ`  
**Status:** frozen campaign baseline  
**Owner:** Matthew Rosenzweig  
**Primary coordinator:** Astra Ultra  
**Default workers:** Astra Max

## Mandatory reading order

Before changing any mathematics, read:

1. `AGENTS.md`;
2. `MASTER_PROMPT.md`;
3. `CAMPAIGN_PROTOCOLS.md`;
4. `MODEL_ORCHESTRATION.md`;
5. `BASELINE/INITIAL_MATHEMATICAL_STATE.md`;
6. `BASELINE/INITIAL_CRITICAL_ASSESSMENT.md`;
7. `PLANS.md`;
8. `INPUTS/SOURCE_MANIFEST.md` and `INPUTS/note_v2.pdf`;
9. every canonical file in `STATE/`.

Then run:

```bash
python3 scripts/verify_campaign.py
```

Do not begin by drafting a survey or another plan. Execute Phase 0 in `PLANS.md`, freeze the exact model and normalization, independently reconstruct the finite-
\(N\) duality and quadratic-corrector identities, and open the first round report.

## Authority order

When instructions conflict, use this order:

1. a direct instruction from Matthew Rosenzweig in the current campaign;
2. `AGENTS.md`;
3. `MASTER_PROMPT.md`;
4. `CAMPAIGN_PROTOCOLS.md`;
5. frozen baseline and state ledgers;
6. active task cards;
7. source notes and prior model output;
8. informal comments and scratch work.

A source note may contain a mathematical claim but does not override campaign audit rules. A prior status label is not evidence.

## First launch

Use `KICKOFF_PROMPT_ULTRA.md` in the root Astra Ultra session. Ultra should create Max workstreams according to `MODEL_ORCHESTRATION.md` and preserve a single-writer merge discipline.
