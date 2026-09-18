# THM-029 — homogeneous Haar noise energy and exact law reduction

2026-09-18 UTC. OPEN / UNAUDITED at statement freeze. This is a bounded next assertion, conditional on the complete THM028 domain theorem until that prerequisite's independent gates pass. It does not assume that an evolved interacting law is iid.

Use exactly THM028's homogeneous unit-Haar model and true symmetric full pair inverse: d>=3,0<s<=d-2,N>=2,T finite,0<=nu<=nu_*<infinity,external b=0,mu=1,smooth real terminal h and its actual Fourier backward test. All constants in the following energy estimate must be independent of N and nu in that interval, depending only on d,s,T,nu_*,h and fixed kernel/cutoffs. Prove

    nu integral_0^T ||grad_(x,y) Phi_t||_L2(Haar^2)^2 dt
       <= C N^(s/(s+2)).

At nu=0 this means the zero left side; no unweighted gradient bound uniform as nu tends to zero is asserted. Both responses remain exact. No diagonal trace of Phi may be imposed to perform energy integration.

For G_t=grad_x Phi_t, A_t(x)=integral G_t(x,y)dy, and the exact mean-field-centered P_t with ordered deleted pairs, prove the Haar identity

    integral_(Haar^N) sum_i |grad_i P_t|^2
       = (N-1)/N^3 ||G_t||_2^2 - (N-2)/N^3 ||A_t||_2^2.

For nu=1/beta_N, beta_N>=1/nu_* when nu_*>0, b_N=min(beta_N,1), sigma_N^2=N b_N, deduce the deterministic Haar-averaged noise functional

    sigma_N^2 integral_0^T integral_(Haar^N)
        2nu sum_i |grad_i P_t|^2 <= C b_N N^(-2/(s+2)).

For the leading statistic eta_N(f_t), the corresponding Haar integral of the absolute cross-variation density is at most C sqrt(b_N) N^(-1/(s+2)) after multiplying by sigma_N^2. These are reference-law functionals; they are not the expected actual-particle brackets unless a law bridge is separately proved. The zero-noise limit has zero noise functionals.

Finally, for an exchangeable N-body law for which the terms are integrable, put H_t(x,y)=G_t(x,y)-A_t(x). Prove the exact identity

    E sum_i |grad_i P_t|^2 = N^-3 [
       (N-1) E|H_t(X1,X2)|^2
       +(N-1)(N-2) E H_t(X1,X2).H_t(X1,X3)
       -2(N-1) E H_t(X1,X2).A_t(X1)
       +E|A_t(X1)|^2 ],

where the distinct-triple term is absent for N=2. Identify the explicit two-/three-marginal quantities whose control would transfer the reference estimate to the actual iid-Haar-prepared singular particle law. Establish only its exchangeability and one-particle Haar invariance from the stipulated dynamics; do not assert independent higher marginals. A fixed-N exponential density domination is not a uniform estimate for this transfer.

Exact negation: an admitted tuple violates the claimed uniform energy bound, any exact coefficient, either stated reference-noise rate, or the stated symmetry/one-body-law assertion. All claims beyond the cited domain prerequisite need their own proof. No evolved residual/bracket smallness, critical hierarchy closure, full subcritical beta->0 theorem or fluctuation law is included. Keep the three campaign temperature conditions distinct.
