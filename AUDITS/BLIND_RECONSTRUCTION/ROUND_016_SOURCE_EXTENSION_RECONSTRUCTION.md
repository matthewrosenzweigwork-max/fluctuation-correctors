# AUD051 — blind whole-claim reconstruction of THM038

TASK080. Issued 2026-09-18 UTC. **RECONSTRUCTED IN FULL; SAME-CONTEXT DIAGNOSTICS PASSED; SEALED BEFORE COMPARISON.** This is an isolated reconstruction, not a claim that its author has independently certified this new proof. Root comparison, hostile review, and campaign promotion remain separate gates.

The frozen assertion is proved below throughout its stated range, including zero noise, arbitrary fixed smooth tests, and the Coulomb endpoint. The proof bounds the genuine deleted source in actual-law L1. It does not infer concentration from an expectation alone: a positive short-scale pair bound and a deterministic absolute commutator inequality provide the needed bridge. No pair inverse, cubic domain, bracket limit, hierarchy closure, or fluctuation theorem is used or certified.

## 1. Frozen assertion, exact negation, and exposure boundary

Fix an integer \(d\ge3\), \(0<s\le d-2\), \(0\le T<\infty\), \(0\le\nu_*<\infty\), and a fixed real \(h\in C^\infty(\mathbb T^d)\). Haar mass is one, and \(e_k(x)=e^{2\pi i k\cdot x}\). The interaction is exactly

\[
 \widehat g(0)=0,\qquad \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1}
\]

For every integer \(N\ge2\) and every \(0\le\nu\le\nu_*\), the actual singular process starts from iid Haar, independently of its independent standard Brownian drivers, and solves

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu}\,dW_i.
 \tag{2}
\]

Let

\[
 f_t^\nu=\widehat h(0)+\sum_{m\ne0}\widehat h(m)
 e^{-(T-t)(4\pi^2\nu|m|^2+4\pi^2c_{d,s}|m|^{s+2-d})}e_m,
 \qquad J_f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y)).
 \tag{3}
\]

No value is assigned to this singular kernel at \(x=y\). For its integrable contractions, use precisely

\[
 P_N[J_f]=\frac1{2N^2}\sum_{i\ne j}J_f(X_i,X_j)
 -\frac1N\sum_i\int J_f(X_i,y)\,dy
 +\frac12\iint J_f(x,y)\,dx\,dy.
 \tag{4}
\]

The assertion is genuine integrability and

\[
 \sup_{0\le t\le T}\mathbb E|P_N[J_{f_t^\nu}]|
 \le C N^{s/d-1},
 \tag{5}
\]

where C depends only on the fixed data in the card and is independent of N, chosen diffusivity, and deterministic time. Its exact negation is one admitted fixed datum for which integrability fails, or the supremum of the left side divided by the displayed power over admitted N, diffusivities, and times is infinite. A generic exchangeable law is not the actual-law negation. Failure of an attempted estimate is not that negation either.

For \(b=\min(1/\nu,1)\) at positive noise and \(b=1\) at zero noise, \(\sigma=\sqrt{Nb}\), the quantitative consequence is

\[
 \sigma\mathbb E\int_0^T|P_N[J_{f_t^\nu}]|\,dt
 \le C\sqrt b\,N^{s/d-1/2}.
 \tag{6}
\]

This yields uniform scaled smallness when \(s<d/2\); at equality it is only a bounded estimate, and above equality it asserts no decay. Neither failure of decay nor a limiting law is inferred at those excluded decay endpoints.

