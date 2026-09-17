# Round 001 source intake and normalization audit

- Task: `TASK-003`; authoring lane: `/root/source`, Astra Max.
- Date: 2026-09-17 UTC.
- Worktree: `/private/tmp/hocf-round001-source-20260917`.
- Branch: `codex/hocf-r001-source`.
- Baseline commit: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Common dossier: `TASKS/ACTIVE/ROUND_001_MODEL.md`, version 1.0.
- Scope: complete intake of the seven-page note and the frozen normalization. This is not an independent audit of another worker's proof, a singular-limit proof, or a literature/novelty review.
- Audit status of the present mathematical checks: `SELF_CHECKED`. The original note and provisional baseline assessment were available to this lane; no claim of blind reconstruction is made.

## Disposition

The frozen Fourier constant is correct for local singularity \(|x|^{-s}\), unit torus, and Fourier characters \(e^{2\pi i k\cdot x}\). The smooth versions of the note's finite-particle identities can be retained for reconstruction. The note's `Fact` labels do not certify their singular formulations, weighted estimates, or dynamical consequences. The transport subtraction does not prove coercivity or residual control. The weighted hierarchy and static-to-dynamic arguments retain substantial open obligations, and several literal transfers fail.

There are **26 numbered label items**: five imports I1--I5; eight Facts (1.2, 1.3, 1.4, 2.1, 2.2, 3.2, 4.1, 4.2); four Hopes; five Missing ingredients (6.1, 6.2, 6.3, 6.4, 6.6); Lemma 6.5; and three Obstructions. Every item appears below with its original label. Remark 3.1, C1--C4, equations (7), (11)--(12), and the unnumbered work-order claims are also covered.

No result from the unavailable manuscript [N], no attached numerical script, and no static local-law/free-energy theorem has been imported as a verified campaign input. Neither [N] nor the script is indispensable to the present smooth finite-particle algebra.

## Evidence and source availability

The primary supplied source is `INPUTS/note_v2.pdf`, title **Why Comm_N <= C F_N is crude, and what to replace it with**, dated September 14, 2026. Its SHA-256 is

`a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`.

All seven pages were read through `BUILD/note_v2.txt` and visually inspected after rendering. PDF page numbers and printed page numbers agree. The PDF has no embedded attachments. The PDF author metadata is empty; attribution to Sylvia Serfaty comes from `INPUTS/SOURCE_MANIFEST.md`, not an independently verified author field. This report does not change that manifest.

The note references **Fluctuations around the mean-field limit for Coulomb/Riesz flows** as [N], without an accessible manuscript, bibliography entry, theorem locations, or version in this checkout. Repository inventory found only the note PDF and the two repository utility scripts among PDF/TeX/numerical-code files. In particular, the numerical script described on note p. 3 as attached is absent, including from PDF embedded attachments. Claims about the external static free-energy program, screening bound, quadrupole reduction, and next-order logarithmic mean likewise lack source statements in the supplied materials. Their status is `UNCHECKED`, not a declaration that those results are false or unavailable everywhere.

The source's opening legend explicitly equates `Fact` with proved, `Hope` with a target, `Missing ingredient` with required input, and `Obstruction` with a limit of the proposed ideas. These are **source labels**. Campaign statuses below are separate. Unless a narrower status is explicitly given, the source claim remains `OPEN / UNAUDITED` as a campaign theorem.

## Frozen normalization and exact source mapping

| Object | Supplied note | Round 001 mapping and limitation |
|---|---|---|
| Geometry | Both torus and whole space, followed by the global formula \(g(x)=|x|^{-s}\) | Round 001 is the unit torus; the periodic kernel has this singularity only locally. Euclidean midpoint and affine-dilation formulas do not become global periodic formulas. |
| Dynamics | Drift \(N^{-1}\sum_{j\ne i}M\nabla g(x_i-x_j)-\nabla V(x_i)\), noise \(\sqrt{2/\beta}\) | Set \(M=-I\), \(K=-\nabla g\), \(b=-\nabla V\), \(\nu_N=\beta_N^{-1}\). There is no extra factor two or factor \(1/s\). |
| Force discrepancy | \(a_i=N^{-1}\sum_{j\ne i}\nabla g(x_i-x_j)-\nabla g*\mu(x_i)\) | Particle drift minus \(u\) is \(-a_i\). Even smooth \(g\) gives \(K(0)=0\); this does not remove diagonal terms from arbitrary pair statistics. |
| Energy and pair statistic | \(F_N=\tfrac12\langle g,\rho_N^{\otimes2}\rangle_{\ne}\), \(P_N[\Phi]=\tfrac12\langle\Phi,\rho_N^{\otimes2}\rangle_{\ne}\) | Exactly \(P_N=U_2/2\), with ordered distinct labels and denominator \(N^2\). |
| Deletion | Written \(x\ne y\); the proof uses \(i\ne j\) | At distinct positions and a nonatomic background these agree. For a smooth kernel with coincident particle positions, coordinate deletion differs from label deletion. The dossier's label convention governs all configurations. |
| Background | Smooth mean-field solution, with diffusion \(\beta^{-1}\Delta\mu\) | Retain dependence on \(N,\beta_N,g\). The note does not supply uniform background or propagator estimates. |
| Centering | Mean-field centering \(\rho_N=\mu_N-\mu\) | Not exact first-marginal centering; the deleted pair statistic is not expectation-centered even for iid data. |
| Fluctuation scale | I5 displays \(\sigma_N=\min(\sqrt{N\beta},\kappa_N)\) | Matches dossier. The square root covers both \(N\) and \(\beta\). For iid data \(\kappa_N=\sqrt N\) is the selected baseline scale; no CLT follows merely from selecting it. |
| Effective coupling | Hope 5.4 uses \(\beta_{\rm eff}=\beta N^{s/d-1}\) | Equals \(\lambda_N\). It is distinct from \(\beta_NN^{2s/d-1}\). |
| Logarithm | Mentioned by setting a separate interaction \(-\log|x|\) | Excluded from Round 001. The log remarks below are extracted, not adopted by substitution \(s=0\). |

For every smooth symmetric \(\Phi\), the full-product/deleted-product conversion is

\[
U_2[\Phi]=\langle\Phi,\rho^{\otimes2}\rangle
-\frac1N\langle\Phi(x,x),\eta\rangle.
\]

