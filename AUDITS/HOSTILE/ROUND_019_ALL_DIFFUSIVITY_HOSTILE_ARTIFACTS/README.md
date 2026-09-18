# AUD058 / TASK089 sealed hostile handoff

The complete review is `REPORT.md`, identical to the separately issued `../ROUND_019_ALL_DIFFUSIVITY_REVIEW.md`. Its verdict is PASS for the entire frozen THM041 mathematical conjunction; root alone matches earlier source gates, compares the separate reconstruction, and integrates. This packet is source-exposed hostile review, not a blind proof or a chronology certificate. No source claim was repaired.

The fifteen hash-locked source copies are under `INPUTS/`. `INPUT_SHA256SUMS.txt` is byte-identical to the supplied hostile input manifest. `SOURCE_EXPOSURE_PREFLIGHT.md` records the source boundaries and actual exposure.

`fresh_exact_diagnostic.py` was authored de novo. It tests source/force/energy labels, retained-symbol and remainder constants, all-noise energy algebra, formal fixed-time covariance and initial moments, true Brownian bracket factors, conditional martingale dependence, the L1-only tail mechanism, and failures of pointwise-to-uniform or density-without-tails shortcuts. Its final Python 3.9.6 run contains **7,564 exact assertions in 40 categories and 879 mutation rejections in 24 families**. All calculations use integers, rational numbers, Gaussian rational pairs, or exact formal polynomial identities. No randomness, tolerance, dependency installation, or prior program was used. Diagnostic examples are proof-step challenges, not claimed singular-particle counterexamples or replacements for analytic proof.

From the isolated worktree root, reproduce the diagnostic with:

    python3 AUDITS/HOSTILE/ROUND_019_ALL_DIFFUSIVITY_HOSTILE_ARTIFACTS/fresh_exact_diagnostic.py

From this artifact directory, verify the complete sealed handoff without writing files:

    python3 seal_and_verify.py --verify

The verifier compares rerun stdout byte-for-byte with `DIAGNOSTIC_RESULTS.json`; checks the fifteen input copies and their exact digest list; checks every payload digest; validates the complete archive-member set, names, regular-file types, size and bytes without extraction; checks the archive and outer handoff seals; and verifies every artifact and the external report is read-only. It uses only Python's standard library.

The seals are layered deliberately to avoid recursive hashing:

1. `OUTPUT_SHA256SUMS.txt` hashes every payload file: all fifteen input copies, the report, this README, source/exposure preflight, input manifest, program, actual result, and verifier.
2. `SEALED_PACKET.tar.gz` contains exactly those payload files plus `OUTPUT_SHA256SUMS.txt`, under one safe directory prefix. Every archived entry is a regular read-only file. The archive is deterministic with zeroed time/ownership fields. It excludes its own digest and the outer verification records.
3. `ARCHIVE_SHA256SUMS.txt` hashes the complete archive. `SEAL_VERIFICATION.json` records successful byte/safety/reproduction checks and the relevant digests.
4. `HANDOFF_SHA256SUMS.txt` hashes every final artifact file other than itself, including all inner seals, archive, and verification record. The final handoff reports the digest of this outer manifest and of the separately issued report.

The complete archive is a self-contained payload, not a recursive package of its own outer seals. The full artifact directory supplies the archive's external seal and verification record. No unsafe or arbitrary extraction is part of verification.

All issued files and artifact directories are read-only. Do not modify issued bytes; a later finding requires a new superseding audit. No canonical ledger or source, earlier audit, Git commit, or remote was modified by this lane.
