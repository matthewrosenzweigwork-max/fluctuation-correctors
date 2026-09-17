# Round 002: statement-only reconstruction of the finite-list Gaussian criterion

Date: 2026-09-17 UTC. Task: TASK-019.
Worktree: `/private/tmp/hocf-round002-gaussian-blind-20260917`.
Starting commit: `a06178658d1e3d458536ff312ca793947212ec67`.

Reconstruction outcome: the frozen statement is proved below.
Mathematical status: `PROVED_CANDIDATE` for this reconstruction;
same-context checks only. The Gaussian constructor's proof has not been
seen or reviewed, and no PASS is assigned to it. This report is sealed before
any comparison with that proof.

Isolation disclosure: this agent previously constructed the permitted
fixed-smooth residual and all-order moment arguments. The context is reused;
independence is from the new Gaussian argument, not from those prerequisites.
No other Round 002 worktree, Gaussian report, Gaussian theorem card, hostile
Gaussian report, or root TeX was read in this reconstruction. The only new
Gaussian input was the statement in TASK-019. The earlier own-report hashes,
already sealed before this task, are recorded in Section 10. The relevant
second-moment coupling calculation is included here so the limiting argument
is human-checkable without a martingale central limit theorem import.

## 1. Exact statement and definitions

Fix the permitted smooth periodic model, its fixed horizon \(T\), iid initial
law \(\mu_0\), and independent driving Brownian motions independent of the
initial samples. Write \(K=-\nabla g\), \(b=-\nabla V\),
\(\nu_N=\beta_N^{-1}\),
\(\eta_t^N=N^{-1}\sum_i\delta_{x_i(t)}\), and
\(\rho_t^N=\eta_t^N-\mu_t^N\), where \(\mu^N\) is the model's deterministic
mean-field solution. The interaction is fixed and smooth throughout this
report; no cutoff limit is taken.

Let there be \(m\) real terminal tests \(\varphi_a\), at times
\(t_a\in[0,T]\), and let \(f_a^N\) solve the full backward linearized test
equation on \([0,t_a]\), with terminal value \(\varphi_a\). The statement
also supplies the associated zero-terminal pair correctors and its uniform
\(C^{4d+12}\) bounds. Let \(A\) be a common such bound for the finite family,
enlarged if necessary so that all these individual norms are at most \(A\).

Put

\[
 \sigma_N=\min(\sqrt{N\beta_N},\sqrt N),\qquad
 a_N=\frac{\sigma_N}{\sqrt N}=\min(\sqrt{\beta_N},1),\qquad
 c_N=\frac{\sigma_N^2}{N\beta_N}=\min(1,\beta_N^{-1}).
 \tag{1.1}
\]

Define the scaled initial and leading martingale vectors by

\[
\begin{aligned}
 Z_N^a&=\sigma_N\langle f_a^N(0),\rho_0^N\rangle,\\
 M_N^a(t)&=\frac{\sigma_N\sqrt{2\nu_N}}N
       \sum_i\int_0^{\min(t,t_a)}
                  \nabla f_a^N(r,x_i(r))\cdot dW_i(r),\qquad
 M_N^a=M_N^a(T),\\
 X_N^a&=\sigma_N\langle\varphi_a,\rho_{t_a}^N\rangle.
\end{aligned}
\tag{1.2}
\]

The deterministic covariance arrays in the statement are exactly

\[
\begin{aligned}
 I_N^{ab}&=a_N^2\operatorname{Cov}_{\mu_0}
                         (f_a^N(0),f_b^N(0)),\\
 D_N^{ab}&=2c_N\int_0^{\min(t_a,t_b)}
       \left\langle\nabla f_a^N(r)\cdot\nabla f_b^N(r),\mu_r^N\right\rangle dr.
\end{aligned}
\tag{1.3}
\]

Assume entrywise limits \(I_N\to I\) and \(D_N\to D\). We prove

