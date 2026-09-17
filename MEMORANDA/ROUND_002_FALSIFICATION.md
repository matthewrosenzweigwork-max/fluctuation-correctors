# Round 002 independent falsification: smooth iid residual

Date: 2026-09-17 UTC. Task: TASK-011. Worker: `/root/r002_falsification`, fresh gpt-6-astra Max context. Worktree: `/private/tmp/hocf-round002-falsification-20260917`. Input commit: `a06178658d1e3d458536ff312ca793947212ec67`; historical frozen baseline: `475a5399828bc6e2ccbade08c59b8778638df14a`.

## 1. Verdict and isolation

**No counterexample to the exact fixed-smooth iid assertion was found. A self-contained independent proof candidate is given below, in addition to the falsification tests.** It controls the evolved interacting law and proves stronger quantitative bounds than the three requested limits. This conclusion follows from the proof in Sections 3–5, not from the passing finite tests.

- Mathematical status: `PROVED_CANDIDATE` for the fixed-smooth iid assertion under exactly the uniform bounds in `PO-001_RESIDUAL.md`.
- Audit status of this report's new proof: `SELF_CHECKED`. This worker was isolated from the Round 002 constructor, but has not reviewed that constructor's proof; this is not a hostile verdict on an unseen proof. Root comparison and a separate hostile audit remain necessary for promotion.
- Source status: self-contained finite sums, smooth stochastic calculus, and elementary Fourier estimates. No external propagation-of-chaos, equilibrium, CLT, or singular-limit theorem is imported.
- Scope: arbitrary sequences of finite positive inverse temperatures, fixed smooth interaction and confinement, fixed finite horizon, iid preparation, and the stated deterministic uniform spatial bounds. No cutoff-uniform, singular, long-time, equilibrium-prepared, field-limit, or corrector-order-uniform theorem is claimed.

The inputs read were the governing root instructions/specifications, frozen baseline and state ledgers, `ROUND_001_MODEL.md`, `PO-001_RESIDUAL.md`, TASK-011, the definitions in `THM-008_SMOOTH_PAIR.md` and `COR-001_PAIR_CORRECTOR.md`, and the supplied source-note text. No Round 002 constructor output or other Round 002 worktree was read. The source note supplies no estimate used here. No canonical ledger, frozen input, or prior report was edited.

The exact assertion and its negation are those of `PO-001_RESIDUAL.md`: every permitted sequence has all three scaled endpoint/residual/bracket quantities tending to zero; its negation is one fixed permitted data set and temperature sequence with a positive limsup in at least one quantity, or a necessary uniform constant left unproved. Sections 3–5 rule out that negation within the fixed-smooth scope, subject to independent review of this proof.

## 2. Exact algebra and the first possible failure

Write \(\eta=N^{-1}\sum_i\delta_{X_i}\), \(\rho=\eta-\mu\), and \(\nu=1/\beta\). At each time, for a symmetric smooth pair kernel \(\Phi\),

\[
 2P_N[\Phi]=U_2[\Phi]
 =\rho^{\otimes2}(\Phi)-\frac1N\eta(\Phi(x,x)). \tag{2.1}
\]

For a symmetric smooth triple kernel \(F\), exact inclusion–exclusion gives

\[
 U_3[F]=\rho^{\otimes3}(F)
 -\frac3N\int\eta(dx)\rho(dy)F(x,x,y)
 +\frac2{N^2}\eta(F(x,x,x)). \tag{2.2}
\]

To check (2.2), expand the ordered distinct triple sum as the full product minus the three pair coincidences plus twice the triple coincidence. Each of the three occupied-pair/background terms then restores one of the deleted pair coincidences with its remaining variable integrated against \(\mu\). This proof deletes labels, including at coincident coordinates. It also applies when \(N=2\).

For iid sampling from the current background, the exact biases are

\[
 \mathbb E U_2[\Phi]=-\frac{\mu^{\otimes2}(\Phi)}N,
 \qquad
 \mathbb E U_3[F]=\frac{2\mu^{\otimes3}(F)}{N^2}. \tag{2.3}
\]

