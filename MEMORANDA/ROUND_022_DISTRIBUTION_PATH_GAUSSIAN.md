# Round022 — actual distribution-valued continuous-path fluctuations

2026-09-18 UTC. ROOT CONSTRUCTION / SELF_CHECKED / VERSION_LOCKED. Entire THM044 and negation frozen separately. This is exposed synthesis; R20's whole path theorem is an expressly conditional input pending its independent gate. No independent mathematical status or full flagship conclusion is assigned.

## 1. Hilbert conventions and actual random paths

Use exactly THM044. For the real Fourier basis e_l, the weight w_l=(1+|k_l|^2)^(-r) makes the H^-r norm of a mean-zero distribution equal to sum_l w_l|u[e_l]|^2; the sine/cosine normalization agrees with the opposite complex Fourier pair. The zero mode of Z_N is exactly zero. The real weighted sequence Hilbert space is complete and separable, by truncation and rational finite sequences.

Because r>d/2, sum_k(1+|k|^2)^(-r)<infinity. Thus each delta_x belongs to H^-r with a uniform bound. Dominated convergence applied to its Fourier coefficients proves x->delta_x is continuous into this space. Actual finite-N continuous noncolliding torus paths therefore give continuous H^-r paths Z_N. Coordinate measurability and separability, or uniform limits of measurable finite Fourier interpolations, give measurable C([0,T],H^-r)-valued random elements. Haar centering is exactly the actual one-body centering by the full translation/uniqueness argument in R18/R20. No positive-time product law is used.

## 2. Simultaneous Hilbert control of the genuine source

The complete deterministic R16 argument, restated in R20(3.8), gives at every collision-free configuration and simultaneously for each real smooth h

    |P_N[J^h](x)|<=C ||h||_(A_R) V_l(x),
    V_l=E_l+S_(2l)+c_(2l)>=0, R=alpha+M+3.

Every original empirical/Haar contraction remains. Its actual-law energy consequence at l=N^(-2/d) is sup_t E V_l(X_t)<=C N^(s/d-1), independent of N and selected bounded noise. This is a deterministic family bound, not a supremum of separate expectations. The full accepted source proof supplies the polynomial retained symbol, commutator and positive omitted kernel; a theorem-card label alone is insufficient.

For each real Fourier mode e_j, Q_a^nu e_j=exp(-(D_j+nu a_j)a)e_j. Its A_R seminorm is at most C(1+|k_j|)^R, uniformly in terminal/integration times and noise. At any fixed terminal t and integration u<=t, the sequence with components P_N[J^(Q_(t-u)^nu e_j)] therefore has H^-r norm at most

    C V_l(X_u) [sum_j w_j(1+|k_j|)^(2R)]^(1/2).

The sum is finite exactly under the sufficient strict r>R+d/2. This remains true simultaneously in all t,u. Finite sums and Minkowski, followed by monotone convergence, define the Hilbert source integral E_N(t) and show

    E sup_(t<=T)||E_N(t)||_(H^-r)
      <=C sqrt(Nb_N) integral_0^T E V_l(X_u)du
      <=C sqrt(b_N) N^(s/d-1/2).                       (2.1)

More explicitly, for each realized finite-N path, positive minimum separation on the compact time interval makes V_l(X_u) bounded and continuous. Each coordinate source integral is continuous in t, and the square-summable mode envelope gives uniform Hilbert convergence of the coordinate truncations by the same pathwise bound. Thus E_N is a continuous Hilbert random path, genuinely defined by the original singular sources. No stochastic limit/interchange, source-square moment or singular diagonal assignment is used. The scale is chosen only after the fixed-N particle heat passage.

## 3. Linear Fourier part and its uniform high-mode tail

The genuine scalar stopped first-order identity, proved in full R18/R20 with literal source half and row -D*h, holds for every deterministic time and each e_j. The resulting continuous version is

    Z_N[e_j](t)=I_N,j(t)+M_N,j(t)+E_N[e_j](t),
    I_N,j(t)=sqrt(b_N/N) exp(-L_N,j t) sum_i e_j(X_i(0)),
    M_N,j(t)=integral_0^t exp(-L_N,j(t-u))dB_N,j(u),
    B_N,j(t)=sqrt(2nu_N b_N/N) sum_i integral_0^t grad e_j(X_i(u)).dW_i(u).

