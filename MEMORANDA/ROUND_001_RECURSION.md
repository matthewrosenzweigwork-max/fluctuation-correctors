# Round 001: exact all-order deleted-label recursion

- Task: `TASK-004`; claim: the algebraic part of `THM-001` / `PO-003`.
- Date: 2026-09-17 UTC.
- Frozen input: `TASKS/ACTIVE/ROUND_001_MODEL.md`, version 1.0.
- Baseline: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Mathematical status: `EXACT_IDENTITY` under the fixed smooth model stated below.
- Audit status: `SELF_CHECKED`; no independent audit of the general proof is claimed here.
- Computation status: `REPRODUCED` exact-arithmetic discovery tests, not an independent certificate.
- Imported mathematical inputs: none beyond the frozen model, finite sums, torus integration by parts and smooth Itô calculus. No singular source theorem is used.
- M2 status: `OPEN`. The exact recursion is obtained; the critical power-counting theorem is not.

The main result is equation (R1). It has one upward level, an internal interaction at the same level, and two explicitly specified lower levels. There is no separate Brownian lowering term in the drift of this particular deleted-label statistic. Brownian shared-label contractions occur in its quadratic and cross variations; their complete partial-matching expansion is (R5).

## 1. Assertion, model and conventions

**Primary assertion.** For every finite integer N at least two, every positive beta, every fixed smooth even periodic interaction g, every smooth periodic V, every smooth strictly positive probability solution mu of the frozen mean-field equation, every integer k at least one, and every deterministic symmetric kernel Phi that is C1 in time and smooth in its k spatial variables, (R1), (R3) and (R5) hold on the stated finite time interval. No exchangeability or preparation assumption is needed.

**Exact negation.** One permitted choice of these data violates at least one identity, with a nonzero difference in its drift, martingale integrand or bracket. A nonzero exact Laurent coefficient in the tests below is therefore a valid falsifier of the tested instance.

Write nu=1/beta, K=-grad g, b=-grad V, q=K*mu and u=b+q. The particle dynamics and mean-field equation are

\[
 dx_i=\left(b(x_i)+\frac1N\sum_{j\ne i}K(x_i-x_j)\right)dt
       +\sqrt{2\nu}\,dW_i,
 \qquad
 \partial_t\mu=-\operatorname{div}(u\mu)+\nu\Delta\mu.
\]

The torus has volume one. All labels in each empirical tuple are distinct, all tuples are ordered, and all denominators are powers of N. Coordinate coincidences between different labels are allowed. Empty sums, products and zero-body statistics have their literal finite-set meanings. In particular, formulas remain valid when k>N: some factorial sums vanish, but the centered U_k need not vanish.

For a finite slot set A define the empirical factorial measure

\[
 D_A=N^{-|A|}\sum_{\iota:A\hookrightarrow[N]}
        \bigotimes_{a\in A}\delta_{x_{\iota(a)}},\qquad D_\varnothing=1.
\]

Let S=[k], and use products of measures on disjoint slot sets. Define

\[
 U_S=\sum_{A\subseteq S}(-1)^{|S|-|A|}D_A\mu^{S\setminus A}.
 \tag{R0}
\]

For a kernel H on S, U_S[H] means its integral against this signed measure. By symmetry it agrees with the frozen U_k notation. This is algebraic mean-field centering, not centering by the exact expectation and not a probabilistic cumulant.

## 2. Explicit operators and the recursion

The full tensorized linearized operator is

\[
 \mathcal L_k\Phi
 =\sum_{a=1}^k
   \left(u(x_a)\cdot\nabla_a\Phi+\nu\Delta_a\Phi
               +\mathcal R_a\Phi\right),
\]

where the background response is

\[
 (\mathcal R_a\Phi)(x_1,\ldots,x_k)
 =\int K(y-x_a)\cdot\nabla_y
       \Phi(x_1,\ldots,x_{a-1},y,x_{a+1},\ldots,x_k)\,\mu(dy).
\]

