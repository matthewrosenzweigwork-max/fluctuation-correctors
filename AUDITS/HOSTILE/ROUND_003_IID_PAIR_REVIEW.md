# Hostile review of the Round 003 initial iid pair interface

Date: 2026-09-17 UTC. Task: TASK-023. Reviewer: /root/r002_falsification, gpt-6-astra Max. Worktree: /private/tmp/hocf-round003-hostile-20260917. Reviewed checkout: 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2.

## 1. Verdict and scope

**HOSTILE_REVIEW_PASS for THM-015 and THM-016, supported by both complete submitted proofs.** No coefficient, normalization, missing hypothesis, or invalid limiting argument requiring a candidate repair was found. The exact iid projection identity, sharp universal second-moment bound, heat-cutoff orders, infinite unregularized second moment, and the stated sufficient probability limits all pass in their declared scopes.

This review does not convert the sufficient probability condition into a converse or a sharp threshold. At fixed square-root particle scaling the submitted argument proves probability convergence below \(s=3d/4\), including \(2s=d\), but does not determine the unregularized probability limit at or above \(s=3d/4\). Its temperature-dependent sufficient conclusion in that larger range is valid. Nonvanishing or divergent second moments have not been used to claim nonconvergence in probability.

All conclusions concern initial iid preparation. The Haar bare-potential diagnostic is not identified with the actual backward corrector, and no positive-time interacting law, Gibbs law, singular dynamic comparison, or full campaign fluctuation theorem is promoted.

The exact assertion reviewed is the conjunction of the finite-particle identities and bounds, specified two-sided cutoff comparisons, and stated sufficient probability conclusions in the two cards. Its logical negation is one admissible input violating a displayed conclusion, or an omitted hypothesis needed for that conclusion. The tests and analytic reconstruction below found neither. Finite tests support the review; the analytic arguments, not a passing test count, establish the universal conclusions.

## 2. Inputs, source preflight, and actual independence

The initial manifest was verified before opening its mathematical dossier. The supplemental manifest was verified before opening the complete constructor proof. All listed inputs passed, and were rechecked after this review was written.

| Exact input | SHA-256 |
|---|---|
| TASKS/ACTIVE/TASK-023_ROUND003_HOSTILE.md | 6f244b2991fe29d5c9cc9908aee55e9141f1081609a0c68f0fa96d7a2f324da8 |
| THEOREMS/THM-015_IID_PAIR_SECOND_MOMENT.md | c61e042599bd18993b6b760f22bde9d9044675f206fb42ea3418197be36db150 |
| THEOREMS/THM-016_IID_RIESZ_PROBABILITY_TRUNCATION.md | 75e94300f0117f9cb4599e626f25834900ee418a85628b504e71cdb9118018d1 |
| MEMORANDA/ROUND_003_COLLISION_FALSIFICATION.md | 9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4 |
| MEMORANDA/ROUND_003_IID_PAIR.md | 68ed536685133906877efe7599f1e93300e796ad0b62bb6b228837df08438d5a |
| TASKS/ACTIVE/ROUND_001_MODEL.md | 3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57 |

Initial manifest SHA-256: bf4125f8ab66ef8304ac2c968f79134142df596fb9a22a0f829fe8f98ec44371. Supplemental manifest SHA-256: ee89bb6cbcda6f6e69f704059e5e642b88b237371a1bf893dc4a45a66432c4a1.

For concise source locations below, “pair report” means ROUND_003_IID_PAIR.md and “collision report” means ROUND_003_COLLISION_FALSIFICATION.md, always the exact bytes above. Their own starting worktrees used a06178658d1e3d458536ff312ca793947212ec67. The reviewed frozen model has the same hash as the model named in both constructions. The later published checkout used for this review does not change their mathematical input normalization.

This reviewer did not construct either Round 003 candidate. The context previously constructed a fixed-smooth residual argument, Gaussian criterion and viscosity-continuity result, and reviewed the separate all-order smooth estimates. This reuse is disclosed: the present audit is neither a fresh session nor a blind reconstruction. The two complete proof narratives were read as audit inputs. Neither worker's other worktree or computational code was inspected or run. The reviewer wrote separate exact checks after deriving the identities. No child worker was used.