\[
 (Z_N,M_N)\ \Longrightarrow\ (G_I,G_D),\qquad
 G_I\ \hbox{and}\ G_D\ \hbox{independent},\qquad
 X_N\ \Longrightarrow\ G_I+G_D,
 \tag{1.4}
\]

where the two centered Gaussian vectors have covariances \(I,D\), allowing
singular or zero covariance matrices. Consequently the covariance in the
last limit is \(I+D\). Its logical negation is an admissible sequence with
the stipulated covariance limits and failure of at least one conclusion.

Neither \(a_N\), \(c_N\), nor \(\beta_N\) is required to converge separately.
Only the matrices in (1.3) must converge. Their limits are positive
semidefinite, because each \(I_N\) is a covariance matrix and each \(D_N\)
is the integral of a Gram matrix with nonnegative multiplier.

## 2. The actual-law empirical estimate used below

Choose \(q=\lfloor d/2\rfloor+2\), and define

\[
\begin{gathered}
 Q=(d+1)^{q/2},\quad w_k=1+4\pi^2|k|^2,\quad
 B^2=\sum_kw_k^{-q},\quad
 D_*^2=\sum_k4\pi^2|k|^2w_k^{-q},\\
 \|\zeta\|_{-q}^2=\sum_kw_k^{-q}|\widehat\zeta(k)|^2,\quad
 \kappa_j=\|K\|_{C^j},\quad v_1=\|b\|_{C^1},\\
 L=d(v_1+2\kappa_1),\qquad
 \mathcal K=\left(\sum_{j=1}^d\|K_j\|_{H^q}^2\right)^{1/2}
                  \le\sqrt d\,Q\kappa_q,\\
 h_L(T)=\begin{cases}(e^{LT}-1)/L,&L>0,\\T,&L=0,\end{cases}
 \qquad R=B(1+D_*\mathcal K h_L(T)).
\end{gathered}
\tag{2.1}
\]

The norm convention is the componentwise maximum of derivatives of total
order at most the indicated integer. All sums converge since \(q>d/2+1\).
The following two consequences hold for the actual interacting law:

\[
 \sup_{r\le T}\mathbb E\|\rho_r^N\|_{-q}^2\le R^2/N,
 \qquad
 \sup_{r\le T}\mathbb E\|\rho_r^N\|_{-q}\le R/\sqrt N.
 \tag{2.2}
\]

Their constants are independent of \(\nu_N\), \(N\), and all background
derivatives. To recall their complete short proof, couple the particles to
independent nonlinear diffusions \(y_i\), with deterministic drift
\(b+K*\mu_r^N\), the same initial samples, and the same Brownian motions.
Their law is \(\mu_r^N\), by the linear Fokker--Planck equation with this
given deterministic drift; equality follows by testing against its smooth
backward expectations. Smooth bounded coefficients give the global
additive-noise flows by Picard iteration. These facts do not assert that the
interacting particles have product law.

Let \(\overline\rho_r=N^{-1}\sum_i\delta_{y_i(r)}-\mu_r^N\). Independence
in the real Hilbert space of the Fourier norm gives directly

\[
 \mathbb E\|\overline\rho_r\|_{-q}^2
     =\frac{B^2-\|\mu_r^N\|_{-q}^2}{N}\le B^2/N.
 \tag{2.3}
\]

Use common lifts for each pair of coupled positions at time zero. Noise
cancels in their lifted displacement. Since \(K(0)=0\), the force with the
deleted self label is exactly the full empirical force. For
\(D_N(r)=N^{-1}\sum_i|x_i(r)-y_i(r)|\), the Lipschitz bounds and Fourier
duality therefore yield

\[
 D_N(r)\le\mathcal K\int_0^r e^{L(r-s)}
                               \|\overline\rho_s\|_{-q}ds,
 \quad
 \|\rho_r^N\|_{-q}\le\|\overline\rho_r\|_{-q}+D_*D_N(r).
 \tag{2.4}
\]

