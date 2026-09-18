# TASK070 — complete statement-only reconstruction of THM030 and THM031

**Verdict: both complete bounded assertions reconstruct, conditional on the supplied prior modules in their issued scopes.** This is a fresh construction and same-context falsification check, not the separate hostile review or a promotion decision. In particular the complete THM028 domain premise and the integrated THM029 Haar-energy premise have not been independently certified here. The actual unsmoothed singular-noise limit remains unproved.

The report covers the entropy, clipping, Fourier, smoothing, path, centering, initial-covariance and shrinking-window claims in both frozen cards and their statement-only supplement. No failed line was found within those conditional claims. The first additional unproved line is the vanishing of the actual complementary singular bracket on a positive fixed horizon.

## 1. Isolation, assertion and source preflight

This lane is /Users/matthewrosenzweig/.codex/worktrees/hocf-r010-reductions-blind, branch codex/hocf-r010-reductions-blind, created from the stipulated published R9 commit 29d7ce427ad7a98739b18d07781e71c4598b3579. Exactly 23 permitted files were copied and checked against the supplied SHA-256 manifest before mathematics. Its hash is e3524d5cfc49ec15c006e2acbd9e34b64341eee4b52bb7a9b8252cb710c5dd3d. Other inherited worktree files were ignored.

The first two files read were TASK070 and its input manifest. No R10 candidate proof, root seed, current audit, R11/R12 output, canonical state/history, memory file or previous checking program was accessed. The generic ambient context contained the campaign mission and a memory-summary mention of higher-order fluctuation work; neither was used as evidence. The dispatch explicitly clarified the intended smoothing exponent as N^(-theta/2). Allowed prior reports contain historical status statements and references to other audits. Those references were not opened and their historical verdicts were not adopted as current certifications.

The restricted task dossier controls orientation: non-allowlisted README, orchestration and state files were not read, and no canonical ledger was edited. No commit, push, dependency installation or child agent was used. The report and new diagnostic are sealed before candidate exposure. Root comparison and a separate hostile review remain required.

The primary assertion is the conjunction of every statement in THM030, THM031 and the supplement, retaining their prerequisites. Its logical negation is an admitted tuple or sequence satisfying those prerequisites for which one displayed bound, coefficient, passage, centering identity, sign or equivalence fails. Failure of an assumed prior module is not excluded by this implication.

| Permitted source | Use and retained scope |
|---|---|
| TASKS/ACTIVE/ROUND_001_MODEL.md; MEMORANDA/ROUND_001_ALGEBRA.md, Sections 1 and 3 | Unit Haar, ordered deleted labels, denominator \(N^2\), factor \(1/2\), signs and both responses. |
| THM021; MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md, Sections 2–5 | Heat representation, local coefficient one, \(K\in L^1\), finite signed \(D=\operatorname{div}K\ge-\kappa\,dx\), compensated responses. |
| THM023/024/025 and supplied R5 memoranda | Actual bounded Borel full inverse, base Markov evolution and its strong Haar \(L^2\) heat passage, both-response Volterra formulation and homogeneous backward test. |
| Supplied R5 source/constant and symmetry addenda | A common enlarged \(\kappa\); pair symmetry means exchanging slots, not Haar self-adjointness. |
| THM026; MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md, Sections 3–8 | Fixed-\(N\) noncollision, local Itô calculus, same-noise particle heat passage, stopped energy and density domination. |
| THM028; MEMORANDA/ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md, Sections 5–11 | Explicit conditional premise for the genuine inverse's weak derivatives, finite-particle gradient and true martingale; its weighted constants may depend on \(N\). |
| THM029; MEMORANDA/ROUND_009_HAAR_NOISE_ENERGY.md, Sections 5–10 | Its issued integrated Haar-energy assertion only. Algebraic law identities are rederived. No extra timewise energy estimate is imported. |
| THM030, THM031 and AUDITS/ROUND_010_BLIND_STATEMENT_SUPPLEMENT.md | Statements to reconstruct, not proof inputs. |

No outside literature or novelty claim is used. The new work below is derived from these premises and elementary integration, heat estimates, finite sums and probability inequalities, with their needed forms explained.

## 2. Model, normalization and genuine full inverse

Fix \(d\ge3\), \(0<s\le d-2\), \(N\ge2\), \(T<\infty\), smooth real \(h\), and \(0<\nu\le\nu_*<\infty\). Haar measure on \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) has mass one. Freeze

\[
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad
 \widehat g(0)=0,\quad \widehat g(k)=c_{d,s}|k|^{s-d}\ (k\ne0),\qquad K=-\nabla g.
 \tag{2.1}
\]

The particles start iid Haar independently of their independent Brownian motions and solve

\[
 dX_i=B_i(X)\,dt+\sqrt{2\nu}\,dW_i,\qquad
 B_i=\frac1N\sum_{j\ne i}K(X_i-X_j)=-\nabla_iH_N,\qquad
 H_N=\frac1N\sum_{i<j}g(X_i-X_j).
 \tag{2.2}
\]

Set \(\beta=1/\nu\), \(b_N=\min(\beta,1)\), \(\sigma_N^2=Nb_N\), \(p=s+2\), \(a=s/p\), and \(\theta=1-s/d\). Then

\[
 \nu b_N\le1,\qquad b_N\sqrt\nu\le1,\qquad a-1=-2/p,\qquad 0<\theta<1.
 \tag{2.3}
\]

The actual backward test is

\[
 f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)(4\pi^2\nu|k|^2+d_k)}e^{2\pi i k\cdot x},\qquad
 d_k=4\pi^2c_{d,s}|k|^{s+2-d}.
 \tag{2.4}
\]

Every fixed spatial derivative is uniformly bounded by the rapidly decaying Fourier coefficients of \(h\). Write

\[
 J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)),\qquad
 B^{\rm pair}=K(x-y)\cdot(\nabla_x-\nabla_y).
\]

The genuine \(\Phi\) is the supplied symmetric bounded Borel terminal-zero inverse

\[
 \Phi_t=\int_t^T S_{t,u}J_u\,du+\int_t^T S_{t,u}(R_x+R_y)\Phi_u\,du,
 \qquad \Phi_T=0,
 \tag{2.5}
\]

where \(S\) has base generator \(\nu(\Delta_x+\Delta_y)+B^{\rm pair}/N\), and

\[
 R_xv(x,y)=-\int v(x+w,y)\,D(dw),\qquad
 R_yv(x,y)=-\int v(x,y+w)\,D(dw),\qquad D=\operatorname{div}K.
 \tag{2.6}
\]

