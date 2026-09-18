# AUD074 / TASK115 — whole THM051 hostile review

Issued 2026-09-18 UTC. Fresh isolated hostile context assigned Astra Max.
Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r026-overlap-hostile.
The task supplies branch codex/hocf-r026-overlap-hostile and provisioned base
ef438b612f732d21af1fa1756dd7559ef63c6d61; these metadata were not independently
read. All 15 allowed inputs were individually SHA-256 verified before
mathematical use and copied exactly into this audit packet.

**Whole mathematical verdict: PASS for the entire frozen THM051(A)–(D),
including its auxiliary actual-pair estimates and the mathematical
assertions in the complete TASK111 report. No failed mathematical line,
counterexample to the frozen conjunction, repair, change of quantifiers,
or silent replacement premise was found.**

This is one independent hostile-review axis. It does not promote a campaign
status, certify its own diagnostics as proofs, verify the constructor's
unavailable diagnostic history, establish the remaining three-label
cancellation, or certify THM049's L1/L2 equivalence. Root owns comparison with
the separate reconstruction axis, exact accepted source-gate matching and
integration.

## 1. Exact scope, negation and separate verdicts

The model is precisely the coefficient-one, mean-zero Coulomb kernel on the
unit four-torus, Fourier coefficient |m|^-2 for m nonzero, force minus its
gradient, ordered interaction coefficient 1/N, independent Brownian noise
sqrt(2 nu), and initial iid unit Haar independent of the drivers. Here N is
every integer at least two and nu is positive and finite. No altered
preparation, equilibrium replacement, positive-time product law, untruncated
source L2 premise, current/initial density or new UI theorem is used.

The mode k is a fixed nonzero integer vector. The A/B auxiliary bounds are
at each deterministic finite time with constants uniform in N, time and
positive diffusivity. Their spatial cutoffs have exactly the frozen domains.
The C/D bounds are uniform on each fixed finite horizon and each fixed
positive finite critical window for beta/sqrt(N). A limiting critical
sequence enters some such window eventually; finite initial segments do not
change any asymptotic equivalence.

| Clause | Verdict | Exact load-bearing content |
|---|---|---|
| A | PASS | Actual energy sign, positive heat decomposition, N/(N-1), self diagonal g_r(0)/(N-1), coupled estimate, and small-ball term R^4+N^-1. |
| B | PASS | True heat response, zero Haar rows, smooth diagonal, L1 cutoff error, logarithmic truncated square with 1/(N r^2), all Fourier coefficients and their r/8 comparison, literal overlap self subtraction. |
| C | PASS | Current overlap at most C N^-1/2 and mixed overlap at most C N^-1/4 sqrt(1+log N), with the specified uniformity and genuine integrability. |
| D | PASS | Exact two-/three-label splitting, unchanged three-label weights, quantitative two-label error, vanishing and positive-limsup equivalences on the same fixed data; zero three-label term at N=2. |
| Complete TASK111 mathematical assertions | PASS | Definitions, source mechanisms, auxiliary claims, finite-N modal identity, signed-negative-part statement and the one-way ancillary L1-failure implication are checked below. |
| Whole conjunction and exact negation | PASS / no admitted negating witness | The negation remains a violation of a stated clause or its coefficients/domains/uniformity, not proof failure or an excluded-law example. |

First failed mathematical line: **none**. This conclusion uses the literal
claim; no row is weakened to a stopped process, a smooth physical dynamics,
a finite frequency range, a time depending on N, or a merely formal
calculation. There are separate evidence limitations in Section 9.

## 2. Kernel and actual-law source reconstruction

References here locate allowed mathematical text, not an assertion that its
printed historical status is currently accepted. The source mechanisms used
from R1, R4, R6, R10 and R16 have been recomputed in the precise d=4,s=2 row.

Set c=4 pi^2 and let p_u be the periodized Euclidean heat kernel. Fourier
integration gives
\[
 g=c\int_0^\infty(p_u-1)\,du,\qquad
 \widehat g(m)=|m|^{-2}\quad(m\ne0).
\]
The central Gaussian integral has coefficient one:
\[
 c\int_0^\infty(4\pi u)^{-2}e^{-|z|^2/(4u)}\,du=|z|^{-2}.
\]
The noncentral small-time terms have integrable differentiated Gaussian
bounds on a fixed ball; subtracting the Euclidean integral at large time
also has integrable derivatives. Consequently g=|z|^-2+H locally, with H
smooth; g is smooth off zero and bounded below by a finite g_*<0. The force
is odd, locally 2z/|z|^4 plus a smooth field, and is integrable.

