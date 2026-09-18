# Round 006 particle realization: isolated hostile review

2026-09-17 UTC. TASK-048. Reviewer: `/root/r006_particle_hostile`, fresh isolated Astra Max context. Worktree: `/tmp/hocf-r006-particle-hostile-20260917`. Branch: `codex/hocf-r006-particle-hostile`. Pinned base: `93c20daa45aad455a95437b1dc6beed2883afada`.

**Verdict: PASS AS STATED for every assertion of the frozen THM-026 and the candidate's accompanying finite-mean energy identities. No failed line, counterexample to the admitted claim, missing hypothesis, or required proof repair was found.** The result is a fixed-N singular particle realization and density estimate. This review does not certify a corrector domain, interacting corrector Itô formula, residual or bracket estimate, law-class transfer uniform in N, or critical closure. Root comparison and canonical promotion remain separate actions.

The candidate was reviewed as submitted. No input was edited, and no silent repair is used below. The expanded calculations in this report reconstruct steps already present in the candidate. No campaign identifier is reserved by this reviewer.

## Evidence boundary and reproducibility

The new worktree was created from the prescribed published R4 commit before copying the dossier. Source bytes were checked against the prescribed input manifest before copying, and copied bytes were checked again. Exactly eight substantive input files were admitted. The routing task and manifest were read to establish this boundary. No other audit, constructor checker, canonical state, history, memory, root analysis, or external source was read. No singular-SDE theorem is imported. No child, dependency installation, commit, push, or root working-tree edit was performed.

The supplied manifest `AUDITS/ROUND_006_PARTICLE_HOSTILE_INPUT_SHA256SUMS.txt` has SHA-256 `a837b5e99ecf726c21cf9963697d563c4af2f3f53c3b6fe182ff4b0492e87b21`. The identical eight-entry manifest is copied into this report's directory as `ROUND_006_PARTICLE_HOSTILE_INPUT_SHA256SUMS.txt`.

| Admitted file | SHA-256 | Role in this review |
|---|---|---|
| `TASKS/ACTIVE/TASK-048_ROUND006_PARTICLE_HOSTILE.md` | `74701dac98ca1dd7ac0d703127bf0ea9e0165b2d3274535423ebcb3e232ad965` | Audit question and source boundary |
| `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md` | `aaaec9f6e10be3b5b6e82473ce11a441ad67c6c9b03c17254c144270e0103c7a` | Frozen statement and negation |
| `AGENTS.md` | `cc3a478358f1fcb3ccf472615c715acfdef575d9a80b5aa49417593a25825ed3` | Applicable campaign discipline, subject to the narrower task |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57` | Haar, Fourier, force, deleted-label and heat conventions |
| `THEOREMS/THM-021_SINGULAR_RESPONSE_OPERATOR.md` | `0dfa0d0fff1b6b7516e7779a0ac58f8fe03ab40625d81379d4c3abf8f2e4c4ed` | Identifies the needed kernel facts without assigning them audit status |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md` | `135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be` | Actual heat normalization, local expansion and divergence proof, reconstructed here |
| `MEMORANDA/ROUND_005_PERIODIC_PAIR_POTENTIAL.md` | `80abe107bc5dc4c832962868f38b43537ca1d6d1c5c560baa2f77d90a2cdba7e` | Acknowledged analogous cutoff, random-flow and measure-passage methods only |
| `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md` | `d4d1eae9f18d5796e8e99aa4b5e364b39321167f48eb27fa764bc7e327272017` | Complete candidate under review |

All eight files were inspected; none of their referenced but unlisted files was opened. The R5 pair theorem is not used to establish an N-particle theorem. The response-operator portions of R4 and the pair-potential portions of R5 are outside this review's certification scope.

Location references below use `C` for the candidate memorandum, `R4` for the supplied singular-response memorandum, `R5` for the supplied periodic-pair memorandum, and `T` for the frozen THM-026 card. These are report-local labels, not campaign identifiers.

## Exact assertion and falsification target

The asserted geometry is the unit Haar torus with characters `exp(2 pi i k.x)`. The fixed data satisfy `d>=3`, `0<s<=d-2`, `N>=2`, finite `nu>=0`, smooth real periodic V, the frozen coefficient-one positive Fourier Riesz kernel, `b=-grad V` and `K=-grad g`. Brownian motions are independent and standard; an initial random state is independent of their future increments. Particle interactions have coefficient `1/N`, and each coordinate's sum omits its own label.

