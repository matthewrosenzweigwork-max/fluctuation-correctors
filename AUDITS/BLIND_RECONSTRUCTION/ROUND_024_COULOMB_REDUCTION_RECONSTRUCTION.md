# AUD067 / TASK105 — entire THM047, independent reconstruction

Issued 2026-09-18 UTC. Fresh Astra Max worker, assigned isolated worktree `/Users/matthewrosenzweig/.codex/worktrees/hocf-r024-coulomb-reduction-blind`, root-provisioned base `3efdbb96e7b94529b280234e83eb36f5fca3ef36`.

**Verdict: PASS, the entire frozen THM047 conjunction is independently reconstructed from its statement and the expressly permitted prior modules.** No current constructor proof, narrative, code, results, or constructor source/exposure record was inspected. This is an isolated reconstruction, not the separate hostile review and not a canonical promotion. Earlier printed source statuses remain historical; this report does not infer their present acceptance or independently certify every preceding theorem. The exact source contracts actually used are listed below. THM046 remains open.

The decisive new mechanism is a punctured flux identity: the previously supplied structural integrability of the internal drift forces the spherical average to converge. Common translations then give the needed uniform smoothness of its contraction. Actual empirical Fourier control, derived from the genuine evolved expected energy, supplies the absolute lower-drift estimate. Retaining the critical diffusivity factor in the smoothed noise estimate gives the asserted martingale rate.

## 1. Entire assertion and its negation

The unit torus is four-dimensional with Haar mass one and characters `exp(2 pi i k.x)`. Set

\[
\widehat g(0)=0,\quad \widehat g(k)=|k|^{-2}\ (k\ne0),\quad
K=-\nabla g,\quad c=4\pi^2.
\tag{1.1}
\]

For every finite `N >= 2` use the actual singular gradient process, initially iid Haar and independent of its independent Brownian drivers,

\[
dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)dt+\sqrt{2\nu_N}\,dW_i,
\quad \beta_N=1/\nu_N>0,
\quad \lambda_N=\beta_N N^{-1/2}\longrightarrow\lambda\in(0,\infty).
\tag{1.2}
\]

The fixed datum is a finite `T >= 0` and a smooth real terminal test `h`. Let

\[
f_t=Q_{T-t}^{\nu_N}h,\qquad
\widehat{Q_a^\nu h}(k)=e^{-a(c+c\nu|k|^2)}\widehat h(k)\ (k\ne0),
\quad \widehat{Q_a^\nu h}(0)=\widehat h(0),
\]
\[
J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)).
\tag{1.3}
\]

Every tuple is ordered with distinct labels and denominator `N^k`. In particular

\[
P_N[v]=\frac1{2N^2}\sum_{i\ne j}v(X_i,X_j)
-\frac1N\sum_i q_v(X_i)+\frac12r_v,
\quad q_v(x)=\int v(x,y)dy,\quad r_v=\iint v.
\tag{1.4}
\]

For symmetric triple `F`,

\[
U_3[F]=\frac1{N^3}\sum_{i,j,k\ {\rm distinct}}F(X_i,X_j,X_k)
-\frac3{N^2}\sum_{i\ne j}F_1(X_i,X_j)
+\frac3N\sum_iF_2(X_i)-F_0,
\tag{1.5}
\]

where subscripts mean the actual Haar background integrations. In particular the first sum being empty at `N=2` does not make this statistic zero.

The supplied genuine symmetric terminal-zero full inverse is denoted by `Phi`; its off-diagonal equation and fixed-N R8 domain are retained:

\[
\partial_t\Phi+\nu\Delta_{x,y}\Phi+N^{-1}B\Phi+R\Phi=-J,
\quad B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi,
\]
\[
R\Phi=-2c\Phi+cq(x)+cq(y),\qquad q(x)=\int\Phi(x,y)dy.
\tag{1.6}
\]

With `rho = eta_N - dx`, set

\[
b_t(x)=\int B\Phi_t(x,y)dy,\quad
\ell_N(t)=N^{-1}\rho_t[b_t]+(2N)^{-1}\int b_t.
\tag{1.7}
\]

The full frozen conjunction is as follows.

- **A:** For every finite `N`, time, and remaining position, the normalized spherical average of `Phi_t(x,x-epsilon theta)` converges. Its value `tau_t(x)` is bounded in modulus by the supremum norm of `Phi_t`. With `D = grad_x + grad_y`,

\[
b_t(x)=\int K(z)\cdot D\Phi_t(x,x-z)dz+2c(q_t(x)-\tau_t(x)),
\quad
\sup_t\|b_t/\sqrt N\|_{C^j}\le C_j\|h\|_{C^{j+3}}
\tag{1.8}
\]

for every nonnegative integer `j`, uniformly over all `N >= 2` and positive diffusivities in a fixed bounded interval. The exact scalar `integral b_t` is zero for this genuine homogeneous-source inverse.

- **B:** On each admitted critical sequence, for all sufficiently large indices,

\[
\sqrt N\,\mathbb E\int_0^T|\ell_N(t)|dt\le C N^{-1/4}.
\tag{1.9}
\]

This is an actual-law absolute estimate.

- **C:** For

