# Round 014 — the exact lower drift contractions

TASK-073, 2026-09-18 UTC. **CONDITIONAL PROOF CONSTRUCTED / SELF-CHECKED; NO INDEPENDENT AUDIT OR PROMOTION.** Every assertion of the frozen THM-035 card follows from its admitted smaller-gradient and complete-domain premises. No new analytic premise, modified coefficient, different inverse, or evolved iid hypothesis is needed. The estimate below is in fact pathwise. The cubic remainder is not shown to vanish.

This report was constructed in `/Users/matthewrosenzweig/.codex/worktrees/hocf-r014-lower-drift`, branch `codex/hocf-r014-lower-drift`, at base `1df1805ed7cd8f7c295945f99273c8ffdb598e74`. Exactly the 25 current inputs in the assigned seal were verified, copied, and verified again before mathematical use. The companion `ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC` contains the complete frozen dossier, exposure record, independently written exact diagnostic, results, and seals. This is a construction context, not a blind or hostile audit context.

## 1. Frozen assertion, negation, and source boundary

Fix an integer \(d\ge3\), \(0<s<d-2\), \(3s<2d-2\), a finite nonnegative horizon \(T\), a smooth real terminal test \(h\), and finite nonnegative \(L,\nu_*\). For \(N\ge2\), take \(0\le\nu\le\nu_*\) with

\[
p=s+2,\qquad \chi=\nu N^{2/p}\le L.
\tag{1.1}
\]

The geometry is the unit Haar torus, the external drift is zero, the reference is Haar, and the actual singular particles start from iid Haar independently of their Brownian drivers. The actual law is the law of the supplied noncolliding solution of

\[
dX_i(t)=\frac1N\sum_{j\ne i}K(X_i(t)-X_j(t))\,dt+\sqrt{2\nu}\,dW_i(t),
\qquad i=1,\ldots,N,
\]

with independent standard Brownian motions. For positive noise set

\[
b=\min(1/\nu,1),\qquad \sigma=\sqrt{Nb};
\]

at zero noise set \(b=1\), \(\sigma=\sqrt N\), exactly as in the card. No reciprocal of zero is taken. Let \(f\) be the actual homogeneous backward Fourier test and \(\Phi\) the genuine symmetric terminal-zero full inverse, with both response slots. Define

\[
\begin{split}
q_-&=\max(1,s/2),\qquad
q_+=\min(d/2,d-s-1,s+1),\qquad q=(q_-+q_+)/2,\\
B\Phi_t(x,y)&=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi_t(x,y),\\
g_t(x)&=\int B\Phi_t(x,y)\,dy,\qquad
c_t=\iint B\Phi_t(x,y)\,dx\,dy,\\
\rho_t&=\eta_N(t)-dx,\qquad
\ell_N(t)=\frac1N\rho_t[g_t]+\frac1{2N}c_t.
\end{split}
\tag{1.2}
\]

The claim is admissibility of this \(q\), positivity of \(\kappa_q=(2q-s)/(2p)\), and a constant depending only on the fixed data such that

\[
\sigma\,\mathbb E\int_0^T|\ell_N(t)|\,dt
\le C\sqrt b\,N^{-\kappa_q}.
\tag{1.3}
\]

It also claims inclusion of every strict R12 critical decay exponent range \(0<s<d-2\), \(s(s+2)<2d\), and the exact equivalence of scaled integrated cubic-plus-lower smallness with scaled integrated cubic smallness in that range. Its logical negation is an admitted fixed family violating the uniform bound, or failure of an admissibility, inclusion, or reduction assertion. Showing divergence of an upper-bound majorant outside the admitted range is not this negation.

The proof uses the following precise parts of the supplied sources. All issued status qualifications remain in force; this context does not certify any prior source.

