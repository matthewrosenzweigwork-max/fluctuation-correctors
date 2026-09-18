# TASK104 issued source and derivation packet

The authoritative new mathematical artifact is the sibling ROUND_024_COULOMB_TRACE_SOURCE_AUDIT.md. It proves the genuine lower-contraction consequence in the actual critical four-dimensional Coulomb row from the admitted sources, using a spherical-average trace and actual-law Fourier concentration. It leaves THM046 source cancellation, cubic control and genuine noise control open.

Status: new derivation self-checked; ordinary distinct source/derivation lane, not an independent theorem audit. Root owns any promotion and canonical integration.

Contents:

- INPUTS/ and INPUT_SHA256SUMS.txt: exact twenty-file frozen dossier.
- SOURCE_INDEX.md and EXPOSURE.md: exact source use, qualifications and exposure.
- exact_diagnostic.py and RESULTS.json: fresh exact rational supporting checks and detecting mutations.
- verify_packet.py: safe read-only byte/member verifier, with no archive extraction.
- verifier_negative_checks.py and VERIFIER_NEGATIVE_RESULTS.json: in-memory malicious-member and byte mutation rejection tests.
- VERIFICATION.md: executed commands, outcomes, failures and limitations.
- BUNDLE_SHA256SUMS.txt: report and all packet file hashes, excluding only itself.
- Sibling archive and SEAL.md: exact archive and manifest anchors.

From the worktree root, rerun:

    python3 MEMORANDA/ROUND_024_COULOMB_TRACE_AUDIT_ARTIFACTS/exact_diagnostic.py
    python3 MEMORANDA/ROUND_024_COULOMB_TRACE_AUDIT_ARTIFACTS/verifier_negative_checks.py
    python3 MEMORANDA/ROUND_024_COULOMB_TRACE_AUDIT_ARTIFACTS/verify_packet.py --archive MEMORANDA/ROUND_024_COULOMB_TRACE_AUDIT_ARTIFACTS.tar.gz --require-read-only

For a safely extracted standalone packet, the byte/member verifier works with --root pointing to the extraction root. The mathematics checker reads the copied source manifest as a fallback if original worktree paths are absent. Compare the external seal before trusting a copied manifest. The verifier never extracts archive contents.

No TeX was created or modified, and no dependency was installed. Issued files and the archive are read-only. Corrections must use a new superseding artifact, preserving this packet.