Consequently, under iid particles of law \(\mu\),

\[
\mathbb E U_2[\Phi]= -\frac1N\iint\Phi(x,y)\mu(x)\mu(y)\,dx\,dy.
\]

These follow by expanding the ordered sums: the off-diagonal empirical expectation is \((1-1/N)\mu\otimes\mu\). They show why neither a full-product Itô trace nor an iid centering can be transferred silently to the deleted statistic. For the smooth commutator kernel the diagonal vanishes, so this particular correction is zero. For \(\Phi=g_\varepsilon\) it is generally nonzero.

### Fourier constant: primary-source check and direct calculation

The only external mathematical input checked in this lane is the Riesz normalization in Bartłomiej Dyda, Alexey Kuznetsov, and Mateusz Kwaśnicki, **Fractional Laplace operator and Meijer G-function**, [arXiv:1509.08529v1](https://arxiv.org/pdf/1509.08529v1), §1.1, printed pp. 3--4, equations (7), (8), (11), (12). Equations (7)--(8) give the kernel normalization for \(0<\alpha<d\); (11)--(12) specify its multiplier and Fourier convention. The inspected version was submitted September 28, 2015; its PDF title page is dated September 30, 2015. Its downloaded PDF SHA-256 is `ea30437da8dd70139b17e29d3a0007c4d05e9ec98a79df2524b696359d59a06c`. This is `PRIMARY_VERIFIED / VERSION_LOCKED` for these formulas only; no proposition or fluctuation theorem is imported.

In that convention,

\[
\gamma_d(\alpha)
=\frac{2^\alpha\pi^{d/2}\Gamma(\alpha/2)}{\Gamma((d-\alpha)/2)},
\qquad
\mathcal F_{+i}[|x|^{\alpha-d}](\xi)
=\gamma_d(\alpha)|\xi|^{-\alpha}.
\]

Putting \(\alpha=d-s\) and \(\xi=2\pi k\) gives

\[
c_{d,s}|k|^{s-d},\qquad
c_{d,s}
=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},
\]

exactly the dossier constant. The transform sign has no effect because the kernel is even. This mapping is our calculation from the cited formulas.

A direct check uses

\[
|x|^{-s}=\frac1{\Gamma(s/2)}\int_0^\infty t^{s/2-1}e^{-t|x|^2}\,dt,
\quad
\mathcal F_{2\pi}(e^{-t|x|^2})(\xi)
=(\pi/t)^{d/2}e^{-\pi^2|\xi|^2/t}.
\]

The substitution \(u=\pi^2|\xi|^2/t\) gives the same constant for \(\xi\ne0\); the calculation is justified distributionally by testing against Schwartz functions and truncating the positive parameter integral. In particular, the value \(s=d-2\), \(d>2\), yields

\[
-\Delta g=(d-2)|\mathbb S^{d-1}|(\delta_0-1)
\]

on the unit torus. For \(d=3,s=1\), the Fourier coefficient is \((\pi|k|^2)^{-1}\), and the preceding constant is \(4\pi\). This is a normalization check, not permission to discard the delta term in singular Itô calculus.

To check the asserted local principal singularity rather than simply sample a Euclidean transform, put \(a=(d-s)/2\), let \(H_t\) be the mass-one torus heat kernel, and define

\[
g(x)=\frac{2^{d-s}\pi^{d/2}}{\Gamma(s/2)}
\int_0^\infty t^{a-1}(H_t(x)-1)\,dt.
\]

The integral converges in \(L^1\): near zero use \(\|H_t-1\|_1\le2\) and \(a>0\); at infinity use the exponentially converging Fourier series. The zero coefficient is zero. For \(k\ne0\), integration gives exactly \(c_{d,s}|k|^{s-d}\). In the Gaussian periodization of \(H_t\), the zero image integrated over all positive times contributes \(|x|^{-s}\). The nonzero images for small time, the subtracted constant, and the large-time difference give a smooth function near zero. Thus the displayed periodic kernel has the claimed local singularity with coefficient one.

Heat regularization \(e^{\varepsilon\Delta}g\) multiplies its coefficients by \(e^{-4\pi^2\varepsilon|k|^2}\), as frozen. It is smooth, even, real, and zero mean for every fixed positive \(\varepsilon\). No estimate uniform as \(\varepsilon\downarrow0\) has been obtained here.

An immediate transfer issue follows: a nonzero integrable zero-mean periodic kernel with a positive singularity takes negative values. Hence Missing ingredient 6.6's pointwise interval \(\tfrac12g\le g_\theta\le\tfrac32g\) is empty wherever \(g<0\). This is a literal `SOURCE_MISMATCH` under the frozen normalization. A different, explicitly normalized comparison of singular parts may be possible, but has not been substituted into the source claim.

## Complete labeled extraction

### Imported from [N] 1.1, I1 -- p. 1

**Source statement.** \(F_N(X,\mu)\ge-o_N\) for every configuration, with \(o_N\asymp N^{s/d-1}\), and a logarithmic contribution \(\log N/N\) when \(s=0\).

**Campaign status.** `OPEN`; source `UNCHECKED`. This is an asserted import, not proved by the note. [N]'s theorem, interaction normalization, geometry, density hypotheses, dependence of constants, and precise logarithmic statement are unavailable. Do not turn an order notation into a uniform lower bound for all dossier parameters. Collision configurations, if admitted in a singular energy, need their extended-value convention. The logarithmic phrase is preserved without merging it into the positive-power regime.

### Imported from [N] 1.1, I2 -- p. 1

**Source statement.** \(|\operatorname{Comm}_N(v)|\le C\|v\|_* (F_N+o_N)\).

**Campaign status.** `OPEN`; source `UNCHECKED`. The norm \(\|v\|_*\), allowed exponents/geometries, regularity, and constants are unspecified here. The note says that only I2 is questioned, but that is not a campaign verification of I1 or I3--I5. A Fourier normalization change must also be propagated into this imported inequality.

### Imported from [N] 1.1, I3 -- p. 1, equation (3) on p. 2

**Source statement.** Well-posedness and regularity of the backward linearized equation, defining \(U^{r,t}\).

**Campaign status.** `OPEN`; source `UNCHECKED`. Neither functional domain nor dependence on \(\beta_N\), the background, time, or cutoff is supplied. At fixed smooth coefficients this is a separate analytic task; it does not authorize a cutoff-uniform propagator for the singular kernel.

