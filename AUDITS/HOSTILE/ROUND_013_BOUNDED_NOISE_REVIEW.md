# TASK072: hostile examination of the frozen THM034 bounded-noise candidate

Issued 2026-09-18 UTC. Reviewer lane: /root/r013_noise_hostile. Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r013-noise-hostile. Branch: codex/hocf-r013-noise-hostile, created from the prescribed published R9 commit 29d7ce427ad7a98739b18d07781e71c4598b3579.

**Verdict: CONDITIONAL PASS for every frozen THM034 assertion.** The complete supplied R13 argument proves its additional uniform bounded-diffusivity noise conclusion, conditional on the exact earlier source, inverse, differentiation, particle/domain, Haar-energy, and R10 floor/clipping premises identified below. No unsupported new line, admitted counterexample, missing physical factor, or necessary repair was found. The conclusion is the actual full-corrector bracket, not only its clipped part or a subfamily with bounded rescaled diffusivity.

This is a hostile review of a supplied proof, not a statement-only reconstruction. It does not certify an earlier module merely because a theorem card or source addendum mentions an audit. Every such module retains its supplied conditional status. The root alone compares the separate current reviews and decides promotion. No canonical record, earlier report, or candidate was edited.

The examined constructor is MEMORANDA/ROUND_013_BOUNDED_NOISE_SMALL_RIESZ.md, SHA-256 5fbf1dfd2895ed239a7149d7c356bd836b593dc6c6c60277180d0350801fa8a7. The frozen statement is THEOREMS/THM-034_BOUNDED_NOISE_SMALL_RIESZ.md, SHA-256 d4033888db7b7ae91bd826e31713a7ab5a0855e809a118c6277d12685a925a97. Both were read in full after all 28 permitted inputs had been copied and checked against the supplied manifest.

## 1. Assertion, negation, and review boundary

The fixed data are integer \(d\ge4\), \(0<s<2\), finite \(T\ge0\), a real smooth terminal test \(h\), finite \(\nu_*\ge0\), and the frozen coefficient-one periodic Riesz kernel and R7 weights. For every integer \(N\ge2\) and \(0<\nu\le\nu_*\), set

\[
 p=s+2,\qquad a=\frac{s}{p},\qquad \theta=1-\frac{s}{d},
 \qquad b=\min(1,\nu^{-1}),\qquad \sigma_N^2=Nb.
\]

The process is the actual homogeneous gradient particle system, with zero external drift, force \(K=-\nabla g\), noise \(\sqrt{2\nu}\), iid unit-Haar initial positions, and independent Brownian drivers. The reference is unit Haar. The test is the actual backward Fourier solution. The pair inverse is the genuine bounded Borel terminal-zero full inverse including both responses; its classical/Itô realization is an explicit conditional prerequisite.

For each fixed
\[
 1<q<\min(d-2,d/2),\qquad q\le s+1,\qquad
 \eta=s+1-q<2,
\]
the first claim is
\[
 \sup_{0\le t\le T}\sup_{x\ne y}
 \frac{|\nabla_{x,y}\Phi_t(x,y)|}{w_q(x-y)}
 \le C_q\min\!\left(N^{\eta/p},\nu^{-\eta/2}\right).
 \tag{H1}
\]
The corrector statistic has ordered distinct labels, denominator \(N^2\), coefficient \(1/2\), and its original mean-field background subtraction. Its expected scaled bracket is
\[
 Q_N=2\nu Nb\,\mathbb E\int_0^T
          \sum_i|\nabla_iP_N[\Phi_t](X_t)|^2\,dt.
 \tag{H2}
\]
At positive noise the second bound is
\[
 Q_N\le Cb\min\!\left(N^a,\nu^{-s/2}\right)
                   (N^{-\theta}+\nu).
 \tag{H3}
\]
The remaining claims are the uniform limit on the entire closed bounded noise interval, the five-term sufficient rate stated in THM034, boundedness of the actual leading scaled bracket, and uniform disappearance of the expected integral of the absolute scaled cross-variation. At zero noise \(Q_N=0\) is defined directly by the noise coefficient.

The exact logical negation is one admitted fixed tuple and either a violating \(N,\nu\) family for (H1)/(H3), a sequence with positive limiting upper bracket, or a failure of one of the other asserted uniform bounds. The review tried to realize this negation by challenging the one-sided Jacobian, both response slots, true-inverse identification, energy occupation, clipping recentering, finite-label contractions, and every endpoint/rate. It did not find such an instance.

The proof reviewed below retains the frozen statement exactly. It introduces no extra condition on \(\nu N^{2/p}\), no assumption that \(\nu\) has a limit, and no silently restricted temperature sequence.

