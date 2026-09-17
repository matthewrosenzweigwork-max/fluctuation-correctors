# TASK-041: hostile review of the periodic base and conditional composition

2026-09-17 UTC. Fresh reviewer: `/root/r005_periodic_hostile`.

**Verdict: PASS for THM-023 in its stated bounded-diffusivity, prescribed-field scope. PASS for THM-024 as the stated conditional implication.** No blocking mathematical defect was found in the submitted proofs. One nonblocking wording qualification is recorded below: symmetry of the evolution means commutation with pair exchange, as expressly defined in the conditional memorandum; no Haar self-adjointness has been proved or used.

This is a full-proof hostile review of submitted arguments, not a blind reconstruction, and not certification of missing inputs for the actual mean-field fluctuation problem. The finite computations corroborate specific identities and negative controls; the analytic review below supplies the basis for the verdict. No replacement proof is being substituted for a failed submitted step.

## 1. Isolation, frozen inputs, and scope of the negation

The review took place in the new worktree `/tmp/hocf-r005-periodic-hostile-20260917`, branch `codex/hocf-r005-periodic-hostile`, based on `52bda5d0d24067b051c6fe9763f2a78e7599e593`. On this host `/tmp` resolves through `/private/tmp`; both names refer to the same worktree. The root checkout's pre-existing changes were inspected as status metadata only and were not edited. No commit, push, dependency installation, child agent, canonical-state edit, memory read, unrelated proof, or response-constructor proof was used.

All thirteen files in `AUDITS/ROUND_005_PERIODIC_HOSTILE_INPUT_SHA256SUMS.txt` passed SHA-256 verification before and after copying. The same input manifest is preserved as `AUDITS/HOSTILE/ROUND_005_PERIODIC_AND_COMPOSITION_REVIEW_INPUT_SHA256SUMS.txt`. The restricted task dossier takes precedence over the repository's broader orientation requests for this isolated review.

The permitted files inspected were:

| Input | Use |
|---|---|
| `TASKS/ACTIVE/TASK-041_ROUND005_PERIODIC_HOSTILE.md` | Review contract and excluded reading |
| `AGENTS.md` | Campaign discipline and isolation |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Pair noise, internal-force, centering, and denominator conventions |
| `THEOREMS/THM-015_IID_PAIR_SECOND_MOMENT.md` | Exact initial-iid assertion, independently recomputed below |
| `THEOREMS/THM-020_DIFFUSIVE_LOCAL_PAIR.md` | Scope of the earlier local result, not a full-periodic premise |
| `THEOREMS/THM-023_PERIODIC_BASE_PAIR.md` | Periodic submitted assertion and exact negation |
| `THEOREMS/THM-024_CONDITIONAL_FULL_PAIR.md` | Conditional submitted assertion and exact negation |
| `MEMORANDA/ROUND_004_DIFFUSIVE_RECONSTRUCTION.md` | Radial profile and local probabilistic prerequisites |
| `MEMORANDA/ROUND_004_DIFFUSIVE_RECONSTRUCTION_ALL_N_ADDENDUM.md` | All-particle-number radial integral estimate |
| `MEMORANDA/ROUND_005_PERIODIC_PAIR_POTENTIAL.md` | Complete submitted periodic proof |
| `MEMORANDA/ROUND_005_CONDITIONAL_FULL_PAIR_INVERSE.md` | Complete submitted conditional composition proof |
| `VERIFICATION_CODE/round005_periodic_pair_exact.py` | Constructor's finite exact checks; rerun separately without altering inputs |
| `VERIFICATION_CODE/round005_periodic_pair_exact_output.json` | Frozen check output; byte equality checked against the rerun |

The primary assertion reviewed is the conjunction of every assertion on THM-023 and the implication on THM-024. Its negation is an admissible set of data that violates one of the declared process, measurability, integrability, uniqueness, operator, convergence, or norm statements; for THM-024 all its input hypotheses must hold before a counterexample would negate the claim. Failure to establish a response bound or an actual backward-test regularity bound is not a counterexample to this conditional statement, but it prevents its unconditional application.

