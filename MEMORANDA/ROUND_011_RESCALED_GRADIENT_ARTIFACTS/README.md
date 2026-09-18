# TASK063 sealed construction

Status: PROVED_CANDIDATE / SELF_CHECKED. The root seed was explicitly disclosed. This packet is an ordinary construction, not a blind or independent audit.

The complete proof is ../ROUND_011_BOUNDED_RESCALED_DIFFUSION_GRADIENT.md. It establishes uniform weighted value and actual first-gradient bounds for the existing homogeneous full pair inverse when the rescaled diffusivity is bounded. Both finite-measure responses and the Coulomb compensation are retained. It also establishes uniform local C1 and global Haar W1,1 convergence to the terminal-zero response-only inverse, and uniform convergence of the contracted gradients.

The bound includes every N at least two and zero noise. Constants are explicit in the memorandum and independent of N and the admitted diffusivity. The proof does not use a source-occupation bound proportional to N. No actual-law singular tail, law transfer, bracket decay, H1 bound, diagonal trace, or weighted-supremum convergence near the shrinking diagonal region is claimed. Fixed positive diffusivity is outside this new uniform parameter class. The full bounded-noise target remains distinct.

## Files and verification

* The assigned manifest in AUDITS names the twenty permitted inputs. COPIED_INPUT_SHA256SUMS.txt records their verified bytes.
* round011_rescaled_gradient_exact_checks.py is a newly written standard-library checker; no prior checker was read. Its result records 9,248 exact assertions, including input integrity.
* The checker uses rational Cartesian second-order jets, exact perfect-power roots, literal compensated Fourier modes, and exact repeated Volterra integration. It does not use numerical tolerances or randomness.
* VERIFICATION.json records the verified base, branch, input hashes, exact-check result, unchanged tracked checkout, and syntax/whitespace checks.
* OUTPUT_SHA256SUMS.txt seals the six named payload outputs. It excludes itself.
* The timestamped archive contains precisely the twenty inputs, assigned manifest, six payload files, and output manifest. The external archive-verification JSON records safe member names, CRC, exact member list, and member-by-member SHA-256 comparison.
* The timestamped packet seal hashes the assigned input manifest, copied-input manifest, output manifest, archive, and archive-verification JSON. It is outside the archive to avoid a circular seal.

Run the exact checks from the assigned worktree:

    python3 MEMORANDA/ROUND_011_RESCALED_GRADIENT_ARTIFACTS/round011_rescaled_gradient_exact_checks.py

Verify the input and output manifests from that same directory:

    shasum -a 256 -c AUDITS/ROUND_011_RESCALED_GRADIENT_INPUT_SHA256SUMS.txt
    shasum -a 256 -c MEMORANDA/ROUND_011_RESCALED_GRADIENT_ARTIFACTS/OUTPUT_SHA256SUMS.txt

The checker recreates its deterministic JSON result. Its absolute worktree path appears in console output only; the result's content is deterministic in any checkout containing the same inputs.

The worktree is /Users/matthewrosenzweig/.codex/worktrees/hocf-r011-rescaled-gradient, branch codex/hocf-r011-rescaled-gradient, at base b2510ed08ecc26387d9fc14daaf174d3c35f5638. No tracked file was changed. Added files are the copied task/manifest and this construction packet. No commit, push, dependency installation, child agent, or canonical state change was performed. The mathematical deliverable is Markdown; no TeX source was created.

## Handoff

Root should review and integrate the precisely scoped assertions before assigning any canonical theorem identifier. A fresh isolated reconstruction and hostile review remain required. The exact diagnostics are same-context supporting evidence, not certification of the analytic proof.

All payload bytes and the issued archive are immutable after sealing. Any correction must be a separately named superseding report and seal. The next unsupported downstream step is a quantitative estimate under the actual evolving particle law; it is not supplied by the spatial norms proved here.
