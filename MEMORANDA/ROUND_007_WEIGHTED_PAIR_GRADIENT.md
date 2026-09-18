# Round 007: weighted first derivatives of the full pair inverse

2026-09-17 UTC. TASK-049. Constructor `/root/r006_particle_domain`, working in the new branch `codex/hocf-r007-weighted-gradient` at `/Users/matthewrosenzweig/.codex/worktrees/hocf-r007-weighted-gradient`, based on published R4 commit `93c20daa45aad455a95437b1dc6beed2883afada`.

**PROVED_CANDIDATE / SELF_CHECKED.** This construction proves the frozen assertion in THM-027. Fresh statement-only reconstruction and hostile review remain required. The root disclosed the Jacobian/weight route; it is an unproved construction seed, not an independent-audit input. The expectation-differentiation step below includes an additional local simultaneous-flow argument, proved rather than presumed.

Exactly the fourteen files in `AUDITS/ROUND_007_WEIGHTED_GRADIENT_INPUT_SHA256SUMS.txt` were copied and verified before work. The task and THM-027 were read in full. Only the supplied dossier, its manifest, and this lane's outputs are used. The previous particle-domain worktree and its seal are untouched. No root edits, canonical ledger changes, commits, pushes, dependencies, external sources, memory, or child agents are involved.

## 1. Frozen assertion and source preflight

Use the unit Haar torus, Fourier characters \(e^{2\pi i k\cdot x}\), and the frozen coefficient-one periodic Riesz kernel

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d}
 \quad(k\ne0),\qquad K=-\nabla g.
 \tag{1.1}
\]

Fix \(d\geq3\), \(0<s\leq d-2\), \(N\geq2\), finite \(T\), and \(0\leq\nu\leq\nu_*<\infty\). The prescribed real data satisfy

\[
 \mu\in C([0,T];C^2),\quad \mu_t\geq0,\quad\int\mu_t=1,
 \qquad u\in C([0,T];C^1),\qquad f\in C([0,T];C^3).
 \tag{1.2}
\]

All spatial norms below are uniform over time. Write \(M_j=\sup_t\|D^j\mu_t\|_\infty\), \(U_j=\sup_t\|D^ju_t\|_\infty\) for \(j=0,1\), and \(F_j=\sup_t\|D^jf_t\|_\infty\). Derivative norms are Euclidean operator norms, and full pair gradients use the Euclidean norm on \(\mathbb R^{2d}\). No regularity of an unknown inhomogeneous reference solution is asserted.

On \(E=\{(x,y):x\ne y\}\), the auxiliary pair generator and source are

\[
 G_t=\nu(\Delta_x+\Delta_y)+u_t(x)\cdot\nabla_x+u_t(y)\cdot\nabla_y
 +\frac1N K(x-y)\cdot(\nabla_x-\nabla_y),
 \quad J_t=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)).
 \tag{1.3}
\]

The supplied THM-023 proof constructs a continuous, pathwise unique, jointly measurable noncolliding process from every fixed state in E and its deterministic-time Markov evolution \(S_{t,a}\). Its absolute J occupation has a bounded potential for fixed N. THM-021 supplies the exact responses, and THM-024/025 and their interface addendum supply the unique bounded Borel terminal-zero inverse

\[
 \Phi_t=U_t+\int_t^T S_{t,a}(R_a\Phi_a)\,da,
 \qquad U_t=\mathbb E_{t,x,y}\int_t^T J_a(X_a,Y_a)\,da,
 \quad R=R_x+R_y.
 \tag{1.4}
\]

The source/constant addendum explicitly identifies the local kernel premise with Section 2 of the complete R4 response proof, not just its short theorem card. That proof establishes

\[
 g(z)=|z|^{-s}+h(z),\quad h\in C^\infty(B_{1/3}),\quad h\text{ even},
 \quad K\in L^1,
 \tag{1.5}
\]

and, with \(D=\operatorname{div}K\),

\[
 D=s(d-2-s)g_{s+2}\,dz\quad(s<d-2),
 \qquad D=c_d(\delta_0-dz)\quad(s=d-2),
 \quad c_d=(d-2)|\mathbb S^{d-1}|.
 \tag{1.6}
\]

Its positive heat representation verifies the Fourier coefficient and the coefficient one in (1.5); the gamma recurrence gives \(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\), with \(4\pi^2c_{d,d-2}=c_d\) at Coulomb. These facts are imported only from their supplied complete proofs. The symmetry clarification means commutation with pair exchange, not Haar self-adjointness. The homogeneous Fourier subcase in the supplied interface proof satisfies (1.2) for every smooth terminal test.

For every \(1<q<d/2\), the assertion to prove is that \(\Phi_t\) has C1 spatial representatives on E, jointly Borel first derivatives, and

\[
 \sup_{0\leq t\leq T}\left(\|\Phi_t\|_\infty+
     \sup_E\frac{|\nabla_{x,y}\Phi_t|}{w_q(x-y)}\right)<\infty,
 \tag{1.7}
\]

