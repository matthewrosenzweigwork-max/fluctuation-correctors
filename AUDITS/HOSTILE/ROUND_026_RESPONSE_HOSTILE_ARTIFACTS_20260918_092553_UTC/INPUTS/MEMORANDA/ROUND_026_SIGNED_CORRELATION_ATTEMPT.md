# Round 026 — conditional response and a Coulomb angular-trace obstruction

TASK110, 2026-09-18 UTC. Ordinary fresh Astra Max construction at base
`06bf56dae256085646228aa28159210b567bf409`, in the assigned isolated worktree.
**The signed-correlation target remains OPEN. No admitted positive-limsup
negation is proved. All new conclusions below are SELF-CHECKED candidates.**

The attempted mechanism was cutoff-uniform sensitivity of the actual
backward N-particle response. The mechanism fails in a stronger way than
an unbounded force Hessian: at every fixed finite N and positive noise,
the backward response of one smooth empirical cosine is not in Haar
W1,4 for all sufficiently small positive times. A close initial pair
separates to radius of order t^(1/4), retaining its initial direction to
leading order. The smooth symmetric terminal observable consequently
has a nonconstant angular trace at the pair collision. Its nonzero
degree-two spherical projection proves the fourth-gradient obstruction.
The full periodic dynamics and all other labels are retained in this
argument. No initial law is substituted in the asserted Haar conclusion.

A new exact conditional-response decomposition also separates the
remaining modal defect into a conditional-mean error and a nonnegative
noise-response cost. The latter has an exact heat-cutoff Dirichlet
representation with its true martingale and cross brackets. The new
obstruction rules out global C1 and Haar fourth-gradient bounds for
that route. It does not rule out the actual L2 estimates still needed.

## 1. Frozen target, source boundary, and normalization

Use precisely THM049: unit Haar torus T4, c=4 pi^2,
g_hat(k)=|k|^-2 for k nonzero and g_hat(0)=0, K=-grad g,
independent standard four-dimensional Brownian drivers, and

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)dt+\sqrt{2\nu}\,dW_i,
 \qquad X(0)\sim dx^{\otimes N},\qquad \nu=\beta^{-1}>0.
 \tag{1.1}
\]

The target is Re Rcal_N(k,T) tending to zero for every fixed nonzero
integer mode, finite T, and sequence beta_N/sqrt(N) tending to a finite
positive lambda. Rcal is the exact expression reconstructed in Section 2.
Its admitted negation is the existence of such fixed k,T,lambda and
sequence with positive limsup. A fixed-N sensitivity failure is not
that negation. The original THM046 uses sqrt(N min(beta_N,1)) and its
absolute value after the time integral; no changed preparation, test,
horizon, or temperature is asserted here.

All 17 allowlisted inputs passed the supplied SHA-256 manifest before
mathematics. Their complete byte copies and the original manifest are in
the packet. The supplied R24/R25 narratives and THM048/049 cards are
candidate construction inputs, not certified premises. The argument
below reconstructs the finite-N portion of THM049 it uses. It does not
use or certify the R25 squared-tail theorem or its L1/L2 equivalence.
The exact input/exposure record lists partial and hash-only reads.
Task-specific isolation supersedes the general request to read other
README/spec/state files or edit ledgers. Root owns future identifiers,
canonical state, and independent review.

The local kernel facts needed here are reconstructed from the allowed
R4 heat calculation. With the unit-torus heat kernel p_u,

\[
 g(z)=c\int_0^\infty(p_u(z)-1)du=|z|^{-2}+H(z)
 \quad (0<|z|<1/3),\qquad H\text{ smooth and even}.
 \tag{1.2}
\]

The Fourier integral is c/(4 pi^2 |k|^2). Integrating the central
Euclidean Gaussian gives coefficient one; derivatives of noncentral
lattice terms are exponentially integrable at small u, and the
large-time remainder is exponentially integrable. Thus

\[
 K(z)=2z|z|^{-4}+K_{\rm reg}(z),\quad
 |K_{\rm reg}(z)|\le C|z|,\quad
 \operatorname{div}K=c(\delta_0-dx).
 \tag{1.3}
\]

The atom has flux 2|S3|=4 pi^2 and the constant restores zero total
mass. K and g are Haar integrable and smooth away from zero.

