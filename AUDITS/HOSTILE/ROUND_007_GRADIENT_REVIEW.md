# Round 007 hostile review of the weighted full-pair gradient

2026-09-18 UTC. TASK-052. Reviewer: `/root/r007_gradient_hostile`, isolated Astra Max hostile lane. Worktree: `/Users/matthewrosenzweig/Library/CloudStorage/GoogleDrive-mrosenz2@andrew.cmu.edu/My Drive/Git/fluctuation-correctors-r007-gradient-hostile`. Branch: `codex/hocf-r007-gradient-hostile`. Base: published R6 `3aa91391516f35afe5317a287b4f0e2e93e6384c`.

**Verdict: PASS for the full frozen THM-027 assertion, with one rendering-only note.** The candidate supplies the required off-diagonal first derivatives, their fixed-N bound uniform over the bounded diffusivity interval, and the stated global weak H1 conclusion. I found no failed mathematical line and no counterexample within the frozen range. No hypothesis or exponent range is weakened in this verdict. This is an independent hostile review of the supplied complete proof, not a statement-only reconstruction and not the constructor's self-check.

**First failed mathematical line: none identified.** The literal `|quad(s<d-2)` in candidate line 427 is recorded verbatim in HGR-E01 below. It is not used to conceal an analytic gap, and the sealed candidate has not been edited.

The next particle-domain assertion remains outside this verdict: no N-particle Itô drift, second or time derivative, evolved residual estimate, uniform-N bracket, or critical limiting law is certified here.

## 1. Isolation, exact assertion, and source preflight

Exactly the fifteen files named in `AUDITS/HOSTILE/ROUND_007_GRADIENT_INPUT_SHA256SUMS.txt` were copied from the root and verified against the supplied manifest before review. I read every one of those files in full, including all 562 candidate lines, the complete R4 response proof, the complete R5 pair-potential proof, the conditional inverse proof, and the interface and symmetry clarifications. The task-specific boundary overrides general repository orientation. I did not read TASK-049, a root seed, the constructor's checker, any additional audit, canonical state/history/memory, or R8 work. References to earlier audit files inside the permitted source/constant addendum were not followed or treated as independently checked audit outcomes.

The reviewed candidate is `MEMORANDA/ROUND_007_WEIGHTED_PAIR_GRADIENT.md`, SHA-256 `eb65ed8680416032ca2667db1cab9b39b493fcb1c578985c632a8bbfd1e9953a`. The frozen card is `THEOREMS/THM-027_WEIGHTED_PAIR_GRADIENT.md`, SHA-256 `45a1e5a6b43b9cdebd02513131b41ae8bb1b201dfcf65ff7a0169940d735e108`.

The assertion retains the unit Haar torus, the coefficient-one positive-Fourier Riesz kernel, integer dimension at least three, positive Riesz exponent at most the Coulomb exponent, finite N at least two, finite horizon, and diffusivity in a fixed finite interval including zero. The prescribed density is time-continuous in C2, the ordinary drift is time-continuous in C1, and the test is time-continuous in C3, with their stated uniform bounds. For every exponent strictly between one and half the dimension, the genuine bounded Borel full inverse is C1 off the pair diagonal, has jointly Borel first derivatives with the stated weight bound, and those derivatives are the global weak derivatives of its Haar H1 class. Constants may depend on N but must be uniform in the selected diffusivity. The exact negation is an admissible tuple or exponent violating any one of these conclusions.

The supplied source bridge is sufficient. R4 Section 2, especially lines 69--109 and equations (2.1)--(2.4), derives the positive heat representation, the exact Fourier coefficient, the local power with coefficient one, and a smooth even remainder. Differentiating the Gaussian representation on the two heat-time ranges is integrably dominated on the stated local chart. R4 Section 3 derives the divergence as a finite measure, including the positive Coulomb atom and the exact negative torus compensation. In dimension three at Coulomb, the frozen Fourier coefficient is `1/pi` times the inverse square frequency, so the divergence coefficient is `4*pi`, agreeing with the flux of the coefficient-one kernel. The gamma recurrence below Coulomb also gives the stated coefficient `s(d-2-s)`.

