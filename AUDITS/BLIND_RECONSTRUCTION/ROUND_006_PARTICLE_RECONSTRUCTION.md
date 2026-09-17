# TASK-046: statement-only reconstruction of THM-026

2026-09-17 UTC. **Verdict: every assertion in the frozen THM-026 card is reconstructed below.** No counterexample or unsupported line remains within that card's fixed-parameter scope. This is an independent statement-only reconstruction, not the constructor's self-check and not a substitute for its separately required hostile audit. No singular corrector-domain assertion is proved.

The worker started from published R4 commit `93c20daa45aad455a95437b1dc6beed2883afada` in `/Users/matthewrosenzweig/.codex/worktrees/hocf-r006-particle-blind`, branch `codex/hocf-r006-particle-blind`. The six permitted inputs were copied byte for byte and checked against `ROUND_006_PARTICLE_INPUT_SHA256SUMS.txt` before reconstruction. TASK045, its constructor proof, the periodic singular proof, other reviews, state/history, and memory were not read. Of THM-021 and its permitted complete memorandum, only the local kernel, heat-kernel, and divergence facts are mathematical inputs here. No particle construction or law-transfer conclusion is imported from it. The bounded task's input/output restrictions take precedence over the general instruction to open further repository documents or edit canonical ledgers. No root working-tree file, immutable input, canonical ledger, dependency, commit, or remote is changed.

## 1. Assertion, negation, prerequisites, and constants

The primary assertion is the entire conjunction in the frozen `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md`: for each fixed admissible parameter tuple and every distinct initial configuration there is a global collision-free pathwise unique measurable realization; it has the stated deterministic-time conditional Markov property, heat approximation, stopped energy estimate, and bounded-density law domination. Its exact negation is one admissible tuple, start, or initial density for which any one of these conclusions fails.

Fix an integer \(d\geq3\), \(0<s\leq d-2\), \(N\geq2\), \(0\leq\nu<\infty\), a smooth real periodic potential \(V\), and a finite horizon \(T\). The torus has Haar mass one. The Brownian motions \(W_1,\ldots,W_N\) are independent standard \(d\)-dimensional Brownian motions. Random initial conditions, when used, are independent of these Brownian motions. Equivalently one can work with an initial sigma field independent of their future increments. No exchangeability is required.

The frozen convention, unchanged here, is

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=\pi^{s-d/2}
 \frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d},
 \quad k\ne0,
 \qquad K=-\nabla g,\quad b=-\nabla V.
 \tag{1}
\]

The local facts supplied and proved by the permitted THM-021 memorandum, sections 2, 3, and 5, are as follows:

- \(g\in L^1\), is real and even, is smooth away from the origin, and locally \(g(z)=|z|^{-s}+h(z)\), where \(h\) is smooth and the coefficient of the power is exactly one.
- \(K\in L^1\), is odd, and is the distributional negative gradient of \(g\).
- \(D=\operatorname{div}K\) is a finite signed measure with \(D\geq-\kappa\,dz\) for some finite \(\kappa\geq0\). Below Coulomb, \(D=s(d-2-s)g_{s+2}\,dz\). At Coulomb,

\[
 D=c_d(\delta_0-dz),\qquad
 c_d=(d-2)|\mathbb S^{d-1}|,
 \quad \kappa=c_d\text{ is admissible}.
 \tag{2}
\]

- The frozen heat regularization is \(g_\varepsilon=p_\varepsilon*g\), with multiplier \(e^{-4\pi^2\varepsilon|k|^2}\). The periodized Gaussian \(p_\varepsilon\) is positive and has mass one. Thus \(K_\varepsilon=p_\varepsilon*K\), \(D_\varepsilon=p_\varepsilon*D\), and \(D_\varepsilon\geq-\kappa\) pointwise.

This use of the prerequisite retains its exact full periodic compensation. In particular the Coulomb classical Laplacian away from zero is \(\Delta g=c_d\), not zero. The local flux gives the atom in (2); the zero Fourier mode and constant nonzero Fourier coefficients identify the compensating constant. Below Coulomb the gamma recurrence gives
\(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\).
The local Gaussian representation in the permitted proof checks the coefficient one in (1). No logarithmic limit, unverified source theorem, or literature or novelty claim is used. The remainder of this reconstruction uses finite sums, ordinary differential equations with globally Lipschitz coefficients, smooth stopped Itô calculus, Brownian independent increments, and elementary measure arguments; the needed constructions are given below.