The flux through a small sphere is 2|S^3|=4 pi^2. The zero Fourier
coefficient supplies the compensating Haar term:
\[
 \operatorname{div}K=c(\delta_0-dz),\qquad
 \Delta g=c\ \hbox{only off zero}.
\]
Thus using the punctured equality in a stopped particle energy calculation
is legitimate; using it in a Haar response integral without its atom would
be wrong. The report uses the two formulas in the correct places.
R4 lines 69–109 and 111–190, R16 Sections 2–3, and TASK111 lines 139–151
agree with these constants.

Write H_N=N^-1 sum_{i<j}g(x_i-x_j). Differentiating both coordinates of each
unordered pair gives B=-grad H_N and Delta_{4N}H_N=c(N-1) off collisions.
The shift
\[
 Y=H_N-(N-1)g_*/2
\]
is a sum of nonnegative pair energies, and tends to infinity at every
partial collision. Its sublevels are compact subsets of the collision-free
configuration space. Local smooth cutoffs of the drift therefore patch a
pathwise unique local solution. For the exit tau_R of Y below height R,
smooth stopped Ito gives
\[
 H_N(X_{t\wedge\tau_R})+
 \int_0^{t\wedge\tau_R}\sum_i|B_i|^2du
 =H_N(X_0)+\nu c(N-1)(t\wedge\tau_R)+M_R(t),
\]
\[
 \langle M_R\rangle_t=2\nu\int_0^{t\wedge\tau_R}\sum_i|B_i|^2du.
\]
If the initial energy is already above R, the stop is zero. This covers
unbounded iid initial energy without assuming its second moment. The
stopped martingale integrand is bounded on the applicable sublevel, and
\[
 \mathbb P(\tau_R\le T)
 \le [\mathbb EY(X_0)+\nu c(N-1)T]/R.
\]
The finite mean of Y(X_0) follows from Haar integrability of g. Energy
sublevels prevent every finite-time collision or nonextendible endpoint.
After noncollision, Fatou yields finite expected complete-force action.
Stochastic isometry gives convergence of M_R to the true martingale in L2;
localization supplies the pathwise identity, whose terms are now
integrable. Taking expectations gives exactly
\[
 \mathbb EH_N(X_t)+\mathbb E\int_0^t\sum_i|B_i|^2du
       =\nu c(N-1)t.                                      \tag{H1}
\]
This checks TASK111 (2.2)–(2.3), including its unstopping. The full drift
square is retained. No integrability of individual force squares at initial
time, cancellation of their cross terms, or initial energy variance was
inserted. R6 lines 240–345 and R16 Section 3 supply the same stopped-to-true
mechanism.

The additional sign \(\mathbb EH_N(X_t)\le0\) does not follow just from H1.
At a fixed physical heat cutoff delta and fixed N,nu,T, the smooth density
F_delta starts from one and is positive and smooth. Its exact periodic
free-energy calculation is
\[
 \frac d{dt}\left(\nu\int F_\delta\log F_\delta+
                  \int H_{N,\delta}F_\delta\right)
 =-\int F_\delta|\nabla H_{N,\delta}+
                       \nu\nabla\log F_\delta|^2\le0.
\]
Both initial terms vanish. Entropy is nonnegative on mass-one Haar space,
so the smooth energy mean is at most zero. Every noncolliding singular
path has positive minimum separation on a compact horizon. Heat forces
converge locally in C1 away from collisions; under the same-noise coupling,
Gronwall up to one quarter of the singular minimum separation yields
uniform path convergence and prevents this comparison stop for small delta.
The heat energies have the common fixed-N lower bound (N-1)g_*/2. Fatou
after this shift gives
\[
                  \mathbb EH_N(X_t)\le0.                  \tag{H2}
\]
There is no limit interchange with N or nu and no passage of a singular
Fisher-information identity. This verifies TASK111 (2.4) and the relevant
parts of R10 Section 2 and R16 Section 3.

