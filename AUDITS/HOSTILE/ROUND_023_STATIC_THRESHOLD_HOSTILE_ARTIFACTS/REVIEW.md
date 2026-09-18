# AUD066 — entire THM045 hostile review

Issued 2026-09-18 UTC. TASK101. Fresh isolated hostile reviewer, dispatched as Astra Max. Base `64ac0538dff37a37d0883661b401ad04c311a5e5`; branch `codex/hocf-r023-static-threshold-hostile`; worktree `/Users/matthewrosenzweig/.codex/worktrees/hocf-r023-static-threshold-hostile`.

## 1. Verdict and exact scope

**Whole frozen THM045: VERIFIED by hostile reconstruction of the existing construction. Its exact negation is ruled out by the constructed family. No theorem hypothesis, law class, support condition, or limiting constant has been weakened.**

**Frozen proof text: NOT CLEAN. One non-load-bearing sentence is false and requires an explicit separately issued correction before an unqualified clean proof-text disposition.** In `MEMORANDA/ROUND_023_STATIC_THRESHOLD_INPUT_OBSTRUCTION.md:153`, the assertion that *all* of (6.1) is invariant under common translations, and holds on the final translated support, is false. Only its separation and energy bounds are invariant. The cosine/sine coordinates rotate. The existing proof already contains everything needed for the actual final support requirements and the moment limit without that false ancillary assertion. Finding AUD066-F01 below gives an exact counterexample and the dependency analysis. No candidate file has been changed or silently reinterpreted.

This is a theorem verdict plus a distinct proof-text defect, not a claim that failure of one sentence disproves THM045. Conversely, the defect is not hidden by reporting an unqualified proof pass. Root decides the formal gate disposition and must preserve this frozen issue when issuing any correction.

The theorem verified here is exactly the following conjunction. For the unit four-torus, coefficient-one periodic Coulomb kernel, and fixed test `h(x)=cos(4*pi*x_1)`, there are fixed `a,c>0` and `m0` so that every integer `m>=m0`, with `N=m^4`, has a bounded smooth probability density on the full labelled configuration torus. Its law is exchangeable and invariant under common translations, all one-body marginals are exactly Haar, and every configuration in its support has separation at least `c/m` and energy at most `-c*m^2`. With the literal deleted-pair statistic and original Haar contractions,

    lim sqrt(N) E |P_N[J_h]| = 16*pi^3*a^2 > 0.

The exact negation is nonexistence of any such fixed constants and family satisfying the entire conjunction. A failure of a particular route would not establish that negation. No actual iid-prepared process, evolving law, entropy inequality, fixed-time dynamic obstruction, time-integrated source obstruction, temperature sequence, fluctuation limit, or higher-corrector failure follows from this audit. In particular the actual iid-flow endpoint remains outside this gate.

## 2. Isolation, sources, and evidence categories

The first filesystem reads were precisely TASK101 and its eleven-entry input checksum manifest. The prescribed new worktree was then created from the exact published base. Each of the eleven root input byte strings was checked against its prescribed SHA-256 before overlay, and the overlay was checked again. No other repository mathematical file was opened. Every one of the eleven permitted documents was read in full, including the entire R4, R10, and R16 memoranda and the entire R23 root proof. Their embedded diagnostic summaries are exposed narrative, not verified computational evidence.

The following source roles were retained:

