# Round 016 — the full sub-Coulomb and Coulomb quadratic source

TASK-079. Issued 2026-09-18 UTC. Constructor /root/r016_source_extension, fresh Astra Max context. **THM-038: PROVED CANDIDATE FOR THE ENTIRE FROZEN ASSERTION; SELF-CHECKED; WHOLE-CLAIM RECONSTRUCTION AND HOSTILE REVIEW STILL REQUIRED.** No independent certification is assigned here.

The proof covers every fixed integer dimension at least three and every positive Riesz exponent through the Coulomb endpoint, including three-dimensional Coulomb. It proves actual-law absolute integrability and the stated deterministic-time uniform source bound, with the original Haar centering and deleted labels. It also proves the scaled upper bound when its exponent is zero or positive, without claiming decay there. Zero noise uses its actual deterministic flow. No pair inverse, corrector domain, cubic estimate, bracket, hierarchy, or fluctuation limit is assumed or certified.

The new step is a positive heat-integral splitting whose retained Fourier weights have a logarithmic derivative bounded uniformly in the splitting scale. This yields a direct Fourier commutator estimate. A nonnegative heat integral at twice the scale dominates the discarded singular source. Actual expected energy, with its exact self and background subtractions, controls both positive quantities. Smooth heat dynamics are used separately to justify the actual singular expected-energy inequality.

## 1. Frozen assertion, exact negation, and source preflight

Fix exactly the data in THM-038: integer \(d\ge3\), \(0<s\le d-2\), \(0\le T<\infty\), \(0\le\nu_*<\infty\), and a fixed smooth real periodic terminal function \(h\). Haar measure on \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) has mass one; Fourier characters are \(e^{2\pi i k\cdot x}\). Put

\[
 \widehat g(0)=0,\qquad \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1.1}
\]

For every \(N\ge2\), \(0\le\nu\le\nu_*\), use the actual singular process

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu}\,dW_i,
 \qquad X_i(0)\text{ iid Haar, independent of all Brownian drivers}.
 \tag{1.2}
\]

Its exact backward test is

\[
 \widehat f_t(k)=\widehat h(k)e^{-(T-t)(4\pi^2\nu|k|^2+d_k)},\quad
 d_k=4\pi^2c_{d,s}|k|^{s+2-d}\quad(k\ne0),\qquad
 \widehat f_t(0)=\widehat h(0).
 \tag{1.3}
\]

Write \(v_t=\nabla f_t\), \(J_t(x,y)=K(x-y)\cdot(v_t(x)-v_t(y))\) off the pair diagonal. The statistic retains every original contraction:

\[
 P_N[J]=\frac1{2N^2}\sum_{i\ne j}J(X_i,X_j)
 -\frac1N\sum_i\int J(X_i,y)dy+\frac12\iint J(x,y)dxdy.
 \tag{1.4}
\]

The complete assertion is genuine integrability and a constant depending only on the fixed data, not on \(N,\nu,t\), such that

\[
 \sup_{0\le t\le T}\mathbb E|P_N[J_t](X(t))|\le C N^{s/d-1}.
 \tag{1.5}
\]

For \(b=\min(1/\nu,1)\) at positive noise, and \(b=1\) at zero noise, it also asserts

\[
 \sqrt{Nb}\,\mathbb E\int_0^T|P_N[J_t](X(t))|dt
 \le C\sqrt b\,N^{s/d-1/2}.
 \tag{1.6}
\]

The exact negation is one admitted fixed datum with failure of integrability or no finite common constant in (1.5), including the unchanged source and actual zero-noise flow. A failed upper bound, an inadmissible exchangeable law, a terminal test changing with \(N\), or a nondecaying right side in (1.6) is not this negation.

Only the nine task-allowlisted inputs were copied and byte-hash checked. The task and input manifest were read first. Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r016-source-extension. Branch: codex/hocf-r016-source-extension. Published base: 072cab684b9ce41855ead6c48f435c8fc184ec35. The task's explicit isolation and root-only integration restrictions govern this lane; inherited non-allowlisted files and current state were not read.

| Exact permitted input | Use and retained limitation |
|---|---|
| AGENTS.md | Research discipline and exact passages; the bounded task supersedes general state-reading and orchestration directions. |
| TASKS/ACTIVE/ROUND_001_MODEL.md | Torus/Fourier normalization, kernel coefficient, interaction, noise, deleted-label denominator and centering. |
| MEMORANDA/ROUND_001_ALGEBRA.md, Sections 1–2 | Source/statistic convention and response sign. Section 5 rederives the necessary contractions; no singular extension of its smooth diagonal convention is imported. |
| MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md, Sections 2–3 | Heat representation, local coefficient one, finite divergence measure, Coulomb atom and compensation. Section 2 checks these exact facts. No propagator theorem is needed. |
| THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md | Its issued status remains OPEN / UNAUDITED / VERSION_LOCKED. The card specifies earlier scope; its label is not proof. |
| MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md, Sections 3–8 | Stopped-energy construction, same-noise heat passage, fixed-\(N\) density domination. Section 3 reconstructs the facts used here. The earlier self-checked status is unchanged. |
| MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md, Sections 2–3 | Smooth free energy/Fatou and exact self subtraction. These arguments are rederived below. No corrector, reference-energy or singular-gradient premise mentioned elsewhere in that report is imported. |
| THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md | The entire frozen assertion and negation, without range repair. |
| TASKS/ACTIVE/TASK-079_ROUND016_SOURCE_EXTENSION_CONSTRUCTION.md | Assignment, permitted inputs, worktree and sealed handoff. |

