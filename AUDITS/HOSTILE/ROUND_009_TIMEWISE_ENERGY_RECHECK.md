# TASK062 — supplemental review of the timewise Haar energy extension

Issued 2026-09-18 UTC after the original TASK059 packet was sealed. **Verdict: PASS_CONDITIONAL_EXTENSION.** The additional argument in the permitted TASK056 reconstruction proves a uniform Haar-L1 bound for the actual time derivative, a uniform Haar pair Dirichlet-energy bound at every deterministic time, and the corresponding timewise Haar absolute cross-density rate. The complete THM028 domain assertion and the stipulated R4–R6 modules remain explicit premises.

No unsupported line was found in this extension. The original integrated THM029 implication and the original TASK059 verdict are unchanged. This is a narrow supplemental review in the reused hostile context, not another fresh audit, not a blind reconstruction, and not certification of the entire TASK056 report. No actual-law asymptotic estimate follows.

## Exact reviewed claim and source

The newly exposed source is `AUDITS/BLIND_RECONSTRUCTION/ROUND_009_ENERGY_RECONSTRUCTION.md`, SHA-256 `7c4570bf133434ab3d216e1129f5315b1fc8fd45612bb27ade2cb2e279296307`. The reviewed extension is Section 3.2, lines 182–225, Section 4, lines 227–284, and the timewise consequences in Section 5, especially lines 341 and 367. Sections 1–3.1 and the indicated earlier module locations were inspected only to verify the extension's hypotheses, constants, and source identities. No verdict on the full blind report is issued.

Keep the exact frozen homogeneous model: unit Haar torus; integer d at least three; positive s at most d minus two; N at least two; finite horizon T; diffusivity between zero and a fixed finite upper bound; external drift zero; reference density one; the actual Fourier backward test of smooth real terminal h; and the given symmetric terminal-zero full pair inverse with both responses. Write a = s/(s+2). The additional conclusion is

```text
sup_(t,N,nu) ||partial_t Phi_t||_L1 <= C_dot,
nu ||grad_pair Phi_t||_L2^2 <= C_* N^a       at every deterministic t in [0,T].
```

Every constant depends only on the displayed fixed data and the fixed kernel/cutoffs, not on the selected N or diffusivity. For positive diffusivity with the frozen thermal scale, this yields

```text
sigma_N^2 integral_(Haar^N) 2nu sum_i |grad_i P_t|^2
    <= C_* b_N N^(-2/(s+2)),

sigma_N^2 integral_(Haar^N)
    |2nu sum_i N^-1 grad f_t(X_i) dot grad_i P_t|
    <= C_cross sqrt(b_N) N^(-1/(s+2)).
```

These inequalities hold timewise, uniformly in the indicated deterministic time. Integrating them over the fixed horizon gives integrated bounds as well. The logical negation tested is failure of one of these uniform conclusions under the full stated premises, including an unbounded normalized family at fixed admitted data. No pointwise conclusion is inferred solely from an integral estimate.

## Per-issue verdict

| ID | New issue and source location | Verdict |
|---|---|---|
| TASK062-E01 | Exact singular measure-domination constant and common kappa; reconstruction lines 186–193; R5 base proof (9.3) | PASS. The source exponent is twice C0 over N. Enlarging C0 to the permitted common kappa and then using N at least two gives the stated uniform L1 bound. |
| TASK062-E02 | Base L1 equality classes and strong continuity; reconstruction lines 186–193 | PASS. The source measure bound gives null-set independence and the L1 norm bound. Continuous-path convergence first treats continuous tests; density treats all L1 data. |
| TASK062-E03 | Both L1 responses, full Dyson evolution, and strong continuity; reconstruction lines 62–70, 195–204 | PASS. Finite-measure convolution is bounded on L1. Ordered simplex bounds retain the sum of interval lengths and do not require either Markov positivity of the full evolution or commutation of the two operators. |
| TASK062-E04 | Uniform C1(L1) source and full source identity; reconstruction lines 88–108, 206–213 | PASS. The bounded-diffusivity Fourier formula controls the necessary time-differentiated Hessian. Absolute occupation and simplex majorants identify the actual Borel inverse in L1 without any source-regularization interchange. |
| TASK062-E05 | Time differentiation and actual classical derivative; reconstruction lines 215–225 | PASS GIVEN THM028. Differentiating the changed-variable integral requires only strong continuity and C1 source data. THM028's fixed-N integrable time-derivative bound identifies the resulting L1 derivative with the actual classical one. |
| TASK062-E06 | Collision cutoff, Coulomb sign, and pointwise energy; reconstruction lines 229–275 | PASS GIVEN THM028. The diffusion cutoff term vanishes at fixed tuple by H1 and the cutoff capacity power. The internal annular flux has the correct sign and coefficient. No trace, unjustified flux limit, or N-dependent constant remains in the estimate. |
| TASK062-E07 | Timewise reference noise and absolute cross density; reconstruction lines 295–367 | PASS GIVEN THM028. The already checked exact Haar identity combines with the new energy estimate at the same time. Two spatial Cauchy–Schwarz steps give the timewise absolute bound; time integration is a later operation. |
| TASK062-E08 | Every deterministic time, endpoints, and zero cases | PASS. The argument is not restricted to almost every time, uses no division by diffusivity, includes N=2 and Coulomb, and handles terminal time, initial time, constant data, and zero horizon as described below. |

