# TASK-061 sealed actual-law packet

Issued 2026-09-18 UTC from the isolated `codex/hocf-r010-law-falsification` worktree at published R8 `b2510ed08ecc26387d9fc14daaf174d3c35f5638`.

The genuine singular full-corrector noise target remains open and was not falsified. The report proves actual-law energy and Fourier estimates, a low-noise labelled trajectory estimate, actual bracket decay for explicit smoothings of the genuine full inverse, and equivalence of the full target with one specified singular-tail estimate. The independent actual-law initial triple derivative is nonpositive for every smooth centered probe. There is no uniform singular Taylor remainder claim.

Read `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md` first. Sections 2–6 contain the new proof; Section 7 states the exact remaining gap; Section 8 gives the independent falsification attempt; Section 10 records per-claim status. All new proof claims are self-checked and require fresh review. The report preserves every imported module's scope and treats the supplied R9 reference-energy reconstruction as conditional. Its extra pointwise estimate is not used.

Outputs:

- `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md`: complete analytic attempt and dispositions.
- `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION_README.md`: this handoff.
- `AUDITS/ROUND_010_LAW_FALSIFICATION_EXPOSURE.md`: exact isolation, inputs, and worktree provenance.
- `VERIFICATION_CODE/round010_actual_law_exact.py`: newly written standard-library exact Fourier diagnostic.
- `VERIFICATION_CODE/round010_actual_law_exact_output.json`: PASS, 1,421 exact assertions and twenty verified input digests.
- `AUDITS/ROUND_010_LAW_FALSIFICATION_INPUT_SHA256SUMS.txt`: original twenty-file input manifest, preserved byte-for-byte.
- `AUDITS/ROUND_010_LAW_FALSIFICATION_OUTPUT_SHA256SUMS.txt`: issued output hashes, excluding this manifest itself.
- `ARCHIVES/ROUND_010_ACTUAL_LAW_FALSIFICATION_20260918_024821_UTC.zip`: sealed packet with inputs under `COPIED_INPUTS/` and named outputs only.
- `AUDITS/ROUND_010_LAW_FALSIFICATION_ARCHIVE_SHA256SUMS.txt`: archive and manifest seal.

Verification command, run from the isolated worktree:

```text
python3 VERIFICATION_CODE/round010_actual_law_exact.py
```

It uses exact Gaussian-rational arithmetic without numerical tolerances, random sampling, an earlier checker, or additional dependencies. After archive extraction it automatically locates the sealed inputs under `COPIED_INPUTS/`; within the original worktree it uses the same manifest paths directly. It supports algebraic factors and signs, and does not replace the analytic singular-limit proof. The issued archive is checked for CRC, exact member set, and member-by-member SHA-256 equality to the named files; output and copied-input hashes are checked separately. No TeX source or compiled PDF is part of the assigned Markdown/checker packet. The final handoff uses no mathematical LaTeX.

The root must integrate and assign any new canonical identifiers. No canonical state or cumulative memorandum was edited, no commit or push was made, and no dependency was installed. Issued bytes are immutable; any correction should be separately named and sealed.
