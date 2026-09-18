# THM-026 — finite-N singular particle realization, heat passage and density bound

2026-09-17. OPEN / UNAUDITED / VERSION_LOCKED at statement freeze, before receiving the TASK045 constructor. The claim is finite-N and does not certify a corrector domain or N-uniform interacting-law estimates.

On unit Haar torus, fix d>=3,0<s<=d-2, the frozen positive Fourier Riesz g_s with local coefficient one, K=-gradg_s, and smooth real periodic V with b=-gradV. Let N>=2,0<=nu<infinity,T<infinity. From every configuration of N pairwise distinct coordinates, the SDE

    dX_i=[b(X_i)+(1/N)sum_(j!=i)K(X_i-X_j)]dt+sqrt(2nu)dW_i

has a pathwise unique global jointly measurable realization through T, with no pair collisions almost surely from each fixed start. It has the deterministic-time conditional Markov property; no common exceptional set for all uncountably many starts is asserted. Each finite-horizon realized path has a strictly positive minimum pair distance.

Heat-regularized interactions with the same driving Brownian motions converge uniformly in time almost surely to this path for each fixed tuple/start. No rate uniform in N,nu or initial configurations is asserted. For any initial probability density F0 on the N-particle Haar space with finite supremum norm, its singular time-t law has density bounded almost everywhere by

    F_t <= ||F0||infty exp{[N a+(N-1)kappa]t},

where a,kappa>=0 satisfy divb>=-a and divK>=-kappa as a finite measure. In particular iid mu0<=M gives M^N times this exponential, not a uniform iid-moment estimate.

An explicit finite-N stopped energy/noncollision estimate must accompany the construction, using H_N=sum_i V(x_i)+(1/N)sum_(i<j)g_s(x_i-x_j) and a nonnegative shift depending only on the fixed data and N. It must retain the exact Nd Laplacian coefficient2/N and justify all stopped expectations. Partial/simultaneous collisions and smooth periodic remainders are included. The energy bound is also integrable under any bounded F0. All constants and per-start quantifiers must be stated.

Exact negation: an admissible tuple/start/density violates any stated construction, noncollision, uniqueness, path convergence, measure domination or energy assertion. The logarithmic case, attractive forces, non-gradient external drift, unbounded initial density, uniform-N law transfer, pair-kernel gradients, singular corrector Ito passage, residual/brackets, Gaussianity and hierarchy closure are outside this claim. The first remaining corrector-domain assertion is not implied by particle existence.
