# TASK-076 verification record

2026-09-18 UTC. Verification of this new review packet is a reviewer self-check. The hostile mathematical review is separate from the constructor context; this packet's own exact diagnostic and integrity checks do not independently certify this review, any earlier premise, or the cubic limit.

## Exact diagnostic

Final command from the assigned worktree:

```text
python3 AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/exact_hostile_diagnostic.py
```

Outcome: **PASS, 236,686 exact assertions; all nine deliberately wrong coefficient alternatives detected.** The full assertion categories and exact polynomial witnesses are in `RESULTS.json`. There are 84 complete finite-label cases, 27,716 admitted exponent cases, 12,384 strict critical exponent cases, and 34,875 elementary signed-function/empirical-measure constant checks. Rational exponent tests use dimensions 3 through 30 and denominators through 17. No floating tolerance or random seed is used.

The diagnostic was initially run against the isolated source copies. Before issuance, two administrative refinements were made to the new checker: the JSON boundary label for the R12 critical range was made to include strict positivity/sub-Coulombity as well as the quadratic inequality; input lookup was changed to the packet-adjacent frozen `INPUTS/` for portability. No assertion failed before or after these refinements. The issued source is the final portable version, and no already issued input was changed.

A final replay uses the absolute checker path with working directory `/` and a new output file `REPLAY_RESULTS.json`. It consumes only the adjacent packet inputs and standard library. Its JSON is compared byte-for-byte with `RESULTS.json`; the seal procedure below requires equality before archive creation. The input-copy tests are included in each diagnostic run.

## Input, text, and worktree checks

- All 27 controlling input hashes matched at the source before copy, in the isolated worktree after copy, and in the portable packet copy. A final check re-read only those 27 paths at the canonical source and confirmed they remained unchanged.
- Every newly written text file was checked for UTF-8 decoding, terminal newline, no control characters other than ordinary whitespace, and no trailing whitespace. Markdown display delimiters were balanced. Both Python programs were parsed as Python syntax without creating bytecode caches. JSON results were parsed successfully.
- `git rev-parse HEAD` matched `072cab684b9ce41855ead6c48f435c8fc184ec35`, and `git branch --show-current` matched `codex/hocf-r014-lower-hostile`.
- The isolated worktree's complete status path set was checked to contain only copied allowlisted inputs, the controlling manifest, the assigned report, and this uniquely named packet. No unrelated inherited file content was inspected or changed.
- `git diff --check -- AUDITS/HOSTILE/ROUND_014_LOWER_DRIFT_REVIEW.md AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC` passed. Since the new report/packet are untracked, the direct text checks above are the substantive text validation; a clean tracked diff alone would not verify them.

The review's mathematical derivations were checked against every assertion in the frozen card and entire constructor, including the stronger claims and the separate erratum. The report identifies exact locations and conditional boundaries. This is mathematical review evidence, not a claim that successful compilation or a numerical battery proves an analytic theorem.

No TeX source was created or edited. These are Markdown/code/JSON/archive deliverables. No TeX build or PDF rendering was performed, and no rendered-layout certification is claimed. The original malformed sum is deliberately preserved; its separate erratum was assessed against the exact frozen mathematical convention.

## Output and archive seals

`OUTPUT_SHA256SUMS.txt` enumerates every substantive output plus all 27 copied input files. It excludes itself and external archive/seal sidecars, avoiding a circular digest. Paths are relative to the worktree or an extracted archive root. `SEALED_PACKET.zip` contains exactly that list plus the output manifest, and no inherited repository files or unrelated root state.

The integrity verifier checks all input/output digests, exact archive member set, unique safe relative names, absence of directory entries, archive CRC, and member-by-member equality with the sealed external files. `SEAL_VERIFICATION.json` records that archive verification before the final external seal is written. Its `external_seal_checked` value is therefore false by construction; it is not a failed check. The subsequent `SEAL_SHA256SUMS.txt` hashes the archive, output manifest, and this verification JSON. A final verifier run after creating that seal checks all three external entries as well.

Commands used in the final sealing sequence:

```text
python3 AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/verify_packet.py --require-archive --output AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/SEAL_VERIFICATION.json
python3 AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/verify_packet.py --require-archive
```

The issuing sequence requires every check to succeed and makes issued report/packet files read-only only after success. No canonical ledger or root source was edited; no commit, push, installation, external search, prior checker, or child agent was used. Any future correction must be issued separately, preserving this packet's bytes.
