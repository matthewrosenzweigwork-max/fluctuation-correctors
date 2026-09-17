# Round 003: statement-only reconstruction of the iid Riesz probability estimate

Date: 2026-09-17 UTC. Task: TASK-024.
Worktree: /private/tmp/hocf-round003-probability-blind-20260917.
Starting commit: 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2.
Status: **PROVED_RECONSTRUCTION; SELF_CHECKED; COMPARISON PENDING**.

The frozen THM-016 probability assertions are proved below from their
statement. This is not a verdict on the unseen constructor's proof.
The present context previously constructed the permitted TASK-021 iid pair
moment prerequisite; that context and its sealed report are reused openly.
The new probability proof is reconstructed without reading TASK-022, its
report, a Round 003 hostile review, root TeX, a comparison, or another
Round 003 worktree. It is not a fresh-session or prerequisite-independent
certification. Root alone compares the sealed constructions and decides
promotion.

All three entries of AUDITS/ROUND_003_PROBABILITY_BLIND_INPUT_SHA256SUMS.txt
were verified before reading the statement. The only mathematical inputs
read were that statement, the frozen model, and the author's own sealed
TASK-021 report. The heat argument below also supplies the real-space input
which was not proved in that prerequisite. No external theorem or remembered
singularity normalization is imported.

## 1. Assertion, quantifiers, and conclusion

Fix an integer \(d\ge1\) and \(0<s<d\). The torus is
\(\mathbb R^d/\mathbb Z^d\), with Haar measure of mass one. Let \(X_i\) be
iid Haar. For every finite \(N\ge2\), distinct labels are used in

\[
 P_N[g]=\frac1{2N^2}\sum_{i\ne j}g(X_i-X_j)
       =\frac1{N^2}\sum_{i<j}g(X_i-X_j).
 \tag{1.1}
\]

The frozen zero-mean Riesz potential has Fourier coefficients

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}
          \frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad k\ne0.
 \tag{1.2}
\]

Let \(\beta_N>0\) be any deterministic sequence, and write

\[
 b_N=\min(\beta_N,1),\qquad \sigma_N=\sqrt{Nb_N}.
 \tag{1.3}
\]

The conclusions reconstructed here are:

1. The potential has an integrable, mean-zero representative, smooth away
   from the origin, and near that origin equals \(|x|^{-s}\) plus a bounded
   smooth remainder. The statistic (1.1) is finite almost surely,
   integrable, and has mean zero. Its second moment is finite precisely
   when \(2s<d\).
2. If \(s\le d/2\), then \(\sigma_NP_N[g]\to0\) in probability for every
   positive temperature sequence.
3. If \(d/2<s<d\), then the same conclusion holds whenever
   \[
      A_N:=b_NN^{4s/d-3}\longrightarrow0.
      \tag{1.4}
   \]
   In particular \(\sqrt N P_N[g]\to0\) in probability for every
   \(0<s<3d/4\).

The logical negation under examination is an admissible fixed \(d,s\),
Haar iid family, and, where applicable, positive sequence satisfying the
displayed condition but violating a stated integrability or probability
conclusion. The proof eliminates that negation for the displayed assertions.
It proves no converse or probability nonconvergence claim.

Section 7 separately proves an additional consequence: the same sufficient
conditions give convergence in \(L^1\), with explicit rates. This strengthens
the mode of convergence and is not silently substituted for the frozen
statement.

## 2. Heat representation and the exact local singularity coefficient

Put \(\tau=(d-s)/2>0\), and let

\[
 h_t(x)=(4\pi t)^{-d/2}e^{-|x|^2/(4t)},\qquad
 p_t(x)=\sum_{n\in\mathbb Z^d}h_t(x+n).
 \tag{2.1}
\]

Integration over translated unit cubes gives \(\int p_t=1\).
The Gaussian Fourier integral gives
\(\widehat p_t(k)=e^{-4\pi^2t|k|^2}\).
The constant multiplying the heat integral is exactly

