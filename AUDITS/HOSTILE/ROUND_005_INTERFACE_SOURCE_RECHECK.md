# TASK047 — supplemental source and constant recheck

Task date: 2026-09-17. Existing review worktree: `/private/tmp/hocf-r005-interface-hostile-20260917_232336_UTC`, branch `codex/hocf-r005-interface-hostile`, based on `52bda5d0d24067b051c6fe9763f2a78e7599e593`.

## Verdict and exact disposition

**SOURCE_RECHECK_PASS. TASK044-D1 and TASK044-D2 are discharged for the original THM-025 candidate together with the separately hashed source-and-constant addendum.** No residual source or constant gap remains in these two dispositions.

The revised scoped verdict is **HOSTILE_REVIEW_PASS for THM-025 plus `AUDITS/ROUND_005_INTERFACE_SOURCE_AND_CONSTANT_ADDENDUM.md`**, SHA-256 `2abad6a860b99f00ada1b6e6610689c4a3c77031e078c1f11fe362fa7e2aceec`, conditional on the exact prerequisite module statements and restricted to the original prescribed-data inverse and actual homogeneous initial iid endpoint. This is not an unqualified pass of the original proof in its original card-only dossier. The original `ROUND_005_INTERFACE_REVIEW.md` remains an immutable historical **REPAIR_REQUIRED** report, with SHA-256 `35ed3222548dc1ce7b5b1dbf8d4124fce71d54c5e0c25bd26bd94b4ea64185f1`.

No theorem range, norm, centering, iid coefficient, rate, or microscopic regime has changed. No finite-particle generator-domain theorem, singular Ito passage, evolved-law estimate, residual/bracket control, fluctuation law, or critical hierarchy closure is added.

## Context reuse, inputs, and preservation

This is the **same reviewer context** that conducted TASK044 and independently wrote the heat bridge in that earlier report. It is therefore a supplemental source/constant recheck, not a new blind context, not a second fresh review of THM-025, and not independent certification of that reviewer's own additional proof. The evidence used to discharge D1 is the newly supplied pre-existing R4 source text, checked at its cited location, with the separate reconstruction and hostile report as corroboration. The earlier reviewer-added bridge is not used as independent evidence.

The TASK047 task and addendum were read fully. All three cited R4 reports were read; the mathematical recheck is restricted to the cited local-kernel premise and the common divergence constant. The five supplemental files were hashed at the root, copied into this worktree, and hashed again before use. The supplemental input manifest is preserved separately from the original nine-file input generation.

Before copying and again in the final integrity checks, the original nine inputs, five listed review outputs, original input manifest, and original output manifest all matched their seals. The original THM-025 card, candidate memorandum, TASK044 report, checks, results, and seals were not edited. No R4 source was edited. No root working-tree file was edited, and no commit, push, dependency installation, or child worker was used. No memory, canonical state, repository history, or unlisted source was read.

The supplied R4 reports contain their own isolation and seal declarations. This recheck verifies the supplied report bytes and their mathematical content. Historical R4 input/output manifest files and checker files are outside the five-file supplement and were not inspected or rerun. The exact creation chronology implied by “before THM025 existed” is not independently established from the dated report texts alone. Those administrative assertions are not required for the two mathematical/source dispositions and are not silently certified here.

## Source-location and hash checks

