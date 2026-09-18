# Round 006: finite-particle singular realization and heat passage

2026-09-17 UTC. TASK-045. Constructor: `/root/r006_particle_domain`. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r006-particle-domain`. Branch: `codex/hocf-r006-particle-domain`. Base: published R3 commit `52bda5d0d24067b051c6fe9763f2a78e7599e593`.

**Mathematical status: PROVED_CANDIDATE. Audit status: SELF_CHECKED; fresh reconstruction and hostile review required.** The finite-particle assertion in the task is established below, including zero diffusivity, every prescribed collision-free starting configuration, the Coulomb endpoint, the full finite-particle divergence constant, and the passage from smooth heat flows. This is a constructor report and assigns no independent certification to itself or to its prerequisites.

The actual six-file dossier is frozen in `AUDITS/ROUND_006_PARTICLE_REALIZATION_INPUT_SHA256SUMS.txt`. Each root byte string was checked against that manifest before copying, and each copied file was checked again. Only that dossier and its manifest were read. The task's restricted-input and single-writer instructions govern this lane in place of the general instruction to read later state/history. The root energy route was supplied as an unproved seed, not as an imported theorem. The R5 proof is used explicitly as an analogous method for measurable cutoff construction, random-flow Jacobians, and continuous-test measure passage; its two-particle result is not an input proving an N-particle assertion. No singular-SDE theorem, outside literature claim, private source, memory, other worker output, or new dependency is used.

## 1. Assertion, quantifiers, and exact negation

The torus is \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), with Haar measure of mass one and Fourier characters \(e^{2\pi i k\cdot x}\). Fix an integer \(d\geq3\), an exponent \(0<s\leq d-2\), an integer \(N\geq2\), a real smooth periodic function \(V\), and a finite \(\nu\geq0\). The zero-mean even Riesz kernel is frozen by

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=\pi^{s-d/2}
 \frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d},\quad k\ne0,
 \qquad K=-\nabla g,\quad b=-\nabla V.
 \tag{1.1}
\]

Let \(m_N\) be Haar measure on \((\mathbb T^d)^N\), and set

\[
 E_N=\{x=(x_1,\ldots,x_N):x_i\ne x_j\text{ for }i\ne j\},
 \quad \delta(x)=\min_{i<j}\operatorname{dist}_{\mathbb T^d}(x_i,x_j).
 \tag{1.2}
\]

The complement of \(E_N\) is \(m_N\)-null. Choose finite constants \(a,\kappa\geq0\) such that

\[
 \operatorname{div}b\geq-a,\qquad
 D:=\operatorname{div}K\geq-\kappa\,dx,
 \qquad C_N:=Na+(N-1)\kappa.
 \tag{1.3}
\]

Explicit admissible choices are given in Section 2. For independent standard d-dimensional Brownian motions, the assertion is that

\[
 dX_i(t)=\left[b(X_i(t))+
   \frac1N\sum_{j\ne i}K(X_i(t)-X_j(t))\right]dt
   +\sqrt{2\nu}\,dW_i(t)
 \tag{1.4}
\]

has a unique global continuous pathwise realization in \(E_N\), from every prescribed \(x\in E_N\), almost surely. Its maps and transition probability kernels are jointly Borel in time and state, and are obtained by a direct path construction. The solution is unique among continuous adapted solutions driven by the same Brownian motions; consequently its law is unique. There is no claim of a single probability-one noncollision event valid simultaneously for all starting states or all parameter tuples.

For every fixed tuple of parameters, starting state, and finite \(T\), the smooth heat equations with \(K_\varepsilon=p_\varepsilon*K\), the same initial state, and the same Brownian motions satisfy

\[
 \sup_{0\leq t\leq T}\max_i
 \operatorname{dist}_{\mathbb T^d}(X_i^\varepsilon(t),X_i(t))
 \longrightarrow0\quad\text{almost surely as }\varepsilon\downarrow0.
 \tag{1.5}
\]

This is convergence of the full family of heat parameters, not only a subsequence. Every such singular realization has

\[
 \inf_{0\leq t\leq T}\delta(X(t))>0
 \quad\text{almost surely}.
 \tag{1.6}
\]

The lower distance in (1.6) can depend on the realization, initial configuration, \(N,\nu,V,d,s,T\). At zero diffusivity a deterministic bound is given below.

If the initial state, independent of the Brownian motions, has a probability density \(F_0\in L^\infty(m_N)\), its law at every fixed time \(t\geq0\) has a density satisfying

\[
 0\leq F_t\leq\|F_0\|_\infty e^{C_Nt}
 \quad m_N\text{-almost everywhere}.
 \tag{1.7}
\]

For iid initial density \(0\leq\mu_0\leq M\), this becomes \(F_t\leq M^N e^{C_Nt}\). No exchangeability is needed for the general density assertion. This is a fixed-N estimate; the exponential and the iid factor are displayed and are not treated as uniform fluctuation estimates.

The logical negation is an admissible choice of the above parameters, starting state, or bounded initial density violating any included existence, uniqueness, measurability, collision, heat-passage, or density assertion. The proof below rules out that negation within exactly these hypotheses. Starting at collisions, logarithmic kernels, exponents above Coulomb, and non-gradient dynamics are not included. No uniform heat-passage rate or uniformly bounded energy input as diffusivity tends to infinity is asserted; the density exponent itself is independent of diffusivity.

## 2. Source and normalization preflight

The definition (1.1) and the deleted-label interaction coefficient \(1/N\) are exactly those of the frozen R1 model. Sections 2 and 3 of the supplied `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, summarized in the supplied THM-021 card, prove the following kernel facts. They are the only mathematical kernel inputs from that report:

