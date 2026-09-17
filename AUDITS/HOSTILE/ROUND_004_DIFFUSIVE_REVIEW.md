# TASK-035 — sealed hostile review of THM-020

2026-09-17 UTC. Reviewer context: `/root/r004_diffusive_hostile`.
Worktree: `/private/tmp/hocf-r004-hostile-20260917`.
Branch: `codex/hocf-r004-hostile`.
Observed initial HEAD: `52bda5d0d24067b051c6fe9763f2a78e7599e593`.

**Verdict: HOSTILE PASS for the precise THM-020 assertion. First substantive failure: none identified.** The submitted construction proves its bounded local probabilistic realization and the initial iid cutoff diagnostic estimate in the stated range. This is an adversarial full-proof review in a fresh context, not a blind reconstruction and not a verdict on any unseen reconstruction or response work. Root alone assigns canonical theorem and campaign status.

There is one **FAIL for rendering only**, TASK035-E01 below. No mathematical claim has been repaired or silently promoted in order to obtain this verdict. No proof gap requiring a separate construction repair and no false mathematical assertion were identified within the submitted scope.

## 1. Input boundary, assertion, and source preflight

The only mathematical inputs read were the eight files in `AUDITS/ROUND_004_DIFFUSIVE_HOSTILE_INPUT_SHA256SUMS.txt`. That manifest was read with TASK-035 in the root, then its exact listed bytes were copied into the new worktree and independently hashed. The manifest itself has SHA-256

`29f55c027b8a01f2c9ed82275769ac4711db59de85710b542bf78eb7222e71b4`.

The sealed THM-020 proof has SHA-256

`30d9f0c98413335fc56c7cc903cf23aca904bc082ec20412872145a77ff15576`.

The full THM-020 statement and full 450-line diffusion memorandum were read. The governing AGENTS file, frozen Round 001 model, THM-015 and THM-017 statements, and relevant THM-017 proof portions were also inspected. In the latter, the characteristic/source material at lines 9–155 and the cutoff/iid material at lines 256–366 supplied the relevant dependency checks. No other Round 004 proof, worker output, prior review, memory, root notes, root TeX, external paper, or unspecified source was read. The task-specific dossier restriction controls over the generic request in AGENTS to open additional orientation files.

The assertion under review is exactly THM-020: for integer dimension at least three, positive exponent at most dimension minus two, finite particle number at least two, finite nonnegative diffusivity, finite horizon, and a constant real symmetric matrix, the declared punctured Euclidean diffusion admits the specified global realization and source potential, bounded martingale/characteristic uniqueness, uniform radial majorization, killed-annular passage, and separately defined initial iid endpoint. The negation is an admissible tuple or member of a declared class violating any one of those assertions. The assertion is not existence of the campaign's full backward corrector.

The retained coefficients were checked against the frozen model and THM-017: the difference of two independent noises of amplitude `sqrt(2 nu)` has covariance `4 nu I`, hence generator `2 nu Delta`; the relative internal drift is `2s/N`; and the local quadratic test gives source `s r^(-s) theta^T A theta`. THM-017's characteristic integral reproduces the coefficient `N/4`. No Fourier coefficient, logarithmic normalization, equilibrium input, or external singular-SDE existence theorem is used. THM-015's needed iid identity is rederived below, so an earlier candidate label is not treated as certification of a load-bearing input. Brownian continuity and independent increments, smooth localized Itô calculus, and elementary measure/conditional-expectation operations are the declared probabilistic inputs.

## 2. Individual claim verdicts

References in this table are to `MEMORANDA/ROUND_004_DIFFUSIVE_COMPARISON.md` unless another file is named.

