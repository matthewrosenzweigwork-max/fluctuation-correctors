# Round 002: the fixed-smooth iid residual by synchronous coupling

Date: 2026-09-17 UTC. Task: TASK-010. Worktree:
`/private/tmp/hocf-round002-coupling-20260917`.
Starting commit: `a06178658d1e3d458536ff312ca793947212ec67`.
Frozen scientific model: `TASKS/ACTIVE/ROUND_001_MODEL.md`.
Exact target: `TASKS/ACTIVE/PO-001_RESIDUAL.md`, version 1.0.

Mathematical status: `PROVED_CANDIDATE` for that fixed-smooth iid assertion.
Audit status: `SELF_CHECKED`; this report is not an independent audit.
Proof provenance: self-contained finite sums, Fourier estimates, elementary
independence, synchronous coupling, and smooth Itô calculus. No quantitative
propagation-of-chaos, concentration, equilibrium, or private-source theorem is
imported. The root coordinator owns the fresh hostile review and canonical
ledger integration. No Round 002 constructor report from another lane was read.

## 1. Exact assertion, negation, and quantitative conclusion

Fix an integer dimension \(d\geq1\), a finite horizon \(T\geq0\), and the frozen
smooth periodic functions \(g,V\). On the unit torus, of Haar mass one, let
\(K=-\nabla g\), \(b=-\nabla V\), and \(\nu=\beta^{-1}\), where
\(N\geq2\) and \(\beta>0\) are arbitrary. The kernel is even, so \(K(0)=0\).
For independent Brownian motions and iid initial positions of law \(\mu_0\),

\[
 dx_i=\left(b(x_i)+\frac1N\sum_{j\ne i}K(x_i-x_j)\right)dt
                +\sqrt{2\nu}\,dW_i,
 \qquad
 \partial_t\mu=-\operatorname{div}((b+K*\mu)\mu)+\nu\Delta\mu.
 \tag{1.1}
\]

Initial positions and the Brownian motions are independent, as in the usual
adapted iid initialization of the frozen diffusion. The deterministic reference
\(\mu=\mu^{N,g}\) is the stated smooth solution with initial value \(\mu_0\).
Write \(\eta=N^{-1}\sum_i\delta_{x_i}\) and \(\rho=\eta-\mu\). All centering
below remains mean-field centering.

Let \(f_t=f_t^N\) and the symmetric \(\Phi_t=\Phi_t^N\) be the deterministic
tests in the residual card, including the full backward equations and the
zero-terminal pair condition specified there. All particle tuples in \(U_k\)
are ordered and have distinct labels, with denominator \(N^k\), and
\(P_N=U_2/2\). Define exactly

\[
 F_t=C\Phi_t=\operatorname{Sym}_3
       [K(x-z)\cdot\nabla_1\Phi_t(x,y)],
 \qquad
 \sigma_N=\sqrt N\min(\sqrt\beta,1),
 \tag{1.2}
\]

where the symmetrization is the average over all six permutations.

The primary assertion is that all four nonnegative residual quantities in
PO-001 tend to zero, for every temperature sequence and all data obeying its
uniform \(C^{4d+12}\) assumption. Its logical negation is the existence of fixed
permitted data and a temperature sequence obeying that assumption for which at
least one such quantity has positive limsup, or a required uniform constant
does not follow from the declared data. The following explicit bounds prove
the assertion. Their constants are defined in Section 2 and contain no
\(N\), \(\beta\), or hidden background derivative:

\[
\begin{aligned}
 \sigma_N\mathbb E|P_N[\Phi_0]|
   &\le I\,\frac{\min(\sqrt\beta,1)}{\sqrt N},\\
 \sigma_N\mathbb E\left|\int_0^T U_3[F_t]dt\right|
   &\le T C_3\,\frac{\min(\sqrt\beta,1)}{N},\\
 \sigma_N^2\mathbb E[M_\Phi]_T
   &\le 2T H^2\,\frac{\min(1,\beta^{-1})}{N},\\
 \sigma_N^2\mathbb E|[M_f,M_\Phi]_T|
   &\le 2T L_fH\,\frac{\min(1,\beta^{-1})}{\sqrt N}.
\end{aligned}
\tag{1.3}
\]

For the cubic term we prove the stronger bound with
\(\mathbb E\int_0^T|U_3[F_t]|dt\) on the left before multiplication by
\(\sigma_N\). For the cross variation we bound its total variation in
expectation, also stronger than the stated absolute terminal covariation.
Consequently no signed cancellation is being substituted for an absolute
estimate.

