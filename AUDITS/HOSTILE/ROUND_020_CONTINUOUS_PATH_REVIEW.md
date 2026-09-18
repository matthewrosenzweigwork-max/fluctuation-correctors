# AUD060 — whole-claim hostile review of the continuous-path Gaussian assertion

TASK092. Issued 2026-09-18 UTC. Reviewer worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r020-continuous-path-hostile`; branch: `codex/hocf-r020-continuous-path-hostile`; prescribed and verified base: `e75f8b780682a7e9fb0715b5e8b5873be684a2e8`.

**Whole verdict: PASS, CONDITIONAL ON THE EXACT FULL-SOURCE PREMISES AND THEIR SEPARATE ROOT GATES. The entire frozen THM042 survives this hostile review, with no load-bearing mathematical repair, scope restriction, or additional hypothesis required.** No admitted counterexample, failed load-bearing line, or unmet mathematical source-interface premise was found. This is the hostile-review axis, with visible exposure to the complete constructor narrative. It is not a blind reconstruction, certification of every assertion in the historical source reports, canonical promotion, or campaign completion. Root alone compares the fresh axes and matches the previous source gates.

There is one nonblocking typographical finding, AUD060-N01, at candidate line 189: the relation in (3.3) is printed as literal `le`. Its intended less-than-or-equal relation is stated in the surrounding prose and is the exact inequality of the full R16 source. No source was repaired. A future superseding version may replace that token by `\le`; the sealed source bytes and historical statuses remain unchanged.

## 1. Frozen conjunction and exact negation

All quantifiers and conventions of THM042 are retained. Fix an integer (d\ge3), (0<s\le d-2) and (s<d/2), finite (T\ge0), a finite positive integer (m), and fixed real (h_1,\ldots,h_m\in C^\infty(\mathbb T^d)). The torus has Haar mass one and characters (e^{2\pi i k\cdot x}). Its zero-mean, coefficient-one kernel is

\[
 \widehat g(k)=c_{d,s}|k|^{s-d},\quad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad k\ne0,
 \qquad K=-\nabla g.
\]

There is zero external drift. For each (N\ge2), the actual global singular gradient paths have interaction coefficient (1/N), independent standard Brownian drivers with amplitude (\sqrt{2\nu_N}), and iid Haar initial positions independent of those drivers. Assume (0\le\nu_N\le\nu_*<\infty) and (\nu_N\to\bar\nu\ge0), without a rate. Set (b(0)=1), (b(\nu)=\min(1/\nu,1)) at positive noise, (b_N=b(\nu_N)), and (\sigma_N=\sqrt{Nb_N}). The complete conjunction is:

1. The actual observables (Z_{N,j}(t)=\sigma_N(\eta_N(t)[h_j]-\int h_j)) are measurable continuous paths and have exact one-body Haar centering.
2. The limiting centered, possibly degenerate Gaussian process exists with continuous paths. With (a_k=4\pi^2|k|^2), (D_k=4\pi^2c_{d,s}|k|^{s+2-d}), (L_k=D_k+\bar\nu a_k), and (\bar b=b(\bar\nu)), its covariance at arbitrary (t,u\in[0,T]) is exactly

\[
 \mathbb E Z_i(t)Z_j(u)=\bar b\sum_{k\ne0}\widehat h_i(k)\overline{\widehat h_j(k)}
 \left[\frac{D_k}{L_k}e^{-(t+u)L_k}
 +\frac{\bar\nu a_k}{L_k}e^{-|t-u|L_k}\right].
\]

3. The entire actual sequence is tight and converges weakly to that process in (C([0,T],\mathbb R^m)) with its uniform norm. Genuine singular identities, the original deleted-label source and both Haar contractions, and the independent-noise Itô correction and cross brackets must justify the passage. A fixed-terminal source estimate or covariance calculation alone does not suffice.
4. The same conjunction includes zero noise, zero or positive finite (T), constants, repeated evaluations, linear dependence, and singular covariance matrices.

The exact negation is the existence of one admitted fixed datum and bounded convergent noise sequence violating exact centering, existence or continuity of the specified Gaussian limit, tightness of the actual path laws, or weak convergence to that process in the stated uniform topology. Failure of a particular attempted bound is not that negation. The review also checks the genuine integrability required for the identities; it finds no such failure.

Unbounded noise, uniform particle heat-approximation rates in (N), distribution-valued fields, growing test lists, larger exponents, logarithmic kernels, inhomogeneity, other preparations, and the higher hierarchy remain excluded. The old energy-floor condition, full microscopic subcriticality, and finite positive microscopic criticality are not identified with one another.

## 2. Source and exposure preflight

The assignment and its input manifest were the first files opened. The branch/worktree was created from the exact prescribed base. All sixteen root input byte strings were checked against the supplied manifest, copied into the isolated worktree, and checked again before reading. The complete allowed source reports and complete candidate narrative were read. Two tool displays elided text: the omitted R20 Sections 4–7 and R18 Sections 4–5 spans were recovered directly from those same allowed files. No missing displayed span was treated as read.

The input copies, original routing manifest, hashes, and detailed exposure record are in the packet. The candidate's descriptions of its own diagnostic and the historical reports' embedded diagnostic summaries were visible narrative exposure only. No constructor program, saved result, separate previous audit, blind reconstruction, state/history/memory file, root scratch, unprovided reference, or external source was opened. No candidate diagnostic result is used as independent evidence here.

| Full permitted input | Checked load-bearing interface and retained boundary |
|---|---|
| `AGENTS.md`; `ROUND_001_MODEL.md`; TASK092 | Exact normalization, denominator, interaction, noise, assertion, and isolation. The narrow task supersedes broad orientation, state, and orchestration instructions. |
| R1 algebra, complete; especially Sections 1–2 and 5 | Smooth source half, response sign, deleted labels, one-body Itô correction and bracket. Its smooth diagonal assignment and higher hierarchy are not a singular premise. |
| R4 singular response, complete; especially Sections 2–5 | Heat normalization, coefficient one, integrable force, the full finite divergence measure, Coulomb atom and compensation. The necessary proof is present; historical references to unseen R3 work are not independent inputs. |
| THM026 and R6 particle realization, complete; especially Sections 3–8 | Finite-(N) measurable global noncollision, pathwise uniqueness, positive pathwise minimum separation, and same-noise heat passage at fixed data. R6's R5 analogy is not needed as an unseen theorem: the finite-(N) construction is supplied in full. |
| THM031 and R10 actual-law report, complete; used Sections 2–3 | Actual expected-energy sign, pair-energy integrability, positive heat truncation, and empirical Fourier bound. The full singular pair-gradient tail, inverse/domain modules, and R9 assumptions in other sections are nondependencies. Zero noise is proved directly in the full text. |
| THM038 and R16 source extension, complete; used Sections 2–7 | Exact positive splitting and self/background coefficients, scale-independent commutator seminorm, and positive absolute remainder domination. These deterministic statements, not the fixed-test card alone, supply simultaneous terminal-time control. |
| THM040 and R18 bounded-noise report, complete; used Sections 2–8 | Smooth one-body bracket concentration, triangular initial tests, conditional exponential, joint weak passage, and covariance. R18's comparison with unseen R17 is not a premise of the reproduced argument. R18 does not supply path tightness. |
| THM042, full unchanged card | Entire conjunction, exact negation, edges, topology, and exclusions. |
| R20 continuous-path memorandum, complete | The full candidate under attack, including its candidate-level provenance and self-check descriptions. |
| R20 `SOURCE_EXPOSURE.md`, complete | Constructor exposure narrative only. Its assertions about its own workflow are not substituted for this lane's own source checks. |

The OPEN / UNAUDITED, PROVED_CANDIDATE / SELF_CHECKED, conditional and historical status wording in those exact files is preserved. There is no independent source-gate status evidence in this isolated dossier. No unmet mathematical interface premise was found in the portions used for THM042; establishing that the corresponding prior independent gates passed remains the root's separate provenance obligation.

## 3. Analytic hostile review of every load-bearing claim

### AUD060-C01 — normalization, endpoint, and semigroup: PASS

Candidate Sections 1–2 and (3.1) agree with R4 Sections 2–3. For \(\alpha=(d-s)/2\ge1\) and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\), the nonzero heat integral coefficient is \(A\Gamma(\alpha)(4\pi^2|k|^2)^{-\alpha}\), equal to the frozen coefficient. The Euclidean substitution gives exactly local coefficient one. The derivative of the remaining lattice/large-time contribution is integrable at every fixed spatial order. In particular (g=|z|^{-s}+H), (H) smooth locally, (g_*:=\inf g> -\infty), and (K\in L^1) because (s+1<d).

The punctured flux vanishes below Coulomb and equals (c_d\delta_0) at Coulomb, where (c_d=4\pi^2c_{d,d-2}). Including the zero mode yields exactly (D=\operatorname{div}K=s(d-2-s)g_{s+2}\,dx) below Coulomb and (c_d(\delta_0-dx)) at Coulomb. Its lower bound by (-\kappa dx) is sufficient for energy construction; it is not an assertion that (D\ge0). Dropping either part of the Coulomb measure would alter the response, including its action on constants.

The test generator is (A_\nu=\nu\Delta-D*\), with nonzero multiplier (-(D_k+\nu a_k)). The exponent (s+2-d\le0) implies (D_k\le C) for nonzero lattice modes. Therefore (Q_a^\nu) contracts every Fourier absolute seminorm, and one time derivative costs at most two spatial powers uniformly for (0\le\nu\le\nu_*), also at (a=0). A spectral gap is not assumed: when (\bar\nu=0) below Coulomb, (D_k\to0) at high frequency. Nothing later divides by a uniform lower bound for these rates.

### AUD060-C02 — actual singular paths and heat passage: PASS under the exact finite-particle source

Candidate Section 2 uses the complete R6 mechanism. With (H_N=N^{-1}\sum_{i<j}g(x_i-x_j)), the shift (H_N-(N-1)g_*/2) is a sum of nonnegative pair terms. Any colliding pair makes its own term infinite, even at simultaneous collisions. Thus its sublevels are compact inside the collision-free configuration space. The identities (B=-\nabla H_N) and (\Delta_{Nd}H_N=(2/N)\sum_{i<j}\Delta g\le(N-1)\kappa) retain both differentiated coordinates of every unordered pair.

On a sublevel the stopped Itô martingale is true because its integrand is bounded. The resulting exit bound tends to zero as the energy level increases. Cutoff Picard solutions patch measurably and uniquely; a bounded-energy path extends. This proves noncollision from each fixed collision-free start, and joint measurability permits integration over iid Haar starts. It does not require a common exceptional set for uncountably many starts.

The realized finite-horizon path has positive minimum pair distance by continuity and compactness of the time interval. Local (C^1) heat convergence away from zero and cancellation of the same additive Brownian paths yield the fixed-(N) heat passage by a stopped Gronwall comparison. No estimate uniform in (N), initial separation, or noise is extracted from that comparison. The punctured classical Laplacian is used on these stopped paths only; it does not replace the full Coulomb measure in a response convolution.

### AUD060-C03 — actual energy, integrability, and centering: PASS

The actual expectation sign is not inferred from formal singular Fisher information. At a fixed smooth heat cutoff and positive noise, the classical compact-space density is positive with finite upper/lower bounds. Its free-energy derivative is exactly minus the integral of (F|\nabla H+\nu\nabla\log F|^2). Initial entropy and energy are zero. Nonnegative entropy gives (\mathbb EH_N^\varepsilon\le0); the fixed-(N) common lower bound ((N-1)g_*/2) and almost-sure energy convergence allow Fatou. At zero noise, actual deterministic energy decrease supplies the same result without division by noise.

This proves (\mathbb EH_N\le0), genuine energy integrability, and, by exchangeability, (\mathbb E|g(X_1-X_2)|\le2|g_*|). The local expansion then bounds the inverse (s)-th-power pair-distance moment uniformly in (N,\nu,t). This is precisely the integrability needed for the symmetrized source. It does not assert a pair-force-square bound.

Actual pathwise uniqueness gives common-translation equivariance. The initial law is invariant, so each one-body marginal is Haar; nonzero Fourier coefficients vanish under a suitable common translation. This proves exact centering for all bounded measurable one-body tests at every deterministic time. It does not assert independent particles at positive time. All source/background expectations are consequently used in their proper law class.

### AUD060-C04 — simultaneous source domination: PASS; decisive path-space issue checked

Candidate (3.2)–(3.8), lines 166–244, correctly use the deterministic content of R16 Sections 4–7. Write (w_\ell(v)=(1-e^{-v/\ell})^M), (M=d+2), and (\psi_\ell=1-w_\ell). The retained (g_\ell) has positive Fourier weights, enough decay for two absolutely summable derivatives, and (g_\ell(0)\le C\ell^{-s/2}). The discarded kernel (Q_\ell^{\rm rem}\ge0) has mass (c_\ell=C\ell^\alpha). The exact deleted-pair identity is

\[
 \frac{H_N}{N}=E_\ell+S_\ell-\frac{g_\ell(0)}{2N}
                          -\frac{N-1}{2N}c_\ell.
\]

Thus actual expected energy controls each nonnegative term, with upper bound (C(N^{-1}\ell^{-s/2}+\ell^\alpha)). This is also valid at (2\ell\le2), as the full source explicitly requires. Neither energy self term nor finite-(N) background term is omitted.

The retained radial weights have logarithmic slope at most (2(\alpha+M)); the integration-by-parts endpoints vanish and (0\le v w_\ell'(v)\le M w_\ell(v)) gives the bound. For nonzero lattice frequencies, comparison of the two radii and the triangle inequality gives candidate (3.5). The symmetrized Fourier commutator then costs exactly the seminorm order (R=\alpha+M+3): one test gradient and one factor of frequency difference supply the two extra powers. Applying the square-summable shifted product inequality bounds its absolute value by (C\|f\|_{\mathcal A_R}E_\ell). Fourier manipulations have absolute majorants at every fixed splitting scale.

For the discarded part, the shortest torus distance is no larger than each Gaussian translate's Euclidean distance. Differentiation therefore proves (\operatorname{dist}(z,0)|\nabla p_v(z)|\le C p_{2v}(z)). The gradient-test mean-value estimate and the substitution (a=2v) produce (Q_{2\ell}^{\rm rem}) as an absolute majorant. All three original contractions are dominated, with coefficients (S_{2\ell},c_{2\ell},c_{2\ell}/2). The resulting inequality

\[
 |P_N[J^f](x)|\le C\|f\|_{\mathcal A_R}
              (E_\ell(x)+S_{2\ell}(x)+c_{2\ell})
\]

holds at each collision-free configuration simultaneously for every smooth real (f). It is a genuine common random majorant. It was not obtained by interchanging a supremum and separate expectation bounds. Only the retained smooth source uses a zero diagonal; the singular source and discarded kernel never receive a diagonal value. Positivity used here is proved Fourier positivity and pointwise domination, not positivity of an arbitrarily weighted interaction.

### AUD060-C05 — expected path-supremum error: PASS

For all (a\in[0,T]), the seminorm of (Q_a^{\nu_N}h) is bounded by that of the fixed (h). The preceding common majorant therefore controls the entire family at each actual time (r). On each collision-free configuration, the source is continuous in (a); a countable dense set gives its measurable supremum. At \(\ell=N^{-2/d}\), the two error powers both equal (N^{s/d-1}). Tonelli applies after taking the terminal-time supremum:

\[
 \mathbb E\sup_{t\le T}\left|\sigma_N\int_0^t
 P_N[J^{Q_{t-r}^{\nu_N}h}](X_r)\,dr\right|
 \le C_hT\sqrt{b_N}\,N^{s/d-1/2}\longrightarrow0.
\]

This establishes the required (L^1) uniform-path smallness. Finite-(N) continuity of the error follows from the path's positive minimum separation and continuous test/Haar-contraction dependence. The argument uses a first absolute moment, not a missing fourth moment of a singular source. The particle heat limit is already complete at fixed (N) before a deterministic splitting scale is selected, so no joint-limit exchange is hidden here.

### AUD060-C06 — singular first-order identity and brackets: PASS

Candidate (4.1)–(4.5), lines 272–322, retain the original row (j_f=-K*\nabla f=Rf) and zero double Haar integral. At Coulomb (Rf=-c_d(f-\int f)). Direct ordered-label symmetrization gives the interaction (P_N[J^f]+\eta_N[Rf]), with its source half. The independent-noise Itô correction is (\nu_N\eta_N[\Delta f]). The backward equation cancels the one-body terms.

The symmetrized drift is integrable by C03, including probability times time. Collision stops eventually exceed the horizon almost surely; their drift integrals pass by dominated convergence, stochastic integrals by bounded-gradient isometry, and endpoint/time-derivative terms by bounded convergence. Thus the actual identity (Z_N=I_N+M_N+E_N) is genuine. Its one-body cross bracket is

\[
 2\nu_Nb_N\int_0^{a\wedge t_i\wedge t_j}
 \eta_N(r)[\nabla Q_{t_i-r}^{\nu_N}h_i\cdot\nabla Q_{t_j-r}^{\nu_N}h_j],dr.
\]

The Brownian-label sum cancels the scaled (1/N). There is no (N-1) deleted-pair factor in this bracket and no cross-particle noise trace. The source denominator remains (N^2). This proof applies Itô to smooth one-body observables on actual singular paths; it does not require the unresolved Itô domain of a singular pair inverse.

### AUD060-C07 — continuous stochastic-convolution version: PASS

Candidate line 310 defines (M_N=Z_N-I_N-E_N), all three terms already known continuous. For each deterministic terminal time this equals the stochastic convolution almost surely by C06, so it is a continuous version. This is not circular use of the desired tightness. Each fixed pair of terminal-time moment identities transfers to the version, and countably many dyadic evaluations may be put on one full-probability event. Rational-time measurability and continuity give a random variable in the uniform path space. No unproved stochastic Fubini step is necessary, and the moving-terminal convolution is never declared a terminal-time martingale.

### AUD060-C08 — uniform fourth moments: PASS

For the initial term, only iid preparation at time zero is used. The exact fourth moment of a centered normalized sum is

\[
 b_N^2\left[N^{-1}\int v^4+3(N-1)N^{-1}(\int v^2)^2\right].
\]

With (v=(Q_t^{\nu_N}-Q_u^{\nu_N})h), its norm is (O(|t-u|)) uniformly in the admitted noise, so its fourth moment is (O(|t-u|^4)). At time zero the fourth moments are uniformly bounded.

For a martingale with deterministic bracket-density majorant (w(r)dr), stopped Itô applied to the fourth power gives (6\mathbb E\int U_r^2d\langle U\rangle_r\). Stopped isometry bounds its expectation by (6\int w(r)\int_0^r w(v)dv,dr=3(\int w)^2); Fatou removes the stop. This is a valid bound for adapted integrands, not an equality with three times the squared mean bracket.

For (t\ge u), the convolution difference includes the changed test on the entire old interval ([0,u]) and the new integral on ((u,t]). Their gradient bounds are respectively (C(t-u)) and (C). Since (\nu_Nb_N\le1), the deterministic bracket-density majorant integrates to (C(T(t-u)^2+(t-u))\le C_T(t-u)). The fourth moment is therefore (O(|t-u|^2)). No independence of the old and new terms, or of the initial vector, is assumed. Summing over fixed (m) yields candidate (5.6) for (Y_N=I_N+M_N). This argument does not assign a fourth-moment bound to (E_N).

### AUD060-C09 — compactness of the linear part and actual laws: PASS

Candidate Section 6 uses the correct moment exponent. There are (2^n) adjacent dyadic increments, each with fourth moment (C2^{-2n}). At threshold (A2^{-\gamma n}), their union probability is (CA^{-4}2^{-(1-4\gamma)n}), summable for (0<\gamma<1/4). Together with the initial fourth moment, all dyadic increment bounds hold outside an event of uniformly small probability. The endpoint approximation chains and continuity give a common Hölder modulus.

The resulting closed, bounded, equicontinuous path set is totally bounded by finite-grid quantization and compact by completeness. This directly proves uniform tightness of (Y_N).

A fixed-radius neighborhood of a compact set would not suffice for (Z_N), and the candidate correctly avoids it. For each tolerance (e_j\downarrow0) and summable probability budget (p_j), C05 chooses (N_j) so the error norm is small for (N\ge N_j). The uniform Hölder control then chooses a modulus scale for those indices. For the finitely many smaller indices, their actual continuity makes the modulus probabilities tend to zero, allowing further reduction of that scale. A union bound over (j) gives one closed bounded equicontinuous set of actual paths with arbitrarily high probability, uniformly in (N). The compact set may depend on the fixed admitted sequence, as the theorem permits; all quantitative source and linear moment constants are uniform over the bounded noise interval. No stronger uniform particle-approximation claim is inferred.

### AUD060-C10 — continuous Gaussian existence and exact covariance: PASS

Candidate Section 7 constructs the limit explicitly using a real orthonormal mean-zero trigonometric basis, independent normals, and independent Brownian motions. A mode is

\[
 G_l(t)=\sqrt{\bar b}\left(e^{-L_lt}\xi_l+
 \sqrt{2\bar\nu a_l}\int_0^t e^{-L_l(t-r)}dB_l(r)\right).
\]

Integration by parts bounds the convolution supremum by (2\sup|B_l|); the elementary Brownian maximal estimate bounds its expected supremum. Hence (\mathbb E\sup|G_l|\le C_T(1+\sqrt{a_l})), uniformly even when (L_l\to0). The smooth test coefficients are absolutely summable against this weight. Tonelli therefore proves absolute uniform convergence almost surely and expected uniform convergence of the tails. The process is a genuine measurable continuous vector process.

At every finite tuple the series converges in (L^2); independent Gaussian partial sums identify the centered Gaussian limit, allowing degeneracy. Direct isometry gives initial covariance (\bar b e^{-(t+u)L_l}) plus thermal covariance (2\bar\nu\bar b a_l\int_0^{t\wedge u}e^{-(t+u-2r)L_l}dr). Integrating gives the frozen coefficient (D_l/L_l) on the time sum and (\bar\nu a_l/L_l) on the time difference. Combining the sine and cosine pair reproduces the complex Fourier sum with no extra factor two. The same smooth bounds give fourth-moment increments for the limit, so its law has compact modulus sets as well. No covariance-only existence assertion is being used.

### AUD060-C11 — actual bracket concentration and slow-noise replacement: PASS

Candidate Section 8 uses only R10 Sections 2–3. The positive heat-integral truncation includes the smooth energy self subtraction. With scale (N^{-2/d}) and the actual energy sign it gives (\mathbb E|\widehat\eta_N(r,k)|^2\le\min(1,CN^{-q}|k|^{d-s})), (q=1-s/d). For low frequencies the integration interval ([|k|^{-2},2|k|^{-2}]) lies above that scale; for higher frequencies the trivial bound completes the assertion. This is an actual-law bound, not positive-time iid independence.

Absolute Fourier convergence and Cauchy–Schwarz in probability then give (\mathbb E|\rho_N[\psi]|\le CN^{-q/2}\|\psi\|_{\mathcal A_\alpha}). The absolute Fourier seminorm is an algebra, and all products of the deterministic backward gradients have a uniformly bounded such seminorm. Tonelli therefore yields (L^1) bracket concentration for every finite tuple, including all cross terms.

The multiplier mean-value estimate costs (C|\nu_N-\bar\nu|\) in every fixed smooth seminorm, uniformly on the finite time interval. The functions (\nu b(\nu)=\min(\nu,1)) and (\sqrt{b(\nu)}) are Lipschitz, including across one. Initial test differences are exactly centered, so the iid variance of their normalized sum is their (L^2) norm squared. No factor (\sqrt N\) multiplies the noise error. Arbitrarily slow convergence and terms with exactly zero noise are admitted as stated.

### AUD060-C12 — initial/thermal dependence and joint finite-dimensional passage: PASS

For every fixed coefficient vector, the scalar integration-time martingale has a deterministic bracket upper bound. The compensated complex exponential with **positive** compensator (\exp(iU+\langle U\rangle/2)) is a true square-integrable martingale: Itô cancels its drift, and both its modulus and integral square norm are bounded. Conditional expectation given the entire initial sigma field equals one. Multiplication by a bounded initial-measurable characteristic factor and replacement of the random bracket by its deterministic limit are justified by C11's (L^1) error and the bounded exponential derivative.

This proves the required asymptotic factorization without finite-(N) independence. The bounded iid initial summand expansion gives the Gaussian initial characteristic function; the source error disappears by C05. All scalar projections, with their full cross brackets, identify the joint covariance rather than just separate coordinate limits.

The characteristic-function-to-weak-limit step is complete. The linear vector has uniformly bounded second moments. Convolution with an independent Gaussian supplies an integrable Fourier multiplier, uniform convergence of the resulting densities, and uniform tails. Bounded Lipschitz convergence follows by removing that convolution; compact-ball approximation extends it to bounded continuous tests. The (L^1) source error transfers the assertion and tail bounds to the actual vector. The method includes zero or singular covariance and does not require a density for the limiting un-convolved Gaussian.

### AUD060-C13 — uniform-topology weak identification: PASS

Candidate Section 9 makes the necessary path-space step explicitly. Piecewise-linear interpolation (P_n) on a dyadic grid is a continuous function of finitely many evaluations and has uniform error at most the path modulus at the grid scale. The compact sets from C09 make those modulus tails uniformly small for the actual sequence; C10 does the same for the limit. At fixed grid level, C12 proves convergence of the entire evaluation tuple, including repeated tests.

For each bounded Lipschitz functional on the uniform path space, interpolation errors are controlled in expectation by a tolerance plus a uniformly small modulus-tail probability. Taking the particle limit at fixed grid and then refining the grid proves convergence for all such functionals. Actual and target tightness provide a common compact set. Infimum Lipschitz extensions, clipped to the bounded range, approximate each bounded continuous functional uniformly on that set. Its complement has arbitrarily small probability. This proves the asserted weak convergence for all bounded continuous uniform-path functionals. Finite-dimensional convergence has not been mistaken for tightness, and no unstated subsequence theorem is needed.

### AUD060-C14 — edges and exclusions: PASS

At (T=0), the assertion is the finite-dimensional iid limit and dyadic time rescaling is not used. If (\nu_*=0), the actual dynamics are deterministic gradient flows, (b_N=1), and all stochastic terms vanish; the random limit comes from the initial field alone. If only (\bar\nu=0), the same bounds allow arbitrarily slow cooling and zero entries, while the limiting thermal contribution vanishes directly. For positive limit noise it remains present.

Constants give identically zero fluctuations, source, gradient, and limit. Linear dependence and repeated tests require no covariance inverse; any constant linear combination vanishes as an entire path. The conjunction (s\le d-2) and (s<d/2) includes three-dimensional Coulomb and excludes four-dimensional Coulomb. At the excluded equality the source bound has exponent zero, so no decay is inferred. The proof does not expand the test family with (N), treat a logarithmic limit, change centering or preparation, transfer Haar estimates to arbitrary laws, or infer a higher-order hierarchy.

## 4. Independent falsification and diagnostic evidence

The hostile route attacked the actual source supremum, not just its covariance, and reconstructed the compactness and joint probability implications. In addition, the fresh program `hostile_exact_diagnostic.py` was written without reading an old program or saved result. It uses only Python's standard library and exact rational arithmetic. It is read-only except that the invoking shell initially saved its stdout as the result artifact; there is no randomness, tolerance, package installation, or external source.

Its main independent temporal test is the continuum convolution (M(t)=\int_0^t[1-\lambda(t-r)]dB_r=B_t-\lambda\int_0^tB_rdr). These two constructions give exact rational polynomial covariances. The test compares them, recomputes old/recent increment contributions, and checks variances of arbitrary three-time linear combinations and the continuous path integral. At \(\lambda=1,t=1,u=1/2\), the increment variance is (5/12); erasing old noise gives (7/24). At unit horizon the variance of the integrated path is (2/15); erasing its memory gives (1/3). These are exact temporal witnesses, not a replacement dynamics or admitted particle counterexample.

Other controls recompute the literal ordered source and cross-bracket scaling in a smooth Fourier probe; reconstruct the self/background identity from direct unordered pairs and a full Gram sum; evaluate retained positive Laplace moments both by an alternating finite sum and an independently positive product derivative; check dyadic probability summability and interpolation error; and exhibit separated continuous tent paths inside a fixed neighborhood of the compact singleton zero. The latter family has disjoint dyadic supports and pairwise uniform distance one half for arbitrarily many indices, so such a neighborhood need not be totally bounded. The candidate does not use that invalid compactness shortcut.

A separate conditional Brownian-integral example has initial-measurable bracket taking values (3/2) and (13/2). Its initial/thermal covariance is zero, but its initial-weighted squared martingale moment is nonzero. Exact Gaussian moments and formal characteristic series reject both replacing the bracket by its mean and using a negative exponential compensator. This tests the probability inference; it does not assert finite-(N) independence or Gaussianity for actual particle martingales.

**Executed diagnostic: PASS, 3,316 exact assertions in 48 categories; all 18 nonvacuous mutations rejected with explicit witnesses.** The JSON records every category, mutation witness, evidence limitation, and the program digest. No diagnostic success supplies an analytic compactness theorem or an actual singular-law estimate; the per-claim review above is the analytic evidence.

## 5. Dispositions, verification, and bounded handoff

| Item | Disposition |
|---|---|
| Entire unchanged THM042 conjunction and exact negation | PASS on this whole-claim hostile axis, conditional on the exact source premises and root's separate source-gate matching. No admitted counterexample or failed load-bearing line found. |
| Simultaneous terminal-time source, actual tightness, continuous Gaussian existence, and uniform-topology weak passage | All explicitly checked; no narrowing to finite-dimensional convergence. |
| Initial/thermal dependence, every source/background/Itô coefficient, and zero-noise/degenerate cases | Retained and checked. |
| AUD060-N01 | Nonblocking literal `le` typo in candidate (3.3), line 189; no silent edit. |
| Earlier cards and full-source histories | Unchanged byte-for-byte; not independently promoted by this review. |
| Blind reconstruction, source gate provenance, canonical ledgers and theorem promotion | Root-only actions outside this lane. No blind narrative or results read. |

Only this review and its unique artifact directory were created beyond the task-authorized exact input overlay. The packet contains this complete review, all sixteen input byte strings, the original routing manifest, a detailed exposure record, exact diagnostic/program results, and a read-only verifier. The payload manifest covers every payload file other than its own hash listing. The archive is verified without extraction for exact member inventory, safe canonical relative names, regular-file type, absence of duplicate/link/special members, exact sizes and hashes, and agreement with on-disk bytes. External seals cover the archive, payload manifest, sibling review, verification evidence, and all other final outputs; the final manifest's digest is supplied in the handoff as its external anchor.

Reproduction from the worktree:

```text
python3 AUDITS/HOSTILE/ROUND_020_CONTINUOUS_PATH_HOSTILE_ARTIFACTS/packet/hostile_exact_diagnostic.py
python3 AUDITS/HOSTILE/ROUND_020_CONTINUOUS_PATH_HOSTILE_ARTIFACTS/packet/verify_packet.py --rerun-diagnostic --self-test-rejections
```

Both are read-only and write their reports only to stdout. The verifier checks exact bytes without archive extraction and includes in-memory adversarial archive/byte controls. Executed outcomes and complete seals are recorded in the artifact README and verification result. Every reported output exists and is part of the sealed inventory. Issued files are made read-only; any correction requires a new superseding artifact.

No canonical state, cumulative memorandum, immutable input content, prior audit, other worktree output, or remote was edited. No external browse, source beyond the manifest, memory lookup, child agent, dependency installation, commit, push, publication, or author contact occurred. The unavoidable ambient high-level memory summary was not used as mathematical evidence. No TeX source was edited and the final handoff contains no mathematical LaTeX, so no TeX build is implicated.

The exact next action is root comparison of this sealed AUD060 packet with the separately reconstructed whole assertion, followed by matching the unchanged source bytes and source-gate provenance. This is the authorized sealed bounded handoff, not a request for source repair and not campaign completion.
