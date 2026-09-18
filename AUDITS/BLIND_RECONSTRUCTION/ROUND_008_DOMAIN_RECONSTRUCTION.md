# Round 008 statement-only reconstruction of the homogeneous corrector domain

2026-09-18 UTC. TASK-053. Fresh statement-only reconstruction on branch
`codex/hocf-r008-domain-blind`, worktree
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r008-domain-blind-20260918`,
base `3aa91391516f35afe5317a287b4f0e2e93e6384c`.

**Verdict: the frozen THM028 conjunction is proved below, within its stated
finite-N homogeneous scope.** This is a new independent reconstruction from
the statement and accepted prerequisites. Its newly constructed argument and
supporting computation have been self-checked; a separate hostile review is
still required. No independent certification of this reconstruction is claimed.
No premise from THM027 or a later operator proof is used.

## 1. Exposure, assertion, and source preflight

Exactly the 17 files named by `ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt` were read
as mathematical/instruction inputs. Each source digest and each copied digest
was verified. The task and its narrow allowlist replace the usual broad
orientation. The initial Git status/worktree metadata disclosed filenames,
branch names, and commit identifiers outside the dossier; no content of those
files, commits, reports, state ledgers, or worktrees was read. There was no
constructor/root seed, R7 proof, other audit, memory, literature, private input,
or child-agent exposure. No dependencies were installed and no commit or push
was made. Only the isolated worktree was written.

The assertion is exactly THM028: for every frozen tuple and smooth terminal h,
the full bounded Borel pair inverse has the stated joint classical and weak
regularity, with every displayed weighted bound uniform for 0 <= nu <= nu_*;
and its ordered deleted-label statistic satisfies the stated singular
N-particle identity, with absolutely integrable expected drift and a square
integrable true martingale under any bounded initial density independent of
the Brownian motions. Its exact negation is one permitted tuple, exponent,
test, or initial density violating any member of that conjunction. No
replacement statement or changed centering is used.

All constants below can depend on N, nu_*, T, d, s, h and the fixed cutoffs and
exponents. They never depend on the particular nu in its closed interval.
Initial-law estimates additionally depend on ||F0||infinity. At T=0 all
potential and particle assertions are immediate; assume T>0 in the proof.

The imported inputs and their exact use are:

| Dossier source | Input actually used | Normalization checked |
|---|---|---|
| R1 model and full algebra, sections 1, 3--5 | Definitions of P, U3, B, C and the smooth identity to be independently reconstructed | Unit Haar mass, ordered labels, denominators N^k, P=U2/2, Sym3 average of six |
| R4 full response proof, sections 2--4; THM021 | Local kernel expansion, finite-measure divergence and both compensated responses | K=-grad g, local coefficient one; R_x=-D convolution in its slot for mu=1 |
| R5 full base proof, sections 2--9; THM023 | Noncolliding auxiliary pair, bounded absolute source potential and Markov property | Relative diffusion 2nu and relative drift 2K/N |
| R5 composition/interface proofs; THM024/025 | Unique bounded Borel full inverse and exact homogeneous f | Both responses coefficient one; positive Fourier decay rate |
| R5 source/constant and symmetry addenda | Precise local-kernel source and meaning of pair symmetry | Common enlarged lower-divergence constant; exchange symmetry, not self-adjointness |
| R6 full particle proof, sections 3--8; THM026 | Actual singular particle paths, compact collision stops and density domination | Full exponent (N-1)kappa when b=0; initial state independent of Brownian motions |

These prerequisites are accepted in their task-specified scopes, not promoted
from the historical status text on their cards. Their complete supplied proofs
were inspected. In particular the R4 heat integral gives

    g(z)=|z|^(-s)+H(z), H smooth even locally,
    K(z)=s z |z|^(-s-2)+k(z), k smooth odd and O(|z|).

With p=s+2, the gamma recurrence in that proof gives
4 pi^2 c_(d,s)/c_(d,s+2)=s(d-2-s) below Coulomb. At Coulomb,
4 pi^2 c_(d,d-2)=c_d=(d-2)|S^(d-1)|, and

    D=div K=c_d(delta_0-dx).

Below Coulomb D=s(d-2-s)g_(s+2)dx. Thus D has zero total mass, its only
possible atom is at zero, K is L1, and below Coulomb
|D|(dw) <= C(1+|w|^(-p))dw locally, with p<d. These facts concern the full
periodic kernel, including its compensation. No logarithmic substitution is
made. The homogeneous response is exactly

    R=R_x+R_y=-T_D^x-T_D^y,
    T_D^x F(x,y)=integral F(x+w,y)D(dw).

For the homogeneous backward test, each nonzero frequency decays with
4 pi^2 nu |k|^2+4 pi^2 c_(d,s)|k|^(s+2-d). Rapid Fourier decay of h gives
uniform bounds on every fixed spatial derivative of f and of partial_t f for
nu in [0,nu_*]. Consequently, off the pair diagonal,

    |D^j J_t| <= C w_(s+j), j=0,1,2,
    |partial_t J_t| <= C w_s.                         (1)

The signs, factor two in relative diffusion, and all deleted-label factors are
checked again below, rather than imported as conclusions about singular tests.

## 2. A weighted convolution and occupation estimate

Weights w_q are smooth positive functions off zero on the relative torus,
equal to r^(-q) in a fixed embedded ball, and bounded above and below away from
that ball. Their values at zero are never used. Different fixed choices are
equivalent. For every 0<q<d,

    T_|D| w_q <= C_q w_q.                             (2)

Here the expression on the left is a relative-coordinate convolution, and the
same bound applies to either slot. At Coulomb it is simply
c_d(w_q+integral w_q). Below Coulomb, put r=|z| small and split the integral
of |w|^(-p)|z+w|^(-q) into |w|<r/2, |z+w|<r/2, and the complement. The first
two pieces are bounded by C r^(d-p-q). In the complement, the region |w|<=2r
has the same bound, and dyadic annuli 2r<|w|<R give a constant, a logarithm,
or C r^(d-p-q). Each is at most C r^(-q), because p<d. Smooth remainders and
outside-chart pieces are bounded by integrability. For z separated from zero,
split around the two separated singular points. This proves (2), including
pointwise finiteness off zero, without a positivity assertion about a weighted
Riesz bilinear form.

Write Z=(X,Y), A(Z)=(K(X-Y)/N,-K(X-Y)/N), and

    L=nu(Delta_x+Delta_y)+A.grad.

In the local relative chart its action is 2nu Delta_z+(2K/N).grad_z. The
symmetric matrix DA has largest eigenvalue at most

    a(Z)=a0 chi(z) r^(-p)+C0,   a0=2s/N, C0>=0,         (3)

where chi is one near zero and the constant dominates the compact remainder.
Indeed the relative block is 2 DK/N; its principal tangential eigenvalue is
2s r^(-p)/N, and its radial eigenvalue is
-2s(s+1)r^(-p)/N. The center block is zero. Also

    |D^2 A| <= C w_(p+1).                             (4)

Introduce a Poisson process of rate m=2||D||TV. At each jump choose one of the
two slots with probability 1/2 and add a displacement with law |D|/||D||TV.
Between jumps use the actual auxiliary pair diffusion. For each fixed start
this process is well defined and noncolliding on each inter-jump interval:
a nonzero jump has an absolutely continuous displacement, and a zero atom
leaves the state unchanged. A finite number of jumps cannot accumulate.
Its Markov generator is L+T_|D|^x+T_|D|^y-mI. Put
A_t^*=integral_0^t a(Z_v)dv.

For every real ell>=0 and ell<q<d there exist C,k>0 such that

    (L+T_|D|^x+T_|D|^y+ell a)w_q
        <= C w_q-k w_(q+p).                           (5)

Locally, before compact remainders, the left side divided by w_q is

    2nu q(q+2-d)r^(-2)-a0(q-ell)r^(-p).

The remainder k(z)=O(r) costs Cw_q, as do (2) and compact terms. If the
Laplacian coefficient is positive, absorb half the negative r^(-p) term
using p>2 and nu<=nu_*; its residual maximum is finite for fixed N. This is
essential in d=3, where permissible q1>1 can exceed d-2. The argument never
discards a positive diffusion term.

Stopped smooth Ito between jumps, conditioning each finite jump increment on
its mark, gives from (5)

    E[e^(mt+ell A_t^*) w_q(Z_t)]
      +k E integral_0^t e^(mv+ell A_v^*) w_(q+p)(Z_v)dv
        <= C_T w_q(Z_0), 0<=t<=T.                    (6)

More explicitly first multiply by e^(-Ct), and stop before a collision tube,
a large A_t^*, and a large jump count. Before these stops the differential
terms are bounded. At a jump exit the unbounded new weight is integrable by
(2), uniformly while the pre-jump state stays in its compact region; truncate
the mark value first if needed and pass by monotone convergence. The finite
jump compensator is therefore legitimate. Drop the nonnegative stopped
terminal term when passing occupations, and use Fatou for the terminal term.
Noncollision and finite jump count remove the stops. Undoing e^(-Ct) proves
(6), with a possibly smaller k and larger C_T. No integrability of
w_(q+p) is assumed beforehand; q+p is allowed to exceed d. Formula (6) also
holds from any deterministic intermediate time, conditionally on its state.

## 3. Signed jump representation of the full inverse

At a mark with displacement w attach sign
sigma=-dD/d|D|(w), whose absolute value is one. Let S_t be the product of all
signs before t, with empty product one. For bounded Borel F define

    Q_t F(Z)=e^(mt) E_Z[S_t F(Z_t)].                   (7)

Expanding the finite Poisson distribution gives the ordered-time Dyson series
for the base evolution perturbed by -T_D^x-T_D^y. Its absolutely convergent
bounded-input series has exactly R, with neither a missing compensator nor an
extra response factor. Thus the full inverse is

    Phi_t(Z)=E_Z integral_0^(T-t)
                   e^(mv) S_v J_(t+v)(Z_v)dv.         (8)

This is a bounded Borel function: on each inter-jump interval, conditional
absolute source occupation is bounded by the R5 constant B_N; e^(mv)<=e^(mT)
and E(number of intervals)<=1+mT. In particular the absolute right side of
(8) is bounded by e^(mT)(1+mT)B_N uniformly in the starting state. Expanding
in jumps and using this absolute bound identifies (8) with the Volterra
solution supplied by THM024/025. It is the same Phi, not a newly selected
representative or a new corrector. Pair symmetry follows either from this
construction or from the imported uniqueness. The diagonal remains excluded.

For unbounded off-diagonal F dominated by w_q, 0<q<d, (6) with ell=0 gives

    |Q_t F(Z)| <= C_T ||F/w_q||infinity w_q(Z).         (9)

The expansion and expectation are absolutely meaningful on this class. At
Coulomb (7) has rate m=4c_d and reproduces exactly
R=-c_d(2I-P_x-P_y), where P_x,P_y are Haar averages. In particular R1=0 and
Q_t1=1. Signed jumps are a proof representation, not a claim that R is a
Markov generator or that Q preserves positivity.

## 4. Justifying differentiation of (8)

This section supplies the expectation passage; pathwise flow derivatives by
themselves would not suffice.

First, for the homogeneous auxiliary pair there is an elementary useful
pathwise fact. Put gamma strictly between 1/p and 1/2. On a common probability
one event the relative additive Brownian signal is gamma-Holder on [0,T].
One proof is the Gaussian dyadic increment tail bound followed by a union
bound and Borel--Cantelli; the dyadic telescoping representation then bounds
all increments by a random constant times |t-u|^gamma. Multiplying the signal
by any fixed sqrt(nu) preserves this property; nu=0 is immediate.

Every such signal has a global off-diagonal relative flow for **all** starting
points in this auxiliary homogeneous pair problem. To prove the assertion,
consider a putative passage from radius 2r to radius r in a small local chart,
and choose the last time a at radius 2r before the first such b at radius r.
On [a,b], radii lie in [r,2r]. Fix delta=L r^p. Since p gamma>1, signal
oscillation on an interval of length delta is less than r/4 for all sufficiently
small r, uniformly in a. Subtract this signal increment and call the resulting
absolutely continuous vector Y. On [a,min(b,a+delta)],

    Y.z >= 3r^2/4, |Y|<=9r/4,
    d|Y|^2/dt >= c r^(2-p)>0,

where c>0 depends on a0 and the fixed smooth remainder, after decreasing the
radius. If b<=a+delta, monotonicity contradicts |Y_a|=2r and
|Y_b|<=5r/4. Otherwise choose L with 4+cL>81/16; the inequality at a+delta
contradicts |Y|<=9r/4. Thus such inward crossings are impossible at all small
r. Any finite-time collision would require these crossings. Local existence,
continuation on collision-excluded compact sets, and this argument prove the
claim. Smooth dependence on initial state now follows by the usual local
integral-equation difference quotients, with the signal subtracted, and covers
a compact family of starts by finitely many such neighborhoods. This stronger
pathwise fact is used only for this auxiliary pair, not asserted for the
N-particle process of THM026.

For a fixed compact straight initial segment lying off the diagonal, the
entire segment also survives the finite jump construction almost surely.
Condition on the Brownian path and jump times. Before the first jump its
relative image is a smooth curve. In dimension d>=3 this curve has Haar
measure zero: subdividing a bounded-derivative parametrization into M pieces
covers it by M balls of radius C/M, with total volume O(M^(1-d)). A jump with
an absolutely continuous displacement almost surely avoids that curve; the
zero atom is harmless. Induct through the finite marks. On survival, compactness
and local smooth dependence give smooth dependence in a neighborhood of the
whole initial segment. This proves the fundamental theorem of calculus along
any fixed segment almost surely; it avoids a possible unjustified derivative
exchange across an exceptional set of starting points.

Let H_v be the first spatial derivative of this flow and Q_v^(2) its second
spatial derivative, for any fixed realization that survives locally. Jumps
are translations, so their first derivative is I and second derivative zero.
The integral-equation variational equations and (3)--(4) give

    |H_v| <= e^(A_v^*),
    |Q_v^(2)| <= C e^(A_v^*)
                  integral_0^v e^(A_u^*) w_(p+1)(Z_u)du.  (10)

The first inequality uses the largest eigenvalue of the symmetric DA, not its
much larger absolute radial eigenvalue. The second follows by variation of
constants: propagation from u to v costs e^(A_v^*-A_u^*) and its quadratic
input costs |H_u|^2. These are finite on each realized compact path.

Formal derivatives of the random integral in (8) are genuine pathwise
derivatives by this local flow construction. Their absolute values are bounded
(up to fixed constants and e^(mT)) by

    G1 = integral_0^(T-t) e^(A_v^*) w_(s+1)(Z_v)dv,

    G2 = integral_0^(T-t) e^(2A_v^*) w_(s+2)(Z_v)dv
       + integral_(0<u<v<T-t) e^(A_v^*+A_u^*)
                    w_(s+1)(Z_v)w_(p+1)(Z_u)du dv.    (11)

Formula (6), with (ell,q)=(1,q1), bounds E G1 by Cw_q1 because
s+1<q1+p. For the first term in G2 use (ell,q)=(2,q2), possible since q2>2.
For the double term condition at u and apply the G1 occupation bound to the
remaining interval. The result is bounded by

    C E integral_0^(T-t) e^(2A_u^*)
                         w_(p+1)(Z_u)w_q1(Z_u)du
        <= Cw_q2(Z_0),                               (12)

using q2>q1+1 and (6) with (ell,q)=(2,q2). This is the precise origin of the
second exponent gap.

For uniform integrability and continuity choose 1<alpha<q1 and
alpha+1<beta<q2. Choose r>1 sufficiently close to one that

    alpha>r, beta>2r,
    alpha+p>r(s+1),
    beta+p>r(p+1)+alpha.                             (13)

All four strict gaps are available. Jensen on one time integral, and on the
double time simplex, reduces the r-th moments of (11) to the same occupation
calculations with potentials r a and 2r a and weights alpha and beta.
Conditional expectation at u gives, explicitly for the double term, an inner
bound C w_alpha(Z_u) for the occupation of w_(r(s+1)); the outer source is
w_(r(p+1)+alpha), absorbed by w_(beta+p). The first Hessian term also fits
beta+p>r(s+2), which follows by taking r still closer to one if necessary.
Consequently

    E G1^r <= C w_alpha(Z_0),
    E G2^r <= C w_beta(Z_0).                          (14)

Constants are uniform in t and nu in their stated ranges. On compact sets of
initial points these are uniform finite bounds.

For a fixed segment, apply its almost-sure fundamental theorem of calculus to
the random integral, then Fubini using (14). The expectation has the expected
first weak derivative. Apply the same argument to the random first derivative
to obtain its second weak derivative. For a convergent sequence of initial
points and times, the local flow and the time integrals converge almost surely
on the good event for its limit start. Formula (14) supplies uniform
integrability; hence their expected first and second derivatives converge.
Continuous weak derivatives are classical derivatives (integrate on coordinate
segments, or mollify locally and pass uniformly). Thus

    sup_t |grad Phi_t|/w_q1 <= C,
    sup_t |D^2 Phi_t|/w_q2 <= C,                      (15)

and these derivatives are jointly continuous off the diagonal, including the
terminal limit zero. No singular-flow derivative was passed through expectation
without both the segment argument and a moment bound.

## 5. Time derivative, the equation, and global weak derivatives

Autonomy of the homogeneous base process and of both responses gives from (8)

    partial_t Phi_t
      =-Q_(T-t) J_T + integral_0^(T-t) Q_v(partial_t J_(t+v))dv. (16)

For fixed off-diagonal start, differentiating in t uses (1), (9) with q=s,
and dominated time integration. Boundary-time evaluation is legitimate:
choose r>1 with rs<d, apply (9) to w_(rs), and obtain uniform integrability of
J evaluated at nearby terminal times. The path has no jump at any prescribed
terminal time almost surely; away from its finite jumps it is continuous.
These facts, local dependence on the initial state, and the same moment bound
prove that (16) is jointly continuous off the diagonal. At t=0,T it is the
one-sided derivative. In particular

    |partial_t Phi_t| <= C w_s.                      (17)

No time derivative of a Brownian path is being taken.

The accepted martingale characterization of Phi along the auxiliary base pair
has integrated source J+R Phi. Independently, (15)--(17) permit classical
Ito for Phi on every collision-excluded compact stop. The difference of those
two local martingales is the time integral of the continuous function

    partial_t Phi+L Phi+R Phi+J.

It is both a continuous finite-variation process and a local martingale and
therefore zero. Starting at every off-diagonal state and then letting elapsed
time decrease to zero proves pointwise

    partial_t Phi+nu(Delta_x+Delta_y)Phi+B Phi/N+R Phi=-J. (18)

Continuity of R Phi off the diagonal follows directly from its convolution:
at Coulomb it is multiplication plus the continuous background averages;
below Coulomb split near the two separated singularities and use bounded Phi,
local continuity and (2), or the integrable local tail bound. Thus this step
uses a classical continuous equation, not an a.e. generator slogan.

Let chi_epsilon remove a relative epsilon-neighborhood of the diagonal. Since
Phi is bounded, the cutoff boundary error for its first weak derivative is
O(epsilon^(d-1)). The error for the derivative of its first derivative is
O(epsilon^(d-1-q1)), which vanishes because q1<d/2<d-1. The claimed derivative
integrals converge because q1<d and q2<d. This proves that the classical
off-diagonal derivatives extend as global weak derivatives, without a delta
term supported on the diagonal. Moreover 2q1<d gives Phi in Haar H1, and
q2<d gives Phi in W^(2,1), uniformly in time. For time differentiation use
(17) and s<d in Fubini and dominated integration.

Crucially, solve (18) for the internal derivative:

    B Phi=N[-J-partial_t Phi-nu(Delta_x+Delta_y)Phi-R Phi]. (19)

Every term on the right is Haar L1 uniformly in time, by (1), (15), (17),
bounded Phi and bounded R. Thus B Phi is L1. The crude product
|K| |grad Phi| can fail to be L1 and is not used for this conclusion.

The background quantities

    q_t(x)=integral Phi_t(x,y)dy,
    a_t(x)=integral grad_x Phi_t(x,y)dy,
    r_t=integral Phi_t(x,y)dxdy

are C1 in time and C2 in their spatial variables where applicable. Their
indicated derivatives can be integrated under the sign of integration:
uniform relative tails are C epsilon^(d-q1), C epsilon^(d-q2), and
C epsilon^(d-s). Splitting into these tails and their compact complement
proves continuity, as well as the differentiated identities. In particular
integral Delta_y Phi(x,y)dy=0, and the analogous identities hold in the other
slot. These are consequences of the weak derivative result, not chosen
values on a diagonal.

## 6. Singular particle algebra without partial-diagonal substitutions

Use the actual N-particle process from THM026 with b=0, and set
M_N=||F0||infinity exp((N-1)kappa T). For every nonnegative Haar-integrable
configuration function G and every time, that theorem gives

    E G(X_t) <= M_N integral G.                       (20)

This applies to any initial N-body density independent of the noises; its
coordinates need not be mutually independent or exchangeable. No evolved iid
estimate is used.

On a compact collision stop, the actual statistic is a C1-time, C2-space test:

    P[Phi]=1/(2N^2) sum_(i!=j) Phi(X_i,X_j)
             -1/N sum_i q(X_i)+r/2,
    grad_i P=1/N^2 sum_(j!=i) grad_x Phi(X_i,X_j)-a(X_i)/N. (21)

Independent noises yield no mixed second derivative between distinct labels.
The local drift is P[(partial_t+nu Delta_pair)Phi] plus

    1/N^3 sum_(i!=j) sum_(k!=i) K_ik.grad_x Phi_ij
      -1/N^2 sum_(i!=k) K_ik.a(X_i).                  (22)

Split k=j first and pair the two orientations. Its entire contribution is
D2[B Phi]/(2N). Combining before taking absolute values is necessary; individual
K_ij.grad_x Phi_ij need not have the asserted Haar integrability. The remaining
three-distinct-label contribution is D3[C Phi], with C the average of six.

Here is a direct background-contraction calculation that uses no evaluation
such as C(x,x,z). Set F=C Phi and
H(x,y)=K(x-y).(a(x)-a(y)). With all equalities a.e. where required,

    6 integral F(x,y,z)dz = H(x,y)+R Phi(x,y),
    3 integral F(x,y,z)dy dz = A_1 q(x),
    integral F dxdy dz=0,
    integral R Phi(x,y)dy=A_1 q(x),
    integral R Phi dxdy=0,                           (23)

where A_1 q(x)=integral K(z-x).grad q(z)dz. In the first identity two of the
six terms vanish by integral K=0, two give H, and the last two give the two
responses. Integrating it again gives the second identity. Response integration
by parts is legitimate here: if x!=y, the kernel is smooth at z=x, so the
finite-measure flux formula retains the Coulomb atom; near z=y the force
K(z-x) is smooth and bounded Phi makes the boundary error O(epsilon^(d-1)).
The derivative itself is locally L1. Absolute triple integrability, proved
below, permits all the remaining Fubini operations. No trace on x=y is taken.

The literal ordered definition of U3 and (23) now give

    U3[F]+P[R Phi]=D3[F]-D2[H]/2.

Since the last term of (22) equals -D2[H]/2, (22) is exactly

    U3[C Phi]+P[R Phi]+D2[B Phi]/(2N).

Finally use the literal U2 definition:

    D2[B Phi]/(2N)=P[B Phi/N]
               +(1/N)rho[(B Phi)_mu]+(1/(2N))integral B Phi. (24)

Equations (18) and (21)--(24) prove, at each compact stop, exactly the displayed
THM028 drift and its coefficients. In particular the order-zero contraction
and order-one contraction survive, and U3 does not vanish at N=2: only its
all-distinct empirical triple term vanishes there.

## 7. Absolute expected drift and true-martingale passage

The triple kernel is absolutely Haar integrable. Indeed each of its six terms
is bounded by a permutation of

    |K(x-z)| |grad_x Phi(x,y)|,

whose triple integral is ||K||1 ||grad_x Phi||1 by first integrating z. The
same statement holds uniformly in time. All literal empirical/background terms
of U3 therefore have finite expected absolute time integrals by (20) and
Fubini: integrating out unselected particle coordinates costs no factor other
than the already explicit M_N. This treats intersections of partial collision
sets as well as an isolated diagonal.

Similarly J is L1, and (19) gives B Phi in L1, so every term of P[J],
rho[(B Phi)_mu], and integral B Phi has finite expected absolute occupation.
The background derivatives used in (21) are bounded, as established in section
5. Values assigned on true coinciding coordinates alter none of these Haar
integrals, none of the distinct-label evaluations of the noncolliding process,
and none of the time-integrated quantities under (20). There is no extra
collision trace or diagonal convention hidden in (23)--(24).

For the martingale, Jensen and the finite-sum Cauchy--Schwarz inequality give

    integral sum_i |grad_i P|^2
       <= 2[(N-1)^2/N^3+1/N] ||grad_x Phi||2^2
       <= (4/N)||grad_x Phi||2^2.                    (25)

The norm is finite because 2q1<d. Consequently

    E integral_0^T 2nu sum_i |grad_i P_t(X_t)|^2 dt
       <= (8nu_* T M_N/N) sup_t ||grad_x Phi_t||2^2 < infinity. (26)

The prescribed stochastic integral is therefore a square-integrable true
martingale, and its bracket is exactly 2nu sum_i |grad_iP|^2dt. At nu=0 it is
identically zero; no division by nu or estimate uniform as nu_* tends to
infinity is used.

Let compact stops exhaust the collision-free N-particle configuration space.
THM026 gives a strictly positive pathwise minimum separation on [0,T], so
these stops eventually exceed T on each good path. The statistic P is bounded
uniformly over all configurations off collisions, by bounded Phi and its
background integrals. Its stopped values thus converge boundedly at every
time. The absolute occupation estimates above give convergence of every
drift term in L1, and (26) gives convergence of the stopped martingales in L2
(and uniformly in time in L2 by the elementary maximal inequality). Passing
the stopped identity proves the global integral identity, hence the stated
differential notation, on the whole interval. This completes the actual
singular-particle passage.

## 8. Independent falsification route and exact checks

The analytic proof route was a finite signed-jump representation, a radial
occupation inequality, and a justified flow-differentiation passage. The
separate falsification route recomputes raw Fourier particle generators from
literal subset/deleted-label definitions and tests the dangerous radial
coefficients by exact rational Taylor algebra. Neither route reads another
R7/R8 construction. Both are within this same new reconstruction context;
this does not replace hostile review.

The companion `round008_domain_exact_checks.py` uses only Python's standard
library, exact fractions and finite Laurent/Taylor polynomials. It has no
random seed, floating point tolerance, numerical solution, or dependency.
Its execution passed **285 exact checks**. Its JSON records every check and
verifies all 17 copied input digests. It checks:

- N=2 and N=3 (and an additional finite N): the full raw particle generator
  versus both responses, the six-permutation C, exact U3, internal B/N,
  and both lower/scalar terms, for constant, separable, difference-mode,
  one-body-sum and mixed-mode symmetric pair tests, with nu=0 and positive nu.
- The smooth one-coordinate Fourier diagnostic is embedded in dimension d>=3.
  Computation uses angular derivatives; restoring a spatial derivative multiplies
  each first derivative by 2pi and each diffusion term by (2pi)^2. These are
  exact smooth algebra tests, not replacements for the frozen Riesz kernel.
- Exact local Taylor derivatives of r^(-s) and r^(-q) at a unit axis point,
  including Coulomb in d=3 and higher dimensions, recover the tangential and
  radial eigenvalues, Laplacian, relative factor two, and q-ell absorption gap.
- Strict exponent and higher-moment gaps, including d=3 where the weight's
  diffusion term is positive, are checked rationally. The proof absorbs this
  term and never assumes its sign is nonpositive.
- Constant terminal h has J=0, hence Phi=0 by uniqueness, so every drift and
  bracket is zero. A nonzero constant pair test is also checked: P[c]=-c/(2N),
  which detects an incorrect factorial or centering convention.
- At Coulomb both the atom and the negative Haar compensation are retained:
  each one-slot nonzero Fourier response multiplier is -c_d, whereas the
  zero-frequency multiplier is zero. Dropping either part fails the constant
  test. At zero noise the occupation argument, regularity, algebra and law
  passage still hold, and the stochastic integral vanishes.

The exact checker is supporting verification of finite formulas, not a
computational proof of the analytic domain assertion. Source normalizations,
localization, moment bounds and weak-derivative extensions are proved in the
text. No literature novelty claim is made.

## 9. Per-claim disposition and handoff

| Frozen claim | Reconstruction verdict | Decisive argument |
|---|---|---|
| Same bounded Borel full inverse, both responses | Proved from accepted inverse module | Signed Dyson series, (7)--(8) |
| C1 time and C2 space off diagonal, joint continuity and endpoint derivatives | Proved here | Segment survival, r-th moments, (10)--(17) |
| Every permitted q1,q2 and uniformity over [0,nu_*] | Proved here | Strict gaps in (5), (12)--(14); finite absorption of positive diffusion |
| Global Haar H1 and W^(2,1) weak derivatives | Proved here | Vanishing cutoff errors and 2q1<d, q2<d |
| Classical full pair equation | Proved here | Local Ito compared with accepted source martingale, (18) |
| L1 time derivative and internal B Phi | Proved here | (17) and structural equation (19) |
| Exact singular N-particle identity and all coefficients | Proved here | Distinct-label direct calculation, (21)--(24) |
| Mixed/background/partial-collision integrals | Proved here | Triple product integrability, weak derivatives and density domination |
| Absolute expected drift and square-integrable true martingale | Proved here | (20), (25)--(26), passage through compact collision stops |

There is no unsupported line left in the frozen finite-N conjunction in this
reconstruction. The new proof's most delicate auditable lines are the segment
argument and uniform-integrability bounds of section 4, and the structural
use of (18) in (19). They must receive separate hostile scrutiny. This report
is not a theorem promotion by the root and not an audit of its own proof.

The next scientific line outside THM028 is quantitative control uniform in N
of the interacting-law residuals, lower contractions and corrector brackets,
and their consequences for centering and fluctuation limits. Nothing here
proves a CLT, critical hierarchy closure, inhomogeneous domain theorem,
beta-to-zero uniformity, or logarithmic assertion. The explicit fixed-N
M_N factor remains.

Created deliverables are this report, the independent exact checker, its JSON,
the copied 17-input manifest, and the output SHA256 manifest. Input seals are
rechecked after construction. All final output paths are confined to
`AUDITS/BLIND_RECONSTRUCTION/` in this worktree. No canonical state file,
existing proof, immutable audit, or root file was edited. No TeX source is
needed for this Markdown/checker handoff, whose final message contains no
mathematical LaTeX. Once issued, these bytes and their output seal are immutable;
a correction would require a new superseding report.

Executed verification commands:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/round008_domain_exact_checks.py
  PASS: 285 exact checks; 17 input digests verified in the generated JSON.
git diff --check
  PASS; copied inputs and new untracked deliverables are also checked directly.
shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt
  PASS: all 17 files.
shasum -a 256 -c AUDITS/BLIND_RECONSTRUCTION/ROUND_008_DOMAIN_OUTPUT_SHA256SUMS.txt
  PASS: all four sealed output files.
```

The final direct checks verify terminal newlines, absence of trailing whitespace,
input byte identity, the required report/checker/JSON paths, and output hashes.
The manifest lists the report, checker, JSON and copied input manifest; it is
not self-hashed. No TeX was modified or created and no TeX build was run.