The result does not identify a limiting Gaussian law or prove field tightness.
It proves the first bounded residual assertion. The fixed-kernel constants
below are not uniform in a singular Riesz cutoff; the singular subcritical and
critical missions remain separate.

## 2. All constants and norm orders

For a scalar function, \(\|\cdot\|_{C^m}\) is the maximum of the suprema of all
componentwise spatial derivatives of total order at most \(m\), precisely as
in the task. For vector fields use the maximum over components as well. Put

\[
\begin{gathered}
 q=\lfloor d/2\rfloor+2,\qquad r_*=3q+1,\qquad
 w_k=1+4\pi^2|k|^2,\qquad Q=(d+1)^{q/2},\\
 B=\left(\sum_{k\in\mathbb Z^d}w_k^{-q}\right)^{1/2},\qquad
 D=\left(\sum_{k\in\mathbb Z^d}4\pi^2|k|^2w_k^{-q}\right)^{1/2},\\
 \kappa_m=\max_{a,\,|\alpha|\le m}\|\partial^\alpha K_a\|_\infty,
 \qquad v_1=\max_{a,\,|\alpha|\le1}\|\partial^\alpha b_a\|_\infty.
\end{gathered}
\tag{2.1}
\]

Both lattice sums converge because \(q>d/2+1\); grouping lattice points in
annuli reduces the second to a convergent sum of powers with exponent
\(d+2-2q<0\). These constants depend only on \(d\). The norms of \(K\) are
bounded by the corresponding \(C^{m+1}\) norms of \(g\); \(v_1\) is bounded by
\(\|V\|_{C^2}\).

The scalar Sobolev convention is
\(\|h\|_{H^q}^2=\sum_kw_k^q|\widehat h(k)|^2\), with the Fourier characters
\(e^{2\pi i k\cdot x}\). Define

\[
\begin{gathered}
 \mathcal K=\left(\sum_{a=1}^d\|K_a\|_{H^q}^2\right)^{1/2}
       \le\sqrt d\,Q\kappa_q,
 \qquad L=d(v_1+2\kappa_1),\\
 h_L(T)=\begin{cases}(e^{LT}-1)/L,&L>0,\\ T,&L=0,\end{cases}
 \qquad J=2\,3^{7/6}B,\qquad
 R=J(1+D\mathcal K h_L(T)).
\end{gathered}
\tag{2.2}
\]

Thus the only nonpolynomial data dependence used below is the displayed
finite-horizon exponential in the Lipschitz norms of the fixed drift.
No inverse diffusion coefficient appears in \(R\).

For the deterministic test family set

\[
 A_m=\sup_{N,\,t\in[0,T]}\|\Phi_t^N\|_{C^m},\qquad
 A_f=\sup_{N,\,t\in[0,T]}\|f_t^N\|_{C^1},\qquad
 G_m=d\,2^m\kappa_m A_{m+1}\quad(0\le m\le3q).
\tag{2.3}
\]

The constants in (1.3) are

\[
\begin{aligned}
 I&=\tfrac12(Q^2 A_{2q}B^2+A_0),\\
 C_3&=Q^3G_{3q}R^3+3QG_qR,\\
 L_\Phi&=\sqrt d\,Q A_{q+1},\qquad
 D_\Phi=\sqrt d\,A_1,\qquad
 H=L_\Phi R+D_\Phi,\qquad L_f=\sqrt d\,A_f.
\end{aligned}
\tag{2.4}
\]

Under the frozen assumption all required \(A_m\) and \(A_f\) are at most
the card's \(A\), because
\(r_*=3\lfloor d/2\rfloor+7\le4d+12\). The mean-field solution enters these
constants only through its probability mass one. No uniform lower bound,
upper bound, or derivative of \(\mu\) is required for the residual argument.
This does not prove the uniform bounds on the backward solutions; those are
explicit hypotheses of the card.

## 3. Elementary Fourier bounds

For a real signed measure \(\zeta\), use the real Hilbert space underlying

\[
 \|\zeta\|_{-q}^2=\sum_kw_k^{-q}|\widehat\zeta(k)|^2.
 \tag{3.1}
\]

The Fourier definition gives, directly,

\[
 \|\delta_x\|_{-q}=B,
 \qquad
 \|\delta_x-\delta_y\|_{-q}\le D|\widetilde x-\widetilde y|,
 \tag{3.2}
\]

