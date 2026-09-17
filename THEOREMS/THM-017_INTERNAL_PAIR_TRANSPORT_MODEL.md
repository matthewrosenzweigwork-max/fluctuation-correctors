# THM-017 — exact internal-pair transport model and iid endpoint

2026-09-17. PROVED_CANDIDATE / SELF_CHECKED at submission. Proof: MEMORANDA/ROUND_003_PAIR_TRANSPORT_MODEL.md, SHA-256 9cfe0d7b7fb970ce74e14f4d25b784437debeefac3e9d8a8e1ab47152514ef5d. Root proposed the model and the separate TASK-025 worker constructed the complete proof. A separate hostile verdict is required.

For fixed integer d>=1, 0<s<d, N>=2, finite T>=0 and fixed real symmetric matrix A, the punctured Euclidean zero-diffusion equation

    (partial_t + (2s/N)|z|^(-s-2) z.grad_z) Phi_N
       = -s |z|^-s (theta.A.theta),        Phi_N(T,z)=0

has a unique solution in the forward absolutely-continuous characteristic class stated in Section 1 of the proof. For r=|z|>0, theta=z/r and tau=T-t it is

    Phi_N = (N/4)(theta.A.theta)
             [(r^(s+2)+2s(s+2)tau/N)^(2/(s+2))-r^2].

The proof gives explicit near/far bounds, local L2 norm and two-sided asymptotic powers, collision and terminal behavior, and the angular norm for every symmetric A. The radius is ell=(2s(s+2)tau/N)^(1/(s+2)). A nonscalar A has direction-dependent collision limits at positive tau; no smooth coincidence extension is asserted.

For the fixed radial cutoff and periodic diagnostic H_(N,tau)(x,y) defined in Section 6, iid initial law with uniformly bounded density, b_N=min(beta_N,1), and sigma_N=sqrt(N b_N), uniformly over deterministic tau in [0,T],

    E|sigma_N P_N[H_(N,tau)]|^2 <= C_T b_N times
       N^-1                          when 2s<d,
       (1+log N)/N                   when 2s=d,
       N^(-(d+2-s)/(s+2))             when 2s>d.

The supremum is outside the expectation. The full campaign mean-field centering and N^2 denominator are retained. Constants are independent of N, beta_N and tau. This diagnostic endpoint therefore vanishes for all 0<s<d. The positive temperature enters only its scaling: the equation itself has exactly zero diffusion.

Exact negation: an admissible parameter, characteristic-class solution or displayed norm/endpoint bound violates the statement. This is a theorem only for the declared internal-transport model and independently defined periodic diagnostic. Diffusion, ordinary transport, both response terms, actual time-dependent test, periodic force remainder, cutoff annular source, interacting law and singular passage are not supplied by it. The sufficient full-corrector comparison in proof (8.2) is OPEN. Later review status belongs in canonical records; submitted bytes remain frozen.
