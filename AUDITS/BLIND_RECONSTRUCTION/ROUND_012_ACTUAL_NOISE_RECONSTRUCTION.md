# Round 012: fresh reconstruction of the genuine corrector noise estimate

TASK066. Issued 2026-09-18 UTC. **RECONSTRUCTION COMPLETE; CONDITIONAL DERIVATION; NO AUDIT PASS ASSIGNED.**

The frozen THM033 estimates follow from the specified prior pair, particle, and domain premises. The new argument below has no unproved additional line. The conclusion remains conditional on those premises, in particular the complete THM028 singular corrector domain and the supplied energy construction. This report does not certify those earlier modules or presume an unseen R10 review. Root comparison and a separate fresh hostile review are still required.

The two decisive quantitative facts are a uniform weighted derivative propagation estimate under bounded rescaled diffusivity, and a strict sub-Coulomb pair occupation estimate extracted from the *signed Laplacian term* in the full particle energy identity. No individual pair-force square is extracted from the total-force square. All estimates concern the true inverse with both responses and the actual iid-Haar-prepared particle dynamics.

The worktree and exact exposure are recorded in `EXPOSURE.md`. The first reads were TASK066 and its input manifest; exactly 23 allowed source files were copied and hash-verified before mathematical reading. No root candidate, current R11 output, current audit/state/history, memory file, or prior checker was opened. The automatic app memory summary was ambient exposure only. No source was edited, no child was spawned, and no commit or push was made. This report was sealed before mathematical comparison.

## 1. Assertion, negation, conventions, and imported premises

Fix an integer \(d\ge3\), \(0<s<d-2\), \(N\ge2\), finite \(T\), smooth real terminal \(h\), and finite \(L,\nu_*\ge0\). Set

\[
p=s+2,\qquad a=s/p,\qquad \theta=1-s/d,
\qquad 0\le\nu\le\nu_*,\qquad \chi_N=\nu N^{2/p}\le L.
\tag{1.1}
\]

The torus has Haar mass one and characters \(e^{2\pi i k\cdot x}\). The exact frozen kernel is

\[
\widehat g(0)=0,\quad
\widehat g(k)=c_{d,s}|k|^{s-d},\quad
c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},
\qquad K=-\nabla g.
\tag{1.2}
\]

The supplied kernel proof gives \(g(z)=|z|^{-s}+v(z)\) near zero, with smooth even \(v\). In this strict range, with \(D=\operatorname{div}K\),

\[
D(z)=s(d-2-s)g_{p}(z),\qquad
D(z)=s(d-2-s)|z|^{-p}+O(1)\quad(z\to0).
\tag{1.3}
\]

It is an integrable signed density with total integral zero. The bounded smooth remainder includes the compensation; it is never dropped. In particular \(D\ge-\kappa\) for a fixed finite \(\kappa\).

The homogeneous actual Fourier test is

\[
f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
e^{-(T-t)[4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{s+2-d}]}
e^{2\pi i k\cdot x}.
\tag{1.4}
\]

Every fixed spatial derivative is bounded uniformly in \(N,t,\nu\), by the corresponding absolutely summable Fourier seminorm of \(h\). The source and full pair generator are

\[
J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)),\qquad
G_N=\nu(\Delta_x+\Delta_y)+N^{-1}K(x-y)\cdot(\nabla_x-\nabla_y),
\tag{1.5}
\]

\[
R_xF(x,y)=-\int D(w)F(x+w,y)\,dw,\qquad
R_yF(x,y)=-\int D(w)F(x,y+w)\,dw,\qquad R=R_x+R_y.
\tag{1.6}
\]

Let \(S_{t,u}\) be the true singular base pair evolution and

\[
U_t=\mathbb E_{t,x,y}\int_t^T J_u(X_u,Y_u)\,du,
\qquad
\Phi_t=U_t+\int_t^T S_{t,u}R\Phi_u\,du.
\tag{1.7}
\]

This is the unique bounded Borel terminal-zero full inverse in the supplied source class. It is pair symmetric. No surrogate inverse or response truncation occurs below.