The stronger R7 prescribed-data assumptions meet the R5 existence and source-potential assumptions: the drift's divergence has a finite lower bound from its C1 norm, and C3 test regularity supplies the required C2 bound. R5 Sections 3--6 construct the pair path, prove fixed-start noncollision and absolute source occupation, and give the bounded potential used in candidate (5.11). The coefficient choices in candidate (5.10)--(5.11) agree with that proof under inner radius R, outer radius 2R, and the larger drift remainder bound `U1+H`. The complete response and Volterra proofs provide the actual inverse and its pointwise off-diagonal uniqueness. The symmetry clarification means exchange of slots, not Haar self-adjointness.

No source-potential derivative is imported from heat terminal-data convergence. No external literature result or private input is used in this review. I do not extend this review to the separate iid moment theorem referred to by the prerequisites; it is unnecessary for THM-027.

## 2. Per-claim dispositions

These HGR labels are local review labels, not new canonical campaign identifiers. All line references in this table refer to the sealed R7 candidate.

| Local claim | Location | Verdict | Reason |
|---|---|---|---|
| HGR-01: frozen source and normalizations | 11--75 | PASS | Complete supplied proofs establish the local coefficient, finite-measure divergence, exact inverse, and declared prescribed-data interface. |
| HGR-02: weights and cutoff constants | 79--94 | PASS | The exponential cutoff weight is positive and smooth on the punctured space, equals the exact power near zero, and obeys the required product identity. Other allowed weights have finite comparison constants. |
| HGR-03: one-sided pair Jacobian | 96--122 | PASS | The relative transverse eigenvalue is `2s/N` times the singular power; the negative radial eigenvalue is not replaced by its absolute value. The stated ordinary-drift and annular bounds cover the whole space. |
| HGR-04: repulsion, diffusion, and explicit absorption | 127--191 | PASS | The relative diffusion factor is two, the negative coefficient is `(alpha-p)2s/N`, and the maximization and all annular terms are correct. |
| HGR-05: stopped Feynman--Kac and occupation | 193--216 | PASS | Positivity permits Fatou for the terminal term and monotone passage for occupation; neither boundary killing nor uniform integrability of the stopped weight is assumed. |
| HGR-06: maximal weighted moment | 218--229 | PASS | The level-crossing bound is applied to the doubled parameters, followed by integration of a square-root tail. It requires no unjustified first moment of the supremum of that supermartingale. |
| HGR-07: truncated path supremum | 233--254 | PASS | Both threshold cases are covered, including exploding starts and a supremum exactly equal to the truncation level. Local Lipschitz continuity does not presume common noncollision. |
| HGR-08: high moments, Morrey constant, common local flow | 256--278 | PASS | The spatial dimension is `2d`; the averaging coefficient is correct; Fubini, Fatou, a subsequence, and monotonicity give a common event for each fixed initial time. |
| HGR-09: expectation finite differences and continuity | 280--288 | PASS | A deterministic ball has pointwise-in-start Lp derivative bounds for some p greater than one; segment integration supplies uniformly integrable difference quotients. |
| HGR-10: base propagation | 300--317 | PASS | The higher weight `p*q` supplies the derivative moment. The first-moment estimate and sup contraction give the stated weighted norm bound. |
| HGR-11: source derivatives and source occupation | 319--371 | PASS | Both coordinate derivatives have the right signs and Hessian terms. The source-gradient bound and occupation exponent condition imply the required Lp estimate and first-moment weighted bound. |
| HGR-12: terminal source behavior and zero-order bound | 374--394 | PASS | The source derivative tends to zero locally as the horizon shrinks, and the independent nonnegative barrier supplies the zero-order bound. |
| HGR-13: two colliding convolution singularities | 398--444 | PASS | Separate local integrability of both powers suffices for the weighted bound even when their sum exceeds the dimension. Coulomb is handled as a measure with its atom retained. |
| HGR-14: global weak derivatives | 448--449 | PASS | The bounded function gives a vanishing tube-boundary contribution; the gradient weight is integrable. No trace is assumed. |
| HGR-15: both response derivatives | 451--471 | PASS | Translated products retain the density gradient, density Hessian, and both derivatives of the kernel input. Fubini is justified globally in L1 before pointwise continuity is claimed. |
| HGR-16: response continuity and representatives | 473--501 | PASS | The two singularities are separated locally; a change of variable fixes the moving input singularity. The atom samples the current off-diagonal state. |
| HGR-17: pointwise Volterra differentiation | 503--516 | PASS | Local derivative bounds justify time integration; the factorial series converges in values and locally uniformly in derivatives. The pointwise solution is the unique supplied inverse. |
| HGR-18: constants, H1, terminal representative | 518--536 | PASS | All constituent bounds are finite and uniform over the fixed diffusivity interval; squared-gradient integrability uses exactly `2q<d`. Diagonal changes do not affect the weak class. |
| HGR-19: claimed scope | 538--562 | PASS | The text retains the particle-domain and uniform-N gaps and makes no stronger law or generator claim. |
| HGR-E01: literal rendering token | 427, equation (6.4) | RENDERING NOTE | The token `|quad(s<d-2)` is present verbatim; the finite compensation constant and surrounding conditional formula have an unambiguous mathematical meaning. |

