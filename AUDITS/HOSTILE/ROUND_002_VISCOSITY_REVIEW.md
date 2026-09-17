# TASK-020: hostile review of smooth diffusivity and covariance limits

Issued 2026-09-17 UTC by `/root/capacity`, Astra Max, in `/private/tmp/hocf-round002-hostile-20260917`. Baseline HEAD: `a06178658d1e3d458536ff312ca793947212ec67`. This report is immutable on issuance and separate from both earlier residual and Gaussian reviews.

**Verdict: PASS for the submitted fixed-smooth diffusivity-continuity theorem and its stated covariance identification.** No mathematical or cosmetic defect was found in THM-013 or its 459-line proof. The characteristic construction supplies the inviscid reference, the response Volterra equation supplies its full backward tests, and the explicit comparison estimates identify the covariance left conditional at zero diffusivity in THM-011. Positive-diffusivity smooth mean-field existence remains the declared model assumption. The particle conclusion also retains the reviewed Gaussian theorem's pair/residual requirements. No singular result or complete M3 gate is certified.

## Independence, chronology, and inputs

This context's prior work comprised an operational configuration inquiry, a sealed blind reconstruction of the smooth all-order algebra, the TASK-015 residual review, and the TASK-017 Gaussian review. It did not participate in the present PDE/covariance construction. The Gaussian review was sealed at SHA-256 `81e6fc21db22b9284072a60e0ce9474596f6325d7fa2f785e3a03af90414e13f` and that hash was sent to root before any present-dossier file was read. Thus this is a separate independent hostile review of the new construction, using already reviewed prerequisites; it is not a claim that the entire context was mathematically blank. No power-counting dossier or other worktree was read.

The complete task, theorem card, and proof were read. The supplied `AUDITS/ROUND_002_VISCOSITY_INPUT_SHA256SUMS.txt` has SHA-256 `6f06a3aab119aaa2c972f4ab5bfba25db7c070a16bfcdd4ae9962db85ac58ddb` and seals:

| Input | SHA-256 |
|---|---|
| `TASKS/ACTIVE/TASK-020_ROUND002_VISCOSITY_REVIEW.md` | `6508f927b4d52d0021c606dc836b6424d30e54d81518a30a3ed73927a260af1b` |
| `THEOREMS/THM-013_SMOOTH_DIFFUSIVITY_LIMIT.md` | `059905d0fcb2b16839634a7b72faf64ae7da969008b32e501f2f1f615453acc7` |
| `MEMORANDA/ROUND_002_VISCOSITY_LIMIT.md` | `700eed5dc912f4f6e621f01009ed60d5f4b479adb478ce06b8b974442e6afe2f` |

The new `AUDITS/ROUND_002_VISCOSITY_ADDITIONAL_INPUT_SHA256SUMS.txt` identifies the nine permitted prerequisites actually used: frozen model, PO-001, THM-008, THM-011, root smooth-data qualification, the residual and Gaussian constructions, and their two sealed hostile reviews. All candidate and prerequisite hashes were verified. The known rendering defect in the older residual proof remains covered only by the previous residual review; no old proof, erratum, or issued verdict was repaired or amended here.

## Per-result verdicts

Physical line numbers refer to the sealed viscosity memorandum.