In particular, the pair bias is not generally minus the background diagonal integral divided by \(N\). The centered full product already has its own diagonal contribution. For constant kernels, \(U_2[1]=-1/N\) and \(U_3[1]=2/N^2\) deterministically. Evolved interacting particles are not iid, so (2.3) cannot be used at positive time without a law-specific argument.

The pair noise integrand is exactly

\[
 H_i[\Phi]=\int\rho(dy)\nabla_x\Phi(X_i,y)
 -\frac1N\nabla_x\Phi(X_i,X_i). \tag{2.4}
\]

The derivative in the last term is the first-slot derivative, not the total derivative along the diagonal. Direct differentiation of (2.1) verifies the factor: symmetry supplies two first-slot derivatives, canceled by the factor \(1/2\) in \(P_N\). Therefore

\[
 \frac{d[M_\Phi]}{dt}=rac{2}{\beta N^2}\sum_i|H_i|^2,
 \quad
 \frac{d[M_f,M_\Phi]}{dt}
 =\frac{2}{\beta N^2}\sum_i\nabla f(X_i)\cdot H_i. \tag{2.5}
\]

The potentially dangerous high-temperature prefactor is neutralized by precisely the scale in the task:

\[
 \sigma_N^2=N\min(\beta_N,1),\qquad
 \frac{\sigma_N^2}{\beta_N N}
 =\min(1,\beta_N^{-1})\le1. \tag{2.6}
\]

This observation alone proves nothing about \(H_i\). The actual missing estimate is its decay under the evolved law, together with a sixth-moment bound on smooth linear statistics sufficient to control the cubic full product. A coupling argument proves these estimates below without a temperature-dependent constant.

## 3. Uniform moment estimate for the actual interacting law

All constants in this section depend only on \(d,T\), the supremum norm and Lipschitz constant of the fixed \(K\), and the Lipschitz constant of \(b\). They are independent of \(N\), \(\beta>0\), the speed of background evolution, and all spatial derivatives of \(\mu\). These independence statements are proved, not assumed.

For each particle, use the same initial point and Brownian motion to define an independent nonlinear particle

\[
 dY_i=(b+K*\mu_t)(Y_i)dt+\sqrt{2/\beta}\,dW_i,
 \qquad Y_i(0)=X_i(0). \tag{3.1}
\]

Because the reference is deterministic and the initial pairs/Brownian motions are independent across labels, the \(Y_i\)'s are iid at every time. Their common law is \(\mu_t\): both solve the same linear Fokker–Planck equation with prescribed drift \(b+K*\mu_t\) and the same initial density. Uniqueness follows, for example, by the elementary \(L^2\) energy inequality for the difference of two smooth densities, with coefficient \(\|\operatorname{div}(b+K*\mu_t)\|_\infty\le \|\operatorname{div}b\|_\infty+\|\operatorname{div}K\|_\infty\). Smooth torus coefficients and positive finite diffusivity justify this argument; no uniform lower bound on diffusivity is used in the inequality.

Lift both processes to \(\mathbb R^d\) with the same initial representative and the same Brownian path, extending their drifts periodically. Set \(e_i=X_i-Y_i\) for those lifts. The Brownian parts cancel **exactly**, even when \(\beta\) tends to zero. Since \(K(0)=0\), insert the self-label into the interaction sum and write the forcing error at the independent system as

\[
 Z_i(t)=\frac1N\sum_{j\ne i}
 \{K(Y_i-Y_j)-(K*\mu_t)(Y_i)\}
 -\frac1N(K*\mu_t)(Y_i). \tag{3.2}
\]

Conditional on \(Y_i\), the summands in braces are centered and independent. Their components are bounded by \(2B\), where \(B=\|K\|_\infty\), using the Euclidean vector norm. A sixth-power expansion has no term with a singleton label. For \(M\) scalar summands bounded by \(2B\), the possible label multiplicities are \(6\), \(4+2\), \(3+3\), and \(2+2+2\), giving an upper bound

\[
 (2B)^6\{M+25M(M-1)+15M(M-1)(M-2)\}
 \le 41(2B)^6 N^3. \tag{3.3}
\]

Apply this conditionally, then take the \(L^6\) norm, sum vector components, and retain the final bias in (3.2). One obtains the explicit sufficient bound

