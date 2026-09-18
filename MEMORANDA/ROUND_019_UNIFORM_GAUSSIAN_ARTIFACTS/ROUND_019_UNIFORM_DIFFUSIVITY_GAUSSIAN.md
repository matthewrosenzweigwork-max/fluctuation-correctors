# Round019 — uniform approximation over every finite diffusivity

2026-09-18 UTC. ROOT CONSTRUCTION / SELF_CHECKED, prepared for immutable issuance; independent gates pending. The exact two-part assertion and negation are frozen separately as THM041; earlier cards remain unchanged. Root is exposed to the earlier campaign, full R16/R17 proofs and R18 worker mechanism summaries. No independent certification is assigned. This construction must receive a complete source/diagnostic packet and both fresh independent gates before promotion.

## 1. Scope and the new uniformity obligation

Use exactly the model and normalizations in THM041. For Part A fix integer d>=3, 0<s<=d-2, a coefficient-one periodic Riesz kernel, finite T and one fixed smooth real terminal h. For Part B additionally s<d/2 and fix a finite time/test tuple of size m. Constants may depend on these fixed data but never on N>=2 or any finite diffusivity nu>=0. Write theta=1-s/d>0, a_k=4pi^2|k|^2, D_k=4pi^2 c_(d,s)|k|^(s+2-d), L_k(nu)=D_k+nu a_k. Q_t^nu preserves constants and multiplies each nonzero mode by exp(-tL_k(nu)). Set b=min(1/nu,1) at positive nu and b(0)=1. Thus 0<b<=1 and 0<=nu b<=1.

The earlier THM038 card states a bounded diffusivity interval. It alone cannot prove Part A. This proof checks the constants in its complete construction and in the actual Fourier argument directly. The complete local sources are R4 singular response for the kernel and compensated divergence, R6 actual particles for each fixed finite N and nu, R10 actual-law falsification Sections2–3 for energy and Fourier bounds, and R16 source extension Sections3–7 for the deterministic positive-kernel/commutator estimate. They have their issued conditional histories; the matching exact R4/R6/R10/R16 scopes have separate accepted gates. No R18 proof or gate, pair corrector, cubic residual, entropy propagation rate or private source is needed.

The full distribution D=div K is finite, has mass zero and Fourier coefficient D_k. At Coulomb it equals c_d(delta_0-dx), including compensation, not merely its punctured value. K is Haar L1. Every Haar contraction below is an ordinary integral against an integrable kernel, and every empirical interaction remains off diagonal. Actual finite-N noncollision and fixed-N same-noise heat approximation are applied for each finite nu separately. Their local constants may depend on nu; no large-N estimate uses those constants.

## 2. The actual energy and Fourier estimates are uniform over all noise

For H_N=N^-1 sum_(i<j)g(X_i-X_j), let g_* be the finite negative lower bound of g. At any fixed positive finite nu and heat parameter epsilon, the smooth law has

    d/dt [nu Ent(F_t^epsilon)+E H_N^epsilon(X_t^epsilon)]
       =-integral F_t^epsilon |grad H_N^epsilon+nu grad log F_t^epsilon|^2 <=0.

Initial entropy and expected energy are both zero. Entropy is nonnegative, so the smooth expected energy is at most zero. This conclusion has no coefficient depending on nu. Smooth existence/differentiation at this step can depend on the fixed nu. Coupled heat paths converge almost surely at this fixed N,nu and time horizon, and g_epsilon converges locally away from zero. The common bound H_N^epsilon>=(N-1)g_*/2 permits shifted Fatou, giving E_nu H_N(t)<=0. At zero noise use deterministic energy decrease and the initial expected energy zero. Therefore the same inequality holds for every finite nu>=0, with the same right side.

Exchangeability and the local coefficient-one expansion then yield E_nu |g(X_1-X_2)|<=2|g_*| and E_nu[1+dist(X_1,X_2)^(-s)]<=C. These constants are independent of every finite nu, N and deterministic time. Common translations and pathwise uniqueness give exactly Haar one-body marginals, as in Section4 below. They do not give product higher marginals.

For completeness the required empirical Fourier estimate follows with the same uniformity. Put alpha=(d-s)/2>=1 and A=4^alpha pi^(d/2)/Gamma(s/2). For 0<r<=1 the positive sharp heat retention g^>r has nonzero coefficient

    a_r(k)=A integral_r^infinity u^(alpha-1) exp(-4pi^2|k|^2 u) du>0.

