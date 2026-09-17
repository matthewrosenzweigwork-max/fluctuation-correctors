# TASK-028: statement-only reconstruction of the sharp iid pair criterion

2026-09-17 UTC. Reconstructor: `/root/capacity`, Astra Max. Worktree `/private/tmp/hocf-round003-pair-transport-20260917`, baseline `2f532ccd2cb5f3d84db456be96e438f03f7e2ad2`.

**Reconstruction outcome: the stated probability lower bound, matching L1 scale, temperature equivalence, and tightness consequences are proved below in their declared range.** Mathematical status of this newly written proof: PROVED_CANDIDATE; verification status: SELF_CHECKED pending comparison and a separately allocated review. This report does not evaluate the unseen constructor's proof or its audit.

## 1. Exposure and precise scope

This is a reused context. It previously constructed the permitted TASK-022 iid projection/integrability/truncation report and the separate TASK-025 internal-pair transport diagnostic. Both were sealed before this task. The root sharp proof, its hostile review, THM-018, another reconstruction, root TeX, and other worktrees were not read. No result from the transport toy model is used in this proof.

The only new mathematical disclosure was the THM-019 statement card. It explicitly named broad ingredients: a close-pair-count second moment, positivity of the local singularity, an exact centered outer variance, and an L1 inner bound. Thus this is reconstruction from a statement with disclosed proof ingredients, using the permitted prior iid prerequisite; it is not a blank-session audit. Constants, truncation decomposition, event estimates, and consequences below were derived in this context without the root proof narrative.

The new task/card input seal is `AUDITS/ROUND_003_SHARP_BLIND_INPUT_SHA256SUMS.txt`, verified before work. The permitted earlier inputs are separately recorded in `AUDITS/ROUND_003_SHARP_BLIND_ADDITIONAL_INPUT_SHA256SUMS.txt`.

Fix an integer `d>=1` and

\[
 \frac d2<s<d.
\]

Let `g` be the mean-zero real even torus Riesz kernel with the frozen positive Fourier normalization. Let `X_1,...,X_N` be independent Haar points on the unit torus. The only statistic studied here is the initial bare pair

\[
 P_N[g]=\frac1{N^2}\sum_{i<j}g(X_i-X_j),\qquad
 u_N=N^{2s/d-2}. \tag{1.1}
\]

The frozen deleted-label definition gives (1.1) because the Haar first projection and mean of the difference kernel vanish. The statistic is integrable and has expectation zero. It is almost surely finite, since the finite set of distinct labels has no spatial collision under the Haar product law. Its infinite second moment in the stated range will not be used to infer a probability conclusion.

The target is to give constants `a,p,C>0` and integer `N_0>=2`, depending only on `d,s`, such that for every `N>=N_0`,

\[
 \mathbb P\{P_N[g]\ge a u_N\}\ge p,
 \qquad apu_N\le\mathbb E|P_N[g]|\le Cu_N. \tag{1.2}
\]

The exact negation is permitted data in this range violating at least one of these bounds or the ensuing stated implications. The proof below excludes that negation. It is not a statement about an actual backward corrector, an evolved interacting law, or a Gibbs law.

## 2. Analytic prerequisite and constants fixed before N

The permitted TASK-022 report proves from the frozen Fourier convention, by a torus heat-kernel integral, that `g` is integrable, has mean zero, is smooth off zero, and satisfies

\[
 g(z)=|z|^{-s}+H(z)
\]

with `H` smooth on the Euclidean ball of radius one third. It also proves the exact iid canonical-pair variance formula used below. No additional source theorem, extreme-pair theorem, or U-statistic limit theorem is imported.

Let `v_d` be the Euclidean unit-ball volume, `omega_d=d v_d`, and

\[
 H_*:=\sup_{|z|\le1/4}|H(z)|,\qquad
 r_*:=\min\left\{\frac14,[2(1+H_*)]^{-1/s}\right\}.
\]

Then for `0<|z|<=r_*`,

\[
 \frac12|z|^{-s}\le g(z)\le\frac32|z|^{-s}. \tag{2.1}
\]

In particular, the small-distance part is pointwise nonnegative. This fact uses the positive real-space principal coefficient, not a general assertion that positive Fourier coefficients imply pointwise positivity everywhere.

For `0<R<=r_*`, put

