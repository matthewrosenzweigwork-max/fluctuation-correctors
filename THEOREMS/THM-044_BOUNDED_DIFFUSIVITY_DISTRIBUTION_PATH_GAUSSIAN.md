# THM044 — distribution-valued continuous-path Gaussian law

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO031. Fix d>=3,0<s<=d-2,s<d/2, finite T, actual homogeneous iid-Haar-prepared singular gradient dynamics on the unit torus, coefficient-one periodic Riesz force1/N and independent noise sqrt(2nu_N). Assume0<=nu_N<=nu_*<infinity and nu_N->nu_bar>=0, with no rate. Let b(0)=1,b(nu)=min(1,1/nu) for positive nu and Z_N(t)=sqrt(Nb(nu_N))(eta_N(t)-dx), a real mean-zero distribution. Every original normalization/contraction remains.

Set alpha=(d-s)/2, M=d+2, R=alpha+M+3. Fix any real r>R+d/2=2d+5-s/2. The real Hilbert space H^-r has squared norm sum_(k in Z^d)(1+|k|^2)^(-r)|u_hat(k)|^2 with conjugate Fourier symmetry. The assertion is weak convergence of the actual continuous random paths Z_N in C([0,T],H^-r), with the uniform Hilbert norm, to the following centered continuous Gaussian random distribution, with all zero-time/noise/constant/degenerate cases included.

Use the real orthonormal mean-zero Fourier basis e_l (sqrt2 sine/cosine for one representative of each opposite-frequency pair), a_l=4pi^2|k_l|^2,D_l=4pi^2 c_ds |k_l|^(s+2-d),L_l=D_l+nu_bar a_l. Independent standard real normals xi_l and independent standard Brownian motions B_l define coefficients

    G_l(t)=sqrt(b_bar)[exp(-L_l t) xi_l
               +sqrt(2nu_bar a_l) integral_0^t exp(-L_l(t-u))dB_l(u)].

The resulting series sum_l G_l(t)e_l must be proved to define a continuous H^-r-valued Gaussian process. For any fixed smooth tests h_i,h_j and times t,u, its covariance is exactly the THM040/042 initial-plus-thermal covariance, equivalently sum_l h_i,l h_j,l b_bar[(D_l/L_l)exp(-(t+u)L_l)+(nu_bar a_l/L_l)exp(-|t-u|L_l)]. Exact first-marginal Haar centering must be retained.

Required quantitative interface: a continuous decomposition Z_N=Y_N+E_N in H^-r with E sup_t||E_N(t)||_(H^-r)<=C sqrt(b_N) N^(s/d-1/2), and Fourier projection Pi_K onto |k|<=K satisfying

    E sup_t||(Id-Pi_K)Y_N(t)||_(H^-r)^2
         <=C sum_(|k|>K)(1+|k|^2)^(-r)(1+|k|^2).

Constants depend only on fixed d,s,T,nu_*,r,kernel data, not N,selected nu_N,K. The precise Hilbert-valued existence, all infinite sums, simultaneous-source control, actual tightness and full bounded-continuous weak passage must be justified. Fixed-test convergence alone is insufficient. The explicit r restriction is sufficient and is not asserted optimal.

Exact negation: some admitted fixed parameters/noise sequence violates genuine Hilbert-path existence, one of the stated uniform estimates, Gaussian-series existence/continuity, exact centering, actual path tightness or the asserted weak convergence. A weaker topology or changed parameter/test class cannot silently replace this assertion. No unbounded-diffusivity path theorem, larger s, higher-order hierarchy, inhomogeneous/logarithmic setting, arbitrary preparation or complete flagship is asserted. Old-floor, full-subcritical and finite-critical conditions remain distinct.
