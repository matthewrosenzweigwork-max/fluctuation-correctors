# Round024 threshold falsification packet

The authoritative report is the sibling ROUND_024_THRESHOLD_DYNAMIC_FALSIFICATION.md. THM046 remains open. The packet supplies an exact actual-law two-time/BBGKY reduction and disproves two specific closure shortcuts; it does not prove an admitted counterexample or the critical source assertion.

Contents:

- INPUTS: all 20 exact permitted source byte strings.
- INPUT_SHA256SUMS.txt and INPUT_INVENTORY.json: original allowlist and verified byte inventory.
- EXPOSURE_AND_SOURCES.md: complete source-reading and context boundary.
- round024_independent_diagnostic.py and DIAGNOSTIC_RESULT.json: new exact smooth/Fourier diagnostic, 2,434 passing assertions, 40 categories, and 16 concrete nonvacuous mutation types.
- verify_packet.py and VERIFIER_SELF_TEST_RESULT.json: safe archive/member/byte checks and adversarial in-memory verifier tests.
- OUTPUT_MANIFEST.json: exact payload membership, sizes and SHA-256 values. It excludes only itself to avoid a self-hash cycle; its own hash is pinned by the sibling seal.

The sibling ZIP contains this memorandum and all packet files, with exact relative paths and regular-file read-only attributes. The sibling seal pins archive bytes, manifest bytes, original input-manifest bytes, base, and member count. Hashes provide byte consistency relative to that external seal; they are not a cryptographic signature or mathematical certification.

Reproduce the diagnostic in a writable copy:

    python3 MEMORANDA/ROUND_024_THRESHOLD_FALSIFICATION_ARTIFACTS/round024_independent_diagnostic.py

It regenerates DIAGNOSTIC_RESULT.json, so do not run that writing command against the issued read-only packet.

Verify an issued archive without extracting any member:

    python3 MEMORANDA/ROUND_024_THRESHOLD_FALSIFICATION_ARTIFACTS/verify_packet.py --seal MEMORANDA/ROUND_024_THRESHOLD_FALSIFICATION_PACKET_20260918_082248_UTC.seal.json --workspace .

The verifier rejects duplicate, unsafe, absolute, traversal, noncanonical, encrypted, nonregular, writable or unexpected members; checks exact member inventory, sizes, hashes, all 20 frozen input copies, and the pinned archive/manifest; and, with --workspace, checks the corresponding on-disk read-only bytes and directories. It does not trust ZIP paths for extraction and does not extract files. It also refuses oversized payloads.

Read-only issuance is a local preservation convention, not a substitute for fresh whole independent mathematical review. Corrections require a separately named issuance.
