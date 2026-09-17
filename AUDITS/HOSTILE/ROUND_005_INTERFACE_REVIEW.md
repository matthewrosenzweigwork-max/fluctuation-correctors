# TASK044 — sealed hostile review of the full-pair interface

Date: 2026-09-17 UTC. Review type: fresh full-proof hostile review, **not blind**. Target: THM-025 and `MEMORANDA/ROUND_005_FULL_PAIR_INTERFACE_AND_HOMOGENEOUS_DATA.md`. Base commit: `52bda5d0d24067b051c6fe9763f2a78e7599e593`. Branch: `codex/hocf-r005-interface-hostile`. Working directory: `/private/tmp/hocf-r005-interface-hostile-20260917_232336_UTC`.

## Verdict

**REPAIR_REQUIRED for the submitted statement-level source interface. No counterexample to the mathematical endpoint assertion was found.** The first unsupported line is memorandum line 9: “THM021 proves the local coefficient-one hypothesis of THM023.” The supplied THM-021 card does not state that hypothesis. A second, minor constant identification on the same line should be made explicit. These defects do not change the exponent range, centering, iid constant, Fourier sign, or claimed rate.

The prescribed-data implication, pointwise/quotient compatibility, time hypotheses, actual homogeneous Fourier construction, and initial iid estimate pass this bounded review **conditional on the exact prerequisite statements** and the local kernel bridge identified below. Section “Additional independent kernel derivation” proves that bridge directly from the frozen Fourier definition; that derivation is reviewer-added work, not evidence that it was present in the supplied THM-021 statement. The candidate was not edited. Its source attribution still requires a separate source-location clarification or explicit incorporation of the bridge.

This verdict does not re-audit the proofs of THM-021, THM-023, or THM-024, does not infer their final audit status from submission labels, and does not certify a finite-particle generator domain, singular Ito identity, evolved-law estimate, or fluctuation theorem.

## Scope and provenance

The nine files listed in `ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt` were hashed at the root, copied into the new worktree, and hashed again before reading their contents. The verification script rechecks all nine. The root manifest itself was copied unchanged. Only the permitted task, AGENTS, frozen Round 001 model, five theorem cards, and candidate memorandum were read. No other memorandum, reviewer report, canonical state, repository history, memory, or external source was read. The task-specific allowlist supersedes AGENTS' general orientation requirement to read additional documents. No children, dependencies, commits, or pushes were used. No root working-tree files were edited.

The coordinator was notified promptly of the first missing statement-level premise and later of the constant clarification. A prospective clarification from an out-of-dossier proof was explicitly deferred; it is not treated as evidence here. This is a full-proof review of the submitted candidate, with the earlier cards accepted solely as prerequisite statements, as TASK044 requires.

The exact assertion reviewed is that the frozen periodic Riesz kernel with d at least 3 and 0 < s <= d-2, regular prescribed background/test data, N at least 2, and diffusivity in one bounded interval supplies the abstract composition hypotheses and hence a bounded Borel auxiliary-pair inverse with the stated Haar L2 and initial iid bounds. The actual-data corollary fixes zero external drift, Haar initial reference, and one fixed real smooth terminal test. Its negation is an admissible instance violating an interface premise, inverse assertion, Fourier construction, or endpoint estimate. Initial iid sampling, auxiliary-pair dynamics, and the interacting N-particle law remain distinct.

## Defects and required dispositions

### TASK044-D1 — missing local-kernel premise in the supplied prerequisite statement

- **Location:** candidate memorandum line 9; downstream blanket interface assertion at line 19 and THM-025 line 7.
- **Required premise:** THM-023 line 5 requires an even periodic kernel smooth off zero and a local representation `g(z)=|z|^(-s)+q(z)` with smooth even q on an embedded ball.
- **Supplied evidence:** THM-021 lines 5–10 fix the Fourier coefficients and assert the finite-measure divergence, integrability of K, and lower bound. They do not explicitly state smoothness off zero or the smooth local remainder. The Round 001 model's description of a “local principal singularity” does not state the required smooth-remainder conclusion either.
- **Diagnosis:** the cited card does not supply the premise as attributed. This is a source/interface omission, not a counterexample to the local property or the endpoint.
- **Severity and confidence:** load-bearing documentation gap; high confidence. A card-only implication cannot cite an unstated module conclusion without a bridge.
- **Repair:** cite a precise permitted, verified source statement/proof location that establishes the full local hypothesis, or add the independent derivation below as an explicit lemma. The source file need not be silently edited to resolve the attribution.
- **Strongest surviving statement:** assuming this local kernel property in addition to the supplied prerequisite statements, every subsequent analytic interface and endpoint conclusion reviewed below follows. The extra property is proved independently in this report, so there is no remaining mathematical obstruction at this interface once that proof is incorporated or separately source-verified.