Permutation equivariance gives exchangeability. Common translation
equivariance and Haar preparation give Haar one-body marginals, without
giving a product pair law. Exchangeability and H2 imply
\[
 \mathbb E g(X_1-X_2)\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|.                            \tag{H3}
\]
The local bound |j_k(x,y)|<=C_k(1+dist(x-y,0)^-2), together with the
local form of g, proves a uniform bound for E|j_k(X_1,X_2)|. All four
expectations A2,A3,B2,B3 are consequently absolutely integrable in time
whenever their labels exist. This includes the initial-phase factors,
which have modulus one. No current/initial density is needed.

## 3. Clause A: coupled estimate and current-pair small balls

For every 0<r<=1 the exact off-zero splitting is
\[
 g=g_r+q_r-cr,\qquad
 q_r=c\int_0^r p_u\,du\ge0,\qquad
 a_r(m)=|m|^{-2}e^{-cr|m|^2}\ (m\ne0).
\]
At fixed r the smooth Fourier series is absolutely convergent and
\[
 0\le g_r(0)=\sum_{m\ne0}a_r(m)\le C/r.
\]
The estimate follows by integrating the four-dimensional on-diagonal
heat bound from r to one and the exponentially decaying remainder after
one. It is uniform throughout the stated r domain.

For each configuration, the ordered empirical sum contains N smooth
self terms; exchangeability therefore gives
\[
 \mathbb E g_r(X_1-X_2)
 =\frac{N}{N-1}M_r-\frac{g_r(0)}{N-1}.
\]
Both M_r and E q_r are finite: the former is bounded by g_r(0), and the
latter is controlled by H3 and the bounded smooth g_r. Substitution in
H3 yields exactly
\[
 \frac N{N-1}M_r+\mathbb E q_r(X_1-X_2)
 \le\frac{g_r(0)}{N-1}+cr.                                  \tag{H4}
\]
The two terms on the left are nonnegative for explicitly different
reasons: positive Fourier weights and a positive heat kernel. Thus
\[
 M_r+\mathbb E q_r(X_1-X_2)
 \le C((Nr)^{-1}+r)
\]
since N/(N-1)>=1 and (N-1)^-1<=2/N. This checks the stronger coupled
version in the frozen card, not merely two unrelated marginal estimates.

For 0<R<=R0<1/8 and dist(z,0)<=R, the central Gaussian integrated over
u in [R^2/2,R^2] is at least a fixed positive constant times R^-2.
Hence q_{R^2}(z)>=c0 R^-2. Markov's inequality and H4 at r=R^2 give
\[
 \mathbb P(\operatorname{dist}(X_1-X_2,0)\le R)
 \le C R^2((NR^2)^{-1}+R^2)
 =C(N^{-1}+R^4).                                           \tag{H5}
\]
The bound holds at every deterministic time uniformly in positive nu.
It is neither a pathwise minimal separation statement nor an improved
R^4 estimate below the microscopic scale. The N^-1 term is indispensable
to the subsequent quantified estimate.

These computations verify TASK111 lines 217–271 and all of clause A.

## 4. Clause B: literal cutoff, row response and truncated square

Let d=d_{k,r}=c exp(-r ell_k). The full smooth divergence is c(p_r-1).
Convolution or Fourier integration gives
\[
 \int J_{k,r}(x,y)\,dy=-d e_k(x),\qquad
 \iint J_{k,r}=0.
\]
Therefore both Haar rows of j_{k,r}=J_{k,r}+d(e_k(x)+e_k(y))
vanish. At the smooth diagonal J_{k,r}(x,x)=0, so its centered
diagonal is exactly 2d e_k(x). The singular j_k is never assigned a
diagonal value. Substitution of c for d at positive r would fail the
row identity.

For every Gaussian translate, dist(z,0)<=|z+n|. Differentiation and
the scalar Gaussian bound give
\[
 \operatorname{dist}(z,0)|\nabla p_u(z)|\le C p_{2u}(z).
\]
Because the phase-gradient difference is at most C_k dist(x-y,0),
integration from zero to r yields
\[
 |J_k-J_{k,r}|\le C_k q_{2r}(x-y),\qquad
 |c-d|\le C_k r.
\]
Using H4 at 2r is legal for r<=1/2, and gives exactly
\[
 \mathbb E|j_k(X_1,X_2)-j_{k,r}(X_1,X_2)|
 \le C_k(r+(Nr)^{-1}).                                     \tag{H6}
\]
The background error is present; this is an observable cutoff on the
actual dynamics. No physical-law approximation is now being tied to N.

