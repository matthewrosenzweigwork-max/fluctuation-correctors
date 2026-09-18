# Normalization and scaling ledger

## Frozen symbols

- Dimension: \(d\).
- Riesz exponent: \(0<s<d\); log separate.
- Particle number: \(N\).
- Inverse temperature: \(\beta_N\).
- Effective microscopic coupling:
  \[
  \lambda_N=\beta_NN^{s/d-1}.
  \]
- Empirical measure:
  \[
  \mu_N=N^{-1}\sum_{i=1}^N\delta_{x_i}.
  \]
- Fluctuation discrepancy: \(\rho_N=\mu_N-\mu\).
- Fluctuation scale: record theorem by theorem; thermal candidate \(\sqrt{N\beta_N}\), initial candidate \(\kappa_N\), combined scale must be frozen explicitly.

## Regime table

| Regime | Condition | Equivalent beta scale | Status |
|---|---|---|---|
| Old pathwise sufficient | \(\beta_NN^{2s/d-1}\to0\) | \(\beta_N\ll N^{1-2s/d}\) | existing baseline to supersede |
| Full subcritical | \(\lambda_N\to0\) | \(\beta_N\ll N^{1-s/d}\) | target |
| Critical | \(\lambda_N\to\lambda\in(0,\infty)\) | \(\beta_N\sim\lambda N^{1-s/d}\) | target |
| Supercritical | \(\lambda_N\to\infty\) | \(\beta_N\gg N^{1-s/d}\) | sharpness |

## Required additions

For every active theorem, append:

- exact Hamiltonian convention;
- factor of \(1/N\) in pair interaction;
- Brownian coefficient;
- deleted diagonal convention;
- periodic Fourier normalization;
- modulated energy factor \(1/2\);
- test-function normalization;
- corrector coefficient;
- centering and counterterms;
- error after multiplication by the fluctuation scale.


## Round 001 v1.0 freeze (2026-09-17)

Authoritative common dossier: `TASKS/ACTIVE/ROUND_001_MODEL.md`; baseline `475a5399828bc6e2ccbade08c59b8778638df14a`.

- Unit torus, Haar mass one, Fourier characters exp(2 pi i k.x); zero mode of g is zero. Fixed smooth even kernel first; singular target is heat-regularized Riesz with the explicit Fourier coefficient in the dossier. Fourier constant is separately source-audited before use.
- Hamiltonian H_N=sum_i V(x_i)+(1/(2N))sum_{i!=j}g(x_i-x_j); gradient drift is -grad_i H_N; Brownian coefficient sqrt(2/beta_N). Its formal invariant Gibbs density is exp(-beta_N H_N), but no equilibrium/dynamic transfer is used.
- nu_N=1/beta_N; reference mu^{N,g} retains temperature and kernel dependence. Smooth positivity is assumed on the finite horizon, not claimed uniformly without stated bounds.
- Empirical measure eta=N^{-1}sum delta_i, rho=eta-mu. Ordered distinct-label tuples, denominators N^k, not (N)_k. Label deletion is meaningful even at coincident coordinates for smooth kernels.
- P_N=U_2/2. General U_k is the precise inclusion-exclusion statistic in the dossier. Background centering is not mean-zero under iid laws: E U_2[Phi]=-mu_0^2(Phi)/N at t=0. For constant Phi=1, U_2=-1/N and U_3=2/N^2.
- sigma_N=min(sqrt(N beta_N),kappa_N); iid row has kappa_N=sqrt(N). Do not replace this by the thermal scale when beta_N grows.
- Initial laws are arbitrary for finite-N pathwise identities, exchangeable when deriving marginals; iid and Gibbs fluctuation theorems remain distinct and open.
- For fixed smooth g, the Riesz reference exponent s labels a sequence but does not create a microscopic singularity. Fixed-cutoff bounds cannot be used to infer lambda_N critical power counting.
- Logarithmic normalization remains separately OPEN. No s=0 substitution.

## Ordered-source temperature map

In dimension one, V=0, source H=N^{-s} sum_{i!=j}g has Gibbs density exp(-b H). Campaign energy is (2N)^{-1} sum_{i!=j}g, so b=beta_N N^{s-1}/2=lambda_N/2. No ordered/unordered factor is suppressed. The source real-space kernel has exactly the campaign Fourier constant; its separately printed fractional-Laplacian c_s is inconsistent and is not adopted. Frozen campaign exponents and Fourier coefficients remain unchanged.

## Round 002 residual scaling

For fixed smooth iid data, raw endpoint/cubic/pair-bracket/cross-bracket rates are N^-1, N^-3/2, beta_N^-1 N^-2, beta_N^-1 N^-3/2, respectively. Scaled rates are min(sqrt(beta_N),1) N^-1/2, min(sqrt(beta_N),1) N^-1, min(1,beta_N^-1) N^-1 and min(1,beta_N^-1) N^-1/2. Both independent proofs recompute sigma_N^2/(beta_N N)=min(1,beta_N^-1). No Riesz exponent or effective lambda gain has been inserted into this fixed-smooth calculation. All three frozen Riesz regimes are unchanged.

## Round 002 final integration