Confidence is high within the stated premises. No repair or weakened replacement statement is required. The checks below give the analytic justification, rather than using a finite computation as a proxy for any operator or singular-limit claim.

## Independent analytic check

### 1. Exact source measure bound and base L1 evolution

The full source is `MEMORANDA/ROUND_005_PERIODIC_PAIR_POTENTIAL.md`, lines 419–425 and 539–546. Its full pair drift has divergence bounded below by minus twice `(D_u + C0/N)`, and equation (9.3) gives, for every nonnegative Borel v,

```text
integral S_(t,t+r) v dm <= exp(2(D_u+C0/N)r) integral v dm.
```

Here D_u is the ordinary-transport divergence constant, not the divergence measure of K. In the present homogeneous model D_u is zero and the evolution depends only on r. The original singular measure-domination constant is therefore `exp(2 C0 r/N)`. It is not the L2 norm constant `exp(C0 r/N)` and is not the N-particle density exponent.

R5 lines 497–510 define C0 as the supremum of the negative part of the smooth remainder in its fixed local divergence decomposition. The permitted `AUDITS/ROUND_005_INTERFACE_SOURCE_AND_CONSTANT_ADDENDUM.md`, lines 13–20, specifies kappa as the maximum of that C0 and the R4 lower-divergence constant. Thus

```text
exp(2 C0 r/N) <= exp(2 kappa r/N) <= exp(kappa r),  N >= 2.
```

All three constants have the necessary independence from N and the selected diffusivity. At Coulomb the R4 measure is the positive atom minus its constant compensation; this is not discarded when choosing kappa.

For an L1 representative v, positivity of the base probability kernel gives `|S_r v| <= S_r |v|` wherever the latter is finite. The measure bound makes it finite for Haar-almost every starting pair. If two representatives differ on a Haar-null set, applying the same bound to their absolute difference gives zero L1 difference in their images. Truncation or approximation therefore defines a bounded operator on Haar L1 with exactly the bound used in reconstruction (3.8). No dynamics starting on the diagonal is required.

For continuous v on the full compact pair torus, path continuity at each fixed off-diagonal start gives `S_r v -> v` as r decreases to zero; bounded convergence first in paths and then in Haar gives L1 convergence. The diagonal is Haar-null. Continuous functions are dense in L1, and the above operator norms are bounded on each finite time interval, so the same convergence holds for every L1 v. The Markov composition extends by density, yielding strong continuity at all times. This reasoning is for each fixed N and diffusivity; uniform strong continuity in those parameters is neither needed nor claimed. The quantitative norm bound itself is uniform as stated.

### 2. The L1 full evolution and the singular source identity

For either response slot, Tonelli and translation invariance give

```text
||integral v(shifted slot) D(dw)||_L1 <= ||D||_TV ||v||_L1.
```

The same argument proves equality-class consistency even when D has its Coulomb atom. The atom multiplies the value at the current pair and supplies no pair-diagonal trace. The two-response bound is `C_R = 2||D||_TV`; at Coulomb this is four times c_d. It is independent of N and diffusivity.