Choose any finite \(a\geq0\) with \(\operatorname{div}b\geq-a\); for example \(a=\max(0,\sup\Delta V)\). Put

\[
 C=Na+(N-1)\kappa.
 \tag{3}
\]

The constants below may depend on this fixed tuple. No uniformity in \(N,\nu\), the starting configuration, or a family of potentials is asserted.

Write \(r(z)=\operatorname{dist}_{\mathbb T^d}(z,0)\), and define

\[
 B=\max\left(0,\sup_{z\ne0}\{r(z)^{-s}-g(z)\}\right),
 \qquad v_-=\max(0,-\min V),
 \qquad c_N=1+Nv_-+\frac{N-1}{2}B.
 \tag{4}
\]

The number \(B\) is finite: near zero the expression in braces equals \(-h\); away from zero it is bounded on a compact set. The cut locus causes no problem because only continuity of the torus distance is used, never its derivatives. The shift \(c_N\) is explicitly nonnegative and depends only on the fixed data and \(N\).

Let

\[
 \mathcal O=\{X=(x_1,\ldots,x_N):x_i\ne x_j\ (i\ne j)\},
 \quad \delta(X)=\min_{i<j}r(x_i-x_j),
\]

\[
 H(X)=\sum_iV(x_i)+\frac1N\sum_{i<j}g(x_i-x_j),
 \qquad U(X)=H(X)+c_N.
 \tag{5}
\]

All gradients and Laplacians of \(H\) below are classical derivatives on the open set \(\mathcal O\).

## 2. Exact finite-N algebra and coercivity at every collision pattern

Evenness of \(g\) gives, for each particle,

\[
 \nabla_iH=\nabla V(x_i)+\frac1N\sum_{j\ne i}\nabla g(x_i-x_j).
 \tag{6}
\]

For a summand whose lower label is \(j<i\), differentiation in the second coordinate gives \(-\nabla g(x_j-x_i)=\nabla g(x_i-x_j)\). Therefore the full particle drift is exactly \(\mathcal B=-\nabla_XH\); no pair self-interaction is present. The generator on \(\mathcal O\) is

\[
 Lf=\nu\Delta_Xf-\nabla_XH\cdot\nabla_Xf.
 \tag{7}
\]

Each unordered interaction is differentiated in two distinct particle coordinates. Consequently

\[
 \Delta_XH=\sum_i\Delta V(x_i)
            +\frac2N\sum_{i<j}\Delta g(x_i-x_j)
 \leq Na+\frac2N\frac{N(N-1)}2\kappa=C.
 \tag{8}
\]

The coefficient is **\(2/N\)** for the full \(Nd\)-dimensional trace. Since \(D\geq-\kappa\,dz\) and its restriction off zero has smooth density, \(-\Delta g\geq-\kappa\) pointwise there. The measure inequality supplies precisely the classical inequality used in (8). It does not authorize evaluation of a delta measure on a particle trajectory.

For clarity, the whole force square in (7) has expansion

\[
\begin{split}
 |\nabla_XH|^2
 &=\sum_i|\nabla V(x_i)|^2
 +\frac2N\sum_{i<j}
    [\nabla V(x_i)-\nabla V(x_j)]\cdot\nabla g(x_i-x_j)\\
 &\quad+\frac1{N^2}\sum_i\sum_{j\ne i}\sum_{k\ne i}
       \nabla g(x_i-x_j)\cdot\nabla g(x_i-x_k).
\end{split}
 \tag{9}
\]

The last sum retains \(j=k\) and \(j\ne k\). It is the sum of squared total interaction forces after grouping by \(i\). Individual cross terms have no sign. No estimate drops those cross terms or asserts that each particle has a large force in a colliding cluster.

The required simultaneous-collision coercivity is instead the direct energy inequality

\[
\begin{split}
 U(X)
 &=1+\sum_i[V(x_i)+v_-]
      +\frac1N\sum_{i<j}[g(x_i-x_j)+B]\\
 &\geq1+\frac1N\sum_{i<j}r(x_i-x_j)^{-s}
 \geq1+\frac{\delta(X)^{-s}}N.
\end{split}
 \tag{10}
\]

Every term in the first sum is nonnegative and every shifted pair term dominates its positive principal power. Thus all smooth periodic remainders are controlled simultaneously, including interactions between different clusters. If \(m\) pairs have distance at most \(r\), the right side is at least \(1+m/(Nr^s)\). A cluster of \(q\) particles contributes all \(q(q-1)/2\) internal pairs. In particular any partial or simultaneous collision forces \(U\to\infty\). This coercivity does not require a force lower bound; (8) is the reason energy coercivity alone suffices throughout the frozen exponent range.