The exact primary assertion is that for every fixed \(1<q<d/2\) with \(q\le s+1\),

\[
\sup_{0\le t\le T}\sup_{x\ne y}
\frac{|\nabla_{x,y}\Phi_t(x,y)|}{w_q(x-y)}
\le C_qN^{(s+1-q)/p},
\tag{1.8}
\]

and, for positive \(\nu\), with \(\beta=1/\nu\), \(b_N=\min(\beta,1)\),

\[
Q_N:=2\nu Nb_N\,\mathbb E\int_0^T\sum_i
|\nabla_iP_N[\Phi_t](X(t))|^2dt
\le Cb_NN^a(N^{-\theta}+\nu).
\tag{1.9}
\]

Here the expectation is under the actual singular particle law, started from iid Haar independently of its Brownian drivers. The statistic is exactly

\[
P_N[F]=\frac1{2N^2}\sum_{i\ne j}F(X_i,X_j)
-\frac1N\sum_i\int F(X_i,y)\,dy
+\frac12\int F(x,y)\,dxdy.
\tag{1.10}
\]

The assertion includes the leading and cross bracket statements and strict-range consequences proved in Sections 6–7. Its negation is an admitted fixed tuple/family violating one of the stated uniform estimates or cross bounds, or an admitted sequence in an asserted strict range with positive limsup of the genuine noise functional. This is an implication with the exact source premises below; failure of a source premise is not silently ruled out by this reconstruction.

| Supplied files | Imported mathematical content and boundary |
|---|---|
| Frozen R1 model and algebra | Unit-Haar/Fourier/noise convention and literal deleted-pair statistic. New particle coefficients below are derived again. |
| R4 response proof, Sections 2–4; THM021; R5 source addendum | The coefficient-one expansion, positive heat representation, finite signed response measure, and (1.3). No source statement outside its hypotheses is invoked. |
| R5 pair/full-inverse/interface proofs, THM023–025, symmetry clarification | Singular base process, Borel source inverse, both response operators, pointwise Volterra uniqueness, exact Fourier test. Symmetry means exchange of pair slots, not self-adjointness. |
| R7 complete weighted-gradient proof, Sections 2–8; THM027 | Fixed-N legitimate flow derivative/expectation formulas, weighted response differentiation, and identification of derivative series with the true inverse. Its existing N-dependent constants are **not** used as uniform constants. |
| R6 particle proof, Sections 3–5 and 7–8; THM026 | Actual singular paths, iid preparation, fixed-N singular energy identity with absolute Laplacian occupation at positive noise. No uniform density bound is imported. |
| Complete R8 domain premise, Sections 9–11; THM028 | Weak/slice derivatives and the genuine corrector stochastic integral and bracket. This remains explicitly conditional; existence of the pair inverse alone is insufficient. |
| R10 report, Section 3; THM031 | The deterministic energy-floor construction, restated in Section 5. Its issued candidate status is preserved; no unseen audit verdict and no R9/R11 energy assertion is imported. |

No external literature claim, theorem number, or novelty assertion is needed. The quantitative construction below does not use R10 entropy, Fourier fluctuation bounds, smooth-tail approximation, or three-label sign. Their availability is not a substitute for an actual-law estimate.

## 2. Uniform weighted propagation at bounded rescaled diffusivity

Use the R7 fixed cutoff: \(R_0=1/16\), a smooth even cutoff \(\zeta\) equal to one on \(B_{R_0}\), zero outside \(B_{2R_0}\), and

\[
w_1(z)=\exp[\zeta(z)\log(1/|z|)],\qquad w_\alpha=w_1^\alpha.
\tag{2.1}
\]

Thus \(w_\alpha\ge1\), \(w_\alpha=|z|^{-\alpha}\) in the inner ball, and \(w_\alpha^m=w_{m\alpha}\) exactly. Constants for another fixed allowed weight change only by finite comparison factors.

The pair drift has Jacobian

\[
\frac1N\begin{pmatrix}DK(z)&-DK(z)\\-DK(z)&DK(z)\end{pmatrix}.
\tag{2.2}
\]

