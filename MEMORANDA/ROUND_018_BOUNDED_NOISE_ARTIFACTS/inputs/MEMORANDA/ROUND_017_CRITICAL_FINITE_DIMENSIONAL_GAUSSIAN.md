# Round 017 — a conditional finite-dimensional critical fluctuation theorem

2026-09-18 UTC. ROOT CONSTRUCTION / UNAUDITED, conditional on the explicitly open THM038 source estimate and the earlier complete kernel/particle/energy modules. This complete construction is being issued with exact input/output seals; no independent audit or campaign promotion is assigned. The exact target is THM039, unchanged by this derivation. The complete R16 source construction is now supplied as an expressly conditional premise. Its independent gate must pass before the present conditional implication is promoted.

## 1. Scope, dependencies and centering

Use every hypothesis and exclusion in THEOREMS/THM-039_CRITICAL_FINITE_DIMENSIONAL_HOMOGENEOUS_GAUSSIAN.md: integer d>=3,0<s<=d-2,s<d/2,actual iid-Haar-prepared homogeneous singular particles, coefficient-one periodic Riesz force, positive finite microscopic critical lambda, a fixed finite list of deterministic times and real smooth tests. Constants below depend only on this fixed list, d,s,T, the kernel and fixed bounds for the critical tail. The source bound is required uniformly over the bounded diffusivity interval containing that tail. No theorem for an inhomogeneous, logarithmic or path-space setting is inferred.

The complete local sources are R1 algebra Sections2–3 for comparison of first-order coefficients, R4 singular response Sections2–4 for K in L1 and its compensated divergence measure, R6 actual particle realization for noncollision/uniqueness and finite-N singular paths, and R10 actual-law energy Sections2–3 for the actual bounded pair w_s moment. Their exact issued hypotheses and earlier conditional statuses remain in force. No pair inverse, R8 pair domain, R11 spatial limit, R12/R13 bracket or R14/R15 cubic result is a premise. The new quantitative premise is the entire THM038 actual source bound, whose independent gate is currently OPEN. The complete version-locked MEMORANDA/ROUND_016_SOURCE_EXTENSION.md, SHA25662fc121556fa2cb08f0ec3e2c7d1813f40bce6a86a2f5ea07ed2d616c6ce9a26, supplies this proof in Sections3–9, including the fixed-N actual energy sign and positive heat splitting. Root read all544 lines and verified/reproduced its construction packet. No stronger initial-mode derivative observation from that source is needed. The present argument derives the conditional implication; it does not infer a proof from a card or worker progress message.

Let mu denote unit Haar and eta_N the empirical probability measure. Translating the initial configuration by any fixed torus vector and using the same Brownian increments translates the entire singular path, by the difference form of the force and pathwise uniqueness. Iid Haar preparation is invariant under this translation. Each one-body time law is invariant under every torus translation. Its nonzero Fourier coefficients therefore vanish (choose a translation with nontrivial phase for each nonzero frequency); trigonometric-polynomial density identifies it with Haar. Consequently E eta_N(t)[h]=mu[h] exactly for every deterministic time. This neither factors higher marginals nor claims positive-time independence. No deterministic centering correction is present.

## 2. The genuine first-order singular identity

Write D=div K as the full finite signed periodic measure, including its atom and compensating Haar part at Coulomb. Define on smooth functions

    R f(x) = - integral f(x+w) D(dw).

The measure has total mass zero and is even. In Fourier variables its multiplier is -D_s(k) on k!=0, with D_s(k)=4 pi^2 c_(d,s)|k|^(s+2-d), and zero on constants. For a fixed terminal pair (t,h), put

    f_r^nu = S_(t-r) exp(nu (t-r) Delta) h, 0<=r<=t.

The two Fourier multipliers commute and have modulus at most one. Hence every fixed spatial derivative and the needed time derivative have absolutely convergent Fourier series uniformly over bounded nu, r and t in this fixed family; the time multiplier grows at most quadratically. The backward equation is partial_r f+nu Delta f+R f=0, with f_t=h, and mu[f_r]=mu[h]. No regularity of a pair corrector is used.

Define J_r(x,y)=K(x-y) dot(grad f_r(x)-grad f_r(y)) only off the diagonal. Smoothness, the geodesic gradient difference and the local force expansion give |J_r(x,y)|<=C w_s(x-y), uniformly in the admitted data. K in L1 and smooth f justify the row integral. Distributional integration by parts gives exactly

    j_r(x) := integral J_r(x,y)dy = - integral K(x-y) dot grad f_r(y)dy
              = - integral f_r(x+w) D(dw) = R f_r(x),
    integral j_r(x)dx = 0.

