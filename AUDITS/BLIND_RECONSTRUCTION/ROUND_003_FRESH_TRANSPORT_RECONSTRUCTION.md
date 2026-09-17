# Round 003 fresh reconstruction: internal-pair transport

Date: 2026-09-17 UTC. Status: **SEALED FRESH RECONSTRUCTION**, independently derived from the permitted statements. This is neither a review of nor a verdict on any unseen constructor proof.

## Isolation and exact scope

The reconstruction was performed in the isolated worktree /private/tmp/hocf-r003-fresh-transport-20260917, branch codex/hocf-r003-fresh-transport, at base commit 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2. No constructor proof, prior review, diffusion note, root TeX, other worktree, or private manuscript was opened. There was no delegation. No canonical root file was edited and no commit, push, merge, dependency installation, or configuration change was performed.

The two new mathematical inputs were copied unchanged from the root:

- THEOREMS/THM-017_INTERNAL_PAIR_TRANSPORT_MODEL.md, SHA-256 2c95e74ea8874e8d624d23a8ce2dfa9dfdca4eda9d796c9e403dda5277811c79.
- THEOREMS/THM-015_IID_PAIR_SECOND_MOMENT.md, SHA-256 c61e042599bd18993b6b760f22bde9d9044675f206fb42ea3418197be36db150.

The administrative read set was AGENTS.md, README_FIRST.md, MODEL_ORCHESTRATION.md, and TASKS/ACTIVE/ROUND_001_MODEL.md at the stated base. The bounded isolation instruction took precedence over the broad campaign reading list. The frozen task supplied the torus normalization, ordered distinct-label statistic, denominator, and centering. Input hashes are recorded in ROUND_003_FRESH_TRANSPORT_INPUT_SHA256SUMS.txt.

The THM-017 statement refers to a characteristic class and cutoff defined in an unseen proof. This report makes both choices explicit. A later comparison must check those definitions; this report makes no assertion about their unseen wording. The iid moment formula needed below is proved here, rather than assumed from the candidate status of THM-015. No heat-cutoff or Fourier claim from THM-015 is used.

**Primary assertion reconstructed.** For the parameters and class specified below, the displayed terminal-value transport equation has exactly the displayed solution; its local norm has the stated three regimes; the explicitly defined periodic diagnostic has the asserted iid scaled second-moment upper bounds, uniformly over deterministic backward times.

**Logical negation.** There are admissible parameters and either a second solution in the specified characteristic class, a point where the formula fails the terminal-value equation, or a violation of one of the explicit norm comparisons below; alternatively, for some fixed permitted \(d,s,A,M,\chi,T\), no finite constant bounds the endpoint by the displayed rate for all \(N\geq2\), \(\beta_N>0\), density-bounded iid laws, and deterministic \(\tau\in[0,T]\).

Everything below concerns the punctured, zero-diffusion internal-pair model. It supplies no diffusion estimate, full-operator identity, interacting-law bound, actual backward-corrector estimate, or singular dynamical passage.

## 1. Parameters and the characteristic class

Fix an integer \(d\geq1\), \(0<s<d\), an integer \(N\geq2\), \(0\leq T<\infty\), and a real symmetric \(d\)-by-\(d\) matrix \(A\). Write
\[
p=s+2,\qquad \alpha=\frac2p,\qquad c=2sp,\qquad
a(\theta)=\theta^{\mathsf T}A\theta,\qquad \tau=T-t .
\]
The spatial domain is \(\mathbb R^d\setminus\{0\}\). In particular, no equation or boundary value is imposed at the collision point.

For \(z=r\theta\ne0\), \(u\in[t,T]\), define
\[
R_{t,r}(u)=\left(r^p+\frac cN(u-t)\right)^{1/p},
\qquad Z_{t,z}(u)=R_{t,r}(u)\theta .
\]
The reconstructed solution class consists of finite real-valued functions \(\Phi\) on \([0,T]\times(\mathbb R^d\setminus\{0\})\) such that, for every \((t,z)\), the map \(u\mapsto\Phi(u,Z_{t,z}(u))\) is absolutely continuous on \([t,T]\), satisfies
\[
\frac{d}{du}\Phi(u,Z_{t,z}(u))
   =-s\,a(\theta)R_{t,r}(u)^{-s}
\quad\text{for almost every }u,
\]
and has terminal value \(\Phi(T,w)=0\) for every \(w\ne0\). This is a pointwise characteristic class, not merely an equivalence class modulo spacetime null sets.

