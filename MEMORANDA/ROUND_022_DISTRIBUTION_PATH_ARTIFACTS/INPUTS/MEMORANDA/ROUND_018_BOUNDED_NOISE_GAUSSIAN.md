# Round 018 — bounded-diffusivity finite-dimensional Gaussian fluctuations

TASK-084. Issued 2026-09-18 UTC. Bounded construction of the entire frozen THM-040. **CONDITIONAL PROVED CANDIDATE / CONSTRUCTOR SELF-CHECK; INDEPENDENT RECONSTRUCTION AND HOSTILE REVIEW PENDING.** This report supplies a complete implication from the expressly conditional, version-locked source modules. It does not certify their independent gates or assign independent certification to this construction.

The complete R16 proof supplies the actual quadratic-source estimate as an explicit conditional premise. The complete R10 proof supplies a sufficient quantitative actual-law estimate for the first-order thermal bracket: its empirical Fourier bound applies to uniformly smooth deterministic products of backward-test gradients. No singular corrector-gradient estimate is required. An initial-sigma-field-weighted stochastic exponential proves the full joint probability passage, including initial/thermal dependence. The covariance alone is not the conclusion.

The fourteen prescribed inputs were hash-checked, copied, and checked again in /Users/matthewrosenzweig/.codex/worktrees/hocf-r018-bounded-noise-construction, branch codex/hocf-r018-bounded-noise-construction, from published base faf6f775a55579722319795cd9a9921e5829a903. Root alone may integrate canonical records after the separate independent axes. The accompanying sealed packet contains exact input copies, source/exposure records, a fresh exact diagnostic with mutation controls, and reproducible input/output/archive verification.

## 1. Frozen assertion, exact negation, and premises

Fix exactly the data in THM-040: an integer \(d\ge3\), \(0<s\le d-2\) with \(s<d/2\), finite \(T\ge0\), and a fixed positive integer \(m\) with fixed deterministic \(t_j\in[0,T]\) and real smooth periodic \(h_j\). Haar measure \(\mu=dx\) on \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) has mass one. Fourier characters are \(e^{2\pi i k\cdot x}\). The coefficient-one zero-mean periodic Riesz interaction is
\[
 \widehat g(0)=0,\qquad \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1.1}
\]
For every \(N\ge2\), the actual singular particles satisfy
\[
 dX_i=\frac1N\sum_{\ell\ne i}K(X_i-X_\ell)\,dr+\sqrt{2\nu_N}\,dW_i,
 \qquad \eta_N=N^{-1}\sum_i\delta_{X_i}.
 \tag{1.2}
\]
Initial coordinates are iid Haar, independent of all independent standard Brownian drivers. The usual filtration includes the initial vector; Brownian increments remain independent of its time-zero sigma field. Set \(0\le\nu_N\le\nu_*<\infty\), \(\nu_N\to\bar\nu\ge0\), and
\[
 b(\nu)=
 \begin{cases}1,&0\le\nu\le1,\\ \nu^{-1},&\nu>1,\end{cases}
 \quad b_N=b(\nu_N),\quad \bar b=b(\bar\nu),\quad
 \sigma_N=\sqrt{Nb_N},\quad \rho_N=\eta_N-\mu .
 \tag{1.3}
\]
Thus \(\nu b(\nu)=\min(\nu,1)\). Zero diffusivity is defined directly, without division by zero.

The primary assertion is the conjunction of genuine required integrability, exact one-body Haar centering, and joint weak convergence in \(\mathbb R^m\) of
\[
 Z_{N,j}=\sigma_N\rho_N(t_j)[h_j]
 \tag{1.4}
\]
to a centered, possibly degenerate Gaussian vector with exactly the covariance in Section 8. Every fixed tuple is included, with zero/repeated times, constant tests and linear dependence. No rate of convergence of \(\nu_N\) is a hypothesis.

Its exact negation is the existence of one admitted fixed datum and one bounded convergent diffusivity sequence for which a needed genuine integrability or centering assertion fails, or the stated joint weak convergence fails for an admitted fixed tuple. A failed estimate, a generic exchangeable-law example, or a larger theorem outside this card is not that negation.

This construction uses the following **complete-source premises, with all issued conditional and audit statuses retained**.

| Version-locked input | Exact assertion used; hypothesis map and boundary |
|---|---|
| AGENTS.md and TASK-084 | Bounded construction, exact assertion/negation, source control, isolated single writer and sealed handoff. The explicit task restriction supersedes general instructions to inspect non-allowlisted README, orchestration, state and history or to make a commit. |
| ROUND_001_MODEL.md; R1 algebra Sections 1–2, especially (1.3), (2.3), (2.6)–(2.9) | Unit Haar/Fourier conventions; interaction \(1/N\); noise \(\sqrt{2\nu}\); ordered deleted pairs divided by \(N^2\); statistic \(P_N=U_2/2\). Section 3 below rederives the needed coefficients on singular paths. The smooth source's value on its diagonal is not imported. |
| R4 singular response Sections 2–5 | Coefficient-one heat representation and local singularity; \(K\in L^1\); the full finite measure \(D=\operatorname{div}K\), its zero mass and Coulomb atom/compensation; smooth-test integration by parts and heat passage. The supplied proof is used, not an unseen kernel source cited by it. |
| THM-026 and R6 particle realization Sections 1–8 | At each finite \(N,\nu,T\), with \(V=0\): actual global noncolliding measurable solution, pathwise uniqueness, positive pathwise minimum separation; same-noise fixed-\(N\) heat passage. The optional fixed-\(N\) density bound is used only in Section 9's initial derivative test. No uniform-\(N\) density estimate is inferred. THM-026's OPEN / UNAUDITED / VERSION_LOCKED card is not a proof. |
| THM-031 and complete R10 actual-law memorandum Sections 2–3, especially (2.6), (2.8), (3.5)–(3.7) | Actual nonpositive expected energy, uniform pair-energy moment, and \(\mathbb E|\widehat\eta_N(r,k)|^2\le\min(1,CN^{-(1-s/d)}|k|^{d-s})\). Section 4 reconstructs exactly the part required for the bracket. R10's proof explicitly handles zero noise by deterministic energy decrease; no entropy division at zero is used. Its corrector-domain, full-inverse, residual-tail and R9 premises are not imported. |
| THM-038 and complete R16 source extension Sections 2–7 | Full genuine actual-law source integrability and \(\sup_r\mathbb E|P_N[J_r]| \le C N^{s/d-1}\), uniform for \(N\ge2\), \(0\le\nu\le\nu_*\), and the actual backward test of each fixed \((t_j,h_j)\). The complete heat splitting, commutator and positive remainder proof is supplied and has been read. This is expressly conditional until its separate gates pass. Its broader range is used only inside THM-040's \(s<d/2\) row. |
| THM-039 and complete R17 critical memorandum Sections 1–5 | Comparison with the zero-limit-noise critical construction and its exact scope/status. The complete proof was read. Its critical reduction \(\nu_N\to0\) and its already-vanishing thermal error are not premises proving the present positive-noise result. The construction below rederives the first-order identity and probability passage. No independent R17 gate is presumed. |
| THM-040 | The entire unchanged frozen assertion, covariance, negation and exclusions. |

