# Round 003: exact punctured rescaling of the diffusion-retaining local model

2026-09-17. Root Astra Ultra calculation. EXACT_IDENTITY / SELF_CHECKED at submission; no existence, boundary-domain, kernel bound or singular-limit theorem is claimed. This isolates the next missing operator problem after THM-017. The calculation does not assume that the anisotropic transport-only profile has an L2 Laplacian.

Fix d>=1, 0<s<d, N>=2 and nu_N=1/beta_N>0. Put p=s+2. Consider, only on z!=0 and only for a sufficiently differentiable test function, the local terminal equation with both relative diffusion and singular internal transport:

    (partial_t + 2 nu_N Delta_z
       + (2s/N)|z|^(-s-2) z.grad_z) Phi_N
       = -s |z|^-s a(theta),      Phi_N(T,z)=0,

where theta=z/|z| and a(theta)=theta.A.theta for a fixed symmetric matrix A. This is a local Euclidean model, not the full periodic pair equation. Ordinary transport, both responses, actual backward test and force remainder are still omitted.

Set tau=T-t, y=N^(1/p)z and Phi_N(t,z)=N^(s/p)F_N(tau,y). The chain rule gives exactly

    partial_tau F_N
      = 2 chi_N Delta_y F_N
        + 2s |y|^(-s-2) y.grad_y F_N
        + s |y|^-s a(y/|y|),
    chi_N = N^(2/(s+2))/beta_N,       F_N(0,y)=0.

The drift factor is exact because N^-1 times N^((s+2)/p)=1. The Laplacian gains N^(2/p), while both Phi and the source carry N^(s/p). Thus no factor two is absorbed into chi_N. For a fixed remaining-time rescaling using ell=(2s(s+2)tau/N)^(1/p), the corresponding diffusion strength is nu_N tau/ell^2 = chi_N tau^(s/p)/(2s(s+2))^(2/p); the factor 2 remains in the diffusion operator. This last expression applies only for tau>0, not at the terminal corner by division.

Write A=A_0+(tr A/d)I. Its angular source consists of degree zero and degree two spherical modes (the degree-two component is absent in d=1). On the punctured domain a radial coefficient W_l, l=0 or 2, formally satisfies the exact separated equation

    partial_tau W_l
      = 2 chi_N [W_l''+(d-1)W_l'/r
                   -l(l+d-2)W_l/r^2]
        +2s r^(-s-1)W_l' +s r^-s.

For l=2 the angular eigenvalue is 2d. This formula is a differential identity for smooth punctured separated functions, not an assertion that a domain has been chosen or that a zero-initial solution exists in a class appropriate for the campaign. In particular, pointwise cancellation between singular drift and angular diffusion may be relevant even when the two terms separately fail a proposed norm. One cannot infer nonexistence from such separate norm failures.

At microscopic criticality lambda_N=beta_N N^(s/d-1)->lambda in (0,infinity), the exact coefficient is

    chi_N = lambda_N^-1
       N^[s(s+2-d)/(d(s+2))].

It tends to zero if d>s+2, to 1/lambda if d=s+2, and to infinity if d<s+2. These are statements only about the rescaled coefficient. They do not justify convergence of the local operator or its solutions in any of the three cases. Under full microscopic subcriticality lambda_N->0 the same exact identity holds, but no single diffusion limit follows without its rate. The old energy-floor exponent is not replaced. The logarithmic model is excluded.

The first mathematical task is to specify a closed collision-domain realization for this diffusion-retaining local operator and prove an initial-endpoint-adequate bound on its zero-terminal solution, with quantitative dependence on chi_N and both angular modes. Then the actual missing full-operator terms and evolved law still require separate comparison. The rescaling itself is not a power-counting theorem for the entire hierarchy.
