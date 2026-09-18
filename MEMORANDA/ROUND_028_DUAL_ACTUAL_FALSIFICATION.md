# Round 028 — the actual modal defect reduced to its first-collision history

TASK120, ordinary Astra Max, 2026-09-18 UTC. Worktree
/Users/matthewrosenzweig/.codex/worktrees/hocf-r028-dual-falsification,
base ef438b612f732d21af1fa1756dd7559ef63c6d61.

**QUANTITATIVE BOUNDARY REDUCTION / SELF_CHECKED ONLY.
The original THM046 remains OPEN; no admitted positive-limsup witness is proved.**

After survival to any fixed horizon, continue the same attractive path to
its first collision. Its empirical fixed Fourier mode changes by a quantity
that tends to zero in the original square-root-N L2 scale. The error is
bounded explicitly below, uniformly over bounded positive diffusivities.
Thus the actual critical target is equivalent to a precise exponentially
weighted first-collision-history defect. The exponentially rare survival
normalizer and the initial/collision correlation are retained exactly.

This is new quantitative progress beyond the supplied duality/survival
statement. The new proof uses a canonically centered clipping of the iid
source, stopped occupation identities, and the full stopped martingale.
It neither bounds an individual force square nor treats a Brownian integral
conditioned on future survival as a martingale. The remaining inequality
concerns the initial Fourier mark on an exponentially rare lifetime tail.
The unmarked collision law does not resolve that inequality.

## 1. Unchanged target, negation, and the new local claims

Use precisely d=4, s=2, the unit torus and mass-one Haar measure m.
Fourier characters are e_k(x)=exp(2 pi i k.x). The coefficient-one
Coulomb kernel has g_hat(0)=0 and g_hat(k)=|k|^-2 for k nonzero.
Set c=4 pi^2, K=-grad g,
H_N=N^-1 sum_(i<j) g(x_i-x_j), and kappa=c(N-1).
The collision-free configuration space is Omega; configuration Haar is
m_N=m^N. The repulsive process X starts iid Haar independently of all
Brownian drivers, has drift -grad H_N and covariance 2 nu times the
identity, and is conservative. The explicitly auxiliary attractive
process Y starts from the same iid Haar law, has drift +grad H_N and the
same noise covariance, and is killed at its maximal collision-free
lifetime zeta. Its process is never substituted for X without the exact
law identity.

Fix N>=2, finite nu>0, nonzero fixed k in Z^4, and fixed finite T>=0.
Write
\[
 F=F_k=N^{-1}\sum_i e_k(x_i),\qquad
 \ell=\ell_k=c|k|^2,\quad a=c+\nu\ell,\quad A_T=e^{-aT},
 \quad b=c(1-1/N)-\nu\ell.                              \tag{1.1}
\]
The precise defect at the start of this task is
\[
 \mathcal D_N(k,T)
 =N\mathbb E_{\rm att}\big[|F(Y_0)-A_TF(Y_T)|^2
                                      \mid\zeta>T\big]. \tag{1.2}
\]
By the supplied whole-path identity this is exactly
N E_rep |F(X_T)-A_T F(X_0)|^2. Its orientation is literal.

For the original target, beta_N/sqrt(N) tends to a fixed lambda in
(0,infinity), nu_N=1/beta_N, and the same k,T are fixed independently of N.
THM046 asks for the original expected absolute integrated source to vanish
for every fixed smooth real test. Accepted THM048/049, through the complete
R25 proof and gate supplied here, identify this assertion with vanishing
of (1.2) for every fixed nonzero k. Its exact negation is an admitted
fixed k,T,lambda and critical sequence with positive limsup of (1.2),
which yields a fixed real cosine or sine source witness. An auxiliary
static law, moving test/time, zero-noise finite-N model, or failed proof
does not negate it.

In this row the old energy-floor condition is beta_N -> 0; microscopic
subcriticality is beta_N/sqrt(N) -> 0; the critical positive-limit
condition just stated is separate. There is no logarithmic substitution.

Local labels D28-A through D28-E identify claims in this memorandum only;
root owns any canonical THM/PO allocation.

- D28-A: the attractive collision endpoint exists almost surely; its
  joint lifetime/position law is the exact one-pair fusion law (3.5).
- D28-B: the original canonical source has the quantitative iid bound
  (4.6), with the exact deleted-pair coefficient.
- D28-C: the first-collision mode change satisfies the finite-N L2
  inequality (5.5), including after any fixed survival horizon.
- D28-D: the original defect and the collision-profile norm differ by
  at most the explicit error (6.5), with their critical vanishing and
  positive-limsup criteria equivalent.
- D28-E: the unconditioned initial/collision covariance tends to one in
  its N-normalization, while this does not control the rare-tail profile.