where any chosen lifts to \(\mathbb R^d\) can be used on the right. Indeed
\(|e^{2\pi ik\cdot x}-e^{2\pi ik\cdot y}|
 \le2\pi|k|\,|\widetilde x-\widetilde y|\). Also

\[
 |\langle h,\zeta\rangle|\le\|h\|_{H^q}\|\zeta\|_{-q},
 \qquad \|h\|_{H^q}\le Q\|h\|_{C^q}.
 \tag{3.3}
\]

The second inequality follows by expanding
\((1+\sum_{a=1}^d4\pi^2k_a^2)^q\) with the multinomial theorem and applying
Parseval. The sum of its nonnegative coefficients is \((d+1)^q\), and each
resulting derivative has order at most \(q\). The mass of the torus is one.

For a smooth kernel \(H_k\) on \((\mathbb T^d)^k\), Cauchy--Schwarz in all
Fourier variables similarly gives

\[
 |\langle H_k,\zeta_1\otimes\cdots\otimes\zeta_k\rangle|
 \le \|H_k\|_{H^{q,\ldots,q}}\prod_{j=1}^k\|\zeta_j\|_{-q}
 \le Q^k\|H_k\|_{C^{kq}}\prod_{j=1}^k\|\zeta_j\|_{-q}.
 \tag{3.4}
\]

Here the first norm has Fourier weight \(\prod_{j=1}^k w_{k_j}^q\).
Its derivative expansion uses at most \(q\) derivatives in each slot and
at most \(kq\) in total. Initially proving (3.4) for trigonometric polynomials
and then taking their smooth Fourier approximations justifies the measure
pairings. Equivalently, the tensor negative norm is exactly the product of
the negative norms in (3.1).

A useful bound for the partially diagonal cubic kernel is cheaper. For any
probability measure \(\theta\),

\[
 \left|\iint F(x,x,y)\,d\theta(x)d\zeta(y)\right|
 \le Q\|F\|_{C^q}\|\zeta\|_{-q}.
 \tag{3.5}
\]

For each fixed \(x\) apply (3.3) only in the last variable and then integrate
the resulting uniform bound against \(\theta\). No derivative of a diagonal
trace in the repeated variable is needed.

## 4. Iid moments and synchronous coupling

### 4.1. An iid Hilbert-space estimate proved by finite expansion

Let \(Y_1,\ldots,Y_N\) be independent with any common probability law
\(m\) on the torus and put
\(\overline\rho=N^{-1}\sum_i\delta_{Y_i}-m\). This law may depend on
\(N,t,\beta\). Set \(Z_i=\delta_{Y_i}-m\) in the real Hilbert space (3.1).
Then \(\mathbb EZ_i=0\) and \(\|Z_i\|_{-q}\le2B\). Independence gives

\[
 \mathbb E\|\overline\rho\|_{-q}^2
  =\frac{B^2-\|m\|_{-q}^2}{N}\le\frac{B^2}{N}.
 \tag{4.1}
\]

To control higher absolute moments, expand
\(\|\sum_iZ_i\|^6=(\sum_{i,j}\langle Z_i,Z_j\rangle)^3\).
An index appearing exactly once in one of its six positions makes the
expectation zero: condition on all the other random vectors and use that the
remaining factor is linear in the centered vector. A surviving term therefore
has at most three distinct indices. The number of index lists with at most
three distinct indices is bounded above by

\[
 \sum_{\ell=1}^3\binom N\ell\ell^6
 \le3^7N^3.
 \tag{4.2}
\]

This overcounts, which is harmless. Each term has absolute value at most
\((2B)^6\). Dividing by \(N^6\) and using the monotonicity of probability
\(L^p\) norms proves, for every \(1\le p\le6\),

\[
 \big(\mathbb E\|\overline\rho\|_{-q}^p\big)^{1/p}
 \le\frac{J}{\sqrt N}.
 \tag{4.3}
\]

This proof is dimension-independent after \(B\) is specified. No concentration
theorem, Gaussian limit, or assumption about the future particle law enters it.

### 4.2. The independent nonlinear comparison particles

For the actual system (1.1), choose lifts of its initial positions in a
fundamental cube. Construct comparison particles with the same initial
positions and the same Brownian motions:

\[
 d\widetilde y_i=(b+K*\mu_t)(\widetilde y_i)dt
                       +\sqrt{2\nu}\,dW_i,
 \qquad \widetilde y_i(0)=\widetilde x_i(0),
 \tag{4.4}
\]