## 3. Local measurable construction and the stopped identity

Here is a construction without importing a singular SDE theorem. Choose radii \(r_m=2^{-m-3}\). There are smooth periodic functions \(\chi_m(X)\) equal to one on \(\{\delta\geq r_m\}\) and zero in a neighborhood of the collision set: take the product over pairs of an even cutoff which is zero when \(r(z)\leq r_m/2\), one when \(r(z)\geq r_m\), and is defined radially inside the injectivity radius. The field
\(\mathcal B_m=\chi_m\mathcal B\), extended by zero near collisions, is smooth on the full product torus. It is globally Lipschitz on a periodic Euclidean lift.

For a continuous forcing path \(w\) starting at zero and a starting point \(x\), subtract \(\sqrt{2\nu}w_t\). The remaining equation is

\[
 Y_t=x+\int_0^t\mathcal B_m(Y_q+\sqrt{2\nu}w_q)\,dq.
 \tag{11}
\]

Picard iteration is a contraction on a sufficiently short interval determined by the Lipschitz constant. Successive intervals give a unique solution on every finite horizon. Boundedness prevents finite-time escape of the lift; projection gives a torus path \(F^m(x,w)\). Gronwall applied to two initial points and two forcing paths proves continuity of the solution map into continuous paths on each compact time interval, in local lifts; periodicity gives the corresponding torus statement. In particular it is jointly Borel in \(x,w\), is nonanticipating, and for Brownian forcing is a strong adapted solution of the smooth equation. This includes \(\nu=0\).

Define \(\tau_m\) to be the first time \(\delta(F^m_t)\leq r_m\), with \(\tau_m=0\) if the initial distance already satisfies that inequality. The hitting times are measurable in \(x,w\). For \(n>m\), uniqueness applied while the distance exceeds \(r_m\) gives
\(F^n=F^m\) on \([0,\tau_m]\) and \(\tau_n\geq\tau_m\). Indeed \(F^n\) cannot hit the smaller threshold before reaching the larger one. The locally consistent paths therefore define a solution \(X_t\) for \(t<\tau_\infty:=\lim_m\tau_m\). On every compact subset of \(\mathcal O\) the vector field is bounded and Lipschitz; if a finite lifetime stayed in such a set, the integral equation and continuity of Brownian forcing would provide a limit and a continuation. Thus the only possible finite lifetime is approach to the collision set.

For a fixed starting configuration \(x\in\mathcal O\), let \(\tau_r\) be the first time the local path reaches \(\delta\leq r\), with value zero if it starts there. For \(r<\delta(x)\), this can be constructed using any smooth cutoff with threshold smaller than \(r\). Before stopping the path lies in a compact subset where \(H\), its first two derivatives, and the drift are bounded. A smooth extension agreeing with \(H\) in a neighborhood of that subset makes ordinary Itô calculus applicable. It gives the exact identity

\[
\begin{split}
 U(X_{t\wedge\tau_r})
 &+\int_0^{t\wedge\tau_r}|\nabla_XH(X_q)|^2\,dq\\
 &=U(x)+\nu\int_0^{t\wedge\tau_r}\Delta_XH(X_q)\,dq+M_{t,r},\\
 M_{t,r}&=\sqrt{2\nu}\sum_i\int_0^{t\wedge\tau_r}
                 \nabla_iH(X_q)\cdot dW_i(q),\\
 [M_{\cdot,r}]_t&=2\nu\int_0^{t\wedge\tau_r}|\nabla_XH(X_q)|^2\,dq.
\end{split}
 \tag{12}
\]

At each fixed \(r\), boundedness of the stopped integrand proves that the stochastic integral is square integrable, has mean zero, and has the displayed bracket. All other terms in (12) are integrable. For starts with \(\delta(x)\leq r\), the identity reduces to the initial value and zero integrals. No assumption about expected singular force at an unstopped time has been used.

Taking expectations gives

\[
 \mathbb E_x U(X_{t\wedge\tau_r})
 +\mathbb E_x\int_0^{t\wedge\tau_r}|\nabla_XH(X_q)|^2\,dq
 \leq U(x)+\nu C\,\mathbb E_x(t\wedge\tau_r)
 \leq U(x)+\nu Ct.
 \tag{13}
\]