\[
 g_R^{\rm in}=g\mathbf1_{\{\operatorname{dist}(z,0)<R\}},\quad
 \tau_R=\int g_R^{\rm in},\quad
 h_R=g\mathbf1_{\{\operatorname{dist}(z,0)\ge R\}},\quad
 k_R=h_R+\tau_R.
\]

The torus balls are embedded at these radii. Because `integral g=0`, the last kernel has mean zero, and the translation-invariant pair kernel `k_R(x-y)` is canonical under Haar measure. Define

\[
 C_\tau=\frac{3\omega_d}{2(d-s)},\qquad
 C_V=1+\int_{\operatorname{dist}(z,0)\ge r_*}g(z)^2dz
            +\frac{9\omega_d}{4(2s-d)}.
 \tag{2.2}
\]

Both are finite, positive, and depend only on the fixed normalized kernel, hence on `d,s`. Polar integration and (2.1) give

\[
 0\le\tau_R\le C_\tau R^{d-s},\qquad
 V_R:=\|k_R\|_2^2=\int h_R^2-\tau_R^2
                 \le C_V R^{d-2s}. \tag{2.3}
\]

For the second estimate, on the annulus between R and `r_*`, the square is bounded by `(9/4) r^(-2s)`; its integral is at most `9 omega_d R^(d-2s)/(4(2s-d))`. The fixed outer integral is at most itself times `R^(d-2s)`, since `R<1` and `d-2s<0`. This proves (2.3) with the explicit displayed constant. It is the strict inequality `2s>d` that gives the power bound used in this reconstruction.

Fix

\[
 N_0=\max\{2,\lceil r_*^{-d/2}\rceil\},\qquad
 R_N=N^{-2/d}\quad(N\ge N_0). \tag{2.4}
\]

Thus `R_N<=r_*`. The two exact power identities used repeatedly below are

\[
 R_N^{d-s}=u_N,\qquad
 N^{-2}R_N^{d-2s}=u_N^2. \tag{2.5}
\]

All constants have been fixed before considering a temperature sequence.

## 3. Exact centered outer decomposition and L1 upper scale

Let `M_N=N(N-1)/2` and define

\[
 Q_N=\frac1{N^2}\sum_{i<j}g_{R_N}^{\rm in}(X_i-X_j),\qquad
 Y_N=\frac1{N^2}\sum_{i<j}k_{R_N}(X_i-X_j).
\]

Then `Q_N>=0`, `E Q_N=(M_N/N^2) tau_(R_N)`, `E Y_N=0`, and the exact identity is

\[
 P_N[g]=Y_N+Q_N-\frac{M_N}{N^2}\tau_{R_N}. \tag{3.1}
\]

This retains the discarded inner mean with its correct coefficient `(N-1)/(2N)`. It is not legitimate to identify the full pair with its centered outer part on a no-close-pair event without this correction.

The canonical-pair variance is

\[
 \mathbb EY_N^2=\frac{N-1}{2N^3}V_{R_N}
       \le\frac{C_V}{2}u_N^2. \tag{3.2}
\]

For clarity, two different unordered canonical pair terms have covariance zero. Disjoint pairs are independent. For pairs sharing one label, condition on the shared Haar point; the remaining points are independent, and each canonical conditional mean is zero. Identical unordered pairs contribute `V_R`. This gives the exact coefficient `M_N/N^4=(N-1)/(2N^3)` and requires no joint independence of all pairs.

Taking absolute expectations in (3.1), using the nonnegative inner term and its known mean, gives

\[
 \begin{split}
 \mathbb E|P_N[g]|
 &\le\sqrt{\mathbb EY_N^2}
        +2\frac{M_N}{N^2}\tau_{R_N}\\
 &\le\left(\sqrt{C_V/2}+C_\tau\right)u_N.
 \end{split} \tag{3.3}
\]

This proves the required upper bound with

\[
 C=C_\tau+\sqrt{C_V/2}. \tag{3.4}
\]

The argument bounds the absolute inner contribution, not just a signed expectation. It does not assume independence between `Q_N` and `Y_N`.

## 4. Pair-count second moment without joint independence

Choose a constant `rho>0`, to be fixed explicitly in Section 5, satisfying `rho<=1` and `v_d rho^d<=1`. Define indicators and their sum