For a pair of slots set

\[
 B_{ab}\Phi=K(x_a-x_b)\cdot(\nabla_a-\nabla_b)\Phi,
 \qquad
 C_k\Phi=\sum_{1\le a<b\le k}B_{ab}\Phi.
\]

Oddness of K gives the exact equality

\[
 C_k\Phi=\sum_{a\ne b}K(x_a-x_b)\cdot\nabla_a\Phi.
\]

The upward operator uses **averaged** symmetrization over all k+1 slots:

\[
 A_k^+\Phi
 =\operatorname{Sym}_{k+1}
   \left[\sum_{a=1}^kK(x_a-x_{k+1})\cdot\nabla_a\Phi(x_1,\ldots,x_k)\right].
\]

The two contractions are

\[
 \begin{aligned}
 Q_k\Phi(x_1,\ldots,x_{k-1})
 &=\int\sum_{a=1}^{k-1}
   K(x_a-y)\cdot(\nabla_a-\nabla_y)
   \Phi(x_1,\ldots,x_{k-1},y)\,\mu(dy),\\
 R_k\Phi(x_1,\ldots,x_{k-2})
 &=\iint K(y-z)\cdot(\nabla_y-\nabla_z)
   \Phi(x_1,\ldots,x_{k-2},y,z)\,\mu(dy)\mu(dz).
 \end{aligned}
\]

They are symmetric in the remaining variables. Their mu factors are evaluated at the same time as the drift; no additional time differentiation of Q_k or R_k belongs in (R1). Define all contraction terms as zero when their indicated pair of slots does not exist.

The exact semimartingale identity is

\[
\boxed{
\begin{aligned}
 dU_k[\Phi]
 =\Big\{&U_k[(\partial_t+\mathcal L_k+N^{-1}C_k)\Phi]
          +U_{k+1}[A_k^+\Phi]\\
        &+\frac{k}{N}U_{k-1}[Q_k\Phi]
          +\frac{\binom{k}{2}}{N}U_{k-2}[R_k\Phi]\Big\}\,dt+dM_k[\Phi].
\end{aligned}}
\tag{R1}
\]

Thus there are no hidden factors (N-k), (N)_k or 1/k! in these operators. They would change under other normalization conventions.

## 3. Finite-subset proof

The proof starts with distinct particle labels, before any use of empirical full products.

### 3.1 Direct differentiation of one subset

For A contained in S write F_A[Phi]=D_A mu^(S minus A)[Phi]. Smooth Itô calculus and integration by parts in each background variable give the drift

\[
\begin{aligned}
 dF_A[\Phi]/dt\big|_{\rm drift}
 ={}&F_A\left[(\partial_t+\sum_{a\in S}(u_a\cdot\nabla_a+\nu\Delta_a))\Phi\right]\\
 &+\sum_{a\in A}
   (D_{A\cup\{*\}}-D_A\mu_*)\mu^{S\setminus A}
   [K(x_a-x_*)\cdot\nabla_a\Phi]\\
 &+\frac1N\sum_{\substack{a,b\in A\\a\ne b}}
      D_A\mu^{S\setminus A}[K(x_a-x_b)\cdot\nabla_a\Phi].
\end{aligned}
\tag{R2}
\]

Here the starred slot is new. The second line comes from force labels outside the tuple, followed by subtraction of q(x_a), which was included in the first line. Its coefficient is exactly one: the force contributes 1/N, and adding a new distinct label changes D_A to D_(A plus star), whose denominator contains the same extra 1/N. The third line consists of force labels already inside the tuple. Brownian cross terms between different occupied slots vanish because their labels are distinct and the driving Brownian motions are independent.

### 3.2 Inversion and the single cancellation identity

Equation (R0) has the exact inverse

\[
 D_A=\sum_{B\subseteq A}U_B\mu^{A\setminus B}.
\]

Indeed, after substitution the coefficient of a fixed D_C mu^(A minus C) is the sum of (-1)^(|B|-|C|) over C contained in B contained in A; this is zero unless C=A, when it is one. The only other finite-set identity needed is