An equivalent, useful nonnegative version of the same stopped equality is

\[
\begin{split}
 \mathbb E_x U(X_{t\wedge\tau_r})
 &+\mathbb E_x\int_0^{t\wedge\tau_r}|\nabla_XH|^2\,dq\\
 &+\nu\mathbb E_x\int_0^{t\wedge\tau_r}(C-\Delta_XH)\,dq
 =U(x)+\nu C\,\mathbb E_x(t\wedge\tau_r).
\end{split}
 \tag{14}
\]

For \(\nu=0\), the third term and the martingale are simply absent.

## 4. Quantitative noncollision, global uniqueness, and energy integrability

On \(\{\tau_r\leq t\}\), (10) bounds the terminal stopped energy below by \(1+1/(Nr^s)\). If the start is outside the stopping region, continuity gives distance exactly \(r\) at the first hit. If it starts inside, (10) is stronger. Hence

\[
 \boxed{\displaystyle
 \mathbb P_x(\tau_r\leq T)
 \leq\frac{U(x)+\nu CT}{1+1/(Nr^s)}
 \leq Nr^s[U(x)+\nu CT].}
 \tag{15}
\]

In particular, apply (15) to \(r_m\) and use \(\tau_m\uparrow\tau_\infty\). For every finite \(T\),
\(\mathbb P_x(\tau_\infty\leq T)=0\).
The union over positive integer horizons gives a global solution almost surely for each fixed \(x\). Compactness of each time interval and continuity of \(\delta(X_t)>0\) then imply

\[
 \min_{0\leq t\leq T}\delta(X_t)>0
 \quad\text{almost surely for each fixed }x,T.
 \tag{16}
\]

This conclusion concerns a finite horizon. It is not a positive lower bound independent of time, start, or Brownian sample.

Two solutions driven by the same Brownian motions and start agree up to each exit from a compact subset of \(\mathcal O\), by the local Lipschitz integral equation. Noncollision makes those exit times exhaust every finite horizon almost surely. This proves pathwise uniqueness among global collision-free solutions, and the local construction shows that no finite collision or finite maximal lifetime can occur for any solution satisfying the equation up to its lifetime.

For completeness the removal of stopping also yields genuine integrability, not only a formal expected energy bound. On the full-probability noncollision set, for fixed \(t\), eventually \(\tau_m>t\). Fatou and monotone convergence in (14) give

\[
 \mathbb E_xU(X_t)
 +\mathbb E_x\int_0^t|\nabla_XH|^2\,dq
 +\nu\mathbb E_x\int_0^t(C-\Delta_XH)\,dq
 \leq U(x)+\nu Ct.
 \tag{17}
\]

All three terms are nonnegative. The force integral in (17) makes the unstopped martingale square integrable. The stopped martingales converge to it in \(L^2\), since their remaining quadratic variations converge to zero in expectation. The other two increasing integral terms converge in \(L^1\) by their integrability, and \(t\wedge\tau_m\to t\) in \(L^1\). The pathwise version of (14), including the martingale, then shows convergence of the terminal energies in \(L^1\). Consequently (17) is in fact an equality. In particular,

\[
 \mathbb E_xU(X_t)+
 \mathbb E_x\int_0^t|\nabla_XH(X_q)|^2\,dq
 \leq U(x)+\nu Ct.
 \tag{18}
\]

When \(\nu>0\), (17) also justifies the expected integral of the negative part of the Laplacian. When \(\nu=0\), no such integrability is needed or asserted by the zero coefficient.

The shift is integrable under every bounded initial probability density \(F_0\). Indeed \(s<d\), \(g\in L^1\), its mean is zero, and

\[
 \int_{(\mathbb T^d)^N} U(X)\,dX=c_N+N\overline V<\infty,
 \qquad \overline V=\int_{\mathbb T^d}V.
 \tag{19}
\]

This number is positive by (10). If \(L_0=\|F_0\|_\infty\), then

\[
 \mathbb E_{F_0}U(X_0)
 \leq L_0(c_N+N\overline V)<\infty.
 \tag{20}
\]

Integrating the per-start stopped identities and bounds is justified by the measurable construction, independence of the driving Brownian motions, and the nonnegative terms in (14). Equations (13), (15), (17), and (18) hold with \(U(x)\) replaced by \(\mathbb E_{F_0}U(X_0)\). Thus the asserted energy bound is integrable under the exact stated law class. No iid hypothesis has been used.

## 5. Joint realization and the deterministic-time conditional Markov property

