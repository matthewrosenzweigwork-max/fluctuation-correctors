# Round 001 frozen model and common dossier

- Dossier version: 1.0, 2026-09-17 UTC.
- Baseline commit: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Primary assertion: for every finite N >= 2 and beta_N > 0, the smooth periodic gradient model below admits an exact one-body backward duality and an exact deleted-diagonal pair generator identity, decomposed into the full linearized pair operator, upward interaction, explicit lower contractions, martingale and its quadratic/cross variations.
- Exact negation: there exists a permitted N, beta, smooth kernel/background/test and configuration for which this decomposition fails, or a term cannot be expressed in the declared hierarchy without enlarging it.
- Mathematical scope: finite N identities only in Round 001; no singular or fluctuation-limit theorem presumed.

## Model

The unit torus is R^d/Z^d, with Haar mass one and Fourier characters exp(2 pi i k.x). Start with any smooth even real periodic interaction g, zero mean. Set K=-grad g (odd, K(0)=0), b=-grad V, with V smooth periodic. Independent standard d-dimensional Brownian motions drive

    dx_i = [b(x_i) + (1/N) sum_{j != i} K(x_i-x_j)] dt + sqrt(2/beta_N) dW_i.

Let nu_N=1/beta_N. The reference mu=mu^{N,g} solves

    partial_t mu = -div((b+K*mu)mu) + nu_N Delta mu,

on a fixed horizon [0,T], with a smooth strictly positive probability density. Its dependence on beta_N and g is retained; no uniform derivative estimate is assumed. Denote u=b+K*mu, eta=N^{-1}sum_i delta_{x_i}, rho=eta-mu.

For the singular target separately, 0<s<d, g_hat(0)=0 and

    g_hat(k)=pi^(s-d/2) Gamma((d-s)/2)/Gamma(s/2) |k|^(s-d), k != 0.

This is the unit-torus Riesz normalization with local principal singularity |x|^(-s). The source audit must independently check this Fourier constant before a singular claim uses it. Heat regularization multiplies g_hat(k) by exp(-4 pi^2 epsilon |k|^2), epsilon>0. All identities begin at fixed epsilon or a fixed smooth g. The logarithmic model is excluded from this dossier and retains a separate open normalization.

## Statistics and centering

All particle tuples are ordered and have distinct particle labels; the denominator is N^k, not (N)_k. For a symmetric pair kernel Phi,

    U_2[Phi] = N^(-2) sum_{i != j} Phi(x_i,x_j)
                - (2/N)sum_i integral Phi(x_i,y)mu(y)dy
                + integral Phi(x,y)mu(x)mu(y)dxdy;
    P_N[Phi] = U_2[Phi]/2.

Deletion means labels, even when coordinates coincide; for smooth kernels the definition is valid on all configurations. Deterministic time-dependent test kernels are smooth in space and C^1 in time. The empirical diagonal convention and any alternative full-product convention must be mapped exactly.

For k>=0 define U_k[Phi] by summing over A subset {1,...,k}: integrate the complement against mu, insert distinct particle labels in the slots A, multiply by (-1)^(k-|A|) N^(-|A|), and sum all such labels. U_0[c]=c. No factorial normalization is hidden.

Initial law is arbitrary for exact identities; where exchangeability is needed for marginals, assume it explicitly. Iid initial mu_0, modulated Gibbs, equilibrium and deterministic preparations remain separate theorem rows. Primary algebra uses mean-field centering rho, with exact first-marginal centering separately tracked.

Retain sigma_N=min(sqrt(N beta_N),kappa_N). For iid initial data kappa_N=sqrt(N); neither the thermal scale alone nor any CLT is assumed. Exact algebra does not need sigma_N.

The regimes remain distinct: old beta_N N^(2s/d-1)->0; full subcritical lambda_N=beta_N N^(s/d-1)->0; critical lambda_N->lambda in (0,infinity). For a fixed smooth g, s is only a reference exponent until an actual estimate justifies its use. Do not infer singular critical power counting from fixed-cutoff algebra.

## Permitted and forbidden inputs

Permitted: the above definitions, elementary finite sums, integration by parts on the torus, smooth Ito calculus, and independently verified primary sources. No private manuscript input is needed for finite smooth algebra. Forbidden: reading another constructor output before independent reconstruction; local equilibrium, positivity of arbitrary weights, silent diagonal omission, inferred critical truncation, or source labels used as proof.

## Acceptance and falsification tests

Recover one-body duality twice independently. Derive all pair terms and compare both constructions. Check N=2 and N=3, K=0, constant Phi, separable Phi, and one Fourier mode. Give martingale brackets. State every N,beta and diagonal coefficient. Derive k=3 and investigate k=4/general recursion in a separate lane. No promotion beyond stated smooth scope.

Root alone integrates canonical state. Workers write only their assigned worktree output files; no commits, merges, pushes, changes to immutable inputs or canonical ledgers. A finished report must identify exact remaining lines and actual audit status. This invocation is setup plus execution of Round 001; the full mission remains open unless genuinely proved.