Here \(\|\delta_x-\delta_y\|_{-q}\le D_*|x-y|\) follows term by term from
the Fourier characters. Applying Minkowski and (2.3) proves (2.2). The
supremum is outside the expectation; no uniform-in-diffusivity supremum over
the random time path is asserted or needed.

For future use, expansion of \((1+4\pi^2|k|^2)^q\) and Parseval give

\[
\begin{aligned}
 |\langle h,\rho\rangle|&\le Q\|h\|_{C^q}\|\rho\|_{-q},\\
 |\langle H,\rho^{\otimes2}\rangle|
       &\le Q^2\|H\|_{C^{2q}}\|\rho\|_{-q}^2.
\end{aligned}
\tag{2.5}
\]

For the second line apply Cauchy--Schwarz with the product Fourier weight
\(w_k^q w_\ell^q\); its derivative coefficient sum is \((d+1)^{2q}\).
Thus every norm order used in the limiting steps is explicit.

## 3. Linearized reduction and mean-field bias

The permitted one-body identity, also obtainable by direct Itô expansion,
is

\[
 \langle\varphi_a,\rho_{t_a}^N\rangle
 =\langle f_a^N(0),\rho_0^N\rangle
   +\frac{\sqrt{2\nu_N}}N\sum_i\int_0^{t_a}
                         \nabla f_a^N(r,x_i(r))\cdot dW_i(r)
   +\int_0^{t_a}P_N[H_{a,r}^N]dr,
 \tag{3.1}
\]

where
\(H_{a,r}^N(x,y)=K(x-y)\cdot(\nabla f_a^N(r,x)-\nabla f_a^N(r,y))\).
To verify the full linearization, write the particle drift as
\(b+K*\mu+K*\rho\), split the force pairing's first empirical slot into
\(\mu+\rho\), and place the term with \(\mu\) in the response operator
\(Af(y)=\int K(x-y)\cdot\nabla f(x)\,d\mu(x)\).
The remaining product symmetrizes by oddness of \(K\) into
\(\tfrac12\rho^{\otimes2}(H_{a,r}^N)\). This is exactly the full backward
operator specified in the task, not independent transport alone.

There is no diagonal error in this particular source: \(H_{a,r}^N(x,x)=0\).
The exact convention conversion therefore gives

\[
 P_N[H_{a,r}^N]=\tfrac12\langle H_{a,r}^N,(\rho_r^N)^{\otimes2}\rangle.
 \tag{3.2}
\]

Leibniz expansion and the frozen bound yield

\[
 \sup_{N,a,r}\|H_{a,r}^N\|_{C^{2q}}
       \le d 2^{2q+1}\kappa_{2q}A.
 \tag{3.3}
\]

Only \(2q+1\) derivatives of the one-body test enter, and
\(2q+1\le4d+12\). Define the finite, temperature-independent constant

\[
 C_{\mathrm{quad}}=d 2^{2q}Q^2\kappa_{2q}A R^2.
 \tag{3.4}
\]

Equations (2.2), (2.5), and (3.2) imply the actual-law absolute estimate

\[
 \mathbb E|P_N[H_{a,r}^N]|\le C_{\mathrm{quad}}/N.
 \tag{3.5}
\]

Consequently, with \(E_N^a=X_N^a-Z_N^a-M_N^a\),

\[
 \mathbb E|E_N^a|\le T C_{\mathrm{quad}}\frac{a_N}{\sqrt N}
                    \le T C_{\mathrm{quad}}N^{-1/2}.
 \tag{3.6}
\]

This is a particularly short fixed-smooth reduction made available by the
permitted empirical moment prerequisite. The pair-corrector residual theorem
would give the same vanishing conclusion, but its use is unnecessary here.
The supplied pair-corrector bounds remain valid assumptions of the frozen
statement; no modification of that statement or singular extension is made.

