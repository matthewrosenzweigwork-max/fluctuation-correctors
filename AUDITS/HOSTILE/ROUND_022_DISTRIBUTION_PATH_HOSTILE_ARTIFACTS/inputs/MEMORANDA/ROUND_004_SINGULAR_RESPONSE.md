# Round 004: finite-measure Riesz response and smooth pair propagation

2026-09-17 UTC. TASK-034. Constructor: `/root/r004_response`, Astra Max. Branch: `codex/hocf-r004-response`. Worktree: `/Users/matthewrosenzweig/Library/CloudStorage/GoogleDrive-mrosenz2@andrew.cmu.edu/My Drive/Git/fluctuation-correctors-r004-response`. Base: published commit `52bda5d0d24067b051c6fe9763f2a78e7599e593`.

Mathematical status: **PROVED_CANDIDATE** for the assertions explicitly stated below. Audit status: **SELF_CHECKED**, requiring a separate reconstruction and hostile review before promotion. Source status: **SELF_CONTAINED**, with the frozen Riesz definition and R1 response convention identified below. No literature or novelty claim is made.

The root's finite-measure mechanism was disclosed in TASK-034 and is not treated as a proved input. This context has not read either unsealed R4 diffusion proof, another worktree, or memory. The task card was copied byte-for-byte from the root and has SHA-256 `c4eb41591d160d8c56e2718ec83424345848f12a2f9ae7bab9e04a6561184a38`. Administrative instructions and permitted older inputs are frozen in `AUDITS/ROUND_004_SINGULAR_RESPONSE_INPUT_SHA256SUMS.txt`, whose SHA-256 is `3961cd34a78272c4f5ac859c47ee275abb4d828ffb4a1564d779e5d98a7f66b0`. The R3 iid and sharp-iid reports were searched only to locate the local heat representation; their probability conclusions are not inputs to this proof. The actual heat argument is R3 collision report, section 3, reconstructed below.

The bounded task's input isolation and single-writer instruction supersede the general first-launch instruction to read all ledgers. No canonical ledger, cumulative memorandum, historical input, or root file is edited. No commit, push, dependency installation, or child worker is used. Root integration and independent audit remain separate actions.

## 1. Exact assertions and spaces

Fix an integer \(d\geq3\), \(0<s\leq d-2\), the unit torus \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), and Haar measure \(dx\) of mass one. Fourier coefficients use \(e^{2\pi i k\cdot x}\). The kernel is the frozen even, real, zero-mean periodic Riesz kernel

\[
 \widehat g_s(0)=0,\qquad
 \widehat g_s(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}
 \frac{\Gamma((d-s)/2)}{\Gamma(s/2)}\quad(k\ne0).
 \tag{1.1}
\]

Set \(K=-\nabla g_s\) as a distribution; its integrable representative is identified below. Let \(\mu\in C^1(\mathbb T^d)\) be a nonnegative probability density and put

\[
 M_0=\|\mu\|_\infty,\qquad M_1=\|\nabla\mu\|_\infty,
 \qquad D=\operatorname{div}K,
 \qquad C_0=M_0\|D\|_{\mathrm{TV}}+M_1\|K\|_1.
 \tag{1.2}
\]

The gradient norm is the Euclidean vector norm. Unless explicitly marked otherwise, every \(L^2\) norm in this report uses Haar measure, on one or two copies of the torus. In particular the response assertion is on \(L^2(dx\,dy)\), not on an unspecified weighted space. No lower bound for \(\mu\) is used. The iid input space in THM-015 is instead \(L^2(\mu\otimes\mu)\); the distinction is retained in section 8.

Write \(B_b\) for actual bounded Borel functions with the pointwise supremum norm, rather than equivalence classes. TASK-034's primary assertion is the following conjunction.

1. \(K\in L^1\), \(D\) is a finite signed measure, and its singular part and torus compensation have the exact constants in (3.3) and (3.5).
2. The formulas

\[
\begin{split}
 R_x\Phi(x,y)
 &=-\int \mu(x+w)\Phi(x+w,y)\,D(dw)\\
 &\hspace{4mm}-\int K(w)\cdot\nabla\mu(x+w)\Phi(x+w,y)\,dw,\\
 R_y\Phi(x,y)
 &=-\int \mu(y+w)\Phi(x,y+w)\,D(dw)\\
 &\hspace{4mm}-\int K(w)\cdot\nabla\mu(y+w)\Phi(x,y+w)\,dw
\end{split}
\tag{1.3}
\]

define bounded operators on \(B_b\) and unique bounded extensions from smooth functions to Haar \(L^2\). Each norm is at most \(C_0\), and

\[
 \|R_x+R_y\|\leq C_R:=2C_0.
 \tag{1.4}
\]

They also induce bounded operators on the Haar \(L^\infty\) quotient. The sum preserves pair symmetry. The atom in \(D\) requires multiplication by \(\Phi(x,y)\), not a separately defined pair-diagonal trace.
3. With the frozen heat mollification \(g_{s,\varepsilon}=p_\varepsilon*g_s\), the corresponding responses converge strongly in Haar \(L^2\). This convergence is uniform over time-dependent backgrounds with common \(M_0,M_1\) bounds when applied to each fixed \(L^2\) input. For \(s<d-2\) the convergence holds in operator norm on both \(L^2\) and \(B_b\). At \(s=d-2\), operator-norm convergence in \(L^2\), or convergence for every bounded Borel input in supremum norm, is false in general.

