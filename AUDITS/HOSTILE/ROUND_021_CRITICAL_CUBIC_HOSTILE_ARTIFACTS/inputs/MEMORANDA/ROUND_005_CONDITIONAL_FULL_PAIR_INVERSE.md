# Round 005 conditional module: restoring both nonlocal responses

2026-09-17. Root construction, CONDITIONAL / SELF_CHECKED. This is a complete bounded-perturbation argument conditional on the precise base-process, source-potential and response hypotheses below. It does not declare TASK034 or TASK036 proved, nor establish regularity of the actual mean-field/backward-test solutions. A separate review is required before promotion. The statement distinguishes Haar L2 from the initial reference-law norm.

## Explicit hypotheses

On the unit Haar torus pair space off the diagonal D, for N>=2 and a finite interval [0,T], suppose S_(t,a) is the jointly measurable two-time Markov evolution of a noncolliding continuous auxiliary pair process with the prescribed base generator G_N (ordinary transport, independent noises and exact internal B/N). The following are hypotheses, not deductions from a formal differential expression.

1. It acts on bounded Borel functions off the diagonal as a positive sup-norm contraction, with the deterministic-time conditional Markov property and composition law. It has a consistent strongly measurable extension to Haar L2 of norm at most exp(c(a-t)), for a fixed c>=0 independent of N and parameters in the claimed range. Diagonal values are immaterial to these operators.
2. J_t is measurable, symmetric in the pair, and has absolutely integrable occupation from every starting point. Its signed base potential U_N(t)=E_(t,x,y) integral_t^T J_a(X_a,Y_a) da is a bounded Borel function for each finite N with sup bound B_N<infinity. Its Haar L2 norm is bounded by A_N uniformly in t. The absolute-source potential has a finite sup bound as well. These bounds and time measurability are proved inputs required of TASK036, not an unqualified smoothness argument.
3. The exact two-response operator R_t=R_x,t+R_y,t is a jointly measurable operator on bounded Borel functions off the diagonal, of sup norm at most C_R, and has a consistent strongly measurable Haar L2 extension of norm at most C_R, uniformly in time and N. For a finite-measure kernel its values off the pair diagonal do not depend on a chosen value on that diagonal. It commutes with pair exchange. TASK034 is intended to supply this assertion for 0<s<=d-2 and a prescribed bounded C1 density, including the Coulomb atom.
4. The base evolution and source commute with pair exchange. All time integrals below are well-defined pointwise and as Bochner L2 integrals; joint measurability and the displayed uniform bounds are sufficient in the separable L2 space. This measurability is part of the input assertion, not hidden notation.

The claimed solution is the full bounded Borel martingale inverse with source J+R Phi, namely for every initial state and time, Phi at the current state plus the integrated source is a true martingale, with terminal value zero. No classical or distributional regularity is included. The equivalent pointwise integral equation is

    Phi_t = U_N(t)+integral_t^T S_(t,a) R_a Phi_a da.         (1)

Exact negation: inputs obeying 1–4 fail to have the unique bounded Borel solution described below, or its displayed norm bound fails. The proof does not assert that some larger unspecified operator domain has this inverse.

## Construction with all finite-time constants

Define Vh(t)=integral_t^T S_(t,a)R_a h_a da. Starting with U_N, iterated time-simplex integration and Markov contraction give

    ||(V^k U_N)(t)||infty <= B_N [C_R(T-t)]^k/k!.

Every term is bounded Borel by the assumed measurable kernels and time integration. The series Phi=sum_(k>=0) V^k U_N converges uniformly in (t,x,y), is bounded Borel, vanishes at terminal time and satisfies (1), by dominated convergence. Its sup norm is at most B_N exp(C_R T). Pair exchange commutes term by term, hence Phi is symmetric. The response remains the signed operator with both slots and coefficient one; it is not presumed Markov or dissipative.

For k>=1, the L2 norm of the product of intervening semigroups on an ordered simplex is bounded by exp(c(a_k-t)): the interval lengths add, rather than introducing k copies of exp(cT). The terminal U_N(a_k) has norm at most A_N. Thus for every k>=0 (enlarging the k=0 bound harmlessly),

    ||(V^k U_N)(t)||2 <= exp(cT) A_N [C_R(T-t)]^k/k!.

