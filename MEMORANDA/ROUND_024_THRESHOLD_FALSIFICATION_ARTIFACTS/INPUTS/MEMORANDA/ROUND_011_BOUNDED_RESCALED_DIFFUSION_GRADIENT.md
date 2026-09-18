# Round 011 — uniform weighted gradients at bounded rescaled diffusivity

TASK063. Issued 2026-09-18 UTC. **PROVED_CANDIDATE / SELF_CHECKED.** This is an ordinary proof construction from an explicitly disclosed, unproved root seed. It is neither a blind reconstruction nor independent certification. Fresh review is still required.

The assigned worktree is /Users/matthewrosenzweig/.codex/worktrees/hocf-r011-rescaled-gradient, branch codex/hocf-r011-rescaled-gradient, based on published R8 b2510ed08ecc26387d9fc14daaf174d3c35f5638. The twenty files in the assigned input manifest were copied and SHA-256 verified. Only those inputs were used. No R9/R10 proof or audit, current canonical ledger/history, memory, prior checker, external source, child agent, dependency installation, canonical edit, commit, or push was used. The specific task restriction supersedes the standing requests to read other repository orientation documents and to edit canonical ledgers.

The primary bound and a precisely uniform convergence extension are proved below. The decisive change is to estimate the source directly with its natural value and gradient weights. The proof does not use the older source-occupation estimate whose coefficient is proportional to N. Every high-moment constant used for common starts or expectation differentiation is rebuilt in the bounded-rescaled-diffusivity range.

## 1. Assertion, negation, and source preflight

Fix an integer \(d\ge3\), \(0<s\le d-2\), finite \(T\ge0\), \(L\ge0\), and a real smooth periodic terminal test \(h\). Haar measure on \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) has mass one. Set

\[
 p=s+2,\qquad q=s+1,\qquad
 \chi_{N,\nu}=\nu N^{2/p},\qquad
 N\ge2,\quad 0\le\nu\le L N^{-2/p}.
 \tag{1.1}
\]

The frozen potential and force are

\[
 \widehat g(0)=0,\quad
 \widehat g(k)=c_{d,s}|k|^{s-d},\quad
 c_{d,s}=\pi^{s-d/2}
 \frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\quad K=-\nabla g.
 \tag{1.2}
\]

There is no external drift. The actual reference density is one, so the mean-field velocity is zero. The actual backward test is

\[
 f_t^\nu(x)=\widehat h(0)+
 \sum_{k\ne0}\widehat h(k)
 e^{-(T-t)[\,4\pi^2\nu|k|^2+
                 4\pi^2c_{d,s}|k|^{s+2-d}\,]}
 e^{2\pi i k\cdot x}.
 \tag{1.3}
\]

Let \(E=\{(x,y):x\ne y\}\), and write \(\nabla_{\rm pair}\) for the Euclidean full gradient in the two slots. The auxiliary base generator, source, and full response are

\[
 G_{N,\nu}=\nu(\Delta_x+\Delta_y)
       +N^{-1}K(x-y)\cdot(\nabla_x-\nabla_y),\qquad
 J_t^\nu=K(x-y)\cdot(\nabla f_t^\nu(x)-\nabla f_t^\nu(y)),
 \tag{1.4}
\]

\[
 RF=R_xF+R_yF,\quad
 R_xF(x,y)=-\int F(x+w,y)D(dw),\quad
 R_yF(x,y)=-\int F(x,y+w)D(dw),\quad D=\operatorname{div}K.
 \tag{1.5}
\]

The target \(\Phi^{N,\nu}\) is the *existing full symmetric terminal-zero bounded Borel inverse*, with both responses, equivalently

\[
 \Phi_t^{N,\nu}=U_t^{N,\nu}
       +\int_t^T S_{a-t}^{N,\nu}R\Phi_a^{N,\nu}\,da,\qquad
 U_t^{N,\nu}=\int_t^T S_{a-t}^{N,\nu}J_a^\nu\,da.
 \tag{1.6}
\]

Here \(S^{N,\nu}\) is the noncolliding auxiliary pair Markov evolution, not an interacting N-body law.

For any fixed admissible smooth positive weights equal to \(r^{-s}\) and \(r^{-q}\) near the pair diagonal, the primary assertion is

\[
 \sup_{\substack{N\ge2\\0\le\nu N^{2/p}\le L}}
 \sup_{0\le t\le T}\left[
   \sup_E\frac{|\Phi_t^{N,\nu}|}{w_s(x-y)}
   +\sup_E\frac{|\nabla_{\rm pair}\Phi_t^{N,\nu}|}{w_q(x-y)}
 \right]<\infty.
 \tag{1.7}
\]

The gradients must be actual continuous off-diagonal derivatives of that same inverse and its global weak first derivatives. They are jointly continuous in time and pair space off the diagonal. In particular each inverse is a global Haar \(W^{1,1}\) representative, with a uniform norm. The contracted gradient

\[
 A_t^{N,\nu}(x)=\int\nabla_x\Phi_t^{N,\nu}(x,y)\,dy
 \tag{1.8}
\]

must be a continuous function with a uniform supremum bound. The exact negation is fixed admitted data and a bounded-\(\chi\) sequence for which the normalized norm is unbounded or one of these derivative, representative, or contraction assertions fails.

The separately proved convergence assertion is

\[
 \lim_{N\to\infty}\ \sup_{0\le\nu\le L N^{-2/p}}\quad
 \sup_{0\le t\le T}
 \|\Phi_t^{N,\nu}-\Phi_t^0\|_{C^1(H)}=0
 \quad\hbox{for every compact }H\Subset E,
 \tag{1.9}
\]

\[
 \lim_{N\to\infty}\ \sup_{0\le\nu\le L N^{-2/p}}\quad
 \sup_{0\le t\le T}
 \|\Phi_t^{N,\nu}-\Phi_t^0\|_{W^{1,1}(\mathbb T^{2d})}=0,
 \tag{1.10}
\]

where \(C^1(H)\) means the supremum of values and full spatial first derivatives on H, and

