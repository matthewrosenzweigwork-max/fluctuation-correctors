# Round 003 fresh hostile review: transport model and sharp iid pair criterion

Issued 2026-09-17 UTC by `/root/r003_fresh_hostile`.
Published starting commit: `2f532ccd2cb5f3d84db456be96e438f03f7e2ad2`.
Branch: `codex/hocf-r003-fresh-hostile`.
Worktree: `/private/tmp/hocf-r003-fresh-hostile-20260917`.

**Verdict:** THM-017, THM-018, and THM-019 pass this fresh hostile review in their stated scopes. The punctured diffusion rescaling identities also pass. One scalar-coefficient sentence in the diffusion memorandum is overbroad and fails as written; the exact correction is recorded in FH-D01 below. It does not invalidate any of the three theorem cards or the rescaling identity. No candidate input was edited.

This is a fresh **HOSTILE_REVIEW**, not a blind reconstruction or an external audit. Candidate proofs were deliberately available. The reviewer had not constructed the submitted claims and did not read other Round 003 reviews, sharp reconstructions, other workers' code, or root TeX. The only new mathematical inputs copied from the root are the eight sealed files listed in Section 8. The permitted probability reconstruction was read for the L1 construction and its elementary prerequisites. The collision memorandum was used for normalization and the iid projection prerequisite. No status label in an input was accepted as proof.

Governing instructions and the frozen model were read from the stated baseline. The bounded input restriction takes precedence over generic whole-campaign onboarding for this isolated audit. Canonical state remains the root coordinator's responsibility. Creation of this explicitly requested branch/worktree changed Git worktree metadata; no canonical root file, candidate, historical input, existing audit, ledger, or other worktree was written. No child, commit, push, installation, or remote operation occurred.

## 1. Assertions, negations, and per-result dispositions

The exact primary assertions under review are the displayed transport solution and its declared norm/endpoint estimates; the initial iid L1 upper bounds; the positive-probability and matching first-moment bounds for the bare Haar pair and their temperature/tightness consequences; and the punctured chain-rule identities in the diffusion note. Their logical negation is an admissible parameter, function in the specified class, Haar configuration law, or positive temperature sequence violating one of those assertions.

| Result | Verdict | Qualification |
|---|---|---|
| Frozen Riesz normalization and local coefficient one | PASS | Independently checked from the supplied heat integrals; fixed positive s only. |
| Exact iid projection, bias, and second moment | PASS | Full background centering and the N-squared denominator retained, including N=2. |
| THM-017 characteristic solution and uniqueness | PASS | Exactly the stated forward absolutely-continuous characteristic class on the punctured space. |
| THM-017 angular collision behavior and local squared norms | PASS | Angular discontinuity is retained; no collision-domain or singular Itô conclusion. |
| THM-017 diagnostic iid endpoint, including all finite N | PASS | FH-C01 below explicitly supplies the all-N deduction from the submitted inequalities. |
| THM-018 L1 rates | PASS | Initial iid Haar bare pair only, with constants and threshold independent of temperature. |
| THM-019 positive lower probability and matching L1 order | PASS | The dependent events are handled by subtraction of unconditional probabilities. |
| THM-019 convergence and tightness consequences | PASS | FH-C02 states the further-subsequence step explicitly. No endpoint distribution identified. |
| Diffusion-note punctured chain rule and angular equations | PASS | Differential identities only; no existence, domain, operator convergence, or solution limit. |
| Diffusion-note last subcritical sentence, line 37 | FAIL as an unrestricted fixed-parameter assertion | FH-D01: rate dependence occurs only when d is greater than s+2. |

The source status of the reviewed inputs is **proved directly from the permitted elementary model**, with no critical imported theorem or unverified external reference. Exact arithmetic checks support the coefficient review; they do not certify a singular dynamic theorem.

## 2. Normalization and iid centering

Write \(a=(d-s)/2\). For the periodized Gaussian heat kernel, the coefficient multiplying the heat integral is

\[
 B=\frac{4^a\pi^{d/2}}{\Gamma(s/2)}.
\]

Its nonzero Fourier coefficient is

\[
 B\Gamma(a)(4\pi^2|k|^2)^{-a}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}|k|^{s-d}.
\]