Both responses have coefficient one. Below Coulomb \(D=s(d-2-s)g_{s+2}\,dx\); at Coulomb

\[
 D=c_d(\delta_0-dx),\qquad
 c_d=(d-2)|\mathbb S^{d-1}|=4\pi^2c_{d,d-2}.
 \tag{2.7}
\]

A response atom multiplies the same-slot input; it is not an arbitrary pair-diagonal trace. Choose one fixed admissible \(\kappa\ge0\) with \(D\ge-\kappa\,dx\), enlarged as in the source addendum when using the base-pair norm.

Where explicitly used, retain the full THM028 domain assertion and the integrated THM029 estimate as conditional premises:

\[
 \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2\,dt\le C_E N^a.
 \tag{2.8}
\]

Constants not marked \(C_{N,r}\) depend only on the fixed \(d,s,T,\nu_*,h\) and kernel/weight conventions, never on \(N\), selected \(\nu\), or a smoothing parameter unless displayed.

## 3. The two heat constructions and their floors

Let \(p_t\) be the torus heat kernel, with Fourier multiplier \(e^{-4\pi^2t|k|^2}\). Put

\[
 \alpha=(d-s)/2,\qquad A_{d,s}=4^\alpha\pi^{d/2}/\Gamma(s/2),\qquad
 g(z)=A_{d,s}\int_0^\infty t^{\alpha-1}(p_t(z)-1)\,dt.
 \tag{3.1}
\]

For \(k\ne0\), its Fourier coefficient is
\(A_{d,s}\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}=c_{d,s}|k|^{s-d}\).
The substitution \(u=|z|^2/(4t)\) gives

\[
 A_{d,s}\int_0^\infty t^{\alpha-1}(4\pi t)^{-d/2}e^{-|z|^2/(4t)}\,dt=|z|^{-s}.
\]

Nonzero lattice translates at small time and the exponentially decaying torus remainder at large time give a smooth local remainder. Thus \(g\in L^1\), and \(g_*=\inf_{z\ne0}g(z)\) is finite and negative.

First use heat convolution \(g^\epsilon=p_\epsilon*g\), including \(\epsilon=0\) off the diagonal. Since \(\Delta g=-D\le\kappa\,dx\),

\[
 g^{\epsilon+u}\le g^\epsilon+\kappa u\qquad(u>0).
 \tag{3.2}
\]

For \(\epsilon>0\) this follows by integrating the smooth heat equation; for \(\epsilon=0\) take its off-diagonal limit. With \(\eta_N=N^{-1}\sum_i\delta_{x_i}\), positive Fourier coefficients give

\[
 H_N^{\epsilon+u}
 =\frac N2\sum_{k\ne0}\widehat g(k)e^{-4\pi^2(\epsilon+u)|k|^2}
 |\widehat\eta_N(k)|^2-\frac12g^{\epsilon+u}(0).
 \tag{3.3}
\]

The last term is the exact self-diagonal subtraction. The heat kernel or positive Fourier sum gives
\(0\le g^{\epsilon+u}(0)\le g^u(0)\le Cu^{-s/2}\) for \(0<u\le1\). Therefore

\[
 H_N^\epsilon\ge-\tfrac12Cu^{-s/2}-\tfrac12\kappa(N-1)u.
\]

Choosing \(u=N^{-2/p}\) proves, with one fixed \(C_0\),

\[
 \boxed{H_N^\epsilon\ge-C_0N^a\quad\text{for every }\epsilon\ge0.}
 \tag{3.4}
\]

All configurations are admitted when \(\epsilon>0\); the finite \(\epsilon=0\) assertion is on collision-free configurations.

For the sharper floor, truncate the heat integral itself:

\[
 g^{[r]}=A_{d,s}\int_{r^2}^\infty t^{\alpha-1}(p_t-1)\,dt,\qquad
 g=g^{[r]}+\ell^{[r]},\qquad 0<r\le1.
 \tag{3.5}
\]

Then

\[
 \ell^{[r]}\ge-\frac{A_{d,s}}{\alpha}r^{d-s},\quad
 0\le g^{[r]}(0)\le Cr^{-s},\quad
 \widehat g^{[r]}(k)=c_{d,s}|k|^{s-d}
 \frac{\Gamma(\alpha,4\pi^2r^2|k|^2)}{\Gamma(\alpha)}>0.
 \tag{3.6}
\]

The lower bound uses \(p_t\ge0\). The diagonal bound follows by splitting at time one, using \(p_t(0)\le Ct^{-d/2}\) for small times and exponential decay for large times. Heat convolution preserves the lower bound for \(\ell^{[r]}\), and
\((p_\epsilon*g^{[r]})(0)\le g^{[r]}(0)\) by Fourier positivity. Thus

\[
 H_N^\epsilon\ge
 \frac N2\sum_{k\ne0}e^{-4\pi^2\epsilon|k|^2}\widehat g^{[r]}(k)|\widehat\eta_N(k)|^2
 -\frac12(p_\epsilon*g^{[r]})(0)
 -\frac{A_{d,s}}{2\alpha}(N-1)r^{d-s}.
 \tag{3.7}
\]

Choosing \(r=N^{-1/d}\) proves

\[
 \boxed{H_N^\epsilon\ge-CN^{s/d}.}
 \tag{3.8}
\]

The convolution comparison costs \(Nu\); the heat-integral truncation costs \(Nr^{d-s}\). These are distinct cutoffs. At Coulomb their optimized exponents agree, but their definitions do not.

## 4. Actual free energy and singular passage

For a fixed positive cutoff, the smooth density solves

\[
 \partial_tF_N^\epsilon=\operatorname{div}(F_N^\epsilon\nabla H_N^\epsilon)+\nu\Delta F_N^\epsilon,
 \qquad F_N^\epsilon(0)=1.
\]

Positive noise gives a positive smooth density. Periodic integration by parts gives

\[
 \frac d{dt}\left[\nu\operatorname{Ent}(F_N^\epsilon)+\int H_N^\epsilon F_N^\epsilon\right]
 =-\int F_N^\epsilon|\nabla H_N^\epsilon+\nu\nabla\log F_N^\epsilon|^2\le0,
 \tag{4.1}
\]

where \(\operatorname{Ent}(F)=\int F\log F\) relative to probability Haar measure. The initial free energy is zero, since the initial density is one and \(g^\epsilon\) has zero mean. Entropy is nonnegative.

Pass at each fixed \(N,\nu,t\). The stipulated same-noise particle construction gives \(X^\epsilon\to X\) uniformly on the horizon almost surely after integrating over the iid initial law. Each singular path has positive minimum separation. Therefore
\(H_N^\epsilon(X^\epsilon(t))\to H_N(X(t))\) almost surely, by smooth convergence away from the diagonal. The laws converge weakly on the compact configuration torus.

