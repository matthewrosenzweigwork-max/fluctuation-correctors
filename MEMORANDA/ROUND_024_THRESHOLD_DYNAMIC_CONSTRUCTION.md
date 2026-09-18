# Round 024 — an actual critical Coulomb reduction with the lower drift removed

TASK-102. Issued 2026-09-18 UTC. Ordinary construction in the isolated worktree
`hocf-r024-threshold-construction`, base
`4ab1d492c3bb9bb3537732f2d75502971f5ee6da`.

**SELF_CHECKED EXACT REDUCTION; THM-046 / PO-033 REMAINS OPEN.**
No admitted actual-law counterexample is produced. No independent audit or
theorem promotion is assigned by this worker.

The new analytic step is a Coulomb flux identity for the lower contraction of
the genuine full pair inverse. Common-translation derivatives, rather than an
absolute force-times-gradient estimate, give a uniform smooth-test bound on
that contraction after division by the square root of the particle number.
The actual expected-energy inequality then makes the entire scaled lower
drift tend to zero. Its scalar contraction is exactly zero. The argument stays
at four-dimensional Coulomb; it does not extend the strict sub-Coulomb R12/R14
occupation theorem by substitution.

Together with the established iid endpoint estimate and a directly checked
heat-smoothing estimate, this reduces the frozen assertion to the single
dynamic estimate (7.5): the actual integrated cubic term plus the martingale
from the unsmoothed part of this same inverse. These two terms are retained
together. Their smallness is not proved, and neither is discarded by taking
its signed expectation.

## 1. Frozen assertion, negation, and exact scope

Haar measure on the unit torus has mass one, with characters
\(e^{2\pi i k\cdot x}\). Fix \(d=4,s=2\),
\(\widehat g(0)=0\), \(\widehat g(k)=|k|^{-2}\) for \(k\ne0\),
and \(K=-\nabla g\). The actual noncolliding gradient particles are

\[
dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)dt+\sqrt{2\nu_N}\,dW_i,
\qquad X_i(0)\text{ iid Haar, independent of the Brownian drivers}.
\tag{1.1}
\]

Here \(\beta_N>0\), \(\nu_N=\beta_N^{-1}\), and
\(\lambda_N=\beta_NN^{-1/2}\to\lambda\in(0,\infty)\).
Set \(b_N=\min(\beta_N,1)\), \(\sigma_N=\sqrt{Nb_N}\).
For all sufficiently large \(N\), \(b_N=1\) and
\(\nu_N=N^{-1/2}/\lambda_N\); all estimates used below are uniform on a
fixed bounded interval of diffusivities and for eventual fixed lower and
upper bounds on \(\lambda_N\). Discarding finitely many indices changes no
limit.

Fix the original finite \(T\ge0\) and smooth real terminal test \(h\).
Write \(c=4\pi^2\) and \(f_t=Q_{T-t}^{\nu_N}h\), where the nonzero-mode
multiplier of \(Q_a^\nu\) is \(e^{-a(c+c\nu|k|^2)}\) and constants are
preserved. Set

\[
J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)),\quad x\ne y,
\]
\[
P_N[v]=\frac1{2N^2}\sum_{i\ne j}v(X_i,X_j)
       -\frac1N\sum_i\int v(X_i,y)dy+\frac12\iint v(x,y)dxdy.
\tag{1.2}
\]

The entire frozen target, with the absolute value after time integration, is

\[
\sigma_N\,\mathbb E\left|\int_0^T P_N[J_t](X(t))dt\right|\longrightarrow0.
\tag{1.3}
\]

Its negation is an admitted fixed \(T,h,\lambda>0\) and critical sequence
for which this nonnegative expression has positive limsup. A static law,
an altered preparation, an \(N\)-dependent terminal test or time horizon,
or a nondecaying upper bound does not negate (1.3).

Every tuple below is ordered with distinct particle labels and denominator
\(N^k\). Neither normalization nor centering is changed. Constants in the
new estimates depend only on the fixed kernel, horizon, indicated finite
seminorms of the same \(h\), a bounded diffusivity interval, and eventual
critical-sequence bounds. They do not depend on \(N\), a smoothing parameter,
or a collision cutoff unless explicitly marked as fixed-\(N\) domain constants.

## 2. Dossier, normalization, and domain preflight

All twenty input byte strings in the assigned manifest were SHA-256 verified
before mathematical use. The task, AGENTS, orchestration instructions, and
manifest were first read to establish the restriction; the substantive
mathematical files were read after this verification. The report uses no
external literature claim or unverified citation. Exact exposure, including
partial and truncated reads and files only hashed/copied, is recorded in the
artifact directory. Current state, history, memory files, other worktrees,
and R23 proofs/audits were not opened.

