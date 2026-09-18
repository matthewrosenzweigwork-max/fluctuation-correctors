# Round 010 — actual-law entropy transfer and the remaining gradient tail

TASK060. **RIGOROUS SHARPER REDUCTION / SELF_CHECKED; full actual-noise assertion OPEN.** The domain assertion THM028 and the supplied R9 energy construction remain conditional prerequisites in this dossier. This is the disclosed continuation constructor of TASK051 and TASK055, with the earlier root seed disclosed. It is not a fresh reconstruction or independent certification.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r010-law-transfer-20260918`. Branch: `codex/hocf-r010-law-transfer`. Base: published R7 `4171be9839feb8acf4c70e1dda014458fdb44490`. The twenty permitted inputs were copied and hash-checked before construction. Only that dossier was used. Prior worktrees and seals were preserved. No ongoing audit, current other-worker output, canonical state/history, memory, old checker, or outside literature was read; no root edits, commits, pushes, installations or children were used.

The new analytic result is an actual-dynamics free-energy bound and its quantitative two-/three-marginal entropy consequences. These prove vanishing expected noise for a precisely clipped part of the actual corrector martingale throughout the task's bounded-noise range. The original expected bracket vanishes if and only if the remaining large-gradient martingale tail vanishes. This is a sharper exact reduction, not a proof of the full assertion. Section 9 gives its first unproved line and an explicit attempt to estimate it with the supplied weighted domain bounds.

## 1. Assertion, normalization, and the exact starting reduction

Use the unit Haar torus, fixed integer `d>=3`, `0<s<=d-2`, finite T, smooth real terminal h, zero external drift, reference density one, the frozen positive-Fourier Riesz potential g, and `K=-grad g`. Put `p=s+2`, `a=s/p`. For each integer `N>=2`, take `0<nu=1/beta_N<=nu_*`, set `b_N=min(beta_N,1)` and `sigma_N^2=N b_N`, and use the genuine symmetric terminal-zero full pair inverse Phi with both exact responses. The initial N-body law is iid Haar, independent of the independent Brownian drivers.

The primary assertion to be proved or falsified is

\[
 Q_N:=\sigma_N^2\mathbb E\langle M_{2,N}\rangle_T
 =2\nu N b_N\int_0^T\mathbb E\sum_i|v_{i,t}(X_t)|^2dt\longrightarrow0,
 \tag{1.1}
\]

where the conditional THM028 domain theorem supplies the square-integrable true martingale and

\[
 \begin{gathered}
 G_t(x,y)=\nabla_x\Phi_t(x,y),\qquad A_t(x)=\int G_t(x,y)dy,
 \qquad H_t(x,y)=G_t(x,y)-A_t(x),\\
 v_{i,t}=\nabla_iP_t
 =N^{-2}\left[\sum_{j\ne i}H_t(X_i,X_j)-A_t(X_i)\right].
 \end{gathered}
 \tag{1.2}
\]

The exact negation is an admitted fixed `d,s,T,h` and bounded-noise sequence for which the limsup of the nonnegative quantity (1.1) is positive or infinite. No such sequence for the stipulated dynamics is constructed here. Zero noise gives a zero bracket directly, without a reciprocal convention at zero. Constant h gives a zero source and corrector, and T=0 gives zero integrated noise.

The supplied R9 construction gives, conditionally,

\[
 Q_N^{\rm Haar}\le C_E b_N N^{-2/p},
 \tag{1.3}
\]

with C_E independent of N and of the selected noise in its range. Its exact law difference is

\[
 Q_N-Q_N^{\rm Haar}
 ={2\nu b_N\over N^2}\int_0^T
 [(N-1)\delta_{2,N}+(N-1)(N-2)\delta_{3,N}
                         -2(N-1)\delta_{A,N}]dt,
 \tag{1.4}
\]

where the deviations test the actual pair density against `|H|^2`, the triple density against `H(x,y).H(x,z)`, and the pair density against `H(x,y).A(x)`, respectively. The triple term is absent at N=2. The one-body square term has already cancelled because the actual one-body marginal is Haar. No signed term in (1.4) is replaced by an assumed zero.

The present route estimates (1.4) first for bounded clipped fields by actual-law entropy. It then keeps the remaining martingale tail as a nonnegative quadratic quantity, preserving its signed internal contractions.

## 2. A uniform lower bound for the actual interaction energy

Define the total energy whose gradient gives the drift by

\[
 U_N(X)=\frac1N\sum_{i<j}g(X_i-X_j),\qquad
 b_i(X)=-\nabla_iU_N(X)=\frac1N\sum_{j\ne i}K(X_i-X_j).
 \tag{2.1}
\]

Thus U_N is N times the ordered-pair energy with coefficient `1/(2N^2)`. This factor is important for the entropy bound below.

The supplied `ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, equations (1.1) and (2.2)–(2.6), fixes