The source preflight uses the frozen Fourier coefficient, torus convention, denominator and fluctuation scale directly. The heat representation, its leading real-space coefficient, and the probability bounds are proved from those definitions. No remembered source theorem, outside citation, novelty assertion, singular stochastic identity, or private manuscript input is load bearing.

## 3. Per-result dispositions

| Claim and source location | Verdict | Decisive point |
|---|---|---|
| General iid projection decomposition; pair (2.4)–(2.6), collision (1.2) | PASS | The finite-particle first projection is retained with coefficient \(-N^{-2}\); the mean is \(-\theta/(2N)\). |
| Exact variance and second moment; pair (2.7)–(2.8), collision (1.4)–(1.5) | PASS | Orthogonality leaves exactly \(N\) first-level terms and \(N(N-1)/2\) canonical unordered pairs. |
| Sharp second-moment constant and equality scope; pair (2.9)–(2.10), collision (1.6) | PASS | Equality holds for all kernels at \(N=2\), and precisely canonical kernels for \(N>2\); universal sharpness is distinct from optimality on a one-point space. |
| Product-null representatives and spatial versus label diagonals; both Section 1 | PASS | Distinct labels have product law. Coordinate-diagonal values matter at atoms and are not silently removed. |
| Real-space heat normalization and smooth local remainder; collision (3.1)–(3.5) | PASS | The heat integral has exactly the frozen Fourier coefficient and unit coefficient of \(|x|^{-s}\). All remainder derivatives have integrable time majorants. |
| Exact Haar heat norm and variance; pair (4.2)–(4.3), collision (4.2) | PASS | The squared multiplier is \(e^{-8\pi^2\epsilon|k|^2}\); both background projections vanish. |
| Explicit two-sided lattice constants; pair (5.1)–(5.12) | PASS | The max-norm shell bounds, negative radial power, integral comparisons and cutoff interval give the displayed constants. |
| Both polynomial cutoff rates and all-temperature factors; pair Section 6, THM-015 | PASS | The powers are \(2s/d-2\) and \(4s/d-3\) above the square-integrability threshold. Necessity concerns second moments only. |
| Integrable unregularized representative and infinite second moment; pair Section 7, collision Section 4, THM-016 | PASS | Both the conditional-expectation contradiction and the positive-part lower bound are valid without expanding infinite cross moments. |
| Fixed-particle cutoff convergence and limits of its quantitative use; pair (7.4)–(7.6), collision (4.5) | PASS | Fixed-\(N\) convergence in \(L^1\) does not supply an unstated fluctuation-scale joint rate. |
| Close-pair bound, discarded mean, centered variance; collision (5.1)–(5.6) | PASS | The shift is \((N-1)m_r/(2N)\), and Chebyshev uses the centered truncated canonical kernel. |
| Endpoint \(2s=d\) and strict range \(s<3d/4\); collision (6.1)–(6.3) | PASS | The displayed radii make all three obligations vanish, including the logarithmic variance at \(2s=d\). |
| Arbitrary temperature-sequence criterion; collision (6.4)–(6.6), THM-016 | PASS | The three radius substitutions are exact identities, not only power-sequence heuristics. |
| Limitation of the particular truncation method at fixed scale; collision end of Section 6 | PASS | Vanishing of its union-bound majorant forces a radius whose centered truncated variance diverges at and above \(3d/4\). This is not an unregularized nonconvergence theorem. |
| Actual-corrector and dynamic exclusions; pair Section 8, collision Section 7, both cards | PASS | The kernel norm, law, and positive-time comparison remain separate obligations. |

No failing local defect identifier is needed. The scope qualifications recorded below are interpretations explicitly supported by the submitted proofs, not repairs to their mathematics.

## 4. Independent reconstruction of the iid coefficients and equality scope

Write the orthogonal decomposition

\[
 \Phi(x,y)=\theta+h(x)+h(y)+H(x,y),\qquad
 \mu(h)=0,\qquad \int H(x,y)\,\mu(dy)=0.
 \tag{4.1}
\]

