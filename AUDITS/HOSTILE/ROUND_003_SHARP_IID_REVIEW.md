# Separate hostile review of the sharp iid criterion and first-moment extension

Date: 2026-09-17 UTC. Task: TASK-026 with its separately sealed THM-018 supplement. Reviewer: /root/r002_falsification, gpt-6-astra Max. Worktree: /private/tmp/hocf-round003-hostile-20260917, based on published 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2.

## 1. Separate verdicts

**THM-019: HOSTILE_REVIEW_PASS.** The root construction proves a positive-probability lower bound at the stated scale, a matching first-absolute-moment upper bound, the necessary-and-sufficient vanishing criterion, and the asserted tightness/non-tightness conclusions. The lower bound controls cancellation by the centered outer statistic rather than inferring probability behavior from infinite variance. Its constants can be chosen once, independently of particle number and temperature.

**THM-018: HOSTILE_REVIEW_PASS.** The independently sealed supplementary reconstruction proves all three displayed first-absolute-moment rates, including the square-integrability endpoint. Its explicit constants and threshold pass. The factor \((N-1)/(2N)\) for the centered inner statistic is retained before the stated upper simplification. Agreement with the upper half of THM-019 does not constitute a separate reconstruction of THM-019's lower bound.

A minor quantified proof-language point is recorded openly in Section 6: the root report's line 118 needs a further subsequence tending to infinity when starting with a merely unbounded subsequence. The theorem as stated is correct, and the explicit elementary extraction below completes its proof without any additional hypothesis. No inequality, normalization, threshold, or theorem range requires repair.

The original TASK-023 review remains sealed and unchanged at SHA-256 6676c824052a7b1a6444b6af15eed5de948ec3dc4503b9e7adbb9932bff6a9b5. Its statement that the then-supplied proofs did not resolve the converse remains an accurate historical verdict. This new report reviews new arguments; it does not retroactively strengthen either original Round 003 submission or that earlier review.

Both new claims concern only the bare mean-zero Riesz potential under initial iid Haar preparation. No endpoint distribution, stable law, actual backward-corrector estimate, interacting or Gibbs law, singular dynamic comparison, or full fluctuation theorem is certified.

## 2. Exact submissions and actual context

The initial sharp-claim manifest was checked before reading the root proof or card. The supplemental manifest was checked before reading the independent reconstruction or THM-018 card. Both manifests and the preserved TASK-023 report were rechecked after the present report was written.

| Input | SHA-256 |
|---|---|
| TASKS/ACTIVE/TASK-026_ROUND003_SHARP_REVIEW.md | ae3e0c81e1c0c7b0b52296e7fc80c19ba074d9f6aa63e4a86a5bbcec582368aa |
| THEOREMS/THM-019_SHARP_IID_RIESZ_PAIR_CRITERION.md | bfcc98dd9f0edeaa24a91d0348fd9932bc4bce3a23443b9901f2aaa35a7181a1 |
| MEMORANDA/ROUND_003_SHARP_IID_PAIR_LOWER_BOUND.md | 98e9259f79bc09164f6e304e552da338ae4b93217f9d586912c03f54332d2268 |
| THEOREMS/THM-018_IID_RIESZ_L1_RATES.md | 7526dbdbfbfaf20756830a8acfc33f3607a66e8d7aaf13d58a1e84e0d85e80cb |
| AUDITS/BLIND_RECONSTRUCTION/ROUND_003_PROBABILITY_RECONSTRUCTION.md | 9eb7e54ab0fa6e38ef226cd2d815d618d2b421718ed0e1c59bb07dc27ae79e6f |

Initial sharp-input manifest SHA-256: 68156e7f199ed5a24fbd5af3f77f8db9ae6f0d72879e9583cc8f2321ee368dc5. Supplemental manifest SHA-256: 8bf62bcda46b228ce8dcfa66376b36d7a55094cf73260558a5fca8944ad5dda9.

Below, “root proof” denotes the exact lower-bound memorandum in this table, and “supplement” denotes the exact statement-only probability reconstruction. The earlier collision proof, with hash 9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4, and the iid pair proof, with hash 68ed536685133906877efe7599f1e93300e796ad0b62bb6b228837df08438d5a, are the permitted previously reviewed prerequisites. They supply the frozen real-space normalization and exact canonical variance.

