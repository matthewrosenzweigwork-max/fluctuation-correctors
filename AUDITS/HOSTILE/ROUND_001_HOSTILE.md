# Round 001 hostile audit — frozen smooth identities and two negative claims

- Task: `TASK-008`; report version 1.0, prepared 2026-09-17 UTC.
- Auditor context: fresh `/root/hostile`, assigned Astra Max role.
- Worktree: `/private/tmp/hocf-round001-hostile-20260917`.
- Branch: `codex/hocf-r001-hostile`.
- Baseline HEAD: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Issuance: the report is issued only with its final SHA-256 in the completion message, after final input-integrity and report review. Once issued it is immutable; corrections require a new report.
- Canonical audit identifier and global ledger promotion remain the coordinator's responsibility.

## 1. Scoped verdicts

| Frozen claim | Hostile verdict | Exact scope |
|---|---|---|
| `THM-008` one-body identity, pair identity, and stated martingale brackets | **PASS — exact identities** | Every finite N at least two, positive finite beta, stipulated smooth deterministic data on the unit torus, arbitrary initial law; all configurations, including coincident coordinates |
| `ROUND_001_RECURSION.md`, (R1), (R3), (R4), (R5) | **PASS — exact identities** | Every finite integer k at least one, including k greater than N; fixed smooth model; the given ordered-label, N-power normalization |
| Universal weighted-energy floor (1.4) in `ROUND_001_FALSIFICATION.md` | **DISPROVED — counterexample accepted** | Arbitrary smooth symmetric nonnegative weights and all distinct-particle configurations, already in dimension one with 0<s<1 and reference density one; the strictly positive-weight extension is also valid |
| Universal lower singular order for (1.5) in `ROUND_001_FALSIFICATION.md` | **DISPROVED — counterexample accepted** | The specified pointwise remainder in dimension one, with a fixed smooth strictly positive symmetric weight and 0<s<1 |

No load-bearing defect was found in the two identity proofs or the two counterexample arguments. These verdicts rest on proof examination and recomputation, not on passing finite tests. No candidate input was repaired or edited during this audit.

This audit does **not** certify a singular stochastic identity, cutoff-uniform corrector estimate, microscopic power count, critical truncation, infinite resummation, Gaussian limit, or other fluctuation theorem. It does not promote an arbitrary-law result to an iid, Gibbs, stationary, or well-prepared result. The negative verdicts concern the two stated route assumptions; they do not disprove the campaign's fluctuation targets.

## 2. Frozen inputs, isolation, and provenance

Both supplied hash manifests were checked successfully before examining the candidate proofs. The mathematical dossier was limited to the following eight files; all were read. The final integrity check again found every supplied hash unchanged.

```text
3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57  TASKS/ACTIVE/ROUND_001_MODEL.md
8966a834d2f5d1968971cc42e9ffb089e81ad62e391cc0fb147c4f7ab3b1c287  THEOREMS/THM-008_SMOOTH_PAIR.md
e5db5923ba82bf929218e23fe641ed5a7387c106220e6374f37bd06b80c3e4de  MEMORANDA/ROUND_001_ALGEBRA.md
62027e0851f09fab2076207d3bb1785793021cd70af69689e310e745d5e468a8  MEMORANDA/ROUND_001_BBGKY.md
952a78af8b36e4847c867ec6f833ca0d5272005702daed1a58d9063332925dbd  VERIFICATION_CODE/round001_fourier_pair_check.py
f3657dc770aa1efe51c97e9ab95e6e4618ff4827f03d5f167d70f44d3e03c093  VERIFICATION_CODE/round001_bbgky_exact_fourier.py
bb6aeaa44c91cac7c5f1c0a0fc8199cc00cffb6ca23ee823df79167d0c650aae  MEMORANDA/ROUND_001_RECURSION.md
fa693536ba949985272a05e85a7a715b189b9b4f07b34a50cc2e81589030b823  MEMORANDA/ROUND_001_FALSIFICATION.md
```

Manifest hashes:

```text
da8ce235e042f7e9cd5f33bbe0b39982cefa6346cee6a1788cd1f998c7cb1515  AUDITS/HOSTILE/ROUND_001_PAIR_INPUT_SHA256SUMS.txt
3d38b22e915bf0214f7e35e3789ade7a3517c6eb1792be4ae3d316e8e53e4e6e  AUDITS/HOSTILE/ROUND_001_ADDITIONAL_INPUT_SHA256SUMS.txt
```

The ancillary conduct/scope files read in this worktree were:

```text
cc3a478358f1fcb3ccf472615c715acfdef575d9a80b5aa49417593a25825ed3  AGENTS.md
97ad15edbb28f67738de6d7b7dc2ae4e8abe309bede069ad08d18a2289dec2ce  README_FIRST.md
e49ee3901ea41494b36f251d16a72f1d06d6405a842cc09d889a2c87c1ef83e1  MODEL_ORCHESTRATION.md
455be54cfdf091f13bbfb0af09c339989644986dbafe3cb0acedce712e625c07  TASKS/ACTIVE/TASK-008_HOSTILE.md
```

The assigned frozen dossier and isolation restriction governed the mathematical reading scope. No other worktree, canonical state, source note, baseline mathematical narrative, constructor discovery script, memory file, or external source was read. No earlier constructor conversation was supplied to this context. The theorem statement was read before the proof narratives, and its pair drift was recomputed using the empirical full product and diagonal subtraction before the constructor derivation was examined. The all-order and negative-claim reviews were hostile examinations of the permitted proofs, not claimed blind reconstructions.

The claimed independent provenance of the BBGKY lane is recorded in its own report. This audit can verify the mathematics in its frozen output, but cannot independently attest to that worker's historical access controls. No mathematical verdict here depends on accepting an unobserved provenance assertion.

The directory initially contained the eight dossier files, task card, and manifests as untracked additions. They were preserved. No existing tracked file was changed, no dependencies were installed, and no branch, commit, instruction, remote, or canonical ledger was changed. The broad campaign verifier was not run because this audit was confined to the supplied dossier. The coordinator owns repository-wide integration checks.

## 3. Pair identity: decisive recomputation

The conventions are material: particle tuples are ordered; denominators are powers of N; the deleted diagonal deletes repeated labels; and K is odd with K(0)=0. Write A for the local operator in `THM-008`, R for its response, and C for its averaged three-slot kernel. In particular C here is the theorem's C, not the twice-larger BBGKY kernel.

The one-body force discrepancy expands as

\[
 \eta[(K*\rho)\cdot\nabla f]
 =\rho[Rf]+\frac12\rho^{\otimes2}[J_f].
\]

The diagonal of J_f is zero, so the last expression is exactly one half of U_2[J_f]. The reference equation supplies the local A term with the same diffusivity as the particles. This establishes the response sign and coefficient in `THM-008:12–17`, without a law assumption or limiting argument.

For the pair, set

\[
 Q[\Phi]=\tfrac12\rho^{\otimes2}[\Phi],\quad
 d_\Phi(x)=\Phi(x,x),\quad
 \tau_\Phi(x)=\sum_{a=1}^d\partial_{x_a}\partial_{y_a}\Phi(x,x).
\]

Direct finite-sum Itô differentiation gives

\[
 dQ[\Phi]=
 \left\{\tfrac12\rho^{\otimes2}[(\partial_t+L_2)\Phi]
       +\rho^{\otimes3}[C\Phi]+\frac\nu N\eta[\tau_\Phi]\right\}dt
 +dM_Q.
\]

The conversion to the claimed observable is exactly

\[
 P[\Phi]=Q[\Phi]-\frac1{2N}\eta[d_\Phi].
\]

The chain rule

\[
 \Delta d_\Phi=(\Delta_x+\Delta_y)\Phi|_{x=y}+2\tau_\Phi
\]

cancels the full-product trace. The corresponding transport and explicit test-time derivatives also cancel under diagonal subtraction. The remaining response diagonal is

\[
 \frac1N\iint K(z-x)\cdot\nabla_1\Phi(z,x)\,\eta(dx)\mu(dz),
\]

whereas the nonlinear part of the subtracted diagonal is