## 2. Source and normalization preflight

Only the 28-file permitted dossier was used as mathematical evidence. The following table records the exact inputs needed by the new implication, rather than importing all claims in each historical report.

| Supplied input | Exact use and limit of that use |
|---|---|
| ROUND_001_MODEL and ROUND_001_ALGEBRA, Sections 1–3 and 5 | Unit Haar mass, \(e^{2\pi i k\cdot x}\), \(K=-\nabla g\), noise \(\sqrt{2\nu}\), ordered distinct labels, \(P_N=U_2/2\), denominator \(N^2\), and mean-field centering. The derivative and all new square coefficients are recomputed below. |
| THM021 and ROUND_004_SINGULAR_RESPONSE, Sections 2–4 | Exact heat representation, local coefficient one, smooth even remainder, finite signed divergence measure, compensation, and both homogeneous response convolutions. No unseen R4 audit supplies evidence. |
| THM023/024/025, complete R5 pair/response/interface reports, and the two supplied R5 clarifications | Noncolliding auxiliary pair evolution, bounded absolute source occupation, genuine bounded Borel full inverse and uniqueness, pair-exchange symmetry, exact Fourier test, and fixed uniform response/propagation constants. “Symmetric” means pair exchange, not self-adjoint base evolution. |
| THM027 and ROUND_007_WEIGHTED_PAIR_GRADIENT, Sections 2–8 | Fixed periodic weights, one-sided Jacobian, fixed-\(N\) higher moments and common-start differentiability, legitimate differentiated expectation formulas, weighted convolution bounds, and identification with the existing full inverse. Its old \(N\)-dependent constants are not used as uniform estimates. |
| THM026 and ROUND_006_SINGULAR_PARTICLE_REALIZATION, Sections 3–8 | Actual singular particles, finite-\(N\) noncollision and same-driver heat passage, bounded densities at fixed \(N\), and the exact globally integrable energy identity. No uniform density comparison is inferred. |
| THM028 and ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN, especially Sections 6–11 | The same full inverse has the needed local regularity, differentiated backgrounds, weak derivatives, and exact actual true-martingale bracket after collision-stop removal. This is a conditional domain premise, not a new R13 singular Itô theorem. |
| THM029 and ROUND_009_HAAR_NOISE_ENERGY, Sections 2–9 | Conditional uniform Haar energy \(\nu\int\|\nabla_{x,y}\Phi\|_2^2\le C_E N^a\), exact Haar and exchangeable square formulas, and one-body Haar preservation. The supplied Haar result is not called an actual-law result. |
| THM031 and ROUND_010_ACTUAL_LAW_FALSIFICATION, Section 3, (3.1)–(3.5) | The sharp deterministic floor \(H_N\ge-CN^{s/d}\), derived from the positive heat-integral truncation with the exact self subtraction. Its smoothing theorem, later-time covariance assertions, and shrinking-time corollary are not needed. |
| THM030 and ROUND_010_ACTUAL_NOISE_LAW_TRANSFER, Sections 2–7 | Actual singular free energy, marginal entropy, bounded-test transfer, recentered radial clipping, and the physical clipped-bracket estimate. This complete proof, including its weaker \(N^a\) floor and conditional R9 Haar input, supplies the clipping premise as issued. |

The R10 report mentioning a blind R9 proof does not import that non-allowlisted proof into this review. The supplied complete R9 constructor gives the specific Haar premise used here. Similarly, the existence or alleged success of current R11/R12 constructions or audits is not an input. R13's references to those rounds describe construction history only.

The normalization checks are direct. With
\[
 A_{d,s}=\frac{4^{(d-s)/2}\pi^{d/2}}{\Gamma(s/2)},\qquad
 \alpha=\frac{d-s}{2},
\]
the nonzero coefficient of
\[
 A_{d,s}\int_0^\infty t^{\alpha-1}(p_t-1)\,dt
\]
is
\[
 \frac{A_{d,s}\Gamma(\alpha)}
 {(4\pi^2|k|^2)^\alpha}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}
   |k|^{s-d}.