The reviewer did not construct THM-019 or THM-018. The reviewer did construct earlier smooth results and review the original Round 003 submissions. TASK-023 was sealed before these new proofs were opened. This is a separate hostile review with disclosed context reuse, not a new blank session or blind reconstruction. The supplement itself discloses reuse of its author's own iid-pair prerequisite and states that its new proof was sealed without seeing the root lower-bound construction. Its upper-bound agreement is recorded at precisely that scope. Neither author's other worktree or code was inspected or run, and no child worker was used.

The exact negation tested is an admissible fixed dimension and exponent, initial iid Haar family, or permitted temperature sequence violating a displayed bound or claimed implication. The arguments below rule out such a violation in the stated ranges. No external source theorem or unverified singular normalization is required.

## 3. Per-result findings

| Submitted assertion | Verdict and reason |
|---|---|
| Root (2), positive local singularity and finite outer variance constant | PASS. The coefficient-one local expansion gives positivity on a sufficiently small fixed ball; the finite outer contribution is absorbed using \(d-2s<0\). |
| Root Section 2, close-pair indicator independence in pairs | PASS. Conditional ball probabilities are constant under Haar translations; this is stronger than conditional independence alone and gives the required unconditional joint probability. Mutual independence is not asserted. |
| Root (3), close-pair count lower bound and \(c_0\) | PASS. The exact second moment and finite-\(N\) mean interval give precisely the stated constant. |
| Root (4)–(5), centered outer/positive inner decomposition | PASS. The mean subtraction has coefficient \((N-1)/(2N)\); the positive inner sum prevents cancellation among inner terms. |
| Root (6)–(7), outer variance and Chebyshev factor | PASS. The variance is at most \(C_Vu_N^2/2\), and the threshold gives exactly \(32C_V\delta^{2s}\). |
| Root (8), compatible fixed \(\delta\), constants \(a,p\) | PASS. The strict condition \(2s>d\) makes the bad-event probability smaller than half the close-pair lower bound. No independence of those two events is needed. |
| Root Section 4, first-moment upper bound | PASS. The centered singular inner term needs only \(L^1\), with the exact unordered-pair coefficient. |
| Root (9), necessity and sufficiency in probability and \(L^1\) | PASS. The positive lower tail proves necessity directly; the absolute-moment upper bound proves sufficiency. |
| Root tightness consequences, line 118 and card | PASS for the theorem. Section 6 records the needed explicit further-subsequence extraction and the overly literal reading it avoids. |
| Supplement (2.11), explicit local remainder bound | PASS. All four terms majorize their respective parts of the heat representation with the frozen coefficient. |
| Supplement (4.6), (4.8)–(4.10), constants \(C_1,K_0,C_2\) | PASS. Polar integration and the outer-region integral give the specified parameter dependence. |
| Supplement (7.1)–(7.3), global split and exact centered inner factor | PASS. It is an unconditional decomposition, with no discarded close-pair event. |
| Supplement (7.4)–(7.6), all three rates and threshold | PASS. The two terms balance at radius \(N^{-2/d}\); the logarithmic endpoint constant and threshold are correct. |
| Scope exclusions in both cards | PASS. Bare initial iid data are kept separate from corrector dynamics, singular model comparison and endpoint distributions. |

## 4. Independent check of the positive lower probability

Fix \(d/2<s<d\). Write \(r_N=N^{-2/d}\) and \(u_N=N^{2s/d-2}\). The already proved local expansion permits a fixed \(R<1/4\) and positive constants \(C_\tau,C_V\), depending only on \(d,s\), such that for \(r<R\),

\[
 g(z)\ge\frac12|z|^{-s}\quad(0<|z|<R),\qquad
 0<\tau_r\le C_\tau r^{d-s},\qquad
 V_r\le C_V r^{d-2s}.
 \tag{4.1}
\]