The radial flow solves
\[
\frac{dR}{du}=\frac{2s}{N}R^{-s-1},\qquad
\frac{d}{du}R^p=\frac cN,\qquad
\frac{d}{du}R^2=\frac{4s}{N}R^{-s}.
\]
It is strictly outward for positive elapsed time. Starting at a nonzero point, it neither hits the origin nor explodes before any finite terminal time. Thus the terminal condition determines every forward characteristic without an additional collision boundary condition.

## 2. Construction, uniqueness, and independent substitution

Integration along the characteristic gives necessarily
\[
\begin{aligned}
\Phi_N(t,r\theta)
 &=s\,a(\theta)\int_t^T R_{t,r}(u)^{-s}\,du\\
 &=\frac N4 a(\theta)
   \left[\left(r^p+\frac{c\tau}{N}\right)^{2/p}-r^2\right].
\end{aligned}                                                    \tag{2.1}
\]
The integral is finite because \(R_{t,r}(u)\geq r>0\). Formula (2.1) has the stated terminal value and belongs to the characteristic class, by the same calculation. Conversely, the fundamental theorem for absolutely continuous functions forces (2.1) for every member of the class. This proves existence and uniqueness in that class, with no growth condition at infinity required.

The solution is smooth in \(z\ne0\), and is continuously differentiable in \(t\) with one-sided derivatives at the temporal endpoints. An independent substitution checks the sign and coefficient. Put \(R=(r^p+c\tau/N)^{1/p}\). Direct differentiation gives
\[
\partial_t\Phi_N=-s\,a(\theta)R^{-s},\qquad
\partial_r\Phi_N=\frac N2a(\theta)
       \left[r^{s+1}R^{-s}-r\right].
\]
Consequently,
\[
\partial_t\Phi_N+\frac{2s}{N}r^{-s-1}\partial_r\Phi_N
=-s\,a(\theta)R^{-s}
 +s\,a(\theta)(R^{-s}-r^{-s})
=-s\,a(\theta)r^{-s}.                                            \tag{2.2}
\]
Since the vector field is radial, its action on \(\Phi_N\) is exactly the radial derivative appearing here; it does not differentiate \(a(\theta)\).

If \(T=0\), only the terminal value is present and the solution is identically zero. All subsequent expressions involving \(\ell>0\) apply to \(\tau>0\); at \(\tau=0\) the kernel and every norm are zero.

## 3. Explicit near and far bounds, including time dependence

For \(\tau>0\), set
\[
\ell=\left(\frac{c\tau}{N}\right)^{1/p},\qquad
F(u)=(1+u^p)^\alpha-u^2,\qquad m_s=2^\alpha-1>0 .
\]
Then
\[
\Phi_N(t,r\theta)=\frac N4 a(\theta)\ell^2 F(r/\ell).              \tag{3.1}
\]
For \(u>0\),
\[
F'(u)=2u\left[\left(\frac{u^p}{1+u^p}\right)^{s/p}-1\right]<0,
\quad F(0)=1,\quad F(1)=m_s .
\]
For \(r\leq\ell\), this gives the explicit two-sided bounds
\[
\frac{m_sN}{4}|a(\theta)|\ell^2
 \leq|\Phi_N(t,r\theta)|
 \leq\frac N4|a(\theta)|\ell^2 .                                \tag{3.2}
\]
The inequalities remain valid when \(a(\theta)=0\), when all three expressions are zero.