\[
\Psi_{t,\delta}=e^{\delta\Delta_x}e^{\delta\Delta_y}\Phi_t,
\quad \delta_N=N^{-1/40},\quad V_N=\Phi-\Psi_{\delta_N},
\]
\[
M_t^2[v]=\sqrt{2\nu_N}\sum_i\int_0^t\nabla_iP_N[v_a](X_a)\cdot dW_i(a),
\quad C\Phi=\operatorname{Sym}_3[K(x-z)\cdot\nabla_x\Phi(x,y)],
\]
\[
S_N=\sqrt N\int_0^TP_N[J_t]dt,
\quad
W_N=\sqrt N\left(\int_0^TU_3[C\Phi_t]dt+M_T^2[V_N]\right),
\tag{1.10}
\]

all random variables are genuine and integrable, the residual noise is a difference of true square-integrable martingales, and on the critical tail

\[
\mathbb E|S_N-W_N|\le
C\left[N^{-1/4}+\sqrt{\frac{1+\log N}{N}}+N^{-3/8}\right]\longrightarrow0.
\tag{1.11}
\]

Consequently the original THM046 L1 assertion is equivalent to `E|W_N| -> 0`, and its positive-limsup negation is preserved. This asserts neither limit. The exact rates concern indices satisfying fixed eventual positive upper and lower bounds on `lambda_N`; existence of such a tail follows from convergence, with no prescribed rate or bound on its starting index. Every finite earlier index remains within the fixed-N domain. This is the asymptotic sequence interpretation of the frozen rate, not a claim of a universal waiting index.

The **exact negation** is the existence of admitted fixed data, finite parameters, or critical family violating at least one assertion above: trace existence/bound, exact coefficients, smooth uniformity, scalar cancellation, actual-law absolute rate, finite-N domain/integrability, martingale interpretation, quantitative reduction, or limit/negation equivalence. The negation of a uniform estimate means that no constant with the stated permitted dependence works for the admitted family. A failed proof, an inadmissible law, an N-dependent test or horizon, separate nonvanishing of cubic/noise terms, or failure of THM046 itself is not this negation.

## 2. Source boundary and normalization preflight

All 21 allowed bytes were hash-verified before mathematical use, then exactly copied and reverified. No linked, nonallowlisted report was followed. The companion exposure document distinguishes full reads, partial reads, and hash-only inputs. The following are the exact imported contracts; equations subsequently needed beyond them are derived here.

| Permitted source | Contract actually used |
|---|---|
| Frozen R1 model; R1 algebra, lines 1–125 | Unit Haar/Fourier convention, ordered labels, all backgrounds, noise and drift coefficients. The finite pair algebra is reconstructed in Section 7. |
| R4 singular-response memorandum, Sections 2–4 | Local coefficient-one expansion, integrable force, exact finite divergence measure and both response slots. |
| R5 periodic-pair memorandum, Sections 2–9 | Actual noncolliding pair evolution, positive-source barrier, Borel Markov measure inequality, bounded source potential and Haar L2 control. Its limits are at fixed N. |
| R5 full-inverse and interface memoranda; both supplied clarifications | Actual Volterra inverse with both signed responses, sup/L2 construction and homogeneous backward test. Symmetry means exchange of slots, not Haar self-adjointness. |
| R6 particle memorandum, Sections 3–8 | Actual noncolliding N-particle process, same-noise fixed-N heat passage, and finite-N density domination. No uniform-in-N density constant is imported. |
| R8 full domain memorandum, Sections 5–11 | The exact given Phi has local C1 time/C2 space regularity, global H1 and W2,1 representatives, integrable time derivative, structurally integrable B Phi with uniformly integrable slices at fixed N, genuine background contractions, actual integrated identity and true L2 martingale. |
| R10 actual-law memorandum, Sections 2–6; R16 source memorandum, Sections 2–4 | Their energy/Fourier and smoothing mechanisms are independently rederived in Sections 5 and 8. No current audit label or unsmoothed noise conclusion is imported. |
| R12 and R14 permitted reports | Boundary checks only: their strict sub-Coulomb occupation/product estimates do not supply a Coulomb argument. |

Here and below constants are independent of `N`, time and the selected diffusivity in the specified bounded interval, unless a bound is explicitly marked fixed-N. They may depend on the fixed kernel, horizon, smooth test seminorms, derivative order, interval endpoint, and eventual critical bounds as stated.

For this particular kernel, the heat representation is especially simple:

\[
g(z)=c\int_0^\infty(p_u(z)-1)du,
\quad \widehat p_u(k)=e^{-c u|k|^2}.
\tag{2.1}
\]

The nonzero coefficient of the integral is `1/|k|^2`. The central Euclidean Gaussian integral, with the change of variables `v=|z|^2/(4u)`, equals `|z|^-2` with coefficient one. Noncentral translates have exponentially small differentiated bounds at small heat times; the large-time torus remainder decays exponentially. Thus on a fixed embedded ball,

\[
g(z)=|z|^{-2}+H(z),\quad H\text{ smooth and even},
\quad K(z)=2z|z|^{-4}+k(z),\quad k(z)=O(|z|).
\tag{2.2}
\]

The force is integrable in dimension four. Its leading outward flux is `2 |S^3| = 4 pi^2 = c`, and its Fourier divergence has coefficient `c` at each nonzero mode and zero at zero. Therefore the complete distribution is