\[
 \sum_{A:\,E\subseteq A\subseteq S}(-1)^{|S|-|A|}
 =\begin{cases}1,&E=S,\\0,&E\ne S.\end{cases}
\]

This follows by choosing a subset of S minus E and expanding (1-1) to the power |S minus E|.

### 3.3 External force and full response

In the second line of (R2), inversion gives

\[
 D_{A\cup\{*\}}-D_A\mu_*
 =\sum_{B\subseteq A}U_{B\cup\{*\}}\mu^{A\setminus B}.
\]

Now sum (R2) over A with the sign in (R0). For a fixed force differentiation slot a and a fixed B, the permitted A contain B union {a}. The cancellation identity leaves exactly two cases:

1. B=S. This gives the upward term U_(k+1)[A_k^+ Phi].
2. B=S minus {a}. The a variable is integrated against mu and the starred variable replaces it. This gives U_k[R_a Phi].

The response term is therefore forced by the exact expansion. It cannot be dropped while retaining (R1).

### 3.4 Internal force and every lower contraction

In the third line of (R2), fix an ordered pair a not equal to b and expand D_A. The sign sum vanishes unless

\[
 B\cup\{a,b\}=S.
\]

There are exactly four surviving B:

\[
 S,\qquad S\setminus\{a\},\qquad S\setminus\{b\},
       \qquad S\setminus\{a,b\}.
\]

Each coefficient is positive one. The first gives C_k at level k. For the single-deletion cases, choose the deleted slot c. Summing all directed pairs incident to c gives the pair differences in Q_k. There are k equivalent choices of c. For the double-deletion case choose the unordered pair {c,d}; the two directions combine into B_cd, and there are binomial(k,2) equivalent pairs. These are exactly the last two drift terms of (R1).

This also proves that no other deterministic lower level occurs in the drift. The k=2 double contraction is the deterministic level U_0. At higher orders, scalar contributions remain present inside the definitions of U_j; there is no additional scalar term suppressed from (R1).

## 4. Martingale, bracket and every shared-label pattern

For a distinguished particle label i and a kernel H on m variables define

\[
 V_m^{(i)}[H]
 =\sum_{A\subseteq[m]}(-1)^{m-|A|}N^{-|A|}
   \sum_{\iota:A\hookrightarrow[N]\setminus\{i\}}
   \int H(x_{\iota(A)},y_{[m]\setminus A})\,\mu^{[m]\setminus A}(dy).
\]

Its denominator is N, not N-1. The excluded label is i even if another label occupies the same spatial point. Differentiating the explicit subset statistic gives

\[
 \Gamma_{k,i}[\Phi]:=\nabla_{x_i}U_k[\Phi]
 =\frac{k}{N}V_{k-1}^{(i)}[\nabla_1\Phi(x_i,\cdot)].
\]

There are k equivalent choices of the slot occupied by i; the remaining occupied labels must avoid it. Consequently

\[
 M_k[\Phi]_t=\sqrt{2\nu}\sum_{i=1}^N
       \int_0^t\Gamma_{k,i}[\Phi_r] \cdot dW_i(r).
\tag{R3}
\]

These are continuous square-integrable martingales on each fixed finite horizon. For real kernels their exact predictable cross variation is

\[
 \frac{d}{dt}\langle M_k[\Phi],M_\ell[\Psi]\rangle_t
 =2\nu\sum_{i=1}^N\Gamma_{k,i}[\Phi]\cdot\Gamma_{\ell,i}[\Psi]
 =\frac{2\nu k\ell}{N^2}\sum_i
    V_{k-1}^{(i)}[\nabla_1\Phi(x_i,\cdot)]\cdot
    V_{\ell-1}^{(i)}[\nabla_1\Psi(x_i,\cdot)].
\tag{R4}
\]