The exact integral identity
\[
(r^p+\ell^p)^\alpha-r^2
   =\alpha\int_0^{\ell^p}(r^p+v)^{-s/p}\,dv                     \tag{3.3}
\]
implies, for \(r\geq\ell\),
\[
s\,2^{-s/p}\tau|a(\theta)|r^{-s}
\leq|\Phi_N(t,r\theta)|
\leq s\tau|a(\theta)|r^{-s}.                                   \tag{3.4}
\]
The upper bound on the right holds for every \(r>0\). Monotonicity of \(F\) also gives, for every \(r>0\),
\[
|\Phi_N(t,r\theta)|
 \leq |a(\theta)|
       \min\left\{\frac14c^{2/p}N^{s/p}\tau^{2/p},
                    s\tau r^{-s}\right\}.                     \tag{3.5}
\]
The two regimes meet at the exact radius \(\ell\); the finite-\(N\) relation used in (3.4) is \(N\alpha\ell^p/4=s\tau\).

The asymptotic constants are also explicit:
\[
F(u)\longrightarrow1\quad(u\downarrow0),\qquad
u^sF(u)\longrightarrow\alpha\quad(u\to\infty).
\]
The second limit follows by dividing \((1+x)^\alpha-1\) by \(x\) at \(x=u^{-p}\downarrow0\). Thus the far expression is asymptotic to \(s\tau a(\theta)r^{-s}\) when \(r/\ell\to\infty\). No uniform-in-\(N\) claim is inferred from a bound whose explicit factor is \(N^{s/p}\).

## 4. Collision, terminal time, and the angular norm

At every fixed \(\tau>0\),
\[
\lim_{r\downarrow0}\Phi_N(T-\tau,r\theta)
       =\frac N4\ell^2a(\theta).                               \tag{4.1}
\]
There is a common collision limit if and only if \(A=a_0I\) for some real \(a_0\). Indeed, a symmetric matrix whose quadratic form is constant on the unit sphere has all eigenvalues equal, and the converse is immediate. For \(d=1\), every symmetric matrix is scalar. For \(d\geq2\), a nonscalar symmetric matrix has two unit eigenvectors with different limits in (4.1). It therefore has no continuous coincidence extension at positive backward time. Assigning any value at the origin for a measurable kernel does not repair this failure.

For a scalar matrix, (4.1) defines a continuous spatial extension at positive backward time. No assertion of a smooth extension of arbitrary order is needed or made. At \(\tau=0\), the punctured solution vanishes. For each fixed \(N\), (3.5) implies
\[
\sup_{z\ne0}|\Phi_N(T-\tau,z)|
 \leq\frac14\|A\|_{\mathrm{op}}c^{2/p}N^{s/p}\tau^{2/p}
 \longrightarrow0 .
\]
In particular the terminal collision corner has limit zero at fixed \(N\), even when the positive-time collision limits depend on direction.

With ordinary surface measure on \(S^{d-1}\), let
\[
M_A=\int_{S^{d-1}}a(\theta)^2\,d\theta
 =\frac{|S^{d-1}|}{d(d+2)}
       \left[(\operatorname{tr}A)^2+2\operatorname{tr}(A^2)\right]. \tag{4.2}
\]
For completeness, diagonalize \(A\). For uniform \(\theta\) on the sphere in \(d\geq2\), sign changes eliminate odd products. Rotation in the first two coordinates yields
\(\mathbb E\theta_1^4=3\mathbb E\theta_1^2\theta_2^2\).
Taking the expectation of \((\sum_i\theta_i^2)^2=1\) gives
\(\mathbb E\theta_1^4=3/[d(d+2)]\) and
\(\mathbb E\theta_1^2\theta_2^2=1/[d(d+2)]\).
Expansion of the diagonal quadratic form proves (4.2). For \(d=1\), the two points of \(S^0\) give \(M_A=2A_{11}^2\), which agrees with the same formula.

Thus \(M_A>0\) for every nonzero symmetric \(A\), including nonzero trace-free matrices. Angular averaging of the signed quadratic form cannot replace its squared angular norm.

## 5. Exact local norm and two-sided orders

For any fixed \(R>0\) and \(\tau>0\), polar coordinates give the exact equality
\[
\|\Phi_N(T-\tau,\cdot)\|_{L^2(B_R)}^2
 =\frac{N^2}{16}M_A\,\ell^{d+4}J_{d,s}(R/\ell),\qquad
J_{d,s}(L)=\int_0^L F(u)^2u^{d-1}\,du .                         \tag{5.1}
\]
The point \(0\) is immaterial to this integral. The kernel is locally square integrable for every permitted \(s\), since it is bounded at each fixed \(N,\tau>0\), although generally discontinuous at the origin.

