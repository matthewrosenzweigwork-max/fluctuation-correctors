# Round 001 independent analytic review

- Task: `TASK-009`; reviewed candidate: `THM-008`, bounded analytic part of `PO-001a`.
- Issued: 2026-09-17T18:41:59.021881+00:00.
- Reviewer role: fresh independent analytic auditor, assigned Astra Max; constructor conversation was not available to this reviewer.
- Baseline commit: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Audit worktree: `/private/tmp/hocf-round001-analytic-audit-20260917`.
- Candidate: `MEMORANDA/ROUND_001_SMOOTH.md`, SHA-256 `934538be3fdb83d5949d5059abb65d9834064539a4d3006d2ca99a528089eb1f`.
- Issuance rule: this report and its sealed reconstruction are immutable after issuance. A later change requires a new report, not alteration of this verdict.

## 1. Verdicts and exact scope

**Statement-only reconstruction verdict: `ISOLATED_RECONSTRUCTION_PASS`.** From the frozen model and memorandum Section 1 alone, the reviewer reconstructed the response estimate, transport commutator, construction of the mild solution, symmetry argument, source norm and the exact bound (1.4), with the constants (1.1). The reconstruction was saved before the candidate proof was opened, as `AUDITS/HOSTILE/ROUND_001_ANALYTIC_RECONSTRUCTION.md`, SHA-256 `d73f1a4c00d982c6bfef77b9d31f22d344659d7a07606f8ebefc043f5e9f2b30`.

**Hostile proof-review verdict: `HOSTILE_REVIEW_PASS`, restricted to the fixed-smooth analytic statement (1.1)–(1.4), its forcing estimate (1.6)–(1.7), both supplied analytic mechanisms, the Fourier diagnostics in Section 5, and the explicit Fourier-sequence cutoff diagnostics (7.1)–(7.5).** No mathematical defect was found in that scope. The solution exists and is unique in the stated mild class for every integer N at least two and every nonnegative diffusion coefficient. The constants are independent of these parameters only through the explicitly stated actual coefficient, background and forcing norms.

These are two phases of **one fresh reviewer**, independent of the constructor, not two separately staffed analytic audits. Isolation was **statement-only**: Section 1 disclosed the proposed constants and conclusion. The reconstruction was not performed without knowledge of those constants. The candidate's own two proof mechanisms remain constructor work; their number does not establish audit independence.

The verdict does not certify a singular fluctuation theorem, a singular corrector, removal of the cutoff, a critical limiting law, closure of the hierarchy, or a probabilistic estimate for the actual evolved particle law. The finite-particle algebra imported in (6.1)–(6.3) is not independently recertified by this analytic audit. The primary-source identification of the Fourier constant with the specified torus Riesz normalization remains outside this review.

## 2. Dossier, isolation and input integrity

Before reconstruction the mathematical input was limited to `TASKS/ACTIVE/ROUND_001_MODEL.md` and the candidate memorandum up to, but not including, its Section 2. The task card and repository instructions were also read. The pre-proof extraction used `awk '/^## 2\./{exit} {print}' MEMORANDA/ROUND_001_SMOOTH.md`, which stopped at the Section 2 heading. No other constructor output, other worktree, source-note proof, or constructor conversation was consulted. The reconstruction was written and hashed before the first call reading the proof sections. After sealing it, the complete candidate memorandum and its verification program were read.

The generic campaign reading sequence was kept separate from the explicitly restricted mathematical audit dossier. `MASTER_PROMPT.md` and `CAMPAIGN_PROTOCOLS.md` were read after the reconstruction was sealed; the imported note was not used as a mathematical input. `STATE/STATUS_VOCABULARY.md` was read solely for verdict vocabulary. No canonical ledger was edited.

The input manifest has SHA-256 `48b467b2bc1522919cdab364bc9552da8e2bb82873b931ae7570f62fb36e47cb` and contains:

| Input | SHA-256 |
|---|---|
| `TASKS/ACTIVE/ROUND_001_MODEL.md` | `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57` |
| `TASKS/ACTIVE/TASK-009_ANALYTIC_AUDIT.md` | `dee245dcd2bb7a58b42cf80c102e5a77788119c85e553ebac8813fa571e92e18` |
| `MEMORANDA/ROUND_001_SMOOTH.md` | `934538be3fdb83d5949d5059abb65d9834064539a4d3006d2ca99a528089eb1f` |
| `VERIFICATION_CODE/check_round001_smooth_fourier.py` | `8b9edbee049db20d70e250ea333d069d66cd201f54c4c8c803c4875fb1c29ffc` |