\[
 B_{d,s}:=\frac{c_{d,s}(4\pi^2)^\tau}{\Gamma(\tau)}
       =\frac{4^\tau\pi^{d/2}}{\Gamma(s/2)}.
 \tag{2.2}
\]

The Bochner integral

\[
 g=B_{d,s}\int_0^\infty t^{\tau-1}(p_t-1)\,dt
       \quad\hbox{in }L^1(\mathbb T^d)
 \tag{2.3}
\]

converges. On \(0<t\le1\), \(\|p_t-1\|_1\le2\). On \(t\ge1\), the
absolutely convergent Fourier series gives

\[
 \|p_t-1\|_1
 \le\sum_{k\ne0}e^{-4\pi^2t|k|^2}
 \le e^{-2\pi^2t}\sum_{k\ne0}e^{-2\pi^2|k|^2}.
 \tag{2.4}
\]

Both bounds are integrable against the time weight. Fubini in (2.3)
therefore gives zero mean and, for \(k\ne0\),

\[
 B_{d,s}\int_0^\infty
       t^{\tau-1}e^{-4\pi^2t|k|^2}\,dt
 =B_{d,s}\Gamma(\tau)(4\pi^2|k|^2)^{-\tau}
 =c_{d,s}|k|^{s-d}.
 \tag{2.5}
\]

This identifies (2.3) with the frozen Fourier normalization. It is real
and even.

Choose the Euclidean representative near zero, and fix \(r_0=1/4\).
For \(0<|x|\le r_0\), subtract the full Euclidean heat integral from (2.3).
Its value is exactly

\[
\begin{aligned}
 B_{d,s}\int_0^\infty t^{\tau-1}h_t(x)\,dt
 &=\frac{4^{-s/2}}{\Gamma(s/2)}
       \int_0^\infty t^{-s/2-1}e^{-|x|^2/(4t)}\,dt\\
 &=|x|^{-s}.
\end{aligned}
\tag{2.6}
\]

The second equality follows by \(u=|x|^2/(4t)\); all factors of \(4\),
\(\pi\), and \(\Gamma(s/2)\) are thereby fixed. Consequently

\[
 g(x)=|x|^{-s}+R(x),
 \tag{2.7}
\]

where the remainder is represented on \(|x|\le r_0\) by

\[
\begin{aligned}
 R(x)=B_{d,s}\bigg[
 &\int_0^1 t^{\tau-1}
     \left(\sum_{n\ne0}h_t(x+n)-1\right)dt\\
 &+\int_1^\infty t^{\tau-1}
     \left(p_t(x)-1-h_t(x)\right)dt\bigg].
\end{aligned}
\tag{2.8}
\]

Here \(R\) extends smoothly across \(x=0\). To justify every derivative,
let \(m\ge0\). Differentiating the Gaussian \(m\) times gives a polynomial
in \(x/\sqrt t\) times \(t^{-(d+m)/2}e^{-|x|^2/(4t)}\).
The polynomial times \(e^{-|x|^2/(8t)}\) is bounded, so

\[
 |D^m h_t(z)|\le C_{d,m}t^{-(d+m)/2}e^{-|z|^2/(8t)}.
 \tag{2.9}
\]

For \(n\ne0\) and \(|x|\le1/4\), \(|x+n|\ge3|n|/4\).
The differentiated image sum in the first integral is thus bounded,
for \(0<t\le1\), by a constant depending on \(d,m\) times
\(t^{-(d+m)/2}e^{-c/t}\), with \(c>0\); split
\(\sum_{n\ne0}e^{-9|n|^2/(128t)}\) into
\(e^{-9/(256t)}\sum_{n\ne0}e^{-9|n|^2/256}\).
Every time-weighted derivative is integrable there. The undifferentiated
constant \(-1\) contributes only \(1/\tau\).

For the second integral, differentiation of the Fourier series bounds
\(D^m(p_t-1)\) by