| Permitted source | Content used and its boundary |
|---|---|
| Frozen model and THM-046 | Actual preparation, coefficients, target, and exact negation. The theorem card is not evidence of proof. |
| R4, local heat/divergence calculation; R16, Sections 2–3 | Coefficient-one Coulomb singularity, the full divergence measure, actual realization and expected-energy sign. The needed estimates are restated below. |
| R5 periodic pair memorandum, Sections 2–9 | Actual auxiliary pair evolution, absolute source barrier, sup bound, Haar L2 bound, and Haar measure inequality. No unspecified uniform regularity constant is imported. |
| R5 conditional inverse/interface and both allowed clarifications | The bounded Borel Volterra inverse with both responses; the actual backward test; the distinction between exchange symmetry and Haar self-adjointness. |
| R8, complete domain proof, especially Sections 8–11 | At each finite N: classical off-diagonal inverse, genuine background slices, absolute integrability of the internal contraction and cubic, global Haar H1, and the true square-integrable finite-particle martingale. Its density constant is used only for this fixed-N domain statement. |
| R16, Sections 3–7; R10, Sections 3, 5–7 | Actual expected-energy sign, positive Fourier controls, inverse L1 bound, and the smooth-noise mechanism. Sections 3 and 6 below give the precise arguments and constants needed here. |
| R1, Sections 1–3; R8, Section 10 | Literal deleted-label algebra. Section 5 and the fresh checker recompute its signs and coefficients. |
| R12 and R14 | Boundary nondependencies only: their strict sub-Coulomb occupation/product arguments do not establish the Coulomb estimate. |

The status labels printed in older sources are historical issuance labels.
This worker does not infer current independent certification from them or
reassign their campaign status. The new result is a self-checked implication
from the precise full-proof dossier modules in the table, not a fresh blind
certification of those modules.

For normalization, the positive heat representation specializes to

\[
g(z)=4\pi^2\int_0^\infty(p_u(z)-1)du,
\qquad \widehat p_u(k)=e^{-4\pi^2u|k|^2}.
\tag{2.1}
\]

Its nonzero coefficient is exactly \(|k|^{-2}\). The central Euclidean
Gaussian integral is \(|z|^{-2}\), and the remaining local lattice terms
are smooth and even. Hence in a fixed embedded ball

\[
g(z)=|z|^{-2}+H(z),\qquad K(z)=2z|z|^{-4}-\nabla H(z),\qquad
H\text{ smooth and even}.
\tag{2.2}
\]

In particular \(K\in L^1\), the smooth force remainder is \(O(|z|)\), and
the sphere flux is \(2|\mathbb S^3|=4\pi^2=c\). The exact distribution is

\[
D=\operatorname{div}K=c(\delta_0-dz),\qquad
\operatorname{div}_{\rm cl}K=-c\text{ off zero}.
\tag{2.3}
\]

The atom and its Haar compensation give both pair responses

\[
R\Phi=-2c\Phi+cq(x)+cq(y),\qquad q(x)=\int\Phi(x,y)dy.
\tag{2.4}
\]

The one-body response is \(-c(f-\int f)\), and the source row is
\(\int J^f(x,y)dy=-c(f(x)-\int f)\); its scalar integral is zero.
Thus the response sign agrees with the frozen decaying multiplier. The norm
of the two-response operator on either bounded functions or Haar L1 is at
most \(4c\); its two slots are never replaced by one.

Let \(\Phi=\Phi^{N,\nu}[h]\) be the same terminal-zero full inverse in the
dossier. With
\(B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi\), it obeys off the diagonal

\[
\partial_t\Phi+\nu(\Delta_x+\Delta_y)\Phi+N^{-1}B\Phi+R\Phi=-J,
\qquad \Phi_T=0.
\tag{2.5}
\]

The R5 barrier at \(s=2,p=4\) has radial profile

\[
F_{N,a}(r)=\frac N4\left[(r^4+16a/N)^{1/2}-r^2\right],\qquad
0\le F_{N,a}\le\sqrt{Na}.
\tag{2.6}
\]

Its relative diffusion is \(2\nu\Delta_z\), its relative repulsive drift is
\(4N^{-1}r^{-4}z\), and \(\Delta F_{N,a}\le0\) in dimension four.
The fixed annular cutoff errors are bounded uniformly for bounded \(\nu\).
The stopped positive-barrier argument and bounded-response Volterra series
therefore give

\[
\sup_t\|\Phi_t[h]\|_\infty\le C\sqrt N\,\|h\|_{C^2},\qquad
\sup_t\|\Phi_t[h]\|_2^2\le C(1+\log N)\|h\|_{C^2}^2.
\tag{2.7}
\]