The logical negation is one admissible choice of the stated data violating at least one of these assertions. The positive parts are proved in sections 2–5; section 7 gives explicit counterexamples to the stronger, excluded conclusions.

The secondary assertion concerns only the *smooth* mollified pair generator in section 6. It gives a propagation bound uniform in \(\varepsilon>0\), \(N\geq2\), and \(\nu\geq0\). It does not assert existence of singular particle trajectories, existence of a singular pair Markov propagator, convergence of the smooth propagators, or an evolved-law fluctuation estimate.

## 2. Source and normalization preflight

The precise R1 convention is `MEMORANDA/ROUND_001_ALGEBRA.md`, equations (3.1)–(3.3) and (7.1): the first response integrates \(K(z-x)\cdot\nabla_z\Phi(z,y)\mu(z)\,dz\), both responses have coefficient one, and the internal pair field has coefficient \(1/N\). No change of sign, unordered-pair convention, or extra factor of two is made here. The frozen model is `TASKS/ACTIVE/ROUND_001_MODEL.md`. R3 collision report, section 3, supplies the local heat construction; the necessary facts and constants are checked directly as follows.

For every \(0<p<d\), let

\[
 \alpha_p=(d-p)/2,\quad
 A_{d,p}=\frac{4^{(d-p)/2}\pi^{d/2}}{\Gamma(p/2)},\quad
 q_t(z)=(4\pi t)^{-d/2}e^{-|z|^2/(4t)},\quad
 p_t(z)=\sum_{n\in\mathbb Z^d}q_t(z+n).
\]

Unfolding the Gaussian integral gives \(\widehat p_t(k)=e^{-4\pi^2t|k|^2}\), \(p_t\geq0\), and \(\int p_t=1\). For \(t\geq1\), the Fourier series of \(p_t-1\) and every spatial derivative decay exponentially. For \(0<t\leq1\), \(\|p_t-1\|_1\leq2\). Hence the integral

\[
 g_p(z)=A_{d,p}\int_0^\infty t^{\alpha_p-1}(p_t(z)-1)\,dt
 \tag{2.1}
\]

converges in \(L^1\), has zero mean, and by Fubini has nonzero Fourier coefficients

\[
 A_{d,p}\frac{\Gamma(\alpha_p)}{(4\pi^2|k|^2)^{\alpha_p}}
 =c_{d,p}|k|^{p-d}.
 \tag{2.2}
\]

For \(z\ne0\) in Euclidean coordinates, substituting \(v=|z|^2/(4t)\) gives

\[
 A_{d,p}\int_0^\infty t^{\alpha_p-1}q_t(z)\,dt=|z|^{-p}.
 \tag{2.3}
\]

The coefficient in (2.3) is exactly one. On \(|z|<1/3\), subtract (2.3) from (2.1). At small times the nonzero lattice translates and all their derivatives have bounds by a power of \(t^{-1}\) times \(e^{-c/t}\); the subtracted constant is integrable against \(t^{\alpha_p-1}\). At large times the torus remainder decays exponentially and the whole-space term is bounded by a constant times \(t^{-p/2-1}\), with better decay after spatial differentiation. These bounds justify every spatial derivative on compact subsets of this ball. Thus

\[
 g_p(z)=|z|^{-p}+H_p(z),\qquad H_p\in C^\infty(B_{1/3}),
 \tag{2.4}
\]

and \(g_p\) is smooth away from the origin. These statements use local torus coordinates only. No global Euclidean distance representative or global smooth decomposition of a nonperiodic power is assumed.

Finite measures on the torus are determined by their Fourier coefficients: convolve the difference with \(p_t\); its absolutely convergent Fourier series is zero if all coefficients are zero, and test against continuous functions before sending \(t\downarrow0\). The same argument identifies distributions by their coefficients, using smooth tests. This justifies the Fourier identifications used in section 3 without importing a fractional-Laplacian theorem.

## 3. The distributional divergence and its exact compensation

From (2.4), for \(0<|z|<1/3\),

\[
 K(z)=s\frac{z}{|z|^{s+2}}-\nabla H_s(z).
 \tag{3.1}
\]

Since \(s+1<d\), this field is integrable. It is also the distributional negative gradient of \(g_s\): integration by parts outside \(B_r\) produces a boundary term bounded by a constant times \(r^{d-1-s}\), which tends to zero. Consequently \(K\) is an odd, integrable field; assigning an arbitrary value to \(K(0)\) changes none of the integrals here.

For a smooth periodic scalar test \(\psi\), integrate over the torus minus \(B_r\). The outward normal of the punctured domain on its inner boundary is \(-z/r\). Therefore

\[
\begin{split}
 -\int_{\mathbb T^d\setminus B_r}K\cdot\nabla\psi
 &=\int_{\mathbb T^d\setminus B_r}\psi\,\operatorname{div}_{\rm cl}K\\
 &\quad+s r^{d-s-2}\int_{\mathbb S^{d-1}}\psi(r\theta)\,dS(\theta)
   +O_\psi(r^{d-1}).
\end{split}
\tag{3.2}
\]

