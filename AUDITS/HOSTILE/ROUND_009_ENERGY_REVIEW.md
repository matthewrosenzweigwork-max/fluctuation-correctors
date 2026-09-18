# TASK059 — hostile review of the complete conditional THM029 argument

Issued 2026-09-18 UTC. **Verdict: PASS_CONDITIONAL.** The complete sealed Round 009 proof establishes the full THM029 implication with the complete THM028 domain assertion as an explicit premise. No unsupported line, false coefficient, hidden loss of uniformity, or counterexample to that conditional implication was found. No repair of the frozen card or proof is required by this review.

This is an independent hostile review of the submitted proof, not a blind reconstruction and not independent certification of THM028. The separate blind reconstruction was withheld. The actual-law error estimate remains open; neither the reference bracket rate nor this verdict promotes it to an interacting-law estimate.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r009-energy-hostile`. Branch: `codex/hocf-r009-energy-hostile`. Exact base: published R7 `4171be9839feb8acf4c70e1dda014458fdb44490`. All twenty permitted source files were copied from root and verified before review. The input manifest has SHA-256 `4d6f6519c56f424e9aac4a9f2f93829c7292546efc372a701acdd4228271e6c7`. The sealed proof has SHA-256 `dd0710cfb8a1b8a87abce3f746efc02364c4fa408056144f678f8c519b31e077`.

## Assertion tested and its negation

The tested assertion is the conjunction of all claims in frozen `THEOREMS/THM-029_HAAR_NOISE_ENERGY_AND_LAW_REDUCTION.md`, lines 3–34: the stated Haar pair energy bound uniform over all admitted particle numbers and diffusivities; the exact Haar gradient identity; the two scaled reference-noise rates; the four-term exchangeable-law identity; the explicit pair/triple/mixed reduction; and exchangeability plus one-body Haar invariance for the actual iid-Haar-prepared singular dynamics.

The negation tested is an admitted tuple satisfying the complete conditional prerequisite for which any one of those bounds, coefficients, or symmetry assertions fails. The range remains integer d at least three, positive s at most d minus two, N at least two, finite nonnegative horizon, diffusivity in the fixed bounded interval including zero, homogeneous Haar reference, external drift zero, and the actual Fourier backward test of smooth real terminal data. No logarithmic interaction, extra law class, or unbounded-diffusivity family was substituted.

An unknown or failed independent verdict for THM028 is not a counterexample to this implication. Conversely, taking THM028 as a premise does not excuse any unsupported new R9 estimate: each such step was checked below.

## Per-claim disposition

Locations in this table refer to `MEMORANDA/ROUND_009_HAAR_NOISE_ENERGY.md` unless another file is named. These are local review identifiers, not newly allocated canonical campaign audit identifiers.

| ID | Exact scope and location | Verdict | Reason and downstream consequence |
|---|---|---|---|
| TASK059-C01 | Frozen model, Fourier sign, and uniform actual test bounds; lines 11–31, 43–57 | PASS | Unit mass and characters are unchanged. The damping coefficient is nonnegative, and time differentiation has the opposite sign from the spatial generator. Gradient and Hessian Fourier sums are independent of N and the selected diffusivity. |
| TASK059-C02 | Full-source constants and supremum bound; lines 35–113 | PASS | Full R5 proof supplies the necessary pointwise bound, including its N power; the shorter theorem card is not used as a substitute. Both response slots give the stated exponential with a constant independent of N and diffusivity. |
| TASK059-C03 | Common divergence constant and optional sharper Haar-L2 comparison; lines 115–117 | PASS | Taking the maximum of the two source constants is valid. The optional logarithmic and supercritical-in-L2 comparisons divide by N correctly; they are unnecessary for the main energy route. |
| TASK059-C04 | Deleted-tube diffusion identity; lines 121–153 | PASS GIVEN THM028 | The transformed flux has the correct metric and both original gradients. Its boundary power is positive for every allowed first-derivative exponent. Global H1 and W2,1 justify absolute volume limits. No diagonal trace is imposed. |
| TASK059-C05 | Internal-drift flux and Coulomb endpoint; lines 155–187 | PASS GIVEN THM028 | The bulk coefficient is one after the half from differentiating the square cancels the relative drift factor two. The inner flux is nonpositive; at Coulomb it is retained. Absolute convergence uses the stipulated structural B-Phi integrability, not a possibly nonintegrable force-gradient product. |
| TASK059-C06 | Finite-measure response form; lines 191–208 | PASS | The even measure has the exact nonnegative nonzero Fourier multipliers and zero multiplier at zero. Both slots occur. Finite variation makes the Fourier-polynomial argument pass to the actual Haar-L2 kernel. This does not claim dissipativity of the base-pair evolution. |
| TASK059-C07 | Time differentiation, energy sign, and uniform energy bound; lines 212–255 | PASS GIVEN THM028 | The integrable common time-derivative majorant justifies differentiation. The initial norm is positive on the left. The only final constants are the explicit uniform source, supremum, divergence, and time constants. |
| TASK059-C08 | Exact statistic gradient, deletion term, and Haar identity; lines 259–309 | PASS GIVEN THM028 | Direct differentiation of ordered pairs gives the stated field. Conditional Haar centering cancels exactly the indicated cross terms and leaves the finite-N A term. N=2 and N=3 agree independently. |
| TASK059-C09 | Reference corrector-noise and leading-noise functionals; lines 313–346 | PASS GIVEN THM028 | Pair symmetry supplies the exact factor two between full and first-slot gradient norms. The scale and all N factors are correct. The leading thermal factor is at most one on both sides of diffusivity one. |
| TASK059-C10 | Absolute cross-density integral; lines 348–365 | PASS GIVEN THM028 | Cauchy–Schwarz is applied first to the actual particle/vector sum and then to the common time/configuration measure. The absolute value stays inside the integrals. |
| TASK059-C11 | Arbitrary exchangeable-law identity and integrability; lines 371–393 | PASS IN THE STATED INTEGRABILITY DOMAIN | Raw finite-sum squaring yields all four terms without any product or one-body Haar assumption. Fields must be defined almost surely; the proof explicitly makes no derivative or trace assertion at a collision. The actual and reference laws avoid these exceptional sets. |
| TASK059-C12 | Actual singular-law equivariance; lines 397–411 | PASS FROM STIPULATED REALIZATION | Common translations preserve all force differences; label permutations preserve the equation after permuting the iid drivers. Per-start uniqueness and joint measurability suffice after integrating the initial law. No common exceptional set over all translations is needed. |
| TASK059-C13 | Nonproduct and nonzero mixed-term diagnostics; lines 413–426 | PASS | The proposed invariant density is positive, normalized, exchangeable, and has Haar one-body marginals but a nonproduct pair marginal. Exact Fourier calculation confirms the nonzero mixed contraction. |
| TASK059-C14 | Measurable marginals and exact scaled law-error reduction; lines 430–458 | PASS GIVEN THM028 AND STIPULATED REALIZATION | Fixed-N domination permits time-integrated densities and every absolute pairing. One-body Haar removes only the A-square deviation. All three remaining signed deviations and their coefficients are exact; the triple term is absent at N=2. |
| TASK059-C15 | Sufficient transfer condition and explicit residual limitation; lines 460–479 | PASS AS CONDITIONAL IMPLICATIONS | The absolute error quantity bounds the signed difference. A rate or vanishing estimate for it would transfer the corresponding conclusion, and the leading actual noise uses only the proved one-body marginal. Exponential fixed-N domination provides no such uniform estimate. |
| TASK059-C16 | Endpoints, zero data, and temperature scope; lines 113, 255, 309, 365–367 | PASS | Zero horizon, zero noise, constant terminal data, N=2, Coulomb, and the Haar-L2 logarithmic borderline are handled without dividing by zero or deleting an undefined triple. The three campaign temperature conditions are not conflated. |

Confidence is high for every row within its displayed premises. There is no finding with a requested repair, so severity and downstream repair dependencies are not applicable. Conditional rows remain conditional in this verdict.

## Source and normalization preflight

The mathematical source inputs are the permitted frozen model and the supplied proofs, not the status labels in historical cards or references to other audits. No external citation, theorem number, private source, or novelty assertion is needed for this bounded review.

1. `TASKS/ACTIVE/ROUND_001_MODEL.md` and `MEMORANDA/ROUND_001_ALGEBRA.md`, lines 56–84 and 190–223, fix ordered distinct labels, denominator N squared, the factor one-half in P, both response slots, and coefficient one over N for the internal pair drift. R1 lines 507–548 fix the Brownian bracket convention. R1's smooth diagonal identities are not transferred to the singular kernel.
2. `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, lines 69–109, derives the coefficient-one local Riesz singularity from the exact heat/Fourier normalization. Lines 113–196 identify the integrable force, finite signed divergence, lower bound, Coulomb atom, and its negative constant compensation. Lines 200–258 justify equality-class consistency and response action. These are the full proofs referred to by the permitted source addendum.
3. `MEMORANDA/ROUND_005_PERIODIC_PAIR_POTENTIAL.md`, lines 87–170, 177–257, and 305–334, supplies the actual radial profile, cutoff calculation, and pointwise source bound. With ordinary transport zero, its regular relative-field Lipschitz bound is exactly L_k because two over N is at most one. Its cutoff diffusion cross coefficient remains four times diffusivity. The full source supremum is the one extracted in R9, not an inferred consequence of the short L2 card.
4. `MEMORANDA/ROUND_005_CONDITIONAL_FULL_PAIR_INVERSE.md`, in its construction with all finite-time constants, applies Markov supremum contraction on each ordered time simplex. The Volterra sum multiplies the base supremum by at most the exponential of the two-response norm times the horizon. No derivative constant or N-dependent semigroup exponent enters this supremum step.
5. `MEMORANDA/ROUND_005_FULL_PAIR_INTERFACE_AND_HOMOGENEOUS_DATA.md` gives the actual homogeneous Fourier test and the exact off-diagonal response representative check. The two allowed clarification documents fix the source reference, the common lower-divergence constant, and the meaning of pair-exchange symmetry. Their references to other audits were not followed or treated as current verdicts.
6. `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, lines 229–289 and 402–423, supplies the local construction, global per-start uniqueness, joint measurable realization, and integration of exceptional sets. Lines 471–544 give the fixed-N density estimate with the full factor N minus one. It is the actual N-particle construction, not the two-particle auxiliary process, used for the law assertions.
7. The complete THM028 card is used as an explicit conditional premise. Relevant interfaces in `MEMORANDA/ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, lines 527–580, 631–733, agree with that premise: the structural B-Phi identity, differentiated Haar contractions, genuine configuration gradient, true-martingale bracket, and fixed-N integrability. This review does not reconstruct or certify the proof of THM028.