One may enlarge the constant for \(N\ge2\); at \(T=0\) the inverse is zero.
The first bound follows from (2.6), with the fixed cutoff/background constant
and \(e^{4cT}\). For the second, split the profile square integral at
\(r\asymp N^{-1/4}\): the core is bounded and the tail is the logarithmic
integral \(\int r^{-1}dr\). The R5 pair propagator Haar L2 norm is at most
\(e^{c(a-t)/N}\); the response series changes only the fixed time constant.
No actual N-body density enters these uniform bounds.

For the finite-N uses of (2.5), R8 supplies local C1-time/C2-space regularity,
global Haar H1, and absolute slice integrability of \(B\Phi\) through its
equation. Its first-gradient exponent can be chosen in \((1,2)\) and its
second-gradient exponent in \((q_1+1,4)\). These fixed-N constants are not
used as asymptotic estimates. The actual noncolliding paths have positive
minimum separation on each finite time interval, so stopped classical Itô
applies and the R8 L1/L2 passage removes the stops. Singular diagonal values
are not part of that domain.

## 3. Actual-law weak concentration and uniform inverse L1

Write \(H_N=N^{-1}\sum_{i<j}g(X_i-X_j)\) and
\(\eta_N=N^{-1}\sum_i\delta_{X_i}\). The actual energy sign supplied and
proved in R16 is

\[
\mathbb E H_N(X_t)\le0.
\tag{3.1}
\]

Its mechanism is specific to the admitted law: at fixed heat cutoff, the
free energy \(\nu\operatorname{Ent}(F)+\mathbb EH_N\) decreases from zero;
entropy relative to mass-one configuration Haar is nonnegative. Same-noise
particle convergence at fixed \(N,\nu,T\) and Fatou after a fixed lower
energy shift give (3.1). At zero noise ordinary energy decrease gives it
directly. The actual law has Haar one-body marginal by common-translation
invariance, not by independence at positive time.

For \(0<r\le1\), set
\(g^{>r}=c\int_r^\infty(p_u-1)du\). Then
\(g\ge g^{>r}-cr\) off zero, its nonzero coefficients are
\(a_r(k)=|k|^{-2}e^{-c r|k|^2}>0\), and \(g^{>r}(0)\le Cr^{-1}\).
Deleted-pair evaluation gives the exact self/background factors

\[
H_N\ge\frac N2\sum_{k\ne0}a_r(k)|\widehat\eta_N(k)|^2
       -\frac12g^{>r}(0)-\frac{N-1}{2}cr.
\tag{3.2}
\]

Choosing \(r=N^{-1/2}\) after taking the expectation yields
\(\mathbb E\sum a_r(k)|\widehat\eta_N(k)|^2\le C N^{-1/2}\).
For \(|k|\le N^{1/4}\), \(a_r(k)\ge e^{-c}|k|^{-2}\). For larger modes
use \(|\widehat\eta_N(k)|\le1\). Consequently, uniformly in deterministic
time and all the admitted diffusivities,

\[
\mathbb E|\widehat\eta_N(t,k)|^2
\le\min(1,CN^{-1/2}|k|^2),\qquad k\ne0.
\tag{3.3}
\]

For every deterministic smooth test \(a\), even one depending on \(N,t,\nu\),
Minkowski and its absolutely summable Fourier series give

\[
\mathbb E|\rho_t[a]|
\le C N^{-1/4}\sum_{k\ne0}|k|\,|\widehat a(k)|
\le C N^{-1/4}\|a\|_{C^6},\qquad \rho_t=\eta_N(t)-dx.
\tag{3.4}
\]

For the last inequality use \((1-\Delta)^3\): in four dimensions the sum
of \(|k|(1+|k|^2)^{-3}\) is finite. This is a uniform estimate on bounded
families of smooth tests, not merely a fixed-mode convergence statement.

The source has uniform Haar L1 norm, since its singularity is at most
\(C_h r^{-2}\). The auxiliary pair Haar measure bound is
\(\|S_a v\|_1\le e^{2ca/N}\|v\|_1\), and \(\|R\|_{1\to1}\le4c\).
In the Volterra expansion the intervening time intervals add to at most T.
Absolute summation over ordered simplices therefore gives

\[
\sup_{t,N,\nu}\|\Phi_t[h]\|_1\le C\|h\|_{C^2}.
\tag{3.5}
\]

These are bounds on the genuine inverse. No smoothing has yet been applied.

## 4. New Coulomb contraction lemma, including its boundary flux

For every fixed spatial order m, common-translation covariance and linearity
give

\[
\Phi_t[h](x+a,y+a)=\Phi_t[h(\cdot+a)](x,y),\qquad
(\partial_x+\partial_y)^\alpha\Phi_t[h]=\Phi_t[\partial^\alpha h].
\tag{4.1}
\]

