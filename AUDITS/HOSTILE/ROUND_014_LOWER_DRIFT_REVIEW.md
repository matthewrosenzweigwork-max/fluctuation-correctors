# Round 014 lower-drift hostile review — TASK-076

2026-09-18 UTC. **CONDITIONAL PASS for the complete frozen THM-035 assertion and the constructor's stronger mathematical claims. The separate rendering erratum is accepted.** No admissible counterexample or first failed line was found in the new conditional implication. This is a fresh hostile review of the supplied constructor, not a statement-only blind reconstruction and not certification of its earlier premises. Root alone compares the separate reviews and assigns campaign status.

The target is `THEOREMS/THM-035_LOWER_DRIFT_CONTRACTIONS.md`, SHA-256 `74cb2e2a7e697f11451da160bb0eb668919a8e9d70e1d1a4a0d07f811766d4fb`. The entire constructor is `MEMORANDA/ROUND_014_LOWER_DRIFT_CONTRACTIONS.md`, SHA-256 `266d8fe2cdbaa4111c3f5b515ed22c791f291508987618de525c49f9c67d3f14`; its separate erratum has SHA-256 `403b3444eb22ff631c00c4d9a17bbd750e3482ea9128eb30e7fedcbad3fd243a`. Locations below refer to those immutable input bytes. No input was repaired in place.

The new estimate needs the genuine inverse's admitted R12 uniform weighted gradient estimate and the admitted R8 actual representatives/domain. Its new constant has no density factor, energy floor, extra power of particle number, or positive-noise requirement. Both lower coefficients and both response slots survive a direct finite-label reconstruction. The reduction removes only the lower drift: it does not show the cubic small, nor establish a limiting law.

## 1. Review boundary, assertion, and negation

The assigned branch is `codex/hocf-r014-lower-hostile` in `/Users/matthewrosenzweig/.codex/worktrees/hocf-r014-lower-hostile`, created from the specified commit `072cab684b9ce41855ead6c48f435c8fc184ec35`. All 27 allowlisted files were verified against the controlling manifest before copying and after copying. All 27 were read in full. No current reconstruction, other current audit, R13/R15 mathematical result, canonical state/history file, memory file, prior checker program, external source, or child agent was consulted. Detailed ambient exposure, including the automatic checkout subject and injected high-level memory summary, is disclosed in the companion preflight; neither supplied mathematical evidence. The constructor's own narrative was read, as required for hostile review.

Fix integer \(d\ge3\), \(0<s<d-2\), \(3s<2d-2\), finite nonnegative \(T,L,\nu_*\), and a fixed smooth real terminal test \(h\). For every \(N\ge2\) and \(0\le\nu\le\nu_*\) such that \(\nu N^{2/(s+2)}\le L\), use the specified genuine homogeneous symmetric terminal-zero inverse \(\Phi\), its actual Fourier test, and both responses. The actual particle preparation is iid unit Haar, independent of the Brownian drivers. Write

\[
p=s+2,\quad q_-=\max(1,s/2),\quad
q_+=\min(d/2,d-s-1,s+1),\quad q=(q_-+q_+)/2,
\]

\[
b=\min(1/\nu,1),\quad \sigma=\sqrt{Nb}\quad(\nu>0),
\qquad b=1,\quad\sigma=\sqrt N\quad(\nu=0).
\]

The contraction, with the actual R8 representatives, is

\[
B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi,\quad
g_t(x)=\int B\Phi_t(x,y)dy,\quad c_t=\int g_t(x)dx,
\]

\[
\ell_N(t)=N^{-1}\rho_t[g_t]+(2N)^{-1}c_t,
\qquad \rho_t=\eta_N(t)-dx.
\]

The primary assertion is existence/admissibility of this \(q\), positivity of \(\kappa_q=(2q-s)/(2p)\), and a fixed-data constant with

\[
\sigma\,\mathbb E\int_0^T|\ell_N(t)|dt
\le C\sqrt b\,N^{-\kappa_q},
\tag{H1}
\]

together with the critical-range inclusion and the stated integrated-residual equivalence. Its negation is an admitted fixed-data family defeating every such uniform constant, or a failure of one of the stated admissibility, inclusion, coefficient, or reduction assertions. A failure outside the allowed range, a counterexample for a different inverse, or divergence of an upper majorant at an excluded endpoint is not that negation.