uniformly over \(\nu\in[0,\nu_*]\), with finite constants permitted to depend on N and the displayed data. Those derivatives are global weak first derivatives of any diagonal extension, and \(\Phi_t\) has a uniform-in-time Haar H1 bound. The exact negation is admissible data or q violating one of these assertions. The construction below excludes that negation. It asserts no second/time derivative, particle generator-domain membership, singular Itô passage, N-uniform bracket estimate, or fluctuation limit.

## 2. Weights and the correct Jacobian eigenvalue

Fix \(R=1/16\). Let \(0\leq\chi\leq1\) be the smooth even radial cutoff equal to one on \(B_R\) and zero outside \(B_{2R}\), using the explicit smooth-step formula in the supplied R5 proof, Section 2. All radial formulas below live in this embedded chart; extension by zero or one is made before using the torus. Define

\[
 w_1(z)=\exp\{\chi(z)\log(1/|z|)\},\qquad w_\alpha=w_1^\alpha\quad(\alpha>0),
 \tag{2.1}
\]

and set \(w_1=1\) outside \(B_{2R}\). Thus \(w_\alpha\geq1\), it equals \(|z|^{-\alpha}\) on \(B_R\), and products of weights obey \(w_\alpha^p=w_{p\alpha}\) exactly. In particular no extra constant is silently added to the local power. Any other weight allowed in THM-027 is equivalent to this one, with finite comparison constants depending on that chosen weight; hence proving (1.7) for (2.1) proves the stated weight formulation.

Write \(k=-\nabla h\), \(H=\sup_{B_{2R}}\|Dk\|\), and

\[
 k_0=\frac{2s}{N},\quad L_0=U_1+\frac{2H}{N},\quad
 K_j=\sup_{\operatorname{dist}(z,0)\geq R}\|D^jK(z)\|\ (j=0,1),
 \quad L=\max\left(L_0,U_1+\frac{2K_1}{N}\right).
 \tag{2.2}
\]

Here \(k(0)=0\) by evenness, so \(|k(z)|\leq H|z|\). The relative drift on the inner ball is \(k_0r^{-s-2}z+a_t(x,y)\), where
\(|a_t(x,y)|\leq L_0r\). For the pair drift \(B_t\), the exact Jacobian block matrix is

\[
 DB_t=\begin{pmatrix}Du_t(x)&0\\0&Du_t(y)\end{pmatrix}
       +\frac1N\begin{pmatrix}DK(z)&-DK(z)\\-DK(z)&DK(z)\end{pmatrix}.
 \tag{2.3}
\]

For the principal force, \(DK=s r^{-s-2}[I-(s+2)e\otimes e]\), \(e=z/r\). In center/difference coordinates the principal block has eigenvalues zero in all center directions, \(k_0r^{-s-2}\) in each transverse difference direction, and \(-(s+1)k_0r^{-s-2}\) in the radial difference direction. The largest eigenvalue is the positive transverse value; the absolute matrix norm is larger by \(s+1\). They cannot be interchanged in this argument.

The symmetric part of the ordinary drift contributes at most \(U_1\); the smooth remainder contributes at most \(2H/N\) locally. With

\[
 c(z)=k_0\chi(z)r^{-s-2},\qquad \ell(z)=c(z)+L\geq0,
 \tag{2.4}
\]

extended by zero for c outside its chart, (2.2)--(2.3) show globally that
\(\lambda_{\max}(\operatorname{Sym}DB_t)\leq\ell\). Along a fixed noncolliding path the starting-state derivative \(A_{t,a}\) exists locally by C1 ordinary differential equations after subtraction of the additive noise. Its variational equation and the quadratic form bound give

\[
 \|A_{t,a}\|\leq\exp\left\{\int_t^a\ell(Z_r)\,dr\right\},\qquad Z_r=(X_r,Y_r).
 \tag{2.5}
\]

At this point (2.5) is only a pathwise local derivative statement. It is not used alone to differentiate an expectation.

## 3. Explicit weighted Feynman--Kac bounds

The following family is needed for both first derivatives and higher moments. Fix \(p\geq0\), \(\alpha>p\), and set

\[
 b_{p,\alpha}=(\alpha-p)k_0>0,\qquad
 a_\alpha=2\nu_*\alpha(\alpha+2-d)_+.
 \tag{3.1}
\]

On \(r\leq R\), direct differentiation in the relative variable gives

\[
 \frac{(G_t+p\ell)w_\alpha}{w_\alpha}
 \leq-b_{p,\alpha}r^{-s-2}+a_\alpha r^{-2}+\alpha L_0+pL.
 \tag{3.2}
\]

The diffusion term before its upper bound is exactly
\(2\nu\alpha(\alpha+2-d)r^{-2}\). The principal drift coefficient is \((p-\alpha)2s/N\), not an absolute-Hessian coefficient. In particular with \(\alpha=pq\) it is \(p(1-q)2s/N<0\).

Define the explicit finite maximum