The covariance follows from the actual pair evolution, the two homogeneous
responses, and uniqueness of the bounded Volterra inverse. For the derivative,
take difference quotients in \(C^2\) of the smooth terminal test and use the
first estimate in (2.7); the quotients converge in the off-diagonal sup norm.
Thus this is a genuine derivative assertion, independent of the potentially
large individual relative derivatives. In particular

\[
\sup_t\| (\partial_x+\partial_y)^\alpha\Phi_t[h]\|_\infty
\le C\sqrt N\,\|h\|_{C^{m+2}},\qquad |\alpha|\le m.
\tag{4.2}
\]

Define the genuine contraction
\(b_t(x)=\int B\Phi_t(x,y)dy\), which is absolutely convergent for every
x by R8. Fix t,x and put \(\psi_x(z)=\Phi_t(x,x-z)\) off zero. Then

\[
B\Phi_t(x,x-z)
=K(z)\cdot[(\nabla_x+\nabla_y)\Phi_t(x,x-z)+2\nabla_z\psi_x(z)].
\tag{4.3}
\]

The first summand is absolutely integrable by \(K\in L^1\) and (4.2).
The second is therefore absolutely integrable as a scalar product because
the left side is. This does not assert absolute integrability of every
individual force-gradient component.

Integrate over the punctured torus \(\{|z|>\varepsilon\}\) and use
\(\operatorname{div}_{\rm cl}K=-c\). The inner normal is \(-\theta\), and
\(K(\varepsilon\theta)\cdot(-\theta)\varepsilon^3=-2+O(\varepsilon^4)\).
The divergence theorem therefore gives

\[
\int_{|z|>\varepsilon}K\cdot\nabla_z\psi_x
=c\int_{|z|>\varepsilon}\psi_x(z)dz
 -2\int_{\mathbb S^3}\psi_x(\varepsilon\theta)dS(\theta)
 +O(\varepsilon^4\|\Phi_t\|_\infty).
\tag{4.4}
\]

All integrals on the left converge absolutely at this fixed N; the volume
integral on the right converges by boundedness. Thus the *spherical average*
has a limit

\[
\tau_t(x)=\lim_{\varepsilon\downarrow0}
\frac1{|\mathbb S^3|}\int_{\mathbb S^3}
                    \Phi_t(x,x-\varepsilon\theta)dS(\theta),\qquad
|\tau_t(x)|\le\|\Phi_t\|_\infty.
\tag{4.5}
\]

Existence of this average is a consequence of the already legitimate
contraction, not an assumed pointwise trace or a singular Itô premise.
No directionwise limit and no value of \(\Phi(x,x)\) are asserted. Combining
(4.3)–(4.5), with \(c=2|\mathbb S^3|\), proves the exact identity

\[
\boxed{\displaystyle
b_t(x)=\int K(z)\cdot(\nabla_x+\nabla_y)\Phi_t(x,x-z)dz
                   +2c\,[q_t(x)-\tau_t(x)].}
\tag{4.6}
\]

The coefficient is \(2c\), not c. Both its negative spherical-flux term
and its positive periodic compensation remain. It gives

\[
\|b_t[h]\|_\infty
\le\|K\|_1\|(\nabla_x+\nabla_y)\Phi_t[h]\|_\infty
          +4c\|\Phi_t[h]\|_\infty
\le C\sqrt N\,\|h\|_{C^3}.
\tag{4.7}
\]

The contraction itself is linear and translation covariant:
\(b_t[h](x+a)=b_t[h(\cdot+a)](x)\). Difference quotients in \(C^3\), now
using (4.7), show that b is smooth and

\[
\sup_t\|b_t[h]/\sqrt N\|_{C^m}\le C\|h\|_{C^{m+3}}
\quad\text{for every fixed }m.
\tag{4.8}
\]

This avoids differentiating a nonuniform singular product under its integral.
The finite-N continuity from R8 identifies the resulting derivative
representatives everywhere. Averaging the covariance over all translations
and using the bounded linear map in (4.7) gives

\[
\int b_t[h](x)dx=b_t[\textstyle\int h](x)=0.
\tag{4.9}
\]

The same argument with (2.7) gives \(\iint\Phi_t=0\). These are special
properties of the genuine inverse driven by the homogeneous one-body source;
the scalar contraction is not zero for a general symmetric pair test.

Let the two exact lower terms be

\[
\ell_N(t)=\frac1N\rho_t[b_t]+\frac1{2N}\int b_t(x)dx.
\tag{4.10}
\]

Equations (3.4), (4.8) with \(m=6\), and (4.9) prove the new bound

