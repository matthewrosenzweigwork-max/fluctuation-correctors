# AUD052 — full hostile review of the Round 016 source extension

TASK081. Issued 2026-09-18 UTC by `/root/r016_source_hostile`, the assigned fresh Max hostile reviewer. Frozen candidate: `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md`, SHA-256 `62fc121556fa2cb08f0ec3e2c7d1813f40bce6a86a2f5ea07ed2d616c6ce9a26`. Frozen theorem: THM-038, SHA-256 `257260a31d299f2d22d38deb0aea4add7b183b739d83d1031705d5d31f9982cb`.

**Verdict: PASS for the entire frozen THM-038 assertion and the stronger mathematical assertions reviewed below.** I found no first failed mathematical line and no admissible counterexample. No range, source, centering, noise, endpoint, or terminal-test repair is required. This is an isolated hostile review of the disclosed construction, not the withheld blind reconstruction and not a promotion of the complete earlier modules. Root alone compares the two gates and assigns canonical status.

The decisive mechanism is valid: the actual law has nonpositive expected interaction energy; an exact decomposition expresses that energy as two nonnegative quantities minus the retained self term and the discarded mass; a uniform Fourier commutator controls the retained source and a positive heat-kernel estimate controls the absolute discarded source. The argument never estimates a source square. Its use of a deterministic splitting scale follows, and is separate from, the fixed-particle singular-process limit.

## 1. Scope, negation, isolation, and source preflight

The audited quantifiers are every fixed integer \(d\ge3\), \(0<s\le d-2\), finite \(T\ge0\), finite \(\nu_*\ge0\), and one arbitrary fixed smooth real periodic terminal test \(h\). For every \(N\ge2\) and \(0\le\nu\le\nu_*\), the particles start iid Haar independently of their Brownian drivers, have zero external drift, interact with coefficient \(1/N\), and have noise \(\sqrt{2\nu}\). The unit torus has Haar mass one and characters \(e^{2\pi i k\cdot x}\). The kernel has exactly the frozen coefficient-one Riesz normalization. No logarithmic interpretation is admitted.

The backward test is the actual frozen Fourier multiplier, including its unchanged constant mode. The source is \(J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y))\) off the diagonal. The statistic has ordered distinct labels, denominator \(N^2\), and the three coefficients \(1/(2N^2)\), \(-1/N\), \(1/2\) in its empirical, mixed, and Haar terms. The claim is

\[
 \sup_{0\le t\le T}\mathbb E|P_N[J_t](X_t)|\le C N^{s/d-1},
 \qquad
 \sqrt{Nb}\,\mathbb E\int_0^T|P_N[J_t](X_t)|dt
 \le C\sqrt b\,N^{s/d-1/2},
\]

with genuine integrability and a constant independent of the chosen \(N,\nu,t\). Here \(b=\min(1/\nu,1)\) for positive noise and \(b=1\) at zero noise. The exact negation requires an admitted fixed datum violating integrability or the existence of that common constant. A generic exchangeable law, an \(N\)-dependent terminal test, failure of an unrelated square estimate, and absence of scaled decay above its stated range are not negations.

The task and its input manifest were read first. The prescribed worktree `/Users/matthewrosenzweig/.codex/worktrees/hocf-r016-source-hostile` was created on `codex/hocf-r016-source-hostile` from published `072cab684b9ce41855ead6c48f435c8fc184ec35`. Exactly eleven allowlisted files were copied and checked against the frozen SHA-256 manifest before mathematical reading. Every input was checked again before packet sealing. The task-specific isolation restrictions supersede the generic instructions to inspect state, history, the general README, orchestration files, or other source material.

The candidate was intentionally read in full before this hostile review. The first long display had a truncation around its splitting definitions; those exact lines were reread separately. There was no claim of blindness to the candidate. Ambient exposure consisted of the supplied global/project instructions, tool/skill metadata, the high-level memory summary already in the prompt, and the short subject printed by the worktree command. No memory file was opened or used. Earlier permitted reports contain historical references, statuses, and checker summaries; none supplied a mathematical premise and no referenced non-allowlisted file was opened. The full declaration is in `ROUND_016_SOURCE_HOSTILE_ARTIFACTS/EXPOSURE.md`.