\[
 e^{-2\pi^2t}
       \sum_{k\ne0}(2\pi|k|)^m e^{-2\pi^2|k|^2}.
 \tag{2.10}
\]

For \(h_t\), (2.9) bounds the weighted derivative by a constant times
\(t^{-(s+m)/2-1}\), integrable on \([1,\infty)\) because \(s>0\).
Dominated differentiation proves the claim about \(R\).
The same small-time Gaussian argument on compact sets avoiding the
origin proves smoothness of \(g\) everywhere else. These pointwise
representations agree almost everywhere with the \(L^1\) integral by
Fubini, so they specify its intended off-origin representative.

For clarity the constants below depend only on the fixed \(d,s\).
For example an explicit finite upper bound \(M_{d,s}\) for
\(\sup_{|x|\le r_0}|R(x)|\) is

\[
\begin{aligned}
 M_{d,s}:=B_{d,s}\bigg[
 &\frac1\tau
 +(4\pi)^{-d/2}
   \int_0^1 t^{-s/2-1}
       \sum_{n\ne0}e^{-9|n|^2/(64t)}\,dt\\
 &+\int_1^\infty t^{\tau-1}
       \sum_{k\ne0}e^{-4\pi^2t|k|^2}\,dt
 +(4\pi)^{-d/2}\frac2s\bigg].
\end{aligned}
\tag{2.11}
\]

All displayed sums and integrals converge by the bounds just proved.
Let \(v_d\) be the volume of the Euclidean unit ball and
\(\omega_{d-1}=dv_d\). The finite number
\[
 G_{d,s}:=\int_{\{\operatorname{dist}(x,0)\ge r_0\}} |g(x)|^2\,dx
 \tag{2.12}
\]
depends only on \(d,s\), since the integrand is smooth on that compact
set and is fixed by (2.3). It introduces no unproved uniformity in another
parameter.

## 3. Integrability, exact mean, and the finite-variance boundary

Let \(\rho(x)=\operatorname{dist}_{\mathbb T^d}(x,0)\).
Equation (2.7) and \(s<d\) imply local integrability, consistent with
(2.3). The origin is the only possible singularity and has zero Haar
measure. For each distinct-label pair, \(X_i-X_j\) is Haar. A finite union
of collision events has probability zero. Thus (1.1) is finite almost
surely and belongs to \(L^1\), with

\[
 \mathbb E|P_N[g]|
       \le\frac{N-1}{2N}\|g\|_1,\qquad
 \mathbb E P_N[g]=0.
 \tag{3.1}
\]

For \(2s<d\), the kernel is in \(L^2\), and its Haar pair kernel is
canonical: integrating either variable gives zero. The permitted
TASK-021 formula therefore gives

\[
 \mathbb E P_N[g]^2
       =\frac{N-1}{2N^3}\|g\|_2^2.
 \tag{3.2}
\]

This coefficient also follows directly: two distinct unordered pair
terms have zero covariance, including when they share one label,
because conditioning on the shared label leaves two zero Haar integrals.
There are \(N(N-1)/2\) diagonal terms in the unordered sum.

For \(2s\ge d\), choose a sufficiently small fixed \(r_1>0\) so that
\(r_1\le r_0\) and \(M_{d,s}r_1^s\le1/2\).
Then (2.7) implies \(g(x)\ge |x|^{-s}/2\) for \(0<|x|<r_1\).
Consequently \(g\notin L^2\), by the integral
\(\int_0^{r_1}t^{d-1-2s}dt\).
The full pair statistic cannot acquire finite variance by cancellation:
its \(L^1\) conditional expectation is exactly

\[
 \mathbb E[P_N[g]\mid X_1,X_2]=\frac1{N^2}g(X_1-X_2).
 \tag{3.3}
\]

Every other pair integrates to zero, whether it shares a conditioned
label or has two unconditioned labels. If \(P_N[g]\) were in \(L^2\),
conditional Jensen would put the right-hand side in \(L^2\), a
contradiction. This proves infinite second moment for every \(N\ge2\)
when \(2s\ge d\), without making a probability-limit inference from it.

