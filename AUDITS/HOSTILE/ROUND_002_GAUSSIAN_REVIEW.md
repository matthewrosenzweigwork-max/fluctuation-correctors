# TASK-017: hostile review of the fixed-smooth Gaussian criterion

Issued 2026-09-17 UTC by `/root/capacity`, Astra Max. Worktree: `/private/tmp/hocf-round002-hostile-20260917`. Baseline HEAD: `a06178658d1e3d458536ff312ca793947212ec67`. This is a separate immutable review of the submitted THM-011 card and Gaussian proof, not an amendment of TASK-015.

**Verdict: PASS within the stated fixed-smooth, iid, finite-dimensional, covariance-convergence scope.** No mathematical or rendering defect was found in the new Gaussian dossier. The exact corrected remainder, conditional martingale argument, triangular iid expansion, weak-limit passage, covariance diagnostics, and both stated temperature-endpoint conclusions pass separately below. This verdict does not assert the missing initial covariance limit at zero diffusivity, any singular limit, or the full M3 gate.

## Provenance and sealed inputs

This context first performed an operational Codex configuration investigation, then independently reconstructed the all-order smooth deleted-label algebra before seeing a constructor proof. Its blind report was sealed at `f96a78c701829b3744b0ffb05748db2aa38426f09da5eb9d26f85864a5e47747`; root owns its comparison. The context subsequently reviewed the two residual constructions and the smooth-data qualification. That separate TASK-015 report was sealed at `7e541f928f15236c15cd44572ac4d6f28abcbfde8ecd86cf616de14a586f8ca9` before this Gaussian dossier was received.

No Gaussian constructor narrative was seen before TASK-017. This is an independent hostile review of that construction, with the previously reviewed residual proof used as an explicit prerequisite. It is not a fresh blind reconstruction of the entire campaign. No other worktree, subsequent viscosity proof, or power-counting dossier was inspected for this review. No candidate proof or earlier report was edited.

The supplied `AUDITS/ROUND_002_GAUSSIAN_INPUT_SHA256SUMS.txt` was verified on receipt and before sealing. Its own SHA-256 is `5cd90a032cd81a8c96ac3c09a9f3768e62e7e5d7169c66d93420279665e3f07f`. It seals:

| Input | SHA-256 |
|---|---|
| `TASKS/ACTIVE/TASK-017_ROUND002_GAUSSIAN_REVIEW.md` | `fa9b78042de22dfc35f2ceba9bdf1097a3b54336434e682a19b42da855f6398b` |
| `THEOREMS/THM-011_SMOOTH_GAUSSIAN_CRITERION.md` | `7509a7754108c407475272b351a00dbaa419dbc990c1d184e0eab62ba26b7981` |
| `MEMORANDA/ROUND_002_SMOOTH_GAUSSIAN.md` | `7c581d5d9a34f7e0fd277c183321e4b789f10fe11e265e27cc461a2a2352438e` |

The complete 416-line Gaussian proof and complete theorem/task cards were read. Permitted prerequisites actually used are listed with hashes in `AUDITS/ROUND_002_GAUSSIAN_ADDITIONAL_INPUT_SHA256SUMS.txt`: the frozen model, PO-001, THM-008, COR-001, the sealed independent residual proof, and the prior hostile residual report. Administrative orientation read `AGENTS.md` and `README_FIRST.md`; no source-note mathematics was imported. The stale candidate-status text in the baseline THM-008 card is not treated as evidence; its formulas were checked against the independent reconstruction and the permitted reviewed pair identity.

TASK-015 identified a form-feed rendering defect in the original residual proof's pair bracket display. Its mathematical coefficient was independently checked there. This report uses that checked formula and the readable residual estimates; it does not silently change the original bytes. The separate root rendering erratum was not read or audited here, and the previous verdict remains unchanged.

## Per-result verdicts

All source locations below refer to the physical line numbers of the sealed Gaussian proof.