To see that the constants introduce no hidden dependence, choose \(R\) so the fixed smooth remainder obeys \(|H(z)|\le|z|^{-s}/2\) there. The radial integral then bounds \(\tau_r\). For \(V_r\), the square integral off any fixed smaller ball is finite; since \(r^{d-2s}\) grows as \(r\) decreases, that fixed contribution is absorbed into the same bound. One may take
\[
 N_0=\max\{2,\lfloor R^{-d/2}\rfloor+1\},
 \tag{4.2}
\]
so \(r_N<R\) for every \(N\ge N_0\). All subsequent choices are independent of \(N\) and \(\beta_N\).

For a fixed \(0<\delta<1\), let \(I_{ij}\) indicate
\(\operatorname{dist}(X_i,X_j)<\delta r_N\), \(i<j\), and let \(Z_N=\sum I_{ij}\). The embedded torus ball has probability

\[
 q_N=v_d\delta^dN^{-2}.
 \tag{4.3}
\]

For pairs sharing a label, condition on that label. The other two positions are independent Haar variables, and each conditional event has the same probability \(q_N\), independent of the conditioned position. Hence their joint probability is \(q_N^2\). Disjoint pairs use independent labels. This proves independence for each pair of distinct indicators; it does not assert independence of a triangle of indicators.

With \(M=N(N-1)/2\) and \(m_N=Mq_N\),

\[
 \mathbb E Z_N^2
 =Mq_N+M(M-1)q_N^2
 =m_N+m_N^2-Mq_N^2
 \le m_N+m_N^2.
 \tag{4.4}
\]

Cauchy--Schwarz applied to \(Z_N\mathbf1_{\{Z_N>0\}}\) gives
\(\mathbb P(Z_N>0)\ge m_N^2/\mathbb EZ_N^2\ge m_N/(1+m_N)\).
The exact factor \(M/N^2=(N-1)/(2N)\) lies between \(1/4\) and \(1/2\). Therefore

\[
 \mathbb P(Z_N>0)\ge c_0\delta^d,\qquad
 c_0=\frac{v_d}{4(1+v_d/2)}.
 \tag{4.5}
\]

This recomputes the root constant without a Poisson approximation.

Let \(k_r=g\mathbf1_{\{\operatorname{dist}\ge r\}}+\tau_r\), which has zero Haar mean. On every configuration avoiding collisions,

\[
 P_N[g]=P_N[k_{r_N}]
   +\frac1{N^2}\sum_{i<j}g(X_i-X_j)
                   \mathbf1_{\{\operatorname{dist}(X_i,X_j)<r_N\}}
   -\frac{N-1}{2N}\tau_{r_N}.
 \tag{4.6}
\]

Haar collisions have probability zero, and all terms are integrable; the identity therefore suffices for all probability statements. Every summand in the middle is nonnegative by (4.1). On \(\{Z_N>0\}\), one summand is at least
\(\frac12(\delta r_N)^{-s}\). The two exact scaling identities are

\[
 N^{-2}r_N^{-s}=r_N^{d-s}=u_N.
 \tag{4.7}
\]

Consequently (4.6) is at least
\[
 P_N[k_{r_N}]+\left(\frac{\delta^{-s}}2-\frac{C_\tau}2\right)u_N.
 \tag{4.8}
\]
The bound uses the finite-\(N\) mean coefficient only by replacing it with its valid upper bound \(1/2\).

The outer kernel is canonical and in \(L^2\). Its exact iid variance gives

\[
 \operatorname{Var}(P_N[k_{r_N}])
 =\frac{N-1}{2N^3}V_{r_N}
 \le\frac{C_V}2\left(1-\frac1N\right)u_N^2
 \le\frac{C_V}2u_N^2.
 \tag{4.9}
\]

In particular there is no missing first projection or infinite-variance expansion. Its mean is zero. Chebyshev at threshold \(\delta^{-s}u_N/8\) gives exactly

\[
 \mathbb P\!\left(P_N[k_{r_N}]<-\frac{\delta^{-s}}8u_N\right)
 \le32C_V\delta^{2s}.
 \tag{4.10}
\]

Choose one \(\delta\in(0,1)\) with
\(\delta^{-s}\ge2C_\tau\) and
\(\delta^{2s-d}\le c_0/(64C_V)\).
Such a choice exists because \(s>0\) and \(2s-d>0\). The deterministic contribution in (4.8) is then at least \(\delta^{-s}u_N/4\). On the complement of the bad outer event it leaves at least \(\delta^{-s}u_N/8\). Subtracting (4.10) from (4.5) yields