| Allowlisted input | Exact use and source limitations |
|---|---|
| `AGENTS.md` | Mathematical discipline and isolation. No status assertion imported. |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Model, Fourier coefficient, noise, ordered/deleted convention, and source centering. Read in full. |
| `MEMORANDA/ROUND_001_ALGEBRA.md`, lines 1–188 | Smooth source convention, response sign, the half, and original background contractions. The singular diagonal convention is not imported from the smooth identity. |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, lines 65–196 | Heat representation, local coefficient, gradient integrability, the exact divergence measure and its lower bound. Recomputed in Section 3 below. |
| `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md` | Full earlier finite-particle card read. Its issued OPEN/UNAUDITED status is neither altered nor used as proof. |
| `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, lines 80–544 | Full-energy stopping, actual noncollision, measurable realization, same-noise heat passage, and finite-particle density domination. Only the needed homogeneous specializations are verified here; the entire earlier theorem is not certified. |
| `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, lines 76–235 and 442–496 | Smooth free energy and lower-bounded Fatou mechanism, exact self subtraction, and the initial weak-generator mechanism. The full report's other statements remain conditional as issued and are not imported. |
| `THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md` | Full frozen assertion and exact negation; no scope alteration. |
| `TASKS/ACTIVE/TASK-081_ROUND016_SOURCE_EXTENSION_HOSTILE.md` | Assignment, eleven-file allowlist, output restrictions, sealed handoff. |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md`, lines 1–544 | Entire intentional hostile-review target, including stronger assertions and limitations. Its previous checker and reported checker count were not inspected or used as evidence. |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION_ARTIFACTS/EXPOSURE.md` | Constructor exposure declaration, read as a declaration only. Its account of external actions was not independently forensically certified. |

The companion source preflight records all eleven digests and read ranges. No external source, literature theorem number, private source, prior checker, current blind output, R11–R15 proof/audit, state/history, root scratch/R17 work, or child agent was used. Basic Gaussian integration, finite Fourier algebra, local Picard iteration, smooth stopped Itô calculus, compact-torus change of variables, and elementary convergence theorems are reconstructed with their relevant bounds below.

## 2. Per-claim verdicts, including stronger claims

These verdicts concern the precise statements in the frozen candidate, not any extrapolation from their names. Confidence is high on each mathematical PASS, supported by the calculations below.

| ID | Candidate location | Claim | Verdict and retained scope |
|---|---|---|---|
| AUD052-C01 | 11–59 | Entire frozen assertion and exact negation are preserved | PASS; all parameters and original source terms match the card. |
| AUD052-C02 | 81–109 | Heat representation, coefficient one, smooth local remainder, finite lower bound, integrable force | PASS for every admitted \(s\); no \(s=0\) substitution. |
| AUD052-C03 | 111–139 | Exact divergence, lower bound and heat convolution through Coulomb | PASS; the atom and compensating Haar part both remain. |
| AUD052-C04 | 143–174 | Finite-particle noncollision, uniqueness, measurable realization, stopped energy and exact \(2/N\) Laplacian factor | PASS for the homogeneous model actually used; per-start probability-one scope is correct. |
| AUD052-C05 | 176 | Same-noise full heat-family path convergence | PASS at fixed \(N,\nu,T\); local constants may depend on the path, and no uniform rate is used. |
| AUD052-C06 | 178–193 | Density bound \(F_t\le e^{(N-1)\kappa t}\), including zero noise | PASS; explicitly finite-\(N\), used for the initial derivative only. |
| AUD052-C07 | 195–232 | Smooth free-energy identity; actual expected-energy sign and absolute pair moment; one-body Haar law | PASS; positive-noise Fatou and zero-noise decrease are separate. No singular dissipation equality or higher-marginal independence follows. |
| AUD052-C08 | 236–288 | Positive splitting, finite mass, positive retained coefficients, \(C^2\) regularity, retained self bound | PASS for the entire real exponent range. Integer-exponent tests are diagnostics only. |
| AUD052-C09 | 290–306 | Exact energy self/background identity and simultaneous actual expectation bounds for both positive pieces | PASS; both subtraction coefficients are correct. |
| AUD052-C10 | 310–338 | Original Haar contractions; exact backward-test seminorms; genuine source integrability | PASS for arbitrary fixed smooth \(h\), with a finite explicit Fourier seminorm. |
| AUD052-C11 | 342–370 | Uniform logarithmic derivative and lattice multiplier inequality | PASS, independently recomputed. Constants are independent of splitting scale. |
| AUD052-C12 | 372–403 | Full-product/Fourier identity for the retained source and deterministic commutator bound for any smooth vector field | PASS; only the retained smooth source receives its zero diagonal, and the zero Fourier mode of the signed measure is zero. |
| AUD052-C13 | 407–431 | Remainder gradient in Haar \(L^1\); absolute pointwise domination by \(Q_{2r}\) | PASS. This is positive-kernel domination, not positivity of an arbitrary weighted energy. |
| AUD052-C14 | 433–469 | All source contractions, full uniform source estimate, time integrability, scaling, zero noise, and edge cases | PASS for the whole card; bounded/growing scaled upper bounds are retained when appropriate. |
| AUD052-C15 | 473–487 | Actual fixed-\(N\) initial variance derivative, for every noise including zero and at Coulomb | PASS; singular generator integrability and the one-sided derivative at zero are justified. No uniform Taylor remainder or later-time sign is claimed. |
| AUD052-C16 | 489–498 | Constant test, \(T=0\), actual \(N=2\) relative dynamics, near-collision starts, and possible source-square failure at \(s\ge d/2\) | PASS; an explicit admissible fixed test establishes the square failure without contradicting the \(L^1\) theorem. |
| AUD052-C17 | 500–528 | Constructor's reported diagnostic count and historical execution account | NOT USED AS EVIDENCE. The prior checker was forbidden and not opened; fresh diagnostics are supplied here. |
| AUD052-C18 | 531–544 | Earlier full-module statuses and excluded corrector/hierarchy conclusions remain unchanged | PASS as the scope of this mathematical review. Canonical integration and the withheld reconstruction belong to root. |

