# Round 024 — actual Coulomb dynamics: a two-time correlation reduction

TASK-103, 2026-09-18 UTC. Fresh worker /root/r024_threshold_falsification, at base 4ab1d492c3bb9bb3537732f2d75502971f5ee6da in the assigned isolated worktree. **THM-046 / PO-033 remains OPEN. No admitted negation has been proved.** The result here is a complete finite-N reduction to a specified actual dynamic correlation estimate, together with two disproved closure shortcuts. The reduction and diagnostic are **SELF-CHECKED**, not independently certified. No current constructor narrative, TASK-102 output, Round-023 construction/audit, canonical state/history, memory file, other worktree, external source, or previous checker was read.

The instantaneous source has infinite second moment at the admitted iid initial law for a fixed smooth test. Its time integral, however, is square integrable at every fixed particle number by a stopped one-body identity. Its possible smallness is reduced below to bounded, two-time observables and then an exact two-/three-label correlation remainder. No pair inverse is constructed or used.

## 1. Frozen target and source preflight

Set \(c=4\pi^2\), on the unit Haar torus \(\mathbb T^4\), with characters \(e_k(x)=e^{2\pi i k\cdot x}\). The coefficient-one periodic Coulomb potential has

\[
 \widehat g(0)=0,\quad \widehat g(k)=|k|^{-2}\ (k\ne0),\quad K=-\nabla g,
 \qquad \operatorname{div}K=c(\delta_0-dx).
 \tag{1.1}
\]

For finite \(N\ge2\), use the actual singular process

\[
 dX_i=N^{-1}\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu_N}\,dW_i,\qquad
 X(0)\sim dx^{\otimes N},\qquad \nu_N=\beta_N^{-1}>0,
 \tag{1.2}
\]

with initial vector independent of the drivers. The admitted sequence satisfies
\(\lambda_N=\beta_NN^{-1/2}\to\lambda\in(0,\infty)\).
Put \(b_N=\min(\beta_N,1)\) and \(\sigma_N=\sqrt{Nb_N}\); eventually \(b_N=1\) and \(\nu_N=\lambda_N^{-1}N^{-1/2}\). Fix finite \(T\ge0\) and real \(h\in C^\infty(\mathbb T^4)\). The prescribed response is \(f_t=Q_{T-t}^{\nu_N}h\), where

\[
 Q_t^\nu e_k=e^{-(c+\nu\ell_k)t}e_k\quad(k\ne0),\qquad
 \ell_k=4\pi^2|k|^2,\qquad Q_t^\nu1=1.
 \tag{1.3}
\]

For \(J^f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y))\), retain

\[
 P_N[J^f]=\frac1{2N^2}\sum_{i\ne j}J^f(X_i,X_j)
 -\frac1N\sum_i\int J^f(X_i,y)dy+\frac12\iint J^f(x,y)dxdy.
 \tag{1.4}
\]

THM-046 is

\[
 \sigma_N\mathbb E|I_N(h,T)|\longrightarrow0,\qquad
 I_N(h,T)=\int_0^T P_N[J^{f_t}](X(t))dt.
 \tag{1.5}
\]

Its **exact negation** is an admitted fixed \(T,h,\lambda>0\) and an admitted sequence for which the left side has positive limsup. The absolute value is after integration. A static law, a changing test or horizon, a signed expectation, or failure of a stronger variance estimate is not that negation.

All 20 paths in the supplied input manifest passed SHA-256 verification before substantive use; their complete byte copies are in the packet. The exact reading exposure is recorded separately.

| Permitted complete source proof and location | Use and limitation |
|---|---|
| Frozen R1 model; R1 algebra, Sections 1–2 | Ordered labels, denominator \(N^2\), half factor, original centering, smooth one-body identity. The singular passage is proved below. |
| R4 response, Sections 2–3 | Heat normalization, coefficient-one local singularity, \(K\in L^1\), Coulomb atom and compensation. |
| R6 particle realization, complete Sections 3–8 | Noncollision, measurability, fixed-N same-noise heat passage, full-drift energy equality, density bound \(F_t\le e^{c(N-1)t}\). The last is used only at fixed N. |
| R10 actual-law falsification, complete Sections 2–4 | Actual energy sign, explicit floor \(H_N\ge-C\sqrt N\), labeled displacement argument. Their mechanisms are restated below. |
| R16 source extension, entire proof, especially Sections 2–7 | Genuine source integrability and \(\mathbb E|P_N[J^{f_t}]|\le C_hN^{-1/2}\), with an explicit fixed Fourier seminorm. Its bounded threshold conclusion is not promoted to smallness. |
| R5 homogeneous interface, actual Fourier-test proof | Response sign and smooth-test seminorms. No auxiliary pair-inverse conclusion is used. |
| R8 scope and Sections 10–11 | Boundary comparison: a finite-N pair identity supplies no uniform threshold estimate. Corrector regularity is not an input here. |
| R12 entire proof; R14 Sections 1–2 | Boundary nondependencies: R12 needs \(s(d-2-s)>0\); R14 needs \(1<q<d-s-1\). Here these become zero and \(1<q<1\). No extension by continuity. |
| R5 base/conditional inverse and clarifications; R7/R11 stated scopes | Examined for source boundaries; their inverse/gradient results are not used below. |