## 3. The load-bearing analytic checks

### 3.1. Jacobian and fixed-N exponential weight

Independently differentiating the principal potential gives the force derivative with radial eigenvalue `-s(s+1)` and transverse eigenvalue `s`, after the common radial factor is removed. The pair block has zero center modes and twice the force derivative divided by N on the difference modes. Thus candidate (2.5) uses the largest eigenvalue, not the operator norm of the Hessian. A nonsymmetric ordinary drift causes no problem: its symmetric part is bounded above by its operator norm. On the cutoff annulus, the chosen L already bounds the entire derivative of K; the reduced cutoff coefficient need not dominate that singular derivative there.

For the local power, direct pair-coordinate differentiation gives

\[
 \frac{(G+p\ell)w_\alpha}{w_\alpha}
 \leq-(\alpha-p)\frac{2s}{N}r^{-s-2}
       +2\nu\alpha(\alpha+2-d)r^{-2}+\alpha L_0+pL.
\]

At three-dimensional Coulomb and any permitted q, the first-moment diffusion coefficient is positive. The negative term has the strictly higher singular order because s is positive. Maximizing the retained positive part gives exactly candidate (3.3); the factor four in its critical point follows from retaining half the negative term. For positive diffusion this can grow as a power of N inside an exponential. That is permitted by THM-027 and cannot be reused as an N-uniform bound.

For fixed starts, stopped Itô is legal on the collision-excluded compact sets. Conditional Fatou makes the nonnegative weighted process a supermartingale. Applying its level-crossing inequality at doubled parameters gives a tail bounded by the initial doubled weight divided by the level. Integrating the square root of this tail gives the factor two in (3.10). This is the required maximal estimate; the proof does not claim an integrable supremum of a generic nonnegative supermartingale itself.

### 3.2. Common nearby-start flow and the Morrey coefficient

The candidate does not infer simultaneous noncollision from a union over uncountably many probability-one events. For a fixed continuous driving path, a start whose untruncated weight supremum is at most m has a collision-excluded compact trajectory through the whole horizon. Continuous dependence for a sufficiently fine cutoff then gives uniform local Lipschitz control of the time-indexed family of weights. This also covers equality with m. If the untruncated supremum exceeds m, a finite pre-lifetime time already has weight greater than m; continuity up to that time makes the truncated supremum identically m in a neighborhood. An exploding start lies in this second case. Hence the truncation is locally Lipschitz for every signal without already assuming the conclusion.

The gradient bound uses the chain rule, the variational estimate, and the finite constant for the derivative of the weight divided by its square. Raising to P and using (3.10) with parameters `(P,2P)` yields exactly (4.3). A measurable almost-everywhere spatial derivative may be chosen by coordinate difference quotients. Local Lipschitz continuity for each path and fixed-start noncollision suffice for Fubini; no random exceptional-start set is discarded without that integration.

To check the averaging coefficient, let n be the pair dimension and average the line-segment fundamental theorem over the ball of radius b centered at x. Interchanging the two radial integrations gives the exact gradient contribution

\[
 \frac{1}{n\omega_n}\int_{B_b(x)}
 \left[1-\left(\frac{|y-x|}{b}\right)^n\right]
 |y-x|^{1-n}|\nabla v(y)|\,dy.
\]

Discarding the bracket bounds this by the kernel used in (4.4). Its conjugate-power integral is the displayed one, with denominator

\[
 n-(n-1)P'=\frac{P-n}{P-1}>0.
\]