\[
 \widehat g(k)=c_{d,s}|k|^{s-d}>0\ (k\ne0),\quad\widehat g(0)=0,
 \qquad D=\operatorname{div}K=-\Delta g\ge-\kappa\,dx,
 \tag{2.2}
\]

where `c_(d,s)=pi^(s-d/2) Gamma((d-s)/2)/Gamma(s/2)` is exactly the frozen positive coefficient, and kappa is fixed and nonnegative. At Coulomb, `D=c_d(delta_0-dx)`; the heat smoothing below retains this atom exactly. Let `g_epsilon=exp(epsilon Delta)g`. For every positive epsilon and r,

\[
 g_\epsilon(z)\ge g_{\epsilon+r}(z)-\kappa r,
 \tag{2.3}
\]

because `partial_r g_(epsilon+r)=exp((epsilon+r)Delta)Delta g<=kappa`. At epsilon zero this follows off the collision point by local uniform convergence of the heat regularization. To see that convergence directly, split g into a smooth part agreeing with it near a chosen compact collision-excluded set and an L1 part supported a positive distance away. The Gaussian approximate identity handles the first part, and its decaying off-support bound handles the second. No value of the singular potential at zero is used in a deleted sum.

There is a fixed finite C_g such that

\[
 0<g_r(0)\le C_g r^{-s/2}\qquad(0<r\le1).
 \tag{2.4}
\]

For an explicit sufficient constant, dyadic shells in the frozen Fourier series give

\[
 C_g=c_{d,s}5^d\left[
 {2^s\over2^s-1}+\sum_{j\ge1}2^{js}e^{-\pi^2 4^j}\right].
 \tag{2.5}
\]

Indeed the shell `2^m<=|k|<2^(m+1)` has at most `5^d 2^(md)` lattice points. Its contribution is at most `c_(d,s)5^d 2^(ms) exp(-4 pi^2 r 4^m)`. Choose M with `2^M<=r^-1/2<2^(M+1)`. The terms through M are bounded by `r^-s/2 2^s/(2^s-1)`, and the remaining terms are bounded by `r^-s/2 sum_(j>=1)2^(js)exp(-pi^2 4^j)`. The convergent series proves (2.4) for every r in the interval, not just asymptotically.

All nonzero Fourier coefficients of `g_(epsilon+r)` are nonnegative. Hence

\[
 \sum_{i,j}g_{\epsilon+r}(X_i-X_j)
 =\sum_{k\ne0}\widehat g(k)e^{-4\pi^2(\epsilon+r)|k|^2}
               \left|\sum_i e^{2\pi i k\cdot X_i}\right|^2\ge0.
 \tag{2.6}
\]

Its diagonal contribution is exactly `N g_(epsilon+r)(0)`. Combining (2.3)–(2.6) and using `g_(epsilon+r)(0)<=g_r(0)` gives, for the smooth or singular deleted energy,

\[
 U_N^\epsilon\ge-\frac12g_r(0)-\frac{\kappa(N-1)}2r.
 \tag{2.7}
\]