Historical audit references in permitted texts are not new proof evidence. No external theorem, citation, novelty claim, installation, commit, push, or canonical edit occurs.

## 2. Singular passages and actual-law facts

The permitted R4 heat proof specializes to

\[
 g(z)=c\int_0^\infty(p_u(z)-1)du,\qquad
 g(z)=|z|^{-2}+H(z),\qquad K(z)=2z|z|^{-4}-\nabla H(z)
 \tag{2.1}
\]

locally, with \(H\) smooth. The Fourier integral is \(c/(4\pi^2|k|^2)=|k|^{-2}\). The central Euclidean Gaussian integral has coefficient one; the other lattice terms have exponentially small small-time derivative bounds, and the large-time remainder is integrable after differentiation. The flux of \(2z|z|^{-4}\) is \(2|\mathbb S^3|=c\). Zero Fourier mass supplies the constant compensation in (1.1). The punctured divergence is \(-c\), while \(\Delta g=c\) only off zero. Those statements are never interchanged.

Let

\[
 H_N=N^{-1}\sum_{i<j}g(x_i-x_j),\qquad B=-\nabla H_N,\qquad
 H_N-(N-1)g_*/2\ge0,\quad g_*=\inf g>-\infty.
 \tag{2.2}
\]

Every energy sublevel is compact away from every partial collision: each shifted pair term is nonnegative and diverges at its own collision. Smooth cutoff Picard solutions patch uniquely until energy exits. On the stopped collision-free compact sets, Itô gives the complete drift square and

\[
 \Delta_{4N}H_N=c(N-1),\qquad
 dH_N=-\sum_i|B_i|^2dt+\nu c(N-1)dt+
             \sqrt{2\nu}\nabla H_N\cdot dW.
 \tag{2.3}
\]

The expected shifted energy bounds the probability of reaching height \(R\) by
\([\mathbb E(H_N(0)-(N-1)g_*/2)+\nu c(N-1)T]/R\).
The complete R6 Sections 4–5 then give global noncollision, integrability of the total-force square, and \(L^2\) passage of its martingale. Since \(\mathbb EH_N(0)=0\),

\[
 \mathbb EH_N(X(T))+\mathbb E\int_0^T\sum_i|B_i|^2dt
 =\nu c(N-1)T.
 \tag{2.4}
\]

There is no individual force-square claim. The punctured identity in (2.3) is used only along separated paths; no atom is evaluated on a particle diagonal.

A realized finite-horizon singular path has a positive minimum pair distance. Same-noise heat approximation converges uniformly along it by local \(C^1\) force convergence and Gronwall. For the heat flow,
\(\operatorname{div}K_\varepsilon=c(p_\varepsilon-1)\) gives
\(\operatorname{div}_{4N}B^\varepsilon\ge-c(N-1)\).
The smooth-flow Jacobian bound, passage against continuous tests, and Borel approximation in R6 Sections 7–8 prove

\[
 F_t\le e^{c(N-1)T},\qquad 0\le t\le T.
 \tag{2.5}
\]

This is finite at fixed \(N,T\), and justifies first-force weak passages. It is never a uniform-in-N estimate.

The actual sign \(\mathbb EH_N(X(t))\le0\) has a separate argument. At fixed heat cutoff, smooth density bounds justify

\[
 \frac d{dt}\left(\nu\int F^\varepsilon\log F^\varepsilon+
                       \int H_N^\varepsilon F^\varepsilon\right)
 =-\int F^\varepsilon|\nabla H_N^\varepsilon+
                         \nu\nabla\log F^\varepsilon|^2\le0.
 \tag{2.6}
\]

The initial entropy and energy vanish and entropy is nonnegative. Same-noise convergence and the common lower bound \(H_N^\varepsilon\ge(N-1)g_*/2\) allow Fatou to give the singular energy sign. Uniqueness and permutation equivariance give exchangeability; common translations make every one-body marginal Haar. Therefore

\[
 \mathbb E|g(X_1(t)-X_2(t))|\le2|g_*|,\qquad
 \mathbb E|J^{f_t}(X_1(t),X_2(t))|\le C_h.
 \tag{2.7}
\]

