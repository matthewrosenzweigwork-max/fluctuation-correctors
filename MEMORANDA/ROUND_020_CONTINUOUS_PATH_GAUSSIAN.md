# Round 020 — continuous-path Gaussian fluctuations for fixed smooth observables

TASK-090. Issued 2026-09-18 UTC. **Entire frozen THM042: CONDITIONAL PROVED CANDIDATE / CONSTRUCTOR SELF-CHECKED. Fresh whole-claim reconstruction and hostile gates remain pending.** This is a complete implication from the expressly conditional, byte-locked full sources supplied to this lane. Neither an earlier card's status nor this constructor's checking constitutes independent certification.

The additional path argument has two load-bearing steps. The deterministic inequalities inside the full R16 proof bound the source simultaneously over the entire family of backward tests. They imply that the nonlinear error tends to zero in expected uniform norm. The remaining continuous process has uniform fourth moments of increments, with a squared time increment on the right. An elementary dyadic argument proves tightness, and a real Fourier Gaussian series gives the specified continuous limit. Finite-dimensional convergence alone is not used to infer tightness.

## 1. Exact assertion, negation, and source boundary

Fix exactly the THM042 data: an integer \(d\ge3\), \(0<s\le d-2\), \(s<d/2\), \(T\in[0,\infty)\), a positive integer \(m\), and fixed real \(h_1,\ldots,h_m\in C^\infty(\mathbb T^d)\). The unit torus has Haar mass one and characters \(e^{2\pi i k\cdot x}\). The even, zero-mean, coefficient-one kernel has

\[
 \widehat g(k)=c_{d,s}|k|^{s-d}\quad(k\ne0),\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1.1}
\]

The actual singular particles start independently with Haar law, independently of all independent standard Brownian drivers, and solve

\[
 dX_i(r)=\frac1N\sum_{\ell\ne i}K(X_i(r)-X_\ell(r))\,dr
              +\sqrt{2\nu_N}\,dW_i(r),\qquad N\ge2.
 \tag{1.2}
\]

There is no external drift. Assume \(0\le\nu_N\le\nu_*<\infty\) and \(\nu_N\to\bar\nu\ge0\), without a rate. Define

\[
 b(\nu)=\begin{cases}1,&0\le\nu\le1,\\1/\nu,&\nu>1,\end{cases}
 \quad b_N=b(\nu_N),\quad\bar b=b(\bar\nu),\quad
 \sigma_N=\sqrt{Nb_N},\quad\rho_N=\eta_N-dx,
 \quad\eta_N=N^{-1}\sum_i\delta_{X_i}.
 \tag{1.3}
\]

The exact assertion is that \(Z_{N,j}(t)=\sigma_N\rho_N(t)[h_j]\) has exact mean zero at each deterministic time, and that the actual continuous vector converges weakly in \(C([0,T],\mathbb R^m)\), with its uniform norm, to a centered continuous possibly degenerate Gaussian process. Write

\[
 a_k=4\pi^2|k|^2,\qquad D_k=4\pi^2c_{d,s}|k|^{s+2-d},\qquad
 L_k=D_k+\bar\nu a_k>0\quad(k\ne0).
\]

The required covariance, for all \(t,u\in[0,T]\), is

\[
 \mathbb E Z_i(t)Z_j(u)=\bar b\sum_{k\ne0}
 \widehat h_i(k)\overline{\widehat h_j(k)}
 \left[\frac{D_k}{L_k}e^{-(t+u)L_k}
       +\frac{\bar\nu a_k}{L_k}e^{-|t-u|L_k}\right].
 \tag{1.4}
\]

All original source, Haar background, and Itô terms must be genuine. The exact negation is an admitted fixed datum and bounded convergent noise sequence violating exact centering, existence or continuity of this Gaussian limit, tightness of the actual path laws, or weak convergence to it in the stated uniform topology. Failure of one proof estimate does not establish that negation.

The task and its manifest were read first. The isolated branch is `codex/hocf-r020-continuous-path-construction`, at worktree `/Users/matthewrosenzweig/.codex/worktrees/hocf-r020-continuous-path-construction`, created from `e75f8b780682a7e9fb0715b5e8b5873be684a2e8`. Exactly fourteen listed inputs were checked in the root before copying and checked again in this worktree. The manifest itself was copied as routing evidence. Inherited non-allowlisted files were ignored. The narrower task restriction supersedes general orientation, state-editing, orchestration and commit instructions.

| Supplied full input | Exact use and retained boundary |
|---|---|
| AGENTS.md; ROUND_001_MODEL.md; TASK-090 | Frozen model, scope, normalization, deleted-label convention, isolation and bounded handoff. |
| R1 algebra, entire supplied report | Sections 1–2 and 5 supply the smooth first-order convention. Section 4 below reconstructs its actual singular version. Its smooth diagonal assignment and all higher-corrector claims are not imported. |
| R4 singular response, entire supplied report | Sections 2–5 supply the coefficient-one heat representation, integrable force, full divergence measure and smooth-test response. No pair-propagator limit is used. |
| THM026 and complete R6 particle report | Global measurable noncollision, uniqueness, same-noise fixed-\(N\) heat passage, and collision-excluded local Itô calculus. The proof mechanisms are restated in Section 2. The card remains OPEN / UNAUDITED as issued; its status is not evidence of a gate. |
| THM031 and complete R10 actual-law report | Only Sections 2–3: actual expected-energy sign, pair-energy integrability, and quantitative empirical Fourier control. Its unsmoothed pair-gradient, R8 domain and R9 reference-energy premises are nondependencies. |
| THM038 and complete R16 source report | Sections 2–7, with their explicit test seminorms and deterministic inequalities. Section 3 proves the needed simultaneous-family consequence from that full argument; it is not inferred from the card's fixed-terminal statement. Its source status remains conditional as issued. |
| THM040 and complete R18 finite-dimensional report | Entire issued source read, especially Sections 2–8. Section 8 here reproduces the necessary probability implication. The R17 comparison mentioned in R18 is not a premise; no unseen R17 file, card or checker is used. R18 expressly disclaims path tightness. |
| THM042 | Entire unchanged new assertion, covariance, exact negation and exclusions. |

The full supplied historical narratives were read; their references to unprovided files did not grant access to, or establish results from, those files. No separate prior checker or result artifact was read. No outside citation, theorem number, literature theorem, private source or novelty claim is invoked. All necessary compactness and continuity criteria used below are proved in their actual form. All constants in the path argument depend only on the fixed data and finitely many explicitly displayed smooth seminorms; they are independent of \(N\), the chosen noise, collision stops and particle heat cutoffs. Finite-\(N\) source construction constants are distinguished below.

## 2. Actual singular law, energy input, and exact centering

Here are the precise conditional earlier facts and their mechanisms. Put \(\alpha=(d-s)/2\ge1\), \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\), and let \(p_r\) be the positive unit-mass periodized Gaussian heat kernel. The full R4 construction gives