### Imported from [N] 1.1, I4 -- p. 1

**Source statement.** A central limit theorem for the martingale part.

**Campaign status.** `OPEN`; source `UNCHECKED`. The initial law, covariance, normalization, mode/topology of convergence, and joint convergence with initial fluctuations are not stated. Corrector martingales can change this covariance and cannot be covered merely by citing the old martingale theorem.

### Imported from [N] 1.1, I5 -- p. 1

**Source statement.** \(\sigma_N=\min(\sqrt{N\beta},\kappa_N)\), with \(\kappa_N\) the initial fluctuation scale, together with the exponent \(\gamma\) of an \(H^{-\gamma}\) field theorem and its master rate.

**Campaign status.** Scale convention matches the dossier; the field exponent and master rate are `OPEN / UNCHECKED`. There is no actual master-rate formula in these seven pages. Hope 5.3 later states \(\gamma=m_*+d+3\), but does not define \(m_*\). No field theorem or initial-law assumption is imported from this entry.

### Fact 1.2 (corrector identity) -- pp. 1--2, equation (1)

**Source statement.** With

\[
\mathcal A\Phi=\partial_t\Phi+u(x)\cdot\nabla_x\Phi+u(y)\cdot\nabla_y\Phi
+\beta^{-1}(\Delta_x+\Delta_y)\Phi,
\quad
b_i[\Phi]=\frac1N\sum_{j\ne i}\nabla_x\Phi(x_i,x_j)-\int\nabla_x\Phi(x_i,y)\mu(y)\,dy,
\]

and \(\mathcal T_N[\Phi]=N^{-1}\sum_i(Ma_i)\cdot b_i[\Phi]\), the source asserts

\[
dP_N[\Phi]=\tfrac12\langle\mathcal A\Phi,\rho_N^{\otimes2}\rangle_{\ne}\,dt
+\mathcal T_N[\Phi],dt
+\frac{\sqrt{2/\beta}}N\sum_i b_i[\Phi]\cdot dW_i.
\tag{source 1}
\]

**Campaign status.** `EXACT_IDENTITY` for fixed smooth data and label deletion, at most `SELF_CHECKED` in this source lane; singular statement `FORMAL_IDENTITY`. The printed proof expands all three particle/background terms and is consistent at smooth coefficients. Merely being \(C^{1,2}\) off the diagonal does not justify integration against a smooth background, integration by parts across the diagonal, collision passage, or the singular stochastic integrals. Quadratic and cross variations are not provided. Also, \(\mathcal A\) is independent transport/diffusion in the two slots: the unexpanded \(\mathcal T_N\) still contains quadratic background response, upward terms, and finite-particle contractions. This display is not already the full linearized pair hierarchy sought in Round 001.

### Fact 1.3 (energy identity) -- p. 2, equation (2)

**Source statement.** Taking \(\Phi=g\) yields

\[
dF_N=\left[\tfrac12\operatorname{Comm}_N(u)+\frac1N\sum_i a_i^TSa_i
+\beta^{-1}\langle\Delta g,\rho_N^{\otimes2}\rangle_{\ne}\right]dt
+\frac{\sqrt{2/\beta}}N\sum_i a_i\cdot dW_i.
\tag{source 2}
\]

The middle term is \(-D_N\) for \(M=-I\).

**Campaign status.** `EXACT_IDENTITY` at fixed smooth kernel by specialization of (1); singular statement `FORMAL_IDENTITY`. The coefficient and gradient-flow sign agree with the dossier. For singular Riesz kernels, \(\Delta g\) is not generally an ordinary locally integrable function, and in the Coulomb case its diagonal distribution is essential. The deleted-diagonal notation does not itself prescribe the regularized limit of the particle/background terms or the martingale bracket. No cutoff passage is supplied.

### Fact 1.4 (duality identity) -- p. 2, equations (3)--(4)

**Source statement.** Define

\[
\psi_f(y)=\int\nabla f(x)\cdot M\nabla g(x-y)\mu(x)\,dx,
\qquad \mathcal L_\mu f=u\cdot\nabla f+\beta^{-1}\Delta f+\psi_f.
\]

Then

\[
d\langle f,\rho_N\rangle
=\langle\partial_t f+\mathcal L_\mu f,\rho_N\rangle dt
+\tfrac12\operatorname{Comm}_N(M^*\nabla f)dt
+\frac{\sqrt{2/\beta}}N\sum_i\nabla f(x_i)\cdot dW_i.
\]

For \(f^r=U^{r,t}\phi\) with terminal value \(\phi\),

\[
\langle\phi,\rho_N^t\rangle
=\langle U^{0,t}\phi,\rho_N^0\rangle+M_N^t[f]
+\tfrac12\int_0^t\operatorname{Comm}_N(M^*\nabla f^r)\,dr.
\tag{source 4}
\]

**Campaign status.** Smooth identity `EXACT_IDENTITY / SELF_CHECKED`; existence and uniform estimates for its backward solution remain separate; singular use `FORMAL_IDENTITY` until justified. Its sign and half factor map to \(M=-I\), \(v=-\nabla f\). The following source assertion that the first two terms yield the limiting law relies on I3, I4 and initial fluctuation assumptions, not the displayed identity alone. The claimed sufficient smallness of the integrated last term must specify its probability mode, time/test uniformity, and joint convergence requirements.

### Fact 2.1 (force form) -- pp. 2--3, equation (5)

**Source statement.** For the scalar contraction
\(h_v(x)=\int\nabla g(x-y)\cdot v(y)\mu(y)\,dy\),

\[
\operatorname{Comm}_N(v)=\frac2N\sum_i v(x_i)\cdot a_i+2\langle h_v,\rho_N\rangle.
\tag{source 5}
\]

**Campaign status.** `EXACT_IDENTITY` for smooth periodic data, `SELF_CHECKED`; singular extension conditional on definitions and finiteness. Oddness gives the printed sign. Convolution of a periodic distribution with a smooth function is smooth, but for some \(s\) the written gradient integral requires a distribution/principal-value interpretation. In whole space, smoothness without decay or growth assumptions is insufficient to justify every convolution.