\[
\operatorname{div}K=c(\delta_0-dz),\qquad
\operatorname{div}_{\rm cl}K=-c\quad(z\ne0).
\tag{2.3}
\]

This retains both the atom and the periodic constant. The homogeneous response in each slot is `-c` times that slot's value plus `c` times its Haar integration, giving (1.6). It has norm at most `4c` in both bounded-Borel sup norm and Haar L1/L2 for the sum of the two slots.

For any fixed `a >= 0`,

\[
Q_a^\nu=(1-e^{-ca})\Pi+e^{-ca}e^{\nu a\Delta},\qquad \Pi h=\int h.
\tag{2.4}
\]

Positivity and unit mass of the heat kernel show that this operator contracts every spatial C^m norm taken as the sum of derivative suprema. For positive-order derivatives the constant projection vanishes. Hence no Fourier summability loss is needed for the precise `C^(j+3)` dependence in (1.8).

The R5 local positive profile, specialized to (2.2), is

\[
F_{N,a}(r)=\frac N4\left[\sqrt{r^4+16a/N}-r^2\right]
\le\min(2ar^{-2},\sqrt{Na}).
\tag{2.5}
\]

Its punctured four-dimensional Laplacian is nonpositive. The fixed annular correction in the R5 positive barrier has constants uniform for bounded diffusivity. Thus the absolute source occupation and base potential are bounded by `C sqrt(N) ||h||C2`. Squaring the right side of (2.5), integrating against `r^3 dr`, and splitting at a constant multiple of `N^-1/4` gives `C(1+log N)||h||C2^2`; when that splitting radius exceeds the chart radius the bounded core gives the same all-N bound. The source itself has Haar L1 norm at most `C||h||C2`.

For the singular pair Markov evolution, its supplied measure inequality is

\[
\int S_{t,a}u\le e^{2c(a-t)/N}\int u\quad(u\ge0).
\tag{2.6}
\]

This is a Borel measure statement, not an L2-to-L1 inference. Jensen also gives the L2 norm exponent `c(a-t)/N`. Apply these estimates and the response norm to each ordered time-simplex term of the actual full Volterra series. The semigroup interval lengths add; the response factors sum with their factorial denominators. The result is

\[
\sup_t\|\Phi_t[h]\|_\infty\le C\sqrt N\|h\|_{C^2},
\quad
\sup_t\|\Phi_t[h]\|_1\le C\|h\|_{C^2},
\quad
\sup_t\|\Phi_t[h]\|_2^2\le C(1+\log N)\|h\|_{C^2}^2.
\tag{2.7}
\]

The Borel and norm series represent the same supplied inverse by its uniqueness. Neither response is a Markov operator or has been discarded.

## 3. Common translations and uniform smooth bounds

Write `h_a(x)=h(x+a)`. Simultaneously translating both pair coordinates leaves the base dynamics and both response kernels unchanged. Translating the source is exactly replacement of `h` by `h_a`. Linearity and uniqueness of the full Volterra construction therefore give, pointwise off the diagonal,

\[
\Phi_t[h](x+a,y+a)=\Phi_t[h_a](x,y).
\tag{3.1}
\]

Difference quotients of `h_a` converge to the corresponding derivative of `h` in C2. Apply the first bound in (2.7) to their differences. This proves convergence of the corresponding Phi difference quotients in the global bounded-Borel supremum norm. Their local classical values agree with the R8 representative. Iterating gives every simultaneous derivative and the exact identity

\[
D^\alpha\Phi_t[h]=\Phi_t[\partial^\alpha h],\qquad
\sup_t\|D^\alpha\Phi_t[h]\|_\infty
\le C\sqrt N\|h\|_{C^{|\alpha|+2}}.
\tag{3.2}
\]

Only simultaneous derivatives are bounded this way; no bound on arbitrary individual pair derivatives is inferred.

The R8 fixed-N domain supplies every slice of B Phi as an absolutely integrable function. This uses its structural equation

\[
B\Phi=-N(J+\partial_t\Phi+\nu\Delta_{x,y}\Phi+R\Phi),
\tag{3.3}
\]

and its integrable weighted bounds on the four terms, not the potentially nonintegrable product `|K| |grad Phi|`. At this endpoint such a product bound would fail for the previously allowed first-derivative exponents. It is precisely (3.3) that will justify the next flux limit.

## 4. Spherical-average trace, exact flux and scalar cancellation

Fix `N,t,x` and put

\[
F_x(z)=\Phi_t(x,x-z),\qquad D\Phi=(\nabla_x+\nabla_y)\Phi.
\]

The chain rule on the punctured torus gives

\[
B\Phi_t(x,x-z)=K(z)\cdot D\Phi_t(x,x-z)
                  +2K(z)\cdot\nabla_zF_x(z).
\tag{4.1}
\]

The first term is absolutely integrable by (3.2) and `K in L1`; the left side has the fixed-N slice integrability (3.3). Consequently the scalar product `K dot grad_z F_x` is absolutely integrable, even though an absolute product of the two vector norms need not be. This distinction is necessary.

Integrate on the torus with the radius-epsilon ball deleted. The inner outward normal is `-theta`. Using (2.3) for the ordinary divergence away from zero and (2.2) at the inner boundary,