The two load-bearing premises remain conditional exactly as issued:

1. **Gradient premise G:** THM-033 lines 5–10 and R12 memorandum lines 9–14, 25–85, for the exact R7 weights, provide
   \[
   \sup_{t,x\ne y}|\nabla_{x,y}\Phi_t(x,y)|/w_q(x-y)
   \le A_q N^{(s+1-q)/(s+2)}.
   \tag{G}
   \]
   Its constant is uniform in the admitted \(N,\nu\) family, including zero noise. It is not a fixed-\(N\) R7 constant. The R12 noise bracket, occupation proof, and R10 energy estimate are not needed.
2. **Domain premise D:** THM-028 lines 5–19 and the complete R8 memorandum supply local classical derivatives, the genuine continuous Haar contractions, the classical pair equation, the actual singular-particle Itô identity, and finite expected absolute time integrals of every drift term. Constants in this premise may depend on \(N\). They are used to define and identify terms, not to infer uniform smallness.

The supplied earlier kernel, auxiliary inverse, and particle realization modules retain their own frozen assumptions and status qualifications. Reading their source proofs and checking the interface does not independently certify those entire modules.

## 2. Normalization and exponent preflight

The unit Haar convention and ordered-label normalization are R1 model lines 11–42 and R1 algebra (1.3), (1.4), (3.1)–(3.7). In particular \(P_N=U_2/2\), all denominators are powers \(N^k\), and symmetrization is the average over six permutations.

The supplied R4 heat proof, lines 69–120, fixes

\[
\widehat g(k)=c_{d,s}|k|^{s-d},\qquad
c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},
\qquad K=-\nabla g.
\]

The normalization can be checked without a remembered source theorem. Put \(a=(d-s)/2\) and \(A=4^a\pi^{d/2}/\Gamma(s/2)\). Integrating the nonzero heat Fourier coefficient gives \(A\Gamma(a)(4\pi^2|k|^2)^{-a}=c_{d,s}|k|^{s-d}\). In the Euclidean heat integral, the substitution \(v=r^2/(4t)\) gives the coefficient

\[
A(4\pi)^{-d/2}4^{s/2}\Gamma(s/2)=1.
\]

The complete supplied proof controls the remaining lattice terms at small heat times and the large-time tails with every local derivative. Thus its local input is precisely

\[
g(z)=|z|^{-s}+H_s(z),\quad H_s\in C^\infty(B_{1/3}),\quad
K(z)=s z|z|^{-s-2}-\nabla H_s(z).
\tag{H2}
\]

The R5 source addendum lines 7–20 correctly points to this complete local lemma and permits enlarging the common lower-divergence constant. The symmetry clarification means pair exchange, not Haar self-adjointness. No local expansion was silently inferred from the short THM-021 card alone.

For \(D=\operatorname{div}K\), the homogeneous responses are

\[
R_xv=-\int v(x+w,y)D(dw),\qquad
R_yv=-\int v(x,y+w)D(dw).
\tag{H3}
\]

Since \(\widehat D(k)=4\pi^2c_{d,s}|k|^{s+2-d}\) for nonzero \(k\), the response multiplier in each slot is negative. Consequently the constructor's Fourier test (1.4), lines 68–82, has the correct decaying backward multiplier. Each fixed spatial derivative is uniformly bounded by the corresponding absolutely summable Fourier seminorm of the fixed smooth \(h\). This uses neither a varying terminal test nor a derivative bound for an unknown inhomogeneous solution.

To attack the chosen interval, compare every member of \(\{1,s/2\}\) with every member of \(\{d/2,d-s-1,s+1\}\). The comparisons with 1 follow from \(d>2\), \(s<d-2\), and \(s>0\). For \(s/2\), the only extra restriction is

\[
s/2<d-s-1\quad\Longleftrightarrow\quad3s<2d-2.
\]

Therefore the maximum is strictly below the minimum, and the midpoint satisfies

\[
1<q<d/2,\quad q<s+1,\quad q<d-s-1,\quad q>s/2.
\tag{H4}
\]