The precise file names and hashes are in the packet's input manifest and source preflight. No external literature theorem, private source, theorem-number attribution, novelty claim, unseen source theorem, or previous checker is used. Smooth Itô calculus and elementary finite sums, Fourier series, Gaussian integrals and measure convergence are used with the needed bounds given below.

All constants denoted \(C\) or \(C_u\) depend only on \(d,s,T,\nu_*\), the fixed kernel, the fixed finite tuple, and, for \(C_u\), its fixed real coefficient vector \(u\). They are independent of \(N\), the chosen \(\nu_N\), time, collision stops and heat parameters. Constants used solely for finite-\(N\) construction or the Section 9 diagnostic are labeled as such.

## 2. Kernel, actual paths, and exact centering

The relevant R4 normalization check can be written without a literature input. With \(\alpha=(d-s)/2\ge1\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\), the positive unit-mass torus heat kernel \(p_a\) gives
\[
 g=A\int_0^\infty a^{\alpha-1}(p_a-1)\,da,\qquad
 A\frac{\Gamma(\alpha)}{(4\pi^2|k|^2)^\alpha}=c_{d,s}|k|^{s-d}.
 \tag{2.1}
\]
The integral is Haar \(L^1\): at small \(a\), \(\|p_a-1\|_1\le2\); at large \(a\), the nonconstant Fourier series decays exponentially. Substitution in the central Euclidean Gaussian term gives precisely \(|z|^{-s}\). The other lattice terms at small \(a\) and the large-time difference have locally integrable bounds for every derivative. Hence \(g(z)=|z|^{-s}+H(z)\) near zero, with \(H\) smooth; \(g\) is smooth off zero, bounded below by a finite \(g_*<0\), and \(K(z)=s z|z|^{-s-2}-\nabla H(z)\). In particular \(K\in L^1\) because \(s+1<d\).

Distributional integration by parts outside a ball retains the inner flux \(s r^{d-s-2}\int_{\mathbb S^{d-1}}a(r\theta)\,d\theta\) for a smooth test \(a\). Below Coulomb it vanishes and the divergence is integrable; at Coulomb it tends to \(c_d a(0)\), where \(c_d=(d-2)|\mathbb S^{d-1}|\). Gamma recurrence and the zero Fourier coefficient identify the full measure:
\[
 D=\operatorname{div}K=
 \begin{cases}
 s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2.
 \end{cases}
 \quad D(\mathbb T^d)=0,\quad D\ge-\kappa\,dz
 \tag{2.2}
\]
for a fixed finite \(\kappa\). Its nonzero Fourier coefficient is
\[
 D_k=4\pi^2c_{d,s}|k|^{s+2-d}>0.
 \tag{2.3}
\]
The Coulomb atom is part of every convolution using \(D\). A classical punctured Laplacian does not replace (2.2).

Here is the finite-\(N\) mechanism being imported from the complete R6 source. With \(H_N=N^{-1}\sum_{i<\ell}g(x_i-x_\ell)\), the shifted nonnegative energy
\(\mathcal H_N=H_N-(N-1)g_*/2\) has collision-excluded compact sublevels, including every partial or simultaneous collision. The complete drift is \(B=-\nabla H_N\), and on the punctured configuration space
\[
 \Delta_{Nd}H_N=\frac2N\sum_{i<\ell}\Delta g(x_i-x_\ell)\le(N-1)\kappa.
 \tag{2.4}
\]
Smooth even collision cutoffs give a local measurable pathwise-unique solution by Picard iteration after subtracting the continuous additive noise. Until an energy exit \(\tau_R\), smooth Itô calculus gives drift
\(-|B|^2+\nu\Delta H_N\) and a true stopped energy martingale. It follows that
\[
 \mathbb P_x(\tau_R\le T)\le
 \frac{\mathcal H_N(x)+\nu(N-1)\kappa T}{R}.
 \tag{2.5}
\]
The complete drift square is retained; no individual force square is extracted. A bounded-energy path remains in a compact collision-excluded set and extends past any finite endpoint. Thus (2.5) gives global noncollision for each fixed start, almost surely. The source's joint measurability permits Fubini against iid Haar, whose initial shifted-energy mean is \(-(N-1)g_*/2\). No exceptional set common to every uncountable start or parameter is needed. Every realized continuous singular path has positive minimum pair distance on a finite horizon.

For the heat force \(K_\varepsilon=p_\varepsilon*K\), local \(C^1\) convergence away from zero follows by splitting off a smooth local part and bounding the distant \(L^1\) part with Gaussian tails. Coupled heat and singular solutions have the same additive noise. Gronwall, stopped before their separation reaches a quarter of the singular path's minimum pair distance, proves their uniform-in-time convergence at each fixed \(N,\nu,T\). These are exactly the fixed-\(N\) R6 hypotheses needed in Section 4's energy passage. No \(N\)-uniform heat rate is asserted.

