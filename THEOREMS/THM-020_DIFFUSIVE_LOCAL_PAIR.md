# THM-020 — diffusion-retaining local pair inverse

2026-09-17. PROVED_CANDIDATE / SELF_CHECKED at submission. Complete proof MEMORANDA/ROUND_004_DIFFUSIVE_COMPARISON.md, SHA256 30d9f0c98413335fc56c7cc903cf23aca904bc082ec20412872145a77ff15576. Root proposed the radial/Lyapunov seed; TASK032 constructed the proof. Separate TASK033 reconstruction and a fresh hostile review are required before promotion.

For integer d>=3, 0<s<=d-2, p=s+2, N>=2, finite nu>=0,T>=0 and a constant real symmetric matrix A, the auxiliary SDE on punctured Euclidean space with diffusion sqrt(4nu) and drift (2s/N)|z|^-s-2 z has a unique global pathwise measurable realization from each nonzero point, with collision avoidance and no finite-time explosion. For J_A=s|z|^-s theta^T A theta, its absolutely integrable source potential U_A(tau,z)=E_z integral_0^tau J_A(Z_h) dh gives the unique bounded Borel terminal-zero martingale solution, in the exact deterministic-time conditional-expectation class defined in proof Section7. It satisfies

    |U_A(tau,z)| <= ||A||op F_(N,tau)(|z|),
    F_(N,tau)(r)=(N/4)[(r^(s+2)+2s(s+2)tau/N)^(2/(s+2))-r^2].

The factor one is independent of N,nu and annular radii. Killed annular potentials for nu>0 have the same bound and converge at each fixed time/point by an explicitly dominated source-integral passage. This is probabilistic killing, not an unproved continuous boundary trace. Any bounded classical solution meeting the stated stopped-Ito hypotheses is identified, but classical existence/regularity is not asserted. At nu=0, the pointwise forward absolutely-continuous characteristic class is used without a finite-radius transport outflow condition.

For the fixed smooth even cutoff supported in an embedded torus ball of radius <1/2, the separately defined symmetric diagnostic H(x,y)=chi(x-y) U_A(tau,x-y), with any specified diagonal value, satisfies the initial iid estimate for density bounded by M and b_N=min(beta_N,1), sigma_N=sqrt(N b_N):

    sup_(tau in [0,T]) E|sigma_N P_N[H]|^2 <= C_T b_N *
      N^-1                    if 2s<d,
      (1+log N)/N              if 2s=d,
      N^(-(d+2-s)/(s+2))       if 2s>d.

The constant is independent of N, finite nu>=0, beta_N>0 and tau. A sequence nu=1/beta_N is allowed. Mean-field centering and N^2 denominator are retained; the density bound enters only once. Supremum is outside the expectation. No two-sided norm order for nu>0, path supremum, evolved-law estimate, classical regularity, full periodic equation or hierarchy closure is asserted. Ordinary transport, both nonlocal responses, actual time-dependent source/test, periodic force and diagnostic annular forcing remain omitted.

Exact negation: an admissible tuple or member of one of the declared classes violates any displayed bound/existence/uniqueness or convergence assertion. All source and domain hypotheses are part of the claim; d<s+2 is outside its range. Later audit verdicts live in canonical state; submitted bytes remain fixed.