| Supplied source | Imported content and restriction |
|---|---|
| `TASKS/ACTIVE/ROUND_001_MODEL.md`; `MEMORANDA/ROUND_001_ALGEBRA.md`, Sections 1, 3, 7 | Unit Haar, ordered distinct labels with denominator \(N^k\), \(P=U_2/2\), coefficient-one upward interaction, and the exact two lower coefficients. Section 4 below reconstructs those coefficients directly. |
| THM-021; `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–3 | Frozen Fourier normalization, local coefficient-one singularity with smooth even remainder, integrability of \(K\), and both compensated homogeneous responses. The local statement comes from the full proof, not just its short card. |
| THM-023/024/025; the three R5 memoranda and two allowed clarifications | The true singular auxiliary pair evolution, the bounded Borel Volterra inverse, both response slots, pair-exchange symmetry, and the actual Fourier test. No self-adjointness or diagonal-start evolution is used. |
| THM-026 and its R6 memorandum | The actual finite-particle realization, uniqueness, finite-horizon noncollision, and permitted iid-Haar preparation independent of the drivers. No uniform-in-\(N\) density bound is imported. |
| THM-028; `MEMORANDA/ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, Sections 8–11 | **Conditional complete-domain premise:** the classical off-diagonal representatives, their actual Haar slices, every mixed contraction, the exact genuine finite-particle Itô identity, and fixed-\(N\) expected absolute integrability of the cubic. |
| THM-033, its first displayed bound; `MEMORANDA/ROUND_012_SUBCOULOMB_ACTUAL_NOISE.md`, Sections 1–4 | **Conditional smaller-gradient premise:** for every fixed \(1<q<d/2\), \(q\le s+1\), the genuine inverse satisfies (2.3) below uniformly over the bounded-\(\chi\) family, including zero noise. The weight is the exact R7 weight. |
| THM-027 and `MEMORANDA/ROUND_007_WEIGHTED_PAIR_GRADIENT.md`, Section 2 | The Euclidean product norm for the pair gradient and the fixed multiplicative weights. No fixed-\(N\) constant from this older theorem is silently treated as uniform. |

THM-031 and the allowed R10 memorandum were consulted only for their source/law-class boundaries. Their energy floor, entropy, Fourier-moment and smoothing assertions are **not needed** for (1.3). In particular the R12 noise bound and its energy-occupation proof are not inputs to this lower-drift estimate. No external literature claim or new source theorem is used. The R5 clarifications contain references to older audit reports, but those reports were not opened and their verdicts are not new evidence here.

The frozen kernel and actual Fourier test are, without altered constants,

\[
\begin{split}
\widehat g(0)&=0,\quad
\widehat g(k)=c_{d,s}|k|^{s-d},\quad
c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad K=-\nabla g,\\
f_t(x)&=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
e^{-(T-t)(4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{s+2-d})}
e^{2\pi i k\cdot x}.
\end{split}
\tag{1.4}
\]

Thus all fixed spatial derivatives of \(f\) are bounded uniformly over the admitted \(N,t,\nu\). This follows by absolute domination with the rapidly decreasing Fourier coefficients of the fixed smooth \(h\), since the exponential has modulus at most one. Both responses are

\[
R_x v(x,y)=-\int v(x+w,y)D(dw),\qquad
R_y v(x,y)=-\int v(x,y+w)D(dw),\qquad D=\operatorname{div}K.
\tag{1.5}
\]

The full inverse solves the supplied Volterra equation with \(R_x+R_y\), and, under the domain premise, satisfies the classical equation off the pair diagonal

\[
\partial_t\Phi+\nu(\Delta_x+\Delta_y)\Phi+N^{-1}B\Phi
 +(R_x+R_y)\Phi=-J,\qquad
J=K(x-y)\cdot(\nabla f(x)-\nabla f(y)),\quad \Phi_T=0.
\tag{1.6}
\]

## 2. Every exponent restriction and the quantitative premise

Each element of the maximum \(q_-\) is strictly smaller than each element of the minimum \(q_+\). For 1 these inequalities are

\[
1<d/2,\qquad 1<d-s-1,\qquad 1<s+1,
\]

using respectively \(d\ge3\), \(s<d-2\), and \(s>0\). For \(s/2\), they are

\[
s/2<d/2,\qquad s/2<d-s-1,\qquad s/2<s+1.
\]

The middle inequality is precisely \(3s<2d-2\); the others follow from the displayed hypotheses. Hence \(q_-<q_+\), and their midpoint obeys

\[
1<q<d/2,\qquad q<s+1,\qquad q<d-s-1,\qquad q>s/2.
\tag{2.1}
\]

In particular it is admissible for the supplied R12 gradient theorem. A compatible R8 second-derivative exponent is \(q_2=(q+1+d)/2\): since \(q<d/2\) and \(d\ge3\), one has \(q+1<d\), so \(q+1<q_2<d\). This is a domain choice only; no R8 constant depending on \(N\) is used in the new uniform estimate. Put

