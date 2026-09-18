# TASK-071 sealed statement-only reconstruction

Issued 2026-09-18 UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r013-noise-blind`. Branch: `codex/hocf-r013-noise-blind`. Published R9 base: `29d7ce427ad7a98739b18d07781e71c4598b3579`.

Verdict: **CONDITIONAL RECONSTRUCTION PASS for every frozen THM-034 conclusion**, including the full bounded-diffusivity supremum and its stated quantitative bound. Every earlier particle/inverse/domain/clipping prerequisite remains conditional as issued. No candidate proof or root seed was inspected, and no comparison occurred before sealing. Root alone compares or promotes.

The mathematical report is the sibling file `../ROUND_013_BOUNDED_NOISE_RECONSTRUCTION.md`. Its source/normalization preflight is Section 2, the new uniform derivative construction is Sections 3–4, the actual singular expectation passage is Section 5, and the full-interval closure is Sections 6–8. Sections 9–10 record falsification checks, exact scope, conditional dependencies, and handoff.

The fresh exact checker passed **2,513 assertions**. It uses Python standard-library rational arithmetic without randomness or numerical tolerances. It tests literal deleted-label derivatives, all four law contractions under Haar and a positive nonproduct diagnostic density, the physical generator product identity, Fourier self-diagonal subtraction, both compensated response slots, one-sided radial Jacobian coefficients, weight Laplacians, uniform rate identities, and failures of the particular mechanism at excluded endpoints. It does not certify the singular analytical premises or simulate the actual limiting law.

Files in this output packet:

- `../ROUND_013_BOUNDED_NOISE_RECONSTRUCTION.md`: complete conditional reconstruction.
- `round013_noise_blind_exact.py` and `EXACT_RESULT.json`: fresh exact diagnostics and recorded result.
- `INPUT_SHA256SUMS.txt` and `INPUT_VERIFICATION.json`: the 27-input allowed dossier and before-reading copy verification.
- `EXPOSURE.md`: full isolation and ambient-exposure record.
- `README.md`: this handoff.
- `seal_packet.py`: fresh archive/manifest construction and member-by-member verification program.
- `OUTPUT_SHA256SUMS.txt`: output digests, excluding the manifest itself and subsequent package records.
- `ROUND_013_NOISE_BLIND_SEALED.zip`: precisely the 27 inputs, the listed pre-seal outputs, and the output manifest.
- `PACKET_VERIFICATION.json`: post-creation input/output/archive verification record.
- `FINAL_SHA256SUMS.txt`: hashes of the archive, output manifest, and post-creation verification record.

Reproduce the checker in a separate extracted working copy from its worktree root:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_013_NOISE_BLIND_ARTIFACTS/round013_noise_blind_exact.py
```

The original checker result and proof are issued immutable artifacts; do not rerun a result-writing command in this sealed directory. Standard SHA-256 verification from the worktree root can check `INPUT_SHA256SUMS.txt`, `OUTPUT_SHA256SUMS.txt`, and `FINAL_SHA256SUMS.txt`; all recorded paths are relative to that root. The archive contains no inherited non-allowlisted file and no canonical state/history. Its member CRCs and every member digest were checked before the final seal was written. The post-creation verification record is outside the archive to avoid a circular archive digest; it is covered by the final seal.

No TeX source or PDF was generated: the requested authoritative output is Markdown, and the final handoff contains no mathematical LaTeX. No package, dependency, global setting, canonical ledger, commit, push, or root manuscript file was changed. The only branch/worktree creation was the exact one authorized by TASK-071. Any correction after issuance requires a separately named superseding packet.
