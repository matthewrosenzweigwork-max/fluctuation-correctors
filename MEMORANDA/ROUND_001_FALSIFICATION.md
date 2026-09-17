# Round 001: weighted-route counterexamples and finite-particle checks

Date: 2026-09-17 UTC. Task: TASK-005. Baseline commit:
475a5399828bc6e2ccbade08c59b8778638df14a.

This report uses the frozen common dossier and the coordinator's two bounded
claims. No constructor report, proof narrative, or provisional mathematical
assessment was read. These negative arguments are independent of the
construction lanes. Their proofs are SELF_CHECKED and await a separate hostile
audit. Root alone assigns global obstruction identifiers and updates state.

**Verdict.** The universal weighted lower bound is **DISPROVED** for arbitrary
smooth symmetric nonnegative weights, already on the one-dimensional torus
with homogeneous positive reference density. The assertion that the specified
weighted remainder is always less singular than the Riesz kernel is also
**DISPROVED**. These conclusions concern two route assumptions; they neither
disprove the fluctuation targets nor certify singular stochastic identities.

## 1. Claims, conventions, and normalization

Fix \(0<s<1\), \(\mathbb T=\mathbb R/\mathbb Z\), and Haar measure of mass one.
Use Fourier characters \(e^{2\pi ikx}\) and the mean-zero periodic kernel
\[
 \widehat g_s(k)=
 \pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}
 |k|^{s-1}\quad(k\ne0),\qquad \widehat g_s(0)=0.
\]
Here is an independent verification of both the Fourier constant and the local
singularity. For \(x\notin\mathbb Z\), define
\[
 g_s(x)=\frac1{\Gamma(s/2)}
 \int_0^\infty t^{s/2-1}
 \left\{\sum_{n\in\mathbb Z}e^{-t(x+n)^2}
                  -\sqrt{\frac\pi t}\right\}\,dt.                 \tag{1.1}
\]
Integrating the periodized Gaussian over the real line gives its Fourier
coefficients \(\sqrt{\pi/t}\,e^{-\pi^2k^2/t}\). Its Fourier series implies
exponential convergence of the bracket in (1.1) to zero as \(t\downarrow0\).
As \(t\to\infty\), the bracket has \(L^1(\mathbb T)\) norm at most
\(2\sqrt{\pi/t}\). Its weighted integral therefore converges in \(L^1\),
because \(s<1\), so Fubini is justified. For \(k\ne0\), substituting
\(u=\pi^2k^2/t\) yields
\[
 \frac{\sqrt\pi}{\Gamma(s/2)}
 \int_0^\infty t^{(s-3)/2}e^{-\pi^2k^2/t}\,dt
 =\pi^{s-1/2}|k|^{s-1}
   \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\]
The mean of the bracket is zero. Subtracting the \(n=0\) Gaussian integral
also proves, on every interval \(|x|<r_0<1/2\),
\[
             g_s(x)=|x|^{-s}+H_s(x),\qquad H_s\in C^\infty.       \tag{1.2}
\]
For this last assertion, split the integral at \(t=1\). Near zero, the
subtracted integrand and all spatial derivatives are integrable against
\(t^{s/2-1}\); above one, all \(n\ne0\) terms decay exponentially locally
uniformly, and the constant subtraction is integrable since \(s<1\).
In particular, \(g_s(r)>0\) for all sufficiently small nonzero \(r\).
No source theorem is imported without proof in this normalization check.

Retain the dossier's ordered-label convention
\[
 P_N[h]=\frac1{2N^2}\sum_{i\ne j}h(x_i,x_j)
       -\frac1N\sum_i\int h(x_i,y)\mu(y)\,dy
       +\frac12\iint h(x,y)\mu(x)\mu(y)\,dx\,dy.                  \tag{1.3}
\]
Write \(F_N^w=P_N[w g_s]\). If a source calls \(2P_N\) its weighted energy,
the negative energies below double and the contradiction is unchanged.

