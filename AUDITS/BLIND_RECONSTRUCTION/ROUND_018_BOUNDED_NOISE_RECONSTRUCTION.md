# AUD055 — whole statement-only reconstruction of THM040

TASK-085. Issued 2026-09-18 UTC. Assigned fresh Astra Max reconstruction lane.

**Disposition: COMPLETE CONDITIONAL RECONSTRUCTION of the entire frozen THM040.** The exact issued R16 source estimate is an express premise, with its source and audit histories unchanged. Subject to that premise, the singular identity, exact Haar centering, all cross brackets, and the actual joint probability limit follow below on the full stated range. No admitted counterexample was found. This report neither certifies R16 nor promotes THM040. Root comparison and a separate hostile review remain required.

The probability passage is proved here, including the needed conditional characteristic-function identity and the passage from characteristic functions to weak convergence. Independence of the initial vector and the martingale at finite N is never asserted. Only smooth one-body tests enter stochastic integrals. No singular pair inverse, singular corrector bracket, reference-law transfer, positive-time iid assertion, or higher hierarchy is used.

## 1. Isolation, exposure, and exact sources

The task and `AUDITS/ROUND_018_BOUNDED_NOISE_BLIND_INPUT_SHA256SUMS.txt` were read first. The prescribed worktree was then created at `/Users/matthewrosenzweig/.codex/worktrees/hocf-r018-bounded-noise-blind`, branch `codex/hocf-r018-bounded-noise-blind`, from `faf6f775a55579722319795cd9a9921e5829a903`. Exactly twelve mathematical/administrative inputs were copied from the root. Each root byte string and each copied byte string matched its prescribed SHA-256 before use. The manifest itself is administrative sealing data. Inherited non-allowlisted worktree files were not inputs.

Only this report and its unique `ROUND_018_BOUNDED_NOISE_BLIND_ARTIFACTS` directory are authored outputs. The bounded assignment supersedes generic directions to read later ledgers, README, frozen campaign specifications, model orchestration, or memory. No current R18 candidate, R17 construction/reconstruction/audit, current R16 audit, root scratch/state/history, prior checker, private source, or other worktree output was read. No external search, dependency installation, child agent, commit, push, canonical edit, publication, or author contact occurred. Ambient app/global instructions and their automatically supplied general memory summary were visible; no memory file was opened and no mathematical assertion was taken from that summary. No constructor proof narrative for THM040 was supplied.