| Addendum assertion | Verified source and exact location | Result |
|---|---|---|
| Constructor's local kernel lemma | `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, Section 2, lines 69–109, equations (2.1)–(2.4) | PASS. The file has 541 lines. The stated range contains the heat formula, exact Fourier coefficient, coefficient-one Euclidean integral, smooth local remainder, smoothness off zero, and Fourier identification argument. |
| Independent reconstruction contains the same local preflight | `AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RESPONSE_RECONSTRUCTION.md`, Section 1, lines 20–70 | PASS. Gaussian evenness is explicit at line 27, the Fourier coefficient is computed at lines 47–61, and the coefficient-one integral and smooth local remainder occur at lines 63–70. Its independence is disclosed in its own lines 3–8; it is not inferred from a filename alone. |
| Hostile report checked the local coefficient and differentiation bounds | `AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_REVIEW.md`, C01 at line 35 and Section 3.1, lines 63–76 | PASS. C01 records the bounded claim, and the cited subsection explicitly recomputes the Fourier prefactor, Euclidean coefficient one, and the two heat-time derivative bounds. |
| Same frozen local premise as THM-023 | Original `THEOREMS/THM-023_PERIODIC_BASE_PAIR.md`, line 5 | PASS. The newly supplied lemma gives the exact coefficient, periodic even kernel, smoothness off zero, and smooth even remainder on an embedded ball required there. |
| Common divergence constant | Addendum lines 15–20, together with original THM-021 line 10 and THM-023 line 16 | PASS. The maximum construction supplies the exact comparison that was previously left implicit. |

The three source hashes in the addendum match the independently computed hashes:

- Constructor: `135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be`.
- Reconstruction: `e07df6f4285cdb2dbb3a4fd28ab7cf325a355c75129378118f29a7fd76df53f1`.
- Hostile report: `06bccaa37a0c7018e1595d14662289c2c4be28017ee673abf8dffe2dc600aaa1`.

The constructor hash also agrees with the full-proof hash already printed in the original THM-021 card. This is an exact source identification; the missing local lemma is supplied by the addendum, not retroactively inserted into the earlier card-only dossier.

## TASK044-D1: mathematical check of the supplied local lemma

The R4 proof uses `alpha=(d-p)/2` and

    A=4^((d-p)/2) pi^(d/2)/Gamma(p/2),
    g_p=A integral_0^infinity t^(alpha-1)(p_t-1) dt,

where p_t is the periodized mass-one Gaussian heat kernel. For `0<p<d`, the integral converges in L1: near zero its integrand norm is at most `2 t^(alpha-1)`, and at infinity the nonzero heat Fourier modes give exponential decay. Thus the Fourier interchange is justified, and direct cancellation gives

    A Gamma(alpha)/(4 pi^2)^alpha
      = pi^(p-d/2) Gamma((d-p)/2)/Gamma(p/2).

This is precisely the frozen torus coefficient. In the Euclidean Gaussian contribution, substituting `v=|z|^2/(4t)` gives the coefficient

    A (4 pi)^(-d/2) 4^(p/2) Gamma(p/2) = 1.

The powers of 4 and pi cancel exactly; there is no missing volume, half, or Fourier factor.

The regularity argument supplies a smooth remainder **through zero**, which is stronger than a principal-singularity asymptotic. On any compact subset of the ball of radius 1/3, every nonzero lattice image is separated from zero. At short times its Gaussian derivatives, summed over the lattice, are bounded by a fixed inverse power of t times `exp(-c/t)`, for each fixed derivative order. These bounds remain integrable after multiplication by `t^(alpha-1)`. The separately subtracted constant is integrable because alpha is positive. At long times the periodic remainder and its derivatives decay exponentially. The Euclidean contribution and every fixed derivative, on the compact ball, are bounded after the time weight by an integrable multiple of `t^(-p/2-1)` or a faster-decaying power. This exponent is integrable because p is positive. Dominated differentiation therefore gives the smooth remainder asserted in equation (2.4), including its value and all derivatives at zero. The same argument away from lattice zero gives smoothness elsewhere.

Evenness is an exact property of the supplied representation. The Euclidean Gaussian is even, and changing lattice index n to -n gives `p_t(-z)=p_t(z)`. The integral and its principal power are even, so their smooth difference is even on the symmetric embedded ball. No extra symmetry assumption or silent change of representative is needed. With p=s, this supplies every local kernel hypothesis in THM-023.

The addendum's reference to a positive heat representation is valid in the sense of a nonnegative heat kernel and positive prefactor; the formula still subtracts 1. It does not assert pointwise positivity of the zero-mean Riesz kernel, and no positivity of that kernel is used here.

**Disposition: D1 discharged by the supplied R4 lemma and this explicit source incorporation.** The absence of the lemma from the original THM-021 card remains correctly recorded in the historical TASK044 report.

