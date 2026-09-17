# Separate hostile disposition of the THM-014 symmetry repair

Date: 2026-09-17 UTC. Parent task: TASK-018, with explicit follow-up to review the additive repair. Reviewer: /root/r002_falsification, gpt-6-astra Max. Worktree: /private/tmp/hocf-round002-falsification-20260917. Commit: a06178658d1e3d458536ff312ca793947212ec67.

## 1. Verdict and immutable provenance

**HOSTILE_REVIEW_PASS for the submitted THM-014 repair.** The exact submitted card and additive memorandum make the necessary symmetrization mandatory in every rooted first-slot derivative and generator formula. This is sufficient to repair local finding PC-01. All numerical moment, bracket, generator, summability, and conditional cutoff bounds retain their original constants and hypotheses.

This is a separate disposition of new submitted bytes. It does not alter or retract the original audit's failure of the unrestricted unsymmetrized identity. The original THM-012 card, original construction report, and original hostile audit remain unchanged. The new theorem is the original collection of qualified conclusions together with the mandatory correction in the two new documents.

| Reviewed or preserved document | SHA-256 |
|---|---|
| THEOREMS/THM-014_REPAIRED_SMOOTH_ORDER_AND_CUTOFF.md | 23ea8ae628309c9a4bbbe21289cd3e84a58085e98863e5891d7c1fbe235477b3 |
| MEMORANDA/ROUND_002_POWERCOUNT_SYMMETRY_REPAIR.md | 202143d25d67d33a4ce7f291a69714d37b8ba74883160ab05926a5b3fbe2c94d |
| THEOREMS/THM-012_SMOOTH_ORDER_AND_CUTOFF.md | 93e889a841d66d3554d0236840f87d73d4f240166da6978d5018bbb77cd5e296 |
| MEMORANDA/ROUND_002_POWERCOUNT.md | f0bd6a670b194767afa2fe75f259d59bfe4589433f21252992d1dde79c92f01d |
| AUDITS/HOSTILE/ROUND_002_POWERCOUNT_REVIEW.md | 7ee6af5a61958453352219f69677e4fa9cd8d027f7c104805d3ece5d5e0b9956 |

The complete original dossier and its prerequisite hashes are recorded in the preserved audit. Its input manifest was rechecked successfully before the present disposition. Both repair files were read and hashed in this worktree; this verdict concerns those exact submissions, not merely the earlier proposed wording.

The reviewer did not construct THM-012 and did not read its constructor's code. The reviewer previously constructed the independent fixed-order residual argument, then the Gaussian criterion and viscosity-continuity result; the same reviewer subsequently issued the original power-counting audit. This is follow-up hostile review in that disclosed context, not a fresh-session, blind, or second-independent-auditor certification. No child worker was used.

## 2. Exact content and sufficiency of the repair

For a deterministic kernel on the product of \(k\) unit tori, define

\[
 \operatorname{Sym}_k\Phi(z_1,\ldots,z_k)
 =\frac1{k!}\sum_{\pi\in S_k}
       \Phi(z_{\pi(1)},\ldots,z_{\pi(k)}).
 \tag{2.1}
\]

At a fixed time the background \(\mu\) is a deterministic probability measure, and the particle coordinates may be arbitrary, including coincident coordinates. The deleted statistic is the alternating sum over occupied slot sets \(A\subset[k]\), injective maps \(A\to[N]\), and background integrals in the remaining slots, with coefficient
\((-1)^{k-|A|}N^{-|A|}\).

For each permutation in (2.1), permuting \(A\), its injective label map, and the background variables is a bijection of the terms in this definition, preserving that coefficient. Therefore, configuration by configuration,

\[
 U_k^\mu[\Phi]=U_k^\mu[\operatorname{Sym}_k\Phi].
 \tag{2.2}
\]

This proof does not require \(k\le N\). Occupied sets larger than \(N\) have no injective label maps on either side. The cases \(k=0,1\) have the usual identity symmetrization.

For every nonnegative integer \(m\), a slot permutation preserves the total order of every partial derivative and the domain of its supremum. The maximum \(C^m\) norm used in the submitted report consequently satisfies

\[
 \|\operatorname{Sym}_k\Phi\|_{C^m}
 \le \frac1{k!}\sum_{\pi\in S_k}
                  \|\Phi\circ\pi\|_{C^m}
 =\|\Phi\|_{C^m}.
 \tag{2.3}
\]

The same statement holds componentwise if needed. There is no factor \(k!\), \(k\), or derivative-dependent permutation constant. Applied at each time, it preserves all the displayed deterministic time suprema. Time differentiation commutes with the finite average whenever the original kernel has the assumed time regularity.