| Prescribed input | Exact use and retained boundary |
|---|---|
| `AGENTS.md` | Mathematical discipline and isolation. General ledger/orchestration actions are outside this bounded lane. |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Unit Haar torus, Fourier convention, coefficient-one Riesz normalization, interaction coefficient, noise and deleted-label convention. |
| `MEMORANDA/ROUND_001_ALGEBRA.md`, Sections 1–2 | Smooth one-body convention. The singular identity is derived anew below; its smooth diagonal assignment is not imported. |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–4 | Complete local heat, force and divergence calculations relevant here. Their constants are checked below. No pair propagator conclusion is needed. |
| `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md` | Scope of the particle module; its OPEN / UNAUDITED / VERSION_LOCKED issued label is not proof. |
| `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, Sections 1–8 | Full stopped particle construction, per-start quantifiers, same-noise heat passage and fixed-N density domination. The arguments needed here are restated in Section 3. No uniform-N density premise is inferred. |
| `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, Sections 2–3 | Complete proved actual energy/Fourier argument, reconstructed in Section 4. None of the pair-inverse/domain or conditional R9 claims elsewhere in the report is a premise. |
| `THEOREMS/THM-031_ACTUAL_FOURIER_SMOOTHING_AND_TAIL.md` | Scope check only. Its label is not substituted for the supplied R10 proof. Its remaining singular corrector-noise gap is irrelevant to the smooth one-body martingale here. |
| `THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md` | Exact source assertion. Its OPEN / UNAUDITED status remains unchanged. |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md`, complete report | Expressly conditional full-source premise, specifically (1.5), (7.4)–(7.6), with its genuine statistic, actual law and uniformity. Exact applicability is checked in Section 6; no fresh certification of that report is claimed. |
| `THEOREMS/THM-040_BOUNDED_DIFFUSIVITY_FINITE_DIMENSIONAL_GAUSSIAN.md` | Entire frozen assertion and negation, with no range, preparation, time, test or covariance repair. |
| `TASKS/ACTIVE/TASK-085_ROUND018_BOUNDED_NOISE_GAUSSIAN_BLIND.md` | Assignment, prohibited exposures, output scope and sealed stopping gate. |

No citation or theorem number from an unseen source is a premise. Basic smooth stopped Itô calculus, finite-dimensional calculus and linear algebra, elementary integral convergence, and iid factorization at time zero are used explicitly. The probabilistic limiting argument is supplied rather than imported by a theorem name.

## 2. Whole assertion and exact negation

Fix an integer \(d\ge3\), \(0<s\le d-2\) with \(s<d/2\), and finite \(T\ge0\). On \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), with mass-one Haar measure and characters \(e^{2\pi i k\cdot x}\), set

\[
\widehat g(0)=0,\qquad \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
\tag{2.1}
\]

For each \(N\ge2\), let \(0\le\nu_N\le\nu_*<\infty\) and \(\nu_N\to\bar\nu\ge0\). The actual singular equation is

\[
dX_i=\frac1N\sum_{\ell\ne i}K(X_i-X_\ell)\,dt+\sqrt{2\nu_N}\,dW_i,
\tag{2.2}
\]

with independent standard \(d\)-dimensional Brownian motions and iid Haar initial positions independent of all drivers. Initial laws for different N need not be placed on one probability space. Put

\[
b(\nu)=\begin{cases}\min(1/\nu,1),&\nu>0,\\1,&\nu=0,\end{cases}
\quad b_N=b(\nu_N),\quad\bar b=b(\bar\nu),\quad
\sigma_N=\sqrt{Nb_N},\quad\eta_N=N^{-1}\sum_i\delta_{X_i}.
\tag{2.3}
\]

The function b is continuous on \([0,\infty)\), including zero and one, and \(0<b_N\le1\), \(\nu_Nb_N\le1\). No rate in the convergence of diffusivities is imposed.

For every fixed positive integer m and fixed deterministic tuple \((t_j,h_j)_{j=1}^m\), \(0\le t_j\le T\), real \(h_j\in C^\infty(\mathbb T^d)\), the assertion is exact Haar one-body centering and

\[
Z_{N,j}=\sigma_N\left(\eta_N(t_j)[h_j]-\int h_j\right)
\ \Longrightarrow\ \mathcal N_m(0,C),
\tag{2.4}
\]

where the Gaussian is allowed to be singular. Set, for \(k\ne0\),

\[
a_k=4\pi^2|k|^2,\qquad D_k=4\pi^2c_{d,s}|k|^{s+2-d}>0,
\qquad L_k=D_k+\bar\nu a_k.
\tag{2.5}
\]

The claimed covariance is exactly

\[
C_{ij}=\bar b\sum_{k\ne0}\widehat h_i(k)\overline{\widehat h_j(k)}
\left[\frac{D_k}{L_k}e^{-(t_i+t_j)L_k}
+\frac{\bar\nu a_k}{L_k}e^{-|t_i-t_j|L_k}\right].
\tag{2.6}
\]

Its equivalent initial Gram plus thermal integral representation is proved in Section 10. Genuine integrability, the singular first-order identity, actual source control, and the full joint limit, rather than merely its covariance, are parts of the assertion being reconstructed.

The exact negation is existence of admitted fixed \(d,s,T,m,(t_j,h_j)\), a bounded convergent diffusivity sequence, and the specified actual preparation for which exact one-body Haar centering fails, required genuine integrability fails, or (2.4) with (2.6) fails. Failure of an estimate in a proposed route, correlation at positive time, a generic exchangeable counterexample, or failure outside the stated exponent/noise/preparation range is not this negation. The proof below rules out the entire negation **conditional on the expressly retained R16 full-source premise**. It does not rule it out unconditionally by assigning that premise an unseen audit status.

## 3. Kernel, actual particle paths and Haar centering

Write \(\alpha=(d-s)/2\ge1\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). For the periodized Gaussian \(p_u\), the normalization is

\[
g(z)=A\int_0^\infty u^{\alpha-1}(p_u(z)-1)\,du.
\tag{3.1}
\]

The small-time Haar L1 integrand is bounded by \(2u^{\alpha-1}\); the large-time nonconstant heat modes decay exponentially. Taking a nonzero Fourier coefficient gives \(A\Gamma(\alpha)/(4\pi^2|k|^2)^\alpha\), exactly (2.1). Substitution \(v=|z|^2/(4u)\) in the central Euclidean Gaussian integral gives exactly \(|z|^{-s}\). The other lattice terms and every derivative are exponentially small at small u on a ball of radius less than one third; the large-time differences are integrable. Thus locally

\[
g(z)=|z|^{-s}+H(z),\quad H\in C^\infty,\qquad
K(z)=s z|z|^{-s-2}-\nabla H(z),\qquad K\in L^1.
\tag{3.2}
\]

The last fact uses \(s+1<d\). The gradient boundary term is \(O(r^{d-1-s})\), so the integrable force is the distributional negative gradient. Denote the finite signed divergence measure by \(\mathcal D=\operatorname{div}K\), to distinguish it from its coefficients \(D_k\). The flux across a radius-r inner boundary is
\(s r^{d-s-2}\int_{\mathbb S^{d-1}}\phi(r\theta)\,dS\).
Consequently, retaining the torus compensation through the zero Fourier mode,

\[
\mathcal D=\begin{cases}s(d-2-s)g_{s+2}\,dx,&s<d-2,\\
c_d(\delta_0-dx),&s=d-2,\end{cases}
\quad c_d=(d-2)|\mathbb S^{d-1}|,
\tag{3.3}
\]

with \(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\) below Coulomb and \(4\pi^2c_{d,d-2}=c_d\) at Coulomb. In particular \(\mathcal D(\mathbb T^d)=0\), \(\widehat{\mathcal D}(k)=D_k\) for \(k\ne0\), and \(\mathcal D\ge-\kappa dx\) for a fixed finite \(\kappa\). Also \(g_*:=\inf_{z\ne0}g(z)\) is finite and negative. These are the exact R4 facts used here, with the normalization checked rather than guessed.

For clarity, the needed R6 actual realization has a direct local proof. For fixed N and \(\nu\ge0\), define

\[
H_N(x)=\frac1N\sum_{i<\ell}g(x_i-x_\ell),\qquad
E_N(x)=H_N(x)-\frac{N-1}{2}g_*\ge0.
\tag{3.4}
\]

Each summand in E is nonnegative, so any partial or simultaneous collision drives E to infinity. Its sublevels are compact in the collision-free configuration space. Smooth even cutoffs of K, equal to K away from decreasing collision neighborhoods, give globally Lipschitz additive-noise equations. Subtracting the continuous Brownian path permits Picard construction, jointly Borel in start, driving path and time. Local uniqueness patches these cutoff solutions up to their exits. On the collision-free domain the complete vector drift is \(B=-\nabla H_N\) and

\[
\Delta_{Nd}H_N=\frac2N\sum_{i<\ell}\Delta g(x_i-x_\ell)
\le (N-1)\kappa.
\tag{3.5}
\]

This uses the punctured inequality only on stopped trajectories. The full measure (3.3), including its atom, is used whenever a distribution is integrated. Stop at the first E-level R, setting that stop to zero if the initial energy is already at least R. Smooth stopped Itô calculus gives

\[
E_N(X_{t\wedge\tau_R})+\int_0^{t\wedge\tau_R}|B|^2\,dr
\le E_N(X_0)+\nu(N-1)\kappa t
+\sqrt{2\nu}\int_0^{t\wedge\tau_R}\nabla H_N\cdot dW.
\tag{3.6}
\]

The stopped martingale is square integrable because its integrand is bounded on the compact sublevel, and zero for starting points already outside it. For a deterministic collision-free start this gives
\(\mathbb P(\tau_R\le T)\le [E_N(X_0)+\nu(N-1)\kappa T]/R\).
A bounded-energy trajectory can continue at every finite endpoint by the local smooth equation. Letting R increase proves global noncollision, for each fixed start almost surely; no common exceptional set over uncountably many starts is asserted. The iid Haar vector is collision-free almost surely, since each of its finitely many pair diagonals has Haar measure zero. Borel dependence and Fubini cover this vector, whose initial energy mean is finite. Continuity on the compact time interval then gives a strictly positive pathwise minimum pair distance. The argument also works at exactly zero noise.

The heat forces \(K_\epsilon=p_\epsilon*K\) converge in C1 away from zero: split K into a locally agreeing smooth part and a distant L1 part and use differentiated Gaussian exponential bounds on the latter. With identical initial vectors and drivers, heat and singular trajectory noises cancel in their difference. Stop the difference at one quarter of the positive singular minimum separation. A local common Lipschitz bound and Gronwall force the stopped difference to zero and prevent that exit for sufficiently small epsilon. Thus the entire family of heat trajectories converges uniformly on the fixed horizon, almost surely at fixed N and diffusivity. No N-uniform rate is asserted or needed.

For the optional fixed-N law integrability used below, the smooth heat flow for each driving path is a diffeomorphism, by forward and backward uniqueness after subtracting that path. Its initial-point derivative obeys the ordinary variational equation. Since

\[
\operatorname{div}_{Nd}B^\epsilon
=\frac2N\sum_{i<\ell}(p_\epsilon*\mathcal D)(x_i-x_\ell)
\ge-(N-1)\kappa,
\tag{3.7}
\]

its positive Jacobian is at least \(e^{-(N-1)\kappa t}\). Change of variables from initial Haar, followed by Brownian expectation, gives \(F_t^\epsilon\le e^{(N-1)\kappa t}\). The almost-sure trajectory passage passes this inequality first on continuous nonnegative tests; increasing continuous open-set approximants and outer regularity give it on Borel sets. Hence the actual law has

\[
F_t\le e^{(N-1)\kappa t}.
\tag{3.8}
\]

This is only a fixed-N statement, never the uniform law estimate used for the limit.

Permutation equivariance gives exchangeability. For each fixed common translation z, translating all particle positions leaves every pair drift unchanged and leaves the Brownian drivers unchanged. Pathwise uniqueness identifies this translated path with the solution from the translated iid vector. That vector has the same Haar product law, independent of the drivers. Thus the actual law at every time is common-translation invariant. Every one-body marginal is translation invariant: a nonzero Fourier coefficient equals its product with \(e^{2\pi i k\cdot z}\) for all z and therefore vanishes. Approximation by trigonometric polynomials identifies it with Haar. In particular

\[
\mathbb E\eta_N(t)[h]=\int h
\quad\text{for every smooth h, every admitted N, noise and deterministic time.}
\tag{3.9}
\]

This is exact first-marginal centering. The N-body law is not asserted to be product Haar at positive time.

## 4. An actual empirical concentration bound from the complete R10 source

The bound required for the first-order cross brackets follows from the actual energy/Fourier part of R10, independently of its unresolved singular-corrector tail. Here is the full needed argument and its zero-noise case.

At fixed \(\epsilon>0\) and \(\nu>0\), the smooth periodic law from density one solves
\(\partial_tF^\epsilon=\operatorname{div}(F^\epsilon\nabla H_N^\epsilon+\nu\nabla F^\epsilon)\).
At this fixed cutoff the coefficients and all their derivatives are bounded. The heat integral equation and smooth approximation give a smooth solution; comparison with \(e^{\pm Ct}\), \(C\ge\|\Delta H_N^\epsilon\|_\infty\), supplies positive lower and finite upper bounds on finite time intervals. Thus entropy differentiation and periodic integration by parts are justified. Direct calculation gives

\[
\frac d{dt}\left[\nu\int F_t^\epsilon\log F_t^\epsilon
+\int H_N^\epsilon F_t^\epsilon\right]
=-\int F_t^\epsilon|\nabla H_N^\epsilon+\nu\nabla\log F_t^\epsilon|^2\le0.
\tag{4.1}
\]

The initial energy and entropy are zero and probability entropy relative to mass-one Haar is nonnegative. Hence \(\mathbb EH_N^\epsilon(X_t^\epsilon)\le0\). Positivity of the heat kernel gives \(H_N^\epsilon\ge (N-1)g_*/2\), independently of epsilon at this fixed N. Section 3's path passage and local uniform kernel convergence imply convergence of these energies almost surely at a fixed time. Fatou after subtracting their common lower bound proves

\[
\mathbb EH_N(X_t)\le0.
\tag{4.2}
\]

No singular entropy derivative, Fisher-information passage, or interchange with \(N\to\infty\) occurs. At \(\nu=0\), the actual noncolliding deterministic gradient flow gives \(dH_N/dt=-|B|^2\le0\), and its integrable initial energy has expectation zero, proving the same inequality directly. Exchangeability and \(|g|\le g+2|g_*|\) now give

\[
\mathbb E g(X_1-X_2)\le0,\qquad
\mathbb E|g(X_1-X_2)|\le2|g_*|,
\tag{4.3}
\]

uniformly in time, N and noise. The local inverse s-power pair-distance moment is therefore uniformly bounded.

For \(0<r\le1\), truncate the heat integral, distinct from smoothing particle dynamics:

\[
g^{>r}=A\int_r^\infty u^{\alpha-1}(p_u-1)\,du,\qquad
q_r(k)=A\int_r^\infty u^{\alpha-1}e^{-4\pi^2|k|^2u}\,du>0
\quad(k\ne0).
\tag{4.4}
\]

The discarded positive heat kernel gives \(g\ge g^{>r}-Ar^\alpha/\alpha\) off zero. The periodized Gaussian bound gives \(0\le g^{>r}(0)\le Cr^{-s/2}\). Exact subtraction of the retained smooth self diagonal yields

\[
H_N\ge\frac N2\sum_{k\ne0}q_r(k)|\widehat\eta_N(k)|^2
-\frac12g^{>r}(0)-\frac{N-1}{2\alpha}Ar^\alpha.
\tag{4.5}
\]

Choose \(r=N^{-2/d}\) only after this deterministic identity/inequality is established, and put \(q=1-s/d>0\). Equations (4.2)–(4.5) give

\[
\mathbb E\sum_{k\ne0}q_{N^{-2/d}}(k)|\widehat\eta_N(t,k)|^2
\le C N^{-q}.
\tag{4.6}
\]

For \(0<|k|\le N^{1/d}\), the integration interval \([|k|^{-2},2|k|^{-2}]\) in (4.4) is above the lower cutoff and gives \(q_r(k)\ge c|k|^{s-d}\). For larger k the empirical coefficient has modulus at most one, and \(N^{-q}|k|^{d-s}>1\). Enlarging C yields

\[
\mathbb E|\widehat\eta_N(t,k)|^2
\le\min(1,CN^{-q}|k|^{d-s}),\qquad k\ne0.
\tag{4.7}
\]

Every constant is independent of deterministic time, N and the admitted diffusivity; the proof includes zero noise. Positivity used here is exactly the displayed positive Fourier truncation, not positivity of a weighted singular kernel. The actual expectation (4.2), not iid at positive time, is the law input.

If \(\psi\) is a smooth deterministic test, absolute Fourier summation and Cauchy–Schwarz in probability imply

\[
\mathbb E|\eta_N(t)[\psi]-\textstyle\int\psi|
\le C N^{-q/2}\sum_{k\ne0}|\widehat\psi(k)|\,|k|^{(d-s)/2}.
\tag{4.8}
\]

For any smooth family with a common sufficiently high C-order norm the sum is uniformly finite: integration by parts bounds coefficients by \(C(1+|k|)^{-M}\), and choose \(M>d+(d-s)/2\). This observation permits the N-dependent deterministic bracket tests below; it does not permit an arbitrary N-dependent singular observable.

## 5. Exact backward tests and the genuine singular first-order identity

Let \(Q^\nu_a\) preserve constants and multiply mode \(k\ne0\) by \(e^{-a(D_k+\nu a_k)}\), for \(a\ge0\). For each terminal pair define, for \(0\le r\le t_j\),

\[
f_{N,j}(r)=Q^{\nu_N}_{t_j-r}h_j,\qquad
\bar f_j(r)=Q^{\bar\nu}_{t_j-r}h_j.
\tag{5.1}
\]

For every nonnegative integer M, absolute Fourier summation gives uniform C-M bounds for these tests and their gradients over N and the relevant r. Indeed all exponential factors have modulus at most one. Since \(s+2-d\le0\), the \(D_k\) are bounded on nonzero lattice modes; one time derivative costs at most two powers of |k| on the bounded noise interval. The tests are C1 in time and smooth in space, including at their endpoints. Modewise convergence and a summable smooth Fourier majorant show

\[
\sup_{0\le r\le t_j}\|f_{N,j}(r)-\bar f_j(r)\|_{C^M}\longrightarrow0.
\tag{5.2}
\]

For each fixed k the exponential convergence is uniform on the compact time interval. This proves (5.2) without a rate for \(\nu_N\to\bar\nu\).

For a real smooth f define only off the pair diagonal

\[
J_f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y)).
\tag{5.3}
\]

The force bound and the gradient difference give \(|J_f(x,y)|\le C_f(1+\operatorname{dist}(x,y)^{-s})\). Equations (4.3) and (3.2) imply integrability of each actual deleted pair term, uniformly over the bounded family (5.1) and deterministic times. Its Haar integrals are absolutely convergent. Write their original contractions as

\[
A_f(x)=\int J_f(x,y)\,dy=-\int K(x-y)\cdot\nabla f(y)\,dy
=-(\mathcal D*f)(x),\qquad \int A_f=\iint J_f=0.
\tag{5.4}
\]

The first equality uses \(\int K=0\); the second is distributional integration by parts against the smooth f, using the entire finite measure (3.3). At Coulomb it is exactly \(A_f=-c_d(f-\int f)\). Both the atom and its Haar compensation contribute. No value of \(J_f(x,x)\) is introduced.

Use exactly the genuine statistic

\[
P_N[J_f]=\frac1{2N^2}\sum_{i\ne\ell}J_f(X_i,X_\ell)
-\frac1N\sum_i A_f(X_i)+\frac12\int A_f.
\tag{5.5}
\]

Before any estimate, oddness of K and the ordered deleted labels give the exact raw interaction identity

\[
\frac1{N^2}\sum_{i\ne\ell}K(X_i-X_\ell)\cdot\nabla f(X_i)
=\frac1{2N^2}\sum_{i\ne\ell}J_f(X_i,X_\ell)
=P_N[J_f]+\eta_N[A_f].
\tag{5.6}
\]

For a deterministic C1-time smooth f, apply smooth one-body Itô calculus only up to the energy exits of Section 3. The stopped identity has the exact drift \(\eta_N[\partial_r f+\nu_N\Delta f]+\) the first term of (5.6). Subtract the Haar time derivative. Since \(\int\Delta f=0\) and \(\int A_f=0\), putting \(\rho_N=\eta_N-dx\) gives

\[
d\rho_N[f]
=\{\rho_N[\partial_r f+\nu_N\Delta f-\mathcal D*f]
+P_N[J_f]\}\,dr
+\frac{\sqrt{2\nu_N}}N\sum_i\nabla f(X_i)\cdot dW_i.
\tag{5.7}
\]

The force is smooth on each stopped compact configuration set. To remove stopping, noncollision makes the stopping intervals exhaust the horizon almost surely. The deterministic smooth terms are bounded. The source has integrable probability-time absolute value by (4.3)–(5.5) and Tonelli. Bounded one-body gradients make the stopped martingales converge in L2 to their unstopped stochastic integrals. Equivalently the continuous pathwise identity extends by local exhaustion and the same bounds make every displayed integral genuine. Thus (5.7) is an actual singular identity, not a formal substitution in the smooth full-product formula. At zero noise its stochastic integral is identically zero without dividing by noise.

The backward tests satisfy exactly

\[
\partial_r f_{N,j}+\nu_N\Delta f_{N,j}-\mathcal D*f_{N,j}=0,
\qquad f_{N,j}(t_j)=h_j.
\tag{5.8}
\]

Multiplying the integrated (5.7) by \(\sigma_N\) therefore gives simultaneously for every member of the finite tuple

\[
Z_{N,j}=I_{N,j}+M_{N,j}(T)+R_{N,j},
\tag{5.9}
\]

where

\[
\begin{split}
I_{N,j}&=\sqrt{b_N/N}\sum_{\ell=1}^N
\left(f_{N,j}(0,X_\ell(0))-\int h_j\right),\\
M_{N,j}(u)&=\frac{\sqrt{2\nu_N}\,\sigma_N}{N}
\sum_{\ell=1}^N\int_0^{u\wedge t_j}
\nabla f_{N,j}(r,X_\ell(r))\cdot dW_\ell(r),\quad 0\le u\le T,\\
R_{N,j}&=\sigma_N\int_0^{t_j}P_N[J_{f_{N,j}(r)}](X(r))\,dr.
\end{split}
\tag{5.10}
\]

The indicators at a terminal time can be taken predictable, e.g. \(1_{[0,t_j]}\); changing a deterministic endpoint does not change these integrals. The processes M are continuous true square-integrable martingales in the filtration enlarged by the independent initial vector. No independence of M and that initial vector follows from this fact.

## 6. Exact applicability of the conditional full R16 source premise

For each fixed j apply the issued complete R16 source statement with terminal horizon \(t_j\), the same fixed \(h_j\), the same \(d,s\), the same bounded interval \([0,\nu_*]\), and the actual solution (2.2). The terminal horizon and h do not change with N. The f in R16 is exactly (5.1), since both use \(D_k+\nu_Na_k\) in the same normalization. Its J is exactly (5.3), and its three original Haar contractions, ordered denominator \(N^2\), one-half factor and deleted labels are exactly (5.5). R16 includes zero diffusivity, the entire sub-Coulomb/Coulomb range here, arbitrary fixed smooth tests, and deterministic times including zero and the terminal time. It does not require positive-time iid laws. Thus its asserted constant \(C_j\) is independent of N and the chosen \(\nu_N\):

\[
\sup_{0\le r\le t_j}\mathbb E|P_N[J_{f_{N,j}(r)}](X(r))|
\le C_j N^{s/d-1}.
\tag{6.1}
\]

This is the **expressly conditional full-source premise** in this report. R16's complete proof was supplied and read; its heat-splitting scale is separate from the particle heat passage, and its conclusion is a genuine actual-law L1 estimate. Its history remains PROVED CANDIDATE / SELF-CHECKED / pending its own gates as issued. Reading or checking its applicability here does not change that history.

Joint measurability follows from the Borel particle realization and the off-diagonal smooth kernel/test. Therefore Tonelli, (6.1), and \(b_N\le1\) give

\[
\mathbb E|R_{N,j}|\le C_jt_j\sqrt{b_N}\,N^{s/d-1/2}\longrightarrow0,
\tag{6.2}
\]

since \(s<d/2\). Summing finitely many such bounds proves \(R_N\to0\) in L1 in any fixed Euclidean norm. For \(t_j=0\) the residual is exactly zero; no division by that horizon is involved. This is the only place where the conditional R16 quantitative source premise, and the strict exponent inequality, enter the new limit proof.

## 7. Exact cross brackets and their actual-law deterministic limits

Independence of different Brownian drivers, rather than independence of particles, gives

\[
\langle M_{N,i},M_{N,j}\rangle_u
=2\nu_Nb_N\int_0^{u\wedge t_i\wedge t_j}
\eta_N(r)[\nabla f_{N,i}(r)\cdot\nabla f_{N,j}(r)]\,dr.
\tag{7.1}
\]

The coefficient is obtained by squaring \(\sqrt{2\nu_N}\sigma_N/N\), summing the N identical labels, and using \(\sigma_N^2=Nb_N\): no extra factor of N or one half remains. No mixed label term survives the Brownian cross variation. The empirical measure in (7.1) is the actual interacting one.

On the overlapping interval, let \(\psi_{N,ij}(r)=\nabla f_{N,i}(r)\cdot\nabla f_{N,j}(r)\). Product differentiation and Section 5 give a common C-M bound for every fixed M, hence a common weighted Fourier sum in (4.8). Define the deterministic matrix

\[
B_{N,ij}=2\nu_Nb_N\int_0^{t_i\wedge t_j}\int
\nabla f_{N,i}(r)\cdot\nabla f_{N,j}(r)\,dx\,dr.
\tag{7.2}
\]

Equation (4.8), applied to this deterministic smooth family, and \(\nu_Nb_N\le1\), show

\[
\mathbb E|\langle M_{N,i},M_{N,j}\rangle_T-B_{N,ij}|
\le C_{ij}T N^{-q/2}\longrightarrow0.
\tag{7.3}
\]

This is concentration of the actual bracket, not just calculation of its expectation. In fact the same bound controls the supremum of the corresponding cumulative difference, by placing the absolute value inside the time integral, although no path-space limit is asserted. Equations (5.2) and continuity of \(\nu b(\nu)\) imply

\[
B_{N,ij}\longrightarrow B_{ij}:=
2\bar\nu\bar b\int_0^{t_i\wedge t_j}\int
\nabla\bar f_i(r)\cdot\nabla\bar f_j(r)\,dx\,dr.
\tag{7.4}
\]

For every fixed real vector v, \(M_N^v=\sum_jv_jM_{N,j}\) has nonnegative bracket V with the deterministic bound

\[
0\le V_N:=\langle M_N^v\rangle_T
\le2T\left(\sum_j|v_j|\sup_{N,r}\|\nabla f_{N,j}(r)\|_\infty\right)^2=:K_v<\infty.
\tag{7.5}
\]

Equations (7.3)–(7.4) give \(\mathbb E|V_N-v^TBv|\to0\). These statements remain true at T=0 and for exactly vanishing noise. When \(\bar\nu=0\), the sharper direct bracket bound with its factor \(\nu_Nb_N\) already tends to zero, so the thermal martingale vanishes in L2 on every such cooling sequence. No microscopic coupling restriction is used.

## 8. The initial triangular tests and their joint limit

Put \(\phi_{N,j}=f_{N,j}(0)-\int h_j\) and \(\phi_j=\bar f_j(0)-\int h_j\). All have Haar mean zero. The test replacement is a variance identity, not a pointwise bound multiplied by \(\sqrt N\). If

\[
\widetilde I_{N,j}=\sqrt{\bar b/N}\sum_{\ell=1}^N\phi_j(X_\ell(0)),
\]

then initial iid factorization gives exactly

\[
\mathbb E|I_{N,j}-\widetilde I_{N,j}|^2
=\|\sqrt{b_N}\phi_{N,j}-\sqrt{\bar b}\phi_j\|_{L^2(dx)}^2\longrightarrow0.
\tag{8.1}
\]

Cross labels disappear because the summand is centered. Equation (5.2) and \(b_N\to\bar b\) prove the limit with no rate requirement. Thus the entire finite vector can be replaced in L2.

For completeness the initial iid limit follows by an elementary characteristic calculation. For fixed \(u\in\mathbb R^m\) set \(\phi=\sum_j u_j\phi_j\), real, bounded and centered. The Taylor bound
\(|e^{ix}-1-ix+x^2/2|\le|x|^3/6\) gives

\[
\mathbb E e^{i\sqrt{\bar b/N}\phi(X_1(0))}
=1-\frac{\bar b}{2N}\int\phi^2+O_u(N^{-3/2}).
\tag{8.2}
\]

The Nth power converges to \(\exp[-\bar b\int\phi^2/2]\): for large N the factor is within one half of one, and \(\log(1+z)=z+O(|z|^2)\). Its O-constant is fixed because the tuple is fixed and smooth. Equation (8.1) and \(|e^{ix}-e^{iy}|\le|x-y|\) prove

\[
\mathbb E e^{iu\cdot I_N}\longrightarrow e^{-u^TAu/2},\qquad
A_{ij}=\bar b\int\phi_i\phi_j.
\tag{8.3}
\]

No covariance invertibility is needed. Also \(\sup_N\mathbb E|I_N|^2<\infty\), from the exact initial iid variance and the uniform test bounds.

## 9. Actual joint probability passage, without finite-N independence

Here is the full martingale argument needed. For fixed u,v let \(Y_N=u\cdot I_N\), which is measurable with respect to the initial sigma field, and let \(M_N^v\) and \(V_N\) be as in Section 7. Smooth Itô calculus for the continuous real martingale gives the complex stochastic exponential

\[
E_N(t)=\exp\{iM_N^v(t)+\tfrac12\langle M_N^v\rangle_t\},
\qquad dE_N=iE_N\,dM_N^v,
\tag{9.1}
\]

since \(i^2=-1\) cancels the positive one-half bracket term. By (7.5), \(|E_N(t)|\le e^{K_v/2}\). Its stochastic-integral expectation and conditional initial expectation are legitimate: its integrand has squared norm bounded by \(e^{K_v}\) times the bracket density, whose time integral is at most \(K_v\). Hence it is a true square-integrable complex martingale with

\[
\mathbb E[E_N(T)\mid\mathcal F_0]=1.
\tag{9.2}
\]

Multiplying by the bounded initial variable \(e^{iY_N}\) is now allowed. Let \(b_v=v^TBv\), a deterministic nonnegative number. From (9.2),

\[
\begin{split}
\left|\mathbb E e^{iY_N+iM_N^v(T)}
-e^{-b_v/2}\mathbb E e^{iY_N}\right|
&=\left|\mathbb E\left[e^{iY_N+iM_N^v(T)}
\{1-e^{(V_N-b_v)/2}\}\right]\right|\\
&\le\tfrac12e^{K_v/2}\mathbb E|V_N-b_v|\longrightarrow0.
\end{split}
\tag{9.3}
\]

Here \(0\le b_v\le K_v\), by the bracket convergence, and the elementary mean-value bound justifies the last line. At \(K_v=0\) all terms are identically zero and the conclusion is immediate. Equations (8.3) and (9.3) give for every u,v

\[
\mathbb E e^{iu\cdot I_N+iv\cdot M_N(T)}
\longrightarrow \exp\{-\tfrac12u^TAu-\tfrac12v^TBv\}.
\tag{9.4}
\]

This proves the asymptotic independent joint Gaussian characteristic function; finite-N independence was not used. In particular put \(u=v=\theta\), use (5.9), and bound the characteristic error from the residual by \(|\theta|\mathbb E|R_N|\). Then

\[
\mathbb E e^{i\theta\cdot Z_N}\longrightarrow
e^{-\theta^T(A+B)\theta/2}.
\tag{9.5}
\]

Both A and B are real nonnegative Gram matrices, so a centered Gaussian with covariance A+B exists, for example as a symmetric nonnegative matrix square root applied to an m-dimensional standard normal vector. This construction permits a singular matrix.

We spell out why the characteristic conclusion is the actual weak limit, without citing a martingale limit theorem or leaving a probability gap. The vectors \((I_N,M_N(T))\) have uniformly bounded second moments, since \(\mathbb E|M_{N,j}(T)|^2=\mathbb E\langle M_{N,j}\rangle_T\) and (7.5) applies. They are therefore tight by Markov's inequality. The L1-small R makes Z tight as well. Fix an independent standard Gaussian G in the relevant finite dimension and a smoothing parameter \(\delta>0\). The random vector \(Z_N+\delta G\) has continuous density

\[
p_{N,\delta}(x)=(2\pi)^{-m}\int_{\mathbb R^m}
e^{-i\theta\cdot x}\,\mathbb E e^{i\theta\cdot Z_N}
e^{-\delta^2|\theta|^2/2}\,d\theta.
\tag{9.6}
\]

This follows directly by conditioning the Gaussian density on Z and the elementary Fourier transform of the Gaussian; the integrable Gaussian Fourier factor justifies Fubini. Dominated convergence in (9.6) gives uniform convergence of these densities to that of \(Z+\delta G\), where \(Z\sim\mathcal N_m(0,A+B)\). Uniform convergence on each bounded ball, together with tightness of the smoothed vectors, proves convergence of expectations for bounded continuous functions at each fixed delta: split the integral into that ball and its uniformly small probability tail. Finally, for any bounded continuous F, tightness of Z and all Z_N and uniform continuity of F on each enlarged compact ball give
\(\sup_N|\mathbb EF(Z_N+\delta G)-\mathbb EF(Z_N)|\to0\)
as delta decreases, by first controlling the tails and then \(\mathbb P(\delta|G|>\varepsilon)\). The same holds for Z. Letting delta decrease proves weak convergence in (2.4). This also proves the joint weak limit underlying (9.4), by the identical argument in dimension 2m. Degeneracy is harmless because only the added smoothing Gaussian is required to have a density.

## 10. Covariance, endpoints, zero noise and degeneracies

By (8.3) and (7.4), the resulting covariance is exactly

\[
C_{ij}=\bar b\int\left(Q^{\bar\nu}_{t_i}h_i-\int h_i\right)
\left(Q^{\bar\nu}_{t_j}h_j-\int h_j\right)dx
+2\bar\nu\bar b\int_0^{t_i\wedge t_j}\int
\nabla Q^{\bar\nu}_{t_i-r}h_i\cdot\nabla Q^{\bar\nu}_{t_j-r}h_j\,dx\,dr.
\tag{10.1}
\]

All Fourier series and gradient products here are absolutely summable because h is smooth; a majorant with two additional powers of |k| handles the gradient integral. For \(k\ne0\), \(L_k>0\), even when \(\bar\nu=0\). The initial Fourier coefficient contributes
\(\bar b e^{-(t_i+t_j)L_k}\widehat h_i(k)\overline{\widehat h_j(k)}\).
The thermal integral contributes the same test factor times

\[
2\bar\nu\bar b a_k e^{-(t_i+t_j)L_k}
\int_0^{t_i\wedge t_j}e^{2rL_k}\,dr
=\bar b\frac{\bar\nu a_k}{L_k}
\left(e^{-|t_i-t_j|L_k}-e^{-(t_i+t_j)L_k}\right).
\tag{10.2}
\]

Adding and using \(1-\bar\nu a_k/L_k=D_k/L_k\) proves precisely (2.6). The coefficients are bounded between zero and one, so the final series is absolutely convergent as well. Pairing k with -k makes it real, and (10.1) makes its symmetry and nonnegative definiteness transparent.

* At \(\bar\nu=0\), \(\bar b=1\), \(L_k=D_k>0\), and the thermal term is exactly zero; the covariance is the initial Gram after the nonlocal damping. Even if \(\nu_N>0\) along a cooling sequence, its martingales vanish in L2 by (7.5) with the retained \(\nu_Nb_N\) factor. No old floor, full-subcritical, or finite positive critical coupling assumption appears. This establishes the issued zero-limit clause, without importing an unseen THM039 proof or claiming its audit status.
* If all \(\nu_N=0\), the exact deterministic flow, the same source bound premise, and the initial iid calculation already give the result. It is not obtained by declaring zero the reciprocal of a finite inverse temperature.
* At positive \(\bar\nu\), the thermal covariance in (10.1) persists. The proof includes sequences crossing \(\nu=1\), since b is continuous there, and includes arbitrary slow diffusivity convergence.
* If \(t_i=0\) or \(t_j=0\), the cross-bracket integral vanishes and \(|t_i-t_j|=t_i+t_j\), so (2.6) reduces to the exact initial/evolved cross covariance. If T=0 the entire statement is the initial iid limit, with no time integral and no positive horizon required.
* Constants are preserved by Q, and their gradients and J vanish. A constant terminal test gives an identically zero centered coordinate for every N, and an exactly zero row and column in C, including nonzero constants.
* Repeated times are allowed by the stopped common-time martingales in (5.10), with overlap exactly \(t_i\wedge t_j\). Repeated identical time/test pairs give identical finite-N coordinates and identical limiting coordinates.
* The argument tests every real linear combination and never divides by a variance or inverts C. If \(\theta^TC\theta=0\), both nonnegative Gram contributions in (10.1) vanish in that direction and the limiting scalar is the point mass at zero. Linear relations between tests at a common time are preserved. Tests that are linearly related but observed at different times need not give a singular covariance when the thermal noise is positive; (10.1), rather than an incorrect blanket rank claim, determines the actual degeneracy.
* The Coulomb endpoint within this theorem's strict exponent range is three-dimensional \(s=1\). Its \(\mathcal D=4\pi(\delta_0-dx)\) and \(D_k=4\pi\) give the same identities. No logarithmic or equality-\(s=d/2\) limit is taken.

## 11. Separate falsification route and fresh exact diagnostics

The analytic proof route was duality, an actual empirical law estimate and a conditional characteristic identity. A distinct attempted falsification compares the actual time-zero full-particle generator against the proposed two-time covariance, without deriving its prediction from duality.

Let \(\zeta_k=N^{-1}\sum_i e^{-2\pi i k\cdot X_i}\) for a nonzero fixed k. Initial iid Haar gives \(\mathbb E|\zeta_k(0)|^2=1/N\). Applying the literal coordinate generator to \(\zeta_k\) and multiplying by \(\overline{\zeta_k(0)}\), only one label contraction in its interaction survives at zero: the conjugate label equals the other member of the interacting pair. The same-label contraction integrates K to zero, and a third label integrates its character to zero. The surviving force integral is

\[
(-2\pi i k)\cdot\widehat K(k)
=(-2\pi i k)\cdot(-2\pi i k\widehat g(k))=-D_k.
\]

There are \(N(N-1)\) ordered interacting pairs and denominator \(N^3\). Therefore the actual derivative is

\[
\left.\frac d{dt}\mathbb E[\zeta_k(t)\overline{\zeta_k(0)}]\right|_{t=0}
=-\frac{\nu a_k}{N}-\frac{N-1}{N^2}D_k.
\tag{11.1}
\]

For the equal-time squared modulus, the Brownian quadratic variation contributes \(2\nu a_k/N\). Together with the two diffusion terms this cancels at initial Haar, leaving

\[
\left.\frac d{dt}\mathbb E|\zeta_k(t)|^2\right|_{t=0}
=-\frac{2(N-1)}{N^2}D_k.
\tag{11.2}
\]

These are genuine fixed-N actual-law derivatives. The relevant coordinate generator terms are Haar L1 because K is L1, and the finite-N density bound (3.8) is uniform on a short initial interval. Approximation of those terms in Haar L1 by continuous functions, bounded-density control of the errors, and path continuity identify their initial expectations. The integral stopped Itô identity then differentiates at zero. This retains (3.3)'s full distribution when integrated and never presumes a singular Taylor expansion uniform in N.

After multiplication by \(Nb_N\), the limits of (11.1) and (11.2) are respectively \(-\bar b L_k\) and \(-2\bar bD_k\), exactly the derivatives of the proposed initial/evolved and equal-time mode covariances. Thus this falsification route finds no coefficient or sign obstruction. It is not used to interchange differentiation and weak convergence, and is not a proof of the limiting law.

The newly authored standard-library diagnostic `round018_exact_diagnostic.py` is independent of all previous checkers. It uses exact rationals and Gaussian rationals, finite Fourier-polynomial probes and finite formal exponential sums; no simulation, random seed, floating tolerance, dependency installation or singular numerical approximation is involved. Its physical derivative convention and each restored factor are recorded in its JSON output. It checks the literal ordered sums, background signs, finite-N generator contractions, one-body bracket coefficient, initial variance scaling, covariance integral coefficients, repeated/zero times, constant and dependent coordinates, and the conditional-exponential sign. Every intentionally wrong mutation is required to be detected on a nonvacuous probe. Diagnostics support the proof, not the singular premise or the limiting probability argument. Exact counts and commands are recorded in the artifact README and diagnostic JSON.

A separate elementary probability challenge guards the independence inference: if an initial Bernoulli label chooses between Brownian integrands 1 and 2, its terminal martingale has mean zero conditional on the label and zero covariance with that label, but its conditional variance is 1 or 4. Thus it is not independent of the initial label. The exact diagnostic detects this via the mixed second moment and verifies that the positive-half-bracket exponential cancels both conditional variances. This example is a counterexample to a false inference, not an admitted counterexample to THM040. The proof uses deterministic limiting bracket concentration precisely where such a mixture would otherwise persist.

## 12. Whole-claim disposition, vulnerabilities checked and handoff

| Required component | Disposition and dependency |
|---|---|
| Exact actual Haar one-body centering | Reconstructed from translation equivariance, uniqueness and iid Haar preparation, Section 3. No source estimate required. |
| Kernel normalization, finite divergence measure and Coulomb compensation | Checked from the permitted complete heat/flux calculations, Section 3. No pointwise replacement of the divergence measure. |
| Actual singular first-order identity, genuine pair/source integrability and original contractions | Reconstructed by stopped smooth one-body calculus and actual energy integrability, Sections 3–5. No singular diagonal assignment. |
| Quantitative actual source remainder smallness | Complete conditional deduction from exact issued R16 source estimate, Section 6. R16 is neither silently promoted nor weakened. |
| Entire martingale cross-bracket matrix and deterministic limiting values | Reconstructed under the actual law from the complete R10 energy/Fourier argument, Sections 4 and 7. No positive-time iid premise. |
| Initial triangular-test replacement and Gaussian characteristic function | Exact initial variance replacement and bounded iid Taylor expansion, Section 8. No diffusivity rate. |
| Joint law of initial vector and martingale; actual joint weak limit of Z | Direct conditional exponential argument plus a fully supplied Gaussian-smoothing probability passage, Section 9. Finite-N independence is explicitly unnecessary. |
| Both issued covariance formulas and every endpoint/degeneracy clause | Reconstructed in Section 10, including T=0, zero/repeated times, constants, rank deficiency, positive and zero limiting diffusivity. |
| Entire THM040 and its exact negation | Entire assertion reconstructed and exact negation excluded conditionally on the full issued R16 premise. No admitted counterexample found. No independent promotion made. |
| Unconditional certification and comparison with the current candidate | Outside this sealed lane. Root comparison, R16's own gates and separate hostile review remain required. |

The strongest new joint-law claim was challenged at its load-bearing lines. Expectation-only bracket convergence would fail at (9.3); actual L1 concentration (7.3) supplies the missing strength. A random limiting bracket would leave a mixture; its limit here is the fixed Gram matrix (7.4). The bounded complex exponential is a true martingale because its bracket is bounded, not by an unverified formal expectation. A pointwise triangular-test replacement multiplied by \(\sqrt N\) would require a false rate; exact iid variance (8.1) avoids it. Fixed-N density domination is used only for integrability and the time-zero falsification test, never for the uniform bracket concentration. All singular identities are localized before unstopping. Positivity or invertibility of a full covariance matrix is not presumed. The source is L1-small; a source-square estimate is not needed.

There is no failed line in the new conditional implication. The first line that cannot be presented as independently certified in this bounded packet is (6.1), the expressly conditional full R16 actual source estimate. If that source premise were withheld, Sections 3–5 and 7–9 would still prove exact centering, a genuine decomposition, actual Gaussian convergence of the joint initial and smooth-martingale terms, and the exact reduction of the desired Z limit to control of the residual in (5.10). This is the strongest surviving statement without (6.1); covariance algebra alone would not remove that residual. The current packet accepts (6.1) only to the precise extent authorized in TASK-085.

No path-space tightness theorem, distribution-valued topology, growing test family, arbitrary preparation, inhomogeneous background, unbounded diffusivity, logarithmic kernel, exponent beyond the frozen range, higher corrector hierarchy or full flagship campaign conclusion is asserted. Positive finite critical coupling, full microscopic subcriticality, and the older energy-floor condition remain distinct and are not hypotheses added to this card.

Input copies, exposure information, reproducible diagnostic code/results, exact membership lists, input/output manifests and a safe immutable archive are in the unique artifact directory. The README specifies seal verification. Every reported artifact is verified before issuance. Read-only issued bytes must be superseded by a separately named packet if a correction is necessary. No canonical ledger is edited. **Stop here at the complete bounded sealed handoff; root alone compares and decides the next audit or promotion action.**