The first assertion tested is: for every smooth symmetric \(w\ge0\), there
are finite \(C_w\) and \(\delta>0\), independent of \(N\) and configuration,
such that
\[
 F_N^w\ge
 \zeta(s)N^{s-1}\int_{\mathbb T}w(x,x)\mu(x)^{1+s}\,dx
       -C_wN^{s-1-\delta}.                                     \tag{1.4}
\]
Its negation is a fixed admissible \(s,w,\mu\) and configurations violating
(1.4) for arbitrarily large \(N\), for every proposed finite \(C_w\) and
positive \(\delta\). Section 2 establishes precisely this negation.

The second assertion is that, for every such weight,
\[
 D_w(x,y):=(w(x,y)-w(x,x))g_s'(x-y)
                  +\partial_xw(x,y)g_s(x-y)                    \tag{1.5}
\]
has strictly lower pointwise singular order than \(g_s(x-y)\). Its negation
is an admissible \(w,x\) with a nonzero limit of
\(D_w(x,x-r)/g_s(r)\) as \(r\to0\). Section 3 supplies this witness.

## 2. Separated-support counterexample and explicit particles

Choose disjoint small closed arcs \(A,B\) in one coordinate chart such that
\[
              g_s(x-y)\ge m>0\quad(x\in A,\ y\in B).             \tag{2.1}
\]
By (1.2), one may take the centers a small positive distance apart and the
radii still smaller. Let \(p,q\ge0\) be smooth, supported in the respective
interiors, with \(\int p=\int q=1\). Set
\[
 f=p-q,\qquad
 w(x,y)=p(x)q(y)+q(x)p(y),\qquad h(x,y)=w(x,y)g_s(x-y).
\]
The weight is smooth, symmetric and nonnegative. It vanishes on a full
neighborhood of the diagonal; hence \(h\), extended by zero there, is smooth
with \(h(x,x)=w(x,x)=0\). There is no singular limit hidden in this example.
Put
\[
 A_0:=\iint p(x)^2q(y)^2g_s(x-y)\,dx\,dy
       \ge m\left(\int p^2\right)\left(\int q^2\right)>0.
\]
Disjoint supports give the exact identity
\[
                 \frac12\iint h(x,y)f(x)f(y)\,dx\,dy=-A_0.       \tag{2.2}
\]
Each of the two cross rectangles contributes \(-A_0\) before the factor
\(1/2\). Thus a nonnegative scalar weight need not produce a nonnegative
quadratic form.

Fix the reference \(\mu\equiv1\), and define
\[
 \gamma=\frac{1-s}{4},\quad a=\frac1{2\|f\|_\infty},\quad
 \alpha_N=aN^{-\gamma},\quad \nu_N=1+\alpha_N f.
\]
Every \(\nu_N\) is a smooth probability density between \(1/2\) and \(3/2\).
Let \(Q_N\) invert \(t\mapsto\int_0^t\nu_N(x)\,dx\) on \([0,1]\), and take
the distinct particles
\[
 x_i^{(N)}=Q_N\!\left(\frac{i-1/2}{N}\right),\quad i=1,\ldots,N,
 \qquad \eta_N=\frac1N\sum_i\delta_{x_i^{(N)}}.                  \tag{2.3}
\]
Since \(Q_N\) is 2-Lipschitz, quantile coupling proves
\[
 W_1(\eta_N,\nu_N)\le
 2\sum_{i=1}^N\int_{(i-1)/N}^{i/N}
       \left|t-\frac{i-1/2}{N}\right|dt=\frac1{2N}.              \tag{2.4}
\]
The interval estimate also bounds torus Wasserstein distance.

Let \(L=\max(\|\partial_xh\|_\infty,\|\partial_yh\|_\infty)\).
Since \(h(x,x)=0\), deleted-diagonal energy equals the full quadratic form
of \(\eta_N-\mu\). Coupling once in each variable gives
\[
 \left|F_N^w-\frac12\iint h(x,y)(\nu_N(x)-1)(\nu_N(y)-1)\,dx\,dy\right|
 \le 2L W_1(\eta_N,\nu_N)\le L/N .
\]
By (2.2), for every \(N\ge2\),
\[
 \boxed{\big|F_N^w+A_0a^2N^{-(1-s)/2}\big|\le L/N.}             \tag{2.5}
\]
For all sufficiently large \(N\), the energy is at most
\(-\tfrac12 A_0a^2N^{-(1-s)/2}\). The diagonal integral in (1.4) is
exactly zero. Since \((1-s)/2<1-s+\delta\) for every \(\delta>0\)
(and even for \(\delta=0\)), (2.5) violates (1.4) for every finite \(C_w\).