\[
 \Phi_t^0=\int_0^{T-t} e^{rR}J_{t+r}^0\,dr,\qquad
 J_t^0=K(x-y)\cdot(\nabla f_t^0(x)-\nabla f_t^0(y)).
 \tag{1.11}
\]

The exponential in (1.11) is the ordinary norm-convergent series of the bounded response on the weighted space specified below. The limiting kernel need not be bounded at the diagonal. No value or trace there is asserted.

The imported premises are limited and explicit.

* R1, equations (3.1)–(3.3), fixes the two response signs, their coefficients one, and the internal coefficient \(1/N\).
* The complete R4 response memorandum, Sections 2–4, supplies the coefficient-one local expansion, integrability of K, and the exact finite signed measure D. The source/interface addendum explicitly points to this complete proof rather than the short theorem card.
* The complete R5 base memorandum, Sections 4–6, constructs the measurable, pathwise unique, per-start noncolliding auxiliary process and its Markov evolution, and proves a bounded absolute source potential for each fixed N, uniformly over bounded diffusivity. Its cutoff Picard construction and stopped \(r^{-(d-2)}\) barrier also cover zero noise.
* The complete R5 conditional inverse and homogeneous interface memoranda supply the pointwise full inverse (1.6), its boundedness for fixed N, and the explicit test (1.3). The symmetry clarification means commutation with exchange of slots, not Haar self-adjointness.

For clarity, the normalization preflight can be checked directly from those proofs. Their positive heat representation has coefficient
\(4^{(d-s)/2}\pi^{d/2}/\Gamma(s/2)\); substitution in the Euclidean heat integral gives exactly \(|z|^{-s}\), and the lattice remainder is smooth and even near zero. Thus

\[
 g(z)=|z|^{-s}+h_g(z),\quad h_g\in C^\infty,\quad h_g(-z)=h_g(z),
 \quad K(z)=s z|z|^{-s-2}+k(z),\quad k=-\nabla h_g,\quad k(0)=0.
 \tag{1.12}
\]

The gamma recurrence and the punctured-sphere flux give

\[
 D=s(d-2-s)g_{s+2}(z)\,dz\quad(s<d-2),\qquad
 D=c_d(\delta_0-dz)\quad(s=d-2),\quad
 c_d=(d-2)|\mathbb S^{d-1}|.
 \tag{1.13}
\]

Indeed \(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\), while
\(4\pi^2c_{d,d-2}=c_d\). At Coulomb the atom has positive mass \(c_d\) and the constant compensation has mass \(-c_d\). The one-body response multiplier is negative, \(-4\pi^2c_{d,s}|k|^{s+2-d}\), agreeing with (1.3).

The R7/R8 constructor arguments are permitted comparison inputs but none of their unspecified fixed-N moment constants or differentiated-semigroup conclusions is imported as an N-uniform lemma. THM026 and the particle-domain assertions of THM028 are not needed. The submitted cards' historical status labels are not treated as a current audit ledger. No literature claim or unverified external reference enters the proof.

## 2. The uniform weighted flow-moment inequality

Choose \(R_0=1/16\), a fixed smooth radial cutoff \(0\le\zeta\le1\), equal to one for \(r\le R_0\) and zero for \(r\ge2R_0\). All chart-supported expressions below are extended before use on the torus. Put

\[
 w_1(z)=\exp\{\zeta(z)\log(1/|z|)\},\qquad
 w_\alpha=w_1^\alpha\quad(\alpha>0).
 \tag{2.1}
\]

These weights are at least one, equal \(r^{-\alpha}\) in the inner ball, and satisfy \(w_\alpha^b=w_{b\alpha}\). Any weights in the assertion are comparable to these with fixed constants independent of N and \(\nu\).

In (1.12), define finite constants

\[
 H=\sup_{B_{2R_0}}\|Dk\|,\quad
 M=\max\{H,\sup_{\operatorname{dist}(z,0)\ge R_0}\|DK(z)\|\},\quad
 K_0=\sup_{\operatorname{dist}(z,0)\ge R_0}|K(z)|.
 \tag{2.2}
\]

Write \(F_N(x,y)=N^{-1}(K(x-y),-K(x-y))\). Its Jacobian is
\[
 DF_N=N^{-1}
 \begin{pmatrix}DK&-DK\\-DK&DK\end{pmatrix}.
 \tag{2.3}
\]
For the principal Riesz part, the center eigenvalues are zero, the transverse relative eigenvalues are \(2sN^{-1}r^{-p}\), and the radial relative eigenvalue is \(-2s(s+1)N^{-1}r^{-p}\). The largest symmetric eigenvalue is the transverse one, not the absolute matrix norm. Consequently

\[
 \lambda_{\max}(\operatorname{Sym}DF_N)
 \le\ell_N(z):=\frac{2s}{N}\zeta(z)r^{-p}+\frac{2M}{N}.
 \tag{2.4}
\]

For any \(m\ge0\) and \(\alpha>m\), direct differentiation in the relative variable gives, on the inner ball,

\[
 \frac{(G_{N,\nu}+m\ell_N)w_\alpha}{w_\alpha}
 \le-\frac{B_{\alpha,m}}{N}r^{-p}
       +A_\alpha\nu r^{-2}+\frac{2\alpha H+2mM}{N},
 \tag{2.5}
\]

\[
 A_\alpha=2\alpha(\alpha+2-d)_+,\qquad
 B_{\alpha,m}=2s(\alpha-m)>0.
 \tag{2.6}
\]

Before taking the positive part, the diffusion coefficient is exactly
\(2\nu\alpha(\alpha+2-d)\). The two particle Laplacians therefore give \(2\nu\) in the relative coordinate. The smooth remainder contributes
\(-2\alpha N^{-1}r^{-2}k(z)\cdot z\), which is at most \(2\alpha H/N\).

For \(a\ge0,b>0\), differentiation of \(av^2-(b/2)v^{s+2}\) on \(v\ge0\) gives its exact supremum