\[
\boxed{\displaystyle
\sqrt N\,\mathbb E\int_0^T|\ell_N(t)|dt
=\mathbb E\int_0^T|\rho_t[b_t/\sqrt N]|dt
\le C_{h,T}N^{-1/4}.}
\tag{4.11}
\]

This is stronger than cancellation of a signed mean. The absolute value
remains inside the time integral. The proof uses only the actual weak
concentration estimate and a deterministic smooth family of tests; it never
replaces the positive-time law by product Haar. Formula (4.11) is the new
Coulomb endpoint progress of this round.

## 5. Exact actual identity and the iid endpoint

Set \(p_t(x,y)=\nabla_x\Phi_t(x,y)\),
\(a_t(x)=\int p_t(x,y)dy\), and

\[
C\Phi(x,y,z)=\operatorname{Sym}_3[K(x-z)\cdot\nabla_x\Phi(x,y)],
\tag{5.1}
\]

where the symmetrization averages the six permutations. The literal U3 has
coefficients \(1,-3,3,-1\) in its three-label, one-background,
two-background, and full-background terms. At N=2 only its three-label
empirical sum is empty.

For a direct coefficient check, the force part of the particle generator of
P is

\[
\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}K(X_i-X_k)\cdot p(X_i,X_j)
 -\frac1{N^2}\sum_{i\ne k}K(X_i-X_k)\cdot a(X_i).
\tag{5.2}
\]

Separate \(k=j\), pair its two orientations, and expand all cubic
backgrounds. With \(D_2[v]=N^{-2}\sum_{i\ne j}v(X_i,X_j)\), the result is
\(U_3[C\Phi]+P[R\Phi]+(2N)^{-1}D_2[B\Phi]\).
The exact relation
\(D_2[B\Phi]-2P[B\Phi]=2\rho[b]+\int b\) gives the two lower
coefficients in (4.10). The time/diffusion part is
\(P[(\partial_t+\nu\Delta_{x,y})\Phi]\); no diffusion cross variation
exists between the distinct labels in that sum. Background Laplacians
integrate to zero in the R8 domain. Using (2.5) gives

\[
dP_N[\Phi_t]=[-P_N[J_t]+U_{3,t}[C\Phi_t]+\ell_N(t)]dt+dM_t^2[\Phi],
\tag{5.3}
\]
\[
M_t^2[v]=\sqrt{2\nu}\sum_i\int_0^t\nabla_iP_N[v_a](X_a)\cdot dW_i(a),
\quad
\nabla_iP_N[v]=\frac1{N^2}\sum_{j\ne i}\nabla_xv(X_i,X_j)
               -\frac1N\int\nabla_xv(X_i,y)dy.
\tag{5.4}
\]

These identities are for the actual finite-N process, with absolutely
integrable drifts and a true square-integrable martingale, by the supplied
R8 domain and its stopped passage. The fixed-N density bound in that passage
is \(e^{c(N-1)T}\); it is not a uniform concentration bound here.

Integration and \(\Phi_T=0\) give the exact sign

\[
\int_0^T P_N[J_t]dt
=P_N[\Phi_0]+\int_0^T U_{3,t}[C\Phi_t]dt
 +\int_0^T\ell_N(t)dt+M_T^2[\Phi].
\tag{5.5}
\]

For completeness the iid endpoint can be checked without any evolved-law
argument. For a symmetric square-integrable kernel v, put \(r=\iint v\),
\(a(x)=\int v(x,y)dy-r\), and
\(v^\circ=v-r-a(x)-a(y)\). Direct overlap counting at product Haar gives

\[
\mathbb E P_N[v]^2
=\frac{N-1}{2N^3}\|v^\circ\|_2^2
 +\frac1{N^3}\|a\|_2^2+\frac{r^2}{4N^2}
\le\frac{N-1}{2N^3}\|v\|_2^2\quad(N\ge2).
\tag{5.6}
\]

The equality retains the small first projection and deterministic mean.
For v=\(\Phi_0\), (2.7) therefore implies

\[
\mathbb E|\sqrt N P_N[\Phi_0]|
\le C\sqrt{(1+\log N)/N}\longrightarrow0.
\tag{5.7}
\]

The endpoint is evaluated only at the actual iid initial law.

## 6. Removing only the explicitly controlled part of the martingale

For \(0<\delta\le1\), let
\(\Psi_{t,\delta}=e^{\delta\Delta_x}e^{\delta\Delta_y}\Phi_t\), a
smoothing of this same full inverse. Put \(G_\delta=\nabla_x\Psi_\delta\).
The uniform L1 bound (3.5) bounds every Fourier coefficient of \(\Phi\).
Summing its heat multipliers in four dimensions gives

