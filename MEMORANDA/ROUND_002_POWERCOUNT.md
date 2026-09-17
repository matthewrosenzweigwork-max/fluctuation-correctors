# Round 002: all-order smooth iid moments and the heat-cutoff interface

Date: 2026-09-17 UTC. Task: TASK-013. Worktree:
`/private/tmp/hocf-round002-powercount-20260917`.
Starting commit: `a06178658d1e3d458536ff312ca793947212ec67`.
Mathematical status: `PROVED_CANDIDATE` for the bounded statements below.
Audit status: `SELF_CHECKED`. This is construction, not independent review.

The starting model and centering are exactly
`TASKS/ACTIVE/ROUND_001_MODEL.md`: unit torus, gradient drift, iid initial
law, Brownian coefficient \(\sqrt{2/\beta}\), ordered distinct-label
statistics with denominators \(N^k\), and mean-field centering. The earlier
TASK-010 coupling report is used in its permitted construction role, with
SHA-256 `7eb57c1f4e8f6da9c80a2f53a95349153605467532afb33b269938b242761852`.
Its file was checked and remains unchanged. No other Round 002 constructor
report was read. The all-order moment improvement and partition formula are
proved here. The Round 001 recursion is used only in its explicitly stated
smooth finite-order scope, with its operators reproduced below.

## 1. Assertions and their limits

For every fixed smooth permitted kernel and every \(p\ge1\), the actual
evolved iid-prepared interacting law satisfies an explicit \(L^p\) bound of
order \(N^{-k/2}\) for every smooth \(U_k\). The bound is valid for all
integers \(k\ge0\), including \(k>N\), with its dependence on \(k,p\),
kernel norms, time, and test norms displayed. A rooted version gives all
quadratic and cross-variation bounds. No propagated product law is assumed.
The logical negation is a permitted instance violating one of the displayed
bounds with its declared constants.

For heat-regularized positive-power Riesz interactions, the same proof gives
an explicit sufficient joint-limit condition for the **regularized model's
own** fixed-order residuals. Under finite fixed-cutoff norm envelopes a
sufficiently slowly vanishing cutoff exists. This does not compare the
regularized particles or reference with their singular counterparts.

The negative conclusion is precise: the constants of this smooth mechanism
are not cutoff uniform, and its order gains contain no universal factor of
\(\lambda_N=\beta_NN^{s/d-1}\). Divergence of these proof constants does not
disprove a singular theorem or every different estimate.

The first missing singular input after this result is a fluctuation-scale
comparison with the singular dynamics, or a direct singular-compatible
replacement for the fixed-smooth empirical/kernel norm bounds. Critical
summation additionally requires actual order-uniform kernel and coefficient
control. A factorial count of partitions alone supplies neither input.

## 2. Norms and all-moment empirical control

Retain the following constants from the coupling proof, defining them here
to fix all conventions:

\[
\begin{gathered}
 q=\lfloor d/2\rfloor+2,\quad Q=(d+1)^{q/2},\quad
 w_n=1+4\pi^2|n|^2,\\
 B^2=\sum_{n\in\mathbb Z^d}w_n^{-q},\qquad
 D^2=\sum_{n\in\mathbb Z^d}4\pi^2|n|^2w_n^{-q},\\
 \|\zeta\|_{-q}^2=\sum_n w_n^{-q}|\widehat\zeta(n)|^2,
 \quad \kappa_m=\|K\|_{C^m},\quad v_1=\|b\|_{C^1},\\
 L=d(v_1+2\kappa_1),\quad
 \mathcal K=\left(\sum_{a=1}^d\|K_a\|_{H^q}^2\right)^{1/2}
       \le\sqrt d\,Q\kappa_q,\\
 h_L(T)=\begin{cases}(e^{LT}-1)/L,&L>0,\\T,&L=0,\end{cases}
 \qquad S=1+D\mathcal K h_L(T).
\end{gathered}
\tag{2.1}
\]

Vector \(C^m\) norms are maximum componentwise norms, with derivatives of
total order at most \(m\); the torus has mass one. The sums are finite since
\(q>d/2+1\). Let \(\rho_t=\eta_t-\mu_t\) for the actual interacting law.
For every real \(p\ge1\), define

\[
 m(p)=\lceil p/2\rceil,\qquad
 R_p=2BS\sqrt{2m(p)}.
 \tag{2.2}
\]

Then

\[
 \sup_{t\le T}\|\|\rho_t\|_{-q}\|_{L^p}
       \le R_pN^{-1/2}.
 \tag{2.3}
\]

Here and below the supremum in time is outside the expectation. All constants
are uniform over \(N\ge2\) and \(\beta>0\).

