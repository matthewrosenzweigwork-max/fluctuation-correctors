# THM-025 — full periodic probabilistic inverse and actual homogeneous initial endpoint

2026-09-17. PROVED_CANDIDATE / SELF_CHECKED / VERSION_LOCKED at submission. THM021/023/024 are explicit prerequisite modules with their own separate audit histories. This card does not enlarge their scopes or identify a Borel inverse with a finite-particle Ito domain.

Use unit Haar torus, frozen Fourier Riesz kernel K=-grad g_s, d>=3,0<s<=d-2,N>=2,finite T,nu in[0,nu_*] with finite nu_*. Prescribe a time-continuous C1 probability density mu_t with uniform M0,M1 bounds, a time-continuous uniformly C1 u_t with divu>=-D_u, and a time-continuous uniformly C2 real test f_t. No general mean-field existence is asserted. The base pair generator has ordinary transport u, independent noise sqrt(2nu), and exact internal B/N. J_t=K(x-y).(gradf_t(x)-gradf_t(y)). Both exact nonlocal responses are those of THM021, with this same mu.

THM021/023 satisfy every hypothesis of THM024 for these data, including pointwise independence of diagonal extensions off the diagonal, Haar consistency and time measurability. Consequently there is a unique symmetric bounded Borel terminal-zero martingale inverse Phi with integrated source J+(R_x+R_y)Phi along the auxiliary base pair process. It has sup_t Haar L2 squared norm <=C rho_N, with rho_N=1,1+logN,N^((2s-d)/(s+2)) according as2s<d,=d,>d. Constants depend only on displayed fixed data, not N or nu in the interval.

For iid initial law with density mu_0 and b_N=min(beta_N,1), the exact mean-field-centered P_N with N^2 denominator satisfies

    E|sqrt(Nb_N)P_N[Phi_0]|^2 <= C M0^2 (b_N/N) rho_N.

This uses both responses and actual prescribed time-dependent source. It is a direct endpoint estimate, not closeness to a specific diagnostic. With nu=1/beta_N, uniformity requires beta_N>=beta_*>0; zero noise is a separate included limit. No assertion for every subcritical beta_N tending to zero.

Actual-data subcase: set external drift b=0 and mu_0=1. The reference mu_t=1,u=0 solves the frozen mean-field equation. For any real smooth terminal h, the actual backward one-body test is

    f_t(x)=h_hat(0)+sum_(k nonzero) h_hat(k)
       exp[-(T-t)(4pi^2 nu |k|^2+4pi^2 c_(d,s)|k|^(s+2-d))]
       exp(2pi i k.x).

It solves partial_t f+nu Delta f+R f=0 with f_T=h and has every fixed spatial derivative uniformly bounded in N,t,nu>=0. Thus the preceding inverse/initial endpoint holds for actual homogeneous reference/test data, for beta_N>=beta_*>0. All critical lambda_N=beta_N N^(s/d-1)->lambda in(0,infinity) eventually satisfy this beta restriction; only the subcritical sequences satisfying it are included. No general weak-solution uniqueness for the mean-field equation is required or claimed.

Exact negation: admissible prescribed data, or the explicit homogeneous reference/test, violate any stated module-interface, inverse or endpoint assertion. The following are outside the claim: classical/kernel derivative regularity, singular finite-particle Ito passage, evolved iid propagation, residual/bracket estimates, Gaussian fluctuation limit, critical hierarchy closure, unbounded-diffusivity pair estimate, logarithmic case or altered normalization.