For every prescribed collision-free start, the assertion is a pathwise unique global continuous realization with no collisions almost surely, joint measurability, deterministic-time conditional Markov property, positive minimum distance on each finite horizon, and almost-sure uniform convergence of the full family of same-noise heat approximations. For a bounded initial probability density, the time-t law has density at most `||F0||infinity exp((N a+(N-1) kappa)t)`. Explicit stopped and global energy bounds accompany it.

The negation would be an admissible tuple, start, or bounded density violating at least one of those conclusions. I tested that negation both by reconstructing the proof and by independent algebraic counterchecks. The exclusions in T line 19 are essential: logarithmic normalization, attractive interactions, non-gradient external drift, a bound for unbounded initial density, N-uniform law transfer, singular corrector derivatives or Itô passage, residuals, brackets, Gaussianity, and hierarchy closure are not admitted conclusions.

## Per-claim verdicts

| Claim | Candidate location | Verdict and decisive check |
|---|---|---|
| Frozen Fourier coefficient and local coefficient one | C 11–18, 82–113; R4 69–109 | PASS. The two heat integrals give exactly the frozen coefficient and unit local singularity. |
| Integrable force, finite divergence measure, positive Coulomb atom and periodic compensation | C 84–140; R4 113–194 | PASS. The integrability margin is `d-s-1>=1`; punctured flux and Fourier coefficients identify the atom and negative constant separately. |
| Admissible constants a and kappa, with no heat or N dependence | C 115–140 | PASS. The lower bounds follow from a smooth external potential and the bounded negative part of the exact divergence. |
| Nonnegative shifted energy, including every partial/simultaneous collision | C 147–180 | PASS. Every shifted pair term is nonnegative, and any colliding pair independently drives the sum to infinity. |
| Full drift is exactly the energy's negative gradient | C 182–188 | PASS. Both coordinates of each unordered pair produce the stated `1/N` force. |
| Full Laplacian coefficient `2/N`, drift square and all triple terms | C 190–227 | PASS. Coordinate Taylor extraction and separately assembled forces agree; omitting the second Laplacian contribution fails the negative-control checks. |
| Local construction, continuation and measurable maximal map | C 231–237 | PASS. Smooth cutoff Picard equations, compatibility before exits, countable patching and compact continuation suffice. |
| Energy stopping, fixed-start martingale integrability and exact stopped identity | C 239–287 | PASS. The stopped integrand has a deterministic bound on a fixed compact energy sublevel. High-energy immediate stops are handled explicitly. |
| Nonexplosion before the positive-minimum-distance conclusion | C 246, 281–289, 373–381 | PASS. The energy-exit probability tends to zero before compactness of an already global path is used. |
| Pathwise uniqueness and uniqueness in law | C 289 | PASS. Any competitor agrees through each compact cutoff exit; the measurable global construction exhausts finite horizons. |
| Random initial states with finite energy mean | C 293–300 | PASS. On the high-initial-energy event the stopped integrand vanishes; on its complement the same deterministic compact bound applies. |
| Fatou, then integrable full drift, then true global martingale | C 302–327 | PASS. The order is noncircular and establishes the necessary expected bracket bound before un-stopped expectations are taken. |
| Exact global expectation equality and treatment of zero diffusion | C 327–345 | PASS. The global martingale is square integrable; no unwarranted uniform integrability of stopped energies is assumed. At zero diffusion the weighted Q term is identically zero. |
| Explicit distance-exit bounds and deterministic zero-noise separation | C 347–381 | PASS. A single minimizing pair controls the event; no missing pair-count factor or prior deterministic positive separation is used. |
| Bounded-density energy input and sharper iid initial-energy bound | C 383–400 | PASS. The zero mean of g and nonnegative shift give the displayed Haar integral; one iid variable can be integrated using its density bound. |
| Per-start exceptional sets, joint Borel kernels and deterministic Markov identity | C 402–423 | PASS. Joint measurability permits integration of state-dependent null exceptional events against the current-state law. |
| Full-family same-noise heat convergence | C 425–469 | PASS. Local C1 convergence, a path-dependent collision-free neighborhood, exact noise cancellation and a stopped Gronwall bound give the entire epsilon limit. |
| Exact N-particle divergence exponent | C 471–487 | PASS. Ordered label counting gives `N a+(N-1) kappa`, not the pair-process exponent. |
| Pathwise smooth random-flow diffeomorphism and Jacobian | C 489–514 | PASS. Backward solution gives the inverse; spatial differentiation has no Brownian derivative or additional Itô term. |
| Continuous-test passage, Borel measure domination and density | C 516–535 | PASS. Bounded convergence is used only for continuous terminal tests before open-set approximation and Haar outer regularity. |
| Fixed-N limitations and separation from corrector-domain claims | C 537–544, 569–584; T 3, 11–19 | PASS. The theorem keeps its density cost, path-dependent heat constants, and corrector exclusions visible. |

