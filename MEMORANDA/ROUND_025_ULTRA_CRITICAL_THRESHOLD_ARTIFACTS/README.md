# Round 025 critical threshold Ultra construction packet

TASK107, base 3efdbb96e7b94529b280234e83eb36f5fca3ef36.
SELF-CHECKED construction; independent promotion is pending.

REPORT.md is byte-identical to the assigned sibling memorandum. It proves
a new candidate squared-tail estimate and L1/L2 equivalence for the exact
critical iid-Haar integrated Coulomb source. It reconstructs the exact
remaining signed correlation gate. THM046 remains OPEN; no admitted
counterexample or full limiting law is claimed. CLAIM_CARD.md gives the
whole conjunction and exact negation for fresh review.

Contents:

- REPORT.md: complete proof, exact target, source preflight, tests, remaining line.
- CLAIM_CARD.md: precise bounded claim and negation.
- EXPOSURE_AND_SOURCES.md: every permitted read and status-only parent exposure.
- INPUTS/: all 26 complete permitted source byte strings.
- INPUT_SHA256SUMS.txt and INPUT_INVENTORY.json: exact allowlist and input bytes.
- round025_tail_diagnostic.py and DIAGNOSTIC_RESULT.json: new exact finite
  tests, radial-tail calculation, concrete mutation witnesses and reproducibility limits.
- RUN_HISTORY.md: commands and executed diagnostic outcome.
- verify_packet.py: portable read-only verifier with nonvacuous corruption controls.
- PAYLOAD_SHA256SUMS.txt and PAYLOAD_INVENTORY.json: all payload files except
  those two self-descriptive inventory files, listed explicitly.

The sibling archive is ROUND_025_ULTRA_CRITICAL_THRESHOLD_ARTIFACTS.tar.gz.
The sibling ROUND_025_ULTRA_CRITICAL_THRESHOLD_ARTIFACTS.SEAL.json contains
its byte digest and the complete exact archive-member inventory, including
the two inventory files. Thus there is no unlisted self-reference exception
in the external member seal. Every archive member is a unique safe
relative regular file. The packet, memorandum, archive and seal are
issued read-only; hashes detect any later alteration. This is a byte
integrity seal, not a digital authorship signature or mathematical audit.

Run after unpacking beside the archive and seal, or in the original worktree:

    python3 MEMORANDA/ROUND_025_ULTRA_CRITICAL_THRESHOLD_ARTIFACTS/verify_packet.py --run-diagnostic --source-root .

The optional --source-root checks exactly the original 26 allowlisted
paths against their input digests; omit it for a standalone handoff.
Options --packet, --archive and --seal accept moved locations. The
verifier does not extract archives, modify files, install packages or
write bytecode/results. The default diagnostic also only prints output;
its --write-result option was used before sealing to produce the included
result and must not be used to overwrite issued files.

Python >=3.9 standard library suffices. Exact coefficient tests have no
random seed or tolerance. The separately labeled radial quadrature uses
20,000 Simpson subintervals in the logarithmic radial coordinate and
2e-10 times max(1,absolute expression) tolerance; its formulas are proved
analytically in REPORT.md. These tests are not singular particle
simulations or independent proof certification.

Next action: fresh whole-claim reconstruction and hostile review of the
new tail lemma and equivalence. If accepted, the sole remaining dynamic
line of this route is REPORT.md (8.7), now equivalent to the full original
L1 assertion. Root alone owns canonical integration and identifier assignment.