Here are the measurable-version details; a union of exceptional sets over uncountably many starts is not taken. Work on canonical continuous Brownian-path space \(\mathcal W=C_0([0,\infty);\mathbb R^{Nd})\) with its compact-open Borel sigma field and Wiener law. The cutoff solution maps and the hitting times constructed in section 3 are Borel in \((x,w)\). Define the Borel set

\[
 \mathcal G=\bigcap_{k\geq1}\bigcup_{m\geq1}\{(x,w):\tau_m(x,w)>k\}.
 \tag{21}
\]

For each fixed \(x\in\mathcal O\), the section \(\mathcal G_x\) has Wiener probability one by (15). On \(\mathcal G\), the cutoff paths are eventually identical on each compact time interval. Their limit is therefore a continuous path in \(\mathcal O\). Define \(\Phi(x,w)\) to be that path on \(\mathcal G\), and the constant path \(x\) on its complement. This is a Borel map into continuous torus paths: restrict to integer time intervals, use the eventual uniform limit of the Borel cutoff maps on \(\mathcal G\), and use the specified Borel constant map on its complement. Its evaluation \((t,x,w)\mapsto\Phi_t(x,w)\) is jointly Borel.

The locally constructed process before its lifetime is nonanticipating. For each fixed start, the path-valued version just defined differs from it only on a Wiener-null set. Thus on the usual completed Brownian filtration it is an adapted strong solution. For an independent random initial configuration the same conclusion holds after product-measure completion, because Fubini gives a null exceptional set for that initial law. This describes precisely how the continuous path-valued version and adapted realization are reconciled. It does not assert that the chosen null-set modification is nonanticipating for every exceptional deterministic pair \((x,w)\), or that one Brownian-null set works for all starts.

For bounded Borel \(f\) on \(\mathcal O\), let

\[
 P_tf(x)=\int f(\Phi_t(x,w))\,d\mathbb W(w).
 \tag{22}
\]

This is Borel in \(x\) by the Borel parameter integral. It is positive, preserves constants, and defines probability kernels. Fix a deterministic start, deterministic times \(s,t\geq0\), and let \(Y=\Phi_s(x,W)\). The increments \(\theta_sW(q)=W(s+q)-W(s)\) are independent of the completed past and have Wiener law. The measurable bad set in (21) satisfies

\[
 \mathbb P\{(Y,\theta_sW)\notin\mathcal G\}
 =\int\mathbb W(\mathcal G_y^c)\,\mathcal L(Y)(dy)=0.
 \tag{23}
\]

On the intersection of the original and restarted good events, \(q\mapsto\Phi_{s+q}(x,W)\) and \(q\mapsto\Phi_q(Y,\theta_sW)\) solve the same local integral equation with the same start and increments. Pathwise uniqueness gives equality on every finite interval. Conditional integration of the independent future increments now proves

\[
 \boxed{\displaystyle
 \mathbb E_x[f(X_{s+t})\mid\mathcal F_s]=P_tf(X_s)
 \quad\text{almost surely}.}
 \tag{24}
\]

The argument works equally for an independent random initial law. It also gives \(P_{s+t}=P_sP_t\). It proves the deterministic-time conditional Markov property exactly as stated. A stronger stopping-time theorem is unnecessary here and is not substituted for the argument at a random starting position.

## 6. Heat interactions converge for the same Brownian paths

First verify the off-collision approximation needed for trajectories. If \(A\) is compact in \(\mathbb T^d\setminus\{0\}\), choose a smooth cutoff \(\zeta\) equal to one in a neighborhood of \(A\), vanishing near zero. The function \(\zeta K\) is globally smooth. Its heat convolutions converge uniformly, with any fixed number of derivatives. The remainder \((1-\zeta)K\) is integrable and its support is separated from \(A\). On this separated set the periodized heat kernel and each derivative are bounded by a power of \(\varepsilon^{-1}\) times \(e^{-c/\varepsilon}\). Multiplication by \(\|K\|_1\) bounds the remainder convolution. Hence

\[
 K_\varepsilon\longrightarrow K
 \quad\text{in }C^1(A)\text{, and in fact in every fixed }C^j(A).
 \tag{25}
\]

Only uniform convergence on an off-collision neighborhood is needed below. An \(L^1\)-kernel limit alone would not be enough for this step.