Take `r=N^(-2/p)<=1`. Both `r^(-s/2)` and `Nr` equal `N^a`. Consequently

\[
 \boxed{U_N^\epsilon\ge-C_0N^a,\qquad
 C_0=(C_g+\kappa)/2,\qquad N\ge2,\quad\epsilon\ge0.}
 \tag{2.8}
\]

For epsilon zero the assertion is on collision-free configurations. The constant is uniform in N, the smoothing parameter, time, and noise. This is a proved, possibly nonoptimal lower bound. It is not asserted to be the optimal microscopic energy floor or identified with any campaign temperature condition.

## 3. Free energy for the actual iid-Haar-prepared law

For a probability density F relative to unit Haar N-body measure, write

\[
 \mathcal H_N(F)=\int F\log F,\qquad 0\log0=0.
\]

At a fixed positive smoothing epsilon and positive nu, the smooth gradient dynamics have Fokker–Planck equation

\[
 \partial_tF_N^\epsilon
 =\nu\Delta F_N^\epsilon+
       \operatorname{div}(F_N^\epsilon\nabla U_N^\epsilon),
 \qquad F_N^\epsilon(0)=1.
 \tag{3.1}
\]

All derivatives here are in the full N-particle configuration. At fixed epsilon, compactness and the smooth drift permit the heat integral equation to be solved in spatially differentiable classes: the heat gradient bound has an integrable `t^-1/2` time singularity, and successive short intervals give any finite horizon. The scalar maximum principle, applied with an exponential factor bounding `div grad U_N^epsilon`, gives a positive lower bound at fixed epsilon and T. Thus the density is smooth and positive, and integration by parts below is legitimate. These preliminary constants need not be uniform in epsilon; they are not used in (3.4).

Differentiating and using (3.1) gives the exact identity

\[
 \frac d{dt}\left[\nu\mathcal H_N(F_N^\epsilon)
                    +\int U_N^\epsilon F_N^\epsilon\right]
 =-\int F_N^\epsilon
       |\nu\nabla\log F_N^\epsilon+\nabla U_N^\epsilon|^2\le0.
 \tag{3.2}
\]

The Fisher-square coefficient in this normalization is `nu^2`, not nu. The initial free energy is exactly zero: `F_0=1`, Haar entropy is zero, and the kernel has zero mean. By (2.8),

\[
 \nu\mathcal H_N(F_N^\epsilon(t))+
       \mathbb E U_N^\epsilon(X_t^\epsilon)\le0,
 \qquad\mathcal H_N(F_N^\epsilon(t))\le {C_0N^a\over\nu}.
 \tag{3.3}
\]

We now pass to the stipulated singular dynamics, rather than declaring (3.2) valid across collisions. Section 7 of the supplied R6 realization proves, for fixed N and nu and iid Haar preparation, same-noise convergence of the smoothed paths uniformly on finite time intervals, almost surely. The limiting path is collision-free and has positive minimum separation on each finite interval. Local uniform convergence of the smoothed potential therefore gives
`U_N^epsilon(X_t^epsilon)->U_N(X_t)` almost surely at every fixed t. The common lower bound (2.8) permits Fatou after adding `C_0N^a`.

The laws also converge weakly. Relative entropy is lower semicontinuous in this topology: it is the supremum over continuous bounded q of
`integral q dLambda-log integral exp(q) dHaar`. The inequality in this formula follows from Jensen with density F, and equality follows by truncating `log F` and approximating the truncations in the finite measures involved by continuous functions on the compact torus. This supplies both the lower semicontinuity mechanism and the topology used. The actual law already has a bounded density at fixed N by R6. Combining the two lower semicontinuity bounds, with their common finite lower bounds, passes the sum in (3.3). Thus for every time,

\[
 \boxed{\nu\mathcal H_N(F_N(t))+\mathbb E U_N(X_t)\le0,
 \qquad \mathcal H_N(F_N(t))\le {C_0N^a\over\nu}.}
 \tag{3.4}
\]