For the principal force, its eigenvalues are zero in center directions, \(2sN^{-1}r^{-p}\) in transverse relative directions, and \(-2s(s+1)N^{-1}r^{-p}\) in the radial relative direction. Consequently, for a fixed constant \(C_0\) absorbing the periodic and cutoff remainders,

\[
\ell_N(z)=\frac{2s}{N}\zeta(z)r^{-p}+\frac{C_0}{N}\ge0,
\qquad
\|A_{t,u}\|\le\exp\left(\int_t^u\ell_N(Z_v)\,dv\right),
\tag{2.3}
\]

where \(A\) is the starting-state derivative of the auxiliary pair flow. The one-sided eigenvalue, rather than the absolute Hessian norm, is essential.

On the inner ball the relative generator is \(2\nu\Delta_z+(2/N)K(z)\cdot\nabla_z\). For \(q>1\), direct differentiation therefore gives

\[
\frac{(G_N+\ell_N)w_q}{w_q}
\le-\frac{2s(q-1)}N r^{-p}
+2\nu q(q+2-d)_+r^{-2}+\frac{C_q}{N}.
\tag{2.4}
\]

Write \(b=2s(q-1)/N\) and \(A=2\nu q(q+2-d)_+\). The exact scalar maximum is

\[
\sup_{v\ge0}\{Av^2-(b/2)v^{s+2}\}
=\frac{s}{s+2}A\left(\frac{4A}{(s+2)b}\right)^{2/s}
\tag{2.5}
\]

when \(A>0\), and is zero when \(A=0\). This follows by differentiating, with maximum at \(v^s=4A/((s+2)b)\). Its parameter dependence is

\[
C_{s,q}\nu^{1+2/s}N^{2/s}
=C_{s,q}(\nu N^{2/p})^{1+2/s}
\le C_{s,q}L^{1+2/s}.
\tag{2.6}
\]

All annular derivatives are bounded. Their diffusion contribution is bounded by a constant times \(\nu_*\), their drift contribution by a constant times \(1/N\). Thus there are \(C<\infty\), independent of selected \(N,\nu\), and \(c=s(q-1)>0\) such that globally

\[
(G_N+\ell_N)w_q
\le Cw_q-\frac cN\mathbf1_{r\le R_0}r^{-q-p}.
\tag{2.7}
\]

Stop the supplied auxiliary pair process before entering a shrinking collision tube and apply ordinary Itô to
\(e^{-C(u-t)+\int_t^u\ell_N}w_q(Z_u)\).
Before each stop every coefficient is bounded and the stochastic term has zero expectation. Retaining the nonnegative terminal term and occupation term, and then using noncollision, Fatou for the terminal term, and monotone convergence for the occupation, gives

\[
\mathbb E_{t,z}e^{\int_t^u\ell_N}w_q(Z_u)\le e^{C(u-t)}w_q(z),
\tag{2.8}
\]

\[
\mathbb E_{t,z}\int_t^T e^{\int_t^u\ell_N}
\frac1N\mathbf1_{r_u\le R_0}r_u^{-q-p}\,du
\le c^{-1}e^{CT}w_q(z).
\tag{2.9}
\]

Discarding a positive terminal quantity is in the correct direction. No uniform integrability of a stopped singular weight is assumed.

For fixed N the R7 expectation-derivative formula is valid for bounded C1 inputs with finite weighted derivative seminorm. Its proof uses higher-moment barriers and a simultaneous local-flow construction on compact sets away from collisions; it does not rely only on a derivative along one random path. For completeness, the same local barrier has \((G_N+m\ell_N)w_\alpha\) and negative coefficient \(2s(\alpha-m)/N\) whenever \(\alpha>m\). Arbitrarily large \(\alpha\) supply all compact-start moments needed in that proof. Formula (2.6) also makes those constants uniform under the present restriction when the moment and weight are fixed. Uniformity of the interchange itself is unnecessary: validity at each fixed N is enough before applying (2.8).

With \(|F|_q=\sup|\nabla F|/w_q\), (2.3), (2.8), and that legitimate formula give