Here and below all time arguments on the right are the bracket time. The formulas extend complex bilinearly; conjugation would have to be inserted explicitly for a complex covariance convention.

To expose every coincidence in (R4), let L and R be disjoint slot sets of sizes k-1 and ell-1, and use a common root slot 0. Put

\[
 H(x_0,x_L,z_R)=\nabla_0\Phi(x_0,x_L)\cdot\nabla_0\Psi(x_0,z_R).
\]

For A contained in L and B contained in R, let tau range over **all partial bijections** between A and B, including the empty one. Write q(tau) for its number of matched pairs. Form the quotient slot set

\[
 J_\tau=(\{0\}\sqcup A\sqcup B)/\{a\sim\tau(a)\}.
\]

The root is never matched with another slot. There are

\[
 m=1+|A|+|B|-q(\tau)
\]

classes. Let H_(A,B,tau) be obtained from H by identifying precisely these matched variables and integrating L minus A and R minus B against independent mu factors. Then

\[
\boxed{
 \frac{d}{dt}\langle M_k[\Phi],M_\ell[\Psi]\rangle_t
 =2\nu k\ell
   \sum_{A\subseteq L}\sum_{B\subseteq R}
     (-1)^{k+\ell-2-|A|-|B|}
   \sum_\tau N^{-1-q(\tau)}D_{J_\tau}[H_{A,B,\tau}].}
\tag{R5}
\]

Every D in (R5) uses an injective assignment to its quotient classes. Thus it has no further coincidences. A pair of tuples in (R4) has a unique partial bijection determined by its shared nonroot labels, and conversely every injection on J_tau produces exactly one such pair. This proves both completeness and absence of multiplicity in (R5). Its power of N follows directly from

\[
 N^{-2-|A|-|B|}\sum_{J_\tau\hookrightarrow[N]}
 =N^{-1-q(\tau)}D_{J_\tau}.
\]

There are no omitted cases when m>N, since that injection sum is empty. If desired, every D in (R5) can be replaced by its subset inverse from Section 3.2 to express the bracket entirely in centered U_j. Formula (R5) is already a complete contraction formula, with explicit finite-N coefficients.

For example, writing F(x,y)=grad_x Phi(x,y), G(x,z)=grad_x Psi(x,z), and F_mu(x)=integral F(x,y)mu(dy), the pair-pair bracket is

\[
\begin{aligned}
 \frac{d}{dt}\langle M_2[\Phi],M_2[\Psi]\rangle
 ={}&\frac{8\nu}{N}\{D_3[F(x,y)\cdot G(x,z)]
       -D_2[F(x,y)\cdot G_\mu(x)]\\
 &\hspace{32mm}-D_2[F_\mu(x)\cdot G(x,z)]
       +D_1[F_\mu\cdot G_\mu]\}
       +\frac{8\nu}{N^2}D_2[F(x,y)\cdot G(x,y)].
\end{aligned}
\]

The last term is exactly the shared nonroot label. At k=ell=1, (R5) reduces to (2nu/N) eta[grad f dot grad h]. The bracket for P=U_2/2 is one quarter of the displayed pair-pair bracket; cross brackets involving P acquire the corresponding factor one half.

## 5. Manual low-order checks and Brownian cancellation

For k=1, the contractions vanish. Equation (R1) is the exact one-body identity

\[
 d\rho[f]=\{\rho[(\partial_t+\mathcal L_1)f]
             +U_2[\operatorname{Sym}_2 K(x-y)\cdot\nabla f(x)]\}\,dt+dM_1[f].
\]

Because K is odd, the symmetric kernel is half the usual difference-gradient kernel. Its diagonal value is zero.

For k=2 set B=B_12 and (B Phi)_mu(x)=integral B Phi(x,y)mu(dy). The internal term in the raw subset sum is D_2[B Phi]/N. Inversion gives exactly

\[
 \frac1N D_2[B\Phi]
 =\frac1N U_2[B\Phi]+\frac2N U_1[(B\Phi)_\mu]
       +\frac1N\mu^{\otimes2}[B\Phi].
\]