This equality uses the full distribution D, rather than its off-origin density. At Coulomb, if D=c(delta_0-mu), it reads Rf=-c(f-mu[f]), with the local term retained. No singular empirical diagonal is introduced.

For each finite N, apply time-dependent Ito to N^-1 sum_i f_r(X_i) stopped before any collision. The observable itself is globally smooth; only the particle force needs the stop. Oddness of K and the ordered distinct labels give directly

    N^-2 sum_(i!=j) K(X_i-X_j) dot grad f_r(X_i)
        = (1/2) D2[J_r] = P_N[J_r] + eta_N[j_r],

where D2 is the ordered N^-2 sum and the last equality uses the zero scalar integral. Thus the backward equation cancels the one-body term exactly and yields

    d rho_N(r)[f_r] = P_N[J_r] dr + dM_r,
    M_r = sqrt(2nu)/N sum_i integral_0^r grad f_u(X_i(u)) dot dW_i(u).

There is no force self term: all original sums are over i!=j. There is no mixed-particle Brownian trace. The observable's ordinary Laplacian is already nu eta_N[Delta f]. The noise bracket is exactly

    <M>_t = (2nu/N) integral_0^t eta_N(u)[|grad f_u|^2]du.

The actual bounded pair w_s moment follows from R10's nonpositive expected energy and the coefficient-one local comparison; it bounds every expected absolute force-symmetrized/source drift integral at fixed N. The row Rf is bounded. Noncollision on the compact time interval makes the collision-stop times eventually exceed t almost surely. Dominated convergence in probability-times-time (using the preceding absolute integrability) passes each drift in L1. The bounded gradient and the bracket bound pass stochastic integrals in L2. Endpoints are bounded. The unstopped identity is therefore genuine, with a square-integrable true M:

    rho_N(t)[h] = rho_N(0)[f_0^nu] + integral_0^t P_N[J_r]dr + M_t.       (A)

Its zero-noise version has M=0. This proof handles Coulomb without a pair-domain theorem or a singular diagonal assignment. It is an independent finite-label/domain derivation in the root constructor context, not an isolated audit.

## 3. Quantitative approximation by initial iid statistics

At positive finite microscopic criticality, theta=1-s/d>0,

    nu_N=lambda_N^-1 N^-theta ->0, beta_N->infinity,
    b_N=1 and sigma_N=sqrt(N) eventually.

For the fixed terminal tuple, THM038's explicit quantitative premise and Tonelli give

    sqrt(N) E |integral_0^t P_N[J_r]dr|
       <= C N^(s/d-1/2).

The constant is uniform along the critical tail, not obtained from a positive-time product law. The exact martingale bracket in (A) and bounded gradients give

    N E<M>_t <= 2nu_N t sup_r ||grad f_r||_infty^2,
    sqrt(N) E|M_t| <= C sqrt(nu_N).                              (B)

No estimate of a pair-corrector bracket enters this thermal first-order bound.

It remains to replace the triangular backward test f_0^nu by the fixed S_t h in the initial statistic without losing a factor sqrt(N). The heat identity

    exp(nu t Delta)h-h = integral_0^(nu t) exp(a Delta) Delta h da

and heat L2 contraction imply ||exp(nu t Delta)h-h||_2<=nu t ||Delta h||_2. S_t is L2 contractive by its real nonnegative Fourier damping. Thus v_N=f_0^nu-S_t h has Haar mean zero and ||v_N||_2<=nu t ||Delta h||_2. Initial independence gives exactly

    E |N^-1/2 sum_i v_N(X_i(0))|^2 = ||v_N||_2^2.

The expected absolute replacement error is at most C nu_N. This is the only step using initial product independence besides the Gaussian limit below; it is never applied at positive time.

For each fixed j let V_j(x)=S_(t_j)h_j(x)-mu[h_j]. Combining (A), (B), and the last estimate gives, on the eventual critical tail,

    E | Z_N,j - N^-1/2 sum_i V_j(X_i(0)) |
       <= C [N^(s/d-1/2)+sqrt(nu_N)+nu_N].                       (C)

Every term tends to zero because s<d/2. Finite summation makes the whole vector error tend to zero in expected Euclidean norm. At zero time the source/noise/replacement errors vanish exactly. Constant tests also give zero, and repeated times require no change. The bound does not claim decay at s=d/2.