The task and input manifest were read first. The worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r016-source-blind`, branch `codex/hocf-r016-source-blind`, created from published R13 `072cab684b9ce41855ead6c48f435c8fc184ec35`. Exactly the nine prescribed inputs were overlaid and SHA-256 checked. No current construction, R11–R16 proof/audit result, state/history file, root scratch, memory file, prior checker, or external source was opened. The initial Git check revealed only the root path and a count of 56 preexisting status entries. Worktree creation printed the base commit title. Automatically supplied ambient instructions included a high-level memory summary and campaign mission; they supplied no proof of this claim and were not used as mathematical inputs. The full exposure record is in the packet. No candidate comparison has occurred.

## 2. Source preflight and independently rechecked ingredients

| Frozen input | Use and disposition |
|---|---|
| `AGENTS.md`, TASK080, frozen model | Scope, isolation, coefficient-one normalization, actual law, ordered labels, and report contract. The bounded isolation rule excludes reading general ledgers and older non-allowlisted files. |
| `ROUND_001_ALGEBRA.md`, Sections 1–4 | Source convention and the one-body linear response. All source/background coefficients actually used here are rederived in Section 5. Pair-generator and martingale conclusions are not needed. |
| `ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–3 and heat facts in Section 5 | Heat normalization, local singularity, finite divergence measure, Coulomb atom and compensation. The necessary derivation is reproduced below; its status label is not an input. |
| THM026 and `ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, Sections 2–8 | Collision-free actual process and same-noise heat approximation. Their necessary finite-N argument is reconstructed in Section 3. No corrector domain or N-uniform density estimate is imported. |
| `ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, Sections 2–3 | Actual expected energy and heat floor. These supplied conditional arguments are rechecked in Sections 3–4. Its other, unavailable pair-domain and earlier audit premises are not imported. |
| THM038 | Entire frozen assertion and exact negation, without repairing or narrowing its range. |

Set

\[
 \alpha=(d-s)/2\ge1,\qquad A=4^\alpha\pi^{d/2}/\Gamma(s/2),
 \quad q_u(z)=(4\pi u)^{-d/2}e^{-|z|^2/(4u)},
 \quad p_u(z)=\sum_{n\in\mathbb Z^d}q_u(z+n).
 \tag{7}
\]

Unfolding the Gaussian shows that p is positive, has mass one, and has Fourier coefficients \(e^{-4\pi^2u|k|^2}\). Its nonconstant modes and every derivative decay exponentially for \(u\ge1\). Its L1 norm is one, so

\[
 g(z)=A\int_0^\infty u^{\alpha-1}(p_u(z)-1)\,du
 \tag{8}
\]

converges in L1. Taking a nonzero Fourier coefficient yields
\(A\Gamma(\alpha)/(4\pi^2|k|^2)^\alpha=c_{d,s}|k|^{s-d}\), exactly (1). Substitution \(v=|z|^2/(4u)\) in the Euclidean Gaussian integral gives coefficient one times \(|z|^{-s}\). Subtracting that term on a small ball leaves a smooth remainder: all nonzero lattice translates have exponentially small short-time derivatives, the constant integrates at zero because \(\alpha>0\), and the large-time Euclidean integrand is bounded by a multiple of \(u^{-s/2-1}\). Thus g is smooth off zero,

\[
 g(z)=|z|^{-s}+H_s(z)\quad\hbox{locally},\qquad
 H_s\in C^\infty,\quad g\in L^1,\quad K\in L^1,\quad
 g_*:=\inf_{z\ne0}g(z)>-\infty.
 \tag{9}
\]

In fact \(g_*<0\) because the mean is zero and the positive singularity is nonconstant. Gradient integrability follows from \(s+1<d\).

Write \(D=\operatorname{div}K=-\Delta g\) in distributions. Punctured integration by parts produces the inner-boundary flux
\(s r^{d-s-2}\int_{\mathbb S^{d-1}}\psi(r\theta)\,dS\). It vanishes below Coulomb and equals \((d-2)|\mathbb S^{d-1}|\psi(0)\) at Coulomb. Fourier coefficients and the gamma recurrence then give exactly

\[
 D=\begin{cases}
 s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \quad c_d=(d-2)|\mathbb S^{d-1}|=4\pi^2c_{d,d-2}.
 \tag{10}
\]

Below Coulomb the singular density has exponent \(s+2<d\); at Coulomb the atom and compensating Haar measure are both present. Equality of the distributions follows from equality of all Fourier coefficients, which can be checked by heat convolution and passage against smooth tests. In both cases D is finite and \(D\ge-\kappa\,dz\) for some finite kernel-dependent \(\kappa\ge0\). The convolution regularization satisfies

\[
 g_\varepsilon=p_\varepsilon*g,\quad K_\varepsilon=p_\varepsilon*K,
 \quad D_\varepsilon=p_\varepsilon*D\ge-\kappa.
 \tag{11}
\]

At Coulomb, \(D_\varepsilon=c_d(p_\varepsilon-1)\), not the constant \(-c_d\). The latter is only the restriction of D to the punctured torus; it cannot replace (10) or (11) in a limiting identity.

No literature or novelty claim is used. The remaining tools are finite sums, Gaussian integration, smooth finite-dimensional SDE/ODE construction and localized Itô calculus, smooth periodic diffusion, and explicitly indicated convergence theorems.

