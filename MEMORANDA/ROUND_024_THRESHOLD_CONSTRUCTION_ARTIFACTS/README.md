# Round024 threshold construction packet

TASK-102, frozen THM-046 / PO-033. Status: **SELF_CHECKED EXACT REDUCTION;
full target remains OPEN**. The report is `REPORT.md`, byte-identical to
`MEMORANDA/ROUND_024_THRESHOLD_DYNAMIC_CONSTRUCTION.md` at issuance.

The new result removes the complete scaled lower drift at four-dimensional
Coulomb using a spherical-average flux identity, translation covariance,
and actual weak concentration. The remaining statement is report equation
(7.5), the actual integrated cubic term plus the retained singular part of
the corrector martingale. No static-law counterexample, signed-mean
substitution, or extension of the strict sub-Coulomb occupation theorem is
claimed.

The packet contains exactly twenty frozen input copies. Consult
`SOURCE_PREFLIGHT.md` for uses and limitations and `EXPOSURE.md` for what the
constructor actually saw. `INPUT_SHA256SUMS.txt` is the exact original
twenty-entry manifest; its paths are relative to `inputs/` in this packet.

`exact_diagnostic.py` is new standard-library code. Its 1,446 assertions
include exact finite-label Fourier algebra, Coulomb flux and compensation,
endpoint moments, generator brackets, actual initial-mode signs, exponent
checks, and a smooth limiting Fourier ODE. All fifteen mathematical mutation
categories have nonzero detecting witnesses. The ODE has an explicitly
recorded tolerance and 50-digit arithmetic; the other algebra is rational.
These checks are supporting evidence, not an independent mathematical audit.

Run the diagnostic without changing issued files:

```text
python3 exact_diagnostic.py --check
```

Run the separate read-only verifier on the sibling issued archive and seal:

```text
python3 verify_packet.py --archive /absolute/path/to/issued.zip --seal /absolute/path/to/issued.seal.json --self-test --rerun-diagnostic
```

When checking from the original worktree, add `--source-root` with its
absolute path to verify every still-frozen original input and the external
report. The verifier does not extract the archive. It checks safe regular
member paths, exact closed membership, CRC, every byte digest, original
input copies, diagnostic freshness, all mutation categories, and the seal.
Its six separate in-memory archive mutations must all be rejected.

`OUTPUT_SHA256SUMS.txt` hashes every payload file except itself and the
inventory. `ARCHIVE_INVENTORY.json` lists every member except its own entry
with byte size and digest; its own member name is explicitly declared.
The sibling seal hashes the archive, inventory, output manifest, and report.
This avoids circular self-hashing while retaining exact archive membership.

All issued files and copied inputs are read-only. Any correction requires
a new superseding report and packet. Root owns canonical state, identifiers,
integration, and fresh audit assignment. No commit or push was made here.

The exact next mathematical action is report equation (7.5); the immediate
review target is the new flux/translation lemma and its use of actual weak
concentration. The theorem is not marked complete by this handoff.
