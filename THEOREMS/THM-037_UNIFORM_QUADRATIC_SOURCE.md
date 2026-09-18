# THM-037 — actual quadratic source at the microscopic energy scale

2026-09-18 UTC. OPEN at statement freeze. This is a separately identified stronger subclaim for the THM036 construction; no audit pass or proof is presumed from a worker progress message.

Fix integer d>=4,0<s<2,finite T>=0,finite nu_*>=0,smooth real terminal h, the frozen coefficient-one periodic Riesz kernel, unit Haar, K=-grad g and zero external drift. Let N>=2 and0<=nu<=nu_*. Use the actual singular particles initially iid Haar independently of their Brownian drivers, and the actual homogeneous Fourier backward test f_t^nu on[0,T]. Define J_t(x,y)=K(x-y) dot(grad f_t(x)-grad f_t(y)), using its genuine off-diagonal representative and the exact R1/R8 ordered statistic P_N=U2/2 with all original Haar contractions. No diagonal value is assigned to the singular kernel.

The assertion is a constant depending only on fixed d,s,T,nu_*,h and the fixed kernel, independent of N,selected nu and deterministic t, such that

    sup_(0<=t<=T) E | P_N[J_t](X_t) | <= C N^(s/d-1).

The expectation is of the absolute statistic under the actual evolving law, not its signed expectation or a reference product law. Prove genuine integrability and the uniform quantitative bound, including zero noise. In particular, with b=min(1/nu,1),sigma=sqrt(Nb) for positive noise and b=1,sigma=sqrt(N) at zero noise,

    sigma E integral_0^T |P_N[J_t](X_t)|dt <= C sqrt(b) N^(s/d-1/2) ->0

uniformly throughout the bounded noise interval. The exact negation is admitted fixed data for which no such N/nu/t-independent constant exists. Do not mistake a failure of one estimate for such a counterexample. This source estimate alone is not a complete fluctuation theorem, a cubic estimate without the exact identity, or a claim for s=2,d=3,Coulomb,logarithmic interaction,general backgrounds or unbounded noise. All earlier complete local premises retain their issued conditional scope.
