# Round 027 — an exact killed attractive dual for the actual Coulomb flow

TASK116. Root Astra Ultra, 2026-09-18 UTC. This is an exposed construction and self-check only. THM052/PO039 is OPEN/UNAUDITED. THM046 and the actual critical signed-correlation cancellation remain open. The new result concerns an explicitly auxiliary killed process and an exact change of path law; it does not replace the original preparation or dynamics in the mission.

## 1. Objects and whole assertion

Use the complete frozen THM052 conjunction and exact negation. The state space is the collision-free open subset Omega of the compact4N-dimensional torus with unit Haar measure. With H=H_N=N^-1 sum_(i<j)g(x_i-x_j), the original drift is -grad H and the auxiliary drift is +grad H. Both noises have covariance2nu times the identity. On Omega,

    Delta H = c(N-1) =: kappa,   c=4pi².                         (1)

The coefficient follows from Delta g=c off zero, two particle coordinates per unordered pair, and N(N-1)/2 pairs divided by N. This punctured identity does not erase the distributional collision atom. The full kernel retains div K=c(delta0-dx). Every integration below deletes the measure-zero collision set and controls approach to it by killing on explicit domains.

P is the conservative actual semigroup. Q is the minimal attractive diffusion killed at its maximal lifetime zeta. The new full assertion is P_t^*=exp(kappa t)Q_t with respect to Haar, the resulting exact exponential survival/product-Haar conditional marginal, and equality of the entire reversed attractive path conditioned on survival with the original repulsive path. All identities are at fixed N,nu before any critical limit.

## 2. Construction and a common exhaustion

The local coefficient-one heat calculation gives g(z)=|z|^-2+smooth even remainder near zero. Thus H is smooth on Omega, bounded below by (N-1)inf(g)/2 and diverges at every partial collision. Both locally Lipschitz drifts define pathwise unique continuous strong solutions up to exit from compact subsets of Omega, by solving on bounded smooth extensions and identifying solutions up to their common exit. The auxiliary process is killed at the increasing limit of those exit times. This construction defines a measurable strong Markov family: on each extension Picard approximants are measurable functions of the start and Brownian increments; uniqueness patches them, and the increment/uniqueness argument gives the Markov property up to killing. No entrance process at collision is defined.

For integers L sufficiently large, use the nested open domains

    D_L = {x: min_(i<j) dist(x_i,x_j)>1/L}.

Their closures are compact in Omega; boundary corners do not matter below. H and its first two derivatives are bounded on each closure. Extend the two drifts smoothly and boundedly outside a slightly larger collision-free neighborhood of that closure. Kill the extension upon leaving D_L. On paths surviving to t the extension agrees with the original local equation, and neither its choice nor any value of H outside that neighborhood is used.

For the original repulsive process, the shifted H is a nonnegative collision barrier. Up to a height exit, Itô gives dH=-|grad H|²dt+nu kappa dt+sqrt(2nu)grad H.dW. Expected stopped shifted energy is bounded by initial shifted energy+nu kappa t. The probability of reaching height R before t is at most that bound divided by R. At every deterministic collision-free start, letting R increase proves no finite explosion/collision. Its continuous path therefore lies in some D_L throughout each fixed compact time interval. The original P is conservative. Initial iid Haar has finite expected H since g is integrable; the same stopped argument also applies after averaging. The auxiliary attractive process has no such asserted conservativity. Its maximal lifetime is exactly lim_L tau_L by local existence and compactness. Before that lifetime paths are continuous in Omega.

## 3. Exact killed-domain duality, without a missing boundary term

Fix L and t, and temporarily write D=D_L. Start Brownian motion on the torus with generator nu Delta. Girsanov for the bounded drift extensions applies because their exponential quadratic-energy moment is bounded by a deterministic exp(Ct). On the event tau_D>t, Itô for H along this Brownian path gives

    integral_0^t grad H(B_s).dB_s
       = H(B_t)-H(B_0)-nu kappa t.                            (2)

Here dB denotes the Brownian coordinate differential, with covariance2nu; the Girsanov density for adding drift b is exp[(1/(2nu)) integral b.dB -(1/(4nu)) integral|b|²ds]. Formula(2) is legitimate up to the exit and uses only bounded derivatives on the closure. Define V=|grad H|²/(4nu) on D and the killed Brownian Feynman–Kac operator

    K_t^D v(x) = E_x^Brownian[1_(tau_D>t)
                           exp(-integral_0^t V(B_s)ds) v(B_t)].

This operator is symmetric with respect to Haar on D. Indeed stationary torus Brownian motion has symmetric heat transition densities. For every finite time partition the joint Haar-start density is unchanged by reversal of the coordinates and time increments. Cylinder sets generate the Borel sigma-field of continuous paths, so reversal invariance holds for every bounded measurable path functional. The event that the entire path stays in D and the integral of V are reversal invariant. Taking the functional f(B0)v(Bt) times these two factors proves symmetry by Fubini. Endpoints are in D on that event. No smooth boundary theorem, zero boundary trace of the singular process, or formal integration by parts at collision is being presumed.

Applying the Girsanov density for b=-grad H and b=+grad H respectively yields the exact bounded-domain identities

    P_t^D h = exp(H/(2nu)+kappa t/2)
                   K_t^D(exp(-H/(2nu))h),
    Q_t^D f = exp(-H/(2nu)-kappa t/2)
                   K_t^D(exp(H/(2nu))f).                     (3)

All multiplying functions are bounded on this fixed domain. Symmetry of K now gives

    integral_D f P_t^D h dx
       = exp(kappa t) integral_D h Q_t^D f dx.                (4)

