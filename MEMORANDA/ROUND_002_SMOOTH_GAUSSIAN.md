# Round 002: a fixed-smooth finite-dimensional Gaussian criterion

Date: 2026-09-17 UTC. Task: TASK-014. Constructor: `/root/r002_falsification`, gpt-6-astra Max. Worktree: `/private/tmp/hocf-round002-falsification-20260917`. Input commit: `a06178658d1e3d458536ff312ca793947212ec67`.

Mathematical status: `PROVED_CANDIDATE`. Audit status: `SELF_CHECKED`; a separate hostile review is required. Source status: self-contained characteristic-function argument, using the frozen smooth identities and the explicitly identified residual proof candidate below. No external martingale central limit theorem is imported. No singular limit, field tightness, or full M3 closure is claimed.

This construction started **after** the independent TASK-011 report was sealed at SHA-256 `125317981b543cf83a47a64efc1455453fbd942e476a52b15e64ec984c216856`. The present worker is the constructor of this Gaussian criterion and cannot independently audit it. The earlier residual report's isolated role does not confer independent status on this new construction. No other Round 002 proof or worktree was read.

## 1. Exact theorem candidate

Fix the dimension, a finite horizon \(T\), a smooth real even interaction \(g\) of zero mean on the unit torus, a smooth confinement \(V\), and a fixed smooth strictly positive probability density \(\mu_0\). Put \(K=-\nabla g\), \(b=-\nabla V\), and use the exact particle diffusion and deterministic mean-field solution from `ROUND_001_MODEL.md`, with arbitrary \(\beta_N>0\). Start the particles iid with law \(\mu_0\). Write \(\eta_t^N=N^{-1}\sum_i\delta_{X_i(t)}\) and \(\rho_t^N=\eta_t^N-\mu_t^N\).

Freeze a finite list \((t_a,\phi_a)_{a=1}^m\), where \(t_a\in[0,T]\) and each \(\phi_a\) is a fixed smooth real test. For each \(a,N\), solve the **full** one-body backward linearized equation on \([0,t_a]\), with terminal value \(\phi_a\), and denote the solution by \(f_a^N\). Let \(\Phi_a^N\) be the zero-terminal COR-001 pair corrector on that same interval.

Assume exactly the uniform spatial bounds of `PO-001_RESIDUAL.md`, with \(r=4d+12\), for \(\mu^N,f_a^N,\Phi_a^N\), uniformly in \(N\), time in their respective domains, and the finite index set \(a\). One may use the maximum of the finitely many assumed constants as \(A\). For \(t_a=0\), the pair corrector is zero and \(f_a^N(0)=\phi_a\).

Set

\[
 \sigma_N=\min(\sqrt{N\beta_N},\sqrt N),\qquad
 a_N=\frac{\sigma_N}{\sqrt N}=\sqrt{\min(\beta_N,1)},
 \qquad
 c_N=\frac{\sigma_N^2}{N\beta_N}=\min(1,\beta_N^{-1}). \tag{1.1}
\]

Define the deterministic real covariance matrices

\[
 I_N^{ab}=a_N^2\operatorname{Cov}_{\mu_0}
              (f_a^N(0),f_b^N(0)), \tag{1.2}
\]

\[
 D_N^{ab}=2c_N\int_0^{t_a\wedge t_b}
   \mu_r^N(\nabla f_a^N(r)\cdot\nabla f_b^N(r))\,dr. \tag{1.3}
\]

**Assertion.** If \(I_N\to I\) and \(D_N\to D\) entrywise, then

\[
 \big(\sigma_N\rho_{t_a}^N(\phi_a)\big)_{a=1}^m
 \ \Longrightarrow\ \mathcal N_m(0,I+D). \tag{1.4}
\]

The matrices \(I,D\) are positive semidefinite, and the Gaussian may be degenerate, including identically zero. More precisely, the initial linearized fluctuation vector and its leading martingale vector converge jointly to independent centered Gaussian vectors with covariances \(I\) and \(D\).

The exact negation is permitted fixed smooth data and a temperature sequence with the stated uniform norms and convergent matrices, but for which (1.4) fails. Sections 2–6 give a complete candidate proof ruling this out. The covariance-convergence hypothesis is not asserted for an arbitrary oscillating temperature sequence.

## 2. Dependencies, constants, and exact remainder