`shasum -a 256 -c AUDITS/HOSTILE/ROUND_001_ANALYTIC_INPUT_SHA256SUMS.txt` passed both before reconstruction and after proof review. There were no tracked modifications on arrival. The manifest, model, task card, candidate memorandum and supplied verification program were already untracked audit inputs. Their bytes have not been changed.

## 3. Response derivatives and exact coefficient bounds

The decisive response calculation is correct at `MEMORANDA/ROUND_001_SMOOTH.md:126`–`159`, equations (2.1)–(2.3). For a derivative with no x derivative on the x-response, integration by parts in the integrated variable moves the otherwise excessive derivative from the unknown onto K and mu. Its bound is

\[
 (d\kappa_1+\kappa_0M_1)\|\Phi\|_{C^m}.
\]

If at least one x derivative is present, it falls on K(z-x). In that case the remaining derivative count on the unknown is at most m, and the original, unintegrated expression is bounded by d kappa_m times its C^m norm. This covers pure and mixed pair derivatives, including the case of m derivatives entirely in the passive variable. The analogous y-response gives exactly

\[
 \|(R_x+R_y)\Phi\|_{C^m}
 \le 2(d\kappa_m+\kappa_0M_1)\|\Phi\|_{C^m}.
\]

No hidden derivative of mu beyond its displayed W^{1,1} seminorm appears. No hidden C^{m+1} norm of K or Phi is needed for this estimate. Positivity and mass one of mu are used when bounding the original integrals and the drift convolution. A positive lower bound for mu is not used.

The principal pair drift has components u(x)+K(x-y)/N and u(y)-K(x-y)/N. Componentwise derivatives of order at most m are bounded by

\[
 b_m+(1+N^{-1})\kappa_m\le b_m+\tfrac32\kappa_m=A_m.
\]

The pair norm counts total derivative order in 2d coordinates. Mixed derivatives of K(x-y) produce one signed derivative of K, not a new dimension-dependent factor. This verifies (2.5). Keeping B/N in that principal drift is essential: it is not bounded on C^m as a separate perturbation.

## 4. Flow construction, every flow constant, and the Volterra series

The construction in Section 3 is valid. Subtracting the additive Brownian path leaves an ordinary integral equation with globally Lipschitz spatial drift on a periodic lift. Short-interval Picard construction, concatenation, and the bounded periodic drift give a pathwise solution on the finite horizon. This also covers zero diffusion. Spatial difference quotients satisfy the variational integral equations, with deterministic bounds independent of the Brownian path and of the diffusion coefficient. Thus differentiation under the expectation requires no estimate that deteriorates as diffusion vanishes or grows.

The exact constants at lines 214–246 were checked as follows. Let n=2d and use Euclidean multilinear operator norms. A vector field with componentwise r-th partial derivatives bounded by A_m has

\[
 \|D^r a\|_{\rm op}\le n^{(r+1)/2}A_m
 \le n^{(m+1)/2}A_m=\ell_m,\qquad 1\le r\le m.
\]

For r at least two, the one-block term in the partition chain rule is the linear variational term. Every other block has size less than r. Writing H for the integrated ell_m, induction gives

\[
 \|D^r Z\|_{\rm op}
 \le e^H\int_0^H e^{(r-1)v}\,dv
       \sum_{\substack{\pi\in\Pi_r\\|\pi|\ge2}}
                 \prod_{D\in\pi}c^*_{|D|}
 =c_r^*(e^{rH}-e^H)\le c_r^*e^{rH}.
\]

The initial higher variations are zero. The first variation starts at the identity and has bound e^H. This verifies (3.3)–(3.4), also when A_m=0 by continuity or direct inspection.

For the composed scalar h(Z), its derivative of order r is a sum over all partitions. The component-to-operator comparison gives a factor no larger than n^{r/2}; the sum of the products of the c-values is

\[
 \sum_{\pi\in\Pi_r}\prod_{D\in\pi}c^*_{|D|}
 =c_r^*+(r-1)c_r^*=r c_r^*.
\]

