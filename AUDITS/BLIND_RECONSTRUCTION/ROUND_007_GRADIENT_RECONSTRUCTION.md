# Round 007: statement-only reconstruction of the weighted pair gradient

2026-09-17 UTC. TASK-050, fresh Astra Max reconstruction in /tmp/hocf-r007-gradient-blind-20260917, branch codex/hocf-r007-gradient-blind, based on 93c20daa45aad455a95437b1dc6beed2883afada.

**Verdict: the complete frozen THM-027 assertion is proved below, using only its supplied THM-021/023/024/025 prerequisite constructions.** This is a fresh statement-only reconstruction followed by its own falsification checks. It is not the separate hostile review of a constructor. No gradient constructor, TASK-049, root gradient seed, other audit, later state/history, or memory was read. All fourteen dossier files were verified against the supplied SHA-256 list before copying, and the copies were verified again. The copied input manifest is ROUND_007_GRADIENT_INPUT_SHA256SUMS.txt in this directory, SHA-256 6cc0d45ad58a20779137cddc3e2c5de7c4688009dc918fd4991b869a0dff5e05.

All new constants may depend on the fixed particle number. The small radii below can decrease with that number, and the exponential constants need not be polynomial in it. Both exact responses, ordinary transport, the Coulomb atom and its compensation, and zero diffusivity remain included. No finite-particle Itô identity is asserted.

## 1. Assertion, negation, and prerequisite preflight

Fix precisely the THM-027 data: unit Haar torus, integer \(d\geq3\), \(0<s\leq d-2\), integer \(N\geq2\), finite \(T\geq0\), and \(0\leq\nu\leq\nu_*<\infty\). The density is continuous into \(C^2\), the ordinary drift into \(C^1\), and the test into \(C^3\), with the stated uniform bounds. Set \(E=(\mathbb T^d)^2\setminus\{x=y\}\). Fix \(1<q<d/2\). The assertion is off-diagonal \(C^1\) regularity of the specified bounded Borel full inverse, jointly Borel first derivatives, their time-uniform weighted bound, and their identification as global weak \(L^2\) first derivatives. Its exact negation is an admissible tuple violating any one of these conclusions. No second derivative, time derivative, particle-generator domain, interacting-law bound, or fluctuation limit is appended.

The exact imported inputs are:

* ROUND_004_SINGULAR_RESPONSE.md, Sections 2–4, proves the coefficient-one local expansion for the frozen Fourier coefficient \(c_{d,s}=\pi^{s-d/2}\Gamma((d-s)/2)/\Gamma(s/2)\):
  \[
  g(z)=|z|^{-s}+H(z),\qquad
  K(z)=s|z|^{-s-2}z+k(z),\quad k=-\nabla H.
  \]
  Here \(H\) is smooth and even through zero and \(k\) is smooth and odd. The Euclidean heat integral has coefficient exactly one. This complete proof supplies the local premise, not the shorter THM-021 card by itself.
* The same proof gives \(K\in L^1\), and the exact signed measure and response
  \[
  D=\operatorname{div}K=
  \begin{cases}
  s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
  c_d(\delta_0-dz),\quad c_d=(d-2)|\mathbb S^{d-1}|,&s=d-2,
  \end{cases}                                                    \tag{1}
  \]
  \[
  R_xh=-\int\mu_t(x+w)h(x+w,y)D(dw)
       -\int K(w)\cdot\nabla\mu_t(x+w)h(x+w,y)\,dw,                 \tag{2}
  \]
  together with the second-slot formula. Each response has coefficient one, has actual bounded Borel and consistent Haar equivalence-class action, and is independent off the diagonal of values assigned on the pair diagonal.
* ROUND_005_PERIODIC_PAIR_POTENTIAL.md, Sections 4–6, gives the pathwise unique noncolliding pair process from every off-diagonal start, its measurable deterministic-time Markov evolution \(S_{t,a}\), and a bounded absolute-source potential for
  \[
  J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)).                 \tag{3}
  \]
  The drifts are \(u_t(x)+K(x-y)/N\) and \(u_t(y)-K(x-y)/N\), with independent noises \(\sqrt{2\nu}\). Its relative diffusion is \(2\nu\Delta_z\), and its singular relative drift is \(2sz/(N|z|^{s+2})\).
* ROUND_005_CONDITIONAL_FULL_PAIR_INVERSE.md and ROUND_005_FULL_PAIR_INTERFACE_AND_HOMOGENEOUS_DATA.md identify the particular full inverse as the unique bounded Borel solution
  \[
  \Phi_t=U_t+\int_t^T S_{t,a}(R_x+R_y)_a\Phi_a\,da,\qquad
  U_t=\mathbb E_{t,x,y}\int_t^T J_a(X_a,Y_a)\,da.                  \tag{4}
  \]
  The source/constant addendum supplies the full local-kernel premise and common lower-divergence constant; the symmetry clarification means commutation with pair exchange, not Haar self-adjointness.

