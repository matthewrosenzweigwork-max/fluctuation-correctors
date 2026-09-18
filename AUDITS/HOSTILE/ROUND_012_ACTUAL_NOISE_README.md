# TASK067 sealed hostile review

Verdict: PASS_CONDITIONAL. The frozen R12 uniform full-inverse gradient and actual-noise implication pass with no new unsupported line or required repair. The R10 sharp deterministic energy floor and R8 genuine particle-martingale domain remain conditional premises. No broader fluctuation result is certified.

Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r012-noise-hostile

Branch: codex/hocf-r012-noise-hostile

Base commit: 29d7ce427ad7a98739b18d07781e71c4598b3579

Sealed archive: ROUND_012_ACTUAL_NOISE_TASK067_20260918_034515_UTC.tar.gz

The archive preserves repository-relative paths. It contains only the 24 permitted dossier files, their original manifest, and this review's output files. The archive and issued files are read-only; later changes must be separately issued superseding artifacts.

The principal deliverables under AUDITS/HOSTILE are:

- ROUND_012_ACTUAL_NOISE_REVIEW.md: complete analytic reconstruction, explicit uniform constants, 22 per-claim dispositions, exact conditional scope, first unsupported external premises and exposure disclosure.
- round012_actual_noise_hostile_exact.py: fresh standard-library exact arithmetic checker. It never imports a previous checker.
- ROUND_012_ACTUAL_NOISE_EXACT_RESULTS.json: PASS, 22,725 exact assertions, detailed categories, source and checker hashes.
- ROUND_012_ACTUAL_NOISE_EXACT_RERUN.json: independently executed rerun, byte-identical to the issued result.
- ROUND_012_ACTUAL_NOISE_INPUT_VERIFICATION.json: copied 24-input record with hashes and byte lengths.
- ROUND_012_ACTUAL_NOISE_ENVIRONMENT.json: environment, exposure, preservation and verification record.
- ROUND_012_ACTUAL_NOISE_INPUT_SHA256SUMS.txt and ROUND_012_ACTUAL_NOISE_OUTPUT_SHA256SUMS.txt: input and output seals. The output manifest excludes itself and the archive to avoid a hash cycle; the archive has its own adjacent SHA-256 receipt.

From the worktree or an extracted archive root, verify the dossier and outputs:

    shasum -a 256 -c AUDITS/HOSTILE/ROUND_012_ACTUAL_NOISE_INPUT_SHA256SUMS.txt
    shasum -a 256 -c AUDITS/HOSTILE/ROUND_012_ACTUAL_NOISE_OUTPUT_SHA256SUMS.txt

Reproduce the checker without modifying sealed results. Choose a new writable output path:

    python3 AUDITS/HOSTILE/round012_actual_noise_hostile_exact.py --output /tmp/hocf-task067-independent-rerun.json
    cmp AUDITS/HOSTILE/ROUND_012_ACTUAL_NOISE_EXACT_RESULTS.json /tmp/hocf-task067-independent-rerun.json

The recorded rerun used:

    python3 AUDITS/HOSTILE/round012_actual_noise_hostile_exact.py --output AUDITS/HOSTILE/ROUND_012_ACTUAL_NOISE_EXACT_RERUN.json
    cmp AUDITS/HOSTILE/ROUND_012_ACTUAL_NOISE_EXACT_RESULTS.json AUDITS/HOSTILE/ROUND_012_ACTUAL_NOISE_EXACT_RERUN.json

Verify the archive from AUDITS/HOSTILE:

    shasum -a 256 -c ROUND_012_ACTUAL_NOISE_TASK067_20260918_034515_UTC.tar.gz.sha256

The checker uses Fraction arithmetic and Gaussian rational sparse Fourier polynomials; no external package, floating-point tolerance, random seed, or simulation is required. Its results include its own SHA-256 and Python version. A different Python version may therefore change result metadata even when all assertions pass. The 22,725 assertions are not 22,725 independent mathematical cases; related identities and repeated parameter values are counted separately.

The finite diagnostics support the analytic proof. They do not certify singular limits, independent source premises, or mathematical novelty. There is no TeX/PDF deliverable in this bounded Markdown review.

Input source contents and canonical records were not edited. Current R11 work, blind review, root diagnostics and previous checkers were not read or used. No commit, push, installation or child agent was involved. The coordinator can integrate this conditional pass only at its stated source scope.