The average of the function itself has coefficient `(omega_n*b^n)^(-1/P)`. Thus the stated Morrey constant is correct, including its dimension factor.

Integrating (4.3) on the larger deterministic starting ball bounds the expectation of the sum of the two P-th powers of norms uniformly in m. Fatou makes its liminf finite almost surely. Along a subsequence realizing the finite liminf, the Morrey estimate bounds the supremum of the truncated functions on the smaller ball. Monotonicity in m then bounds every truncation, so no start in that ball can explode. A countable chart cover gives the claimed common event. Its dependence on the fixed initial time and parameter tuple is allowed; the theorem does not need an event common to uncountably many time or diffusivity parameters. Local cutoff uniqueness then gives a C1 flow on compact initial sets through the horizon.

### 3.3. Differentiating the expectations, including the source

The common flow is used before taking finite differences. For terminal F, the higher derivative moment comes from the weight with exponent `p*q`, which is strictly larger than p. On a compact deterministic initial ball the right side is uniformly bounded. The pathwise fundamental theorem expresses every short coordinate difference quotient as an integral of the derivative along a deterministic segment. Jensen and Fubini give the same Lp bound for these quotients. The tail bound of order `K^(1-p)` then proves uniform integrability and expectation differentiation. Applying the identical argument to derivatives at a converging sequence of starts proves their continuity. No expectation of a random local Lipschitz constant is assumed.

For the source, differentiating its complete expression produces both the force-Jacobian term and the Hessian-of-test term in each coordinate. The absolute force-Jacobian norm is correctly used here, after the one-sided growth estimate has already been established elsewhere. The inner source bound is

\[
 |\nabla_{x,y}J|\leq\sqrt2 F_2
 [s(s+2)+2HR^{s+2}]\,r^{-s-1},
\]

and the outer bound uses the stated `2F1*K1+F2*K0`. This verifies (5.5), including the full-pair factor.

The source derivative cannot be treated as bounded terminal data. Candidate (5.6) instead uses the retained occupation term. The condition `alpha+s+2 >= p(s+1)` is the correct inner comparison; the outer contribution is controlled by the terminal weighted estimate integrated in time. Time Jensen produces (5.7). The explicit second-moment choice satisfies both required inequalities, uniformly on every compact initial ball. On the common-flow event the entire source path integral is C1 because all starts in that compact set stay in a common smooth region. Its moment bound therefore justifies (5.8) by the same finite-difference argument. At first moment, `alpha=q` is admissible for every frozen q, and gives (5.9).

When the remaining horizon is h, the second-moment bound for the derivative integral is at most a fixed compact-set constant times `h*(h+constant)`. Its expected absolute value is therefore of order at most the square root of h. At the terminal time the source potential and its derivative are zero. The zero-order source potential is supplied independently by the R5 positive barrier; it is not deduced from this local derivative calculation or from terminal-data heat convergence.

### 3.4. The two singularities and both response derivatives

The convolution proof needs two separate neighborhoods. Near the origin of the convolution kernel, the input weight is separated from its singularity. Near the shifted singularity of the input weight, the convolution kernel has size at most a constant times the separation to the power `-a`. The latter contribution is proportional to

\[
 \rho^{d-a-q}=\rho^{-q}\rho^{d-a}\leq\rho^{-q}.
\]

The inequality uses `a<d` and `rho<1`; it does not require `a+q<d`. Thus the proof remains valid when the convolution itself diverges as the two singularities merge. For example, at three-dimensional Coulomb with q equal to five quarters, the force exponent is two and the near-second-singularity power is minus one quarter. Below Coulomb, taking s equal to one half in dimension three makes the divergence-density exponent five halves, with power minus three quarters for the same q. Both are consistent with the asserted weighted bound and refute an unweighted bounded-convolution shortcut.

The force is locally integrable throughout the frozen range; the sub-Coulomb divergence density has exponent strictly below d. At Coulomb its replacement is the measure `c_d*(delta_0-dz)`. Its total-variation convolution with the weight is exactly `c_d*w_q(z)+c_d*integral(w_q)`, before the stated upper bound. Neither the atom nor the compensation is omitted.

The weak derivative argument first removes a tube around the pair diagonal. Boundedness of F makes the boundary term vanish as its area, and the weight makes the bulk derivative integrable. Multiplication by the C2 density and translation preserve these global weak derivatives. Integrating their full pair L1 norms against the finite measure and the L1 force justifies Fubini in (7.2).