These are respectively the R12 lower/upper admissibility requirements, its source-weight restriction, force-gradient integrability, and positive decay. The additional R8 choice \(q_2=(q+1+d)/2\) is legal because \(q+1<d\); it obeys \(q+1<q_2<d\). No R8 constant is thereby made uniform in particle number.

## 3. Singular product, every slice, and the actual representative

Use \(R=1/16\) and precisely the R7 weight \(w_q=w_1^q\), with \(w_q(z)=|z|^{-q}\) on \(B_R\setminus\{0\}\). Set

\[
\alpha=(s+1-q)/p,\quad m=s+1+q<d,\quad
\omega_{d-1}=|\mathbb S^{d-1}|,
\]

\[
H_0=\sup_{|z|\le R}|\nabla H_s(z)|,\qquad
M_{K,q}^{\rm out}=\sup_{z\notin B_R}|K(z)|w_q(z),
\]

\[
J_q^*=
\frac{s\omega_{d-1}R^{d-s-1-q}}{d-s-1-q}
+\frac{H_0\omega_{d-1}R^{d-q}}{d-q}
+M_{K,q}^{\rm out}.
\tag{H5}
\]

Every denominator is positive by (H4). The exact inner radial majorant is
\(s r^{-s-1-q}+H_0r^{-q}\), integrated against \(\omega_{d-1}r^{d-1}dr\). The complement has Haar mass at most one. Thus

\[
\int|K(z)|w_q(z)dz\le J_q^*<\infty.
\tag{H6}
\]

The Euclidean product gradient norm in G and R7 is material: the vector \((K,-K)\) has norm \(\sqrt2|K|\). Hence, pointwise off the diagonal,

\[
|B\Phi_t(x,y)|\le\sqrt2 A_qN^\alpha|K(x-y)|w_q(x-y).
\tag{H7}
\]

Put \(D_q=\sqrt2 A_qJ_q^*\). Translation invariance of Haar and (H6) prove, for every remaining coordinate,

\[
\int|B\Phi_t(x,y)|dy\le D_qN^\alpha,\qquad
\int|B\Phi_t(x,y)|dx\le D_qN^\alpha.
\tag{H8}
\]

In particular \(\|g_t\|_\infty,|c_t|\le D_qN^\alpha\), and absolute Fubini identifies \(c_t=\int g_t\). Merely knowing \(q<d\) or \(2q<d\) would not prove this product bound. The constructor uses the stronger inequality it actually needs.

Here is the representative check, with the limit order explicit. For \((t_n,x_n)\to(t,x)\), fix small \(\delta<R/3\). When \(x_n\) is sufficiently close to \(x\), the integrals over the union of the two radius-\(\delta\) balls around \(x_n\) and \(x\) are at most a fixed multiple of

\[
A_qN^\alpha\left(\delta^{d-s-1-q}+\delta^{d-q}\right).
\tag{H9}
\]

For each integrand, that union is contained in a radius-\(3\delta\) ball about its own singular point. On the common complement, premise D gives joint continuity of the off-diagonal derivatives on a compact set and a fixed integrable bound. First let \(n\to\infty\) there, then let \(\delta\downarrow0\). This proves continuity of the actual slice, including one-sided time endpoints; integrating gives continuity of \(c_t\). The same integral defines the R8 contraction, so the continuous representatives agree pointwise. No Haar equivalence class is evaluated at a potentially exceptional empirical point.

Changing values on the true pair diagonal changes none of these integrals. Conversely, this observation does not license assigning a diagonal derivative or inserting a diagonal value in the singular generator. The proof makes no such insertion. No new regularization limit or singular Itô formula is required for (H6)–(H9); the actual singular-domain identity remains premise D.

## 4. Independent reconstruction of every force coefficient

This derivation starts from the finite-particle observable rather than a product-measure overlap formula. Suppress time and set \(a(x)=\int\nabla_x\Phi(x,y)dy\), \(p(x,y)=\nabla_x\Phi(x,y)\), and