where periodic coefficients are evaluated on the lifts. Smooth bounded
Lipschitz coefficients give unique global solutions by the integral-equation
Picard iteration. Since the drift in (4.4) is deterministic, the processes
\(y_i\) are independent and identically distributed. Their one-time law is
\(\mu_t\). For completeness, for any smooth terminal scalar test the backward
expectation for (4.4) solves the linear backward equation with drift
\(b+K*\mu_t\). This follows from the Markov property and smooth Itô calculus;
spatial differentiability follows by differentiating its smooth additive-noise
flow. Pairing that backward solution with either the given smooth
Fokker--Planck solution or the law of (4.4) gives the same constant initial
pairing. Equality for all terminal smooth tests identifies both laws. This
uses the given deterministic reference, and does not assume that the
interacting particles have that law.

Write \(\overline\eta_t=N^{-1}\sum_i\delta_{y_i(t)}\),
\(\overline\rho_t=\overline\eta_t-\mu_t\), and

\[
 e_i(t)=\widetilde x_i(t)-\widetilde y_i(t),\qquad
 D_N(t)=\frac1N\sum_i|e_i(t)|.
 \tag{4.5}
\]

The noise cancels exactly in \(e_i\). Since \(K(0)=0\), the deleted force is
also exactly the full empirical force for both configurations; there is no
discarded self-force. The Lipschitz constants of \(b,K\) in Euclidean norm
are at most \(dv_1,d\kappa_1\), respectively. Splitting the force difference
into the displacement of both arguments and the independent empirical error
gives, for almost every time,

\[
\begin{aligned}
 \frac d{dt}|e_i|
 &\le d(v_1+\kappa_1)|e_i|+d\kappa_1D_N
                    +|(K*\overline\rho_t)(y_i)|,\\
 \frac d{dt}D_N
 &\le LD_N+\sup_x|(K*\overline\rho_t)(x)|
 \le LD_N+\mathcal K\|\overline\rho_t\|_{-q}.
\end{aligned}
\tag{4.6}
\]

The norm inequality at \(e_i=0\) follows from the elementary inequality for
the derivative of the norm of an absolutely continuous vector. The last
inequality is (3.3), componentwise, followed by the Euclidean sum; translation
and reflection preserve the \(H^q\) norm of each component of \(K\).
Consequently the scalar integrating-factor argument and \(D_N(0)=0\) give

\[
 D_N(t)\le\mathcal K\int_0^t e^{L(t-s)}
                                 \|\overline\rho_s\|_{-q}\,ds.
 \tag{4.7}
\]

For every individual time, (3.2) and the triangle inequality yield

\[
 \|\rho_t\|_{-q}
 \le\|\overline\rho_t\|_{-q}+D D_N(t).
 \tag{4.8}
\]

Apply Minkowski's inequality in probability and in the time integral of
(4.7), and then (4.3) at each time. For every \(1\le p\le6\),

\[
 \boxed{\quad
 \sup_{0\le t\le T}
    \big(\mathbb E\|\rho_t\|_{-q}^p\big)^{1/p}
 \le\frac{R}{\sqrt N}.
 \quad}
 \tag{4.9}
\]

All integrals are justified directly by boundedness of probability measures
in (3.1). No time independence of the comparison particles is used. The
supremum is outside the expectation; (4.9) does not claim a bound on
\(\mathbb E\sup_t\|\overline\rho_t\|_{-q}^p\) uniform at arbitrarily rapid
diffusion. Neither the comparison nor the moments contain \(\nu\). This is
the needed law-specific estimate for the actual evolved interacting law,
proved here rather than inserted as a chaos hypothesis.

## 5. Exact diagonal conversion and the cubic absolute estimate

The following identities are pointwise in every configuration, including
coincident coordinates. For a symmetric pair kernel,

\[
 U_2[\Phi]=\langle\Phi,\rho^{\otimes2}\rangle
              -\frac1N\int\Phi(x,x)\,d\eta(x).
 \tag{5.1}
\]

For a symmetric triple kernel,

\[
 U_3[F]=\langle F,\rho^{\otimes3}\rangle
       -\frac3N\iint F(x,x,y)\,d\eta(x)d\rho(y)
       +\frac2{N^2}\int F(x,x,x)\,d\eta(x).
 \tag{5.2}
\]

