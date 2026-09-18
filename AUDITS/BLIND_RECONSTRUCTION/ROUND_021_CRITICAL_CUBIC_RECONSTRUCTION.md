# AUD061 / TASK094 — complete statement-only reconstruction of THM043

Issued 2026-09-18 UTC. Bounded independent reconstruction; no canonical promotion.

**Disposition: the entire frozen THM043 conjunction is reconstructed in its stated range.** No admitted counterexample or first failed line was found. The estimate is for the absolute value of the time integral. The proof below does not assert decay of the integral of the instantaneous absolute cubic. This is the statement-only gate; a separately isolated hostile review and the root's comparison remain required. No prior source's issued conditional history is retroactively changed.

## 1. Frozen assertion, negation, and isolation

Fix an integer \(d\ge3\), \(0<s<d-2\), \(s(s+2)<2d\), a finite horizon \(T\ge0\), a fixed smooth real terminal test \(h\), and the coefficient-one periodic Riesz kernel on the unit-Haar torus:
\[
 \widehat g(0)=0,\quad \widehat g(k)=c_{d,s}|k|^{s-d},\quad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad K=-\nabla g.
\]
For each \(N\ge2\), use the actual singular gradient particles with force \(N^{-1}\sum_{j\ne i}K(X_i-X_j)\), independent noises \(\sqrt{2\nu_N}\,dW_i\), and iid Haar initial coordinates independent of those drivers. Set
\[
 p=s+2,\ a=s/p,\ \theta=1-s/d,\quad
 \lambda_N=\beta_NN^{-\theta}\longrightarrow\lambda\in(0,\infty),\
 \nu_N=\beta_N^{-1},\ b_N=\min(\beta_N,1),\ \sigma_N=\sqrt{Nb_N}.
\]
The test \(f\) is the exact homogeneous backward Fourier test. The kernel \(\Phi\) is its genuine symmetric terminal-zero full inverse, with the internal drift \(B/N\) and both compensated responses, and with the actual R8 representatives.

For any symmetric triple kernel \(F\), write \(F_1(x,y)=\int F(x,y,z)dz\), \(F_2(x)=\iint F(x,y,z)dydz\), and \(F_0=\int F\). The statistic is literally
\[
 U_3[F]=N^{-3}\!\sum_{i,j,k\ {\rm distinct}}F(X_i,X_j,X_k)
 -3N^{-2}\!\sum_{i\ne j}F_1(X_i,X_j)
 +3N^{-1}\!\sum_iF_2(X_i)-F_0 .
\]
All tuples are ordered. Let \(C\Phi=\operatorname{Sym}_3[K(x-z)\cdot\nabla_x\Phi(x,y)]\), with the average of all six permutations. The complete assertion requires finite expected absolute integrals for every drift term in the actual R8 identity, a genuine true martingale, the exact initial endpoint, and
\[
 \sigma_N\mathbb E\left|\int_0^T U_3[C\Phi_t](X_t)dt\right|
 \le C\left[N^{s/d-1/2}+N^{-1/2}
           +N^{(a-\theta)/2}+N^{-\kappa_q}\right] \longrightarrow0,       \tag{1}
\]
for all sufficiently large \(N\), where
\[
 q_-=\max(1,s/2),\quad q_+=\min(d/2,d-s-1,s+1),\quad
 q=(q_-+q_+)/2,\quad \kappa_q=(2q-s)/(2p).
\]
The constant depends only on fixed model/test/time/kernel data and finite eventual positive lower and upper bounds for \(\lambda_N\). Every four displayed exponents must be negative, \(q_-<q_+\), and the bounded rescaled-diffusion hypothesis must actually hold.

Its exact negation is an admitted fixed datum and critical sequence for which any required integrability, exact identity/representative, or uniform rate/limit fails. A proof failure, an excluded boundary, or a generic exchangeable-law example would not prove that negation.

The task and the input seal were the first two files read. All 29 prescribed source byte strings were checked and copied into the assigned worktree before use. No root R21 narrative, other current or historical audit, R15 synthesis, R17–R20 output, old diagnostic, canonical state, memory file, or external mathematical source was opened. The two allowed R5 addenda were read only for their source-interface content. Ambient exposure and the exact source ranges are recorded in the companion SOURCE_EXPOSURE.md. The worktree is at the prescribed base e75f8b780682a7e9fb0715b5e8b5873be684a2e8 on codex/hocf-r021-critical-cubic-blind. No child, commit, push, dependency installation, or canonical edit occurred.

## 2. Parameter preflight, without narrowing the range

Since \(p<d\), \(\theta>0\). On a tail with \(0<\lambda_-\le\lambda_N\le\lambda_+<\infty\),
\[
 \nu_N=\lambda_N^{-1}N^{-\theta},\qquad
 \chi_N=\nu_NN^{2/p}
       =\lambda_N^{-1}N^{s(p-d)/(dp)}\longrightarrow0.                 \tag{2}
\]
Thus \(\nu_*=\lambda_-^{-1}\) and \(L=\lambda_-^{-1}\) are valid fixed bounds on that tail. Eventually \(\beta_N\ge1\), so \(b_N=1\); throughout the proof \(b_N\le1\) is enough. No theorem for bounded \(\chi_N\) is applied to unrestricted bounded positive noise.

The strict hypotheses imply \(s<d/2\). If \(s\le2\), then \(d>s+2\ge2s\); if \(s>2\), then \(s(s+2)>4s\), so \(4s<2d\). They also imply \(3s<2d-2\): for \(s\le2\), \(2d-2>2s+2\ge3s\); for \(s>2\), \(2d-2>s(s+2)-2=3s+(s-2)(s+1)>3s\).

Each of \(1,s/2\) is therefore strictly below each of \(d/2,d-s-1,s+1\). Consequently
\[
 1<q<d/2,\quad s/2<q<s+1,\quad q<d-s-1,\quad s+1+q<d.              \tag{3}
\]
All four powers in (1) are strictly negative:
\[
 s/d-1/2<0,\quad -1/2<0,\quad
 a-\theta=\frac{s(s+2)-2d}{dp}<0,\quad -\kappa_q<0.
\]
These are proofs for every real admitted \(s\), not inferences from a rational parameter grid. The endpoint \(s(s+2)=2d\), Coulomb, logarithmic, and other temperature regimes remain outside this assertion.

## 3. Kernel, actual law, and the two responses

This reconstruction uses the proofs in R4 Sections 2–4, R5 Sections 2–9, and R6 Sections 3–8, with the constants matched as follows.

