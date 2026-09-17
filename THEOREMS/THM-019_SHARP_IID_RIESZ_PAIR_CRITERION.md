# THM-019 — sharp vanishing criterion for the bare iid Riesz pair

2026-09-17. Root construction, PROVED_CANDIDATE / SELF_CHECKED. Separate hostile review required. Full proof: MEMORANDA/ROUND_003_SHARP_IID_PAIR_LOWER_BOUND.md; frozen positive-power Fourier convention and Haar iid law.

For every integer d>=1 and d/2<s<d, there are constants a,p,C>0 and N_0 depending only on d,s such that for every N>=N_0, with u_N=N^(2s/d-2),

    P(P_N[g]>=a u_N)>=p,
    ap u_N <= E|P_N[g]| <= C u_N.

Here P_N[g]=N^-2 sum_(i<j) g(X_i-X_j), with independent Haar X_i and the mean-zero Riesz kernel. Consequently, for every beta_N>0, sigma_N=sqrt(N min(beta_N,1)), convergence of sigma_N P_N[g] to zero in probability is equivalent to min(beta_N,1) N^(4s/d-3)->0, and equivalent to convergence to zero in L1. Unboundedness of that deterministic sequence along a subsequence implies non-tightness; boundedness implies tightness. At sqrt(N) scale this gives vanishing for s<3d/4, tight nonvanishing at equality, and non-tightness above it. The smaller-s cases use the separate THM-016/018 statements.

Exact negation: admissible data violate one displayed bound or implication. The proof uses a close-pair-count second moment, positivity of the local singularity, exact centered outer variance, and an L1 inner bound. It does not infer probability failure from variance divergence. It identifies no endpoint distribution or stable law. It is neither a theorem nor a counterexample about the actual backward corrector or singular dynamic fluctuation target. Those kernels, laws and all omitted bridges remain separate obligations. Future verdicts belong in the ledger; submitted bytes remain frozen.