Jensen and Fubini place all components in the indicated \(L^2\) spaces. Conditional zero means give their orthogonality and
\(\|\Phi\|_2^2=\theta^2+2\|h\|_2^2+\|H\|_2^2\).
The background term in the campaign statistic is \(-N^{-1}\sum_i(\theta+h(X_i))+\theta/2\). Each first projection occurs \(N-1\) times in the unordered empirical pair sum. Direct collection therefore yields

\[
 P_N=-\frac{\theta}{2N}
       -\frac1{N^2}\sum_i h(X_i)
       +\frac1{N^2}\sum_{i<j}H(X_i,X_j).
 \tag{4.2}
\]

The constant, first projection and canonical coefficients have thus been checked from the definition rather than inferred from a usual unbiased U-statistic normalization.

Conditioning on one particle leaves only its first-projection term. Conditioning on two particles also leaves their canonical pair term. This gives both conditional projection formulas in the pair report. Distinct canonical pairs with a shared label have zero covariance by conditioning on that label; disjoint pairs have zero covariance by independence. First-level and pair terms are orthogonal by the same conditioning. Cauchy--Schwarz makes every product in this finite calculation integrable. The resulting second moment is exactly

\[
 \mathbb E P_N^2
 =\frac{\theta^2}{4N^2}
   +\frac{\|h\|_2^2}{N^3}
   +\frac{N-1}{2N^3}\|H\|_2^2.
 \tag{4.3}
\]

A useful exact check of both the bound and its equality cases is the gap:

\[
 \frac{N-1}{2N^3}\|\Phi\|_2^2-\mathbb E P_N^2
 =\frac{N-2}{4N^3}\theta^2
    +\frac{N-2}{N^3}\|h\|_2^2.
 \tag{4.4}
\]

It is zero for every kernel at \(N=2\); for \(N>2\), it vanishes exactly when \(\theta=h=0\). A nonzero centered \(u\in L^2(\mu)\) produces the attaining symmetric canonical kernel \(u\otimes u\), whose product-space squared norm is \(\|u\|_2^4\); no fourth moment of \(u(X)\) is required.

The constant is sharp uniformly over the permitted probability laws and kernels. On a fixed law it is attained by a nonzero canonical kernel whenever that law supports a nonconstant \(L^2\) function. A one-point probability space has no such function, and its best nonzero-kernel constant for \(N>2\) is the smaller constant-kernel coefficient. The collision report states this exception; the card's “sharp” wording is valid as universal sharpness and must not be repurposed as optimality on every degenerate law.

For density inputs, the coordinate diagonal is product-null. For the general-law card, product-null representatives still give the same statistic almost surely, but the coordinate diagonal at atoms has positive product mass. Deleting equal particle labels never deletes collisions of distinct labels. No self-label trace is used. The collision report provides the general probability-law proof; the pair report proves the density specialization and its nondegenerate sharpness.

The constant kernel checks the nonzero bias; an additive centered kernel checks the otherwise easily missed first projection; a centered product kernel checks sharpness. An exact dependent-law witness also prevents an unsupported transfer: if all particles share the same centered sign and \(\Phi(x,y)=xy\), each marginal is unchanged but \(P_N=(N-1)/(2N)\). Iid orthogonality is indispensable.

## 5. Fourier normalization, heat representation, and cutoff constants

Let \(\tau=(d-s)/2\), and let \(p_t\) be the periodization of
\((4\pi t)^{-d/2}e^{-|x|^2/(4t)}\). Unfolding the unit cubes gives Fourier coefficients \(e^{-4\pi^2t|k|^2}\), including zero mode one. The collision report's prefactor is

\[
 A=\frac{4^\tau\pi^{d/2}}{\Gamma(s/2)}.
 \tag{5.1}
\]

For small times, \(\|p_t-1\|_1\le2\); for large times the nonzero Fourier modes and all their derivatives decay exponentially. Thus \(A\int_0^\infty t^{\tau-1}(p_t-1)\,dt\) converges in \(L^1\), has zero mean, and its nonzero Fourier coefficient is

\[
 \frac{A\Gamma(\tau)}{(4\pi^2|k|^2)^\tau}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}
       |k|^{s-d}.
 \tag{5.2}