Here are the singular-domain facts actually used, with their mechanism.
Set H_N=N^-1 sum_(i<j) g(x_i-x_j). Its shift by
-(N-1)inf(g)/2 is nonnegative with compact collision-free sublevels.
Local smooth force cutoffs and additive-noise Picard iteration give
unique paths up to these energy exits. On an energy sublevel,

\[
 dH_N=-\sum_i|B_i|^2dt+\nu c(N-1)dt
       +\sqrt{2\nu}\sum_i\nabla_iH_N\cdot dW_i.
 \tag{1.4}
\]

Both coordinates of each unordered pair contribute, so Delta H_N is
c(N-1) off collisions. The expected shifted energy bounds the
probability of reaching height L by (initial shifted energy plus
nu c(N-1)T)/L. Letting L increase proves global noncollision for each
collision-free deterministic start, and then for iid Haar. Stopping
first and applying Fatou proves integrability of the full drift-square
action. Isometry then removes the energy martingale stop in L2.
This supplies no individual pair-force-square estimate.

For g_epsilon=p_epsilon*g, K_epsilon converges in local C1 away
from zero. Every realized singular path has positive minimum pair
distance on a finite time interval. The same-noise difference, stopped
before half that distance is lost, obeys Gronwall; hence the heat paths
converge uniformly on the interval at fixed N,nu and starting point.
All convergence here precedes any N limit. Moreover
div B_epsilon >= -c(N-1), so the smooth random-flow determinant is
at least exp[-c(N-1)t]. Change of variables from initial Haar and
Brownian averaging, followed by bounded continuous-test passage and
open-set approximation, yield actual density at most exp[c(N-1)T].
This bound is used only for fixed-N first-moment integrability, never
for an N-uniform estimate. Translation and permutation equivariance
give Haar one-body marginals and exchangeability, not product law.

## 2. Reconstruction of the exact modal identity

For e_k(x)=exp(2 pi i k.x), put ell_k=c|k|^2,
a=c+nu ell_k, a_tilde=a-c/N, A=exp(-aT), and Z=eta_N[e_k].
Distributional integration by parts using both terms in (1.3) gives

\[
 \int K(x-y)\cdot(\nabla e_k(x)-\nabla e_k(y))dy=-ce_k(x).
 \tag{2.1}
\]

The double background is zero. If j_k is J_k+c(e_k(x)+e_k(y)),
it has zero Haar rows, and exact ordered-label counting gives

\[
 U=(2N^2)^{-1}\sum_{i\ne j}j_k(X_i,X_j),\qquad
 P_N[J_k]=U+(c/N)Z,
\]
\[
 dZ=-\widetilde aZdt+Udt+dM_k,
 \qquad M_k=\frac{\sqrt{2\nu}}N\sum_i\int\nabla e_k(X_i)dW_i.
 \tag{2.2}
\]

The extra c/N row is positive. The true brackets are

\[
 d\langle M_k,\overline M_l\rangle
 =\frac{2\nu c(k\cdot l)}N Z_{k-l}dt,\qquad
 d\langle M_k,M_l\rangle
 =-\frac{2\nu c(k\cdot l)}N Z_{k+l}dt.
 \tag{2.3}
\]

In particular the diagonal conjugate bracket is 2 nu ell_k/N.
The weak source J is bounded by C_k(1+dist(x,y)^-2); the actual
fixed-N density bound proves absolute time integrability of every
source paired with a bounded current or initial mode. Thus localization
passes in L1 and the bounded-gradient martingales pass in L2. No
instantaneous source square or two-time density is needed.

There are 2N(N-1) overlap triples and N(N-1)(N-2) distinct triples
in the covariance of U and Z, with the denominator 2N^2 after
multiplication by N. Consequently, using exactly the A2,A3,B2,B3 of
THM049,

\[
 N\mathbb E[U\overline {Z(t)}]=F_N,
 \quad N\mathbb E[U\overline {Z(0)}]=G_N,
\]
\[
 F_N=\frac{N-1}N A2+\frac{(N-1)(N-2)}{2N}A3,
 \quad G_N=\frac{N-1}N B2+\frac{(N-1)(N-2)}{2N}B3.
 \tag{2.4}
\]

Omit the third-label terms at N=2. For V=N E|Z(t)|^2 and
R=N E[Z(t) conjugate Z(0)], product Ito and initial measurability give

\[
 V'=-2\widetilde a V+2\nu\ell_k+2\Re F_N,
 \quad R'=-\widetilde a R+G_N,\qquad V(0)=R(0)=1.
 \tag{2.5}
\]

