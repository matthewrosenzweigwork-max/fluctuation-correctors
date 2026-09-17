# Round 003: exact iid pair moments and Riesz heat-cutoff orders

Date: 2026-09-17 UTC. Task: TASK-021.
Worktree: `/private/tmp/hocf-round003-pair-20260917`.
Starting commit: `a06178658d1e3d458536ff312ca793947212ec67`.
Mathematical status: `PROVED_CANDIDATE`; audit status: `SELF_CHECKED`.
This is a construction, not an audit of the earlier work.

The agent's prior context includes its own smooth coupling, moment, and
Gaussian reconstructions. They are not proof inputs to the exact iid
calculation here. No other Round 003 worker output or worktree was read.
The result below uses the frozen normalization and elementary finite sums,
orthogonal projections, Fourier/Parseval, and lattice estimates. No
real-space singularity constant or external probabilistic theorem is imported.
Root alone owns new theorem identifiers, canonical integration, independent
falsification, and the separate hostile review required before promotion.

## 1. Exact assertion and scope

Let \(\mu\) be a probability density on the unit torus, with its associated
probability measure denoted by the same symbol. Let \(X_1,\ldots,X_N\) be
iid with that law, where \(N\ge2\). Let \(\Phi\) be a real symmetric element
of \(L^2(\mu\otimes\mu)\). All ordered empirical pairs have distinct labels,
and every empirical denominator is \(N^2\), not \(N(N-1)\). The campaign
pair is