\[
 g(z)=A\int_0^\infty r^{\alpha-1}(p_r(z)-1)\,dr.
 \tag{2.1}
\]

The nonzero Fourier integral is \(A\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}\), exactly (1.1). Substitution \(v=|z|^2/(4r)\) in the central Euclidean Gaussian term gives local coefficient one. Small-time bounds on the other lattice translates and large-time exponential Fourier bounds permit all derivatives in their difference. Thus \(g(z)=|z|^{-s}+H(z)\) near zero, with \(H\) smooth. It follows that \(g\) has a finite negative lower bound \(g_*\), is smooth away from zero, and \(K\in L^1\), since \(s+1<d\).

The punctured-ball boundary flux against a smooth test is
\(s r^{d-s-2}\int_{\mathbb S^{d-1}}f(r\theta)\,d\theta+O_f(r^{d-1})\).
It vanishes below Coulomb and converges to \(c_df(0)\) at Coulomb. Fourier identification, including the zero mode, gives the full measure

\[
 D:=\operatorname{div}K=
 \begin{cases}s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \quad c_d=(d-2)|\mathbb S^{d-1}|=4\pi^2c_{d,d-2}.
 \tag{2.2}
\]

It has zero mass and \(D\ge-\kappa\,dz\) for a fixed finite \(\kappa\). Its nonzero coefficient is \(D_k\). At Coulomb the compensating Haar part and atom are retained in every response convolution. The punctured identity \(\Delta g=c_d\) is used only on collision-excluded paths.

For \(H_N=N^{-1}\sum_{i<\ell}g(x_i-x_\ell)\), the shifted energy
\(\mathcal H_N=H_N-(N-1)g_*/2\) is nonnegative and has compact sublevels in the collision-free configuration space. Every partial or simultaneous collision makes at least one nonnegative summand diverge. The full drift is \(B=-\nabla H_N\), and

\[
 \Delta_{Nd}H_N=\frac2N\sum_{i<\ell}\Delta g(x_i-x_\ell)\le(N-1)\kappa.
 \tag{2.3}
\]

Even smooth collision cutoffs, Picard iteration after subtracting additive noise, and agreement before exits construct a jointly measurable local solution. Stopping at energy \(R\), the exact energy drift is \(-|B|^2+\nu\Delta H_N\), and the stopped bracket is \(2\nu\int|B|^2\). Every coefficient is bounded on that sublevel, so the stopped martingale is true. Consequently

\[
 \mathbb P_x(\tau_R\le T)\le
 [\mathcal H_N(x)+\nu(N-1)\kappa T]/R.
 \tag{2.4}
\]

Bounded-energy paths extend, so this proves global noncollision and pathwise uniqueness from each fixed collision-free start. Joint measurability permits integration against iid Haar, whose shifted-energy expectation is \(-(N-1)g_*/2\). No common exceptional set for all uncountably many starts is claimed. Each realized finite-horizon path has positive minimum pair distance. Heat forces converge locally in \(C^1\) away from zero; same-noise subtraction and Gronwall on that path's collision-excluded neighborhood prove full heat-family path convergence at fixed \(N,\nu,T\). No rate uniform in \(N\) is used.

The actual energy sign is a separate law input, supplied with proof in R10 and R16. At a fixed particle heat cutoff and positive noise, the smooth density starts at one and obeys the smooth Fokker–Planck equation. Bounded coefficients on the compact configuration space give a classical density with positive upper and lower comparison bounds on finite intervals. Differentiation and periodic integration by parts give

\[
 \frac d{dt}\left(\nu\int F_t^\varepsilon\log F_t^\varepsilon
                    +\int H_N^\varepsilon F_t^\varepsilon\right)
 =-\int F_t^\varepsilon
      |\nabla H_N^\varepsilon+\nu\nabla\log F_t^\varepsilon|^2\le0.
 \tag{2.5}
\]

Both initial terms are zero; entropy is nonnegative on the unit-mass space. Heat positivity gives \(H_N^\varepsilon\ge(N-1)g_*/2\). Fixed-\(N\) path passage and local uniform energy convergence, followed by Fatou after this common lower shift, yield

\[
 \mathbb E H_N(X_t)\le0.
 \tag{2.6}
\]

At zero noise, the actual deterministic gradient flow has \(dH_N/dt=-|B|^2\), and averaging its integrable iid initial energy gives (2.6) directly. There is no division by zero and no passage of singular Fisher information. Shifted-energy nonnegativity proves genuine integrability. Permutation symmetry and \(|g|\le g+2|g_*|\) give

\[
 \mathbb E|g(X_1(t)-X_2(t))|\le2|g_*|,
 \qquad\mathbb E(1+\operatorname{dist}(X_1(t),X_2(t))^{-s})\le C,
 \tag{2.7}
\]

uniformly in \(N,\nu,t\). No individual force-square bound is inferred from a total drift square.

Common translations commute with the actual path map, by uniqueness and the difference force. Initial iid Haar is invariant under them, so each one-body marginal is translation invariant. Each nonzero Fourier coefficient of that marginal is zero, by choosing a translation with nontrivial character; density of trigonometric polynomials identifies the probability measure with Haar. Hence

\[
 \mathbb E\eta_N(t)[f]=\int f\,dx
 \tag{2.8}
\]

for every bounded measurable \(f\) and deterministic \(t\). This is exact finite-\(N\) centering. No higher-marginal independence is asserted after time zero.

## 3. Simultaneous source domination and the path supremum

For \(r\ge0\) define \(\|f\|_{\mathcal A_r}=\sum_k(1+|k|)^r|\widehat f(k)|\). Smoothness makes each fixed seminorm finite. The semigroup \(Q_a^\nu\) preserves constants and has multiplier
\(e^{-a(D_k+\nu a_k)}\) on nonzero modes. Let \(A_\nu=\nu\Delta+R\), where \(Rf=-\int f(\cdot+w)D(dw)\), so its multiplier is \(-(D_k+\nu a_k)\). For \(a\ge0\),

\[
 \|Q_a^\nu f\|_{\mathcal A_r}\le\|f\|_{\mathcal A_r},\qquad
 \|A_\nu Q_a^\nu f\|_{\mathcal A_r}\le C(1+\nu_*)\|f\|_{\mathcal A_{r+2}}.
 \tag{3.1}
\]

Here \(D_k\le4\pi^2c_{d,s}\) since \(s+2-d\le0\) and \(|k|\ge1\). Termwise integration of absolutely convergent series proves these statements and time differentiability, also at \(a=0\). In particular all the following families are uniformly smooth, including at zero noise.

We extract an explicitly simultaneous bound from the proof of R16, not from its fixed-test theorem card. To distinguish splitting scale from time, write \(\ell\in(0,1]\). Set \(M=d+2\),

