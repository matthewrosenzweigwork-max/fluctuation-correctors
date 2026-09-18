# TASK065 — hostile review of the frozen THM031 smoothing and tail assertion

Issued 2026-09-18 UTC. **CONDITIONAL PASS.** No unsupported line was found in the asserted conclusions of Sections 2–9 of the sealed TASK061 proof, with exactly the source premises and exclusions stated in the frozen card. The actual full singular-noise limit remains **OPEN**, at the residual estimate (7.4). That estimate is not proved by this review, and the candidate is not repaired or replaced.

This is a fresh hostile review of the complete frozen statement and proof, with independent reconstruction and newly written exact diagnostics. It is not a statement-only blind reconstruction, a construction of the missing tail estimate, or certification of a prior domain theorem. Earlier source statuses are not upgraded. In particular the full THM028 domain premise and the Section 9 integrated THM029 energy premise remain conditional irrespective of any current root status.

The isolated worktree is "/Users/matthewrosenzweig/.codex/worktrees/hocf-r010-smoothing-hostile", on "codex/hocf-r010-smoothing-hostile", created from commit "29d7ce427ad7a98739b18d07781e71c4598b3579". Exactly the 22 files in "AUDITS/ROUND_010_SMOOTHING_HOSTILE_INPUT_SHA256SUMS.txt" were copied from root and checked before mathematics was read. They were checked again by the independent diagnostic and at sealing. No canonical/root output was edited; no commit, push, installation, or child was used. The exposure record and reproduction instructions are supplied alongside this report.

The ambient app/global/user preamble, including a high-level memory summary, was available before the task. No memory file was opened, searched, or used as mathematical evidence. No non-allowlisted current state, history, audit, R10 output, checker, or constructor diagnostic was consulted. The permitted sealed proof contains its own description of diagnostics; those reported results were not adopted or rerun.

## 1. Assertion, logical negation, and source boundary

Write **M** for the sealed "MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md" and **C** for "THEOREMS/THM-031_ACTUAL_FOURIER_SMOOTHING_AND_TAIL.md". All references below identify their frozen line numbers or equation numbers. The complete conjunction under review is C:5–29, with its proof scope M:76–515. It includes all claimed limits, conditional qualifications, exact coefficients, centering, law classes, and endpoints; it does not include the explicitly open estimate as a proved conclusion.

Fix integer \(d\ge3\), \(0<s\le d-2\), \(T<\infty\), a finite diffusivity upper bound, and smooth real terminal \(h\). Uniformity means constants depend on these fixed data and the frozen kernel/cutoffs or specified seminorms of \(h\), but not on \(N\ge2\), \(0<\nu\le\nu_*\), or deterministic \(t\in[0,T]\). Dependence on a fixed smoothing parameter is displayed before a prescribed sequence of smoothings is chosen. The actual initial configuration is iid unit Haar, independent of the Brownian motions. The whole-space, logarithmic, inhomogeneous, non-gradient, arbitrary-exchangeable-preparation, and unbounded-diffusivity cases are outside the assertion.

The exact negation is either an admitted instance violating an exact identity, sign, domain/passage implication, or endpoint, or fixed admitted data for which no finite allowed constant works uniformly over \(N,\nu,t\), or an admitted sequence violating an asserted limit. For conditional parts the premises must hold: failure of a prior premise does not by itself falsify a conditional implication. This formulation retains the uniform quantifier; choosing one finite tuple and then enlarging its constant is not its negation.

The source preflight uses only the following permitted evidence. Reading a premise here does not certify its full construction.

| Source and exact location | Input actually used | Boundary retained |
|---|---|---|
| Frozen R1 model; R1 algebra (1.2)–(1.4), (3.8), (5.1)–(5.2) | Unit Haar mass, characters \(e^{2\pi i k\cdot x}\), ordered distinct labels, denominator \(N^2\), factor \(1/2\), independent noise \(\sqrt{2\nu}\) | New noise/label coefficients are reconstructed below. Smooth algebra alone does not authorize a singular insertion. |
| THM021; R4 response memorandum:69–194, 198–234 | Coefficient-one heat representation, smooth local remainder, \(K\in L^1\), finite \(D=\operatorname{div}K\), its lower bound and compensation | No logarithmic substitution; Coulomb atom and constant compensation both retained. |
| THM023; R5 base pair memorandum:402–563, especially (9.3) | Singular pair evolution and its Borel measure domination | The \(L^1\) bound follows from the actual measure inequality, not an \(L^2\) operator bound. |
| THM024/025; R5 conditional inverse and full-pair interface memoranda; the two allowed R5 addenda | Same bounded Borel Volterra inverse with both responses; exact homogeneous Fourier test; common divergence constant | Pair exchange is not Haar self-adjointness. The conditional abstract module is not a new unconditional particle theorem. |
| THM026; R6 particle memorandum:145–227, 291–342, 425–544 | Actual particle paths, fixed-\(N\) heat passage and density domination; exact total-force energy identity and its integrable expectation passage | Density costs may grow exponentially in \(N\). No individual pair-force square is extracted. |
| THM028; R8 domain memorandum:399–407, 473–552, 723–759 | Full stipulated off-diagonal regularity, global weak derivatives, background contractions, finite-\(N\) actual Itô/bracket and integrability premise | Remains conditional. Its \(N\)-dependent bounds are used only in fixed-\(N\) identification and limiting steps. |
| THM029; allowed R9 energy reconstruction (4.4), (5.3)–(5.4) | Only the integrated Haar energy/reference-noise implication, for Section 9 | Remains conditional. No additional timewise estimate is imported. |

