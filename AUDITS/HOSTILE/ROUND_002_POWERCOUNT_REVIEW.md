# Hostile review of THM-012: all-order moments and cutoff criteria

Date: 2026-09-17 UTC. Task: TASK-018. Reviewer: /root/r002_falsification, gpt-6-astra Max. Worktree: /private/tmp/hocf-round002-falsification-20260917. Commit: a06178658d1e3d458536ff312ca793947212ec67.

## 1. Verdict and actual independence

**One narrow scope correction is required before an unqualified pass.** The compact exact rooted-gradient identity in the submitted report requires symmetric kernels, but the report/card do not state that restriction globally before invoking it. An explicit unused-slot kernel disproves the unrestricted identity. The frozen symmetric-corrector interpretation is correct, and every reviewed quantitative inequality, partition coefficient, heat estimate, and conditional cutoff conclusion passes in that interpretation.

Audit disposition:

- **HOSTILE_REVIEW_FAIL AS UNRESTRICTED WORDING** for the exact first-slot derivative/martingale identity in Section 5, and hence for a reading of the card that includes nonsymmetric kernels in that identity.
- **HOSTILE_REVIEW_PASS** for the partition conversion and moment inequalities for arbitrary deterministic smooth kernels, subject to the stated norms.
- **HOSTILE_REVIEW_PASS** for the rooted derivative, bracket, generator, and summability claims in the frozen symmetric-kernel scope.
- **HOSTILE_REVIEW_PASS** for the stated heat derivative bounds, nonuniformity of this coupling constant, and conditional slow-cutoff conclusions about the regularized model itself.

The needed correction is a symmetry/symmetrization statement, not a new estimate. Section 3 below records it separately; no submitted byte has been changed. Root should attach an explicit scope addendum before giving the submitted theorem an unqualified audit status.

This reviewer did not participate in the THM-012 all-order construction or its code. The reviewer previously independently constructed fixed-order residual estimates, then constructed the Gaussian criterion and viscosity-continuity report. Those roles are disclosed: this is a hostile review in an existing mathematical context, **not** a fresh-session or blind reconstruction. The viscosity report was sealed before the present dossier was opened. No child worker was used.

## 2. Hashed inputs and scope of review

The supplied manifest was verified before reading the dossier: all four entries passed. Manifest SHA-256:
27b538d69f2ffbf533e16404adb7f1d0d64ae46037e49a5e755345ae06db3af7.

| Input | SHA-256 |
|---|---|
| TASKS/ACTIVE/TASK-018_ROUND002_POWERCOUNT_REVIEW.md | c1c23e7519984f018d0bce1491d92fc560e6f64a990a74df395915f296b2bb93 |
| THEOREMS/THM-012_SMOOTH_ORDER_AND_CUTOFF.md | 93e889a841d66d3554d0236840f87d73d4f240166da6978d5018bbb77cd5e296 |
| MEMORANDA/ROUND_002_POWERCOUNT.md | f0bd6a670b194767afa2fe75f259d59bfe4589433f21252992d1dde79c92f01d |
| MEMORANDA/ROUND_002_COUPLING.md | 7eb57c1f4e8f6da9c80a2f53a95349153605467532afb33b269938b242761852 |

The frozen recursion definitions were also checked against MEMORANDA/ROUND_001_RECURSION.md, SHA-256 bb6aeaa44c91cac7c5f1c0a0fc8199cc00cffb6ca23ee823df79167d0c650aae, and its symmetric-kernel theorem card, SHA-256 ff9e1e8dc08b48dbfe6c96b3d760a208ab30f85b69ba21beef7ffcef39e40264. This review does not reissue an independent proof audit of that entire older generator theorem; it checks that the operators and coefficients used here match it.

The exact assertion audited is the conjunction of the finite-order partition/moment/bracket bounds and the separately conditional summability/cutoff criteria, with their displayed constants. Its negation is one admissible instance violating a displayed formula or estimate, or a missing hypothesis required by one of those claims. The symmetry omission is such a missing hypothesis for the compact exact first-slot formula. No counterexample was found to the inequalities or to the symmetric-corrector statement.

The source preflight is limited and sufficient: the Riesz Fourier sequence is an explicit definition in the frozen model, so the heat bounds are elementary estimates of that specified sequence. No source theorem about singular dynamics, local equilibrium, or critical behavior is imported.