To verify the second identity directly, let the full empirical cubic sum be
\(\langle F,\eta^{\otimes3}\rangle\). Inclusion-exclusion over its three
pairwise label-equality events subtracts
\(3N^{-1}\langle F(x,x,y),\eta\otimes\eta\rangle\) and adds back
\(2N^{-2}\langle F(x,x,x),\eta\rangle\). Every intersection of two equality
events is the same all-equal event, so the coefficient is \(3-1=2\).
Each of the three empirical-empirical-background terms has its empirical
diagonal deleted. Substituting its full-product value subtracts the term
\(-3N^{-1}\langle F(x,x,y),\eta\otimes\mu\rangle\) with the opposite sign.
The full-product parts form \(\rho^{\otimes3}\); the remaining two-variable
terms form \(\eta\otimes\rho\). This proves (5.2), including \(N=2\), where
the all-distinct triple sum is empty.

Equations (3.4), (3.5), and (4.9) imply for every smooth symmetric \(F_t\),

\[
 \mathbb E|U_3[F_t]|
 \le\frac{Q^3\|F_t\|_{C^{3q}}R^3
                       +3Q\|F_t\|_{C^q}R}{N^{3/2}}
                   +\frac{2\|F_t\|_\infty}{N^2}.
 \tag{5.3}
\]

The leading term uses a third absolute moment of the empirical discrepancy,
not the expectation of its cube. The partial diagonal uses a first absolute
moment, with its explicit extra \(1/N\).

For the actual kernel \(F_t=C\Phi_t\), the all-equal term vanishes exactly,
because every summand contains \(K(0)=0\). Componentwise Leibniz expansion
also gives

\[
 \|C\Phi_t\|_{C^m}\le d\,2^m\kappa_m\|\Phi_t\|_{C^{m+1}}
                  \le G_m,\qquad 0\le m\le3q.
 \tag{5.4}
\]

A derivative in \(z\) of \(K(x-z)\) changes only a sign, and permutation of
slots does not enlarge a maximum derivative norm. Thus the displayed
Leibniz coefficient includes every composition and symmetrization factor.
It follows that

\[
 \sup_{t\le T}\mathbb E|U_3[C\Phi_t]|
       \le\frac{C_3}{N^{3/2}},\qquad
 \mathbb E\int_0^T|U_3[C\Phi_t]|dt\le\frac{TC_3}{N^{3/2}}.
 \tag{5.5}
\]

This closes the exact first open load-bearing line in the residual card,
within its declared fixed-smooth iid scope. In particular, replacing the
cubic statistic at interacting positions by its iid value was unnecessary.

## 6. Initial pair and lower contractions

At time zero the actual positions are iid. Apply (5.1), (3.4) with \(k=2\),
and the sharper initial second moment (4.1):

\[
 \mathbb E|P_N[\Phi_0]|
 \le\frac12\left(Q^2A_{2q}\mathbb E\|\rho_0\|_{-q}^2
                            +\frac{A_0}{N}\right)
 \le\frac{I}{N}.
 \tag{6.1}
\]

The deletion is not omitted or replaced by Wick centering. In particular,
direct iid expectation gives
\(\mathbb E U_2[\Phi_0]=-\langle\Phi_0,\mu_0^{\otimes2}\rangle/N\), which
is generally nonzero. The absolute bound (6.1) controls this bias together
with its random part.

For reference, in the frozen corrected identity the two lower drifts are

\[
 \frac1N\langle(B\Phi_t)_{\mu_t},\rho_t\rangle
 +\frac1{2N}\langle B\Phi_t,\mu_t^{\otimes2}\rangle,
 \qquad
 B\Phi=K(x-y)\cdot(\nabla_1-\nabla_2)\Phi.
 \tag{6.2}
\]

Since \(\|\rho\|_{\mathrm{TV}}\le2\) and
\(\|B\Phi_t\|_\infty\le2d\kappa_0A_1\), their integrated absolute value is
bounded, configuration by configuration, by

\[
 \frac{5Td\kappa_0A_1}{N}.
 \tag{6.3}
\]

Multiplication by \(\sigma_N\le\sqrt N\) therefore makes these terms vanish
as well, with no centering adjustment or law substitution.

## 7. Pair martingale and its cross variation

For clarity, the bracket coefficients are rederived from the pair statistic,
rather than assumed from a previous report. Differentiating its explicit
ordered sum and using symmetry gives

