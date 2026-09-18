# AUD066 sealed hostile packet

Read `REVIEW.md` first. The entire THM045 conjunction is verified; the frozen proof has one false non-load-bearing support sentence at line 153, requiring an explicit separate correction. Exact inputs are preserved unchanged. This is a static-law result, with no inference about an actual iid-prepared process.

The packet contains exactly eleven input copies under `INPUTS/`, their original prescribed checksum manifest, the full review, a source/exposure record, a newly written singular-kernel diagnostic and complete results, diagnostic development history, and a new read-only byte verifier. `OUTPUT_SHA256SUMS.txt` covers every artifact file except itself. That manifest is itself included and byte-compared in the archive; its digest is recorded in the final external seal receipt. This deliberate exclusion avoids a circular self-hash. The separate standalone review must equal `REVIEW.md` byte-for-byte.

The sibling ZIP holds the exact complete artifact directory as regular read-only files, including its output manifest. The sibling `.zip.sha256` gives the archive digest. The final `ROUND_023_STATIC_THRESHOLD_HOSTILE_SEAL.json` records the actual verification result and is outside the archive to avoid a circular archive receipt. Files and artifact directories are read-only; a correction requires a new packet.

To verify hashes, exact members, read-only modes, safe paths/types, archive CRCs, and complete archive/disk byte equality without extraction:

    python3 AUDITS/HOSTILE/ROUND_023_STATIC_THRESHOLD_HOSTILE_ARTIFACTS/verify_packet.py

To recompute the diagnostic and compare it with the saved result without writing any sealed file:

    python3 AUDITS/HOSTILE/ROUND_023_STATIC_THRESHOLD_HOSTILE_ARTIFACTS/hostile_diagnostic.py --verify

The latter can take about a minute. Python 3.9.6 and its standard library suffice; no dependencies were installed. The final supporting result is 384 assertions in 22 categories and 12 detecting mutations. See the JSON for all cases, values, tolerances, and script digest. Exact integer/rational checks and nonrigorous floating checks are distinguished. No numerical output substitutes for the analytic review.

## Independent Ewald diagnostic

At the heat split `t0=1/(4*pi)`, the small-time image integral is explicit:

    4*pi^2 * integral_0^t0 (4*pi*t)^-2 * exp(-r^2/(4*t)) dt
      = exp(-pi*r^2)/r^2.

The constant subtraction contributes `-pi`. The large-time nonzero Fourier integrals give `exp(-pi*|k|^2)/|k|^2`. Therefore, off the singularity,

    g(x) = sum_n exp(-pi*|x+n|^2)/|x+n|^2 - pi
           + sum_{k!=0} exp(-pi*|k|^2)*cos(2*pi*k.x)/|k|^2.

The force is the negative derivative. A spatial image contributes

    2*(x+n)*exp(-pi*r^2)*(pi/r^2+1/r^4),

and a paired positive/negative Fourier frequency contributes the corresponding sine term. The central image has finite part `-pi` after removing `|x|^-2`; it is distinct from the constant subtraction. At zero the remaining image and Fourier sums coincide. This supplies a second direct check of `H0` and of the self-subtraction coefficient.

For the deformation in the proof, only the first coordinates change. Summing the three transverse grid offsets turns the image indices into `j/m`, with exact integer multiplicities for `j_2^2+j_3^2+j_4^2`. In the truncated Fourier sum all transverse frequencies vanish when the Fourier cutoff is below `m`. The first-coordinate pairs are still summed literally, with the exact `1/(2*N^2)` statistic and `1/N` energy conventions. The program uses image and Fourier cutoffs 4, plus a cutoff-3 stability test. This is a deterministic finite Ewald calculation, without certified tail bounds or interval arithmetic.

The tested illustrative `a=0.05` is not asserted to be an explicit bound on the abstract sufficiently small `a` from the analytic proof. The numerical finite-grid convergence is supporting falsification evidence only. The analytic source limit, energy absorption, and density construction are checked independently in the review.

## Handoff

Root alone compares this result with other lanes and issues any correction or canonical status update. The required correction is local and explicit: the final support inherits the first two bounds of (6.1); its third bound is pretranslation and is used through the rotation-invariant amplitude. The theorem is not narrowed and its constant is unchanged. Do not alter the frozen source copy or this issued audit to implement that correction.