This is a local construction, not independent certification of an earlier report. The load-bearing kernel, particle and energy facts are checked with their required mechanisms below. No external literature theorem, private input, theorem number, citation or novelty claim is used.

## 2. Kernel normalization and the Coulomb measure

Set

\[
 \alpha=(d-s)/2\ge1,\quad A=\frac{4^\alpha\pi^{d/2}}{\Gamma(s/2)},\quad
 p_u(z)=\sum_{n\in\mathbb Z^d}(4\pi u)^{-d/2}e^{-|z+n|^2/(4u)}.
\]

Unfolding the Gaussian gives \(p_u\ge0\), \(\int p_u=1\), and Fourier multiplier \(e^{-4\pi^2u|k|^2}\). The nonconstant Fourier series and all derivatives decay exponentially for \(u\ge1\). At small times \(\|p_u-1\|_1\le2\). Consequently

\[
 g(z)=A\int_0^\infty u^{\alpha-1}(p_u(z)-1)du
 \tag{2.1}
\]

exists in Haar \(L^1\), with nonzero coefficient

\[
 A\frac{\Gamma(\alpha)}{(4\pi^2|k|^2)^\alpha}
 =c_{d,s}|k|^{s-d}.
 \tag{2.2}
\]

The Euclidean central Gaussian integral is exactly \(|z|^{-s}\), by substituting \(w=|z|^2/(4u)\). On a ball of radius less than \(1/3\), the other lattice terms and all derivatives have exponentially small bounds at small \(u\). The large-time torus part decays exponentially, and the subtracted Euclidean part and all its spatial derivatives are integrable there. Thus

\[
 g(z)=|z|^{-s}+H(z),\quad H\in C^\infty(B_{1/3}),\qquad
 K(z)=s z|z|^{-s-2}-\nabla H(z).
 \tag{2.3}
\]

The kernel is smooth off zero and has a finite lower bound \(g_*<0\). The strict sign follows from zero mean and the positive nonconstant singularity. Because \(s+1<d\), \(K\in L^1\). Integration outside a small ball produces a gradient boundary term \(O(r^{d-1-s})\), which tends to zero, identifying this representative with the distributional negative gradient.

For \(D=\operatorname{div}K\), the inner-boundary flux against a smooth test \(a\) is

\[
 s r^{d-s-2}\int_{\mathbb S^{d-1}}a(r\theta)dS(\theta)+O_a(r^{d-1}).
 \tag{2.4}
\]

Below Coulomb the classical singular divergence is the integrable density \(s(d-2-s)|z|^{-s-2}\), and the flux vanishes. At Coulomb the flux is \(c_d a(0)\), with \(c_d=(d-2)|\mathbb S^{d-1}|\). The gamma recurrence and zero Fourier mode give the exact full measures

\[
 D=\begin{cases}s(d-2-s)g_{s+2}(z)dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,\end{cases}
 \quad
 \frac{4\pi^2c_{d,s}}{c_{d,s+2}}=s(d-2-s),\quad
 4\pi^2c_{d,d-2}=c_d.
 \tag{2.5}
\]

The ratio is used only below Coulomb. Fourier identification follows by heat-convolving the distributional difference, whose smoothed Fourier series is absolutely convergent, then testing against smooth functions as the heat parameter vanishes.

Hence \(D\) is a finite signed measure and \(D\ge-\kappa dz\) for a fixed finite \(\kappa\): below Coulomb use \(s(d-2-s)\max(0,-\inf g_{s+2})\); at Coulomb use \(c_d\). On the punctured torus \(\Delta g\le\kappa\). Heat mollification instead retains the whole measure:

\[
 D_\varepsilon=p_\varepsilon*D\ge-\kappa,\qquad
 D_\varepsilon=c_d(p_\varepsilon-1)\quad\text{at Coulomb}.
 \tag{2.6}
\]

The punctured equality \(\Delta g=c_d\) at Coulomb is used only on collision-excluded stopped paths. It is never substituted for (2.5) or (2.6) in an integral identity.

## 3. The actual law and its expected energy

Define

\[
 H_N(x)=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
 \mathcal H_N(x)=H_N(x)-\frac{N-1}{2}g_*
 =\frac1N\sum_{i<j}(g(x_i-x_j)-g_*)\ge0.
 \tag{3.1}
\]

