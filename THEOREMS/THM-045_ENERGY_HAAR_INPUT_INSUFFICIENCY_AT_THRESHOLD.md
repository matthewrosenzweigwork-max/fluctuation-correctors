# THM045 — static energy/Haar inputs do not force threshold source decay

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO032. This is a static-law insufficiency assertion, not a counterexample to the actual iid-prepared dynamics or a change to either flagship mission.

Fix the coefficient-one periodic Coulomb kernel in dimension4: g_hat(0)=0,g_hat(k)=|k|^-2 for k!=0, local g(x)=|x|^-2+H(x), K=-grad g. Haar mass is one and Fourier characters exp(2pi i k.x). Put h(x)=cos(4pi x_1), J_h(x,y)=K(x-y).(grad h(x)-grad h(y)), H_N=N^-1 sum_(i<j)g(x_i-x_j), eta_N=N^-1 sum_i delta_xi, and the literal deleted statistic

    P_N[J_h]=(2N^2)^-1 sum_(i!=j)J_h(x_i,x_j)
               -eta_N[integral J_h(.,y)dy]+(1/2)integral J_h(x,y)dxdy.

The assertion: there exist fixed positive a,c and an integer m0, and for every integer m>=m0, with N=m^4, a bounded smooth probability density F_N on (T^4)^N such that its law is exchangeable and invariant under simultaneous translations, every one-body marginal is exactly Haar, its support has minimum pair distance at least c/m, and H_N<=-c m^2 throughout its support. Nevertheless

    lim_(m->infinity) sqrt(N) E_(F_N)|P_N[J_h]|=16 pi^3 a^2>0.

The fixed a is independent of m and may be chosen sufficiently small. No bound on the N-body density uniform in N is asserted. Every singular source/background integral must be justified with the exact coefficient and original centering; the smooth-density construction and the displayed limit, not just an atomic example or heuristic continuum expansion, are required.

Exact negation: no such fixed constants/sequence exists, including failure of any symmetry, support, energy, regularity or exact limit requirement. A failure of one construction is not the negation. No iid law, actual evolved law, beta/nu sequence, dynamic entropy or Gaussian/higher-corrector failure is claimed. This tests precisely whether nonpositive energy plus exact Haar centering and exchangeability alone can extend the scaled absolute quadratic-source decay to s=d/2. The actual iid-flow endpoint remains open regardless of this gate's outcome.