\]

The pair report's prefactor \(c_{d,s}(4\pi^2)^\tau/\Gamma(\tau)\) equals exactly (5.1). There is no difference of normalization between the reports.

For the whole-space Gaussian, substituting \(u=|x|^2/(4t)\) gives

\[
 A(4\pi)^{-d/2}\int_0^\infty
              t^{-s/2-1}e^{-|x|^2/(4t)}\,dt=|x|^{-s}.
 \tag{5.3}
\]

The factors of four, pi and gamma cancel to one. As a normalization check, \(d=3,s=1\) gives \(c_{3,1}=1/\pi\), consistently with (5.2)–(5.3).

On \(|x|<1/3\), subtracting (5.3) leaves the nonzero Gaussian translates at small time, the integrable constant subtraction, and the large-time torus-minus-Euclidean remainder. For a nonzero lattice translate, \(|x+n|\ge(2/3)|n|\). Every fixed derivative of the sum is bounded by a finite negative power of \(t\) times \(e^{-c/t}\) on a smaller closed ball, and is integrable with the weight \(t^{\tau-1}\). At large time, the Euclidean zeroth-derivative integrand is bounded by \(Ct^{-s/2-1}\), and spatial derivatives improve its decay; the torus part decays exponentially. These bounds justify differentiation under the integral to every finite order, including at zero after subtraction. Hence

\[
 g(x)=|x|^{-s}+H(x),\qquad H\text{ smooth near zero}.
 \tag{5.4}
\]

Smoothness away from zero and the compact torus give a global lower bound. Polar integration of the positive principal term proves \(g\in L^p\) exactly when \(ps<d\), including logarithmic failure at equality. This proves the real-space claim used by THM-016 rather than assuming it from the Fourier label “Riesz.”

For the heat cutoff, the squared norm has the exact multiplier \(e^{-8\pi^2\epsilon|k|^2}\). The explicit constants in the pair report can be checked without a lattice asymptotic. Put \(q=2s-d\) and \(a=8\pi^2\). The shell \(|k|_\infty=n\) has exactly
\((2n+1)^d-(2n-1)^d\) points. Integration of \(d x^{d-1}\) over \([2n-1,2n+1]\) proves its bounds between \(2dn^{d-1}\) and \(2d3^{d-1}n^{d-1}\).
Because \(2s-2d<0\) and \(n\le|k|\le\sqrt d\,n\), both the radial power and heat factor are bounded in the correct direction. This gives precisely

\[
 A_-\sum_{n\ge1}n^{q-1}e^{-ad\epsilon n^2}
 \le V_\epsilon
 \le A_+\sum_{n\ge1}n^{q-1}e^{-a\epsilon n^2},
 \quad
 A_-=2dc_{d,s}^2d^{s-d},\quad
 A_+=2d3^{d-1}c_{d,s}^2.
 \tag{5.5}
\]

For \(q<0\), the integral test yields the upper constant \(1+1/(-q)\), and the \(2d\) Euclidean unit modes give the stated lower constant. Dominated convergence gives the finite positive limiting norm.

For \(q=0\), take \(R=(ad\epsilon)^{-1/2}\). The prescribed \(\epsilon_0=(ad)^{-2}\) ensures \(R\ge2\), \(a\epsilon<1\), and \(\log(1/\epsilon)\ge2\log(ad)\). The lower harmonic sum is at least \(e^{-1}\log R\), hence at least \(\log(1/\epsilon)/(4e)\). The decreasing-function upper integral is at most \(1+\frac12\log(1/(a\epsilon))+\frac12e^{-1}\), which is bounded by \(2\log(1/\epsilon)\) on that interval. Thus both constants in the pair report's (5.8) pass.

For \(q>0\), the interval \(R\le n\le2R\) contains at least \(R/2\) integers, has radial factor at least \(2^{\min(q-1,0)}R^{q-1}\), and heat factor at least \(e^{-4}\). This is the lower constant in (5.9). For the upper sum, on \(x\in[n,n+1]\),