\[
P_N[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(x_i,x_j)
-\frac1N\sum_i\int\Phi(x_i,y)dy+\frac12\iint\Phi,
\qquad D_2[v]=N^{-2}\sum_{i\ne j}v(x_i,x_j).
\]

Differentiating at a collision-free configuration gives

\[
\nabla_iP_N[\Phi]=N^{-2}\sum_{j\ne i}p(x_i,x_j)-N^{-1}a(x_i).
\tag{H10}
\]

Multiplying by the actual force \(N^{-1}\sum_{k\ne i}K(x_i-x_k)\) and summing yields

\[
Q=N^{-3}\sum_{i\ne j}\sum_{k\ne i}K(x_i-x_k)\cdot p(x_i,x_j)
-N^{-2}\sum_{i\ne k}K(x_i-x_k)\cdot a(x_i).
\tag{H11}
\]

The \(k=j\) summands are exactly

\[
N^{-3}\sum_{i\ne j}K(x_i-x_j)\cdot p(x_i,x_j)
=\frac1{2N}D_2[B\Phi].
\tag{H12}
\]

Pair symmetry turns the swapped gradient into the other slot, while force oddness supplies its minus sign. The distinct-label condition is retained throughout.

For the three-distinct part define \(C\Phi=\operatorname{Sym}_3[K(x-z)\cdot p(x,y)]\). Its six terms are

\[
\begin{aligned}
6C\Phi={}&K(x-z)\cdot p(x,y)+K(x-y)\cdot p(x,z)\\
&+K(y-z)\cdot p(y,x)+K(y-x)\cdot p(y,z)\\
&+K(z-y)\cdot p(z,x)+K(z-x)\cdot p(z,y).
\end{aligned}
\tag{H13}
\]

At fixed distinct \(x,y\), the two possible integration singularities in \(z\) are separated. Each is integrable: the force has power \(s+1<d\), the gradient has power \(q<d\). In the full triple Haar integral the two independent relative variables can be integrated separately. Thus the following background integrations are legitimate without evaluating \(p(x,x)\).

The first and third terms of (H13) vanish after integrating \(z\), because \(\int K=0\). The second and fourth give
\(A_a(x,y)=K(x-y)\cdot(a(x)-a(y))\). The last two give the two different integrated-gradient responses, which agree off diagonal with (H3) by premise D. Therefore

\[
C_1=(A_a+R_x\Phi+R_y\Phi)/6.
\tag{H14}
\]

Write \(v(x)=\int K(z-x)\cdot a(z)dz\). Direct integration shows

\[
\int A_a(x,y)dy=v(x),\quad
\int R_x\Phi(x,y)dy=v(x),\quad
\int R_y\Phi(x,y)dy=0,
\]

\[
C_2=v/3,\qquad C_0=0,\qquad (R\Phi)_\mu=v,\quad\iint R\Phi=0.
\tag{H15}
\]

The correct literal cubic is

\[
U_3[F]=N^{-3}\sum_{\substack{i,j,k\\\text{pairwise distinct}}}F(x_i,x_j,x_k)
-3N^{-2}\sum_{i\ne j}F_1(x_i,x_j)+3N^{-1}\sum_iF_2(x_i)-F_0.
\tag{H16}
\]

All triples in this display are ordered. If \(T_3\) denotes its first sum for \(F=C\Phi\), equations (H14)–(H15) give

\[
U_3[C\Phi]=T_3-\tfrac12D_2[A_a+R\Phi]+\eta_N[v],
\quad P_N[R\Phi]=\tfrac12D_2[R\Phi]-\eta_N[v].
\]

The last term of (H11) is \(-D_2[A_a]/2\). Hence

\[
Q=U_3[C\Phi]+P_N[R\Phi]+\frac1{2N}D_2[B\Phi].
\tag{H17}
\]

Subtract the full inverse's exact internal operator contribution \(P_N[B\Phi]/N\). Expanding the pair statistic, without a diagonal identity, gives

\[
\frac1{2N}D_2[B\Phi]-\frac1NP_N[B\Phi]
=\frac1N\eta_N[g]-\frac1{2N}c
=\frac1N\rho[g]+\frac1{2N}c.
\tag{H18}
\]

Thus the centered scalar has positive coefficient \(1/(2N)\), even though the regrouped empirical expression has a negative scalar. Both response slots have coefficient one. There is no leftover \(N^{-2}\) force term. Replacing the pair denominator by a falling factorial, halving a response, or dropping the scalar changes the identity.

Independent diffusion has no extra thermal trace here. In the particle-particle sum its two labels are distinct, so Brownian cross variation is zero. For the mixed term, premise D gives \(\int\Delta_y\Phi(x,y)dy=0\) and \(\int\Delta_x\Phi(x,y)dy=\Delta_x\int\Phi(x,y)dy\); the scalar Laplacian integral vanishes. Consequently the time-diffusion contribution is precisely \(P_N[(\partial_t+\nu\Delta_{x,y})\Phi]\). The supplied actual Itô passage and the classical inverse equation then give

\[
dP_N[\Phi_t]=\{-P_N[J_t]+U_3[C\Phi_t]+\ell_N(t)\}dt+dM_t^2.
\tag{H19}
\]

This last singular-domain passage is conditional on D; finite-label algebra alone would not justify it. At \(N=2\), \(T_3=0\), while (H16)'s background terms usually remain nonzero.

## 5. The stronger bound, all constants, and the actual law

By the empirical form in (H18), for every empirical probability measure,

\[
|\ell_N(t)|\le N^{-1}\eta_N[|g_t|]+(2N)^{-1}|c_t|
\le\tfrac32D_qN^{\alpha-1}.
\tag{H20}
\]

This is an elementary pointwise estimate on a continuous one-body function. It does not use a positive-time iid law or even the actual particle distribution. The exact regrouping improves the naive separate bound on \(\rho[g]\); it does not remove either contraction.

Since

\[
\alpha-\tfrac12=\frac{s-2q}{2(s+2)}=-\kappa_q,
\]

the pathwise estimate is

\[
\sigma\int_0^T|\ell_N(t)|dt\le
\frac{3\sqrt2}{2}TA_qJ_q^*\sqrt b\,N^{-\kappa_q}.
\tag{H21}
\]

This agrees with the constructor's constant (5.3), including \(\sqrt2\), \(3/2\), the coefficient \(s\), sphere area, both radial denominators, and the complement's volume bound. Every quantity in the additional constant depends only on the fixed data and weights. The uniformity of \(A_q\) is exactly G. No older constant depending on \(N\), density supremum, selected diffusivity, or cutoff is inserted into (H21).

The actual R6/R8 paths meet the domain/noncollision hypotheses almost surely under their supplied law. The lower integrand is measurable by the continuous representative, and its time integral is deterministically bounded. Tonelli and expectation therefore give (H1), with no mean-to-concentration inference. The stronger pointwise bound is on the lower contraction only; it does not define the singular pair Itô observable at colliding configurations or transfer a fluctuation theorem to another law class.

The nonessential one-body assertion at constructor line 348 is correct under the supplied realization: translating every initial coordinate by the same fixed torus vector and retaining the Brownian increments translates the path by uniqueness, since the drift uses only differences. Iid Haar preparation is invariant under that translation. Each time marginal is therefore invariant under every torus translation, hence Haar. This does not imply independence of two or more particles and is not needed for (H21).

At \(\nu=0\), use \(b=1\) as declared; both G and D cover that endpoint and (H21) contains no reciprocal or noise division. At \(T=0\) the integral is zero. For constant \(h\), the source vanishes and uniqueness of the terminal-zero full inverse gives \(\Phi=0\). The report never needs or asserts scalar noncancellation for the genuine inverse: retaining the scalar is valid even if additional structure happens to make it zero.

## 6. Critical inclusion and the two integral norms

Suppose \(0<s<d-2\) and \(s(s+2)<2d\). If \(s\le2\), then
\(2d-2>2s+2\ge3s\). If \(s>2\), then

\[
2d-2>s(s+2)-2=3s+(s-2)(s+1)>3s.
\]

Thus every strict R12 critical decay exponent lies in the new lower range. No equality endpoint is added. For a positive finite critical limit, put \(\theta=1-s/d\) and \(\lambda_N=\beta_NN^{-\theta}\to\lambda\in(0,\infty)\). Then

\[
\nu_N=\lambda_N^{-1}N^{-\theta}\to0,\qquad
\nu_NN^{2/(s+2)}=
\lambda_N^{-1}N^{s(s+2-d)/(d(s+2))}\to0.
\tag{H22}
\]

The last exponent is negative because \(s+2<d\). The sequence eventually fits any fixed positive \(L,\nu_*\). A zero choice of either bound admits no positive-noise critical sequence, as the constructor correctly states. Since \(0<b_N\le1\), (H21) tends to zero in every admitted fixed-data sequence with \(N\to\infty\).

The temperature examples at constructor line 388 are correct: for \(d=3,s=1/2\), critical \(\beta_N=N^{5/6}\) makes the old floor expression \(N^{1/6}\); \(\beta_N=N^{3/4}\) is fully subcritical but makes that old expression \(N^{1/12}\). None of these conditions is substituted for another.

Let \(u_N(t)=U_{3,t}[C\Phi_t]\), and define exactly

\[
A_N=\sigma_N\int_0^T u_N(t)dt,\qquad
Z_N=\sigma_N\int_0^T(u_N(t)+\ell_N(t))dt.
\]

Premise D gives finite expected absolute time integrals at each fixed \(N\), so both random variables are in \(L^1\). With \(\varepsilon_N=C_*\sqrt{b_N}N^{-\kappa_q}\), the actual difference satisfies

\[
\mathbb E|Z_N-A_N|\le\sigma_N\mathbb E\int|\ell_N|\le\varepsilon_N,
\qquad
\big|\mathbb E|Z_N|-\mathbb E|A_N|\big|\le\varepsilon_N.
\tag{H23}
\]

Since \(\varepsilon_N\to0\), vanishing of either integrated \(L^1\) norm is equivalent to vanishing of the other. This proves both the card's critical claim and the constructor's stronger bounded-rescaled-diffusion reduction. It proves neither norm small.

The additional claims at constructor line 412 also survive. Pointwise integration gives

\[
\mathbb E\sup_{0\le r\le T}\left|\sigma_N\int_0^r\ell_N(t)dt\right|
\le\varepsilon_N.
\]

For the stronger absolute-time-integral norms the pointwise reverse triangle inequality gives

\[
\left|\sigma_N\mathbb E\int|u_N+\ell_N|-
\sigma_N\mathbb E\int|u_N|\right|\le\varepsilon_N.
\tag{H24}
\]

This is a separate equivalence. An absolute value outside a time integral cannot be moved inside it. For example, the deterministic function equal to 2 on the first third of \([0,1]\) and to \(-1\) on the remaining two thirds has signed integral zero and absolute integral \(4/3\). The constructor explicitly avoids that false inference.

## 7. Falsification tests and the separate rendering erratum

The independently written standard-library diagnostic is in the companion packet. It constructs rational Laurent polynomials from scratch; differentiates the entire particle observable directly; evaluates the literal subset/injective-label statistic; and computes the response from minus-divergence convolution. It does not import a prior checker or a constructor's numeric outputs. All Fourier coefficients, not merely finitely many evaluated configurations, are compared for each finite test case.

The physical convention is stated in the script and README: \(\partial_j=2\pi i\delta_j\), and the physical real odd force is \(i\) times the formal rational odd Laurent force. All formal force expressions multiply by \(-2\pi\); the separately checked diffusion identity multiplies by \(-4\pi^2\). This restores every physical derivative factor and does not alter relative coefficients.

The final run passed **236,686 exact assertions**, including 84 full finite-label parameter cases, 27,716 admitted rational exponent cases, 12,384 strict critical exponent cases, and 34,875 elementary pathwise-constant probes. It detected all nine deliberately wrong coefficient alternatives: omitted scalar, flipped scalar sign, halved centered lower term, either omitted response, halved repeated-pair contribution, falling-factorial pair normalization, doubled cubic, and discarded two-particle background cubic. Dimensions 3 through 30 and rational denominators through 17 were used for the exponent probes. No randomness, floating tolerance, singular inverse approximation, or analytic-limit certification is involved.

One explicit physical smooth probe in the diagnostic is

\[
K(z)=-\tfrac65\sin(4\pi z),\qquad \Phi(x,y)=\cos(4\pi(x-y)).
\]

It is an odd gradient force from the even potential \(-3\cos(4\pi z)/(10\pi)\). Direct integration gives

\[
g=c=24\pi/5,\quad \rho[g]=0,\quad
\ell_N=12\pi/(5N),\quad
U_{3,2}[C\Phi]=-\tfrac{6\pi}{5}\cos(4\pi(x_1-x_2)).
\]

Thus deleting the scalar or the two-particle background cubic fails an exact universal coefficient test. This smooth probe is not the genuine singular inverse and asserts nothing about its scalar cancellation. Additive and mixed pair modes independently detect the centered lower coefficient and response slots.

The boundary attacks agree with the constructor's mathematical interpretation:

| Attack | Verified implication |
|---|---|
| \(d=7,s=4\) | The interval collapses at \(q=2\), the decay power is zero, and the product radial exponent is \(-1\). The strict proof cannot cross this endpoint. |
| \(d=8,s=5\) | The lower endpoint exceeds the upper one; midpoint \(9/4\) gives negative decay and nonintegrable product majorant. This is outside the theorem. |
| \(q=d-s-1\) | The force-gradient majorant has logarithmic divergence. |
| \(q=d/2\) | The squared gradient weight has logarithmic divergence; this is a different domain restriction. |
| \(q=s/2\) | The displayed decay power is zero. |
| \(s=0\), or \(d=3,s=1\) | The selected interval closes; no logarithmic normalization or Coulomb endpoint follows. |
| Fixed positive \(\nu\), \(N\to\infty\) | The rescaled diffusion is unbounded, so G's uniform constant is unavailable for that family. |
| \(d=12,s=4\) | R12's critical decay equality is excluded there, while the lower estimate's interval remains open. This is not a lower-drift counterexample. |

These majorant failures do not prove necessity for an improved structural theorem. They test the exact strict restrictions being asserted.

**Rendering finding TASK076-E01 — accepted separate erratum, low severity, high confidence.** Constructor lines 267–268 contain malformed TeX text in the sum subscript. The literal issued bytes do not constitute a clean TeX rendering. Erratum line 5 correctly identifies the intended ordered pairwise-distinct sum; R1 model lines 29–38, R1 algebra lines 69–80, R8 lines 641–650, and the coefficient derivation (H13)–(H18) all select that same interpretation. In particular this is not permission to use an unordered sum or a different denominator. Equation (H16) is a readable rendering in this new review. Required repair for any future rendered synthesis: use the explicitly ordered, pairwise-distinct subscript and preserve every coefficient. No mathematical repair is required for the input plus its separate erratum, and no issued input or checksum was edited.

The constructor's assertions about its own prior checker execution/packet at lines 416–436 are not independently reproduced: those checker and result files were deliberately outside this dossier. Their listed mathematical challenges were re-evaluated above; this review's confidence comes from the derivations and its separately written diagnostic, not from unseen execution records.

## 8. Per-claim dispositions and exact remaining obligation

Claim identifiers below are local to TASK-076 and allocate no canonical theorem or audit identifier.

| Local claim | Exact constructor/card location | Disposition and reason |
|---|---|---|
| C01: complete fixed-family assertion and negation | Card 5–16; constructor 9–66 | CONDITIONAL PASS. The fixed data, actual inverse, law, and logical negation are retained in Section 1. |
| C02: kernel, Fourier test, both responses | Constructor 68–97 | PASS FROM SUPPLIED PREMISES. Constants and signs checked in Section 2; no altered inverse. |
| C03: midpoint, all admissibility inequalities, positive decay, R8 exponent | Constructor 101–125 | PASS. The six comparisons prove strict admissibility and the compatible second exponent. |
| C04: exact R12 uniform input and weight | Constructor 127–138 | CONDITIONAL INPUT CORRECTLY USED. G has precisely the claimed scope; no fixed-particle constant is promoted. |
| C05: product integrability and every additional constant | Constructor 142–195 | CONDITIONAL PASS. Equations (H5)–(H8) recompute the singular power, both denominators, sphere area, and product-norm factor. |
| C06: every-coordinate slices and actual continuous representatives | Constructor 198–208 | CONDITIONAL PASS. The moving-ball proof in Section 3 supplies pointwise identification, including endpoints. |
| C07: raw generator, repeated labels, all cubic/response backgrounds | Constructor 212–281 | PASS OF THE ALGEBRA, with D for singular domains. Equations (H10)–(H17) retain all six permutations and both responses. |
| C08: exact centered lower/scalar coefficients and sign | Constructor 283–294 | PASS. Equation (H18) gives both forms exactly, without a diagonal extension or extra particle-number term. |
| C09: actual singular Itô identity and no extra thermal trace | Constructor 296–303 | CONDITIONAL PASS. Algebra is checked; R8's complete domain and limit passage remain premises. |
| C10: stronger pathwise bound, explicit constant, expectation | Constructor 307–346 | CONDITIONAL PASS. Equation (H21) has exactly the claimed constant and is uniform in the selected diffusivity and particle law. |
| C11: actual one-body Haar marginal, without evolved independence | Constructor 348 | PASS FROM SUPPLIED REALIZATION. Common translations and uniqueness suffice; the estimate does not need this assertion. |
| C12: zero noise, zero horizon, constant terminal test | Constructor 350 | CONDITIONAL PASS. No division by zero or missing terminal value occurs. |
| C13: all strict R12 critical exponents and critical temperature family | Card 14; constructor 354–386 | PASS. Section 6 proves both exponent inclusion and eventual bounded rescaled diffusion; zero bounds are treated correctly. |
| C14: distinction of the three temperature conditions | Constructor 388 | PASS. The displayed example powers are exact; the proof uses neither of the other two conditions. |
| C15: integrated cubic-plus-lower iff cubic, including every admitted fixed-data sequence | Constructor 392–410 | CONDITIONAL PASS. Finite-particle integrability is D, and (H23) supplies the quantitative perturbation. No cubic smallness is proved. |
| C16: absolute-time-integral norm and supremum of lower primitive | Constructor 412 | CONDITIONAL PASS. The two separate inequalities in Section 6 justify both stronger claims without conflating the norms. |
| C17: listed coefficient/range falsification interpretations | Constructor 418–434 | PASS OF THE LISTED MATHEMATICAL INTERPRETATIONS. Independent probes and analytic boundary arguments are in Section 7. Prior checker execution remains unverified and unused. |
| C18: ordered-sum rendering interpretation | Constructor 267–268; separate erratum 3–7 | ERRATUM ACCEPTED. The source bytes are malformed, but the mathematical reading is unambiguous and matches the frozen convention; TASK076-E01 records the required future rendering. |
| C19: no new unconditional premise, no cubic/law promotion | Constructor 438–452 | AGREED WITH ITS CONDITIONAL QUALIFICATION. This review finds no failed line in the new implication, but certifies no earlier source and grants no campaign promotion. |

**First failing line:** none found within the frozen conditional implication. If the gradient or full-domain premise were removed, the first unavailable steps would be (G), corresponding to constructor lines 127–136, or the actual representative/domain uses at lines 198–208 and 296–303. The present review does not discharge those external premises.

**Strongest surviving conclusion:** conditional on the issued genuine-inverse gradient and complete-domain statements, the exact lower functional satisfies the deterministic bound (H21), hence (H1), the expected supremum bound for its primitive, and the two separately stated residual equivalences. The exact remaining mathematical obligation for drift closure is smallness of the actual integrated cubic with the specified centering and norm. No admissible cubic counterexample or cubic estimate is supplied here.

**Required repair:** no mathematical repair to THM-035 or to the constructor's stronger claims was found. The separate rendering erratum must accompany use of the original (4.6), and future standalone rendered work must use readable ordered-distinct notation. Earlier premise status and cubic smallness remain unchanged.

## 9. Verification and sealed handoff

The companion directory is `AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC`. It contains the full 27-input frozen copy, source/exposure preflight, README, newly written diagnostic, exact results, verification record, input and output seals, archive, and archive verification. The diagnostic command was:

```text
python3 AUDITS/HOSTILE/ROUND_014_LOWER_HOSTILE_ARTIFACTS_20260918_044046_UTC/exact_hostile_diagnostic.py
```

It passed 236,686 exact assertions and detected nine coefficient mutations. The final verification record identifies the output hashes, archive membership/CRC/digest checks, scoped worktree checks, and text checks. All mathematical artifacts here are Markdown; no TeX source was created or edited, no rendered-layout certification is claimed, and the final handoff contains no mathematical LaTeX. The rendering erratum was checked as source and mathematical interpretation, not by pretending the issued malformed source compiled.

Only the assigned worktree and review packet were written. No canonical root file or ledger, historical source, issued input, existing audit, commit, push, installation, external service, or child agent was modified or used. The packet is issued immutable. Any later correction requires a separately named superseding artifact. Root alone compares/promotes; this bounded hostile review stops at the sealed handoff.