Each energy sublevel is compact in the collision-free configuration space: every summand is nonnegative and any colliding pair makes its own summand diverge. This includes partial and simultaneous collisions. Differentiate both coordinates of each unordered pair:

\[
 B=-\nabla H_N,\qquad
 \Delta_{Nd}H_N=\frac2N\sum_{i<j}\Delta g(x_i-x_j)\le(N-1)\kappa.
 \tag{3.2}
\]

The drift square used below is the square of the complete interacting drift; no pair-force or triple cross terms are discarded.

For the needed particle construction, multiply \(K\) by even smooth local cutoffs at the collision. Subtracting the continuous Brownian path reduces each smooth additive-noise equation to an integral equation with a bounded globally Lipschitz drift. Picard differences have a factorially summable bound and Gronwall gives uniqueness. Iteration makes the maps jointly Borel in starting state, driving path and time. The cutoff solutions agree until their collision-excluded exits and patch to the local singular solution.

Stop when \(\mathcal H_N\) first reaches \(R\). Every differentiated quantity is bounded on this compact energy sublevel. Smooth Itô calculus has drift exactly \(-|B|^2+\nu\Delta_{Nd}H_N\), and martingale \(\sqrt{2\nu}\int\nabla H_N\cdot dW\), with stopped bracket \(2\nu\int|B|^2dt\). The stopped martingale is square integrable and has zero mean. Thus

\[
 \mathbb E_x\mathcal H_N(X(t\wedge\tau_R))
 \le\mathcal H_N(x)+\nu(N-1)\kappa t,\qquad
 \mathbb P_x(\tau_R\le T)\le
 \frac{\mathcal H_N(x)+\nu(N-1)\kappa T}{R}.
 \tag{3.3}
\]

A bounded-energy path has a limit at a finite endpoint, in a compact collision-excluded set with bounded smooth drift, and is extendible. Letting \(R\to\infty\) in (3.3) therefore proves global noncollision from each fixed collision-free start, almost surely, and local uniqueness gives global pathwise uniqueness. Joint measurability and Fubini cover the independent iid vector; its initial shifted-energy mean is \(-(N-1)g_*/2<\infty\). No exceptional set uniform over uncountably many starts is asserted.

Every such continuous path has a positive minimum pair distance on \([0,T]\). The heat drifts \(K_\varepsilon=p_\varepsilon*K\) converge in \(C^1\) on compact sets away from zero: split \(K\) into a smooth part agreeing near that set and an \(L^1\) part supported a positive distance away, and use differentiated Gaussian exponential bounds for the latter. Couple heat and singular solutions with the same start and Brownian paths; their noises cancel in their difference. Stop if their maximum coordinate distance reaches one quarter of the singular minimum separation. The common local Lipschitz bound and Gronwall make this stopped difference tend to zero, preventing the stop for sufficiently small \(\varepsilon\). This proves uniform-in-time convergence of the full heat family, almost surely, for each fixed \(N,\nu,T\). No uniform-in-\(N\) rate or limit interchange is claimed.

The fixed-\(N\) density bound used only in the initial-time falsification test follows as well. For each Brownian path the smooth heat flow is a diffeomorphism: its initial-point derivative solves the ordinary variational equation, and the backward additive integral equation gives its inverse. By (2.6),

\[
 \operatorname{div}_{Nd}B^\varepsilon
 =\frac2N\sum_{i<j}D_\varepsilon(x_i-x_j)\ge-(N-1)\kappa.
 \tag{3.4}
\]

The positive Jacobian is at least \(e^{-(N-1)\kappa t}\). Change of variables against initial Haar and Brownian expectation give the density bound. Path convergence passes it first for continuous nonnegative tests. Increasing continuous approximants to open-set indicators and outer regularity extend it to all Borel sets. Therefore the singular law has density

\[
 F_t\le e^{(N-1)\kappa t}.
 \tag{3.5}
\]

This bound is not used for a uniform-in-\(N\) estimate.

To prove the actual energy sign, keep \(\varepsilon>0\) fixed and take \(\nu>0\). The smooth law from initial density one satisfies

\[
 \partial_t F^\varepsilon
 =\operatorname{div}(F^\varepsilon\nabla H_N^\varepsilon+\nu\nabla F^\varepsilon),
 \qquad H_N^\varepsilon=N^{-1}\sum_{i<j}g_\varepsilon(x_i-x_j).
\]

All coefficient derivatives are bounded at this fixed cutoff. Iteration of the heat integral equation, spatial differentiation and heat smoothing give its classical solution. Comparison with constants times \(e^{\pm Ct}\), for \(C\ge\|\Delta H_N^\varepsilon\|_\infty\), gives positive lower and finite upper bounds on a finite time interval. The entropy differentiation and periodic integrations by parts are consequently legitimate. Combining them with the energy derivative gives exactly