| Result | Location | Verdict | Scope checked |
|---|---|---|---|
| V-01: statement and existence boundary | lines 11–49; theorem card | PASS | Every finite spatial order; nonnegative diffusivities; fixed smooth data; positive-diffusivity reference existence assumed. |
| V-02: global inviscid characteristic fixed point | lines 51–64, (2.1) | PASS | Periodic lift, correct Lipschitz constant, consecutive finite time intervals, uniqueness. |
| V-03: smooth positive inviscid pushforward | lines 66–89, (2.2)–(2.4) | PASS | Smooth velocity is obtained before assuming density smoothness; invertible flow and Jacobian formula justify the density and uniqueness. |
| V-04: maximum-norm transport and density bounds | lines 91–128, (3.1)–(3.4) | PASS | All multi-index and vector-component factors; positive lower barrier; no inverse diffusivity. |
| V-05: response integration by parts | lines 130–148, (3.5)–(3.6) | PASS | Correct sign, output derivative location, mass and density-gradient terms. |
| V-06: full backward Volterra construction | lines 150–185, (3.7)–(3.10) | PASS | Correct backward sign, factorial convergence, uniqueness, all finite derivative orders, inhomogeneous norm bound. |
| V-07: density parameter difference and explicit constant | lines 189–235, (4.1)–(4.5) | PASS | Both density products, Laplacian sign, two-derivative loss and all constants. |
| V-08: full backward difference and explicit constant | lines 237–279, (5.1)–(5.5) | PASS | Transport and response differences both retained; response comparison needs only the density's supremum difference. |
| V-09: covariance continuity | lines 281–331, (6.1)–(6.5) | PASS | Lipschitz prefactors, initial covariance subtraction, changing density and both gradients, unequal-time overlap. |
| V-10: finite positive and infinite inverse-temperature limits | lines 333–355, (6.6)–(6.7) | PASS | Identified full backward limiting kernels, including the constructed inviscid ones. |
| V-11: vanishing inverse temperature and subsequences | lines 357–365 | PASS | Uses the prior high-temperature argument, not an infinite-diffusivity application of the finite-parameter comparison; oscillating sequences remain qualified. |
| V-12: free heat and derivative-loss tests | lines 367–393, (7.1)–(7.3) | PASS | Either parameter may be zero; the varying-data counterexample has the asserted scale. |
| V-13: signed one-mode and removable resonance tests | lines 395–447, (7.4)–(7.9) | PASS | Response sign and factor, both interaction signs, parameter bound and every covariance factor. |
| V-14: compatibility and scope | lines 187, 331, 365, 449–459; card | PASS | Compatible with the earlier root qualification and Gaussian review; no pair-at-zero, singular, growing-list or field assertion is inferred. |

There are no new defect identifiers. These V-labels are report-local and do not allocate canonical campaign identifiers.

## Characteristic construction and the absence of a regularity circle

For continuous periodic displacements `h`, write `F(x)=x+h(x)` as a lift. The integral vector field in (2.1) is defined on the entire displacement Banach space: periodicity makes every interaction independent of choices of representatives. Its difference for two displacements is bounded by `(L_b+2L_K)||F-G||_infinity`, since both particle arguments vary. Its speed is bounded by the fixed Euclidean supremum norms of `b` and `K`. Picard is a contraction for a sufficiently short time interval, and the same constants apply after any intermediate time. No spatial derivative can obstruct continuation of this continuous fixed point to a prescribed finite horizon.

For the obtained continuous `F`, pushforward of the initial probability measure gives a probability measure before any density regularity is known. Nevertheless

\[
 u_t(x)=b(x)+\int K(x-F_t(y))\mu_0(y)dy
\]

is smooth in `x`, continuous in time at every fixed derivative order, and satisfies the displayed componentwise derivative bounds `||u_t||_(C^j) <= U_j`. This follows directly from bounded derivatives of the fixed smooth kernel and dominated convergence against a probability measure. The already constructed `F` solves the ordinary nonautonomous flow equation for this velocity. Difference quotients in its initial position give (2.2); repeated differentiation gives a linear equation for each highest derivative with lower derivatives already controlled. Finite-horizon Gronwall induction yields all spatial derivatives. Solving the prescribed-velocity ODE backwards gives a smooth inverse, and the determinant equation gives (2.3). The change-of-variables formula then yields exactly (2.4), with strict positivity. Thus smoothness of the density was not assumed to obtain the velocity smoothness that proves it.

Differentiating a smooth test along the flow gives the inviscid continuity equation. Conversely any smooth solution with the same initial density is the pushforward by its own characteristic flow, and that flow must satisfy the same unique integral fixed point. This proves inviscid uniqueness. It does not purport to prove the assumed positive-diffusivity mean-field existence.