| Exact input | Role in this review |
|---|---|
| `AGENTS.md` | Research discipline. TASK101's explicit isolation overrides broad state/specification reading. |
| `MODEL_ORCHESTRATION.md` | Hostile-review role and separation of duties; no new worker was spawned. |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | Unit-Haar torus, Fourier characters, coefficient-one kernel, force sign, ordered deleted labels, denominator and centering. |
| `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md` | Read all 541 lines. Load-bearing use is its self-contained heat construction and compensated divergence in Sections 2–3, lines 69–196. These are reconstructed below. No propagation result is needed. |
| `MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md` | Read all 562 lines. Lines 76–235 distinguish the actual-law free-energy step from the deterministic floor/Fourier consequences. No particle-realization premise or dynamic estimate is transferred to the constructed static law. |
| `MEMORANDA/ROUND_016_SOURCE_EXTENSION.md` | Read all 544 lines. Lines 310–326 confirm the same source/background convention; lines 289–306 and 405–469 delimit the energy-based estimate and its threshold. Its actual preparation remains an additional hypothesis for its dynamic statement. |
| `THEOREMS/THM-045_ENERGY_HAAR_INPUT_INSUFFICIENCY_AT_THRESHOLD.md` | Whole assertion and exact negation; no altered theorem substituted. |
| `TASKS/ACTIVE/TASK-101_ROUND023_STATIC_THRESHOLD_HOSTILE.md` | Exact bounded task, base, worktree, allowed inputs, output and seal restrictions. |
| `MEMORANDA/ROUND_023_STATIC_THRESHOLD_INPUT_OBSTRUCTION.md` | Full candidate proof under hostile review, including the sentence identified as false. |
| `MEMORANDA/ROUND_023_STATIC_THRESHOLD_ARTIFACTS/SOURCE_PREFLIGHT.md` | Root's source-use attestation only. Its reference to TASK099 was not followed. |
| `MEMORANDA/ROUND_023_STATIC_THRESHOLD_ARTIFACTS/EXPOSURE.md` | Root exposure and chronology attestation only. Hashes authenticate supplied bytes, not chronology or independence claims. |

No R23 blind material, other audit, root checker/results, root scratch, current state/history, memory file, external source, non-allowlisted link, private source, or source cited only by one of the inputs was opened. No installation, child, canonical edit, commit, or push occurred. Creation of the assigned worktree necessarily updated Git worktree/branch metadata, as authorized. The checkout printed the base commit subject; this incidental metadata was not used as mathematics. Ambient developer instructions included a high-level memory summary; no part of it was used as evidence. The parent task and subsequent messages contained the bounded role and, after this reviewer discovered F01, an instruction to preserve and explicitly report it; they supplied no alternative proof or checker.

Independent evidence here means reconstruction and newly written diagnostics in this fresh hostile context, after exposure to the candidate narrative. It is not a blind reconstruction. The source modules' broader historical statuses are unchanged. This audit verifies their exact facts needed for THM045, not every earlier campaign theorem.

## 3. Normalization and original background: hostile reconstruction

At `d=4,s=2`, the R1 coefficient is exactly one: its power of pi is zero and both gamma arguments are one. The R4 coefficient in the heat integral is `4*pi^2`, and the heat-time exponent is zero. Consequently the nonzero Fourier coefficients are `1/|k|^2` and the zero coefficient is zero.

The central Euclidean Gaussian integral is exactly `|x|^-2`. Subtracting it in a local ball leaves the nonzero image terms and the constant term at small heat time, and the torus remainder minus the Euclidean term at large time. The former have an exponentially small image bound, with every fixed derivative; the constant is integrable over a finite interval. The latter have exponential torus decay and an integrable four-dimensional Euclidean tail. This supplies the smooth even local regular part. Compactness off the origin then supplies all fixed-order derivative bounds used in R23. This is a local statement; no globally smooth shortest-distance power is asserted.

In particular, `K` has local order `r^-3` in dimension four and is Haar integrable. Its distributional divergence has Fourier coefficient `4*pi^2` at every nonzero mode and zero at mode zero. Thus it is precisely `4*pi^2*(delta_0-dx)`. The sign agrees with the positive outward flux of `2*x/|x|^4`; the sphere has area `2*pi^2`. The atom cannot be discarded in the Haar contraction.

For a smooth real test, the difference of its gradients is bounded by a constant times torus distance. Therefore `J_h` has integrable local order `r^-2`. Since the odd integrable force has zero mean, the first term of its row integral vanishes. For the second term, integration by parts in `y` gives

    integral K(x-y).grad h(y) dy = 4*pi^2*(h(x)-integral h).