Permutation equivariance gives exchangeability. Translating every initial coordinate by a common torus vector translates the entire path under the same Brownian increments, by the difference form of \(K\) and pathwise uniqueness. Initial iid Haar is invariant under every such translation. Each one-body marginal is therefore translation invariant; its nonzero Fourier coefficients vanish by choosing a translation with nontrivial phase. Trigonometric-polynomial density identifies the marginal with Haar. Consequently
\[
 \mathbb E\,\eta_N(r)[h]=\mu[h]
 \quad\text{for every deterministic }r\in[0,T]\text{ and every bounded measurable }h .
 \tag{2.6}
\]
This is exact finite-\(N\) centering. Higher marginals need not be product Haar. No deterministic correction, pressure subtraction or Wick/diagonal convention is inserted.

## 3. Genuine singular first-order identity

For \(\nu\ge0\) define \(Q_a^\nu\) on smooth real functions by preserving constants and multiplying a nonzero mode by
\[
 \exp[-a(D_k+\nu a_k)],\qquad a_k=4\pi^2|k|^2,\quad a\ge0.
 \tag{3.1}
\]
The notation \(Q_a=Q_a^{\bar\nu}\) is reserved for the limiting semigroup. For each terminal pair \((t_j,h_j)\), let
\[
 f_{N,j}(r)=Q_{t_j-r}^{\nu_N}h_j,\qquad 0\le r\le t_j .
 \tag{3.2}
\]
The response on smooth functions is
\[
 Rf(x)=-\int f(x+w)\,D(dw).
 \tag{3.3}
\]
It has multiplier \(-D_k\), preserves the zero mean condition and kills constants. Every spatial derivative of (3.2), and the needed time derivative, has an absolutely convergent Fourier series uniformly over the bounded diffusivity interval. The time multiplier has at most two powers of frequency. Thus
\[
 \partial_r f_{N,j}+\nu_N\Delta f_{N,j}+Rf_{N,j}=0,\qquad
 \mu[f_{N,j}(r)]=\mu[h_j].
 \tag{3.4}
\]
No derivative estimate for a pair corrector is used.

For a given such \(f_r\), define only off the diagonal
\[
 J_r(x,y)=K(x-y)\cdot(\nabla f_r(x)-\nabla f_r(y)).
\]
It is symmetric. Its magnitude is bounded by \(C(1+\operatorname{dist}(x,y)^{-s})\), using the gradient mean-value bound along a shortest torus geodesic. Its row contraction exists since \(K\in L^1\). Directly,
\[
 j_r(x):=\int J_r(x,y)\,dy
 =-\int K(x-y)\cdot\nabla f_r(y)\,dy
 =-\int f_r(x+w)\,D(dw)=Rf_r(x),\qquad \int j_r=0.
 \tag{3.5}
\]
The last integration by parts is distributional against a smooth test and uses all of (2.2). At Coulomb it is \(Rf=-c_d(f-\mu[f])\). It is not evaluation of a singular empirical diagonal.

Keep the precise statistic
\[
 P_N[J_r]=\frac1{2N^2}\sum_{i\ne\ell}J_r(X_i,X_\ell)
             -\eta_N[j_r]+\frac12\iint J_r(x,y)\,dx\,dy .
 \tag{3.6}
\]
The double integral is zero by (3.5), not by definition. Applying time-dependent Itô to the globally smooth observable \(N^{-1}\sum_i f_r(X_i)\), stopped in a collision-excluded compact set, the interaction is exactly
\[
 \frac1{N^2}\sum_{i\ne\ell}K(X_i-X_\ell)\cdot\nabla f_r(X_i)
 =\frac1{2N^2}\sum_{i\ne\ell}J_r(X_i,X_\ell)
 =P_N[J_r]+\eta_N[Rf_r].
 \tag{3.7}
\]
Oddness and ordered distinct labels give the factor one half. There is no force self term. The Itô correction is \(\nu_N\eta_N[\Delta f_r]\), with no mixed-particle Brownian trace. Equation (3.4) cancels the one-body drift exactly.

The actual pair-energy moment proved in Section 4 below makes the symmetrized force/source drift absolutely integrable in probability times time at each fixed \(N\). Its row is bounded. Noncollision makes collision stops eventually exceed the terminal time almost surely. Dominated convergence for these integrable drift functions passes their stopped integrals in \(L^1\). The bounded gradients pass stochastic integrals in \(L^2\) by their Itô isometry; bounded endpoints pass by dominated convergence. In using the stopped time-dependent observable, one first includes the integral of its bounded time derivative up to the stop. Thus the unstopped equation is a genuine identity, with a square-integrable true martingale:
\[
 \rho_N(t_j)[h_j]
 =\rho_N(0)[f_{N,j}(0)]
   +\int_0^{t_j}P_N[J_{N,j}(r)]\,dr
   +\frac{\sqrt{2\nu_N}}N\sum_i\int_0^{t_j}
                  \nabla f_{N,j}(r,X_i(r))\cdot dW_i(r).
 \tag{3.8}
\]
At zero noise the stochastic term is identically zero on the actual deterministic flow.

Define the scaled initial, source, and martingale terms by
\[
 I_{N,j}=\frac1{\sqrt N}\sum_i\sqrt{b_N}
                \big(f_{N,j}(0,X_i(0))-\mu[h_j]\big),\quad
 E_{N,j}=\sigma_N\int_0^{t_j}P_N[J_{N,j}(r)]\,dr ,
 \tag{3.9}
\]
\[
 M_{N,j}(a)=\sqrt{\frac{2\nu_N b_N}{N}}\sum_i
       \int_0^{a\wedge t_j}\nabla f_{N,j}(r,X_i(r))\cdot dW_i(r),
 \quad 0\le a\le T .
 \tag{3.10}
\]
Then \(Z_N=I_N+M_N(T)+E_N\) exactly. The full conditional THM-038 estimate, applied with horizon \(t_j\) and the same fixed \(h_j\), gives
\[
 \mathbb E|E_N|\le C N^{s/d-1/2}\longrightarrow0 .
 \tag{3.11}
\]
One takes the maximum of finitely many source constants; \(b_N\le1\). All times \(t_j=0\) have zero source integral. Equation (3.11) is the sole place requiring the threshold \(s<d/2\) for source decay. It is an actual-law \(L^1\) bound, not an estimate under product Haar.