**First failed line: none. Required repair: none.** The following reconstructions explain the analytic verdict rather than relying on the table or computation count.

## Kernel preflight and complete finite-N algebra

For `0<p<d`, put `alpha=(d-p)/2`. The supplied heat representation multiplies the periodized Gaussian integral by

`A=4^alpha pi^(d/2)/Gamma(p/2)`.

Its nonzero Fourier coefficient is

`A Gamma(alpha)/(4 pi^2 |k|^2)^alpha = pi^(p-d/2) Gamma((d-p)/2)/Gamma(p/2) |k|^(p-d)`.

Independently substituting `v=|z|^2/(4t)` into the single Gaussian integral gives `|z|^(-p)` with coefficient one. The zero mode vanishes. Small-time nonzero lattice translates have exponentially decaying derivative bounds; the subtracted constant has an integrable `t^(alpha-1)` weight. At large time the torus remainder decays exponentially and the single Gaussian term has integrable `t^(-p/2-1)` decay. Differentiation on a ball of radius below `1/3` is therefore justified. This establishes the smooth local remainder used by C, not merely a formal Fourier asymptotic.

The force has singularity `s z |z|^(-s-2)` and is integrable since `s+1<d`. The boundary term for taking one distributional derivative of g is bounded by a constant times `r^(d-1-s)` and vanishes. For the divergence of K, the inner flux is

`s r^(d-s-2) integral_(S^(d-1)) psi(r theta) dS(theta)`.

Below Coulomb it vanishes, and the classical density is locally integrable. The gamma recurrence then yields `D=s(d-2-s) g_(s+2) dx`. At Coulomb the flux tends to `c_d psi(0)`, where `c_d=(d-2)|S^(d-1)|`. Nonzero Fourier modes have coefficient `c_d`, while the zero mode has coefficient zero. Thus `D=c_d(delta_0-dx)`. It follows that the punctured equality is `Delta g=c_d`, whereas the heat divergence is `D_epsilon=c_d(p_epsilon-1)`. Omitting either component would fail the source normalization and the later density argument. The independent checker verifies the gamma identities exactly for integer dimensions 3 through 9; the preceding recurrence proves the general admitted real-exponent statement.

The needed consequence of R4 is therefore independently verified here: a finite measure lower bound `D>=-kappa dx` and the punctured upper bound `Delta g<=kappa`. The lower bound survives convolution with the nonnegative probability kernel. No response-operator conclusion is used.

For the full system, each unordered pair contributes `N^(-1) grad g(x_i-x_j)` to the energy gradient in coordinate i and its negative in coordinate j. Oddness of K therefore gives exactly `B=-grad H_N`. Taking both coordinate Laplacians yields

`Delta H_N=sum_i Delta V(x_i)+(2/N)sum_(i<j) Delta g(x_i-x_j)`.

There are `N(N-1)/2` unordered pairs, so the upper bound is `C_N=N a+(N-1) kappa`. Defining `Q_N=C_N-Delta H_N` gives the pointwise nonnegative function required by the stopped argument. The generator and energy-martingale bracket are consequently

`L E_N=nu C_N-|B|^2-nu Q_N`,

`d<M>_t=2 nu |B(X_t)|^2 dt`.

The two factors of 2 have different origins: two coordinate derivatives for the Laplacian, and Brownian variance `2 nu` for the bracket. Both survive the independent relative-coordinate check.

