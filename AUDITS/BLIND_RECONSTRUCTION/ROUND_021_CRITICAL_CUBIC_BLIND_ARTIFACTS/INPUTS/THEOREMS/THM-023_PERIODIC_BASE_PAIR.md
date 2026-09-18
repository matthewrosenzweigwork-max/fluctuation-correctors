# THM-023 — periodic singular base pair potential

2026-09-17, submission card. PROVED_CANDIDATE / SELF_CHECKED / VERSION_LOCKED. This statement is a candidate, not an audit verdict. The scope is prescribed regular backgrounds and tests, with bounded diffusivity.

Fix integer d>=3, 0<s<=d-2, p=s+2, finite T,nu_*>=0. On the unit Haar torus let g be even, periodic, smooth off zero, and equal to |z|^-s+q(z) in an embedded ball, with q smooth and even there. Set K=-grad g. Let u_t be continuous in time and C1 in space with uniform derivative bound and div u_t>=-D, D>=0. Let f_t be continuous in time and C2 in space with uniform gradient and Hessian bounds. The time-space derivatives are jointly measurable. These are hypotheses, not assertions about the actual mean-field and backward-test equations.

For every N>=2 and nu in [0,nu_*], the pair process with drifts u_t(x)+K(x-y)/N and u_t(y)+K(y-x)/N and independent noises sqrt(2nu) has a global pathwise unique, jointly measurable, noncolliding realization from every off-diagonal state. It defines a deterministic-time Markov evolution S_(t,a). For J_t(x,y)=K(x-y).(grad f_t(x)-grad f_t(y)), absolute source occupation through T is integrable from every start and its potential is bounded uniformly in t,x,y for each fixed N. The signed potential U_N is symmetric bounded Borel, terminal zero, and is unique in the bounded Borel true-martingale source class. No classical regularity or diagonal-start dynamics is asserted.

With constants depending only on the stated fixed data, not N or nu in the interval,

    sup_t ||U_N(t)||_L2(Haar^2)^2 <= C rho_N,
    rho_N = 1                    if 2s<d,
            1+log N             if 2s=d,
            N^((2s-d)/(s+2))     if 2s>d.

Distributionally div K=P+R_g, with P nonnegative (the local Riesz density or Coulomb atom) and R_g smooth bounded; write C0=||(R_g)_-||infty. Heat regularization K_epsilon=e^(epsilon Delta)K defines smooth pair evolutions S_epsilon. Their Haar L2 norms and that of S are at most exp[(D+C0/N)(a-t)]. S_epsilon converges strongly in Haar L2 to S for each fixed N,nu,t,a as epsilon decreases to zero. The two-time singular evolution is jointly strongly continuous on Haar L2. This includes equality-class independence and a justified singular passage, not just a formal energy identity. No operator-norm convergence or convergence of heat-regularized source potentials is claimed.

Exact negation: admissible data violate any declared existence, uniqueness, integrability, norm, measurability or convergence assertion. No nonlocal response is in this base generator; finite-particle generator-domain, evolved-law and critical hierarchy assertions are outside this card. Earlier local radial assertions may be used only in their stated scopes.
