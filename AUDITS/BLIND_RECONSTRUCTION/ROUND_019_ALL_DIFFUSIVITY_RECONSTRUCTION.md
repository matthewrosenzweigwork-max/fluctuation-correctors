# AUD057 / TASK088 — whole reconstruction of THM041

Issued 2026-09-18 UTC. Statement-only, bounded reconstruction of the new two-part THM041. **Verdict: the whole frozen assertion is reconstructed below, with no range repair.** This is a fresh reconstruction report awaiting root comparison, a separate hostile gate and exact source-gate mapping. It does not promote THM041, independently certify the allowed R16 constructor, or alter any earlier issued source status. Supporting exact computations are diagnostics, not analytic certification.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r019-all-diffusivity-blind`; branch `codex/hocf-r019-all-diffusivity-blind`; base `faf6f775a55579722319795cd9a9921e5829a903`. No candidate comparison took place before issuance. The task and input manifest were read first, and precisely the eleven allowed files were copied with pre-copy and post-copy SHA-256 checks. Inherited non-allowlisted worktree contents were ignored.

## 1. Assertion, negation and exposure boundaries

Fix integer \(d\ge3\), \(0<s\le d-2\), the coefficient-one Riesz kernel, unit-Haar torus, zero external drift, iid Haar preparation independent of Brownian drivers, and finite \(T\ge0\). At each finite \(\nu\ge0\), the actual particle equation has coefficient \(1/N\) and noise \(\sqrt{2\nu}\). Put

\[
 b(0)=1,\qquad b(\nu)=\min(1,1/\nu)\quad(\nu>0),\qquad
 q=1-s/d>0,\qquad \sigma=\sqrt{Nb}.
\]

Part A claims genuine integrability of the original ordered/deleted source, all Haar contractions retained, and

\[
 \sup_{0\le\nu<\infty}\sup_{0\le r\le T}
 \mathbb E_\nu|P_N[J_{Q_{T-r}^\nu h}](X(r))|\le C_hN^{-q}.
 \tag{A}
\]

The constant depends only on fixed data, not an upper diffusivity bound. Part B additionally assumes \(s<d/2\). For every fixed finite tuple \((t_j,h_j)_{j=1}^m\), it claims the stated uniform bounded-Lipschitz approximation to the centered Gaussian with exactly the frozen covariance, along with exact Haar one-body centering and every finite-limit, divergent-diffusivity, constant-test, zero-time, repeated-time and degenerate-covariance consequence. The proof below gives the full supremum, not only convergent-parameter subsequences.

Its exact negation is a fixed admitted datum violating genuine integrability, a common constant in (A), exact Haar centering, or the uniform approximation or any stated sequence consequence. Failure of a proposed estimate, a changing test list, inadmissible initial preparation, or a path-space assertion is not this negation. The reconstruction excludes that negation within the declared hypotheses, subject to separate review of the proof and source gates. No counterexample is claimed.

The task's restricted reading and single-writer instructions supersede general directions to read current state, README/history, orchestration documents, or memory. The first read consisted only of TASK088 and its manifest. No root R19 candidate/checker/scratch, R17/R18 construction/reconstruction/audit, current R16 audit, current ledger, historical Git content, other worktree, prior checker implementation, external source, or memory file was read. Ambient conversation instructions contain a general memory summary; it was not used as evidence or mathematical input. The complete allowed R16 memorandum, including its account of its own diagnostic, was read; no earlier diagnostic code or output artifact was opened. Its disclosed source mechanism is an allowed source exposure, so this lane claims statement-only blindness to THM041's proposed proof, not blindness to the older R16 source proof. No children, installations, commits, pushes, canonical edits or external contacts occurred. Astra Ultra was the task's authorized bounded escalation; model naming supplies no mathematical evidence.

## 2. Full source preflight and normalization

| Allowed file | Checked use and retained status |
|---|---|
| `AGENTS.md` | Mathematical discipline; bounded isolation controls this lane. |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Unit mass, Fourier characters, coefficient-one kernel, independent noises, ordered deleted labels, denominator \(N^2\), factor \(1/2\). |
| `MEMORANDA/ROUND_001_ALGEBRA.md`, §§1–2 and one-body bracket | The smooth first-order identity and response convention. Section 6 below rederives the actual singular identity with its genuine contractions; no smooth singular diagonal is imported. |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, §§2–3 and heat bounds in §5 | Full local heat construction, integrable force, exact finite divergence measure, Coulomb atom/compensation. Rechecked in §3 below. Its broader pair propagation is unused. |
| `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md` | Frozen scope only; OPEN / UNAUDITED / VERSION_LOCKED remains unchanged. |
| `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, §§3–8 | Entire needed stopped construction, noncollision, measurability, same-noise heat passage and density domination; §3 below reconstructs their finite-parameter mechanisms. No uniform-in-N density estimate or uniform heat rate is imported. |
| `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, §§2–3 | Actual energy sign, exact self subtraction and empirical Fourier control. These are rederived in §§3–5. No inverse/corrector/domain/noise assertion elsewhere in the report is used. |
| `THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md` | Bounded-noise scope and conditional issued history only. This card alone does not prove (A). |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md`, complete allowed memorandum | Its full proof, not its card or status, is checked. Sections 3–5 below reconstruct the kernel/actual-law/commutator/remainder chain and remove the unused upper-noise dependency by explicit constant accounting. Its SELF-CHECKED candidate status is unchanged. |
| `THEOREMS/THM-041_UNIFORM_ALL_DIFFUSIVITY_GAUSSIAN_APPROXIMATION.md` | Entire target and exact negation. No proposed target proof was supplied. |
| `TASKS/ACTIVE/TASK-088_ROUND019_ALL_DIFFUSIVITY_BLIND.md` | Worktree, isolation, whole-statement and sealed-handoff contract. |

No external mathematical statement, theorem number, unverified citation or novelty claim is used. Basic finite-dimensional Picard iteration, smooth Itô calculus, Fourier series, elementary measure convergence and Gaussian integration are used with the needed bounds made explicit. In particular there is no invoked martingale central limit theorem whose uniformity or independence hypotheses must be guessed.