\[
\int_{|z|>\epsilon}K(z)\cdot\nabla_zF_x(z)dz
=c\int_{|z|>\epsilon}F_x(z)dz
-2\int_{\mathbb S^3}F_x(\epsilon\theta)dS(\theta)
+O(\epsilon^4\|\Phi_t\|_\infty).
\tag{4.2}
\]

The remainder uses `k(epsilon theta)=O(epsilon)` and boundary area `epsilon^3`. There is no outer boundary on the torus. The left side has a limit by the absolute integrability just established; the first right-hand integral converges by boundedness. Thus the spherical integral has a limit along the full epsilon limit, with no subsequence or Sobolev trace theorem. Since `2 |S^3|=c`, the normalized limit `tau_t(x)` satisfies

\[
\int K\cdot\nabla_zF_x=cq_t(x)-c\tau_t(x),
\qquad |\tau_t(x)|\le\|\Phi_t\|_\infty.
\tag{4.3}
\]

Combining with (4.1) proves the coefficient-exact contraction formula (1.8).

The bound in (1.8) with `j=0` follows at once:

\[
\|b_t\|_\infty
\le\|K\|_1\|D\Phi_t\|_\infty+4c\|\Phi_t\|_\infty
\le C\sqrt N\|h\|_{C^3}.
\tag{4.4}
\]

This also proves continuity of the map from smooth `h` with the C3 norm to `b_t` in supremum norm. Translation covariance for the actual B-Phi contraction follows either by changing its Haar variable or from (4.1)–(4.3):

\[
b_t[h](x+a)=b_t[h_a](x).
\tag{4.5}
\]

Apply (4.4) to difference quotients of the test in C3. The uniform limit is `b_t[partial h]`; the supplied R8 contraction is continuous, and the uniform difference-quotient limit proves it has that classical derivative. Iteration yields

\[
\partial^\alpha b_t[h]=b_t[\partial^\alpha h],\qquad
\sup_t\|b_t/\sqrt N\|_{C^j}\le C_j\|h\|_{C^{j+3}}.
\tag{4.6}
\]

The constants are uniform over the entire prescribed bounded noise interval and all `N >= 2`. No derivative of the spherical trace was assumed to obtain this result.

Finally average (4.5) in `a`. The test translations are continuous in C3, so the bounded linear map in (4.4) commutes with this integral, first for Riemann sums and then their uniform limit. Their average is the constant `integral h`, whose source and unique inverse are zero. Therefore

\[
\int b_t[h](x)dx=b_t[\,\textstyle\int h\,](0)=0.
\tag{4.7}
\]

This is an operator identity for the genuine homogeneous-source inverse. It is false for a general symmetric kernel, as the exact relative-cosine diagnostic below shows. It is not inferred from an actual-law signed expectation.

Equations (4.2)–(4.7) prove every part of A, for all times including `t=T`. No pointwise diagonal value or directionwise limit has been proved or used.

## 5. Actual expected energy and empirical Fourier control

This section reconstructs the law-class bridge needed for B and the smoothed martingale. It uses the actual iid preparation and gradient dynamics.

Let

\[
H_N=\frac1N\sum_{i<j}g(X_i-X_j),\qquad g_*:=\inf_{z\ne0}g(z)>-\infty.
\]

At fixed positive heat cutoff epsilon and positive noise, the smooth potential `H_N^epsilon` and its smooth actual density `F_t^epsilon`, initially one, satisfy the smooth periodic Fokker–Planck equation. At this fixed cutoff all derivatives of the coefficients are bounded. The heat integral equation gives a smooth solution; comparison with positive constants times exponentials gives finite upper and positive lower bounds on a fixed time interval. Entropy differentiation and periodic integration by parts therefore give

\[
\frac d{dt}\left(\nu\int F_t^\epsilon\log F_t^\epsilon
             +\int H_N^\epsilon F_t^\epsilon\right)
=-\int F_t^\epsilon
 |\nabla H_N^\epsilon+\nu\nabla\log F_t^\epsilon|^2\le0.
\tag{5.1}
\]

Both initial terms are zero: initial density is one and each pair has Haar difference with zero-mean interaction. Entropy on mass-one Haar space is nonnegative, so `E H_N^epsilon <= 0`. The supplied R6 same-noise passage is at fixed `N,nu,T`; actual noncollision gives a positive realized minimum separation. Thus `H_N^epsilon(X_t^epsilon)` converges almost surely to `H_N(X_t)` at every deterministic time. Heat positivity gives the common lower bound `(N-1)g_*/2`. Fatou after subtracting this bound proves

\[
\mathbb E H_N(X_t)\le0.
\tag{5.2}
\]

It also proves finite integrability after the same shift. This argument does not pass a singular entropy-dissipation identity. Exchangeability and common-translation invariance of the actual law follow from pathwise uniqueness and the preparation. In particular one-body marginals are Haar, but higher marginals have not been identified with iid Haar. No estimate below uses an N-uniform density supremum.

For `0 < r <= 1`, truncate the positive heat representation only at this deterministic scale:

\[
g^{>r}(z)=c\int_r^\infty(p_u(z)-1)du,
\quad a_r(k)=|k|^{-2}e^{-cr|k|^2}>0\ (k\ne0).
\tag{5.3}
\]