\[
 g(z)=|z|^{-s}+h_s(z),\qquad h_s\in C^\infty(B_{1/3}),
 \quad g\in L^1,\quad K\in L^1,
 \tag{2.1}
\]

with g smooth off zero and local coefficient exactly one. Also

\[
 D=\begin{cases}
 s(d-2-s)g_{s+2}(z)\,dz,&0<s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \qquad c_d=(d-2)|\mathbb S^{d-1}|.
 \tag{2.2}
\]

The normalization can be checked directly in the supplied proof: with
\(\alpha_p=(d-p)/2\) and \(A_{d,p}=4^{(d-p)/2}\pi^{d/2}/\Gamma(p/2)\),

\[
 g_p(z)=A_{d,p}\int_0^\infty t^{\alpha_p-1}(p_t(z)-1)\,dt,
 \qquad
 A_{d,p}\int_0^\infty t^{\alpha_p-1}
 (4\pi t)^{-d/2}e^{-|z|^2/(4t)}\,dt=|z|^{-p}.
 \tag{2.3}
\]

Taking a nonzero Fourier coefficient of the first integral gives exactly (1.1). The gamma recurrence gives
\(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\) below Coulomb. At the endpoint it gives \(4\pi^2c_{d,d-2}=c_d\). Thus the positive Coulomb atom and the negative constant compensation in (2.2) are both retained. No substitution of zero into a positive-power formula is made.

Put

\[
 v_*:=\min V,\qquad g_*:=\inf_{z\ne0}g(z),\qquad
 a:=\max(0,\sup\Delta V).
 \tag{2.4}
\]

The number \(g_*\) is finite and attained away from zero: g tends to positive infinity at zero and is continuous on collision-excluded compact sets. Its zero mean and nonconstant singularity also imply \(g_*<0\). Sufficient choices in (1.3) are

\[
 \kappa=\begin{cases}
 s(d-2-s)\max(0,-\inf_{z\ne0}g_{s+2}(z)),&s<d-2,\\
 c_d,&s=d-2.
 \end{cases}
 \tag{2.5}
\]

These constants depend only on the frozen kernel and V, not on \(N,\nu\), or a heat parameter. If a value specified by an infimum is inconvenient, the explicit convergent heat-integral lower bound in the supplied R4 proof, Section 3.1, gives a larger admissible \(\kappa\). No optimization is required here.

On a punctured neighborhood, (2.2) implies the ordinary smooth inequality \(\Delta g\leq\kappa\). Indeed, restriction of the measure inequality to that open set is a smooth density inequality, hence holds pointwise. At Coulomb, the exact punctured identity is \(\Delta g=c_d\); the atom is not evaluated on a trajectory. Heat regularization instead retains it by convolution:

\[
 D_\varepsilon:=\operatorname{div}K_\varepsilon=p_\varepsilon*D
 \geq-\kappa.
 \tag{2.6}
\]

Sections 7--9 of the supplied R5 periodic-pair memorandum use the positivity of the periodized Gaussian, local convergence away from zero, and random-flow change of variables. They serve as explicitly acknowledged analogous methods. All finite-N identities and the collision Lyapunov function are established anew here. Basic finite-dimensional Picard iteration, smooth stopped Itô calculus, Brownian independent increments, Fatou/monotone/dominated convergence, and elementary finite-measure extension are used with their necessary bounds stated below. No imported singular existence statement is being applied.

## 3. Full energy, every partial collision, and the exact generator

Define on \(E_N\)

\[
 H_N(x)=\sum_i V(x_i)+\frac1N\sum_{i<j}g(x_i-x_j),
 \qquad
 \mathcal E_N(x)=H_N(x)-Nv_*-\frac{N-1}{2}g_*.
 \tag{3.1}
\]

The shift is explicitly of order N for fixed kernel and V. More importantly,

\[
 \mathcal E_N(x)=\sum_i(V(x_i)-v_*)
      +\frac1N\sum_{i<j}(g(x_i-x_j)-g_*)\geq0.
 \tag{3.2}
\]

All summands in (3.2) are nonnegative. If any one pair approaches a collision, its own shifted term diverges to positive infinity. The other terms cannot cancel it, even if several disjoint pairs or an entire cluster collide simultaneously. Therefore every sublevel \(\{\mathcal E_N\leq R\}\) is a compact subset of \(E_N\). This proves the required coercivity at every partial collision, with no assumption on the signs of pair-force cross products.