\[
 \mathcal M_s(a,b)=
 \begin{cases}
 0,&a=0,\\
 \displaystyle\frac{s}{p}a
       \left(\frac{4a}{pb}\right)^{2/s},&a>0.
 \end{cases}
 \tag{2.7}
\]

The maximizing positive point satisfies \(v^s=4a/(pb)\); the derivative changes from positive to negative there. Applying this with \(a=A_\alpha\nu\), \(b=B_{\alpha,m}/N\) gives exactly

\[
 \mathcal M_s(A_\alpha\nu,B_{\alpha,m}/N)
 =Z_{\alpha,m}N^{2/s}\nu^{p/s}
 =Z_{\alpha,m}\chi_{N,\nu}^{p/s}
 \le Z_{\alpha,m}L^{p/s},
 \tag{2.8}
\]

where \(Z_{\alpha,m}=0\) when \(A_\alpha=0\), and otherwise
\[
 Z_{\alpha,m}=\frac{s}{p}A_\alpha
       \left(\frac{4A_\alpha}{pB_{\alpha,m}}\right)^{2/s}.
 \tag{2.9}
\]

This equality, including its N exponent, is the uniformity mechanism. It applies at arbitrarily high fixed moment orders as well as at the first moment.

To include every cutoff term, define
\[
 a_{\alpha,1}=\sup_{r\ge R_0}\frac{|\nabla_z w_\alpha|}{w_\alpha},
 \qquad
 a_{\alpha,2}=\sup_{r\ge R_0}\frac{|\Delta_z w_\alpha|}{w_\alpha}.
 \tag{2.10}
\]
A sufficient constant, independent of the selected N and \(\nu\), is
\[
 C_{\alpha,m}(L)=\max\left\{
 \alpha H+mM+Z_{\alpha,m}L^{p/s},\
 2L a_{\alpha,2}+K_0a_{\alpha,1}
       +m(sR_0^{-p}+M),\
 0\right\}.
 \tag{2.11}
\]
Here \(2/N\le1\), \(\nu\le L\), and
\(G w_\alpha=2\nu\Delta_z w_\alpha+(2/N)K\cdot\nabla_z w_\alpha\)
bound the annulus. Combining (2.5)–(2.11) proves globally
\[
 (G_{N,\nu}+m\ell_N)w_\alpha
 \le C_{\alpha,m}(L)w_\alpha
 -\frac{B_{\alpha,m}}{2N}
       {\bf1}_{r\le R_0}r^{-p}w_\alpha.
 \tag{2.12}
\]

Let \(Z_a\) be the supplied base pair flow from a fixed start \(z\in E\), and write \(I_a=\int_0^a\ell_N(Z_b)\,db\). On a compact collision stop, ordinary Itô calculus applied to \(e^{mI_a-C_{\alpha,m}a}w_\alpha(Z_a)\) gives a nonnegative local supermartingale, retaining the nonnegative occupation term from (2.12). Its stopped stochastic integral has bounded coefficients. Per-start noncollision and conditional Fatou give a nonnegative supermartingale after removing the stops. In particular, for \(0\le a\le T\),
\[
 \mathbb E_z[e^{mI_a}w_\alpha(Z_a)]
 \le e^{C_{\alpha,m}(L)a}w_\alpha(z).
 \tag{2.13}
\]
No uniform integrability of the stopped weights is assumed, and no boundary value is assigned at collision.

Stopping the nonnegative supermartingale at its first crossing of a level u gives the maximal tail bound \(\min(1,w_\alpha(z)/u)\). Apply this to parameters \(2m,2\alpha\), and integrate its square-root tail. The multiplicative weight choice in (2.1) yields
\[
 \mathbb E_z\sup_{a\le T}e^{mI_a}w_\alpha(Z_a)
 \le 2e^{C_{2\alpha,2m}(L)T/2}w_\alpha(z).
 \tag{2.14}
\]
For each fixed \(b>0\), applying (2.14) to \(bm,b\alpha\) also bounds the b-th moment of this supremum. Every constant remains uniform in (1.1). The occupation coefficient \(2N/B_{\alpha,m}\) is deliberately not used for the new source estimate.

## 3. Common local starts and legitimate expectation derivatives

The maximal local additive-noise flow can be constructed for every continuous driving signal by the R5 cutoff Picard argument. Subtraction of the noise reduces it to an ordinary integral equation with smooth coefficients on each compact subset of E. Along a trajectory existing through T, its initial-state derivative \(A_a\) satisfies
\[
 \dot A_a=DF_N(Z_a)A_a,\qquad A_0=I,\qquad
 \|A_a\|\le e^{I_a},
 \tag{3.1}
\]
by (2.4). This is initially a pathwise local assertion, insufficient by itself for expectation differentiation.

For a fixed driving signal, let V be the supremum of \(w_1\) along the maximal trajectory through T, with value infinity if its lifetime is at most T. A finite lifetime can only end at collision. For an integer j, let \(V_j=\min(V,j)\). This is locally Lipschitz as a function of the initial pair state. If \(V>j\), a finite time before any lifetime already has weight greater than j; continuous dependence to that time makes \(V_j=j\) nearby. If \(V\le j\), the reference path stays in a compact collision-excluded set through T, and nearby paths are furnished by a common smooth cutoff flow; their finite-time supremum is locally Lipschitz. These alternatives include \(V=j\).

There is a finite cutoff constant
\[
 C_w=\sup_E |\nabla_{\rm pair}w_1|/w_2<\infty.
\]
At almost every initial state at which the derivative is defined, on its per-start probability-one noncollision event,
\[
 |\nabla V_j|\le C_w\sup_{a\le T}e^{I_a}w_2(Z_a).
 \tag{3.2}
\]
The corresponding bound also controls \(V_j\) because \(w_1\le w_2\) and \(\ell_N\ge0\). Hence, for every finite \(Q>2d\), (2.14) gives
\[
 \mathbb E\bigl[|V_j(z)|^Q+|\nabla V_j(z)|^Q\bigr]
 \le 2(1+C_w^Q)e^{C_{4Q,2Q}(L)T/2}w_{2Q}(z),
 \tag{3.3}
\]
uniformly in j, N, and \(\nu\). Fubini is applicable to the measurable cutoff construction and its locally Lipschitz initial-state functions; for each fixed start the exceptional driving signals have probability zero.

