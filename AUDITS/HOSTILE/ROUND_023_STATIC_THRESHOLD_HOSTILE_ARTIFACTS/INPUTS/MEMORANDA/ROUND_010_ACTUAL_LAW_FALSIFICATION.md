# Round 010 — actual-law falsification and a singular-tail reduction

TASK-061. Issued 2026-09-18 UTC. **NOT FALSIFIED; ACTUAL-LAW ESTIMATES AND AN EXACT REMAINING REDUCTION. SELF-CHECKED, FRESH REVIEW REQUIRED.**

The genuine full-corrector noise target is not proved in this report, and no admissible counterexample is produced. There is a concrete advance beyond the reference-law reduction: the actual iid-Haar-prepared dynamics satisfy a uniform expected-energy inequality and quantitative control of every fixed Fourier mode. These imply vanishing actual-law noise for explicit, progressively less smoothed versions of the genuine full inverse. The remaining assertion is exactly a uniform actual-law estimate for the discarded singular scales. An independently derived initial-time test has the opposite sign from a proposed positive-correlation counterexample: the first centered three-label covariance derivative is nonpositive for every smooth centered probe. No uniform singular Taylor remainder is claimed.

The twenty inputs were copied and hash-checked in the isolated worktree `/tmp/hocf-r010-law-falsification-20260917`, on branch `codex/hocf-r010-law-falsification`, from published R8 commit `b2510ed08ecc26387d9fc14daaf174d3c35f5638`. The task and input manifest were read first. No R10 constructor task, seed, proof, current audit/state/history, memory file, other checker, or non-allowlisted mathematical source was read. Ambient app/global instructions included an automatically supplied high-level memory summary; it was not used as a mathematical input, and that unavoidable exposure is recorded. No root/canonical files, commits, pushes, dependency installations, or children are involved. The precise exposure and seals accompany this report. Earlier theorem cards retain their issued statuses; this report does not independently certify an earlier construction.

## 1. Target, negation, and source preflight

Use exactly the supplied homogeneous unit-Haar model: integer \(d\ge3\), \(0<s\le d-2\), finite \(T\), smooth real terminal \(h\), zero external drift, and the frozen coefficient-one Riesz kernel

\[
 \widehat g(0)=0,\qquad \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1.1}
\]

For each \(N\ge2\) and \(0<\nu\le\nu_*<\infty\), the actual particle process starts from iid unit Haar, independently of the standard Brownian motions, and satisfies

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu}\,dW_i.
 \tag{1.2}
\]

Write \(\beta=1/\nu\), \(b_N=\min(\beta,1)\), and \(\sigma_N^2=Nb_N\). In particular \(\nu b_N\le1\). Let \(f\) be the exact Fourier backward test and \(\Phi\) the terminal-zero symmetric genuine full pair inverse. Its equation includes both compensated responses, each with coefficient one:

\[
 \partial_t\Phi+\nu(\Delta_x+\Delta_y)\Phi+N^{-1}B\Phi
       +(R_x+R_y)\Phi=-J,
 \quad J=K(x-y)\cdot(\nabla f(x)-\nabla f(y)).
 \tag{1.3}
\]

The statistic keeps its actual mean-field centering and ordered deleted pairs:

\[
 P_N[v]=\frac1{2N^2}\sum_{i\ne j}v(X_i,X_j)
       -\frac1N\sum_i\int v(X_i,y)dy+\frac12\int v(x,y)dxdy.
 \tag{1.4}
\]

For any admissible time-dependent symmetric kernel define the actual-law noise functional

\[
 Q_N[v]=2\nu Nb_N\,\mathbb E\int_0^T
                     \sum_i|\nabla_iP_N[v_t](X(t))|^2dt.
 \tag{1.5}
\]

For the genuine inverse, its equality with the expected scaled martingale bracket uses the full supplied domain premise. The target is \(Q_N[\Phi]\to0\) for every admitted sequence. Its negation is a fixed admitted \(d,s,T,h,\nu_*\) and sequence with positive or infinite limsup of this nonnegative quantity. Zero noise gives zero functionals separately; it is not the reciprocal of a finite inverse temperature.

The source boundaries used here are explicit:

| Permitted source | Exact use and retained limitation |
|---|---|
| Frozen R1 model and `ROUND_001_ALGEBRA.md`, Sections 1, 3, 5 | Unit mass, ordered distinct labels, denominator \(N^2\), factor one half, noise \(\sqrt{2\nu}\), both responses. New coefficients below are derived directly. |
| `ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–4, and THM021 | The coefficient-one heat representation, \(K\in L^1\), finite \(D=\operatorname{div}K\), lower bound \(D\ge-\kappa\), and exact constant-background response convolution. |
| `ROUND_005_PERIODIC_PAIR_POTENTIAL.md`, (9.3), THM023 | The actual singular auxiliary pair evolution and its Borel Haar measure inequality. An L2 norm alone is not used as an L1 bound. |
| R5 full inverse/interface and its two supplied clarifications, THM024/025 | The genuine Borel Volterra inverse with both responses, pair-exchange symmetry, and exact homogeneous Fourier test. No law transfer is imported. |
| `ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, Sections 3–8, THM026 | The actual singular process, fixed-N same-noise heat passage, density bound, and total-drift energy identity. No N-uniform density bound is imported. |
| THM028 and `ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, Sections 5, 7–11 | The full provisional regularity/Itô premise for unsmoothed \(\Phi\) and fixed-N integrability. Its constants may depend on N and do not become uniform constants here. |
| Supplied R9 blind energy reconstruction | Its reference-energy theorem is conditional. It is used only for the expressly conditional shrinking-time corollary in Section 9. Its extra timewise estimate is not used. |

No external literature statement or novelty claim is used. The core new actual-law estimates in Sections 2–4 use the particle and kernel modules, not the R9 reference energy or R8 corrector derivative estimates. Statements involving the genuine unsmoothed bracket retain its domain premise.

The three temperature conditions remain separate throughout: the old floor condition \(\beta_NN^{2s/d-1}\to0\), full subcriticality \(\lambda_N:=\beta_NN^{s/d-1}\to0\), and criticality \(\lambda_N\to\lambda\in(0,\infty)\). None is silently assumed for the target. Set

\[
 q:=1-s/d>0.
 \tag{1.6}
\]

All unspecified constants below depend only on the displayed fixed data and, when explicitly indicated, on a smoothing parameter or finitely many seminorms of h. They are independent of N and the admitted diffusivity.

## 2. An actual-law free-energy inequality with its singular passage

The N-particle potential is

\[
 H_N(x)=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
 B_i(x)=\frac1N\sum_{j\ne i}K(x_i-x_j)=-\nabla_iH_N(x).
 \tag{2.1}
\]

Let \(g_*=\inf_{z\ne0}g(z)>-\infty\). The local positive singularity and zero mean give \(g_*<0\). At each fixed heat parameter \(\epsilon>0\), use the exact smooth heat kernel \(g_\epsilon=p_\epsilon*g\), its potential \(H_N^\epsilon\), and the actual smooth particle law \(F_t^\epsilon\) from initial density one. For positive diffusivity the smooth periodic Fokker–Planck equation is

\[
 \partial_tF^\epsilon=\operatorname{div}
       (F^\epsilon\nabla H_N^\epsilon+\nu\nabla F^\epsilon).
 \tag{2.2}
\]

At this fixed cutoff its coefficients and their derivatives are bounded. The heat integral equation produces its smooth solution; the maximum principle gives strictly positive upper and lower bounds on each fixed compact time interval, starting from one. Thus the following differentiations and periodic integrations by parts are legitimate at the cutoff; they use neither a singular density equation nor a collision trace. Directly differentiating gives

\[
 \frac{d}{dt}\left(\nu\int F_t^\epsilon\log F_t^\epsilon
                          +\int H_N^\epsilon F_t^\epsilon\right)
 =-\int F_t^\epsilon
       |\nabla H_N^\epsilon+\nu\nabla\log F_t^\epsilon|^2\le0.
 \tag{2.3}
\]

The initial entropy and initial energy are both zero: each pair difference has Haar law and \(\int g_\epsilon=0\). Also \(\int F\log F\ge0\) for a probability density on a space of mass one, by convexity. Consequently

\[
 \mathbb EH_N^\epsilon(X_t^\epsilon)\le0.
 \tag{2.4}
\]

The supplied particle heat-passage theorem couples \(X^\epsilon\) to \(X\) from the same iid initial vector and Brownian motions, with uniform-in-time path convergence almost surely for each fixed N and parameter tuple. The singular path has a positive minimum pair distance on a finite horizon almost surely. Local uniform convergence \(g_\epsilon\to g\) away from zero therefore gives

\[
 H_N^\epsilon(X_t^\epsilon)\longrightarrow H_N(X_t)
 \quad\hbox{almost surely at every fixed }t.
 \tag{2.5}
\]

The heat kernel is positive, so \(g_\epsilon\ge g_*\) and
\(H_N^\epsilon\ge (N-1)g_*/2\), uniformly in the heat cutoff at this fixed N. Fatou applied after subtracting that lower bound proves

\[
 \boxed{\quad\mathbb EH_N(X_t)\le0\quad(0\le t\le T).\quad}
 \tag{2.6}
\]

This is an inequality for the actual evolved law. It does not assert equality of that law with product Haar. At zero diffusivity, the supplied exact deterministic energy decrease proves (2.6) directly after averaging the iid initial energy zero.

One may also pass the entire free energy. Relative entropy is lower semicontinuous under weak convergence on the compact configuration torus: for each continuous a,
\(\int a\,dF-\log\int e^a\le\operatorname{Ent}(F)\), and the supremum over continuous a equals entropy, by truncating the density and approximation in finite measure. This variational representation proves the claimed lower semicontinuity directly. Together with (2.5) and the common energy lower bound it gives, for positive diffusivity,

\[
 \nu\operatorname{Ent}(F_t)+\mathbb EH_N(X_t)\le0.
 \tag{2.7}
\]

There is no passage of a Fisher-information or singular dissipation identity in this step. Only the nonpositive free energy is passed. Finite-N absolute continuity is already supplied independently by the particle module.

Exchangeability follows from permutation equivariance and pathwise uniqueness; common translations preserve the SDE and the initial law, hence each one-body marginal is Haar. From exchangeability and (2.6),

\[
 \mathbb Eg(X_1(t)-X_2(t))=\frac{2}{N-1}\mathbb EH_N(X_t)\le0,
 \qquad
 \mathbb E|g(X_1(t)-X_2(t))|\le2|g_*|.
 \tag{2.8}
\]

The last bound follows from \(|g|\le g+2|g_*|\). By the local coefficient-one expansion it also bounds the corresponding local moment of the inverse s-th power of pair distance, uniformly in N, diffusivity, and deterministic time. It does not bound an individual squared force.

## 3. A deterministic floor and actual empirical Fourier estimates

This construction derives the required floor rather than importing the old completed-energy closure. Put

\[
 \alpha=(d-s)/2,\qquad A=\frac{4^{(d-s)/2}\pi^{d/2}}{\Gamma(s/2)},
 \qquad g^{>r}(z)=A\int_r^\infty t^{\alpha-1}(p_t(z)-1)dt,
 \quad0<r\le1.
 \tag{3.1}
\]

The R4 heat representation is in the frozen normalization. This truncation is a truncation of its heat integral, distinct from the heat convolution used for the particle approximation. The positive heat kernel gives the pointwise lower comparison off zero

\[
 g(z)\ge g^{>r}(z)-A r^\alpha/\alpha.
 \tag{3.2}
\]

Its smooth Fourier coefficients are

\[
 a_r(k)=A\int_r^\infty t^{\alpha-1}e^{-4\pi^2|k|^2t}dt>0
       \quad(k\ne0),\qquad a_r(0)=0.
 \tag{3.3}
\]

They decay rapidly at this fixed r. The periodized Gaussian bound
\(p_t(0)\le Ct^{-d/2}\) for \(0<t\le1\), and exponential decay of \(p_t-1\) for \(t\ge1\), give

\[
 0\le g^{>r}(0)\le Cr^{-s/2}.
 \tag{3.4}
\]

Indeed the small-time integrand is bounded by \(Ct^{-s/2-1}\); the large-time integral is finite. Let \(\eta_N=N^{-1}\sum_i\delta_{x_i}\), with
\(\widehat\eta_N(k)=N^{-1}\sum_i e^{-2\pi i k\cdot x_i}\). Exact subtraction of the smooth self diagonal gives

\[
\begin{split}
 H_N(x)&\ge\frac N2\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2
            -\frac12g^{>r}(0)-\frac{N-1}{2\alpha}Ar^\alpha,\\
 H_N(x)&\ge-CN^{s/d}\qquad\text{on choosing }r=r_N=N^{-2/d}.
\end{split}
 \tag{3.5}
\]

The diagonal coefficient is exactly one half, since the potential has unordered pairs with coefficient \(1/N\). Both errors in the first line have size \(N^{s/d}\) at the stated r. Positivity here is positivity of explicitly positive Fourier coefficients, not of an arbitrary weighted pair kernel.

Taking actual-law expectations in (3.5) and using (2.6) yields

\[
 \mathbb E\sum_{k\ne0}a_{r_N}(k)|\widehat\eta_N(t,k)|^2
            \le C N^{-q},\qquad q=1-s/d.
 \tag{3.6}
\]

For \(0<|k|\le N^{1/d}\), the interval \([|k|^{-2},2|k|^{-2}]\) lies above \(r_N\), and its integral in (3.3) is at least

\[
 A|k|^{s-d}\int_1^2u^{\alpha-1}e^{-4\pi^2u}du
            =c|k|^{s-d}.
\]

For \(|k|>N^{1/d}\), use \(|\widehat\eta_N(k)|\le1\). Increasing a fixed constant gives the all-frequency bound

\[
 \boxed{\quad
 \mathbb E|\widehat\eta_N(t,k)|^2
       \le\min\{1,CN^{-q}|k|^{d-s}\},\qquad k\ne0.
 \quad}
 \tag{3.7}
\]

It is uniform in deterministic time, N, and all diffusivities considered here, including zero. In particular each fixed Fourier mode tends to zero in mean square even on microscopic critical sequences. No mode beyond the scale at which the right side becomes order one is claimed to be small.

There is also a law-class consequence strictly below criticality. Equations (2.7) and (3.5) imply

\[
 \operatorname{Ent}(F_t)\le C\beta N^{s/d}=CN\lambda_N.
 \tag{3.8}
\]

Partitioning the labels into \(\lfloor N/k\rfloor\) blocks of size k and a possible leftover, entropy relative to product Haar is at least the sum of block entropies. This follows by writing the joint density as its block marginals times the conditional-density ratio and applying convexity to the latter. Exchangeability therefore gives
\(\operatorname{Ent}(F_t^{(k)})\le Ck\lambda_N\) for \(k\le N/2\). For a probability density u, the scalar convexity bound
\(u\log u-u+1\ge (u-1)^2/[2(u+1)]\), followed by Cauchy–Schwarz, gives
\(\|u-1\|_1\le2\sqrt{\operatorname{Ent}(u)}\). Thus each fixed marginal converges in total variation when \(\lambda_N\to0\). At criticality this entropy estimate is only of order N and gives no such total-variation conclusion. Neither statement controls an unbounded, N-dependent corrector-gradient product without an additional uniform-integrability estimate.

## 4. An actual trajectory estimate at low noise

The exact R6 energy identity retains the full force square and the singular Laplacian defect. In the homogeneous model, after restoring the unshifted potential, it gives

\[
 \mathbb EH_N(X_T)+\mathbb E\int_0^T\sum_i|B_i(X_t)|^2dt
       =\nu\,\mathbb E\int_0^T\Delta_{Nd}H_N(X_t)dt
       \le\nu\kappa(N-1)T.
 \tag{4.1}
\]

At positive noise the absolute Laplacian occupation and true energy martingale passage are exactly part of that supplied result. At zero noise use its deterministic identity. Applying the deterministic lower bound (3.5), then exchangeability, proves

\[
 \mathbb E\int_0^T|B_i(X_t)|^2dt
           \le C N^{-q}+\nu\kappa T.
 \tag{4.2}
\]

For consistent Euclidean lifts, the difference between \(X_i(t)\) and
\(X_i(0)+\sqrt{2\nu}W_i(t)\) is precisely \(\int_0^tB_i(X_a)da\). Cauchy–Schwarz in time and the fact that torus distance is bounded by lifted distance give

\[
 \mathbb E\sup_{t\le T}\operatorname{dist}
       (X_i(t),X_i(0)+\sqrt{2\nu}W_i(t))^2
           \le C_T(N^{-q}+\nu).
 \tag{4.3}
\]

The Brownian maximum has mean square at most \(4dT\), by the elementary L2 martingale maximal inequality. Consequently the same bound, with a larger fixed constant, holds for \(\mathbb E\sup_{t\le T}\operatorname{dist}(X_i(t),X_i(0))^2\). On a critical sequence, \(\nu_N=N^{-q}/\lambda_N\), so this is \(O(N^{-q})\). This controls each labelled particle on the fixed torus scale, and still permits microscopic rearrangements. It is not a control of singular pair observables evaluated at shrinking separations.

## 5. Both responses and a uniform L1 bound for the genuine inverse

The following avoids importing the conditional R9 pointwise energy estimate. The backward Fourier test has uniformly bounded derivatives through any fixed order, with bounds depending on the corresponding absolutely summable Fourier seminorm of h. The source therefore obeys

\[
 \sup_{t,N,\nu}\|J_t\|_{L^1(dxdy)}\le C_h,
 \tag{5.1}
\]

because its local singularity is at most a multiple of \(|x-y|^{-s}\). The supplied Borel pair measure inequality (R5 (9.3)), in this zero-transport homogeneous case, is

\[
 \|S_{t,a}v\|_1\le e^{2\kappa(a-t)/N}\|v\|_1.
 \tag{5.2}
\]

For \(\mu=1\), the exact responses are

\[
 R_xv(x,y)=-\int v(x+w,y)D(dw),\quad
 R_yv(x,y)=-\int v(x,y+w)D(dw),\quad
 \|R_x+R_y\|_{1\to1}\le2\|D\|_{\rm TV}.
 \tag{5.3}
\]

Tonelli and translation invariance prove this L1 bound, including the Coulomb atom and compensation. The base source potential has L1 norm at most \(TC_he^{\kappa T}\). Apply (5.2) and (5.3) to each ordered time-simplex term of the exact full Volterra inverse. The intervening intervals sum to at most T, so their exponential factors occur only once. Summation gives

\[
 \boxed{\quad \sup_{t,N,\nu}\|\Phi_t\|_1\le C_h.\quad}
 \tag{5.4}
\]

Every term is the supplied Borel inverse term; its L1 series is absolutely summable, so the identification is legitimate. No response has been removed, replaced by a local drift, or assumed to be a Markov generator.

For completeness, the background projection is better behaved than a crude full gradient bound suggests. Translation covariance and linearity of the inverse imply
\(\Phi[h](x+v,y+v)=\Phi[h(\cdot+v)](x,y)\). Difference quotients of h in each of its summable Fourier seminorms converge to the corresponding derivative. Equation (5.4) therefore supplies every common-translation weak derivative of \(\Phi\) in L1, uniformly in N and diffusivity. If
\(q_t(x)=\int\Phi_t(x,y)dy\), translation in the integrated variable shows that every derivative of q has a uniform L1 bound. Fourier coefficient estimates using an arbitrary number of these derivatives show

\[
 \sup_{t,N,\nu}\|q_t\|_{C^m}<\infty\quad\text{for every fixed }m.
 \tag{5.5}
\]

The same argument shows \(\int\Phi_t=0\): averaging h over all common translations leaves only its constant mode, whose source and inverse are zero. Common-translation invariance of the actual law then gives \(\mathbb EP_N[\Phi_t]=0\). This is an exact homogeneous expectation statement, not concentration or noise control.

## 6. Actual noise vanishes for explicit smoothings of the full inverse

Let \(0<\delta\le1\) and smooth in both slots:

\[
 \Psi_{t,\delta}=e^{\delta\Delta_x}e^{\delta\Delta_y}\Phi_t,
 \qquad G_\delta=\nabla_x\Psi_\delta,
 \quad A_\delta(x)=\int G_\delta(x,y)dy.
 \tag{6.1}
\]

This is a smoothing of the actual full inverse, not the inverse of a different truncated generator. It retains its dependence on N, diffusivity, h, and both responses. Equation (5.4) bounds each Fourier coefficient of \(\Phi_t\). Hence, writing \((G_\delta)_k(x)\) for the y-Fourier coefficient,

\[
 \sup_x|(G_\delta)_k(x)|
    \le C\delta^{-(d+1)/2}e^{-4\pi^2\delta|k|^2},\qquad
 \|G_\delta\|_\infty\le C\delta^{-(2d+1)/2}.
 \tag{6.2}
\]

For the first inequality, sum \(2\pi|p|e^{-4\pi^2\delta|p|^2}\) over the x frequencies. The bound on this lattice sum follows by comparison on unit lattice cubes with the radial Gaussian integral; it is \(C\delta^{-(d+1)/2}\). The same comparison gives

\[
 S_\delta:=\sum_{k\ne0}|k|^{(d-s)/2}
                         \sup_x|(G_\delta)_k(x)|
       \le C\delta^{-(5d-s+2)/4}.
 \tag{6.3}
\]

The exact derivative of (1.4), including the missing self label, is

\[
 \nabla_iP_N[\Psi_\delta]
 =\frac1N\left[v_\delta(X_i)
                  -\frac1N G_\delta(X_i,X_i)\right],
 \quad
 v_\delta(x)=\int G_\delta(x,y)(\eta_N-dy)(dy).
 \tag{6.4}
\]

Only this smooth diagnostic takes the diagonal value in (6.4). No diagonal value of the singular full inverse or its derivative is prescribed. Expand \(v_\delta\) in y-Fourier modes. Pointwise in x it is bounded by
\(\sum_{k\ne0}\sup_x|(G_\delta)_k(x)|\,|\widehat\eta_N(k)|\). Minkowski in the actual probability space and (3.7) give

\[
 \mathbb E\sup_x|v_\delta(x)|^2\le CN^{-q}S_\delta^2.
 \tag{6.5}
\]

There is no independence between \(X_i\) and \(\eta_N\) in this argument; the pointwise supremum makes it unnecessary. Substitution into the exact physical bracket functional gives, with
\(r_*=(5d-s+2)/2\),

\[
\begin{split}
 Q_N[\Psi_\delta]
 &\le C\nu b_N\left[N^{-q}\delta^{-r_*}
                        +N^{-2}\delta^{-(2d+1)}\right]\\
 &\le C N^{-q}\delta^{-r_*}.
\end{split}
 \tag{6.6}
\]

Here \(\nu b_N\le1\), \(q<1\), and \(r_*\ge2d+1\). The first line retains the exact diffusivity factor; the second is a uniform simplification. The calculation uses \(2\nu Nb_N\), the N particle gradients, and their squared \(1/N\) factor exactly once each. For a fixed smoothing this proves actual-law noise smallness on the full admitted temperature range, including critical sequences.

It also allows a prescribed smoothing scale to vanish. Set

\[
 \gamma=\frac{q}{2r_*}=\frac{d-s}{d(5d-s+2)},\qquad
 \delta_N=N^{-\gamma}.
 \tag{6.7}
\]

Then

\[
 \boxed{\quad Q_N[\Psi_{\delta_N}]\le C N^{-q/2}\longrightarrow0.\quad}
 \tag{6.8}
\]

The physical smoothing length is \(\sqrt{\delta_N}\). This estimate does not describe the unsmoothed kernel at that length or assert that its discarded gradients are negligible.

## 7. The precise remaining assertion, with all label contractions

For the genuine kernel let \(G=\nabla_x\Phi\), \(A(x)=\int G(x,y)dy\), and \(H(x,y)=G(x,y)-A(x)\). The full supplied domain premise makes these quantities and the following expectations well-defined for each finite N. Differentiation of the literal ordered-pair statistic gives

\[
 \nabla_iP_N[\Phi]
    =N^{-2}\left[\sum_{j\ne i}H(X_i,X_j)-A(X_i)\right].
 \tag{7.1}
\]

Expanding the square, with \(j=k\) kept separately from the three distinct labels, proves

\[
\begin{split}
 Q_N[\Phi]=\frac{2\nu b_N}{N^2}\int_0^T\big[&
 (N-1)\mathbb E|H_{12}|^2
 +(N-1)(N-2)\mathbb EH_{12}\cdot H_{13}\\
 &-2(N-1)\mathbb EH_{12}\cdot A_1
 +\mathbb E|A_1|^2\big]dt.
\end{split}
 \tag{7.2}
\]

The distinct-triple term is absent for N=2. No X3 is then introduced. Although that triple expectation can have either sign, the entire bracketed combination is nonnegative. The one-body Haar marginal identifies the last term with its Haar integral; it does not factor either other marginal.

Define the residual
\(V_N=\Phi-\Psi_{\delta_N}\), using exactly (6.7). Linearity of the statistic and Minkowski in the space of particle-gradient integrands on probability times time show

\[
 \big|\sqrt{Q_N[\Phi]}-\sqrt{Q_N[V_N]}\big|
       \le\sqrt{Q_N[\Psi_{\delta_N}]}\longrightarrow0.
 \tag{7.3}
\]

Consequently the full target is **equivalent**, on every admitted sequence, to the single remaining estimate

\[
 \boxed{\qquad Q_N[\Phi-\Psi_{\delta_N}]\longrightarrow0.
                   \qquad\text{OPEN}\qquad}
 \tag{7.4}
\]

This equivalence also identifies a counterexample exactly: a positive limsup of this residual noise functional is a positive limsup of the genuine one, and conversely. Formula (7.2), applied to V_N and its own G, A, H, displays every two-label, distinct-triple, and background contraction required for (7.4).

An alternative equivalent form is
\(\lim_{\delta\downarrow0}\limsup_{N\to\infty}Q_N[\Phi-\Psi_\delta]=0\), since every fixed smoothing has vanishing Q by (6.6) and the same triangle inequality applies. For each fixed N the reversed smoothing limit does hold: heat smoothing converges in Haar H1, the fixed-N domain bound dominates the time integral, and the finite-N density domination transfers convergence to the particle expectation. That argument has an N-dependent density constant and does not interchange the limits.

The exact first failed inference in the attempted proof is replacing this fixed-N H1 convergence by the uniform statement (7.4). Neither (2.8), the fixed-marginal entropy bound, nor the Fourier estimate (3.7) supplies uniform integrability for the N-dependent singular products of residual gradients. At criticality, (3.7) becomes noninformative precisely at growing frequencies of particle-spacing order. The supplied derivative weights have N-dependent constants, while the reference energy is integrated against Haar. Applying the available N-body density supremum to it restores an exponential in N. Thus the remaining point is a genuine singular actual-law estimate, not a missing coefficient or a change of centering.

## 8. Independent falsification: exact initial BBGKY sign

Let \(F_t^{(k)}\) be the actual k-label marginal. For globally smooth tests, local Itô and finite-N density domination justify all force integrals because \(K\in L^1\). Integrating over unused labels gives the weak hierarchy

\[
\begin{split}
 \partial_tF^{(k)}={}&\nu\sum_{i=1}^k\Delta_iF^{(k)}
 -\frac1N\sum_{\substack{i,j\le k\\i\ne j}}
                    \nabla_i\cdot(K_{ij}F^{(k)})\\
 &-\frac{N-k}{N}\sum_{i=1}^k\nabla_i\cdot
                 \int K(x_i-y)F^{(k+1)}(x_1,\ldots,x_k,y)dy.
\end{split}
 \tag{8.1}
\]

The last line is absent at k=N. At time zero every marginal is product Haar, and \(\int K=0\). In the sense of distributions,

\[
 \left.\partial_tF_t^{(k)}\right|_{0}
              =-\frac2N\sum_{1\le i<j\le k}D(x_i-x_j).
 \tag{8.2}
\]

Here is a time-zero justification for the singular force. For a globally smooth test a, \(L_Na\) is Haar L1. The density bound gives a common finite supremum for \(0\le t\le t_0\) at each fixed N; the laws converge weakly to Haar at zero by path continuity. Approximate \(L_Na\) in L1 by continuous functions. The density bound controls the approximation error uniformly on this short interval, and weak convergence handles the continuous approximant. Thus \(\mathbb E L_Na(X_t)\to\int L_Na\), and the integral Itô identity differentiates at zero. Integration by parts against the finite distribution D gives (8.2), including its Coulomb atom. It is not a pointwise density derivative assertion at a collision.

Now take any real smooth vector kernel \(H_t(x,y)\) with
\(\int H_t(x,y)dy=0\), C1 in time near zero. For N at least three set

\[
 C_N(t)=\mathbb E H_t(X_1(t),X_2(t))\cdot H_t(X_1(t),X_3(t)).
\]

The reference integral is identically zero at every time, so its time derivative contributes zero. In (8.2), the D12 and D13 terms vanish by integrating the remaining centered partner. Only D23 survives. Therefore

\[
\begin{split}
 C_N(0)&=0,\\
 C_N'(0)&=-\frac2N\int dx\int H_0(x,y)\cdot H_0(x,z)D(y-z)\,dy\,dz\\
 &=-\frac2N\int dx\sum_{k\ne0}d_k|\widehat H_0(x,k)|^2\le0,\\
 d_k&=4\pi^2c_{d,s}|k|^{s+2-d}>0.
\end{split}
 \tag{8.3}
\]

The finite-measure convolution in the second line is interpreted by integrating in the difference variable. Its Fourier identity holds first for finite sums and then for smooth H by absolute convergence. The constant compensation disappears because of exact partner centering, not because it was dropped. At Coulomb this is exactly

\[
 C_N'(0)=-\frac{2c_d}{N}\|H_0\|_2^2,
 \qquad c_d=(d-2)|\mathbb S^{d-1}|.
 \tag{8.4}
\]

The diffusivity does not occur in (8.3), because diffusion applied to initial product Haar contributes zero. The smoothing in Section 6 supplies genuine-corrector smooth probes to which this identity applies, with their fixed-N time regularity from the domain premise. More generally (8.3) is an actual-dynamics assertion for every stated smooth centered probe.

This demotes an initial positive-three-label-correlation falsification route. It does not prove that the covariance stays negative, or that its time integral is small for the N-dependent singular probe. The proof differentiates at fixed N and fixed smoothing. A uniform remainder that survives N tending to infinity and smoothing removal is not supplied, so (8.3) is not presented as an asymptotic counterexample or an unsmoothed Taylor expansion. At later times the last line of (8.1) genuinely involves further labels; its sign cannot be inferred from the initial D-convolution form.

## 9. What the supplied reference bound does rule out at short times

This paragraph is explicitly conditional on the supplied R9 integrated Haar-energy result, in addition to its stated domain premise. Write \(a=s/(s+2)<1\). That result gives a full-horizon reference noise upper bound \(Cb_NN^{a-1}\). Since the actual iid-Haar particle density obeys \(F_t\le e^{\kappa(N-1)t}\), nonnegativity alone gives, for any \(0\le\tau\le T\),

\[
 Q_N^{[0,\tau]}[\Phi]\le Cb_Ne^{\kappa(N-1)\tau}N^{a-1}.
 \tag{9.1}
\]

For \(0<\theta<1-a\), choose
\(\tau_N=\min\{T,\theta\log N/[\kappa(N-1)]\}\). The Riesz case has a finite positive admissible \(\kappa\). Then

\[
 Q_N^{[0,\tau_N]}[\Phi]\le Cb_NN^{-(1-a-\theta)}\to0.
 \tag{9.2}
\]

This excludes an entire initial interval as the sole source of a positive limiting bracket, subject to the stated R9 condition. It uses only its integrated reference estimate; the extra pointwise estimate in that reconstruction is not imported. The interval tends to zero, so this does not bound the remaining fixed horizon. No exponential density bound is promoted to a uniform-in-N law estimate.

## 10. Diagnostics, hostile self-check, and claim dispositions

The independent standard-library checker differentiates the literal ordered-pair statistic and applies a literal finite-particle Fourier generator to the three-label product. It does not read or import an earlier checker. Arithmetic lies in the Gaussian rationals, so every equality is exact. The first coordinate of the torus suffices for these coefficient diagnostics in every admitted dimension; a finite Fourier kernel is a smooth diagnostic, not a replacement for the singular Riesz model.

Run:

```text
python3 VERIFICATION_CODE/round010_actual_law_exact.py
```

The result is **PASS, 1,421 exact assertions**. The companion JSON records the assertion count, exact outcome, Fourier scaling convention, and all twenty input hashes. Cases include N=2 through 5 for pair gradients; N=3,4,5, zero and positive noises, several symmetric/additive/mixed/constant kernels for the actual initial three-label generator derivative; positive and zero convolution energies; both canceled partial contractions; exact smooth Fourier self-diagonal energy subtraction for N=2 through 9; and rational dimension/exponent checks for the heat floor and explicit smoothing rate. No random seed or floating-point tolerance is involved. A physical first derivative is \(2\pi\) times the implemented derivative; the physical generator is \((2\pi)^2\) times the implemented one, and the gradient-product time derivative restores \((2\pi)^4\).

The strongest new arguments were challenged as follows. These are self-checks, not independent certification.

| Challenge | Resolution or exact remaining failure |
|---|---|
| Could free-energy dissipation have been applied directly across singular collisions? | It is used only for the smooth heat dynamics, followed by the supplied fixed-N path passage and a common lower bound. No singular Fisher-information identity is needed. |
| Does the energy floor silently omit the N-particle self diagonal? | The exact subtraction is \(g^{>r}(0)/2\); the error from low heat times has \((N-1)/2\). Both are retained before choosing the scale. |
| Could the Fourier bound assume positive-time iid structure? | Its only law input is the actual expectation (2.6). Positivity is a deterministic Fourier identity. |
| Does a labelled force-energy estimate control each pair-force square? | No. Section 4 retains the complete total-force square and makes no such extraction. |
| Does smoothing change the pair inverse or remove responses? | It smooths the already constructed full inverse. The L1 estimate keeps the exact two signed response operators throughout. |
| Is a smooth diagonal trace silently applied to the genuine singular kernel? | The diagonal in (6.4) is used only for \(\Psi_\delta\). The unsmoothed formula (7.1) uses deleted labels exclusively. |
| Do low-mode control or subcritical total variation imply uniform integrability of singular derivatives? | No. This is the first failed implication, isolated as (7.4). |
| Is the initial derivative an asymptotic counterexample? | No. It has a nonpositive sign and no claimed uniform singular remainder. The full target remains unfalsified. |
| Is the Coulomb compensation absent from the BBGKY sign? | It cancels only after integrating the exactly centered probe, leaving the explicit \(c_d\) in (8.4). |
| Could the extra R9 pointwise energy assertion be used without its separate audit? | It is not used. Only the expressly conditional integrated estimate enters Section 9. |

| New or examined claim | Disposition |
|---|---|
| Actual singular expected energy at most zero; uniform pair Riesz-energy moment | PROVED HERE FROM THE SUPPLIED PARTICLE/KERNEL MODULES; SELF-CHECKED |
| Deterministic \(N^{s/d}\) floor and actual Fourier estimate (3.7) | PROVED HERE; SELF-CHECKED |
| Actual fixed-marginal entropy bound in full subcriticality | PROVED HERE, FOR POSITIVE DIFFUSIVITY; SELF-CHECKED |
| Labelled total-drift and low-noise trajectory estimates | PROVED FROM THE SUPPLIED EXACT ENERGY IDENTITY AND THE NEW FLOOR; SELF-CHECKED |
| Uniform L1 full inverse and smooth background projection | PROVED FROM THE SUPPLIED FULL PAIR MODULES; SELF-CHECKED |
| Actual noise for progressively less smoothed genuine inverses, (6.8) | PROVED HERE; SELF-CHECKED |
| Equivalence of full target with residual estimate (7.4) | PROVED GIVEN THE FULL DOMAIN PREMISE; SELF-CHECKED |
| Actual initial centered triple derivative and its sign | PROVED FOR SMOOTH CENTERED PROBES; SELF-CHECKED |
| Shrinking initial-window bound | CONDITIONAL ON THE SUPPLIED R9 INTEGRATED ENERGY ASSERTION |
| Genuine singular noise target over fixed T; singular three-label tail | OPEN; NO ADMISSIBLE COUNTEREXAMPLE FOUND |
| Critical fluctuation law, full corrector hierarchy, general backgrounds | NOT CLAIMED |

## 11. Recoverable handoff

The maximal rigorous output is an actual-law estimate and a specified smoothing reduction, not a resolution of the entire target. A successor can resume without reconstructing this context: verify the new energy/Fourier/smoothing proof in a fresh context, then attempt (7.4) for the actual dynamics. An admissible counterexample must make that nonnegative singular-tail functional have a positive limsup; common-translation symmetry, a generic exchangeable law, or a fixed-N initial derivative will not suffice. The next useful estimate must control the genuine two-/three-label gradient products at shrinking spatial scales, or the combined nonnegative expression (7.2), while retaining the exact dynamics and preparation.

No new canonical theorem, obstruction, or audit identifier is assigned. No canonical state or cumulative memorandum is edited. Root integration and any promotion require separate review. All linked output files are named in the accompanying README and output manifest. Issued files and their archive are sealed; any correction must be issued separately rather than changing this report after issuance.
