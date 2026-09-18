# AUD068 diagnostic history

The diagnostic was newly written in the assigned artifact directory. No prior
checker or constructor result was read. No assertion failure was observed.

1. An initial dry run of the draft was started. The orchestration call printed
   only its empty early output and did not preserve/forward the ongoing session
   identifier. Its eventual result was not observed and is not credited.
2. A second dry run of the same draft was observed to completion: PASS, 885
   assertions, 18 nonzero mutation witnesses. Draft SHA-256:
   `ac66278ee340acdc4855cec086e030a7fe33517373b8d727b588b3288dc26a5a`.
3. Before issuance, two tautological support checks were removed and six
   substantive constant-test/constant-response checks were added. No failed
   coefficient or theorem argument prompted this revision. The exact prior
   draft bytes are retained at `history/UNISSUED_DRAFT_v0.py` and their hash
   was checked against the previously observed hash.
4. The issued diagnostic ran with explicit results output: PASS, 889 assertions,
   18 nonzero mutation witnesses. Its code SHA-256 is
   `fec384535da1f152b8ae56af755be39407aae2dba9427aa477065912d4b9b480`.
   Complete category counts and exact nonzero witnesses are in `RESULTS.json`.
5. A read-only `--check RESULTS.json` run was observed to completion: PASS,
   889 assertions and 18 nonzero witnesses, with the same issued code hash.
   This compares regenerated results with the issued JSON interpreted as JSON.
   Syntax parsing and the new-text hygiene checks also passed; all 24 original
   input digests and all 24 copied digests were rechecked successfully.
6. Packet verification separately checks source/result bytes, all input copies,
   closed membership, regular read-only modes, ZIP CRC, and external seals.
   The final handoff and sibling verification seal record its observed outcome.

Arithmetic: Python standard-library `Fraction`; no floating point, random seed,
sampling tolerance or installed dependency. Derivatives divide by 2 pi i;
second-order physical expressions divide by 4 pi squared, with the resulting
minus sign in gradient products retained. One-coordinate algebraic probes
embed in T4, while the Coulomb flux test also uses full four-dimensional
frequency vectors. All domain/martingale passages remain analytic proof
obligations checked in the review; no finite calculation substitutes for them.

All records here precede packet issuance. The draft is historical supporting
evidence, not a second competing issued diagnostic or theorem statement.