## Maximum-norm constants and the response propagator

Use the submitted maximum norm over all componentwise derivatives of total order at most `m`. For each multi-index `alpha`, the nonzero subindices in the transport commutator have total binomial weight `2^|alpha|-1 <= 2^m-1`. Their derivatives of the transported function have order at most `m`; summing velocity components costs exactly the displayed factor `d`. Hence

\[
 \|[\partial^\alpha,u\cdot\nabla]h\|_\infty
 \le d(2^m-1)U_m\|h\|_{C^m}=p_m\|h\|_{C^m}.
\]

The density reaction term contributes at most `d 2^m U_(m+1)||mu||_(C^m)` by Leibniz. Taking the maximum over the finite derivative family introduces no extra count: each signed derivative has its forcing bounded by the same family maximum, so the first-contact argument gives the upper Dini inequality. Diffusion has a favorable sign at its contact point for every nonnegative diffusivity, including zero. This verifies

\[
 M_m=\|\mu_0\|_{C^m}
 \exp\{T[p_m+d2^mU_{m+1}]\}.
\]

At `m=0` the transport commutator vanishes. The positive barrier `(inf mu_0) exp(-d U_1 t)` follows from the same reaction bound, so using the probability mass and positivity in later estimates is justified for the constructed zero-diffusivity member and for the existing positive-diffusivity family.

Integration by parts in the response input gives

\[
 R_\mu f(y)=-\sum_j\int f(z)
 \big[(\partial_jK_j)(z-y)\mu(z)+K_j(z-y)\partial_j\mu(z)\big]dz.
\]

There is no boundary term on the torus. All derivatives in `y` fall on `K`; they do not differentiate `f` or `mu`. Probability mass bounds the first term by `d K_(m+1)||f||_infinity`, and `sum_j ||partial_j mu||_(L1) <= d M_1` bounds the second by `d K_m M_1||f||_infinity`. This verifies precisely `r_m=d(K_(m+1)+K_m M_1)`, including `m=0`. It is a bounded linear response estimate and requires no order preservation.

The local backward transport or transport-diffusion propagator obeys `||P_(t,s) h||_(C^m) <= exp(p_m(s-t))||h||_(C^m)` by the same finite-family maximum argument. At zero diffusivity it is the characteristic composition. At positive diffusivity it can be constructed by the additive-noise SDE with this already specified smooth velocity: pathwise Picard after subtracting the Brownian translation gives a global trajectory, and the bounded velocity derivatives control its initial-position derivatives. Taking expectation gives the local propagator; Itô's formula and its composition property give the local backward equation. This constructs the linear propagator without adding an assertion about existence of the nonlinear positive-diffusivity reference.

For the equation `partial_t f + A f = -R f`, zero-diffusivity variation of constants has the plus sign in (3.7). The n-response time-ordered integral has volume `(t_a-t)^n/n!`, transport norms multiply to `exp(p_m(t_a-t))`, and the n response factors each cost at most `r_m`. Thus (3.8) is exact as a sufficient norm bound, the series converges in every finite `C^m`, and the same Volterra estimate gives uniqueness. Uniqueness at the lower orders makes the constructions compatible, so differentiation of the series at higher orders justifies the smooth full backward solution. Summation gives `F_m=phi_m exp(T(p_m+r_m))`. With a zero terminal value the inhomogeneous formula has a minus sign before its forcing integral; taking its norm removes this sign and gives the stated (3.10).

## Recomputed parameter comparisons

Put `delta=mu^nu-mu^nu'` and `v=K*delta`. Subtracting the divergence-form equations, then expressing the principal part with `u^nu` and `nu`, gives

\[
 \partial_t\delta+u^\nu\cdot\nabla\delta-\nu\Delta\delta
 =-(\operatorname{div}u^\nu)\delta
  -v\cdot\nabla\mu^{\nu'}-(\operatorname{div}v)\mu^{\nu'}
  +(\nu-\nu')\Delta\mu^{\nu'}.
\]