\[
 M_s(a,b)=\begin{cases}
 0,&a=0,\\
 \displaystyle\frac{s}{s+2}\,a
       \left(\frac{4a}{(s+2)b}\right)^{2/s},&a>0.
 \end{cases}
 \tag{3.3}
\]

Indeed \(a v^2-(b/2)v^{s+2}\) on \(v\geq0\) is maximized where
\(v^s=4a/((s+2)b)\), and its maximum is (3.3). Thus (3.2) is at most
\(\alpha L_0+pL+M_s(a_\alpha,b_{p,\alpha})-(b_{p,\alpha}/2)r^{-s-2}\).

All cutoff terms are accounted for explicitly by finite annular constants

\[
 A_{\alpha,1}=\sup_{r\geq R}\frac{|\nabla_z w_\alpha|}{w_\alpha},\qquad
 A_{\alpha,2}=\sup_{r\geq R}\frac{|\Delta_z w_\alpha|}{w_\alpha},
 \tag{3.4}
\]

where the notation denotes the full torus complement of \(B_R\). Set

\[
\begin{split}
 C^{\rm out}_{p,\alpha}
 &=2\nu_*A_{\alpha,2}+(2U_0+2K_0/N)A_{\alpha,1}
      +p(L+k_0R^{-s-2}),\\
 C_{p,\alpha}
 &=\max\{C^{\rm out}_{p,\alpha},
       \alpha L_0+pL+M_s(a_\alpha,b_{p,\alpha}),0\}.
\end{split}
\tag{3.5}
\]

These are explicit coefficient choices in terms of fixed cutoff derivatives and finite displayed data norms. The entire pair generator, including ordinary transport and the periodic remainder, then satisfies

\[
 (G_t+p\ell)w_\alpha
 \leq C_{p,\alpha}w_\alpha
 -\frac{b_{p,\alpha}}2\,\mathbf1_{r\leq R}r^{-\alpha-s-2}.
 \tag{3.6}
\]

For example d=3 and q strictly between 1 and 3/2 give a positive first-moment diffusion coefficient \(2\nu q(q-1)\), but (3.3) controls it because s is positive. The cost can be severe: for positive \(a_\alpha\), (3.3) grows as \(N^{2/s}\) at fixed remaining data. Its exponential below is not claimed polynomial or bounded in N.

Stop the supplied noncolliding process before a collision tube. On each stopped compact set, all coefficients, weights, and the accumulated potential are bounded; ordinary stopped Itô calculus applied to

\[
 Y_a=e^{-C_{p,\alpha}(a-t)+p\int_t^a\ell(Z_r)dr}\,w_\alpha(Z_a)
 \tag{3.7}
\]

gives the inequality with the nonnegative terminal term and the nonnegative occupation term in (3.6) both retained. Let the stopping tube shrink. Noncollision is an imported proved premise. Fatou gives the terminal bound, and monotone convergence gives the positive occupation bound after the terminal term is discarded. In particular, with h equal to a horizon length at most T,

\[
 \mathbb E_{t,z}e^{p\int_t^{t+h}\ell}w_\alpha(Z_{t+h})
 \leq e^{C_{p,\alpha}h}w_\alpha(z),
 \tag{3.8}
\]

\[
 \mathbb E_{t,z}\int_t^{t+h}e^{p\int_t^a\ell}
       \mathbf1_{r_a\leq R}r_a^{-\alpha-s-2}\,da
 \leq\frac{2}{b_{p,\alpha}}e^{C_{p,\alpha}h}w_\alpha(z).
 \tag{3.9}
\]

There is no assumption of uniform integrability of the stopped weight, and no collision boundary value is set to zero. The lost term is nonnegative, which is the correct direction. Conditional Fatou applied to stopped versions also shows that Y is a nonnegative supermartingale.

We will use the following maximal consequence, rather than presume an exponential moment. Applying (3.7) with \((2p,2\alpha)\) and stopping at its first level crossing gives
\(\mathbb P(\sup Y>v)\leq\min(1,w_{2\alpha}(z)/v)\). Since the square of
\(e^{p\int\ell}w_\alpha\) is at most \(e^{C_{2p,2\alpha}h}\sup Y\), integration of this tail gives

\[
 \mathbb E_{t,z}\sup_{t\leq a\leq t+h}
        e^{p\int_t^a\ell}w_\alpha(Z_a)
 \leq2e^{C_{2p,2\alpha}h/2}w_\alpha(z).
 \tag{3.10}
\]

This proof of the maximal inequality is a stopped nonnegative-supermartingale argument; it does not invoke an unproved high moment of Y.

## 4. Nearby starts and differentiation of expectations

This section fills a gap that pointwise path differentiation alone would leave. For fixed initial time and horizon, each individual noncolliding path admits a neighborhood of initial states that stays in a common smooth region over that horizon. This follows from cutoff-flow continuous dependence and a positive minimum separation along the reference path. The neighborhood can depend on the driving path, and by itself does not justify a finite-difference interchange.

We first prove a simultaneous local-flow statement from (3.10). The maximal cutoff construction makes sense for every continuous driving signal, with lifetime \(\tau(z,w)\), whether or not that signal is exceptional. Let

