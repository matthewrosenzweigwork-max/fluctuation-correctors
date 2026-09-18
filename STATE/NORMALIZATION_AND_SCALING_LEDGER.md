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


Round014 final gate,2026-09-18 UTC. R14 accepted: alpha=(s+1-q)/(s+2),kappa=(2q-s)/(2(s+2))>0; sigma integral|ell|<=C sqrt(b)N^-kappa pathwise. Both centered rho[g]/N+c/(2N) and regrouped eta[g]/N-c/(2N) are exact. Critical chi=lambda_N^-1 N^[s(s+2-d)/(d(s+2))] tends to zero in strict sub-Coulombity. Zero noise uses b1 directly. No old-floor/full-subcritical/critical exponent changes.


Round015 final gate,2026-09-18 UTC. R15: theta=1-s/d,a=s/(s+2),omega=min(s,d-s-2)/2,e=(s-omega)/(s+2). The scaled critical integrated cubic is bounded by C[N^(1/2-theta)+N^-1/2+N^(e-1/2)+N^((a-theta)/2)], all strictly decaying for d>=4,0<s<2. Source sup_t E|PJ|<=C N^-theta uniformly over bounded nu; scaled absolute time integral<=C sqrt(b)N^(s/d-1/2). Critical nu=lambda_N^-1N^-theta and bounded chi are checked. No exponent or original normalization changes.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R16 raw N^(s/d-1) source is reconstructed through Coulomb, but sqrt(Nb) absolute-time-integral bound only decays at s<d/2. R17 has nu_N=lambda_N^-1N^(s/d-1),b_N1 eventually and error C[N^(s/d-1/2)+sqrt(nu_N)+nu_N]. THM040 uses b(nu)=min(1/nu,1) with b0=1, no convergence rate in bounded nu_N->nu_bar assumed. The three old/full-subcritical/critical conditions remain distinct.


R17 final gate,2026-09-18 UTC. R17 accepted critical nu=lambda^-1 N^(s/d-1), eventual b1, exact error C[N^(s/d-1/2)+sqrt(nu)+nu]. Timesum covariance and strict s<d/2 remain. THM041 proposes all finite diffusivities with b=min(1/nu,1),b0=1 and nu b<=1, but that new uniformity is unaudited and does not follow solely from the bounded-noise card.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 preserve b=min(1/nu,1),b(0)=1,sigma=sqrt(Nb),D_k=4pi^2 c_ds |k|^(s+2-d),a_k=4pi^2|k|^2. Exact covariance weights D/L and nu*a/L; timesum initial and timelag thermal. Original old-floor/full-subcritical/finite-critical exponents remain distinct.


R21 root synthesis,2026-09-18 UTC. New THM043/PO030 freezes actual integrated critical U3 decay throughout the entire strict R12 noise-decay range d>=3,0<s<d-2,s(s+2)<2d. Root TASK093 complete exposed working proof MEMORANDA/ROUND_021_CRITICAL_CUBIC_SYNTHESIS.md is UNSEALED/UNAUDITED. It composes accepted R5 initial endpoint, R8 actual domain/identity, R12 whole bracket, R14 both lower contractions and R16 source. The conditions imply s<d/2 and3s<2d-2; critical chi tends to0. Exact four-term bound is C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa], with p=s+2,a=s/p,theta=1-s/d and R14 midpoint q,kappa=(2q-s)/(2p)>0. No instantaneous absolute U3 claim. Root fresh diagnostic12531 assertions/18categories/4mutationfamilies passes but full source/exposure/seal packet and both independent gates remain outstanding. TASK094/AUD061 reserved fresh R21blind andTASK095/AUD062 reserved separate hostile, not yet written. Next freeTASK096,AUD063,THM044,PO031. R20 TASK091/AUD059 prepared blind retains next available worker priority; TASK092/AUD060 reserved R20hostile. No earlier card changed or independent status assigned.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.

R20/R21 subsequent status at R18/R19 acceptance: R20 constructor sealed; independent blind and hostile active. R21 root source/exposure/diagnostic packet is now sealed SELF_CHECKED (29 inputs,38 archive members); fresh TASK094/AUD061 whole reconstruction active, TASK095/AUD062 hostile still reserved. Earlier unsealed entries above are chronological history. Neither new theorem is promoted. Current exact pointers/hashes are STATE/CAMPAIGN_STATE.md.


R22 pending extension,2026-09-18 UTC. New THM044/PO031 freezes distribution-valued path convergence in C([0,T],H^-r) for the same bounded-convergent-noise homogeneous iid-Haar row d>=3,0<s<=d-2,s<d/2, with explicit sufficient r>2d+5-s/2. Required source remainder is expected Hilbert path supremum C sqrt(b)N^(s/d-1/2), and linear Fourier-tail second moment is bounded by C sum_(|k|>K)(1+|k|^2)^(-r)(1+|k|^2). No optimality or full hierarchy claim. Root TASK096 complete exposed construction is sealed SELF_CHECKED, expressly conditional on the full R20 source pending its gate.16inputs25members47437 exact checks19categories12 mutation witnesses reproduce byte-identically. ProofSHAaeb80c4b794fc8433faeefcbd5d244b48b26aa776e50f4294b677b050d501bd2; archiveSHA7a74dec907e0be0024c177d8b64273c04b9451bcda88999643816370d878fe5f. Exact proof MEMORANDA/ROUND_022_DISTRIBUTION_PATH_GAUSSIAN.md. TASK097/AUD063 statement-only Max dossier prepared16inputs, not dispatched; TASK098/AUD064 hostile reserved. Next freeTASK099,AUD065,THM045,PO032. No independent promotion; root previously read full R20 constructor and only current reviewer progress summaries.


