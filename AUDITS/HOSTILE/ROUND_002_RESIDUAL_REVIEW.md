# TASK-015: hostile review of the fixed-smooth iid residual dossier

Date: 2026-09-17 UTC. Reviewer: `/root/capacity`, assigned Astra Max. Worktree: `/private/tmp/hocf-round002-hostile-20260917`, HEAD `a06178658d1e3d458536ff312ca793947212ec67`.

## Verdicts

| Bounded result reviewed | Verdict | Exact scope |
|---|---|---|
| THM-010 and the constructor's four explicit residual bounds | **PASS** | The displayed constants in coupling (2.1)--(2.4), the four raw estimates, and their temperature-scaled limits are valid. |
| Constructor's lower-drift bound | **PASS** | The stated constant is `5 T d kappa_0 A_1/N`, with no missing factor of two. |
| Constructor's Section 8 sufficient-regularity refinement | **PASS** | It is an a priori estimate for deterministic smooth tests with the stated uniform norms; no existence theorem at reduced regularity is inferred. |
| Independent residual proof, falsification Sections 3--5 | **PASS** | Its actual-law sixth-moment argument and absolute residual/bracket bounds hold under the frozen iid hypotheses. |
| Uniform smooth-data estimate (D1) | **PASS** | The reaction term and transport commutator give the stated exponent. |
| Uniform smooth-data estimate (D2) | **PASS** | The response is bounded on the stated one-body `C^m` space for `m>=1`. |
| Uniform smooth-data estimate (D3) and the resulting choice of A | **PASS** | This uses the supplied audited THM-009 estimate and retains the required extra derivative of the terminal test. |
| Free, moving-background, and one-mode interacting diagnostics | **PASS, mathematically** | All displayed coefficients were checked analytically; the independent exact computation below additionally checks the most sensitive ones. |
| Gibbs law-class obstruction, falsification Section 8 | **PASS** | It disproves an unqualified transfer of the smooth moment/pair estimates to this Gibbs preparation; it does not contradict the iid theorem. |
| Rendering of falsification equation (2.5), first display line | **FAIL, cosmetic only** | One literal form-feed byte corrupts the fraction command. The coefficient is unambiguous from the definitions and was independently recomputed. |

No load-bearing false assertion or unfilled mathematical proof step was found in these bounded results. The cosmetic failure is documented below and was not silently repaired. The submitted proof bytes were preserved. These verdicts do not certify a Gaussian limit or any singular/cutoff-uniform assertion.

## 1. Isolation, authority, and immutable inputs

This reviewer first performed an operational concurrency-configuration task and then an isolated reconstruction of the finite smooth all-order generator and bracket identities. The latter report was sealed and its hash supplied before this residual dossier was read. Neither residual construction nor the root's norm-qualification proof had been seen during those earlier tasks. The present review is one hostile-review context assessing two independently submitted proof candidates; it is not two separately staffed audits and is not a newly allocated session. The root alone performs the separate comparison with the previously sealed all-order reconstruction.

The five files listed in `AUDITS/ROUND_002_RESIDUAL_INPUT_SHA256SUMS.txt` were verified before reading the mathematical submissions. Their SHA-256 values are:

```text
b431943e983b7be60c0c8e48f0391b3be5990ce51909837573028ecfbd92e98d  TASKS/ACTIVE/TASK-015_ROUND002_HOSTILE.md
d50c875c3c37a354f8af6129bdba634b97e0f05d17f198cb2f2ef530c32eec6f  THEOREMS/THM-010_SMOOTH_IID_RESIDUAL.md
7eb57c1f4e8f6da9c80a2f53a95349153605467532afb33b269938b242761852  MEMORANDA/ROUND_002_COUPLING.md
125317981b543cf83a47a64efc1455453fbd942e476a52b15e64ec984c216856  MEMORANDA/ROUND_002_FALSIFICATION.md
078472d56b74ce3c59fc9777e70f56ad38e23778f419dd619b871d3b5296e458  MEMORANDA/ROUND_002_UNIFORM_SMOOTH_DATA.md
```

The explicitly permitted supplementary inputs were the frozen model, `PO-001_RESIDUAL.md`, `COR-001_PAIR_CORRECTOR.md`, the THM-009 theorem card, and the statement/constants and operator estimates in Sections 1--2 of `ROUND_001_SMOOTH.md`. Their hashes are in `AUDITS/ROUND_002_RESIDUAL_ADDITIONAL_INPUT_SHA256SUMS.txt`. The audited THM-009 bound is an imported, identified dependency; this report does not reissue an audit of its entire prior proof. No private theorem or external literature result was used. No other worktree or newly submitted finite-dimensional limit dossier was inspected for this review.