The exact negation of this auxiliary conjunction is an admitted finite
N,nu,k,T violating endpoint existence, its joint law, the stated iid or
mode-change inequality with the defined constants, or the exact norm
comparison and its stated consequences. It is distinct from the original
target's negation. All five local claims remain SELF_CHECKED.

## 2. Exact sources and the killed mechanism actually used

All 17 allowlisted byte strings were verified before mathematical work
and copied completely into the packet. Their complete texts were read.
The first combined R4/R6 tool display was truncated; the relevant ranges
were subsequently reread explicitly, with the R6 ending reread in full.
No linked nonallowlisted file was opened. The task-specific isolation
rule takes precedence over general instructions to read canonical state,
the README, or campaign history. The original instruction/task/manifest,
not a current status label, fixes the scope.

The source qualifications are as follows.

| Supplied source | Exact use and limitation |
|---|---|
| AGENTS, MODEL_ORCHESTRATION, R1 model, TASK120 | Conduct, normalization, ordinary role and bounded scope; no certification follows from model name. |
| R1 algebra | Ordered distinct labels, N^2 denominator, half factor, both backgrounds and noise convention. New coefficients below are recomputed. |
| R4 singular response | Coefficient-one local kernel and the full Coulomb divergence measure. No L2 source square or pointwise singular diagonal is imported. |
| R6 particle realization | Conservative repulsive realization by stopped complete energy; local cutoff construction and measurable Markov laws. No N-uniform density bound is imported. |
| R10 actual-law report | Entire text inspected; its unrelated corrector/domain premises and nonallowlisted cited sources are not used. |
| R16 source extension | Entire text inspected; supports the original source scope but its nondecaying threshold bound does not imply this target. |
| THM046, THM048, THM049 and full R25 proof/gate | Exact original target and accepted L1/modal-L2 equivalence. Printed OPEN labels on old frozen cards are not substituted for the supplied accepted gate. |
| THM052, full R27 proof and exposure note | Exposed self-checked duality construction, not an independent certificate. Its needed mechanism is reconstructed below; full fresh whole gates remain root's responsibility. |

No external/private theorem, source retrieval, novelty claim, memory file,
other worktree, prior checker, current audit narrative or canonical
STATE/history is used. The parent later gave a status-only notice that
another ordinary lane also addresses unmarked collision flux. That notice
arrived after the endpoint/flux argument here was derived and reported.
No mathematical text or result from that lane was received or read.

For completeness, the mechanisms needed from R27 are visible here.
The heat representation is
g=c integral_0^infinity (p_u-1) du. It gives
g(z)=|z|^-2+H(z) near zero, H smooth even, K in L1, and
\[
 \operatorname{div}K=c(\delta_0-m),\qquad
 \Delta_{4N}H_N=\kappa\quad\hbox{on }\Omega.           \tag{2.1}
\]
The two differentiated coordinates per unordered pair give 2/N.
Distributionally on the full configuration torus,
\[
 \Delta_{4N}H_N
 =\kappa m_N-\frac{2c}{N}\sum_{i<j}\gamma_{ij}.        \tag{2.2}
\]
Here gamma_ij integrates a function with x_i=x_j, their common coordinate
Haar, and all other coordinates independent Haar. Equation (2.2) retains
both the Coulomb atom and the torus compensation; it is not the punctured
identity used across a collision.

The shifted energy H_N-(N-1)inf(g)/2 is nonnegative and diverges at every
partial collision. Smooth local cutoffs give the two drifts up to their
collision-excluded exits. Repulsive stopped Ito has drift
-|grad H_N|^2+nu kappa; its exit probability is at most the initial shifted
energy plus nu kappa T, divided by the exit height. Thus the repulsive
process is conservative. Only its complete drift square is used.

On D_L={minimum pair distance>1/L}, extend the drifts smoothly and kill on
exit. For Brownian motion with generator nu Delta, Ito for H_N before exit
and bounded Girsanov give
\[
 P_t^{D_L}h=e^{H_N/(2\nu)+\kappa t/2}
      K_t^{D_L}(e^{-H_N/(2\nu)}h),\qquad
 Q_t^{D_L}f=e^{-H_N/(2\nu)-\kappa t/2}
      K_t^{D_L}(e^{H_N/(2\nu)}f).                    \tag{2.3}
\]
The same K is the killed Brownian Feynman--Kac operator with potential
|grad H_N|^2/(4nu). It is symmetric under Haar: stationary Brownian path
reversal preserves the event of staying in D_L and this time integral.
Every coefficient and exponential weight in (2.3) is bounded at this
fixed domain. Hence integration gives
integral f P_t^{D_L}h = e^(kappa t) integral h Q_t^{D_L}f.
For nonnegative bounded functions, domain exhaustion is monotone.
Repulsive exits tend to infinity and attractive exits tend to zeta.
This proves
\[
 \int fP_th\,dm_N=e^{\kappa t}\int hQ_tf\,dm_N,
 \qquad
 \mathbb E_m[f(Y_t)\mathbf1_{t<\zeta}]
                  =e^{-\kappa t}\int f\,dm_N.       \tag{2.4}
\]
The second equality uses P_t1=1. Nonnegative measurable integrable
extensions follow by monotone truncation. In particular zeta has exact
exponential law of rate kappa and the current survivor marginal is
product Haar. No uniform estimate is extracted from the fixed-domain
H_N weights.

