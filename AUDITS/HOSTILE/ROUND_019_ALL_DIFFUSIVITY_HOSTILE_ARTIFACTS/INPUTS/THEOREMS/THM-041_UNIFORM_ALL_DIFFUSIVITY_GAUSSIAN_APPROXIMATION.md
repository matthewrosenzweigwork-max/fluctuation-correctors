# THM-041 — uniform source and Gaussian approximation over all diffusivities

2026-09-18 UTC. OPEN / UNAUDITED at statement freeze. This is a new two-part assertion. Earlier THM038/039/040 scopes and issued bytes remain unchanged. A bounded-parameter theorem alone does not supply this assertion.

The model has integer d>=3, 0<s<=d-2, coefficient-one periodic Riesz interaction on the unit-Haar torus, K=-grad g, zero external drift, and actual global singular particles with interaction coefficient 1/N and noise sqrt(2nu). Initial particles are iid Haar independently of their Brownian drivers. For every finite nu>=0 set b(nu)=min(1/nu,1) when nu>0, b(0)=1, and sigma=sqrt(Nb). Every uniform supremum below is over finite nu in [0,infinity), including the zero-noise flow. Infinity is only a limiting value, never an SDE coefficient. Every source uses the original ordered/deleted denominator N^2 and all original Haar contractions, with P_N=U2/2.

Part A. For each fixed finite T and fixed real smooth terminal h, define f_r^nu=Q_(T-r)^nu h. The operator Q_t^nu preserves constants and has nonzero Fourier multiplier exp(-t L_k(nu)), where L_k(nu)=D_k+nu a_k, a_k=4pi^2|k|^2, and D_k=4pi^2 c_(d,s)|k|^(s+2-d)>0, with the frozen coefficient c_(d,s). The genuine source J_f(x,y)=K(x-y) dot (grad f(x)-grad f(y)) is evaluated only off the diagonal, with its original integrable contractions. There exists C depending only on d,s,T,h and the fixed kernel such that

    sup_(finite nu>=0) sup_(0<=r<=T) E_nu |P_N[J_(f_r^nu)](X(r))|
       <= C N^(s/d-1), for every N>=2.

Every actual-law, heat-limit and constant uniformity must be justified from complete source proofs, rather than extrapolated from THM038's fixed upper diffusivity bound. No uniform time-derivative seminorm as nu diverges is required or asserted.

Part B. Additionally assume s<d/2. For each fixed positive integer m and finite deterministic tuple (t_j,h_j), with t_j in [0,T] and h_j real smooth, let

    Z_(N,nu),j=sqrt(Nb(nu))(eta_N(t_j)[h_j]-integral h_j).

The actual one-body marginals are exactly Haar. Define C(nu) by

    C_ij(nu)=b(nu) sum_(k!=0) hhat_i(k) conjugate(hhat_j(k))
        [(D_k/L_k(nu)) exp(-(t_i+t_j)L_k(nu))
         +(nu a_k/L_k(nu)) exp(-|t_i-t_j|L_k(nu))].

For probability laws P,Q on R^m, let d_BL(P,Q) be the supremum of the absolute difference of their integrals of real functions F with sup norm at most one and Lipschitz constant at most one. The entire uniform approximation is

    sup_(finite nu>=0) d_BL(Law(Z_(N,nu)), centered Gaussian(C(nu))) ->0.

Possibly degenerate covariance, constant tests, zero or repeated times, and arbitrary fixed smooth tuples are included. Every deterministic finite diffusivity sequence nu_N therefore has this Gaussian approximation without a rate or convergence assumption on nu_N. If nu_N tends to a finite nu_bar, the limiting covariance is C(nu_bar). If nu_N tends to infinity, Z_(N,nu_N) tends to zero in probability, with no growth-rate restriction. Initial-vector and martingale dependence must be handled exactly; finite-N independence cannot be assumed. Prove uniformity of the actual source residual, actual martingale bracket fluctuations, Gaussian approximation of the initial triangular iid vector, full joint probability passage and supremum over bounded Lipschitz tests. Pointwise convergence for each fixed nu is insufficient.

The exact negation is an admitted fixed datum violating genuine source integrability, the uniform Part A constant, exact centering, or uniform Part B convergence and its stated sequence consequences. A failed estimate is not a counterexample. No path-space or distribution-valued tightness, growing test list, fluctuation law at s>=d/2, inhomogeneity, arbitrary preparation, logarithmic kernel or higher hierarchy is asserted. The old energy-floor condition beta_N N^(2s/d-1)->0, full subcritical lambda_N=beta_N N^(s/d-1)->0, and finite positive critical lambda remain distinct. A result holding across these regimes does not identify their conditions. All earlier complete modules remain conditional as issued until their exact independent gates are mapped. This is not full flagship resolution.