All constants and the weight are fixed independently of \(N\). Also
\(\eta_N\) converges weakly to the reference density: (2.4) tends to zero
and \(\|\nu_N-1\|_{L^1}=2\alpha_N\to0\). Mere macroscopic convergence
does not repair the bound. No stronger microscopic well-preparedness
condition is claimed for these particles.

### 2.1 Strictly positive weights also fail

The obstruction is not restricted to zero diagonal weights. Define
\[
 E_f=\frac12\iint g_s(x-y)f(x)f(y)\,dx\,dy,\qquad w_M=1+Mw,
\]
where \(M>0\) is so large that \(E_f-MA_0<0\). The integral is finite
because \(s<1\). For fixed \(0<\alpha\le a\), put \(\nu=1+\alpha f\).
The continuum weighted energy relative to \(\mu=1\) is
\[
 \frac12\iint w_M(x,y)g_s(x-y)(\nu(x)-1)(\nu(y)-1)\,dx\,dy
                      =\alpha^2(E_f-MA_0)<0.                    \tag{2.6}
\]
Here \(w_M\ge1\) and \(w_M(x,x)=1\).

Sample particles iid from \(\nu\), while retaining reference \(\mu=1\).
Absolute integrability justifies direct counting of the \(N(N-1)\) pairs:
\[
 \mathbb E_{\nu^{\otimes N}}F_N^{w_M}
 =\alpha^2(E_f-MA_0)
  -\frac1{2N}\iint w_M(x,y)g_s(x-y)\nu(x)\nu(y)\,dx\,dy
 \longrightarrow\alpha^2(E_f-MA_0)<0.                           \tag{2.7}
\]
Any all-configuration bound tending to zero would also bound this
expectation, a contradiction. For every sufficiently large \(N\), a
violating distinct-particle configuration therefore exists. This is not
a typicality statement under iid \(\mu\), Gibbs, or another preparation.

### 2.2 Necessary repair and fixed-cutoff compatibility

A universal lower bound tending to zero forces the continuum kernel
\(wg_s\) to be nonnegative on smooth zero-mass perturbations: repeat
(2.7) with \(\nu=\mu+\alpha f>0\), then let \(N\to\infty\).
Pointwise \(w\ge0\) does not give this necessary quadratic-form property.
A possible structural class is \(w(x,y)=b(x)b(y)\), \(b\ge0\), since
\[
 \iint w(x,y)g_s(x-y)f(x)f(y)\,dx\,dy
       =\sum_{k\ne0}\widehat g_s(k)|\widehat{bf}(k)|^2\ge0.
\]
This continuum positivity does not prove the sharp finite-particle
constant or remainder. Law or preparation restrictions are another
possible repair only after their hypotheses and estimates are proved.

The first counterexample also works with heat regularization
\(g_{s,\varepsilon}=e^{\varepsilon\Delta}g_s\). On the compact difference
set \(A-B\), convergence holds in every \(C^m\) norm. To justify this,
split \(g_s\) into a smooth part near this set and an \(L^1\) part a
positive distance away; derivatives of the heat kernel acting on the
latter tend to zero exponentially. Thus \(w g_{s,\varepsilon}\to w g_s\)
smoothly. For all sufficiently small fixed \(\varepsilon>0\), (2.1)
holds with \(m/2\), and the same construction applies at that fixed
smooth cutoff. Even the smooth kernel \(\cos(2\pi x)\) exhibits the
same mechanism on suitable separated patches.

## 3. Leading local singularity and exact surviving repair