For \(0<L\leq1\), there are explicit bounds
\[
\frac{m_s^2}{d}L^d\leq J_{d,s}(L)\leq\frac1d L^d .              \tag{5.2}
\]
For \(L\geq1\), (3.4) in scaled variables yields
\[
\frac{m_s^2}{d}
 +\alpha^2 2^{-2s/p}\int_1^L u^{d-2s-1}\,du
\leq J_{d,s}(L)
\leq\frac1d+\alpha^2\int_1^L u^{d-2s-1}\,du .                  \tag{5.3}
\]
These bounds cover every \(N,\tau,R\), including \(R<\ell\). In the regime \(R\geq\ell\) they imply the following two-sided orders for \(A\ne0\), with positive comparison constants depending only on \(d,s\):
\[
\|\Phi_N\|_{L^2(B_R)}^2\asymp_{d,s}
\begin{cases}
 M_A\,\tau^2 R^{d-2s}, & 2s<d,\\
 M_A\,\tau^2[1+\log(R/\ell)], & 2s=d,\\
 M_A\,N^{(2s-d)/p}\tau^{(d+4)/p}, & 2s>d.
\end{cases}                                                   \tag{5.4}
\]
For \(R\leq\ell\), the corresponding two-sided expression is
\(M_A N^2\ell^4R^d\), with the explicit factors in (5.1)-(5.2).
For \(A=0\), every norm is zero; no positive lower comparison is asserted.

For \(A\ne0\), there are more precise asymptotics as \(R/\ell\to\infty\). Since \(u^sF(u)\to\alpha\),
\[
\|\Phi_N\|_{L^2(B_R)}^2\sim
\begin{cases}
\displaystyle\frac{s^2M_A}{d-2s}\tau^2R^{d-2s}, & 2s<d,\\[5pt]
\displaystyle s^2M_A\tau^2\log(R/\ell), & 2s=d,\\[5pt]
\displaystyle\frac{M_A}{16}c^{(d+4)/p}J_{d,s}(\infty)
             N^{(2s-d)/p}\tau^{(d+4)/p}, & 2s>d .
\end{cases}                                                   \tag{5.5}
\]
In the last case \(0<J_{d,s}(\infty)<\infty\), by (5.2)-(5.3). The first two asymptotics follow by comparing the tail integrand with \(\alpha^2u^{d-2s-1}\); the last follows by monotone convergence of the positive defining integral. These arguments justify the displayed ratios, not only their formal powers.

For \(A\ne0\) and fixed \(R>0,\tau>0\), the squared-norm orders as \(N\to\infty\) are, respectively, \(1\), \(\log N\), and \(N^{(2s-d)/(s+2)}\). The norm itself has the square roots of these powers. At the critical exponent, the exact leading coefficient of \(\log N\) is \(s^2M_A\tau^2/p\).

For the endpoint below, the following upper bounds valid for all \(\tau>0\) are useful:
\[
\|\Phi_N\|_{L^2(B_R)}^2\leq
\begin{cases}
\displaystyle\frac{s^2M_A}{d-2s}\tau^2R^{d-2s}, & 2s<d,\\[5pt]
\displaystyle s^2M_A\tau^2\left[\frac{p^2}{4d}
                                    +\log_+(R/\ell)\right], & 2s=d,\\[5pt]
\displaystyle\frac{M_A}{16}c^{(d+4)/p}
 \left(\frac1d+\frac{\alpha^2}{2s-d}\right)
 N^{(2s-d)/p}\tau^{(d+4)/p}, & 2s>d .
\end{cases}                                                   \tag{5.6}
\]
Here \(\log_+x=\max\{\log x,0\}\). The first bound integrates the global far upper bound. For the second, split at \(\min\{R,\ell\}\), use the constant near bound and \(s\tau r^{-s}\) outside, and use \(N^2\ell^{d+4}=c^2\tau^2\) when \(d=2s\). If \(R<\ell\), the near integral is bounded by its value at \(R=\ell\). For the third, use \(J_{d,s}(R/\ell)\leq J_{d,s}(\infty)\leq 1/d+\alpha^2/(2s-d)\). Thus no large-\(N\) restriction is hidden in (5.6).