The complete square contains the background square, background-force cross terms, the unordered pair-square coefficient `2/N^2`, and all ordered distinct triple terms. It is not replaced by any of its pieces. The symmetric triple witness below confirms that negative cross terms matter even for a repulsive singular principal force. The proof needs only the nonnegativity of the complete square.

## Energy coercivity and the order of the probabilistic argument

The infimum g_* is finite, attained away from zero, and negative. This follows from the limit of g to positive infinity at zero, smoothness elsewhere, zero mean and nonconstancy. With `v_*=min V`, the shift is exactly

`E_N=H_N-N v_*-(N-1)g_*/2`.

Expanding it gives a sum of `V(x_i)-v_*` and `(g(x_i-x_j)-g_*)/N`, each nonnegative. Thus one colliding pair cannot be concealed by another pair, the external potential, a negative smooth remainder, a disjoint cluster, or a force cancellation. Every energy sublevel is compact inside the collision-free configuration space. With the candidate's `r0=1/4` and `A=1+sup_(|z|<=r0)|h_s(z)|+|g_*|`, one minimizing pair yields

`E_N(x)>=(delta(x)^(-s)-A)/N` when `delta(x)<=r0`.

This is the exact estimate needed for both energy and distance exits.

The local construction uses smooth forces that agree with K beyond a prescribed collision tube. Subtracting the continuous additive driving signal reduces each cutoff equation to a globally Lipschitz deterministic integral equation. Picard series converge by factorial bounds; the solution is nonanticipating and Borel in its parameters. Local uniqueness gives compatibility. Countably many compact exits patch these solutions to a maximal path in the collision-free space. This reconstruction is independent of the R5 pair theorem.

If a finite-lifetime path remained in a fixed compact subset of that space, its drift integral and its continuous driving signal would have a limit; a finer cutoff would continue it. Hence approaching collisions is the only finite-lifetime obstruction. Since bounded energy forces a fixed positive distance from every collision, the increasing energy exits exhaust the lifetime. This justifies C line 246 without already assuming noncollision.

For fixed R and initial energy below R, all derivatives in the energy Itô identity and its stochastic integrand are bounded on a deterministic compact set. At the stop, continuity gives terminal energy R. If initial energy is already at least R, the stop is zero and the stochastic integrand vanishes. Thus the stopped integral is square integrable, and every expected identity before removing the stop is legitimate. In particular,

`P(sigma_R<=T)<=min(1,(E_N(x)+nu C_N T)/R)`.

Sending R to infinity gives zero probability of finite lifetime. Only after this conclusion does continuity on a compact time interval imply a strictly positive minimum separation. The proof has the required order; it never assumes this minimum to prove global existence.

For an independent initial law with finite `J0=E E_N(X0)`, the same bounded stochastic-integrand argument applies, since the high-initial-energy event has an immediate stop. The stopped terminal energy on that event may be unbounded, but its expectation is at most the admitted J0. This separates the two integrability issues correctly.

After noncollision, the nonnegative stopped energy, dissipation and weighted Q occupation have the Fatou bound

`E E_N(X_t)+E integral_0^t |B|^2+E integral_0^t nu Q_N <= J0+nu C_N t`.

The expected drift square is now integrable in time. Consequently the global energy martingale is square integrable, with expected bracket at most `2 nu(J0+nu C_N T)`. The brackets of the omitted stopped intervals tend to zero by dominated convergence of an integrable time occupation. Thus the stopped martingales converge in L2 to the global one. Alternatively, pathwise localization identifies the same global identity on each finite horizon. All terms are integrable, so expectation gives exact equality. No equality is inferred directly from Fatou and no separate, unproved uniform integrability of stopped energies is required.

When `nu>0`, integrability of Q occupation also gives integrability of the absolute Laplacian occupation from `Delta H_N=C_N-Q_N`. When `nu=0`, the term `nu Q_N` is identically zero as an integrand, and the pathwise identity is ordinary energy dissipation. There is no division by zero or assertion that the unweighted Q occupation has finite expectation at zero diffusivity.

At a distance exit with `rho^(-s)>A`, the shifted energy is at least `(rho^(-s)-A)/N`. Applying the same bounded localization yields

`P(inf_(0<=t<=T) delta(X_t)<=rho)<=min(1,N(J0+nu C_N T)/(rho^(-s)-A))`.