The central retained Euclidean potential is
\[
 R^{-2}(1-e^{-R^2/(4r)}).
\]
Differentiating gives, with u=R^2/(4r),
\[
 R|K_r^{\rm Eucl}|=
 2R^{-2}[1-(1+u)e^{-u}].
\]
The bracket equals \(\int_0^u v e^{-v}dv\), hence is bounded by both one
and u^2/2. Noncentral and large-time derivatives are bounded uniformly
in a fixed small r domain. Including the row terms,
\[
 |j_{k,r}(x,y)|\le C_k[1+\min(r^{-1},R^{-2})]                 \tag{H7}
\]
through the smooth diagonal and on the rest of the torus.

The squared bound reduces to E min(r^-2,R^-4). Above R0^-4, H5 gives
P(R^-4>v)<=C(v^-1+N^-1). Layer cake from that fixed threshold to r^-2
therefore gives
\[
 \mathbb E|j_{k,r}(X_1,X_2)|^2
 \le C_k[1+\log(1/r)+(Nr^2)^{-1}].                          \tag{H8}
\]
If the upper endpoint is below the fixed threshold, its contribution is
absorbed into the constant. Thus no unmentioned requirement r<R0^2 is
needed in the stated fixed r0 interval. This argument preserves the
finite-N term at every positive cutoff and proves no square integrability
after taking r to zero at fixed N.

This checks every pointwise and moment assertion in TASK111 lines 291–356.

## 5. Clause B: all Fourier coefficients and all-frequency comparison

Multiplying j_{k,r}(x,y) by the conjugate phase at x leaves a function
of z=x-y. With a_r(0)=0, the force term is
\[
 c\sum_m(k\cdot m)a_r(m)[e_m(z)-e_{m-k}(z)].
\]
The row correction adds d[1+e_{-k}(z)]. Therefore its coefficient is
exactly
\[
 b(m)=c[(k\cdot m)a_r(m)-(k\cdot(m+k))a_r(m+k)]
       +d(1_{m=0}+1_{m=-k}).
\]
At m=0 and m=-k the response cancels the corresponding force coefficient,
giving b(0)=b(-k)=0. Absolute summability follows from Gaussian decay.
Summing the force difference telescopes, so
\[
                       \sum_{m\ne0}b(m)=2d.               \tag{H9}
\]
This independently recovers the same diagonal.

Here is a quantified check of the all-frequency comparison. For
|m|>=2|k| put F_r(x)=x|x|^-2 exp(-cr|x|^2), and use the segment
x=m+theta k. It obeys |x|>=|m|/2. The operator norm of the derivative
of x/|x|^2 is |x|^-2, so
\[
 |DF_r(x)|\le(4|m|^{-2}+2cr)e^{-cr|m|^2/4}.
\]
The delta corrections vanish in this range. With u=cr|m|^2, mean
value and multiplication by c|k| give
\[
 \frac{|b(m)|}{a_{r/8}(m)}
 \le c|k|^2(4+2u)e^{-u/8}\le 8c|k|^2.                      \tag{H10}
\]
The final scalar maximum is 16 exp(-3/4)<8. For the remaining nonzero
integer m there are finitely many vectors depending only on k.
Their a_{r/8}(m) are bounded below uniformly for 0<r<=r0<=1/2,
and their numerators are bounded above; the response deltas are included.
This proves the entire comparison with a finite C_k. It does not use
a false uniform ratio between adjacent Gaussian weights at the same r.

For an exchangeable law the exact empirical identity is
\[
 \mathbb E e_m(X_1-X_2)
   =\frac{N\mathbb E|Z_m|^2-1}{N-1}.
\]
This does not require product law or positivity of the overlap multiplier.
Using the absolutely convergent series and H9 gives
\[
 A_{2,r}=\frac N{N-1}\mathbb E\sum_{m\ne0}b(m)|Z_m|^2
                 -\frac{2d}{N-1}.                        \tag{H11}
\]
All coefficients in TASK111 (5.1)–(5.4) and THM051(B) are correct.
H10, H4 at r/8 and H6 then imply
\[
 |A_2(t)|\le C_k[r+(Nr)^{-1}]+2c/(N-1).                    \tag{H12}
\]
This completes clause B as well as the current half of clause C.