## 3. Actual particles and the nonpositive expected energy

The following reconstruction records the finite-N input needed to apply the new estimate to the actual law. Define on collision-free configurations

\[
 H_N=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
 \mathcal E_N=H_N-\frac{N-1}{2}g_*
 =\frac1N\sum_{i<j}(g(x_i-x_j)-g_*)\ge0.
 \tag{12}
\]

Every partial or simultaneous collision makes at least one nonnegative summand diverge. Hence every finite sublevel of \(\mathcal E_N\) is compact inside the collision-free set. Differentiating the unordered pairs in both particle coordinates gives

\[
 B=-\nabla H_N,\quad B_i=\frac1N\sum_{j\ne i}K_{ij},\qquad
 \Delta_{Nd}H_N=\frac2N\sum_{i<j}\Delta g(x_i-x_j)
 \le (N-1)\kappa=:C_N.
 \tag{13}
\]

The punctured restriction in the last inequality is legitimate on a stopped collision-free compact set. At Coulomb its value is exactly \((N-1)c_d\); this statement does not remove the distributional atom from (10). The full drift square in the energy identity is
\(N^{-2}\sum_i\sum_{j,k\ne i}K_{ij}\cdot K_{ik}\). Both \(j=k\) and all three-label terms remain; no positivity of the latter is assumed.

Smooth cutoffs that agree with K outside progressively smaller collision neighborhoods have globally Lipschitz drifts. Picard iteration applied after subtracting the continuous Brownian driving path constructs their unique nonanticipating solutions. They agree until the corresponding collision-neighborhood exits and therefore patch to a maximal solution. The constructions and exit times are jointly Borel in initial state and driving path. A finite lifetime can only approach the collision set, since a path remaining in a collision-free compact set has a limit and can be continued.

Stop at the first energy level R, with an immediate stop when the initial energy already exceeds R. Smooth Itô calculus gives

\[
 \begin{split}
 \mathcal E_N(X_{t\wedge\tau_R})
 +\int_0^{t\wedge\tau_R}|B|^2\,du
 +\nu\int_0^{t\wedge\tau_R}(C_N-\Delta H_N)\,du
 =\mathcal E_N(X_0)+\nu C_N(t\wedge\tau_R)+M_R(t),\\
 \langle M_R\rangle_t=2\nu\int_0^{t\wedge\tau_R}|B|^2\,du.
 \end{split}
 \tag{14}
\]

The integrands are bounded on the stopped sublevel, so this is a true square-integrable stopped martingale. Its expectation is zero. Consequently, for each fixed collision-free start,
\(\mathbb P(\tau_R\le T)\le[\mathcal E_N(X_0)+\nu C_NT]/R\). Letting R increase proves nonexplosion and noncollision on each finite horizon. Local uniqueness proves global pathwise uniqueness. A continuous global path has a positive minimum pair distance on every compact time interval. Integrating the Borel construction over the independent iid-Haar initial state is legitimate; that state is collision-free almost surely and

\[
 \mathbb E\mathcal E_N(X_0)=-(N-1)g_*/2<\infty.
 \tag{15}
\]

At zero noise, (14) is the deterministic decrease of H. This construction thus supplies exactly the actual deterministic flow required by the card.

For heat-regularized forces, \(K_\varepsilon\to K\) in C1 on every compact subset away from zero. Split K into a smooth local extension there and an L1 term supported a positive distance away; Gaussian derivative bounds make the latter convolution exponentially small. On a fixed noncollision path choose a separation margin smaller than its minimum separation. Couple all heat solutions with the same initial state and Brownian paths. The Brownian terms cancel in the difference equation. Before a difference exit from that margin, the drifts have a common local Lipschitz constant and their uniform discrepancy tends to zero. Gronwall prevents the exit for all sufficiently small epsilon and yields

\[
 \sup_{0\le t\le T}|X_t^\varepsilon-X_t|\longrightarrow0
 \quad\hbox{almost surely at each fixed }N,\nu,T.
 \tag{16}
\]

The local constants can depend on the path and on the fixed finite data. No N-uniform path-passage rate is used.