\[
 \nabla_{x_i}P_N[\Phi_t]=\frac1N H_{i,t},\qquad
 H_{i,t}=\frac1N\sum_{j\ne i}\nabla_1\Phi_t(x_i,x_j)
                       -\int\nabla_1\Phi_t(x_i,y)\,d\mu_t(y).
 \tag{7.1}
\]

The factor two from differentiating both ordered slots cancels the factor
\(1/2\) in \(P_N\). The background is deterministic. Thus Itô calculus gives

\[
 dM_\Phi=\frac{\sqrt{2\nu}}N\sum_i H_{i,t}\cdot dW_i,
 \qquad
 dM_f=\frac{\sqrt{2\nu}}N\sum_i\nabla f_t(x_i)\cdot dW_i.
 \tag{7.2}
\]

Independent noises then give exactly

\[
\begin{aligned}
 [M_\Phi]_T&=\frac{2\nu}{N^2}\sum_i\int_0^T|H_{i,t}|^2dt,\\
 [M_f,M_\Phi]_T&=\frac{2\nu}{N^2}\sum_i\int_0^T
                      \nabla f_t(x_i)\cdot H_{i,t}\,dt.
\end{aligned}
\tag{7.3}
\]

These are both the pathwise and predictable quadratic covariations for these
continuous Brownian integrals. Their integrands are bounded for fixed \(N,\beta\)
and the finite horizon, so the martingales are square integrable.

The exact conversion retaining the omitted label is

\[
 H_{i,t}=\int\nabla_1\Phi_t(x_i,y)\,d\rho_t(y)
                         -\frac1N\nabla_1\Phi_t(x_i,x_i).
 \tag{7.4}
\]

For each component apply (3.3) only in \(y\), uniformly in \(x_i\). This proves
the pathwise bound

\[
 \max_i|H_{i,t}|\le L_\Phi\|\rho_t\|_{-q}+\frac{D_\Phi}{N}.
 \tag{7.5}
\]

It is valid even though the argument \(x_i\) and the signed measure \(\rho_t\)
are dependent. No conditioning or fictitious independence is used. Combining
(7.5) and the second and first moments from (4.9) gives

\[
\begin{aligned}
 \mathbb E\frac1N\sum_i|H_{i,t}|^2
   &\le\left(\frac{L_\Phi R}{\sqrt N}+\frac{D_\Phi}{N}\right)^2
     \le\frac{H^2}{N},\\
 \mathbb E\frac1N\sum_i|H_{i,t}|
   &\le\frac{L_\Phi R}{\sqrt N}+\frac{D_\Phi}{N}
     \le\frac H{\sqrt N}.
\end{aligned}
\tag{7.6}
\]

The two raw estimates are therefore

\[
 \mathbb E[M_\Phi]_T\le\frac{2\nu TH^2}{N^2},\qquad
 \mathbb E\operatorname{TV}_{[0,T]}[M_f,M_\Phi]
                   \le\frac{2\nu T L_fH}{N^{3/2}}.
 \tag{7.7}
\]

The cross variation's total variation bounds its absolute terminal value.
Alternatively its raw order follows from Cauchy--Schwarz between (7.7)'s
pair bracket and
\(\mathbb E[M_f]_T\le2\nu T L_f^2/N\), which independently checks the
power of \(N\) in the cross estimate.

Finally \(\sigma_N^2\nu=N\min(1,\beta^{-1})\). Equations (5.5), (6.1), and
(7.7) prove every line of (1.3). The worst bounds over all \(\beta>0\) are
\(O(N^{-1/2})\), \(O(N^{-1})\), \(O(N^{-1})\), and \(O(N^{-1/2})\),
respectively. No assumption on a limiting temperature is needed.

## 8. A separately labeled regularity refinement

**Additional proved candidate, not an amendment of the frozen card.**
Retaining smoothness for each fixed parameter to justify Itô and the SDEs,
the residual estimates require only the uniform pair-test norm
\(A_{r_*}<\infty\), the uniform one-body norm \(A_f<\infty\), and the fixed
kernel/drift norms \(\kappa_{3q}<\infty\), \(v_1<\infty\), where
\(r_*=3\lfloor d/2\rfloor+7\). No uniform background derivative is needed.
The statement holds for every such deterministic smooth symmetric pair test
and deterministic smooth one-body test; their particular backward equations
are not used by this probabilistic estimate. It therefore applies to the
card's backward solutions once their assumed norms hold.