## 6. Clause C: tagged displacement and the mixed-time comparison

The same positive heat splitting gives the configurationwise floor
\[
 H_N\ge\frac N2\sum_{m\ne0}a_r(m)|Z_m|^2
                -\frac12g_r(0)-\frac{N-1}{2}cr.
\]
With r=N^-1/2 it is H_N>=-C sqrt(N). Combining with H1 and
exchangeability, for each fixed tag i,
\[
 \mathbb E\int_0^T|B_i|^2dt\le C N^{-1/2}+c\nu T.           \tag{H13}
\]
A consistent Euclidean lift changes by integral B_i plus sqrt(2nu) W_i.
Cauchy–Schwarz in time and the L2 Brownian maximal inequality imply
\[
 \mathbb E\sup_{t\le T}\operatorname{dist}(X_i(t),X_i(0))^2
     \le C_T(N^{-1/2}+\nu).                               \tag{H14}
\]
For example, the left side is bounded by
2T E integral |B_i|^2+4nu E sup|W_i|^2, and
E sup|W_i|^2<=4dT. H13 always involves the full drift square;
there is no decomposition into inadmissible individual force squares.

The exact difference B2-A2 has integrand j_k(X1(t),X2(t)) times the
difference of the two conjugate phases at tag one. Truncate only j.
The L1 replacement error is at most twice H6. Cauchy–Schwarz for the
two random variables, H8 and the Lipschitz bound for e_k yield
\[
 |B_2-A_2|
 \le C_k[r+(Nr)^{-1}]
 +C_{k,T}[1+\log(1/r)+(Nr^2)^{-1}]^{1/2}
                      (N^{-1/2}+\nu)^{1/2}.              \tag{H15}
\]
No independence, conditional law, or joint density is inserted.

Choose a fixed positive r_* small enough for every cutoff domain and put
r=r_* N^-1/2. Then r+(Nr)^-1 is C N^-1/2 and
1+log(1/r)+(Nr^2)^-1 is at most C(1+log N). H12 gives
\[
 \sup_{t\le T}|A_2(t)|\le C_k N^{-1/2}.
\]
On the whole specified critical window,
nu<=lambda_-^-1 N^-1/2. H15 gives
\[
 \sup_{t\le T}|B_2(t)|
       \le C_{k,T,\lambda_-}N^{-1/4}\sqrt{1+\log N}.
\]
No asymptotic use was needed to cover small N. Dependence on lambda_+
is allowed but unnecessary for these bounds. At T=0 both overlaps vanish
by iid Haar centering. All absolute time integrability was already
established by H3, before any Fourier/time manipulation.

The mixed estimate is too large after the order-N three-label
multiplicity. The report correctly refrains from claiming that its same
argument settles the triple term.

## 7. Clause D and the exact finite-N mode calculation

Distributional Haar integration with the atom retained gives
integral J_k(x,y)dy=-c e_k(x) and zero double integral. Direct ordered
counting then gives
\[
 P_N[J_k]=U_N^k+(c/N)Z_k,\qquad
 dZ_k=-\widetilde a_k Z_k\,dt+U_N^k\,dt+dM_k,
 \qquad \widetilde a_k=c(1-1/N)+\nu\ell_k.
\]
The residual has positive sign. The complex brackets are
\[
 d\langle M_k,\overline{M_l}\rangle_t
      =(2\nu/N)c(k\cdot l) Z_{k-l}(t)\,dt .
\]
At l=k, Z0=1. The smooth mode has bounded gradients; its martingale
passes directly through collision-excluded stopping in L2, while the
source drift passes using H3 in L1. No derivative of the singular
source is used.

In N U_N^k times the conjugate empirical mode there are 2N(N-1)
triples where the conjugate tag is one of the pair and
N(N-1)(N-2) triples with three different tags. The common denominator
is 2N^2. Exchangeability and symmetry identify the overlap terms, for
either current or initial conjugate tag. Thus the F_N,G_N definitions
with weights (N-1)/N and (N-1)(N-2)/(2N) are exact.