\[
 n^{q-1}e^{-u n^2}
 \le 2^{(1-q)_+}x^{q-1}e^{-u x^2/4}.
 \tag{5.6}
\]

Integration gives
\(2^{\max(q-1,0)}\Gamma(q/2)u^{-q/2}\), exactly the coefficient in (5.10). Thus the explicit \(L_{d,s}\) and \(U_{d,s}\) in (5.12) are correct, as are all three two-sided orders of the squared norm. No uniformity across \(s=d/2\) or \(s=0,d\) is inferred from these fixed-\((d,s)\) constants.

## 6. Temperature factors, infinite variance, and cutoff passage

Haar translation invariance and zero mean make \(g_\epsilon(x-y)\) canonical. Substituting it in (4.3), and only then multiplying by \(\sigma_N^2=N b_N\), gives

\[
 \mathbb E(\sigma_NP_N[g_\epsilon])^2
 =\frac{b_N(N-1)}{2N^2}V_\epsilon,
 \qquad b_N=\min(\beta_N,1).
 \tag{6.1}
\]

The finite-\(N\) coefficient lies between \(b_N/(4N)\) and \(b_N/(2N)\). Therefore the necessary-and-sufficient conditions in the pair report's Section 6 are indeed conditions for vanishing of this second moment, uniformly over all positive temperature sequences.

When \(2s>d\), substituting \(\epsilon_N=N^{-2/d}\) yields \(b_NN^{2s/d-2}\), which tends to zero for all \(s<d\). Substituting \(\epsilon_N=N^{-4/d}\) yields \(b_NN^{4s/d-3}\). Below the square-integrability threshold the order is \(b_N/N\), and at the threshold it is \(b_N\log N/N\), up to the fixed cutoff exponent. In particular the second cutoff's \(s=3d/4\) second moment vanishes exactly when \(b_N\to0\); above that exponent its vanishing criterion forces \(\beta_N\to0\). These are not probability converses.

At microscopic critical coupling, \(s<d\) forces \(\beta_N\to\infty\), hence eventually \(b_N=1\). The report correctly uses that only to describe these initial cutoff second moments. Full subcritical coupling alone permits different physical-temperature limits and does not decide the second-cutoff criterion.

For the unregularized kernel, \(L^1\) suffices to define every finite deleted sum almost surely and to give expectation zero. The two submitted proofs of infinite second moment have different valid mechanisms:

1. The pair report first proves \(g\notin L^2\) from the nonsquare-summable Fourier coefficients when \(2s\ge d\). Since all remaining pair terms have conditional mean zero,
   \[
   \mathbb E[P_N[g]\mid X_1,X_2]=N^{-2}g(X_1-X_2).
   \tag{6.2}
   \]
   The conditional expectation exists in \(L^1\). If \(P_N[g]\) belonged to \(L^2\), conditional Jensen would put its right-hand side in \(L^2\), a contradiction.
2. The collision report uses \(g\ge-C\) and \(M=N(N-1)/2\) to obtain
   \[
   (P_N[g])_+\ge N^{-2}
          \big(g(X_1-X_2)-C(M-1)\big)_+.
   \tag{6.3}
   \]
   The positive local singularity makes the right-hand side have infinite second moment, including the logarithmic threshold.

Neither argument expands a sum of nonintegrable second-order cross terms. Every positive finite \(\sigma_N\) preserves the infinite second moment for a fixed \(N\). Also \(g-g_\epsilon\notin L^2\) for every positive fixed \(\epsilon\): otherwise adding the smooth cutoff would put \(g\) in \(L^2\). Its mean and first projection are zero, so (6.2) applies to the difference as well. This confirms the collision report's obstruction to an unregularized \(L^2\) transfer.

The reports' \(L^1\) approximate-identity arguments are valid. The collision report additionally establishes pointwise convergence off zero; a fixed finite Haar sample has no collisions almost surely. The quantitative finite-\(N\) bound remains only

\[
 \mathbb E|\sigma_N(P_N[g_\epsilon]-P_N[g])|
 \le \sigma_N\frac{N-1}{2N}\|g_\epsilon-g\|_1.
 \tag{6.4}
\]