The source bound follows from \(|J^{f_t}(x,y)|\le C_h(1+|x-y|^{-2})\) and (2.1). It proves absolute integrability before any covariance calculation. A bounded current or initial test may multiply this source. The needed seminorms of \(f_t\) are uniform for bounded \(\nu\) by (1.3), which covers the eventual critical sequence.

## 3. Exact nonsingular endpoint reduction

Oddness and integrability of \(K\), followed by distributional integration by parts against the smooth test, give

\[
 A_f(x):=\int J^f(x,y)dy
 =-\int f(x+z)\operatorname{div}K(dz)
 =-c\left(f(x)-\int f\right),\qquad \iint J^f=0.
 \tag{3.1}
\]

Both the atom and its constant compensation remain. In particular constants have zero response. No singular diagonal value is assigned.

Apply Itô to \(N^{-1}\sum_i f_t(X_i(t))\) up to an energy exit. Pairing orientations gives exactly

\[
 N^{-2}\sum_{i\ne j}K(X_i-X_j)\cdot\nabla f_t(X_i)
 =(2N^2)^{-1}\sum_{i\ne j}J^{f_t}(X_i,X_j).
 \tag{3.2}
\]

Use \(\partial_t f_t+\nu\Delta f_t-c(f_t-\int h)=0\) and all contractions in (3.1). The integrated result is

\[
 I_N(h,T)=\rho_T[h]-\rho_0[Q_T^\nu h]-M_N(h,T),
 \quad \rho_t=N^{-1}\sum_i\delta_{X_i(t)}-dx,
\]
\[
 M_N(h,T)=\frac{\sqrt{2\nu}}N\sum_i\int_0^T
                       \nabla f_t(X_i(t))\cdot dW_i(t).
 \tag{3.3}
\]

Here is the stop removal. The endpoints are bounded; the grouped drift terms have finite expected absolute integral by (2.7); the martingale integrands are bounded. Stopped martingales converge in \(L^2\) by isometry, and noncollision exhausts each path. The identity passes in \(L^1\) and pathwise. Its right side belongs to \(L^2\), so the **integrated source** belongs to \(L^2\) at each finite \(N\). No instantaneous source square or two-time singular-square Fubini argument is used.

Define

\[
 \Delta_N(h,T)=\sqrt N\{\rho_T[h]-\rho_0[Q_T^\nu h]\},\qquad
 D_N(h,T)=\mathbb E|\Delta_N(h,T)|^2.
 \tag{3.4}
\]

Actual one-body Haar gives the exact scaled martingale variance

\[
 q_N:=Nb_N\mathbb E|M_N|^2
 =2\nu b_N\int_0^T\|\nabla Q_{T-t}^{\nu}h\|_2^2dt
 =\nu b_N\sum_{k\ne0}\frac{\ell_k|\widehat h(k)|^2}{c+\nu\ell_k}
                     (1-e^{-2(c+\nu\ell_k)T})
 \le2\nu b_NT\|\nabla h\|_2^2\to0.
 \tag{3.5}
\]

The martingale need not be independent of the final endpoint or source. Norm triangle inequalities, not a false subtraction of variances, give

\[
 \left|\sigma_N\mathbb E|I_N|-\sqrt{b_N}\mathbb E|\Delta_N|\right|
 \le\sqrt{q_N},
\qquad
 \left|\sqrt{Nb_N\mathbb E|I_N|^2}-\sqrt{b_ND_N(h,T)}\right|
 \le\sqrt{q_N}.
 \tag{3.6}
\]

The first is an asymptotic **\(L^1\) equivalence** to a nonsingular endpoint obligation. The condition \(D_N(h,T)\to0\) is sufficient for THM-046 and equivalent to its stronger \(L^2\) version. It is **not asserted necessary for the original \(L^1\) assertion**; uniform integrability of squared defects is unproved.

Let \(h_0=h-\int h\), \(q=Q_T^\nu h_0\), and let \(F_T^{(2)}\) be the actual current two-label law. Let \(\Gamma_s=\operatorname{Law}(X_1(T),X_1(0))\) and \(\Gamma_o=\operatorname{Law}(X_1(T),X_2(0))\). Direct label counting gives, for real \(h\),

\[
\begin{split}
 D_N(h,T)={}&\|h_0\|_2^2+(N-1)\int h_0(x)h_0(y)dF_T^{(2)}+\|q\|_2^2\\
 &-2\int h_0(x)q(y)d\Gamma_s
 -2(N-1)\int h_0(x)q(y)d\Gamma_o.
\end{split}
 \tag{3.7}
\]

All observables are bounded. Same-label terms have coefficient one; distinct labels have coefficient \(N-1\). The initial distinct-label term vanishes only because the admitted initial preparation is iid.