Successive transposition of semigroups in finite cylinder expectations
gives the reversed attractive path conditional on zeta>T as the repulsive
path from Haar. Both paths are continuous on the surviving compact
interval, and rational evaluations generate the Borel sigma-field for
the uniform topology. This identifies the whole path measure and gives
(1.2). This paragraph acknowledges reconstruction from the exposed R27
argument; it is not a fresh independent audit of it.

## 3. A genuine collision endpoint and its exact mark law

This section is needed for the later quantitative argument, not offered
as its sole outcome. Write B^+=grad H_N. For each fixed finite N,
\[
 \int_\Omega\sum_i|B_i^+|\,dm_N
       \le (N-1)\|K\|_1<\infty.
\]
Tonelli and (2.4) therefore give
\[
 \mathbb E_m\int_0^\zeta\sum_i|B_i^+(Y_s)|\,ds
       \le \frac{N-1}{\kappa}\|K\|_1<\infty.         \tag{3.1}
\]
Thus the Euclidean lifts of the drift integrals have finite total
variation before zeta almost surely. The Brownian drivers are defined
for all finite times, and zeta is finite almost surely. Each coordinate
therefore has a limit as time increases to zeta. Denote this limit by
Y_zeta on the full torus, without continuing the SDE there. If it were
collision-free, local smooth continuation would contradict maximality.
This proves endpoint existence and collision support, without a
pointwise force-square bound.

For any globally smooth complex configuration test phi, stopped Ito on
D_L passes to zeta and to a deterministic time t because L^+phi is Haar
L1, its expected stopped time integral is finite by (2.4), the function
is bounded, and the stopped Brownian integrands are bounded. Thus
\[
 \mathbb E_m[\phi(Y_t)\mathbf1_{t<\zeta}]
 +\mathbb E_m[\phi(Y_\zeta)\mathbf1_{\zeta\le t}]
 =\int\phi\,dm_N+
   \int_0^t e^{-\kappa s}\int L^+\phi\,dm_N\,ds,      \tag{3.2}
\]
where L^+=nu Delta+grad H_N.grad. No boundary value of a singular
corrector is used. The test itself is smooth on the full configuration
torus.

Ordinary distributional integration against (2.2) gives
\[
 \int L^+\phi\,dm_N
 =-\kappa\int\phi\,dm_N+\frac{2c}{N}
                                  \sum_{i<j}\gamma_{ij}[\phi].
                                                               \tag{3.3}
\]
The nu Delta integral is zero. Substituting (2.4) into (3.2) yields
\[
 \mathbb E_m[\phi(Y_\zeta)\mathbf1_{\zeta\le t}]
 =(1-e^{-\kappa t})\,\Gamma_N[\phi],\qquad
 \Gamma_N={\binom N2}^{-1}\sum_{i<j}\gamma_{ij}.      \tag{3.4}
\]
Smooth approximation first extends this identity to continuous tests;
uniqueness of finite Borel measures then extends it to bounded Borel
tests. Subtracting two times identifies the entire product measure
\[
 \boxed{\mathbb P_m(\zeta\in dt,Y_\zeta\in dz)
       =\kappa e^{-\kappa t}\,dt\,\Gamma_N(dz).}      \tag{3.5}
\]
This also proves that almost surely exactly one pair, rather than a
larger cluster, coincides at the first collision. Each gamma_ij gives
other coincidences measure zero, and the different one-pair strata are
disjoint up to those null sets. The colliding unordered pair is uniform
and independent of zeta. Neither statement makes Y_0 independent of
zeta or Y_zeta.

For nonzero k the initial and fused Fourier moments are exactly
\[
 \int F\,dm_N=\Gamma_N[F]=0,\quad
 \int|F|^2dm_N=1/N,\quad
 \Gamma_N[|F|^2]=(N+2)/N^2.                        \tag{3.6}
\]
The last numerator is 4 from the merged pair plus N-2 other squared
coefficients. Equivalently the N self terms and precisely two additional
ordered equal-coordinate terms survive. There is no singular diagonal
value of J or g in this calculation.

## 4. Canonical iid clipping of the exact Fourier source

