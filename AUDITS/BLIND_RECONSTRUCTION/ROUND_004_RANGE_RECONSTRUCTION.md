# ROUND 004 — statement-only blind reconstruction of THM-022

**Disposition: PASS — the assertion is true with exactly the fixed-data and every-small-positive-time quantifiers on the supplied card.** Two complete local proofs are given below. The second proof does not use the third-order Taylor constant in the first proof. No defect or unsupported line in the mathematical statement was found. The card's status-at-submission line and its references to other reports were not used as evidence.

- Task: `TASK-042_ROUND004_RANGE_BLIND.md`.
- Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r004-range-blind-20260917`.
- Branch: `codex/hocf-r004-range-blind`.
- Base: `52bda5d0d24067b051c6fe9763f2a78e7599e593`.
- Proof inputs: exactly the four files in `ROUND_004_RANGE_RECONSTRUCTION_INPUT_SHA256SUMS.txt`, copied from the root and independently hash-checked before reconstruction.
- Isolation: no constructor proof, erratum, hostile review, state ledger, memory, or unrelated repository file was read. No child agent, external source, dependency installation, root edit, commit, merge, or push was used. The task-specific blind-input restriction supersedes generic instructions to consult other project documents or update canonical ledgers in this lane.
- Evidence classification: complete analytic reconstruction, plus exact arithmetic self-checks. The arithmetic checks are neither a stochastic proof nor a further independent audit. This reconstruction is independent of the inaccessible constructor and hostile-review narratives.

## 1. Assertion, exact negation, and scope preflight

Fix an integer \(d\geq1\), \(0<s<d\) with \(s>d-2\), \(N\geq2\), \(\nu>0\), \(z_0\ne0\), and \(0<a<r_0=|z_0|<R<\infty\). Set
\[
 D=\{z:a<|z|<R\},\qquad
 L=2\nu\Delta+b\cdot\nabla,\qquad
 b(z)=\frac{2s}{N}|z|^{-s-2}z,\qquad
 j(z)=s|z|^{-s}.
\]
Let \(\rho\) be first exit from \(D\). Define
\[
 A(t)=\mathbb E_{z_0}\int_0^{t\wedge\rho}j(Z_h)\,dh,
 \qquad
 F(t,r)=\frac N4\left[
 \left(r^{s+2}+\frac{2s(s+2)}N t\right)^{2/(s+2)}-r^2\right].
\]
The assertion is that **for every fixed admissible tuple there exists a positive time \(t_0\) such that \(A(t)>F(t,r_0)\) for every \(0<t<t_0\)**. No common time over tuples is asserted.

Its exact logical negation is: there is one admissible tuple such that, for every \(\epsilon>0\), there exists \(t\in(0,\epsilon)\) with \(A(t)\leq F(t,r_0)\). Producing just one tuple/time with the strict inequality would negate a universal coefficient-one upper comparison, but would be weaker than the supplied assertion; the proofs below establish the full supplied assertion.

Normalization and law preflight:

1. A Brownian coefficient \(2\sqrt\nu\) has generator \(2\nu\Delta\). The frozen model's difference of two independent Brownian terms with coefficient \(\sqrt{2\nu}\) has precisely this covariance. For the principal kernel \(|z|^{-s}\), \(-\nabla |z|^{-s}=s|z|^{-s-2}z\), and the two opposite direct pair forces yield the displayed factor \(2s/N\). This checks the local algebra; it does not remove other forces from the interacting model.
2. The process in this proof starts at the deterministic point \(z_0\) in a finite **Euclidean annulus**. No iid, Gibbs, exchangeable, evolved, stationary, or interacting law is used. No centering operation is present.
3. The frozen periodic model is context, not an equality of full generators. Neither the periodic Fourier normalization nor an approximation to the singular interacting dynamics is used.
4. Every differentiated function is smooth on a neighborhood of the closed annulus. There is no evaluation at the singularity, collision integration by parts, singular Itô formula, or singular-limit passage.
5. No external literature is imported. The construction and estimates use smooth Itô calculus, elementary Brownian exponential martingales, ordinary differentiation, and explicit integral bounds.

## 2. Finite-annulus realization and a quantitative exit estimate

Choose a smooth radial cutoff equal to one on a neighborhood of \([a,R]\), vanishing near zero and outside a larger finite interval. Multiplying \(b\) by it, and defining the result to be zero near the origin, gives a smooth globally Lipschitz vector field \(\widetilde b\). Solve
\[
 Z_t=z_0+2\sqrt\nu\,W_t+\int_0^t\widetilde b(Z_h)\,dh.
\]
For completeness, for each continuous Brownian sample path the right-hand side defines a contraction on a sufficiently short interval in the supremum norm after subtracting the additive Brownian path. Picard iteration gives a unique continuous solution on that interval; concatenating equal-length intervals gives a global path. The iteration is adapted. Two extensions agree up to first exit by the same Lipschitz uniqueness argument on the closed annulus. Thus the stopped law is well defined without claiming a global realization of the singular drift. Continuity and \(z_0\in D\) give \(\rho>0\) almost surely. When \(d=1\), the annulus is disconnected; the same argument applies to the component containing \(z_0\).

Put
\[
 \delta=\min\{r_0-a,R-r_0\}>0,\qquad
 B=\frac{2s}{Na^{s+1}},\qquad
 T_B=\frac{\delta}{2B},\qquad
 c=\frac{\delta^2}{32\nu d}>0.
\]
On \(\{\rho\leq t\}\), the endpoint displacement is at least \(\delta\). Before exit the drift norm is at most \(B\). Hence, for \(0<t\leq T_B\),
\[
 \{\rho\leq t\}
 \subseteq
 \left\{\sup_{h\leq t}|W_h|\geq\frac{\delta}{4\sqrt\nu}\right\}.
\]
At least one coordinate then has absolute supremum at least \(\delta/(4\sqrt{\nu d})\). For a one-dimensional Brownian motion, applying the martingale \(\exp(qW_h-q^2h/2)\) at the first hitting time of a positive level, capped at \(t\), gives
\(\mathbb P(\sup_{h\leq t}W_h\geq u)\leq\exp(-u^2/(2t))\)
after minimizing in \(q>0\). The same estimate holds for \(-W\). A union bound therefore yields
\[
 p(t):=\mathbb P(\rho\leq t)
 \leq 2d\exp(-c/t),\qquad 0<t\leq T_B. \tag{2.1}
\]
In particular the killing error is smaller than every fixed power of \(t\). We will also use the explicit elementary estimate
\[
 e^{-c/t}\leq6t^3/c^3, \tag{2.2}
\]
which follows from \(e^x\geq x^3/6\).

## 3. First proof: killed Dynkin expansion with a finite remainder

For a smooth function \(f\) near \(\overline D\), write
\[
 K_hf=\mathbb E[f(Z_h)\mathbf1_{\{h<\rho\}}],\qquad
 Q_hf=\mathbb E[f(Z_\rho)\mathbf1_{\{\rho\leq h\}}].
\]
On the event \(\rho=\infty\), the latter integrand is defined to be zero. A smooth cutoff extension of \(f\) permits ordinary bounded stopped Itô calculus; the stopped martingale has zero expectation. The exact identity is
\[
 K_hf=f(z_0)+\int_0^h K_u(Lf)\,du-Q_hf. \tag{3.1}
\]
The last term is essential: dropping it would conflate a stopped process with a killed semigroup. Applying (3.1) to \(j\) and \(Lj\), and integrating in \(h\), gives the exact equality
\[
\begin{aligned}
 A(t)={}&j(z_0)t+\frac{Lj(z_0)}2t^2
 +\int_0^t\frac{(t-v)^2}{2}K_v(L^2j)\,dv\\
 &-\int_0^t(t-u)Q_u(Lj)\,du-\int_0^tQ_hj\,dh. \tag{3.2}
\end{aligned}
\]
All integrands are bounded on the closed annulus, so these expectation/integration interchanges are justified by boundedness and finite time.

Set \(\theta=s+2-d>0\). Direct radial differentiation gives
\[
 \Delta j=s^2\theta r^{-s-2},\qquad
 Lj=2\nu s^2\theta r^{-s-2}-\frac{2s^3}N r^{-2s-2}. \tag{3.3}
\]
To make every remainder constant explicit, define
\[
 U=2\nu s^2\theta,\qquad V=\frac{2s^3}N,\qquad
 J=sa^{-s},\qquad M_1=Ua^{-s-2}+Va^{-2s-2},
\]
and
\[
\begin{aligned}
 M_2={}&U\left[2\nu(s+2)(s+4-d)a^{-s-4}
       +\frac{2s(s+2)}N a^{-2s-4}\right]\\
 &+V\left[2\nu(2s+2)(2s+4-d)a^{-2s-4}
       +\frac{2s(2s+2)}N a^{-3s-4}\right].
\end{aligned} \tag{3.4}
\]
Every summand is positive under the stated range. The formula
\[
 L(r^{-q})=2\nu q(q+2-d)r^{-q-2}
              -\frac{2sq}N r^{-q-s-2}
\]
shows that \(J\), \(M_1\), and \(M_2\) bound respectively \(|j|\), \(|Lj|\), and \(|L^2j|\) on \(\overline D\). In particular, (3.2) implies
\[
 \left|A(t)-j(z_0)t-\frac{Lj(z_0)}2t^2\right|
 \leq\frac{M_2}6t^3+
       \left(\frac{M_1}2t^2+Jt\right)p(t). \tag{3.5}
\]
The boundary values of both \(j\) and \(Lj\) have been included. No boundary condition on either is assumed.

For the deterministic comparison function, ordinary differentiation yields
\[
\begin{aligned}
 F_t(t,r)&=s\left(r^{s+2}+\frac{2s(s+2)}N t\right)^{-s/(s+2)},\\
 F_{tt}(t,r)&=-\frac{2s^3}N
 \left(r^{s+2}+\frac{2s(s+2)}N t\right)^{-2(s+1)/(s+2)},\\
 F_{ttt}(t,r)&=\frac{8s^4(s+1)}{N^2}
 \left(r^{s+2}+\frac{2s(s+2)}N t\right)^{-(3s+4)/(s+2)}.
\end{aligned} \tag{3.6}
\]
Thus, with
\[
 H=\frac{8s^4(s+1)}{N^2}r_0^{-3s-4},
\]
Taylor's formula in integral form gives
\[
 F(t,r_0)=sr_0^{-s}t-\frac{s^3}N r_0^{-2s-2}t^2+R_F(t),
 \qquad 0\leq R_F(t)\leq\frac H6t^3. \tag{3.7}
\]
This is a bound on the actual third derivative over the entire interval, not only a formal Taylor coefficient.

Define the strictly positive quadratic coefficient and the finite cubic bound
\[
 \kappa=\nu s^2\theta r_0^{-s-2}>0,\qquad C=\frac{M_2+H}{6}>0.
\]
Subtracting (3.7) from (3.5) and using (2.1) proves
\[
 A(t)-F(t,r_0)
 \geq\kappa t^2-Ct^3
       -\left(\frac{M_1}2t^2+Jt\right)2d e^{-c/t},
 \qquad 0<t\leq T_B. \tag{3.8}
\]
For an explicit positive choice set
\[
 t_0=\min\left\{
 T_B,\ \frac{\kappa}{4C},\
 \left(\frac{\kappa c^3}{48dJ}\right)^{1/2},\
 \left(\frac{\kappa c^3}{24dM_1}\right)^{1/3}
 \right\}. \tag{3.9}
\]
All denominators are positive and finite. For every \(0<t\leq t_0\), (2.2) bounds each of the three subtracted terms in (3.8) by \(\kappa t^2/4\). Consequently
\[
 \boxed{\quad A(t)-F(t,r_0)\geq\frac\kappa4 t^2>0,
                  \qquad 0<t\leq t_0.\quad} \tag{3.10}
\]
This proves the required assertion, even at the chosen endpoint time. Every parameter is fixed before choosing \(t_0\); the time depends on those parameters and the annulus. No limiting exchange or uniform-in-data assertion occurs.

## 4. Independent sign/falsification route: the exact backward residual

This route tests the sign by the exact equation for \(F\), independently of the third derivative and the twice-iterated generator calculation. It also exposes the killing loss directly.

Let
\[
 p=s+2,\quad k=\frac{2sp}{N},\quad
 \alpha=\frac{s}{p},\quad \gamma=\frac{2(s+1)}p,\quad
 x=\frac{kq}{r^p}.
\]
Here \(q\geq0\) is remaining time, not a stopping time. Direct differentiation gives
\[
 F_q-b\cdot\nabla F=j,\qquad
 \Delta F(q,r)=\frac N2 G(x),
\]
where
\[
 G(x)=(s+d)(1+x)^{-\alpha}-s(1+x)^{-\gamma}-d,
\]
and its derivative factors exactly as
\[
 G'(x)=\frac{s}{p}(1+x)^{-\gamma-1}
           [\theta-(s+d)x]. \tag{4.1}
\]
Put
\[
 \eta=\frac{\theta}{2(s+d)}>0,\quad
 m=(1+\eta)^{-\gamma-1}>0,\quad
 K=\frac{s^2\theta}{2}mR^{-p}>0,\quad
 T_F=\frac{a^p\eta}{k}>0.
\]
For \(0\leq q\leq T_F\) and \(a\leq r\leq R\), one has \(0\leq x\leq\eta\),
\(G'(x)\geq s\theta m/(2p)\), and \(G(0)=0\). Therefore
\[
 \Delta F(q,r)\geq\frac{s^2\theta}{2}m q r^{-p}\geq Kq. \tag{4.2}
\]
Apply smooth Itô calculus to \(F(t-h,|Z_h|)\) up to \(t\wedge\rho\). Its drift is \(-j+2\nu\Delta F\), so the exact identity is
\[
 A(t)-F(t,r_0)
 =2\nu\,\mathbb E\int_0^{t\wedge\rho}
          \Delta F(t-h,|Z_h|)\,dh
   -\mathbb E\left[F(t-\rho,|Z_\rho|)\mathbf1_{\{\rho\leq t\}}\right].
 \tag{4.3}
\]
Because \(0\leq F(q,r)\leq j(r)q\), the last expectation is at most \(Jtp(t)\). On the event \(\rho>t\), the integral of \(t-h\) over \([0,t]\) is \(t^2/2\); on its complement it is nonnegative. Thus for \(0<t\leq T_F\),
\[
 A(t)-F(t,r_0)\geq\nu Kt^2(1-p(t))-Jtp(t). \tag{4.4}
\]
For complete quantitative closure choose
\[
 t_1=\min\left\{T_B,T_F,
          \left(\frac{c^3}{24d}\right)^{1/3},
          \left(\frac{\nu Kc^3}{48dJ}\right)^{1/2}\right\}>0.
\]
For every \(0<t\leq t_1\), (2.1)--(2.2) give \(p(t)\leq1/2\) and \(Jtp(t)\leq\nu Kt^2/4\). Hence (4.4) is at least \(\nu Kt^2/4>0\). This proves the full assertion a second time, with an explicit positive time and with no Taylor remainder.

The attempted sign falsification therefore fails in the stated range. It does uncover why an unrestricted-in-time extension of this particular Laplacian-sign argument is invalid: \(G(x)\to-d<0\) as \(x\to\infty\). No claim for all positive times is made here.

## 5. Exact checks and adversarial tests

The accompanying Python script uses only standard-library `Fraction` arithmetic. It represents rational-power radial functions as finite Laurent sums, differentiates them directly, and forms the radial Laplacian and drift separately. It compares those operations with (3.3), the expanded second generator, the binomial expansion of \(F\), and the independent factorization (4.1). No floating-point simulation is used.

The script verifies the expanded identity
\[
\begin{aligned}
 L^2j={}&4\nu^2s^2\theta(s+2)(s+4-d)r^{-s-4}\\
 &-\frac{4\nu s^3}N
   [\theta(s+2)+(2s+2)(2s+4-d)]r^{-2s-4}\\
 &+\frac{8s^4(s+1)}{N^2}r^{-3s-4}.
\end{aligned}
\]
Results:

- **81 admissible exact rows passed:** nine choices spanning dimensions 1, 2, 3, 4, 5, and 8, including nonintegral exponents, crossed with \(N=2,3,11\) and \(\nu=1/4,1,7/3\). The exact quadratic coefficient at \(r_0=1\) is positive in every row.
- **Five excluded diagnostic rows passed:** two exponents below \(d-2\) have negative quadratic coefficient; two positive-power endpoint rows have zero quadratic coefficient and negative cubic coefficient; and a zero-diffusion row agrees with the deterministic \(F\) expansion through order eight.
- At \(s=d-2>0\), the computed cubic difference is exactly \(-4\nu s^3(s+1)(s+2)/(3N)\) at \(r_0=1\). This is an algebraic endpoint diagnostic, not an added theorem in this report.
- At \(\nu=0\), the radial ODE \(\dot r=2s r^{-s-1}/N\) solves \(r(t)^{s+2}=r_0^{s+2}+2s(s+2)t/N\), and its source integral is exactly \(F\) before exit. Thus a strict result could not omit the positive-diffusion hypothesis.
- **One exact finite-annulus constant check passed:** \(d=3,s=2,N=2,\nu=1,a=1/2,r_0=1,R=2\). The constants are \(B=16,c=1/384,J=8,M_1=640,M_2=249856,H=96,C=124976/3,\kappa=4\). The rational time \(1/131072\) satisfies all four inequalities in (3.9), giving the lower bound \(A(t)-F(t,1)\geq t^2\) for every positive time at most that value.
- The `d=1` disconnected-annulus case, both inner and outer boundary exits, arbitrary fixed direction of \(z_0\), arbitrarily small positive \(\nu\), \(s\) arbitrarily close to \(d-2\) from above, and arbitrarily thin but fixed annuli were also checked analytically. The time is permitted to degenerate in each limiting family; the theorem claims no uniformity.

**Failed tests: none.** The negative and zero controls were expected outcomes outside the hypotheses, not failed tests. No constructor error was inferred from the card's historical status narrative. The reconstruction uses the exact third derivative (3.6) and a second proof that avoids that derivative entirely.

Verification command:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RANGE_EXACT_CHECKS.py > AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RANGE_EXACT_CHECKS.json
```