Set V=N E|Z_k(t)|^2 and R=N E[Z_k(t) conjugate Z_k(0)].
The product identities are
\[
 V'=-2\widetilde a_kV+2\nu\ell_k+2\Re F_N,\qquad
 R'=-\widetilde a_kR+G_N,\qquad V(0)=R(0)=1.
\]
The initial variable is measurable in the initial filtration; independence
of initial and final states is unnecessary. Solving these integrable
scalar equations gives
\[
 N\mathbb E|Z_k(T)-A_k Z_k(0)|^2
 =(e^{-\widetilde a_kT}-e^{-a_kT})^2
 +\frac{\nu\ell_k}{\widetilde a_k}
                  (1-e^{-2\widetilde a_kT})
 +2\Re\mathcal R_N.                                      \tag{H16}
\]
This checks every coefficient and weight in TASK111 (7.1)–(7.5),
including the factor two in the current variance equation.

Since \(\widetilde a_k\ge c/2\), the first explicit term is at most
(cT/N)^2 and the second is O_k(nu), uniformly on each fixed horizon.
On a critical window their orders are N^-2 and N^-1/2. H16 therefore
forces the negative part of Re Rcal_N to vanish. This justifies the
positive-limsup formulation of the admitted signed-target negation,
without using THM049's L1/L2 equivalence.

Insert the two label-count terms into the definition of Rcal_N. The
two-label part contains exactly (N-1)/N times the integral involving
A2 and B2. The three-label part contains exactly
\[
 \frac{(N-1)(N-2)}{2N}\int_0^T
 \left[e^{-2\widetilde a_k(T-t)}A_3(t)
       -A_ke^{-\widetilde a_k(T-t)}B_3(t)\right]dt.
\]
The weights have modulus at most one, and Section 6 proves
\[
 |\mathcal R_N^{(2)}|
       \le C N^{-1/4}\sqrt{1+\log N}.
\]
At N=2 the triple sum is empty and the specified three-label part is zero.
At T=0 all time integrals and H16 vanish. Along every admitted critical
sequence the real difference Rcal_N-Rcal_N^(3) tends to zero. Hence both
vanishing and positive-limsup assertions are equivalent for the same
fixed data. This equivalence needs no separate A3/B3 bound and no
interchange of a limit with the signed integral.

The first still-open line is the original weighted three-distinct-label
signed cancellation displayed as TASK111 (7.6). An open remaining target
is not a failure of any clause of THM051.

## 8. Complete-report ancillary assertion audit

The following table accounts for the full report, including assertions
beyond the quantitative final conjunction. Line numbers refer to the
exact hashed MEMORANDA/ROUND_026_CORRELATION_FALSIFICATION.md.

| Location | Mathematical content and disposition |
|---|---|
| 7–28 | Quantitative two-label cancellation and reduction only: PASS by H12–H16. Original target/witness remain open; no broader conclusion follows. |
| 30–79 | Model, definitions, weights, fixed signed target and positive-limsup negation: PASS. The asymptotically negligible negative part is proved in H16, not assumed. |
| 81–98 | Literal original P statistic, preserved response/scale, original-source target and negation, finite beta<1 segment: correctly transcribed from THM046. No resolution or full equivalence is claimed. |
| 100–127 | Complete uniform-window quantitative conjunction and its negation: PASS with every stated parameter and N domain. |
| 139–215 | Kernel normalization, full divergence, actual noncollision/action/free-energy sign, exchangeability, one-body Haar and absolute integrability: PASS as reconstructed in Section 2. |
| 217–289 | Positive heat splitting, both coupled terms, deterministic-time small balls, configuration floor and tagged displacement: PASS. No pathwise separation or singular variance conclusion is made from the pair bound. |
| 291–356 | Literal heat response, cutoff error, retained Euclidean potential/force, global source envelope, layer cake and exact cutoff balance: PASS in Section 4. |
| 358–419 | Spectral coefficient, its two zero coefficients, total self mass, full-frequency comparison, exact empirical overlap: PASS in Section 5. |
| 420–448 | Mixed difference and Cauchy–Schwarz with actual displacement: PASS; no independence or two-time density premise. The analogous coarse triple estimate is insufficient after multiplication by N. |
| 450–516 | Finite-N stochastic mode equations, brackets, label multiplicities, scalar endpoint identity, explicit orders and equivalences: PASS in Section 7. |
| 517–520 | One-way original-source L1 failure to an endpoint L2 defect and then a positive triple remainder: PASS with the mode-to-smooth detail reconstructed below; this does not assert the converse or a UI theorem. |
| 524–531 | Infinite initial singular-source second moment and the limited near-collision failure-mechanism interpretation: PASS as checked below. Only a two-label contribution is ruled out. |
| 544–551 | Logarithmic radial majorant and finite-N-atom diagnostic mechanisms are mathematically valid; their claimed original execution is separately unverified. |
| 569–583 | Every stated limit of the argument is consistent with the proof. In particular Gaussianity, general preparation, triple closure and new L1 equivalence are absent. |
| 584–601 | Open/partial/status distinctions and the identified next mathematical line are consistent. A new independent audit status is root's action. |
| 131–138, 533–543, 553–567, 603–611 | Provenance, execution counts, packaging and exposure assertions are evidence/history claims, separately disposed of in Section 9; they are not proof premises. |