## 3. Required scope correction: exact rooted identity

**Local finding PC-01** (this label is local to the audit, not a newly allocated canonical obstruction identifier).

- Location: submitted power-counting report lines 396–403, the compact derivative statement and equation (5.5); relevant card wording is its reference to (5.1)–(5.6).
- Diagnosis: the factor \(k\) times the first-slot derivative requires symmetry. The report's early general statements and Section 5 do not explicitly restrict \(\Phi\) to symmetric kernels. Symmetry is first explicit for the concrete family in Section 7. The older frozen recursion has that assumption, but the new unrestricted wording needs to preserve it visibly.
- Severity: a local, required hypothesis/scope correction. It does not invalidate the intended symmetric-corrector theorem or force larger constants.
- Confidence: exact.

For a counterexample to the unrestricted identity, take \(k=2\), any smooth nonconstant periodic \(h\), and

\[
 \Phi(x,y)=h(y).
\]

For every probability background and every configuration, the original deleted-label definition gives

\[
 U_2[\Phi]
 =\frac{N-1}{N}\eta(h)-\mu(h)-\eta(h)+\mu(h)
 =-\frac{\eta(h)}N.
 \tag{3.1}
\]

Therefore

\[
 \nabla_{x_i}U_2[\Phi]=-\frac{\nabla h(x_i)}{N^2},
 \qquad
 \frac2N V_1^{(i)}[\nabla_1\Phi(x_i,\cdot)]=0.
 \tag{3.2}
\]

For example \(h(x)=\cos(2\pi x)\) and \(x_i=1/4\) make the first expression nonzero. This test uses an unused first slot and is valid with the smooth Haar background; it is not based on an inadmissible initial particle law.

**Corrected sufficient statement, separately from the submitted text.** Either restrict the compact identity and generator applications to deterministic symmetric kernels, as in frozen THM-001, or replace their first-slot kernel by its averaged symmetrization:

\[
 \nabla_{x_i}U_k[\Phi]
 =\frac{k}{N}V_{k-1}^{(i)}
       [\nabla_1(\operatorname{Sym}_k\Phi)(x_i,\cdot)].
 \tag{3.3}
\]

The statistic satisfies \(U_k[\Phi]=U_k[\operatorname{Sym}_k\Phi]\), and averaged symmetrization does not increase any of the stated maximum \(C^m\) norms. Thus all quantitative bounds retain the submitted constants. In the example, \(\operatorname{Sym}_2\Phi=(h(x)+h(y))/2\); its rooted formula gives exactly the left side of (3.2). The partition identity itself does not require symmetry and passes for nonsymmetric kernels as written.

No other correction to a displayed coefficient or exponent was found. No submitted report or card has been edited by this reviewer.

## 4. Per-result analytic findings

| Result | Verdict | Decisive check |
|---|---|---|
| All-\(p\) Hilbert empirical estimate, (2.3)–(2.7) | PASS | Symmetrization and the even-multiplicity coefficient comparison prove the stated double-factorial constant; the existing coupling is pathwise and temperature-free. |
| Exact partition formula, (3.2) | PASS, including nonsymmetric kernels | Partition Möbius weights select exactly injective labels; background singleton choices sum to \(\rho\). |
| Norm conversion and order constants, (4.1)–(4.8) | PASS | Only singleton variables are differentiated; cycle multiplicities and powers of \(N\) are exact. |
| Iid preparation biases, (4.10)–(4.11) | PASS | The generating function and its leading even/odd powers agree with the deleted definition. |
| Root-excluded moments, (5.1)–(5.4) | PASS | The remaining empirical measure has mass \(1-1/N\); the missing root is retained in \(\rho^{(i)}\). |
| Compact rooted derivative/noise formula, (5.5) | PASS for symmetric kernels; FAIL without that hypothesis | Counterexample (3.1)–(3.2); correction (3.3). |
| All brackets, (5.6) | PASS in frozen symmetric scope; same inequalities survive symmetrization | Independent Brownian covariance plus the rooted \(L^2\) estimate gives the exact exponent. |
| Generator norms and power table, Section 6 | PASS in the inherited symmetric recursion scope | All four coefficients match frozen R1; no extra small factor is assigned to the double contraction. |
| General series criteria and concrete factorial lemma, Section 7 | PASS with stated additional premises | Absolute \(L^1\) and integrand-\(L^2\) majorants justify their respective sums; no actual hierarchy normalization is assumed. |
| Heat upper and lower derivative bounds, Section 8 | PASS | Dyadic integration preserves every \(2\pi\), derivative-order, gamma, and cutoff exponent. |
| Slow-cutoff criterion and diagonal choice, Section 9 | PASS for the regularized model only | Fixed-order constants are polynomial in the coupling constant; the logarithmic condition makes them \(N^{o(1)}\). |
| Claimed exclusions, Section 10 | PASS | No singular-model comparison, critical closure, or infinite-order cutoff result is claimed. |