The algebraic inputs are `THM-008_SMOOTH_PAIR.md` and `COR-001_PAIR_CORRECTOR.md`: their full response operators, ordered distinct-label normalization, one-body martingale, pair martingale, and lower drift contractions. These are fixed-smooth inputs; neither an equilibrium theorem nor a singular statement is used.

The analytic input is the sealed `MEMORANDA/ROUND_002_FALSIFICATION.md`, Sections 3–5. Its elementary synchronous coupling proves, for every Fourier character \(e_k\),

\[
 \sup_{t\le T}\|\rho_t^N(e_k)\|_{L^6}
 \le C(1+|k|)N^{-1/2}. \tag{2.1}
\]

Its proof cancels the Brownian paths in the coupling, treats the omitted self-label explicitly, and expands the sixth moment of a bounded centered independent sum. Thus the constant is uniform in every positive \(\beta_N\). It uses the actual interacting law, not a product-law substitution at positive time. The reference may depend on temperature and vary in time.

All constants below depend only on \(m,d,T,A\), \(\|b\|_{C^1}\), and finitely many fixed smooth norms of \(K\), together with the displayed characteristic-function arguments where applicable. They are independent of \(N,\beta_N\). More explicitly, the coupling constant uses \(\|K\|_\infty\), \(\|DK\|_\infty\), \(\|Db\|_\infty\), and an exponential in \(T(\|Db\|_\infty+2\|DK\|_\infty)\); the cubic estimate additionally uses \(\|K\|_{C^{3d+4}}\) and \(\|\Phi_a^N\|_{C^{3d+5}}\). No cutoff-uniformity is implicit in the symbol \(C\).

For each \(a\), add the exact one-body and pair identities and integrate on \([0,t_a]\). Since \(\Phi_a^N(t_a)=0\),

\[
 Z_N^a:=\sigma_N\rho_{t_a}^N(\phi_a)
 =S_N^a+L_N^a+R_N^a, \tag{2.2}
\]

where

\[
 S_N^a=\sigma_N\rho_0^N(f_a^N(0)),
 \quad
 L_N^a=\frac{\sigma_N\sqrt{2/\beta_N}}{N}
   \sum_i\int_0^{t_a}\nabla f_a^N(r,X_i(r))\cdot dW_i(r), \tag{2.3}
\]

and the remainder is **exactly**

\[
 \begin{split}
 R_N^a={}&\sigma_N P_N[\Phi_a^N(0)]
       +\sigma_N M_{\Phi_a^N}(t_a)\\
 &+\sigma_N\int_0^{t_a}
 \left\{U_3[C\Phi_a^N(r)]
  +\frac{\rho_r^N((B\Phi_a^N(r))_{\mu_r^N})}{N}
  +\frac{(\mu_r^N)^{\otimes2}(B\Phi_a^N(r))}{2N}
 \right\}dr. \tag{2.4}
 \end{split}
\]

All signs and the deterministic factor \(1/(2N)\) in the last term are retained. There is no terminal pair endpoint because its terminal kernel is zero. The lower drift is bounded pathwise by \(C/N\): use \(\|\rho\|_{\rm TV}\le2\), probability mass one, and the uniform supremum norm of \(B\Phi\).

The sealed proof supplies the following quantitative bounds, including \(L^2\) rather than just absolute expectation for the first two rows:

\[
 \|P_N[\Phi_a^N(0)]\|_2\le C/N,
 \quad
 \left\|\int_0^{t_a}U_3[C\Phi_a^N(r)]dr\right\|_2
       \le C/N^{3/2}, \tag{2.5}
\]

\[
 \sigma_N^2\mathbb E[M_{\Phi_a^N}]_{t_a}\le C/N.
 \tag{2.6}
\]

Itô isometry applies for each finite \(N,\beta_N\), because the smooth integrands are bounded on the finite horizon. Since \(\sigma_N\le\sqrt N\), (2.4)–(2.6) give

\[
 \max_{a\le m}\|R_N^a\|_2\le C N^{-1/2}. \tag{2.7}
\]

This is a finite-list estimate; it makes no assertion about a supremum over all terminal tests or all times.

### Centering and finite-particle bias

The initial leading vector has mean zero exactly. The pair correction need not: its exact initial iid mean is

\[
 \mathbb E P_N[\Phi_a^N(0)]
 =-\frac{\mu_0^{\otimes2}(\Phi_a^N(0))}{2N}. \tag{2.8}
\]

