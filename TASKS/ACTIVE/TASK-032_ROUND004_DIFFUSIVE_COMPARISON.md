# TASK-032 — diffusion-retaining local comparison in d>=s+2

2026-09-17. Next bounded construction after the R3 output seal; do not begin before the assigned worker's fresh R3 reconstruction is sealed. Root proposes the following mechanism and does not claim independent certification of it. Scientific mission and full-operator exclusions remain unchanged.

Freeze integer d>=3, 0<s<=d-2, p=s+2, N>=2, nu>=0, finite T, symmetric constant matrix A. On a punctured Euclidean relative coordinate, consider the zero-terminal operator partial_t+2nu Delta+(2s/N)|z|^(-s-2)z.grad, with source minus s|z|^-s theta.A.theta. For nu>0 first use annuli a<|z|<R with zero lateral boundary and specify the exact solution class. Handle nu=0 in the punctured characteristic class; do not impose an incompatible zero boundary condition at a transport outflow. The bounded assertion is that the solution obeys |Phi(t,z)|<=||A||_op F_(N,T-t)(|z|), with the THM017 radial profile, uniformly in annular radii, N and nu. Exact negation: admissible data/declared solution violate that displayed bound.

Root's proposed calculation to verify independently: with q=r^p/(r^p+2sp tau/N), the radial profile has

    Delta F = (N/2)[q^(s/p)(d+s-sq)-d] <= 0

when d>=p, since the derivative of the bracket's first term has the sign of d+s-(2s+2)q. The profile may therefore be a supersolution for the diffusion-retaining problem, despite anisotropic Laplacian failure of the original signed transport profile. Verify the time sign, terminal/annular boundary values, radial inequality, and a direct parabolic comparison proof. Do not presume a collision-domain result from this formal calculation.

Try to construct and identify a punctured infinite-domain limit through annular exhaustion (or prove it for a precisely defined killed-diffusion/Feynman-Kac realization), establishing nonexplosion/collision control and the integrability needed for the source. Distinguish an assumed bounded-domain classical solution from any globally constructed one. If existence/domain passage cannot be certified, return the complete conditional annular theorem and exact first unproved line rather than asserting a global inverse. Any imported existence theorem needs a primary-verified precise source/hypotheses or a self-contained proof.

Further root seed to test, not a certified input: the additive-noise SDE dZ=sqrt(4nu)dB+(2s/N)|Z|^(-s-2)Z dt admits stopped pathwise Picard construction because the drift is locally Lipschitz off zero. For V(r)=r^2+r^-q, q>0,

    LV = 4nu d +(4s/N)r^-s
       +2nu q(q-d+2)r^-q-2 -(2sq/N)r^-q-s-2.

This is bounded above for each fixed N,nu,q; the negative highest singular power can control approach to zero, and r^2 controls infinity. Check the optional-stopping passage and exact exit probabilities. Applying Ito to the positive radial transport profile along stopped paths may give an integrable positive-source bound independent of nu. The signed angular source is bounded by ||A|| times that source. A global bounded probabilistic solution in an explicitly defined martingale class may be sufficient even if classical regularity has not yet been established; do not silently call a measurable expectation a classical solution. Define and prove any Markov/uniqueness or kernel measurability step actually used.

For a justified limiting kernel, derive the compactly supported periodic diagnostic iid endpoint from THM015/017 bounds, with one density factor, all centerings and sup outside expectation. The question is the local diffusion-retaining model only: ordinary transport, both nonlocal responses, actual time-dependent test and periodic force remainder remain omitted, and no evolved-law or singular flagship theorem follows. Test d=s+2, d>s+2, nu=0, large nu, isotropic/traceless A, N=2,3 and zero remaining time. Do not infer anything in d<s+2 from this comparison.

Work in a new isolated local worktree from the published R3 commit once available, or the explicit R2 base with separately hashed prerequisite dossier if dispatched earlier. Read only permitted frozen model, THM015/017 statements/proofs and the reviewed rescaling/erratum. Write MEMORANDA/ROUND_004_DIFFUSIVE_COMPARISON.md with all quantifiers/constants/domains and seal before separate review. No root canonical edits, source rewrites, commits, pushes, dependencies or child workers. No broad new plan in place of the proof.