The p. 3 numerical claim uses \(\mathbb T^1\), \(s=1/2\), \(\mu=1\), \(v=\sin(2\pi x)\), and \(N=200,400,800\), reporting agreement to \(10^{-11}\). Its script, particle configurations, periodic-kernel prescription, precision, and seed are unavailable. Status: source-reported numerical observation, **not `REPRODUCED`**. Equation (5) does not need that computation for smooth algebra, and the script is not indispensable here.

### Fact 2.2 (stress form) -- p. 3, equation (6)

**Source statement.** For Euclidean \(m=(x+y)/2\), \(z=x-y\), \(E_v=\operatorname{sym}\nabla v\),

\[
e_N=\tfrac12\iint_{\ne}g(z)\delta_m\,d\rho_N^{\otimes2},\qquad
S_N^\circ=-s\iint_{\ne}|z|^{-s-2}(z\otimes z)^\circ\delta_m\,d\rho_N^{\otimes2},
\]

the source gives \(e_N(\mathbb D)=F_N\) and

\[
\operatorname{Comm}_N(v)
=-\frac{2s}{d}\langle\operatorname{div}v,e_N\rangle
+\langle E_v^\circ,S_N^\circ\rangle
+\langle r_v,\rho_N^{\otimes2}\rangle_{\ne},
\qquad |r_v|\le C\|\nabla^2v\|_\infty |z|^{1-s}.
\tag{source 6}
\]

It further gives \(\operatorname{Comm}_N(a\operatorname{Id})=-2saF_N\), and in one dimension \(\operatorname{Comm}_N(v)=-2sF_N^{w_v}\), \(w_v=(v(x)-v(y))/(x-y)\). Its separate logarithmic remark is a compression term \(-d^{-1}\langle\operatorname{div}v(m),\rho_N^{\otimes2}\rangle_{\ne}\) and \(\operatorname{Comm}_N(a\operatorname{Id})=a/N\).

**Campaign status.** `CONDITIONAL` Euclidean identity when the displayed integrals exist and the required derivative bound holds; `SOURCE_MISMATCH` for literal global use on the frozen torus. A torus has no globally defined midpoint of this form, a nonzero affine dilation is not a periodic vector field, and its Riesz kernel does not globally satisfy \(z\cdot\nabla g=-sg\). Local coordinates plus the smooth periodic remainder must be retained. The measures are signed; their total mass does not control their total variation. The logarithmic formula uses a distinct kernel and is not promoted.

The ensuing assertion identifying (5) and (6) with an exact Irving--Kirkwood force-divergence identity is not established: exact pair stress is distributed along the bond, whereas the source's stress is at its midpoint and has a Taylor remainder. No primary stress theorem or global periodic construction is imported.

### Fact 3.2 (renormalized energy: no forcing, no floor) -- p. 4, equation (8)

**Source statement.** For a local-structure coefficient \(\varepsilon_s\), stated to be \(\zeta(s)\) for a one-dimensional zero-temperature lattice, set

\[
\bar e_N=\varepsilon_sN^{s/d-1}\mu^{1+s/d}\,dx,
\quad \bar F_N=\bar e_N(\mathbb D),\quad G_N=F_N-\bar F_N.
\]

The source states

\[
\frac d{dt}G_N
=-\frac{s}{d}\langle\operatorname{div}u,e_N-\bar e_N\rangle
+\tfrac12\langle E_u^\circ,S_N^\circ\rangle
+\tfrac12\langle r_u,\rho_N^{\otimes2}\rangle_{\ne}
+\frac1N\sum_i a_i^TSa_i+\beta^{-1}(\cdots).
\tag{source 8}
\]

It concludes that the compression forcing and self-energy floor have been removed.

**Campaign status.** Deterministic transport cancellation is a `CONDITIONAL` algebraic observation under the Euclidean stress formula; coercivity/floor removal is `OPEN`, and the displayed finite-temperature pathwise equation needs repair. The source proof explicitly leaves diffusion in an ellipsis but also omits the martingale of (2). Subtracting deterministic \(\bar F_N\) does not remove that martingale. At fixed smooth kernel its bracket density is \(2(\beta N^2)^{-1}\sum_i|a_i|^2\), so it cannot be silently represented as a deterministic drift. For example, on the unit circle take \(g(x)=\cos(2\pi x)\), \(\mu=1\), \(V=0\), \(N=2\), and positions \(0,1/4\): \(a_1=\pi\), \(a_2=-\pi\), and the bracket density is \(\pi^2/\beta>0\).

Subtracting a scalar neither bounds the signed local energy residual nor controls shear or endpoint excesses. The coefficient \(\varepsilon_s\), its law/temperature dependence, and the claimed \(\zeta(s)\) normalization need a source or proof; for \(0<s<1\) the unrenormalized lattice sum is divergent. The later identification with the static charge sum rule and the claimed \(-1/4\) logarithmic mean coefficient is `UNCHECKED`. Neither compression-side completion nor a pressure coefficient has been certified by this subtraction.

### Fact 4.1 (d = 1: the hierarchy closes exactly) -- pp. 4--5, equations (9)--(10)

**Source statement.** For symmetric smooth \(w\), \(M=\pm1\), set

\[
\widetilde w=\frac{\partial_xw-\partial_yw}{x-y},\quad
D_N^w=\frac1N\sum_iw(x_i,x_i)|a_i|^2.
\]

The source repeats (9), \(\operatorname{Comm}_N(v)=-2sF_N^{w_v}\), and states

\[
dF_N^{w^r}
=\left[F_N^{\mathcal Aw}-sF_N^{ww_u}-2s\beta^{-1}F_N^{\widetilde w}
+\beta^{-1}\langle wg'',\rho_N^{\otimes2}\rangle_{\ne}
+MD_N^w+R_N^w\right]dr+d(\mathrm{mart.}),
\tag{source 10}
\]

where

