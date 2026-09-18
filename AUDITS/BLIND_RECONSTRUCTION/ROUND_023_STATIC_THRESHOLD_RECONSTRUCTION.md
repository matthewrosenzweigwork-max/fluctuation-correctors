# AUD065 — whole static threshold reconstruction

TASK100 / THM045. Prepared in the prescribed isolated worktree from published
base 64ac0538dff37a37d0883661b401ad04c311a5e5. The eight overlaid inputs
match the frozen SHA-256 manifest exactly.

**Verdict: the entire existential conjunction is reconstructed below.**
The construction gives bounded smooth densities, the exact symmetries and
marginals, a uniform separation constant, pointwise negative energy, and the
stated nonzero limit for the literal deleted and Haar-centered source.
No failed mathematical line was identified in this reconstruction.
This is a statement-only reconstruction, not the separate hostile audit or a
canonical promotion. It is not an iid-prepared dynamical counterexample.

## 1. Assertion, exact negation, and scope

Work on \(\mathbb T^4=\mathbb R^4/\mathbb Z^4\), with Haar mass one and
characters \(e^{2\pi i k\cdot x}\). The fixed real even kernel satisfies
\(\widehat g(0)=0\), \(\widehat g(k)=|k|^{-2}\) for \(k\ne0\);
put \(K=-\nabla g\) and \(h(x)=\cos(4\pi x_1)\). Every tuple has
\(N=m^4\) particles. The definitions are exactly
\[
 H_N(X)=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
 J_h(x,y)=K(x-y)\cdot(\nabla h(x)-\nabla h(y)),
\]
\[
 P_N[J_h](X)=\frac1{2N^2}\sum_{i\ne j}J_h(x_i,x_j)
 -\frac1N\sum_i A_h(x_i)+\frac12\int A_h,\qquad
 A_h(x)=\int_{\mathbb T^4}J_h(x,y)\,dy.
 \tag{1.1}
\]

THM045 asserts the existence of fixed \(a,c>0\), an integer \(m_0\), and
a sequence of bounded \(C^\infty\) probability densities \(F_{m^4}\), for
every integer \(m\ge m_0\), with all stated symmetry, marginal, separation
and energy properties, and with
\[
 \lim_{m\to\infty}m^2\mathbb E_{F_{m^4}}|P_{m^4}[J_h]|
          =16\pi^3a^2.
 \tag{1.2}
\]

Its exact negation quantifies over every choice of \(a,c,m_0\) and every
candidate sequence: either at least one required finite-\(m\) property
fails for some \(m\ge m_0\), or the limit in (1.2) fails to exist or has a
different value. Failure of one construction would not establish this
negation. Sections 2–8 construct a sequence satisfying all clauses
simultaneously, thereby refuting the exact negation.

No preparation, time evolution, diffusivity, temperature, entropy, or
Gaussian fluctuation assertion is attached to this sequence.

## 2. Sources and normalization

The eight allowed files are preserved byte-for-byte in the attached
inputs tree. The mathematical source facts used are:

| Allowed source | Facts checked here | Scope not imported |
|---|---|---|
| TASKS/ACTIVE/ROUND_001_MODEL.md | Unit torus, Fourier and deleted-label conventions | No dynamical conclusion |
| MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md, §§2–3 | Heat representation, local coefficient, integrable force, Coulomb measure | No propagator or older audit status |
| MEMORANDA/ROUND_010_ACTUAL_LAW_FALSIFICATION.md, §3 | Smooth energy self subtraction | No actual-law estimate transferred |
| MEMORANDA/ROUND_016_SOURCE_EXTENSION.md, §§2, 4–6 | Coulomb contraction and centered smooth-source algebra | No source-decay, density, or dynamic theorem |

All load-bearing facts from these rows are rederived here. No linked
file, unprovided reference, or external literature was consulted.