This is the submitted (4.1), with a positive diffusivity-difference forcing in the forward equation. Since the torus volume is one, `||delta||_(L1) <= ||delta||_infinity`. Differentiating the convolution on its kernel gives `||v||_(C^m) <= K_m ||delta||_infinity` and `||div v||_(C^m) <= d K_(m+1)||delta||_infinity`. The two resulting products cost

\[
 d2^m(K_mM_{m+1}+K_{m+1}M_m)\|\delta\|_\infty.
\]

The first density reaction contributes `d2^m U_(m+1)||delta||_(C^m)`, the transport commutator contributes `p_m||delta||_(C^m)`, and the Laplacian forcing costs `d |nu-nu'| M_(m+2)`. Thus the exact sufficient Gronwall coefficient is the submitted

\[
 h_m=p_m+d2^mU_{m+1}
     +d2^m(K_mM_{m+1}+K_{m+1}M_m),
\]

and the zero initial difference gives

\[
 \sup_{t\le T}\|\delta_t\|_{C^m}
 \le dTM_{m+2}e^{h_mT}|\nu-\nu'|.
\]

No choice of ordering between the parameters was made and no diffusivity was divided out. The homogeneous version proves uniqueness in the existing smooth probability-solution class, consistently with the characteristic uniqueness at zero. The two additional density derivatives are used explicitly in the Laplacian forcing. In terms of raw data, computing `M_(m+2)` also uses the additional displayed smooth drift/kernel norms; these are not silently included in a density-only constant.

For the backward difference `w=f^nu-f^nu'`, subtracting the two full equations gives