The four full prerequisite proofs and both addenda were read. References inside them to older reports are not silently imported: the needed local kernel, response, process and composition arguments are contained in the permitted proofs. The initial-iid consequence is not used here. No external source or novelty claim is used. Heat-cutoff semigroup convergence is not used to differentiate the singular-source expectation.

## 2. Weights and the Jacobian coefficient

Put \(p=s+2\). Choose \(0<R<1/12\) so the local expansion holds through \(B_{3R}\). Choose smooth radial \(0\leq\chi\leq1\), equal to one on \(B_R\), zero outside \(B_{2R}\), with periodic zero extension. A concrete annular choice is
\[
\chi(z)=\frac{e((2R)^2-|z|^2)}
 {e((2R)^2-|z|^2)+e(|z|^2-R^2)},\qquad
e(v)=\begin{cases}e^{-1/v},&v>0,\\0,&v\leq0.\end{cases}
\]

For \(a>0\) define
\[
W_a(z)=1+\chi(z)(|z|^{-a}-1).                                  \tag{5}
\]
It is positive and smooth off zero, at least one, exactly \(|z|^{-a}\) on \(B_R\), and one outside \(B_{2R}\). Moreover
\[
W_q^2\leq W_{2q},                                              \tag{6}
\]
since the difference is \(\chi(1-\chi)(|z|^{-q}-1)^2\). Any weight in the frozen statement is comparable to \(W_q\): their ratio is one near zero and bounded above and below on the compact complement. Thus it suffices to use (5). Distances are never differentiated across a torus cut locus.

Let \(U_0=\sup_t\|u_t\|_\infty\), \(L_u=\sup_t\|Du_t\|_{\mathrm{op},\infty}\), \(L_k=\sup_{B_{2R}}\|Dk\|_{\mathrm{op}}\), and \(L=L_u+L_k\). On \(B_R\), the nonsingular relative drift \(w_t=u_t(x)-u_t(y)+2k(x-y)/N\) obeys \(|w_t|\leq L|x-y|\), since \(2/N\leq1\).

The field \(k_g=K-s\chi |z|^{-p}z\) extends smoothly through zero and periodically. Define the finite sufficient constants
\[
M_K=\|Dk_g\|_{\mathrm{op},\infty}
 +s\sup_{R\leq|z|\leq2R}|z|^{1-p}|\nabla\chi(z)|,\qquad
A_0=L_u+2M_K/N,\qquad
A(z)=A_0+(2s/N)\chi(z)|z|^{-p}.                               \tag{7}
\]
The largest eigenvalue of the singular part
\(s\chi r^{-p}(I-p\theta\otimes\theta)\) of \(DK\) is \(s\chi r^{-p}\); its radial eigenvalue is \(-s(s+1)\chi r^{-p}\). For a pair variation,
\[
N^{-1}(v_1-v_2)\cdot DK(z)(v_1-v_2)
\leq(2/N)(s\chi r^{-p}+M_K)(|v_1|^2+|v_2|^2).
\]
The two ordinary-transport blocks contribute at most \(L_u\) to the largest symmetric-part eigenvalue. Therefore every first variation of the pair flow satisfies
\[
\|DF_{t,b}(x,y)\|_{\mathrm{op}}
\leq\exp\!\left(\int_t^b A(X_r-Y_r)\,dr\right).                 \tag{8}
\]
Only first spatial derivatives of \(u\) occur. The additive Brownian displacement has spatial derivative the identity. Justification of a common local pathwise flow and of the expectation derivative follows next.

## 3. Pathwise localization for a neighborhood of starting points

Pointwise-in-start noncollision alone is insufficient for differentiating an expectation. We first remove that exceptional-set problem without requiring moments of a random localization radius.

Choose \(1/p<\gamma<1/2\). Almost every Brownian path on the finite interval is \(\gamma\)-Hölder. For completeness, at dyadic level \(n\), a Gaussian tail and a union bound bound the probability that any increment exceeds a fixed multiple of \(2^{-n\gamma}\) by \(C2^n\exp(-c2^{n(1-2\gamma)})\). This is summable. Borel–Cantelli and a maximum over the finitely many remaining levels give a finite bound for all dyadic increments. Dyadic approximations of two arbitrary times and a geometric series then give the Hölder estimate for all times. Apply this to the finitely many coordinates. Thus the relative additive noise \(\xi=\sqrt{2\nu}(B^1-B^2)\) obeys
\[
|\xi_b-\xi_a|\leq H|b-a|^\gamma
\]
with finite \(H\geq1\), using \(\nu_*\) if necessary. The zero-noise path satisfies this as well.

For each such fixed driving path put \(b_0=2s/N>0\). Choose \(\varepsilon\) sufficiently small that \(2\varepsilon<R\), and, with
\[
\delta=(\varepsilon/(4H))^{1/\gamma},\qquad
\delta\leq\min(1,(8L)^{-1}),\qquad
b_0(2\varepsilon)^{-p}\delta\geq1,                             \tag{9}
\]
where the inverse of zero is interpreted as infinity. This is possible because \(1/\gamma<p\).