\[
\alpha_q=\frac{s+1-q}{s+2},\qquad m=s+1+q<d.
\tag{2.2}
\]

The exact quantitative premise needed from R12 is a finite constant \(A_q\), depending only on \(d,s,q,T,h,L,\nu_*\) and the fixed kernel/weight, for which

\[
\sup_{0\le t\le T}\sup_{x\ne y}
\frac{|\nabla_{x,y}\Phi_t(x,y)|}{w_q(x-y)}
\le A_q N^{\alpha_q}
\tag{2.3}
\]

for all admitted \(N,\nu\). Here \(A_q\) is the **uniform constant of the admitted gradient premise**, not an older \(C_N\). It is the only imported quantitative constant in the new bound. Formula (5.3) below gives the entire additional constant explicitly in terms of this premise and fixed kernel norms. No unrecorded particle-density, cutoff or time-dependent constant is introduced.

For precision, use the supplied R7 weight: \(R=1/16\), \(w_1=\exp(\chi_{\rm cut}\log(1/r))\) on the embedded cutoff chart, \(w_1=1\) off \(B_{2R}\), and \(w_a=w_1^a\). The cutoff is fixed, equals one on \(B_R\), and vanishes off \(B_{2R}\). Thus \(w_q=r^{-q}\) on \(B_R\setminus\{0\}\); it is bounded on the complement. No global smooth torus distance is differentiated.

## 3. Absolute slice integrability, representatives, and constants

The local kernel premise gives

\[
g(z)=|z|^{-s}+H_s(z),\qquad
K(z)=s z|z|^{-s-2}-\nabla H_s(z),\qquad H_s\in C^\infty(B_{1/3}).
\tag{3.1}
\]

Define fixed finite quantities

\[
\begin{split}
\omega_{d-1}&=|\mathbb S^{d-1}|,\qquad
H_0=\sup_{|z|\le R}|\nabla H_s(z)|,\\
M_{K,q}^{\rm out}&=\sup_{z\notin B_R}|K(z)|w_q(z),\\
J_q&=\int_{\mathbb T^d}|K(z)|w_q(z)\,dz,\\
J_q^*&=\frac{s\omega_{d-1}R^{d-m}}{d-m}
 +\frac{H_0\omega_{d-1}R^{d-q}}{d-q}+M_{K,q}^{\rm out}.
\end{split}
\tag{3.2}
\]

All denominators are strictly positive by (2.1). Polar integration on the embedded ball and the fact that the complementary Haar mass is at most one give

\[
J_q\le J_q^*<\infty.
\tag{3.3}
\]

This is the relevant product-integrability check: the singular exponent is \(s+1+q\), not merely \(q\), and the radial integral is \(\int_0^R r^{d-1-m}\,dr\). The conditions \(2q<d\) and \(q<d\) also hold and agree with the supplied domain theorem, but alone would not imply (3.3).

For the Euclidean product norm, Cauchy–Schwarz gives exactly

\[
|B\Phi_t(x,y)|
=|(K(x-y),-K(x-y))\cdot\nabla_{x,y}\Phi_t(x,y)|
\le\sqrt2\,A_q N^{\alpha_q}|K(x-y)|w_q(x-y).
\tag{3.4}
\]

Consequently, with \(D_q=\sqrt2 A_q J_q^*\),

\[
\sup_{t,x}\int|B\Phi_t(x,y)|\,dy\le D_qN^{\alpha_q},\qquad
\sup_{t,y}\int|B\Phi_t(x,y)|\,dx\le D_qN^{\alpha_q},
\tag{3.5}
\]

and therefore

\[
\sup_t\|g_t\|_\infty\le D_qN^{\alpha_q},\qquad
|c_t|\le D_qN^{\alpha_q},\qquad c_t=\int g_t(x)\,dx.
\tag{3.6}
\]

These are uniform slice estimates for **every** remaining coordinate, not only almost every coordinate. We use the R8 classical off-diagonal representative. The singular point excluded in each slice has Haar measure zero; arbitrary values assigned on the true pair diagonal change no slice or scalar integral. Absolute Fubini justifies the last identity in (3.6).

There is no representative ambiguity at particle evaluations of \(g_t\). The R8 contraction is continuous; this also follows directly here. Split a moving slice integral into a small ball around the moving singular point and its complement. By (3.1)–(3.4), the ball contribution is bounded uniformly in its center and in time by a fixed multiple of