The full source paths are uniquely specified in the 22-file input manifest. For the pair propagator and particle density, choose one fixed positive \(\kappa\) at least as large as the R4 lower-divergence constant and the R5 smooth-remainder constant, as specified in the permitted R5 addendum. Increasing it preserves every bound and avoids division by zero in the shrinking-window formula. This is the existing source convention, not a repair.

## 2. Complete per-claim disposition

“Pass” means the new implication is verified within the exact source boundary above. It is not a verdict on the entire prerequisite construction. Local labels C01–C16 belong only to this review and are not newly assigned canonical theorem/audit identifiers.

| Claim | Frozen proof location | Verdict | First unsupported line |
|---|---|---|---|
| C01 Actual energy and free energy after heat passage | M:86–137, (2.3)–(2.7); C:7 | PASS from particle/kernel premises | None in the asserted implication. |
| C02 Uniform actual pair-energy moment | M:139–148, (2.8); C:7 | PASS | None. |
| C03 Positive heat-integral floor and exact self subtraction | M:154–196, (3.1)–(3.5); C:7 | PASS; independent deterministic reconstruction | None. |
| C04 All-frequency actual empirical bound | M:198–223, (3.6)–(3.7); C:9 | PASS | None; high modes use the trivial bound. |
| C05 Full configuration entropy and fixed marginals | M:225–235, (3.8); C:11 | PASS for positive diffusivity | None; block-count constant is uniform. |
| C06 Total-force occupation and labelled paths | M:237–266, (4.1)–(4.3); C:11 | PASS from the exact energy premise | None; only the complete total force is controlled. |
| C07 Uniform Haar \(L^1\) norm of the true full inverse | M:268–300, (5.1)–(5.4); C:13 | PASS from the full pair premises | None; both responses remain. |
| C08 Common-translation derivatives, smooth projection, exact actual mean | M:302–311, (5.5); C:13 | PASS | None; orbit averaging proves the actual mean. |
| C09 Heat/Fourier smoothing bounds and missing self | M:315–359, (6.1)–(6.5); C:15,19 | PASS | None; the diagonal is evaluated only after smoothing. |
| C10 Actual smoothed bracket and prescribed vanishing scale | M:361–391, (6.6)–(6.8); C:15–17 | PASS | None; physical factors independently recovered. |
| C11 Exact four-term actual-law expansion | M:395–416, (7.1)–(7.2); C:19 | PASS conditional on the full domain premise | None; the \(N=2\) triple term is absent. |
| C12 Residual and iterated-limit equivalences | M:418–438, (7.3)–(7.4); C:19 | PASS conditional on the full domain premise | None in the equivalence itself. |
| C13 Fixed-\(N\) approximation and refusal to interchange limits | M:437–440; C:19 | PASS conditional on the full domain premise | Uniform residual estimate (7.4) remains unproved, as stated. |
| C14 Initial BBGKY derivative and Coulomb sign | M:444–496, (8.1)–(8.4); C:21–27 | PASS from particle/kernel premises, for the stated smooth probes | None; no later-time sign or singular Taylor remainder follows. |
| C15 Shrinking initial-window bound | M:500–515, (9.1)–(9.2); C:27 | CONDITIONAL PASS on integrated THM029 energy and the domain premise | None in this implication; imported energy remains conditional. |
| C16 Full singular bracket, critical law, hierarchy closure | M:427–440, 555–560; C:19,29 | OPEN / NOT CLAIMED PROVED | M:429–431, estimate (7.4), is the first unproved assertion needed for the full bracket target. |

No revision is required for this bounded conjunction. The remaining sections supply the analytic reconstruction behind these dispositions rather than treating diagnostic results as proofs.

## 3. Energy, singular passage, Fourier floor, and entropy

### 3.1 Actual free energy and the order of the limits