This proves absolute convergence of the same series in uniformly bounded time-dependent Haar L2 and gives

    sup_t ||Phi_t||2 <= A_N exp[(c+C_R)T].                 (2)

Consistency of Borel and L2 actions identifies the two series almost everywhere at each time. No derivative norm, inverse ellipticity constant, kernel cutoff loss or N-dependent exponential is hidden in (2). The constants c,C_R must actually be uniform on the proposed parameter range.

For two bounded Borel solutions of (1), their difference d=Vd obeys

    ||d_t||infty <= sup_a||d_a||infty [C_R(T-t)]^k/k!

for every k. Letting k tend to infinity proves pointwise uniqueness. The same argument with the L2 evolution bound proves uniqueness among strongly measurable, uniformly Haar-L2-bounded mild solutions, by taking the L2 supremum and exp(cT) outside the simplex integral. This is a distinct a.e. uniqueness assertion; no pointwise recovery from an arbitrary L2 representative is presumed.

## Martingale identity without classical derivatives

The constructed response R Phi is bounded and jointly measurable. Its occupation is therefore absolutely integrable on [0,T]. The input J occupation is integrable by hypothesis2. Using (1), the conditional Markov property, the flow composition and time splitting at a deterministic intermediate time shows

    Phi_(t+h)(X_(t+h),Y_(t+h))
      +integral_t^(t+h) [J_a+R_a Phi_a](X_a,Y_a) da
    =E[ integral_t^T [J_a+R_a Phi_a](X_a,Y_a) da | F_(t+h) ]

for the process started at (t,x,y). To justify the interchange, first use bounded time-simple approximations for R Phi and positive/negative truncated J; then apply bounded convergence to the response and domination by the absolutely integrable full J occupation. The right side is the conditional expectation of one integrable random variable and hence a true uniformly integrable martingale. Conversely, terminal expectation of this martingale identity gives (1), so the uniqueness already proved applies. This restores both nonlocal responses in the specified probabilistic inverse without asserting a classical PDE solution or using a singular Ito formula on Phi.

## Initial iid consequence and the different density factor

Suppose in addition that the iid initial law has density mu_0 bounded by M_0, and freeze the exact mean-field-centered statistic P_N from THM015. Since Phi is symmetric,

    E|sqrt(N b_N) P_N[Phi_0]|^2
      <= b_N (N-1)/(2N^2) ||Phi_0||_L2(mu_0^2)^2
      <= [b_N M_0^2/(2N)] A_N^2 exp[2(c+C_R)T],            (3)

where b_N=min(beta_N,1), beta_N>0. The factor here is M_0 squared because the full kernel is not assumed translation invariant and (2) gives only its Haar pair norm. The single density factor for the earlier relative-coordinate cutoff diagnostic cannot be copied into this bound. The deterministic mean and first projection are included by the exact THM015 second-moment identity; no centering has been changed.

If the base potential satisfies A_N^2<=C times 1,1+log N,or N^((2s-d)/(s+2)) according as 2s<d,2s=d,or2s>d, then the full inverse has the corresponding endpoint rates b_N/N,b_N(1+log N)/N,or b_N N^(-(d+2-s)/(s+2)). This would discharge the bounded analytic initial-endpoint implication directly, without proving closeness to a particular diagnostic. It is conditional on the stated modules and prescribed background/test bounds. TASK036 currently proposes only nu in a fixed bounded interval, so this conditional conclusion must not be called uniform over all beta_N if nu=1/beta_N. The bound covers only beta_N bounded below by the inverse interval endpoint (with the zero-noise limit included separately).

## Remaining assertions

Neither source-potential hypothesis2 nor singular-semigroup hypothesis1 is proved in this memo; TASK036 is the active constructor. Finite-measure response hypothesis3 is the separate TASK034 candidate, not assumed from a remembered integration-by-parts rule. Uniform C1 density/background and C2 actual backward test, full generator differentiability/approximation, positive-time evolved-law cubic residuals, contractions, corrector/cross brackets and singular hierarchy tails are still separate tasks. A bounded Borel inverse by itself cannot be inserted into the smooth finite-particle Ito identity. Its gradient/domain and regularized passage require proof.

No Gaussian claim, law transfer, finite critical truncation, new normalization or mathematical novelty assertion follows from this conditional construction. A separate independent review of this memo and verification of its input modules are necessary. This file preserves a concrete, complete module at the natural resumption point rather than replacing the campaign with a broad plan.