## 4. A precise sufficient fixed-mode gate

For \(k\ne0\), put

\[
 Z_k(t)=N^{-1}\sum_i e_k(X_i(t)),\quad a_k=c+\nu\ell_k,\quad A_k=e^{-a_kT},
\]
\[
 C_N=\mathbb E e_k(X_1(T)-X_2(T)),\quad
 S_N=\mathbb E e_k(X_1(T)-X_1(0)),\quad
 O_N=\mathbb E e_k(X_1(T)-X_2(0)).
 \tag{4.1}
\]

The dependence on \(k,T\) is implicit in these three correlations. Exchangeability makes \(C_N\) real. Retaining real parts avoids needing any further symmetry. The exact nonnegative defect is

\[
 \boxed{\mathcal D_N(k,T):=N\mathbb E|Z_k(T)-A_kZ_k(0)|^2
 =1+(N-1)C_N+A_k^2-2A_k\operatorname{Re}[S_N+(N-1)O_N].}
 \tag{4.2}
\]

Translation invariance kills mixed-mode covariances, hence

\[
 D_N(h,T)=\sum_{k\ne0}|\widehat h(k)|^2\mathcal D_N(k,T).
 \tag{4.3}
\]

For finite Fourier sums this is algebra. At fixed \(N\), the bound
\(|\sqrt N(Z_k(T)-A_kZ_k(0))|\le2\sqrt N\) and absolute summability of \(\widehat h\) give dominated \(L^2\) passage. This does not provide uniform-in-N domination.

A sufficient gate for the entire fixed-smooth-test assertion is

\[
 \boxed{\mathcal D_N(k,T)\to0\quad\text{for each fixed }k\ne0,T.}
 \tag{4.4}
\]

The extension to smooth tests needs a uniform bound, available in \(L^1\). In R16, \(d=4,s=2,\alpha=1,M=6\), and the commutator seminorm has degree \(\alpha+M+3=10\). Apply that proof to the real and imaginary parts of \(e_k\), then use (3.3) and (3.5):

\[
 \mathbb E|\sqrt N(Z_k(T)-A_kZ_k(0))|\le C_T(1+|k|)^{10}.
 \tag{4.5}
\]

The constant is independent of \(N,k\) on the eventual bounded-noise range; the polynomial also bounds the lower-order leading-martingale term. For smooth \(h\), the series
\(\sum_k|\widehat h(k)|(1+|k|)^{10}\) converges. Condition (4.4) gives convergence in \(L^1\) at each mode by Cauchy–Schwarz. Dominated summation using (4.5), then (3.6), proves THM-046 for every fixed smooth \(h\). No uniform \(L^2\) Fourier domination is claimed.

## 5. Actual same-particle stability removes one correlation term

The R10 floor has a direct Coulomb specialization. For \(r>0\), retain
\(g^{>r}=c\int_r^\infty(p_u-1)du\). Its nonzero Fourier coefficients are positive, \(g^{>r}(0)\le Cr^{-1}\), and \(g\ge g^{>r}-cr\) off zero. Subtracting the smooth self diagonal yields

\[
 H_N\ge\frac N2\sum_{k\ne0}\widehat {g^{>r}}(k)|\widehat\eta_N(k)|^2
 -\frac12g^{>r}(0)-\frac{N-1}{2}cr\ge-C\sqrt N
 \quad\text{at }r=N^{-1/2}.
 \tag{5.1}
\]

Together with (2.4) and exchangeability,

\[
 \mathbb E\int_0^T|B_1|^2dt\le CN^{-1/2}+\nu cT.
 \tag{5.2}
\]

In consistent Euclidean lifts, the displacement is the drift integral plus
\(\sqrt{2\nu}W_1\). Cauchy–Schwarz in time and the \(L^2\) martingale maximum inequality give

\[
 \mathbb E\sup_{t\le T}\operatorname{dist}(X_1(t),X_1(0))^2
 \le C_T(N^{-1/2}+\nu)=O(N^{-1/2})
 \tag{5.3}
\]

along an admitted critical sequence. This is an actual-path result. Consequently

\[
 0\le1-\operatorname{Re}S_N(k,T)
 \le2\pi^2|k|^2\mathbb E\operatorname{dist}(X_1(T),X_1(0))^2
 \le C_{T,\lambda}|k|^2N^{-1/2}.
 \tag{5.4}
\]

Thus (4.2) is exactly

\[
 \mathcal D_N(k,T)=\mathcal C_N(k,T)+2A_k(1-\operatorname{Re}S_N(k,T)),
\]
\[
 \boxed{\mathcal C_N(k,T):=(N-1)[C_N(k,T)-2A_k\operatorname{Re}O_N(k,T)]
                                      +(1-A_k)^2.}
 \tag{5.5}
\]

