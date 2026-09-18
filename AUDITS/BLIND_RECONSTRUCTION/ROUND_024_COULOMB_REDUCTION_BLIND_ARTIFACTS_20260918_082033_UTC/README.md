# AUD067 sealed whole-claim reconstruction

Verdict: the entire THM047 conjunction is independently reconstructed relative to the exact supplied prior R5/R6/R8 contracts. The current constructor was withheld throughout. This does not promote canonical status or resolve THM046; root comparison and a separate hostile review remain.

The mathematical report is the sibling `ROUND_024_COULOMB_REDUCTION_RECONSTRUCTION.md`. The `dossier/` tree contains all 21 allowed source bytes, with their exact input hashes and byte-count inventory. SOURCE_EXPOSURE.md records what was fully read, partially read or only hashed, plus unavoidable ambient exposure. VERIFICATION_HISTORY.md records all pre-issuance checking and the sole pre-issuance checker cleanup. The fresh checker is `exact_checks.py`; its deterministic final output is RESULTS.json: 593 exact assertions, 19 categories, and 11 concrete nonzero mutation witnesses.

No external dependencies are needed. From the directory containing the report and this artifact directory, run:

    python3 -B ROUND_024_COULOMB_REDUCTION_BLIND_ARTIFACTS_20260918_082033_UTC/VERIFY.py

The verifier is read-only. It checks the complete copied dossier, output hashes, scoped file set, read-only regular-file safety, exact archive membership and bytes, CRC, and a fresh read-only checker run against RESULTS.json. It does not unpack, chmod, generate caches, replace files or rewrite results. Relocating the report, artifact directory and named sibling archive/member manifest together preserves this invocation. `--root PATH` permits an explicit relocated containing directory.

PACKET_LAYOUT.json gives the exact sibling archive, membership manifest, final verification JSON and outer-seal names. OUTPUT_SHA256SUMS.txt excludes itself to avoid a self-reference; the sibling member manifest includes it. The outer seal hashes the archive, member manifest, output manifest and final verifier JSON. To verify the final outer seal, run `shasum -a 256 -c` on its named file from this containing directory.

All issued member bytes are regular and read-only. No canonical files or frozen inputs were edited; there were no commits, pushes, dependencies, children, memory/history reads, external links, other-worktree reads, or current-constructor exposure. There is no TeX artifact or compile claim. Corrections must be separately issued.