The local interaction coefficient is one, the torus Haar mass is one, and the source and internal drift are those explicitly specified in the submitted proof. No identification of the whole periodic interaction with the frozen Fourier-defined Riesz kernel is imported. In particular, the review does not verify a Fourier-to-local-regular-remainder theorem for that kernel. No outside literature assertion, novelty assertion, or private source is needed for the scoped proof.

## 2. Per-claim verdicts

Here `P` denotes the periodic memorandum and `C` the conditional memorandum. Line references are to the sealed bytes listed above.

| Claim | Submitted location | Verdict and limitation |
|---|---|---|
| Time-dependent cutoff construction and measurable path map | P, lines 259–265 | PASS; bounded spatial Lipschitz coefficients suffice; no time derivative of the data is used |
| Noncollision, global continuation, and pathwise uniqueness | P, lines 267–303 | PASS from each prescribed off-diagonal starting state; no diagonal-start dynamics or common exceptional set for all starts |
| Local radial identities and all cutoff terms | P, lines 121–257 | PASS, including the relative diffusion cross term and bounded-diffusivity dependence |
| Absolute occupation and bounded Borel potential | P, lines 305–335, 376–400 | PASS; the supremum bound may grow with particle number |
| All-N Haar pair L2 rate | P, lines 337–374 and the all-N addendum | PASS for all N at least two, including a core larger than the cutoff |
| Distributional divergence and Coulomb atom | P, lines 481–514 | PASS; the bounded remainder is essential on a periodic domain |
| Regularized flow/Jacobian and L2 bound | P, lines 402–479 | PASS at zero and positive diffusivity, with the stated exponent |
| Pathwise heat-force passage and Haar measure extension | P, lines 516–548 | PASS for fixed parameters and deterministic times |
| Strong L2 approximation and joint two-time continuity | P, lines 550–563 | PASS; neither operator-norm convergence nor singular-source-potential convergence follows |
| Pointwise bounded Borel response series and uniqueness | C, lines 7–42 | PASS conditional on all stated pointwise measurability and response bounds |
| Haar L2 series consistency, bound, and mild uniqueness | C, lines 28–42 | PASS conditional; equality classes and pointwise classes remain distinct |
| True-martingale characterization | C, lines 44–52 | PASS conditional; no differentiation of the constructed inverse is used |
| Exact initial-iid coefficient, density factor, and rates | C, lines 54–64 | PASS conditional; density factor is squared; no positive-time iid transfer |

## 3. Periodic barrier and global process: recomputation

For a test depending on `z=x-y`, the two independent noises of amplitude `sqrt(2 nu)` give relative covariance `4 nu I` and generator `2 nu Delta_z`. The two internal drifts give `2K(z)/N`. Locally this is

```text
L_rel = 2 nu Delta + [(2s/N) r^(-s-2) z + w_t(x,y)] . grad,
|w_t(x,y)| <= (L_u + L_k) r = L r.
```

The factor in the regular remainder uses `2/N<=1`. The mean-value estimates use periodic lifts along the short segment in the embedded chart; they do not differentiate torus distance through a cut locus. Evenness of the local remainder gives `k(0)=0`, which is necessary for its contribution to be of order r.

Writing `p=s+2`, `c=2sp`, `W=r^p+c tau/N`, and `Q=r^p/W`, direct differentiation gives

```text
F = (N/4) [W^(2/p)-r^2],
F_tau = s W^(-s/p),
F_r = (N/2) r [Q^(s/p)-1],
Delta F = (N/2) [Q^(s/p)(d+s-sQ)-d],
F_tau - (2s/N)r^(-s-1) F_r = s r^(-s).
```

The derivative of `Q^(s/p)(d+s-sQ)` is

```text
(s/p) Q^(s/p-1) [d+s-(2s+2)Q].
```

Its bracket is at least `d-s-2`, so the punctured Laplacian is nonpositive throughout the claimed range, including the endpoint. At zero remaining time all spatial derivatives of F vanish. At positive remaining time and the Coulomb endpoint the Laplacian is still strictly negative at positive radius, although the first small-time coefficient vanishes. The independent formal-series checker reproduces this endpoint distinction and the reversed first-order sign outside the allowed range.