Therefore (R1), divided by two, yields

\[
\begin{aligned}
 dP[\Phi]=\Big\{&P[(\partial_t+\mathcal L_2+N^{-1}B)\Phi]
       +U_3[\operatorname{Sym}_3 K(x-z)\cdot\nabla_x\Phi(x,y)]\\
       &+N^{-1}\rho[(B\Phi)_\mu]
       +(2N)^{-1}\mu^{\otimes2}[B\Phi]\Big\}\,dt+\tfrac12dM_2[\Phi].
\end{aligned}
\]

For k=3 the raw centered statistic is D_3[Phi]-3D_2[Phi_mu]+3eta[Phi_mumu]-mu^3[Phi]. Its internal force terms before inversion are

\[
 \frac1N\{D_3[C_3\Phi]-3D_2[(B_{12}\Phi)_{\mu,3}]\}.
\]

Let A(x) be the integral of B_12 Phi over slots 2 and 3. Inverting the first term gives contributions at levels 3,2,1,0. At level 2,

\[
 (C_3\Phi)_{\mu,3}=(B_{12}\Phi)_{\mu,3}+Q_3\Phi,
\]

so the two-body coefficient is 3Q_3. At level 1 the integral of C_3 Phi over two slots is 2A+R_3 Phi, while inversion of the subtracted D_2 term gives 6A. Hence the one-body coefficient is 3R_3. At level zero, mu^3[C_3 Phi]=3mu^3[B_12 Phi], which cancels exactly. The resulting identity is

\[
 dU_3[\Phi]
 =\{U_3[(\partial_t+\mathcal L_3+N^{-1}C_3)\Phi]
       +U_4[A_3^+\Phi]+3N^{-1}U_2[Q_3\Phi]
       +3N^{-1}U_1[R_3\Phi]\}\,dt+dM_3[\Phi].
\]

The martingale integrands at these levels are, directly from their particle sums,

\[
 \Gamma_{2,i}=\frac2N\left\{\frac1N\sum_{j\ne i}\nabla_1\Phi(x_i,x_j)
                        -\int\nabla_1\Phi(x_i,y)\mu(dy)\right\},
\]

\[
\begin{aligned}
 \Gamma_{3,i}=\frac3N\Big\{&N^{-2}\sum_{\substack{j,\ell\ne i\\j\ne\ell}}
                 \nabla_1\Phi(x_i,x_j,x_\ell)
       -\frac2N\sum_{j\ne i}\int\nabla_1\Phi(x_i,x_j,y)\mu(dy)\\
       &+\iint\nabla_1\Phi(x_i,y,z)\mu(dy)\mu(dz)\Big\}.
\end{aligned}
\]

At k=4 the internal raw expression is

\[
 N^{-1}\{D_4[C_4\Phi]
       -4D_3[(C_3^{123}\Phi)_{\mu,4}]
       +6D_2[(B_{12}\Phi)_{\mu,3;\mu,4}]\},
\]

where C_3^(123) acts on the first three slots only. The general cancellation proof reduces it to

\[
 N^{-1}\{U_4[C_4\Phi]+4U_3[Q_4\Phi]+6U_2[R_4\Phi]\}.
\]

This full k=4 identity, including all other drift and noise coefficients, is tested by the exact code described below.

The absence of a separate diffusion lowering term is substantive, not an omission. For a symmetric pair kernel,

\[
 U_2[\Phi]=(\rho\otimes\rho)[\Phi]-N^{-1}\eta[\Phi(x,x)].
\]

The full-product Brownian Itô contraction is

\[
 (2\nu/N)\eta[(\nabla_1\cdot\nabla_2\Phi)(x,x)].
\]

The Laplacian of the diagonal restriction equals

\[
 \Delta(\Phi(x,x))
  =[(\Delta_1+\Delta_2+2\nabla_1\cdot\nabla_2)\Phi](x,x).
\]

