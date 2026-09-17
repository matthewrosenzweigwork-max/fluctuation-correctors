# Round 003: iid pair projections and singular collision truncation

2026-09-17 UTC. TASK-022. Constructor: `/root/capacity`, Astra Max. Worktree: `/private/tmp/hocf-round003-falsification-20260917`, based on `a06178658d1e3d458536ff312ca793947212ec67`.

Mathematical status: **PROVED_CANDIDATE** for the exact iid formula, the stated singular second-moment obstruction, and the sufficient probability bounds proved here. Audit status: **SELF_CHECKED**. Independent hostile review is required before promotion. No endpoint stable law, converse to the sufficient range, or singular dynamic corrector theorem is asserted.

This reused context previously investigated an operational setting, reconstructed smooth deleted-label algebra, and reviewed the Round 002 residual, Gaussian, and diffusivity dossiers. It had not constructed this iid singular-pair argument. For the present construction it read only TASK-022, the frozen model, and administrative instructions in this assigned baseline worktree. It did not read TASK-021's constructor output, any other Round 003 worktree, or a Round 003 proof narrative. All arguments below are derived here from the stated model, elementary iid conditioning, heat/Fourier identities, and probability inequalities. The input seal is `AUDITS/ROUND_003_COLLISION_FALSIFICATION_INPUT_SHA256SUMS.txt`.

The results concern the initial iid law. The raw Riesz difference kernel used for the singular diagnostic is not identified with a backward pair corrector. Mean-field centering, exact expectation centering, and diagonal deletion are distinguished throughout. No canonical identifiers or state files are changed by this report.

## 1. Exact iid formula, including the finite-particle first projection

Let `(E,mu)` be a probability space on which the displayed product integrals and iid variables are defined, and let `Phi` be a measurable real symmetric element of `L2(mu tensor mu)`. Fix `N>=2` and independent `X_1,...,X_N` with law `mu`. Define

\[
 m=\iint\Phi(x,y)\mu(dx)\mu(dy),\quad
 q(x)=\int\Phi(x,y)\mu(dy)-m,
\]

\[
 r(x,y)=\Phi(x,y)-m-q(x)-q(y).
\]

Fubini and Jensen show that these are well defined in their indicated L2 classes, `mu(q)=0`, and `integral r(x,y) mu(dy)=0` for `mu`-almost every `x`. Orthogonality of the constant, the two first projections, and the remaining kernel gives

\[
 \|\Phi\|_{L^2(\mu^2)}^2
 =m^2+2\|q\|_{L^2(\mu)}^2+\|r\|_{L^2(\mu^2)}^2. \tag{1.1}
\]

Use exactly the frozen normalization