Differentiating the integral representation of F yields

```text
0 <= -r F_r <= s F,
F <= s tau r^(-s),
|F_r| <= s^2 tau r^(-s-1),
|F_rr| <= 3s^2(s+1) tau r^(-s-2).
```

The last coefficient is the sum `s^2(p-1)+s^2(s+p)`. The annular estimates vanish with remaining time and are independent of N. The separate core bound is `(c^(2/p)/4) N^(s/p) tau^(2/p)`.

The source inequality uses the inner-ball Hessian estimate and the bounded force outside that ball. It is valid on the transition annulus even though the cutoff is less than one: the bounded exterior source term already controls the whole source there. In particular, no positivity of the signed source is needed.

For the cutoff product, the complete operator calculation is

```text
(partial_tau-L)(chi F)
 = chi [s r^(-s)-2 nu Delta F-w.grad F]
   -F[2 nu Delta chi+(v_N+w).grad chi]
   -4 nu grad chi.grad F.
```

The final coefficient is four. Bounding all annular terms exactly as in the submitted constants gives the error `E_* tau`, with `E_*` independent of N and of the particular diffusivity in the fixed interval. The drift absorption is `-w.grad F >= -s L F`. Thus, with the submitted choices,

```text
alpha = 1+sL,
C_B = B_J+H_f E_*/alpha,
alpha-sL = 1,
alpha C_B-H_f E_* = alpha B_J >= 0.
```

The nonnegative barrier therefore has backward operator at most `-|J|`. Bounded diffusivity is genuinely used here: the cutoff error contains the upper diffusivity bound. The proof does not yield a uniform constant as that bound tends to infinity.

The path construction is also adequate at the stated time regularity. For each spatial cutoff, subtracting the additive continuous noise leaves a deterministic integral equation with measurable time dependence, bounded drift, and a uniform spatial Lipschitz constant. Picard convergence is factorial, and difference estimates give uniqueness. Its measurable iterates and countable cutoff patching supply a jointly measurable maximal map. Joint continuity of the background itself also follows from time continuity and the uniform spatial Lipschitz estimate. Spatial derivatives need only be jointly measurable and uniformly bounded for the subsequent variational argument.

Noncollision is not inferred from source integrability. The separate positive test is `V=1+chi r^(2-d)`. On the inner ball,

```text
Delta r^(2-d) = 0,
L_rel V = -(2s(d-2)/N) r^(-s-d) + w.grad r^(2-d)
        <= (d-2)(L_u+L_k) V.
```

The annular terms are bounded and V is at least one. Smooth stopped Itô applied to its exponential damping therefore gives

```text
P{enter the epsilon tube before a}
 <= exp(C_V(a-t)) V(x,y)/(1+epsilon^(-(d-2))).
```

For the limiting argument one takes epsilon smaller than the initial separation. This avoids a trivial starting-on-the-stopping-set case and is sufficient for the stated limit. The right side tends to zero. Compactness of the torus away from a fixed collision tube excludes any other finite lifetime obstruction. A continuous noncolliding trajectory then has strictly positive minimum separation on a fixed closed time interval. This last fact is pathwise and is not used as a substitute for expectation integrability.

The source estimate is separately obtained by stopped Itô on the nonnegative barrier. Its time derivative and two spatial derivatives are regular on each stopped domain, including at the terminal time. Monotone convergence applies to the stopped absolute occupations after noncollision is established. It gives both expectation integrability and the claimed fixed-N uniform potential bound. The zero-noise case is covered by the same deterministic argument without an artificial transport boundary condition.

## 4. All-N square norm, Borel potential, and martingale class

The relative-coordinate Haar identity has no extra density factor:

```text
integral |h(x-y)|^2 dx dy = integral |h(z)|^2 dz.
```

For `ell=(c tau/N)^(1/p)` and `a0=c^2/(16d)`, the core contribution before the sphere-area factor is exactly