### TASK044-D2 — propagator constant requires an explicit choice

- **Location:** candidate memorandum line 9, `exp[(D_u+kappa/2)(a-t)]`.
- **Required input:** THM-023 line 16 states `exp[(D_u+C0/N)(a-t)]`, with `C0=||(R_g)_-||infty`. THM-021 line 10 states a lower-bound constant kappa; the two cards do not identify it with C0. The smooth-cutoff estimate in THM-021 line 21 alone is not a stated singular estimate for the merely C1 prescribed transport.
- **Diagnosis:** the desired parameter-independent bound is supplied, but with C0. The written substitution is not explicit.
- **Severity and confidence:** minor statement-interface clarification; high confidence. No rate or finite-N normalization changes.
- **Repair:** take `c=D_u+C0/2` directly from THM-023, or declare that kappa has been enlarged to at least C0. Both constants are fixed-data constants independent of N and the allowed diffusivity. This report uses the first choice. This is not a claim that the sharper lower-bound estimate is false.

No other actionable defect was found within the declared scope. The missing interacting-law/domain bridge at candidate line 64 is correctly disclosed and remains outside this theorem.

## Per-claim review

| Claim and source location | Reconstruction and disposition |
|---|---|
| Kernel normalization and THM-023 local hypothesis; memorandum 7–9 | TASK044-D1 applies. The explicit frozen coefficient is used without a normalization change. The additional derivation below proves the missing local property. No logarithmic substitution occurs. |
| Prescribed u, f, and diffusivity; THM-025 5, THM-023 5–7 | Matches: uniform C1 transport and divergence lower bound, time-continuous C2 test with uniform gradient/Hessian bounds, fixed finite horizon, N >= 2, and bounded nonnegative diffusivity. No unknown mean-field regularity is assumed. |
| Auxiliary pair process and source potential; memorandum 9 | Supplied by THM-023, after the local premise is supplied: continuous noncolliding pathwise-unique realization, deterministic conditional Markov evolution, jointly measurable bounded Borel source potential, absolute occupation, terminal zero, and `A_N^2 <= C rho_N`. Internal drift is exactly K/N in the first slot and -K/N in the second slot. |
| Markov contraction and Haar extension; THM-024 5 | A Markov expectation is a Borel sup-norm contraction. THM-023's equality-class consistency and jointly strongly continuous Haar L2 evolution supply strong measurability. Use `c=D_u+C0/2`; TASK044-D2 records the original notation gap. |
| Borel and L2 response bounds; memorandum 11–15 | THM-021 gives each norm at most `M0 TV(D_K)+M1 ||K||1`, hence the factor 2 for the sum. Same background mu is used in both operators. No weighted-L2 bound is substituted here. |
| Time hypotheses; memorandum 15 | The response difference bound with density/gradient differences proves operator-norm continuity for mu continuous into C1. Parameter integration against fixed finite signed measure and fixed L1 vector field gives joint Borel output. Strongly measurable L2 input combined with the operator-norm-continuous response and jointly strongly continuous propagator gives the required Bochner integrands. |
| Diagonal and Haar representatives; memorandum 17 | Passes, by the separate arguments below. Pointwise independence off the pair diagonal is stronger than equality almost everywhere and is checked separately. No diagonal trace of an arbitrary L2 class is used. |
| Pair exchange; memorandum 19 | Exchanging particles and their independent Brownian motions preserves the law; pathwise uniqueness identifies the base evolution. J is symmetric because both K and the gradient difference change sign. The summed response commutes with exchange by THM-021. |
| Volterra solution, bounds, and uniqueness; memorandum 19–23 | Follows from the exact THM-024 statement. A direct series reconstruction below confirms the sup-norm and L2 exponents and keeps pointwise uniqueness distinct from L2 uniqueness. The integrated source is J plus the full summed response. |
| Iid scaling and density factor; memorandum 25–31 | Correct ordered distinct-label denominator N squared and P=U2/2. The finite-N coefficient is `b_N(N-1)/(2N^2)` before the final upper bound. The conversion factor is M0 squared. Independent rational enumeration confirms N=2,3,4,5. |
| All three rates; memorandum 31 | Correct: `b_N/N`, `b_N(1+log N)/N`, and `b_N N^(-(d+2-s)/(s+2))`. In the last regime `d+2-s >= 4`; hence decay holds. Only bounded diffusivity is covered. |
| Homogeneous reference; memorandum 37 | K is integrable and odd, so K convolved with Haar density is zero. The constant probability density solves the frozen equation, with u=0, M0=1, M1=0, and D_u=0. This is explicit existence, with no weak-solution uniqueness assertion. |
| Fourier sign and terminal condition; memorandum 39–56 | Correct multiplier, decay sign, zero mode, real-valuedness, and terminal data. The construction below checks the backward equation independently. |
| Spatial/time differentiation; memorandum 45–50 | Rapid Fourier decay dominates every fixed spatial derivative. For each finite diffusivity it also dominates the extra time-derivative multiplier. Uniform spatial bounds for all diffusivities do not imply or require uniform time-derivative bounds. |
| Parameter and regime quantifiers; memorandum 56–58, THM-025 13 and 21 | Fix terminal h and a positive lower beta bound; choose diffusivity interval up to its reciprocal. Every critical sequence eventually lies in that range because s<d. Only subcritical sequences having such a lower bound are covered. Zero noise is separate from reciprocal finite beta. |
| Dynamic exclusions; memorandum 64, THM-025 23 | Correctly excludes finite-particle Ito/domain passage, evolved iid propagation, interacting-law residuals/brackets, tightness, Gaussian or other fluctuation limits, and critical hierarchy closure. The initial bound does not establish those claims. |