Heat positivity, exact smooth self subtraction and g^>r(0)<=C r^(-s/2) give

    H_N >= (N/2)sum_(k!=0)a_r(k)|eta_hat(k)|^2
             -g^>r(0)/2 -(N-1)A r^alpha/(2alpha).

Take actual expectation, use E_nu H_N<=0, and set r=N^(-2/d). Then E_nu sum a_r(k)|eta_hat(k)|^2<=C N^(-theta). For 0<|k|<=N^(1/d), the interval [|k|^-2,2|k|^-2] is retained and shows a_r(k)>=c |k|^(s-d), with c depending only on the kernel. For higher modes use |eta_hat(k)|<=1. Hence for all k!=0,

    E_nu |rho_hat(t,k)|^2 <= min(1,C N^(-theta)|k|^(d-s)).          (2.1)

Every constant is independent of all finite nu and deterministic time. This bound is applied to smooth observables, not singular squared forces. No bounded interval or entropy constant enters its proof.

In particular, for a deterministic smooth function phi with Haar mean subtracted,

    E_nu |rho_N(t)[phi]| <= C N^(-theta/2)
         sum_(k!=0)|k|^((d-s)/2)|phi_hat(k)|.                    (2.2)

Absolute Fourier summation, Cauchy–Schwarz on each random mode, and (2.1) justify (2.2). Its deterministic summability condition will be verified for every test family used below.

## 3. Part A: the source constant does not require a noise cutoff

The entire positive-retention argument from R16 is an inequality for an instantaneous smooth vector field v, an actual configuration law with E H_N<=0, and the fixed kernel. Its ingredients and constants are recorded here to isolate the uniformity.

Take M=d+2, w_r(u)=(1-exp(-u/r))^M, psi_r=1-w_r>=0. The heat decomposition g=g_r+Q_r-c_r has Q_r>=0, c_r=integral Q_r=C_(alpha,M) r^alpha, and positive retained coefficients a_r(k) with polynomial tails. Set

    E_r=(1/2)sum_(k!=0)a_r(k)|eta_hat(k)|^2,
    S_r=(1/(2N^2))sum_(i!=j)Q_r(X_i-X_j).

Both are nonnegative. The exact identity is

    H_N/N=E_r+S_r-g_r(0)/(2N)-(N-1)c_r/(2N),
    E_nu(E_r+S_r)<=C(N^-1 r^(-s/2)+r^alpha), 0<r<=2.            (3.1)

The last inequality uses only g_r(0)<=C r^(-s/2) and Section2's actual expected-energy sign. It is therefore uniform over all finite nu. The retained source has only its smooth zero diagonal and all its original Haar contractions. With L=2(alpha+M), the logarithmic-symbol estimate 0<=-xi a_r'(xi)/a_r(xi)<=L yields the deterministic commutator bound

    |P_N[J_(g_r,v)]|<=2 C_v E_r,
    C_v=pi(1+L)sum_q |q|(1+|q|)^(L/2+1)|v_hat(q)|.              (3.2)

The proof is the lattice inequality for nonzero k,l,
 |k a_r(k)-l a_r(l)|/sqrt(a_r(k)a_r(l))
 <=(1+L)|k-l|(1+|k-l|)^(L/2+1),
followed by Cauchy–Schwarz on translated weighted Fourier sequences. The zero signed-measure mode vanishes. No dynamics, time derivative or noise occurs in this deterministic inequality.

For the omitted source, the differentiated Gaussian estimate dist(z)|grad p_u(z)|<=C p_(2u)(z), the gradient difference bound and psi_r(u/2)=psi_(2r)(u) give

    |J_(g-g_r,v)(x,y)|<=C 2^(-alpha)||Dv||_infinity Q_(2r)(x-y).

The empirical term is bounded by a constant times S_(2r), the mixed contraction by c_(2r), and the scalar term by c_(2r)/2. Thus all original contractions and the omitted positive kernel are controlled using (3.1). The resulting inequality is

    E_nu |P_N[J_(g,v)]| <= C [C_v+||Dv||_infinity]
                          [N^-1 r^(-s/2)+r^alpha], 0<r<=1.     (3.3)

The genuine source and its contractions are integrable because |J_(g,v)|<=C||v||_(C1)(1+dist^-s) and Section2 supplies the actual pair moment. The heat integral defining the omitted gradient is Haar L1 since alpha>=1. Thus (3.3) bounds the original singular observable, not a limiting surrogate or assigned diagonal.