\[
 \mathbb P\!\left(P_N[g]\ge\frac{\delta^{-s}}8u_N\right)
 \ge\frac{c_0}2\delta^d.
 \tag{4.11}
\]

This uses only \(\mathbb P(E\cap F^c)\ge\mathbb P(E)-\mathbb P(F)\); the two events can be dependent. Thus the submitted
\(a=\delta^{-s}/8\) and \(p=c_0\delta^d/2\) are correct positive constants. The lower first-moment bound \(ap\,u_N\) follows directly.

The strict range \(2s>d\) is load bearing here: it permits the outer bad-event upper bound, with power \(\delta^{2s}\), to be smaller than the close-pair lower bound, with power \(\delta^d\). This proof has not been extended to \(2s=d\) by formal substitution.

## 5. The matching upper bound and the independent THM-018 rates

For the root proof's small positive ball, let
\(\ell_r=g\mathbf1_{\{\operatorname{dist}<r\}}-\tau_r\).
Both \(k_r\) and \(\ell_r\) have zero mean and \(g=k_r+\ell_r\) everywhere off zero. Positivity inside the ball implies \(\|\ell_r\|_1\le2\tau_r\). The exact unordered-pair count gives

\[
 \mathbb E|P_N[\ell_r]|
 \le\frac{N-1}{2N}\|\ell_r\|_1
 \le\frac{N-1}{N}\tau_r
 \le\tau_r.
 \tag{5.1}
\]

The inner singular kernel is used only in \(L^1\). At \(r=r_N\), (4.9) bounds the outer first moment by \(\sqrt{C_V/2}\,u_N\), and (5.1) bounds the inner one by \(C_\tau u_N\). Thus the root constant
\[
 C=\sqrt{C_V/2}+C_\tau
 \tag{5.2}
\]
is valid independently of any limiting temperature hypothesis.

The supplement proves a more general upper estimate without needing positivity on its entire fixed local ball. Its explicit heat prefactor equals
\(4^{(d-s)/2}\pi^{d/2}/\Gamma(s/2)\), as in the prior reviewed normalization. In its remainder bound (2.11):

- The constant subtraction on \(0<t<1\) contributes \(1/\tau\), with \(\tau=(d-s)/2\).
- The Gaussian images satisfy \(|x+n|\ge3|n|/4\) on \(|x|\le1/4\), giving the displayed exponent \(9|n|^2/(64t)\) for the undifferentiated remainder.
- The large-time torus part is bounded by its absolute nonzero Fourier sum.
- The Euclidean large-time integral is bounded by \((4\pi)^{-d/2}2/s\).

These are exactly the four terms of its finite \(M_{d,s}\). The derivative bounds in (2.9)–(2.10) justify smoothness and boundedness of the local remainder; all time weights are integrable. The finite outer-region integral \(G_{d,s}\) is an explicitly defined quantity of the fixed kernel, not an unstated uniform norm in another parameter.

With \(r_0=1/4\), \(\omega_{d-1}=dv_d\), and the notation of the supplement, polar integration gives

\[
 D(r):=\int_{\{\operatorname{dist}<r\}}|g|
 \le C_1r^{d-s},\qquad
 C_1=\frac{\omega_{d-1}}{d-s}+M_{d,s}v_dr_0^s.
 \tag{5.3}
\]

The squared outer norm is bounded by
\(K_0+2\omega_{d-1}\int_r^{r_0}t^{d-1-2s}dt\),
where \(K_0=G_{d,s}+2M_{d,s}^2v_dr_0^d\).
For \(q=2s-d>0\), \(r\le r_0\) gives

\[
 \|g_r\|_2^2\le C_2r^{-q},\qquad
 C_2=K_0r_0^q+\frac{2\omega_{d-1}}q.
 \tag{5.4}
\]

The factor \(r_0^q\) is in the correct direction because
\(K_0\le K_0r_0^q r^{-q}\).

Let \(H_r=g_r-m_r\) be the centered outer kernel and
\(J_r=g\mathbf1_{\{\operatorname{dist}<r\}}+m_r\) the centered inner kernel. Their sum is \(g\), and both have zero mean. For the general signed inner part,
\(\|J_r\|_1\le2D(r)\).
The exact centered-inner estimate is