Put \(\alpha=(d-s)/2\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). For the periodized Gaussian \(p_u\),
\[
 g(z)=A\int_0^\infty u^{\alpha-1}(p_u(z)-1)du.                       \tag{4}
\]
The integral converges in \(L^1\): at small times \(\|p_u-1\|_1\le2\), and the nonconstant large-time modes decay exponentially. The nonzero coefficient is \(A\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}=c_{d,s}|k|^{s-d}\). Substitution \(v=|z|^2/(4u)\) in the central Euclidean Gaussian term gives exactly \(|z|^{-s}\). Nonzero lattice translates at small times have exponentially small differentiated bounds; the large-time central Euclidean remainder has integrable powers. Hence \(g(z)=|z|^{-s}+H(z)\), with \(H\) smooth and even through zero in an embedded ball. Thus \(K=s z|z|^{-p}-\nabla H\in L^1\), is odd, and is smooth off zero.

Punctured-ball integration has inner flux \(s r^{d-s-2}\int_{\mathbb S^{d-1}}\varphi(r\omega)d\omega+O(r^{d-1})\). Here it tends to zero, and gamma recurrence gives the full compensated density
\[
 D=\operatorname{div}K=s(d-2-s)g_{s+2}\,dz,\quad D(\mathbb T^d)=0,
 \quad D\ge-\kappa\,dz,\quad \|D\|_{\rm TV}<\infty.                 \tag{5}
\]
Choose one \(\kappa\) at least the exact lower-density constant and the smooth-remainder lower bound in the R5 local decomposition. This is the explicit R5 addendum's compatible choice; no equality of differently defined constants is presumed. No Coulomb atom is dropped: that case is excluded here, and its separate source formula is \(c_d(\delta_0-dz)\).

For the homogeneous background the responses are
\[
 R_xv(x,y)=-\int v(x+w,y)D(dw),\qquad
 R_yv(x,y)=-\int v(x,y+w)D(dw),\quad R=R_x+R_y.                   \tag{6}
\]
Their summed sup and Haar \(L^2\) operator norms are at most \(C_R=2\|D\|_{\rm TV}\), by Cauchy–Schwarz against \(|D|\), translations, and Fubini. Null-class consistency and off-diagonal pointwise independence of diagonal extensions are separate facts: the latter follows here because \(D\) has a density. Integrated-gradient formulas follow by the punctured integration by parts with two separated possible singularities. Both responses, each with coefficient one, persist in every equation below. Exchange symmetry means exchange of pair coordinates; it does not mean Haar self-adjointness.

For the actual particles set \(H_N=N^{-1}\sum_{i<j}g(X_i-X_j)\), and \(g_*=\inf g>-\infty\). The shift \(H_N-(N-1)g_*/2\) is nonnegative and diverges at every partial or simultaneous collision. On its compact sublevels,
\[
 B^{\rm part}=-\nabla H_N,\quad
 \Delta_{Nd}H_N=\frac2N\sum_{i<j}\Delta g(X_i-X_j)\le(N-1)\kappa .
\]
Smooth local cutoffs, the additive-noise integral equation, and Picard uniqueness construct the maximal solution. Stopped Itô and the nonnegative shifted energy give
\[
 \mathbb P_x(\tau_R\le T)\le
 [H_N(x)-(N-1)g_*/2+\nu(N-1)\kappa T]/R.
\]
This proves per-start global noncollision. It applies to independent iid Haar starts by measurability and finite initial energy. Fatou first bounds the complete force-square occupation and the nonnegative Laplacian defect. That bound makes the unstopped energy martingale square integrable; Itô isometry passes stopped martingales in \(L^2\), and then gives the exact expected energy identity
\[
 \mathbb EH_N(X_T)+\mathbb E\int_0^T|B^{\rm part}|^2dt
       +\nu(N-1)\int_0^T\mathbb E D(X_1-X_2)dt=0.                 \tag{7}
\]
Absolute Laplacian occupation is justified at positive \(\nu\); there is no extraction of individual pair-force squares from the total square.

Heat forces converge in \(C^1\) on collision-excluded compact sets. Coupling with identical drivers and using the singular path's positive finite-horizon separation gives uniform-in-time path convergence at each fixed \(N,\nu\). The smooth flow's full divergence is \(2N^{-1}\sum_{i<j}D_\varepsilon\ge-(N-1)\kappa\). Its Jacobian and change of variables give \(F_t^\varepsilon\le e^{(N-1)\kappa t}\). Path convergence passes the inequality on continuous nonnegative tests; open-set approximation and outer regularity extend it to Borel sets:
\[
 F_t\le D_T:=e^{(N-1)\kappa T}.                                  \tag{8}
\]
This finite-\(N\) density bound is used only for domain/integrability, never as an \(N\)-uniform moment estimate. Common translations and permutations commute with the pathwise unique dynamics, so the actual one-body law is Haar and the law is exchangeable. Its higher marginals are not presumed independent.

## 4. Genuine inverse and exact initial endpoint

The exact test is
\[
 f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)(4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{p-d})}e^{2\pi i k\cdot x}.
\]
Rapid Fourier decay gives every fixed spatial derivative uniformly in \(\nu\ge0,t\); time derivatives are also bounded on bounded-\(\nu\) intervals. Its one-body response multiplier is negative, \(-4\pi^2c_{d,s}|k|^{p-d}\), so it solves exactly the frozen backward equation. With \(J_t=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y))\), one has \(|D^jJ|\le C_jw_{s+j}\) for \(j=0,1,2\), and time derivatives bounded by \(Cw_s\).

For the auxiliary pair generator \(G=\nu\Delta_{x,y}+B/N\), R5's harmonic Lyapunov function \(1+\chi_{\rm cut}r^{-(d-2)}\) gives per-start noncollision; the stopped exit probability is bounded by \(e^{C_VT}V(z)/(1+\varepsilon^{-(d-2)})\). The positive radial source barrier is
\[
 F_{N,\tau}(r)=\frac N4[(r^p+2sp\,\tau/N)^{2/p}-r^2].
\]
Direct differentiation gives \((\partial_\tau-2\nu\Delta-(2s/N)r^{-p}z\cdot\nabla)F\ge s r^{-s}\), because
\(\Delta F=(N/2)[Q^{s/p}(d+s-sQ)-d]\le0\), \(Q=r^p/(r^p+2sp\,\tau/N)\), using \(d\ge p\). Also \(-rF_r\le sF\), \(F\le s\tau r^{-s}\), \(F\le(2sp)^{2/p}N^{s/p}\tau^{2/p}/4\). A fixed chart cutoff adds bounded annular errors of order \(\tau\). Multiplication by \(e^{(1+sL_0)\tau}\) and addition of \(C\tau\), with the explicit annular constant in R5 (3.3), yields a nonnegative bounded barrier for \(|J|\). Stopped Itô, dropping only its nonnegative terminal value, proves finite bounded absolute source occupation at fixed \(N\). This directly supplies the genuine bounded Borel base potential \(U\), without any unproved singular heat-source limit.