Let
\[
 p_t(z)=\sum_{n\in\mathbb Z^4}(4\pi t)^{-2}e^{-|z+n|^2/(4t)}.
\]
Unfolding the Gaussian gives Fourier coefficients
\(e^{-4\pi^2t|k|^2}\), positivity, and mass one. Therefore
\[
 g(z)=4\pi^2\int_0^\infty(p_t(z)-1)\,dt
 \tag{2.1}
\]
holds in \(L^1\), with the required nonzero coefficients \(1/|k|^2\).
At small times \(\|p_t-1\|_1\le2\); at large times the nonconstant
Fourier series decays exponentially. These bounds justify the integral
and Fourier calculation.

The central Euclidean Gaussian satisfies, by \(v=|z|^2/(4t)\),
\[
 4\pi^2\int_0^\infty(4\pi t)^{-2}e^{-|z|^2/(4t)}dt=|z|^{-2}.
\]
Noncentral lattice terms at small times and large-time remainders can
be differentiated arbitrarily often in a ball of radius less than
\(1/3\). Hence
\[
 g(z)=|z|^{-2}+H(z),\quad H\in C^\infty,\qquad
 K(z)=2z|z|^{-4}-\nabla H(z).
 \tag{2.2}
\]
In particular \(g,K\in L^1\). With
\(\delta(z)=\operatorname{dist}_{\mathbb T^4}(z,0)\), compactness away
from zero gives
\[
 |D^2g(z)|\le C\delta(z)^{-4},\qquad
 |D^jK(z)|\le C_j\delta(z)^{-3-j}\quad(0\le j\le3).
 \tag{2.3}
\]

The flux of \(2z|z|^{-4}\) through a small three-sphere is
\(2|\mathbb S^3|=4\pi^2\). Integration on the punctured torus, whose
inner normal is \(-z/|z|\), identifies this atom; the smooth remainder
has vanishing boundary flux. Fourier coefficients then identify the
full measure, including its zero coefficient:
\[
 D:=\operatorname{div}K=4\pi^2(\delta_0-dz).
 \tag{2.4}
\]
Fourier uniqueness follows by heat-convolving the distributional
difference and testing the resulting smooth equality before removing
the heat parameter. This does not substitute the punctured classical
density for the measure.

Oddness and integrability give \(\int K=0\). Distributional integration
by parts against the smooth test \(h\) gives
\[
 A_h(x)=-\int K(x-y)\cdot\nabla h(y)\,dy
       =-4\pi^2h(x),\qquad \int A_h=0.
 \tag{2.5}
\]
For the sign, \(K\) has multiplier \(-2\pi i k/|k|^2\); contraction
with \(\nabla h\) gives \(+4\pi^2h\) before the minus sign in \(A_h\).
Thus the unchanged literal source is
\[
 P_N[J_h](X)=\frac1{2N^2}\sum_{i\ne j}J_h(x_i,x_j)
                         +4\pi^2\eta_N(h).
 \tag{2.6}
\]
The background in this formula remains present throughout.

## 3. Negative grid energy and the exact self coefficient

Write \(R=H(0)\). Its strict negative sign will be proved, not assumed.
Set \(\vartheta(u)=\sum_{n\in\mathbb Z}e^{-\pi u n^2}\).
The Gaussian Fourier calculation gives
\(\vartheta(u)=u^{-1/2}\vartheta(1/u)\). Subtracting the central
Euclidean Gaussian in (2.1), and putting \(u=4\pi t\), yields
\[
 R=\pi\int_0^\infty[\vartheta(u)^4-1-u^{-2}]\,du
   =2\pi\left\{\int_1^\infty[\vartheta(u)^4-1]\,du-1\right\}.
 \tag{3.1}
\]
Both improper integrals converge absolutely. The second equality
uses the Gaussian duality and the substitution \(u\mapsto1/u\).

