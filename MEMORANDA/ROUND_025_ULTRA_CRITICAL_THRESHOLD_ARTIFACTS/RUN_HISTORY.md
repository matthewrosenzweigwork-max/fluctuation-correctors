# Reproducibility and run history

1. Read the TASK107 card and its exact manifest in the assigned worktree.
2. `shasum -a 256 -c AUDITS/ROUND_025_CRITICAL_THRESHOLD_ULTRA_INPUT_SHA256SUMS.txt`
   passed all 26 inputs before substantive mathematical reading.
3. Read only permitted files as detailed in EXPOSURE_AND_SOURCES.md.
   Several combined outputs were truncated; relevant proofs were recovered
   in explicit bounded reads and reconstructed in the memorandum.
4. `git rev-parse --show-toplevel HEAD` confirmed the assigned worktree and
   base 3efdbb96e7b94529b280234e83eb36f5fca3ef36.
   `python3 --version` returned Python 3.9.6. No environment modification.
5. Created the new proof, claim card and fresh diagnostic without opening
   previous diagnostic code. Ran from the assigned worktree:

       python3 MEMORANDA/ROUND_025_ULTRA_CRITICAL_THRESHOLD_ARTIFACTS/round025_tail_diagnostic.py --write-result MEMORANDA/ROUND_025_ULTRA_CRITICAL_THRESHOLD_ARTIFACTS/DIAGNOSTIC_RESULT.json

   Outcome: PASS, 19,132 assertions, 32 categories, 12 distinct nonvacuous
   mutation types. The result stores exact witnesses, all finite cases,
   radial outputs, precision/tolerance, and the script digest.
6. Reconstructed the whole original-law covariance criterion and wrote its
   exact relation to the new tail lemma. The original cancellation remains
   OPEN. This is same-context self-check, not independent certification.
7. Copied all 26 verified source bytes into INPUTS and preserved the input
   manifest verbatim. Issuance generates input/payload inventories, a
   regular-member-only archive and complete external member/byte seal.
8. The final read-only verifier is run after sealing, including its
   in-memory malformed-member and digest controls and the read-only fresh
   diagnostic rerun. Its machine-readable stdout is the verification
   outcome; no post-issuance edits are permitted. The README gives the
   exact reproducible command.

No TeX file was created or changed; no compilation was required. The final
handoff prose uses no mathematical LaTeX. Mathematical proof is in the
Markdown memorandum and its byte-identical packet copy. This packet has
no external bibliographic dependency or unverified external reference.