\[
 (\partial_t+A^\nu+R_{\mu^\nu})w
 =-(\nu-\nu')\Delta f^{\nu'}
  -(K*\delta)\cdot\nabla f^{\nu'}
  -(R_{\mu^\nu}-R_{\mu^{\nu'}})f^{\nu'},
 \qquad w(t_a)=0.
\]

The diffusivity forcing is negative in this backward comparison, as in the candidate. Both density changes are present. For their response difference, use the original, unintegrated form

\[
 (R_{\mu^\nu}-R_{\mu^{\nu'}})f^{\nu'}(y)
 =\int K(z-y)\cdot\nabla f^{\nu'}(z)\delta(z)dz.
\]

The output derivatives fall on `K`, giving the correct bound `d K_m F_1 ||delta||_infinity` without a derivative of `delta`. The transport product has bound `d 2^m K_m F_(m+1)||delta||_infinity`. The Laplacian costs `d |nu-nu'| F_(m+2)`. Using the already proved density comparison only at order zero bounds the entire forcing by (5.4). Integrating the inhomogeneous estimate gives exactly

\[
 C_{f,m}=dT e^{(p_m+r_m)T}
 \big[F_{m+2}+K_m(2^mF_{m+1}+F_1)C_{\mu,0}\big].
\]

This verifies every factor in (5.5). The comparison needs two additional backward spatial derivatives and only two density derivatives for `C_(mu,0)`. At covariance level, order zero for the density and order one for the tests are enough; the corresponding order-two density and order-three backward bounds are available within `r=4d+12`. If the finite bounds are used rather than recomputed from smooth data, the requirement `m+2 <= r` is retained. No positive lower diffusivity bound occurs.

## Covariance identification and compatibility

The prefactors `vartheta(nu)=1` up to one and `1/nu` thereafter, and `chi(nu)=min(1,nu)`, are each globally one-Lipschitz and bounded by one. At zero, their values are one and zero. Thus they extend precisely the two Gaussian theorem prefactors. In this fixed-data model the deterministic reference and full one-body backward equations have no separate N-dependence; the pair equation's explicit N-dependence does not enter these two covariance matrices.

For the initial covariance, subtracting both the product expectation and the product of means bounds its change by `2F_0(||f_a^nu-f_a^nu'||_infinity+||f_b^nu-f_b^nu'||_infinity)`. The covariance itself is bounded in absolute value by `F_0^2` using Cauchy–Schwarz. For the dynamical integrand, changing the density with the gradients held fixed costs `d F_1^2 ||delta||_infinity`. Changing one gradient at a time with the other density held fixed costs `d F_1` times the sum of the two `C^1` differences. This recomputes (6.4), including both gradient terms and the probability-mass normalization.

For example, one sufficient explicit constant for the sum of the two entrywise covariance differences in (6.5) is

\[
 F_0^2+4F_0C_{f,0}
 +2Td\big[F_1^2+F_1^2C_{\mu,0}+2F_1C_{f,1}\big].
\]

This is a direct expansion of the submitted dependencies, not a repair. The fixed overlap interval ends at `min(t_a,t_b)` and introduces no time-jump term. Positive semidefiniteness is retained because the expressions are initial covariances and space-time gradient Gram matrices with nonnegative prefactors.

It follows that when the inverse temperature tends to a finite positive value, its diffusivity tends to a finite positive parameter and both matrices converge to the full reference/backward matrices at that parameter. When the inverse temperature tends to infinity, the diffusivity tends to zero: the constructed inviscid backward tests are the uniform limits, the initial covariance has the submitted identified value, and the dynamical covariance tends to zero. The previous Gaussian criterion therefore applies whenever its pair/residual hypotheses hold. This closes the particular covariance-identification condition left open in the prior Gaussian dossier; it does not retroactively change that earlier report's conditional wording.

When the inverse temperature tends to zero, the diffusivity tends to infinity. The candidate correctly uses the separately reviewed backward-energy and actual-law arguments for this endpoint, not a finite-parameter compactness argument. Extended-interval subsequences can be extracted after the map `beta -> beta/(1+beta)`. Each convergent-parameter subsequence is identified, but different accumulation parameters can still produce different limiting laws.

Compatibility with the root qualification is direct. Its density exponent is `d(2^(m+1)-1)U_(m+1)`, while the present exponent is `d(2^m-1)U_m+d2^m U_(m+1)`, which is no larger. Its one-body estimate for `m>=1` uses the original response form and can be sharper; the present integration-by-parts bound also covers `m=0` and is still valid. The root's separately reviewed pair bound supplies a uniform pair norm for fixed smooth data within the existing smooth class; this memorandum neither reproves it nor transfers it to a singular family. A zero-diffusivity pair kernel is unnecessary to identify the one-body covariance and is not asserted to exist here as a consequence of the covariance proof.

## Recomputed solvable diagnostics

For zero interaction and confinement, the heat formulas hold also at zero diffusivity. For a fixed time separation `h`, differentiating the heat semigroup in its diffusivity parameter gives `h Delta exp(nu h Delta)`. Commutation with every spatial derivative and the supremum contraction give `dT` times the `C^(m+2)` input norm as the parameter-Lipschitz constant. This verifies (7.2)–(7.3) with either endpoint parameter zero and no inverse diffusivity.

For the varying-data example `phi_n=n^(-m) cos(2 pi n x)` and diffusivities `n^(-2)` and zero, the `C^m` input norms are bounded by `(2 pi)^m`. At fixed positive separation `h`, the supremum of the mth derivative of the solution difference is exactly

\[
 (2\pi)^m(1-e^{-4\pi^2h}),
\]

whereas the parameter difference tends to zero. Thus a uniform Lipschitz constant depending only on the `C^m` data bound is impossible. This is a family of changing terminal data and does not refute the theorem for fixed smooth data. The proof makes no claim of an optimized fractional-regularity threshold.

For the signed interaction `g=a cos(qx)`, `q=2pi`, uniform reference and zero confinement, directly compute

\[
 R\cos(qy)=\int aq\sin(q(z-y))(-q\sin(qz))dz
          =-\frac{aq^2}{2}\cos(qy).
\]

The full local-plus-response eigenvalue is therefore `-q^2(nu+a/2)`. Solving the scalar terminal ODE gives exactly (7.5), including the sign of `a/2`. Differentiation in `nu` gives a factor `q^2(t_a-t)`; the `C^m` cosine norm is `q^m`, and the growth for all nonnegative diffusivities is bounded by `exp(|a|q^2T/2)`. This reproduces (7.6) for both interaction signs.

With `gamma=q^2(nu+a/2)` and `h=min(t_a,t_b)`, the Haar cosine variance is one half and the mean squared derivative is `q^2/2`. These give

\[
 I^{ab}(\nu)=\frac{\vartheta(\nu)}2e^{-\gamma(t_a+t_b)},\qquad
 D^{ab}(\nu)=\chi(\nu)q^2
          \int_0^h e^{-\gamma(t_a+t_b-2r)}dr.
\]

For nonzero `gamma`, integration gives the submitted coefficient `chi(nu)/(2nu+a)` multiplying the difference of exponentials. At `2nu+a=0`, the integrand is identically one, so the value is exactly `chi(nu)q^2 h`; taking the limit of the quotient gives the same value because the numerator has first term `2gamma h`. In particular the apparent denominator is removable, including for the attractive sign. Negative `gamma` causes finite-horizon growth, not a sign error in the covariance. At zero diffusivity `chi(0)=0` and the initial entry is exactly `exp(-a q^2(t_a+t_b)/2)/2`. The same formulas cover zero, equal, and unequal terminal times. These are analytic recomputations; no numerical approximation is used as evidence for the theorem.

## Defects, limits, and verification record

Mathematical defects: none found within the stated scope. Cosmetic defects: none found in the new card or proof; nonprinting-control-character, terminal-newline, trailing-whitespace and display-delimiter checks passed. No submitted bytes were repaired. No external theorem or unverified literature assertion was used in reaching the verdict.

The assumptions remain fixed smooth periodic fields, a smooth positive fixed initial probability density, a finite horizon and finite fixed terminal list. Positive-diffusivity reference existence is assumed; its uniqueness and bounds are proved within that class, while zero-diffusivity existence is constructed. Constants depend on the displayed smooth derivative norms and can diverge along a singular regularization. For `0<s<d`, the cited critical growth of inverse temperature tends to infinity, but using the result with one fixed smooth interaction is only a diagnostic and yields no singular critical theorem. No field/path tightness, growing list, cutoff removal, law-class transfer, critical truncation, logarithmic normalization, or whole-M3 conclusion follows.

Commands and checks in the assigned worktree:

- `shasum -a 256 -c AUDITS/ROUND_002_VISCOSITY_INPUT_SHA256SUMS.txt`: all three submitted inputs OK on receipt and final seal.
- `shasum -a 256 -c AUDITS/ROUND_002_VISCOSITY_ADDITIONAL_INPUT_SHA256SUMS.txt`: all nine permitted prerequisite hashes OK.
- `shasum -a 256 -c AUDITS/HOSTILE/ROUND_002_GAUSSIAN_REVIEW_SHA256SUMS.txt`: both previously sealed outputs OK. The prior residual report hash was also preserved and verified in the supplementary manifest.
- `python3 scripts/verify_campaign.py`: `CAMPAIGN VERIFICATION PASSED`; this is repository-integrity verification, not mathematical certification.
- `git diff --check`: passed. New output files were separately scanned for trailing whitespace, terminal newlines, control characters and paired display delimiters before sealing.
- Complete line-numbered proof/card reads and the analytic recomputations above checked the mathematical assertions. No new script, numerical experiment, package installation, or external source was needed.

New outputs are this report, `AUDITS/ROUND_002_VISCOSITY_ADDITIONAL_INPUT_SHA256SUMS.txt`, and the adjacent `ROUND_002_VISCOSITY_REVIEW_SHA256SUMS.txt`. The adjacent seal records the report's final hash and the supplementary manifest hash. No candidate, previously sealed review, canonical ledger, historical input, or TeX artifact was modified. No commit, push, remote operation, dependency installation, or child-agent spawn occurred. Root alone integrates this separate verdict and decides canonical promotion.
