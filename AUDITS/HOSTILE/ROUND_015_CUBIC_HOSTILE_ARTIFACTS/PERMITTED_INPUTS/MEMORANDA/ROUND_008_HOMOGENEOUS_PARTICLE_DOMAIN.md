# Round 008 — homogeneous corrector in the finite-particle Itô domain

TASK051. Construction with the disclosed, unproved root seed. **PROVED_CANDIDATE / SELF_CHECKED; independent reconstruction and hostile audit are pending.** This is not a blind or independent audit. The proof below establishes the bounded assertion in THM028, using the supplied established pair-process/inverse and finite-N particle modules. It imports no differentiated-semigroup, higher-moment, or regularity lemma from THM027. The weighted barriers, common-completeness argument, differentiated expectations, second variations, response regularity, and time derivative are proved here.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r008-homogeneous-domain-20260918`. Branch: `codex/hocf-r008-homogeneous-domain`. Base: published R5 `32d17afba1ddb3c4198fb9a45e912907629618ce`. The eighteen files in the assigned manifest were copied and SHA-256 checked before work. Only that permitted dossier was used. The prior worktree and its seals remain untouched. No root files, canonical ledgers or IDs, commits, pushes, dependencies, or child agents were used.

## 1. Assertion, negation, and exact inputs

Fix the THM028 data: integer `d>=3`, `0<s<=d-2`, finite `N>=2`, finite T, `0<=nu<=nu_*<infinity`, unit Haar torus, frozen coefficient-one positive Fourier Riesz potential, `K=-grad g`, external drift zero, reference density one, and smooth real terminal test h. Let f be the actual homogeneous Fourier backward test in THM025. Write

\[
 E=\{(x,y):x\ne y\},\quad z=x-y,\quad
 F(x,y)=N^{-1}(K(z),-K(z)),\quad
 G=\nu\Delta_{x,y}+F\cdot\nabla_{x,y}=\nu\Delta_{x,y}+B/N,
\]

\[
 Bv=K(x-y)\cdot(\nabla_x-\nabla_y)v,
 \qquad J_t=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)).
\]

The full response is **both** homogeneous compensated slots,

\[
 Rv=R_xv+R_yv,qquad
 R_xv(x,y)=-\int v(x+w,y)D(dw),quad D=\operatorname{div}K.
 \tag{1.1}
\]

The exact assertion and its logical negation are those in THM028: the specified inverse either has every stated regularity/domain/integrability property and exact finite-N identity for every admissible tuple, or some admissible tuple violates at least one. This report does not weaken the quantifiers to positive noise or sub-Coulomb exponents. Constants may depend on N and all displayed fixed data and weights, but are uniform in the selected `nu in [0,nu_*]`. Independence of the initial N-body random variable below means independence from the driving Brownian motions; no factorization of its density is needed. In particular the claimed independent-particle preparations are included.

Imported inputs and exact scope:

- The R4 response proof, Section 2, gives `g(z)=|z|^-s+q(z)` with q smooth and even in an embedded ball. Its Section 3 gives `K in L1`, the finite measure D, and a lower divergence bound `D>=-kappa dx`. Below Coulomb D has a density locally of order `|z|^-s-2`; at Coulomb it is exactly `c_d(delta_0-dx)`.
- The R5 base proof supplies the off-diagonal pair process, deterministic Markov property, per-start noncollision, and bounded absolute potential of the actual J for fixed N, uniformly over bounded diffusivity. Its pointwise Borel inverse and the R5 response composition identify the already constructed bounded inverse Phi. The source/constant and exchange-symmetry clarifications are retained. None of their source-convergence exclusions is changed.
- The explicit R5 Fourier formula gives, for every fixed spatial order and every fixed time-derivative order, uniform derivative bounds for f on the bounded diffusivity interval. Indeed its coefficient is `exp[-a_k(T-t)]`, where `a_k=4 pi^2 nu |k|^2+4 pi^2 c_(d,s)|k|^(s+2-d)`, so every differentiated Fourier series is dominated by a fixed polynomial times the rapidly decreasing coefficients of h.
- THM026 and its full R6 construction supply the actual N-particle paths, their positive finite-horizon minimum separation almost surely, local smooth Itô calculus, and

\[
 \|F_t\|_\infty\le D_T:=\|F_0\|_\infty e^{(N-1)\kappa T}
 \quad(0\le t\le T)
 \tag{1.2}
\]

for a bounded initial N-body density independent of the Brownian motions. This uses `b=0`. No iid law is inferred at positive time.
- R1 equations (1.3), (1.4), and (3.2)–(3.7) fix the ordered-label algebra. Section 10 below reconstructs it directly, without evaluating a singular kernel or its derivatives on a particle diagonal.

THM027 is read only as an unproved first-gradient target, not an input lemma. No external theorem or literature claim is imported. The elementary local Sobolev estimate needed below is derived explicitly.

## 2. A global weighted Feynman–Kac barrier with constants

Fix embedded radii `0<R_0<R_1<1/3`. In this chart

\[
 K(z)=s r^{-s-2}z+k(z),\quad r=|z|,\quad k(0)=0,
 \quad |k(z)|\le L_k r,
\]

with k smooth and odd. Choose a fixed nonnegative smooth cutoff chi equal to one on `r<=R_0`, zero on `r>=R_1`. Write `p=s+2` and `a=2s/N`. For each positive alpha choose a positive smooth weight `w_alpha` on E, depending on z, equal to `r^-alpha` on `r<=R_0`, bounded above and below by positive constants outside that ball. We may and do choose it at least one. Other weights in the theorem are equivalent to these, with fixed comparison constants.

Put

\[
 c(z)=a\chi(z)r^{-p}.
\]

The cutoff product is defined in its chart and zero outside. For the principal pair Jacobian, the center modes have eigenvalue zero; in relative modes the transverse eigenvalue is `a r^-p`, while the radial eigenvalue is `-(s+1)a r^-p`. Consequently

\[
 \lambda_{\max}\big(\operatorname{Sym}DF\big)\le c+L,
 \qquad |D^2F|\le C_F w_{s+3},
 \tag{2.1}
\]

where explicit sufficient choices are

\[
 L=\frac2N\max\!\left\{L_k,
  \sup_{\operatorname{dist}(z,0)\ge R_0}\|DK(z)\|\right\},
 \qquad C_F=\sup_E |D^2F|/w_{s+3}<\infty.
\]

The norm on the pair space is the Euclidean product norm, so the singular relative Jacobian really is `2DK/N`. Replacing its largest symmetric eigenvalue by the absolute Hessian norm would multiply the singular expansion coefficient by `s+1` and lose the required thresholds.

Let `m>=0` and `alpha>m`. On `r<R_0`, direct differentiation gives

\[
 (G+mc)w_\alpha
 =-a(\alpha-m)r^{-\alpha-p}
  +2\nu\alpha(\alpha+2-d)r^{-\alpha-2}
  -\frac{2\alpha}{N}r^{-\alpha-2}k(z)\cdot z.
 \tag{2.2}
\]

Set

\[
 A=a(\alpha-m)>0,\quad D_\alpha=2\nu_*\alpha(\alpha+2-d)_+,
 \quad b_{\alpha,m}=A/2.
\]

For `D_alpha>0`, the exact elementary maximization over `u>=0` is

\[
 D_\alpha u^2-\frac A2u^{s+2}
 \le Y_{\alpha,m}:=
 \frac{sD_\alpha}{s+2}
 \left(\frac{4D_\alpha}{A(s+2)}\right)^{2/s}.
 \tag{2.3}
\]

For `D_alpha=0` set Y to zero. The maximizing point in the positive case satisfies `u^s=4D_alpha/[A(s+2)]`. Thus inside the inner ball,

\[
 (G+mc)w_\alpha+b_{\alpha,m}r^{-\alpha-p}
 \le (2\alpha L_k/N+Y_{\alpha,m})w_\alpha.
\]

To include **all** cutoff terms, define the finite annular constant

\[
 C_{\rm ann}=\sup_{r\ge R_0}
 \frac{\nu_*|\Delta_{x,y}w_\alpha|
       +|F|\,|\nabla_{x,y}w_\alpha|
       +mcw_\alpha+b_{\alpha,m}\chi r^{-\alpha-p}}
      {w_\alpha},
\]

where chart-supported products are zero outside their chart. Finally take

\[
 C_{\alpha,m}=\max\{2\alpha L_k/N+Y_{\alpha,m},C_{\rm ann},0\}.
\]

This yields the global inequality, uniform in the bounded noise interval,

\[
 (G+mc)w_\alpha+b_{\alpha,m}\chi r^{-\alpha-p}
 \le C_{\alpha,m}w_\alpha.
 \tag{2.4}
\]

All dependence on N, alpha, m, cutoffs and `nu_*` is explicit. Large moments are allowed; their constants need not be small or N-uniform.

For the supplied pair process `Z_t`, let `I_t=int_0^t c(Z_r)dr`. First stop on a compact collision-excluded domain. Smooth Itô applied to
`exp(m I_t-C_(alpha,m)t)w_alpha(Z_t)` and (2.4) gives

\[
 \begin{split}
 \mathbb E_z[e^{mI_\tau-C_{\alpha,m}\tau}w_\alpha(Z_\tau)]
 &+b_{\alpha,m}\mathbb E_z\int_0^\tau
 e^{mI_r-C_{\alpha,m}r}\chi r(Z_r)^{-\alpha-p}\,dr
 \le w_\alpha(z)
 \end{split}
 \tag{2.5}
\]

for a bounded stopped time tau. On each stopped domain the stochastic integrand is bounded, so this is an expectation identity/inequality of true stopped martingales. The already supplied per-start noncollision permits passage to a fixed horizon by Fatou and monotone convergence for the nonnegative occupation term. In particular

\[
 \mathbb E_z[e^{mI_t}w_\alpha(Z_t)]\le e^{C_{\alpha,m}T}w_\alpha(z),
\]

\[
 \mathbb E_z\int_0^T e^{mI_r}\chi r(Z_r)^{-\alpha-p}\,dr
 \le b_{\alpha,m}^{-1}e^{C_{\alpha,m}T}w_\alpha(z).
 \tag{2.6}
\]

The weight `w_beta` is bounded by a fixed multiple of `w_alpha+chi r^-alpha-p` whenever `0<=beta<=alpha+p`. Equations (2.6) therefore also give

\[
 \mathbb E_z\int_0^T e^{mI_r}w_\beta(Z_r)\,dr
 \le C(\alpha,m,\beta,T)w_\alpha(z),\qquad
 \alpha>m,quad\beta\le\alpha+p.
 \tag{2.7}
\]

A definite sufficient coefficient in (2.7) is

\[
 O_{\alpha,m,\beta}=K_{\alpha,\beta}e^{C_{\alpha,m}T}
       (T+b_{\alpha,m}^{-1}),\qquad
 K_{\alpha,\beta}=\sup_E
 \frac{w_\beta}{w_\alpha+\chi r^{-\alpha-p}}<\infty.
 \tag{2.8}
\]

Only deterministic-time Markov conditioning will be needed later.

## 3. Higher moments and common completeness: the exceptional-start issue

It is not sufficient that each fixed starting point has its own full-probability noncollision event. Nor does almost-sure pathwise differentiability alone permit differentiation of an expectation. We supply the additional argument.

### 3.1 Arbitrarily high compact-start moments

The nonnegative local supermartingale in (2.5), without its nonnegative accumulated occupation, is a supermartingale after passing bounded localizations by conditional Fatou. Its elementary maximal estimate is

\[
 \mathbb P_z\left\{\sup_{t\le T}
 e^{mI_t-C_{\alpha,m}t}w_\alpha(Z_t)>u\right\}
 \le \min(1,w_\alpha(z)/u).
 \tag{3.1}
\]

Indeed stop at its first crossing of u, apply the stopped expectation bound, and pass the compact stops. Integrating this tail gives, for `0<theta<1`, a bound `w_alpha(z)^theta/(1-theta)` for the theta moment of this supremum.

Fix arbitrary finite `b,l,Q>=0`, with `Q>0`. Choose `R>Q`, `m=lR`, and `alpha>max(m,bR)`. Since `w_b^R<=C w_alpha`, (3.1) implies

\[
 \mathbb E_z\!\left[\left(\sup_{t\le T} e^{lI_t}w_b(Z_t)\right)^Q\right]<\infty,
 \tag{3.2}
\]

uniformly for z in any fixed compact subset of E and uniformly in nu. This follows with `theta=Q/R`; all constants are provided by (2.3)–(2.4) and the weight-comparison bound. The exponent Q need not be integral.

Before invoking common completeness, the maximal additive-noise equation already has a jointly measurable local flow. To see this directly, smoothly truncate F outside successive collision-excluded compact sets. For each continuous noise path, subtract the noise and solve the ordinary integral equation by Picard iteration. It is smooth in its initial state on its maximal domain; different truncations agree until exit. This is the same local construction used in the supplied pair module. Along a path existing to T, initial-state variations satisfy

\[
 \dot A_t=DF(Z_t)A_t,\quad A_0=I,\qquad
 |A_t|\le e^{Lt+I_t},
 \tag{3.3}
\]

because differentiating `|A_t v|^2` uses the largest symmetric eigenvalue in (2.1). No derivative of a Brownian path is taken. These statements hold on a random neighborhood of each initial state whose given path stays separated: a fixed compact truncation agreeing along that path also agrees for sufficiently nearby initial states. They do not yet assert a common global flow.

### 3.2 Closing the common exceptional set

Fix a driving continuous path omega, a bounded initial-state coordinate ball O whose closure lies in E, and a compact inner ball H. Let `D_T(omega)` be the open set of initial states whose maximal paths exist through T. Define on this set

\[
 V(z,\omega)=\sup_{t\le T}w_1(Z_t^z(\omega)),
\]

and put V equal to infinity outside it. The extended function V tends to infinity when a good starting point approaches a bad one. Otherwise a sequence of nearby good paths would have a common positive minimum separation. A smooth truncation below that separation has continuous dependence on the initial state and agrees along all those paths; its limiting path also remains separated and would make the alleged bad state good, a contradiction.

For each integer n, set `V_n=min(V,n)`, taking the value n at bad points. This is locally Lipschitz throughout O. On the good open set this follows by differentiating its compact path supremum; near every bad point the preceding blow-up argument makes `V_n` locally constant. Almost everywhere on the good set,

\[
 |\nabla V_n|\le\sup_{t\le T}|\nabla w_1(Z_t)|\,|A_t|
 \le C_T\sup_{t\le T}e^{I_t}w_2(Z_t).
 \tag{3.4}
\]

Each deterministic starting point is good with probability one by the supplied per-start result. Fubini consequently makes the bad set Lebesgue null almost surely in O. Equation (3.2), with arbitrarily large Q, now gives

\[
 \sup_n\mathbb E\|V_n\|_{W^{1,Q}(O)}^Q<\infty.
 \tag{3.5}
\]

Choose `Q>2d`, the dimension of the initial pair space. The elementary local Sobolev bound

\[
 \sup_H|v|\le C_{O,H,Q}(\|v\|_{L^Q(O)}+\|\nabla v\|_{L^Q(O)})
 \tag{3.6}
\]

applies to each locally Lipschitz `V_n`. Here is a direct justification, to specify the theorem being used. For a ball of radius R contained in O and centered at z in H, average the fundamental theorem of calculus over radial segments. In ambient dimension M this bounds the difference from the ball average by
`|S^(M-1)|^-1 int_(B_R(z)) |grad v(y)| |y-z|^(1-M)dy`. Hölder gives a finite coefficient because the conjugate exponent satisfies `(M-1)Q'<M`, exactly `Q>M`; the average is bounded by `|B_R|^-1/Q ||v||_Q`. A fixed radius below the distance of H to the complement of O gives (3.6), with explicit finite radial integral `|S^(M-1)| R^(M-(M-1)Q')/[M-(M-1)Q']` in its gradient coefficient.

Equations (3.5)–(3.6), followed by monotone convergence, give `sup_H V<infinity` almost surely. Any bad point in H would instead make `sup_H V_n=n` for every n. Thus there are no bad points in H on a single full-probability event. Exhaust E by countably many such inner balls (and finite integer horizons if desired). For each fixed parameter tuple, the pair flow exists simultaneously for all off-diagonal initial states, is smooth in its initial state locally, and has a positive minimum separation uniformly on each compact initial set and finite time horizon, almost surely.

This strengthens the per-start module only for the present homogeneous smooth off-diagonal drift, using the newly proved high-moment estimates. It is not imported from THM026 and does not assert a common exceptional set over uncountably many noise coefficients. All moment constants remain uniform in the prescribed bounded interval of noise coefficients.

### 3.3 Second variations and legitimate differentiation of expectations

The second initial variation H satisfies the ordinary equation

\[
 H_t=\int_0^t A_{t,r}\,D^2F(Z_r)[A_r,A_r],dr,
 \qquad |A_{t,r}|\le e^{L(t-r)+I_t-I_r}.
 \tag{3.7}
\]

In particular

\[
 \sup_{t\le T}|H_t|
 \le C_T e^{2I_T}\sup_{r\le T}w_{s+3}(Z_r)
\le C_T\left[\sup_{r\le T}e^{2I_r}w_{s+3}(Z_r)\right]^2.
 \tag{3.8}
\]

The constant includes T and `C_F`. Equations (3.2), (3.3), and (3.8) give all finite moments of the first and second variations, with any additional fixed inverse-distance power, uniformly for deterministic initial states in a compact subset of E.

For a continuous local C2 terminal function v whose first two derivatives have finite power growth, the common flow makes the first and second chain rules valid on every deterministic small segment of initial states. Their random derivatives have a moment strictly above one, uniformly along that segment, by the preceding bounds. Fubini applies to the segment fundamental theorem of calculus. For a convergent sequence of initial states, local pathwise smooth dependence gives pointwise convergence of those derivative expressions; the same moment bound gives uniform integrability. Thus their expectations are continuous, and differentiating the averaged fundamental theorem gives

\[
 \nabla S_t v=\mathbb E[\nabla v(Z_t)A_t],
\quad
 D^2S_t v=\mathbb E[D^2v(Z_t)[A_t,A_t]+\nabla v(Z_t)H_t].
 \tag{3.9}
\]

The identical argument with an extra time integral applies to source potentials whose derivatives have finite power growth. This proves expectation differentiation rather than merely formal variational identities. Time and initial-state continuity of the displayed derivatives follow by the same sequence/UI argument, including t=0, because the common local flow and its variations are continuous in time. No simultaneous-null-set assumption is left hidden in the segment argument.

## 4. Precise first- and second-derivative weights

Fix the theorem's exponents

\[
 1<q_1<d/2,\qquad q_1+1<q_2<d.
 \tag{4.1}
\]

In particular `q_2>2`. Let X be the space of bounded local C2 functions on E, with norm

\[
 \|v\|_X=\|v\|_\infty+
 \sup_E|\nabla v|/w_{q_1}+\sup_E|D^2v|/w_{q_2}.
\]

Joint time continuity below is always local in space; no strong continuity in this weighted sup norm is assumed.

For the first term in (3.9), (2.6) with `(alpha,m)=(q_1,1)` gives

\[
 |\nabla S_tv(z)|\le C_T\|v\|_X w_{q_1}(z).
\]

For the terminal Hessian term, use `(alpha,m)=(q_2,2)` to get `C_T ||v||_X w_q2(z)`.

For the second-variation term, insert (3.7) and condition at the deterministic intermediate time r. The future flow has the same Markov law and its Jacobian norm is bounded by the future exponential. Equation (2.6) with `(q_1,1)` therefore bounds

\[
 \mathbb E[|\nabla v(Z_t)|\,|A_{t,r}|\mid\mathcal F_r]
 \le C_T\|v\|_Xw_{q_1}(Z_r).
\]

Consequently this entire term is at most

\[
 C_T\|v\|_X\mathbb E_z\int_0^t
 e^{2I_r}|D^2F(Z_r)|w_{q_1}(Z_r)\,dr.
\]

The integrand's spatial weight is of order `w_(s+3+q1)`. Since

\[
 s+3+q_1<q_2+s+2=q_2+p,
\]

(2.7) with `(alpha,m)=(q_2,2)` bounds it by `C_T ||v||_X w_q2(z)`. Thus

\[
 \sup_{0\le t\le T}\|S_t v\|_X\le C_S\|v\|_X.
 \tag{4.2}
\]

For an explicit sufficient operator coefficient, put

\[
 E_1=e^{C_{q_1,1}T},\quad E_2=e^{C_{q_2,2}T},\quad
 \beta=s+3+q_1,\quad
 M_w=\sup_E w_{s+3}w_{q_1}/w_\beta<\infty.
\]

Then one may take

\[
 C_S=1+e^{LT}E_1+e^{2LT}E_2
       +C_FM_we^{3LT}E_1O_{q_2,2,\beta}.
 \tag{4.2a}
\]

This is an operator estimate proved for X, not a statement borrowed from the first-gradient card.

The actual source satisfies, uniformly in t and nu,

\[
 |D^jJ_t|\le C_J w_{s+j}\quad(j=0,1,2),
 \qquad |\partial_t^lJ_t|\le C_{J,l}w_s\quad(l=1,2).
 \tag{4.3}
\]

For example the difference of the two gradients in J supplies one factor of r; each pair differentiation loses at most one such power. Smoothness of the remainder and the Fourier bounds for f give the stated constants.

The base potential is `U(t)=int_0^(T-t) S_a J_(t+a) da`. Its fixed-N sup bound is imported from the already established absolute source potential. Differentiating its expectation is legitimate by Section 3 and (4.3). For its gradient use (2.7) with `(q_1,1)` and source exponent `s+1`. For its terminal-Hessian term use `(q_2,2)` and source exponent `s+2`. For the integrated second-variation term, first condition at r and integrate future a. Its inner future integral is bounded by `C w_q1(Z_r)` by the same first-gradient occupation estimate; the resulting earlier integral is precisely the one just bounded using `s+3+q_1<q_2+p`. Tonelli applies to these nonnegative majorants. Therefore

\[
 \sup_{0\le t\le T}\|U(t)\|_X\le C_U<\infty.
 \tag{4.4}
\]

Writing `J_j=sup_(t,nu,z) |D^jJ_t(z)|/w_(s+j)(z)` for j=1,2 and B_N for the supplied uniform absolute-source-potential supremum, one sufficient choice is

\[
 \begin{split}
 C_U={}&B_N+e^{LT}J_1O_{q_1,1,s+1}
       +e^{2LT}J_2O_{q_2,2,s+2}\\
      &+C_FM_we^{3LT}J_1O_{q_1,1,s+1}O_{q_2,2,\beta}.
 \end{split}
 \tag{4.4a}
\]

All its coefficients are finite by the displayed Fourier/local estimates and (2.8). The constants are uniform in nu, and the first two spatial derivatives are jointly continuous on `[0,T] x E`. This includes terminal time, where the time intervals shrink to zero and the compact-start dominating moments in Section 3 justify convergence. Neither heat convergence of terminal tests nor heat convergence of singular source potentials has been used.

## 5. Both responses preserve the weighted derivative space

First, every v in X has its displayed derivatives as global weak derivatives. Delete the tube `r<=epsilon` in an integration by parts against a smooth pair test. The first boundary term is at most `C ||v||_infinity epsilon^(d-1)`, hence vanishes. For the second derivative the boundary term is at most `C ||v||_X epsilon^(d-1-q1)`, which also vanishes because `q_1<d-1`. The volume integrals converge absolutely because `q_1,q_2<d`. Thus

\[
 v\in W^{2,1},\qquad v\in H^1
\]

with bounds by `C||v||_X`; the last assertion uses `2q_1<d`. No value on the pair diagonal is involved.

We need the following elementary convolution bound. If `0<a,q<d`, then on the torus, with fixed smooth positive power weights,

\[
 \int w_a(w)w_q(w+z)\,dw\le C_{a,q}w_q(z),\qquad z\ne0.
 \tag{5.1}
\]

For small `r=|z|`, split into `|w|<r/2`, `|w+z|<r/2`, and their complement. The first contribution is at most `C r^-q r^(d-a)`. The second is at most `C r^-a r^(d-q)`. Each is at most `C r^-q` since `a<d` and the chart radius is fixed. On the complement `w_q(w+z)<=C r^-q`, and `w_a` is integrable. Smooth outside-chart terms are bounded in the same way. This proof does not require `a+q<d`.

Below Coulomb, `|D|(dw)<=C w_(s+2)(w)dw` with `s+2<d`. At Coulomb `D=c_d(delta_0-dw)`. Constant-coefficient convolution commutes with global weak derivatives, so the two derivatives of (1.1) are the same finite-measure convolutions of the corresponding weak derivatives of v. Fubini is valid since these derivatives are L1 and D is finite. Formula (5.1) gives their pointwise weighted bounds; the atom simply multiplies the existing derivatives at `(x,y)`. The original bounded-input response bound gives its sup norm. Hence

\[
 \|Rv\|_X\le C_R^X\|v\|_X.
 \tag{5.2}
\]

Explicitly, define

\[
 R_q=\sup_{z\ne0}\frac{\int w_q(z+w)|D|(dw)}{w_q(z)}<\infty.
\]

A sufficient coefficient in (5.2) is
`C_R^X=2 max(||D||_TV,R_q1,R_q2)`; the factor two retains both slots. The corresponding weighted-function coefficient later is `C_R^Y=2R_s`.

The resulting weak derivatives are locally continuous on E. To verify this near a given off-diagonal pair, the possible displacement singularities at `w=0` and `w=y-x` are separated. Near the first, the translated input derivative is uniformly continuous and bounded, with an integrable D majorant. Near the second, change to the relative variable `v=x+w-y`; the D density is smooth and bounded there and `w_q(v)` is integrable. The complement has an ordinary bounded continuous integrand. Shrinking those two neighborhoods and then using dominated convergence proves continuity, including simultaneous variation of x and y. The atom is already a locally continuous term. The same argument handles joint time continuity for uniformly X-bounded families with locally continuous derivatives. Thus these weak derivatives are the classical local derivatives of Rv.

For later algebra, the response also has its original integrated-gradient representation at every off-diagonal state:

\[
 R_xv(x,y)=\int K(z-x)\cdot\nabla_1v(z,y)\,dz.
 \tag{5.3}
\]

The two singular points `z=x` and `z=y` are distinct. Near the first, v is smooth and the finite-measure integration by parts retains the Coulomb atom. Near the second, K is smooth, v is bounded, and the deleted-sphere boundary tends to zero; its gradient is integrable because `q_1<d`. A partition separating those points justifies both absolute integration and integration by parts. The second-slot formula follows in the same manner. This argument does not apply on `x=y`, and no such application is required.

## 6. Spatial construction of the actual full inverse

On time-dependent kernels set

\[
 (\mathcal Vv)(t)=\int_t^T S_{a-t}Rv(a)\,da.
\]

Start with U from (4.4). Sections 3–5 justify each pointwise time integral and its first two local spatial derivatives. If the input derivatives are jointly locally continuous, so are the output derivatives, by the compact-start uniform-integrability argument. Iterating (4.2) and (5.2) over ordered simplices gives

\[
 \|(\mathcal V^mU)(t)\|_X
 \le C_U(C_SC_R^X)^m\frac{(T-t)^m}{m!}.
 \tag{6.1}
\]

Thus the series converges in the weighted norms and locally uniformly with its first two derivatives. It is jointly locally C2 in space, is bounded, and solves the exact full Volterra equation. Its Borel sup-norm series is the already known series, since all pointwise operator actions agree. Bounded Borel uniqueness from the supplied module identifies its sum with the **given** Phi in THM028, rather than a new auxiliary kernel. We have proved

\[
 \sup_t\left(\|\Phi_t\|_\infty+
 \sup_E\frac{|\nabla\Phi_t|}{w_{q_1}}+
 \sup_E\frac{|D^2\Phi_t|}{w_{q_2}}\right)
 \le C_Ue^{C_SC_R^XT}.
 \tag{6.2}
\]

The common first/second derivative representative belongs globally to H1 and W2,1 by Section 5. Both responses remain present throughout; their preservation of pair exchange makes Phi symmetric. No strong continuity of `S_t` on X was needed.

## 7. A separate weighted evolution gives the time derivative

Let Y be the actual Borel weighted-sup space `||v||_Y=sup_E |v|/w_s`. Here `G w_s<=C_s w_s`: inside the local ball the diffusion term is `2nu s(s+2-d)r^-s-2<=0`, the principal drift term is negative, and the smooth remainder is bounded by a multiple of w_s; outside it all cutoff terms are bounded. Equivalently (2.4) with `(alpha,m)=(s,0)` gives this estimate directly. Stopped Itô, Fatou and per-start noncollision give

\[
 \|S_t\|_{Y\to Y}\le e^{C_st}.
 \tag{7.1}
\]

Equation (5.1), now with q=s, proves `||R||_(Y->Y)<=C_R^Y`, including the Coulomb atom. This action is well-defined pointwise off diagonal: the two possible singularities are separated there. It respects diagonal representatives in precisely the same way as the bounded action.

Define a full homogeneous evolution by a Dyson series:

\[
 T_t=S_t+\sum_{m\ge1}
 \int_{0<a_1<\cdots<a_m<t}
 S_{a_1}R S_{a_2-a_1}R\cdots R S_{t-a_m}\,da_1\cdots da_m.
 \tag{7.2}
\]

Every integral here is a pointwise measurable integral. Absolute majorants from (7.1) and the weighted R bound give norm at most
`e^(C_s t)(C_R^Y t)^m/m!`. Thus it defines a bounded operator on Y with norm at most `exp[(C_s+C_R^Y)t]`. The semigroup composition follows by multiplying the absolutely convergent series and partitioning the ordered time simplex at the intermediate time; Fubini is justified by the same positive majorants. This argument makes no assertion of strong continuity on the full weighted Borel space.

For a function locally continuous on E and bounded by a multiple of w_s, `S_t v(z)` is jointly continuous in `(t,z)`, including t=0. Common local path continuity gives pointwise convergence; Section 3 supplies a moment above one for the relevant power of the inverse separation uniformly over compact sets of initial states and the time interval. Hence those evaluations are uniformly integrable. The same separated-singularity argument as in Section 5 proves local continuity for Rv. The Dyson terms and their locally uniform majorants therefore give this joint continuity for `T_t v`, as well as for locally continuous time-dependent input families with the same growth bound. These are continuity statements for the particular inputs, not generator assertions on Y.

The function

\[
 \Psi_t=\int_0^{T-t}T_rJ_{t+r}\,dr
 \tag{7.3}
\]

is well-defined in the pointwise Y class. Expanding the series and rearranging absolutely convergent time integrals shows that it solves the original Volterra equation with U. Uniqueness among uniformly Y-bounded solutions follows by the same factorial iteration as for bounded functions. The already bounded Phi is uniformly Y-bounded and solves that equation, so `Psi=Phi` pointwise.

The family J is twice continuously differentiable in time as a Y-valued family: (4.3) and the uniform Fourier bounds even give a uniform Y bound on its second time derivative. Difference quotients in the integrand of (7.3) are therefore dominated in Y and converge there. Moving the upper endpoint uses the locally continuous value `T_(T-t)J_T`. Direct differentiation of this integral, with **no derivative of the semigroup in its weighted norm**, gives

\[
 \boxed{
 \partial_t\Phi_t=-T_{T-t}J_T+
       \int_0^{T-t}T_r\partial_tJ_{t+r}\,dr.}
 \tag{7.4}
\]

The derivative is jointly continuous locally on `[0,T] x E`, one-sided at the endpoints, by the continuity just proved and domination by the uniform weighted majorants. At T the formula reads `partial_t Phi_T=-J_T`. Moreover

\[
 \sup_t|\partial_t\Phi_t(z)|\le
 e^{(C_s+C_R^Y)T}
 (\sup_t\|J_t\|_Y+T\sup_t\|\partial_tJ_t\|_Y)w_s(z).
 \tag{7.5}
\]

This completes the asserted temporal regularity, uniformly in bounded diffusivity. An unproved generator derivative on a weighted sup space has not entered.

## 8. The classical pair equation and the integrable internal drift

Phi now has C1 time and local C2 space regularity with jointly continuous indicated derivatives. Apply ordinary smooth Itô to Phi along the auxiliary pair process stopped in a small compact subset of E. Compare it with its already established true-martingale inverse, whose integrated source is `J+R Phi`. Their difference has continuous finite-variation drift

\[
 H(t,z)=\partial_t\Phi_t+G\Phi_t+R\Phi_t+J_t.
\]

Taking expectation from an arbitrary deterministic `(t,z)` up to a sufficiently small stopped time, dividing by its time length and using local continuity gives `H(t,z)=0`. Thus, including endpoint one-sided derivatives,

\[
 \partial_t\Phi+\nu\Delta_{x,y}\Phi+B\Phi/N+R\Phi=-J
 \quad\hbox{classically on }[0,T]\times E.
 \tag{8.1}
\]

It follows **through this identity**, not an absolute force-gradient estimate, that

\[
 B\Phi=-N(J+\partial_t\Phi+\nu\Delta_{x,y}\Phi+R\Phi).
 \tag{8.2}
\]

The four terms on the right are bounded respectively by a multiple of `w_s`, `w_s`, `w_q2`, and 1. Since `s,q_2<d`, this proves a uniform-in-time Haar L1 bound for B Phi, also uniform in the chosen nu. It also proves uniform slice integrability in either variable. The crude product `|K| |grad Phi|` could have exponent `s+1+q_1>=d` and is not used to estimate this repeated-pair term.

Section 5 already proves global H1 and W2,1 membership. Equation (7.5) supplies global L1 time derivatives. No distributional value of the pair drift on the true diagonal or its trace is needed.

## 9. Differentiated background contractions and all partial diagonals

Define, with Haar background,

\[
 q_t(x)=\int\Phi_t(x,y)dy,\quad
 a_t(x)=\int\nabla_1\Phi_t(x,y)dy,\quad
 r_t=\int\Phi_t(x,y)dxdy.
\]

These integrals and the corresponding first, second, and time derivative integrals converge absolutely and uniformly in the remaining variable, by the respective weights `1,w_q1,w_q2,w_s`. Their contractions are continuous. To prove continuity with a moving singular point, split off a tube of radius delta around that point. Its derivative integral is uniformly at most `C delta^(d-q_j)` or `C delta^(d-s)`; outside a slightly larger tube the integrand is uniformly continuous on a compact set. Let the evaluation points converge first and then delta decrease to zero. This proves the claimed continuity without using a fixed-location majorant incorrectly.

Global weak differentiation from Section 5 and Fubini identify these continuous functions as the weak derivatives of q. A function whose weak derivatives through order two have these continuous representatives has the corresponding classical derivatives, as follows by convolution with a smooth approximate identity and integrating the convergent continuous derivatives along coordinate segments. Therefore q is C1 in time and C2 in x, `grad q=a`, and its derivatives are exactly the integrals just stated. Its second derivatives and time derivative are bounded. Slice integration by parts, with boundary `O(epsilon^(d-1-q1))`, gives

\[
 \int\Delta_y\Phi_t(x,y)dy=0
\]

for every x. Consequently mixed and scalar diffusion contractions in the direct Itô calculation below are legitimate and create no missing trace.

The same moving-tube argument and (8.2) give a continuous bounded contraction

\[
 b_t(x)=\int B\Phi_t(x,y)dy
\]

and an absolutely finite scalar integral. This conclusion relies on the structurally proved bound for B Phi.

Let `p(x,y)=grad_1 Phi(x,y)` and set

\[
 A(x,y,z)=K(x-z)\cdot p(x,y),\qquad C\Phi=\operatorname{Sym}_3 A,
 \tag{9.1}
\]

where the symmetrization is the average over six permutations. Conditioning on x in Haar integration gives

\[
 \int|A(x,y,z)|dxdydz
 \le \|K\|_1\sup_x\int|p(x,y)|dy<\infty.
 \tag{9.2}
\]

This is the needed simultaneous triple-collision bound: the two independent relative variables have exponents `s+1<d` and `q_1<d` separately. Their sum is not required to be below d. On the partial diagonal `x=y!=z`, the gradient singularity is integrable in y; on `x=z!=y`, the force singularity is integrable in z; on `y=z!=x`, neither factor is singular. All permutations obey the same argument.

For two fixed distinct empirical coordinates x,y, every one-background term in C has possible singularities at the two separate points z=x and z=y; each integral is absolutely finite by the same separated-singularity argument used for (5.3). One empirical coordinate and two background coordinates are covered directly by (9.2) slice by slice. Two coinciding empirical coordinates are never required. Actual coinciding background coordinates form null sets in their Lebesgue integrations. Thus no assignment of `p(x,x)`, `B Phi(x,x)`, or `C Phi(x,x,z)` is used.

Writing

\[
 A_a(x,y)=K(x-y)\cdot(a(x)-a(y)),\qquad
 v(x)=\int K(z-x)\cdot a(z)dz,
\]

the six terms of (9.1), integrated absolutely, give the precise contractions

\[
 C_1(x,y):=\int C\Phi(x,y,z)dz
   =\frac16[A_a(x,y)+R\Phi(x,y)],
 \tag{9.3}
\]

\[
 C_2(x):=\iint C\Phi(x,y,z)dydz=\frac13v(x),
 \qquad C_0:=\int C\Phi\,dxdydz=0.
 \tag{9.4}
\]

Here `int K=0`; the first-slot response integrates in y to v, while the second-slot response integrates in y to zero. In particular

\[
 (R\Phi)_\mu=v,\qquad \int R\Phi=0.
 \tag{9.5}
\]

The gradient a is Lipschitz because q has bounded second derivatives, so `A_a` itself has at most the integrable singularity `w_s`. Alternatively its two separate terms are already integrable since a is bounded and K is L1. These identities expose every partial contraction needed in U3 without a diagonal extension.

## 10. Exact finite-N identity from distinct labels

Suppress t temporarily. For the actual particle configuration with distinct coordinates, the statistic is exactly R1 (1.3):

\[
 P[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(x_i,x_j)
         -\frac1N\sum_iq(x_i)+\frac12r.
 \tag{10.1}
\]

For symmetric triple F, R1 (1.4) is

\[
 U_3[F]=\frac1{N^3}\sum_{i,j,k\ {\rm distinct}}F(x_i,x_j,x_k)
 -\frac3{N^2}\sum_{i\ne j}F_1(x_i,x_j)
 +\frac3N\sum_iF_2(x_i)-F_0.
 \tag{10.2}
\]

Each tuple is ordered; denominators are `N^k`, not falling factorials. For N=2 the first sum in (10.2) is empty, but the background terms generally are not.

First stop the actual paths on a compact collision-excluded configuration set. Sections 6–9 make (10.1) a C1-time, C2-space observable there, including its background terms. Ordinary Itô gives the independent time-diffusion part

\[
 P[(\partial_t+\nu\Delta_{x,y})\Phi]
\]

and the force part

\[
 Q=\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}
       K(x_i-x_k)\cdot p(x_i,x_j)
   -\frac1{N^2}\sum_{i\ne k}K(x_i-x_k)\cdot a(x_i).
 \tag{10.3}
\]

In the first sum separate `k=j` from the three-distinct terms. Pairing the two orientations of `k=j` gives

\[
 \frac1{N^3}\sum_{i\ne j}K(x_i-x_j)\cdot p(x_i,x_j)
 =\frac1{2N}D_2[B\Phi],\qquad
 D_2[F]=N^{-2}\sum_{i\ne j}F(x_i,x_j).
 \tag{10.4}
\]

This pairing is performed **before** estimating; its individual unsymmetrized terms need not be Haar integrable. The three-distinct sum equals the same ordered sum of C Phi. Oddness of K turns the second sum of (10.3) into `-(2N^2)^-1 sum_(i!=j) A_a(x_i,x_j)`. Insert (9.3)–(9.5) into (10.2). Direct cancellation yields

\[
 Q=U_3[C\Phi]+P[R\Phi]+\frac1{2N}D_2[B\Phi].
 \tag{10.5}
\]

For clarity, the cubic expansion contributes `-(2N^2)^-1 sum(A_a+R Phi)+(1/N)sum v`; moving its last two pieces to the other side is exactly `P[R Phi]`. This verifies both response slots and the upward coefficient one without any singular diagonal-overlap identity.

Combining (10.5) with the independent part reproduces R1 (3.6) on the collision-excluded domain. By the purely algebraic definition of P,

\[
 D_2[B\Phi]-2P[B\Phi]
 =2\rho[(B\Phi)_\mu]+\int B\Phi\,dxdy,
 \tag{10.6}
\]

where `rho=eta-dx`. This is well-defined by Section 8 and the background contractions in Section 9. Thus R1 (3.7), with `G_(2,N)=nu Delta_pair+R+B/N`, is reproduced. Using the actual classical inverse equation (8.1) gives exactly

\[
 \boxed{
 dP_t[\Phi_t]=\left\{
 -P_t[J_t]+U_{3,t}[C\Phi_t]
 +\frac1N\rho_t[(B\Phi_t)_\mu]
 +\frac1{2N}\int B\Phi_t\,dxdy
 \right\}dt+dM^2_t.}
 \tag{10.7}
\]

The gradient of (10.1), using symmetry, is

\[
 \nabla_iP[\Phi]=\frac1{N^2}\sum_{j\ne i}p(x_i,x_j)-\frac1N a(x_i).
 \tag{10.8}
\]

Hence its stopped noise and bracket are

\[
 dM^2_t=\sqrt{2\nu}\sum_i\nabla_iP_t[\Phi_t](X_t)\cdot dW_i(t),
 \qquad
 d\langle M^2\rangle_t=2\nu\sum_i|\nabla_iP_t[\Phi_t](X_t)|^2dt.
 \tag{10.9}
\]

There is no separate thermal trace in this deleted-label convention. In the particle-particle sum, the two labels are distinct, so their Brownian cross variation is zero. In the mixed terms, the integrated Haar background is stationary under the independent diffusion, and its integrated Laplacian vanishes by the weak/slice result in Section 9. This directly proves the absence of an extra trace without subtracting an undefined full-product diagonal. At zero nu the martingale and bracket vanish.

## 11. Absolute integrability and removal of the collision stops

All these claims are at fixed N. The density domination (1.2) implies, for every nonnegative Haar-integrable configuration function H,

\[
 \mathbb E\int_0^T H_t(X_t)dt
 \le D_T\int_0^T\|H_t\|_{L^1((\mathbb T^d)^N)}dt.
 \tag{11.1}
\]

Joint measurability and nonnegativity justify Tonelli. Since Haar mass is one, the same density bound applies after integrating out any unused particle coordinates.

The displayed drift in (10.7) is integrable term by term. For `P[J]`, use `|J|<=Cw_s` and its bounded slice integrals. For `U3[C Phi]`, use (9.2) for every all-distinct empirical triple and absolute Fubini for all mixed contractions. These arguments include every partial triple collision. For the lower and scalar contractions use the structural bound (8.2); their slice integrals are even uniformly bounded. Thus every term has finite expected absolute time integral, with the allowed dependence on N and `||F0||_infinity`.

For the bracket, (10.8), the finite-sum Cauchy–Schwarz inequality, and `2q_1<d` give

\[
 \sum_i\|\nabla_iP_t[\Phi_t]\|_{L^2((\mathbb T^d)^N)}^2<\infty
\]

uniformly in t and nu. One explicit sufficient bound, writing
`G_2=sup_t ||grad_1 Phi_t||_(L2(pair))` and
`A_2=sup_t ||a_t||_(L2(one-body))<=G_2`, is

\[
 \sum_i\|\nabla_iP_t\|_2^2
 \le\frac{2(N-1)^2}{N^3}G_2^2+\frac2N A_2^2.
 \tag{11.2}
\]

Multiplication by `2nu_* D_T T` bounds the expected full bracket. The stochastic integral in (10.9) is therefore a square-integrable true martingale, not merely a local one.

Let tau_epsilon be the first actual particle time with any separation at most epsilon, truncated by a fixed finite horizon when defining stopped integrals. The supplied finite-N noncollision and path continuity imply a strictly positive realized minimum separation on `[0,T]`; hence the indicators of survival up to each t increase to one almost surely and eventually are identically one along each such path. The stopped observable tends to the unstopped observable almost surely and in L2 because Phi and its undifferentiated contractions are bounded uniformly in time. It is continuous along each separated path by the established local regularity.

Every stopped drift integral converges in L1 by the absolute expected integral bounds just proved, with the integrand grouped as in (10.7). The stochastic integrals converge in L2 by Itô isometry and (11.2). Passing the stopped identity to the limit proves (10.7) at every deterministic time; taking continuous versions and a countable dense set of times proves the integrated identity simultaneously for all times. No corrector heat approximation is used. This is a direct collision-localization passage, and is not labelled heat-source convergence.

The conclusion requires no diagonal trace: bounded initial density assigns collision sets zero mass, and the actual paths never collide. The marginal integrations use the Lebesgue representatives whose weak derivatives and absolute contractions were proved above.

## 12. Falsification route, exact checks, and status of every claim

The proof route uses the repulsive symmetric-Jacobian bound and conditional occupation estimates. Its separate algebraic falsification route uses literal subset/distinct-label Fourier polynomials and exact rational arithmetic, not the diagonal-overlap derivation. The checker is

```text
python3 MEMORANDA/ROUND_008_DOMAIN_ARTIFACTS/round008_domain_exact_checks.py
```

It passes **4,405 exact assertions**, using Python's standard library only. There is no random seed or numerical tolerance. Its finite Fourier convention divides all second-order spatial expressions by the common factor `(2 pi)^2`; its one-coordinate fields are embedded in the allowed d-dimensional torus. It checks the unscaled factors separately through the frozen Fourier and radial constants. The tests are supporting algebraic evidence, not an independent audit of the new analytic lemmas.

The checker includes:

1. The exact full identity and raw R1 pair identity for N=2,3, zero and positive nu, zero and two-mode forces and homogeneous Coulomb Fourier cutoffs, with constant, relative, separable, additive, and mixed pair kernels. It chooses the instantaneous time derivative from the corrector equation and compares the direct N-particle generator against the fully contracted right side.
2. Literal deleted-label U2/U3 sums, both cubic background contractions, the vanishing full cubic Haar mean, the `1/N` lower contraction and `1/(2N)` scalar. Tests detect a missing U3 at N=2, a missing response slot, an incorrect lower term, and a missing scalar term.
3. The exact gradient of P and the generator product identity giving `2nu sum_i |grad_iP|^2`, including zero noise and all deletion factors. Constants h give J=0 and Phi=0 by uniqueness, so the actual theorem reduces to the zero identity.
4. The radial contraction versus transverse expansion eigenvalues; the exact `(m-alpha)2s/N` barrier coefficient; the positive diffusion term and exact Young maximum; every weak-derivative and triple-collision exponent inequality; the second-variation source inequality `s+3+q_1<q_2+s+2`.
5. The Coulomb constant recurrence and two compensated slots on supported finite Fourier modes. The analytic proof retains the true atom and Haar compensation; a truncated Fourier test is not substituted for the singular theorem.
6. All eighteen frozen input digests.

| THM028 assertion | Construction disposition | Load-bearing justification |
|---|---|---|
| Common local flow neighborhoods and expectation differentiation | PROVED_CANDIDATE | Arbitrarily high weighted moments, truncated path-supremum Sobolev argument, and segment/UI proof in Section 3. |
| First and second weighted spatial derivatives for every prescribed exponent pair | PROVED_CANDIDATE | Sections 4–6, including conditional future Jacobian estimates and the second-variation source. |
| Both compensated responses preserve weak/local derivatives | PROVED_CANDIDATE | Section 5; the two-singularity convolution estimate requires only each exponent below d. |
| C1 time derivative, including endpoints | PROVED_CANDIDATE | Independent weighted Dyson construction and explicit Leibniz formula (7.4). |
| Classical off-diagonal equation | PROVED_CANDIDATE | Comparison of the given martingale inverse with localized classical Itô. |
| Global H1, W2,1, and L1 time/internal-drift bounds | PROVED_CANDIDATE | Deleted-tube weak derivatives; structural PDE cancellation for B Phi. |
| Mixed backgrounds and all partial triple collisions | PROVED_CANDIDATE | Moving-tube continuity and separate relative-variable integrability. |
| Exact finite-N identity and square-integrable true martingale | PROVED_CANDIDATE | Direct distinct-label algebra, supplied density domination, L1 drift and L2 noise passage. |
| N-uniform residual/bracket smallness or fluctuation limit | OPEN / NOT CLAIMED | All new constants may depend strongly on N; no asymptotic law or smallness estimate is proved. |

No unsupported line in the bounded THM028 assertion was found in this construction and its self-check. Its audit status remains pending. The first subsequent unsupported line is an N/temperature-uniform estimate making the evolved cubic residual, lower contractions, and corrector self/cross brackets sufficiently small, together with the corresponding centering and limiting-law analysis. The fixed-N density factor in (1.2), and the barrier constants involving inverse powers of `a=2s/N`, cannot be treated as such estimates. No CLT, beta-to-zero uniformity, actual inhomogeneous regularity theorem, or critical hierarchy truncation/resummation follows.

## 13. Recoverable handoff and seals

Generated outputs are this memorandum, the exact checker, its JSON result, a README, copied-input and output manifests, and a sealed archive in `MEMORANDA/ROUND_008_DOMAIN_ARTIFACTS/`. The input manifest records the eighteen allowed source files. The output manifest records the issued proof, checker, results, README, and copied-input manifest; it excludes itself. The archive contains precisely those eighteen inputs and the named output packet, with no unrelated worktree files. A separate seal hashes the archive and output manifest. The old worktree and its prior report are untouched.

Verification includes the 4,405 exact checks; all eighteen input hashes; output hashes; archive CRC and member-by-member digest comparison; and confirmation of the assigned base and branch. This is a construction with a disclosed seed, and all verification performed here is a self-check. The proof is not independently certified by its own checker. After issuance the sealed memorandum is immutable; any correction must use a separately named superseding report.