Now take v=grad f_r^nu for the backward test in THM041. Every spatial Fourier coefficient of f is bounded in magnitude by that of the fixed h, for every finite nu>=0 and r in[0,T]. Both C_v and ||Dv||_infinity in (3.3) are bounded by a fixed finite weighted absolute Fourier seminorm of h, for example an integer power greater than alpha+M+3. No uniform bound on partial_r f as nu diverges is used. Choosing the deterministic observable scale N^-2/d in (3.3) proves Part A with a common constant. Particle regularization has already been removed for each fixed finite parameter tuple; this scale choice does not exchange singular and large-N limits.

## 4. Exact first-order vector decomposition

Fix the tuple in Part B. Let f_(j,r)^nu=Q_(t_j-r)^nu h_j on0<=r<=t_j. For each fixed N and finite nu these tests are smooth in space and time, even though their time derivative need not be bounded uniformly in nu. The full source row is -D*f, with scalar contraction zero; the backward equation is partial_r f+nu Delta f-D*f=0.

The actual noncolliding paths can be stopped on compact collision-free sets and ordinary time-dependent Ito applied to N^-1 sum_i f(X_i). Oddness and ordered relabeling give the interaction exactly half the deleted J sum, hence P_N[J]+eta_N[-D*f]. This cancels the backward linear response. Passing the stops uses the finite actual pair moment for symmetrized drift integrability, the bounded row, pathwise positive minimum separation on the fixed horizon, and bounded-gradient Ito isometry for the martingale. Alternatively the same identity follows from the complete heat backward passage in R17. In either derivation fixed finite nu is held until the genuine identity is obtained.

Consequently, for each coordinate,

    Z_(N,nu),j=A_(N,nu),j+M_(N,nu),j+R_(N,nu),j,
    A_j=sqrt(b/N) sum_i[f_(j,0)^nu(X_i(0))-integral h_j],
    M_j=sqrt(2nu b/N) sum_i integral_0^t_j grad f_(j,r)^nu(X_i(r)) dot dW_i(r),
    R_j=sqrt(Nb) integral_0^t_j P_N[J_(f_(j,r)^nu)](X(r))dr.     (4.1)

Every M_j is a square-integrable true martingale stopped at t_j and extended constantly to T. The thermal martingale is zero when nu=0. Part A, Tonelli and b<=1 imply

    sup_nu E_nu |R_(N,nu)| <= C N^(-kappa),
    kappa=1/2-s/d>0,                                           (4.2)

for the Euclidean vector norm, by finite coordinate summation. Only initial iid is used to form A. Higher marginals are correlated.

For each fixed translation a of the torus, translating all initial particles by a and keeping the Brownian increments translates the actual unique path. The initial joint law is translation invariant, hence every one-body time law is translation invariant. Its nonzero Fourier coefficients vanish by choosing a phase-changing translation; uniqueness of finite measures from their trigonometric moments gives Haar. This proves exact centering for all finite nu. No common exceptional set over uncountably many starts or translations is required.

## 5. Actual brackets and finite-N initial dependence

For a fixed real coefficient vector u, let M=u dot M_(N,nu) and define the deterministic vector field

    G_r^nu(x)=sum_j u_j 1_(r<=t_j) grad Q_(t_j-r)^nu h_j(x).

Endpoint values of the indicators do not affect time integrals. Its finitely many time discontinuities are harmless. The exact quadratic variation and its Haar version are

    q_(N,nu)=2nu b integral_0^T eta_N(r)[|G_r^nu|^2]dr,
    v_nu=2nu b integral_0^T integral |G_r^nu|^2 dx dr.             (5.1)

Independence of the Brownian coordinates gives this coefficient; no independence between initial vector and martingale is presumed. Spatial Fourier seminorms of G, and of |G|^2, are uniformly bounded in nu and r. Explicitly, convolution and
 (1+|k+l|)^p<=(1+|k|)^p(1+|l|)^p
bound the weighted absolute Fourier sum of a product by the product of the two sums. Gradients require only one additional fixed Fourier power of each h_j. Thus (2.2) applies uniformly to |G|^2. Since nu b<=1,

    E_nu |q_(N,nu)-v_nu|<=C |u|^2 N^(-theta/2),
    0<=q_(N,nu),v_nu<=C |u|^2                                  (5.2)