## 4. Spatial truncation and all finite-particle centering factors

For \(0<r\le r_0\), set

\[
 g_r(x)=g(x)\mathbf 1_{\{\rho(x)\ge r\}},\qquad
 m_r=\int g_r=-\int_{\{\rho<r\}}g,\qquad
 H_r=g_r-m_r.
 \tag{4.1}
\]

These are real and even, \(g_r\in L^2\), and \(H_r\) has mean zero.
Let

\[
 Z_{N,r}=\frac1{N^2}\sum_{i<j}H_r(X_i-X_j).
 \tag{4.2}
\]

Thus \(\mathbb E Z_{N,r}=0\). To distinguish the three centerings,
define \(F_N[f]=N^{-2}\sum_{i<j}f(X_i-X_j)\), and let \(m_f=\int f\).
For a translation-invariant kernel, the campaign's full background
statistic satisfies, exactly,

\[
\begin{aligned}
 P_N[f]&=F_N[f]-\frac{m_f}{2},&
 \mathbb E F_N[f]&=\frac{N-1}{2N}m_f,&
 \mathbb E P_N[f]&=-\frac{m_f}{2N},\\
 F_N[f-m_f]
     &=F_N[f]-\frac{N-1}{2N}m_f
       =P_N[f]+\frac{m_f}{2N}.
\end{aligned}
\tag{4.3}
\]

In particular \(Z_{N,r}=P_N[g_r]+m_r/(2N)\).
No \(N(N-1)\) denominator is inserted, and \(P_N[g]\) agrees with
\(F_N[g]\) only because \(g\) has zero mean.

Let \(E_{N,r}\) be the event that every distinct-label pair has distance
at least \(r\). Since \(r\le1/4\), the torus ball has volume \(v_dr^d\).
Independence gives the exact single-pair probability and then the union
bound

\[
 \mathbb P(E_{N,r}^{\,c})
   \le {N\choose2}v_dr^d
   \le\frac{v_d}{2}N^2r^d.
 \tag{4.4}
\]

No independence between the various pair events is asserted or needed.
On \(E_{N,r}\), the original and outer bare sums agree. The exact
on-event comparison is

\[
 P_N[g]=Z_{N,r}+\frac{N-1}{2N}m_r.
 \tag{4.5}
\]

The deterministic mean in this formula must not be dropped. Define the
discarded absolute mass \(D(r)=\int_{\{\rho<r\}}|g|\).
The local representation gives the explicit bound

\[
\begin{aligned}
 |m_r|\le D(r)
 &\le \frac{\omega_{d-1}}{d-s}r^{d-s}
                  +M_{d,s}v_dr^d\\
 &\le C_1r^{d-s},\qquad
 C_1:=\frac{\omega_{d-1}}{d-s}
                  +M_{d,s}v_dr_0^s.
\end{aligned}
\tag{4.6}
\]

For the centered outer statistic, the exact canonical variance is

\[
 \operatorname{Var}(Z_{N,r})
   =\frac{N-1}{2N^3}\big(\|g_r\|_2^2-m_r^2\big).
 \tag{4.7}
\]

Set \(K_0=G_{d,s}+2M_{d,s}^2v_dr_0^d\). Squaring
\(|g(x)|\le |x|^{-s}+M_{d,s}\) on the local ball and integrating gives

\[
 \|g_r\|_2^2
   \le K_0+2\omega_{d-1}\int_r^{r_0}t^{d-1-2s}dt.
 \tag{4.8}
\]

For \(s=d/2\), this is
\[
 \|g_r\|_2^2\le K_0+2\omega_{d-1}\log(r_0/r).
 \tag{4.9}
\]
For \(s>d/2\), put \(q=2s-d>0\). Then
\[
 \|g_r\|_2^2\le C_2r^{-q},\qquad
 C_2:=K_0r_0^q+\frac{2\omega_{d-1}}q.
 \tag{4.10}
\]

