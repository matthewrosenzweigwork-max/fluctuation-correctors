# TASK-046 sealed independent reconstruction

2026-09-17 23:48:58 UTC.

Verdict: every frozen THM-026 assertion is reconstructed. No unsupported line or counterexample was found within the stated scope after acceptance of the permitted local kernel/divergence prerequisite. This is a statement-only reconstruction; the constructor's separate hostile audit and root comparison remain required. No canonical theorem status is changed.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r006-particle-blind`.
Branch: `codex/hocf-r006-particle-blind`.
Unchanged HEAD: `93c20daa45aad455a95437b1dc6beed2883afada`.

The six dossier files were hash-checked at source before copying, copied byte-for-byte, and checked again in the isolated worktree after proof completion. Only the permitted dossier was read; no TASK045 narrative, periodic singular proof, other review, canonical state/history, memory, or unrelated source was consulted. THM-021's mathematical use is limited to local kernel, heat, and divergence prerequisites. No root working-tree edits, commits, pushes, dependency changes, or child workers occurred.

## Completed verification

- `python3 AUDITS/BLIND_RECONSTRUCTION/check_round006_particle_exact.py`: exit 0, 242 exact checks passed on Python 3.9.6.
- `shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_006_PARTICLE_INPUT_SHA256SUMS.txt`: all six inputs OK.
- Python `ast.parse` of the checker: valid syntax.
- Report checks: 36 distinct sequential equation labels, balanced mathematical delimiters, and no trailing whitespace in the sealed text files.
- `git rev-parse HEAD` and `git branch --show-current`: values above.
- No TeX was edited; the requested output is the complete Markdown reconstruction. No unrelated repository build or campaign-wide verifier was run.

## Content hashes before seal

- `ROUND_006_PARTICLE_INPUT_SHA256SUMS.txt`: `b348664ec3ba9f346302026170fccc2e5a727d6b66ec79596c907c5fc034a50f`.
- `ROUND_006_PARTICLE_RECONSTRUCTION.md`: `bbbf50b98e09499d1bde225d8a82bcef560276e6126f4cf3e8a6009af2fc1f00`.
- `check_round006_particle_exact.py`: `eec916b463e07095d164308640aee9384008f87c428be0fc8b487bc55d55c448`.
- `ROUND_006_PARTICLE_CHECK_RESULTS.txt`: `16e2d251a0adf7798fad43f35804e6fde8c76d9b9c67ec82d4e8a57f91abda97`.

The output manifest also covers this seal. After it is issued, all listed output bytes are immutable; any correction must be a separately named superseding report. The manifest itself is not self-hashed. Root may copy the sealed output files for comparison and later canonical integration.