The low-time positive heat kernel gives `g >= g^{>r} - cr` off zero. Also
`0 <= g^{>r}(0) <= C/r`, by integrating the four-dimensional Gaussian bound at small times and exponential decay at large times. Apply the comparison only to deleted pairs, and subtract the smooth self diagonal exactly:

\[
\frac{H_N(x)}N\ge
\frac12\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2
-\frac{g^{>r}(0)}{2N}-\frac{N-1}{2N}cr.
\tag{5.4}
\]

Every term in the sum is nonnegative. Taking actual expectations and using (5.2), then choosing `r_N=N^-1/2`, yields

\[
\mathbb E\sum_{k\ne0}a_{r_N}(k)|\widehat\eta_N(t,k)|^2
\le C(N^{-1}r_N^{-1}+r_N)=C N^{-1/2}.
\tag{5.5}
\]

For `0 < |k| <= N^1/4`, the multiplier is at least `e^-c |k|^-2`; for larger frequencies use the deterministic bound `|eta_hat(k)| <= 1`. Enlarging one fixed constant gives

\[
\mathbb E|\widehat\eta_N(t,k)|^2
\le\min(1,C N^{-1/2}|k|^2),\qquad k\ne0.
\tag{5.6}
\]

All bounds are uniform in deterministic time and the admitted noise interval. This is actual-law control. At Coulomb the punctured divergence is the negative constant (2.3); no positive `r^-4` occupation estimate has been asserted.

For any deterministic smooth scalar test `a`, its absolutely convergent Fourier expansion and Minkowski in the actual probability space now give

\[
\big(\mathbb E|\rho_t[a]|^2\big)^{1/2}
\le C N^{-1/4}\sum_{k\ne0}|k|\,|\widehat a(k)|
\le C N^{-1/4}\|a\|_{C^6}.
\tag{5.7}
\]

For the last inequality, six integrations by parts in a coordinate of maximal `|k_j|` bound its coefficient by `C ||a||C6 (1+|k|)^-6`; the weighted lattice sum converges in dimension four. The test may depend deterministically on `N,t,nu`; its displayed norm is retained.

## 6. Absolute lower drift

Put `a_t=b_t/sqrt(N)`. Equations (4.6) and (4.7) imply

\[
\sqrt N\,\ell_N(t)=\rho_t[a_t],\qquad
\sup_t\|a_t\|_{C^6}\le C\|h\|_{C^9}.
\tag{6.1}
\]

Apply (5.7), then Cauchy–Schwarz in probability and Tonelli in time:

\[
\sqrt N\,\mathbb E\int_0^T|\ell_N(t)|dt
=\int_0^T\mathbb E|\rho_t[a_t]|dt
\le C T\|h\|_{C^9}N^{-1/4}.
\tag{6.2}
\]

This proves B, in fact on every bounded-noise family, without criticality. The scalar was retained until its separate exact cancellation. Neither a signed mean nor an iid positive-time estimate is substituted for the absolute value.

## 7. Finite-N identity, backgrounds and initial endpoint

Here is a direct reconstruction of the coefficients in the actual-domain identity. Put `p=grad_x Phi`, `A=grad q`. On a separated configuration the force part of the generator acting on (1.4) is

\[
\mathcal F=\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}
K(X_i-X_k)\cdot p(X_i,X_j)
-\frac1{N^2}\sum_{i\ne k}K(X_i-X_k)\cdot A(X_i).
\tag{7.1}
\]

Separate `k=j`. Pairing the two orientations gives the repeated-label part `D_2[B Phi]/(2N)`, where `D_2[v]=N^-2 sum_(i!=j) v`. The remaining three-label part is the ordered sum of `C Phi` with coefficient one. Write

\[
A_K(x,y)=K(x-y)\cdot(A(x)-A(y)),\quad
v(x)=\int K(z-x)\cdot A(z)dz.
\]

Integrating the six terms defining the cubic gives

\[
(C\Phi)_1=(A_K+R\Phi)/6,\quad
(C\Phi)_2=v/3,\quad(C\Phi)_0=0,
\quad(R\Phi)_\mu=v,\quad\iint R\Phi=0.
\tag{7.2}
\]

The R8 domain supplies the absolute integrability of these particular mixed contractions: the two force/gradient singular points in a background variable are separated, and distinct relative variables at a triple collision have separately integrable exponents. No diagonal extension is involved. Substitution in (1.5) gives

\[
\mathcal F=U_3[C\Phi]+P_N[R\Phi]+\frac1{2N}D_2[B\Phi].
\tag{7.3}
\]

The time/diffusion part is `P_N[(partial_t+nu Delta_pair)Phi]`. Use (1.6) and the exact identity

\[
\frac1{2N}(D_2[B\Phi]-2P_N[B\Phi])
=\frac1N\rho[b]+\frac1{2N}\int b=\ell_N.
\tag{7.4}
\]

This reconstructs

\[
dP_N[\Phi_t]=\{-P_N[J_t]+U_3[C\Phi_t]+\ell_N(t)\}dt+dM_t^2[\Phi].
\tag{7.5}
\]

The derivative of the literal statistic is

\[
\nabla_iP_N[\Phi]=N^{-2}\sum_{j\ne i}p(X_i,X_j)-N^{-1}A(X_i),
\quad d\langle M^2[\Phi]\rangle_t=2\nu\sum_i|\nabla_iP_N[\Phi_t]|^2dt.
\tag{7.6}
\]