The error is the boundary flux of the smooth remainder. The left side converges absolutely because \(K\in L^1\). For \(s<d-2\), the classical singular divergence is the integrable density \(s(d-2-s)|z|^{-s-2}\), and the displayed boundary flux tends to zero. At \(s=d-2\), the classical singular divergence vanishes away from zero, while the flux tends to \((d-2)|\mathbb S^{d-1}|\psi(0)\). This proves the absence of an atom below the endpoint and its exact positive coefficient at the endpoint. In particular no principal value or unspecified collision boundary term remains.

### 3.1. Below the Coulomb exponent

If \(0<s<d-2\), set \(a_s=s(d-2-s)>0\). The preceding calculation first proves that \(D\) is an \(L^1\) density. The Fourier coefficients then identify it exactly:

\[
 D=a_s g_{s+2}(z)\,dz.
 \tag{3.3}
\]

Indeed, its coefficient at \(k\ne0\) is \(4\pi^2 c_{d,s}|k|^{s+2-d}\), and the gamma recurrence gives

\[
 \frac{4\pi^2c_{d,s}}{c_{d,s+2}}
 =4\frac{d-s-2}{2}\frac{s}{2}=s(d-2-s).
\]

Both sides have zero coefficient at zero. This is the exact periodic compensation, not a claim that the density is globally nonnegative. For an explicit decomposition at any \(0<R<1/3\),

\[
 D=a_s\mathbf1_{B_R}(z)|z|^{-s-2}\,dz+w_R(z)\,dz,
 \quad w_R\in L^\infty,\quad
 \int w_R=-s|\mathbb S^{d-1}|R^{d-s-2}.
 \tag{3.4}
\]

The density \(w_R\) is smooth on each side of the boundary of the ball; no derivative of its indicator is being taken. Alternatively choose a smooth nonnegative cutoff \(\chi\) supported in \(B_R\) and equal to one near zero. Then \(D=a_s\chi|z|^{-s-2}\,dz+w_\chi\,dz\), where \(w_\chi\) is globally smooth and \(\int w_\chi=-a_s\int\chi|z|^{-s-2}\). This is a globally valid smooth compensation statement.

Because \(g_{s+2}\) tends to positive infinity at zero and is smooth away from zero, it is bounded below. Thus \(D\geq-\kappa\,dz\) for a finite \(\kappa\) depending only on \(d,s\) under the frozen normalization. One permissible exact choice is \(\kappa=a_s\max(0,-\inf_{z\ne0}g_{s+2}(z))\). If a bound expressed entirely through the heat representation is preferred, put \(p=s+2\) and take

\[
 \kappa=a_s A_{d,p}\left(\frac1{\alpha_p}
 +\int_1^\infty t^{\alpha_p-1}
       \sum_{k\ne0}e^{-4\pi^2t|k|^2}\,dt\right).
\]

The first term uses \(p_t-1\geq-1\) on \((0,1)\); the second uses the absolutely convergent Fourier series. The integral is finite. Also \(\|D\|_{\mathrm{TV}}=a_s\|g_{s+2}\|_1<\infty\).

### 3.2. At the Coulomb exponent

If \(s=d-2\), define

\[
 c_d=(d-2)|\mathbb S^{d-1}|
 =\frac{2(d-2)\pi^{d/2}}{\Gamma(d/2)}
 =\frac{4\pi^{d/2}}{\Gamma((d-2)/2)}.
\]

The local calculation (3.2) proves that \(D\) has atom \(c_d\delta_0\) and a smooth remainder. The Fourier coefficient at every nonzero \(k\) is
\(4\pi^2c_{d,d-2}=c_d\), while the zero coefficient is zero. It follows that

\[
 D=c_d(\delta_0-dz),\qquad
 \|D\|_{\mathrm{TV}}=2c_d,\qquad D\geq-c_d\,dz.
 \tag{3.5}
\]

The two terms in (3.5) are mutually singular, which gives the stated total variation exactly. In either regime \(D(\mathbb T^d)=0\), also directly from \(\langle\operatorname{div}K,1\rangle=0\). A nonzero nonnegative measure cannot have this mass. Since its nonzero Fourier coefficients are positive, \(D\) is nonzero, so global nonnegativity is impossible.

The exact constant density \(-c_d\) in (3.5) uses the full frozen Fourier normalization. The coefficient-one local expansion alone would give an atom of mass \(c_d\) and a smooth compensating density of total mass \(-c_d\); it would not identify that density as constant after an arbitrary additional smooth periodic perturbation.

The endpoint here has \(s=d-2>0\). No logarithmic normalization or limit as \(s\downarrow0\) is used.

## 4. Bounded responses, equivalence classes, and the atom

For a finite signed measure \(\eta\), define in the first slot

\[
 (T_\eta F)(x,y)=\int F(x+w,y)\,\eta(dw).
\]

For bounded Borel \(F\), this integral exists for every \((x,y)\), is Borel measurable, and has supremum norm at most \(\|\eta\|_{\mathrm{TV}}\|F\|_\infty\). Measurability follows first for indicators of Borel rectangles and then for bounded Borel integrands by the monotone-class construction of parameter integrals. Formula (1.3) therefore defines actual bounded Borel outputs and proves (1.4) in \(B_b\).

For \(F\in L^2(dx\,dy)\), choose a Borel representative finite almost everywhere. Translation invariance and Cauchy–Schwarz against \(|\eta|\) give