Only the current slot evolves in R. The martingale is orthogonal to
time-zero information, not independent of the current mode. Solving
these absolutely continuous equations yields

\[
 D_N:=N\mathbb E|Z(T)-AZ(0)|^2
 =(e^{-\widetilde aT}-A)^2
 +\frac{\nu\ell_k}{\widetilde a}(1-e^{-2\widetilde aT})
 +2\Re\mathcal R_N,
 \tag{2.6}
\]
\[
 \mathcal R_N=\int_0^T
 [e^{-2\widetilde a(T-t)}F_N(t)
       -Ae^{-\widetilde a(T-t)}G_N(t)]dt.
 \tag{2.7}
\]

Since a_tilde>=c/2, the two explicit terms are respectively O(N^-2)
and O_k,T(nu) on the critical tail. In particular Re Rcal has negative
part o(1), and its vanishing is equivalent to D_N tending to zero.
This finite-N reconstruction does not use the separate L1/L2 theorem.

## 3. The conditional-response proof attempt

Let P_t^N be the actual Markov semigroup furnished by the measurable
path construction, and let F(x)=N^-1 sum_i e_k(x_i). Its magnitude is
at most one. Define

\[
 C_N=N\|P_T^NF-AF\|_{L^2(dx^{\otimes N})}^2,
 \qquad
 J_N=N\mathbb E|F(X_T)-P_T^NF(X_0)|^2.
 \tag{3.1}
\]

Conditional expectation given X0 and expansion of the square give the
exact, absolutely integrable, nonnegative decomposition

\[
 \boxed{D_N=C_N+J_N.}                           \tag{3.2}
\]

The cross term vanishes because the second difference has zero
conditional mean, not because the two terms are independent. The
normalization is N in both terms. Thus the target is exactly the two
vanishings C_N->0 and J_N->0, in the same critical sequence and fixed
mode/time. This is a response representation of the signed cancellation,
not its proof.

The noise term also has a precise singular-limit definition requiring
no guessed differentiability of P^N. For the actual heat cutoff put
u_s^epsilon=P_(T-s)^(N,epsilon)F. Smooth flow differentiation or the
heat integral equation gives the smooth backward solution. Ito gives

\[
 d[u_s^\epsilon(X_s^\epsilon)]
 =\sqrt{2\nu}\sum_i\nabla_i u_s^\epsilon(X_s^\epsilon)\cdot dW_i,
\]
\[
 J_N^\epsilon
 =2\nu N\int_0^T\mathbb E\sum_i
                  |\nabla_i u_s^\epsilon(X_s^\epsilon)|^2ds.
 \tag{3.3}
\]

At this fixed cutoff all integrands are bounded, so these are true L2
martingales. Their bracket is the integrand on the right without N.
Their cross bracket with the original forward empirical martingale is

\[
 d\langle u^\epsilon(X^\epsilon),\overline{M_k^\epsilon}\rangle_s
 =\frac{2\nu}N\sum_i\nabla_i u_s^\epsilon(X_s^\epsilon)
              \cdot\overline{\nabla e_k(X_i^\epsilon(s))}\,ds.
 \tag{3.4}
\]

For the backward one-body martingale multiply the right side by
exp[-a(T-s)]. No cross bracket has been replaced by zero.
The path convergence and |F|<=1 give convergence of all endpoint
second moments and of P_T^(N,epsilon)F in Haar L2. Therefore

\[
 J_N=\lim_{\epsilon\downarrow0}
 2\nu N\int_0^T\mathbb E\sum_i
 |\nabla_i P_{T-s}^{N,\epsilon}F(X_s^\epsilon)|^2ds.
 \tag{3.5}
\]

This is a limit of nonnegative numbers, not an exchange of a gradient
with the singular limit. Its existence follows from the bounded
conditional variance identity. It is at each finite N before N tends
to infinity.

The concrete attempted estimate was to propagate the empirical test's
gradient size through the backward flow, uniformly over starting states
and the cutoff:

\[
 \sup_{\epsilon>0}\sup_x\sum_i
 |\nabla_iP_t^{N,\epsilon}F(x)|^2\le C_{k,T}/N,
 \quad 0\le t\le T.                             \tag{3.6}
\]