Independent noises have no cross variation for the two distinct labels. Background Haar Laplacians integrate to zero in the supplied W2,1/slice domain, so there is no extra thermal trace. R8 proves passage from compact collision stops: grouped drift terms converge in expected absolute integral and stochastic integrals converge in L2. Its density factor can depend on `N` and is used here only to establish each finite-N identity and square integrability. It is not used in (6.2) or the uniform smoothing bound below.

For the initial endpoint, let a general symmetric square-integrable kernel have mean `r`, first centered projection `q_0=q-r`, and canonical part

\[
v^\circ(x,y)=v(x,y)-q_0(x)-q_0(y)-r.
\]

Literal expansion of (1.4) under iid Haar gives

\[
P_N[v]=\frac1{2N^2}\sum_{i\ne j}v^\circ(X_i,X_j)
-\frac1{N^2}\sum_iq_0(X_i)-\frac r{2N}.
\tag{7.7}
\]

The three components are orthogonal in L2. In the canonical pair square only identical unordered label sets contribute; their two orders give exactly

\[
\mathbb E P_N[v]^2
=\frac{N-1}{2N^3}\|v^\circ\|_2^2+\frac1{N^3}\|q_0\|_2^2+\frac{r^2}{4N^2}.
\tag{7.8}
\]

Since `||v||2^2=||v^circ||2^2+2||q_0||2^2+r^2`, comparison of the three coefficients for `N >= 2` yields

\[
\mathbb E|\sqrt N P_N[v]|^2\le\frac{N-1}{2N^2}\|v\|_2^2.
\tag{7.9}
\]

Apply this only at time zero with the actual iid initial law and use (2.7):

\[
\mathbb E|\sqrt N P_N[\Phi_0]|\le C\sqrt{(1+\log N)/N}.
\tag{7.10}
\]

No iid structure at positive time is needed.

## 8. The precise smoothed-martingale rate

Fix `0 < delta <= 1`. By the Haar L1 bound in (2.7), every pair Fourier coefficient of `Phi_t` is bounded by the same constant independent of `N,nu,t`. Let

\[
G_\delta=\nabla_x\Psi_\delta,\qquad
A_\delta(x)=\int G_\delta(x,y)dy.
\]

Writing `G_delta,k(x)` for the y-Fourier coefficient, the heat multiplier and the differentiated x sum give

\[
\sup_x|G_{\delta,k}(x)|\le C\delta^{-5/2}e^{-c\delta|k|^2},
\quad \|G_\delta\|_\infty\le C\delta^{-9/2},
\quad \sum_{k\ne0}|k|\sup_x|G_{\delta,k}(x)|\le C\delta^{-5}.
\tag{8.1}
\]

For completeness the lattice estimates used here follow by grouping unit cubes and bounding finitely many cubes near zero separately: for any fixed nonnegative power `m`, the sum of `|k|^m exp(-c delta |k|^2)` in four dimensions is at most `C delta^(-(4+m)/2)`. The corresponding radial Gaussian integral follows after rescaling by `sqrt(delta)`. This proves all three powers in (8.1).

For the smooth kernel only, the exact deleted-label gradient can be rewritten as

\[
\nabla_iP_N[\Psi_\delta]
=\frac1N\left(v_\delta(X_i)-\frac1N G_\delta(X_i,X_i)\right),
\quad
v_\delta(x)=\int G_\delta(x,y)\rho_t(dy).
\tag{8.2}
\]

The diagonal in this formula belongs solely to the smooth kernel. Expanding in y-Fourier modes, taking a supremum before evaluating at any particle, and applying Minkowski and (5.6) gives

\[
\mathbb E\sup_x|v_\delta(x)|^2
\le C N^{-1/2}\left(\sum_{k\ne0}|k|\sup_x|G_{\delta,k}(x)|\right)^2
\le C N^{-1/2}\delta^{-10}.
\tag{8.3}
\]

No independence between an empirical measure and the particle at which it is evaluated was assumed. The true smooth martingale has bounded integrands for each finite `N,delta`; Itô isometry, (8.2), and the two-term square inequality give

\[
\mathbb E|\sqrt N M_T^2[\Psi_\delta]|^2
=2\nu N\mathbb E\int_0^T\sum_i|\nabla_iP_N[\Psi_{t,\delta}]|^2dt
\le C\nu\left(N^{-1/2}\delta^{-10}+N^{-2}\delta^{-9}\right).
\tag{8.4}
\]

In particular the factor `nu` has not been replaced by a constant before criticality is used. On a critical tail, `nu_N=lambda_N^-1 N^-1/2` with bounded `lambda_N^-1`. Set exactly `delta_N=N^-1/40`. The two exponents in (8.4) are

\[
-\tfrac12-\tfrac12+\tfrac{10}{40}=-\tfrac34,
\qquad -\tfrac12-2+\tfrac9{40}=-\tfrac{91}{40}<-\tfrac34.
\]

Therefore

\[
\mathbb E|\sqrt N M_T^2[\Psi_{\delta_N}]|
\le\left(\mathbb E|\sqrt N M_T^2[\Psi_{\delta_N}]|^2\right)^{1/2}
\le C N^{-3/8}.
\tag{8.5}
\]

This estimates the actual smoothed martingale. It says nothing about uniform actual-law smallness of the discarded singular gradients.

