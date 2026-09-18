# THM049 — exact signed-correlation criterion for the actual critical source

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO036. Bounded companion of THM048, not a replacement or resolution of THM046. Same exact actual d4,s2 iid-Haar gradient model, fixed finite T, beta_N N^-1/2 tending to finite positive lambda, positive finite nu_N, Haar/Fourier conventions, literal deleted P_N and backgrounds. THM048 is a new unproved companion and may be used only if reconstructed in the same fresh audit or independently accepted.

For each fixed nonzero k in Z4 put e_k(x)=exp(2pi i k.x), Z_k(t)=eta_N(t)[e_k], ell_k=c|k|², a_k=c+nu_N ell_k, a_tilde=a_k-c/N, A_k=exp(-a_k T), c=4pi². Define

    j_k(x,y)=K(x-y).(grad e_k(x)-grad e_k(y))+c(e_k(x)+e_k(y)),
    U_N^k(t)=(2N²)^-1 sum_(i!=j) j_k(X_i(t),X_j(t)).

Define actual current and current/initial expectations

    A2(t)=E[j_k(X1(t),X2(t)) conjugate(e_k(X1(t)))],
    A3(t)=E[j_k(X1(t),X2(t)) conjugate(e_k(X3(t)))],
    B2(t)=E[j_k(X1(t),X2(t)) conjugate(e_k(X1(0)))],
    B3(t)=E[j_k(X1(t),X2(t)) conjugate(e_k(X3(0)))].

At N2 omit the three-label terms rather than assigning a nonexistent third particle. Set

    F_N(t)=(N-1)A2(t)/N +(N-1)(N-2)A3(t)/(2N),
    G_N(t)=(N-1)B2(t)/N +(N-1)(N-2)B3(t)/(2N),
    Rcal_N(k,T)=integral_0^T [exp(-2a_tilde(T-t))F_N(t)
                  -exp(-a_k T)exp(-a_tilde(T-t))G_N(t)]dt,
    Dcal_N(k,T)=N E|Z_k(T)-A_k Z_k(0)|².

The entire frozen conjunction is:

(A) All these actual finite-N time integrals are absolutely integrable. The exact modal identity is

    Dcal_N(k,T)=(exp(-a_tilde T)-exp(-a_k T))²
       +(nu_N ell_k/a_tilde)(1-exp(-2a_tilde T)) +2 Re Rcal_N(k,T).

Both explicit terms are nonnegative and, for each fixed k,T on the critical tail, respectively O(N^-2) and O_k(N^-1/2). In particular the negative part of Re Rcal_N is o(1). No equal-time or two-time product law is assumed; the latter need not possess a smooth joint density.

(B) For every admitted critical sequence and fixed T, the assertion of THM046 for every fixed smooth real h is equivalent to

    Re Rcal_N(k,T)->0 for every fixed nonzero k.

The equivalence is with the original expected absolute time-integrated source, not only a stronger sufficient L2 bound. It includes T0 and constant tests, arbitrary convergence rate of lambda_N and finite initial segment with min(beta_N,1)!=1. The mode-to-smooth passage is justified with an N-uniform polynomial L1 mode majorant for this same original source, not an unproved uniform L2 summability estimate.

(C) The exact full-target negation is correspondingly equivalent to existence of admitted fixed k!=0,T,lambda and critical sequence with limsup Re Rcal_N(k,T)>0. Such a witness yields a fixed real cosine or sine test with positive original-source L1 limsup; absence of a limit for a stronger unrelated estimate is not a witness. No vanishing or positive-limsup witness is asserted here.

Exact negation of THM049 is an admitted violation of(A),(B),or(C), including a coefficient, integrability, rate, quantifier or equivalence. The original cancellation Re Rcal_N->0 stays OPEN. No separate decay of F_N/G_N or their four summands, N-dependent test/time, altered preparation, static obstruction, Gaussian/process result, hierarchy truncation, logarithmic substitution or broader singularity range is claimed.