The heat pair-flow divergence is at least \(-2\kappa/N\). Its Jacobian, Jensen, then fixed-\(N\) heat-path passage give
\(\|S_{t,u}\|_{2\to2}\le e^{\kappa(u-t)/N}\le e^{\kappa(u-t)/2}\). Equality-class independence and extension to \(L^2\) follow by measure domination; continuous-test approximation gives strong continuity. These steps are the full singular R5 proof, not the smooth-only conclusion of the R4 card.

Here \(2s<d\), already proved in Section 2, so \(J_*=\sup_{\nu\le\nu_*,t}\|J_t\|_2<\infty\). For example, with \(F_j=\sup\|\nabla^jf\|_\infty\), \(|\nabla H|\le L_0r\) on \(r<R\), and \(K_{\rm out}=\sup_{r\ge R}|K|\), a sufficient squared bound is
\[
 J_*^2\le
 \frac{2F_2^2s^2|\mathbb S^{d-1}|R^{d-2s}}{d-2s}
 +\frac{2F_2^2L_0^2|\mathbb S^{d-1}|R^{d+4}}{d+4}
 +4F_1^2K_{\rm out}^2.
\]
Thus \(\|U_t\|_2\le TJ_*e^{\kappa T/2}\). This elementary bound suffices on the entire frozen range; no unallowlisted radial-profile addendum is needed.

The series \(\Phi=\sum_{m\ge0}\mathcal V^mU\), \(\mathcal Vv(t)=\int_t^T S_{t,u}Rv(u)du\), converges in bounded Borel sup norm and in uniformly bounded Haar \(L^2\). Time-simplex factors are \((C_RT)^m/m!\); intervening semigroup lengths add to at most \(T\). The bound is
\[
 \sup_t\|\Phi_t\|_2\le C_\Phi:=TJ_*e^{(\kappa/2+C_R)T}.              \tag{9}
\]
The same factorial estimate gives uniqueness in each stated class. Deterministic Markov conditioning with absolute source occupation makes the inverse a true martingale source inverse along the auxiliary process. Pair exchange commutes with all terms. This identifies the actual prescribed inverse with both responses.

For clarity the initial endpoint is independently derived, not imported from the unallowlisted THM015 referenced by an older source. Decompose a symmetric real kernel \(v=c+u(x)+u(y)+v^\circ(x,y)\), where \(c=\iint v\), \(u(x)=\int v(x,y)dy-c\), \(\int u=0\), and \(v^\circ\) has zero slices. At iid Haar coordinates,
\[
 P[v]=\frac1{2N^2}\sum_{i\ne j}v^\circ(X_i,X_j)
       -\frac1{N^2}\sum_i u(X_i)-\frac{c}{2N},
\]
and degeneracy and literal pair counts give
\[
 \mathbb EP[v]^2=
 \frac{N-1}{2N^3}\|v^\circ\|_2^2+
 \frac1{N^3}\|u\|_2^2+\frac{c^2}{4N^2}.                           \tag{10}
\]
The three summands are orthogonal, including the deterministic bias. Since
\(\|v\|_2^2=\|v^\circ\|_2^2+2\|u\|_2^2+c^2\) and \(N\ge2\),
\[
 \mathbb E|\sigma_NP[\Phi_0]|^2
 \le\frac{b_N(N-1)}{2N^2}\|\Phi_0\|_2^2
 \le\frac{C_\Phi^2b_N}{2N},\quad
 \sigma_N\mathbb E|P[\Phi_0]|\le C_\Phi N^{-1/2}/\sqrt2 .          \tag{11}
\]
No exact-mean recentering or dropped initial term has been used.

## 5. Singular domain, every background, and the actual identity

The R8 proof was read through its complete domain and stopping passage. Its load-bearing analytic steps are reconstructed here to distinguish an actual domain result from a Borel inverse label. All constants in this section may depend on fixed \(N\); their later uniform replacements are explicit in Sections 6–8.

Fix \(1<q_1<d/2\) and \(q_1+1<q_2<d\). Choose fixed positive weights equal to \(r^{-\gamma}\) on an embedded ball. The homogeneous pair drift \(F=(K,-K)/N\) has largest symmetric-Jacobian eigenvalue bounded by \(c+L_N\), where \(c=(2s/N)\chi_{\rm cut}r^{-p}\) and \(L_N\) is a bounded remainder. The singular radial eigenvalue is \(-(s+1)2sr^{-p}/N\); the transverse eigenvalue is \(2sr^{-p}/N\). Its absolute matrix norm cannot replace the largest eigenvalue.

For \(m\ge0,\gamma>m\), direct radial differentiation gives, on the inner ball,
\[
 (G+mc)w_\gamma
 =-\frac{2s(\gamma-m)}N r^{-\gamma-p}
 +2\nu\gamma(\gamma+2-d)r^{-\gamma-2}
 -\frac{2\gamma}N r^{-\gamma-2}k(z)\cdot z ,
\]
where \(k=-\nabla H=O(r)\). Retain half the negative first term. The maximum of \(D v^2-(A/2)v^p\) is
\[
 Y=\frac{sD}{p}\left(\frac{4D}{pA}\right)^{2/s}
\]
when \(D>0\), and zero otherwise, with \(A=2s(\gamma-m)/N\), \(D=2\nu_*\gamma(\gamma+2-d)_+\). On the fixed annulus all cutoff derivatives are bounded; their full supremum divided by \(w_\gamma\), plus \(Y+2\gamma\sup|k|/rN\), gives a finite common \(C_{\gamma,m}\). Therefore
\[
 (G+mc)w_\gamma+b_{\gamma,m}\chi_{\rm cut}r^{-\gamma-p}
 \le C_{\gamma,m}w_\gamma,\qquad b_{\gamma,m}=s(\gamma-m)/N>0.       \tag{12}
\]
Stopped exponential-weight Itô and conditional Fatou give both the terminal weighted estimate and the positive occupation estimate. Nonnegative terminal terms are never assumed uniformly integrable to justify this passage.