\[
 P_N[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
       -\frac1N\sum_i\int\Phi(X_i,y)\,d\mu(y)
       +\frac12\iint\Phi(x,y)\,d\mu(x)d\mu(y).
 \tag{1.1}
\]

The assertion is the exact projection and second-moment formulas (2.4)--(2.8)
and the sharp bound (2.9), for every such datum. Its exact negation is an
admissible instance violating one of those statements. The heat-cutoff
specialization fixes Haar preparation and the precise positive-power Fourier
normalization in the task; its two-sided estimates are stated separately.

No value of \(\Phi(x,x)\) is assumed. Conditional integration defines the
one-variable projection \(\mu\)-almost everywhere. Each distinct-label pair
\((X_i,X_j)\) has law \(\mu\otimes\mu\), so changes in an almost-everywhere
representative do not change (1.1) almost surely. In particular, for a density
the coordinate diagonal has zero product measure and may be left undefined.
All formulas use actual deleted-label sums, never a full empirical product
requiring a diagonal evaluation.

This is an initial iid statement. There is no assertion about an evolved
interacting law, a Gibbs law, or an actual backward pair corrector unless
its precise kernel and law are separately shown to satisfy the stated inputs.

## 2. Orthogonal decomposition and every finite-particle coefficient

Define

\[
\begin{aligned}
 \theta&=\iint\Phi(x,y)\,d\mu(x)d\mu(y),\\
 h(x)&=\int\Phi(x,y)\,d\mu(y)-\theta,\\
 H(x,y)&=\Phi(x,y)-\theta-h(x)-h(y).
\end{aligned}
\tag{2.1}
\]

Jensen's inequality places \(h\) in \(L^2(\mu)\), and \(H\) in
\(L^2(\mu^2)\). They satisfy

\[
 \mu(h)=0,\qquad \int H(x,y)\,d\mu(y)=0
        \quad\hbox{for \(\mu\)-almost every \(x\)},
 \tag{2.2}
\]

and the analogous identity in the other variable. Integrating these identities
against the other factors shows that the constant, the two one-variable
terms, and \(H\) are orthogonal in \(L^2(\mu^2)\). Thus

\[
 \|\Phi\|_{L^2(\mu^2)}^2
       =\theta^2+2\|h\|_{L^2(\mu)}^2+\|H\|_{L^2(\mu^2)}^2.
 \tag{2.3}
\]

Insert (2.1) in the ordered sum in (1.1). The constant occurs \(N(N-1)\)
times. Each \(h(X_i)\) occurs in \(2(N-1)\) ordered positions. After
subtracting the background term, the exact result is

\[
 \boxed{\quad
 P_N[\Phi]= -\frac{\theta}{2N}
       -\frac1{N^2}\sum_{i=1}^N h(X_i)
       +\frac1{N^2}\sum_{1\le i<j\le N}H(X_i,X_j).
 \quad}
 \tag{2.4}
\]

In particular,

\[
 \mathbb E P_N[\Phi]= -\frac{\theta}{2N},\qquad
 \mathbb E[P_N\mid X_i]-\mathbb E P_N=-\frac{h(X_i)}{N^2}.
 \tag{2.5}
\]

The first Hoeffding projection of the statistic is generally nonzero even
though the formula uses product-background centering. Its sum is precisely
the middle term of (2.4); replacing \(N^2\) by a falling-factorial denominator
would change this calculation. The second projection is

\[
 \mathbb E[P_N\mid X_i,X_j]
    -\mathbb E[P_N\mid X_i]-\mathbb E[P_N\mid X_j]
    +\mathbb E P_N=\frac{H(X_i,X_j)}{N^2},\qquad i\ne j.
 \tag{2.6}
\]

The random summands on the two levels in (2.4) are orthogonal. Indeed, an
\(h(X_i)\) and a pair term involving \(i\) have zero covariance by (2.2);
if they do not share a label, independence and centering give zero. Distinct
unordered pair terms have zero covariance: for disjoint label sets use
independence; when they share one label, condition on that label and integrate
the two other independent variables using (2.2). All such products are
integrable by Cauchy--Schwarz, since their individual second moments are finite.
It follows, counting \(N\) singletons and \(N(N-1)/2\) unordered pairs, that

\[
 \operatorname{Var}(P_N[\Phi])
 =\frac{\|h\|_{L^2(\mu)}^2}{N^3}
   +\frac{N-1}{2N^3}\|H\|_{L^2(\mu^2)}^2,
 \tag{2.7}
\]

and therefore

\[
 \boxed{\quad
 \mathbb E P_N[\Phi]^2
 =\frac{\theta^2}{4N^2}
  +\frac{\|h\|_{L^2(\mu)}^2}{N^3}
  +\frac{N-1}{2N^3}\|H\|_{L^2(\mu^2)}^2.
 \quad}
 \tag{2.8}
\]

These are formulas for the campaign \(P_N=U_2/2\), not for a renormalized
mean-zero U-statistic. Multiplication by four gives the second moment for
\(U_2\); multiplication by two gives its mean and first projection.

### Sharp bound

For \(N\ge2\),
\(1/(4N^2)\le(N-1)/(2N^3)\) and
\(1/N^3\le2(N-1)/(2N^3)\). Combining (2.3) and (2.8) gives

\[
 \boxed{\quad
 \mathbb E P_N[\Phi]^2
       \le\frac{N-1}{2N^3}\|\Phi\|_{L^2(\mu^2)}^2,
 \qquad
 \mathbb E|P_N[\Phi]|
       \le\frac{\sqrt{N-1}}{\sqrt2\,N^{3/2}}
                              \|\Phi\|_{L^2(\mu^2)}.
 \quad}
 \tag{2.9}
\]

The second-moment coefficient is sharp. For any nonzero mean-zero
\(u\in L^2(\mu)\), the kernel \(u(x)u(y)\) is canonical: \(\theta=h=0\).
It attains equality. Such a bounded nonzero \(u\) exists for any probability
density, by taking a set of probability strictly between zero and one and
subtracting its probability from its indicator. For \(N>2\), equality in
the second-moment bound holds exactly for canonical kernels, up to the zero
kernel. For \(N=2\), every kernel satisfies the stronger exact identity

\[
 \mathbb E P_2[\Phi]^2=\frac1{16}\|\Phi\|_{L^2(\mu^2)}^2.
 \tag{2.10}
\]

Sharpness is asserted for the second-moment coefficient; the displayed first
absolute-moment estimate is its Cauchy--Schwarz consequence.

## 3. Direct finite-particle tests

For \(\Phi\equiv c\), (1.1) gives
\(P_N=-c/(2N)\). Thus its nonzero squared mean is exactly the first term of
(2.8); a formula that claimed all product-background-centered kernels had
zero mean would fail this test.

For \(\Phi(x,y)=f(x)f(y)\), let \(m=\mu(f)\) and
\(v=\mu((f-m)^2)\). Then
\(\theta=m^2\), \(h=m(f-m)\), and
\(H=(f-m)\otimes(f-m)\). Hence

\[
 \mathbb E P_N[f\otimes f]^2
  =\frac{m^4}{4N^2}+\frac{m^2v}{N^3}
                  +\frac{(N-1)v^2}{2N^3}.
 \tag{3.1}
\]

Taking \(m=0\) tests a canonically degenerate kernel and the sharp coefficient.
Taking \(m\ne0\) tests the first projection. For an additive kernel
\(\Phi(x,y)=c+u(x)+u(y)\), with \(\mu(u)=0\), the canonical pair part
vanishes and

\[
 P_N=-\frac c{2N}-\frac1{N^2}\sum_i u(X_i),\qquad
 \mathbb E P_N^2=\frac{c^2}{4N^2}+\frac{\mu(u^2)}{N^3}.
 \tag{3.2}
\]

At \(N=2\), (2.8) is
\(\theta^2/16+\|h\|^2/8+\|H\|^2/16\), agreeing with (2.10).
At \(N=3\), it is
\(\theta^2/36+\|h\|^2/27+\|H\|^2/27\).
These coefficients are also checked below by exact enumeration from (1.1),
independently of the projection computation within this construction context.

## 4. Haar Riesz heat cutoff: exact norm and exact moment

For the rest of the cutoff calculation take \(\mu\) to be Haar measure on
\(\mathbb T^d\), of mass one. Fix an integer \(d\ge1\) and \(0<s<d\).
Retain exactly the frozen positive-power Fourier sequence

\[
\begin{gathered}
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}>0,\\
 \widehat g_\epsilon(k)=c_{d,s}|k|^{s-d}e^{-4\pi^2\epsilon|k|^2}
           \quad(k\ne0),\qquad \widehat g_\epsilon(0)=0,\qquad\epsilon>0,\\
 \Phi_\epsilon(x,y)=g_\epsilon(x-y).
\end{gathered}
\tag{4.1}
\]

