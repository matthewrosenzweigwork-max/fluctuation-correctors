# THM052 — killed attractive duality for actual Coulomb dynamics

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO039. New root construction; no independent status. Fix N>=2 and finite nu>0 in the coefficient-one d4 periodic Coulomb model, unit Haar, g_hat(k)=|k|^-2 for k!=0, g_hat(0)=0. Put H_N=N^-1 sum_(i<j)g(x_i-x_j), Omega=collision-free configurations, c=4pi² and kappa=c(N-1). Let P_t be the actual conservative repulsive semigroup with generator L=nu Delta-grad H_N.grad on Omega. Define the auxiliary attractive diffusion dY=+grad H_N(Y)dt+sqrt(2nu)dW, uniquely up to its maximal lifetime zeta in Omega, and killed thereafter. Its sub-Markov semigroup is Q_t f(x)=E_x[f(Y_t)1_(t<zeta)]. The auxiliary law is explicit and is never substituted silently for the original law.

(A) For all t>=0 and bounded measurable nonnegative f,h on Omega,

    integral f P_t h dx = exp(kappa t) integral h Q_t f dx.

The identity extends to bounded signed or complex functions by linearity. Haar gives the deleted collision set measure zero. The actual law at time t from iid Haar has density exp(kappa t)Q_t1 with respect to dx^N, bounded by exp(kappa t). The killed attractive process from iid Haar satisfies

    E_iid[f(Y_t)1_(t<zeta)] = exp(-kappa t) integral f dx,
    P_iid(zeta>t)=exp(-kappa t).

Thus its lifetime is exactly exponential with rate kappa, and conditional on survival to any fixed time its current configuration is exactly product Haar. The lifetime/rate assertion is for this precise initial law; it need not hold for each deterministic start.

(B) For every finite T>=0 the actual continuous path law (X_t:0<=t<=T) from iid Haar equals the law (Y_(T-t):0<=t<=T) of the attractive process from iid Haar conditional on zeta>T. Equality is as probability measures on C([0,T],(T4)^N), with the ordinary uniform topology. All finite-dimensional products and the full path law, not only endpoint marginals, are included. At T0 the statement is the initial Haar identity. This does not make the original positive-time law product Haar.

(C) In particular for every bounded complex configuration observable F and A in C,

    E_rep |F(X_T)-A F(X_0)|²
      = E_att[|F(Y_0)-A F(Y_T)|² | zeta>T].

For F=N^-1 sum_i exp(2pi i k.x_i), fixed nonzero k, A=exp[-(c+nu c|k|²)T], multiplying by N gives exactly the THM049 modal defect. Along a critical sequence nu_N=1/beta_N, beta_N/sqrt(N)->finite positive lambda, its vanishing is equivalent to vanishing of this same N-scaled conditional attractive defect; positive-limsup criteria also agree exactly. No limit or witness is proved, and the rare survival probability exp[-c(N-1)T] cannot be discarded or treated as a uniform conditioning bound.

Exact negation is any admitted N,nu,t or bounded datum violating(A), a path-law violation in(B), or a violation of the exact identity/criterion(C). The required construction includes the killed auxiliary lifetime, actual conservative original domain, passage from bounded collision-free domains, every drift/noise/divergence factor, and full path identification. A formal adjoint expression without those passages is not a proof. No L2 gradient regularity, Gaussian/hierarchy theorem, general initial preparation, or altered scientific mission is asserted.