## 4. Why the complete R10 source is sufficient for this bracket

The relevant quantitative law estimate can be recovered from the supplied R10 proof, without importing any source that is merely named elsewhere in that report. At a fixed heat cutoff and positive \(\nu\), its smooth probability density \(F_t^\varepsilon\) starts at one and satisfies the classical smooth Fokker–Planck equation with potential \(H_N^\varepsilon\). On the compact configuration torus all coefficient derivatives are bounded; the heat integral equation and smoothing give the classical solution, and comparison gives positive lower and finite upper density bounds on a fixed time interval. Entropy differentiation and periodic integration by parts are consequently legitimate at that cutoff:
\[
 \frac d{dt}\left(\nu\int F_t^\varepsilon\log F_t^\varepsilon
                       +\int H_N^\varepsilon F_t^\varepsilon\right)
 =-\int F_t^\varepsilon
       |\nabla H_N^\varepsilon+\nu\nabla\log F_t^\varepsilon|^2\le0.
 \tag{4.1}
\]
Both initial terms are zero; entropy is nonnegative on the unit-mass reference space. Hence \(\mathbb E H_N^\varepsilon(X_t^\varepsilon)\le0\). Heat positivity gives \(H_N^\varepsilon\ge(N-1)g_*/2\). The fixed-\(N\) same-noise path passage from Section 2 and local uniform kernel convergence give almost-sure convergence of this energy at each deterministic time. Fatou after subtracting the common lower bound gives
\[
 \mathbb E H_N(X_t)\le0.
 \tag{4.2}
\]
No singular Fisher-information passage occurs. At \(\nu=0\), the actual noncolliding gradient flow has \(dH_N/dt=-|B|^2\le0\); averaging the integrable iid initial energy zero proves (4.2) directly.

The shifted energy is nonnegative, so this also gives genuine integrability. Exchangeability, \(|g|\le g+2|g_*|\), and the local coefficient-one expansion imply
\[
 \mathbb E g(X_1-X_2)\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|,\qquad
 \mathbb E(1+\operatorname{dist}(X_1,X_2)^{-s})\le C .
 \tag{4.3}
\]
All are uniform over \(N,\nu,t\). These prove the integrability used in Section 3 and the source module. They do not bound an individual force square.

For \(0<r\le1\), truncate the heat integral rather than the particle heat cutoff:
\[
 g^{>r}=A\int_r^\infty a^{\alpha-1}(p_a-1)\,da,\qquad
 a_r(k)=A\int_r^\infty a^{\alpha-1}e^{-4\pi^2|k|^2a}\,da>0
 \quad(k\ne0).
\]
The coefficients are rapidly decaying, \(g^{>r}(0)\le C r^{-s/2}\), and positivity of the heat kernel gives \(g\ge g^{>r}-Ar^\alpha/\alpha\) off zero. Exact subtraction of the smooth self diagonal yields
\[
 H_N\ge \frac N2\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2
             -\frac12g^{>r}(0)-\frac{N-1}{2\alpha}Ar^\alpha .
 \tag{4.4}
\]
Here the self coefficient is exactly one half; the constant term counts \(N(N-1)\) ordered labels. At \(r_N=N^{-2/d}\), both errors are \(O(N^{s/d})\). Set \(q=1-s/d>0\). Taking actual expectations using (4.2) gives
\[
 \mathbb E\sum_{k\ne0}a_{r_N}(k)|\widehat\eta_N(t,k)|^2\le C N^{-q}.
 \tag{4.5}
\]
For \(0<|k|\le N^{1/d}\), the interval \([|k|^{-2},2|k|^{-2}]\) lies above \(r_N\) and gives \(a_{r_N}(k)\ge c|k|^{s-d}\). For higher frequencies use \(|\widehat\eta_N|\le1\). Increasing a fixed constant proves exactly the complete R10 estimate
\[
 \mathbb E|\widehat\eta_N(t,k)|^2
       \le\min\{1,CN^{-q}|k|^{d-s}\},\qquad k\ne0 .
 \tag{4.6}
\]
It holds at all deterministic times and throughout the fixed bounded noise interval, including zero. No positive-time product law is used.

Let \(p=(d-s)/2\). For a deterministic smooth scalar function \(\psi\), absolute Fourier convergence, Cauchy–Schwarz in probability and (4.6) imply
\[
 \mathbb E|\rho_N(t)[\psi]|
 \le C N^{-q/2}\sum_{k\ne0}|k|^p|\widehat\psi(k)|.
 \tag{4.7}
\]
This follows first for partial sums; their uniform deterministic tails pass expectations. It applies uniformly to a deterministic \(N,t\)-dependent family with the displayed seminorm bounded. This is the precise quantitative estimate needed here. It does not give uniform integrability of an \(N\)-dependent singular pair-corrector gradient product, the still-open tail in the full R10 target.

For clarity about uniform smoothness, put
\(\|v\|_{\mathcal A_r}=\sum_k(1+|k|)^r|\widehat v(k)|\), using the Euclidean norm for vector coefficients. Smooth functions have finite seminorms of every fixed order, by sufficiently many integrations by parts in Fourier coefficients. For \(r\ge0\), convolution and
\(1+|k+\ell|\le(1+|k|)(1+|\ell|)\) give
\[
 \|v\cdot w\|_{\mathcal A_r}\le\|v\|_{\mathcal A_r}\|w\|_{\mathcal A_r}.
 \tag{4.8}
\]
The multipliers (3.1) have modulus at most one, so
\(\|\nabla f_{N,j}(r)\|_{\mathcal A_p}\le2\pi\|h_j\|_{\mathcal A_{p+1}}\).
Thus every gradient product entering the bracket has the uniform seminorm required in (4.7).

## 5. Exact cross bracket and deterministic convergence