The exponential gives a real even smooth kernel with zero mean.
Translation invariance and the zero Fourier mode imply \(\theta=h=0\),
so this kernel is canonical. Parseval and a change of variables give exactly

\[
 V_\epsilon:=\|\Phi_\epsilon\|_{L^2((\mathbb T^d)^2)}^2
 =\|g_\epsilon\|_{L^2(\mathbb T^d)}^2
 =c_{d,s}^2\sum_{k\ne0}|k|^{2s-2d}e^{-8\pi^2\epsilon|k|^2},
 \tag{4.2}
\]

and

\[
 \mathbb E P_N[\Phi_\epsilon]=0,\qquad
 \mathbb E P_N[\Phi_\epsilon]^2=\frac{N-1}{2N^3}V_\epsilon.
 \tag{4.3}
\]

Nothing in this calculation evaluates the cutoff kernel on an empirical
diagonal. The Fourier constant in (4.1) has not been altered, and no local
real-space asymptotic is needed for (4.2).

## 5. Two-sided cutoff orders with explicit constants

Write

\[
 \alpha=2s-d,\qquad a=8\pi^2,\qquad
 \epsilon_0=(ad)^{-2},\qquad c=c_{d,s},
 \qquad A_-=2d c^2d^{s-d},\qquad A_+=2d3^{d-1}c^2.
 \tag{5.1}
\]