The minus sign already present in `J_h` then gives the row `-4*pi^2*(h-mean h)`. Its full Haar integral is zero. For the chosen zero-mean test, the exact original statistic is the ordered raw sum with coefficient `1/(2*N^2)` plus `4*pi^2*eta_N[h]`. This verifies R23 lines 9–21 against R1, R4, and R16 independently of a formal punctured Laplacian calculation.

No singular value of the force or source on a coincident empirical label is used. Singular Haar contractions are justified before constructing the laws, by integrability and the full divergence measure.

## 4. Negative regular part and exact lattice subtraction

The majorants just described also justify taking `x` to zero after central Gaussian subtraction. The result is R23 (2.1). With `v=4*pi*t`, its factor is pi, not `4*pi^2` or one. The image and Fourier versions of the same periodized Gaussian imply `Theta(v)=v^-1/2*Theta(1/v)`. Under inversion `v=1/u`,

    [Theta(v)^4-1-v^-2] dv

on `(0,1)` becomes `[Theta(u)^4-u^-2-1] du` on `(1,infinity)`. Therefore the two portions are equal, including the constant and power subtractions. The positive exponential terms may then be integrated term by term, giving

    H0 = 2*pi*(sum_{k!=0} exp(-pi*|k|^2)/(pi*|k|^2) - 1).

All sums here converge absolutely. No Epstein-zeta value or theta inequality from outside the dossier is imported. The explicit rational theta bound in the proof is valid: the first nine Taylor terms of `exp(3)` exceed 20; `n^2>=1+3*(n-1)` for positive integer `n`; the resulting ratio is `8799/7999`; and its fourth power is less than `3/2`. The positive sum is less than `1/(2*pi)<1/6`, proving `H0<-5*pi/3`. Both the sign and strictness survive hostile checking.

For the grid identity, averaging a Fourier character over the full `m^4` grid kills every frequency outside `m*Z^4`. A surviving coefficient is `m^4/|m*k|^2=m^2/|k|^2`. Both sides have zero mean, so no undetermined additive constant remains. Distributional equality is legitimate; after restriction away from the grid both sides are smooth and hence equal pointwise. Near the origin, `m^2*g(m*x)` has singularity exactly `|x|^-2` and regular constant `m^2*H0`. The left side has the identical singularity, regular constant `H0`, and all nonzero grid values. Thus

    sum_{z in G_m, z!=0} g(z) = (m^2-1)*H0.

The energy definition counts each unordered pair once with coefficient `1/N`. Every displacement occurs once in the sum seen from each particle. The resulting energy is one half of that displacement sum. No extra `N`, falling factorial, diagonal constant, or factor two is missing in (3.2).

Finally, the force seen at each grid point is zero: every displacement is paired with its negative; an order-two displacement is itself fixed by negation and its smooth periodic odd force is zero. This proves the vanishing first variation of energy before an estimate is applied. It does not assert local or global energy minimality of the grid.

## 5. Uniform deformation, separation, and energy margin

For the fixed smooth vector field `v(x)=sin(2*pi*x_1)e_1`, a sufficiently small fixed `epsilon0` makes every `T_epsilon` a degree-one diffeomorphism. The derivative in the first coordinate is positive. Applying the Lipschitz bound to each periodic lift proves the two-sided torus-distance bound even when the minimizing lift changes; no differentiation of the distance function is required.

An epsilon derivative of a pair displacement produces `v(x)-v(y)`, whose size is at most a fixed constant times the original distance. The second derivative of the pair potential is its Hessian contracted twice against that displacement difference. The Hessian has order `r^-4` and the two differences contribute `r^2`, leaving order `r^-2`. The deformed distances are uniformly comparable to the original ones. Smooth terms off the diagonal have uniform fixed constants. Thus (3.4) has constants independent of `m` and of the allowed epsilon.

For completeness, after taking shortest grid representatives `j/m`, the deleted near-diagonal sum is bounded by

    m^-2 * sum_{0<|j|<=delta*m} |j|^-2 <= C*delta^2.

