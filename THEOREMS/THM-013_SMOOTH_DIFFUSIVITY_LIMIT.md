# THM-013 — fixed-smooth diffusivity continuity and covariance identification

Version 1.0, 2026-09-17. Mathematical status PROVED_CANDIDATE; audit SELF_CHECKED at submission. Complete proof MEMORANDA/ROUND_002_VISCOSITY_LIMIT.md, SHA-256 700eed5dc912f4f6e621f01009ed60d5f4b479adb478ce06b8b974442e6afe2f. Preserve this submitted card and report; later audit status belongs in the ledger.

Fix the smooth periodic b,K, positive smooth probability mu_0, finite horizon and finite terminal list of THM-011. Among the existing smooth positive-diffusivity solutions, add the unique smooth zero-diffusivity solution constructed by the characteristic fixed point (2.1). Construct its full backward solutions by the response Volterra series. For every finite m and nu,nu' in a bounded nonnegative interval, the complete proof gives

sup_t ||mu_t^nu-mu_t^nu'||C^m <= C_(mu,m) |nu-nu'|,

max_a sup_(t<=t_a) ||f_a^nu(t)-f_a^nu'(t)||C^m <= C_(f,m) |nu-nu'|.

The exact sufficient constants are (3.4), (3.6), (3.9), (4.4)-(4.5), and (5.5). They use fixed data and two additional density/backward spatial derivatives, but no inverse diffusivity or lower diffusivity bound. If only a finite C^r hypothesis is used, m+2<=r; the covariance application requires only m=0 for density and m=1 for tests.

Consequently THM-011's matrices I_N,D_N converge whenever beta_N has a limit in (0,infinity]. At a finite positive beta_* they are the matrices computed from the full reference/backward equations at nu_*=1/beta_*. At beta_*=infinity, D=0 and I^{ab}=Cov_mu0(f_a^0(0),f_b^0(0)), with the constructed inviscid full backward kernels. The separately proved beta_N->0 degenerate L2 limit is retained. These identify every physical-temperature convergent subsequence in the fixed-smooth finite-dimensional model; arbitrary oscillating temperatures need not have one limit.

Exact negation: permitted data violate the displayed parameter bound with its constants or the resulting covariance identification. The proof retains both transport and response changes with the density, and displays the Laplacian's two-derivative loss. Free heat, signed one-mode response, removable resonance and a varying-data high-frequency test check these issues.

Positive-diffusivity smooth reference existence is the existing model assumption; zero-diffusivity existence/uniqueness is proved here. Particle limit conclusions additionally use THM-011 and its pair/residual hypotheses. The separate audited fixed-data qualification may supply those bounds within the existing smooth class. No singular family, field/path tightness, critical resummation or full M3 gate is claimed. The singular critical label beta_N~lambda N^(1-s/d) implies beta_N->infinity only as a fixed-smooth diagnostic, not as a singular theorem.