\[
\nabla S_{t,u}F=\mathbb E[A_{t,u}^{\mathsf T}\nabla F(Z_u)],
\qquad |S_{t,u}F|_q\le e^{C(u-t)}|F|_q.
\tag{2.10}
\]

No N-dependent R7 exponential has been relabelled a uniform constant: it has been recomputed in (2.4)–(2.7).

## 3. The source derivative and the exact N power

Differentiating the actual source retains both terms:

\[
\begin{aligned}
\nabla_xJ&=DK(z)^{\mathsf T}(\nabla f(x)-\nabla f(y))+D^2f(x)K(z),\\
\nabla_yJ&=-DK(z)^{\mathsf T}(\nabla f(x)-\nabla f(y))-D^2f(y)K(z).
\end{aligned}
\tag{3.1}
\]

The Hessian bound on \(f\) supplies the factor \(r\) in the gradient difference. Hence, uniformly in time and parameters,

\[
|\nabla_{x,y}J_t|\le C r^{-s-1}\quad(r\le R_0),
\qquad |\nabla J_t|\le C\quad(r\ge R_0).
\tag{3.2}
\]

Fix \(q\le s+1\) and put \(k=s+1-q\). Then \(0\le k<p\). For every \(r>0\),

\[
r^{-k}\le N^{k/p}\left(1+\frac1N r^{-p}\right).
\tag{3.3}
\]

Indeed, with \(x=N^{-1/p}/r\), this is \(x^k\le1+x^p\); use \(x\le1\) or \(x\ge1\). In particular the case \(k=0\) is included without division by \(k\). Combining (3.2) and (3.3) yields

\[
|\nabla J_t(z)|\le CN^{k/p}
\left[w_q(z)+\frac1N\mathbf1_{r\le R_0}r^{-q-p}\right].
\tag{3.4}
\]

The fixed-N source differentiation formula established in R7 gives

\[
\nabla U_t(z)=\mathbb E_{t,z}\int_t^T
A_{t,u}^{\mathsf T}\nabla J_u(Z_u)\,du.
\tag{3.5}
\]

Its justification is applicable to the actual smooth Fourier data. The R7 local compact-start source moment bound uses a higher moment exponent and sufficiently large weight; it supplies uniform integrability of difference quotients before differentiating. Equations (2.8), (2.9), and (3.4) then prove the new quantitative estimate

\[
|U_t|_q\le CN^{k/p}e^{C(T-t)}(T-t+c^{-1}).
\tag{3.6}
\]

This step improves the old crude occupation cost of order N. Keeping the factor \(1/N\) in (3.4) matched to the negative term in (2.7) is what gives the stated power.

## 4. Restoring both responses without contaminating the exponent

Since the background is exactly constant, weak differentiation commutes with (1.6). There is no derivative of a background density and no zeroth-order input term in the derivative estimate. The R7 convolution estimate gives

\[
\int |D(w)|w_q(z+w)\,dw\le C_{D,q}w_q(z),
\qquad |RF|_q\le2C_{D,q}|F|_q.
\tag{4.1}
\]

Here \(D\) has local power \(p<d\), and \(q<d\). One elementary verification splits the integration into neighborhoods of \(w=0\), \(w=-z\), and the complement. The first/complement pieces cost a constant times \(r^{-q}\int|D|\); the second costs at most \(Cr^{-p}r^{d-q}\le Cr^{-q}\), as \(p<d\). Bounded periodic remainders are harmless. This is a weighted bound, not a claim that the convolution is bounded at \(z=0\).

Fubini against the finite measure \(|D|\), applied to the globally L1 weak derivatives supplied by R7, justifies the differentiation. Off diagonal the two singularities are separated and local dominated convergence gives the continuous derivative representative. No singular measure is differentiated and no diagonal value is assigned to \(\nabla\Phi\).

Let \(VF(t)=\int_t^T S_{t,u}RF_u\,du\). On every ordered time simplex, the propagation exponents in (2.10) add over disjoint intervals; their sum is at most \(CT\). Iterating (2.10), (3.6), and (4.1),

\[
|(V^jU)_t|_q\le CN^{k/p}e^{CT}
\frac{(2C_{D,q}T)^j}{j!}.
\tag{4.2}
\]

