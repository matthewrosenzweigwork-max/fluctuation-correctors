# AUD052 sealed hostile-review packet

Verdict: full hostile PASS for the frozen THM038 card and complete Round 016 candidate, including the stronger mathematical assertions itemized in the report. No mathematical repair is required. This is the intentionally candidate-exposed hostile lane; root compares it with the withheld blind reconstruction and alone assigns canonical status. Earlier complete local modules retain their issued conditional scope and status.

The report is `../ROUND_016_SOURCE_EXTENSION_REVIEW.md`. This unique artifact directory contains the new exact diagnostic and results, exposure declaration, complete source preflight, all eleven byte-identical input copies, and reproducible packet verification controls.

## Contents and evidence

- `independent_diagnostic.py`: new standard-library exact rational/Gaussian-rational diagnostics. No prior checker is read. Spatial derivatives are divided by twice pi; the scalar source and particle generator are divided by four pi squared. These finite examples check coefficients; the report supplies the singular analytic arguments.
- `independent_diagnostic_results.json`: PASS, 1,700 assertions in 37 categories. All eight deliberate coefficient errors were detected. Exact parameters, results, normalizations, and script digest are recorded.
- `SOURCE_PREFLIGHT.md`, `INPUT_SHA256SUMS.txt`, and `INPUTS/`: exactly eleven frozen input byte strings, their digests, read ranges, and permitted uses. The candidate is included intentionally; no blind output or earlier checker is included.
- `EXPOSURE.md`: intentional and ambient exposure, scope restrictions, and action declaration.
- `seal_packet.py`: packet construction and read-only verification, confined to the literal payload. It does not read state/history, mathematical files outside the allowlist, or earlier checkers.
- `ARCHIVE_MEMBERS.txt`: exact sorted list of the 21 permitted regular-file archive members, including this member list and the output manifest.
- `OUTPUT_SHA256SUMS.txt`: digests of all 20 payload files other than this output manifest itself. The output manifest's digest is separately sealed.

## Archive and noncircular controls

Archive filename:

    ROUND_016_SOURCE_HOSTILE_AUD052_20260918_053542_UTC.tar.gz

The archive includes the report and the artifact payload at their repository-relative paths. It contains no directory entries, links, duplicate names, absolute paths, or traversal components. Every member has mode 0444, zero timestamp, zero uid/gid, and empty owner/group names. Gzip metadata is deterministic. Literal member order/set and every decompressed byte string are compared against the declared payload, rather than merely accepting an archive-open success.

The archive does not contain itself or its external seal controls. `ARCHIVE_SHA256SUMS.txt` seals its bytes. `SEAL_REPORT.json` records the archive, input/output/member manifests, report digest, exact counts, safety checks, and read-only controls. `SEAL_SHA256SUMS.txt` seals those external controls plus the manifest and archive byte strings without including its own digest. The handoff separately gives the digest of that final seal manifest, avoiding a self-hash cycle.

All issued files are set to 0444, and directories within this artifact packet to 0555. The copied worktree inputs are also set to 0444. These are read-only permissions and byte-digest seals, not a claim that a filesystem owner cannot intentionally undo permissions. Corrections must be separately issued.

## Verification

The diagnostic was executed before sealing:

    python3 AUDITS/HOSTILE/ROUND_016_SOURCE_HOSTILE_ARTIFACTS/independent_diagnostic.py

It passed with no suppressed failure. Do not rerun it in place inside the sealed directory, since that command writes its JSON output. For a diagnostic rerun, copy the script alone to a separate writable directory and compare its JSON with the issued result; it reads no other input.

Before sealing, inline Markdown math delimiters introduced during report writing were corrected. One packet-preparation orchestration call had a quoting-related syntax error before execution; its corrected call copied and hash-verified all eleven inputs. These were drafting/tooling corrections, not a failed mathematical check. The independent diagnostic passed on its first execution.

Read-only packet verification, from the worktree or a repository containing the integrated report and packet:

    python3 AUDITS/HOSTILE/ROUND_016_SOURCE_HOSTILE_ARTIFACTS/seal_packet.py --verify

The verifier checks the eleven packet input copies, the independent diagnostic's recorded script digest and assertion totals, every output byte, exact archive members/bytes/metadata, archive digest, all external seal hashes, literal artifact file/directory inventory, and read-only file/directory permissions. It runs in-memory negative controls for traversal, duplicate names, symlinks, hard links, unexpected members, and altered bytes. It does not rerun the diagnostic or modify sealed files. At original sealing, worktree input bytes were also rechecked against the frozen manifest.

No TeX, PDF, or manuscript source was changed or created. The assigned deliverable is a Markdown audit, so no LaTeX build was required. No commit, push, install, external search, canonical edit, or child agent occurred. Root alone integrates; the reviewer stops after the sealed handoff.
