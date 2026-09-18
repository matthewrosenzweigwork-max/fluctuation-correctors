# AUD059 — statement-only reconstruction of the whole THM042

TASK091. Issued 2026-09-18 UTC. Fresh bounded reconstruction at base e75f8b780682a7e9fb0715b5e8b5873be684a2e8, branch codex/hocf-r020-continuous-path-blind, in /Users/matthewrosenzweig/.codex/worktrees/hocf-r020-continuous-path-blind.

**Verdict: the entire frozen assertion reconstructs conditionally on the supplied complete earlier source premises.** The new path-space steps are proved below: a common deterministic source envelope gives an actual supremum remainder in \(L^1\); uniform fourth moments give tightness in the uniform topology; a Gaussian Hilbert-space construction gives a continuous limiting process; polygonal approximation identifies the full weak limit. No counterexample in the admitted law class was found. This is a statement-only independent reconstruction of THM042, with its own self-checks. It is not independent certification of the earlier source modules, not the separate hostile gate, and not campaign completion.

The task and its controlling manifest were the first repository reads. Exactly fourteen mathematical/control inputs were copied and SHA-256 checked before use. The complete R18 construction was an expressly permitted earlier conditional input. No R20 construction, current audit, R19/R21 proof or audit, R18 audit, state/history/memory, root scratch, previous program or result artifact, external search, child agent, canonical edit, commit or push was used. The source/exposure records in the sealed packet give exact read ranges and the isolation boundary. General orientation instructions were narrowed by the explicit task.

## 1. Assertion, negation, constants and source boundary

Fix integer \(d\ge3\), \(0<s\le d-2\), \(s<d/2\), finite \(T\ge0\), a finite positive integer \(m\), and fixed real \(C^\infty\) periodic functions \(h_1,\ldots,h_m\). The torus \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) has Haar mass one. Write \(\mu=dx\), with Fourier characters \(e^{2\pi i k\cdot x}\), and

\[
 \widehat g(0)=0,\quad \widehat g(k)=c_{d,s}|k|^{s-d},\quad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad K=-\nabla g.
 \tag{1}
\]

For \(N\ge2\), the actual noncolliding singular gradient particles obey

\[
 dX_i(r)=\frac1N\sum_{\ell\ne i}K(X_i-X_\ell)\,dr+\sqrt{2\nu_N}\,dW_i(r),
 \quad\eta_N=N^{-1}\sum_i\delta_{X_i},\quad\rho_N=\eta_N-dx.
 \tag{2}
\]

The initial coordinates are iid Haar and independent of the independent standard Brownian drivers. The filtration includes the initial vector. Every \(0\le\nu_N\le\nu_*<\infty\), and \(\nu_N\to\bar\nu\ge0\), with no rate. Set \(b(\nu)=1\) for \(0\le\nu\le1\), \(b(\nu)=1/\nu\) above one, \(b_N=b(\nu_N)\), \(\bar b=b(\bar\nu)\), and \(\sigma_N=\sqrt{Nb_N}\). In particular \(\nu b(\nu)=\min(\nu,1)\), also at zero.

The whole primary assertion is exact one-body Haar centering and weak convergence of the continuous vectors

\[
 Z_N(r)=(\sigma_N\rho_N(r)[h_j])_{j=1}^m
 \quad\hbox{in } C([0,T],\mathbb R^m),\qquad
 \|z\|_\infty=\sup_{r\in[0,T]}|z(r)|,
 \tag{3}
\]

to a centered continuous Gaussian process with the exact covariance (39) below. Existence, continuity, possible degeneracy, all stated zero-noise/time/constant/linear-dependence cases, tightness and full weak convergence are included. The exact negation is some admitted fixed datum and bounded convergent noise sequence violating exact centering, continuity/existence of the specified Gaussian process, tightness of the actual path laws, or this weak convergence. A failed estimate is not the negation.

All constants below are finite and depend only on \(d,s,T,\nu_*,m\), the fixed kernel and fixed tests, unless an additional dependence is displayed. They are independent of \(N,\nu_N\), deterministic observation/integration times, collision stops, particle heat cutoff and deterministic splitting scale. Some preliminary particle estimates are deliberately fixed-\(N\) and explicitly marked. The statements at \(T=0\) are handled separately in Section 12.

The source boundary is exact. R4 supplies its proved-in-file heat representation and full divergence measure; R6 supplies the complete fixed-\(N\) actual path construction and heat passage; R10 Sections 2–3 supply the complete actual energy/Fourier argument; R16 Sections 2–7 supply the complete positive splitting, commutator and singular remainder argument. Their issued conditional/audit statuses are unchanged. R18 is a complete earlier conditional finite-dimensional source; its time-point result is not a premise for tightness. We check and reconstruct the necessary calculations below. No unseen result merely cited in those documents is imported. In particular their other inverse, hierarchy, entropy-tail, R17-comparison and corrector-domain assertions are nondependencies.

## 2. Normalization, actual paths, energy and Haar centering

Put \(\alpha=(d-s)/2\ge1\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). The positive unit-mass periodic heat kernel \(p_u\) gives

\[
 g=A\int_0^\infty u^{\alpha-1}(p_u-1)\,du,\qquad
 A\frac{\Gamma(\alpha)}{(4\pi^2|k|^2)^\alpha}=c_{d,s}|k|^{s-d}.
 \tag{4}
\]

Small-time Haar integrability follows from \(\|p_u-1\|_1\le2\); large-time convergence follows from its exponentially decaying nonconstant Fourier series. The central Euclidean Gaussian integral, with substitution \(w=|z|^2/(4u)\), is exactly \(|z|^{-s}\). The remaining lattice terms have all differentiated small-time bounds of the form a power of \(u^{-1}\) times \(e^{-c/u}\). The large-time remainder is integrable after every spatial differentiation. Thus locally \(g(z)=|z|^{-s}+H(z)\) with smooth \(H\), and \(g_*:=\inf g>-\infty\), in fact \(g_*<0\). Also \(K\in L^1\), since \(s+1<d\).

Distributional integration by parts outside a ball produces the inner flux

\[
 s r^{d-s-2}\int_{\mathbb S^{d-1}}a(r\theta)\,dS(\theta)+O_a(r^{d-1}).
\]