For an explicit distance comparison, fix \(r_0=1/4\) and let

\[
 A:=1+\sup_{|z|\leq r_0}|h_s(z)|+|g_*|>0.
 \tag{3.3}
\]

If \(\delta(x)\leq r_0\), select a minimizing pair in the local chart. Its term in (3.2), together with (2.1), gives

\[
 \mathcal E_N(x)\geq\frac{\delta(x)^{-s}-A}{N}.
 \tag{3.4}
\]

The harmless extra 1 in A prevents degenerate denominators. This is a global lower bound obtained from one pair, not a sum of estimates that could lose control at a cluster.

Write \(B=(B_1,\ldots,B_N)\) for the drift in (1.4). Differentiating each unordered pair in both coordinates and using evenness of g gives exactly

\[
 B_i=-\nabla_{x_i}H_N=b(x_i)+\frac1N\sum_{j\ne i}K(x_i-x_j),
 \quad B=-\nabla H_N,
 \tag{3.5}
\]

and

\[
 \Delta_{Nd}H_N
 =\sum_i\Delta V(x_i)+\frac2N\sum_{i<j}\Delta g(x_i-x_j)
 \leq Na+(N-1)\kappa=C_N.
 \tag{3.6}
\]

The factor \(2/N\) in (3.6) comes from the two differentiated coordinates of each unordered pair; it is not \(1/N\). Put

\[
 Q_N(x):=C_N-\Delta_{Nd}H_N(x)\geq0.
 \tag{3.7}
\]

For the smooth local generator \(L_N=B\cdot\nabla+\nu\Delta_{Nd}\) on \(E_N\),

\[
 L_N\mathcal E_N=-|B|^2+\nu\Delta_{Nd}H_N
 =\nu C_N-|B|^2-\nu Q_N.
 \tag{3.8}
\]

In particular the full square remains the full square. With \(K_{ij}=K(x_i-x_j)\), its exact expansion is

\[
\begin{split}
 |B|^2={}&\sum_i|b_i|^2+
 \frac2N\sum_i\sum_{j\ne i}b_i\cdot K_{ij}
 +\frac{2}{N^2}\sum_{i<j}|K_{ij}|^2\\
 &+\frac1{N^2}\sum_i
    \sum_{\substack{j,k\ne i\\j\ne k}}K_{ij}\cdot K_{ik}.
\end{split}
\tag{3.9}
\]

The ordered triple cross terms in the last line need not be nonnegative individually and are never deleted. Equation (3.8) uses only the nonnegativity of the complete square. In particular this proof does not infer a bound on the sum of individual squared pair forces from a bound on the squared total drift.

## 4. Direct local construction and stopped energy identities

Multiply K by even smooth cutoff functions so that the resulting force equals K for torus distance at least \(1/m\), is zero for distance at most \(1/(2m)\), and is smooth in between, for sufficiently large integer m. These are genuine local-chart cutoffs extended periodically; no torus cut-locus distance is differentiated. The resulting N-particle drift \(B^{(m)}\) is smooth, periodic, bounded, and globally Lipschitz. It need not be a gradient inside the cutoff region, where no singular energy identity is asserted.

For each continuous driving path \(w\), lift the initial configuration to Euclidean space and subtract \(\sqrt{2\nu}\,w\). The smooth-cutoff equation is a deterministic integral equation with a globally Lipschitz drift. Picard iteration gives a unique global solution: on a finite interval of length T its successive differences are bounded by a constant times \(L_m^{j-1}T^j/j!\), a summable series. Gronwall proves uniqueness. The torus solution does not depend on the integer lift. Iteration also makes the map Borel in starting state, driving path, and time, and nonanticipating. At \(\nu=0\) it is an ordinary deterministic flow.

For \(\delta(x)>1/m\), stop at the first exit from \(\{\delta>1/m\}\). Any finer cutoff gives the same solution up to that exit by uniqueness. The exit times increase with m, and the solutions patch to a maximal continuous adapted solution on \(E_N\), of lifetime \(\tau\). These exits, and the energy exits below, are stopping times because the cutoff solution is nonanticipating and continuous. The exit-time construction is jointly Borel: for a continuous path, entry/exit events are tested using infima over compact time intervals and countable rational times; countable patching preserves measurability. One can assign a cemetery value after \(\tau\) to obtain a map defined on every driving path, without declaring that the cemetery path is a solution of (1.4).

Only approach to the collision set can obstruct continuation. To check this explicitly, if a solution remains in a fixed collision-excluded compact set up to a finite time, the drift there is bounded. In Euclidean lifts the drift integral and the continuous driving path then have limits at that time. The limiting state is still collision-free, and a finer smooth cutoff continues the solution. No explosion of position or other boundary is available on the compact torus.

For \(R>0\), let

\[
 \sigma_R:=\inf\{t\in[0,\tau):\mathcal E_N(X(t))\geq R\},
 \tag{4.1}
\]