All constants are independent of \(N,\beta_N,r\).
Multiplying the exact variance by the requested scale yields

\[
 \sigma_N^2\operatorname{Var}(Z_{N,r})
   =\frac{b_N(N-1)}{2N^2}
                \big(\|g_r\|_2^2-m_r^2\big)
   \le\frac{b_N}{2N}\|g_r\|_2^2.
 \tag{4.11}
\]

Equations (4.4), (4.6), and (4.11) are separate bounds for the close-pair
event, deterministic discarded mean, and centered variance.
For every fixed \(\eta>0\), once
\(\sigma_N (N-1)|m_r|/(2N)\le\eta/2\), the event comparison and
Chebyshev imply

\[
 \mathbb P(|\sigma_NP_N[g]|>\eta)
 \le \frac{v_d}{2}N^2r^d
          +\frac{4}{\eta^2}
                \sigma_N^2\operatorname{Var}(Z_{N,r}).
 \tag{4.12}
\]

This estimate does not condition the variance on the close-pair event.
It uses the unconditional variance and so introduces no dependence gap.

## 5. Explicit limits, including the infinite-variance boundary

### The range \(s<d/2\)

There is no truncation to pass here. Equation (3.2) gives

\[
 \mathbb E(\sigma_NP_N[g])^2
   =\frac{b_N}{2N}\left(1-\frac1N\right)\|g\|_2^2
   \longrightarrow0
 \tag{5.1}
\]

for every positive sequence, because \(0<b_N\le1\).

### The endpoint \(s=d/2\)

Choose
\[
 r_N=\min(r_0/2,N^{-3/d}).
 \tag{5.2}
\]
For sufficiently large \(N\) it equals \(N^{-3/d}\). The three bounds
then give, respectively,

\[
\begin{aligned}
 \mathbb P(E_{N,r_N}^{\,c})&\le(v_d/2)N^{-1},\\
 \sigma_N\frac{N-1}{2N}|m_{r_N}|
       &\le(C_1/2)\sqrt{b_N}\,N^{-1},\\
 \sigma_N^2\operatorname{Var}(Z_{N,r_N})
       &\le C_d\,\frac{b_N(1+\log N)}{N}\longrightarrow0.
\end{aligned}
\tag{5.3}
\]

Here one may take \(C_d=K_0/2+3\omega_{d-1}/d\), evaluated at \(s=d/2\).
For each fixed \(\eta>0\), the mean bound is eventually at most \(\eta/2\),
and (4.12) tends to zero. This handles the boundary even though every
finite-\(N\) unregularized second moment is infinite.

### The range \(d/2<s<d\)

Let \(q=2s-d>0\) and \(p=d-s>0\), and suppose (1.4).
All \(A_N\) are positive. Take the explicit radius

\[
 \delta_N=A_N^{1/(2q)},\qquad
 r_N=\min(r_0/2,N^{-2/d}\delta_N).
 \tag{5.4}
\]

Since \(A_N\to0\), the second argument is selected for all sufficiently
large \(N\), and \(\delta_N\to0\). The three error bounds are then

\[
\begin{aligned}
 \mathbb P(E_{N,r_N}^{\,c})
    &\le (v_d/2)\delta_N^d
       =(v_d/2)A_N^{d/(2q)},\\
 \left(\sigma_N\frac{N-1}{2N}|m_{r_N}|\right)^2
    &\le(C_1^2/4)\,Nb_N r_N^{2p}
       =(C_1^2/4)A_N^{1+p/q},\\
 \sigma_N^2\operatorname{Var}(Z_{N,r_N})
    &\le(C_2/2)\frac{b_N}{N}r_N^{-q}
       =(C_2/2)A_N^{1/2}.
\end{aligned}
\tag{5.5}
\]