Suppose a local solution downcrosses from radius \(2\varepsilon\) to radius \(\varepsilon\). Let \(\sigma\) be its last radius-\(2\varepsilon\) time before its first radius-\(\varepsilon\) time \(\tau\). The intervening path stays in the embedded annulus. With \(e=z_\sigma/(2\varepsilon)\) and \(h=e\cdot z\), up to \(\min(\tau,\sigma+\delta)\),
\[
h_a=2\varepsilon+\int_\sigma^a b_0|z_r|^{-p}h_r\,dr
 +\int_\sigma^a e\cdot w_r\,dr+e\cdot(\xi_a-\xi_\sigma).
\]
The last two terms together are at least \(-\varepsilon/2\). A first-crossing argument gives \(h_a\geq3\varepsilon/2\): at a first lower crossing the positive integral prevents it. If \(\tau\leq\sigma+\delta\), this contradicts \(|z_\tau|=\varepsilon\). Otherwise, at \(\sigma+\delta\), the integral is at least \(3\varepsilon b_0(2\varepsilon)^{-p}\delta/2\geq3\varepsilon/2\), so \(h\geq3\varepsilon>2\varepsilon\), contradicting the annulus constraint. No such downcrossing exists.

For any compact set of initial pairs in \(E\), choose \(2\varepsilon\) below its minimum separation and satisfy (9). All trajectories for this driving path stay at least \(\varepsilon\) from the diagonal through the horizon. Patch their local equations; no other blow-up can occur on the compact collision-excluded state space. A countable compact exhaustion yields a probability-one set on which there is a global flow from all starting points, with uniform separation on each compact set. Uniqueness identifies it with the supplied process. Relative lifts during each annular excursion are valid because that excursion stays within one embedded difference chart.

Subtracting the continuous additive path leaves an integral equation with \(C^1\) spatial drift. On the established compact neighborhood, its derivative is bounded and uniformly continuous. Subtracting the equations, then their difference quotients, and applying Gronwall proves the variational equation and continuous dependence of its derivative on the initial point. The error term tends uniformly to zero by uniform continuity of the drift derivative. Consequently, for almost every driving path, \(F_{t,b}\) is \(C^1\) on \(E\), locally uniformly in the initial point through the time interval, and obeys (8). No moment of the random separation bound is presumed.

## 4. Weighted moments and collision occupation

For \(\lambda>0\) and \(a>\lambda\), define
\[
c_{a,\lambda}=s(a-\lambda)/N,\qquad Q_a=2\nu_*a(a+2-d)_+,
\qquad
\rho_{a,\lambda}=
\begin{cases}
R,&Q_a=0,\\
\min(R,(c_{a,\lambda}/Q_a)^{1/s}),&Q_a>0.
\end{cases}                                                   \tag{10}
\]
On \(0<r<R\), using the exact relative diffusion \(2\nu\),
\[
(L_t+\lambda A)W_a
\leq\left[-(2s/N)(a-\lambda)r^{-p}
 +2\nu_*a(a+2-d)_+r^{-2}+aL+\lambda A_0\right]W_a.             \tag{11}
\]
On \(r<\rho_{a,\lambda}\), the first two terms are at most
\(-c_{a,\lambda}r^{-p}W_a\). This includes \(d=3\), where the diffusion term can be positive; it is absorbed with \(r^s\), not dropped. At zero noise no inverse diffusivity occurs.

For \(\rho=\rho_{a,\lambda}\), make the global constants explicit by setting
\[
B_\rho=2U_0+(2/N)\sup_{\operatorname{dist}(z,0)\geq\rho}|K(z)|,
\]
\[
\begin{split}
C_{a,\lambda}={}&aL+\lambda A_0
 +2\nu_*\sup_{\operatorname{dist}\geq\rho}|\Delta W_a|/W_a\\
&+B_\rho\sup_{\operatorname{dist}\geq\rho}|\nabla W_a|/W_a
 +\lambda\sup_{\operatorname{dist}\geq\rho}A,\\
H_{a,\lambda}(z)={}&\mathbf1_{\{0<|z|<\rho\}}|z|^{-p}W_a(z).
\end{split}                                                   \tag{12}
\]
All suprema are finite and \(C_{a,\lambda}\geq0\). Equations (11)–(12) give on all of \(E\)
\[
(L_t+\lambda A)W_a\leq C_{a,\lambda}W_a-c_{a,\lambda}H_{a,\lambda}.
                                                                  \tag{13}
\]
Stop at a positive collision radius and apply smooth Itô to
\[
\exp\!\left(\lambda\int_t^r A(X_v-Y_v)\,dv-C_{a,\lambda}(r-t)\right)
 W_a(X_r-Y_r).
\]
All differentiated functions, coefficients and exponential factors are bounded on the stopped compact domain, so its stochastic integral is a true martingale. Add the nonnegative occupation term from (13). Decrease the stopping radius to zero and apply Fatou to both nonnegative terms, using noncollision. Removing the discount by \(C_{a,\lambda}\geq0\) yields, for \(t\leq b\leq T\),
\[
\begin{split}
&\mathbb E_{t,x,y}e^{\lambda\int_t^b A}W_a(X_b-Y_b)\\
&\quad+c_{a,\lambda}\mathbb E_{t,x,y}\int_t^b
 e^{\lambda\int_t^r A}H_{a,\lambda}(X_r-Y_r)\,dr
 \leq e^{C_{a,\lambda}(b-t)}W_a(x-y).                         \tag{14}
\end{split}
\]
The different time discount factors are each bounded below by the same \(e^{-C_{a,\lambda}(b-t)}\); hence the displayed sum has the stated single constant.