## 6. A precise fixed periodic cutoff

This reconstruction chooses \(r_0=1/8\), \(R_0=1/4\), and
\[
\eta(v)=
\begin{cases}e^{-1/v},&v>0,\\0,&v\leq0,\end{cases}
\qquad
\chi(r)=\frac{\eta(R_0-r)}
                {\eta(R_0-r)+\eta(r-r_0)}\quad(r\geq0).
\]
The denominator is everywhere positive. The function \(\chi\) is smooth, \(0\leq\chi\leq1\), equals one on \([0,r_0]\), and is zero on \([R_0,\infty)\). It is constant near zero, so its radial realization is smooth at zero.

On the mass-one unit torus, let \(z\) be the representative of \(x-y\) in \([-1/2,1/2)^d\), and define
\[
k_{N,\tau}(z)=
\begin{cases}
\chi(|z|)\Phi_N(T-\tau,z),&z\ne0,\\
0,&z=0,
\end{cases}
\qquad H_{N,\tau}(x,y)=k_{N,\tau}(x-y).                         \tag{6.1}
\]
Set \(k_{N,0}=0\). Because the support lies in the closed radius-\(1/4\) ball, strictly inside the injectivity radius, the periodic definition is independent of representatives wherever it is nonzero. It is real, measurable, and even in \(z\); hence \(H\) is symmetric. For a nonscalar \(A\), the selected diagonal value is only a measurable convention.

The exact Lebesgue kernel norm is
\[
\|k_{N,\tau}\|_2^2
 =\frac{N^2M_A}{16}\int_0^{R_0}
  \chi(r)^2\left[(r^p+\ell^p)^\alpha-r^2\right]^2 r^{d-1}\,dr ,
\]
and it lies between the local squared norms on \(B_{r_0}\) and \(B_{R_0}\). For \(A\ne0\), it has the same three powers in \(N\) at fixed positive \(\tau\). More explicitly, in the integrable case \(2s<d\), dominated convergence using (3.4) gives
\[
\|k_{N,\tau}\|_2^2\longrightarrow
s^2M_A\tau^2\int_0^{R_0}\chi(r)^2r^{d-2s-1}\,dr .
\]
For \(2s=d\), the lower and upper local bounds in (5.5) have the same leading term \(s^2M_A\tau^2\log(1/\ell)\). For \(2s>d\), they have the same leading constant, the last line of (5.5). Squeezing proves those cutoff asymptotics as well.

No transport equation is asserted for \(k_{N,\tau}\): differentiating the cutoff would produce an annular source. Its sole role here is a separately defined periodic iid diagnostic.

## 7. Iid prerequisite reconstructed, with exact finite-\(N\) factors

Let \(X_1,\ldots,X_N\) be iid with probability law \(\mu\). For any real symmetric \(\Psi\in L^2(\mu\otimes\mu)\), define
\[
m=\iint\Psi\,d\mu\,d\mu,\qquad
h(x)=\int\Psi(x,y)\,d\mu(y)-m,\qquad
Q(x,y)=\Psi(x,y)-m-h(x)-h(y).
\]
Then \(\int h\,d\mu=0\), \(\int Q(x,y)\,d\mu(y)=0\) for almost every \(x\), and orthogonality gives
\[
\|\Psi\|_2^2=m^2+2\|h\|_2^2+\|Q\|_2^2.                         \tag{7.1}
\]
The campaign convention, retaining ordered distinct labels and the \(N^2\) denominator, is
\[
P_N[\Psi]=\frac1{2N^2}\sum_{i\ne j}\Psi(X_i,X_j)
-\frac1N\sum_i\int\Psi(X_i,y)\,d\mu(y)+\frac m2 .
\]
Counting occurrences of each \(h(X_i)\) yields the exact random-variable identity
\[
P_N[\Psi]=-\frac m{2N}
-\frac1{N^2}\sum_i h(X_i)
+\frac1{2N^2}\sum_{i\ne j}Q(X_i,X_j).                           \tag{7.2}
\]
Every term is defined almost surely from the \(L^2\) kernel. No repeated-label evaluation appears.