At fixed \(\varepsilon>0\), the smooth drift is \(-\nabla H_N^\varepsilon\). For \(\nu>0\), its smooth positive density \(F_t^\varepsilon\), initially one, solves the smooth periodic Fokker–Planck equation. Existence and the differentiations can be obtained from the heat integral equation on the compact configuration torus; positive upper and lower finite-time bounds follow from the maximum principle. Differentiation and periodic integration by parts give

\[
 \frac d{dt}\left[\nu\int F_t^\varepsilon\log F_t^\varepsilon
 +\int H_N^\varepsilon F_t^\varepsilon\right]
 =-\int F_t^\varepsilon
 |\nabla H_N^\varepsilon+\nu\nabla\log F_t^\varepsilon|^2\le0.
 \tag{17}
\]

The initial entropy and energy are zero. Entropy relative to unit Haar is nonnegative by convexity. Thus \(\mathbb EH_N^\varepsilon(X_t^\varepsilon)\le0\). The exact smooth divergence used here, if density bounds are desired, is
\(\operatorname{div}_{Nd}B^\varepsilon=(2/N)\sum_{i<j}D_\varepsilon(x_i-x_j)\ge-(N-1)\kappa\); no endpoint atom has been discarded. That bound yields only an N-dependent density bound and is not a uniform-law input.

By (16) and local convergence of g, the regularized energies converge almost surely at every fixed time. Positivity of heat convolution gives the common lower bound \(H_N^\varepsilon\ge(N-1)g_*/2\). Fatou applied after subtracting that bound proves

\[
 \boxed{\mathbb EH_N(X_t)\le0,\qquad 0\le t\le T.}
 \tag{18}
\]

The lower bound and (18) give genuine integrability. At zero noise use deterministic energy decrease and the iid initial mean zero, so no division by diffusivity occurs. There is no passage of a singular Fisher-information identity. In particular no finite derivative of the singular expected energy at time zero is asserted.

Permutation equivariance of the construction gives exchangeability. Common translations preserve (2) and the initial law, so the one-particle marginal is Haar; positive-time independence is not claimed. Since every shifted pair energy in (12) is nonnegative, (18) and exchangeability give

\[
 \mathbb E g(X_1-X_2)\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|,
 \quad
 \mathbb E\big[1+\operatorname{dist}(X_1,X_2)^{-s}\big]\le C.
 \tag{19}
\]

The last assertion follows from the local expansion and boundedness away from zero. The constants are independent of N, deterministic time, and admitted diffusivity. This is a pair-energy moment, not a squared-force estimate.

## 4. One positive identity controls microscopic pairs and smoothed energy

For \(0<R\le2\), define

\[
 Q_R(z)=A\int_0^R u^{\alpha-1}p_u(z)\,du\ge0,
 \quad G_R(z)=A\int_R^\infty u^{\alpha-1}(p_u(z)-1)\,du,
 \quad a_R(k)=A\int_R^\infty u^{\alpha-1}e^{-4\pi^2|k|^2u}\,du>0
 \tag{20}
\]

for nonzero k, with \(a_R(0)=0\). G is smooth. Q is evaluated only at off-diagonal particle pairs; its positive heat representation is used for Haar integrals, without assigning a source trace. The exact off-zero decomposition is \(g=Q_R-AR^\alpha/\alpha+G_R\). Put

\[
 z_k=\langle\eta_N-dx,e_k\rangle,\quad z_0=0,\qquad
 E_R=\sum_{k\ne0}a_R(k)|z_k|^2,\qquad
 L_R=\frac1{N^2}\sum_{i\ne j}Q_R(X_i-X_j).
 \tag{21}
\]

Both are nonnegative. The Fourier series of G is absolutely convergent. In particular the exact smooth self contribution in the pair sum is \(G_R(0)/N\), and direct substitution gives

\[
 \boxed{\frac{2H_N}{N}
 =L_R+E_R-\frac{A(N-1)}{N\alpha}R^\alpha-\frac{G_R(0)}N.}
 \tag{22}
\]

The coefficient \((N-1)/N\), the ordered-pair denominator, and the full smooth self subtraction are retained. No singular diagonal of g or J appears. Gaussian lattice bounds give \(0\le G_R(0)\le C R^{-s/2}\) for \(0<R\le2\): on \((0,1]\), \(p_u(0)\le C u^{-d/2}\), so the integrand is bounded by \(C u^{-s/2-1}\); the rest decays exponentially. The lattice bound follows by separating finitely many near lattice points and summing the Gaussian tails. For R between one and two a larger fixed constant suffices.