No weak convergence of an unbounded force square or singular entropy-production term is asserted. Only the free-energy inequality is passed. This argument uses the supplied particle realization and the kernel normalization, and does not use THM028 or R9's corrector regularity.

There is also a useful actual pair-energy consequence. Since entropy is nonnegative, (3.4) gives `E U_N<=0`. Exchangeability then yields

\[
 \mathbb E g(X_1-X_2)\le0,
 \qquad\mathbb E[g(X_1-X_2)-g_*]\le-g_*,\quad
 g_*:=\inf g<0.
 \tag{3.5}
\]

Both sides are well-defined: the lower bound and (3.4) imply finite positive energy expectation. Any fixed positive weight w_s equal to `r^-s` near zero obeys

\[
 \sup_{N,\nu,t}\mathbb E w_s(X_1-X_2)\le C_s<\infty,
 \tag{3.6}
\]

because `w_s<=C[1+g-g_*]` on the torus. The constant depends only on the frozen weight and kernel. This improves the elementary time-dependent pair-energy upper bound obtainable from the energy identity alone.

## 4. Fixed-marginal information bounds with exact finite-N factors

Common translations and permutations of labels preserve the singular equation and its iid Haar initial/driver law. The supplied per-start pathwise uniqueness and joint measurability justify the transformed-law comparison after integrating over initial data. Therefore the actual law is exchangeable and each one-body marginal is Haar. As in R9, this gives no product assertion for higher marginals.

Let `H_k(t)` be the relative entropy of its k-body marginal. For completeness, set `H_0=0` and `c_j=H_j-H_(j-1)`. The entropy chain rule identifies c_j with the expected relative entropy, against one-body Haar, of the conditional distribution of X_j given the first `j-1` variables. Convexity under averaging the last conditioning variable and exchangeability imply `c_(j+1)>=c_j`. Also `c_1=0` because the one-body marginal is Haar. Averages of the first `k-1` members of this nondecreasing sequence cannot exceed the average of all `N-1` members. Hence

\[
 \boxed{H_k(t)\le {k-1\over N-1}H_N(t)
      \le {C_0(k-1)N^a\over\nu(N-1)},\qquad 2\le k\le N.}
 \tag{4.1}
\]

The chain rule is applicable because (3.4) is finite; conditional densities on null conditioning events may be chosen arbitrarily. At `k=N` this is equality in the first comparison. For N=2 only k=2 is required.

We use the following elementary form of the entropy-to-L1 estimate:

\[
 \|F-1\|_1\le\sqrt{2\mathcal H(F)}.
 \tag{4.2}
\]

To verify the normalization, let `B={F>=1}`, `q=Haar(B)`, `p=integral_B F`. Jensen on B and its complement bounds entropy below by the Bernoulli relative entropy with parameters p,q. Its second derivative in p is `1/[p(1-p)]>=4`, and its value and first derivative vanish at p=q, so it is at least `2(p-q)^2`. Since `||F-1||_1=2(p-q)`, (4.2) follows, with degenerate cases obtained by a limit.

For k=2,3 define the available upper bounds

\[
 e_{k,N}=\min\left(2,
 \sqrt{{2C_0(k-1)N^a\over\nu(N-1)}}\right).
 \tag{4.3}
\]

Then every bounded measurable k-body test Z satisfies, uniformly in time,

\[
 \left|\int Z(F_t^{(k)}-1)\right|\le\|Z\|_\infty e_{k,N},
 \qquad e_{k,N}\le2\sqrt{{C_0(k-1)\over\nu}}N^{-1/p}.
 \tag{4.4}
\]

The second estimate uses `N/(N-1)<=2` and `(a-1)/2=-1/p`. The third marginal and its bound are simply omitted when N=2. Densities can be chosen jointly measurable for time-integrated formulas by taking the Radon–Nikodym derivative of the measure `dt Lambda_t` against time times Haar; R6 domination is uniform on each fixed-N finite interval. Alternatively all expressions are defined directly by the jointly measurable marginal kernels.