Define the m-insertion Dyson term on L1 by integrating

```text
S_(r1) R S_(r2-r1) R ... R S_(r-rm)
```

over the ordered simplex `0 < r1 < ... < rm < r`. The sum of all intervening interval lengths is r. Applying the base norm bound to each interval therefore gives one factor `exp(2 kappa r/N)`, followed by `C_R^m r^m/m!`. The series converges in operator norm uniformly on bounded time intervals and has norm at most `exp((kappa+C_R)r)`.

For each fixed L1 input, the integrands are strongly measurable and strongly continuous in their interval arguments by the already established base continuity and boundedness of R. A change to a fixed simplex and dominated convergence proves continuity of each term. Uniform convergence of the series proves strong continuity of the full evolution. Its composition also follows by splitting the ordered insertions at an intermediate time and applying absolutely convergent Fubini. No commutation of S and R and no positivity of R or of the full evolution is used.

The actual Fourier test satisfies the prescribed homogeneous backward equation. Its multiplier is bounded by one; one time derivative introduces a coefficient bounded by a constant times one plus the squared Fourier frequency on the fixed diffusivity interval. Since h is smooth, the C2 Fourier series for both f and its time derivative converge absolutely and uniformly. Inserting either in the source gains one relative-coordinate power from the gradient difference. The resulting local majorant is a constant times `r^-s + 1`, which is Haar-integrable because s is less than d. This proves the asserted uniform bounds for J and its time derivative and proves `J in C1([0,T];L1)` by dominated differentiation and continuity.

For fixed t, absolute source occupation and the base L1 bound justify Tonelli for

```text
U_N(t) = integral_0^(T-t) S_r J_(t+r) dr
```

as an L1 identity for the actual Borel source potential. For the m-response contribution, the absolute integrated norm is at most

```text
C_J exp(kappa T) C_R^m T^(m+1)/(m+1)!.
```

This is summable. The Borel response actions agree with their L1 classes, so expanding the given bounded Borel Volterra inverse and regrouping its absolutely summable ordered integrals gives exactly reconstruction (3.10), for every t, as an L1 identity for the stipulated Phi. The argument uses the already constructed singular occupation formula. It does not use heat convergence of a singular source potential or assume that J lies in a generator domain.

### 3. Time derivative and its exact identification

Keep r as the integration variable in the identity just proved. Its dependence on t is only through the upper endpoint and J at t plus r. Strong continuity of the full evolution, C1(L1) regularity of J, and the common exponential norm majorant allow the L1 difference quotient to pass through the integral. The endpoint integrand is the full evolution at T minus t applied to J_T. Thus

```text
partial_t Phi_t = -T_(T-t) J_T
                 + integral_0^(T-t) T_r partial_t J_(t+r) dr
```

in L1, with norm at most

```text
C_dot = exp((kappa+C_R)T) (C_J + T C'_J).
```

This differentiates neither S nor T in a generator norm. It does not require an unproved bound on applying their generators to J.

The original kernel is the same L1 class at every t. Under the complete THM028 premise, its classical off-diagonal derivative is jointly continuous there and bounded in absolute value, uniformly over t at each fixed N and diffusivity, by an integrable multiple of the weight with local behavior `r^-s`. The pointwise fundamental theorem and dominated convergence therefore make the original kernel curve C1 in L1, with this actual derivative. Uniqueness of the derivative of that L1 curve identifies it with the displayed formula at every t, not only almost every t. The endpoint difference quotients are one-sided. The fixed-N bound is used only for identification; its value never enters C_dot.

The related formula in the permitted R8 memorandum, lines 473–525, is consistent with this calculation. Its weighted evolution constants are not used to obtain the new N-uniform estimate. This supplement takes the full THM028 domain as a premise and does not independently certify its proof.

### 4. Collision cutoff and pointwise energy

Choose a smooth cutoff between zero and one which is zero inside the radius-epsilon pair tube, one outside twice that radius, and radially nondecreasing in its embedded annulus. Its pair-gradient L2 norm is bounded by a fixed constant times epsilon to the power `(d-2)/2`. This follows by the annular volume of order epsilon to power d and the gradient of order epsilon to power minus one, with the two pair coordinates contributing the fixed factor two to the squared norm. The exponent is positive for every admitted dimension.

