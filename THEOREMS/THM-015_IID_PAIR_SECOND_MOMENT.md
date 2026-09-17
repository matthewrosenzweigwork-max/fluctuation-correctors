# THM-015 — exact iid deleted-pair second moment and heat-cutoff orders

2026-09-17. Frozen statement for Round 003. Mathematical status PROVED_CANDIDATE, pending sealed proof comparison and hostile review. Source status self-contained; the Riesz Fourier coefficient is the frozen definition. No literature or novelty claim.

Let N>=2, let X_i be iid with probability law mu, and let Phi be real, symmetric and in L2(mu tensor mu). Use the campaign's ordered distinct-label statistic P_N=U_2/2 with denominator N^2. Define theta=mu^2(Phi), h(x)=integral Phi(x,y)mu(dy)-theta, and H(x,y)=Phi(x,y)-theta-h(x)-h(y). Then

    E P_N = -theta/(2N),
    E P_N^2 = theta^2/(4N^2) + ||h||_2^2/N^3
              + (N-1)||H||_2^2/(2N^3)
             <= (N-1)||Phi||_2^2/(2N^3).

The last constant is sharp, with equality for nonzero canonical H; at N=2 it is equality for every Phi. No evaluation at a repeated particle label is required. Changing spatial-diagonal values is immaterial when mu is atomless; with atoms, such values may have positive mu^2 mass and are part of the L2 kernel. All assertions concern initial iid samples only.

For Haar mu and Phi_epsilon(x,y)=g_epsilon(x-y), with the frozen positive-power Riesz heat multiplier and 0<s<d, both theta and h vanish. The exact squared kernel norm is the sum of squared Fourier coefficients, comparable as epsilon decreases to zero to 1 for 2s<d, log(1/epsilon) for 2s=d, and epsilon^(-(2s-d)/2) for 2s>d, with positive finite constants depending only on d,s and a fixed cutoff range. For sigma_N=min(sqrt(N beta_N),sqrt N), its exact scaled second moment is min(beta_N,1)(N-1)||g_epsilon||_2^2/(2N^2).

At epsilon_N=N^(-2/d) this tends to zero for every s<d and every positive beta_N sequence. At epsilon_N=N^(-4/d), in the range 2s>d it is comparable to min(beta_N,1) N^(4s/d-3). These are second moments for the regularized statistic; no conclusion about convergence in probability of the unregularized statistic follows solely from a variance divergence.

Exact negation: admissible data violate any displayed finite-N identity, sharp inequality or specified heat-cutoff comparison. Constants, separable/canonical kernels, N=2,3 and threshold exponents are required tests. This does not concern the actual backward corrector, the evolved interacting or Gibbs law, field tightness, or a singular dynamic comparison. The frozen old/subcritical/critical exponents and separate logarithmic normalization are unchanged. Complete proofs and their final hashes will be referenced in the canonical ledger without altering this submitted statement.