Both the initial linear term and the Brownian integral in (3.1) have exactly
zero expectation. In particular the latter is square integrable for each
fixed \(N,\nu_N\). Thus the mean-field bias itself obeys

\[
 \left|\mathbb E\langle\varphi_a,\eta_{t_a}^N\rangle
                -\langle\varphi_a,\mu_{t_a}^N\rangle\right|
       \le T C_{\mathrm{quad}}/N.
 \tag{3.7}
\]

It is negligible after multiplication by \(\sigma_N\). This proves the
centering conclusion in mean-field normalization; no substitution of the
exact first marginal is hidden in the argument.

## 4. The triangular iid initial vector

Fix \(u\in\mathbb R^m\). If \(Y\) has law \(\mu_0\), put

\[
 \xi_N(Y)=a_N\sum_a u_a
       (f_a^N(0,Y)-\langle f_a^N(0),\mu_0\rangle).
\]

Then \(\mathbb E\xi_N=0\), \(|\xi_N|\le2A\|u\|_1\), and
\(\mathbb E\xi_N^2=u^TI_Nu\). Independence of the initial samples gives

\[
 \mathbb E e^{i u\cdot Z_N}
     =\left(\mathbb E e^{i\xi_N(Y)/\sqrt N}\right)^N.
 \tag{4.1}
\]

The scalar Taylor formula with integral remainder gives

\[
 \mathbb E e^{i\xi_N/\sqrt N}
  =1-\frac{u^TI_Nu}{2N}+r_N,
 \qquad |r_N|\le\frac{(2A\|u\|_1)^3}{6N^{3/2}}.
 \tag{4.2}
\]

The deviation from one is \(O_u(N^{-1})\). For large \(N\), the convergent
logarithm series on the disk of radius \(1/2\) gives
\(|\log(1+z)-z|\le2|z|^2\). Hence

\[
 \mathbb E e^{i u\cdot Z_N}
 =\exp\{-\tfrac12u^TI_Nu+O_u(N^{-1/2})\}
 \longrightarrow e^{-u^TIu/2}.
 \tag{4.3}
\]

This proves the triangular-array characteristic-function calculation
directly. It requires neither convergence of the functions \(f_a^N(0)\) nor
positivity of the limiting covariance.

## 5. Leading brackets under the interacting law

Extend the spatial gradients as zero beyond their respective terminal times,

\[
 G_{N,a}(r,x)=\mathbf1_{\{r\le t_a\}}\nabla f_a^N(r,x).
\]

The values at deterministic terminal instants do not affect the stochastic
integrals. These piecewise continuous deterministic-time integrands are
predictable. Independence of particle Brownian noises gives the exact
covariation

\[
 [M_N^a,M_N^b]_T
   =2c_N\int_0^{\min(t_a,t_b)}
       \langle\nabla f_a^N(r)\cdot\nabla f_b^N(r),\eta_r^N\rangle dr.
 \tag{5.1}
\]

The deterministic counterpart is exactly \(D_N^{ab}\), not a covariance
computed under an assumed iid evolved law. The test product has norm

\[
 \|\nabla f_a^N\cdot\nabla f_b^N\|_{C^q}
                         \le d 2^q A^2.
 \tag{5.2}
\]

Since \(c_N\le1\), (2.2) and (2.5) prove

\[
 \mathbb E|[M_N^a,M_N^b]_T-D_N^{ab}|
       \le\frac{2TQd 2^qA^2R}{\sqrt N}.
 \tag{5.3}
\]

For a scalar projection \(v\in\mathbb R^m\), let
\(m_N(t)=\sum_av_aM_N^a(t)\),
\(q_N(t)=[m_N]_t\), and \(d_N=v^TD_Nv\). Set

\[
 H_v=2TdA^2\|v\|_1^2,\qquad
 B_v=2TQd 2^qA^2R\|v\|_1^2.
 \tag{5.4}
\]

Both the pathwise bracket and its deterministic counterpart are nonnegative
and bounded, uniformly in all parameters, as follows:

\[
 0\le q_N(T),d_N\le H_v,\qquad
 \mathbb E|q_N(T)-d_N|\le B_vN^{-1/2}.
 \tag{5.5}
\]

Indeed both are integrals of
\(|\sum_av_aG_{N,a}|^2\) against a probability measure, with coefficient
\(2c_N\). This uniformly bounded bracket, rather than a bound containing an
uncontrolled \(1/\nu_N\), is the key to the next step.

## 6. Conditional characteristic functions and independence

Let \(\mathcal F_0\) be the initial sigma field, which contains \(Z_N\).
For the scalar continuous martingale in Section 5 define

\[
 \mathcal E_N(t)=\exp\{i m_N(t)+\tfrac12q_N(t)\}.
 \tag{6.1}
\]

Itô's formula cancels its finite variation terms and gives
\(d\mathcal E_N=i\mathcal E_Ndm_N\), with initial value one.
This is a true complex-valued martingale, not merely a formal exponential:
\(|\mathcal E_N(t)|^2=e^{q_N(t)}\le e^{H_v}\), and
\(\mathbb E\int_0^T|\mathcal E_N|^2dq_N\le e^{H_v}H_v<\infty\).
The real and imaginary stochastic integrals are consequently square
integrable, and

\[
 \mathbb E[\mathcal E_N(T)\mid\mathcal F_0]=1.
 \tag{6.2}
\]

For **any** bounded, possibly \(N\)-dependent, complex
\(\mathcal F_0\)-measurable variable \(Y_N\), use
\(e^{im_N(T)}=\mathcal E_N(T)e^{-q_N(T)/2}\) and (6.2). The function
\(x\mapsto e^{-x/2}\) has Lipschitz constant \(1/2\) on \([0,\infty)\).
Therefore

\[
\begin{aligned}
 &\left|\mathbb E[Y_Ne^{im_N(T)}]
                   -e^{-d_N/2}\mathbb E Y_N\right|\\
 &\quad=\left|\mathbb E\left[
     Y_N\mathcal E_N(T)(e^{-q_N(T)/2}-e^{-d_N/2})\right]\right|\\
 &\quad\le\tfrac12\|Y_N\|_\infty e^{H_v/2}
                         \mathbb E|q_N(T)-d_N|
 \le\tfrac12\|Y_N\|_\infty e^{H_v/2}B_vN^{-1/2}.
\end{aligned}
\tag{6.3}
\]

This is the decisive dependence estimate. It applies to
\(Y_N=e^{iu\cdot Z_N}\), which has absolute value one, even though the
martingale integrands depend on all the initial positions through the
interacting dynamics. Combining (4.3) and (6.3) gives

\[
 \mathbb E e^{i u\cdot Z_N+i v\cdot M_N}
    \longrightarrow
      \exp\{-\tfrac12u^TIu-\tfrac12v^TDv\}.
 \tag{6.4}
\]

The right-hand side is the characteristic function of independent Gaussian
vectors of covariances \(I,D\). No martingale central limit theorem, stable
convergence theorem, conditional Gaussianity assertion, or asymptotic
independence assumption was imported. Although
\(\mathbb E[Z_N^aM_N^b]=0\) already holds exactly, that identity alone would
not have proved independence; (6.3) does.

## 7. From the characteristic functions to the asserted distributional limit

Here are the needed finite-dimensional details, so the argument does not
leave its final convergence theorem unqualified. Positive semidefinite
\(I,D\) admit real symmetric square roots by diagonalization. On a product
probability space let \(G_I=I^{1/2}G\) and \(G_D=D^{1/2}G'\), where \(G,G'\)
are independent standard normal vectors. Elementary Gaussian integration
gives the characteristic function in (6.4), including zero eigenvalues.

The vectors \((Z_N,M_N)\) have uniformly bounded second moments:

\[
 \mathbb E|Z_N|^2=\operatorname{tr}I_N\le mA^2,
 \qquad
 \mathbb E|M_N|^2=\sum_a\mathbb E[M_N^a]_T\le2mTdA^2.
 \tag{7.1}
\]

Thus their tails are uniformly bounded by a constant times the inverse
square of the radius. The following elementary smoothing argument applies
to any sequence \(Y_N\) with this second-moment bound and the pointwise
characteristic-function limit of a finite-second-moment random vector \(Y\).
Add an independent standard Gaussian vector \(G_0\), multiplied by
\(\epsilon>0\). By the explicit Fourier formula for the Gaussian density
and Fubini, the density of \(Y_N+\epsilon G_0\) is

\[
 p_{N,\epsilon}(x)=(2\pi)^{-r}\int_{\mathbb R^r}
       e^{-it\cdot x}\,\mathbb E e^{it\cdot Y_N}
                         e^{-\epsilon^2|t|^2/2}\,dt,
 \tag{7.2}
\]

where \(r\) is the vector dimension. The integrable Gaussian factor permits
dominated convergence, giving uniform convergence of these densities to
the density of \(Y+\epsilon G_0\). On a fixed ball this implies convergence
of integrals against bounded functions; the second-moment tail bounds make
the integrals outside a sufficiently large ball uniformly small. Hence for
every bounded Lipschitz \(h\),

\[
 \mathbb E h(Y_N+\epsilon G_0)\longrightarrow
                          \mathbb E h(Y+\epsilon G_0).
\]

The difference from the unsmoothed expectation is at most
\(\operatorname{Lip}(h)\epsilon\mathbb E|G_0|\), uniformly in \(N\).
Letting \(\epsilon\downarrow0\) proves convergence for all bounded Lipschitz
tests. For a bounded continuous test, first approximate it uniformly on a
large compact ball by a Lipschitz function (for example by piecewise affine
interpolation on a sufficiently fine finite grid and a bounded extension),
then use the same tail bounds. This proves weak convergence as claimed.

Apply this argument with \(Y_N=(Z_N,M_N)\), \(Y=(G_I,G_D)\), using (6.4)
and (7.1). This proves the first two conclusions of (1.4). For a bounded
Lipschitz function \(h\) on \(\mathbb R^m\), (3.6) gives

\[
 |\mathbb Eh(X_N)-\mathbb Eh(Z_N+M_N)|
        \le\operatorname{Lip}(h)\sum_a\mathbb E|E_N^a|
        \longrightarrow0.
 \tag{7.3}
\]

The joint limit just established implies convergence of the sum; (7.3) and
the same compact approximation establish the last conclusion of (1.4).
For that approximation the sums are uniformly tight by (7.1), and the
remainders tend to zero in \(L^1\); Markov's inequality therefore makes
\(X_N\) tight as well. No second-moment claim about the remainder is needed.
In particular no positive lower covariance bound or inversion of \(I+D\)
was needed. The limiting Gaussian is centered, and (3.7) separately verifies
the required mean-field centering at the fluctuation scale.

## 8. Required edge and solvable-model tests

### Unequal terminal times

The use of stopped components in (1.2) gives the overlap interval
\([0,\min(t_a,t_b)]\) in (5.1) directly from Brownian covariance. In a
projection involving several times, the integrand is the single predictable
vector \(\sum_av_aG_{N,a}\); its bracket is nonnegative even when individual
cross entries have either sign. The conditional exponential argument requires
only this common-time scalar martingale, so no joint convergence over a time
path or unproved multi-time martingale theorem is hidden in the proof.

### Zero time and degeneracy

If \(t_a=0\), then \(f_a^N(0)=\varphi_a\), \(M_N^a=0\), and \(E_N^a=0\)
exactly. The associated row and column of \(D_N\) vanish, whereas its initial
covariance with positive-time components is still the one in (1.3).
If a terminal test is constant, its backward solution is the same constant,
and every centered initial, martingale, and terminal component is exactly
zero. Repeated tests or a limiting covariance of deficient rank cause no
problem because (4.2), (6.3), and the Gaussian-smoothing argument do not divide
by any variance. A zero Gaussian vector is independent of the other vector
in the ordinary distributional sense.