with the first bound allowing a fixed tuple-dependent constant. The second is pathwise for q and deterministic for v. These estimates hold simultaneously as inequalities for every finite nu, not through a limiting product law.

Let A=u dot A_(N,nu), measurable with respect to the initial sigma-field. For the combined continuous real martingale M_r, the process exp(iM_r+<M>_r/2) has Ito differential i exp(iM_r+<M>_r/2)dM_r. Its modulus is bounded by exp(C|u|^2/2), and its stochastic integrand is square integrable by (5.2). It is a true complex martingale with conditional expectation1 given the initial sigma-field. Multiplying that identity by exp(iA) gives

    exp(-v_nu/2) E_nu exp(iA)
       =E_nu[exp(i(A+M)) exp((q_(N,nu)-v_nu)/2)].

The mean value bound for the real exponential and (5.2) therefore give

    |E_nu exp(i(A+M))-exp(-v_nu/2) E_nu exp(iA)|
       <=C_u N^(-theta/2).                                    (5.3)

The constants C_u are bounded when u ranges over any fixed compact set. This is the required treatment of finite-N dependence. It does not claim A and M are independent.

## 6. Initial triangular vectors and exact covariance

For each nu, the vectors V_i^nu=(sqrt(b)(Q_tj^nu h_j(X_i(0))-integral h_j))_j are iid and centered. Their norm is bounded by one fixed constant, uniformly in nu: absolute Fourier sums bound Q_t^nu in sup norm and b<=1. Their covariance B(nu) is the initial Gram matrix. Taylor's formula with absolute cubic remainder gives, uniformly in nu and in u on a fixed compact set,

    E exp(iu dot V_1^nu/sqrt(N))
       =1-u^T B(nu)u/(2N)+O_u(N^-3/2).

Taking the Nth power and using log(1+z)=z+O(|z|^2) for the eventually uniformly small z proves

    sup_nu |E exp(iu dot A_(N,nu))-exp(-u^T B(nu)u/2)|
       <=C_u N^-1/2.                                         (6.1)

No replacement by a fixed test or convergence assumption on nu is needed. Let V(nu) be the deterministic thermal covariance from (5.1), so u^T V(nu)u=v_nu. Equations(4.2),(5.3),(6.1) imply

    sup_nu |E exp(iu dot Z_(N,nu))-exp(-u^T C(nu)u/2)| ->0,      (6.2)

uniformly for u on compact sets, with C=B+V. The three errors are bounded by C_u times N^-kappa+N^(-theta/2)+N^-1/2. Every covariance is real positive semidefinite, being a sum of two Gram matrices.

To evaluate it, Fourier expansion of the initial Gram gives b exp(-(t_i+t_j)L_k) for each paired mode. The thermal Gram gives

    2nu b a_k integral_0^min(t_i,t_j) exp(-(t_i+t_j-2r)L_k)dr
      =b(nu a_k/L_k)[exp(-|t_i-t_j|L_k)-exp(-(t_i+t_j)L_k)].

L_k>0 for every nonzero mode, including nu0. Adding the initial term gives exactly THM041's covariance. Smoothness permits absolute Fourier summation and time integration; conjugate symmetry yields the stated real covariance. Constant modes are excluded only after their actual centering. The formula covers repeated or zero times and all linear dependencies. In particular

    C_jj(nu)<=b(nu)||h_j-integral h_j||_2^2,                    (6.3)

since the two nonnegative coefficients D_k/L_k and nu a_k/L_k sum to one and every exponential is at most one.

## 7. Uniform weak approximation in the required metric

A uniform characteristic-function conclusion is not yet the stated supremum over bounded Lipschitz tests. Here is a complete passage. Let G_nu be a centered Gaussian with covariance C(nu), constructed by a positive-semidefinite square root applied to a standard m-dimensional Gaussian. No inverse of C is used. These Gaussians have uniformly bounded second moments by (6.3).

The vectors W=A+M have uniformly bounded second moments by the initial covariance bound, martingale isometry and the pathwise bracket bound: E|W|^2<=2E|A|^2+2E|M|^2<=C. Equation(4.2) then gives, uniformly over N>=2 and finite nu,

    P(|Z|>R)<=C/R^2+C N^-kappa/R.                              (7.1)

Thus the actual vectors are uniformly tight; no second moment of the singular source is asserted. The same tail conclusion remains uniform after adding an independent sqrt(epsilon) standard Gaussian, for any fixed epsilon>0.