with \(\sigma_R=0\) when the initial energy is at least R and the usual infinite value for an empty set. Compactness of the energy sublevel just proved allows use of a fixed sufficiently fine cutoff up to \(\sigma_R\). Thus \(\sigma_R\uparrow\tau\) as \(R\uparrow\infty\): otherwise a bounded-energy path would have a finite nonextendible endpoint in a compact subset of \(E_N\), contradicting the preceding continuation argument.

For deterministic \(x\in E_N\), smooth Itô calculus on that stopped compact set gives the exact identity

\[
\begin{split}
 \mathcal E_N(X(t\wedge\sigma_R))
 &+\int_0^{t\wedge\sigma_R}|B(X(r))|^2\,dr
 +\nu\int_0^{t\wedge\sigma_R}Q_N(X(r))\,dr\\
 &=\mathcal E_N(x)+\nu C_N(t\wedge\sigma_R)+M_R(t),
\end{split}
\tag{4.2}
\]

where

\[
 M_R(t)=\sqrt{2\nu}\sum_i\int_0^{t\wedge\sigma_R}
        \nabla_{x_i}H_N(X(r))\cdot dW_i(r),
 \quad
 \langle M_R\rangle_t=2\nu\int_0^{t\wedge\sigma_R}|B(X(r))|^2\,dr.
 \tag{4.3}
\]

Every differentiated quantity in these formulas is bounded before the energy stop. The stopped stochastic integral is a true square-integrable martingale, so it has expectation zero. There is no singular global Itô formula or unproved uniform-integrability passage in this step. Equivalently, before replacing the Laplacian by its upper bound,

\[
 \mathbb E_x\mathcal E_N(X(t\wedge\sigma_R))
 +\mathbb E_x\int_0^{t\wedge\sigma_R}|B|^2
 =\mathcal E_N(x)+\nu\mathbb E_x\int_0^{t\wedge\sigma_R}\Delta_{Nd}H_N.
 \tag{4.4}
\]

In particular, for every finite \(T\),

\[
 \mathbb P_x(\sigma_R\leq T)
 \leq \min\left(1,\frac{\mathcal E_N(x)+\nu C_NT}{R}\right).
 \tag{4.5}
\]

At an energy exit starting below R, continuity gives energy exactly R; starting above R gives an immediate exit and an energy at least R. The other terms on the left of (4.2) are nonnegative, which proves (4.5) in either case.

Because \(\sigma_R\uparrow\tau\), (4.5) implies \(\mathbb P_x(\tau\leq T)=0\). Apply this for all positive integer T. The maximal solution is global and collision-free almost surely. Local pathwise uniqueness then proves global pathwise uniqueness. Any purported competing solution agrees with the cutoff construction until every collision-excluded exit; the probability-one global construction exhausts all finite horizons. This also proves uniqueness in law, since the solution is a measurable functional of the prescribed initial state and independent Brownian motions.

## 5. Global integrability, exact expectations, and distance exit bounds

The preceding conclusion first holds for each deterministic collision-free start. Its joint measurability lets it be integrated against any independent initial distribution supported on \(E_N\). Let that distribution have finite energy mean

\[
 J_0:=\mathbb E\mathcal E_N(X(0))<\infty.
 \tag{5.1}
\]

The stopped identity and bounds continue to hold with \(\mathcal E_N(x)\) replaced in expectations by \(J_0\). When the random initial energy is at least R the stop is zero, so the martingale integrand vanishes there; otherwise its bound is the bound on the same compact energy sublevel. Hence no unbounded-initial-state martingale claim is hidden in the integration.

Every expected occupation term containing \(\nu Q_N\) below means the expectation of the integral of the nonnegative function \(\nu Q_N\). At \(\nu=0\) it is identically zero without any convention multiplying zero by an infinite expectation of Q alone. Fatou's lemma for the nonnegative left side of (4.2) gives, after noncollision has been proved,

\[
 \mathbb E\mathcal E_N(X(t))+
 \mathbb E\int_0^t|B|^2+
 \nu\mathbb E\int_0^t Q_N
 \leq J_0+\nu C_Nt.
 \tag{5.2}
\]

All integrals have the limits of increasing stopping intervals. In particular \(\mathbb E\int_0^T|B|^2<\infty\). This is the needed integrability derived from stopping, not assumed in advance. It implies that the un-stopped stochastic integral

\[
 M(t)=\sqrt{2\nu}\sum_i\int_0^t\nabla_{x_i}H_N(X(r))\cdot dW_i(r)
 \tag{5.3}
\]

is square integrable and

\[
 \mathbb E|M(T)|^2=2\nu\mathbb E\int_0^T|B|^2
 \leq2\nu(J_0+\nu C_NT).
 \tag{5.4}
\]

Moreover \(M_R(T)\to M(T)\) in \(L^2\), since the expectation of the bracket on the omitted time interval tends to zero by dominated convergence of the integrable time integral. Pathwise localization therefore yields (4.2) without a stop. All its nonnegative terms are integrable by (5.2), so taking expectations now proves the exact equality

\[
 \boxed{\quad
 \mathbb E\mathcal E_N(X(t))+
 \mathbb E\int_0^t|B|^2+
 \nu\mathbb E\int_0^t Q_N
 =J_0+\nu C_Nt.\quad}
 \tag{5.5}
\]