| Identifier | Submitted claim and location | Verdict and exact scope |
|---|---|---|
| TASK035-C01 | Coefficients, time direction and normalization, lines 14–38, 60–78 | **PASS.** Noise, generator, drift, source and `N/4` are consistent. The backward source sign is negative. |
| TASK035-C02 | Radial derivatives, superharmonicity and envelope, lines 54–110 | **PASS.** All derivatives are correct, including equality in `d=s+2`. The factor one is uniform in finite diffusivity and annular radii, not a uniform-in-N supremum norm. |
| TASK035-C03 | Conditional classical annular comparison, lines 114–125 | **PASS.** For the explicitly assumed classical class with zero lateral and terminal values. No existence or trace theorem is supplied or needed. |
| TASK035-C04 | Measurable Picard construction and patching, lines 129–159 | **PASS.** Joint Borel dependence and adapted local solutions follow from the displayed estimates and countable patching. Globality is obtained only after C05. |
| TASK035-C05 | Lyapunov identity, exit estimates, noncollision and nonexplosion, lines 163–206 | **PASS.** The explicit maximum and both boundary powers are correct. The conclusion is for each fixed nonzero start; a simultaneous all-starts null set is not asserted. |
| TASK035-C06 | Source integrability and removal of stopping, lines 210–240 | **PASS.** Monotone convergence gives integrability before the signed potential is defined; bounded/dominated convergence gives the exact expectation identity. |
| TASK035-C07 | Borel potential, deterministic-time Markov conditioning and martingale existence, lines 244–280 | **PASS.** A common measurable path functional plus independent future increments suffices. No strong Markov assertion or hidden differentiability is required. |
| TASK035-C08 | Bounded Borel martingale uniqueness and classical identification, lines 282–284 | **PASS.** Terminal expectation gives pointwise uniqueness from every start. Classical identification uses the stated localized Itô hypotheses, boundedness and proved source integrability. |
| TASK035-C09 | Killed-annular class and uniqueness, lines 286–303 | **PASS.** The survival indicator and stopping time are correct. The boundary convention is probabilistic killing, not an asserted continuous Dirichlet trace. |
| TASK035-C10 | Nested annular exhaustion, lines 305–312 | **PASS.** Exit times tend to infinity, and stopped signed integrals converge in L1 by the full integrable absolute source envelope. No derivative convergence is claimed. |
| TASK035-C11 | Zero diffusivity, finite-radius outflow and terminal time, lines 314–320, 434 | **PASS.** The explicit outward characteristic solves the declared finite characteristic class uniquely. No incompatible extra finite-radius boundary condition is imposed. |
| TASK035-C12 | Evenness, Borel periodic diagnostic and diagonal convention, lines 324–338 | **PASS.** Reflection symmetry yields a symmetric kernel. Any finite diagonal assignment is irrelevant under the stated bounded-density laws. |
| TASK035-C13 | Density factor and full iid projections, lines 340–378 | **PASS.** Exactly one density bound is used. Bias and first projection remain present with the frozen `N^2` denominator. Coefficient comparisons include N=2. |
| TASK035-C14 | All-N spatial regimes and endpoint, lines 382–411 | **PASS.** Both core-radius orderings and all three `2s` versus `d` cases work, including zero remaining time. Constants are independent of N, finite diffusivity, temperature and remaining time, with the fixed-data dependence stated. |
| TASK035-C15 | Isotropic strictness and anisotropic short-time source, lines 419–432 | **PASS.** Strict comparison holds for positive diffusivity and positive time. The traceless source is not discarded; the signed short-time passage is justified in L1. |
| TASK035-C16 | Law, geometry and operator exclusions, lines 338, 411, 436–438; THM-020 | **PASS.** No evolved-law, path-supremum, classical existence, full periodic equation, nonlocal response estimate, or hierarchy closure is claimed. |
| TASK035-E01 | Conditional-expectation display D23, line 276 | **FAIL — rendering only.** The source has literal `middle|` rather than the TeX control sequence `\middle|`. The mathematical conditional-expectation statement is explicit at lines 270, 272 and 280–282. This does not fail C07 or change the theorem's scope. |

## 3. Adversarial verification of the load-bearing steps

### Radial calculation, signs, and the boundary dimension

Write `p=s+2`, `c=2sp/N`, and let `R=(r^p+c tau)^(1/p)` be the endpoint radius. The submitted profile is `F=N(R^2-r^2)/4`. Differentiating the endpoint radius directly gives

