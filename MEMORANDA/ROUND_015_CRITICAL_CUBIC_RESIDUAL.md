# Round 015 — critical integrated cubic residual

TASK-075. Issued 2026-09-18 UTC. **PROVED_CANDIDATE / SELF_CHECKED, conditional on the complete permitted earlier modules in Section 2. Fresh reconstruction and hostile audit are required.** This is a construction, not independent certification. No current audit label is used as a premise.

The construction proves the exact integrated assertion in THM-036 throughout its frozen range. The new analytic step is an actual-law estimate for the original quadratic commutator source. A positive low-heat remainder controls close pairs, and a Fourier commutator estimate controls the retained frequencies. The literal R8 identity then gives the integrated cubic estimate, with the initial endpoint, both lower contractions, and the genuine martingale kept explicitly. This proof does not estimate the absolute instantaneous cubic integrand uniformly in N.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r015-cubic`. Branch: `codex/hocf-r015-cubic`. Base: published R10 `1df1805ed7cd8f7c295945f99273c8ffdb598e74`. The 27 manifest inputs were verified before copying and reverified in this worktree. Only this dossier was used. Complete exposure, checker, results, input/output manifests, and archive seal are in `MEMORANDA/ROUND_015_CUBIC_ARTIFACTS/`. Root alone integrates. No canonical edits, commits, pushes, installations, outside searches, prior checker reads, or child agents were used.

## 1. Exact assertion, negation, and quantitative conclusion

Fix an integer \(d\ge4\), \(0<s<2\), finite \(T\ge0\), and smooth real \(h\) on the unit-Haar torus \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\). The frozen Fourier convention is \(e_k(x)=e^{2\pi i k\cdot x}\), with

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
 \tag{1.1}
\]

The actual particles have zero external drift and satisfy

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu_N}\,dW_i,
 \tag{1.2}
\]

from iid Haar initial coordinates, independently of the independent standard Brownian motions. Put

\[
 \theta=1-\frac{s}{d},\quad p=s+2,\quad a=\frac{s}{p},\quad
 \lambda_N=\beta_NN^{-\theta}\longrightarrow\lambda\in(0,\infty),
 \quad\nu_N=\beta_N^{-1},\quad
 b_N=\min(\beta_N,1),\quad\sigma_N=\sqrt{Nb_N}.
 \tag{1.3}
\]

All temperatures are finite and positive. The reference is Haar, \(\rho_t=N^{-1}\sum_i\delta_{X_i(t)}-dx\). The test is the actual backward Fourier solution

\[
 f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)[4\pi^2\nu_N|k|^2+4\pi^2c_{d,s}|k|^{s+2-d}]}e_k(x).
 \tag{1.4}
\]

Let \(\Phi\) be the genuine symmetric terminal-zero full pair inverse for

\[
 J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)),
\]
\[
 \partial_t\Phi+\nu_N\Delta_{x,y}\Phi+N^{-1}B\Phi+R_x\Phi+R_y\Phi=-J,
 \quad B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi.
 \tag{1.5}
\]

Both responses have coefficient one. The statistic is

\[
 P_N[F]=\frac1{2N^2}\sum_{i\ne j}F(X_i,X_j)
 -\frac1N\sum_i\int F(X_i,y)dy+\frac12\int F(x,y)dxdy.
 \tag{1.6}
\]

For symmetric triple \(F\), its Haar contractions are \(F_1(x,y)=\int F(x,y,z)dz\), \(F_2(x)=\iint F(x,y,z)dydz\), and \(F_0=\int F\). The exact ordered deleted statistic is

\[
 U_3[F]=\frac1{N^3}\sum_{i,j,k\,\mathrm{distinct}}F(X_i,X_j,X_k)
 -\frac3{N^2}\sum_{i\ne j}F_1(X_i,X_j)
 +\frac3N\sum_iF_2(X_i)-F_0.
 \tag{1.7}
\]

Every denominator is a power of N, not a falling factorial. Set

\[
 C\Phi=\operatorname{Sym}_3[K(x-z)\cdot\nabla_x\Phi(x,y)],
 \tag{1.8}
\]

where the symmetrization averages all six permutations. The primary assertion is exactly

\[
 \sigma_N\,\mathbb E\left|\int_0^T U_3[C\Phi_t](X_t)dt\right|\longrightarrow0.
 \tag{1.9}
\]

Its exact negation is admitted fixed \(d,s,T,h\) and a positive finite critical sequence for which the left side has positive limsup. No altered preparation, source, inverse, dynamics, or notion of centering is an admitted counterexample.

Choose the fixed exponent

\[
 \omega=\frac12\min\left\{s,d-s-2,\frac d2-1\right\}>0,
 \quad r=1+\omega,
 \quad e=\frac{s-\omega}{s+2}.
 \tag{1.10}
\]

There are a finite constant C and an index \(N_0\), depending only on the fixed data, fixed kernel/weights, and positive lower and finite upper bounds for the critical sequence on its tail, such that for \(N\ge N_0\),

\[
 \boxed{\quad
 \sigma_N\mathbb E\left|\int_0^T U_3[C\Phi_t]dt\right|
 \le C\left[N^{1/2-\theta}+N^{-1/2}
             +N^{e-1/2}+N^{(a-\theta)/2}\right].\quad}
 \tag{1.11}
\]

All four powers are negative in the frozen range. If \(T=0\), the assertion is exactly zero; constant h also gives \(J=\Phi=0\) by the supplied uniqueness. No statement of a full fluctuation limit follows from this bounded result alone.

## 2. Complete-source and normalization preflight

Only complete permitted arguments are conditional premises. Short theorem cards identify targets and scope, not certification. In particular the historical audit language inside permitted files is not a live audit verdict.

| Permitted complete source | Exact use and retained qualification |
|---|---|
| Frozen R1 model and `ROUND_001_ALGEBRA.md`, Sections 1–5 | Fourier convention, noise, ordered distinct labels, factor one half, six-term symmetrization, both response coefficients and exact lower coefficients. Section 7 below independently recounts the force terms without singular diagonal evaluation. |
| `ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–4 | Positive Riesz heat representation with coefficient one, local smooth remainder, integrable K, finite compensated divergence, and both response signs. The normalization used in the new estimates is reconstructed below. |
| Complete R5 base, conditional inverse, and homogeneous interface; the two supplied interface clarifications | The same full bounded Borel inverse, its Fourier test, and uniform Haar L2 bound when twice s is below d. Section 8 reconstructs the required iid calculation without an unlisted earlier U-statistic proof. The common divergence constant is chosen as in the addendum; symmetry means pair exchange, not self-adjointness. These modules keep their explicit base-process hypotheses. |
| `ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, Sections 3–8 | Actual singular paths and noncollision, fixed-N same-noise heat passage, finite-N density domination, and the exact energy/total-force identity. No uniform-N density bound is inferred. |
| `ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, complete proof, especially Sections 5–11 | The genuine representatives, weak/background derivatives, all partial-diagonal integrals, finite-N true martingale, and exact singular pair identity. Its fixed-N derivative constants are not relabelled uniform. |
| `ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, Sections 2–3 | Actual nonpositive expected energy and positive heat-integral energy identity. Their short proof is reproduced in Section 3. No R9-only corollary, critical total-variation convergence, or law factorization is imported. |
| `ROUND_012_SUBCOULOMB_ACTUAL_NOISE.md`, complete Sections 1–7, with its explicit R7/R8 and energy premises | Uniform weighted gradients at each fixed admissible exponent, and the genuine scaled martingale bracket. Their precise estimates and their regime check are restated in Section 8. No statement outside their strict sub-Coulomb scope is imported. |

The R7 and R11 complete gradient files are in the sealed allowed dossier. The R11 proof was read as an allowed comparison, but no R11 convergence assertion is needed for this construction. Every inherited premise above remains conditional on its supplied complete proof. This construction does not independently recertify its prerequisites.

Here \(s<2\) and \(d\ge4\) imply both \(s<d-2\) and \(2s<d\), strictly. Thus all invoked strict sub-Coulomb and square-integrable source ranges are met. The logarithmic case and the Coulomb endpoint are not reached. For \(D=\operatorname{div}K\), the exact response is

\[
 R_xF(x,y)=-\int F(x+w,y)D(dw),\qquad
 R_yF(x,y)=-\int F(x,y+w)D(dw),
\]
\[
 D=s(d-2-s)g_{s+2}(w)dw,\quad \int D=0,
 \quad D\ge-\kappa\,dw.
 \tag{2.1}
\]

The periodic compensation is retained. The gamma recurrence is
\(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\), and the one-body response multiplier is the negative number \(-4\pi^2c_{d,s}|k|^{s+2-d}\), as in (1.4).

Put

\[
 \alpha=\frac{d-s}{2}>1,\quad c=4\pi^2,\quad
 A=\frac{4^{(d-s)/2}\pi^{d/2}}{\Gamma(s/2)}.
 \tag{2.2}
\]

For the periodized Gaussian \(p_t\), which is positive and has mass one,

\[
 g(z)=A\int_0^\infty t^{\alpha-1}(p_t(z)-1)dt,
 \qquad \widehat p_t(k)=e^{-ct|k|^2}.
 \tag{2.3}
\]

The nonzero coefficient of this integral is
\(A\Gamma(\alpha)c^{-\alpha}|k|^{-2\alpha}=c_{d,s}|k|^{s-d}\).
Substitution \(u=|z|^2/(4t)\) into its Euclidean Gaussian term gives exactly \(|z|^{-s}\). The remaining lattice terms are smooth near zero by their exponentially small short-time tails and integrable long-time derivatives. In particular \(g(z)=|z|^{-s}+\text{smooth}\), \(K(z)=sz|z|^{-s-2}+\text{smooth}\), and the coefficient of the local singularity has not changed.

Every unspecified constant below depends on d,s and finitely many absolutely summable Fourier seminorms of h, and on T or the fixed bounded-diffusivity class where indicated. For instance
\(\sum_k(1+|k|)^{d+4}|\widehat h(k)|\) suffices for the new source estimate. It is finite by smoothness. The coefficients of (1.4) are bounded in absolute value by those of h, uniformly in N, diffusivity, and time.

## 3. Actual energy and a positive close-pair remainder

Write

\[
 H_N(X)=\frac1N\sum_{i<j}g(X_i-X_j),\qquad
 D_2[v]=\frac1{N^2}\sum_{i\ne j}v(X_i,X_j).
 \tag{3.1}
\]

The following actual-law input is worth reconstructing because it supplies the sign in the new argument. First smooth the *particle interaction* by heat convolution, denoting this auxiliary cutoff by \(\eta>0\). At each fixed \(N,\nu>0,\eta\), its smooth law \(F_t^\eta\) starts from density one. Smooth periodic integration by parts gives

\[
 \frac d{dt}\left(\nu\int F_t^\eta\log F_t^\eta
                   +\int H_N^\eta F_t^\eta\right)
 =-\int F_t^\eta|\nabla H_N^\eta+
                            \nu\nabla\log F_t^\eta|^2\le0.
 \tag{3.2}
\]

All coefficients are smooth and bounded at this cutoff; the positive heat equation solution justifies the logarithm, differentiation, and integration by parts. Initial entropy and initial energy are zero; entropy on a probability space of mass one is nonnegative. Thus \(\mathbb EH_N^\eta\le0\).

Let \(g_* =\inf_{z\ne0}g(z)>-\infty\). Heat positivity implies \(H_N^\eta\ge (N-1)g_*/2\). The permitted R6 same-noise passage, followed by local uniform convergence of g away from zero and the realized positive minimum separation, gives convergence of this energy to \(H_N(X_t)\) almost surely at each fixed N and time. Fatou after subtracting the common lower bound gives

\[
 \mathbb EH_N(X_t)\le0,\qquad 0\le t\le T.
 \tag{3.3}
\]

This is the actual law, not product Haar at positive time. The finite-N energy integrability is supplied separately by R6. Exchangeability gives

\[
 \mathbb Eg(X_1-X_2)\le0,\qquad
 \mathbb E|g(X_1-X_2)|\le2|g_*|.
 \tag{3.4}
\]

Consequently the local \(s\)-power pair moment is uniformly bounded. No individual force-square estimate is used.

We now use a *different* cutoff, a heat-integral truncation used only to analyze an observable of the actual singular particles. For \(0<\tau\le2\), set

\[
 g^{>\tau}(z)=A\int_\tau^\infty t^{\alpha-1}(p_t(z)-1)dt,
 \quad W_\tau(z)=A\int_0^\tau t^{\alpha-1}p_t(z)dt,
 \quad c_\tau=\frac{A\tau^\alpha}{\alpha}.
 \tag{3.5}
\]

Here \(W_\tau\ge0\), \(\int W_\tau=c_\tau\), and off zero

\[
 g=g^{>\tau}+W_\tau-c_\tau.
 \tag{3.6}
\]

The smooth zero-mean kernel has positive nonzero Fourier coefficients

\[
 a_\tau(k)=A\int_\tau^\infty t^{\alpha-1}e^{-c|k|^2t}dt>0,
 \quad a_\tau(0)=0,
 \quad 0\le g^{>\tau}(0)\le C\tau^{-s/2}.
 \tag{3.7}
\]

The last bound follows from \(p_t(0)\le Ct^{-d/2}\) for \(t\le1\) and exponential decay of \(p_t(0)-1\) for large t. Exact subtraction of the smooth self diagonal gives, for every collision-free configuration,

\[
 D_2[g^{>\tau}]
 =\sum_{k\ne0}a_\tau(k)|\widehat\eta_N(k)|^2
                  -\frac{g^{>\tau}(0)}N,
 \quad \widehat\eta_N(k)=\frac1N\sum_i e^{-2\pi i k\cdot X_i}.
 \tag{3.8}
\]

Since \(D_2[g]=2H_N/N\), equations (3.3), (3.6), and (3.8) prove the stronger joint inequality

\[
 \mathbb E\sum_{k\ne0}a_\tau(k)|\widehat\eta_N(k)|^2
 +\mathbb ED_2[W_\tau]
 \le \frac{g^{>\tau}(0)}N+\left(1-\frac1N\right)c_\tau
 \le C\left(N^{-1}\tau^{-s/2}+\tau^\alpha\right).
 \tag{3.9}
\]

Both terms on the left are nonnegative, so each obeys this bound. The exact finite-label distinction is

\[
 \mathbb EW_\tau(X_1-X_2)
 \le\frac{g^{>\tau}(0)}{N-1}+c_\tau;
 \tag{3.10}
\]

(3.9) instead uses the ordered sum divided by \(N^2\), which is \((N-1)/N\) times the labelled-pair expectation. No coefficient is transferred between these two conventions.

The smooth diagonal subtraction occurs only in (3.8). No value of \(W_\tau\), g, J, or the corrector is evaluated on a coinciding empirical pair. Their background integrals are Lebesgue integrals of integrable representatives. All the identities are valid first at fixed N; the resulting constants in (3.9) are uniform. Taking

\[
 \varepsilon_N=N^{-2/d}
 \tag{3.11}
\]

makes either right-hand term of (3.9), at \(\tau=2\varepsilon_N\) or \(\varepsilon_N/64\), a fixed constant times \(N^{-\theta}\). Its physical length is \(N^{-1/d}\), exactly the particle-spacing scale; this is not the bounded-rescaled-diffusivity length of an auxiliary pair flow.

## 4. Absolute source-tail control

Let \(\ell(z)=\operatorname{dist}_{\mathbb T^d}(z,0)\). Differentiating the periodized Gaussian term by term gives

\[
 \ell(z)|\nabla p_t(z)|\le C_d p_{2t}(z),\qquad t>0.
 \tag{4.1}
\]

Indeed, for a nearest representative z, \(\ell(z)\le|z+n|\) for every lattice translate. Its differentiated Gaussian term is bounded by
\(|z+n|^2(2t)^{-1}(4\pi t)^{-d/2}e^{-|z+n|^2/(4t)}\).
The elementary bound \(u e^{-u/4}\le C e^{-u/8}\), followed by summing the Gaussian at time \(2t\), proves (4.1). This is a bound on the norm of the sum by the sum of norms and is valid at every off-zero point.

For any smooth real test v, let

\[
 J_v=K(x-y)\cdot(\nabla v(x)-\nabla v(y)),\qquad
 J_v^{>\varepsilon}=-\nabla g^{>\varepsilon}(x-y)
                         \cdot(\nabla v(x)-\nabla v(y)).
\]

The shortest torus segment gives \(|\nabla v(x)-\nabla v(y)|\le\|D^2v\|_\infty\ell(x-y)\). Integrating (4.1) in the positive heat representation, with the change of variable \(u=2t\), proves the pointwise off-diagonal estimate

\[
 |J_v-J_v^{>\varepsilon}|(x,y)
 \le C_{d,s}\|D^2v\|_\infty W_{2\varepsilon}(x-y).
 \tag{4.2}
\]

All differentiations in this step are away from zero, where the short-time Gaussian tail justifies them. Integrability of \(W\) justifies every ensuing background integral. In particular every row integral of the right side is \(C\|D^2v\|_\infty c_{2\varepsilon}\), uniformly in the remaining coordinate. Applying the literal definition (1.6), then (3.9), yields

\[
 \mathbb E|P_N[J_v-J_v^{>\varepsilon}]|
 \le C\|D^2v\|_\infty
       \left(N^{-1}\varepsilon^{-s/2}+\varepsilon^\alpha\right).
 \tag{4.3}
\]

This includes the particle-background and scalar terms: explicitly their coefficients contribute at most \(c_{2\varepsilon}+c_{2\varepsilon}/2\) times the fixed prefactor, while the particle-particle term contributes \(\mathbb ED_2[W_{2\varepsilon}]/2\). No expectation of a signed tail is substituted for its absolute expectation.

## 5. The retained Fourier commutator

We prove the multiplier estimate used here instead of appealing to a general commutator theorem. Define \(a_\varepsilon\) by (3.7), also for nonzero real vectors. If \(u,v\in\mathbb Z^d\setminus\{0\}\), \(m=u+v\ne0\), and
\(\varepsilon |m|^2\le1\), then

\[
 \left|m\cdot\{u a_\varepsilon(u)+v a_\varepsilon(v)\}\right|
 \le C_{d,s}|m|^{2\alpha+1}
             \sqrt{a_{\varepsilon/64}(u)a_{\varepsilon/64}(v)}.
 \tag{5.1}
\]

The constant is independent of \(\varepsilon\in(0,1]\) and every indicated lattice vector. Its dependence on m is polynomial, which will matter for smooth h.

To prove it, set \(L_\varepsilon(k)=k a_\varepsilon(k)\). With
\(\Gamma(\alpha,x)=\int_x^\infty z^{\alpha-1}e^{-z}dz\), substitution gives

\[
 a_\delta(k)=A c^{-\alpha}|k|^{-2\alpha}
                     \Gamma(\alpha,c\delta|k|^2).
 \tag{5.2}
\]

For \(\alpha>1\), \(\Gamma(\alpha,x)\ge c_\alpha e^{-x}\) for all \(x\ge0\): for \(x\ge1\), integrate on \([x,x+1]\) and use \(z^{\alpha-1}\ge1\); for \(x\le1\), use the integral on \([1,2]\). Also \(a_\varepsilon(k)\le C|k|^{-2\alpha}\).

If \(|u|\le2|m|\), then \(|v|\le3|m|\). The right-side square root in (5.1) is at least \(c|u|^{-\alpha}|v|^{-\alpha}\), since \(\varepsilon|u|^2,\varepsilon|v|^2\le9\). It is therefore at least \(c|m|^{-2\alpha}\). Meanwhile, because both nonzero lattice vectors have norm at least one and \(1-2\alpha<0\), the numerator is at most
\(C|m|(|u|^{1-2\alpha}+|v|^{1-2\alpha})\le C|m|\).
This proves (5.1) in that case.

If \(|u|>2|m|\), write
\(u a_\varepsilon(u)+v a_\varepsilon(v)=L_\varepsilon(u)-L_\varepsilon(u-m)\), using evenness of a. Along the segment \(k=u-tm\), \(|u|/2\le|k|\le3|u|/2\). Direct differentiation gives

\[
 \|DL_\varepsilon(k)\|
 \le A\int_\varepsilon^\infty t^{\alpha-1}
                (1+2c|k|^2t)e^{-c|k|^2t}dt
 \le C|k|^{-2\alpha}e^{-c\varepsilon|k|^2/2}.
 \tag{5.3}
\]

For the second inequality, in the rescaled integral use
\(e^{-z}\le e^{-x/2}e^{-z/2}\) for \(z\ge x\); the remaining gamma integrals are finite constants. The segment formula bounds the numerator by

\[
 C|m|^2|u|^{-2\alpha}e^{-c\varepsilon|u|^2/8}.
 \tag{5.4}
\]

On the other hand (5.2) and its lower bound give

\[
 \sqrt{a_{\varepsilon/64}(u)a_{\varepsilon/64}(v)}
 \ge c|u|^{-2\alpha}
       e^{-c\varepsilon(|u|^2+|v|^2)/128}
 \ge c|u|^{-2\alpha}e^{-13c\varepsilon|u|^2/512}.
 \tag{5.5}
\]

Here \(|v|\le3|u|/2\). Since \(1/8>13/512\), (5.4) is at most a constant times \(|m|^2\) times (5.5); \(|m|^2\le|m|^{2\alpha+1}\) for \(|m|\ge1\). This proves (5.1). For m=0 the original multiplier is exactly zero, without any estimate.

Let v have Fourier support \(|m|\le\varepsilon^{-1/2}\). A direct multiplication of \(-\nabla g^{>\varepsilon}\) and the two test gradients shows that the pair Fourier coefficient of \(J_v^{>\varepsilon}\) at \((u,v')\), with \(m=u+v'\), is

\[
 -4\pi^2\widehat v(m)\,
       m\cdot\{u a_\varepsilon(u)+v'a_\varepsilon(v')\}.
 \tag{5.6}
\]

The prime distinguishes the second frequency from the test. The sign and the sum of both gradient contributions are independently checked by direct Fourier polynomial multiplication in the companion diagnostic.

This commutator is smooth and its diagonal is exactly zero, because its gradient difference is zero there. Consequently its literal deleted-pair statistic satisfies

\[
 P_N[J_v^{>\varepsilon}]
 =\frac12\langle\rho^{\otimes2},J_v^{>\varepsilon}\rangle.
 \tag{5.7}
\]

There is no residual self term in (5.7). The separate positive energy kernel does have the self term in (3.8), which has already been retained. Equation (5.7) is not asserted for an undefined singular diagonal.

Since \(\widehat\rho(0)=0\), the pairing in (5.7) uses only nonzero u and v'. Define
\(b(k)=\sqrt{a_{\varepsilon/64}(k)}|\widehat\rho(k)|\) for \(k\ne0\), and zero at k=0. At fixed positive epsilon it is square summable. For each m,
\(\sum_u b(u)b(m-u)\le\sum_u b(u)^2\) by Cauchy–Schwarz and reindexing. Equations (5.1), (5.6), and absolute Fourier convergence give the configuration-wise bound

\[
 |P_N[J_v^{>\varepsilon}]|
 \le C\left[\sum_m|\widehat v(m)|(1+|m|)^{d-s+1}\right]
       \sum_{k\ne0}a_{\varepsilon/64}(k)|\widehat\eta_N(k)|^2.
 \tag{5.8}
\]

Only the explicitly positive Fourier energy is used. A pointwise nonnegative arbitrary weight multiplying g is not asserted to be positive semidefinite.

## 6. The actual unsmoothed quadratic source

Take \(\varepsilon=\varepsilon_N\) from (3.11) and \(R=\varepsilon^{-1/2}\). Split the actual Fourier series (1.4) exactly as
\(f_t=f_t^{\le R}+f_t^{>R}\). This is an analytical decomposition of the fixed source, not a changed source or inverse. The series is conjugate symmetric, so both pieces are real.

The low part has uniformly bounded Hessian and uniformly bounded seminorm in (5.8), since its coefficient magnitudes are at most those of h. Equations (3.9), (4.3), and (5.8) therefore give

\[
 \mathbb E|P_N[J_{f_t^{\le R}}]|
 \le C\left(N^{-1}\varepsilon^{-s/2}+\varepsilon^\alpha\right)
 =C N^{-\theta}.
 \tag{6.1}
\]

Arbitrarily high Fourier modes of h require a separate check. No factor such as \(e^{C\varepsilon|m|^2}\) is summed against a merely smooth test. Let
\(H_* =\sum_m(1+|m|)^{d+4}|\widehat h(m)|<\infty\). Then

\[
 \sup_{t,N,\nu}\|f_t^{>R}\|_{C^2}
 \le C H_* R^{-(d+2)}.
 \tag{6.2}
\]

The zero Fourier mode lies in the low part. The local kernel expansion gives
\(|J_w(x,y)|\le C\|w\|_{C^2}(1+\ell(x-y)^{-s})\).
Its background row integrals are bounded, and the actual pair moment is uniformly bounded by (3.4). Thus

\[
 \mathbb E|P_N[J_{f_t^{>R}}]|
 \le C H_* R^{-(d+2)}
 =C H_*\varepsilon^{(d+2)/2}
 \le C H_*\varepsilon^\alpha,
 \tag{6.3}
\]

because \(\alpha=(d-s)/2<(d+2)/2\) and \(\varepsilon\le1\). Combining the exact linear split with (6.1)–(6.3) proves the new uniform estimate

\[
 \boxed{\qquad
 \sup_{0\le t\le T}\mathbb E|P_N[J_t]|
                      \le C_{d,s,h}N^{-\theta}.
 \qquad}
 \tag{6.4}
\]

The constant is independent of N and of the diffusivity in the actual homogeneous Fourier test. Positive diffusivity is used only in the free-energy proof; the deterministic energy proof also gives the same estimate at zero noise, though that endpoint is not needed for the finite-temperature sequence. No evolving iid approximation is used. Tonelli and (6.4) yield

\[
 \sigma_N\mathbb E\left|\int_0^T P_N[J_t]dt\right|
 \le \sigma_N\int_0^T\mathbb E|P_N[J_t]|dt
 \le C_T N^{1/2-\theta}.
 \tag{6.5}
\]

This is a stronger instantaneous absolute estimate for the quadratic source. It is not an instantaneous absolute estimate for the cubic kernel.

## 7. Literal singular-domain identity and all contractions

We use exactly the R8 domain of the supplied genuine inverse. To make its relevance and factors explicit, write
\(G(x,y)=\nabla_x\Phi(x,y)\), \(A_\Phi(x)=\int G(x,y)dy\), and
\(q_\Phi(x)=\int\Phi(x,y)dy\). The full response has its integrated-gradient representative off the pair diagonal. Direct integration of the six distinct expressions in (1.8) gives

\[
 (C\Phi)_1(x,y)=\frac16\left[
 K(x-y)\cdot(A_\Phi(x)-A_\Phi(y))+(R_x+R_y)\Phi(x,y)\right],
 \tag{7.1}
\]
\[
 (C\Phi)_2(x)=\frac13 v_\Phi(x),\quad
 v_\Phi(x)=\int K(z-x)\cdot A_\Phi(z)dz,\quad
 (C\Phi)_0=0,\quad ((R_x+R_y)\Phi)_\mu=v_\Phi.
 \tag{7.2}
\]

These are the actual Haar contractions in (1.7). None is suppressed. In particular the all-distinct triple sum is empty at N=2, but its lower background terms need not be zero.

Here are the domain checks from the complete permitted R8 proof, in their finite-N scope. Choose any \(1<q_1<d/2\) and \(q_1+1<q_2<d\). The inverse is locally \(C^1\) in time and \(C^2\) off the pair diagonal, has global weak first and second derivatives, with bounded-in-time gradient and Hessian majorants \(C_Nw_{q_1}\) and \(C_Nw_{q_2}\). Its time derivative and the structurally grouped internal drift are Haar integrable; its gradient is Haar square integrable. Slice weak differentiation gives the actual background derivatives and \(\int\Delta_y\Phi(x,y)dy=0\).

For the cubic, each raw term has majorant
\(C_N|K(x-z)|w_{q_1}(x-y)\). Integrating in the two independent relative variables gives

\[
 \int |K(x-z)||G(x,y)|\,dxdydz
 \le\|K\|_1\sup_x\int|G(x,y)|dy<\infty.
 \tag{7.3}
\]

The exponents \(s+1<d\) and \(q_1<d\) are checked separately. Their sum need not be below d. For a one-background contraction with two distinct fixed empirical coordinates, the two possible singular locations in the background variable are separated, each with its own integrable local exponent. The remaining two-background terms follow by absolute Fubini. This handles all partial and simultaneous triple collisions without assigning \(G(x,x)\) or \(C\Phi(x,x,z)\).

For clarity, the force term in direct Itô differentiation of (1.6), while stopped away from all actual particle collisions, is exactly

\[
 Q=\frac1{N^3}\sum_{i\ne j}\sum_{k\ne i}
       K(X_i-X_k)\cdot G(X_i,X_j)
 -\frac1{N^2}\sum_{i\ne k}K(X_i-X_k)\cdot A_\Phi(X_i).
 \tag{7.4}
\]

Separate k=j from the three distinct labels before estimating. Pairing the two orientations of the repeated pair gives \(D_2[B\Phi]/(2N)\). The distinct part is the distinct sum of \(C\Phi\); substitution of (7.1)–(7.2) into its definition gives

\[
 Q=U_3[C\Phi]+P_N[(R_x+R_y)\Phi]+\frac1{2N}D_2[B\Phi].
 \tag{7.5}
\]

The independent diffusion contributes \(P_N[\nu\Delta_{x,y}\Phi]\). There is no cross variation between two distinct particle labels, and the background Haar Laplacians integrate to zero as just justified. Thus there is no additional thermal trace. Writing
\(b_t(x)=\int B\Phi_t(x,y)dy\), \(\bar b_t=\int B\Phi_t\), the elementary identity
\(D_2[B\Phi]=2P_N[B\Phi]+2\rho[b_t]+\bar b_t\), together with the full inverse equation, gives exactly

\[
 dP_N[\Phi_t]
 =\left[-P_N[J_t]+U_3[C\Phi_t]
          +\frac1N\rho_t[b_t]+\frac1{2N}\bar b_t\right]dt+dM_t^2,
 \tag{7.6}
\]
\[
 M_t^2=\sqrt{2\nu_N}\sum_i\int_0^t
        \nabla_iP_N[\Phi_u](X_u)\cdot dW_i(u),\quad
 \nabla_iP_N[\Phi]=\frac1{N^2}\sum_{j\ne i}G(X_i,X_j)
                                  -\frac1N A_\Phi(X_i).
 \tag{7.7}
\]

The finite-N density bound is \(F_t\le e^{(N-1)\kappa T}\). It transfers (7.3) and the other integrable drift majorants to finite absolute expected time integrals, and the Haar square-integrable gradient to a finite expected bracket. The supplied noncollision gives a positive realized separation on \([0,T]\). Removing the collision stops uses L1 convergence of each displayed drift and L2 convergence of the stochastic integral; it yields the same genuine identity and a square-integrable true martingale. These are the complete R8 passage mechanisms. Their exponential density constant is used only for fixed-N validity, never for an N-uniform estimate.

Terminal zero and \(M_0^2=0\) now give the pathwise integrated identity

\[
 \int_0^T U_3[C\Phi_t]dt
 =\int_0^T P_N[J_t]dt-P_N[\Phi_0]-M_T^2
                  -\frac1N\int_0^T\rho_t[b_t]dt
                  -\frac1{2N}\int_0^T\bar b_tdt.
 \tag{7.8}
\]

The target concerns the absolute value after this time integral, which is why (7.8) is an admissible proof route. Estimating only \(\mathbb EU_3\), or replacing the left side by an unproved absolute instantaneous bound, would not suffice.

## 8. Endpoint, lower terms, and the full noise

At positive finite criticality,

\[
 \nu_N=\lambda_N^{-1}N^{-\theta},\qquad
 \nu_NN^{2/p}=\lambda_N^{-1}
       N^{s(s+2-d)/(d(s+2))}.
 \tag{8.1}
\]

Since \(d>s+2\), this rescaled diffusivity is eventually bounded, and \(\nu_N\to0\), \(\beta_N\to\infty\), \(b_N=1\) eventually. All source, inverse, domain, and R12 gradient/noise hypotheses hold on this tail for fixed finite \(L,\nu_*\).

The complete R5 full-inverse bound gives \(\|\Phi_0\|_{L^2(dxdy)}^2\le C\), since \(2s<d\). The following direct iid calculation supplies its endpoint consequence without an unlisted U-statistic input:

\[
 \sigma_N^2\mathbb E|P_N[\Phi_0]|^2\le\frac{C b_N}{N}.
 \tag{8.2}
\]

To check (8.2), for any symmetric Haar L2 kernel F define \(m=\int F\), \(q_0(x)=\int F(x,y)dy-m\), and \(F_\circ(x,y)=F(x,y)-q_0(x)-q_0(y)-m\). Both rows of \(F_\circ\) have mean zero. Exact distinct-label counting gives

\[
 P_N[F]=\frac12D_2[F_\circ]-\frac1N\eta_N[q_0]-\frac{m}{2N}.
 \tag{8.2a}
\]

Under iid Haar sampling, two distinct-pair summands of \(F_\circ\) are orthogonal unless their unordered labels coincide: a singly occurring label integrates to zero. They are also orthogonal to every \(q_0(X_i)\). Independence similarly gives variance \(\|q_0\|_2^2/N\) for \(\eta_N[q_0]\). Thus

\[
 \mathbb E|P_N[F]|^2
 =\frac{N-1}{2N^3}\|F_\circ\|_2^2
   +\frac1{N^3}\|q_0\|_2^2+\frac{m^2}{4N^2},
 \quad \|F\|_2^2=\|F_\circ\|_2^2+2\|q_0\|_2^2+m^2.
 \tag{8.2b}
\]

These identities are first immediate for bounded kernels and pass by L2 approximation; finite sums and product Haar make all displayed evaluations converge in L2. Multiplying by \(Nb_N\) bounds the first expression by \(b_N\|F\|_2^2/(2N)\). Applying it to the supplied genuine \(\Phi_0\) proves (8.2). It is applied only initially, yielding \(\sigma_N\mathbb E|P_N[\Phi_0]|\le C N^{-1/2}\). No evolved iid estimate is made.

The complete R12 estimate, in its exact bounded-rescaled-diffusivity class, supplies for any fixed \(1<r<d/2\), \(r\le s+1\),

\[
 |\nabla_{\rm pair}\Phi_t(x,y)|
 \le C_r N^{(s+1-r)/p}w_r(x-y),
 \tag{8.3}
\]

uniformly in time and the admitted parameters. With r from (1.10),
\(r<d-s-1\) as well, and \(s+1+r=p+\omega<d\). Therefore, using the actual gradient representative,

\[
 |B\Phi_t(x,y)|\le C N^e w_{s+1+r}(x-y),\qquad
 \|b_t\|_\infty+|\bar b_t|\le C N^e.
 \tag{8.4}
\]

The product is integrable for this explicitly chosen exponent. This does not make the crude product integrable for every R8 exponent or transfer a fixed-N gradient constant to a uniform one. It uses the exact R12 polynomial bound. The two lower terms in (7.8) hence satisfy separately

\[
 \frac{\sigma_N}{N}\mathbb E\left|\int_0^T\rho_t[b_t]dt\right|
 \le C N^{e-1/2},\qquad
 \frac{\sigma_N}{2N}\left|\int_0^T\bar b_tdt\right|
 \le C N^{e-1/2}.
 \tag{8.5}
\]

The first uses \(|\rho_t[b_t]|\le2\|b_t\|_\infty\); the second retains its exact coefficient one half. Neither term is discarded by an unproved centering assertion.

For the genuine martingale, the complete R12 bound is

\[
 Q_N:=\sigma_N^2\mathbb E\langle M^2\rangle_T
 =2\nu_NNb_N\mathbb E\int_0^T
                   \sum_i|\nabla_iP_N[\Phi_t](X_t)|^2dt
 \le C b_NN^a(N^{-\theta}+\nu_N).
 \tag{8.6}
\]

This uses its proved gradient with exponent p/2 and the actual positive Laplacian-density occupation, not a bound on an individual squared pair force. Both responses and every cross term of the full nonnegative bracket are retained there. At criticality it is at most \(C N^{a-\theta}\). The true-martingale property in Section 7 and Itô isometry give

\[
 \sigma_N\mathbb E|M_T^2|\le\sqrt{Q_N}
                                \le C N^{(a-\theta)/2}.
 \tag{8.7}
\]

No first-moment bound is renamed concentration; this is an L2 bound for the actual stochastic integral.

Finally,

\[
 \theta-\frac12=\frac12-\frac sd>0,\qquad
 \frac12-e=\frac{2-s+2\omega}{2(s+2)}>0,
\]
\[
 \theta-a=\frac{2d-s(s+2)}{d(s+2)}>0,
 \tag{8.8}
\]

because \(s<2\), \(d\ge4\), and thus \(s(s+2)<8\le2d\). Inserting (6.5), (8.2), (8.5), and (8.7) into (7.8) proves (1.11), hence (1.9). The exact negation is excluded conditional on the stated earlier modules. No equality boundary is included by these strict inequalities.

## 9. Falsification route and adversarial self-review

The analytical construction was tested independently at the coefficient level by a newly written standard-library exact Fourier/finite-label program. It reads no prior checker. It uses rational coefficients in formal Fourier polynomials, direct subset/deleted-label sums, and a direct N-particle generator, rather than deriving the target side from (7.5). Its finite smooth diagnostics can be embedded in the first coordinate of the admitted d-dimensional torus; they do not replace the singular argument or the actual law. The common physical factor \((2\pi)^2\) is factored out of all spatial second-order expressions, and the source coefficient is checked separately in (5.6).

The diagnostic covers N=2,3,4, zero and positive noise, constant/additive/relative/mixed pair kernels, both response slots, all lower contractions including the scalar, direct drift and bracket coefficients, the independently counted initial iid second moment, the full smooth commutator self diagonal, positive-kernel pair decomposition with exact N versus N-1 coefficients, and a rational grid of the critical exponent inequalities. Its separate high-frequency calculation checks the cancellation between the two commutator frequencies in a solvable inverse-power multiplier. Exact counts and all results are in the sealed JSON. No Monte Carlo inference or tolerance is used.

| Attempted failure | Resolution in this construction |
|---|---|
| Positive expected energy might be hidden by an iid assumption at positive time. | The smooth free-energy inequality is passed to the actual singular law at fixed N in Section 3. Product structure is used only initially. |
| A positive low-heat remainder is treated as a signed cancellation. | Equation (3.9) retains the two nonnegative terms jointly; (4.2) controls the absolute source tail pointwise. |
| The labelled-pair and N-squared normalized pair coefficients are confused. | Equations (3.9) and (3.10) state both exact formulas; the checker tests the conversion. |
| The smooth self diagonal is silently removed. | It is explicitly subtracted for the energy in (3.8); it is exactly zero for the commutator in (5.7). No singular diagonal extension is used. |
| A smaller cutoff incurs an exponential cost in a smooth terminal mode. | Lemma (5.1) has a polynomial cost only on the stated low band. Section 6 estimates the complementary source directly, using a fixed finite Fourier seminorm. No exponential is summed against smooth decay. |
| An arbitrary weighted Riesz kernel is called positive. | Only the explicitly positive coefficients of g greater than the cutoff enter the Cauchy–Schwarz argument. |
| A Haar bound is transferred to the evolved law. | The source estimate uses actual energy. Uniform contraction bounds are pointwise. The noise is the explicit R12 actual-law estimate. Fixed-N density domination is used solely to justify the identity. |
| A cubic partial diagonal or background response is missing. | Equations (7.1)–(7.7) retain all contractions and give the separated-variable integrability check before the identity is used. |
| The pair inverse was replaced by a cutoff inverse. | Only J is decomposed inside an exact linear estimate. The original Phi, original f, both responses, and original actual paths remain in (7.8). |
| The absolute time integral was confused with the integral of the absolute cubic. | Only the stated target is proved, using (7.8). No uniform instantaneous cubic claim is made. |
| The noise or lower bounds miss the corner d=4 and s near 2. | The strict exponent calculation (8.8) and the explicit positive omega retain decay there, with constants allowed to deteriorate as fixed s approaches the excluded endpoint. |
| Same-context checking is called independent certification. | This report remains a construction and self-check; an isolated reconstruction and hostile audit are outstanding. |

The initial strategy considered a smooth-cubic/tail reduction. The completed proof instead controls the original quadratic source through positive heat remainders and uses the exact integrated pair identity. No failed route or generic-law example is offered as a counterexample to THM-036. No external source became necessary. There is no novelty assertion.

## 10. Disposition, nonclaims, and recoverable handoff

| Frozen target | Construction disposition |
|---|---|
| Exact actual-law integrated THM-036 cubic limit for d at least 4 and s strictly between 0 and 2 at positive finite critical coupling | PROVED_CANDIDATE, conditional on the complete permitted prerequisites, by (1.11). |
| An admitted counterexample to that target | None found; the candidate bound excludes its exact negation under those same premises. |
| Genuine singular domain, partial diagonals, exact background contractions | Earlier full R8 domain retained, explicitly checked for applicability and used without a diagonal extension. |
| Stronger absolute instantaneous cubic estimate | Not proved or claimed. |
| Full CLT, broader exponent or temperature range, hierarchy truncation/resummation, logarithmic case, nonhomogeneous or different-law statement | Not proved or claimed. |
| Independent mathematical certification | Not performed in this constructor context. |

The next action is a fresh statement-only reconstruction and hostile audit of the positive-tail/commutator mechanism and its use of the R12 and R8 premises. The first remaining gate is independent verification of this construction, not an unproved estimate inside the stated conditional proof. If any premise or new estimate fails review, the theorem status must be repaired explicitly in a separately issued artifact.

Only this memorandum and the assigned artifact directory were created in the isolated worktree, in addition to the copied permitted task/theorem/manifest files. No canonical ledgers or manuscript source were changed. No TeX file was created or modified; the final handoff contains no mathematical LaTeX. Issued bytes are immutable. Root alone may integrate the result and assign canonical ledger dispositions.