All assertions below hold for every \(0<\epsilon\le\epsilon_0\); all
constants are finite and positive for the fixed \((d,s)\) in their stated
range. No uniformity as \(s\) approaches a threshold is asserted.

The exact max-norm shell \(\{k:|k|_\infty=n\}\), \(n\ge1\), has size
\((2n+1)^d-(2n-1)^d\). The integral form of this polynomial difference gives

\[
 2d n^{d-1}\le(2n+1)^d-(2n-1)^d
                  \le2d3^{d-1}n^{d-1}.
 \tag{5.2}
\]

On this shell, \(n\le|k|\le\sqrt d\,n\). Since \(2s-2d<0\), (4.2) is
therefore bounded by the elementary one-dimensional sums

\[
 A_-\sum_{n\ge1}n^{\alpha-1}e^{-ad\epsilon n^2}
      \le V_\epsilon
      \le A_+\sum_{n\ge1}n^{\alpha-1}e^{-a\epsilon n^2}.
 \tag{5.3}
\]

This proves the following three cases without a remembered lattice asymptotic.

### Subcritical square integrability: \(2s<d\)

Here \(\alpha<0\). The upper sum without its exponential is bounded by
\(1+1/(-\alpha)\), by the integral test. The \(2d\) Euclidean unit modes
give a lower bound. Thus

\[
 2dc^2e^{-a\epsilon_0}\le V_\epsilon
        \le A_+\left(1+\frac1{d-2s}\right).
 \tag{5.4}
\]

Moreover dominated convergence in the Fourier sum yields the finite positive
limit

\[
 V_0=c^2\sum_{k\ne0}|k|^{2s-2d},\qquad
 V_\epsilon\longrightarrow V_0.
 \tag{5.5}
\]

### Borderline: \(2s=d\)

Here \(\alpha=0\). Put \(R=(ad\epsilon)^{-1/2}\). Our choice of
\(\epsilon_0\) ensures \(R\ge2\). For \(n\le R\), the exponential in the
lower sum is at least \(e^{-1}\), so

\[
 \sum_{n\ge1}n^{-1}e^{-ad\epsilon n^2}
 \ge e^{-1}\sum_{n\le R}\frac1n
 \ge e^{-1}\log R
 \ge\frac1{4e}\log(1/\epsilon).
 \tag{5.6}
\]

The harmonic-sum estimate uses
\(\sum_{n=1}^{\lfloor R\rfloor}n^{-1}\ge\log(\lfloor R\rfloor+1)\ge\log R\).
The final inequality uses
\(\log(1/\epsilon)\ge2\log(ad)\).
For \(u=a\epsilon<1\), the decreasing function \(x^{-1}e^{-u x^2}\) gives

\[
\begin{aligned}
 \sum_{n\ge1}n^{-1}e^{-u n^2}
 &\le1+\int_1^\infty x^{-1}e^{-u x^2}dx\\
 &\le1+\tfrac12\log(1/u)+\tfrac12e^{-1}
 \le2\log(1/\epsilon),
\end{aligned}
\tag{5.7}
\]

where the integral after \(u^{-1/2}\) becomes
\(\tfrac12\int_1^\infty e^{-y}y^{-1}dy\le e^{-1}/2\).
The last bound is valid on the already specified interval. Combining with
(5.3),

\[
 \frac{A_-}{4e}\log(1/\epsilon)
       \le V_\epsilon\le2A_+\log(1/\epsilon).
 \tag{5.8}
\]

### Supercritical square integrability: \(2s>d\)

Here \(\alpha>0\). For the lower sum use the integer points
\(R\le n\le2R\), with \(R=(ad\epsilon)^{-1/2}\ge2\). There are at least
\(R/2\) such integers; the power is at least
\(2^{\min(\alpha-1,0)}R^{\alpha-1}\), and the exponential is at least
\(e^{-4}\). Hence