Multiplying the Euclidean heat kernel by the same prefactor and substituting \(u=|z|^2/(4t)\) gives exactly \(|z|^{-s}\). There is no missing factor of two, Fourier factor, or normalization sign. The supplied small-time image bounds and large-time Fourier bounds justify integration in L1 and every derivative of the local remainder. Consequently the representative is even, mean zero, smooth off the origin, and equals \(|z|^{-s}\) plus a smooth remainder locally. The positivity, discarded-mass estimate, and truncated second-moment estimate needed below follow by shrinking one fixed embedded ball. Constants depend on fixed d,s; no uniform limit as s approaches zero, d/2, or d is asserted.

For a real symmetric L2 kernel H under an iid probability law, independently expand

\[
 m=\mu^2(H),\quad q(x)=\int H(x,y)\,\mu(dy)-m,
 \quad r(x,y)=H(x,y)-m-q(x)-q(y).
\]

The original ordered deleted-label definition gives

\[
 P_N[H]=-\frac{m}{2N}-\frac1{N^2}\sum_iq(X_i)
            +\frac1{N^2}\sum_{i<j}r(X_i,X_j).
\]

In particular its expectation is \(-m/(2N)\), not zero in general. Conditioning on shared labels gives the exact orthogonality and hence

\[
 \mathbb E P_N[H]^2
 =\frac{m^2}{4N^2}+\frac{\|q\|_2^2}{N^3}
    +\frac{N-1}{2N^3}\|r\|_2^2
 \le\frac{N-1}{2N^3}\|H\|_2^2.                 \tag{A}
\]

Here \(\|H\|_2^2=m^2+2\|q\|_2^2+\|r\|_2^2\). Comparing the three coefficients proves the inequality for every N at least two, with equality for every symmetric kernel at N=2. Constant, pure first-projection, and canonical kernels all retain their expected nonzero coefficients. There is no self-label trace. For the bounded-density law in THM-017, the spatial diagonal is product-null; for the Haar difference kernels below, mean zero makes the statistic exactly the unordered bare sum.

The finite-law checker described in Section 7 recomputes this identity directly from the original definition, using unequal atom weights and exhaustive configurations. Thus it also tests a setting where distinct labels can coincide in space, without silently deleting such coordinates.

## 3. THM-017: independent transport and collision checks

Put \(p=s+2\), \(c=2sp\), \(\tau=T-t\), and \(a(\theta)=\theta^TA\theta\). Along a forward characteristic,

\[
 \dot r=(2s/N)r^{-s-1},\qquad r(h)^p=r^p+ch/N.
\]

Every such characteristic starting away from zero reaches the terminal time without a collision. Integrating the source along it gives

\[
 \Phi_N(t,z)=s a(\theta)\int_0^\tau(r^p+ch/N)^{-s/p}\,dh
 =\frac N4a(\theta)\big[(r^p+c\tau/N)^{2/p}-r^2\big].
\]

The factor N/4 can also be checked by replacing time integration with radius integration: the integrand becomes \((N/2)r\,dr\). Direct differentiation gives the submitted PDE with its negative right-hand side. All forward characteristic values are determined by their terminal values, proving uniqueness in the stated class. An attempt to add arbitrary collision-boundary data does not produce a different member of this class, because no forward characteristic starting at a permitted point reaches that boundary before the terminal time. No claim of uniqueness in a larger distributional class is needed or reviewed.

The profile \(H(u)=(1+u^p)^{2/p}-u^2\) obeys

\[
 H(u)=\frac2p\int_0^1(u^p+v)^{-s/p}\,dv.
\]

This gives the submitted core and far-field bounds, with the exact core radius \(\ell=(c\tau/N)^{1/p}\). The far-field second coefficient is \(-s^3\tau^2/N\), so the repulsive transport decreases the positive radial amplitude relative to the static source. The factor of two is correct for relative coordinates and survives the explicit N=2 and N=3 substitutions.

For positive remaining time the collision limit is \(F_0 a(\theta)\), with

\[
 F_0=\frac14c^{2/p}N^{s/p}\tau^{2/p}.
\]