Let

\[
 \alpha=(d-s)/2\ge1,\quad
 A=4^\alpha\pi^{d/2}/\Gamma(s/2),\quad
 c_{d,s}=\pi^{s-d/2}\Gamma(\alpha)/\Gamma(s/2),
\]
\[
 a_k=4\pi^2|k|^2,\quad D_k=4\pi^2c_{d,s}|k|^{s+2-d}>0,
 \quad L_k(\nu)=D_k+\nu a_k\qquad(k\ne0).
 \tag{2.1}
\]

The uppercase \(D_k\) is a Fourier coefficient, while \(D\) below is the divergence measure. There is no substitution \(s=0\), no altered Fourier convention, and no infinite-noise SDE.

## 3. Kernel, actual law and the diffusivity-independent energy sign

Write \(p_u(z)=\sum_{n\in\mathbb Z^d}(4\pi u)^{-d/2}e^{-|z+n|^2/(4u)}\). Gaussian unfolding gives positivity, integral one and multiplier \(e^{-a_ku}\). At large \(u\), every derivative of \(p_u-1\) decays exponentially. At small \(u\), \(\|p_u-1\|_1\le2\). Thus

\[
 g=A\int_0^\infty u^{\alpha-1}(p_u-1)\,du
 \tag{3.1}
\]

converges in Haar \(L^1\), has zero mean, and has nonzero coefficient
\(A\Gamma(\alpha)/(4\pi^2|k|^2)^\alpha=c_{d,s}|k|^{s-d}\). The Euclidean central Gaussian integral is \(|z|^{-s}\), with coefficient one, by \(v=|z|^2/(4u)\). Subtract it from (3.1) on a ball of radius less than \(1/3\). The other translates have bounds by powers of \(u^{-1}\) times \(e^{-c/u}\) at small \(u\), and the large-time remainders and all spatial derivatives are integrable. Hence

\[
 g(z)=|z|^{-s}+H(z),\quad H\in C^\infty(B_{1/3}),\qquad
 K(z)=sz|z|^{-s-2}-\nabla H(z).
 \tag{3.2}
\]

In particular \(K\in L^1\) because \(s+1<d\); its distributional identification follows by the boundary estimate \(O(r^{d-1-s})\). The lower bound \(g_*:=\inf_{z\ne0}g(z)>-\infty\) is negative, by zero mean and the positive singularity. Integrating the divergence outside a ball produces flux
\(s r^{d-s-2}\int_{\mathbb S^{d-1}}\phi(r\theta)dS+O_\phi(r^{d-1})\).
The flux vanishes below Coulomb and equals \(c_d\phi(0)\) at Coulomb. Fourier coefficients and the gamma recurrence therefore give the full measures

\[
 D=\operatorname{div}K=
 \begin{cases}s(d-2-s)g_{s+2}(z)dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \quad c_d=(d-2)|\mathbb S^{d-1}|=4\pi^2c_{d,d-2}.
 \tag{3.3}
\]

Their mass is zero, their nonzero Fourier coefficients are \(D_k\), and \(D\ge-\kappa dz\) for a finite fixed-kernel constant \(\kappa\). Below Coulomb take \(s(d-2-s)\max(0,-\inf g_{s+2})\); at Coulomb take \(c_d\). Fourier identification can be verified by heat-convolving the difference and then testing against smooth functions. On the punctured torus only, \(\Delta g\le\kappa\). Heat mollification retains the whole measure: \(D_\epsilon=p_\epsilon*D\ge-\kappa\), and at Coulomb \(D_\epsilon=c_d(p_\epsilon-1)\).

For fixed \(N\), finite \(\nu\) and collision-free starting state, put

\[
 H_N(x)=N^{-1}\sum_{i<j}g(x_i-x_j),\qquad
 E_N(x)=H_N(x)-(N-1)g_*/2\ge0.
\]

Every energy sublevel is compact and collision-free: each summand \((g-g_*)/N\) is nonnegative, and any colliding pair forces divergence of its own term. This covers partial and simultaneous collisions. The full drift satisfies \(B=-\nabla H_N\), and

\[
 \Delta_{Nd}H_N=\frac2N\sum_{i<j}\Delta g(x_i-x_j)\le(N-1)\kappa.
 \tag{3.4}
\]

Smooth collision cutoffs and subtraction of the continuous Brownian path yield globally Lipschitz integral equations. Picard's factorial difference bound constructs their solutions; Gronwall gives uniqueness and compatibility until each collision-excluded exit. Picard iteration and countable stopping/patching give a jointly Borel, nonanticipating local solution map. Stop this map on first reaching \(E_N=R\); the entire stopped drift and differentiated energy are bounded. Smooth Itô then gives the complete drift \(-|B|^2+\nu\Delta_{Nd}H_N\) and a square-integrable zero-mean martingale. Therefore

\[
 \mathbb E_x E_N(X_{t\wedge\tau_R})\le E_N(x)+\nu(N-1)\kappa t,
 \qquad
 \mathbb P_x(\tau_R\le T)\le\frac{E_N(x)+\nu(N-1)\kappa T}{R}.
 \tag{3.5}
\]

A bounded-energy path at a finite endpoint has a limit in a collision-excluded compact set and extends by a smooth cutoff. Thus (3.5), as \(R\to\infty\), proves global noncollision, and pathwise uniqueness follows from local uniqueness. The complete force square is retained; no individual pair or triple term has been discarded. The same construction at \(\nu=0\) is the deterministic gradient flow. For each realized finite-horizon singular path the minimum pair distance is positive by continuity. The initial iid vector has finite shifted-energy mean \(-(N-1)g_*/2\), so joint measurability and Fubini permit this preparation. No simultaneous exceptional-set assertion over all starts or all diffusivities is needed.

