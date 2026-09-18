# Round 005 full-pair interface and actual homogeneous data

2026-09-17. Root construction, PROVED_CANDIDATE / SELF_CHECKED. The composition is conditional on the precise THM023/024 modules until their independent reviews pass. This document checks their interface with THM021 and gives a completely explicit actual-data subcase. It is not a finite-particle generator-domain theorem or a fluctuation limit.

## Prescribed regular data and exact interface

Fix unit Haar torus, d>=3,0<s<=d-2,N>=2,finite T, and nu in a fixed interval [0,nu_*]. Use the frozen Fourier Riesz kernel g_s, K=-grad g_s. Let mu_t be a nonnegative probability density continuous in time with values in C1, with uniform bounds M0 and M1 on density and gradient. Let u_t be continuous in time and C1 in space uniformly, div u_t>=-D_u, and f_t continuous in time and C2 in space uniformly. These are prescribed data; one may take u=b+K*mu if it meets these bounds, but no general mean-field existence assertion is hidden here.

THM021 proves the local coefficient-one hypothesis of THM023 and finite signed measure D_K=div K with a lower bound -kappa. The resulting base pair process includes ordinary transport, independent noises sqrt(2nu) and exact internal drift B/N. THM023 supplies its bounded Borel source potential U_N for the actual source J_t=K(x-y).(grad f_t(x)-grad f_t(y)), absolute occupation integrability, and the Haar L2 bound C rho_N. Its L2 propagator bound is at most exp[(D_u+kappa/2)(a-t)] because N>=2. Taking this larger exponent gives a constant c independent of N.

Both exact responses are THM021's compensated operators with the same mu_t. Their sum has Borel sup and Haar L2 norms at most

    C_R=2[M0 TV(D_K)+M1 ||K||1].

This is uniform in t and N. Time-continuity of mu in C1 gives operator-norm continuity on Haar L2: the difference bound is the same expression with the C1 differences of the two densities. Jointly Borel pair inputs give jointly Borel outputs by parameter integration against a fixed finite measure and integrable vector field. These properties supply the two distinct time-measurability requirements in THM024.

There is one additional representative check not implied by a generic finite measure. Off the pair diagonal, the response does not depend on the value assigned on that diagonal. In the first slot the altered integrand can be nonzero only at w=y-x. If x differs from y this is a nonzero point. Below Coulomb D_K has an L1 density, hence no atom there; at Coulomb its only atom is at zero, also not there. The K integration is absolutely continuous and assigns a singleton mass zero. The second slot has the same property. Thus a Borel kernel on the off-diagonal space can be extended arbitrarily on the diagonal, acted on by R and restricted back, with a pointwise-independent answer. Haar consistency follows from the separate translation/Fubini argument in THM021; these are not the same check.

The base flow commutes with pair exchange by pathwise uniqueness after exchanging the two Brownian motions, and the source and summed response are symmetric. All THM024 hypotheses are therefore supplied by THM021/023 and the explicitly prescribed data. Its series gives the full terminal-zero inverse Phi of G_N+R_x+R_y in the bounded Borel true-martingale sense, with source J and response included in the integrated source. It obeys

    sup_t ||Phi_t||_L2(Haar^2)^2 <= C rho_N exp[2(c+C_R)T].

The exact form is the pointwise Volterra equation, or equivalently the martingale for Phi along the auxiliary base pair process with integrated source J+R Phi. No differentiability of Phi is obtained by renaming this identity a PDE.

For iid initial density mu_0 with the same bound M0, THM015 implies

    E|sqrt(N b_N)P_N[Phi_0]|^2
       <= C M0^2 exp[2(c+C_R)T] (b_N/N) rho_N,
    b_N=min(beta_N,1), nu=1/beta_N.

The three rates are b_N/N, b_N(1+log N)/N, and b_N N^(-(d+2-s)/(s+2)). In the last case d+2-s>=4 on this theorem's range, so every displayed rate vanishes. The estimates are uniform only for beta_N>=1/nu_* when nu_*>0. Nu=0 is a separate mathematical zero-noise endpoint; it is not the reciprocal of a finite beta. There is no claim uniform over beta_N decreasing to zero. Supremum over deterministic time can stay outside the expectation; this proof does not move it inside.