For the first response, the derivative includes the density-gradient times F and density times the full derivative of F, and also the density-Hessian times K times F and the density-gradient contracted with K times the full derivative of F. The second response supplies the exchanged four products. The constants in (7.3)--(7.5) bound these terms without a missing pair-norm factor. At Coulomb the atom yields ordinary multiplication at `(x,y)`, so the derivative also includes the derivative of that density factor. It never evaluates F at `(x,x)` when the output point is off the diagonal.

Pointwise continuity of the derivative is not inferred from L1 weak differentiation alone. The candidate separates fixed small neighborhoods of the two singular locations and shifts the integration variable near the input singularity. This leaves a fixed integrable weight multiplying continuous bounded factors. At the atom one treats the finite local multiplication separately. The resulting continuous weak derivative and continuous response imply the classical derivative locally by mollification. The argument does not need a diagonal trace or continuity at the diagonal.

### 3.5. Volterra series, constants, and weak H1

The iterated response terms are defined by pointwise time integrals of jointly Borel functions. The base and response derivative estimates supply a deterministic local majorant, so line-segment differentiation under those integrals is justified. No Bochner integral in a potentially nonseparable weighted supremum space is needed. On each ordered time simplex, the propagation exponents add over successive intervals, while the response bound contributes its kth power. The simplex volume gives the factorial in (8.1).

The series converges uniformly in values and locally uniformly in derivatives, with a uniform weighted derivative bound. On a compact ball the fundamental theorem therefore passes to the limit and gives a C1 function for each time. The value series is exactly the supplied pointwise Volterra construction, so pointwise uniqueness identifies this representative with the genuine full inverse. Joint Borel derivative measurability also follows from coordinate difference quotients of the resulting jointly Borel C1 function; no separate nonmeasurable version is selected at different times.

Every constant in (8.2) is finite for the frozen parameter tuple and uses the diffusivity only through its prescribed upper bound. The source bound, Jacobian weight, periodic remainders, density derivatives, and fixed annular derivatives all appear explicitly. No polynomial or bounded dependence on N is obtained or claimed.

Finally, applying the tube argument to the bounded inverse identifies its global weak derivative. The square of the chosen weight is exactly the weight with doubled exponent. The strict inequality `2q<d` gives the finite radial integral and the stated H1 estimate. Arbitrary modifications on the pair diagonal do not change the Haar equivalence class or its weak derivative. They do not provide a trace, a diagonal-start dynamics, or a pointwise bound for arbitrarily assigned diagonal values. The terminal function is zero with zero first derivative.

## 4. Independent falsification checks

The independent script is `AUDITS/HOSTILE/ROUND_007_GRADIENT_REVIEW_CHECKS.py`; its results are in the adjacent JSON file. It was written in this isolated lane, without opening or importing the constructor's checker. It uses exact rational automatic differentiation, matrix eigenvector checks, finite Fourier coefficient identities, and elementary exponent calculations. There is no randomness, floating-point tolerance, dependency installation, or simulation. The script supports the algebraic review; the stochastic interchange, common-flow argument, response continuity, and Volterra passage are certified by the prose review above, not by counting arithmetic assertions.

Executed result: **5,468 exact assertions passed under Python 3.9.6**.

| Independent check | Actual scope and outcome |
|---|---|
| Principal potential differentiated with rational jets | Confirms the force sign and complete Jacobian for dimensions 3, 4, 5, 6 and several integer or half-integer exponents. |
| Pair matrix applied to center, radial, and transverse vectors | Confirms zero center modes and the exact signed eigenvalues at N equal to 2, 3, 11. |
| Full pair-coordinate differentiation of the weight | Confirms the factor two in diffusion and internal drift, and the strict negative coefficient for moment weights. |
| Complete local source differentiated directly | Confirms both coordinate derivatives for a cubic test and for principal force with or without a smooth even-potential remainder; constant source tests give zero. These are local jet diagnostics. |
| Exact zero-noise radial trajectory and source integral | Checks the radial solution, radial contraction, transverse expansion, weighted terminal derivative, and anisotropic source derivative at N equal to 2, 3, 17. |
| Dimension-three Coulomb noise and source moments | Confirms that the positive diffusion coefficient remains present at positive noise, vanishes at zero noise, and is compatible with the stated repulsive absorption and source UI choices. |
| Morrey radial averaging and conjugate exponent | Confirms the averaging coefficient and the strict pair-dimension integrability threshold. |
| Two-singularity exponent comparisons | Includes force and sub-Coulomb divergence cases whose exponent sum exceeds d; only the correct weighted comparison is tested. |
| Inhomogeneous one-coordinate Fourier response algebra | Independently compares the original integrated-gradient response with both compensated terms, and then checks all density-gradient/Hessian products in both slots. Dimensionless angle factors are restored equally on the two sides. |
| Coulomb atom and compensation | Confirms the exact zero/nonzero-frequency distinction, both response slots, negative signs, and constant cancellation with nonconstant density. |
| Weak H1 threshold | Checks the strict integrability exponents used in the proof; does not assert failure of the true kernel at an excluded endpoint. |