It would make (3.5) at most 2 nu T C_(k,T), hence o(1). It would
still leave the conditional-mean response in (3.1) to be compared with
the prescribed linear semigroup; bounded sensitivity alone never
proves that comparison. Differentiating the cutoff flow gives a
Jacobian equation containing the interaction Hessian. Instead of
assuming a favorable sign or bounded growth in that equation, the
following actual dynamic calculation tests its implication (3.6).
It proves (3.6) false even with an arbitrary finite constant depending
on N,nu,t. It also rules out a Haar L4 replacement. This is the first
failed line of this concrete mechanism.

## 4. Local actual-dynamics expansion at one pair collision

Fix any integer N>=2 and any finite nu>0. They stay fixed throughout
this section; the constants are not claimed uniform in N or nu.
Choose a compact set Q, of positive volume in local coordinates, of
q=(z,x3,...,xN) with all the displayed distinct points separated by a
fixed distance. For N=2, q consists only of z. Choose slightly larger
coordinate neighborhoods and a radius R>0 so that x1=z+y/2 and
x2=z-y/2, |y|<R, stay separated from every other particle; all other
pairs also stay separated. Initially y=r theta, theta in S3. Let tau
be the first exit of y or of the slow coordinates from these larger
neighborhoods. All constants below are uniform in q in Q and theta.

Before tau, exact subtraction and addition of the two particle
equations give independent Brownian directions with

\[
 dY=\alpha Y|Y|^{-4}dt+b(Y,q)dt+2\sqrt\nu\,dB,
 \quad \alpha=4/N,\quad |b(Y,q)|\le L|Y|,
 \tag{4.1}
\]

while the center has noise sqrt(nu) dB_center and bounded drift, and
each other coordinate has its original noise sqrt(2nu) dW_j and
bounded drift. The internal pair forces cancel from the center.
The other-label contribution to b is
N^-1 sum_(j>=3)[K(z+y/2-xj)-K(z-y/2-xj)], which is O(|y|)
on this domain. The smooth local remainder in (1.3) has the same bound.
The relative Brownian generator is 2nu Delta, not nu Delta. Center
and relative Brownian cross brackets are zero; the drift may couple
them, and no process independence is used.

Every application of Ito below first stops above a positive lower
pair radius. The actual noncollision result allows its removal. The
moment bounds displayed below are independent of that lower stop.
Write R_s=|Y_(s wedge tau)| and m_p(s)=E R_s^p. For even p>=4,
the radial generator and an upper bound are

\[
 L|y|^p=p\alpha |y|^{p-4}+2\nu p(p+2)|y|^{p-2}
                         +p|y|^{p-2}y\cdot b,
\]
\[
 m_p(t)\le r^p+\int_0^t
 [p\alpha m_{p-4}(s)+2\nu p(p+2)m_{p-2}(s)+pL m_p(s)]ds,
 \tag{4.2}
\]

with the p=4 first term bounded by 4 alpha. Indicators of s<tau in
the exact identity were only discarded from nonnegative upper bounds.
For 0<t<=t0<=1, the p=4 inequality and m2<=sqrt(m4) first give
m4<=C(r^4+t), by sqrt(x)<=1+x and Gronwall. Inductively (4.2)
gives, for every even p>=4,

\[
 m_p(t)\le C_p(r^4+t)^{p/4},\qquad
 m_2(t)\le C(r^4+t)^{1/2}.                       \tag{4.3}
\]

For the induction, integrate (r^4+s)^((p-4)/4) and
(r^4+s)^((p-2)/4); both are bounded by a constant times
(r^4+t)^(p/4) on this fixed bounded interval, and then apply Gronwall.
For p=6 use m2 already established. These are stopped-process bounds.

Taking p=8 controls pair exit. A slow-coordinate exit requires a
Brownian displacement of a fixed positive size before time t once
t is below the distance margin divided by twice its bounded drift.
The coordinate reflection bound for Brownian maxima is exponentially
small in 1/t and hence O(t^2). A union over finitely many coordinates
therefore gives

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}\mathbb P(tau\le t)
 \le C t^2.                                     \tag{4.4}
\]

No heat-cutoff noncollision estimate is asserted here.

The exact stopped fourth-radius equation is

\[
 R_t^4=r^4+4\alpha(t\wedge\tau)
 +\int_0^{t\wedge\tau}[48\nu|Y_s|^2+4|Y_s|^2Y_s\cdot b_s]ds
 +8\sqrt\nu\int_0^{t\wedge\tau}|Y_s|^2Y_s\cdot dB_s.
 \tag{4.5}
\]