### Free heat Fourier calculation

Take \(K=b=0\), \(\mu_0=1\), and one nonconstant mode
\(\varphi(x)=\cos(2\pi k\cdot x)\), \(k\ne0\). Put
\(\omega=4\pi^2|k|^2\). For this same terminal test at any times \(t_a,t_b\),

\[
 f_a^N(r,x)=e^{-\nu_N\omega(t_a-r)}\varphi(x),\qquad
 \int\varphi^2=\tfrac12,\qquad
 \int|\nabla\varphi|^2=\tfrac\omega2.
 \tag{8.1}
\]

The initial and dynamic covariance entries are therefore exactly

\[
\begin{aligned}
 I_N^{ab}&=\frac{a_N^2}{2}e^{-\nu_N\omega(t_a+t_b)},\\
 D_N^{ab}&=\frac{a_N^2}{2}
     \left(e^{-\nu_N\omega|t_a-t_b|}
                         -e^{-\nu_N\omega(t_a+t_b)}\right),\\
 (I_N+D_N)^{ab}&=\frac{a_N^2}{2}e^{-\nu_N\omega|t_a-t_b|}.
\end{aligned}
\tag{8.2}
\]

To derive the second line, integrate the exponential in (1.3) over
\([0,\min(t_a,t_b)]\) and use \(c_N/\nu_N=a_N^2\). This checks both the
factor two in the noise and the unequal-time endpoint. The last line is
also the exact finite-\(N\) covariance of the scaled empirical Fourier
statistics, because the particles are iid stationary heat diffusions.
Orthogonal cosine/sine modes have zero cross entries by Fourier orthogonality.
The nonlinear remainder and the actual zero-terminal pair corrector vanish
identically in this model.

As \(\beta_N\to\infty\), the initial covariance for this same mode tends to
the rank-one matrix whose entries are \(1/2\), and the dynamic covariance
tends to zero. As \(\beta_N\to0\), \(a_N^2=\beta_N\to0\), and both matrices
tend to zero for all fixed times, including zero. There is no contradiction
with \(c_N=1\) in this regime: the backward heat gradients decay on the
short time scale, and their integrated contribution is the quantity in
(8.2). For a finite positive limiting temperature, (8.2) retains the expected
nontrivial temporal covariance. These checks do not require a uniform bound
on a backward solution involving \(1/\nu_N\).

### Dependence diagnostic

A centered continuous martingale need not become independent of its initial
data merely because all their covariances vanish. For example, a Brownian
integral with a nonconstant positive \(\mathcal F_0\)-measurable volatility
has an initial-data-dependent random terminal bracket and generally a
Gaussian mixture law. That diagnostic does not satisfy (5.5) with a
deterministic limit. Estimate (6.3), whose error is controlled by the actual
bracket discrepancy, is the step that excludes this failure mechanism here.

## 9. Scope and conclusion of the reconstruction

Every decisive limiting step has been reconstructed from the statement:
the triangular iid characteristic function; the actual interacting-law
bracket estimate; conditional characteristic-function factorization against
the initial sigma field; the finite-dimensional Gaussian convergence; the
linearized reduction; and the mean-field bias. The finite family and all
temperature factors are explicit. The conditional exponential proof is
independent of any external martingale central limit theorem.

This proves the precise fixed-smooth finite-list criterion, contingent only
on the frozen hypotheses, including the covariance limits. It does not prove
that those limits exist for every temperature sequence, identify a singular
limit, give a field/path topology, prove tightness in such a topology, extend
to a different initial law, or close the singular critical mission. The
earlier residual/coupling prerequisite was constructed by this same agent;
the present statement-only reconstruction does not independently audit that
prerequisite.

