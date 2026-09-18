# AUD078 / TASK123 — whole hostile audit of THM053 and THM055

Issued 2026-09-18 UTC by the assigned fresh Astra Max hostile reviewer in
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r028-boundary-hostile`, branch
`codex/hocf-r028-boundary-hostile`, observed base
`72fe7e2fb4964d03643cb2e1e1bde46c3eb2c4d8`.

**THM053(A)–(B), entire unchanged conjunction: HOSTILE_REVIEW_PASS.**

**THM055(A)–(E), entire unchanged conjunction: HOSTILE_REVIEW_PASS.**

No mathematical repair, weakened quantifier, added assumption, deleted clause,
or counterexample to either frozen conjunction is needed. These are the
verdicts of this hostile axis, not a claim that this reviewer has seen the
separate blind axis or that root integration is complete. THM046/PO033 remains
OPEN. The new boundary criterion is an exact reduction, not critical decay.

The first read was the assigned task card and its manifest. All 21 allowed
input byte strings matched before mathematical work and in the packet copies.
The entire flux constructor has 397 lines. The entire quantitative constructor
has **706** lines in the hash-matching file; the dispatch's 705 is an
administrative count discrepancy. All 706 lines, including the final line,
were read. Full source/read/exposure and execution records accompany this
report. No current blind report, third route, constructor diagnostic source,
nonallowlisted linked file, canonical state/history, memory file, external
source, or other worktree was accessed. The supplied current proofs were
available to this hostile reviewer; this is not blind reconstruction.

## 1. Exact scope and clause verdicts

All assertions below use finite integer N at least two, finite positive
diffusivity, the coefficient-one four-dimensional periodic Coulomb kernel,
probability Haar, and iid Haar initial state independent of Brownian noise.
The attractive auxiliary law is killed at its maximal collision-free lifetime.
The original law is conservative and repulsive. The two signs are never
interchanged without the proved adjoint/path-law identity.

| Frozen clause | Verdict | Load-bearing audit below |
|---|---|---|
| THM053(A), exact full-drift first-power action and terminal limit | PASS | Sections 2–5 |
| THM053(B), unique pair, all marked Borel laws and independence | PASS | Section 6 |
| THM055(A), full unmarked law and empirical mode moments | PASS | Sections 5–7 |
| THM055(B), actual source, explicit tails and canonical clipping | PASS | Section 7 |
| THM055(C), stopped observable, brackets, uniform bounds and correlation | PASS | Section 8 |
| THM055(D), lifetime profile, exact response cost and original equivalence | PASS | Sections 9–10 |
| THM055(E), conditional expansion, five classes and lower bound | PASS | Section 11 |

For each conjunction its exact negation is an admitted finite datum violating
one of its identities, existence claims, bounds, Borel extensions, or uniform
quantifiers, or an admitted critical sequence violating its stated equivalence.
The arguments below exclude that negation in the frozen scope. They do not
exclude the negation of THM046: an original fixed-real-test positive-limsup
witness remains possible, and none is supplied here.

## 2. Kernel and probability-diagonal normalization

Write M for the full configuration torus and Omega for its collision-free
part. The heat representation from the allowed R4 proof specializes to

    g(z) = c integral_0^infinity (p_t(z)-1) dt,   c=4 pi^2.

At small t the Haar L1 norm of p_t-1 is at most two; at large t its Fourier
series decays exponentially. Its nonzero coefficient is exactly |k|^-2.
The central Gaussian integral is
c integral_0^infinity (4 pi t)^-2 exp[-|z|^2/(4t)]dt=|z|^-2.
Noncentral small-time terms and large-time differences are smooth with
integrable derivatives on any smaller zero chart. Consequently
g=|z|^-2+h, with h smooth, and grad g=-2z/|z|^4+grad h. This proves
smoothness off zero, a finite lower bound, divergence to positive infinity,
and Haar L1 of both g and grad g. Differentiation has no extra gradient
measure: its omitted spherical boundary term is O(r).

Fourier differentiation gives Delta g=c(dx-delta_0). The local flux agrees:
-2 times area(S3)=-4 pi^2. For each unordered pair change variables
xi=y+z, xj=y. The Haar Jacobian is one. After integration in y and the other
coordinates, Delta_xi+Delta_xj becomes 2 Delta_z; mixed y derivatives and
derivatives in the remaining coordinates integrate to zero. Thus for every
smooth full-configuration test f,

    integral g(xi-xj) Delta_M f dx = 2c(integral f dx - m_ij[f]),
    Delta_M H = kappa dx - (2c/N) sum_(i<j) m_ij,
    H=N^-1 sum_(i<j)g,   kappa=c(N-1).

Here m_ij is precisely the probability pushforward described by the card.
It is not unnormalized induced surface measure. Independently, normal
coordinates q=(xi-xj)/sqrt(2), p=(xi+xj)/sqrt(2) give principal energy
|q|^-2/(2N), transverse flux -2 pi^2/N per p-volume, and dp=4dy on the
diagonal. Their product is -8 pi^2/N=-2c/N. Both computations agree.

Writing B=grad_M H, the triangle inequality in the full 4N norm gives

    integral_M |B| dx <= sqrt(2) binom(N,2) ||grad g||_1/N < infinity.

Consequently the global distributional integration by parts is legitimate:
integral B.grad f=-kappa integral f+(2c/N)sum m_ij[f]. No classical
punctured divergence is extended across a collision without its measure.

## 3. Local construction, conservative comparison and killed duality

For each compact collision-excluded set a smooth bounded extension of either
drift has a unique additive-noise solution, obtained by Picard iteration
after subtracting the Brownian path. The iterations and exit times are jointly
measurable in start and driving path. Uniqueness patches them over
D_L={minimum pair distance>1/L}; for starts outside D_L its exit is zero.
The exits increase to the maximal lifetime. If their limit preceded that
lifetime, a longer compact time segment of the continuous collision-free
path would have a positive minimum separation, a contradiction. No boundary
regularity of D_L is required.

This construction also supplies the deterministic-time restart property for
the killed family: Brownian increments after a deterministic time are
independent of the past, and local uniqueness identifies the restarted path.
Measurability allows integration over random current states. No arbitrary
stopping-time strong Markov theorem is needed in the quantitative transfer.

For the repulsive sign use E=H-(N-1)inf(g)/2. It is a sum of nonnegative
pair terms and every energy sublevel is compact in Omega, including near
all possible partial collisions. On a height stop R, ordinary Ito gives

    dE = -|B|^2 dt + nu kappa dt + sqrt(2nu) B.dW.

The stopped integrand is bounded, so the martingale expectation is zero.
Starting below R, the probability of reaching R by T is at most
(E(x)+nu kappa T)/R. This proves noncollision/nonexplosion from every
collision-free deterministic start. A bounded drift on a compact set permits
continuation and rules out another explosion mechanism. Hence P_t1=1 for
the repulsive semigroup. No attractive force-square bound follows.

On a fixed D_L all Girsanov coefficients are bounded; their exponential
quadratic moment is bounded by a deterministic exp(C_L t). Brownian motion
with generator nu Delta, on survival within D_L, satisfies
integral B.dW_coord=H(end)-H(start)-nu kappa t. The Girsanov density for
adding drift a is exp[(2nu)^-1 integral a.dW_coord-(4nu)^-1 integral|a|^2].
The killed Brownian operator K_t with potential |B|^2/(4nu) is symmetric:
Haar Brownian finite-dimensional laws reverse by symmetry of heat kernels,
and the entire continuous-path survival event and potential integral are
reversal invariant. Cylinder uniqueness extends this argument to those
path functionals. Thus the two gauge formulas have exactly the signs

    P_t^D h = exp[H/(2nu)+kappa t/2] K_t(exp[-H/(2nu)]h),
    Q_t^D f = exp[-H/(2nu)-kappa t/2] K_t(exp[H/(2nu)]f).

It follows that integral fP_t^Dh=exp(kappa t) integral hQ_t^Df.
For nonnegative tests killed expectations increase under the common
exhaustion. On the repulsive side the limit is P_t; on the attractive side
the union of survival events is exactly {zeta>t}. Monotone convergence gives

    integral fP_th = exp(kappa t) integral hQ_tf,
    E_m[f(Y_t) 1_(t<zeta)] = exp(-kappa t) integral f dx.             (A)

The second identity uses h=1 and conservativity, rather than a formal
adjoint domain. Bounded signed and complex tests follow by linearity;
nonnegative unbounded tests follow by monotone truncation. In particular
0<zeta<infinity almost surely, its mean is 1/kappa, and its survivor
configuration is Haar. This is an iid-start assertion only.

## 4. Full path law and precise response orientation

Transpose each semigroup in a finite cylinder expectation under Haar,
keeping multiplication operators fixed. Products of factors exp(kappa dt)
give exactly exp(kappa T); the resulting killed product has reversed tests
and reversed time increments. Therefore the repulsive continuous path on
[0,T] has the law of (Y_(T-t)) conditional on zeta>T. Both are probability
measures on continuous path space. Evaluations at a countable dense time
set generate its Borel sigma-field: uniform distance is the supremum of
the distances at those times, and the space is separable. Finite cylinders
therefore identify the whole path measure, without a tightness argument.

At T=0 this is simply Haar. For bounded complex F, endpoint measurability
already yields

    E_rep |F(X_T)-A F(X_0)|^2
      = E_att[|F(Y_0)-A F(Y_T)|^2 | zeta>T].                     (B)

This verifies the entrance definition of D_N in THM055, including the
orientation of the response. In particular exp(kappa T) is the exact
normalizer; no uniform-in-N bound for it is used. Original positive-time
Haar, independence of the two endpoints, and point-start exponential
survival have not entered the argument.

## 5. Full first-power action, limit and stopped tests

Tonelli applied to (A), first to product tests and then nonnegative Borel
functions of time and state, gives

    E integral_0^zeta a(t,Y_t)dt
       = integral_0^infinity exp(-kappa t) integral a(t,x)dx dt.   (C)

Setting a=|B| proves the exact THM053(A) identity, not only an upper
bound. Its finiteness implies absolute convergence of the vector drift
integral almost surely. A measurable Euclidean lift satisfies
Ytilde_t=Ytilde_0+integral_0^t B(Y_s)ds+sqrt(2nu)W_t. Since zeta is finite
and Brownian motion is continuous at every finite time, the lift has a
limit at zeta. Its projection Z is the actual torus limit. Compactness
alone would only give subsequences and is not used for this conclusion.

If Z were collision-free, the tail of the convergent path would lie in a
compact collision-free neighborhood. A bounded smooth extension, with the
same Brownian path, would continue it through zeta, contradicting maximality.
Thus Z is a collision configuration. Evaluating Z thereafter as a constant
stopped path is just a bookkeeping convention; it does not continue the SDE.

For a global smooth f stop Ito at t wedge tau_L. The finite variation is
dominated on the entire lifetime by
nu||Delta f||_infinity zeta+||grad f||_infinity integral_0^zeta|B|,
which is integrable by (C). The bounded f converges in L1. The stochastic
integrands, taken zero after the lifetime, converge in L2 by isometry;
their expected bracket is bounded by 2nu||grad f||_infinity^2/kappa.
Hence the stopped martingale is true and uniformly integrable, and

    f(Ybar_t)-f(Y_0)=integral_0^(t wedge zeta) L^+f(Y_s)ds+M_t^f. (D)

One may also send t to infinity, using these same integrable envelopes and
the finite expected full bracket. No Ito formula for singular H at an
attractive collision, instantaneous force square, or unproved stopped-noise
mean has been inserted. All passages occur at fixed N and nu.

## 6. Joint exit law, all Borel marks and N=2

The Haar integral of L^+f is -kappa Haar[f]+(2c/N)sum m_ij[f]; its
diffusion integral is zero. Take expectations in (D), use (C), and subtract
the survivor expectation (A). This proves

    E[1_(zeta<=t) f(Z)]
       = (2c/N) integral_0^t exp(-kappa s)ds sum_(i<j)m_ij[f].    (E)

This computation includes every possible collision configuration; it has
not assumed a binary collision. Smooth trigonometric approximation extends
(E) to continuous tests. For each fixed t these determine finite Borel
measures on compact M: indicators of open sets can be increased to by
continuous distance cutoffs, and finite-measure uniqueness gives all Borel
sets. Subtracting two times identifies the measure on rectangles
(a,b] times A. Finite-measure uniqueness on their generating system gives

    Law(zeta,Z)(dt,dx) = (2c/N) exp(-kappa t) dt sum_(i<j)m_ij(dx).

Both sides have mass one; the right mass is (2c/N)binom(N,2)/kappa.
Linear decomposition gives every bounded Borel test, and monotone
convergence gives all nonnegative extended tests. This proves the full
joint law, rather than only its marginals or an infinitesimal flux.

Let S_ij consist of the ij diagonal with every other pair equality removed.
Under m_ij the common point and the other coordinates are independent
nonatomic Haar points. Every additional equality, shared or disjoint,
has zero mass; a finite union still has zero mass. Thus m_ij(S_ij)=1
and m_kl(S_ij)=0 for another pair. The exit measure proves Z lies almost
surely in the disjoint union of these strata. Define I by that stratum.
Restricting the joint law to S_ij gives exactly THM053(B), with coefficient
2c/N. It factors as exponential time times the uniform pair/configuration
mixture, so zeta is independent of (I,Z), and conditional on I the
terminal law is m_ij. I and Z themselves are not independent.

At N=2, kappa=c and 2c/N=c. There is one Haar common point, no other
pair to exclude, and no globally chosen torus center is needed. This
also proves the complete THM055(A) exit law with Gamma_N as stated.

## 7. Modal moments, original source and every clipping constant

For nonzero k let F=N^-1 sum e_k, ell=c|k|^2. Haar integration gives
Haar[F]=0 and Haar[|F|^2]=1/N. Under a fused pair F has coefficient
two on the common character and coefficient one on each of N-2 other
independent Haar characters. Hence Gamma_N[F]=0 and
Gamma_N[|F|^2]=(4+N-2)/N^2. These also hold at N=2.

For J=K(x-y).(grad e_k(x)-grad e_k(y)), integrability follows from
the Lipschitz gradient difference and |K|=O(r^-3). Integration against
div K=c(delta_0-dx) yields the literal Haar row -c e_k(x) and zero
double mean. Thus j=J+c(e_k(x)+e_k(y)) is symmetric with both rows zero.
The added rows contribute c(N-1)F/N to its ordered pair sum. Keeping
the two backgrounds in P_N[J] gives exactly P_N[J]=U+cF/N.

The constants in the frozen statement need no enlargement. On r<=r0,
the Hessian norm of e_k is ell and

    |j| <= (2r^-3+M_H)ell r+2c <= alpha/r^2+B0,
    alpha=2ell, B0=ell M_H r0+2c.

Away from this ball each gradient has norm 2pi|k|, giving
|j|<=4pi|k|M_K+2c=D0. For L>=L0, the tail is within the ball,
B0<=L/2, and |j|>L implies r^2<2alpha/L<=r0^2. Its probability is
at most (pi^2/2)(2alpha/L)^2=2pi^2 alpha^2/L^2. For 1<=L<L0 the
bound C_k/L^2 follows from C_k>=L0^2. All suprema defining M_H and
M_K are finite on their indicated compact domains; none depends on N,nu,T.

Modulus clipping satisfies |j-j_L|=(|j|-L)_+. Layer cake therefore
gives ||j-j_L||_1<=C_k/L and ||j_L||_2^2<=1+2C_k log L, including
L=1. The commuting orthogonal coordinate-average projections give
v_L=(1-E_x)(1-E_y)j_L, so ||v_L||_2<=||j_L||_2. Because j already
has zero rows, j-v_L=(1-E_x)(1-E_y)(j-j_L) in L1; conditional
expectation contracts L1, giving precisely the factor four.

Under iid Haar, disjoint unordered pairs factor, and a one-label overlap
vanishes by conditioning on the common coordinate and using the zero row.
Symmetry combines the two ordered orientations. Thus the variance equals
binom(N,2)||v_L||_2^2/N^4=(N-1)||v_L||_2^2/(2N^3).
The remaining L1 expectation is at most
[(N-1)/(2N)] times 4C_k/L. At L=N this is exactly the displayed
2C_k(N-1)/N^2. The square-root variance plus that remainder is the
frozen u_N,k, with order sqrt(1+log N)/N. This argument does not
require an instantaneous L2 norm of j or change the particle dynamics.

## 8. Observable, both brackets, stopping and future transfer

Direct generator differentiation reverses the repulsive force sum but
not the diffusion sign. Since the raw J sum is U-c(N-1)F/N,

    L^+F = [c(1-1/N)-nu ell]F-U = bF-U.

For k,l the gradient products are
grad e_k.grad conjugate(e_l)=c(k.l)e_(k-l), and
grad e_k.grad e_l=-c(k.l)e_(k+l). Independent particle Brownian
coordinates and the factor sqrt(2nu)/N therefore give exactly

    d<M_k,conjugate(M_l)> = (2nu c/N)(k.l)F_(k-l)1_(s<zeta)ds,
    d<M_k,M_l> = -(2nu c/N)(k.l)F_(k+l)1_(s<zeta)ds.

The self conjugate bracket is 2nu ell(s wedge zeta)/N. Section 5
justifies the full lifetime L2 limit and the genuine identity Delta=I+M,
where Delta=F(Z)-F(Y_0) and I is the stated drift integral. Its exact
martingale second moment is 2nu ell/(N kappa). The occupation identity
and the preceding iid bound give

    E|I| <= kappa^-1 (|b|/sqrt(N)+u_N,k).

Since |Delta|<=2, keeping both cross terms yields
E|Delta|^2<=2E|I|+sqrt(E|Delta|^2 E|M|^2).
Young's inequality gives E|Delta|^2<=4E|I|+E|M|^2. In particular
this is legitimate even before asserting L2 of I; its first term uses
bounded Delta and L1 of I, and Delta=I+M subsequently supplies L2 of I.
Multiplication by N gives the exact frozen epsilon, with no lost factor.

For 0<nu<=nu_* use kappa>=cN/2, |b|<=c+nu_*ell, and the explicit
u bound. This proves, uniformly on that interval,
epsilon=O(N^-1/2+sqrt(1+log N)/N). No lower diffusivity bound is used.

For the future assertion, let G be any nonnegative measurable functional
of the restarted killed path including its endpoint. Local construction
makes its kernel x -> E_xG measurable; any endpoint exceptional set can
be assigned an arbitrary value, since it has zero Haar-start probability.
At deterministic T, the restart identity and (A) give

    E[1_(zeta>T) G(future from T)]
      = exp(-kappa T) integral E_xG dx.

Division by the exact survival probability transfers the entire future
segment to its iid-start law. Apply this to N|F(Z)-F(Y_T)|^2. This
proves the stated bound for every finite T without conditioning a past
Brownian integral on survival. The future need not be independent of Y_0.
Finally Cauchy–Schwarz, with N E|F(Y_0)|^2=1, gives
|N E[F(Y_0)conjugate(F(Z))]-1|<=sqrt(epsilon). It is an unconditioned
typical-lifetime correlation statement, not a fixed-long-lifetime bound.

## 9. Lifetime profile, exact response change and uniform norm comparison

The bounded variable defining R(t) admits a conditional expectation with
respect to zeta on a standard Borel space, or equivalently a
Radon–Nikodym density against its positive exponential density. Thus R
is nonnegative measurable, bounded by 4N, and defined up to Lebesgue-null
sets. Integrating over zeta>T gives exactly

    B_N(k,T)=exp(kappa T) integral_T^infinity kappa exp(-kappa t)R(t)dt
            =integral_0^infinity kappa exp(-kappa u)R(T+u)du.

In particular no term involving the initial mark has lost its survival
weight. Only the future-only estimate in Section 8 cancels that weight.

By the proved independence of Z and zeta, the conditional residual life
U=zeta-T has density kappa exp(-kappa u), and N E|F(Z)|^2=1+2/N.
Consequently the response-change second moment is exactly

    A_T^2(1+2/N)[1-2kappa/(kappa+a)+kappa/(kappa+2a)]
      = A_T^2(1+2/N) 2a^2/[(kappa+a)(kappa+2a)].

No initial/terminal independence is used. Two norm triangle inequalities,
first inserting A_TF(Z), then changing A_T to exp(-a zeta), prove
the complete square-root comparison in THM055(D), with precisely its
epsilon and response factor. Here (B) identifies its first norm with
the actual original defect.

For fixed k and nu<=nu_*, a<=c+nu_*ell and A_T<=1 for every T>=0.
The response square root is at most 2a/kappa<=4a/(cN). The other
term is O(N^-1/4); sqrt(1+log N)/N is O(N^-1/2). Thus the stated
O(N^-1/4) bound is genuinely uniform over all finite horizons and all
bounded positive diffusivities. At T=0 the original defect is exactly
zero and the same comparison bounds B_N(k,0), without division by T.

On a critical sequence nu_N tends to zero and is eventually bounded.
The square-root difference tends to zero. Nonnegative sequences then
vanish together; failure of vanishing is exactly a positive limsup, and
that alternative also agrees. No boundedness of exp(kappa T) or of the
initial conditional variance is assumed for this implication.

## 10. Imported source-to-mode interface checked in its actual scope

The allowed R25 report was read in full and its needed proof was checked;
the accepted gate is not used instead of that proof. The R1 one-body
coefficients and brackets, R4 kernel/divergence argument, and R6 local
construction/energy mechanism were checked in their stated smooth or
fixed-N scopes. Unrelated older pair-propagator or hierarchy claims are
not premises. The supplied R27 proof was reconstructed in Sections 3–4.

For clarity, the R25 interface does more than assert that an L2 source
bound would suffice. Its heat split uses w_r(u)=(1-exp(-u/r))^6 and
g=g_r+Q_r-c_r, with Q_r>=0, c_r=O(r), g_r positive in nonzero
Fourier coefficients and g_r(0)=O(r^-1). Exact diagonal subtraction
gives H/N=F_r+V_r-g_r(0)/(2N)-(N-1)c_r/(2N), where F_r,V_r>=0.
At r=N^-1/2 this proves H>=-C sqrt(N).

The retained Fourier coefficient a_r(rho) has logarithmic slope at most
fourteen: integration by parts in u uses 0<=u w'_r<=6w_r and gives
-rho a'_r/a_r<=14. Comparing radial coefficients and directions between
nonzero lattice points yields the displayed safe bound
|k a_r(k)-l a_r(l)|/sqrt(a_r(k)a_r(l))
<=15|k-l|(1+|k-l|)^8. In the Fourier source sum, shifted-sequence
Cauchy–Schwarz bounds this by F_r times the degree-nine norm of the
vector field. For a scalar test this is degree ten. The discarded
part obeys dist(z,0)|grad p_u(z)|<=C p_(2u)(z), by the Gaussian
formula, and its three empirical/background pieces are bounded by
V_(2r),c_(2r),c_(2r)/2. Combining the split energies proves the
pointwise source majorant sqrt(N)|P_N[J_t]|<=C_h(G+H/sqrt(N)),
with the same degree-ten norm for every backward response.

The conservative energy martingale has bracket 2nu integral|B|^2,
and the floor and initial E H=0 give E integral|B|^2<=C sqrt(N)+nu c(N-1)T.
On an eventual critical window its maximal second moment is O(1).
The source majorant then bounds |S_N| by a fixed A plus
C(H_0^++sup|E_mart|)/sqrt(N), which by itself is only order one.

R25 removes the infinite initial energy variance by clipping g at
L_0N^2 and restoring its negative mean. The initial bad-pair probability
is O(N^-2), by the unordered union bound and the r^-2 tail. The
canonically centered clipped energy has variance
(N-1)||g_clipped||_2^2/(2N)=O(log N), by conditional zero rows.
On the good event the original positive energy is bounded by its clipped
absolute value. On the bad event the exact source identity is used
instead: S_N=bounded endpoint of size O(sqrt(N)) minus the one-body
martingale. The event is time-zero measurable, so its conditional
isometry follows by putting its indicator in the integrand. Its cost
is O(N) times O(N^-2), plus the small martingale cost. This gives
E(|S_N|-A)_+^2<=C(1+log N)/N, with the stated eventual-window uniformity.

At each finite N the endpoint is bounded and the one-body martingale
has finite variance, so all finite-prefix sources are L2. The inequality
x^2<=2Ax+2(x-A)_+^2 proves source L1/L2 vanishing equivalence; the
squared excess also proves squared uniform integrability, handling a
finite prefix separately. The endpoint/source martingale difference has
second moment O(nu), using only the one-body Haar marginal. Its L2
norm tends to zero, giving the endpoint equivalence and its UI. These
arguments never condition a past martingale on a future survival event.

For a complex mode the actual squared endpoint defect is the sum of the
cosine and sine squared defects. The degree-ten L1 mode majorant just
checked permits dominated summation for every fixed smooth real h.
Thus decay of all fixed modal defects is exactly the full fixed-smooth
source criterion; one fixed modal positive limsup yields a fixed cosine
or sine witness by the same UI argument. Since beta_N~lambda sqrt(N),
min(beta_N,1)=1 eventually; its finite exceptional prefix alters no limit.
Arbitrary convergence rate of the critical sequence is allowed. T=0
and constant tests are zero identically. This verifies precisely the
THM048/049 interface claimed in THM055(D), without extending it to a
moving mode, moving external time, different preparation or hierarchy.

## 11. Conditional initial marks, lower bounds and five label classes

Given survival, the terminal second moment is still (1+2/N)/N because
Z and zeta are independent. Expanding the intermediate defect therefore
gives exactly v_N+A_T^2(1+2/N)-2A_T Re q_N. Cauchy–Schwarz gives
Re q_N<=sqrt[v_N(1+2/N)], which proves the complete square lower
bound. Its norm difference from D_N is at most A_T sqrt(epsilon)
by Section 8. This can supply a sufficient falsification condition if
there is a persistent variance mismatch; no such mismatch is proved.

Permutation equivariance of the entire path law and of survival implies
that a permutation-invariant integrable path functional has the same
expectation after additionally conditioning on each specified collision
pair. Uniformity of that pair on survival also follows from Section 6.
Thus the symmetric quantities in the expansion can be evaluated with
I={1,2}. In q_N the expansion of N F_0 conjugate(F_Z) has coefficient
1/N on each of N^2 ordered choices of initial and terminal labels.
The stabilizer of the fused pair identifies exactly these five classes:

| Initial/terminal labels | Number |
|---|---|
| fused/common fused | 2 times 2 = 4 |
| outside/common fused | (N-2) times 2 |
| fused/outside | 2 times (N-2) |
| same outside | N-2 |
| distinct outside | (N-2)(N-3) |

Their sum is N^2. All outside classes vanish at N=2; the last vanishes
at N=3. No absent representative is assigned a value. Common translation
of the whole path preserves the conditioning event and multiplies each
nonzero one-body character by a phase, so its mean is zero. It does not
factor the two-time products. Lifetime disintegration and Section 6
give the same expansion almost everywhere with A=exp(-at), as stated.
The notation v_N(t),q_N(t) in that last expression denotes conditioning
on zeta=t, as explicitly redefined in the constructor, not survival
conditioning. There is no inference that these two conditional families
coincide. THM055(E) and all its lower-bound qualifications pass.

## 12. Complete constructor and ancillary coverage

The following range map accounts for all mathematical and ancillary
material in both complete constructors. Administrative execution claims
in their packets are reported as their claims only: the allowed exposure
files were read, but excluded constructor code/results were not opened.
Root owns that separate execution and source/gate matching check.

| Constructor range | Disposition |
|---|---|
| Flux lines 1–57, assertion, negation, source status | Scope consistent; metadata not mathematical certification. |
| Flux 58–127, heat/distribution/full norm | Recomputed in Section 2, including probability-Haar factor. |
| Flux 128–198, process/repulsive energy/killed duality | Recomputed in Sections 3–4; bounded-domain signs and exhaustion pass. |
| Flux 199–223, action and terminal limit | Recomputed in Section 5, including the full first-power norm. |
| Flux 224–262, stopped Ito | Section 5 supplies full lifetime L1/L2 passages. |
| Flux 263–313, unmarked joint exit law | Section 6, including full Borel measure identification. |
| Flux 314–343, binary mark, product law and N=2 | Section 6, with no presumed simultaneous-collision exclusion. |
| Flux 344–375, Fourier, normal flux, radial and Laplace diagnostics | Recomputed here and in fresh diagnostics; see below. |
| Flux 376–392, failed shortcuts and scope | Mathematical objections valid; no concealed proof premise. |
| Flux 393–397, issuance | Administrative execution claims reserved for root. |
| Quantitative lines 1–93, target, negations and five local claims | Same data and distinction of original versus auxiliary assertions. |
| Quantitative 94–188, sources and duality | Sections 2–4 reconstruct the required mechanisms. |
| Quantitative 189–262, action, endpoint, flux and moments | Sections 5–7; all moment numerators and N=2 pass. |
| Quantitative 263–336, canonical source and explicit tails | Every displayed constant and multiplicity checked in Section 7. |
| Quantitative 337–428, generator, brackets, epsilon, future and correlation | Section 8, with no lost drift/noise cross term. |
| Quantitative 429–519, profile, response, uniform comparison, equivalence | Sections 9–10; exact normalizer retained. |
| Quantitative 520–571, q/v, lower bound and five label classes | Section 11, including both conditional notations. |
| Quantitative 572–625, failed routes | Correct distinctions and scalar counterexample to inference, not to actual target. |
| Quantitative 626–679, local models and self-review | Ancillary calculations below pass; old checker counts are not new evidence. |
| Quantitative 680–706, handoff and remaining line | Original target still open; administrative counts qualified above. |

For the Fourier ancillary check, a configuration character integrates to
one against m_ij exactly when all other frequencies are zero and the two
pair frequencies sum to zero. At a nonzero opposite-pair character,
H has coefficient 1/(N|k|^2); its full Laplacian multiplier gives -2c/N.
All other nonzero patterns give zero, including three nonzero frequencies
summing to zero. The zero mode gives zero on both sides. The normal
coordinate check was independently recomputed in Section 2.

For the principal Euclidean relative process the drift is -4z/(N|z|^4)
and the generator is 2nu Delta. Applying it to r^p in four dimensions
gives 2nu p(p+2)r^(p-2)-(4p/N)r^(p-4); hence the displayed r^2 and
r^4 formulas pass. The r^4 bracket is 4nu|grad r^4|^2=64nu r^6.
At zero noise r^4=r_0^4-16t/N, and zeta=N r_0^4/16, including r_0^4/8
at N=2. The full two-particle drift length is r_0/sqrt(2); its squared
action is proportional to integral_0^r0 r^-3 dr and diverges. A uniform
four-ball makes r_0^4 uniform, producing a constant short-time local
flux, not a global periodic exponential law. The fixed Euclidean center
gives F=e_k(center)cos(pi k.z), whose change is O(r_0^2). These models
have the explicit nonperiodic/zero-noise qualifications made in the reports.

The Laplace ancillary identity follows from (D) applied to exp(-at)f,
with the same full-lifetime bounds. The Haar integral of (L^+-a)f
is -(kappa+a)Haar[f]+(2c/N)sum m_ij[f], giving exactly
(2c/N)/(kappa+a) sum m_ij[f]. The a=0 case is included.

For every nonzero k, the leading local j is
-2 e_k(y)(2pi k.omega)^2 r^-2 plus lower singular order. On a cone
with k.omega bounded away from zero its squared integral contains
integral r^-1 dr, so the asserted logarithmic instantaneous divergence
is valid. Individual force squares diverge more strongly. Neither
divergence invalidates an L1 occupation estimate or the bounded observable
martingale. Full-drift squares can also contain nonzero pair cross terms;
no sum-of-pair-squares identity was used. All eight flux shortcuts and
all seven quantitative shortcuts correctly identify invalid inferences.

## 13. Fresh falsification attempts and portable evidence

Fresh standard-library diagnostics passed **16,732 assertions in 39
categories**, including **27 distinct nonzero deliberate mathematical
mutations**. They use exact rational and Gaussian-rational arithmetic,
apart from explicitly labeled numerical evaluation of analytic logarithmic
layer-cake expressions. There is no random sampling or simulated singular
SDE. The complete source, full stdout/stderr, exact run metadata and
source snapshots are retained, including any failed run if one occurred.
The first diagnostic execution succeeded; its wrapper returned before
stdout was displayed, and the saved completion record was then read.

The independently enumerated tests include full configuration Fourier
coefficients; geometric normalization; complex clipped zero rows and
orthogonal pair covariances; literal deleted source and attractive drift;
initial and fused moments; all five label classes; conjugate and
unconjugated brackets; local radial coefficients; exact residual-response
integrals; a two-state killed chain with a Haar left eigenmeasure; entire
three-time reversed cylinders; and complete future-functional transfer.

The killed chain explicitly exposes a changed initial law after survival,
nonzero survival-conditioned past-martingale mean, failed conditional
isometry, a nontrivial endpoint reversal and the omitted normalizer.
A coupled time/mark table has correct marginals and wrong joint law.
A threshold profile has a vanishing typical lifetime average and unit
normalized fixed-tail average. These are counterexamples to shortcuts,
never substitutes for the original particle model. Their nonzero
mutation residuals are recorded exactly in DIAGNOSTIC_RESULT.json.

No load-bearing line in either frozen conjunction failed. The first
unproved extension is still the quantitative constructor's equation
(6.7): vanishing of its normalized lifetime-profile tail for every
admitted fixed mode, fixed horizon and critical sequence. A typical
lifetime estimate, fused terminal law, or finite-prefix equivalence
does not establish that assertion. Neither limiting alternative is
selected by this audit.

The accompanying uniquely named packet retains all 21 frozen input copies,
their exact manifest and preflight, this report, full read/exposure and
operation records, failed-route account, diagnostics, README and a portable
read-only verifier. Its complete regular-member inventory, named archive,
and external seal make this issuance recoverable without repository
history or chat. They are frozen read-only. No source/canonical edit,
child, install, commit, push, remote operation or TeX work occurred.
Root alone integrates this hostile result with the separately isolated
axis and checks constructor execution claims. Corrections, if ever needed,
must be a distinct issuance rather than an edit to this sealed evidence.