## 9. Exact residual identity, all limits and degeneracies

For each finite `N`, the R8 martingale for Phi is true and square integrable. Heat smoothing in space gives a smooth kernel with bounded gradients on the compact torus, measurable in time. Its stochastic integral is also true and square integrable. The common weak gradient of `V_N=Phi-Psi` is their difference, and linearity of the stochastic integral in L2 gives exactly

\[
M_T^2[\Phi]=M_T^2[V_N]+M_T^2[\Psi_{\delta_N}].
\tag{9.1}
\]

Thus the residual is defined through genuine particle gradients, not a formal subtraction of divergent brackets. R8 gives expected absolute time integrability of the cubic and source at each finite `N`; the lower drift has (6.2); the initial endpoint has (7.10). Every quantity in (1.10) is consequently an L1 random variable.

The terminal kernel is exactly zero. Integrating (7.5) and rearranging retains all signs:

\[
\int_0^TP_N[J_t]dt
=P_N[\Phi_0]+\int_0^TU_3[C\Phi_t]dt+\int_0^T\ell_N(t)dt+M_T^2[\Phi].
\tag{9.2}
\]

Subtract (1.10), using (9.1), to obtain the exact equality

\[
\boxed{\ S_N-W_N=\sqrt N\left(P_N[\Phi_0]
+\int_0^T\ell_N(t)dt+M_T^2[\Psi_{\delta_N}]\right).\ }
\tag{9.3}
\]

Equations (6.2), (7.10), and (8.5) prove (1.11) by the triangle inequality. There is no assumption that the cubic and residual martingale separately vanish or separately have small absolute-time-integral norms.

For all sufficiently large `N`, `beta_N=lambda_N sqrt(N)>1`, so `b_N=min(beta_N,1)=1` and the original THM046 normalization is exactly `sqrt(N)`. An arbitrary finite initial segment cannot affect an N-limit or limsup. Also

\[
\left|\mathbb E|S_N|-\mathbb E|W_N|\right|
\le\mathbb E|S_N-W_N|\longrightarrow0.
\tag{9.4}
\]

Consequently vanishing of either expectation is equivalent to vanishing of the other. Their extended nonnegative limsups agree, including the case of an infinite limsup, so positive limsup is preserved. No rate of convergence of `lambda_N` was invoked, only fixed bounds on its eventual tail.

If `T=0`, the terminal-zero inverse is zero throughout its one-time domain and all time integrals/martingales are zero. If `h` is constant, its gradient difference is zero, so the source and unique inverse are zero for every horizon and noise; every displayed object is zero. At `N=2`, (1.5) retains its backgrounds and (7.8) remains valid. The proof of A stays uniform as positive noise tends to zero on a bounded interval, but no reciprocal of zero is taken and no additional zero-noise sequence theorem is inserted into the card.

All limits used above have their order and mechanism specified: the singular particle heat passage is fixed-N with same-noise path convergence and Fatou; the trace is a fixed-N full-radius limit of absolutely integrable fluxes; the smooth scale is inserted only after a uniform inequality is proved; the critical N-limit is then a direct power bound. No interchange of the singular and N limits is used.

## 10. Fresh falsification route and diagnostic history

The fresh read-only standard-library checker `exact_checks.py` was written in this isolated context. It imports no previous checker or result. Its final run passes **593 exact assertions in 19 categories**, with **11 nonzero mutation witnesses**. Arithmetic consists of exact fractions and Laurent polynomial coefficient dictionaries; there is no random seed, numerical tolerance or singular-process simulation. A formal first derivative is the physical derivative divided by `2 pi i`; all force/source/generator identities consistently restore the square of this common factor. The first-coordinate Fourier examples embed in the admitted four-dimensional torus.

This route independently differentiates the literal finite-particle observable, constructs each Haar subset term in U3, and compares the resulting exact polynomials. It also computes the exact iid second moment by Haar integration of the observable square. The cases include `N=2,3,4`, zero and nonzero smooth two-mode forces, zero and positive diffusivity, and constant, additive, relative, product, mixed and nonzero-mean kernels. These are universal algebra checks, not substitutes for the singular domain theorem.

The force pairings in the flux diagnostic are exact evaluations against the genuine Coulomb distribution for smooth finite-mode probes: only finitely many exact coefficients of the actual singular kernel enter those integrals. In particular, for a relative cosine with mean zero and diagonal one, common translation derivative zero, the exact contraction is `-2c`. For a constant probe it is zero because `q=tau`; deleting the periodic compensation fails. For an additive nonconstant probe the common-translation term is nonzero. These are not counterexamples to the scalar-zero assertion for the genuine source inverse: they demonstrate why its separate translation-averaging proof is indispensable.

A separate solvable local model is the noiseless coefficient-one radial Coulomb pair flow,

\[
r(a)^4=r(0)^4+16a/N,
\quad \int_0^a 2r(u)^{-2}du
=\frac N4\left[\sqrt{r(0)^4+16a/N}-r(0)^2\right].
\tag{10.1}
\]

Direct rational differentiation verifies its transport equation, nonpositive four-dimensional radial Laplacian, and the squared bound by `N a`. Its collision average is `sqrt(N a)`. This tests the local force factor and natural supremum scale, not the torus responses or actual N-body limit.

