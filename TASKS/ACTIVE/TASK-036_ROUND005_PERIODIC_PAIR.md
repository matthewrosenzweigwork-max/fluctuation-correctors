# TASK-036 — periodic singular pair Markov potential with bounded diffusivity

2026-09-17. Natural continuation after a worker's R4 report is sealed. Root seed below is explicitly unproved. New isolated worktree from published R3 52bda5d0d24067b051c6fe9763f2a78e7599e593 plus permitted sealed R4 local proof. No other unsealed worker proof. Astra Max constructor, not a blind certification task.

Freeze unit Haar torus, integer d>=3, 0<s<=d-2, g coefficient-one local Riesz potential with g=|z|^-s+smooth near zero, smooth off zero, even and periodic, K=-grad g odd. N>=2, nu in [0,nu_*] for fixed finite nu_*; T finite. Prescribed u_t is continuous in time and C1 in space uniformly, with bounded derivative and divergence lower bound -D. Prescribed f_t is continuous in time and C2 in space uniformly. These background/test bounds are hypotheses, not a claim about the actual mean-field/test equations.

Construct a global pair process off the diagonal with independent noises sqrt(2nu), first drift u_t(x)+K(x-y)/N, second u_t(y)+K(y-x)/N. Exact source J_t(x,y)=K(x-y).(grad f_t(x)-grad f_t(y)). Define its signed source potential by expectation through T. Prove/falsify existence, noncollision, measurable two-time Markov evolution, a bounded Borel terminal-zero martingale class and unique potential in that class, and

    sup_t ||U_N(t)||_L2(Haar^2)^2 <= C *
      1,                         2s<d,
      1+log N,                   2s=d,
      N^((2s-d)/(s+2)),           2s>d,

with C independent of N and nu in the declared interval. Exact negation: admissible data violate any included assertion. No nonlocal responses are included in this base generator; their bounded perturbation is a separate task. No full fluctuation theorem or evolved iid law. State all hypotheses and constants without claiming results beyond the interval of diffusivities.

Root barrier seed: relative drift near diagonal is (2s/N)r^-s-2 z plus w_t(x,y) with |w|<=Lr. Since -r F_r<=s F for the R4 radial profile, exp(c tau) F can absorb this Lipschitz drift. A fixed radial cutoff chi(r)F plus C tau, with a suitable exponential, may dominate the actual time-dependent source globally. On the cutoff annulus the profile and its first two derivatives are O(tau), uniformly in N; bounded nu_* keeps all cutoff diffusion errors controlled. Prove these estimates and the full backward signs. The singular Lyapunov chi(r) r^-(d-2) may prove noncollision. Do not use a torus distance formula across its cut locus: work inside an embedded ball and a fixed smooth cutoff.

Secondary exact interface needed for later L2 response perturbation: establish ||S_(t,a)||_(L2->L2)<=exp[(D+C0/N)(a-t)] if div K>=-C0 as a measure. For a smooth heat regularization, pair divergence is div u(x)+div u(y)+(2/N)div K(x-y); derive the energy sign and factor exactly. Then justify passage to the constructed singular Markov semigroup, not merely formal integration by parts. A possible path is local pathwise convergence of smooth approximations along noncolliding paths, the uniform density bound tested first on continuous functions, measure extension, and L2 density/continuity. All these are proof obligations. Do not assume uniform operator-norm convergence.

Permitted inputs: AGENTS, model, THM015/017/020 statements, sealed R4 local diffusion construction/reconstruction once supplied, R1 response/operator definitions, R3 heat representation and normalization. No response worker proof before its seal, no root later notes, no existing review interpreted as a theorem. Freeze all supplied inputs. Write complete MEMORANDA/ROUND_005_PERIODIC_PAIR_POTENTIAL.md, optional exact checks, and output/input manifests. No canonical root edits, commits, pushes, dependencies or child workers. If the full bound fails, return the exact first failure and strongest corrected bounded result. A separate fresh hostile review is required after construction.