\[
 \sum_{n\ge1}n^{\alpha-1}e^{-ad\epsilon n^2}
 \ge2^{\min(\alpha-1,0)-1}e^{-4}(ad\epsilon)^{-\alpha/2}.
 \tag{5.9}
\]

For the upper sum and \(x\in[n,n+1]\), one has
\(n^{\alpha-1}\le2^{(1-\alpha)_+}x^{\alpha-1}\) and
\(e^{-u n^2}\le e^{-u x^2/4}\). Integration over each unit interval gives

\[
 \sum_{n\ge1}n^{\alpha-1}e^{-u n^2}
 \le2^{(1-\alpha)_+}\int_0^\infty x^{\alpha-1}e^{-u x^2/4}dx
 =2^{\max(\alpha-1,0)}\Gamma(\alpha/2)u^{-\alpha/2}.
 \tag{5.10}
\]

Thus

\[
 L_{d,s}\epsilon^{-(2s-d)/2}
      \le V_\epsilon\le U_{d,s}\epsilon^{-(2s-d)/2},
 \tag{5.11}
\]

with the explicit constants

\[
\begin{aligned}
 L_{d,s}&=A_-2^{\min(\alpha-1,0)-1}e^{-4}(ad)^{-\alpha/2},\\
 U_{d,s}&=A_+2^{\max(\alpha-1,0)}\Gamma(\alpha/2)a^{-\alpha/2}.
\end{aligned}
\tag{5.12}
\]

Equations (5.4), (5.8), and (5.11) concern the **squared** kernel norm.
The norm itself has orders respectively
\(1\), \(\sqrt{\log(1/\epsilon)}\), and
\(\epsilon^{-(2s-d)/4}\).

## 6. Exact iid fluctuation scale and cutoff sequences

Let \(\beta_N>0\) be arbitrary, and put

\[
 b_N=\min(\beta_N,1),\qquad
 \sigma_N=\sqrt{Nb_N}.
\]

For any \(\epsilon>0\), (4.3) gives the exact identity

\[
 \boxed{\quad
 \mathbb E\big(\sigma_NP_N[\Phi_\epsilon]\big)^2
   =\frac{b_N}{2N}\left(1-\frac1N\right)V_\epsilon.
 \quad}
 \tag{6.1}
\]

The finite-particle multiplier lies between \(b_N/(4N)\) and
\(b_N/(2N)\). In particular all comparisons below have constants depending
only on the fixed \(d,s\), uniformly over all positive temperature sequences.
For \(\epsilon_N\to0\), they give these exact necessary-and-sufficient
conditions for **vanishing of the second moment**:

| Range | Scaled second-moment order | Condition for convergence to zero |
|---|---|---|
| \(2s<d\) | \(b_N/N\) | always |
| \(2s=d\) | \(b_N\log(1/\epsilon_N)/N\) | \(b_N\log(1/\epsilon_N)/N\to0\) |
| \(2s>d\) | \(b_N/(N\epsilon_N^{(2s-d)/2})\) | \(b_N/(N\epsilon_N^{(2s-d)/2})\to0\) |

Whenever the indicated second moment vanishes, Cauchy--Schwarz and Markov's
inequality also give convergence in \(L^1\) and in probability. The converse
statement is only about second moments, not about convergence in probability.
For example, divergent second moments alone do not exclude concentration of
rare events with vanishing probability.

For a polynomial cutoff \(\epsilon_N=N^{-\gamma}\), \(\gamma>0\), the
high-singularity row becomes

\[
 \mathbb E(\sigma_NP_N[\Phi_{\epsilon_N}])^2
     \asymp_{d,s,\gamma} b_N N^{-1+\gamma(s-d/2)},\qquad 2s>d.
 \tag{6.2}
\]