For \(H_N=N^{-1}\sum_{i<j}g(x_i-x_j)\), evenness gives \(B_i=-\nabla_iH_N\). At a fixed positive heat cutoff the actual density, initially one, solves

\[
 \partial_tF^\epsilon=\operatorname{div}
       (F^\epsilon\nabla H_N^\epsilon+\nu\nabla F^\epsilon).
\]

Smooth coefficients, positive diffusivity and the compact configuration torus justify classical integrations by parts at this cutoff. Direct differentiation, using mass conservation, gives

\[
 \frac d{dt}\left[\nu\operatorname{Ent}(F^\epsilon_t)
                 +\int H_N^\epsilon F^\epsilon_t\right]
 =-\int F^\epsilon_t
       |\nabla H_N^\epsilon+\nu\nabla\log F^\epsilon_t|^2.
\]

There is no missing factor of \(\nu\) on the right: expanding the square matches differentiation of \(\nu\operatorname{Ent}+EH\). The initial value is zero because the full initial configuration density is one and every pair difference is Haar. Relative entropy is nonnegative on this probability space.

Fix \(N,\nu,T\) before removing the cutoff. The permitted same-noise theorem, integrated over the independent iid starting vector, gives uniform path convergence almost surely. The limiting path is separated from every collision on its finite horizon. Local uniform convergence of \(g_\epsilon\) away from zero therefore gives M:111–116. Positivity of heat convolution gives

\[
 H_N^\epsilon\ge L_N:=(N-1)g_*/2.
\]

Fatou applies to \(H_N^\epsilon-L_N\ge0\), so \(EH_N\le0\). This needs neither equality of energy expectations nor uniform integrability of singular energy.

For the joint inequality, weak convergence of laws on the compact torus and the entropy variational formula give lower semicontinuity of entropy. The energy lower bound is common at fixed \(N\), while entropy is nonnegative. Thus

\[
 \nu\operatorname{Ent}(F_t)+EH_N-L_N
 \le\liminf_{\epsilon\downarrow0}
       [\nu\operatorname{Ent}(F^\epsilon_t)+EH_N^\epsilon-L_N]
 \le-L_N.
\]

This proves (2.7) without passing a singular Fisher-information identity or a collision boundary term. Cutoff approximation constants need not be uniform in \(N\): the conclusion is obtained for each fixed tuple before a uniform deterministic floor is applied. At zero noise the energy statement instead follows from the supplied deterministic energy identity; entropy division is not performed.

Permutation equivariance and uniqueness give exchangeability. Common translations preserve the SDE and iid Haar law, so the one-particle marginal is Haar. For a pair,

\[
 Eg(X_1-X_2)=\frac{2}{N-1}EH_N\le0,
 \qquad |g|\le g+2|g_*|.
\]

Thus \(E|g(X_1-X_2)|\le2|g_*|\), uniformly in deterministic time, \(N\), and noise. The coefficient-one local expansion transfers this to the stated local inverse-\(s\)-power moment. It supplies no squared-force moment.

### 3.2 Exact heat normalization and diagonal subtraction

Put \(\alpha=(d-s)/2\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). The normalization check is

\[
 A\frac{\Gamma(\alpha)}{(4\pi^2|k|^2)^\alpha}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d}.
\]

The Euclidean Gaussian integral has coefficient one by substituting \(u=|z|^2/(4t)\). Neither the heat-integral truncation \(g^{>r}\) nor its Fourier coefficients are confused with the convolution cutoff for particle approximation.

For \(z\ne0\), the missing small-heat interval satisfies

\[
 A\int_0^r t^{\alpha-1}(p_t(z)-1)dt\ge-Ar^\alpha/\alpha.
\]

The smooth truncated kernel has positive nonzero Fourier coefficients \(a_r(k)\), zero mean, and \(g^{>r}(0)\le Cr^{-s/2}\). The latter uses the large-time exponential tail and the small-time integrand \(Ct^{-s/2-1}\). Its value at zero is nonnegative since it is the sum of positive nonzero Fourier coefficients.

Exact finite summation gives

\[
 \frac1N\sum_{i<j}g^{>r}(x_i-x_j)
 =\frac N2\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2
       -\frac12g^{>r}(0).
\]

There are \(N\) self terms in the full sum and denominator \(2N\), hence exactly \(1/2\), with no \(N^{-1}\) remaining on the diagonal subtraction. The lower comparison error has \(N(N-1)/2\) pairs and coefficient \(1/N\), hence exactly \((N-1)Ar^\alpha/(2\alpha)\). At \(r_N=N^{-2/d}\), both errors have exponent \(s/d\). This proves (3.5) on every collision-free configuration, and trivially for the extended value \(+\infty\) at collisions.

No arbitrary weighted-kernel positivity is used. Positivity is the explicit Fourier quadratic form for this smooth heat-integral truncation.