\[
 F_\tau=sR^{-s},\qquad
 F_r=\frac N2(r^{s+1}R^{-s}-r),
\]

\[
 F_{rr}=\frac N2\big[(s+1)(r/R)^s-s(r/R)^{2s+2}-1\big].
\]

These yield exactly

\[
 -F_\tau+\frac{2s}{N}r^{-s-1}F_r=-sr^{-s},\qquad
 \Delta F=\frac N2\big[(d+s)q^{s/p}-s q^{s/p+1}-d\big].
\]

Thus the backward diffusion term is `+2 nu Delta F`. The derivative of the expression before subtraction of `d` is

\[
 \frac{s}{p}q^{s/p-1}\big[d+s-(2s+2)q\big].
\]

Its bracket is `d-s-2+(2s+2)(1-q)`. It is nonnegative throughout the declared range and strictly positive when `q<1`, even at `d=s+2`. Consequently the Laplacian is strictly negative at every punctured point with positive remaining time, is zero at zero remaining time, and lies between `-Nd/2` and zero. The comparison would lose this argument below the declared dimensional boundary; that excluded range has not been promoted.

Concavity of the power `2/p` gives the finite core envelope. Integrating the decreasing positive characteristic source gives the outer envelope `s tau r^(-s)`. Both hold at every radius, not only in their respective radial regions. The classical annular argument has the correct initial/terminal reversal: after replacing terminal time by remaining time, the difference from the majorant has nonpositive parabolic operator and nonpositive initial/lateral data. Subtraction of a positive multiple of remaining time excludes a positive interior maximum. If differentiability is only interior in time, apply the argument below the top time and then use the assumed continuity. This checks the stated class; it does not construct a classical solution.

### Path construction, fixed-start globality, and source integrability

The cutoff drifts are smooth with compact support away from zero, hence bounded and globally Lipschitz. The factorial Picard bound makes the iterates uniformly Cauchy on every finite path interval; the limit solves the integral equation. The repeated integral inequality proves uniqueness and the displayed dependence estimate. This is a construction and supplies Borel dependence on the initial point and continuous driving path, as well as adaptedness.

The domains `D_m` are nested. For a fixed start one begins with the first domain containing it; the omitted finitely many smaller domains are immaterial. Cutoff solutions agree until the common exit by local uniqueness. Hitting the closed complement of an annulus is a Borel path operation, and evaluation of a stopped continuous path is measurable. The countable patching therefore gives measurable exit times, lifetime, and path coordinates. It does not require choosing arbitrary versions separately for each starting point. The cemetery convention can be fixed on the measurable finite-lifetime event, rather than by an unmeasurable selection of null sets.

For `V=r^2+r^(-eta)`, direct radial differentiation gives exactly D13. With `eta=d-2`, the inverse-power diffusion term vanishes. For the remaining nonconstant part, set

\[
 f(r)=a r^{-s}-b r^{-s-d},\quad
 a=\frac{4s}{N},\quad b=\frac{2s(d-2)}N.
\]

The derivative changes from positive to negative at

\[
 r^d=\frac{(s+d)b}{sa}=\frac{(d-2)(s+d)}{2s}.
\]

Its value there is precisely the second term in D14. It is a genuine global maximum: `f` tends to minus infinity at zero and to zero at infinity. The constant in D14 need not be uniform in diffusivity; its use is only to prove nonexplosion for each fixed tuple.

On a closed annulus the stopped stochastic integrand for `V` is bounded, so its expectation vanishes. Nonnegativity of `V`, continuity at exit, and the inequalities `V(a)>=a^(-(d-2))` and `V(R)>=R^2` give both D16 probabilities. For the nested radii `1/m,m`, their sum tends to zero. The events that all exit times are at most a fixed horizon are precisely the finite-lifetime event at that horizon. Thus the maximal lifetime is infinite almost surely for each fixed start. Continuity then confines each individual path on a finite horizon to some compact annulus. This is sufficient for every ensuing stopping passage; no assertion of strong completeness is needed.