\[
 \frac d{dt}\left[\nu\int F_t^\varepsilon\log F_t^\varepsilon
                     +\int H_N^\varepsilon F_t^\varepsilon\right]
 =-\int F_t^\varepsilon
 |\nabla H_N^\varepsilon+\nu\nabla\log F_t^\varepsilon|^2\le0.
 \tag{3.6}
\]

Both initial quantities are zero, because each pair difference is Haar and \(\int g_\varepsilon=0\). Convexity gives nonnegative entropy on the mass-one configuration space; hence \(\mathbb E H_N^\varepsilon(X_t^\varepsilon)\le0\).

Heat positivity gives the common lower bound \(H_N^\varepsilon\ge(N-1)g_*/2\). Same-noise path passage and local uniform kernel convergence give \(H_N^\varepsilon(X_t^\varepsilon)\to H_N(X_t)\) almost surely at each deterministic time. Fatou after subtracting this fixed-\(N\) lower bound proves

\[
 \boxed{\mathbb E H_N(X_t)\le0.}
 \tag{3.7}
\]

No singular entropy-dissipation identity is asserted. At zero noise the actual noncolliding deterministic flow has \(dH_N/dt=-|B|^2\le0\); averaging its integrable initial energy zero proves (3.7) directly, without division by noise.

The shifted energy is nonnegative, so Fatou also proves integrability of \(H_N(X_t)\). Permutation equivariance and uniqueness give exchangeability. Consequently

\[
 \mathbb E g(X_1-X_2)=\frac2{N-1}\mathbb E H_N\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|.
 \tag{3.8}
\]

The second inequality uses \(|g|\le g+2|g_*|\). The local inverse \(s\)-th-power pair-distance moment is uniformly bounded by (2.3). Common translations preserve the actual dynamics and preparation, so the one-body law is Haar. No independence of higher marginals at positive time follows or is used.

## 4. A positive splitting with polynomial Fourier tails

Choose the fixed integer \(M=d+2\). For \(0<r\le2\), define

\[
 w_r(u)=(1-e^{-u/r})^M,\qquad\psi_r(u)=1-w_r(u),
\]
\[
 g_r(z)=A\int_0^\infty u^{\alpha-1}w_r(u)(p_u(z)-1)du,\quad
 Q_r(z)=A\int_0^\infty u^{\alpha-1}\psi_r(u)p_u(z)du,\quad
 c_r=A\int_0^\infty u^{\alpha-1}\psi_r(u)du.
 \tag{4.1}
\]

The deterministic splitting scale \(r\) is distinct from the particle heat parameter \(\varepsilon\). We have \(Q_r\ge0\) off zero and \(\int Q_r=c_r\). The bounds \(w_r(u)\le\min(1,(u/r)^M)\) and \(0\le\psi_r(u)\le\min(1,Me^{-u/r})\) imply

\[
 c_r=A r^\alpha B_{\alpha,M},\qquad
 B_{\alpha,M}=\int_0^\infty u^{\alpha-1}[1-(1-e^{-u})^M]du\in(0,\infty).
 \tag{4.2}
\]

Its alternative formula is \(\Gamma(\alpha)\sum_{j=1}^M(-1)^{j+1}\binom Mj j^{-\alpha}\); positivity follows from the integral, not an assumed sign of the alternating sum.

The real even function \(g_r\) has zero mean and is \(C^2\). The small-time differentiated Gaussian bounds through order two integrate because \(M>(s+2)/2\); equivalently the Fourier coefficients are \(O_r(|k|^{-2\alpha-2M})\), absolutely summable with two powers of \(|k|\). They are strictly positive:

\[
 a_r(k)=A\int_0^\infty u^{\alpha-1}w_r(u)e^{-4\pi^2u|k|^2}du>0
 \quad(k\ne0),\qquad a_r(0)=0.
 \tag{4.3}
\]

The bound \(p_u(0)\le C u^{-d/2}\) for \(u\le1\) and exponential large-time decay yield

\[
 0\le g_r(0)=\sum_{k\ne0}a_r(k)\le C r^{-s/2}\quad(0<r\le2).
 \tag{4.4}
\]

For \(r\le1\), integrate \(r^{-M}u^{M-s/2-1}\) on \((0,r)\), \(u^{-s/2-1}\) on \((r,1)\), then the finite large-time remainder. For \(1\le r\le2\) enlarge the fixed constant. The lower bound is the positive Fourier identity.

The exact splitting, in \(L^1\) and pointwise off zero, is

\[
 g=g_r+Q_r-c_r.
 \tag{4.5}
\]

No singular value at zero is assigned. For the collision-free empirical measure \(\eta_N=N^{-1}\sum_i\delta_{x_i}\), set

\[
 E_r(x)=\frac12\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2\ge0,\qquad
 S_r(x)=\frac1{2N^2}\sum_{i\ne j}Q_r(x_i-x_j)\ge0.
\]

Apply (4.5) only to deleted pairs and subtract the smooth self diagonal:

\[
 \boxed{\frac{H_N(x)}N
 =E_r(x)+S_r(x)-\frac{g_r(0)}{2N}-\frac{N-1}{2N}c_r.}
 \tag{4.6}
\]

The \(N(N-1)\) ordered pairs give exactly \((N-1)/(2N)\) in the constant term. The smooth self term is exactly \(1/(2N)\). At each fixed \(r,N,t\), \(E_r\) is bounded and \(S_r\) is integrable by (4.5) and (3.8). Thus (3.7) permits expectation of this exact identity:

\[
 \boxed{\mathbb E E_r(X_t)+\mathbb E S_r(X_t)
 \le\frac{g_r(0)}{2N}+\frac{N-1}{2N}c_r
 \le C(N^{-1}r^{-s/2}+r^\alpha).}
 \tag{4.7}
\]

No generic-law inequality replaces the actual energy sign, and the two nonnegative terms have explicit separate justifications.

## 5. Original background contractions and actual integrability

For a smooth vector field \(v\), the odd integrable force gives by direct integration

\[
 A_g(x):=\int J_g(x,y)dy=-\int K(x-y)\cdot v(y)dy,\qquad
 \int A_g=\iint J_g=0.
 \tag{5.1}
\]

For \(v=\nabla f\), distributional integration by parts against the smooth test uses exactly \(D\):

\[
 A_g(x)=-\int f(x+z)D(dz),\qquad
 \widehat A_g(k)=-d_k\widehat f(k).
 \tag{5.2}
\]

At Coulomb this is \(-c_d(f-\int f)\), including atom and compensation. The double contraction is zero by the computed integral (5.1), not by deletion from the statistic.

For every nonnegative integer \(m\), the exact multipliers (1.3) give

\[
 \sup_{0\le t\le T,\,0\le\nu\le\nu_*}\|f_t\|_{C^m}
 \le C_m\sum_k(1+|k|)^m|\widehat h(k)|<\infty.
 \tag{5.3}
\]

The multipliers have modulus at most one. Two more powers give the time regularity needed on the bounded noise range. These are bounds on every fixed smooth test, with no polynomial restriction.

From (2.3) and the mean-value bound on \(v_t\), \(|J_t(x,y)|\le C_h(1+\operatorname{dist}(x,y)^{-s})\) near the diagonal and is bounded away from it. Hence its Haar \(L^1\) norm is uniform in \(t,\nu\). Equation (3.8) proves actual integrability of every deleted pair term, and (5.1)–(5.2) bound the contractions. This proves genuine integrability before applying a Fourier commutator. No path evaluates a singular diagonal.

## 6. A uniform commutator bound for the retained kernel

Regard (4.3) as a radial function \(a_r(\xi)\) for \(\xi>0\). It satisfies