\[
N^{\alpha_q}(\delta^{d-m}+\delta^{d-q}),
\]

which tends to zero for each fixed \(N\). On the complement, joint continuity of the actual off-diagonal derivatives from R8 gives continuity of the integral. When the center moves, take the union of the two small balls; their contributions obey the same bound with a fixed enlargement of the radius. First take the limit on the complement and then let \(\delta\downarrow0\). This proves joint continuity of \(g\), including the supplied one-sided time endpoints. Integrating \(g\) gives continuity of \(c\). Thus the integrals here select exactly the R8 continuous representatives, rather than an arbitrary Haar equivalence class.

No new singular Itô formula, differentiation under an unproved singular expectation, collision integration by parts, or heat-limit exchange is used in this estimate. The old structural PDE bound for \(B\Phi\) remains part of R8; in the smaller present range the independently verified product bound (3.4) supplies the needed uniform power.

## 4. Exact deleted-label coefficients and both responses

Here is a direct coefficient reconstruction on a fixed collision-free configuration. Write

\[
P_N[v]=\frac1{2N^2}\sum_{i\ne j}v(x_i,x_j)
 -\frac1N\sum_i\int v(x_i,y)\,dy+\frac12\iint v(x,y)\,dx\,dy,
\quad D_2[v]=N^{-2}\sum_{i\ne j}v(x_i,x_j).
\tag{4.1}
\]

For \(p(x,y)=\nabla_x\Phi(x,y)\), \(a(x)=\int p(x,y)\,dy\), the configuration force generator contributes

\[
Q=\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}
 K(x_i-x_k)\cdot p(x_i,x_j)
 -\frac1{N^2}\sum_{i\ne k}K(x_i-x_k)\cdot a(x_i).
\tag{4.2}
\]

Splitting \(k=j\) from the three-distinct terms and pairing the two orientations gives the exact repeated-label contribution

\[
\frac1{N^3}\sum_{i\ne j}K(x_i-x_j)\cdot p(x_i,x_j)
=\frac1{2N}D_2[B\Phi].
\tag{4.3}
\]

No diagonal value is involved: the displayed labels are distinct and the actual coordinates are collision-free. Define the cubic with the prescribed average over all six permutations,

\[
C\Phi=\operatorname{Sym}_3[K(x-z)\cdot p(x,y)].
\tag{4.4}
\]

For clarity, all its background contractions are retained. Put

\[
A_a(x,y)=K(x-y)\cdot(a(x)-a(y)),\qquad
v(x)=\int K(z-x)\cdot a(z)\,dz.
\]

Integrating the six terms in (4.4) over the third variable gives two zero terms by \(\int K=0\), two terms making \(A_a\), and the two different response slots. Hence, with \(R=R_x+R_y\),

\[
(C\Phi)_1=\frac16(A_a+R\Phi),\qquad
(C\Phi)_2=\frac13v,\qquad
(C\Phi)_0=0,\qquad
(R\Phi)_\mu=v,\quad\int R\Phi=0.
\tag{4.5}
\]

The second identity follows by integrating the first: both \(A_a\) and \(R\Phi\) have slice integral \(v\). The final scalar vanishes because \(\int K=0\). The absolute integrability of these mixed contractions is part of the admitted R8 domain; its Section 9 separates the two possible singular points before performing each response integral. No illegal value of \(C\Phi(x,x,z)\) is used.

The literal ordered-label statistic is

\[
U_3[F]=\frac1{N^3}\sum_{i,j,k\ {
m distinct}}F(x_i,x_j,x_k)
 -\frac3{N^2}\sum_{i\ne j}F_1(x_i,x_j)
 +\frac3N\sum_iF_2(x_i)-F_0.
\tag{4.6}
\]

Insert (4.5) into (4.6). The last term in (4.2), paired by oddness, is \(-(2N^2)^{-1}\sum_{i\ne j}A_a(x_i,x_j)\). Thus cancellation of the explicit background terms, not a change of normalization, gives

\[
Q=U_3[C\Phi]+P_N[R\Phi]+\frac1{2N}D_2[B\Phi].
\tag{4.7}
\]

In particular both response slots are needed with coefficient one. For \(N=2\), the first sum in (4.6) is empty, but \(U_3\) generally is not zero.

The full inverse places \(P_N[B\Phi]/N\) in its linear pair operator. Subtracting precisely this quantity from (4.3) leaves