The signs of both exponential H weights and of kappa are essential. The same spatial force square enters both Feynman–Kac operators; it is bounded only because the domain is fixed. No estimate uniform in L or N is inferred from those weights.

## 4. Removal of the artificial killing and the exact survival law

For nonnegative bounded f,h, the killed expectations on increasing D_L increase pointwise. On the repulsive side the exit times tend to infinity by Section2, so P_t^(D_L)h tends to P_t h. On the attractive side they tend to zeta, and the surviving expectations tend to Q_t f by the definition of the minimal killed process. At an initial point outside D_L the killed expression is zero; eventually every point of Omega is inside. Monotone convergence in(4) proves

    integral f P_t h dx = exp(kappa t) integral h Q_t f dx.    (5)

This is a positive-kernel identity on bounded measurable functions, and signed/complex versions follow by decomposing real and imaginary parts. Both sides are finite since P and Q are(sub-)Markov and the measure is finite. No singular derivative or weak boundary condition is passed to a limit.

Set f=1 to identify the actual density at time t as exp(kappa t)Q_t1, bounded by exp(kappa t). Set h=1, using P_t1=1, to obtain

    integral Q_t f dx = exp(-kappa t) integral f dx.           (6)

Thus from iid Haar, P(zeta>t)=exp(-kappa t), and the surviving configuration measure is exactly exp(-kappa t)dx. The conditional current configuration is product Haar. The lifetime is almost surely finite with the exact exponential law because kappa>0 and(6) holds at every t>=0. None of these assertions is made for each deterministic start. In particular Q_t1 is generally not spatially constant; the original positive-time density need not be Haar. A survival-conditioned one-time marginal of a different killed process is not a closure assumption for the original process.

## 5. Identification of the entire conditional reversed path

Take0=t0<t1<...<tm=T and bounded nonnegative configuration tests h0,...,hm. The actual repulsive expectation of their product is

    integral h0 P_(t1-t0)[h1 P_(t2-t1)[...hm]] dx.

Use(5) successively, equivalently transpose each semigroup with respect to the bilinear Haar integral; multiplication by a test transposes to itself. This equals

    exp(kappa T) integral hm Q_(tm-t(m-1))
                     [h(m-1) Q_(t(m-1)-t(m-2))[...h0]] dx.    (7)

The killed Markov property makes the last expression exp(kappa T) times the attractive expectation of product_j h_j(Y_(T-t_j)) with indicator zeta>T. Equation(6) says exp(kappa T) is exactly the reciprocal survival probability. This proves every finite-dimensional identity for the conditional reversed path. Repeated or missing endpoint times follow by inserting the test1; signed/complex tests follow by linearity.

On survival beyond T the attractive path is continuous on[0,T]. Both compared measures are therefore probability measures on C([0,T],(T4)^N). This is a separable complete metric space in the uniform metric; evaluations at a countable dense set of times generate its Borel sigma-field. To see the latter, uniform distances between continuous paths are suprema of their distances at those times, so open balls about a countable dense family of paths are evaluation-measurable and generate the topology. Equality of cylinder measures at rational times, established in(7), therefore identifies the full path measures. This is a measure-identification argument, not an unproved tightness or subsequence claim. T0 is the direct initial-law identity.

## 6. Relation to the still-open modal defect

Take a bounded complex F and complex number A. The bounded continuous endpoint expression first satisfies the path-law identity, and bounded measurable F follows already from the endpoint kernel identity. Thus

    E_rep|F(X_T)-A F(X_0)|²
       = E_att[|F(Y_0)-A F(Y_T)|² | zeta>T].                  (8)

For the empirical nonzero Fourier F and the exact A of THM049, N times(8) is precisely its modal endpoint defect, with the initial/final response orientation retained. The original target is therefore the vanishing of this N-scaled rare-survival-conditioned attractive defect. This is an exact alternative representation; it is not a decay estimate. The conditioning probability is exp[-c(N-1)T], exponentially small for a fixed positive T. Estimates for unconditioned attractive paths cannot be substituted without this factor. Nor can one infer independence of Y0 and YT from the exactly Haar marginal at the surviving final time.

The first unresolved assertion in this route is that the right-hand side of(8), multiplied by N with that fixed mode/time/critical sequence, tends to zero. No endpoint gradient estimate, local-equilibrium assumption, triple-correlation decay, positive-limsup witness or Gaussian/hierarchy theorem has been proved. Existing THM048/049 provide a separately audited equivalence back to the original source; they are not needed to prove(1)-(8).

## 7. Exposure and adversarial boundaries

Root has read the campaign history and all current ordinary and independent reports. This is an exposed root derivation motivated by the failure of global response regularity and the residual three-label route; no independence is claimed. The mathematical source contract here uses the exact model, local Coulomb identity and actual repulsive realization only. Those mechanisms were reconstructed in Sections1–2. The two current R26 candidates are not premises. No external source, novelty assertion or private input is used.

Potential false shortcuts explicitly excluded are: applying formal adjoints across collision without killed domains; assuming the attractive flow is conservative; confusing product-Haar conditional survivor marginals with the actual repulsive law; reversing the response orientation in(8); dropping the exponential survival normalizer; imposing a collision entrance law; replacing the complete drift square by individual pair squares; or passing fixed-domain exponential H bounds uniformly to the singular/N limit. The proof avoids them with bounded Girsanov, reversible killed Brownian path functionals, monotone exhaustion and full cylinder identification. It remains a SELF_CHECKED candidate requiring both fresh whole axes before promotion.
