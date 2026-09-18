# Round026 actual-correlation falsification packet

Status: new bounded cancellation, SELF-CHECKED only. THM046 and the full
critical signed-correlation target remain open. No admitted counterexample
or independent certification is claimed.

Read REPORT.md for the complete proof and exact remaining triple-label
integral; CLAIM_CARD.md freezes the whole new assertion and negation.
The two-label current and current/initial overlaps vanish quantitatively
under the original actual iid-Haar dynamics. The proof uses an actual
current-pair small-ball estimate, logarithmic truncated-source square,
and exact Fourier overlap self subtraction.

INPUTS/ contains all 17 complete allowlisted source copies at their exact
original bytes. INPUT_SHA256SUMS.txt is the original manifest, and
INPUT_INVENTORY.json records all 17 sizes and hashes. The precise displayed
reading and isolation boundaries are in EXPOSURE_AND_SOURCES.md.

The new diagnostic.py and DIAGNOSTIC_RESULT.json contain the finite exact
Fourier/radial checks, nonzero mutation witnesses and a labeled floating
heat-envelope sweep. RUN_HISTORY.md records all runs, including the
read-only harness failure preserved in CHECK_ONLY_FAILURE.md and
`diagnostic_check_only_initial_failed.py`. The latter is historical evidence
and must not be used as the active checker.

Keep this directory beside the named archive, member inventory, seals,
verification record and main memorandum. From any location, using an
existing Python 3 standard library:

```
python3 /path/to/ROUND_026_CORRELATION_FALSIFICATION_ARTIFACTS/verify_packet.py
python3 /path/to/ROUND_026_CORRELATION_FALSIFICATION_ARTIFACTS/diagnostic.py --check-only
```

Both commands are read-only. build_packet.py records the one-time
pre-issuance packaging method; it refuses to overwrite an existing sibling
packet and should not be rerun against issued evidence. The verifier checks exact source copies,
all payload digests, safe unique regular archive members, every archived
member digest against the sibling inventory, exact local/archive equality,
report equality, sibling seals and final read-only permissions. It never
extracts or executes an archive member. The diagnostic rerun is separate
from package integrity and does not certify the mathematical proof.

The sibling archive is ROUND_026_CORRELATION_FALSIFICATION_ARTIFACTS.tar.gz.
The sibling MEMBERS.json is the complete size/digest inventory of every
archive member, including internal inventory/manifest files. The sibling
SHA256SUMS.txt seals the archive, complete member inventory, final report,
and verification record. Internal FILE_INVENTORY.json covers every payload
file except itself and PAYLOAD_SHA256SUMS.txt; the latter seals those same
payload files plus FILE_INVENTORY.json. These intentionally noncircular
internal lists are completed by the external all-member inventory and
archive seal. All archive members are safe, unique, relative regular files.

The report and issued packet files/archive/seals are read-only. Do not edit
issued evidence; any correction needs a separately named artifact. No
canonical state or input was edited and no commit/push was made. Root
owns integration, fresh audit, and the remaining mathematical gate.