\]
The Euclidean Gaussian substitution \(u=|z|^2/(4t)\) gives local principal term \(|z|^{-s}\) with coefficient one. On the present range \(s<d-2\), hence
\[
 D_{\rm cl}(z)=s(d-2-s)|z|^{-p}+\text{smooth local remainder}.
 \tag{H4}
\]
The positive coefficient is strictly nonzero, \(p<d\), and the exact torus divergence has total mass zero. It is not globally a positive density. Its Fourier multiplier is \(4\pi^2c_{d,s}|k|^{s+2-d}\). The homogeneous sum of responses therefore has multiplier minus the sum of the two slot multipliers. The Fourier test uses the damping
\[
 \exp\!\left[-(T-t)
     \{4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{s+2-d}\}\right].
\]
Its spatial derivatives of every fixed order are bounded by the corresponding absolutely summable Fourier seminorm of \(h\), uniformly in \(t,N,\nu\). This verifies the source-gradient constant used by R13.

## 3. Per-claim verdicts

All locations in this table refer to the frozen R13 memorandum; equation numbers are its equation numbers. A conditional pass preserves exactly the source premises in Section 2.

| ID | Frozen claim and location | Verdict | Decisive verification |
|---|---|---|---|
| H-C01 | Model, full inverse, physical normalization, lines 7–13 | CONDITIONAL PASS | Correct actual law, both responses, \(1/(2N^2)\), background \(1/N\), and \(\sigma_N^2=Nb\); no claimed domain follows from Borel existence alone. |
| H-C02 | Favorable weight generator, (2.1)–(2.2), lines 17–29 | PASS | Relative diffusion is \(2\nu\); largest transverse Jacobian eigenvalue is \(2s|z|^{-p}/N\); both retained coefficients are strictly favorable. |
| H-C03 | Singular stopped bounds, (2.3), lines 31–39 | CONDITIONAL PASS | Positive terminal and occupation terms pass at fixed \(N,\nu\) by Fatou/monotone convergence after noncollision; no terminal uniform integrability is asserted. |
| H-C04 | Source splits and genuine base derivative, (3.1)–(3.2), lines 43–54 | CONDITIONAL PASS | Both scales give their claimed powers; the derivative formula is supplied before applying the new first-moment estimates. \(\eta=0\) is valid. |
| H-C05 | Both responses, genuine full inverse, (3.3), lines 56–64 | CONDITIONAL PASS | The homogeneous derivative bound has no amplitude term; its coefficient is \(2C_{D,q}\). Backward Volterra/Gronwall uses finite fixed-\(N\) regularity only for legitimacy. |
| H-C06 | Actual occupation, (4.1), lines 68–72 | CONDITIONAL PASS | Exact energy factor is \(\nu(N-1)\); sharp floor and positive punctured divergence give the claimed \(N^{-\theta}+\nu\). |
| H-C07 | \(q_*=p/2\) and full bracket, (4.2)–(4.3), lines 74–83 | CONDITIONAL PASS | \(2q_*=p<d\); squared gradient scale is \(\min(N^a,\nu^{-s/2})\). Direct actual square yields precisely \(4\nu b\) and \((N-1)^2/N^2\). |
| H-C08 | Low-noise supremum, (4.4), lines 85–90 | PASS | Split at \(N^{-2/p}\); \(a-\theta<0\) and \(1-s/2>0\). Empty subintervals cause no change. |
| H-C09 | \(q_-\), radial clipping, own mean, (5.1), lines 94–103 | PASS | \(q_-=1+s/4\) is admitted; \(r=p/q_->2\); \(w_{q_-}^r=w_p\) exactly. Clipping need not be a potential gradient. |
| H-C10 | Actual residual bracket, (5.2), lines 105–110 | CONDITIONAL PASS | Occupation controls \(\nu\) times the moment. No additional \(\delta^{-1}\) is lost; the background is the tail's own mean. |
| H-C11 | Actual clipped bracket, (5.3), lines 112–117 | CONDITIONAL PASS | Complete supplied R10 entropy/clipping proof applies with the identical \(G\), law, mean, and scaling; \(b\sqrt\nu\le1\). |
| H-C12 | Entire bounded interval, line 119 | CONDITIONAL PASS | Probability-time-particle \(L^2\) decomposition, fixed-\(\delta\) tail, and low-noise supremum cover every noise choice depending arbitrarily on \(N\). |
| H-C13 | Five-term rate, (6.1), lines 123–135 | PASS, GIVEN THE PRECEDING ESTIMATES | All arithmetic identities and signs check. The faster low-noise term is legitimately absorbed. |
| H-C14 | Zero noise, leading bracket, absolute cross-variation, lines 13 and 135 | CONDITIONAL PASS | No reciprocal at zero; actual leading bracket is bounded by \(2T\|\nabla f\|_\infty^2\); absolute cross-variation is bounded by the product of bracket norms. |
| H-C15 | Exact scope and exclusions, lines 137–141 and THM034 | PASS | No dimension-three, \(s=2\), Coulomb, logarithmic, general-background, unbounded-noise, cubic-residual, or fluctuation-law assertion is inferred. No necessity claim is made. |