Its martingale bracket is 64nu integral |Y|^6 ds. All moments needed
for isometry follow from (4.3). Consequently the drift error has
limsup O(nu t^(3/2)+L t^2), the martingale L1 error has limsup
O(sqrt(nu) t^(5/4)), and replacing t wedge tau by t costs O(t^3).
Divide |R_t^4-4 alpha t| by sqrt(4 alpha t), using
|sqrt(x)-sqrt(y)|<=|x-y|/sqrt(y), to obtain

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
 E|R_t^2-\sqrt{4\alpha t}|\le C t^{3/4}.
 \tag{4.6}
\]

The positive power alpha and all constants stay at fixed N. This
estimate is not a critical N-uniform estimate.

To control the angle, the squared-radius identity is

\[
 d|Y|^2=(2\alpha|Y|^{-2}+16\nu+2Y\cdot b)dt
                    +4\sqrt\nu Y\cdot dB.
 \tag{4.7}
\]

The stopped identity bounds the expected integral of |Y|^-2 by
(m2(t)+2L integral m2)/(2 alpha). Fatou removes the lower stop,
and (4.3) implies its limsup as r->0 is at most C sqrt(t).
Thus the directional stochastic integral is a true L2 martingale.
For Theta=Y/|Y| its exact equation is

\[
 d\Theta=\frac{(I-\Theta\Theta^T)b}{|Y|}dt
       -\frac{6\nu}{|Y|^2}\Theta dt
       +\frac{2\sqrt\nu}{|Y|}(I-\Theta\Theta^T)dB.
 \tag{4.8}
\]

Taking the scalar product with its initial direction theta, then
expectations, gives

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
 E|\Theta_{t\wedge\tau}-\theta|^2
 \le C(\nu\sqrt t+t).
 \tag{4.9}
\]

This uses |b|/|Y|<=L and 2(1-E Theta.theta), not an estimate on
an instantaneous force square. Combining (4.6), (4.9), Cauchy--Schwarz,
and m4=O(t) proves for each fixed k

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
 \left|E(k\cdot Y_{t\wedge\tau})^2
                   -\sqrt{4\alpha t}(k\cdot\theta)^2\right|
 \le C_k t^{3/4}.                                \tag{4.10}
\]

Now use the actual empirical mode F. In these local coordinates it is

\[
 F=\frac2N e_k(z)\cos(\pi k\cdot y)+\frac1N\sum_{j\ge3}e_k(x_j)
 =H_k(q)-\frac{\pi^2}N e_k(z)(k\cdot y)^2+O_k(|y|^4/N).
 \tag{4.11}
\]

The generator of H_k involves only the bounded slow drifts and their
original Brownian terms, so E H_k(q_(t wedge tau))=H_k(q)+O(t).
Also E|z_(t wedge tau)-z|^2<=C(t^2+nu t). Its multiplication into
the quadratic term costs O(t) by Cauchy--Schwarz and (4.3).
The Taylor remainder is O(t). Replacing the stopped final observable
by the unstopped one costs at most 2P(tau<=t)=O(t^2).
Since sqrt(4 alpha)=4/sqrt(N), we have proved the uniform statement

\[
 \boxed{\quad
 \limsup_{r\downarrow0}\sup_{q\in Q,\theta\in S^3}
 \left|P_t^NF(q,r\theta)-H_k(q)
       +\frac{4\pi^2}{N^{3/2}}e_k(z)(k\cdot\theta)^2\sqrt t\right|
 \le C_{N,\nu,k,Q}t^{3/4},\quad 0<t\le t_0.\quad}
 \tag{4.12}
\]

No existence of an exact collision entrance law or directional limit
is asserted. The uniform limsup estimate suffices. The near-collision
initial points are used to analyze the conditional expectation; the
Haar conclusion below integrates over a positive-volume set of actual
iid initial configurations.

## 5. Nonzero spherical projection and the failed gradient mechanism

Take k=(1,0,0,0) and the real empirical cosine f=Re F. Choose Q with
cos(2 pi z1)>=1/2. Let normalized surface measure be d sigma on S3 and

\[
 Y_2(\theta)=\theta_1^2-1/4,\quad
 \int Y_2=0,\quad\int\theta_1^2Y_2=1/16,\quad
 \Delta_{S^3}Y_2=-8Y_2.
 \tag{5.1}
\]