For the actual heat passage, \(K_\epsilon\to K\) in \(C^1\) on each compact set away from zero. To see this, split \(K\) into a smooth function agreeing near that set and an \(L^1\) function supported a positive distance away; differentiated Gaussian bounds control the second convolution by \(C\epsilon^{-M}e^{-c/\epsilon}\). Couple heat and singular paths with the same initial state and Brownian motions. Until their difference reaches one quarter of the singular minimum separation, their noises cancel and Gronwall gives a difference bounded by \(T e_\epsilon e^{CT}\), with \(e_\epsilon\to0\) and a finite path-dependent local Lipschitz constant. This prevents the stop for small \(\epsilon\), proving uniform-in-time almost-sure convergence at each fixed \(N,\nu,T\). This passage needs no constant uniform in \(\nu\) or \(N\).

The smooth heat flow has configuration divergence
\(\operatorname{div}B^\epsilon=(2/N)\sum_{i<j}D_\epsilon\ge-(N-1)\kappa\).
After subtracting the additive Brownian signal it is a differentiable initial-point flow with derivative equation \(\dot J=DB^\epsilon J\); the backward integral equation gives its inverse. Its Jacobian is at least \(e^{-(N-1)\kappa t}\). Pathwise change of variables, followed by Brownian expectation, gives density at most this reciprocal for initial Haar. Continuous-test passage using the preceding path convergence, then increasing approximations of open sets and Haar outer regularity, gives

\[
 F_t\le e^{(N-1)\kappa t}\quad\text{a.e.}
 \tag{3.6}
\]

This fixed-N bound is used below only for the initial-generator falsification check, never as uniform concentration.

For the decisive stronger energy sign, first fix \(\epsilon>0\) and \(\nu>0\). The smooth density solves
\(\partial_tF^\epsilon=\operatorname{div}(F^\epsilon\nabla H_N^\epsilon+\nu\nabla F^\epsilon)\).
Bounded smooth coefficients and the heat integral equation give a classical solution; comparison with constants times \(e^{\pm Ct}\), \(C\ge\|\Delta H_N^\epsilon\|_\infty\), gives positive upper and lower bounds on a finite interval. Entropy differentiation and periodic integration by parts are legitimate and give exactly

\[
 \frac d{dt}\left(\nu\int F^\epsilon\log F^\epsilon+
                         \int H_N^\epsilon F^\epsilon\right)
 =-\int F^\epsilon|\nabla H_N^\epsilon+\nu\nabla\log F^\epsilon|^2\le0.
 \tag{3.7}
\]

Initially both quantities are zero. Entropy is nonnegative on a mass-one configuration space. Therefore \(\mathbb EH_N^\epsilon(X_t^\epsilon)\le0\). Positivity of heat convolution gives the common lower bound \(H_N^\epsilon\ge(N-1)g_*/2\). The fixed-parameter coupled passage and local kernel convergence give almost-sure convergence of these energies. Fatou after subtracting the lower bound proves

\[
 \mathbb E_\nu H_N(X_t)\le0\quad\text{for every }N\ge2,
 \quad0\le\nu<\infty,\quad0\le t\le T.
 \tag{3.8}
\]

At zero noise this follows instead directly from \(dH_N/dt=-|B|^2\le0\), averaged over integrable iid initial energy. There is no singular entropy-dissipation passage and no division by \(\nu\). Although (3.5) and smooth PDE constants can grow with \(\nu\), the conclusion (3.8) has constant zero for every finite \(\nu\). This is exactly why the later uniform supremum is legitimate.

Permutation equivariance gives exchangeability, and common-translation equivariance and uniqueness preserve common-translation invariance of the initial law. The one-body marginal is therefore exactly Haar: equivalently all its nonzero Fourier coefficients vanish under arbitrary translation. Also, from (3.8),

\[
 \mathbb Eg(X_1-X_2)=2\mathbb EH_N/(N-1)\le0,
 \qquad \mathbb E|g(X_1-X_2)|\le2|g_*|.
 \tag{3.9}
\]

Here \(|g|\le g+2|g_*|\). These expectations are finite by the shifted nonnegative-energy Fatou argument. The local inverse-s-th-power distance moment is uniformly bounded by (3.2). No higher-marginal independence is inferred.

## 4. Uniform source estimate from the complete R16 proof

For any real smooth terminal \(h\), let \(f_r^\nu=Q_{T-r}^\nu h\), where the nonzero multipliers are \(e^{-(T-r)L_k(\nu)}\) and the constant multiplier is one. For every real \(p\ge0\), the weighted Fourier seminorm

\[
 \|u\|_{\mathcal A_p}:=\sum_k(1+|k|)^p|\widehat u(k)|
\]

satisfies \(\sup_{\nu<\infty,r\le T}\|f_r^\nu\|_{\mathcal A_p}\le\|h\|_{\mathcal A_p}\). All spatial derivatives needed below are therefore uniform over the whole half-line. At each fixed finite \(\nu\), the time derivative is smooth as well, since \(D_k+\nu a_k\le C(1+\nu)(1+|k|)^2\). A uniform time-derivative norm is neither claimed nor needed.

For \(v=\nabla f\), the original off-diagonal \(J(x,y)=K(x-y)\cdot(v(x)-v(y))\) is bounded by \(C_h(1+\operatorname{dist}(x,y)^{-s})\). Thus its Haar and actual deleted-pair integrability follow respectively from \(s<d\) and (3.9), before using Fourier estimates. Its original one-body and double contractions are

\[
 A_f(x)=\int J(x,y)dy=-\int K(x-y)\cdot\nabla f(y)dy
       =-\int f(x+z)D(dz),\qquad \int A_f=\iint J=0.
 \tag{4.1}
\]

The integrations use \(K\in L^1\), oddness and distributional integration by parts against a smooth function. In particular \(\widehat A_f(k)=-D_k\widehat f(k)\). At Coulomb this is exactly \(-c_d(f-\int f)\), with both atom and compensation. No diagonal value of \(J\) is assigned.

The bounded-noise THM038 card is insufficient here. We now check its complete allowed constructor mechanism with all constants. Fix \(M=d+2\), and, for \(0<r\le2\), set