No issue requires an implemented mathematical repair. In particular, the explanations below are recomputations of lines already present, not missing hypotheses silently supplied to make the theorem true. No first failed line exists in this review. The first boundary outside this audit is the theorem card's express exclusion of inverse/corrector/cubic/bracket/hierarchy/fluctuation conclusions; no such conclusion is licensed by this PASS.

## 3. Kernel and particle reconstruction

Put \(\alpha=(d-s)/2\ge1\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). Unfolding the periodized Gaussian gives its mass one and nonzero Fourier coefficient \(e^{-4\pi^2u|k|^2}\). The integral \(A\int_0^\infty u^{\alpha-1}(p_u-1)du\) converges in Haar \(L^1\): the small-time norm is at most \(2Au^{\alpha-1}\), and at large time the mean-zero heat kernel decays exponentially. Its coefficient is

\[
 A\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d}.
\]

For the central Euclidean Gaussian, substituting \(w=|z|^2/(4u)\) gives

\[
 A(4\pi)^{-d/2}\int_0^\infty u^{-s/2-1}e^{-|z|^2/(4u)}du
 =|z|^{-s}.
\]

Near zero the other lattice translates have differentiated bounds by a power of \(u^{-1}\) times \(e^{-c/u}\). At large time the subtracted Euclidean term and its derivatives are integrable since \(s>0\). Hence the remainder after the coefficient-one singularity is smooth. The resulting \(K=s z|z|^{-s-2}-\nabla H\) is in \(L^1\) because \(s+1<d\). The gradient boundary term is \(O(r^{d-1-s})\to0\).

For the divergence, integration outside a radius-\(r\) ball gives the positive inner flux

\[
 s r^{d-s-2}\int_{\mathbb S^{d-1}}a(r\theta)dS+O_a(r^{d-1}).
\]

It tends to zero below Coulomb and to \(c_d a(0)\) at Coulomb, with \(c_d=(d-2)|\mathbb S^{d-1}|\). Gamma recurrence and the zero Fourier mode then give exactly

\[
 D=\operatorname{div}K=
 \begin{cases}s(d-2-s)g_{s+2}(z)dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2.
 \end{cases}
\]

The sub-Coulomb identity uses \(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\); the endpoint identity uses \(4\pi^2c_{d,d-2}=c_d\). Both have total mass zero and a finite negative-density bound \(-\kappa dz\). In particular \(D_\varepsilon\ge-\kappa\), and at Coulomb \(D_\varepsilon=c_d(p_\varepsilon-1)\). Replacing it by \(-c_d\) in a Haar integral would fail; the candidate does not do this.

With \(H_N=N^{-1}\sum_{i<j}g_{ij}\), set \(\mathcal H_N=H_N-(N-1)g_*/2\ge0\). Its sublevels exclude every partial or simultaneous collision because every shifted pair summand is nonnegative. Direct differentiation gives