For each fixed mode and horizon, \(\mathcal C_N\to0\) is **equivalent to the stronger mode gate (4.4)**. The remaining task is a specific cancellation between same-time and unequal-time distinct-label correlations. For example, two sufficient estimates, both still open here, are

\[
 (N-1)C_N(k,T)\to e^{-2cT}-1,\qquad
 (N-1)\operatorname{Re}O_N(k,T)\to e^{-cT}-1.
 \tag{5.6}
\]

Neither their separate necessity nor a limiting-law theorem is asserted. Tagged-particle stability alone cannot prove (5.5): Cauchy–Schwarz on \(N\) displacement errors loses the fluctuation scale. Their signed collective correlation is the missing information.

## 6. Exact BBGKY and mixed cumulant form of the first unproved line

At fixed \(N\), let \(F_t^{(m)}\) be the law of the first \(m\) current positions. For smooth \(\varphi\), the true weak hierarchy is

\[
\begin{split}
 \frac d{dt}\int\varphi\,dF_t^{(m)}
 ={}&\nu\int\sum_{i=1}^m\Delta_i\varphi\,dF_t^{(m)}
 +\frac1N\sum_{\substack{i,j\le m\\i\ne j}}
          \int K(x_i-x_j)\cdot\nabla_i\varphi\,dF_t^{(m)}\\
 &+\frac{N-m}{N}\sum_{i=1}^m
          \int K(x_i-z)\cdot\nabla_i\varphi\,dF_t^{(m+1)}(x,z).
\end{split}
 \tag{6.1}
\]

For \(m=N\) the last term is absent. This is an absolutely continuous weak identity. Stop first; then (2.5) and \(K\in L^1\) give a finite expected absolute time integral and remove the stops. No singular derivative of a marginal density is required.

There is a sharper centered form for the mode at issue. For fixed \(k\ne0\), define

\[
 j_k(x,y)=J^{e_k}(x,y)+c[e_k(x)+e_k(y)],\qquad
 \int j_k(x,y)dy=\int j_k(x,y)dx=0.
 \tag{6.2}
\]

This rewrites the original statistic without changing its centering. Each particle occurs \(2(N-1)\) times in the added ordered rows. Therefore

\[
 P_N[J^{e_k}]=U_N^k+\frac cN Z_k,\qquad
 U_N^k=\frac1{2N^2}\sum_{i\ne j}j_k(X_i,X_j).
 \tag{6.3}
\]

The residual row is \(+cZ_k/N\), not zero or its negative. The exact forward equation and conjugate bracket are

\[
 dZ_k=-\widetilde a_kZ_kdt+U_N^kdt+dM_k,\qquad
 \widetilde a_k=c+\nu\ell_k-c/N>0,\qquad
 d\langle M_k,\overline M_k\rangle_t=\frac{2\nu\ell_k}{N}dt.
 \tag{6.4}
\]

The bracket is deterministic because \(|\nabla e_k|^2=\ell_k\). Define

\[
\begin{aligned}
 A_{2,N}(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(t))}],\\
 A_{3,N}(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(t))}],\\
 B_{2,N}(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(0))}],\\
 B_{3,N}(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(0))}].
\end{aligned}
 \tag{6.5}
\]

The label-3 terms are absent at \(N=2\). All others are genuine \(L^1(dt\,d\mathbb P)\) quantities by (2.7); the added rows and final factors are bounded. Put

\[
 \mathcal F_N(t)=\frac{N-1}{N}A_{2,N}(t)
       +\frac{(N-1)(N-2)}{2N}A_{3,N}(t),\qquad
 \mathcal G_N(t)=\frac{N-1}{N}B_{2,N}(t)
       +\frac{(N-1)(N-2)}{2N}B_{3,N}(t).
 \tag{6.6}
\]

There are \(2N(N-1)\) overlap triples and \(N(N-1)(N-2)\) all-distinct triples, divided by \(2N^2\) in \(N\mathbb E[U_N^k\overline Z_k]\). Symmetry of \(j_k\) identifies the two overlap terms. Thus exactly

\[
 N\mathbb E[U_N^k(t)\overline{Z_k(t)}]=\mathcal F_N(t),\qquad
 N\mathbb E[U_N^k(t)\overline{Z_k(0)}]=\mathcal G_N(t).
 \tag{6.7}
\]

Let \(V_N(t)=N\mathbb E|Z_k(t)|^2\) and
\(R_N(t)=N\mathbb E[Z_k(t)\overline{Z_k(0)}]\).
Product Itô gives the exact absolutely continuous equations