At fixed R, E is bounded. Equations (18) and (22) first prove integrability of the positive L, and then yield

\[
 \boxed{\mathbb E L_R+\mathbb E E_R
 \le C\big(R^\alpha+N^{-1}R^{-s/2}\big).}
 \tag{23}
\]

This is the actual-law input to both estimates below. The deterministic floor \(H_N\ge-CN^{s/d}\) follows from (22) with \(R=N^{-2/d}\), but the proof uses the stronger joint positive identity (23). No temperature scaling or prior energy-floor closure is assumed.

## 5. Exact source contractions and one Fourier mode

The local estimate

\[
 |J_f(x,y)|\le C\|f\|_{C^2}
 (1+\operatorname{dist}(x,y)^{-s})
 \tag{24}
\]

follows by combining the first-order difference of the gradients with \(|K(z)|\le C|z|^{-s-1}\) locally, and boundedness elsewhere. Equations (19) and (24) already prove genuine source and contraction integrability.

Distributional integration by parts, justified by \(K\in L^1\), gives all original Haar contractions:

\[
 \int J_f(x,y)\,dy=-D*f(x),\qquad \iint J_f=0.
 \tag{25}
\]

The first term of J integrates to zero since \(\int K=0\); its second term is \(-K*\nabla f=-D*f\). In particular, for \(f=e_m\), \(m\ne0\), set \(d_m=4\pi^2c_{d,s}|m|^{s+2-d}\). Then

\[
 \int J_m(x,y)\,dy=-d_m e_m(x),\qquad
 P_N[J_m]=\frac1{2N^2}\sum_{i\ne j}J_m(X_i,X_j)
 +\frac{d_m}{N}\sum_i e_m(X_i).
 \tag{26}
\]

At Coulomb, \(D*f=c_d(f-\int f)\). Thus (25) contains both the atom and compensation; for every nonzero mode it is \(-c_d e_m\). Using only the punctured density \(-c_d\) would erase this nonconstant contraction and gives the wrong source. The constant test has source identically zero.

Fix one nonzero mode and choose, solely inside the estimate,

\[
 R=R_{N,m}:=N^{-2/d}|m|^{-2},\qquad R|m|^2\le1.
 \tag{27}
\]

This is a heat-integral split of the exact singular source, not a different particle dynamics or a changing terminal test. Write \(J_m=J_m^{<R}+J_m^{>R}\) using the gradients of the short and long parts of (20). All three terms of (4) split linearly.

### 5.1. The genuine short part

For every lifted difference \(w=x-y+n\), periodicity gives
\(|\nabla e_m(x)-\nabla e_m(y)|\le(2\pi)^2|m|^2|w|\). Thus

\[
 |\nabla p_u(x-y)\cdot(\nabla e_m(x)-\nabla e_m(y))|
 \le C_d|m|^2 p_{2u}(x-y).
 \tag{28}
\]

Indeed \((|w|^2/(2u))q_u(w)/q_{2u}(w)
=2^{d/2}(|w|^2/(2u))e^{-|w|^2/(8u)}\) is bounded, and one sums over lifts. The derivative heat integral converges in L1 because \(\int_0^R u^{\alpha-3/2}\,du<\infty\); it also converges locally pointwise off zero. Hence no singular derivative interchange is left implicit. Substitution in the heat integral gives

\[
 |J_m^{<R}(x,y)|\le C|m|^2 Q_{2R}(x-y).
 \tag{29}
\]

The empirical part of (4) is bounded by \(C|m|^2L_{2R}\). Its mixed and background contractions are bounded by \(C|m|^2R^\alpha\), since \(\int Q_{2R}=A(2R)^\alpha/\alpha\) independently of the unintegrated variable. Therefore (23), including its applicability up to \(2R\le2\), gives

\[
 \mathbb E|P_N[J_m^{<R}]|
 \le C|m|^2(R^\alpha+N^{-1}R^{-s/2})
 \le C N^{s/d-1}|m|^{s+2}.
 \tag{30}
\]

This estimate uses a positive majorant only for the short part; it makes no claim that the weighted source kernel is positive semidefinite.

### 5.2. The smooth long part and its full contraction

For G_R, the kernel \(J_m^{>R}\) is smooth and vanishes on its diagonal. Thus its literal statistic (4) equals one half its full \((\eta_N-dx)^{\otimes2}\) pairing. Expanding both terms of the gradient difference, with the physical \(2\pi\) factors retained, gives exactly