\[
\|G_\delta\|_\infty\le C\delta^{-9/2},\qquad
\sup_x|(G_\delta)_k(x)|\le C\delta^{-5/2}e^{-c\delta|k|^2},
\]
\[
\sum_{k\ne0}|k|\sup_x|(G_\delta)_k(x)|\le C\delta^{-5}.
\tag{6.1}
\]

Here \((G_\delta)_k\) is the Fourier coefficient in y; the lattice sums are
bounded by their radial Gaussian integrals plus finitely many small modes.
No N-dependent regularity constant is used.

For this smooth diagnostic only, differentiating the literal statistic gives

\[
\nabla_iP_N[\Psi_\delta]
=\frac1N\left[v_\delta(X_i)-\frac1N G_\delta(X_i,X_i)\right],
\quad v_\delta(x)=\int G_\delta(x,y)\rho_t(dy).
\tag{6.2}
\]

The subtraction is the missing self label; it is not suppressed. Minkowski,
(3.3), and (6.1) give
\(\mathbb E\sup_x|v_\delta(x)|^2\le C N^{-1/2}\delta^{-10}\).
Taking the supremum before evaluating at \(X_i\) avoids any independence
assumption. Define for every finite-N admissible v

\[
Q_N[v]=2\nu N\,\mathbb E\int_0^T\sum_i
                      |\nabla_iP_N[v_t](X_t)|^2dt.
\tag{6.3}
\]

It is the expected bracket of \(\sqrt N M^2[v]\). Equations (6.1)–(6.2)
prove, with every power and the physical \(2\nu N\) retained,

\[
Q_N[\Psi_\delta]
\le C\nu\,[N^{-1/2}\delta^{-10}+N^{-2}\delta^{-9}].
\tag{6.4}
\]

Choose \(\delta_N=N^{-1/40}\) and set
\(V_N=\Phi-\Psi_{\delta_N}\). On the actual critical sequence,

\[
Q_N[\Psi_{\delta_N}]\le C[N^{-3/4}+N^{-91/40}]
\le C N^{-3/4},\qquad
\mathbb E|\sqrt N M_T^2[\Psi_{\delta_N}]|\le C N^{-3/8}.
\tag{6.5}
\]

The last inequality is the actual Itô isometry followed by Cauchy–Schwarz.
Both \(M^2[\Phi]\) and the smooth integral are true L2 martingales at each
finite N, so \(M^2[V_N]\) is their exact difference. The singular kernel is
never evaluated on a diagonal. The only diagonal in (6.2) is that of the
explicitly smoothed kernel.

For possible future control of the retained noise, write
\(G=\nabla_xV_N\), \(A(x)=\int G(x,y)dy\), and \(H(x,y)=G(x,y)-A(x)\).
At each finite N its exact actual-law bracket is

\[
\begin{split}
Q_N[V_N]=\frac{2\nu}{N^2}\int_0^T\big[&
(N-1)\mathbb E|H_{12}|^2
+(N-1)(N-2)\mathbb E(H_{12}\cdot H_{13})\\
&-2(N-1)\mathbb E(H_{12}\cdot A_1)+\mathbb E|A_1|^2\big]dt.
\end{split}
\tag{6.6}
\]

At N=2 the distinct-triple term is absent. The full combination is
nonnegative, but the individual cross terms need not be. Haar one-body
marginals do not factor the other expectations.

## 7. Strictly smaller exact dynamic obligation and its first open line

Define the original scaled source random variable and the remaining one by

\[
S_N=\sqrt N\int_0^T P_N[J_t]dt,
\qquad
W_N=\sqrt N\left[\int_0^T U_{3,t}[C\Phi_t]dt+M_T^2[V_N]\right].
\tag{7.1}
\]

Every term is an L1 random variable at each finite N by the actual domain.
Equations (4.11), (5.5), (5.7), and (6.5) give

\[
\boxed{\displaystyle
\mathbb E|S_N-W_N|
\le C\left[N^{-1/4}+\sqrt{(1+\log N)/N}+N^{-3/8}\right]
\longrightarrow0.}
\tag{7.2}
\]

In particular

\[
|\mathbb E|S_N|-\mathbb E|W_N||\le\mathbb E|S_N-W_N|\to0.
\tag{7.3}
\]

This proves both directions of the reduction, including preservation of a
positive limsup in the exact negation. The finite initial segment where
\(b_N\ne1\) does not affect either side.

The weaker but simpler version, before smoothing, is already exact up to
the first two errors:

\[
\mathbb E\left|S_N-\sqrt N\left[
\int_0^T U_{3,t}[C\Phi_t]dt+M_T^2[\Phi]\right]\right|\to0.
\tag{7.4}
\]

