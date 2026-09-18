# THM-021 — finite-measure singular response and smooth pair propagation

2026-09-17. PROVED_CANDIDATE / SELF_CHECKED at submission. Complete proof MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md, SHA256135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be. Separate fresh hostile TASK038 and a fresh statement-only reconstruction are required; neither is inferred from root reading. The proof's internal SELF_CONTAINED source label describes a reproof, not a new canonical source-status category.

Freeze unit Haar torus, e^(2pi i k.x), d>=3,0<s<=d-2, zero-mean positive Riesz g_s with Fourier coefficient c_ds |k|^(s-d), c_ds=pi^(s-d/2)Gamma((d-s)/2)/Gamma(s/2), and K=-grad g_s. Let mu be a C1 probability density with M0=||mu||infty and M1=||grad mu||infty; no positive lower bound. D=div K is a finite signed measure, K belongs to L1, and

    D=s(d-2-s) g_(s+2) dx,                 0<s<d-2,
    D=c_d(delta_0-dx), c_d=(d-2)|S^(d-1)|, s=d-2.

D has total mass0 and a finite lower bound D>=-kappa dx; at Coulomb ||D||TV=2c_d and kappa=c_d. Exact periodic compensation uses the full frozen Fourier kernel, not just its local singularity.

The formula

    R_x Phi(x,y)=-integral mu(x+w) Phi(x+w,y) D(dw)
                -integral K(w).grad mu(x+w) Phi(x+w,y) dw

and its second-slot analog define bounded operators on actual bounded Borel functions with pointwise sup norm, and unique bounded extensions from smooth inputs to Haar L2. They induce bounded Haar-Linfty quotient operators. Each norm is at most M0||D||TV+M1||K||1; their sum is at most C_R=2(M0||D||TV+M1||K||1), and preserves pair symmetry. The atom multiplies Phi(x,y), rather than taking a pair-diagonal trace. The formula agrees pointwise with the original integrated-gradient response on smooth Phi. Both responses kill constants.

For heat mollification of the interaction with the SAME mu, R_x,epsilon=P_epsilon^x R_x and similarly in y. Below Coulomb convergence is in operator norm on Haar L2 and bounded Borel sup space. At Coulomb it is strong in Haar L2, uniformly over backgrounds with common M0,M1 when applied to each fixed input, and uniformly over a compact continuous-in-time L2 input family. No uniformity on the L2 unit ball is claimed: for mu=1, the two-response difference has operator norm exactly2c_d at every positive epsilon. Sup-norm convergence for every bounded Borel input is false, with the pair-diagonal indicator a witness. Different approximations of mu require separate stated C1 control.

For each smooth cutoff, u_t continuous in time and smooth in space, with all spatial derivatives bounded on the finite time interval for each fixed parameter tuple and div u_t>=-a(t), a>=0 integrable, the pair Markov generator nu(Delta_x+Delta_y)+u_t(x).grad_x+u_t(y).grad_y+(1/N)K_epsilon(x-y).(grad_x-grad_y) has Haar-L2 propagator norm at most exp(integral[a+ kappa/N]). This is uniform in epsilon>0,N>=2,nu>=0 when the displayed lower bound is uniform. The exact pair divergence has2D_epsilon/N and the norm exponent has kappa/N. Under continuous C1 mu_t and prescribed L1_t L2 forcing, adding both bounded responses yields the corresponding unique L2 mild solution with exponent a+kappa/N+C_R(t). This is a SMOOTH-CUTOFF result, not a singular-flow or corrector-limit claim.

Exact negation: admissible data violate any of the declared distribution, operator, convergence, counterexample or smooth propagation/mild-solution assertions. Weighted L2(mu^2), a diagonal trace of an arbitrary Haar-L2 class, singular semigroup existence/limit, actual forcing integrability, evolved-law transfer and fluctuation closure are excluded. The one-way norm conversion is ||Phi||_L2(mu^2)<=M0||Phi||_L2(Haar^2). Later dispositions belong in canonical state; submitted bytes remain fixed.