Independence of distinct Brownian drivers, with their exact coefficient in (3.10), gives
\[
 \langle M_{N,i},M_{N,j}\rangle_a
 =2\nu_N b_N\int_0^{a\wedge t_i\wedge t_j}
  \eta_N(r)[\nabla f_{N,i}(r)\cdot\nabla f_{N,j}(r)]\,dr.
 \tag{5.1}
\]
There is no deleted-pair factor \(N-1\) in this first-order bracket: the \(N\) Brownian coordinates cancel the \(1/N\) after scaling. Terms from distinct labels have zero quadratic covariation. The distinct initial and thermal vectors are not asserted independent.

Define the deterministic matrix
\[
 B_{N,ij}=2\nu_N b_N\int_0^{t_i\wedge t_j}
   \int\nabla Q_{t_i-r}^{\nu_N}h_i\cdot
             \nabla Q_{t_j-r}^{\nu_N}h_j\,dx\,dr.
 \tag{5.2}
\]
By exact one-body Haar centering, (5.2) is exactly
\(\mathbb E\langle M_{N,i},M_{N,j}\rangle_T\) for each \(N\). That mean identity alone would be insufficient. Equations (4.7)–(4.8) instead give the required concentration:
\[
 \mathbb E\left|\langle M_{N,i},M_{N,j}\rangle_T-B_{N,ij}\right|
 \le C N^{-q/2}.
 \tag{5.3}
\]
Tonelli applies to the absolute integrand in probability times time. This is the actual-law passage.

To handle the whole vector, fix \(u\in\mathbb R^m\) and put
\[
 G_{N,u}(r,x)=\sum_j u_j\mathbf1_{\{r\le t_j\}}\nabla f_{N,j}(r,x),\qquad
 M_N^u(a)=\sum_j u_jM_{N,j}(a).
\]
Values at the finitely many deterministic endpoints of these intervals do not affect any integral; a predictable version is taken. All stochastic integrands are bounded and adapted. The scalar bracket is
\[
 V_N^u=\langle M_N^u\rangle_T
 =2\nu_N b_N\int_0^T\eta_N(r)[|G_{N,u}(r)|^2]\,dr .
 \tag{5.4}
\]
It has a deterministic upper bound
\[
 0\le\langle M_N^u\rangle_a\le K_u:=
 2T\left(2\pi\sum_j|u_j|\|h_j\|_{\mathcal A_1}\right)^2,\qquad a\le T.
 \tag{5.5}
\]
The same bound holds for each deterministic limiting bracket below, since \(\nu b(\nu)\le1\). No assumption of bracket independence from the initial sigma field appears.

Write \(\delta_N=|\nu_N-\bar\nu|\). From the exponential multiplier and the mean-value theorem,
\[
 \|(Q_a^{\nu_N}-Q_a^{\bar\nu})h\|_{\mathcal A_r}
 \le4\pi^2a\,\delta_N\|h\|_{\mathcal A_{r+2}},\qquad 0\le a\le T .
 \tag{5.6}
\]
Also \(|\nu_N b_N-\bar\nu\bar b|\le\delta_N\). These bounds and (5.2) show
\[
 B_{N,ij}\longrightarrow B_{ij}:=
 2\bar\nu\bar b\int_0^{t_i\wedge t_j}
       \int\nabla Q_{t_i-r}h_i\cdot\nabla Q_{t_j-r}h_j\,dx\,dr,
 \qquad |B_{N,ij}-B_{ij}|\le C\delta_N .
 \tag{5.7}
\]
Consequently
\[
 \mathbb E|V_N^u-u^TBu|\le C_u(N^{-q/2}+\delta_N)\longrightarrow0.
 \tag{5.8}
\]
This is sufficient even when \(B\) is singular or zero. In particular no lower positive noise bound or convergence rate for \(\nu_N\) is required.

## 6. Initial triangular-test replacement and joint probability passage

The function \(\sqrt{b(\nu)}\) equals one up to \(\nu=1\) and equals \(\nu^{-1/2}\) above it; its derivative there has magnitude at most one half. Splitting an interval at one proves
\(|\sqrt{b_N}-\sqrt{\bar b}|\le\delta_N/2\).
Define the fixed bounded real vector function
\[
 V_j(x)=\sqrt{\bar b}\big(Q_{t_j}h_j(x)-\mu[h_j]\big),\qquad
 \bar I_N=N^{-1/2}\sum_{\ell=1}^N V(X_\ell(0)),\qquad
 A_{ij}=\int V_iV_j\,dx .
 \tag{6.1}
\]
Each difference
\[
 v_{N,j}=\sqrt{b_N}(Q_{t_j}^{\nu_N}h_j-\mu[h_j])-V_j
\]
has Haar mean zero and \(L^2\) norm at most \(C\delta_N\), by (5.6) or by heat \(L^2\) contraction and the corresponding multiplier bound. Initial iid preparation gives exactly
\[
 \mathbb E|I_{N,j}-\bar I_{N,j}|^2
  =\mathbb E\left|N^{-1/2}\sum_\ell v_{N,j}(X_\ell(0))\right|^2
  =\|v_{N,j}\|_2^2 .
 \tag{6.2}
\]
All cross-label terms vanish from zero mean and initial independence. Hence
\(\mathbb E|I_N-\bar I_N|\le C\delta_N\). There is no erroneous factor \(\sqrt N\,\delta_N\), so arbitrarily slow convergence of diffusivity is allowed.

For a fixed \(u\), Taylor's formula for a single bounded iid summand gives
\[
 \mathbb E e^{iu\cdot V(X_1(0))/\sqrt N}
   =1-\frac{u^TAu}{2N}+r_N,\qquad
 |r_N|\le\frac{\int|u\cdot V|^3\,dx}{6N^{3/2}} .
 \tag{6.3}
\]
Raising to the \(N\)-th power by initial independence gives
\[
 \mathbb E e^{iu\cdot\bar I_N}\longrightarrow e^{-u^TAu/2}.
 \tag{6.4}
\]
For example, compare the \(N\)-th power with \((1-u^TAu/(2N))^N\) by telescoping, with error \(O_u(N^{-1/2})\) for sufficiently large \(N\); the latter tends to the displayed exponential by the elementary logarithm expansion. Thus no nonsingularity assumption or unproved triangular-array CLT is hidden here.

