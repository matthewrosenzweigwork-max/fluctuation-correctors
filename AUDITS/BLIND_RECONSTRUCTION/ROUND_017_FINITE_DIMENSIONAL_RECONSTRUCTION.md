# AUD053 — full fresh reconstruction of THM-039

TASK-082, Round 017. Issued 2026-09-18 UTC. Isolated reconstruction lane `/root/r017_gaussian_blind`, prescribed Astra Ultra task. Worktree `/Users/matthewrosenzweig/.codex/worktrees/hocf-r017-gaussian-blind`, branch `codex/hocf-r017-gaussian-blind`, published base `072cab684b9ce41855ead6c48f435c8fc184ec35`.

**Verdict: the entire frozen THM-039 follows from the explicitly conditional complete R16 source premise, with no additional corrector, noise, or hierarchy gate.** This report independently reconstructs the finite-N identity, its singular passage, exact centering, the specified quantitative approximation, and the full joint weak limit. It does not presume that THM-038 or any earlier theorem has passed an independent gate. The frozen R16 full proof supplies precisely the actual-law source assertion used below, in the required scope. Its gate remains separate. No admitted counterexample was found; the exact negation is excluded conditionally on that source assertion, not on a status label.

No R17 candidate derivation/checker, R16 audit/reconstruction, current R11–R15 result or audit, state/history content, memory, root scratch, external source, private source, or prior checker was read. The result is sealed before any comparison. Root alone may compare and integrate it. No canonical state was edited and no commit, push, installation, external search, or child task occurred.

## 1. Assertion, negation, and precise scope

Fix an integer \(d\ge3\), \(0<s\le d-2\) with \(s<d/2\), and a finite \(T\ge0\). Work on the unit-Haar torus with characters \(e^{2\pi i k\cdot x}\). The interaction is the frozen coefficient-one Riesz kernel

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},
 \qquad K=-\nabla g.
 \tag{1.1}
\]

The actual particles solve

\[
 dX_i=\frac1N\sum_{\ell\ne i}K(X_i-X_\ell)\,dt
       +\sqrt{2\nu_N}\,dW_i,
 \quad \nu_N=\beta_N^{-1},\quad
 X_i(0)\text{ iid Haar, independently of all }W_i.
 \tag{1.2}
\]

There is no external drift. The positive finite sequence obeys
\(\lambda_N=\beta_NN^{s/d-1}\to\lambda\in(0,\infty)\).
Set \(b_N=\min(\beta_N,1)\), \(\sigma_N=\sqrt{Nb_N}\), and
\(\eta_N=N^{-1}\sum_i\delta_{X_i}\).
For every fixed positive integer \(m\), every deterministic tuple
\((t_j,h_j)_{j=1}^m\) with \(t_j\in[0,T]\) and real smooth periodic \(h_j\), the claimed vector is

\[
 Z_{N,j}=\sigma_N\left(\eta_N(t_j)[h_j]-\bar h_j\right),
 \qquad \bar h_j=\int h_j\,dx.
 \tag{1.3}
\]

Define \(D_s(k)=4\pi^2c_{d,s}|k|^{s+2-d}\) for \(k\ne0\), and let \(S_t\) preserve constants and multiply mode \(k\ne0\) by \(e^{-tD_s(k)}\). The limit is the centered, possibly degenerate real Gaussian with

\[
 C_{ij}=\int(S_{t_i}h_i-\bar h_i)(S_{t_j}h_j-\bar h_j)\,dx
 =\sum_{k\ne0}\widehat h_i(k)\overline{\widehat h_j(k)}
                e^{-(t_i+t_j)D_s(k)}.
 \tag{1.4}
\]

The required sufficient approximation is, for each fixed coordinate on an eventual critical tail,

\[
 \mathbb E\left|Z_{N,j}-\frac1{\sqrt N}\sum_{a=1}^N
       (S_{t_j}h_j(X_a(0))-\bar h_j)\right|
 \le C\left(N^{s/d-1/2}+\sqrt{\nu_N}+\nu_N\right).
 \tag{1.5}
\]

The constant is independent of \(N\). It may depend on the fixed tuple, kernel, and positive upper/lower bounds for \(\lambda_N\) on the tail. Repeated and zero times, constants, all linear dependencies, and arbitrary fixed smooth tests are included. Exact Haar one-body marginals, with no inserted counterterm, are part of the assertion.

The exact negation is one admitted fixed datum, tuple, and critical sequence violating any centering, approximation, or weak-limit assertion. A failure of a proposed estimate, an arbitrary exchangeable law, or a statement outside this range is not the negation. No path-space/distribution-valued convergence, growing test list, threshold \(s=d/2\), logarithmic case, nonhomogeneous preparation, full subcritical law, or higher hierarchy is asserted or established here.