\[
 \mathbb E|P_N[J_r]|
 \le\frac{N-1}{2N}\|J_r\|_1
 \le\frac{N-1}{N}D(r).
 \tag{5.5}
\]

There is no replacement of this centering by the uncentered discarded sum. Combining (5.5) with the canonical outer variance and then enlarging the finite-\(N\) factors gives exactly the supplement's (7.3):

\[
 \mathbb E|\sigma_NP_N[g]|
 \le\sqrt{\frac{b_N}{2N}}\|g_r\|_2
       +\sqrt{Nb_N}\,D(r).
 \tag{5.6}
\]

This is a global \(L^1\) decomposition. It does not require a no-close-pair event or a conditional variance.

For \(s>d/2\), taking \(r=N^{-2/d}\) in (5.3)–(5.6) proves

\[
 \mathbb E|\sigma_NP_N[g]|
 \le\left(\sqrt{C_2/2}+C_1\right)
       \sqrt{b_N}\,N^{2s/d-3/2}.
 \tag{5.7}
\]

At \(s=d/2\), the same radius gives
\(\|g_r\|_2^2\le K_0+(4\omega_{d-1}/d)\log N\), after dropping the nonpositive \(\log r_0\) term. The inner part contributes at most \(C_1\sqrt{b_N/N}\). Hence the submitted choice

\[
 C_d=\sqrt{K_0/2+2\omega_{d-1}/d}+C_1
 \tag{5.8}
\]

indeed bounds the total by
\(C_d\sqrt{b_N(1+\log N)/N}\).
The same symbol used earlier in the supplement for a different probability bound is explicitly assigned a separate value; the constants are not conflated.

For \(s<d/2\), the exact finite second moment gives the first-moment constant \(\|g\|_2/\sqrt2\) multiplying \(\sqrt{b_N/N}\). No truncation is needed. The radius used in the other two cases is at most \(r_0\) for every integer
\(N\ge r_0^{-d/2}=2^d\), exactly the submitted threshold. All constants depend only on the fixed \(d,s\), with no asserted uniformity as the exponent approaches a threshold.

These calculations establish the THM-018 upper rates independently of the root lower-bound argument. The supplement itself neither claims nor supplies the new probability converse.

## 6. Necessity, equivalence of modes, and tightness

For \(d/2<s<d\), put
\(A_N=b_NN^{4s/d-3}\).
The exact scaling relation is

\[
 \sigma_Nu_N=\sqrt{A_N}.
 \tag{6.1}
\]

The reviewed bounds therefore imply, uniformly for \(N\ge N_0\),

\[
 ap\sqrt{A_N}\le\mathbb E|\sigma_NP_N[g]|
       \le C\sqrt{A_N},\qquad
 \mathbb P(\sigma_NP_N[g]\ge a\sqrt{A_N})\ge p.
 \tag{6.2}
\]

If \(A_N\to0\), the upper moment bound proves \(L^1\) convergence and hence probability convergence to zero. If \(A_N\not\to0\), there are \(\epsilon>0\) and indices \(N_j\to\infty\) with \(A_{N_j}\ge\epsilon\). The lower event then has probability at least \(p\) and exceeds the fixed positive threshold \(a\sqrt{\epsilon}/2\). Probability convergence to zero is impossible. The same moment lower bound directly rules out \(L^1\) convergence. Thus the two convergence modes are equivalent here through the quantitative criterion, without invoking a general implication from probability convergence to \(L^1\) convergence or assuming uniform integrability.

If \(A_N\) is bounded, the upper moments in (6.2) are uniformly bounded for all large \(N\). The finitely many earlier random variables are integrable, so their absolute moments have a finite maximum as well. Markov proves tightness of the whole real-valued sequence.

If \(A_N\) is unbounded, choose increasing indices \(N_j\) with \(A_{N_j}\ge j^2\). This is possible after discarding any finite initial set, since each individual value is finite. For every fixed \(L>0\), eventually \(a\sqrt{A_{N_j}}>L\), and the tail probability at \(L\) is at least \(p\). Taking any desired tightness error less than \(p\) proves non-tightness. This is a probability argument using (6.2), not a variance argument.