The number of integer points in a shell of fixed width at radius `n` is at most `C*(n+1)^3`, so the shell sum is at most a constant times `(delta*m)^2`. For `delta<1/m` it is empty. The same calculation through a fixed torus radius yields the full uniform bound (3.5). Grid boundary representatives change constants only. Each particle has the same displacement multiset, so the second energy derivative, with its literal `1/N` unordered-pair coefficient, is bounded by `C_E*N`.

The exact first derivative at the grid is zero. Taylor's theorem with this second-derivative bound gives R23 (3.4)–(3.6) and the energy inequality at `epsilon=a/m`. The perturbation cost is of order `N*(a/m)^2=a^2*m^2`, precisely the order that can be absorbed into the negative grid energy by choosing one fixed positive `a` sufficiently small. Such a choice is compatible with `a<=epsilon0`; it does not depend on `m`. The negative margin and separation then hold for every `m>=5`, after choosing a fixed smaller energy constant. This supplies genuine fixed constants, rather than a different `a_m`.

The proof does not use critical coupling, a Gibbs distribution, a gradient evolution, isotropy, or a lower bound for arbitrary weighted kernels in this step.

## 6. Exact lower-order cancellations and moving-scale source

The crucial uniform bound is not merely convergence of an undeformed Riemann sum. For each of the derivatives through order three, differentiate the source in its two separate factors. If `l` derivatives fall on `K`, its derivative has order `r^(-3-l)`, while the `l` displacement differences contribute `r^l`. The other factor is the difference at `x` and `y` of the smooth function formed from derivatives of `h(T_epsilon x)` and fixed powers of `v(x)`. That function has a uniform Lipschitz bound, including derivatives of `v`; it contributes another factor `r`. Every term therefore has order at most `r^-2`. The same proof covers `l=0` and all combinations. This verifies R23 line 95 without treating the velocity powers as constant in space.

The grid bound then yields a uniform third epsilon derivative of the full statistic. The smooth original Haar row is included and has the same uniformity directly. The factor `N^-2` in the pair sum is essential; after summing over the first grid point it leaves the normalized displacement sum used above.

At epsilon zero, the source is a translation-covariant linear functional of `h`. Grid relabelling leaves it unchanged, so its frequencies `+/-2e_1` are killed for the prescribed `m>=5`. For the first variation, simultaneous translation of `h` and `v` leaves the bilinear functional unchanged by the same grid relabelling. Its total frequencies are `+/-e_1` and `+/-3e_1`, none in `m*Z^4`. This includes differentiation of the row, whose transformation is the same. Hence `F_m(0)=F'_m(0)=0` exactly. The exclusion of small aliasing grids is substantive; no quantitative approximation is substituted for these identities.

For the second derivative at zero, the differentiated kernel has the integrable order already established. Removing a diagonal tube of radius delta costs at most `C*delta^2` both in the grid sum and in the Haar double integral, uniformly in `m`. On its complement a continuous cutoff gives ordinary product-grid Riemann convergence. First take `m` to infinity at fixed cutoff and then delta to zero. The smooth row converges directly. This proves convergence of the second derivatives themselves.

The continuum pushforward has smooth density because the Jacobian is bounded away from zero and the inverse diffeomorphism depends smoothly on epsilon. Differentiating the inverse and reciprocal Jacobian gives the expansion in every fixed smooth norm,

    rho_epsilon = -2*pi*epsilon*cos(2*pi*x_1) + O(epsilon^2).

The original Haar contractions cancel the linear terms exactly; the continuum expression is the centered bilinear form, with coefficient one half in its symmetric version and coefficient one in its unsymmetrized version. It is bounded on bounded densities by a fixed multiple of the square of their sup norm because `K` is Haar integrable. Consequently replacing the density by its first variation introduces an error of order epsilon cubed.

