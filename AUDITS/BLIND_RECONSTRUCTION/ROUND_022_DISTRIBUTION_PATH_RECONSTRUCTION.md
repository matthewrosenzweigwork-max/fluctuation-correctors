# AUD063 — whole distribution-path blind reconstruction

TASK097, 2026-09-18 UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r022-distribution-path-blind`; branch: `codex/hocf-r022-distribution-path-blind`; published base: `64ac0538dff37a37d0883661b401ad04c311a5e5`.

**Disposition: the entire frozen THM044/PO031 is reconstructed, conditional on the exact supplied complete-source premises. No analytic gap or admitted counterexample was found.** This is a fresh blind reconstruction of the frozen assertion, not a review of the root's construction: that construction, its artifacts, current state, other audits and outside sources were not read. The reconstruction includes actual Hilbert-valued continuous paths, both quantitative interfaces, the Gaussian series, actual tightness, and convergence against every bounded continuous functional in the stated uniform topology. Supporting finite diagnostics do not certify these analytic statements. Current source-gate matching, comparison with the root, separate hostile review and promotion remain root responsibilities.

## 1. Frozen conjunction, negation, and source boundary

Fix precisely an integer \(d\ge3\), \(0<s\le d-2\), \(s<d/2\), \(0\le T<\infty\), and \(0\le\nu_N\le\nu_*<\infty\), with \(\nu_N\to\bar\nu\ge0\), without a rate. On the unit Haar torus use the coefficient-one periodic Riesz kernel
\[
 \widehat g(0)=0,\quad \widehat g(k)=c_{d,s}|k|^{s-d},\quad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad K=-\nabla g.
\]
The actual singular gradient particles, with no external drift, start iid Haar independently of the independent standard Brownian motions and have interaction coefficient \(1/N\) and noise \(\sqrt{2\nu_N}\). Set \(b(0)=1\), \(b(\nu)=\min(1,\nu^{-1})\) for positive \(\nu\), \(b_N=b(\nu_N)\), \(\bar b=b(\bar\nu)\), \(\sigma_N=\sqrt{Nb_N}\), and \(Z_N=\sigma_N(\eta_N-dx)\).

Let \(\alpha=(d-s)/2\), \(M=d+2\), \(R=\alpha+M+3\). Fix exactly any real
\[
 r>R+d/2=2d+5-s/2.                                      \tag{1}
\]
The Hilbert norm is the frozen one, \(\|u\|_{-r}^2=\sum_k(1+|k|^2)^{-r}|\widehat u(k)|^2\), with real conjugate symmetry and zero constant coefficient. Write \(\mathcal X=C([0,T],H^{-r}_0)\), with uniform Hilbert norm. The mean-zero closed subspace embeds isometrically into the full stated space, so proving convergence there proves exactly the full-space assertion as well: restriction of any full-space bounded continuous functional is bounded continuous on this subspace.

Use the prescribed real orthonormal sine/cosine basis \(e_l\); both basis functions belonging to \(\{k,-k\}\) have weight \(w_l=(1+|k|^2)^{-r}\), \(a_l=4\pi^2|k|^2\), \(D_l=4\pi^2c_{d,s}|k|^{s+2-d}\), and \(L_l=D_l+\bar\nu a_l>0\). The target series has coefficients
\[
 G_l(t)=\sqrt{\bar b}\left[e^{-L_lt}\xi_l+
 \sqrt{2\bar\nu a_l}\int_0^t e^{-L_l(t-u)}dB_l(u)\right],             \tag{2}
\]
with all the independent normals and Brownian motions specified in the frozen card.

The complete conjunction requires exact Haar centering; genuine continuous random paths; a continuous decomposition \(Z_N=Y_N+E_N\); the source bound \(\mathbb E\|E_N\|_{\mathcal X}\le C\sqrt{b_N}N^{s/d-1/2}\); the Fourier-tail bound
\[
 \mathbb E\|(1-\Pi_K)Y_N\|_{\mathcal X}^2
 \le C\sum_{|k|>K}(1+|k|^2)^{-r}(1+|k|^2);                       \tag{3}
\]
existence and continuity of (2) as an actual Gaussian random distribution; actual tightness; and weak convergence in this uniform topology. Its exact negation is an admitted fixed datum/noise sequence violating any member of that conjunction. It is not the failure of a selected proof estimate or a counterexample in a different law class.

The task card and manifest were read first. Exactly sixteen input byte strings were checked before overlay and checked afterward. All supplied full mathematical reports were read in their entirety. References in those narratives to unprovided material were not followed. The older reports' conditional histories and issued status labels are unchanged. The R17 comparison in R18 supplies no premise. In particular, neither R10's unsmoothed pair-corrector domain nor any R9 assertion is needed below. Detailed exposure and the sixteen exact hashes are in the accompanying packet.

| Full authorized source | Mathematical use and excluded inference |
|---|---|
| AGENTS; frozen R1 model; TASK097 | Model, exact scope, normalization, isolation and bounded handoff. The task overrides broad orientation/state instructions. |
| R1 algebra, entire report | Ordered deleted statistic, denominator \(N^2\), factor \(1/2\), first-order response and independent-noise bracket. Singular identities are justified below, not imported from a smooth diagonal assignment. |
| R4 singular response, entire report | Heat normalization, local coefficient one, integrable force, finite divergence measure with its Coulomb atom and compensation. No pair-propagator theorem is needed. |
| THM026 and full R6 | Actual measurable noncolliding finite-particle realization and fixed-\(N\) same-noise heat passage. No uniform density or heat-passage rate is inferred. |
| THM031 and full R10 | Only its proved energy/pair-moment/Fourier mechanisms in Sections 2–3 are used; the other conditional modules and residual singular-tail assertions are nondependencies. |
| THM038 and full R16 | Explicit deterministic retained-kernel commutator, positive discarded-kernel domination and actual energy control. Their test seminorm is retained quantitatively. |
| THM040 and full R18 | Complete finite-tuple probability argument, including initial/thermal dependence and bounded-continuous passage. Its R17 comparison is not used. |
| THM042 and full R20 | Complete conditional finite-observable path proof, including its actual compactness construction. The necessary finite-mode mechanisms are reconstructed in Sections 7–8 below. Its source gate is not certified here. |
| THM044 | Entire unchanged assertion, topology, quantitative interfaces and negation. |

## 2. Checked singular and actual-law interfaces

Here are the precise complete-source facts used, with their mechanisms and uniformity checked. They are retained as source premises for audit accounting; no old status label establishes them.

With \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\) and the positive periodized Gaussian \(p_v\),
\[
 g=A\int_0^\infty v^{\alpha-1}(p_v-1)dv.                           \tag{4}
\]
The small-time integral is in Haar \(L^1\) since \(\|p_v-1\|_1\le2\), and the large-time nonconstant Fourier series decays exponentially. Its nonzero coefficient is \(A\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}\), exactly the frozen coefficient. The substitution \(z=|x|^2/(4v)\) in the central Euclidean Gaussian gives precisely \(|x|^{-s}\). Other lattice translates and their derivatives are exponentially small at small time locally near zero; the remaining large-time difference is integrable with every spatial derivative. Thus \(g=|x|^{-s}+H\) locally, with \(H\) smooth, \(g_*:=\inf g<0\) finite, and \(K\in L^1\) because \(s+1<d\).

Integration outside a ball retains boundary flux \(s\varepsilon^{d-s-2}\int_{\mathbb S^{d-1}}f(\varepsilon\theta)d\theta\). It vanishes below Coulomb and becomes \(c_df(0)\) at Coulomb, where \(c_d=(d-2)|\mathbb S^{d-1}|\). Gamma recurrence and the zero Fourier mode identify the full measure
\[
 D:=\operatorname{div}K=
 \begin{cases}s(d-2-s)g_{s+2}\,dx,&s<d-2,\\c_d(\delta_0-dx),&s=d-2.
 \end{cases}                                                    \tag{5}
\]
It has zero mass, Fourier coefficients \(D_k\) for nonzero \(k\), and a lower bound \(D\ge-\kappa dx\) with fixed finite \(\kappa\). In every smooth-test contraction (5), including both endpoint terms, is used. The punctured classical Laplacian is confined to stopped particle energy calculus.

For \(H_N=N^{-1}\sum_{i<j}g(x_i-x_j)\), the shift \(H_N-(N-1)g_*/2\) is a sum of nonnegative terms. Every partial or simultaneous collision makes one term diverge. Its sublevels are compact and collision-free. The complete drift is \(-\nabla H_N\), and
\[
 \Delta_{Nd}H_N=\frac2N\sum_{i<j}\Delta g(x_i-x_j)\le(N-1)\kappa.
\]
Smooth collision cutoffs give measurable local solutions by Picard iteration after subtracting additive noise. On an energy sublevel the stopped Itô drift is exactly \(-|\nabla H_N|^2+\nu\Delta H_N\); the martingale has bounded integrand. Its expectation gives energy-exit probability at most \([H_N(x)-(N-1)g_*/2+\nu(N-1)\kappa T]/B\) at level \(B\). Bounded-energy trajectories extend, so letting \(B\to\infty\) gives global noncollision for each fixed start. Joint measurability permits integration against iid Haar. Each realized finite-horizon path has positive minimum pair distance. Local \(C^1\) convergence of heat forces off zero, cancellation of common Brownian noise and Gronwall give the full fixed-\(N\) same-noise heat passage. This uses no rate uniform in \(N\), and no exceptional event uniform over uncountably many initial states is asserted.

At fixed heat cutoff and positive noise, the smooth law starts at density one. Its positive, bounded classical density satisfies the legitimate smooth identity
\[
 \frac d{dt}\left(\nu\int F\log F+\int H_N^\varepsilon F\right)
 =-\int F|\nabla H_N^\varepsilon+\nu\nabla\log F|^2\le0.
\]
Both initial terms are zero and entropy is nonnegative on the mass-one space. Heat positivity gives the common lower bound \(H_N^\varepsilon\ge(N-1)g_*/2\). The fixed-\(N\) path passage and local energy convergence allow Fatou after that lower shift. At zero noise, deterministic energy decrease applies directly. Consequently, uniformly in admitted \(N,\nu,t\),
\[
 \mathbb EH_N(X_t)\le0,\qquad
 \mathbb E(1+\operatorname{dist}(X_1(t),X_2(t))^{-s})\le C.           \tag{6}
\]
The shifted energy first establishes integrability; then exchangeability and \(|g|\le g+2|g_*|\) give \(\mathbb E|g(X_1-X_2)|\le2|g_*|\). No individual force-square estimate is inferred. No singular Fisher information is passed.

Common translations commute with the actual measurable path map by pathwise uniqueness and the difference force. Initial iid Haar is invariant under them; each one-body marginal is therefore translation invariant. Every nonconstant Fourier coefficient vanishes, and trigonometric-polynomial density identifies that measure with Haar. Thus centering is exact for every deterministic time and bounded measurable test. Higher marginals are not asserted independent.

## 3. A simultaneous source inequality with the exact frequency cost

For clarity, the spatial splitting scale below is \(\ell\), distinct from both time and the Hilbert exponent. Put \(w_\ell(v)=(1-e^{-v/\ell})^M\), \(\psi_\ell=1-w_\ell\), and
\[
 g_\ell=A\int_0^\infty v^{\alpha-1}w_\ell(v)(p_v-1)dv,\quad
 Q_\ell=A\int_0^\infty v^{\alpha-1}\psi_\ell(v)p_vdv\ge0,\quad
 c_\ell=\int Q_\ell=C_{d,s,M}\ell^\alpha.
\]
The exact splitting is \(g=g_\ell+Q_\ell-c_\ell\) in Haar \(L^1\) and off zero. The retained kernel is \(C^2\): its Fourier coefficients have decay \(O_\ell(|k|^{-2\alpha-2M})\), summable with two derivatives. Its strictly positive nonzero coefficients are
\[
 a_\ell(k)=A\int_0^\infty v^{\alpha-1}w_\ell(v)e^{-4\pi^2v|k|^2}dv,
 \qquad 0\le g_\ell(0)\le C\ell^{-s/2},\quad 0<\ell\le2.
\]
The last bound follows by splitting the heat integral at \(\ell\) and at one, using \(w_\ell(v)\le\min(1,(v/\ell)^M)\). Define
\[
 \mathcal E_\ell(x)=\tfrac12\sum_{k\ne0}a_\ell(k)|\widehat\eta_N(k)|^2,
 \qquad \mathcal S_\ell(x)=\frac1{2N^2}\sum_{i\ne j}Q_\ell(x_i-x_j).
\]
Both are nonnegative. Exact deleted-label counting, including the smooth self diagonal and the constant background, gives
\[
 \frac{H_N}N=\mathcal E_\ell+\mathcal S_\ell
 -\frac{g_\ell(0)}{2N}-\frac{N-1}{2N}c_\ell,
 \quad
 \mathbb E(\mathcal E_\ell+\mathcal S_\ell)(X_t)
 \le C(N^{-1}\ell^{-s/2}+\ell^\alpha).                            \tag{7}
\]
Integrability in this equality follows from (6) and the splitting. It remains valid through scale two, as needed below.

For smooth real \(f\), retain the literal source
\[
 J^f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y)),\quad x\ne y,
\]
\[
 P_N[J^f]=\frac1{2N^2}\sum_{i\ne j}J^f(x_i,x_j)
 -\eta_N\left[\int J^f(\cdot,y)dy\right]+\frac12\iint J^f.        \tag{8}
\]
No value of the singular diagonal is assigned. Write \(\|f\|_{\mathcal A_R}=\sum_k(1+|k|)^R|\widehat f(k)|\). The complete deterministic R16 proof gives, simultaneously for all collision-free configurations and smooth real \(f\),
\[
 |P_N[J^f](x)|\le C\|f\|_{\mathcal A_R}
 [\mathcal E_\ell(x)+\mathcal S_{2\ell}(x)+c_{2\ell}].             \tag{9}
\]
The frequency cost in (9) is essential and is checked as follows. Integrating the derivative of \(v^\alpha w_\ell(v)e^{-\lambda v}\), with zero endpoints, and using \(0\le vw_\ell'(v)\le Mw_\ell(v)\), bounds the radial logarithmic slope of \(a_\ell\) by \(L=2(\alpha+M)\). Integrating that slope between nonzero lattice radii gives
\[
 \frac{|ka_\ell(k)-ja_\ell(j)|}{\sqrt{a_\ell(k)a_\ell(j)}}
 \le(1+L)|k-j|(1+|k-j|)^{L/2+1}.
\]
Indeed set \(u=\min(|k|,|j|)\ge1\), \(v=\max(|k|,|j|)\); then \(a_\ell(u)/a_\ell(v)\le(v/u)^L\), \(a_\ell(u)-a_\ell(v)\le La_\ell(u)(v-u)/u\), and \(v/u\le1+|k-j|\). The smooth retained source has diagonal zero. Symmetrizing its full-product Fourier expression gives
\[
 -\pi i\sum_{k,j\ne0}[ka_\ell(k)-ja_\ell(j)]\cdot
 \widehat{\nabla f}(j-k)\widehat\rho(k)\overline{\widehat\rho(j)}.
\]
Absolute summability follows from the retained coefficients and smooth test; Cauchy–Schwarz on each frequency translate bounds it by \(C\mathcal E_\ell\sum_q|q|(1+|q|)^{\alpha+M+1}|\widehat{\nabla f}(q)|\), at most \(C\mathcal E_\ell\|f\|_{\mathcal A_R}\). This proves the retained part with exactly \(R=\alpha+M+3\).

Termwise differentiation of each Gaussian gives \(\operatorname{dist}(z,0)|\nabla p_v(z)|\le C_dp_{2v}(z)\). The shortest-geodesic mean-value estimate for \(\nabla f\) and the substitution \(u=2v\) therefore give \(|J^f_{g-g_\ell}(x,y)|\le C\|D^2f\|_\infty Q_{2\ell}(x-y)\). In (8) the three original terms contribute respectively \(\mathcal S_{2\ell}\), \(c_{2\ell}\), and \(c_{2\ell}/2\). Since \(R>2\), this proves (9). It is positive-kernel domination of an absolute value, not weighted positive semidefiniteness.

Now fix \(\ell_N=N^{-2/d}\), \(q=1-s/d\), and put
\[
 V_N(t)=\mathcal E_{\ell_N}(X_t)+\mathcal S_{2\ell_N}(X_t)+c_{2\ell_N}\ge0.
\]
For each actual finite-\(N\) path this is a finite continuous function: all deleted separations stay bounded away from zero and the retained Fourier series is uniformly absolutely convergent. Equations (7)–(9) give
\[
 \sup_{t\le T}\mathbb EV_N(t)\le CN^{-q},\qquad
 |P_N[J^f](X_t)|\le C\|f\|_{\mathcal A_R}V_N(t)                  \tag{10}
\]
simultaneously in \(f\). This is stronger than separate fixed-test expectation estimates and is what permits the Hilbert sum.

## 4. Actual Hilbert paths and the source error

In the real basis the frozen Hilbert norm is exactly \(\sum_lw_lu_l^2\): the cosine/sine pair converts to the two complex coefficients by an orthogonal real change of coordinates, with no extra factor two. For any fixed real exponent \(p\), lattice shells \(2^n\le|k|<2^{n+1}\) contain at most \(C_d2^{dn}\) points. Consequently
\[
 S_R(K):=\sum_{|k|>K}(1+|k|^2)^{-r}(1+|k|)^{2R}<\infty,
 \qquad S_R(K)\longrightarrow0.                                  \tag{11}
\]
This is the geometric series with exponent \(d+2R-2r<0\), exactly (1). For \(K\ge1\), it is bounded by \(C K^{d+2R-2r}\). The same argument proves summability with \(R\) replaced by one or zero. At the endpoint equality the shell exponent would be zero; the present proof does not include it.

The map \(x\mapsto\delta_x\) is continuous into \(H^{-r}\), already for \(r>d/2\): each complex Fourier coefficient is continuous and its squared difference is at most four, an absolutely summable weighted majorant. Therefore actual particle path continuity gives \(Z_N\in\mathcal X\) directly. Its Fourier coordinates are jointly measurable. Alternatively finite projections converge uniformly along a continuous path, proving measurability as a path-valued random variable. The space \(\mathcal X\) is complete and separable: completeness follows by uniform limits, and finite Fourier sums with rational coefficients and piecewise-linear grids at rational multiples of \(T\) give a countable dense family. On null exceptional sets processes can be set to zero.

Let \(L_{N,l}=D_l+\nu_Na_l\), and let \(S_N(t)\) be the diagonal contraction with multipliers \(e^{-L_{N,l}t}\). For each \(u\in H^{-r}_0\), dominated convergence in its weighted squared Fourier sum proves strong continuity of this semigroup. Define the source coefficients \(F_{N,l}(u)=P_N[J^{e_l}](X_u)\). Since \(\|e_l\|_{\mathcal A_R}=\sqrt2(1+|k_l|)^R\), (10)–(11) show that their series defines an \(H^{-r}_0\)-valued continuous function on each realized path. In detail, coefficient continuity and the uniform bound \(\sup_{u\le T}V_N(u)<\infty\) make its finite Fourier sums uniformly Cauchy in time in the Hilbert norm. Thus it is strongly measurable and Bochner integrable.

For every smooth real \(f\), its rapidly decaying basis coefficients make \(\sum_l f_lF_{N,l}(u)\) absolutely convergent. Approximation in \(\mathcal A_R\) and (9) identify this pairing with the original \(P_N[J^f](X_u)\). The Hilbert source construction therefore preserves the original statistic for every smooth test, not just the chosen basis.

Define
\[
 E_N(t)=\sigma_N\int_0^t S_N(t-u)F_N(u)du.                         \tag{12}
\]
It is a genuine Bochner integral. Either strong semigroup continuity and dominated convergence, or the following uniform Fourier-tail bound, proves continuity in \(t\). Its coefficient is exactly \(\sigma_N\int_0^t e^{-L_{N,l}(t-u)}P_N[J^{e_l}](X_u)du\). By (10), pathwise
\[
 \|(1-\Pi_K)E_N\|_{\mathcal X}
 \le C\sigma_N S_R(K)^{1/2}\int_0^T V_N(u)du.                    \tag{13}
\]
Use the finite sum inequality first; the nonnegative weighted squared tails and (11) pass it to the limit. In particular the partial sums converge uniformly almost surely, without assigning an uncountable collection of exceptional sets. Tonelli now gives
\[
 \boxed{\mathbb E\|(1-\Pi_K)E_N\|_{\mathcal X}
 \le C\sqrt{b_N}N^{s/d-1/2}S_R(K)^{1/2}.}                         \tag{14}
\]
At \(K=0\) this is the required source interface. It uses only a first moment of \(V_N\), never its square. Since \(s/d-1/2<0\), it also gives tails tending to zero uniformly in \(N\) and admitted noise choices. All constants depend only on \(d,s,T,r\) and kernel data, with admissible dependence on \(\nu_*\); none depends on \(N,K\) or the selected diffusivity. At \(T=0\), (12) vanishes and all these assertions remain valid.

## 5. Genuine modal identity and the linear Hilbert path

For a smooth test \(f\), integrability of \(K\), its oddness and distributional integration by parts against the smooth test give
\[
 j_f(x):=\int J^f(x,y)dy=-\int K(x-y)\cdot\nabla f(y)dy
 =-\int f(x+z)D(dz)=:\mathcal Rf(x),\quad \int j_f=\iint J^f=0.     \tag{15}
\]
The multiplier of \(\mathcal R\) is \(-D_k\); at Coulomb it is \(-c_d(f-\int f)\). Both atom and compensation in (5) remain. Direct symmetrization of the ordered deleted force gives
\[
 \frac1{N^2}\sum_{i\ne j}K(X_i-X_j)\cdot\nabla f(X_i)
 =\frac1{2N^2}\sum_{i\ne j}J^f(X_i,X_j)
 =P_N[J^f]+\eta_N[\mathcal Rf].                                  \tag{16}
\]
Thus (8) retains the original row and double background contractions, the latter evaluated as zero only after (15). There is no singular self value and no missing force label.

Apply ordinary Itô to the globally smooth empirical observable, localized on collision-excluded energy sublevels. The independent-noise correction is exactly \(\nu_N\eta_N[\Delta f]\). Since \(|J^f|\le C_f(1+\operatorname{dist}^{-s})\), (6) makes its symmetrized drift integrable in probability times time. The row and time derivatives are bounded. Collision stops eventually exceed the horizon almost surely. Dominated convergence passes the drift and endpoints; bounded gradients and Itô isometry pass the stochastic integrals in \(L^2\). This proves a genuine unstopped identity, rather than a formal singular Itô calculation.

For every basis function let
\[
 z_{N,l}(t)=\sigma_N\eta_N(t)[e_l],\qquad
 U_{N,l}(t)=\sqrt{\frac{2\nu_Nb_N}{N}}
       \sum_i\int_0^t\nabla e_l(X_i(u))\cdot dW_i(u).
\]
The exact scalar equation is
\[
 dz_{N,l}=-L_{N,l}z_{N,l}\,dt+\sigma_NF_{N,l}\,dt+dU_{N,l}.         \tag{17}
\]
Its cross bracket, for any two smooth tests, is \(2\nu_Nb_N\int\eta_N[\nabla f\cdot\nabla h]dt\); no deleted-pair factor belongs to this one-body noise. Every \(U_{N,l}\) is a true square-integrable martingale, with
\[
 \langle U_{N,l}\rangle_T=2\nu_Nb_N\int_0^T\eta_N[|\nabla e_l|^2]du,
 \quad \mathbb E|U_{N,l}(T)|^2=2\nu_Nb_Na_lT.                     \tag{18}
\]
The last equality uses exact Haar one-body marginals, not independence. Pointwise, the bracket density is at most \(4\nu_Nb_Na_l\), since \(\|\nabla e_l\|_\infty^2\le2a_l\).

Variation of constants in (17) gives the coefficient decomposition
\[
 z_{N,l}(t)=I_{N,l}(t)+M_{N,l}(t)+E_{N,l}(t),
 \quad I_{N,l}(t)=e^{-L_{N,l}t}z_{N,l}(0),
 \quad M_{N,l}(t)=\int_0^t e^{-L_{N,l}(t-u)}dU_{N,l}(u).           \tag{19}
\]
No initial/thermal independence is asserted for the particle system. Integration by parts with a deterministic smooth kernel gives the continuous version
\[
 M_{N,l}(t)=U_{N,l}(t)-L_{N,l}\int_0^t e^{-L_{N,l}(t-u)}U_{N,l}(u)du,
 \qquad \sup_{t\le T}|M_{N,l}(t)|\le2\sup_{t\le T}|U_{N,l}(t)|.    \tag{20}
\]
The kernel integral has mass \(1-e^{-L_{N,l}t}\le1\). This bound has no factor growing with \(L_{N,l}\). It does not call the moving-terminal stochastic convolution a martingale.

For completeness the square maximal inequality used here follows from a finite time grid: first crossing of level \(\lambda\) and conditional Jensen give \(\lambda\mathbb P(U^*\ge\lambda)\le\mathbb E[|U(T)|1_{\{U^*\ge\lambda\}}]\). Integrating to a truncation level and applying Cauchy–Schwarz gives \(\mathbb E(U^*\wedge B)^2\le4\mathbb E|U(T)|^2\). Increasing dyadic grids, continuity and monotone convergence remove both truncations. Hence (18)–(20) imply
\[
 \mathbb E\sup_t|M_{N,l}(t)|^2\le32\nu_Nb_Na_lT\le32a_lT.         \tag{21}
\]
At preparation, iid Haar and the orthonormal zero-mean basis give \(\mathbb E|z_{N,l}(0)|^2=b_N\). Damping is nonnegative, so \(\mathbb E\sup_t|I_{N,l}(t)|^2=b_N\). These estimates hold for each individual mode; no cross-mode independence is needed in any Hilbert norm sum.

By (11) with exponent one, Tonelli gives
\[
 \mathbb E\sum_lw_l\sup_t|M_{N,l}(t)|^2<\infty.
\]
Thus that nonnegative series is finite almost surely. On the resulting common event, finite Fourier sums are uniformly Cauchy in \(H^{-r}\), since the squared norm of every tail is bounded by the corresponding tail of this scalar series. Their limit is a continuous Hilbert path. The same reasoning applies to \(I_N\), also identified directly as \(S_N(t)Z_N(0)\). Define \(Y_N=I_N+M_N\). Passing finite sums by Tonelli yields
\[
 \begin{split}
 \mathbb E\|(1-\Pi_K)Y_N\|_{\mathcal X}^2
 &\le\sum_{|k_l|>K}w_l\,[2b_N+64\nu_Nb_Na_lT]\\
 &\le C_T\sum_{|k|>K}(1+|k|^2)^{-r}(1+|k|^2).
 \end{split}                                                    \tag{22}
\]
The real basis has exactly two coordinates for each opposite pair, matching exactly the complex sum in (3). This proves the second required interface with a constant independent of selected noise, \(N\) and \(K\).

The localized identities can first be taken on a single probability-one event for countably many modes and rational terminal times. All four Hilbert paths in (19) have now been constructed continuously, so those identities extend to every time; equality of all Fourier coefficients gives equality in the Hilbert space. This proves the genuine continuous decomposition \(Z_N=Y_N+E_N\). There is no unproved exchange of an infinite stochastic sum with an integral. Constant modes are identically zero in every term.

## 6. Existence and covariance of the Gaussian Hilbert path

Construct the independent normals and Brownian motions in (2) on their countable product probability space. Apply (20) to Brownian motion in each mode. Its square maximal bound is at most \(4T\), so
\[
 \mathbb E\sup_{t\le T}|G_l(t)|^2\le2\bar b+64\bar\nu\bar b\,a_lT
 \le C_T(1+|k_l|^2).                                            \tag{23}
\]
Together with the summable weights, Tonelli proves almost-sure uniform Hilbert convergence of the full Fourier series, and convergence of its tails in \(L^2\) of the uniform norm. Every partial sum is continuous, so the limit \(G\) is a continuous \(H^{-r}_0\)-valued random variable in \(\mathcal X\). These conclusions are about the full series, not only each fixed test. The same proof gives its analogue of (22).

The process is centered Gaussian. One can verify even Gaussianity as a Banach-valued random variable: each finite Fourier sum is Gaussian under every continuous linear functional on \(\mathcal X\). To justify this, approximate its finitely many continuous coefficient paths by time-grid interpolation. Each interpolated functional is a linear combination of finitely many Gaussian evaluations. The approximations converge in \(L^2\), using continuity and the integrable supremum in (23). Limits of centered real Gaussians in \(L^2\) are centered Gaussian, by their variances and characteristic functions. Finally apply the same argument to the Fourier partial sums, which converge in \(L^2(\mathcal X)\). This also proves the asserted finite-test interpretation, including degenerate laws.

Independence and Itô isometry give exactly
\[
 \mathbb E G_l(t)G_l(u)=\bar b\left[e^{-(t+u)L_l}
 +2\bar\nu a_l\int_0^{t\wedge u}e^{-(t+u-2v)L_l}dv\right]
 =\bar b\left[\frac{D_l}{L_l}e^{-(t+u)L_l}
 +\frac{\bar\nu a_l}{L_l}e^{-|t-u|L_l}\right].                    \tag{24}
\]
There is no zero denominator: \(D_l>0\) for every nonzero mode, also at zero noise. Its absolute value is at most \(\bar b\). For smooth tests, \(\sum_l|h_{i,l}h_{j,l}|<\infty\) by Cauchy–Schwarz in \(L^2(dx)\), so covariance sums may be passed absolutely. Pairing with a smooth test is also a continuous functional on \(H^{-r}\), since the test belongs to \(H^r\). Summing (24) gives the frozen real-basis formula and, on combining sine/cosine pairs, exactly the THM040/042 complex Fourier formula, with no additional factor two. Equivalently it is the initial Gram covariance plus the thermal time-space gradient Gram covariance.

At \(\bar\nu=0\) the thermal part vanishes directly; initial normals still give a continuous path. At \(T=0\), the series is the weighted white-noise initial field with variance \(\bar b\). A constant test has zero pairing, and any linear dependence or other degeneracy is allowed. No stationarity is assumed: the initial term has the sum of the two times, whereas only the thermal term has their difference.

## 7. Finite-mode tightness and identification, with no dependence shortcut

This section records the complete finite-observable mechanism needed for the remaining infinite-dimensional argument. It agrees with the full supplied R18/R20 sources; the cards alone are not being used as proofs.

Fix a finite collection of modes or smooth tests. Every spatial Fourier seminorm of \(Q_t^\nu h\), where the multiplier is \(e^{-t(D_k+\nu a_k)}\), is bounded by that of \(h\). Since \(D_k\le4\pi^2c_{d,s}\) and \(\nu\le\nu_*\), its time derivative loses at most two powers of frequency. Thus \(Q_t^\nu h-Q_u^\nu h\) and its needed gradient seminorms are bounded by \(C_h|t-u|\), uniformly in admitted noise.

For a zero-mean iid summand \(v\), elementary label partitions give
\[
 \mathbb E\left(\frac{\sqrt b}{\sqrt N}\sum_iv(X_i(0))\right)^4
 =b^2\left[\frac{\int v^4}{N}+3\frac{N-1}{N}(\int v^2)^2\right].   \tag{25}
\]
It follows that initial-process fourth increments are at most \(C|t-u|^4\), with uniformly bounded fourth initial moments. The convolution increment at \(t\ge u\) has two stochastic-integrand pieces: \(\nabla(Q_{t-v}^\nu-Q_{u-v}^\nu)h\) for \(v\le u\), and \(\nabla Q_{t-v}^\nu h\) for \(u<v\le t\). They are bounded respectively by \(C(t-u)\) and \(C\). Its bracket density is bounded by \(C[(t-u)^2 1_{[0,u]}+1_{(u,t]}]\), whose integral is at most \(C_T(t-u)\). The earlier-noise interval has not been dropped.

For a stochastic-integral martingale with deterministic bracket-density bound \(w(v)\), stopping and Itô on its fourth power give \(\mathbb EU(T)^4\le6\int_0^Tw(v)\int_0^vw(a)dadv=3(\int_0^Tw)^2\). The stopped isometry bounds the interior second moment; Fatou removes the stop. This argument requires no conditional Gaussianity of adapted integrands. Hence for every fixed finite projection,
\[
 \sup_N\mathbb E|\Pi_KY_N(0)|^4\le C_K,
 \quad \mathbb E|\Pi_KY_N(t)-\Pi_KY_N(u)|^4\le C_K|t-u|^2.          \tag{26}
\]

For \(T>0\), rescale time to \([0,1]\). Markov and a union bound over the \(2^n\) adjacent dyadic intervals show that increments exceed \(A2^{-\gamma n}\) with probability at most \(C_KA^{-4}2^{-(1-4\gamma)n}\), for any \(0<\gamma<1/4\). Sum over levels and add the initial fourth-moment tail. Dyadic chaining and continuity then give, except on probability \(C_{K,\gamma}A^{-4}\), a common \(\gamma\)-Hölder bound and initial bound. Such a closed set is compact in finite-dimensional uniform path norm: finite time grids and finite nets for their bounded values prove total boundedness, and completeness gives compactness. This proves uniform tightness of \(\Pi_KY_N\).

Transfer this to \(\Pi_KZ_N\) using the vanishing expected uniform error (14), without treating a fixed-radius neighborhood of a compact set as compact. For a summable probability budget \(p_j\) and tolerances \(e_j\downarrow0\), choose \(N_j\) so that \(2\|\Pi_KE_N\|\le e_j/2\) except on probability \(p_j/2\), for all \(N\ge N_j\). The Hölder compactness just proved chooses \(\delta_j\) with the modulus of \(\Pi_KY_N\) at most \(e_j/2\) except on probability \(p_j/2\), uniformly in \(N\). For the finitely many \(N<N_j\), actual path continuity permits further shrinking \(\delta_j\) so their actual moduli exceed \(e_j\) with probability less than \(p_j\). Make \(\delta_j\downarrow0\). The actual paths thus satisfy every chosen modulus bound with probability at least \(1-\sum_jp_j\). Their initial values have the uniform fourth-moment bound since \(E_N(0)=M_N(0)=0\). These closed initial-and-modulus constraints define a compact finite-dimensional path set by the same net argument. Tightness here is for every fixed admitted sequence; these compact sets may depend on that sequence. The quantitative constants in (14), (22) do not.

To identify finite tuples, the required actual-law Fourier estimate follows directly from (4), (6). Truncate the heat integral at \(\ell=N^{-2/d}\). Its positive weights \(\widetilde a_\ell(k)\) and exact self subtraction give
\[
 H_N\ge\frac N2\sum_{k\ne0}\widetilde a_\ell(k)|\widehat\eta_N(k)|^2
 -\frac12g^{>\ell}(0)-\frac{N-1}{2\alpha}A\ell^\alpha.
\]
The two errors are \(O(N^{s/d})\). For \(|k|\le N^{1/d}\), integrate its weight over \([|k|^{-2},2|k|^{-2}]\) to obtain \(\widetilde a_\ell(k)\ge c|k|^{s-d}\). For larger modes use \(|\widehat\eta_N|\le1\). Thus, for deterministic smooth \(\psi\),
\[
 \mathbb E|\widehat\eta_N(t,k)|^2\le\min(1,CN^{-q}|k|^{d-s}),\quad
 \mathbb E|(\eta_N-dx)[\psi]|\le CN^{-q/2}\|\psi\|_{\mathcal A_\alpha}.
                                                                    \tag{27}
\]
Absolute Fourier convergence and Cauchy–Schwarz in probability justify the second inequality. It is uniform for deterministic families with the displayed seminorm bounded. Products of the needed backward gradients have that property, by convolution of absolutely summable Fourier coefficients.

For fixed terminal tuples \((t_j,h_j)\), let \(f_{N,j}(v)=Q_{t_j-v}^{\nu_N}h_j\), stopped at \(t_j\). Equation (16) cancels the drift in their backward equations. Their integration-time martingales have exact cross bracket
\[
 2\nu_Nb_N\int_0^{t_i\wedge t_j}\eta_N(v)
       [\nabla f_{N,i}(v)\cdot\nabla f_{N,j}(v)]dv.                \tag{28}
\]
Equation (27) shows that (28) differs from its deterministic Haar integral in \(L^1\) by at most \(CN^{-q/2}\). The Fourier mean-value estimate
\[
 \|(Q_t^{\nu_N}-Q_t^{\bar\nu})h\|_{\mathcal A_p}
 \le4\pi^2t|\nu_N-\bar\nu|\|h\|_{\mathcal A_{p+2}}
\]
and the Lipschitz function \(\nu b(\nu)=\min(\nu,1)\) pass that integral to the thermal Gram matrix \(B\) of (24), without a rate assumption. The scalar bracket of each fixed linear combination is bounded by a deterministic constant \(K\) and converges to its deterministic quadratic form \(v\) in \(L^1\).

The initial normalized sums use triangular tests \(\sqrt{b_N}(Q_{t_j}^{\nu_N}h_j-\int h_j)\). Replace them with the fixed limiting tests. Their difference has zero Haar mean and \(L^2\) norm \(O(|\nu_N-\bar\nu|)\), since \(\sqrt{b}\) is Lipschitz also across one. Initial independence makes the variance of the normalized difference sum exactly that squared norm. There is no \(\sqrt N\) loss. For the fixed bounded vector summand \(V\), the Taylor formula is \(\mathbb Ee^{iu\cdot V/\sqrt N}=1-u^TAu/(2N)+O_u(N^{-3/2})\). Raising to the \(N\)-th power gives the initial Gaussian characteristic function with covariance \(A\).

Initial and thermal vectors may be dependent at finite \(N\). For the scalar martingale \(U_N\), Itô gives the true complex martingale \(\exp(iU_N+\langle U_N\rangle/2)\); its modulus and stochastic-integral square norm are bounded by the deterministic bracket bound. Its conditional mean given the full initial sigma field is one. For any bounded initial-measurable \(W_N\), \(|W_N|\le1\), replacing its bracket by \(v\) gives
\[
 |\mathbb E(W_Ne^{iU_N(T)})-e^{-v/2}\mathbb EW_N|
 \le\tfrac12e^{K/2}\mathbb E|\langle U_N\rangle_T-v|\longrightarrow0.  \tag{29}
\]
Use the exponential of the initial vector as the weight. The source tends to zero in \(L^1\) by (14). This proves convergence of every joint characteristic function to the centered Gaussian with covariance \(A+B\), exactly the evaluations of (2).

For a complete weak passage at these finite tuples, the linear vector has uniformly bounded second moments and hence uniform tails. Convolve it and the target with an independent Gaussian of covariance \(\varepsilon I\). Elementary Gaussian Fourier inversion and the integrable multiplier \(e^{-\varepsilon|u|^2/2}\) give uniform convergence of convolved densities by dominated convergence. On a large ball integrate bounded Lipschitz tests using that convergence; outside use uniform second-moment tails. Coupling with the added Gaussian changes Lipschitz expectations by \(O(\sqrt\varepsilon)\). First send \(N\to\infty\), then \(\varepsilon\downarrow0\); the source error transfers this to the actual vector and preserves its tails. Uniform Lipschitz approximation on a compact ball extends it to bounded continuous tests. This includes singular covariance matrices.

The corresponding finite projection of \(G\) has continuous paths and the same fourth-increment bound (26), either from its deterministic stochastic integrands or the Gaussian fourth moment. Its finite-dimensional path law is tight by the dyadic construction. Piecewise-linear time interpolation depends on a finite evaluation tuple and approaches each path with error bounded by its modulus. Uniform compact-set moduli for the actual and limiting laws and the finite-tuple limit therefore prove convergence of bounded Lipschitz path expectations; compact-set Lipschitz approximation then gives all bounded continuous ones. Thus
\[
 \Pi_KZ_N\ \Longrightarrow\ \Pi_KG
 \quad\hbox{in }C([0,T],\operatorname{Ran}\Pi_K)                 \tag{30}
\]
for every fixed \(K\). At \(T=0\), the interpolation and rescaling steps are omitted; the initial iid finite-vector argument proves (30) directly.

## 8. Actual compact sets in the full Hilbert path space

The additional spatial tail is indispensable: (30) alone would not imply this section. Combining (14), (22), Cauchy–Schwarz and \(N^{s/d-1/2}\le1\) gives
\[
 \sup_{N\ge2}\mathbb E\|(1-\Pi_K)Z_N\|_{\mathcal X}
 \le C\left[S_1(K)^{1/2}+S_R(K)^{1/2}\right]\longrightarrow0,       \tag{31}
\]
where \(S_1\) can equivalently use \(1+|k|^2\) instead of \((1+|k|)^2\), at a fixed factor. The Gaussian tail has the same conclusion by (23). This estimate concerns the supremum over the whole time interval; it does not exchange expectation and time supremum incorrectly.

Here is an explicit compactness construction in \(\mathcal X\). Given \(\varepsilon>0\), select increasing integer cutoffs \(K_j\) so that (31) and Markov give
\[
 \sup_N\mathbb P(\|(1-\Pi_{K_j})Z_N\|_{\mathcal X}>2^{-j})
 <\varepsilon2^{-j-2}.
\]
Finite-mode tightness supplies compact sets \(A_j\) in \(C([0,T],\operatorname{Ran}\Pi_{K_j})\) with \(\sup_N\mathbb P(\Pi_{K_j}Z_N\notin A_j)<\varepsilon2^{-j-2}\). Consider the set
\[
 \mathcal K=\{z\in\mathcal X:\ \Pi_{K_j}z\in A_j,
       \ \|(1-\Pi_{K_j})z\|_{\mathcal X}\le2^{-j}\text{ for every }j\ge1\}.
                                                                    \tag{32}
\]
Every defining constraint is closed. Given a desired net radius \(\delta>0\), choose \(j\) with \(2^{-j}<\delta/2\) and a finite \(\delta/2\)-net for \(A_j\). That net is a finite \(\delta\)-net for \(\mathcal K\), since every full path is within \(2^{-j}\) of its projection. Thus \(\mathcal K\) is totally bounded and closed in a complete space, hence compact. A union bound gives \(\inf_N\mathbb P(Z_N\in\mathcal K)\ge1-\varepsilon\), with slack in the chosen budget. This proves actual tightness, including all small \(N\). No closed Hilbert ball or fixed-radius neighborhood of a compact path set has been called compact.

The same construction with (23) and tight finite Gaussian projections gives compact sets of arbitrarily high probability for \(G\). It also works at \(T=0\), when the finite projected spaces are Euclidean. Projection tail constraints control spatial compactness in both cases. A common compact set for the two families is obtained by taking the union of their two compact sets.

## 9. Full weak passage and every edge of the frozen claim

For a bounded Lipschitz functional \(F\) on \(\mathcal X\), any \(e>0\) gives
\[
 |\mathbb EF(Z_N)-\mathbb EF(\Pi_KZ_N)|
 \le\operatorname{Lip}(F)e+2\|F\|_\infty
       \mathbb P(\|(1-\Pi_K)Z_N\|_{\mathcal X}>e).                \tag{33}
\]
The probability tends uniformly to zero as \(K\to\infty\) by (31); the same holds for \(G\). At fixed \(K\), (30) applies to the restricted functional and identifies its limit. First take \(N\to\infty\), then \(K\to\infty\) and \(e\downarrow0\). This proves convergence against every bounded Lipschitz functional on the full path space.

To obtain exactly bounded-continuous weak convergence, let \(F\) be bounded continuous and take a common compact set \(\mathcal K\) of arbitrarily high actual and target probability, from Section 8. The restriction of \(F\) to \(\mathcal K\) is uniformly continuous. If \(|F|\le B\), then the functions
\[
 F_L(x)=\max(-B,\min(B,\inf_{y\in\mathcal K}[F(y)+L\|x-y\|_{\mathcal X}]))
\]
are globally bounded Lipschitz and approximate \(F\) uniformly on \(\mathcal K\) as \(L\to\infty\). To verify approximation, split the infimum at a uniform-continuity radius \(\delta\). Nearby values differ by at most the corresponding modulus; distant values have penalty \(L\delta\), which eventually exceeds \(2B\). Outside \(\mathcal K\) the expectation error is bounded by \(2B\) times its probability. Applying the proved Lipschitz convergence, then sending approximation and probability errors to zero, proves
\[
 Z_N\Longrightarrow G\quad\hbox{in }C([0,T],H^{-r}),
\]
against every bounded continuous functional of the stated uniform Hilbert norm. This argument requires no unproved subsequence or probability compactness theorem.

All zero-time, zero-noise and constant cases were kept in the actual identities. If \(\nu_*=0\), the dynamics are the actual deterministic gradient flow and every \(U_N,M_N\) vanishes; random initial data still give the Gaussian limit. If only \(\bar\nu=0\), (29) controls the full admitted sequence and the limiting thermal covariance vanishes directly, with no convergence-rate hypothesis. The normalization is continuous across \(\nu=1\). Repeated times, test dependence and degenerate covariance need no inverse covariance matrix. Coulomb within the simultaneous exponent restrictions includes three-dimensional Coulomb; four-dimensional Coulomb has \(s=d/2\) and is excluded. No logarithmic substitution, larger exponent, arbitrary preparation, inhomogeneous background, unbounded-noise theorem, higher hierarchy or full campaign resolution is asserted. The old-floor, full microscopic-subcritical and positive finite critical conditions remain distinct; none was interchanged in this proof.

## 10. Independent falsification route and analytic failure controls

The construction uses the source envelope and modal maximal bounds. A different route tries to falsify the Hilbert upgrade through spatial escape, endpoint divergence, and moment/supremum errors. These are counterexamples to invalid inferences, not substituted particle law classes.

1. **Coordinate convergence without tightness.** In a Hilbert basis with weight \(w_n\), the deterministic constant paths \(v_n=w_n^{-1/2}e_n\) have norm one and mutual distance \(\sqrt2\). Every fixed finite projection is eventually zero. Their Dirac laws are not tight: a compact set is totally bounded and can contain only finitely many points separated by \(\sqrt2\), whereas probability greater than one half for every Dirac law would require all of them. Thus finite-mode convergence alone cannot prove the frozen claim. The actual estimate (31) excludes this escape.

2. **The strict source summability threshold.** A dyadic shell model with \(2^{dn}\) coefficients of size \(2^{Rn}\) and Hilbert weight \(2^{-2rn}\) contributes \(2^{(d+2R-2r)n}\) to its squared norm. Under the frozen strict inequality it is a convergent geometric series. At equality every shell contributes one and partial sums grow without bound. This challenges a hidden endpoint inclusion or a missing dimension factor in the Hilbert sum; it does not claim the actual theorem fails at a sharper topology. Equation (11) supplies the genuine lattice estimate.

3. **A first source moment does not provide a square moment.** Let \(A=2^n\) with probability \(3/4^n\), \(n\ge1\). This is a probability law with \(\mathbb EA=3\) and \(\mathbb EA^2=\infty\). A Hilbert source of the form \(Av\) therefore has the required first moment for each fixed \(v\), but need not have a second moment. Equations (13)–(14) use the common random envelope linearly after taking the Hilbert norm. They never sum expected squared source coefficients. The linear-process tail (22) has its own martingale second-moment proof.

4. **Supremum is not additive across modes.** Two orthogonal coordinates with disjoint continuous unit peaks satisfy \(\sup_t\sum_l|u_l(t)|^2=1\) while \(\sum_l\sup_t|u_l(t)|^2=2\). The needed direction is the inequality \(\sup\sum\le\sum\sup\). Equations (21)–(23) use that direction explicitly, and do not infer a supremum estimate from one-time variances.

5. **Convolution is not an undamped martingale.** With a single damped mode and a drive having nonzero history before time \(u\), the convolution difference at \(t>u\) includes \((e^{-L(t-u)}-1)M(u)\). It cannot be omitted. The integration-by-parts formula (20) has a uniform factor two because its nonnegative kernel mass is at most one, even for large damping. It supplies the frequency-square tail in the frozen claim rather than a frequency-fourth-power loss from differentiating terminal time.

6. **Real Fourier and Brownian factors.** For a sine/cosine pair, the pointwise sum of squared gradients is \(2a_k\), while each individual Haar gradient norm squared is \(a_k\). Both real basis coordinates together correspond to exactly the two complex frequencies. The particle Brownian bracket has coefficient \(2\nu_Nb_N/N\) before summing labels, so its Haar expectation for one real mode is \(2\nu_Nb_Na_k\), without \((N-1)/N\). These identities test the exact target covariance and tail bookkeeping independently of the source estimate.

No admitted counterexample to any component of the frozen conjunction survived the analytic checks. The strict regularity assumption suffices; its optimality was not investigated or claimed.

## 11. Whole-claim dispositions and bounded handoff

The independently written standard-library program `round022_blind_diagnostic.py` was executed under Python 3.9.6. Its actual result is **PASS: 59,033 exact assertions in 27 categories; 15 nonvacuous mutations rejected**. It uses rational and exact exponential-polynomial arithmetic, with no random samples or floating-point tolerance. The results record every altered coefficient or invalid inference and a concrete witness. The tested mechanisms include source-shell exponents, Hilbert escape, first-versus-second moments, supremum direction, damped convolution, literal Brownian label brackets, real/complex Fourier conversion and initial-plus-thermal covariance. These finite checks do not certify singular passages, infinite sums, tightness or weak convergence; Sections 2–9 supply the analytic argument. The program digest and complete executed output are in the packet.

| Frozen conjunct or negation | Blind reconstruction disposition and decisive lines |
|---|---|
| Actual singular path and exact first-marginal Haar centering | Reconstructed from full conditional sources with actual-law mechanisms, Section 2. No arbitrary-law transfer. |
| Actual continuous \(H^{-r}\)-valued paths and measurable path interpretation | Established in Sections 4–5 by Dirac-map continuity and uniform Fourier limits. |
| Continuous decomposition and all original contractions | Established by (8), (15)–(20) and the countable-event argument. |
| Required uniform expected source norm | Established by simultaneous (10), exact threshold (11), and (14) at \(K=0\). No source square. |
| Required uniform Fourier tail for \(Y_N\) | Established by the true modal martingale (18), integration by parts (20) and (22). |
| Full Gaussian-series existence, continuity and centering | Established by (23), Tonelli, uniform Hilbert convergence and the Gaussian functional argument. |
| Exact initial-plus-thermal covariance | Established in (24), with absolutely convergent testing and exact real/complex conversion. |
| Actual path tightness | Established in (26), finite-mode error transfer, (31)–(32). Spatial escape and compact-neighborhood shortcuts are excluded. |
| Full bounded-continuous weak convergence | Established by finite-tuple dependence control (27)–(29), finite-path interpolation (30), and full-space passage (33). |
| All specified zero/constant/degenerate cases | Retained explicitly throughout and collected in Section 9. |
| Entire exact negation | Excluded by this complete implication from the specified full-source premises. No unconditional source-gate certification is assigned here. |
| Whole THM044/PO031 | PASS as a fresh whole-claim blind reconstruction, conditional on the unchanged complete-source premises; root comparison, source-gate matching and separate hostile review remain. |

This report was constructed without reading a root R22 proof mechanism or another R22 audit. The authorized R20 complete proof is disclosed exposure, as required; independence here is from the new construction under audit, not from authorized earlier source proofs. All mathematically used earlier hypotheses and constants were mapped above. No source merely named in those histories supplies a premise. This report does not change a canonical ledger, certify older reports' independent audits, commit, push or publish.

The accompanying packet contains this entire report, all sixteen exact input copies, the complete source/exposure record, a fresh standard-library diagnostic with nonvacuous mutation witnesses, actual results, README and byte manifests. Its safe verifier checks every archive member and byte without extracting. Issued output is made read-only. Any correction after issuance must be a new artifact. Root's next action is to compare the complete reconstruction with the root construction, match current prior source gates and obtain the separate hostile disposition before any canonical promotion. This is the required bounded handoff, not completion of the research campaign.