Use \((a,\lambda)=(q,1)\), abbreviating its constants by \(C_1,c_1,\rho_1,H_1\). Also use \((a,\lambda)=(2q,2)\). With (6), this gives the crucial second moment
\[
\mathbb E\left[\left(e^{\int_t^b A}W_q(X_b-Y_b)\right)^2\right]
 \leq e^{C_{2q,2}(b-t)}W_{2q}(x-y).                          \tag{15}
\]
The auxiliary exponent \(2q\) need not be below \(d-2\); its positive diffusion coefficient is handled by (10). Haar integrability is a separate issue.

## 5. A complete expectation-differentiation argument

Let \(\mathcal X_q\) be the bounded \(C^1(E)\) functions with norm
\[
\|h\|_{\mathcal X_q}=\|h\|_\infty+G(h),\qquad
G(h)=\sup_E|\nabla_{x,y}h|/W_q(x-y).                          \tag{16}
\]
For \(h\in\mathcal X_q\), the actual pointwise transition expectation is \(C^1(E)\), and
\[
D(S_{t,b}h)(x,y)=\mathbb E[Dh(F_{t,b})DF_{t,b}],\qquad
G(S_{t,b}h)\leq e^{C_1(b-t)}G(h).                            \tag{17}
\]

To justify it, fix a deterministic compact ball in \(E\). Section 3 gives one probability-one set on which \(h\circ F_{t,b}\) is \(C^1\) throughout that ball. Its derivative is bounded by \(G(h)e^{\int A}W_q(X_b-Y_b)\); (15) bounds its second moment uniformly over initial points in the ball. Along any convergent sequence of initial points, the random derivatives converge almost surely by the pathwise \(C^1\) dependence and continuity of \(Dh\). They converge in \(L^1\) as well: truncate at a large magnitude, apply bounded convergence to the truncated part, and bound the tails uniformly by the second moment. Thus their expectations are continuous in the initial point. Along any short deterministic line segment in the ball, the pathwise fundamental theorem of calculus and Fubini apply because of the uniform first-moment bound. The difference of the endpoint expectations is the line integral of this continuous expected derivative. This proves differentiability, the exact formula, and continuity in (17). Its weighted estimate follows from (8) and (14). Sup-norm contraction then gives
\[
\|S_{t,b}h\|_{\mathcal X_q}\leq e^{C_1(b-t)}\|h\|_{\mathcal X_q}. \tag{18}
\]

The same argument applies to \(\int_t^T S_{t,b}h_b\,db\), if the time family and its derivatives are jointly Borel, each member is \(C^1(E)\), and their \(\mathcal X_q\) norms are uniformly bounded. Use (15) on the product of time measure and Brownian probability to obtain uniform integrability; also integrate the line identity in time. This proves differentiation under that time integral and continuity of its derivative. It applies to a terminal-time integral of length zero as well.

The flow derivatives are jointly Borel, being limits of difference quotients of the measurable path map. Composing, multiplying and parameter integration preserve that property. Alternatively the final derivatives are limits of Borel difference quotients of the expectations on each torus chart. No time derivative of the data is taken. These arguments supply more than almost-sure pointwise path differentiability; they explicitly justify the expectation interchanges.

## 6. Singular-source occupation and derivative convergence

Let \(G_f=\sup_t\|\nabla f_t\|_\infty\) and \(H_f=\sup_t\|D^2f_t\|_{\mathrm{op},\infty}\). For \(r<R\), direct differentiation of (3) yields
\[
|J_t|\leq C_0^Jr^{-s},\qquad
|\nabla_{x,y}J_t|\leq C_1^Jr^{-s-1},
\]
\[
C_0^J=H_f(s+L_kR^{s+2}),\qquad
C_1^J=\sqrt2H_f[s(s+2)+2L_kR^{s+2}].                         \tag{19}
\]
Each slot derivative is at most \(\|DK\|H_fr+H_f|K|\), and
\(\|DK\|\leq s(s+1)r^{-p}+L_k\), proving the coefficients. Outside \(B_{\rho_1}\) a sufficient bound is
\[
J_{\rm out}=\sqrt2\left[
2G_f\sup_{\operatorname{dist}\geq\rho_1}\|DK\|
 +H_f\sup_{\operatorname{dist}\geq\rho_1}|K|\right].            \tag{20}
\]

