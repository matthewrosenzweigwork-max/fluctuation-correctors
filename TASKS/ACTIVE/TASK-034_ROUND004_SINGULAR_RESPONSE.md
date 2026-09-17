# TASK-034 — singular response operator in the Newtonian-or-weaker range

2026-09-17. Bounded independent analytic workstream. Base published R3 52bda5d0d24067b051c6fe9763f2a78e7599e593. Root proposes the following mechanism, not a certified input. Freeze d>=3, 0<s<=d-2, unit Haar torus, Fourier normalization and coefficient-one local g=|z|^-s+smooth from R3, K=-grad g. mu is a C1 probability density, with explicit sup and gradient bounds.

Exact question: does div K extend to a finite signed measure, with the Coulomb atom and torus mean-zero compensation computed with exact constants, and do both responses extend to bounded L2 and bounded Borel operators by

R_x Phi(x,y) = -integral Phi(z,y) [mu(z) div K(z-x) + K(z-x).grad mu(z) dz],

with the analogous y term and norm at most C_R=2(||mu||infty ||div K||TV + ||grad mu||infty ||K||L1)? Prove or falsify including well-defined equivalence classes, the diagonal atom, pair symmetry, time-uniform parameters, convergence of a named mollification, and consistency with the original gradient formula on smooth Phi. Exact negation: some admissible g,mu,Phi violates well-definedness or the displayed operator norm.

Root seed: for s<d-2 the singular divergence is s(d-2-s)|z|^-s-2 locally; at s=d-2 the atom is (d-2)|S^(d-1)| delta_0. Smooth periodic remainder may contribute a signed measure of total integral cancelling the positive singular contribution; global nonnegativity is impossible at nonzero mass. Prove, do not assume, these statements and integration-by-parts boundary passages. For heat mollification measure TV and K L1 do not increase; prove strong L2 response convergence using approximate identities and explicit multiplication/commutator treatment. Do not claim uniform operator-norm convergence at the Coulomb atom.

Secondary bounded assertion if the first closes: for the smooth mollified pair Markov generator G_N=nu(Delta_x+Delta_y)+u(x).grad_x+u(y).grad_y+(1/N)K(x-y).(grad_x-grad_y), establish an L2 propagation bound uniform in mollifier,N>=2,nu>=0 when div u has a uniform lower bound and div K has a uniform lower bound as a measure. Derive signs, pair factor2/N and the norm exponent. Do not infer the singular diffusion's existence or a semigroup limit without proving it. This is the response/energy interface, not the actual full corrector or evolved-law closure.

Read AGENTS, frozen model, R1 algebra response definitions and R3 local heat representation, exact THM015 statement as needed. Do not read either unsealed R4 diffusion proof or other worktrees. Write MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md with complete proof, exact hypotheses, negative tests and source provenance; optional exact checker. Freeze an input manifest and seal outputs, then stop for root comparison. Own new local worktree and codex/ branch; no root canonical edits, commits, pushes, dependencies, global changes or child workers. Astra Max. Constructor report requires subsequent separate audit before promotion.