## Independent reconstruction of the vulnerable analytic steps

### Uniform constants and the energy estimate

Write p = s + 2 and a = s/p. Direct evaluation of the supplied radial profile gives

```text
F_(N,tau)(r) = (N/4) [(r^p + 2sp tau/N)^(2/p) - r^2]
            <= [(2sp)^(2/p)/4] N^a tau^(2/p).
```

Concavity of the power two over p proves this for all N and nonnegative remaining times. The R5 barrier then gives precisely the displayed R9 constant C_infinity after the bounded Volterra response composition. The actual Fourier test bounds its gradient and Hessian uniformly by absolutely convergent sums of terminal Fourier coefficients; the damping multipliers have modulus at most one. The explicit source bound is Haar-L1 because s is strictly less than d.

The sharper optional L2 route does not introduce a hidden endpoint loss: below its borderline rho_N is one, at the borderline one plus log N is at most N, and above it the exponent of rho_N is strictly less than one. The main proof avoids this extra input by using the supremum alone.

In coordinates z = x minus y and y, the transformed pair metric has blocks two times identity, minus identity, minus identity, and identity. Therefore the inner diffusion flux is exactly minus Phi times the radial component of twice its z gradient minus its y gradient. The bound is a fixed-N constant times epsilon to the power d minus one minus q1, which tends to zero. THM028's H1 and W2,1 conclusions justify the volume limits. This argument never adds a trace on the pair diagonal.

