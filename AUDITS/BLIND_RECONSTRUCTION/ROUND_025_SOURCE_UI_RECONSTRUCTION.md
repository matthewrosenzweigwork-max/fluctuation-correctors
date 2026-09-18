# AUD069 / TASK108 — isolated reconstruction of all of THM048 and THM049

Issued 2026-09-18 UTC from the isolated branch `codex/hocf-r025-source-ui-blind`, provisioned base `3efdbb96e7b94529b280234e83eb36f5fca3ef36`. The task requests a fresh Astra Max context. This report is an independent reconstruction, not the constructor's self-check or the root's certification. The assigned worker did not inspect current constructor work or other current audits. Earlier reports keep their historical statuses. Exact inputs, exposure, diagnostics, limitations and integrity evidence accompany this report.

**Whole THM048 verdict: RECONSTRUCTED — every clause A/B follows in the frozen scope. Whole THM049 verdict: RECONSTRUCTED — every clause A/B/C follows in the frozen scope. Joint verdict: RECONSTRUCTED, pending the root's source/dependence comparison and a separately assigned hostile review.** Neither theorem proves source decay. The cancellation criterion and the original THM046 limit remain open.

The decisive new probabilistic point is to truncate *initial pair values*, rather than square the singular initial energy. On the initial rare event the smooth endpoint identity gives the needed estimate, conditionally on the initial configuration. The modal identity is then an exact second-moment and current/initial-moment calculation; it never deletes a source/noise correlation.

## 1. Frozen assertion, exact negation, source boundary

The unit torus is \(\mathbb T^4=\mathbb R^4/\mathbb Z^4\), with Haar mass one, characters \(e_k(x)=e^{2\pi i k\cdot x}\), and
\[
 \widehat g(0)=0,\quad \widehat g(k)=|k|^{-2}\ (k\ne0),\quad
 c=4\pi^2,\quad K=-\nabla g.
 \tag{1.1}
\]
For each integer \(N\ge2\), \(0<\beta_N<\infty\), \(\nu_N=\beta_N^{-1}\), use the actual singular gradient solution
\[
 dX_i=B_i(X)dt+\sqrt{2\nu_N}\,dW_i,
 \qquad B_i=N^{-1}\sum_{j\ne i}K(X_i-X_j),
 \tag{1.2}
\]
from independent Haar positions independent of the independent standard Brownian drivers. Initial independence is used only where stated below. Positive-time laws are exchangeable and translation invariant, not presumed product laws.

Fix a real smooth \(h\) and a finite \(T\ge0\). The complete backward test preserves constants and, for \(k\ne0\), has multiplier
\[
 \widehat f_t(k)=e^{-(T-t)(c+c\nu_N|k|^2)}\widehat h(k).
 \tag{1.3}
\]
Let \(\eta_N=N^{-1}\sum_i\delta_{X_i}\), \(\rho=\eta_N-dx\), and, off the pair diagonal,
\[
 J^f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y)),
\]
\[
 P_N[J]=\frac1{2N^2}\sum_{i\ne j}J(X_i,X_j)
       -\frac1N\sum_i\int J(X_i,y)dy+\frac12\iint J(x,y)dxdy.
 \tag{1.4}
\]
The labels are ordered and distinct, with denominator \(N^2\). There is no assigned singular diagonal. Set
\[
 S_N=\sqrt N\int_0^TP_N[J^{f_t}](X_t)dt,\qquad
 D_N=\sqrt N\{\rho_T[h]-\rho_0[f_0]\}.
 \tag{1.5}
\]
The critical assumption is exactly \(\lambda_N=\beta_NN^{-1/2}\to\lambda\in(0,\infty)\). For any fixed eventual interval \(0<\lambda_-\le\lambda_N\le\lambda_+<\infty\), THM048 asserts finite-N square integrability; constants \(A,C<\infty\), depending only on \(h,T,g\) and those interval bounds, with
\[
 \mathbb E (|S_N|-A)_+^2\le C(1+\log N)/N
 \tag{1.6}
\]
on that tail; uniform integrability of \(\{|S_N|^2\}\) and \(\{|D_N|^2\}\), including the finite initial segment; and equivalence of all four zero limits in L1 and L2 for \(S_N,D_N\), together with the corresponding positive-limsup criteria. The original source uses \(\sigma_N=\sqrt{N\min(\beta_N,1)}\). No uniform entry time into the eventual interval is asserted.

THM049 adds its exact definitions and modal identity in Section 8, the equivalence for *every fixed smooth real test* in Section 9, and the full-target positive-limsup witness statement in Section 10. Its finite-N integrals must be genuine integrals of the actual current and current/initial observables.

The joint logical negation is the existence of an admitted datum or critical sequence violating at least one frozen clause: finite-N L2, the uniform squared-overshoot estimate and its stated dependence, either squared-UI assertion, one of the L1/L2/endpoint equivalences, a modal coefficient/integrability/rate assertion, the all-smooth-test modal equivalence, or its fixed-mode positive-limsup formulation. Infinite instantaneous source variance, failure of an attempted proof, or a nonzero unresolved THM046 limit is not that negation.

All eleven original inputs were hash-verified before their mathematical use. The two added inputs were verified before reading the companion theorem. The packet contains all thirteen original byte strings and both manifests. Only these source contracts are used:

| Allowed input | Mathematical use and limitation |
|---|---|
| Frozen R1 model | Normalization, noise, ordered deleted labels and mean-field centering. |
| R1 algebra, Sections 1–2 | Smooth one-body convention and sign; Section 3 below derives the singular instance directly. No singular diagonal is inherited. |
| R4 response, Sections 2–3 | Heat representation and compensated Coulomb measure, rechecked in Section 2. No pair-propagator theorem is imported. |
| R6 realization, Sections 3–5 | Local cutoff construction, noncollision, energy localization and true martingale passage, specialized below. No corrector-domain theorem or uniform density estimate is imported. |
| R10 actual-law report, Section 3 | Positive heat-split energy floor; derived again below. Its free-energy sign, entropy estimates, corrector and conditional reference-energy inputs are not premises. |
| R16 source report, Sections 4–7 | Positive polynomial-tail splitting, commutator and remainder bounds; specialized and rederived in Section 4. Its expected-energy theorem is not used to obtain a second moment. |
| THM046 | The still-open target, actual law and critical sequence; never a premise asserting decay. |
| THM048 and THM049 | Frozen propositions and exact negations to be proved. |
| AGENTS, orchestration, task and addendum | Research and isolation instructions, not mathematical evidence. |

No external literature theorem, private source, nonallowlisted linked file, current canonical state/history, memory file or previous checker is used. The scoped task overrides the general directions to read other status files, write canonical ledgers, spawn children or checkpoint a commit. No such action occurred.

## 2. Kernel, actual paths, and the energy martingale

Let \(p_u\) be the periodized Gaussian with Fourier coefficient \(e^{-cu|k|^2}\). Unfolding its Gaussian gives positivity, mass one and this coefficient. Therefore
\[
 g(z)=c\int_0^\infty(p_u(z)-1)du
 \tag{2.1}
\]
in Haar L1: at small times the L1 integrand is at most two, and at large times it decays exponentially. Its nonzero Fourier coefficients are exactly \(|k|^{-2}\). Integrating the central Euclidean Gaussian gives \(|z|^{-2}\). Other lattice Gaussians at small times and the large-time remainder differentiate under integrable bounds locally, giving
\[
 g(z)=|z|^{-2}+H(z),\quad H\in C^\infty(B_{1/3}),\quad
 K(z)=2z|z|^{-4}-\nabla H(z).
 \tag{2.2}
\]
Consequently \(g\in L^1\), \(K\in L^1\), and \(g_*:=\inf_{z\ne0}g(z)>-\infty\). The local flux is \(2|\mathbb S^3|=4\pi^2=c\); the zero mode and the Fourier coefficients identify
\[
 \operatorname{div}K=c(\delta_0-dz),\qquad
 \Delta g=c\quad\hbox{off zero}.
 \tag{2.3}
\]
The constant compensation is retained in contractions. The punctured formula is used only on collision-excluded paths.

Define the complete energy
\[
 H_N(x)=N^{-1}\sum_{i<j}g(x_i-x_j),\qquad
 E_N^\circ=H_N-(N-1)g_*/2\ge0.
 \tag{2.4}
\]
Its sublevels are compact in the collision-free configuration space, because each shifted pair term is nonnegative and a colliding pair makes one term diverge. Direct differentiation of both coordinates of every unordered pair gives
\[
 B=-\nabla H_N,\qquad \Delta_{4N}H_N=c(N-1).
 \tag{2.5}
\]
The whole squared drift is used, including all three-label force cross terms; it is not replaced by a sum of individual squared pair forces.

For completeness, multiply \(K\) by smooth even collision cutoffs. Subtracting each continuous driving path reduces the cutoff equation to an ordinary integral equation with a globally Lipschitz drift. Picard iteration with its summable factorial remainder gives existence and uniqueness; its iterates give joint measurability in the initial state and Brownian path. Cutoff solutions agree up to the corresponding collision-excluded exits. They therefore patch into the maximal local singular solution. On an energy sublevel all differentiated quantities are bounded. Stopping at the first level \(R\), smooth Itô calculus gives
\[
 E_N^\circ(X_{t\wedge\tau_R})+
 \int_0^{t\wedge\tau_R}|B(X_u)|^2du
 =E_N^\circ(X_0)+\nu c(N-1)(t\wedge\tau_R)+M^E_{t\wedge\tau_R},
 \tag{2.6}
\]
\[
 M_t^E=\sqrt{2\nu}\sum_i\int_0^t\nabla_iH_N(X_u)\cdot dW_i(u),
 \qquad [M^E]_t=2\nu\int_0^t|B(X_u)|^2du.
 \tag{2.7}
\]
Initially the martingale notation denotes the stopped integral. For a fixed collision-free initial state, expectation of (2.6) gives an exit probability at most \((E_N^\circ(X_0)+\nu c(N-1)T)/R\). A finite-time path confined to a collision-excluded compact set has a limit and can be continued. Sending \(R\to\infty\) proves global noncollision and uniqueness. Joint measurability permits integration against the independent iid initial law. This law has finite initial shifted-energy mean because \(g\in L^1\), and \(\mathbb EH_N(X_0)=0\).

Fatou applied to the nonnegative left side of (2.6) proves \(\mathbb E\int_0^T|B|^2<\infty\). Thus (2.7) is a true L2 martingale, and its stopped versions converge in L2 by the Itô isometry and integrability of the omitted bracket. The un-stopped identity is now justified pathwise and in expectation:
\[
 H_N(X_t)+I_t=H_N(X_0)+\nu c(N-1)t+M_t^E,
 \qquad I_t=\int_0^t|B(X_u)|^2du,
 \tag{2.8}
\]
\[
 \mathbb EH_N(X_t)+\mathbb EI_t=\nu c(N-1)t.
 \tag{2.9}
\]
No square-integrability hypothesis on \(H_N(X_0)\) is used. Conditioning on any event measurable with respect to the initial positions preserves Brownian independence and the localized argument; for bounded stochastic integrands its conditional Itô isometry follows directly by multiplying by the event indicator. An anticipative event would not justify the same conditional argument.

