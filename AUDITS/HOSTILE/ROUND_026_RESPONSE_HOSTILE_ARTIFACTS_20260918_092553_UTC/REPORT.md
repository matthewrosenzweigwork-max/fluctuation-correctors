# AUD072 — whole hostile review of THM050 / PO037

TASK113. Issued 2026-09-18 UTC by the isolated hostile lane in
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r026-response-hostile`.
The assigned branch is `codex/hocf-r026-response-hostile` and the provisioned
base is `ef438b612f732d21af1fa1756dd7559ef63c6d61`; these are parent-provided
metadata, not independently inspected Git facts. No Git metadata or history
was read or changed. This is the hostile axis, not the blind axis or root's
whole-gate promotion.

**Verdict: PASS for (A), PASS for (B), PASS for (C), and PASS for the frozen
THM050 conjunction. No first failing mathematical line was found.** The
supporting arguments below were recomputed, with the supplied proof visible.
This is not a blind reconstruction, a repair, a weakened replacement theorem,
or a proof or negation of THM046. Its critical source assertion and the needed
actual-law square-gradient estimates remain open.

The 13 supplied input digests passed before mathematical reading and again
when their complete bytes were copied into the packet. The supplied TASK110
report has **646 lines**, including its final restrictions at lines 643–646;
all 646 were reviewed. TASK113's “643-line” description is administrative
staleness, not a truncated input or an omitted review tail. The original task
card is preserved unchanged. Parent later confirmed that 643 was the
pre-issuance count, without supplying any blind result or mathematical detail.

## 1. Frozen assertion, negation, and dispositions

The authoritative statement is the exact copied
`THEOREMS/THM-050_COULOMB_CONDITIONAL_RESPONSE_AND_ANGULAR_OBSTRUCTION.md`.
The worker claim card agrees with its substantive three clauses. The root
card additionally states the artificial constant-mode comparison explicitly.
The physical signed-correlation target concerns only nonzero modes.

| Clause | Frozen scope reviewed | Hostile disposition |
|---|---|---|
| (A) | Every finite N at least two, finite positive diffusivity, integer mode and finite nonnegative horizon; original iid Haar preparation; exact conditional-mean and conditional-noise costs; true heat-cutoff martingale/brackets; fixed-N numerical Dirichlet-cost limit; nonnegative equivalence along the critical sequence | PASS. No unproved singular gradient, independence assertion, or exchange of the cutoff and N limits is needed. |
| (B) | Every admitted compact, separated, positive-volume local set of slow coordinates; all directions; one fixed N and positive diffusivity; a positive time interval with the stated uniform radial limsup and coefficient | PASS. The proof gives uniform moment, exit, radial and directional bounds before taking the limsup. It needs no collision entrance limit. |
| (C) | Every fixed N and positive diffusivity; every sufficiently small positive time; failure of full-coordinate Haar W1,4 and divergence of the actual cutoff fourth-gradient integral | PASS. The projection survives on a positive-volume set of slow coordinates, and polar slicing uses the correct full-gradient factor. |
| Whole conjunction | All clauses with their original quantifiers, normalization, integrability, and cutoff order | PASS on this hostile axis. Root must separately compare the whole blind axis and authenticate prior gate provenance. |

The exact negation is an admitted violation of at least one clause, not a
failed proof route. In (B), one admitted datum must defeat every finite error
constant and every positive time window at some time in that window. In (C),
one admitted N and diffusivity must have no positive interval on which both
conclusions hold at every time. The review produces neither witness. Lack of
an N-uniform time window, a static law, or failure of the proposed global
sensitivity estimate does not supply the critical source negation.

The precise line that fails in the **attempted route** is TASK110 (3.6), lines
281–296. That is an explicitly disproved estimate inside the report, not a
false line asserted by THM050. It is not repaired here.

## 2. Domain, normalization, and cutoff preflight

References below are to the complete hashed TASK110 report unless another
file is named. Historical R1/R4/R6 status labels are not used as certified
premises. Their necessary mechanisms can be reconstructed from the allowed
definitions, as follows.

For the unit torus and coefficient-one d4 kernel, let c=4π². Integrating
the nonzero heat Fourier multiplier gives c/(4π²|k|²)=|k|⁻². In local
coordinates the central Gaussian integral is

\[
 c\int_0^\infty(4\pi u)^{-2}e^{-|y|^2/(4u)}\,du=|y|^{-2}.
\]

Subtract it from the periodic heat integral. Small-time noncentral lattice
terms and all their derivatives have an exponential distance factor;
large-time periodic remainders decay exponentially, while the subtracted
Euclidean term and its derivatives are integrable. The difference is smooth
and even near zero. Consequently K(y)=2y/|y|⁴+Kreg(y), with Kreg=O(|y|).
The local flux is 2|S³|=4π². The Fourier zero mode supplies exactly the
compensation −c dx, hence div K=c(δ0−dx). The local force and energy are
integrable in four dimensions. These recomputations validate lines 59–81;
the relevant allowed R4 material is lines 69–196. No logarithmic or other
Riesz normalization is imported.

Write H=N⁻¹Σi<j g(xi−xj), and subtract (N−1)inf(g)/2. The resulting energy
is nonnegative and has compact sublevels in the collision-free state space.
Smooth local cutoffs give a measurable, nonanticipating, pathwise unique
solution until exit from that space. On an energy sublevel, B=−∇H and
ΔH=c(N−1): both coordinates of every unordered pair contribute c/N.
Ordinary stopped Itô calculus therefore gives

\[
 dH=-|B|^2dt+\nu c(N-1)dt
       +\sqrt{2\nu}\nabla H\cdot dW.
\]

If the energy exit level is L, its probability before T is at most the
initial shifted energy plus νc(N−1)T, divided by L. A finite nonextendible
path remaining in a compact collision-free sublevel could be continued by
the smooth local equation, so these exits exhaust the possible lifetime.
Letting L grow proves noncollision for every collision-free deterministic
start. The iid Haar starting energy has finite mean. Fatou then gives
integrability of the **total** drift-square action; it does not yield the
sum of individual pair-force squares. That action bound makes the energy
martingale square integrable and removes its stop by isometry. Thus the
order of the arguments at lines 83–102 is valid.

The local cutoff construction is jointly measurable in the initial point
and Brownian path. Uniqueness gives its deterministic-time restart identity.
Independent Brownian increments then give the Markov property after
conditioning on the current collision-free point. An exceptional set that
depends on this point causes no problem: the measurable conditional
probability is zero at every fixed such point. This supplies the actual
semigroup used in (A). No singular generator-domain theorem or collision
entrance extension is silently assumed. The allowed R6 lines 229–327 and
402–423 give the same mechanism.

For fixed N, diffusivity and starting point, a realized noncolliding path
has positive minimum pair distance on each finite interval. Heat convolution
converges to K in local C1 away from collision. Coupling with the same noise,
stopping the difference before it reaches a fraction of that minimum
distance, and applying Gronwall shows that this stop cannot occur for all
sufficiently small heat parameters. This proves the full heat-parameter
path limit on that interval. No heat-process noncollision estimate uniform
in the cutoff is needed. The allowed R6 lines 425–469 justify the same
local comparison; the claim at TASK110 lines 104–109 is correctly fixed-N.

For the ancillary integrability used in the modal equations, the full
smooth drift divergence is

\[
 \operatorname{div}B^\varepsilon
 =\frac{2c}{N}\sum_{i<j}(p_\varepsilon(x_i-x_j)-1)
 \geq-c(N-1).
\]

For every fixed Brownian driving path its smooth additive-noise flow is a
diffeomorphism; subtracting that path leaves an ordinary time-dependent
ODE. Its Jacobian determinant is at least exp[−c(N−1)t]. Change of variables,
then Brownian averaging, gives the heat law density bound exp[c(N−1)t]
from Haar initial data. The bound passes first on continuous tests using
the fixed-N path limit, then to open and Borel sets by measure approximation.
This verifies lines 110–116 and R6 lines 471–544 without claiming that the
singular flow is onto. Translation and permutation equivariance give Haar
one-body marginals and exchangeability; neither gives a positive-time
product law.

## 3. Clause (A): conditional costs and true brackets

Let Y=F(XT), m(X0)=P_T F(X0), and V=m(X0)−AF(X0). Every variable is bounded.
Conditional on X0, the noise Y−m has mean zero. Therefore

\[
 E[V\overline{(Y-m)}]=0,\qquad
 N E|Y-AF(X_0)|^2=N E|V|^2+N E|Y-m|^2.
\]

The first term is precisely C under the original Haar initial law, and the
second is J. All integrability is absolute. Orthogonality of these two
differences is sufficient; independence is neither true in general nor
used. Both costs have coefficient N. This verifies lines 208–231.

At every fixed positive cutoff the generator is smooth on the compact
configuration torus. Flow differentiation and the semigroup identity give
the smooth backward function u_s=P_(T−s)^εF. Its drift under the same
cutoff dynamics is zero. Itô's formula gives Brownian coefficient
√(2ν)∇i u_s in coordinate i. Conjugate products of these coefficients
give 2νΣi|∇i u_s|². With the empirical martingale coefficient
√(2ν)∇e_k/N, the cross bracket is

\[
 \frac{2\nu}{N}\sum_i\nabla_i u_s(X_s^\varepsilon)
            \cdot\overline{\nabla e_k(X_i^\varepsilon(s))}\,ds.
\]

All integrands are bounded at that fixed cutoff, so the martingales are
true square-integrable martingales. Isometry gives the displayed cutoff
Dirichlet cost with factor 2νN, not 2ν or 2ν/N. The common noise prevents
discarding the cross bracket. These facts verify lines 233–261.

The one-body factor exp[−a(T−s)] corresponds to the frozen **target** test
exp[−a(T−s)]e_k from THM046 and TASK110's definition of a. Multiplying its
Brownian integrand gives exactly that factor in the cross bracket. This is
not an identification of the target test with the backward solution for the
heat-cutoff linearized operator. For that different operator the nonzero
mode damping would be c exp(−εell_k)+νell_k. THM050 makes no such
identification, and none is needed for its true stochastic-integral bracket.

The coupled bounded endpoints converge in L2. For each collision-free
deterministic start, bounded convergence also gives P_T^εF→P_TF; Haar
dominated convergence gives convergence in Haar L2. Equivalently,

\[
 J^\varepsilon=N\left(E|F(X_T^\varepsilon)|^2
                          -\|P_T^\varepsilon F\|_2^2\right)\longrightarrow J.
\]

This proves the Dirichlet-cost limit as a limit of numbers, as asserted at
lines 262–275. It does not interchange a gradient with a singular limit.
Along any sequence, nonnegativity and D=C+J give the stated equivalence of
vanishing. Critical scaling is relevant to the eventual target, not needed
for that elementary equivalence.

At k=0, F=1, P_TF=1 and all Brownian gradients vanish. Under the expressly
frozen a=c, C=D=N(1−exp(−cT))² and J=0. At T=0 every cost and time integral
is zero. The physical nonzero-mode damping convention is thus not extended
to constants. The report's Section 2 modal equations are read in their
explicit nonzero-target scope from lines 39–46; they would not have initial
V=R=1 for k=0. The root card already makes this distinction, so no theorem
repair is being inserted by this review.

## 4. Clause (B): recomputation of the local estimates

Fix N and ν throughout. Compactness and separation of Q give uniform
neighborhood and distance margins. Before the local exit τ, all forces
other than the isolated pair's principal singular force are smooth on a
common compact set. Their contribution to the relative drift vanishes
linearly with y. With Y=X1−X2 and Z=(X1+X2)/2, subtraction gives

\[
 dY=\alpha Y|Y|^{-4}dt+b(Y,q)dt+2\sqrt\nu\,dB,
 \qquad \alpha=4/N,\quad |b|\leq L|Y|.
\]

Indeed each original internal force is ±2Y/(N|Y|⁴). The center's internal
force is zero and its noise coefficient is √ν; each remaining coordinate
keeps √(2ν). Orthogonal sums and differences of the original Brownian
motions have zero cross bracket. The resulting processes need not be
independent once the drifts couple them. This verifies every factor at
lines 311–328.

First impose a positive lower radial stop as well as τ. For each even p≥4,
the four-dimensional relative generator applied to |y|p is

\[
 p\alpha |y|^{p-4}+2\nu p(p+2)|y|^{p-2}
                       +p|y|^{p-2}y\cdot b.
\]

Its stopped expectation has an indicator of remaining inside both stops.
After bounding the last term above by pL|y|p, all right-hand terms are
nonnegative, so that indicator can be discarded for an upper bound using
stopped moments. For p=4, m2≤sqrt(m4) and sqrt(x)≤1+x give
m4≤C(r⁴+t) by the integral Gronwall inequality. For p=6, use this m2 bound;
then induct on even p. With U=r⁴+t bounded, the two integrals are bounded
by t U^((p−4)/4)≤U^(p/4) and
t U^((p−2)/4)≤C U^(p/4). Thus

\[
 m_p(t)\leq C_p(r^4+t)^{p/4},\qquad
 m_2(t)\leq C(r^4+t)^{1/2}.
\]

The constants are uniform in q, direction and lower radial stop. For each
fixed positive initial r, noncollision removes that stop pathwise; bounded
stopped radii allow passage in these moments. Uniformity of the inequalities
is retained without asserting a common probability-one event over all
initial points. This validates lines 330–360.

At pair exit the stopped eighth-radius equals the fixed boundary radius to
the eighth power. Its expectation therefore controls that exit probability.
A slow-coordinate exit requires a Brownian maximum exceeding a fixed
distance margin after subtracting a bounded drift over time t. The
one-dimensional reflection bound, applied to finitely many components,
gives an exponentially small probability, hence O(t²). The eighth moment
then proves limsup_(r↓0) sup_(q,θ) P(τ≤t)≤Ct². This is lines 362–374;
no collision event or near-pair force-square bound is substituted.

Direct differentiation gives the stopped fourth-radius equation

\[
 R_t^4=r^4+4\alpha(t\wedge\tau)
  +\int_0^{t\wedge\tau}(48\nu|Y|^2+4|Y|^2Y\cdot b)\,ds
  +8\sqrt\nu\int_0^{t\wedge\tau}|Y|^2Y\cdot dB.
\]

The last bracket is 64ν∫|Y|⁶. In the uniform radial limsup, the drift error
is O(νt^(3/2)+Lt²), the martingale's L1 norm is O(√ν t^(5/4)), and the
time-stop replacement costs O(t³). Dividing by sqrt(4αt) in the difference
of square roots proves

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
 E\big|R_t^2-\sqrt{4\alpha t}\big|\leq Ct^{3/4}.
\]

This division is legitimate because α>0 at every fixed N. It is not an
N-uniform estimate. The relevant candidate lines are 376–399.

The second-radius equation has drift 2α|Y|⁻²+16ν+2Y·b and Brownian
coefficient 4√νY. Taking stopped expectations and retaining the positive
inverse-radius term yields

\[
 2\alpha E\int_0^{t\wedge\tau}|Y_s|^{-2}ds
 \leq m_2(t)+2L\int_0^t m_2(s)ds.
\]

This follows first at the lower stop and then by Fatou; the noncollision
result alone is not being mistaken for expected inverse-radius
integrability. The right side has uniform radial limsup O(sqrt(t)).
For Θ=Y/|Y|, differentiation in dimension four gives tangential noise
2√ν(I−ΘΘᵀ)/|Y| and Itô drift −6νΘ/|Y|², plus the projected b/|Y|.
The preceding occupation bound makes the direction martingale L2.
Pairing its equation with the initial direction and using
|Θ−θ|²=2(1−Θ·θ) gives

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
 E|\Theta_{t\wedge\tau}-\theta|^2\leq C(\nu\sqrt t+t).
\]

Combining this with the fourth moment by Cauchy–Schwarz, and with the
second-radius approximation, gives the error Ct^(3/4) in the quadratic
directional moment. This checks lines 401–441 without assuming a limiting
angle or an entrance law.

The empirical pair contributes exactly

\[
 \frac2N e_k(z)\cos(\pi k\cdot y)
 =\frac2N e_k(z)-\frac{\pi^2}{N}e_k(z)(k\cdot y)^2
                                      +O_k(|y|^4/N).
\]

All slow-coordinate drifts are bounded until τ, so the expectation of H_k
changes by O(t). The center displacement has second moment O(t²+νt);
its product with the quadratic pair term costs O(t) by the fourth-radius
bound. The Taylor error is O(t), and removing the final local stop costs
at most 2P(τ≤t). Finally sqrt(4α)=4/sqrt(N). These computations recover
the stated negative coefficient 4π²/N^(3/2) and the full uniform limsup
in lines 443–472. They apply for every t in one sufficiently small interval,
with constants depending only on the fixed data and neighborhoods.

## 5. Clause (C): full-coordinate Sobolev and cutoff conclusions

For k=(1,0,0,0), choose a positive-volume set Q with cos(2πz1)≥1/2 and
all other displayed points separated. Such a set exists for every finite
N by taking sufficiently small product neighborhoods around finitely many
distinct points. No uniform size of Q in N is needed.

With normalized sphere measure, rotation symmetry gives
Eσ θ1²=1/4 and Eσ θ1⁴=1/8. Hence Y2=θ1²−1/4 has zero mean and
∫θ1²Y2=1/16. The homogeneous polynomial y1²−|y|²/4 is harmonic of
degree two, giving ΔS³Y2=−8Y2. Projecting (B) onto Y2 yields leading
magnitude at least π²sqrt(t)/(8N^(3/2)). Choose t0 so its O(t^(3/4))
error is smaller by a fixed factor, then use the **uniform** limsup to
choose a positive r*(t) for every fixed t. Reducing t0 slightly if needed
leaves the strict margin giving

\[
 \left|\int u(q,r\theta)Y_2(\theta)d\sigma\right|
 \geq \frac{\pi^2}{16N^{3/2}}\sqrt t
 \quad(q\in Q,\ 0<r<r_*(t)).
\]

This merely makes explicit the “reducing t0” already present at candidate
lines 490–503; it does not add a hypothesis or change its claim. An exact
directional limit remains unnecessary.

Spherical integration by parts and Hölder give
|∫vY2|≤(1/8)||∇S Y2||_(4/3)||∇S v||4. Approximation in local smooth
charts gives the same inequality for weak W1,4 spherical functions.
In the injective local pair coordinates, the absolute Jacobian is one and

\[
 |\nabla_{x_1}u|^2+|\nabla_{x_2}u|^2
     =\tfrac12|\nabla_z u|^2+2|\nabla_yu|^2,
 \qquad |\nabla_Xu|^4\geq4r^{-4}|\nabla_Su|^4.
\]

The remaining labels only add nonnegative terms. Lebesgue measure in y
is |S³|r³ dr dσ. If u belonged to full Haar W1,4, change of variables and
Fubini on each positive annulus would give weak spherical W1,4 slices
for almost every q and r, with their tangential derivative given by the
weak gradient. This can also be seen by approximating on such annuli and
passing in the Sobolev norm. Applying the projection inequality and
integrating over Q would then bound its fourth-gradient integral below
by a positive constant times

\[
 t^2|Q|\int_0^{r_*(t)}\frac{dr}{r}=+\infty,
\]

a contradiction. The codimension of the pair collision is four; replacing
this radial dimension by the full 4N is an error. The argument uses an
actual positive-volume family, not a single slice. It verifies lines
474–533 including the full gradient and weak polar passage.

For actual heat responses uε, smoothness and |uε|≤1 hold at each cutoff.
The fixed-N path passage gives pointwise convergence to u at every
collision-free starting point. On any annulus δ<r<r*(t), dominated
convergence passes their spherical projections and their fourth powers
under dq dr/r. Applying the same spherical inequality before the limit
therefore gives

\[
 \liminf_{\varepsilon\downarrow0}\int|\nabla u_\varepsilon|^4
 \geq C t^2 |Q|\log(r_*(t)/\delta),\qquad C>0.
\]

The left side is independent of δ; letting δ decrease proves it is
infinite. This is an actual-cutoff conclusion, not a substituted smoothing
of u. It checks lines 535–555 without requiring compactness or convergence
of the gradients. The analogous power for a squared gradient is r dr,
which is integrable; no Haar W1,2 failure or estimate follows. The full
critical source and its positive-limsup negation remain unaffected.

## 6. Ancillary mathematics and source qualifications

The nonzero-mode finite-N reconstruction in Section 2 also passes. Both
terms in div K must be retained: the commutator row is −ce_k and its
double background is zero. Thus j has zero Haar rows. Ordered-label
counting gives P_N[J]=U+(c/N)Z and the drift
−(c+νell_k−c/N)Z+U. The conjugate martingale bracket is
(2νc(k·l)/N)Z_(k−l), while the nonconjugate one has a minus sign and
Z_(k+l). The diagonal conjugate bracket is 2νell_k/N.

The weak source is bounded by a constant times 1+dist(x,y)⁻², which is
Haar integrable. Fixed-N density domination gives its absolute time
integrability, including when multiplied by a bounded initial mode.
No two-time joint density or source square is needed. Among ordered
triples (i,j,h) with i≠j, exactly 2N(N−1) have h=i or h=j and
N(N−1)(N−2) have three distinct labels. With denominator 2N² this
recovers both coefficients in F_N and G_N. At N=2 the third-label
term is omitted.

Product Itô and initial measurability give the two stated ODEs for
V=N E|Zt|² and R=N E[Zt conjugate(Z0)], both starting at one for nonzero
k. Their integrating factors give exactly (2.6)–(2.7), including the
minus sign and both damping factors in the initial/current contribution.
Since a_tilde≥c/2, the explicit terms are nonnegative and have sizes
O(N⁻²) and O(ν), respectively. On the critical tail ν is O(N⁻1/2).
Thus the negative part of Re Rcal is o(1), and Re Rcal→0 is equivalent
to D→0 for this fixed nonzero mode. This checks lines 118–204.

This recomputation does **not** certify THM049's separate equivalence
between all smooth real tests in the original L1 source assertion and
the modal L2 criterion. That clause can depend on the unprovided THM048
and its uniform-integrability/source-majorant input. TASK110 expressly
does not use or certify that theorem at lines 48–57 and 201–204. Its
“target” at lines 228–231 is therefore verified here as its stated
nonzero-modal signed-correlation target. THM050 itself needs none of the
unverified L1/L2 bridge. THM046's historical R8/R12/R14/R16 gate-status
sentences likewise are scope records, not premises of this review.

The local radial ODE in lines 572–579 also passes: R⁴=r⁴+4αt, radial
Jacobian eigenvalue (r/R)³, tangential eigenvalue R/r, and determinant
one in four dimensions. It only tests the local coefficients. It is
neither the actual positive-noise process nor a witness for the original
critical negation. The mathematical interpretation of the diagnostic
claims and self-check table at lines 563–629 is appropriately limited.

| Identifier | Location | Finding and severity | Disposition |
|---|---|---|---|
| AUD072-F01 | TASK113 description versus complete TASK110 file | Administrative line-count mismatch, certain; no mathematical severity | Reviewed all 646 hashed lines; original task card retained; parent explanation recorded. |
| AUD072-F02 | TASK110 590–593 and 633–641 | The constructor's assertion count, mutation outcomes, 17-source verification and archive/read-only issuance are not independently authenticated here; evidence limitation, certain | Constructor code/results/packet were withheld. Those claims are not adopted as evidence. This packet supplies a separate fresh diagnostic and complete 13-input evidence. |
| AUD072-F03 | THM046 line 15; THM049 (B)/(C); historical labels in allowed sources | Prior accepted-gate provenance and the all-smooth-test L1 bridge are outside this source allowlist; evidence limitation, certain | No source-status promotion. Root owns authentication. All mechanisms needed for THM050 were recomputed above. |
| AUD072-F04 | TASK110 Section 2 and lines 260–261; THM050 (A) | Constant-mode and backward-test conventions require the frozen distinctions; normalization qualification, certain | Root card's artificial constant comparison is respected. The backward bracket uses the specified target test, not the different heat-linearized response test. No coefficient repair is needed. |

No finding requires changing the frozen A/B/C assertion, the actual dynamics,
the initial law, the local data class, the cutoff order, or the claimed time
quantifiers. No outside citation or novelty claim is used.

## 7. Whole-report coverage and fresh evidence

| Candidate lines | Reviewed content | Disposition |
|---|---|---|
| 1–57 | Target, mission boundary, constructor status, source restrictions | Scope and qualification retained; provenance claims not independently inherited. |
| 59–116 | Heat normalization, singular process, energy, heat passage and density | Recomputed and PASS at fixed N. |
| 118–204 | Nonzero-mode deleted-diagonal equations and signed-correlation formula | Recomputed and PASS within the stated modal scope. |
| 206–275 | Response decomposition, both true brackets, fixed-N numerical cost limit | PASS, clause (A). |
| 277–296 | Proposed uniform global sensitivity bound | Correctly identified as the failed route; not a theorem premise. |
| 298–472 | Full local actual-dynamics calculation with other labels and exits | PASS, clause (B). |
| 474–561 | Positive-volume projection, weak full-gradient contradiction and actual cutoff divergence | PASS, clause (C); no square-gradient conclusion. |
| 563–594 | Finite-probability, ODE and computational claims | Analytical ODE and diagnostic interpretation checked; constructor execution counts not authenticated. |
| 595–629 | Self-check, exact remaining obligations and status | Consistent with the reviewed proof; no critical target resolved. |
| 631–646 | Issuance, source exposure and operational restrictions | Read completely; historical operational claims remain the constructor's record. |

The fresh `hostile_diagnostic.py` uses only Python's standard library. Its
final baseline passed **283 assertions in 13 categories**: exact rational
conditional orthogonality and nonzero endpoint/noise covariance; coordinate
noise and Coulomb factors; explicit overlap enumeration; rational automatic
differentiation of radial and angular functions; retained cutoff brackets;
spherical moments; exact radial-flow Jacobians; empirical cosine coefficient;
full-gradient coordinate transformation; radial integration powers; and the
artificial constant mode. Thirty-six deterministic cosine checks use binary
floating point with the explicit fourth-order Taylor bound and an absolute
roundoff allowance of 2e−15. All other checks use exact rational arithmetic.
There is no random sample, stochastic discretization, installed dependency,
or reliance on constructor code.

All **13 mathematical mutations exited 1 with explicit nonzero witnesses**:
omit C; erase the endpoint/noise covariance; halve relative drift; halve
relative noise; halve the angular Itô drift; erase the cutoff cross bracket;
remove the backward test factor; halve the empirical quadratic coefficient;
change the spherical projection; halve the full-gradient fourth-power factor;
use 4N instead of four for the collision's radial dimension; omit overlap
labels; and erase the artificial constant-mode defect. Complete commands,
stdout, stderr and exits are in `DIAGNOSTIC_RESULTS.json`. These controls
test sensitivity of the supporting checker, not the stochastic limiting
arguments or the entire theorem by computation.

The portable read-only verifier checks the exact directory tree and regular
member inventory, every file digest and size, all 13 frozen input copies,
safe regular tar members, archive/directory byte equality, the external
report's equality with the packet report, read-only file modes, and the
sibling checksum seal. Its four deliberately invalid controls—changed
payload digest, parent traversal, archive symlink and extra inventory
member—all exited 1. They run in memory and neither write nor extract
malicious fixtures. Their complete results are retained.

The issued packet is
`ROUND_026_RESPONSE_HOSTILE_ARTIFACTS_20260918_092553_UTC`, with named sibling
archive, full inventory, core-verification record and SHA-256 seal. The
exact invocation and source/read/exposure history are in the packet README
and `EXPOSURE_AND_HISTORY.md`. The source reports and theorem cards were
not edited. No STATE file, canonical memorandum, current blind audit,
constructor diagnostic/result, nonallowlisted history, memory, other
worktree, remote, or external source was read or changed. No child, Git
mutation, installation, publication or contact occurred.

The only mathematical verdict issued here is the whole hostile PASS above.
Root still owns comparison with the separate complete blind reconstruction,
accepted-source authentication, promotion and integration. There is no new
claim that the actual critical source vanishes, has positive limsup, or is
controlled in Haar W1,2.