Let \(X^\varepsilon\) solve the globally smooth heat-interaction equation with exactly the same initial point and Brownian motions as \(X\). Fix a Brownian sample for which \(X\) is collision-free on \([0,T]\), and put \(\rho=\min_{[0,T]}\delta(X_t)>0\). Compare Euclidean lifts with the same initial lifts and forcing, stopping when the maximum coordinate displacement first reaches \(\rho/4\). Up to this time every regularized pair has distance at least \(\rho/2\), and each straight comparison segment between the two close configurations stays away from all collisions. The singular drift has a finite Lipschitz constant \(L\) along these segments. Define

\[
 e_\varepsilon=
 \sup_{\delta(Z)\geq\rho/2}|\mathcal B_\varepsilon(Z)-\mathcal B(Z)|
 \longrightarrow0.
 \tag{26}
\]

Here either a fixed Euclidean product norm or the maximum coordinate norm may be used, with its finite-dimensional constant absorbed in \(L\) and \(e_\varepsilon\). Brownian terms cancel exactly in the difference equation. Gronwall gives, up to that stopping time,

\[
 \sup_{q\leq t}\max_i|X_i^\varepsilon(q)-X_i(q)|
 \leq t e^{Lt}e_\varepsilon.
 \tag{27}
\]

For every sufficiently small \(\varepsilon\), the right side at \(T\) is less than \(\rho/4\); continuity then prevents the stopping threshold from being reached. Equation (27) holds on the whole interval and converges to zero. This proves uniform-in-time almost-sure convergence as the full real parameter \(\varepsilon\downarrow0\), not merely along a subsequence, for every fixed start and tuple. The argument is deterministic on the good sample. Its constants and cutoff threshold depend on the realized separation \(\rho\); no uniform rate is claimed.

## 7. Actual bounded-density law passage

Let \(\mathcal B_\varepsilon\) be the smooth full \(N\)-particle drift. Oddness of \(K_\varepsilon\) and differentiation in both coordinates of each pair give

\[
\begin{split}
 \operatorname{div}_X\mathcal B_\varepsilon(X)
 &=\sum_i\operatorname{div}b(x_i)
   +\frac1N\sum_i\sum_{j\ne i}D_\varepsilon(x_i-x_j)\\
 &=\sum_i\operatorname{div}b(x_i)
   +\frac2N\sum_{i<j}D_\varepsilon(x_i-x_j)
 \geq-C.
\end{split}
 \tag{28}
\]

In the first line differentiation is only in the particle coordinate of the displayed drift component; the second line collects the two equal contributions. Positivity of heat convolution and the signed-measure lower bound justify \(D_\varepsilon\geq-\kappa\) even at Coulomb.

For every fixed continuous Brownian sample, subtract the additive translation as in (11). The resulting smooth time-dependent ODE has a globally defined spatial flow. Solving its time-dependent equation backwards from a terminal position constructs the inverse, so the map \(F_t^{\varepsilon,w}\) is a diffeomorphism of the product torus. Differentiating its integral equation in the initial point gives the variational equation. The determinant satisfies

\[
 J_t^{\varepsilon,w}(x)
 =\exp\left(\int_0^t
      \operatorname{div}\mathcal B_\varepsilon
       (F_q^{\varepsilon,w}(x))\,dq\right)
 \geq e^{-Ct}.
 \tag{29}
\]

No time derivative of Brownian motion is taken: the translated ODE has continuous time dependence, and spatial Brownian translations have derivative the identity. These facts apply without ellipticity, including \(\nu=0\).

Condition on the Brownian path and push forward the independent initial density \(F_0\). The change-of-variables formula and (29) give a conditional density bounded by \(L_0e^{Ct}\), where \(L_0=\|F_0\|_\infty\). Averaging retains the same bound. Equivalently, for every nonnegative continuous function \(f\) on the product torus,

\[
 \mathbb E f(X_t^\varepsilon)
 \leq L_0e^{Ct}\int f(X)\,dX.
 \tag{30}
\]

The collision set is Haar-null, so an initial probability density is supported on \(\mathcal O\) up to a null set. The joint measurability in section 5 and the per-start almost-sure convergence in section 6 allow Fubini over \(F_0(x)dx\): the same coupling with random initial data converges uniformly in time almost surely. Bounded convergence gives \(\mathbb E f(X_t^\varepsilon)\to\mathbb E f(X_t)\). Passing to the limit in (30) yields

\[
 \int f\,d\mathcal L(X_t)\leq L_0e^{Ct}\int f\,dX
 \quad(f\geq0\text{ continuous}).
 \tag{31}
\]