The bounded-value series is already the unique Borel inverse in (1.7). Equation (4.2) makes its derivatives converge locally uniformly off diagonal and uniformly after division by the weight. The elementary closedness of C1 under local uniform convergence of values and derivatives identifies the derivative limit with that same inverse. Summing proves (1.8), including terminal time, where the inverse and derivative vanish.

It is essential here to propagate only the derivative seminorm. Propagating the old combined sup-plus-derivative norm would import the larger sup bound on \(U\), and would not prove (1.8) when \(q\) is close to \(s+1\). Homogeneity is used at exactly this point.

The derivative is the global weak derivative: deleting a tube of radius \(\epsilon\) in integration by parts produces a boundary contribution bounded by \(C\|\Phi\|_\infty\epsilon^{d-1}\to0\); the derivative majorant is L1. Since \(2q<d\), it is also Haar L2. These statements are for each finite N, with (1.8) the quantitative bound. This topology does not itself transfer to the interacting law; Section 5 supplies the required separate estimate.

## 5. Actual pair occupation from the full energy identity

Set

\[
H_N(x)=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
B_i(x)=\frac1N\sum_{j\ne i}K(x_i-x_j)=-\nabla_iH_N(x).
\tag{5.1}
\]

The deterministic floor needed below is \(H_N\ge-CN^{s/d}\). To make the exact source and diagonal coefficient explicit, put \(\alpha=(d-s)/2\) and use the supplied positive heat representation

\[
g^{>\tau}(z)=A\int_\tau^\infty t^{\alpha-1}(p_t(z)-1)dt,
\qquad A=\frac{4^{\alpha}\pi^{d/2}}{\Gamma(s/2)}.
\tag{5.2}
\]

Positivity of the heat kernel gives \(g\ge g^{>\tau}-A\tau^\alpha/\alpha\) off zero. Its nonzero Fourier coefficients \(a_\tau(k)\) are positive. The small-time Gaussian bound and large-time exponential decay give \(g^{>\tau}(0)\le C\tau^{-s/2}\) for \(0<\tau\le1\). Thus exact removal of the self diagonal gives

\[
H_N\ge\frac N2\sum_{k\ne0}a_\tau(k)|\widehat\eta_N(k)|^2
-\frac12g^{>\tau}(0)-\frac{N-1}{2\alpha}A\tau^\alpha.
\tag{5.3}
\]

Taking \(\tau=N^{-2/d}\), each negative term is at most \(CN^{s/d}\). This reproduces precisely the floor portion of the conditional R10 construction. The argument uses a Fourier-positive truncated kernel, not a pointwise-positive weighted kernel. It requires no assertion about iid laws at positive times.

At positive diffusivity the supplied R6 exact energy identity, after undoing its nonnegative shift, is

\[
\mathbb EH_N(X_T)+\mathbb E\int_0^T\sum_i|B_i(X_t)|^2dt
=\mathbb EH_N(X_0)+\nu\mathbb E\int_0^T\Delta_{Nd}H_N(X_t)dt.
\tag{5.4}
\]

The initial expectation is zero because the preparation is iid Haar and \(\int g=0\). Its finiteness follows from \(g\in L^1\). Every unordered pair is differentiated in both particle coordinates, so off collisions

\[
\Delta_{Nd}H_N=-\frac2N\sum_{i<j}D(x_i-x_j).
\tag{5.5}
\]

Exchangeability and (5.4) give the exact signed identity

\[
\nu(N-1)\mathbb E\int_0^T D(X_1-X_2)dt
=-\mathbb EH_N(X_T)-\mathbb E\int_0^T\sum_i|B_i|^2dt.
\tag{5.6}
\]

The source passage is substantive: R6 first proves the stopped identity, then integrability of the full drift square and of its nonnegative Laplacian defect, then convergence of the energy martingale in L2. For positive \(\nu\), this gives absolute occupation of \(\Delta H_N\). In the strict sub-Coulomb case, (1.3) and a bounded negative part show that this also makes the individual nonnegative pair singularities integrable. Thus (5.5)–(5.6) are legitimate ordinary off-collision density integrals, not formal evaluations of a distribution on a path. There is no new singular limit interchange here.