\[
 P_N[J_m^{>R}]
 =-2\pi^2\sum_{k\in\mathbb Z^d\setminus\{0,m\}}
 m\cdot\big[k a_R(k)+(m-k)a_R(m-k)\big]z_k z_{m-k}.
 \tag{31}
\]

Terms k=0 and k=m vanish because \(z_0=0\), which is exactly the Haar-contraction cancellation. The deleted-to-full conversion here uses only the smooth zero source diagonal, while the separate energy comparison (22) retains its nonzero smooth energy self subtraction.

We prove the following uniform symbol bound whenever \(R|m|^2\le1\):

\[
 \left|m\cdot\big[k a_R(k)+(m-k)a_R(m-k)\big]\right|
 \le C|m|^{2\alpha+2}
 \sqrt{a_{R/64}(k)a_{R/64}(m-k)}
 \quad(k\ne0,m).
 \tag{32}
\]

The wider heat range on the right is deliberate. It avoids any false bounded shift-ratio assertion for a fixed Gaussian cutoff at arbitrarily high frequencies.

Here is the full proof. Write \(q=4\pi^2\), and extend a to nonzero real vectors by its integral. Integrating on \([R+|\xi|^{-2},R+2|\xi|^{-2}]\), using \(\alpha\ge1\), gives

\[
 c|\xi|^{-2\alpha}e^{-qR|\xi|^2}
 \le a_R(\xi)\le C|\xi|^{-2\alpha}.
 \tag{33}
\]

If \(|k|\le2|m|\), then \(|m-k|\le3|m|\); both nonzero lattice lengths are at least one. Since \(1-2\alpha\le-1\), the numerator of (32) is at most \(C|m|\). By (33) and \(R|m|^2\le1\), its proposed denominator is at least \(c|m|^{-2\alpha}\). Their ratio is at most \(C|m|^{2\alpha+1}\), hence the displayed bound.

If \(|k|>2|m|\), the entire segment \(\xi=k-\theta m\), \(0\le\theta\le1\), has length between \(|k|/2\) and \(3|k|/2\). Differentiating the integral defining \(p_R(\xi)=\xi a_R(\xi)\) gives

\[
 \|Dp_R(\xi)\|
 \le A\int_R^\infty u^{\alpha-1}(1+2qu|\xi|^2)e^{-qu|\xi|^2}\,du
 \le C|k|^{-2\alpha}e^{-qR|k|^2/8}.
 \tag{34}
\]

For the last inequality, split the exponential in halves; one half is at most \(e^{-qR|k|^2/8}\). Bound the other using \(|\xi|\ge|k|/2\), bound the polynomial using \(|\xi|\le3|k|/2\), and extend its integral to zero. Substitution \(v=u|k|^2\) yields the claimed power and a finite gamma integral. The vector sum in (32) is \(p_R(k)-p_R(k-m)\), so the fundamental theorem of calculus bounds its numerator by
\(C|m|^2|k|^{-2\alpha}e^{-qR|k|^2/8}\). On the other hand (33) gives a lower bound for its denominator of
\(c|k|^{-2\alpha}e^{-13qR|k|^2/512}\), because \(|m-k|\le3|k|/2\). Since \(1/8>13/512\), their ratio is at most \(C|m|^2\). This proves (32) in both cases, including \(\alpha=1\). No segment through zero was differentiated.

Apply (32) in (31). Cauchy–Schwarz on the k sum, with the bijection \(k\mapsto m-k\), bounds that sum by E at scale R/64. Consequently

\[
 |P_N[J_m^{>R}]|\le C|m|^{2\alpha+2}E_{R/64},
 \qquad
 \mathbb E|P_N[J_m^{>R}]|
 \le C N^{s/d-1}|m|^{2\alpha+2+s}
 =C N^{s/d-1}|m|^{d+2}.
 \tag{35}
\]

All sums are absolutely convergent at each fixed R before the estimate, because G_R is smooth. No individual empirical Fourier mode is assumed independent of another. Combining (30) and (35), and using \(s+2\le d+2\), proves for every nonzero mode

\[
 \boxed{\mathbb E|P_N[J_m]|\le C N^{s/d-1}|m|^{d+2}.}
 \tag{36}
\]

The constant is independent of m, N, diffusivity, and deterministic time. The m-dependent splitting parameter disappears from the statement. This directly covers arbitrarily high terminal frequencies with polynomial cost, rather than restricting the card to Fourier polynomials.