Since \(\pi>3\) and the first five positive terms in the series for
\(e^3\) exceed \(16\), we have \(q=e^{-\pi}<1/16\). By \(n^2\ge n\),
\[
 \vartheta(1)\le1+\frac{2q}{1-q}<\frac{17}{15},\qquad
 (17/15)^4-1<1.
\]
Nonnegative termwise integration gives
\[
 \int_1^\infty[\vartheta(u)^4-1]\,du
 =\sum_{k\ne0}\frac{e^{-\pi|k|^2}}{\pi|k|^2}
 \le\frac{\vartheta(1)^4-1}{\pi}<\frac13.
\]
Consequently
\[
 R<-\frac{4\pi}{3}.
 \tag{3.2}
\]
No numerical approximation is needed for this sign.

Let \(\Lambda_m=(m^{-1}\mathbb Z/\mathbb Z)^4\), with \(N=m^4\).
For fixed \(\varepsilon>0\), summing the absolutely convergent Fourier
series of \(g_\varepsilon=p_\varepsilon*g\) on the grid gives
\[
 \sum_{z\in\Lambda_m}g_\varepsilon(z)=m^2g_{m^2\varepsilon}(0).
 \tag{3.3}
\]
This sum includes the smooth self term. Moreover
\[
 g_\varepsilon(0)=\frac1{4\varepsilon}+R+o(1).
 \tag{3.4}
\]
The singular part follows by integrating \(|z|^{-2}\) against the
four-dimensional Euclidean heat kernel; the smooth part tends to
\(R\), and the periodized tails are exponentially small.
Subtract \(g_\varepsilon(0)\) from (3.3) and let
\(\varepsilon\downarrow0\) with \(m\) fixed. The divergent parts
cancel exactly, so
\[
 \sum_{z\in\Lambda_m\setminus\{0\}}g(z)=(m^2-1)R,\qquad
 H_N(\Lambda_m)=\tfrac12(m^2-1)R.
 \tag{3.5}
\]
The last half is from unordered pairs with coefficient \(1/N\).
No singular self value has been assigned. For \(m\ge2\),
\[
 H_N(\Lambda_m)\le-\frac{\pi}{2}m^2.
 \tag{3.6}
\]

## 4. A deterministic deformation preserves the energy sign

Define
\[
 u(x)=\sin(2\pi x_1)e_1,\qquad T_t(x)=x+t\,u(x).
 \tag{4.1}
\]
For \(|t|\le t_0=1/(4\pi)\), this is a smooth torus diffeomorphism
with lower Lipschitz constant \(1/2\). Its first coordinate is an
increasing degree-one circle map with derivative between \(1/2\)
and \(3/2\); the other coordinates do not change. Also
\(|u(x)-u(y)|\le2\pi\operatorname{dist}(x,y)\).

The grid shell estimate
\[
 \frac1{m^4}\sum_{\substack{r\in\Lambda_m\\0<\delta(r)\le b}}
                \delta(r)^{-2}\le Cb^2\quad(0<b\le1)
 \tag{4.2}
\]
holds uniformly in \(m\). The sum is empty if \(b<1/m\).
Indeed take shortest representatives \(r=k/m\). A unit-thickness
integer shell of radius \(j\) has \(O(j^3)\) vectors, giving
\(m^{-2}\sum_{1\le |k|\le mb}|k|^{-2}\le Cb^2\).
Increasing the fixed constant covers the full torus. This also
bounds the complete normalized sum.