No sufficient joint rate is inferred merely from \(\|g_\epsilon-g\|_1\to0\). In the range \(2s<d\), the separate \(L^2\) convergence and the exact pair formula do justify the stronger comparison. Both reports maintain this distinction.

## 7. Full probability truncation and both endpoints

Use exactly the collision report's hard distance cutoff \(r<1/4\), and write \(h_r=g\mathbf1_{\{\operatorname{dist}\ge r\}}\), \(m_r=\int h_r=-\tau_r\), \(k_r=h_r-m_r\). These kernels are translation invariant; \(k_r(x-y)\) is canonical. Its boundedness at each fixed \(r>0\) is enough for the iid second-moment formula; no smoothness across the cutoff surface is needed.

Each Haar difference is uniform. The ball lies within the torus injectivity radius, so its volume is exactly \(v_dr^d\). Summing over the unordered pairs gives the valid union bound \(N(N-1)v_dr^d/2\), with no independence assumption for different close-pair events.

On the no-close-pair event, the empirical values of \(g\) and \(h_r\) agree, but their deterministic means differ. Directly from the raw canonical sum,

\[
 P_N[g]=P_N[k_r]+\frac{N-1}{2N}m_r.
 \tag{7.1}
\]

Meanwhile the fully background-centered statistic satisfies
\(P_N[h_r]=P_N[k_r]-m_r/(2N)\).
Both identities hold with exactly the submitted signs and coefficients; neither removes the discarded mean in (7.1).

Let \(V_r=\|k_r\|_2^2\) and
\(B_N(r)=\sigma_N(N-1)|\tau_r|/(2N)\).
For \(z>B_N(r)\), the triangle inequality on the good event and Chebyshev for the centered canonical pair give

\[
 \mathbb P(|\sigma_NP_N[g]|>z)
 \le\frac{N(N-1)}2v_dr^d
 +\frac{b_N(N-1)V_r}{2N^2(z-B_N(r))^2}.
 \tag{7.2}
\]

This checks all finite-particle factors in the collision report's boxed estimate.
Polar integration of (5.4) gives

\[
 \tau_r=\frac{dv_d}{d-s}r^{d-s}+O(r^d).
 \tag{7.3}
\]

The indicated remainder bound uses exactly the submitted supremum of \(H\) on the closed radius-\(1/4\) ball. The upper bound on \(V_r\) in the report follows from
\(g^2\le2|x|^{-2s}+2\|H\|_\infty^2\) there. For the lower orders, the cross term \(|x|^{-s}H\) is locally integrable because \(s<d\), and \(m_r^2\to0\). Consequently
\(V_r\) is of order \(\log(1/r)\) at \(2s=d\) and \(r^{d-2s}\) above it, including both directions. The finite outer-region constant is legitimate because \(g\) is smooth off zero.

At \(2s=d\), \(r_N=N^{-3/d}\) yields close-pair majorant of order \(N^{-1}\), scaled mean of order \(N^{-1}\) at the largest allowed scale, and scaled truncated variance of order \(\log N/N\). The logarithmic endpoint therefore passes despite infinite untruncated variance.

For \(d/2<s<3d/4\), the interval \(2/d<a<1/(2s-d)\) is nonempty. With \(r_N=N^{-a}\), the close-pair and variance exponents are negative. The mean exponent obeys

\[
 \frac12-a(d-s)<\frac{2s}{d}-\frac32<0.
 \tag{7.4}
\]

The direct \(L^2\) formula handles \(s<d/2\). This verifies the full fixed square-root particle scale conclusion for \(0<s<3d/4\), including its endpoint at \(s=d/2\).

For arbitrary temperature sequences in \(d/2<s<d\), set

\[
 A_N=\sqrt{b_N}\,N^{2s/d-3/2},\qquad
 r_N=N^{-2/d}A_N^{1/(2s-d)}.
 \tag{7.5}
\]

The condition in THM-016 is exactly \(A_N\to0\). Since \(b_N>0\), this radius is positive and eventually less than \(1/4\). Direct substitution, without assuming a power law for \(\beta_N\), gives

