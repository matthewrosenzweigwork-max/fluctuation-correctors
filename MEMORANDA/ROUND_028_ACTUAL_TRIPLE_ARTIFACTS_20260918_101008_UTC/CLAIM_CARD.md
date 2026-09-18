# R28 complete new claim and target boundary

SELF_CHECKED construction only; not independent certification.
The following exact sections are copied from the issued REPORT.md.
The first remaining unproved line is REPORT equation (9.3).

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