Because the coefficient \(c_s=s(d-2-s)\) is strictly positive, (1.3), smoothness off zero, and the fixed definition of \(w_p\) give

\[
D(z)\ge c_s w_p(z)-C_s\quad(z\ne0).
\tag{5.7}
\]

One may choose \(C_s\) as the maximum of \(c_sw_p-D\), whose extension is bounded near zero and on the complement. Retain the entire nonnegative force square in (5.6), then discard it only with its negative sign. Using (5.3),

\[
\nu c_s(N-1)\mathbb E\int_0^T w_p(X_1-X_2)dt
\le CN^{s/d}+\nu C_s(N-1)T.
\tag{5.8}
\]

Since \(N/(N-1)\le2\),

\[
\boxed{\quad
\nu\mathbb E\int_0^T w_p(X_1-X_2)dt
\le C(N^{-\theta}+\nu).
\quad}
\tag{5.9}
\]

This estimate concerns the actual law. No density supremum, factorization, entropy-to-unbounded-test passage, or concentration inference is used. Its constant can deteriorate as \(s\uparrow d-2\); the exponent is fixed. At zero noise no division is made and (5.9) is not needed for brackets.

## 6. Genuine particle gradients and self/cross brackets

Choose the particular allowed weight

\[
q_*=(s+2)/2=p/2.
\tag{6.1}
\]

Then \(q_*>1\) because \(s>0\), \(q_*<d/2\) because \(s<d-2\), and \(q_*\le s+1\) because \(s\ge0\). Formula (1.8) gives, with \(G_t=\nabla_x\Phi_t\),

\[
|G_t(x,y)|^2\le CN^{s/p}w_p(x-y)=CN^aw_p(x-y).
\tag{6.2}
\]

Let \(A_t(x)=\int G_t(x,y)dy\). The weak/slice differentiation in the full R8 premise identifies it with the derivative of the background projection. Since \(q_*<d\), (1.8) also gives the sufficient bound

\[
\sup_{t,x}|A_t(x)|^2\le CN^a\left(\int w_{q_*}\right)^2\le CN^a.
\tag{6.3}
\]

No stronger N-uniform smooth projection estimate is required. Direct differentiation of the ordered statistic (1.10), using pair symmetry to combine its two contributions, yields exactly

\[
\nabla_iP_N[\Phi_t]
=\frac1{N^2}\sum_{j\ne i}G_t(X_i,X_j)-\frac1N A_t(X_i).
\tag{6.4}
\]

There is no evaluation at \((X_i,X_i)\). The factor one half in (1.10) is canceled precisely by the two ordered appearances of the differentiated label. For comparison with row centering, putting \(H=G-A\) rewrites (6.4) as
\(N^{-2}[\sum_{j\ne i}H_{ij}-A_i]\); the missing-self background remains.

Finite-sum Cauchy–Schwarz, followed by exchangeability, gives

\[
\mathbb E\sum_i|\nabla_iP_N|^2
\le\frac{2(N-1)^2}{N^3}\mathbb E|G_{12}|^2
+\frac2N\mathbb E|A_1|^2.
\tag{6.5}
\]

No distinct-triple covariance sign is assumed in this inequality; it controls the full square. This formula also applies to N=2. Multiplying once by the physical scaling \(2\nu Nb_N\) and integrating gives

\[
Q_N\le4\nu b_N\left[
\frac{(N-1)^2}{N^2}\mathbb E\int_0^T|G_{12}|^2dt
+\mathbb E\int_0^T|A_1|^2dt\right]
\le Cb_NN^a(N^{-\theta}+\nu),
\tag{6.6}
\]

where (5.9), (6.2), and (6.3) were used. This proves (1.9). The complete R8 premise identifies this functional with the expected bracket of the *genuine* corrector martingale; without that premise (6.6) is only a bound on a well-defined gradient functional.

The leading unscaled martingale is