For \(\nu>0\), this also proves integrability of \(\int_0^t|\Delta_{Nd}H_N|\), because \(\Delta H_N=C_N-Q_N\). When \(\nu=0\), the Laplacian occupation bound is neither needed nor inferred by dividing by \(\nu\); the pathwise exact formula is simply

\[
 \mathcal E_N(X(t))+\int_0^t|B|^2=\mathcal E_N(X(0)).
 \tag{5.6}
\]

All these statements concern the total interacting drift. In particular they do not claim square-integrability of each individual pair force at a fixed initial time.

There are also explicit distance exits. For \(0<\rho\leq r_0\) with \(\rho^{-s}>A\), put

\[
 \tau_\rho:=\inf\{t\geq0:\delta(X(t))\leq\rho\},
 \qquad b_\rho:=\frac{\rho^{-s}-A}{N}>0.
 \tag{5.7}
\]

If the initial separation is already at most \(\rho\), the stop is zero. Otherwise the stopped path remains in the compact set \(\delta\geq\rho\), so exactly the same stopped Itô identity is valid. At every exit (3.4) gives energy at least \(b_\rho\). Consequently

\[
 \mathbb P(\tau_\rho\leq T)
 \leq\min\left(1,\frac{N(J_0+\nu C_NT)}{\rho^{-s}-A}\right).
 \tag{5.8}
\]

In particular, for \(0<\rho\leq\min(r_0,(2A)^{-1/s})\),

\[
 \mathbb P\left(\inf_{0\leq t\leq T}\delta(X(t))\leq\rho\right)
 \leq\min(1,2N(J_0+\nu C_NT)\rho^s).
 \tag{5.9}
\]

No union bound with a missing number of pairs is used: the complete energy controls every collision event. These bounds also hold for deterministic initial x with \(J_0=\mathcal E_N(x)\).

For an individual global path, continuity in \(E_N\) on a compact time interval already gives (1.6). More explicitly, if \(S_T=\sup_{0\leq t\leq T}\mathcal E_N(X(t))\), then \(S_T<\infty\) pathwise and (3.4) gives

\[
 \inf_{0\leq t\leq T}\delta(X(t))
 \geq\min\left(r_0,(NS_T+A)^{-1/s}\right)>0.
 \tag{5.10}
\]

At \(\nu=0\), (5.6) lets one replace \(S_T\) by the deterministic initial energy in (5.10), for every T. For positive diffusivity the proof supplies the random bound (5.10) and the probability bound (5.8); it does not assert a deterministic separation shared by every Brownian realization.

For bounded-density initial data the finite-mean hypothesis (5.1) is automatic with an explicit constant. The nonnegative formula (3.2), the zero mean of g, and unit Haar mass give

\[
 \int\mathcal E_N\,dm_N
 =N\left(\int V-v_*\right)-\frac{N-1}{2}g_*=:I_N<\infty,
 \qquad J_0\leq\|F_0\|_\infty I_N.
 \tag{5.11}
\]

This proves every required energy and exit integrability statement for that initial law class before any density propagation is invoked. For iid \(\mu_0\leq M\) one may either use \(\|F_0\|_\infty\leq M^N\) in (5.11), or the sharper elementary estimate

\[
 J_0\leq N\|V-v_*\|_\infty+
           \frac{N-1}{2}M(-g_*).
 \tag{5.12}
\]

Indeed \(g-g_*\geq0\), its Haar integral is \(-g_*\), and integrating one of the two iid variables using \(\mu_0\leq M\), then the other using unit mass, bounds its expectation by \(M(-g_*)\). This does not change the evolved density factor in (1.7).

## 6. Joint measurable Markov laws

Let \(\Phi_t(x,w)\) be the maximal path map from Section 4, with a cemetery convention on explosion. On the Borel event of no explosion it is the increasing-domain limit of cutoff solutions; the nonexplosion event itself is Borel because the cutoff exit times are Borel. At each fixed starting state that event has Wiener probability one. Thus

\[
 P_tG(x):=\mathbb E[G(\Phi_t(x,W))],\qquad x\in E_N,
 \tag{6.1}
\]

defines a jointly Borel probability kernel in \((t,x)\) for bounded Borel G on \(E_N\). Measurability of the expectation follows by the monotone-class construction of parameter integrals from the joint Borel map. Values of G at the cemetery state do not affect (6.1).

Local uniqueness gives the deterministic restart identity before any lifetime. For the global Brownian solution, Brownian increments after a deterministic time a are independent of the past and have the original Wiener law. Conditional on the current state, the future path is the measurable restarted solution driven by these increments. A possible state-dependent exceptional set causes no problem: its conditional probability is zero at every fixed collision-free state, and integration of the jointly measurable indicator still gives zero. It follows that

\[
 \mathbb E_x[G(X(a+t))\mid\mathcal F_a]=P_tG(X(a)),
 \qquad P_{a+t}=P_aP_t,
 \tag{6.2}
\]