This is an actual law statement. To see explicitly that it gives domination on Borel sets, approximate the indicator of an open set \(O\) from below by the continuous functions
\(\min(1,n\operatorname{dist}(X,O^c))\), handling the full torus separately. Monotone convergence gives (31) for open sets. Haar outer regularity then gives it for every Borel set. Thus
\(\mathcal L(X_t)\leq L_0e^{Ct}dX\).
The Radon–Nikodym density satisfies

\[
 \boxed{\displaystyle
 F_t(X)\leq\|F_0\|_\infty
       \exp\{[Na+(N-1)\kappa]t\}
 \quad\text{for Haar-almost every }X.}
 \tag{32}
\]

This argument neither identifies a singular classical Fokker–Planck solution nor assumes one. Weak law convergence plus a common measure domination is the precise passage. The bound is for each time and requires no simultaneous choice of pointwise density representatives.

For iid initial data \(\mu_0\leq M\), \(F_0=\mu_0^{\otimes N}\leq M^N\); the bound in (32) is therefore
\(M^N\exp\{[Na+(N-1)\kappa]t\}\).
Its exponential dependence on particle number is retained. It provides no uniform iid-moment estimate, no independence of the evolved coordinates, and no singular-corrector domain or fluctuation conclusion.

## 8. Independent falsification route and required edge cases

The following tests were performed from the statement and exact local algebra, independently of any TASK045 proof narrative. They search for failures of signs, finite-N factors, force coercivity, boundary compensation, exceptional-set handling, and law transfer. The accompanying checker supports the elementary finite-sum assertions; the analytical proof above is not replaced by computation.

**Two particles.** With constant external potential, set \(R=X_1-X_2\). Then

\[
 dR=K(R)\,dt+\sqrt{4\nu}\,dB,
 \qquad H=2V+\tfrac12g(R),
 \quad |\nabla_XH|^2=\tfrac12|\nabla g(R)|^2,
 \quad\Delta_XH=\Delta g(R).
 \tag{33}
\]

Thus the relative generator is \(2\nu\Delta_R+K\cdot\nabla_R\), and the energy drift is \(-|\nabla g|^2/2+\nu\Delta g\), exactly agreeing with (8) and (12). The energy martingale bracket is \(\nu\int|\nabla g(R)|^2\). Missing either ordered-pair contribution would fail this test.

**Three particles.** With constant \(V\), put \(u=\nabla g(x_1-x_2)\), \(v=\nabla g(x_1-x_3)\), \(w=\nabla g(x_2-x_3)\). Then

\[
 \nabla H=\tfrac13(u+v,-u+w,-v-w),
\]

\[
 |\nabla H|^2=\tfrac29
 (|u|^2+|v|^2+|w|^2+u\cdot v-u\cdot w+v\cdot w),
 \quad \Delta_XH=\tfrac23(\Delta g_{12}+\Delta g_{13}+\Delta g_{23}).
 \tag{34}
\]

The cross terms cannot be discarded term by term. This is an independent check on the exact coefficient \(1/N\) in the drift, \(2/N\) in the trace, and \(1/N^2\) in the force square.

**Zero diffusion.** At \(\nu=0\), there is no martingale and the ordinary chain rule gives \(dH/dt=-|\nabla H|^2\). Equations (10) and (15) imply collision avoidance for every deterministic start, with no stochastic threshold argument. The smooth Jacobian proof of (32) remains valid. An ellipticity-based proof would have left this case unsupported; the construction here does not.

**Constant potential and the Coulomb threshold.** For \(V\) constant and \(s=d-2\), equation (2) gives

\[
 \Delta_XH=(N-1)c_d\quad\text{on }\mathcal O,
 \qquad C=(N-1)c_d.
 \tag{35}
\]

For \(N=2,3\), the energy heating terms are respectively \(\nu c_d\) and \(2\nu c_d\), while the density exponents are \(c_d\) and \(2c_d\), without a factor of \(\nu\). Below the threshold the local principal Laplacian is \(s(s+2-d)|z|^{-s-2}\leq0\); at the threshold its classical local principal value is zero. The nonzero constant in (35) is the full periodic remainder and must remain. No argument silently continues this sign to \(s>d-2\).

**Partial and simultaneous close pairs.** Inequality (10) directly controls two disjoint close pairs, two separate colliding clusters, or an entire cluster; bounded negative remainders cannot cancel any of their divergent energies. A useful adverse test is three collinear particles at \(-r,0,r\) for the local principal kernel. The center particle's leading interaction force is exactly zero, while the leading interaction energy is