### 4.1. Hilbert moments and actual-law transfer

The proof of the new moment estimate has no Gaussian assumption. Conditional Jensen symmetrizes the centered empirical sum. For deterministic Hilbert vectors, expand the \(m\)-th power of the squared norm and average the independent signs. Terms with any odd index multiplicity disappear. Bounding each surviving inner product by the product of norms yields the scalar sign moment, and

\[
 (2a)!\ge 2^a a!
\]

gives the coefficientwise bound by
\((2m-1)!!(\sum_i\|z_i\|^2)^m\). Since each difference of Dirac vectors has norm at most \(2B\), (2.6) follows with precisely its stated power of \(N\). Taking \(m=\lceil p/2\rceil\) covers every real \(p\ge1\), with monotone \(R_p\).

The prerequisite coupling was checked at its used lines: the same Brownian paths cancel; the full empirical force equals the deleted one because \(K(0)=0\); the drift comparison involves \(d(v_1+2\kappa_1)\); and the Hilbert Dirac displacement bound uses \(D\). Minkowski integrates pointwise-in-time iid moments, without replacing them by a temporal supremum moment. The resulting multiplier is exactly \(S=1+D\mathcal K h_L(T)\). This also applies at arbitrarily high temperature. No exchangeability-to-independence inference for the interacting particles occurs.

### 4.2. Partition weights, traces, and biases

The signed weight of a block of size \(r\) is \((-1)^{r-1}(r-1)!\). Summing products of these weights over refinements of an equality block yields the signed permutation sum. A transposition reverses permutation sign when the block has size at least two, so the sum is zero there and one for a singleton. This proves the injective-label indicator. Combining occupied singleton choices with unoccupied background choices gives \(\eta-\mu=\rho\); nonsingleton blocks remain integrated against \(\eta\). The formula is configuration-wise, including repeated coordinates and \(k>N\).

For a partition with \(j\) singleton blocks and \(\ell\) other blocks, the power is

\[
 N^{-(k-j-\ell)}N^{-j/2}
 =N^{-k/2-\frac12\sum_{|A|\ge2}(|A|-2)}.
 \tag{4.1}
\]

This recomputes the exponent in (4.2). A pair block has no additional gain. In the Fourier duality, each singleton variable is an original unrepeated slot. Holding the repeated-block variables fixed means no derivative lands on a diagonal substitution, so no missing block-size chain-rule factor is present. Integrating the resulting uniform bound against the positive probability measures \(\eta\) does not require independence.

For a cycle type \((m_1,\ldots,m_k)\), the number of partitions times its unsigned cycle weight is

\[
 \frac{k!}{m_1!\prod_{r\ge2}m_r!r^{m_r}}.
 \tag{4.2}
\]

This gives exactly (4.6). At a fixed singleton weight \(A\), the two generating functions in (4.7)–(4.8) follow respectively from
\(\exp(Az+\sum_{r\ge2}z^r/r)\) and
\(\exp(Az+\sum_{r\ge2}z^rN^{-(r-2)/2}/r)\). They are coefficient identities, not convergence claims. The inequality \(A\ge1\) used to compare the truncated exponential is valid because \(B\ge1\), \(S\ge1\), and \(Q\ge1\).

Direct iid expectation produces
\(e^{-z}(1+z/N)^N\). Expanding its logarithm gives the negative quadratic term and positive cubic term; the leading even bias uses only pairs, and the leading odd bias uses one triple plus pairs. This confirms both signs and the factorial in (4.11). These are initial-law identities, not evolved iid assertions.

### 4.3. Rooted brackets and all four drift rows

