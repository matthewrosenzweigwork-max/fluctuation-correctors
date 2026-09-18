# AUD075 — whole THM052 isolated reconstruction packet

Verdict: all frozen clauses reconstructed. Read ROUND_027_DUALITY_RECONSTRUCTION.md first. This packet supplies the independent reconstruction axis; root owns comparison, promotion and integration. No critical modal decay or witness is proved.

Contents include all eight exact inputs, the complete mathematical report, source/read/exposure and execution history, 322 fresh exact rational diagnostic checks, nine nonzero semantic mutation runs, nine nonzero in-memory verifier guard mutation runs, and a portable read-only verifier. No outside library is required.

With this directory and its named sibling archive, complete inventory, checksum manifest, outer seal and assigned report present, run:

    python3 -B verify.py
    python3 -B verify.py --run-diagnostics

Both commands are read-only. The first hashes and validates all material and checks the archive without extracting it. The second also reruns the baseline and nine semantic mutants, requiring byte-identical outputs and the recorded return codes. To validate just an extracted packet without its sibling seals, use:

    python3 -B verify.py --payload-only

That mode explicitly reports PASS_PAYLOAD_ONLY and does not claim verification of unavailable outer seals or archive bytes. If an extraction utility changes permission bits, restore read-only permissions deliberately before using the verifier; it checks that packet members have no write bit. No verifier option silently changes permissions.

PAYLOAD_INVENTORY.json and PAYLOAD_SHA256SUMS.txt enumerate and hash every payload file except those two self-sealing files. Their exclusion is explicit and avoids circular self-hashes. The complete sibling INVENTORY.json enumerates and hashes every regular file in the packet, including those two internal seals and the verifier itself. The sibling SHA256SUMS.txt covers every packet file, the complete inventory, the archive and the separately assigned report. The sibling SEAL.json hashes that checksum manifest and the other named sibling objects. As usual, the outer seal does not contain its own hash. The final read-only verifier result is a separately named sibling, with its own checksum, because a result cannot be inserted into the archive whose digest it reports without circularity.

The archive contains only safe ordinary regular-file members under this packet's single top-level directory: no symlinks, hardlinks, devices, extraction or unsafe paths. It contains every packet file, including the report, inputs, all results, verifier and internal manifests. The separate complete inventory covers its exact member set and bytes. Reproducible gzip/tar metadata are fixed, and write permission bits are absent at issuance.

Diagnostics use exact fractions and exhaustive finite signals. Their solvable interval model and local rational energy jets are tests of the proof's vulnerable mechanisms, not simulations or proofs of the singular Coulomb theorem. The continuum theorem is proved in the report. The guard mutations are synthetic in-memory corruptions, with recorded nonzero exits, and do not alter the final package. No references, model configuration claims, or mathematical claims are inferred from code success alone.

The immutable original-source boundary is recorded in SOURCE_EXPOSURE_HISTORY.md. Never edit an issued audit report or packet. Corrections must be separately named superseding artifacts.