Consequently the stated constants

\[
 C_{n,m}=n^{m/2}W_m,\qquad q_{n,m}=m n^{(m+1)/2}
\]

are sufficient for (3.5). As an additional check, the recursion actually gives c_r^*=(r-1)!: a partition weighted by the product of (block size minus one) factorials enumerates permutations by their cycle partition, so the full sum is r!. This identity is an audit check of the existing constants, not an amendment to the candidate. Exact independent enumeration through order eight also agreed.

Strong continuity on C^m follows first on smooth functions from the flow and its variations and then on C^m by smooth approximation and (3.5). The backward equation follows from the Markov composition property and the short-time Itô expansion: the derivative with respect to the initial time is minus the local generator applied to P_{t,s}h. In particular, differentiating the Duhamel integral gives minus F_t minus R_t Phi_t minus G_t Phi_t, which verifies the sign in (3.6).

For k response insertions at ordered times between t and the forcing time s, the propagation factors contribute C_{n,m}^{k+1}, and their exponentials combine to exp(q_{n,m}A_m(s-t)). The ordered response integral is

\[
 \frac1{k!}\left(\int_t^s R_m(r)dr\right)^k.
\]

Summing gives precisely (3.7), including the single leading C_{n,m} and the coefficient C_{n,m} multiplying R_m inside the exponent. The same factorial estimate on the difference of two mild solutions yields uniqueness. Repeating the construction in each higher finite spatial norm and using uniqueness identifies a single spatially smooth solution. Continuous forcing and coefficients give the stated classical time equation in lower spatial norms.

Section 3 supplies its own uniform estimate (3.7), which is weaker than (1.4). Section 4 supplies the sharper exact constant in (1.4), using the existence result of Section 3. The candidate states this relationship accurately; these are not two independent constructions of existence with the same optimal numerical constants.

## 5. Differentiated maximum principle, time orientation and symmetry

The commutator at lines 286–301 is correct, and each derivative of the unknown on its right has order at most m. The sum of binomial coefficients other than the zero term is 2^{|gamma|}-1, and there are 2d drift components. The resulting bound is exactly

\[
 2d(2^m-1)A_m\|\Psi\|_{C^m}.
\]

There is no diffusion commutator. After tau=T-t, the diffusion has the forward nonnegative sign. At a positive or negative extremum of any differentiated component the drift vanishes and the diffusion is nonpositive. Compactness and the finite derivative index set justify the upper Dini derivative bound for the maximum of these sup norms. This is valid for every nonnegative diffusion coefficient, including zero, without ellipticity, smoothing, or a factor reciprocal to diffusion.

The response estimate from Section 3 of this audit yields (4.4). Scalar integrating-factor comparison followed by the time reversal gives exactly

\[
 \|\Phi_t\|_{C^m}
 \le\int_t^T
   \exp\left(\int_t^s c_m(r)dr\right)\|F_s\|_{C^m}ds.
\]

The exponent runs from t to the forcing time s. It is not reversed and does not run from s to T. The source has the correct positive sign in forward reversed time. Smoothness at every finite spatial order, established before this argument, justifies the differentiated equation and the terminal derivative later used in the cutoff test.

Swapping x and y commutes with the local pair drift because K is odd, and exchanges the response operators. Uniqueness then proves symmetry for symmetric forcing. The source J_f is symmetric, vanishes on the coordinate diagonal, and its norm estimate (1.6) follows from d component terms, a factor at most two for the gradient difference, and the 2^m Leibniz coefficient sum. Inserting it in (1.4) gives (1.7). Parameters can still enter through the background and one-body test norms; the candidate explicitly retains this dependence.

## 6. Independent falsification and exact Fourier checks

The following checks were recomputed directly, without treating the program's output as a proof.

1. **Zero interaction and constant modes.** The heat eigenvalue is 4 pi squared times diffusion times the sum of squared pair frequencies. Its integrated exponential multiplier is bounded by the remaining time for every nonnegative diffusion coefficient, with the continuous zero-eigenvalue limit equal to that time. This confirms the terminal sign, zero-diffusion case and constant forcing.
2. **Signed response and potential instability.** For uniform background the x-response multiplier is minus 4 pi squared times the squared x frequency times the corresponding Fourier coefficient of g. The minus sign comes from multiplying the coefficient of K at minus that frequency by the derivative coefficient. For the symmetric sum mode in (5.4), the internal transport vanishes and the complete eigenvalue is exactly the displayed one. Negative amplitude with zero diffusion produces exponential growth. This invalidates a contraction argument for the response but is compatible with the proved exponential estimate.
3. **Nonzero internal transport.** For the difference cosine H_n in one dimension, direct multiplication of the two sine factors gives