Here is the spatial estimate used to remove that exceptional-start issue. In dimension \(n=2d\), take concentric coordinate balls \(H\Subset O\Subset E\), with a fixed positive radius b available for balls centered in H. Averaging the segment fundamental theorem over \(B_b(x)\) gives
\[
 |v(x)|\le |B_b|^{-1/Q}\|v\|_{L^Q(O)}
 +|\mathbb S^{n-1}|^{-1}
 \left(\int_{B_b}|u|^{(1-n)Q'}du\right)^{1/Q'}
 \|\nabla v\|_{L^Q(O)},\quad Q'=\frac{Q}{Q-1}.
 \tag{3.4}
\]
The radial integral is finite precisely when \(Q>n\); explicitly it equals
\(|\mathbb S^{n-1}|b^{n-(n-1)Q'}/[n-(n-1)Q']\).
This proves the needed local supremum estimate directly.

Integrate (3.3) over O and use (3.4). The expected Q-th power of \(\sup_H V_j\) is bounded uniformly in j. Since \(V_j\) increases to V, monotone convergence gives \(\sup_H V<\infty\) almost surely. A bad start in H would have \(V_j=j\) for all j, a contradiction. A countable exhaustion by such balls proves that, for each fixed N and \(\nu\), a single full-probability event supports the flow for every off-diagonal initial state through T, locally C1 in the initial state, with uniform positive separation on each compact set of starts. This assertion uses the newly proved uniform high moments, not a presumed globally complete stochastic flow. No common exceptional set over uncountably many parameter choices is asserted or needed.

We now justify the interchange actually used below. Let \(H(z,\omega)\) be pathwise C1 on a deterministic compact initial ball on that event. Suppose its derivatives have a moment \(b>1\) bounded uniformly over deterministic starts in a slightly larger ball. The segment fundamental theorem and Jensen bound the b-th moment of every short difference quotient by the same bound. Therefore these quotients are uniformly integrable: their L1 tail above K is at most a constant times \(K^{1-b}\). Almost-sure convergence to the path derivative then implies L1 convergence, so
\[
 \nabla\mathbb EH=\mathbb E\nabla H.
 \tag{3.5}
\]
For varying starts or times, pathwise continuity of the derivative and the same moment bound imply continuity of its expectation. This supplies actual continuous derivatives, not only distributional derivatives.

## 4. Uniform propagation at the source weights

Let X consist of local C1 functions on E with
\[
 \|F\|_X=|F|_s+|\nabla_{\rm pair}F|_q,\qquad
 |v|_a=\sup_E |v|/w_a.
 \tag{4.1}
\]
No global boundedness is included in this space. Its elements and derivatives are Borel. Local uniform closedness of the C1 class makes the weighted norm complete.

For \(b>1\), the value of \(F(Z_a)\) has a b-th moment bounded by (2.13) with \((\alpha,m)=(bs,0)\), since \(bs>0\). The pathwise derivative \(A_a^T\nabla F(Z_a)\) has b-th moment at most
\[
 |\nabla F|_q^b\,e^{C_{bq,b}(L)a}w_{bq}(z),
 \tag{4.2}
\]
because \(bq>b\). These bounds are uniform over compact deterministic starts and the entire parameter class. Section 3 therefore proves
\[
 \nabla S_a^{N,\nu}F
 =\mathbb E[A_a^T\nabla F(Z_a)].
 \tag{4.3}
\]
For \(F\) not bounded globally, its expectation is still absolutely integrable by the value moment just proved. Applying (2.13) at the first moments gives
\[
 |S_a^{N,\nu}F|_s\le e^{C_{s,0}(L)a}|F|_s,\qquad
 |\nabla S_a^{N,\nu}F|_q
 \le e^{C_{q,1}(L)a}|\nabla F|_q.
 \tag{4.4}
\]
With
\[
 C_X=\max\{C_{s,0}(L),C_{q,1}(L)\},
 \qquad \|S_a^{N,\nu}F\|_X\le e^{C_Xa}\|F\|_X,
 \tag{4.5}
\]
this is the uniform differentiated-semigroup estimate needed here.

Every fixed spatial derivative of \(f^\nu\) is uniformly bounded for \(\nu\ge0\): the differentiated Fourier series is dominated by the corresponding rapidly summable coefficients of h, since all exponential factors have modulus at most one. Put \(F_j=\sup_{\nu\ge0,t}\|D^jf_t^\nu\|_\infty\) for \(j=1,2\). These are finite with the displayed Fourier sums as explicit bounds.

On the inner ball, the gradient difference in J supplies a factor r. Direct differentiation gives
\[
 \nabla_xJ=DK^T(\nabla f(x)-\nabla f(y))+D^2f(x)K,\quad
 \nabla_yJ=-DK^T(\nabla f(x)-\nabla f(y))-D^2f(y)K.
 \tag{4.6}
\]
Consequently, sufficient source constants independent of N and \(\nu\) are
\[
 M_0=\max\{F_2(s+HR_0^{s+2}),\,2F_1K_0\},
 \tag{4.7}
\]
\[
 M_1=\max\{\sqrt2F_2[s(s+2)+2HR_0^{s+2}],
             \sqrt2(2F_1K_1+F_2K_0)\},\quad
 K_1=\sup_{r\ge R_0}\|DK\|.
 \tag{4.8}
\]
They give \(|J_t^\nu|\le M_0w_s\), \(|\nabla J_t^\nu|\le M_1w_q\), and \(\|J_t^\nu\|_X\le M_J:=M_0+M_1\).

The source path integral is locally C1 on the common-start event. For example time Jensen and (2.13) give, for \(b>1\) and \(0\le a\le T-t\),
\[
 \mathbb E_z\left|
 \int_0^a A_r^T\nabla J_{t+r}^\nu(Z_r)\,dr\right|^b
 \le a^b M_1^b e^{C_{bq,b}(L)T}w_{bq}(z).
 \tag{4.9}
\]
Its value has the analogous bound with \(bs,0,M_0\). These estimates prove the source-expectation derivative by (3.5), including continuity and its zero terminal value. In particular
\[
 \nabla U_t^{N,\nu}
 =\mathbb E\int_0^{T-t}A_r^T\nabla J_{t+r}^\nu(Z_r)\,dr,\qquad
 \|U_t^{N,\nu}\|_X
 \le M_J(T-t)e^{C_X(T-t)}.
 \tag{4.10}
\]
This direct bound has no factor N. The former approach with a smaller gradient exponent required an occupation gain; the present exponent \(q=s+1\) requires only the terminal moment with \(\alpha=q>1\). No assertion is being made that the former constants were uniform.

## 5. Weak derivatives and both finite-measure responses

An \(F\in X\) and its displayed gradient belong to global Haar L1 because \(s<d\) and \(q=s+1<d\). Delete a tube of radius \(\delta<R_0\) and integrate by parts against a smooth pair test. Its boundary contribution is bounded by a fixed surface constant times
\[
 |F|_s\,\delta^{d-1-s}.
 \tag{5.1}
\]
Here \(d-1-s\ge1\), so it tends to zero. The bulk gradient is dominated by an integrable weight. Thus the continuous off-diagonal derivatives are the global weak derivatives of every diagonal extension. This proves \(F\in W^{1,1}\) and
\[
 \|F\|_{W^{1,1}}\le |F|_sW_s+|\nabla F|_qW_q,\qquad
 W_a=\int_{\mathbb T^d}w_a(z)\,dz
 \le1+\frac{|\mathbb S^{d-1}|(2R_0)^{d-a}}{d-a}
 \quad(0<a<d).
 \tag{5.2}
\]

A weighted convolution estimate must handle two different singular locations. For \(0<a<d\), \(0<b<d\), let \(h_a(w)=\zeta(w)|w|^{-a}\). Set
\[
 H_a=\frac{|\mathbb S^{d-1}|(2R_0)^{d-a}}{d-a},\qquad
 C_{a,b}=R_0^{-b}
 \left[2^bH_a+
 \frac{2^{a+b-d}|\mathbb S^{d-1}|}{d-b}\right].
 \tag{5.3}
\]
For \(z\ne0\), put \(\rho=\min(\operatorname{dist}(z,0),R_0)\). Off the ball \(\operatorname{dist}(w+z,0)<\rho/2\), the weight is at most \(2^b\rho^{-b}\). Inside that ball, \(\operatorname{dist}(w,0)\ge\rho/2\), so \(h_a(w)\le2^a\rho^{-a}\), while the weight integral is exactly
\(|\mathbb S^{d-1}|(\rho/2)^{d-b}/(d-b)\).
Since \(\rho^{d-a}\le1\) and \(\rho^{-b}\le R_0^{-b}w_b(z)\),
\[
 \int h_a(w)w_b(w+z)\,dw\le C_{a,b}w_b(z).
 \tag{5.4}
\]
This proof uses \(a<d\) and \(b<d\) separately; it does not incorrectly require \(a+b<d\) or claim the convolution is bounded.

Below Coulomb write
\[
 D=s(d-2-s)\zeta(w)|w|^{-p}dw+b_D(w)dw,\qquad
 B_D=\|b_D\|_\infty<\infty.
 \tag{5.5}
\]
For either \(b=s\) or \(b=q\), a sufficient weighted response constant is
\[
 D_b=
 \begin{cases}
 s(d-2-s)C_{p,b}+B_DW_b,&s<d-2,\\
 c_d(1+W_b),&s=d-2.
 \end{cases}
 \tag{5.6}
\]
Thus \(\int w_b(z+w)|D|(dw)\le D_bw_b(z)\).
At Coulomb the exact expression is \(c_dw_b(z)+c_dW_b\), retaining the atom and Haar compensation.

Global weak derivatives commute with translations. Fubini against the finite measure \(|D|\) is justified by the global L1 norms from (5.2). Therefore, as weak derivatives,
\[
 \nabla_{\rm pair}R_xF(x,y)
 =-\int\nabla_{\rm pair}F(x+w,y)D(dw),
 \tag{5.7}
\]
and likewise in the y slot. These integrals are absolutely finite off the diagonal by (5.6). They are continuous there: near a given difference \(z_0\ne0\), separate the displacement singularities \(w=0\) and \(w=-z_0\). Near the first, the translated F and gradient are bounded and continuous with a finite-measure majorant. Near the second, change variable \(v=w+x-y\); the D density is smooth and bounded while the F and gradient bounds are respectively \(w_s(v)\) and \(w_q(v)\), both integrable. Their small-ball integrals tend to zero uniformly. The complement is nonsingular. The Coulomb atom is treated separately as multiplication at the actual off-diagonal output point. The identical reasoning proves continuity of the response value.

A continuous function with these continuous weak derivatives is classically C1 locally: mollify on a compact chart and pass the segment fundamental theorem using uniform convergence of the value and derivative mollifications. Hence
\[
 \|RF\|_X\le D_X\|F\|_X,\qquad
 D_X=2\max(D_s,D_q).
 \tag{5.8}
\]
The factor two is precisely the sum of the two slots.

This response is the original integrated-gradient response. For \(x\ne y\), in
\(\int K(z-x)\cdot\nabla_1F(z,y)\,dz\), the singularities at z=x and z=y are distinct. Near x, K is integrable and the gradient is bounded; near y, K is smooth and the gradient is integrable. Integration by parts retains the atom at x, while the boundary at y is \(O(\delta^{d-1-s})\) and vanishes. The compensation in (1.13) gives (1.5), with the minus sign. No evaluation of F on its pair diagonal occurs: the only possible atom of D is at displacement zero, whereas the changed diagonal representative could matter only at the nonzero displacement y-x. Both responses kill constants because D has total mass zero.

The same separated-singularity argument gives a continuity fact needed later. A family uniformly bounded in X that converges locally uniformly in value and first derivatives also has responses converging locally uniformly in those derivatives. This convergence is uniform over additional compact parameters whenever the input convergence is uniform in those parameters. The tails at the moving F singularity are bounded by constants times \(\delta^{d-s}\) and \(\delta^{d-q}\); the remaining compact regions use the input convergence. As global weak operators the responses also obey
\(\|RF\|_{W^{1,1}}\le2\|D\|_{\rm TV}\|F\|_{W^{1,1}}\).

## 6. Factorial construction and identification with the full inverse

All subsequent time integrals are pointwise parameter integrals, with derivatives justified by the local bounds already proved. No strong measurability or strong continuity on an arbitrary weighted Borel supremum space is assumed.

Let \((\mathcal VF)_t=\int_t^T S_{a-t}^{N,\nu}RF_a\,da\). The products of propagation exponents on an ordered time simplex combine into the exponent of the sum of its interval lengths. Thus (4.5), (4.10), and (5.8) give
\[
 \|(\mathcal V^kU)_t\|_X
 \le M_Je^{C_X(T-t)}
       \frac{D_X^k(T-t)^{k+1}}{(k+1)!},\qquad k\ge0.
 \tag{6.1}
\]
The series of values and first derivatives converges in the weighted norms, locally uniformly in space, uniformly in time and in all parameters (1.1). Local C1 closedness and the expectation/response continuity proofs make its sum a jointly continuous local C1 representative. Its terminal value and gradient are zero. The sum solves (1.6) by absolute convergence and dominated time integration.

Identification with the given bounded inverse is separate. Let Y be the pointwise Borel weighted value space \(\|F\|_Y=|F|_s\). We proved
\[
 \|S_a^{N,\nu}\|_{Y\to Y}\le e^{C_{s,0}(L)a},\qquad
 \|R\|_{Y\to Y}\le2D_s.
 \tag{6.2}
\]
For two solutions of (1.6) uniformly bounded in Y over time, their difference equals every Volterra iterate of itself and consequently is bounded by its time-supremum Y norm times
\[
 e^{C_{s,0}(L)T}\frac{(2D_sT)^k}{k!}.
 \tag{6.3}
\]
Letting k increase proves pointwise uniqueness in this larger class. The already supplied bounded Borel inverse is uniformly Y-bounded at each fixed N and \(\nu\), because \(w_s\ge1\). The constructed X-series is also Y-bounded. Both solve precisely the same equation with the same operators and source, so they agree at every off-diagonal point. No boundedness of the new weighted series had to be presumed to make this identification.

A sufficient completely specified constant for (1.7), for the canonical weights, is
\[
 C_*:=T M_J\exp\{(C_X+D_X)T\},
 \tag{6.4}
\]
with zero if \(T=0\), and with all constants defined in (2.2), (2.6), (2.9)–(2.11), (4.7)–(4.8), and (5.2)–(5.6). In particular C depends only on the admitted fixed data and weights, not N or \(\nu\). Pair symmetry is preserved in each term because the base evolution, source, and summed response commute with pair exchange.

Section 5 proves that these same derivatives are the global weak derivatives and
\[
 \sup_{N,\nu,t}\|\Phi_t^{N,\nu}\|_{W^{1,1}}
 \le C_*(W_s+W_q).
 \tag{6.5}
\]
It supplies no diagonal trace and no \(H^1\) assertion: the particular bound \(w_q\) need not be square integrable.

For (1.8),
\[
 \sup_{N,\nu,t,x}|A_t^{N,\nu}(x)|\le C_*W_q.
 \tag{6.6}
\]
Continuity follows by splitting a moving diagonal tube: its integral is at most a fixed constant times \(\delta^{d-q}\), uniformly in x and t; the complement uses local joint continuity. The same applies to \(\int\Phi_t(x,y)dy\). Global weak differentiation and Fubini identify A as its weak x-gradient, and the continuous-weak-derivative argument makes it its actual classical gradient. This proves the contraction assertion for the same representative.

## 7. Uniform local stability of the vanishing base flow

This section proves a new convergence lemma; it does not formally delete the local generator.

Consider a family \(F^{N,\nu}_\theta\), with an additional parameter \(\theta\) in a compact set, uniformly bounded in X. Assume its values and first derivatives converge uniformly on every compact subset of E, uniformly in \(\theta\) and \(0\le\nu\le L N^{-2/p}\), to \(F^0_\theta\). Assume the limit and its spatial first derivatives are jointly continuous in \((\theta,z)\). Then
\[
 \sup_{\substack{0\le a\le T\\\theta,\ 0\le\nu\le L N^{-2/p}}}
 \|S_a^{N,\nu}F_\theta^{N,\nu}-F_\theta^0\|_{C^1(H)}
 \longrightarrow0
 \quad(H\Subset E).
 \tag{7.1}
\]

To prove this, take a compact neighborhood \(H'\Subset E\) of H. On \(H'\), the base drift and its derivative have bounds \(B_{H'}/N\) and \(B'_{H'}/N\). Use consistent local lifts or finitely many coordinate charts. Up to exiting a small fixed neighborhood of a start \(z\in H\), the additive-noise equation gives
\[
 \sup_{a\le T}|Z_a-z|
 \le \sqrt{2\nu}\sup_{a\le T}|W_a|+\frac{B_{H'}T}{N},
 \tag{7.2}
\]
where W is the standard \(2d\)-dimensional Brownian driver. The Jacobian there satisfies
\[
 \sup_{a\le T}\|A_a-I\|\le e^{B'_{H'}T/N}-1.
 \tag{7.3}
\]
Choose an arbitrary small \(\varepsilon>0\) below that neighborhood width. The event on which the right side of (7.2) is at most \(\varepsilon\) prevents the exit for every start in H. Its complement has probability tending to zero uniformly over \(\nu\le L N^{-2/p}\): replace \(\nu\) in the event by \(L N^{-2/p}\), and use that the Brownian path supremum is finite almost surely. This reasoning only needs the common finite-cutoff flow on that event. It does not require a simultaneous singular-flow exceptional set for all noise parameters.

On the event, convergence of \(F^{N,\nu}_\theta\) on \(H'\), uniform continuity of \(F^0_\theta\) and its gradient there, and (7.3) make both chain-rule integrands close to their limiting values, uniformly in \(a,z,\theta\). On its complement, Hölder and the uniform moment estimates bound each error by a constant times the event probability to power \(1-1/b\), for any fixed \(b>1\). The value moment uses \((bs,0)\) and the gradient moment uses \((bq,b)\), exactly as in Section 4; the start weights are bounded uniformly on H. The limiting deterministic values on H are bounded as well. First let N increase and then let \(\varepsilon\) decrease. Equations (4.3), (7.2), and (7.3) give (7.1). Supremums remain outside expectation throughout, so no unproved moment of a spatial supremum of Jacobians is used.

The source family meets the lemma's hypotheses and even converges in X. Indeed,
\[
 \sup_{t\le T}\|f_t^\nu-f_t^0\|_{C^j}\le C_{h,j,T}\nu
 \tag{7.4}
\]
for every fixed j. To see this, use
\(|e^{-\nu4\pi^2|k|^2(T-t)}-1|\le4\pi^2T\nu|k|^2\)
in the rapidly summable differentiated Fourier series; the other exponential has modulus at most one. Applying (4.6) and the source bounds to the difference, with \(j=2\), gives
\[
 \sup_{t\le T}\|J_t^\nu-J_t^0\|_X
 \le C_{h,d,s,T}\nu\longrightarrow0
 \tag{7.5}
\]
uniformly in the bounded-\(\chi\) range. The limit source and derivatives are jointly continuous locally, including both time endpoints.

## 8. Identification and convergence of the limiting full kernel

At limiting local evolution \(S_a^0=I\), the same response estimates construct
\[
 e^{rR}=\sum_{k=0}^\infty\frac{r^kR^k}{k!}
\]
as a bounded operator on X and Y. The pointwise integral (1.11) therefore defines a symmetric local C1 kernel with the same weighted bound, and a global weak \(W^{1,1}\) representative. It solves
\[
 \Phi_t^0=\int_t^T[J_a^0+R\Phi_a^0]\,da.
 \tag{8.1}
\]
Uniqueness among uniformly Y-bounded solutions follows from the same factorial iteration. Because \(J^0\) is continuous in X and R is bounded there, (8.1) also gives the terminal-zero time equation
\(\partial_t\Phi^0+R\Phi^0=-J^0\) as an X-valued identity; this extra statement only concerns the limiting kernel.

For completeness, compare the full finite-N series term by term. Its zeroth term is \(\int_t^T S_{a-t}^{N,\nu}J_a^\nu\,da\), which converges locally in C1, uniformly in t and \(\nu\), to \(\int_t^TJ_a^0\,da\) by (7.1). Assume the k-th terms converge in that topology and are uniformly X-bounded. Section 5 gives local C1 convergence after applying R, uniformly over their time parameter. The limiting term and derivatives are jointly continuous in time and space. Lemma (7.1), with the source time as the extra compact parameter, then gives convergence after applying the base evolution. Integrating over \(a\in[t,T]\) proves convergence of the next term uniformly in t. This induction handles every finite number of response insertions.

The majorant (6.1) is summable uniformly in N, \(\nu\), t, and in weighted values and gradients. It also bounds the corresponding limiting terms. The uniform tails and the finite-term convergence prove (1.9). Expanding \(e^{rR}\), and using absolute time-simplex integration, identifies the sum of the limiting terms exactly with (1.11). The responses are present before and after this limit.

To upgrade to the global integrable derivative norm, fix \(\delta<R_0\). On the compact complement of the diagonal tube of radius \(\delta\), (1.9) gives convergence in value and gradient uniformly in t and \(\nu\). On the tube, the uniform weighted bounds for both kernels give
\[
 \int_{|x-y|<\delta}
 \bigl(|\Phi_t^{N,\nu}-\Phi_t^0|
       +|\nabla(\Phi_t^{N,\nu}-\Phi_t^0)|\bigr)\,dx\,dy
 \le 2C_*|\mathbb S^{d-1}|
 \left(\frac{\delta^{d-s}}{d-s}
       +\frac{\delta^{d-q}}{d-q}\right).
 \tag{8.2}
\]
Both powers are positive; at Coulomb \(d-q=1\). Taking N large and then \(\delta\) small proves (1.10) for the global weak representatives. This is a norm convergence assertion uniform over time and over the full admitted noise interval, not merely convergence along a selected subsequence.

The same moving-tube bound, now with x fixed, proves
\[
 \sup_{\substack{0\le\nu\le LN^{-2/p}\\t,x}}
 |A_t^{N,\nu}(x)-A_t^0(x)|\longrightarrow0,
 \quad A_t^0(x)=\int\nabla_x\Phi_t^0(x,y)\,dy.
 \tag{8.3}
\]
The value contractions converge uniformly as well. No sampling law is involved in (8.2) or (8.3).

## 9. Independent exact diagnostics and adversarial self-review

The accompanying newly written checker does not read any prior checker. Its exact rational calculations are an independent algebraic diagnostic route within this same constructor context. They support the proof; they do not constitute an independent analytic audit.

The checker differentiates radial powers through Cartesian second-order jets and forms the full pair Jacobian before testing radial, transverse, and center vectors. It tests the relative Laplacian factor two, the sign \(\alpha-m>0\), arbitrary high moments, exact rescaling, the optimizing radial profile, the microscopic exponent, finite Fourier response compensation and both slots, and the weak-derivative/tube exponents. Its source-jet calculation also tests the gradient difference that lowers the source singularity by one power. There is no floating-point tolerance or random seed.

A separate solvable diagnostic shows why stronger near-diagonal convergence should not be inferred. In the zero-noise Euclidean radial pair model, take a local quadratic test with scalar Hessian a and omit the responses for this diagnostic only. Then
\[
 r_\tau^p=r_0^p+\frac{2sp}{N}\tau,\qquad
 J(r)=sa r^{-s},\qquad
 U_N(\tau,r_0)=\frac{aN}{4}
 \left[\left(r_0^p+\frac{2sp}{N}\tau\right)^{2/p}-r_0^2\right].
 \tag{9.1}
\]
Direct differentiation gives the correct source derivative at \(\tau=0\) and
\[
 \partial_{r_0}U_N=\frac{aN}{2}r_0
 \left[\left(\frac{r_0^p}{r_0^p+2sp\tau/N}\right)^{s/p}-1\right].
 \tag{9.2}
\]
For \(a\ge0\), the occupation and its radial derivative obey
\(U_Nr_0^s\le sa\tau\) and
\(|\partial_{r_0}U_N|r_0^{s+1}\le s^2a\tau\), by differentiating the actual radial flow under its elementary time integral. At \(r_0=N^{-1/p}\xi\), value and gradient have sizes \(N^{s/p}\) and \(N^{(s+1)/p}\), with bounded weighted ratios. The weighted value profile differs from the identity-flow profile \(sa\tau\) by a fixed nonzero amount for nonzero \(\tau\) and fixed \(\xi\). This is an exact diagnostic of the shrinking region and of the scale in (2.8). It is not offered as a counterexample for the full periodic response inverse, and the proof makes no weighted-supremum convergence claim for that inverse.

The strongest new assertions were tested against the following potential failures.

| Potential failure | Disposition in this construction |
|---|---|
| The old fixed-N exponential was simply relabelled uniform. | Excluded by the exact identity (2.8) and the explicit annular constant (2.11), for every moment order used. |
| A factor N from the source occupation survives. | Excluded by direct source moments (4.9)–(4.10); the occupation gain in (2.12) is not used. |
| An absolute Hessian norm replaces the largest expansion eigenvalue. | Excluded by the full block calculation (2.3)–(2.4), independently checked in Cartesian coordinates. |
| Per-start noncollision is silently used for all points on a segment. | Repaired explicitly by the truncated path-supremum and spatial estimate in Section 3. |
| Pathwise differentiation alone is used to differentiate an expectation. | Excluded by the \(b>1\) derivative moment and uniform-integrability segment proof (3.5), (4.2), and (4.9). |
| The response derivative creates a Coulomb diagonal trace or loses compensation. | Excluded by (1.13), (5.6)–(5.7) and the separated singularities; the atom multiplies the output off-diagonal value. |
| The weighted construction might be a different inverse. | Excluded by pointwise Y-class factorial uniqueness, Section 6. |
| The convergence proof formally drops the singular base drift. | Excluded by the stopped compact comparison, event splitting, and derivative moments in Section 7, followed by response-series induction. |
| Local convergence is incorrectly treated as global convergence. | Excluded by the uniform integrable tube estimate (8.2) and verified weak representatives. |
| The zero-noise endpoint or \(L=0\) is omitted. | Every flow, moment, response, and convergence argument includes it; Brownian terms simply vanish. |

No unsupported line remains in (1.7)–(1.10) within this construction's stated premises. This is a candidate proof, awaiting genuinely separate review.

## 10. Regime calculation, limitations, and exact remaining scope

For finite positive \(\beta_N\), with \(\nu=1/\beta_N\) and
\(\lambda_N=\beta_NN^{s/d-1}\), direct exponent arithmetic gives
\[
 \chi_{N,\nu}
 =\lambda_N^{-1}N^{s/d-1+2/(s+2)}
 =\lambda_N^{-1}
 N^{\,s(s+2-d)/(d(s+2))}.
 \tag{10.1}
\]
The exponent is nonpositive on \(0<s\le d-2\), zero exactly at the Coulomb endpoint, and negative below it. Therefore any sequence with \(\lambda_N\) bounded below by a positive constant eventually belongs to a bounded-\(\chi\) class. In particular every microscopically critical sequence \(\lambda_N\to\lambda\in(0,\infty)\) does. At Coulomb (10.1) is exactly \(\chi=\lambda_N^{-1}\). Zero noise is separately included as a mathematical endpoint and is not the reciprocal of a finite beta.

This is an explicit subrange module of the full bounded-noise target. A fixed positive \(\nu\) makes \(\chi=\nu N^{2/p}\) unbounded and is outside the new uniform assertion. Neither the old energy-floor condition \(\beta_NN^{2s/d-1}\to0\) nor the full microscopically subcritical condition \(\lambda_N\to0\) is replaced by (1.1). In particular the module does not resolve every subcritical sequence.

No N-body evolved-law domination, singular-tail estimate, residual smallness, bracket decay, Gaussian law, corrector truncation, or hierarchy resummation follows from these spatial estimates. A Haar \(W^{1,1}\) bound and convergence do not transfer an iid reference estimate to an evolved law. The gradient majorant alone gives no diagonal trace and need not give \(H^1\). No time-derivative convergence or second-spatial-derivative convergence is claimed. The logarithmic model, inhomogeneous backgrounds, and non-gradient dynamics remain outside this report.

The first unsupported downstream line is the law-dependent use of this spatial control in the actual evolving hierarchy. That requires a separate quantitative law-class estimate; it cannot be supplied by renaming (6.5) or (8.2) an expectation bound.

## 11. Recoverable handoff

The artifact directory contains the new exact checker and its JSON result, README, copied-input manifest, output manifest, verification report, and immutable archive seal. The archive contains only the twenty permitted inputs, their assigned manifest, and this lane's named outputs. The output manifest excludes itself; the archive is sealed separately. No canonical theorem identifier is assigned. Root integration and a new isolated audit are the next actions.

All checks here are self-checks of this proof construction. After issuance the memorandum, checker, result, and sealed archive are immutable; a correction must be a separately named superseding report.
