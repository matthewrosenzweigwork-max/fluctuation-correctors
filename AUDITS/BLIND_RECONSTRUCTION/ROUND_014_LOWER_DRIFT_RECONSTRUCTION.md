# Round 014 lower drift contractions: independent reconstruction

TASK-074. Prepared in the isolated worktree
`/Users/matthewrosenzweig/.codex/worktrees/hocf-r014-lower-blind`, branch
`codex/hocf-r014-lower-blind`, based on the specified published R10 commit
`1df1805ed7cd8f7c295945f99273c8ffdb598e74`.

**Verdict: the complete frozen THM-035 implication is proved below, conditional
on precisely the supplied R12 weighted-gradient and R8 genuine-domain premises
in their issued scopes.** No admitted counterexample to this implication was
found. This report does not independently promote either premise. The proof
gives a pathwise bound stronger than the requested actual-law expectation
bound and an exact reduction of the integrated residual. It gives no estimate
making the cubic residual small.

The current R14 constructor, R13 materials, other current audits, canonical
state/history contents, memory files and prior checker code were not inspected. The
control task and input manifest were read first; all 25 allowed files were
hash-verified before copying and again afterward. Complete exposure and
verification details are in the companion artifact directory. No comparison
preceded sealing. The root alone compares reports and decides promotion.

## 1. Complete reconstructed assertion and its negation

Fix an integer \(d\geq3\), a real exponent \(0<s<d-2\) satisfying
\(3s<2d-2\), a finite horizon \(T\geq0\), finite nonnegative bounds
\(L,\nu_*\), a smooth real terminal test \(h\), the fixed periodic Riesz
kernel and fixed weights. The space is the unit-mass Haar torus
\(\mathbb R^d/\mathbb Z^d\), with characters \(e^{2\pi i k\cdot x}\).
The kernel has zero mean and

\[
 \widehat g(k)=c_{d,s}|k|^{s-d}\quad(k\ne0),\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1}
\]

For every integer \(N\geq2\) and \(0\leq\nu\leq\nu_*\) with
\(\chi=\nu N^{2/(s+2)}\leq L\), use the genuine homogeneous symmetric
terminal-zero full pair inverse \(\Phi=\Phi^{N,\nu,h}\), with both response
slots and the actual Fourier test

\[
 f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)(4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{s+2-d})}
 e^{2\pi i k\cdot x}.
 \tag{2}
\]

Thus \(J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y))\), and off the
diagonal the supplied domain premise identifies the genuine inverse through

\[
 \partial_t\Phi+\nu(\Delta_x+\Delta_y)\Phi+N^{-1}B\Phi+R\Phi=-J,
 \quad \Phi_T=0,\quad R=R_x+R_y,
 \quad B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi.
 \tag{3}
\]

The homogeneous compensated responses are
\(R_xF=-\int F(x+z,y)\,D(dz)\) and
\(R_yF=-\int F(x,y+z)\,D(dz)\), where \(D=\operatorname{div}K\).
This notation retains the full periodic compensation. The inverse is the
bounded Borel inverse from the supplied full-pair construction, with the
classical off-diagonal derivative representative from R8; it is not a new
solution defined only by the estimate sought here.

The actual particles start iid Haar, independently of the Brownian drivers,
and solve the singular dynamics supplied by R6,

\[
 dX_i=N^{-1}\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu}\,dW_i,
 \qquad\eta_t=N^{-1}\sum_i\delta_{X_i(t)},\qquad\rho_t=\eta_t-dx.
 \tag{4}
\]

At positive noise put \(p=s+2\), \(b=\min(1/\nu,1)\) and
\(\sigma=\sqrt{Nb}\). At zero noise take \(b=1\), \(\sigma=\sqrt N\)
directly; no reciprocal is taken. Set

\[
 q_{\rm lo}=\max(1,s/2),\qquad
 q_{\rm hi}=\min(d/2,d-s-1,s+1),\qquad
 q=(q_{\rm lo}+q_{\rm hi})/2,\qquad
 \kappa_q=\frac{2q-s}{2p}.
 \tag{5}
\]

The assertions to prove are:

1. This interval is nonempty, its midpoint is admissible for the supplied
   R12 gradient estimate, and \(\kappa_q>0\).
2. With the actual R8 representatives
   \(g_t(x)=\int B\Phi_t(x,y)\,dy\) and
   \(c_t=\int B\Phi_t\,dxdy\), the exact lower drift
   \(\ell_t=N^{-1}\rho_t[g_t]+(2N)^{-1}c_t\) satisfies
   \[
   \sigma\,\mathbb E\int_0^T|\ell_t|\,dt
       \leq C\sqrt b\,N^{-\kappa_q},
   \tag{6}
   \]
   for one constant depending only on the fixed displayed data, kernel and
   weights, independently of \(N\) and the selected \(\nu\).
   The exact two coefficients and both contractions are retained.
3. The exponent range contains every supplied R12 microscopic critical decay
   range \(0<s<d-2\), \(s(s+2)<2d\). Along every such critical sequence,
   the full cubic-plus-lower time-integrated residual tends to zero in scaled
   \(L^1\) if and only if the integrated \(U_3[C\Phi]\) alone does.
   This is a reduction, not cubic smallness.

The exact negation is the existence of admitted fixed data and a family of
admitted \((N,\nu)\) for which the ratio of the left side of (6) to
\(\sqrt bN^{-\kappa_q}\) is unbounded, or a failure of one of the admissibility,
range, genuine-contraction/coefficient, or stated residual-equivalence
assertions. Because this is a conditional implication, the negation must
satisfy its supplied R8 and R12 premises; an unproved or later falsified
premise is not silently certified by this reconstruction.

No unrestricted bounded-noise sequence, full cubic bound, higher hierarchy,
fluctuation law, logarithmic normalization, general background or new external
source theorem is part of this assertion.

## 2. Source and normalization preflight

Only the 25 files of the assigned manifest are source material. The precise
inputs used in the proof are:

| Input | Supplied scope and use here |
| --- | --- |
| Frozen R1 model and `ROUND_001_ALGEBRA.md`, (1.3), (1.4), (3.4), (3.7) | Ordered distinct-label statistics with denominators \(N^k\), factor \(1/2\) in \(P\), six-term average in \(C\). The algebra is reconstructed in Section 5. |
| `ROUND_004_SINGULAR_RESPONSE.md`, Section 2, (2.1)–(2.4), with THM-021 | Exact Fourier constant, local coefficient one and a smooth local remainder. Only the resulting force bound is needed for (6). |
| THM-023/024/025 and supplied R5 interface/addenda | Identification of the full inverse, both responses, pointwise representatives and the actual homogeneous Fourier test. No finite-particle domain is inferred from these alone. |
| THM-027 and `ROUND_007_WEIGHTED_PAIR_GRADIENT.md`, (2.1) | Fixed weights \(w_a=w_1^a\geq1\), equal to \(|z|^{-a}\) near zero; a fixed-N bound is not treated as uniform. |
| THM-033 and `ROUND_012_SUBCOULOMB_ACTUAL_NOISE.md`, (1.1), Sections 2–4 | **Conditional premise:** the genuine pair gradient is bounded by \(C_qN^{(s+1-q)/p}w_q\), uniformly on bounded \(\chi\), for \(1<q<d/2\), \(q\leq s+1\). The noise/energy part of R12 is not used to prove (6). |
| THM-028 and `ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, Sections 8–11 | **Conditional premise:** genuine derivatives, actual background contractions, full singular particle identity and finite-N absolute drift integrability, including zero noise. No uniform-in-N density conclusion is imported. |
| THM-026 and its R6 memorandum | Actual singular noncolliding particle realization and its fixed-N law class, as used by R8. |
| THM-031 and supplied R10 memorandum | Not needed for the lower-contraction estimate or its range. In particular its energy floor, entropy and actual Fourier concentration claims supply no hidden premise here. |

The input cards' historical status words and the allowed memoranda's references
to earlier audits do not supply a current audit verdict. The task explicitly
permits only the earlier conditional statements in their issued scopes.

For completeness, the normalization needed in the product estimate can be
checked directly. Set \(a=(d-s)/2\) and
\(A=2^{d-s}\pi^{d/2}/\Gamma(s/2)\). The Haar heat kernel \(p_t\) gives

\[
 g_s(z)=A\int_0^\infty t^{a-1}(p_t(z)-1)\,dt,
 \qquad A\Gamma(a)(4\pi^2)^{-a}=c_{d,s}.
 \tag{7}
\]

The Euclidean zero-lattice term integrates to
\(A(4\pi)^{-d/2}2^s\Gamma(s/2)|z|^{-s}=|z|^{-s}\).
For small heat times, nonzero lattice translates and all derivatives decay
exponentially in the inverse heat time on an embedded ball; the constant
subtraction is integrable because \(a>0\). For large heat times, the torus
remainder is exponentially decaying and the subtracted Euclidean term is
integrable as \(t^{-s/2-1}\), with better derivative decay. Thus the local
remainder is smooth and even. In particular, on that ball,

\[
 K(z)=s z|z|^{-s-2}+K_{\rm sm}(z),\qquad
 |K(z)|\leq C_K w_{s+1}(z),
 \tag{8}
\]

and the latter inequality holds globally after increasing the fixed constant
on the compact complement. This is the precise normalization and sign used
below. No Coulomb atom or logarithmic substitution enters the estimate.

Equation (2) has all fixed spatial derivatives uniformly bounded for
\(t\in[0,T]\), \(N\geq2\) and \(\nu\geq0\): the nonzero-mode damping is
positive and each polynomially weighted Fourier series of the fixed smooth
\(h\) is absolutely summable. This checks the actual-test data required by
the supplied gradient premise.

## 3. The weight interval and uniform bound

Each of the three upper endpoints in (5) is strictly greater than 1:
\(d/2>1\), \(d-s-1>1\) because \(s<d-2\), and \(s+1>1\).
Each is also strictly greater than \(s/2\): the first uses \(s<d\), the
second is exactly \(3s<2d-2\), and the third uses \(s>0\).
Consequently \(q_{\rm lo}<q_{\rm hi}\), and its strict midpoint obeys

\[
 1<q<d/2,\qquad s/2<q<d-s-1,\qquad q<s+1.
 \tag{9}
\]

The first and last inequalities place it in the exact R12 gradient range.
Writing \(\alpha=(s+1-q)/p\), that conditional premise gives

\[
 |\nabla_{x,y}\Phi_t(x,y)|\leq C_q N^\alpha w_q(x-y),\qquad x\ne y,
 \tag{10}
\]

uniformly over the admitted \(t,N,\nu\). No constant from a fixed-N R7 or
R8 estimate is substituted for \(C_q\).

Since \(|u-v|\leq\sqrt2(|u|^2+|v|^2)^{1/2}\), (8), (10), and the exact
weight product imply

\[
 |B\Phi_t(x,y)|
 \leq\sqrt2 C_KC_qN^\alpha w_{s+1+q}(x-y).
 \tag{11}
\]

Put \(I=\int_{\mathbb T^d}w_{s+1+q}(z)\,dz\). It is finite: near zero
the radial integral is a constant times
\(\int_0^R r^{d-1-(s+1+q)}\,dr\), whose exponent is greater than \(-1\)
by (9); the complement is bounded. Therefore, with
\(M=\sqrt2 C_KC_q I\),

\[
 \sup_{t,x}\int|B\Phi_t(x,y)|\,dy\leq MN^\alpha,
 \qquad\sup_t\|g_t\|_\infty\leq MN^\alpha,
 \qquad\sup_t|c_t|\leq MN^\alpha.
 \tag{12}
\]

This is where the additional range condition is used. In a wider range,
blindly multiplying a force and a fixed-N gradient can be nonintegrable; the
present exponent is expressly chosen to make the multiplication legitimate.

## 4. Genuine representatives, actual law and zero noise

Equation (11) is an absolute bound on the genuine off-diagonal product. In
relative coordinates the contraction is
\(g_t(x)=\int K(z)\cdot(\nabla_x-\nabla_y)\Phi_t(x,x-z)\,dz\).
For every \(z\ne0\) its integrand is jointly continuous in \((t,x)\) by
the supplied R8 domain premise. The bound (11) is an integrable majorant
independent of \((t,x)\). Dominated convergence proves a continuous
representative of \(g\), including one-sided endpoint continuity in time.
The same argument gives continuity of \(c\), and absolute Fubini gives
\(c_t=\int g_t\,dx\). These are exactly the R8 absolute contractions of
the same derivative representative. No diagonal value, trace, mollified
corrector or modified coefficient is introduced.

For every empirical probability measure \(\eta\), deterministically,

\[
 \ell_t=\frac1N\left(\eta_t[g_t]-\frac12c_t\right),\qquad
 |\ell_t|\leq\frac{3M}{2}N^{\alpha-1}.
 \tag{13}
\]

This rewrites the two exact terms by \(\rho=\eta-dx\) and
\(dx[g_t]=c_t\); it does not discard either term. The bound holds for each
configuration on which the actual observable is defined. In fact its
contraction expression is bounded even for an arbitrary empirical probability
measure because it evaluates only the continuous one-variable \(g\).
For the actual singular process, noncollision and all required finite-N drift
integrability remain the supplied R8/R6 premises.

Multiplying (13) by \(\sigma=\sqrt{Nb}\) and integrating gives the stronger
pathwise assertion

\[
 \sigma\int_0^T|\ell_t|\,dt
 \leq\frac{3MT}{2}\sqrt b\,N^{\alpha-1/2}
 =\frac{3MT}{2}\sqrt b\,N^{-\kappa_q},
 \quad\alpha-\tfrac12=\frac{s-2q}{2(s+2)}=-\kappa_q<0.
 \tag{14}
\]

Expectation proves (6). It uses no evolved product law, exchangeability,
one-body marginal assertion, energy floor, entropy, concentration estimate or
fixed-N density domination. In particular an exponential density cost is
never hidden in \(M\). The actual iid-Haar law stipulated by the theorem is
one allowed law for this deterministic estimate.

The constant depends only on \(d,s,q,T,h,L,\nu_*\), the fixed kernel and
weight. Since \(q\) is fixed by \((d,s)\), this is the asserted dependence.
It may deteriorate as fixed exponents approach the excluded boundaries; no
uniformity over all \((d,s)\) is claimed. If \(T=0\), both sides vanish.
At \(\nu=0\), (10) is in the supplied closed noise interval, \(b=1\) is
used directly, and (14) remains valid for the deterministic dynamics with
random iid initial data. No noise factor is needed to make the drift small.

## 5. Reconstruction of the exact lower coefficients

This derivation stays off true collision diagonals. Set
\(H(x,y)=\nabla_x\Phi(x,y)\),
\(a(x)=\int H(x,y)\,dy\), \(q_\Phi(x)=\int\Phi(x,y)\,dy\), and
\(r_\Phi=\int\Phi\,dxdy\). Suppress time and write

\[
 P[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
          -\frac1N\sum_iq_\Phi(X_i)+\frac12r_\Phi.
 \tag{15}
\]

On compact collision-excluded stops, differentiation gives
\(\nabla_iP=N^{-2}\sum_{j\ne i}H(X_i,X_j)-N^{-1}a(X_i)\).
The particle-force contribution to its generator is consequently

\[
 Q=\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}
        K(X_i-X_k)\cdot H(X_i,X_j)
    -\frac1{N^2}\sum_{i\ne k}K(X_i-X_k)\cdot a(X_i).
 \tag{16}
\]

The overlap \(k=j\), paired in its two orientations using symmetry of
\(\Phi\) and oddness of \(K\), is
\((2N^3)^{-1}\sum_{i\ne j}B\Phi(X_i,X_j)=(2N)^{-1}D_2[B\Phi]\).
The remaining labels are all distinct and their ordered sum is the ordered
sum of
\(C\Phi=\operatorname{Sym}_3[K(x-z)\cdot H(x,y)]\), where
\(\operatorname{Sym}_3\) is the average over all six permutations.

To reconstruct its backgrounds, put
\(A_a(x,y)=K(x-y)\cdot(a(x)-a(y))\) and
\(v(x)=\int K(z-x)\cdot a(z)\,dz\). Absolute integration of those six
terms gives

\[
 C_1(x,y)=\int C\Phi(x,y,z)\,dz=\frac{A_a(x,y)+R\Phi(x,y)}6,
 \quad C_2(x)=\iint C\Phi(x,y,z)\,dydz=\frac{v(x)}3,
 \quad C_0=0.
 \tag{17}
\]

Indeed, the two terms whose force integrates alone vanish by \(\int K=0\);
the two with derivative integrated in the third slot give \(A_a\); the
remaining two give the two responses. Furthermore
\(\int A_a(x,y)\,dy=v(x)\),
\(\int R\Phi(x,y)\,dy=v(x)\), and \(\int v=0\), yielding the second
and third identities. At the one-background level singularities occur at
the two separated fixed coordinates and are individually integrable; at
the double-background level \(|K(x-z)|\,|H(x,y)|\) has independent relative
variables, with exponents \(s+1<d\) and \(q<d\). The supplied R8 domain
also justifies the original response representatives and the differentiated
backgrounds. No expression \(C\Phi(x,x,z)\) is evaluated.

Use the literal deleted-label formula

\[
 U_3[C\Phi]=\frac1{N^3}\sum_{i,j,k\,\mathrm{distinct}}C\Phi(X_i,X_j,X_k)
 -\frac3{N^2}\sum_{i\ne j}C_1(X_i,X_j)
 +\frac3N\sum_iC_2(X_i)-C_0.
 \tag{18}
\]

Oddness makes the second term of (16) equal to
\(-(2N^2)^{-1}\sum_{i\ne j}A_a(X_i,X_j)\).
Substituting (17) into (18), and using
\((R\Phi)_{dx}=v\), \(\int R\Phi=0\), therefore gives exactly

\[
 Q=U_3[C\Phi]+P[R\Phi]+\frac1{2N}D_2[B\Phi].
 \tag{19}
\]

The independent time-diffusion contribution is
\(P[(\partial_t+\nu\Delta_{x,y})\Phi]\). Distinct particle labels have
zero Brownian cross variation; the Haar-integrated Laplacian of a background
slot is zero by the supplied weak-domain and slice integration-by-parts
premise. Thus there is no additional thermal trace.

Finally, the exact definition (15) with kernel \(B\Phi\) yields

\[
 \frac1{2N}D_2[B\Phi]-\frac1NP[B\Phi]
 =\frac1N\eta[g]-\frac1{2N}c
 =\frac1N\rho[g]+\frac1{2N}c.
 \tag{20}
\]

Combining (3), (19) and (20) recovers the actual R8 identity

\[
 dP_t[\Phi_t]=\{-P_t[J_t]+U_{3,t}[C\Phi_t]+\ell_t\}\,dt+dM_t^2.
 \tag{21}
\]

The collision-stop removal and actual true-martingale passage are the
explicit conditional R8 input, not a new assertion justified only by finite
algebra. This reconstruction verifies the coefficient conversion without
using a singular diagonal-overlap or a full-product trace. It is valid at
\(N=2\): only the first sum in (18) is empty, while its background terms
remain. No denominator \((N)_k\) or alternate centering is substituted.

Neither oddness of \(K\) nor pair symmetry alone permits deletion of the
scalar. In angle coordinates with normalized Haar, take the smooth diagnostic
\(K(x-y)=\sin(x-y)\), \(\Phi(x,y)=\cos(x-y)\). Then
\(B\Phi=-2\sin^2(x-y)\) and \(c=-1\). This is an exact counterexample
to a parity-only cancellation claim, not a counterexample to the genuine
Riesz inverse theorem. An additional cancellation particular to that inverse
is unnecessary for (14) and is not presumed here.

## 6. Critical range and the precise scaled L1 equivalence

Suppose \(0<s<d-2\) and \(s(s+2)<2d\). If \(s\leq2\), then
\(d>s+2\), whence
\(2d>2s+4\geq3s+2\). If \(s\geq2\), then
\(2d>s^2+2s\geq3s+2\), because
\(s^2-s-2=(s-2)(s+1)\geq0\). Thus in all cases
\(3s<2d-2\), exactly the additional hypothesis in (5). The common case
\(s=2\) is covered with a strict first inequality, without an endpoint
extension of R12.

For a positive-noise microscopic critical sequence, put
\(\theta=1-s/d\) and
\(\lambda_N=\beta_NN^{-\theta}\to\lambda\in(0,\infty)\). Then

\[
 \nu_N=\lambda_N^{-1}N^{-\theta},\qquad
 \chi_N=\lambda_N^{-1}N^{2/p-\theta},\qquad
 \frac2p-\theta=\frac{s(p-d)}{dp}<0.
 \tag{22}
\]

Hence \(\nu_N\to0\), \(\chi_N\to0\), and \(b_N=1\) eventually.
Every such sequence is eventually in a family with fixed positive bounds
\(L,\nu_*\). Finitely many earlier indices do not affect any limiting
claim. The exact zero-noise convention is included in (14) but is not
identified with a positive finite critical \(\lambda\).

Define the random integrated quantities, using the genuine R8 identity,

\[
 A_N=\int_0^T U_{3,t}[C\Phi_t]\,dt,\qquad
 D_N=\int_0^T\ell_t\,dt,\qquad R_N=A_N+D_N.
 \tag{23}
\]

All are integrable at every fixed \(N\) by the R8 actual-law premise and
(14). The elementary triangle inequality and its reverse give the exact
comparison

\[
 \left|\|\sigma_NR_N\|_{L^1(\mathbb P_N)}
       -\|\sigma_NA_N\|_{L^1(\mathbb P_N)}\right|
 \leq\sigma_N\mathbb E|D_N|
 \leq\sigma_N\mathbb E\int_0^T|\ell_t|\,dt
 \leq C\sqrt{b_N}N^{-\kappa_q}.
 \tag{24}
\]

The probability space may depend on \(N\); the inequality is within each
space and requires no common coupling. Since \(0<b_N\leq1\) and
\(\kappa_q>0\), its right side tends to zero. Therefore exactly

\[
 \sigma_N\mathbb E|R_N|\longrightarrow0
 \quad\Longleftrightarrow\quad
 \sigma_N\mathbb E|A_N|\longrightarrow0.
 \tag{25}
\]

This holds in particular throughout the supplied R12 critical decay range.
It holds for the bounded-\(\chi\) parameter sequences of this theorem more
generally, but does not assert that either equivalent limit is zero.
For every upper integration endpoint in \([0,T]\), the same error bound
holds. In particular
\(\mathbb E\sup_{u\leq T}|\sigma_N\int_0^u\ell_tdt|\) is bounded by
(14). One must not confuse \(\mathbb E|\int U_3dt|\) with
\(\mathbb E\int|U_3|dt\); neither cubic norm has been shown small here.
If the stronger time-absolute norm is intended, its analogous equivalence
follows separately from \(\big||a+b|-|a|\big|\leq|b|\) and (14).

The old energy-floor condition \(\beta_NN^{2s/d-1}\to0\), full
microscopically subcritical coupling \(\lambda_N\to0\), and positive finite
critical coupling remain different conditions. None is substituted for
another in (14) or (22).

## 7. Independent falsification route and adversarial review

The analytic proof route is the integrable pointwise force-gradient product.
The separate falsification route uses exact Fourier polynomials, literal
particle-label sums and exact Haar integration, followed by rational range
probes. The independently written `lower_blind_exact.py` uses only the Python
standard library and exact Gaussian rational/Fraction arithmetic. It reads
no campaign checker. The checked smooth examples are algebra diagnostics,
not replacements for the singular Riesz inverse.

The final checker passed **208,486 exact assertions**, including 225 smooth
generator cases, 27,339 admitted rational parameter cases and 10,682 critical
parameter cases. Every requested coefficient mutation produced an exact
nonzero witness. A second execution of the final code produced byte-identical
JSON output. The result files preserve all counts and witnesses.

The diagnostic directly differentiates (15) at the particle coordinates,
applies their interacting drift and independent diffusion, and compares it
with the assembled full pair operator, six-permutation cubic and both lower
contractions. Haar integrals are obtained by exact zero-Fourier-mode
selection, never by sampling a grid. Evaluations at quarter-turn coordinates
are exact; repeated coordinates are permitted only in these smooth tests,
while deletion continues to refer to labels. The angle-coordinate mapping
to the unit torus is documented in the checker, so no missing \(2\pi\)
factor is interpreted as a normalization test of the singular kernel.

The tests include constants, relative and common-translation modes, a
one-body symmetric pair kernel and a mixed Fourier polynomial; \(N=2,3,4,5,7\);
zero and positive diffusion; several configurations; nonzero scalar and
nonzero order-one contractions. Mutations omit/double the scalar, reverse
the order-one coefficient, omit the cubic or one response, double the internal-pair term or
insert a falling-factorial correction. Each must produce an exact nonzero
witness. The \(N=2\) tests require an explicit nonzero cubic background
witness even though no three distinct labels exist.

Exact rational range probes separately check the midpoint, the integrability
gap, the decay exponent identity, the critical inclusion and the bounded-chi
exponent. At the excluded boundary \((d,s)=(8,14/3)\), the allowed midpoint
interval collapses, the decay exponent becomes zero and the radial product
has exponent \(-1\), displaying the logarithmic endpoint obstruction to
this proof. This is not a disproof outside the frozen theorem's strict range.
Zero noise is tested without a reciprocal. Finite tests do not certify an
analytic estimate, a singular limit or a universal real-parameter claim;
those are the arguments in Sections 2–6.

The principal adverse possibilities have the following dispositions:

| Attempted failure | Disposition |
| --- | --- |
| Hidden \(N\)-dependent constant from R7/R8 | Avoided: the only uniform gradient input is precisely R12 (1.1); (12)–(14) show every new factor. |
| Nonintegrable force times gradient | Ruled out in the frozen range by \(s+1+q<d\); the excluded boundary probe loses integrability exactly. |
| Wrong actual-law transfer | No transfer is used: (14) is pathwise; R8 is needed only for identification/integrability of the full actual residual. |
| Arbitrary diagonal extension changes the contraction | Ruled out by absolute integration of the genuine off-diagonal representative; no trace is evaluated. |
| Scalar disappears by symmetry | False as a general algebra claim; the exact smooth witness has scalar \(-1\). Both terms remain in this proof. |
| \(N=2\) removes the whole cubic | False; only the all-distinct particle sum disappears, not its backgrounds. |
| Absolute time integral or cubic smallness inferred from a signed mean | Neither is inferred; the lower error is bounded with absolute value before integration, and (24) is the precise norm comparison. |
| Critical range loses a subset | Ruled out by the two-case real-parameter proof and (22); no equality endpoint of R12 is included. |

This is an independent reconstruction of the R14 assertion from the sealed
earlier sources. The diagnostic and adversarial section are self-checks
within this reconstruction context, not an additional isolated hostile audit.

## 8. Disposition and recoverable handoff

Every component of frozen THM-035 has a complete conditional proof: the
weight interval and positivity in Section 3; representative and uniform
actual-law drift estimate in Sections 3–4; exact coefficients in Section 5;
the full critical inclusion and precise scaled \(L^1\) equivalence in
Section 6. No additional mathematical premise is needed for the new
implication beyond the frozen sources explicitly named above.

The unresolved next assertion is the smallness of the genuine integrated
cubic residual. No estimate in this report bounds it by a quantity tending
to zero. The inherited R8 and R12 premises retain their issued conditional
status until the root establishes their independently reviewed status from
authorized evidence. No theorem or canonical ledger is promoted here.

Created files are confined to this assigned reconstruction report and its
companion `ROUND_014_LOWER_BLIND_ARTIFACTS` directory, plus its archive/seal.
The artifact README gives the exact diagnostic commands, immutable input
and output manifests, deterministic rerun result and archive verification.
No canonical source/state file was edited; no commit, push, merge, dependency
installation or child agent was used. All linked handoff files were verified
before sealing. No TeX source was changed or created, and no final-channel
mathematical LaTeX is needed for the bounded handoff.