\[
 N^2r_N^d=A_N^{d/(2s-d)},\qquad
 \sigma_Nr_N^{d-s}=A_N^{s/(2s-d)},\qquad
 \frac{b_N}{N}r_N^{d-2s}=A_N.
 \tag{7.6}
\]

All three expressions vanish. For each fixed \(z>0\), eventually \(B_N(r_N)<z/2\), so (7.2) tends to zero. This states the order of limits explicitly: a single deterministic radius sequence is chosen, then \(N\to\infty\) at fixed probability threshold \(z\). No additional cutoff limit is exchanged with a singular second moment.

At \(s=3d/4\), the sufficient criterion is \(b_N\to0\). Above that exponent it requires faster temperature decay. At and below \(s=d/2\), the estimates already apply for every positive sequence because \(\sigma_N\le\sqrt N\).

For fixed \(b_N=1\) and \(s\ge3d/4\), making the particular union-bound majorant vanish forces \(r_N=N^{-2/d}\ell_N\) with \(\ell_N\to0\). The actual centered truncated variance is then comparable to
\(N^{4s/d-3}\ell_N^{-(2s-d)}\), which diverges. This establishes the limitation of that simultaneous truncation strategy. It does not establish nonconvergence of the original random variable. The already proved range \(d/2\le s<3d/4\) is itself a concrete warning against interpreting infinite variance as failure of convergence in probability.

## 8. Independent exact checks and final handoff

The reviewer wrote VERIFICATION_CODE/round003_hostile_pair_exact.py without inspecting either constructor's code. It executes only standard-library integer and Fraction arithmetic. Result: **PASS, 18,603 exact checks**.

The checks start from the original ordered-pair definition and include:

- Pointwise decompositions, both conditional projections, means, variances, second moments, norm decompositions, sharp inequalities and exact equality criteria, over all configurations for multiple one-, two- and three-point laws through \(N=6\).
- Nonzero means, nonzero first projections, canonical kernels, mixed kernels, a degenerate one-point law and an atomic coordinate-diagonal witness.
- All finite-particle temperature coefficients and a dependent-law witness showing why one-particle marginals alone cannot replace iid preparation.
- A separate seven-point cyclic truncation model, checking the good-event mean shift, the nonzero-mean truncated statistic, centered variance, close-pair union bound and full probability inequality by exhaustive configuration sums.
- Exact max-norm shell counts, both heat-cutoff exponents, the radial square-integrability threshold, the logarithmic-endpoint radius exponents, and all three temperature-radius exponent identities for rational test parameters.

The finite cyclic model tests the probability algebra, not the real-space Riesz singularity. The latter, the universal coefficient formulas, and arbitrary temperature sequences are addressed analytically above. No random sampling, tolerance, floating-point claim, external package, or computational certificate of an asymptotic theorem is involved.

Supporting artifact hashes:

| Artifact | SHA-256 |
|---|---|
| VERIFICATION_CODE/round003_hostile_pair_exact.py | 44434f323bbcf0092bbffbec3be1949c4b596aa5d8214943d001471b99494806 |
| VERIFICATION_CODE/round003_hostile_pair_exact_output.json | f7d6efd8516ad8ace0603bf63a2c7c99b8d81d41732acf84bfbd82665b4a866a |

Verification commands: both input manifests checked with shasum -a 256 -c; the independent exact checker with output saved to the JSON file above; python3 scripts/verify_campaign.py; git diff --check; and control-character, terminal-newline, trailing-whitespace and final hash checks. All passed. The campaign verifier checks repository structure and protected inputs, not the mathematics.

Only this report and the two supporting artifacts were created. Both candidate cards, both submitted proofs, the frozen model and manifests remain byte-identical. No canonical ledger, previous audit, historical input or TeX source was edited. No commit, push, installation, child worker or remote operation was used.

The required disposition is a pass for the initial iid interface with the scopes in Section 1. The first missing lines for a singular dynamic application remain actual backward-corrector norm/projection estimates, positive-time law control and a compatible fluctuation-scale comparison of regularized and singular dynamics. At the fixed largest iid scale, the submitted raw-potential probability argument leaves \(s\ge3d/4\) unresolved; no converse or limiting law there has been certified by this review.