### 3.3 Every frequency regime

Actual expectation and \(EH_N\le0\) give

\[
 E\sum_{k\ne0}a_{r_N}(k)|\widehat\eta_N(k)|^2\le CN^{-q},
 \qquad q=1-s/d.
\]

If \(0<|k|\le N^{1/d}\), then \([|k|^{-2},2|k|^{-2}]\subset[r_N,\infty)\). Integrating on that interval gives

\[
 a_{r_N}(k)\ge
 A|k|^{s-d}\int_1^2u^{\alpha-1}e^{-4\pi^2u}du=c|k|^{s-d},
\]

with fixed \(c>0\), also at the threshold. Above it the truncated coefficient need not admit that lower bound; instead \(N^{-q}|k|^{d-s}>1\), and \(|\widehat\eta_N(k)|\le1\). Increasing \(C\ge1\) and combining the two valid bounds proves exactly the minimum in (3.7). There is no frequency gap or smallness claim for arbitrarily large modes.

### 3.4 Full configuration entropy and conditional chain rules

For positive diffusivity, the justified singular inequality and deterministic floor imply

\[
 \operatorname{Ent}(F_N(t))\le C\beta N^{s/d}=CN\lambda_N.
\]

This is the entropy of the full \(N\)-coordinate density relative to unit product Haar, not entropy per particle. Partition labels into \(m=\lfloor N/k\rfloor\) blocks of size \(k\) and a possible remainder. If \(F_j\) are the block marginals, the exact decomposition is

\[
 \operatorname{Ent}(F_N)=\sum_j\operatorname{Ent}(F_j)
       +D\!\left(F_N\middle\|\bigotimes_jF_j\right).
\]

Vanishing densities are handled by the density ratio on its support, or positive approximation and lower semicontinuity; the finite entropy bound makes the terms legitimate. The final term is nonnegative by convexity. Equivalently, factorizing into the first block marginal and conditional densities gives

\[
 \operatorname{Ent}(F_N)=\operatorname{Ent}(F_1)
       +\int F_1\operatorname{Ent}(F_{2,\ldots\mid1}),
\]

and conditional convexity gives the same block inequality. Conditioning is on configuration blocks, not on independently evolved reference labels.

Exchangeability identifies the \(m\) equal block entropies, and the remainder is nonnegative. For \(k\le N/2\), \(m\ge N/(2k)\), so

\[
 \operatorname{Ent}(F_N^{(k)}(t))\le2Ck\lambda_N.
\]

The factor two is absorbed by the unspecified constant in M:233. The scalar inequality used there gives \(\|F_N^{(k)}-1\|_1\le2\sqrt{\operatorname{Ent}(F_N^{(k)})}\). Every fixed marginal therefore converges in total variation when \(\lambda_N\to0\), uniformly in deterministic time. At criticality this upper bound does not tend to zero. “No such conclusion” correctly describes a limitation of this bound, not a theorem that total-variation convergence is impossible. Neither entropy estimate bounds arbitrary unbounded \(N\)-dependent gradient products.

## 4. Total-force energy and labelled paths

Restoring the unshifted potential in the supplied R6 exact identity and using initial energy zero gives

\[
 EH_N(X_T)+E\int_0^T\sum_i|B_i|^2dt
 =\nu E\int_0^T\Delta_{Nd}H_Ndt.
\]

The full-space Laplacian is \(2N^{-1}\sum_{i<j}\Delta g(x_i-x_j)\), not \(N^{-1}\sum_{i<j}\Delta g\). Its classical value on collision-free configurations is at most \(\kappa(N-1)\). At Coulomb it is exactly \(c_d(N-1)\): distributionally \(D=c_d(\delta_0-dx)\), while off zero \(\Delta g=c_d\). These uses of a distribution and a pathwise classical derivative are consistent. No collision atom is evaluated along a particle path.

The positive-noise R6 premise includes absolute Laplacian occupation and the true energy martingale passage. The full drift square is integrable before expectations are taken. The new floor then gives

\[
 E\int_0^T\sum_i|B_i|^2dt\le CN^{s/d}+\nu\kappa(N-1)T.
\]

Divide by \(N\) using exchangeability to obtain (4.2). Subtracting each label's free Brownian lift leaves exactly \(\int_0^tB_i\,da\); time Cauchy–Schwarz contributes \(T\int_0^T|B_i|^2\). Torus distance is bounded by lift distance. Doob's \(L^2\) inequality gives \(E\sup_{t\le T}|W_i(t)|^2\le4dT\), so adding the Brownian displacement proves the second maximal estimate. On a critical sequence \(\nu_N=N^{-q}/\lambda_N\), the limiting positive coupling bounds its reciprocal eventually, giving \(O(N^{-q})\).

