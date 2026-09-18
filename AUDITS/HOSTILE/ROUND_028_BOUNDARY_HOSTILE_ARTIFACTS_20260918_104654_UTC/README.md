# AUD078 portable hostile-review packet

Final mathematical verdicts: **THM053(A)–(B) whole HOSTILE_REVIEW_PASS** and
**THM055(A)–(E) whole HOSTILE_REVIEW_PASS**, with no frozen claim or constructor
repair. These are this hostile axis's verdicts. Root separately compares the
blind axis and verifies constructor execution/source-gate matching.
The original critical source THM046/PO033 remains OPEN.

Read `REVIEW.md` for the complete analytic audit. It checks every frozen clause,
the entire 397-line flux constructor, and the entire hash-matching 706-line
quantitative constructor. The dispatch's 705-line figure is administrative.
All 21 frozen inputs are under `INPUTS/` with exact relative paths; the original
manifest, preflight, final original-input recheck and precise reading/exposure
record distinguish full reading from selected older-source ranges.

The fresh diagnostic passed **16,732 assertions in 39 categories**, including
**27 nonzero deliberate mathematical mutation witnesses**. Most arithmetic is
exact rational or Gaussian-rational; the few evaluations of analytic logarithms
are explicitly labeled numerical. No random sampling, external dependency or
singular SDE simulation is used. Diagnostics support coefficients and expose
invalid inferences; they do not replace the analytic proof.

`RUNS/diagnostic_001.*` contains the exact executed source, full stdout/stderr,
command, runtime timestamp and exit code. That execution succeeded. The
wrapper initially yielded before displaying its stdout; the saved completion
was then read. The other display issue was a truncated combined constructor
read, recovered completely by bounded rereads. All failures/shortcuts and
operations are recorded. No failed diagnostic execution is omitted.

Before sealing, root observed that this worker's draft needed an N>=3 qualifier
on its ancillary I/Z nonindependence sentence. At N=2 the mark is constant.
The exact unissued earlier draft is retained under `DRAFT_HISTORY/` solely as
disclosed history. It is not the authoritative report. This feedback did not
change either frozen theorem, either constructor or either whole verdict.

## Read-only verification

Python 3.9 or newer suffices. There is no dependency installation. From any
location, running the packet's `verify.py` with `-B` verifies its exact file
set and hashes, all 21 copied inputs, read-only modes, malformed-name rejection
and a fresh diagnostic rerun. It writes nothing and never extracts an archive.

For complete sibling verification, place the packet beside its named siblings
and run this command from that parent directory:

```sh
python3 -B ROUND_028_BOUNDARY_HOSTILE_ARTIFACTS_20260918_104654_UTC/verify.py \
  --archive ROUND_028_BOUNDARY_HOSTILE_ARTIFACTS_20260918_104654_UTC.tar.gz \
  --inventory ROUND_028_BOUNDARY_HOSTILE_ARTIFACTS_20260918_104654_UTC.ARCHIVE_MEMBERS.json \
  --seal ROUND_028_BOUNDARY_HOSTILE_ARTIFACTS_20260918_104654_UTC.SEAL.json \
  --report ROUND_028_JOINT_BOUNDARY_REVIEW.md \
  --sha256sums ROUND_028_BOUNDARY_HOSTILE_ARTIFACTS_20260918_104654_UTC.SHA256SUMS
```

`CONTENT_MANIFEST.json` lists every packet file except itself. The verifier
requires exactly that set plus the manifest, so no unlisted regular member,
symlink or special file is accepted. The external archive-member inventory
includes every regular file, including the content manifest. The archive has
only unique safe relative regular members beneath this packet's name; no
directory, link or special tar member is included. The archive is compared
byte-for-byte by each member's size and SHA-256 without extracting it.

The external seal records the actual pre-seal verification command/output,
original-input postflight, exact archive/report/manifest digests, counts and
whole verdicts. The sibling SHA256SUMS covers the archive, member inventory,
seal and main report. The final-verification sibling records the actual full
post-seal command, stdout/stderr and exit status. These external records avoid
circular payload hashes. Their exact final counts and digests are authoritative.

Every issued file is read-only and every packet directory is nonwritable.
The packet can be verified in place or copied together with its siblings;
verification requires no Git repository, original worktree, chat, network,
memory, private input, or other current audit. A later correction must be a
distinct issuance. No commit, push, remote operation, installation, child,
canonical edit or TeX operation was performed.