The reviewed model has fixed smooth interaction and confinement on the unit torus, fixed finite horizon, iid initial positions independent of the driving Brownian motions, arbitrary finite positive inverse temperature, and deterministic mean-field centering. All estimates concern the actual evolved interacting law. Symmetry of the pair test is supplied by the stated backward problem. The explicit uniform spatial norm hypothesis in PO-001 is used as written; it is not inferred from an initial iid law.

## 2. Constructor constants and moment estimate

Here the letters are the constructor's, including its Sobolev index `q`, not the inverse-particle-number abbreviation in the previous algebra reconstruction.

The index is
\(q=\lfloor d/2\rfloor+2>d/2+1\). On dyadic frequency shells the two lattice sums defining \(B^2\) and \(D^2\) have contributions bounded respectively by constants times \(2^{j(d-2q)}\) and \(2^{j(d+2-2q)}\); both are summable. This checks coupling lines 98--110, including the derivative needed for the Dirac-mass Lipschitz estimate.

The multinomial expansion of \((1+4\pi^2|k|^2)^q\), followed by Parseval on the mass-one torus, gives
\(\|h\|_{H^q}\le(d+1)^{q/2}\|h\|_{C^q}=Q\|h\|_{C^q}\).
For a k-variable kernel the product Fourier weight uses at most `kq` total derivatives and has coefficient sum \((d+1)^{kq}\). Thus coupling (3.3)--(3.4) have the displayed constants `Q` and `Q^k`, with no missing dimension factor. Vector fields acquire the separate factor \(\sqrt d\) displayed in \(\mathcal K\), \(L_\Phi\), and \(D_\Phi\).

For iid comparison samples, the centered Hilbert vectors have norm at most `2B`. Their second moment is exactly
\[
 \mathbb E\|\overline\rho\|_{-q}^2
 =N^{-1}(B^2-\|\mu\|_{-q}^2).
\]
In the sixth moment, a label appearing once vanishes by conditioning and linearity. At most three labels remain, so the number of potentially surviving lists is bounded by
\(\sum_{l=1}^3\binom Nl l^6\le3^7N^3\).
Bounding each term by \((2B)^6\), dividing by \(N^6\), and taking the sixth root gives exactly \(J=2\,3^{7/6}B\). Lower probability moments follow by monotonicity. This validates coupling (4.1)--(4.3), including their constants.

For the synchronous coupling, Euclidean Lipschitz constants are at most `d v_1` and `d kappa_1`. Noise cancels on common lifts. The averaged displacement therefore satisfies
\[
 D_N'(t)\le d(v_1+2\kappa_1)D_N(t)
               +\mathcal K\|\overline\rho_t\|_{-q}.
\]
The root label is not dropped: `K(0)=0` makes the deleted empirical force exactly the full one. Although the comparison particle and its empirical error are dependent, the convolution bound is pathwise and uniform in the evaluation point. Its use requires no conditional independence at that step.

The Dirac Lipschitz constant is exactly the stated lattice norm `D`. Applying the integrating factor, Minkowski, and the iid estimate gives
\[
 \sup_{t\le T}\|\|\rho_t\|_{-q}\|_{L^p}
 \le \frac{J(1+D\mathcal K h_L(T))}{\sqrt N}
 =\frac R{\sqrt N},\qquad 1\le p\le6.
\]
The common law of the comparison particles is the prescribed deterministic reference: duality against its smooth linear backward equation identifies it without assuming that the interacting particles have that law. No time derivative bound on the reference, no positive lower bound on diffusivity, and no expectation of a time supremum enter this argument. Thus the constant `R` is independent of `N` and inverse temperature as claimed.

## 3. Residual, diagonal, and bracket coefficients

Direct inclusion-exclusion reproduces both diagonal formulas:
\[
 U_2[\Phi]=\rho^{\otimes2}(\Phi)-N^{-1}\eta(\Phi(x,x)),
\]
\[
 U_3[F]=\rho^{\otimes3}(F)
 -3N^{-1}(\eta\otimes\rho)(F(x,x,y))
 +2N^{-2}\eta(F(x,x,x)).
\]
The triple intersection coefficient is `3-1=2`, and restoring the deleted pair/background diagonals produces `eta tensor rho`, with the indicated sign. These are identities of labels even at coincident coordinates and at `N=2`.