\[
\begin{split}
\frac1{2N}\{D_2[B\Phi]-2P_N[B\Phi]\}
&=\frac1N\eta_N[g]-\frac1{2N}c\\
&=\frac1N\rho[g]+\frac1{2N}c.
\end{split}
\tag{4.8}
\]

Both equalities follow by expanding (4.1) and using \(\int g=c\), already justified by (3.3)–(3.6). There is no additional \(N^{-2}\) term, no falling-factorial denominator, and no diagonal extension. In particular the scalar is not silently discarded. Its sign in the first line of (4.8) is negative because the first-marginal centering has been expanded; its coefficient in the original centered form remains the positive \(1/(2N)\).

The supplied R8 passage from compact collision stops gives the actual identity

\[
dP_N[\Phi_t]=\{-P_N[J_t]+U_3[C\Phi_t]+\ell_N(t)\}\,dt+dM_t^2,
\tag{4.9}
\]

with the genuine martingale there. The independent-particle noise and the deleted-label convention introduce no extra thermal trace. We import that domain/passage premise in its issued scope; the coefficient reconstruction above does not replace it.

## 5. Uniform pathwise bound and actual-law expectation

From (4.8), for every empirical probability measure and every \(t\),

\[
|\ell_N(t)|
\le\frac1N\eta_N[|g_t|]+\frac1{2N}|c_t|
\le\frac32D_qN^{\alpha_q-1}.
\tag{5.1}
\]

This retains both original contractions through an exact algebraic regrouping. We prove and use no assertion that \(c_t=0\). Even an additional valid scalar cancellation would only improve the bound, and is unnecessary for the frozen card.

Multiplying (5.1) by \(\sigma=\sqrt{Nb}\) and integrating gives the stronger, samplewise estimate

\[
\sigma\int_0^T|\ell_N(t)|\,dt
\le\frac32TD_q\sqrt b\,N^{\alpha_q-1/2}
=C_*\sqrt b\,N^{-\kappa_q},\qquad
\kappa_q=\frac{2q-s}{2(s+2)}>0,
\tag{5.2}
\]

where one fully explicit additional constant is

\[
\boxed{\displaystyle
C_*=\frac{3\sqrt2}{2}\,T A_q
\left[\frac{s\omega_{d-1}R^{d-s-1-q}}{d-s-1-q}
 +\frac{H_0\omega_{d-1}R^{d-q}}{d-q}+M_{K,q}^{\rm out}\right].}
\tag{5.3}
\]

Here \(A_q\) is exactly the admitted uniform R12 constant of (2.3); all other quantities are fixed and explicitly defined in (3.2). This makes the dependence on that conditional input transparent. Every newly introduced constant is independent of \(N\), the selected \(\nu\), time, and the actual particle law. The elementary exponent identity used in (5.2) is

\[
\frac{s+1-q}{s+2}-\frac12
=\frac{s-2q}{2(s+2)}=-\kappa_q.
\tag{5.4}
\]

Taking expectation in (5.2) proves the displayed THM-035 bound. It is expectation of a nonnegative, bounded time integral; Tonelli applies. The actual R6/R8 paths, started from iid Haar independently of the Brownian drivers, meet the required collision-free and domain premises almost surely. No evolved pair or triple law has been replaced by Haar, and no exponential-in-\(N\) density bound is paid: (5.1) is valid for each empirical configuration.

For completeness, the actual one-body marginal is Haar, but the proof does not need this fact. Simultaneously translating all coordinates commutes with the singular drift and the full pathwise unique equation. The iid-Haar initial law is invariant under this translation, while the Brownian increments are unchanged. Therefore the law at every deterministic time is invariant under all common translations; each one-body marginal is consequently Haar. This does not make the evolved particles independent. Using this fact instead in (5.1) also gives \(\mathbb E\eta_N[|g_t|]=\int|g_t|\le D_qN^{\alpha_q}\), with the same constant.

When \(\nu=0\), the assumed gradient estimate and the deterministic particle flow remain available, \(b=1\), and exactly (5.2) applies. No noise bracket or positive-diffusion estimate is used. If \(T=0\), both sides hold with \(C_*=0\); if \(h\) is constant, the true source and inverse vanish by the supplied uniqueness. These cases need no limiting argument.

## 6. Inclusion of the R12 critical exponent range

Suppose \(0<s<d-2\) and \(s(s+2)<2d\). If \(0<s\le2\), then