No positive individual pair-force square is extracted from a sum with signed triple cross terms. The estimate controls each label on the fixed torus scale and makes no singular-observable claim at shrinking distances. At zero diffusivity it uses the separate deterministic energy identity and zero Brownian term.

## 5. Both responses, common translations, and the true mean

The exact homogeneous Fourier formula for \(f_t\) has damping multiplier at most one. Every fixed spatial derivative is bounded by an absolutely summable Fourier seminorm of \(h\), uniformly in time and admitted noise. Near the pair diagonal, cancellation in \(\nabla f(x)-\nabla f(y)\) improves the order of \(K\) by one, so \(|J_t(x,y)|\le C|x-y|^{-s}\) locally and \(\sup_t\|J_t\|_1\le C_h\).

The actual singular pair measure inequality, specialized to zero transport, gives

\[
 \|S_{t,a}v\|_1\le e^{2\kappa(a-t)/N}\|v\|_1.
\]

For the exact homogeneous responses,

\[
 R_xv(x,y)=-\int v(x+w,y)D(dw),
 \qquad \|R_x+R_y\|_{1\to1}\le2\|D\|_{\mathrm{TV}}.
\]

Tonelli against \(|D|\) and translation invariance prove this on \(L^1\) equality classes. At Coulomb \(R_x=-c_dI+c_d\Pi_x\), where \(\Pi_x\) integrates the first slot. The atom multiplies the existing value, and compensation is the projection; neither is dropped. The response is a signed bounded operator, not a Markov generator.

Expand the supplied Borel Volterra inverse. The \(m\)-response term, including its source time integral, is bounded by

\[
 C_h e^{2\kappa(T-t)/N}
       \frac{(2\|D\|_{\mathrm{TV}})^m(T-t)^{m+1}}{(m+1)!}.
\]

The propagator intervals add to at most \(T-t\); their exponential factors are not repeated \(m\) times. Summing gives \(\sup_{N,\nu,t}\|\Phi_t\|_1<\infty\). The same Borel series defines the candidate inverse, so absolute \(L^1\) summability identifies the estimate with the true full inverse. No \(N\)-dependent sup bound has been substituted for it.

For a common translation \(v\), equivariance of the pair process, both responses and source, together with linearity in \(h\), gives

\[
 \Phi[h](x+v,y+v)=\Phi[h(\cdot+v)](x,y).
\]

The \(L^1\) estimate is a continuous linear bound in a fixed sufficiently strong Fourier seminorm of \(h\). Difference quotients of smooth \(h\) converge in that seminorm. Hence for every multi-index \(\alpha\),

\[
 (\nabla_x+\nabla_y)^\alpha\Phi[h]=\Phi[\partial^\alpha h]
 \quad\text{as common-translation weak derivatives in }L^1,
\]

with uniform constants. These are not uniform estimates for all separate relative-coordinate derivatives.

If \(q_t(x)=\int\Phi_t(x,y)dy\), changing the integrated variable gives

\[
 \partial^\alpha q_t(x)
 =\int(\nabla_x+\nabla_y)^\alpha\Phi_t(x,y)dy
\]

in distributions. Every such derivative has a uniform \(L^1\) bound. For \(2L>m+d\), the Fourier coefficients of \(q_t\) are bounded by \((1+|k|^2)^{-L}\) times \(\|(1-\Delta)^Lq_t\|_1\); absolute summation after \(m\) derivatives gives the uniformly bounded \(C^m\) representative. This verifies the derivative topology without assuming separate singular derivative estimates.

Averaging \(h(\cdot+v)\) over translations gives its constant mode, whose source and terminal-zero inverse vanish. Thus the **orbit average** \(\int\Phi_t(x+v,y+v)dv\) vanishes in \(L^1\), and in particular \(\int\Phi_t=0\). Scalar Haar mean zero alone would not imply actual expectation zero under a correlated translation-invariant pair law; the orbit identity supplies that reasoning. The actual law is translation invariant and has the fixed-\(N\) density bound, so Haar-null exceptions do not affect expectation. Therefore \(E\Phi_t(X_1,X_2)=0\), \(Eq_t(X_1)=\int q_t=0\), and the literal statistic has \(EP_N[\Phi_t]=0\). This exact mean is not concentration.

## 6. Physical noise factors and every smoothing exponent

Start from the original statistic, not an imported bracket formula:

\[
 P_N[v]=\frac1{2N^2}\sum_{i\ne j}v(X_i,X_j)
       -\frac1N\sum_i\int v(X_i,y)dy+\frac12\int v.
\]

For symmetric smooth \(v\), the two occurrences of label \(i\) cancel the ordered-pair factor \(1/2\), giving