\[
 I_{ij}=\mathbf1_{\{\operatorname{dist}(X_i,X_j)<\rho R_N\}},
 \qquad L_N=\sum_{i<j}I_{ij},\qquad
 q_N=v_d\rho^d R_N^d=\frac{v_d\rho^d}{N^2}.
\]

Each indicator has mean `q_N`. For two distinct pairs, their indicators are pairwise independent: this is direct independence for disjoint labels; for one shared label, condition on that point and use that the Haar probability of its translated ball is the same constant `q_N`, while the two remaining points are independent. This establishes exactly the joint expectations needed for the second moment and nothing stronger.

Writing `ell_N=M_N q_N` for the expected count,

\[
 \mathbb E L_N=\ell_N,
 \qquad
 \mathbb E L_N^2=M_Nq_N+M_N(M_N-1)q_N^2
               =\ell_N+\ell_N^2-\ell_Nq_N.
 \tag{4.1}
\]

Cauchy–Schwarz applied to `L_N 1_(L_N>0)` gives

\[
 \mathbb P(L_N>0)
 \ge\frac{(\mathbb E L_N)^2}{\mathbb E L_N^2}
 \ge\frac{\ell_N}{1+\ell_N}. \tag{4.2}
\]

For every `N>=2`,

\[
 \frac{v_d\rho^d}{4}\le\ell_N
 =\frac{N-1}{2N}v_d\rho^d\le\frac{v_d\rho^d}{2}\le\frac12.
\]

In particular the convenient uniform lower bound

\[
 \mathbb P(L_N>0)\ge\frac{v_d\rho^d}{8} \tag{4.3}
\]

holds. This is a positive constant in N after rho is fixed. No extreme-value limit theorem is used.

Joint independence would be false. For an explicit continuous Haar example in dimension one, let a radius `r<1/4` be fixed. Conditioning on `X_1=0`, both `X_2` and `X_3` must lie in `(-r,r)` for their two close-pair events with label one. The third event cuts two triangles of total area `r^2` from the square of area `4r^2`. Therefore the probability that all three pairs are close is `3r^2`, whereas the product of the three marginal probabilities would be `(2r)^3`. Only the two-edge moments in (4.1) are needed.

## 5. Positive probability lower bound with explicit constants

On the event `L_N>0`, one pair lies inside `rho R_N`. By (2.1), its inner contribution is at least one half of `(rho R_N)^(-s)`, and every other inner contribution is nonnegative. Hence

\[
 Q_N\ge\frac12\rho^{-s}u_N
 \quad\hbox{on }\{L_N>0\}. \tag{5.1}
\]

The deterministic subtraction in (3.1) is bounded by

\[
 \frac{M_N}{N^2}\tau_{R_N}\le\frac{C_\tau}{2}u_N. \tag{5.2}
\]

For the bad outer event, the centered variance (3.2) and Chebyshev give

\[
 \mathbb P\left\{Y_N<-\frac18\rho^{-s}u_N\right\}
 \le32C_V\rho^{2s}. \tag{5.3}
\]

Now fix the following single constant, depending only on d and s:

\[
 \rho=\min\left\{
 \frac12,
 v_d^{-1/d},
 (4C_\tau)^{-1/s},
 \left(\frac{v_d}{512C_V}\right)^{1/(2s-d)}
 \right\}>0. \tag{5.4}
\]

It satisfies all earlier restrictions and also

\[
 \frac{C_\tau}{2}\le\frac18\rho^{-s},\qquad
 32C_V\rho^{2s}\le\frac{v_d\rho^d}{16}. \tag{5.5}
\]

Combining (3.1), (5.1), and (5.2), on the intersection of the close-pair event and the complement of the bad outer event,

\[
 P_N[g]\ge\left(\frac12-\frac18-\frac18\right)
                    \rho^{-s}u_N
          =\frac14\rho^{-s}u_N. \tag{5.6}
\]

No independence between those two events is assumed. Subtracting the unconditional bad-event probability from (4.3) is sufficient:

\[
 \mathbb P\left\{P_N[g]\ge\frac14\rho^{-s}u_N\right\}
 \ge\frac{v_d\rho^d}{8}-32C_V\rho^{2s}
 \ge\frac{v_d\rho^d}{16}. \tag{5.7}
\]

Thus (1.2) holds with the explicit choices