\[
 P_N[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
 -\frac1N\sum_i\int\Phi(X_i,y)\mu(dy)+\frac m2.
\]

Every evaluation with distinct particle labels has law `mu tensor mu`, so changing a product-null representative does not change this statistic almost surely. Its definition contains no self-label evaluation `Phi(X_i,X_i)`. For atomless `mu`, including all smooth-density model inputs, the spatial diagonal is product-null and its values need not be supplied. For a measure with atoms, diagonal values at atoms belong to the L2 equivalence class because distinct labels can have equal coordinates; they cannot be arbitrarily deleted. The claim of not needing a separate diagonal trace is valid in both cases, but the stronger statement that arbitrary diagonal values never matter requires atomlessness.

Collecting the constant and first-projection contributions in the unordered pair sum gives the exact identity

\[
 P_N[\Phi]= -\frac m{2N}
             -\frac1{N^2}\sum_i q(X_i)
             +\frac1{N^2}\sum_{i<j}r(X_i,X_j). \tag{1.2}
\]

Indeed, each `q(X_i)` occurs `N-1` times in the unordered pair sum, while the background term contributes `-q(X_i)/N`; their coefficient is `(N-1)/N^2-1/N=-1/N^2`. The constant coefficient is `(N-1)/(2N)-1+1/2=-1/(2N)`.

Every term in the last two sums has mean zero. The first-projection sum is orthogonal to every canonical pair term: if its label is a pair label, condition on that label and use the zero conditional mean of `r`; otherwise use independence. Two different unordered pair terms are orthogonal as well. Disjoint pairs are independent; pairs with one common label are conditionally independent given that label, with conditional means zero. Only an identical unordered pair contributes its squared norm. All these products are integrable by Cauchy–Schwarz. Consequently

\[
 \mathbb E P_N[\Phi]= -\frac m{2N}, \tag{1.3}
\]

\[
 \operatorname{Var}P_N[\Phi]
 =\frac{\|q\|_2^2}{N^3}
  +\frac{N-1}{2N^3}\|r\|_2^2, \tag{1.4}
\]

\[
 \mathbb E P_N[\Phi]^2
 =\frac{m^2}{4N^2}
  +\frac{\|q\|_2^2}{N^3}
  +\frac{N-1}{2N^3}\|r\|_2^2. \tag{1.5}
\]

Thus mean-field centering does not make the deleted-label statistic exactly expectation-centered. Subtracting its exact expectation removes only the first term in (1.5).

Comparing (1.5) with (1.1), for every `N>=2`,

\[
 \|P_N[\Phi]\|_2
 \le \sqrt{\frac{N-1}{2N^3}}\,\|\Phi\|_{L^2(\mu^2)}
 \le\frac1{\sqrt2 N}\|\Phi\|_{L^2(\mu^2)}. \tag{1.6}
\]

The first constant is sharp whenever the probability space admits a nonzero centered L2 function: take `Phi(x,y)=h(x)h(y)` with `mu(h)=0`, so that `m=q=0`. In the one-point probability space the same bound is valid, though its larger canonical coefficient cannot be attained for `N>2`. At `N=2`, equality in the first bound holds for every symmetric kernel because all three normalized coefficients coincide.

The precise assertion is (1.2)–(1.6) for all stated iid L2 inputs. Its negation is one such input for which one of these identities or the bound fails. The finite-sum and conditioning proof excludes this negation; no U-statistic limit theorem is imported. The assertion makes no claim for an evolved dependent law, or for an arbitrary merely integrable kernel.

## 2. Small-N, constant, first-projection, and temperature checks

For a constant kernel `Phi=c`, the exact statistic is `-c/(2N)`. Its variance is zero, and its second moment is `c^2/(4N^2)`. For `Phi(x,y)=h(x)+h(y)` with `mu(h)=0`, it is `-N^(-2) sum_i h(X_i)`, whose variance is `||h||_2^2/N^3`. Thus deleting the first-projection term in (1.2) would be false even for bounded kernels. A canonical rank-one kernel checks sharpness without requiring any diagonal value for an atomless law.

At `N=2`, (1.5) is `m^2/16+||q||^2/8+||r||^2/16=||Phi||^2/16`. At `N=3`, it is `m^2/36+||q||^2/27+||r||^2/27`. These checks use the frozen denominator `N^2`, not `N(N-1)`.

Put

\[
 b_N=\min(\beta_N,1),\qquad \sigma_N=\sqrt{Nb_N},
 \qquad \beta_N>0. \tag{2.1}
\]

For a canonical kernel, the exact scaled variance is

\[
 \mathbb E|\sigma_NP_N[\Phi]|^2
 =\frac{b_N(N-1)}{2N^2}\|\Phi\|_2^2. \tag{2.2}
\]

For a general L2 kernel, (1.6) gives the same right side as an upper bound for the second moment. In particular a fixed L2 kernel is negligible at this scale for every positive temperature sequence. No assertion that a positive temperature factor makes an infinite second moment finite is intended.

An independently written standard-library checker evaluates the original ordered-pair formula over all configurations of a three-point iid law of weights `1/2,1/3,1/6`, using exact rational arithmetic. It checks constant, nonzero first projection, canonical rank-one, and mixed kernels at `N=2,3,4,6`. Its 3,453 checks comprise 3,384 configuration identities, 59 moment/norm/sharpness checks, and 10 positive-temperature factor checks. This is supporting evidence for the proof, not an independent audit.

## 3. Real-space Riesz behavior proved from the frozen Fourier normalization

Now take the unit torus in integer dimension `d>=1`, Haar probability measure, and `0<s<d`. Write

\[
 \alpha=\frac{d-s}{2}>0,\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}.
\]