\[
 \nabla_iP_N[v]=N^{-2}\sum_{j\ne i}G(X_i,X_j)-N^{-1}A(X_i),
 \quad G=\nabla_xv,\quad A=\int G\,dy.
\]

Its Brownian term is \(\sqrt{2\nu}\sum_i\nabla_iP_N\cdot dW_i\). Independent Brownian motions give bracket \(2\nu\sum_i|\nabla_iP_N|^2dt\). Scaling the martingale by \(\sigma_N\) multiplies this by \(\sigma_N^2=Nb_N\). Thus the physical functional is exactly \(2\nu Nb_N E\int\sum_i|\nabla_iP_N|^2dt\). The factor \(1/2\) is not inserted again.

For \(v=\Psi_\delta=e^{\delta\Delta_x}e^{\delta\Delta_y}\Phi\), each joint Fourier coefficient of \(\Phi\) is bounded by its uniform \(L^1\) norm. Summing the differentiated \(x\) heat coefficients gives

\[
 \sup_x|(G_\delta)_k(x)|
 \le C\delta^{-(d+1)/2}e^{-4\pi^2\delta|k|^2}.
\]

This includes \(k=0\), but the background subtraction removes \(k=0\) from the empirical fluctuation. Summing the \(y\) coefficients also gives \(\|G_\delta\|_\infty\le C\delta^{-(2d+1)/2}\). The weighted nonzero-frequency sum has exponent

\[
 \frac{d+1}{2}+\frac{d+(d-s)/2}{2}=\frac{5d-s+2}{4}.
\]

The empirical derivative representation is

\[
 \nabla_iP_N[\Psi_\delta]
 =\frac1N\left[\int G_\delta(X_i,y)(\eta_N-dy)(dy)
                  -\frac1N G_\delta(X_i,X_i)\right].
\]

The self term is necessary even for a row-centered kernel. Its value is smooth and unambiguous; no trace on \(\nabla_x\Phi\) is imposed.

Expand in nonzero \(y\) frequencies and take a supremum in the \(x\) argument before expectation. Minkowski and the all-frequency bound give

\[
 \left(E\sup_x\left|\int G_\delta(x,y)(\eta_N-dy)(dy)\right|^2\right)^{1/2}
 \le CN^{-q/2}\sum_{k\ne0}|k|^{(d-s)/2}\sup_x|(G_\delta)_k(x)|.
\]

This does not condition on \(X_i\) or assume its independence of the empirical measure. Absolute heat summation justifies interchange. There are \(N\) particle gradients, each with prefactor \(1/N\); squaring and multiplying by \(2\nu Nb_N\) leaves a fixed multiple of \(\nu b_N\). Hence

\[
 Q_N[\Psi_\delta]
 \le C\nu b_N\left[N^{-q}\delta^{-r_*}
                    +N^{-2}\delta^{-(2d+1)}\right],
 \quad r_*=(5d-s+2)/2.
\]

For positive \(\nu\), \(\nu b_N=\min(\nu,1)\le1\). Since \(r_*-(2d+1)=(d-s)/2>0\), \(0<q<1\), \(N\ge2\), and \(0<\delta\le1\), the second term is dominated by the first. With

\[
 \gamma=\frac{q}{2r_*}=\frac{d-s}{d(5d-s+2)},
 \qquad\delta_N=N^{-\gamma},
\]

the exponent is \(-q+\gamma r_*=-q/2\), proving (6.8). The physical spatial length is \(\sqrt{\delta_N}\). The check covers every admitted exponent including \(s=d-2\), every frequency, deterministic time, and positive-noise sequence. No constant depending on the full THM028 derivative weights enters this smoothed estimate.

## 7. Four contractions and the precise tail equivalence

For unsmoothed \(\Phi\), the full domain premise supplies the weak/classical identifications and finite-\(N\) integrability. Put \(H(x,y)=G(x,y)-A(x)\). The literal derivative is

\[
 \nabla_iP_N[\Phi]
 =N^{-2}\left[\sum_{j\ne i}H(X_i,X_j)-A(X_i)\right].
\]

The square has \(N(N-1)\) equal-partner terms, \(N(N-1)(N-2)\) ordered distinct-partner terms, \(-2N(N-1)\) cross terms with \(A\), and \(N\) pure \(A\) terms, all over \(N^4\). Exchangeability identifies the respective expectations. Multiplication by \(2\nu Nb_N\) gives exactly \(2\nu b_N/N^2\) and the four terms in (7.2). At \(N=2\), no variable \(X_3\) or triple expectation is introduced. Only the last expectation is automatically a Haar integral from one-body invariance. The combined expression is nonnegative; its signed terms need not be.

For fixed \(N\), \(v\mapsto\sqrt{Q_N[v]}\) is the seminorm of a linear particle-gradient map in \(L^2\) of probability, time, labels and Euclidean components. Thus