\[
 B=-\nabla H_N,qquad
 \Delta_{Nd}H_N=\frac2N\sum_{i<j}\Delta g_{ij}\le(N-1)\kappa.
\]

On a compact energy sublevel the cutoff construction agrees with the singular equation, all differentiated quantities are bounded, and stopped Itô has drift \(-|B|^2+\nu\Delta_{Nd}H_N\). Its stopped martingale has bracket \(2\nu\int|B|^2\) and zero mean. The full drift square, including all possible cross terms, remains intact. The energy-exit probability is at most \([\mathcal H_N(x)+\nu(N-1)\kappa T]/R\). A path trapped in a collision-free compact set has an extendible finite endpoint because its drift integral and continuous Brownian signal have limits. These facts prove noncollision and global uniqueness from every fixed distinct start, almost surely. Local Picard iteration and countable stopping/patching give joint measurability; integration against the independent iid initial vector is therefore legitimate. Its initial shifted-energy mean is finite, equal to \(-(N-1)g_*/2\).

Each realized continuous noncolliding path on a finite horizon has positive minimum separation. Away from zero, write \(K\) as a smooth function plus a distant \(L^1\) remainder; differentiated Gaussian bounds make the latter's heat convolution vanish locally in \(C^1\). On the event of positive singular-path separation, stop a coupled smooth/singular difference before it reaches one quarter of that separation. Identical noise cancels. A path-dependent local Lipschitz bound and Gronwall prevent that stop for all sufficiently small heat parameters. This proves full-family path convergence, not merely a weak subsequence, at fixed \(N,\nu,T\).

For a smooth heat flow, the initial-point derivative obeys an ordinary variational equation after subtracting the additive Brownian signal. Its Jacobian is at least \(e^{-(N-1)\kappa t}\), since the exact configuration divergence is \(2N^{-1}\sum_{i<j}D_\varepsilon(x_i-x_j)\). The flow is a diffeomorphism by the backward smooth integral equation. Change of variables, expectation in the independent Brownian signal, and the just-proved path convergence give the density bound first on continuous nonnegative tests. Increasing continuous approximants for open sets and Haar outer regularity extend it to Borel sets. The resulting \(F_t\le e^{(N-1)\kappa t}\) is valid also at zero noise. This exponential factor never enters the uniform source constant.

## 4. Actual expected energy and the exact positive splitting

At a fixed smooth heat cutoff and positive noise, the initial density is one. The compact smooth forward equation gives a classical positive density, bounded above and below on a finite time interval; comparison with \(e^{\pm Ct}\), \(C\ge\|\Delta H_N^\varepsilon\|_\infty\), supplies the bounds needed for logarithmic differentiation. The fixed-cutoff construction is also obtainable by iteration of its heat integral equation, whose spatial-gradient kernel has integrable \(t^{-1/2}\) norm. No estimate uniform in cutoff or inverse noise is required at this stage. Smooth forward/backward duality identifies this density with the actual smooth SDE law.

Writing all cross terms shows why the expected-energy sign is valid:

\[
\begin{split}
 \frac d{dt}\mathbb E H_N^\varepsilon
 &=-\int F|\nabla H_N^\varepsilon|^2
   -\nu\int\nabla F\cdot\nabla H_N^\varepsilon,\\
 \frac d{dt}\left(\nu\int F\log F\right)
 &=-\nu\int\nabla F\cdot\nabla H_N^\varepsilon
   -\nu^2\int\frac{|\nabla F|^2}{F}.
\end{split}
\]

Their sum is \(-\int F|\nabla H_N^\varepsilon+\nu\nabla\log F|^2\). The two initial quantities vanish. Entropy relative to the mass-one Haar reference is nonnegative, so \(\mathbb EH_N^\varepsilon\le0\). Heat positivity preserves \(H_N^\varepsilon\ge(N-1)g_*/2\). The same-noise convergence and local kernel convergence give the actual singular energy pointwise at each deterministic time. Fatou after that fixed-\(N\) lower shift proves \(\mathbb EH_N\le0\), and also proves its integrability. This is the correct direction of Fatou; neither uniform integrability nor passage of a singular entropy-dissipation equality is asserted.

At zero noise, the actual deterministic flow satisfies \(H_N(t)+\int_0^t|B|^2=H_N(0)\). Its lower bound and the integrable initial energy yield the same expectation sign directly. Exchangeability then gives \(\mathbb Eg_{12}=2\mathbb EH_N/(N-1)\le0\) and \(\mathbb E|g_{12}|\le2|g_*|\). The local inverse-\(s\)-power pair-distance moment follows. Common translation equivariance gives Haar one-body marginals, without iid claims at later times.

