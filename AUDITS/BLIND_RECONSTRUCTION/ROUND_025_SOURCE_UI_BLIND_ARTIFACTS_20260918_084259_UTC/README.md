# AUD069 — full THM048 and THM049 isolated reconstruction

Separate whole-claim verdicts: **THM048 RECONSTRUCTED; THM049 RECONSTRUCTED. Joint verdict: RECONSTRUCTED.** Root source/dependence comparison and separately assigned hostile review remain required. THM046 and actual signed-correlation cancellation remain open.

`REPORT.md` is the complete human-checkable proof, byte-identical to the assigned sibling reconstruction report. `SOURCE_EXPOSURE.md` records every allowed source and the administrative two-input extension. `FAILURES_LIMITATIONS.md` retains failed shortcuts and the remaining scientific/audit obligations. `PERMITTED_INPUTS/` contains all thirteen exact inputs and both original manifests. `verdict.json` gives the separate and joint dispositions.

The fresh `fresh_exact_diagnostic.py` uses only the Python standard library and exact rational/Gaussian-rational arithmetic. Its first execution passed **2,203 assertions in 32 categories**. All **sixteen mutation families have nonzero detections**, recorded in `diagnostic_results.json`. There is no random seed, floating-point tolerance, imported checker or dependency installation. Finite diagnostic models support coefficients and scaling; they are not proofs of singular stochastic limits.

From any directory, verify the issued packet and sibling archive without writing to them:

```text
python3 /path/to/ROUND_025_SOURCE_UI_BLIND_ARTIFACTS_20260918_084259_UTC/verify_packet.py
```

The verifier checks all payload paths/hashes/sizes, all thirteen input hashes, the exact report copy, complete and safe unique regular archive membership, the archive and external-inventory seals, read-only issued modes, and deterministic replay of the fresh diagnostic. It does not extract the archive or alter files. It requires only Python 3.9 or later and the standard library.

To rerun just the diagnostic without writing a result file:

```text
python3 /path/to/ROUND_025_SOURCE_UI_BLIND_ARTIFACTS_20260918_084259_UTC/fresh_exact_diagnostic.py
```

`PAYLOAD_MANIFEST.json` lists every packet file except itself, whose hash is bound by the external seal. The named sibling `*_ARCHIVE_MEMBERS.json` lists every archive member, including the payload manifest, with its size and SHA-256. The named sibling `*_SEAL.json` binds the archive, member inventory, payload manifest and external report. The archive contains only unique safe regular file members under the one packet prefix; no directory, link, device or extraction-dependent member is needed. The payload and issued sibling files are read-only. Integrity evidence is not a cryptographic signature or a mathematical certification.

Original verification commands were the two `shasum -a 256 -c` manifest checks, the fresh diagnostic with its assigned JSON output, and this portable verifier after issuance. No commit or canonical integration was performed. There is no TeX artifact in this audit packet; the proof and handoff documents are Markdown, and no TeX build is claimed.