\[
 -\frac1N\iint K(x-z)\cdot\nabla_1\Phi(x,x)\,\eta(dx)\rho(dz).
\]

The cubic conversion has the sign and multiplicities

\[
 \rho^{\otimes3}[F]
 =U_3[F]+\frac3N(\eta\otimes\rho)[F(x,x,z)]
             -\frac2{N^2}\eta[F(x,x,x)].
\]

For the theorem's averaged C,

\[
 C\Phi(x,x,x)=0,\qquad
 3C\Phi(x,x,z)
 =K(x-z)\cdot\nabla_1\Phi(x,x)
   +K(z-x)\cdot\nabla_1\Phi(z,x).
\]

The first partial-diagonal term cancels the nonlinear diagonal subtraction. The other combines with the response diagonal, by adding rho and mu, to give

\[
 \frac1N\iint K(z-x)\cdot\nabla_1\Phi(z,x)\,\eta(dx)\eta(dz)
 =\frac1{2N}D_2[B\Phi].
\]

There is no suppressed all-equal term: its value is zero. Finally,

\[
 D_2[B\Phi]=U_2[B\Phi]+2\rho[(B\Phi)_\mu]+\mu^{\otimes2}[B\Phi]
\]

gives exactly the internal, order-one, and scalar terms in `THM-008:28–29`. This verifies the load-bearing steps in `ROUND_001_ALGEBRA.md:392–454` and its independent full-product check at lines 456–505.

Differentiating the original particle observable, rather than its drift formula, gives

\[
 \nabla_{x_i}P[\Phi]=N^{-1}H_i[\Phi].
\]

Thus the noise coefficient is sqrt(2nu)/N times H_i. Independence of the Brownian motions gives every bracket in `THM-008:34–36`; time-dependent deterministic tests produce no extra bracket term. Expanding H_i times H_i retains the shared nonroot label j=k and excludes j=i and k=i. The supplied constructor and BBGKY bracket expansions agree with this count.

### Comparison of the two proof conventions

The proof files use different letters and different cubic normalization:

| Theorem / algebra notation | BBGKY notation |
|---|---|
| local A / algebra L^0 | L |
| one-body L=A+R | A |
| pair L_2 | A_2 |
| B Phi | J Phi |
| C Phi | one half of the BBGKY C Phi |
| P | U_2/2 |

The BBGKY C is the averaged sum of the forces differentiating both pair slots. Hence it is twice the theorem's C, and the factor one half in BBGKY equation (3.6) is necessary. There is no disagreement between the two frozen pair identities.

I checked the marginal count in BBGKY (4.1)–(4.6): the probability-marginal coefficients are (N-1)/N for the one-body external force, 1/N for the pair's mutual force, and (N-2)/N for the pair's external force. Multiplication by the factorial normalizations converts the external coefficients to one. The single-background contractions of the raw cubic kernel give the two responses and the two first-marginal interaction terms. The double-background and triple-background contractions then give exactly its displayed centered identity. At N=2 the third probability marginal is not required. The marginal argument proves expectation identities only; the separate pathwise calculation and direct observable differentiation correctly supply the random identity and brackets.

The fixed-smooth backward construction in algebra Section 7 and BBGKY Section 2 also has no missing smooth-solvability step: integration by parts makes R bounded on each fixed C^m space; the smooth local diffusion gives a finite-horizon C^m propagator; the time-ordered Picard series converges by its factorial denominator. This supports backward duality only with constants allowed to depend on the stated smooth coefficient norms. It does not provide the uniform analytic estimate needed for the campaign.

## 4. All-order recursion and shared-label brackets

I checked `ROUND_001_RECURSION.md:127–194` directly as a finite-subset identity. For a set A of occupied slots, a force label either lies outside the tuple or is one of its other occupied labels. The former produces D_(A plus star) with coefficient one, because its extra normalization is the force's factor 1/N. The latter produces the directed internal sum with coefficient 1/N. Different occupied slots cannot have a Brownian cross derivative because their particle labels are distinct.

The inverse subset expansion is a genuine finite identity. For fixed derivative slot a and retained subset B, the external-force coefficient is

\[
 \sum_{A:\,B\cup\{a\}\subseteq A\subseteq S}(-1)^{|S|-|A|}.
\]