Take expectations in the unscaled version of (2.2)–(2.4). Both martingales have zero expectation; the initial leading term has zero expectation; (2.5) controls the cubic; and the lower drifts have size \(C/N\). Thus

\[
 |\mathbb E\rho_{t_a}^N(\phi_a)|\le C/N,
 \qquad
 \sigma_N|\mathbb E\rho_{t_a}^N(\phi_a)|\le C/\sqrt N. \tag{2.9}
\]

Consequently the limit in (1.4) is centered under the stated deterministic mean-field centering. No exact-first-marginal recentering or unproved equilibrium centering has been substituted. Large raw high-temperature martingale variances do not enter this expectation calculation; their means remain zero, while their scaled variances are controlled by (2.6).

## 3. Replacement of the leading bracket

For bookkeeping on a common interval, put

\[
 v_a^N(r,x)=\mathbf1_{[0,t_a]}(r)\nabla f_a^N(r,x).
\]

Only the stochastic integrands are extended by zero. The backward PDE and the exact duality identity were applied separately on each terminal interval, so no terminal jump term is omitted by this convention.

Let \(L_N(t)\) be the vector stochastic integral in (2.3), stopped at the respective \(t_a\)'s. Its bracket matrix is

\[
 Q_N^{ab}(t)=[L_N^a,L_N^b]_t
 =2c_N\int_0^t\eta_r^N(v_a^N(r)\cdot v_b^N(r))dr. \tag{3.1}
\]

Let \(D_N(t)\) denote the same deterministic expression with \(\mu_r^N\) instead of \(\eta_r^N\); thus \(D_N(T)=D_N\) from (1.3).

The Fourier estimate (2.1), now only in \(L^1\), yields for every deterministic smooth scalar \(h\)

\[
 \mathbb E|\rho_r^N(h)|\le C N^{-1/2}\|h\|_{C^{d+2}}. \tag{3.2}
\]

Indeed, expand \(h\) in Fourier modes and sum the bound in (2.1); \(d+2>d+1\) makes the coefficient sum weighted by \(1+|k|\) absolutely convergent. The product \(\nabla f_a^N\cdot\nabla f_b^N\) has a uniformly bounded \(C^{d+2}\) norm, since the task bounds \(f_a^N\) in \(C^r\) and \(d+3\le r\).

As \(c_N\le1\), integrating the absolute value gives

\[
 \mathbb E\sup_{t\le T}|Q_N^{ab}(t)-D_N^{ab}(t)|
 \le C N^{-1/2}. \tag{3.3}
\]

This is replacement under the actual evolved law, uniformly in temperature. No signed-mean-to-concentration inference occurs.

For a fixed \(\theta\in\mathbb R^m\), the scalar bracket satisfies the deterministic bound

\[
 0\le Q_N^\theta(t):=\theta^TQ_N(t)\theta
 =2c_N\int_0^t\eta_r^N\left(\left|\sum_a\theta_a v_a^N(r)\right|^2\right)dr
 \le B_\theta, \tag{3.4}
\]

where, for example, \(B_\theta=2TdA^2(\sum_a|\theta_a|)^2\). The same bound holds for \(q_N^\theta:=\theta^TD_N\theta\). Equation (3.3) gives

\[
 \mathbb E|Q_N^\theta(T)-q_N^\theta|\le C_\theta N^{-1/2}. \tag{3.5}
\]

## 4. Direct martingale characteristic function and independence

Let \(\mathcal F_0^N\) contain the iid initial configuration and let the filtration also contain the driving Brownian motions up to time \(t\). Fix \(\theta\), put \(M_N^\theta(t)=\theta\cdot L_N(t)\), and define

\[
 E_N^\theta(t)
 =\exp\left(iM_N^\theta(t)+\frac12Q_N^\theta(t)\right). \tag{4.1}
\]

The sign in front of the bracket is positive: Itô's formula cancels the quadratic term from \(iM_N^\theta\), giving

\[
 dE_N^\theta=iE_N^\theta\,dM_N^\theta,
 \qquad E_N^\theta(0)=1. \tag{4.2}
\]

This is a true complex martingale. Indeed, its modulus is bounded by \(e^{B_\theta/2}\), and the second moment of its stochastic-integral integrand is bounded by

\[
 \mathbb E\int_0^T|E_N^\theta(r)|^2dQ_N^\theta(r)
 \le e^{B_\theta}B_\theta.
\]