The simpler bound `min(1,2N(J0+nu C_N T)rho^s)` has exactly the additional restriction stated by C. A union bound is neither used nor needed. The bound involving the pathwise energy supremum, and its deterministic initial-energy specialization at zero diffusion, both follow with the stated constants.

Finally, `integral E_N dm_N=N(integral V-v_*)-(N-1)g_*/2` is finite because g is integrable and zero mean. A bounded F0 therefore has finite J0 before any propagated density result is used. For iid density bounded by M, integrating one pair variable first bounds each nonnegative shifted pair energy by `M(-g_*)`, giving the candidate's sharper initial-energy estimate. This does not improve the evolved configuration-density factor `M^N`.

## Measurability, heat passage and density

The measurable cutoff paths and their exits define a jointly Borel maximal map with a cemetery convention. At each fixed start its nonexplosion event has probability one. A Borel continuous-path version can be obtained by using the actual continuous path on that event and the constant initial path on its complement. For a fixed starting state this changes only a null event; the adapted construction itself remains the local nonanticipating map. No exceptional set uniform over uncountably many starts is asserted or needed.

At a deterministic restart time, local uniqueness gives the restart identity up to lifetimes. Brownian future increments are independent of the past. Conditional on the present collision-free state, the measurable future construction fails with probability zero at that state. Integrating that jointly measurable indicator against the current-state distribution still gives zero. This is sufficient for the displayed deterministic-time conditional Markov property and semigroup law. Neither strong Markov assertions nor merely formal generator identifications are being substituted.

For heat approximation, split K into a smooth periodic part agreeing with K near a fixed collision-excluded compact set and an L1 remainder supported a positive distance away. The smooth part converges in C1 under heat convolution. For the distant part, each needed Gaussian derivative is bounded by a polynomial in `epsilon^(-1)` times `exp(-c/epsilon)` on the target set; multiplication by the L1 norm gives convergence. Thus the actual force converges locally in C1, which is stronger than distributional convergence.

Fix a noncolliding singular path and choose `eta` below its positive minimum separation and at most `1/8`. Use identical Euclidean lifts initially. Before the maximal particle displacement between the heat and singular paths reaches `eta/4`, every interpolating pair difference remains at least `eta/2` from a lattice collision. Subtracting the equations cancels Brownian increments exactly. The force error is at most `(N-1)e_epsilon/N`, and the Lipschitz factor is exactly the candidate's

`||Db||infinity+[2(N-1)/N]sup ||DK_epsilon||`.

Gronwall gives `T(N-1)e_epsilon exp(LT)/N`. For every sufficiently small epsilon this is below the stopping threshold, preventing the stop. Since this is a deterministic comparison on the singular good event, it proves the full epsilon-family limit there, without taking a sequence or intersecting uncountably many exceptional events. The constants depend on that path through eta. No global heat noncollision estimate or uniform-in-N rate is required.

The smooth heat drift has full divergence

`sum_i div b(x_i)+(1/N)sum_i sum_(j!=i)D_epsilon(x_i-x_j)>=-C_N`.

For each continuous driving path its smooth flow is a C1 diffeomorphism of the full N-particle torus. Spatial difference quotients satisfy the usual linear variational equation with bounded coefficients; solving the original integral equation backward with the same continuous signal gives the inverse. The initial-coordinate derivative of the additive signal is zero. Hence the determinant is the positive exponential of the integrated full drift divergence and is at least `exp(-C_N t)`. This remains valid when diffusion is zero.

Change of variables for this actual smooth diffeomorphism bounds the pushforward of Haar by `exp(C_N t) dm_N`, path by path. Multiplying by the bounded initial density and using Tonelli proves the heat-law bound. The singular law is already a defined probability measure through the Borel kernel. For continuous terminal tests, same-noise convergence and bounded convergence in both Brownian path and initial state pass that bound to the singular law. The collision set is initial-Haar-null.

To pass from continuous tests to Borel sets, the continuous functions `min(1,j dist(z,O^c))` increase to the indicator of any proper open set O; the whole-space case uses the constant function. Monotone convergence gives the open-set bound. Open supersets whose Haar masses decrease to a Borel set's Haar mass then give the same domination on that set. Thus the singular law is absolutely continuous and has precisely the claimed density bound. No convergence for arbitrary Borel terminal tests, singular-source expectations, singular-flow surjectivity or singular Jacobian is assumed.