Define the literal symmetric zero-row kernel and its statistic
\[
 j(x,y)=K(x-y)\cdot(\nabla e_k(x)-\nabla e_k(y))
                          +c(e_k(x)+e_k(y)),\qquad
 U=\frac1{2N^2}\sum_{i\ne j}j(x_i,x_j).             \tag{4.1}
\]
Only distinct labels at collision-free coordinates occur in U.
The original row of J is -c e_k and its double Haar contraction is zero:
integrate by parts against div K=c(delta_0-m). Thus each row of j
vanishes exactly. The original statistic is P_N[J]=U+(c/N)F.
This last coefficient is the empirical self-deletion correction, not
a change of centering.

Here is a concrete kernel-dependent tail constant. Fix r0=1/4,
M_H=sup_(|z|<=r0)|grad H(z)| and
M_K=sup_(dist(z,0)>=r0)|K(z)|, both finite. Put
A_k=2 ell,
B_k=ell M_H r0+2c,
D_k=4 pi |k| M_K+2c, and
\[
 L_{0,k}=\max(1,2B_k,2D_k,2A_k/r_0^2),\qquad
 C_k=\max(L_{0,k}^2,2\pi^2 A_k^2).                 \tag{4.2}
\]
These A_k and D_k are constants used only in (4.2), not the response
A_T or modal defect. Near zero, |j|<=A_k/r^2+B_k; away from zero,
|j|<=D_k. For L>=L_0,k, the event |j|>L is inside
r^2<2A_k/L<=r0^2, of four-ball volume at most
2 pi^2 A_k^2/L^2. For 1<=L<L_0,k the trivial probability bound suffices.
Consequently, on Haar pair space,
\[
 m^2(|j|>L)\le C_k L^{-2}\quad(L\ge1).              \tag{4.3}
\]
All constants depend only on fixed k and the frozen kernel, never N,nu,T.
This estimate is for the actual complex j; it is not a source L2 claim.

Let j_L=j min(1,L/|j|), with zero mapped to zero. Let r_L(x) be its
Haar row and m_L its double mean, and set
v_L(x,y)=j_L(x,y)-r_L(x)-r_L(y)+m_L.
This is the orthogonal double-centering projection in complex Haar L2;
the two coordinate averaging projections commute, so
||v_L||_2<=||j_L||_2. Since j already has zero rows, the residual
j-v_L is the double-centering of j-j_L in L1 and has norm at most
4||j-j_L||_1. Layer-cake applied to (4.3) gives
\[
 \|j_L\|_2^2\le1+2C_k\log L,\qquad
 \|j-j_L\|_1\le C_k/L.                             \tag{4.4}
\]
These are genuine complex modulus bounds; no clipping of the dynamics
or of the source in the target is performed.

For iid Haar coordinates, the distinct unordered summands v_L(X_i,X_j)
are orthogonal in complex L2. Disjoint pairs factor by independence;
one-label overlaps vanish by conditioning on their shared coordinate
and using the zero rows. Since v_L is symmetric, the two ordered
orientations have already combined to coefficient 1/N^2. Therefore
\[
 \mathbb E_m\left|\frac1{2N^2}\sum_{i\ne j}v_L(X_i,X_j)\right|^2
       =\frac{N-1}{2N^3}\|v_L\|_2^2.              \tag{4.5}
\]
There is no assumed independence between overlapping pairs.

Taking L=N and retaining the residual coefficient proves the explicit
bound
\[
 \boxed{\mathbb E_m|U|\le u_{N,k}:=
 \sqrt{\frac{N-1}{2N^3}(1+2C_k\log N)}
             +\frac{2C_k(N-1)}{N^2}.}             \tag{4.6}
\]
Thus u_N,k=O_k(sqrt(1+log N)/N). A fixed-time iid bound alone is not
being transferred to the repulsive law; it will be integrated only
against the exactly known killed survivor measure.

## 5. Quantitative mode control from any survivor horizon to collision

Directly apply the attractive generator to the smooth configuration
observable F. Its diffusion is -nu ell F, and its force term is the
negative of the repulsive ordered-pair force term. Counting both
orientations gives the exact identity
\[
 L^+F=bF-U,\qquad b=c(1-1/N)-\nu\ell.              \tag{5.1}
\]
For example the row addition in (4.1), summed with coefficient
1/(2N^2), is c(N-1)F/N. This is why b contains -c/N and why the
attractive diffusion contribution has the same negative sign as the
repulsive diffusion contribution.