A direct real trigonometric calculation checks the sign and coefficient. Write `theta=2*pi*x_1`. The first-order density is `-2*pi*epsilon*cos(theta)`; its force convolution is `-4*pi^2*epsilon*sin(theta)`; and `grad h=-8*pi*sin(theta)*cos(theta)e_1`. Their product is `-64*pi^4*epsilon^2*sin(theta)^2*cos(theta)^2`. The Haar average of the last trigonometric product is `1/8`. Thus the quadratic coefficient is `-8*pi^4`, and the second derivative is `-16*pi^4`. This also checks the single-frequency Fourier normalization independently of the candidate's triple-sine integral.

Only after these exact cancellations, derivative convergence, and uniform third-derivative bound have been proved is epsilon set to `a/m`. The scaled Taylor remainder is bounded by a constant times `a^3/m`, and hence

    m^2*F_m(a/m) -> -8*pi^4*a^2.

No uniform rate for zeroth-order singular Riemann convergence is assumed. This is the point where a naive continuum replacement would fail, but the supplied derivative argument does not make that inference.

## 7. Translation, absolute moment, and genuinely smooth densities

For an arbitrary collision-free configuration, common translation of the particles is equivalent to translating the test, with its original Haar row. For the two real frequency-two tests, this gives a two-dimensional rotation of the coefficients `C,S`. Averaging one uniform common translation therefore yields exactly

    E_Y |P_N[J_h](x+Y)| = (2/pi)*sqrt(C^2+S^2).

The first coordinate of Haar translation covers two full periods of the angle `4*pi*Y_1`; the mean absolute cosine remains `2/pi`. The signed average is zero and is not used as an absolute estimate.

The deformed grid is invariant under inversion because the displacement field is odd. For the sine test, its gradient is even and the force is odd, so the raw source changes sign under inversion. Its row is odd as well. Hence `S=0` for that specific grid. Combining the exact translation average with the negative source asymptotic and `sqrt(N)=m^2` gives exactly `16*pi^3*a^2`, with no loss in the constant.

Independent Haar translation makes each labelled one-body marginal Haar conditional on the pretranslated configuration. Independent uniform label permutation makes the joint law exchangeable. Neither operation asserts independent particles. Initially this orbit law need not have a full-dimensional density, so that construction alone would not prove the frozen theorem.

The full-dimensional smoothing step is valid as actually used in the moment calculation. At each fixed `m`, the base configuration has strict positive separation and a strict negative energy margin. Energy and both source coordinates are continuous on a collision-free compact neighborhood. One may choose a closed product displacement neighborhood of a positive radius `delta_m<1/(16*m)` so that the pretranslation inequalities (6.1) hold. This uses only finite-dimensional continuity at each fixed `m`; no uniform-in-`m` continuity or density bound is needed.

A nonnegative smooth bump in that radius, independently added to each labelled point, gives a bounded smooth product density on the entire configuration torus. Translation averaging is an integral over a compact torus, and permutation averaging is a finite sum. For fixed `N`, all their differentiated integrands have finite suprema, so derivatives pass through those averages. The result remains nonnegative, normalized, bounded, and smooth. Its symmetries give the stated exact marginals.

The separation and energy inequalities are invariant under translations and permutations. The closed pretranslation neighborhood is compact, and its union over the compact translation group and finite permutation group is compact. Every point in the final support therefore satisfies these two inequalities, including closure points. These are precisely the support requirements in THM045.

For the moment limit, the pretranslation coordinate error in (6.1) bounds the error of the norm `sqrt(C^2+S^2)` by `m^-3`, since Euclidean norm is one-Lipschitz and the Euclidean difference is at most its coordinate sum. The exact translation-average formula then gives an error at most `(2/pi)*m^-3`. After multiplication by `m^2`, it vanishes. This is exactly the argument already written at R23 line 155. It does not need coordinate closeness after translation. The choice `c=min(1/2,c_E/2)` meets both final support requirements uniformly. No density bound independent of `N` is claimed or used.

## 8. AUD066-F01: false support sentence and its dependencies

**Location:** R23 proof, line 153, final sentence. **Type:** false ancillary mathematical assertion. **Severity:** non-load-bearing for THM045, but prevents an unqualified clean proof-text pass. **Confidence:** certain; exact rotation counterexample.