For completeness, the differentiability of expectations needs more than per-start smooth paths. The nonnegative local supermartingale from (12) has maximal tail bounded by its initial weight divided by the threshold. Apply it with arbitrarily large \(m,\gamma\), then integrate a power strictly below one. For each compact set of deterministic off-diagonal starts, this bounds every finite moment of
\(\sup_{t\le T}e^{\ell\int_0^tc}w_b(Z_t)\), for any fixed finite \(\ell,b\). The local additive-noise flow has derivative \(A_t\) with \(|A_t|\le e^{L_Nt+\int_0^tc}\). For its capped inverse-distance path supremum \(V_n\), values and starting-point gradients have uniform \(L^Q\) expectations for every \(Q>2d\). They are locally Lipschitz even at bad starts: a trajectory with a larger inverse-distance supremum exceeds the cap before its possible lifetime ends, and nearby starts do so as well. Fubini and the local Sobolev estimate
\(\sup_H|v|\le C(\|v\|_{L^Q(O)}+\|\nabla v\|_{L^Q(O)})\), obtained by averaging segment derivatives with the integrable kernel \(|z|^{1-2d}\), show \(\sup_H\sup_n V_n<\infty\) almost surely. Hence all starts in a compact initial ball share a noncolliding smooth flow. Countably many balls suffice. No common null set over all noise parameters is asserted.

The second variation is
\[
 H_t^{(2)}=\int_0^t A_{t,r}D^2F(Z_r)[A_r,A_r]dr,\qquad
 |D^2F|\le C_Nw_{s+3}.
\]
Its moments with any fixed inverse-distance factor follow from those just proved. Segment differentiation and these moments give uniformly integrable first and second chain-rule derivatives, so
\[
 \nabla S_tv=\mathbb E[\nabla v(Z_t)A_t],\quad
 D^2S_tv=\mathbb E[D^2v(Z_t)[A_t,A_t]+\nabla v(Z_t)H_t^{(2)}].
\]
The same argument applies to integrated sources, and gives joint local continuity. The weighted first derivative uses \((\gamma,m)=(q_1,1)\); the direct Hessian uses \((q_2,2)\). In the second-variation term, conditioning at its insertion time bounds the future gradient by \(Cw_{q_1}\). The remaining occupation exponent is \(s+3+q_1<q_2+p\), so (12) controls it. For the source the exponents \(s+1,s+2\) obey the corresponding occupation inequalities. This proves bounded propagation and source potential in the norm
\[
 \|v\|_X=\|v\|_\infty+\sup|\nabla v|/w_{q_1}
                              +\sup|D^2v|/w_{q_2}.
\]

Both responses preserve this space. For \(0<a,b<d\), splitting neighborhoods of \(0,-z\) and their complement proves
\(\int w_a(w)w_b(z+w)dw\le C_{a,b}w_b(z)\): near either point the bound is \(Cr^{d-a-b}\le Cr^{-b}\), and on the complement \(w_b(z+w)\le Cr^{-b}\). No assumption \(a+b<d\) is needed. Since \(|D|\le Cw_p\,dz\) with \(p<d\), convolution commutes with global weak derivatives and preserves their weights. Those weak derivatives exist because deleted-tube boundary terms for orders one and two are \(O(\varepsilon^{d-1})\) and \(O(\varepsilon^{d-1-q_1})\), both vanishing. Thus \(X\subset H^1\cap W^{2,1}\). Separating the two displacement singularities proves classical local continuity of the response derivatives. A sufficient response norm is \(2\max(\|D\|_{\rm TV},R_{q_1},R_{q_2})\), where \(R_\gamma=\sup_{z\ne0}w_\gamma(z)^{-1}\int w_\gamma(z+w)|D|(dw)<\infty\). The factorial Volterra series converges with its first two local derivatives and, by bounded uniqueness, is exactly the \(\Phi\) of Section 4.

Time regularity is established separately. On the weighted Borel space \(Y=\{|v|\le Cw_s\}\), (12) with \(m=0,\gamma=s\) bounds \(S_t\); the response norm is at most \(2R_s\). The absolutely convergent Dyson series defines \(T_t\) there, with norm at most \(e^{(C_s+2R_s)t}\) and joint local continuity on locally continuous inputs. The full inverse equals \(\int_0^{T-t}T_rJ_{t+r}dr\), by the Volterra equation and factorial uniqueness in \(Y\). Since the time derivatives of \(J\) are bounded in \(Y\),
\[
 \partial_t\Phi_t=-T_{T-t}J_T+
                 \int_0^{T-t}T_r\partial_tJ_{t+r}dr,\qquad
 |\partial_t\Phi_t|\le C_Nw_s.                                   \tag{13}
\]
This differentiates the source and moving endpoint, not a nonexistent generator derivative on a full Borel sup space. Comparison of localized smooth Itô with the already constructed inverse martingale gives the classical equation off the diagonal:
\[
 \partial_t\Phi+\nu\Delta_{x,y}\Phi+B\Phi/N+R\Phi=-J.              \tag{14}
\]
Consequently \(B\Phi=-N(J+\partial_t\Phi+\nu\Delta\Phi+R\Phi)\) is Haar \(L^1\), with uniform-in-time finite slice bounds. This is a structural identity; the possibly nonintegrable crude product is not used in this general domain step.

Write \(G_\Phi=\nabla_x\Phi\), \(q_\Phi(x)=\int\Phi(x,y)dy\), \(a_\Phi(x)=\int G_\Phi(x,y)dy\), \(c_\Phi=\iint\Phi\). Uniform integrability of \(w_{q_1},w_{q_2},w_s\), weak differentiation and moving small-tube estimates show \(q_\Phi\) is \(C^1\) in time, \(C^2\) in space, with those actual derivative integrals. In particular \(\int\Delta_y\Phi\,dy=0\); the relevant boundary term is again \(O(\varepsilon^{d-1-q_1})\). The contraction of \(B\Phi\) has a continuous representative by (14).

For \(A(x,y,z)=K(x-z)\cdot G_\Phi(x,y)\),
\[
 \int|A|\,dxdydz\le\|K\|_1\sup_x\int|G_\Phi(x,y)|dy<\infty.       \tag{15}
\]
This handles simultaneous triple collisions by two independent relative variables. With two fixed distinct empirical coordinates, the remaining variable has two separated integrable singularities. No value of \(G_\Phi(x,x)\) or a partial diagonal of \(C\Phi\) is used.