The factor nu in noise will compensate for the inverse square root of nu in (4.4). No assertion that the unweighted total variation tends to zero for every admitted temperature sequence is being made.

## 5. A bounded part of the actual martingale whose bracket vanishes

For L>0, clip only the first-coordinate gradient vector radially:

\[
 G_t^L(x,y)=\begin{cases}
 G_t(x,y),&|G_t(x,y)|\le L,\\
 L G_t(x,y)/|G_t(x,y)|,&|G_t(x,y)|>L.
 \end{cases}
 \quad A_t^L(x)=\int G_t^L(x,y)dy,\quad H_t^L=G_t^L-A_t^L.
 \tag{5.1}
\]

Thus `|G^L|,|A^L|<=L` and `|H^L|<=2L`. Define

\[
 v_{i,t}^L=N^{-2}\left[\sum_{j\ne i}H_t^L(X_i,X_j)-A_t^L(X_i)\right],
 \qquad M_N^L=\sqrt{2\nu}\sum_i\int_0^\cdot v_{i,t}^L(X_t)\cdot dW_i(t).
 \tag{5.2}
\]

This is an actual square-integrable martingale: its field is predictable and bounded by `2L/N`. Boundedness and dominated convergence also give the needed measurable background integrals. The field need not be the gradient of a new pair potential. We are decomposing the noise of the genuine corrector, not replacing its equation, drift, or centering.

Set `Q_N^L=sigma_N^2 E< M_N^L>_T` and define its Haar reference analog by evaluating the same field on independent Haar points. Conditional Haar centering gives the exact identity for this arbitrary vector field,

\[
 \int_{\mathrm{Haar}^N}\sum_i|v_i^L|^2
 ={N-1\over N^3}\|G^L\|_2^2-{N-2\over N^3}\|A^L\|_2^2.
 \tag{5.3}
\]

Since `|G^L|<=|G|`, pair symmetry of the original Phi and the conditional R9 energy estimate give

\[
 (Q_N^L)^{\rm Haar}\le C_E b_N N^{-2/p}.
 \tag{5.4}
\]

The exact exchangeable-law square expansion remains R9 (8.1), with `H,A` replaced by `H^L,A^L`. Its deviations satisfy

\[
 |\delta_{2,N}^L|\le4L^2e_{2,N},\qquad
 |\delta_{3,N}^L|\le4L^2e_{3,N},\qquad
 |\delta_{A,N}^L|\le2L^2e_{2,N}.
 \tag{5.5}
\]

Substitution in the exact coefficients (1.4), without omitting the mixed contraction, yields

\[
 \left|Q_N^L-(Q_N^L)^{\rm Haar}\right|
 \le8\nu b_N T L^2{N-1\over N^2}
             [2e_{2,N}+(N-2)e_{3,N}].
 \tag{5.6}
\]

At N=2 the last summand is absent; the coefficient is `4nu b_N T L^2 e_(2,N)`. Using (4.4) and
`(N-1)[2+sqrt(2)(N-2)]/N^2<=sqrt(2)` gives

\[
 \boxed{Q_N^L\le C_E b_NN^{-2/p}
       +C_* b_N\sqrt\nu\,L^2N^{-1/p},
       \qquad C_*=16T\sqrt{2C_0}.}
 \tag{5.7}
\]

The physical normalization is useful here:

\[
 b_N\sqrt\nu=\min(\sqrt\nu,\nu^{-1/2})\le1.
 \tag{5.8}
\]

Consequently, for every deterministic choice

\[
 L_N\longrightarrow\infty,\qquad L_N^2N^{-1/p}\longrightarrow0,
 \tag{5.9}
\]

this actual clipped martingale has `Q_N^(L_N)->0`, uniformly over the task's bounded-noise range. One concrete choice is `L_N=N^(1/(4p))`, for which

\[
 \boxed{Q_N^{L_N}\le C_E b_N N^{-2/p}+C_*N^{-1/(2p)}.}
 \tag{5.10}
\]