## Independent exact checks and attempted falsifications

The companion checker was written in this isolated context without reading the candidate checker. It uses raw scalar perturbations `x -> x+t e_a` and extracts the coefficients through order two from the energy using the binomial series. A separately assembled coordinate force, ordered divergence and complete force-square expansion provide the comparison. All transverse coordinate perturbations are included even when test points are collinear. Exact fractions, exact integer roots and symbolic powers of pi are used; there is no simulation, numerical tolerance or random seed.

The run under Python 3.9.6 passed **4,910 exact checks across 132 differential configurations**. Repeated consistency assertions are included in that count; the count is supporting evidence rather than a mathematical-certification metric. The configurations include N=2, N=3 and N=4, dimensions 3 through 6, Coulomb and strict sub-Coulomb exponents including the noninteger exponent `s=1/2`, a noncollinear 3-4-5 triangle, symmetric triples and disjoint close pairs. Zero and nonzero smooth even remainders and external gradient backgrounds are tested. Those local polynomials test algebra only; they are not substituted for the frozen Riesz remainder or the periodic V in the theorem. Their finite local jets can be realized by smooth periodic extensions.

| Independent check group | Result |
|---|---|
| Energy coordinate derivative versus full force | 1,848 exact equalities |
| Raw full Laplacian, independently counted divergence and complete ordered triple square | 132 checks for each group |
| Deliberately missing second pair derivative | Rejected in all 100 cases with nonzero pair Laplacian sum |
| Energy generator, including zero diffusion | 396 checks |
| Exact gamma/Fourier ratios and Coulomb coefficient | 21 below-endpoint identities and 7 endpoint identities |
| Coulomb particle compensation, Q=0 and divergence sign | 28 checks for each group |
| Zero and nonzero Fourier-mode compensation | 3 checks |
| Full density exponent | 12 checks |
| Triple cancellation, nonzero individual pair forces, negative cross term and energy blowup coefficient | 15 checks for each group |
| Disjoint close-pair energy lower bound | 15 checks |
| Zero-noise relative integral and energy dissipation | 15 checks for each group |
| Relative Brownian diffusion factor | 90 checks |

The following witnesses make the falsification tests concrete.

For the coefficient-one Euclidean principal kernel with `d=3,s=1,N=3` and positions `(-rho,0,rho)` on an axis, at `rho=1/64` the middle particle's total drift square is zero. Its two individual drift-contribution squares sum to `33554432/9`, and its ordered cross term is exactly `-33554432/9`. The full energy is `160/3` and the full drift square is `52428800/9`. This refutes deleting those middle cross terms or controlling each of that particle's pair-force squares by its total drift. It does not, by itself, disprove every conceivable separate global coercivity estimate, and no such estimate is asserted here. The candidate retains the full square throughout.

Along the entire symmetric triple family, the principal energy satisfies `3 H rho^s=2+2^(-s)` and diverges as rho tends to zero. For two disjoint close pairs in the same local chart at `N=4,s=1,rho=1/128`, the exact principal energy is `69566/1023`, at least the close-pair contribution 64. Bounded smooth remainders cannot remove either divergence. These tests challenge simultaneous-collision coercivity independently of force-square positivity.

For the zero-noise two-body principal model, direct radial integration gives `r(t)^(s+2)=r(0)^(s+2)+2s(s+2)t/N` and direct energy differentiation gives `dH/dt=-2s^2 r^(-2s-2)/N^2`. The actual two-particle system has N=2. Additional N=3 and N=17 occurrences in this relative-coordinate diagnostic test only the coefficient `1/N`; they are not alternative N-particle models. The noisy relative generator has diffusion `2 nu`, and its energy action agrees exactly with the full-coordinate calculation.

At periodic Coulomb with constant V, the exact divergence measure forces `Delta H_N=(N-1)c_d`, so `Q_N=0` for the displayed minimal choices of a and kappa. The energy input is exactly `nu(N-1)c_d t`. The singular deterministic flow then has negative divergence off collisions, but the candidate does not claim that it maps the punctured configuration space onto itself. Only smooth heat flows are used for the surjective change of variables. Thus this apparent volume-contraction challenge does not contradict its proof or probability conservation.