Entropy is lower semicontinuous in this topology, by

\[
 \operatorname{Ent}(F)=\sup_{\varphi\in C}
 \left(\int\varphi\,dF-\log\int e^\varphi\,dX\right).
\]

Jensen after exponential tilting proves the upper bound for each test; truncation of \(\log F\) and continuous approximation proves equality, including value \(+\infty\) for non-densities. Every expression in the supremum is weakly continuous.

Fatou applied to the uniformly shifted nonnegative energies in (3.4), together with this entropy lower semicontinuity, passes the sum in (4.1), not merely its formal separate terms. Hence

\[
 \boxed{\nu\operatorname{Ent}(F_N(t))+\mathbb E H_N(X(t))\le0.}
 \tag{4.2}
\]

No singular Fisher-information identity is invoked. The actual density separately obeys

\[
 0\le F_N(t)\le e^{\kappa(N-1)t}.
 \tag{4.3}
\]

Indeed the smooth divergence is \((2/N)\sum_{i<j}D_{ij}^\epsilon\ge-\kappa(N-1)\); its density bound passes first on continuous tests and then as Borel measure domination. The topology used for (4.2) is weak law convergence plus coupled convergence and lower semicontinuity, not a claimed total-variation heat passage.

Permutation symmetry, common-translation covariance, pathwise uniqueness and the initial law imply exchangeability and common-translation invariance of the actual law. Averaging the one-body translation identity over the translating point gives a Haar one-body marginal. No independence of higher marginals follows.

Exchangeability, (4.3) and \(g\in L^1\) give

\[
 \mathbb EH_N=\frac{N-1}{2}\mathbb E g(X_1-X_2)\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|.
 \tag{4.4}
\]

The second inequality uses \(|g|=g+2g_-\le g+2|g_*|\). For a fixed smooth positive weight \(w_s\) equal to \(|z|^{-s}\) near zero,
\(w_s\le C(1+g-g_*)\). Thus its actual pair moment is bounded uniformly in \(N,\nu,t\); its Haar moment is finite as well. This is not a force-square or concentration bound.

## 5. Marginal entropy and exact bounded-test constants

Write \(E_k=\operatorname{Ent}(F_k)\). All these entropies are finite by (4.3), and \(E_1=0\). Conditional mutual information gives

\[
 E_{j+1}-E_j\ge E_j-E_{j-1}\qquad(2\le j<N).
 \tag{5.1}
\]

Its nonnegative relative entropy is that of the joint conditional law of two labels, given the other \(j-1\), against their conditional product. Expanding its logarithm gives \(E_{j+1}+E_{j-1}-2E_j\); the two \(j\)-marginal entropies agree by exchangeability. Averaging these nondecreasing increments from \(E_1=0\) proves

\[
 \boxed{E_k\le\frac{k-1}{N-1}E_N\qquad(2\le k\le N).}
 \tag{5.2}
\]

The coarse floor gives \(E_N\le C_0N^a/\nu\). Pinsker in the convention here is
\(\|f-1\|_1\le\min(2,\sqrt{2\operatorname{Ent}(f)})\).
To verify the constant, set \(A=\{f\ge1\}\), \(p=\int_Af\), \(q=|A|\). Jensen on \(A,A^c\) bounds entropy below by binary relative entropy. Its second derivative in \(p\) is \(1/[p(1-p)]\ge4\), with value and first derivative zero at \(p=q\), so it is at least \(2(p-q)^2\). Since \(\|f-1\|_1=2(p-q)\), the assertion follows; endpoints follow by limits.

Define

\[
 e_k=\min\left(2,\sqrt{\frac{2C_0(k-1)N^a}{\nu(N-1)}}\right).
 \tag{5.3}
\]

For every bounded measurable \(k\)-test \(Z\),

\[
 |\mathbb EZ(X_1,\ldots,X_k)-\int Z|\le\|Z\|_\infty e_k,\qquad
 e_k\le2\sqrt{\frac{C_0(k-1)}{\nu}}\,N^{-1/p}.
 \tag{5.4}
\]

The last bound uses \(N/(N-1)\le2\) and \((a-1)/2=-1/p\). At \(N=2\) only \(e_2\) is needed.

The sharp floor instead yields

\[
 E_N\le C\beta N^{s/d}=CN\lambda_N,\qquad
 \lambda_N=\beta N^{s/d-1},\qquad E_k\le Ck\lambda_N\quad(k\le N/2),
 \tag{5.5}
\]

with enlarged fixed \(C\). Thus each fixed marginal converges in total variation to the Haar product if \(\lambda_N\to0\). At criticality the bound is merely \(O(k)\); it proves no unweighted total-variation convergence. All sequence claims retain bounded diffusivity.

## 6. Exact field and all four contractions

For a vector kernel \(G_t\), define its own row and centered field:

\[
 A_t(x)=\int G_t(x,y)\,dy,\quad H_t=G_t-A_t,\quad
 v_i[G]=\frac1{N^2}\left[\sum_{j\ne i}H_t(X_i,X_j)-A_t(X_i)\right].
 \tag{6.1}
\]

Equivalently \(v_i=N^{-2}\sum_{j\ne i}G_{ij}-N^{-1}A_i\). For \(G=\nabla_x\Phi\), symmetry and the original statistic