At the borderline \(2s=d\), it is comparable to
\(b_N\gamma\log N/N\); below the borderline it is comparable to \(b_N/N\).
These comparisons hold once \(N\) is large enough that
\(N^{-\gamma}\le\epsilon_0\).

### Cutoff \(\epsilon_N=N^{-2/d}\)

The three orders are

\[
 \frac{b_N}{N}\quad(2s<d),\qquad
 \frac{b_N\log N}{N}\quad(2s=d),\qquad
 b_NN^{2s/d-2}\quad(2s>d).
 \tag{6.3}
\]

All tend to zero for every \(0<s<d\) and every \(\beta_N>0\), because
\(b_N\le1\) and \(2s/d-2<0\). This is an iid initial estimate for the
regularized pair with kernel \(g_{\epsilon_N}(x-y)\).

### Cutoff \(\epsilon_N=N^{-4/d}\)

Below and at \(2s=d\), the first two orders in (6.3) remain the same up to
constants. Above it the order is

\[
 b_NN^{4s/d-3}.
 \tag{6.4}
\]

Consequently:

- If \(0<s<3d/4\), the second moment tends to zero for every positive
  temperature sequence.
- If \(s=3d/4\), it tends to zero exactly when \(b_N\to0\), equivalently
  \(\beta_N\to0\). If \(b_N\) is bounded below, the second moment is
  bounded above and below by positive constants.
- If \(3d/4<s<d\), it tends to zero exactly when
  \(b_NN^{4s/d-3}\to0\). This condition forces \(\beta_N\to0\) and is
  equivalently \(\beta_NN^{4s/d-3}\to0\). If \(\beta_N\) is bounded below,
  the second moment diverges with that power of \(N\).

At the frozen microscopic critical scaling
\(\beta_NN^{s/d-1}\to\lambda\in(0,\infty)\), one has \(\beta_N\to\infty\)
and eventually \(b_N=1\). Thus the second cutoff has a nonvanishing
second-moment order at \(s=3d/4\) and divergent order for \(s>3d/4\), while
the first cutoff still has a vanishing second moment. Full subcriticality
\(\beta_NN^{s/d-1}\to0\) by itself does not decide these second-cutoff
conditions, since \(\beta_N\) may tend to zero, stay bounded, or grow within
that regime. The old energy-floor condition and the full subcritical and
critical conditions remain distinct. None of these initial calculations
is a theorem about the critical dynamic limiting law.

## 7. What can be said about the unregularized iid statistic

### The square-integrable range

If \(2s<d\), the unregularized Fourier sequence in (4.1) is square summable.
It defines a unique mean-zero \(L^2\) kernel \(g\), and Parseval gives
\(g_\epsilon\to g\) in \(L^2\). The kernel \(g(x-y)\) is canonical under
Haar preparation and fits Section 2 without any assumed diagonal value.
Thus

\[
 \mathbb E P_N[g(x-y)]^2=\frac{N-1}{2N^3}V_0,
 \qquad
 \sigma_N P_N[g(x-y)]\longrightarrow0\quad\hbox{in }L^2
 \tag{7.1}
\]

for every positive temperature sequence. The exact same formula applied to
\(g_\epsilon-g\) controls the fixed-\(N\) \(L^2\) cutoff passage and any
joint cutoff choice in this range.

### An integrable representative for all \(0<s<d\), without a real-space asymptotic

For completeness the Fourier data also define an \(L^1\) representative in
the other ranges. This can be proved without invoking the local
\(|x|^{-s}\) singularity. Let \(p_t\) be the periodized Gaussian

\[
 p_t(x)=\sum_{n\in\mathbb Z^d}(4\pi t)^{-d/2}
                    e^{-|x+n|^2/(4t)}.
\]