The frozen kernel has zero Fourier mean and nonzero coefficients `c_(d,s)|k|^(s-d)`. The following derivation proves the real-space representative needed here and verifies its leading constant; it does not assume the claimed local singularity as an unproved input.

Let

\[
 q_t(x)=(4\pi t)^{-d/2}e^{-|x|^2/(4t)},\qquad
 p_t(x)=\sum_{n\in\mathbb Z^d}q_t(x+n).
\]

The Gaussian integral, first in one coordinate and then by products, gives the Fourier transform of `q_t` at frequency `k` as `exp(-4 pi^2 t |k|^2)`. Unfolding the absolutely convergent periodization proves that these are the Fourier coefficients of `p_t`. Thus `p_t` is nonnegative, has mass one, and is the torus heat kernel. Its Fourier series shows exponential decay of `p_t-1`, with all spatial derivatives, for `t>=1`.

Set

\[
 A_{d,s}=\frac{4^{(d-s)/2}\pi^{d/2}}{\Gamma(s/2)},\qquad
 g(x)=A_{d,s}\int_0^\infty t^{\alpha-1}(p_t(x)-1)dt. \tag{3.1}
\]

This integral defines an L1 function: for `t<=1`, the L1 norm of `p_t-1` is at most two, and for `t>=1` it decays exponentially. Its mean is zero. Fubini gives for `k!=0`

\[
 \widehat g(k)=A_{d,s}\frac{\Gamma(\alpha)}{(4\pi^2|k|^2)^\alpha}
             =c_{d,s}|k|^{s-d}, \tag{3.2}
\]

exactly the frozen positive normalization. This specifies the required L1 representative, uniquely up to null sets; uniqueness follows, for example, by convolving the difference with `p_t`, whose Fourier series is absolutely convergent, and then using the elementary approximate-identity property as `t` decreases to zero.

For `x!=0` in Euclidean coordinates,

\[
 A_{d,s}\int_0^\infty t^{\alpha-1}q_t(x)dt=|x|^{-s}, \tag{3.3}
\]

by the substitution `u=|x|^2/(4t)`. The prefactor in (3.3) is exactly one. On the ball `|x|<1/3`, subtract this whole-space integral from (3.1). For `t<=1`, all nonzero lattice translates have distance bounded away from zero; their derivatives are bounded by a fixed negative power of `t` times `exp(-c/t)`, which is integrable against every relevant power of `t`. The subtracted constant term is integrable because `alpha>0`. For `t>=1`, the torus heat remainder decays exponentially, while the whole-space integrand has size at most a constant times `t^(-s/2-1)`, also integrable. Spatial derivatives of the latter improve this large-time bound. Differentiation under these bounds proves

\[
 g(x)=|x|^{-s}+H(x),\qquad H\text{ smooth on }|x|<1/3. \tag{3.4}
\]

The same heat representation gives smoothness off the origin. Therefore `g` is bounded below on the torus, is integrable, and satisfies

\[
 g\in L^p\quad\Longleftrightarrow\quad ps<d
 \qquad (1\le p<\infty). \tag{3.5}
\]

Here the failure at equality is logarithmic, and the lower bound needed for necessity comes from the positive principal coefficient in (3.4). No logarithmic interaction is introduced by this argument; `s` remains strictly positive.

## 4. The precise second-moment obstruction and the cutoff-order issue

For iid Haar labels, `Phi(x,y)=g(x-y)` has zero mean and zero first projection in L1. The unregularized statistic is well defined almost surely and integrable, since distinct labels do not collide with positive probability and `g` is integrable. Explicitly,