Choose smooth \(0\leq\eta\leq1\) equal to zero on \((-\infty,1]\) and one on \([2,\infty)\). A concrete transition is
\(\eta(v)=e(v-1)/(e(v-1)+e(2-v))\) for \(1<v<2\), with \(e\) as above. Put \(M_\eta=\|\eta'\|_\infty\). For \(0<\delta<\rho_1/4\), let \(J^\delta=\eta(r/\delta)J\), with the cutoff one outside the embedded chart. This source is globally bounded \(C^1\). Its cutoff derivative has pair norm at most
\(\sqrt2M_\eta/\delta\leq2\sqrt2M_\eta/r\) on the transition annulus. With
\[
C_J=C_1^J+2\sqrt2M_\eta C_0^J,
\]
we have
\[
|\nabla J^\delta_t|\leq J_{\rm out}W_q+C_J\rho_1^{q+1}H_1.     \tag{21}
\]
Section 5 first justifies differentiation of
\(U^\delta_t=\mathbb E\int_t^T J^\delta_b(X_b,Y_b)\,db\)
using the finite derivative bound for each fixed cutoff. Equations (8), (14), and (21) then give
\[
G(U^\delta_t)\leq e^{C_1T}
 (TJ_{\rm out}+C_J\rho_1^{q+1}/c_1)=:G_U.                     \tag{22}
\]
More importantly, the derivative of \(J^\delta-J^\varepsilon\) is supported where \(r<2\max(\delta,\varepsilon)\) and is at most \(2C_Jr^{-s-1}\). Since \(H_1=r^{-s-2-q}\) there,
\[
G(U^\delta_t-U^\varepsilon_t)
\leq(2C_J/c_1)e^{C_1T}[2\max(\delta,\varepsilon)]^{q+1}.        \tag{23}
\]
This is the near-collision estimate for the differentiated source occupation. It cannot be replaced by smooth-cutoff semigroup convergence.

For completeness the supplied base-potential proof, equations (3.1)–(3.4) and (5.3), gives the sufficient fixed-\(N\) absolute-source bound
\[
B_{\rm abs}:=\sup_{t,E}\mathbb E\int_t^T|J_b|\,db
\leq e^{\alpha T}
\left[\frac{H_f(2sp)^{2/p}}4N^{s/p}T^{2/p}+C_BT\right],        \tag{24}
\]
where, using the same radii \(R,2R\),
\[
\begin{gathered}
\alpha=1+sL,\quad B_J=H_fL_kR^2+2G_fK_{\rm out},\quad
K_{\rm out}=\sup_{\operatorname{dist}\geq R}|K|,\\
V_*=sR^{-s-1}+2LR,\quad C_\chi^{(1)}=\|\nabla\chi\|_\infty,\quad
C_\chi^{(2)}=\|\Delta\chi\|_\infty,\\
E_*=sR^{-s}(2\nu_*C_\chi^{(2)}+V_*C_\chi^{(1)})
 +4\nu_*C_\chi^{(1)}s^2R^{-s-1},\qquad
C_B=B_J+H_fE_*/\alpha.
\end{gathered}
\]
All its prescribed-data hypotheses hold here. Since \(|J^\delta|\leq|J|\), \(\|U^\delta_t\|_\infty\leq B_{\rm abs}\), and dominated convergence by the absolute occupation gives \(U^\delta_t\to U_t\) at every off-diagonal start. Equation (23) makes the gradients Cauchy locally uniformly, uniformly also in time. Taking the limit in their line-segment identities identifies the continuous gradient limit as the derivative of \(U_t\). Consequently
\[
\sup_t\|U_t\|_{\mathcal X_q}\leq B_{\rm abs}+G_U=:B_U.          \tag{25}
\]
A countable cutoff sequence and the Borel formulas give jointly Borel derivatives of \(U\). No value or convergence on the pair diagonal is used.

## 7. Weak derivatives and the exact convolution threshold

Two elementary facts avoid hidden representative and integrability assumptions.

First, if \(h\in\mathcal X_q\) and \(q<d\), its off-diagonal gradient is its global weak first derivative and is in \(L^1\). The weight is integrable because its tube radial exponent is \(d-1-q>-1\). Multiply \(h\) by a smooth cutoff vanishing on a radius-\(\varepsilon\) diagonal tube and equal to one outside radius \(2\varepsilon\). In integration by parts against a smooth full-torus test, the derivative of this cutoff contributes at most
\(C\|h\|_\infty\|\varphi\|_\infty\varepsilon^{d-1}\),
since the tube volume is \(O(\varepsilon^d)\). It tends to zero. Dominated convergence for the other two terms gives the global weak derivative identity, without a diagonal boundary measure.

Second, write \(\mathfrak d(z)\) for torus distance to zero, only for estimates, and put
\(D_*=\sqrt d/2\), \(\omega_d=|\mathbb S^{d-1}|\), \(F_b(z)=1+\mathfrak d(z)^{-b}\).
For \(0<b<d\),
\[
\int F_b\leq M_b:=1+\omega_dD_*^{d-b}/(d-b).                  \tag{26}
\]
For any \(0<a<d\) and \(0<q<d\),
\[
\int F_a(w)F_q(z+w)\,dw\leq C_{a,q}^{\rm conv}F_q(z),          \tag{27}
\]
with the explicit sufficient constant
\[
\begin{split}
C_{a,q}^{\rm conv}={}&2^qM_a\\
&+\omega_d\left[
\frac{2^{-d}}d(D_*^{d+q}+2^aD_*^{d+q-a})
 +\frac{2^{q-d}}{d-q}(D_*^d+2^aD_*^{d-a})\right].             \tag{28}
\end{split}
\]
To verify it, set \(r=\mathfrak d(z)>0\). On \(\mathfrak d(z+w)\geq r/2\), the second factor is at most \(2^qF_q(z)\), giving the first term. On the complement, \(\mathfrak d(w)>r/2\) by the triangle inequality; bound the first factor by \(1+2^ar^{-a}\) and integrate the second over a radius-\(r/2\) ball. Its integral is at most
\(\omega_d[(r/2)^d/d+(r/2)^{d-q}/(d-q)]\).
A torus ball is represented by the intersection of a Euclidean ball with a fundamental cube, so this bound remains valid above the injectivity radius. Divide by \(F_q(z)\geq r^{-q}\); the remaining powers of \(r\) are all positive because \(a<d\). Replacing them by their values at \(D_*\) gives (28). In particular no condition \(a+q<d\) is needed.

For (5), \(W_q\leq F_q\leq c_WW_q\), with \(c_W=1+R^{-q}\). Define
\[
B_K^*=\sup_{z\ne0}|K(z)|/F_{s+1}(z),\qquad
B_D^*=\sup_{z\ne0}|s(d-2-s)g_{s+2}(z)|/F_{s+2}(z)\quad(s<d-2).
\]
These constants are finite by the local expansion and smoothness off zero. Thus
\[
\int W_q(z+w)|K(w)|\,dw\leq A_KW_q(z),\qquad
\int W_q(z+w)|D|(dw)\leq A_DW_q(z),                           \tag{29}
\]
with
\[
A_K=B_K^*c_WC_{s+1,q}^{\rm conv},\qquad
A_D=\begin{cases}
B_D^*c_WC_{s+2,q}^{\rm conv},&s<d-2,\\
c_d(1+M_q),&s=d-2.
\end{cases}                                                  \tag{30}
\]
The Coulomb row uses the actual measure \(|D|=c_d\delta_0+c_d\,dw\), so its convolution is exactly \(c_dW_q+c_d\int W_q\). It is not an \(r^{-d}\) density.

## 8. Both responses preserve the weighted \(C^1\) space

Let \(M_j=\sup_t\|D^j\mu_t\|_\infty\), \(j=0,1,2\), in vector/operator norm as appropriate. Set
\[
C_R=2(M_0\|D\|_{\rm TV}+M_1\|K\|_1),\qquad
C_B^R=M_1\|D\|_{\rm TV}+M_2\|K\|_1,
\]
\[
C_q^R=C_R+2C_B^R+2(M_0A_D+M_1A_K).                          \tag{31}
\]
For \(h\in\mathcal X_q\), both actual pointwise responses are \(C^1\) off the diagonal and
\[
|\nabla(R_x+R_y)_th|
\leq2C_B^R\|h\|_\infty+2(M_0A_D+M_1A_K)G(h)W_q(x-y).         \tag{32}
\]
Indeed, differentiating the first product in (2) in all pair coordinates gives norm at most
\(M_1\|h\|_\infty+M_0G(h)W_q(x+w-y)\).
The second product gives at most
\(|K(w)|[M_2\|h\|_\infty+M_1G(h)W_q(x+w-y)]\).
Use (29), then the second slot. The absolute kernels and weight are even, so the same constants apply. Both factors two are retained.

Here is the justification of these pointwise derivatives. Section 7 puts \(h\) in global \(W^{1,1}\). Multiplication by the smooth density and its gradient gives the displayed product weak derivatives. Fubini for their integrable derivatives and the finite measures in (2) makes the proposed formulas global distributional derivatives. Their off-diagonal integrals are finite by (29) and continuous there: on a compact output set away from the diagonal, the kernel singularity at \(w=0\) is separated from the possible singularity of \(\nabla h(x+w,y)\) at \(w=y-x\). Near zero the latter argument stays uniformly away from its diagonal and a fixed integrable kernel dominates. Near the moving second singularity, the kernel is smooth and bounded and the integral over a radius-\(\varepsilon\) neighborhood is uniformly \(O(\varepsilon^{d-q})\). Off these neighborhoods use dominated convergence for continuous integrands. The atom is merely the derivative of \(-c_d\mu(x)h(x,y)\), continuous off the diagonal. The same argument with bounded \(h\), without its derivative, shows continuity of the actual response itself.

A continuous function with these continuous distributional derivatives is \(C^1\) on every ball in \(E\): mollify in a slightly larger ball, pass uniformly in function and derivative, and use the line identity. This identifies the actual representative's derivative, not just an arbitrary a.e. version. Parameter integration gives joint Borel measurability. Changing diagonal values affects integrands only at \(w=y-x\ne0\), where there is no atom, so it changes none of these off-diagonal values. At Coulomb the atom at \(w=0\) multiplies \(h(x,y)\), never a diagonal trace.

Together with the exact sup bound and \(W_q\geq1\), (32) proves
\[
\|(R_x+R_y)_th\|_{\mathcal X_q}\leq C_q^R\|h\|_{\mathcal X_q}.  \tag{33}
\]
The \(C^2\) density assumption supplies exactly the \(M_2\) term. No regularity of an unspecified actual reference is presumed.

## 9. Weighted construction and identification of the full inverse

The normed space \(\mathcal X_q\) is complete: a Cauchy sequence converges uniformly in value and locally uniformly in first derivative, and its line identity identifies the limit's derivative. Work with jointly Borel time families with uniform \(\mathcal X_q\) bounds. Integrals below are defined pointwise with the derivative formula from Section 5; no Bochner measurability in a possibly nonseparable weighted supremum space is presumed.

Put \(Vh(t)=\int_t^T S_{t,a}(R_x+R_y)_ah_a\,da\). Iterating (18) and (33) over ordered time simplices gives
\[
\|(V^kU)(t)\|_{\mathcal X_q}
\leq e^{C_1(T-t)}B_U[C_q^R(T-t)]^k/k!,\qquad k\geq0.          \tag{34}
\]
The propagation interval lengths add, yielding one exponential in their total length. Each term and derivative are jointly Borel. The series \(\widetilde\Phi=\sum_{k\geq0}V^kU\) converges uniformly in value and weighted derivative, uniformly in time. Its first derivatives are continuous on \(E\) for every time and jointly Borel, and
\[
\sup_{0\leq t\leq T}\|\widetilde\Phi_t\|_{\mathcal X_q}
\leq B_Ue^{(C_1+C_q^R)T}.                                    \tag{35}
\]
Dominated integration shows the series solves (4) pointwise. It is bounded Borel and terminal zero, so THM-024/025 pointwise uniqueness identifies it with the originally specified \(\Phi\), not merely its Haar class. Source, evolution and summed response commute with pair exchange; hence symmetry is preserved. Both exact signed responses are restored, without treating them as a positive Markov perturbation.

All coefficient choices in (7), (10), (12), (19)–(24), (28), (30), (31), and (35) are finite. Their only diffusivity parameter is \(\nu_*\); the radii and resulting constants may depend severely on fixed \(N\). If \(T=0\), the inverse and derivative are zero directly. This proves the entire off-diagonal differentiability and weighted-bound portion of THM-027.

## 10. Global weak \(H^1\) conclusion

Apply Section 7's cutoff integration by parts to \(\Phi_t\). It identifies the off-diagonal gradients as global weak first derivatives. Since \(2q<d\),
\[
\int_{\mathbb T^d}W_q(z)^2\,dz
\leq2[1+\omega_dD_*^{d-2q}/(d-2q)]=:I_q<\infty.              \tag{36}
\]
Translation invariance gives \(\int W_q(x-y)^2\,dx\,dy=\int W_q(z)^2\,dz\). Thus
\[
\sup_t\|\Phi_t\|_{H^1((\mathbb T^d)^2)}^2
\leq(1+I_q)B_U^2e^{2(C_1+C_q^R)T}.                            \tag{37}
\]
Zero diagonal values give a Borel representative. Any other assignment on that null set gives the same complete-Haar equivalence class and weak derivatives. This is not a diagonal trace theorem. The boundary error is \(O(\varepsilon^{d-1})\) because \(\Phi\) is bounded; no gradient trace is assumed.

## 11. Falsification tests and per-claim disposition

The following distinct checks were developed in this statement-only context.

1. **Zero-noise radial diagnostic.** With local pure singular force and no ordinary drift, \(r_b^p=r_t^p+(2sp/N)(b-t)\), with fixed direction. The tangential derivative is \(r_b/r_t\), and the radial derivative is \((r_t/r_b)^{p-1}\). This confirms the tangential growth coefficient \(2sr^{-p}/N\) in (7); replacing it by the absolute radial eigenvalue \(2s(s+1)r^{-p}/N\) would incorrectly lose \(1<q\leq s+1\). For a local quadratic test with Hessian \(H\), the exact source potential before exiting the chart is \((N/4)(\theta\cdot H\theta)(r_b^2-r_t^2)\). A nonconstant angular factor gives an inverse-radius angular derivative. The asserted \(q>1\) dominates it; arbitrary \(q<1\) fails in that local model. This is a diagnostic, not a substitution of a nonperiodic force into the theorem.
2. **Dimension three and noise.** At \(d=3\), the diffusion coefficient in (11) is \(2\nu a(a-1)>0\) for the exponents used. Formula (10) absorbs it, including \(a=2q\) for the second moment. At \(\nu_*=0\), the choice is \(\rho=R\), and no ellipticity division is introduced.
3. **Coulomb atom, compensation and constants.** At \(s=d-2\), the first response is
   \(-c_d\mu(x)h(x,y)+c_d\int\mu(z)h(z,y)\,dz-\int K(z-x)\cdot\nabla\mu(z)h(z,y)\,dz\).
   For \(h=1\), the three terms cancel, including for inhomogeneous density. Dropping either the atom or compensation gives a false nonzero response. For homogeneous density, the two-slot Fourier eigenvalue is \(-c_d(\mathbf1_{k\ne0}+\mathbf1_{\ell\ne0})\).
4. **Constant test.** A spatially constant \(f_t\), even with a time-varying constant, gives \(J=U=\Phi=0\) for any admissible \(\mu,u\), at zero or positive noise. Its derivatives and all weighted bounds vanish.
5. **Convolution threshold.** Below Coulomb, \(s+2+q\) may equal or exceed \(d\). A diagonal convolution value can diverge; the off-diagonal bound (27) needs only \(s+2<d\) and \(q<d\). At the endpoint \(s+2=d\), (30) uses the atom, not an invalid limiting density.
6. **Expectation derivatives.** The proof supplies a common pathwise local domain, higher moments, \(L^1\) continuity in the initial point, an integrable line identity, and the separate source tail (23). Pathwise differentiability or strong cutoff-semigroup convergence alone supplies none of these automatically.

| Frozen claim | Disposition |
|---|---|
| Off-diagonal \(C^1\) in both slots for every time | Proved in Sections 3–6, 8–9 |
| Jointly Borel first derivatives | Proved in Sections 5–6 and the series in Section 9 |
| Weighted bound for every \(1<q<d/2\) | Proved with explicit constants in (10)–(14), (22), (31), (35) |
| Uniformity in \(\nu\in[0,\nu_*]\) | Proved; constants use only \(\nu_*\) |
| Both responses, transport, Coulomb atom and compensation | Retained in (1)–(2), (7), (30)–(33) |
| Off-diagonal representative and convolution claims | Proved in Sections 7–9; no trace assertion |
| Global weak derivatives and time-uniform Haar \(H^1\) | Proved in Sections 7 and 10 |
| Particle Itô formula, second derivatives, law transfer, bracket decay | Outside the frozen statement; unproved here |

There is no first unsupported line within the frozen THM-027 conjunction identified by this reconstruction. For the excluded dynamical use, the first unsupported line would be inserting this first-order regularity into a singular \(N\)-particle generator/Itô formula and passing its second-order and interaction terms under the actual particle law. That insertion is not justified here.

## 12. Reproducibility and seal

The standard-library checker round007_gradient_exact_checks.py uses exact rational arithmetic. It checks radial/tangential pair coefficients, primary and higher-moment barrier margins, zero noise, dimension three, small particle numbers, the source-tail exponent, the weight-square identity, admissible convolution thresholds, the two-slot Coulomb response, and constant-input cancellation with inhomogeneous density. Its sealed JSON records the counts and conventions. These checks corroborate algebra and scope; they do not replace the analytic proof.

Verification before issuance:

* Running the exact checker completed with all 10,327 exact rational assertions passing; the counts and conventions are in its sealed JSON.
* The copied input SHA-256 manifest verified all fourteen dossier files.
* The Git whitespace check passed. New output text was additionally checked directly for trailing whitespace, control characters and final newlines.
* The output SHA-256 manifest seals this report, the checker, its JSON, and the copied input manifest, and is verified after creation. No sealed output is subsequently changed.

The reproducible commands, run from the worktree named above, are:

    python3 AUDITS/BLIND_RECONSTRUCTION/round007_gradient_exact_checks.py
    shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_007_GRADIENT_INPUT_SHA256SUMS.txt
    git diff --check
    shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_007_GRADIENT_OUTPUT_SHA256SUMS.txt

Only this isolated worktree has new outputs. Its creation added the requested Git worktree/branch metadata; no mathematical root file, canonical ledger, older report, or immutable input was edited. No commit, push, dependency installation, or child worker occurred. The bounded dossier overrides broad orientation reading. This report is a Markdown mathematical artifact; no TeX source is modified and the final handoff contains no mathematical LaTeX.

Root may now compare the sealed reconstruction with the separately constructed candidate. That comparison and the separate hostile review remain distinct duties. The campaign mission and the excluded singular particle-domain step remain open.
