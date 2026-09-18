# Round 026 response blind reconstruction evidence

TASK112 / AUD071. Whole THM050 reconstruction from eight sealed inputs. The report reconstructs all of A, B and C; the root owns whole-proof comparison and promotion. The actual critical source and weaker response target remain open.

`RECONSTRUCTION.md` is byte-identical to the assigned sibling `ROUND_026_RESPONSE_RECONSTRUCTION.md`. `SOURCE_EXPOSURE.md` records all input reads, historical source status, automatic context and isolation limits. The complete exact inputs are in `inputs/`; `INPUT_SHA256SUMS.txt` is the supplied manifest, copied verbatim. The included input verification result records all eight matching hashes.

`code/diagnostic.py` contains fresh exact-rational supporting tests. Its first execution passed **256 checks** and detected **30 deliberately wrong controls with nonzero exact residuals**. There is no tolerance, seed, external library, singular-process simulation, or computational mathematical-certification claim. The saved result includes every check and mutant. `results/diagnostic_attempt_01.json` records the actual command, Python version, zero exit code and empty stderr. There were no baseline execution failures.

From any location, with Python 3.8 or newer, run:

```text
python3 /path/to/ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC/code/verify.py
```

The verifier is read-only. It checks exact external seals, every payload file, eight input hashes, complete filesystem and archive membership, regular-file-only archive safety, read-only payload modes, report equality, and exact diagnostic reproduction. It reads the archive without extracting it. It creates no files, makes no network request, invokes no repository commands, and installs no dependency. Its result is also preserved in the named sibling `.VERIFY.json`.

Keep the directory and these sibling files together for portable verification:

* `ROUND_026_RESPONSE_RECONSTRUCTION.md`
* `ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC.tar.gz`
* `ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC.FILES.json`
* `ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC.SHA256SUMS.txt`
* `ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC.SEAL.md`
* `ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC.VERIFY.json`

The external inventory lists every regular archive/payload member with its exact path, size, mode and SHA-256, including the internal hash manifest. The internal `SHA256SUMS.txt` hashes every other payload member. Its own hash is in the external inventory, avoiding a circular self-hash. The external SHA-256 seal covers the archive, inventory, seal note, assigned report and saved verification result. Its checksum is reported at handoff as an external trust anchor; hashing alone does not authenticate authorship.

All issued payload files and siblings are read-only, and the payload directories are read-only. Corrections require distinct superseding artifacts; do not edit this issued report or packet. No campaign source/state, historical input, dependency, repository history or remote was modified. There is no TeX artifact or unrelated build; the assigned proof is Markdown and the final handoff is prose without mathematical LaTeX.