```text
N^2 ell^4 min(R,ell)^d/(16d)
 = a0 tau^2 ell^(-2s) min(R,ell)^d.
```

When `ell<R`, the tail is bounded by `s^2 tau^2 integral_ell^R r^(d-1-2s) dr`. When `ell>=R`, there is no tail. In the first range the core is bounded by `a0 tau^2 R^(d-2s)`; in the critical range it is bounded by `a0 tau^2`; in the third range it is bounded by `a0 tau^2 ell^(-(2s-d))`. The respective large-core ratios are `(R/ell)^(2s)`, `(R/ell)^d`, and `(R/ell)^d`, all at most one. This validates the submitted addendum's all-N extension rather than merely its asymptotic version.

At the critical threshold, monotonicity of the actual F permits replacing the remaining time by T before estimating the logarithm. The inequality `log_+(Nx)<=log N+log_+x` then produces the submitted constant. This avoids an incorrect monotonicity claim about an estimated logarithmic expression. At zero time the profile is zero, so no negative power or logarithm needs evaluation. In the upper range the identities

```text
2-(2s-d)/(s+2) = (d+4)/(s+2),
(2s-d)/(s+2)-1 = -(d+2-s)/(s+2)
```

give the exact norm and final endpoint exponents. Together with the bounded constant part of the barrier, these calculations prove the three submitted Haar pair rates, uniformly over N at least two and over the fixed diffusivity interval.

The restart identity for the measurable path map and independent Brownian increments give the deterministic conditional Markov property. A common noncollision event for all starting states is unnecessary: the zero exceptional probability for each state can be integrated against the current-state law. This is sufficient for the specific deterministic-time identities used in both proofs; no strong-Markov assertion is being smuggled in.

The source is jointly Borel under the stated derivative measurability. Measurable time integration and Brownian expectation give joint Borel measurability of its positive and negative potentials, which are finite by the absolute estimate. Conditional Tonelli for those two parts, or bounded truncation followed by the same absolute occupation bound, identifies

```text
U(a,X_a,Y_a)+integral_t^a J_r(X_r,Y_r) dr
 = E[integral_t^T J_r(X_r,Y_r) dr | F_a].
```

This is a true martingale, indeed a uniformly integrable family. Taking its terminal expectation gives pointwise uniqueness in exactly the declared bounded Borel class. It is not uniqueness in an unspecified generator domain. Pair exchange and exchange of the Brownian paths leave both the process law and source unchanged, so the potential is symmetric in the two coordinates.

## 5. Divergence, Haar measure passage, and continuity

The singular force and potential are locally integrable because `s+1<d`. The flux through a sphere of radius epsilon is `s epsilon^(d-s-2)` times sphere integration of the test function. Therefore the local distributional divergence is

```text
s(d-s-2) r^(-s-2),       0<s<d-2,
(d-2) omega_d delta_0,  s=d-2.
```

The first density is nonnegative and locally integrable; the endpoint has a positive atom. Writing the global potential as `chi r^(-s)+v` with v smooth produces exactly

```text
div K = P + R_g,
R_g = -2 grad chi.grad r^(-s) - (Delta chi) r^(-s) - Delta v.
```

The remainder is smooth and bounded because cutoff derivatives are supported away from zero. The torus divergence has total mass zero, so discarding the remainder would not be a valid periodic calculation. The submitted lower bound with `C0=||(R_g)_-||infinity` follows.

Positive heat convolution preserves that measure lower bound. With the two copies of the internal drift the full regularized divergence is

```text
div b^epsilon = div u(x)+div u(y)+(2/N)div K_epsilon(x-y)
             >= -2(D+C0/N).
```

For fixed noise, the regularized flow is a C1 spatial diffeomorphism. The derivative of its integral equation is justified by bounded measurable-time spatial derivatives and dominated convergence; continuity in the initial point follows from the spatial continuity of those derivatives at each time and the same domination. Backward solution for the fixed continuous driving path gives the inverse. Jacobi's identity gives the determinant lower bound with exponent `-2(D+C0/N)(a-t)`. Change of variables therefore yields a pushed-forward Haar density bound with exponent `+2(D+C0/N)(a-t)`. Jensen followed by a square root yields the L2 operator exponent `D+C0/N`, as submitted. This argument also works at zero noise.