Localization followed by the elementary \(L^2\) isometry therefore justifies conditional expectation without invoking any martingale CLT. In particular,

\[
 \mathbb E[E_N^\theta(T)\mid\mathcal F_0^N]=1. \tag{4.3}
\]

For any bounded complex \(\mathcal F_0^N\)-measurable variable \(Y_N\), compare the random bracket with its deterministic value:

\[
 \begin{split}
 &\left|\mathbb E[Y_N e^{i\theta\cdot L_N}]
        -e^{-q_N^\theta/2}\mathbb E Y_N\right|\\
 &\quad=\left|\mathbb E\left[Y_NE_N^\theta(T)
      \{e^{-Q_N^\theta(T)/2}-e^{-q_N^\theta/2}\}\right]\right|\\
 &\quad\le\frac12\|Y_N\|_\infty e^{B_\theta/2}
       \mathbb E|Q_N^\theta(T)-q_N^\theta|
 \le C_\theta\|Y_N\|_\infty N^{-1/2}. \tag{4.4}
 \end{split}
\]

The identity uses (4.3), and the inequality uses the Lipschitz constant \(1/2\) of \(e^{-x/2}\) on \([0,\infty)\). This explicit factorization against every bounded initial-measurable variable is the needed independence mechanism. Finite-particle independence between the leading martingale and the initial state was never assumed and generally is false.

## 5. Initial triangular iid characteristic expansion

Write

\[
 S_N=\frac{a_N}{\sqrt N}\sum_{i=1}^N\xi_{N,i},
 \quad
 \xi_{N,i}^a=f_a^N(0,X_i(0))-\mu_0(f_a^N(0)). \tag{5.1}
\]

For each \(N\), these vectors are iid and centered. They are bounded uniformly in \(N\), and \(a_N\le1\). For a fixed \(\alpha\in\mathbb R^m\), the elementary Taylor inequality for \(e^{ix}\) gives

\[
 \mathbb E\exp\left(i\frac{a_N}{\sqrt N}\alpha\cdot\xi_{N,1}\right)
 =1-\frac{\alpha^TI_N\alpha}{2N}+\varepsilon_N,
 \qquad |\varepsilon_N|\le C_\alpha N^{-3/2}. \tag{5.2}
\]

The covariance \(I_N\) includes the factor \(a_N^2\) exactly. Raise (5.2) to the \(N\)-th power. To avoid any choice of complex logarithm, use the identity for a difference of two \(N\)-th powers: for all sufficiently large \(N\), both the exact one-particle characteristic function and \(1-(\alpha^TI_N\alpha)/(2N)\) have modulus at most one, so their powers differ by at most \(N|\varepsilon_N|\). The latter real power differs from \(\exp(-\alpha^TI_N\alpha/2)\) by \(O_\alpha(N^{-1})\), uniformly because \(I_N\) is bounded. Consequently,

\[
 \mathbb E e^{i\alpha\cdot S_N}
 =e^{-\alpha^TI_N\alpha/2}+O_\alpha(N^{-1/2}). \tag{5.3}
\]

No convergence of the individual backward kernels is required; convergence of the covariance matrices is the sufficient hypothesis.

Now put \(Y_N=e^{i\alpha\cdot S_N}\) in (4.4). Equations (4.4) and (5.3) imply, for every \(\alpha,\theta\in\mathbb R^m\),

\[
 \mathbb E e^{i\alpha\cdot S_N+i\theta\cdot L_N}
 =\exp\left(-\tfrac12\alpha^TI_N\alpha
            -\tfrac12\theta^TD_N\theta\right)
   +O_{\alpha,\theta}(N^{-1/2}). \tag{5.4}
\]

When the prescribed matrices converge, the right-hand side tends to the characteristic function of independent centered Gaussian vectors \(G_I,G_D\) with those covariance matrices. Positive semidefiniteness follows from the covariance/bracket definitions and survives entrywise limits. Singular matrices are allowed by constructing the Gaussians as matrix square roots applied to standard Gaussian vectors.

## 6. Passage to the distribution and the claimed observable

For completeness, the characteristic-function step can be closed without an unstated probabilistic limit theorem. The initial vector has uniformly bounded second moment because \(I_N\) is bounded; the leading martingale does too because \(\mathbb E|L_N|^2=\operatorname{tr}\mathbb E Q_N(T)\) is bounded. Thus \((S_N,L_N)\) has uniformly bounded second moment and is tight by Chebyshev.

