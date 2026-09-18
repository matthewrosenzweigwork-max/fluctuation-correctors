# AUD073 / TASK114 — whole THM051 isolated reconstruction

Issued 2026-09-18 UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r026-overlap-blind`. Assigned branch: `codex/hocf-r026-overlap-blind`. Provisioned base reported by the task: `ef438b612f732d21af1fa1756dd7559ef63c6d61`. The branch and base are provisioning metadata, not independently established by a Git/history read in this restricted lane.

**Verdict: the entire frozen conjunction THM051(A)–(D) is independently reconstructed. No admitted counterexample or unresolved proof line remains in that conjunction.** This report is an isolated reconstruction, not a hostile review of an unseen constructor proof, and does not decide root promotion. The actual signed three-distinct-label cancellation, and hence the original critical source mission, remain open. No vanishing limit or positive-limsup witness for that residual is asserted.

The twelve exact inputs passed the supplied digest manifest before mathematical reading. The current constructor derivation, code, results and exposure record, every current audit, current state/history, nonallowlisted linked files, other worktrees and memory files were not read. The automatically supplied global memory summary and global instructions were unavoidable ambient context; no mathematical assertion was taken from them. Earlier status labels appearing inside permitted historical sources were not treated as premises. The task restriction supersedes general instructions to read README, state and additional specification files, to edit canonical memoranda/ledgers, or to commit. No child, external source, installation, Git action, remote action or canonical edit was used.

## 1. Exact assertion, negation and source boundary

Use precisely the actual singular gradient dynamics on the unit four-torus, from independent Haar positions independent of independent standard four-dimensional Brownian motions:

\[
 dX_i=B_i(X)\,dt+\sqrt{2\nu}\,dW_i,
 \qquad B_i=\frac1N\sum_{j\ne i}K(X_i-X_j),\qquad
 K=-\nabla g,\quad \widehat g(m)=|m|^{-2}\ (m\ne0),\quad\widehat g(0)=0.
 \tag{1}
\]

Here every integer \(N\ge2\) and every finite \(\nu>0\) is admitted. Haar measure has mass one, \(e_m(x)=e^{2\pi i m\cdot x}\), \(c=4\pi^2\), \(\ell_k=c|k|^2\), and \(k\in\mathbb Z^4\setminus\{0\}\) is fixed. Distances below are torus distances. All time-uniform expectations are deterministic-time expectations, not assertions about the probability of a minimum separation event.

THM051(A) asserts its exact heat-energy inequality and its uniform pair small-ball bound. Part (B) asserts the correctly row-centered heat truncation, both actual-pair error and square bounds, all-frequency coefficient comparison and the exact finite-N current-overlap identity. Part (C) asserts the two quantitative overlaps throughout every fixed critical window. Part (D) asserts the exact two-/three-label splitting, its vanishing two-label error and equivalence of the signed cancellation and positive-limsup alternatives. These are all proved below with exactly the frozen coefficients. The logical negation is a violation of at least one clause with its stated quantifiers, including failure of any claimed common constant. A failure of a proposed argument, an altered law, a moving test or time, an untruncated square divergence, or the unresolved residual cancellation is not this negation.

Only definitions are imported from the frozen THM046/THM049 cards. No unproved THM049 equivalence, THM048 statement or nonallowlisted historical source is a premise here. Sections 2–4 reconstruct the kernel, actual-process, energy and displacement mechanisms required from R4/R6/R10. The R1 input fixes ordered deletion and centering; the needed contractions are computed again. R16 supplies a permitted comparison with the earlier energy/source mechanism, but its polynomial-tail splitting, theorem label and source-bound status are not imported as proof. No external literature or novelty assertion is used.

| Clause | Fresh proof location | Verdict |
|---|---|---|
| A: exact positive heat energy, self subtraction, small balls | §§2–5 | Reconstructed, full fixed-N/time/diffusivity quantifiers |
| B: rows/diagonal, truncation, square, all-frequency Fourier comparison and current overlap | §§6–8 | Reconstructed, no singular diagonal or untruncated square used |
| C: both actual overlaps on every fixed critical window | §§4, 9 | Reconstructed, including finite prefixes within the window |
| D: exact remainder and both signed alternatives | §10 | Reconstructed; residual limit itself remains open |
| Whole conjunction / exact negation | §§2–11 | No failed clause; no admitted negating example |

## 2. Kernel normalization and the actual singular process

Let

\[
 p_u(z)=\sum_{n\in\mathbb Z^4}(4\pi u)^{-2}e^{-|z+n|^2/(4u)}.
\]

Unfolding gives positivity, mass one and coefficient \(e^{-cu|m|^2}\). The nonconstant Fourier series and all spatial derivatives decay exponentially for \(u\ge1\). Since \(\|p_u-1\|_1\le2\) at small times, the integral

\[
 g=c\int_0^\infty(p_u-1)\,du
 \tag{2}
\]

converges in Haar \(L^1\), has zero mean, and has the coefficients in (1). Its Euclidean central Gaussian integral is

\[
 c\int_0^\infty(4\pi u)^{-2}e^{-|z|^2/(4u)}\,du=|z|^{-2}.
\]

The substitution \(v=|z|^2/(4u)\) verifies the constant. On a ball of radius less than one third, the other lattice terms are exponentially small at small times, with all derivatives; at large times the torus remainder and the subtracted Euclidean integral, with all derivatives, are integrable. Therefore

\[
 g(z)=|z|^{-2}+H(z),\quad H\in C^\infty(B_{1/3}),\qquad
 K(z)=2z|z|^{-4}-\nabla H(z).
 \tag{3}
\]

In particular \(g,K\in L^1\), \(g\) is smooth off zero, and \(g_*:=\inf_{z\ne0}g(z)\) is finite and negative. The positivity of the singularity and zero mean imply the strict sign. Integration outside a ball of radius \(R\) gives a vanishing gradient boundary term of order \(R\), identifying the displayed \(K\) as the distributional negative gradient. Its divergence flux tends to \(2|\mathbb S^3|=4\pi^2=c\). Equivalently its nonzero Fourier coefficients equal \(c\) and its zero coefficient vanishes. Testing a heat-convolved distributional difference then identifies

\[
 \operatorname{div}K=c(\delta_0-dz),\qquad
 \Delta g=c\quad\hbox{off zero},\qquad
 \operatorname{div}K_\epsilon=c(p_\epsilon-1)\ge-c.
 \tag{4}
\]

The atom in the first formula is retained when mollifying; the punctured second formula is only applied on collision-excluded paths. No logarithmic limit or arbitrary smooth modification of the kernel is used.

For completeness the actual process and the limiting passages used here can be constructed directly. Put

\[
 H_N=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
 \mathcal H_N=H_N-\frac{N-1}{2}g_*\ge0.
\]

Every energy sublevel is compact in the collision-free configuration space: each summand \(g-g_*\) is nonnegative and each colliding pair makes its own summand diverge. Smooth even local cutoffs of \(K\), zero near zero and equal to \(K\) outside a shrinking ball, give globally Lipschitz periodic drifts. Subtracting the continuous Brownian displacement gives a deterministic integral equation. Its Picard differences are bounded by a summable factorial series; Gronwall gives uniqueness. The resulting maps are measurable in time, initial state and Brownian path, and adapted. They agree before their collision-excluded exits and patch to the maximal singular path. A bounded-energy path has a limit at a finite endpoint inside a compact collision-excluded set, and hence extends there.

Differentiating both coordinates of each unordered pair gives, on that space,

\[
 B=-\nabla H_N,\qquad \Delta_{4N}H_N=c(N-1).
 \tag{5}
\]

Stop at the first energy level \(R\), with immediate stop if the initial shifted energy is already at least \(R\). Smooth Itô calculus on the compact stopped domain gives

\[
 \mathcal H_N(X_{t\wedge\tau_R})+
 \int_0^{t\wedge\tau_R}|B(X_s)|^2ds
 =\mathcal H_N(X_0)+\nu c(N-1)(t\wedge\tau_R)+M_R(t),
 \quad \langle M_R\rangle_t=2\nu\int_0^{t\wedge\tau_R}|B|^2ds.
 \tag{6}
\]

The bounded stopped integrand makes this a true martingale with zero mean. Thus the energy-exit probability by time \(T\) is at most \((\mathbb E\mathcal H_N(X_0)+\nu c(N-1)T)/R\). The iid initial expectation is \(-(N-1)g_*/2<\infty\). Letting \(R\) tend to infinity excludes a finite lifetime; the resulting path is globally collision-free almost surely. This is a fixed-parameter conclusion. Joint measurability permits averaging over iid initial positions without an exceptional set uniform over every starting point.

Every such continuous path has a positive random minimum pair distance on each finite interval. Heat mollification converges with one spatial derivative to \(K\) uniformly on any compact set away from zero: split the integrable kernel into a smooth part agreeing near that set and a distant integrable remainder; differentiated Gaussian bounds make the latter contribution exponentially small. Couple the heat and singular SDEs with identical initial points and Brownian paths. The noises cancel in their difference. Until the distance between the paths is a quarter of the singular minimum pair distance, a common local Lipschitz bound and Gronwall give a difference tending to zero. This prevents that stop for sufficiently small heat parameter. Thus the full heat family converges uniformly on every fixed finite interval almost surely. Constants here can depend on the path and on \(N,\nu,T\); no uniform rate is extracted.

## 3. Actual expected energy, with an explicit singular passage

This step is essential: initial product Haar is not asserted to remain product Haar. For fixed \(\epsilon>0\), let \(H_N^\epsilon\) and \(F_t^\epsilon\) be the heat-regularized potential and actual density from density one. At finite positive \(\nu\), the smooth periodic equation is

\[
 \partial_t F^\epsilon=\nu\Delta F^\epsilon+
       \operatorname{div}(F^\epsilon\nabla H_N^\epsilon).
 \tag{7}
\]

At this fixed cutoff every coefficient derivative is bounded. One direct construction iterates the heat integral equation in continuous functions: the gradient heat convolution has an integrable \((t-s)^{-1/2}\) bound, so this is a contraction on a short interval and iterates to any finite interval. Differentiation and heat smoothing give the classical solution for smooth initial density and coefficients. Smooth backward tests and Itô identify it with the law of the smooth SDE. Comparison with \(e^{\pm Ct}\), for \(C\ge\|\Delta H_N^\epsilon\|_\infty\), yields positive lower and finite upper bounds on each finite interval, and integration preserves total mass. Consequently the following differentiations are legitimate:

\[
 \frac d{dt}\left(\nu\int F_t^\epsilon\log F_t^\epsilon
                    +\int H_N^\epsilon F_t^\epsilon\right)
 =-\int F_t^\epsilon
       |\nabla H_N^\epsilon+\nu\nabla\log F_t^\epsilon|^2\le0.
 \tag{8}
\]

Both initial terms vanish, since every initial pair difference is Haar and \(g_\epsilon\) has zero mean. Entropy is nonnegative on this mass-one space by convexity. Thus \(\mathbb E H_N^\epsilon(X_t^\epsilon)\le0\).

Heat positivity gives the common lower bound \(H_N^\epsilon\ge(N-1)g_*/2\) at fixed \(N\). The same-noise passage of §2 and local uniform convergence \(g_\epsilon\to g\) give almost-sure convergence of these energies at every fixed time. Fatou after subtracting the common lower bound proves

\[
 \mathbb E H_N(X_t)\le0\qquad(N\ge2,\ 0<\nu<\infty,\ 0\le t<\infty).
 \tag{9}
\]

This also proves integrability of the shifted energy. Permutation equivariance and pathwise uniqueness give exchangeability. Common translations preserve both the initial law and the equation, so each one-particle marginal is Haar. Only exchangeability is needed for

\[
 \mathbb E g(X_1-X_2)=\frac2{N-1}\mathbb E H_N\le0,
 \qquad \mathbb E|g(X_1-X_2)|\le2|g_*|.
 \tag{10}
\]

The second inequality uses \(|g|\le g+2|g_*|\). By (3) and a bounded estimate outside a fixed small ball it also gives

\[
 \sup_{N,\nu,t}\mathbb E\operatorname{dist}(X_1(t)-X_2(t),0)^{-2}<\infty.
 \tag{11}
\]

All constants in (9)–(11) depend only on the frozen kernel. The heat parameter limit was taken at fixed \(N,\nu,t\) before deriving the uniform bound. No singular entropy-dissipation identity, fixed-N density exponent treated as uniform, or initial/current joint density is used.

## 4. Deterministic floor and labeled displacement

This section records the only time-dependent estimate needed later. It is proved independently of the overlap bounds. For any \(0<r\le1\), (2) gives the exact off-zero splitting

\[
 g=g_r+q_r-cr,\qquad
 g_r=p_r*g=c\int_r^\infty(p_u-1)du,
 \quad q_r=c\int_0^r p_u\,du\ge0.
 \tag{12}
\]

The smooth function \(g_r\) has positive nonzero coefficients
\(a_r(m)=|m|^{-2}e^{-cr|m|^2}\), and zero constant coefficient. The heat bound at zero gives

\[
 0\le g_r(0)=\sum_{m\ne0}a_r(m)\le C/r.
 \tag{13}
\]

Indeed \(p_u(0)\le Cu^{-2}\) for \(0<u\le1\), while \(p_u(0)-1\) decays exponentially for \(u\ge1\). The lower sign also follows directly from the positive Fourier series.

For every collision-free configuration, with \(Z_m=N^{-1}\sum_i e_m(x_i)\), smooth self subtraction and (12) give

\[
 H_N\ge \frac N2\sum_{m\ne0}a_r(m)|Z_m|^2
              -\frac12g_r(0)-\frac{N-1}{2}cr.
 \tag{14}
\]

There are \(N(N-1)/2\) unordered pairs. The deleted self contribution is exactly \(g_r(0)/2\). Choose \(r=N^{-1/2}\) to obtain the deterministic lower bound \(H_N\ge-C\sqrt N\).

Taking expectations in stopped (6), restoring the unshifted potential, and using this deterministic floor yields

\[
 \mathbb E\int_0^{T\wedge\tau_R}|B|^2ds
 \le C\sqrt N+\nu c(N-1)T.
\]

The initial unshifted energy has mean zero. Fatou as the increasing stops tend to infinity gives the same inequality on \([0,T]\). The unstopped energy martingale then has integrable bracket and is square integrable. The stopped martingales converge to it in \(L^2\), because the expected omitted bracket tends to zero. Localization and expectation consequently give the exact energy identity as well, but only the displayed inequality is needed here. In particular exchangeability implies

\[
 \mathbb E\int_0^T|B_i|^2ds\le C N^{-1/2}+\nu cT.
 \tag{15}
\]

The square is the square of each *total* drift; individual pair-force squares and all their cross terms have not been separated or discarded.

Choose consistent Euclidean lifts. The displacement is \(\int_0^tB_i ds+\sqrt{2\nu}W_i(t)\). Cauchy–Schwarz in time, the bound of torus distance by lifted distance, and the Brownian maximal bound \(\mathbb E\sup_{t\le T}|W_i(t)|^2\le4dT\) give

\[
 \mathbb E\sup_{0\le t\le T}\operatorname{dist}(X_i(t),X_i(0))^2
 \le C_T(N^{-1/2}+\nu).
 \tag{16}
\]

For each critical window \(\lambda_-\le\beta/\sqrt N\le\lambda_+\), one has \(\nu\le\lambda_-^{-1}N^{-1/2}\), so the right side is \(C_{T,\lambda_-}N^{-1/2}\). No cutoff-dependent displacement estimate or singular-observable continuity is inferred from this alone.

## 5. Clause A: exact heat energy and small balls

At a fixed positive \(r\), absolute Fourier convergence and exchangeability give the literal identity

\[
 \mathbb E g_r(X_1-X_2)
 =\frac N{N-1}\mathbb E\sum_{m\ne0}a_r(m)|Z_m|^2
       -\frac{g_r(0)}{N-1}.
 \tag{17}
\]

The singular \(q_r\) is nonnegative and integrable under the pair law by (12), (10), and boundedness of \(g_r\). Inserting (17) into (12) and using (10) gives exactly

\[
 \frac N{N-1}M_r(t)+\mathbb E q_r(X_1(t)-X_2(t))
 \le\frac{g_r(0)}{N-1}+cr.
 \tag{18}
\]

Since both quantities on the left are nonnegative, (13), \((N-1)^{-1}\le2/N\), and \(N/(N-1)\ge1\) prove the second claimed inequality

\[
 M_r(t)+\mathbb E q_r(X_1(t)-X_2(t))
 \le C\big((Nr)^{-1}+r\big).
 \tag{19}
\]

For \(0<R\le R_0<1/8\), select a nearest lift \(z\) with \(|z|\le R\). Retaining its Gaussian contribution and integrating on \([R^2/2,R^2]\) gives the explicit lower bound

\[
 q_{R^2}(z)\ge \frac{e^{-1/2}}8R^{-2}.
\]

Apply (19) at \(r=R^2\). Markov's inequality for this positive function gives

\[
 \mathbb P(\operatorname{dist}(X_1(t)-X_2(t),0)\le R)
 \le C R^2\big((NR^2)^{-1}+R^2\big)
 =C(R^4+N^{-1}).
 \tag{20}
\]

The constants are fixed kernel constants; a single choice works for every \(R_0<1/8\). The same estimates hold at time zero and every finite deterministic time and every finite positive diffusivity. They provide no pathwise minimal-separation estimate. This proves every assertion of (A).

## 6. Clause B: centered heat truncation and its actual-pair error

Write \(z=x-y\), \(d_r=c e^{-r\ell_k}\), and

\[
 j_r(x,y)=K_r(z)\cdot(\nabla e_k(x)-\nabla e_k(y))
                +d_r(e_k(x)+e_k(y)),\quad K_r=-\nabla g_r.
 \tag{21}
\]

Fourier convolution gives \(\int K_r=0\) and
\(K_r*\nabla e_k=d_r e_k\). Thus the first term has Haar row \(-d_r e_k(x)\), and the added response cancels it exactly; the other row is zero by symmetry. As a smooth kernel its diagonal is exactly \(2d_r e_k(x)\). For the singular kernel the same Haar-row computation is legitimate since \(K\in L^1\); the coefficient is \(c\), and no singular diagonal is assigned.

The derivative of (12) off zero yields
\(K-K_r=-c\int_0^r\nabla p_u du\). Let \(\rho=\operatorname{dist}(z,0)\). For each Gaussian translate \(v=z+n\), one has \(\rho\le|v|\) and

\[
 \rho\,|\nabla[(4\pi u)^{-2}e^{-|v|^2/(4u)}]|
 \le \frac{|v|^2}{2u}(4\pi u)^{-2}e^{-|v|^2/(4u)}
 \le C(8\pi u)^{-2}e^{-|v|^2/(8u)}.
\]

Summing gives \(\rho|\nabla p_u(z)|\le Cp_{2u}(z)\). This inequality includes the noncentral lattice terms; the torus distance is never differentiated. Since the smooth periodic gradient of \(e_k\) is Lipschitz,

\[
 |(K-K_r)(z)\cdot(\nabla e_k(x)-\nabla e_k(y))|
 \le C_k q_{2r}(z).
\]

Also \(|c-d_r|\le c\ell_k r\). Consequently, for \(0<r\le r_0\le1/2\), applying (19) at \(2r\le1\) proves

\[
 \mathbb E|j_k(X_1,X_2)-j_r(X_1,X_2)|
 \le C_k\big(r+(Nr)^{-1}\big).
 \tag{22}
\]

The heat response correction was included in the truncation before estimating. We have not taken the expectation of a merely formal differentiated singular energy.

## 7. Clause B: the logarithmic truncated-square estimate

The same Gaussian estimate, now integrated over \([r,1]\), and exponential derivative decay above time one give

\[
 \rho|K_r(z)|\le C+C\int_r^1u^{-2}e^{-\rho^2/(C u)}du
 \le C\big(1+\min\{r^{-1},\rho^{-2}\}\big).
\]

For the middle inequality the periodized Gaussian satisfies
\(p_{2u}(z)\le Cu^{-2}e^{-\rho^2/(C u)}\) on \(0<u\le1\): split the exponent in each translate, use its distance lower bound in one factor, and sum the other factor uniformly over the nearest fundamental cube. The last inequality follows either by dropping the exponential and integrating from \(r\), or by substituting \(v=\rho^2/(C u)\) and integrating from zero. Thus

\[
 |j_r(x,y)|^2\le C_k\big(1+\min\{r^{-2},\rho^{-4}\}\big)
 \quad(x\ne y).
 \tag{23}
\]

This does not assert any square integrability of \(j_k\). Apply layer-cake to the truncated quantity. If \(r^{-2}>R_0^{-4}\), split its layer integral at \(R_0^{-4}\). On the upper range (20) gives

\[
 \mathbb P(\rho^{-4}>u)\le C(u^{-1}+N^{-1}).
\]

The lower range costs a fixed constant. Hence

\[
 \mathbb E\min\{r^{-2},\rho^{-4}\}
 \le C+C\int_{R_0^{-4}}^{r^{-2}}(u^{-1}+N^{-1})du
 \le C\big(1+\log(1/r)+(Nr^2)^{-1}\big).
 \tag{24}
\]

If the upper endpoint is smaller than the splitting point, the whole layer integral is bounded by that fixed splitting constant, giving the same conclusion after enlarging \(C\). Combining (23)–(24) proves the requested square bound for every \(0<r\le r_0\). Constants can be fixed once and for all for, for example, \(R_0=1/16\) and \(r_0\le1/2\); none depends on \(N,\nu,t,r\).

## 8. Clause B: all Fourier coefficients and exact self subtraction

At positive \(r\), multiplying (21) by \(\overline{e_k(x)}\) leaves the function of \(z\)

\[
 (2\pi i k)\cdot K_r(z)(1-e_{-k}(z))+d_r(1+e_{-k}(z)).
\]

Substitution of \(\widehat K_r(m)=-2\pi i m a_r(m)\) gives its exact coefficient

\[
 b_r(m)=c\{(k\cdot m)a_r(m)-(k\cdot(m+k))a_r(m+k)\}
              +d_r(\mathbf1_{m=0}+\mathbf1_{m=-k}).
 \tag{25}
\]

Here \(a_r(0)=0\). The terms at \(m=0,-k\) each cancel exactly, so \(b_r(0)=b_r(-k)=0\). The two rapidly convergent sums in the braces cancel under translation of the summation index. Therefore

\[
 \sum_{m\ne0}b_r(m)=\sum_m b_r(m)=2d_r.
 \tag{26}
\]

This is also the smooth value at \(z=0\), hence checks the diagonal independently. All series used here are absolutely convergent at fixed positive \(r\).

For clarity the divided-difference estimate is proved on *all* lattice frequencies. For \(|m|\ge2|k|\), set
\(F_r(\xi)=(k\cdot\xi)|\xi|^{-2}e^{-cr|\xi|^2}\). On the segment \(\xi=m+\theta k\), \(0\le\theta\le1\), the derivative in direction \(k\) obeys

\[
 |k\cdot\nabla F_r(\xi)|
 \le C_k(|\xi|^{-2}+r)e^{-cr|\xi|^2}
 \le C_k|m|^{-2}(1+r|m|^2)e^{-cr|m|^2/4}
 \le C_k|m|^{-2}e^{-cr|m|^2/8}.
 \tag{27}
\]

The final step uses boundedness of \((1+v)e^{-cv/8}\) for \(v\ge0\). The indicators in (25) vanish in this range. Integrating (27) proves the comparison there. In the finite set \(0<|m|<2|k|\), the numerator in (25) is uniformly bounded for \(0<r\le1/2\), including \(m+k=0\); each denominator \(|m|^{-2}e^{-cr|m|^2/8}\) is bounded below by a positive constant depending only on \(k\). Increasing that finite constant proves

\[
 |b_r(m)|\le C_k a_{r/8}(m)\qquad(m\ne0,\ 0<r\le r_0).
 \tag{28}
\]

No fixed-frequency limit is used to stand in for (28).

For any nonzero lattice vector \(m\), the pointwise ordered sum and exchangeability imply

\[
 \mathbb E e_m(X_1-X_2)
 =\frac{N\mathbb E|Z_m|^2-1}{N-1}.
 \tag{29}
\]

The ordered sum is \(N^2|Z_m|^2-N\). Symmetry under label exchange makes this expectation real; no rotational symmetry or independence is needed. Multiply (29) by (25) and sum, using absolute convergence and (26). This proves exactly

\[
 A_{2,r}(t)=\frac N{N-1}\mathbb E\sum_{m\ne0}b_r(m)|Z_m(t)|^2
                 -\frac{2d_r}{N-1}.
 \tag{30}
\]

The heat multiplier, the factor \(N/(N-1)\) and the self subtraction are all literal. This completes (B).

## 9. Clause C: current and mixed-initial overlaps

Equations (19), (28), and (30) imply, uniformly over all the parameters of (A),

\[
 |A_{2,r}(t)|\le C_k\big(r+(Nr)^{-1}+N^{-1}\big).
\]

Together with (22), this gives the same bound for \(|A_2(t)|\). The preceding proofs hold throughout \(0<r\le1/2\), independently of a smaller stated cutoff cap. Choose the universal numerical value \(\alpha=1/2\) and

\[
 r_N=\alpha N^{-1/2}.
\]

This lies in the interval on which the preceding proofs establish the estimates for *every* \(N\ge2\); no hidden threshold or finite-prefix omission occurs. Both terms in (22) are \(O_k(N^{-1/2})\), with a constant depending only on the fixed kernel and mode. If the theorem names a smaller \(r_0\), the proof has simply established the same auxiliary estimates on a larger interval; the final constants do not depend on that naming choice. Thus

\[
 \sup_{t\le T}|A_2(t)|\le C_kN^{-1/2}.
 \tag{31}
\]

This estimate in fact needs no critical-window restriction. The square estimate at the same cutoff gives

\[
 \sup_{t,\nu}\mathbb E|j_{r_N}(X_1(t),X_2(t))|^2
 \le C_k(1+\log N),
 \tag{32}
\]

because \(Nr_N^2=\alpha^2\).

For the mixed-initial term, insert the same *truncated* kernel into the exact difference

\[
 B_2(t)-A_2(t)=
 \mathbb E\{j_k(X_1(t),X_2(t))
 [\overline{e_k(X_1(0))}-\overline{e_k(X_1(t))}]\}.
\]

The bracket is bounded by two and is \(2\pi|k|\)-Lipschitz in the torus displacement. By (22), Cauchy–Schwarz for the truncated kernel, (16), and (32),

\[
 |B_2(t)-A_2(t)|
 \le C_kN^{-1/2}
 +C_k\sqrt{1+\log N}\,(\mathbb E\operatorname{dist}(X_1(t),X_1(0))^2)^{1/2}
 \le C_{k,T,\lambda_-}N^{-1/4}\sqrt{1+\log N}
 \tag{33}
\]

throughout the critical window. With (31) this proves the asserted bound on \(B_2\). The upper window endpoint need not be used; allowing dependence on it is harmless. Constants do not depend on how quickly a critical sequence approaches its limiting coupling. No initial/current joint density, product-law closure or untruncated source square occurs in (33).

Absolute integrability is separate from cancellation. From (3), the Lipschitz gradient difference, and (11),

\[
 \sup_{N,\nu,t}\mathbb E|j_k(X_1(t),X_2(t))|\le C_k.
 \tag{34}
\]

All multipliers in the definitions of \(A_2,A_3,B_2,B_3\) have modulus one. They are measurable by the path construction and have absolutely finite time integrals on every finite horizon, even away from a critical window. Tonelli bounds the time integral of the absolute source by \(C_kT\). For \(N=2\) no three-label variable is defined or used.

## 10. Clause D: the full signed three-label reduction

It is useful to rederive the label coefficients rather than merely accept the definitions. Let \(U_N^k=(2N^2)^{-1}\sum_{i\ne j}j_k(X_i,X_j)\). Then

\[
 N\mathbb E[U_N^k(t)\overline{Z_k(t)}]=F_N(t),\qquad
 N\mathbb E[U_N^k(t)\overline{Z_k(0)}]=G_N(t).
 \tag{35}
\]

Indeed, after expanding there are exactly \(2N(N-1)\) terms with the third label equal to one of the first two and \(N(N-1)(N-2)\) terms with all three distinct. Pair symmetry makes the two overlapping terms equal. The common prefactor is \(1/(2N^2)\), giving \((N-1)/N\) and \((N-1)(N-2)/(2N)\). At \(N=2\) the second count is zero without introducing a nonexistent third coordinate.

The original Haar-centered source remains distinct from the centered pair sum. The row of \(J^{e_k}\) is \(-ce_k\), so its literal deleted statistic satisfies

\[
 P_N[J^{e_k}]=U_N^k+(c/N)Z_k.
 \tag{36}
\]

This confirms the finite-N background used in the frozen \(\widetilde a=a_k-c/N\), rather than replacing it by \(a_k\). Formula (36) does not change any original source centering.

By the frozen definitions, the two-label part is exactly

\[
 \mathcal R_N^{(2)}=\frac{N-1}{N}\int_0^T
 \{e^{-2\widetilde a(T-t)}A_2(t)
       -A_k e^{-\widetilde a(T-t)}B_2(t)\}\,dt.
 \tag{37}
\]

The remaining terms are exactly the displayed \(\mathcal R_N^{(3)}\) in THM051, with prefactor \((N-1)(N-2)/(2N)\), and zero at \(N=2\). Equations (34)–(35) justify all expansions and integrals at each fixed \(N\). Therefore

\[
 \mathcal R_N=\mathcal R_N^{(2)}+\mathcal R_N^{(3)}
 \tag{38}
\]

is an exact identity, with no estimate or limiting passage hidden in the decomposition.

Since \(\widetilde a=c(1-1/N)+\nu\ell_k\ge c/2\), and \(0<A_k=e^{-a_kT}\le1\), every weight in (37) has modulus at most one. Equations (31)–(33) then give

\[
 |\mathcal R_N^{(2)}|\le
 C_{k,T,\lambda_-,\lambda_+}N^{-1/4}\sqrt{1+\log N}.
 \tag{39}
\]

For any admitted critical sequence, choose once and for all an eventual window, for example \([\lambda/2,2\lambda]\). Formula (39) tends to zero on that tail. Every finite prefix has well-defined absolutely finite integrals by (34); no condition on \(\min\{\beta,1\}\) was introduced in this theorem. Thus for the *same fixed mode, time, limiting coupling and sequence*,

\[
 \operatorname{Re}\mathcal R_N\longrightarrow0
 \quad\Longleftrightarrow\quad
 \operatorname{Re}\mathcal R_N^{(3)}\longrightarrow0.
 \tag{40}
\]

Moreover their limsups agree as extended real numbers, since the difference tends to zero. In particular

\[
 \limsup_N\operatorname{Re}\mathcal R_N>0
 \quad\Longleftrightarrow\quad
 \limsup_N\operatorname{Re}\mathcal R_N^{(3)}>0.
 \tag{41}
\]

This remains true if either limsup is infinite or either sequence has no limit. It does not assert that the logical negation of an arbitrary real sequence converging to zero is always a *positive* limsup: that additional interpretation for the original source uses the separately frozen THM049 criterion. Here (40) proves the zero-limit equivalence directly, and (41) proves the precise positive-limsup equivalence requested. No validity of the original-source L1/L2 equivalence is silently inferred from these elementary implications. If the separately audited THM049 criterion is invoked, the same fixed witness transfers through (41); this report does not re-certify THM049(B)–(C).

At \(T=0\) all three remainders vanish identically, so (38)–(41) are immediate, and both overlap bounds still hold. No separate estimate for \(A_3\) or \(B_3\), cancellation between them, or limiting law has been proved here.

## 11. Falsification route, quantifier review and remaining boundary

The attempted falsification route directly challenges the vulnerable identities on finite Fourier kernels and finite label configurations; it does not reuse empirical-law estimates as numerical assumptions. It tests wrong signs, wrong heat response, missing self terms, omitted second overlap and wrong triple coefficient. It also probes high frequencies scaling with the heat cutoff, rather than only fixed modes. The first complete run passed 134 checks and rejected all 34 nonzero mutation instances. Its three mode families also contain 43,344 binary64 all-frequency probes, summarized by three of those checks. These diagnostics are fresh, reproducible supporting checks. They are not a simulation of the actual singular law, proof of a uniform bound or an additional independent audit. The theorem is proved in §§2–10.

The following potential failures were checked analytically and do not survive:

1. Dropping the nonnegative short-scale heat term would lose the uniform small-ball information. Equation (18) retains it with coefficient one and retains the larger coefficient on \(M_r\).
2. Using \(c\) instead of \(ce^{-r\ell_k}\) in the smooth observable leaves nonzero rows. Equations (21), (25) and (26) fix all three corresponding coefficients.
3. A fixed-frequency heat argument does not imply the all-frequency estimate. The derivative estimate (27) and the separate finite set prove it with constants independent of \(r\).
4. An untruncated L2 estimate has a logarithmic singularity already under Haar in this dimension. Equations (23)–(24) truncate before squaring, and the cutoff at \(\alpha N^{-1/2}\) makes the extra finite-N term bounded.
5. Displacement control alone cannot bound the singular mixed overlap. Equation (33) first controls the L1 truncation error, then uses only the truncated square and displacement in Cauchy–Schwarz.
6. An asymptotic estimate cannot erase finite-N diagonals. Equations (17), (26), (30), (35), and (36) retain them exactly, including the no-triple convention at \(N=2\).
7. Failure of signed cancellation would require a genuine fixed-data witness; none is provided. The remaining three-label expression retains its sign and both terms.

All inequalities in (A)–(B) are uniform over all finite deterministic times and all positive finite diffusivities; only the displacement and hence (C)–(D) use a fixed horizon and a fixed lower critical-window bound. Every singular passage is performed at fixed finite parameters. There is no interchange of the singular approximation with an N-limit. Actual expectations remain under exactly the iid-Haar-prepared gradient process, and every comparison of positive Fourier energy concerns the actual empirical measure. No preparation, geometry, singularity exponent, logarithmic normalization or fluctuation theorem has changed.

The mathematical outcome is the entire frozen THM051 conjunction, with no first failed line to report. The first still-open line after this theorem is the vanishing, or an admitted positive-limsup counterexample, of the signed three-distinct-label integral in (40)–(41). The original critical source mission is not claimed complete.

The companion packet contains the exact twelve input copies, manifest, source/read/exposure and execution history, fresh diagnostic source and all results including mutation outcomes, safe inventories, portable read-only verifier and sibling archive/seals. Its reconstruction copy is byte-identical to this issued report. No TeX source was edited and no mathematical LaTeX is required in the short final handoff. The issued report and packet bytes are read-only; any correction must be a separately named superseding artifact.