The local C1 heat-force convergence follows by separating a smooth local part from a distant L1 part. Gaussian derivative tails kill the latter. For a fixed starting state, parameters, and time interval, the singular path has positive minimum separation almost surely. Uniform convergence and a common Lipschitz bound on a smaller collision-excluded neighborhood, followed by the stopped Gronwall estimate, force the regularized path to stay in that neighborhood for sufficiently small smoothing. This proves pathwise uniform convergence through the terminal time. The neighborhood may depend on the sample path; the proof does not require a uniform regularized noncollision estimate.

Bounded continuous terminal data then converge pointwise under the Markov evolutions and in Haar L2 by domination. The Haar density estimate passes first for nonnegative continuous functions. The submitted extension to open sets via continuous distance cutoffs, then to Borel sets via outer regularity of Haar measure, and finally to all nonnegative Borel functions is valid. It follows that Haar-null terminal sets have zero transition probability for Haar-almost every initial state. This is the actual mechanism for equality-class independence; it is not inferred solely from trajectory convergence.

Jensen therefore defines the singular L2 extension with the same bound. Continuous-function density and the uniform regularized/singular norm estimates then give strong L2 convergence for arbitrary terminal L2 data. This says nothing about convergence in operator norm or about heat-regularized source potentials with unbounded source.

The submitted joint two-time continuity argument also passes. On a reference noncolliding path, choose a fixed cutoff equal to the singular force along a surrounding collision-excluded neighborhood. For the cutoff equation, varying the starting and terminal times changes only small integration intervals, the uniformly continuous Brownian increments, and a Lipschitz comparison over the common interval. The resulting path difference tends to zero. Nearby time pairs consequently remain in the neighborhood, where the cutoff and singular equations agree. Bounded convergence proves continuity on continuous terminal data, including along the boundary `t=a`. Uniform operator bounds and L2 density extend it to every fixed L2 input. No derivative in time of u is required.

## 6. Conditional response series and its two uniqueness classes

The conditional proof's operator R includes both responses with coefficient one. It is not assumed positive or dissipative. The assumptions explicitly include the pointwise joint measurability, Borel-to-L2 consistency, diagonal-representative independence, and Bochner measurability needed for the construction. No proof of these assumptions for the campaign's actual response operator is imported here.

Writing `Vh(t)=integral_t^T S_(t,a) R_a h_a da`, the pointwise estimate can be obtained directly by induction on k:

```text
||(V^k U)(t)||infinity <= B_N C_R^k (T-t)^k/k!.
```

This argument uses scalar time integrals of norm bounds and does not need to exchange a general bounded Borel operator with a merely pointwise time integral. Thus it remains valid in the full abstract class stated in the card. The same estimate gives uniform convergence of the series; boundedness of V permits passage to the sum. Each term is Borel by the asserted measurable action. Pair exchange commutes through every term. The terminal value is zero.

For L2, each successive interval contributes its own factor `exp(c times interval length)`. Those lengths telescope, so the bound on a product is `exp(c(a_k-t))`, not `exp(k c T)`. Equivalently, a direct norm induction uses

```text
||(V^k U)(t)||2 <= exp(c(T-t)) A_N C_R^k (T-t)^k/k!.
```

The next integration step factors out `exp(c(a-t)) exp(c(T-a))=exp(c(T-t))`. This verifies the submitted slightly relaxed uniform bound `A_N exp((c+C_R)T)`. Bochner convergence and consistency of the actions identify the pointwise and L2 series at each time almost everywhere; Fubini handles time-dependent exceptional sets. No pointwise action on an arbitrary L2 representative is being inferred.

For a difference satisfying `d=Vd`, iteration gives the same factorial bound with the global supremum norm of d, hence pointwise uniqueness among bounded Borel solutions. Replacing that norm by the uniformly bounded time-dependent L2 norm gives the separate L2 mild uniqueness. The latter is uniqueness of equality classes, not a route to pointwise uniqueness on Haar-null sets.