\[
 w_r(u)=(1-e^{-u/r})^M,\quad\psi_r=1-w_r,
\]
\[
 g_r=A\int_0^\infty u^{\alpha-1}w_r(u)(p_u-1)du,
 \quad Q_r=A\int_0^\infty u^{\alpha-1}\psi_r(u)p_u\,du,
 \quad c_r=A\int_0^\infty u^{\alpha-1}\psi_r(u)du.
 \tag{4.2}
\]

The scale \(r\) is unrelated to the particle heat parameter \(\epsilon\). We have \(Q_r\ge0\), \(\int Q_r=c_r=C_{d,s,M}r^\alpha\), and
\(g=g_r+Q_r-c_r\) in \(L^1\) and off zero. Bounds
\(w_r\le\min(1,(u/r)^M)\) and \(\psi_r\le\min(1,Me^{-u/r})\) prove these assertions. The retained kernel is \(C^2\): its Fourier coefficients

\[
 A_r(k)=A\int_0^\infty u^{\alpha-1}w_r(u)e^{-a_ku}du>0\quad(k\ne0)
 \tag{4.3}
\]

are \(O_r(|k|^{-2\alpha-2M})\), summable with two derivatives since \(2M>s+2\). Its zero coefficient is zero. Gaussian bounds through the split \((0,r),(r,1),(1,\infty)\) give
\(0\le g_r(0)\le C r^{-s/2}\) for \(0<r\le2\).
Define the nonnegative quantities

\[
 E_r(x)=\tfrac12\sum_{k\ne0}A_r(k)|\widehat\eta_N(k)|^2,
 \qquad S_r(x)=\frac1{2N^2}\sum_{i\ne j}Q_r(x_i-x_j).
\]

Exact subtraction of the smooth self diagonal and the constant over precisely \(N(N-1)\) ordered pairs gives

\[
 \frac{H_N}{N}=E_r+S_r-\frac{g_r(0)}{2N}-\frac{N-1}{2N}c_r.
 \tag{4.4}
\]

There is no Fourier representation of the singular self diagonal. The terms are integrable: \(E_r\) is bounded at fixed scale and \(S_r\) follows either from the splitting and (3.9) or this identity. Consequently (3.8) implies

\[
 \mathbb EE_r+\mathbb ES_r\le C(N^{-1}r^{-s/2}+r^\alpha),
 \quad0<r\le2,
 \tag{4.5}
\]

uniformly in every finite \(\nu\) and deterministic time. Positivity is justified separately for each of these two quantities.