\[
 \sup_t\|Z_i(t)\|_{L^6}
 \le c_d B N^{-1/2},\qquad c_d=2d\,41^{1/6}+1. \tag{3.4}
\]

No conditional independence of the interacting \(X_i\)'s was asserted.

Let \(L_b,L_K\) be Euclidean Lipschitz constants of the periodic extensions. Pathwise drift comparison gives

\[
 |e_i(t)|\le\int_0^t
 \left((L_b+L_K)|e_i(s)|
  +\frac{L_K}{N}\sum_j|e_j(s)|+|Z_i(s)|\right)ds. \tag{3.5}
\]

By exchangeability, Minkowski's inequality and Gronwall,

\[
 \sup_{t\le T}\|e_i(t)\|_{L^6}
 \le D_T N^{-1/2},\qquad
 D_T=c_d BT e^{(L_b+2L_K)T}. \tag{3.6}
\]

This estimate remains valid for a genuinely time-dependent background and arbitrary finite positive temperature. It does not differentiate \(\mu_t\) or estimate \(\nu\Delta\mu_t\).

For \(e_k(x)=e^{2\pi i k\cdot x}\), decompose the linear statistic into its coupling error and iid empirical error. The former is bounded in \(L^6\) by \(2\pi|k|D_TN^{-1/2}\). For the latter, apply the same sixth-moment count to the real and imaginary parts of \(e_k(Y_i)-\mu_t(e_k)\), whose absolute values are at most two. Thus

\[
 \sup_{N,\beta,t}
 \frac{\sqrt N\,\|\rho_t(e_k)\|_{L^6}}{1+|k|}
 \le D'_T<\infty. \tag{3.7}
\]

