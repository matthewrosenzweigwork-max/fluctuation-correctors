# AUD062 immutable hostile-review packet

TASK095, 2026-09-18 UTC. Verdict: **WHOLE-CLAIM HOSTILE PASS for the entire frozen THM043 conjunction**, with no range repair or missing analytic input in the permitted dossier. This is the isolated hostile axis, exposed to the full constructor proof. Root alone compares it with the separate reconstruction, matches historical source gates and promotes any theorem. The full campaign remains outside this bounded verdict.

The report is the adjacent `../ROUND_021_CRITICAL_CUBIC_REVIEW.md`. This directory contains the exact 32 permitted inputs, the original input hash manifest, exposure/source records, a fresh independent exact diagnostic, its actual results, a read-only byte/membership verifier, and a complete sealed archive. No other worker output or old checker was read. Source status labels and embedded checker summaries were never mathematical premises.

From the worktree root, reproduce integrity checks without extracting or modifying anything:

    python3 AUDITS/HOSTILE/ROUND_021_CRITICAL_CUBIC_HOSTILE_ARTIFACTS/verify_packet.py --self-test

This pins the original input manifest digest; verifies all 32 input byte strings, nine payload outputs, the output manifest, exact local file/directory membership, 42 archive members, archive CRC and bytes, and the outer seal; and rejects ten in-memory archive/manifest mutations. It writes no file. Symlinks, duplicate names, traversal/absolute paths, directories in the ZIP, unexpected members and modified bytes are rejected.

The independent mathematical diagnostic can also be reproduced read-only:

    python3 AUDITS/HOSTILE/ROUND_021_CRITICAL_CUBIC_HOSTILE_ARTIFACTS/exact_diagnostic.py

It prints deterministic JSON. Its initial recorded run used `--write` before sealing to create `RESULTS.json`; do not run that writing option on an issued packet. Actual result: **137,147 exact assertions, 29 categories, 12,384 distinct admitted parameter pairs, ten coefficient/sign mutation witnesses and four exponent mutation controls, PASS.** Finite smooth Fourier models, time jets and Laplace moments support the analytic audit; they do not prove singular estimates. There is no randomness, numerical tolerance, external dependency or installation.

`OUTPUT_SHA256SUMS.txt` hashes exactly the report and eight payload files in this directory. It excludes itself to avoid a hash cycle. `ARCHIVE_MEMBERS_SHA256SUMS.txt` specifies the complete ZIP member set: 32 `inputs/` members and ten `outputs/` members, the latter including the output manifest. It is outside the ZIP to avoid another hash cycle. `SEAL.json` hashes the input, output and archive-member manifests and the complete ZIP. The verifier hard-codes the expected output names and pins the input manifest, so an omitted or extra output cannot be hidden by editing only an unhashed membership list.

The ZIP is `AUD062_PACKET.zip`. It contains only regular files and preserves every member's exact bytes. The ZIP does not contain itself, the external archive-member manifest or the outer seal. The local packet includes those three final controls, for 44 files in this directory and the adjacent report. All issued files are read-only after verification. This is an integrity packet, not a digital signature or independent certification of root chronology. Any later correction must be separately named and sealed; never edit issued bytes.

Prescribed provenance: branch `codex/hocf-r021-critical-cubic-hostile`, worktree `/Users/matthewrosenzweig/.codex/worktrees/hocf-r021-critical-cubic-hostile`, published base `64ac0538dff37a37d0883661b401ad04c311a5e5`. No canonical edits, child, install, commit or push. No TeX source was changed and no PDF/build claim is made for these Markdown/code outputs. See `VERIFICATION.md` for the executed checks and limitations.