For the internal drift, the vector field in these coordinates is `(2K,-K)`. Applying the divergence theorem to Phi squared divided by two produces

```text
integral_(tube complement) Phi B Phi
 = - integral_(inner sphere) (K dot radial unit vector) Phi^2
   - integral_(tube complement) D_cl Phi^2.
```

There is one copy of the classical divergence in the bulk. Near the sphere the first term is nonpositive because the coefficient-one repulsion dominates the smooth odd remainder. It tends to zero below Coulomb. At Coulomb the proof keeps its nonpositive sign rather than asserting its disappearance. The left integral converges absolutely by bounded Phi and the stipulated structural L1 bound on B Phi. The bulk converges by integrability of D_cl. Thus its final upper bound uses only kappa times the Haar squared norm, uniformly in N. No limit in N is interchanged with the tube limit.

The homogeneous responses are negative convolution with the even finite measure D in their respective slots. Their quadratic form is the negative sum over Fourier pairs of `(d_k+d_l)` times the squared Fourier coefficient of Phi. Both multipliers are nonnegative and bounded on the admitted range. Finite-measure convolution is bounded on Haar L2, so finite Fourier projections justify the formula for the supplied Phi itself. The negative compensation in D does not contradict positivity of its Fourier coefficients or this response sign.

Finally, time differentiation of the squared Haar norm uses bounded Phi and the common integrable majorant for its time derivative. In the terminal-zero equation, integration gives

