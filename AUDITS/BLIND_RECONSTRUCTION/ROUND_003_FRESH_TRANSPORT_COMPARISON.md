# AUD-019 — fresh isolated reconstruction of THM-017

2026-09-17. Root compares the sealed constructor with a fresh Astra Max context, TASK-031, fork_turns=none, in /private/tmp/hocf-r003-fresh-transport-20260917. Input and output manifests are adjacent. Reconstruction report SHA-256 dd5116c54e7f424271c3f7a8e2ccb83cdcb13474d89c1175e4301d9a325a86ad. Candidate card and constructor bytes are unchanged.

## Isolation and verdict

The worker received only the THM-017 and THM-015 statements, frozen model/administrative inputs and its bounded task. It did not receive the constructor proof, any review, root diffusion memo or root TeX. It sealed its reconstruction before receiving comparison feedback. Root read the whole issued reconstruction. Verdict: FRESH ISOLATED_RECONSTRUCTION_PASS for THM-017's stated punctured characteristic formula, collision value behavior, local norms and cutoff iid endpoint. This is independent reconstruction of the declared model, not a proof of the full singular corrector or a new review of previous reused contexts.

## Line-by-line claim comparison

1. Forward characteristics give radius to the power s+2 increasing at 2s(s+2)/N, with angle fixed. The integrated quadratic source gives exactly the constructor's N/4 factor, time orientation and radial exponent. Terminal value is zero.
2. The solution class is finite pointwise on every nonzero starting point, with absolutely continuous composition along each forward characteristic through terminal time. The derivative is the negative source almost everywhere. Integrating along that path proves uniqueness. No unproved growth condition, collision boundary condition or PDE uniqueness theorem is used. This is exactly the constructor's declared characteristic class.
3. The directional limit, anisotropic discontinuity, angular moment Q(A), inner and outer amplitude estimates, and three L2 regimes agree. The reconstruction also proves the all-N upper bounds directly, independently of the prior hostile constant completion. Bounds depend on fixed dimension, singularity, radius and time horizon; the vanishing-time case is separated.
4. Both reports allow an arbitrary fixed smooth radial cutoff with values in [0,1], one on an inner ball and zero outside a ball of radius less than 1/2. The fresh example is one through radius 1/8 and zero from 1/4, using a flat exponential in r; the constructor's example uses r squared and arbitrary fixed radii. These are different realized kernels in the same declared admissible family. The general estimates use only this family and the support radii, so the same theorem is reconstructed. No bytewise equality of cutoffs or diagnostic kernels is claimed.
5. The fresh report proves the exact iid projection identity directly, including nonzero mean and first projection, ordered-label normalization and deterministic centering term. It obtains the single density factor M after the relative-coordinate integral. The endpoint bounds hold for every deterministic time with the supremum outside the expectation; they do not claim a path supremum or an evolved iid law.
6. The constructor's extra isotropic C2 Hessian, punctured Laplacian expansion and annular source are not independently reconstructed by this bounded task. They retain their separate fresh hostile evidence AUD-018. No extra claim receives blind status by association.

## Reproduction

Root reran python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_TRANSPORT_CHECK.py. PASS: 12 exactly enumerated iid cases and 54 exact rational transport substitutions. Output: CERTIFICATES/OUTPUTS/round003_fresh_transport_root_rerun.json. These finite tests check coefficients; the analytic bounds, characteristic uniqueness and limits are proved in the report. All four sealed outputs and their input manifest were verified against the worker's original manifest before integration.