\[
\begin{split}
 \int |T_\eta F(x,y)|^2\,dx\,dy
 &\leq \|\eta\|_{\mathrm{TV}}
   \int\int |F(x+w,y)|^2\,dx\,dy\,|\eta|(dw)\\
 &=\|\eta\|_{\mathrm{TV}}^2\|F\|_2^2.
\end{split}
\tag{4.1}
\]

The parameter integrals are absolutely finite for almost every \((x,y)\), also by Fubini since finite-volume \(L^2\) embeds into \(L^1\). If representatives differ on a product-null set \(E\), then

\[
 \int\int\mathbf1_E(x+w,y)\,dx\,dy\,|\eta|(dw)=0.
\]

Thus the output classes are independent of the representative, even when \(\eta\) has an atom. The same reasoning with \(|K(w)|\,dw\), using \(|K\cdot\nabla\mu|\leq|K|M_1\), yields

\[
 \|R_x\Phi\|_2\leq
 (M_0\|D\|_{\mathrm{TV}}+M_1\|K\|_1)\|\Phi\|_2.
 \tag{4.2}
\]

Interchanging slots proves the other bound and their sum. Smooth functions are dense in Haar \(L^2\), so this bounded extension is unique. The same null-set argument gives the \(L^\infty\) quotient extension. Uniqueness from smooth inputs is asserted in \(L^2\); continuous functions are not dense in all bounded Borel functions in supremum norm, and no such uniqueness claim is made for \(B_b\).

For \(\Phi\) smooth, apply (3.2) to \(\psi(z)=\mu(z)\Phi(z,y)\), translated by \(x\), and use the product rule. This test is \(C^1\), which is enough in the boundary argument; equivalently approximate it in \(C^1\) by smooth heat convolutions. The finite variation of \(D\) and integrability of \(K\) justify that approximation. It follows, pointwise for every \((x,y)\), that

\[
 R_x\Phi(x,y)=\int K(z-x)\cdot\nabla_z\Phi(z,y)\mu(z)\,dz,
 \tag{4.3}
\]

with the analogous identity for \(R_y\). In particular this is exactly the frozen R1 response. Equivalently the distributional product rule is
\(\operatorname{div}_z(\mu(z)K(z-x))=\mu(z)D(d(z-x))+K(z-x)\cdot\nabla\mu(z)\,dz\).

At Coulomb, (1.3) reads explicitly

\[
\begin{split}
 R_x\Phi(x,y)
 &=-c_d\mu(x)\Phi(x,y)
   +c_d\int\mu(z)\Phi(z,y)\,dz\\
 &\quad-\int K(z-x)\cdot\nabla\mu(z)\Phi(z,y)\,dz.
\end{split}
\tag{4.4}
\]

The atom sets the integrated variable \(z\) equal to the output variable \(x\). It does not set \(x=y\). Consequently (4.4) only multiplies the existing two-variable equivalence class. A restriction of the output to \(x=y\) is not defined by its \(L^2\) class and is not asserted here. On actual Borel inputs such a restriction can be read pointwise and can depend on the chosen Borel representative, as section 7 shows.

Let \((J\Phi)(x,y)=\Phi(y,x)\). Directly from (1.3), \(JR_x=R_yJ\) and \(JR_y=R_xJ\). Therefore \(R_x+R_y\) preserves symmetry; the individual responses are not claimed to do so. Finally \(R_x1=R_y1=0\), by the product rule with test \(\mu\). This checks both the background-gradient term and the compensating constant.

For backgrounds \(\mu_t\), all bounds are uniform whenever \(\sup_t\|\mu_t\|_\infty\leq M_0\) and \(\sup_t\|\nabla\mu_t\|_\infty\leq M_1\). The constants have no hidden dependence on \(N\), \(\nu\), \(\beta_N\), or a heat cutoff. A parameter-dependent family of backgrounds must supply these bounds explicitly.

## 5. Heat regularization and the precise convergence statements

Set

\[
 g_{s,\varepsilon}=p_\varepsilon*g_s,\quad
 K_\varepsilon=p_\varepsilon*K=-\nabla g_{s,\varepsilon},\quad
 D_\varepsilon=p_\varepsilon*D=\operatorname{div}K_\varepsilon.
 \tag{5.1}
\]

These are smooth periodic objects. Their Fourier multiplier is exactly \(e^{-4\pi^2\varepsilon|k|^2}\), as required by the frozen model. Positivity and mass one of the heat kernel imply

\[
 \|K_\varepsilon\|_1\leq\|K\|_1,\qquad
 \|D_\varepsilon\|_1\leq\|D\|_{\mathrm{TV}}.
 \tag{5.2}
\]

For example \(|D_\varepsilon(x)|\leq\int p_\varepsilon(x-w)|D|(dw)\), and integration proves the second inequality. The vector triangle inequality proves the first. If \(D\geq-\kappa\,dx\), then

\[
 D_\varepsilon+\kappa=p_\varepsilon*(D+\kappa\,dx)\geq0,
 \qquad D_\varepsilon(x)\geq-\kappa.
 \tag{5.3}
\]