The decisive joint step uses the full time-zero sigma field \(\mathcal F_{N,0}\). For the real scalar martingale \(M_N^u\), let
\[
 \mathcal E_N^u(a)=
 \exp\left(iM_N^u(a)+\frac12\langle M_N^u\rangle_a\right).
 \tag{6.5}
\]
Smooth Itô calculus gives \(d\mathcal E_N^u=i\mathcal E_N^u\,dM_N^u\). The drift from the second derivative is \(-\frac12d\langle M_N^u\rangle\), which cancels the **positive** compensator in (6.5). By (5.5), \(|\mathcal E_N^u|\le e^{K_u/2}\) and
\(\mathbb E\int|\mathcal E_N^u|^2\,d\langle M_N^u\rangle\le e^{K_u}K_u\).
The stochastic integral is therefore a true square-integrable complex martingale. In particular
\[
 \mathbb E[\mathcal E_N^u(T)\mid\mathcal F_{N,0}]=1.
 \tag{6.6}
\]
This conditional identity is valid although its integrand and terminal bracket depend on the initial particles.

For every \(\mathcal F_{N,0}\)-measurable complex \(Y_N\) with \(|Y_N|\le1\), write \(v=u^TBu\in[0,K_u]\). Multiplying (6.6) by \(Y_N\), subtracting the same expression with the compensator replaced by \(v\), and using the mean-value bound for \(e^{x/2}\) on \([0,K_u]\), gives
\[
 \left|\mathbb E(Y_Ne^{iM_N^u(T)})-e^{-v/2}\mathbb E Y_N\right|
 \le \frac12e^{K_u/2}\,\mathbb E|V_N^u-v|
 \le C_u(N^{-q/2}+\delta_N).
 \tag{6.7}
\]
The factor \(e^{-v/2}\le1\) was bounded above by one. This proves the necessary asymptotic factorization by direct argument; it does not assume finite-\(N\) independence, or substitute an expected bracket into a random exponential.

Take \(Y_N=e^{iu\cdot I_N}\). Equations (6.2)–(6.4) and (6.7) show
\[
 \mathbb E e^{iu\cdot(I_N+M_N(T))}
   \longrightarrow \exp[-\tfrac12u^T(A+B)u].
 \tag{6.8}
\]
The source error satisfies (3.11), so \(|e^{ix}-e^{iy}|\le|x-y|\) transfers (6.8) to \(Z_N\). More explicitly, for each fixed \(u\) and all sufficiently large \(N\),
\[
 \left|\mathbb E e^{iu\cdot Z_N}-e^{-u^T(A+B)u/2}\right|
 \le C_u\left(N^{s/d-1/2}+N^{-(1-s/d)/2}
                  +\delta_N+N^{-1/2}\right).
 \tag{6.9}
\]
This is a characteristic-function estimate, not a distribution-distance rate. It assumes no rate for the vanishing term \(\delta_N\).

## 7. From the joint characteristic function to weak convergence

Both \(A\) and \(B\) are real symmetric positive semidefinite Gram matrices: (6.1) represents the initial one, and (5.7) represents the time-space gradients, with nonnegative weight \(2\bar\nu\bar b\). Thus \(C=A+B\) is a finite positive semidefinite matrix. Let \(G=C^{1/2}\mathcal Z\), with \(\mathcal Z\) a standard real \(m\)-dimensional Gaussian. This defines a centered Gaussian with covariance \(C\), including the zero or singular matrix.

Here is a direct weak-convergence passage. Put \(Y_N=I_N+M_N(T)\) just within this paragraph; it is distinct from the bounded sigma-field multiplier in (6.7). Initial variances and the bounded martingale brackets show \(\sup_N\mathbb E|Y_N|^2<\infty\). In fact the initial/martingale cross expectations vanish: \(I_N\) is time-zero measurable and the true martingale has conditional mean zero at time zero. This orthogonality is not independence. The fixed-\(N\) variables \(I_N\) are bounded, so the conditional-expectation product is legitimate. Its variance identity has precisely the initial trace plus \(\sum_j B_{N,jj}\).