The analytic falsification checks targeted possible circular noncollision reasoning, an unbounded random-initial-state martingale integrand, replacing Fatou by equality, state-dependent exceptional sets at restart, full-family epsilon quantifiers, and passing a continuous-test inequality directly to arbitrary Borel expectations. Each of these potential failures is explicitly blocked by a supplied step of the candidate; none requires a new assumption or repair.

## Constants and exact limits of the accepted claim

| Quantity | Allowed dependence and consequence |
|---|---|
| `g_*`, local remainder bound, kappa | Frozen d,s and Fourier normalization; independent of N, nu and heat parameter |
| `v_*`, a | Fixed smooth periodic V; `a=max(0,sup Delta V)` is admissible |
| `C_N=N a+(N-1) kappa` | Linear in N for fixed data; controls both energy input and density exponent |
| Energy shift | Exactly `N v_*+(N-1)g_*/2`; no configuration or path dependence |
| `A` and `r0` | `r0=1/4`; A depends only on the fixed kernel and the stated local chart |
| J0 | Fixed initial energy or mean shifted energy; finite for every bounded initial density |
| Haar initial-energy integral | `N(integral V-v_*)-(N-1)g_*/2`; finite without propagated density |
| Energy and exit estimates | Explicit dependence on N, J0, nu, C_N and horizon; not uniform over arbitrary initial configurations or unbounded nu |
| Path separation | Random at positive diffusion; deterministic from initial energy at zero diffusion |
| Heat comparison | Fixed tuple/start/horizon; constants may depend on the realized minimum separation; no uniform rate |
| Density | `||F0||infinity exp(C_N t)`; exponent independent of finite nu and heat parameter but not N |
| iid density | Initial configuration bound `M^N`; no uniform iid-moment conclusion |

The only newly established global square occupation is that of the complete interacting drift. An individual pair-force square can be nonintegrable under Haar, and a bounded density bound does not change that integrability threshold. Local smooth Itô calculus on compact collision-excluded sets does not make an arbitrary bounded Borel or Haar-L2 corrector differentiable. These exclusions are accurately retained by C lines 537–584 and T line 19.

## Artifacts, verification and handoff

Created in this isolated worktree only:

- `AUDITS/HOSTILE/ROUND_006_PARTICLE_REVIEW.md` — this complete report.
- `AUDITS/HOSTILE/round006_particle_hostile_exact.py` — independent exact checker.
- `AUDITS/HOSTILE/round006_particle_hostile_exact_output.json` — reproducible results, group counts, parameter cases and witnesses.
- `AUDITS/HOSTILE/ROUND_006_PARTICLE_HOSTILE_INPUT_SHA256SUMS.txt` — identical eight-input seal.
- `AUDITS/HOSTILE/ROUND_006_PARTICLE_HOSTILE_OUTPUT_SHA256SUMS.txt` — report, checker, JSON and input-manifest seal; the manifest does not hash itself.

Verification commands, run from the worktree root:

```text
python3 AUDITS/HOSTILE/round006_particle_hostile_exact.py
shasum -a 256 -c AUDITS/HOSTILE/ROUND_006_PARTICLE_HOSTILE_INPUT_SHA256SUMS.txt
git diff --check
shasum -a 256 -c AUDITS/HOSTILE/ROUND_006_PARTICLE_HOSTILE_OUTPUT_SHA256SUMS.txt
```

The exact checker passed. All eight inputs passed both the initial source/copy verification and the final input-seal verification. The output seal passed verification. `git diff --check` passed; untracked report/code/JSON were additionally checked for terminal newline, trailing whitespace and control characters. The worktree HEAD was verified against the prescribed R4 base. No TeX was created or modified; this task's report is Markdown and the final handoff contains no mathematical LaTeX. No unrelated campaign tests or prior checkers were run.

**Final audit disposition: PASS AS STATED, with no failed line and no candidate repair.** The report and companion artifacts are immutable upon issuance under their SHA-256 output seal. Any later change in verdict requires a new report. The next authorized root action is comparison with the separately isolated reconstruction and this sealed hostile review, followed by root-owned canonical integration. The first corrector-domain assertion remains outside this verdict.
