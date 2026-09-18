# THM-040 — bounded-diffusivity homogeneous finite-dimensional Gaussian law

2026-09-18 UTC. OPEN / UNAUDITED at statement freeze. This is a separate scope extension of THM039, not an inferred critical or full-subcritical flagship theorem. Preserve the earlier card unchanged.

Fix integer d>=3,0<s<=d-2 with s<d/2, finite T>=0, coefficient-one periodic Riesz interaction on the unit-Haar torus, K=-grad g, zero external drift, and actual singular particles initially iid Haar independently of the Brownian drivers. For each N>=2 let diffusivity nu_N>=0 lie in a fixed bounded interval and converge to nu_bar>=0. Noise is sqrt(2nu_N), interaction coefficient1/N. At positive nu let b(nu)=min(1/nu,1), and set b(0)=1. Write b_N=b(nu_N), b_bar=b(nu_bar), sigma_N=sqrt(Nb_N), eta_N(t)=N^-1 sum_i delta_Xi(t).

For every fixed positive integer m and fixed deterministic tuple(t_j,h_j),t_j in[0,T],h_j real smooth periodic, the R^m vector Z_N,j=sigma_N(eta_N(t_j)[h_j]-integral h_j) converges in distribution to a centered possibly degenerate Gaussian vector. Exact one-body Haar centering must be justified. Set a_k=4pi^2|k|^2, D_k=4pi^2 c_(d,s)|k|^(s+2-d)>0 and L_k=D_k+nu_bar a_k for nonzero k, with the frozen coefficient-one c_(d,s). The covariance is

    C_ij=b_bar sum_(k!=0) hhat_i(k) conjugate(hhat_j(k))
       [(D_k/L_k) exp(-(t_i+t_j)L_k)
        +(nu_bar a_k/L_k) exp(-|t_i-t_j|L_k)].

Equivalently let Q_t preserve constants and multiply mode k by exp(-t L_k). The covariance is b_bar times the initial Gram matrix of Q_tj h_j minus their Haar means, plus

    2nu_bar b_bar integral_0^min(t_i,t_j)
      integral grad Q_(t_i-r)h_i dot grad Q_(t_j-r)h_j dx dr.

The full joint limit, zero and repeated times, constant tests, linear dependence and degenerate covariance are required. A complete proof must justify the genuine singular first-order identity, actual uniform source control, exact martingale cross bracket and its deterministic limiting value under the actual law, the initial triangular-test replacement, and the joint probability passage. No finite-N independence of the martingale and initial vector may be assumed. At nu_bar=0 this reduces to the THM039 covariance and includes sequences cooling toward zero beyond criticality; at positive nu_bar it retains a thermal contribution. No rate of convergence nu_N->nu_bar is assumed.

Complete earlier source modules, especially THM038's actual source estimate, may be used only as exact expressly conditional full-source premises until their own independent gates pass. A previous card or status label alone is not a proof. The exact negation is an admitted fixed datum/tuple/bounded diffusivity sequence violating centering, genuine needed integrability, or the stated joint weak limit. A failed bound is not a counterexample. No path-space tightness, distribution-valued topology, growing test family, s>=d/2, unbounded diffusivity, arbitrary preparation, inhomogeneity, logarithmic kernel, full microscopic-subcritical flagship, or higher hierarchy is asserted. Positive finite critical lambda, full subcritical lambda->0 and the old energy-floor condition remain distinct.