\[
 w_\ell(v)=(1-e^{-v/\ell})^M,\quad\psi_\ell=1-w_\ell,
 \quad g_\ell=A\int_0^\infty v^{\alpha-1}w_\ell(v)(p_v-1)\,dv,
\]
\[
 Q_\ell^{\rm rem}(z)=A\int_0^\infty v^{\alpha-1}\psi_\ell(v)p_v(z)\,dv\ge0,
 \qquad c_\ell=\int Q_\ell^{\rm rem}=C_{d,s,M}\ell^\alpha.
 \tag{3.2}
\]

The notation \(Q_\ell^{\rm rem}\) here is a scalar kernel, distinct from the test semigroup \(Q_a^\nu\). The exact splitting is \(g=g_\ell+Q_\ell^{\rm rem}-c_\ell\) off zero and in Haar \(L^1\). The retained kernel is \(C^2\), with positive Fourier weights
\(a_\ell(k)=A\int_0^\infty v^{\alpha-1}w_\ell(v)e^{-4\pi^2v|k|^2}dv\).
The Gaussian bounds give \(g_\ell(0)\le C\ell^{-s/2}\). Define nonnegative configuration functions

\[
 E_\ell=\tfrac12\sum_{k\ne0}a_\ell(k)|\widehat\eta_N(k)|^2,
 \quad S_\ell=\frac1{2N^2}\sum_{i\ne l}Q_\ell^{\rm rem}(x_i-x_l).
\]

Retaining the exact smooth self subtraction and constant background gives

\[
 \frac{H_N}N=E_\ell+S_\ell-\frac{g_\ell(0)}{2N}
                         -\frac{N-1}{2N}c_\ell,
 \qquad
 \mathbb E(E_\ell+S_\ell)(X_r)le
 C(N^{-1}\ell^{-s/2}+\ell^\alpha).
 \tag{3.3}
\]

The second statement follows from (2.6). It also holds through scale two with a larger fixed constant, as in R16, which is needed for \(S_{2\ell}\). The integrability follows from (2.7) and the exact splitting. Neither nonnegative term is a weighted-positivity assumption.

For a smooth real \(f\), put \(J^f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y))\) off the diagonal and retain exactly

\[
 P_N[J^f]=\frac1{2N^2}\sum_{i\ne l}J^f(x_i,x_l)
             -\frac1N\sum_i\int J^f(x_i,y)dy+\frac12\iint J^f.
 \tag{3.4}
\]