For completeness, the unrestricted particle derivative has a sum over rooted slots:

\[
 \nabla_{x_i}U_k^\mu[\Phi]
 =\frac1N\sum_{a=1}^k
       V_{k-1}^{(i)}[J_a\Phi(x_i;\,\cdot)],
 \tag{2.4}
\]

where \(J_a\Phi(z;\,\cdot)\) is \(\nabla_a\Phi\) with \(z\) inserted in slot \(a\) and the other arguments retaining their relative order. To prove (2.4), a differentiated term must place label \(i\) in one occupied slot \(a\). Injectivity excludes it from all remaining occupied slots. Removing \(a\) leaves precisely the rooted statistic, with denominator \(N\), an additional factor \(1/N\), and sign
\((-1)^{(k-1)-(|A|-1)}\). The background has no dependence on the particle coordinate being differentiated.

For a symmetric kernel the \(k\) rooted terms in (2.4) agree after relabeling the remaining slots. Differentiate the exact equality (2.2), then apply that symmetric formula. This yields the repaired identity

\[
 \nabla_{x_i}U_k^\mu[\Phi]
 =\frac{k}{N}V_{k-1}^{(i)}
       [\nabla_1\operatorname{Sym}_k\Phi(x_i,\cdot)].
 \tag{2.5}
\]

The root-excluded empirical measure retains mass \(1-1/N\), and its centered version retains mass \(-1/N\). Symmetrization changes neither fact and never replaces the denominator by \(N-1\).

The original counterexample remains decisive. For \(k=2\) and \(\Phi(x,y)=h(y)\),

\[
 U_2^\mu[\Phi]=-\frac{\eta(h)}N,\qquad
 \nabla_{x_i}U_2^\mu[\Phi]=-\frac{\nabla h(x_i)}{N^2},
 \qquad \nabla_1\Phi=0.
 \tag{2.6}
\]

The unsymmetrized first-slot formula is false. In (2.5), however,
\(\operatorname{Sym}_2\Phi=(h(x)+h(y))/2\). Its rooted derivative is the constant-in-the-remaining-slot vector \(\nabla h(x_i)/2\), whose rooted order-one statistic equals \(-\nabla h(x_i)/(2N)\). The factor \(2/N\) gives precisely (2.6).

Thus the repair corrects the false identity itself; it does not conceal it inside an inequality or impose a new particle-law assumption.

## 3. Martingales, cross variations, and generator use

For the smooth stochastic model, the martingale part of the statistic is defined by its actual particle gradient:

\[
 dM_k^\Phi
 =\sqrt{2\nu}\sum_{i=1}^N
             \nabla_{x_i}U_k^{\mu_t}[\Phi_t]\cdot dW_i
 =\frac{k\sqrt{2\nu}}N\sum_{i=1}^N
       V_{k-1}^{(i)}
       [\nabla_1\operatorname{Sym}_k\Phi_t(x_i,\cdot)]\cdot dW_i.
 \tag{3.1}
\]

The first equality and (2.2) show that this is the same martingale as the one belonging to the original statistic. Time dependence of the deterministic background and kernel affects finite-variation terms; it does not alter (3.1).

The original rooted estimate (5.3), which is itself valid for any smooth root-dependent kernel, gives

\[
 \left\|V_{k-1}^{(i)}
     [\nabla_1\operatorname{Sym}_k\Phi_t(x_i,\cdot)]\right\|_{L^2}
 \le \sqrt d\,D_{k-1,2}(N)N^{-(k-1)/2}
                 \|\Phi_t\|_{C^{(k-1)q+1}}.
 \tag{3.2}
\]

Here (2.3) removes the symmetrization without increasing the right-hand side. The estimate is uniform in the root before its random position is inserted, so no root/other-particle independence is used.