For a specified temperature sequence there is a weaker sufficient threshold condition than the uniform choice (5.9):

\[
 L_N\longrightarrow\infty,\qquad
 b_N\sqrt{\nu_N}\,L_N^2N^{-1/p}\longrightarrow0.
 \tag{5.11}
\]

The same conclusion follows directly from (5.7). This permits larger thresholds on sufficiently small-noise sequences while retaining every physical factor.

Thus a nontrivial actual-law part of PO024 has been closed. The estimate follows from the actual gradient dynamics, their iid Haar free energy, exact marginal information inequalities, and the supplied conditional Haar corrector bound. It uses no assumption of iid evolved particles.

## 6. Exact reduction of the full assertion to the large-gradient tail

Define the remaining kernel, its row mean, and its centered version by

\[
 G_t^{>,L}=G_t-G_t^L,\qquad A_t^{>,L}=\int G_t^{>,L}(x,y)dy,
 \qquad H_t^{>,L}=G_t^{>,L}-A_t^{>,L}.
 \tag{6.1}
\]

The remaining vector has magnitude `(|G|-L)_+`; no diagonal trace is assigned.

The exact remaining configuration field is

\[
 v_{i,t}^{>,L}=v_{i,t}-v_{i,t}^L
 =N^{-2}\left[\sum_{j\ne i}H_t^{>,L}(X_i,X_j)-A_t^{>,L}(X_i)\right].
 \tag{6.2}
\]

The difference `M_N^(>,L)=M_(2,N)-M_N^L` is a square-integrable true martingale at every fixed N by the conditional domain theorem and boundedness of the clipped part. Set

\[
 \mathcal T_N(L)=2\nu Nb_N\int_0^T\mathbb E\sum_i|v_{i,t}^{>,L}(X_t)|^2dt.
 \tag{6.3}
\]

The Hilbert-space norm of a predictable field is the square root of its expected scaled bracket. The triangle and reverse triangle inequalities therefore give exactly

\[
 \boxed{\left|\sqrt{Q_N}-\sqrt{\mathcal T_N(L)}\right|
                   \le\sqrt{Q_N^L}.}
 \tag{6.4}
\]

There is no orthogonality assertion about the two martingales. Their cross term is retained and bounded by Cauchy–Schwarz. Combining the clipped estimate and (6.4) proves the necessary-and-sufficient reduction

\[
 \boxed{Q_N\longrightarrow0\quad\Longleftrightarrow\quad
            \mathcal T_N(L_N)\longrightarrow0,
       \qquad L_N\text{ satisfying (5.9) or (5.11)}.}
 \tag{6.5}
\]

In particular (6.5) applies to the explicit threshold in (5.10). The original assertion has not been weakened to a clipped theorem: the exact remaining condition is visible, equivalent to the full target, and still open.

## 7. Every coefficient in the remaining tail is explicit

Expanding (6.2) under the exchangeable actual law gives

\[
 \begin{split}
 \mathcal T_N(L)={2\nu b_N\over N^2}\int_0^T\big[&
 (N-1)\mathbb E|H_t^{>,L}(X_1,X_2)|^2\\
 &+(N-1)(N-2)\mathbb E H_t^{>,L}(X_1,X_2)\cdot H_t^{>,L}(X_1,X_3)\\
 &-2(N-1)\mathbb E H_t^{>,L}(X_1,X_2)\cdot A_t^{>,L}(X_1)
       +\|A_t^{>,L}\|_2^2\big]dt.
 \end{split}
 \tag{7.1}
\]

The triple term is absent at N=2. The pair term, ordered distinct-triple term, mixed term, and one-body square retain their original coefficients and signs. The entire expression is nonnegative, even though individual contractions need not be. This signed quadratic condition can be much weaker than demanding smallness of the separate absolute marginal errors in R9 (10.3).