Its subtraction cancels that cross term exactly. Section 3.1 proves the all-order cancellation directly from independent noises at distinct labels. The bracket of two statistics still has shared labels and therefore has the contractions in (R5).

## 6. Centering and elementary checks

For iid particles of law mu at one instant,

\[
 \mathbb E U_k[\Phi]
 =\left[\sum_{r=0}^k(-1)^{k-r}\binom{k}{r}\frac{(N)_r}{N^r}\right]
         \mu^{\otimes k}[\Phi].
\]

In particular the coefficients for k=1,2,3,4 are respectively

\[
 0,\qquad -N^{-1},\qquad 2N^{-2},\qquad 3N^{-2}-6N^{-3}.
\]

These identities require iid input only for this paragraph. They do not assert the dynamic law stays iid. For any time-independent constant kernel every derivative in (R1) is zero, even though U_k[1] may be a nonzero deterministic constant. For K=0 every interaction, response and lower drift term vanishes, leaving only the tensorized b-transport and independent diffusion.

For an exchangeable law with normalized r-point marginal f_r, the exact mean bridge is

\[
 \mathbb E U_k[\Phi]
 =\sum_{r=0}^k(-1)^{k-r}\binom{k}{r}\frac{(N)_r}{N^r}
   (f_r\otimes\mu^{\otimes(k-r)})[\Phi].
\]

Terms with r>N are zero; they require no definition of f_r. No transfer to a Gibbs, equilibrium or arbitrary deterministic preparation is used.

## 7. Exact reproducible computation

Files:

- `DISCOVERY_CODE/round001_recursion_check.py`.
- `DISCOVERY_CODE/round001_recursion_check_output.txt`.

Command, run in this worktree:

```sh
python3 DISCOVERY_CODE/round001_recursion_check.py > DISCOVERY_CODE/round001_recursion_check_output.txt
```

Environment: Python 3.9.6; only the Python standard library; no random seed because the inputs are deterministic; tolerance exactly zero. All Laurent coefficients lie in Q(i), represented as pairs of rational numbers.

The test is written in angle coordinates theta=2pi x. In those coordinates it takes K(theta)=sin(theta), b(theta)=sin(2theta), and diffusion coefficient nu_theta=3/5. This is an exact instance of the unit-torus gradient model: choose

\[
 g(x)=(2\pi)^{-2}\cos(2\pi x),\qquad
 V(x)=\frac{1}{2(2\pi)^2}\cos(4\pi x),\qquad
 \beta=(2\pi)^2/(3/5).
\]

The positive background density, with respect to dtheta/(2pi), is

\[
 1+\tfrac13\cos\theta+\tfrac15\sin(2\theta).
\]

It is at least 7/15. Its first time derivative is computed from the exact mean-field equation at that instant. Thus the inhomogeneous response terms and the time evolution of every mu factor are both exercised. Complex test kernels are used only as a compact coefficient basis; taking real and imaginary parts gives tests of real smooth kernels.

The direct drift calculation first builds U_k as a Laurent polynomial in all N particle coordinates, differentiates that complete polynomial with the particle generator, and adds the explicit mean-field time derivatives. The proposed calculation instead applies L_k, C_k, A_k^+, Q_k and R_k to kernel polynomials before inserting them into U. The two sides share elementary rational-polynomial arithmetic but not this substantive decomposition. This remains one constructor's discovery self-check; it does not replace the independent verifier required by the campaign.

Observed results:

- 37,886 exact integer subset coefficients pass through k=9, for every force support of size one or two and every candidate B.
- Full drift identities pass for k=1,2,3,4 and N=2,3,4, including k>N, on symmetric mixed Fourier kernels plus separable products.
- The explicit deterministic time-derivative slot is checked at all these levels.
- Every rooted gradient agrees with direct particle differentiation for all the same k and N.
- Constant-kernel and K=0 checks pass at k=4 for N=2,3,4.
- Full partial-matching bracket identities pass for (N,k,ell)=(2,1,1),(2,2,2),(3,2,3),(3,1,4).
- Final recorded line: `ALL ROUND 001 RECURSION SELF-CHECKS PASSED`.

