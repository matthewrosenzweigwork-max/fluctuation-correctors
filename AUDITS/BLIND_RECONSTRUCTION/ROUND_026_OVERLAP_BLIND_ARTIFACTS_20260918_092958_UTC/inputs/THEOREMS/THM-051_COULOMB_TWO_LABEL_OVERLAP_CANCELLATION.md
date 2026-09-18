# THM051 — actual Coulomb two-label overlap cancellation

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO038. Use the exact actual iid-Haar coefficient-one d4,s2 singular gradient model, independent Brownian drivers, finite positive nu=1/beta, and all definitions A2,A3,B2,B3,F_N,G_N,Rcal_N,Z_m,ell_k,a_k,a_tilde,A_k,j_k from THM049. Fix a nonzero integer mode k. No current candidate proof is a certified premise. This conjunction includes the auxiliary actual-pair estimates needed for the quantitative cancellation.

(A) Let p_r be the unit-torus heat kernel, g_r=p_r*g, q_r=c integral_0^r p_u du, a_r(m)=|m|^-2 exp(-cr|m|²) for m!=0 and a_r(0)=0, c=4pi². Put M_r(t)=E sum_(m!=0)a_r(m)|Z_m(t)|². For every N>=2, every positive finite nu, every finite t>=0 and0<r<=1,

    (N/(N-1)) M_r(t)+E q_r(X1(t)-X2(t)) <= g_r(0)/(N-1)+cr,
    M_r(t)+E q_r(X1(t)-X2(t)) <= C((Nr)^-1+r).

Constants here depend only on the kernel. Choose fixed R0<1/8. There is such a C with

    P(dist(X1(t)-X2(t),0)<=R) <= C(R^4+N^-1), 0<R<=R0.

These are deterministic-time bounds, uniform in time and positive diffusivity, not pathwise minimal separation or positive-time product law.

(B) Define K_r=-grad g_r, d_(k,r)=c exp(-r ell_k),

    j_(k,r)(x,y)=K_r(x-y).(grad e_k(x)-grad e_k(y))
                  +d_(k,r)(e_k(x)+e_k(y)).

Its Haar rows are zero, and its smooth diagonal is2d_(k,r)e_k(x); no singular diagonal is assigned. For a fixed small r0<=1/2, there is C_k such that, uniformly in the same N,nu,t and0<r<=r0,

    E|j_k(X1,X2)-j_(k,r)(X1,X2)| <= C_k(r+(Nr)^-1),
    E|j_(k,r)(X1,X2)|² <= C_k(1+log(1/r)+(Nr²)^-1).

Writing the smooth Fourier coefficients of j_(k,r)(x,y)conjugate(e_k(x)) as

    b_(k,r)(m)=c[(k.m)a_r(m)-(k.(m+k))a_r(m+k)]
                   +d_(k,r)(1_(m=0)+1_(m=-k)),

one has b(0)=b(-k)=0, sum_(m!=0)b(m)=2d_(k,r), and |b(m)|<=C_k a_(r/8)(m) for nonzero m. All sums are absolutely convergent for fixed positive r. Consequently the exact current overlap is

    A_(2,r)(t)=E[j_(k,r)(X1(t),X2(t))conjugate(e_k(X1(t)))]
      =(N/(N-1)) E sum_(m!=0)b_(k,r)(m)|Z_m(t)|²
          -2d_(k,r)/(N-1).

The heat response and self subtraction are literal finite-N coefficients.

(C) For every fixed finite T>=0 and fixed0<lambda_-<=lambda_+<infinity, there is finite C depending only on k,T,kernel and these bounds such that for every N>=2 and lambda_-<=beta/sqrt(N)<=lambda_+,

    sup_(0<=t<=T)|A2(t)| <= C N^-1/2,
    sup_(0<=t<=T)|B2(t)| <= C N^-1/4 sqrt(1+logN).

All are actual expectations, with finite absolute time integrals. No L2 norm of the untruncated singular source or current/initial joint density is claimed.

(D) Put Rcal_N^(2) equal to the THM049 remainder with the A3,B3 terms omitted, and for N>=3 put

    Rcal_N^(3)=((N-1)(N-2)/(2N)) integral_0^T
       [exp(-2a_tilde(T-t))A3(t)-A_k exp(-a_tilde(T-t))B3(t)]dt.

Define it as zero at N2. Then Rcal_N=Rcal_N^(2)+Rcal_N^(3) exactly and |Rcal_N^(2)|<=C N^-1/4 sqrt(1+logN). Along every admitted critical sequence beta_N/sqrt(N)->finite positive lambda, Re Rcal_N->0 iff Re Rcal_N^(3)->0, and their positive-limsup negations are equivalent for the same fixed data. Neither limit nor a witness is asserted. The original L1 source mission is unchanged; its transfer through the separately frozen THM049 is not a new L1/L2 theorem here.

Exact negation is a violation of any(A)-(D) clause with its stated domains, coefficients, constant dependence or quantifiers. A failure of a proof, a static or altered-law example, a changing mode/time, or the openness of triple cancellation is not that negation. This gives no separate A3/B3 decay, hierarchy closure, Gaussian/path theorem, general preparation, logarithmic normalization or enlarged exponent range.