All regularization is at fixed \(N,\nu,T\). The local cutoff is removed by the energy exits, before any \(N\to\infty\) claim. Along each actual path the minimum pair distance on \([0,T]\) is positive almost surely. A heat approximation, if used for the kernel, converges with all needed derivatives on this path's compact collision-excluded range. No simultaneous stochastic cutoff/particle limit, uniform collision separation or singular collision trace is used.

## 3. Smooth endpoint identity and finite-N square integrability

For a smooth scalar \(f\), oddness and integrability of \(K\) give the actual row and background
\[
 A_f(x):=\int J^f(x,y)dy=-c(f(x)-\langle f\rangle),
 \qquad \iint J^f=0.
 \tag{3.1}
\]
Indeed the first gradient term has zero force integral; the second is the compensated divergence pairing with \(f\). Also \(|J^f(x,y)|\le C_f(1+\operatorname{dist}(x,y)^{-2})\), so the row is an ordinary L1 integral. This proves the contractions without assigning any diagonal value.

Apply smooth Itô to \(N^{-1}\sum_i f_t(X_i(t))\) on the energy stops. Symmetrizing the finite deleted sum gives the drift term \((2N^2)^{-1}\sum_{i\ne j}J^{f_t}_{ij}\). The backward equation is
\[
 \partial_tf_t+\nu\Delta f_t-c(f_t-\langle h\rangle)=0.
\]
Together with (3.1), this yields after removal of the stops
\[
 D_N=S_N+Z_N^f,
 \quad Z_N^f=\sqrt{2\nu/N}\sum_i\int_0^T\nabla f_t(X_i(t))\cdot dW_i(t),
 \tag{3.2}
\]
\[
 [Z_N^f]_t=\frac{2\nu}{N}\sum_i\int_0^t|\nabla f_u(X_i(u))|^2du
 \le 2\nu T L_h^2,
 \quad L_h:=\sup_{0\le t\le T}\|\nabla f_t\|_\infty.
 \tag{3.3}
\]
For each fixed \(\nu\), all derivatives of \(f\) are bounded. Uniformly in all \(\nu>0\), its spatial seminorms are bounded by fixed Fourier seminorms of \(h\), since the multipliers have modulus at most one. The row contribution in (3.2) is present with exactly the sign in (3.1).

The time-integrated source is first defined pathwise: the actual path is collision-free, and its finite pair sum and smooth rows are continuous on its compact time range. Stopped equalities therefore pass pathwise; the stochastic integral passes in L2 by bounded gradients. In addition, \(Q_a h=\langle h\rangle+e^{-ca}P_{\nu a}(h-\langle h\rangle)\) is a convex combination of a heat average and the Haar average, so \(\|f_t\|_\infty\le\|h\|_\infty\). Hence
\[
 |D_N|\le 2\sqrt N\|h\|_\infty,
 \qquad \mathbb E|Z_N^f|^2\le 2\nu TL_h^2.
 \tag{3.4}
\]
For every finite \(N\) and every finite positive \(\beta_N\), (3.2) proves genuine L2 integrability of \(S_N\) and \(D_N\). It does not assert L2 integrability of the instantaneous source. For an initial event \(E\), the needed conditional estimate is
\[
 \mathbb E[\mathbf1_E|Z_N^f|^2]
 =\mathbb E[\mathbf1_E[Z_N^f]_T]\le2\nu TL_h^2\mathbb P(E).
 \tag{3.5}
\]
This uses \(\mathbf1_E\in\mathcal F_0\), not independence of the evolved particles. We do not set \(\mathbb E[S_N Z_N^f]\) to zero.

## 4. Deterministic source domination and the sharp energy floor

This section specializes the earlier positive-splitting argument and supplies its actual pointwise consequence. It is not an inference from its old L1 conclusion.

Fix \(M=6\), \(0<r\le2\), and set
\[
 w_r(u)=(1-e^{-u/r})^6,\quad \psi_r(u)=1-w_r(u),
\]
\[
 g_r=c\int_0^\infty w_r(u)(p_u-1)du,\quad
 q_r=c\int_0^\infty\psi_r(u)p_u\,du\ge0,\quad
 b_r=c\int_0^\infty\psi_r(u)du=cr\sum_{j=1}^6j^{-1}.
 \tag{4.1}
\]
Thus \(g=g_r+q_r-b_r\) in L1 and off zero. At fixed \(r\), \(g_r\) is C2: the small-time bound \(w_r(u)\le(u/r)^6\) makes the differentiated Gaussian integrals through order two integrable. Its positive nonzero Fourier coefficients are
\[
 a_r(k)=c\int_0^\infty w_r(u)e^{-cu|k|^2}du
       =cr\frac{6!}{z(z+1)\cdots(z+6)},\qquad z=cr|k|^2.
 \tag{4.2}
\]
The identity follows by expanding \((1-e^{-u/r})^6\), or by one substitution and six integrations by parts. From the Gaussian bound and the split of the integral at \(r\),
\[
 0\le g_r(0)=\sum_{k\ne0}a_r(k)\le Cr^{-1},\qquad b_r\le Cr.
 \tag{4.3}
\]
All constants here depend only on the fixed kernel and dimension.