For the averaged six-term kernel `F=C Phi`, its full diagonal vanishes because every summand contains `K(0)`. The derivative bound
\(\|F\|_{C^m}\le d2^m\kappa_m A_{m+1}=G_m\)
includes every Leibniz term; differentiating `K(x-z)` adds signs but no additional derivative-composition coefficient. Symmetrization is an average. In the partial diagonal estimate only the unpaired variable is differentiated, so no repeated-variable trace derivative is needed. Consequently the constructor's exact cubic constant is
\[
 C_3=Q^3G_{3q}R^3+3QG_qR,
 \qquad \mathbb E|U_3[C\Phi_t]|\le C_3N^{-3/2}.
\]
The third absolute moment, rather than a signed cubic expectation, is used. Tonelli yields the stronger time-integrated absolute estimate in THM-010.

The initial pair estimate uses the sharper iid second moment, not the later rough constant `R`, and gives precisely
\[
 I=\tfrac12(Q^2A_{2q}B^2+A_0),\qquad
 \mathbb E|P_N[\Phi_0]|\le I/N.
\]
This retains the generally nonzero iid bias \(-\mu_0^{\otimes2}(\Phi_0)/N\) in `U_2`.

Differentiating the original ordered pair statistic yields \(\nabla_{X_i}P_N=H_i/N\), where
\[
 H_i=\int\nabla_1\Phi(X_i,y)\,d\rho(y)
           -N^{-1}\nabla_1\Phi(X_i,X_i).
\]
The last derivative is the first-slot derivative before diagonal restriction. Both ordered slots contribute, and their factor two cancels the factor one half in `P_N`. Hence the raw Brownian coefficients are exactly
\[
 dM_\Phi=\frac{\sqrt{2/\beta}}N\sum_iH_i\cdot dW_i,
 \quad dM_f=\frac{\sqrt{2/\beta}}N\sum_i\nabla f(X_i)\cdot dW_i.
\]
The pathwise supremum-in-root bound is
\(\max_i|H_i|\le L_\Phi\|\rho\|_{-q}+D_\Phi/N\), with precisely the displayed
\(L_\Phi=\sqrt d QA_{q+1}\), \(D_\Phi=\sqrt d A_1\).
Minkowski gives the second moment with `H=L_Phi R+D_Phi`, and the first moment with the same `H`. Therefore
\[
 \mathbb E[M_\Phi]_T\le\frac{2TH^2}{\beta N^2},\qquad
 \mathbb E\operatorname{TV}_{[0,T]}[M_f,M_\Phi]
 \le\frac{2TL_fH}{\beta N^{3/2}}.
\]
These are absolute estimates under the actual law. Replacing total variation by the absolute terminal covariation is valid.

For the two lower drift contractions, `||rho||TV<=2` and
\(\|B\Phi\|_\infty\le2d\kappa_0A_1\) give respectively
`4 T d kappa_0 A_1/N` and `T d kappa_0 A_1/N`. Their sum is the submitted constant `5 T d kappa_0 A_1/N`.

Finally,
\(\sigma_N^2/\beta=N\min(1,\beta^{-1})\).
The four scaled rates are bounded by constants times
\(N^{-1/2},N^{-1},N^{-1},N^{-1/2}\), respectively, uniformly over positive inverse temperatures. The proof does not assume a limiting temperature. The constructor requires at most
\(3q+1=3\lfloor d/2\rfloor+7\le4d+12\)
derivatives of the pair test and one of the one-body test; every lesser displayed order is covered. Its regularity refinement is valid with the stated fixed-parameter smoothness retained for Itô calculus.

## 4. The independent proof

In falsification (3.2), conditioning is on a comparison particle, not an interacting particle. The `N-1` other comparison particles are then independent with law `mu`. The remaining root-exclusion bias is exactly `-(K*mu)(Y_i)/N` and is retained.

The sixth-moment multiplicity count is exact at the level of label patterns. The `4+2` pattern contributes `15 M(M-1)`, the `3+3` pattern contributes `10 M(M-1)`, and `2+2+2` contributes `15 M(M-1)(M-2)`, in addition to the all-equal term `M`. Thus the coefficient `25` and the upper constant `41` in (3.3) are valid. Summing vector components and adding the bias gives the submitted sufficient constant
\(c_d=2d41^{1/6}+1\).
Exchangeability, Minkowski, and the common-noise displacement inequality then give
\(D_T=c_d\|K\|_\infty T e^{(L_b+2L_K)T}\).