At fixed epsilon>0, both Z+sqrt(epsilon)xi and G_nu+sqrt(epsilon)xi have densities given by the elementary Gaussian Fourier integral and Fubini. Their difference in sup norm is bounded by the integral of the characteristic-function difference times exp(-epsilon|u|^2/2), divided by(2pi)^m. Split this integral into a fixed ball and its complement. On the ball use the compact-uniform version of(6.2); outside use the bound2 and the Gaussian tail. First send N to infinity, then the Fourier ball radius to infinity. This proves that the density difference tends to zero uniformly in both x and nu, without requiring measurability of a supremum over nu.

For every real F with sup norm<=1, integrate the density difference on a fixed spatial ball and bound the outside by the two tail probabilities. The bound is independent of F and nu: ball volume times the uniform density error plus uniform tails from(7.1) and the Gaussian second moment. Sending N to infinity and then the spatial radius to infinity proves convergence uniformly over such F for the smoothed vectors.

If F additionally has Lipschitz constant<=1, coupling with the added Gaussian changes either expectation by at most sqrt(epsilon) E|xi|, uniformly in nu,N,F. Thus the limsup of the desired double supremum is at most2sqrt(epsilon)E|xi| for every epsilon>0. Let epsilon decrease to zero. This is precisely the d_BL assertion in Part B. It includes degenerate C and requires neither path-space compactness nor finite-N initial/noise independence.

## 8. Sequence consequences and limitations

If nu_n tends to a finite nu_bar, b is continuous there (including zero and its corner at one), and the covariance series converges by domination by a fixed summable product of smooth Fourier coefficients. Hence C(nu_n)->C(nu_bar). Matrix square roots are continuous on bounded positive-semidefinite matrices: uniformly approximate sqrt(x) on a bounded nonnegative interval by polynomials and use the spectral theorem. Coupling the Gaussian vectors with the same standard Gaussian then proves convergence in expected norm. The uniform d_BL conclusion gives the stated actual Gaussian weak limit.

If nu_n tends to infinity, b(nu_n)->0 and(6.3) implies trace C(nu_n)->0. Therefore d_BL(G_nu,delta0)<=E|G_nu|<=sqrt(trace C(nu))->0. Uniform approximation gives d_BL(Law Z,delta0)->0. For each fixed epsilon>0, the bounded Lipschitz test min(1,|x|/epsilon), divided by max(1,1/epsilon), belongs to the defining class; it bounds the probability of |Z|>=epsilon. Hence Z tends to zero in probability without a growth-rate condition on nu_n. Infinity was never used as a coefficient in the particle equation.

Part A has no s<d/2 restriction. Part B needs that strict inequality for its source residual. No claimed decay survives at equality from this proof. The result is for a fixed finite tuple in the homogeneous iid-Haar law and this kernel range. It proves no distribution-valued or path-space tightness, growing family, logarithmic or inhomogeneous theorem, arbitrary preparation or higher-order hierarchy. The old energy-floor, full microscopic-subcritical and positive finite critical conditions remain distinct. The present proposed uniform result, if both independent gates pass, would apply across them in this restricted exponent/law class; it is not a proof of every campaign flagship.

No first unresolved line remains in this root proof attempt, but its new all-noise source uniformity and entire metric conclusion are unaudited. The supporting exact diagnostic and complete source/exposure/seal packet accompany this issuance. Fresh reconstruction and separate hostile review remain mandatory. Root construction is not an independent certificate.


## 9. Supporting falsification and reproducibility

The fresh standard-library exact diagnostic checks 22623 rational assertions in27 categories, with9 mutation families. Modal covariance is evaluated both by the closed formula and by an independent discrete Gram representation of the integrated noise. Principal minors, initial and thermal components, zero times/noise, hot-noise bounds, exact Brownian-label coefficients, strict source threshold and an initial-measurable Gaussian-variance mixture test are included. The mixture has E(SM)=0 but E(SM^2)=e, and rejects finite-N independence and replacing a random compensator by its mean. Wrong covariance time, normalization, deleted-label factor and compensator sign have explicit rejected witnesses.

The rational modal probes use times i*(-log r)/(D+nu*a), with rational r. These times vary with parameters for exact algebraic checking; no fixed-time or uniform-noise theorem is inferred from that grid. The analytic proof in Sections2–8 establishes those assertions. No random seed, tolerance, numerical simulation, dependency installation, external theorem or novelty claim is used. The packet records the exact command, new code/results and all input/output/archive hashes.
