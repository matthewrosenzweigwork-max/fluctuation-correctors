# AUD060 sealed hostile-review packet

This is the complete bounded TASK092 handoff for the entire frozen THM042. The analytic verdict is **PASS on the conditional whole-claim hostile axis**, with no load-bearing mathematical repair or added hypothesis. The exact source premises and their earlier conditional histories remain unchanged. Root must separately compare the blind axis and source-gate provenance before any canonical promotion.

Read `REVIEW.md` for the full assertion and negation, per-claim analytic review, source boundaries, diagnostic limitations, and nonblocking finding AUD060-N01. The sibling `AUDITS/HOSTILE/ROUND_020_CONTINUOUS_PATH_REVIEW.md` is byte-identical. `SOURCE_EXPOSURE.md` records what this context actually read; `PROVENANCE.json` records the base, paths, environment, original manifest digest, and per-input check results.

## Contents and evidence classes

- `INPUTS/` contains all sixteen exact allowlisted input byte strings, including the full candidate, full permitted historical proofs, frozen theorem cards, task and source-exposure narrative. `INPUT_SHA256SUMS.txt` is the original routing manifest copied byte-for-byte.
- `hostile_exact_diagnostic.py` is a new standard-library exact diagnostic. `diagnostic_results.json` records **PASS: 3,316 assertions in 48 categories; 18 nonvacuous mutations rejected**. No old checker or separate saved result was read. Its Brownian Volterra path-functional tests, finite Fourier/Gram coefficient tests, positive Laplace-moment checks, compactness-inference controls and conditional exponential controls support the analytic review; they do not prove an actual singular estimate or theorem.
- `verify_packet.py` is read-only. It streams archives without extracting them; verifies every copied input, every payload byte, the complete archive inventory, sibling review equality, outer seal, and final output inventory; can reproduce the diagnostic stdout exactly; and rejects in-memory archive/manifest tampering.
- `PAYLOAD_SHA256SUMS.txt` hashes every payload file except itself. The external `SEAL.json` hashes that manifest, the sibling review, the original input manifest and the complete archive, with exact sizes/counts.
- The archive is `../ROUND_020_CONTINUOUS_PATH_HOSTILE_PACKET.tar.gz`. It contains exactly the payload with a single `packet/` prefix and no directory, link, duplicate or special members. Creation uses deterministic sorted USTAR members and gzip metadata.
- `../VERIFICATION_RESULTS.json` records the executed core byte verification and diagnostic reproduction while the final inventory was being prepared. It correctly marks that final list as not yet checked in that preparation run. The later strict final verification checks the finished list and read-only file modes; its stdout is the final handoff verification evidence.
- `../FINAL_SHA256SUMS.txt` covers every final file in this unique artifact directory, including the archive, seals and verification result, plus the sibling review. It excludes only itself. Its digest is supplied externally in the handoff; no self-hashing claim is made.

## Reproduce without changing any bytes

From the isolated worktree:

```text
python3 AUDITS/HOSTILE/ROUND_020_CONTINUOUS_PATH_HOSTILE_ARTIFACTS/packet/hostile_exact_diagnostic.py
python3 AUDITS/HOSTILE/ROUND_020_CONTINUOUS_PATH_HOSTILE_ARTIFACTS/packet/verify_packet.py --rerun-diagnostic --self-test-rejections
```

The second command is strict by default and requires the completed final seal and read-only issued files. Both programs write only to stdout and create no extracted files. The diagnostic has no seed because it makes no random draws, no floating-point tolerance, and no third-party dependency. Smooth Fourier differentiation in the coefficient probe is divided by `2*pi`; physical generator/bracket quantities share the restored `(2*pi)^2` factor. Polynomial Brownian-kernel calculations use exact isometry and integrated covariance formulas. Abstract Gram matrices are algebra controls, not Riesz particle configurations.

The verifier's `--prepare-seal` option was used once before creating the final output manifest to record core verification without a circular self-reference. It is not the final-verification command. Its rejection battery uses only in-memory archives; it tests changed bytes and sizes, missing/extra/duplicate members, traversal, absolute/dot/repeated-separator/backslash names, symbolic/hard links, FIFO/directory members, and duplicate/malformed/traversal hash listings. All 17 controls must be rejected.

The handoff digest authenticates the final manifest relative to this issuance. As with any unsigned artifact, a verifier cannot authenticate simultaneous malicious replacement of its code and every seal without that external anchor. Archive safety and hash agreement are provenance checks, not mathematical certification.

## Scope and next action

The full-source mathematical interfaces were checked. Earlier independent gate outcomes were not read and are not inferred from cards or historical status labels. No blind material, current state/history/memory, outside source, constructor code/result, install, child agent, commit, push, publication or author contact was used. No canonical source, ledger or previous audit was edited. Issued files are read-only. Corrections must be issued as new superseding artifacts, not edited into this packet.

Root compares this AUD060 packet with the separate fresh reconstruction and matches the frozen source gates. This completes the authorized bounded review, not the campaign.