One may take \(D'_T=2\pi D_T+4\,41^{1/6}\). The same bound holds in \(L^p\), \(1\le p\le6\). This is the uniform moment estimate whose absence would invalidate a proof based only on finite tests. Equations (3.1)–(3.7) supply its complete fixed-smooth proof candidate.

## 4. Fourier estimates, including all diagonals

For a function on \(\mathbb T^D\), repeated integration by parts in a coordinate with largest frequency gives

\[
 |\widehat G(\xi)|\le c_{D,m}\|G\|_{C^m}
 (1+|\xi|)^{-m}. \tag{4.1}
\]

Hence weighted absolute Fourier sums of degree \(j\) are bounded by \(c\|G\|_{C^m}\) whenever \(m>D+j\). This follows by comparing the lattice sum with radial shells; there is no Sobolev embedding or hidden moment input here. Approximate by finite Fourier sums first; the displayed absolute bounds allow their passage in \(L^2\) and against finite signed measures.

For the full pair product, (3.7), Hölder with \(L^4\), and (4.1) with \(D=2d\), \(j=2\), \(m=2d+3\), give

\[
 \|\rho_t^{\otimes2}(\Phi_t)\|_{L^2}
 \le \frac{C\|\Phi_t\|_{C^{2d+3}}}{N}. \tag{4.2}
\]

The diagonal contribution in (2.1) is bounded by \(\|\Phi\|_\infty/N\). This proves the required initial estimate and, in fact, the same estimate at each positive time under the actual interacting law.

For a symmetric triple kernel, use Hölder with three \(L^6\) factors and \(D=3d,j=3,m=3d+4\):

\[
 \|\rho_t^{\otimes3}(F_t)\|_{L^2}
 \le C N^{-3/2}\|F_t\|_{C^{3d+4}}. \tag{4.3}
\]

For \(G(x,y)=F(x,x,y)\), the remaining random diagonal term is not estimated by its deterministic total variation. Instead, expand \(G\) in two-variable Fourier modes. Since \(|\eta(e_k)|\le1\), (3.7) and (4.1) with \(D=2d,j=1,m=2d+2\) give

\[
 \left\|\int\eta(dx)\rho(dy)G(x,y)\right\|_{L^2}
 \le C N^{-1/2}\|G\|_{C^{2d+2}}. \tag{4.4}
\]

The diagonal composition costs only a dimension/derivative-order constant. The last term in (2.2) is bounded by \(2\|F\|_\infty/N^2\). Combining all three terms,

\[
 \sup_{t\le T}\|U_3[F_t]\|_{L^2}
 \le C N^{-3/2}\sup_t\|F_t\|_{C^{3d+4}}. \tag{4.5}
\]

For the actual source

\[
 F_t=C\Phi_t
 =\operatorname{Sym}_3[K(x-z)\cdot\nabla_x\Phi_t(x,y)],
\]

Leibniz's rule gives, with \(m=3d+4\),

\[
 \|F_t\|_{C^m}
 \le d\,2^m\|K\|_{C^m}\|\Phi_t\|_{C^{m+1}}. \tag{4.6}
\]

Here the symmetrization is the average over six permutations. All the requested derivatives are available under \(r=4d+12\). No alternate lower-regularity theorem is being substituted for the task's assumption.

For (2.4), use the same two-variable Fourier argument on \(\nabla_x\Phi(x,y)\), taking a supremum over the first variable before substituting the random \(X_i\). It proves

\[
 \left\|\sup_x\left|\int\rho_t(dy)\nabla_x\Phi_t(x,y)\right|\right\|_{L^2}
 \le C A N^{-1/2},
 \qquad \sup_i\|H_i(t)\|_{L^2}\le C N^{-1/2}. \tag{4.7}
\]

Only \(\Phi\)'s \(C^{2d+3}\) norm is needed in this particular estimate. Taking the supremum before substitution avoids any invalid independence assumption between the root particle and its empirical discrepancy.

## 5. The three requested quantities

Let \(m_N=\min(\beta_N,1)\). A constant \(C\) depending only on \(d,T,A\), \(\|b\|_{C^1}\), and finitely many displayed smooth norms of \(K\) satisfies

| Quantity | Raw bound | Bound at the task's scale |
|---|---:|---:|
| Initial pair \(\mathbb E|P_N[\Phi_0]|\) | \(C/N\) | \(C\sqrt{m_N}/\sqrt N\) |
| Absolute integrated cubic \(\mathbb E|\int_0^T U_3[C\Phi_t]dt|\) | \(C/N^{3/2}\) | \(C\sqrt{m_N}/N\) |
| Pair bracket \(\mathbb E[M_\Phi]_T\) | \(C/(\beta_N N^2)\) | \(C\min(1,\beta_N^{-1})/N\) |
| Absolute cross bracket \(\mathbb E|[M_f,M_\Phi]_T|\) | \(C/(\beta_N N^{3/2})\) | \(C\min(1,\beta_N^{-1})/\sqrt N\) |

The first two rows are scaled by \(\sigma_N\), and the last two by \(\sigma_N^2\). For the integrated cubic, Minkowski gives the stronger \(L^2\) bound \(CTN^{-3/2}\); no signed cancellation or temporal decorrelation is needed. For the brackets, insert (4.7) in (2.5). For the cross bracket, take the absolute value inside the time integral and particle sum, use \(\|\nabla f\|_\infty\le c_d A\), and use Cauchy–Schwarz on \(H_i\). Thus its requested absolute value is controlled, not merely its signed expectation.

All four scaled quantities tend to zero for **every** positive temperature sequence, including arbitrary rates of \(\beta_N\downarrow0\) and \(\beta_N\uparrow\infty\). Raw bracket bounds may grow at high temperature; that does not contradict the scaled claim. The lower drift contractions remain bounded by \(C\sigma_N/N\) as in the task. The proof concerns this residual assertion only; it does not identify a limiting covariance, prove a CLT, or close a campaign theorem about singular critical laws.

## 6. Free heat/Fourier falsification

### 6.1 Actual corrector versus diagnostic kernels

For \(K=b=0\), the actual forcing \(J_f\) is zero and the zero-terminal pair corrector is identically zero. All three quantities in the task then vanish exactly. A nonzero arbitrary pair probe in this model is a test of the diagonal and bracket formulas, not a nonzero instance of the actual corrector. This distinction prevents a vacuous heat test from being presented as evidence for the interacting residual.

Take iid uniform particles, let \(k\ne0\), \(q=2\pi|k|\), and \(Z_j=N^{-1}\sum_i e^{2\pi i j k\cdot X_i}\). Complex probes are used solely to simplify algebra; real and imaginary parts give real tests. For \(\Phi=e_k\otimes e_k\) and \(F=e_k^{\otimes3}\),

\[
 U_2=Z_1^2-Z_2/N,\qquad
 U_3=Z_1^3-3Z_1Z_2/N+2Z_3/N^2. \tag{6.1}
\]

Counting matching ordered labels gives

\[
 \mathbb E|P_N|^2=\frac{N-1}{2N^3},\qquad
 \mathbb E|U_3|^2=\frac{6(N)_3}{N^6}. \tag{6.2}
\]

The second quantity is exactly zero for \(N=2\). Under independent heat dynamics, for \(t\ge s\),

\[
 \mathbb E[U_3(t)\overline{U_3(s)}]
 =\frac{6(N)_3}{N^6}e^{-c(t-s)},\qquad c=3q^2/\beta. \tag{6.3}
\]

Each occupied label contributes one heat eigenvalue; independence and the same matching count prove (6.3). Consequently,

\[
 \mathbb E\left|\int_0^T U_3(t)dt\right|^2
 =\frac{12(N)_3}{N^6}
 \left(\frac{T}{c}-\frac{1-e^{-cT}}{c^2}\right). \tag{6.4}
\]

As \(\beta\to\infty\), the bracketed factor tends to \(T^2/2\). As \(\beta\to0\), it is asymptotic to \(T\beta/(3q^2)\). Neither endpoint produces a surviving scaled cubic. The proof of Section 5 does not rely on this favorable free temporal decorrelation.

The exact positive complex pair bracket satisfies

\[
 \mathbb E\frac{d[M_\Phi,\overline M_\Phi]}{dt}
 =\frac{2q^2}{\beta}\frac{N-1}{N^3}. \tag{6.5}
\]

For the one-body probe \(e_{2k}\),

\[
 \frac{d[M_{e_{2k}},\overline M_\Phi]}{dt}
 =\frac{4q^2}{\beta N}\left(|Z_1|^2-\frac1N\right),\qquad
 \mathbb E\left(|Z_1|^2-\frac1N\right)^2
 =\frac{N-1}{N^3}. \tag{6.6}
\]

The signed expectation in (6.6) vanishes, but its absolute value does not vanish identically. It must still be bounded. Deterministic backward-heat amplitudes of modulus at most one can be inserted without worsening these estimates. In particular both scaled brackets are uniformly small at both temperature endpoints.

### 6.2 Time-dependent nonuniform background

In dimension one take \(\mu_0(x)=1+\varepsilon\cos(2\pi x)\), \(0<|\varepsilon|<1\), and keep \(K=b=0\). Then

\[
 \mu_t(x)=1+\varepsilon e^{-q^2t/\beta}\cos(qx),
 \quad q=2\pi,
 \quad m_t=\mu_t(\cos(qx))=\frac\varepsilon2e^{-q^2t/\beta}. \tag{6.7}
\]

All spatial derivatives are uniformly bounded across \(\beta>0\), although time derivatives need not be. The law remains iid with this moving background, so (2.3) holds at every time. For the complex pair/triple probes in (6.1), their means are respectively \(-m_t^2/N\) and \(2m_t^3/N^2\), not zero.

For the real pair probe \(\Phi(x,y)=\cos(qx)\cos(qy)\), conditioning on the root particle gives the exact formulas

\[
 \mathbb E\frac{d[M_\Phi]}{dt}
 =\frac{q^2}{\beta N^3}
 \{(N-1)(1/2-m_t^2)+m_t^2\}, \tag{6.8}
\]

\[
 \mathbb E\frac{d[M_{\cos(q\cdot)},M_\Phi]}{dt}
 =-\frac{q^2m_t}{\beta N^2}. \tag{6.9}
\]

For clarity, the general iid conditional formula behind these checks is, with \(a(x,y)=\nabla_x\Phi(x,y)\) and \(h(x)=\mu(a(x,\cdot))\),

\[
 \mathbb E[H_i\mid X_i=x]=-h(x)/N,
 \quad
 \mathbb E[|H_i|^2\mid X_i=x]
 =\frac{N-1}{N^2}\mu(|a(x,\cdot)-h(x)|^2)
 +\frac{|h(x)|^2}{N^2}. \tag{6.10}
\]

Thus even free moving backgrounds have a generally nonzero finite-particle cross-bracket bias. Neglecting the excluded root label would miss the second term in (6.10) and (6.9). Equations (6.8)–(6.9) remain harmless under the task's scaling. This is an exact time-dependent-background test; the actual \(K=0\) corrector remains zero.

## 7. Nonzero smooth interaction: a genuine iid diagnostic

Take \(d=1\), \(b=0\), \(g(x)=a\cos(qx)\), \(q=2\pi\), \(a\ne0\). Then \(K(x)=a q\sin(qx)\), and \(\mu_t\equiv1\) is a mean-field solution. Start the actual particles iid uniform. Translation symmetry preserves the uniform first marginal but does not preserve independence.

For the distinct-pair mode \(Q_N=U_2[\cos(q(x-y))]=|Z_1|^2-1/N\), an exact generator computation at time zero gives

\[
 \mathbb E Q_N(0)=0,
 \quad \mathbb E Q_N(0)^2=\frac{N-1}{N^3},
 \quad
 \left.\frac d{dt}\mathbb E Q_N(t)\right|_{t=0}
 =-a q^2\frac{N-1}{N^2}. \tag{7.1}
\]

Indeed, for one fixed ordered pair the mutual drift contributes
\(-2a q^2\sin^2(q(X_i-X_j))/N\), whose iid mean is \(-a q^2/N\). The other-label force terms and the diffusion term integrate to zero at iid uniform preparation. Multiplication by \((N)_2/N^2\) gives (7.1). The correlation bias is created instantly, is of order \(1/N\), and survives exact first-marginal centering. This falsifies an iid-at-positive-time shortcut, while agreeing with the proved smooth bounds.

For the actual terminal test \(\phi(x)=\cos(qx)\), the exact one-body backward solution is

\[
 f_t(x)=e^{-q^2(\nu+a/2)(T-t)}\cos(qx). \tag{7.2}
\]

The response eigenvalue is \(-a q^2/2\); omitting it gives the wrong backward solution. For the terminal source itself,

\[
 J_\phi(x,y)=\frac{a q^2}{2}
 \{\cos(q(x-2y))+\cos(q(2x-y))
 -\cos(qx)-\cos(qy)\}. \tag{7.3}
\]

Its diagonal and its first-slot derivative on the diagonal vanish; its one-background projection is \(-a q^2\cos(qx)/2\). The exact pair observable is

\[
 P_N[J_\phi]=\frac{a q^2}{2}\operatorname{Re}(Z_2\overline Z_1). \tag{7.4}
\]

At iid uniform preparation, direct mode counting or (6.10) gives

\[
 \mathbb E P_N[J_\phi]=0,
 \quad
 \mathbb E P_N[J_\phi]^2=\frac{a^2q^4}{8N^2}, \tag{7.5}
\]

\[
 \mathbb E\frac{d[M_{J_\phi}]}{dt}
 =\frac{\nu a^2q^6(5N-4)}{4N^3},
 \quad
 \mathbb E\frac{d[M_\phi,M_{J_\phi}]}{dt}
 =\frac{\nu a q^4}{2N^2}. \tag{7.6}
\]

These are the exact initial brackets for the fixed source probe \(J_\phi\), not an assertion that \(\Phi=J_\phi\) solves COR-001. They test the nonzero leading kernel of the actual corrector: for each fixed finite \(N,\beta\), its terminal Taylor expansion is \(\Phi_{T-h}=hJ_\phi+o(h)\) in every fixed spatial norm. This follows directly from its smooth final-value equation and \(\Phi_T=0\). The expansion is only a fixed-parameter small-time statement here; it is not used as a uniform high-temperature estimate or as a substitute for Section 3.

The polynomial factors in (7.6), including \(5N-4\), retain both conditional variance and the root-exclusion bias. They are nonzero for \(N=2,3\). Both signs of \(a\) pass: attraction cannot amplify an initial \(N^{-1/2}\) fluctuation to order one on a fixed horizon with a fixed smooth Lipschitz drift. Equation (3.6), with its explicit finite-horizon exponential, is the required proof of that statement, independent of stability of the homogeneous mean-field solution.

## 8. A genuine failure of the tempting law-class extension

This section is deliberately **outside** the iid assertion. It identifies why an equilibrium substitution is invalid even in the same smooth one-mode model.

Take \(a<0\) and the canonical Gibbs law. Its density relative to product Haar measure is proportional to

\[
 \exp\left(\frac{\beta|a|N}{2}|Z_1|^2\right), \tag{8.1}
\]

because the frozen Hamiltonian equals \(a(N|Z_1|^2-1)/2\). Its one-point marginal is exactly uniform by translation invariance. Fix \(\delta>0\). There is an arc of positive Haar length \(p_\delta\) such that, if every particle lies in that arc, \(|Z_1|^2\ge1-\delta/2\). Comparing this subset in the partition function with the event \(|Z_1|^2\le1-\delta\) yields

\[
 \mathbb P_{\rm Gibbs}(|Z_1|^2\le1-\delta)
 \le p_\delta^{-N}\exp(-\beta|a|N\delta/4). \tag{8.2}
\]

For any \(\beta_N\to\infty\), the right side tends to zero. Therefore \(Q_N=|Z_1|^2-1/N\to1\) in probability under these Gibbs laws, despite exact first-marginal centering about the uniform reference. The linear-statistic moment bound (3.7), the pair bound (4.2), and a law-uniform version of them are false in that class. This is a rigorous counterexample to an unqualified iid-to-equilibrium transfer, not a counterexample to PO-001. No equilibrium law is used in Sections 3–5.

## 9. Tests, limitations, and first singular obstruction

The separately written standard-library script `VERIFICATION_CODE/round002_falsification_exact.py` represents Fourier polynomials with exact rational coefficients. Its generator contains the actual nonzero one-mode interaction; bracket products differentiate the particle polynomial directly. It uses no constructor algorithm or floating-point arithmetic.

Executed command:

```text
python3 VERIFICATION_CODE/round002_falsification_exact.py
```

Result: **PASS: 116 exact rational checks**. Particle counts: \(N=2,3,4,6\). Nonuniform background Fourier means: \(1/4,1/8\). Interaction amplitudes: \(-1,1/2\). Diffusivities: \(0,1/3,3\); zero is only an algebraic endpoint diagnostic, not an added hypothesis in the task. Tested: constant finite-particle biases, deleted pair/triple identities including \(N<3\), iid moments, positive pair and signed cross brackets, moving-background biases/brackets, nonzero-interaction correlation creation, and (7.5)–(7.6). Temperature endpoint limits in Section 6 are analytic, not inferred from this finite parameter grid. Computation status: `REPRODUCED` within this context; no independent certificate is claimed.

Also executed `python3 scripts/verify_campaign.py`: PASS, including the frozen source-note SHA-256 `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`. Python version: 3.9.6. No dependency was installed. No random seed or tolerance is applicable to exact rational arithmetic. No TeX source was changed or created by this task.

The first fixed-smooth moment estimate was (3.7); this report supplies a complete proof candidate rather than leaving that estimate as an unverified input. Its proof still needs a fresh hostile review, particularly the conditioning in (3.2), the random-root substitution in (4.7), and the deleted triple formula (2.2). These are explicit review targets, not missing mathematical steps concealed by the finite tests.

The first obstruction to a singular critical transfer is concrete. The constant in (3.6) contains

\[
 \|K\|_\infty T\exp\{T(L_b+2\|DK\|_\infty)\}, \tag{9.1}
\]

and (4.6) additionally uses \(\|K\|_{C^{3d+4}}\) and a uniform corrector norm. These are fixed-smooth constants; this proof establishes no bound for them as a Riesz cutoff is removed. The stated \(A\) is not a singular-uniform input. A joint cutoff choice would still require fluctuation-scale comparison with the unregularized dynamics and corrector, including the initial law and all diagonal/bracket terms. None is proved here.

In particular, the smooth vanishing of the cubic does not classify singular critical diagrams, exclude a surviving pair field, prove a finite critical truncation, or permit arbitrary slow subcritical coupling merely by relabeling the temperature sequence. The singular theorem, critical power counting, and higher-order tail control remain open. The logarithmic normalization is untouched.

Root-only integration actions: compare this independent proof with the constructor; obtain hostile review; then update the affected moment/residual/bracket/law-class ledgers with the actual audit status. No commit, push, publication, contact, or canonical-state mutation was made by this worker.
