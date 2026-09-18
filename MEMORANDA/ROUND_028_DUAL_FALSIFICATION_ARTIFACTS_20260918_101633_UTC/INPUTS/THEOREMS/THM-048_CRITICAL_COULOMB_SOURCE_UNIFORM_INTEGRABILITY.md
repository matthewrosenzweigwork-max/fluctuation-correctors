# THM048 — actual critical Coulomb source: squared-tail control and L1/L2 equivalence

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO035. This is a bounded new subgate of the unchanged THM046; it asserts no source decay.

Use exactly the actual iid-Haar d4,s2 periodic gradient model, coefficient-one kernel g_hat(k)=|k|^-2, c=4pi², K=-grad g, independent Brownian drivers and finite positive diffusivity nu_N=1/beta_N from THM046. Fixed smooth real h and finite T>=0. Its complete backward test is f_t=Q_(T-t)^nu_N h, constants preserved, nonzero multiplier exp[-a(c+c nu_N|k|²)]. Keep literal P_N[J], all Haar rows and deleted labels, with J_t=K(x-y).(grad f_t(x)-grad f_t(y)). Define

    S_N(h,T)=sqrt(N) integral_0^T P_N[J_t]dt,
    D_N(h,T)=sqrt(N)(rho_T[h]-rho_0[Q_T^nu_N h]).

For every admitted microscopic critical sequence lambda_N=beta_N N^-1/2 -> lambda in(0,infinity), the following entire conjunction is proposed.

(A) S_N and D_N are actual L2 random variables for every finite N. For every fixed eventual interval 0<lambda_-<=lambda_N<=lambda_+<infinity, there are finite deterministic constants A,C, depending only on h,T,kernel and those interval bounds, such that for all sufficiently large N on that tail,

    E[(|S_N(h,T)|-A)_+²] <= C(1+log N)/N.

There is no universal waiting index for convergence to the interval and no convergence-rate hypothesis. The family |S_N|² is uniformly integrable along every such sequence, including its finite initial segment. The same uniform-integrability conclusion holds for |D_N|².

(B) For each fixed h,T and sequence, E|S_N|->0 if and only if E|S_N|²->0, and these statements are equivalent respectively to E|D_N|->0 and E|D_N|²->0. Thus the original THM046 assertion for this datum, with sigma_N=sqrt(N min(beta_N,1)), is equivalent to its actual second-moment version and to either endpoint-defect assertion. Failure of any such limit has the equivalent positive-limsup formulation. This is an equivalence, not proof of any of these limits.

T=0 and constant h are included. The claim does not assert finite instantaneous source variance, a pointwise kernel diagonal, positive-time product law, uniform N-body density, Gaussian convergence, quantitative source decay, a covariance-closure identity, hierarchy closure, a static-law counterexample, general initial preparation or any enlarged exponent range. No separate logarithmic normalization is imported.

Exact negation: some admitted datum/sequence violates one clause of(A) or(B): genuine finite-N L2, the stated uniform squared-overshoot bound with the specified dependence, squared uniform integrability, or an equivalence of vanishing/positive-limsup criteria. Failure of an attempted proof, infinite instantaneous source variance, nonvanishing of the still-open target or an inadmissible static law is not the negation.