The root-deleted measures satisfy
\(\eta^{(i)}(1)=1-1/N\) and
\(\rho^{(i)}(1)=-1/N\). In particular they cannot be replaced by a normalized empirical probability measure with \(N-1\) in the denominator. The submitted \(B/N\) correction in the negative norm is retained, giving (5.1). The partition proof applies unchanged to this subprobability measure; its total mass at most one suffices in the bounds.

For symmetric kernels, the \(k\) possible locations of the root give the exact gradient factor \(k/N\). A root-excluded statistic of order \(k-1\) has \(L^2\) size \(N^{-(k-1)/2}\). Thus the Brownian bracket calculation is

\[
 \frac{2\nu k\ell}{N^2}\cdot N\cdot
 N^{-(k-1)/2}N^{-(\ell-1)/2}
 =2\nu k\ell N^{-(k+\ell)/2},
 \tag{4.3}
\]

before inserting the displayed \(d,T\), kernel, and partition constants. This checks the raw exponent, including \(k=1\), and retains all cross terms. Multiplication by \(\sigma_N^2\) changes \(\nu N^{-(k+\ell)/2}\) to
\(\min(1,\beta^{-1})N^{1-(k+\ell)/2}\), with no additional temperature restriction.

The generator kernels and coefficients reproduce frozen R1. The derivative norms in (6.2) follow from the number of interaction terms and the \(2^m\) Leibniz sum. In \(R_k\), derivatives in the remaining slots never hit \(K(y-z)\), explaining the use of \(\kappa_0\) in that bound. The raw statistical orders of the four rows are

\[
 N^{-(k+1)/2},\quad N^{-(k+2)/2},\quad
 N^{-(k+1)/2},\quad N^{-k/2},
 \tag{4.4}
\]

respectively. The double contraction is the same order as level \(k\), and the report does not mislabel it as another small factor. At \(P=U_2/2\), the martingale and bracket divisions stated in the report are correct.

### 4.4. Infinite sums are separately qualified

The statistic criterion is an absolute \(L^1\) majorant, uniform over the displayed deterministic time supremum. The martingale criterion is the sum of norms of the Brownian integrands in the joint time/probability Hilbert space; its square-integrable limit retains cross variations. It is not a sum of diagonal brackets alone.

For the explicitly additional hypothesis
\(\|\Phi_{N,k,t}\|_{C^{kq+1}}\le Ab^k\) with coefficients \(1/k!\), both relevant order constants are bounded by \(e^{c\sqrt k}\) after division by the appropriate factorial. The elementary inequality
\(c\sqrt k\le\delta k+c^2/(4\delta)\) yields the geometric majorant with ratio \(be^\delta/\sqrt N\). Its tail is exactly the series in (7.6), of order \(N^{-K/2}\) for fixed \(K\). To obtain the whole martingale bound one still multiplies that series by the prefactor in (7.3).

This does not establish the actual hierarchy's coefficient normalization, its geometric kernel growth, or summability of its drift series. Those exclusions are explicit in the submission. No limit or infinite sum is exchanged without the displayed absolute majorant. Any future full infinite identity must also control its remaining drift/principal terms or prove their exact cancellation; the present model lemma does not assert such an identity.

### 4.5. Heat constants and slow cutoffs

A derivative of order \(j\) of \(K_\epsilon\) contributes
\((2\pi)^{j+1}|n|^{s-d+j+1}\). On a dyadic annulus the lattice count is bounded by \(5^d2^{d\ell}\), producing the power \(p=s+j+1>0\). The integral comparison on \([2^{\ell-1},2^\ell]\) yields precisely

\[
 \sum_{\ell\ge0}2^{p\ell}e^{-4\pi^2\epsilon4^\ell}
 \le\frac{\Gamma(1+p/2)}{1-2^{-p}}
          (4\pi^2\epsilon)^{-p/2}.
 \tag{4.5}
\]

The combined \(2\pi\) factor is \((2\pi)^{-s}\), not a derivative-order-dependent omitted factor. Maximizing over \(j\le m\), using \(\epsilon\le1\), gives exactly the stated \(L_m^{\rm heat}\) and exponent \((s+m+1)/2\).

