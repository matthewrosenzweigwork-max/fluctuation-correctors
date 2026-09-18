# TASK-075 — pre-seal verification

The assigned base is exactly `1df1805ed7cd8f7c295945f99273c8ffdb598e74`, and the branch is exactly `codex/hocf-r015-cubic`. The initially absent worktree and artifact directory were newly created. The isolated worktree had no unrelated modifications. After construction, Git status contains only the permitted copied task/theorem/manifest and this lane's assigned memorandum/artifact directory; no tracked base file changed.

Checks performed:

- All 27 input SHA-256 digests matched before copying and after copying. The exact checker checks them again.
- The fresh exact checker completed successfully. Its JSON records all counts, mutation witnesses, arithmetic convention, and nonclaims. The final checker run includes the independently reconstructed initial iid second moment.
- `git diff --check` passed. Because the newly created files are untracked, all issued Markdown and Python files were also scanned directly for trailing whitespace, control characters, final newlines, and syntax/delimiter consistency where applicable.
- The memorandum was reviewed against every THM-036 quantifier and exclusion: actual iid-Haar preparation, exact Fourier test, coefficient-one periodic Riesz kernel, both responses, physical scaling, genuine R8 domain, all background contractions, finite critical sequences, and absolute value after the time integral.
- Every exponent in the final upper bound is strictly negative on the frozen range. The exact rational grid includes dimensions beginning at four and values of the exponent approaching two from below; the displayed symbolic argument proves the entire interval.
- No TeX source was created or modified; no LaTeX mathematical expression is used in the final handoff. These deliverables are Markdown, Python, JSON, manifests, and an archive, so no TeX build was invoked.

The output manifest is generated only after these checks. The ZIP is then built from an explicit allowlist, its CRC and exact member list are checked, and every archived member is compared byte-for-byte by SHA-256 to the intended input/output. The separate `ARCHIVE_VERIFICATION.json` records those post-creation checks. The outer seal hashes the ZIP, output manifest, and archive verification report; it avoids a circular manifest.

Checks here establish reproducibility and exact finite algebra within this constructor context. They do not constitute independent analytic certification of this proof or its conditional premises. No failed check is being hidden. Any future correction must be a separately issued artifact.
