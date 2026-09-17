# THM-009 — bounded smooth backward pair problem

Version 1.0, 2026-09-17 UTC. Mathematical status: PROVED_CANDIDATE; audit ISOLATED_RECONSTRUCTION_PASS and HOSTILE_REVIEW_PASS in AUD-003, performed in two sealed/documented phases by one fresh reviewer. This separates the analytic statement from THM-008's exact algebra.

Exact assertion and negation: MEMORANDA/ROUND_001_SMOOTH.md Section 1, equations (1.1)–(1.4). For fixed smooth g,V, m>=2, probability reference mu with explicitly bounded spatial first derivative in L1, and continuous-time smooth symmetric forcing F, the terminal pair equation (partial_t+L_2+B/N)Phi=-F, Phi_T=0 has a unique symmetric smooth solution. The stated C^m bound is uniform for every N>=2 and nu>=0, with all background, kernel, forcing, m,d,T dependence explicit. There is no assumed positivity of g or response semigroup, and no hidden uniform bound on parameter-dependent mu or f.

Two proof mechanisms: additive-noise flow plus bounded response Volterra series; differentiated PDE and maximum principle. Three exact model tests include zero diffusion, negative kernel amplitude, and nonzero B/N. Code passes 120 rational identities. Exact constants and source bound are in (1.1), (1.6)–(1.7). No external source theorem is imported.

Counterexample to a stronger passage: Section 7's fixed cosine terminal test makes the pair source C^2 norm diverge under the Riesz heat cutoff. This estimate does not prove a singular inverse bound, cubic probabilistic residual estimate, subcritical CLT, or critical closure. Those remain separate obligations.
