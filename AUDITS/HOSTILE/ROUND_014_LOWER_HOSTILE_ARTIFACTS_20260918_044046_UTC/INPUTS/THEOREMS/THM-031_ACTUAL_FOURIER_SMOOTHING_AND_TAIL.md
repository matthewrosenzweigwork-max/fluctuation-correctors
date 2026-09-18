# THM-031 — actual Fourier control, smoothing, and singular-tail reduction

2026-09-18 UTC. PROVED_CANDIDATE / SELF_CHECKED at statement freeze. Exact scope: Sections2–9 of sealed TASK061 report. Prior particle/full-pair modules are explicit source premises; unsmoothed corrector assertions retain the full THM028 domain premise and the shrinking-time corollary retains the conditional integrated THM029 Haar estimate. No extra R9 timewise estimate is imported.

Fix d>=3,0<s<=d-2,N>=2,T finite,smooth real h,0<nu<=nu_*; unit Haar homogeneous gradient model, iid-Haar preparation, beta=1/nu,b_N=min(beta,1),sigma_N^2=N b_N,ordered pairs/N^2 and factor1/2. Let H_N=N^-1 sum_(i<j)g, q=1-s/d. Constants independent of N,nu except explicitly fixed smoothing.

Prove E H_N(X_t)<=0 and nu Ent(F_N(t))+E H_N(X_t)<=0 by actual smooth-to-singular passage, not singular Fisher-information formalism. Prove uniform pair energy moment. The positive Fourier heat-integral truncation in (3.1) yields H_N>=-C N^(s/d), with exact self-diagonal subtraction, and for every nonzero k

    E|eta_hat_N(t,k)|^2 <= min(1,C N^(-q)|k|^(d-s)).

Prove Ent(F_N)<=C N lambda_N and fixed-marginal total-variation convergence when lambda_N->0, with no such conclusion at criticality. Prove the full total-force occupation/labelled path estimates (4.2)–(4.3); at criticality mean-square maximal displacement is O(N^-q). No pair-force-square extraction.

For the true full Phi with both responses, prove uniform Haar L1 norm, all fixed common-translation weak derivatives in L1, smooth uniformly bounded background projection q_t(x)=integral Phi_t(x,y)dy, scalar integral Phi=0 and actual E P_N[Phi_t]=0. No concentration conclusion from this mean.

Let Psi_delta=exp(delta Delta_x)exp(delta Delta_y)Phi. Its actual expected scaled bracket functional Q_N obeys (6.6), and for r_*=(5d-s+2)/2, gamma=(d-s)/(d(5d-s+2)),delta_N=N^-gamma,

    Q_N[Psi_delta_N] <= C N^(-q/2) ->0.

The exact gradient includes the smooth missing-self term G_delta(Xi,Xi)/N. No singular diagonal trace is introduced. Prove the full target Q_N[Phi]->0 iff Q_N[Phi-Psi_delta_N]->0 and the equivalent iterated limit, with the exact four-term law expansion. The final residual estimate remains OPEN. Fixed-N Haar H1 approximation and exponential density cost do not permit interchanging limits.

For every smooth real row-centered vector H_t, C1 near0, N>=3, prove the actual initial triple covariance derivative

    d/dt E[H_t(X1,X2).H_t(X1,X3)] at0
      =-(2/N) integral_x sum_(k!=0) d_k |H_hat_0(x,k)|^2 <=0,
    d_k=4 pi^2 c_(d,s)|k|^(s+2-d).

At Coulomb this is -(2c_d/N)||H_0||2^2. No later-time sign or uniform singular Taylor remainder. Finally assess the conditional shrinking-window estimate (9.1)–(9.2); it uses only integrated Haar energy and excludes no positive fixed-horizon tail.

Exact negation: an admitted tuple/family or smooth centered probe violates a stated inequality, coefficient, limit, domain/passage or sign. Zero diffusivity gives zero brackets and deterministic energy; entropy division requires positive nu. No actual full singular-noise theorem, critical law, hierarchy closure or general-background assertion. Keep all three campaign temperature regimes distinct.