It is direction independent precisely for scalar A. The traceless degree-two part satisfies \(\Delta_{S^{d-1}}a_0=-2d a_0\); expanding the profile therefore reproduces the singular angular Laplacian term \(-2dF_0r^{-2}a_0\) and the constant term \(-N\operatorname{tr}(A)/2\). A zero angular average does not remove this term or its square norm. For scalar A the claimed Hessian at coincidence is correct. The punctured field tends uniformly to zero as remaining time tends to zero for fixed N, which is compatible with discontinuity at collision at every earlier time. No distributional extension or singular Itô step is hidden in these conclusions.

The fourth spherical moment gives

\[
 Q(A)=\frac{|S^{d-1}|}{d(d+2)}
       \big[(\operatorname{tr}A)^2+2\operatorname{tr}(A^2)\big].
\]

This is positive for every nonzero symmetric A, including a nonzero traceless matrix; the dimension-one formula uses the two-point sphere and has no traceless mode. Polar integration then gives exactly

\[
 \|\Phi_N\|_{L^2(B_R)}^2
 =\frac{Q(A)N^2\ell^{d+4}}{16}
      \int_0^{R/\ell}H(u)^2u^{d-1}\,du.          \tag{B}
\]

The core contribution and the tail \(H(u)\sim(2/p)u^{-s}\) reproduce all three two-sided powers, the logarithmic boundary, and the submitted asymptotic constants. The large-core case is also covered by the exact integral, so no relation between N and remaining time is silently imposed.

The compactly supported diagnostic is a well-defined even L2 torus kernel. Its cutoff multiplication introduces exactly the stated annular source. The autocorrelation of a density bounded by M is at most M, so only one factor M is needed in passing from Lebesgue square norm to the pair norm. Applying (A) proves the submitted endpoint coefficient, with all bias and first-projection terms retained.

### FH-C01: explicit all-N clarification

The theorem card starts with every N at least two, whereas the display (7.4) in the proof is presented for sufficiently large N. This is not a false estimate, and no additional hypothesis is needed. For completeness, the following deduction from the submitted inequalities closes that wording gap explicitly, without changing any candidate.

Let \(S_{N,\tau}=\mathbb E|\sigma_NP_N[\mathcal H_{N,\tau}]|^2\), keep the fixed outer cutoff radius R, and set \(\alpha=2/p\). For \(2s<d\), the global upper bound \(F\le s\tau r^{-s}\) gives for every N

\[
 S_{N,\tau}\le\frac{b_N}{N}
       \frac{M Q(A)s^2T^2R^{d-2s}}{2(d-2s)}.
\]

For \(2s>d\), the integral in (B) is at most
\(1/d+\alpha^2/(2s-d)\), independently of its upper limit. Thus

\[
 S_{N,\tau}\le\frac{M Q(A)c^{(d+4)/p}}{32}
 \left(\frac1d+\frac{\alpha^2}{2s-d}\right)
 T^{(d+4)/p}b_N N^{-(d+2-s)/p}.
\]

At \(2s=d\), the integral is at most \(1/d+\alpha^2\log_+(R/\ell)\) for every positive upper limit. Set \(a_R=R^p/c\). Since

\[
 \log_+(R/\ell)\le\frac{\log N+\log_+(a_R/\tau)}p,
 \qquad \tau^2\log_+(a_R/\tau)\le\frac{a_R^2}{2e},
\]

one obtains for every N at least two

\[
 S_{N,\tau}\le\frac{M Q(A)c^2}{32}
 \left[\frac{T^2}d+\frac{\alpha^2T^2}p
                    +\frac{\alpha^2a_R^2}{2ep}\right]
 b_N\frac{1+\log N}{N}.
\]

At zero remaining time the statistic is zero, so no division by zero is involved. These constants are independent of N, temperature, and remaining time. The supremum remains outside the expectation. Two-sided endpoint orders in the submitted proof apply to its special Haar, nonzero traceless, fixed-positive-time diagnostic, not to every density or matrix.

## 4. THM-018: the L1 argument is complete

For a spatial radius r in the fixed embedded ball, write

\[
 k_r=g\mathbf1_{\{|z|\ge r\}}+\tau_r,
 \qquad l_r=g\mathbf1_{\{|z|<r\}}-\tau_r,
 \qquad \tau_r=\int_{|z|<r}g.
\]