| Result | Location | Verdict | Audited scope |
|---|---|---|---|
| G-01: theorem hypotheses and normalization | lines 11–47; card | PASS | Fixed finite list; iid initial law; full backward kernels; uniform spatial bounds; separate deterministic covariance limits. |
| G-02: exact corrected remainder | lines 64–94, (2.2)–(2.4) | PASS | Initial pair endpoint, pair martingale, cubic and both lower contractions have the displayed signs and coefficients. |
| G-03: second-moment remainder and mean-field bias | lines 96–135, (2.5)–(2.9) | PASS | Genuine L2 inputs give the asserted rate; the unscaled mean bias is of order one over N. |
| G-04: actual-law leading bracket replacement | lines 137–185, (3.1)–(3.5) | PASS | Dependent particles are retained; absolute integrated discrepancy is controlled; unequal terminal times are correct. |
| G-05: complex exponential and conditional factorization | lines 187–230, (4.1)–(4.4) | PASS | Positive bracket sign, bounded modulus, true martingale, and conditioning on the initial sigma-field are justified. |
| G-06: triangular iid expansion and joint independence | lines 232–268, (5.1)–(5.4) | PASS | Uniform Taylor error, correct initial covariance factor, and factorization for independent Gaussian limits. |
| G-07: weak convergence, degeneracy and covariance comparison | lines 270–280 | PASS | Gaussian smoothing and uniform second moments justify the limit and removal of the remainder. |
| G-08: homogeneous free heat covariances | lines 282–324, (7.1)–(7.4) | PASS | Direct one-particle and initial-plus-bracket calculations agree for all terminal-time arrangements. |
| G-09: moving free heat covariance | lines 326–344, (7.5) | PASS | Both background means are subtracted; zero and orthogonal modes need no singular division. |
| G-10: oscillating-temperature obstruction | lines 346–348 | PASS | The two time-zero variances give distinct subsequential Gaussian limits. |
| G-11: full-response high-temperature endpoint | lines 350–398, (8.1)–(8.4) | PASS | The response term is retained; both deterministic covariances vanish; the observable converges to zero in L2. |
| G-12: low-temperature endpoint and scope boundary | lines 400–416; card | PASS | Dynamical noise vanishes; the initial covariance limit remains explicitly conditional. |

There are no newly identified defects requiring repair. These local identifiers organize this review and do not allocate canonical campaign identifiers.

## Exact remainder, norm strength, and centering

Write the one-body backward equation as `(partial_t + L)f = 0`, and the corrector equation as `(partial_t + L_2 + B/N)Phi = -J_f`, with terminal pair kernel zero. The reviewed identities give

\[
 d\rho(f)=P_N[J_f]dt+dM_f,
\]

\[
 dP_N[\Phi]=\left\{-P_N[J_f]+U_3[C\Phi]
 +\frac1N\rho((B\Phi)_\mu)
 +\frac1{2N}\mu^{\otimes2}(B\Phi)\right\}dt+dM_\Phi.
\]

Adding and integrating leaves the initial pair term on the right with a plus sign. Both martingales and both integrated lower terms also have plus signs. Symmetrization in `C` remains the six-permutation average inherited from the pair identity. No terminal endpoint survives; no diagonal trace or lower contraction is silently removed. This reproduces exactly the submitted (2.4).

The prior residual proof, Section 4, supplies actual-law L2 bounds, not only the L1 rows of its summary table. Its (4.2) and the subtracted empirical diagonal give `||P_N[Phi]||_2 <= C/N`. Its (4.3)–(4.5), including the empirical/background partial diagonal, give `||U_3[C Phi]||_2 <= C/N^(3/2)`. Minkowski gives the same rate for the time integral. The needed source norms are `K` in `C^(3d+4)` and `Phi` in `C^(3d+5)`, both available within the frozen hypothesis.

The exact pair bracket and the supremum-before-root-substitution estimate for its integrand give

\[
 \sigma_N^2\,\mathbb E[M_\Phi]_{t_a}
 \le \frac{C\sigma_N^2}{\beta_N N^2}
 =\frac{C c_N}{N}\le\frac C N.
\]

Finite-parameter smoothness and bounded spatial integrands give square integrable stochastic integrals even when the unscaled noise coefficient is large. Itô isometry yields an L2 pair-martingale contribution of order `N^(-1/2)` after scaling. The pathwise lower terms have unscaled size at most `C/N`; total variation of `rho` is at most two. Since `sigma_N <= sqrt(N)`, the four pieces of the scaled remainder are bounded in L2 by, respectively, `C/sqrt(N)`, `C/sqrt(N)`, `C/N`, and `C/sqrt(N)`. This proves G-03 without replacing an absolute moment by a signed mean.

At iid time zero, ordered distinct labels give

\[
 \mathbb E U_2[\Phi_0]
 =\left(\frac{N(N-1)}{N^2}-2+1\right)
   \mu_0^{\otimes2}(\Phi_0)
 =-\frac1N\mu_0^{\otimes2}(\Phi_0).
\]

The factor one half in `P_N` produces (2.8). The leading initial fluctuation and both martingales have zero expectation. The unscaled cubic and lower terms give the asserted order-one-over-N bias. The proof does not impose exact-first-marginal centering.

