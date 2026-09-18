# AUD055 / TASK-085 sealed bounded handoff

Issued 2026-09-18 UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r018-bounded-noise-blind`. Branch: `codex/hocf-r018-bounded-noise-blind`. Exact base: `faf6f775a55579722319795cd9a9921e5829a903`.

The adjacent `ROUND_018_BOUNDED_NOISE_RECONSTRUCTION.md` reconstructs the entire frozen THM040, including the genuine singular identity, exact Haar centering, full cross brackets and actual joint weak convergence. The result is conditional on the exact complete R16 actual-source premise as issued. R16 and all earlier source/audit histories remain unchanged. No current candidate comparison, independent promotion, or separate hostile review is claimed.

The proof explicitly establishes asymptotic separation of the initial vector and noise using a conditional exponential identity. It does not assume their independence at finite N. It includes every fixed finite tuple, arbitrary convergent bounded diffusivity sequences, zero limiting noise, zero/repeated times, constants and singular covariance. The first source line that cannot be represented as independently certified in this bounded packet is report equation (6.1). The exact surviving result without that premise is also stated in the report.

## Contents and provenance

* The adjacent report is the complete mathematical reconstruction and assertion/negation disposition.
* `INPUTS/` contains exactly the twelve prescribed original-byte input copies, retaining their original relative paths. `INPUT_SHA256SUMS.txt` is the prescribed input manifest, unchanged.
* `EXPOSURE.json` records the exact input set, worktree, base, exposure boundaries, conditional-source status and actions taken or excluded.
* `round018_exact_diagnostic.py` is newly authored standard-library diagnostic code. It does not read an earlier checker or any repository input.
* `round018_exact_diagnostic_output.json` records its PASS, exact counts and source-code hash.
* `verify_sealed_packet.py` is a read-only input/output/archive verifier. It pins all twelve original hashes and does not extract the archive.
* `OUTPUT_SHA256SUMS.txt` hashes the report, all seven artifact payload files and all twelve input copies, relative to the report's directory. It excludes itself to avoid a self-hash.
* `ARCHIVE_MEMBERS.txt` is the exact sorted archive membership. Its file is itself included in the output manifest and archive. The archive also includes `OUTPUT_SHA256SUMS.txt`.
* `AUD055_ROUND018_BOUNDED_NOISE_IMMUTABLE.zip` is the safe archive of the complete payload and output manifest, under one fixed top-level directory. `ARCHIVE_SHA256SUMS.txt` is its external byte seal. Neither the archive nor its external checksum is placed inside itself.

There are no commits, canonical ledger edits, children, dependency installations, external sources, contact or publication. Only the assigned report and unique artifact directory were authored after copying the prescribed inputs. The original issued input histories are preserved byte-for-byte.

## Verification performed

From the isolated worktree:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_018_BOUNDED_NOISE_BLIND_ARTIFACTS/round018_exact_diagnostic.py
```

Result: **PASS — 4,575 exact assertions in 36 categories; 2,172 deliberate mutation rejections across 17 mutation categories.**

The checks use exact rational and Gaussian-rational arithmetic, finite literal particle Fourier generators, direct deleted-label sums, formal exponential identities and positive rational Gram representations. No random seed, numerical tolerance or simulation is used. The code restores the physical derivative factors explicitly in its recorded convention. Smooth Fourier kernels and rational covariance parameters are coefficient probes; they do not prove a singular theorem. The analytic proof supplies the singular passages and limiting probability argument. All deliberate mutations have nonvacuous witnesses, including loss of an ordered-pair factor, wrong response sign, missing Haar contraction, wrong normalization, wrong thermal lag, lost initial randomness, a false finite-N independence assumption, and the wrong stochastic-exponential sign.

The source/test applicability and complete report were reviewed in this reconstruction context. This self-check is not the separate hostile audit. No TeX source is modified, and the handoff message contains no mathematical LaTeX.

## Read-only seal verification

Run from the isolated worktree:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_018_BOUNDED_NOISE_BLIND_ARTIFACTS/verify_sealed_packet.py
```

The verifier checks all original input hashes, exact local input membership, all output hashes, the diagnostic's recorded code hash and expected counts, exact archive membership, byte agreement between every archive member and the issued file, regular file modes, absence of symlinks/path traversal/duplicates/encryption, bounded archive sizes, ZIP CRCs, the external archive checksum, and read-only issued-file permissions. It reads only this packet. Its output reports the archive and report SHA-256 values. No extraction or file mutation occurs.

The issued layout includes the adjacent report and this entire artifact directory. To move the handoff, preserve that layout and carry the external archive and checksum with the directory. The ZIP payload deliberately does not contain its own archive bytes or external archive checksum. To rerun the diagnostic without modifying issued bytes, copy only its source to an empty writable directory, execute that copy, and compare the newly generated JSON with the sealed JSON; no repository inputs are needed for the diagnostic.

All issued payload files, output manifest, archive and external archive seal are read-only after verification. The packet's own directories are read-only as well. A correction must be issued as a new named report/packet, not edited into this one. SHA-256 seals establish the issued bytes; ordinary read-only filesystem modes are not a claim of hardware-enforced immutability.

**Bounded stopping gate:** the packet is sealed before comparison. Root alone compares with the current candidate, integrates any permitted conclusions, obtains the separate hostile review and decides promotion. The R16 source premise remains expressly conditional throughout that process until its own authorized gates are satisfied.