\[
 F_m(z,w)=\min\left(m,\sup_{\substack{t\leq a\leq T\\a<\tau(z,w)}}w_1(Z_a(z,w))\right),
 \tag{4.1}
\]

interpreting the supremum up to an exploding endpoint as infinity. The actual horizon length is \(T-t\leq T\). The only possible finite-lifetime obstruction is a collision, so that convention agrees with the supremum before the endpoint.

For every fixed continuous signal, \(F_m\) is locally Lipschitz in z on E. To verify every case: if its untruncated supremum is below or equal to m, the trajectory remains in a compact collision-excluded region through the horizon, and its nearby-start flows are C1 with bounded derivative. The supremum of that uniformly locally Lipschitz family is locally Lipschitz, as is its minimum with m. If the untruncated supremum exceeds m, including an exploding path, a finite time before the lifetime already has weight greater than m. Continuous dependence up to that time makes \(F_m=m\) on a neighborhood of that start. This proves the assertion without assuming nonexplosion for all starts.

There is a finite explicit cutoff constant

\[
 C_w:=\sup_{z\ne0}\frac{|\nabla_{x,y}w_1(z)|}{w_2(z)}<\infty.
 \tag{4.2}
\]

For each fixed starting point, almost surely the supplied process is noncolliding, and the local Lipschitz gradient of (4.1), wherever it exists, is bounded by
\(C_w\sup_a e^{\int_t^a\ell}w_2(Z_a)\). The same supremum bounds its values up to a fixed constant, since \(w_1\leq w_2\) and \(\ell\geq0\). Thus for every finite \(P>2d\), (3.10) with \((p,\alpha)=(P,2P)\) proves a bound uniform in m for

\[
 \mathbb E\left[|F_m(z)|^P+|\nabla_zF_m(z)|^P\right]
 \leq2(1+C_w^P)e^{C_{2P,4P}T/2}w_{2P}(z).
 \tag{4.3}
\]

The gradient estimate is understood almost everywhere in the starting variable; Fubini applies to these locally Lipschitz functions and the measurable cutoff construction. On any coordinate ball with compact closure in E, the right side is uniformly bounded and integrable.

Here is the elementary spatial inequality needed to turn (4.3) into a simultaneous statement. Put \(n=2d\), let \(\omega_n\) be the volume of the Euclidean unit n-ball, let a coordinate ball have radius \(2b\), and take x in its concentric ball of radius b. Averaging the line-segment fundamental theorem over \(B_b(x)\), followed by polar integration, gives for every locally Lipschitz v