The constructed response source is bounded and jointly measurable. Its occupation is integrable, and the original source has the separately assumed absolute integrability. Conditional Tonelli applied to positive and negative parts of the full source verifies the submitted conditional expectation identity directly. Therefore the resulting process is a true uniformly integrable martingale. Conversely, the terminal expectation of a solution in that martingale class gives the mild equation, so the preceding uniqueness applies. There is no singular Itô application to the constructed inverse in this argument.

## 7. Initial-iid endpoint and independent solvable tests

For a real symmetric kernel, let theta be its mean, h its centered first projection, and H its canonical part. Keeping the ordered distinct-label statistic and denominator N squared gives the exact decomposition

```text
P_N = -theta/(2N) - N^(-2) sum_i h(X_i)
      + N^(-2) sum_(i<j) H(X_i,X_j).
```

Conditioning on a shared label makes distinct canonical pair terms orthogonal. Their cross terms with the first projection and deterministic term vanish. Hence

```text
E P_N^2 = theta^2/(4N^2) + ||h||2^2/N^3
          +(N-1)||H||2^2/(2N^3)
        <= (N-1)||Phi||2^2/(2N^3).
```

The constant and projection comparisons are respectively `N<=2(N-1)` and `1<=N-1`, both valid for all N at least two, with equality throughout for N equal to two. Complete finite-space enumeration independently checked this decomposition and moment identity, including atomic samples with equal spatial coordinates but different particle labels. This tests that no spatial diagonal or centering term has been accidentally removed.

Multiplication by `N b_N` gives the coefficient `b_N(N-1)/(2N^2)`. A density bound by M0 gives

```text
||Phi||^2_L2(mu0 tensor mu0) <= M0^2 ||Phi||^2_L2(Haar tensor Haar).
```

There is no relative-coordinate reduction for the full kernel, so the square is needed. The checker includes a four-cell torus model with density two on two cells, zero on the other two, and canonical product kernel generated by values `1,-1,0,0`. Its Haar pair norm squared is one quarter and its initial-law pair norm squared is one. For N equal to three and b equal to one, the exact scaled second moment is one ninth, whereas the erroneous relaxed bound with only one density factor would be one twelfth. This is a negative control for the omitted hypothesis of translation invariance, not a counterexample to the submitted squared-factor bound.

For the response composition, the independent exact model uses the identity base evolution of a constant continuous off-diagonal process. Partition the pair space into two equal-Haar, pair-exchange-invariant measurable cells. On cell averages define signed square-zero matrices A and B, with A used before the time midpoint and B after it. Both Borel sup and Haar L2 bounds equal the corresponding matrix-entry bound. The source is constant on each cell. For a half-interval length h and remaining time tau in the later interval,

```text
Phi_late(tau) = tau j + (tau^2/2) B j.
```

With `q=Phi_late(h)` and remaining time r before the midpoint,

```text
Phi_early(r) = q + r(j+Aq) + (r^2/2) A j.
```

The derivatives, midpoint match, terminal value, and full mild equation are exact polynomials. Their source occupations also verify the martingale identity for the constant path. The mixed term has order A B, not B A; 192 tested instances distinguish these orders. Signed response entries test that positivity of R is unnecessary. This model checks the conditional argument independently of the singular-process construction.

The independent checker passed **4,415 exact rational assertions**, covering formal radial time coefficients, the endpoint Laplacian sign and excluded-range negative control, relative generator coefficients, small-N and large-core estimates, iid enumeration, the density-factor negative control, noncommuting response compositions, and simplex factorial/exponent identities. The constructor's checker was separately copied to a temporary directory and rerun; its 567 checks passed and its JSON output was byte-for-byte equal to the frozen input output. None of these finite checks replaces a parameter-uniform analytic argument or proves stochastic sample-path assertions by simulation.

## 8. Defects, wording qualification, and excluded scope

There are no critical or major defects requiring theorem repair in this sealed dossier. There is one low-severity wording issue:

| Identifier | Location | Diagnosis, confidence, repair, and consequence |
|---|---|---|
| TASK-041-E01 | `THEOREMS/THM-024_CONDITIONAL_FULL_PAIR.md`, line 5 | High confidence, nonblocking terminology ambiguity. “Symmetric Markov evolution” can conventionally mean Haar self-adjointness. The submitted proof, hypothesis 4 at C line 12, explicitly means commutation with pair exchange. A future clarification should use that exact wording. The card bytes were not changed. The audit grants no self-adjointness assertion and requires no such property for the conditional theorem. |

The strongest surviving result is exactly the submitted periodic base process and source-potential theorem together with the submitted bounded-response conditional implication and its initial-iid estimate. There is no mathematical failure requiring a weaker replacement theorem.

The following scope boundaries remain load-bearing:

- The dimension and singularity range are `d>=3` and `0<s<=d-2`; the logarithmic model is absent.
- The local coefficient-one singularity plus smooth remainder is a hypothesis. An actual periodic Fourier kernel must separately be shown to satisfy it before application.
- The background C1 and test C2 bounds are prescribed hypotheses, not conclusions about the campaign's mean-field or backward-test equations.
- The periodic barrier is uniform only on a fixed bounded diffusivity interval. Substituting diffusivity `1/beta_N` therefore requires the positive temperatures to obey the corresponding lower bound on beta; arbitrary sequences tending to zero are not covered by this periodic estimate. The zero-noise limit is separately included.
- Noncollision is from every fixed off-diagonal starting point; diagonal-start dynamics and simultaneous pathwise noncollision for all initial states are not asserted.
- The heat passage concerns terminal L2 data at fixed parameters. It does not give operator-norm convergence, a rate uniform in parameters, or convergence of heat-regularized singular-source potentials.
- Response boundedness, representative independence, and measurable action remain hypotheses here. This review has not read or certified the separate response proof.
- The final inverse is bounded Borel and satisfies its exact probabilistic martingale identity. Finite-particle generator-domain membership, spatial derivatives, singular Itô formulas, and associated quadratic/cross brackets remain unproved by this module.
- The iid consequence is an initial deterministic-time second moment. It gives no path supremum, no transfer to evolved interacting or Gibbs laws, and no control of the cubic remainder or hierarchy tail.
- No subcritical fluctuation theorem, critical law, finite critical truncation, Gaussian conclusion, or full campaign resolution is certified.

## 9. Verification and sealed handoff

The new review outputs are this report, the independent checker and its JSON output, the constructor-rerun JSON record, the copied input manifest, and a verification log. Their hashes are recorded by `AUDITS/HOSTILE/ROUND_005_PERIODIC_AND_COMPOSITION_REVIEW_SHA256SUMS.txt`. The output manifest intentionally does not hash itself. Each declared input remains byte-for-byte equal to the supplied dossier.

The exact verification commands for the handoff are:

```text
python3 AUDITS/HOSTILE/ROUND_005_PERIODIC_AND_COMPOSITION_EXACT_CHECK.py
shasum -a 256 -c AUDITS/HOSTILE/ROUND_005_PERIODIC_AND_COMPOSITION_REVIEW_INPUT_SHA256SUMS.txt
git diff --check
shasum -a 256 -c AUDITS/HOSTILE/ROUND_005_PERIODIC_AND_COMPOSITION_REVIEW_SHA256SUMS.txt
```

The independent checker passed, all thirteen input checks passed, and whitespace/integrity checks passed. A direct scan additionally checks the untracked report/code/JSON/manifests for terminal newlines, trailing whitespace, control characters, and balanced code fences. The verification log records these results. No TeX file was created, and the final handoff contains no mathematical LaTeX; no compilation claim is made for these Markdown/code outputs.

No submitted proof, theorem card, prior audit, immutable input, canonical ledger, or root working file was changed. Root alone integrates this review and chooses any canonical promotion or separate clarification. This verdict is an independent hostile audit of the stated arguments; it does not convert a conditional premise into a proved campaign input.