## TASK044-D2: exact common-constant check

Distinguish the THM-021 lower-bound constant `kappa_21` from the THM-023 smooth-compensation constant `C0_23`. Fix the local decomposition independently of N and diffusivity, and set

    kappa = max(kappa_21, C0_23).

Both constants are finite fixed-data constants. The measure inequality `div K >= -kappa_21 dx` implies `div K >= -kappa dx`. For every N at least 2,

    C0_23/N <= kappa/N <= kappa/2.

The supplied **singular** propagator bound from THM-023 consequently gives exactly

    ||S_(t,a)||_(2->2) <= exp[(D_u+C0_23/N)(a-t)]
                      <= exp[(D_u+kappa/2)(a-t)].

No smooth-cutoff result is promoted to a singular-flow result in this argument. Using `c=D_u+C0_23/2` directly would also suffice. The response norm still uses the unchanged total variation of div K and the unchanged L1 norm of K; enlarging kappa does not change `C_R=2[M0 TV(div K)+M1 ||K||1]`.

There is a notation collision in the newly supplied R4 source: its equation (1.2) calls a response bound C0. The addendum expressly identifies C0 with the THM-023 compensation norm, not with that R4 response bound. Keeping those source-local names distinct removes any ambiguity and introduces no additional defect.

**Disposition: D2 discharged.** Constants remain independent of N and the permitted diffusivity; optimality of kappa is neither needed nor asserted.

## Revised scope and remaining boundary

The candidate-plus-addendum passes the original bounded interface review for the unit Haar torus, d at least 3, positive Riesz exponent at most d-2, finite horizon, N at least 2, bounded nonnegative diffusivity, and the stated uniform regular prescribed data. The exact THM-021, THM-023, and THM-024 statements remain prerequisites; their entire proofs are not newly certified by this two-item recheck.

The actual homogeneous reference and fixed smooth terminal test retain the Fourier signs and uniform spatial bounds checked in TASK044. The initial mean-field-centered iid endpoint retains the original density factor, deleted-label normalization, and rates. The positive beta lower bound and separate zero-noise endpoint remain explicit. Eventual coverage of critical sequences and coverage only of the stated subcritical sequences are unchanged.

The first out-of-scope dynamical obligation is still the domain/regularization theorem connecting the auxiliary Borel pair inverse to the interacting N-particle corrector identity, including derivatives, cubic source, contractions, and brackets. Neither D1 nor D2 repairs that separate gap.

## Checks, outputs, and seal

Command executed in this worktree:

    python3 AUDITS/HOSTILE/ROUND_005_INTERFACE_SOURCE_RECHECK_VERIFY.py

Result: **PASS**, Python 3.9.6, standard library only. The checks verify all nine original inputs, all five supplemental inputs, all five original listed outputs, both original manifest hashes, the three cited source hashes, the exact source locations, and 27 exact rational instances of the common-constant inequality. There is no random sampling or floating-point tolerance. The finite scalar checks support the displayed all-parameter argument; they do not replace the local regularity proof. Prior check outputs were not rerun or overwritten.

Created outputs are this separate report, its verification script, JSON check results, README, supplemental input manifest, and supplemental output manifest. The supplemental output manifest hashes every new output except itself. The original input/output generation remains separately sealed. No TeX was generated or modified; the requested audit outputs are Markdown and verification records.

Original input manifest SHA-256: `d75bf1f5f67fbc8cabc65ba097d0c77bfda3dc485e50d2808b6b30ecc9fb446e`.

Original output manifest SHA-256: `10b4836f893136fd2166af4e9358c3c0612c76da8f17bab93a0fbbfa8ca89c03`.

Supplemental input manifest SHA-256: `892ab43a9933fc844dd880e8d7e3e90c9203296236555293f43298f3d434e22b`.

This recheck is immutable after sealing. Its scoped pass applies to the exact candidate-plus-addendum combination identified above. The original REPAIR_REQUIRED report remains historical evidence of the original dossier and is not edited or relabeled.