\[
 P_N[g]=\frac1{N^2}\sum_{i<j}g(X_i-X_j),\qquad \mathbb EP_N[g]=0. \tag{4.1}
\]

If `2s<d`, (1.4) applies. If `2s>=d`, it cannot be invoked with a finite norm. In fact the second moment of (4.1) is infinite for every finite `N>=2`. To see this without an unjustified expansion of infinite cross moments, choose a finite `C` with `g>=-C` everywhere off the origin. With `M=N(N-1)/2`,

\[
 (P_N[g])_+\ge \frac1{N^2}\big(g(X_1-X_2)-C(M-1)\big)_+.
\]

The right side has infinite second moment by (3.4). Multiplication by any positive finite `sigma_N` does not change this conclusion. This proves an L2 obstruction, not nonconvergence in probability.

For heat regularization `g_epsilon=p_epsilon*g`, Parseval and (3.2) give

\[
 \|g_\varepsilon\|_2^2
 =c_{d,s}^2\sum_{k\ne0}|k|^{2s-2d}
                   e^{-8\pi^2\varepsilon|k|^2}. \tag{4.2}
\]

Dyadic lattice annuli contain between fixed positive multiples of `R^d` points for all sufficiently large radii `R`; this follows by covering with unit cubes and comparing the volumes of annuli of fixed relative width. Applying this to (4.2), and summing the exponentially small annuli beyond `R` of order `epsilon^(-1/2)`, gives

\[
 \|g_\varepsilon\|_2^2\asymp
 \begin{cases}
 1,&2s<d,\\
 \log(1/\varepsilon),&2s=d,\\
 \varepsilon^{-(2s-d)/2},&2s>d,
 \end{cases}\qquad \varepsilon\downarrow0. \tag{4.3}
\]

The first row has the stronger conclusion of convergence to `||g||_2^2>0`. Constants depend only on the fixed `d,s` normalization. At equality every dyadic annulus contributes a bounded positive amount up to the cutoff; above equality the final unsuppressed annuli have the stated power. These observations supply both lower and upper bounds, not just a formal radial integral.

Combining (2.2) with (4.2) gives the exact regularized variance at every finite `N`. In the supercritical L2 range, it is small along any joint choice satisfying

\[
 \frac{b_N}{N}\varepsilon_N^{-(2s-d)/2}\longrightarrow0. \tag{4.4}
\]

For example, with `b_N=1` and `epsilon_N=N^(-q)`, any `0<q<2/(2s-d)` suffices. At `2s=d` the condition is `b_N log(1/epsilon_N)/N -> 0`. Nevertheless the unregularized statistic, and its difference from this fixed smooth regularization, each have infinite second moment whenever `2s>=d`. The difference kernel retains the same positive singularity and a bounded remainder, so the preceding lower-bound proof applies to it as well.

Thus the shortcut transferring a small heat-regularized variance to an unregularized L2 residual is false. A proposed transfer only in probability requires an additional cutoff comparison; infinite variance by itself neither proves nor disproves that probability conclusion.

For completeness, `g_epsilon` does converge to `g` in L1 and pointwise away from zero. In (3.1), convolution with `p_epsilon` replaces `p_t` by `p_(t+epsilon)`. Dominated convergence in L1 uses the bound two for small `t` and exponential bounds for large `t`. At a fixed nonzero point the periodized Gaussian remains bounded as its time decreases to zero, so the same argument gives pointwise convergence. Consequently for fixed finite `N`, `P_N[g_epsilon] -> P_N[g]` almost surely and in L1, even in the infinite-variance range. The direct quantitative comparison available without further estimates is

\[
 \mathbb E\big|\sigma_N(P_N[g_\varepsilon]-P_N[g])\big|
 \le \sigma_N\frac{N-1}{2N}\|g_\varepsilon-g\|_1. \tag{4.5}
\]

An unscaled fixed-N limit supplies no rate sufficient to make (4.5) vanish along a joint cutoff/particle sequence. For fixed positive cutoff the scaled pair tends to zero in L2 as `N` increases; for fixed `N` the cutoff removal has divergent second moments when `2s>=d`. These two facts do not justify interchanging the L2 limits. For `2s<d`, ordinary L2 cutoff convergence and (1.4) do justify the L2 comparison.