```text
nu integral_0^T ||grad_pair Phi||_2^2 + ||Phi_0||_2^2/2
 = integral_0^T <J,Phi>
   + (1/N) integral_0^T <Phi,B Phi>
   + integral_0^T <Phi,R Phi>.
```

The initial norm has the required positive sign. Its upper bound is the sum of a constant times N to power a and another constant times N to power two a minus one. Since a lies strictly between zero and one, the latter is bounded by a constant times N to power a. The constants remaining are exactly C_J, C_infinity, kappa, and the horizon. All fixed-N derivative constants were used only for legitimacy of the operations and disappear from this estimate.

### Exact finite-N algebra and the meaning of the brackets

Differentiating the original ordered-pair statistic, including both background terms, gives

```text
grad_i P = N^-2 sum_(j != i) G(X_i,X_j) - N^-1 A(X_i)
         = N^-2 [sum_(j != i) H(X_i,X_j) - A(X_i)].
```

Conditioning on the first variable under Haar product measure kills the distinct H-H terms and H-A terms. The remaining square is `(N-1)||H||_2^2 + ||A||_2^2`, divided by N to the fourth, for each particle. Orthogonality then gives the exact Haar formula on the card. In particular the N=2 coefficient is one-eighth of the first-slot gradient norm squared; the N=3 numerator is twice that norm squared minus the A norm squared, divided by 27. If G equals A, the result is the A norm squared divided by N cubed, not zero.

Multiplication by the prescribed scale and by twice diffusivity, followed by pair symmetry, gives the prefactor `b_N (N-1)/N^2` multiplying the full pair Dirichlet energy. This yields the stated reference-noise rate. Direct differentiation of the leading empirical test gives its reference functional `2 b_N nu integral ||grad f||_2^2`; the product b_N times nu is the minimum of one and nu. Applying Cauchy–Schwarz with the same nonnegative measure to the absolute cross density proves the asserted cross rate. A signed average could cancel while the average absolute value is positive; the proof does not make that replacement.