for bounded Borel G. This constructs the time-homogeneous Markov laws; no Markov property is inferred merely from a displayed generator. For arbitrary independent initial laws supported on \(E_N\), integrate these kernels against the initial law. A strong-Markov theorem at arbitrary stopping times is not required for, or imported into, the claimed result.

For completeness, the continuous-path laws can be made jointly measurable without requiring an exceptional-set choice uniform in x. On the joint Borel nonexplosion event use the actual full continuous path. On its complement assign the constant path with value x. The resulting map to continuous path space is Borel, since its evaluations at rational times are Borel and determine that path-space Borel structure. For each fixed x this modification changes nothing almost surely. The adapted solution is the original maximal construction, with any completion on its null explosion event; the artificial path on the exceptional event is not used to claim a deterministic solution for an arbitrary driving signal.

## 7. Same-noise heat passage

The torus heat kernel is

\[
 p_\varepsilon(z)=\sum_{n\in\mathbb Z^d}(4\pi\varepsilon)^{-d/2}
        e^{-|z+n|^2/(4\varepsilon)},\qquad K_\varepsilon=p_\varepsilon*K.
 \tag{7.1}
\]

It is nonnegative, has mass one, and has Fourier multiplier \(e^{-4\pi^2\varepsilon|k|^2}\), exactly the frozen regularization. The force \(K_\varepsilon\) is smooth and odd. Its smooth N-particle equation therefore has a global measurable solution for every continuous driving path by the same Picard construction; no collision avoidance is presumed for an arbitrary fixed heat parameter.

We need convergence stronger than convergence of distributions. On any compact set separated from zero, write \(K=K_{\mathrm{near}}+K_{\mathrm{far}}\), with a smooth periodic first term agreeing with K on a neighborhood of that compact set and an \(L^1\) second term supported a positive distance away. Convolution of the first term converges in \(C^1\) by the Gaussian approximate identity. Each derivative of the Gaussian in the convolution of the distant term is bounded by a polynomial in \(\varepsilon^{-1}\) times \(e^{-c/\varepsilon}\), uniformly on the given compact set. Multiplication by \(\|K_{\mathrm{far}}\|_1\) proves that term and its first derivatives tend to zero. Hence

\[
 K_\varepsilon\longrightarrow K\quad\text{in }C^1
 \text{ on each compact subset of }\mathbb T^d\setminus\{0\}.
 \tag{7.2}
\]

Fix x, the parameter tuple, and T. Work on the probability-one event that the singular trajectory is global. Choose \(0<\eta\leq1/8\) below its minimum separation over \([0,T]\). Use the same Euclidean lifts at time zero for the heat and singular solutions. Their Brownian terms cancel exactly in their difference equation.

Stop the difference if \(q_\varepsilon(t):=\max_i|X_i^\varepsilon(t)-X_i(t)|\) reaches \(\eta/4\). Up to this stop, every segment between the two lifted configurations has all torus pair distances at least \(\eta/2\). Let

\[
 e_\varepsilon=\sup_{\operatorname{dist}(z,0)\geq\eta/2}
                  |K_\varepsilon(z)-K(z)|\longrightarrow0,
 \quad
 L=\|Db\|_\infty+\frac{2(N-1)}N
   \sup_{\substack{\operatorname{dist}(z,0)\geq\eta/2\\0<\varepsilon\leq\varepsilon_0}}
                \|DK_\varepsilon(z)\|<\infty.
 \tag{7.3}
\]

Choose \(\varepsilon_0\) small using (7.2). For this maximum-particle norm, the factor 2 in L comes from the difference of the two arguments of each pair force. Direct subtraction of the equations and Gronwall give, before the stop,

\[
 \sup_{0\leq t\leq T}q_\varepsilon(t)
 \leq T\frac{N-1}{N}e_\varepsilon e^{LT}.
 \tag{7.4}
\]

For every sufficiently small \(\varepsilon\), the right side is below \(\eta/4\), so it prevents the stop. This proves (1.5) over the whole horizon, for the full heat-parameter limit. The good event is exactly the singular noncollision event for the fixed starting state; its validity does not require uniform noncollision estimates for the heat processes. In particular the heat trajectories eventually also stay separated on this coupled finite interval.

All constants used for the local comparison may depend on the path through \(\eta\). This is legitimate for the stated almost-sure fixed-data assertion and supplies no uniform-in-N convergence rate. Fubini also gives (1.5) for an independent random initial point with any law supported on \(E_N\).

## 8. Exact N-particle divergence and density domination

Let \(B^\varepsilon\) denote the smooth heat drift on the whole N-particle torus. Differentiate before estimating:

\[
\begin{split}
 \operatorname{div}_{Nd}B^\varepsilon(x)
 &=\sum_i\operatorname{div}b(x_i)
   +\frac1N\sum_i\sum_{j\ne i}D_\varepsilon(x_i-x_j)\\
 &=\sum_i\operatorname{div}b(x_i)
   +\frac2N\sum_{i<j}D_\varepsilon(x_i-x_j)
 \geq-Na-(N-1)\kappa=-C_N.
\end{split}
\tag{8.1}
\]