## 2. Input verification, exposure, and source preflight

The task and manifest were read before other files. All eleven prescribed input byte strings were verified at the root, copied into the isolated worktree and packet, and verified again. `INPUT_VERIFICATION.json` records all digests. The complete R16 source memorandum was read, including its scope, proof, limitations, and self-check status. Other mathematical reads were restricted to the allowlisted earlier material, chiefly the sections below.

| Input | Exact use and limitation |
|---|---|
| `AGENTS.md` | Campaign discipline. The specific blind task overrides generic README/specification/state/orchestration reading, canonical updating, and child work instructions. |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Interaction coefficient, noise, Haar/Fourier normalization, ordered distinct labels and denominator \(N^2\). |
| `MEMORANDA/ROUND_001_ALGEBRA.md`, Sections 1–2 | Smooth convention cross-check only. Section 5 below rederives the needed first-order identity directly from ordered sums. Its smooth diagonal convention is not applied to the singular kernel. |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–3 | Heat representation, coefficient one, integrable force, divergence measure and Coulomb compensation. These facts are checked in Section 3 below. An additional displayed part of Section 4 was visible in the bounded read; no pair-response theorem is used. |
| `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md` | Earlier scope only; its issued OPEN / UNAUDITED status is not a premise. |
| `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, Sections 2–8 | Local construction, energy noncollision, same-noise heat passage and fixed-N density domination. The required mechanisms are supplied in Sections 3 and 6 below. Neither corrector domains nor uniform-N density control is imported. |
| `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, Sections 2–3 | Cross-check of smooth free energy/Fatou and exact self subtraction. Its later corrector/response/noise discussion is a nondependency. |
| `THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md` | Explicitly conditional source assertion only, in exactly its admitted model and law class. |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md`, complete file | Complete conditional proof supplying the actual source bound and all its kernel/particle/energy mechanisms. No statement is inferred from its candidate status. |
| `THEOREMS/THM-039_CRITICAL_FINITE_DIMENSIONAL_HOMOGENEOUS_GAUSSIAN.md` | Exact target/negation and exclusions, unchanged. |
| `TASKS/ACTIVE/TASK-082_ROUND017_FINITE_DIMENSIONAL_BLIND.md` | Assignment, isolation and sealed handoff. |

Ambient exposure: this task context contained the global campaign contract, generic memory summary, and the parent's instruction that the R16 construction is conditional. No memory lookup was performed and no memory-derived mathematical fact is used. A required root Git-status check exposed filenames of dirty/untracked work, including the filename of an R17 memorandum, and creation of the worktree displayed the base commit's subject. No contents of those non-allowlisted files were read. A first batched read of allowed source files exceeded the tool output budget; the relevant allowed sections and the complete R16 file were subsequently read in bounded chunks. The R16 memorandum itself mentions its own diagnostic result; that prior checker and its artifacts were not opened, copied, or run. The new diagnostic was written independently.

The sole nontrivial uniform-in-N estimate imported as a conditional premise is the following entire actual-source statement from R16, for each fixed terminal time \(t\), smooth real \(h\), and bounded noise interval \([0,\nu_*]\): with the exact Fourier backward test \(f_r^\nu\),

\[
 \sup_{0\le r\le t}\mathbb E|P_N[J_{f_r^\nu}](X(r))|
 \le C_{d,s,t,\nu_*,h}N^{s/d-1}.
 \tag{2.1}
\]

Here the statistic is the original ordered deleted statistic with both original Haar contractions, and its singular terms are genuinely integrable. This is R16 (1.4)–(1.5), proved there in Sections 2–7. It is not an iid estimate at positive time. Its applicability uses \(d\ge3\), \(0<s\le d-2\), the same fixed kernel, actual homogeneous gradient dynamics, iid Haar preparation, and fixed smooth test. The extra restriction \(s<d/2\) is imposed only to make the scaled source vanish in THM-039. R16 allows zero noise, although the present sequence has positive noise.

The complete source verifies the following chain, rather than merely restating the card. R16 (3.6) differentiates smooth free energy with complete drift square; entropy is nonnegative and initial energy is zero. Same-noise fixed-N heat passage and a common lower bound permit Fatou in (3.7), giving actual expected energy at most zero. Its positive splitting (4.1)–(4.6) has retained positive Fourier weights, a nonnegative discarded kernel, exactly \(g_r(0)/(2N)\) self subtraction and \((N-1)c_r/(2N)\) background subtraction. Thus (4.7) controls both positive pieces by \(N^{-1}r^{-s/2}+r^{(d-s)/2}\). The logarithmic derivative estimate (6.1) gives the lattice commutator bound (6.2) uniformly in \(r\); summable fixed-test Fourier coefficients give (6.5). The termwise differentiated Gaussian bound (7.1) controls the singular remainder by the positive kernel at scale \(2r\), with the mass/contraction terms retained in (7.3). Choosing \(r=N^{-2/d}\) in an already proved deterministic inequality yields (2.1). No generic weighted positivity, source square, exchangeability-to-iid transfer, or simultaneous particle/scale limit enters that chain.

Those displayed facts and their constants match the needed premise in the admitted scope, including three-dimensional Coulomb and arbitrary smooth tests. This source preflight is not a promotion of R16's separate gate. The conditional implication proved in the rest of this report has no further uniform law-class assumption. No unavailable external theorem, citation, private input, pair inverse, cubic source, full corrector bracket, or unseen earlier gate is required.

## 3. Kernel and actual finite-N realization

Put \(\alpha=(d-s)/2\ge1\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). For the positive periodized Gaussian \(p_u\),

\[
 g(z)=A\int_0^\infty u^{\alpha-1}(p_u(z)-1)\,du.
 \tag{3.1}
\]

At small \(u\), \(\|p_u-1\|_1\le2\); at large \(u\), the zero-mean heat kernel decays exponentially. Taking the nonzero Fourier coefficient gives
\(A\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}=c_{d,s}|k|^{s-d}\).
The central Euclidean Gaussian integral, after substituting \(|z|^2/(4u)\), is exactly \(|z|^{-s}\). The other translates at small times have differentiated exponential bounds, and the large-time remainder is differentiable under the integral. Consequently \(g=|z|^{-s}+H\) near zero with \(H\) smooth, and \(g\) is smooth off zero with a finite lower bound \(g_*<0\).

The force is \(K(z)=sz|z|^{-s-2}-\nabla H(z)\), integrable because \(s+1<d\). Its distributional gradient identification has boundary error of order \(r^{d-1-s}\to0\). The divergence has the exact finite-measure form

\[
 D:=\operatorname{div}K=
 \begin{cases}
 s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \quad c_d=(d-2)|\mathbb S^{d-1}|=4\pi^2c_{d,d-2}.
 \tag{3.2}
\]

Indeed the inner-boundary flux is
\(s r^{d-s-2}\int_{\mathbb S^{d-1}}a(r\theta)d\theta\): it vanishes below Coulomb and tends to \(c_da(0)\) at Coulomb. The gamma recurrence identifies the lower-range density, and the frozen zero/nonzero Fourier coefficients determine the compensating Haar part. Thus \(D\ge-\kappa\,dx\), with \(\kappa\) fixed, \(\int D=0\), and \(\widehat D(k)=D_s(k)>0\) for nonzero modes. On the punctured torus \(\Delta g\le\kappa\); this punctured fact is not substituted for (3.2) in a convolution.

For completeness, the required finite-N process does not rely on an earlier status label. On the collision-free configuration space put

\[
 H_N=\frac1N\sum_{i<\ell}g(x_i-x_\ell),\qquad
 \mathcal E_N=H_N-\frac{N-1}{2}g_*\ge0.
\]

Every energy sublevel is compact away from every partial or simultaneous collision, since each shifted summand is nonnegative and its own colliding pair diverges. The drift is \(B=-\nabla H_N\), and differentiation in both coordinates of every unordered pair gives

\[
 \Delta_{Nd}H_N=\frac2N\sum_{i<\ell}\Delta g(x_i-x_\ell)
 \le(N-1)\kappa.
 \tag{3.3}
\]

Smooth collision cutoffs yield globally Lipschitz additive-noise equations. Subtracting the continuous driving path, Picard iteration gives measurable local solutions and Gronwall uniqueness; they agree before collision-excluded exits and patch. Stop the energy at level \(R\). Itô's formula on that compact sublevel, with complete drift square retained, gives

\[
 \mathbb E_x\mathcal E_N(X_{t\wedge\tau_R})
 \le\mathcal E_N(x)+\nu(N-1)\kappa t,
 \quad
 \mathbb P_x(\tau_R\le T)
 \le\frac{\mathcal E_N(x)+\nu(N-1)\kappa T}{R}.
 \tag{3.4}
\]

The stopped energy martingale has bracket
\(2\nu\int_0^{t\wedge\tau_R}|B|^2dr\), finite on the compact sublevel. Thus its expectation is zero. Bounded-energy paths extend by a finer cutoff, so letting \(R\to\infty\) proves global noncollision from every fixed collision-free initial state almost surely. Local uniqueness gives global pathwise uniqueness. The jointly measurable cutoff construction and Fubini apply this to independent iid Haar starts, which are collision-free almost surely and have finite mean shifted energy \(-(N-1)g_*/2\). A continuous collision-free path on a compact time interval has strictly positive minimum pair distance. No separation uniform in \(N\), initial data, or paths is asserted.

Let \(K_\varepsilon=p_\varepsilon*K\). It is smooth and odd and converges in \(C^1\) on each compact set away from zero: split \(K\) into a smooth local part and an integrable part supported a positive distance away, and use differentiated Gaussian bounds for the latter. Couple the heat and singular processes with identical starts and Brownian motions. Before their maximum discrepancy reaches one quarter of the singular path's minimum separation, the drifts have a common local Lipschitz bound and the Brownian increments cancel in the difference. Gronwall bounds that discrepancy by \(T\sup|B_\varepsilon-B|e^{LT}\to0\), preventing the stop for small \(\varepsilon\). Thus the whole heat family converges uniformly in time almost surely at each fixed \(N,\nu,T\). This is a fixed-N passage, with random local constants, before the large-N argument.

## 4. Exact centering and backward tests

For any fixed torus translation \(a\), the translated path \((X_i+a)_i\) solves the same equation with start \((X_i(0)+a)_i\) and the same Brownian drivers. The translated iid Haar vector has exactly the original law and remains independent of the drivers. Measurable realization and uniqueness therefore make the joint time-t law invariant under common translations. Its one-body marginals are translation invariant. For a nonzero mode choose \(a\) with \(e^{2\pi i k\cdot a}\ne1\); invariance forces its Fourier coefficient to vanish. Fourier uniqueness of finite measures gives Haar. This argument is for each fixed \(a,t\) and does not require a common exceptional set over uncountably many starts/translations. Therefore

\[
 \mathbb E\eta_N(t)[h]=\bar h\quad\text{for every deterministic }t.
 \tag{4.1}
\]

Higher marginals need not be independent. No deterministic pressure or other centering correction is present.

For a fixed terminal pair \((t,h)\), write \(\bar h=\int h\). Define

\[
 \widehat f_r^\nu(k)=\widehat h(k)
 e^{-(t-r)(4\pi^2\nu|k|^2+D_s(k))}\ (k\ne0),
 \qquad \widehat f_r^\nu(0)=\bar h,
 \quad 0\le r\le t.
 \tag{4.2}
\]

Every spatial derivative is bounded uniformly for \(\nu\) in a fixed bounded interval by a finite weighted absolute sum of the same smooth test's Fourier coefficients. The same holds for a time derivative after two extra powers of \(|k|\). No positivity-preserving property of \(S_t\) is needed; the mode multipliers have modulus at most one and give both these smooth bounds and the \(L^2\) contraction.

For \(J_f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y))\), off the diagonal, define its original Haar contraction
\(A f(x)=\int J_f(x,y)dy\). Oddness and \(K\in L^1\) give

\[
 A f(x)=-\int K(x-y)\cdot\nabla f(y)dy
       =-\int f(x+z)D(dz),
 \qquad \int A f=\iint J_f=0.
 \tag{4.3}
\]

The second equality is distributional integration by parts against the smooth test, justified by (3.2). In particular \(\widehat{Af}(k)=-D_s(k)\widehat f(k)\), and at Coulomb
\(Af=-c_d(f-\bar f)\), retaining atom and compensation. Thus

\[
 (\partial_r+\nu\Delta+A)f_r^\nu=0,
 \quad f_t^\nu=h,
 \quad f_0^\nu=e^{\nu t\Delta}S_th.
 \tag{4.4}
\]

## 5. Exact finite-N first-order identity from ordered sums

First take a smooth heat force \(K_\varepsilon\) and any smooth time-dependent scalar test \(f\). Direct Itô differentiation gives the ordered interaction contribution

\[
 \frac1{N^2}\sum_{i\ne\ell}
 K_\varepsilon(X_i-X_\ell)\cdot\nabla f(X_i)
 =\frac1{2N^2}\sum_{i\ne\ell}J_f^\varepsilon(X_i,X_\ell).
 \tag{5.1}
\]

This is relabeling the ordered sum and using oddness, so its factor is exactly one half. Write the full prescribed statistic as

\[
 P_N[J_f^\varepsilon]
 =\frac1{2N^2}\sum_{i\ne\ell}J_f^\varepsilon(X_i,X_\ell)
 -\frac1N\sum_i A_\varepsilon f(X_i)
 +\frac12\iint J_f^\varepsilon.
 \tag{5.2}
\]

The last term is zero by its actual Haar integral; the middle term is retained. Equation (5.1) is therefore \(P_N[J_f^\varepsilon]+\eta_N[A_\varepsilon f]\). Subtracting the Haar mean of \(f\), diffusion has zero Haar integral and \(A_\varepsilon\) has zero Haar mean. With \(\rho_N=\eta_N-dx\), the exact identity is

\[
 d\rho_N[f_r]=
 \{\rho_N[(\partial_r+\nu\Delta+A_\varepsilon)f_r]
   +P_N[J_{f_r}^\varepsilon]\}\,dr+dM_{N,r}^\varepsilon[f],
 \quad
 dM_{N,r}^\varepsilon[f]=\frac{\sqrt{2\nu}}N
          \sum_i\nabla f_r(X_i)\cdot dW_i.
 \tag{5.3}
\]

No \((N)_2\) denominator, extra \(1/N\) drift, or omitted Haar contraction is available. The smooth diagonal of \(J_f^\varepsilon\) is zero, but this calculation used ordered off-diagonal terms directly and does not assign a singular diagonal value.

Use the exact heat backward test \(f_r^{\nu,\varepsilon}\) obtained from (4.2) by replacing \(D_s(k)\) with
\(D_s(k)e^{-4\pi^2\varepsilon|k|^2}\). Its terminal datum is exactly \(h\). The bracketed linear term in (5.3) is zero. Integration gives

\[
 \rho_N^\varepsilon(t)[h]
 =\rho_N(0)[f_0^{\nu,\varepsilon}]
  +\int_0^tP_N[J_{f_r^{\nu,\varepsilon}}^\varepsilon]
                   (X^\varepsilon(r))dr
  +M_N^\varepsilon(t).
 \tag{5.4}
\]

## 6. Singular passage and the exact martingale coefficients

At fixed \(N,\nu,t\), the Fourier sums imply
\(f^{\nu,\varepsilon}\to f^\nu\) uniformly in time in every fixed spatial \(C^q\) norm, and also after one time derivative. Domination uses the fixed smooth Fourier coefficients and
\(4\pi^2\nu|k|^2+D_s(k)\); \(D_s(k)\) is bounded on nonzero lattice modes in this range. The heat paths converge as proved in Section 3 and eventually stay uniformly separated on each good path. It follows that every off-diagonal source evaluation in (5.4) converges uniformly in time on that path. The original contractions converge uniformly because
\(K_\varepsilon\to K\) in Haar \(L^1\) and the test gradients converge uniformly. Their time integrals therefore converge pathwise. No singular diagonal or collision trace is used.

The martingale integrands converge pointwise almost surely and are dominated by a deterministic bound on the test gradients. Itô isometry and dominated convergence on probability times time give
\(M_N^\varepsilon(t)\to M_N(t)\) in \(L^2\). Thus every term in (5.4) converges in probability to its stated limit, identifying the almost-sure equality

\[
 \boxed{\rho_N(t)[h]
 =\rho_N(0)[f_0^\nu]
  +\int_0^tP_N[J_{f_r^\nu}](X(r))dr
  +M_N(t),\qquad
 M_N(t)=\frac{\sqrt{2\nu}}N\sum_i\int_0^t
          \nabla f_r^\nu(X_i(r))\cdot dW_i(r).}
 \tag{6.1}
\]

The conditional actual source premise (2.1) makes its integral \(L^1\); joint measurability follows from the measurable path, deterministic smooth test and Borel off-diagonal kernel. Tonelli applies to the nonnegative absolute integrand. The singular identity did not require convergence of source expectations from smooth dynamics. Its pathwise passage is completed first, then the actual-law estimate is applied.

For terminal pairs indexed by \(i,j\), set \(f_{i,r}^\nu\) on \([0,t_i]\), and extend its integrand by zero after \(t_i\). Independence of Brownian coordinates gives the exact scaled cross bracket, at the terminal horizon,

\[
 \left\langle\sigma_NM_{N,i},\sigma_NM_{N,j}\right\rangle
 =2b_N\nu_N\int_0^{t_i\wedge t_j}
 \eta_N(r)[\nabla f_{i,r}^{\nu_N}\cdot\nabla f_{j,r}^{\nu_N}]\,dr.
 \tag{6.2}
\]

In particular, (4.1) and Itô isometry yield

\[
 \mathbb E|\sigma_NM_{N,j}|^2
 =2b_N\nu_N\int_0^{t_j}\|\nabla f_{j,r}^{\nu_N}\|_2^2dr
 \le C_jb_N\nu_N.
 \tag{6.3}
\]

Even without exact Haar centering the bounded-gradient estimate proves the same upper bound. Haar here computes the precise expected bracket, not a product-law surrogate. No independence from the initial fluctuation is claimed or needed. The entire martingale vector tends to zero in \(L^2\) coordinatewise on the critical tail; there is no positive limiting thermal martingale.

## 7. Quantitative approximation and critical scaling

Let \(a=s/d<1/2\). For tail bounds \(0<\ell\le\lambda_N\le L<\infty\),

\[
 \beta_N=\lambda_NN^{1-a}\to\infty,
 \qquad \nu_N=\lambda_N^{-1}N^{a-1}\to0.
 \tag{7.1}
\]

After increasing the tail threshold using \(\ell\), we have \(\nu_N\le1\), \(b_N=1\), \(\sigma_N=\sqrt N\). The identity (6.1), multiplied by \(\sqrt N\), uses the same process as the frozen card. Apply (2.1) separately with terminal time \(t_j\), test \(h_j\), and \(\nu_*=1\), to obtain

\[
 \mathbb E\left|\sqrt N\int_0^{t_j}P_N[J_{f_{j,r}^{\nu_N}}]dr\right|
 \le C_j t_j N^{a-1/2}.
 \tag{7.2}
\]

This is an actual-law \(L^1\) error. Equation (6.3) and Cauchy–Schwarz bound the martingale error by \(C_j\sqrt{\nu_N}\).

It remains to replace the \(N\)-dependent initial test without losing \(\sqrt N\). Set
\(q_N=f_{j,0}^{\nu_N}-S_{t_j}h_j\). It has exactly zero Haar mean. Parseval, the contraction of \(S_{t_j}\), and \(1-e^{-x}\le x\) give

\[
 \|q_N\|_2^2
 =\sum_{k\ne0}|\widehat h_j(k)|^2e^{-2t_jD_s(k)}
       |e^{-4\pi^2\nu_Nt_j|k|^2}-1|^2
 \le \nu_N^2t_j^2\|\Delta h_j\|_2^2.
 \tag{7.3}
\]

Independence and exact mean zero at the initial time now give the precise variance cancellation

\[
 \mathbb E\left|\frac1{\sqrt N}\sum_{a=1}^Nq_N(X_a(0))\right|^2
 =\|q_N\|_2^2.
 \tag{7.4}
\]

All unequal-label terms vanish, rather than contributing an uncontrolled \(N\)-factor. Therefore the \(L^1\) replacement error is at most \(\nu_Nt_j\|\Delta h_j\|_2\). Combining (7.2), (6.3), and (7.4) proves exactly (1.5), with one common constant for the fixed finite tuple after taking a maximum. At \(t_j=0\), all three errors are zero on the tail. All powers on its right tend to zero; in particular the decisive source exponent is strictly negative precisely in the admitted \(s<d/2\) range. No old energy-floor temperature condition is inserted.

For clarity, finitely many indices before this eventual threshold do not enter either the quantitative tail assertion or the weak limit. We have not equated \(\sigma_N\) with \(\sqrt N\) before proving that \(b_N=1\) on the tail.

## 8. Full joint probability limit, including singular covariance

Define the fixed real smooth centered functions
\(v_j=S_{t_j}h_j-\bar h_j\). If \(U_a=X_a(0)\), the vectors
\(Y_a=(v_1(U_a),\ldots,v_m(U_a))\) are iid, bounded, centered, and independent of \(N\). Their covariance is the real Gram matrix \(C\) in (1.4), hence is symmetric and positive semidefinite. No matrix inverse is needed. Define the possibly degenerate Gaussian \(G=C^{1/2}\xi\), where \(\xi\) has independent standard real Gaussian coordinates.

Put \(V_N=N^{-1/2}\sum_{a=1}^NY_a\). For each fixed \(\theta\in\mathbb R^m\), let \(Q=\theta\cdot Y_1\). Taylor's formula with absolute third remainder gives

\[
 \mathbb E e^{iQ/\sqrt N}
 =1-\frac{\theta^TC\theta}{2N}+r_N(\theta),
 \qquad |r_N(\theta)|\le\frac{\mathbb E|Q|^3}{6N^{3/2}}.
 \tag{8.1}
\]

Independence yields
\(\mathbb E e^{i\theta\cdot V_N}=(\mathbb Ee^{iQ/\sqrt N})^N
\to e^{-\theta^TC\theta/2}\). To justify this last scalar limit, write the factor as \(1+z_N\), where \(Nz_N\to-\theta^TC\theta/2\) and \(N|z_N|^2\to0\); the power-series bound \(\log(1+z)=z+O(|z|^2)\) applies eventually. If \(\theta^TC\theta=0\), then \(Q=0\) almost surely because its mean square is zero, and the characteristic function is exactly one. There is no division by a variance or nondegeneracy assumption.

Here is an explicit weak-convergence passage, so that (8.1) is not left as a formal characteristic-function calculation. Let \(\zeta\) be an independent standard Gaussian in \(\mathbb R^m\), and fix \(\delta>0\). The random vectors \(V_N+\delta\zeta\) and \(G+\delta\zeta\) have densities. The elementary Gaussian Fourier integral and Fubini express the former as

\[
 p_{N,\delta}(x)=(2\pi)^{-m}\int_{\mathbb R^m}
 e^{-i\theta\cdot x}\,
 \mathbb E e^{i\theta\cdot V_N}
 e^{-\delta^2|\theta|^2/2}\,d\theta.
 \tag{8.2}
\]

The Gaussian factor is integrable, the other characteristic-function factor has modulus at most one, and (8.1) gives pointwise convergence. Dominated convergence gives convergence of these densities at every \(x\) to \(p_\delta\), the density of \(G+\delta\zeta\). Both are probability densities. Since \(\min(p_{N,\delta},p_\delta)\le p_\delta\), dominated convergence gives
\(\int\min(p_{N,\delta},p_\delta)\to1\); hence
\(\|p_{N,\delta}-p_\delta\|_1\to0\).
This remains valid when \(C\) is singular, since only the added \(\delta^2I\) is inverted implicitly by the Gaussian density.

For every bounded Lipschitz function \(F\),

\[
 |\mathbb EF(V_N)-\mathbb EF(G)|
 \le2\operatorname{Lip}(F)\,\delta\,\mathbb E|\zeta|
   +\|F\|_\infty\|p_{N,\delta}-p_\delta\|_1.
 \tag{8.3}
\]

First let \(N\to\infty\), then \(\delta\downarrow0\). This proves convergence for bounded Lipschitz tests. To obtain the definition of weak convergence for every bounded continuous \(F\), note the uniform tightness bound

\[
 \mathbb P(|V_N|>R)\le\frac{\operatorname{tr}C}{R^2},
 \qquad \mathbb P(|G|>R)\le\frac{\operatorname{tr}C}{R^2}.
 \tag{8.4}
\]

On the compact ball of radius \(R\), uniform continuity permits uniformly approximating \(F\) by a bounded Lipschitz function: for example interpolate a finite sufficiently fine net by the infimum of finitely many Lipschitz cones and clip at \(\pm\|F\|_\infty\). The compact error can be made arbitrarily small, and the errors outside the ball are bounded by \(2\|F\|_\infty\) times the tail probabilities in (8.4). Apply (8.3), then send the compact error to zero and \(R\to\infty\). This proves \(V_N\Rightarrow G\) without an unverified compactness or Fourier-continuity step.

Finally, (1.5) gives
\(\mathbb E|Z_N-V_N|\le\sum_j\mathbb E|Z_{N,j}-V_{N,j}|\to0\).
For bounded Lipschitz \(F\), the difference of expectations is at most
\(\operatorname{Lip}(F)\mathbb E|Z_N-V_N|\). Tightness of \(Z_N\) follows from (8.4) and Markov applied to this difference; finitely many initial indices can be added to any compact bound. The same compact approximation now proves \(Z_N\Rightarrow G\). Neither independence of the residual from the initial vector nor an \(L^2\) source estimate is necessary.

The Fourier equality in (1.4) follows from Parseval for the real smooth functions \(v_i,v_j\); its sum is absolutely convergent by Cauchy–Schwarz (indeed smoothness is stronger). Realness follows from conjugate symmetry. The damping uses the sum \(t_i+t_j\), since both coordinates are functions of the same initial vector, not independent increments. Repeated coordinates produce the corresponding exact linear dependence; zero times have multiplier one; constant tests produce the zero function and zero Gaussian coordinates. Every possible singular Gram matrix is handled by the same argument.

## 9. Independent falsification route and exact diagnostics

A complementary route probes the literal initial generator on a smooth Fourier mode, rather than using the source bound and backward identity. Let
\(Z_k=N^{-1}\sum_i e^{2\pi i k\cdot X_i}\), \(k\ne0\). The \(N\) self terms in \(|Z_k|^2\) are constants; distinct labels have Haar mean zero initially. Direct integration of the literal generator against initial product Haar gives

\[
 \mathbb E|Z_k(0)|^2=\frac1N,
 \qquad
 \left.\frac d{dt}\mathbb E|Z_k(t)|^2\right|_{t=0}
 =-\frac{2(N-1)}{N^2}D_s(k).
 \tag{9.1}
\]

Here is the coefficient count. In a distinct pair's mode difference, the two internal forces together have factor \(2/N\); forces containing any third label integrate to zero against initial Haar. Integrating the remaining pair force against the derivative of the Fourier mode uses \(\widehat D(k)=D_s(k)\) and gives \(-2D_s(k)/N\). Multiplying by the ordered distinct-pair fraction \((N-1)/N\) gives (9.1). Diffusion integrates to zero against the initial constant configuration density; its damping and martingale terms cancel in this initial derivative. The negative sign agrees with the limiting damping, and omitting the internal-pair factor, self terms, or Coulomb atom changes the result.

This derivative has a legitimate singular meaning at fixed \(N\). The generator of this smooth observable is Haar \(L^1\) because \(K\in L^1\). The heat flow divergence obeys
\(\operatorname{div}_{Nd}B_\varepsilon\ge-(N-1)\kappa\), retaining the full measure in (3.2). The pathwise smooth flow Jacobian is at least \(e^{-(N-1)\kappa t}\); change of variables against initial Haar gives a density at most \(e^{(N-1)\kappa t}\). Fixed-N path passage extends the measure bound first on continuous tests, then on Borel sets by open approximation and outer regularity. Thus the singular laws have this same finite-N density bound. Approximate the integrable generator in Haar \(L^1\) by continuous functions; this density bound controls the approximation uniformly near zero time, while path continuity handles the continuous functions. Taking expectations in a stopped Itô identity and using time integrability of the force gives the full integrated generator identity and its right derivative (9.1). No density constant uniform in \(N\) is used.

This falsification test is consistent with the theorem; it neither asserts convergence of second moments at later times from an \(L^1\) approximation nor interchanges an \(N\)-limit with a derivative at zero. At three-dimensional Coulomb, \(D_s(k)=4\pi\) for every nonzero \(k\), so the test specifically detects losing the atom. At \(T=0\), the theorem is precisely a fixed iid finite-dimensional central limit assertion on the eventual \(\sqrt N\) scale. A constant test is identically zero for every \(N\), including before that tail. Repeated tests/times force, rather than obstruct, Gaussian degeneracy.

The independently written standard-library diagnostic is
`ROUND_017_GAUSSIAN_BLIND_ARTIFACTS/round017_gaussian_blind_exact.py`.
It uses exact rational and Gaussian-rational Laurent polynomials, no randomness, no floating tolerance, and no prior input/checker code. Derivatives are divided by \(2\pi\), so the source/generator/bracket identities are in units of \((2\pi)^2\); restoring this common factor gives the physical convention. Smooth finite Fourier kernels on one torus coordinate embedded in higher dimensions probe exact coefficients only, not the singular estimate.

The diagnostic compares literal ordered particle generators with independently assembled original deleted statistics and Haar contractions; checks source symmetry, zero smooth diagonal and zero double contraction; checks the exact scaled cross bracket; computes the actual initial Fourier-variance derivative; counts iid covariance and fourth-moment label partitions; checks joint sum-of-times covariance, real Gram positivity and degeneracy; and enumerates the critical scaling range. Deliberately wrong source halves, denominators, response signs, martingale normalization and damping signs are required to fail. Rational semigroup multipliers in the covariance examples are declared algebraic probes; no claim that those arbitrary rational values are the Riesz spectrum is made.

Command: `python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_017_GAUSSIAN_BLIND_ARTIFACTS/round017_gaussian_blind_exact.py`. Outcome: **PASS, 2,447 exact assertions in 31 categories**. The companion JSON records every category, declared conventions, covariance examples, scaling cases, and the diagnostic script digest. The exact diagnostic supports the coefficient audit; the analytic proof establishes the continuum implication.

## 10. Dispositions and immutable handoff

| Item | Disposition |
|---|---|
| Genuine singular first-order identity, all finite-N coefficients and original contractions | RECONSTRUCTED HERE, with fixed-N heat path and martingale passages. |
| Exact one-body Haar centering | PROVED HERE from translation equivariance, measurable realization and uniqueness. |
| Specified quantitative approximation | PROVED HERE CONDITIONAL ON THE EXPLICIT COMPLETE R16 ACTUAL-SOURCE PREMISE. |
| Full joint centered Gaussian limit and covariance, repeated/zero times, constants and degenerate covariance | PROVED HERE under the same sole uniform source premise, with explicit weak-convergence passage. |
| THM-039 exact negation | Excluded under that explicit premise; no admitted counterexample constructed. No unconditional certification based on an unpassed source label. |
| R16 source status | Unchanged as issued. Its complete proof was checked for exact applicability and sufficiency; its separate whole-claim source gate is not presumed passed. |
| Pair inverse, corrector/cubic/noise gates or higher hierarchy | NONDEPENDENCIES of this finite-dimensional implication. No wider result is promoted. |
| Independent audit status | This is a fresh reconstruction relative to the unseen R17 constructor, with its own self-check. It is not a separate hostile review of itself; root must compare after the seal and obtain any further required review. |

The complete report and independent diagnostics are the bounded handoff. The packet README records verified input/output manifests, diagnostics, ambient exposure, archive member safety and immutable seals. Corrections after issuance must be separate superseding documents. No source input or issued earlier report was edited in place; task-authorized copies were the only changes outside this lane's new report/artifact paths. The remaining integration action is root comparison, exact source gating, separate hostile review as required, and canonical disposition. No scientific scope decision or unavailable private input was needed for this reconstruction.