It is nonnegative, has integral one, and has Fourier coefficients
\(e^{-4\pi^2t|k|^2}\), by integration of the Euclidean Gaussian over its
translated unit cubes. Put \(\tau=(d-s)/2>0\) and
\(B_{d,s}=c_{d,s}(4\pi^2)^\tau/\Gamma(\tau)\). Then the Bochner integral

\[
 g=B_{d,s}\int_0^\infty t^{\tau-1}(p_t-1)dt
 \quad\hbox{in }L^1(\mathbb T^d)
 \tag{7.2}
\]

converges: for \(0<t\le1\), \(\|p_t-1\|_1\le2\); for \(t\ge1\), its
absolutely convergent Fourier series gives

\[
 \|p_t-1\|_1\le\sum_{k\ne0}e^{-4\pi^2t|k|^2}
 \le e^{-2\pi^2t}\sum_{k\ne0}e^{-2\pi^2|k|^2}.
 \tag{7.3}
\]

Both are integrable with the indicated time weight. Fubini and
\(\int_0^\infty t^{\tau-1}e^{-ut}dt=\Gamma(\tau)u^{-\tau}\) show that
(7.2) has zero Fourier mode zero and all other Fourier coefficients exactly
\(c_{d,s}|k|^{s-d}\). It is real and even. Moreover
\(p_\epsilon*g=g_\epsilon\). The periodized Gaussian is an approximate
identity: its mass outside a fixed torus neighborhood of zero tends to zero,
and translations are continuous in \(L^1\). The inequality
\(\|p_\epsilon*g-g\|_1
 \le\int p_\epsilon(z)\|g(\cdot-z)-g\|_1dz\)
therefore proves \(g_\epsilon\to g\) in \(L^1\).
These are Fourier/heat-kernel facts; no real-space leading constant is assumed.

For iid Haar samples and each fixed \(N\), this \(L^1\) kernel defines
\(P_N[g(x-y)]\) almost surely and in \(L^1\), with mean zero. Since its
one-variable integrals vanish,

\[
 P_N[g(x-y)]=\frac1{N^2}\sum_{i<j}g(X_i-X_j),\qquad
 \mathbb E|P_N[g_\epsilon]-P_N[g]|
       \le\frac{N-1}{2N}\|g_\epsilon-g\|_1\longrightarrow0.
 \tag{7.4}
\]

For \(2s\ge d\), the Fourier sequence is not square summable, by (5.8) or
(5.11); hence this \(L^1\) representative is not in \(L^2\). In fact the
unregularized pair has infinite second moment for every fixed \(N\ge2\).
If it were in \(L^2\), Jensen's inequality for its conditional expectation
given \(X_1,X_2\) would put that conditional expectation in \(L^2\). But
the canonical zero projections give exactly

\[
 \mathbb E[P_N[g]\mid X_1,X_2]=\frac1{N^2}g(X_1-X_2),
 \tag{7.5}
\]

contradicting \(g\notin L^2\). The conditional expectation is legitimate
in \(L^1\); pair terms sharing one of these labels integrate to zero and
the remaining pair terms have zero mean. Thus the failure of an
unregularized finite-variance estimate is proved, while the random statistic
itself is well-defined.

No unregularized probability limit in these ranges follows from (7.4) and
the cutoff variance estimates alone. After multiplication by the fluctuation
scale, the available comparison here is only

\[
 \mathbb E|\sigma_N(P_N[g_{\epsilon_N}]-P_N[g])|
 \le\sigma_N\frac{N-1}{2N}\|g_{\epsilon_N}-g\|_1.
 \tag{7.6}
\]

This would suffice if its right-hand side were proved to vanish, but no
quantitative rate sufficient for a specified joint choice is asserted by
the mere \(L^1\) approximate-identity argument. In particular nonvanishing
or diverging cutoff variances are not nonconvergence-in-probability results
for either the cutoff or unregularized statistic.

## 8. Interface to the actual corrector and dynamics