It is one exactly when B union {a} equals S, and zero otherwise. The only survivors are B=S and B=S minus {a}; these give the upward operator and the full response in that slot. There is no additional factor N-k.

For an internal directed pair a,b, the same coefficient is one exactly when B union {a,b} equals S. The four surviving subsets are precisely those listed at lines 185–192. Combining opposite directed pairs uses oddness of K. Grouping the single removed slot yields k/N times Q_k; grouping the unordered pair of removed slots yields binomial(k,2)/N times R_k. Because Q_k already sums k-1 pair operators, an extra k-1 outside it would be incorrect. The stated formula has no such extra factor.

These cancellations prove (R1) for every finite k. They remain legitimate when k exceeds N, because injection sums with too many occupied slots are empty while the finite subset identities remain unchanged. The k=2 reduction is exactly `THM-008`; the k=3 coefficients are 3/N and 3/N, and the k=4 coefficients are 4/N and 6/N, as claimed. The k=3 scalar cancellation is explicit in the memorandum and correct.

For the martingale, a particle can occupy exactly one of k distinguished kernel slots. Differentiation gives k/N times the excluded-label statistic V_(k-1) with denominator N, not N-1. This proves (R3) and its direct bracket (R4).

In the product of two rooted tuples, every shared nonroot label determines one edge of a unique partial bijection. Labels cannot be shared twice within one tuple; the root cannot match another slot. Conversely, an injective assignment to the quotient classes realizes exactly that partial bijection. For q shared nonroot labels the quotient has

\[
 1+|A|+|B|-q
\]

classes. Its normalization is therefore

\[
 N^{-2-|A|-|B|}N^{1+|A|+|B|-q}=N^{-1-q}.
\]

This verifies the power of N, all subset signs, absence of multiplicity, and exhaustiveness of (R5), including empty partial matchings and empty injection sums. At k=ell=1 it gives the one-body bracket; at k=ell=2 its q=1 term is exactly the shared nonroot label in the pair bracket. The theorem's P convention divides that bracket by four. No diffusion-lowering drift term is missing: the relevant Brownian contractions occur between statistics in their bracket, not between distinct labels inside one factorial term.

## 5. Weighted floor: examination of the counterexample

The one-dimensional Fourier normalization used by the negative argument is justified internally. For fixed positive Gaussian parameter, the periodized Gaussian has the stated Fourier coefficients by real-line Gaussian integration. The resulting Fourier series is absolutely convergent; its nonzero modes control the small-parameter end exponentially. At the large-parameter end the bracket in (1.1) has L^1 norm at most twice sqrt(pi/t), so integration against t^(s/2-1) is absolutely integrable precisely in the stated range 0<s<1. The substitution u=pi^2 k^2/t yields the displayed positive Fourier constant. Subtracting the central Gaussian integral gives the principal singularity |x|^(-s) with a smooth remainder in a fixed neighborhood of zero. Differentiating that remainder under the split integral is justified by the local exponential decay and integrable small-parameter bounds stated in the proof. No unverified singular source theorem is needed for this argument.

For the separated supports in `ROUND_001_FALSIFICATION.md:93–114`, positivity of the kernel on the two cross rectangles follows from that local expansion. Smooth nonnegative normalized bumps p and q with disjoint supports produce a fixed symmetric nonnegative weight. Its product h with the Riesz kernel is smooth and zero near the entire diagonal. Thus the proof does not hide a divergent diagonal evaluation or regularization passage.

With f=p-q, I recomputed the two cross rectangles. Both contribute negatively, and symmetry gives exactly

\[
 \tfrac12\iint h(x,y)f(x)f(y)\,dx\,dy=-A_0<0.
\]

The quantile densities are positive probability densities uniformly between one half and three halves. Their inverse distribution functions are 2-Lipschitz. The midpoint quantile coupling has the claimed bound 1/(2N), and strict monotonicity makes the particles distinct. For fixed smooth h, changing the two empirical factors and the mixed factor gives an error at most 2L times this Wasserstein distance. Hence the exact witness estimate is