Here L_N,j=D_j+nu_N a_j>0. B_N,j is a true continuous martingale in t. M_N,j is a stochastic convolution, not generally a martingale in terminal time. The identities hold simultaneously on a single probability-one set for all countably many modes and rational times, hence all times by continuity. Initial iid Haar gives E|I_N,j(0)|^2=b_N and sup_t|I_N,j(t)|=|I_N,j(0)|.

The pathwise bracket density of B_N,j is at most4nu_N b_N a_j, since |grad e_j|^2<=2a_j. Stopped isometry and the elementary martingale L2 maximum inequality give E sup_t|B_N,j(t)|^2<=16nu_N b_N a_j T. The maximum inequality follows from the same first-crossing/conditional Jensen/integration argument given in R20 for Brownian motion, valid for |B_N,j| as a submartingale with integrable square. No independent or deterministic-integrand Gaussian assumption is needed.

Deterministic integration by parts yields

    M_N,j(t)=B_N,j(t)-L_N,j integral_0^t exp(-L_N,j(t-u))B_N,j(u)du,
    sup_t|M_N,j(t)|<=2 sup_t|B_N,j(t)|.

Thus E sup_t|I_N,j+M_N,j|^2<=C_T(1+a_j), using b_N<=1,nu_N b_N<=1. This also handles zero noise directly. Sum nonnegative weighted terms and use supremum of sum<=sum of sup to get exactly

    E sup_t||(Id-Pi_K)Y_N(t)||_(H^-r)^2
       <=C_T sum_(|k|>K)(1+|k|^2)^(-r)(1+|k|^2),          (3.1)

with the two real modes per opposite pair matching the complex-lattice sum up to the explicit harmless fixed constant. The series converges since r>d/2+1, which follows from the frozen stronger restriction. Tonelli gives summability of the weighted coordinate suprema almost surely, hence uniform Hilbert convergence to a continuous Y_N. Coordinate identities identify Z_N=Y_N+E_N as Hilbert paths. This identification avoids assuming a Hilbert-valued stochastic integral without verifying it.

## 4. The continuous Gaussian distribution

For independent xi_j and B_j from the card, the scalar modal convolution obeys the identical integration-by-parts bound. Consequently E sup_t|G_j(t)|^2<=C_T(1+a_j) and sum_j w_j E sup|G_j|^2<infinity. Tonelli and tail summability give almost-sure uniform Hilbert convergence of the partial sums, and convergence of tails in expected squared uniform norm. This constructs a continuous measurable mean-zero H^-r path G.

Every continuous real linear functional of finitely many Hilbert evaluations is an L2 limit of centered Gaussian finite sums, because the weighted tail estimate and Cauchy-Schwarz control the approximation. Its characteristic function is the limit of the Gaussian characteristic functions. Thus G is a centered Hilbert Gaussian process, including all degeneracies. Direct initial independence and Ito isometry give the exact modal covariance in THM044. Smooth tests pair continuously with H^-r (their H^r norm is finite); absolute Fourier summation gives exactly the R18/R20 covariance without an extra factor two or a zero mode. No assertion about sharp Sobolev regularity is made.

## 5. Actual tightness and full path weak convergence

For fixed K, Pi_K Y_N has tight laws in the finite-dimensional continuous-path space: the full R20 initial fourth-moment and adapted-convolution increment proof applies to this fixed finite real Fourier list, giving uniform initial fourth moments and increments bounded by C_K|t-u|^2. Its explicit dyadic compact-set construction proves tightness. The same statement for Pi_K Z_N follows from the full conditional R20 actual-modulus argument, or its accepted whole conclusion once gated. This fixed-K fact does not itself prove Hilbert tightness.

