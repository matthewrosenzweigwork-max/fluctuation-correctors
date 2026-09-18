# THM-030 — actual entropy, clipped noise, and exact tail reduction

2026-09-18 UTC. PROVED_CANDIDATE / SELF_CHECKED at statement freeze. The submitted claim is exactly Sections2–8 of the sealed TASK060 report; the full singular bracket remains OPEN. Imported THM028 domain and THM029 Haar energy are explicit conditional premises in this dossier, not independently proved here.

Fix the homogeneous unit-Haar model d>=3,0<s<=d-2,N>=2,T finite,smooth real h and 0<nu<=nu_*<infinity. Actual singular particles start iid Haar with independent Brownian motions; beta=1/nu,b_N=min(beta,1),sigma_N^2=N b_N. The potential is U_N=N^-1 sum_(i<j)g(Xi-Xj), with frozen zero-mean positive-Fourier g, K=-grad g. Put p=s+2,a=s/p. All claimed constants are independent of N and chosen nu unless explicitly named C_(N,q).

Prove the smooth-and-singular lower bound U_N^epsilon>=-C0 N^a and actual free energy nu Ent(F_N(t))+E U_N(X_t)<=0. Prove E g(X1-X2)<=0 and uniform actual pair w_s moment. Actual law is exchangeable with one-body Haar. For 2<=k<=N prove Ent(F_k)<=(k-1)/(N-1) Ent(F_N), with Ent(F_N)<=C0 N^a/nu and the explicit bounded-test estimates (4.3)–(4.4).

For the genuine full inverse Phi, let G=grad_x Phi,A=integral_y G,H=G-A. Radially clip G at L to G^L and re-center its own row A^L,H^L. Define v_i^L=N^-2[sum_(j!=i)H^L(Xi,Xj)-A^L(Xi)] and the actual true martingale M^L=sqrt(2nu)sum_i integral v_i^L dWi. This vector field need not be a new potential gradient. Its scaled expected bracket satisfies

    Q_N^L <= C_E b_N N^(-2/p) +16T sqrt(2C0) b_N sqrt(nu) L^2 N^(-1/p).

With L_N=N^(1/(4p)), Q_N^L<=C_E b_N N^(-2/p)+C_*N^(-1/(2p))->0. More generally the exact uniform or sequence-specific threshold conditions in (5.9)/(5.11) suffice.

Define the tail by G^>=G-G^L and its own row means. Its actual scaled expected bracket T_N(L) satisfies |sqrt(Q_N)-sqrt(T_N(L))|<=sqrt(Q_N^L). Hence full Q_N->0 iff T_N(L_N)->0. Retain all four contractions and their coefficients in (7.1), with no triple object at N=2. This is a necessary-and-sufficient reduction, not proof of the tail. The Haar tail bound and finite-N density comparison retain their explicit scope. For s>2 also assess (8.3), retaining C_(N,q) and its unproved growth criterion; for s<=2 assess the stated limitation of this particular moment argument.

Exact negation: an admitted tuple/family violates one stated uniform inequality, finite-N identity, regularization passage or equivalence. Zero-noise functionals are separately zero; constant h and T=0 are included. No unweighted total-variation convergence at criticality, actual singular-tail smallness, evolved residual or completed fluctuation theorem. The three campaign temperature conditions stay distinct.