\[
2d-2>2s+2\ge3s,
\tag{6.1}
\]

where the first inequality is strict sub-Coulombity. If \(s>2\), then

\[
2d-2>s(s+2)-2
=3s+(s-2)(s+1)>3s.
\tag{6.2}
\]

Thus the strict R12 critical decay range is contained in the present \(3s<2d-2\) range, with no equality boundary added.

To verify the actual temperature hypothesis, set \(\theta=1-s/d>0\), and let

\[
\lambda_N=\beta_NN^{-\theta}\longrightarrow\lambda\in(0,\infty),\qquad
\nu_N=\beta_N^{-1}=\lambda_N^{-1}N^{-\theta}.
\]

Then

\[
\chi_N=\lambda_N^{-1}N^{2/(s+2)-\theta}
=\lambda_N^{-1}N^{s(s+2-d)/(d(s+2))}\longrightarrow0,
\tag{6.3}
\]

since \(s+2<d\). Also \(\nu_N\to0\). Hence the sequence eventually belongs to any fixed positive bounds \(L,\nu_*\); those bounds can be chosen once for its tail. If a fixed bound equals zero, it admits only the zero-noise family and has no positive-noise critical sequence, so no such sequence is being inserted into that degenerate family. Finally \(0<b_N\le1\), so the right side of (5.2) tends to zero. No hidden dependence on \(\lambda_N\) is introduced into the uniform estimate.

The old condition \(\beta_NN^{2s/d-1}\to0\), full subcriticality \(\lambda_N\to0\), and positive finite criticality remain different. For example, with \(d=3,s=1/2\), critical \(\beta_N=N^{5/6}\) makes the old expression \(N^{1/6}\). The fully subcritical choice \(\beta_N=N^{3/4}\) has \(\lambda_N=N^{-1/12}\to0\) but makes the old expression \(N^{1/12}\). This proof invokes neither old-floor smallness nor full subcriticality.

## 7. Exactly which cubic reduction follows

Let the actual integrated quantities on the same probability space be

\[
A_N=\sigma_N\int_0^T U_{3,t}[C\Phi_t]\,dt,\qquad
Z_N=\sigma_N\int_0^T\{U_{3,t}[C\Phi_t]+\ell_N(t)\}\,dt.
\tag{7.1}
\]

At each finite \(N\), the supplied R8 premise makes the cubic integrable in expected absolute time integral, so these are well-defined \(L^1\) random variables. The reverse triangle inequality and (5.2) give

\[
\left|\mathbb E|Z_N|-\mathbb E|A_N|\right|
\le\mathbb E|Z_N-A_N|
\le\sigma_N\mathbb E\int_0^T|\ell_N(t)|\,dt
\le C_*\sqrt{b_N}N^{-\kappa_q}\longrightarrow0.
\tag{7.2}
\]

Therefore \(Z_N\to0\) in \(L^1\) **if and only if** \(A_N\to0\) in \(L^1\) in the asserted critical range. Indeed the same equivalence holds along every admitted fixed-data bounded-\(\chi\) sequence. This is an exact reduction, not an estimate proving either cubic smallness or a fluctuation law.

The norms must not be conflated. The new result controls \(\mathbb E\int|\ell_N|\), which implies \(\mathbb E|\int\ell_N|\) and even the expected supremum of its time primitive. The cubic target in (7.1) is \(\mathbb E|\int U_3|\); we do not claim that it vanishes, nor infer control of \(\mathbb E\int|U_3|\) from a signed expectation. If one separately asks for the stronger absolute-time-integral cubic norm, the same reverse-triangle perturbation gives equivalence with the corresponding stronger full-residual norm, but proves neither norm small. A signed-integral cancellation alone never supplies such a stronger conclusion.

## 8. Falsification route, exact diagnostic, and dispositions

The independent falsification route for this construction is literal finite-label polynomial algebra plus exact rational exponent and boundary tests. It was written from scratch in `exact_diagnostic.py`; no prior checker or other worker result was read. It does not numerically approximate the singular inverse.

The algebra uses Gaussian rational Laurent coefficients, Haar integration by exact zero-mode extraction, the literal subset/distinct-label definition of \(U_3\), and direct differentiation of the finite-particle observable. It compares that direct generator with the full two-response decomposition for \(N=2,3,4,5\), six symmetric kernels, and zero or nonzero two-mode odd force. Physical derivatives restore a common factor \(2\pi\); the implemented force-drift identities are divided throughout by exactly that factor. The smooth one-dimensional probes test universal coefficients, not the admitted singular theorem's dimension or regularity hypotheses.

