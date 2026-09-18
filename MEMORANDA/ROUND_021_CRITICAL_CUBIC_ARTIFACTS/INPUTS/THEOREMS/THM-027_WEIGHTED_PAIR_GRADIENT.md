# THM-027 — weighted first derivative of the genuine full pair inverse

2026-09-17. New assertion frozen OPEN / UNAUDITED before construction. This is a fixed-N domain prerequisite, not an N-uniform bracket estimate or a particle Ito formula.

Fix unit Haar torus, d>=3,0<s<=d-2, frozen coefficient-one positive Fourier Riesz g, K=-gradg, N>=2,finite T and 0<=nu<=nu_*<infinity. Let prescribed real densities mu_t be probability densities, continuous in time in C2 with uniform C2 bound; u_t real time-continuous C1 with uniform C1 bound; f_t real time-continuous C3 with uniform C3 bound. Bounds may depend on the fixed data. No unproved actual inhomogeneous reference/test regularity is assumed. The homogeneous actual data of THM025 meet these stronger hypotheses for smooth terminal h.

Let Phi be the unique terminal-zero bounded Borel probabilistic full pair inverse constructed in THM025 from the THM023 singular base pair evolution, source J_t=K(x-y).(gradf_t(x)-gradf_t(y)), and both exact responses R_x+R_y from THM021. It is symmetric under exchanging x,y. Equality and evaluation on the pair diagonal are treated exactly as in those modules.

For every q with 1<q<d/2, choose a positive smooth weight w_q on the off-diagonal pair space, depending only on the difference, equal to |x-y|^-q on a fixed embedded neighborhood of the diagonal and bounded above/below by positive constants outside a smaller neighborhood. The assertion is that Phi_t is C1 in both spatial variables off the diagonal for every t, with jointly Borel first derivatives, and

    sup_(0<=t<=T) [ ||Phi_t||infty + sup_(x!=y) |grad_(x,y)Phi_t(x,y)|/w_q(x-y) ] <= C.

C is finite and may depend on N,nu_*,T,d,s,q and the displayed uniform data bounds and fixed cutoffs. It must be uniform in the chosen nu within the bounded interval; no polynomial dependence or boundedness in N is asserted. All explicit coefficient choices must be supplied. The off-diagonal representative, extended arbitrarily on the diagonal, has these as its global weak first derivatives. It belongs to Haar H1 with a uniform-in-time finite bound, since 2q<d. No second derivative, time derivative, generator-domain membership, classical PDE, singular Ito passage, self/cross bracket decay, or law-limit conclusion is part of this assertion.

Exact negation: an admissible parameter/data tuple or q violates the stated off-diagonal differentiability, jointly measurable derivative, weighted bound with the stated dependence, or weak H1 conclusion. A proof must justify every expectation derivative and source occupation near collisions; smooth finite-cutoff calculations or pointwise differentiability of each path alone do not suffice. Both responses, Coulomb atom/compensation, and ordinary transport stay in the operator. Any failure must identify the exact first unsupported line, a counterexample or strongest corrected range, without changing this frozen target.
