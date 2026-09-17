# Status vocabulary

## Mathematical status

- `OPEN` — no complete proof or disproof.
- `FORMAL_IDENTITY` — algebra at a formal level; singular/regularity issues unresolved.
- `EXACT_IDENTITY` — proved finite-\(N\) identity under stated regularity.
- `PROVED_CANDIDATE` — complete candidate proof, not independently audited.
- `CONDITIONAL` — proved assuming explicitly listed open inputs.
- `HEURISTIC` — scaling or mechanism only.
- `EXACT_REDUCTION` — equivalent or sufficient reduction to named obligations.
- `COUNTEREXAMPLE` — explicit example disproves a specified claim.
- `DISPROVED` — claim rigorously false in stated class.
- `RETRACTED` — previously promoted claim failed; prohibited from use.
- `BLOCKED_BY_EXTERNAL_INPUT` — genuinely unavailable private/source theorem required.

## Audit status

- `UNAUDITED`.
- `SELF_CHECKED`.
- `ISOLATED_RECONSTRUCTION_PASS`.
- `ISOLATED_RECONSTRUCTION_FAIL`.
- `HOSTILE_REVIEW_PASS`.
- `HOSTILE_REVIEW_FAIL`.
- `EXTERNAL_AUDIT_PASS`.
- `EXTERNAL_AUDIT_FAIL`.

## Source status

- `UNCHECKED`.
- `SECONDARY_ONLY`.
- `PRIMARY_LOCATED`.
- `PRIMARY_VERIFIED`.
- `VERSION_LOCKED`.
- `SUPERSEDED`.
- `SOURCE_MISMATCH`.

## Computation status

- `EXPLORATORY`.
- `REPRODUCED`.
- `RIGOROUSLY_ENCLOSED`.
- `CERTIFICATE_VERIFIED`.

## Manuscript status

- `NOT_DRAFTED`.
- `INTERNAL_MEMORANDUM`.
- `MANUSCRIPT_READY_PENDING_AUDIT`.
- `AUTHOR_ACCEPTED`.
- `PUBLIC_RELEASE_AUTHORIZED`.

Never write “verified” or “certified” without the corresponding explicit axis and report.
