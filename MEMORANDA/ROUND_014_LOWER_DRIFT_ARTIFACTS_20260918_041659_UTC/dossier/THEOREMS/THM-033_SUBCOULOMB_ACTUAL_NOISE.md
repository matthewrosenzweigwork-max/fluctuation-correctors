# THM-033 — bounded-rescaled-diffusion gradients and strict sub-Coulomb actual noise

2026-09-18 UTC. PROVED_CANDIDATE / ROOT SELF_CHECKED at statement freeze; fresh isolated reconstruction and hostile review required. This is an additional sufficient subrange, not replacement of the full campaign target. THM032 is reserved for the separately assigned R11 spatial module, which is not a prerequisite here.

Fix d>=3,0<s<d-2,N>=2,T finite,smooth real terminal h,L<infinity,nu_*<infinity,0<=nu<=nu_* with chi_N=nu N^(2/(s+2))<=L. Use the true homogeneous terminal-zero symmetric pair inverse with both responses and its actual Fourier test, unit Haar and zero external drift. Let p=s+2,a=s/p,theta=1-s/d. Let w_q be the fixed R7 positive periodic weight equal to r^-q near zero. Constants may depend only on the fixed displayed data, weight and kernel, not N or selected nu.

For every fixed 1<q<d/2 with q<=s+1, prove

    sup_(t,x!=y) |grad_pair Phi_t(x,y)|/w_q(x-y)
       <=C_q N^((s+1-q)/(s+2)).

Then for the actual singular particle law from iid Haar independent of its Brownian drivers, at positive nu define beta=1/nu,b_N=min(beta,1),sigma_N^2=N b_N. Prove for the genuine corrector martingale from the conditional R8 domain premise

    Q_N=2nu N b_N E integral_0^T sum_i|grad_i P_N[Phi_t](X_t)|^2dt
       <=C b_N N^a (N^-theta+nu).

P_N uses the fixed ordered deleted-pair coefficient1/(2N^2), empirical background subtraction1/N and mean-field centering. At zero noise the bracket is zero directly; no division by zero or unweighted gradient estimate uniform beyond the stated weight. The actual leading martingale has bounded scaled expected bracket and the expected integral of absolute scaled cross-variation is at most C sqrt(Q_N).

Consequently every microscopic critical sequence lambda_N=beta_N N^-theta->lambda in(0,infinity) has Q_N->0 if s(s+2)<2d. Also every bounded-chi sequence with0<s<min(2,d-2) has Q_N->0. More generally the displayed bound suffices when a<theta and N^a nu_N->0. No equality boundary, Coulomb endpoint, larger-s range, unrestricted bounded-noise sequence or full subcriticality is claimed by these corollaries.

Exact negation: a fixed admitted tuple/family violates a stated N-uniform estimate or cross bound, or a sequence in one of the asserted strict ranges has positive limsup genuine Q_N. Every new step must be proved; no claim that fixed-N C_N bounds are uniform. The source THM031 energy/Fourier construction is conditional on its own correctness at this dossier's freeze; evaluate the implication with its exact supplied statements, not any unseen current audit verdict.

No singular cubic residual estimate, full fluctuation law, higher hierarchy closure, general background, logarithmic case or transfer between law classes without proof. The old beta_N N^(2s/d-1)->0, full subcritical lambda_N->0 and critical lambda_N->positive finite remain distinct.
