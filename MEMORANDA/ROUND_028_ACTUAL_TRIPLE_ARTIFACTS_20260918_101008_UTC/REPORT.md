# Round 028 — fourth moments and localization of the actual three-label gate

TASK119. Ordinary Astra Max construction, 2026-09-18 UTC, isolated worktree
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r028-triple-construction`,
base `ef438b612f732d21af1fa1756dd7559ef63c6d61`.

**NEW ACTUAL-LAW ESTIMATES AND A SHARPER EXACT REDUCTION; SELF_CHECKED ONLY.
THM046 remains OPEN. No admitted positive-limsup witness is proved.**

The actual scaled empirical Fourier modes, endpoint defects, and integrated
sources have uniform fourth moments on each bounded positive critical
window. This follows from an exact fourth-moment graph expansion for an
auxiliary clipped initial energy, not from squaring the singular energy.
The energy martingale is retained and estimated on a time-zero event.

These fourth moments make the three-label contribution of a heat-smoothed
observable vanish even when its smoothing scale decreases with N. The
dynamics remain the original singular dynamics. The two different time
weights, ordered half, falling factorial, and initial versus current tag
remain literal. In particular, all of the surviving gate can be placed in
the force difference K minus its heat convolution at a specified shrinking
scale. The row correction in that difference also tends to zero, by a
separate exact label calculation. The remaining estimate is still a signed
actual-law correlation; the result supplies neither its decay nor a witness.

## 1. Frozen data, assertion, and negation

Use Haar mass one on the unit four-torus, Fourier characters
\(e_m(x)=\exp(2\pi i m\cdot x)\), and \(c=4\pi^2\). The frozen kernel is
\(\widehat g(0)=0\), \(\widehat g(m)=|m|^{-2}\) for nonzero m,
\(K=-\nabla g\). Actual particles satisfy
\[
 dX_i= B_i(X)dt+\sqrt{2\nu}\,dW_i,
 \qquad B_i=N^{-1}\sum_{j\ne i}K(X_i-X_j),\qquad \nu=\beta^{-1}>0. \tag{1.1}
\]
The starting vector is iid Haar, independent of the independent Brownian
drivers. All asymptotic constants below are uniform for
\[
 N\ge2,\qquad 0<\lambda_-\le\beta/\sqrt N\le\lambda_+<\infty, \tag{1.2}
\]
with fixed window endpoints and fixed finite T. Each convergent critical
sequence eventually lies in such a window. There is no convergence-rate
assumption. Fixed finite initial segments do not change a limit.

For a fixed nonzero k set
\[
 Z_m(t)=N^{-1}\sum_i e_m(X_i(t)),\quad \ell_m=c|m|^2,
 \quad a_m=c+\nu\ell_m,\quad \widetilde a_k=a_k-c/N,
 \quad A_k=e^{-a_kT},\quad u_t=e^{-\widetilde a_k(T-t)}. \tag{1.3}
\]
The original backward response uses a_m, preserves constants, and is never
replaced by a cutoff-dependent eigenvalue. Write
\[
 J_k(x,y)=K(x-y)\cdot(\nabla e_k(x)-\nabla e_k(y)),\qquad
 j_k=J_k+c(e_k(x)+e_k(y)),\quad x\ne y. \tag{1.4}
\]
For N at least three let A3 and B3 have exactly the THM049 meanings,
with the third phase respectively at time t and time zero, and put
\[
 p_N=\frac{(N-1)(N-2)}{2N},\qquad
 \mathcal R_N^{(3)}=p_N\int_0^T
   \{u_t^2 A3(t)-A_k u_t B3(t)\}\,dt. \tag{1.5}
\]
At N=2 this quantity is zero, with no third particle assigned.
The target is its real part tending to zero for every fixed k,T and every
admitted critical sequence. Its exact negation is an admitted fixed
k,T,positive lambda and sequence with positive limsup of that real part.
Changing k or T with N, changing the law, or failing a stronger bound is
not this negation.

The original THM046 remains the expected absolute value of the time integral
of the literal deleted-pair source, scaled by
\(\sqrt{N\min(\beta,1)}\), for each fixed smooth real test. Both Haar rows
and the double background remain in that statistic. The accepted R25 gate
supplies its exact equivalence to THM049. The R26 two-label mechanism is
reproduced below to connect (1.5), without promoting its frozen status label.

## 2. Complete new assertion and exact scope of its negation

For every nonzero integer m and deterministic \(0\le t\le T\), define
\[
 S_{N,m}(t)=\sqrt N\int_0^t
 P_N[J^{Q_{t-s}^{\nu}e_m}](X(s))\,ds,\qquad
 D_{N,m}(t)=\sqrt N\{Z_m(t)-e^{-a_mt}Z_m(0)\}. \tag{2.1}
\]
Complex notation joins the corresponding two real tests. Put
\(w_m=(1+|m|)^{10}\).

**Moment assertion.** There is a finite constant C, depending only on
T, the window (1.2), and the fixed kernel, such that
\[
 \sup_{t\le T}\mathbb E\big[
  |S_{N,m}(t)|^4+|D_{N,m}(t)|^4+|\sqrt N Z_m(t)|^4\big]
       \le C w_m^4. \tag{2.2}
\]
This is a supremum of deterministic-time expectations. It is not the
expectation of a time supremum, and does not assert uniform integrability
of fourth powers. No instantaneous singular source is squared.

**Smoothed three-label assertion.** Let \(g_r=p_r*g\), \(K_r=-\nabla g_r\),
\(d_{k,r}=c e^{-r\ell_k}\), and
\[
 j_{k,r}(x,y)=K_r(x-y)\cdot(\nabla e_k(x)-\nabla e_k(y))
               +d_{k,r}(e_k(x)+e_k(y)). \tag{2.3}
\]
Use this observable in A3 and B3 to define \(\mathcal R_{N,r}^{(3)}\),
but keep the actual process and exactly the weights (1.3), (1.5).
For fixed k and a fixed sufficiently small positive \(r_0\),
\[
 |\mathcal R_{N,r}^{(3)}|
 \le C_{k,T}\left[
    N^{-1/2}r^{-11}
    +N^{-1/4}\{1+\log(1/r)+(Nr^2)^{-1}\}^{1/2}\right],
 \quad 0<r\le r_0. \tag{2.4}
\]
The constant is independent of r,N,beta within these domains. Fix any
\(0<r_*\le r_0\) and take
\[
                         r_N=r_*N^{-1/24}. \tag{2.5}
\]
Then \(|\mathcal R_{N,r_N}^{(3)}|\le C_{k,T,r_*}N^{-1/24}\).
More generally (2.4) tends to zero at \(r=r_*N^{-\delta}\) for every
fixed \(0<\delta<1/22\). No optimal exponent is claimed.

**Force-tail reduction.** Replace j_k in A3 and B3 by just
\[
 J_{k}^{>r}(x,y)=(K-K_r)(x-y)\cdot
                    (\nabla e_k(x)-\nabla e_k(y)) \tag{2.6}
\]
and call the resulting expression with the same p_N,u_t,A_k
\(\mathcal H_{N,r}^{(3)}\). The deleted-label statistic is not silently
recentered: Section 8 calculates its omitted row contribution exactly.
At (2.5),
\[
 \left|\mathcal R_N^{(3)}-\mathcal H_{N,r_N}^{(3)}\right|
                         \le C_{k,T,r_*}N^{-1/24}. \tag{2.7}
\]
Thus the original signed target and its same-fixed-data positive-limsup
negation are respectively equivalent to those for
\(\Re\mathcal H_{N,r_N}^{(3)}\). Neither is established here.

The new assertion is the conjunction (2.2), (2.4), (2.7) and their stated
exact identities. Its logical negation is an admitted datum violating an
identity, or fixed T/window (and fixed k,r_* where specified) for which no
finite constant with the declared dependencies bounds all specified
N,beta,m,t,r, or a mismatch in the resulting limit/positive-limsup
equivalence. The auxiliary fourth-moment identity in Section 4 is asserted
for every even real zero-mean bounded translation kernel and every N;
its negation is a single such finite datum violating that equality.
Failure of the still-open force-tail cancellation is not a negation of
any assertion proved here.

## 3. Source and normalization preflight; actual-law mechanisms retained

All 21 rows of the supplied input manifest passed before mathematical use.
Complete bytes, exact manifest, and a range-specific read/exposure ledger
are in the packet. Only allowed inputs were used; the one misspelled,
nonexistent read and its correction are recorded. R25 whole-gate acceptance
and the complete THM050 root comparison are explicitly supplied provenance.
The present argument does not use a response-gradient estimate. In
particular the accepted fourth-gradient obstruction is not misread as a
fourth-*value*-moment obstruction. No other linked source was followed.

The allowed R4 normalization gives, directly by its Gaussian integral,
\[
 g=c\int_0^\infty(p_v-1)dv=|z|^{-2}+H(z)\ \hbox{locally},\quad
 H\in C^\infty,\quad \operatorname{div}K=c(\delta_0-dz). \tag{3.1}
\]
The Fourier integral is \(c/(c|m|^2)\), and the outward local flux is
\(2|\mathbb S^3|=c\). Thus K is Haar integrable, g has finite lower
bound, and \(\Delta g=c\) only on the punctured torus.

For \(H_N=N^{-1}\sum_{i<j}g(X_i-X_j)\), collision-excluded energy
sublevels give the actual noncolliding process by stopped smooth Itô
calculus. Both coordinates of each unordered pair contribute to
\(\Delta_{4N}H_N=c(N-1)\). The exact unstopped identity is
\[
 H_N(X_t)+A_t=H_N(X_0)+\nu c(N-1)t+E_t,\quad
 A_t=\int_0^t\sum_i|B_i|^2ds,\quad
 \langle E\rangle_t=2\nu A_t,\quad
 E_t=\sqrt{2\nu}\sum_i\int_0^t\nabla_iH_N\cdot dW_i. \tag{3.2}
\]
To justify unstopping, first use the shifted nonnegative energy to bound
exits, then Fatou for A, then isometry for the true energy martingale.
This controls the complete force square, including its cross terms.
It gives no separate pair-force-square integrability.

The positive heat split
\(g=g_r+q_r-cr\), \(q_r=c\int_0^r p_vdv\ge0\), and literal smooth
self subtraction give the deterministic floor \(H_N\ge-C\sqrt N\).
Indeed the two discarded errors are \(g_r(0)/2\le C/r\) and
\(c(N-1)r/2\); choose \(r=N^{-1/2}\).
Initial iid Haar has \(\mathbb EH_N(X_0)=0\). Hence
\[
 \mathbb EA_T\le C\sqrt N+\nu c(N-1)T. \tag{3.3}
\]

At a fixed physical heat cutoff epsilon, smooth free-energy dissipation
from initial density one implies \(\mathbb EH_N^\epsilon(X_t^\epsilon)
\le0\). Same-noise localization and Gronwall give path convergence on a
fixed horizon because each actual path has positive minimum separation.
Heat positivity supplies the common lower bound
\((N-1)\inf g/2\); Fatou proves
\[
              \mathbb EH_N(X_t)\le0. \tag{3.4}
\]
This passage is at fixed N,nu,T before any N limit. Permutation and
translation equivariance give exchangeability and one-body Haar marginals,
not positive-time independence. In particular
\(\mathbb E|g(X_1-X_2)|\le2|\inf g|\). This proves absolute time
integrability of every source paired with a bounded phase below.

One accepted R25 pointwise input is used with its actual dependence:
\[
 \sqrt N|P_N[J^{Q_{t-s}^{\nu}e_m}](x)|
       \le Cw_m\{G+H_N(x)/\sqrt N\},\quad 0\le s\le t\le T. \tag{3.5}
\]
Here G is fixed and the brace is nonnegative for every collision-free
configuration. This is R25 Sections 3, 5, not a variance closure. Its
mechanism is the positive split with retained heat weight
\((1-e^{-v/r})^6\), logarithmic Fourier slope at most 14, and the
commutator bound with seminorm
\(\sum_q|q|(1+|q|)^8|\widehat{\nabla e_m}(q)|\le Cw_m\).
Both self/background errors and the discarded positive heat term are
controlled at r=N to the power minus one half by (3.2)'s energy.
The allowed full R25 proof and its supplied whole-gate receipt support
this exact input; no hidden all-modes L2 estimate is imported.

Finally the literal one-body equation gives
\[
 S_{N,m}(t)=D_{N,m}(t)-L_{N,m,t},\qquad
 L_{N,m,t}=\sqrt{2\nu/N}\sum_i\int_0^t
       \nabla Q_{t-s}^{\nu}e_m(X_i(s))\cdot dW_i(s). \tag{3.6}
\]
Its conjugate bracket is at most \(2\nu T\ell_m\). The original energy
and this martingale have the nonzero cross bracket
\[
 d\langle E,\overline L_{N,m,t}\rangle_s
  =\frac{2\nu}{\sqrt N}\sum_i\nabla_iH_N\cdot
       \overline{\nabla Q_{t-s}^{\nu}e_m(X_i(s))}\,ds. \tag{3.7}
\]
No proof below sets it, or the endpoint/noise cross term, to zero.
Magnitude inequalities suffice. Stopping, (3.2), and bounded gradients
justify (3.6) before moment estimates are applied.

## 4. New exact fourth-moment expansion of the clipped initial energy

Let h be any bounded even real zero-mean translation kernel on a compact
abelian group equipped with Haar probability. For iid Haar \(Y_1,\ldots,Y_N\), set
\[
 H^h=N^{-1}\sum_{i<j}h(Y_i-Y_j),\quad
 \mu_2=\int h^2,\quad \mu_4=\int h^4,\quad
 \tau_h=\int h(z)^2(h*h)(z)dz,\quad
 \chi_h=\int(h*h)(z)^2dz. \tag{4.1}
\]
Then the exact equality is
\[
\begin{split}
 N^4\mathbb E(H^h)^4={}&{N\choose2}\mu_4
   +18{N\choose3}\mu_2^2+36{N\choose3}\tau_h\\
   &+18{N\choose4}\mu_2^2+72{N\choose4}\chi_h. \tag{4.2}
\end{split}
\]
Binomial coefficients are zero if there are too few labels.

Expand the fourth power into ordered quadruples of unordered edges. A
vertex of degree one makes its term zero after integration in that
coordinate, by the zero row. Thus at most four vertices survive. With
two vertices all four edges agree. With three vertices, the surviving
patterns are two doubled edges (three choices of center, six orders)
or a triangle with one edge doubled (three choices, twelve orders).
Their integrals are respectively \(\mu_2^2\) and \(\tau_h\). With four
vertices, the patterns are two disjoint doubled edges (three matchings,
six orders) or a four-cycle (three cycles, twenty-four orders), giving
\(\mu_2^2\) and \(\chi_h\). This exhausts the degree count and proves
all coefficients, including the two distinct occurrences of 18.

Cauchy--Schwarz gives \(\|h*h\|_\infty\le\mu_2\), so
\(|\tau_h|\le\mu_2^2\), \(0\le\chi_h\le\mu_2^2\). Consequently
\[
             \mathbb E(H^h)^4\le C(\mu_4/N^2+\mu_2^2). \tag{4.3}
\]
No independence of overlapping edges is assumed.

Apply this to the auxiliary initial kernel
\[
 h_L=\min(g,L)-m_L,\qquad m_L=\int\min(g,L)
                  =-\int(g-L)^+\le0. \tag{4.4}
\]
The local singularity (3.1) gives, for a fixed sufficiently large L0,
\[
 |\{g>L\}|\le CL^{-2},\quad |m_L|\le C/L,\quad
 \int h_L^2\le C(1+\log L),\quad \int h_L^4\le C(1+L^2),
 \qquad L\ge L_0. \tag{4.5}
\]
These are layer-cake integrals of the tail of exponent two, with bounded
negative part; recentering changes only the displayed constants.
Set \(L_N=L_0N^2\), \(H_N^L=H^{h_{L_N}}\), and let B be the
time-zero event that some unordered initial pair has g larger than L_N.
Then
\[
 \mathbb P(B)\le CN^{-2},\quad
 \mathbb E(H_N^L)^2\le C(1+\log N),\quad
 \mathbb E(H_N^L)^4\le C\{N^2+(1+\log N)^2\}. \tag{4.6}
\]
The second identity follows from the same zero-row pairing; the third
is (4.3). On \(B^c\), with the finite-N coefficient visible,
\[
 H_N(X_0)=H_N^L+\frac{N-1}{2}m_{L_N}\le H_N^L,
                    \qquad H_N(X_0)^+\le|H_N^L|. \tag{4.7}
\]
The original unclipped energy still has infinite second and fourth
moments. No dynamics, source, or centering has been clipped.

## 5. The energy martingale on the good initial event

Let \(E_*^R=\sup_{s\le T}|E_{s\wedge\tau_R}|\), with an additional
bracket/localization stop when needed. The deterministic floor and
(3.2) give
\[
 A_{T\wedge\tau_R}\le Q+E_*^R,\qquad
 Q=H_N(X_0)+C\sqrt N+\nu c(N-1)T\ge0. \tag{5.1}
\]
On \(B^c\), (4.7) bounds Q by
\(|H_N^L|+C\sqrt N+\nu c(N-1)T\). In particular
\[
                      \mathbb E[\mathbf1_{B^c}Q^2]\le C N \tag{5.2}
\]
on (1.2).

For a continuous real stopped martingale M starting at zero,
\(\mathbb E M_*^4\le C\mathbb E\langle M\rangle_T^2\).
For completeness, Itô gives
\(\mathbb EM_T^4=6\mathbb E\int M_s^2d\langle M\rangle_s\);
the L4 maximal inequality and Cauchy--Schwarz then give the displayed
bound after absorbing its square-root factor. The maximal inequality
itself follows from optional stopping on first crossings of a level,
the submartingale \(|M|\), integration of the resulting tail inequality,
and Hölder. Bounded stops justify these operations; increasing them and
Fatou remove the preliminary boundedness requirement.

Apply this to \(\mathbf1_{B^c}E_{\cdot\wedge\tau_R}\). This is a true
martingale because B is measurable at time zero. Its bracket is
\(2\nu\mathbf1_{B^c}A_{\cdot\wedge\tau_R}\). Equations (5.1), (5.2)
and Young's inequality give
\[
\begin{split}
 \mathbb E[\mathbf1_{B^c}(E_*^R)^4]
 &\le C\nu^2\mathbb E[\mathbf1_{B^c}\{Q^2+(E_*^R)^2\}]\\
 &\le C\nu^2\mathbb E[\mathbf1_{B^c}Q^2]
    +\tfrac12\mathbb E[\mathbf1_{B^c}(E_*^R)^4]+C\nu^4.
\end{split} \tag{5.3}
\]
Since \(\nu\le\lambda_-^{-1}N^{-1/2}\), removal of all stops by Fatou
proves
\[
            \mathbb E[\mathbf1_{B^c}E_*^4]\le C,
            \qquad E_*:=\sup_{s\le T}|E_s|. \tag{5.4}
\]
This is deliberately a restricted fourth moment. No unconditioned
fourth moment of the energy martingale or A is asserted.

## 6. Proof of the actual fourth-moment assertion

Integrating (3.5), using (3.2) and \(A\ge0\), gives uniformly over
terminal times t in the stated interval
\[
 |S_{N,m}(t)|\le C_Tw_m
      \{1+N^{-1/2}H_N(X_0)^++N^{-1/2}E_*\}. \tag{6.1}
\]
Here the critical bound on \(\nu\sqrt N\) has been included in the
constant. On \(B^c\), equations (4.6), (4.7), (5.4) imply
\[
                  \mathbb E[\mathbf1_{B^c}|S_{N,m}(t)|^4]
                         \le Cw_m^4. \tag{6.2}
\]
On B use (3.6), not (6.1). The endpoint has the deterministic bound
\(|D_{N,m}(t)|\le2\sqrt N\). The two real components of
\(\mathbf1_BL_{N,m,t}\) are martingales with bracket at most
\(2\nu T\ell_m\mathbf1_B\). The fourth-moment martingale inequality
therefore proves
\[
 \mathbb E[\mathbf1_B|L_{N,m,t}|^4]
       \le C\nu^2T^2\ell_m^2\mathbb P(B),
 \quad
 \mathbb E[\mathbf1_B|S_{N,m}(t)|^4]
       \le C(N^2+\nu^2T^2\ell_m^2)\mathbb P(B)\le Cw_m^4. \tag{6.3}
\]
Time-zero measurability is essential; no independence of B and the
trajectory is asserted. Combining (6.2), (6.3) proves the source part of
(2.2). Equation (3.6) and the unrestricted bounded-bracket fourth
moment of L prove the endpoint part without discarding a cross term.
Finally iid Haar gives the exact initial modal identity
\[
                   \mathbb E|\sqrt N Z_m(0)|^4=2-1/N \tag{6.4}
\]
for every nonzero integer m: in the conjugate expansion only the two
pairings survive, with the all-equal labels counted once. Since
\(\sqrt N Z_m(t)=D_{N,m}(t)+e^{-a_mt}\sqrt N Z_m(0)\), the final part
of (2.2) follows. This proves the whole moment assertion, including
uniformity in m with exactly the displayed polynomial weight.

The clipping power N squared is not arbitrary in this proof. The
same-edge term in (4.2), after division by N squared for the scaled
source fourth power, costs \(L^2/N^4\); the bad event costs \(N^4/L^2\).
Both are bounded at \(L\) of order N squared. Neither is claimed to tend
to zero. This is why a bounded fourth moment is proved, not fourth-power
uniform integrability or source decay.

## 7. Fourier calculation of the smoothed actual three-label term

All r below truncate an observable, not the force driving (1.1). Let
\(a_r(m)=|m|^{-2}e^{-cr|m|^2}\) for nonzero m and \(a_r(0)=0\).
Directly multiplying (2.3) gives
\[
 j_{k,r}(x,y)=\sum_m b_{k,r}(m)e_{k+m}(x)e_{-m}(y),
\quad b_{k,r}(m)=c\{(k\cdot m)a_r(m)
 -(k\cdot(m+k))a_r(m+k)\}
       +d_{k,r}(\mathbf1_{m=0}+\mathbf1_{m=-k}). \tag{7.1}
\]
Its rows vanish, \(b(0)=b(-k)=0\), \(b(m)=b(-k-m)\), and
\(\sum_m b(m)=2d_{k,r}\). The latter is the smooth diagonal
\(j_{k,r}(x,x)=2d_{k,r}e_k(x)\), not a singular diagonal convention.

For fixed k,
\[
 |b_{k,r}(m)|\le C_k|m|^{-2}e^{-cr|m|^2/8},\quad m\ne0,
 \qquad
 \sum_m|b_{k,r}(m)|w_{k+m}w_m\le C_k r^{-11}. \tag{7.2}
\]
The first inequality follows by differentiating
\(x|x|^{-2}e^{-cr|x|^2}\) along the segment from m to m+k when
\(|m|\ge2|k|\). Its derivative is bounded by
\(C(|m|^{-2}+r)e^{-cr|m|^2/4}\), which is at most the displayed
broader Gaussian. The remaining modes form a finite set. No bounded
ratio of neighboring Gaussian weights is assumed. For the second bound,
the large-radius lattice summand has weight at most
\(C_k|m|^{18}e^{-cr|m|^2/8}\). Counting at most \(C(j+1)^3\) modes in
unit radial shells and integrating the resulting power 21 gives r to
the power minus eleven. The finite low modes are absorbed since r is
at most a fixed r0. All sums are absolutely convergent at positive r.

Put \(U_r=(2N^2)^{-1}\sum_{i\ne j}j_{k,r}(X_i,X_j)\). Exact deletion
in the smooth Fourier series yields
\[
 U_r=\tfrac12\sum_m b(m)Z_{k+m}Z_{-m}-\frac{d_{k,r}}N Z_k. \tag{7.3}
\]
Using (2.2) for the first two modes, and their L2 consequence for the
last mode, Hölder with exponents 4,4,2 gives
\[
 |N\mathbb E[U_r\overline{Z_k(t)}]|
   +|N\mathbb E[U_r\overline{Z_k(0)}]|
                  \le C_{k,T}N^{-1/2}r^{-11}. \tag{7.4}
\]
For the second term the initial mode has L2 norm exactly N to the power
minus one half. The self term in (7.3) contributes at most C/N. It is
included in (7.4), not deleted. The vanished coefficients at m=0,-k
are essential: no constant empirical mode is inserted into Hölder as a
small fluctuation.

For completeness, the needed actual-pair truncation estimates from R26
can be reproduced without any unproved marginal factorization. From
(3.4), positive q_r and exact Fourier deletion one has
\[
 \frac N{N-1}\mathbb E\sum_{m\ne0}a_r(m)|Z_m(t)|^2
  +\mathbb E q_r(X_1-X_2)
     \le\frac{g_r(0)}{N-1}+cr. \tag{7.5}
\]
The central heat kernel on \([R^2/2,R^2]\) gives
\(q_{R^2}(z)\ge c_0R^{-2}\) for \(|z|\le R\). Hence
\(\mathbb P(\operatorname{dist}(X_1-X_2,0)\le R)
 \le C(R^4+N^{-1})\).
The retained radial force and its bounded periodic remainder give
\(|j_{k,r}(x,y)|\le C_k[1+\min(r^{-1},\operatorname{dist}(x-y,0)^{-2})]\).
Layer cake therefore gives
\[
 \mathbb E|j_{k,r}(X_1,X_2)|^2
       \le C_k\{1+\log(1/r)+(Nr^2)^{-1}\}. \tag{7.6}
\]
The finite-N term in this bound cannot be dropped when r tends to zero.
The full-force action (3.3), exchangeability and Brownian maximal square
give tagged displacement at most \(C_T(N^{-1/2}+\nu)\) in mean square.

Let A2r,B2r be the two overlaps with the displayed smoothed j. The exact
current Fourier overlap is
\[
 A2r=\frac N{N-1}\sum_{m\ne0}b(m)\mathbb E|Z_m(t)|^2
                         -\frac{2d_{k,r}}{N-1}. \tag{7.7}
\]
Equations (2.2), (7.2) imply \(|A2r|\le C N^{-1}r^{-11}\).
The difference between its current and initial phase is controlled by
Cauchy--Schwarz, (7.6), and tagged displacement:
\[
 |B2r-A2r|\le C_{k,T}N^{-1/4}
                   \{1+\log(1/r)+(Nr^2)^{-1}\}^{1/2}. \tag{7.8}
\]
This uses no current/initial density and no independence.

In each covariance in (7.4) there are exactly 2N(N-1) overlap triples
and N(N-1)(N-2) distinct triples. Thus
\[
 N\mathbb E(U_r\overline{Z_k(t)})
       =\frac{N-1}N A2r+p_N A3r,
 \quad
 N\mathbb E(U_r\overline{Z_k(0)})
       =\frac{N-1}N B2r+p_N B3r. \tag{7.9}
\]
Use (7.4), (7.7), (7.8) in (7.9), multiply by the two distinct weights
\(u_t^2\) and \(A_ku_t\), and integrate. Each has modulus at most one
since \(\widetilde a_k\ge c/2\). This proves exactly (2.4).
At (2.5) its first term is \(C N^{-1/24}\); its second is
\(C N^{-1/4}\sqrt{1+\log N}\), which is at most \(C N^{-1/24}\)
for N at least two. These separate bounds apply only to the smoothed
observable; no separate decay of the original A3 or B3 is asserted.

## 8. Exact transfer to the force tail, including its row correction

The literal difference satisfies
\[
 j_k-j_{k,r}=J_k^{>r}+(c-d_{k,r})(e_k(x)+e_k(y)). \tag{8.1}
\]
Linearity already gives an exact centered-tail decomposition of (1.5).
To remove only the explicitly displayed row contribution, put
\[
 C_t=\mathbb E[e_k(X_1(t))\overline{e_k(X_2(t))}],\quad
 O_t=\mathbb E[e_k(X_1(t))\overline{e_k(X_2(0))}],\quad
 S_t=\mathbb E[e_k(X_1(t))\overline{e_k(X_1(0))}].
\]
Exchangeability and exact same-label deletion give
\[
 C_t=\frac{N\mathbb E|Z_k(t)|^2-1}{N-1},\qquad
 O_t=\frac{N\mathbb E[Z_k(t)\overline{Z_k(0)}]-S_t}{N-1}. \tag{8.2}
\]
By (2.2), its L2 consequence, initial variance 1/N, and \(|S_t|\le1\),
both numerators are bounded uniformly on the critical window. Thus the
exact row remainder is
\[
 \mathcal B_{N,r}=2p_N(c-d_{k,r})
      \int_0^T\{u_t^2 C_t-A_ku_t O_t\}\,dt,
 \qquad |\mathcal B_{N,r}|\le C_{k,T}r. \tag{8.3}
\]
In particular,
\[
 \mathcal R_N^{(3)}=\mathcal R_{N,r}^{(3)}
                        +\mathcal H_{N,r}^{(3)}+\mathcal B_{N,r} \tag{8.4}
\]
exactly. At (2.5) equations (2.4), (8.3) prove (2.7).

The singular two-label part also remains negligible under these actual
inputs: (7.5), the kernel bound
\(|J_k-J_{k,r}|\le C_k q_{2r}\), and
\(|c-d_{k,r}|\le C_kr\) bound its truncation error by
\(C_k[r+(Nr)^{-1}]\). More explicitly, the first bound in (7.2) compares
\(|b(m)|\) to \(C_k a_{r/8}(m)\). Equations (7.5), (7.7) therefore give
\(|A2r|\le C_k[r+(Nr)^{-1}+N^{-1}]\), independently of the new
fourth-moment estimate. At r of order N to the power minus one half,
this bound, (7.6), truncation error, and displacement
give precisely R26's A2 bound \(CN^{-1/2}\) and B2 bound
\(CN^{-1/4}\sqrt{1+\log N}\). Its integrated prefactor is
\((N-1)/N\), not p_N. This reproduces the used THM051(D) mechanism;
it is not claimed as new work or separate certification.

## 9. Complete attempt at the surviving estimate, and the first open line

The new proof route was to estimate the actual collective source with
three low-frequency factors, using genuine fourth moments in two slots.
It succeeds exactly for (2.4), including a shrinking observable cutoff.
The next attempted step was uniform removal of that cutoff. Its failure
can be located quantitatively, rather than called missing decorrelation.

The actual energy/heat estimate gives only
\[
 \mathbb E|j_k-j_{k,r}|\le C_k[r+(Nr)^{-1}]. \tag{9.1}
\]
Putting a phase of modulus one in the third slot and taking absolute
values before time integration would cost
\[
                         C_{k,T}(Nr+r^{-1}). \tag{9.2}
\]
Even its minimum over r is of order square root N. Keeping the aggregate
source/endpoint structure improves existing control to bounded order,
but does not make it tend to zero. The summable majorant used in (7.4)
is \(N^{-1/2}r^{-11}\); it is not uniform as r decreases to zero at
fixed N. Thus dominated summation or cutoff passage cannot close this
line. Subtracting the row, which really is small by (8.3), does not
supply a bound for the force-tail correlation.

An independent falsification test was the initial near-collision energy
tail. A direct fourth-moment use of the untruncated energy is false:
already one separated pair neighborhood contributes an integral of
\(r^3r^{-8}\) near zero. The exact clipping expansion and the bad-event
endpoint bound repair precisely this failure. Their competing powers
are both bounded at L of order N squared, so this mechanism does not
produce a positive-limsup target witness. The finite radial and algebraic
tests in the packet verify those powers; they are not replacement laws.

The first still-unproved line is now exactly
\[
 \boxed{\ \Re\left[p_N\int_0^T
  \left\{u_t^2\mathbb E[J_k^{>r_N}(X_1(t),X_2(t))
                                  \overline{e_k(X_3(t))}]
       -A_ku_t\mathbb E[J_k^{>r_N}(X_1(t),X_2(t))
                                  \overline{e_k(X_3(0))}]\right\}dt\right]
                          \longrightarrow0.\ } \tag{9.3}
\]
Here k,T,lambda stay fixed, r_N is precisely (2.5), and all expectations
are under (1.1). The raw force tail has its explicit row error already
accounted for in (8.3), not silently erased. An admitted positive-limsup
witness to (9.3) would be an admitted witness to the frozen target by
(2.7), the reproduced two-label bound, and the accepted R25 criterion.
Neither such a witness nor (9.3) is proved.

The physical heat approximation epsilon was removed at fixed N in
Section 3. The r_N here is only an auxiliary observable scale along the
already constructed actual law. There is no exchange of physical cutoff
and N limits. The target has acquired neither a moving external test nor
a moving horizon. No local equilibrium, cumulant estimate, mixing,
product marginal, or global response regularity has been assumed.

## 10. Fresh checks, self-review, and recoverable handoff

The accompanying standard-library diagnostic independently enumerates
four-edge multigraphs and exact finite-Haar fourth moments, including
all triangle, adjacent-double, disjoint-double and four-cycle coefficients.
It also compares direct finite-Fourier pair sums against (7.3), the
current and mixed label counts (7.9), and the row identities (8.2)--(8.4).
Current and initial configurations differ. Distinct rational backward
weights catch an illicit merging of the two weights. The diagnostics
also check the nonvanishing noise cross term, clipping balance and
cutoff exponent. Results and all intentionally nonzero mutation runs
are in the packet. The baseline passed 5,695 exact assertions in 31
categories, with 17 distinct nonzero mathematical mutation witnesses.
No old constructor code, SDE simulation, random seed,
dependency installation or numerical asymptotic theorem is involved.

| Adversarial question | Resolution and limit |
|---|---|
| Does Haar W1,4 failure conflict with (2.2)? | No; (2.2) bounds values, not derivatives of a conditional response. |
| Is infinite initial energy variance used? | No; (4.2) is for a bounded centered initial auxiliary kernel only. |
| Is the good event allowed inside a martingale inequality? | Yes, it is measurable at time zero; its indicator is placed in the integrand before the inequality. |
| Is an unrestricted fourth energy/action moment asserted? | No; (5.4) has the good-event indicator throughout. |
| Are original martingale cross terms dropped? | No; (3.7) is retained and all moment comparisons use inequalities for sums. |
| Are zero Fourier modes passed through a small-mode bound? | No; b(0)=b(-k)=0 before (7.4). |
| Is the heat diagonal omitted? | No; (7.3) contains minus d Z/N and (7.7) minus 2d/(N-1). |
| Are the three-label multiplicity and two weights exact? | Yes; p_N and u squared versus A times u occur unchanged throughout. |
| Has the process been regularized at r_N? | No; r_N only changes the tested kernel. |
| Is the raw force-tail row lost? | No; its exact contribution is (8.3), bounded separately. |
| Does a bounded fourth moment imply the desired limit? | No; it supplies the three-factor estimate only after smoothing. |
| Does the result certify THM046 or THM051? | No; all new assertions are same-context SELF_CHECKED, and (9.3) remains open. |

The output packet contains this full report, all 21 exact input copies,
the original manifest, claim/exposure/read/history records, fresh program
and results with every failed control, README, complete safe regular-member
inventories and digests, and a portable read-only verifier. Issued evidence
is sealed read-only; corrections require a distinct issuance.

Only the assigned memorandum, uniquely timestamped artifact directory,
and named sibling archive/seals are written. Root owns identifiers,
canonical ledgers, source/gate comparison, and independent review.
There is no canonical/input edit, child, memory read, current R27/R28
narrative read, other-worktree read, external literature claim, commit,
push, installation, author contact, publication or remote change.

The maximal new result here is (2.2), (2.4), and (2.7), not a proof or
disproof of THM046. The next load-bearing task is exactly (9.3).
