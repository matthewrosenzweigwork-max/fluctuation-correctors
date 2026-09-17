# Round 003 fresh reconstruction of the sharp iid Riesz pair criterion

Date: 2026-09-17 UTC. Worker: `/root/r003_fresh_sharp`.
Worktree: `/private/tmp/hocf-r003-fresh-sharp-20260917`.
Branch: `codex/hocf-r003-fresh-sharp`.
Baseline: `2f532ccd2cb5f3d84db456be96e438f03f7e2ad2`.

**Verdict:** every assertion of the permitted THM-019 statement is independently reconstructed below on its stated iid Haar, positive-power, bare-pair scope. The proof gives explicit admissible constants in terms of local kernel bounds. This reconstruction is self-checked. It is not a review, comparison, or verdict on the unseen constructor proof, and it does not certify a dynamic corrector, an endpoint distribution, or the campaign target.

## 1. Exposure and frozen scope

Before mathematical work, this worker created the separate local worktree at the specified baseline, enabled a sparse checkout, copied only the four permitted input files, and checked source/copy SHA-256 equality. No constructor sharp proof, sharp review/reconstruction, THM-018, root TeX, canonical ledger, previous audit, or unpermitted mathematical source was read. No memory file or external source was consulted.

The complete content exposure was: the governing instructions delivered in the task context; the parent dispatch; the four files in the following table; and a later parent administrative message naming TASK-029. TASK-029 itself was not opened. The initial root `git status` and path inventory exposed filenames, including filenames of excluded outputs, but no contents from those files. The bounded reading list superseded the repository's general request to read broad orientation documents; this worker did not open README_FIRST or MODEL_ORCHESTRATION. Root retains canonical integration and campaign-level audit duties.