## 4. Joint Gaussian convergence, including degeneracy

Set V=(V_1,...,V_m), a fixed bounded real vector function with Haar mean zero, and let C=integral V V^T dmu. It is symmetric positive semidefinite. A possibly degenerate centered Gaussian G with this covariance exists as C^(1/2) times an m-dimensional standard Gaussian. This defines the asserted limit without assuming C invertible.

Let Y_N=N^-1/2 sum_i V(X_i(0)). For every fixed u in R^m, Taylor's formula for exp(iu.V/sqrt(N)), with remainder bounded by |u.V|^3/(6N^(3/2)), gives

    E exp(iu.V(X_1(0))/sqrt(N))
       =1 - u^T C u/(2N) + O_u(N^-3/2).

Independence therefore gives

    E exp(iu.Y_N) -> exp(-u^T C u/2).                            (D)

Here is an explicit weak-convergence passage, to avoid hiding degeneracy or a compactness identification. For epsilon>0, add an independent sqrt(epsilon) standard Gaussian Z. Its characteristic multiplier exp(-epsilon |u|^2/2) is integrable. The density of Y_N+sqrt(epsilon)Z is the mixture of translated Gaussian densities. The elementary Gaussian Fourier integral and Fubini express it as the inverse Fourier transform of the characteristic function of Y_N times that multiplier. By (D), boundedness of characteristic functions and dominated convergence in u, these densities converge uniformly in x to the density of G+sqrt(epsilon)Z.

Also E|Y_N|^2=trace C for every N, so the convolved vectors have second moments trace C+m epsilon. Markov's inequality gives uniform tails. Splitting an integral into a compact ball and its complement proves convergence of expectations of every bounded Lipschitz function for the convolved vectors: on the ball use uniform density convergence; on the complement use boundedness and the uniform tails. For any bounded 1-Lipschitz test psi, coupling with the added Gaussian changes either expectation by at most sqrt(epsilon) E|Z|. Taking N to infinity at fixed epsilon and then epsilon to zero proves convergence of these expectations for Y_N to those for G. This proves the finite-dimensional weak convergence, including singular C, without relying on a density for G itself. Bounded Lipschitz tests characterize weak convergence in finite-dimensional Euclidean space; equivalently approximate continuous tests uniformly on a compact ball and use the same tight tails.

Finally (C) bounds the difference of any bounded 1-Lipschitz test evaluated at Z_N and Y_N by E|Z_N-Y_N|, which tends to zero. The same weak limit therefore holds for the actual fluctuation vector.

## 5. Covariance, centering and exact scope

The covariance is precisely

    C_ij = integral [S_(t_i)h_i-mu h_i][S_(t_j)h_j-mu h_j] dmu
         = sum_(k!=0) hhat_i(k) conjugate(hhat_j(k))
             exp(-(t_i+t_j)D_s(k)).

Absolute convergence follows from smooth tests; real-valuedness follows either from the real-space formula or conjugate pairing. Common initial particles produce cross-time covariance, with sum t_i+t_j, not |t_i-t_j|. The thermal noise vanishes by (B); there is no independent positive-noise Gaussian component left at this scaling. No covariance correction depending on the positive limiting lambda is created by this finite-horizon restricted theorem.

This is the exact conditional THM039 implication. Its exact negation is excluded only after the open THM038 source premise is supplied in the full admitted range and its independent gates pass. A finite-dimensional Gaussian conclusion does not establish tightness in path space, in a distribution-valued topology, or for a growing test family. In particular it does not close the higher hierarchy or silently enlarge the s<d/2 range. The three temperature conditions remain distinct; neither the old energy-floor condition nor full microscopic subcriticality is used in this critical proof.

Root exposure: the root has constructed prospective R16 source estimates, read the R15 constructor and independent reconstruction and all accepted earlier modules, and written this synthesis. This is exposed construction and cannot be labeled blind. The complete version-locked THM038 source construction and a new11741-assertion first-order/covariance diagnostic are now supplied with source/input/output seals. The independent source gate, fresh statement-only reconstruction and separate hostile review of the entire THM039 assertion remain necessary. Root received unsolicited progress summaries saying the fresh reconstruction closes conditionally and uses Gaussian smoothing before this seal, but no proof, checker or audit output was opened; the complete root proof and diagnostic predate those summaries. This is exposed construction, never a blind audit. Any promotion requires both fresh axes and root comparison.
