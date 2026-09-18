# THM047 — Coulomb lower contractions and exact remaining dynamic obligation

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO034. Separate bounded subgate of THM046; neither original target nor negation is changed.

Use the exact THM046 model: unit T4, g_hat(k)=|k|^-2 for nonzero k, K=-grad g, c=4pi^2, iid Haar initial data, independent Brownian drivers, drift N^-1 sum_(j!=i)K and noise sqrt(2nu_N), beta_N=1/nu_N>0, lambda_N=beta_N N^-1/2->lambda in(0,infinity). Fixed smooth real h and T>=0. f_t=Q_(T-t)^nu_N h has multiplier exp[-a(c+c nu_N |k|^2)] on nonzero modes and preserves constants. J_t=K(x-y).(grad f_t(x)-grad f_t(y)). P_N is the exact ordered deleted-pair statistic with denominator2N^2, minus empirical/Haar row plus half double Haar mean; rho=eta-dx. Every U_k retains all original Haar backgrounds and ordered distinct labels/N^k.

Let Phi_t be the genuine symmetric terminal-zero full pair inverse supplied by the exact R5/R8 modules, with BOTH responses, solving off diagonal

    partial_t Phi +nu_N(Delta_x+Delta_y)Phi +B Phi/N +R Phi=-J,
    B Phi=K(x-y).(grad_x-grad_y)Phi,
    R Phi=-2c Phi+c q(x)+c q(y), q(x)=int Phi(x,y)dy.

Keep its actual R8 finite-N domain, genuine contractions, true square-integrable martingale and all fixed-N limiting passages. No additional diagonal value is assigned. Define b_t(x)=int B Phi_t(x,y)dy and

    ell_N(t)=rho_t[b_t]/N +(1/(2N))int b_t.

The frozen conjunction is:

(A) For every fixed N and t the normalized spherical average

    tau_t(x)=lim_(epsilon down0) (1/|S3|)int_(S3)Phi_t(x,x-epsilon theta)dS(theta)

exists, and |tau_t(x)|<=||Phi_t||infinity. With D=grad_x+grad_y, the exact contraction identity is

    b_t(x)=int_(T4) K(z).D Phi_t(x,x-z)dz +2c(q_t(x)-tau_t(x)).

For each nonnegative integer j, sup_t ||b_t/sqrt(N)||C^j <= C||h||C^(j+3), uniformly for all N>=2 and positive nu_N in a fixed bounded interval. Constants depend only on fixed T/kernel/bounded interval and j. The scalar int b_t is exactly zero for this genuine homogeneous-source inverse. The assertion is about an averaged trace, not an assumed pointwise diagonal or directionwise limit.

(B) Under the actual iid-prepared dynamics,

    sqrt(N) E int_0^T |ell_N(t)|dt <= C N^-1/4

for all sufficiently large N on each admitted critical sequence. In particular the bound is for the absolute lower drift, not just its signed mean.

(C) Set Psi_(t,delta)=exp(delta Delta_x)exp(delta Delta_y)Phi_t, delta_N=N^-1/40, V_N=Phi-Psi_(delta_N). Let

    M_t^2[v]=sqrt(2nu_N) sum_i int_0^t grad_i P_N[v_a](X_a).dW_i(a),
    C Phi=Sym_3[K(x-z).grad_x Phi(x,y)]

with Sym_3 the average over six permutations. All terms below are genuine integrable random variables and M^2[V_N] is the difference of true square-integrable martingales. For

    S_N=sqrt(N) int_0^T P_N[J_t]dt,
    W_N=sqrt(N)[int_0^T U_3[C Phi_t]dt +M_T^2[V_N]],

one has the uniform bound

    E|S_N-W_N| <= C[N^-1/4 +sqrt((1+log N)/N)+N^-3/8] ->0.

Thus the original THM046 L1 assertion is equivalent to E|W_N|->0; positive limsup in its exact negation is preserved. This equivalence, not either limit, is part of the new assertion. The finite initial segment with b_N=min(beta_N,1)!=1 does not affect the limits. T=0 and constant h are included. No rate for lambda_N convergence is assumed.

Exact negation of THM047: an admitted datum/parameter/critical sequence violates at least one clause (A),(B),(C), including trace existence, its coefficients, uniformity, scalar zero, actual domain or displayed rate. Failure of one construction is not the negation. The main dynamic target remains OPEN. No separate vanishing of U3 or the residual bracket, instantaneous absolute U3 estimate, Coulomb occupation extension from strict sub-Coulomb, general-preparation statement, Gaussian law or hierarchy closure is asserted.