\[
 V_N'=-2\widetilde a_kV_N+2\nu\ell_k+2\operatorname{Re}\mathcal F_N,\qquad
 R_N'=-\widetilde a_kR_N+\mathcal G_N,\qquad V_N(0)=R_N(0)=1.
 \tag{6.8}
\]

Current and initial modes are bounded, and the initial mode is measurable at time zero, so the relevant martingales have zero expectation. No initial/final independence is assumed. The same-label Itô contraction is precisely \(2\nu\ell_k\).

Both evolved coordinates contribute in the current/current equation, giving the full \(2c\) response before its two finite-N row corrections. Only the current coordinate evolves in the current/initial equation, giving \(c\) before its single row correction. Thus neither a response slot nor a background factor has disappeared in the passage from the particle generator to (6.8).

Solving (6.8) and using \(\mathcal D_N=V_N(T)+A_k^2-2A_k\operatorname{Re}R_N(T)\) proves

\[
\begin{split}
 \mathcal D_N(k,T)={}&
 (e^{-\widetilde a_kT}-e^{-a_kT})^2
 +\frac{\nu\ell_k}{\widetilde a_k}(1-e^{-2\widetilde a_kT})
 +2\operatorname{Re}\mathcal R_N(k,T),\\
 \mathcal R_N(k,T)={}&\int_0^T
 \left[e^{-2\widetilde a_k(T-t)}\mathcal F_N(t)
 -e^{-a_kT}e^{-\widetilde a_k(T-t)}\mathcal G_N(t)\right]dt.
\end{split}
 \tag{6.9}
\]

At critical scaling, the first explicit term is \(O_T(N^{-2})\), and the second is \(O_{k,T,\lambda}(N^{-1/2})\), since \(\widetilde a_k\ge c/2\). The **first unproved uniform estimate for this stronger mode route** is precisely

\[
 \boxed{\operatorname{Re}\mathcal R_N(k,T)\longrightarrow0
             \quad\text{for every fixed }k\ne0,T.}
 \tag{6.10}
\]

It is equivalent to (4.4) and (5.5) in the actual critical model, and hence sufficient for THM-046 by Section 4. It is weaker than absolute smallness of each term.

The quantifiers in (6.10) are: for every fixed \(k\in\mathbb Z^4\setminus\{0\}\), every fixed finite \(T\), every \(\lambda\in(0,\infty)\), and every sequence \(\beta_N>0\) with \(\beta_NN^{-1/2}\to\lambda\), evaluated under the actual law (1.2). Its **exact negation** is an admitted such \(k,T,\lambda,\beta_N\) with \(\limsup_N\operatorname{Re}\mathcal R_N(k,T)>0\). Indeed, (6.9) makes \(\operatorname{Re}\mathcal R_N\ge-o(1)\); failure to tend to zero is therefore equivalent to positive limsup, or to exceeding one fixed positive number on an infinite subsequence. This negates the stronger covariance route only, not automatically THM-046's \(L^1\) target.

A stronger sufficient set of conditions would be

\[
 \int_0^T(|A_{2,N}|+|B_{2,N}|)dt=o(1),\qquad
 \int_0^T(|A_{3,N}|+|B_{3,N}|)dt=o(N^{-1}).
 \tag{6.11}
\]

Neither (6.10) nor (6.11) is proved here. R16's single-source absolute-moment bound does not prove these signed current/initial correlations.

The connected quantities can be defined without heuristic factorization. Current one-body marginals are Haar, so define

\[
 \kappa_t^{(3)}
 =F_t^{(3)}-F_{t,12}^{(2)}dx_3-F_{t,13}^{(2)}dx_2
             -F_{t,23}^{(2)}dx_1+2dx_1dx_2dx_3.
 \tag{6.12}
\]

Then \(A_{3,N}=\int j_k(x_1,x_2)\overline{e_k(x_3)}d\kappa_t^{(3)}\). Every subtracted term vanishes by either a zero row of \(j_k\) or the zero mean of \(e_k\). Similarly \(A_{2,N}\) pairs \(j_k(x_1,x_2)\overline{e_k(x_1)}\) with \(F_t^{(2)}-dx_1dx_2\).

For either mixed law \(\Gamma_t=\operatorname{Law}(X_1(t),X_2(t),X_j(0))\), \(j=1\) or \(3\), subtract its three two-coordinate marginals times Haar and add twice Haar cubed. Pairing this connected signed measure with \(j_k(x_1,x_2)\overline{e_k(y)}\) gives exactly \(B_{2,N}\) or \(B_{3,N}\). These are probability/signed measures, not presumed smooth two-time densities. At \(t=0\) a current/initial marginal can be supported on a diagonal. The subtracted terms remain absolutely integrable: \(j_k\) has uniformly bounded Haar \(L^1\) slices, and each one-coordinate marginal is Haar. The genuine term is integrable by (2.7). For \(B_2\), “third connected” counts three variables but only two particle labels; its coefficient remains the overlap coefficient in (6.6).