All terms are integrable at each fixed N. The full gradient is Haar L2 uniformly in time by the conditional domain theorem; the tail is bounded in magnitude by that gradient, and row averaging contracts L2. Haar triple products are integrable by conditional Cauchy–Schwarz. R6's bounded actual densities then give their actual-law integrability, with a possibly exponential finite-N cost. The products share one particle index, but no true coinciding-coordinate value is introduced. At N=2 no third coordinate or third density is requested.

The Haar reference tail already satisfies

\[
 \mathcal T_N^{\rm Haar}(L)\le C_E b_NN^{-2/p}
 \tag{7.2}
\]

for every L, because `|G^{>,L}|<=|G|` in the exact Haar identity. The available full-density comparison is only

\[
 \mathcal T_N(L)\le e^{\kappa(N-1)T}\mathcal T_N^{\rm Haar}(L).
 \tag{7.3}
\]

This is not a uniform transfer. The new entropy argument has already removed the bounded part from this issue; it does not turn (7.3) into a tail estimate.

## 8. A direct attempt to control the tail with the new pair-energy bound

This section records an actual analytic estimate of the remaining term, including where it fails to close the N-limit.

Suppose first that `s>2`. Choose `1<q<s/2`, which also satisfies `q<d/2`, and let `C_(N,q)` be the finite domain constant such that

\[
 |G_t(x,y)|\le C_{N,q}w_q(x-y)
 \quad\text{uniformly for }t\in[0,T],\ 0\le\nu\le\nu_*.
 \tag{8.1}
\]

This is supplied only with possible N dependence. Write `r=s/q>2`; fixed weights satisfy `w_q^r<=C_w w_s`. The elementary inequality

\[
 |G_t^{>,L}|^2\le |G_t|^2\mathbf1_{|G_t|>L}
        \le L^{2-r}C_{N,q}^{r}w_q^r
\]

and the actual pair moment (3.6) imply

\[
 \mathbb E|G_t^{>,L}(X_1,X_2)|^2,\quad\|G_t^{>,L}\|_2^2
 \le C_{s,q}C_{N,q}^{r}L^{2-r}.
 \tag{8.2}
\]

The Haar version uses its finite w_s integral. No actual higher marginal estimate is needed for this inequality. Directly from (6.2), before any cancellation,

\[
 \begin{split}
 \mathcal T_N(L)
 &\le4\nu b_N\int_0^T\left[
       {(N-1)^2\over N^2}\mathbb E|G_t^{>,L}(X_1,X_2)|^2
                       +\|A_t^{>,L}\|_2^2\right]dt\\
 &\le8\nu b_NT C_{s,q}C_{N,q}^{r}L^{2-r}.
 \end{split}
 \tag{8.3}
\]

The first line follows from `|sum_(j!=i)G_ij^(>,L)-N A_i|^2<=2(N-1)sum_(j!=i)|G_ij^(>,L)|^2+2N^2|A_i|^2`; one-body Haar invariance supplies the A norm, and Jensen gives `||A^(>,L)||_2^2<=||G^{>,L}||_2^2`.

With `L_N=N^(1/(4p))`, (8.3) would close the tail if

\[
 \nu_N b_N C_{N,q}^{s/q}N^{-(s/q-2)/(4p)}\longrightarrow0.
 \tag{8.4}
\]

This is a precise sufficient conditional criterion, not a proved temperature subrange: the supplied THM028 gives finiteness of `C_(N,q)` for every N but no N-growth estimate that verifies (8.4). Its construction cannot be silently read as providing a uniform gradient constant.

For `0<s<=2`, the same route has an earlier algebraic obstruction: every admitted q is greater than one, so `s/q<=2`. The pair-energy moment of order s cannot supply the strictly larger than quadratic gradient moment needed for the tail estimate (8.2). This includes three-dimensional Coulomb. The fixed-N density theorem does make the square integrable, but with precisely the N-dependent cost that (7.3) displays.

More generally, for each fixed N dominated convergence gives `mathcal T_N(L)->0` as `L->infinity`. It does not give this convergence for the simultaneous thresholds constrained by (5.9). Choosing an arbitrarily huge threshold separately for each N can destroy the proved clipped estimate. This is the exact quantifier issue; no exchange of those limits is made.