No finding requires an in-place correction, and none was made.

## 4. Recomputed Jacobian, stopped estimate, and derivative identification

Write \(\rho=|z|\) in the fixed inner chart, \(z=x-y\), and \(K=s\rho^{-p}z+k(z)\), where \(k(0)=0\) and \(|k(z)|\le H\rho\). The principal pair-drift Jacobian is
\[
 \frac1N\begin{pmatrix}DK&-DK\\-DK&DK\end{pmatrix},
 \qquad DK=s\rho^{-p}(I-p\,e\otimes e),\quad e=z/\rho.
\]
The center eigenvalues are zero. The difference eigenvalues are \(2s\rho^{-p}/N\) transversely and \(-2s(s+1)\rho^{-p}/N\) radially. Thus the largest symmetric eigenvalue is the transverse one, not the absolute operator norm. R7's \(\ell\) includes this singular upper bound and a smooth \(O(N^{-1})\) remainder.

For \(w_q=\rho^{-q}\) in the inner ball,
\[
 \Delta_z w_q=q(q+2-d)\rho^{-q-2},\qquad
 \frac2N K\cdot\nabla_z w_q
 =-\frac{2sq}{N}\rho^{-q-p}+O(N^{-1})w_q.
\]
Both particle Laplacians produce \(2\nu\Delta_z\). Adding the Jacobian potential gives exactly the two leading terms in R13 (2.1):
\[
 -2\nu q(d-2-q)w_{q+2}
 -\frac{2s(q-1)}Nw_{q+p}.
 \tag{H5}
\]
Both coefficients are strictly positive when moved to the left. A smooth annulus contributes only \(C(\nu+N^{-1})w_q\), and \(\nu\le\nu_*\), \(N\ge2\) make this uniformly bounded.

For specificity, let \(A_j\) be the R7 annular supremum of the absolute first derivative or Laplacian of \(w_q\), divided by \(w_q\), let \(K_0,K_1\) be the off-inner-ball force and Jacobian bounds, and let \(L_k=\max(H,K_1)\). One may bound the nonnegative remainder by the maximum of
\[
 qH+L_k,\qquad
 2\nu_*A_2+K_0A_1+sR^{-p}+L_k,\qquad 0.
\]
This is independent of \(N,\nu,t\). Reducing either negative coefficient only weakens the inequality. Thus the global R13 (2.2) is a genuine estimate on the given periodic auxiliary generator, not merely on a Euclidean diagnostic.

For a fixed off-diagonal start, stop before separation \(\varepsilon\). Apply smooth Itô to
\[
 e^{-C(u-t)+\int_t^u\ell(Z_v)\,dv}w_q(Z_u)
\]
up to that stop. Its positive terminal expectation plus the two retained positive weighted occupations is bounded by \(w_q(z)\). Every stopped stochastic integrand is bounded on a compact collision-excluded set. At each fixed \(N,\nu\), imported noncollision makes the stops exhaust the horizon. Fatou gives the terminal bound; positive occupation convergence gives the other two inequalities. Removing \(e^{-C(u-t)}\) costs at most \(e^{CT}\). This proves R13 (2.3) with uniform coefficients. No exchange of this singular limit with an \(N\)-limit occurs.

The source calculation gives
\[
 \nabla_xJ=DK(z)^T(\nabla f(x)-\nabla f(y))+D^2f(x)K(z),
\]
and the analogous second derivative slot. The difference of test gradients supplies one power of separation. Hence \(|\nabla_{x,y}J|\le C_h w_{s+1}\), uniformly in the displayed parameters.

Let \(\eta=s+1-q\). In the inner ball,
\[
 w_{s+1}
 \le N^{\eta/p}w_q
      +N^{\eta/p-1}w_{q+p},
 \qquad
 w_{s+1}
 \le \nu^{-\eta/2}w_q
      +\nu^{1-\eta/2}w_{q+2}.
 \tag{H6}
\]
These are \(x^\eta\le1+x^m\), with \(m=p\) and \(m=2\), respectively. Since \(\eta<2<p\), both are valid, including \(\eta=0\). On the complement the weights are bounded. Its second bound costs at most a fixed power of \(\nu_*\), not an uncontrolled power of the selected \(\nu\).