It vanishes below Coulomb; at Coulomb it converges to \(c_d a(0)\), where \(c_d=(d-2)|\mathbb S^{d-1}|\). Fourier identification and the gamma recurrence give the full finite measure

\[
 D:=\operatorname{div}K=
 \begin{cases}s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \quad D(\mathbb T^d)=0,\quad D\ge-\kappa\,dx,
 \tag{5}
\]

with \(\kappa\) depending only on the kernel. Its nonzero Fourier coefficients are \(D_k=4\pi^2c_{d,s}|k|^{s+2-d}>0\). This verifies the normalization and the endpoint compensation rather than replacing (5) with a punctured classical Laplacian.

For clarity, the precise R6 path premise used here has the following mechanism. The nonnegative shifted energy

\[
 \mathcal H_N=H_N-(N-1)g_*/2,\quad
 H_N=N^{-1}\sum_{i<\ell}g(x_i-x_\ell),\quad B=-\nabla H_N,\quad
 \Delta_{Nd}H_N=\frac2N\sum_{i<\ell}\Delta g\le(N-1)\kappa
 \tag{6}
\]

has compact collision-excluded sublevels, including every partial or simultaneous collision. Smooth local force cutoffs, Picard iteration after subtracting additive noise, and patching give a measurable pathwise-unique local solution. Smooth Itô calculus stopped at level \(R\) gives drift \(-|B|^2+\nu\Delta H_N\), a true stopped martingale, and

\[
 \mathbb P_x(\tau_R\le T)\le
 [\mathcal H_N(x)+\nu(N-1)\kappa T]/R.
 \tag{7}
\]

The complete drift square is retained. A bounded-energy path extends in a collision-excluded compact set. Hence (7) proves global noncollision for each fixed start, almost surely. Joint measurability permits integration against iid Haar, whose initial shifted-energy mean is \(-(N-1)g_*/2<\infty\). Each realized continuous path has positive minimum separation on this finite horizon. No common exceptional set over all starts, or uniform-in-\(N\) separation, is used.

Heat convolution \(K_\varepsilon=p_\varepsilon*K\) converges in local \(C^1\) away from zero, by splitting a smooth local part and a distant \(L^1\) part with Gaussian tail bounds. The same-noise heat and singular paths have cancelling additive noise. Gronwall, stopped before their difference reaches a quarter of the singular path's minimum separation, proves uniform-time convergence at each fixed \(N,\nu,T\). No uniform heat rate is needed or inferred.

The R10/R16 actual energy argument is essential; product Haar at positive times is not assumed. At fixed heat cutoff and positive noise, the smooth positive bounded density from initial density one satisfies the classical Fokker–Planck equation. Smooth periodic integration by parts gives

\[
 \frac d{dt}\left(\nu\int F_t^\varepsilon\log F_t^\varepsilon
             +\int H_N^\varepsilon F_t^\varepsilon\right)
 =-\int F_t^\varepsilon|\nabla H_N^\varepsilon+
                  \nu\nabla\log F_t^\varepsilon|^2\le0.
 \tag{8}
\]

Both initial quantities are zero and entropy is nonnegative on the mass-one space. Heat positivity preserves the fixed-\(N\) lower energy bound. Fixed-\(N\) path convergence, local uniform kernel convergence and Fatou after this common lower shift give \(\mathbb EH_N(X_t)\le0\). At zero noise use the actual deterministic identity \(dH_N/dt=-|B|^2\le0\) and integrable iid initial energy. Permutation equivariance yields exchangeability, whence

\[
 \mathbb E g(X_1-X_2)\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|,\qquad
 \mathbb E(1+\operatorname{dist}(X_1-X_2,0)^{-s})\le C.
 \tag{9}
\]

The constants in (9) are uniform in all the parameters indicated in Section 1. No singular Fisher-information passage or individual pair-force-square estimate occurs.

Common translation of every initial coordinate translates the full path under the same Brownian increments, by pathwise uniqueness and the difference form of the force. Initial iid Haar is invariant under this operation. Each one-body marginal is translation invariant, so every nonzero Fourier coefficient is zero; trigonometric-polynomial density identifies the marginal with Haar. Consequently

\[
 \mathbb E\eta_N(r)[h]=\int h\,dx
 \tag{10}
\]

for every deterministic \(r\) and every bounded Borel \(h\). This is exact Haar centering, with no correction and no positive-time product-law assertion.

## 3. A common source envelope, rather than a fixed-terminal-time bound

This is the additional implication extracted from the complete R16 proof. It is not implied merely by the THM038 card's fixed-test constant. Put \(M=d+2\), and, for \(0<\ell\le2\), define

\[
 w_\ell(u)=(1-e^{-u/\ell})^M,\quad\psi_\ell=1-w_\ell,
\]
\[
 g_\ell=A\int_0^\infty u^{\alpha-1}w_\ell(u)(p_u-1)\,du,\quad
 Q_\ell=A\int_0^\infty u^{\alpha-1}\psi_\ell(u)p_u\,du\ge0,\quad
 c_\ell=\int Q_\ell=C_{d,s,M}\ell^\alpha.
 \tag{11}
\]

Here \(Q_\ell\) is a positive kernel, not the one-body semigroup used later. No value of \(Q_\ell\) on the singular diagonal is assigned. Its use below is always off-diagonal. The retained \(g_\ell\) is \(C^2\), has positive nonzero Fourier coefficients

\[
 a_\ell(k)=A\int_0^\infty u^{\alpha-1}w_\ell(u)e^{-4\pi^2|k|^2u}\,du,
 \quad 0\le g_\ell(0)\le C\ell^{-s/2},\quad g=g_\ell+Q_\ell-c_\ell.
 \tag{12}
\]

The \(C^2\) and diagonal bounds follow by integrating the heat bounds using \(w_\ell(u)\le\min(1,(u/\ell)^M)\) and \(M>(s+2)/2\). Define nonnegative configuration quantities

\[
 E_\ell(x)=\frac12\sum_{k\ne0}a_\ell(k)|\widehat\eta_N(k)|^2,\qquad
 S_\ell(x)=\frac1{2N^2}\sum_{i\ne j}Q_\ell(x_i-x_j).
\]

The exact deleted-pair splitting, with both self and background subtractions, is

\[
 H_N/N=E_\ell+S_\ell-\frac{g_\ell(0)}{2N}
                      -\frac{N-1}{2N}c_\ell.
 \tag{13}
\]

