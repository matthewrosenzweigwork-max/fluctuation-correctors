# AUD054 — hostile review of the entire THM039 construction

TASK-083. Issued 2026-09-18 UTC. Fresh isolated hostile reviewer, `/root/r017_gaussian_hostile`. Prescribed worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r017-gaussian-hostile`; branch `codex/hocf-r017-gaussian-hostile`; exact base `072cab684b9ce41855ead6c48f435c8fc184ec35`.

**Verdict: PASS AS THE COMPLETE CONDITIONAL IMPLICATION STATED BY THE CANDIDATE.** No failed mathematical line or admitted counterexample was identified. The entire frozen THM039 assertion, including its quantitative approximation and full finite-dimensional joint law, follows from the expressly conditional complete source premises. This report does not discharge the separate THM038 gate, certify historical source gates, assign a blind-reconstruction result, or promote THM039. Root comparison with both required independent axes and matching source gates remains necessary.

The target and candidate were not repaired, weakened, edited, or supplemented by a different theorem. The calculations below are verification of the mechanisms already present in the candidate. In particular the Gaussian-smoothing probability passage is present in the candidate itself, rather than a repair supplied by this review.

## 1. Exact scope and negation

The reviewed assertion has integer dimension d at least three, exponent 0 < s <= d-2 with the additional strict inequality s < d/2, unit Haar torus, the positive coefficient-one periodic Riesz kernel, K = -grad g, zero external drift, ordered interaction coefficient 1/N, and actual singular particles with iid Haar initial positions independent of the Brownian drivers. Inverse temperatures are positive and finite, with beta_N N^(s/d-1) tending to a positive finite limit. A finite T, a positive integer m, deterministic times in [0,T], and arbitrary fixed real smooth tests are fixed before N varies.

With b_N = min(beta_N,1) and sigma_N = sqrt(N b_N), each vector component is sigma_N times the empirical test minus its Haar integral. Its claimed limit is the centered possibly degenerate Gaussian whose covariance is

    C_ij = integral (S_(t_i)h_i - mean(h_i))
                    (S_(t_j)h_j - mean(h_j)) dx,
    S_t e_k = exp(-t D_s(k)) e_k for k != 0,
    D_s(k) = 4 pi^2 c_(d,s) |k|^(s+2-d),
    c_(d,s) = pi^(s-d/2) Gamma((d-s)/2) / Gamma(s/2).

Constants are unchanged by S. The one-body marginal is asserted to be exactly Haar at each deterministic time. For each component, the claimed expected absolute error from the normalized sum of the fixed initial tests is bounded by

    C [N^(s/d-1/2) + sqrt(nu_N) + nu_N],  nu_N = 1/beta_N,

on an eventual critical tail. Constants may depend on the fixed data and positive upper/lower bounds for the critical coupling on that tail, but not N. No counterterm is present.

The exact negation is existence of admitted fixed data and a critical sequence violating at least one of the exact centering, quantitative approximation, or joint weak-limit assertions. A failed estimate would not be this negation. Neither a clustered exchangeable law nor a test changing with N is admitted. The present conditional proof excludes this negation conditional on its full supplied premises; it does not assert that an open source gate has already passed.

## 2. Input, source, and exposure preflight

The task and supplied manifest were read first. The prescribed worktree was created from the exact base, and only the fourteen prescribed byte strings were copied as inputs and independently hash-checked before mathematical inspection. The input manifest SHA-256 is `0d4c561dbad0cde60df0122092d3a5bfdb70419053d129f7662bdf98f4677bf7`. The full path/digest list, exact input copies, and initial verification record are in the companion packet.

| Permitted file | Material actually inspected and use |
|---|---|
| `AGENTS.md` | Entire file. Mathematical discipline, exact coefficients and singular passages. The bounded task's explicit isolation/no-commit/no-canonical-edit directions supersede general state/orchestration-reading instructions. |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Entire file. Unit torus/Haar/Fourier convention, coefficient-one Riesz, ordered deleted labels and N-power denominator, noise and law classes. |
| `MEMORANDA/ROUND_001_ALGEBRA.md` | Sections 1–2, with heading/status inventory elsewhere. Its smooth exact identity is a comparison only; the singular first-order formula is recomputed here from ordered sums. No smooth diagonal convention is transferred to the singular kernel. |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md` | Sections 1–4 and heading/status inventory. Local coefficient-one heat representation, integrable force, full finite compensated divergence measure and sign of the Haar response. Its issued PROVED_CANDIDATE / SELF_CHECKED status is retained. |
| `THEOREMS/THM-026_FINITE_N_SINGULAR_PARTICLE_REALIZATION.md` | Entire card, including OPEN / UNAUDITED / VERSION_LOCKED and every fixed-N limitation. The card is not a proof. |
| `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md` | Sections 1–8. Actual noncolliding jointly measurable unique paths, fixed-start quantifiers, energy localization, and same-noise heat passage. Its construction status remains as issued; no uniform-N path-convergence or density estimate is imported. |
| `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md` | Sections 1–3 and heading/status inventory. Actual smooth free energy, fixed-N Fatou passage, and the uniform actual pair-energy moment. No corrector, reference-law, tail, noise or conditional R9 result is used. |
| `THEOREMS/THM-038_FULL_SUBCOULOMB_COULOMB_QUADRATIC_SOURCE.md` | Entire card. Actual-law absolute source bound for every N, every bounded diffusivity including zero, and every deterministic time for each fixed smooth terminal test. The separate gate stays open in this input. |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md` | Entire 544-line construction. Checked the kernel/actual-energy/positive-splitting/commutator/remainder interface, all terms of the source estimate, its uniformities and exclusions. It is a complete expressly conditional source, not a theorem inferred from a card. The extra initial-mode derivative is not a premise. Its diagnostic descriptions were visible in the permitted text, but no program, results file, audit or archive from that source was read or reproduced. |
| `THEOREMS/THM-039_CRITICAL_FINITE_DIMENSIONAL_HOMOGENEOUS_GAUSSIAN.md` | Entire frozen assertion and negation, including quantitative error, zero/repeated times, constants, arbitrary smooth real tuple, singular covariance and exclusions. |
| `TASKS/ACTIVE/TASK-083_ROUND017_FINITE_DIMENSIONAL_HOSTILE.md` | Entire bounded assignment. |
| `MEMORANDA/ROUND_017_CRITICAL_FINITE_DIMENSIONAL_GAUSSIAN.md` | Entire 120-line candidate. All mathematical steps and the exposure paragraph reviewed; no candidate checker opened. |
| `MEMORANDA/ROUND_017_GAUSSIAN_ARTIFACTS/EXPOSURE.md` | Entire attestation. Records constructor exposure and earlier unsolicited progress summaries; not independent evidence that the asserted chronology occurred. |
| `MEMORANDA/ROUND_017_GAUSSIAN_ARTIFACTS/SOURCE_PREFLIGHT.md` | Entire mapping. Checked against the actual permitted source texts and current seals. |

No external literature claim, theorem number, private source or novelty claim is used. The probability and Fourier arguments needed here are given in the candidate and reconstructed below. Conditionality applies to the exact complete local modules supplied, not unseen theorems.

The automatically supplied ambient instructions included a high-level memory summary and the user/global campaign instructions. No memory file was opened and no memory-derived mathematical fact was used. The initial delegated task contained the assignment and the conditional R16 status, but no proof. This is a fresh hostile context, exposed to the full candidate as required; it is not a statement-only blind reconstruction. The allowed candidate/exposure text itself discloses unsolicited TASK082 summaries (conditional closure and Gaussian smoothing). Those disclosures were seen; no worker proof, checker, results, current state/history, R11–R15 proof/audit, root scratch, or other worktree output was opened. Their truth is not used in the proof verdict.

## 3. Source interface: actual law and the full singular range

The heat representation in R4 gives local g(z) = |z|^(-s) plus a smooth remainder. Since s+1 < d throughout 0 < s <= d-2, K is an integrable odd field. Its full divergence is

    D = s(d-2-s) g_(s+2)(z) dz               for s < d-2,
    D = c_d (delta_0 - dz)                   for s = d-2,
    c_d = (d-2) |sphere_(d-1)| = 4 pi^2 c_(d,d-2).

Below Coulomb the boundary flux vanishes and the density is integrable. At Coulomb the inner-boundary flux is c_d times evaluation at zero. The nonzero Fourier coefficients and zero total mass identify the compensating term as precisely minus c_d Haar. The gamma recurrence gives 4 pi^2 c_(d,s)/c_(d,s+2) = s(d-2-s) only below Coulomb; it is not used with a zero endpoint factor. This verifies the normalization used in the response and in S.

R6 constructs actual fixed-N paths by cutoff patching and the shifted total energy. With zero external drift,

    H_N = (1/N) sum_(i<j) g(X_i-X_j),
    B = -grad H_N,
    Delta_(Nd) H_N = (2/N) sum_(i<j) Delta g <= (N-1) kappa.

Every shifted pair-energy summand is nonnegative, so any partial or simultaneous collision leaves every bounded energy sublevel. Stopped Itô expectations give nonexplosion and noncollision. The complete drift square, not individual pair-force squares, is used. The stated joint measurability handles random iid initial states and fixed translations by integration; no common exceptional set for all uncountably many states is needed. A continuous collision-free finite-N path on a compact time interval has positive minimum separation. Same-noise heat paths converge by localized ordinary Gronwall; constants may depend on that path and N.

The actual-law energy sign in R10 Section 2 and R16 Section 3 has the correct direction. At a fixed smooth cutoff and positive noise, differentiating entropy plus energy gives

    d/dt [nu Ent(F_t) + E H_N] =
       -integral F_t |grad H_N + nu grad log F_t|^2 <= 0.

Both initial terms are zero for iid Haar, and entropy is nonnegative on a probability space of mass one. Thus the smooth expected energy is nonpositive. After subtracting the common fixed-N lower bound (N-1)g_*/2, Fatou and same-noise path passage preserve the inequality for the singular energy. This also proves absolute integrability, since the energy is bounded below. At exactly zero noise the actual deterministic energy decreases directly. Exchangeability consequently yields

    E g(X_1-X_2) = 2 E H_N/(N-1) <= 0,
    E |g(X_1-X_2)| <= 2 |g_*|.

The local expansion then controls the actual expectation of 1 + dist(X_1,X_2)^(-s), uniformly in N, bounded diffusivity and deterministic time. This is the required occupation integrability. No positive-time product law or uniform-N density domination is used. The fixed-N exponential density bound exists in R6 but is unnecessary for the present first-order passage.

The complete R16 source supplies exactly the claimed rate, not only an expectation without an absolute value. Its retained kernel has positive Fourier coefficients and zero mean; its omitted heat kernel Q_r is pointwise nonnegative with Haar mass c_r. The deterministic identity is

    H_N/N = E_r + S_r - g_r(0)/(2N) - (N-1)c_r/(2N),
    E_r >= 0, S_r >= 0,
    E E_r + E S_r <= C [N^(-1) r^(-s/2) + r^((d-s)/2)].

The factors use ordered N(N-1) pairs and the retained smooth self value only. The singular self value is never assigned. For the retained Fourier weights, their logarithmic slope is bounded by 2(alpha+M), with alpha = (d-s)/2 and M = d+2, uniformly in r. The resulting commutator is bounded by a fixed finite Fourier seminorm of the velocity times E_r. The Gaussian derivative comparison dist(z,0)|grad p_u(z)| <= C p_(2u)(z), the geodesic velocity difference, and the substitution a=2u give |J_(g-g_r)| <= C Q_(2r). Its full deleted/background statistic is controlled by S_(2r) and c_(2r), with all original contractions retained. Choosing r=N^(-2/d) balances the two powers at N^(s/d-1).

I checked these mechanisms against Sections 2–7 of the complete source. There is no weighted-kernel positivity claim, simultaneous N/heat limit, source-square estimate, or loss at the Coulomb endpoint. The test seminorm is uniform for the exact backward test over 0 <= nu <= nu_* and the fixed time interval, including arbitrary smooth h. R16's derivative-at-zero test is not needed and its correctness is not a condition of this THM039 implication. The separate full R16 gate remains a separate administrative and mathematical prerequisite to promotion.

## 4. Independent first-order coefficient and stopped-passage check

For a fixed terminal time t and real smooth h, put f_r = S_(t-r) exp(nu(t-r)Delta)h. Its mean is mean(h). The nonzero frequency multiplier has derivative in r equal to (nu 4 pi^2 |k|^2 + D_s(k)) times itself. Hence

    partial_r f_r + nu Delta f_r + R f_r = 0,
    R f(x) = -integral f(x+w) D(dw).

The multiplier D_s(k) is bounded over nonzero lattice frequencies because s+2-d <= 0. The additional diffusion multiplier costs two derivatives. Absolute Fourier sums of a fixed smooth h bound every required spatial and time derivative uniformly over bounded nu and the fixed horizon. No regularizing effect of S at high frequency is assumed; at Coulomb it has none beyond scalar damping.

For x != y, set J(x,y) = K(x-y) dot(grad f(x)-grad f(y)). This is symmetric. Its Haar row is obtained directly:

    j(x) = -integral K(x-y) dot grad f(y) dy
         = integral K(w) dot grad f(x+w) dw
         = -integral f(x+w) D(dw) = Rf(x).

The first missing term is zero because integral K=0. The last step is a distributional pairing of an integrable force and a smooth test; it includes the Coulomb atom. The double contraction is integral Rf=0 because D has total mass zero. Thus the finite-label symmetrization is exactly

    (1/N^2) sum_(i!=j) K(X_i-X_j) dot grad f(X_i)
      = (1/(2N^2)) sum_(i!=j) J(X_i,X_j)
      = P_N[J] + eta_N[Rf].

There is no (N-1)/N correction to the response: the Haar row is already multiplied by eta_N with coefficient one in the definition of P_N. There is no diagonal trace to restore and no use of a falling-factorial denominator. The backward equation cancels this response after adding the ordinary one-body diffusion and time derivatives. The resulting stopped identity has coefficient plus one on P_N.

The local gradient difference supplies |J(x,y)| <= C(1 + dist(x,y)^(-s)). At fixed N, exchangeability and the actual pair bound in Section 3 imply finite expectation of its absolute integral over time, and the response row is bounded. Therefore the cancelled drift, not the unsymmetrized singular individual-force magnitude, has an integrable majorant on probability times time. This distinction is essential and is respected in candidate lines 33–47.

Use any increasing collision-excluded localizations of the actual path. They eventually exceed each fixed finite horizon almost surely by the supplied noncollision and positive minimum separation. For each localization the smooth empirical observable admits ordinary Itô calculus. Its endpoints converge by bounded convergence. Dominated convergence on probability times time passes the symmetrized drift in expected absolute value; bounded gradients pass the stochastic integral in mean square. The stochastic integral is therefore a true square-integrable martingale with

    M_t = sqrt(2nu)/N sum_i integral_0^t grad f_r(X_i(r)) dot dW_i(r),
    bracket(M)_t = (2nu/N) integral_0^t eta_N(r)[|grad f_r|^2] dr.

The cross bracket for two tests on possibly different horizons has the same coefficient, integrated to the minimum horizon, with the dot product of their backward gradients. Independent particle Brownian motions remove mixed-particle traces, not the two-test same-particle cross bracket. A cross-bracket limit is not needed because all scaled martingales vanish componentwise.

This verifies candidate (A) in the actual singular model. It uses no pair-corrector regularity or singular Itô formula for a pair observable. At Coulomb Rf = -c_d(f-mean(f)); replacing D by its punctured classical density would give the wrong response. At zero noise the stochastic integral vanishes and the identical localized drift argument applies.

## 5. Centering and critical approximation

For each fixed translation a, local uniqueness makes the shifted path from x+a equal to the path from x plus a, with identical Brownian increments, outside a null set for each fixed starting state. Joint measurability and integration over the independent iid initial vector suffice; no intersection over uncountably many a or starts is necessary. The initial joint law is invariant under common translation. Each time marginal is therefore invariant under every fixed a. Its Fourier coefficient at a nonzero k equals itself times exp(2 pi i k dot a); selecting a nontrivial phase makes it zero. Trigonometric-polynomial density identifies that probability law with Haar. This proves the centering in the frozen statement exactly, without factoring any higher marginal.

Put theta=1-s/d. It is positive, and on a tail with 0 < L <= lambda_N <= U < infinity,

    beta_N = lambda_N N^theta -> infinity,
    nu_N = lambda_N^(-1) N^(-theta) -> 0.

Thus b_N=1 and sigma_N=sqrt(N) on a sufficiently late tail; nu_N lies in a fixed bounded interval. For each terminal time t_j, use THM038 with that terminal horizon and the same fixed h_j. There are finitely many such applications, so their constants have a common maximum. No theorem for a varying terminal test is invoked. The source bound and Tonelli give the first error C N^(s/d-1/2). Bounded gradients and the exact bracket give sqrt(N) E|M_t| <= C sqrt(nu_N).

For the remaining replacement, v_N = f_0^(nu_N) - S_t h has Haar mean zero. The heat identity, heat contraction and the Fourier L2 contraction of S give

    ||v_N||_2 <= nu_N t ||Delta h||_2,
    E |N^(-1/2) sum_i v_N(X_i(0))|^2 = ||v_N||_2^2.

The equality comes from initial independence and mean zero; cross-label terms vanish. Its square root is the required C nu_N bound, without a spurious sqrt(N) loss. Initial iid preparation also remains part of the imported source/energy premise. Candidate line 80, describing the new direct uses of independence, cannot be read as deleting that source hypothesis; lines 7–9 and the frozen statement retain it explicitly.

Adding the three errors gives exactly candidate (C), with the same normalization, centering and fixed tests as THM039. The strict s < d/2 makes the source exponent negative. For the whole vector, the Euclidean norm is bounded by the sum of absolute component errors, so its expected norm tends to zero. The old floor expression evaluated at critical beta has power s/d > 0 and is not assumed small anywhere in this proof.

## 6. Full joint probability passage

This review tested the full tuple, not independent one-time limits. Define the one-particle real vector V(x) by its components S_(t_j)h_j(x)-mean(h_j). It is bounded, fixed in N, and mean zero. Its covariance C is symmetric positive semidefinite because u^T C u = integral (u dot V)^2 for every real u. Finite-dimensional diagonalization constructs C^(1/2) and hence the centered Gaussian G, even when C is singular.

For Y_N = N^(-1/2) sum_i V(X_i(0)), Taylor's integral remainder gives, for each fixed real u,

    E exp(i u dot V / sqrt(N))
      = 1 - (u^T C u)/(2N) + r_N(u),
    |r_N(u)| <= E|u dot V|^3/(6 N^(3/2)).

Taking the Nth power uses independence across particle labels, never across tuple coordinates. For sufficiently large N the scalar increment has modulus less than one half, so the elementary expansion of log(1+z) proves convergence to exp(-u^T C u/2), including u^T C u=0. Boundedness of V supplies the remainder uniformly in N for each fixed u. No formal expansion with an uncontrolled triangular test remains.

The candidate does not stop at characteristic functions. With an independent standard m-dimensional Gaussian W and fixed epsilon>0, the density of Y_N+sqrt(epsilon)W is a Gaussian mixture. Under the Euclidean characteristic-function convention used above, Fourier inversion of this Gaussian mixture and Fubini give

    sup_x |p_(N,epsilon)(x)-p_(G,epsilon)(x)|
      <= (2 pi)^(-m) integral |phi_N(u)-phi_G(u)|
                              exp(-epsilon |u|^2/2) du -> 0.

The majorant is twice an integrable Gaussian; thus dominated convergence is valid. Both smoothed laws have second moment trace(C)+m epsilon. For a bounded Lipschitz test, split its integral at a ball of radius R. Uniform density convergence handles the ball, and Markov's inequality controls both tails by their displayed second moments. First take N to infinity, then R to infinity. Finally coupling with the added Gaussian changes expectations of a 1-Lipschitz test by at most sqrt(epsilon) E|W|. Sending epsilon to zero proves convergence of bounded Lipschitz expectations for Y_N to G without requiring a density for G.

These expectations imply ordinary finite-dimensional weak convergence: the unsmoothed second moments give tight tails, and a bounded continuous function can be uniformly approximated on a compact ball by a bounded Lipschitz function. Equivalently the same compact-ball argument in the candidate suffices. For the actual Z_N, the expected norm error from Section 5 makes every bounded Lipschitz expectation differ from that for Y_N by a quantity tending to zero. It also supplies tightness in this fixed Euclidean space by Markov's inequality for the error. This finishes the weak limit for the actual full vector. No process or distribution-valued tightness is asserted or needed.

Parseval with real tests gives the covariance stated in THM039, with exponent t_i+t_j. The conjugation and omission of the constant mode are necessary. A time difference exponent would describe a different covariance and is rejected by a two-positive-time mode probe. Repeated time/test pairs may give identical coordinates; other linear dependencies also produce singular C and are all covered. At zero time, the three approximation errors vanish exactly; constant tests yield zero at every N. T=0 therefore gives the ordinary finite-dimensional iid initial Gaussian result. Arbitrary fixed smooth real tests are covered by their finite Fourier seminorms; Fourier polynomials occur only in diagnostics.

## 7. Per-claim hostile verdicts

Line locations below refer to the sealed 120-line candidate.

| Claim identifier | Candidate location | Hostile verdict and scope |
|---|---|---|
| AUD054-C01 | 3, 7–9 | PASS CONDITIONAL. Full current range and actual law match the frozen card; open THM038 and historical source statuses remain explicit. |
| AUD054-C02 | 11 | PASS. Exact deterministic-time one-body Haar centering follows from fixed-translation equivariance, measurable unique paths and initial invariance. |
| AUD054-C03 | 15–23 | PASS. Full compensated divergence, response sign, mode multiplier, constants and uniform smooth-test control agree. |
| AUD054-C04 | 25–31 | PASS. Off-diagonal source and its original Haar row/double contraction have the stated values; Coulomb atom and compensation are indispensable. |
| AUD054-C05 | 33–43 | PASS. Ordered pair coefficient one half, N^2 denominator, response cancellation and absent singular self term are correct. |
| AUD054-C06 | 43–49 | PASS CONDITIONAL. The actual pair moment supplies the time-probability majorant; bounded gradients give the exact true-martingale bracket and mean-square localization passage. |
| AUD054-C07 | 55–68 | PASS CONDITIONAL. Every positive finite critical sequence has the required tail; actual absolute source and thermal errors are uniform there. |
| AUD054-C08 | 72–80 | PASS. Initial triangular-test replacement is centered, uses exact iid variance, and costs nu_N, not sqrt(N)nu_N. Imported iid source hypotheses remain in force. |
| AUD054-C09 | 82–87 | PASS CONDITIONAL. The exact frozen approximation holds componentwise and in expected finite-vector norm; strict source range is retained. |
| AUD054-C10 | 91–100 | PASS. Whole-vector covariance is positive semidefinite, its Gaussian exists with degeneracy, and the fixed-vector characteristic-function remainder is controlled. |
| AUD054-C11 | 102–106 | PASS. Gaussian smoothing plus uniform second-moment tails supplies a full weak-convergence argument and transfers it to actual particles. |
| AUD054-C12 | 110–116 | PASS. Real cross-time covariance uses t_i+t_j, complex conjugation and shared initial particles; the thermal contribution vanishes. |
| AUD054-C13 | 87, 91, 104, 116–118 | PASS. Zero time, T=0, repeated times, constants, arbitrary fixed real smooth tuples and degenerate covariance are all admitted without extra hypotheses. |
| AUD054-C14 | 7, 118 | PASS. No path-space, distribution-valued, growing-family, endpoint s=d/2, above-threshold, logarithmic, inhomogeneous, arbitrary-preparation, full-subcritical or higher-hierarchy conclusion is promoted. |
| AUD054-C15 | 120 and supplied exposure | PROVENANCE QUALIFIED. The constructor is correctly labeled exposed; the historical chronology is an attestation, not independently verified in this restricted lane. Its truth is unnecessary to the mathematical implication. |

No mathematical repair is required by this hostile review. No finding labels a failed upper bound a counterexample. The strongest surviving mathematical statement is the entire conditional THM039 assertion, not a one-time proxy or a repaired subrange.

Two non-defect boundaries remain explicit: AUD054-Q01 (candidate lines 3, 9, 118) is the open matching source-gate requirement; severity is promotion-blocking until root verifies it, with high confidence and no candidate edit proposed. AUD054-Q02 (candidate line 120 and exposure file) is the limit on verifying constructor chronology; severity is provenance-only, with high confidence that this lane cannot verify unseen records. Root must use the independent axes and its own exact gate mapping, rather than turn these attestations into blind-certification evidence.

## 8. Fresh exact diagnostics and mutation controls

The new standard-library program `hostile_exact_diagnostics.py` was written in this lane without opening any constructor or earlier checker. It uses exact rational and Gaussian-rational coefficients; no random seed, float tolerance, external package or installation is involved. Fourier differentiation is divided by 2 pi, so the source, generator and bracket comparisons are all divided by (2 pi)^2, consistently. The separate gamma-recurrence checks retain powers of pi symbolically.

The full generator is applied literally to finite Fourier empirical observables in dimensions three and four and at N=2,3,4, with zero and positive rational noises. Its carré du champ is computed from the generator product rule itself and compared with the asserted two-test thermal bracket. This independently tests cancellation of all interacting drift terms. The packet records 4,974 exact polynomial coefficients compared across these identities and the energy tests.

Further diagnostics check positive heat-splitting Laplace moments and scale-independent slopes by exact integration of binomial exponentials; the energy self/background coefficients; exact gamma recurrence and Coulomb constants; critical and excluded scaling powers; a six-dimensional joint covariance at genuine three-dimensional Coulomb times that are integer multiples of log(2)/(4 pi); zero and repeated tests/times, conjugate pairing and degeneracy; initial triangular-test variance; fourth-order iid label contractions; and the smoothing variance parameter. These are meaningful exact probes, not a computational proof of a singular theorem or weak convergence.

Outcome: **PASS — 1,031 exact assertions, 4,974 polynomial coefficients compared, and 15 deliberately incorrect mutations rejected.** Mutation witnesses include a missing pair factor one half, wrong source row sign or deletion, falling-factorial normalization, missing thermal factor two, wrong thermal N, missing energy self term, wrong omitted-kernel mass coefficient, removed Coulomb atom or compensation, response sign reversal, covariance time difference, uncentered constant mode, missing complex conjugation and incorrect Gaussian smoothing scale. Exact witnesses are recorded in `DIAGNOSTIC_RESULTS.json`.

The first development run reached the joint-constant test and exposed a diagnostic helper error: the zero polynomial had no stored dimension, causing `StopIteration` in the helper that centers a polynomial. An explicit empty-polynomial return corrected that helper. This was a harness failure, not a candidate failure; the constant-test case is retained. The full final battery then passed. A second full run with a separate output path reproduced the JSON byte-for-byte before issuance; the seal record documents that comparison.

## 9. Sealed handoff and stopping point

Only the prescribed copied inputs and the assigned audit report/artifact directory were written in this worktree. No canonical edit, state/ledger update, commit, push, external browse, installation, child agent, author contact or public communication occurred. The report is construction-exposed hostile analysis, not blind reconstruction. Historical source statuses are unchanged.

The companion `ROUND_017_GAUSSIAN_HOSTILE_ARTIFACTS` directory contains a byte-identical report copy, all fourteen sealed input copies, input verification and manifests, the new program/results, exposure and source maps, reproduction notes, output manifest, a safe exact-member ZIP, its digest and the archive verification result. Archive verification rejects unsafe paths, directories, symlinks, duplicate/extra/missing members and byte mismatches, checks every input and output hash, and verifies extraction in a new directory. Issued files are made read-only after all checks; changes require a separately issued superseding report.

The bounded handoff is complete only after those recorded seals pass. The next owner action is root comparison against the untouched statement-only reconstruction and the separate matching THM038/source gates. This reviewer stops at this sealed handoff and performs no canonical promotion.
