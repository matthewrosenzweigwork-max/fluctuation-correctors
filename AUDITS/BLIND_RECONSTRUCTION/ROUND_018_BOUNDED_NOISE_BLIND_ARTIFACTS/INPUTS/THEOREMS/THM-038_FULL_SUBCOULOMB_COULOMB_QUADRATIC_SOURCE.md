# THM-038 — uniform actual quadratic source through the Coulomb endpoint

2026-09-18 UTC. OPEN / UNAUDITED at statement freeze. A new identifier is used for the wider range; THM037 is unchanged.

Fix integer d>=3, 0<s<=d-2, finite T>=0, finite nu_*>=0, and a smooth real terminal test h on the unit-Haar torus. Use the frozen coefficient-one periodic Riesz interaction g_s, Fourier exp(2 pi i k.x), K=-grad g_s, zero external drift, and actual singular particles initially iid Haar independently of their Brownian drivers. For every N>=2 and 0<=nu<=nu_*, the noise is sqrt(2nu). Let f_t^nu be the actual homogeneous backward Fourier test, with nonzero mode multiplier exp(-(T-t)[4 pi^2 nu |k|^2+4 pi^2 c_(d,s)|k|^(s+2-d)]). Its constant mode is unchanged. Set J_t(x,y)=K(x-y) dot(grad f_t(x)-grad f_t(y)).

Use the genuine off-diagonal source and all original Haar contractions in the ordered deleted statistic P_N=U2/2: one half N^-2 sum_(i!=j) J_t(X_i,X_j), minus N^-1 sum_i integral J_t(X_i,y)dy, plus one half integral J_t(x,y)dxdy. No singular diagonal is assigned.

The assertion is genuine integrability and a constant C depending only on d,s,T,nu_*,h and the fixed kernel, independent of N, chosen nu and deterministic t, such that

    sup_(0<=t<=T) E |P_N[J_t](X_t)| <= C N^(s/d-1).

At zero noise the same actual deterministic flow and bound are required. At the Coulomb endpoint retain the distributional divergence atom and compensating Haar part in any argument that uses divergence; a classical pointwise Laplacian cannot replace that measure in a limiting identity. All tests are fixed arbitrary smooth functions, not merely finite Fourier polynomials.

For positive nu define b=min(1/nu,1), sigma=sqrt(Nb), with b=1 at nu=0. The quantitative consequence is

    sigma E integral_0^T |P_N[J_t](X_t)|dt <= C sqrt(b) N^(s/d-1/2).

This implies uniform scaled smallness only when s<d/2. At s=d/2 the displayed bound is only bounded; above it no decay is asserted. The exact negation is an admitted fixed datum for which no N/nu/t-independent C exists, or the asserted integrability fails. Failed upper bounds and generic-law examples are not counterexamples.

The source estimate neither requires nor certifies a pair inverse, cubic domain, full bracket, hierarchy, or fluctuation theorem. General backgrounds, logarithmic interaction, d=1,2, s>d-2, unbounded noise and changing terminal tests are excluded. Complete earlier local sources are conditional as issued. This scope extension must receive its own whole-claim reconstruction and hostile gates.
