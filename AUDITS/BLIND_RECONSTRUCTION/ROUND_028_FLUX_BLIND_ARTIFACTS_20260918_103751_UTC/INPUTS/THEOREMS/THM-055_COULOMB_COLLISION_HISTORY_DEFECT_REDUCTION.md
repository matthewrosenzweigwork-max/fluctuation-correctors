# THM055 — quantitative collision-history reduction of the actual modal defect

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO042. New TASK120 construction; no independent status. Use the exact coefficient-one d4 periodic model and minimal killed attractive process Y of THM052, from iid Haar independent of noise. N>=2, nu>0 finite, c=4pi², kappa=c(N-1), H=N^-1 sum_(i<j)g, drift +grad H, covariance 2nu. The original conservative repulsive process X retains drift -grad H. Fix nonzero k, ell=c|k|², F=N^-1 sum_i e_k(x_i), a=c+nu ell, A_T=exp(-aT), b=c(1-1/N)-nu ell. Every horizon T>=0 is finite. The exact original defect is D_N(k,T)=N E_rep|F(X_T)-A_TF(X0)|²=N E_att[|F(Y0)-A_TF(YT)|² | zeta>T].

(A) The actual attractive terminal configuration Z=Y_(zeta-) exists almost surely and is a collision configuration. With gamma_ij the probability law fusing exactly the coordinates i,j at a Haar common point and giving the other coordinates independent Haar values, Gamma_N=binom(N,2)^-1 sum_(i<j)gamma_ij, the full joint law is

    P(zeta in dt,Z in dz)=kappa exp(-kappa t)dt Gamma_N(dz).

Almost surely exactly one unordered pair collides; it is uniform and independent of lifetime. The time is independent of the terminal configuration, without independence from the initial state. For nonzero k, Haar[F]=Gamma_N[F]=0, Haar[|F|²]=1/N and Gamma_N[|F|²]=(N+2)/N². All bounded Borel tests, extended nonnegative tests and N=2 are included. The separate THM053 first-power full-drift identity and marked version are audited in the joint gate, with their own exact scope.

(B) Let j(x,y)=K(x-y).(grad e_k(x)-grad e_k(y))+c(e_k(x)+e_k(y)), with both zero Haar rows, and U=(2N²)^-1 sum_(i!=j)j. The original source is exactly P_N[J]=U+cF/N. Define a fixed explicit tail constant as follows. On |z|<=r0=1/4 write g(z)=|z|^-2+H_reg(z). Set M_H=sup|grad H_reg| there, M_K=sup_(dist(z,0)>=r0)|K(z)|, alpha=2ell, B0=ell M_H r0+2c, D0=4pi|k| M_K+2c, L0=max(1,2B0,2D0,2alpha/r0²), and C_k=max(L0²,2pi²alpha²). Then Haar-pair(|j|>L)<=C_k L^-2 for every L>=1. Canonically double-center j_L=j min(1,L/|j|), obtaining v_L. Its norm satisfies ||v_L||2<=||j_L||2, ||j-j_L||1<=C_k/L, ||j_L||2²<=1+2C_k log L, and ||j-v_L||1<=4||j-j_L||1. Under iid Haar,

    E|(2N²)^-1 sum_(i!=j)v_L(X_i,X_j)|²
       =(N-1)||v_L||2²/(2N³),
    E|U| <= u_N,k := sqrt[(N-1)(1+2C_k log N)/(2N³)]
                         +2C_k(N-1)/N².

Thus u_N,k=O_k(sqrt(1+log N)/N). This clips an auxiliary iid estimate only, not the dynamics or target; no untruncated instantaneous variance is asserted.

(C) The genuine stopped observable identity has L^+F=bF-U and

    F(Z)-F(Y0)=I+M,
    I=int_0^zeta(bF(Y_s)-U(Y_s))ds,
    M=sqrt(2nu)/N sum_i int_0^zeta grad e_k(Y_i(s)).dW_i(s),
    E|M|²=2nu ell/(N kappa).