\[
 \left|F_N^w+A_0a^2N^{-(1-s)/2}\right|\le L/N.
\]

All constants and the weight are fixed independently of N. The diagonal term in the proposed floor is zero. Its proposed remainder decays faster than the negative leading energy for every positive delta, and even for delta=0. The error L/N is smaller than that leading energy. The proposed all-configuration lower bound is therefore false along an explicit sequence of distinct configurations. Those empirical measures converge weakly to the reference density one; the proof does not assert a stronger microscopic preparation.

The strictly positive extension at lines 164–188 is also sound. Absolute integrability holds because s<1 and all densities and weights are bounded. The ordered-pair expectation under the perturbed product density has the claimed correction of size 1/(2N). Its limit is a fixed negative number when M is chosen as stated. An all-configuration bound tending to zero would survive averaging and contradict that negative limit; a violating distinct configuration therefore exists for every sufficiently large N. This is an existence argument, not a concentration statement.

Neither counterexample needs verification of the sharp zeta coefficient: the first has zero diagonal weight, and the second contradicts any fixed finite leading coefficient multiplying a power that tends to zero. The general sharp floor for a structurally restricted weight class is outside this verdict. The memorandum correctly identifies positivity of the continuum quadratic form as a necessary condition rather than a sufficient sharp finite-particle estimate. Its fixed-cutoff compatibility argument is valid on the separated compact support and does not certify a stochastic singular limit.

## 6. Diagonal-gradient remainder: coefficient and witness

For a symmetric smooth weight, put d(x)=w(x,x). Symmetry gives

\[
 \partial_1w(x,x)=\partial_2w(x,x)=\tfrac12d'(x)=a_x.
\]

At fixed x, the difference w(x,x-r)-d(x) is -r a_x plus an error of order r squared; the partial derivative in (1.5) is a_x plus an error of order r. Since the derivative of the principal Riesz singularity is -s r |r|^(-s-2), the two leading terms have the same sign. Their sum is

\[
 D_w(x,x-r)=\frac{1+s}{2}d'(x)|r|^{-s}
                +O(|r|^{1-s})+O(1).
\]

Thus the coefficient is 1+s, not 1-s. The periodic smooth remainder does not change the limiting ratio. For the explicit weight at lines 240–247, the diagonal derivative at zero is 2pi and the limiting ratio is pi(1+s), which is nonzero. This weight is symmetric, periodic, smooth, and at least one everywhere. It is a valid counterexample to the stated universal pointwise gain.

The retained local qualification is also correct: when d'(x)=0, both first partial derivatives vanish at that diagonal point, and the specified remainder is of order |r|^(1-s). A constant diagonal gives this gain uniformly. This conclusion concerns precisely (1.5); differentiating the diagonal value as part of a larger total derivative would be a different expression. No cancellation after integration has been assumed.

## 7. Reproducible tests and their limits

Environment: Python 3.9.6; standard library only. No dependency installation, random input, or numerical tolerance was used. The supplied verifier sources were inspected before execution.

Commands executed in the isolated worktree:

```sh
shasum -a 256 -c AUDITS/HOSTILE/ROUND_001_PAIR_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_001_ADDITIONAL_INPUT_SHA256SUMS.txt
python3 VERIFICATION_CODE/round001_fourier_pair_check.py > VERIFICATION_CODE/round001_hostile_supplied_pair_output.json
python3 VERIFICATION_CODE/round001_bbgky_exact_fourier.py > VERIFICATION_CODE/round001_hostile_supplied_bbgky_output.txt
python3 VERIFICATION_CODE/round001_hostile_contractions.py > VERIFICATION_CODE/round001_hostile_contractions_output.json
```

Results:

- Supplied uniform Fourier verifier: PASS, 45 raw and 45 decomposed comparisons. Of these 90 comparisons, 60 have positive diffusivity within the theorem's finite-beta scope and 30 use zero diffusivity as an additional algebraic degeneracy test. It covers N=2,3,4 and five pair kernels.
- Supplied BBGKY Fourier verifier: PASS, 24 exact rational cases, comprising 16 pair and eight one-body cases. Its extra comparisons of lower contractions, particle martingale coefficients, and pair cross brackets also pass. Its inhomogeneous cases differentiate the reference according to the mean-field PDE, rather than holding a nonstationary density fixed.
- New hostile test: PASS, 14,846 integer subset-coefficient checks through k=8; 216 exact rational partial-matching bracket checks; 72 exact rational free-diffusion checks; and 24 constant-statistic checks.