\[
 a=\frac14\rho^{-s},\qquad p=\frac{v_d\rho^d}{16},\qquad
 C=C_\tau+\sqrt{C_V/2},
\]

and N_0 from (2.4). The lower absolute first-moment estimate follows immediately by integrating over the event in (5.7). The exact zero mean would also give an additional factor two by equality of positive and negative first moments, but that strengthening is unnecessary for the stated claim.

The decisive strict exponent is visible: the close-pair event has lower probability of order `rho^d`, while the outer bad tail has upper bound of order `rho^(2s)`. The strict inequality `2s>d` allows a fixed sufficiently small rho to separate them. At equality this comparison does not provide the same separation. The proof makes no converse claim at the L2 integrability threshold.

## 6. Temperature equivalence and tightness

Let an arbitrary positive temperature sequence be given and define

\[
 b_N=\min(\beta_N,1),\qquad
 \sigma_N=\sqrt{Nb_N},\qquad
 B_N=b_N N^{4s/d-3},\qquad Z_N=\sigma_NP_N[g].
\]

The letter B_N here is merely the displayed deterministic scalar; it is not a generator operator or the campaign's microscopic coupling. The exact scaling identity is

\[
 \sigma_Nu_N=\sqrt{B_N}. \tag{6.1}
\]

Since `sigma_N>0` at every finite N, (1.2) gives, uniformly for `N>=N_0`,

\[
 \mathbb P\{Z_N\ge a\sqrt{B_N}\}\ge p,
 \qquad ap\sqrt{B_N}\le\mathbb E|Z_N|\le C\sqrt{B_N}. \tag{6.2}
\]

These bounds prove the claimed equivalence:

\[
 Z_N\to0\text{ in probability}
 \quad\Longleftrightarrow\quad B_N\to0
 \quad\Longleftrightarrow\quad Z_N\to0\text{ in }L^1. \tag{6.3}
\]

Indeed, `B_N->0` implies L1 convergence by the upper bound, and hence probability convergence by Markov. If `B_N` does not tend to zero, a subsequence satisfies `B_N>=delta>0`. Along it, the first bound in (6.2) gives probability at least p above `a sqrt(delta)`, and therefore at least p above the fixed smaller threshold `a sqrt(delta)/2`; probability convergence to zero fails. Finally, the lower first-moment bound directly excludes L1 convergence on the same subsequence. No general assertion that convergence in probability implies convergence in L1 is being used; the special lower bound establishes necessity here.

If `(B_N)` is bounded, the upper bound in (6.2) gives a uniform first absolute moment after the finite prefix. The prefix also has finite first moments because `g` is integrable. Markov therefore proves tightness of the entire sequence `(Z_N)`. If `(B_N)` is unbounded along a subsequence, pass to a further subsequence on which it tends to infinity. For every fixed K, eventually `a sqrt(B_N)>K`, and (6.2) yields

\[
 \mathbb P\{|Z_N|>K\}\ge p
\]

along that further subsequence. This violates tightness, taking an error tolerance less than p. It does not assert that all the mass escapes, or that `|Z_N|` tends to infinity in probability. Thus boundedness of the displayed deterministic scale is sufficient for tightness and its unboundedness is an obstruction, exactly as in the statement.

At the `sqrt(N)` scale, take `b_N=1`. Within `d/2<s<d`, the scalar is `B_N=N^(4s/d-3)`. Consequently:

- If `s<3d/4`, the scaled pair tends to zero in L1 and probability.
- If `s=3d/4`, the sequence is tight, has uniformly bounded first absolute moments, and has a fixed positive probability of exceeding a fixed positive threshold. It does not vanish in probability.
- If `s>3d/4`, the sequence is not tight.

These conclusions identify no distribution at the boundary or elsewhere. There is no claimed stable law, Gaussian limit, or full convergence in distribution at the boundary. Oscillating temperature sequences are covered by the deterministic criterion and subsequence arguments, without presuming a parameter limit.

## 7. Boundary, finite-N, and dependence checks

The principal theorem and its matching scale are restricted to `d/2<s<d`. The constant `C_V` in (2.2) displays why this proof does not silently include `2s=d`. The earlier permitted analytic bounds can nevertheless check the vanishing side there without reading any excluded theorem: at `s=d/2`, take `R_N=N^(-2/d)`, use `tau_R<=C R^(d/2)` and `V_R<=C(1+log(1/R))` in the exact decomposition (3.1). This yields