For the second equality D is even, as follows from evenness of g. Equivalently differentiating both coordinate contributions of one unordered pair gives the same sign twice. There are exactly \(N(N-1)/2\) unordered pairs. Thus this is the full N-particle exponent, not the two-particle exponent from the analogous R5 argument.

Fix a continuous Brownian driving path and \(\varepsilon>0\). The smooth additive-noise flow \(\Phi_t^\varepsilon\) is a \(C^1\) diffeomorphism of the N-particle torus. Here are the required details. Differentiate the uniformly convergent local Picard equations in the initial point, or apply their difference-quotient equations and Gronwall, using bounded first and second derivatives of the smooth drift. The resulting derivative solves

\[
 \dot J(t)=DB^\varepsilon(\Phi_t^\varepsilon(x))J(t),\quad J(0)=I.
 \tag{8.2}
\]

The coefficient is continuous in time. Solving the original additive integral equation backward from a terminal state, for this fixed continuous signal, gives the inverse flow; uniqueness verifies both inverse identities. The variational equation is invertible, and differentiating the determinant polynomial, or using its inverse equation, yields

\[
 \det D\Phi_t^\varepsilon(x)
 =\exp\left\{\int_0^t\operatorname{div}B^\varepsilon
                     (\Phi_r^\varepsilon(x))\,dr\right\}
 \geq e^{-C_Nt}.
 \tag{8.3}
\]

The determinant is positive. The additive Brownian term has no derivative in the initial point, so no additional Itô term enters this ordinary variational equation. This argument is equally valid at \(\nu=0\).

For every nonnegative Borel G on the full torus, change of variables for the smooth diffeomorphism gives, path by path,

\[
 \int G(\Phi_t^\varepsilon(x))\,dm_N(x)
 \leq e^{C_Nt}\int G\,dm_N.
 \tag{8.4}
\]

Multiply by \(F_0(x)\leq\|F_0\|_\infty\), then take Brownian expectation and use Tonelli. If \(\lambda_t^\varepsilon\) is the resulting probability law, this proves

\[
 \int G\,d\lambda_t^\varepsilon
 \leq\|F_0\|_\infty e^{C_Nt}\int G\,dm_N.
 \tag{8.5}
\]

The bound is uniform in the heat parameter and finite diffusivity. It was obtained from the actual random flow, without presupposing a solution of a Fokker--Planck equation.

The singular law \(\lambda_t\) is already defined by the measurable probability kernel in Section 6. For continuous G on the full compact torus, Section 7 and bounded convergence in Brownian paths give \(P_t^\varepsilon G(x)\to P_tG(x)\) for every \(x\in E_N\). A second bounded-convergence step against \(F_0\,dm_N\) is valid because \(E_N^c\) is null. Passing (8.5) to the limit therefore gives it for \(\lambda_t\) and nonnegative continuous G.

To extend this inequality to Borel sets without assuming what it is meant to prove, let O be open. The continuous functions \(\min(1,j\operatorname{dist}(z,O^c))\) increase to \(1_O\); use the constant function 1 if O is the whole torus. Monotone convergence proves the inequality for O. For a Borel set B, choose open supersets O with \(m_N(O)\) decreasing to \(m_N(B)\), using outer regularity of Haar/Lebesgue measure. Since \(\lambda_t(B)\leq\lambda_t(O)\), one obtains

\[
 \lambda_t(B)\leq\|F_0\|_\infty e^{C_Nt}m_N(B).
 \tag{8.6}
\]

Nonnegative simple functions followed by monotone convergence then give (8.5) for every nonnegative Borel G at the singular limit. In particular \(\lambda_t\) is absolutely continuous, and its Radon--Nikodym density satisfies (1.7). This proof uses neither convergence for arbitrary Borel terminal tests nor convergence of a singular source expectation. It also does not assert that the singular flow is onto or has a globally defined inverse.

For example, the resulting integrability for every nonnegative Haar-integrable configuration function f is exactly

\[
 \mathbb E f(X(t))\leq\|F_0\|_\infty e^{C_Nt}\|f\|_{L^1(m_N)}.
 \tag{8.7}
\]

The factor remains explicit. In particular g and K give finite pair-energy and first-force moments under the evolved law at each finite time, since they are integrable. Formula (8.7) does not make a nonintegrable derivative or force square integrable, and does not turn a merely bounded Borel pair kernel into an Itô test function.

## 9. Falsification route and checks

The proof route was the complete gradient energy and the smooth random-flow Jacobian. A separate algebraic falsification route differentiates raw local pair energies by exact rational automatic differentiation, then compares with a directly assembled coordinate force. It retains transverse derivatives even for collinear test configurations. This is algebraically separate from counting differentiated unordered pairs, but remains a same-context check and is not an independent audit.

The supporting standard-library checker is `VERIFICATION_CODE/round006_particle_realization_exact.py`; it writes `VERIFICATION_CODE/round006_particle_realization_exact_output.json`. It uses exact rational arithmetic, no numerical tolerance, random seed, or installed dependency. It checks the following vulnerable points.