## Bracket replacement and independence

For a common time interval, use only the stopped stochastic integrands
`v_a(r,x) = 1_[0,t_a](r) grad f_a(r,x)`. Their deterministic endpoint values do not affect the stochastic integral. Each backward duality was already applied on its own interval. Thus no artificial PDE jump is introduced. The independent driving Brownian coordinates give exactly

\[
 Q_N^{ab}(t)=\frac{2\sigma_N^2}{\beta_N N^2}
 \sum_i\int_0^t v_a(r,X_i)\cdot v_b(r,X_i)dr
 =2c_N\int_0^t\eta_r^N(v_a\cdot v_b)dr.
\]

The modewise L6 estimate from the reviewed residual proof implies the same L1 estimate. Integration by parts in a largest-frequency coordinate gives absolute summability after multiplication by `1+|k|` for every scalar test in `C^(d+2)`. Consequently

\[
 \mathbb E|\rho_r^N(h_r)|\le C N^{-1/2}\|h_r\|_{C^{d+2}}.
\]

The gradient product uses at most `d+3` derivatives of each one-body kernel. Taking the absolute value inside the time integral establishes (3.3), including its supremum over the upper integration limit. It does not assert a supremum-in-time empirical moment. This is an estimate under the actual interacting law supplied by the synchronous coupling, not an iid replacement of the evolved particles.

For fixed real `theta`, let `M = theta.L_N` and `Q=[M]`. The deterministic bound `0 <= Q <= B_theta` follows directly from the bounded gradients, probability mass one, and `c_N <= 1`. With `E=exp(iM+Q/2)`, Itô's formula gives

\[
 dE=iE\,dM+\tfrac12E\,dQ+\tfrac12i^2E\,dQ=iE\,dM.
\]

The sign is positive. Moreover `|E| <= exp(B_theta/2)` and the expected integrated squared stochastic integrand is at most `exp(B_theta) B_theta`. Its real and imaginary parts are therefore true square integrable martingales. Relative to the usual SDE filtration, with initial particles independent of the driving Brownian motions, the conditional identity `E[E_T | F_0]=1` is valid.

Writing `q=theta^T D_N theta`, the exact identity for a bounded initial-measurable complex `Y` is

\[
 \mathbb E[Y e^{iM_T}]-e^{-q/2}\mathbb E Y
 =\mathbb E[Y E_T(e^{-Q_T/2}-e^{-q/2})].
\]

Both `Q_T` and `q` are nonnegative, so the Lipschitz constant of the real exponential here is one half. The bracket-replacement error gives (4.4). No independence between the finite-particle leading martingale and its initial state is assumed. In particular, zero cross covariance alone is not used as a substitute for independence.

## Triangular array and weak-limit passage

For fixed `alpha`, set `X_N = a_N alpha.xi_(N,1)`. These real variables are centered and bounded uniformly, with variance `alpha^T I_N alpha`. Taylor's integral remainder gives

\[
 \left|\mathbb E e^{iX_N/\sqrt N}
 -1+\frac{\alpha^T I_N\alpha}{2N}\right|
 \le\frac{\mathbb E|X_N|^3}{6N^{3/2}}.
\]

The covariance already includes `a_N^2`; none is lost. For sufficiently large `N`, both the exact one-particle characteristic function and its real quadratic approximation have modulus at most one. Factoring the difference of their Nth powers bounds it by `C_alpha N^(-1/2)`. For bounded nonnegative `v`, `(1-v/(2N))^N` differs from `exp(-v/2)` by `O(N^(-1))` uniformly; for example, the real identity `log(1-x)+x = -integral_0^x u/(1-u) du` supplies the bound when `x <= 1/2`. This needs no complex logarithm and no convergence of the individual backward kernels.

Putting `Y=exp(i alpha.S_N)` in the conditional factorization proves the joint characteristic-function approximation for arbitrary fixed `alpha,theta`. Convergent `I_N,D_N` are positive semidefinite limits, so matrix square roots construct the independent Gaussian vectors, including singular covariance matrices.

The second moments of `(S_N,L_N)` are uniformly bounded by `tr(I_N)+E tr(Q_N(T))`. After adding an independent Gaussian of covariance `epsilon` times the identity, each characteristic function is dominated by the integrable function `exp(-epsilon |zeta|^2/2)`. Fourier inversion can be justified directly by writing the density as the expectation of the translated Gaussian density and applying Fubini. Dominated convergence gives uniform convergence of these smoothed densities. Compact-set integration plus the uniform second-moment tail bound gives convergence of bounded-test expectations for each fixed `epsilon`.

