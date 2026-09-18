# THM050 — actual Coulomb conditional response and angular regularity obstruction

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO037. This whole bounded subgate does not prove or negate THM046. Fix the coefficient-one periodic d4 Coulomb kernel g_hat(k)=|k|^-2 for nonzero k, g_hat(0)=0, c=4pi², K=-grad g. For every integer N>=2 and finite positive nu, use the actual singular gradient process dX_i=N^-1 sum_(j!=i)K(X_i-X_j)dt+sqrt(2nu)dW_i. It is defined at every collision-free deterministic start; Haar integration means the original iid Haar initial law, independent of the Brownian drivers. P_t^N denotes its Markov semigroup. The actual heat regularization is g_epsilon=p_epsilon*g, with semigroup P_t^(N,epsilon) and same-noise process X^epsilon. Every cutoff limit below precedes the N limit.

(A) For every fixed integer Fourier mode k, F(x)=N^-1 sum_i exp(2pi i k.x_i), finite T>=0, ell_k=c|k|², a=c+nu ell_k, A=exp(-aT), the exact absolutely integrable conditional-variance decomposition is

    D_N := N E|F(X_T)-A F(X_0)|² = C_N+J_N,
    C_N := N ||P_T^N F-AF||_(L2(dx^N))²,
    J_N := N E|F(X_T)-P_T^NF(X_0)|².

Both terms are nonnegative. With u_s^epsilon=P_(T-s)^(N,epsilon)F and M_k^epsilon=(sqrt(2nu)/N) sum_i integral grad e_k(X_i^epsilon)dW_i, the exact true cutoff martingale has

    d[u_s^epsilon(X_s^epsilon)] = sqrt(2nu) sum_i grad_i u_s^epsilon(X_s^epsilon).dW_i,
    d< u^epsilon(X^epsilon), conjugate(u^epsilon(X^epsilon)) >_s
        =2nu sum_i |grad_i u_s^epsilon(X_s^epsilon)|² ds,
    d< u^epsilon(X^epsilon), conjugate(M_k^epsilon) >_s
        =(2nu/N) sum_i grad_i u_s^epsilon(X_s^epsilon).conjugate(grad e_k(X_i^epsilon(s))) ds,
    J_N = lim_(epsilon down0) 2nu N integral_0^T E sum_i
             |grad_i P_(T-s)^(N,epsilon)F(X_s^epsilon)|² ds.

The corresponding backward one-body cross bracket includes the factor exp[-a(T-s)]. The limit exists as a limit of numbers without inserting an unproved singular gradient. For a critical sequence beta_N/sqrt(N)->finite positive lambda, nu_N=1/beta_N, D_N->0 if and only if both C_N,J_N->0. No such vanishing is asserted. At k0 F is constant: C_N=N(1-exp(-cT))² and J_N=0 under the displayed definition of a; no nonzero-mode physical damping statement is imported for that artificial constant-mode comparison.

(B) Fix N,nu,k as above. Let q=(z,x3,...,xN) range over any compact positive-volume set Q inside a local coordinate domain whose displayed distinct points are separated by a positive distance. Choose a small pair radius and larger local neighborhoods so x1=z+y/2,x2=z-y/2 and all remaining distinct pairs stay separated while the slow coordinates remain in those neighborhoods. For N2 q consists only of z. Put

    H_k(q)=(2/N) exp(2pi i k.z)+(1/N) sum_(j>=3) exp(2pi i k.x_j).

There exist t0>0 and finite C depending on N,nu,k,Q and the chosen neighborhoods such that for every 0<t<=t0,

    limsup_(r down0) sup_(q in Q, theta in S3)
       |P_t^N F(q,r theta)-H_k(q)
          +(4pi²/N^(3/2)) exp(2pi i k.z)(k.theta)² sqrt(t)|
       <= C t^(3/4).

Here (q,r theta) denotes the displayed original particle coordinates. No directional collision limit, entrance law or N-uniform t0/error is asserted.

(C) For k=(1,0,0,0) and f=Re F, at every fixed N>=2 and finite positive nu there is t0>0 such that for every 0<t<=t0, P_t^N f is not in W^(1,4)((T4)^N,dx^N), and

    liminf_(epsilon down0) integral_(T4)^N |grad P_t^(N,epsilon)f|^4 dx = +infinity.

The gradient is the full4N-coordinate gradient. Therefore no finite cutoff-uniform global C1 or Haar fourth-gradient estimate is possible at those fixed times, even allowing constants depending on N,nu,t. The conclusion must hold on a positive-volume set of centers and other coordinates; a single fixed slice does not suffice. This gives no failure or proof of Haar W1,2 response control, no critical fixed-time positive-limsup counterexample and no enlargement of the scientific mission.

Exact negation: an admitted finite N, positive nu and datum violates some clause of(A),(B),(C) with its stated quantifiers, coefficients, integrability and cutoff order. In(B) it requires a datum for which every finite C,t0 fails the displayed uniform limsup bound at some0<t<=t0. In(C) it requires absence of any positive time interval on which both conclusions hold for every time. Failure of a proof, lack of uniformity in N, a static example or the unresolved actual critical source is not the negation. The claim is frozen as a whole for separate fresh reconstruction and hostile review.