The powers follow from the exact identities
\(1-4p/d=4s/d-3\) and \(-1+2q/d=4s/d-3\).
Every displayed exponent of \(A_N\) is positive. Thus, first choose the
fixed probability tolerance \(\eta>0\); then let \(N\to\infty\) with
the single predetermined radius (5.4). The deterministic shift is
eventually at most \(\eta/2\), and (4.12) tends to zero.
There is no interchange with a heat-cutoff limit and no unchosen
iterated limit.

For \(b_N=1\), condition (1.4) holds for \(d/2<s<3d/4\); combined with
the preceding cases this proves the stated \(\sqrt N\) conclusion for
every \(0<s<3d/4\). For arbitrary \(b_N\le1\) the same range is automatic.
At \(s=3d/4\), (1.4) is \(b_N\to0\), equivalently \(\beta_N\to0\).
At \(s>3d/4\), (1.4) is equivalent to
\(\beta_NN^{4s/d-3}\to0\), because that condition forces
\(\beta_N\to0\), so eventually \(b_N=\beta_N\).
These are statements about the displayed sufficient condition.

## 6. What failure of the cutoff condition means

For \(q>0\), write a generic spatial cutoff as
\(r_N=N^{-2/d}\delta_N\). The close-pair union-bound expression tends
to zero exactly when \(\delta_N\to0\), and the scalar variance bound
from (4.10) is a constant times \(A_N\delta_N^{-q}\).
The existence of a sequence for which both these *bounds* vanish
requires \(A_N\to0\):
\[
 A_N=(A_N\delta_N^{-q})\delta_N^q\longrightarrow0.
 \tag{6.1}
\]
Conversely (5.4) makes them and the mean bound vanish.
Thus (1.4) characterizes feasibility of these specific scalar sufficient
bounds in the super-\(L^2\) range. It is not proved necessary for
convergence in probability of the statistic. Failure to make a union
bound or Chebyshev estimate vanish is a failure of this proof criterion,
not a lower probability bound.

In particular neither the infinite unregularized second moments nor the
diverging heat-cutoff variances proved in TASK-021 establish nonconvergence
in probability. No critical endpoint nonconvergence or stable limit is
asserted here. The fluctuation scale uses \(b_N=\min(\beta_N,1)\);
replacing it by \(\beta_N\) in the growing-temperature regime would alter
the conclusion.

## 7. Additional proved \(L^1\) consequence

The same spatial decomposition also yields a stronger mode of convergence
under the same sufficient conditions, without using a close-pair event.
This is an additional result of this reconstruction, distinct from the
frozen probability assertion.

Let \(\ell_r=g\mathbf 1_{\{\rho<r\}}\), let \(a_r=\int\ell_r=-m_r\),
and put \(J_r=\ell_r-a_r\). Then \(H_r+J_r=g\) exactly and both terms
have zero Haar mean. Hence, with the same deleted-label normalization,

\[
 P_N[g]=P_N[H_r]+P_N[J_r],\qquad
 \|J_r\|_1\le2D(r).
 \tag{7.1}
\]

The inner term requires only integrability. The triangle inequality
over the unordered sum gives

\[
 \mathbb E|P_N[J_r]|
 \le\frac{N-1}{2N}\|J_r\|_1
 \le\frac{N-1}{N}D(r).
 \tag{7.2}
\]

Cauchy--Schwarz and (4.7) control the outer term. In combination,

\[
 \mathbb E|\sigma_NP_N[g]|
 \le\sqrt{\frac{b_N}{2N}}\|g_r\|_2
            +\sqrt{Nb_N}\,D(r).
 \tag{7.3}
\]

For \(d/2<s<d\), choose \(r=N^{-2/d}\) for all sufficiently large
\(N\) that this is at most \(r_0\). Equations (4.6) and (4.10) give
the explicit estimate

\[
 \boxed{\quad
 \mathbb E|\sigma_NP_N[g]|
  \le \big(\sqrt{C_2/2}+C_1\big)
       \sqrt{b_N}\,N^{2s/d-3/2}
  =\big(\sqrt{C_2/2}+C_1\big)\sqrt{A_N}.
 \quad}
 \tag{7.4}
\]