The heat approximate-identity property is available without a rate: translation continuity in \(L^p\), \(p<\infty\), follows by approximating with trigonometric polynomials; split the heat integral into a small ball and its complement to conclude \(p_\varepsilon*f\to f\) in \(L^p\). The mass of the complement tends to zero by the periodized Gaussian formula. The same argument with uniform continuity works for continuous functions in supremum norm. In particular
\(K_\varepsilon\to K\) in \(L^1\), and \(D_\varepsilon\,dx\to D\) weakly as finite measures. At Coulomb, the latter is not convergence in total variation: by (3.5), \(D_\varepsilon\,dx-D=c_d(p_\varepsilon\,dx-\delta_0)\), whose variation is exactly \(2c_d\) for every \(\varepsilon>0\).

In defining the regularized response, only the interaction is heat-mollified; the same \(\mu\) is used on both sides. Let \(P_\varepsilon^x\) be heat convolution in the output variable \(x\). Fubini, translation invariance, and evenness of \(p_\varepsilon\) give the useful exact identity

\[
 R_{x,\varepsilon}\Phi=P_\varepsilon^xR_x\Phi,
 \qquad R_{y,\varepsilon}\Phi=P_\varepsilon^yR_y\Phi.
 \tag{5.4}
\]

For bounded Borel functions Fubini is absolutely justified, so (5.4) is pointwise. The \(L^2\) identity follows by the established boundedness and density. Notice that the heat convolution is outside the entire response; it does not silently commute with multiplication by \(\mu\). Strong \(L^2\) convergence for fixed \(\mu,\Phi\) now follows from the approximate-identity property applied to \(R_x\Phi,R_y\Phi\).

### 5.1. Operator-norm convergence below Coulomb

Here \(D\in L^1\), and \(\|D_\varepsilon-D\|_1\to0\). The proof of (4.2), applied to the differences, gives on both \(L^2\) and \(B_b\)

\[
 \|R_{x,\varepsilon}+R_{y,\varepsilon}-R_x-R_y\|
 \leq2M_0\|D_\varepsilon-D\|_1
      +2M_1\|K_\varepsilon-K\|_1\longrightarrow0.
 \tag{5.5}
\]

This is uniform over any family of backgrounds with the same \(M_0,M_1\) bounds, hence also uniform in time for such a family. No uniform modulus of continuity of \(\nabla\mu_t\) is needed in (5.5).

### 5.2. Coulomb multiplication and its commutator

Write \(M_\mu\) for multiplication in one slot. From (4.4),

\[
 R_{x,\varepsilon}-R_x
 =-c_d(P_\varepsilon^x-I)M_\mu
   -T_{K_\varepsilon-K}\cdot M_{\nabla\mu}.
 \tag{5.6}
\]

The rank-one background term cancels exactly. The first term in (5.6) is not replaced by \(-c_d M_\mu(P_\varepsilon^x-I)\) without a commutator. In fact

\[
 (P_\varepsilon M_\mu-M_\mu P_\varepsilon)F(x,y)
 =\int p_\varepsilon(w)[\mu(x+w)-\mu(x)]F(x+w,y)\,dw.
\]

Since \(\mu\) is \(M_1\)-Lipschitz for the torus distance, Minkowski gives

\[
 \|[P_\varepsilon,M_\mu]F\|_2
 \leq M_1 h_\varepsilon\|F\|_2,
 \quad h_\varepsilon:=\int\operatorname{dist}(w,0)p_\varepsilon(w)\,dw
 \leq\sqrt{2d\varepsilon}.
 \tag{5.7}
\]

The last bound unfolds the torus Gaussian and uses \(\operatorname{dist}(z\bmod\mathbb Z^d,0)\leq|z|\), followed by Cauchy–Schwarz and its second moment \(2d\varepsilon\). Consequently, for every fixed \(\Phi\in L^2(dx\,dy)\),

\[
\begin{split}
 \|(R_{x,\varepsilon}+R_{y,\varepsilon}-R_x-R_y)\Phi\|_2
 &\leq c_dM_0\big(\|(P_\varepsilon^x-I)\Phi\|_2
                   +\|(P_\varepsilon^y-I)\Phi\|_2\big)\\
 &\quad+2c_dM_1\sqrt{2d\varepsilon}\,\|\Phi\|_2
       +2M_1\|K_\varepsilon-K\|_1\|\Phi\|_2
 \longrightarrow0.
\end{split}
\tag{5.8}
\]

This proves the asserted uniformity over time or any family of backgrounds with common \(C^1\) bounds. It does not differentiate \(\nabla\mu\), and does not need a uniform modulus for that derivative. If \(t\mapsto\Phi_t\) is continuous in \(L^2\) on a compact time interval, convergence is uniform also with input \(\Phi_t\): cover the compact image by a finite norm-net and use the uniform operator bound on the error from the net. A merely bounded, cutoff-dependent family of \(L^2\) inputs has no such conclusion; section 7 supplies the obstruction.

For clarity, if the background itself is also mollified, this is a second approximation and must be estimated separately. For \(\mu_\varepsilon=p_\varepsilon*\mu\), \(\mu\in C^1\) gives \(\mu_\varepsilon\to\mu\) in \(C^1\), and the additional operator difference is at most

\[
 2\|D\|_{\mathrm{TV}}\|\mu_\varepsilon-\mu\|_\infty
 +2\|K\|_1\|\nabla\mu_\varepsilon-\nabla\mu\|_\infty.
\]

Uniformity of this *additional* approximation over a time family requires the corresponding uniform \(C^1\) approximation, for example continuity into \(C^1\) on a compact interval. It is not implicit in (5.8).

## 6. The smooth pair propagator and its exact exponent