Stop the one-body martingale on the collision-free exhaustion, pass
at fixed N,nu to zeta, then let the deterministic outer time tend to
infinity. Equation (3.1), or (2.4) and (4.6) applied to |bF-U|,
gives absolute drift integrability. The bounded gradient gives the
following L2 limit and exact stopped identity:
\[
 F(Y_\zeta)-F(Y_0)=I+M,\quad
 I=\int_0^\zeta(bF(Y_s)-U(Y_s))\,ds,\quad
 M=\frac{\sqrt{2\nu}}N\sum_i\int_0^\zeta
                           \nabla e_k(Y_i(s))\,dW_i(s).        \tag{5.2}
\]
The martingale is under the unconditioned iid-start law. Its exact
complex bracket and expected square are
\[
 d\langle M_k,\overline M_l\rangle_s
 =\frac{2\nu c}{N}(k\cdot l)F_{k-l}(Y_s)
                                  \mathbf1_{s<\zeta}\,ds,
 \quad
 \mathbb E|M|^2=\frac{2\nu\ell}{N\kappa}.             \tag{5.3}
\]
The unconjugated cross bracket is
-2 nu c(k.l) F_(k+l) 1_(s<zeta) ds/N. In particular the self
conjugate bracket is 2 nu ell (s wedge zeta)/N. No drift/martingale
or endpoint/martingale cross term is set to zero.

By the killed occupation identity,
E|I| <= kappa^-1 (|b|/sqrt(N)+u_N,k). Write Delta=F(Y_zeta)-F(Y_0);
|Delta|<=2. Then
E|Delta|^2=Re E(Delta conjugate(I))+Re E(Delta conjugate(M))
<=2 E|I|+sqrt(E|Delta|^2 E|M|^2).
The elementary inequality xy<=x^2/2+y^2/2 yields
\[
 \mathbb E|\Delta|^2\le4\mathbb E|I|+\mathbb E|M|^2.
                                                               \tag{5.4}
\]
Thus
\[
 \boxed{N\mathbb E_m|F(Y_\zeta)-F(Y_0)|^2
 \le\epsilon_{N,k,\nu}:=
 \frac{4N}{\kappa}\left(\frac{|b|}{\sqrt N}+u_{N,k}\right)
                      +\frac{2\nu\ell}{\kappa}.}    \tag{5.5}
\]
There is no instantaneous source variance in this proof. In particular,
the logarithmically infinite Haar square of j is harmless here because
only its clipped iid L1 estimate enters a stopped time integral.

For 0<nu<=nu_* and fixed k,
epsilon_N,k,nu=O_(k,nu_*)(N^-1/2+sqrt(1+log N)/N).
This includes every critical tail, but asserts no zero-noise replacement
for the admitted original model.

Now fix any deterministic T>=0. Conditional on zeta>T, Y_T is Haar,
and the future path follows the same killed Markov family started there.
Consequently every nonnegative functional of the path from T until
its later collision has precisely its unconditioned iid-start law.
This is a statement about that future segment only; it does not make
it independent of Y_0. Applying (5.5) gives the exact uniform-horizon
consequence
\[
 \boxed{N\mathbb E_m[|F(Y_\zeta)-F(Y_T)|^2\mid\zeta>T]
                   \le\epsilon_{N,k,\nu}.}          \tag{5.6}
\]
Here the left conditional expectation means division by exp(-kappa T).
It has not been bounded by a dropped or uniformized survival probability.
Instead the exact Markov/QSD identity cancels that factor for this
future-only functional.

A useful falsification of an independence shortcut follows at T=0:
\[
 \left|N\mathbb E_m[F(Y_0)\overline{F(Y_\zeta)}]-1\right|
                          \le\sqrt{\epsilon_{N,k,\nu}}.        \tag{5.7}
\]
This is Cauchy--Schwarz with N E|F(Y_0)|^2=1 and (5.5).
Hence the initial and collision Fourier marks are strongly correlated
at the fluctuation scale along critical sequences, even though the
collision position is independent of its lifetime. Those are different
independence statements.

## 6. Exact lifetime-resolved reduction of the original fixed-T target

Because zeta has a strictly positive exponential density, regular
conditional expectations given zeta=t exist for almost every t>0.
This uses only disintegration on the standard Borel product of the
continuous stopped path and lifetime. Alternatively each bounded
marked expectation has a Radon--Nikodym density relative to the
lifetime measure, which defines the functions below without a choice
of pointwise conditional law. Define the nonnegative measurable profile
\[
 R_{N,k,\nu}(t)
  =N\mathbb E_m\big[|F(Y_0)-e^{-at}F(Y_\zeta)|^2
                                           \mid\zeta=t\big].   \tag{6.1}
\]
It is bounded by 4N. Values on a Lebesgue-null set do not affect any
formula. Its response is evaluated at the actual lifetime t, and its
initial mark is the true initial mark of that same killed path.