\[
 |v(x)|\leq(\omega_nb^n)^{-1/P}\|v\|_{L^P}
 +\frac1{n\omega_n}
 \left[\frac{n\omega_nb^{n-(n-1)P'}}{n-(n-1)P'}\right]^{1/P'}
       \|\nabla v\|_{L^P},\qquad P'=P/(P-1).
 \tag{4.4}
\]

The norms on the larger ball suffice. The gradient kernel in that averaging is \(|x-y|^{1-n}\); its stated integral is finite exactly because \(P>n\). This proves the needed Morrey-type supremum bound directly, with no flow-completeness theorem imported.

Integrate (4.3) over the larger starting ball. Fatou shows that the liminf, as m increases, of the random P-th powers of the two norms in (4.4) is finite almost surely. Apply (4.4) along a subsequence realizing that finite liminf. Since \(F_m\) increases with m, its supremum over m and over the smaller starting ball is finite almost surely. An exploding start in that smaller ball would instead have \(F_m=m\) for every m, a contradiction. A countable collection of such balls covers E. We have therefore proved, for each fixed initial time and finite horizon, a probability-one event on which every starting state in each such ball is noncolliding through the horizon.

Local cutoff uniqueness now implies that the actual flow on that event is C1 in the starting state. On a compact initial ball its image over the time interval stays uniformly away from the pair diagonal: the local flow is jointly continuous in initial state and time, and compactness gives a finite cover. This is a derived local simultaneous-flow property, not an assumption of a universal complete stochastic flow across all time/parameter choices.

We can now justify expectation derivatives. Suppose a random function \(H(z,w)\) is C1 in z on one of these initial balls almost surely, and its derivatives satisfy

\[
 \sup_{z\text{ in the ball}}\mathbb E|D_zH(z,W)|^p<\infty
 \quad\text{for some }p>1.
 \tag{4.5}
\]

The pathwise line-segment fundamental theorem and Jensen give the same p-th moment bound for every sufficiently short difference quotient. These quotients are uniformly integrable: their L1 tails above a level K are at most a common p-th moment bound times \(K^{1-p}\). Bounded truncation and that tail bound make their almost-sure derivative limit converge in L1, proving \(D\mathbb EH=\mathbb EDH\). If \(D_zH\) is pathwise continuous, (4.5) and the same uniform-integrability argument imply continuity of its expectation. This is the precise interchange used twice below. The required joint measurability follows from measurable cutoff variational equations, countable patching, and measurable parameter integration.

## 5. Base propagation and the singular source derivative

For a bounded C1 function F on E, define

\[
 |F|_q=\sup_E\frac{|\nabla_{x,y}F|}{w_q},\qquad
 \|F\|_{\mathcal X_q}=\|F\|_\infty+|F|_q.
 \tag{5.1}
\]

The weight is at least one. For terminal F, pathwise differentiation of the flow gives \(D_z[F(Z_a)]=A_{t,a}^T\nabla F(Z_a)\). For p greater than one, (2.5) and (3.8) with \(\alpha=pq>p\) give

\[
 \mathbb E|D_z[F(Z_a)]|^p
 \leq |F|_q^p e^{C_{p,pq}(a-t)}w_{pq}(z).
 \tag{5.2}
\]

This is uniform on compact initial balls, so Section 4 justifies the expectation derivative and its continuity. The first-moment bound with \((p,\alpha)=(1,q)\) then yields

\[
 \nabla S_{t,a}F=\mathbb E[A_{t,a}^T\nabla F(Z_a)],\quad
 |S_{t,a}F|_q\leq e^{C_{1,q}(a-t)}|F|_q,
 \quad \|S_{t,a}F\|_{\mathcal X_q}\leq e^{C_{1,q}(a-t)}\|F\|_{\mathcal X_q}.
 \tag{5.3}
\]

Sup-norm contraction supplies the last inequality's zero-th order part. No expectation derivative is inferred from pathwise differentiation without (5.2).

For J, direct coordinate differentiation gives

\[
\begin{split}
 \nabla_xJ&=DK(z)^T(\nabla f(x)-\nabla f(y))+D^2f(x)K(z),\\
 \nabla_yJ&=-DK(z)^T(\nabla f(x)-\nabla f(y))-D^2f(y)K(z).
\end{split}
\tag{5.4}
\]

Using (1.5), the absolute norm of the principal DK here is \(s(s+1)r^{-s-2}\). This use of an absolute norm for a source derivative is distinct from the largest eigenvalue used in (2.5). A sufficient explicit source-gradient constant is

\[
 C_J=\max\left\{\sqrt2 F_2[s(s+2)+2HR^{s+2}],
                  \sqrt2[2F_1K_1+F_2K_0]\right\}.
 \tag{5.5}
\]

Thus \(|\nabla J|\leq C_J r^{-s-1}\) on the inner ball and \(|\nabla J|\leq C_J\) outside it, uniformly in time. These bounds use only part of the stronger prescribed C3 regularity, so no missing third derivative is assumed.

For a moment parameter p at least one, choose any \(\alpha>p\) with
\(\alpha+s+2\geq p(s+1)\). Equations (3.8)--(3.9), with the outside-ball contribution bounded by \(w_\alpha\geq1\), give

\[
 \mathbb E\int_t^{t+h}e^{p\int_t^a\ell}|\nabla J_a(Z_a)|^p\,da
 \leq C_J^p e^{C_{p,\alpha}h}
       \left(h+\frac2{b_{p,\alpha}}\right)w_\alpha(z).
 \tag{5.6}
\]

On the inner ball, \(r^{-p(s+1)}\leq r^{-\alpha-s-2}\), since \(R<1\). Every term controlling this more singular occupation came from the retained negative term in (3.6).

Put \(I=\int_t^{t+h}\|A_{t,a}\||\nabla J_a(Z_a)|\,da\). Time Jensen and (5.6) imply

\[
 \mathbb EI^p\leq h^{p-1}C_J^p e^{C_{p,\alpha}h}
       \left(h+\frac2{b_{p,\alpha}}\right)w_\alpha(z).
 \tag{5.7}
\]

For uniform integrability one may choose explicitly \(p=2\) and \(\alpha=2(s+2)+1\); this satisfies both strict and weak inequalities above. On a compact initial ball the right side is uniform. The local simultaneous-flow property shows that the path integral defining U is C1 pathwise on that ball: along all those starts its integrand and derivative remain on a common compact smooth region over the finite time interval. Section 4 and (5.7) therefore prove

\[
 \nabla U_t(z)=\mathbb E_{t,z}\int_t^T A_{t,a}^T\nabla J_a(Z_a)\,da.
 \tag{5.8}
\]

The derivative is continuous off diagonal. Its joint Borel measurability in time/state follows from the measurable path/variational construction and integrable parameter integration. For its weighted first-moment bound use p=1 and \(\alpha=q\), which also satisfies the source exponent condition:

\[
 |U_t|_q\leq C_U:=C_J e^{C_{1,q}T}
       \left(T+\frac{2}{(q-1)k_0}\right).
 \tag{5.9}
\]

At terminal time the integral and its derivative are zero. On compact initial sets (5.7) with p=2 also bounds the expected derivative integral by a constant times \(h^{1/2}\), so no nonzero endpoint term is hidden as the remaining horizon shrinks. When T=0 the result is simply \(\Phi=0\); constants below can be replaced by zero.

For completeness, use the explicit zero-th order bound from the supplied R5 proof, Sections 2--5. With the same R and cutoff, let

\[
 L_b=U_1+H,\quad C_1=\|\nabla\chi\|_\infty,\quad C_2=\|\Delta\chi\|_\infty,
 \quad V_b=sR^{-s-1}+2RL_b,
 \tag{5.10}
\]

\[
\begin{split}
 B_J&=F_2HR^2+2F_1K_0,\quad a_b=1+sL_b,\\
 E_b&=sR^{-s}(2\nu_*C_2+V_bC_1)+4\nu_*C_1s^2R^{-s-1},\\
 B_b&=B_J+F_2E_b/a_b,\quad p_s=s+2,\quad c_s=2sp_s,\\
 B_N&=e^{a_bT}\left[\frac{F_2c_s^{2/p_s}}4N^{s/p_s}T^{2/p_s}+B_bT\right].
\end{split}
\tag{5.11}
\]

Its complete nonnegative barrier proof gives \(\sup_t\|U_t\|_\infty\leq B_N\), uniformly over the stated diffusivity interval. Hence \(\sup_t\|U_t\|_{\mathcal X_q}\leq B_N+C_U\). The imported supremum bound does not follow merely from the weighted derivative bound, and no such implication is used.

## 6. Two colliding convolution singularities

We give an elementary convolution estimate, since an assertion that these convolutions are globally bounded would be false when the two exponents sum to more than d. Let \(0<a<d\), \(0<q<d\), and
\(h_a(w)=\chi_a(w)|w|^{-a}\), with \(0\leq\chi_a\leq1\) supported in an embedded ball of radius \(R_a<1/3\). Write \(\sigma_d=|\mathbb S^{d-1}|\), \(\omega_d=\sigma_d/d\), and choose

\[
 H_a=\frac{\sigma_dR_a^{d-a}}{d-a},\quad
 B_q=\omega_d2^{-d}+\frac{\sigma_d2^{q-d}}{d-q},\quad
 C_{a,q}=R^{-q}\left[(1+2^q)H_a+2^aB_q\right].
 \tag{6.1}
\]

For \(z\ne0\), put \(\rho=\min(\operatorname{dist}(z,0),R)\). Split the w integral into a neighborhood \(\operatorname{dist}(w,0)<\rho/2\), the disjoint neighborhood \(\operatorname{dist}(w+z,0)<\rho/2\), and the complement. On the first and third pieces, the second singularity is at least \(\rho/2\) away, so \(w_q(w+z)\leq(1+2^q)\rho^{-q}\); their total integral against h is at most this number times \(H_a\). On the second piece, \(h_a(w)\leq2^a\rho^{-a}\), while
\(\int_{|v|<\rho/2}w_q(v)dv\leq B_q\rho^{d-q}\). Its contribution is at most \(2^aB_q\rho^{d-a-q}\leq2^aB_q\rho^{-q}\). Finally \(\rho^{-q}\leq R^{-q}w_q(z)\). Thus

\[
 \int h_a(w)w_q(w+z)\,dw\leq C_{a,q}w_q(z).
 \tag{6.2}
\]

This proof works whether \(a+q\) is below, at, or above d. It uses the essential hypotheses \(a<d\) and \(q<d\) separately. A bounded nonsingular remainder of size B contributes at most \(B W_qw_q(z)\), where

\[
 W_q:=\int w_q\leq1+\frac{\sigma_d(2R)^{d-q}}{d-q}<\infty.
 \tag{6.3}
\]

Choose a fixed cutoff \(\chi_a=\chi\) in the complete kernel decompositions. The supplied local expansion gives finite constants

\[
 B_K=\sup|K-s\chi z|z|^{-s-2}|,
 \qquad B_D=s(d-2-s)\sup|g_{s+2}-\chi|z|^{-s-2}|quad(s<d-2).
 \tag{6.4}
\]

Each displayed remainder extends boundedly across zero. These constants include all cutoff and periodic compensation terms. Consequently sufficient weighted convolution bounds are

\[
\begin{split}
 C_{K,q}&=sC_{s+1,q}+B_KW_q,\\
 C_{D,q}&=s(d-2-s)C_{s+2,q}+B_DW_q\quad(s<d-2),\\
 C_{D,q}&=c_d(1+W_q)\quad(s=d-2).
\end{split}
\tag{6.5}
\]

They satisfy \(\int|K(w)|w_q(w+z)dw\leq C_{K,q}w_q(z)\) and
\(\int w_q(w+z)|D|(dw)\leq C_{D,q}w_q(z)\). At Coulomb the latter is exact before the last inequality:
\(c_dw_q(z)+c_dW_q\). The atom is not discarded or differentiated.

## 7. Response derivatives, weak differentiation, and continuity

First note a general fact about \(\mathcal X_q\) for \(q<d\). Every bounded C1 function F on E with \(|F|_q<\infty\) has those spatial derivatives as global weak first derivatives. Integrate by parts after deleting \(|x-y|\leq\delta\). The boundary contribution against a smooth test is bounded by a constant times
\(\|F\|_\infty\delta^{d-1}\), which tends to zero. The pair-coordinate surface measure is at most \(2\sigma_d\delta^{d-1}\); there is no trace assumption on F. The bulk gradient is integrable because \(w_q\in L^1\). Dominated convergence proves the assertion on the full pair torus. Values on the diagonal are immaterial.

The supplied finite-measure response is exactly

\[
 R_xF(x,y)=-\int\mu(x+w)F(x+w,y)D(dw)
          -\int K(w)\cdot\nabla\mu(x+w)F(x+w,y)dw.
 \tag{7.1}
\]

Differentiate the translated products, not the singular measure. The full pair derivative is

\[
\begin{split}
 \nabla_{x,y}R_xF={}&-\int\nabla_{x,y}[\mu(x+w)F(x+w,y)]D(dw)\\
 &-\int\nabla_{x,y}[(K(w)\cdot\nabla\mu(x+w))F(x+w,y)]dw.
\end{split}
\tag{7.2}
\]

The first product derivative has a \((\nabla\mu F,0)\) term and a \(\mu\nabla_{x,y}F\) term. The second has a \((D^2\mu\,K(w)F,0)\) term and a \((K(w)\cdot\nabla\mu)\nabla_{x,y}F\) term. Both original responses and every such product term are retained. The y-slot formula follows by exchanging slots.

Here is the differentiation justification. The preceding weak-derivative fact, multiplication by C2 densities, and translation invariance imply globally integrable weak product derivatives. Fubini against the finite measure \(|D|\) and the L1 field \(|K|\) is justified by their total mass times the full pair L1 norm of those derivatives. Thus (7.2) is the global weak derivative as an L1 identity. At every off-diagonal point its integrals converge absolutely by (6.5).

The right side of (7.2) is continuous off diagonal. Near a fixed \((x_0,y_0)\) with difference \(z_0\ne0\), divide the w integration into small disjoint neighborhoods of zero and \(-z_0\), and their complement. Near zero, the translated F argument stays away from its diagonal; its derivatives are continuous and uniformly bounded, so the singular measure or K is an integrable dominating measure. Near \(-z_0\), change variable \(v=w+x-y\) to fix the F singularity at v=0. The measure density and K are smooth bounded functions of \(v-(x-y)\) there, while the derivatives of \(F(y+v,y)\) are bounded by a common constant times \(w_q(v)\in L^1\). Dominated convergence applies. On the remaining part both singularities are separated, with a fixed integrable bound. At Coulomb the atom is dealt with separately as a product at the actual off-diagonal point; the remaining measure is constant density. This proves continuity without assuming a diagonal trace or global boundedness of the convolution.

The response itself is continuous off diagonal by the same argument with bounded F. Its continuous weak derivative (7.2) is therefore its classical derivative there: local mollification makes both the function and these continuous derivative fields converge uniformly on smaller compact sets, and the fundamental theorem identifies the limit as C1. This also justifies all coordinate derivatives simultaneously.

Let \(D_0=\|D\|_{\rm TV}\), \(K_{L1}=\|K\|_1\), and set

\[
 C_{R,0}=2(M_0D_0+M_1K_{L1}),\qquad
 A_R=M_1D_0+M_2K_{L1}.
 \tag{7.3}
\]

Equations (6.5)--(7.2) give the full weighted bound

\[
 |RF|_q\leq2A_R\|F\|_\infty
      +2(M_0C_{D,q}+M_1C_{K,q})|F|_q.
 \tag{7.4}
\]

The factor two is the sum of the two responses, not a missing symmetrization. A sufficient operator constant is

\[
 C_{R,q}=C_{R,0}+2A_R+2(M_0C_{D,q}+M_1C_{K,q}),
 \qquad \|RF\|_{\mathcal X_q}\leq C_{R,q}\|F\|_{\mathcal X_q}.
 \tag{7.5}
\]

All terms are finite, uniform in time, and independent of the selected \(\nu\). Joint Borel measurability for time-dependent inputs and derivatives follows by the displayed parameter integrals. Off-diagonal values do not depend on diagonal representatives: D has no atom at any nonzero w, and its only possible atom is at zero, which samples F(x,y) when x differs from y.

## 8. Full inverse, local uniform derivative convergence, and H1

Use pointwise time integrals and the Volterra operator in (1.4). Every term \(V^kU\) is bounded Borel and C1 off diagonal. To justify this inductively, (5.3) and (7.5) give uniform local bounds on its derivatives; the path/response formulas are jointly Borel; differentiation under the time integral follows from the line-segment fundamental theorem and dominated convergence on each compact initial set. No separability or Bochner measurability of the weighted sup space is presumed.

On an ordered k-simplex the propagation exponents multiply to the exponent of the sum of the time intervals. Therefore, putting \(B_q^*=B_N+C_U\),

\[
 \|(V^kU)_t\|_{\mathcal X_q}
 \leq B_q^*e^{C_{1,q}(T-t)}
       \frac{[C_{R,q}(T-t)]^k}{k!}.
 \tag{8.1}
\]

The series \(\sum_{k\geq0}V^kU\) converges uniformly in values on the full off-diagonal space and locally uniformly in first derivatives, indeed uniformly after division by \(w_q\). The elementary closedness of the C1 class under these two local uniform convergences proves a C1 representative for every t. Derivatives are jointly Borel as limits of the explicit measurable derivative terms. The resulting bounded Borel solution of (1.4) agrees pointwise on E with the already unique inverse in THM-025; this identifies the newly proved regularity with that genuine full inverse, rather than with a different diagnostic kernel. Pair symmetry is preserved term by term.

A fully specified sufficient constant in (1.7), for positive T, is

\[
 C=(B_N+C_U)\exp\{(C_{1,q}+C_{R,q})T\},
 \tag{8.2}
\]

with every constituent fixed in (2.2), (3.1)--(3.5), (5.5), (5.9)--(5.11), (6.1)--(6.5), and (7.3)--(7.5). This is uniform over \(\nu\in[0,\nu_*]\). It may deteriorate exponentially in a positive power of N; no uniform N conclusion is attached to it.

Apply the weak-derivative argument at the beginning of Section 7 to the resulting bounded C1 representative. Because \(q<d\), its displayed derivatives are globally integrable weak derivatives. Since \(2q<d\), they are square integrable as well, and, with the convention that the H1 norm includes the full pair gradient,

\[
 \sup_t\|\Phi_t\|_{H^1(dx,dy)}^2
 \leq C^2\left[1+\int w_{2q}(z)dz\right]
 \leq C^2\left[2+\frac{\sigma_d(2R)^{d-2q}}{d-2q}\right].
 \tag{8.3}
\]

No diagonal trace is obtained from this argument. Arbitrarily changing diagonal values leaves the weak derivative and Haar H1 class unchanged. Terminal time is included by the zero function, with zero derivative.

## 9. Falsification checks and unresolved particle-domain line

The proof route uses one-sided Jacobian growth, weighted supermartingales, an explicitly proved nearby-start argument, and convolution of finite-measure responses. The separate exact algebraic checker tests the vulnerable signs, exponents, and factors without differentiating these displayed formulas by name. Its output is same-context supporting evidence, not an independent audit.

The tests include:

- d=3, s=1, and q=5/4 or 7/5. At positive noise the coefficient \(2\nu q(q+2-d)\) is positive; the exact maximization (3.3) still absorbs it. At zero noise that coefficient is zero, while the strict repulsive coefficient remains negative.
- The full pair-space principal block has center eigenvalue zero, radial eigenvalue \(-(s+1)k_0r^{-s-2}\), and transverse eigenvalue \(k_0r^{-s-2}\). Replacing the last by an absolute Hessian norm would destroy the claimed q-greater-than-one range and is not permitted.
- Finite N=2,3 and additional values, first and higher moment weights, and the source moment condition. In particular \(\alpha=pq\) produces exactly \(p(1-q)2s/N\), and the two relative Laplacians produce exactly the factor \(2\nu\).
- The Coulomb atom contributes a local multiplication term, not a diagonal trace. For homogeneous density, a pair Fourier character with frequencies k and l has response multiplier \(-[\widehat D(k)+\widehat D(l)]\), with \(\widehat D(0)=0\). Derivatives commute with these homogeneous responses; the negative sign and both slots agree with the supplied one-body Fourier solution.
- For a spatially constant f, J and its derivative vanish exactly, so U and the full inverse vanish by uniqueness. For constant F the two terms in (7.1) cancel by the distributional divergence identity even with nonconstant density; neither product term can be omitted.
- In (6.2), the near-second-singularity contribution has power \(\rho^{d-a-q}\). It can diverge as the separation tends to zero when \(a+q>d\). The proof only bounds it by a multiple of \(w_q\), which is valid because \(a<d\); it never asserts a bounded convolution.

The exact checker, README, verification record, and input/output seals accompany this memorandum. The construction has no unresolved step within the weighted first-derivative assertion as stated, subject to the required independent reviews.

The next unsupported particle-domain line is still substantive. The crude pointwise product of the internal singular force with the proved derivative behaves as

\[
 |K(x-y)|\,|\nabla\Phi(x,y)|\ \lesssim\ r^{-s-1-q}.
 \tag{9.1}
\]

At Coulomb, \(s=d-2\), this majorant is \(r^{-d+1-q}\), whose radial Haar integral diverges for every q greater than one. H1 controls a first weak derivative square, but it neither supplies second/time derivatives nor proves the integrability or cancellation needed for the full interacting particle drift. Thus inserting \(P_N[\Phi_t]\) into the N-particle Itô identity, identifying its drift and background contractions, and passing singular approximations for martingale brackets all remain unproved. A better directional cancellation or a separately justified extended-generator argument may address that line; it is not inferred here. The constants in (8.2) also provide no N-uniform martingale decay or evolved residual estimate.

No logarithmic normalization, parameter range, centering, law class, or limiting law is changed. This is a fixed-N first-derivative prerequisite for the existing genuine full pair inverse, and no larger campaign closure is claimed.