For the one-way assertion at lines 517–520, a single complex mode has
the original backward identity
\[
 S_N^k:=\int_0^T P_N[J^{Q_{T-t}e_k}](X_t)dt
       =Z_k(T)-A_kZ_k(0)-M_N^{k,\mathrm{back}} .
\]
Its scaled noise square is
\[
 N\mathbb E|M_N^{k,\mathrm{back}}|^2
   =2\nu\ell_k\int_0^T e^{-2a_k(T-t)}dt
   \le2\nu\ell_k T=o(1).
\]
Thus positive original-source scaled L1 limsup for this fixed mode gives
positive endpoint L2 limsup by the triangle inequality and Jensen.
H16 and the two-label estimate then give a positive triple limsup
along a subsequence.

For an arbitrary fixed smooth real h, the reduction to one fixed mode
requires a uniform tail bound, and is not inferred just from formal
Fourier expansion. The allowed R16 mechanism supplies the needed bound
without its broader theorem being adopted by label. In its Sections
4–7, specialize alpha=1, M=6 and L=2(alpha+M)=14. The retained positive
weights have logarithmic derivative at most L; its vector divided
difference is bounded by
\[
 (1+L)|q|(1+|q|)^{L/2+1}
                    \sqrt{a_r(p)a_r(p-q)} .
\]
The proof follows by integrating the radial logarithmic derivative,
using the triangle inequality, then discrete Cauchy–Schwarz in p.
Consequently the retained source is bounded by its positive Fourier
energy times a constant controlled by
\(\sum_q(1+|q|)^{10}|\widehat h(q)|\).
Its discarded source is bounded by a positive heat remainder, including
the original two Haar contractions; the same actual energy sign bounds
both. At r=N^-1/2 this proves, uniformly on the critical tail,
\[
 \sqrt N\,\mathbb E|S_N^q|\le C_T(1+|q|)^{10}.
\]
The exact multiplier of the backward test is bounded by one, so no
growth with N enters this seminorm. Smooth Fourier tails are summable
against this polynomial. The triangle inequality first discards a
uniformly small tail, then a positive limsup for the finite sum forces a
positive limsup for at least one fixed mode along a subsequence. This
checks the report's abbreviated one-way ancillary statement explicitly.
It neither invokes the candidate UI theorem nor supplies its converse.
Only this specialized source-majorant mechanism of R16 was checked;
there is no certification of all of R16 or THM049 by this audit.

For the initial source square, put z=x-y=R theta. Direct expansion gives
\[
 j_k(x,x-z)
   =-2c\,e_k(x)(k\cdot\theta)^2R^{-2}+O_k(R^{-1})+O_k(1).
\]
On a cone where |k dot theta|>=|k|/2 the leading coefficient is nonzero.
Initial iid Haar therefore gives a divergent radial integral
of R^3 R^-4 near zero. Thus E|j_k(X1(0),X2(0))|^2 is indeed infinite
for nonzero k. This does not obstruct H6–H8, which square only a strictly
positive-cutoff observable.