Set
\[
 \mathcal B_N(k,T)
 =\int_0^\infty\kappa e^{-\kappa u}R_{N,k,\nu}(T+u)\,du
 =e^{\kappa T}\int_T^\infty
                 \kappa e^{-\kappa t}R_{N,k,\nu}(t)\,dt.        \tag{6.2}
\]
This is exactly
N E[|F(Y_0)-e^(-a zeta)F(Y_zeta)|^2 | zeta>T].
The second expression explicitly retains the rare-survival normalizer.
The first expression is an exact residual-lifetime change of variable;
it is not an unconditioned approximation.

Insert the intermediate endpoint A_T F(Y_zeta). The L2 norm triangle
inequality and (5.6) bound its difference from (1.2) by
A_T sqrt(epsilon_N,k,nu). For the response change, (3.5) gives the exact
second moment
\[
 \begin{split}
 &N\mathbb E_m[|(A_T-e^{-a\zeta})F(Y_\zeta)|^2\mid\zeta>T]\\
 &\qquad=A_T^2(1+2/N)
       \left(1-\frac{2\kappa}{\kappa+a}
                         +\frac{\kappa}{\kappa+2a}\right)
 =A_T^2(1+2/N)\frac{2a^2}{(\kappa+a)(\kappa+2a)}.     \tag{6.3}
 \end{split}
\]
Only independence of the collision configuration and lifetime was
used here. Initial/collision independence was not used. The numerator
2 and both shifted denominators matter.

Define the explicit error
\[
 E_{N,k,\nu}(T)=A_T\left[
    \sqrt{\epsilon_{N,k,\nu}}+
    \sqrt{(1+2/N)\frac{2a^2}{(\kappa+a)(\kappa+2a)}}\right].
                                                               \tag{6.4}
\]
Then the new quantitative reduction is
\[
 \boxed{\left|\sqrt{\mathcal D_N(k,T)}
                   -\sqrt{\mathcal B_N(k,T)}\right|
                  \le E_{N,k,\nu}(T).}              \tag{6.5}
\]
All quantities are actual finite-N expectations. For fixed k,
0<nu<=nu_* and all T>=0, this error is O_(k,nu_*)(N^-1/4);
the response-change part is O_(k,nu_*)(N^-1). At T=0, D_N=0
exactly, so (6.5) also gives a proved bound on B_N(k,0).

For every admitted critical sequence and fixed k,T,
\[
 \mathcal D_N(k,T)\longrightarrow0
       \quad\Longleftrightarrow\quad
 \mathcal B_N(k,T)\longrightarrow0.                 \tag{6.6}
\]
Their positive-limsup failures are equivalent by the same square-root
inequality. The earlier accepted source/modal equivalence now proves:
the full THM046 assertion for every fixed smooth real h at this same
T holds if and only if B_N(k,T)->0 for every fixed nonzero k.
A positive limsup for B_N at one admitted fixed k,T,lambda and critical
sequence would be an original-source witness through a fixed real
cosine or sine test. No such witness is asserted here.

The exact smaller first unproved inequality in this route is therefore
\[
 \boxed{\int_0^\infty c(N-1)e^{-c(N-1)u}
           R_{N,k,\nu_N}(T+u)\,du\longrightarrow0}
 \quad\hbox{for every admitted fixed }k,T
       \hbox{ and critical sequence}.                         \tag{6.7}
\]
This fixes the original horizon T; it does not replace the target by
an N-dependent time theorem. The shrinking lifetime window is part of
an exact normalized integral identity for that fixed target.

## 7. What remains correlated at the boundary

To make the residual content of (6.7) explicit, keep the response at T
temporarily and put
\[
 v_N(T)=N\mathbb E[|F(Y_0)|^2\mid\zeta>T],\qquad
 q_N(T)=N\mathbb E[F(Y_0)\overline{F(Y_\zeta)}\mid\zeta>T].
\]
The intermediate collision defect is exactly
\[
 v_N(T)+A_T^2(1+2/N)-2A_T\operatorname{Re}q_N(T).      \tag{7.1}
\]
It differs from D_N in square-root norm by at most
A_T sqrt(epsilon_N,k,nu). In particular
\[
 (7.1)\ \ge
 \left(\sqrt{v_N(T)}-A_T\sqrt{1+2/N}\right)^2.        \tag{7.2}
\]
Thus a mismatch of that conditional initial variance gives a legitimate
sufficient falsification criterion, but no mismatch has been proved.

For a fully literal label count, condition additionally on the colliding
pair being {1,2}. This pair has conditional probability 1/binom(N,2)
even on zeta>T, by (3.5). The symmetric quantities in (7.1) are unchanged
by this additional conditioning. In q_N there are the following five
classes, each expectation taken under this same conditional law:

| Initial label / collision label | Representative product | Multiplicity before division by N |
|---|---|---|
| fused / common fused coordinate | e_k(Y_1(0)) conjugate(e_k(Y_1(zeta))) | 4 |
| outside / common fused coordinate | e_k(Y_3(0)) conjugate(e_k(Y_1(zeta))) | 2(N-2) |
| fused / outside | e_k(Y_1(0)) conjugate(e_k(Y_3(zeta))) | 2(N-2) |
| same outside label | e_k(Y_3(0)) conjugate(e_k(Y_3(zeta))) | N-2 |
| distinct outside labels | e_k(Y_3(0)) conjugate(e_k(Y_4(zeta))) | (N-2)(N-3) |

The total multiplicity is N^2. At N=2 all outside classes are absent;
at N=3 the last class is absent. No nonexistent label is assigned a
value. These are two-time marked correlations, not product-Haar
integrals. The current fusion law determines neither them nor v_N(T).
Common translations show their constituent one-body means are zero,
including the initial mean under the conditioned event, but do not
factor the products.

The exact time-density version is also explicit. With
v_N(t)=N E[|F(Y_0)|^2 | zeta=t] and
q_N(t)=N E[F(Y_0) conjugate(F(Y_zeta)) | zeta=t], defined almost
everywhere, (6.1) is
v_N(t)+(1+2/N)e^(-2at)-2e^(-at) Re q_N(t).
Equation (6.7) asks for the cancellation of this nonnegative combined
quantity on the exponentially normalized tail, not for separate
smallness of its nonzero terms.

## 8. Completed proof/falsification attempt and exact failures

The positive route is complete through (6.5): reconstruct the killed
occupation measure; justify an actual collision endpoint; identify its
unmarked law; exploit iid canonical clipping only under that exact
occupation measure; retain the stopped Ito martingale; then continue
the same path beyond T and change the response time with its exact
second moment. All cutoff limits occur at fixed N,nu before any
critical limit. L=N is an auxiliary initial-law truncation parameter
in a proved deterministic probabilistic inequality, not a simultaneous
singular-SDE cutoff.

The genuinely different falsification attempt uses the fused endpoint
variance (3.6), the conditional initial variance lower bound (7.2),
and the independent finite-path/limiting-model checks. It does not use
another current construction or a generic exchangeable-law surrogate
as a counterexample. It produces no admitted positive-limsup witness.

The failed steps are recorded rather than hidden:

1. Dropping survival from (1.2) or replacing its reciprocal by a constant
   costs exp(kappa T), so it cannot control the critical fixed-T target.
   The useful cancellation in (5.6) applies only to a future-only
   functional, not to a functional containing F(Y_0).
2. Product-Haar Y_T given survival does not factor Y_0 and Y_T. Even
   initial/collision independence is contradicted by (5.7) at T=0.
3. Squaring the instantaneous iid source is invalid. For suitable fixed
   nonconstant modes its near-diagonal square has radial integral
   integral r^3 r^-4 dr and can diverge. Canonical clipping supplies
   L1 control, and the bounded endpoint plus martingale controls L2
   only after integration to collision.
4. Attractive individual-force squares also fail Haar integrability.
   The proof uses the L1 drift to construct Y_zeta and the bounded
   one-body gradient for its martingale bracket; it never extracts
   pair-force control from a total-force identity.
5. The unconditioned estimate (5.5) controls a typical lifetime of order
   1/N. It does not control (6.7) after a fixed positive T. The scalar
   nonnegative profile R_N(t)=1_(t>=T0), with fixed T0>0, has its
   exponential average at zero equal exp(-kappa T0) while its average
   at T0 equals one. This is a counterexample to the proposed inference,
   not an admitted particle counterexample.
6. A conditional Brownian integral over the full interval [0,T] need
   not be centered or obey conditional isometry when conditioned on
   future survival. Formula (5.3) is used under the unconditioned
   stopped law; Markov/QSD transfers the complete future functional.
7. Extending (5.7) uniformly from typical to fixed positive lifetime
   would be the first unjustified step in a purported full proof.
   Precisely the weighted initial marks in (7.1), or their combined
   lifetime profile (6.7), are missing. No local equilibrium, pressure,
   mixing, entrance-law regularity, or hierarchy truncation is presumed.

These failures demote concrete shortcuts and leave a smaller exact
boundary criterion. They neither prove nor disprove THM046.

## 9. Solvable models, finite coefficients, and adversarial self-review

For the local two-particle Euclidean attractive principal kernel, the
relative coordinate has drift -4z/(N|z|^4) and diffusion generator
2 nu Delta. At zero noise its exact radial solution is
r(t)^4=r(0)^4-16t/N until collision, with
zeta=N r(0)^4/16. At N=2 this gives zeta=r(0)^4/8.
In d=4 a uniform four-ball has uniform r(0)^4, so this local model has a
constant short-time collision flux; it does not have the global
periodic exponential lifetime law. The inward flux is
4|S^3|/N=2c/N for one pair, agreeing with (2.2).
The center is constant and
F=e_k(center) cos(pi k.z), so its change at absorption is of order
r(0)^2. This tests the qualitative gain from integrating the singular
source to collision. Zero noise and this local model are diagnostics
only, never an admitted critical witness.