\[
M^1_t=\frac{\sqrt{2\nu}}N\sum_i\int_0^t\nabla f_u(X_i(u))\cdot dW_i(u).
\tag{6.7}
\]

Its expected bracket scaled by \(Nb_N\) satisfies

\[
Q_N^{(1)}=2\nu b_N\mathbb E\int_0^T
\langle\eta_N,|\nabla f_t|^2\rangle dt
\le C\nu b_N\le C.
\tag{6.8}
\]

The last inequality is exact since \(\nu b_N=\min(1,\nu)\). Apply Cauchy–Schwarz first to the finite particle scalar product and then in probability times time. The expected total variation of the scaled cross bracket obeys

\[
\mathbb E\int_0^T
\left|\frac{d\langle\sqrt{Nb_N}M^1,\sqrt{Nb_N}M^2\rangle_t}{dt}\right|dt
\le\sqrt{Q_N^{(1)}Q_N}\le C\sqrt{Q_N}.
\tag{6.9}
\]

This is a bound on the integral of the absolute cross density, stronger than a bound only on its signed integral. It needs no positivity of a cross covariance. At \(\nu=0\), both stochastic integrals and all their brackets vanish directly; \(\beta=1/\nu\) is not introduced.

## 7. Strict exponent consequences and excluded boundaries

For a microscopic critical sequence \(\lambda_N=\beta_NN^{-\theta}\to\lambda\in(0,\infty)\),

\[
\nu_N=\lambda_N^{-1}N^{-\theta},\qquad b_N=1\text{ eventually},
\qquad
\theta-\frac2p=\frac{s(d-s-2)}{dp}>0.
\tag{7.1}
\]

Thus the bounded-\(\chi_N\) hypothesis is eventually satisfied, indeed \(\chi_N\to0\), for every fixed strict sub-Coulomb exponent. Formula (6.6) is \(Q_N\le CN^{a-\theta}\). Its exponent is negative exactly when

\[
a<\theta
\quad\Longleftrightarrow\quad s(s+2)<2d.
\tag{7.2}
\]

Every critical sequence in the stated strict range therefore has \(Q_N\to0\), and (6.9) gives vanishing absolute scaled cross variation in expectation.

If instead \(\chi_N\le L\) and \(0<s<\min(2,d-2)\), then \(\nu_N\le LN^{-2/p}\). Hence

\[
Q_N\le Cb_N[N^{a-\theta}+LN^{(s-2)/p}]\to0.
\tag{7.3}
\]

Both exponents are strictly negative: the second because \(s<2\), and the first because \(s(s+2)<2(s+2)<2d\). More generally, within the fixed-data bounded-\(\chi_N\) family where (6.6) applies, \(a<\theta\) and \(N^a\nu_N\to0\) are sufficient, since \(b_N\le1\).

At equality in either exponent test the bound only remains bounded and supplies no decay. The Coulomb endpoint is excluded in two distinct ways: \(q_*=d/2\) is not an allowed Haar H1 weight, and \(D=c_d(\delta_0-dz)\) has no positive off-collision \(r^{-d}\) density. Equation (5.7) then fails. The strict sub-Coulomb density argument must not be applied to the atom. No logarithmic normalization is obtained by substituting \(s=0\).

There is no conclusion here for unrestricted bounded diffusivity, all larger s, full subcriticality, a cubic residual, a limiting fluctuation law, or an infinite critical hierarchy. Mean-field centering is unchanged. The three campaign temperature conditions remain distinct.

## 8. Independent falsification route and exact supporting checks

An elementary deterministic radial diagnostic independently tests the proposed N power. Remove periodic remainders and noise only in this diagnostic, and use a local quadratic test with Hessian \(cI\), \(c\ne0\). Then the base relative trajectory obeys

\[
r(u)^p=r_0^p+2spu/N,\qquad J=scr^{-s},\qquad
U(r_0)=\frac{cN}{4}[r(T)^2-r_0^2].
\tag{8.1}
\]

Differentiation gives

\[
U'(r_0)=-\frac{cN}{2}r_0[1-(r_0/r(T))^s].
\tag{8.2}
\]