The battery checks the two response slots, \(1/N\) and \(1/(2N)\) contractions, repeated-label coefficient, background terms surviving at \(N=2\), and exact regrouping in (4.8). Mutation tests must detect an omitted scalar, halved lower coefficient, omitted response slot, falling-factorial pair denominator, and dropped \(N=2\) cubic. An explicit relative-mode probe has nonzero scalar contraction even though its centered one-body contraction vanishes. That is a warning against deleting the scalar from general algebra; it is not a claim about scalar noncancellation for the genuine inverse.

Exact rational parameter tests cover \(3\le d\le20\), denominators through 13, every positive mesh exponent strictly below \(d-2\), all six admissibility inequalities, the exponent identity, critical inclusion, and the critical bounded-\(\chi\) exponent. These finite tests support, but do not replace, the proofs for every real admitted \(s\) in Sections 2 and 6.

The adversarial boundary tests have the following precise interpretations:

| Test | What it establishes, and what it does not |
|---|---|
| \(d=7,s=4\), so \(3s=2d-2\) | \(q_-=q_+=2\), the selected exponent has zero decay, and the force-gradient radial majorant becomes \(dr/r\). The stated strict proof cannot include this boundary. This is not a counterexample to an additional structural theorem. |
| \(d=8,s=5\), still strictly below Coulomb | \(q_->q_+\); the required integrability and positive-power constraints cannot both be satisfied by this midpoint choice. |
| \(q=d-s-1\), \(q=d/2\), \(q=s/2\) | Respectively logarithmic force-gradient nonintegrability, logarithmic squared-weight nonintegrability, and zero decay power. Each strict inequality has a distinct role. |
| \(s=0\) or the Coulomb endpoint \(d=3,s=1\) | The present selected interval closes. No logarithmic normalization or endpoint claim is obtained by substitution. |
| Fixed positive noise as \(N\to\infty\) | \(\chi_N\) is unbounded. The supplied R12 uniform gradient constant cannot be invoked for this family. No unrestricted bounded-noise theorem is inferred. |
| \(d=12,s=4\), \(s(s+2)=2d\) | This noise-decay equality is outside R12's strict critical corollary, but the lower-contraction range still holds. An excluded noise boundary is not a lower-drift counterexample. |
| A deterministic time integrand \(+1\) on the first half, \(-1\) on the second | Its signed integral is zero while its absolute integral is one. This detects an invalid replacement of the norm proved in (1.3). |

The diagnostic output and its exact assertion counts are preserved in the companion `RESULTS.json` and `VERIFICATION.md`. No floating arithmetic, tolerance, random seed, simulation of the actual law, or appeal to the diagnostic as proof is involved.

| Frozen item | Construction disposition |
|---|---|
| Existence and admissibility of the prescribed midpoint | Proved here, Section 2. |
| Every weight integral and actual slice representative | Proved here from the conditional gradient/domain premises, Section 3. |
| Exact two lower coefficients and full response normalization | Reconstructed here without diagonal extension, Section 4; singular passage retains the supplied domain premise. |
| Uniform expected absolute lower-drift bound | Proved as the stronger pathwise conditional estimate, Section 5, with explicit new constant (5.3). |
| Zero noise, finite \(N=2\), all times and terminal endpoint | Included explicitly; no reciprocal, missing background cubic, or time-singular estimate. |
| Inclusion of every stated R12 critical decay range | Proved here, Section 6. |
| Full integrated residual iff cubic integrated residual | Proved conditional exact reduction, Section 7. |
| Actual cubic smallness | Open; not asserted or inferred. |
| Earlier source certification and current audit status | Unchanged and not independently determined in this construction. |

There is no first failed line in the frozen **conditional implication**. Its earliest external obligations remain the admitted genuine-inverse gradient theorem and complete-domain theorem in their issued scopes. Conditional on them, the remaining new analytic question is exactly the actual integrated cubic term in (7.1). Removing those conditional premises, proving the cubic, extending to unrestricted bounded noise, or establishing a fluctuation law requires a separately authorized round.

No canonical root file, state ledger, frozen input, commit, push, installation, or other worker output was changed. The packet is sealed before handoff; root alone may integrate or promote it after the required independent reconstruction and hostile review.