We supply that missing step. For an arbitrary epsilon>0 choose e_j=2^-j and positive p_j summing to less than epsilon/4. Equation(3.1) gives K_j increasing so that sup_N P(||(Id-Pi_Kj)Y_N||_C>e_j/2)<p_j. Equation(2.1) gives N_j with P(||E_N||_C>e_j/2)<p_j for all N>=N_j. Therefore the Z_N tails exceed e_j with probability at most2p_j on that tail of N. For the finitely many2<=N<N_j, Pi_K Z_N->Z_N uniformly in time almost surely: for any continuous Hilbert path its compact image has uniformly vanishing projection tails, by a finite covering and the contraction norm of Id-Pi_K. Increase K_j to make each of these finitely many tail probabilities at most2p_j. Increasing K_j preserves the already established tail inequalities because orthogonal projection tails decrease in norm at each time.

For each j, tightness of the fixed finite projection supplies a compact set C_j in its finite-dimensional path space with sup_N P(Pi_Kj Z_N notin C_j)<p_j, after reducing the p_j total if necessary. Let A be the set of Hilbert paths with Pi_Kj z in C_j and ||(Id-Pi_Kj)z||_C<=e_j for every j. A is closed. For any positive tolerance choose one j with e_j below half that tolerance; a finite net of C_j embedded into the Hilbert path space gives a finite net of A. Thus A is totally bounded and, as a closed subset of the complete uniform Hilbert path space, compact. The union bound gives inf_N P(Z_N in A)>=1-3sum_j p_j>1-epsilon. This proves actual tightness in exactly the claimed topology. The same proof, or its stronger direct tail/moment estimates, gives tightness of G. No neighborhood of a compact set is asserted compact.

For each K the full R20 fixed-list theorem supplies weak convergence Pi_K Z_N=>Pi_K G in the finite-dimensional continuous-path space, with the same covariance and exact centering. For bounded globally Lipschitz F on Hilbert path space, (3.1), Cauchy-Schwarz and (2.1) show

    limsup_N |E F(Z_N)-E F(Pi_K Z_N)|
      <=Lip(F) C [sum_(|k|>K) w_k(1+|k|^2)]^(1/2).

Here Id-Pi_K is a contraction and the residual vanishes as N->infinity; no uniform-in-N high-mode estimate is incorrectly deduced from just its small total norm. The same tail bound applies to G. First pass N->infinity at fixed K and then K->infinity. This proves all bounded Lipschitz expectations. Actual and Gaussian tightness supply a common compact set with arbitrarily high probability; infimal Lipschitz approximation of bounded continuous functions on that set, exactly as in R20, extends the conclusion to every bounded continuous functional. This is full weak convergence in C([0,T],H^-r).

## 6. Scope and outstanding gates

T=0 is the initial Hilbert iid assertion, with all thermal/source integrals zero and the same finite-projection/tail proof. At zero limiting or identically zero noise the corresponding thermal limit or actual martingale vanishes; no inverse-noise division is used. Constants are absent zero modes; linearly dependent test evaluations and degenerate covariance require no matrix inverse. Every finite bounded-convergent noise sequence is admitted without a rate. Only the explicit sufficient r range is asserted, and the strict source threshold remains s<d/2.

Conditional on the full same-source interfaces and R20, the whole frozen conjunction has the preceding proof. Root has read the constructor's R20 proof and prior source/audit narratives; this is exposed synthesis. The accompanying immutable packet supplies the full source/exposure dossier and fresh Hilbert-tail/normalization/falsification diagnostic. Separate whole reconstruction and hostile review remain required. No original theorem or independent source history is altered. No entire higher-order hierarchy, inhomogeneous/logarithmic/general-preparation or outside-range flagship resolution is claimed.

## 7. Supporting exact diagnostic and issuance

The new root standard-library program passes47437 exact assertions in19 categories, with12 coefficient/projection/inference mutation witnesses. It enumerates literal finite cyclic iid real/complex Fourier normalization, exact positive-kernel convolution and its maximum bound, weighted projection identities and sup-sum inequality, all topology/source exponent conditions and dyadic shell counts. Escaping orthogonal unit vectors give the concrete mechanism defeating coordinate-only tightness and compact-neighborhood inferences; finite computed instances support the explicit infinite sequence, not a singular particle counterexample. No random seed, tolerance, external dependency or outside theorem is used. This is exposed root self-check only. Exact commands, copies and seals are in the adjacent artifact packet.