1. For N=2 and N=3, and additional finite N, the full force is the negative derivative of \(\sum V+N^{-1}\sum_{i<j}g\), its divergence is minus the full Laplacian, and its square retains the ordered triple cross terms. Both constant and nonconstant local backgrounds are tested. Local polynomial backgrounds used in the checker test differential coefficients only; the theorem retains periodic V.
2. Coulomb cases \((d,s)=(3,1),(4,2),(5,3),(6,4)\) give zero punctured Euclidean Laplacian of the principal power. Sub-Coulomb tests give the nonpositive sign. The separate exact periodic calculation (2.2) restores the positive atom and, at the endpoint, \(\Delta g=c_d\) away from zero. The Euclidean tests are not silently substituted for the periodic compensation.
3. Triple-close configurations and two disjoint close pairs are tested. In a symmetric three-particle cluster the middle particle's total force vanishes while its individual pair forces do not. The negative middle-particle cross term is retained. The energy is still a sum of positive principal pair energies and diverges along either cluster collapse. This specifically challenges a false individual-force lower bound, which the proof does not use.
4. For the exactly solvable pure Euclidean two-particle model with constant V and \(\nu=0\), the relative separation satisfies

\[
 r(t)^{s+2}=r(0)^{s+2}+\frac{2s(s+2)}N t,
 \quad H_N=\frac1N r^{-s},\quad
 |B|^2=\frac{2s^2}{N^2}r^{-2s-2},
 \tag{9.1}
\]

where the actual two-particle equation has N=2. Thus \(dH_N/dt=-|B|^2\). The same local relative-coordinate identity is checked algebraically for a general coefficient \(1/N\) as a coefficient test only. With noise the relative generator has diffusion \(2\nu\), and its action on \(g/N\) gives \(-(2/N^2)|K|^2+(2\nu/N)\Delta g\), agreeing with the full-space energy formula. This catches both a missing pair derivative and a missing Brownian factor.
5. For constant V at the periodic Coulomb endpoint, (3.6) is exactly \(\Delta H_N=(N-1)c_d\), hence Q is identically zero with the choices \(a=0,\kappa=c_d\). The energy input in (5.5) is exactly \(\nu(N-1)c_dt\), and (8.1) is exactly \(-(N-1)c_d\) away from collisions. At \(\nu=0\), a forward singular map need not be onto the punctured configuration space, so a contracting local Jacobian is not in conflict with conservation of total probability. The proof correctly uses only smooth-flow surjectivity before taking the limit.

The self-review also checks the proof's nonalgebraic hinges. Energy expectations are taken only after bounded localization; noncollision is proved before asserting a positive pathwise minimum separation; Fatou produces integrable total drift before the un-stopped martingale is declared true; the heat comparison cancels identical driving paths and uses a path-dependent compact region; density inequalities first pass on continuous tests and are then extended to Borel measures. None of these steps is replaced by a formal generator assertion. The exact verification count and artifact-integrity results are recorded in the companion README and verification JSON.

## 10. Scope and the next unsupported domain line

The accepted candidate in this lane is a finite-N global collision-free realization, its local smooth Itô calculus, its same-noise heat approximation, explicit stopped and global energy identities, and the fixed-N bounded-density domination (1.7). No failure of that stated assertion was found in the proof or same-context checks. Its audit disposition remains pending fresh contexts.

The next unsupported line is the application of interacting N-particle Itô calculus to the empirical pair statistic formed from a merely bounded Borel or Haar-L2 pair inverse. Such an application would require, for the actual time-dependent pair solution \(\Phi_t\), meaningful derivatives of \(P_N[\Phi_t]\) and an identity of the form

\[
 dP_N[\Phi_t](X(t))
  = (\partial_t+L_N)P_N[\Phi_t](X(t))\,dt
   +\sqrt{2\nu}\sum_i\nabla_{x_i}P_N[\Phi_t](X(t))\cdot dW_i(t).
 \tag{10.1}
\]

Equation (10.1) is displayed as the **unproved next domain assertion**, not a conclusion of this report. At a minimum one must establish the needed local regularity or an appropriate extended-generator martingale identity for the interacting N-particle process; justify differentiated background contractions; and control approximation of the residual and the squared gradients entering brackets. A bounded Borel pair inverse characterized through a different pair process does not supply those facts for the full interacting system. The bounded-density result transfers an already proved Haar-integrable bound with its fixed-N cost, but does not provide the missing derivatives, integrability, approximation, or any N-uniform evolved residual/bracket estimate.

Consequently this lane does not close a corrector domain, a higher-order fluctuation theorem, the full microscopically subcritical regime, or the critical limiting law. No theorem scope, centering, or law class is enlarged silently. Root integration, canonical identifier assignment, fresh reconstruction, and hostile review remain separate steps. The worker changed no root file or canonical state ledger, made no commit or push, installed no dependency, and used no child agent. The Markdown outputs contain the complete construction; no TeX source is modified in this lane, and the final handoff uses no mathematical LaTeX.
