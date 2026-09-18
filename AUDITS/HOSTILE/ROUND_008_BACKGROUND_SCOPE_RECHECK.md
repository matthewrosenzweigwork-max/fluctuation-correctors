# Round 008 supplemental background-scope review

TASK-058. Issued 2026-09-18 UTC, after the original TASK054 seal. **Verdict: PASS for the root's explicit background-regularity qualification and the stated line-440 referent. Those qualifications leave the frozen THM028 proof complete; no additional derivative of the contracted gradient is required.** The unrestricted reading that asserts C1 time or C2 space regularity of the contracted gradient is unsupported and is not certified.

This is a **reused-context supplemental review**, not a fresh audit, blind reconstruction, author clarification, or new independent review of the entire reconstruction. The original TASK054 verdict and every original report/seal remain unchanged. The new mathematical exposure is limited to the four-file supplemental dossier in addition to the original allowed dossier.

Worktree: `/private/tmp/hocf-r008-domain-hostile-20260918`, accessible also as `/tmp/hocf-r008-domain-hostile-20260918`. Branch: `codex/hocf-r008-domain-hostile`; assigned R6 HEAD remains `3aa91391516f35afe5317a287b4f0e2e93e6384c`.

## Chronology and preserved evidence

1. The original hostile report was sealed before any exposure to TASK053's reconstruction. Its review SHA-256 is `977d703cb9fe0175eded6de294421f660328d06ed5ead3a49292084465d826f7`; output-manifest SHA-256 is `8ad8a8d92c179d58220e6bb815470c2c8ea62b08b085dc4aabc04b24bd85fa47`; outer-seal SHA-256 is `0363298ff8dfe0e210929896107de75fd1cc98ca1ed4ca8c4ce36e0a8ea69ded`. The original output-manifest and outer-seal modification times are respectively `2026-09-18T00:46:18.093293+00:00` and `2026-09-18T00:46:18.117005+00:00`. These filesystem times are recorded as chronology evidence, not substituted for the byte seals.
2. After that issuance, the parent reported receiving and reading the original review. An intervening parent message disclosed only the R7 publication identifier `4171be9839feb8acf4c70e1dda014458fdb44490`; no R7 contents were opened or used. That publication has no bearing on the present mathematical verdict.
3. The parent then assigned TASK058 and supplied the fact that the attempted TASK057 author followup failed with `agent thread limit reached`. No author addendum was supplied, opened, or presumed. This report is not presented as the old author's explanation.
4. TASK058 and the supplemental manifest were read first. At the `2026-09-18 00:49:59 UTC` tool-time checkpoint, all original input/output/outer seals were reverified, then exactly the four supplemental files were source-hash checked, copied or confirmed byte-identical in this existing worktree, and destination-hash checked. Only after those checks were the root comparison and complete 610-line reconstruction opened.
5. The complete reconstruction, the root comparison, and the frozen THM028 card were read. The actual uses of the background quantities were then searched and checked against their displayed derivative bounds, weak-derivative argument, and particle formula. At `2026-09-18 00:51:37 UTC`, original report/seal hashes and modification times were checked again. No original report was edited.
6. This separate supplement and its new seals are the only new review outputs. No R9 task/proof, other state/history, memory file, constructor code, extra audit, external source, dependency, or child agent was used. No root file, original audit, canonical ledger, commit, push, or branch state was changed. Standing platform context is disclosed in the unchanged original report; no new memory exposure was requested or used.

The supplemental mathematical inputs are exactly:

- `TASKS/ACTIVE/TASK-058_ROUND008_BACKGROUND_SCOPE_RECHECK.md`, SHA-256 `bdc654d928d1a2cba2be6931bdcd52b45b952453abea6f89eb601f26a5760c93`.
- `THEOREMS/THM-028_HOMOGENEOUS_PARTICLE_CORRECTOR_DOMAIN.md`, SHA-256 `262f2ef32cfb9fa7757774e09970862c06c38891b2ef2d1bd1af875947e928a3`.
- `AUDITS/BLIND_RECONSTRUCTION/ROUND_008_DOMAIN_RECONSTRUCTION.md`, SHA-256 `6e12bf6adf5ae301b9cc7d71df7c0a4cb75aec14318c000c4612c187adbc825e`.
- `AUDITS/BLIND_RECONSTRUCTION/ROUND_008_DOMAIN_COMPARISON.md`, SHA-256 `30e2a7906a12174ec8d55f4e7862eb1f86552c7a164ce9263cd27235fb17f811`.

## Exact regularity that follows