R7 Sections 4–5 establish common-start differentiation and moments above one at every fixed \(N,\nu\); these justify
\[
 \nabla U_t(z)=
 \mathbb E_{t,z}\int_t^T A_{t,u}^{\,T}\nabla J_u(Z_u)\,du,
 \qquad
 \nabla S_{t,u}F=
 \mathbb E_{t,z}[A_{t,u}^{\,T}\nabla F(Z_u)].
 \tag{H7}
\]
The old constants in those uniform-integrability arguments may depend severely on \(N\). R13 does not use them to estimate (H7). It estimates the already justified identities using (H5)–(H6) and the new first-moment occupations. This distinction is valid: each equality is obtained first at fixed \(N,\nu\), while the resulting inequalities have newly controlled constants.

For a bounded C1 off-diagonal \(F\) in the supplied weighted class, its global weak gradient is integrable. Translation/Fubini differentiates the two homogeneous responses without differentiating the measure \(D\):
\[
 \nabla RF=-\int\nabla F(x+w,y)\,D(dw)
           -\int\nabla F(x,y+w)\,D(dw).
\]
R7's separated-singularity estimate gives
\[
 |RF|_q\le2C_{D,q}|F|_q.
 \tag{H8}
\]
The density-gradient amplitude terms in the general R7 formula vanish because \(\mu=1\). No value norm is needed in (H8), and no response is omitted.

The fixed-\(N\) R7 inverse is already the same bounded Borel Volterra inverse as the full-pair module. It has a finite time-uniform weighted gradient. Differentiating its Volterra equation is legitimate by (H7)–(H8), and yields, for \(D_q(t)=|\Phi_t|_q\),
\[
 D_q(t)\le C\min(N^{\eta/p},\nu^{-\eta/2})
   +2C_{D,q}\int_t^T e^{C(u-t)}D_q(u)\,du.
\]
Backward Gronwall, or factorial Volterra iteration with the known finite fixed-\(N\) supremum, proves (H1). The prefactor depends only on \(q\) and the fixed data. This is true-inverse identification followed by an estimate; existence or uniqueness is not inferred from a derivative seminorm.

## 5. Actual energy occupation and the complete bracket factor

For the actual particles put
\[
 H_N=\frac1N\sum_{i<j}g(X_i-X_j),\qquad
 B_i=\frac1N\sum_{j\ne i}K(X_i-X_j).
\]
The exact R6 energy identity, restored from its harmless shift, is
\[
 \mathbb EH_N(X_T)+
 \mathbb E\int_0^T\sum_i|B_i|^2\,dt+
 \nu(N-1)\mathbb E\int_0^T D_{\rm cl}(X_1-X_2)\,dt=0.
 \tag{H9}
\]
Indeed \(\Delta_{Nd}H_N=(2/N)\sum_{i<j}\Delta g\); exchangeability gives exactly \(N-1\). The iid initial expectation is zero because \(g\in L^1\) and \(\int g=0\). At positive noise, the absolute Laplacian occupation and true energy martingale are part of the supplied stopped R6 argument, before taking this expectation. A formal singular integration by parts is not being substituted.

The R10 sharp floor follows by truncating the heat representation at \(r_N=N^{-2/d}\). Positivity gives the comparison error \(CNr_N^{(d-s)/2}\), while the exact deleted self term is one half of the truncated kernel at zero, bounded by \(Cr_N^{-s/2}\). Both powers are \(N^{s/d}\). This rechecks the claimed scale and the self factor. This truncation is distinct from the heat convolution used to construct the actual particles.

From (H4), the fixed weight satisfies \(D_{\rm cl}\ge c w_p-C\) with \(c>0\). Discarding only the complete nonnegative force square in (H9), applying the sharp floor, and using \(N/(N-1)\le2\) gives
\[
 \nu\,\mathbb E\int_0^T w_p(X_1-X_2)\,dt
 \le C(N^{-\theta}+\nu).
 \tag{H10}
\]
No positive individual pair-force square is extracted from the total-force square. The smooth torus compensation contributes the retained \(C\nu\) term.

Take \(q_*=p/2=1+s/2\). It lies strictly below both \(d-2\) and \(d/2\), and its \(\eta=s/2\). Squaring (H1) yields
\[
 |G_t(x,y)|^2\le C M\,w_p(x-y),\qquad
 M=\min(N^a,\nu^{-s/2}),\quad G=\nabla_x\Phi.
 \tag{H11}
\]
Since \(p<d\), \(\int w_p<\infty\). Put \(A(x)=\int G(x,y)\,dy\).

Direct differentiation of the ordered statistic, before any law argument, gives
\[
 v_i=\nabla_iP_N[\Phi]
 =\frac1{N^2}\left[\sum_{j\ne i}G(X_i,X_j)-N A(X_i)\right].
 \tag{H12}
\]
The two orientations of each pair cancel the original factor \(1/2\). The subtracted coefficient is \(N\), not \(N-1\). Equivalently, after row centering \(H=G-A\), the remaining deletion term is \(-A\).