R20 accepted gate,2026-09-18 UTC. Entire THM042/PO029 passes fresh whole reconstruction AUD059 and separate hostile AUD060; root full642/601/234-line comparison, exact accepted R4/R6/R10/R16/R18 source matching, and4255/2508/3316 supporting-check reproduction are complete. All14/14/16 input and22/23/25 archive-member packets verify unchanged/read-only; diagnostic reruns byte-identical. Genuine common source-family domination yields expected supremum remainder C sqrt(b)N^(s/d-1/2); adapted fourth moments and finite-prefix modulus sets give actual uniform-path tightness; continuous Gaussian existence and full weak passage are proved. Scope d>=3,0<s<=d-2,s<d/2,actual homogeneous iid-Haar preparation,bounded convergent noise,fixed finite smooth test list; all frozen zero/degenerate cases included. Mathematical label PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS/HOSTILE_REVIEW_PASS; no field/higher-exponent/hierarchy promotion. Exact records AUDITS/ROUND_020_GATE_INTEGRATION.md and ROUND_020_RECONSTRUCTION_COMPARISON.md. Constructor le typo and hostile tar-versus-ZIP wording are separately recorded, originals unchanged.

R21 whole reconstruction AUD061 now root-read527lines and byte-reproduced117352 assertions/72 whole finite identities/18 mutations;29-input38-member immutable packet verified. Comparison AUDITS/ROUND_021_RECONSTRUCTION_COMPARISON.md. TASK095/AUD062 fresh Max hostile dispatched32inputs, still pending sealed verdict. Root proof independent status is not inflated. R22 TASK097/AUD063 fresh Max blind16inputs and TASK098/AUD064 fresh Max hostile19inputs are both dispatched in separate worktrees at64ac0538, pending. Current active workers095/097/098; cap10 configured versus3 available plus root. Next freeTASK099,AUD065,THM045,PO032.


R23 new static-law gate,2026-09-18 UTC. THM045/PO032 freezes insufficiency of energy/Haar inputs at d4,s2: bounded smooth exchangeable common-translation-invariant static densities with exact Haar one-body marginals, support separation c N^-1/4 and pointwise energy at most -c N^1/2, yet sqrt(N) E|P[J_cos(4pi x1)]| tends to16 pi^3 a^2>0 along N=m^4. This is NOT an actual iid-prepared dynamical counterexample or mission change. Root TASK099 proves a negative grid regular part, exact grid energy, small coherent deformation, low-order frequency selection, uniformly controlled second variation/Riemann passage and smooth jitter realization. Complete exposed root proof MEMORANDA/ROUND_023_STATIC_THRESHOLD_INPUT_OBSTRUCTION.md is sealed SELF_CHECKED,8inputs17members1549 exact assertions24categories10 detecting mutations; fresh code-only root rerun byte-identical and safe member/byte verifier passes. ProofSHA4cf376ce886714eb2de2d1c100d10c1e5b29db4510bd5684cca60f4d9af51855; archiveSHAa7c6ddf00043fa4df3fc702dccfa195704a4e27973abc9fed432050c99e38a23. Fresh TASK100/AUD065 blind8-input and TASK101/AUD066 hostile11-input dossiers prepared, neither dispatched. Next freeTASK102,AUD067,THM046,PO033. Actual iid-flow threshold cancellation, integrated source bounds and higher hierarchy remain open. No new external citation/private input.


R21 final whole gate accepted,2026-09-18 UTC. THM043/PO030 is PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS (AUD061) and HOSTILE_REVIEW_PASS (AUD062), with exact published source/gate matching. The full strict range d>=3,0<s<d-2,s(s+2)<2d at finite positive microscopic critical lambda is retained. The actual integrated cubic residual obeys sigma E|integral U3[C Phi]dt| <= C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa] ->0. Absolute value remains after time integration; the genuine pair inverse retains both responses, the exact R8 domain, full true martingale and both lower contractions rho[g]/N+c/(2N). No instantaneous cubic estimate, Coulomb endpoint, Gaussian law or hierarchy is inferred. Root complete source/candidate/527-line blind/249-line hostile reading and twelve-item comparison are AUDITS/ROUND_021_GATE_INTEGRATION.md and ROUND_021_RECONSTRUCTION_COMPARISON.md. All29/29/32-input38/38/42-member packets verify unchanged; fresh diagnostics12531/117352/137147 reproduce saved bytes. The hostile stdout-only extra newline is explicitly recorded and no evidence normalized. All-real exponent implications are proved analytically; finite computations support but do not certify them. Earlier pending entries are chronological history.