The **first unproved dynamic line** in the sharper route is exactly

\[
\boxed{\displaystyle
\mathbb E\left|\sqrt N\left[
\int_0^T U_{3,t}[C\Phi_t]dt+
\sqrt{2\nu_N}\sum_i\int_0^T\nabla_iP_N[V_{N,t}](X_t)\cdot dW_i(t)
\right]\right|\longrightarrow0.}
\tag{7.5}
\]

There are no remaining lower contractions, initial endpoints, smooth
martingale pieces, scalar means, or unidentified domain passages in this
line. It is a uniform estimate under the original actual dynamics, and keeps
possible cancellation between its drift and martingale. The separately
stronger pair of conditions
\(\sqrt N\mathbb E|\int U_3[C\Phi]|\to0\) and \(Q_N[V_N]\to0\)
would suffice, but is not asserted to be necessary or established.

## 8. Complete attempted closures and their exact failures

1. **Direct absolute source bound.** R16 gives
   \(\mathbb E|P[J_t]|\le C(N^{-1}r^{-1}+r)\).
   Multiplication by \(\sqrt N\) and optimization at \(r=N^{-1/2}\)
   give only a constant. Indeed the minimum of the displayed two-term
   majorant after scaling is 2. This proves failure of that majorant to
   decay, not a lower bound on the actual source. Moving the absolute value
   outside time can help only through additional dynamic cancellation.

2. **R14 absolute product estimate at Coulomb.** The required gradient
   exponent must satisfy \(q>1\), whereas integrability of
   \(|K|w_q\) in dimension four requires \(3+q<4\), or \(q<1\).
   There is no admissible q. At q=1 the radial majorant is \(dr/r\).
   Section 4 repairs precisely this lower-contraction route by keeping the
   signed scalar product and proving its spherical-flux identity.

3. **R12 positive singular Laplacian occupation.** Its coefficient
   \(s(d-2-s)\) is zero here. The actual punctured divergence is \(-c\),
   not a positive multiple of \(r^{-4}\). Hence the energy identity gives
   no positive \(\nu\int\mathbb E r_{12}^{-4}\) occupation term.
   The atom in (2.3) cannot be substituted for such a pathwise bulk term.
   This is the exact reason that the existing noise proof cannot close (7.5).

4. **Uniformizing fixed-N heat convergence.** For every fixed N the R8
   Haar H1 domain and finite density bound justify heat approximation of
   the martingale integrands. Multiplication by
   \(e^{c(N-1)T}\) gives no uniform estimate at \(\delta_N\).
   Thus the next unproved inference would be \(Q_N[V_N]\to0\).
   The available critical entropy estimate is only of order N, and the
   Fourier estimate (3.3) loses smallness at \(|k|\asymp N^{1/4}\).
   Neither controls the singular products in (6.6).

5. **Using the natural pointwise gradient weight.** R11's uniform natural
   weight at bounded rescaled diffusivity is \(r^{-3}\) for the gradient.
   Its square has radial Haar power \(r^{3-6}=r^{-3}\), which is not
   integrable, much less controlled by the actual energy moment of order
   \(r^{-2}\). The R8 smaller fixed-N exponent makes its own square
   integrable but supplies no N-uniform rate. Neither bound proves (6.6)
   small or controls the actual cubic products.

6. **Signed means and total-force coercivity.** Translation covariance
   makes the signed expectation of the source zero, and the martingale has
   mean zero. Those facts do not estimate (1.3) or (7.5). Likewise the actual
   energy identity controls the square of the complete sum of particle
   forces. Its cross terms cannot be dropped to obtain a sum of pair-force
   squares. No such positivity or independence step is used here.

7. **A source-square estimate at the initial law.** For a smooth test with
   nonzero Hessian on an open set, the leading Coulomb source is
   \(2r^{-2}\theta^TD^2f(x)\theta\). Its square has the logarithmic
   radial integral \(\int dr/r\). This explains why a blanket source L2
   argument already fails at iid Haar. The integrated source is still L1;
   this observation does not negate the target.

These failures leave a specific uniform dynamic estimate, not a claim of
impossibility. No static-law construction is used as a negation.

## 9. Independent falsification calculation and fresh diagnostic

An independent analytic test uses the actual initial generator on the smooth
observable \(|Z_k|^2\), \(Z_k=N^{-1}\sum_i e^{-2\pi i k\cdot X_i}\),
rather than the corrector proof. Under iid Haar, the self terms give
\(\mathbb E|Z_k(0)|^2=1/N\). The two internal forces of an ordered pair
give \(-2c/N\) after integration against its nonzero difference mode;
each third-label force has zero Haar integral. Multiplication by the
ordered-pair fraction \((N-1)/N\) gives