\[
 \mathbb E|P_N[g]|\le C N^{-1}(1+\sqrt{\log N}),
\]

so multiplication by `sqrt(N)` still gives a vanishing L1 upper bound. This is only an upper bound and is not claimed to be a sharp boundary asymptotic. When `2s<d`, the direct L2 identity from the permitted prerequisite gives the vanishing result at `sqrt(N)` scale. No THM-016 or THM-018 proof or card was read to obtain these consistency checks.

At `N=2`, `M_N=1`, the count second moment is exactly `q_N`, and the canonical outer variance is `V_R/16`. At `N=3`, the count second moment is `3q_N+6q_N^2`, and the canonical outer variance is `V_R/27`. The discarded mean coefficients are respectively one quarter and one third. The positivity-radius restriction in the lower-bound theorem is enforced by N_0; these coefficient identities themselves hold at every finite N. A positive temperature factor simply multiplies the statistic, its first moment, and its event threshold as in (6.1); it does not restore a finite untruncated second moment.

The supporting exact checker `VERIFICATION_CODE/round003_sharp_blind_exact.py` uses iid Haar measure on cyclic groups of sizes five and seven, at `N=2,3,4`. It enumerates 3,568 configurations and performs 28 exact rational checks of the two-edge count moments, the Cauchy–Schwarz count bound, the canonical pair coefficient, and failure of joint independence for triangle events. In these finite groups a close-neighbor event has probability `3/m`; the three-edge triangle probability is `7/m^2`, not `(3/m)^3`. This is an algebraic diagnostic of the dependence and normalization arguments, not a discretization proof or a replacement for the continuous Riesz estimates.

## 8. Outcome, limits, and sealed verification

All displayed assertions of the permitted THM-019 statement have been independently reconstructed under the declared initial Haar iid bare-kernel hypotheses. The lower bound is a probability estimate built from a local positive event and a controlled centered outer remainder. It is not inferred from failed second moments. The matching first-moment scale retains the discarded inner mean, and no step assumes joint independence of pair events or independence of the close and outer events.

The open boundary is distributional identification, not the vanishing criterion proved here. No endpoint law is obtained. For the campaign's actual target, the missing bridge remains identification and control of the actual backward corrector and the evolved law: the bare Riesz kernel in this report cannot be substituted for that corrector. The previously constructed internal-transport diagnostic is likewise a different kernel and does not enter this proof. The singular dynamic generator, cutoff comparison, cubic remainder, martingale controls, other initial law classes, and microscopic critical law remain separate obligations. No campaign regime or logarithmic normalization is changed.

Sealed source hashes:

- Task card: `41dc3eb83dad6cd759e9dc6ec59f4613cdffc8eb0efa5e04f124d3e2f92215f4`.
- THM-019 statement: `bfcc98dd9f0edeaa24a91d0348fd9932bc4bce3a23443b9901f2aaa35a7181a1`.
- Supplied task/card manifest: `bedfe6e83c8061f0beaf14201bb64022a36a74e8458a5857804d19987335aff8`.
- Permitted TASK-022 prerequisite: `9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4`.
- Frozen model: `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57`.

Executed checks were the supplied and supplemental input-manifest verifications; the prior TASK-025 output-seal verification; `python3 VERIFICATION_CODE/round003_sharp_blind_exact.py`, which passed all 28 checks and wrote its exact output; `git diff --check`; and scans of newly created text for control characters, trailing whitespace, terminal newlines and paired display delimiters. No unrelated broad test suite was run. The exact checker hash is `d9ae370f83bf4fc086a154cfd09db65fab419b80841fdd523626a45ca93c7bbd`; its output hash is `dd752ea3d9db81460f4f4aec39388a0a2dea1d1dfc59a6ce534dd384636a9838`.

Created outputs are this reconstruction, the supplemental input manifest, the checker and its output, and the adjacent `ROUND_003_SHARP_IID_RECONSTRUCTION_SHA256SUMS.txt`. The adjacent seal records final output hashes; the report does not embed its own hash. All earlier seals and candidate bytes are unchanged. No canonical edit, commit, push, remote operation, dependency installation, child agent, or TeX work occurred. Root alone compares this report with the unseen construction after sealing and decides any resulting status change.