For each Fourier mode, the displacement contribution has Lipschitz factor `2 pi |k|`. The iid complex error can be split into its real and imaginary components, giving the stated `4*41^(1/6)` constant. Thus
\(D'_T=2\pi D_T+4\,41^{1/6}\)
is sufficient in (3.7). Linear Fokker--Planck uniqueness uses
\(\tfrac12\partial_t\|w\|_2^2=-\nu\|\nabla w\|_2^2-\tfrac12\int(\operatorname{div}u)w^2\),
which introduces no inverse diffusivity.

The absolute Fourier-sum argument requires `m>D+j` for a weight of degree `j` in `D` scalar variables. The submitted orders `2d+3`, `3d+4`, and `2d+2` satisfy this strictly for the pair, full cubic, and partial diagonal. The diagonal composition has only a finite derivative-order constant. Hölder uses at most sixth moments. The root-noise estimate takes the spatial supremum before substituting the dependent root particle, so no independence is falsely invoked.

The actual cubic source costs one more pair-test derivative, giving `3d+5<=4d+12`; the root-noise estimate needs `2d+3` pair derivatives. The general all-equal `N^-2` term is harmless at the claimed `N^-3/2` rate, even before using its special vanishing for the actual source. All four estimates in Sections 3--5 therefore follow without an unproved chaos hypothesis or hidden norm assumption.

## 5. Uniform smooth-data qualification

For (D1), differentiate the nondivergence density equation. At order at most `m`, the transport commutator has total multi-index coefficient at most `2^m-1`; the differentiated reaction `(div u)mu` has coefficient at most `2^m`. Summing the `d` vector components and using only probability mass to bound derivatives of `K*mu` gives
\[
 D^+\|\mu_t\|_{C^m}
 \le d(2^{m+1}-1)U_{m+1}\|\mu_t\|_{C^m}.
\]
At a signed maximum of a derivative, nonnegative diffusion has the correct favorable sign. A strict barrier, then a limit, gives the asserted maximum-norm estimate. The stated positive-minimum bound also has the correct reaction sign and factor `d U_1`. No spatially constant-density or incompressible-drift assumption was inserted.

For (D2), the same derivative family for the reversed-time backward equation has commutator constant `d(2^m-1)U_m`. In its response, every external derivative falls on `K(y-x)`; the one derivative of the integrated test is already covered when `m>=1`. Probability mass gives
\(\|Rf\|_{C^m}\le d\kappa_m\|f\|_{C^m}\).
Order preservation of the response is unnecessary. Adding this bound gives exactly the stated `a_m`. The Duhamel existence remark is compatible with the bounded response on that space and the smooth local propagator.

For (D3), (D1) at `m=1` gives the exponent `3d U_2`, hence
\(M_1(t)\le d\|\mu_0\|_{C^1}e^{3dU_2T}=\overline M\).
Substitution in the supplied THM-009 constant gives exactly
\[
 \overline c_m=2d(2^m-1)(b_m+3\kappa_m/2)
              +2(d\kappa_m+\kappa_0\overline M).
\]
The source norm is `d 2^(m+1) kappa_m ||f||C^(m+1)`, so (D2) must, and does, appear at order `m+1`. Integrating the zero-terminal propagator estimate gives the stated `T exp(cbar_m T)` factor. The internal interaction divided by `N` stays in the principal transport; it is never treated as a bounded operator on `C^m`.

At `r=4d+12`, the displayed sum of the three bounds is a permissible common `A`. In particular it uses `h` at order `r+1` for the pair estimate and fixed derivatives of `b,K` at the corresponding displayed orders. The frozen data are smooth, so these are available and independent of temperature. This is within the explicitly stated existing-smooth-solution class; no singular existence theorem or cutoff-uniformity is supplied.

## 6. Diagnostics and the Gibbs obstruction

The free complex pair and triple counts give respectively
\((N-1)/(2N^3)\) and \(6(N)_3/N^6\) for their squared magnitudes. The triple free-heat covariance has exactly three one-label eigenvalues, giving decay `3 q^2/beta` with the diagnostic notation `q=2 pi |k|`. Integrating the two-time covariance gives falsification (6.4), including its factors two and its small/large-temperature limits. The real free-mode constants in coupling (9.2)--(9.4) follow from `E cos^2=1/2`, `E sin^4=3/8`, and the two permitted label-overlap patterns; their cross-density variance is exactly the submitted expression. Actual zero-interaction correctors vanish, and both reports correctly separate that fact from nonzero diagnostic probes.

For moving backgrounds, conditional root exclusion gives the bias `-h(x)/N` and the conditional second moment `(N-1) Var(a(x,Y))/N^2+|h(x)|^2/N^2`. Integrating against the stated one-mode density reproduces (6.8)--(6.9), including the negative cross-bias sign.

For the nonzero one-mode interaction, the mutual-pair drift gives exactly
`-a q^2 (N-1)/N^2` for the initial derivative of the pair mode. The response eigenvalue is `-a q^2/2`, validating the backward solution. The source's diagonal and first-slot diagonal derivative both vanish. Its first projection and exact particle polynomial give the stated pair moment.

For additional verification of the sensitive bracket coefficient, at uniform background the source derivative has conditional variance `5 a^2 q^6/8`, while its projected derivative has squared mean `a^2 q^6/8` after integrating the root. Therefore
\[
 \mathbb E|H_i[J_\phi]|^2
 =\frac{a^2q^6(5N-4)}{8N^2},
\]
which gives exactly the pair bracket `nu a^2 q^6 (5N-4)/(4N^3)` and cross bracket `nu a q^4/(2N^2)`. These are source-probe calculations, not claims that the fixed source equals the actual finite-horizon pair solution.

For the Gibbs claim, direct evaluation of the frozen Hamiltonian gives
\(H_N=a(N|Z_1|^2-1)/2\).
For negative `a`, dropping its additive constant yields exactly the density in (8.1). Translation invariance gives a uniform one-point marginal. On a fixed arc of length `p_delta`, all points have squared empirical mode at least `1-delta/2`. Its product-Haar mass is `p_delta^N`. Comparing this contribution to the partition function with the event `|Z_1|^2<=1-delta` gives
\[
 \mathbb P(|Z_1|^2\le1-\delta)
 \le\exp\{N\log(p_\delta^{-1})-\beta|a|N\delta/4\}.
\]
For any `beta_N` tending to infinity this tends to zero. Hence the pair mode tends to one even after exact first-marginal centering. The `N^-1/2` linear-statistic estimate and the `N^-1` pair estimate cannot be transferred to that preparation. This is a law-class obstruction, not a claim about iid initial data or a singular critical model.

## 7. Recorded defect

**TASK-015-D01 — cosmetic rendering defect; high confidence.**

- Exact location: `MEMORANDA/ROUND_002_FALSIFICATION.md`, physical line 57, first line of equation (2.5); zero-based byte offset 4466.
- Submitted bytes contain `=`, then byte `0x0C` (form feed), then `rac{2}{\\beta N^2}` instead of a literal backslash before `frac`.
- Effect: the first quadratic-variation fraction is not valid mathematical markup and may render incorrectly. No other control character of this kind was found in the four mathematical submissions.
- Mathematical consequence: none after independent verification. Differentiating the original pair statistic gives the factor `2/(beta N^2)` directly, as recorded above; the adjacent cross-bracket formula, later estimates, and independently recomputed diagnostics agree. This is not a patched proof gap.
- Required disposition: a separately identified rendering erratum or corrected presentation copy, preserving the sealed original proof. This reviewer changed no submitted byte and has not audited an erratum outside the supplied dossier.

## 8. Independent computation, verification, and exclusions

The new verifier `VERIFICATION_CODE/round002_hostile_residual_exact.py` imports no constructor code. It constructs the original deleted-label statistics as finite particle Laurent polynomials, differentiates those particle polynomials directly, applies the actual one-mode microscopic generator, and integrates Fourier monomials exactly. It uses rational coefficients and no random seed or floating-point tolerance.

Executed:

```text
python3 VERIFICATION_CODE/round002_hostile_residual_exact.py > VERIFICATION_CODE/round002_hostile_residual_exact_output.json
```

Result: **PASS, 208 exact checks**: 48 constants/iid biases, 12 free complex moments, 32 moving-background brackets, 104 interacting source/correlation checks, and 12 temperature-factor identities. Particle counts are 2, 3, 4, and 6. Angular frequency is normalized to one in the code; the physical frequency powers were checked analytically above. Zero diffusivity is used only as an algebraic diagnostic, not added to the positive-temperature theorem. These finite checks support the proof review but do not replace it.

Both input checksum manifests were verified again at issuance. Created files are this report, its output checksum manifest, the supplemental input manifest, and the independent verifier/output. Canonical ledgers, frozen inputs and submitted proofs were not changed; no workers, commits, pushes, installations, or remote changes were made.

Not reviewed or certified here: the forthcoming finite-dimensional Gaussian criterion; any limiting covariance or CLT; path or field tightness; the root's separate all-order constructor comparison; singular well-posedness; removal of a Riesz cutoff; uniformity in corrector order; long-time or other-preparation extensions; critical power counting; or a Gaussian/non-Gaussian decision in the singular critical regime. The old energy-floor condition and the two microscopic-coupling regimes remain separate.

This report is immutable after its SHA-256 is issued. Any subsequent mathematical correction requires a new report or addendum. Root alone integrates the bounded verdicts and dispositions.
