# THM054 — actual fourth moments and reduction to a force tail

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO041. New TASK119 construction; no independent status. Use the actual coefficient-one d4,s2 periodic repulsive Coulomb particles, iid Haar independent of noise, unit torus, e_m(x)=exp(2pi i m.x), c=4pi², g_hat(m)=|m|^-2 for m!=0, g_hat(0)=0, K=-grad g, drift N^-1 sum_(j!=i)K and noise sqrt(2nu), nu=1/beta>0. Fix a finite T and positive finite critical window lambda_-<=beta/sqrt(N)<=lambda_+, every N>=2. Constants below are uniform throughout that window with their declared dependencies. No source law, centering or physical dynamics is clipped.

Put Z_m(t)=N^-1 sum_i e_m(X_i(t)), ell_m=c|m|², a_m=c+nu ell_m and w_m=(1+|m|)^10. Q^nu is the original homogeneous one-body backward response: Q_t^nu e_m=exp(-a_m t)e_m for m!=0 and Q_t^nu1=1. P_N retains both Haar backgrounds and the deleted pair diagonal with ordered denominator 2N². Define S_N,m(t)=sqrt(N) integral_0^t P_N[J^(Q_(t-s)^nu e_m)](X(s))ds and D_N,m(t)=sqrt(N)[Z_m(t)-exp(-a_m t)Z_m(0)].

(A) There is C depending only on T, the fixed window and kernel such that, for every nonzero integer m,

    sup_(0<=t<=T) E[|S_N,m(t)|^4+|D_N,m(t)|^4+|sqrt(N)Z_m(t)|^4] <= C w_m^4.

This is a supremum of expectations, not an expected time supremum, fourth-power uniform integrability, gradient bound, instantaneous source square or critical decay.

The following auxiliary exact identity is included in the conjunction. For every compact abelian group with Haar probability, every bounded real even zero-mean translation kernel h, iid Haar Y_i and H^h=N^-1 sum_(i<j)h(Y_i-Y_j), set mu2=int h², mu4=int h^4, tau=int h²(h*h), chi=int(h*h)². Then

    N^4 E(H^h)^4 = binom(N,2)mu4
       +18binom(N,3)mu2²+36binom(N,3)tau
       +18binom(N,4)mu2²+72binom(N,4)chi.

Binomial terms are zero when too few labels exist. No untruncated Coulomb energy moment is asserted. The actual source/energy martingale cross term must be retained; a time-zero clipping event may enter a martingale integrand, a future event may not be substituted.

(B) Fix nonzero k. Let g_r=p_r*g, K_r=-grad g_r, d_r=c exp(-r ell_k), and j_k(x,y)=K(x-y).(grad e_k(x)-grad e_k(y))+c(e_k(x)+e_k(y)) on distinct points. Its smooth observable is j_k,r=K_r.(grad e_k(x)-grad e_k(y))+d_r(e_k(x)+e_k(y)). For N>=3 set A3r(t)=E[j_k,r(X1(t),X2(t)) conjugate(e_k(X3(t)))], B3r(t)=E[j_k,r(X1(t),X2(t)) conjugate(e_k(X3(0)))]. Use analogous A3,B3 for j_k. Write p_N=(N-1)(N-2)/(2N), a=a_k, a_tilde=a-c/N, A=exp(-aT), u_t=exp[-a_tilde(T-t)], and R_N,r^(3)=p_N int_0^T [u_t² A3r(t)-A u_t B3r(t)]dt. All triple expressions are zero for N=2, with no nonexistent label assigned. Keep the actual singular process and these exact two weights. For some fixed sufficiently small r0>0 and every 0<r<=r0,

    |R_N,r^(3)| <= C_(k,T,window) [N^-1/2 r^-11
        +N^-1/4 sqrt(1+log(1/r)+1/(Nr²))].

The constant is independent of N,beta,r. Consequently r_N=r_*N^-1/24, any fixed 0<r_*<=r0, gives |R_N,r_N^(3)|<=C N^-1/24. More generally r=r_*N^-delta tends to zero in this bound for every fixed 0<delta<1/22. No optimal exponent is claimed.

The complete finite-N Fourier/deletion identities are included. For a_r(m)=|m|^-2 exp(-cr|m|²), a_r(0)=0,

    j_k,r(x,y)=sum_m b_r(m)e_(k+m)(x)e_(-m)(y),
    b_r(m)=c[(k.m)a_r(m)-(k.(m+k))a_r(m+k)]
                  +d_r(1_(m=0)+1_(m=-k)).

Rows vanish; b_r(0)=b_r(-k)=0, b_r(m)=b_r(-k-m), sum_m b_r(m)=2d_r, and |b_r(m)|<=C_k |m|^-2 exp(-cr|m|²/8) for nonzero m. The weighted absolute sum sum|b_r(m)|w_(k+m)w_m<=C_k r^-11. With U_r=(2N²)^-1 sum_(i!=j)j_k,r(X_i,X_j), exactly U_r=(1/2)sum_m b_r(m)Z_(k+m)Z_(-m)-d_r Z_k/N. Both current and mixed covariances satisfy N E[U_r conjugate(Z_k(current or initial))]=(N-1)A2r_or_B2r/N+p_N A3r_or_B3r, where the overlapping phase uses label1. In particular A2r=N/(N-1) sum_(m!=0)b_r(m)E|Z_m(t)|²-2d_r/(N-1). Smooth diagonal terms cannot be discarded.

(C) Let H_N,r^(3) be the same triple expression tested only with J_k^>r(x,y)=(K-K_r)(x-y).(grad e_k(x)-grad e_k(y)), without silently recentering that raw force tail. Put C_t=E[e_k(X1(t)) conjugate(e_k(X2(t)))], O_t=E[e_k(X1(t)) conjugate(e_k(X2(0)))], and S_t=E[e_k(X1(t)) conjugate(e_k(X1(0)))]. Exact same-label deletion gives C_t=[N E|Z_k(t)|²-1]/(N-1), O_t=[N E(Z_k(t)conjugate(Z_k(0)))-S_t]/(N-1). The full unsmoothed triple expression R_N^(3) obeys

    R_N^(3)=R_N,r^(3)+H_N,r^(3)+B_N,r,
    B_N,r=2p_N(c-d_r)int_0^T[u_t² C_t-A u_t O_t]dt,
    |B_N,r|<=C_(k,T,window) r.

At r_N=r_*N^-1/24, |R_N^(3)-H_N,r_N^(3)|<=C_(k,T,window,r_*)N^-1/24. Their same-fixed-data zero-limit and positive-limsup criteria for the real parts are equivalent. Combining the exact accepted THM048/049/051 bridge, this is the original THM046 source criterion. No force-tail cancellation or admitted witness is proved.

The entire new conjunction includes A-C, the auxiliary graph identity, stated finite-N identities, bounds and quantifiers; the constructor's ancillary assertions must also be reviewed. Exact negation is an admitted datum violating an equality or, at fixed declared parameters, failure of existence of a finite constant controlling all quantified variables, or a mismatch of the stated limiting criteria. A failure of the open force-tail limit does not negate this reduction. Physical smoothing is removed at fixed N first; r_N smooths only an observable of the actual process. Original old beta_N condition, microscopic beta_N/sqrt(N)->0 and critical positive limit stay distinct. No larger Gaussian/hierarchy conclusion follows.
