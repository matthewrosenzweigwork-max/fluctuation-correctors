# Execution, correction and failure history

1. Read TASK120 and its exact manifest first in the assigned worktree.
2. Executed shasum -a 256 -c on that manifest: all 17 entries passed.
3. Observed the assigned worktree root and base ef438b612f732d21af1fa1756dd7559ef63c6d61.
   The only pre-existing untracked items were supplied task/manifest/R27/THM052 inputs.
4. Read all 17 exact inputs. One combined display was truncated by the tool
   wrapper; explicit range rereads recovered all text, as recorded in
   EXPOSURE_AND_SOURCES.md. This display failure did not change any file.
5. Independently derived the collision endpoint/flux identity. Reported
   it to root, then derived the canonical iid clipping bound and the
   stopped mode estimate through collision. Root later noted status-only
   overlap in unmarked flux; no other workstream was read.
6. Created the unique packet at 20260918_101633_UTC and copied all 17
   inputs and the original manifest. Every copied digest matched.
7. Wrote the complete mathematical memorandum. Its failed proof/falsification
   routes are preserved in Section 8; no actual critical witness was found.
8. Wrote diagnostic.py from scratch, with exact Fraction/Gaussian-rational
   arithmetic and no external imports. The first execution succeeded:
   3,845 assertions in 41 categories, including 20 nonzero mutation
   witnesses. DIAGNOSTIC_RESULT.json is the complete unedited stdout.
   There was no diagnostic-code failure, rerun repair or suppressed test.
9. Added the exact diagnostic outcome to the memorandum before sealing.
   This was an administrative result update, not a mathematical repair.
10. Prepared the read-only verifier, full payload inventory, file manifest,
    packet/report byte match and sibling archive. The final recorded
    verification is the named sibling VERIFICATION.json; it includes
    exact replay of the diagnostic, all copied inputs, every archive
    regular member, byte digests, safety checks and read-only modes.

Python observed: 3.9.6 (Clang 21.0.0). Standard library only.
No random sampling, tolerance-based numerical test, SDE simulation,
dependency installation, TeX source/build, canonical edit or Git mutation.
The local radial zero-noise calculation is an explicitly excluded diagnostic
model, not an admitted critical counterexample.

Pre-seal verifier execution: PASS, all 17 inputs, 25 payload/27 total
regular files, exact diagnostic replay (3,845 checks, 41 categories,
20 nonzero mutations), report byte match and 15 safety rejections.
No verifier failure or code repair occurred before issuance.