Round 002: Gaussian covariance prefactors are a_N^2=min(beta_N,1) and c_N=min(1,beta_N^-1), with dynamic factor 2 and unequal-time overlap ending at the smaller terminal time. Zero-diffusivity covariance equals the initial covariance of the full inviscid backward tests; dynamic covariance is zero. The cosine heat check carries variance factor one half. These physical-temperature facts do not replace the frozen old, full-subcritical or critical Riesz exponents.

## Round 003 scales, without changing the campaign regimes

The iid scale is sigma_N=sqrt(N b_N), b_N=min(beta_N,1). Above 2s=d, the bare initial Riesz pair's natural absolute-moment size is N^(2s/d-2); its proposed sharp scaled criterion in THM-019 is b_N N^(4s/d-3)->0. THM-018 separately constructs the upper bound. At sqrt(N) the bare-pair threshold is 3d/4. This criterion is a theorem about an initial statistic only; it replaces neither beta_N N^(2s/d-1)->0 nor lambda_N=beta_N N^(s/d-1)->0 nor critical positive finite lambda_N. At critical lambda and s<d, beta_N grows and b_N is eventually one.

The internal-transport diagnostic has a different core ell=(2s(s+2)tau/N)^(1/(s+2)). Its squared norm grows as N^((2s-d)/(s+2)) above 2s=d; multiplying by b_N/N yields b_N N^(-(d+2-s)/(s+2)), which vanishes for all s<d. This is not a change to the physical-temperature or effective-coupling normalizations.

## Round 004 retained diffusion scaling

Relative noise is sqrt(4nu), generator2nu Delta, internal force2s/N, and source s r^-s theta^T A theta. THM020's initial iid upper rates match the transport diagnostic for all finite nu, including nu=1/beta_N: b_N/N, b_N(1+log N)/N, or b_N N^(-(d+2-s)/(s+2)). This is upper control for the local model only, not a two-sided diffusive norm or actual hierarchy power count. The old floor, microscopic lambda and logarithmic normalization remain unchanged.

Round005 periodic base squared Haar norm is O(rho_N), with rho_N=1,1+logN,N^((2s-d)/(s+2)) across2s<d,=d,>d. The conditional full-response multiplier is exp[2(c+C_R)T], independent ofN under prescribed data bounds. Iid scaling yields b_N rho_N/N with M0 squared, not one density factor. Periodic barrier requires bounded nu=1/beta_N; it does not inherit the local theorem's all-finite-nu uniformity.

THM025 AUD028/029: full inverse initial iid orders b_N/N, b_N(1+logN)/N, b_N N^(-(d+2-s)/(s+2)) are proved for d>=3,0<s<=d-2 and beta bounded below, including every critical sequence eventually. General product-density factor M0^2 and mean-field bias remain. These rates do not control positive-time residuals. Old energy-floor and microscopic coupling powers are unchanged.

R8 adds a domain theorem with unchanged ordered-label/N^k normalization, P=U2/2, internal coefficient1/N, lower1/N and scalar1/(2N). Fixed-N derivative/density estimates supply no new power count. Pending R9 reference-noise claims use sigma_N^2=N b_N,b_N=min(beta_N,1),nu=1/beta_N with beta bounded below. The old floor, full microscopic lambda and positive finite critical limit remain separate; logarithmic interaction is still separate.

R9 accepted reference scaling: nu||grad_pair Phi||_L2(time,Haar)^2<=C N^a,a=s/(s+2); sigma_N^2=N b_N,b_N=min(beta_N,1),nu=1/beta_N. Pair symmetry reduces full gradient norm squared to2||G||2^2, leaving b_N(N-1)/N^2 times the full nu-energy. Thus self-noise<=C b_N N^(a-1) and absolute cross<=C sqrt(b_N)N^((a-1)/2). Zero-noise handled separately. No relation among the three frozen temperature regimes is changed; critical sequences eventually have bounded nu, general beta-to-zero subcritical sequences need a new uniformity argument.


R10 submitted/audited-hostile powers use p=s+2, a=s/p, theta=1-s/d. The two energy floors are -C N^a and -C N^(s/d), with s/d<=a. Clipping level N^(1/(4p)) yields approximate actual noise O(N^(-1/(2p))) plus its faster Haar rate. Smoothing delta=N^(-theta/(5d-s+2)) yields O(N^(-theta/2)). These are actual bounded/regularized fields, with full-tail equivalences separately stated. No fixed exponent is silently transferred to the original full noise. Full subcritical lambda, old energy floor and finite positive critical lambda are distinct; logarithm separate.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 keeps physical2nu Nb, ordered deletion and original mean-field centering. With p=s+2,a=s/p,theta=1-s/d, critical chi=lambda^-1 N^[s(p-d)/(dp)] tends to zero, and a-theta=(s(s+2)-2d)/(dp). Both strict signs are required. No Coulomb/equality limit is silently included; old energy-floor, full-subcritical and finite positive critical powers remain distinct.

R11/R13 gate scaling check: R11 chi=nu N^(2/(s+2)) equals lambda_N^-1 N^[s(s+2-d)/(d(s+2))], so criticality lies in bounded chi through Coulomb, but general full subcriticality does not. R13 covers all bounded nu,d>=4,0<s<2 with sigma^2=N min(1/nu,1). No beta exponent is replaced. THM035 uses b=1,sigma=sqrt(N) at zero noise for deterministic drift; this differs from setting the noise bracket to zero.