The deterministic R16 estimates have the following uniform content. The radial logarithmic slope of \(a_\ell\) is between zero and \(L=2(\alpha+M)\), independently of \(\ell\). Indeed \(0\le v w_\ell'(v)\le M w_\ell(v)\), and integrating the derivative of \(v^\alpha w_\ell(v)e^{-\lambda v}\), with vanishing endpoints, gives the claimed ratio bound. For nonzero lattice vectors \(k,l\), it implies

\[
 \frac{|k a_\ell(k)-l a_\ell(l)|}{\sqrt{a_\ell(k)a_\ell(l)}}
 \le(1+L)|k-l|(1+|k-l|)^{L/2+1}.
 \tag{3.5}
\]

To see this, put \(u=\min(|k|,|l|)\ge1\), \(v=\max(|k|,|l|)\). Integrating the logarithmic slope gives \(a_\ell(u)/a_\ell(v)\le(v/u)^L\), while integration of its derivative gives \(a_\ell(u)-a_\ell(v)\le L a_\ell(u)(v-u)/u\). Bound the numerator by \(|k-l|a_\ell(u)+v[a_\ell(u)-a_\ell(v)]\) and use \(v/u\le1+|k-l|\).

The retained smooth source has diagonal zero, so its centered full-product formula is legitimate. Symmetrizing the Fourier series, then applying (3.5) and \(\sum_k b_k b_{k-q}\le\sum_k b_k^2\), gives

\[
 |P_N[J_{g_\ell}^f]|\le C\|f\|_{\mathcal A_R}E_\ell,
 \qquad R=\alpha+M+3.
 \tag{3.6}
\]

More explicitly the symmetrized series is
\(-\pi i\sum_{k,l\ne0}[k a_\ell(k)-l a_\ell(l)]\cdot\widehat{\nabla f}(l-k)\widehat\rho(k)\overline{\widehat\rho(l)}\).
The constant is bounded by a fixed multiple of
\(\sum_q|q|(1+|q|)^{L/2+1}|\widehat{\nabla f}(q)|\), hence by the displayed seminorm. The absolutely summable smooth coefficients justify the Fourier manipulation.

For the singular discarded part, direct differentiation of each Gaussian translate proves
\(\operatorname{dist}(z,0)|\nabla p_v(z)|\le C_dp_{2v}(z)\).
The shortest-geodesic mean-value estimate on \(\nabla f\), followed by the substitution \(a=2v\), gives

\[
 |J_{g-g_\ell}^f(x,y)|\le C\|D^2f\|_\infty Q_{2\ell}^{\rm rem}(x-y).
 \tag{3.7}
\]

Inserting this bound into all three terms of (3.4) retains respectively \(S_{2\ell}\), \(c_{2\ell}\), and \(c_{2\ell}/2\). Thus for every collision-free configuration, simultaneously for every smooth real \(f\),

\[
 \boxed{|P_N[J^f](x)|\le C\|f\|_{\mathcal A_R}
                    [E_\ell(x)+S_{2\ell}(x)+c_{2\ell}].}
 \tag{3.8}
\]

This explicit deterministic inequality is the family-uniform step. It was not obtained by taking a supremum of separate expectation bounds. Singular empirical diagonal values are never assigned; only the retained smooth source uses its zero diagonal.

Fix \(h\) from the list and the actual noise \(\nu_N\). By (3.1), (3.8) holds for all \(Q_a^{\nu_N}h\), \(0\le a\le T\), with the same constant. The supremum is measurable: on each collision-free configuration the source is continuous in \(a\), so a countable dense set suffices. With \(\ell=N^{-2/d}\), (3.3) proves

\[
 \sup_{0\le r\le T}\mathbb E\sup_{0\le a\le T}
       |P_N[J^{Q_a^{\nu_N}h}](X_r)|\le C_h N^{-q},
 \qquad q=1-s/d.
 \tag{3.9}
\]

Define the continuous nonlinear term

\[
 E_N^h(t)=\sigma_N\int_0^tP_N[J^{Q_{t-r}^{\nu_N}h}](X_r)\,dr.
 \tag{3.10}
\]

Pathwise continuity follows from positive minimum separation of the actual finite-\(N\) path and the smooth parameter dependence of the tests and their Haar contractions. Taking the time supremum first, using (3.8), and only then expectation and Tonelli gives

\[
 \boxed{\mathbb E\|E_N^h\|_{C([0,T])}
       \le C_h T\sqrt{b_N}\,N^{s/d-1/2}\longrightarrow0.}
 \tag{3.11}
\]

For the vector, sum the finitely many bounds. This is genuine actual-law uniform-path smallness. It does not require a source square or a moment of a singular force gradient. The choice of splitting scale is inserted into already proved estimates after the fixed-\(N\) particle heat passage; it is not an interchange of those limits.

## 4. Exact continuous decomposition with every original term

For fixed terminal \(t\), use \(f_r=Q_{t-r}^{\nu_N}h\), \(0\le r\le t\). The row contraction in (3.4) is

\[
 j_f(x)=\int J^f(x,y)dy=-\int K(x-y)\cdot\nabla f(y)dy
       =-\int f(x+w)D(dw)=Rf(x),\qquad\int j_f=\iint J^f=0.
 \tag{4.1}
\]

Oddness and integrability of \(K\) give the first equality; distributional integration by parts against the smooth test gives the second. At Coulomb it is exactly \(-c_d(f-\int f)\), with both parts of (2.2).

Localize the actual paths on collision-excluded energy sublevels and apply smooth Itô to \(\eta_N[f_r]\). The force sum is exactly

\[
 \frac1{N^2}\sum_{i\ne l}K(X_i-X_l)\cdot\nabla f_r(X_i)
 =\frac1{2N^2}\sum_{i\ne l}J^{f_r}(X_i,X_l)
 =P_N[J^{f_r}]+\eta_N[Rf_r].
 \tag{4.2}
\]

The independent-noise Itô correction is \(\nu_N\eta_N[\Delta f_r]\). There is no cross-particle diffusion trace or force self term. Since
\(\partial_r f_r+\nu_N\Delta f_r+Rf_r=0\) and \(\int f_r=\int h\), the one-body drift cancels exactly.

The genuine source and symmetrized force are bounded by a fixed test seminorm times \(1+\operatorname{dist}^{-s}\). Equation (2.7) makes them integrable in probability times time. Collision stops eventually exceed the fixed terminal time almost surely. Dominated convergence therefore passes their stopped integrals in \(L^1\); bounded test gradients pass the stochastic integrals in \(L^2\) by Itô isometry. The bounded time derivative and endpoint terms pass by dominated convergence as well. This proves, for every deterministic \(t\),

\[
 Z_N^h(t)=I_N^h(t)+M_N^h(t)+E_N^h(t),
 \quad I_N^h(t)=\frac{\sqrt{b_N}}{\sqrt N}\sum_i
                  [Q_t^{\nu_N}h(X_i(0))-\textstyle\int h],
 \tag{4.3}
\]
\[
 M_N^h(t)=\sqrt{\frac{2\nu_Nb_N}{N}}\sum_i\int_0^t
           \nabla Q_{t-r}^{\nu_N}h(X_i(r))\cdot dW_i(r).
 \tag{4.4}
\]

For every fixed \(t\), (4.4) is the terminal value of a true square-integrable martingale in its integration time. As a process of terminal times it is a stochastic convolution, not generally a martingale. A continuous version needs no unstated stochastic Fubini theorem: define it by the continuous process \(Z_N^h-I_N^h-E_N^h\). Equation (4.3) shows equality almost surely at each deterministic time with (4.4), hence this is a version. We use this continuous version throughout. Every pair of deterministic-time moment identities transfers to it. All vector processes are measurable as continuous-path random variables, since their rational-time evaluations are measurable. Set \(Y_N=I_N+M_N=Z_N-E_N\).

For later use, at any fixed terminal tuple \((t_l,h_l)\) the integration-time martingales have the exact cross bracket

\[
 \langle M_{N,i},M_{N,j}\rangle_a
 =2\nu_Nb_N\int_0^{a\wedge t_i\wedge t_j}
    \eta_N(r)[\nabla Q_{t_i-r}^{\nu_N}h_i\cdot
                       \nabla Q_{t_j-r}^{\nu_N}h_j]dr.
 \tag{4.5}
\]

The factor is exactly two; the \(N\) independent Brownian labels cancel the \(1/N\). No deleted-pair factor belongs in this one-body bracket. At zero noise these terms are identically zero on the actual deterministic flow.

## 5. Uniform fourth moments of the continuous linear part

This section proves moment uniformity instead of invoking a martingale tightness theorem. From (3.1), for every fixed seminorm,

\[
 \|(Q_t^\nu-Q_u^\nu)h\|_{\mathcal A_r}
   \le C_h|t-u|,\qquad
 \|\nabla Q_a^\nu h\|_\infty\le C_h,
 \tag{5.1}
\]

uniformly for \(0\le t,u,a\le T\), \(0\le\nu\le\nu_*\). Constants may use two additional derivatives; the tests are fixed smooth functions.

If \(v\) has zero Haar mean, iid preparation gives the exact fourth moment

\[
 \mathbb E\left(\frac{\sqrt b}{\sqrt N}\sum_i v(X_i(0))\right)^4
 =b^2\left[\frac{\int v^4}{N}
          +3\frac{N-1}{N}\left(\int v^2\right)^2\right].
 \tag{5.2}
\]

Only the all-equal label partition and the three pair partitions survive; all partitions with singleton labels have zero mean. Apply this to \((Q_t^{\nu_N}-Q_u^{\nu_N})h\), whose mean is exactly zero, and to \(h-\int h\) at time zero. Since \(b_N\le1\),

\[
 \mathbb E|I_N^h(t)-I_N^h(u)|^4\le C_h|t-u|^4,
 \qquad \sup_N\mathbb E|I_N^h(0)|^4<\infty.
 \tag{5.3}
\]

The following elementary stochastic estimate applies to adapted, non-Gaussian integrands. If a continuous real stochastic-integral martingale \(U\) starts at zero and \(d\langle U\rangle_r\le w(r)dr\) for deterministic nonnegative integrable \(w\), then

\[
 \mathbb E|U_T|^4\le3\left(\int_0^T w\right)^2.
 \tag{5.4}
\]

Indeed stop when \(|U|\) reaches \(R\). Itô's formula and bounded localization give
\(\mathbb E U_{T\wedge\tau_R}^4=6\mathbb E\int_0^{T\wedge\tau_R}U_r^2d\langle U\rangle_r\).
The stopped isometry bounds \(\mathbb E U_{r\wedge\tau_R}^2\le\int_0^r w\). The previous display is therefore at most
\(6\int_0^T w(r)\int_0^r w(v)\,dv\,dr=3(\int w)^2\).
Fatou as \(R\to\infty\) proves (5.4). It does not replace a random bracket by its mean.

For \(t\ge u\), \(\delta=t-u\), the difference in (4.4) is one martingale terminal value with integrand

\[
 \begin{cases}
 \nabla(Q_{t-r}^{\nu_N}-Q_{u-r}^{\nu_N})h(X_i(r)),&0\le r\le u,\\
 \nabla Q_{t-r}^{\nu_N}h(X_i(r)),&u<r\le t.
 \end{cases}
\]

The first is bounded by \(C_h\delta\), the second by \(C_h\), by (5.1). Since \(\nu_Nb_N\le1\), its bracket density is at most
\(C_h[\delta^2\mathbf1_{[0,u]}+\mathbf1_{(u,t]}]\).
Its integral is at most \(C_h(T\delta^2+\delta)\le C_{h,T}\delta\). Thus (5.4) gives

\[
 \mathbb E|M_N^h(t)-M_N^h(u)|^4\le C_{h,T}|t-u|^2.
 \tag{5.5}
\]

In particular the contribution from the earlier interval \([0,u]\), where the terminal test changes, has not been dropped. No independence of this contribution from the recent interval or from the initial vector is required. Using \(|a+b|^4\le8(|a|^4+|b|^4)\) and \(|z|^4\le m\sum_j|z_j|^4\), we conclude, for \(T>0\),

\[
 \boxed{\sup_N\mathbb E|Y_N(0)|^4\le C,
 \qquad \mathbb E|Y_N(t)-Y_N(u)|^4\le C|t-u|^2.}
 \tag{5.6}
\]

Only the smooth linear part is assigned this fourth-moment bound. The singular error requires just (3.11), and no fourth-moment estimate for it is asserted.

## 6. Elementary compactness proof in the uniform topology

First suppose \(T>0\) and rescale its interval to \([0,1]\); the constant in (5.6) changes only with \(T\). Let \(\Delta_n(Y)\) be the maximum of adjacent increments on the dyadic grid of level \(n\). Fix \(0<\gamma<1/4\), for example \(\gamma=1/8\). Markov's inequality and the \(2^n\) intervals give

\[
 \mathbb P(\Delta_n(Y_N)>A2^{-\gamma n})
   \le CA^{-4}2^{-(1-4\gamma)n}.
 \tag{6.1}
\]

The geometric series is summable. Also \(\mathbb P(|Y_N(0)|>A)\le CA^{-4}\). Except on an event of probability at most \(C_\gamma A^{-4}\), all levels satisfy their adjacent-increment bounds and \(|Y_N(0)|\le A\).

On this event continuity and dyadic chaining give
\(|Y_N(t)-Y_N(u)|\le C_\gamma A|t-u|^\gamma\).
For detail, choose \(n\) with \(2^{-(n+1)}<|t-u|\le2^{-n}\). The level-\(n\) lower dyadic approximants differ by at most two grid edges. Each approximation to an endpoint changes by at most one edge at each finer level. Sum two coarse edges and two copies of \(\sum_{k>n}A2^{-\gamma k}\); continuity identifies the limiting endpoints. The geometric sum is at most \(C_\gamma A2^{-\gamma n}\le C'_\gamma A|t-u|^\gamma\).

The set of paths with this Hölder bound and initial bound is compact in uniform norm. It is closed; the bounds give equicontinuity and uniform boundedness. To verify compactness directly, approximate every path by its values on one sufficiently fine grid and quantize those bounded values in a finite net. Piecewise-linear interpolation gives a finite uniform net for the path set. It is therefore totally bounded and, being closed in the complete uniform-norm space of continuous paths, is compact. This proves uniform tightness of \(Y_N\) without a probability compactness theorem.

Now transfer tightness to the actual \(Z_N\). Write
\(w_z(\delta)=\sup_{|t-u|\le\delta}|z(t)-z(u)|\). Equation (3.11) implies

\[
 w_{Z_N}(\delta)\le w_{Y_N}(\delta)+2\|E_N\|_\infty,
 \qquad \|E_N\|_\infty\longrightarrow0\quad\hbox{in probability}.
 \tag{6.2}
\]

A fixed-radius neighborhood of a compact set need not be compact here, so that invalid shortcut is not used. Instead construct compact sets as follows. Given \(\varepsilon>0\), choose tolerances \(e_j=2^{-j}\) and probabilities \(p_j>0\) with \(\sum_jp_j<\varepsilon/2\). For each \(j\), (3.11) and Markov give an integer \(N_j\) such that
\(\mathbb P(2\|E_N\|_\infty>e_j/2)<p_j/2\) for every \(N\ge N_j\).
The already proved tight Hölder bounds choose a small \(\delta_j\) with
\(\sup_N\mathbb P(w_{Y_N}(\delta_j)>e_j/2)<p_j/2\).
For the finitely many \(2\le N<N_j\), actual path continuity gives
\(w_{Z_N}(\delta)\to0\) almost surely as \(\delta\downarrow0\); bounded convergence of the indicators after a fixed positive threshold makes each probability tend to zero. Shrink \(\delta_j\) further so these finitely many probabilities are below \(p_j\), and so \(\delta_j\downarrow0\). Then

\[
 \sup_{N\ge2}\mathbb P(w_{Z_N}(\delta_j)>e_j)<p_j.
 \tag{6.3}
\]

Since \(E_N(0)=M_N(0)=0\), (5.3) chooses \(R\) with \(\sup_N\mathbb P(|Z_N(0)|>R)<\varepsilon/2\). The closed set
\(\{|z(0)|\le R,\ w_z(\delta_j)\le e_j\text{ for all }j\}\)
is equicontinuous and bounded (cover the finite interval by finitely many intervals of length \(\delta_1\)). The same finite-grid proof makes it compact. The union bound and (6.3) give probability at least \(1-\varepsilon\) for every \(N\). This proves full tightness of the actual laws in precisely \(C([0,T],\mathbb R^m)\).

## 7. Construction of the continuous possibly degenerate Gaussian process

Take a real orthonormal mean-zero trigonometric basis \((e_l)\): for one representative of each pair \(\{k,-k\}\), use \(\sqrt2\cos(2\pi k\cdot x)\) and \(\sqrt2\sin(2\pi k\cdot x)\). Assign both its \(a_l,D_l,L_l\) from that frequency. Let \(h_{j,l}=\int h_je_l\). Smoothness implies
\(\sum_l|h_{j,l}|(1+|k_l|)^p<\infty\) for every fixed \(p\).
On a countable product probability space choose independent standard real normals \(\xi_l\) and standard real Brownian motions \(B_l\), independent of the normals. Put

\[
 G_l(t)=\sqrt{\bar b}\left[e^{-L_lt}\xi_l
           +\sqrt{2\bar\nu a_l}\int_0^t e^{-L_l(t-r)}dB_l(r)\right],
 \qquad Z_j(t)=\sum_l h_{j,l}G_l(t).
 \tag{7.1}
\]

This series converges absolutely uniformly almost surely, with tails tending to zero in expected uniform norm. Here is an explicit bound. Deterministic-kernel integration by parts gives

\[
 \int_0^t e^{-L(t-r)}dB_r=B_t-L\int_0^t e^{-L(t-r)}B_rdr,
 \quad \sup_{t\le T}\left|\int_0^t e^{-L(t-r)}dB_r\right|
       \le2\sup_{t\le T}|B_t|.
 \tag{7.2}
\]

The elementary \(L^2\) maximum bound is \(\mathbb E\sup|B|^2\le4T\). One proof first uses a finite time grid and its first crossing of level \(\lambda\): conditional Jensen, summed over the finitely many possible first-crossing times, gives the submartingale inequality below. Continuity then passes through increasing dyadic grids. Thus
\(\lambda\mathbb P(B^*\ge\lambda)\le\mathbb E[|B_T|1_{\{B^*\ge\lambda\}}]\).
Integration for \(0\le\lambda\le R\), followed by Cauchy–Schwarz, bounds \(\mathbb E(B^*\wedge R)^2\le4\mathbb E B_T^2\); monotone convergence removes \(R\). Thus (7.2) gives

\[
 \mathbb E\sup_{t\le T}|G_l(t)|\le C_T(1+\sqrt{a_l}).
 \tag{7.3}
\]

The summed bound is finite by smoothness. Tonelli implies absolute uniform convergence almost surely, and the same majorant gives convergence of tails in expected supremum. Every partial sum is continuous, hence \(Z\) is a continuous random vector process. No distribution-valued field claim is made.

Each finite set of evaluations of a partial sum is centered Gaussian. Its covariance series converges absolutely; the series also converges in \(L^2\) at each evaluation by independence and square summability. Characteristic functions therefore give a centered Gaussian vector at every finite tuple, including singular covariance matrices. This proves Gaussianity of the process and its zero mean without assuming nondegeneracy.

Independence and the Itô isometry give

\[
 \mathbb E G_l(t)G_l(u)=\bar b\left[e^{-(t+u)L_l}
 +2\bar\nu a_l\int_0^{t\wedge u}e^{-(t+u-2r)L_l}dr\right]
 =\bar b\left[\frac{D_l}{L_l}e^{-(t+u)L_l}
 +\frac{\bar\nu a_l}{L_l}e^{-|t-u|L_l}\right].
 \tag{7.4}
\]

Combining the two real basis functions for each opposite-frequency pair gives exactly (1.4), with no extra two. Equivalently the covariance is the sum of the initial Haar Gram term and the time-space gradient Gram term

\[
 \bar b\int(Q_t^{\bar\nu}h_i-\textstyle\int h_i)
                   (Q_u^{\bar\nu}h_j-\textstyle\int h_j)dx
 +2\bar\nu\bar b\int_0^{t\wedge u}\int
   \nabla Q_{t-r}^{\bar\nu}h_i\cdot\nabla Q_{u-r}^{\bar\nu}h_j\,dx\,dr.
 \tag{7.5}
\]

It is positive semidefinite by construction. For completeness its increment variance is at most \(C|t-u|\): use (5.1) on the initial term and split the stochastic integral into its old and recent intervals as in Section 5, now with deterministic integrands. Centered Gaussian fourth moments are three times variance squared; this identity follows by four differentiations of its elementary Gaussian characteristic function. Thus the process also satisfies the vector fourth-moment criterion of Section 6 and its law is tight in that same space. Its continuous law is uniquely determined by its finite-dimensional laws: piecewise-linear dyadic approximations converge to each continuous path uniformly, and their laws depend only on finite tuples of evaluations.

## 8. Identification of all finite-dimensional laws, with dependence retained

The full conditional R18 argument applies to each fixed tuple selected from the tests and times. For recoverability, the complete probability mechanism needed here follows. Its law estimate needs only R10 Sections 2–3, not any pair inverse.

The positive heat-integral truncation
\(g^{>\ell}=A\int_\ell^\infty r^{\alpha-1}(p_r-1)dr\)
has weights \(\widetilde a_\ell(k)>0\), self value at most \(C\ell^{-s/2}\), and
\(g\ge g^{>\ell}-A\ell^\alpha/\alpha\) off zero. Exact self subtraction gives

\[
 H_N\ge\frac N2\sum_{k\ne0}\widetilde a_\ell(k)|\widehat\eta_N(k)|^2
       -\frac12g^{>\ell}(0)-\frac{N-1}{2\alpha}A\ell^\alpha.
 \tag{8.1}
\]

At \(\ell=N^{-2/d}\), use (2.6). For \(|k|\le N^{1/d}\), integrate the weight over \([|k|^{-2},2|k|^{-2}]\) to get \(\widetilde a_\ell(k)\ge c|k|^{s-d}\). For higher modes use \(|\widehat\eta_N|\le1\). Hence

\[
 \mathbb E|\widehat\eta_N(r,k)|^2\le\min(1,CN^{-q}|k|^{d-s}),
 \quad\mathbb E|\rho_N(r)[\psi]|\le CN^{-q/2}\|\psi\|_{\mathcal A_\alpha}.
 \tag{8.2}
\]

The second follows from absolutely convergent Fourier sums and Cauchy–Schwarz in probability. It applies to any deterministic family with that seminorm uniformly bounded. Since
\(\|v\cdot w\|_{\mathcal A_\alpha}\le\|v\|_{\mathcal A_\alpha}\|w\|_{\mathcal A_\alpha}\),
all products of backward-test gradients in (4.5) qualify, uniformly in time and bounded noise.

For a fixed tuple \((t_l,h_l)\), let \(I_N\) be the initial vector in (4.3), and let \(\mathcal M_N(a)\) be its vector of integration-time martingales stopped at their respective terminal times. Its terminal vector is the corresponding vector of stochastic convolutions. For a fixed real coefficient vector \(v\), the scalar martingale \(U_N=v\cdot\mathcal M_N\) has bracket bounded deterministically by a constant \(K_v\). Equation (8.2), Tonelli and (4.5) give

\[
 \mathbb E|\langle U_N\rangle_T-v^TBv|
       \le C_v(N^{-q/2}+|\nu_N-\bar\nu|)\longrightarrow0,
 \tag{8.3}
\]

where \(B\) is the thermal Gram matrix in (7.5). To justify the deterministic noise replacement, the Fourier mean-value bound is
\(\|(Q_a^{\nu_N}-Q_a^{\bar\nu})h\|_{\mathcal A_r}
\le4\pi^2a|\nu_N-\bar\nu|\|h\|_{\mathcal A_{r+2}}\),
and \(\nu b(\nu)=\min(\nu,1)\) is Lipschitz. No convergence rate is needed.

Let \(V_l=\sqrt{\bar b}(Q_{t_l}^{\bar\nu}h_l-\int h_l)\), and set
\(\bar I_N=N^{-1/2}\sum_iV(X_i(0))\), with covariance matrix \(A_{ij}=\int V_iV_j\).
The difference of each triangular initial test and \(V_l\) has zero Haar mean and \(L^2\) norm at most \(C|\nu_N-\bar\nu|\): \(\sqrt{b(\nu)}\) is Lipschitz, also across one. Initial independence makes the variance of the normalized difference sum exactly that squared \(L^2\) norm. Therefore
\(\mathbb E|I_N-\bar I_N|\le C|\nu_N-\bar\nu|\), without a factor \(\sqrt N\).
For each \(v\), the bounded summand Taylor expansion is

\[
 \mathbb E e^{iv\cdot V(X_1)/\sqrt N}
 =1-\frac{v^TAv}{2N}+O_v(N^{-3/2}).
\]

Taking the \(N\)-th power proves convergence of the initial characteristic function to \(e^{-v^TAv/2}\).

There is no finite-\(N\) independence assumption between the initial vector and martingale. With \(\mathcal F_{N,0}\) including the initial particles, the process

\[
 \exp(iU_N(a)+\tfrac12\langle U_N\rangle_a)
 \tag{8.4}
\]

is a true complex martingale: Itô cancels its drift with the **positive** compensator, and its modulus and stochastic-integral square norm are bounded using \(K_v\). Its conditional expectation at \(T\), given \(\mathcal F_{N,0}\), is one. Multiplying by any \(\mathcal F_{N,0}\)-measurable \(W_N\) with \(|W_N|\le1\), replacing the compensator by \(v^TBv\), and using the mean-value bound of the exponential on \([0,K_v]\), yields

\[
 \left|\mathbb E(W_Ne^{iU_N(T)})-e^{-v^TBv/2}\mathbb EW_N\right|
 \le C_v\mathbb E|\langle U_N\rangle_T-v^TBv|.
 \tag{8.5}
\]

Take \(W_N=e^{iv\cdot I_N}\) and use (3.11). The characteristic function of the actual tuple tends to \(e^{-v^T(A+B)v/2}\), exactly that of the evaluations of (7.1).

This yields finite-dimensional weak convergence without a hidden nondegeneracy or compactness assumption. The linear tuple has uniformly bounded second moments from initial iid variance and deterministic bracket bounds; its tails are uniformly small. Convolve its law and the target Gaussian law with an independent Gaussian of covariance \(\varepsilon I\). Fourier inversion of the elementary Gaussian integral expresses their densities as inverse transforms of the characteristic functions multiplied by \(e^{-\varepsilon|v|^2/2}\). This factor is integrable, so dominated convergence gives uniform convergence of the convolved densities. On a large compact ball integrate bounded Lipschitz tests using that convergence; outside use the uniform second-moment tails. Coupling with the added Gaussian changes each Lipschitz expectation by at most its Lipschitz constant times \(\sqrt\varepsilon\mathbb E|G|\). Send \(N\to\infty\), then \(\varepsilon\downarrow0\). The source error tends to zero in \(L^1\), so it transfers bounded Lipschitz convergence to the actual tuple and preserves tightness by Markov's inequality. Compact-ball uniform approximation by Lipschitz functions then proves convergence for bounded continuous tests. The same conclusion includes zero and singular covariance matrices.

## 9. Uniform-topology weak convergence, without an unproved subsequence theorem

Let \(P_nz\) be piecewise-linear interpolation of a continuous vector path on the dyadic grid of \([0,T]\). It is a continuous function of a finite tuple and
\(\|P_nz-z\|_\infty\le w_z(T2^{-n})\).
For a bounded Lipschitz functional \(F\) on path space, any \(e>0\) gives

\[
 |\mathbb EF(Z_N)-\mathbb EF(P_nZ_N)|
 \le\operatorname{Lip}(F)e+2\|F\|_\infty
                    \mathbb P(w_{Z_N}(T2^{-n})>e).
 \tag{9.1}
\]

The probability is uniformly small as \(n\to\infty\) by the actual compact sets constructed in Section 6 (equicontinuity on a compact set gives that statement directly). The same holds for \(Z\), by its continuous tight law in Section 7. At fixed \(n\), Section 8 applies to the grid tuple and proves
\(\mathbb EF(P_nZ_N)\to\mathbb EF(P_nZ)\).
Use (9.1), then send \(n\to\infty\) and \(e\downarrow0\). This proves convergence for all bounded Lipschitz path functionals.

It also proves the usual weak convergence for every bounded continuous path functional. Indeed actual tightness and target tightness supply one common compact set with arbitrarily high probability (take the union of their two compact sets). On that compact set a bounded continuous \(F\) is uniformly continuous. It can be uniformly approximated there by bounded globally Lipschitz functions: the functions
\(F_L(x)=\inf_{y\in K}[F(y)+L\|x-y\|_\infty]\), clipped to the bounded range of \(F\), have this property as \(L\to\infty\). To check it, split \(y\) at a uniform-continuity distance \(\delta\); for farther points \(L\delta\) exceeds the possible oscillation, while nearer points change \(F\) by at most its modulus. The error outside the compact set is bounded by twice the uniform bound times its probability. Let the Lipschitz approximation error and that probability vanish. This completes weak convergence in exactly the asserted uniform-norm space, without treating finite-dimensional convergence as tightness and without an unstated Prokhorov application.

## 10. Edges, independent falsification, and hostile self-review

At \(T=0\), path space is canonically \(\mathbb R^m\). Source and thermal integrals vanish, and the iid Taylor argument in Section 8 proves the assertion directly. The Gaussian series is evaluated at zero. No dyadic rescaling of a zero interval occurs.

If \(\nu_*=0\), every dynamics is the actual deterministic gradient flow, \(b_N=1\), the martingale is zero, and the Gaussian path randomness comes solely from the initial normals in (7.1). If only \(\bar\nu=0\), all thermal terms of the limit vanish directly; the uniform bounds remain valid for the entire sequence, including exactly zero terms and arbitrarily slow noise convergence. At \(\bar\nu>0\) the thermal term stays. The kink at \(\nu=1\) causes no loss because the two elementary Lipschitz functions used above remain Lipschitz across it.

Constant tests give zero actual fluctuations, source, gradients and all limiting coordinates exactly. Repeated times, repeated tests and any linear dependence require no inverse covariance. The Gram representation and series construction permit all degeneracies. For example a linear combination of the fixed tests which is constant vanishes as a whole path both before and after the limit. A zero variance at an individual tuple is handled by the same Gaussian construction.

The two exponent restrictions are simultaneous: the admissible Coulomb endpoint in this card is three-dimensional Coulomb. Four-dimensional Coulomb has \(s=d/2\) and is excluded; no smallness is claimed there. All higher admissible dimensions remain below Coulomb or otherwise within both stated inequalities. The positive-power logarithmic exclusion is retained; no substitution \(s=0\) occurs.

The construction route uses positive source domination and fourth moments. A distinct falsification route challenges path information and the claimed limit through exact narrow-spike examples and solvable modal dynamics.

**Each-time smallness cannot justify a path supremum.** On \([0,1]\), choose uniformly one of \(n\) disjoint intervals \([j/n,(j+1)/n]\), and on that interval place a continuous tent of height one with its peak at the midpoint, zero elsewhere. At each fixed time the expected absolute value is at most \(1/n\). Every sample path has supremum one, and its modulus at \(1/(2n)\) is one. For every fixed positive \(\delta\), sufficiently large \(n\) therefore have modulus at least one with probability one. These laws are not tight in \(C\), despite each-time \(L^1\) convergence. This is an exact counterexample to a proof inference, not an admitted particle counterexample. It motivates the simultaneous deterministic bound (3.8), which genuinely rules out such an error for the actual remainder by (3.11).

**The entire modal convolution must be retained.** A single real modal fluctuation obeys the solvable Gaussian equation
\(dG=-LGdt+\sqrt{2\bar\nu\bar b a}\,dB\), with independent initial variance \(\bar b\), where \(L=D+\bar\nu a\), \(D>0\). Direct integration yields (7.4). For \(t>u\), subtracting its two convolution formulas leaves both the earlier-noise contribution \((e^{-L(t-u)}-1)\int_0^u e^{-L(u-r)}dB_r\) and the recent-noise integral. When \(\bar\nu a>0\) and \(u>0\), the earlier contribution has strictly positive variance. Calling the moving-terminal convolution a martingale and dropping this term fails this solvable-model test. Section 5 keeps it and bounds it by a squared terminal-time increment.

The same modal model has right increment-variance derivative \(2\bar\nu\bar b a\) at every time. At zero noise the derivative is zero and increments have a squared time scale. Initial damping alone would miss the positive-noise derivative; replacing the initial time sum by a time difference would incorrectly make its transient initial contribution stationary. The fresh exact diagnostic tests these coefficients separately.

**A bracket mean does not make an adapted martingale Gaussian.** Let \(B\) be real Brownian motion and put \(U=B_1+c(B_1)(B_2-B_1)\), with \(c=2\) on \(B_1>0\) and \(c=1\) otherwise. Its bracket has mean \(7/2\) and deterministic upper bound five. Symmetry of the Gaussian even moments gives \(\mathbb EU^4=87/2\), whereas \(3(\mathbb E\langle U\rangle)^2=147/4\). The latter replacement is false; (5.4) correctly only gives the upper bound \(75\). This is a probability-inference test, not a different law offered as a particle counterexample. Section 8 uses actual bracket concentration and a conditional exponential instead.

| Strongest-claim challenge | Resolution and limitation |
|---|---|
| Could source constants vary with terminal time or with \(N\)-dependent backward tests? | (3.8) is deterministic for all smooth tests with an explicit seminorm, and (3.1) bounds that seminorm for the whole family. No card-level family extension is presumed. |
| Does a singular value on the empirical diagonal enter? | The original source always deletes labels. Only the retained \(C^2\) kernel uses its zero source diagonal and its nonzero energy self subtraction. |
| Does finite-dimensional convergence supply path compactness? | Sections 5–6 prove actual uniform-topology tightness independently; the tent family disproves the shortcut. |
| Is the stochastic convolution silently a martingale in terminal time? | It is treated as a martingale terminal value only after fixing each increment or tuple. Its common-history increment is explicit. |
| Are fourth moments under the interacting law inferred from iid data? | Iid fourth moments are used only at time zero. Dynamic fourth moments use bounded adapted gradients and (5.4), with deterministic bracket-density bounds. |
| Can the source's vanishing sup error be used as a compact neighborhood? | No. Section 6 constructs actual modulus compact sets and handles the finitely many small \(N\) by actual continuity. |
| Does the continuous Gaussian process only exist formally as a covariance? | (7.1) converges absolutely in path supremum almost surely and in expected tails. |
| Are sources silently certified, or unseen references imported? | The full source premises remain conditional as issued. R10's extra corrector premises and R18's R17 comparison are nondependencies. |
| Are source squares, inverse temperatures or a convergence rate hidden? | No source square is used, zero noise is direct, and all replacements use \(|\nu_N-\bar\nu|\) without multiplying by \(\sqrt N\). |

No admitted counterexample was found. Subject to the exact conditional sources, Sections 2–9 rule out every component of the frozen negation. They do not assert that an independent audit has excluded it. The broader campaign, distribution-valued topology, growing test families, exponents outside the card, unbounded noise, other preparations, logarithmic interaction, inhomogeneity and higher hierarchy remain outside this result. The old energy-floor condition, full microscopic subcriticality and finite positive microscopic criticality remain distinct.

## 11. Diagnostic, dispositions, and sealed handoff

The fresh standard-library program `ROUND_020_CONTINUOUS_PATH_ARTIFACTS/round020_path_diagnostic.py` was written without reading any prior checker. It uses exact fractions and finite exponential polynomials, no random samples, floating-point tolerance or installed dependencies. Its JSON result records each category, assertion count, explicit nonzero mutation witness, and the program digest. The executed result is **PASS: 4,255 exact assertions in 26 categories, including 13 nonvacuous mutation controls, all rejected as intended.** The supporting tests concern coefficients and invalid probability inferences; the analytic proof above establishes singular actual-law estimates and path convergence.

The test battery independently assembles modal covariance from the initial-plus-noise integral and from the frozen formula; checks zero/positive noise, zero/repeated times, cross-test polarizations and the factor two; derives the modal small-increment coefficients as formal exact series; retains the old-noise part of a stochastic convolution; enumerates the iid fourth moment on finite centered distributions; checks the exact narrow-tent supremum/modulus obstruction; and rejects using a mean bracket as a fourth-moment identity. Every deliberately mutated claim has a concrete witness. The README and result JSON contain the executed command and exact outcome.

| Assertion or route | Disposition at this handoff |
|---|---|
| Entire THM042, unchanged scope and topology | CONDITIONAL PROVED CANDIDATE, including genuine singular identity, exact centering, expected uniform source smallness, actual tightness, continuous Gaussian existence and weak convergence. |
| Simultaneous source-family consequence | PROVED HERE from the explicit deterministic full R16 argument, not inferred from a fixed-time card. |
| Each-time-error-to-path-tightness inference | DISPROVED by the exact tent family; not used. |
| Terminal-time-martingale shortcut | DISPROVED by the solvable nonzero-drift modal convolution; not used. |
| Entire frozen negation | Excluded by the conditional construction when its stated full-source premises hold; no unconditional certification or admitted counterexample assigned. |
| Earlier sources and their issued statuses | Preserved byte-for-byte; no promotion by this constructor. |
| Required independent whole reconstruction and hostile gates | PENDING ROOT ARRANGEMENT. This lane's tests and self-review are not those gates. |

Only this memorandum, its unique artifact directory and sibling archive/seals were created beyond the exact authorized input overlay. The packet includes the entire proof, exact fourteen input byte strings, their manifest, source/exposure map, new program and results, README, output hashes and a safe verifier. The archive is checked for exact membership, safe relative paths, absence of links or duplicate members, every byte digest and agreement with the on-disk packet, then its digest and verification are recorded in the sibling seal. Issued files are made read-only; corrections require a separately issued superseding artifact.

No canonical ledger, cumulative memorandum, historical input, other worktree output or remote was edited. No external search, state/history/memory lookup, previous audit/checker, child agent, dependency installation, commit, push, publication or author contact occurred. Ambient instructions and their automatically supplied high-level memory summary were unavoidable exposure and were not used as mathematical inputs. Filename-only worktree status was inspected to preserve the prescribed input overlay; no non-allowlisted content was opened.

The exact next action is a fresh whole-claim reconstruction of THM042 from its approved dossier, and a separate isolated hostile review of this complete proof and sealed packet. Root alone integrates canonical ledgers and assigns gate status. There is no remaining local path-estimate gap in the conditional construction; source validation and the two independent gates remain explicit prerequisites to promotion. This ends the authorized sealed bounded handoff, not the campaign.