The offending sentence says: “All configurations in its support, including closure points, obey(6.1), since those inequalities were imposed on a closed product neighborhood and are invariant under translations/permutations.” The third inequality of (6.1) is

    |C-F_m(a/m)| + |S| <= m^-3.

It is not invariant under translations. On the unsmoothed base configuration, `C=F_m(a/m)` and `S=0`. Translation by `Y_1=1/8` makes the rotation angle pi/2; the new pair is `(0,C)` up to the immaterial sine sign convention. Its left side in the asserted inequality becomes `2*|F_m(a/m)|`. The proved asymptotic gives `2*|F_m(a/m)|` of order `m^-2` with a strictly positive coefficient, which exceeds `m^-3` for all sufficiently large `m`.

This is not an artifact of having used the atomic orbit. For any pretranslation support point satisfying the third inequality, write `C=F_m+e` and keep `|e|+|S|<=m^-3`. After the same quarter-period rotation the new left side is at least `2*|F_m|-m^-3`, again larger than `m^-3` for sufficiently large `m`. The final law has translation-invariant support, so the same false universal coordinate bound cannot hold on its final support. The error persists for a genuinely smooth density.

**Dependency analysis:** The first two lines of (6.1) are invariant and establish all final support conditions in THM045. The law's regularity and symmetries use only the averaging construction. The required limit at line 155 uses the coordinate inequality before the translation integral and then the rotation-invariant amplitude in (5.1). Those statements already appear in the supplied proof and remain valid. Neither the theorem nor this existing moment argument requires a uniform posttranslation coordinate inequality. Thus F01 does not negate any conjunct of THM045 or change the exact constant.

**Required explicit textual disposition:** A separate correction should restrict the sentence's inherited support statement to the first two inequalities of (6.1), while retaining the third as a pretranslation estimate for the amplitude calculation. This is a proposed correction, not an edit or a silent reinterpretation of the frozen candidate. This issued report and its eleven exact input copies preserve the false sentence byte-for-byte. Root alone may issue and integrate the correction.

No other load-bearing or ancillary mathematical defect was found in the eleven-input proof chain required for this claim. This statement is not an audit of unrelated assertions in earlier modules.

## 9. New independent diagnostic and active falsification

The new standard-library diagnostic does not read or copy any root checker or results. Its main route is a direct Ewald calculation of the actual four-dimensional singular kernel, obtained by splitting the heat representation at `t=1/(4*pi)`. The resulting potential is a Gaussian image sum plus a Fourier sum minus pi. Differentiation gives its force. At the origin, subtracting the coefficient-one singularity contributes another negative pi. The exact analytic identity used for the diagnostic is derived in its README; the computation is a finite truncation, not a rigorous numerical enclosure.

Three transverse grid directions are summed by integer squared-radius multiplicities, leaving all first-coordinate pairs explicit. The singular grid self subtraction is tested separately. This differs from a smooth finite-mode replacement of the singular kernel. All numerical assertions are labelled diagnostic; none establishes the infinite-lattice sign, the uniform singular derivative bound, the limiting Riemann passage, or density smoothness.

Run from the isolated worktree:

    python3 AUDITS/HOSTILE/ROUND_023_STATIC_THRESHOLD_HOSTILE_ARTIFACTS/hostile_diagnostic.py

**Final result: PASS, 384 assertions across 22 categories, with 12 detecting mutations.** Python 3.9.6; standard library only; deterministic cases; no random seed. Exact auxiliary arithmetic uses integers and fractions. Ewald values use ordinary Python floating arithmetic, explicitly without interval certification. The code, complete result JSON, and code digest are in the packet.

The diagnostic independently checks the theta rational bounds, trigonometric moments, exact finite-frequency selection, explicit small-grid aliasing, kernel regular-part sign, singular lattice identity with both self constants, source inversion symmetry, negative energy for a fixed illustrative deformation, moving-scale source convergence, source/background factors, common-translation absolute average, and the smoothing error power. For `a=0.05`, scaled source values at `m=5,7,9,13,17` are approximately `-2.89046,-2.46107,-2.28051,-2.11640,-2.04862`, approaching the analytic target `-1.94818`. This finite sequence is not a proof of the limit or an explicit bound for the sufficiently small `a` in the theorem.