Let \(A_a(x,y)=K(x-y)\cdot(a_\Phi(x)-a_\Phi(y))\) and
\(v(x)=\int K(z-x)\cdot a_\Phi(z)dz\). Integrating each of the six summands, by (15) and separated-singularity integration by parts, gives exactly
\[
 (C\Phi)_1=(A_a+R\Phi)/6,\quad (C\Phi)_2=v/3,\quad (C\Phi)_0=0,
 \quad (R\Phi)_\mu=v,\quad \iint R\Phi=0.                        \tag{16}
\]
The two zero contributions in the first contraction use \(\int K=0\); the two response contributions are different slots.

Now apply smooth Itô on a compact collision-excluded actual-particle stop to
\[
 P[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
          -\frac1N\sum_iq_\Phi(X_i)+\frac12c_\Phi .
\]
The force part is
\[
 Q=\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}K_{ik}\cdot G_\Phi(X_i,X_j)
       -\frac1{N^2}\sum_{i\ne k}K_{ik}\cdot a_\Phi(X_i).
\]
Pair the orientations of \(k=j\) before estimating. That contribution is \(D_2[B\Phi]/(2N)\). The three-distinct part and (16) then give
\[
 Q=U_3[C\Phi]+P[R\Phi]+\frac1{2N}D_2[B\Phi].
\]
Moreover \(D_2[B\Phi]-2P[B\Phi]=2\rho[g_t]+c_t\), where
\(g_t(x)=\int B\Phi_t(x,y)dy\), \(c_t=\int g_t\).
Using (14) gives the actual identity with all coefficients:
\[
 dP[\Phi_t]=\{-P[J_t]+U_3[C\Phi_t]+\ell_N(t)\}dt+dM_t,\quad
 \ell_N=N^{-1}\rho[g_t]+(2N)^{-1}c_t,                            \tag{17}
\]
\[
 \nabla_iP=N^{-2}\sum_{j\ne i}G_\Phi(X_i,X_j)-N^{-1}a_\Phi(X_i),
 \qquad M_t=\sqrt{2\nu}\sum_i\int_0^t\nabla_iP\,dW_i.             \tag{18}
\]
There is no thermal diagonal term: distinct particle labels have zero cross variation, and the background Laplacians just integrated vanish. At \(N=2\), only the raw triple sum is empty; the other terms of \(U_3\) remain.

Every term of (17) has finite expected absolute time integral by (8), (15), the structural \(B\Phi\) bound, and the integrable source weight. The square gradient is Haar integrable because \(2q_1<d\); explicitly
\[
 \sum_i\|\nabla_iP\|_{L^2({\rm Haar}^N)}^2
 \le \frac{2(N-1)^2}{N^3}\|G_\Phi\|_2^2+\frac2N\|a_\Phi\|_2^2 .
\]
Multiplying by \(2\nu D_TT\) proves finite expected bracket. Thus (18) is a square-integrable true martingale. Collision stops exhaust the paths; drifts converge in \(L^1\), stochastic integrals in \(L^2\), and the bounded observables in \(L^2\). This proves (17) unstopped, with continuous versions, without a singular diagonal trace or an unproved corrector heat-limit. Each finite initial \(N\) in the critical sequence also has these properties: one may choose its own finite \(\nu_*\) for this fixed-\(N\) domain argument.

## 6. Uniform gradient and full actual martingale bound

The complete R7 proof justifies the derivative representation used in R12: its capped-flow Sobolev argument, higher moments, segment uniform integrability, and source-occupation differentiation are the first-order version of Section 5. They are needed at fixed \(N\) before taking uniform estimates. The following computes those uniform constants rather than treating an old \(C_N\) as uniform.

Use the multiplicative R7 weights \(w_\gamma=w_1^\gamma\), \(w_1=\exp(\chi_{\rm cut}\log(1/r))\), with \(R=1/16\), equal to one outside \(B_{2R}\). Fix \(1<q<d/2,\ q\le s+1\), and put \(\eta=s+1-q\ge0\), \(\eta<p\). With \(\ell\) the full pair-Jacobian upper bound,
\[
 (G+\ell)w_q\le C_Lw_q-\frac{c_q}N1_{r\le R}w_{q+p},\quad c_q=s(q-1)>0. \tag{19}
\]
Indeed retain half of the inner negative coefficient \(2s(q-1)/N\). For \(A_q^0=2q(q+2-d)_+\), the remaining Young maximum is
\[
 \sup_{v\ge0}\{A_q^0\nu v^2-c_qv^p/N\}
 =\frac{sA_q^0}{p}
       \left(\frac{2A_q^0}{pc_q}\right)^{2/s}\chi^{p/s}
\]
if \(A_q^0>0\), and zero otherwise. The fixed annular terms and bounded remainders are at most \(C_{\rm ann}(\nu+N^{-1})\). Taking this maximum at \(\chi=L\), adding a fixed bound for those terms at \(\nu_*\), defines a finite \(C_L\) independent of \(N,\nu\). Thus the stopped exponential-weight proof gives
\[
 \mathbb Ee^{\int_t^u\ell}w_q(Z_u)\le e^{C_L(u-t)}w_q(z),\quad
 N^{-1}\mathbb E\int_t^T e^{\int_t^u\ell}1_{r_u\le R}w_{q+p}(Z_u)du
 \le c_q^{-1}e^{C_LT}w_q(z).                                    \tag{20}
\]
Globally,
\(w_{s+1}\le C_wN^{\eta/p}[w_q+N^{-1}1_{r\le R}w_{q+p}]\),
where one can take \(C_w=\max(1,\sup_{r\ge R}w_1^\eta)\); on the inner ball this is \(v^\eta\le1+v^p\) with \(v=w_1/N^{1/p}\).

Let \(J_1=\sup_{\nu\le\nu_*,t}|\nabla J_t|/w_{s+1}\). Formula (20) and the legitimate differentiated source expectation give
\[
 |\nabla U|_q\le A_{\rm base}N^{\eta/p},\quad
 A_{\rm base}=C_wJ_1 e^{C_LT}(T+c_q^{-1}).
\]
Here \(|\nabla U|_q\) denotes the weighted supremum. The response derivative bound is \(2R_q\) with \(R_q\) as in Section 5. The derivative propagator norm is \(e^{C_L(u-t)}\). Applying backward Gronwall to the finite norm of the genuine Volterra inverse gives a sufficient explicit constant
\[
 |\nabla_{x,y}\Phi_t(x,y)|\le A_qN^{(s+1-q)/p}w_q(x-y),\quad
 A_q=A_{\rm base}\exp(2R_qe^{C_LT}T).                            \tag{21}
\]
This retains both response slots. All constants have precisely the fixed-data dependence allowed in THM043.