**Local precision note SH-01.** Root proof line 118 says that if \(A_N\) is unbounded along a subsequence, the lower threshold eventually exceeds every fixed \(L\) along that subsequence. A merely unbounded subsequence can oscillate, so the word “eventually” requires the further extraction just given. For an admissible example of the distinction, take \(s=7d/8\), \(\beta_N=1\) for odd \(N\), and \(\beta_N=N^{-1/2}\) for even \(N\). Then \(A_N=\sqrt N\) on odd indices and \(A_N=1\) on even indices. The entire sequence is unbounded but does not eventually exceed \(2\). Extracting the odd indices proves precisely the intended non-tightness conclusion.

Severity: minor quantified proof clarification, with exact confidence. The theorem's unboundedness-to-non-tightness assertion survives unchanged; no extra assumption, constant, rate, or input is needed. The original candidate text is preserved, and this audit states the extraction explicitly rather than silently changing the meaning of “unbounded.”

At \(b_N=1\), \(A_N\) tends to zero for \(s<3d/4\), equals one at \(s=3d/4\), and tends to infinity above it. Accordingly the claimed fixed-scale vanishing, tightness with nonvanishing, and non-tightness follow. “Nonvanishing” at equality means failure to converge to zero in probability; no particular limiting distribution or convergence of the full sequence in law is identified. The smaller-exponent \(L^1\) bounds are supplied by THM-018, separately reviewed above.

## 7. Exact support, preserved artifacts, and remaining scope

The reviewer wrote VERIFICATION_CODE/round003_sharp_hostile_exact.py from scratch in this worktree, without reading either submitted worker's code. Its saved output reports **PASS, 31,194 exact checks**, using only standard-library integer and Fraction arithmetic.

The finite tests include:

- Exhaustive cyclic Haar configurations through \(N=5\), checking the close-pair count's exact first and second moments, its positive-probability bound, shared-label indicator independence, and an explicit failure of mutual triangle independence.
- The global centered inner/outer identity, the finite-\(N\) positive-inner decomposition, exact outer variance, exact centered-inner first-moment coefficient, and the unconditional absolute-moment bound, including a signed inner kernel.
- Compatible rational fixed-\(\delta\) choices for many positive constants and rational exponents, the exact \(32\), \(64\), \(1/8\), \(c_0\) factors, the finite-\(N\) count interval, and all power identities in the lower and upper estimates.
- The logarithmic-endpoint constant majorant and the radius threshold.

Finite cyclic Haar examples test algebra and indicator conditioning, not the continuous singularity or asymptotic Riesz theorem. Rational proxy volumes test the constant algebra; the analytic proof above covers the actual Euclidean volume. No numerical simulation, tolerance, Poisson limit, extreme-value theorem, stable law, or probabilistic asymptotic is inferred from these tests.

| New supporting artifact | SHA-256 |
|---|---|
| VERIFICATION_CODE/round003_sharp_hostile_exact.py | a5f6d79c9bfc7243397b407aa1173c1d935beca80e169fd40360e37e5762a36b |
| VERIFICATION_CODE/round003_sharp_hostile_exact_output.json | f96667198985a756b0451ca7a2bbb4a81d0f35d2a4d502402824972c7ec6375f |

Verification: the sharp-input and supplemental manifests passed before and after review; the original Round 003 manifests and the TASK-023 review hash remain valid; the exact checker passed; python3 scripts/verify_campaign.py and git diff --check passed; the new artifacts passed control-character, terminal-newline and trailing-whitespace checks. The campaign verification is structural evidence, not a mathematical certificate.

Only this review and its two supporting artifacts were created for TASK-026. No candidate, submitted proof, earlier report, previous code/output, canonical ledger or TeX source was edited. No commit, push, installation, remote mutation or child worker was used.

The sharp result resolves the vanishing criterion for the stated bare initial iid pair in \(d/2<s<d\), and THM-018 supplies the upper first-moment rates over \(0<s<d\). It does not determine the actual backward kernel's singularity, establish any dependent-law estimate, or compare singular and regularized dynamics. Those separate load-bearing questions are unchanged.