The twelve detecting mutations are: omission of the regular self subtraction; omission of the central image finite part; replacing the lattice `m^2` factor by `N`; omission of the Haar row; reversal of its sign; halving the raw pair coefficient; reversal of the full force/row sign; replacing `N^2` by the falling factorial; omitting common Haar translation; using deformation scale `m^-2`; substituting the signed mean for the absolute mean; and omission of the `2/pi` factor. The actual false sentence F01 is separately detected by its quarter-period coordinate rotation; it is not counted as an invented mutation.

One preliminary diagnostic run failed a deliberately finite-grid closeness threshold when its largest grid was only `m=13`: the absolute scaled error was approximately `0.16822`, above the chosen `0.15` threshold. This was a diagnostic truncation-of-the-sequence issue, not a theorem contradiction: the proof asserts convergence with no rate or threshold at 13. The grid sequence was extended to 17 without weakening that threshold, and the error became approximately `0.10044`. Before the final rerun, a proposed epsilon-sign parity check was restricted to an even grid, where half-period relabelling proves it; no odd-grid parity is claimed. Both adjustments and the failed initial check are disclosed in `DIAGNOSTIC_HISTORY.md`. The final code/results, not an earlier development version, are sealed.

## 10. Entire-conjunction coverage and handoff

| Frozen requirement | Disposition and evidence |
|---|---|
| Exact coefficient-one four-dimensional Coulomb kernel and original source | Verified; R4 heat and divergence reconstructed, full compensated Haar row retained. |
| Fixed positive `a,c` and one threshold `m0` | Verified; uniform deformation constants precede the fixed small choice of `a`; final support constant is fixed. |
| Every integer `m>=m0`, `N=m^4` | Verified; grid and bump construction work for every such integer, not just a subsequence. |
| Bounded smooth probability density on the full `N`-body torus | Verified; product bump followed by compact translation and finite permutation averaging; no uniform density bound asserted. |
| Exchangeability and common-translation invariance | Verified directly from independent group averages. |
| Exactly Haar one-body marginals | Verified conditional on pretranslated coordinates. |
| Separation and strictly negative energy on the entire support | Verified, including closure points; these are the invariant first two bounds in (6.1). |
| Literal deleted statistic and singular/background integrability | Verified off collisions and through Haar integrability; no singular diagonal assigned. |
| Exact positive scaled absolute limit | Verified; derivative-level moving-scale passage, inversion, translation factor and negligible bump error give `16*pi^3*a^2`. |
| Exact negation | Ruled out by this full construction; the false extra coordinate-support assertion is not a theorem conjunct. |
| Claimed invariance of all of (6.1) at line 153 | False; AUD066-F01 requires separate correction. |
| Actual iid-flow, integrated source, or campaign endpoint failure | Not claimed and not inferred. |

Only this report and its unique hostile artifact directory, plus the corresponding archive and seal records, were authored in the assigned worktree. The eleven permitted source overlays and packet copies are exact prescribed bytes. No canonical or source edit, branch switch, commit, push, outside source, or child occurred. The final packet contains all eleven exact input copies, their original manifest, this report, the new diagnostic and results, source/exposure record, verification program, output manifest, and handoff README. The verifier checks exact membership, every input and output digest, byte equality of all archive members against disk without extraction, the standalone/report-copy equality, safe member types and paths, and read-only modes. The archive digest and final receipt accompany the packet. Its exact final membership and hashes are enumerated in those manifests rather than guessed in this report.

The bounded handoff is complete when the read-only packet's final verifier passes. Root alone compares this hostile result with any other lane and issues the F01 correction and gate decision. Any correction to this issued audit must be a new artifact; neither the preserved candidate nor this report is to be edited after seal.