Both kernels have zero Haar mean and sum to g. The centered outer kernel belongs to L2; the inner one only needs L1. Its absolute mass is bounded by twice the discarded absolute mass D(r). Thus the exact unordered-pair coefficient gives

\[
 \mathbb E|\sigma_NP_N[g]|
 \le\sqrt{\frac{b_N}{2N}}\|g\mathbf1_{\{|z|\ge r\}}\|_2
          +\sqrt{Nb_N}\,D(r).                   \tag{C}
\]

There is no event condition, conditional variance estimate, hidden mean subtraction, or use of an infinite second moment in (C). Substituting \(r=N^{-2/d}\) gives the submitted exponent \(2s/d-3/2\) when \(2s>d\). At equality, the outer square integral is logarithmic and the inner contribution is of order \(\sqrt{b_N/N}\). Below equality the untruncated L2 bound directly gives the first rate. The constants in Sections 2, 4, and 7 of the probability reconstruction are finite and give exactly the bounds claimed in THM-018. The stated threshold \(N\ge r_0^{-d/2}\), with \(r_0=1/4\), is independent of temperature.

The heat representation supplies the L1 representative; a finite union of Haar collision events has probability zero. Thus the statistic is finite almost surely and integrable for every finite N even in the infinite-second-moment range. No conclusion about the actual pair backward kernel or an evolved dependent law follows.

## 5. THM-019: independent attack on the lower probability

Fix \(d/2<s<d\), set \(R_N=N^{-2/d}\), and take N large enough that this ball lies inside the fixed positivity ball. Let Z count unordered pairs at distance less than \(\delta R_N\). Its pair probability and mean are

\[
 q_N=v_d\delta^d/N^2,\qquad m_N={N\choose2}q_N.
\]

For two pairs with one shared label, conditioning on that label leaves two independent uniform positions with the same constant ball probability. Thus distinct indicators are pairwise independent, but mutual independence is neither asserted nor used. In particular

\[
 \mathbb EZ^2=m_N+{N\choose2}\left({N\choose2}-1\right)q_N^2
 \le m_N+m_N^2,
\]

and Cauchy--Schwarz yields the stated lower bound
\(\mathbb P(Z>0)\ge c_0\delta^d\), where
\(c_0=v_d/[4(1+v_d/2)]\). This holds already at N=2 whenever the ball is embedded. A finite cyclic Haar check in Section 7 confirms that the second-moment identity can hold while the triangle indicators are not jointly independent.

Let \(u_N=N^{2s/d-2}\). The exact splitting is

\[
 P_N[g]=P_N[k_{R_N}]
  +N^{-2}\sum_{i<j}g(X_i-X_j)\mathbf1_{\{|X_i-X_j|<R_N\}}
  -\frac{N-1}{2N}\tau_{R_N}.                  \tag{D}
\]

Every inner summand is nonnegative. On the close-pair event at least one gives \(\delta^{-s}u_N/2\). The mean correction is at most \(C_\tau u_N/2\). The outer canonical variance is at most \(C_Vu_N^2/2\), because

\[
 N^{-2}R_N^{d-2s}=u_N^2.
\]

Accordingly the unconditional probability of
\(P_N[k_{R_N}]<-\delta^{-s}u_N/8\) is at most
\(32C_V\delta^{2s}\). Choose a fixed positive delta less than one with

\[
 \delta^{-s}\ge2C_\tau,\qquad
 \delta^{2s-d}\le c_0/(64C_V).
\]

Such a choice exists precisely because the argument is in the strict range \(2s>d\). Subtracting this bad probability from \(\mathbb P(Z>0)\), without assuming independence between the events, proves

\[
 \mathbb P\{P_N[g]\ge\delta^{-s}u_N/8\}
       \ge c_0\delta^d/2.                      \tag{E}
\]

The positive local contribution, the finite-N deterministic correction, and the dependence issue all survive this check. An explicit sufficient particle threshold is
\(N_0=\max\{2,\lfloor R^{-d/2}\rfloor+1\}\) for the chosen positivity radius R. Constants depend only on d,s and the frozen kernel, not temperature.

The L1 upper bound follows either from (C) or directly from (D) with both components centered. Its constant can be \(\sqrt{C_V/2}+C_\tau\); the lower constant is the product of the positive threshold and probability in (E). Thus the claimed two-sided first-absolute-moment order is established, without inferring probability failure from variance divergence.