\[
\left.\frac d{dt}\mathbb E|Z_k(t)|^2\right|_{t=0}
=-\frac{2(N-1)}{N^2}c<0\qquad(k\ne0).
\tag{9.1}
\]

Diffusion has zero initial Haar integral. This derivative is valid for the
singular actual law at each fixed N: its smooth-observable generator is
Haar L1 since K is; approximate it in L1 by continuous functions, use the
fixed-N density bound on a short initial interval, and then weak convergence
of the path law to iid Haar. This justifies differentiating the expectation
at zero and retains the Coulomb atom in the distributional integration.
It rules out an immediate positive low-mode variance-creation mechanism.
It proves no uniform Taylor remainder and no later-time variance sign.

The separately coded `exact_diagnostic.py` reads no earlier code. Rational
Laurent-polynomial arithmetic compares the direct finite-particle generator
with the full pair identity, including both responses, all U3 backgrounds,
both lower coefficients, exact iid endpoint moments, and the carré du champ.
The probes have N=2,3,4 (and N=5 for the initial derivative), zero/positive
diffusion, zero/one/two Fourier-mode force, and constant/relative/additive/
mixed symmetric kernels. Their one-coordinate dependence embeds in T4.
Every physical second-order expression is divided by the common factor
\((2\pi)^2\), which is restored in (9.1).

A separate finite-Fourier computation checks (4.6) for globally smooth pair
kernels: here the spherical average is their ordinary diagonal trace. It
compares direct internal drift contraction against the common-translation
term plus **both** Coulomb flux/compensation terms. Nonzero total modes have
zero scalar contraction; a relative-mode test has a nonzero scalar, detecting
the invalid universal deletion of that term. A radial-shell calculation
checks the same boundary coefficient in physical coordinates.

The limiting smooth Fourier test independently integrates the scalar ODE
\(u'=-ru+e^{-a}\), \(u(0)=0\), for response rates r=1 and r=2, by RK4
and compares against the exact response integral at a=1. Arithmetic has
50 decimal digits, steps 128 and 256, and tolerance 2e-10. This tests the
single-active-slot and two-active-slot limits; the missing-response mutation
has a nonzero discrepancy. It is a smooth limiting-model check, not a
simulation or proof of the singular actual dynamics.

`RESULTS.json` records all assertion counts, exact detecting mutations,
decimal errors, the code digest, and evidence class. No random seed is
needed. Mutation witnesses are required to be nonzero; merely running a
changed formula that vanishes on a selected test is not counted as detection.

The analytic self-check separately challenged: the inner-normal sign; the
factor two in relative differentiation; the periodic compensation; the
existence rather than assumption of the spherical-average limit; interchange
of common translations through the inverse; the exact zero scalar only for
the genuine source; smooth-test uniformity in (3.4); initial first projection;
the missing self label in (6.2); and the absolute value in (7.5). No independent
audit status follows from those checks or from the program.

## 10. Dispositions and recoverable handoff

| Item | Disposition |
|---|---|
| Full THM-046 / PO-033 assertion | OPEN; neither proved nor falsified. |
| Coulomb spherical-average identity (4.6) and smooth contraction bound (4.8) | PROVED HERE FROM THE PRECISE DOSSIER DOMAIN/INVERSE MODULES; SELF_CHECKED. |
| Actual scaled lower drift (4.11), including scalar zero | PROVED HERE; SELF_CHECKED. No extension of the R12 occupation premise. |
| Actual source equivalence (7.2)–(7.5) | EXACT SMALLER DYNAMIC REDUCTION; SELF_CHECKED. |
| Singular martingale-tail control or integrated cubic control | OPEN. Their separate smallness is only a sufficient possible route. |
| Static-law obstruction, Gaussian law, finite hierarchy closure, novelty claim | NOT CLAIMED. |

The next mathematical action is to prove or disprove (7.5) under the original
iid-prepared dynamics, or first establish either of its two stronger
sufficient estimates while retaining the other. The immediate audit action
is a fresh isolated check of the new flux/translation lemma and the actual
weak-concentration transfer, followed by a coefficient/domain check of the
complete reduction. This constructor may not promote its own gate.

Only this memorandum, its named artifact directory, and the allowed sibling
archive/seal are written. The artifact packet contains all twenty exact
input copies, the original input manifest, source/exposure records, fresh
diagnostic and results, an independent packaging verifier, exact archive
inventory, README, and output manifest. The archive inventory is closed:
no absolute paths, traversal, links, duplicate members, unexpected members,
or unmanifested bytes are accepted. Issued files are made read-only after
verification. No canonical ledger, input, existing audit, branch, commit,
remote, or global configuration is changed. Root owns integration and any
new canonical identifiers.