For a collision-free configuration define
\[
 E_r=\tfrac12\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2\ge0,
 \qquad Q_r=\frac1{2N^2}\sum_{i\ne j}q_r(x_i-x_j)\ge0.
\]
Subtract the *smooth* energy self term and retain the constant background to obtain
\[
 \frac{H_N}{N}=E_r+Q_r-\frac{g_r(0)}{2N}-\frac{N-1}{2N}b_r.
 \tag{4.4}
\]
At \(r=N^{-1/2}\), (4.3) proves the deterministic sharp floor
\[
 H_N\ge-F\sqrt N
 \tag{4.5}
\]
for a kernel constant \(F\). This is a pointwise bound, independent of a law or diffusivity. In particular (2.9) and the Doob L2 inequality give
\[
 \mathbb EI_T\le F\sqrt N+\nu c(N-1)T,
\]
\[
 \mathbb E(M_T^{E,*})^2\le 8\nu\{F\sqrt N+\nu c(N-1)T\},
 \quad M_T^{E,*}:=\sup_{t\le T}|M_t^E|.
 \tag{4.6}
\]
The true martingale property was proved with the coarse collision barrier before using the sharper floor to improve the bound. There is no circular use of an unproved energy square.

For completeness, the commutator estimate for the retained kernel follows from
\[
 0\le-\frac{\xi a_r'(\xi)}{a_r(\xi)}
 =2\sum_{j=0}^6\frac{cr\xi^2}{cr\xi^2+j}\le14.
 \tag{4.7}
\]
If \(k,\ell\ne0\), \(q=k-\ell\), comparison of their lengths gives
\[
 \frac{|k a_r(k)-\ell a_r(\ell)|}{\sqrt{a_r(k)a_r(\ell)}}
 \le15|q|(1+|q|)^8.
 \tag{4.8}
\]
To see this, put \(u=\min(|k|,|\ell|)\ge1\), \(R=\max(|k|,|\ell|)\). Integrate (4.7) to bound \(a_r(u)/a_r(R)\le(R/u)^{14}\) and the difference by \(14a_r(u)(R-u)/u\). Bound the vector difference by \(|q|a_r(u)+R(a_r(u)-a_r(R))\), then use \(R-u\le|q|\) and \(R/u\le1+|q|\).

For a smooth vector field \(v\), set \(J_r=-\nabla g_r(x-y)\cdot(v(x)-v(y))\). Its smooth diagonal is zero. The literal statistic, including all rows, equals its centered full product and has Fourier form
\[
 P_N[J_r]=-\pi i\sum_{k,\ell\ne0}
 (k a_r(k)-\ell a_r(\ell))\cdot\widehat v(\ell-k)
 \widehat\rho(k)\overline{\widehat\rho(\ell)}.
 \tag{4.9}
\]
This follows by writing the force convolution against \(\rho\), whose zero mode vanishes, and symmetrizing the two Fourier indices. Its series is absolutely convergent at fixed \(r\); the following bound supplies another absolute majorant. Apply (4.8) and Cauchy–Schwarz to the shifted sequence \(\sqrt{a_r(k)}|\widehat\rho(k)|\):
\[
 |P_N[J_r]|\le 2C_v E_r,\qquad
 C_v=15\pi\sum_q|q|(1+|q|)^8|\widehat v(q)|.
 \tag{4.10}
\]
The argument also works for a complex vector field by the same absolute values.

For the discarded kernel use \(\delta(z)=\operatorname{dist}(z,0)\). Each Gaussian translate satisfies
\[
 \delta(z)|\nabla p_u(z)|\le C p_{2u}(z).
\]
Indeed \(\delta(z)\le|z+n|\), and the remaining factor after division by the wider Gaussian is a constant times \(y e^{-y}\), which is bounded. Thus the mean-value bound on \(v\) gives
\[
 |J_{g-g_r}(x,y)|\le C\|Dv\|_\infty q_{2r}(x-y).
 \tag{4.11}
\]
The change of variables is \(u\mapsto2u\), and \(\psi_r(u)=\psi_{2r}(2u)\). The Haar gradient integrals are legitimate because their small-time L1 bound is \(Cu^{-1/2}\), integrable here. Applying (4.11) separately to the deleted pair, row and background terms gives
\[
 |P_N[J_{g-g_r}]|\le C\|Dv\|_\infty(Q_{2r}+\tfrac32b_{2r}).
 \tag{4.12}
\]
No weighted-kernel positivity is claimed. Only the positive \(q\) majorant and positive retained Fourier coefficients are used.

In (4.4), \(E_r\le H_N/N+d_r\), \(Q_{2r}\le H_N/N+d_{2r}\), where \(d_r=g_r(0)/(2N)+(N-1)b_r/(2N)\). Combining (4.3), (4.10), (4.12) at \(r=N^{-1/2}\), and increasing a kernel constant to cover (4.5), proves
\[
 |P_N[J^{f_t}]|\le C_h\left(\frac{H_N}{N}+\frac{F_1}{\sqrt N}\right),
 \qquad H_N+F_1\sqrt N\ge0.
 \tag{4.13}
\]
Here \(C_h\) is bounded by a fixed Fourier seminorm of \(h\), uniformly in \(t,N,\nu>0\). One may choose it proportional to \(\sum_k(1+|k|)^{10}|\widehat h(k)|\). For the single nonzero mode \(e_k\), it is at most \(C(1+|k|)^{10}\). Constant tests are handled separately with identically zero source. Equations (4.1)–(4.13) use a deterministic splitting scale on an already constructed actual path; it is not a singular-SDE approximation scale.

## 5. The initial iid truncation and the rare complement

The local expansion (2.2) gives, for all \(L\ge L_0\),
\[
 |\{z:g(z)>L\}|\le CL^{-2},\quad
 \int(g-L)_+\le C/L,\quad
 \int\min(g,L)^2\le C(1+\log L).
 \tag{5.1}
\]
For the first bound a large superlevel lies in a ball of radius \(C L^{-1/2}\), whose four-dimensional volume is \(O(L^{-2})\). The second follows by integrating this tail. For the third, the bounded negative part contributes a constant, and the positive part satisfies the exact tail formula \(\mathbb E\min(g_+,L)^2=2\int_0^L u\,\mathbb P(g_+>u)du\). This is the source of the logarithm, not a finite second moment of \(g\).

Put \(g_L=\min(g,L)\), \(m_L=\int g_L=-\int(g-L)_+\), and
\[
 H_{N,L}=N^{-1}\sum_{i<j}g_L(X_i(0)-X_j(0)).
\]
Its expectation is \((N-1)m_L/2\). For distinct unordered pairs the centered summands have covariance zero. Disjoint pairs are independent. If the pairs share one label, condition on that Haar position; each of the two remaining independent positions has conditional row mean \(m_L\), constant in the shared position. Therefore exactly
\[
 \operatorname{Var}(H_{N,L})
 =\frac{N-1}{2N}\left(\int g_L^2-m_L^2\right),
\]
\[
 \mathbb EH_{N,L}^2\le C(1+\log L)+CN^2/L^2.
 \tag{5.2}
\]
This is an initial product-law statement only. Its factors include the unordered pair count and the energy denominator \(N\).

For sufficiently large \(N\), choose \(L=N^2\) and the initial event
\[
 G_N=\{g(X_i(0)-X_j(0))\le N^2\text{ for every }i<j\}.
\]
The union bound and (5.1) give
\[
 \mathbb P(G_N^c)\le C/N^2,
 \quad H_N(X_0)=H_{N,N^2}\text{ on }G_N,
 \quad \mathbb E[\mathbf1_{G_N}(H_N(X_0)^+)^2]\le C(1+\log N).
 \tag{5.3}
\]
There is no conditional product-law claim on \(G_N\); the moment bound is the *unconditional* truncated-energy second moment, with a nonnegative indicator discarded.

## 6. Entire THM048(A)

Integrating (4.13) and using (2.8), with its nonnegative dissipation discarded only for this upper bound, yields
\[
 |S_N|\le C_hT\left[F_1+\nu c(N-1)T/\sqrt N
       +\frac{H_N(X_0)^++M_T^{E,*}}{\sqrt N}\right].
 \tag{6.1}
\]
On the fixed eventual interval, \(\nu\sqrt N=1/\lambda_N\le1/\lambda_-\). Choose \(A=C_hT(F_1+cT/\lambda_-)\), enlarged if needed. All choices depend only on the permitted fixed data and bounds; no sequence convergence rate enters. Then
\[
 \mathbb E[\mathbf1_{G_N}(|S_N|-A)_+^2]
 \le \frac{2C_h^2T^2}{N}
 \{\mathbb E[\mathbf1_{G_N}(H_N(X_0)^+)^2]
   +\mathbb E(M_T^{E,*})^2\}
 \le C(1+\log N)/N.
 \tag{6.2}
\]
The energy martingale bound (4.6) is \(O(1)\) on this tail. Squaring the untruncated initial energy here would be invalid.

On the complement use the different identity (3.2), the bounded endpoint and the conditional Itô estimate (3.5):
\[
 \mathbb E[\mathbf1_{G_N^c}(|S_N|-A)_+^2]
 \le\mathbb E[\mathbf1_{G_N^c}|S_N|^2]
 \le (8N\|h\|_\infty^2+4\nu TL_h^2)\mathbb P(G_N^c)
 \le C/N.
 \tag{6.3}
\]
This is the rare-event passage. No square of the singular initial energy occurs on this event, and the Brownian integral is conditioned on an event in the initial sigma field. Equations (6.2)–(6.3) prove exactly (1.6).

To prove squared uniform integrability, write \(Y_N=(|S_N|-A)_+\). If \(R>2A\), then on \(\{|S_N|>R\}\), \(|S_N|^2\le4Y_N^2\). Given \(\varepsilon>0\), (1.6) makes the latter expectation at most \(\varepsilon\) for every sufficiently large \(N\), uniformly on the chosen tail. The finitely many remaining \(S_N\) are L2 by Section 3, so their squared tails tend to zero as \(R\to\infty\). This proves UI, including any finite initial segment with arbitrarily large or small finite \(\beta_N\).

Moreover \(\mathbb E|Z_N^f|^2\le C\nu_N\to0\). A sequence of nonnegative random variables whose expectations tend to zero is uniformly integrable after including any finite integrable prefix: split at a large index, then treat the finite prefix. Thus \(\{|Z_N^f|^2\}\) is UI. For any two real numbers, the squared tail of their sum is bounded by four times the sum of their squared tails at half the threshold. Apply this to (3.2) to obtain UI of \(\{|D_N|^2\}\).

At \(T=0\), both variables and every time integral vanish. If \(h\) is constant, \(f_t=h\), all gradients and sources vanish and both defects are zero. These cases satisfy (1.6) with \(A=C=0\). No exceptional endpoint or preparation has been removed.

## 7. Entire THM048(B)

For any sequence \(Y_N\) with \(\{|Y_N|^2\}\) UI, \(\mathbb E|Y_N|^2\to0\) implies L1 convergence by Cauchy–Schwarz. Conversely, for fixed \(R\),
\[
 \mathbb E|Y_N|^2\le R\mathbb E|Y_N|
       +\mathbb E[|Y_N|^2\mathbf1_{\{|Y_N|>R\}}].
\]
First take \(N\to\infty\) and then \(R\to\infty\). This proves the converse. Apply it separately to \(S_N,D_N\). Finally (3.2) gives
\[
 |\|S_N\|_{L^p}-\|D_N\|_{L^p}|\le\|Z_N^f\|_{L^p}\to0,
 \qquad p=1,2.
 \tag{7.1}
\]
All four vanishing limits are equivalent. Because they concern nonnegative finite quantities, failure of any zero limit is exactly positive limsup; the proved equivalences therefore give the four equivalent failure criteria too. This does not say their nonzero limsup values are equal.

Criticality implies \(\beta_N=\lambda_N\sqrt N\to\infty\), so \(b_N=\min(\beta_N,1)=1\) eventually, without a universal index. The original THM046 quantity is \(\sqrt{b_N}\,\mathbb E|S_N|\), and its second-moment version is \(b_N\mathbb E|S_N|^2\). The finite prefix does not affect limits or positive-limsup criteria. This proves exactly the claimed equivalence, while leaving all such limits unresolved.

## 8. Entire THM049(A): finite labels, true noise and the identity

Fix a nonzero \(k\). Use exactly the frozen definitions
\[
 Z_k(t)=\eta_N(t)[e_k],\quad \ell_k=c|k|^2,\quad a_k=c+\nu\ell_k,
 \quad \widetilde a=a_k-c/N,\quad A_k=e^{-a_kT},
\]
\[
 j_k(x,y)=J^{e_k}(x,y)+c(e_k(x)+e_k(y)),\quad
 U_N^k=\frac1{2N^2}\sum_{i\ne j}j_k(X_i,X_j).
 \tag{8.1}
\]
Its Haar row and background are zero by (3.1). The finite-label correction is exactly
\[
 P_N[J^{e_k}]=U_N^k+\frac cN Z_k.
 \tag{8.2}
\]
Indeed the added two one-body terms contribute \(c(N-1)Z_k/N\) to \(U_N^k\), whereas the literal negative row in \(P_N\) contributes \(cZ_k\). This difference must not be suppressed.

For current versus initial labels, define exactly
\[
 A_2(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(t))}],