For any configuration, finite-sum Cauchy–Schwarz gives
\[
 \left|\sum_{j\ne i}G_{ij}-N A_i\right|^2
 \le2(N-1)\sum_{j\ne i}|G_{ij}|^2+2N^2|A_i|^2.
\]
Exchangeability and actual one-body Haar invariance, followed by multiplication by \(2\nu Nb\), therefore give exactly
\[
 Q_N\le4\nu b\int_0^T
 \left[\frac{(N-1)^2}{N^2}\mathbb E|G_{12}|^2+
                         \|A\|_2^2\right]dt.
 \tag{H13}
\]
Jensen bounds the background by \(CM\int w_p\); (H10) handles the actual pair term. This proves (H3), including its dependence on \(b\). It does not use product-law cancellation at positive time.

## 6. Clipping preflight and the actual singular tail

The direct estimate (H3) is not alone sufficient at a fixed positive noise: its second term need not tend to zero. R13 explicitly supplies the required actual-law clipping step.

For the low-noise interval \(0<\nu\le\delta\le\min(1,\nu_*)\), split at \(\nu_0=N^{-2/p}\). Below this scale,
\[
 Q_N\le C[N^{a-\theta}+N^{(s-2)/p}].
\]
Above it and below \(\delta\),
\[
 Q_N\le C[N^{a-\theta}+\delta^{1-s/2}].
\]
These inequalities imply R13 (4.4). The gap identity is
\[
 a-\theta=\frac{s(s+2)-2d}{d(s+2)}<0,
\]
because \(s(s+2)<8\le2d\). Also \(1-s/2>0\).

On \(\delta\le\nu\le\nu_*\), take \(q_-=1+s/4\), \(\eta_-=3s/4\), and
\[
 r=\frac{p}{q_-}=\frac{4(s+2)}{s+4}>2.
\]
These exponents meet every hypothesis of (H1), and \(w_{q_-}^r=w_p\) by the exact common-base weight convention. Thus
\[
 |G|\le C\delta^{-\eta_-/2}w_{q_-}.
\]
With radial clipping \(G^L=G\min(1,L/|G|)\), assigned zero when \(G=0\), set \(R_L=G-G^L\) and \(A_R=\int R_L\,dy\). The elementary scalar inequality is
\[
 |R_L|^2=(|G|-L)_+^2
 \le L^{2-r}|G|^r
 \le C\delta^{-\eta_-r/2}L^{2-r}w_p.
 \tag{H14}
\]
Reusing (H13) for this vector field and its own row mean gives
\[
 \mathcal T_N(L)
 \le Cb\,\delta^{-\eta_-r/2}L^{2-r}(N^{-\theta}+\nu)
 \le C\delta^{-\eta_-r/2}L^{2-r}.
 \tag{H15}
\]
The physical \(\nu\) is already absorbed into the actual occupation (H10); dividing (H10) by \(\nu\) and then introducing an extra \(\delta^{-1}\) would be an unnecessary loss. The same physical factor multiplies the Haar background term, leaving a bounded \(\nu\) contribution. All constants in (H15) are independent of \(N,\nu,\delta,L\); the displayed \(\delta,L\) factors contain their dependence.

The supplied R10 clipping result has exactly the field
\[
 v_i^L=N^{-2}\left[\sum_{j\ne i}G^L(X_i,X_j)-N A^L(X_i)\right],
 \qquad A^L=\int G^L\,dy.
\]
The continuous and measurable domain input makes the fields predictable; bounded clipping gives a true martingale. It need not be a gradient of any new pair kernel. The full and residual martingales are genuine square-integrable objects at each fixed \(N\) by the conditional domain theorem.

For clarity, the source chain for the clipped estimate was recomputed:

1. The smooth actual free energy has dissipation
   \(-\int F|\nu\nabla\log F+\nabla H_N^\varepsilon|^2\), starting from zero. Its \(\nu^2\) coefficient in the Fisher square is correct. Fixed-\(N\) same-driver heat convergence, the common energy lower bound, Fatou, and weak lower semicontinuity of entropy pass only the free-energy inequality to the singular law.