Put \(E_m(t)=H_N((T_tz)_{z\in\Lambda_m})\).
Every grid force is zero:
\(\sum_{r\in\Lambda_m\setminus\{0\}}\nabla g(r)=0\) by oddness;
self-inverse half-period differences have zero gradient individually.
Thus \(E_m'(0)=0\). Differentiating the collision-free finite sum
twice and using (2.3), (4.1), (4.2) gives
\[
 |E_m''(t)|\le\frac C{2N}\sum_{x\ne y}
       \delta(x-y)^{-4}|u(x)-u(y)|^2\le C_HN.
 \tag{4.3}
\]
Hence, for a fixed finite positive \(C_E\),
\[
 |E_m(t)-E_m(0)|\le C_ENt^2,\qquad |t|\le t_0.
 \tag{4.4}
\]
Choose once and for all
\[
 0<a\le\min\{t_0,\sqrt{\pi/(4C_E)}\},\qquad
 t_m=a/m,\qquad Y_m=(T_{t_m}z)_{z\in\Lambda_m}.
 \tag{4.5}
\]
This is a nonempty interval; \(C_E\) can be increased if necessary.
For every \(m\ge2\), (3.6) and (4.4) imply
\[
 H_N(Y_m)\le-\frac{\pi}{4}m^2,\qquad
 \min_{i\ne j}\operatorname{dist}(Y_{m,i},Y_{m,j})\ge\frac1{2m}.
 \tag{4.6}
\]
Thus the positive continuum cost of the deformation does not consume
the negative discrete energy margin.

## 5. Singular Taylor and quadrature estimates for the original source

Let \(h_\theta(x)=h(x+\theta)\) and
\[
 S_m(t,\theta)=P_N[J_{h_\theta}]((T_tz)_{z\in\Lambda_m}).
 \tag{5.1}
\]
Translation invariance of \(K\) identifies this with
\(P_N[J_h]((T_tz+\theta)_{z\in\Lambda_m})\).

A Taylor expansion requires a bound uniform in \(m,\theta\).
For \(0\le j\le3\),
\[
 \left|\partial_t^jJ_{h_\theta}(T_tx,T_ty)\right|
       \le C_j\delta(x-y)^{-2}\quad(x\ne y,\ |t|\le t_0).
 \tag{5.2}
\]
Each derivative on \(K\) contributes
\(D^\ell K(T_tx-T_ty)[u(x)-u(y)]^\ell\), bounded by
\(C\delta(x-y)^{-3}\). Each remaining factor is a difference
between the values at \(x,y\) of the same uniformly smooth field,
so it is \(O(\delta(x-y))\). This proves (5.2), including all mixed
derivative placements. The background in (2.6) has bounded smooth
derivatives. Consequently (4.2) gives
\[
 \sup_{m,\theta,|t|\le t_0}|\partial_t^3S_m(t,\theta)|<\infty.
 \tag{5.3}
\]

For \(m\ge4\) there are exact cancellations:
\[
 S_m(0,\theta)=\partial_tS_m(0,\theta)=0.
 \tag{5.4}
\]
For the first equality fix a grid difference \(r=x-y\). The sum
over \(x\) of \(\nabla h_\theta(x)-\nabla h_\theta(x-r)\) is zero,
and the grid mean of \(h_\theta\) is zero. In the first derivative,
every term has first-coordinate frequencies \(\pm2\pm1\), namely
\(\pm1,\pm3\), in the common variable \(x\). Their grid means vanish
for \(m\ge4\). This covers both derivative placements in the pair
term and the derivative of the background. No linear term is
discarded on heuristic size grounds.

Let \(S(t,\theta)\) denote the same centered expression with the
smooth probability measure \(T_{t\#}dx\) replacing the grid measure.
Then
\[
 \partial_t^2S_m(0,\theta)\longrightarrow
           \partial_t^2S(0,\theta)
 \quad\text{uniformly in }\theta.
 \tag{5.5}
\]
To justify the singular quadrature, exclude
\(\delta(x-y)\le b\) by a smooth cutoff. Outside it the derivative
kernel is smooth, so ordinary product-grid Riemann sums converge.
The omitted discrete sum is at most \(Cb^2\) by (5.2), (4.2);
the omitted integral has the same bound by integration in dimension
four. First send \(m\to\infty\), then \(b\downarrow0\).
The background is an ordinary smooth Riemann sum. Uniformity in
\(\theta\) follows also from the two-dimensional span of
\(\cos(4\pi\theta_1),\sin(4\pi\theta_1)\).

Let \(q_t\) be the density of \(T_{t\#}dx\). The Jacobian formula gives
in every fixed smooth norm
\[
 q_t=1-t\,\operatorname{div}u+O(t^2)
       =1-2\pi t\cos(2\pi x_1)+O(t^2).
 \tag{5.6}
\]
Since \(J_{h_\theta}\in L^1(dx\,dy)\), the exact original background
subtractions imply
\[
 \begin{split}
 S(t,\theta)&=\frac12\iint J_{h_\theta}(x,y)
                   (q_t(x)-1)(q_t(y)-1)\,dx\,dy\\
 &=\int\nabla h_\theta(x)\cdot[K*(q_t-1)](x)(q_t(x)-1)\,dx.
 \end{split}
 \tag{5.7}
\]
The last identity uses oddness and exchange of variables. All terms
are absolutely integrable because \(K\in L^1\) and \(q_t\) is bounded.
This continuum identity does not assign a singular diagonal value
to an atomic measure.

For \(r(x)=-2\pi\cos(2\pi x_1)\), the fixed Fourier multiplier gives
\[
 (K*r)(x)=-4\pi^2\sin(2\pi x_1)e_1.
 \tag{5.8}
\]
Combining this with
\(\nabla h_\theta=-4\pi\sin(4\pi x_1+4\pi\theta_1)e_1\), we get
\[
 S(t,\theta)=-8\pi^4t^2\cos(4\pi\theta_1)+O(t^3),\qquad
 \partial_t^2S(0,\theta)=-16\pi^4\cos(4\pi\theta_1).
 \tag{5.9}
\]
The two factors \(1/2\) are from
\(\sin(2\pi x)\cos(2\pi x)=\frac12\sin(4\pi x)\) and
\(\int_0^1\sin(4\pi x+\phi)\sin(4\pi x)dx=\frac12\cos\phi\).
The remainder is uniform in \(\theta\) by (5.6), (5.7).

Taylor's formula, with (5.3)–(5.5), now proves
\[
 \sup_\theta\left|
       m^2S_m(a/m,\theta)+8\pi^4a^2\cos(4\pi\theta_1)
                \right|\longrightarrow0.
 \tag{5.10}
\]
Indeed the scaled cubic remainder is \(O(a^3/m)\), and the quadratic
term is \((a^2/2)\partial_t^2S_m(0,\theta)\). This is the required
finite-particle singular source estimate at the threshold scale.

## 6. Bounded smooth densities with all exact symmetries

Choose a nonnegative normalized \(C^\infty_c\) function \(b\) on
\(\mathbb R^4\) supported in the closed unit ball; for example normalize
\(\exp[-1/(1-|z|^2)]\) on the open unit ball and extend by zero.
Set \(\epsilon_m=m^{-8}\) and let \(b_{\epsilon_m}\) be its
periodization after the rescaling \(\epsilon_m^{-4}b(z/\epsilon_m)\).

Independently choose a Haar shift \(\Theta\), a uniform permutation
\(\Pi\) of the \(N\) labels, and independent jitters \(\xi_i\) with
density \(b_{\epsilon_m}\). Define
\[
 X_i=Y_{m,\Pi(i)}+\Theta+\xi_i.
 \tag{6.1}
\]
The law has the explicit density
\[
 F_N(x_1,\ldots,x_N)=\frac1{N!}\sum_\pi\int_{\mathbb T^4}
     \prod_{i=1}^Nb_{\epsilon_m}(x_i-\theta-Y_{m,\pi(i)})\,d\theta.
 \tag{6.2}
\]
This is nonnegative, bounded and \(C^\infty\) for each fixed \(N\);
differentiate under the finite sum and compact integral.
For example it is bounded by \(\|b_{\epsilon_m}\|_\infty^N\).
Integrating the product gives total mass one. No bound uniform in
\(N\) is asserted.

Permutation invariance follows by relabeling the sum. Simultaneous
translation is absorbed by the Haar shift. Integrating out all but
one coordinate gives
\(\int b_{\epsilon_m}(x-\theta-y)d\theta=1\), so each one-body
marginal is exactly Haar. No asymptotic marginal argument is used.

Every point of the support is a limit of configurations (6.1) with
\(|\xi_i|\le\epsilon_m\). For \(m\ge2\),
\[
 \min_{i\ne j}\operatorname{dist}(X_i,X_j)
       \ge\frac1{2m}-2m^{-8}\ge\frac1{4m}.
 \tag{6.3}
\]
The same estimate holds on the closed support by continuity.
Throughout a segment of these perturbations each separation is at
least \(1/(4m)\). Using \(|\nabla g|\le C\delta^{-3}\) in each pair,
\[
 |H_N(X)-H_N(Y_m)|\le CNm^3\epsilon_m=Cm^{-1}.
 \tag{6.4}
\]
Permutation and common translation do not change energy.
Choose \(m_0\ge4\) large enough that this error is at most
\((\pi/8)m^2\). Equations (4.6), (6.4) imply
\[
 H_N(X)\le-\frac{\pi}{8}m^2
 \quad\text{throughout the support of }F_N.
 \tag{6.5}
\]
The single fixed constant \(c=1/8\) now works in both the separation
and the energy conditions.

## 7. Absolute expectation and the exact nonzero limit

First spatial derivatives of \(J_h(x,y)\) are bounded by
\(C\delta(x-y)^{-3}\): a derivative on \(K\) is accompanied by the
gradient difference \(O(\delta)\), and all other terms use
\(K=O(\delta^{-3})\) and bounded derivatives of \(h\).
The background is smooth. The same perturbation argument, with the
source normalization \(1/(2N^2)\), therefore yields
\[
 \sup_{\theta,\pi,|\xi_i|\le\epsilon_m}
 \left|P_N[J_h](Y_{m,\pi}+\theta+\xi)
                -P_N[J_h](Y_m+\theta)\right|
       \le Cm^3\epsilon_m=Cm^{-5}.
 \tag{7.1}
\]
This is pointwise before expectation or absolute value.
Combine it with (5.10) and
\(\big||v|-|w|\big|\le|v-w|\). Uniform convergence gives
\[
 \begin{split}
 \lim_{m\to\infty}m^2\mathbb E_{F_N}|P_N[J_h]|
 &=8\pi^4a^2\int_0^1|\cos(4\pi\theta_1)|\,d\theta_1\\
 &=8\pi^4a^2\frac2\pi=16\pi^3a^2>0.
 \end{split}
 \tag{7.2}
\]
Since \(m^2=\sqrt N\), this is precisely the requested limit.
The signed expectation is instead zero, because common-translation
averaging kills the nonzero Fourier test. It has not been mistaken
for an estimate of the absolute source.

## 8. Singular passage and limiting order

Every finite-particle evaluation is off the collision set, uniformly
on each fixed-\(m\) support. No singular value on a deleted diagonal
is assigned. Haar integrals are absolutely convergent because
\(|J_h(x,y)|\le C\delta(x-y)^{-2}\) and \(K\in L^1\).
Integration by parts in (2.5) is against a smooth test and retains
both the atom and the constant compensation.

For the prescribed heat regularization,
\(K_\varepsilon\to K\) in \(L^1\). The Haar contractions consequently
converge uniformly, and their exact regularized values are
\[
 A_{h,\varepsilon}=-4\pi^2e^{-16\pi^2\varepsilon}h,\qquad
 \int A_{h,\varepsilon}=0.
 \tag{8.1}
\]
On any fixed closed set away from zero, \(g_\varepsilon\) and its
derivatives converge uniformly to those of \(g\). To check this,
split by a smooth local cutoff: convolution of the smooth local
part is an approximate identity, and differentiated heat tails
from the separated remainder are exponentially small.
Thus each fixed-\(m\) deleted sum and its expectation have the stated
singular limit. The only energy self subtraction is explicitly
handled in (3.3)–(3.5).

The order of operations is: fix \(m\) for any heat removal; prove
uniform singular derivative bounds; remove a separate diagonal
cutoff in the Riemann-sum argument; insert \(t=a/m\); add jitter
of radius \(m^{-8}\); then send \(m\to\infty\).
No uniform \(N\)-body density estimate or unjustified interchange
of singular limits is required.

## 9. Independent falsification probes and local adversarial review

The proof above does not rely on finite computation. The attached
new diagnostic uses exact Gaussian rational Fourier arithmetic and
a separate direct finite-label evaluation, followed by an approximate
calculation for the actual singular grid.

In angle coordinates \(D=(2\pi)^{-1}\partial_x\), the pushforward
density has expansion
\[
 q_t=1+(2\pi t)(-Du)+(2\pi t)^2\tfrac12D^2(u^2)+O(t^3).
 \tag{9.1}
\]
For \(u=\sin(2\pi x)\), \(h=\cos(4\pi x)\), the coefficient of
\((2\pi)^4t^2\) in the raw pair term is \(-1\), whereas the
subtracted background has coefficient \(-1/2\); the literal
source has coefficient \(-1/2\). Dropping the background therefore
doubles the answer. The diagnostic independently calculates these
coefficients for several frequencies, checks finite-label formulas,
and detects eight deliberate coefficient mutations.

For a different singular diagnostic, average \(g\) over the three
transverse grid directions. For \(0<z<1\), the result and its force are
\[
 \begin{split}
 V_m(z)&=2\pi^2(z^2-z+1/6)\\
 &\quad+\sum_{\ell\in\mathbb Z^3\setminus\{0\}}
  \frac{\pi}{m|\ell|}
  \frac{e^{-2\pi m|\ell|z}+e^{-2\pi m|\ell|(1-z)}}
       {1-e^{-2\pi m|\ell|}},\\
 -V_m'(z)&=4\pi^2(1/2-z)\\
 &\quad+2\pi^2\sum_{\ell\ne0}
  \frac{e^{-2\pi m|\ell|z}-e^{-2\pi m|\ell|(1-z)}}
       {1-e^{-2\pi m|\ell|}}.
 \end{split}
 \tag{9.2}
\]
The zero transverse mode gives the polynomial. For a nonzero
transverse mode, periodize \(\pi b^{-1}e^{-2\pi b|z|}\),
\(b=m|\ell|\); direct one-dimensional integration gives Fourier
coefficients \((n^2+b^2)^{-1}\). This proves (9.2) without an
external summation formula. The series converge absolutely away
from \(z=0,1\). To justify the transverse restriction directly, start
with (2.1) and perform the finite transverse grid average. Its heat
factor is
\(p_t^{(1)}(z)\sum_{\ell\in\mathbb Z^3}
e^{-4\pi^2tm^2|\ell|^2}-1\).
Separate the zero transverse mode; all remaining heat integrals
are nonnegative, so Tonelli justifies their summation. The resulting
series is finite at every \(0<z<1\). Thus no distribution is
restricted to a singular submanifold without justification.

For \(y_j=j/m+(a/m)\sin(2\pi j/m)\), the exact source becomes
\[
 P_N[J_h](Y_m)=\frac1{m^2}\sum_{j<k}[-V_m'(y_j-y_k)]
       [h'(y_j)-h'(y_k)]+\frac{4\pi^2}{m}\sum_jh(y_j),
 \tag{9.3}
\]
with differences taken modulo one. Same-layer terms vanish because
their gradients of \(h\) agree. The energy increment is
\[
 \frac{H_N(Y_m)-H_N(\Lambda_m)}{m^2}
       =\sum_{j<k}[V_m(y_j-y_k)-V_m((j-k)/m)].
 \tag{9.4}
\]
These are reductions of the singular object independent of the
double-grid Taylor proof.

For \(\min(mz,m(1-z))\ge1/2\), omitting the transverse cube
\(|\ell|_\infty\le L\) gives force error at most
\[
 \frac{4\pi^2}{1-e^{-2\pi m}}
              \sum_{j>L}(24j^2+2)e^{-\pi j}.
 \tag{9.5}
\]
The coefficient is the exact max-norm shell count in dimension
three. The diagnostic reports this truncation bound. Floating
roundoff is not interval certified.

The first diagnostic run passed 230 exact assertions, but a numerical
error threshold of 0.002 at the largest first-run size \(m=96\)
failed: the observed error was approximately 0.00324045.
That run and an explicitly nonvalidating inspection run are retained.
The final revision extends the size list to \(m=192\), retaining the
same threshold, and uses explicit error checks that cannot be
disabled by Python optimization. The final results and precise
history are in the attached diagnostic records. This finite-size
failure is not a mathematical counterexample or a changed coefficient.
The final run passed all 230 exact assertions and detected all eight
mutations. At the numerical probe value \(a=0.05\) and \(m=192\),
the scaled source at zero shift was approximately -1.94899249,
against the limit prediction -1.94818182; the error was 0.00081067,
below the retained 0.002 tolerance. The computed energy divided by
\(m^2\) was approximately -2.74783834. The analytic force-truncation
bound for the scaled source was \(1.44\times10^{-7}\).
This probe value is not claimed to instantiate the uncomputed
uniform constant \(C_E\) in (4.5); the theorem chooses \(a\) by
that analytic bound. The diagnostic does not certify a limiting
statement, arbitrary large grids, or floating-point roundoff.

The local adversarial review checked:

| Proposed failure | Resolution |
|---|---|
| The Robin constant could be positive | Strict analytic upper bound (3.2) |
| Continuum energy could overwhelm the discrete floor | Exact first derivative zero and fixed \(Ca^2m^2\) bound |
| An \(O(m^{-2})\) quadrature error could change the coefficient | Zeroth and first derivatives vanish exactly; only convergence of the second is needed |
| Taylor differentiation could increase the singularity | Relative-displacement and smooth-difference estimate (5.2) through order three |
| A centering change could create the limit | Original contraction retained, with an explicit detecting mutation |
| Only an atomic law was produced | Bounded smooth density (6.2) |
| Smoothing could lose a support property or the limit | Pointwise bounds (6.3)–(6.5), (7.1) on the closed support |
| Haar marginals might be merely asymptotic | Exact common-shift integration |
| A signed expectation might replace an absolute one | Signed mean zero is distinguished from (7.2) |
| The actual iid flow might be refuted | No dynamic or preparation bridge is asserted |

This is a local self-check of the reconstruction, not an isolated
hostile review of it. A separate hostile gate remains necessary.

## 10. Per-conjunction dispositions and bounded handoff

| Required clause | Disposition |
|---|---|
| Fixed \(a,c>0\), one \(m_0\), every integer \(m\ge m_0\) | Proved: (4.5), \(c=1/8\), fixed enlargement of \(m_0\) |
| \(N=m^4\) | Exact throughout |
| Probability density | (6.2) and integration |
| Bounded and smooth for every fixed \(N\) | Derivatives and bound following (6.2); no uniform bound asserted |
| Exchangeability | Exact permutation average |
| Common-translation invariance | Exact Haar shift |
| Every one-body marginal exactly Haar | Direct marginal integration |
| Separation on the complete support | (6.3) |
| Pointwise energy sign on the complete support | (6.5) |
| Original deleted source and centering | (1.1), (2.5)–(2.6), (5.1), (7.1) |
| Singular/background/self terms and limiting order | §§2, 3, 5, 8 |
| Exact limit \(16\pi^3a^2>0\) | (7.2) |
| Exact negation | Refuted by this complete witness sequence |
| Actual iid-flow endpoint | Unchanged; no theorem or counterexample supplied |

The sealed handoff contains this complete report, eight exact inputs,
source/exposure records, diagnostic code and results, input/output
and archive manifests, and verification of all safe archive members
and bytes without extraction. Finite computations support the
analysis; they do not certify it.

No canonical file or ledger was edited; no commit, push, installation,
child agent, outside source, or unprovided link was used. The branch
and isolated worktree were created exactly as authorized.
The next step is root comparison with the withheld construction and
the separate hostile gate. This report makes no canonical promotion.
