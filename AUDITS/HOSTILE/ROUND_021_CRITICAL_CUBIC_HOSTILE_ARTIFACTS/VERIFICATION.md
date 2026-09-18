# AUD062 executed verification record

2026-09-18 UTC. The exact original 32-input manifest was checked before worktree creation and before any mathematical use. The prescribed base and branch were used, each overlay byte string was verified, and every packet input copy was checked again. Original manifest SHA-256: `1e0082cbce0d36476c5ffabf71f21e7f4af8efbfcd1ed181dadef9ed68d3f13e`.

The new mathematical diagnostic was executed from the isolated worktree:

    python3 AUDITS/HOSTILE/ROUND_021_CRITICAL_CUBIC_HOSTILE_ARTIFACTS/exact_diagnostic.py --write

Exit status 0. Actual outcome: **PASS, 137,147 exact assertions in 29 categories**, including 12,384 distinct admitted rational parameter pairs. `RESULTS.json` records every category count, exact nonzero coefficient/sign mutation witness, four exponent controls, nonzero integrated cubic jets and the diagnostic's SHA-256. The whole-bracket test compares the directly differentiated statistic with an independent generator-product carré-du-champ computation, including all empirical/background terms. No old checker, external package, random seed or floating arithmetic was used.

The output files were scanned directly for UTF-8 readability where applicable, terminal newlines, trailing whitespace, and unexpected control characters; the exact copied inputs were never normalized. `git diff --check` passed on the prescribed worktree's tracked diff. The separate direct scan includes untracked newly created files. Exact input bytes were rechecked against the frozen manifest. Git metadata confirmed the prescribed base and branch. These checks are bookkeeping, not mathematical certification.

The complete output manifest, archive-member manifest, ZIP and outer seal were then generated from the final payload. The final read-only command is:

    python3 AUDITS/HOSTILE/ROUND_021_CRITICAL_CUBIC_HOSTILE_ARTIFACTS/verify_packet.py --self-test

The handoff is issued only after this command passes against the final bytes and again after making issued files read-only. Its asserted final outcome is **PASS**: exactly 32 input files, nine payload outputs, 44 local packet files plus the adjacent report, and 42 archive members, with complete local file/directory membership, every digest, CRC and safe ZIP membership verified without extraction. Ten deliberately malformed in-memory variants are rejected: duplicate member, missing member, extra member, traversal path, absolute path, changed bytes, symlink member, directory member, duplicate manifest path and unsafe manifest path. The command writes no file; final machine output is delivered with the sealed handoff. No issued payload is modified to record that last output.

No full campaign verifier was run because it would consume nonpermitted state and unrelated dossiers. No TeX source was changed or created; the final handoff uses no mathematical LaTeX. There was no dependency installation, commit, push, source/canonical edit, external browse or child. The mathematical audit is the report's analytic per-claim disposition; finite diagnostics and byte checks do not replace it. Root source-gate matching, chronology certification and the other independent audit axis remain outside this lane.