For the zero-noise local principal model, independent integration gives `r(a)^(s+2)=r(0)^(s+2)+2s(s+2)*a/N`. The transverse derivative is `r(a)/r(0)`, so its weighted ratio is `(r(a)/r(0))^(1-q)`. The source integral for an isotropic quadratic test is `N*(r(a)^2-r(0)^2)/4`; an anisotropic quadratic test adds a genuine angular derivative. These checks are confined to a local solvable model and are not substituted for the periodic candidate's smooth remainder or responses.

The tempting stronger claims fail their diagnostic checks: the absolute Hessian would impose a different coefficient; discarding either Coulomb contribution breaks constants; globally bounded convolution is false in the examples above; and an integrable supremum of the undoubled supermartingale does not follow from its first moment. The candidate does not make these claims.

## 5. Rendering note and exact remaining boundary

**HGR-E01 — rendering only; severity editorial; confidence certain.** Candidate line 427 contains, verbatim,

```text
 \qquad B_D=s(d-2-s)\sup|g_{s+2}-\chi|z|^{-s-2}|quad(s<d-2).
```

The literal text `quad` lacks the control-sequence backslash. The intended spacing before the condition is unambiguous from the definition of the bounded smooth compensation and from (6.5). This review preserves the submitted bytes and records the token; it does not silently edit or replace the constructor's proof. An explicitly issued typographic erratum may correct the separator without a new mathematical argument. No mathematical conclusion depends on treating the letters `quad` as a variable or factor.

There is no strongest corrected theorem to substitute: the frozen THM-027 range passes as written. The next excluded particle-domain line remains substantive. The product of the available force and gradient majorants has exponent `s+1+q`; at Coulomb its radial integral diverges for every permitted q. This is a failure of that crude majorant to prove integrability, not a proof that the actual drift diverges or that cancellation is impossible. The review supplies no singular N-particle Itô passage, second/time derivative, interacting-law residual estimate, uniform-N self/cross bracket, finite critical truncation, or limiting fluctuation law.

No centering, law class, geometry, or normalization is changed. General actual inhomogeneous reference/test regularity is still an assumption outside this task. The explicit homogeneous subcase in the supplied interface proof satisfies the stronger spatial assumptions for smooth terminal data.

## 6. Handoff and verification record

Only the isolated worktree contains new review outputs. The root working files, canonical ledgers, immutable input files, and historical evidence were not edited. No commit, push, merge, dependency installation, author contact, child agent, or external source lookup was performed. Creation of the requested branch/worktree changes Git worktree metadata only.

The input seal enumerates the exact fifteen permitted files. The output seal enumerates this report, the independent script and JSON results, the README, and a copy of the input seal. It excludes itself to avoid a self-referential digest. The report and all reviewed inputs are immutable after issuance of that seal.

Verification commands and results are recorded in `AUDITS/HOSTILE/ROUND_007_GRADIENT_REVIEW_README.md`. They include the independent exact checker, all fifteen input hashes, the output hashes, fixed-base verification, whitespace checks, and a direct artifact hygiene check. No TeX source was edited or created; this task delivers Markdown and exact-check artifacts, and its final handoff contains no mathematical LaTeX. No campaign-wide test or unrelated verifier was run under the restricted dossier boundary.

Root may compare this sealed hostile review with the separate reconstruction and decide canonical disposition. This report itself makes no canonical ledger changes and assigns no canonical audit identifier.