On the annulus, the pair vector field is `(K,-K)` and the cutoff is relative-coordinate radial. Consequently B applied to the cutoff is twice the radial derivative times the radial component of K, and is nonnegative for every sufficiently small epsilon. The local repulsive singularity dominates the fixed smooth odd remainder. Ordinary integration by parts away from the true diagonal gives

```text
integral theta Phi B Phi
 = -integral theta D_cl Phi^2
   - (1/2) integral Phi^2 B theta
 <= kappa integral theta Phi^2.
```

The full pair divergence is twice D_cl, canceled by the half from differentiating Phi squared. The displayed coefficient is correct. At Coulomb the bulk is positive c_d times the cutoff square integral, and the annular term is nonpositive. No limit of that annular term is asserted; its sign is enough. No value on the diagonal is introduced.

The diffusion cross term has absolute value at most

```text
nu ||Phi_t||_infinity ||grad_pair theta||_L2 ||grad_pair Phi_t||_L2.
```

For each fixed N, diffusivity, and time, the last factor is finite by the conditional domain. The cutoff factor tends to zero. This establishes the limit at that fixed tuple; it does not pass an N-limit through the cutoff or use a purported N-uniform gradient bound. Bounded Phi, the new L1 time-derivative estimate, the source L1 estimate, and bounded L2 response action justify all other pairings and limits. The response pairing is used with its global nonpositive Fourier sign only after removing the cutoff.

Rearranging the classical equation at the fixed time gives the pointwise inequality

```text
nu ||grad_pair Phi_t||_2^2
 <= integral Phi_t partial_t Phi_t + integral Phi_t J_t
    + (kappa/N) ||Phi_t||_2^2 + <Phi_t,R Phi_t>.
```

The sign in front of the time-derivative pairing is positive. Taking an absolute bound for that pairing is legitimate and is exactly where the newly quantified L1 derivative is used. The previously established supremum estimate is `sup_t ||Phi_t||_infinity <= C_Phi N^a`. Unit Haar mass and the response sign therefore give

```text
nu ||grad_pair Phi_t||_2^2
 <= C_Phi(C_dot+C_J) N^a + kappa C_Phi^2 N^(2a-1)
 <= [C_Phi(C_dot+C_J)+kappa C_Phi^2] N^a.
```

Since a lies between zero and one, the last exponent comparison is valid for every N at least two. This verifies reconstruction (4.3) with all constants independent of N and selected diffusivity. Each part of the argument was applied at an arbitrary fixed time, so the conclusion holds for every deterministic time in the domain premise.

### 5. Timewise reference rates and endpoints

The exact Haar statistic-gradient formula, already reviewed and sealed in TASK059, gives at the same fixed time

```text
sigma_N^2 integral 2nu sum_i |grad_i P_t|^2 dm_N
 <= b_N (N-1)/N^2 times nu ||grad_pair Phi_t||_2^2.
```

Pair symmetry supplies the factor two between full and first-slot gradient norms. Combining this identity with the new pointwise energy estimate gives the timewise corrector-noise rate. There is no need to repeat the finite-N checker to establish this new analytic step.

The leading reference density is exactly `2 nu b_N ||grad f_t||_2^2`, bounded by twice the uniform squared gradient bound because `nu b_N <= 1`. At each configuration apply Cauchy–Schwarz to the particle/vector sum, then apply Cauchy–Schwarz in Haar at that fixed time. The scaled integral of the absolute cross density is at most the square root of these two scaled reference densities. Thus its constant can be chosen as the square root of twice the uniform leading squared-gradient bound times C_*, and its rate is precisely the square-root b_N factor and the power N to minus one over s plus two. The absolute value remains inside the Haar integral. Integration in time is a subsequent valid operation over the fixed horizon.

At terminal time, Phi is zero, its spatial derivatives are zero, and the L1 derivative formula gives minus J_T. The pointwise energy and reference noise densities vanish there. At initial time the same L1 formula has its right derivative and all source/evolution terms remain finite. No interior-only conclusion is being extended to an endpoint without justification.