The new test imports no constructor helper. It computes derivatives of the explicit separable U statistic using elementary symmetric polynomials, and separately assembles the proposed bracket by quotient-class injection sums and partial-matching counts. It uses the smooth tests a(theta)=2+sin(theta) and c(theta)=3+cos(theta)+sin(2theta), uniform reference, zero force, angular diffusivity 3/7, and configurations at quarter-period positions. The corresponding unit-torus beta is finite and positive. Orders run from one through six, particle numbers are two through four, and both k>N and coincident coordinates occur. The diffusion comparison applies the particle Laplacian to the observable on one side and the slot Laplacian before subset insertion on the other.

The tests do not prove all smooth-kernel or all-order quantifiers. The supplied constructor discovery results and the recursion memorandum's reported 144 root checks were not rerun or independently attested in this audit. They are unnecessary for the proof-based verdicts above.

Manual degenerate-case checks also agree: the unit constant has U_2=-1/N and U_3=2/N^2; a time-dependent constant only differentiates that deterministic value. K=0 removes every interaction and response term. For a separable pair kernel, the full-product Brownian trace cancels the empirical diagonal derivative. At N=2 the all-distinct triple term is empty, but U_3 is generally nonzero. The one-mode N=2 calculation retains both the cubic cancellation of the response and the remaining mutual-force coefficient. No argument drops a centered statistic merely because its order exceeds N.

## 8. Defects, open lines, and handoff

No correction to a displayed coefficient, hypothesis, or proof step is required for the four audited claims. The different cubic normalizations are fully reconciled in Section 3; they are a notation hazard for integration, not a defect in the frozen candidates. The finite test battery's zero-diffusivity cases are extra tests, not evidence for an additional finite-beta theorem.

There is no first unproved line inside the audited finite-smooth algebra or the two counterexample arguments. The first unproved analytic lines remain exactly those already excluded from the candidate:

- `ROUND_001_ALGEBRA.md:865–877`: law-specific control of the scaled time-integrated cubic residual, the lower random contraction, initial corrector, deterministic centering, and pair/cross martingale brackets; singular use additionally requires cutoff-uniform corrector estimates and passage to the limit.
- `ROUND_001_RECURSION.md:507`: an order- and cutoff-explicit estimate in a declared function space and law class that decides effective gain, summability, or the need for an enlarged critical state. The finite algebra does not supply it.

The source-note agreement asserted in algebra lines 86–92 was not verified against the original note in this isolated audit and is not certified here. No load-bearing imported theorem or literature claim was used in the audited proofs. The one-dimensional singular normalization is checked for the negative claims only; general-dimensional singular normalization and the logarithmic model remain outside scope.

Created files are this report and four supporting files under `VERIFICATION_CODE/`: the new bounded test, its JSON output, and the two supplied-verifier output captures. Their hashes are:

```text
220da14c7a84c316b370ac2d83d82938ddec003ee0f9ec18faddbfacfcf99587  VERIFICATION_CODE/round001_hostile_contractions.py
1e2a5a1a97886b64ac08a277cee163fb56246958940e1514cfcaa16848e8f37b  VERIFICATION_CODE/round001_hostile_contractions_output.json
5740bb9fc70becdda66b260799c866c7a9c5c35061f30143ac3dd17fcea8cffb  VERIFICATION_CODE/round001_hostile_supplied_pair_output.json
224eb5f3818153137832c3a480bfeef2a224fefe16abd2fe8425a0d2030e6464  VERIFICATION_CODE/round001_hostile_supplied_bbgky_output.txt
```

No TeX artifact was created or modified; this deliverable is a Markdown audit, and no compilation or rendered-layout claim is made. Root alone integrates these files, assigns the canonical audit status, and updates affected ledgers. Issuance of this report certifies only the scoped hostile verdicts in Section 1.