This finishes the local proof attempt. The singular finite-N hierarchy, all contractions, and the exact correlation reduction are established. The explicit contact and noise errors vanish. The surviving signed connected correlation (6.10) is isolated with exact coefficients; closing it is new work, not an invocation of BBGKY by name.

## 7. Actual-law short-time falsification attempt

Independently of the endpoint derivation, apply the actual initial generator to smooth observables. Product Haar at time zero in (6.1) gives, in distributions,

\[
 \left.\partial_tF_t^{(2)}\right|_{t=0}
 =-\frac2N\operatorname{div}K(x-y)
 =-\frac{2c}{N}[\delta_{x=y}-dx\,dy].
 \tag{7.1}
\]

The pair diagonal measure has mass one. The compensation keeps total mass zero. Third-label forces integrate to zero initially. For fixed nonzero \(k\),

\[
 C_N'(k,0)=-2c/N,\qquad
 S_N'(k,0)=-\nu\ell_k,\qquad O_N'(k,0)=-c/N.
 \tag{7.2}
\]

For the same initial tag, diffusion contributes \(-\nu\ell_k\) and the initial force has mean zero. For the distinct initial tag, only its interaction with the current particle survives:
\(N^{-1}\int K(z)\cdot\nabla e_k(z)dz=-c/N\).

These singular right derivatives are justified at each fixed \(N\). The current-observable generator is Haar \(L^1\); (2.5) gives a uniform density bound on a short interval. Approximate that generator in Haar \(L^1\) by continuous functions, control errors with (2.5), and use path continuity for approximants. For a mixed initial-tag observable, approximate \(K\) in \(L^1\) by bounded continuous fields. Its error is still bounded by the current-pair density bound times the \(L^1\) error, since the initial factor has modulus one. The approximated mixed observable converges by path continuity. No two-time density bound or uniform-in-N Taylor remainder is used.

Equivalent exact checks are

\[
 V_N'(0)=-2c(1-1/N),\quad
 R_N'(0)=-\nu\ell_k-c(1-1/N),\quad
 \mathcal D_N'(k,0)=2\nu\ell_k,
\]
\[
 \mathbb E[P_N[J^{e_k}](X(0))\overline{Z_k(0)}]=c/N^2.
 \tag{7.3}
\]

Initial defect growth is precisely the leading noise at this order and tends to zero on a critical sequence. This attempted immediate-growth route gives no admitted negation. Without a uniform singular Taylor remainder it gives no fixed-time conclusion.