To obtain the actual occupation needed by the noise estimate, set \(p=s+2<d\). The local divergence has positive coefficient \(s(d-2-s)\), so fixed \(c_D>0,C_D<\infty\) can be chosen with \(D(z)\ge c_Dw_p(z)-C_D\) off zero; take \(c_D=s(d-2-s)/2\) and then a sufficiently large fixed supremum for \(C_D\).

The sharp deterministic energy floor used here follows directly from (4), not an old closure assumption. For \(g^{>r}=A\int_r^\infty u^{\alpha-1}(p_u-1)du\), its nonzero Fourier coefficients are positive, \(g^{>r}(0)\le C_Gr^{-s/2}\), and \(g\ge g^{>r}-Ar^\alpha/\alpha\). Exact smooth self subtraction yields
\[
 H_N\ge-\frac12g^{>r}(0)-\frac{N-1}{2\alpha}Ar^\alpha
 \ge-C_EN^{s/d}\quad(r=N^{-2/d}),\quad C_E=(C_G+A/\alpha)/2.       \tag{22}
\]
The heat envelope proving finite \(C_G\) is \(p_u(0)\le C u^{-d/2}\) for \(u\le1\) and exponential decay thereafter. Substitution into (7), and discarding only the nonnegative complete force square, gives
\[
 \nu\int_0^T\mathbb Ew_p(X_1-X_2)dt
 \le \frac{2C_E}{c_D}N^{-\theta}+\frac{C_DT}{c_D}\nu .            \tag{23}
\]
Here \(N/(N-1)\le2\). This is the positive sub-Coulomb Laplacian occupation; its coefficient disappears at Coulomb, which is why the boundary is not included.

Use (21) at \(q_0=p/2\). It is admissible because \(1<q_0<d/2\) and \(q_0\le s+1\). Then
\[
 |G_\Phi(x,y)|^2\le A_{q_0}^2N^aw_p(x-y),\quad
 \|a_\Phi\|_2^2\le A_{q_0}^2N^aW_p,\quad W_p=\int w_p<\infty.
\]
From the exact gradient (18), a finite-sum square inequality, exchangeability, and the actual one-body Haar law,
\[
 Q_N:=\sigma_N^2\mathbb E\langle M\rangle_T
 \le4b_N\nu\int_0^T[(N-1)^2N^{-2}\mathbb E|G_\Phi(X_1,X_2)|^2
                                      +\|a_\Phi\|_2^2]dt
\]
\[
 \le4b_NA_{q_0}^2N^a
 \left[\frac{2C_E}{c_D}N^{-\theta}
             +\left(\frac{C_DT}{c_D}+TW_p\right)\nu\right]
 \le C_Qb_NN^a(N^{-\theta}+\nu).                                \tag{24}
\]
For example \(C_Q=4A_{q_0}^2[2C_E/c_D+C_DT/c_D+TW_p]\) suffices. This bounds the entire actual bracket; no iid positive-time substitution or cancellation of an uncontrolled triple covariance is used. True-martingale isometry and (2) imply
\[
 \sigma_N\mathbb E|M_T|
 \le\sqrt{Q_N}\le\sqrt{C_Q(1+\lambda_-^{-1})}\,N^{(a-\theta)/2}.    \tag{25}
\]

## 7. Uniform actual quadratic source

The source card's status phrase is not used as a premise. The following reconstructs the actual energy and positive splitting argument from the complete R10 Sections 2–3 and R16 Sections 2–7.

For fixed particle heat cutoff \(\varepsilon>0\), the smooth positive density from initial Haar satisfies
\[
 \frac d{dt}\left(\nu\int F^\varepsilon\log F^\varepsilon
                       +\int H_N^\varepsilon F^\varepsilon\right)
 =-\int F^\varepsilon|\nabla H_N^\varepsilon+
                         \nu\nabla\log F^\varepsilon|^2\le0.
\]
Smooth bounded coefficients and positive \(\nu\) give finite positive upper/lower density bounds on finite intervals, so these differentiations are legitimate. Both initial terms vanish, and entropy on a mass-one space is nonnegative. Hence \(\mathbb EH_N^\varepsilon\le0\). Since \(H_N^\varepsilon\ge(N-1)g_*/2\), the fixed-\(N\) path passage in Section 3 and Fatou after subtracting that lower bound give
\[
 \mathbb EH_N(X_t)\le0,\qquad \mathbb E|g(X_1-X_2)|\le2|g_*|.      \tag{26}
\]
At zero noise deterministic gradient-energy decrease gives the same fact, though zero noise is not needed for a finite positive-\(\beta_N\) critical sequence. A singular Fisher-information identity is never invoked. The second conclusion follows from exchangeability and \(|g|\le g+2|g_*|\).

Choose the fixed integer \(M=d+2\), and use a splitting parameter \(0<r\le2\), different from the particle heat cutoff. Set
\[
 w_r(u)=(1-e^{-u/r})^M,\quad \psi_r=1-w_r,\quad
 g_r=A\int_0^\infty u^{\alpha-1}w_r(u)(p_u-1)du,
\]
\[
 Q_r=A\int_0^\infty u^{\alpha-1}\psi_r(u)p_u\,du\ge0,\quad
 c_r=\int Q_r=Ar^\alpha B_{\alpha,M},\
 B_{\alpha,M}=\int_0^\infty u^{\alpha-1}[1-(1-e^{-u})^M]du .
\]
Here \(B_{\alpha,M}\) is positive finite, \(\psi_r\le\min(1,Me^{-u/r})\), and \(w_r\le\min(1,(u/r)^M)\). The retained kernel is \(C^2\), has zero mean, positive nonzero coefficients
\[
 a_r(k)=A\int_0^\infty u^{\alpha-1}w_r(u)e^{-4\pi^2u|k|^2}du>0,
\]
and \(0\le g_r(0)\le C_Gr^{-s/2}\). The small-time integral for two spatial derivatives converges because \(M>(s+2)/2\); the Gaussian estimates and large-time exponential tail give finite fixed \(C_G\). The exact splitting is \(g=g_r+Q_r-c_r\) off zero and in \(L^1\).