This is a reduction of the sufficient uniform regularity assumptions, proved
by the displayed norm orders; it is not a claim of optimal regularity or of
existence with those weaker bounds. The canonical \(r=4d+12\) statement has
not been altered by this worker.

## 9. Direct test calculations and adversarial self-check

The tests in this section use direct finite sums and the free heat law, rather
than the negative-Sobolev coupling inequalities. They constitute a distinct
falsification mechanism in this context, not an isolated audit.

### 9.1. Constants and small particle numbers

For constant pair and triple kernels, the exact values are

\[
 U_2[1]=-\frac1N,\qquad U_3[1]=\frac2{N^2}.
 \tag{9.1}
\]

The latter follows directly from
\((N)_3/N^3-3(N)_2/N^2+3-1\), including \(N=2\). These tests detect both
the pair bias and the all-equal coefficient in (5.2). The triple full-product
term and its partial diagonal vanish for the constant kernel because
\(\rho(1)=0\); only the final term of (5.2) remains. The special zero full
diagonal of \(C\Phi\) was used only after proving the general identity.

### 9.2. Exact free-heat Fourier moments

Take \(b=K=0\), \(\mu_0=1\); at each time the particles are iid Haar for
every \(\nu>0\). Let
\(\varphi(x)=\cos(2\pi k\cdot x)\) with \(k\ne0\), and write
\(c_0=\int\varphi^2=1/2\),
\(c_1=\int|\nabla\varphi|^2=2\pi^2|k|^2\). For a prescribed smooth pair
test \(\Phi_t=a(t)\varphi\otimes\varphi\), direct finite sums give

\[
\begin{aligned}
 P_N[\Phi_t]&=\frac{a(t)}{2N^2}\sum_{i\ne j}\varphi(x_i)\varphi(x_j),\\
 H_{i,t}&=\frac{a(t)}N\nabla\varphi(x_i)
                                    \sum_{j\ne i}\varphi(x_j),\\
 \mathbb E P_N[\Phi_t]^2&=\frac{a(t)^2(N-1)c_0^2}{2N^3},\\
 \mathbb E\frac d{dt}[M_\Phi]_t
     &=\frac{2\nu a(t)^2c_1c_0(N-1)}{N^3}.
\end{aligned}
\tag{9.2}
\]

Only matching unordered pairs survive the third line, and only equal summand
indices in the independent sum over \(j\ne i\) survive the fourth. They
confirm the pair orders \(N^{-1}\) and \(\nu N^{-2}\), with their factors of
two. A general cubic product test has

\[
 U_3[\varphi^{\otimes3}]=\frac1{N^3}
        \sum_{i,j,\ell\ \mathrm{distinct}}
                    \varphi(x_i)\varphi(x_j)\varphi(x_\ell),\qquad
 \mathbb E U_3[\varphi^{\otimes3}]^2
       =\frac{6(N)_3c_0^3}{N^6}.
 \tag{9.3}
\]

Thus the generic smooth cubic root-mean-square order \(N^{-3/2}\) is correct,
and the statistic is exactly zero for \(N=2\) in this product example.

For a one-body test \(f_t=c(t)\varphi\), put

\[
 Z_N=\frac1{N^2}\sum_{i\ne j}|\nabla\varphi(x_i)|^2\varphi(x_j).
\]

The cross bracket density is \(2\nu a(t)c(t)Z_N/N\). Its mean is zero, but
it is not zero as a random variable. Since
\(\int|\nabla\varphi|^2\varphi=0\) and
\(\int|\nabla\varphi|^4=6\pi^4|k|^4\), direct matching of labels gives

\[
 \mathbb E Z_N^2
 =\frac{N(N-1)c_0\int|\nabla\varphi|^4
       +N(N-1)(N-2)c_0c_1^2}{N^4}
 =\frac{\pi^4|k|^4(N-1)(2N-1)}{N^3}.
 \tag{9.4}
\]

This verifies the raw cross-density root-mean-square order
\(\nu N^{-3/2}\). Its vanishing signed mean would not have proved the
absolute estimate in the task. In the actual free-interaction corrector
problem the source \(J_f\) is zero and the zero-terminal corrector itself is
zero. The nonzero prescribed pair tests in (9.2)--(9.4) test the identities
and general residual bounds; they are not being misidentified as that free
corrector. The actual free corrector passes the target identically.

### 9.3. Temperature endpoints and limitations