Every listed mutation has a stored nonzero coefficient witness: dropping the scalar; halving the centered lower coefficient; omitting one response slot; dropping U3 at N=2; omitting the smooth self-label subtraction; replacing N-squared by a falling-factorial denominator; deleting periodic compensation; halving trace flux; omitting the common-translation term; deleting the energy self diagonal; and halving relative repulsive drift. The code stores a concrete case, frequency and exact difference for each. It is impossible to pass this test merely because an altered term happened to vanish on all probes.

The first completed checker run passed 594 assertions. Before issuance one uninformative finite-prefix arithmetic assertion was removed; the mathematical code and all nonzero mutation witnesses were unchanged. The final 593-assertion result was regenerated. No failed mathematical run or failed assertion was suppressed. The chronological verification record and exact final output are in the packet.

## 11. Adversarial self-check and dispositions

This isolated construction performed its own adversarial checks; it is not the separately assigned hostile axis.

| Potential failure | Exact disposition |
|---|---|
| Inferring a pointwise diagonal from H1/W2,1 | Not used. The full spherical limit follows from (4.2) and the structurally integrable scalar product. |
| Estimating `|K| |grad Phi|` at Coulomb | Not used for B Phi. Equation (3.3) is the supplied integrability mechanism. |
| Missing the inner-boundary orientation, factor two, or compensation | The punctured outward normal is negative radial; (4.2)–(4.3) give exactly `2c(q-tau)`. All three terms have exact mutation probes. |
| Losing derivatives of h in Fourier summability | The precise A norm uses the heat/constant contraction (2.4), not a crude Fourier seminorm. Only the B estimate later uses a finite, explicitly adequate C9 seminorm of the fixed h. |
| Setting the scalar to zero for every symmetric kernel | False in general. The genuine-source cancellation is separately proved by translation averaging in (4.7). |
| Replacing actual law with positive-time iid or a uniform N-body density | Uniform estimates use actual expected energy and (5.6). Fixed-N density is used only within the given domain passage. |
| Extending strict sub-Coulomb occupation estimates | Not used. Its singular-density coefficient vanishes here. The proof uses smooth empirical observables and positive Fourier energy. |
| Using signed expectation for B | Equation (5.7) is a second-moment bound and (6.2) controls the absolute time integral. |
| Dropping the missing self label in smoothing | It is retained in (8.2) and yields the second term of (8.4). |
| Losing the stated martingale rate | Keeping `nu_N` gives bracket order N to the power -3/4 and hence L1 order N to the power -3/8. |
| Proving an incorrect residual sign or normalization | The exact integrated equality is (9.3); the iid endpoint and lower drift enter with plus signs. |
| Claiming full dynamics from an exact reduction | Not claimed. The combined quantity W_N is the unresolved load-bearing target. |

| Frozen clause | Verdict |
|---|---|
| A: full averaged-trace existence, bound, contraction coefficients, all Cj norms, scalar zero | Reconstructed completely in Sections 2–4. |
| B: actual expected absolute lower drift, critical tail | Reconstructed in Sections 5–6; a stronger bounded-noise estimate is obtained. |
| C: all finite-N genuine domains, endpoint, smoothed martingale, exact reduction and rate | Reconstructed in Sections 7–9 with the precise supplied R8 domain. |
| T=0, constant h, N=2, bounded-noise uniformity, arbitrary critical convergence rate, finite initial segment | Checked explicitly. |
| Exact negation of THM047 | No admitted counterexample; excluded by the reconstruction relative to the stated prior-module contracts. |
| THM046 or separate cubic/residual-noise vanishing, Gaussian limit, hierarchy closure | OPEN / NOT ASSERTED. |

There is no first failing line in the bounded THM047 implication. Its imported analytic foundation is exactly the R5/R6/R8 source contract listed in Section 2, whose present canonical audit status must be checked by the root outside this isolated lane. The first remaining dynamic obligation is `E|W_N| -> 0` for the actual critical model, including possible cancellation between its integrated cubic and residual martingale. This report supplies no proof or disproof of that obligation.

## 12. Issuance and recoverable handoff

The sole mathematical output is this report. Its companion directory is `ROUND_024_COULOMB_REDUCTION_BLIND_ARTIFACTS_20260918_082033_UTC`. It contains the 21 exact input copies, input inventory and hashes, source/exposure disclosure, final checker and results, chronological verification history, README, portable read-only verifier and output manifest. A sibling archive, exact member/digest manifest, verification result and outer seal complete the handoff.

Before issuance, the verifier checks every input/output hash; safe unique regular read-only member bytes; exact archive membership and member digests; CRC; all final diagnostics; and equality of the rerun diagnostic output with the issued JSON. It performs no writes and launches the diagnostic with Python bytecode generation disabled. Issued report, packet members, archive and seals are read-only. No post-issuance byte is altered; a correction must be a distinct superseding artifact.

No canonical files or inputs were modified, and no commit, push, child, dependency installation, memory/history lookup, external browsing, other-worktree read or current constructor exposure occurred. The supplied base is recorded as provisioned metadata, not independently checked through forbidden history. No TeX file was created or modified; the handoff response contains no mathematical LaTeX. Root alone compares this sealed reconstruction with the still-withheld current construction and arranges a separate hostile review before assigning canonical status.