For the profile Itô calculation, the derivatives are bounded on each stopped space-time annulus, including its zero-remaining-time edge. The stochastic integral is again integrable with mean zero. Removing the nonnegative stopped terminal profile gives an increasing sequence of positive source integrals bounded in expectation by `F`. Monotone convergence proves D18, including absolute integrability of the signed source. Only then is the signed potential used.

To recover D19, the stopped terminal profile tends to zero and is dominated by the global finite profile bound; the stopped Laplacian integral is dominated by `Nd tau/2`; and the source integral has the integrable envelope already established. These are separate justified convergence mechanisms. No unlocalized singular Itô identity or convergence of stochastic integrals is asserted in this step.

### Borel martingale and killed classes

The time-integrated positive and negative source parts are measurable functions of remaining time, initial point, and the driving path. Integration against the fixed Brownian path law gives Borel expectations. Their finiteness follows from D18. This proves the asserted pointwise Borel potential, including the measurability needed by the iid diagnostic.

Splitting the integral equation at a deterministic time gives the pathwise flow identity on the nonexploding paths. Independence of future Brownian increments then proves the deterministic-time conditioning statement. For a random starting state, nonexplosion after conditioning is justified because the same Borel path map has probability-one nonexplosion from every deterministic nonzero state. Positive/negative truncation extends the identity from bounded future functionals to the source integrals. For a fixed horizon, those integrals also have a uniform-in-start expectation bound from D18 and D10, so no integrability gap appears at the random state.

D23 consequently is the conditional expectation of a single integrable terminal source integral. Such conditional expectations form a uniformly integrable family. This can be checked directly by truncating the absolute terminal variable: on an event where a conditional expectation has magnitude above `K`, its absolute value is bounded by twice the conditional expectation of the terminal variable's absolute tail above `K/2`. No path regularity of the Borel potential is inferred from this statement.

The uniqueness argument is intentionally in the declared deterministic-time martingale class. At the terminal time the function term is zero; at time zero it equals its prescribed value at the starting point. Taking expectations forces exactly D20 at every starting pair. This excludes exceptional-point alterations because the class is required from every starting point. The argument would not certify an unstated weak PDE class, and none is claimed.

For a bounded classical solution satisfying the stated stopped Itô hypotheses, the localized martingales have a common integrable dominator: the global bound on the solution plus the full absolute source integral. At each fixed time the localizations eventually agree with the unstopped path. The L1 limit therefore preserves conditional expectations. Terminal continuity is used when the localization also approaches terminal time. This verifies the claimed conditional classical identification without importing classical existence.

In the annular class, the indicator is correctly `h<rho`; after killing both the future potential and future source contribution are zero. Splitting the stopped source integral at a deterministic time leaves precisely the indicator times a new killed source integral on the survival event. Equality at the exit time contributes no extra time integral. The killed Markov identity and terminal expectation therefore establish existence and uniqueness in the stated bounded Borel class. This reasoning uses deterministic-time splitting, not a strong Markov theorem. For a classical annular member, localization to smaller closed annuli and the assumed boundary continuity identify the boundary term with zero on exit.

For arbitrary nested annular radii tending to zero and infinity, each finite path interval eventually lies inside the annulus. The positive source integrals increase to the full integral. The signed ones converge almost surely and in L1 because their absolute values are dominated by the full integrable absolute source integral. Thus the stated point/time convergence holds. No spatial uniform convergence, continuous boundary trace, or regularity at collision has been inserted.

### Zero and large diffusivity, isotropy, and terminal behavior

At zero diffusivity the endpoint radius calculation is the complete solvable model. Along its outward characteristic the direction is constant, and source integration gives `U_A=(theta^T A theta)F`. The characteristic class itself supplies the derivative and terminal value, so uniqueness follows by the fundamental theorem for absolutely continuous functions. A finite outer radius is not part of this global forward characteristic problem. An additional arbitrary outflow condition would be a different problem, as the submission states.