\[
 |\sqrt{Q_N[\Phi]}-\sqrt{Q_N[\Phi-\Psi_\delta]}|
 \le\sqrt{Q_N[\Psi_\delta]}.
\]

All three quantities are finite at each fixed \(N\), by the domain premise and smoothing. Setting \(\delta=\delta_N\) proves both directions of (7.4), not just sufficiency. The two square-root sequences differ by a sequence tending to zero, so their limsups coincide, including \(+\infty\). Positive limsup in one is equivalent to positive limsup in the other.

For every fixed \(\delta>0\), the same estimate and (6.6) give

\[
 \limsup_{N\to\infty}Q_N[\Phi-\Psi_\delta]
 =\limsup_{N\to\infty}Q_N[\Phi]
\]

as extended nonnegative values along the admitted sequence. The subsequent \(\delta\downarrow0\) limit is therefore equivalent to the full target. Neither residual monotonicity in \(\delta\), interchange of limits, nor separate absolute estimates on signed contractions is needed. Bounding those contractions individually could be sufficient but would not be an equivalent reformulation of the combined residual.

At fixed \(N\), heat smoothing converges in the pair Haar \(H^1\) topology at each time. The THM028 uniform-in-time finite-\(N\) \(H^1\) bound and heat contraction dominate the time integral. The particle-gradient map is continuous from pair \(H^1\) to configuration \(L^2\), by the finite sum and Jensen for \(A\). The actual density bound \(e^{\kappa(N-1)T}\) then transfers convergence to \(Q_N\). This proves the reversed fixed-\(N\) limit only. The exponential density constant and possibly \(N\)-dependent domain norm prevent this argument from proving (7.4). A uniform pair-energy moment, low-mode control, or total variation for bounded fixed tests does not supply uniform integrability of these varying singular gradients.

The exact first unproved assertion toward the full target is M:429–431, not a hidden coefficient in (7.2) or a false claim that the residual condition is merely sufficient. This audit does not promote that open assertion and does not attempt to repair it.

## 8. Initial singular BBGKY test, with compensation

For a globally smooth configuration test \(a\), the literal generator has Haar-integrable drift since \(K\in L^1\). Fixed-\(N\) density domination makes its expected absolute occupation finite. Local Itô and the bounded smooth test gradient justify the global weak identity without differentiating a singular density.

At \(t=0\), path continuity gives weak convergence of laws to product Haar. Approximate \(L_Na\) in Haar \(L^1\) by continuous functions. The density bound, uniform on a short interval at fixed \(N\), controls approximation errors; weak convergence controls the continuous approximant. Hence \(EL_Na(X_t)\to\int L_Na\), justifying the right derivative of every smooth-test expectation at zero.

Integrating unused labels in the weak equation produces internal coefficient \(1/N\) and external coefficient \((N-k)/N\) in (8.1). At the iid initial density, the external force vanishes since \(\int K=0\), and diffusion vanishes. Each unordered retained pair contributes the same divergence \(D\) from both coordinates, so

\[
 \left.\partial_tF_t^{(k)}\right|_0
 =-\frac2N\sum_{i<j\le k}D(x_i-x_j)
\]

in distributions. For \(k=N\) the external term is absent. This derivative can contain a Coulomb collision measure even though paths do not collide: it is a weak initial derivative, not a pointwise density formula.

For the real smooth row-centered vector probe \(H_t\), set \(a_t=H_t(x_1,x_2)\cdot H_t(x_1,x_3)\). Its Haar integral is identically zero in time, so the explicit time derivative contributes zero. In the initial distributional derivative, \(D_{12}\) and \(D_{13}\) vanish after integrating the remaining centered partner. Finite-measure Fubini is legitimate for these smooth integrands. Only \(D_{23}\) remains:

\[
 C_N'(0)=-\frac2N\int dx\int D(dw)\int H_0(x,y)\cdot H_0(x,y-w)dy.
\]

The convolution Fourier identity is absolutely convergent for smooth \(H_0\). Since \(D=-\Delta g\), its nonzero multiplier is

\[
 d_k=4\pi^2|k|^2\widehat g(k)=4\pi^2c_{d,s}|k|^{s+2-d}>0.
\]

For real \(H_0\), the paired coefficients are complex conjugates and the vector dot product yields the sum of squared moduli. This proves the nonpositive derivative (8.3), with no diffusivity contribution.

At Coulomb, \(4\pi^2c_{d,d-2}=c_d=(d-2)|\mathbb S^{d-1}|\) by the gamma recurrence. Retaining both terms of \(D=c_d(\delta_0-dw)\) gives