Distinct \(h(X_i)\) terms are orthogonal by independence and centering. Two \(Q\) terms on distinct unordered pairs have zero covariance: disjoint pairs are independent and centered; pairs sharing one label have zero covariance after conditioning on that label. The linear sum is also orthogonal to the \(Q\) sum by the same conditional-centering argument. Each ordered \(Q\) pair has only two potentially nonzero matching partners in the ordered double sum: itself and its reversal. Thus
\[
\mathbb EP_N=-\frac m{2N},\qquad
\mathbb EP_N^2=\frac{m^2}{4N^2}+\frac{\|h\|_2^2}{N^3}
                  +\frac{N-1}{2N^3}\|Q\|_2^2.                 \tag{7.3}
\]
Subtracting this expression from the proposed upper bound gives exactly
\[
\frac{N-1}{2N^3}\|\Psi\|_2^2-\mathbb EP_N^2
=\frac{N-2}{4N^3}m^2+\frac{N-2}{N^3}\|h\|_2^2\geq0.           \tag{7.4}
\]
At \(N=2\) equality holds for every kernel. For \(N>2\), equality holds exactly when \(m=0\) and \(h=0\), including every nonzero canonical kernel. This proves the portion of THM-015 used here, including the residual deterministic bias. The heat-kernel part of that statement was neither used nor audited.

## 8. Periodic iid endpoint, uniformly over deterministic time

For each \(N\), let \(\mu_N(dx)=\rho_N(x)\,dx\) be a probability measure on the unit torus with \(0\leq\rho_N\leq M<\infty\) almost everywhere, with the same bound \(M\) for all \(N\). Let \(X_1,\ldots,X_N\) be iid with this law, and use this same \(\mu_N\) in the centering of \(P_N\). No positive lower bound or smoothness of the density is needed.

For an arbitrary translation-invariant measurable kernel \(k\),
\[
\iint |k(x-y)|^2\rho_N(x)\rho_N(y)\,dx\,dy
=\int |k(z)|^2
       \left[\int\rho_N(y+z)\rho_N(y)\,dy\right]dz
\leq M\|k\|_{L^2(dx)}^2.                                      \tag{8.1}
\]
This uses only the density upper bound and unit total mass. Since the law is atomless, the convention at the spatial diagonal in (6.1) has no effect on either the iid statistic almost surely or its \(L^2(\mu_N^2)\) kernel class.

For any sequence \(\beta_N>0\), set
\(b_N=\min\{\beta_N,1\}\) and \(\sigma_N=\sqrt{Nb_N}\).
The exact finite-\(N\) implication of (7.3)-(7.4) is
\[
\begin{aligned}
\mathbb E|\sigma_NP_N[H_{N,\tau}]|^2
 &=b_N\left[\frac{m_{N,\tau}^2}{4N}
   +\frac{\|h_{N,\tau}\|_2^2}{N^2}
   +\frac{N-1}{2N^2}\|Q_{N,\tau}\|_2^2\right]\\
 &\leq\frac{b_N(N-1)}{2N^2}
                     \|H_{N,\tau}\|_{L^2(\mu_N^2)}^2\\
 &\leq\frac{M b_N(N-1)}{2N^2}
               \|\Phi_N(T-\tau,\cdot)\|_{L^2(B_{R_0})}^2 .
\end{aligned}                                                  \tag{8.2}
\]
Inserting (5.6) preserves all time factors. In particular, with \(q=(2s-d)/p\) and \(\gamma=(d+4)/p\) used only when \(2s>d\),
\[
\mathbb E|\sigma_NP_N[H_{N,\tau}]|^2\leq
\frac{M b_N(N-1)}{2N^2}
\begin{cases}
\displaystyle\frac{s^2M_A}{d-2s}\tau^2R_0^{d-2s}, & 2s<d,\\[5pt]
\displaystyle s^2M_A\tau^2\left[\frac{p^2}{4d}
                              +\log_+(R_0/\ell)\right], & 2s=d,\\[5pt]
\displaystyle\frac{M_A}{16}c^\gamma
  \left(\frac1d+\frac{\alpha^2}{2s-d}\right)N^q\tau^\gamma,
       & 2s>d .
\end{cases}                                                    \tag{8.3}
\]
At \(\tau=0\) the entire left side is zero, and the right side is interpreted by its continuous zero limit.