Outcome: exit code 0; all 81 admissible rows, five excluded diagnostics, and the exact annulus-constant check pass. Input and output hashes are separately recorded. No TeX was edited or compiled; the assigned artifact is this Markdown audit report.

## 6. Disposition, exclusions, and handoff

The first unsupported line requested in the event of falsity does not exist in this reconstruction: the precise assertion is proved in (3.10) and independently by (4.4) with the explicit time \(t_1\). The statement's strict inequality, fixed finite-annulus realization, all-small-positive-time quantifier, parameter dependence, killed boundary loss, and finite-time remainder are all retained.

A universal coefficient-one upper comparison covering this stopped process is therefore false in the specified range. If some global realization exists and agrees in stopped law through \(\rho\), and its subsequent source is nonnegative, its total expected source up to \(t\) is at least the stopped expectation; this is only a conditional transfer of the obstruction. Neither global singular existence nor equality of the relevant global stopped laws is established here.

There is no conclusion about a different majorant, a full pair inverse, evolved interacting-law estimates, Gibbs/iid law bridges, a critical fluctuation theorem, a singular interacting limit, a logarithmic normalization, or the campaign's main mission. No root ledger or theorem card was changed; only the task-prescribed input copies and assigned audit deliverables were written in this worktree. Root may compare this sealed report with the inaccessible constructor and hostile-review outputs and record the resulting gate decision.

Deliverables in `AUDITS/BLIND_RECONSTRUCTION/`:

1. `ROUND_004_RANGE_RECONSTRUCTION.md` — this complete analytic reconstruction.
2. `ROUND_004_RANGE_EXACT_CHECKS.py` — reproducible exact arithmetic checks.
3. `ROUND_004_RANGE_EXACT_CHECKS.json` — exact results, including explicit failed-test list.
4. `ROUND_004_RANGE_RECONSTRUCTION_INPUT_SHA256SUMS.txt` — the four locked input hashes.
5. `ROUND_004_RANGE_RECONSTRUCTION_OUTPUT_SHA256SUMS.txt` — hashes of deliverables 1--4; as usual the manifest excludes itself.

After output sealing, these deliverables must be treated as immutable. Any later correction requires a new superseding report rather than an edit of this report.

Sealed UTC: 2026-09-17 23:21:42 UTC.