Formula (2.8) applies directly to the actual deterministic initial pair
kernel \(\Phi_0^N\) if it belongs to \(L^2(\mu_0^2)\), with its own exact
three projections. In particular the sharp sufficient initial-corrector
condition is

\[
 \frac{\min(\beta_N,1)}{N}
                 \|\Phi_0^N\|_{L^2(\mu_0^2)}^2\longrightarrow0,
 \tag{8.1}
\]

which implies \(\sigma_N\mathbb E|P_N[\Phi_0^N]|\to0\).
The full projection formula can be sharper than (8.1) for kernels dominated
by their first projection. No identification of \(\Phi_0^N\) with
\(g_\epsilon(x-y)\) is made: the actual backward pair equation has its own
forcing, response terms, terminal condition, and diagonal behavior, and its
norm must be estimated from that equation or another proved input.

At positive time, the interacting particle law is generally not a product.
The orthogonality step proving (2.7) then fails without additional quantitative
information about its marginals or another law-specific argument. The
calculation transfers neither to that law nor to Gibbs preparation merely
because the same kernel occurs. The present theorem is an initial iid pair
interface, not a singular corrector or dynamic fluctuation theorem.

## 9. Verification and handoff

The asserted moment and sharp bound have complete finite-sum proofs. The
cutoff estimates have explicit lower and upper constants and parameter
quantifiers, with no imported singularity asymptotic. The integrable
unregularized representative and its infinite second moment above the
square-integrability threshold are separately proved in Section 7. No
unverified reference is load bearing.

Current inputs actually read or verified are the TASK-021 card, the frozen
model, and the applicable already-read campaign instructions at the same
published base. Initial repository status contained only the untracked task
card. Input SHA-256 values:

| Input | SHA-256 |
|---|---|
| TASK-021 | `b9badf089117f0bfe711360600f76a5338ed709c46c57c710808c232f980b56d` |
| ROUND_001_MODEL.md | `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57` |
| AGENTS.md | `cc3a478358f1fcb3ccf472615c715acfdef575d9a80b5aa49417593a25825ed3` |

This report and its supporting exact coefficient program/output are the only
new deliverables. Canonical state, immutable inputs, existing reports,
tracked files, and prior sealed reports are unchanged. No commit, push,
dependency installation, child worker, remote mutation, or TeX edit was made.
Root alone assigns the new theorem identifier and arranges the required
independent falsification and hostile review. The final handoff contains no
mathematical LaTeX.

The command
`python3 DISCOVERY_CODE/check_round003_iid_pair_exact.py > DISCOVERY_CODE/round003_iid_pair_exact_output.json`
passed **5,500 exact rational/integer checks** under Python 3.9.6. It
enumerates all samples for twelve kernel/distribution combinations at
\(N=2,3,4,5\), starting from the ordered sum (1.1). The checks include the
pointwise decomposition, mean, variance, second moment, both conditional
projections, the sharp bound, the constant and separable tests, canonical
equality, and the every-kernel equality at \(N=2\). Separate exact checks
cover the lattice shell inequalities, temperature multiplier, and both
polynomial cutoff exponents. The finite probability spaces are realizable
as cellwise constant kernels on a torus partition with the given cell
probabilities. This is computational support within the construction
context, not independent verification or a replacement for the proofs.

The first invocation exposed an annotation compatibility issue with the
installed Python 3.9 interpreter; adding postponed annotation evaluation
fixed it. No mathematical assertion failed and no environment change was
made. The retained output is from the successful complete run.

`python3 scripts/verify_campaign.py` passed, including the immutable source
and manifest guards. `git diff --check` passed, and a direct check of the
three new deliverables found no trailing whitespace, control characters, or
missing final newline. The final repository status contains only these
three deliverables and the pre-existing untracked task card; no tracked
file changed. Final SHA-256 hashes are supplied separately; issued bytes
will not be edited after handoff.