## 5. A probability bound with close pairs, discarded mean, and centered variance

Here and in the remainder of the report the law is iid Haar at initial time. Let `dist` be the torus Euclidean distance, `v_d` the Euclidean unit-ball volume, and fix `0<r<r_0=1/4`. Define

\[
 h_r(x)=g(x)\mathbf1_{\{\operatorname{dist}(x,0)\ge r\}},\quad
 m_r=\int h_r=-\tau_r,\quad
 \tau_r=\int_{\operatorname{dist}(x,0)<r}g(x)dx,
 \quad k_r=h_r-m_r. \tag{5.1}
\]

The translation-invariant kernel `k_r(x-y)` is canonical and bounded for each fixed positive `r`. Its variance uses the exact coefficient (1.4), with no first projection. Let `E_r` be the event that every pair of distinct labels is at distance at least `r`. A union bound, using the Haar law of each difference, gives

\[
 \mathbb P(E_r^c)\le\frac{N(N-1)}2 v_d r^d. \tag{5.2}
\]

No independence between different close-pair events is asserted. On `E_r`, every sampled `g` equals `h_r`, but its mean does not equal the truncated kernel's mean. Keeping that difference gives exactly

\[
 P_N[g]=P_N[k_r]+\frac{N-1}{2N}m_r
        =P_N[k_r]-\frac{N-1}{2N}\tau_r
 \quad\text{on }E_r. \tag{5.3}
\]

The coefficient in (5.3) is not one half without its finite-N correction. If the nonzero-mean deleted statistic `P_N[h_r]` is used instead, then `P_N[h_r]=P_N[k_r]-m_r/(2N)`; this gives the same (5.3), not a cancellation of the discarded mean.

Write `V_r=||k_r||_2^2=integral h_r^2-m_r^2`. For any `z>0` such that

\[
 B_N(r):=\sigma_N\frac{N-1}{2N}|\tau_r|<z,
\]

Chebyshev on the canonical truncated statistic and (5.2)–(5.3) prove

\[
 \boxed{\quad
 \mathbb P\{|\sigma_NP_N[g]|>z\}
 \le \frac{N(N-1)}2 v_d r^d
 +\frac{b_N(N-1)V_r}{2N^2\,[z-B_N(r)]^2}.
 \quad} \tag{5.4}
\]

This is the precise probability truncation estimate. Its three obligations are a vanishing close-pair probability, a vanishing deterministic discarded-mean shift, and a vanishing truncated centered variance. Each is separately estimated below.

Let `C_H=sup_(|x|<=r_0)|H(x)|`, which is finite by (3.4) and `r_0=1/4`. Polar integration in (3.4) gives

\[
 \tau_r=\frac{dv_d}{d-s}r^{d-s}+O(C_Hv_d r^d),\qquad
 |\tau_r|\le\frac{dv_d}{d-s}r^{d-s}+C_Hv_d r^d. \tag{5.5}
\]

In particular the leading discarded mean is positive. Define the finite constant

\[
 C_0=\int_{\operatorname{dist}(x,0)\ge r_0}g(x)^2dx
          +2C_H^2v_d r_0^d.
\]

Using `g^2 <= 2|x|^(-2s)+2C_H^2` inside the ball gives

\[
 V_r\le C_0+2dv_d\int_r^{r_0}u^{d-1-2s}du
 \le C\begin{cases}
 1,&2s<d,\\
 1+\log(1/r),&2s=d,\\
 r^{d-2s},&2s>d.
 \end{cases} \tag{5.6}
\]

These constants are independent of `N,beta_N,r`. At `2s>=d`, the same local positive singularity also gives the corresponding asymptotic order as a lower bound for `V_r`; subtracting `m_r^2`, which tends to zero, does not remove the divergent integral.

