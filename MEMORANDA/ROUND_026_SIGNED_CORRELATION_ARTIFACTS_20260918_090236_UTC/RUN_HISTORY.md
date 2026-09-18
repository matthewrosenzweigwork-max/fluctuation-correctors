# Complete run and issuance history

Python version observed: 3.9.6. Standard library only. No installations,
random sampling, SDE discretization, children, or external sources.
Observed Git branch: codex/hocf-r026-signed-correlation; observed HEAD:
06bf56dae256085646228aa28159210b567bf409. Git reads were root, HEAD,
branch name, and status only; no history. All supplied source paths
remained unchanged and untracked where initially untracked.

## Source verification

The exact command `shasum -a 256 -c
AUDITS/ROUND_026_SIGNED_CORRELATION_INPUT_SHA256SUMS.txt` returned 0 with
all 17 rows OK before mathematics. Copy construction recomputed every
source digest and verified exactly 17 rows. The same checksum command
returned 0 again after the mathematical report was complete; its full
output is RESULTS/INPUT_RECHECK.txt.

## Mathematical diagnostic

Executed from this packet directory:

`python3 scripts/diagnostic.py > RESULTS/DIAGNOSTIC_RESULT.json`

Result: exit 0, PASS, 1,588 assertions in 33 categories, zero failures.

The six commands obtained by appending `--mutate NAME`, with output in
RESULTS/FAIL_CONTROL_NAME.json, all returned exit 1 as required:

| NAME | Failed assertions | First concrete discrepancy |
|---|---:|---|
| pair_drift | 93 | Relative drift 1 rather than 2 at N=2. |
| diffusion | 930 | Relative Brownian variance 2/7 rather than 4/7. |
| projection | 1 | Angular moment 1/24 rather than 1/16. |
| cross_bracket | 20 | Removed terminal/noise covariance 0 rather than 11/9. |
| omit_bias | 20 | Defect 11/9 rather than 4/3 after omitting conditional bias. |
| radial_power | 1 | Radial power -2 rather than -1. |

Every failed control output is preserved in full. No baseline diagnostic
failed; the nonzero runs are deliberate mutation witnesses. Numerical
cosine series and radial ODE tests are supporting calculations, not a
positive-noise continuum proof. Exact conventions and floating tolerances
are included in the script and every diagnostic result.

## Byte verifier and negative controls

A provisional directory verification using
`python3 scripts/verify_packet.py . --allow-writable` returned 0 and
PASS for 36 then-existing files, including all 17 source copies and 35
hashed payload members. A subsequent code review made relative packet
arguments resolve to their actual directory name for archive checking;
this is a packaging fix, not a mathematical change.

The following two controls returned 1, with their complete outputs
preserved:

- `python3 scripts/verify_packet.py . --allow-writable --negative-control digest`
  rejected an intentionally altered expected digest for CLAIM_CARD.md.
- `python3 scripts/verify_packet.py . --allow-writable --negative-control unsafe-member`
  rejected the unsafe relative path ../escape before any extraction.

The verifier never writes or extracts. Control JSON files were filled
before the final member inventory and payload digests were generated.
The final source-recheck output increased the final inventory by one
file. Two attempted metadata-only patches failed to match their context
and changed no file; the intended diagnostic-count sentence was then
applied with the exact observed context. No mathematical statement or
frozen claim changed in that operation.

## Parent exposure and claim freeze

After the candidate angular-trace proof was complete, root raised the
specific concern that a W1,4 conclusion needs a positive-volume
neighborhood in center/other-coordinate variables, not a single slice.
This was based only on this worker's provisional progress message, not
another route. The completed report already states and proves uniformity
on a compact separated positive-volume Q, uniformity over the sphere,
and the subsequent dq/dr integration. That was explicitly confirmed to
root. This interaction is not independent certification.

Root next asked to freeze the complete claim before preparing a separate
statement-only reconstruction. This worker confirmed the final
CLAIM_CARD.md SHA-256:
89af030e94ad850fca9191f2516421760d1667a75ec8ef93125c306a781f9775.
The final packaging process asserts this same hash. No mathematical
change to that frozen claim occurred thereafter. No new audit output
or another worker's route was disclosed or read.

## Final issuance procedure

The final inventory includes every packet regular file, including
MEMBERS.txt and PAYLOAD_SHA256SUMS.txt. The latter hashes every other
packet file, so there is no self-hash cycle. The external packet seal
hashes the final payload manifest, inventory, report, and frozen claim.
The archive contains exactly the same safe relative regular files,
with no directory, symbolic-link, hard-link, or duplicate members.

Final packet files and memorandum are changed to mode 0444; packet
directories are 0555. The archive and sibling seals are 0444. The final
packaging process runs the read-only verifier against directory plus
archive and records its actual successful JSON result in the external
PACKET_SEAL.json before a final seal-aware verification. A failure would
abort issuance. The seal contains the exact final member count and
archive digest; this record does not invent those values before the
byte check runs.

No TeX source was created, so no LaTeX build or PDF visual certification
is claimed. The mathematical deliverable is Markdown. The sole remaining
scientific issue is the actual L2 conditional-response control in REPORT
(7.1); the original critical signed-correlation target remains open.