For \(\beta\downarrow0\), the raw martingale bounds increase as
\(\beta^{-1}\), but \(\sigma_N^2=N\beta\) cancels that factor exactly.
For \(\beta\uparrow\infty\), \(\sigma_N^2=N\) and the bracket bounds improve
by \(\beta^{-1}\). The noise-canceling coupling proof is unchanged in both
limits. No dissipativity of the interaction was assumed: signed Fourier
kernels are allowed, and their possible finite-time amplification is included
in the explicit exponential of (2.2).

Replacing the fixed kernel by a singular approximation would insert its
derivatives into \(\kappa_{3q}\), \(\mathcal K\), and the exponential involving
\(\kappa_1\). This report proves neither their cutoff uniformity nor a joint
cutoff/model-comparison estimate. The parameters
\(\beta_NN^{2s/d-1}\), \(\lambda_N\to0\), and
\(\lambda_N\to\lambda>0\) remain distinct. No power of the reference Riesz
exponent occurs in this fixed-smooth argument, and no singular critical
truncation conclusion follows from it.

Other adversarial checks: the coupling starts from exact common iid samples;
the law of the interacting configuration is never asserted to be a product;
the fluctuation norm is centered at the prescribed mean field; the partial
diagonal in (5.2) is retained; the pair-gradient subtraction in (7.4) is
retained; every expectation estimate for a target is absolute; and no
supremum-in-time moment is silently substituted for pointwise moments.

## 10. Handoff, verification, and unchanged scope

The bounded assertion is proved by a complete candidate argument. There is
no remaining mathematical gap in that stated fixed-smooth residual estimate
identified by this self-check. A fresh hostile audit remains required before
promotion. This report does not close the complete smooth fluctuation theorem:
the limiting initial/one-body martingale law and any path/field topology still
need their own statements and proofs. Singular norm control, cutoff removal,
other initial laws, and critical higher-order survival remain open interfaces.

The root coordinator should integrate the candidate and its actual audit
status into the proof-obligation, theorem, constants, law/centering,
martingale, normalization, and regularization ledgers. This worker changes
none of them. No new stable theorem/audit identifier is assigned by this lane;
the result is attached to TASK-010 and the frozen PO-001 residual subproblem.

Inspected: the applicable instructions and governing specification; frozen
baseline and plan; all canonical state files; source manifest and the retained
text extraction of the imported note; the frozen model and residual task;
the relevant Round 001 pair identities and smooth-interface definitions.
The imported note supplies no mathematical input to this proof. A lightweight
memory lookup supplied historical routing only; all mathematical inputs and
current repository facts were verified locally.

Created: this memorandum and its exact-arithmetic self-check program/output
listed below. Pre-existing untracked TASK-010 card was preserved. Canonical
state, immutable sources, frozen specification, existing audit reports, and
tracked files remain unchanged. No commit, push, installation, or remote change
was performed. No TeX was modified; the mathematical deliverable is the
assigned Markdown memorandum, and the final worker handoff contains no
mathematical LaTeX.

Verification record:

- `python3 scripts/verify_campaign.py`: PASS before work and after the new
  outputs were created. Imported note SHA-256:
  `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`.
- `python3 DISCOVERY_CODE/check_round002_coupling_exact.py`: PASS, 1,292 exact
  checks. The recorded output is
  `DISCOVERY_CODE/round002_coupling_exact_output.json`. It covers the cubic
  diagonal conversion, pair diagonal conversion and rooted gradient, pair and
  cross bracket coefficients, the actual cubic full diagonal, constant tests,
  the Fourier moment formulas, temperature factors, and regularity orders.
  The configuration battery includes all four-grid configurations for N=2,3
  and three N=5 configurations, including coincident coordinates. Exact iid
  moments are summed for N=2,3,4,5. Computation status: `REPRODUCED`; audit
  status: `SELF_CHECKED`.
- Environment: system Python 3.9.6, standard library only; rational arithmetic
  uses `fractions.Fraction`. No random seed or numerical tolerance applies.
  The finite tests are supporting self-checks, not a universal proof or an
  independent computation certificate.
- `git diff --check`: PASS. A separate direct check of all three new output
  files found no trailing whitespace and confirmed their final newlines.
- `git status --short`: only the three new outputs and the pre-existing
  TASK-010 card are untracked; no tracked file is modified.

The final report hash is supplied separately so it does not recursively alter
its own content. This report is sealed at handoff; any subsequent mathematical
repair must be a separately identified addendum or superseding report.