At `N=2`, the shift coefficient in (5.3) is one quarter and the scaled canonical variance coefficient is `b_N/8`. At `N=3`, they are one third and `b_N/9`. These agree directly with the one and three unordered pairs, respectively.

## 6. Proved sufficient ranges and the unresolved boundary

First take `sigma_N=sqrt(N)`, so `b_N=1`. The sufficient conditions from (5.4) for an arbitrary positive radius sequence decreasing to zero are

\[
 N^2r_N^d\to0,\qquad
 \sqrt N\,r_N^{d-s}\to0,\qquad
 \frac1N\begin{cases}
 1,&2s<d,\\
 1+\log(1/r_N),&2s=d,\\
 r_N^{d-2s},&2s>d
 \end{cases}\longrightarrow0. \tag{6.1}
\]

For `2s<d`, the direct L2 formula already proves the desired conclusion. At the borderline `2s=d`, choosing `r_N=N^(-3/d)` gives close-pair probability `O(N^(-1))`, discarded scaled mean `O(N^(-1))`, and centered truncated variance `O(log(N)/N)`. Thus the probability conclusion holds there despite the infinite untruncated variance at every finite N.

For `d/2<s<3d/4`, choose

\[
 r_N=N^{-a},\qquad \frac2d<a<\frac1{2s-d}. \tag{6.2}
\]

The interval is nonempty precisely in this strict range. The close-pair exponent is `2-ad<0`; the variance exponent is `-1+a(2s-d)<0`; and the mean exponent satisfies `1/2-a(d-s)<1/2-2(d-s)/d<0`. Thus all three terms vanish. We have proved the sufficient statement

\[
 \boxed{\quad 0<s<\frac{3d}4
 \quad\Longrightarrow\quad
 \sqrt N P_N[g]\longrightarrow0\text{ in probability, for iid Haar data.}\quad}
 \tag{6.3}
\]

Its exact negation is fixed permitted `d,s` in this range and some `z>0` with a positive subsequential limsup of the probabilities in (6.3). Bound (5.4) with the displayed radii excludes that negation. This new probabilistic assertion is SELF_CHECKED pending independent review.

Because `sigma_N<=sqrt(N)`, the same conclusion holds with the frozen `sigma_N` for every positive temperature sequence throughout (6.3). In the larger range `d/2<s<d`, the temperature factors give a further sufficient criterion. Set

\[
 A_N=\sqrt{b_N}\,N^{2s/d-3/2}.
\]

If `A_N -> 0`, choose

\[
 r_N=N^{-2/d}A_N^{1/(2s-d)}. \tag{6.4}
\]

For all sufficiently large N this is an admissible small radius. The three terms in (5.4) then have the bounds

\[
 N^2r_N^d=A_N^{d/(2s-d)},\qquad
 \sigma_N r_N^{d-s}=A_N^{s/(2s-d)},\qquad
 \frac{b_N}{N}r_N^{d-2s}=A_N. \tag{6.5}
\]

All vanish. Therefore for `d/2<s<d` we also prove

\[
 b_N N^{4s/d-3}\to0
 \quad\Longrightarrow\quad
 \sigma_NP_N[g]\to0\text{ in probability}. \tag{6.6}
\]

At `s=3d/4`, this includes every sequence with `beta_N -> 0`. Above that exponent it gives the explicit smaller-temperature sufficient condition in (6.6). At or below `s=d/2`, convergence holds for every positive temperature sequence, as already shown. Equation (6.6) is a statement about this initial iid raw pair diagnostic, not a replacement for any microscopic coupling condition in the campaign.

For `sqrt(N)` scaling and `s>=3d/4`, this report does not prove convergence or its failure. There is a precise obstruction to satisfying this particular no-close-pair plus variance argument: vanishing (5.2) forces `r_N=N^(-2/d) ell_N` with `ell_N -> 0`, whereas the actual scaled truncated variance in the supercritical L2 range is comparable to

\[
 N^{4s/d-3}\ell_N^{-(2s-d)},
\]