Add an independent centered Gaussian vector of covariance \(\varepsilon I_{2m}\). Its integrable characteristic function multiplies (5.4) by \(e^{-\varepsilon|\zeta|^2/2}\). Dominated convergence in Fourier inversion gives uniform convergence of the smoothed densities. On compact sets this gives convergence of their integrals against bounded functions. The uniform second-moment bound, also valid after this smoothing, controls the remaining tails uniformly.

For any bounded Lipschitz test on \(\mathbb R^{2m}\), adding or removing that Gaussian changes the expectation by at most its Lipschitz constant times \(\sqrt{2m\varepsilon}\), uniformly in \(N\). Let \(N\to\infty\) first, then \(\varepsilon\downarrow0\). This proves the joint convergence specified after (1.4), including degeneracy. Convergence against bounded Lipschitz tests is the usual weak convergence criterion in finite-dimensional Euclidean space.

Finally, (2.7) implies \(\mathbb E|R_N|\to0\). Replacing \(S_N+L_N\) by \(Z_N\) changes the expectation of a bounded Lipschitz test by at most its Lipschitz constant times \(\mathbb E|R_N|\). The sum of the independent Gaussian limits has covariance \(I+D\), proving (1.4).

As a check on normalization, the exact finite-particle cross covariance of \(S_N\) and \(L_N\) is zero, because \(\mathbb E[L_N\mid\mathcal F_0^N]=0\). This fact alone would not prove independence; the stronger factorization (4.4) is what supplies it. Equations (2.7) and (3.3) also show that the covariance matrix of \(Z_N\) differs from \(I_N+D_N\) by \(O(N^{-1/2})\), with constants for this finite list. The mean converges to zero at the rate in (2.9).

## 7. Exact free heat tests and temperature endpoints

Set \(K=b=0\). The actual pair corrector is zero. For a Fourier character \(e_k(x)=e^{2\pi i k\cdot x}\), put \(\lambda_k=4\pi^2|k|^2\). The actual backward one-body solution with terminal time \(t_a\) is

\[
 f_a^N(r,x)=e^{-\lambda_k(t_a-r)/\beta_N}e_k(x),
 \qquad 0\le r\le t_a. \tag{7.1}
\]

Complex characters are merely a convenient basis: take real and imaginary parts to obtain real covariance matrices in the theorem.

### Homogeneous background

For \(\mu_0=1\) and nonzero modes, the bilinear covariance vanishes unless the modes are opposite. For terminals \((t,e_k)\) and \((s,e_{-k})\), writing \(b_N=\min(\beta_N,1)\), the two deterministic contributions are exactly

\[
 I_N=b_N e^{-\lambda_k(t+s)/\beta_N}, \tag{7.2}
\]

\[
 D_N=b_N\left\{e^{-\lambda_k|t-s|/\beta_N}
                    -e^{-\lambda_k(t+s)/\beta_N}\right\}, \tag{7.3}
\]

and hence

\[
 I_N+D_N=b_N e^{-\lambda_k|t-s|/\beta_N}. \tag{7.4}
\]

To verify (7.3), insert (7.1) into (1.3), use \(\nabla e_k\cdot\nabla e_{-k}=\lambda_k\), integrate to \(t\wedge s\), and use \(\beta_Nc_N=b_N\). An independent finite-particle check gives the same answer: different particles have zero covariance, while one stationary Brownian particle satisfies
\(\mathbb E[e_k(X_t)e_{-k}(X_s)]=e^{-\lambda_k|t-s|/\beta_N}\). Multiplication by \(\sigma_N^2/N=b_N\) proves (7.4) for every finite \(N\), not just asymptotically.

For real cosine tests the right sides of (7.2)–(7.4) have an additional factor \(1/2\). The corresponding sine tests have the same covariance, while sine/cosine cross terms are zero under Haar measure.