For every finite positive diffusivity the favorable Laplacian sign is unchanged, even if the Lyapunov exit constant is large. The theorem does not need estimates uniform in that Lyapunov constant. For `A=I`, the source integral is strictly positive on every positive finite path interval. In D19 the Laplacian integral is strictly negative because remaining time is positive except at the final instant and the path stays punctured. Hence the strict comparison with `F` is valid for every positive diffusivity and positive remaining time. At zero diffusivity equality is recovered. This also checks that the anisotropic transport expression has not simply been reused as a diffusive solution.

For general symmetric `A`, the short-time averages converge pathwise to the source by continuity at the fixed nonzero starting point. The proof correctly handles the possible expectation problem: the positive envelope has expectation at most its starting value, Fatou forces convergence of its expectations, and the minimum identity proves L1 convergence. On the event where that envelope exceeds twice its starting value, the signed error is at most three times the operator norm times the envelope's L1 error. On the complementary event it is bounded and tends to zero. Thus D33 is justified, including a nonzero traceless direction. An angular average is not substituted for the matrix-valued source.

At zero horizon or remaining time, all potentials vanish. The core envelope tends to zero uniformly in the punctured spatial variable for each fixed N, uniformly in diffusivity. Neither a collision trace at positive time nor a time derivative at the terminal collision corner is needed. N=2 and N=3 retain respectively the exact profile factors one half and three quarters and the iid sharp coefficients one sixteenth and one twenty-seventh.

### Diagnostic, density, centering, and all-N norm regimes

Reflection of both the starting point and driving Brownian path preserves the drift equation and the even source. Pathwise uniqueness gives evenness of the expectation. The fixed even cutoff therefore gives a symmetric Borel pair kernel. It is bounded for every finite tuple. With a bounded-density iid law, distinct labels have unequal coordinates almost surely, and the product-law diagonal is null; a finite diagonal assignment changes neither the statistic nor its projections almost surely. This would need a different treatment for atoms, which the diagnostic theorem excludes.

The translated product density is bounded by `M` because one copy of the density is bounded and the other integrates to one. This gives D28 with one density factor. The cutoff merely defines a diagnostic; no full periodic equation is inferred.

The ordered distinct-label sum can be expanded independently using `H=m+q(x)+q(y)+r(x,y)`. Its constant contribution, first projection and canonical pair contribution give exactly D29's displayed decomposition. Conditional zero means make distinct canonical pair terms orthogonal, including pairs sharing one label, and make those terms orthogonal to the first projection. After adding the nonzero squared bias, the three coefficients are

\[
 \frac1{4N^2},\qquad \frac1{N^3},\qquad
 c_N=\frac{N-1}{2N^3}.
\]

In the kernel norm the weights are respectively one, two and one. The coefficient gaps are

\[
 c_N-\frac1{4N^2}=\frac{N-2}{4N^3},\qquad
 2c_N-\frac1{N^3}=\frac{N-2}{N^3}.
\]

They are nonnegative for every N at least two, including equality in both at N=2. The estimate has not discarded mean-field bias or silently changed to exact expectation centering.

For positive remaining time write `ell=(2sp tau/N)^(1/p)` and let `R_1` be the fixed cutoff radius. If `ell<=R_1`, the core is bounded by a constant times `N^2 ell^(d+4)`, while the exterior is bounded by a constant times `tau^2 integral_ell^R_1 r^(d-1-2s) dr`. This gives the three displayed rows. The all-N case `ell>R_1` also checks directly:

- If `2s<d`, the everywhere-valid outer envelope alone gives a constant times `tau^2`. Equivalently, the actual core-ball bound is `N^2 ell^4 R_1^d=(2sp)^2 tau^2 ell^(-2s)R_1^d`, which is at most a fixed constant times `tau^2` when `ell>R_1`.
- If `2s=d`, the core-ball bound is at most `N^2 ell^(d+4)=(2sp)^2 tau^2`, agreeing with the zero logarithmic positive part.
- If `2s>d`, the core-ball bound is again at most `N^2 ell^(d+4)`, which equals a fixed coefficient times `N^((2s-d)/p) tau^((d+4)/p)`.