For a bounded Lipschitz test, removal of the added Gaussian changes expectation by at most its Lipschitz constant times `sqrt(2m epsilon)`. Sending `N` to infinity first and then `epsilon` to zero proves joint bounded-Lipschitz convergence. This implies usual weak convergence: on a fixed ball a bounded continuous function can be uniformly approximated by bounded Lipschitz functions, and the uniformly small tails handle the complement. Degeneracy of the unsmoothed Gaussian causes no problem. The L2 remainder then transfers the conclusion to the terminal observable vector.

Finally, `E[L_N | F_0]=0` makes the finite-particle cross covariance of `S_N` and `L_N` exactly zero. The bracket error is of order `N^(-1/2)`, and Cauchy–Schwarz with the uniform second moment and the L2 remainder gives the same order for the difference between the covariance of the observable and `I_N+D_N`. The mean correction is no larger. The statements at line 280 therefore follow.

## Independent recomputation of the heat covariance tests

These are analytic exact checks; no floating-point simulation or finite-grid check is used as proof. Put `lambda_k=4 pi^2 |k|^2` and `b_N=min(beta_N,1)=beta_N c_N`. With zero interaction and confinement, the pair corrector is zero and the backward terminal mode is

\[
 f_{t,k}(r,x)=e^{-\lambda_k(t-r)/\beta_N}e_k(x).
\]

For Haar initial data and opposite nonzero modes, the initial covariance is
`b_N exp(-lambda_k(t+s)/beta_N)`. The gradient product is `lambda_k` times the two backward amplitudes. Integrating twice `c_N` times that product to `min(t,s)` gives

\[
 D_N=b_N\left(e^{-\lambda_k|t-s|/\beta_N}
               -e^{-\lambda_k(t+s)/\beta_N}\right).
\]

Thus (7.2)–(7.4) have the correct factors. Independently, condition a stationary Brownian particle at the earlier terminal time to get its mode covariance `exp(-lambda_k |t-s|/beta_N)`. Label independence multiplies this by `sigma_N^2/N=b_N`. Real cosine and sine variances each have the extra factor one half; their cross covariance vanishes under Haar measure. If either time is zero the overlap integral vanishes, if the times coincide the total is `b_N`, and other nonopposite modes have zero bilinear covariance. Constant tests have zero centered fluctuation and zero gradient.

For a general smooth probability density write `m_q=mu_0(e_q)`, let `t >= s`, and put

\[
 A=\lambda_k t+\lambda_\ell s,\qquad
 \delta=\lambda_k+\lambda_\ell-\lambda_{k+\ell}
       =-8\pi^2 k\cdot\ell.
\]

The initial covariance from the backward kernels is exactly

\[
 I_N=b_N e^{-A/\beta_N}(m_{k+\ell}-m_km_\ell).
\]

Heat flow gives `mu_r(e_(k+ell)) = exp(-lambda_(k+ell) r/beta_N) m_(k+ell)`, and the gradient product is `-4 pi^2 k.ell` times the combined backward mode. Consequently the integrand of the dynamical covariance, including its prefactor, is

\[
 c_N\delta\,e^{-A/\beta_N}e^{\delta r/\beta_N}m_{k+\ell}.
\]

Integrating to `s` yields

\[
 D_N=b_N m_{k+\ell}
 \left(e^{-[\lambda_k(t-s)+\lambda_{k+\ell}s]/\beta_N}
              -e^{-A/\beta_N}\right).
\]

When `delta=0`, the integrand is identically zero and the displayed difference is zero; this argument never requires division by a vanishing frequency difference. The sum is precisely (7.5). A second derivation conditions a single Brownian particle at time `s`: the mixed moment is the first exponential above times `m_(k+ell)`, and subtracting the product of its two means gives the second term in (7.5). Cross-label covariance is zero under this free iid law, leaving the factor `b_N`. Zero modes, orthogonal modes, `s=0`, and equal times are all included. Complex covariance here is bilinear as stated in the proof; real and imaginary parts recover the real theorem.

At time zero with one Haar cosine, the covariance is `b_N/2`. Alternating temperatures one half and two produce the respective variances one quarter and one half. The triangular iid argument yields different subsequential Gaussian limits, so uniform smoothness alone cannot remove the covariance-limit hypothesis. The other homogeneous free temperature limits follow directly from the exact exponentials and `0 <= I_N,D_N <= b_N` for an opposite-mode diagonal covariance.

## Full-response temperature endpoints

For a single terminal interval let `A f = u.grad f + nu Delta f` and retain the full response `Rf`. Since the deterministic reference satisfies the adjoint local equation and the backward test satisfies `partial_t f = -Af-Rf`,