\quad
 A_3(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(t))}],
\]
\[
 B_2(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(0))}],
\quad
 B_3(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(0))}].
 \tag{8.3}
\]
At \(N=2\) the terms involving label three are absent and never evaluated. Exchangeability follows from permutation equivariance and pathwise uniqueness for (1.2), jointly over the initial/current path. Symmetry of \(j_k\) makes the two overlapping labels equal. Among the \(N(N-1)N\) ordered triples \((i,j,l)\) with \(i\ne j\), exactly \(2N(N-1)\) have \(l=i\) or \(j\), and \(N(N-1)(N-2)\) have three distinct labels. Thus
\[
 N\mathbb E[U_N^k(t)\overline{Z_k(t)}]
 =\frac{N-1}{N}A_2(t)+\frac{(N-1)(N-2)}{2N}A_3(t)=:F_N(t),
\]
\[
 N\mathbb E[U_N^k(t)\overline{Z_k(0)}]
 =\frac{N-1}{N}B_2(t)+\frac{(N-1)(N-2)}{2N}B_3(t)=:G_N(t).
 \tag{8.4}
\]
No equal-time or two-time factorization occurs.

Here all expectations and time integrals are absolutely integrable. To justify this directly at fixed \(N,\nu,T\), \(|j_k(x,y)|\le C_k(1+|g(x-y)|)\) follows from (2.2). The coarse nonnegative energy sum, (2.9), and exchangeability imply finite \(\mathbb E|g(X_1(t)-X_2(t))|\), bounded on this fixed time interval. Multipliers \(e_k\) have modulus one, including at the initial time. Tonelli therefore gives all the required absolute time integrals for (8.3)–(8.4), and also for \(U_N^k\overline Z\). No joint density of \((X(t),X(0))\) is needed. The expectations are jointly measurable because the solution is jointly measurable and the off-diagonal kernel is Borel.