Fix \(T<\infty\), \(N\geq2\), \(\nu\geq0\), and \(\varepsilon>0\). Assume \(u_t\) is continuous in time and smooth periodic in space with bounded spatial derivatives on \([0,T]\) for these fixed parameters. Suppose

\[
 \operatorname{div}u_t(x)\geq-a(t),\qquad
 D\geq-\kappa\,dx,
 \tag{6.1}
\]

where \(a\geq0\) is integrable and \(\kappa\geq0\) is finite. The vector field may depend on the parameters if the same \(a\) works. The Riesz choices of \(\kappa\) in section 3 meet the second condition. Define

\[
 G_{N,\varepsilon,t}
 =\nu(\Delta_x+\Delta_y)+u_t(x)\cdot\nabla_x+u_t(y)\cdot\nabla_y
 +\frac1N K_\varepsilon(x-y)\cdot(\nabla_x-\nabla_y).
 \tag{6.2}
\]

The pair drift is
\(b_t(x,y)=(u_t(x)+N^{-1}K_\varepsilon(x-y),\ u_t(y)-N^{-1}K_\varepsilon(x-y))\).
Differentiating both components gives

\[
 \operatorname{div}_{x,y}b_t
 =\operatorname{div}u_t(x)+\operatorname{div}u_t(y)
     +\frac2N D_\varepsilon(x-y)
 \geq-2a(t)-\frac{2\kappa}{N}.
 \tag{6.3}
\]

The derivative in \(y\) of \(-K_\varepsilon(x-y)\) has the same positive divergence contribution as the derivative in \(x\) of \(K_\varepsilon(x-y)\). This is the source of the factor two.

The lower-bound assumption is available in the frozen smooth mean-field model: if \(u_t=b_t+K_\varepsilon*\mu_t\), \(\mu_t\) is a probability density, and \(\operatorname{div}b_t\geq-a_b(t)\), then \(\operatorname{div}u_t=\operatorname{div}b_t+D_\varepsilon*\mu_t\geq-a_b(t)-\kappa\). Thus \(a=a_b+\kappa\) works uniformly in the cutoff. This uses (5.3) and positivity and mass one of the density, without estimating high derivatives of the regularized kernel.

Here is a construction and a bound that includes \(\nu=0\). For each fixed continuous Brownian path in \(2d\) dimensions, subtract the additive displacement \(\sqrt{2\nu}(W_r-W_s)\) from the SDE driven by \(b_r\). The remaining equation is an ODE with continuous time dependence and globally Lipschitz, periodic spatial coefficients. Picard iteration on short intervals, followed by concatenation, constructs its unique flow for the whole finite interval. The inverse is given by the backwards ODE for the same path. Spatial differentiation gives a smooth diffeomorphism \(F_{s,t}^W\) of the pair torus and the Jacobian identity

\[
 \det D F_{s,t}^W(X)
 =\exp\!\left(\int_s^t\operatorname{div}b_r(F_{s,r}^W(X))\,dr\right)
 \geq\exp\!\left(-2\int_s^t[a(r)+\kappa/N]\,dr\right).
 \tag{6.4}
\]

The determinant identity follows by differentiating the flow ODE and the determinant, with initial determinant one. Brownian spatial translations have derivative the identity. All construction statements use fixed \(\varepsilon\); their derivative estimates are not asserted uniform in \(\varepsilon\).

Set \(S_{s,t}^{N,\varepsilon,\nu}f(X)=\mathbb E f(F_{s,t}^W(X))\). This is a positivity-preserving, constant-preserving contraction on \(B_b\), and the independent-increment flow property gives the Markov propagation law. Smooth Itô calculus identifies its backward generator with (6.2). For bounded Borel \(f\), Jensen, change of variables for each path, and (6.4) show

\[
\begin{split}
 \|S_{s,t}^{N,\varepsilon,\nu}f\|_2^2
 &\leq\mathbb E\int|f(F_{s,t}^W(X))|^2\,dX\\
 &\leq\exp\!\left(2\int_s^t[a(r)+\kappa/N]\,dr\right)\|f\|_2^2.
\end{split}
\tag{6.5}
\]

The same change-of-variables argument shows that product-null modifications of \(f\) change the result only almost everywhere. Density therefore gives a bounded propagator on Haar \(L^2\), with

\[
 \boxed{\displaystyle
 \|S_{s,t}^{N,\varepsilon,\nu}\|_{2\to2}
 \leq\exp\!\left(\int_s^t[a(r)+\kappa/N]\,dr\right)
 \leq\exp\!\left(\int_s^t[a(r)+\kappa/2]\,dr\right).}
 \tag{6.6}
\]

For smooth functions, flow continuity at short time gives strong continuity, by dominated convergence. Approximation and (6.6) extend this to \(L^2\). Oddness of \(K_\varepsilon\) makes the drift equivariant under exchange of the two slots; the Brownian law has the same symmetry. Thus the propagator preserves symmetric kernels.

The energy computation gives an independent sign and exponent check. For a smooth solution of the time-reversed observable equation, \(\partial_\tau v=G_{N,\varepsilon,t-\tau}v\), periodic integration by parts yields

\[
 \frac12\frac d{d\tau}\|v\|_2^2
 =-\nu(\|\nabla_xv\|_2^2+\|\nabla_yv\|_2^2)
 -\frac12\int\operatorname{div}b_{t-\tau}|v|^2
 \leq[a(t-\tau)+\kappa/N]\|v\|_2^2.
 \tag{6.7}
\]