This proves the analytic initial-endpoint implication for the full prescribed-data inverse directly, without comparing it to a particular local diagnostic. Actual-data regularity and compatibility with the finite-particle identity are separate from this implication.

## Actual homogeneous mean-field and backward test

Take b=0 and initial density mu_0=1. Then mu_t=1 is an explicit smooth strictly positive solution of the frozen mean-field equation for every nu>=0: K*1=0 by the odd integrable representative, the drift is zero and the Laplacian of1 is zero. This asserts existence of this reference solution; no general uniqueness theorem for weak reference solutions is needed. Thus u=0, M0=1,M1=0,D_u=0 uniformly in nu and N.

Let h be a real smooth periodic terminal test. Its Fourier coefficients decay faster than every power: integrate by parts using powers of 1-Delta to bound them by C_m(1+|k|^2)^(-m), for every integer m. In particular all sums of coefficients times any fixed polynomial power are absolutely convergent. Define

    a_k(nu)=4 pi^2 nu |k|^2+4 pi^2 c_(d,s)|k|^(s+2-d),  k nonzero,
    f_t(x)=h_hat(0)+sum_(k nonzero) h_hat(k)
                  exp[-a_k(nu)(T-t)] exp(2 pi i k.x).

All a_k are positive, with c_(d,s)>0 the frozen Riesz coefficient. For each finite nu, termwise differentiation in t and any fixed number of spatial derivatives is justified by the rapid Fourier decay; the extra factor a_k grows at most quadratically in |k|. The function is real by conjugate Fourier symmetry and f_T=h. Uniformly for t in [0,T],nu>=0,

    ||partial^alpha f_t||infty
      <=sum_(k nonzero) (2 pi)^|alpha| |k|^|alpha| |h_hat(k)|

for every nonzero multi-index alpha (with the constant coefficient included for alpha=0). Hence the required gradient/Hessian bounds are independent even of an unbounded diffusivity; the separate pair construction still restricts nu to [0,nu_*].

The actual one-body response at mu=1 is Rf(x)=integral K(w).grad f(x+w)dw. On the k-th character its multiplier is -4 pi^2|k|^2 g_hat(k), not its negative: K_hat(-k)=2 pi i k g_hat(k), and dotting it with2 pi i k gives the stated negative number. At zero frequency it vanishes. Since K is L1 and the derivative Fourier series converges absolutely, the interchange of integral and sum is justified. Thus f solves exactly

    partial_t f+nu Delta f+R f=0,  f_T=h,

with u=0 and the frozen signs. All prescribed-data assumptions of the previous section now hold for this actual homogeneous reference/test pair, uniformly for every N and beta_N>=beta_*>0. No regularity of an unknown solution is assumed for this subcase.

Consequently the full periodic probabilistic pair inverse for this actual source has the vanishing mean-field-centered initial iid endpoint with the preceding rates. This includes all critical sequences lambda_N=beta_N N^(s/d-1)->lambda in(0,infinity) in the stated exponent range, because beta_N then tends to infinity. It also includes subcritical sequences satisfying the positive lower beta bound. It does not cover every subcritical sequence, since those may have beta_N tending to zero. Neither the old energy-floor condition nor either microscopic regime is silently replaced by a norm estimate.

For the check h(x)=cos(2 pi k.x), the test is the same cosine multiplied by exp[-a_k(nu)(T-t)]. Constants remain constant and J=0, hence Phi=0 by uniqueness. These exact solvable checks test signs and terminal conditions; they are not evidence of evolved-law closure.

## First missing line

Even in this homogeneous actual-data subcase, the Borel martingale inverse is an auxiliary two-particle construction. The finite-N N-particle corrector identity contains spatial derivatives of Phi, the cubic source, lower contractions and self/cross brackets. A domain/regularization theorem must identify those terms and pass them under the interacting N-particle law. The current construction does not do so. Initial iid sampling does not remain iid at positive time, and a Haar L2 kernel bound is not a control of those interacting-law quantities. PO017 therefore advances only in its initial analytic implication; its full dynamical use, PO001 and PO004 remain open.

Exact negation of this bounded interface/corollary: some data satisfying every displayed prescribed hypothesis, or the explicit homogeneous reference/test, fail the specified composition or endpoint conclusion. No assertion outside those classes is part of this claim. A separate fresh review must check the module interface and explicit Fourier construction before promotion.