Smooth modal Itô calculus, with the same localization as Section 3, gives
\[
 dZ_k=-\widetilde a Z_k\,dt+U_N^k\,dt+dM_k,
\quad
 dM_k=\frac{\sqrt{2\nu}}N\sum_i\nabla e_k(X_i)\cdot dW_i.
 \tag{8.5}
\]
This is a true complex L2 martingale, with both covariations
\[
 d[M_k,\overline{M_k}]_t=\frac{2\nu\ell_k}{N}dt,
 \qquad d[M_k,M_k]_t=-\frac{2\nu\ell_k}{N}Z_{2k}(t)dt.
 \tag{8.6}
\]
The first is the complex squared norm; the second is not identically zero pathwise. Also \(\mathbb E[M_k(t)\overline{Z_k(0)}]=0\), because \(Z_k(0)\) is bounded and initial-measurable. This does not assert that \(M_k(t)\) is independent of \(U_N^k(t)\) or \(Z_k(t)\).

Set \(v(t)=N\mathbb E|Z_k(t)|^2\) and \(q(t)=N\mathbb E[Z_k(t)\overline{Z_k(0)}]\). The initial iid Haar identities give \(v(0)=q(0)=1\). Applying the product rule to (8.5), then taking expectations, gives the absolutely continuous equations
\[
 v'=-2\widetilde a v+2\operatorname{Re}F_N+2\nu\ell_k,
 \qquad q'=-\widetilde a q+G_N.
 \tag{8.7}
\]
For the first equation the real stochastic integral before expectation is \(2N\operatorname{Re}\int\overline{Z_k}\,dM_k\), whose bracket is at most \(8\nu\ell_kNT\); hence it is a true L2 martingale. For the second it is \(N\int\overline{Z_k(0)}dM_k\), with squared-norm bracket at most \(2\nu\ell_kNT\). The drift integrals are L1 by the preceding paragraph. These facts justify expectation and solve the domain and martingale issue without an instantaneous L2 assumption on \(U_N^k\).