For two possibly nonsymmetric kernels of orders \(k,\ell\), the exact cross bracket uses the two symmetrized rooted derivatives in (3.1). Brownian covariance and Cauchy--Schwarz in the particle sum, time, and probability give exactly the original numerical bounds (5.6). In particular, with \(B_k'=\sup_t\|\Phi_{k,t}\|_{C^{(k-1)q+1}}\),

\[
\begin{aligned}
 \mathbb E[M_k^\Phi]_T
 &\le 2\nu Td\,k^2(B_k'D_{k-1,2}(N))^2N^{-k},\\
 \mathbb E\operatorname{TV}_{[0,T]}[M_k^\Phi,M_\ell^\Psi]
 &\le 2\nu Td\,k\ell B_k'B_\ell'
       D_{k-1,2}(N)D_{\ell-1,2}(N)N^{-(k+\ell)/2}.
\end{aligned}
 \tag{3.3}
\]

Neither the constants nor the temperature or particle-number exponents change. Multiplication by the original \(\sigma_N^2\) has exactly its original effect. The pair normalization \(P=U_2/2\) still divides self brackets by four and its cross brackets by two.

For generator formulas the new card explicitly requires the same replacement before applying the frozen symmetric recursion. This addition matters: a correction confined to noise would not by itself authorize an unrestricted unsymmetrized use of first-slot or last-slot representatives in the drift. The submitted card covers that point, and the additive memorandum says that general kernels must first use their symmetrization in the generator rows as well.

Apply the frozen symmetric recursion to \(\operatorname{Sym}_k\Phi\), with that kernel substituted in each displayed operator. Every Section 6 operator bound is a bound by a specified \(C^{m+1}\) norm of its input. Equation (2.3) keeps the same right-hand side expressed using the original \(\Phi\). The upward, internal, single-lowering, and double-contraction coefficients and their power table therefore survive. This is not a claim that each unsymmetrized operator kernel equals the corresponding symmetrized one as a function; such equality is unnecessary and is not part of the repair.

## 4. Disposition of downstream conclusions

References in this table are to the immutable original construction report.

| Conclusion | Disposition after the submitted repair |
|---|---|
| Empirical all-moment estimate, Section 2 | Unchanged. It contains no test-kernel symmetry assumption. |
| Exact partition identity, Section 3 | Unchanged for arbitrary kernels, including \(k>N\). It did not use the false compact derivative. |
| Tensor norm estimates, explicit partition constants, and iid biases, Section 4 | Unchanged for arbitrary kernels. Symmetrization is optional for these assertions. |
| Root-exclusion measure estimate, rooted partition constants, and rooted norm inequalities, (5.1)–(5.4) | Unchanged. In the martingale application use the derivative of the symmetrized kernel; (2.3) preserves the displayed original norm. |
| Exact martingale formula (5.5) and its preceding gradient identity | Repaired by mandatory use of \(\operatorname{Sym}_k\Phi\); the original first-slot formula remains valid when \(\Phi\) is symmetric. |
| Self and cross bracket bounds (5.6), all-temperature scaling, and pair normalization | Same inequalities and constants for arbitrary kernels, by (3.1)–(3.3). |
| Generator operators and power-counting table, Section 6 | Same coefficients, numerical bounds, and limitations. Use the frozen symmetric recursion, replacing a general input kernel by its symmetrization first. |
| Statistic and martingale series criteria (7.2)–(7.3) | Same sufficient absolute-majorant criteria for arbitrary kernels. The martingale sum still includes cross variations through integrand \(L^2\) convergence. |
| Concrete factorial/geometric lemma (7.4)–(7.6) | Unchanged as stated, since that lemma already assumes symmetric kernels. No proof of its additional kernel-growth premise is supplied by the repair. |
| Heat upper/lower bounds and coupling-constant divergence, Section 8 | Unchanged. They concern the interaction and its regularization, independently of slot symmetry. |
| Slow-cutoff criterion and conditional diagonal cutoff choice, Section 9 | Unchanged for the regularized model's own quantities and the same fixed-cutoff norm envelopes. The repair supplies no missing norm envelope or singular-model comparison. |

Consequently the local correction is sufficient for the entire collection of claims reviewed in the original audit. No further load-bearing defect is introduced or left unresolved by this repair. The earlier pass findings remain usable, and PC-01 is repaired for the new THM-014 assertion.

The exclusions are also unchanged. This disposition does not establish the actual hierarchy's factorial normalization, geometric kernel growth, summability of all drift terms, a singular particle-model comparison, a singular critical limiting law, or the full campaign's M2/M3 target. It approves the repaired smooth iid estimates and the stated sufficient conditional criteria only.

## 5. Verification and handoff

The original independent exact test file includes both the nonsymmetric counterexample and its symmetrized correction, along with its partition, rooted, bias, moment, and bracket checks. It was rerun for this disposition: PASS, 1,110 independent exact rational checks. Its preserved SHA-256 is 461f705b9814e2dad5285e0269e99c5e0d76707f5fdb583a20755f2d39379bf9.

The four-entry original input manifest was rechecked successfully. The five hashes in Section 1 were verified before and after writing this report. The campaign verifier passed, the tracked diff whitespace check passed, and this report passed the control-character scan. These checks support provenance and arithmetic; the proof in Sections 2–3 supplies the universal symmetrization argument.

Only this new repair-review file was written for the present follow-up. No original proof, submitted card, audit, canonical ledger, or supporting code was edited. No commit, push, dependency installation, external citation, or new source assumption was used. Root may record the new repaired claim's hostile-review pass while retaining the immutable THM-012 submission defect and its original audit.
