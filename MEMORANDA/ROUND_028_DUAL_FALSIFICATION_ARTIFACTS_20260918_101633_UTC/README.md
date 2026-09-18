# TASK120 quantitative collision-profile packet

Status: SELF_CHECKED ordinary construction, not an independent certificate.
The original critical source target remains OPEN. No admitted counterexample
is claimed.

REPORT.md is byte-identical to the named memorandum
ROUND_028_DUAL_ACTUAL_FALSIFICATION.md. Its principal new result is the
explicit finite-N bound for the Fourier-mode change from a fixed survivor
horizon to the same path's later first collision, and the quantitative
norm comparison with the exponentially weighted first-collision profile.
The exact unresolved inequality is report equation (6.7). The initial/
collision correlations and the full rare-survival normalizer remain.

Contents:

- REPORT.md: complete proof, all attempted routes/failures, explicit
  source qualifications, finite-N constants, martingale and cutoff
  passages, original-target equivalence, and remaining gap.
- INPUTS/: all 17 exact frozen input files, preserving their relative paths.
- INPUT_SHA256SUMS.txt: complete original input manifest.
- EXPOSURE_AND_SOURCES.md: full reading/exposure and dependency record.
- RUN_HISTORY.md: actual commands, outcomes and failure/correction history.
- diagnostic.py and DIAGNOSTIC_RESULT.json: fresh deterministic exact
  support checks, 3,845 assertions in 41 categories and 20 nonzero
  mutation witnesses, with all examples and limitations.
- verify_readonly.py: portable Python standard-library verifier.
- INVENTORY.json: complete payload paths, sizes and SHA-256 digests.
- OUTPUT_SHA256SUMS.txt: every payload digest and the inventory digest;
  the manifest does not purport to hash itself.

Named siblings use this packet directory's name as prefix:

- .tar.gz: complete safe regular-member archive of this packet.
- _ARCHIVE_INVENTORY.json: every archive regular member, byte size and digest.
- _VERIFICATION.json: recorded full verification after immutable issuance.
- _SEAL.json: final sibling sizes/digests and packet-manifest digest.
- _SEAL.sha256: digest of that outer seal.

The outer seal also hashes the original memorandum. The seal/hash pair
avoids a self-referential manifest; the final verification receipt is
outside the already immutable archive and is itself sealed. All issued
regular files are read-only. Corrections must use a distinct issuance.

Portable verification, from any directory, uses only Python 3 standard
library. Invoke verify_readonly.py with --replay to verify the packet and
reproduce the exact full diagnostic JSON. To verify the issued siblings,
also supply --archive with the sibling .tar.gz, --report with the original
memorandum, --outer-seal with the sibling _SEAL.json, and
--require-readonly. No extraction, install, source edit, network, current
repository state or other task output is needed. When examining an
extracted copy whose filesystem modes changed in transit, omit only
--require-readonly; all byte/inventory/safe-member checks remain.

The verifier rejects unsafe or duplicate archive members, links and
nonregular members, extra or missing packet files, incorrect byte
digests, mismatched source copies, changed diagnostic results, and
unsafe metadata. Its safety checks include 15 in-memory nonzero
rejections. It performs no file writes.

No TeX source was edited or compiled. No source/canonical state was
modified, no child spawned, no dependency installed, and no Git/remote
mutation occurred. Root alone owns integration and the full two-axis audit.