For clarity at the logarithmic threshold,
\[
\log_+(R_0/\ell)
\leq\frac1p\left[\log N+\log_+(R_0^p/c)+\log_+(1/\tau)\right],
\qquad
\sup_{\tau>0}\tau^2\log_+(1/\tau)=\frac1{2e}.
\]
Therefore, for every fixed finite \(T\), (8.3) gives
\[
\sup_{0\leq\tau\leq T}
\mathbb E|\sigma_NP_N[H_{N,\tau}]|^2
\leq C_{d,s,A,M,\chi,T}\,b_N
\begin{cases}
N^{-1},&2s<d,\\
(1+\log N)/N,&2s=d,\\
N^{-(d+2-s)/(s+2)},&2s>d .
\end{cases}                                                    \tag{8.4}
\]
The constant is finite and independent of \(N,\beta_N,\tau\). It can be zero when \(A=0\) or \(T=0\). In the last case the exponent follows from \(q-1=-(d+2-s)/(s+2)\). It is strictly negative because \(s<d\). As \(b_N\leq1\), every right side tends to zero.

The supremum in (8.4) is outside the expectation. This proves \(L^2\) convergence for every deterministic sequence of backward times in \([0,T]\), including sequences tending to zero. It does not prove an expected supremum bound or any assertion for a time selected from the particle configuration. The positive temperature appears solely in the scale \(\sigma_N\); the transport equation itself has zero diffusion.

## 9. Falsification checks and reproducibility

The direct PDE substitution (2.2) is independent of the characteristic integration used to construct (2.1). It tests the sign of the terminal integral and both finite-\(N\) coefficients. The norm calculation separately tests the near-to-far transition and recovers \(s\tau r^{-s}\) in the far region. The trace-free matrix test in (4.2) prevents an invalid cancellation of the squared angular norm. A nonscalar diagonal matrix explicitly disproves any attempted continuous collision extension. A constant iid kernel tests the residual mean \(-m/(2N)\), which would be missed by treating the deleted statistic as an exactly centered canonical statistic.

The accompanying standard-library-only checker ROUND_003_FRESH_TRANSPORT_CHECK.py independently enumerates iid laws with three atoms and rational weights for \(N=2,3,4\). It verifies (7.2)-(7.4) exactly for constant, additive, canonical, and mixed symmetric kernels, including the sharp \(N=2\) equality. It also evaluates the displayed candidate with exact rational automatic differentiation at integer \(s=1,2,3\), \(N=2,3,7\), two initial/terminal radius pairs, and three angular coefficients, and checks the resulting transport equation. These checks support the proof and are not its replacement.

Verification command, run from the isolated worktree:

    python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_TRANSPORT_CHECK.py

Outcome: PASS; 12 exact iid moment cases and 54 exact transport substitutions, with no external dependencies. The JSON output is ROUND_003_FRESH_TRANSPORT_CHECK_OUTPUT.json. Input checksum verification also passed for all six listed files. An ancillary delimiter checker initially mistook array line-break spacing for display openings; the corrected check of whole-line display delimiters passed, as did the inline-delimiter and whitespace checks. This was a checker defect, with no mathematical change required. The final output manifest seals the report, checker, test result, and input manifest. No TeX or manuscript source was changed, so no manuscript build was invoked.

## 10. Reconstruction conclusion and comparison boundary

The proposed formula, its natural pointwise characteristic uniqueness, the exact angular norm, the two-sided local norm orders, and the stated iid endpoint powers have been reconstructed and proved here. All finite-\(N\), time, density, and temperature factors used for the endpoint are visible in (8.2)-(8.3). The iid prerequisite is independently proved rather than left conditional.

The only definition-level comparison still needed is with the unseen characteristic class and cutoff referenced by the submitted statement. This report used the explicit class in Section 1 and explicit cutoff in Section 6. No verdict is issued on an unseen proof or its comparison estimate. In particular, the actual singular backward corrector, the full generator, diffusion, interacting laws, periodic-force remainders, cutoff annular sources, and any proposed full-corrector comparison remain outside this result.