M is a true L2 stopped martingale before any survival conditioning. Its conjugate cross bracket for modes k,l is (2nu c/N)(k.l)F_(k-l)1_(s<zeta)ds and its unconjugated bracket is -(2nu c/N)(k.l)F_(k+l)1_(s<zeta)ds. No drift/noise cross term is dropped. Set

    epsilon_N,k,nu=(4N/kappa)(|b|/sqrt(N)+u_N,k)+2nu ell/kappa.

Then N E|F(Z)-F(Y0)|²<=epsilon_N,k,nu, and for every fixed T>=0,

    N E[|F(Z)-F(YT)|² | zeta>T]<=epsilon_N,k,nu.

The latter transfers the entire future segment using the exact survivor Haar law and Markov property; it does not condition a prior martingale on a future event. For every fixed nu_*<infinity, uniformly in 0<nu<=nu_*, epsilon=O_(k,nu_*)(N^-1/2+sqrt(1+log N)/N). Also |N E[F(Y0)conjugate(F(Z))]-1|<=sqrt(epsilon). In particular typical initial and terminal marks remain strongly correlated at fluctuation scale.

(D) Define the bounded nonnegative measurable lifetime profile, up to Lebesgue-null sets,

    R_N,k,nu(t)=N E[|F(Y0)-exp(-at)F(Z)|² | zeta=t],
    B_N(k,T)=int_0^infinity kappa exp(-kappa u)R_N,k,nu(T+u)du
       =exp(kappa T)int_T^infinity kappa exp(-kappa t)R_N,k,nu(t)dt.

Then B_N is exactly N E[|F(Y0)-exp(-a zeta)F(Z)|² | zeta>T]. No initial/terminal independence is assumed. The response-change square has the exact expectation

    N E[|(A_T-exp(-a zeta))F(Z)|² | zeta>T]
       =A_T²(1+2/N)2a²/[(kappa+a)(kappa+2a)].

Consequently

    |sqrt(D_N(k,T))-sqrt(B_N(k,T))|
      <= A_T[sqrt(epsilon_N,k,nu)
          +sqrt((1+2/N)2a²/((kappa+a)(kappa+2a)))].

For fixed k and 0<nu<=nu_* this bound is O_(k,nu_*)(N^-1/4), uniformly over all finite T>=0; its response-change term is O(N^-1). T=0 gives D_N=0 and the resulting bound on B_N(k,0). Along every beta_N/sqrt(N)->fixed lambda in (0,infinity), nu_N=1/beta_N, and fixed k,T, vanishing of D_N is equivalent to vanishing of B_N; their positive-limsup alternatives are equivalent. Via accepted THM048/049, this is precisely the original fixed-smooth-real-test THM046 criterion and its admitted fixed cosine/sine witness criterion. Neither limiting alternative is decided here.

(E) The intermediate defect retaining response time T is exactly v_N(T)+A_T²(1+2/N)-2A_T Re q_N(T), where v_N=N E[|F(Y0)|²|zeta>T] and q_N=N E[F(Y0)conjugate(F(Z))|zeta>T]. It is at least [sqrt(v_N)-A_T sqrt(1+2/N)]² and differs from D_N in square-root norm by at most A_T sqrt(epsilon). Conditioning additionally on collision pair {1,2} preserves these symmetric quantities. The five initial/collision-label classes in q_N have respective multiplicities 4,2(N-2),2(N-2),N-2,(N-2)(N-3), before division by N: fused/common, outside/common, fused/outside, same outside, distinct outside. Absent classes at N=2,3 are omitted. Their products remain two-time marked correlations. The analogous almost-everywhere lifetime expression is R(t)=v_N(t)+(1+2/N)exp(-2at)-2exp(-at)Re q_N(t). The collision fusion law does not determine the initial marks.

The entire conjunction A-E and all ancillary constructor assertions require review. Exact negation is an admitted finite datum violating an identity or bound with these explicit constants, failure of a stated uniformly quantified bound, or failure of a limiting equivalence. It is distinct from failure of the still-open boundary-profile decay. Keep the exact exp[kappa T] normalizer and all original law/preparation/centering/scaling. The old beta_N->0, full microscopic beta_N/sqrt(N)->0 and critical positive limit are separate. There is no point-start exponential law, force-square bound, original positive-time Haar law, moving external time/mode or Gaussian/hierarchy closure.