With positive noise, direct radial differentiation gives
L_rel(r^4)=48 nu r^2-16/N and bracket density 64 nu r^6.
These verify both relative Brownian factors. Finite N=2 and N=3 are
checked without nonexistent third/fourth labels.

The fresh standard-library diagnostic in the packet independently
enumerates finite-label sums, canonical complex and real clipping
examples on a finite cyclic probability space, one-pair fusion moments,
the five marked-correlation multiplicities, and the exact response
Laplace integrals. An explicit finite sub-Markov chain with uniform
left eigenmeasure tests lifetime/mark independence, full survival
normalization, reversed endpoint orientation, and failure of
future-conditioned martingale centering. It is a diagnostic model,
not the singular SDE or a critical counterexample. Deliberately wrong
formulas are required to produce nonzero witnesses. No old checker
was read or adapted, no random seed or dependency was used, and no
numerical SDE was simulated. The executed diagnostic passed 3,845 exact assertions in 41 categories,
including 20 required nonzero mutation witnesses. Complete results and all
execution failures/corrections are recorded in the packet.

The strongest new assertion received the following hostile self-check.
This is not independent review.

| Challenge | Disposition |
|---|---|
| Could the maximal attractive path lack a collision limit? | (3.1) gives almost-sure finite total drift variation, while Brownian paths are continuous at the finite lifetime. |
| Is the collision flux merely formal? | A globally smooth test, genuine stopped Ito passage and (2.2) produce a finite Borel measure; no unknown trace of a semigroup is integrated. |
| Is clipping no longer canonical? | Both rows and the double mean are restored; (4.5) uses the exact projected kernel. |
| Is the square of a time integral estimated by an infinite instantaneous square? | No. (5.4) uses a bounded endpoint and the true stopped martingale. |
| Does conditioning on survival alter the Brownian law? | Yes; the proof transfers an entire future path functional by Markov/QSD instead of asserting unchanged conditioned Brownian increments. |
| Is survival silently replaced by a short-time event? | No. (6.2) gives both the exact rare normalizer and its exactly transformed lifetime integral. |
| Does the response use T, T+u, or zeta inconsistently? | The original uses T; the boundary profile uses zeta; (6.3) is the exact price of that change. |
| Is the fusion endpoint independent of the initial configuration? | No. Its retained correlation is the entire remaining criterion; (5.7) explicitly rules out a general independence shortcut. |
| Does an N-dependent lifetime window violate the fixed-T target? | The window is an exact integral representation at the same fixed T, and only its full average is declared target-equivalent. |
| Are endpoint and martingale cross terms omitted? | No; (5.4) controls the nonzero cross contribution through Cauchy--Schwarz. |
| Is a self-check called an independent gate? | No. Root must run the two complete fresh axes and compare them. |

## 10. Recoverable handoff and verification

The report and packet preserve all 17 exact inputs, the original manifest,
complete exposure/read history, this full proof, fresh diagnostic source
and complete results, run/failure history, README, safe regular-member
inventory, output digests and a portable read-only verifier. The report,
packet and named sibling archive/seals are the only outputs. They are
issued read-only; corrections require a distinct issuance.

| Item | Disposition |
|---|---|
| Original THM046 / THM049 critical cancellation | OPEN; no actual-law witness found. |
| D28-A collision endpoint and exact unmarked law | Derived here from the reconstructed killed mechanism; SELF_CHECKED. |
| D28-B canonical iid source bound | Quantitative proved candidate; SELF_CHECKED. |
| D28-C post-survival-to-collision mode error | Quantitative proved candidate with explicit finite-N bound; SELF_CHECKED. |
| D28-D lifetime-resolved original-target reduction | Exact quantitative reduction; SELF_CHECKED; uses accepted R25 equivalence and reconstructed R27 duality. |
| D28-E typical initial/collision covariance | Proved auxiliary consequence, with rare-tail limitation; SELF_CHECKED. |
| First unsupported line | (6.7), equivalently cancellation of the marked terms in (7.1); retain exact original initial law and fixed k,T. |
| External/private source requirement | None for this result. |
| Canonical state, source edits, commits, pushes, remotes | None; root owns integration and any promotion. |

No TeX source was changed, no dependency installed, and no child was
spawned. The final handoff contains no mathematical LaTeX. The concrete
next mathematical task is to estimate or falsify the combined
first-collision profile in (6.7), after independently auditing the
full new quantitative argument, rather than repeating the unmarked
lifetime identity.