- **Time zero:** if one terminal time is zero, the overlap interval in (1.3) is empty and \(D_N=0\); (7.2) already equals the total covariance.
- **Equal times:** if \(t=s>0\), the total mode covariance is \(b_N\). Its initial contribution is \(b_Ne^{-2\lambda_kt/\beta_N}\), and its martingale contribution is \(b_N(1-e^{-2\lambda_kt/\beta_N})\).
- **Different times:** the total covariance is the decay in (7.4), with the overlap ending at the smaller terminal time, exactly as in (1.3).
- **\(\beta_N\to\beta_*\in(0,\infty)\):** (7.4) tends to \(\min(\beta_*,1)e^{-\lambda_k|t-s|/\beta_*}\).
- **\(\beta_N\to\infty\):** (7.2) tends to one and (7.3) tends to zero. The limiting mode fluctuation is the same initial Gaussian at every frozen time; the noise disappears.
- **\(\beta_N\to0\):** both contributions tend to zero, even at equal times, since they lie between zero and \(b_N=\beta_N\). The Gaussian limit at this normalization is degenerate. A high-temperature nondegenerate thermal limit must not be presumed in this free iid model.

These are physical-temperature/diffusivity statements. No Riesz exponent or microscopic singular scaling appears in the fixed-smooth model.

### Moving free background

The same check can be made with an arbitrary smooth positive \(\mu_0\), in which case the reference evolves by heat flow. For \(t\ge s\), the exact finite-particle bilinear covariance of terminal modes is

\[
 \begin{split}
 &\operatorname{Cov}\big(\sigma_N\rho_t^N(e_k),
                         \sigma_N\rho_s^N(e_\ell)\big)\\
 &\quad=b_N\left\{
 e^{-\lambda_k(t-s)/\beta_N}
 e^{-\lambda_{k+\ell}s/\beta_N}\mu_0(e_{k+\ell})
 -e^{-\lambda_kt/\beta_N-\lambda_\ell s/\beta_N}
       \mu_0(e_k)\mu_0(e_\ell)
 \right\}. \tag{7.5}
 \end{split}
\]

Condition on the one Brownian particle at time \(s\) to obtain the first term; subtract its two means for the second; independence across labels supplies the factor \(b_N\). Substitution in (1.2)–(1.3) gives the same expression, using
\(\lambda_k+\lambda_\ell-\lambda_{k+\ell}=-8\pi^2 k\cdot\ell\). This includes zero or orthogonal modes by continuity, without division by a vanishing frequency difference. It verifies the time-dependent background centering in the covariance criterion as well as the homogeneous special case.

### Why the covariance hypothesis cannot be discarded

Take the free homogeneous model, one cosine test at time zero, and let \(\beta_N\) alternate between \(1/2\) and \(2\). The uniform norms in the task hold, but the initial covariance alternates between \(1/4\) and \(1/2\), with zero martingale contribution. The elementary iid expansion in Section 5 gives these two different subsequential Gaussian limits. Thus an unconditional convergence assertion for arbitrary oscillating temperatures is false even in the free model. This example does not contradict the theorem candidate because its covariance matrices do not converge.

## 8. General temperature endpoints under the frozen bounds

The free heat endpoint checks above extend in a precise way to the full fixed-smooth model. For one terminal interval, suppress the indices and write

\[
 Rf(y)=\int K(x-y)\cdot\nabla f(x)\,\mu(dx),
 \qquad A f=(b+K*\mu)\cdot\nabla f+\nu\Delta f.
\]

The mean-field equation and the full backward equation give the exact energy identity

\[
 \frac d{dt}\mu_t(f_t^2)
 =2\nu\mu_t(|\nabla f_t|^2)-2\mu_t(f_t Rf_t). \tag{8.1}
\]

Indeed, differentiate both the test and the reference measure, use
\(A(f^2)=2fAf+2\nu|\nabla f|^2\), and substitute
\(\partial_t f+Af=-Rf\). The drift and all background time dependence have thereby been included. On the finite torus all integrations by parts are justified by the assumed smoothness.

Let \(B=\|K\|_\infty\) in the Euclidean vector norm. The frozen bounds imply
\(\|Rf\|_\infty\le B\sqrt d A\). Integrating (8.1) up to the terminal time and retaining the sign of the initial square yields

\[
 \begin{split}
 2\beta_N^{-1}\int_0^{t_a}\mu_r^N(|\nabla f_a^N(r)|^2)dr
 &=\mu_{t_a}^N(\phi_a^2)-\mu_0((f_a^N(0))^2)
     +2\int_0^{t_a}\mu_r^N(f_a^N Rf_a^N)dr\\
 &\le A^2+2T\sqrt d B A^2.
 \end{split} \tag{8.2}
\]

Consequently,

\[
 \int_0^{t_a}\mu_r^N(|\nabla f_a^N(r)|^2)dr\le C\beta_N.
 \tag{8.3}
\]