Write \(d(x)=w(x,x)\) and \(r=x-y\). Symmetry and the chain rule imply
\[
 a_x:=\partial_1w(x,x)=\partial_2w(x,x)=\tfrac12d'(x).
\]
Taylor expansion at fixed \(x\) gives
\[
 w(x,x-r)-d(x)=-r a_x+O(r^2),\qquad
 \partial_1w(x,x-r)=a_x+O(r).
\]
Using (1.2) and \((|r|^{-s})'=-sr|r|^{-s-2}\), one obtains
\[
 \boxed{D_w(x,x-r)=\frac{1+s}{2}d'(x)|r|^{-s}
                         +O(|r|^{1-s})+O(1).}                  \tag{3.1}
\]
The bounded term comes from the periodic smooth remainder. For fixed
\(s,w\), constants are locally uniform in \(x\). In particular,
\[
 \lim_{r\to0}\frac{D_w(x,x-r)}{g_s(r)}=\frac{1+s}{2}d'(x).       \tag{3.2}
\]
The first-order weight difference gains a power relative to \(g_s'\),
but generically gains none relative to \(g_s\).

Take the explicit strictly positive periodic weight
\[
 w(x,y)=2+\tfrac12\{\sin(2\pi x)+\sin(2\pi y)\}\ge1 .
\]
At \(x=0\), \(d'(0)=2\pi\), and
\[
 D_w(0,-r)=-\tfrac12\sin(2\pi r)g_s'(r)+\pi g_s(r),\qquad
 \frac{D_w(0,-r)}{g_s(r)}\longrightarrow\pi(1+s)\ne0.            \tag{3.3}
\]
This uses a small local coordinate chart. The sign \(1+s\) is specific
to \(g_s'(x-y)\) and the partial derivative in (1.5). Differentiating
an entire expression containing \(w(x,x)\) is a different formula.

At any point where \(d'(x)=0\), both first derivatives of \(w\) vanish
on that diagonal point. Hence
\[
 w(x,x-r)-d(x)=O(r^2),\quad
 \partial_1w(x,x-r)=O(r),\quad D_w(x,x-r)=O(|r|^{1-s}).          \tag{3.4}
\]
Constant diagonal value gives this improvement uniformly. Conversely,
(3.2) shows that pointwise improvement everywhere requires \(d'\equiv0\).
Cancellations after integration require additional proved structure.

## 4. Deleted-diagonal, iid, and small-particle checks

These are direct finite-sum calculations, not certification of another
lane's decomposed hierarchy. For smooth symmetric \(h\), set
\(h_\mu(x)=\int h(x,y)\mu(y)\,dy\) and \(I_\mu=\iint h\,\mu\mu\).
Then
\[
 P_2[h]=\tfrac14h(x_1,x_2)
       -\tfrac12\{h_\mu(x_1)+h_\mu(x_2)\}+\tfrac12I_\mu,
\]
\[
 P_3[h]=\tfrac19\{h(x_1,x_2)+h(x_1,x_3)+h(x_2,x_3)\}
       -\tfrac13\sum_{i=1}^3h_\mu(x_i)+\tfrac12I_\mu .
\]
For every \(N\), expansion of the empirical product yields
\[
 P_N[h]=\frac12\iint h\,d(\eta_N-\mu)^{\otimes2}
                     -\frac1{2N}\int h(x,x)\,d\eta_N(x),        \tag{4.1}
\]
\[
 P_N[1]=-\frac1{2N},\qquad
 P_N[a\otimes a]=\tfrac12\{(\eta_N(a)-\mu(a))^2-\eta_N(a^2)/N\}.
                                                               \tag{4.2}
\]
Counting the \(N(N-1)\) ordered pairs directly gives
\[
               \mathbb E_{\mu^{\otimes N}}P_N[h]
                                         =-\frac{I_\mu}{2N}.   \tag{4.3}
\]
This remains valid for singular \(h\) whenever the integrals are
absolutely integrable. In Section 2, \(I_\mu>0\), even though
\(h(x,x)=0\). A vanishing spatial diagonal does not imply a mean-zero
statistic with deleted particle labels. For that example, (4.3) alone
rules out the iid-\(\mu\) expectation version of (1.4) when
\(\delta>s\), but not when \(0<\delta\le s\). Section 2's universal
counterexample is stronger and has no such restriction.

A smooth dynamic check isolates the Itô cancellation. Take \(K=b=0\),
\(\mu=1\), \(\nu=1/\beta_N\), and \(a(x)=\cos(2\pi kx)\), \(k\ne0\).
Write \(q=2\pi k\), \(m=\eta_N(a)\), \(r=\eta_N(a^2)\). Direct Itô
calculus gives
\[
 dm=\nu\eta_N(a'')dt+\frac{\sqrt{2\nu}}N\sum_i a'(x_i)dW_i,
 \qquad d[m]=\frac{2\nu}N\eta_N((a')^2)dt,
\]
\[
 dr=\nu\eta_N((a^2)'')dt+
                 \frac{\sqrt{2\nu}}N\sum_i2a(x_i)a'(x_i)dW_i .
\]
Inserting these in \(P_N[a\otimes a]=(m^2-r/N)/2\) cancels the
\(\eta_N((a')^2)\) terms exactly:
\[
 dP_N[a\otimes a]=-2\nu q^2P_N[a\otimes a]dt+
   \frac{\sqrt{2\nu}}N\sum_i(m-a(x_i)/N)a'(x_i)dW_i,             \tag{4.4}
\]
\[
 d[P_N[a\otimes a]]
   =\frac{2\nu}{N^2}\sum_i(m-a(x_i)/N)^2(a'(x_i))^2dt,          \tag{4.5}
\]
\[
 d[P_N[a\otimes a],m]
   =\frac{2\nu}{N^2}\sum_i(m-a(x_i)/N)(a'(x_i))^2dt.            \tag{4.6}
\]
These hold for all \(N\ge2\), including \(N=2,3\), and all configurations.
They are necessary tests of a pair identity, but do not test nonlinear
interaction or the full background-response operator.

## 5. Disposition, limitations, and reproducibility

| Claim | Mathematical disposition | Qualification |
| --- | --- | --- |
| Universal (1.4), arbitrary smooth symmetric nonnegative weights | DISPROVED by (2.3)–(2.5) | Proof SELF_CHECKED, hostile audit pending |
| Universal bound restricted to strictly positive weights | DISPROVED by (2.6)–(2.7) | Finite-configuration existence, not typicality |
| Generic lower singular order in (1.5) | DISPROVED by (3.3) | Pointwise claim |
| Local gain with constant diagonal | PROVED_CANDIDATE, SELF_CHECKED by (3.4) | Fixed smooth weight, one dimension, \(0<s<1\) |
| Diagonal and iid identities | EXACT_IDENTITY, SELF_CHECKED by (4.1)–(4.3) | Specified integrability and iid law |
| Free Fourier pair drift and brackets | EXACT_IDENTITY, SELF_CHECKED by (4.4)–(4.6) | \(K=b=0,\mu=1\), smooth Fourier test |

No temperature regime, fluctuation limit, Gibbs preparation, logarithmic
kernel, or singular Itô formula was certified. Randomly permuting the
deterministic configuration in Section 2 produces an exchangeable law
with the same weighted energy; its first marginal is not \(\mu=1\).
No first-marginal or preparation equivalence is asserted.

The integration consequence is to prohibit the two false assumptions,
while retaining routes with a proved positive-quadratic-form/localization
mechanism or a proved diagonal constraint/cancellation. A route that never
used either false assumption is not demoted by these counterexamples.

Inspected: AGENTS.md, README_FIRST.md, MASTER_PROMPT.md,
CAMPAIGN_PROTOCOLS.md, MODEL_ORCHESTRATION.md, INPUTS/SOURCE_MANIFEST.md,
STATE/STATUS_VOCABULARY.md, and the assigned task/dossier files. To preserve
the fresh-context instruction, other mathematical narratives and constructor
outputs were not consulted. The imported PDF was not a proof input.

Verification: python3 scripts/verify_campaign.py passed before and after
writing this report. Imported note SHA-256:
a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76.
The arguments use exact finite sums, quantile estimates, Gaussian/Fourier
integration and Taylor expansion; no numerical output supplies a proof step.
Only this assigned Markdown report was created. No canonical state,
immutable input, commit, branch, remote, or other worker file was changed.