No comparison with an unseen Gaussian constructor proof has occurred. The
appropriate next step is a separately recorded comparison after this report
has been frozen by hash. Any resulting discrepancy must be addressed without
rewriting the issued reconstruction.

## 10. Provenance and execution record

Permitted current-worktree inputs actually read:

- `TASKS/ACTIVE/TASK-019_ROUND002_GAUSSIAN_BLIND.md`, the statement-only task.
- `AGENTS.md` and the already-known governing campaign instructions.
- `TASKS/ACTIVE/ROUND_001_MODEL.md` and
  `TASKS/ACTIVE/PO-001_RESIDUAL.md` for the frozen model and assumptions.
- `MEMORANDA/ROUND_001_ALGEBRA.md`, its smooth one-body identity and
  normalization; the same decisive coefficient is reconstructed in Section 3.

Prior permitted own construction retained in context, not newly read from
another worktree:

- TASK-010, `MEMORANDA/ROUND_002_COUPLING.md`, sealed SHA-256
  `7eb57c1f4e8f6da9c80a2f53a95349153605467532afb33b269938b242761852`.
- TASK-013, `MEMORANDA/ROUND_002_POWERCOUNT.md`, sealed SHA-256
  `f0bd6a670b194767afa2fe75f259d59bfe4589433f21252992d1dde79c92f01d`.

No external quantitative source theorem is imported. The proof uses finite
sums, elementary Fourier/Hilbert estimates, smooth Itô calculus, bounded
complex stochastic exponentials justified directly, and the explicit
Gaussian smoothing argument in Section 7. The existing input PDF was not
used mathematically; its integrity is checked by the campaign verifier.

The reconstruction and its optional exact self-check/output are the only
new deliverables; the pre-existing untracked TASK-019 card is preserved.
Canonical state, existing audit reports, frozen sources, and tracked files
remain unchanged. No commit, push, dependency installation, child worker,
or remote mutation was performed. No TeX was modified; the final worker
handoff contains no mathematical LaTeX.

Current input hashes:

| Input | SHA-256 |
|---|---|
| TASK-019 statement-only card | `9e7daabf12ca6861cd62587646ec2e077f0bd127018196842380afc44d771c40` |
| ROUND_001_MODEL.md | `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57` |
| PO-001_RESIDUAL.md | `c6a082a848df837454d11c18af1b3297fad348660c59f8811968bd0f4cd5fb36` |
| ROUND_001_ALGEBRA.md | `e5db5923ba82bf929218e23fe641ed5a7387c106220e6374f37bd06b80c3e4de` |

Verification:

- `python3 scripts/verify_campaign.py`: PASS before reconstruction and after
  the new outputs were created. The imported source note hash remains
  `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`.
- `python3 DISCOVERY_CODE/check_round002_gaussian_blind_exact.py`: PASS,
  2,147 exact checks. Output:
  `DISCOVERY_CODE/round002_gaussian_blind_exact_output.json`. The checks cover
  temperature factors, unequal-time overlap exponents, the free-heat
  covariance split and positive semidefiniteness, zero-time rows, duplicate
  times and degeneracy, the exponential Itô cancellation, and a random-bracket
  mixture diagnostic. These are supporting coefficient/model checks, not a
  numerical proof of convergence or an audit of an unseen argument.
- Runtime: Python 3.9.6, standard library only. Arithmetic is integer and
  `fractions.Fraction`; no random seed or numerical tolerance is used.
  Computation status: `REPRODUCED / SELF_CHECKED`.
- `git diff --check`: PASS. Direct checks of the three new files confirm
  their final newlines and absence of trailing whitespace or control
  characters outside newlines/tabs.
- `git status --short`: only this reconstruction, its check program/output,
  and the pre-existing TASK-019 card are untracked; no tracked modification.

The report hash is supplied separately. This reconstruction is sealed at
handoff before comparison, and its bytes must remain unchanged afterward.
