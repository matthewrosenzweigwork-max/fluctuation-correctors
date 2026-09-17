# THM-008 — smooth finite-N duality and pair generator

- Version: frozen candidate 1.0, 2026-09-17 UTC.
- Model and all quantifiers: TASKS/ACTIVE/ROUND_001_MODEL.md, every finite N>=2, beta_N>0, smooth even g, smooth deterministic symmetric Phi and smooth positive reference on a fixed horizon. Law arbitrary for the pathwise assertion.
- Mathematical status: EXACT_IDENTITY candidate construction; proof integration and independent comparison pending.
- Audit status: SELF_CHECKED, not yet independently promoted.
- Source status: proved from the frozen SDE; no imported manuscript theorem.
- Scope exclusion: no cutoff-uniform estimate, fluctuation CLT, singular Ito passage, or all-order closure claimed.

Write nu=1/beta_N, K=-grad g, u=-grad V+K*mu and

    A f = u.grad f + nu Delta f,
    R f(y) = integral K(x-y).grad f(x) mu(dx), L=A+R,
    J_f(x,y)=(grad f(x)-grad f(y)).K(x-y).

Then d rho(f) = rho((partial_t+L)f)dt + U_2[J_f]dt/2 + dM_f,
where dM_f=sqrt(2nu)N^(-1)sum_i grad f(x_i).dW_i.

Define the full pair operator L_2=A_x+A_y+R_x+R_y, where

    R_x Phi(x,y)=integral K(z-x).grad_z Phi(z,y) mu(dz),
    R_y Phi(x,y)=integral K(z-y).grad_z Phi(x,z) mu(dz).

Define B Phi=K(x-y).(grad_x-grad_y)Phi,
and C Phi=Sym_3[K(x-z).grad_x Phi(x,y)] (average over all permutations).
With P=U_2/2, the candidate exact identity is

    dP[Phi] = {P[(partial_t+L_2+B/N)Phi] + U_3[C Phi]
                + rho((B Phi)_mu)/N + mu^2(B Phi)/(2N)}dt + dM_Phi.

For H_i[Phi]=N^(-1)sum_{j!=i} grad_x Phi(x_i,x_j)
                - integral grad_x Phi(x_i,y)mu(dy),

    dM_Phi=sqrt(2nu)N^(-1)sum_i H_i[Phi].dW_i,
    d[M_Phi,M_Psi]/dt=2nu N^(-2)sum_i H_i[Phi].H_i[Psi],
    d[M_f,M_Phi]/dt=2nu N^(-2)sum_i grad f(x_i).H_i[Phi].

The full-product Ito trace cancels with differentiation of the subtracted empirical diagonal; this cancellation must be proved before omitting the trace. The corrector martingale itself remains.

Exact negation: there exists one admissible finite N, beta, smooth g, reference, Phi and configuration where any of the displayed drift or bracket equalities fails.

Acceptance: complete ordered-sum proof, independent BBGKY/pathwise reconstruction, finite-N checks including N=2,3, constant/separable kernels, and separate hostile review. Current independent root verifier performs 90 exact rational Laurent-polynomial checks for a fixed one-mode smooth torus model; it supports the formulas but is not a proof of all quantifiers.