Gronwall gives the squared-norm exponent twice the one in (6.6). The needed hypothesis is a *lower* bound on divergence. Diffusion is nonpositive in (6.7) for every \(\nu\geq0\). At Coulomb with \(u=0\), the norm exponent is \(c_d(t-s)/2\) for \(N=2\), and \(c_d(t-s)/3\) for \(N=3\).

### 6.1. Bounded-response consequence at each smooth cutoff

For completeness this interface also gives a uniform bound after adding the bounded responses. Suppose \(t\mapsto\mu_t\) is continuous into \(C^1\), and let \(C_R(t)\) denote (1.4). For terminal datum \(f\in L^2\) and forcing \(F\in L^1([0,t];L^2)\), solve the Volterra equation

\[
 v_s=S_{s,t}f+\int_s^tS_{s,r}\big[(R_{x,\varepsilon,r}+R_{y,\varepsilon,r})v_r+F_r\big],dr.
 \tag{6.8}
\]

It has a unique continuous \(L^2\) solution. To see this, iterate: the \(n\)-th response term is integrated over an ordered simplex and is bounded by the product of the local propagation factors times \((\int_s^t C_R)^n/n!\). Their series converges uniformly; the same bound applied to a difference proves uniqueness. Summing the series gives

\[
 \|v_s\|_2\leq e^{\int_s^t A(r)dr}\|f\|_2
 +\int_s^t e^{\int_s^q A(r)dr}\|F_q\|_2\,dq,
 \qquad A(r)=a(r)+\kappa/N+C_R(r).
 \tag{6.9}
\]

Every Bochner integral is justified by strong continuity of \(S\), norm continuity of the bounded response in \(\mu_t\), and the stated forcing integrability. Symmetric data and forcing give a symmetric solution by uniqueness. This proves a finite-cutoff \(L^2\) mild equation bound; it does not establish the actual campaign forcing in \(L^1_tL^2\), or any singular generator limit.

## 7. Falsification route, exact tests, and self-review

The following checks use Fourier eigenfunctions, null-set representatives, and a smooth one-coordinate pair field rather than the local flux proof. They are an algebraically distinct falsification route within this same constructor context, not an independent audit.

**Homogeneous Fourier response and the sign.** For \(\mu=1\), the pair mode \(e^{2\pi i(k\cdot x+\ell\cdot y)}\) has response eigenvalue

\[
 -[\widehat D(k)+\widehat D(\ell)],\qquad
 \widehat D(0)=0,\quad
 \widehat D(k)=4\pi^2c_{d,s}|k|^{s+2-d}\ (k\ne0).
 \tag{7.1}
\]

It is nonpositive. Directly in the gradient formula, \(\widehat K(-k)=2\pi i k\widehat g_s(k)\) multiplied by \(2\pi i k\) gives the same negative number. This checks the sign without distributional integration by parts.

**The atom and constant compensation cannot be dropped.** At Coulomb and \(\mu=1\), the full response kills constants. Keeping only the absolutely continuous part of \(D\) would instead give \(R_x1=c_d\), while keeping only the atom would give \(R_x1=-c_d\). With \(\mu=1+q\cos(2\pi k\cdot z)\), \(0<|q|<1\), omitting \(K\cdot\nabla\mu\) gives the false nonzero answer \(-q\widehat D(k)\cos(2\pi k\cdot x)\) on the constant input. The true gradient formula is zero. These tests falsify three common shortcuts.

**Coulomb operator-norm convergence is false.** For \(\mu=1\), write \(P^x\) for averaging in the first variable, and similarly for \(P^y\). Then

\[
 R_x+R_y=-c_d(2I-P^x-P^y),\qquad
 R_{x,\varepsilon}+R_{y,\varepsilon}-(R_x+R_y)
 =c_d(2I-P_\varepsilon^x-P_\varepsilon^y).
 \tag{7.2}
\]

For every \(\varepsilon>0\), the operator norm of the last expression on \(L^2\) is exactly \(2c_d\). The upper bound follows from its nonnegative Fourier multipliers bounded by \(2c_d\); the lower bound follows from modes with \(k=\ell\ne0\) and \(|k|\to\infty\). Real normalized cosines \(\cos(2\pi k\cdot(x+y))\) give the same result within symmetric real kernels. For one response the difference norm is exactly \(c_d\). Thus a bounded family of cutoff-dependent high-frequency inputs invalidates any claimed uniform strong convergence on the \(L^2\) unit ball.

**The Borel distinction is real.** Take \(\Phi(x,y)=\mathbf1_{\{x=y\}}\). At Coulomb, (4.4) and absolute continuity of the remaining integrals give

\[
 (R_x+R_y)\Phi(x,y)=-c_d[\mu(x)+\mu(y)]\mathbf1_{\{x=y\}},
\]

while the heat-regularized response is zero everywhere for every \(\varepsilon>0\). Hence convergence for all bounded Borel inputs fails pointwise on the diagonal and in supremum norm. Both outputs represent zero in Haar \(L^2\), so this does not contradict strong \(L^2\) convergence or equivalence-class well-definedness. It shows exactly why no pointwise diagonal conclusion is extracted from that convergence.