For a general exchangeable law, no conditional-Haar cancellations are available. Expanding the same field before taking expectations gives N minus one equal-label squares, `(N-1)(N-2)` ordered distinct-pair products, minus twice N minus one mixed H-A terms, and one A square, with outside factor N to the minus third. This proves the four-term identity. It applies wherever the stated fields and integrals are defined. On collision-supported laws the stipulated singular corrector has no automatically defined derivative; the proof explicitly labels any extension as a finite-sum field rather than claiming a derivative or trace there. This does not affect any actual or Haar law in the theorem. No integrability under an arbitrary unbounded law is inferred merely from Haar H1 regularity.

For the actual bounded-density law, the H-square and A-square terms are integrable by the Haar L2 bound and density domination. The Haar triple absolute integral is at most the H norm squared, by integrating the two independent background slots and applying Cauchy–Schwarz. The mixed absolute integral is bounded by the product of the H and A norms. The fixed-N density factor therefore suffices for existence of every expectation and time integral, with no uniform-smallness claim.

### Actual singular laws and the remaining reduction

For each fixed translation, translating a collision-free realization preserves the actual singular equation with the same driver. Permuting labels and their independent Brownian drivers preserves the equation as well. For each fixed collision-free initial configuration, the joint measurable realization and pathwise uniqueness identify the transformed law. Integrating the per-start null sets against the independent initial Haar distribution is legitimate. This proves equivariance without a probability-one event uniform over all translations or starting configurations. At zero noise the same uniqueness argument applies to the deterministic flow.

Thus the actual law is exchangeable and invariant under every common translation. Averaging the one-particle invariance against Haar translations proves that the one-particle marginal is Haar. These symmetries do not imply product higher marginals. The invariant density on R9 lines 416–422 is a concrete counterexample to that inference.

The three R9 deviations are exactly: the H-square pairing with the pair density minus one, the H-H pairing with the triple density minus one, and the H-A pairing with the pair density minus one. The first marginal supplies the identical A-square term in the actual and reference laws. Consequently the difference of scaled expected brackets has outside factor `2 nu b_N/N^2` and inside coefficients `N-1`, `(N-1)(N-2)`, and `-2(N-1)` respectively. At N=2 the triple is absent as an object, not multiplied by zero after being left undefined.

The source realization supplies a fixed-N time-uniform density bound. The jointly measurable probability kernels give a measure on time times configuration space, absolutely continuous with respect to time times Haar; its Radon–Nikodym derivative supplies a jointly measurable version for the integrated pairings. Fubini then identifies the same reductions expressed as expectations. This is sufficient for the claimed measurability and absolute integrability.

The first unproved line **beyond** this conditional gate is a suitable N-uniform bound on the signed law-error combination in R9 equation (10.2), lines 449–455, or on the stronger absolute quantity in equation (10.3), lines 462–469. That bound is not claimed in THM029. The fixed-N comparison by `exp[(N-1) kappa T]` does not discharge it. An actual bracket bound would in turn control the expected absolute cross functional because the leading expected noise depends only on the already identified first marginal. None of these implications supplies the missing marginal estimate.

## Independent exact diagnostic

New checker: `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact.py`. It was written in this isolated context without reading, importing, running, or adapting any constructor or previous checker. It uses Python's standard library only, with exact rational real and imaginary Fourier coefficients. It differentiates the original N-variable statistic first and integrates Fourier products by coefficient matching; this is distinct from testing a formula by numerical quadrature.

The first executed run passed **3,832 exact assertions**. The recorded result is `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/round009_energy_hostile_exact_result.json`. There was no failed run, proof modification, coefficient adjustment, or tolerance selection. No random input is used.