## Additional independent kernel derivation

**Status: proved here as additional review work. It was not contained in the supplied THM-021 card.** This argument supplies precisely the local hypothesis in TASK044-D1 from the frozen Fourier definition, without importing a literature normalization.

Write `a=(d-s)/2`, and define the mass-one periodic heat kernel by periodizing the Euclidean Gaussian:

    H_t(x) = sum_(n in Z^d) (4 pi t)^(-d/2) exp(-|x+n|^2/(4t)).

Its k-th Fourier coefficient is `exp(-4 pi^2 t |k|^2)`: unfold the Gaussian integral over the translated unit cubes and take its Fourier transform. All terms are nonnegative before the Fourier transform, and the Gaussian integrals and their derivatives converge absolutely. Define

    A = c_(d,s) (4 pi^2)^a / Gamma(a)
      = 2^(d-s) pi^(d/2) / Gamma(s/2),
    g(x) = A integral_0^infinity t^(a-1) (H_t(x)-1) dt.

The integral converges in L1. Near zero, `||H_t-1||_1 <= 2` and a>0. For t>=1, the nonzero Fourier modes give exponential decay, also after any fixed number of spatial derivatives. Taking Fourier coefficients and using the gamma integral gives zero at k=0 and exactly `c_(d,s)|k|^(s-d)` otherwise. Thus this is the frozen kernel as an L1 function and as a distribution.

For `0<|x|<1/4`, subtract the n=0 Gaussian integrated over all positive t. Its value is

    A (4 pi)^(-d/2) integral_0^infinity
          t^(-s/2-1) exp(-|x|^2/(4t)) dt
      = A 2^(s-d) pi^(-d/2) Gamma(s/2) |x|^(-s)
      = |x|^(-s).

The remainder is the sum of the two integrals

    q(x)/A = integral_0^1 t^(a-1)
                 [sum_(n != 0) (4 pi t)^(-d/2) exp(-|x+n|^2/(4t)) - 1] dt
             + integral_1^infinity t^(a-1)
                 [H_t(x)-1-(4 pi t)^(-d/2) exp(-|x|^2/(4t))] dt.