\[
 P_N[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
 -\frac1N\sum_i\int\Phi(X_i,y)\,dy+\frac12\int\Phi
 \tag{6.2}
\]

give \(v_i=\nabla_iP_N[\Phi]\), under the domain premise. The last \(-A_i\) in (6.1) is essential.

Under any exchangeable law with integrable products, expanding before centering gives

\[
 \mathbb E\sum_i|v_i[G]|^2=N^{-3}\left[
 (N-1)\mathbb E|H_{12}|^2
 +(N-1)(N-2)\mathbb EH_{12}\cdot H_{13}
 -2(N-1)\mathbb EH_{12}\cdot A_1
 +\mathbb E|A_1|^2\right].
 \tag{6.3}
\]

There are \(N-1\) equal-label terms and \((N-1)(N-2)\) ordered unequal-label terms inside one square; the outer label sum gives \(N/N^4=N^{-3}\). At \(N=2\) the triple term is absent and no \(X_3\) is defined.

Under independent Haar sampling, the triple and mixed terms vanish, and

\[
 \boxed{\int\sum_i|v_i[G]|^2\,dX
 =\frac{N-1}{N^3}\|G\|_2^2-\frac{N-2}{N^3}\|A\|_2^2.}
 \tag{6.4}
\]

This uses \(\|G-A\|_2^2=\|G\|_2^2-\|A\|_2^2\) for this field's own row. It is not orthogonality between clipped and complementary fields. At \(N=2\) the value is \(\|G\|_2^2/8\); if \(G=A\), it is \(\|A\|_2^2/N^3\), not zero.

Define

\[
 \mathcal Q_N(G)=2\nu Nb_N\int_0^T\mathbb E\sum_i|v_i[G]|^2\,dt,\qquad
 Q_N[\Psi]=\mathcal Q_N(\nabla_x\Psi).
 \tag{6.5}
\]

For the full \(\Phi\), this is the scaled expected bracket of its actual true martingale under THM028. Haar \(H^1\), Jensen, Cauchy–Schwarz and (4.3) make every product in (6.3) integrable at fixed \(N\), including the triple product. This establishes existence, not uniform smallness.

## 7. Radial clipping and its exact constant

For \(L>0\), set

\[
 G^L=G\min(1,L/|G|),\quad G^L=0\text{ at }G=0,\quad
 A^L=\int G^L\,dy,\quad H^L=G^L-A^L,
 \quad G^>=G-G^L,\quad A^>=A-A^L,\quad H^>=H-H^L.
 \tag{7.1}
\]

Then \(|G^L|,|A^L|\le L\), \(|H^L|\le2L\), and \(|G^>|\le|G|\). Every field is recentered by its own row. No new potential-gradient interpretation is asserted.

The adapted field gives

\[
 M_t^L=\sqrt{2\nu}\sum_i\int_0^t v_i[G^L](X(u))\cdot dW_i(u).
 \tag{7.2}
\]

Since \(|v_i[G^L]|\le2L/N\), this is a square-integrable true martingale with bracket \(2\nu\int\sum_i|v_i|^2\). Its scaled expected bracket is \(Q_N^L=\mathcal Q_N(G^L)\). Deterministic Borel fields here are progressively measurable on the noncolliding adapted paths; the row averages are measurable and bounded.

Under Haar, (6.4), \(|G^L|\le|G|\), symmetry of \(\Phi\) and (2.8) give

\[
 Q_{N,\mathrm{Haar}}^L
 \le\frac{2\nu b_N(N-1)}{N^2}\int_0^T\|G_t\|_2^2\,dt
 \le C_Eb_NN^{-2/p}.
 \tag{7.3}
\]

The \(A^L\)-square term in the law comparison is unchanged, because the one-body law is Haar. The other three tests have supremum norms \(4L^2,4L^2,2L^2\). Thus for \(N\ge3\),

\[
 Q_N^L-Q_{N,\mathrm{Haar}}^L
 \le\frac{8\nu b_NTL^2}{N^2}
 [\,2(N-1)e_2+(N-1)(N-2)e_3\,].
 \tag{7.4}
\]

Use \(e_2\le e_3\le2\sqrt{2C_0/\nu}N^{-1/p}\) and
\(2(N-1)+(N-1)(N-2)=N(N-1)\).
At \(N=2\), use the same numerical upper bound for \(e_2\), with no triple test. In both cases,

\[
 \boxed{Q_N^L\le C_Eb_NN^{-2/p}
 +16T\sqrt{2C_0}\,b_N\sqrt\nu\,L^2N^{-1/p}.}
 \tag{7.5}
\]

For \(L_N=N^{1/(4p)}\), this gives

\[
 Q_N^{L_N}\le C_Eb_NN^{-2/p}+C_*N^{-1/(2p)}\to0,\qquad
 C_*=16T\sqrt{2C_0}.
 \tag{7.6}
\]

More generally \(L_N\to\infty\) and \(L_N^2N^{-1/p}\to0\) suffice uniformly. Along a specified positive-noise sequence, it is enough that

\[
 L_N\to\infty,\qquad b_N\sqrt{\nu_N}\,L_N^2N^{-1/p}\to0.
 \tag{7.7}
\]

The first term of (7.5) tends to zero without a threshold condition.

## 8. Exact clipping-tail equivalence and density scope

The map \(G\mapsto(v_i[G])_i\) is linear. The square root of (6.5) is a seminorm in the Hilbert space with measure \(2\nu Nb_N\,dt\,d\mathbb P\) and particle/vector components. Its reverse triangle inequality gives, for \(Q_N=Q_N[\Phi]\) and \(T_N(L)=\mathcal Q_N(G^>)\),

\[
 \boxed{|\sqrt{Q_N}-\sqrt{T_N(L)}|\le\sqrt{Q_N^L}.}
 \tag{8.1}
\]

Consequently, for the explicit threshold or either sufficient condition above,

\[
 Q_N\to0\quad\Longleftrightarrow\quad T_N(L_N)\to0.
 \tag{8.2}
\]

This uses no orthogonality or sign of a covariance. Apply (6.3) to \(H^>,A^>\) with all four coefficients, omitting the triple object at \(N=2\). Full and complementary actual finiteness uses the domain and density premises.

Since \(|G^>|\le|G|\),

\[
 T_{N,\mathrm{Haar}}(L)\le C_Eb_NN^{-2/p},\qquad
 T_N(L)\le e^{\kappa(N-1)T}C_Eb_NN^{-2/p}.
 \tag{8.3}
\]

The exponential factor is the available full-density comparison. It is finite for fixed \(N\), generally useless for a positive fixed horizon as \(N\to\infty\). Equivalence (8.2) does not prove its right side.

## 9. The stated higher-moment route and its limitation

If \(s>2\), choose \(1<r<s/2\). Since \(s\le d-2\), also \(r<d/2\). The conditional domain estimate supplies a finite \(C_{N,r}\), uniform in time and selected noise, such that \(|G_t|\le C_{N,r}w_r\). Put \(u=s/r>2\). The fixed weights obey \(w_r^u\le C_{s,r}w_s\). Since
\(|G^>|\le|G|\mathbf1_{\{|G|>L\}}\), the actual and Haar pair moments imply

\[
 \mathbb E_{\rm actual}|G^>|^2,\quad \int|G^>|^2
 \le C_{s,r}C_{N,r}^{s/r}L^{2-s/r}.
 \tag{9.1}
\]

Write \(v_i[G^>]=N^{-1}(Z_i-A_i^>)\), where \(Z_i=N^{-1}\sum_{j\ne i}G^>_{ij}\). Jensen gives

\[
 \mathbb E|Z_i|^2\le\frac{N-1}{N}\mathbb E|G^>_{12}|^2,\qquad
 \mathbb E|A_i^>|^2=\|A^>\|_2^2\le\|G^>\|_2^2.
\]

Using \(|Z-A|^2\le2|Z|^2+2|A|^2\) in the scaled bracket proves

\[
 \boxed{T_N(L)\le8\nu b_NT C_{s,r}C_{N,r}^{s/r}L^{2-s/r}.}
 \tag{9.2}
\]

For \(L_N=N^{1/(4p)}\), the sufficient additional condition is

\[
 \nu_Nb_NC_{N,r}^{s/r}N^{-(s/r-2)/(4p)}\to0.
 \tag{9.3}
\]

Finiteness of \(C_{N,r}\) for each \(N\) does not establish this growth condition. If \(0<s\le2\), no \(r>1\) has \(s/r>2\). That blocks this particular larger-than-quadratic-moment argument, not the tail statement itself.

## 10. Actual Fourier control and total-force occupation

Apply (3.7) at \(\epsilon=0\), \(r=N^{-1/d}\), take actual expectation and use \(\mathbb EH_N\le0\). Then

\[
 \sum_{k\ne0}\widehat g^{[r]}(k)\mathbb E|\widehat\eta_N(t,k)|^2\le CN^{-\theta}.
 \tag{10.1}
\]

For \(0<|k|\le r^{-1}\), the incomplete-gamma ratio in (3.6) is at least the positive constant \(\Gamma(\alpha,4\pi^2)/\Gamma(\alpha)\). Hence
\(\mathbb E|\widehat\eta_N(t,k)|^2\le CN^{-\theta}|k|^{d-s}\) in this range. For larger \(|k|\), that right side is at least one after increasing \(C\), whereas \(|\widehat\eta_N(k)|\le1\) deterministically. Thus

\[
 \boxed{\mathbb E|\widehat\eta_N(t,k)|^2
 \le\min(1,CN^{-\theta}|k|^{d-s})\quad(k\ne0).}
 \tag{10.2}
\]

The positive heat-integral truncation is used only up to frequency \(N^{1/d}\); the deterministic estimate handles the remaining modes. No exponentially small multiplier is divided out at unrestricted frequencies.

At positive heat cutoff, smooth Itô calculus for the full energy gives

\[
 \mathbb EH_N^\epsilon(X^\epsilon(t))
 +\mathbb E\int_0^t\sum_i|B_i^\epsilon|^2\,du
 =\nu\mathbb E\int_0^t\Delta_{Nd}H_N^\epsilon\,du,\qquad
 \Delta_{Nd}H_N^\epsilon=\frac2N\sum_{i<j}\Delta g^\epsilon_{ij}
 \le\kappa(N-1).
 \tag{10.3}
\]

The initial expectation is zero. The sharp floor gives
\(\mathbb E\int_0^T\sum_i|B_i^\epsilon|^2\le CN^{s/d}+\nu\kappa(N-1)T\).
Same-noise convergence and the singular path's positive separation give convergence of the forces along those paths; Fatou passes their nonnegative squared time integral. Exchangeability yields the more explicit finite-\(N\) factor

\[
 \boxed{\mathbb E\int_0^T|B_i(X(t))|^2\,dt
 \le CN^{-\theta}+\nu\kappa\frac{N-1}{N}T
 \le CN^{-\theta}+\nu\kappa T.}
 \tag{10.4}
\]

The stopped singular energy identity in the supplied R6 module gives a second route once the sharper floor is available. Neither argument expands a nonnegative full force square and discards its signed cross terms.

Choose Euclidean lifts for each labelled path. Subtracting its own Brownian displacement leaves \(\int_0^tB_i\,du\). Therefore

\[
 \mathbb E\sup_{t\le T}\operatorname{dist}_{\mathbb T^d}
 (X_i(t),X_i(0)+\sqrt{2\nu}W_i(t))^2
 \le T\mathbb E\int_0^T|B_i|^2\,dt.
 \tag{10.5}
\]

The vector \(L^2\) martingale maximal inequality gives
\(\mathbb E\sup_{t\le T}|W_i(t)|^2\le4dT\). Its needed form follows from the stopping-time maximal estimate and integration with Cauchy–Schwarz. Combining with \(|u+v|^2\le2|u|^2+2|v|^2\), both (10.5) and

\[
 \mathbb E\sup_{t\le T}\operatorname{dist}_{\mathbb T^d}(X_i(t),X_i(0))^2
\]

are at most \(C_T(N^{-\theta}+\nu)\). If \(\beta_NN^{-\theta}\to\lambda\in(0,\infty)\), then \(\nu_N=O(N^{-\theta})\), proving the stated critical \(O(N^{-\theta})\) rate. This is a labelled-path estimate, not an equilibrium assertion. A bound on the full total-force square does not by this proof bound every pair-force square: the middle total force can cancel in a symmetric three-particle cluster while its individual pair forces are large.

## 11. Uniform Haar \(L^1\), common translations and smooth projection

This section concerns the full inverse (2.5), including both responses.

The smooth auxiliary pair drift has divergence \(2D^\epsilon(x-y)/N\ge-2\kappa/N\). Its random-flow Jacobian, equivalently its forward density from Haar, gives

\[
 \|S_{t,u}^\epsilon v\|_1\le e^{2\kappa(u-t)/N}\|v\|_1.
 \tag{11.1}
\]

For bounded \(v\), the supplied strong Haar \(L^2\) heat passage implies \(L^1\) convergence on the mass-one pair space. Thus (11.1) holds for singular \(S\). Completion extends it to \(L^1\), and positivity and monotone truncation identify the extension with Markov expectation for nonnegative integrable inputs. This justifies its use for the possibly unbounded source.

The cancellation in the gradient difference gives \(\sup_t\|J_t\|_1\le C_h\): the local bound is \(C|x-y|^{-s}\), with \(s<d\). Each response has \(L^1\) norm at most \(\|D\|_{\rm TV}\), by translation invariance and Tonelli, and their sum has norm at most \(C_R=2\|D\|_{\rm TV}\). Iterating (2.5) on ordered time simplices gives

\[
 \sup_{t\le T}\|\Phi_t\|_1\le C_hT e^{(\kappa+C_R)T}.
 \tag{11.2}
\]

Indeed \(2\kappa/N\le\kappa\), and on each simplex the base-evolution interval lengths add to at most \(T\). The \(m\) response factors give the usual \((C_RT)^m/m!\). Equivalently apply the scalar integral inequality for \(\|\Phi_t\|_1\) after exponential weighting. Consistency with the actual bounded Borel inverse follows from the same Volterra series and its uniqueness; no substitute pair kernel is constructed.

Let \(\mathcal D_j=\partial_{x_j}+\partial_{y_j}\). The homogeneous pair process and both convolution responses commute with common translation, and \(\mathcal D^\alpha J[h]\) is the source for \(\partial^\alpha h\). Difference quotients in \(h\), convergence in its fixed smooth norms, and (11.2) show that

\[
 \mathcal D^\alpha\Phi[h]=\Phi[\partial^\alpha h]\quad\text{as Haar weak derivatives},
 \qquad \sup_t\|\mathcal D^\alpha\Phi_t\|_1\le C_\alpha
 \tag{11.3}
\]

for every fixed multi-index. These are common-translation derivatives, not uniform estimates for all relative derivatives.

Put \(q_t(x)=\int\Phi_t(x,y)\,dy\). Testing against smooth one-body functions and integrating the common-translation derivative gives

\[
 \partial_x^\alpha q_t=\int\mathcal D^\alpha\Phi_t(x,y)\,dy
 \quad\text{weakly},\qquad
 \|\partial^\alpha q_t\|_1\le C_\alpha.
 \tag{11.4}
\]

For explicit smoothness, integrate by parts in the Fourier coefficient using \(1-\Delta_x\). Bounds through order \(2j\) give
\(|\widehat q_t(k)|\le C_j(1+|k|^2)^{-j}\).
Choose \(2j>m+d\); the derivative Fourier series through order \(m\) then converges absolutely and uniformly. Thus

\[
 \boxed{\sup_{N,\nu,t}\|q_t\|_{C^m}\le C_m\quad\text{for every fixed }m.}
 \tag{11.5}
\]

Under the domain premise these are the existing background contraction and its derivatives, not different representatives.

## 12. Exact scalar and actual centering

Let \((\tau_z\Phi)(x,y)=\Phi(x+z,y+z)\). Averaging the translated source over \(z\) gives zero, since the integral of each translated gradient of \(f\) is zero. The base evolution and both responses commute with this average, so every term of the bounded Borel Volterra series has zero average. At each fixed \(N\), boundedness justifies the interchanges. Therefore

\[
 \int_{\mathbb T^d}\tau_z\Phi_t(x,y)\,dz=0
 \tag{12.1}
\]

off the diagonal and in Haar \(L^1\). In particular \(\int\Phi_t=\int q_t=0\).
The actual law is common-translation invariant, so (12.1) gives
\(\mathbb E\Phi_t(X_1,X_2)=0\); the Haar one-body law gives \(\mathbb E q_t(X_1)=0\).
The statistic's exact coefficients now yield

\[
 \boxed{\mathbb EP_N[\Phi_t]
 =\frac{N-1}{2N}\mathbb E\Phi_t(X_1,X_2)-\mathbb E q_t(X_1)+\frac12\int\Phi_t=0.}
 \tag{12.2}
\]

The stronger translation identity (12.1), not just the scalar integral \(\int\Phi=0\), is needed to kill the actual pair mean. No concentration, variance or path-supremum conclusion follows.

## 13. Smoothing, the missing-self term and the specified rate

For \(0<\delta\le1\), define

\[
 \Psi_\delta=e^{\delta\Delta_x}e^{\delta\Delta_y}\Phi,\qquad
 G_\delta=\nabla_x\Psi_\delta.
 \tag{13.1}
\]

This is spatial smoothing of the genuine full inverse, not interaction regularization or a new inverse. It is symmetric and spatially smooth. Its \(y\)-Fourier coefficient is

\[
 \widehat G_\delta^{\,y}(x,k)
 =e^{-4\pi^2\delta|k|^2}\nabla_x e^{\delta\Delta_x}
 \left(\int\Phi(x,y)e^{-2\pi i k\cdot y}\,dy\right).
\]

The bracketed function has \(L^1_x\) norm at most \(\|\Phi\|_1\), while the periodized Gaussian derivative satisfies
\(\|\nabla p_\delta\|_\infty\le C\delta^{-(d+1)/2}\). Equation (11.2) gives

\[
 |\widehat G_\delta^{\,y}(x,k)|
 \le C\delta^{-(d+1)/2}e^{-4\pi^2\delta|k|^2}
 \tag{13.2}
\]

uniformly in \(x,t,N,\nu\). Let \(Z_i=\int G_\delta(X_i,y)\,[\eta_N(dy)-dy]\).
The deleted-pair gradient is precisely

\[
 \boxed{\nabla_iP_N[\Psi_\delta]
 =\frac1N\left[Z_i-\frac1NG_\delta(X_i,X_i)\right].}
 \tag{13.3}
\]

Only the smooth kernel is evaluated on a diagonal; no singular \(G(X_i,X_i)\) is introduced.

The zero Fourier coefficient drops out of \(Z_i\). Minkowski in \(L^2(\mathbb P)\), the uniform coefficient bound and (10.2) imply

\[
 \begin{split}
 (\mathbb E|Z_i|^2)^{1/2}
 &\le C\delta^{-(d+1)/2}N^{-\theta/2}
 \sum_{k\ne0}e^{-4\pi^2\delta|k|^2}|k|^{(d-s)/2}\\
 &\le CN^{-\theta/2}\delta^{-(5d-s+2)/4}.
 \end{split}
 \tag{13.4}
\]

No independence between \(X_i\) and \(\eta_N\) is required: the random coefficient evaluated at \(X_i\) is bounded by a deterministic supremum. The lattice sum is controlled by unit shells and the rescaled integral
\(\int_0^\infty u^{d-1+(d-s)/2}e^{-c\delta u^2}\,du\).
Similarly, summing (13.2) over all modes gives

\[
 \sup_x|G_\delta(x,x)|\le C\delta^{-(2d+1)/2}.
 \tag{13.5}
\]

With \(r_*=(5d-s+2)/2\), (13.3), exchangeability and the square inequality give

\[
 \boxed{Q_N[\Psi_\delta]\le C\nu b_N
 [N^{-\theta}\delta^{-r_*}+N^{-2}\delta^{-(2d+1)}]
 \le CN^{-\theta}\delta^{-r_*}.}
 \tag{13.6}
\]

For the second inequality use \(r_*-(2d+1)=(d-s)/2>0\), \(0<\delta\le1\),
\(0<\theta<1\), and \(\nu b_N\le1\). Every particle factor here follows from the original denominator \(N^2\) and scaling \(Nb_N\).

Set

\[
 \gamma=\frac{d-s}{d(5d-s+2)}=\frac{\theta}{2r_*},\qquad
 \delta_N=N^{-\gamma}.
\]

Then

\[
 \boxed{Q_N[\Psi_{\delta_N}]\le CN^{-\theta/2}\longrightarrow0.}
 \tag{13.7}
\]

The exponent is \(-\theta/2\), as clarified in the dispatch, not a factor one-half in front of \(N^{-\theta}\).

## 14. Both smoothing-tail equivalences and order of limits

Let \(R_{N,\delta}=\Phi_N-\Psi_{N,\delta}\). The same bracket seminorm gives

\[
 |\sqrt{Q_N[\Phi_N]}-\sqrt{Q_N[R_{N,\delta}]}|
 \le\sqrt{Q_N[\Psi_{N,\delta}]}.
 \tag{14.1}
\]

For every admitted positive-noise sequence, (13.7) implies

\[
 Q_N[\Phi_N]\to0
 \quad\Longleftrightarrow\quad Q_N[R_{N,\delta_N}]\to0.
 \tag{14.2}
\]

For each fixed \(\delta>0\), (13.6) makes the right side of (14.1) tend to zero as \(N\to\infty\). Consequently

\[
 Q_N[\Phi_N]\to0
 \quad\Longleftrightarrow\quad
 \lim_{\delta\downarrow0}\limsup_{N\to\infty}Q_N[R_{N,\delta}]=0.
 \tag{14.3}
\]

For the forward direction the inner limsup vanishes for every fixed \(\delta\). For the reverse direction take limsups of square roots in (14.1), then send \(\delta\downarrow0\). The reasoning remains valid for extended nonnegative limsups and makes no interchange of limits.

For each residual use its own \(G=\nabla_xR_{N,\delta}\), \(A=\int G\,dy\), \(H=G-A\) in (6.3), retaining every contraction and coefficient, with no triple object at \(N=2\). The same instruction applies to the full field, clipped field and complementary field.

At a fixed \(N\), the conditional domain premise yields
\(\Phi\in L^2([0,T];H^1(\mathrm{Haar}^2))\).
Heat convolution is an approximate identity in this space: truncate the space-time \(H^1\) Fourier series, use convergence on the finite part, and bound the tail by Parseval and heat multipliers at most one. Thus

\[
 \int_0^T\|\nabla_{x,y}(\Phi-\Psi_\delta)\|_2^2\,dt\to0
 \qquad(\delta\downarrow0,\ N\text{ fixed}).
 \tag{14.4}
\]

Jensen controls rows, while (6.4) and (4.3) transfer this to
\(Q_N[R_{N,\delta}]\to0\) at this fixed \(N\), at cost \(e^{\kappa(N-1)T}\).
Neither this convergence nor that density factor permits reversing the limits in (14.3). The remaining line is precisely a uniform estimate for the right side of (14.2) or (14.3) at positive fixed \(T\).

## 15. Initial triple covariance: actual-law passage and sign

Let \(N\ge3\). Let \(H_t(x,y)\) be a real vector kernel, smooth in space and \(C^1\) in time near zero with the corresponding locally uniform smooth bounds, and suppose
\(\int H_t(x,y)\,dy=0\) for every \(x\) and nearby \(t\).
It is an arbitrary smooth probe, not presumed to be the singular corrector field.
Put \(Z_t(X)=H_t(X_1,X_2)\cdot H_t(X_1,X_3)\).
At iid Haar time zero, \(\int Z_0=0\) and \(\int\partial_tZ_0=0\) by row centering; also \(\int\Delta_{Nd}Z_0=0\).

To justify differentiating the actual singular law, use the smooth probe's stopped Itô formula. Its drift \(B\cdot\nabla Z_t\) is Haar \(L^1\), since \(K\in L^1\). Density domination, localization and absolute integrability pass the expectation identity to the actual paths. As time decreases to zero the laws converge weakly to Haar, with a common finite density bound. Their integrals against any fixed \(L^1\) function converge: approximate it in \(L^1\) by continuous functions, use weak convergence on the approximants, and the common density bound on the errors. The time-dependent generator integrand converges in Haar \(L^1\) by the probe's stated regularity. Hence

\[
 \left.\frac d{dt}\mathbb EZ_t(X(t))\right|_{0+}
 =\int(\partial_tZ_0+\nu\Delta Z_0+B\cdot\nabla Z_0)\,dX.
 \tag{15.1}
\]

Distributional integration by parts against this smooth probe and the finite measure \(D\) is legitimate. Since
\(\operatorname{div}B=(2/N)\sum_{i<j}D(x_i-x_j)\), (15.1) equals

\[
 -\frac2N\sum_{i<j}\int Z_0(X)\,D(x_i-x_j)\,dX.
 \tag{15.2}
\]

Pairs involving an unused label integrate to zero because \(D\) has total mass zero. Pairs \((1,2)\) and \((1,3)\) vanish by integrating the other row-centered variable. Only \((2,3)\) remains. For fixed \(x\), Fourier convolution gives

\[
 \int H_0(x,y)\cdot H_0(x,z)\,D(y-z)\,dy\,dz
 =\sum_{k\ne0}d_k|\widehat H_0^{\,y}(x,k)|^2.
\]

The sum is absolutely convergent by smoothness and boundedness of \(d_k\) on the stated range. Therefore

\[
 \boxed{\left.\frac d{dt}\mathbb E[H_t(X_1,X_2)\cdot H_t(X_1,X_3)]\right|_{0+}
 =-\frac2N\int_x\sum_{k\ne0}d_k|\widehat H_0^{\,y}(x,k)|^2\,dx\le0.}
 \tag{15.3}
\]

At Coulomb \(d_k=c_d\) for every \(k\ne0\), and the zero coefficient of \(H_0\) vanishes. Parseval yields

\[
 \left.\frac d{dt}\mathbb E[H_t(X_1,X_2)\cdot H_t(X_1,X_3)]\right|_{0+}
 =-\frac{2c_d}{N}\|H_0\|_2^2.
 \tag{15.4}
\]

This is the initial right derivative only. There is no later-time sign, uniform singular Taylor remainder or extension of the derivative formula to an arbitrary nonsmooth corrector probe. The triple observable is not defined at \(N=2\).

## 16. Conditional shrinking window and endpoints

Use only the integrated Haar estimate (2.8). For \(0\le\tau\le T\), nonnegativity of the integrand and density domination give

\[
 \boxed{Q_N^{[0,\tau]}[\Phi]\le
 C_Eb_N e^{\kappa(N-1)\tau}N^{a-1}.}
 \tag{16.1}
\]

The Haar integral over the shorter interval is merely bounded by that over \([0,T]\); no new proportional-to-\(\tau\) energy estimate is claimed.

Choose a positive admissible \(\kappa\), enlarging a zero lower-bound constant if needed, and \(0<\zeta<1-a\). Set

\[
 \tau_N=\min\left(T,\frac{\zeta\log N}{\kappa(N-1)}\right).
\]

Then the exponential is at most \(N^\zeta\), so

\[
 \boxed{Q_N^{[0,\tau_N]}[\Phi]\le C_Eb_NN^{-(1-a-\zeta)}\longrightarrow0.}
 \tag{16.2}
\]

This excludes no positive-fixed-horizon tail, and assumes no timewise Haar gradient estimate.

At \(\nu=0\), every noise functional and martingale discussed here is defined separately as zero. The stipulated deterministic gradient dynamics satisfy the localized energy identity
\(H_N(X(t))+\int_0^t\sum_i|B_i|^2=H_N(X(0))\).
Finite-mean Haar preparation gives nonpositive expected energy and the floor-based deterministic occupation bound. Entropy division is not available at zero noise, and no finite \(\beta\) is identified with \(1/0\).
At \(T=0\), all integrated quantities vanish and the terminal inverse is zero.
For constant \(h\), \(J=0\) and uniqueness gives \(\Phi=0\).

The three temperature conditions stay distinct: the old first-order floor condition is
\(\beta_NN^{2s/d-1}\to0\), full microscopic subcriticality is
\(\lambda_N=\beta_NN^{s/d-1}\to0\), and criticality is
\(\lambda_N\to\lambda\in(0,\infty)\).
No logarithmic normalization is obtained by setting \(s=0\). No hierarchy closure, evolved residual estimate, critical limiting law or full fluctuation theorem is proved.

## 17. Falsification routes, exact checks and complete coverage

The analytic route was challenged separately by finite-label algebra, direct Laurent-polynomial generator calculation, cutoff-power matching, degenerate tests and adversarial inspection of the limit order. These are separate mathematical routes within one context, not independent-agent certification.

The newly written standard-library program round010_two_reductions_diagnostics.py passed **4,955 exact rational checks** under Python 3.9.6. It exhaustively evaluates finite-grid fields under Haar and an explicitly correlated exchangeable law with Haar one-body marginals, for \(N=2,3,4,5\). Clipping uses vectors on a rational unit direction, so radial clipping and separate row means remain exact. It checks every coefficient in (6.3), the Haar identity, the missing-self term, linear decomposition and norm polarization. A separate Laurent-polynomial computation derives initial covariance from the particle generator and compares it with the divergence/BBGKY expression, including the Coulomb factor. Further checks cover exponents, the constant-16 count, noise weights and moment admissibility. There is no simulation or fitted rate.

The adversarial checks retained these possible failure mechanisms:

- Confusing integral truncation with convolution loses the sharper floor; Sections 3 and 10 keep their different remainders and multipliers.
- Removing the deleted-label remainder, a response slot or mixed contraction changes exact coefficients; Sections 2, 6, 7 and 13 retain them.
- The clipped law error is weighted by \(b_N\sqrt\nu\); it is not critical total-variation convergence.
- Actual mean zero uses common-translation averaging of the full inverse and gives no concentration.
- Only a smooth diagonal is evaluated. No singular trace is imposed.
- The initial covariance sign is proved for smooth probes; no singular Taylor estimate or later sign is inferred.
- Fixed-\(N\) approximation with exponential density cost is not used to interchange limits.
- The moment estimate retains \(C_{N,r}\), and the short-window bound retains only integrated Haar energy.

| Complete frozen scope | Reconstruction | Status of this implication |
|---|---|---|
| THM030 smooth/singular coarse floor | (3.2)–(3.4) | Proved from supplied kernel premises. |
| THM030 free energy, pair energy and \(w_s\) moment | Section 4 | Proved through actual smooth-to-singular passage. |
| THM030 marginal entropy and both bounded-test estimates | (5.1)–(5.4) | Proved with exact factors and constants. |
| THM030 clipped true martingale, bound and thresholds | Section 7 | Conditional on full-domain/integrated-Haar premises where used. |
| THM030 exact tail equivalence, contractions and density scope | Sections 6 and 8 | Conditional implication proved; actual tail remains open. |
| THM030 moment estimate and low-\(s\) limitation | Section 9 | Conditional estimate proved; growth condition remains unproved. |
| THM031 sharp floor, Fourier control, subcritical marginals | (3.5)–(3.8), (5.5), (10.1)–(10.2) | Proved in the stated law/noise range. |
| THM031 total force and labelled paths, including critical rate | (10.3)–(10.5) | Proved; no pair-force-square extraction. |
| THM031 full inverse \(L^1\), translation derivatives and \(q_t\) | Section 11 | Proved from full-pair modules, both responses included. |
| THM031 scalar and actual mean centering | Section 12 | Proved; no concentration assertion. |
| THM031 smoothing coefficients, diagonal term and specified rate | Section 13 | Proved with the new estimate only for the smooth field. |
| THM031 both tail equivalences and fixed-\(N\) approximation | Section 14 and (6.3) | Conditional on complete unsmoothed domain premise. |
| THM031 initial triple derivative and Coulomb endpoint | Section 15 | Proved for the stipulated smooth probes, \(N\ge3\). |
| THM031 short window, zero noise, constant \(h\), \(T=0\) | Section 16 | Proved in stated scopes; window uses only integrated Haar energy. |

Every subordinate assertion in the supplement is included. Shared-core agreement has not been substituted for coverage of either entire card.

## 18. Handoff and remaining gates

This complete conditional reconstruction is ready for root comparison with the sealed candidates and a separate hostile review. The prior modules' issued assumptions have not been upgraded. On a positive fixed horizon the next unproved line is actual smallness of the complementary singular-noise functional in (8.2), equivalently the smoothing residual in (14.2) or (14.3). The available Haar tail, finite-\(N\) density factor, initial sign and finite derivative constants do not establish it.

The output directory contains this report, a README, the new diagnostic and JSON result, the exact 23-file input seal and verification record, a provenance record, an output seal and a timestamped archive with a separate hash seal. Inputs are rechecked before sealing. The output manifest is non-self-referential. The archive contains the exact permitted input bytes and the sealed reconstruction payload; its hash is stored separately. Sealed outputs are not changed after issuance.

No TeX source was created, and the handoff message contains no mathematical LaTeX. The requested deliverables are Markdown and exact diagnostics, so no TeX build is represented as having run. No canonical file or prior report was changed. Separate comparison and hostile-audit gates remain required.