All line references in this section refer to the sealed reconstruction. It establishes joint continuity of the first two spatial derivatives of Phi off the pair diagonal in (15), lines 319–324, and a jointly continuous time derivative bounded by w_s in (16)–(17), lines 328–342. Its global weak derivatives are justified at lines 365–373. For the quantities defined at lines 383–387, those results give precisely:

| Quantity | Certified class | Certified derivative formulas |
|---|---|---|
| `q_t(x)=integral Phi_t(x,y)dy` | C1 in time, C2 in x, with the stated time and spatial derivatives jointly continuous; time derivatives are one-sided at endpoints | `partial_t q=integral partial_t Phi dy`, `grad q=integral grad_x Phi dy`, `D_x^2 q=integral D_x^2 Phi dy` |
| `a_t(x)=integral grad_x Phi_t(x,y)dy=grad q_t(x)` | Jointly continuous in (t,x) and C1 in x, with its first spatial derivative jointly continuous | `D_x a=integral D_x^2 Phi dy` |
| `r_t=integral Phi_t(x,y)dxdy` | C1 in time, with continuous one-sided endpoint derivatives | `r'_t=integral partial_t Phi_t(x,y)dxdy` |

The derivatives in this table are bounded uniformly over time and the stated bounded diffusivity interval, with the theorem's permitted parameter dependence. This table does not assert existence of `partial_t a`, `D_x^2 a`, a mixed time/spatial derivative of Phi, or a third spatial derivative of Phi. Such stronger regularity has not been disproved; it simply does not follow from the estimates supplied here and is unnecessary.

Here is the derivative passage at the exact scope needed. The relative tails for the first, second, and time derivatives are bounded by constants times `epsilon^(d-q1)`, `epsilon^(d-q2)`, and `epsilon^(d-s)`. Each tends to zero because q1,q2,s are less than d. Off a small moving tube, the indicated derivatives are uniformly continuous on compact sets. Splitting off the tube first proves joint continuity of each contracted derivative in the table, including continuity in time; it does not differentiate that continuous family again.

The globally established weak derivatives and Fubini identify the contracted first and second spatial derivatives of q, and the first derivative of a, with those continuous integral functions. Local convolution followed by integration along coordinate segments identifies these as classical derivatives. For time differentiation, the pointwise time fundamental theorem for Phi and the uniform integrable w_s bound allow Fubini and dominated integration. The contracted time derivative is continuous by the same moving-tube argument. The scalar statement follows by integrating once more. At no point is a gradient applied to `partial_t Phi` or a third spatial derivative integrated.

The slice identity `integral Delta_y Phi(x,y)dy=0` at lines 393–396 requires only the second spatial weak derivative and the first-derivative deleted-sphere flux. The latter is of order `epsilon^(d-1-q1)` and vanishes because q1 is less than d-1. The same reasoning applies in the other slot. It does not require a second spatial derivative of a.

Therefore the root's qualification of the collective wording at line 389 is mathematically correct. The phrase “where applicable” must not be used to certify the stronger class for a. The table above is the exact qualified reading endorsed by this supplement; the unqualified stronger reading remains unsupported.

## Every actual use of the background quantities

| Reconstruction location | Actual operation | Regularity needed and available |
|---|---|---|
| Lines 359–363, continuity of R Phi at Coulomb | Haar averages of bounded, locally continuous Phi | Continuity of q only. This follows directly from bounded Phi and a moving-tube split, so it does not create a circular dependence on later differentiated background claims. |
| Lines 389–396 | Contract first, second, and time derivatives; integrate the other-slot Laplacian | Exactly the derivative formulas and slice identity above. No extra derivative of a is needed. |
| Lines 410–414, equation (21) | Apply local Itô to P built from Phi, q, and r; identify its first particle gradient | Phi is C1-time/C2-space off diagonal; q is C1-time/C2-space; r is C1-time. The gradient uses a as a value. The Hessian of the mixed q term uses `D_x a=D_x^2 q`, already available. There is no application of Itô to a. |
| Lines 417–420, equation (22) | Compute the independent diffusion/time part and the force acting on q | Only `partial_t q`, `D_x^2 q`, and `grad q=a`. The term involving a is a first-order drift contraction, not a differentiated stochastic observable. |
| Lines 427–444, equation (23) | Form `H=K(x-y).(a(x)-a(y))`, identify `A_1 q=integral K(z-x).a(z)dz`, and contract the triple and response terms | Values of bounded a and the identity a=grad q suffice for absolute integrability and Fubini. The available first spatial derivative also makes a Lipschitz if the difference in H is estimated together. No derivative of A_1 q, time derivative of a, or second spatial derivative of a appears. |
| Lines 446–459, equation (24) and final stopped drift | Algebraic U3/U2 expansions and substitution of the already proved classical equation | No new background differentiation. |
| Lines 478–495, equations (25)–(26) | Bound drift occupations and squared stochastic integrands | Bounded background contractions and the Jensen bound `||a||2<=||grad_x Phi||2`. Joint continuity makes the composed gradient a suitable predictable integrand. No derivative of that integrand is needed for Itô integration or its bracket. |
| Lines 502–511 | Remove compact collision stops | Bounded q and r for observable convergence, absolute drift integrability, and the L2 stochastic-integrand bound. No higher background regularity is used. |