For the lower bound, the positive sum for \(\operatorname{div}K_\epsilon(0)\) can be restricted to the stated positive-coordinate box. Its count contributes \(R^d/2^d\), its power contributes \(R^{s-d+2}\) times the stated minimum of the two endpoint constants, and the heat factor is at least \(e^{-16\pi^2d}\). Since \(R=\epsilon^{-1/2}\), the exponent is \((s+2)/2\). Dividing the divergence by \(d\) is justified by the maximum componentwise derivative norm. This verifies \(c_*\), including both signs of \(s-d+2\).

The actual explicit coupling constant \(S_\epsilon\) is consequently not uniform: \(h_L(T)\) is increasing in \(L\), the Lipschitz lower bound makes \(L\) of order at least \(\epsilon^{-(s+2)/2}\), and one nonzero Fourier mode bounds \(\mathcal K_\epsilon\) below. For \(T>0\), the polynomial factor can be absorbed into a smaller positive exponential. This is a statement about this proof constant, not a lower bound on a residual.

For a fixed finite order, the exact partition constants are polynomials in \(S_\epsilon\), with order-dependent finite coefficients. Under (9.2), \(\log S_{\epsilon_N}=o(\log N)\), all required actual test norms have the same subpolynomial growth property, and the negative powers of \(N\) in the residual bounds therefore win. The report correctly avoids using the coarser \(e^{C S_\epsilon\sqrt k}\) majorant in this fixed-order cutoff argument.

The logarithmic-cutoff interpretations and the diagonal construction are valid with the stated uniform fixed-cutoff envelopes. Pointwise finiteness for each \(N,\beta\) would not suffice, and the report explicitly excludes that weaker premise. No estimate compares a regularized particle/reference pair with a singular pair. Equation (10.1) is correctly retained as a separate unproved model-comparison obligation. Neither microscopic critical scaling nor arbitrary slowly subcritical coupling is inferred from these smooth constants.

## 5. Independent exact tests and verification

The reviewer wrote VERIFICATION_CODE/round002_powercount_hostile_exact.py without reading or running the constructor's code. Its SHA-256 is 461f705b9814e2dad5285e0269e99c5e0d76707f5fdb583a20755f2d39379bf9.

Executed result: **PASS: 1,110 independent exact rational checks**. The test battery covers:

- Direct occupied-subset/injective-label sums against a separate partition evaluation through order seven, with \(N=2,3,4\), repeated coordinates, \(k>N\), constant kernels, genuinely unused slots, and a nonuniform finite background.
- The same conversion with the root excluded but denominator still \(N\), and direct particle differentiation versus the compact symmetric rooted formula through order five.
- Cycle-type grouping and the finite generating-function coefficients through order eight.
- Iid bias coefficients through order twelve.
- Hilbert sign-moment comparisons through degree sixteen, using vectors with both positive and negative pairwise inner products.
- Temperature/bracket powers for every pair of orders one through eight and several exact positive rational inverse temperatures.
- The nonsymmetric counterexample (3.2) and its symmetrized repair.

The finite-background and quarter-circle value/derivative tables are tests of the exact algebra; they are not presented as the smooth stochastic model's background law. The analytic proof above addresses the universal identities and estimates. The counterexample itself uses a genuinely smooth periodic kernel and may use the smooth Haar background.

Arithmetic is standard-library integer/Fraction arithmetic under Python 3.9.6. No random seed, tolerance, numerical enclosure, new dependency, or external theorem is involved. These finite tests are independent supporting computation, not a certificate of all quantifiers.

Commands: shasum -a 256 -c AUDITS/ROUND_002_POWERCOUNT_INPUT_SHA256SUMS.txt; python3 VERIFICATION_CODE/round002_powercount_hostile_exact.py; python3 scripts/verify_campaign.py; git diff --check; and final hash/control-character checks. The submitted dossier and all earlier worker proofs are preserved. No canonical ledger, theorem card, prior memorandum, or prior audit has been changed.

## 6. Required disposition

Attach an explicit symmetry/symmetrization scope addendum for Section 5 and the corresponding card language. The exact correction is (3.3), or the narrower declaration that those identities are for the symmetric kernels of frozen THM-001. Preserve the submitted report's bytes. Once that local scope correction is present, no further load-bearing defect was identified by this hostile review of THM-012.

The result remains a smooth iid moment theorem and a set of sufficient conditional series/cutoff criteria. It does not close the singular power-counting gate, establish actual corrector summability, identify a singular critical law, or prove singular-model comparison. No approval for a whole M2/M3 promotion or publication follows from this review.