\[
 \frac{2+2^{-s}}{3r^s}\longrightarrow\infty.
 \tag{36}
\]

Thus an alleged lower bound forcing *each* particle force to diverge would be false. The reconstruction needs only the total nonnegative square and energy coercivity, and survives this cancellation. The checker also examines two close pairs and two close triples with exact rational coordinates and verifies the counting bound in (10) for the principal powers. These are local normalization and cancellation tests, not numerical solutions of the singular torus SDE.

**Measurability and density stress tests.** The invalid shortcut “a Brownian-full event for each deterministic start is full for a random start” is replaced by the measurable map and independent-increment Fubini calculation (23). The equally invalid shortcut “weak density limits are automatically bounded” is replaced by continuous-test measure domination (30)–(32). The smooth density proof works at zero diffusion and does not require a density from a fixed point. Neither deterministic starting configurations nor arbitrary singular initial measures are claimed to have a bounded density.

## 9. Per-claim verdict and remaining scope

| Frozen claim | Verdict and proof location |
|---|---|
| Exact full-particle energy, force, and trace | Reconstructed: (5)–(9), stopped identity (12), including the full \(2/N\) Laplacian coefficient and bracket. |
| Nonnegative shift and all collision patterns | Reconstructed: explicit (4), coercivity (10), probability estimate (15). No force cross-term positivity is assumed. |
| Global collision-free, pathwise unique realization from each distinct start | Reconstructed: cutoff construction in section 3, nonexplosion and uniqueness in section 4. |
| Joint measurability with per-start null-set convention | Reconstructed: explicit Borel set and path map (21); section 5 explains adaptation after completion. No universal exceptional set is asserted. |
| Deterministic-time conditional Markov property | Reconstructed: measurable probability kernel (22), random-restart calculation (23), identity (24). |
| Positive minimum pair distance on each finite realized horizon | Reconstructed: noncollision plus continuous minimum, (16). |
| Heat approximation with the same Brownian paths, uniformly in time almost surely | Reconstructed: off-collision kernel approximation (25), stopped comparison (26)–(27), valid for the full cutoff limit. |
| Stopped expectations and integrability under bounded initial density | Reconstructed: (12)–(20). The dissipation and martingale expectations are justified rather than presumed. |
| Singular time-marginal density bound with exact exponential dependence | Reconstructed: full divergence (28), smooth sample Jacobian (29), actual law passage (30)–(32). |
| Required exclusions | Preserved: logarithmic and attractive cases, non-gradient external drift, unbounded initial density, uniform-N law transfer, and every corrector/hierarchy conclusion remain outside this report. |

There is **no first unsupported line in the frozen THM-026 assertion after the stated local prerequisite is accepted**. The next unavailable inference is any claim that a singular pair-corrector gradient, its Itô formula, a residual, or a bracket is integrable along these particle paths with the required uniform estimates. Fixed-N positive path separation and the exponentially growing density bound do not establish that domain passage.

The independent reconstruction supports the exact frozen statement. Root comparison and the constructor's separate hostile audit remain separate steps. No canonical theorem status is changed by this worker.

## 10. Reproducibility and seal

The standard-library checker `check_round006_particle_exact.py` uses rational Fourier coefficients and exact rational vector algebra. It differentiates a finite torus Fourier energy and separately assembles the ordered interaction drift and unordered trace at \(N=2,3,4,7\); it checks two- and three-particle force squares, a deliberately wrong trace coefficient, local cancellation, multiple close-pair counts, and sub-Coulomb/Coulomb signs. All 242 exact checks passed with Python 3.9.6. There is no random seed, floating-point tolerance, dependency installation, or probabilistic simulation. Its output is recorded in `ROUND_006_PARTICLE_CHECK_RESULTS.txt`. The checker is supporting algebraic evidence only.

The input and output SHA-256 manifests are `ROUND_006_PARTICLE_INPUT_SHA256SUMS.txt` and `ROUND_006_PARTICLE_OUTPUT_SHA256SUMS.txt`. The seal records the exact commands, outcomes, worktree, and unchanged base. All requested output files are in this isolated worktree's `AUDITS/BLIND_RECONSTRUCTION/` directory. The report is the requested Markdown mathematical artifact; no TeX source was edited, no unrelated build or campaign-wide verifier was run, and the final handoff contains no mathematical LaTeX requiring a separate compiled response.