The root coordinator separately reported 144 exact rational Fourier checks of the frozen drift formula using its own implementation. That report is corroboration to be integrated by the root; this worker does not assign independent audit status to its general proof on that basis.

## 8. What this does and does not prove about M2

The exact algebra exposes the following raw coefficients:

| Mechanism | Output level | Exact raw coefficient |
|---|---:|---:|
| One-body transport, diffusion and background response | k | one per slot; diffusion nu |
| External nonlinear interaction | k+1 | one per one of k force slots |
| Interaction between two occupied slots | k | 1/N per unordered pair operator B_ab |
| One contracted member of an internal pair | k-1 | k/N multiplying Q_k, which sums k-1 pairs |
| Two contracted members of an internal pair | k-2 | binomial(k,2)/N |
| Bracket with q shared nonroot labels | up to k+ell-1-q before centering | 2 k ell /(beta N^(q+1)), with all subset signs in (R5) |

For fixed smooth kernels there are elementary deterministic bounds

\[
 |U_k[\Phi]|\le 2^k\|\Phi\|_\infty,
 \qquad
 |\Gamma_{k,i}[\Phi]|\le\frac{k2^{k-1}}N\|\nabla_1\Phi\|_\infty,
\]

and hence

\[
 \left|\frac{d}{dt}\langle M_k[\Phi],M_\ell[\Psi]\rangle\right|
 \le\frac{2k\ell\,2^{k+\ell-2}}{N\beta}
       \|\nabla_1\Phi\|_\infty\|\nabla_1\Psi\|_\infty.
\]

They follow by bounding every normalized injective sum by one and summing its subset terms. They prove square integrability and give fixed-order, fixed-kernel noise bounds. They do not control derivatives of recursively constructed correctors uniformly in order or cutoff.

No Riesz exponent s occurs anywhere in this smooth algebra. It cannot by itself generate a power of lambda_N=beta_N N^(s/d-1), identify a singular partial-diagonal degree, or decide finite versus infinite critical closure. Replacing the displayed raw coefficients with effective lambda powers needs estimates on the actual corrector kernels, singular integration, their background dependence and the selected law. The upward operator is present at every order; its presence does not itself prove that every order survives after scaling.

There is also no law-independent smallness of U_k. For a smooth f with mu[f]=0, choose the permitted smooth-model configuration x_i=x for every i and Phi=f tensor-power k. Then

\[
 U_k[\Phi]=\frac{(N)_k}{N^k}f(x)^k\longrightarrow f(x)^k
\]

for each fixed k, which is nonzero when f(x) is nonzero. Thus an attempted inference of fluctuation-scale smallness from the generator coefficients alone fails already in an allowed deterministic preparation. This does not falsify an iid or Gibbs theorem with its own assumptions.

**First remaining line for M2:** choose the corrector function spaces and the law class, then prove an order- and cutoff-explicit estimate for the time-integrated upward residual and all correction martingale brackets after multiplying by the selected fluctuation scale. Such an estimate must decide whether the gain per corrector order tends to zero, remains summable at fixed critical coupling, or requires an enlarged state. It has not been supplied here. No subcritical or critical limit theorem, singular passage, finite truncation or infinite summability is promoted by this memorandum.

## 9. Handoff and scope

The full all-order smooth generator recursion and complete bracket contraction formula are proved above, with manual k=2 and k=3 reductions and exact k=4 checks. The general proof needs isolated reconstruction and hostile review before any independent promotion. All canonical STATE ledgers and round-level status decisions remain the root's responsibility under the single-writer rule.

Only this memorandum and the two named discovery files were created by this worker. Frozen inputs, baseline files, canonical ledgers, branch state and commits were not modified. Repository verification passed before the work. The exact mathematical result uses no source note claim, so there is no unverified imported theorem hidden in the proof.