## 9. Disposition and first unresolved line

The first unproved load-bearing line for the full actual-noise assertion is

\[
 \boxed{\mathcal T_N\big(N^{1/(4(s+2))}\big)\longrightarrow0,}
 \tag{9.1}
\]

with the exact actual-law four-term expression in (7.1). The full statement is equivalent to (9.1), conditional on the supplied domain/Haar prerequisites, by (5.10) and (6.4). A proof of the signed tail suffices; separate absolute pair/triple/mixed bounds are not required.

The available information does not yet prove this line: the reference energy is a Haar estimate; entropy controls bounded tests and has been fully used to prove (5.10); the weighted derivative constants can depend on N; and the remaining full-density comparison has an exponential cost. The new actual pair moment leads to the explicit estimate (8.3) for s>2, but its residual condition (8.4) is unproved. This is a limitation of the completed proof attempt, not a claimed counterexample to the stipulated dynamics or a proof that the theorem is false.

The new marginal bound implies unweighted fixed-marginal total-variation convergence in the explicitly limited regime `beta_N N^(-2/(s+2))->0`. It does not establish the full bracket even in that regime without the tail argument. The clipped result (5.10) needs no such condition because of (5.8). The campaign's old energy-floor condition `beta_N N^(2s/d-1)->0`, microscopic subcriticality `beta_N N^(s/d-1)->0`, and microscopic criticality with finite positive limit remain distinct and are not replaced by this auxiliary entropy condition. At Coulomb the auxiliary entropy factor is order one on critical sequences, which is consistent with the bounded-noise clipped estimate and supplies no unweighted marginal conclusion there.

No full actual-bracket theorem, fluctuation law, critical hierarchy closure, or broader subcritical theorem is promoted. No additional theorem identifier is assigned in this worker lane.

## 10. Checks and reproducible handoff

The checker is newly written for this continuation and imports no prior checker. It uses rational three-symbol exchangeable laws, exact radial clipping, full/clip/tail field expansions, finite positive-Fourier energy tests, exact entropy intervals, and rational normalization/exponent checks. Its finite laws are algebraic diagnostics, not asserted laws of the singular dynamics. Continuous entropy, heat passage and domain claims are proved above or are identified as conditional; computations do not replace them.

The issued run passes **20,300 exact assertions**. The final checklist covers N=2,3 (and N=4), all four finite-N contractions and physical prefactors, nonzero mixed/triple terms, the absence of an X_3 demand at N=2, exact full/clip/tail decomposition and its cross term, initial Haar entropy, entropy marginal factors, clipped law-error coefficients, the Coulomb compensation and Fourier sign, the deleted self-energy factor, the free-energy square's nu powers, constant h, zero noise, and all proposed rate exponents. The README and results JSON record the exact final count and verification commands.

| Claim | Disposition |
|---|---|
| Uniform interaction lower bound (2.8) | PROVED FROM THE SUPPLIED KERNEL NORMALIZATION |
| Actual-law free energy and pair-energy bounds (3.4)–(3.6) | PROVED FROM THE SUPPLIED PARTICLE REALIZATION |
| Marginal entropy and bounded-test transfer (4.1)–(4.4) | PROVED |
| Actual clipped martingale estimate (5.7)–(5.10) | PROVED CONDITIONAL ON THE DOMAIN AND R9 ENERGY PREREQUISITES |
| Exact necessary-and-sufficient tail reduction (6.5), with (7.1) | PROVED CONDITIONAL ON THOSE PREREQUISITES |
| Pair-energy tail estimate (8.3), s>2 | PROVED, RETAINING ITS N-DEPENDENT DOMAIN CONSTANT |
| Full expected actual bracket tends to zero | OPEN: first unproved line (9.1) |

The input/output manifests and archive preserve this completed reduction and its unresolved line. A later correction must be a new superseding artifact rather than an edit of an issued seal.
