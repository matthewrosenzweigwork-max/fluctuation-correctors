# Round 025 — critical source uniform integrability and an exact covariance gate

TASK107, issued 2026-09-18 UTC. Assigned isolated worktree
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r025-critical-threshold-ultra`,
base `3efdbb96e7b94529b280234e83eb36f5fca3ef36`.

**NEW LOAD-BEARING LEMMA AND EXACT REDUCTION, SELF-CHECKED ONLY.
THM046 REMAINS OPEN. No admitted counterexample is proved.**

For the actual critical iid-Haar dynamics, the squares of the scaled
*time-integrated* sources are uniformly integrable. More precisely, there
are deterministic constants A,C such that their squared excess beyond A
is at most C(1+log N)/N in expectation. This is compatible with the infinite
second moment of the instantaneous source at time zero. The proof combines
a pathwise Coulomb source/energy bound, the true energy martingale, a
canonical clipping of the initial iid energy, and the bounded one-body
endpoint identity on the rare initial event. No instantaneous source square
is integrated.

Consequently the original L1 assertion is equivalent, under its exact law
and scaling, to its L2 version. The signed correlation gate isolated in the
supplied R24 actual-law report is therefore necessary as well as sufficient
for the full fixed-smooth-test assertion. That cancellation is still
unproved; its failure could now furnish an admitted L1 counterexample,
whereas failure of a stronger estimate alone previously could not. This
removes the unresolved uniform-integrability qualification from that route.

The present context constructs and self-checks this lemma. It does not
certify itself or either supplied R24 report. Root owns all identifiers,
canonical changes, and fresh independent gates.

## 1. Frozen assertion and exact negation

The unit torus is T^4, with Haar mass one and characters
\(e_k(x)=e^{2\pi i k\cdot x}\). Put \(c=4\pi^2\),
\(\widehat g(0)=0\), \(\widehat g(k)=|k|^{-2}\) for nonzero k, and
\(K=-\nabla g\). The actual particles solve
\[
 dX_i=B_i(X)dt+\sqrt{2\nu_N}\,dW_i,
 \qquad B_i=N^{-1}\sum_{j\ne i}K(X_i-X_j),
 \tag{1.1}
\]
from iid Haar initial positions independent of all Brownian drivers.
The noise is positive, \(\nu_N=\beta_N^{-1}\), and
\(\lambda_N=\beta_N N^{-1/2}\to\lambda\in(0,\infty)\).
Set \(b_N=\min(\beta_N,1)\), \(\sigma_N=\sqrt{Nb_N}\).
Eventually \(b_N=1\) and \(\nu_N\sqrt N=\lambda_N^{-1}\).
All asymptotic inequalities below hold on this eventual segment, with
constants depending on fixed upper/lower critical bounds, h,T and the
fixed kernel, never N.

Fix the original real smooth h and finite T. Write
\(f_t=Q_{T-t}^{\nu_N}h\), with nonzero-mode multiplier
\(e^{-(T-t)(c+4\pi^2\nu_N|k|^2)}\) and preserved constants, and
\[
 J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)),\qquad x\ne y.
\]
The exact statistic is
\[
 P_N[J]=\frac1{2N^2}\sum_{i\ne j}J(X_i,X_j)
 -\frac1N\sum_i\int J(X_i,y)dy+\frac12\iint J(x,y)dxdy.
 \tag{1.2}
\]
Its ordered labels, denominator, half factor, and both Haar backgrounds
are unchanged. Define
\[
 S_N=\sqrt N\int_0^T P_N[J_t](X(t))dt.                 \tag{1.3}
\]
The frozen assertion is \(\mathbb E|S_N|\to0\); restoring the finitely
many indices with b_N not one does not change it. Its exact negation is an
admitted fixed T,h,lambda and critical sequence with positive limsup of
this nonnegative expectation. No source-square failure, changing test,
changing horizon, altered preparation or static law is that negation.

In this d=4,s=2 row, the old energy-floor condition is beta_N to zero;
full microscopic subcriticality is beta_N/sqrt(N) to zero; the present
critical condition is beta_N/sqrt(N) to a positive finite limit. These
three conditions remain distinct. There is no logarithmic-kernel claim.

## 2. Permitted source preflight and reconstructed actual energy identities

All 26 allowlisted byte strings passed the supplied SHA-256 manifest
before substantive mathematics. The source/exposure record distinguishes
full, partial/truncated, and hash/copy-only inputs. The R24 pair inverse,
its cubic identity and THM047 are not premises of the new lemma. The R24
actual-law report supplies the candidate correlation route, reconstructed
in Sections 5 and 8 below. The old kernel/particle/source arguments needed
here are reconstructed explicitly; no printed historical status is a
current certification.

The heat representation and central Gaussian integral give
\[
 g(z)=c\int_0^\infty(p_u(z)-1)du=|z|^{-2}+H(z)
 \quad\hbox{locally},\qquad H\text{ smooth and even},
 \tag{2.1}
\]
where \(\widehat p_u(k)=e^{-4\pi^2u|k|^2}\).
The nonzero Fourier coefficient of the integral is exactly |k|^-2.
The central Gaussian integral has coefficient one; differentiated
noncentral lattice terms are exponentially integrable at small u and the
large-time torus remainder is exponentially integrable. Thus K is odd,
Haar L1, smooth off zero, and
\[
 K(z)=2z|z|^{-4}-\nabla H(z),\qquad
 \operatorname{div}K=c(\delta_0-dz),\qquad
 \operatorname{div}_{\rm cl}K=-c\text{ off zero}.
 \tag{2.2}
\]
The sphere flux is \(2|S^3|=c\); zero Fourier mass supplies the
compensation. Neither is omitted. The potential has finite lower bound
\(g_*<0\).

Set
\[
 H_N=N^{-1}\sum_{i<j}g(X_i-X_j),\qquad
 A_t=\int_0^t\sum_i|B_i(X(a))|^2da.                 \tag{2.3}
\]
This H_N is the physical N-particle energy, not energy per particle.
The sum is unordered only in this definition. The shifted energy
\(H_N-(N-1)g_*/2\) is a sum of nonnegative pair terms and tends to
infinity at every partial collision. Its sublevels are compact away
from collisions. Local smooth force cutoffs, additive-noise Picard
construction, and the energy-height stopping times therefore yield the
singular realization as follows. On a stopped compact sublevel,
\(B=-\nabla H_N\) and \(\Delta_{4N}H_N=c(N-1)\); the factor 2/N
comes from differentiating both coordinates of each unordered pair.
Stopped Itô gives an exit probability bounded by initial shifted energy
plus \(\nu c(N-1)T\), divided by the exit height. This tends to zero.
Cutoff uniqueness patches a global noncolliding path. Fatou first proves
finite expected total-force action. Its stochastic integral then passes
in L2, and localization gives the exact unstopped identity
\[
 H_N(X_t)+A_t=H_N(X_0)+\nu c(N-1)t+E_t,
 \quad E_t=\sqrt{2\nu}\sum_i\int_0^t\nabla_iH_N(X_a)\cdot dW_i(a),
 \quad \langle E\rangle_t=2\nu A_t.                \tag{2.4}
\]
E is a true square-integrable martingale at each finite N. Only the
complete drift square is used, including all pair-force cross terms.
No individual force-square estimate is extracted. Since iid Haar gives
\(\mathbb EH_N(X_0)=0\), taking expectations is legitimate.
The sharper floor proved in Section 3 gives
\[
 \mathbb EA_T\le C\sqrt N+\nu c(N-1)T,\qquad
 \mathbb E\sup_{t\le T}|E_t|^2\le8\nu\mathbb EA_T\le C
 \tag{2.5}
\]
on the critical sequence. The last maximal estimate is the elementary
L2 martingale inequality followed by isometry. Its normalized cost is
\(\mathbb E\sup|E|^2/N=O(N^{-1})\).

For fixed-N singular passages with bounded smooth tests one can use the
following independently reconstructed bound. Heat regularization keeps
\(\operatorname{div}K_\epsilon=c(p_\epsilon-1)\), hence the smooth
N-body flow Jacobian is at least \(e^{-c(N-1)t}\). Initial Haar,
change of variables and Brownian averaging give density at most
\(e^{c(N-1)T}\). A singular path has positive minimum separation on a
compact time interval; same-noise local C1 convergence and Gronwall give
heat-path convergence at fixed N,nu,T. Passing first against continuous
tests and then open sets/Borel approximation gives the same density
bound for the actual process. This is used only for fixed-N L1 passages,
never as uniform concentration.

Uniqueness and common translations imply exact Haar one-body marginals;
permutation equivariance gives exchangeability. They imply no
positive-time iid law. An expected-energy sign from smooth free energy
is available in the supplied reports, but is not needed for the new tail
argument: (2.4), the floor, and the initial law suffice.

## 3. Pointwise source/energy majorant, with self and background terms

This section recovers a pointwise consequence of the permitted R16
heat-splitting calculation. It is stronger than taking its expectation,
but it will not by itself establish vanishing.

Use M=6 and define, for 0<r<=2,
\[
 w_r(u)=(1-e^{-u/r})^6,\quad \psi_r=1-w_r,
\]
\[
 g_r=c\int_0^\infty w_r(u)(p_u-1)du,\quad
 Q_r=c\int_0^\infty\psi_r(u)p_u\,du,\quad
 c_r=c\int_0^\infty\psi_r(u)du.
 \tag{3.1}
\]
Then \(Q_r\ge0\), \(\int Q_r=c_r=C_*r\),
\(g=g_r+Q_r-c_r\) off zero. The retained kernel is C2, has positive
nonzero Fourier coefficients
\(a_r(k)=c\int_0^\infty w_r(u)e^{-c u|k|^2}du\), and
\(0\le g_r(0)\le C/r\). These follow respectively from
\(w_r\le\min(1,(u/r)^6)\), \(\psi_r\le\min(1,6e^{-u/r})\),
and the differentiated Gaussian bounds. Put
\[
 F_r=\tfrac12\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2\ge0,
 \qquad V_r=\tfrac1{2N^2}\sum_{i\ne j}Q_r(X_i-X_j)\ge0.
\]
(The letters F_r,V_r here denote deterministic configuration quantities,
not particle densities or Fourier-mode variances.) Exact deleted-pair
summation gives
\[
 \frac{H_N}N=F_r+V_r-\frac{g_r(0)}{2N}
                         -\frac{N-1}{2N}c_r.       \tag{3.2}
\]
In particular \(H_N\ge-C\sqrt N\) by r=N^-1/2. No arbitrary weighted
positive-definiteness assertion is used.

For a smooth vector field v and the smooth retained source, the diagonal
is zero. The full-product centered identity therefore equals the literal
statistic (1.2). Fourier symmetrization gives
\[
 P_N[J_{g_r}]= -\pi i\sum_{k,l\ne0}
 [k a_r(k)-l a_r(l)]\cdot\widehat v(l-k)
 \widehat\rho(k)\overline{\widehat\rho(l)}.          \tag{3.3}
\]
A direct integration by parts in u shows the radial logarithmic slope
\(0\le-\xi a_r'(\xi)/a_r(\xi)\le14\), since
\(0\le u w_r'(u)\le6w_r(u)\). If q=k-l, comparison along the radial
segment between |k| and |l| then gives
\[
 \frac{|k a_r(k)-l a_r(l)|}{\sqrt{a_r(k)a_r(l)}}
 \le15|q|(1+|q|)^8.
\]
Cauchy--Schwarz in the shifted sequence
\(\sqrt{a_r(k)}|\widehat\rho(k)|\) yields
\[
 |P_N[J_{g_r}]|\le C_v F_r,
 \qquad C_v\le C\sum_q|q|(1+|q|)^8|\widehat v(q)|.
 \tag{3.4}
\]
All series converge absolutely: the retained coefficients have polynomial
tails of order fourteen and the same smooth v has summable Fourier
coefficients. No Gaussian-weight neighbor ratio is bounded falsely.

For the discarded source, the elementary periodized Gaussian estimate
\(\operatorname{dist}(z,0)|\nabla p_u(z)|\le C p_{2u}(z)\)
and the mean-value estimate for v give
\(|J_{g-g_r}(x,y)|\le C\|Dv\|_\infty Q_{2r}(x-y)\).
The empirical, row and double-background contributions to the *absolute*
statistic are respectively bounded by V_(2r), c_(2r), c_(2r)/2. Therefore,
pointwise at every collision-free configuration,
\[
 |P_N[J_g]|\le C_v'\{F_r+V_{2r}+c_{2r}\}.          \tag{3.5}
\]
The exact double background is in fact zero, since K is odd, but the
inequality has retained its coefficient visibly.

In (3.2) at r and 2r, each nonnegative term is at most H_N/N plus its
explicit error. Choosing r=N^-1/2 gives a fixed G and, for the entire
backward-test family, a finite C_h such that
\[
 \boxed{\sqrt N\,|P_N[J_t](x)|
       \le C_h\{G+H_N(x)/\sqrt N\}.}              \tag{3.6}
\]
G can be enlarged to make the brace nonnegative for every configuration.
One may take C_h controlled by a fixed multiple of
\(\sum_k(1+|k|)^{10}|\widehat h(k)|\); the noise-dependent response
multipliers have modulus at most one. This proves uniformity for the
same arbitrary smooth h, not just Fourier polynomials.

Combining (3.6) with (2.4) and A_t>=0, there are deterministic A,a>=0,
uniform on the critical sequence, such that
\[
 |S_N|\le A+\frac a{\sqrt N}
       \{H_N(X_0)^++\sup_{t\le T}|E_t|\}.         \tag{3.7}
\]
For example A=C_h T(G+c T/underline(lambda)) and a=C_h T suffice after
fixing an eventual positive lower bound on lambda_N. This estimate is
only of order one. Its nondecaying A is not asserted to tend to zero.

## 4. Canonical clipping of the initial Coulomb energy

The new tail argument uses the exact initial preparation. From (2.1) and
boundedness off a small ball, for a fixed L0>=1 and L>=L0,
\[
 |\{z:g(z)>L\}|\le C L^{-2},\quad
 \int \min(g,L)^2\le C(1+\log L),\quad
 m_L:=\int\min(g,L)=-\int(g-L)^+\in[-C/L,0].       \tag{4.1}
\]
Indeed the high-level set lies in a ball of radius C/sqrt(L); the second
bound is the layer-cake integral of the resulting u^-2 tail, with a
bounded negative part; integrating the tail gives the third bound.

Let \(g^{[L]}=\min(g,L)-m_L\). It is even, translation invariant, and
has exactly zero Haar mean. At initial iid Haar define
\[
 H_N^{[L]}=N^{-1}\sum_{i<j}g^{[L]}(X_i(0)-X_j(0)).
\]
Distinct unordered pairs are orthogonal in L2, including pairs with one
label in common: conditioning on the shared coordinate makes each
remaining Haar row integral zero. Thus, with every coefficient retained,
\[
 \mathbb EH_N^{[L]}=0,\qquad
 \mathbb E(H_N^{[L]})^2=\frac{N-1}{2N}\|g^{[L]}\|_2^2
                       \le C(1+\log L).           \tag{4.2}
\]
Choose \(L_N=L_0N^2\), and let B_N^bad be the initial event that at
least one unordered pair has g>L_N. Its probability is bounded by
\[
 \mathbb P(B_N^{bad})\le\frac{N(N-1)}2 C L_N^{-2}\le C N^{-2}.
 \tag{4.3}
\]
This is a union bound, not a claim of pair independence. On its complement,
\[
 H_N(X_0)=H_N^{[L_N]}+\frac{N-1}{2}m_{L_N}
                \le H_N^{[L_N]},\qquad
 H_N(X_0)^+\le|H_N^{[L_N]}|.                       \tag{4.4}
\]
The negative clipping mean is helpful; silently recentering without its
(N-1)/2 coefficient would break the exact identity.

Only an initial random variable is clipped. Neither the singular force,
the particle dynamics, the source, nor its centering is changed. No
simultaneous cutoff/N limit is taken. In particular (4.2) is not the
false assertion that the unclipped H_N has a finite second moment.

## 5. Exact endpoint identity and all martingale terms needed here

Oddness, K in L1 and the full distribution in (2.2) give
\[
 \int J^f(x,y)dy=-c(f(x)-\bar f),\qquad \iint J^f=0.
 \tag{5.1}
\]
The atom and its compensation determine this sign. Pairing the two
orientations in Itô for the empirical test gives the factor 1/(2N^2).
Using \(\partial_t f+\nu\Delta f-c(f-\bar h)=0\), and writing
\(\rho=\eta_N-dx\), one obtains
\[
 S_N=\Delta_N-L_N^{mart},\quad
 \Delta_N=\sqrt N\{\rho_T[h]-\rho_0[Q_T^\nu h]\},
 \quad L_t^{mart}=\sqrt{2\nu/N}\sum_i\int_0^t
                           \nabla f_a(X_i(a))\cdot dW_i(a).
 \tag{5.2}
\]
At fixed N stop at energy-height exits first. The one-body integrands
are bounded, the source is Haar L1 and has a fixed-N density majorant,
and the actual paths never collide. Dominated convergence for the drift
and L2 isometry for the martingale remove the stops. Equivalently the
pointwise bound (3.6) and (2.4) supply its required absolute time
integrability. All these are genuine finite-N identities.

The true martingale has bracket and variance
\[
 \langle L^{mart}\rangle_T
 =\frac{2\nu}N\sum_i\int_0^T|\nabla f_t(X_i(t))|^2dt
 \le2\nu T\|\nabla h\|_\infty^2,
\]
\[
 q_N:=\mathbb E|L_T^{mart}|^2
 =2\nu\int_0^T\|\nabla f_t\|_2^2dt=O(\nu)=O(N^{-1/2}).
 \tag{5.3}
\]
The pathwise bound uses the heat-gradient supremum contraction; the exact
expectation uses only the actual one-body Haar marginal.

The endpoint and L^mart are not independent. The energy and one-body
martingales share Brownian drivers, with the exact cross bracket
\[
 d\langle E,L^{mart}\rangle_t
 =\frac{2\nu}{\sqrt N}\sum_i\nabla_iH_N\cdot\nabla f_t(X_i)dt
 =-\frac{2\nu}{\sqrt N}\sum_i B_i\cdot\nabla f_t(X_i)dt.
 \tag{5.4}
\]
It is finite by the total-force action and bounded test gradients. No
cross term is asserted zero. Later inequalities use squares of sums or
norm triangle inequalities, which do not require such an assertion.

The centered backward heat response has supremum at most
\(\|h-\bar h\|_\infty\). Hence
\[
 |\Delta_N|\le D_h\sqrt N,\qquad D_h=2\|h-\bar h\|_\infty.
 \tag{5.5}
\]
Crucially, B_N^bad is measurable at time zero. Conditional martingale
isometry, without independence of that event and the process, gives
\[
 \mathbb E[\mathbf1_{B_N^{bad}}|L_T^{mart}|^2]
 =\mathbb E[\mathbf1_{B_N^{bad}}\langle L^{mart}\rangle_T]
 \le2\nu T\|\nabla h\|_\infty^2\mathbb P(B_N^{bad}).
 \tag{5.6}
\]
This equality follows equally by applying ordinary isometry to the
stochastic integral with the bounded time-zero indicator in its integrand.
It would generally be false for an arbitrary terminal event.

## 6. New squared-tail lemma and L1/L2 equivalence

The precise new whole claim is this: for each fixed smooth real h, finite
T and fixed critical window 0<lambda_lower<=lambda_upper<infinity, there
exist finite A,C independent of N and the parameter chosen in that window
such that (6.3) holds for every integer
N>=max(2,ceil(lambda_lower^-2)) and every beta>0 with
lambda_lower<=beta/sqrt(N)<=lambda_upper, for the actual process (1.1)
and its prescribed response. On every admitted convergent critical
sequence its squares are uniformly integrable and (6.4)--(6.6) hold;
for the full all-smooth-test assertion, (8.7) is equivalent, with the
positive-limsup negations equivalent as explained there. This is a
separate auxiliary claim and does not replace THM046.

Its exact negation is that an admitted fixed datum and critical window
violates one of these clauses: in particular, the first clause fails
precisely if for some such datum/window no finite A,C works for all the
specified N and beta; the remaining clauses fail if an admitted sequence
has non-uniformly-integrable squared sources, one of the stated limits
without an equivalent limit, or a mismatch between the full target and
the correlation criterion. A failed proof, infinite instantaneous
variance, or failure of a stronger unrelated bound is not this negation.
The claimed uniformity only uses a lower bound on lambda, though both
window endpoints are allowed in the constant notation.

Combine the preceding exact facts. On the good initial event, (3.7) and
(4.4) imply
\[
 (|S_N|-A)_+^2\le\frac{2a^2}N
       \{|H_N^{[L_N]}|^2+\sup_{t\le T}|E_t|^2\}.
 \tag{6.1}
\]
Its expectation is at most C(1+log N)/N by (2.5),(4.2).
On the bad initial event, use (5.2),(5.5) instead of the infinite-variance
initial energy:
\[
 \mathbb E[\mathbf1_{B_N^{bad}}(|S_N|-A)_+^2]
 \le2D_h^2N\mathbb P(B_N^{bad})
       +2\mathbb E[\mathbf1_{B_N^{bad}}|L_T^{mart}|^2]
 \le C/N.                                         \tag{6.2}
\]
Equations (4.3),(5.6) supply the last bound. Thus
\[
 \boxed{\mathbb E (|S_N|-A)_+^2
             \le C\frac{1+\log N}N=:\varepsilon_N\longrightarrow0.}
 \tag{6.3}
\]
This proof never squares the instantaneous source. It establishes L2
integrability of S_N using its exact endpoint expression before applying
any L2 estimates. No potential or source diagonal is assigned.

For x>=0, \(x^2\le2Ax+2(x-A)_+^2\). Therefore
\[
 (\mathbb E|S_N|)^2\le\mathbb E|S_N|^2
       \le2A\mathbb E|S_N|+2\varepsilon_N.         \tag{6.4}
\]
This is the desired quantitative equivalence, including its converse.
For R>2A, \(x^2\mathbf1_{x>R}\le4(x-A)_+^2\). Use (6.3) for the tail
of the sequence and ordinary L2 integrability for each of the finitely
many remaining indices: the family \(\{|S_N|^2\}\) is uniformly
integrable. In fact its limiting distributions are supported in [-A,A],
without any assertion that their only possible value is zero.

The norm triangle inequality in (5.2), retaining all endpoint/noise cross
terms, gives
\[
 \left|\sqrt{\mathbb E|S_N|^2}
       -\sqrt{D_N(h,T)}\right|\le\sqrt{q_N},
 \quad D_N(h,T)=\mathbb E|\Delta_N|^2.             \tag{6.5}
\]
It follows that for every admitted fixed real h,T and critical sequence,
\[
 \boxed{\mathbb E|S_N|\to0
  \quad\Longleftrightarrow\quad \mathbb E|S_N|^2\to0
  \quad\Longleftrightarrow\quad D_N(h,T)\to0.}      \tag{6.6}
\]
Positive-limsup negations are equivalent as well: (6.4),(6.5) and uniform
boundedness prevent variance from being carried by vanishing L1 tails.
If T=0 or h is constant every source is identically zero and this remains
valid without division by A. No convergence-rate theorem for S_N is
asserted; (6.3) is a tail estimate around a possibly nonzero fixed A.

## 7. Independent falsification attempt and exact diagnostic

The principal vulnerability was an initial close pair. Its Coulomb energy
has a tail of exponent two, so a direct attempt to square (3.7) fails.
This is a real failure at the admitted iid initial law, not a numerical
artifact. On a set where all other coordinates remain separated, one
pair has \(g\asymp r^{-2}\) and the H_N square integrates as
\(\int_0^\delta r^3r^{-4}dr=\infty\). The new proof therefore uses
the bounded endpoint on the bad event; a global initial-energy variance
bound is neither assumed nor repaired by notation.

A new exact radial diagnostic takes a uniform radius in the four-ball,
so U=r^4 is uniform on (0,1) and G=U^-1/2-2 has zero mean and lower
bound -1. For L>=0,
\[
 \mathbb P(G>L)=(L+2)^{-2},\quad m_L=-1/(L+2),
\]
\[
 \operatorname{Var}(\min(G,L))
 =2\log(L+2)-3+4/(L+2)-(L+2)^{-2},
\]
\[
 \mathbb E\min(G_+^2/N,N)
 =\{2\log((N+2)/2)+4/(N+2)-2\}/N.                \tag{7.1}
\]
These follow by integrating density 2y^-3 for y=G+2>=1. The untruncated
second moment is infinite; the capped moment has the logarithmic/N rate.
This is a solvable local-tail test, not the full periodic particle law
and not a counterexample to THM046.

The companion fresh standard-library checker also enumerates exact finite
cyclic-group iid laws with even mean-zero rational kernels, their clipped
kernels and every ordered/deleted-label coefficient. It verifies (4.2),
(4.4), the bad-pair union bound and nonzero overlap covariances if clipping
is not recentered. A bounded two-step martingale on an exact finite
probability space tests (5.6) and supplies a nonvacuous counterexample
when its initial event is replaced by a terminal event. Scalar examples
test (6.4); an abstract rare-spike sequence tests why mere L1 boundedness
would not supply (6.6). Such scalar countermodels are explicitly not
admitted particle dynamics.

The executed diagnostic passed 19,132 assertions in 32 categories, with
12 distinct nonvacuous mutation witnesses. The diagnostic has exact rational assertions and analytically derived
radial integrals evaluated with documented floating tolerances. It has
no random sampling, no installed dependency and no discretized SDE
claim. DIAGNOSTIC_RESULT.json contains counts and mutation witnesses;
RUN_HISTORY.md records the executed result. This self-check supports
coefficients and the vulnerable tail mechanism; it does not independently
certify the continuum proof.

## 8. Exact surviving actual-law correlation, now an L1-equivalent gate

Here the supplied R24 correlation deduction is reconstructed, not assumed
as an accepted theorem. Fix a nonzero lattice mode k, and set
\[
 Z_k(t)=N^{-1}\sum_i e_k(X_i(t)),\quad \ell_k=c|k|^2,
 \quad a_k=c+\nu\ell_k,\quad \widetilde a_k=a_k-c/N,
 \quad A_k=e^{-a_kT}.
\]
Define the symmetric zero-row kernel
\[
 j_k(x,y)=J^{e_k}(x,y)+c(e_k(x)+e_k(y)),\qquad
 U_N^k=(2N^2)^{-1}\sum_{i\ne j}j_k(X_i,X_j).
\]
Exact counting of each particle's N-1 partners in both orientations gives
\[
 P_N[J^{e_k}]=U_N^k+(c/N)Z_k,\qquad
 dZ_k=-\widetilde a_k Z_kdt+U_N^kdt+dM_k.
 \tag{8.1}
\]
Here \(M_k=\sqrt{2\nu}N^{-1}\sum_i\int\nabla e_k(X_i)dW_i\), and
\[
 d\langle M_k,\overline M_l\rangle_t
   =(2\nu/N)c(k\cdot l) Z_{k-l}(t)dt,
 \quad d\langle M_k,\overline M_k\rangle_t
   =(2\nu\ell_k/N)dt.                            \tag{8.2}
\]
The conjugate cross bracket has not been set to zero pathwise. The
current/current equation has two response slots; the current/initial
equation below has one evolving slot. This accounts for 2c versus c.

Define actual expectations
\[
 A_{2,N}(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(t))}],
 \quad A_{3,N}(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(t))}],
\]
\[
 B_{2,N}(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_1(0))}],
 \quad B_{3,N}(t)=\mathbb E[j_k(X_1(t),X_2(t))\overline{e_k(X_3(0))}].
\]
The three-label terms are absent at N=2. All are finite time-integrable
quantities at fixed N by the L1 source/density passage in Section 2;
the factors multiplying the source have modulus one. Put
\[
 \mathcal F_N=\frac{N-1}N A_{2,N}
       +\frac{(N-1)(N-2)}{2N}A_{3,N},\qquad
 \mathcal G_N=\frac{N-1}N B_{2,N}
       +\frac{(N-1)(N-2)}{2N}B_{3,N}.              \tag{8.3}
\]
There are 2N(N-1) overlapping triples and N(N-1)(N-2) all-distinct
triples in N times the covariance of U_N^k with the empirical mode;
the denominator is 2N^2. Symmetry identifies the two overlaps. Hence
\(N\mathbb E(U_N^k\overline Z_k(t))=\mathcal F_N\) and
\(N\mathbb E(U_N^k\overline Z_k(0))=\mathcal G_N\).

Product Itô, including (8.2), yields for
\(V_N=N\mathbb E|Z_k(t)|^2\) and
\(R_N=N\mathbb E(Z_k(t)\overline Z_k(0))\),
\[
 V_N'=-2\widetilde a_k V_N+2\nu\ell_k+2\Re\mathcal F_N,
 \qquad R_N'=-\widetilde a_kR_N+\mathcal G_N,
 \qquad V_N(0)=R_N(0)=1.                         \tag{8.4}
\]
Martingale expectations vanish after the bounded current-mode product;
the initial mode is time-zero measurable. This is not independence of
initial and final positions. Solving the two scalar equations gives
\[
 \mathcal D_N(k,T):=N\mathbb E|Z_k(T)-A_kZ_k(0)|^2
 =(e^{-\widetilde a_kT}-e^{-a_kT})^2
 +\frac{\nu\ell_k}{\widetilde a_k}(1-e^{-2\widetilde a_kT})
 +2\Re\mathcal R_N(k,T),                         \tag{8.5}
\]
\[
 \mathcal R_N(k,T)=\int_0^T
 [e^{-2\widetilde a_k(T-t)}\mathcal F_N(t)
  -e^{-a_kT}e^{-\widetilde a_k(T-t)}\mathcal G_N(t)]dt.
 \tag{8.6}
\]
The first explicit term is O(N^-2), the noise term O(N^-1/2), since
\(\widetilde a_k\ge c/2\). The missing line is exactly
\[
 \boxed{\Re\mathcal R_N(k,T)\longrightarrow0
 \quad\text{for each fixed nonzero k and finite T under every admitted
 critical sequence}.}                           \tag{8.7}
\]

By Section 6 applied to the fixed real tests cos(2pi k.x) and
sin(2pi k.x), (8.7) is necessary for the full THM046 assertion. It is
sufficient as well: (8.5) gives L2 and then L1 convergence of each mode.
The pointwise majorant and energy expectation give the uniform mode
bound \(\mathbb E|S_N(e_k,T)|\le C_T(1+|k|)^{10}\).
Smooth h has summable Fourier coefficients against this weight.
Dominated summation extends mode convergence to that same smooth h.
Complex notation combines two real tests and changes no theorem scope.

Thus (8.7) is now **equivalent to the full original L1 target**, not
merely a sufficient stronger-L2 route. Its exact negation is admitted
fixed k,T,lambda,critical sequence with positive limsup of
\(\Re\mathcal R_N\). Equation (8.5) makes its negative part o(1);
positive limsup forces positive endpoint variance. At least one of the
fixed real cosine/sine tests then has positive variance limsup, and
(6.4)--(6.6) transfer it to the exact L1 negation. This conclusion
requires the new tail lemma; it must not be inferred from variance
failure alone in a general law class.

The current and initial two-time pair expression is also exact:
if C_N=E e_k(X1(T)-X2(T)), S_N^tag=E e_k(X1(T)-X1(0)), and
O_N=E e_k(X1(T)-X2(0)), then
\[
 \mathcal D_N=1+(N-1)C_N+A_k^2
       -2A_k\Re[S_N^{tag}+(N-1)O_N].             \tag{8.8}
\]
This formula counts N same labels and N(N-1) distinct labels; the initial
distinct-label term vanishes exactly by iid Haar. It does not close the
remaining dynamic cancellation. No separate absolute smallness of the
four terms in (8.3) has been proved or assumed.

## 9. Adversarial self-check and precise remaining failure

| Challenge | Disposition |
|---|---|
| Does the new proof square the instantaneous singular source? | No. Its square is allowed to be infinite. The endpoint identity first supplies finite-N L2 of the time integral. |
| Does the initial energy secretly have finite variance? | No. Only a centered clipped kernel has the variance (4.2). The rare-event treatment uses a different bound. |
| Is clipping a change of particle dynamics or centering? | No. It is an auxiliary initial random variable; the exact source and all backgrounds remain unchanged. |
| Are overlapping iid pairs treated as independent? | No. Their covariance is zero by conditional zero rows; no independence is claimed. |
| Is the number of rare pairs missing? | The factor N(N-1)/2 is retained in (4.3); the endpoint square costs O(N). |
| Is a terminal event used in conditional isometry? | No. The bad event depends only on initial positions and is time-zero measurable. The finite diagnostic catches this distinction. |
| Is the energy martingale dropped? | No. Its bracket is 2nu A_t and its maximal square costs O(1/N) after normalization. |
| Are energy/one-body or endpoint/one-body cross terms zeroed? | No. The cross bracket (5.4) is explicit. Norm and sum inequalities control them. |
| Are singular limits exchanged with N? | No. Localization/heat passage is at fixed N,nu,T. Initial clipping and heat splitting are deterministic algebraic devices applied afterwards. |
| Does the tail lemma already prove zero? | No. A remains order one. An abstract nonzero bounded scalar sequence satisfies such a tail bound, so an extra dynamic cancellation is indispensable. |
| Is the full pair inverse used without reconstructing its domain? | No. It is not a premise. This construction uses the one-body identity only. |
| Is the covariance reduction called an independent audit? | No. It is reconstructed in this same constructor context and remains self-checked. |

The completed proof attempt closes the precise uniform-integrability
obstruction that separated the L1 target from the correlation route.
It stops at (8.7). The energy argument cannot further replace
\(\Re\mathcal R_N\) by zero: after the proven tail removal its surviving
scale is still order one, and the two-/three-label mixed correlations
are not controlled by any estimate proved here. The new lemma does not
supply positive-time product Haar, a local-equilibrium theorem, a
Coulomb occupation estimate, finite hierarchy truncation, or a Gaussian
limit. No external source is indispensable to this partial result.

## 10. Recoverable handoff and issuance

| Claim | Final status |
|---|---|
| Original THM046 | OPEN; neither proved nor disproved. |
| Squared overshoot estimate (6.3) | PROVED CANDIDATE HERE / SELF-CHECKED. |
| Actual L1/L2 equivalence (6.6) | PROVED CANDIDATE HERE / SELF-CHECKED. |
| Signed correlation criterion equivalent to the full target | EXACT REDUCTION / SELF-CHECKED, contingent on the newly proved tail lemma's fresh audit. |
| Remaining actual cancellation (8.7) | OPEN, with exact admitted negation. |
| Infinite initial energy variance | Explicit failed direct route; it does not negate THM046. |
| R24 pair construction, THM047, other historical modules | No new certification or status change. |

Only this memorandum, its uniquely named artifact directory and named
sibling archive/seals are written. The packet includes complete copies
of all 26 permitted inputs, original manifest, precise exposure record,
fresh diagnostic/code/results, run history, README, exact inventories,
and a portable read-only verifier. The archive has only unique safe
relative regular members. Issued files and archive are read-only; a
correction requires a separately named issuance. No child, canonical
edit, current audit/state/history/memory read, external source, commit,
push, installation or remote change occurred.

Root should next freeze the new lemma and give its input-tail,
conditional-isometry and source-majorant steps to fresh independent
reconstruction/hostile review. If accepted, the next mathematical task
is exactly (8.7), now without a stronger-L2 escape clause. A successor
can recover the entire deduction and its first unproved line from this
packet without chat history.