At zero diffusivity the L1 evolution and differentiation remain valid, while both noise densities are identically zero. No estimate is divided by diffusivity, and no finite inverse temperature is identified as its reciprocal. If the upper diffusivity bound is zero, this is the whole admitted interval. The range for finite positive inverse temperature remains the stated lower bound imposed by bounded diffusivity.

At zero horizon the kernel has only its terminal-zero value, so the pair gradient and all noise quantities are zero. If a time derivative at this degenerate interval is invoked through the stipulated classical equation, that equation gives minus J_0, agreeing with the endpoint formula and its finite L1 bound. Constant terminal data gives J, its derivative, and Phi identically zero by the Fourier formula and uniqueness. N=2 satisfies the same source and operator estimates, with the exact Haar coefficient already checked; no distinct-triple object is needed here. Coulomb is covered by the signed cutoff argument. No logarithmic kernel or uniform unweighted gradient bound is introduced.

## Scope, chronology, and immutable handoff

The original TASK059 output was completed and sealed before this task arrived. Its original archive hash is `236cfd03ac1a5fecf6139aad14f2212f9ac278f095f26433680f6a4aa9be4baa`; its outer seal hash is `c922995bab4d2ff4f7c89a70646ca3727e0b0218f13e222219eef98f45505aa5`. Both the original output manifest and the original outer seal were verified before reading the newly allowed reconstruction and again before issuing this supplement. Every original report, checker, result, archive, and seal remains byte-identical.

The new twenty-two-file manifest is `AUDITS/ROUND_009_TIMEWISE_RECHECK_INPUT_SHA256SUMS.txt`, SHA-256 `bef323e0729ec273e493e27560dd30ca97115f9431a075c6bc9c56d8d1e98f14`. Its original twenty sources matched the already verified worktree bytes. Only TASK062 and the specified TASK056 reconstruction were newly copied; both were hash-verified and made read-only. This reused context had already seen the original R9 constructor proof and had issued its independent hostile verdict. It then read the specified reconstruction through line 380, including the initial lines of Section 6 incidentally; the review's mathematical verdict is restricted to the extension identified above. The reconstruction's other audit/checker references were not followed.

No ongoing R10 input, root memory, other audit, canonical state, external website, private source, or inherited file outside the new allowlist was read. No root/canonical source, frozen card, or either original report was edited. No child, dependency installation, commit, push, or remote change occurred. The existing isolated branch `codex/hocf-r009-energy-hostile` was retained. The prior exposure inventory remains part of the original packet; this paragraph records only the newly authorized exposure after its seal.

No new computational diagnostic is added: the new issues are L1 operator construction, equality-class/source identification, time differentiation, and a singular cutoff limit, for which the written checks above provide the relevant verification. The original 3,832-assertion diagnostic remains preserved and is not relabeled as a new or timewise analytic certificate. There is no TeX change and the final handoff contains no mathematical LaTeX.

The new report is sealed by `AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK_OUTPUT_SHA256SUMS.txt`. The archive `AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK_ARTIFACTS/ROUND_009_TIMEWISE_ENERGY_RECHECK_20260918_023940_UTC.zip` contains exactly the twenty-two permitted inputs, their manifest, this report, and its output manifest: twenty-five files. The separate `AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK_SEAL_20260918_023940_UTC.txt` hashes that archive and both new manifests; it is outside the archive to avoid a circular seal.

Verification: all twenty-two input hashes passed; the original output/archive checks passed; new report text hygiene and the scoped diff check passed; the new output and outer manifests passed; and ZIP inspection verified the exact member list, CRC integrity, and every archived byte against its corresponding sealed source. From the isolated worktree, reproduce the integrity checks with

```sh
shasum -a 256 -c AUDITS/ROUND_009_TIMEWISE_RECHECK_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK_SEAL_20260918_023940_UTC.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_009_ENERGY_HOSTILE_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_009_ENERGY_HOSTILE_SEAL_20260918_022909_UTC.txt
```

**First unsupported line in the reviewed extension: none found.** The accepted strengthening concerns deterministic Haar reference functionals only. The original integrated scope is preserved explicitly; neither the frozen card nor either prior report is changed. Independent prerequisite disposition and uniform actual-law marginal-error control remain outside this supplement. Any later correction must be a new superseding artifact.