Equation (9) justifies expectation of (13); its two positive quantities yield

\[
 \mathbb EE_\ell(X_r)+\mathbb ES_\ell(X_r)
 \le C(N^{-1}\ell^{-s/2}+\ell^\alpha),\quad 0<\ell\le2.
 \tag{14}
\]

For any smooth real vector field \(v\), write \(J_g[v](x,y)=K(x-y)\cdot(v(x)-v(y))\) off the diagonal, with exactly

\[
 P_N[J]=\frac1{2N^2}\sum_{i\ne j}J(X_i,X_j)
              -\eta_N\left[\int J(\,\cdot,y)\,dy\right]
              +\frac12\iint J(x,y)\,dx\,dy.
 \tag{15}
\]

The deterministic retained-kernel estimate in R16 has a scale-independent constant. To check its dependence, radial differentiation of \(a_\ell\), using \(0\le u w'_\ell\le Mw_\ell\) and integrating the derivative of \(u^\alpha w_\ell(u)e^{-\lambda u}\), gives

\[
 0\le-\xi a'_\ell(\xi)/a_\ell(\xi)\le L:=2(\alpha+M).
\]

For \(k,l\ne0\), the logarithmic bound, \(\min(|k|,|l|)\ge1\), and the mean-value estimate imply

\[
 \frac{|k a_\ell(k)-l a_\ell(l)|}
      {\sqrt{a_\ell(k)a_\ell(l)}}
 \le(1+L)|k-l|(1+|k-l|)^{L/2+1}.
 \tag{16}
\]

The smooth retained diagonal is zero, so (15) equals the centered full product only for that retained kernel. Symmetrizing its absolutely convergent Fourier series and applying Cauchy–Schwarz to each frequency difference gives

\[
 |P_N[J_{g_\ell}[v]]|
 \le2\pi(1+L)\left(\sum_q|q|(1+|q|)^{L/2+1}|\widehat v(q)|\right)E_\ell.
 \tag{17}
\]

For the singular remainder \(R_\ell=g-g_\ell\), the differentiated periodized Gaussian satisfies

\[
 \operatorname{dist}(z,0)|\nabla p_u(z)|\le C_dp_{2u}(z).
\]

Use \(\operatorname{dist}(z,0)\le|z+n|\) for each Gaussian translate and bound \(y e^{-y}\). Integration along a shortest torus geodesic gives \(|v(x)-v(y)|\le\|Dv\|_\infty\operatorname{dist}(x,y)\). Substitution \(a=2u\), for which \(\psi_\ell(a/2)=\psi_{2\ell}(a)\), therefore proves

\[
 |J_{R_\ell}[v](x,y)|\le C\|Dv\|_\infty Q_{2\ell}(x-y).
\]

Keeping all three coefficients in (15), its deleted sum, row contraction and double contraction respectively contribute \(S_{2\ell},c_{2\ell},c_{2\ell}/2\). Thus the following holds pointwise at every collision-free configuration, for \(0<\ell\le1\):

\[
 |P_N[J_g[v]]|
 \le C\left(\|Dv\|_\infty+
       \sum_q|q|(1+|q|)^{\alpha+M+1}|\widehat v(q)|\right)
          [E_\ell+S_{2\ell}+c_{2\ell}].
 \tag{18}
\]

This uses positive domination of an absolute value, not false positivity of a weighted Riesz kernel. The full double contraction is actually zero by oddness; its original term remains visible in the estimate.

For \(a\in[0,T]\), define the one-body Fourier semigroup \(\mathcal Q_a^\nu\) to preserve constants and multiply mode \(k\ne0\) by \(e^{-a L_k^\nu}\), where

\[
 a_k=4\pi^2|k|^2,\qquad L_k^\nu=D_k+\nu a_k>0.
 \tag{19}
\]

For \(\|f\|_{\mathcal A_p}=\sum_k(1+|k|)^p|\widehat f(k)|\), its multipliers have modulus at most one. Smooth tests have finite seminorms of every finite order, and \(L_k^\nu\le C(1+|k|)^2\) for the bounded noise range. Hence all needed spatial derivatives and one time derivative are bounded uniformly in \(a,\nu\). In particular the coefficient in (18), with \(v=\nabla\mathcal Q_a^\nu h_j\), is at most a fixed \(C_{h_j}\), controlled by \(\|h_j\|_{\mathcal A_{\alpha+M+3}}\).

Choose \(\ell_N=N^{-2/d}\), and set

\[
 \Lambda_N(r)=E_{\ell_N}(X_r)+S_{2\ell_N}(X_r)+c_{2\ell_N}\ge0,\qquad
 q=1-s/d>0.
\]

Equations (14) and (18) now give the genuinely common envelope

\[
 \sup_{0\le a\le T}|P_N[J_g[\nabla\mathcal Q_a^{\nu_N}h_j]](X_r)|
 \le C_{h_j}\Lambda_N(r),\qquad
 \sup_{0\le r\le T}\mathbb E\Lambda_N(r)\le CN^{-q}.
 \tag{20}
\]

The supremum is bounded pathwise before expectation. Joint measurability follows from the measurable paths and smooth/off-diagonal integrands; (20) and Tonelli make \(\int_0^T\Lambda_N(r)dr\) finite almost surely and integrable. This is the step that a deterministic-terminal-time \(L^1\) bound alone would not justify.

## 4. Singular path identity and supremum remainder

The response is \(\mathcal R f(x)=-\int f(x+w)D(dw)\), with multiplier \(-D_k\). Direct integration of the genuine source, using \(K\in L^1\), gives

\[
 j_f(x):=\int J_g[\nabla f](x,y)dy
 =-\int K(x-y)\cdot\nabla f(y)dy
 =\mathcal Rf(x),\qquad\int j_f=\iint J_g[\nabla f]=0.
 \tag{21}
\]

The distributional integration by parts in (21) uses all of (5); at Coulomb it is \(-c_d(f-\mu[f])\). It is not a singular empirical diagonal trace. For terminal \(t\in[0,T]\), let \(f_r^{t}=\mathcal Q_{t-r}^{\nu_N}h\) for \(0\le r\le t\). Then

\[
 \partial_r f_r^t+\nu_N\Delta f_r^t+\mathcal Rf_r^t=0,\qquad
 \mu[f_r^t]=\mu[h].
\]

Apply time-dependent smooth Itô calculus to \(\eta_N(r)[f_r^t]\), stopped in collision-excluded compacts. Oddness gives the exact interaction coefficient

\[
 \frac1{N^2}\sum_{i\ne l}K(X_i-X_l)\cdot\nabla f(X_i)
 =\frac1{2N^2}\sum_{i\ne l}J_g[\nabla f](X_i,X_l)
 =P_N[J_g[\nabla f]]+\eta_N[\mathcal Rf].
 \tag{22}
\]

The Itô correction is \(\nu_N\eta_N[\Delta f]\). Different particle Brownian motions have zero cross variation. There is no force self term. Equation (21) accounts for the entire background. The backward equation cancels the linear drift.

For the stopped-to-actual passage, \(|J_g[\nabla f](x,y)|\le C(1+\operatorname{dist}(x,y)^{-s})\), uniformly for this family. Equation (9) gives an integrable probability-time majorant at fixed \(N\); rows and time derivatives are bounded. Dominated convergence passes drift and endpoint terms. The stochastic gradients are bounded, so the Itô isometry passes the stochastic integrals in \(L^2\). Noncollision removes all stops. Thus the identity is genuine, with no singular pair Itô formula.

For each component it reads

\[
 Z_{N,j}(t)=I_{N,j}(t)+M_{N,j}(t)+R_{N,j}(t),
 \tag{23}
\]
\[
 I_{N,j}(t)=\sqrt{b_N/N}\sum_i
     (\mathcal Q_t^{\nu_N}h_j(X_i(0))-\mu[h_j]),
\]
\[
 M_{N,j}(t)=\sqrt{2\nu_Nb_N/N}\sum_i\int_0^t
    \nabla\mathcal Q_{t-r}^{\nu_N}h_j(X_i(r))\cdot dW_i(r),
\]
\[
 R_{N,j}(t)=\sigma_N\int_0^t
      P_N[J_g[\nabla\mathcal Q_{t-r}^{\nu_N}h_j]](X_r)dr.
 \tag{24}
\]

The stochastic convolution is generally not a martingale in terminal \(t\). All martingale arguments below use its integration variable \(r\), with fixed terminal tests.

The actual \(Z_N\), the initial term, and the remainder are continuous paths: for the latter, on each realized compact horizon the pair distances have a positive minimum and the deterministic test family is smooth on the time triangle. The fixed-terminal identity holds simultaneously on a countable dense time set. Defining the continuous version \(M_N=Z_N-I_N-R_N\) gives a continuous version of the displayed convolution at every fixed time, because the same Itô identity also holds at that fixed time. This establishes a single path identity without intersecting uncountably many null sets.

Crucially, (20) proves

\[
 \mathbb E\|R_N\|_\infty
 \le C\sigma_N\mathbb E\int_0^T\Lambda_N(r)dr
 \le C\sqrt{b_N}\,N^{s/d-1/2}\longrightarrow0.
 \tag{25}
\]

This is an actual uniform-path \(L^1\) estimate. It is not an expectation of a pointwise source mean, nor an exchange of supremum and expectation.

## 5. Fourth moments for the initial term and stochastic convolution

Let \(0\le u\le t\le T\), \(\delta=t-u\). The Fourier bounds after (19) give

\[
 \|\mathcal Q_t^\nu h-\mathcal Q_u^\nu h\|_\infty\le C\delta,\quad
 \|\nabla\mathcal Q_a^\nu h\|_\infty\le C,\quad
 \|\nabla(\mathcal Q_{a+\delta}^\nu-\mathcal Q_a^\nu)h\|_\infty\le C\delta
 \tag{26}
\]

whenever the time arguments lie in \([0,T]\). The initial summands for an increment have mean zero and magnitude at most \(C\delta\). Independence at time zero gives the exact scalar fourth moment

\[
 \mathbb E|I_{N,j}(t)-I_{N,j}(u)|^4
 =b_N^2\left[N^{-1}\mathbb E\xi^4
       +3(1-N^{-1})(\mathbb E\xi^2)^2\right]\le C\delta^4.
 \tag{27}
\]

Likewise \(\sup_N\mathbb E|I_N(0)|^4<\infty\). The vector estimates follow from \(|x|^4\le m\sum_j|x_j|^4\).

For \(M_{N,j}(t)-M_{N,j}(u)\), keep both intervals: on \([0,u]\) its integrand is the gradient of \((\mathcal Q_{t-r}^{\nu_N}-\mathcal Q_{u-r}^{\nu_N})h_j\); on \((u,t]\) it is \(\nabla\mathcal Q_{t-r}^{\nu_N}h_j\). Regard this sum as the terminal value of a scalar martingale in \(r\in[0,t]\). Its bracket density is at most

\[
 \beta_{t,u}(r)=C\delta^2\mathbf1_{[0,u]}(r)+C\mathbf1_{(u,t]}(r),\qquad
 \int_0^t\beta_{t,u}\le C_T\delta,
 \tag{28}
\]

since \(2\nu_Nb_N\eta_N[|v|^2]\le2\|v\|_\infty^2\). The \(1/N\) in the scaled bracket cancels the sum over all \(N\) Brownian drivers; no deleted-label \(N-1\) enters.

Here is the needed moment lemma without a named martingale inequality. If a real continuous stochastic integral \(U\), starting at zero, satisfies \(d\langle U\rangle_r\le\beta(r)dr\) for deterministic integrable \(\beta\), stop at bounded \(|U|\). Itô's formula gives \(\mathbb E U_{r\wedge\tau}^2\le\int_0^r\beta\) and

\[
 \mathbb E U_{t\wedge\tau}^4
 =6\mathbb E\int_0^t\mathbf1_{r\le\tau}U_r^2\,d\langle U\rangle_r
 \le6\int_0^t\beta(r)\int_0^r\beta(a)da\,dr
 =3\left(\int_0^t\beta\right)^2.
\]

The stopped stochastic terms have mean zero; one may first stop their brackets as well. Fatou removes the stops and proves the bound for \(U_t\). Applying it to (28) gives

\[
 \mathbb E|M_N(t)-M_N(u)|^4\le C\delta^2.
 \tag{29}
\]

Consequently the continuous process \(Y_N=I_N+M_N\) satisfies

\[
 \sup_N\mathbb E|Y_N(0)|^4\le C,\qquad
 \mathbb E|Y_N(t)-Y_N(u)|^4\le C|t-u|^2.
 \tag{30}
\]

These moments are uniform over the admitted bounded noise sequence. In particular no fourth moment of a singular source or a singular pair force was assumed.

## 6. Full tightness in the uniform topology

Assume \(T>0\). Fix any \(0<\gamma<1/4\), for example \(\gamma=1/8\). On the dyadic grid \(t_{n,l}=Tl2^{-n}\), (30), Markov's inequality and the union over the \(2^n\) adjacent increments give

\[
 \sup_N\mathbb P\left(\max_{1\le l\le2^n}
    |Y_N(t_{n,l})-Y_N(t_{n,l-1})|>A2^{-\gamma n}\right)
 \le C_T A^{-4}2^{-(1-4\gamma)n}.
 \tag{31}
\]

The exponent includes the grid-cardinality loss. Its sum over all \(n\ge0\) is finite. On the complement of these events, every dyadic increment is bounded by \(A2^{-\gamma n}\). Approximate any time from below by dyadic grid points: consecutive refinements differ by either zero or one edge, so the tail distance is at most \(A\sum_{l>n}2^{-\gamma l}\). For two points with separation at most \(T2^{-n}\), their level-\(n\) lower approximants are separated by at most one edge. Adding the two tails proves a bound \(C_\gamma A2^{-\gamma n}\). Continuity extends this bound from dyadic points to all points. Choosing \(n\) comparable to the separation gives a common Hölder modulus \(C_{\gamma,T}A|t-u|^\gamma\).

Together with \(\mathbb P(|Y_N(0)|>B)\le CB^{-4}\), this places all \(Y_N\) with probability at least \(1-CB^{-4}-C_TA^{-4}\) in a common closed bounded Hölder ball. That ball is compact in the uniform norm: diagonal subsequence extraction on a countable dense time set gives convergence there, while its common modulus promotes the subsequence to uniform Cauchy convergence and a continuous limit with the same bounds. This proves tightness of the entire family of \(Y_N\) laws.

The transfer to \(Z_N\) needs care: a fixed-radius neighborhood of a compact set need not be compact in this space. Write \(w_\delta(z)=\sup_{|t-u|\le\delta}|z(t)-z(u)|\). From (23),

\[
 w_\delta(Z_N)\le w_\delta(Y_N)+2\|R_N\|_\infty.
 \tag{32}
\]

Equation (25) first gives \(\lim_{\delta\downarrow0}\limsup_{N\to\infty}\mathbb P(w_\delta(Z_N)>a)=0\) for each \(a>0\). To obtain actual tightness of the whole family, fix \(a_l\downarrow0\) and summable positive \(\varepsilon_l\). Choose \(N_l\) so that \(\mathbb P(2\|R_N\|_\infty>a_l/2)<\varepsilon_l\) for every \(N\ge N_l\). The uniform modulus for \(Y_N\) permits a small \(\delta_l\) with \(\sup_N\mathbb P(w_{\delta_l}(Y_N)>a_l/2)<\varepsilon_l\). For the finitely many \(N<N_l\), actual path continuity gives \(w_\delta(Z_N)\to0\) almost surely; bounded convergence of the event indicators permits reducing \(\delta_l\) further so that each such probability is below \(2\varepsilon_l\). Also enforce \(\delta_l\downarrow0\). Thus

\[
 \sup_N\mathbb P(w_{\delta_l}(Z_N)>a_l)\le2\varepsilon_l.
\]

The initial vectors are tight by (27), since \(Z_N(0)=I_N(0)\). The closed set \(\{|z(0)|\le B,\ w_{\delta_l}(z)\le a_l\text{ for all }l\}\) is equicontinuous and bounded (chain intervals of length \(\delta_1\) from time zero), hence compact by the argument just given. A union bound gives mass at least \(1-CB^{-4}-2\sum_l\varepsilon_l\), uniformly in \(N\). These choices make the loss arbitrarily small. This proves full uniform-topology tightness of the actual path laws, not merely a subsequence proxy or a finite-dimensional bound.

## 7. Existence of the continuous Gaussian process

Use real separable Hilbert spaces \(H_0=L^2_0(\mathbb T^d;\mathbb R)\) and \(H_1=L^2([0,T]\times\mathbb T^d;\mathbb R^d)\). On an auxiliary probability space take two independent sequences of independent standard real Gaussians. For a countable orthonormal basis of each space, the series of coefficients times these Gaussians converges in \(L^2\); this defines independent isonormal Gaussian maps \(W_0,W_1\). Finite linear combinations have the Gaussian characteristic function obtained from the product of the one-dimensional ones; \(L^2\) convergence preserves that function. Let \(\mathcal Q=\mathcal Q^{\bar\nu}\), and prescribe at each fixed time

\[
 Z_j(t)=\sqrt{\bar b}\,W_0(\mathcal Q_t h_j-\mu[h_j])
   +\sqrt{2\bar\nu\bar b}\,W_1
       (\mathbf1_{[0,t]}(r)\nabla\mathcal Q_{t-r}h_j(x)).
 \tag{33}
\]

Initially do this on all dyadic times, a countable set. The deterministic profile estimates (26) give variance of each increment at most \(C|t-u|\); a centered real Gaussian of variance \(v\) has fourth moment \(3v^2\), by the elementary Gaussian integral. Vector fourth moments are therefore bounded by \(C|t-u|^2\). Equation (31) and summability now apply to this countable Gaussian process. The probability of infinitely many level violations is zero, since the probability of their union after level \(n\) tends to zero. Early finitely many levels have finite increments, so almost surely a finite random \(A\) bounds every level. The dyadic chaining proof then gives a unique continuous extension to \([0,T]\).

The Hilbert profiles in (33) are \(L^2\)-continuous in \(t\). For any specified real time, their dyadic approximants converge in \(L^2\), hence in probability, to the Gaussian variable in (33). The continuous extension is their almost-sure limit, so the two variables agree almost surely at that time. This proves that the continuous version has all the prescribed joint Gaussian laws and covariance, with no unproved uncountable modification step. Rational evaluations make it a Borel random element of continuous path space. At zero limiting noise, the second term is defined to be zero; it requires no division by noise.

Its covariance is the manifestly positive semidefinite Gram expression

\[
 C_{ij}(t,u)=\bar b\int(\mathcal Q_t h_i-\mu[h_i])
                    (\mathcal Q_u h_j-\mu[h_j])dx
 +2\bar\nu\bar b\int_0^{t\wedge u}\int
         \nabla\mathcal Q_{t-r}h_i\cdot\nabla\mathcal Q_{u-r}h_j\,dx\,dr.
 \tag{34}
\]

No inverse covariance, nondegeneracy or density is required.

## 8. Actual finite-dimensional identification, including initial dependence

The complete earlier R18 implication is available conditionally, but the required probability argument is recorded here to specify exactly what is used. Choose any finite list of deterministic times and any tests from the fixed list, allowing repetitions. Their decomposition is (23). For a real coefficient vector \(v\), the corresponding terminal stochastic sum is the terminal value of the genuine martingale in integration time with deterministic test profile

\[
 G_{N,v}(r,x)=\sum_l v_l\mathbf1_{r\le t_l}\nabla\mathcal Q_{t_l-r}^{\nu_N}h_{j_l}(x).
\]

Its bracket is exactly

\[
 V_N=2\nu_Nb_N\int_0^T\eta_N(r)[|G_{N,v}(r)|^2]dr\le K_v,
 \tag{35}
\]

where \(K_v\) is deterministic, independent of \(N\). In particular the cross bracket before taking this linear combination is

\[
 2\nu_Nb_N\int_0^{t_l\wedge t_p}\eta_N(r)
 [\nabla\mathcal Q_{t_l-r}^{\nu_N}h_{j_l}\cdot
  \nabla\mathcal Q_{t_p-r}^{\nu_N}h_{j_p}]dr.
\]

Haar centering gives its mean, but concentration requires the actual R10 Fourier bound. Its proof uses the positive heat-integral truncation \(g^{>a}=A\int_a^\infty u^{\alpha-1}(p_u-1)du\), distinct from (11). Exact self subtraction and \(g\ge g^{>a}-Aa^\alpha/\alpha\) give

\[
 H_N\ge\frac N2\sum_{k\ne0}a^{>a}(k)|\widehat\eta_N(k)|^2
           -\frac12g^{>a}(0)-\frac{N-1}{2\alpha}Aa^\alpha.
\]

At \(a=N^{-2/d}\), \(g^{>a}(0)\le Ca^{-s/2}\) and (9) control the expectation of the positive sum. Integrating its coefficient over \([|k|^{-2},2|k|^{-2}]\) for \(|k|\le N^{1/d}\), and using \(|\widehat\eta_N(k)|\le1\) for the rest, proves

\[
 \mathbb E|\widehat\eta_N(r,k)|^2\le\min(1,CN^{-q}|k|^{d-s}),\quad
 \mathbb E|\rho_N(r)[\varphi]|\le CN^{-q/2}
       \sum_{k\ne0}|k|^{(d-s)/2}|\widehat\varphi(k)|.
 \tag{36}
\]

The latter follows by absolute Fourier summation and Cauchy–Schwarz in probability. It applies uniformly to smooth deterministic families with the displayed seminorm bounded. Such a bound holds for all products of gradients in (35): weighted Fourier convolution gives \(\|vw\|_{\mathcal A_p}\le\|v\|_{\mathcal A_p}\|w\|_{\mathcal A_p}\), and (19) bounds each factor. Thus \(V_N\) differs in \(L^1\), by at most \(CN^{-q/2}\), from the Haar bracket.

Put \(\delta_N=|\nu_N-\bar\nu|\). Direct differentiation of the exponential multiplier gives

\[
 \|(\mathcal Q_a^{\nu_N}-\mathcal Q_a^{\bar\nu})h\|_{\mathcal A_p}
 \le4\pi^2T\delta_N\|h\|_{\mathcal A_{p+2}},\quad
 |\sqrt{b_N}-\sqrt{\bar b}|\le\delta_N/2,\quad
 |\nu_Nb_N-\bar\nu\bar b|\le\delta_N.
\]

Hence \(\mathbb E|V_N-V|\le C_v(N^{-q/2}+\delta_N)\to0\), where \(V\) is the deterministic thermal Gram quadratic form of (34).

The initial triangular test differs from the limiting test by a mean-zero function with \(L^2\) norm \(O(\delta_N)\). Initial iid preparation gives exactly the squared \(L^2\) norm as the variance of its \(N^{-1/2}\)-sum; there is no \(\sqrt N\delta_N\) loss. For the fixed limiting initial test \(\zeta\), mean zero and bounded, Taylor's formula gives

\[
 \mathbb E e^{i\zeta(X_1)/\sqrt N}
 =1-\mathbb E\zeta^2/(2N)+O(N^{-3/2}),
\]

and its \(N\)-th power tends to the characteristic function of the initial Gaussian Gram form.

Initial and terminal martingale terms are not assumed independent at finite \(N\). If \(U_N\) denotes this scalar terminal martingale, smooth Itô calculus shows that \(\exp(iU_N(r)+\langle U_N\rangle_r/2)\) is a true complex martingale: its positive compensator cancels the second derivative drift, and its modulus is at most \(e^{K_v/2}\). Its stochastic-integral second moment is bounded by \(e^{K_v}K_v\). Conditional expectation at time zero is consequently one. For every time-zero measurable \(|A_N|\le1\), bounded-bracket replacement yields

\[
 \left|\mathbb E[A_Ne^{iU_N(T)}]-e^{-V/2}\mathbb EA_N\right|
 \le\tfrac12e^{K_v/2}\mathbb E|V_N-V|\longrightarrow0.
 \tag{37}
\]

Take \(A_N\) to be the initial characteristic factor. Equations (25) and (37) give the joint characteristic function of (34), for every finite list. To specify the finite-dimensional weak passage: \(I_N+M_N\) has uniformly bounded second moment. Add an independent Gaussian of variance \(\varepsilon I\) to these finite-dimensional vectors. Gaussian Fourier inversion and dominated convergence give uniform convergence of their convolved densities; second-moment tails reduce bounded Lipschitz expectations to a compact ball. Coupling removes the added Gaussian with error \(O(\sqrt\varepsilon)\). Let \(\varepsilon\downarrow0\). The source error (25) transfers bounded Lipschitz expectations and tightness. Uniform approximation on compact balls then gives convergence for bounded continuous tests. This argument covers singular covariance as well as positive covariance.

## 9. Full weak convergence of path laws

Let \(\Pi_nz\) be piecewise linear interpolation of the values of \(z\) on the dyadic grid of mesh \(T2^{-n}\). It is a continuous map from that finite-dimensional vector to \(C([0,T],\mathbb R^m)\), and

\[
 \|z-\Pi_nz\|_\infty\le w_{T2^{-n}}(z).
 \tag{38}
\]

For any bounded Lipschitz real functional \(F\) on this path space, normalize its supremum norm and Lipschitz constant to at most one. The difference between its expectation on \(z\) and on \(\Pi_nz\) is at most \(\eta+2\mathbb P(w_{T2^{-n}}(z)>\eta)\). The uniform modulus proved in Section 6 makes this small uniformly for the actual \(Z_N\); path continuity and bounded convergence do so for \(Z\). At fixed \(n\), Section 8 identifies the finite-dimensional grid law, hence the limit of \(\mathbb EF(\Pi_nZ_N)\). Let first \(N\to\infty\), then \(n\to\infty\), then \(\eta\downarrow0\). This proves convergence of all bounded Lipschitz expectations to the law constructed in Section 7.

To obtain the usual weak convergence for every bounded continuous \(F\), use Section 6's compact set with uniformly small missing mass, and the analogous compact Hölder set from Section 7 for \(Z\). Their union is compact. On it, \(F\) is uniformly continuous and can be uniformly approximated by a bounded Lipschitz function on the full metric space: choose a sufficiently fine finite net and use minima of finitely many distance cones \(F(x_i)+L\|x-x_i\|_\infty\), clipped at a bound for \(F\). With \(L\) large, points farther than the uniform-continuity radius cannot minimize below the target, and a finer net bounds the error above. This proves the approximation directly. The complement costs only its small probability times the uniform bound. Thus the Lipschitz convergence extends to every bounded continuous \(F\).

This is convergence of the entire sequence in the uniform topology. It explicitly identifies the actual weak limit; no merely formal covariance argument, unproved subsequence compactness invocation or finite-dimensional-to-path jump remains.

## 10. Exact covariance and limiting-law scope

Both sums and the time integral in (34) are absolutely summable by smoothness. With \(L_k=D_k+\bar\nu a_k>0\),

\[
 \int_0^{t\wedge u}e^{-(t+u-2r)L_k}dr
 =\frac{e^{-|t-u|L_k}-e^{-(t+u)L_k}}{2L_k}.
\]

Parseval in (34) therefore gives exactly

\[
 \boxed{\mathbb EZ_i(t)Z_j(u)=\bar b\sum_{k\ne0}
  \widehat h_i(k)\overline{\widehat h_j(k)}
  \left[\frac{D_k}{L_k}e^{-(t+u)L_k}
       +\frac{\bar\nu a_k}{L_k}e^{-|t-u|L_k}\right].}
 \tag{39}
\]

For real tests opposite modes pair into a real quantity; covariance symmetry is also explicit in the Gram expression. The sum of the observation times belongs to the decaying initial component; the difference belongs to the thermal component. The exact Brownian factor two is necessary for the coefficients \(D_k/L_k\) and \(\bar\nu a_k/L_k\).

The topology concerns fixed smooth observables only. There is no distribution-valued field statement, growing test family, unbounded-noise path approximation, higher exponent, logarithmic substitution, general background, arbitrary preparation, higher-corrector closure or full hierarchy assertion. The old energy-floor condition, full microscopically subcritical condition and positive finite microscopic critical condition remain distinct. Nothing in this reconstruction promotes the flagship mission beyond this frozen homogeneous row.

## 11. Independent falsification route and newly authored diagnostics

The construction above starts with a deterministic positive source envelope and ends with dyadic compactness. The falsification route instead attacks path-level inference and modal time dependence before consulting any tightness conclusion.

First, let \(T=1\), let \(U\) be uniform on \([1/4,3/4]\), and for integer \(n\ge8\) put \(r_n(t)=(1-n|t-U|)_+\). These continuous paths have \(\sup_t r_n(t)=1\) surely, while \(\sup_t\mathbb Er_n(t)\le2/n\to0\), since the triangular area is \(1/n\) and the density of \(U\) is two. Every fixed finite vector converges to zero in probability by Markov and a finite union. Nevertheless \(\|r_n\|_\infty=1\); these laws cannot be tight with those finite-dimensional limits. More directly their modulus over distance \(1/n\) is at least one. This is an exact counterexample to the proposed shortcut, not to the admitted particle theorem. It forces the common envelope (20), and catches exchanging \(\mathbb E\sup\) with \(\sup\mathbb E\).

Second, solve one real Gaussian mode directly with positive symbolic damping \(L=D+c\), initial variance \(b\), and thermal variance density \(2bc\), where \(c=\nu a\ge0\). Independent increments give

\[
 V(u)=b e^{-2Lu}+\frac{bc}{L}(1-e^{-2Lu}),\qquad
 C(t,u)=e^{-L(t-u)}V(u),\quad t\ge u.
\]

Its increment variance is the sum of three independently identifiable contributions: the initial difference; past thermal noise multiplied by \(e^{-L(t-u)}-1\); and fresh noise over \((u,t]\). Omitting the past-noise contribution is false when \(u>0,c>0,t>u\). Treating the stochastic convolution as a martingale in terminal time is likewise false. Expanding the exact variance at \(t=u+\delta\) gives first-order coefficient \(2bc\delta\), which directly detects a missing Brownian factor two. At \(c=0\) this coefficient vanishes and the leading increment variance is quadratic, consistent with (33). These checks arise from an independent solvable-mode construction, not from replacing a random actual bracket by its mean.

The new standard-library diagnostic in the packet uses exact rational arithmetic and formal finite exponential sums. It verifies this three-part modal increment identity against independently propagated covariance; the initial, zero-noise and constant/linear-dependence cases; literal ordered-label source coefficients in a smooth trigonometric \(N=2,3\) model; the random-tent area/supremum obstruction; and the dyadic union exponent. It rejects deliberately wrong source halves, missing thermal factors, omitted past increments, false terminal martingales, wrong sum/difference exponents, invalid supremum exchange and invalid Hölder exponents. Physical normalization is established analytically in (4)–(5); the toy trigonometric test is expressly an algebraic regularized diagnostic, not a Riesz-law certification. No prior program, test result, external package, floating-point tolerance or random sample is used. Exact counts, mutation witnesses and the code digest are in its newly generated result file.

Executed outcome: **2,508 exact assertions passed; all 13 deliberate mutations were rejected.** The result was generated once by the new program and subsequently recomputed without writing. A report-format check also verified sequential equation tags 1–39 and balanced display/inline mathematical delimiters. These are supporting checks, not mathematical certification.

## 12. Every stated edge case

* **\(T=0\).** The path space is isometric to \(\mathbb R^m\). The source and stochastic integrals are zero, and the ordinary bounded iid characteristic expansion in Section 8 gives covariance \(\bar b\operatorname{Cov}_{dx}(h_i,h_j)\). No division by \(T\) or dyadic construction is used.
* **Any finite positive \(T\).** Constants may depend on it. No claim uniform as \(T\to\infty\) is made.
* **Zero finite noise.** For every \(N\) with \(\nu_N=0\), the actual flow is the deterministic noncolliding flow, \(b_N=1\), the martingale term is zero and the energy argument uses deterministic decrease. Mixed sequences containing zero terms are allowed.
* **\(\bar\nu=0\), including \(\nu_*=0\).** The thermal term of (33) and (39) is exactly zero, \(\bar b=1\), and \(L_k=D_k\). No finite-order critical ansatz or positive lower bound on noise is imposed.
* **Positive limiting noise, including the kink at one.** The thermal Gram term remains. The elementary Lipschitz estimates for \(\sqrt b\) and \(\nu b\) are valid across one. No convergence rate of noise is used.
* **Constant tests.** Their source, response, gradient, initial centered term and actual path fluctuation all vanish exactly. The zero Fourier mode is omitted only after its exact cancellation.
* **Linearly dependent tests and degenerate covariance.** If a real linear combination of the tests is constant, that combination of the actual paths and of the limiting process is zero at every time. More general finite-dimensional degeneracy is permitted by the Gram construction; a combination has zero variance precisely when its initial Hilbert profile and its positive-noise thermal profile vanish. No inverse covariance or density is used anywhere.
* **Zero/repeated observation times and repeated tests.** They are included in the finite-dimensional argument and in (34)–(39). Source/noise integrals for a zero time are zero. Cross brackets use the exact minimum time.
* **Coulomb.** The allowed joint restrictions imply that the positive Coulomb endpoint under \(s<d/2\) occurs in dimension three. Its divergence atom and Haar compensation remain in (5) and (21); no classical punctured replacement occurs in a convolution or background identity.

## 13. Adversarial self-review and per-claim dispositions

| Claim/challenge | Disposition and precise reason |
|---|---|
| Exact assertion and negation, unchanged range | RECONSTRUCTED as stated in Section 1; no card repair. |
| Coefficient-one kernel and endpoint compensation | CHECKED from the supplied heat representation and flux/gamma calculation (4)–(5); earlier source status retained. |
| Actual paths and singular one-body identity | CONDITIONAL ON COMPLETE R6; its exact stopped mechanism and fixed-\(N\) heat passage are mapped in Section 2; the needed singular identity is rederived in Section 4. |
| Actual energy/Fourier inputs | CONDITIONAL ON COMPLETE R10/R16; signs, self terms, zero-noise use and uniform constants are checked in (8)–(14), (36). |
| A THM038 fixed-terminal bound suffices for a supremum | FALSE IN GENERAL; random tents disprove the inference. The common deterministic envelope (18)–(20) is the stronger fact reconstructed from its complete proof. |
| Supremum remainder for actual paths | PROVED HERE, conditionally on those complete source inputs, in (25). No supremum/expectation interchange. |
| Convolution is a terminal-time martingale | FALSE IN GENERAL; never used. The fourth-moment argument is in integration time and retains both intervals (28). |
| Uniform fourth moments and actual uniform-topology tightness | PROVED HERE in Sections 5–6, including the finite-prefix argument and compact modulus sets. |
| Continuous Gaussian existence and all covariances | PROVED HERE in Sections 7 and 10, including a common Gaussian probability space and a justified continuous extension. |
| Actual finite-dimensional limit, initial dependence | RECONSTRUCTED with the expressly conditional earlier R18 source; (35)–(37) prove concentration and initial-sigma-field factorization rather than assuming independence. |
| Full path weak convergence | PROVED HERE in Section 9 by grid approximation and compact-set extension to all bounded continuous functionals. |
| Zero/time/constant/linear-dependence/degenerate cases | ALL INCLUDED explicitly in Section 12. |
| Entire THM042 | CONDITIONAL WHOLE-CLAIM RECONSTRUCTION COMPLETE. No new unresolved path-space line remains under the exact full-source premises. |
| Exact negation | Excluded by this conditional proof when the specified premises hold; not unconditionally excluded before the separate source gates. No admitted counterexample found. |
| Source gates, hostile gate, original constructor comparison | NOT PERFORMED and not inferred. Root alone handles them after this sealed handoff. |

This self-review also checks three possible hidden circularities. The energy/Fourier arguments precede the fluctuation limit and use no Gaussian assertion. The common source envelope is a deterministic configuration inequality, not a deduction from path tightness. The continuous Gaussian process is constructed before weak-limit identification and does not rely on extracting an unknown limit of the particle laws.

## 14. Sealed bounded handoff

Only this assigned report, its unique artifact directory, exact input overlay and sibling archive/seal were written. The packet contains the complete report, exact fourteen input copies and original input manifest, source/exposure records, the new diagnostic and result, and a read-only byte verifier. Its manifest covers every packet payload file except itself; the external seal covers that manifest, the issued report and archive. Safe archive verification rejects nonregular/unsafe/duplicate paths, requires the exact complete member set, checks every declared size, reads every member with CRC verification, and compares every byte and SHA-256 with the original packet. The README gives rerun commands. File contents are sealed only after diagnostics and full byte verification pass; subsequent changes require a superseding artifact.

The remaining action is root comparison with the constructor and separate hostile/source gates. Root alone may integrate canonical state and decide promotion. This worker stops at the complete read-only sealed handoff before receiving any candidate narrative or comparison material.