Multiplication by \(\sigma_N=\sqrt{Nb_N}\) gives a probability lower bound at a fixed positive multiple of
\(\sqrt{A_N}\), and matching upper and lower absolute moments, where
\(A_N=b_NN^{4s/d-3}\). Therefore:

- If A_N tends to zero, the upper bound gives L1 and probability convergence.
- If it does not, a subsequence bounded below by a positive number and (E) exclude probability convergence; no uniform-integrability premise is needed.
- If A_N is bounded, the absolute-moment upper bound and Markov give tightness, with finitely many initial variables absorbed separately.
- If A_N is unbounded, a further subsequence tends to infinity; (E) then excludes tightness.

### FH-C02: explicit subsequence clarification

The last step uses a subsequence along which A_N actually tends to infinity, extracted from unboundedness. This is the precise version of the phrase “eventually exceeds” in line 118 of the sharp memorandum. The conclusion is valid even when the original sequence oscillates. This is a proof clarification, not an extra assumption or a repair of the theorem statement.

The square-root-N trichotomy follows at s=3d/4; the smaller-s upper bounds are supplied by THM-018. At microscopic criticality the frozen cap gives b_N eventually equal to one. No distribution at the trichotomy boundary, stable law, field tightness, or interacting-law result is thereby identified.

## 6. Diffusion rescaling and its exact defect

For \(\Phi_N=N^{s/p}F_N(\tau,N^{1/p}z)\), the time derivative changes sign, the Laplacian gains \(N^{2/p}\), and \(z\cdot\nabla_z=y\cdot\nabla_y\). After dividing by \(N^{s/p}\), the drift coefficient is exactly \(2s\), the source coefficient is s, and the diffusion coefficient is

\[
 2\chi_N,\qquad \chi_N=N^{2/(s+2)}/\beta_N.
\]

The fixed-positive-time core rescaling and its factor two agree with this identity. Applying the polar Laplacian to a separated degree-zero or degree-two angular component gives the stated equation and the angular eigenvalue 2d. The degree-two component is absent in dimension one. These checks use only sufficiently differentiable punctured tests; no boundary-domain realization, existence, collision behavior of a solution, or convergence of operators or solutions is inferred.

The exact temperature identity is

\[
 \chi_N=\lambda_N^{-1}N^e,
 \qquad e=\frac{s(s+2-d)}{d(s+2)}.
\]

The three scalar-coefficient conclusions at fixed positive microscopic critical limit are correct.

### FH-D01: subcritical scalar-coefficient prose is overbroad

**Location:** `MEMORANDA/ROUND_003_DIFFUSION_RESCALING.md:37`, sentence beginning “Under full microscopic subcriticality”.

**Diagnosis:** The claim that no single diffusion-coefficient limit follows without the rate is overbroad for the fixed d,s of the memorandum. If \(d\le s+2\), then \(e\ge0\) and \(\lambda_N\to0\) forces \(\chi_N\to\infty\), independently of the rate. For example, at d=3,s=1 the identity is exactly \(\chi_N=1/\lambda_N\).

**Severity and confidence:** A definite scalar asymptotic error of limited scope; high confidence. It does not affect THM-017, THM-018, THM-019, the chain rule, the critical coefficient classification, or any claimed solution theorem, since none is made here.

**Exact correction:** Under full microscopic subcriticality, the coefficient necessarily tends to infinity when d is at most s+2. Only when d is greater than s+2 can its limit depend on the rate: choosing respectively \(\lambda_N=N^{e/2}\), \(N^e/c_*\) for fixed \(c_*>0\), or \(N^{2e}\) gives coefficient limits zero, \(c_*\), or infinity. Oscillating bounded positive choices for the coefficient likewise give subcritical sequences with no coefficient limit. All these statements concern the scalar coefficient alone.

**Disposition:** The input is preserved byte-for-byte. Root should record a separate erratum rather than editing the sealed note. The root acknowledged this exact correction after the reviewer first reported it; no other review or proof was supplied in that exchange.

## 7. Verification, limitations, and handoff

