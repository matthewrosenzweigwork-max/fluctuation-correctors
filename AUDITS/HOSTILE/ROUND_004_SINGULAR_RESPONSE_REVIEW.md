# TASK-038: hostile review of the Round 004 singular response module

2026-09-17 UTC. Reviewer: fresh worker `/root/r004_response_hostile`, requested Astra Max role. Audit mode: full-proof hostile review. Verdict: **HOSTILE_REVIEW_PASS** for the submitted assertions, under their stated hypotheses and exclusions. No substantive mathematical failure was found. This report does **not** confer an isolated-reconstruction pass, a singular propagator theorem, or a fluctuation theorem.

## 1. Frozen input, isolation, and exact scope

The candidate is `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, SHA-256
`135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be`.
The inspected copy has 541 lines; all source locations below refer to that exact copy. It states the conjunction at lines 13–63 and the conditional smooth-cutoff conclusions in section 6. Its negation is an admissible instance contradicting one of those stated conclusions. Claims explicitly excluded by the candidate are not inserted into that conjunction.

The worktree was created from published commit
`52bda5d0d24067b051c6fe9763f2a78e7599e593`, on branch
`codex/hocf-r004-response-hostile`, at
`/var/folders/yh/pqv2cz6539gc8j2cm154bcrr0000gn/T/hocf-r004-response-hostile-t6cv8gmv`.
The root checkout already contained unrelated modifications and untracked material. The fourteen files listed in the sealed dossier and their manifest were copied into the review worktree; every source hash was checked before copying and every copied hash checked afterwards. No root file was edited.

The root input manifest is `AUDITS/ROUND_004_RESPONSE_HOSTILE_INPUT_SHA256SUMS.txt`, SHA-256
`53bc1a29507011ed0e7719740e459d6d200a91fac5602e481b853fdfaf5c2d5c`.
The review input manifest, which additionally binds that root manifest, is
`AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_REVIEW_INPUT_SHA256SUMS.txt`, SHA-256
`3e9e2787fcbee48a25621e5553ecacd852c3986ffef0c65b2d6c1290a1417ef2`.

The reviewer read the task and manifest first, then the permitted administrative instructions, frozen model, candidate, R1 response definitions and smooth-equation convention, R3 local heat representation, and THM-015 statement. The R3 iid and sharp-iid files were searched only to locate the candidate's identified prerequisites. Their probabilistic proofs were not used. The candidate's local heat argument was checked directly against the frozen Fourier definition, rather than accepted because an older report asserted it.

No unsealed R4/R5 proof, root conditional full-inverse memorandum, other review, memory, constructor checker, or constructor checkpoint was read. No external source or dependency was introduced. The restricted task's isolation instructions govern this review in place of first-launch instructions to read unrelated canonical ledgers. Canonical updates are reserved to the root.

This reviewer received and read the full candidate proof before conducting the hostile checks. Consequently this is a separate full-proof hostile review, **not blind reconstruction**. The finite checker below was independently written in this review context without access to the constructor's checker. Its finite tests are supporting evidence, not a proof of infinite-dimensional estimates.

## 2. Claim-by-claim verdicts

The identifiers in this table are local to TASK-038 and do not allocate new shared theorem or audit identifiers.

| Claim | Submitted location | Verdict | Decisive check |
|---|---|---|---|
| C01. Frozen Fourier normalization and coefficient-one local heat representation | 13–20, 69–109 | **PASS** | Gaussian unfolding, Gamma integral, and both small- and large-time derivative bounds give precisely the stated constant and smooth local remainder. |
| C02. Integrable odd representative of the distributional negative gradient | 113–120 | **PASS** | The gradient boundary term is of order $r^{d-1-s}$, which vanishes throughout the stated range; $s+1<d$. |
| C03. Distributional divergence and punctured-domain boundary sign | 122–134 | **PASS** | The inner normal is negative radial, producing the positive flux in (3.2), with no omitted endpoint term. |
| C04. Below-Coulomb density, compensation, finite variation and lower bound | 138–171 | **PASS** | The Gamma ratio is $s(d-2-s)$; the local singular density is integrable, and its globally compensated representative is bounded below. |
| C05. Coulomb atom, exact constant torus compensation and total variation | 175–196 | **PASS** | The nonzero Fourier coefficients equal the positive atomic coefficient, while the zero coefficient is zero. The constant negative background and variation $2c_d$ follow. |
| C06. Pointwise bounded-Borel response operators | 34–58, 200–206 | **PASS** | Parameter integrals are Borel and bounded against finite variation and the integrable vector field. |
| C07. Haar $L^2$ and $L^\infty$ classes; uniqueness only where asserted | 208–234 | **PASS** | Translation invariance and Fubini remove all dependence on product-null modifications, including for the atom. Smooth density supplies the unique $L^2$ extension. |
| C08. Original gradient response, two factors, constants and pair symmetry | 236–262 | **PASS** | The $C^1$ product test is justified; the atom acts by multiplication, each response has coefficient one, and the sum commutes with slot exchange. |
| C09. Named heat regularization, bounds, lower divergence and outer-convolution identity | 264–302 | **PASS** | Positivity preserves the bounds, and direct change of variables gives (5.4) with convolution outside the full response. |
| C10. Operator-norm convergence below Coulomb | 304–315 | **PASS** | Both kernels in the difference converge in $L^1$, giving (5.5) uniformly over the stated background class. |
| C11. Coulomb strong convergence and exact time/input quantifiers | 317–368 | **PASS** | The multiplication commutator is retained; the heat first moment yields (5.8). Fixed inputs and compact families of inputs have the claimed uniformity. |
| C12. Coulomb counterexamples to stronger operator and Borel conclusions | 475–505 | **PASS** | High frequencies give exact difference norm $2c_d$; the pair-diagonal indicator gives failure of pointwise and supremum convergence. |
| C13. Smooth pair construction and Markov/Haar extension | 372–437 | **PASS** | At each fixed cutoff, additive-noise subtraction gives a globally defined smooth spatial flow. Its Jacobian bound permits the Haar quotient extension. |
| C14. Pair divergence, mean-field lower bound and propagation exponent | 389–449 | **PASS** | Both pair divergences have the same sign. Jacobian change of variables and the half-energy identity both give the norm-bound exponent $a+\kappa/N$. |
| C15. Conditional smooth-cutoff bounded-response mild equation | 451–469 | **PASS** | Joint strong propagation continuity, norm-continuous responses and supplied $L^1_tL^2$ forcing justify the Volterra series and estimate. |
| C16. Fourier and smooth-pair diagnostic calculations | 475–516 | **PASS** | Direct mode selection and exact cosine moments reproduce the signs, factors and constant-input cancellations. |
| C17. Haar/iid interface and exclusions | 522–539 | **PASS** | The one-way weighted-norm inequality is elementary. The report retains all stated singular-limit, forcing, law-class and fluctuation gaps. |

**First substantive failure:** none within C01–C17. No corrected mathematical candidate or silent repair is needed for those conclusions.

There is one non-substantive transcription defect: line 456, equation (6.8), prints `\big],dr` where `\big]\,dr` is intended. The interval, integrand and integration variable are unambiguous. This has no effect on C15. The submitted source was not edited.

The retrospective statement at line 518 that the constructor ran 133 checks, and the file-seal assertions at line 541, are outside this mathematical verdict: the referenced checker and checkpoint were not included in the permitted input manifest. This review does not certify that execution history. It supplies its own sealed exact checks instead.

## 3. Load-bearing recomputations

### 3.1. Heat normalization, boundary terms and compensation

Write $\alpha=(d-s)/2$. Integrating the nonzero Gaussian Fourier mode in time gives

\[
 A_{d,s}\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d}.
\]

In the whole-space integral, the substitution $v=|z|^2/(4t)$ leaves the prefactor

\[
 A_{d,s}(4\pi)^{-d/2}4^{s/2}\Gamma(s/2)=1.
\]

The subtraction giving the local remainder is legitimate at the origin as well: for small time every nonzero lattice translate is separated uniformly from the ball of radius $1/3$, and its differentiated Gaussian is bounded by a power of time times an exponentially decaying factor. The subtracted constant is integrable because $\alpha>0$. At large time the whole-space contribution is bounded by an integrable multiple of $t^{-s/2-1}$; all spatial derivatives remain integrable. This establishes the actual smooth remainder required later. No global Euclidean power is imposed on the torus.

For $K_{\rm sing}=s z|z|^{-s-2}$, the Cartesian derivative sum away from zero is

\[
 \sum_i\partial_i(s z_i|z|^{-s-2})
 =s[d-(s+2)]|z|^{-s-2}.
\]

In integration by parts over the punctured torus, the negative inner normal makes the term subtracted from the boundary integral positive:

\[
 -\int_{\partial B_r}\psi K\cdot(-z/r)\,dS
 =s r^{d-s-2}\int_{\mathbb S^{d-1}}\psi(r\theta)\,dS(\theta)
   +O_\psi(r^{d-1}).
\]

The exponent is strictly positive below Coulomb, and zero exactly at Coulomb. This independently recovers the vanishing flux in the first case and the positive atom in the second. The preceding gradient integration by parts has a different boundary exponent, $d-1-s$, which is also strictly positive at Coulomb. Thus the existence of the integrable gradient does not discard the later divergence atom.

Below Coulomb, the ratio of the Fourier constants is

\[
 \frac{4\pi^2 c_{d,s}}{c_{d,s+2}}
 =4\frac{\Gamma((d-s)/2)}{\Gamma((d-s-2)/2)}
   \frac{\Gamma((s+2)/2)}{\Gamma(s/2)}
 =s(d-s-2).
\]

The local positive singular density has integral over the radius-$R$ ball equal to

\[
 s(d-s-2)|\mathbb S^{d-1}|
 \frac{R^{d-s-2}}{d-s-2}
 =s|\mathbb S^{d-1}|R^{d-s-2},
\]

so the compensating density has precisely the negative mass in (3.4). The bounded remainder near the origin, smoothness away from it, and compactness outside a small ball prove the finite lower bound. Both proposed choices of $\kappa$ are finite and valid. There is no claim of nonnegative divergence on the entire torus.

At Coulomb the flux coefficient, Fourier coefficient and Gamma form agree:

\[
 (d-2)|\mathbb S^{d-1}|
 =\frac{4\pi^{d/2}}{\Gamma((d-2)/2)}
 =4\pi^2c_{d,d-2}.
\]

The zero Fourier coefficient vanishes, forcing $D=c_d(\delta_0-dx)$ for this exact frozen kernel. Atomic and Haar parts are mutually singular, so the variation is $2c_d$. The local coefficient alone would not determine a constant compensating density after a smooth perturbation; the candidate explicitly distinguishes this point at lines 192–194. The endpoint has positive exponent because $d\geq3$; no logarithmic normalization is inferred.

### 3.2. Representatives, response signs and heat convergence

For a product-null set $E$, translation invariance gives

\[
 \int |D|(dw)\int \mathbf1_E(x+w,y)\,dx\,dy=0.
\]

This is the decisive null-set argument. It uses finite variation and Haar invariance, not absolute continuity of $D$. In particular an atom at $w=0$ samples the already existing pair value $\Phi(x,y)$; it does not restrict that class to $x=y$. Absolute finiteness almost everywhere and the $L^2$ estimate follow by the same Fubini calculation and Cauchy–Schwarz against $|D|$. The $K\cdot\nabla\mu$ term is bounded using the Euclidean vector norm; no extra dimension factor is missing. The pointwise $B_b$ construction and the Haar quotient are correctly treated as distinct objects.

The gradient identity follows by applying distributional integration by parts to $\mu(z)\Phi(z,y)$, with the $C^1$ test approximation justified by the finite variation and integrable field. The signs can be checked without that integration by parts. At Coulomb, use an input mode of frequency $k$, a background mode of frequency $m$, and put $n=k+m$. Normalize the response coefficient by $c_d$. For $n\ne0$, the original gradient formula gives

\[
 -\frac{k\cdot n}{|n|^2},
\]

whereas the two transferred-derivative terms give

\[
 -1+\frac{m\cdot n}{|n|^2}
 =-\frac{k\cdot n}{|n|^2}.
\]

For $n=0$, both coefficients are zero. This simultaneously checks the sign, background-gradient cancellation, and zero-mode compensation. Real finite combinations can be chosen with admissible positive backgrounds $1+q\cos(2\pi m\cdot z)$, $|q|<1$. Both slots have coefficient one by the frozen R1 equations (3.1)–(3.3); there is no additional response half-factor.

Convolving the translated measure or integrable vector field in its displacement variable and changing variables yields exactly $R_{x,\varepsilon}=P_\varepsilon^xR_x$. All integrals are absolutely justified on bounded Borel inputs. The common background remains inside the entire outer convolution. Below Coulomb, the difference estimate follows directly from two $L^1$ approximation errors, giving operator-norm convergence even on $B_b$.

At Coulomb, the singular part of the difference is $-c_d(P_\varepsilon^x-I)M_\mu$. Writing this as multiplication times the heat error requires the commutator. Its norm is at most

\[
 M_1\|\Phi\|_2\int\operatorname{dist}(w,0)p_\varepsilon(w)\,dw
 \leq M_1\sqrt{2d\varepsilon}\,\|\Phi\|_2.
\]

The estimate is uniform over all backgrounds having the same supremum and gradient bounds. The remaining kernel difference is controlled in $L^1$, so no continuity modulus of the gradient is needed. A compact set of $L^2$ inputs permits a finite-net argument; a merely bounded set does not. If the background is itself mollified, its derivative approximation is a separate requirement, exactly as stated at lines 361–368.

For Haar background the pair difference has multiplier

\[
 c_d\left(2-e^{-4\pi^2\varepsilon|k|^2}
             -e^{-4\pi^2\varepsilon|\ell|^2}\right).
\]

Its supremum is $2c_d$ for every positive cutoff, also on symmetric real kernels using $k=\ell$. It is therefore false to read the strong convergence as uniform on the unit ball. Separately, the Borel input $\mathbf1_{\{x=y\}}$ is zero in Haar $L^2$, but its unregularized pointwise response at Coulomb is the stated diagonal multiplication; every smooth-cutoff response is pointwise zero. The claimed Borel obstruction is valid and does not contradict equivalence-class well-definedness.

### 3.3. Smooth pair propagation and the conditional mild equation

The pair drift is a vector field on the product torus. Differentiating its second component changes both the sign of the vector field and the sign of the displacement derivative. Consequently

\[
 \operatorname{div}_{x,y}b
 =\operatorname{div}u(x)+\operatorname{div}u(y)
   +\frac2N D_\varepsilon(x-y)
 \geq -2a-2\kappa/N.
\]

The measure lower bound is preserved by positive heat convolution. For the stated mean-field velocity, convolving against a nonnegative mass-one density gives the additional lower bound $-\kappa$, as asserted; no derivative of the density or high cutoff derivative is required for this estimate.

At fixed cutoff all spatial derivatives required for the flow exist and are bounded. Subtracting an additive continuous noise path leaves a globally Lipschitz time-dependent ODE. Its spatial derivative solves the differentiated ODE and its positive Jacobian has lower bound

\[
 J_{s,t}\geq \exp\left(-2\int_s^t(a+\kappa/N)\right).
\]

For every fixed path, change of variables bounds the squared Haar norm of pullback by the reciprocal lower Jacobian bound. Jensen retains this bound after noise averaging. Taking the square root gives exactly the exponent in (6.6), not twice that exponent. The energy identity independently gives

\[
 \tfrac12\partial_\tau\|v\|_2^2
 =-\nu\|\nabla v\|_2^2
   -\tfrac12\int\operatorname{div}b\,|v|^2
 \leq (a+\kappa/N)\|v\|_2^2.
\]

This is a norm **upper-bound exponent**, not an assertion of equality for every regularized Riesz flow. Diffusion may improve the norm. Nonautonomous time reversal changes $s$ to $t-\tau$, as used in the candidate, and produces no sign change in the displayed generator. Flow continuity and boundedness extend the propagator strongly to Haar $L^2$. The same smooth flow construction gives joint continuity in its two time endpoints; this supports the mild integral. Oddness of the regularized kernel and exchange invariance of the Brownian law preserve pair symmetry.

A further exact smooth diagnostic is $K(z)=\sin(2\pi z_1)e_1$, with zero external velocity and diffusivity. For the relative angle $\theta=2\pi(x_1-y_1)$,

\[
 \dot\theta=\frac{4\pi}{N}\sin\theta.
\]

At the equilibrium angle $\theta=\pi$, the flow Jacobian is exactly $\exp(-4\pi(t-s)/N)$. The sum of the two first coordinates is conserved modulo one, and all remaining coordinates are unchanged. Since the divergence is bounded below by $-4\pi/N$ and this value is attained along that orbit, the pure-transport $L^2$ norm is exactly $\exp(2\pi(t-s)/N)$. Continuity of the Jacobian makes its minimum also its essential infimum, justifying this equality of operator norms. This independently tests both the factor two and the square root in the general estimate. Exact cosine moments also recover the energy computation (7.3) for both signs of its amplitude.

For the perturbation, denote $L(r)=a(r)+\kappa/N$. A sequence of local propagators along ordered response times has product bound $\exp(\int_s^t L)$, because the adjacent time intervals partition the full interval. The $n$-fold response norm integral is bounded by $(\int_s^t C_R)^n/n!$. The free forcing term is continuous in $L^2$ under the stated integrability: split off the short interval and use dominated convergence on the remaining interval with joint strong continuity. The response is norm-continuous as a function of its $C^1$ background. These facts justify the convergent Volterra series, uniqueness by the same factorial bound, and the forcing exponent in (6.9).

This construction uses only supplied $L^1_tL^2$ forcing. It does not prove that any actual campaign forcing has this property. Nor does strong convergence of bounded responses prove convergence of the unbounded pair drift or of cutoff-dependent solutions. The candidate retains these exclusions explicitly.

## 4. Independent exact checks and reproducibility

The review wrote and executed:

```text
python3 AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_EXACT_CHECK.py > AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_EXACT_CHECK.txt
```

Outcome: exit code zero, **346 exact checks passed**, on Python 3.9.6, macOS 26.6.2 arm64. The code uses only the Python standard library, rational arithmetic, exact half-integer Gamma evaluations as monomials in $\pi$, mode selection, and exact cosine moments. There is no numerical tolerance, random seed, dependency installation or floating-point Gamma evaluation. Computational status is **REPRODUCED**, with the execution separate from the constructor's reported run.

The tests cover integer dimensions 3 through 12 for Fourier/local and Coulomb constants; every applicable integer sub-Coulomb exponent in those dimensions; representative rational radial exponents; twenty-five inhomogeneous Coulomb mode pairs including zero output modes; exact heat multipliers; both signs of smooth-pair amplitudes at particle numbers 2, 3 and 5; and the Jacobian-to-norm factor. The finite checks do not certify the general analytic limits or a singular semigroup.

Checker SHA-256: `afe613f2b7711a14919a87a40bcd98301730cca5ef535292d80fd4ec438b3392`.
Output SHA-256: `6ea3ea64030e96139545644a91f52149559186697c35da46860683be92f27c3e`.

The source hashes were checked before and after dossier copying, and the input and output seals are checked at issuance. No submitted source was edited, no TeX was changed, and no TeX build is applicable to this requested Markdown audit. The campaign-wide verifier was not run because it would consume unrelated, excluded campaign state. No commit, push, dependency change, canonical-ledger edit or child worker was used.

## 5. Disposition and handoff

The submitted finite-measure response theorem, its heat-approximation statements, the smooth-cutoff propagation estimate, and the conditional smooth-cutoff mild equation receive **HOSTILE_REVIEW_PASS**. There is no substantive defect to repair in the reviewed assertions. The only identified source edit would be the explicitly recorded differential-spacing typo; any change would be a new source version and is left to the root.

The candidate remains limited to the unit Haar torus, positive-power exponents with $d\geq3$ and $0<s\leq d-2$, $C^1$ nonnegative probability backgrounds, and the explicitly assumed smooth local velocities. Constants are uniform only under the common stated bounds. No uniformity as the dimension, exponent or horizon varies is inferred.

The review does not grant a same-constant bound on a vanishing-density weighted $L^2$ space, a pair-diagonal trace, a singular particle/pair flow, convergence of cutoff propagators, singular full-corrector existence, actual forcing membership, martingale convergence, an evolved-law estimate, or subcritical/critical fluctuation closure. The elementary interface $\|\Phi\|_{L^2(\mu\otimes\mu)}\leq M_0\|\Phi\|_{L^2(dx\,dy)}$ is valid, but does not supply a probability-law transfer.

For a proposed singular full-response theorem, the first new obligation remains construction or convergence of the singular local pair propagator and control of the actual forcing/cutoff-dependent inputs. It is not settled by this response audit. A separate withheld-proof reconstruction is also still required for the campaign's stronger audit gate; this review cannot substitute for it.

Created audit deliverables are this report, its input manifest, the independent checker, the recorded checker output, and `AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_REVIEW_SHA256SUMS.txt`. The output manifest binds all four preceding audit files, and omits its own hash to avoid self-reference. The copied candidate and task dossier are preserved separately under their input seal. Root alone should allocate shared audit identifiers and update canonical records. The bounded review ends at this seal.