## 6. Arbitrary smooth terminal tests, uniformity, and the scaled conclusion

Every multiplier in (3) has magnitude at most one. Smoothness on the torus implies

\[
 S_h:=\sum_{m\ne0}|m|^{d+2}|\widehat h(m)|<\infty.
 \tag{37}
\]

For example, repeated integration by parts gives a bound by a sufficiently high fixed derivative norm of h. Equation (24), (19), and \(\sum|m|^2|\widehat h(m)|<\infty\) justify termwise source expansion and both Haar contractions in actual-law L1, uniformly in deterministic t, N, and admitted diffusivity. Pointwise off the diagonal the same expansion follows from C2 convergence. There is no singular diagonal completion. Minkowski's inequality and (36) now yield

\[
 \mathbb E|P_N[J_{f_t^\nu}]|
 \le C S_h N^{s/d-1},
 \tag{38}
\]

which is precisely (5). The permitted constant can absorb T, the fixed kernel, and the other fixed data; no hidden N- or diffusivity-dependent norm of f is used. At \(\nu_*=0\) the same proof uses only the deterministic branch of Section 3. At T=0 the raw estimate remains valid and the time integral is zero.

The actual paths and f are jointly measurable in time, and the source is continuous along each collision-free path. Tonelli applies to the nonnegative absolute value; (38) bounds the time integral by \(CTN^{s/d-1}\). Multiplication by exactly \(\sqrt{Nb}\) proves (6). No limit in N or diffusivity was exchanged with the heat approximation: the latter was removed first at fixed finite data in (16)–(18). The subsequent heat-integral splits are exact representations of the already defined singular source. The infinite smooth-test sum is justified in L1 by the fixed summable seminorm (37).

When \(s=d/2\), the exponent in (6) is zero; since b may equal one, uniform scaled decay does not follow. Such equality is admitted beginning at d=4. For \(s>d/2\), allowed in parts of d at least five, the exponent is positive. The estimate makes no decay claim there. For fixed d and s in the card, the raw exponent \(s/d-1\) remains strictly negative throughout. No logarithmic limit, general background, d=1 or 2, or super-Coulomb statement is appended.

## 7. Independent falsification route and adversarial checks

The falsification route starts from the literal finite-label observable under the actual initial iid-Haar law, independently of the heat-energy proof. For any smooth symmetric J with total Haar integral zero, put \(q(x)=\int J(x,y)dy\) and \(J^0=J-q(x)-q(y)\). Literal counting gives

\[
 P_N[J]=\frac1{2N^2}\sum_{i\ne j}J^0(X_i,X_j)-\frac1{N^2}\sum_i q(X_i).
 \tag{39}
\]

The residual one-label term is retained even though the background is Haar. For a real smooth kernel, iid orthogonality gives

\[
 \mathbb EP_N[J]=0,\qquad
 \mathbb E|P_N[J]|^2
 =\frac{N-1}{2N^3}\|J^0\|_2^2+\frac1{N^3}\|q\|_2^2.
 \tag{40}
\]

There are exactly \(2N(N-1)\) ordered pair-pair matches; all single-overlap terms vanish by the centering of J0. Cross terms against the one-label sum also vanish. This directly tests N=2 and the sign and normalization of the original contractions. It is not applied to a singular J lacking L2 integrability. In particular (40) cannot be used to reject the card at \(2s\ge d\), where the present proof deliberately uses L1 short-scale control.

The independently written standard-library diagnostic expands Laurent polynomials over Gaussian rationals. It constructs the literal deleted statistic, separately constructs (31), checks all Haar contractions and the smooth zero diagonal, verifies (39)–(40), and checks the exact energy self subtraction. Its source is included; no earlier checker was read or imported. It includes high frequencies, constant and mixed tests, small particle numbers, rational scaling exponents, positive and zero noise, and the Coulomb atom/compensation functional. These are exact coefficient and implication checks, not numerical evidence substituted for the infinite-dimensional estimates.

The issued run of `python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_016_SOURCE_BLIND_ARTIFACTS/round016_source_blind_exact.py` returned **PASS, 2,018 exact assertions**. The result JSON records all groups, the six finite-Fourier datasets, largest frequency coordinate 1,000,033, threshold rows, the nine input hashes, and the diagnostic source hash. After sealing, add `--check-only` to reproduce all assertions without rewriting the issued results.