Verification used analytic reconstruction of the load-bearing equations above and a newly written exact checker, `VERIFICATION_CODE/round003_fresh_hostile_exact.py`. It uses Python 3.9.6 on Darwin, only standard-library exact fractions, no randomness, and no other worker's code. Its result is `CERTIFICATES/OUTPUTS/round003_fresh_hostile_exact.json`.

The checker passed 1,440 direct configuration identities, 16 iid moment/bound cases at N=2,3,4,5, two translation-invariant close-pair-count cases, and 351 rational parameter checks of the scaling exponents. Its cyclic Haar triangle probability is 1/7, while the product of the three marginal probabilities is 27/343, explicitly falsifying mutual independence in a diagnostic where the required pairwise identity remains exact. This is supporting finite-model evidence, not a replacement for the continuous proof.

Executed commands:

```text
python3 scripts/verify_campaign.py
python3 VERIFICATION_CODE/round003_fresh_hostile_exact.py
git diff --check
shasum -a 256 -c AUDITS/HOSTILE/ROUND_003_FRESH_HOSTILE_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_003_FRESH_HOSTILE_OUTPUT_SHA256SUMS.txt
```

The baseline campaign verifier and all listed checks passed. The report and checker were also checked for control characters, trailing whitespace, terminal newlines, and balanced display delimiters. The output manifest seals this report, the input manifest, the checker, and its exact output. It intentionally does not contain its own hash. Sealed outputs are not revised after issuance.

This review does not certify any full singular fluctuation theorem, the actual backward corrector, the formal full-operator residual of the transport memorandum, a singular generator passage, evolved-law estimates, martingales or brackets, a positive-temperature collision-domain realization, a non-Gaussian or stable law, or a logarithmic model. The unestimated full-operator comparison remains open. The permitted files are sufficient for the conclusions reviewed; no indispensable private source or unverified reference was encountered.

Root can integrate the three hostile passes, this explicit all-N clarification, and the separate diffusion erratum. No candidate source needs to be changed to obtain the three theorem-card passes. Final promotion and canonical audit identifiers remain root responsibilities.

## 8. Sealed inputs

Only the following new input bytes were copied from the root; each copy was compared to its source immediately after copying. Subsequent work used the worktree copies. Their SHA-256 values are also recorded in `ROUND_003_FRESH_HOSTILE_INPUT_SHA256SUMS.txt`.

| Input | SHA-256 |
|---|---|
| THEOREMS/THM-017_INTERNAL_PAIR_TRANSPORT_MODEL.md | `2c95e74ea8874e8d624d23a8ce2dfa9dfdca4eda9d796c9e403dda5277811c79` |
| THEOREMS/THM-018_IID_RIESZ_L1_RATES.md | `7526dbdbfbfaf20756830a8acfc33f3607a66e8d7aaf13d58a1e84e0d85e80cb` |
| THEOREMS/THM-019_SHARP_IID_RIESZ_PAIR_CRITERION.md | `bfcc98dd9f0edeaa24a91d0348fd9932bc4bce3a23443b9901f2aaa35a7181a1` |
| MEMORANDA/ROUND_003_PAIR_TRANSPORT_MODEL.md | `9cfe0d7b7fb970ce74e14f4d25b784437debeefac3e9d8a8e1ab47152514ef5d` |
| MEMORANDA/ROUND_003_SHARP_IID_PAIR_LOWER_BOUND.md | `98e9259f79bc09164f6e304e552da338ae4b93217f9d586912c03f54332d2268` |
| MEMORANDA/ROUND_003_COLLISION_FALSIFICATION.md | `9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4` |
| MEMORANDA/ROUND_003_DIFFUSION_RESCALING.md | `91ec6efbfb51b8eb1a4f76cd2beddf8d12031e424b1f95a01ce8e939cf1ede2a` |
| AUDITS/BLIND_RECONSTRUCTION/ROUND_003_PROBABILITY_RECONSTRUCTION.md | `9eb7e54ab0fa6e38ef226cd2d815d618d2b421718ed0e1c59bb07dc27ae79e6f` |

The baseline frozen model hash is `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57`. Governing files read were AGENTS.md, README_FIRST.md, MASTER_PROMPT.md, CAMPAIGN_PROTOCOLS.md, and MODEL_ORCHESTRATION.md at the published starting commit. No memory file, other review, sharp reconstruction, root TeX, or other worker code was consulted.