For \(M=d+2\), use \(w_r(u)=(1-e^{-u/r})^M\), \(\psi_r=1-w_r\). The candidate's definitions of \(g_r,Q_r,c_r\) give \(g=g_r+Q_r-c_r\), \(Q_r\ge0\), and

\[
 c_r=A r^\alpha\int_0^\infty u^{\alpha-1}\psi_1(u)du.
\]

The mass integral is positive and finite; the alternating-binomial expression is only its evaluation. Since \(w_r\le\min(1,(u/r)^M)\), the retained Fourier coefficients are positive and decay as \(O_r(|k|^{-2\alpha-2M})\). Here \(2\alpha+2M>d+2\), so two differentiated Fourier powers are summable. The retained kernel is \(C^2\) and has finite self value \(g_r(0)=\sum_{k\ne0}a_r(k)\ge0\). Splitting the small-time integral at \(r\) proves \(g_r(0)\le Cr^{-s/2}\), for all \(0<r\le2\) after a fixed enlargement.

For a collision-free configuration, positivity of its Fourier energy and of the discarded pair kernel separately gives

\[
 E_r=\frac12\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2\ge0,
 \qquad S_r=\frac1{2N^2}\sum_{i\ne j}Q_r(x_i-x_j)\ge0.
\]

Counting, before estimating, gives the exact identity

\[
 \frac{H_N}{N}=E_r+S_r-\frac{g_r(0)}{2N}-\frac{N-1}{2N}c_r.
\]

The self coefficient comes from exactly \(N\) retained self terms. The constant coefficient comes from exactly \(N(N-1)\) ordered distinct pairs. Neither is replaceable by \(1/2\). At fixed \(r,N\), the retained energy is bounded and the discarded term is integrable from the splitting and the actual pair moment. Consequently

\[
 \mathbb EE_r+\mathbb ES_r\le C(N^{-1}r^{-s/2}+r^\alpha).
\]

This controls both positive quantities simultaneously without transferring a generic-law estimate to the actual process.

## 5. The two source estimates, exact contractions, and all uniformities

For any smooth \(v\), oddness and integrability give

\[
 A_g(x):=\int J_g(x,y)dy=-\int K(x-y)\cdot v(y)dy,
 \qquad\int A_g=\iint J_g=0.
\]

For \(v=\nabla f\), distributional integration by parts against the smooth test gives \(A_g=-D*f\), hence \(\widehat A_g(k)=-d_k\widehat f(k)\). In particular the full Coulomb contraction is \(-c_d(f-\int f)\). The candidate's use of \(f(x+z)\) gives the same expression because \(D\) is even. These equations retain, rather than redefine, all original contractions.

The actual backward multiplier has modulus at most one. Thus every spatial Fourier seminorm of the same \(h\) controls that of \(f_t^\nu\), uniformly over the admitted time and noise range. The time derivative adds at most two powers of \(|k|\), with a constant depending on \(\nu_*\), because \(s+2-d\le0\). There is no finite-polynomial replacement. The local estimate \(|J_t|\le C_h(1+\operatorname{dist}(x,y)^{-s})\) and the actual pair moment prove source integrability even before the sharper commutator estimate.

