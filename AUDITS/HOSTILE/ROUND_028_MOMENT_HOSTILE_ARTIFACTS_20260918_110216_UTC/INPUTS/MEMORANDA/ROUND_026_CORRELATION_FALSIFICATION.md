# Round 026 — actual critical correlation: the two-label overlaps vanish

TASK111. Issued 2026-09-18 UTC, isolated worktree
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r026-correlation-falsification`,
provisioned base `06bf56dae256085646228aa28159210b567bf409`.

**NEW QUANTITATIVE CANCELLATION, SELF-CHECKED ONLY. THM046 and the actual
critical signed-correlation target remain OPEN. No admitted positive-limsup
witness is proved.**

The two-label overlap part of the frozen signed-correlation remainder
vanishes under the original dynamics. The current overlap is bounded by
C times N to the power minus one half; the current/initial overlap is
bounded by C times N to the power minus one quarter times the square root
of one plus log N. These are uniform on a fixed finite horizon and a fixed
critical parameter window. Consequently only the weighted correlation
involving three distinct particle labels can carry a nonzero limiting
signed remainder.

The new ingredient is an actual-law small-ball estimate for one current
pair, obtained from the exact energy sign and a positive heat remainder.
It bounds the second moment of the heat-truncated source by a logarithm
at the microscopic heat scale. A separate exact Fourier identity controls
the current overlap, including its smooth self subtraction. Cauchy--Schwarz
then compares the mixed initial overlap with the current overlap using
actual tagged displacement. The argument does not square the untruncated
singular source, assume a positive-time product law, or use the candidate
Round025 uniform-integrability/equivalence theorem.

## 1. Frozen target, negation, and precise new assertion

Let the unit torus be \(\mathbb T^4\), with Haar mass one, and put
\(e_k(x)=\exp(2\pi i k\cdot x)\), \(c=4\pi^2\). The kernel and particles
are exactly
\[
 \widehat g(0)=0,\quad \widehat g(k)=|k|^{-2}\ (k\ne0),\quad K=-\nabla g,
\]
\[
 dX_i=B_i(X)dt+\sqrt{2\nu}\,dW_i,\qquad
 B_i=N^{-1}\sum_{j\ne i}K(X_i-X_j),\qquad \nu=\beta^{-1}>0.       \tag{1.1}
\]
The initial vector is iid Haar and independent of all independent standard
Brownian drivers. Fix \(k\in\mathbb Z^4\setminus\{0\}\) and finite
\(T\ge0\). Write
\[
 Z_k(t)=N^{-1}\sum_i e_k(X_i(t)),\quad \ell_k=c|k|^2,\quad
 a_k=c+\nu\ell_k,\quad \widetilde a_k=a_k-c/N,\quad A_k=e^{-a_kT}.
\]
The singular centered pair kernel is
\[
 J_k(x,y)=K(x-y)\cdot(\nabla e_k(x)-\nabla e_k(y)),\qquad
 j_k(x,y)=J_k(x,y)+c(e_k(x)+e_k(y)),\quad x\ne y.                 \tag{1.2}
\]
Every pair sum below deletes equal labels. Define the four exact expectations
\[
\begin{aligned}
 A_2(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(t))}],\\
 A_3(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(t))}],\\
 B_2(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(0))}],\\
 B_3(t)&=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(0))}].
\end{aligned}                                                       \tag{1.3}
\]
The three-label expressions are absent when N=2. Put
\[
 F_N=\frac{N-1}{N}A_2+\frac{(N-1)(N-2)}{2N}A_3,\qquad
 G_N=\frac{N-1}{N}B_2+\frac{(N-1)(N-2)}{2N}B_3,
\]
\[
 \mathcal R_N=\int_0^T\{e^{-2\widetilde a_k(T-t)}F_N(t)
              -A_ke^{-\widetilde a_k(T-t)}G_N(t)\}\,dt.           \tag{1.4}
\]
The primary target is \(\Re\mathcal R_N(k,T)\to0\) for every fixed
nonzero k, fixed finite T, and every sequence
\(\lambda_N=\beta_N/\sqrt N\to\lambda\in(0,\infty)\), under (1.1).
Its exact admitted negation is existence of one such fixed k,T,lambda and
sequence with positive limsup of \(\Re\mathcal R_N\). Section 7
reconstructs why the negative part is asymptotically zero. A changing
mode, shrinking horizon, altered initial preparation, static law, or
failure of an unrelated stronger estimate is not this negation.

For THM046 the literal statistic is
\[
 P_N[J]=\frac1{2N^2}\sum_{i\ne j}J(X_i,X_j)
 -\frac1N\sum_i\int J(X_i,y)dy+\frac12\iint J,
\]
with the original response \(Q_u^\nu e_k=e^{-a_ku}e_k\) and constants
preserved, and scale \(\sqrt{N\min(\beta_N,1)}\). For each fixed real smooth h, its exact assertion is
\[
 \sqrt{N\min(\beta_N,1)}\,\mathbb E\left|\int_0^T
 P_N[J^{Q_{T-t}^{\nu_N}h}](X(t))\,dt\right|\longrightarrow0.
\]
Its negation requires a fixed such h,T,lambda and an admitted critical
sequence with positive limsup of this displayed nonnegative quantity.
The finite initial segment with beta below one retains the min factor.
This assertion and negation remain unresolved.
The equivalence in the supplied THM049 is a candidate under independent
review; this report does not need THM048 or the L1-to-L2 direction of that
equivalence. We prove the new cancellation directly for (1.3)--(1.4).

Here is the whole new bounded assertion. For each fixed k,T and
\(0<\lambda_-\le\lambda_+<\infty\), there is a finite C, depending only
on these data and the fixed kernel, such that for every N>=2 and
\(\lambda_-\le\beta/\sqrt N\le\lambda_+\),
\[
 \sup_{0\le t\le T}|A_2(t)|\le C N^{-1/2},\qquad
 \sup_{0\le t\le T}|B_2(t)|
       \le C N^{-1/4}\sqrt{1+\log N}.                            \tag{1.5}
\]
Let \(\mathcal R_N^{(2)}\) denote (1.4) with the A3,B3 terms omitted,
and define
\[
 \mathcal R_N^{(3)}=\frac{(N-1)(N-2)}{2N}
  \int_0^T\{e^{-2\widetilde a_k(T-t)}A_3(t)
                 -A_ke^{-\widetilde a_k(T-t)}B_3(t)\}\,dt,        \tag{1.6}
\]
with zero at N=2. Then
\[
 \mathcal R_N=\mathcal R_N^{(2)}+\mathcal R_N^{(3)},\qquad
 |\mathcal R_N^{(2)}|\le C N^{-1/4}\sqrt{1+\log N}.              \tag{1.7}
\]
Thus the frozen signed target, and its positive-limsup negation, are
respectively equivalent to those for \(\Re\mathcal R_N^{(3)}\).
The precise new claim is the conjunction (1.5)--(1.7), not decay of (1.6).
Its exact negation is an admitted fixed k,T,window for which no such C
works for all the specified N,beta, or failure of the exact decomposition
or the stated asymptotic equivalence. Failure of a construction route is
not its negation.

## 2. Source preflight and reconstruction of the actual-law inputs

All 17 allowlisted files passed the supplied SHA-256 manifest before
substantive mathematical use and were copied byte-for-byte into the
packet. The exposure record gives the actual displayed ranges, including
one truncated Round025 output. No current Round026 narrative, constructor
result, code, current audit, state, history, memory file, other worktree,
or nonallowlisted mathematical source was read. No imported external
literature theorem is needed. Historical status labels are not promoted.

The source normalization is checked from the permitted Round004 heat
argument and frozen Round001 model. With the periodized Euclidean heat
kernel \(p_u\), whose Fourier multiplier is \(e^{-cu|m|^2}\),
\[
 g=c\int_0^\infty(p_u-1)du=|z|^{-2}+H(z)\quad\hbox{locally},
 \qquad H\in C^\infty,\qquad \operatorname{div}K=c(\delta_0-dz). \tag{2.1}
\]
The Fourier integral is \(c/(c|m|^2)=|m|^{-2}\). The central Gaussian
integral gives coefficient one; differentiated noncentral translates at
small times and the large-time remainder are integrable. The local
outward flux is \(2|\mathbb S^3|=c\), and zero total Fourier mass supplies
the constant compensation. Consequently \(K\in L^1\), is odd, and
\(\Delta g=c\) only on the punctured torus. Also \(g_*:=\inf g> -\infty\).

For completeness, the exact actual-law arguments needed from the allowed
Round006, Round010 and Round016 proofs are reconstructed here. Set
\[
 H_N=N^{-1}\sum_{i<j}g(X_i-X_j),\qquad B=-\nabla H_N.
\]
The shift \(H_N-(N-1)g_*/2\) is a sum of nonnegative pair terms diverging
at any partial collision. Its sublevels are compact and separated from
collisions. Smooth local force cutoffs give pathwise unique solutions up
to these exits. Stopped Ito, with both coordinates of every unordered
pair differentiated, gives
\[
 \Delta_{4N}H_N=c(N-1),\qquad
 H_N(X_t)+\int_0^t\sum_i|B_i|^2du
 =H_N(X_0)+\nu c(N-1)t+M_E(t),
\]
\[
 M_E(t)=\sqrt{2\nu}\sum_i\int_0^t\nabla_iH_N\cdot dW_i,
 \qquad \langle M_E\rangle_t=2\nu\int_0^t\sum_i|B_i|^2du.       \tag{2.2}
\]
Initially this is stopped. The expected shifted energy bounds the exit
probability at height R by a finite numerator divided by R. This proves
noncollision. Fatou gives finite expected total-force action; stochastic
isometry then removes the stopping in L2 for the martingale. Localization
and the integrable nonnegative terms remove it from the identity. Since
initial iid Haar gives \(\mathbb EH_N(X_0)=0\),
\[
 \mathbb EH_N(X_t)+\mathbb E\int_0^t\sum_i|B_i|^2du
       =\nu c(N-1)t.                                           \tag{2.3}
\]
No individual force-square or initial energy variance is inferred.

A separate fact is the actual sign
\[
                       \mathbb EH_N(X_t)\le0.                  \tag{2.4}
\]
To justify it, first use a fixed heat cutoff delta in both the smooth
force and smooth energy. The positive smooth density from initial density
one satisfies the smooth periodic Fokker--Planck equation. Its entropy
and energy have the exact dissipation
\[
 \frac d{dt}\left(\nu\int F^\delta\log F^\delta
                     +\int H_N^\delta F^\delta\right)
 =-\int F^\delta|\nabla H_N^\delta+\nu\nabla\log F^\delta|^2\le0.
\]
Both initial quantities vanish, and entropy is nonnegative on a space
of Haar mass one. A singular path has positive minimum separation on a
fixed finite horizon. Same-noise local C1 convergence of the heat drifts
and Gronwall give uniform path convergence at each fixed N,nu,T as
delta tends to zero. Since \(H_N^\delta\ge(N-1)g_*/2\), Fatou yields
(2.4). The singular and heat limits are not interchanged with N.

Permutation equivariance gives exchangeability; common translations give
one-body Haar marginals. Neither gives a product law at positive time.
In particular
\[
 \mathbb Eg(X_1(t)-X_2(t))\le0,\qquad
 \mathbb E|g(X_1(t)-X_2(t))|\le2|g_*|.                           \tag{2.5}
\]
The second bound follows from \(|g|\le g+2|g_*|\). Since
\(|j_k(x,y)|\le C_k(1+\operatorname{dist}(x-y,0)^{-2})\), it also
proves the absolute time integrability of all four expectations (1.3),
including the mixed initial factors of modulus one. No joint density of
current and initial coordinates is assumed.

## 3. Positive heat remainder and a quantitative actual-pair small-ball bound

All cutoffs in the rest of the proof are auxiliary observable cutoffs;
the dynamics and initial law remain (1.1). For \(0<r\le1\) let
\[
 g_r=p_r*g=c\int_r^\infty(p_u-1)du,
 \qquad q_r=c\int_0^r p_u\,du\ge0.
\]
Then, off zero,
\[
 g=g_r+q_r-cr,\qquad
 a_r(m):=\widehat g_r(m)=|m|^{-2}e^{-cr|m|^2}>0\ (m\ne0),
 \quad \widehat g_r(0)=0,
\]
\[
 0\le g_r(0)=\sum_{m\ne0}a_r(m)\le C/r.                        \tag{3.1}
\]
The last estimate follows by summing the Gaussian lattice bound, or
integrating \(p_u(0)\le Cu^{-2}\) on (r,1) and the exponentially decaying
remainder on (1,infinity).

Put \(M_r(t)=\mathbb E\sum_{m\ne0}a_r(m)|Z_m(t)|^2\ge0\).
Exact deletion of the smooth self diagonal gives
\[
 \mathbb Eg_r(X_1-X_2)
 =\frac N{N-1}M_r-\frac{g_r(0)}{N-1}.
\]
Combining this equality with (2.5) and the positive q_r gives the stronger
coupled inequality
\[
 \boxed{\frac N{N-1}M_r(t)+\mathbb E q_r(X_1(t)-X_2(t))
         \le\frac{g_r(0)}{N-1}+cr.}                            \tag{3.2}
\]
Every coefficient is finite-N. In particular, uniformly in time and
positive diffusivity,
\[
 M_r(t)\le C((Nr)^{-1}+r),\qquad
 \mathbb E q_r(X_1(t)-X_2(t))\le C((Nr)^{-1}+r).                 \tag{3.3}
\]
This is stronger than merely bounding the expectation of an arbitrary
weighted energy; its two nonnegative terms have explicit Fourier/heat
origins. It uses the actual sign (2.4).

Choose a fixed \(R_0<1/8\). If \(R\le R_0\) and
\(\operatorname{dist}(z,0)\le R\), the central heat kernel on
\(u\in[R^2/2,R^2]\) gives
\(q_{R^2}(z)\ge c_0R^{-2}\) for a fixed \(c_0>0\). Thus (3.3) yields
\[
 \boxed{\mathbb P(\operatorname{dist}(X_1(t)-X_2(t),0)\le R)
           \le C(R^4+N^{-1}),\qquad 0<R\le R_0.}               \tag{3.4}
\]
It is a bound for a fixed current pair at a deterministic time, uniform
in time; it is not a pathwise minimum-separation estimate. Its N inverse
term must be kept at arbitrarily small R. It does not imply a finite
second moment of the singular source.

The same splitting proves the floor used below without an external
premise. Configurationwise
\[
 H_N\ge\frac N2\sum_{m\ne0}a_r(m)|Z_m|^2
           -\frac12g_r(0)-\frac{N-1}{2}cr.
\]
Choosing r=N to the power minus one half gives \(H_N\ge-C\sqrt N\).
Combining with (2.3), exchangeability, Cauchy--Schwarz in time and the
Brownian L2 maximal inequality gives consistent-lift displacement
\[
 \mathbb E\sup_{t\le T}\operatorname{dist}(X_i(t),X_i(0))^2
                    \le C_T(N^{-1/2}+\nu).                     \tag{3.5}
\]
The complete drift square, not a sum of separate pair-force squares,
enters this proof. Equation (3.5) alone was already insufficient in the
older route; the new small-ball and truncated-square estimates provide
the missing weight control for an individual overlap.

## 4. Observable truncation: exact centering, error, and logarithmic square

Let \(K_r=-\nabla g_r\), \(d_{k,r}=c e^{-r\ell_k}\), and define
\[
 J_{k,r}(x,y)=K_r(x-y)\cdot(\nabla e_k(x)-\nabla e_k(y)),\qquad
 j_{k,r}=J_{k,r}+d_{k,r}(e_k(x)+e_k(y)).                         \tag{4.1}
\]
The coefficient is d_(k,r), not c. The smooth divergence is
\(c(p_r-1)\); integration by parts gives
\(\int J_{k,r}(x,y)dy=-d_{k,r}e_k(x)\). Both rows of j_(k,r)
therefore vanish exactly. Its smooth diagonal is
\(j_{k,r}(x,x)=2d_{k,r}e_k(x)\); the singular kernel is never assigned
this or any other diagonal value.

The periodized Gaussian estimate
\(\operatorname{dist}(z,0)|\nabla p_u(z)|\le C p_{2u}(z)\),
proved termwise by using \(\operatorname{dist}(z,0)\le|z+n|\)
and \(v e^{-v}\le C e^{-v/2}\), gives
\[
 |J_k-J_{k,r}|\le C_k q_{2r}(x-y),\qquad |c-d_{k,r}|\le C_k r.
\]
For \(0<r\le1/2\), (3.3) hence proves
\[
 \boxed{\sup_t\mathbb E|j_k(X_1(t),X_2(t))-j_{k,r}(X_1(t),X_2(t))|
                         \le C_k(r+(Nr)^{-1}).}                \tag{4.2}
\]
The background error has been retained; no heat cutoff changes the
original response or source in the target.

Here is a separate pointwise bound needed for squares. For a fixed small
r_0>0 and every \(0<r\le r_0\), the local Euclidean retained potential is
\[
 |z|^{-2}(1-e^{-|z|^2/(4r)}).
\]
Its radial force satisfies
\[
 |z|\,|K_r^{\rm Eucl}(z)|
 =2|z|^{-2}\{1-(1+u)e^{-u}\},\qquad u=|z|^2/(4r).
\]
The brace is bounded by \(\min(1,u^2/2)\). Periodic noncentral heat
terms and the large-time remainder have uniformly bounded derivatives
in a fixed ball; away from that ball all terms are uniformly bounded.
Consequently, writing \(R=\operatorname{dist}(x-y,0)\),
\[
 |j_{k,r}(x,y)|\le C_k\{1+\min(r^{-1},R^{-2})\}.               \tag{4.3}
\]
The bound includes the two smooth row terms. It remains valid on the
smooth diagonal by continuity.

Apply layer cake to \(\min(r^{-2},R^{-4})\). Above a fixed lower
threshold, (3.4) gives
\(\mathbb P(R^{-4}>u)\le C(u^{-1}+N^{-1})\). Integrating up to
r to the power minus two yields the uniform actual-law estimate
\[
 \boxed{\sup_t\mathbb E|j_{k,r}(X_1(t),X_2(t))|^2
       \le C_k\{1+\log(1/r)+(Nr^2)^{-1}\}.}                   \tag{4.4}
\]
Choose once and for all a fixed \(0<r_*\le\min(r_0,R_0^2/8,1/64)\)
and then
\[
                         r_N=r_*N^{-1/2}.                     \tag{4.5}
\]
Equations (4.2) and (4.4) become, respectively, \(C_kN^{-1/2}\)
and \(C_k(1+\log N)\). This is the exact cutoff balance. Sending the
cutoff to zero at a fixed N in (4.4) is not allowed to discard its
\((Nr^2)^{-1}\) term. No finite untruncated source variance is claimed.

## 5. New exact spectral overlap identity and current cancellation

Define
\[
 A_{2,r}(t)=\mathbb E[j_{k,r}(X_1(t),X_2(t))\overline{e_k(X_1(t))}].
\]
The integrand depends only on z=x-y. Write its smooth Fourier expansion
as \(\sum_m b_{k,r}(m)e_m(z)\), setting \(a_r(0)=0\). Multiplying
out (4.1), with its exact response coefficient, gives
\[
 b_{k,r}(m)=c\{(k\cdot m)a_r(m)-(k\cdot(m+k))a_r(m+k)\}
             +d_{k,r}(\mathbf1_{m=0}+\mathbf1_{m=-k}).          \tag{5.1}
\]
In particular
\[
 b_{k,r}(0)=b_{k,r}(-k)=0,\qquad
 \sum_{m\ne0}b_{k,r}(m)=2d_{k,r}.                              \tag{5.2}
\]
The sum is absolutely convergent at each fixed r; its value follows
also by evaluating the smooth diagonal in (4.1). This is where silently
dropping the self term would make the exact identity false.

For each fixed k and \(0<r\le r_0\),
\[
                  |b_{k,r}(m)|\le C_k a_{r/8}(m),\qquad m\ne0.\tag{5.3}
\]
Here is a proof avoiding any false bounded ratio of shifted Gaussian
weights. For \(|m|\ge2|k|\), apply the mean-value formula to
\(F_r(x)=x|x|^{-2}e^{-cr|x|^2}\) on the segment from m to m+k.
On that segment \(|x|\ge|m|/2\), and
\[
 |DF_r(x)|\le C(|m|^{-2}+cr)e^{-cr|m|^2/4}
             \le C|m|^{-2}e^{-cr|m|^2/8}.
\]
The last step is \((1+u)e^{-u/4}\le C e^{-u/8}\). Multiplication
by \(c|k|^2\) proves (5.3) there. The remaining nonzero m form a finite
set depending on k; their denominator \(a_{r/8}(m)\) has a positive
lower bound for \(0<r\le r_0\), while the numerator is bounded. The
m=0 coefficient is zero and is excluded. The response deltas in (5.1)
are included in this finite-set check.

For any exchangeable current law, direct empirical label counting gives
\[
 \mathbb E e_m(X_1-X_2)
             =\frac{N\mathbb E|Z_m|^2-1}{N-1}\quad(m\ne0).
\]
Thus, with all coefficients retained,
\[
 \boxed{A_{2,r}(t)=\frac N{N-1}
      \mathbb E\sum_{m\ne0}b_{k,r}(m)|Z_m(t)|^2
                   -\frac{2d_{k,r}}{N-1}.}                   \tag{5.4}
\]
Combining (5.3), (3.3) at r/8, and \(0\le d_{k,r}\le c\),
\[
 |A_{2,r}(t)|\le C_k\{r+(Nr)^{-1}\}+\frac{2c}{N-1}.
\]
The same bound for the singular A2 follows from (4.2). With (4.5), this
proves the first inequality in (1.5). Its constant is actually independent
of nu and T. No weighted positive-definiteness of j is asserted: the
absolute Fourier coefficient comparison is to the explicitly positive
heat energy.

## 6. New current/initial overlap cancellation

The exact difference is
\[
 B_2(t)-A_2(t)=\mathbb E\big[j_k(X_1(t),X_2(t))
           \{\overline{e_k(X_1(0))}-\overline{e_k(X_1(t))}\}\big].
\]
Replace j by j_(k,r) only in this difference. The replacement error is
at most twice (4.2), since each phase has modulus one. Cauchy--Schwarz,
(4.4), and (3.5) give
\[
\begin{split}
 |B_2(t)-A_2(t)|\le{}& C_k\{r+(Nr)^{-1}\}\\
 &+C_{k,T}\{1+\log(1/r)+(Nr^2)^{-1}\}^{1/2}
                           (N^{-1/2}+\nu)^{1/2}.              \tag{6.1}
\end{split}
\]
Indeed \(\mathbb E|e_k(X_1(t))-e_k(X_1(0))|^2\) is bounded by
\(\ell_k\) times the displacement square in (3.5). No independence of
the phase difference and the source is used. No two-time density appears.
All estimates hold at every deterministic t with one common constant.

At r=r_N, and on the fixed critical window
\(\nu\le\lambda_-^{-1}N^{-1/2}\), (6.1) and Section 5 give exactly
the second inequality in (1.5). The logarithm is harmless after the
N to the power minus one quarter factor, but is not deleted. The same
Cauchy--Schwarz estimate for a third tag would be far too weak after the
order-N coefficient in (1.6), so this proof does not silently extend to
the remaining triple term.

## 7. Exact mode identity, coefficients, and the sharper remaining line

This section reconstructs only the needed finite-N part of the supplied
THM049 candidate; no Round025 tail or L1/L2 equivalence is used.
The full divergence measure in (2.1) gives
\(\int J_k(x,y)dy=-ce_k(x)\) and double integral zero. Therefore
\[
 U_N^k=(2N^2)^{-1}\sum_{i\ne j}j_k(X_i,X_j),\qquad
 P_N[J_k]=U_N^k+(c/N)Z_k,
\]
\[
 dZ_k=-\widetilde a_kZ_kdt+U_N^kdt+dM_k,
 \quad M_k=\frac{\sqrt{2\nu}}N\sum_i\int\nabla e_k(X_i)\cdot dW_i.
                                                                    \tag{7.1}
\]
The c/N is positive. Each particle has N-1 distinct partners in each
orientation; the ordered half is unchanged. The exact brackets are
\[
 d\langle M_k,\overline M_l\rangle_t
      =(2\nu/N)c(k\cdot l)Z_{k-l}(t)dt,
 \qquad d\langle M_k,\overline M_k\rangle_t=(2\nu\ell_k/N)dt.    \tag{7.2}
\]
The pair-source drift has finite expected absolute time integral by
(2.5). Applying Ito up to energy exits and passing by this L1 bound and
bounded martingale integrands proves the genuine unstopped identities.

There are 2N(N-1) overlap triples in \(N U_N^k\overline Z_k\)
and N(N-1)(N-2) distinct triples. Their common denominator is 2N squared.
Symmetry of j and exchangeability identify the two overlap terms, also
when the conjugate tag is initial. Consequently
\[
 N\mathbb E(U_N^k\overline{Z_k(t)})=F_N(t),\qquad
 N\mathbb E(U_N^k\overline{Z_k(0)})=G_N(t),                    \tag{7.3}
\]
with exactly (1.4). No nonexistent third label is assigned when N=2.
Writing \(V=N\mathbb E|Z_k(t)|^2\) and
\(R=N\mathbb E(Z_k(t)\overline{Z_k(0)})\), product Ito gives
\[
 V'=-2\widetilde a_kV+2\nu\ell_k+2\Re F_N,\qquad
 R'=-\widetilde a_kR+G_N,\qquad V(0)=R(0)=1.                   \tag{7.4}
\]
Both current response slots occur in V, only one in R. Initial
measurability makes the relevant martingale mean zero; initial/final
independence is not assumed. Solving the two scalar equations proves
\[
 N\mathbb E|Z_k(T)-A_kZ_k(0)|^2
 =(e^{-\widetilde a_kT}-e^{-a_kT})^2
 +\frac{\nu\ell_k}{\widetilde a_k}(1-e^{-2\widetilde a_kT})
 +2\Re\mathcal R_N.                                          \tag{7.5}
\]
Since \(\widetilde a_k\ge c/2\), the explicit terms are nonnegative,
respectively O(N to the power minus two) and O(N to the power minus one
half) on the critical window. In particular the negative part of the
signed remainder tends to zero.

Decomposing F and G in (7.3) now gives (1.6)--(1.7) exactly. All exponential
weights have modulus at most one, so (1.5) yields the error in (1.7)
without differentiating a singular source. The strictly sharper remaining
load-bearing estimate is
\[
 \boxed{\Re\left[\frac{(N-1)(N-2)}{2N}
  \int_0^T\{e^{-2\widetilde a_k(T-t)}A_3(t)
          -A_ke^{-\widetilde a_k(T-t)}B_3(t)\}\,dt\right]\to0.} \tag{7.6}
\]
No decay rate, separate decay of A3/B3, or finite hierarchy closure is
asserted. The target and its fixed-mode positive-limsup negation are
unchanged: (1.7) makes them equivalent to (7.6) and its positive-limsup
negation. Without using the supplied candidate UI theorem, an original
L1 source counterexample would force an endpoint L2 defect and hence a
positive triple remainder along a subsequence; the converse transfer
back to L1 is not needed or newly certified here.

## 8. Falsification attempt, diagnostic, and adversarial self-check

The concrete failure mechanism tested was a nonvanishing two-label
current/initial overlap produced by near-collision force events, despite
macroscopic tagged displacement. An unweighted displacement estimate
alone cannot rule it out: the singular source has infinite initial
second moment. The new attempt retains the force weight and its cutoff
error. Equations (3.4), (4.4), and (6.1) rule out precisely this mechanism
as a contribution to the frozen signed remainder. They do not rule out
a collective three-label contribution with its order-N multiplicity.

The fresh `diagnostic.py` uses only the Python standard library. Its
main finite-Fourier checks use exact rational arithmetic, including
Gaussian rational values of characters at quarter-period coordinates.
Two positive finite Fourier kernels, four fixed modes, and configurations
with N=2,3,4,5 are tested in two coordinates embedded in the four-torus.
The common factor c=(2 pi) squared is divided out in this diagnostic.
It compares literal pair sums with an independently assembled Fourier
overlap, exact energy self subtraction, source backgrounds, current and
mixed initial label counts, and the mixed-overlap Cauchy--Schwarz bound.
No earlier checker or code was read.

An exact dyadic four-dimensional radial diagnostic gives a truncated
square growing linearly with the number of dyadic scales. A separate
mass-one-over-N atom tests the finite-N cutoff error. These are solvable
majorant tests, not replacements for the actual dynamic law. A finite
lattice sweep checks the heat divided-difference envelope numerically;
it supports, but does not certify, the all-frequency analytic proof
in Section 5. It uses ordinary double arithmetic with a conservative
bound and records the observed maximum.

The executed diagnostic passed **343,521 assertions in 17 categories,
with 15 distinct nonvacuous mutation controls**. Failures caught include
using c rather than the true heat response, reversing the background,
removing or reversing the residual row, deleting or changing the overlap
self subtraction, the ordered half and falling-factorial denominator,
missing an overlap or doubling the distinct-label term, replacing an
initial phase by a current phase, omitting the energy self term, deleting
the growing logarithm, and dropping the finite-N cutoff term. Each
recorded mutation has an explicit nonzero witness in the result file.
There was no SDE discretization, sampling seed, installation, or claimed
numerical asymptotic theorem. The first executed mathematical diagnostic passed. A later read-only
comparison harness failed because JSON reload converts tuple-valued witness
metadata to lists; its canonical JSON comparison was corrected and rerun.
The initial failed harness and failure record are preserved. No mathematical
assertion failed in that harness run.

| Adversarial challenge | Resolution and precise limit |
|---|---|
| Is positive-time product Haar used? | No. Actual energy sign, exchangeability, and a positive Fourier energy suffice. |
| Is the singular source squared? | No. Only j at positive heat cutoff is squared; the original difference is controlled in L1. |
| Is the current/initial law presumed to have a density? | No. Cauchy--Schwarz uses random variables and actual displacement. |
| Does pointwise nonnegative weighting imply PSD? | No. Only explicit heat Fourier weights are positive; the overlap multiplier is dominated coefficientwise. |
| Is the smooth diagonal lost? | No. It is exactly 2 d_(k,r), and gives the minus 2 d_(k,r)/(N-1) in (5.4). |
| Is the heat response treated as Coulomb response? | No. It is c exp(-r ell_k), and the difference is included in (4.2). |
| Is a shifted Gaussian weight ratio falsely bounded? | No. The proof changes the comparison scale to r/8 and proves the divided-difference estimate. |
| Does the small-ball estimate survive below microscopic scale? | Yes with its N inverse term; that term cannot be dropped. |
| Are law approximation and N limits exchanged? | No. The physical heat limit is taken at fixed N,nu,T. Later r_N truncates only an observable. |
| Does the new pair bound settle the triple term? | No. Multiplying the analogous coarse bound by its order-N coefficient fails. |
| Does a mode variance failure alone certify original L1 failure? | Not in this proof. The candidate Round025 UI assertion is not a premise. |
| Is this a blind audit of Round025 or a current constructor? | No. It is a distinct isolated construction/falsification lane, self-checked only. |

## 9. Recoverable handoff

| Item | Disposition |
|---|---|
| THM046 and frozen critical signed target | OPEN; neither proved nor disproved. |
| Actual current-pair small-ball and truncated-square estimates | PROVED CANDIDATE HERE / SELF-CHECKED. |
| Current and current/initial overlap bounds (1.5) | PROVED CANDIDATE HERE / SELF-CHECKED. |
| Two-label-only critical failure mechanism | RULED OUT by the quantitative contribution bound (1.7). |
| Three-distinct-label signed cancellation (7.6) | OPEN; exact remaining line with all finite-N weights retained. |
| Supplied THM048 and full THM049 equivalence | NOT USED AS PREMISES; no new certification or status change. |
| Independent audit or full hierarchy/fluctuation theorem | NOT CLAIMED. |

Root should give the whole new conjunction and its exact source packet
to a fresh reconstruction/hostile audit. The checks most likely to carry
a subtle error are (3.2), the small-ball-to-square layer cake, the heat
response in (4.1), the Fourier self subtraction (5.4), and the comparison
of mixed phases in (6.1). The next mathematical construction target is
exactly (7.6), with fixed original k,T and actual iid initial law.

The named packet contains this complete report, all 17 permitted input
copies and original manifest, precise read/exposure record, full proof
claim, new code/results/history, README, exact regular-member/digest
inventories, and a portable read-only verifier. Issued files and archive
are sealed read-only; corrections require a separate artifact. Only the
assigned memorandum, artifact directory, and named sibling archive/seals
were written. No canonical/input edit, child, current audit/state/history/
memory read, other-worktree read, external source, commit, push,
installation, or remote change occurred.