It **does disprove exact positive-time product Haar closure**. If the actual pair law remained product on an initial interval, every nonzero \(C_N(k,t)\) would vanish there, contradicting \(C_N'(k,0)=-2c/N\). This uses the actual law and generator, not a substituted static law. Its \(1/N\) size matters after multiplication by the number of distinct labels.

## 8. The admitted instantaneous source fails an \(L^2\) closure

Choose the fixed real terminal test \(h(x)=\cos(2\pi x_1)\). For finite \(T,\nu\), \(f_0=e^{-(c+\nu\ell_{e_1})T}h\) has a nonzero Hessian. Take \(y\) in a small open set with \(\cos(2\pi y_1)>1/2\), and \(z=r\theta\) in a cone with \(|\theta_1|>1/2\). Taylor expansion in (2.1) gives uniformly on a smaller set and cone

\[
 J^{f_0}(y+z,y)=2r^{-2}\theta^TD^2f_0(y)\theta+O(r^{-1}).
 \tag{8.1}
\]

The leading coefficient has a fixed nonzero sign bounded away from zero. Thus \(|J^{f_0}(y+z,y)|\ge ar^{-2}\) at sufficiently small \(r\).

For each fixed \(N\), put the other \(N-2\) coordinates in disjoint small neighborhoods separated from the close pair and from one another. This has positive Haar measure. Every other pair term and every row contraction in (1.4) is bounded there by a finite fixed-N constant. The close pair occurs twice with the same sign and total coefficient \(1/N^2\). For small \(r\), it dominates the bounded terms, proving

\[
 \mathbb E_{\mathrm{iid}}|P_N[J^{f_0}]|^2
 \ge c_N\int_0^\varepsilon r^3r^{-4}dr=\infty,\qquad N\ge2.
 \tag{8.2}
\]

The same source is in \(L^1\), because \(r^3r^{-2}\) is integrable. This rigorously disproves a pointwise source-variance closure at an admitted time and fixed test. It does not negate (1.5). Section 3 proves that the time integral belongs to \(L^2\) at each fixed \(N\); integrating the pointwise infinite square misses its cancellation.

## 9. Diagnostic, adversarial self-check, and dispositions

The fresh packet script round024_independent_diagnostic.py was written without reading a previous checker. It uses exact rational sparse Fourier polynomials in two coordinates embedded in \(\mathbb T^4\). Generators and sources are divided by \((2\pi)^2\); this normalization is explicit. Two real even smooth Fourier potentials, four test modes, \(N=2,\ldots,6\), three diffusivities and three endpoint weights are tested. There is no simulation, random seed, floating-point tolerance, or installed dependency.

The executed result is **PASS: 2,434 exact assertions in 40 categories, with 16 distinct nonvacuous mutation types**. Concrete witnesses are in DIAGNOSTIC_RESULT.json. Mutations include deleting the ordered half, reversing background/response signs, omitting or reversing the \(c/N\) residual row, using a falling-factorial denominator, changing two-/three-label coefficients, omitting the Itô factor two, changing the initial BBGKY sign/factor, and removing the Coulomb atom or its compensation. A literal finite-particle generator is compared with independently assembled overlap formulas. This supports smooth finite algebra, not singular dynamics or a critical estimate.

| Adversarial self-check | Resolution or remaining gap |
|---|---|
| Does a bounded endpoint expression prove uniform decay? | No. Its boundedness is fixed-N only; (6.10) remains open. |
| Is \(L^1\) smallness called equivalent to covariance decay? | No. Only the first relation in (3.6) is an \(L^1\) equivalence. Covariance is a stronger sufficient route. |
| Is the martingale treated as independent of the final endpoint? | No. Exact bracket and norm triangle inequalities are used. |
| Is the atom replaced by the punctured divergence? | No. The full measure determines response and initial BBGKY. The punctured Laplacian is used only in stopped energy. |
| Does tagged-particle stability imply collective stability? | No. Section 5 removes just the same-label term and exposes distinct-label cancellation. |
| Are mixed two-time densities assumed? | No. Probability/signed measures and absolute integrability suffice. |
| Is the R16 threshold bound promoted? | No. It supplies integrability and polynomial \(L^1\) domination only. |
| Are R12/R14 silently extended to Coulomb? | No. Their exact endpoint obstructions are recorded. |
| Are initial derivatives a uniform time expansion? | No. Only the fixed-N right derivative is proved. |
| Does the diagnostic certify the continuum proof? | No. It checks smooth coefficients and concrete mutations. |

| Assertion or route | Disposition |
|---|---|
| THM-046 / PO-033 | **OPEN; neither proved nor disproved.** |
| Singular one-body endpoint identity and leading bracket | **PROVED HERE / SELF-CHECKED**, with localization and integrability. |
| Bounded two-time pair formula, fixed-mode sufficient gate, distinct-label reduction | **EXACT REDUCTION / SELF-CHECKED**, with the stronger \(L^2\) limitation explicit. |
| Actual same-particle critical stability | **PROVED FROM THE PERMITTED FULL ENERGY/FLOOR ARGUMENTS**, with uniform constants displayed. |
| Complete finite-N two-/three-label and mixed-cumulant identity (6.9) | **PROVED HERE / SELF-CHECKED.** |
| Signed estimate (6.10), or sufficient termwise estimate (6.11) | **OPEN: first missing uniform estimate.** |
| Exact positive-time product Haar closure | **DISPROVED** by actual initial BBGKY. |
| Instantaneous iid \(L^2\) source closure | **DISPROVED** for an admitted fixed smooth test. |
| Immediate positive-variance negation route | **DOES NOT PRODUCE A NEGATION**; first-order damping and vanishing noise are retained. |
| Independent certification, promotion, full hierarchy or fluctuation law | **NOT CLAIMED.** |

## 10. Recoverable handoff

Only this memorandum, the assigned artifact directory, and the sibling packet archive/seal are issued. The packet contains 20 complete input copies and the original manifest, inventory, read/exposure record, the new diagnostic and concrete results, a safe exact byte/member verifier, output manifest, and README. Issued outputs and archive are made read-only after verification; any correction must be separately issued.

The next mathematical task is to prove or falsify (6.10) under the actual critical dynamics, retaining mixed initial/current correlations and the order-N coefficient of the third connected term. A proof of the original \(L^1\) target may bypass this stronger covariance gate, but must then control the nonsingular \(L^1\) endpoint defect in (3.6) by another argument. Failure of the stronger covariance gate alone would not negate THM-046.

Root integration and fresh whole independent review remain separate. No canonical record was edited, no new campaign identifier was assigned, and no commit or push was made by this worker.