**Proof with the order dependence exposed.** At a fixed time let
\(Y_i\) be iid of law \(\mu_t\), and let \(Y_i'\) be independent copies.
In the real Hilbert space underlying the Fourier norm, Jensen's inequality
conditional on the \(Y_i\) gives

\[
 \mathbb E\left\|\sum_i(\delta_{Y_i}-\mu_t)\right\|_{-q}^{2m}
 \le\mathbb E\left\|\sum_i(\delta_{Y_i}-\delta_{Y_i'})\right\|_{-q}^{2m}.
 \tag{2.4}
\]

The independent differences are symmetric in law, so one can insert
independent signs \(\varepsilon_i\in\{-1,1\}\). For deterministic real
Hilbert vectors \(z_i\), expansion of the \(m\)-th power of the squared
norm, followed by \(|\langle z_i,z_j\rangle|\le\|z_i\|\|z_j\|\), gives

\[
 \mathbb E_\varepsilon\left\|\sum_i\varepsilon_i z_i\right\|^{2m}
 \le\mathbb E_\varepsilon\left(\sum_i\varepsilon_i\|z_i\|\right)^{2m}
 \le(2m-1)!!\left(\sum_i\|z_i\|^2\right)^m.
 \tag{2.5}
\]

For the second inequality only lists with even index multiplicities survive.
If the multiplicities are \(2a_i\), its multinomial coefficient is
\((2m)!/\prod_i(2a_i)!\). The inequality
\((2a_i)!\ge2^{a_i}a_i!\) compares these coefficients with those of the
right-hand side, because \((2m-1)!!=(2m)!/(2^m m!)\).
Since \(\|\delta_x\|_{-q}=B\), the differences in (2.4) have norm at most
\(2B\). Consequently, for the independent empirical discrepancy,

\[
 \mathbb E\|\overline\rho_t\|_{-q}^{2m}
 \le (2B)^{2m}(2m-1)!!N^{-m}.
 \tag{2.6}
\]

In particular its \(L^p\) norm is at most
\(2B((2m(p)-1)!!)^{1/(2m(p))}N^{-1/2}\), and this is bounded by
\(2B\sqrt{2m(p)}N^{-1/2}\). The explicit double factorial in (2.6) is a
sharper alternative to the simpler constant used in subsequent sums.

To transfer the estimate to the actual law, couple the independent nonlinear
particles with the interacting particles using identical initial samples and
Brownian motions, as in the sealed TASK-010 report. For their lifted mean
displacement \(D_N=N^{-1}\sum_i|x_i-y_i|\), noise cancellation, \(K(0)=0\),
and the Lipschitz estimates give

\[
 D_N(t)\le\mathcal K\int_0^t e^{L(t-r)}
                         \|\overline\rho_r\|_{-q}dr,
 \qquad
 \|\rho_t\|_{-q}\le\|\overline\rho_t\|_{-q}+D D_N(t).
 \tag{2.7}
\]

These pathwise inequalities are proved in Section 4 of that report; their
only ingredients are the exact common-noise cancellation and
\(\|\delta_x-\delta_y\|_{-q}\le D|x-y|\) for chosen lifts. Apply Minkowski
and (2.6) at each time to obtain (2.3), or its sharper double-factorial
version with the same multiplier \(S\). No \(\nu=1/\beta\) enters (2.7).
This proves the all-moment extension rather than assuming a quantitative
chaos theorem.

## 3. Exact partition conversion of every deleted statistic

Let \(\mathcal P_k\) be the partitions of \([k]\). For \(\pi\in\mathcal P_k\)
write \(j(\pi)\) for its number of singleton blocks, \(\ell(\pi)\) for the
number of nonsingleton blocks, and

\[
 c(\pi)=\prod_{A\in\pi}(|A|-1)!,\qquad
 a(\pi)=\sum_{A\in\pi}(|A|-1)=k-|\pi|,\qquad
 \Delta(\pi)=\frac12\sum_{|A|\ge2}(|A|-2)\ge0.
 \tag{3.1}
\]

Let \(\Phi_\pi\) be the kernel obtained by identifying all its arguments in
each block. The exact configuration-wise formula is

\[
 \boxed{
 U_k[\Phi]=\sum_{\pi\in\mathcal P_k}
   (-1)^{a(\pi)}c(\pi)N^{-a(\pi)}
   \int\Phi_\pi\,
      \prod_{|A|=1}\rho(dx_A)\prod_{|A|\ge2}\eta(dx_A).}
 \tag{3.2}
\]

The empty partition yields \(U_0[c]=c\). Deletion concerns labels, so the
formula remains valid at coincident spatial coordinates and for \(k>N\).

**Finite proof.** In a raw empirical product indexed by occupied slots, an
injective label assignment is selected by summing over partitions of those
slots with weight \(\prod_A(-1)^{|A|-1}(|A|-1)!\) and imposing equality
inside each block. For a label assignment with equality partition \(\tau\),
the total coefficient factors over its blocks. For a block of size \(r\),
the factor is the sum of \((-1)^{r-c(\sigma)}\) over all permutations of
\([r]\), where \(c(\sigma)\) is its number of cycles: each partition admits
\(\prod_A(|A|-1)!\) cycles. For \(r\ge2\) that sum is zero because multiplying
permutations by a fixed transposition pairs opposite signs; for \(r=1\) it
is one. Hence exactly the injective assignments survive.

Each equality block has one free particle label, so its normalized full sum
contributes \(N^{-(|A|-1)}\eta\). In the inclusion-exclusion defining
\(U_k\), fix all nonsingleton occupied blocks. Every remaining slot is either
an occupied singleton contributing \(\eta\) or a background slot contributing
\(-\mu\). Summing those choices gives \(\rho\) independently in every
remaining slot. This is (3.2), with no factorial normalization suppressed.

## 4. Quantitative all-order moments and explicit order constants

The Fourier tensor duality used below is

\[
 |\langle H,\zeta^{\otimes j}\rangle|
 \le \|H\|_{H^{q,\ldots,q}}\|\zeta\|_{-q}^j
 \le Q^j\|H\|_{C^{jq}}\|\zeta\|_{-q}^j.
 \tag{4.1}
\]

Its first inequality is Cauchy--Schwarz with tensor Fourier weights
\(\prod_{r=1}^jw_{n_r}^{q}\). The second follows by expanding these weights:
their derivative coefficients have sum \((d+1)^{jq}\), and all resulting
derivatives have total order at most \(jq\). This also proves that the stated
derivative orders, rather than a dimension-dependent unnamed norm, suffice.

In each term of (3.2), hold nonsingleton block variables fixed and apply
(4.1) only in the singleton slots. Then integrate against the probability
measures \(\eta\) in the other blocks. This is legitimate pointwise even
though these measures and \(\rho\) are dependent. Derivatives in singleton
slots do not differentiate a diagonal map. For every \(p\ge1\), Minkowski
and (2.3) give the more precise bound

\[
 \|U_k[\Phi_t]\|_{L^p}
 \le\sum_{\pi\in\mathcal P_k}
   c(\pi)Q^{j(\pi)}\|\Phi_t\|_{C^{j(\pi)q}}
   R_{p j(\pi)}^{j(\pi)}
   N^{-k/2-\Delta(\pi)}.
 \tag{4.2}
\]

When \(j=0\), the product involving \(R_{pj}\) is defined to be one and no
moment estimate is used. The exponent is exact in this estimate because

\[
 a(\pi)+j(\pi)/2
   =k-\ell(\pi)-j(\pi)/2=k/2+\Delta(\pi).
 \tag{4.3}
\]

Thus pair blocks have no extra power of \(N\); a block of size \(r\ge3\)
has an additional factor \(N^{-(r-2)/2}\). In particular the leading
\(N^{-k/2}\) bound includes both the full fluctuation product and all
singleton/pair partitions.

Define the following finite, fully specified constant:

\[
 C_{k,p}(N)=\sum_{\pi\in\mathcal P_k}
       c(\pi)(Q R_{p j(\pi)})^{j(\pi)}N^{-\Delta(\pi)},
 \qquad C_{0,p}(N)=1.
 \tag{4.4}
\]

Then for all \(k,N,p\) in the stated ranges,

\[
 \sup_{t\le T}\|U_k[\Phi_t]\|_{L^p}
 \le C_{k,p}(N)N^{-k/2}\sup_t\|\Phi_t\|_{C^{kq}}.
 \tag{4.5}
\]

This is an actual order constant, not an unspecified \(C_k\). It can be
computed without listing labeled partitions. If \(m_r\) denotes the number
of blocks of size \(r\), it equals

\[
 C_{k,p}(N)=
 \sum_{\substack{m_1,\ldots,m_k\ge0\\\sum r m_r=k}}
 \frac{k!\,(Q R_{p m_1})^{m_1}}
      {m_1!\prod_{r=2}^k m_r!r^{m_r}}
 N^{-\frac12\sum_{r=2}^k(r-2)m_r}.
 \tag{4.6}
\]

There is also a simple bound uniform in \(N\). Since \(R_{pj}\le R_{pk}\),
put \(A=Q R_{pk}\ge1\). The cycle-counting identity gives

\[
\begin{aligned}
 C_{k,p}(N)&\le\sum_{\pi\in\mathcal P_k}c(\pi)A^{j(\pi)}
 =k!\sum_{r=0}^k\frac{(A-1)^r}{r!}
 \le k!e^{Q R_{pk}-1}\\
 &\le k!\exp\big(2QB S\sqrt{pk+2}\big),\qquad k\ge1.
\end{aligned}
\tag{4.7}
\]

To obtain the identity, the exponential generating function is
\(\exp(Az+\sum_{r\ge2}z^r/r)=e^{(A-1)z}/(1-z)\).
If the additional powers of \(N\) are retained, the same generating function
with singleton weight \(A\) is

\[
 \exp\left(Az+\sum_{r\ge2}\frac{z^rN^{-(r-2)/2}}r\right)
 =e^{(A-\sqrt N)z}(1-z/\sqrt N)^{-N}.
 \tag{4.8}
\]

These are formal power-series coefficient identities; no convergence of an
infinite corrector expansion is inferred from them. The bound (4.7) is
conservative at large order. The trivial bound
\(|U_k[\Phi]|\le2^k\|\Phi\|_\infty\), from the original definition, also
holds for every \(k,N\) and can be taken in minimum with (4.5).

At the campaign scale the general statistical bound is

\[
 \sigma_N\sup_{t\le T}\|U_k[\Phi_t]\|_{L^p}
 \le \min(\sqrt\beta,1)N^{-(k-1)/2}
       C_{k,p}(N)\sup_t\|\Phi_t\|_{C^{kq}}.
 \tag{4.9}
\]

For any fixed order, fixed smooth kernel, and uniformly bounded displayed
test norm this tends to zero for \(k\ge2\), for every temperature sequence.
The Riesz exponent and \(\lambda_N\) do not appear in this assertion.

### Exact iid preparation bias

The deleted statistics need not have zero expectation, even initially. Direct
expectation of the distinct-label definition gives

\[
 \mathbb E U_k[\Phi_0]=\theta_{k,N}\langle\Phi_0,\mu_0^{\otimes k}\rangle,
 \qquad
 \theta_{k,N}=\sum_{r=0}^k(-1)^{k-r}\binom kr\frac{(N)_r}{N^r},
 \qquad
 \sum_{k\ge0}\theta_{k,N}\frac{z^k}{k!}=e^{-z}(1+z/N)^N.
 \tag{4.10}
\]

For fixed \(m\ge1\), its leading even coefficient is
\(\theta_{2m,N}=(-1)^m(2m-1)!!N^{-m}+O_m(N^{-m-1})\).
For fixed \(m\ge1\), the leading odd coefficient is

\[
 \theta_{2m+1,N}
 =\frac{(-1)^{m-1}(2m+1)!}{3\,2^{m-1}(m-1)!}N^{-m-1}
     +O_m(N^{-m-2}).
 \tag{4.11}
\]

Indeed the logarithm of (4.10)'s generating function starts with
\(-z^2/(2N)+z^3/(3N^2)-\cdots\); the leading even term uses only quadratic
blocks and the leading odd term uses one cubic block. These are explicit
initial-law statements, not assertions that the evolved law is iid.

## 5. Rooted statistics and all martingale brackets

For a particle label \(i\), put
\(\eta^{(i)}=\eta-N^{-1}\delta_{x_i}\) and
\(\rho^{(i)}=\rho-N^{-1}\delta_{x_i}\). The measure \(\eta^{(i)}\) is positive
of mass \(1-1/N\), and

\[
 \|\|\rho^{(i)}\|_{-q}\|_{L^p}
 \le (R_p+B)N^{-1/2}.
 \tag{5.1}
\]

Use \(V_n^{(i)}\) for the same centered distinct-label statistic in \(n\)
slots with label \(i\) excluded and denominator still \(N\), as in the frozen
recursion. The proof of (3.2) applies with \(\eta^{(i)},\rho^{(i)}\), without
changing its coefficients. Define

\[
 D_{n,p}(N)=\sum_{\pi\in\mathcal P_n}c(\pi)
       [Q(R_{p j(\pi)}+B)]^{j(\pi)}N^{-\Delta(\pi)},
 \qquad D_{0,p}(N)=1.
 \tag{5.2}
\]

The same convention applies at \(j=0\). For a root-dependent deterministic
kernel, apply the singleton derivative norm uniformly in the root before
putting the random value \(x_i\) in that slot. It follows that

\[
 \left\|V_{k-1}^{(i)}[\nabla_1\Phi_t(x_i,\cdot)]\right\|_{L^2}
 \le \sqrt d\,D_{k-1,2}(N)N^{-(k-1)/2}
       \|\Phi_t\|_{C^{(k-1)q+1}}.
 \tag{5.3}
\]

No independence between the root and the other measures is assumed. The
explicit order bound corresponding to (4.7) is

\[
 D_{n,p}(N)\le n!e^{Q(R_{np}+B)-1},\qquad n\ge1.
 \tag{5.4}
\]

Differentiating the original distinct-label sum gives
\(\nabla_{x_i}U_k=(k/N)V_{k-1}^{(i)}[\nabla_1\Phi(x_i,\cdot)]\): there are
exactly \(k\) choices for the rooted slot. Thus

\[
 dM_k=\frac{k\sqrt{2\nu}}N\sum_i
        V_{k-1}^{(i)}[\nabla_1\Phi_t(x_i,\cdot)]\cdot dW_i.
 \tag{5.5}
\]

Let \(B_k'=\sup_t\|\Phi_{k,t}\|_{C^{(k-1)q+1}}\). The Brownian covariance,
(5.3), and Cauchy--Schwarz give

\[
\begin{aligned}
 \mathbb E[M_k]_T
 &\le2\nu T d k^2 (B_k'D_{k-1,2}(N))^2N^{-k},\\
 \mathbb E\operatorname{TV}_{[0,T]}[M_k,M_\ell]
 &\le2\nu T d k\ell B_k'B_\ell'
       D_{k-1,2}(N)D_{\ell-1,2}(N)N^{-(k+\ell)/2}.
\end{aligned}
\tag{5.6}
\]

Multiplying either line by \(\sigma_N^2=N\min(\beta,1)\) replaces
\(\nu\) by \(\min(1,\beta^{-1})\) and gains the factor \(N\). These are
the precise all-temperature powers. In particular the scaled cross variation
with level one is of order \(N^{-(k-1)/2}\) with the stated constants. For
\(P=U_2/2\), divide its bracket by four and its cross brackets by two; this
recovers the TASK-010 normalization.

## 6. What the exact smooth generator permits one to count

For reference, the frozen recursion has upward operator

\[
 A_k^+\Phi=\operatorname{Sym}_{k+1}
       \sum_{a=1}^kK(x_a-x_{k+1})\cdot\nabla_a\Phi,
\]

internal operator \(C_k\Phi=\sum_{a\ne b}K(x_a-x_b)\cdot\nabla_a\Phi\),
and lower kernels

\[
\begin{aligned}
 Q_k\Phi&=\int\sum_{a=1}^{k-1}K(x_a-y)\cdot(\nabla_a-\nabla_y)
                         \Phi(x_1,\ldots,x_{k-1},y)\,d\mu(y),\\
 R_k\Phi&=\iint K(y-z)\cdot(\nabla_y-\nabla_z)
                         \Phi(x_1,\ldots,x_{k-2},y,z)\,d\mu(y)d\mu(z).
\end{aligned}
\tag{6.1}
\]

The coefficients in the drift are respectively \(1,1/N,k/N,\binom k2/N\).
At \(k=2\), the upward kernel for \(U_2\) is \(2C\Phi\) in the pair
notation of TASK-010. The factor is accounted for by \(P=U_2/2\).

For every integer \(m\ge0\), componentwise Leibniz expansion gives

\[
\begin{aligned}
 \|A_k^+\Phi\|_{C^m}&\le d k2^m\kappa_m\|\Phi\|_{C^{m+1}},\\
 \|C_k\Phi\|_{C^m}&\le d k(k-1)2^m\kappa_m\|\Phi\|_{C^{m+1}},\\
 \|Q_k\Phi\|_{C^m}&\le2d(k-1)2^m\kappa_m\|\Phi\|_{C^{m+1}},\\
 \|R_k\Phi\|_{C^m}&\le2d\kappa_0\|\Phi\|_{C^{m+1}}.
\end{aligned}
\tag{6.2}
\]

In the last line all differentiations are in the remaining slots, so none
fall on \(K(y-z)\). Integrating against the probability background introduces
no derivative of \(\mu\). Averaged symmetrization introduces no factorial.

Write \(\mathcal B_k(m)=\sup_t\|\Phi_{k,t}\|_{C^m}\). The following table
gives the integrated \(L^1\) estimates by applying (4.5). Terms with negative
indices are absent. The table also fixes every order-dependent coefficient.

| Exact drift term | Raw bound on its expected integrated absolute value |
|---|---|
| \(U_{k+1}[A_k^+\Phi_k]\) | \(T d k2^{(k+1)q}\kappa_{(k+1)q}\mathcal B_k((k+1)q+1)C_{k+1,1}(N)N^{-(k+1)/2}\) |
| \(N^{-1}U_k[C_k\Phi_k]\) | \(T d k(k-1)2^{kq}\kappa_{kq}\mathcal B_k(kq+1)C_{k,1}(N)N^{-(k+2)/2}\) |
| \(kN^{-1}U_{k-1}[Q_k\Phi_k]\) | \(2T d k(k-1)2^{(k-1)q}\kappa_{(k-1)q}\mathcal B_k((k-1)q+1)C_{k-1,1}(N)N^{-(k+1)/2}\) |
| \(\binom k2N^{-1}U_{k-2}[R_k\Phi_k]\) | \(T d k(k-1)\kappa_0\mathcal B_k((k-2)q+1)C_{k-2,1}(N)N^{-k/2}\) |

Multiplication by \(\sigma_N\) multiplies every row by
\(\min(\sqrt\beta,1)\sqrt N\). In particular the double contraction is of
the same raw order as \(U_k\); it is not an additional small factor in a
level-normalized hierarchy. The upward and single-lowering terms have one
extra factor \(N^{-1/2}\), and the internal \(1/N\) term has a full extra
factor \(N^{-1}\), conditional on their actual displayed kernel norms.
Every row vanishes at the linear fluctuation scale for fixed \(k\ge2\) and
uniform fixed-smooth norms. These are smooth iid statements, not singular
critical power counting.

## 7. Exact sufficient truncation and series criteria

These criteria state what quantitative information is still needed about
constructed correctors; they do not assume such information has been proved.
Let \(a_{N,k}\) be deterministic scalar coefficients, constant in time, and
let the smooth deterministic kernels \(\Phi_{N,k,t}\) be given. Put

\[
 E_{N,k}=C_{k,1}(N)\sup_t\|\Phi_{N,k,t}\|_{C^{kq}},\qquad
 J_{N,k}=D_{k-1,2}(N)\sup_t\|\Phi_{N,k,t}\|_{C^{(k-1)q+1}}.
 \tag{7.1}
\]

For a finite or countable set of orders \(I\), the endpoint/statistic sum
satisfies the sufficient bound

\[
 \sup_{t\le T}\mathbb E\left|
       \sigma_N\sum_{k\in I}a_{N,k}U_k[\Phi_{N,k,t}]\right|
 \le\min(\sqrt\beta,1)
     \sum_{k\in I}|a_{N,k}|E_{N,k}N^{-(k-1)/2}.
 \tag{7.2}
\]

Absolute summability of the right-hand side justifies the infinite sum in
\(L^1\); tails tending to zero uniformly in the chosen asymptotic regime
justify truncation there. Vanishing of the full right-hand side proves
negligibility at the linear scale. Applying the first row of Section 6 to the
last retained order gives the corresponding sufficient remainder condition
for a finite corrector truncation. The other three rows must be included
unless exact cancellations or retained lower terms are proved.

For martingales it is unsafe to sum only the individual brackets and omit
cross terms. Minkowski for Brownian integrands in the time-probability Hilbert
space, together with Itô isometry and (5.6), gives instead

\[
 \left\|\sigma_N\sum_{k\in I}a_{N,k}M_k(T)\right\|_{L^2}
 \le\sqrt{2Td\min(1,\beta^{-1})}
       \sum_{k\in I}|a_{N,k}|kJ_{N,k}N^{-(k-1)/2}.
 \tag{7.3}
\]

Absolute summability on the right defines a square-integrable Brownian
integral sum and controls every cross contribution. To pass an infinite
corrector identity, one must additionally sum the appropriate integrated
drift bounds in Section 6. None of these requirements can be replaced by a
formal power series in \(\lambda_N\).

### A concrete all-order smooth summability lemma

For fixed \(g,V,T\), suppose a deterministic symmetric kernel family obeys

\[
 \sup_{N,t}\|\Phi_{N,k,t}\|_{C^{kq+1}}\le A b^k\quad(k\ge2)
 \tag{7.4}
\]

for finite \(A,b\ge0\), and set \(a_{N,k}=1/k!\). This is an explicit
additional order-uniform hypothesis, not a conclusion about solutions of the
backward hierarchy. Let
\(c=Q(2BS\sqrt2+B)\). Equations (4.7) and (5.4) bound both the necessary
statistical order constant divided by \(k!\) and the martingale constant
\(kD_{k-1,2}/k!\) by \(e^{c\sqrt k}\). Indeed
\(2m(k)\le k+1\le2k\) and \(R_{2(k-1)}\le2BS\sqrt{2k}\).
For any \(\delta>0\),

\[
 e^{c\sqrt k}\le e^{c^2/(4\delta)}e^{\delta k}.
 \tag{7.5}
\]

If \(u=be^\delta/\sqrt N<1\), then for every \(K\ge1\), both sums on the
right of (7.2) and (7.3), without their displayed temperature prefactors, over
orders \(k>K\), are at most

\[
 A e^{c^2/(4\delta)}\sqrt N\,\frac{u^{K+1}}{1-u}.
 \tag{7.6}
\]

Thus these infinite statistical and martingale tails are well-defined and
vanish at least as \(N^{-K/2}\) for fixed \(K\) as \(N\to\infty\). This
proves a genuine bounded all-order summability statement. It does not prove
the hierarchy has the normalization \(1/k!\), or that its actual kernels
satisfy (7.4), or that its drift series is summable. Without those separately
verified facts it is only the stated sufficient model lemma.

## 8. Heat-regularized Riesz norms, with order dependence

For this section use precisely the positive-power Fourier sequence in the
frozen model, with \(0<s<d\):

\[
 \widehat g_\epsilon(n)=c_{d,s}|n|^{s-d}e^{-4\pi^2\epsilon|n|^2},\quad
 n\ne0,\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad
 \widehat g_\epsilon(0)=0.
 \tag{8.1}
\]

All statements here concern this explicit Fourier sequence and need no
singular stochastic theorem. The log model is excluded.

For \(0<\epsilon\le1\), define the finite explicit constants

\[
\begin{aligned}
 L_m^{\rm heat}
 &=c_{d,s}5^d(2\pi)^{-s}
   \max_{0\le j\le m}
   \frac{2^{(s-d+j+1)_+}\Gamma(1+(s+j+1)/2)}
        {1-2^{-(s+j+1)}}.
\end{aligned}
\tag{8.2}
\]

Then

\[
 \kappa_m(\epsilon)=\|K_\epsilon\|_{C^m}
 \le L_m^{\rm heat}\epsilon^{-(s+m+1)/2}.
 \tag{8.3}
\]

To check every order constant, a derivative of order \(j\) of a component of
\(K=-\nabla g\) is bounded by
\(c_{d,s}(2\pi)^{j+1}\sum_{n\ne0}|n|^{s-d+j+1}e^{-4\pi^2\epsilon|n|^2}\).
On the dyadic annulus \(2^\ell\le|n|<2^{\ell+1}\), the count is at most
\(5^d2^{d\ell}\), and the power is at most
\(2^{(s-d+j+1)_+}2^{(s-d+j+1)\ell}\). For \(p=s+j+1>0\),

\[
 \sum_{\ell\ge0}2^{p\ell}e^{-4\pi^2\epsilon4^\ell}
 \le\frac{p}{1-2^{-p}}\int_0^\infty r^{p-1}e^{-4\pi^2\epsilon r^2}dr
 =\frac{\Gamma(1+p/2)}{1-2^{-p}}
       (4\pi^2\epsilon)^{-p/2}.
 \tag{8.4}
\]

The comparison integral follows by integrating on
\([2^{\ell-1},2^\ell]\), where the exponential is at least its value at the
right endpoint. The powers of \(2\pi\) simplify to \((2\pi)^{-s}\).
Taking the maximum over derivatives and using \(\epsilon\le1\) proves
(8.3). Thus the gamma-factor dependence on derivative order is explicit.

The divergence of even the Lipschitz norm is real. Let
\(a=(s+2)/2\). For \(0<\epsilon\le1/4\), put \(R=\epsilon^{-1/2}\ge2\)
and restrict the Fourier sum for \(\operatorname{div}K_\epsilon(0)\) to
integer vectors whose every component belongs to \([R,2R]\). There are at
least \((R/2)^d\) of them, their norms lie between \(\sqrt d R\) and
\(2\sqrt d R\), and the heat factor is at least \(e^{-16\pi^2d}\). Therefore

\[
\begin{aligned}
 \kappa_1(\epsilon)&\ge d^{-1}\operatorname{div}K_\epsilon(0)
       \ge c_*\epsilon^{-a},\\
 c_*&=\frac{4\pi^2c_{d,s}}{d\,2^d}
       \min\{d^{(s-d+2)/2},(2\sqrt d)^{s-d+2}\}e^{-16\pi^2d}>0.
\end{aligned}
\tag{8.5}
\]

Positivity follows directly from
\(\operatorname{div}K_\epsilon(0)=4\pi^2c_{d,s}
 \sum_{n\ne0}|n|^{s-d+2}e^{-4\pi^2\epsilon|n|^2}\).
Thus the constants used in (2.1) cannot be claimed cutoff uniform, already
with constant background.

For \(T>0\), (8.3) yields the explicit upper estimate

\[
 S_\epsilon\le1+D\sqrt d\,Q L_q^{\rm heat}T
  \epsilon^{-(s+q+1)/2}
  \exp\{dTv_1+2dT L_1^{\rm heat}\epsilon^{-a}\}.
 \tag{8.6}
\]

Moreover the actual constant \(S_\epsilon\) in (2.1) grows at least
exponentially in a positive multiple of \(\epsilon^{-a}\) for sufficiently
small \(\epsilon\). Indeed (8.5) gives
\(L_\epsilon\ge2dc_*\epsilon^{-a}\); the Fourier mode \(n=e_1\) gives a
positive cutoff-independent lower bound on \(\mathcal K_\epsilon\) for
\(\epsilon\le1/4\); and \(h_L(T)\) is increasing in \(L\). Evaluating it at
\(2dc_*\epsilon^{-a}\) gives an exponential times a polynomial prefactor,
which can be absorbed into a smaller positive exponential for small cutoff.
This disproves uniformity of this particular coupling constant, not the
possibility of a sharper singular argument.

## 9. A precise sufficient slow-cutoff condition

For the regularized pair residual in TASK-010, let

\[
 A_\Phi(N)=\sup_{t\le T}\|\Phi^{N,\epsilon_N}_t\|_{C^{3q+1}},\qquad
 A_f(N)=\sup_{t\le T}\|f^{N,\epsilon_N}_t\|_{C^1}.
 \tag{9.1}
\]

These are actual deterministic solution norms, or proved bounds on them;
their uniformity is not inferred from a label such as critical coupling.
The following explicit condition is sufficient, uniformly for every positive
temperature sequence:

\[
 \epsilon_N\downarrow0,\qquad
 \epsilon_N^{-(s+2)/2}
       +\log(1+A_\Phi(N)+A_f(N))=o(\log N).
 \tag{9.2}
\]

Under (9.2), all four TASK-010 residual quantities, and the two lower drift
contractions, tend to zero for the **heat-regularized system** with kernel
\(g_{\epsilon_N}\) and its own mean-field solution.

**Proof.** For each fixed derivative order, (8.3) has logarithm bounded by
a constant plus a constant times \(\log(1/\epsilon_N)\), which is
\(o(\log N)\) under (9.2). Equation (8.6) similarly gives
\(\log S_{\epsilon_N}=o(\log N)\). The TASK-010 constants are finite sums
and products of these fixed-order kernel norms, powers at most three of its
coupling moment constant, and the test norms in (9.1). Hence each is
\(N^{o(1)}\). Its scaled endpoint, cubic, pair-bracket, and cross-bracket
bounds have respective powers \(N^{-1/2},N^{-1},N^{-1},N^{-1/2}\), with
temperature factors at most one; the lower contractions also have
\(N^{-1/2}\). Every product tends to zero. This proves the asserted joint
limit without assuming a cutoff-independent derivative bound.

The same proof applies to any **fixed finite set of higher orders**, provided
the logarithms of all the test norms required in Sections 4--6 are also
\(o(\log N)\). The constants may depend on those fixed orders. It does not
establish a growing-order or infinite-order cutoff limit.
For this assertion use the exact finite sums (4.4) and (5.2), which are
polynomials in \(S_\epsilon\) at fixed order. The coarser factorial/exponential
upper bounds (4.7) and (5.4) are not needed when the data constants grow with
the cutoff.

There are two useful concrete interpretations of (9.2):

1. If the required test norms grow at most polynomially in \(1/\epsilon\),
   then \(\epsilon_N=(\log N)^{-\gamma}\) suffices for any
   \(0<\gamma<2/(s+2)\).
2. More generally, if they are bounded by a polynomial times
   \(\exp(C\epsilon^{-h})\) for a finite \(h>0\), it suffices to take
   \(0<\gamma<1/\max\{(s+2)/2,h\}\).

Both statements are conditional on the indicated **proved norm bounds**.
The fixed-smooth backward estimate alone is not a proof of a polynomial
cutoff bound, and no such polynomial bound is claimed here.

There is also an existence statement requiring no specified growth rate.
Suppose for every fixed \(\epsilon>0\) the relevant finite family has a finite
norm envelope \(A(\epsilon)\), uniform over the particle numbers and
temperatures under consideration. This is the fixed-cutoff hypothesis used
in the bounded residual task; it must be supplied or proved for the selected
family. Choose \(\epsilon_m=1/m\) and increasing integer thresholds
\(N_m\to\infty\) so large that

\[
 \log N_m\ge m\,[m^{(s+2)/2}+\log(1+A(1/m))+1].
 \tag{9.3}
\]

Take \(\epsilon_N=1/m\) on \([N_m,N_{m+1})\). Its required expression in
(9.2), divided by \(\log N\), is at most \(1/m\). Hence it is a vanishing
cutoff for which the regularized residuals close. It may be very slow and is
not a rate for approximation of the singular model. A uniform finite
fixed-cutoff envelope is an explicit premise of this diagonal construction;
pointwise finite norms without that uniformity do not suffice.

For comparison, a polynomial cutoff \(\epsilon_N=N^{-\alpha}\),
\(\alpha>0\), makes this coupling constant grow like
\(\exp(cN^{\alpha(s+2)/2})\) for \(T>0\). The displayed smooth upper bounds
then do not establish a vanishing residual. This is a failure of this
estimate, not a counterexample to residual vanishing at that cutoff.

## 10. The exact remaining singular and critical obligations

The slow-cutoff statement compares no distinct models. Even for the linear
terminal observable, a singular fluctuation conclusion would require, for
example, a coupling or another comparison proving

\[
 \sigma_N\big\langle\varphi,
    (\eta_T^{\rm sing}-\mu_T^{\rm sing})
       -(\eta_T^{\epsilon_N}-\mu_T^{\epsilon_N})\big\rangle
           \longrightarrow0
 \tag{10.1}
\]

in a specified mode of convergence, with singular well-posedness and any
collision/regularization passage justified. If corrected observables or
martingale limits are compared, the corresponding kernel, centering,
endpoint, and bracket differences also need quantitative control. None of
these differences is bounded by (9.2). A cutoff slow enough for derivative
estimates may smooth precisely the microscopic scales needed for (10.1).

For full subcritical truncation, the actual remainder must satisfy the
appropriate weighted bound in Sections 6--7 for **every** sequence
\(\lambda_N\to0\), without a hidden polynomial gap. This could follow from
new singular kernel/law estimates supplying a proved order gain and a
fluctuation-scale comparison, but it does not follow by substituting
\(\lambda_N\) into a fixed-smooth coefficient.

At \(\lambda_N\to\lambda>0\), a finite truncation requires proving the
actual weighted residual tends to zero; an infinite retained hierarchy
requires order-uniform versions of the endpoint, integrated drift, and full
martingale criteria (7.2)--(7.3), together with identification and uniqueness
of its proposed limiting object. The same criteria allow a nonzero retained
limit instead of negligibility if that limit is separately constructed.
This report makes no finite-truncation or Gaussian-law assertion at singular
critical coupling.

The old energy-floor condition \(\beta_NN^{2s/d-1}\to0\), full
microscopic subcriticality \(\lambda_N\to0\), and microscopic criticality
\(\lambda_N\to\lambda\in(0,\infty)\) are unchanged and not conflated.
The bounded smooth estimates hold for all positive temperatures and contain
no singular regime decision by themselves.

## 11. Verification and handoff

The proof is self-contained apart from the explicitly identified, sealed
TASK-010 pathwise coupling inequalities and the already frozen smooth
generator normalization. No external quantitative theorem or private input
is required. The elementary all-moment symmetrization, partition identity,
rooted estimates, exact order constants, heat derivative bounds, and joint
cutoff criterion are proved in this report.

The applicable authority files and frozen model were byte-compared with the
already-read TASK-010 worktree and agree. The new task card and relevant
Round 001 all-order definitions were read. All earlier constraints and
law/centering distinctions remain in force. The root owns canonical state
integration and a fresh hostile review; no independent audit is claimed.

Created files: this memorandum,
`DISCOVERY_CODE/check_round002_powercount_exact.py`, and its recorded output
`DISCOVERY_CODE/round002_powercount_exact_output.json`.

Verification:

- `python3 scripts/verify_campaign.py`: PASS before construction and after the
  new output files were created; imported source note hash remains
  `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`.
- `python3 DISCOVERY_CODE/check_round002_powercount_exact.py`: PASS, 444 exact
  checks. These cover the full partition conversion through order seven
  (including orders exceeding particle number), rooted derivatives, cycle-type
  order constants and their independent Bell recurrence through order twelve,
  iid bias coefficients through order sixteen, finite Hilbert-vector sign
  moments through degree sixteen, and every temperature/bracket power for
  orders one through five. The configurations include repeated coordinates.
- Arithmetic is standard-library integer and `fractions.Fraction`, using
  Python 3.9.6. No random sampling or tolerance is used. These finite tests
  are `REPRODUCED / SELF_CHECKED` support for the analytic proofs, not an
  independent certificate of universal claims.
- `git diff --check`: PASS. Separate direct checks of the three new files
  confirm final newlines and absence of trailing whitespace.
- `git status --short`: only the three new outputs and the pre-existing
  TASK-013 card are untracked. The sealed TASK-010 hash was rechecked.

No immutable input, existing memorandum/audit, canonical ledger, or tracked
file is changed. No commit, push, installation, or remote mutation is
performed. The earlier TASK-010 report is unchanged. The final handoff uses
prose without mathematical LaTeX; this assigned mathematical deliverable is
Markdown. The report hash is supplied separately. This report is sealed at
handoff; later repairs require an identified addendum or superseding report.