For the retained coefficient \(a_r(\xi)=A\int_0^\infty u^{\alpha-1}w_r(u)e^{-4\pi^2\xi^2u}du\), one has \(0\le uw'_r\le Mw_r\). Integrating the derivative of \(u^\alpha w_r e^{-\lambda u}\) has vanishing boundary terms at zero and infinity. It gives

\[
 0\le-\frac{\xi a'_r(\xi)}{a_r(\xi)}\le L:=2(\alpha+M),
\]

independently of \(r\). For nonzero lattice vectors \(k,\ell\), let \(u=\min(|k|,|\ell|)\ge1\), \(R=\max(|k|,|\ell|)\), \(q=k-\ell\). Integrating the slope gives \(a_r(u)/a_r(R)\le(R/u)^L\) and \(a_r(u)-a_r(R)\le L a_r(u)(R-u)/u\). The vector numerator is at most \(|q|a_r(u)+R[a_r(u)-a_r(R)]\). Since \(R-u\le|q|\) and \(R/u\le1+|q|\), this proves exactly

\[
 \frac{|k a_r(k)-\ell a_r(\ell)|}{\sqrt{a_r(k)a_r(\ell)}}
 \le(1+L)|q|(1+|q|)^{L/2+1}.
\]

No exponentially small neighboring-weight ratio is presumed bounded. The discrete lower bound \(u\ge1\) and absence of the zero signed-measure mode are material and both hold.

Only the retained smooth source has diagonal zero. Thus for \(\rho=\eta_N-dx\), its original statistic equals the centered full product and symmetrizes to

\[
 P_N[J_r]= -\pi i\sum_{k,\ell\ne0}
 [k a_r(k)-\ell a_r(\ell)]\cdot\widehat v(\ell-k)
 \widehat\rho(k)\overline{\widehat\rho(\ell)}.
\]

The sign and coefficient agree with direct expansion of \(\int v\cdot(K_r*\rho)d\rho\). Absolute convergence follows already from \(\sum |k|a_r(k)<\infty\), the bounded Fourier coefficients of the finite signed measure, and the summable coefficients of \(v\). Applying the displayed multiplier estimate and Cauchy–Schwarz to each translation of the sequence \(\sqrt{a_r(k)}|\widehat\rho(k)|\) gives \(|P_N[J_r]|\le2C_vE_r\). The seminorm

\[
 C_v=\pi(1+L)\sum_q|q|(1+|q|)^{L/2+1}|\widehat v(q)|
\]

is bounded by a fixed multiple of \(\sum_q(1+|q|)^{\alpha+M+3}|\widehat h(q)|<\infty\). It is independent of \(r,N,t,\nu\). This explicitly handles infinitely many modes of one arbitrary smooth test.

For the discarded remainder \(R_r=Q_r-c_r\), its gradient is Haar \(L^1\): near heat time zero its norm is bounded by an integrable multiple of \(u^{\alpha-3/2}\), and the other tail is exponentially decaying. For every lattice translate, the shortest torus distance \(\delta(z)\) is at most \(|z+n|\). If \(y=|z+n|^2/(8u)\), the ratio of its differentiated Gaussian majorant to its \(2u\)-Gaussian is \(4\,2^{d/2}y e^{-y}\), uniformly bounded. Therefore

\[
 \delta(z)|\nabla p_u(z)|\le C_d p_{2u}(z),
 \qquad |J_{R_r}(x,y)|\le C_d2^{-\alpha}\|Dv\|_\infty Q_{2r}(x-y).
\]

The equality \(\psi_r(a/2)=\psi_{2r}(a)\) and the factor \(2^{-\alpha}\) come from the exact change of heat variable \(a=2u\). No torus distance is differentiated. The three original source terms are bounded respectively by a multiple of \(S_{2r},c_{2r},c_{2r}/2\). The double contraction is zero, but keeping its absolute bound is valid. The preceding energy inequality at scale \(2r\le2\) therefore proves

\[
 \mathbb E|P_N[J_g]|\le C_h(N^{-1}r^{-s/2}+r^\alpha),\qquad0<r\le1.
\]

Setting \(r=N^{-2/d}\) balances the exponents: both terms are \(N^{s/d-1}\). All particle heat limits have already been completed for fixed \(N,\nu,T\); substituting this deterministic scale does not interchange limits. Joint measurability and Tonelli give the absolute time integral and the stated scaled upper bound. A common constant can be enlarged by \(1+T\), covering \(T=0\).

Since \(s<d\), the unscaled estimate always decays. Scaled decay from this estimate alone holds only for \(s<d/2\); equality gives a bounded estimate, and \(s>d/2\) gives only the displayed possibly growing estimate. This covers three-dimensional Coulomb, four-dimensional Coulomb at the scaled boundary, and larger-dimensional Coulomb without an illicit decay claim. Every step is uniform down to the actual zero-noise flow. No dependence on \(1/\nu\) is hidden in the final constant.

## 6. Independent admissible falsifications and stronger-claim tests

### 6.1. Exact initial generator and Coulomb transport diagnostic

For a fixed nonzero \(k\), write \(Z_k=N^{-1}\sum_i e^{-2\pi i k\cdot X_i}\). The \(N\) self terms give \(\mathbb E|Z_k(0)|^2=1/N\). At initial product Haar the two internal forces of an ordered pair have total coefficient \(2/N\), while a third-label force integrates to zero and diffusion has zero Haar integral. Thus the pair weak derivative is \(-(2/N)D(x-y)\), which gives

\[
 \left.\frac d{dt}\mathbb E|Z_k(t)|^2\right|_{0+}
 =-\frac{2(N-1)}{N^2}d_k\le0.
\]

This is an actual singular-law derivative. For the smooth full-configuration observable, its generator is Haar \(L^1\) since \(K\in L^1\). The fixed-\(N\) density bound is uniform on a short time interval. Approximate the generator in Haar \(L^1\) by continuous functions; the bound controls the errors uniformly and path continuity handles the continuous approximants at time zero. Stopped Itô passes to expectation because the bounded test derivatives and the same density bound make the force occupation integral finite. Hence the expectation derivative equals the initial Haar generator integral. No unbounded cutoff Taylor remainder is required or asserted.

There is a second, direct zero-noise Coulomb check that does not begin with the heat splitting or the weak divergence formula. For the admitted \(N=2\) model, the relative position \(R=X_1-X_2\) satisfies exactly \(\dot R=K(R)\). Its initial law is Haar. The actual noncolliding flow \(\Phi_t:\mathbb T^d\setminus\{0\}\to S_t\) is injective, smooth locally in its initial point, and is a diffeomorphism onto its open image. Local backward uniqueness proves injectivity. On every noncolliding path, \(\operatorname{div}_{\rm cl}K=-c_d\); the variational determinant is exactly \(e^{-c_dt}\). Change of variables gives

\[
 |S_t|=e^{-c_dt},\qquad
 F_t^R=e^{c_dt}\mathbf1_{S_t}.
\]

For every compact set separated from zero, the bounded smooth backward field exists for all sufficiently short times. That compact set is contained in \(S_t\), so its complement shrinks toward zero as \(t\downarrow0\). Since \(|S_t^c|=1-e^{-c_dt}\), for every continuous test \(a\)

\[
 \lim_{t\downarrow0}\frac{\int aF_t^R-\int a}{t}
 =c_d\int a-c_d a(0).
\]

This recovers the full weak derivative \(-D\), with the negative collision atom and positive compensating Haar density, from an actual admissible deterministic flow. Pairing a nonzero character yields \(-c_d\), precisely the \(N=2\) pair coefficient. It independently confirms the candidate's use of the Coulomb atom and shows why the pointwise divergence alone would be insufficient. This diagnostic also shows that the finite-\(N\) density bound can be sharp; it supplies no uniform-\(N\) law transfer.

### 6.2. Remaining attempted counterexamples

| Admitted test or limiting challenge | Calculation and outcome |
|---|---|
| Actual \(N=2\), zero noise | \(B=(K/2,-K/2)\), \(H_2=g(R)/2\), and \(dH_2/dt=-|K(R)|^2/2\). The drift square and the source proof agree; no triple label exists. |
| Actual iid near-collision starts | The initial radial energy moment has exponent \(d-1-s>-1\), so it is finite. Conditional energy stopping covers every distinct start and its iid average. The evolved moment follows from actual expected energy, not a claimed uniform deterministic separation. |
| Fixed nonconstant test with \(s\ge d/2\) | Take the fixed smooth test \(h(x)=\cos(2\pi x_1)\), at terminal time, and an open set where its first Hessian entry stays nonzero. On an angular cone with \(\theta_1^2\) bounded away from zero, the local leading source is \(s\,\theta^T\nabla^2h(x)\theta\,r^{-s}\), with a smaller Taylor remainder. Its squared Haar integral contains \(\int_0^\epsilon r^{d-1-2s}dr\), which diverges at and above the threshold. This verifies the stronger square-failure statement and does not contradict the required \(L^1\) estimate. |
| One fixed smooth test with infinitely many modes | The explicit weighted absolute Fourier sum above is finite. High modes of that same test are controlled by the same seminorm; no degree-dependent polynomial bound is substituted. |
| Noise zero, arbitrarily small positive noise, or a fixed upper bound | The actual energy sign has separate positive/zero-noise proofs, while final test and source constants are independent of the selected noise. No division by a vanishing noise appears. |
| \(h\) constant; \(T=0\) | The source is identically zero for a constant test, including its constant mode. At \(T=0\) the time integral is zero and the pointwise iid estimate remains valid. |
| Four-dimensional Coulomb and higher exponents | The scaled exponent is zero at \(d=4,s=2\) and positive when \(s>d/2\). The theorem claims bounded or possibly growing upper bounds there, so absence of decay is not a counterexample. |
| Generic clustered exchangeable laws | Not admitted. Such laws need not have \(\mathbb EH_N\le0\), the specific actual-law input. They cannot disprove this card. |

The initial positive-variance-creation route fails exactly at the computed negative derivative. No later-time covariance sign, uniform singular Taylor expansion, source-square estimate, or fluctuation conclusion is added.

## 7. Fresh exact diagnostic, controls, and result

The new `ROUND_016_SOURCE_HOSTILE_ARTIFACTS/independent_diagnostic.py` was written from the present recomputations without opening any previous checker. It reads only its own source bytes for its digest. It uses standard-library rational and Gaussian-rational arithmetic, no floating-point tolerance, no random sampling, no external package, and no installation. Its finite Fourier source and generator are normalized by \(4\pi^2\); each spatial derivative is normalized by \(2\pi\). The common Riesz prefactor is explicitly retained in the analytic proof and factored out only where diagnostic ratios cancel it.

The exact tests include all of the following:

- Gaussian/Fourier coefficient and sub-Coulomb/Coulomb gamma recurrences in dimensions 3 through 13 for integer admissible exponents, with powers of pi represented symbolically.
- Positive rational Laplace moments, discarded masses, the scale-doubling factor, and logarithmic slopes across several integer \(\alpha\), \(M=d+2\), small/large splitting scales, and low/high spectral parameters.
- The independent Coulomb identity \(\int_0^\infty(1-e^{-u/r})^Me^{-\lambda u}du=M!/[\lambda\prod_{j=1}^M(\lambda r+j)]\) and its exact logarithmic derivative. This tests the endpoint retained weight by a positive product, independently of an alternating sum.
- Exact vector multiplier inequalities, including nearby high frequencies, low/high separated frequencies, different directions, opposite components, and equal modes.
- Literal ordered/deleted source sums and original mixed contractions versus the symmetric Fourier formula at distinct configurations with \(N=2,\ldots,7\). Literal energy splitting checks retain both self and background coefficients.
- The entire finite-particle Fourier generator, before taking its constant coefficient under product Haar, applied to \(|Z_k|^2\) for \(N=2,\ldots,6\), four noises including zero, present modes, and an absent mode. The full generated polynomial is formed, so third-label terms are not assumed away in the implementation.
- All three scaled regimes, the square-integrability boundary, exact free-energy square coefficients, and the \(N=2\) total-drift coefficient.

Command, from the isolated worktree:

    python3 AUDITS/HOSTILE/ROUND_016_SOURCE_HOSTILE_ARTIFACTS/independent_diagnostic.py

Outcome: **PASS, 1,700 exact assertions in 37 categories.** All eight deliberately wrong coefficients/conventions produced detected witnesses: missing source half, omitted one-body contraction, wrong Fourier sign, falling-factorial source denominator, omitted energy self subtraction, wrong discarded-mass coefficient, wrong force sign, and a missing internal two-label factor. The JSON results record exact cases, witness counts, normalizations, and the script SHA-256. No failed check was suppressed. No theorem is inferred from a finite sample: arbitrary real exponents, singular passages, arbitrary smooth tests, and uniformity are justified by the analytic arguments above.

## 8. Issuance, output control, and bounded handoff

The assigned report and unique artifact directory are the only audit outputs. No canonical ledger, manuscript, current mathematical state, or other worker's file was edited. The eleven worktree input copies were task-authorized; frozen packet input copies reproduce those eleven byte strings. No commit, push, install, external search, publication, author contact, or child agent occurred.

The artifact README gives the exact payload, input/output manifests, archive path, verification procedure, and exposure record. A deterministic archive contains only its declared regular-file members, with relative paths, no traversal, no links, no duplicate names, and read-only modes. Literal member equality and decompressed member bytes are verified against the final payload. Separate archive and seal digests avoid a self-hashing cycle. Every issued payload, input copy, output manifest, archive, and seal control is made read-only and checked before handoff. Corrections must be separately issued; this report is not to be edited after sealing.

**Handoff:** AUD052 is a full hostile PASS on the exact frozen THM-038 card and candidate. No mathematical repair or user decision is required within this bounded assignment. The earlier complete local reports retain their issued conditional status. Root must compare this report with the deliberately withheld whole-claim reconstruction, integrate the sealed files, and decide canonical gate promotion. This worker stops at that sealed bounded handoff.