\[
 0\le-\frac{\xi a_r'(\xi)}{a_r(\xi)}\le L,\qquad L=2(\alpha+M),
 \tag{6.1}
\]

uniformly in \(r>0\). Indeed \(0\le u w_r'(u)\le M w_r(u)\), since \(z/(e^z-1)\le1\). For \(\lambda=4\pi^2\xi^2\), integrate the derivative of \(u^\alpha w_r(u)e^{-\lambda u}\); both boundary terms vanish. This gives

\[
 \lambda\int_0^\infty u^\alpha w_r(u)e^{-\lambda u}du
 =\alpha\int_0^\infty u^{\alpha-1}w_r(u)e^{-\lambda u}du
   +\int_0^\infty u^\alpha w_r'(u)e^{-\lambda u}du
 \le(\alpha+M)\int_0^\infty u^{\alpha-1}w_r(u)e^{-\lambda u}du.
\]

Twice this ratio is the logarithmic derivative in (6.1). Polynomial rather than exponential retained tails permit this bound.

For nonzero lattice vectors \(k,\ell\), put \(q=k-\ell\), \(u=\min(|k|,|\ell|)\ge1\), \(R=\max(|k|,|\ell|)\). From (6.1),
\(a_r(u)/a_r(R)\le(R/u)^L\) and
\(a_r(u)-a_r(R)\le L a_r(u)(R-u)/u\). Consequently

\[
 \frac{|k a_r(k)-\ell a_r(\ell)|}{\sqrt{a_r(k)a_r(\ell)}}
 \le(1+L)|q|(1+|q|)^{L/2+1}.
 \tag{6.2}
\]

To check the vector numerator, bound it by \(|q|a_r(u)+R[a_r(u)-a_r(R)]\), use \(R-u\le|q|\), and then \(R/u\le1+|q|\). These estimates require no comparison of exponentially small neighboring weights.

Let \(\rho=\eta_N-dx\), whose zero Fourier coefficient is exactly zero. The retained kernel \(g_r\) is \(C^2\), with \(K_r=-\nabla g_r\) and \(J_r(x,y)=K_r(x-y)\cdot(v(x)-v(y))\). Its diagonal is zero. Expanding the centered full product therefore recovers precisely (1.4):

\[
 P_N[J_r]=\frac12\iint J_r(x,y)\rho(dx)\rho(dy)
 =\int v(x)\cdot(K_r*\rho)(x)\rho(dx).
 \tag{6.3}
\]

This full-product identity is used only for the retained smooth kernel. Symmetrizing its Fourier series gives

\[
 P_N[J_r]=-\pi i\sum_{k,\ell\ne0}
 [k a_r(k)-\ell a_r(\ell)]\cdot\widehat v(\ell-k)
 \widehat\rho(k)\overline{\widehat\rho(\ell)}.
 \tag{6.4}
\]

For the sign and coefficient, begin with
\(-2\pi i\sum_{k,m}k a_r(k)\cdot\widehat v(-k-m)\widehat\rho(k)\widehat\rho(m)\),
symmetrize \(k,m\), then set \(m=-\ell\). Absolute summability follows from \(\sum |k|a_r(k)<\infty\), the bounded coefficients of a finite measure, and the summable Fourier coefficients of \(v\). The following estimate also supplies an absolute majorant.

Set \(b_k=\sqrt{a_r(k)}|\widehat\rho(k)|\) for \(k\ne0\) and \(b_0=0\). For each \(q\), Cauchy–Schwarz gives \(\sum_k b_k b_{k-q}\le\sum_k b_k^2\). Apply (6.2) to (6.4):

\[
 |P_N[J_r]|\le C_v\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2
 =2C_v E_r,\qquad
 C_v=\pi(1+L)\sum_q|q|(1+|q|)^{L/2+1}|\widehat v(q)|.
 \tag{6.5}
\]

The constant has no dependence on \(r,N\). For \(v_t=\nabla f_t\), (1.3) bounds it uniformly by a constant times
\(\sum_q(1+|q|)^{\alpha+M+3}|\widehat h(q)|\), a finite seminorm of the same fixed smooth \(h\). Arbitrary smooth tests, including their unchanged constant modes, are thus covered.

## 7. The singular remainder and the complete bound

Let \(R_r=g-g_r=Q_r-c_r\). Its gradient is defined off zero by the heat integral and is Haar \(L^1\): at small times \(\|\nabla p_u\|_1\le C u^{-1/2}\) integrates with \(u^{\alpha-1}\), since \(\alpha\ge1\); at large times \(\psi_r\) decays exponentially. Thus its Haar contractions are the original integrals, not limiting diagonal traces.

Write \(\delta(z)=\operatorname{dist}_{\mathbb T^d}(z,0)\). For every Gaussian translate \(\delta(z)\le|z+n|\), so direct differentiation gives

\[
 \delta(z)|\nabla p_u(z)|
 \le\sum_n\frac{|z+n|^2}{2u}(4\pi u)^{-d/2}e^{-|z+n|^2/(4u)}
 \le C_d p_{2u}(z).
 \tag{7.1}
\]

Divide each summand by its \(2u\)-Gaussian: the remaining factor is at most
\(4\,2^{d/2}\sup_{y\ge0}ye^{-y}\). No distance function is differentiated.

Integration of \(Dv\) along a shortest torus geodesic gives
\(|v(x)-v(y)|\le\|Dv\|_\infty\delta(x-y)\). Differentiate \(R_r\) off zero and use (7.1). Substitution \(a=2u\), with \(\psi_r(a/2)=\psi_{2r}(a)\), proves

\[
 |J_{R_r}(x,y)|
 \le C_d\|Dv\|_\infty A\int_0^\infty u^{\alpha-1}\psi_r(u)p_{2u}(x-y)du
 =C_d2^{-\alpha}\|Dv\|_\infty Q_{2r}(x-y).
 \tag{7.2}
\]

This is positive-kernel domination of an absolute value. It does not assert positive semidefiniteness of a weighted Riesz kernel.

For \(0<r\le1\), retain exactly the three coefficients in (1.4). The empirical absolute-value sum gives \(S_{2r}\), the one-body contraction is bounded by \(c_{2r}\), and the double contraction by \(c_{2r}/2\). Therefore

\[
 \mathbb E|P_N[J_{R_r}]|
 \le C_h\left(\mathbb E S_{2r}+\frac32c_{2r}\right)
 \le C_h(N^{-1}r^{-s/2}+r^\alpha).
 \tag{7.3}
\]

The double contraction is actually zero by (5.1); the displayed upper bound preserves all original terms visibly. Tonelli applies to the nonnegative majorant, whose expectation is finite by (4.7). That estimate was proved through scale two expressly to cover this scale doubling.

Linearity of the genuine off-diagonal statistic and its original contractions gives
\(P_N[J_g]=P_N[J_r]+P_N[J_{R_r}]\). Combining (4.7), (6.5), and (7.3) yields

\[
 \mathbb E|P_N[J_t]|\le C_h(N^{-1}r^{-s/2}+r^\alpha),
 \qquad 0<r\le1,
 \tag{7.4}
\]

uniformly in all admitted \(N,\nu,t\). Choose \(r=N^{-2/d}\) in this already proved inequality:

\[
 N^{-1}r^{-s/2}=N^{s/d-1},\qquad
 r^\alpha=N^{-(d-s)/d}=N^{s/d-1}.
 \tag{7.5}
\]

This proves the full (1.5). It is a deterministic scale choice, not a simultaneous singular-SDE limit. Joint measurability follows from the particle construction, smooth \(f_t\), and the Borel off-diagonal kernel. Tonelli and (1.5) imply

\[
 \sqrt{Nb}\,\mathbb E\int_0^T|P_N[J_t]|dt
 \le C_hT\sqrt b\,N^{s/d-1/2}.
 \tag{7.6}
\]

Enlarge the common constant to \((1+T)C_h\) to use one constant for (1.5)–(1.6), also at \(T=0\). There is no inverse noise in the proof. Scaled smallness follows only for \(s<d/2\); at equality the estimate is bounded, and above it the theorem asserts only the displayed possibly growing upper bound. Three-dimensional Coulomb has \(s=1\) and is included. The theorem's exclusions remain unchanged.

## 8. Independent falsification route and limiting tests

The falsification route examines the actual initial generator rather than the heat-splitting commutator. For a nonzero fixed mode \(k\), let
\(Z_k=N^{-1}\sum_i e^{-2\pi i k\cdot X_i}\). Initial product Haar gives

\[
 \mathbb E|Z_k(0)|^2=\frac1N,\qquad
 \left.\frac d{dt}\mathbb E|Z_k(t)|^2\right|_{t=0}
 =-\frac{2(N-1)}{N^2}d_k\le0.
 \tag{8.1}
\]

For the coefficient, retain the \(N\) constant self terms in \(|Z_k|^2\). For an ordered distinct pair the two internal forces have total coefficient \(2/N\); every third-label force integrates to zero at initial product Haar. The initial two-label weak derivative is \(-(2/N)D(x-y)\). Pairing with the difference Fourier mode gives \(-(2/N)d_k\), and multiplying by the ordered-pair fraction \((N-1)/N\) proves (8.1). Diffusion integrates to zero against initial Haar for every \(\nu\), including zero. The diagnostic also derives this from the literal full finite-particle generator.

This is a legitimate singular actual-law derivative for a fixed smooth observable. Its generator is Haar \(L^1\), since \(K\in L^1\). At fixed \(N\), (3.5) uniformly bounds the densities on a short initial interval. Approximate the generator in Haar \(L^1\) by continuous functions; the density bound controls the errors uniformly, and path continuity gives weak convergence to initial Haar for the continuous approximants. The stopped integral Itô formula passes to the full expectation because the force is integrable in probability times time by (3.5), while derivatives of the observable are bounded. It therefore differentiates at zero. The distributional pairing uses (2.5). At Coulomb \(d_k=c_d\); the atom contributes the nonzero right side, while the compensating constant disappears only against the nonzero mode.

Thus immediate positive low-mode variance creation is not an admitted counterexample. No uniform singular Taylor remainder or later-time variance sign is claimed.

| Test | Exact conclusion and limitation |
|---|---|
| Constant terminal \(h\), including a nonzero constant mode | Every source and contraction is zero, at all times and noises. |
| \(T=0\) | The time integral is zero; the pointwise bound still applies to the iid initial source. |
| \(N=2\) actual process | For \(R=X_1-X_2\), relative drift is \(K(R)\), relative noise is \(\sqrt{4\nu}\), and \(H_2=g(R)/2\). At zero noise \(dH_2/dt=-|K(R)|^2/2\), agreeing with the complete drift square. No third label is inserted. |
| Three-dimensional Coulomb | \(D=4\pi(\delta_0-dx)\), \(A_g=-4\pi(f-\int f)\); (2.6), (5.2), and (8.1) retain the atom. No dimension-specific loss occurs in (6.2) or (7.2). |
| \(s\ge d/2\) | For appropriate nonconstant smooth tests the local source square has radial power \(r^{d-1-2s}\), so a Haar \(L^2\) source estimate can fail. Its \(L^1\) singularity remains integrable. The proof uses no source square. |
| Near-collision iid starts | Initial energy is integrable, and (3.3) applies conditionally on each start. No deterministic separation uniform over starts is asserted. |
| Bounded noise and exactly zero noise | Test seminorms are bounded by those of the same \(h\). Energy sign uses smooth free energy or deterministic decrease respectively. No constant diverges as noise tends to zero. |
| Generic clustered exchangeable laws | They need not satisfy (3.7), the precise actual-law input. They cannot negate the admitted statement. |

## 9. New diagnostic and hostile self-check

The fresh standard-library diagnostic is
MEMORANDA/ROUND_016_SOURCE_EXTENSION_ARTIFACTS/round016_exact_diagnostic.py.
It reads no earlier checker. Arithmetic is exact rational and Gaussian rational; examples and Laplace moments are deterministic. There is no random seed, floating-point tolerance, or dependency installation.

It computes the literal deleted source statistic and background contraction and compares with the symmetrized Fourier formula; verifies the energy self/background identity and detects deliberately wrong coefficients; applies the literal finite-particle generator to \(|Z_k|^2\) at Haar for \(N=2\) through six and four noises; checks exact positive smoothing moments and logarithmic derivative bounds; and checks all scaling powers, including bounded and growing scaled upper bounds. Smooth Fourier examples test coefficients; they do not substitute for the singular model. One implemented derivative is divided by \(2\pi\); the source and generator restore \((2\pi)^2\), and the fixed Riesz prefactor is factored out of mode probes.

Command run from the isolated worktree:

    python3 MEMORANDA/ROUND_016_SOURCE_EXTENSION_ARTIFACTS/round016_exact_diagnostic.py

Outcome: **PASS, 2,892 exact assertions in 24 categories.** The companion JSON records exact moment cases, scaling cases, counts, and the script digest. The analytic proof above, not this diagnostic, proves the continuum estimate.

The strongest new claim received the following local challenges. This is a constructor self-check, not the required isolated hostile audit.

| Challenge | Resolution |
|---|---|
| Could Fourier cutoff weights destroy a uniform commutator estimate? | Polynomial tails have the exact scale-independent logarithmic slope (6.1); the lattice bound (6.2) is proved directly. |
| Is the discarded positive kernel's mass missing? | It is exactly \(c_r\); (4.6) retains \((N-1)c_r/(2N)\). |
| Are source and energy self terms confused? | Only the retained \(C^2\) source has diagonal zero. The distinct energy self term is \(g_r(0)/(2N)\), retained exactly. Singular diagonal values are never assigned. |
| Is a fixed-\(N\) density bound used as uniform control? | Uniform control uses (3.7), from smooth free energy and Fatou. Density domination is used only for the fixed-\(N\) initial derivative. |
| Does Coulomb's classical Laplacian replace its measure? | (2.5)–(2.6), (5.2), and (8.1) keep atom and compensation. The punctured value is confined to stopped trajectories. |
| Is near-source domination an unproved weighted positivity claim? | It is the termwise Gaussian inequality (7.1); only \(Q_r\ge0\) and positive retained Fourier coefficients are used. |
| Are arbitrary smooth tests replaced by polynomials? | An explicit finite Fourier seminorm of the same \(h\) bounds the exact test uniformly. Polynomials occur only in diagnostics. |
| Is \(s<d/2\) hidden in the source proof? | Only optional scaled decay uses it. The source proof requires exactly the frozen \(0<s\le d-2\). |
| Are limits interchanged? | Particle heat passage is at fixed \(N,\nu,T\); the later splitting scale is inserted into a proved inequality. |
| Is zero noise obtained by division or limiting inference? | The actual deterministic noncolliding gradient flow and its energy decrease are used directly. |

## 10. Dispositions and recoverable handoff

| Assertion or route | Disposition |
|---|---|
| Entire THM-038: actual integrability, uniform source estimate, zero noise, scaled quantitative consequence | PROVED CANDIDATE HERE; SELF-CHECKED; independent reconstruction and hostile review pending. |
| Exact negation of THM-038 | Ruled out by the candidate proof subject to those gates; no admitted counterexample found. |
| Initial positive low-mode variance-creation route | DISPROVED as a fixed-\(N\) initial derivative claim by (8.1). No later-time sign is asserted. |
| Haar \(L^2\) source control throughout the range | Not a premise and can fail for larger exponents; this does not negate the required \(L^1\) theorem. |
| Earlier particle/kernel/energy reports | Statuses unchanged as issued. Needed facts are reconstructed here; this is not independent certification of those reports. |
| Pair, cubic, bracket, hierarchy or fluctuation theorem | NOT CLAIMED. |

Root alone may integrate the result and assign canonical ledger changes or audit identifiers. The worker created only this memorandum and its unique artifact directory, apart from task-authorized copying of the exact nine dossier inputs into the isolated worktree. No current state, cumulative memorandum, external source, private input, memory file, current R11–R15 proof/audit, prior checker, other worktree output, or non-allowlisted mathematical source was read. No child agent, commit, push, install, external browse, publication or author contact occurred.

The artifact README records verification, exposure, input/output manifests, archive membership, byte digest, and the seal-verification procedure. Packet input copies reproduce the nine checked byte strings. Issued outputs and archive are made read-only after verification; a correction must be separately issued, not edited into the sealed packet.

The next action is fresh whole-claim reconstruction from THM-038 and its approved minimal dossier, followed by isolated hostile review of this complete construction, its coefficients, singular passages and uniformities. No theorem promotion is authorized by this constructor's self-check.