These are checks of the estimates already present at lines 382–396, including the first-row alternative explicitly stated there; no new hypothesis or patched estimate is needed. Multiplication by the iid coefficient costs at most `b_N/N`. In the logarithmic row, `tau^2 log_+(1/tau)` stays bounded on a fixed finite horizon and vanishes at zero. The last N exponent becomes exactly `-(d+2-s)/(s+2)`, which is negative throughout the declared range. The density may vary with parameters under one common bound. All quantifiers in the claimed uniform endpoint are therefore preserved.

The supremum is outside the expectation. The result supplies L2, L1 and probability negligibility for deterministic remaining-time choices, but supplies neither a stochastic path supremum nor an evolved-law estimate. The check does not transfer the zero-diffusion two-sided orders to positive diffusivity.

## 4. Rendering finding and corrected scope

TASK035-E01 has low severity and certain textual confidence. Line 276 uses `\,middle|\,` inside a conditional-expectation display. A future editorial erratum can replace that token by `\,\middle|\,`; this audit does not edit the submitted proof. The surrounding equations and prose state the conditional-expectation identity unambiguously, so this is a rendering defect, not a missing probabilistic argument or a false statement.

No mathematical claim failed, so no reduced or corrected mathematical scope is required. The strongest certified scope remains exactly the submitted local bounded-martingale/characteristic assertion and its initial iid diagnostic endpoint. In particular this report does not add classical existence, strong completeness, strong Markov statements, boundary regularity, two-sided diffusive norm estimates, evolved interacting laws, nonlocal responses, or full corrector closure.

## 5. Independent exact checks and sealed handoff

`AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_EXACT_CHECK.py` was written in this fresh review context. It uses only Python standard-library integer and `fractions.Fraction` arithmetic. There is no floating-point tolerance, random seed, stochastic sampling, numerical convergence extrapolation, or external dependency. Direct endpoint-radius chain-rule expressions are compared with the submitted radial identities; independently differentiated radial Lyapunov expressions are compared with D13; and finite iid configurations are enumerated directly from the frozen ordered sum.

Executed command:

`python3 AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_EXACT_CHECK.py`

Outcome: **PASS**, exit code zero. The saved output reports 2,520 radial/time/barrier tuples, including 1,680 positive-time strict Laplacian cases; 7,560 Lyapunov tuples; 24 iid kernel/N cases containing 2,160 exact finite configurations; and 70 scaling tuples covering all three spatial regimes. Radial N values include 2 and 3, dimensions run from 3 through 10, and rational exponents are filtered by the exact declared range. Diffusivity test values include zero and `10^12`. The iid checks use masses `1/2,1/3,1/6`, retain spatial coincidences of distinct labels, and test zero, constant, separable, canonical, mixed and general symmetric kernels. These are supplementary finite checks; the all-parameter and stochastic assertions are assessed in the analytical review above.

Final integrity commands and outcomes:

- Both input manifests were verified with SHA-256: **PASS**.
- The exact checker was rerun and its stdout saved to `AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_EXACT_CHECK.txt`: **PASS**, exit code zero.
- `git diff --check`: **PASS**. A separate check of created text files found no trailing whitespace or non-tab/newline control characters, and every file ends with a newline.
- `AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_REVIEW_SHA256SUMS.txt` was generated after the report and companion files were final and verified: **PASS**. The manifest excludes itself to avoid a circular digest.

Created output files are this report, the exact checker, its exact stdout, `AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_REVIEW_INPUT_SHA256SUMS.txt`, and `AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_REVIEW_SHA256SUMS.txt`. The input manifest includes the eight source files and the original supplied input manifest. All copied input bytes remain unchanged. No root canonical file, submitted theorem/proof, ledger, prior audit, historical input or TeX file was edited. No commit, push, dependency installation, child worker or external communication occurred. No TeX compilation is applicable to these Markdown and standard-library checker outputs.

The report is sealed on issuance; any later substantive correction must be a new superseding audit. Root may import these exact output files, verify their hashes, compare this verdict with the separately commissioned reconstruction, and assign the canonical audit status. The unseen reconstruction and the full operator/response mission remain outside this verdict.