Solving (8.7), using \(\widetilde a\ge c/2>0\), and expanding the endpoint square yields
\[
 \mathcal D_N(k,T):=N\mathbb E|Z_k(T)-A_kZ_k(0)|^2
 =v(T)+A_k^2-2A_k\operatorname{Re}q(T)
\]
\[
 =\big(e^{-\widetilde aT}-e^{-a_kT}\big)^2
  +\frac{\nu\ell_k}{\widetilde a}(1-e^{-2\widetilde aT})
  +2\operatorname{Re}\mathcal R_N(k,T),
 \tag{8.8}
\]
where precisely
\[
 \mathcal R_N(k,T)=\int_0^T
 \{e^{-2\widetilde a(T-t)}F_N(t)
 -e^{-a_kT}e^{-\widetilde a(T-t)}G_N(t)\}\,dt.
 \tag{8.9}
\]
In particular the subtracted term involves the full current/initial correlation, not just a current moment. The source/noise mixed contribution has not been dropped; (8.7) computes the full current moment.

Both explicit terms in (8.8) are nonnegative. The first is
\(e^{-2a_kT}(e^{cT/N}-1)^2=O_T(N^{-2})\). The second is at most \(2\nu|k|^2\), hence \(O_{k,\lambda_-}(N^{-1/2})\) on the critical tail. These estimates include \(T=0\). From \(\mathcal D_N\ge0\),
\[
 (\operatorname{Re}\mathcal R_N)_-
 \le\tfrac12\left[\big(e^{-\widetilde aT}-e^{-a_kT}\big)^2
       +\frac{\nu\ell_k}{\widetilde a}(1-e^{-2\widetilde aT})\right]=o(1).
 \tag{8.10}
\]
No separate sign, decay or variance estimate for the four correlations is asserted.

## 9. Entire THM049(B): fixed modes to every smooth real test

Extend the source and defect linearly to complex tests. For \(e_k=\cos(2\pi k\cdot x)+i\sin(2\pi k\cdot x)\),
\[
 \mathcal D_N(k,T)=\mathbb E|D_N^{\cos}|^2+\mathbb E|D_N^{\sin}|^2.
 \tag{9.1}
\]
The real-test THM048 already reconstructed in Sections 2–7 therefore implies: the original source L1 limit for both fixed real tests is equivalent to \(\mathcal D_N(k,T)\to0\). By (8.8) and the decay of the explicit terms, this is equivalent to \(\operatorname{Re}\mathcal R_N(k,T)\to0\).

To extend from fixed modes to a fixed smooth \(h\), an L1 majorant for the *same original source* is needed. Equations (4.13) and (2.9), without any second-moment summation, give on the critical tail
\[
 \mathbb E|S_N^{e_k}|
 \le \sqrt N\int_0^T\mathbb E|P_N[J^{Q_{T-t}e_k}]|dt
 \le C_{T,\lambda_-,g}(1+|k|)^{10}.
 \tag{9.2}
\]
In detail \(\mathbb EH_N(X_t)\le\nu c(N-1)t\), so the expectation of the right side of (4.13), multiplied by \(\sqrt N\), is bounded by \(C_k(F_1+cT/\lambda_-)\). This uses no old source-decay theorem and no positive-time product law.

For a fixed smooth \(h\), \(\sum_k(1+|k|)^{10}|\widehat h(k)|<\infty\). At each actual collision-free path its Fourier partial sums and all necessary derivatives converge uniformly. The finite deleted sum, the ordinary Haar rows and the time integral therefore reproduce the original source as the Fourier limit; (9.2) also gives L1 convergence and the uniform tail estimate
\[
 \mathbb E|S_N^h-S_N^{h^{(L)}}|
 \le C\sum_{|k|>L}(1+|k|)^{10}|\widehat h(k)|,
 \tag{9.3}
\]
where symmetric Fourier truncation keeps \(h^{(L)}\) real. If all fixed modes cancel, finitely many modes give \(\mathbb E|S_N^{h^{(L)}}|\to0\); then (9.3) tends to zero as \(L\to\infty\). The constant mode contributes zero. Conversely, an assertion for every fixed smooth real \(h\) applies to each fixed cosine and sine, so (9.1) and (8.8) give modal cancellation.

This proves the equivalence for each admitted critical sequence and each fixed \(T\), with no test depending on \(N\). The use of (9.2) only on an eventual interval is sufficient for convergence; arbitrary finite initial parameters change no limit. If desired, their finitely many L1 source bounds can be absorbed into a sequence-dependent finite-prefix majorant, but no such uniformity is claimed by the theorem. No N-uniform L2 Fourier summability estimate was needed or asserted.

## 10. Entire THM049(C): exact positive-limsup witnesses

The original full-target failure means: there exist a fixed smooth real \(h\), a fixed finite \(T\), \(\lambda>0\), and an admitted critical sequence with positive limsup of the original source L1 quantity. If every fixed nonzero mode cancelled on these same parameters, Section 9 would give that limit zero for this \(h\). Thus some fixed mode does not tend to zero. By (8.10) its negative part tends to zero, so its failure is exactly
\[
 \limsup_N\operatorname{Re}\mathcal R_N(k,T)>0.
 \tag{10.1}
\]
This is a fixed mode, not a mode chosen anew for each \(N\).