Every spatial derivative of the nonzero-image short-time part is bounded by an integrable expression consisting of a fixed power of t times `exp(-c/t)`, uniformly on a slightly larger embedded ball. The constant subtraction is integrable because a>0. For the long-time integral, derivatives of `H_t-1` decay exponentially; the Euclidean term and each derivative are bounded by an integrable constant times `t^(-s/2-1)` on that ball, since s>0. Dominated differentiation therefore gives a smooth remainder through x=0. Reflection in x and n proves evenness. The same localized heat estimates away from lattice zero prove smoothness of g off zero. This proves the exact coefficient-one local hypothesis, with no change to the frozen torus, Fourier characters, or gamma constant.

## Direct response, time, and composition checks

For two bounded Borel extensions that agree off the pair diagonal, their difference in the first response can occur only at `w=y-x`. At an off-diagonal pair this is a nonzero point. Below Coulomb, D_K is absolutely continuous; at Coulomb its only atom is at zero. Consequently D_K assigns that point zero mass. The K term is integrated against Haar measure and also assigns it zero mass. The second response has the same property. In particular, at homogeneous Coulomb data the formula is

    R_x Phi = -c_d Phi + c_d integral Phi(z,y) dz,
    R_y Phi = -c_d Phi + c_d integral Phi(x,z) dz.

Acting on the pair-diagonal indicator yields only `-2 c_d` times that indicator, which is zero off the diagonal and zero as a Haar class. This tests the atomic location explicitly.

For general Haar-null changes, use translation invariance and Fubini in the full pair variables: each fixed translation of a Haar-null subset remains null, and integration against the finite D_K measure or the integrable K field preserves equality almost everywhere. This proves quotient consistency by a different mechanism from the preceding pointwise check.

The response coefficient bound applied to `mu_t-mu_r` and its gradient tends to zero in operator norm as t tends to r. Borel parameter integration is legitimate for its signed measure by total variation; the vector-field term is absolutely integrable. Joint strong continuity of S from THM-023 and strong measurability of an L2-valued input then supply the Bochner integrals in the Volterra series. No operator-norm convergence in a singular cutoff is needed here.

Let V denote the Volterra operator `V F(t)=integral_t^T S_(t,a) R_a F(a) da`. Its iterates satisfy

    ||V^n U_N(t)||_infinity <= B_N C_R^n (T-t)^n/n!,
    ||V^n U_N(t)||_2 <= A_N exp(cT) C_R^n (T-t)^n/n!.

The second estimate uses the product of propagator growth factors along an ordered time simplex, whose total duration is at most T. Summing gives the two stated bounds. Iterating the difference of two solutions gives uniqueness separately in the bounded Borel class and in the uniformly bounded L2 class. Terminal zero and symmetry are preserved. The absolute integrated source is integrable from each permitted start because the J occupation is supplied by THM-023 and `|R Phi| <= C_R ||Phi||_infinity`. Thus the martingale statement uses a true integrable source, not an unproved singular Ito formula.

## Independent iid reconstruction

Use the THM-015 Hoeffding components theta, h, and H, with H canonical. Directly expanding the defining ordered-label statistic gives

    P_N = -theta/(2N) - N^(-2) sum_i h(X_i)
          + N^(-2) sum_(i<j) H(X_i,X_j).

The constant, first-order, and canonical pair parts are orthogonal. Two distinct pair terms have zero covariance even when their labels overlap, by conditioning on the shared label and using the canonical property. Hence

    E P_N^2 = theta^2/(4N^2) + ||h||_2^2/N^3
              + (N-1)||H||_2^2/(2N^3).

Since `||Phi||_2^2=theta^2+2||h||_2^2+||H||_2^2`, the claimed sharp bound follows for N>=2. Multiplication by N b_N yields

    E |sqrt(N b_N) P_N|^2
      <= b_N (N-1) ||Phi||_(L2(mu_0 tensor mu_0))^2/(2N^2)
      <= b_N M0^2 ||Phi||_(L2(Haar^2))^2/(2N).

No exact first-marginal centering is substituted. A density is atomless, so a Borel kernel's arbitrary spatial-diagonal extension does not affect initial iid samples or background integrals. The finite support test deliberately retains spatial coincidences, demonstrating that distinct particle labels do not mean distinct coordinates.

