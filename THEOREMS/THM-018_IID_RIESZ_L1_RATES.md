# THM-018 — initial iid Riesz pair L1 rates

2026-09-17. PROVED_CANDIDATE / SELF_CHECKED at submission. Constructed independently as Section 7 of the sealed TASK-024 statement-only reconstruction, AUDITS/BLIND_RECONSTRUCTION/ROUND_003_PROBABILITY_RECONSTRUCTION.md, SHA-256 9eb7e54ab0fa6e38ef226cd2d815d618d2b421718ed0e1c59bb07dc27ae79e6f. That worker had not seen root's THM-019 construction. Separate hostile review required for this extension.

For fixed integer d>=1 and 0<s<d, iid Haar particles on the unit torus, the frozen mean-zero positive-power Riesz kernel, and every beta_N>0, put b_N=min(beta_N,1), sigma_N=sqrt(N b_N). For all sufficiently large N, constants depending only on d,s give

    E|sigma_N P_N[g]| <= C sqrt(b_N/N),                         2s<d;
    E|sigma_N P_N[g]| <= C sqrt(b_N(1+log N)/N),                2s=d;
    E|sigma_N P_N[g]| <= C sqrt(b_N) N^(2s/d-3/2),              2s>d.

Here P_N[g]=N^-2 sum_(i<j) g(X_i-X_j), almost surely finite and integrable. Constants and the sufficient N threshold are explicit in Sections 2, 4 and 7 of the proof. The proof splits at radius N^(-2/d), centers both the inner and outer kernels, uses the exact iid outer variance and the inner absolute-mass bound with coefficient (N-1)/(2N). No event excluding close pairs is needed.

Exact negation: an admissible fixed d,s has no constants and threshold independent of N and beta_N satisfying its displayed bound. This card claims upper bounds and sufficient L1 convergence only. No converse, stable law, actual backward-corrector estimate, interacting-law bound, or singular dynamic comparison follows from this card. Subsequent dispositions belong in the canonical ledger, not in these frozen bytes.