For \(\varepsilon>0\), add an independent \(\sqrt\varepsilon\mathcal Z'\) to \(Y_N\) and \(G\). The densities are Gaussian mixtures. The elementary Gaussian Fourier integral and Fubini express them as inverse Fourier transforms of their characteristic functions times \(e^{-\varepsilon|u|^2/2}\). This multiplier is integrable. Equation (6.8) and dominated convergence in \(u\) imply uniform convergence of these convolved densities in their spatial variable. The convolved variables have uniformly bounded second moments, hence uniform tail bounds by Markov's inequality. Split integration of a bounded Lipschitz test into a compact ball and its complement: use uniform density convergence on the ball and the uniform tail bound on the complement. This proves convergence of expectations of each such test for the convolved variables.

Coupling with the added Gaussian changes a Lipschitz test expectation by at most its Lipschitz constant times \(\sqrt\varepsilon\,\mathbb E|\mathcal Z'|\). Let \(N\to\infty\) at fixed \(\varepsilon\), then \(\varepsilon\downarrow0\), to obtain convergence for every bounded Lipschitz test of \(Y_N\) to \(G\). This also gives ordinary finite-dimensional weak convergence: the uniform tails reduce a bounded continuous test to a compact ball, where uniform continuity allows uniform Lipschitz approximation. No density for the possibly degenerate \(G\) was required.

Finally, \(Z_N-Y_N=E_N\) tends to zero in \(L^1\) by (3.11). It transfers every bounded Lipschitz expectation to the actual vector \(Z_N\). It also preserves tightness: for \(R>0\),
\[
 \mathbb P(|Z_N|>R)
 \le\mathbb P(|Y_N|>R/2)+\mathbb P(|E_N|>R/2)
 \le 4R^{-2}\mathbb E|Y_N|^2+2R^{-1}\mathbb E|E_N|.
\]
The source error has a uniform first-moment bound since its exponent in (3.11) is negative. The same compact-ball approximation therefore extends the limit to bounded continuous tests. This proves the entire asserted joint weak convergence, not only each separate coordinate or the covariance.

## 8. Covariance, degeneracies, and scope

The real-space covariance just proved is exactly
\[
 C_{ij}=\bar b\int(Q_{t_i}h_i-\mu[h_i])(Q_{t_j}h_j-\mu[h_j])\,dx
 +2\bar\nu\bar b\int_0^{t_i\wedge t_j}
        \int\nabla Q_{t_i-r}h_i\cdot\nabla Q_{t_j-r}h_j\,dx\,dr.
 \tag{8.1}
\]
Write \(L_k=D_k+\bar\nu a_k>0\) for \(k\ne0\). Fourier expansion of the two Gram terms is absolutely summable by smoothness. The time-space term may be integrated term by term because \(\sum a_k|\widehat h_i(k)||\widehat h_j(k)|<\infty\) and \(T<\infty\). The exact time integral is
\[
 \int_0^{t_i\wedge t_j}e^{-(t_i+t_j-2r)L_k}\,dr
 =\frac{e^{-|t_i-t_j|L_k}-e^{-(t_i+t_j)L_k}}{2L_k}.
\]
Combining it with the initial term gives
\[
 \boxed{
 C_{ij}=\bar b\sum_{k\ne0}\widehat h_i(k)\overline{\widehat h_j(k)}
 \left[
 \frac{D_k}{L_k}e^{-(t_i+t_j)L_k}
 +\frac{\bar\nu a_k}{L_k}e^{-|t_i-t_j|L_k}
 \right].}
 \tag{8.2}
\]
All coefficients and factors match THM-040. For real tests, opposite modes are conjugate pairs, and (8.1) fixes the real symmetric covariance. The initial exponent contains the sum of the times; only the thermal component contains their difference.

Constant tests give zero fluctuations and zero rows exactly. At zero time the associated stochastic/source integrals vanish; \(Q_0h=h\). At \(T=0\), the covariance is simply \(\bar b\) times the Haar covariance of the fixed tests. Repeated times or tests require no separate proof. A linear combination has zero limiting variance exactly when its initial \(L^2(dx)\) Gram function vanishes and, if \(\bar\nu>0\), its time-space gradient combination vanishes in \(L^2(dr\,dx)\). This includes exact linear dependence of tests at a common time. No inverse covariance matrix or positive-definiteness assumption has been used.

If \(\bar\nu=0\), then \(\bar b=1\), \(L_k=D_k\), and the thermal term is zero directly; (8.2) reduces to the THM-039 covariance. This includes arbitrary admitted cooling sequences, even ones cooling faster than finite microscopic criticality, and sequences with exactly zero noise terms. If \(\nu_*=0\), the whole proof is the deterministic-flow initial-fluctuation argument. If \(\bar\nu>0\), the nonzero thermal Gram term remains. The kink of \(b\) at one is harmless because the elementary Lipschitz bounds used above hold across it.

The bounded diffusivity hypothesis, fixed smooth test list, actual iid-Haar preparation, homogeneity, periodic gradient model, \(0<s\le d-2\) and \(s<d/2\) remain in force. No path-space tightness, distribution-valued theorem, growing list, arbitrary preparation, inhomogeneous background, logarithmic normalization, unbounded diffusivity, or higher-hierarchy assertion is obtained. The old energy-floor condition, full microscopic subcriticality and positive finite microscopic criticality remain distinct. Some bounded-noise sequences in the present restricted row lie in the subcritical regime; this does not certify the full microscopic-subcritical flagship.

## 9. Independent falsification routes and exact diagnostics

The principal proof uses source reduction and a random-bracket exponential. The falsification route starts instead from the literal finite-particle initial generator and from a solvable conditional Gaussian mixture. These challenge different logical steps.

First let \(h\) be a fixed smooth real test with mean zero, \(N,\nu\) fixed and \(b=b(\nu)\). Write
\[
 \mathcal D(h)=\sum_{k\ne0}D_k|\widehat h(k)|^2,\qquad
 \mathcal A(h)=\int|\nabla h|^2\,dx .
\]
At initial product Haar the exact first derivative of the scaled actual variance is
\[
 \left.\frac d{dt}\mathbb E[(\sigma_N\rho_N(t)[h])^2]\right|_{0}
 =-2b\frac{N-1}{N}\mathcal D(h).
 \tag{9.1}
\]
For the mixed initial/time covariance it is
\[
 \left.\frac d{dt}
 \mathbb E[\sigma_N\rho_N(0)[h]\;\sigma_N\rho_N(t)[h]]\right|_{0}
 =-b\left(\frac{N-1}{N}\mathcal D(h)+\nu\mathcal A(h)\right).
 \tag{9.2}
\]
To derive the interaction term directly, expand the ordered force sum against the initial empirical test. A test label outside the ordered force pair integrates to zero. The label on the differentiated coordinate integrates the partner force to zero. The other pair label gives \(\int h\,Rh=-\mathcal D(h)\). The exact label coefficient before multiplying by \(Nb\) is \((N-1)/N^2\). For (9.1) there are two differentiated test factors. Its diffusion contribution is \(-2\nu b\mathcal A(h)\), canceled by the bracket \(+2\nu b\mathcal A(h)\). In (9.2) only the terminal test is differentiated, leaving \(-\nu b\mathcal A(h)\). These are independent literal finite-label tests of the source and thermal coefficients.

The required singular initial differentiation is valid at fixed \(N\). R6 Section 8 gives \(F_r\le e^{(N-1)\kappa r}\) from initial density one. A globally smooth configuration observable has generator in Haar \(L^1\), since \(K\in L^1\). On a fixed short time interval approximate that generator in \(L^1\) by continuous functions; the density bound controls the errors uniformly and path continuity handles the approximants. For (9.2), the additional bounded initial observable multiplies these errors by its finite fixed-\(N\) supremum, and joint path continuity identifies the initial limit. Weighted martingale expectations vanish because the weight is time-zero measurable. Thus the integral Itô identity differentiates at zero. No bound uniform in \(N\) on a singular Taylor remainder is claimed.

The proposed limiting covariance passes both tests: its equal-time derivative at zero is \(-2\bar b\mathcal D(h)\); its initial/time derivative is \(-\bar b(\mathcal D(h)+\bar\nu\mathcal A(h))\). Their finite-\(N\) discrepancy is precisely the deleted-label factor in (9.1)–(9.2), which tends to one. This is a consistency test, not an interchange-of-derivative-and-limit theorem.

Second, let \(S\) take values \(+1,-1\) equiprobably and be independent of a standard Gaussian \(W\). For rational \(0<e<1\), let \(M=\sqrt{1+eS}\,W\). This is the terminal value of a martingale with initial-measurable integrand and bracket \(1+eS\). Exactly,
\[
 \mathbb E(SM)=0,\qquad \mathbb E(SM^2)=e\ne0,\qquad
 \mathbb E\!\left[e^{izM+z^2(1+eS)/2}\mid S\right]=1.
 \tag{9.3}
\]
Thus orthogonality does not give finite-sample independence, and replacing a random bracket by its expectation without concentration is invalid. The positive compensator and bounded-bracket replacement in (6.5)–(6.7) pass this test. The mixture is a diagnostic of a probability inference, not a counterexample in the admitted particle law class.

The fresh standard-library program in the artifact directory implements exact Gaussian-rational sparse Fourier arithmetic for literal finite-particle generators; checks the deleted source/response identity, full cross carré du champ and initial covariance/variance derivatives; compares two independently assembled exponential-polynomial covariance formulas; checks constants, repeated times and exact linear dependencies; and checks conditional Gaussian-mixture moments and compensated characteristic series. It uses no previous checker, random samples, floating-point tolerance, or dependency installation. Physical first derivatives are \(2\pi\) times the Fourier diagnostic derivative; generator and bracket expressions restore the common \((2\pi)^2\) factor. The covariance tests treat positive modal \(D,a\) as exact symbolic parameters through rational instances, not as a substitute for the singular normalization proof.

Mutation controls deliberately remove a source half, change a response sign, remove the Brownian factor two, insert an erroneous \(1/N\), suppress a cross bracket, conflate the time sum with time difference, discard the thermal contribution, use the wrong compensator sign and replace a random bracket by its mean. Every mutation has an explicit witness and must be rejected. The exact assertion counts, category outcomes, mutation witnesses and program digest are recorded in the diagnostic JSON; the README records the command and result. These are constructor self-checks only.

## 10. Adversarial self-review, dispositions, and handoff

| Challenge | Disposition |
|---|---|
| Does R10 supply only a mean bracket or a product-law estimate? | No. Its full actual Fourier estimate gives (4.7), hence the \(L^1\) random-bracket deviation (5.3). Haar one-body centering supplies only the exact mean and is not used as concentration. |
| Are initial and thermal terms assumed independent? | No. The bounded time-zero weight in (6.6)–(6.7) proves the needed joint factorization; (9.3) rejects the invalid finite-\(N\) shortcut. |
| Does a named martingale CLT hide conditional hypotheses? | No martingale CLT is invoked. The true exponential martingale, its integrability, the bracket replacement and the weak-convergence passage are all proved. |
| Could slow diffusivity convergence produce a \(\sqrt N\) loss? | The exact iid variance of the centered triangular-test difference is (6.2), with error \(C\delta_N\), not \(C\sqrt N\delta_N\). |
| Is singular Itô calculus used for a pair kernel? | No. The observable is globally smooth and only the drift is localized. The actual pair-energy moment passes its symmetrized drift; stochastic gradients are bounded. |
| Is the Coulomb atom lost? | It remains in (2.2), (3.3), (3.5), and both initial generator tests. The punctured value is confined to collision-excluded energy calculus. |
| Is a singular corrector-tail assertion smuggled in from R10? | No. All bracket probes here are uniformly smooth one-body functions. R10's remaining singular pair-gradient tail and its extra source premises are nondependencies. |
| Are zero noise, constant tests, zero/repeated times or degeneracy omitted? | They are retained by the same identities and Gram construction; Section 8 states their exact consequences. |
| Is a source gate promoted by this constructor? | No. The entire THM038 quantitative source is expressly conditional; all earlier cards and source bytes retain their issued statuses. |

| Claim or negation | Disposition at this handoff |
|---|---|
| Entire frozen THM-040 | CONDITIONAL PROVED CANDIDATE from the version-locked complete source premises; full first-order singular, actual-law bracket, initial and joint probability passages supplied. |
| Exact negation of THM-040 | Excluded by this complete conditional argument when its source premises hold; no admitted counterexample found. It is not claimed unconditionally excluded before the source and independent gates. |
| Sufficiency of R10's actual Fourier estimate for this first-order bracket | PROVED HERE by (4.7)–(5.8), using the complete source with its actual-law and zero-noise scope. |
| Finite-\(N\) initial/thermal independence shortcut | DISPROVED as a general inference by (9.3); neither assumed nor needed. |
| Earlier R4/R6/R10/R16/R17 assertions and audit statuses | Unchanged as issued. The present checks are exposed constructor work, not independent verification. |
| Broader campaign or higher hierarchy | NOT CLAIMED. |

No canonical state, historical input, previous audit, commit or remote was changed. The only worktree writes beyond the prescribed exact input overlay are this memorandum and its unique artifact directory and sibling sealed archive/seal files. No current audit, root scratch, state/history, memory file, separate prior checker/program/results artifact, non-allowlisted mathematical file, external search, dependency installation, child agent or publication was used. The exposure record distinguishes unavoidable ambient instructions and filename-only Git status from mathematical inputs.

The root's next action is fresh whole-claim reconstruction and separate hostile review of this entire conditional THM-040 construction, followed by comparison of the exact source hypotheses, dependence argument and sealed bytes. Root alone may update canonical ledgers or assign audit status. This is the complete bounded sealed handoff, not campaign completion. Any correction after issuance must be a new superseding artifact rather than an edit to the sealed packet.