which diverges in this range. This proves failure of that simultaneous truncation strategy; it is not a nonconvergence theorem for the untruncated statistic. Infinite or diverging variances alone do not rule out convergence in probability. Indeed the already proved range `d/2<=s<3d/4` is an explicit example where every untruncated variance is infinite and the probability convergence nevertheless holds.

## 7. Scaling ledger and first remaining line

| Singularity range | Unregularized pair L2 | Heat squared norm as cutoff decreases | Initial iid probability conclusion at the frozen scale |
|---|---|---|---|
| `0<s<d/2` | Finite; exact formula (1.4) | Converges to a finite positive constant | Vanishes for every positive temperature sequence, already in L2. |
| `2s=d` | Infinite at every finite N | Order `log(1/epsilon)` | Vanishes in probability for every positive temperature sequence by logarithmic truncation. |
| `d/2<s<3d/4` | Infinite at every finite N | Order `epsilon^(-(2s-d)/2)` | Vanishes in probability for every positive temperature sequence by (6.2). |
| `s=3d/4` | Infinite at every finite N | Same power rule | Vanishes if `b_N -> 0`; no conclusion here at `sqrt(N)` scale. |
| `3d/4<s<d` | Infinite at every finite N | Same power rule | Vanishes under the sufficient condition `b_N N^(4s/d-3) -> 0`; no converse is claimed. |

The first unresolved line for this diagnostic at fixed `sqrt(N)` scale is a probability or limiting-law analysis of the centered contribution from separations of order `N^(-2/d)` when `s>=3d/4`. An example of the precise term requiring a new argument is

\[
 N^{-3/2}\left[
 \sum_{i<j}g(X_i-X_j)\mathbf1_{\{\operatorname{dist}(X_i,X_j)<cN^{-2/d}\}}
 -\frac{N(N-1)}2\int_{\operatorname{dist}(x,0)<cN^{-2/d}}g(x)dx
 \right], \tag{7.1}
\]

with the remaining distances controlled in the same limiting procedure. No estimate that determines its limiting behavior at the unresolved exponents is proved here. Establishing or refuting a stable limit, proving a converse, or transferring any of these bounds to an actual singular backward corrector would require new work. The kernel of that corrector, its time dependence, and the evolved law cannot be replaced by the Haar raw Riesz diagnostic.

The original energy-floor condition, the microscopic subcritical target, and the critical coupling target remain distinct and unchanged. This report introduces neither a singular dynamic generator passage nor a logarithmic case. The exact iid formula is diagonal-free in the stated sense; no singular pointwise self-interaction was inserted to obtain it.

## 8. Verification and handoff

Input SHA-256 values:

- TASK-022: `502452c43e0e20f3d45699b7f31134a53e8a804c5cb092e1a890b654bbc01217`.
- Frozen model: `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57`.

Commands executed in the assigned worktree:

- `python3 VERIFICATION_CODE/round003_iid_projection_exact.py`: PASS, 3,453 exact rational checks; saved output in `VERIFICATION_CODE/round003_iid_projection_exact_output.json`.
- `python3 scripts/verify_campaign.py`: `CAMPAIGN VERIFICATION PASSED`; structural integrity only, not mathematical certification.
- Input-manifest verification and final `git diff --check`: passed. New outputs were separately checked for control characters, trailing whitespace, terminal newlines and paired display delimiters.

The exact checker SHA-256 is `643e585170569d92496450cbdab7c7992f6e85a5e1be2c5f39e725b3f3be1c6f`; its output SHA-256 is `4f4a28c415d6de367ac3291cd7599caa35402d69fee944e6457c087613ca461f`. The adjacent final output manifest records these and the report/input-manifest hashes after sealing. No self-hash is placed inside the report bytes.

Created files are this memorandum, the input and output hash manifests, and the exact checker with its output. No canonical ledger, candidate from another constructor, historical input, previously issued audit, or TeX file was modified. No commit, push, remote operation, dependency installation, or child worker was used. Root alone compares independent constructions, obtains hostile review, allocates canonical identifiers, and integrates any resulting promotion.