\[
 \frac d{dt}\mu_t(f_t^2)
 =\mu_t(A(f_t^2))-2\mu_t(f_t Af_t)-2\mu_t(f_t Rf_t)
 =2\nu\mu_t(|\nabla f_t|^2)-2\mu_t(f_t Rf_t).
\]

This verifies the sign and the background derivative in (8.1). On the torus the smooth equations justify the differentiations and integration by parts for each finite positive temperature. No uniform time-derivative bound is needed. If `B=||K||_infinity` in the Euclidean vector norm, the componentwise spatial bound gives `||Rf||_infinity <= B sqrt(d) A`. Upon integration the initial square is subtracted and is nonnegative; the response integral is bounded in absolute value. Therefore

\[
 2\beta_N^{-1}\int_0^{t_a}\mu_r(|\nabla f_a|^2)dr
 \le A^2+2T B\sqrt d\,A^2.
\]

For temperatures tending to zero, `a_N^2=beta_N` and `c_N=1` eventually. The diagonal entries of both deterministic covariance matrices are `O(beta_N)`; their off-diagonal entries have the same bound by Cauchy–Schwarz, extending the integrands by zero in time for the dynamical matrix. Hence both covariance limits are zero. Independently, absolute Fourier summation of the reviewed uniform mode estimate for each fixed terminal test gives `||sigma_N rho_(t_a)(phi_a)||_2 <= C sqrt(beta_N)`. This proves the stronger L2 endpoint assertion in the theorem card, even when temperature decreases much faster than a power of N.

For temperatures tending to infinity, `c_N=1/beta_N` eventually and the spatial gradient bound gives `D_N=O(1/beta_N)`. The same deterministic integrand bound applies to the actual bracket, so the leading martingale converges to zero in L2 without first invoking bracket replacement. The initial covariance is then the covariance of the temperature-dependent backward tests at time zero. Its limit is not established in this dossier. Conditional on that covariance converging, the asserted initial Gaussian limit follows. No zero-diffusivity PDE convergence is inferred from the spatial bounds.

## Limits, commands, and output seal

This PASS is conditional on the exact frozen uniform spatial norms and on entrywise convergence of the two deterministic covariance matrices, except where the high-temperature endpoint explicitly proves their convergence to zero. It applies only to a fixed finite list of tests and terminal times, fixed smooth kernels, iid initial preparation and mean-field centering. It does not prove field or path tightness, a growing-test theorem, a new law-class bridge, cutoff-uniform constants, a singular comparison, effective-coupling power counting, critical corrector truncation, a logarithmic normalization, or the full M3 target. No later constructor-specific extension is implicitly reviewed. Root alone decides promotion and canonical ledger changes.

Verification performed in the assigned worktree:

- `shasum -a 256 -c AUDITS/ROUND_002_GAUSSIAN_INPUT_SHA256SUMS.txt`: all three candidate inputs OK, both at initial inspection and final seal.
- `shasum -a 256 -c AUDITS/ROUND_002_GAUSSIAN_ADDITIONAL_INPUT_SHA256SUMS.txt`: all six prerequisites OK.
- `shasum -a 256 -c AUDITS/HOSTILE/ROUND_002_RESIDUAL_REVIEW_SHA256SUMS.txt`: all four previously sealed outputs OK; no prior report was changed.
- `python3 scripts/verify_campaign.py`: `CAMPAIGN VERIFICATION PASSED`. This structural check is not mathematical evidence for the Gaussian limit.
- `git diff --check`: passed for tracked changes; the newly created review and additional manifest were separately checked for trailing whitespace and terminal newlines before sealing.
- Complete proof/card reads, line-numbered checks, and the analytic computations above supplied the mathematical verification. No new numerical code or external theorem was needed. One initial read used the nonexistent path `PROOF_OBLIGATIONS/PO-001_RESIDUAL.md`; it was immediately corrected to the existing `TASKS/ACTIVE/PO-001_RESIDUAL.md`, whose contents and hash were checked.

New outputs are this report, `AUDITS/ROUND_002_GAUSSIAN_ADDITIONAL_INPUT_SHA256SUMS.txt`, and the adjacent `ROUND_002_GAUSSIAN_REVIEW_SHA256SUMS.txt`. The adjacent seal records this report's final SHA-256 and the additional-input manifest hash; a self-hash is deliberately not embedded in the report bytes. No candidate, immutable historical input, canonical ledger, TeX artifact, or previously issued report was modified. No commit, push, dependency installation, remote operation, or worker spawn was performed.