At \(r_0=zN^{-1/p}\), fixed positive \(z,T\), its weighted radial magnitude has exactly the power \(N^{(s+1-q)/p}\). This challenges a smaller claimed power and checks the factor \(2s/N\). It is a local base-model diagnostic, not a periodic full-inverse counterexample or a proof of sharpness for THM033. The genuine estimate above keeps both responses and the actual Fourier test.

The newly written standard-library checker differentiates raw pair energies by second-order automatic differentiation over rational numbers, constructs literal ordered statistics, and tests the generator product identity. It does not read any previous checker. Its checks include:

- Full pair drift Jacobian eigenvalues, the two relative diffusion factors, the negative weighted drift coefficient, and positivity/vanishing of the sub-Coulomb/Coulomb Laplacian coefficient.
- Literal N-particle energy gradients and Laplacians for N=2,3 and larger, including all particle coordinates and transverse second derivatives.
- Direct differentiation of a literal symmetric ordered-pair statistic, its background derivative and missing-self term, and the identity giving exactly \(2\nu\sum_i|\nabla_iP|^2\).
- The finite-sum square estimate used in (6.5), with genuine N=2 cases and zero/positive diffusivities.
- Exact rational exponent identities in (2.6), (3.3), (6.2), and (7.1)–(7.3), including equality cases where decay is not inferred.

The executed checker completed **2,750 exact assertions** successfully. These tests use deterministic rational inputs, no tolerance, random seed, external library, or asymptotic numerical inference. Polynomial/local radial probes test algebra only; they are not substituted for the full periodic inverse in the analytic proof. The checker result and all tested conventions are in the companion JSON. A successful arithmetic check is supporting evidence, not a pass assigned to this report.

## 9. Adversarial self-review, exact disposition, and handoff

| Potential failure | Resolution or retained limitation |
|---|---|
| An old fixed-N exponential was called uniform. | Its scalar maximum is recomputed; the N powers cancel exactly in (2.6) under bounded rescaled diffusivity. |
| Source occupation still costs a full N. | Equation (3.3) puts precisely \(1/N\) beside the retained singular occupation term. |
| The combined weighted norm introduces an excessive sup-bound power. | Only the derivative seminorm is propagated, using exact homogeneous convolution; both responses remain. |
| Differentiating an expectation was based only on a single path. | The complete fixed-N R7 derivative formulas and their moment/local-flow hypotheses are explicitly imported; the new estimate is applied after validity is established. |
| A formal singular energy identity or atom was used on a trajectory. | R6 supplies the fixed-N stopped-to-global passage. This argument uses only the strictly sub-Coulomb density and its bounded negative part. |
| The total-force square was split into positive pair squares. | It is retained as a whole in (5.6); its negative sign allows discarding it. The pair moment comes from the Laplacian density. |
| Product Haar was used at positive times. | Only actual exchangeability, initial iid energy zero, deterministic floor, and the actual energy identity are used. |
| Pair deletion or a background derivative was lost. | Equation (6.4) derives both from the literal statistic; no singular diagonal is evaluated. |
| A covariance sign was presumed. | Finite-sum Cauchy–Schwarz bounds the complete square. The cross bound uses total variation and probability-time Cauchy–Schwarz. |
| A source candidate was silently promoted after an unseen audit. | All input statuses remain as issued. The full result is explicitly conditional on the supplied modules; no unseen verdict was read. |
| A strict range was enlarged to an endpoint. | Section 7 proves every exponent test and states why both Coulomb mechanisms fail. |

The reconstruction supplies the entire frozen quantitative assertion as a conditional theorem with no additional unresolved lemma in the new implication. No admissible counterexample was found. This is the strongest justified disposition; it is not an independent certification of all source modules and is not a hostile-audit pass.

Root must first verify the seals, then compare this argument with the withheld constructor, and only then commission or assess a separate fresh hostile review. Any discrepancy should cite the first mathematical line and its source assumptions. Canonical state integration belongs to root; no state or cumulative memorandum was edited in this worktree. The next campaign gap outside this assertion remains the singular residual and full fluctuation closure, not a consequence silently obtained from noise decay.