The moments follow either by rotational symmetry and sum theta_i^2=1,
or by the elementary one-coordinate spherical integral; all are
checked independently in the diagnostic. The eigenvalue follows by
restricting the harmonic polynomial y1^2-|y|^2/4 to the sphere.
For u=P_t^N f, (4.12) implies, after reducing t0 and then choosing
r_*(t)>0,

\[
 \left|\int_{S^3}u(q,r\theta)Y_2(\theta)d\sigma\right|
 \ge a_N\sqrt t,\qquad
 a_N=\pi^2/(16N^{3/2}),\quad q\in Q,\quad0<r<r_*(t),
 \tag{5.2}
\]

for every fixed 0<t<=t0. Indeed the leading projection has magnitude
at least pi^2 sqrt(t)/(8N^(3/2)), while the error is O(t^(3/4));
uniformity of the limsup gives the stated radius. All constants and
t0 may depend on the fixed N,nu,Q. In particular, this conclusion
holds for every N of every admitted critical sequence with its positive
nu_N; it makes no claim that t0 has an N-independent lower bound.

For a smooth function v on S3, integration by parts and Holder give

\[
 \left|\int vY_2d\sigma\right|
 \le C_Y\left(\int|\nabla_S v|^4d\sigma\right)^{1/4},
 \quad C_Y=\tfrac18\|\nabla_S Y_2\|_{L^{4/3}}<\infty.
 \tag{5.3}
\]

The same holds for weak W1,4 spherical slices, by local convolution
and partition of unity on the compact sphere. In pair coordinates
the Jacobian dx1 dx2=dz dy is one and
|grad_X u|^4 >=4|grad_y u|^4 >=4r^-4|grad_S u|^4.
Since dy=|S3|r^3 dr d sigma, (5.2)--(5.3) imply a positive constant
times

\[
 t^2\int_0^{r_*(t)}\frac{dr}{r}=+\infty.
 \tag{5.4}
\]

If u belonged to Haar W1,4, polar-coordinate slicing on every positive
annulus would justify (5.3) almost everywhere and yield this
contradiction. Thus **P_t^N f is not in Haar W1,4** for all those small
positive t. The conclusion includes the full N-particle gradient and
the original iid Haar integration. No smoothness of the singular
semigroup was presumed in making the contradiction.

The cutoff conclusion is equally explicit. Let u_epsilon=P_t^(N,epsilon)f.
These are smooth, bounded by one, and converge at every collision-free
initial point to u by the fixed-N path passage in Section 1. For each
annulus delta<r<r_*(t), bounded convergence gives convergence of their
spherical projections and of the fourth powers of those projections
integrated against dq dr/r. Apply (5.3) before taking the limit. It gives

\[
 \liminf_{\epsilon\downarrow0}
 \int_{(\mathbb T^4)^N}|\nabla P_t^{N,\epsilon}f|^4dx
 \ge C_{N,\nu,Q,t}\log[r_*(t)/\delta].
 \tag{5.5}
\]

Let delta decrease to zero. The liminf is infinite. This proves the
failure of (3.6), and of any cutoff-uniform Haar fourth-gradient bound,
even if its proposed finite constant is allowed to depend on N,nu,t.
For complex F, the real component already gives the contradiction.
Uniform global Lipschitz estimates fail as well. This is a bounded
smooth terminal test under actual positive-noise dynamics, not the
already known infinite square of an instantaneous singular source.

The radial power in (5.4) does **not** force failure of W1,2:
the analogous radial integral is integral r dr. No L2 response
bound, its failure, or an N-uniform time-integrated estimate is inferred.
The obstruction concerns this particular sensitivity mechanism; it
does not negate signed cancellation or the campaign mission.

## 6. Independent solvable-model and finite-probability diagnostics

The new standard-library diagnostic does not read a previous checker.
It tests the conditional decomposition on exact finite probability
spaces, including nonzero conditional bias and noise. It compares true
conditional orthogonality with false independence: the endpoint/noise
covariance is retained and nonzero. A wrong conditional-mean omission
and a wrong cross-term removal each cause nonzero exit.

An independent solvable local radial test has relative ODE
dY/dt=alpha Y/|Y|^4, alpha=4/N, whose exact solution is
Y(t)=(r^4+4 alpha t)^(1/4) theta. Its radial and tangential Jacobian
eigenvalues are respectively (r/R)^3 and R/r; their determinant is one
in dimension four. The volume-preserving local Coulomb model can
therefore have unbounded directional response. This model is only a
diagnostic of the local mechanism; the actual positive-noise periodic
result is proved in Sections 4--5, with the full remainder retained.