\[
 BH_n=4\pi^2 a n(H_{n+1}-H_{n-1}).
\]

Together with the response and diffusion eigenvalues this verifies (5.5) and all signs and finite-N coefficients in (5.6), including N=2 and N=3.
4. **High-frequency derivative loss.** The normalized difference cosine in (5.7) has C^m norm one. Its differentiated output Fourier coefficient at (n+1,-n-1) has exactly the stated magnitude. The coefficient diverges with n for every nonzero amplitude. Since each Fourier coefficient is bounded by the supremum norm on the mass-one torus, this proves unboundedness of B/N on C^m for every fixed finite N. The candidate avoids this invalid perturbation route by including B/N in the principal drift.

The supplied program was inspected and run with

```text
python3 VERIFICATION_CODE/check_round001_smooth_fourier.py
```

It returned:

```text
PASS: 120 exact rational Fourier identities; N=2,3,17; nu=0,1/3,1,7.
PASS: heat mode, full symmetric sum mode, and forced difference-mode solution.
Status: REPRODUCED / SELF_CHECKED; no floating-point tolerance and no random seed.
```

The code uses exact standard-library fractions and includes negative, zero and positive kernel amplitudes. The reviewer checked its Fourier multiplication formula directly against the operator definitions. The computation is independently **reproduced**, while its finite test set is not a substitute for the analytic proof and is not a certificate of a singular theorem.

## 7. Cutoff diagnostic and its exact logical strength

This part is conditional only on the explicit positive Fourier sequence (7.1), which is fully specified and therefore needs no source identification to test. The equivalence of that sequence to the campaign's intended Riesz normalization is not asserted by this audit.

The absolute Fourier upper bound (7.2) has the correct exponent. A derivative of order j of K contributes j+1 powers of frequency. Annular counting gives the power s+j+1 after including dimension, and heat scaling gives epsilon to minus one half of that power. Since epsilon is at most one, taking the maximum over j up to m gives the stated bound.

At zero, every Fourier term of minus the Laplacian of g has the same positive sign. Thus (7.3) has the correct sign and power. Restricting the sum to frequencies between epsilon^{-1/2} and twice that radius gives at least a constant times epsilon^{-d/2} points, each with comparable positive magnitude. This proves the lower bound as well as the upper bound. Hence the divergence is real, not merely the growth of an upper estimate.

Sign changes of individual lattice coordinates force the off-diagonal entries of DK_epsilon(0) to vanish; coordinate permutations make all diagonal entries equal. This verifies (7.4). For the homogeneous example take b=0 and mu=1, so the background is an admissible solution for every diffusion coefficient. For the fixed terminal test f_T(x)=cos(2 pi x_1), in the local difference coordinate r,

\[
 K_\varepsilon(r)=a_\varepsilon r+O(|r|^3),\qquad
 \nabla f_T(r/2)-\nabla f_T(-r/2)
 =-4\pi^2r_1e_1+O(|r|^3).
\]

Their product has second r_1 derivative minus 8 pi squared times a_epsilon at zero, which is (7.5). In the exact componentwise pair norm,

\[
 \partial_{r_1}^2
 =\tfrac14\partial_{x_1}^2-\tfrac12\partial_{x_1}\partial_{y_1}
                      +\tfrac14\partial_{y_1}^2,
 \qquad
 \|J_{f_T,\varepsilon}\|_{C^2}\ge8\pi^2a_\varepsilon.
\]

The sum of the absolute derivative coefficients is one, so no unrecorded norm-comparison factor is needed. This diverges at least at the stated rate with a fixed terminal test and a uniform homogeneous background.

For each fixed cutoff, the smooth solution has terminal derivative in C^2 equal to the terminal source after reversal of time. Therefore a single cutoff-independent constant bounding its C^2 norm by that constant times the remaining time, for all sufficiently small remaining times, would bound the divergent terminal forcing norms. That contradiction is valid even if the permitted small-time interval were allowed to depend on the cutoff.