The solvable radial majorant used in the fresh audit has radii R=2^-j
with mass (15/16)16^-j. At r=4^-L its truncated R^-4 mean is exactly
1+15L/16. Adding mass 1/N at a radius below sqrt(r) gives a term
1/(N r^2). These are static majorant diagnostics, not claimed actual
particle-law counterexamples. They justify the significance of the two
terms whose omission was challenged.

## 9. Evidence, transcription and independence dispositions

All 15 input hashes and their copies passed. The whole constructor report
was displayed; one initially truncated combined tool output was followed
by a bounded reread covering its entire omitted spectral section. A
second combined source output truncated part of R6; a bounded reread
covered all of that range. Neither truncation is hidden as complete
display. Exact read ranges and every tool/test result are recorded in
EXPOSURE_AND_SOURCES.md and RUN_HISTORY.md in the packet.

The constructor's claim of 343,521 assertions, 15 mutation controls,
successful original packaging and a corrected comparison-harness failure
was **not independently verified**: its code, results, archive and history
are deliberately not allowed inputs. The copied exposure record is a
source's statement about itself. It is not evidence that this audit
observed those executions. These limitations are historical/evidentiary,
not a mathematical counterexample or a repair of THM051.

The fresh audit diagnostic was written from the independently recomputed
identities. It passed **187,032 assertions in 25 categories and 20 distinct
nonzero mutation controls**. It uses exact Gaussian rational arithmetic
for finite Fourier kernels, literal pair/triple sums, response rows,
energy/self subtraction, brackets, Cauchy–Schwarz and scalar modal algebra.
Five values N=2,3,4,5,6, four nonzero modes, two even positive finite
Fourier spectra and two configuration variants are included. The common
factor c is divided out only in those explicitly smooth algebra tests.

A separate finite double-precision heat sweep checks all nonzero
m in [-4,4]^4, those four modes, and seven scales from 1/2 to 2^-30.
For the high-frequency range its maximum normalized ratio was
2.777844181806905, below the analytic bound eight in H10. The finite
low-frequency set reached 53.06292625155662; the proof correctly treats
it separately and does not assert the high-frequency bound there.
This sweep supports H10; it does not prove the all-frequency inequality.

All 20 mutation controls have a literal nonzero witness in the saved
result. They alter the heat response, row centering, three versions of
the overlap self subtraction, empirical factor, overlap/triple
multiplicities, initial phase, ordered half, falling-factorial
normalization, two residual-row terms, energy diagonal, split constant,
positive q term, logarithmic/cutoff terms, and two endpoint response
coefficients. These are deliberately failed alternatives, not failures
of the correct mathematical assertions.

The first mathematical diagnostic execution passed; the final read-only
package verifier also reran it and compared the saved mathematical results.
An earlier
file-creation request was rejected by the patch parser before any file
was created; the exact tool error and its nonmathematical disposition
are preserved. No constructor diagnostic, code, result/history, current
blind narrative, canonical STATE, other worktree, memory file or
nonallowlisted link was read. Ambient app/global text and a memory summary
were present in the inherited context but supplied no mathematical
premise. No child was created. The parent task and my outbound status
messages are recorded; no current audit result was received or used
before this verdict.

## 10. Issuance and recoverable handoff

The packet contains all 15 exact input copies, original manifest, initial
and final input checks, this report, the source/exposure record, fresh
diagnostic and its complete stdout/stderr/process result, failure/history
record, README and a portable read-only verifier. Named sibling inventory,
archive and SHA-256 seal files cover every regular packet member and the
issued report. The verifier checks safe names/types, complete member
sets, sizes/digests, input copy identity, report-copy identity and archive
identity without extraction or writes. Issued report, files and archive
are read-only; corrections must have a separately named report/packet.

No input or canonical file was changed; only the assigned hostile report,
the unique assigned artifact directory and its named sibling archive/seals
were created. No dependency, commit, push, remote change or publication
occurred. No LaTeX source was edited or compiled.

Root's next action is to compare this **whole-claim PASS** with the
separate whole reconstruction, match the exact accepted source gates,
then decide campaign promotion. The scientific remainder is precisely
the frozen weighted three-label cancellation, not an unproved two-label
estimate. This audit does not resolve that remaining cancellation or
the original L1 source mission.
