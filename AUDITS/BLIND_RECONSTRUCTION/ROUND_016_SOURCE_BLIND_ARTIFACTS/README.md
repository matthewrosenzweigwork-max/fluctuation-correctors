# AUD051 / TASK080 sealed blind reconstruction

The complete frozen THM038 claim is reconstructed in `ROUND_016_SOURCE_EXTENSION_RECONSTRUCTION.md`: genuine actual-law source integrability and its uniform raw bound over the full stated sub-Coulomb/Coulomb range, including zero noise and arbitrary fixed smooth terminal tests. The quantitative scaled consequence retains the strict decay threshold; the equality case is only bounded. No excluded fluctuation, inverse, domain, or hierarchy statement is promoted.

This context received no construction candidate or proposed mechanism. It read the task and manifest first, created the prescribed isolated worktree at published R13, and verified exactly nine frozen inputs. Earlier source labels were not treated as certificates; the mathematical ingredients needed here were rechecked in the report. The report and all diagnostics were sealed before comparison. Canonical comparison and promotion belong to the root. The independent reconstruction's own diagnostic checks are self-checks, not independent certification of its new proof.

Contents:

- `ROUND_016_SOURCE_EXTENSION_RECONSTRUCTION.md`: complete proof, negation, source preflight, all dispositions, falsification route, and limitations.
- `EXPOSURE.md`: full isolation and ambient-exposure record.
- `inputs/`: byte-exact snapshots of the nine allowed inputs.
- `INPUT_SHA256SUMS.txt` and `INPUT_MANIFEST_SHA256.txt`: the frozen input list and its original digest.
- `round016_source_blind_exact.py` and its results JSON: independently written Gaussian-rational diagnostics; PASS, 2,018 assertions.
- `verify_packet.py`: exact output and safe ZIP member/byte verification.
- `BUILD_CONTEXT.json`: worktree, branch, base commit, and UTC timestamp.
- `OUTPUT_SHA256SUMS.txt`: every payload file except the checksum file itself.

The final archive, its SHA-256 file, and the external seal verification JSON are adjacent to this directory. The report also exists at the prescribed parent-directory path; the seal verifies that the two report copies are identical. ZIP member contents are checked byte-for-byte against every intended output and exact member names, with no extra, unsafe, duplicate, directory, or symlink entries. The archive hash is external to avoid a circular self-hash. Issued files are read-only and must be superseded, never modified in place.

Run the exact diagnostics without changing issued files:

```text
python3 round016_source_blind_exact.py --check-only
```

Verify the extracted packet, optionally supplying its adjacent archive:

```text
python3 verify_packet.py
python3 verify_packet.py --archive /absolute/path/to/the/sealed.zip
```

The diagnostic uses only the Python standard library, exact integers and fractions, and no random seed, numeric tolerance, prior checker, or external lookup. Its physical derivative convention and precise limitations are recorded in its source and results. No TeX source, canonical ledger, canonical memorandum, commit, push, installation, or child-agent action belongs to this handoff.

Next action: the root verifies the seal, compares this reconstruction with the separately sealed construction, and runs the separate hostile gate. This bounded context stops after its sealed handoff.