For completeness the retained commutator constant is scale independent. Regard \(A_r(\xi)\) as radial for \(\xi>0\). Since \(0\le u w'_r\le M w_r\), integration of
\((u^\alpha w_r e^{-4\pi^2\xi^2u})'\), whose endpoints vanish, yields

\[
 0\le-\xi A_r'(\xi)/A_r(\xi)\le L:=2(\alpha+M).
 \tag{4.6}
\]

For nonzero lattice \(k,\ell\), let \(u=\min(|k|,|\ell|)\ge1\), \(R=\max(|k|,|\ell|)\), \(z=k-\ell\). Integrating (4.6) gives
\(A_r(u)/A_r(R)\le(R/u)^L\) and
\(A_r(u)-A_r(R)\le LA_r(u)(R-u)/u\).
Use \(R-u\le|z|\), \(R/u\le1+|z|\), and the numerator bound
\(|z|A_r(u)+R[A_r(u)-A_r(R)]\) to obtain

\[
 \frac{|kA_r(k)-\ell A_r(\ell)|}{\sqrt{A_r(k)A_r(\ell)}}
 \le(1+L)|z|(1+|z|)^{L/2+1}.
 \tag{4.7}
\]

For the smooth retained source, its diagonal is zero, so its original deleted statistic equals
\(\int v\cdot(K_r*\rho)\,d\rho\), \(\rho=\eta_N-dx\). Absolute Fourier convergence and symmetrization give

\[
 P_N[J_{g_r}]= -\pi i\sum_{k,\ell\ne0}
 [kA_r(k)-\ell A_r(\ell)]\cdot\widehat v(\ell-k)
 \widehat\rho(k)\overline{\widehat\rho(\ell)}.
 \tag{4.8}
\]

For a fixed displacement, Cauchy–Schwarz bounds the convolution of
\(\sqrt{A_r(k)}|\widehat\rho(k)|\) with its translate by its squared \(\ell^2\) norm. Equations (4.7)–(4.8) therefore give

\[
 |P_N[J_{g_r}]|\le2C_v E_r,
 \quad C_v=\pi(1+L)\sum_z|z|(1+|z|)^{L/2+1}|\widehat v(z)|.
 \tag{4.9}
\]

A fixed finite \(\mathcal A_{\alpha+M+3}\) seminorm of \(h\) bounds this constant uniformly in all \(\nu\), by the multiplier bound. No exponential-weight ratio or arbitrary weighted positivity is used.

For \(R_r=g-g_r=Q_r-c_r\), its gradient is integrable: the small-time bound \(\|\nabla p_u\|_1\le Cu^{-1/2}\) is integrable against \(u^{\alpha-1}\), since \(\alpha\ge1\), and the tail decays. For torus distance \(\delta(z)\), each Gaussian translate has \(\delta(z)\le|z+n|\), whence

\[
 \delta(z)|\nabla p_u(z)|\le C_d p_{2u}(z).
\]

This is the elementary bound of \(|z+n|^2u^{-1}e^{-|z+n|^2/(8u)}\) after dividing by the doubled Gaussian. The mean-value bound on \(v\) and substitution \(a=2u\), with \(\psi_r(a/2)=\psi_{2r}(a)\), then show

\[
 |J_{R_r}(x,y)|\le C_d2^{-\alpha}\|Dv\|_\infty Q_{2r}(x-y).
 \tag{4.10}
\]

This controls absolute values, not positivity of a weighted Riesz form. In the original statistic, the three coefficients \(1/(2N^2),-1/N,1/2\) yield respectively \(S_{2r},c_{2r},c_{2r}/2\) as bounds. Thus (4.5) at scale \(2r\) proves

\[
 \mathbb E|P_N[J_{R_r}]|\le C_h(\mathbb ES_{2r}+\tfrac32c_{2r})
 \le C_h(N^{-1}r^{-s/2}+r^\alpha),\quad0<r\le1.
 \tag{4.11}
\]

All integrations use a nonnegative integrable majorant; the double contraction is actually zero by (4.1), but was retained in this bound. Linearity of the genuine off-diagonal statistic combines (4.9), (4.11), and (4.5). Setting \(r=N^{-2/d}\) in the already proved estimate gives exactly
\(N^{-1}r^{-s/2}=r^\alpha=N^{-q}\). This proves (A).

Every constant in (4.2)–(4.11) depends only on \(d,s\), the fixed kernel and a finite spatial seminorm of the same fixed \(h\). The only actual-law input is (3.8), whose bound is independent of finite \(\nu\). No time derivative, upper-noise bound, inverse noise, variable terminal test or unproved singular limit enters. This proves the new all-diffusivity uniformity from the full source proof, while retaining THM038 and the original R16 report as historically conditional issued sources.

## 5. Actual Fourier concentration for every bracket test

Keep \(r_N=N^{-2/d}\) in (4.5). For \(0<|k|\le N^{1/d}\), integrate (4.3) on \([|k|^{-2},2|k|^{-2}]\). On this interval \(u/r_N\ge1\), hence \(w_{r_N}\ge(1-e^{-1})^M\), and
\(A_{r_N}(k)\ge c|k|^{-2\alpha}\), with fixed \(c>0\).
For the remaining modes use \(|\widehat\eta_N(k)|\le1\). Enlarging the fixed constant gives

\[
 \mathbb E_\nu|\widehat\eta_N(t,k)|^2
 \le\min(1,CN^{-q}|k|^{2\alpha}),\quad k\ne0,
 \tag{5.1}
\]

uniformly in \(t\le T,N\ge2,\nu<\infty\). For any smooth deterministic scalar test \(a\), absolute Fourier convergence and Cauchy–Schwarz in probability now imply

\[
 \mathbb E_\nu|\rho_t[a]|\le C N^{-q/2}
       \sum_{k\ne0}|\widehat a(k)||k|^\alpha
 \le C N^{-q/2}\|a\|_{\mathcal A_\alpha}.
 \tag{5.2}
\]

This is an actual-law first absolute-moment bound, not merely a signed mean estimate. It applies uniformly to deterministic families with a common displayed seminorm. The inequality
\((1+|k+\ell|)^p\le(1+|k|)^p(1+|\ell|)^p\) for \(p\ge0\) proves the product estimate
\(\|uv\|_{\mathcal A_p}\le\|u\|_{\mathcal A_p}\|v\|_{\mathcal A_p}\).
Consequently products of any two gradients of the backward tests have a uniform \(\mathcal A_\alpha\) norm, controlled by their fixed terminal \(\mathcal A_{\alpha+1}\) norms. This includes the piecewise time-dependent tests used in all cross brackets below.

## 6. Actual singular first-order identity and complete vector decomposition

For a smooth deterministic \(f_r\), apply Itô to \(N^{-1}\sum_i f_r(X_i)\) up to a collision-excluded energy stop. The interaction term symmetrizes exactly as
\((2N^2)^{-1}\sum_{i\ne j}J_f(X_i,X_j)\). By (4.1), subtracting the original Haar contractions shows this is
\(P_N[J_f]+\eta_N[A_f]\), and \(\int A_f=0\). Thus, on the stopped process,

\[
 d\rho_r[f_r]=\{\rho_r[\partial_rf_r+\nu\Delta f_r-D*f_r]
                  +P_N[J_{f_r}]\}\,dr
     +\frac{\sqrt{2\nu}}N\sum_i\nabla f_r(X_i)\cdot dW_i.
 \tag{6.1}
\]

Here \(D*f(x)=\int f(x+z)D(dz)\), using evenness. For fixed finite \(\nu\), the backward Fourier test solves \(\partial_rf+\nu\Delta f-D*f=0\) with its unchanged constant mode. Its space/time derivatives are bounded at that fixed \(\nu\). The stopped stochastic integrals converge in \(L^2\) as stops exhaust the horizon, by bounded gradient integrands and dominated convergence of their brackets. The source integral converges in \(L^1\) by (A), Tonelli and dominated convergence. The remaining observable terms converge by continuity. This proves the exact identity on the actual singular law, without evaluating a singular diagonal or passing an unbounded force term without its commutator cancellation.

For each pair \((t_j,h_j)\), use its own terminal horizon and set
\(f_{j,r}^\nu=Q_{t_j-r}^\nu h_j\) for \(0\le r\le t_j\). The finite list of Part A constants has a common maximum; horizons are at most \(T\). Write

\[
 Z_{N,\nu}=U_{N,\nu}+M_{N,\nu}+R_{N,\nu},
 \tag{6.2}
\]
\[
 U_j=\frac1{\sqrt N}\sum_{i=1}^N\sqrt b\left(f_{j,0}^\nu(X_i(0))-\int h_j\right),
\]
\[
 M_j=\sqrt{\frac{2\nu b}{N}}\sum_i\int_0^{t_j}\nabla f_{j,r}^\nu(X_i(r))\cdot dW_i(r),
 \qquad R_j=\sqrt{Nb}\int_0^{t_j}P_N[J_{f_{j,r}^\nu}](X(r))dr.
 \tag{6.3}
\]

At \(\nu=0\), the stochastic integral is exactly zero, not a limiting formal expression. At \(t_j=0\), both integrals vanish and the initial test is \(h_j\). The common finite horizon representation stops each martingale at its own \(t_j\). From (A), using Euclidean norm and the finite sum of coordinate bounds,

\[
 \sup_{\nu<\infty}\mathbb E|R_{N,\nu}|
 \le C\,N^{s/d-1/2},
 \qquad
 \mathbb E|R_{N,\nu}|\le C\sqrt b\,N^{s/d-1/2}.
 \tag{6.4}
\]

This tends to zero exactly in the additional range \(s<d/2\). No source square is used.

Let \(B^\nu_{ij}(u)\) be the deterministic function

\[
 B^\nu_{ij}(u)=2\nu b\int_0^{u\wedge t_i\wedge t_j}
                  \int\nabla f_{i,r}^\nu\cdot\nabla f_{j,r}^\nu\,dx\,dr.
\]

Independence of the driving Brownian motions, including all equal-label Itô contractions, gives the actual bracket

\[
 \langle M_i,M_j\rangle_u=2\nu b\int_0^{u\wedge t_i\wedge t_j}
                   \eta_N(r)[\nabla f_{i,r}^\nu\cdot\nabla f_{j,r}^\nu]dr.
 \tag{6.5}
\]

By (5.2) and \(0\le\nu b\le1\), the expectation of the total variation of the bracket difference is at most \(CN^{-q/2}\), uniformly in finite \(\nu\). This proves in particular the uniform terminal bracket fluctuation estimate, with no initial-vector independence premise.

More explicitly, fix \(\theta\in\mathbb R^m\) and
\(G_r^\nu=\sum_j\theta_j\mathbf1_{r<t_j}\nabla f_{j,r}^\nu\).
The indicator choice at finitely many endpoints is immaterial. For the scalar martingale \(M_\theta=\sum_j\theta_jM_j\), let
\(A_\theta=\langle M_\theta\rangle_T\) and
\(V_\theta=\theta^TB^\nu(T)\theta\). Then

\[
 A_\theta=2\nu b\int_0^T\eta_N[|G_r^\nu|^2]dr,
 \quad V_\theta=2\nu b\int_0^T\int|G_r^\nu|^2,
 \quad 0\le A_\theta,V_\theta\le K_\theta,
\]
\[
 \sup_{\nu<\infty}\mathbb E|A_\theta-V_\theta|
       \le C_\theta N^{-q/2}.
 \tag{6.6}
\]

The deterministic \(K_\theta\) follows directly from \(\nu b\le1\), fixed \(T\) and bounded gradients. This stronger pathwise bound will justify an exponential martingale exactly.

## 7. Uniform joint Gaussian approximation without finite-N independence

The initial vector is an iid triangular sum, with mean-zero summand
\(\zeta^\nu(x)=\sqrt b(f_{j,0}^\nu(x)-\int h_j)_{j=1}^m\).
Its sup norm is bounded by a constant depending only on the fixed list, uniformly over all finite \(\nu\). Let

\[
 I^\nu_{ij}=b\int (f_{i,0}^\nu-\int h_i)(f_{j,0}^\nu-\int h_j).
\]

For fixed \(\theta\), Taylor's integral remainder for \(e^{ix}\) gives
\(\mathbb E e^{i\theta\cdot\zeta/\sqrt N}
=1-\theta^TI^\nu\theta/(2N)+O_\theta(N^{-3/2})\), uniformly in \(\nu\).
Comparing this to \(e^{-\theta^TI^\nu\theta/(2N)}\), then using
\(|u^N-v^N|\le N|u-v|\) when \(|u|,|v|\le1\), proves

\[
 \sup_{\nu<\infty}|\mathbb E e^{i\theta\cdot U}
                    -e^{-\theta^TI^\nu\theta/2}|\le C_\theta N^{-1/2}.
 \tag{7.1}
\]

There is no nondegeneracy requirement, limiting diffusivity or division by an initial variance.

To handle dependence, let \(\mathcal F_0\) include the initial vector and put
\(F_0=e^{i\theta\cdot U}\). Smooth Itô gives
\(\mathcal E_u=\exp(iM_\theta(u)+\langle M_\theta\rangle_u/2)\)
as a complex local martingale starting from one: the two finite-variation terms cancel. By (6.6), \(|\mathcal E_u|\le e^{K_\theta/2}\); localization and bounded convergence therefore make it a true martingale. In particular
\(\mathbb E(\mathcal E_T\mid\mathcal F_0)=1\), since the Brownian drivers are independent of the initial data and the stochastic integrals are martingales in this enlarged filtration. Hence

\[
 \mathbb E(F_0e^{iM_\theta+A_\theta/2})=\mathbb EF_0.
\]

Since \(V_\theta\) is deterministic, subtracting the preceding identity multiplied by \(e^{-V_\theta/2}\) gives

\[
 \left|\mathbb E e^{i\theta\cdot(U+M)}
       -e^{-V_\theta/2}\mathbb E e^{i\theta\cdot U}\right|
 \le\tfrac12e^{K_\theta/2}\mathbb E|A_\theta-V_\theta|
 \le C_\theta N^{-q/2}.
 \tag{7.2}
\]

The estimate uses \(|1-e^{(A_\theta-V_\theta)/2}|\le\tfrac12e^{K_\theta/2}|A_\theta-V_\theta|\). It does not claim finite-N independence; it controls precisely its effect on the joint characteristic function. Let \(W=U+M\) and \(C^\nu=I^\nu+B^\nu(T)\). Equations (7.1)–(7.2) prove the explicit uniform bound

\[
 \sup_{\nu<\infty}|\mathbb E e^{i\theta\cdot W}
                      -e^{-\theta^TC^\nu\theta/2}|
 \le C_\theta(N^{-1/2}+N^{-q/2}).
 \tag{7.3}
\]

Both matrices defining \(C^\nu\) are real positive semidefinite Gram matrices, so a centered possibly degenerate Gaussian always exists. Its characteristic function is the displayed one.

We next prove the entire bounded-Lipschitz supremum directly. This avoids replacing it by convergence for a fixed test or by a subsequence argument. Exact one-body Haar centering gives \(\mathbb E\langle M_i,M_j\rangle_T=B^\nu_{ij}(T)\). Conditional martingale mean zero gives \(\mathbb E U_iM_j=0\). Consequently
\(\mathbb E|W|^2=\operatorname{tr}C^\nu\le K\), uniformly; the bound also follows directly from fixed test norms. Let \(Y^\nu\) be the centered Gaussian with this covariance, and let \(G\) be an independent standard Gaussian in \(\mathbb R^m\). For \(\delta>0\), convolution gives continuous densities of \(W+\delta G\) and \(Y^\nu+\delta G\). Fourier inversion for the Gaussian, justified by integrability and Fubini, bounds their uniform density difference by

\[
 D_{N,\delta}:=(2\pi)^{-m}\int_{\mathbb R^m}
 e^{-\delta^2|\theta|^2/2}\min\{2,C_\theta(N^{-1/2}+N^{-q/2})\}\,d\theta.
 \tag{7.4}
\]

The constants in the preceding elementary bounds may be chosen as continuous functions of \(|\theta|\), built from fixed test seminorms and \(e^{K|\theta|^2}\). Thus the majorant is measurable. It tends pointwise to zero and is bounded by twice an integrable Gaussian. Dominated convergence proves \(D_{N,\delta}\to0\) for each fixed \(\delta\), uniformly in the diffusivity through its definition. No covariance determinant is inverted.

For every real \(F\) with \(\|F\|_\infty\le1\) and Lipschitz constant at most one, smoothing changes either expectation by at most \(\delta\mathbb E|G|\). On a ball of radius \(R\), the smoothed difference is at most its volume times \(D_{N,\delta}\). Outside, Markov's inequality and the uniform second moments give the sum of tails at most \(2(K+m\delta^2)/R^2\). Therefore, uniformly in \(\nu\) and all such \(F\),

\[
 |\mathbb EF(W)-\mathbb EF(Y^\nu)|
 \le2\delta\mathbb E|G|+|B_R|D_{N,\delta}
                  +2(K+m\delta^2)/R^2.
 \tag{7.5}
\]

Take \(N\to\infty\) first, \(R\to\infty\) next, and \(\delta\downarrow0\) last. The right side is independent of \(F\) and \(\nu\), proving their joint supremum tends to zero. Finally \(|\mathbb EF(Z)-\mathbb EF(W)|\le\mathbb E|R_{N,\nu}|\), so (6.4) proves precisely Part B's full uniform metric assertion for \(s<d/2\). This step needs no second moment of the nonlinear residual.

## 8. Exact covariance and every sequence/degenerate consequence

Parseval gives

\[
 I^\nu_{ij}=b\sum_{k\ne0}\widehat h_i(k)\overline{\widehat h_j(k)}
                  e^{-(t_i+t_j)L_k},
\]
\[
 B^\nu_{ij}(T)=2\nu b\sum_{k\ne0}a_k\widehat h_i(k)\overline{\widehat h_j(k)}
          \int_0^{t_i\wedge t_j}e^{-(t_i+t_j-2r)L_k}\,dr.
\]

All series and integrals are absolutely dominated by smooth Fourier seminorms; at each finite \(\nu\) this justifies the interchange. Since \(L_k>0\), the integral equals
\([e^{-|t_i-t_j|L_k}-e^{-(t_i+t_j)L_k}]/(2L_k)\), also when a time is zero. Adding and using \(1-\nu a_k/L_k=D_k/L_k\) gives exactly

\[
 C^\nu_{ij}=b\sum_{k\ne0}\widehat h_i(k)\overline{\widehat h_j(k)}
 \left[\frac{D_k}{L_k}e^{-(t_i+t_j)L_k}
       +\frac{\nu a_k}{L_k}e^{-|t_i-t_j|L_k}\right].
 \tag{8.1}
\]

For real tests the paired \(k,-k\) terms make this real symmetric. Its Gram derivation proves positivity even when individual cross-mode products have signs. The bracket coefficient is exactly \(2\nu b\), and the initial coefficient is exactly \(b\).

If \(\nu_N\to\bar\nu<\infty\), then \(b\) is continuous including at zero and one, and each summand in (8.1) is continuous. The weights in brackets are bounded in absolute value by one, so the summable majorant \(|\widehat h_i(k)\widehat h_j(k)|\) gives entrywise \(C^{\nu_N}\to C^{\bar\nu}\). For a direct law passage, the unique positive semidefinite square roots converge: every subsequence has a bounded subsubsequence converging to a positive semidefinite matrix \(S\) with \(S^2=C^{\bar\nu}\); diagonalization of the latter and nonnegativity identify \(S\) uniquely as its nonnegative square root. This proves convergence of the whole root sequence. Coupling the Gaussians by \((C^{\nu_N})^{1/2}G\) proves convergence in mean norm and hence in bounded-Lipschitz distance, without nonsingularity. Part B then gives the announced finite-limit law.

For large noise there is a stronger direct estimate. On the diagonal of (8.1), the bracketed weight is at most \(D_k/L_k+\nu a_k/L_k=1\). Thus

\[
 \mathbb E|W|^2=\operatorname{tr}C^\nu
       \le b\sum_j\|h_j-\textstyle\int h_j\|_2^2.
 \tag{8.2}
\]

Combining (8.2) with the second bound in (6.4) and \(s/d-1/2<0\) gives

\[
 \sup_{N\ge2}\mathbb E|Z_{N,\nu}|\le C\sqrt{b(\nu)}.
 \tag{8.3}
\]

Consequently every sequence of finite \(\nu_N\to\infty\) has \(Z_{N,\nu_N}\to0\) in probability by Markov, with no restriction on how fast \(\nu_N\) grows. Infinity was never used as a drift/noise coefficient. The covariance also tends to zero by (8.2).

For an arbitrary deterministic sequence of finite \(\nu_N\), convergent or not, substituting it into the proved supremum already gives the stated Gaussian approximation; neither an extraction nor a limiting covariance is required. At \(\nu=0\), (8.1) reduces to the initial Gaussian propagated by \(e^{-tD_k}\), with exactly zero martingale. Constant tests have identically zero centered coordinates, gradients and sources. If a time is zero, its martingale and source vanish and (8.1) gives its correct cross covariance with every later coordinate. Repeated times require no ordering assumption: the common interval is \(t_i\wedge t_j\), and \(e^{-|t_i-t_j|L_k}=1\) when equal. Repeated/linearly dependent tests can force singular covariance; every characteristic, smoothing and square-root argument above permits it. If \(T=0\), all coordinates are the initial iid vector, and the same proof applies with both integral terms zero. Arbitrary fixed smooth tuples, not only Fourier polynomials, were retained throughout via their finite Fourier seminorms.

## 9. Independent falsification route and exact diagnostic

A separate falsification route probes the exact initial particle generator and the target covariance rather than the heat commutator. For a nonzero mode \(k\), let \(Y_k=N^{-1}\sum_i e^{-2\pi i k\cdot X_i}\). The full empirical square has N constant self terms. For each ordered distinct pair, the two internal force derivatives contribute total coefficient \(2/N\); every third-label force integrates to zero at initial Haar. Distributional integration by parts uses the full \(D\), hence

\[
 \mathbb E|Y_k(0)|^2=N^{-1},\qquad
 \left.\frac d{dt}\mathbb E|Y_k(t)|^2\right|_{t=0}
   =-2(N-1)D_k/N^2.
 \tag{9.1}
\]

For rigor of this actual singular derivative, the smooth observable's generator is Haar \(L^1\) since \(K\in L^1\). The fixed-N density bound (3.6) makes its occupation integrable on a short interval. Approximate it in Haar \(L^1\) by continuous functions, use (3.6) for uniform approximation error and path continuity for convergence at time zero, then the stopped Itô expectation identity. This proves the derivative without a singular Taylor remainder. At Coulomb it includes the divergence atom; using only its punctured value would give the wrong sign/coefficient.

After multiplying (9.1) by \(Nb\), the derivative is \(-2b(1-1/N)D_k\), whereas (8.1)'s equal-time single-mode covariance derivative at zero is \(-2bD_k\), independent of finite \(\nu\). The finite-N discrepancy is exactly \(2bD_k/N\), uniformly small. Thus a proposed immediate high-noise variance growth contradicts the exact admitted initial generator. This test does not assert later-time monotonicity or a uniform singular Taylor expansion.

The fresh standard-library diagnostic in the artifact directory uses only exact rational arithmetic. It independently expands the literal finite-particle Fourier generator, retains all labels and diffusion terms, and checks (9.1) over multiple N, modes and noise values. It also constructs the scalar/vector covariance on integer time grids twice: from independent initial and increment Gram terms and from (8.1). Integer rates and rational attenuation bases make every coefficient exact. Cases include zero noise, noise above one, time zero, repeated times, signed cross-mode amplitudes and identically zero tests. It tests positive semidefiniteness by the explicit Gram decomposition and selected exact quadratic forms, not by floating-point eigenvalues.

A separate solvable martingale test starts with an initial sign U and an independent standard normal increment B, and uses M=a(U)B with a(-1)=1 and a(1)=2. Then E(M|U)=0 and E(UM)=0, but E(UM^2)=3/2. It rejects the false inference from zero initial/martingale covariance to independence. This toy is labeled a logical mutation control, not a particle counterexample. The proof in §7 handles the dependence by the conditional compensated identity instead.

Deliberately wrong source-deletion denominator, interaction coefficient, missing factor two in the Brownian covariance, missing b normalization, omitted initial contribution, wrong cross-time absolute difference and the independence inference are each required to fail an exact control. Finite diagnostics cannot establish analytic uniformity, singular passages or the full metric limit; those are proved in §§3–8.

## 10. Dispositions, hostile self-check and sealed handoff

| Item | Disposition and exact boundary |
|---|---|
| Part A, all finite diffusivities and zero-noise actual flow | RECONSTRUCTED from full allowed proofs with all source constants checked; no upper-noise restriction retained. |
| Actual law, heat passage, source integrability and original singular first-order identity | Reconstructed in §§3,4,6; heat passage is fixed parameter before any uniform inequalities, and no singular diagonal is assigned. |
| Exact Haar marginal and centering | PROVED HERE by equivariance and uniqueness; higher-marginal independence is not claimed. |
| Uniform full fixed-list Gaussian approximation | RECONSTRUCTED in §§5–8; explicit uniform characteristic control, conditional initial-field treatment and direct full BL supremum passage. |
| All sequence, finite-limit, divergent-noise, degenerate, constant and repeated-time cases | Covered explicitly in §8, including direct uniform-in-N high-noise first-moment bound. |
| Exact negation of entire THM041 | No admitted counterexample; excluded by the complete reconstruction subject to separate proof/source review. |
| R16, THM038 and earlier issued source/audit histories | Unchanged. The full needed mechanisms are checked here; this report does not retroactively certify those documents. |
| Path-space limits, growing lists, s>=d/2 fluctuation law, general backgrounds or preparations, higher hierarchy, flagship resolution | NOT CLAIMED. |

The strongest claims received the following local hostile checks. A finite-N noise bound growing with diffusivity is confined to constructing each actual law; the estimate used for uniformity is the zero energy upper bound, not that growing construction bound. No uniform time derivative is smuggled into the source argument. Every bracket uses actual-law absolute concentration, not merely exact centering. A full martingale bounded-bracket argument replaces an independence assumption. Gaussian convolution proves the test-function supremum without an invertible covariance or parameter subsequence. The high-noise claim follows directly from (8.3), so no unexplained competition between N and diffusivity survives. Residuals are controlled only in L1, which is sufficient for bounded Lipschitz tests; no unjustified L2 residual is used. This is the reconstruction's own adversarial self-check, not the separately required isolated hostile review.

The artifact README and source/exposure record give the exact verification command, output counts, mutation outcomes, input/output manifests, safe archive membership and archive digest. The report and artifacts are sealed read-only after verification. Corrections must be separately issued; the sealed bytes must not be edited. Root alone may compare this result to the constructor, conduct the separate hostile/source gates and integrate canonical records. No canonical record is changed and no commit is made. The bounded task ends at this complete sealed handoff.