Let \(E_r=\frac12\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2\), and
\(S_r=(2N^2)^{-1}\sum_{i\ne j}Q_r(X_i-X_j)\). Both are nonnegative. Deleted-pair counting, with the smooth self term explicitly subtracted, gives
\[
 \frac{H_N}N=E_r+S_r-\frac{g_r(0)}{2N}-\frac{N-1}{2N}c_r,
 \quad
 \mathbb EE_r+\mathbb ES_r\le C_0(N^{-1}r^{-s/2}+r^\alpha).        \tag{27}
\]
One can take \(C_0=(C_G+AB_{\alpha,M})/2\). Integrability follows first from (26) and the splitting. No weighted-positive-definiteness guess is involved.

The retained weights have a scale-independent logarithmic slope. Since \(0\le u w_r'(u)\le Mw_r(u)\), integration of \(\partial_u[u^\alpha w_r(u)e^{-\lambda u}]\) gives
\(0\le-\xi a_r'(\xi)/a_r(\xi)\le L_0:=2(\alpha+M)\).
For nonzero lattice \(k,\ell\), putting \(z=k-\ell\), elementary comparison of the larger/smaller radii yields
\[
 \frac{|ka_r(k)-\ell a_r(\ell)|}{\sqrt{a_r(k)a_r(\ell)}}
 \le(1+L_0)|z|(1+|z|)^{L_0/2+1}.                               \tag{28}
\]
Indeed \(a(u)/a(R)\le(R/u)^{L_0}\), \(a(u)-a(R)\le L_0a(u)(R-u)/u\), and \(R/u\le1+|z|\), since nonzero lattice lengths are at least one.

For \(v_t=\nabla f_t\), the smooth retained source \(J_r=K_r(x-y)\cdot(v_t(x)-v_t(y))\) has diagonal zero. Its original deleted statistic equals the full centered product with \(\rho=\eta-dx\). Symmetrizing the absolutely summable Fourier expansion gives
\[
 P[J_r]=-\pi i\sum_{k,\ell\ne0}
 [ka_r(k)-\ell a_r(\ell)]\cdot\widehat v_t(\ell-k)
                         \widehat\rho(k)\overline{\widehat\rho(\ell)} .
\]
Cauchy–Schwarz in each frequency difference and (28) prove
\[
 |P[J_r]|\le2C_vE_r,\quad
 C_v=\pi(1+L_0)\sup_t\sum_z|z|(1+|z|)^{L_0/2+1}|\widehat v_t(z)|<\infty. \tag{29}
\]
The fixed smooth \(h\) bounds this seminorm uniformly in \(t,\nu\).

For the remainder \(g-g_r=Q_r-c_r\), the periodized Gaussian inequality
\[
 \operatorname{dist}(z,0)|\nabla p_u(z)|\le C_dp_{2u}(z),\qquad
 C_d=4\,2^{d/2}/e
\]
follows termwise from \(\operatorname{dist}(z,0)\le|z+n|\) and
\(\sup_{y\ge0}ye^{-y}=1/e\). Thus the mean-value bound on \(v_t\) gives
\[
 |J_{g-g_r}(x,y)|\le H_*Q_{2r}(x-y),\quad
 H_*=C_d2^{-\alpha}\sup_t\|Dv_t\|_\infty .                       \tag{30}
\]
The factor \(2^{-\alpha}\) is from substituting \(a=2u\). The remainder force is Haar \(L^1\), since its small-time derivative integral has exponent \(\alpha-3/2>-1\); here \(\alpha>1\). Therefore all original Haar contractions are actual integrals. Retaining their three original coefficients and applying (27) at \(2r\le2\) gives
\[
 \mathbb E|P[J_{g-g_r}]|
 \le H_*(\mathbb ES_{2r}+\tfrac32c_{2r})
 \le H_*\left[C_0(N^{-1}(2r)^{-s/2}+(2r)^\alpha)
                         +\tfrac32AB_{\alpha,M}(2r)^\alpha\right].
\]
Combining this with (27)–(29) and choosing \(r=N^{-2/d}\) proves
\[
 \sup_{t\le T}\mathbb E|P[J_t]|\le C_SN^{s/d-1},\quad
 \sigma_N\mathbb E\int_0^T|P[J_t]|dt\le TC_SN^{s/d-1/2},          \tag{31}
\]
where, for example,
\(C_S=4C_vC_0+H_*[C_0(2^{-s/2}+2^\alpha)+\frac32AB_{\alpha,M}2^\alpha]\)
suffices. This is independent of \(N,\nu,t\). The genuine singular \(J\) is never assigned a diagonal value; only the retained smooth source has diagonal zero. The actual-law energy sign, not a generic-law hypothesis, supplies (27). Arbitrary fixed smooth tests are covered by the displayed finite Fourier seminorm.

## 8. Both lower contractions

Use the prescribed \(q\) from (3) in (21). Put
\[
 \eta_q=(s+1-q)/p,\quad
 I_{K,q}=\int|K(z)|w_q(z)dz
 \le\frac{s|\mathbb S^{d-1}|R^{d-s-1-q}}{d-s-1-q}
 +\frac{H_0|\mathbb S^{d-1}|R^{d-q}}{d-q}
 +\sup_{z\notin B_R}|K(z)|w_q(z),                               \tag{32}
\]
where \(H_0=\sup_{B_R}|\nabla H|\). Every denominator is positive by (3). The Euclidean product gradient gives
\(|B\Phi|\le\sqrt2|K||\nabla_{x,y}\Phi|\), so
\(\|g_t\|_\infty,|c_t|\le D_qN^{\eta_q}\), \(D_q=\sqrt2A_qI_{K,q}\).
Moving-tube integration and off-diagonal continuity identify exactly the same continuous R8 slice representatives; arbitrary pair-diagonal extensions do not affect them.

Without deleting either contraction, regroup the exact expression:
\[
 \ell_N=N^{-1}\eta[g_t]-(2N)^{-1}c_t,\quad
 |\ell_N|\le\tfrac32D_qN^{\eta_q-1}.
\]
Thus the stronger pathwise bound is
\[
 \sigma_N\int_0^T|\ell_N(t)|dt
 \le C_L'\sqrt{b_N}N^{-\kappa_q},\quad
 C_L'=\tfrac32TD_q,\quad
 \eta_q-\tfrac12=-\kappa_q .                                   \tag{33}
\]
The scalar is retained with its original positive coefficient in the centered form (17). No assertion of scalar cancellation is needed. This reconstructs the entire needed R14 implication, including every condition on its gradient input.

## 9. Integrated conclusion and quantitative constant

At time \(T\), \(\Phi_T=0\), so (17) gives the exact \(L^1\) equality
\[
 \int_0^T U_3[C\Phi_t]dt
 =-P[\Phi_0]+\int_0^T P[J_t]dt-\int_0^T\ell_N(t)dt-M_T.          \tag{34}
\]
Every term has already been justified as an actual random variable; (34) is not an expectation-only cancellation. Apply the triangle inequality, (11), (25), (31), and (33). A sufficient constant in (1) is
\[
 C=\max\{TC_S,\ C_\Phi/\sqrt2,\
              \sqrt{C_Q(1+\lambda_-^{-1})},\ C_L'\}.             \tag{35}
\]
If \(T=0\) every term is zero; one may take \(C=0\). If \(h\) is constant then \(J=\Phi=0\) by uniqueness. No coefficient, centering, law class, or terminal condition has changed.

Equations (2)–(3) make all uses of uniform estimates valid for every sufficiently large \(N\) on the stated critical sequence, and all powers in (1) strictly negative. Hence the full frozen integrability/rate/limit assertion follows. This proves an integrated cubic estimate and does not establish instantaneous absolute cubic smallness, a Gaussian law, a path-space theorem, an inhomogeneous extension, or higher hierarchy completion.

## 10. Independent falsification route and gate disposition

The analytic construction was challenged separately by a newly written exact finite Fourier diagnostic. It differentiates literal particle-coordinate polynomials and constructs deleted-label statistics by subset enumeration, rather than using (16) or (17) as its implementation. Haar integration is zero-mode extraction; coefficients are Gaussian rationals. The derivative convention is \((2\pi)^{-1}\partial\), the force is the negative derivative in that convention, and every second-order identity has the common \((2\pi)^2\) factor divided out. These one-coordinate probes embed into the admissible higher-dimensional torus; they test universal algebra and do not represent a singular particle simulation.

The test families include nondegenerate constant, additive, relative, separable, and mixed kernels; \(N=2,3,4\); zero and positive diffusivity; genuine two-slot responses; the literal cubic backgrounds; initial iid second moments; and the carré-du-champ identity for the complete martingale. Mutations must actually change a tested identity: omitted response slots, omitted cubic backgrounds, replacing the symmetrization average by a sum, altered internal/lower/scalar coefficients, wrong pair normalization, omitted initial projection/bias, and reversed integrated endpoint/martingale signs. Rational parameter tests supplement the all-real proof of Section 2, including excluded boundaries and an admitted point outside a smaller exponent range. A sign-changing time-polynomial test distinguishes absolute-after-integration from integration-after-absolute. The RESULTS.json file records executed checks and nonzero mutation witnesses; it is not an analytic certification.

The strongest analytic claim was also challenged at the following exact hinges:

| Challenge | Disposition |
|---|---|
| R8 is only a bounded Borel inverse label | Reconstructed spatial/time derivatives, weak domain, partial backgrounds, and \(L^1/L^2\) stopping passage in Section 5 from its full proof. |
| Differentiating a singular expectation from per-start smoothness | High moments, capped starting-point functions, local Sobolev control and segment uniform integrability are explicitly needed and supplied. |
| Prior conditional history is treated as certification | No prior label is a premise; necessary arguments are reconstructed with their exact scopes. No earlier report is reissued or promoted. |
| Uniformity is hidden in a fixed-\(N\) constant | The uniform constants in (19)–(25) are recomputed at bounded \(\chi\); (2) proves that hypothesis. |
| Source estimate needs an unavailable source or a stricter dimension range | Positive splitting, retained Fourier commutator, and Gaussian remainder domination in Section 7 cover the full target; the fixed-\(N\) heat passage is separate. |
| Absolute cubic estimate is stronger than justified | Only (34) is estimated; no estimate of \(\mathbb E\int|U_3|\) tending to zero is claimed. |
| Haar background disappears at \(N=2\) | Literal U3 has surviving lower contractions, retained analytically and tested by a detecting mutation. |
| Initial endpoint or scalar is silently centered away | Exact iid formula (10) retains the first projection and bias; (33) retains both lower terms. |
| Noise is merely local or bounded only under Haar | Fixed-\(N\) domain proves true martingale first; actual-law Laplacian occupation then proves (24). |
| Full force occupation is confused with pair-force squares | Only the nonnegative complete square is discarded in (7); (23) comes from the positive divergence density. |
| Strict boundary or other preparation is used as a counterexample | Excluded. No admitted counterexample was obtained. |
| Finite algebra is substituted for singular analysis | Explicitly excluded; the diagnostic tests coefficients and adversarial mutations only. |

Every element of the frozen conjunction has a disposition:

| Frozen element | Result and location |
|---|---|
| Entire original parameter/law/test range, bounded rescaled diffusivity | Reconstructed, Sections 1–3. |
| Genuine unique full inverse, both response slots, terminal-zero condition | Reconstructed, Sections 3–5. |
| Actual R8 representatives, every singular/mixed/partial integral | Reconstructed, Section 5. |
| Exact finite-label identity, both lower coefficients, true martingale | Reconstructed, (16)–(18) and its stopping proof. |
| Exact initial endpoint with prescribed centering | Reconstructed, (10)–(11). |
| Uniform actual source, gradient/noise, and lower estimates | Reconstructed, Sections 6–8. |
| Prescribed midpoint, all four strictly negative powers | Reconstructed for all real admitted \(s\), Section 2. |
| Exact integrated rate and limit | Reconstructed, (34)–(35). |
| Exact negation on admitted data | No witness; incompatible with the reconstructed proof, subject to the separate hostile gate. |
| Instantaneous absolute cubic decay / Gaussian or hierarchy theorem | Not asserted by the task and not inferred. |
| Canonical theorem promotion and earlier source status changes | Not performed; root-only after the separate hostile review. |

The output packet contains every exact prescribed input, this report byte-for-byte, the complete source/exposure record, newly written diagnostic and results, reproduction instructions, input/output/archive manifests, and a read-only verifier. It verifies membership and uncompressed bytes without archive extraction. All issued files are frozen read-only after successful verification. This is the sealed bounded handoff; there is no request for a changed scientific scope or a user decision.
