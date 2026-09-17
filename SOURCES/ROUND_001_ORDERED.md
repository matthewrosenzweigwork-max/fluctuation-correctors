# TASK-007: circular Riesz sources and the ordered dynamic interface

- Round: 001; report issued 2026-09-17 UTC.
- Worktree: `/private/tmp/hocf-round001-ordered-20260917`.
- Branch and baseline: `codex/hocf-r001-ordered`, `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Authority: `TASKS/ACTIVE/ROUND_001_MODEL.md`, version 1.0.
- Owner: `/root/ordered`; no canonical ledger edits or commits.
- Mathematical disposition: exact normalization and stopped gap identities proved below; a proposed temperature-uniform import disproved; `THM-006` and `PO-013` remain `OPEN`.
- Audit: `SELF_CHECKED`, not independent certification.
- Sources: `SRC-005` and `SRC-006` are version-locked primary PDFs. The numerical normalization in `SRC-005` has status `SOURCE_MISMATCH`; its numerical CLT covariance is **not imported**.

The exact Gibbs match is

\[
 b_N:=\beta_{\mathrm{Boursier},N}
      =\frac12\beta_N N^{s-1}=\frac12\lambda_N,
 \qquad d=1,\quad 0<s<1,\quad V=0.
\]

Thus fixed positive source inverse temperature corresponds to an exactly fixed critical campaign coupling. The full subcritical campaign sends the source inverse temperature to zero. Neither paper supplies the needed moving-law replacement theorem, and the same correlation bound cannot have a constant uniform all the way to zero source inverse temperature. The normalization discrepancy is separate from, and does not invalidate, this Hamiltonian-based temperature map.

## 1. Assertion, negation, and scope

The bounded assertion is: under the frozen conventions, the source ensemble can be mapped exactly into the homogeneous one-dimensional campaign equilibrium, and the actual particle generator has the gap representation in Section 5 before a collision or coordinate-chart exit. Its negation is the existence of a permitted configuration, smooth even kernel, particle number, inverse temperature, or test function for which either coefficient identity fails.

The distinct proposed import tested by falsification is: the fixed-temperature source correlation bound remains valid with the same constant uniformly for every positive source inverse temperature and particle number. Its negation is proved in Section 6. This is a route obstruction, not a disproof of the campaign's subcritical fluctuation target.

The local work uses smooth kernels at fixed cutoff, or the singular kernel only on a stopped set separated from collisions. It proves no cutoff removal, collision avoidance, transient CLT, path tightness, hierarchy truncation, or moving-background theorem. No other constructor output was read.

## 2. Primary sources and version evidence

| Ledger row | Locked primary source | Date and PDF size | SHA-256 |
|---|---|---|---|
| SRC-005 | Jeanne Boursier, [Optimal local laws and CLT for the circular Riesz gas, arXiv:2112.05881v5](https://arxiv.org/pdf/2112.05881v5) | 19 July 2025; 76 pages; 1,058,342 bytes | `e178971833d268fae283068aa7986cbf5ca20f49a0346973fa5ad60a08372e83` |
| SRC-006 | Jeanne Boursier, [Decay of correlations and thermodynamic limit for the circular Riesz gas, arXiv:2209.00396v4](https://arxiv.org/pdf/2209.00396v4) | 19 July 2023; 64 pages; 914,778 bytes | `03c688f1db0d66c84971e144dcaa87076c904bc4dfdf1423f81d006771ee653d` |

The [first submission history](https://arxiv.org/abs/2112.05881) and [second submission history](https://arxiv.org/abs/2209.00396) identified these as their latest revisions when checked. The [author's publication page](https://jboursier.github.io/) links the same two arXiv papers. A bounded search of those records and the author's page did not locate a correcting primary notice; this is not an exhaustive erratum search.

Both PDFs were downloaded and read, rather than relying on their abstracts. Statement and normalization reading concentrated on SRC-005 pp. 1–5 and 12–17, and SRC-006 pp. 1–6, 12–15 and 49. The covariance proof route and its dependence on the static Helffer–Sjöstrand equation were inspected. This is a source qualification, not an independent audit of every proof in either paper.

### Exact theorem locations and safe scope

**SRC-005.** Equations (1.1)–(1.4), pp. 1–2, define the kernel, ordered Hamiltonian and Gibbs law. Theorem 1, p. 4, gives gap and interval-count rigidity with constants depending on fixed \(b,s,\varepsilon\). Theorems 2 and 3, p. 5, concern variance and a scalar quantitative CLT under Assumption 1.1, p. 4; the CLT additionally requires \(N\ell_N\to\infty\). The source observable is

\[
 (N\ell_N)^{-s/2}
 \left(\sum_i\xi(\ell_N^{-1}x_i)-N\ell_N\int\xi\right),
\]

with \(\ell_N\equiv1\), or \(\ell_N\to0\) and \(\xi\) supported in \((-1/2,1/2)\). The source permits finitely many singularities with exponent \(\alpha\in[s-1,s/2)\) satisfying (1.8); smooth periodic tests form the unambiguous campaign subclass. Its constants depend on \(b,s,\varepsilon,\xi\). Numerical covariance qualification fails in Section 4.

**SRC-006.** Equations (1.1), (1.3) and (1.4), pp. 1–2, define the same ensemble. Theorem 1, p. 3, applies to \(0<s<1\) and gap observables. For distinct indices, a safe consequence for \(\xi,\chi\in C_c^\infty(\mathbb R)\) is

\[
 |\operatorname{Cov}(\xi(y_i),\chi(y_j))|
 \le C_{s,b,\varepsilon}\|\xi'\|_\infty\|\chi'\|_\infty
 d_N(i,j)^{-(2-s-\varepsilon)},\qquad
 y_i=N(x_{i+1}-x_i).
\tag{S1}
\]

Here \(b>0\) is fixed and \(d_N\) is cyclic index distance. This follows by bounding both derivative factors in its (1.5) by their suprema. Theorem 3, p. 4, gives local convergence of the rescaled *equilibrium* point process for fixed \(b\). Proposition 3.3, pp. 14–15, gives a constrained static gap Helffer–Sjöstrand representation. Neither statement is a theorem about time correlations of the campaign dynamics.

Two notation issues are quarantined. SRC-005 Assumption 1.1(A1) literally prints \(\xi'=\chi\in C^{1-s+\varepsilon}\), although Remark 1.2 includes indicators. An indicator does not satisfy that printed derivative condition; no singular-test extension is imported here. SRC-006 (1.5) prints derivative factors evaluated at \(x_i,x_j\), despite the gap observables on its left. Bound (S1) avoids that ambiguity by using global derivative suprema. Neither issue is silently repaired.

## 3. Exact Hamiltonian, law, and temperature map

Write the campaign particle potential, for a smooth even kernel initially, as

\[
 E_N(X)=\sum_{i=1}^N V(x_i)+\frac{1}{2N}\sum_{i\ne j}g(x_i-x_j).
\]

The ordered pair sum is essential. Direct differentiation gives

\[
 -\partial_iE_N=-V'(x_i)-\frac1N\sum_{j\ne i}g'(x_i-x_j),
 \qquad
 \mathcal L_N=\beta_N^{-1}\Delta_X-\nabla E_N\cdot\nabla_X.
\]

For the smooth model, integration by parts on the particle torus proves invariance and reversibility of \(Z^{-1}e^{-\beta_NE_N}dX\). For the singular kernel, this density remains a well-defined static probability measure, but this observation alone does not construct or identify a global singular diffusion.

When \(V=0\), the source uses

\[
 H_N^{B}=N^{-s}\sum_{i\ne j}g(x_i-x_j),\qquad
 dP_{N,b}=Z_{N,b}^{-1}e^{-bH_N^B}1_{D_N}\,dX.
\]

Since \(E_N=\tfrac12N^{s-1}H_N^B\), equality of Gibbs exponents gives \(b_N=\lambda_N/2\). Restricting the labeled symmetric Gibbs measure to one cyclic ordering chamber and normalizing produces the source law. Symmetric particle statistics have the same distribution before and after this conditioning; gap observables use the cyclic order and the distinguished root particle. The source law is not an iid product law or a Gibbs law with arbitrary confinement.

Translation invariance gives every labeled marginal equal to Haar measure, so source mean-field and exact-marginal centerings agree for linear statistics. This does not equate higher correlations, even when the campaign starts from uniform iid data. A nonconstant \(V\), a nonuniform reference density, or a time-dependent local Gibbs ansatz needs a separate source theorem or proof.

| Campaign regime in dimension one | Source parameter | Qualification |
|---|---|---|
| \(\lambda_N\to0\) | \(b_N\to0\) | Quantified high-temperature dependence is needed. |
| \(\lambda_N\equiv\lambda>0\) | \(b=\lambda/2\) fixed | Exactly the source equilibrium temperature scaling. |
| \(\lambda_N\to\lambda>0\) | \(b_N\to\lambda/2\) | Requires uniformity in a neighborhood of that value, not merely a fixed-parameter statement. |
| \(\lambda_N\to\infty\) | \(b_N\to\infty\) | No low-temperature-uniform import established. |

In particular, fixed source inverse temperature means campaign inverse temperature \(\beta_N=2bN^{1-s}\), which grows with \(N\). It does not mean fixed campaign inverse temperature. In that equilibrium scaling,

\[
 \sqrt{N\beta_N}\langle\xi,\eta_N-1\rangle
 =\sqrt{2b}\,N^{-s/2}\left(\sum_i\xi(x_i)-N\int\xi\right).
\]

This is an exact comparison of observables, not a transient fluctuation theorem. For iid preparation the dossier instead retains \(\sigma_N=\min(\sqrt{N\beta_N},\sqrt N)\).

## 4. Kernel computation and the printed normalization conflict

### 4.1 Independent Fourier computation

Take the source's actual real-space definition, for \(0<s<1\),

\[
 g_s(x)=\lim_{n\to\infty}
 \left(\sum_{m=-n}^{n}|x+m|^{-s}-\frac{2n^{1-s}}{1-s}\right).
\tag{K1}
\]

The tail after pairing positive and negative indices converges uniformly away from the fixed integrable singularity at zero. The integral of the finite approximation over \([0,1]\) is

\[
 \frac{(n+1)^{1-s}-n^{1-s}}{1-s}\longrightarrow0.
\]

For an integer \(k\ne0\), changing variables in each summand gives

\[
 \widehat g_s(k)
 =\lim_{n\to\infty}\int_{-n}^{n+1}|u|^{-s}e^{-2\pi iku}\,du
 =2\Gamma(1-s)\sin(\pi s/2)(2\pi|k|)^{s-1}.
\tag{K2}
\]

For completeness, the half-line oscillatory integral follows from
\(\int_0^\infty x^{-s}e^{-(a-i\omega)x}dx
=\Gamma(1-s)(a-i\omega)^{s-1}\), \(a>0\), by taking real parts and letting \(a\downarrow0\). Integration by parts bounds the oscillatory tail uniformly in the Abel limit; integrability at zero uses \(s<1\). Gamma duplication and reflection then give

\[
 \widehat g_s(0)=0,\qquad
 \widehat g_s(k)=C_s|k|^{s-1},\qquad
 C_s=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{K3}
\]

Thus the source's real-space kernel agrees exactly with the frozen campaign kernel in dimension one. Its local principal part is \(|x|^{-s}\); it is not globally homogeneous on the circle. No logarithmic conclusion is obtained by setting \(s=0\).

### 4.2 SOURCE_MISMATCH, with precise witness

SRC-005, printed p. 1 / PDF index 0, equation (1.3), visibly prints

\[
 c_s^{\rm printed}=2^{s-1}\sqrt\pi\,
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{K4}
\]

Printed p. 13 / PDF index 12 defines Fourier coefficients with \(e^{-2\pi ikx}\) and the inverse fractional Laplacian with multiplier \((2\pi)^{-2\alpha}|k|^{-2\alpha}\). Consequently (K1)–(K3) force

\[
 (-\Delta)^{(1-s)/2}g_s
 =c_s^{\rm required}(\delta_0-1),\qquad
 c_s^{\rm required}=(2\pi)^{1-s}C_s
 =2^{1-s}\sqrt\pi\,
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{K5}
\]

The ratio is \(c_s^{\rm required}/c_s^{\rm printed}=2^{2(1-s)}\ne1\). An exact one-mode test is \(s=1/2\): (K3) gives \(\widehat g_{1/2}(1)=1\), so the multiplier is \(\sqrt{2\pi}\), whereas (1.3) prints \(\sqrt{\pi/2}\).

There is also an internal check independent of the Fourier integral. At printed p. 15 / PDF index 14, Step 3 of Lemma 2.1 replaces

\[
 \frac{c_s\Gamma(s/2)2^s}{\Gamma((1-s)/2)2\sqrt\pi}
\]

by one. With (K4), that factor equals \(2^{2s-2}\), not one. With (K5), it equals one.

The printed variance coefficient in (1.10), p. 4, and Theorems 2–3, p. 5, uses the same \(c_s\). Therefore the exact covariance is not a qualified campaign input. Merely replacing \(c_s\) in the theorem is a candidate repair requiring a proof-level normalization audit; it has not been performed here. The verified conclusions retained are (K3), the Hamiltonian temperature map, and the stated fixed-law scope. This finding does not purport to disprove the qualitative CLT or its proof mechanism.

## 5. Complete local derivation in ordered gap variables

Fix \(N\ge2\), \(\beta_N>0\), and a smooth even periodic \(g\). Set \(K=-g'\). On a lifted cyclic ordering chart, write

\[
 x_1<\cdots<x_N<x_1+1,\qquad x_{N+1}=x_1+1,\qquad
 y_i=N(x_{i+1}-x_i),\qquad \sum_i y_i=N.
\]

Stop the path before a collision or chart exit, and, for the singular kernel, before a prescribed minimum gap threshold is reached. This permits ordinary smooth Itô calculus. Let

\[
 D_{ij}=\mathbf1_{\{j=i+1\pmod N\}}-\mathbf1_{\{j=i\}},\qquad A=DD^T.
\]

Locally \(y=NDX+Ne_N\), and \(D\mathbf1=0\). If
\(F_i=b(x_i)+N^{-1}\sum_{j\ne i}K(x_i-x_j)\), subtraction of adjacent particle equations gives exactly

\[
 dy=NDF\,dt+\sqrt{2N^2/\beta_N}\,D\,dW,
 \qquad d\langle y_i,y_j\rangle_t=(2N^2/\beta_N)A_{ij}\,dt.
\tag{G1}
\]

In particular, without inserting a fictitious self-force,

\[
 (NDF)_i=N(b(x_{i+1})-b(x_i))+2K(y_i/N)
 +\sum_{j\notin\{i,i+1\}}
 \bigl[K(x_{i+1}-x_j)-K(x_i-x_j)\bigr].
\tag{G2}
\]

All positions in the last formula are understood periodically; its wraparound case follows using the lifted \(x_{N+1}\). The sum of the gap drifts and the gap martingales is zero.

For \(V=0\), define on the gap simplex

\[
 h_N(z)=N^{-s}g(z/N),\quad
 S_{i,k}(y)=\sum_{r=0}^{k-1}y_{i+r},\quad
 H_N^g(y)=\sum_{i=1}^N\sum_{k=1}^{N-1}h_N(S_{i,k}(y)).
\tag{G3}
\]

Here \(s\) is only a scaling label for a smooth kernel. Each ordered pair occurs once in (G3), so \(H_N^B(X)=H_N^g(y(X))\). The chain rule and Section 3 give

\[
 \nabla_XH_N^B=ND^T\nabla_yH_N^g,\quad
 F=-\tfrac12N^sD^T\nabla_yH_N^g,\quad
 NDF=-\tfrac12N^{s+1}A\nabla_yH_N^g.
\]

Therefore a smooth gap test \(f\) has generator

\[
 \mathcal L_N^{\rm gap}f
 =\frac{N^2}{\beta_N}
 \left(A:D^2f-b_N(A\nabla H_N^g)\cdot\nabla f\right),
 \qquad b_N=\frac12\beta_NN^{s-1}.
\tag{G4}
\]

Extensions off the hyperplane \(\sum y_i=N\) do not affect this formula: \(A\) annihilates its normal vector. The gap martingale for time-dependent \(f\) satisfies

\[
 d\langle M^f,M^h\rangle_t
 =\frac{2N^2}{\beta_N}
 (\nabla f)^TA\nabla h(Y_t)\,dt.
\tag{G5}
\]

Thus the physical mobility is the cycle Laplacian \(A\), not the identity. SRC-006 Proposition 3.3 uses the Euclidean Dirichlet form on the constrained gap simplex. Both can represent the same static Gibbs covariance, but their generators and time estimates are different. In particular, the nonzero eigenvalues of \(A\) are
\(4\sin^2(\pi k/N)\), \(1\le k<N\); the lowest is of order \(N^{-2}\). The prefactor \(N^2/\beta_N\) alone is not a proof of rapid relaxation of every relevant mode.

Gap variables also omit the absolute rotation. For a general non-translation-invariant test, keep \(q=x_1\). Directly from the same affine change of variables,

\[
 dq=F_1dt+\sqrt{2/\beta_N}\,dW_1,\quad
 d\langle q,y_i\rangle_t=(2N/\beta_N)D_{i1}\,dt,
 \quad d\langle q\rangle_t=2\beta_N^{-1}dt.
\tag{G6}
\]

The \((q,y)\) generator consequently has the extra terms
\(F_1\partial_q+\beta_N^{-1}\partial_{qq}
 +(2N/\beta_N)\sum_iD_{i1}\partial_{qy_i}\).
This prevents a gap-only state from being advertised as sufficient for every spatially tested fluctuation observable. If \(V\ne0\), (G2) additionally depends on the absolute positions.

For the singular kernel (K1), termwise differentiation off the collision set gives

\[
 g_s''(r)=s(s+1)\sum_{m\in\mathbb Z}|r+m|^{-s-2}>0,
 \qquad 0<r<1.
\]

Hence the quadratic form of the gap Hessian in the interior is

\[
 v^TD^2H_N^g(y)v=
 \sum_{i,k}N^{-s-2}g_s''(S_{i,k}/N)
 \left(\sum_{r=0}^{k-1}v_{i+r}\right)^2\ge0.
\tag{G7}
\]

This is an actual structural positivity argument. It does not use positivity of arbitrary weighted Riesz kernels. It is also not uniform convexity with a controlled temperature/particle-number constant. For the campaign heat cutoff, the Fourier formula instead gives

\[
 g_{s,\epsilon}''(0)
 =-\sum_{k\ne0}(2\pi k)^2 C_s|k|^{s-1}e^{-4\pi^2\epsilon k^2}<0.
\]

Thus the singular ordered convexity cannot simply be imported for every fixed smooth cutoff. Global ordering at fixed smooth cutoff also requires rank-process local-time terms after crossings. Equations (G1)–(G7) make only the stated stopped claim.

## 6. Independent falsification by the zero-coupling gap law

This calculation uses simplex integration, not the source local law or the gap-generator argument.

For \(N\) uniform iid points, root the cyclic ordering at one designated particle. The normalized gaps \((y_1/N,\ldots,y_N/N)\) are uniform on the probability simplex: the joint density of the other \(N-1\) ordered relative positions is constant, and the position-to-gap map has constant Jacobian. Integrating that simplex gives

\[
 \mathbb Ey_i=1,\quad
 \mathbb Ey_i^2=\frac{2N}{N+1},\quad
 \mathbb Ey_iy_j=\frac{N}{N+1}\ (i\ne j),\quad
 \operatorname{Cov}(y_i,y_j)=-\frac1{N+1}.
\tag{F1}
\]

For each fixed \(N\), the singular Gibbs gap law tends to this law as \(b\downarrow0\). Indeed, \(H_N^B\) is bounded below, finite almost everywhere, and the chamber has finite volume. Dominated convergence applies to its density and normalizing constant after subtracting that lower bound. Since \(0<y_i<N\), it also applies to all second gap moments.

Suppose (S1) held with a constant independent of \(b>0\) and \(N\). For each \(N\), choose smooth compactly supported functions equal to the identity on \([0,N]\), with derivative suprema bounded by an absolute constant; such extensions exist by smoothing outside a larger interval. Let \(b\downarrow0\), use (F1), and choose \(d_N(i,j)=\lfloor N/2\rfloor\). For \(0<\varepsilon<1-s\), the result would be

\[
 \frac1{N+1}\le C\lfloor N/2\rfloor^{-(2-s-\varepsilon)},
\]

which is impossible as \(N\to\infty\). Equivalently, continuity permits a diagonal choice \(0<b_N<1/N\) for which the covariance magnitude is at least \(1/(2(N+1))\). Then \(\lambda_N=2b_N\to0\), providing a full subcritical witness against that uniform import. This witness does not assert an obstruction in every subclass with growing campaign inverse temperature.

The initial-law issue is also visible in a single gap. Its iid density is

\[
 p_N(y)=\frac{N-1}{N}(1-y/N)^{N-2},\qquad 0<y<N.
\]

Thus \(\mathbb E_{\rm iid}y^{-p}=\infty\) for every \(p\ge1\). At each fixed positive \(b\) and fixed \(N\), the singular Gibbs law has all inverse-gap moments finite: its energy contains the two orientations of the nearest-neighbor pair, giving a factor bounded above near zero by a constant times \(e^{-2b y^{-s}}\), and all other interactions have a finite lower bound. No source inverse-gap estimate can be used at iid time zero without an initial-layer argument. The finiteness statement here makes no uniform-in-\(N,b\) claim.

## 7. Exact residual reduction and first unproved lines

For a translation-invariant residual \(R_{N,t}\) in the homogeneous model, a potential corrector \(u_{N,t}\) must solve the *physical* backward problem

\[
 (\partial_t+\mathcal L_N^{\rm gap})u_{N,t}=-R_{N,t}.
\tag{R1}
\]

If it is smooth on the stopped region, Itô's formula gives, with \(S=T\wedge\tau\),

\[
 \int_0^S R_{N,t}(Y_t)dt
 =u_{N,0}(Y_0)-u_{N,S}(Y_S)+M_S^u,
 \qquad
 \mathbb E\langle M^u\rangle_S
 =\frac{2N^2}{\beta_N}\mathbb E\int_0^S
 (\nabla u)^TA\nabla u\,dt.
\tag{R2}
\]

Consequently, endpoint estimates
\(\sigma_N\|u_{N,0}(Y_0)\|_2\to0\),
\(\sigma_N\|u_{N,S}(Y_S)\|_2\to0\), and

\[
 \sigma_N^2\frac{2N^2}{\beta_N}
 \mathbb E\int_0^S(\nabla u)^TA\nabla u\,dt\longrightarrow0
\tag{R3}
\]

imply \(\sigma_N\int_0^S R_{N,t}dt\to0\) in \(L^2\). Removing the stop needs its own estimate. For non-translation-invariant residuals, (R1) must instead use the full \((q,y)\) generator and (G6). This is an exact sufficient reduction; no estimates in (R3) are asserted. At criticality it should be applied to a proved hierarchy tail, not used to assume that every quadratic or higher correction vanishes.

The first unproved interface is therefore **a mobility-aware, temperature- and cutoff-controlled estimate for (R1) under the actual transient law**, including the required martingale term and endpoint norms. The static Euclidean gap Helffer–Sjöstrand estimate is not that estimate.

The affected existing ledger rows should remain open, with the following precise qualifications for root integration:

| Existing row | Unproved input remaining |
|---|---|
| SD-005 / OP-005 | Control the physical gap operator with mobility \(A\), including its slow modes and the rotation variable when required. |
| SD-002 / PO-011 | Transfer source static correlations to the actual law, or prove replacement errors at the selected fluctuation scale. Static spatial decay is not temporal mixing. |
| AC-005 | Quantify dependence as \(b_N\downarrow0\); Section 6 rules out retaining the same bound with a bounded constant on the entire temperature range. For varying critical \(b_N\), prove sufficient local uniformity. |
| LG-004 / PO-013 | Treat moving nonuniform backgrounds and confinement, plus iid preparation and its initial layer, separately from circular homogeneous equilibrium. |
| REGULARIZATION_LEDGER | Remove the stop and cutoff with uniform integrability; singular convexity is lost near the diagonal for the smooth heat cutoff. |
| SRC-005 | Resolve the printed \(c_s\) conflict at proof level before importing any exact covariance. |

No statement above says that one static theorem alone closes the entire dynamic hierarchy. The source and dynamic obstructions are explicitly separated.

## 8. Checks, evidence, and disposition

The following tests were completed analytically:

- **One Fourier mode:** \(s=1/2,k=1\) yields (K3) and the factor-two witness to (K4).
- **\(N=2\):** \(A=\begin{pmatrix}2&-2\\-2&2\end{pmatrix}\); (G2) gives gap drift \(2K(y_1/2)\) at \(V=0\), and (G1) gives \(d\langle y_1\rangle=16\beta_N^{-1}dt\), agreeing with direct subtraction of the two particle equations. Counting the cyclic neighbor only once would be wrong here.
- **\(N=3\):** \(A\) has diagonal 2 and off-diagonal \(-1\); gap variances are \(36\beta_N^{-1}dt\), cross-variations \(-18\beta_N^{-1}dt\), and the total-gap bracket vanishes.
- **\(K=0,V=0\):** the drift vanishes and the noise in (G1) is exactly the difference noise. Constant tests have zero drift and bracket.
- **Constraint:** \(A\mathbf1=0\) verifies every contraction preserves \(\sum_i y_i=N\).
- **Iid law:** (F1) is an independent probability calculation and produces the counterexample to uniform-temperature import.

`python3 scripts/verify_campaign.py` passed at intake. The baseline imported note hash was verified as `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`; its seven pages were extracted and read as unverified input, not as a source theorem. No library was installed. PDF text extraction used the bundled `pypdf`; rendered evidence used `pdftoppm`. The first renderer invocation emitted a fontconfig configuration warning; it completed, and the displayed relevant pages were visually inspected and readable.

### Retained local evidence

The following files remain under `BUILD/ordered-sources/` in the assigned worktree, and are intentionally not committed:

| File | Evidence |
|---|---|
| `2112.05881v5.pdf` | Exact downloaded primary bytes with the hash above. |
| `2209.00396v4.pdf` | Exact downloaded primary bytes with the hash above. |
| `2112.05881v5.txt`, `2209.00396v4.txt` | Full extraction, explicitly tagged with one-based PDF page numbers. |
| `local-p1.png` | Printed p. 1 / PDF index 0: (1.1)–(1.4), especially the denominator in (1.3). |
| `local-p4.png` | Printed p. 4 / PDF index 3: Theorem 1, Assumption 1.1, variance coefficient (1.10). |
| `local-p5.png` | Printed p. 5 / PDF index 4: Theorems 2–3 and temperature-dependent constants. |
| `local-p13.png` | Printed p. 13 / PDF index 12: Fourier convention and fractional inverse multiplier. |
| `local-p15.png` | Printed p. 15 / PDF index 14: the Step 3 coefficient incompatible with printed (1.3). |
| `corr-p3.png` | Printed p. 3 / PDF index 2: SRC-006 Theorem 1, including printed derivative arguments. |
| `note_v2.txt` | Page-tagged extraction of the frozen seven-page campaign input. |

All six listed source-page PNGs were opened for visual inspection. Their paths are recoverable from the worktree path at the top of this report. The root should preserve the PDF bytes and these page images with the source-audit checkpoint if this worktree is later removed.

The sole authoritative report created by this lane is `SOURCES/ROUND_001_ORDERED.md`; the source cache is supporting evidence. Pre-existing untracked task cards were preserved. No source input, baseline file, branch, canonical state file, or remote was changed.

**Gate changed:** `SRC-005` and `SRC-006` are located and version-locked; the Hamiltonian and kernel maps are explicit; the numerical SRC-005 covariance is quarantined as `SOURCE_MISMATCH`; an unqualified temperature-uniform source import is `DISPROVED`; the dynamic route is reduced to the precise estimates (R1)–(R3) and the listed law/cutoff bridges. The campaign theorem remains open.

**Next executable actions:** independently audit (K2)–(K5) against the retained page images; trace the covariance proof with the corrected kernel constant before any numerical import; select the actual post-hierarchy residual and attempt (R1)–(R3) at fixed cutoff and a separately declared preparation law. Root integration should update the existing rows above, without treating this same-context report as an independent audit.