These are all substantive uses after the definitions, together with the earlier background continuity use. The bound on “background derivatives used in (21)” at lines 480–481 refers to the derivatives actually present there and in the Itô test, all covered by the table. It is not an independent assertion of extra a derivatives.

The frozen THM028 statement contains no separate claim that a is C1 in time or C2 in space. Its particle formula is therefore fully supported under these exact background classes. No theorem hypothesis, conclusion, coefficient, centering, law class, exponent range, or endpoint has been changed.

## Line 440: the referent of “kernel”

The smooth function at z=x when x differs from y is **the pair kernel `Phi(z,y)` as a function of z**. It is C2 near that point by the proved off-diagonal regularity, and C1 suffices for the finite-measure integration by parts. It is not the force `K(z-x)`, which is singular at z=x.

With that explicit referent, the passage at lines 437–444 is correct:

    integral K(z-x).grad_z Phi(z,y) dz
       = -integral Phi(z,y) D(d(z-x)),  x!=y.

Near z=x, the test factor Phi(z,y) is smooth, while the force retains its finite-measure divergence. Below Coulomb the divergence has the prescribed integrable singular density; at Coulomb its atom contributes the multiplication term `-c_d Phi(x,y)` and its Haar compensation remains present. Smoothness of the test factor is exactly what legitimizes that flux formula; smoothness of the force is neither true nor used.

Near z=y the roles differ: K(z-x) is smooth because x differs from y; Phi is bounded, and its gradient has integrable weight w_q1. The boundary integral involving bounded Phi and smooth K is of order `epsilon^(d-1)` and vanishes. Separating those two neighborhoods proves the integrated-gradient response identity without a true-diagonal trace. The same argument applies in the second slot. No derivative of a enters this integration by parts.

If “kernel” were instead read as K, line 440 would make a false local smoothness assertion. This supplement explicitly rejects that reading. The force's singular flux is retained, so the qualification does not conceal or repair a discarded Coulomb atom.

## Disposition and limits

- **PASS:** the precise q/a/r classes in the root comparison follow from the displayed estimates and weak-derivative argument.
- **UNSUPPORTED, NOT CERTIFIED:** the stronger incidental reading that a itself is C1-time/C2-space.
- **PASS:** line 440 is correct with Phi as the smooth test kernel and K as the singular force carrying its full finite-measure flux.
- **PASS:** every actual background use in the reconstructed particle identity, bracket, and localization passage requires only the qualified classes. No concrete remaining gap in the frozen THM028 proof is created by these two wording issues.

This supplement does not claim an additional fresh audit of the reconstruction's signed-jump/common-event/high-moment machinery, reproduce its checker, reopen the original hostile proof audit, or certify any unproved extra derivative. No different analytic step has been repaired. The original isolated hostile PASS for the constructor is unchanged. Root alone records this reused-context supplemental disposition and any canonical promotion; no campaign progress or later publication was used as mathematical evidence.

## Verification and new seals

No new mathematical code was necessary. Verification consisted of reading the complete supplied reconstruction and comparison, tracing every actual background use, checking the exact derivative/flux requirements above, verifying all four supplemental hashes, and rechecking the original input/output/outer seals. All original bytes remain unchanged. No TeX source was created or edited, and the final handoff uses no mathematical LaTeX.

Created outputs:

- `AUDITS/HOSTILE/ROUND_008_BACKGROUND_SCOPE_RECHECK.md` — this separate supplemental report.
- `AUDITS/HOSTILE/ROUND_008_BACKGROUND_SCOPE_RECHECK_INPUT_SHA256SUMS.txt` — copied four-file input seal.
- `AUDITS/HOSTILE/ROUND_008_BACKGROUND_SCOPE_RECHECK_OUTPUT_SHA256SUMS.txt` — new SHA-256 seal for this report and its copied input seal, excluding itself.

From the isolated worktree root, reproduce the integrity checks with:

```sh
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_BACKGROUND_SCOPE_RECHECK_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_BACKGROUND_SCOPE_RECHECK_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_DOMAIN_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_DOMAIN_SEAL_SHA256SUMS.txt
```

This report and its new seals are issued as separate read-only byte strings. Do not edit them or the original reports after issuance; any later correction requires a separately named superseding artifact.