2. R10's weaker floor \(H_N^\varepsilon\ge-C_0N^a\) suffices to give \(\operatorname{Ent}(F_N)\le C_0N^a/\nu\). This is a different bound from the sharper floor used in (H10); no exponent is conflated.
3. Exchangeability and one-body Haar give \(\operatorname{Ent}(F_k)\le(k-1)\operatorname{Ent}(F_N)/(N-1)\). The bounded-test errors satisfy \(e_{k,N}\le2\sqrt{C_0(k-1)/\nu}\,N^{-1/p}\) for \(k=2,3\) when that marginal exists.
4. For \(H^L=G^L-A^L\), \(|G^L|,|A^L|\le L\), \(|H^L|\le2L\). The exact exchangeable square retains the pair, ordered triple, mixed, and one-body terms with coefficients \(N-1\), \((N-1)(N-2)\), \(-2(N-1)\), and \(1\), respectively, and outer coefficient \(N^{-3}\) before physical scaling.
5. Comparing that square with product Haar gives
   \[
   |Q_N^L-(Q_N^L)^{\rm Haar}|
   \le8\nu bTL^2\frac{N-1}{N^2}
               [2e_{2,N}+(N-2)e_{3,N}].
   \]
   The triple term is absent at \(N=2\). The supplied conditional R9 energy and the exact Haar square give
   \((Q_N^L)^{\rm Haar}\le C_E bN^{-2/p}\).

Consequently the complete supplied estimate is
\[
 Q_N^L\le C_EbN^{-2/p}
       +16T\sqrt{2C_0}\,b\sqrt\nu\,L^2N^{-1/p}.
 \tag{H16}
\]
The factor \(b\sqrt\nu=\min(\sqrt\nu,\nu^{-1/2})\le1\) is correct even when \(\nu_*>1\). With \(L_N=N^{1/(4p)}\), this is exactly R13 (5.3).

Finally \(v=v^L+v^{R_L}\) with the respective own means, so in probability-time-particle \(L^2\),
\[
 Q_N\le2Q_N^{L_N}+2\mathcal T_N(L_N).
 \tag{H17}
\]
No orthogonality or vanished cross term is presumed. For fixed \(\delta>0\), (H15) tends to zero uniformly on \([\delta,\nu_*]\), because \(r>2\). The low-noise estimate tends to zero after first \(N\to\infty\) and then \(\delta\downarrow0\). This proves the whole bounded-interval limit. The tail estimate is under the actual law and closes the simultaneous clipping passage; a fixed-\(N\) density comparison is not used for that limit.

## 7. Rate, cross-variation, and endpoint stress tests

Choose precisely the candidate's \(\delta_N=N^{-\epsilon}\) with \(\epsilon=1/(6p^2)\). At every fixed \(\nu_*>0\), it eventually lies below \(\min(1,\nu_*)\), and \(\epsilon<2/p\). Direct arithmetic gives
\[
 r-2=\frac{2s}{s+4},\quad
 \frac{\eta_-r}{2}=\frac{3sp}{2(s+4)},\quad
 \epsilon\frac{\eta_-r}{2}-\frac{r-2}{4p}
       =-\frac{s}{4p(s+4)},\quad
 \epsilon(1-s/2)=\frac{2-s}{12p^2}.
\]
The low-noise term \(N^{(s-2)/p}\) decays faster than \(N^{-(2-s)/(12p^2)}\). The resulting uniform sufficient rate is therefore exactly
\[
 Q_N\le C\left[
 N^{a-\theta}+N^{-(2-s)/(12p^2)}
 +N^{-s/(4p(s+4))}+N^{-1/(2p)}+N^{-2/p}\right].
 \tag{H18}
\]
Every exponent is strictly negative for the fixed admitted data. No limit is taken in \(s,d,q,T\) or \(\nu_*\). The threshold for “sufficiently large \(N\)” may depend on the fixed positive \(\nu_*\), which is allowed. R13 explicitly disambiguates its last two shorthand exponents, so no parsing correction is needed.

The leading martingale has configuration field \(N^{-1}\nabla f_t(X_i)\). Its expected actual scaled bracket is
\[
 Q_{1,N}=2\nu b\int_0^T\|\nabla f_t\|_2^2\,dt
 \le2T\sup_t\|\nabla f_t\|_\infty^2,
\]
using the actual one-body Haar marginal and \(\nu b\le1\). Applying Cauchy–Schwarz first to the particle/vector sum and then to probability and time, with the common physical measure factor, gives
\[
 \mathbb E\int_0^T
 \left|2\nu Nb\sum_i
   \frac{\nabla f_t(X_i)}N\cdot v_i(t,X_t)\right|dt
 \le\sqrt{Q_{1,N}Q_N}.
 \tag{H19}
\]
The absolute value is inside expectation and time integration. This is the claimed absolute cross-variation bound.

The endpoint and law checks have the following outcomes:

| Stress test | Outcome |
|---|---|
| \(N=2\) | (H12)–(H13) remain exact; no third marginal or \(X_3\) is required by clipping. The exact Haar coefficient is \(\|G\|_2^2/8\). |
| \(N=3\) | The triple coefficient is present and equals \((N-1)(N-2)=2\); the mixed term remains. |
| \(\nu=0\) or \(\nu_*=0\) | All noise and cross-variation functionals are zero directly. No \(\nu^{-1}\), \(0\cdot\infty\), or zero-noise entropy division is used. |
| \(\nu=\nu_N\) arbitrary in the interval | The low/high split and quantitative rate cover oscillating sequences, fixed positive noise, and every approach to zero. |
| Constant \(h\), or \(T=0\) | The source and inverse, or the time integral, vanish. |
| \(\eta=0\) | Both source comparisons and the resulting min bound are valid; the powers equal one. |
| \(q\downarrow1\) or \(q\uparrow d-2\) | Constants may deteriorate. The claim fixes \(q\) strictly inside the interval and asserts no endpoint-uniform constant. |
| \(d=3\) | The interval \(1<q<d-2\) is empty. This proof gives no dimension-three conclusion. |
| \(s=2\) | Low-noise power \(1-s/2\) vanishes; at \(d=4\), the chosen weight and floor gap also reach boundaries. Exclusion is necessary for this proof, not a claim of falsity beyond it. |
| \(s\downarrow0\) | No uniform exponent or constant is asserted; the logarithmic normalization is separate and is not obtained by substitution. |
| General background or actual higher marginals treated as iid | Not admitted. The response derivative amplitude term and law estimates would require different premises. No such substitution occurs. |
| Unbounded \(\nu_*\) | The annular constants use a fixed upper noise bound; no uniformity in that bound is proved. |

No result about the cubic drift residual, lower contractions, evolved endpoint concentration, a higher hierarchy, Gaussianity, or another fluctuation law follows from this noise theorem. The old energy-floor condition and the full microscopic subcritical and positive finite critical conditions retain their different exponents.

## 8. Diagnostics, isolation, and final disposition

The fresh standard-library program in ROUND_013_NOISE_HOSTILE_ARTIFACTS/hostile_exact_checker.py performs **56,353 exact checks** using fractions and integers, with no random seed, floating tolerance, third-party library, network access, or prior checker import. The issued exact_results.json records every check group.

The program reconstructs the pair Jacobian as a full block matrix, differentiates the radial weight, checks the source's local homogeneity, verifies rate identities and endpoint signs, and independently differentiates an ordered symmetric polynomial statistic. It tests the full/clip/tail field decomposition and all four contractions under dependent finite exchangeable laws with uniform one-body marginals for \(N=2,3,4,5\). These tests include nonzero triple, mixed, and clip-tail cross terms. It verifies both response slots on finite Fourier characters and their translation-difference commutation. The finite laws and local polynomials are coefficient diagnostics, not purported actual singular particle laws or periodic test solutions.

The analytic arguments in Sections 4–7, not the finite tests, establish the conditional mathematical verdict. In particular no finite computation certifies expectation differentiation, singular stop removal, entropy lower semicontinuity, or the continuum uniform limit.

The unavoidable initial exposure consisted of the supplied global/app instructions, the user's project contract, and the automatically included high-level memory summary. No memory file was opened or used. The first deliberate reads were TASK072 and its input manifest. The prescribed R9-base worktree was then created, only the manifest's 28 files were copied from the root, and every copied byte string was hash-checked before reading its mathematics. Non-allowlisted inherited worktree files, current state/history, current blind output, current R11/R12/R13 material outside the dossier, and standalone prior checker programs/results were not opened. Historical constructor reports contain their own embedded descriptions of old checks and audits; those permitted-document summaries were encountered but supply no evidence for this verdict. R13's own disclosed construction exposure was read as part of the required complete candidate.

The input manifest, verified input inventory, read-scope/exposure record, exact program/results, output manifest, and immutable archive accompany this report. The archive carries the exact permitted dossier so that the checked source scope is recoverable without current state or chat history. Originals and the root remain unchanged.

**Disposition:** accept THM034 as the precise conditional implication stated in the frozen candidate. No in-place repair, weakened theorem, new assumption, or admissible falsification is required by this review. The remaining dependency is acceptance of the expressly conditional upstream modules through their own gates; unseen audit status is not substituted for it. Even if those gates are accepted, the campaign's actual evolved cubic residual and remaining theorem ranges are separate obligations. This lane assigns no canonical promotion.