The factor M0 squared cannot generally be reduced to M0. For example, a density equal to 2 on a set of Haar measure 1/2 and zero elsewhere, with kernel its product indicator, gives weighted squared norm 1 and Haar squared norm 1/4. This example checks the norm conversion; it is not claimed as a C1 prescribed background. Smooth approximations give the same limiting ratio if desired. The candidate has the correct squared factor.

## Independent homogeneous Fourier and regime reconstruction

At homogeneous reference density, the actual linearized one-body response is

    R f(x) = integral K(w) dot grad f(x+w) dw.

The frozen convention gives `K_hat(-k)=2 pi i k g_hat(k)`. Dotting with the character gradient `2 pi i k` produces the multiplier `-4 pi^2 |k|^2 g_hat(k)`. The diffusion multiplier is `-4 pi^2 nu |k|^2`. Thus for each nonzero k, if a_k is the positive sum written in the candidate, the terminal-value coefficient equation is `f_hat'_t=a_k f_hat_t`; its solution is `h_hat(k) exp[-a_k(T-t)]`. This independently verifies the backward sign. The zero mode is constant.

Repeated integration by parts in h bounds its coefficients by every inverse polynomial. Spatial differentiation multiplies by a fixed power of k, and time differentiation for fixed finite nu adds a multiplier growing at most quadratically on the stated exponent range. These series converge absolutely and uniformly on the full time interval. Dominated convergence gives continuity into every fixed spatial C^m space. The damping factor is at most one for every nonnegative diffusivity, giving uniform spatial derivative bounds; reality follows from conjugate symmetry. At Coulomb, `4 pi^2 c_(d,d-2)=(d-2)|S^(d-1)|`, so at zero noise all nonzero modes have the same decay factor. This is an independent solvable endpoint. Constants give J=0 and then Phi=0 by uniqueness.

For a fixed positive beta lower bound, choose `nu_*=1/beta_*`. The norm constants can depend on this interval and on the fixed terminal test. They do not depend on N or the particular beta within that interval. At critical coupling, beta is asymptotic to a positive constant times `N^(1-s/d)` and therefore tends to infinity. All critical sequences are eventually covered, while beta tending to zero is not covered. For example, d=6, s=4, and beta=1 give microscopic subcriticality while the old energy-floor expression diverges; beta=N^(-1) is also subcritical but has unbounded diffusivity. These distinguish the regimes without asserting a full fluctuation theorem.

## Verification and output manifest

Command run in the isolated worktree:

    python3 AUDITS/HOSTILE/ROUND_005_INTERFACE_CHECKS.py

Result: **PASS** with Python 3.9.6 and standard-library dependencies only. There is no random sampling. All nine input hashes match. Twenty exhaustive exact-rational iid cases cover constant, additive, canonical, mixed, and orthogonal-mixture kernels at N=2,3,4,5. Forty-eight finite Fourier quadratures use a 1,024-point midpoint rule, four specified dimension/exponent pairs, and heat cutoff 0.003; the largest normalized error is about 3.55e-14. The backward mode residual is about 1.39e-16; the heat coefficient error is about 4.45e-16; the Coulomb coefficient relative error is about 2.83e-16. Thirty-six rate identities are checked with exact rational arithmetic. A scalar bounded-response Volterra model agrees with its convergent series to about 1.34e-15. All floating-point checks are supporting diagnostics; the proofs above supply the analytic conclusions.

The exact test configurations, tolerances, arithmetic, and per-iid-case values are in the script and JSON result. The supplied inputs were not changed during the review. Only this report, the checks, JSON results, README, and local manifests are review outputs. No TeX was changed or generated, so no TeX build is implicated.

Files are described in `ROUND_005_INTERFACE_README.md`. `ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt` records the nine frozen inputs. `ROUND_005_INTERFACE_OUTPUT_SHA256SUMS.txt` records every issued output except itself; its own digest is reported to the coordinator. The report is immutable after sealing. Any source clarification or change of verdict must be issued as a separate addendum.

The root's next decision is to source-resolve TASK044-D1 and explicitly choose the harmless propagator constant in TASK044-D2. Subject to those dispositions and the separate prerequisite audits, the bounded auxiliary inverse and homogeneous initial iid corollary pass this interface review. The interacting N-particle domain/regularization bridge remains unproved and outside this gate.