This estimate does not assume a uniform bound on time derivatives and does not discard the full response operator. Its constant is uniform in the temperature sequence under precisely the given spatial bounds.

If \(\beta_N\to0\), then eventually \(a_N^2=\beta_N\) and \(c_N=1\). The initial covariance entries have size \(O(\beta_N)\) by the uniform bound on the initial tests. The diagonal entries of \(D_N\) have the same size by (8.3), and its off-diagonal entries do too by Cauchy–Schwarz on the common time/space integral. Therefore

\[
 I_N\longrightarrow0,\qquad D_N\longrightarrow0,
 \qquad Z_N\Longrightarrow0. \tag{8.4}
\]

Thus covariance convergence is automatic at this endpoint, and the limit is degenerate. As an independent consistency check, (2.1) and absolute Fourier summation applied directly to the fixed terminal tests give \(\|Z_N^a\|_2\le C\sqrt{\beta_N}\) whenever \(\beta_N\le1\), so here convergence to zero actually holds in \(L^2\).

If \(\beta_N\to\infty\), then \(c_N=\beta_N^{-1}\) eventually. The elementary bound \(\int_0^{t_a}\mu|\nabla f_a^N|^2\le TdA^2\) gives \(D_N=O(\beta_N^{-1})\) entrywise, and even the actual martingale has \(\mathbb E|L_N|^2=O(\beta_N^{-1})\). Hence the leading dynamical noise vanishes in \(L^2\). The initial covariance is now \(I_N^{ab}=\operatorname{Cov}_{\mu_0}(f_a^N(0),f_b^N(0))\); the criterion requires its convergence. For example, uniform convergence of each \(f_a^N(0)\) to a specified limiting backward kernel would identify \(I\) as that kernel covariance. Such kernel convergence or a general zero-diffusivity PDE limit is not proved here. Conditional on \(I_N\to I\), the limit is the centered Gaussian with covariance \(I\) alone.

These endpoint conclusions concern fixed smooth kernels and the stated uniform bounds. They do not rename or settle either singular microscopic coupling regime.

## 9. Verification, limits, and integration boundary

The load-bearing proof does not cite a martingale CLT, a propagation-of-chaos theorem, a Gaussian approximation theorem, or any equilibrium result. Its inputs are the named exact R1 identities and the worker's sealed elementary residual proof. The characteristic-function expansion, the bounded exponential martingale, the actual-law bracket replacement, the smoothing passage, and the backward energy identity for the general high-temperature endpoint are displayed in full.

The free heat identities (7.2)–(7.5) were checked by two exact calculations: the initial-plus-bracket decomposition and direct single-particle covariance. Their validity includes zero, equal, and unequal terminal times. The temperature endpoint conclusions are analytic limits of the exact formulas, not numerical extrapolations. No new computation code is needed for these finite formulas. The separate residual script still passes all 116 exact rational checks, but those tests are not a proof or independent audit of the present Gaussian criterion.

Executed verification commands are `python3 scripts/verify_campaign.py`, `python3 VERIFICATION_CODE/round002_falsification_exact.py`, and `git diff --check`. Outcomes are recorded with the final hash handoff. No installation, commit, push, source modification, or canonical-ledger edit was made. No TeX artifact was changed or created in this task.

Remaining review targets are precise: the sign in (4.1), true-martingale justification and conditional identity (4.3), the root-dependent actual-law bracket replacement (3.2)–(3.3), the uniform triangular expansion (5.2), the full corrected remainder (2.4), and the covariance decomposition for unequal terminal times. The present constructor supplies only `SELF_CHECKED` status for them.

The theorem is a conditional finite-dimensional covariance-limit criterion for fixed smooth kernels. It proves neither field/path tightness nor uniformity over growing lists of tests/times. It does not establish the required uniform norms or covariance convergence for a singular kernel family. The constants inherit the explicit smooth derivative dependence of the residual proof. It gives no singular cutoff passage, critical power-counting decision, or finite/infinite corrector truncation theorem. Other initial law classes require their own argument. The logarithmic normalization is untouched.

This result can discharge a specifically named smooth finite-dimensional subclaim after hostile review. The full frozen scope of M3 and the singular campaign mission remain open; the theorem must not be promoted as their completion. Root alone assigns any new canonical theorem identifier and integrates the result into the state ledgers.