The diagnostic blocks the particular uniform derivative/forcing estimate used here. It does not prove divergence of the solution at every fixed positive time, failure of weaker norms, failure of estimates exploiting positive diffusion, or impossibility of a different singular corrector. Section 7 correctly limits its conclusion.

## 8. Defects, remaining obligations and source status

**Defects ordered by severity: none found in the reviewed analytic scope.** No candidate repair was made or incorporated into this verdict. The recomputations above make the supplied proof's constants and standard elementary construction steps explicit; they do not replace a failed argument or change an assumption.

The following boundaries remain material and unchanged:

- The analytic estimate assumes the displayed actual background and forcing norms; it does not prove uniform bounds for parameter-dependent mean-field densities or one-body tests.
- The direct elementary bounds in (6.5) are correct: the symmetrized cubic kernel has the indicated supremum bound and the eight terms defining U_3 each have mass at most one. They supply no decay of the cubic statistic at fluctuation scale.
- The imported exact identities (6.1)–(6.3), martingale formulas and their algebraic provenance require their assigned algebra audit. This report does not assign them an additional independent pass.
- The first probabilistic gap stated in (6.4), or a justified replacement retaining a nonvanishing cubic contribution, remains open. No law-class transfer is permitted by this analytic result.
- The singular normalization source audit, singular limit, diagonal contractions and any critical all-order control remain separate obligations.

No imported literature theorem is used to pass the smooth estimate: the ODE construction, smooth Itô expansion, differentiation, integration by parts, scalar comparison and finite Fourier calculations were checked directly. No primary literature claim has been promoted by inference from the smooth proof. The logarithmic normalization is untouched.

## 9. Reproducibility and changed files

Environment: macOS Darwin 25.6.0 arm64; Python 3.9.6. No package was installed or upgraded. No branch, commit, remote or canonical state was changed. The source files and candidate proof remained byte-for-byte unchanged.

Commands and results:

| Check | Result |
|---|---|
| `git rev-parse HEAD` | Baseline commit shown above |
| `shasum -a 256 -c AUDITS/HOSTILE/ROUND_001_ANALYTIC_INPUT_SHA256SUMS.txt` | All four frozen inputs passed before and after review |
| `python3 scripts/verify_campaign.py` | `CAMPAIGN VERIFICATION PASSED`; imported-note hash matched the frozen baseline |
| `python3 VERIFICATION_CODE/check_round001_smooth_fourier.py` | 120 exact rational identities passed |
| Independent exact partition enumeration through order eight | Passed; reproduction code below |
| `git diff --check` | Passed; no tracked modifications |

Files created by this auditor are the sealed reconstruction, this review, and the output SHA-256 manifest. The reconstruction was not edited after the proof was opened. Mathematical content is in these assigned Markdown audit artifacts; no TeX source was created or changed.

The output manifest is `AUDITS/HOSTILE/ROUND_001_ANALYTIC_OUTPUT_SHA256SUMS.txt`. It seals the report and reconstruction. The report's own hash is recorded there and in the handoff, rather than self-referentially inside this file.

### Exact partition check reproduction

The following standard-library program is the complete additional computation. It has no random input and no tolerance; its output is an auxiliary finite check, while the permutation-cycle argument in Section 4 proves the identity for all orders.

```python
from fractions import Fraction
from math import factorial

def partitions(values):
    if not values:
        yield ()
        return
    head, *tail = values
    for rest in partitions(tail):
        yield ((head,),) + rest
        for j in range(len(rest)):
            yield rest[:j] + ((head,) + rest[j],) + rest[j + 1:]

c = {1: Fraction(1)}
for r in range(2, 9):
    total = Fraction(0)
    for part in partitions(list(range(r))):
        if len(part) < 2:
            continue
        prod = Fraction(1)
        for block in part:
            prod *= c[len(block)]
        total += prod
    c[r] = total / (r - 1)
    assert c[r] == factorial(r - 1)
    all_parts = Fraction(0)
    for part in partitions(list(range(r))):
        prod = Fraction(1)
        for block in part:
            prod *= c[len(block)]
        all_parts += prod
    assert all_parts == r * c[r]
print('PASS: independent set-partition recursion through order 8; '
      'c_r=(r-1)! and partition sum=r*c_r.')
```