\[
R_N^w=\frac MN\sum_i a_i\int_{\ne}
\big[(w(x_i,y)-w(x_i,x_i))g'(x_i-y)+\partial_xw(x_i,y)g(x_i-y)\big],d\rho_N(y).
\]

It labels every kernel in this remainder less singular than \(g\), claims closure modulo weighted dissipation and these remainders, and asserts a definite sign in gradient flow.

**Campaign status.** `FORMAL_IDENTITY` for the singular Euclidean calculation; exact smooth product rules survive before invoking the homogeneity formulas. The literal global torus formula is a `SOURCE_MISMATCH`. The claimed singularity improvement is false in general, as the local check below shows. The dissipation sign requires \(w(x_i,x_i)\ge0\); symmetry alone is insufficient. Also, \(M=+1\) is outside the original one-dimensional assumption \(\operatorname{sym}M\le0\). No finite-temperature singular \(g''\) passage is provided. Broken references `(??)` appear in its proof and consequences.

For the local check, put \(y=x-z\), \(g(z)=|z|^{-s}\). Then

\[
(w(x,x-z)-w(x,x))g'(z)+\partial_xw(x,x-z)g(z)
=(1+s)\partial_1w(x,x)|z|^{-s}+O(|z|^{1-s}),
\]

because symmetry gives \(\partial_1w(x,x)=\partial_2w(x,x)\). A nonzero diagonal derivative retains the original singularity. This is a `COUNTEREXAMPLE` to the source's universal singularity claim, with audit status `SELF_CHECKED`; it is not a proof that all integrated remainders are large.

### Fact 4.2 (d >= 2: what closes) -- p. 5

**Source statement.** The scalar-weighted hierarchy closes if and only if \(E_u^\circ=0\), described as dilational flows in every dimension and conformal flows in the two-dimensional logarithmic case; otherwise scalar energy couples to traceless stress and then further multipoles. Its calculation uses

\[
\mathcal A(wg)=(\mathcal Aw)g+wK_u
+2\beta^{-1}(\nabla_xw-\nabla_yw)\cdot\nabla g+2\beta^{-1}w\Delta g.
\]

**Campaign status.** `OPEN` as an if-and-only-if closure theorem. The local shear coefficient \(z\cdot E_u^\circ z/|z|^2\) is direction-dependent for nonzero traceless strain, which is a valid warning against replacing it by an arbitrary smooth scalar weight at the diagonal. It does not prove the full stated hierarchy theorem, finite closure, an infinite cascade, or sufficiency at positive temperature. The diffusion term is still singular even with zero shear. Weights vanishing at the diagonal and the permitted remainder class matter for any precise necessity statement. The source's Euclidean calculation and characterization of flows also require separate periodic and logarithmic treatments.

### Hope 5.1 (d = 1, beta = infinity, gradient flow, lattice-like data) -- p. 5

**Source statement.** For \(0<s<1\), a perturbed \(\mu^0\)-quantile lattice and \(\kappa_N\ll N^{1-s+\delta}\),

\[
\mu_N^t=\mu^t+N^{s-1}\nu^t+o(N^{s-1}\wedge\kappa_N^{-1}),
\quad
\partial_t\nu=\mathcal L_\mu^*\nu+s\Delta(\zeta(s)\mu^{1+s}),\quad\nu^0=0.
\]

It predicts transport of \(\kappa_N(\rho_N^t-N^{s-1}\nu^t)\) by \(U\), identifies the correction as correlation-hole pressure, and says that only Missing ingredients 6.1 and 6.2 remain.

**Campaign status.** `OPEN`, not an established conditional theorem. The topology and probability mode of the little-o term, perturbation class, uniformity in time, and \(\delta\) are unspecified. Literal total-variation convergence of atomic to smooth measures would fail. The pressure coefficient and initial centering require verification. Equations (11)--(12) also need the geometry, sign, and endpoint-excess repairs recorded below. Thus the assertion that precisely two inputs suffice has not been proved. This is a zero-temperature prepared-law target, not the iid positive-temperature flagship.

### Hope 5.2 (renormalized energy estimate, any d, any u) -- p. 6

**Source statement.** Under Missing ingredients 6.3--6.4, \(G_N^t\le G_N^0+o(N^{s/d-1})\) in Regime P, with no exponential factor or additive floor; consequently \(F_N^t=\bar F_N^t+o(N^{s/d-1})\). It singles out dilational and incompressible flows as immediately accessible cases.

**Campaign status.** `OPEN`; the stated hypotheses do not yet establish this implication. The inputs are bounds on means, while the conclusion is written without an expectation or probability mode. An upper increment bound does not imply two-sided smallness without initial excess preparation and an appropriate lower bound. Diffusion, martingale, signed local energy and shear remain. A dilation is not periodic; incompressibility removes the compression term but need not remove traceless strain. General \(u\) also does not by itself prescribe dissipative particle dynamics.

### Hope 5.3 (the field theorem's gamma) -- p. 6

**Source statement.** [N]'s field exponent \(\gamma=m_*+d+3\) allegedly comes from the commutator test norm. The stress/force rewritings should leave only adjoint regularity and martingale summability; the source asserts a Fourier gain \(|k|^{-1}\) from the Riesz potential.

**Campaign status.** `OPEN / HEURISTIC`; no improved topology theorem is supplied. The asserted universal Fourier gain is not compatible with all \(s,d\). In homogeneous background, for the gradient model and \(v=-\nabla\phi_k\), the exact multiplier of \(h_v\) is \(4\pi^2c_{d,s}|k|^{s-d+2}\phi_k\). Relative to \(v\), convolution by \(\nabla g\) has order \(s-d+1\), which is not uniformly a gain of one derivative. The claimed gamma and \(m_*\) remain source-unverified, and improved finite-dimensional estimates do not supply field tightness.

### Hope 5.4 (Regime P, positive temperature) -- p. 6

**Source statement.** In gradient flow, \(\beta_{\rm eff}=\beta N^{s/d-1}\to0\), with iid data, a Poisson cloud with a hole of size \(\ell_B=(\beta/N)^{1/s}\) should make stress negligible and local energy concentrate. It proposes replacing [N]'s Assumption MF by \(\sigma_N e_N\to0\), where here \(e_N\) denotes the size of the **mean commutator**, and conjectures

\[
e_N\asymp \beta N^{-1}\vee\beta^{d/s-1}N^{1-d/s}.
\]

It then predicts \(s<2d/3\) at scale \(\sqrt N\), with a Debye correction beyond, and calls the route conditional on Missing ingredient 6.6. It explicitly acknowledges previous overstatement.

**Campaign status.** `HEURISTIC / OPEN`. The scalar \(e_N\) here must not be confused with the earlier signed local-energy measure. A mean commutator does not control the centered random time integral needed in (4). No dynamic replacement from iid to the modulated Gibbs inputs is proved. The weak-coupling power count \(N\ell_B^d=\beta_{\rm eff}^{d/s}\) is an exact algebraic equality at the selected density scale, not a cluster expansion or relaxation theorem.

At \(\sigma_N=\sqrt N\), the displayed conjecture would require both \(\beta/\sqrt N\to0\) and \(\beta^{d/s-1}N^{3/2-d/s}\to0\). The stated threshold \(s<2d/3\) follows in the fixed-positive-\(\beta\) situation; it is not sufficient for arbitrary growing \(\beta_N\) in the full subcritical regime. No Debye coefficient or critical law is given.

### Missing ingredient 6.1 (localized lower bound, d = 1) -- p. 6

**Source statement.** For every smooth symmetric \(w\ge0\), every \(X\), and \(\mu\in C^1\) bounded below,

\[
F_N^w(X,\mu)\ge\zeta(s)N^{s-1}\int w(x,x)\mu^{1+s}(x)\,dx
-C\|w\|_{C^1}N^{s-1-\delta}.
\]

**Campaign status.** The unrestricted weight class is not safe: `COUNTEREXAMPLE` by the elementary separated-support construction below, `SELF_CHECKED` only. Neither \(\delta\), constant dependence, nor the cited screening source is specified.

Choose disjoint small arcs \(A,B\) on the unit circle whose pair separations lie in a region where the frozen periodic kernel is smooth and positive. Choose smooth nonnegative \(a,b\), supported in those arcs, with \(a=1\) on a smaller arc and \(b\not\equiv0\). Define

\[
w(x,y)=\frac{a(x)b(y)+b(x)a(y)}{g(x-y)}
\]

on a neighborhood of these separated product supports, and extend it by zero. Supports can be chosen compactly inside that neighborhood, so the extension is smooth, symmetric, nonnegative, and identically zero near the diagonal. Take \(\mu=1\) and distinct particle positions all in the smaller arc. Then

\[
F_N^w=\langle a,\rho_N\rangle\langle b,\rho_N\rangle
=-(1-\textstyle\int a)\int b<0,
\]

uniformly in \(N\), whereas the proposed right-hand side is \(-C\|w\|_{C^1}N^{s-1-\delta}\to0\) for any \(\delta>0\). This disproves the literal universal bound in the frozen periodic normalization. The same construction works with the positive Euclidean kernel on separated supports whenever the background class makes sense. Additional structural conditions on the weighted kernel are necessary; pointwise \(w\ge0\) is insufficient. This does not disprove restricted localized lower bounds with such conditions.

### Missing ingredient 6.2 (less singular remainders) -- p. 6

**Source statement.** \(\int_0^t|R_N^w|\,dr=o(N^{s/d-1})\) for the kernels in (10), described as \(|z|^{-s}\) times a diagonally vanishing weight or \(|z|^{1-s}\).

**Campaign status.** `OPEN`. The singularity premise is false for general \(w\), by the expansion under Fact 4.1. Even genuine improvement of a kernel's local degree would not by itself bound its signed empirical quadratic form or its product with the singular force \(a_i\). The statement omits the law/configuration preparation, uniformity in the generated weights, and the mode of convergence.

### Missing ingredient 6.3 (local equilibrium of the energy density) -- p. 6

**Source statement.**

\[
\big|\mathbb E\langle\operatorname{div}u,e_N-\bar e_N\rangle\big|
\le\varepsilon_N\|\nabla u\|_\infty N^{s/d-1},\qquad\varepsilon_N\to0.
\]

It equates this with concentration of mesoscopic local energy and identifies the localization error with a static almost-additivity surface defect of relative size \(\ell^{-1}N^{-1/d}\) per box.

**Campaign status.** `OPEN`. The displayed absolute expectation is not \(\mathbb E|\cdot|\), variance control, or concentration. The law, conditioning, localization, topology of measures, density/temperature uniformity, and time range must be specified. The static surface estimate and its normalization are not supplied, and no dynamic interface proves that its hypotheses hold. Even the claimed mean estimate would leave the random residual required by the fluctuation theorem open.

### Missing ingredient 6.4 (isotropy of the local stress) -- pp. 6--7

**Source statement.**

\[
\big|\mathbb E\langle E_u^\circ,S_N^\circ\rangle\big|
\le\varepsilon_N\|\nabla u\|_\infty N^{s/d-1},\qquad\varepsilon_N\to0.
\]

After Lemma 6.5, the source proposes \(\tau_{\rm relax}\asymp\beta N^{-2/d}\), anisotropy of order \(\tau_{\rm relax}\|\nabla u\|_\infty\), and \(\varepsilon_N\asymp\beta N^{-2/d}\) in Regime P. Regime R is linked to an angular curvature-weighted local law at the moving density.

**Campaign status.** `OPEN`, with the relaxation scaling `HEURISTIC`. The exact isotropy hypothesis of Lemma 6.5 is not established for the actual conditional dynamics. A vanishing mean does not control a centered random shear residual. The proposed time scale need not vanish merely from subcriticality:

\[
\beta_NN^{-2/d}=\lambda_NN^{1-(s+2)/d}.
\]

If \(s<d-2\), a sufficiently slow \(\lambda_N\downarrow0\) makes this expression grow. If \(s\ge d-2\), its vanishing under subcriticality still does not prove relaxation. Regime R and its external angular local law are not quantitatively defined by the note.

### Lemma 6.5 (rotation) -- pp. 6--7

**Source statement.** A symmetric traceless matrix invariant under a planar rotation of order at least three, and in dimension at least three under generators of an irreducibly acting rotation group, is zero. The source concludes that a local pair-stress expectation vanishes if the relevant conditional law is invariant under those rotations.

**Campaign status.** The finite-dimensional algebra is `PROVED_CANDIDATE / SELF_CHECKED`; the probabilistic application is `CONDITIONAL`. In two dimensions the action on the two-dimensional traceless symmetric subspace has angle twice the original rotation angle and no nonzero fixed vector for these orders. In higher dimensions, invariance means commutation with the group; every eigenspace of a symmetric matrix is invariant. Irreducibility forces a single eigenvalue, and zero trace forces zero. This proof needs no unverified appeal to a real-version Schur lemma.

For the expectation conclusion, require integrability, covariance of the observable, invariance of the chosen box/weight and background, and invariance of the **conditional** law. Conditioning on a fixed exterior configuration generally breaks rotation symmetry. In dimensions at least three a single planar rotation does not suffice; the irreducibility hypothesis is essential. This lemma concerns an expectation, not concentration.

### Missing ingredient 6.6 (static inputs for Hope 5.4) -- p. 7

**Source statement.** For

\[
Q_\theta\propto\exp\left[-\frac\beta{2N}\sum_{i\ne j}g_\theta(x_i-x_j)
+\sum_i(\text{one-body})\right]\mu^{\otimes N},
\quad \tfrac12g\le g_\theta\le\tfrac32g,
\]

the note requires (i) \((\log Z_N)/(\beta N)=o(N^{s/d-1})\); (ii) \(\sup_\theta|\mathbb E_{Q_\theta}\operatorname{Comm}_N(v)|=o(N^{s/d-1})\); and (iii) sub-Gaussian linear statistics. It argues that \(e^{-\beta g/N}\le1\) suppresses close pairs and identifies one-body renormalization as the main difficulty.

**Campaign status.** `OPEN`; literal periodic comparison is `SOURCE_MISMATCH`, for the sign reason proved above. The assertion \(e^{-\beta g/N}\le1\) is also false on the negative part of the zero-mean periodic kernel, though a local singular suppression may still hold. The one-body term, its additive constant, the tilt family, normalization of \(Z_N\), and the quantitative meaning of sub-Gaussian are unspecified. Adding a constant to the one-body exponent changes (i) without changing the probability law, so (i) is not even invariant until that normalization is fixed. No uniform moving-background static theorem, entropy transfer, or iid-to-Gibbs bridge is supplied. These are requested inputs, not imported results.

### Obstruction 7.1 (shear) -- p. 7

**Source statement.** Nonzero traceless strain prevents scalar closure in dimensions at least two; Missing ingredient 6.4 is said to be exactly the missing piece, identical to a static quadrupole \(Q_0\). Resolving that quadrupole plus Missing ingredient 6.3 is claimed to give Regime R; otherwise the route does not pass weak coupling.

**Campaign status.** `OPEN` as an impossibility or sufficient-reduction theorem. Local directional shear is a genuine structural issue for the proposed scalar smooth-weight ansatz, but it is not a proof that the full pair/higher hierarchy cannot close or resum. Neither \(Q_0\), the conditional static reduction, nor its dynamic law/temperature mapping is provided. Random residual, singular passage, and centering obligations are additional to the displayed mean inputs.

### Obstruction 7.2 (Coulomb borderline at zero temperature) -- p. 7

**Source statement.** At \(\beta=\infty\), \(s=d-2\), microscopic motion is of order one per unit time, so local structure is neither transported nor relaxed and no temperature expansion is available.

**Campaign status.** `HEURISTIC`, not an obstruction theorem. At separation \(N^{-1/d}\), the single-pair force scale divided by that separation is \(N^{(s+2)/d-1}\), equal to one at the stated Coulomb exponent. This power count does not prove nontransport or nonrelaxation; cancellation and stationary configurations can eliminate motion. For positive-power Coulomb the row requires \(d>2\); the two-dimensional logarithm is a separate model. No universal impossibility is inferred.

### Obstruction 7.3 (non-gradient flows) -- p. 7

**Source statement.** Hope 5.4 needs an entropy bound relative to \(Q_N\), allegedly supplied by modulated free energy only in gradient flow, and (10) loses the sign of \(MD_N^w\).

**Campaign status.** `OPEN` as stated, with a valid warning about dissipation and ensemble compatibility. No precise entropy theorem is given. The original class \(\operatorname{sym}M\le0\) still has \(a^TSa\le0\), including some nongradient matrices; with a nonnegative scalar weight the same quadratic sign survives. Pure skew flow gives zero rather than strict dissipation. Thus losing all sign is not a universal property of every nongradient flow. Equation (10)'s \(M=\pm1\) scalar comparison does not establish the full multidimensional claim.

## Other claims needed to interpret the labels

### Opening diagnosis and C1--C4 -- pp. 1, 3--4

The note's revision history first identifies an earlier excessive focus on the additive floor, then an earlier unjustified incompressibility assumption. This records the source's own change of position; it is not a campaign retraction of a previously promoted result.

**Incompressibility.** The claim that incompressibility is confined to the Hamiltonian logarithmic case is too broad. For constant skew \(M\), \(\operatorname{div}(M\nabla(g*\mu))=0\) for every sufficiently defined smooth convolution, independently of the Riesz exponent. Under the note's stated confinement, however, \(\operatorname{div}u=-\Delta V\); selecting \(M=J\) alone does not make its full velocity divergence-free. In the periodic setting a harmonic smooth \(V\) is constant. This limitation affects every later Hamiltonian/incompressible example.

**C1 and equation (7).** The source claims that compression is exactly transport of \(\bar e_N\), through

\[
\frac d{dt}\int\mu^{1+s/d}
=-\frac{s}{d}\int\mu^{1+s/d}\operatorname{div}u.
\tag{source 7 premise}
\]

At zero diffusion this is correct, provided boundary terms vanish. At finite temperature, with \(p=1+s/d\), the full calculation is

\[
\frac d{dt}\int\mu^p
=-(p-1)\int\mu^p\operatorname{div}u
-\beta^{-1}p(p-1)\int\mu^{p-2}|\nabla\mu|^2.
\]

The source later acknowledges diffusion in Fact 3.2, but equation (7) itself is not an exact positive-temperature identity as printed. The approximation \(e_N\approx\bar e_N\) is an additional local-equilibrium assertion, not proved by transport.

**C2.** Localization can retain information discarded by a global bound. This is a diagnostic observation. The source's signed local-energy measure is not determined or controlled in total variation by its mass, so the suggested mass-versus-distribution language supplies no new norm estimate.

**C3.** Vanishing expected traceless stress under an invariant law is distinguished from vanishing stress for each configuration. The proposed relaxation-time times strain-rate bound is exactly the open input discussed under Missing ingredient 6.4.

**C4.** The additive completed-energy term has scale \(N^{s/d-1}\); the source calls it a floor. I1 is a negative lower bound, so this language must not be read as \(F_N\) being positive or bounded below by a positive quantity of that size. Subtraction does not make the remaining signed quantity small.

**Remark 3.1.** The source correctly warns that separately bounding the two terms in (5) can destroy cancellation of their linear parts, and that antisymmetrization near the diagonal returns a stress/energy term. The displayed Cauchy--Schwarz diagnostic is not a replacement fluctuation estimate. The further far-field smoothness claim can hold after a specified cutoff, but the cutoff dependence and matching error have not been supplied. No improved rate follows here.

### Consequences of Fact 4.1 -- p. 5, equations (11)--(12)

**Consequence (a), source label: the remainder becomes an explicit smooth corrector.** At zero temperature it solves

\[
\partial_rW+u(x)\partial_xW+u(y)\partial_yW-sw_uW=sw_{v^r},\quad W^t=0,
\]

and asserts, for gradient flow,

\[
\langle\phi,\rho_N^t\rangle
=\langle U^{0,t}\phi,\rho_N^0\rangle+F_N^{W^0}(X^0,\mu^0)
-\int_0^tD_N^{W^r}\,dr+\int_0^tR_N^{W^r}\,dr+\mathrm{mart.}
\tag{source 11}
\]

The formal endpoint sign is consistent with (1) and \(W^t=0\) in the Euclidean homogeneous calculation. It remains conditional on making those identities meaningful. The forcing \(w_v\) need not have one sign, so \(W\) need not be nonnegative; a nonnegative-weight dissipation bound is not automatically available. Moreover, \(\mathcal A\) has not extracted the full quadratic background response contained in \(\mathcal T_N\). This is an exact-rewriting proposal, not a completed pair inversion or remainder estimate. At \(\beta=\infty\) the displayed Brownian martingale is zero.

**Consequence (b), source label: the self-energy floor cancels between endpoints.** For terminal nonnegative weight \(w_0\), the homogeneous transport equation is claimed to preserve positivity and match the transported integral of \(w\mu^{1+s}\). It then asserts

\[
\int_0^tD_N^{w^r}\,dr
=F_N^{w^0}(X^0,\mu^0)-F_N^{w_0}(X^t,\mu^t)
+\int_0^tR_N^{w^r}\,dr.
\tag{source 12}
\]

The characteristic weight/Jacobian calculation is valid for a one-dimensional smooth transport flow when diffusion is zero and the Euclidean homogeneity formula applies. With terminal \(w_0\ge0\), the conclusion is nonnegativity, not strict positivity unless the terminal weight is strictly positive. The source shifts between a two-variable terminal weight and its diagonal restriction; that convention needs to be stated.

Even granting the identity, matching lower bounds at both endpoints alone do not control their difference: initial upper/excess preparation and remainder estimates are required. The universal lower bound proposed in 6.1 fails. Thus (12) does not dissolve the floor for arbitrary data. At positive temperature the pushforward identity \(\mu^t=\Psi^t_\#\mu^0\) is also invalid for the drift flow alone.

### Order of work -- p. 7

The source proposes importing Facts 2.1, 2.2, 3.2 into [N] immediately, closing dilational/incompressible cases without further ingredients, then treating Hope 5.1 through 6.1--6.2, local equilibrium/isotropy in Regime P, Hope 5.4 starting at \(2s<d\) and small temperature parameter, and leaving shear/Coulomb issues open.

This is a proposed work order, not an exact reduction or a permission to import those statements. The phrase that no new input is required conflicts with the geometry, martingale, coercivity, and signed-residual gaps above. Incompressibility can remove compression while retaining shear. The note does not define Regime R quantitatively, nor does it supply a critical-coupling theorem or a proof that finitely many correctors suffice. The frozen campaign's finite smooth algebra is an appropriate independent starting point, with singular and law-class claims kept open.

## Intake gate and remaining lines

The source-extraction part of Phase 0 is complete in this file. The frozen positive-power Fourier normalization has passed this lane's primary-source and direct calculation check. It is not a singular theorem or independent campaign certification.

The first usable mathematical route remains the fixed-smooth-kernel identity (1), with \(\mathcal T_N\) expanded to expose the full pair operator, upward terms, contractions, and martingale brackets, followed by independent coefficient comparison. The source's labels cannot substitute for that comparison.

Before any source-derived singular/dynamical promotion, at least the following lines remain:

1. Establish the regularized-to-singular passage, including background integrals, diagonal distributions, and martingale brackets.
2. Replace the unrestricted weighted lower bound and false generic singularity improvement by valid structural hypotheses and estimates.
3. Prove the actual law's time-integrated centered residual bound; mean commutator or mean stress estimates are insufficient.
4. Freeze law-dependent deterministic centering and the initial preparation error, with the required fluctuation-scale accuracy.
5. Specify and verify every static input and a quantitative static-to-dynamic bridge before using it.
6. Reformulate the Gibbs tilt comparison and partition normalization for the zero-mean periodic kernel.

No private-source request is required to finish Round 001's smooth algebra. [N] would be useful to audit I1--I5 and the claimed original theorem range; its indispensability for a later theorem must be decided at that theorem's exact source-use gate.

## Verification and files

- `python3 scripts/verify_campaign.py`: passed; imported source digest matched.
- `git rev-parse HEAD`: baseline hash above.
- `git status --short` before work: only the two supplied untracked task/dossier files; no source edits.
- PDF inspection: seven pages confirmed by `pypdf`; no embedded attachments; all seven rendered pages inspected.
- Rendering: `pdftoppm -scale-to 1600 -png INPUTS/note_v2.pdf BUILD/note_page`.
- External normalization source: retrieved exact version `https://arxiv.org/pdf/1509.08529v1`; printed pp. 3--4 inspected visually; digest recorded above. A failed fetch from an author's alternate host was superseded by this successful primary arXiv retrieval.
- Primary source renders: `pdftoppm -f 3 -l 4 -scale-to 1500 -png BUILD/1509.08529v1.pdf BUILD/riesz_normalization`.
- Durable output created by this lane: `SOURCES/ROUND_001_SOURCE_AUDIT.md` only. `BUILD/` contains ignored reading/rendering intermediates.
- `INPUTS/`, `BASELINE/`, canonical `STATE/`, and other worker outputs were not changed. No commits, merges, pushes, or dependency installations were performed.

The coordinator owns ledger integration and any subsequent promotion or independently audited counterexample status. This source report is an intake and a set of explicit self-checked repairs, not a declaration that the campaign mission is resolved.