Both terms have the same power; no probability bound for the close-pair
event is used in this additional argument. At \(s=d/2\), the same choice
and (4.9) give
\[
 \mathbb E|\sigma_NP_N[g]|
       \le C_d\sqrt{\frac{b_N(1+\log N)}{N}}.
 \tag{7.5}
\]
For \(s<d/2\), (5.1) directly gives
\[
 \mathbb E|\sigma_NP_N[g]|
       \le\frac{\|g\|_2}{\sqrt2}\sqrt{\frac{b_N}{N}}.
 \tag{7.6}
\]

In (7.5) one may take
\(C_d=\sqrt{K_0/2+2\omega_{d-1}/d}+C_1\), evaluated at \(s=d/2\).
The constants denoted \(C_d\) in (5.3) and (7.5) are thus specified
separately. The estimates (7.4)--(7.5) hold for every
\(N\ge r_0^{-d/2}\), which ensures the selected radius is at most \(r_0\).

Thus all probability conclusions above hold in \(L^1\) as well.
These estimates do not imply a converse, and their upper-bound power
does not by itself determine a limiting distribution at a boundary.

## 8. Scope, verification, and sealed handoff

The proved object is the bare, initial, iid Haar potential pair.
Nothing identifies it with the actual backward pair corrector.
No estimate is transferred to an evolved interacting or Gibbs law,
and no singular-versus-regularized dynamics comparison is made.
The old energy-floor condition, full microscopic subcriticality, and
microscopic criticality remain separate campaign regimes. The logarithmic
model is excluded. All constants here depend only on the fixed \(d,s\);
no uniform limit in \(s\) at a threshold or in \(d\) is claimed.

The inputs checked before reconstruction were:

| Input | SHA-256 |
|---|---|
| TASK-024 | 4fb3bd838b2fb2ef2a12049760740c761c66c2a3c32cb176f121739990cd2cb7 |
| THM-016 frozen statement | 75e94300f0117f9cb4599e626f25834900ee418a85628b504e71cdb9118018d1 |
| Permitted sealed TASK-021 report | 68ed536685133906877efe7599f1e93300e796ad0b62bb6b228837df08438d5a |

The starting status contained those three input files and their checksum
manifest as untracked supplied files. They remain unchanged. Only this
reconstruction and its supporting exact-check program/output are new
deliverables. No other constructor or reviewer proof was read. No
canonical state, immutable source, root TeX, tracked file, or prior
sealed report was edited; no commit, push, dependency installation,
or child worker was used.

The command

    python3 DISCOVERY_CODE/check_round003_probability_blind_exact.py > DISCOVERY_CODE/round003_probability_blind_exact_output.json

passed **5,483 exact rational/integer checks**. Exhaustive cyclic-group
examples at \(N=2,3,4\) check the global centered decomposition, the
on-event shift, the distinction between campaign and exact expectation
centering, the exact outer variance, the inner absolute-moment factor,
and the close-pair union bound. Separate rational exponent checks cover
the heat normalization, the chosen radii, all three error powers, both
parts of the \(L^1\) estimate, the \(L^2\) boundary, and temperature factors.
The finite cyclic examples verify algebra, not the continuous singularity
or a probability theorem; those are proved in the text. These checks are
same-context evidence and do not create an independent audit.

The input checksum verification was rerun and all three supplied entries
remained unchanged. The campaign verifier

    python3 scripts/verify_campaign.py

passed, including the immutable note and manifest guards.
Both git diff --check and git diff --exit-code passed. A direct check
of the three new deliverables found valid UTF-8, final newlines, and no
trailing whitespace or control characters. Final status contains only
the original four supplied untracked inputs and these three deliverables.
No verification command failed and no environment change was required.

The reconstruction and the separate \(L^1\) consequence are now complete
within the stated initial iid scope. Independent comparison and hostile
review remain for root; this report does not evaluate an unseen proof.
Final hashes are supplied separately. After handoff, these issued bytes
will not be altered; any comparison belongs in a new report.