The finite Fourier functions depend on one angular coordinate and therefore embed in every admitted torus dimension. For the gradient algebra, derivatives are normalized by two pi; the missing common squared factor appears on both sides. The direct Coulomb force/derivative calculation restores the cancelling two-pi factors and normalizes its positive constant c_d to one. The test does not substitute a one-dimensional Riesz singular model for the theorem.

- The checker differentiates constant, separable, relative, and mixed third-frequency symmetric kernels directly for N=2,3,4. It checks the finite-sum field, conditional centering, exact Haar identity, both gradient slots, and nonzero deletion term.
- Positive exchangeable laws include Haar, two nonproduct common-translation-invariant densities, and a non-Haar biased exchangeable density. All four general-law terms are compared to the direct statistic square. Nonzero pair, triple, and mixed deviations are all exercised. The non-Haar case also detects the necessity of retaining a potentially different one-body A-square term before specializing to Haar marginals.
- The scaled marginal-error identity and its absolute majorant are tested for zero noise and positive rational diffusivities on both sides of one. The leading-noise prefactor is derived directly from the empirical statistic.
- Independent invariant mixed examples with angular frequencies m=2,3,4 give mixed expectation epsilon times m divided by four. With epsilon two-fifths these are one-fifth, three-tenths, and two-fifths; m=2 also checks the submitted example.
- The actual Fourier force coefficients are used to compute the Coulomb B quadratic form independently of the integration-by-parts formula. For a constant kernel, bulk one plus flux minus one gives zero. For the smooth relative kernel one minus cosine, the diagonal is zero and the B form is positive three-halves. Thus a false full-drift dissipativity claim would be detected. Annular radial calculations check the exact inner and outer fluxes below and at Coulomb.
- Finite Fourier calculations include both response slots and the zero mode. Rational scalar terminal-zero energy tests detect the wrong initial-norm sign. Exact radial-profile calculations test its transport identity, diffusion sign, cutoff-drift absorption premise, and all-N supremum power. Rational exponent calculations include the Coulomb and derivative-weight endpoints.
- Lagrange's exact sum-of-squares identity checks the absolute cross bound's finite-vector step. A separate cancellation example has absolute average one and signed average zero. The singular realization's symmetry is justified analytically above; the checker only tests the independent force-difference and label-counting algebra.

These computations are corroborating exact diagnostics. They do not prove the global singular domain, convergence, finite-measure operator extension, or Cauchy–Schwarz passage in place of the analytic arguments.

## Exposure, changes, verification, and handoff

The detailed exposure inventory is `AUDITS/HOSTILE/ROUND_009_ENERGY_ARTIFACTS/EXPOSURE.md`. The twenty allowlisted sources and their manifest were the only repository source inputs. No other audit, blind reconstruction, root seed, constructor checker, memory file, canonical state/history, or inherited worktree source outside the allowlist was opened. No child agent was used.

Only the assigned isolated worktree contains new audit outputs. Root/canonical files, frozen source bytes, and historical reports were not edited. There were no commits, pushes, dependency installations, contacts, or changes to remotes. The new worktree and branch were explicitly authorized by TASK059. No TeX source is changed or created; the final handoff contains no mathematical LaTeX.

Verification commands and outcomes are recorded in the companion README: all twenty SHA-256 input checks passed; the exact checker passed 3,832 assertions; artifact text hygiene and the scoped diff check passed; the exact archive member list, archive CRC, and every archived input/output digest passed. Output hashes and a separate archive/manifest seal make this issued packet immutable. A subsequent correction must be a newly named superseding report.

**First unsupported line within the submitted conditional implication: none found.** **Unresolved work outside this gate:** independent disposition of THM028 and a proved actual-law marginal-error estimate. Root owns integration, canonical audit identifiers, and comparison with the separate blind review. This packet grants no independent status to those withheld results and no fluctuation-law or temperature-regime closure.