| Adversarial challenge | Disposition |
|---|---|
| Is expected energy used as an unsupported fluctuation bound? | No. Equations (23), (29), and the deterministic absolute inequality (35) prove the actual L1 bridge. |
| Is only the long-wavelength Fourier range controlled? | No. Lemma (32) treats arbitrarily large k, and (27), (36), (37) treat arbitrarily large terminal m with a summable polynomial loss. |
| Does a Gaussian symbol have uniformly bounded shifts at the same cutoff? | In general it does not. The proof uses R/64 and proves the needed bound explicitly. |
| Does the long source retain the missing labels and Haar terms? | Yes: (25)–(26) give the raw contractions, (31) uses z0=0, and (39) exhibits the remaining finite-N one-label correction under iid expansion. |
| Was a singular self value hidden in the positive energy? | No. Only the smooth G_R has a self value, subtracted exactly in (22). The singular g and J have no assigned diagonal. |
| Could the positive Coulomb atom be replaced by the classical punctured Laplacian? | No. The endpoint contraction in (25) and regularized divergence in (11), (17) retain it. |
| Does positive Coulomb punctured Laplacian force the energy mean to increase initially? | This inference neglects the cutoff atom and potentially divergent initial force square. At fixed cutoff the initial energy derivative is nonpositive; (18) is passed by Fatou, not by asserting differentiability of the singular mean. |
| Does the proof break at alpha=1? | The lower bound (33) remains valid with constant time weight; all heat integrals and (32) still hold. |
| Does the proof require source L2 at or beyond s=d/2? | No. It uses the integrable source majorant (24) and the positive short-scale identity; E_R is a smooth positive Fourier quadratic form. |
| Does zero diffusivity rely on an entropy divided by zero? | No. The deterministic energy decrease supplies (18), while every later estimate is unchanged. |
| Does boundedness at s=d/2 prove scaled smallness? | No. That implication is explicitly rejected; above the threshold no decay is asserted either. |
| Has any positive-time iid factorization been used? | No. Iid is used for the initial mean energy; evolved-law estimates use the actual energy inequality. Equation (40) is an initial-law diagnostic only. |
| Is this a proof of a fluctuation theorem or a corrector domain? | No. Those objects are not used, and remain outside this card and this reconstruction. |

## 8. Dispositions and sealed handoff

| Claim or obligation | Disposition in this isolated context |
|---|---|
| Frozen kernel normalization and local coefficient | Reconstructed by the Gaussian heat integral. |
| Finite divergence measure, Coulomb atom, compensation | Reconstructed, with the exact endpoint measure in (10). |
| Actual finite-N collision-free process and same-noise passage needed here | Reconstructed by localized energy and local Gronwall; no uncountable uniform exceptional-set claim. |
| Actual nonpositive expected energy, including zero noise | Reconstructed with a fixed-cutoff free-energy identity and a stated Fatou passage. |
| Genuine source and all background-contraction integrability | Proved in (19), (24), (25), and the mode-summation passage. |
| Full raw uniform THM038 estimate | Proved in (38) throughout every frozen datum. No first unproved line remains in this proof attempt. |
| Quantitative scaled estimate and exact decay restriction | Proved in Section 6; no endpoint decay inflation. |
| Actual-law counterexample to the frozen card | None produced; the negation is excluded by the displayed proof if that proof survives the separate audit. |
| Independent certification of this reconstruction | Not claimed. Exact diagnostics and the table above are same-context self-checks. |
| Candidate comparison, hostile gate, canonical promotion | Reserved to the root after the seal. |
| Broader fluctuation mission and all listed exclusions | Not resolved or enlarged. |

The companion packet contains exact input snapshots, the input manifest, exposure record, diagnostic source and exact results, README, output hashes, and archive-verification evidence. The archive is checked for exact member equality, safe relative paths, no duplicates or symlinks, successful CRC verification, and byte/hash equality with every intended payload file. Its external seal records the archive digest and a duplicate report comparison. Issued report and packet files are made read-only after sealing; any correction must be a new superseding artifact. No canonical ledger or memorandum was edited, no commit or push was made, no dependency was installed, and no child agent or external search was used.

The report contains the complete proof and the exact disposition of every requested scope. Its next action is a root-only comparison with the independently sealed construction and a separate hostile gate; this context stops at the bounded sealed handoff.
