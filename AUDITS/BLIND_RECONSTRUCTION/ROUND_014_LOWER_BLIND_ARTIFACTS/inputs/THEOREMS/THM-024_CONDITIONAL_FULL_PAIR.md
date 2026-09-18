# THM-024 — bounded-response composition and initial iid endpoint

2026-09-17, submission card. CONDITIONAL / SELF_CHECKED / VERSION_LOCKED. This abstract assertion does not presume its analytic inputs for the actual campaign data.

On the off-diagonal unit Haar torus pair space over [0,T], let S_(t,a) be a jointly measurable symmetric Markov evolution, realized by a continuous noncolliding process with deterministic conditional Markov property and composition. It is a sup-norm contraction on bounded Borel functions, consistent with a strongly measurable Haar L2 extension of norm <=exp[c(a-t)], c>=0. Diagonal values are immaterial. Let J be symmetric and jointly measurable; absolute source occupation has a bounded potential for each fixed N. Its signed bounded Borel potential U_N has sup norm <=B_N and sup_t Haar L2 norm <=A_N.

Let R_t be the exact sum of both nonlocal responses, or any jointly measurable linear operator commuting with pair exchange and bounded by C_R on Borel sup norm and Haar L2, with consistent equality-class action and strong measurability. Its off-diagonal values do not depend on diagonal representatives. All constants c,C_R are uniform in the claimed parameters. Time integrals have the assumed pointwise and Bochner measurability.

There is a unique bounded Borel terminal-zero solution of

    Phi_t = U_N(t)+integral_t^T S_(t,a) R_a Phi_a da.

It is symmetric, has sup norm <=B_N exp(C_R T), and

    sup_t ||Phi_t||_L2(Haar^2) <= A_N exp[(c+C_R)T].

It is the unique bounded Borel true-martingale inverse with source J+R Phi and terminal zero. There is also uniqueness among strongly measurable uniformly bounded-in-time L2 mild solutions. Pointwise and L2 uniqueness are different classes; no classical PDE regularity is asserted.

For iid initial density mu_0<=M_0 and the exact mean-field-centered P_N=U_2/2 with N^2 denominator (THM015), b_N=min(beta_N,1),

    E|sqrt(N b_N)P_N[Phi_0]|^2
       <= b_N M_0^2 A_N^2 exp[2(c+C_R)T]/(2N).

The density factor is squared. If A_N^2<=C rho_N as in THM023, the rates are b_N/N, b_N(1+log N)/N and b_N N^(-(d+2-s)/(s+2)). This is only on the parameter range where the hypotheses hold; bounded nu=1/beta_N requires beta_N bounded below. No path supremum, evolved iid transfer, generator-domain membership, singular Ito formula, hierarchy closure or full fluctuation theorem follows.

Exact negation: inputs satisfying every stated hypothesis fail to possess this solution/uniqueness or violate a displayed bound. Acceptance of this abstract implication does not certify any missing hypothesis for the actual dynamics.
