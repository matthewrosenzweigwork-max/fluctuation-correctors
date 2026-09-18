# THM042 — fixed smooth observables, continuous-path Gaussian law

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. New assertion; no earlier card is modified. PO029. Model: exactly ROUND_001_MODEL, unit-Haar torus, coefficient-one Riesz, K=-grad g, force1/N, independent noise sqrt(2nu_N), actual global singular gradient paths, iid Haar starts independent of drivers, zero external drift. Fix d>=3,0<s<=d-2,s<d/2,finite T>=0, finite positive integer m and fixed real C-infinity tests h_1,...,h_m. Let every finite diffusivity satisfy0<=nu_N<=nu_*<infinity and nu_N->nu_bar>=0 without a rate. Let b(nu)=min(1/nu,1) for positive nu and b(0)=1, sigma=sqrt(Nb).

Primary assertion: the continuous actual vectors Z_N(t)=(sigma[eta_N(t)h_j-integral h_j])_j converge weakly in C([0,T],R^m), with its uniform norm, to a centered continuous Gaussian process Z. One-body Haar centering is exact. With a_k=4pi^2|k|^2,D_k=4pi^2 c_(d,s)|k|^(s+2-d),L_k=D_k+nu_bar a_k, its covariance at arbitrary t,u in[0,T] is

    E Z_i(t)Z_j(u)=b(nu_bar) sum_(k!=0) h_i_hat(k) conj(h_j_hat(k))
      [(D_k/L_k)exp(-(t+u)L_k)+(nu_bar a_k/L_k)exp(-|t-u|L_k)].

The process may be degenerate. Zero noise, zero/finite T, constant or linearly dependent tests are included. Supply existence of the continuous Gaussian process, full uniform-path tightness and weak-limit identification, not only finite-dimensional covariance convergence. Genuine singular identities and every original source/background/Itô term must remain visible. A source bound at one fixed terminal time alone is insufficient for the supremum over t.

Exact negation: some admitted fixed datum and bounded convergent noise sequence violates exact centering, continuity/existence of the specified limiting Gaussian process, tightness of the actual path laws, or weak convergence to that process in the stated uniform topology. Failure of a particular proof estimate is not the negation. No unbounded-noise/path-uniform approximation, distribution-valued field, growing test list, higher exponent, logarithmic/inhomogeneous/arbitrary-preparation theorem or full hierarchy claim. Old energy-floor, full microscopic subcritical and finite-positive critical conditions remain distinct. Full sources, construction and both fresh independent gates are required before promotion.