\[
 \int dx\int D(dw)\int H_0(x,y)\cdot H_0(x,y-w)dy
 =c_d\left(\|H_0\|_2^2-\int\left|\int H_0(x,y)dy\right|^2dx\right)
 =c_d\|H_0\|_2^2.
\]

Compensation cancels only because the row mean is exactly zero. This independently checks the coefficient and endpoint. The derivative is taken at fixed \(N\) and fixed smooth probe. No later-time sign, \(N\)-uniform Taylor remainder, or substitution of a singular residual gradient is justified.

## 9. Conditional initial window and limits of the conclusion

Use only the stipulated integrated Haar estimate

\[
 \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt\le CN^a,
 \qquad a=s/(s+2)<1.
\]

The exact Haar calculation, recovered from the original statistic, is

\[
 \int\sum_i|\nabla_iP_N|^2dm_N
 =\frac{N-1}{N^3}\|G\|_2^2-\frac{N-2}{N^3}\|A\|_2^2.
\]

Pair symmetry gives \(2\|G\|_2^2=\|\nabla_{x,y}\Phi\|_2^2\). Multiplication by \(2\nu Nb_N\) and time integration yield reference bound \(Cb_NN^{a-1}\). For \(0\le\tau\le T\), density domination and nonnegativity alone then give

\[
 Q_N^{[0,\tau]}[\Phi]
 \le e^{\kappa(N-1)\tau}Q_N^{\mathrm{Haar},[0,T]}[\Phi]
 \le Cb_Ne^{\kappa(N-1)\tau}N^{a-1}.
\]

For \(0<\theta<1-a\) and the stated minimum defining \(\tau_N\), the exponential is at most \(N^\theta\); since \(b_N\le1\), (9.2) follows. The minimum with \(T\) preserves the bound. At \(T=0\) all integrals are zero. Only an integrated reference estimate is used. For positive fixed \(T\), the window shrinks like \((\log N)/N\); it says nothing about a positive fixed-horizon tail. Its premise remains conditional.

The frozen exclusions are necessary and correctly stated. The old energy-floor regime, full microscopic subcriticality, and microscopic criticality are distinct. Bounded diffusivity excludes an assertion uniform over all subcritical sequences with \(\beta_N\downarrow0\). No change of mean-field centering, Gaussianity, finite critical truncation, or enlarged theorem range is inferred.

## 10. Independent evidence, output integrity, and handoff

The newly written "AUDITS/HOSTILE/ROUND_010_SMOOTHING_ARTIFACTS/independent_exact_check.py" uses only the Python standard library. It imports, opens, and runs no earlier checker. The result is **PASS: 2,024 exact assertions**, recorded in "independent_exact_results.json".

The representation is rational Laurent character algebra. The implemented derivative multiplies by the integer frequency and equals physical differentiation divided by \(2\pi i\). Squared-gradient products restore the minus sign from \(i^2\), and the force generator is checked after division by \((2\pi)^2\). In singular-kernel tests, only the finitely many Fourier coefficients capable of pairing with the smooth probe affect its weak generator integral. The positive overall Riesz normalization is restored analytically above; no finite Fourier dynamics is substituted for the singular theorem.

The tests include:

- Literal ordered-pair differentiation, centered/empirical formulas, smooth self subtraction, and Haar brackets at \(N=2,3,4,5\), for constant, additive, relative, and mixed symmetric kernels.
- Four-term expansions under explicit positive nonproduct exchangeable densities with Haar one-body marginals. Their certified lower bound is at least \(5/8\); this is not an iid-only diagnostic. Physical factors are tested at rational positive diffusivities below, at, and above one.
- Exact Fourier self-diagonal subtraction for \(N=2,\ldots,9\).
- Direct force-label generator integration for real row-centered vector probes at \(N=3,4,5\), sub-Coulomb/Coulomb exponents, canceled partial contractions, zero/positive diffusion, probe time dependence, and the compensated Coulomb norm identity.
- Full configuration, sequential conditional, and block entropy chain identities in finite positive exchangeable probability models. Logarithms are represented exactly as rational combinations of prime logarithms. Positivity of relative entropy is an analytic convexity argument, not a finite computation.
- Rational normalization/exponent comparisons over dimensions 3 through 16, including Coulomb and fractional exponents close to the endpoints.
- All 22 input hashes.

There is no random seed, numerical tolerance, simulation, or computational certificate of singular uniform integrability. The diagnostics support the analytic review. This report and its supporting files are sealed; no prior report or candidate input was revised.

The recoverable outcome is a conditional hostile pass for all claimed bounded conclusions, with the full singular target open at (7.4). The next mathematical action, outside this review, is to prove or disprove that actual-law residual estimate while preserving the complete nonnegative combination and the same preparation. Root may integrate the report and assign canonical audit status; this worker has not changed canonical ledgers or independently certified any conditional premise.
