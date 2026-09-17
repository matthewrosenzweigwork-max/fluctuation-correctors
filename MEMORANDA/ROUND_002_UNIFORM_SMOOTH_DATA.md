# Round 002: uniform smooth data qualification

Root Astra Ultra construction; 2026-09-17. Mathematical status PROVED_CANDIDATE; audit SELF_CHECKED pending separate review. This bounded lemma qualifies the uniform-norm hypothesis in PO-001_RESIDUAL.md for the fixed smooth model. It makes no cutoff-uniform assertion. Inputs: frozen model and independently audited THM-009; no new literature theorem imported.

Fix smooth b=-grad V, K=-grad g, positive smooth probability mu_0, finite T, and smooth terminal h. All norms below are maximum norms over componentwise derivatives of total order at most m; vector norms additionally maximize over components. Write b_m=||b||C^m, kappa_m=||K||C^m and U_m=b_m+kappa_m. The estimates hold for every existing smooth probability solution of the frozen mean-field equation, and every N>=2, beta>0, with nu=1/beta. Smooth solutions and the backward problems are the ones in the frozen model. No assertion about a singular solution is added.

For m>=0 put B_m=d(2^(m+1)-1)U_(m+1). Then

    sup_(t<=T) ||mu_t||C^m <= ||mu_0||C^m exp(B_m T).                 (D1)

Indeed u=b+K*mu satisfies ||u||C^(m+1)<=U_(m+1) using only probability mass. Differentiate the nondivergence equation partial_t mu+u.grad mu-nu Delta mu=-(div u)mu. In the transport commutator, each nonzero derivative of u leaves at most m derivatives of mu; the sum of multi-index binomial coefficients is at most 2^m-1. Summing vector components bounds this part by d(2^m-1)U_(m+1)||mu||C^m. The differentiated reaction contributes at most d 2^m U_(m+1)||mu||C^m. The scalar parabolic maximum estimate, applied to every signed derivative and their finite maximum, gives the upper Dini derivative inequality D^+||mu||C^m<=B_m||mu||C^m. Integration proves (D1). This maximum estimate is justified either by a positive smooth approximation to absolute value and then its limit, or by the first-contact argument for a strict exponential barrier on the compact torus. Nonnegative diffusion improves that argument and never appears in B_m. Positivity similarly gives min mu_t>=min mu_0 exp(-d U_1 t).

For the full backward equation (partial_t+L_1)f=0, f_T=h, let m>=1 and

    a_m=d(2^m-1)U_m+d kappa_m.

Then

    sup_(t<=T)||f_t||C^m <= exp(a_m T)||h||C^m.                    (D2)

The local transport commutator has norm at most d(2^m-1)U_m||f||C^m. For Rf(x)=integral K(y-x).grad f(y) mu(dy), every x derivative falls on K. Hence ||Rf||C^m<=d kappa_m||f||C^m for m>=1, without a derivative loss. The same finite-family maximum argument in backward time yields (D2). The nonlocal forcing need not preserve order; only its displayed norm is used. This is an a priori estimate; existence can also be obtained by the Duhamel iteration in C^m using this bounded response operator and the smooth drift-diffusion propagator.

For the zero-terminal pair corrector, use THM-009 with m>=2. Put

    Mbar=d ||mu_0||C^1 exp(3d U_2 T),
    cbar_m=2d(2^m-1)(b_m+3 kappa_m/2)+2(d kappa_m+kappa_0 Mbar).

The already proved pair propagator estimate and its forcing bound give

    sup_(t<=T)||Phi_t||C^m
      <= T exp(cbar_m T) d 2^(m+1) kappa_m
                       exp(a_(m+1) T)||h||C^(m+1).              (D3)

Here M_1(t)=sum_a||partial_a mu_t||L1<=Mbar by (D1) and torus volume one. The pair source is -J_f. Its C^m norm costs one derivative of f, already displayed in (D3). The internal interaction B/N is part of the principal transport, as required by THM-009; no bounded-operator claim for B alone is made.

Take r=4d+12. The sum of the right sides of (D1) at m=r, (D2) at m=r, and (D3) at m=r is one permissible A in the residual task card, simultaneously for all N>=2 and all beta>0. Thus fixed smooth data and fixed smooth terminal tests supply that card's uniform bounds within its existing smooth-solution class. Constants depend on d,r,T, mu_0, h and the displayed b,K norms; they have no hidden N or beta dependence. None is claimed uniform when g is replaced by g_epsilon. Heat-cutoff kappa_m diverges, and these exponential estimates do not decide singular critical power counting.

Solvable checks: when b=K=0, (D1) and (D2) reduce to the contraction bound for the heat semigroup and (D3) gives Phi=0. When K=0 but b is smooth, response and pair forcing vanish, so Phi=0 and the remaining constants are valid transport-diffusion bounds. At nu=0 the same estimates follow by characteristics; this is an a priori limiting diagnostic, not an interchange of stochastic limits. No fluctuation theorem, tightness, or critical closure is proved by this lemma alone.