**Pair factor and energy sign in a smooth model.** Embed one coordinate in \(\mathbb T^d\), set \(u=0\), \(\nu=0\), \(K(z)=\sin(2\pi z_1)e_1\), and use \(f(x,y)=1+b\cos\theta\), \(\theta=2\pi(x_1-y_1)\). This is a smooth even-potential diagnostic. Direct differentiation and integration give

\[
 G_Nf=-\frac{4\pi b}{N}\sin^2\theta,
 \quad\langle f,G_Nf\rangle=-\frac{2\pi b}{N},
 \quad\operatorname{div}b_{\rm pair}=\frac{4\pi}{N}\cos\theta.
 \tag{7.3}
\]

Since \(\int\cos\theta\,f^2=b\), the energy formula \(-\tfrac12\int\operatorname{div}b_{\rm pair}f^2\) agrees exactly. Omitting the second pair divergence would miss a factor of two. Taking \(b<0\) makes the observable energy derivative positive, confirming that an unjustified uniform contraction statement is false. The lower divergence bound is \(\kappa=2\pi\), consistently with (6.6). The checker evaluates these coefficients at \(N=2,3,5\), including both signs of \(b\).

The optional standard-library checker `DISCOVERY_CODE/check_round004_singular_response_exact.py` uses exact rational Fourier coefficients in dimensionless angle coordinates to compare the direct gradient response with both integration-by-parts terms for inhomogeneous \(\mu\). It also checks (7.3), the \(2/N\) coefficient and half-energy factor, the Coulomb nonzero-mode multiplier, and the algebraic coefficient \(s(d-2-s)\) at representative rational exponents. All **133 exact checks passed** under Python 3.9.6. There is no random seed, floating-point tolerance, external dependency, or numerical inference. Computation status is **REPRODUCED**; it is supporting evidence, not a computational proof or independent certificate.

The self-review specifically checked: (i) local versus global power coordinates; (ii) orientation of the punctured-boundary normal; (iii) total variation versus signed mass; (iv) pointwise Borel values versus Haar equivalence classes; (v) multiplication versus a pair trace at the atom; (vi) the noncommuting multiplication in heat approximation; (vii) time-uniform quantifiers for fixed and varying inputs; (viii) the two drift divergences and half-energy factor; and (ix) the separation between smooth propagation and singular existence. No unresolved defect was found in these stated assertions. That verdict remains a self-check.

## 8. Scope, remaining gates, and integration handoff

The task's finite-measure response question closes as a **PROVED_CANDIDATE**, including the Coulomb endpoint. The estimate is a bound on Haar \(L^2\) functions, on the Haar \(L^\infty\) quotient, and separately on actual bounded Borel functions. It does not assert the same constant in \(L^2(\mu\otimes\mu)\) when \(\mu\) can vanish. A Haar \(L^2\) pair kernel does satisfy
\(\|\Phi\|_{L^2(\mu\otimes\mu)}\leq M_0\|\Phi\|_{L^2(dx\,dy)}\), which is the elementary one-way interface with THM-015's iid hypothesis. No iid theorem is applied to a dependent evolved law.

The smooth local pair propagator and its bounded-response Volterra equation close with the exponents (6.6) and (6.9), provided their explicitly stated drift, background, and forcing hypotheses hold. Those estimates alone do not prove that smooth pair flows or mild solutions converge as \(\varepsilon\downarrow0\). In particular strong convergence of the bounded responses for fixed inputs does not supply convergence of the unbounded first-order part of the generator, compactness of cutoff-dependent correctors, convergence of martingales, or control of the higher-order residual.

| Item for root integration | Exact result here | Remaining requirement |
|---|---|---|
| Divergence and constants | (3.3)–(3.5), including the Coulomb atom and negative torus compensation | Separate reconstruction and hostile audit |
| Response operator | (1.3)–(1.4), (4.1)–(4.4), Haar \(L^2\), \(L^\infty\), and \(B_b\) | No weighted or diagonal-trace promotion |
| Named regularization | (5.1)–(5.8), operator convergence below Coulomb and strong convergence at Coulomb | No uniform operator convergence at Coulomb |
| Smooth local propagation | (6.2)–(6.7), exponent \(a+\kappa/N\), uniform in cutoff and diffusivity | Singular flow/propagator construction and comparison are separate |
| Bounded-response interface | (6.8)–(6.9) for supplied \(L^1_tL^2\) forcing | Actual forcing and corrector limits must be established |
| Centering and law class | No centering change; deterministic function-space result | No dynamic law-class transfer |
| Temperature scaling | No \(\beta_N\), \(\lambda_N\), or old-floor factor in these operator constants | No subcritical or critical fluctuation closure claimed |

The root should allocate canonical identifiers and update the affected normalization, operator, regularization, assumptions, and proof-obligation ledgers only after the appropriate comparison. This worker does not assign a new globally shared theorem number. The next independent audit should reconstruct (3.2), the gamma constant in (3.5), equivalence-class well-definedness in (4.1), the commutator estimate (5.8), and the exponent in (6.6) before reading this narrative.

All created files and hashes are listed in the output seal. Verification commands and actual results are recorded in `REPORTS/CHECKPOINTS/ROUND_004_SINGULAR_RESPONSE_SEAL.md`. The Markdown report is the requested mathematical artifact; no TeX source was edited, and no campaign-wide verifier was run because this isolated task does not consume the unrelated proof dossiers.