| Permitted input | SHA-256 |
|---|---|
| `AGENTS.md` | `cc3a478358f1fcb3ccf472615c715acfdef575d9a80b5aa49417593a25825ed3` |
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57` |
| `THEOREMS/THM-019_SHARP_IID_RIESZ_PAIR_CRITERION.md` | `bfcc98dd9f0edeaa24a91d0348fd9932bc4bce3a23443b9901f2aaa35a7181a1` |
| `MEMORANDA/ROUND_003_COLLISION_FALSIFICATION.md` | `9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4` |

The THM-019 statement itself includes a one-sentence method description (close-pair count, local positivity, exterior variance, and an interior L1 bound). Thus this is independent of the **unseen proof narrative**, but it is not blind to that method hint. The expressly permitted collision memorandum supplies the already-sealed local Riesz facts and earlier iid results; its displayed status is SELF_CHECKED. Its normalization and the exact finite-particle facts actually used are checked below. The earlier sufficient probability theorem is not needed for this reconstruction: the L1 bound below supplies sufficiency directly.

Fix an integer \(d\ge1\) and \(d/2<s<d\). The torus is \(\mathbb R^d/\mathbb Z^d\), Haar mass one, with characters \(e^{2\pi i k\cdot x}\). The mean-zero positive-power Riesz kernel has

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}
 |k|^{s-d}\quad(k\ne0).
\]

Let \(X_1,\ldots,X_N\) be independent Haar variables, \(N\ge2\). The statistic is precisely

\[
 P_N=\frac1{N^2}\sum_{i<j}g(X_i-X_j),\qquad
 u_N=N^{2s/d-2}.
 \tag{F1}
\]

The factor \(1/2\) in the ordered definition has already been absorbed by using unordered pairs. There is no self-label term or diagonal trace. This concerns the initial iid law, without a dynamic, stationary, Gibbs, or arbitrary-exchangeable-law bridge.

The primary assertion is: for each such \(d,s\), there exist \(a,p,C>0\) and \(N_0\), depending only on \(d,s\), such that every \(N\ge N_0\) satisfies

\[
 \mathbb P(P_N\ge a u_N)\ge p,\qquad
 apu_N\le \mathbb E|P_N|\le Cu_N.
 \tag{F2}
\]

Its exact negation is the existence of an admissible \(d,s\) for which, for every proposed \(a,p,C>0,N_0\), some \(N\ge N_0\) violates at least one bound in (F2). The sequence consequences are proved after (F2), so their negations are excluded by the same uniform constants.

## 2. Prerequisite and normalization checks

Write \(\alpha=(d-s)/2\). The local representation in Section 3 of the permitted memorandum follows from

\[
 A=\frac{4^\alpha\pi^{d/2}}{\Gamma(s/2)},\qquad
 g(x)=A\int_0^\infty t^{\alpha-1}(p_t(x)-1)\,dt,
\]

where \(p_t\) is the periodized Gaussian heat kernel. The prefactor check is

\[
 \frac{A\Gamma(\alpha)}{(4\pi^2)^{\alpha}}
 =\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}.
 \tag{F3}
\]

The Gaussian at the zero lattice translate gives, by \(v=|x|^2/(4t)\),

\[
 A(4\pi)^{-d/2}\int_0^\infty
 t^{-s/2-1}e^{-|x|^2/(4t)}\,dt=|x|^{-s}.
 \tag{F4}
\]

Thus the principal coefficient is exactly positive one, without an omitted torus-volume or Fourier factor. The remaining lattice translates have exponentially small small-time bounds on a fixed ball about zero; at large time the torus mean-zero heat kernel decays exponentially, and the subtracted Euclidean kernel is integrable against the displayed weight. These bounds also hold after spatial differentiation. They give \(g(x)=|x|^{-s}+H(x)\) near zero with smooth bounded \(H\), as in the permitted prerequisite, and smoothness away from zero. Small-time L1 integrability follows from \(\|p_t-1\|_1\le2\) and \(\alpha>0\). Large-time exponential decay gives the remaining L1 integral and mean zero. This checks the sign, leading coefficient, integrability, and geometry used below; it uses no logarithmic substitution.

Let \(v_d\) be the Euclidean unit-ball volume. Choose \(0<r_*<1/4\), depending only on \(d,s\), so that for \(0<|x|\le r_*\),

\[
 \tfrac12 |x|^{-s}\le g(x)\le \tfrac32 |x|^{-s}.
 \tag{F5}
\]

For \(0<R\le r_*\), put

\[
 f_R(x)=g(x)\mathbf1_{\{\operatorname{dist}(x,0)<R\}},
 \quad h_R=g-f_R,\quad
 \tau_R=\int f_R,\quad k_R=h_R+\tau_R.
 \tag{F6}
\]

The boundary spheres are Haar-null. In particular \(f_R\ge0\), \(\int h_R=-\tau_R\), \(\int k_R=0\), and \(k_R\in L^2\). Polar integration gives constants \(C_1,C_2>0\), depending only on \(d,s\), such that

\[
 0\le\tau_R\le C_1 R^{d-s},\qquad
 \|k_R\|_2^2\le C_2 R^{d-2s}.
 \tag{F7}
\]

For fully explicit choices in terms of the fixed kernel, take

\[
 C_1=\frac{3dv_d}{2(d-s)},\quad
 B=\int_{\operatorname{dist}(x,0)\ge r_*}g(x)^2\,dx,
 \quad
 C_2=B r_*^{2s-d}+\frac{9dv_d}{4(2s-d)}.
 \tag{F8}
\]

Indeed, \(\|k_R\|_2^2=\int h_R^2-\tau_R^2\le\int h_R^2\), the interior annulus contributes at most
\(\frac94dv_d\int_R^{r_*}t^{d-1-2s}dt\), and \(B\le Br_*^{2s-d}R^{d-2s}\). Finiteness of \(B\) follows from smoothness off zero. The two strict inequalities on \(s\) are used separately: \(s<d\) for the interior first moment and \(2s>d\) for the exterior squared-norm power.

All bounds are for measurable spatial truncations of a static random statistic. No singular Itô formula, integration across collisions, or dynamic cutoff passage is used. Since every difference is Haar and \(g\in L^1\), the original finite sum is integrable, is finite almost surely, and has mean zero.

## 3. Exact exterior variance and the L1 upper bound

Write \(M=N(N-1)/2\) and define

\[
 I_R=\frac1{N^2}\sum_{i<j}f_R(X_i-X_j),\quad
 T_R=\frac1{N^2}\sum_{i<j}k_R(X_i-X_j),\quad
 D_R=\frac{M}{N^2}\tau_R.
\]

The exact identity, valid almost surely, is

\[
 P_N=I_R+T_R-D_R,\qquad
 I_R\ge0,\quad \mathbb EI_R=D_R,\quad \mathbb ET_R=0.
 \tag{F9}
\]

This is a raw exterior sum after centering its kernel; it does not identify the raw sum with the background-corrected statistic of the nonzero-mean kernel \(h_R\).

For an unordered edge \(\{i,j\}\), translation invariance gives
\(\mathbb E[k_R(X_i-X_j)\mid X_i]=0\), and the same is true conditioning on \(X_j\). Two disjoint edges are independent. Two distinct edges with one common label have zero product expectation by conditioning on that label: their remaining labels are independent and their conditional means vanish. Cauchy–Schwarz ensures integrability of these products. Consequently only identical edges remain in the second moment, and

\[
 \mathbb E T_R^2=\frac{M}{N^4}\|k_R\|_2^2.
 \tag{F10}
\]

This rederives the prerequisite's canonical iid coefficient instead of assuming edgewise mutual independence.

Set

\[
 R_N=N^{-2/d}
\]

and choose \(N_0\ge2\) so that \(R_N\le r_*\) for every \(N\ge N_0\). Equations (F7) and (F10) give

\[
 D_{R_N}\le\tfrac12 C_1u_N,\qquad
 \mathbb E T_{R_N}^2\le\tfrac12 C_2u_N^2.
 \tag{F11}
\]

The exponents are exact:
\(R_N^{d-s}=u_N\) and
\(N^{-2}R_N^{d-2s}=u_N^2\).
Since \(I_{R_N}\ge0\) and its expectation is \(D_{R_N}\),

\[
 \mathbb E|P_N|
 \le \mathbb E|I_{R_N}-D_{R_N}|+\mathbb E|T_{R_N}|
 \le 2D_{R_N}+\sqrt{\mathbb E T_{R_N}^2}
 \le\left(C_1+\sqrt{C_2/2}\right)u_N.
 \tag{F12}
\]

This proves the L1 upper bound without assuming any second moment for \(P_N\), and without reading THM-018.

## 4. A positive lower tail at the same order

Choose a constant \(0<\theta\le1\) later. Let \(Z_N\) count unordered pairs whose torus separation is smaller than \(\theta R_N\). Each indicator has expectation

\[
 q_N=v_d\theta^dR_N^d=v_d\theta^dN^{-2}.
\]

Any two distinct edge indicators are independent. Disjoint edges use independence of their labels. For edges sharing one label, conditioning on that label leaves independent Haar differences, and the conditional probability of either event is the fixed value \(q_N\). This pairwise assertion does not claim mutual independence of three or more edges. Thus

\[
 \mathbb EZ_N=Mq_N,\qquad
 \mathbb EZ_N^2=Mq_N+M(M-1)q_N^2.
 \tag{F13}
\]

Cauchy–Schwarz applied to \(Z_N\mathbf1_{\{Z_N>0\}}\) yields

\[
 \mathbb P(Z_N>0)
 \ge\frac{Mq_N}{1+(M-1)q_N}
 \ge\frac{v_d\theta^d/4}{1+v_d\theta^d/2}.
 \tag{F14}
\]

If \(v_d\theta^d\le1\), this is at least \(v_d\theta^d/6\), uniformly for \(N\ge N_0\).

On \(\{Z_N>0\}\), one term of \(I_{R_N}\) has, by (F5), size at least

\[
 \frac1{2N^2}(\theta R_N)^{-s}
 =\tfrac12\theta^{-s}u_N.
 \tag{F15}
\]

Every other term of \(I_{R_N}\) is nonnegative. The adverse exterior event is controlled unconditionally by its finite variance:

\[
 \mathbb P\left(T_{R_N}<-\tfrac18\theta^{-s}u_N\right)
 \le 32C_2\theta^{2s}.
 \tag{F16}
\]

In particular, no conditional variance claim given the close-pair event is made.

Choose \(\theta>0\) small enough that all of

\[
 \theta\le1,\qquad v_d\theta^d\le1,\qquad
 \theta^s\le\frac1{4C_1},\qquad
 \theta^{2s-d}\le\frac{v_d}{384C_2}
 \tag{F17}
\]

hold. Such a choice is possible because \(s>0\) and \(2s-d>0\). The third condition and (F11) give
\(D_{R_N}\le\frac18\theta^{-s}u_N\). The fourth makes the upper bound (F16) at most \(v_d\theta^d/12\), half the guaranteed close-pair probability. On the close-pair event excluding the adverse exterior event, (F9) and (F15) imply

\[
 P_N\ge(\tfrac12-\tfrac18-\tfrac18)\theta^{-s}u_N
 =\tfrac14\theta^{-s}u_N.
\]

The elementary union bound therefore proves

\[
 \mathbb P(P_N\ge a u_N)\ge p,\qquad
 a=\tfrac14\theta^{-s},\quad p=\frac{v_d\theta^d}{12}>0.
 \tag{F18}
\]

Dependence between the two events causes no problem: their intersection has probability at least the probability of the first minus the probability of the complement of the second. Integrating this positive tail gives
\(\mathbb E|P_N|\ge apu_N\). Together with (F12), this proves all of (F2), with \(C=C_1+\sqrt{C_2/2}\).

The separation of scales is decisive. Close-pair probability is bounded below by a constant times \(\theta^d\); adverse exterior probability is bounded above by a constant times \(\theta^{2s}\). The latter can be made smaller precisely in the strict range used here. No infinite-variance argument is involved.

## 5. Every sequence consequence in THM-019

Let \(\beta_N>0\), \(b_N=\min(\beta_N,1)\), \(\sigma_N=\sqrt{Nb_N}\), and define

\[
 A_N=\sigma_Nu_N=\sqrt{b_N}\,N^{2s/d-3/2}.
 \tag{F19}
\]

For all \(N\ge N_0\), (F2) implies

\[
 apA_N\le\mathbb E|\sigma_NP_N|\le CA_N,\qquad
 \mathbb P(\sigma_NP_N\ge aA_N)\ge p.
 \tag{F20}
\]

If \(A_N\to0\), the upper expectation bound gives L1 convergence to zero. Markov's inequality then gives convergence in probability. If \(A_N\not\to0\), there are \(\delta>0\) and infinitely many \(N\) with \(A_N\ge\delta\); along them
\(\mathbb P(|\sigma_NP_N|>a\delta/2)\ge p\), which prevents convergence in probability. The lower expectation bound also prevents L1 convergence. Hence both modes of convergence are equivalent to

\[
 A_N\to0
 \quad\Longleftrightarrow\quad
 b_NN^{4s/d-3}\to0.
 \tag{F21}
\]

If \(\sup_N A_N<\infty\), Markov and (F20) show uniform tightness for \(N\ge N_0\). There are only finitely many smaller indices, and each corresponding random variable is integrable, so these indices preserve tightness. If \(A_N\) is unbounded, select a subsequence tending to infinity. For each fixed \(L>0\), arbitrarily late members have \(aA_N>L\) and thus probability at least \(p\) of exceeding \(L\). This contradicts tightness, for example with tolerance \(p/2\). The same proof applies to any subfamily on which \(A_N\) is unbounded. Squaring the nonnegative deterministic factors gives the exact boundedness/unboundedness criterion stated in THM-019.

At \(\sigma_N=\sqrt N\), \(A_N=N^{2s/d-3/2}\). Within the asserted range \(d/2<s<d\), it tends to zero for \(s<3d/4\), equals one for \(s=3d/4\), and tends to infinity above that threshold. Thus the endpoint family is tight and does not converge to zero; above it the family is not tight. No endpoint distribution, stable limit, or convergence of the entire family to any nonzero law has been proved or used. The smaller-s statements mentioned in THM-019 are outside this reconstruction.

## 6. Falsification checks and scope limits

The following independent checks target errors that would invalidate the proof.

- **Discarded mean:** zero mean of the original kernel does not mean zero mean of the exterior kernel. The finite coefficient is \(D_R=(N-1)\tau_R/(2N)\). At \(N=2\) it is \(\tau_R/4\), and at \(N=3\) it is \(\tau_R/3\). Dropping it would create a false positivity argument.
- **Finite-particle variance:** (F10) equals \(\|k_R\|_2^2/16\) for \(N=2\), and \(\|k_R\|_2^2/27\) for \(N=3\). These are the direct one-edge and three-edge coefficients. No replacement of \(N^2\) by \(N(N-1)\) is made.
- **Dependence:** pairwise indicator independence and vanishing pair covariances have explicit conditional proofs. No product law for all edges is used, and no variance estimate is conditioned on a collision event.
- **Crude lower-bound failure:** combining one close pair with only a global bound \(g\ge-B\) would subtract an order-one quantity after normalization, whereas \(u_N\to0\). That route fails. In (F9) the correctly centered exterior has order-\(u_N\) fluctuations and an explicitly retained order-\(u_N\) deterministic mean.
- **One-cutoff failure:** using the very-close-pair radius itself for the exterior variance would generally produce an adverse-event estimate of the same \(\theta^d\) order as the event being saved, without a coefficient guarantee. The fixed exterior radius \(R_N\) and smaller radius \(\theta R_N\) are distinct in this proof.
- **Zero-mean compatibility:** \(\mathbb EP_N=0\) is maintained. A positive tail of size \(u_N\) with positive probability does not imply nonnegative \(P_N\) everywhere. The lower expectation bound is compatible with the upper bound, since \(ap=v_d\theta^{d-s}/48\to0\) as \(\theta\downarrow0\).
- **Endpoints and uniformity:** neither \(s=d/2\) nor \(s=d\) is asserted. Constants can deteriorate as these endpoints are approached. They are uniform in \(N\) and in every positive sequence \(\beta_N\), with fixed \(d,s\).
- **Law and kernel:** arbitrary iid density, evolved exchangeable law, actual backward corrector, and singular dynamics require additional estimates. Translation invariance and Haar conditional means are load-bearing here. No such bridge is inferred.

The exact rational checker in this output set independently enumerates iid samples from the cyclic group with seven elements at \(N=2,3,4,5\). It uses a nonconstant mean-zero even kernel and a nonnegative interior part. It verifies (F9), the exact centered exterior variance, both close-count moments, every distinct-edge indicator product, the centered-interior L1 inequality, the exterior Cauchy–Schwarz inequality, and the power identities for representative admissible rational exponents. It reports **19,734 passing checks over 19,600 configurations**. This finite-group test supports the finite iid algebra; it does not replace the continuous local-kernel proof or claim numerical evidence for a probability limit.

## 7. Verification, sealing, and handoff

Created output files, all confined to the isolated worktree:

- `AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_RECONSTRUCTION.md` — this report.
- `AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_INPUT_SHA256SUMS.txt` — frozen four-file input manifest.
- `AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_EXACT_CHECK.py` — independent standard-library rational checker.
- `AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_EXACT_CHECK.json` — checker output.
- `AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_OUTPUT_SHA256SUMS.txt` — final output manifest, excluding its own hash.

Verification performed:

1. Source/copy hashes were equal before mathematical work and the frozen input manifest was reverified after the report was written.
2. `python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_EXACT_CHECK.py` — PASS, as above; saved output reproduced byte-for-byte.
3. `git diff --check` and independent output-text checks — PASS; all text outputs have terminal newlines, no trailing whitespace, and balanced displayed-math delimiters.
4. The final output manifest was generated after the report and supporting files were complete, then every recorded hash was verified. The report contains no self-hash.

No TeX source was created or modified, so no TeX build was applicable. No campaign-wide verifier was run: doing so would load code outside the expressly permitted input set and would not certify this theorem. No unverified external theorem or citation is load-bearing. No canonical root file, state ledger, immutable input, or previously issued audit was modified. No commit, push, dependency change, remote operation, child agent, or public communication was performed.

There is no remaining proof gap in the stated THM-019 assertion within this reconstruction. The next action belongs to root: preserve these bytes, compare this independently reconstructed proof with the sealed constructor output, and assign the appropriate audit status. This report deliberately gives no verdict on that unseen output. All wider dynamic and corrector obligations remain untouched.