Conversely, (10.1) and (8.8) give positive limsup of \(\mathcal D_N\). By (9.1), at least one of the two fixed real tests, cosine or sine, has positive limsup of its endpoint second moment. THM048 then gives positive limsup of its original source L1 quantity, since \(b_N=1\) eventually. The elementary finite-choice step is valid even if the two moments alternate: if both limsups were zero, their sum would have zero limsup. This proves the whole witness equivalence. It exhibits no such witness.

## 11. Independent negative route, failures and scope audit

The negative route starts from the collision singularity and actual initial iid law rather than from the energy upper bound. It challenges the strongest tempting shortcut.

For a nonconstant cosine test and \(N=2\), choose an open set of positions and directions on which the Hessian quadratic form is bounded away from zero. As \(y=x-r\theta\),
\[
 J^f(x,y)=2r^{-2}\theta^T D^2f(x)\theta+O(r^{-1}).
\]
The Haar row is bounded, so the initial literal source square has on this set a positive multiple of \(\int_0^\epsilon r^3r^{-4}dr=\infty\). Likewise the initial energy square is infinite. This is an actual admitted finite-N instantaneous obstruction to two possible proof methods, not to THM048's *time-integrated* L2 claim. The proof above specifically survives it through (3.2) and the split (6.2)–(6.3).

A separate local two-body deterministic test checks the proposed rare-collision mechanism. With principal Coulomb force and relative coefficient \(2/N\), the radial equation is \(\dot r=4/(Nr^3)\), hence \(r(t)^4=r_0^4+16t/N\). Its time integral of \(r^{-2}\) is \(\frac N8(\sqrt{r_0^4+16T/N}-r_0^2)\), finite as \(r_0\downarrow0\). At the actual two-particle value \(N=2\), the relative drift is exactly \(K\) and the coefficient is eight in the fourth-power equation. This local noiseless principal-part calculation is a falsification diagnostic, not a replacement for the periodic positive-noise proof.

The finite-group iid truncation diagnostic independently enumerates the covariance cancellations, including shared labels; the Fourier diagnostic independently compares raw force sums, literal rows and the \(c/N\) label correction. Mutation controls remove the shared-row centering, pair factor, overlap coefficient, finite-label correction and noise factor and must be nonzero. Those exact finite models test algebra; they do not certify the singular stochastic limits, which are justified analytically above.

The fresh standard-library diagnostic completed on its first execution: **PASS, 2,203 exact assertions in 32 categories; all sixteen mutation families produced nonzero detections.** It uses rational and Gaussian-rational arithmetic, exhaustive finite configurations and deterministic parameter choices. There is no random seed, floating-point tolerance, dependency installation or imported checker. Exact counts, cases and the diagnostic's own digest are in the companion JSON; the portable verifier repeats the diagnostic and compares its entire result.

Chronological failures/limitations retained in the packet are: (i) the direct initial-energy square is invalid; (ii) the coarse order-N energy shift alone gives too weak a martingale estimate for the claimed rate, repaired by the independently derived order-\(\sqrt N\) floor; (iii) an unconditional noise L2 bound on the rare event would lose its event probability, repaired by initial-sigma-field conditioning; (iv) the original eleven-input task was extended administratively by two frozen inputs before sealing; (v) no current constructor proof, independent audit result or source-decay premise was made available. No failed scientific route has been concealed as a theorem counterexample.

| Frozen clause | Disposition |
|---|---|
| THM048 finite-N L2 and exact singular domain passage | Reconstructed, Sections 2–3. |
| THM048 uniform squared overshoot, prescribed constants and rate | Reconstructed, Sections 4–6. |
| THM048 both squared-UI assertions, finite initial segment, zero/constant endpoints | Reconstructed, Section 6. |
| THM048 every L1/L2/endpoint and positive-limsup equivalence, original scale | Reconstructed, Section 7. |
| THM049 current/current-initial integrability, finite-label overlaps, exact identity | Reconstructed, Section 8. |
| THM049 explicit signs/rates and vanishing negative part | Reconstructed, Section 8. |
| THM049 full smooth-test equivalence via polynomial original-source L1 bound | Reconstructed, Section 9. |
| THM049 fixed-mode positive witness and fixed real test converse | Reconstructed, Section 10. |
| Joint exact negation | No admitted witness found; excluded by the reconstructed proof in the frozen scope, subject to subsequent hostile review. |
| THM046 or actual signed-correlation cancellation | OPEN; neither proved nor disproved. |

## 12. Recoverable handoff

The companion directory is `ROUND_025_SOURCE_UI_BLIND_ARTIFACTS_20260918_084259_UTC` beside this report. Its README gives the exact portable verification command, fresh diagnostic results, nonzero mutation outcomes, input/source/exposure records, complete output inventory, archive member inventory and seals. The packet's report copy is byte-identical to this report. All issued payload bytes and the archive are read-only after checks; corrections must be new superseding artifacts. No canonical state, original input, baseline, git history or remote was changed. No commit, push, install, child agent, external browse, publication or contact occurred.

The next scientific obligation remains to prove or disprove the actual signed cancellation in (8.9), equivalently the original THM046 source limit. The proved squared-tail bound supplies uniform integrability and equivalence only. The next audit action is the root's comparison against the withheld construction, followed by a separately isolated hostile review of this full reconstruction and its package.