Exact rational spherical moments verify the harmonic projection,
finite-N pair and relative diffusion factors, radial Ito contractions,
the logarithmic fourth-gradient threshold, and the subcritical radial
integrability of the square. A documented convergent cosine series
tests the sign and coefficient of the angular trace for several N and
times. A deterministic radial sample checks the tangential gradient
amplification and its predicted 1/r asymptotics. No SDE is discretized,
no random sample or seed is used, and no numerical output proves the
continuum lemma. Results, every failed control, exact tolerances, and
execution commands are preserved in the packet. The passing baseline
completed 1,588 assertions in 33 categories. All six mathematical
mutation controls returned nonzero exit; the digest-corruption and
unsafe-member verifier controls also returned nonzero exit.

## 7. Adversarial self-check and the precise surviving line

| Challenge | Disposition |
|---|---|
| Does a deterministic close-pair example substitute for the actual law? | No. The proof treats the conditional actual positive-noise process for each collision-free start, then integrates over a positive-volume subset of iid Haar initial states. |
| Are the other N-2 labels discarded? | No. Their relative force difference is O(r), their slow drifts are bounded on the stopped domain, and exits are explicitly controlled. |
| Is finite-time angular memory assumed? | No. The exact radius and direction Ito equations give (4.6), (4.9), and the uniform limsup expansion. |
| Is a collision entrance limit asserted without proof? | No. The proof uses only a uniform limsup estimate and nonzero spherical projections. |
| Does Brownian smoothing force a continuous extension at collision? | It does not here; its angular variance over the rapid radial ejection is O(nu sqrt(t)), as proved from (4.7). |
| Are fixed-N constants represented as uniform in the critical sequence? | No. The local time window and error constants may depend on N,nu. The obstruction disproves a bound required at all times in any fixed horizon, but proves no fixed-time critical limsup. |
| Is a singular backward gradient inserted in a bracket without a domain proof? | No. Brackets and Dirichlet costs are written at the heat cutoff; the finite-N noise-cost limit is obtained from bounded endpoint moments. |
| Is source-square divergence or energy/UI reduction repeated as new progress? | No. The new object is the actual semigroup applied to a bounded smooth symmetric low mode, and its angular trace/fourth-gradient obstruction. |
| Does a fourth-gradient obstruction rule out a square-gradient approach? | No. The radial square integral is finite; actual L2 response control remains open. |
| Are current candidate inputs promoted by this construction? | No. Only used finite-N identities and kernel/domain mechanisms are reconstructed. No independent certification is claimed. |

The attempted global-sensitivity line (3.6) is now **DISPROVED by an
actual dynamic obstruction**. The original signed-correlation target
and its admitted negation remain unproved. The precise remaining
conditional-response obligation is

\[
 N\|P_T^NF-e^{-aT}F\|_2^2\longrightarrow0,
 \qquad
 \lim_{\epsilon\downarrow0}2\nu_N N\int_0^T
 E\sum_i|\nabla_iP_{T-s}^{N,\epsilon}F(X_s^\epsilon)|^2ds
 \longrightarrow0.                              \tag{7.1}
\]

The inner cutoff limit is at each fixed N, with its existence already
proved in (3.5). The two nonnegative quantities sum exactly to the
defect in (2.6). A successor can pursue their actual L2 control; a
global C1 or Haar W1,4 bound cannot be supplied as that control.
No external primary source or private input is indispensable to the
proved partial result. All analytical arguments here are same-context
self-checks and require fresh review before promotion.

## 8. Issuance and recoverable handoff

The only writes are this memorandum, the uniquely timestamped
ROUND_026_SIGNED_CORRELATION_ARTIFACTS directory, and its named sibling
archive/seals. The packet contains all 17 complete permitted source
copies, the original manifest, exact exposure record, full report,
whole claim card, fresh diagnostic and nonzero failure controls,
run history, exact inventories and digests, README, and a portable
read-only verifier. The verifier checks source digests, exact member
sets, all payload bytes, safe relative regular archive members, and
archive/directory equality. Final issued files are read-only.

No child, external browse, installation, nonallowlisted source read,
current audit/state/history/memory read, other-worktree read, canonical
edit, commit, push, or remote change occurred. Root alone assigns
identifiers and any independent reconstruction or hostile gate.
