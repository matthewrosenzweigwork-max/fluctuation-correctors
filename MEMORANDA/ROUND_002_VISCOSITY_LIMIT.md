# Round 002: diffusivity continuity and fixed-smooth covariance limits

Date: 2026-09-17 UTC. Task: TASK-016. Constructor: /root/r002_falsification, gpt-6-astra Max. Worktree: /private/tmp/hocf-round002-falsification-20260917. Input commit: a06178658d1e3d458536ff312ca793947212ec67.

Mathematical status: **PROVED_CANDIDATE**. Audit status: **SELF_CHECKED**; independent review is required. Source status: the smooth model, elementary characteristic/maximum-principle arguments, and the two identified sealed candidate proofs. No singular, equilibrium, inviscid-limit, or parabolic estimate is imported from an external source.

The reports ROUND_002_FALSIFICATION.md and ROUND_002_SMOOTH_GAUSSIAN.md remain byte-for-byte unchanged, respectively at SHA-256 125317981b543cf83a47a64efc1455453fbd942e476a52b15e64ec984c216856 and 7c581d5d9a34f7e0fd277c183321e4b789f10fe11e265e27cc461a2a2352438e. This is a new construction, not an independent audit of either report. The root's separate rendering erratum has no mathematical role here.

## 1. Assertion, scope, and norms

Fix smooth periodic \(K=-\nabla g\), \(b=-\nabla V\), a smooth strictly positive probability density \(\mu_0\), a finite horizon \(T\), and the finite real terminal list \((t_a,\phi_a)\) of TASK-014. For diffusivity \(\nu\in[0,\bar\nu]\), consider

\[
 \partial_t\mu^\nu=-\operatorname{div}(u^\nu\mu^\nu)+\nu\Delta\mu^\nu,
 \qquad u^\nu=b+K*\mu^\nu,\qquad \mu^\nu(0)=\mu_0. \tag{1.1}
\]

For \(\nu>0\), existence of the smooth probability solution on the prescribed interval is the existing frozen model input. This report proves uniqueness, uniform a priori spatial bounds, and parameter continuity in that class; it does not appeal to these estimates as an unexplained existence theorem. For \(\nu=0\), Section 2 constructs the solution explicitly and globally on every finite horizon.

For each terminal index define the **full** backward solution by

\[
 (\partial_t+u^\nu\cdot\nabla+\nu\Delta+R_{\mu^\nu})f_a^\nu=0,
 \qquad f_a^\nu(t_a)=\phi_a, \tag{1.2}
\]

\[
 R_\mu f(y)=\int K(z-y)\cdot\nabla f(z)\,\mu(z)\,dz. \tag{1.3}
\]

The response is retained in every construction and comparison. The source of the full operator is the frozen THM-008 definition; no independent-transport replacement is made.

For scalar functions, \(\|\cdot\|_{C^m}\) is the maximum of the supremum norms of all spatial derivatives of total order at most \(m\). For vector fields, also take the maximum over components. The torus has volume one. Put \(K_m=\|K\|_{C^m}\), \(b_m=\|b\|_{C^m}\), and \(U_m=b_m+K_m\).

**Parameter-continuity assertion.** For each fixed nonnegative integer \(m\), there are explicit finite constants below such that

\[
 \sup_{t\le T}\|\mu^\nu_t-\mu^{\nu'}_t\|_{C^m}
 \le C_{\mu,m}|\nu-\nu'|, \tag{1.4}
\]

\[
 \max_a\sup_{t\le t_a}\|f_a^\nu(t)-f_a^{\nu'}(t)\|_{C^m}
 \le C_{f,m}|\nu-\nu'|. \tag{1.5}
\]

No constant involves \(1/\nu\), \(1/\nu'\), or a lower bound on diffusivity. The comparisons cost two spatial derivatives of the compared density or backward kernel. If only the assigned finite \(C^r\) bounds are used, take \(m+2\le r=4d+12\); the covariance application needs only \(m=0\) for the density and \(m=1\) for the backward kernels. The fixed input fields are smooth, so the additional displayed kernel/drift norms are finite.

The exact negation is a permitted fixed smooth family and two converging finite/zero diffusivities for which the claimed norm or covariance convergence fails. Sections 2–6 provide a complete candidate proof excluding it in the stated smooth class. There is no claim uniform over a singular interaction family.

## 2. Construction and uniqueness at zero diffusivity

Write a periodic lift of the characteristic map as \(F_t(x)=x+h_t(x)\). It solves the closed integral equation

\[
 \begin{split}
 F_t(x)=x+\int_0^t\Big\{b(F_s(x))
 +\int_{\mathbb T^d}K(F_s(x)-F_s(y))\,\mu_0(y)\,dy\Big\}ds.
 \end{split} \tag{2.1}
\]

The periodic lift convention makes this equation meaningful without choosing a global torus difference. Changing a lift by an integer leaves the vector fields unchanged.

On continuous periodic displacements, the integrand in (2.1) is Lipschitz in the supremum norm, with constant \(L_b+2L_K\), where \(L_b,L_K\) are Euclidean Lipschitz constants of the periodic vector fields. Indeed, the \(b\) difference costs \(L_b\|F-G\|_\infty\), and the two arguments in the interaction difference cost \(2L_K\|F-G\|_\infty\). Picard iteration is therefore a contraction on a sufficiently short fixed interval. The bound \(\|b\|_\infty+\|K\|_\infty\) on the speed and the same Lipschitz constant allow continuation on consecutive intervals to every finite \(T\).

Define \(\mu_t^0=(F_t)_\#\mu_0\). It is a probability measure and \(F_t\) is the ordinary flow of \(u_t^0=b+K*\mu_t^0\). For every spatial order \(j\), the derivatives of this velocity are bounded by the fixed norms \(U_j\), because convolution is against a probability measure. The first spatial Jacobian solves

\[
 \partial_t DF_t(x)=Du_t^0(F_t(x))DF_t(x),\qquad DF_0=I.
 \tag{2.2}
\]

Repeated differentiation gives linear equations for each highest-order derivative, with known lower-order products as sources. Gronwall induction proves smoothness of the flow at every finite spatial order. Its inverse is obtained from the backward characteristic ODE, and

\[
 \det DF_t(x)=
 \exp\left(\int_0^t\operatorname{div}u_s^0(F_s(x))\,ds\right)>0.
 \tag{2.3}
\]

Consequently its pushforward has the smooth positive density

\[
 \mu_t^0(F_t(x))=
 \mu_0(x)\exp\left(-\int_0^t\operatorname{div}u_s^0(F_s(x))\,ds\right).
 \tag{2.4}
\]

Differentiation along characteristics proves (1.1) at \(\nu=0\). Conversely, any smooth solution of that transport equation is transported by its own smooth characteristic flow. That flow must solve (2.1), whose fixed point is unique. This proves uniqueness in the required inviscid smooth class. The convolution velocity remains globally Lipschitz because \(K\) is fixed and smooth; no local nonlinear conservation-law regularity claim is being imported.

## 3. Uniform a priori estimates and backward construction

Here and below all time bounds are on the fixed finite horizon. Define the transport commutator constant

\[
 p_m=d(2^m-1)U_m. \tag{3.1}
\]

For each derivative \(\partial^\alpha\) with \(|\alpha|\le m\), commuting through \(u^\nu\cdot\nabla\) produces

\[
 \sum_{0<\gamma\le\alpha}\binom{\alpha}{\gamma}
   (\partial^\gamma u^\nu)\cdot
      \nabla\partial^{\alpha-\gamma}h.
 \tag{3.2}
\]

The derivative of \(h\) in every summand has order at most \(m\), and the sum is bounded by \(p_m\|h\|_{C^m}\). At a spatial maximum the diffusion term has the favorable sign for every \(\nu\ge0\). At \(\nu=0\) the same inequality follows directly along characteristics. Applying this observation to each sign of every derivative yields the usual upper-right Dini-derivative inequality for their maximum; thus no positive-diffusivity estimate is hidden in the next bounds.

Write the density equation as

\[
 \partial_t\mu^\nu+u^\nu\cdot\nabla\mu^\nu-\nu\Delta\mu^\nu
   =-(\operatorname{div}u^\nu)\mu^\nu.
 \tag{3.3}
\]

Leibniz's rule bounds the differentiated right side by
\(d\,2^m U_{m+1}\|\mu^\nu\|_{C^m}\). It follows that

\[
 \sup_{\nu,t}\|\mu^\nu_t\|_{C^m}\le M_m,\qquad
 M_m=\|\mu_0\|_{C^m}
       \exp\{T(p_m+d\,2^mU_{m+1})\}. \tag{3.4}
\]

The suprema are over the existing smooth family, including the constructed zero-diffusivity member. The bounds are independent even of the chosen upper bound \(\bar\nu\). Mass conservation follows by integrating (1.1). Positivity can also be tracked explicitly: the lower barrier
\((\inf\mu_0)e^{-dU_1t}\) is preserved by (3.3) and the same maximum-principle argument. Formula (2.4) gives the inviscid instance directly.

To control the full response without losing a derivative of its argument, integrate (1.3) by parts:

\[
 R_\mu f(y)=
 -\sum_{j=1}^d\int f(z)
  \{\partial_{z_j}K_j(z-y)\mu(z)
       +K_j(z-y)\partial_{z_j}\mu(z)\}\,dz. \tag{3.5}
\]

Derivatives in the output variable \(y\) fall only on \(K\). Since the measure has mass one and
\(\sum_j\|\partial_j\mu\|_{L^1}\le dM_1\),

\[
 \|R_{\mu_t^\nu}f\|_{C^m}
 \le r_m\|f\|_\infty,\qquad
 r_m=d(K_{m+1}+K_mM_1). \tag{3.6}
\]

This is a bounded nonlocal operator estimate, not a Markov contraction statement.

For a direct zero-diffusivity backward construction, let \(P_{t,s}^0 h=h\circ F_{t,s}^0\) be transport by the velocity \(u^0\). The commutator estimate above gives
\(\|P_{t,s}^0h\|_{C^m}\le e^{p_m(s-t)}\|h\|_{C^m}\).
Solve the Volterra equation

\[
 f_a^0(t)=P_{t,t_a}^0\phi_a+
          \int_t^{t_a}P_{t,s}^0 R_{\mu_s^0}f_a^0(s)\,ds. \tag{3.7}
\]

Its \(n\)-th successive response term is bounded in \(C^m\) by

\[
 \|\phi_a\|_{C^m}e^{p_m(t_a-t)}
       \frac{(r_m(t_a-t))^n}{n!}. \tag{3.8}
\]

The series therefore converges on the full interval, solves (3.7), and is unique by the same Volterra bound. Construct it at every finite \(m\); uniqueness makes the constructions compatible, yielding a smooth full backward solution. Differentiation of (3.7) gives (1.2), including its response term.

For positive diffusivity, the transport-diffusion propagator with the prescribed smooth velocity \(u^\nu\) satisfies the identical \(C^m\) estimate by (3.2) and the maximum principle. It can equivalently be constructed from the smooth additive-noise SDE; differentiating its initial-position flow gives the same spatial commutators, with no derivative of the Brownian translation. The Volterra series (3.7) with that propagator therefore constructs the full backward solution as well.

In particular, with \(\phi_m=\max_a\|\phi_a\|_{C^m}\),

\[
 \max_{a,\nu,t\le t_a}\|f_a^\nu(t)\|_{C^m}
 \le F_m,\qquad F_m=\phi_m e^{T(p_m+r_m)}. \tag{3.9}
\]

The inhomogeneous zero-terminal equation obeys, by the same commutator/response calculation,

\[
 \|w(t)\|_{C^m}\le
 \int_t^{t_a}e^{(p_m+r_m)(s-t)}\|G(s)\|_{C^m}\,ds
 \tag{3.10}
\]

when \((\partial_t+u^\nu\cdot\nabla+\nu\Delta+R_{\mu^\nu})w=G\) and \(w(t_a)=0\). The sign of \(G\) does not affect this norm estimate.

Thus the density and one-body spatial bounds needed here have been proved for the fixed smooth model. The pair-kernel bounds along the particle-temperature sequence remain precisely the already assigned assumptions from PO-001/TASK-014; no pair assumption is silently removed or attributed to a singular family. A pair kernel at exactly zero diffusivity is not needed to identify the covariance below.

## 4. Mean-field parameter comparison

Put \(\delta=\mu^\nu-\mu^{\nu'}\) and \(v=K*\delta\). Their difference equation, using diffusivity \(\nu\) in its principal part, is exactly

\[
 \begin{split}
 \partial_t\delta+u^\nu\cdot\nabla\delta-\nu\Delta\delta
  ={}&-(\operatorname{div}u^\nu)\delta
      -v\cdot\nabla\mu^{\nu'}
      -(\operatorname{div}v)\mu^{\nu'}\\
    &+(\nu-\nu')\Delta\mu^{\nu'},\qquad \delta(0)=0.
 \end{split} \tag{4.1}
\]

Since the torus volume is one,

\[
 \|v\|_{C^m}\le K_m\|\delta\|_{L^1}
               \le K_m\|\delta\|_\infty,\qquad
 \|\operatorname{div}v\|_{C^m}
               \le dK_{m+1}\|\delta\|_\infty. \tag{4.2}
\]

These are convolution estimates against the signed density difference, not positivity claims. The two response-like density products in (4.1) therefore have total \(C^m\) norm at most

\[
 d\,2^m(K_mM_{m+1}+K_{m+1}M_m)\|\delta\|_\infty. \tag{4.3}
\]

The diffusivity forcing has norm at most
\(d|\nu-\nu'|M_{m+2}\). Combining the maximum-principle derivative estimate, (3.3)'s product bound, and (4.3), define

\[
 h_m=p_m+d\,2^mU_{m+1}
          +d\,2^m(K_mM_{m+1}+K_{m+1}M_m).
 \tag{4.4}
\]

Gronwall with zero initial difference proves (1.4) with the explicit sufficient constant

\[
 C_{\mu,m}=dTM_{m+2}e^{h_mT}. \tag{4.5}
\]

This proof includes \(\nu=0\), \(\nu'=0\), and either ordering of the parameters. Applying the same homogeneous inequality when the diffusivities and initial data agree gives uniqueness among existing smooth solutions. For the constructed inviscid solution it agrees with the independent characteristic uniqueness proof.

The two extra spatial derivatives are visible in the forcing \((\nu-\nu')\Delta\mu^{\nu'}\). There is no division by the diffusivity of the principal operator and no parabolic smoothing estimate used to hide this loss.

## 5. Full backward parameter comparison

Fix a terminal index and put \(w=f^\nu-f^{\nu'}\). The terminal value of \(w\) is zero, and subtraction gives

\[
 \begin{split}
 (\partial_t+u^\nu\cdot\nabla+\nu\Delta+R_{\mu^\nu})w
 ={}&-(\nu-\nu')\Delta f^{\nu'}
      -(K*\delta)\cdot\nabla f^{\nu'}\\
    &-(R_{\mu^\nu}-R_{\mu^{\nu'}})f^{\nu'}.
 \end{split} \tag{5.1}
\]

Both changes caused by the density are present: the transport velocity difference and the response difference. The latter is exactly

\[
 (R_{\mu^\nu}-R_{\mu^{\nu'}})f^{\nu'}(y)
 =\int K(z-y)\cdot\nabla f^{\nu'}(z)\delta(z)\,dz. \tag{5.2}
\]

For this difference it is better to use the displayed form directly. Output derivatives again hit only \(K\), so

\[
 \|(R_{\mu^\nu}-R_{\mu^{\nu'}})f^{\nu'}\|_{C^m}
 \le dK_m F_1\|\delta\|_\infty. \tag{5.3}
\]

Thus no derivative of the density difference is lost through the full response. The transport difference has norm at most
\(d\,2^mK_mF_{m+1}\|\delta\|_\infty\). Using (4.5) with \(m=0\), the entire right side in (5.1) is bounded by

\[
 d|\nu-\nu'|
 \{F_{m+2}+K_m(2^mF_{m+1}+F_1)C_{\mu,0}\}. \tag{5.4}
\]

Equation (3.10) proves (1.5) with

\[
 C_{f,m}=dT e^{(p_m+r_m)T}
 \{F_{m+2}+K_m(2^mF_{m+1}+F_1)C_{\mu,0}\}. \tag{5.5}
\]

Only the \(C^0\) density comparison is needed for this estimate, thanks to the fixed smooth convolution kernel. The two additional derivatives of \(f^{\nu'}\) come from the explicit Laplacian forcing. Equations (3.4), (3.9), (4.5), and (5.5) list sufficient dependencies entirely in terms of fixed initial data, terminal tests, \(d,T\), and finitely many derivatives of \(b,K\). If the assigned uniform finite norms are used instead, replace \(M_j,F_j\) by those bounds for the displayed orders. Neither implementation introduces an inverse diffusivity.

## 6. Identification of covariance limits

Define continuous prefactors on \([0,\infty)\) by

\[
 \vartheta(\nu)=
 \begin{cases}1,&0\le\nu\le1,\\ \nu^{-1},&\nu>1,\end{cases}
 \qquad
 \chi(\nu)=\min(1,\nu).
 \tag{6.1}
\]

Both functions are globally Lipschitz with constant one. For positive \(\nu=1/\beta\), they equal the old prefactors \(a_N^2=\min(\beta,1)\) and \(c_N=\min(1,\beta^{-1})\), respectively.

Use the actual smooth family to define

\[
 I^{ab}(\nu)=\vartheta(\nu)
     \operatorname{Cov}_{\mu_0}(f_a^\nu(0),f_b^\nu(0)), \tag{6.2}
\]

\[
 D^{ab}(\nu)=2\chi(\nu)
       \int_0^{t_a\wedge t_b}
       \mu_r^\nu(\nabla f_a^\nu(r)\cdot\nabla f_b^\nu(r))\,dr.
 \tag{6.3}
\]

In particular \(D(0)=0\). For the fixed finite terminal list, (1.4) with \(m=0\) and (1.5) with \(m=0,1\) show that both covariance matrices are Lipschitz in \(\nu\) on the stated interval.

Here is the estimate behind this assertion. Covariance differences at time zero are bounded by a constant times \(F_0\max_a\|f_a^\nu(0)-f_a^{\nu'}(0)\|_\infty\). In a dynamical integrand, insert and subtract the product with one common density and one common pair of gradients:

\[
 \begin{split}
 &\left|\mu_r^\nu(\nabla f_a^\nu\cdot\nabla f_b^\nu)
        -\mu_r^{\nu'}(\nabla f_a^{\nu'}\cdot\nabla f_b^{\nu'})\right|\\
 &\qquad\le dF_1^2\|\mu_r^\nu-\mu_r^{\nu'}\|_\infty
       +dF_1\big(\|f_a^\nu-f_a^{\nu'}\|_{C^1}
                 +\|f_b^\nu-f_b^{\nu'}\|_{C^1}\big).
 \end{split} \tag{6.4}
\]

Combine this with the Lipschitz prefactors and integrate over the fixed overlap interval. It gives explicitly a finite constant \(C\), determined by \(T,d,F_0,F_1,C_{\mu,0},C_{f,0},C_{f,1}\), such that

\[
 \max_{a,b}\big\{|I^{ab}(\nu)-I^{ab}(\nu')|
                  +|D^{ab}(\nu)-D^{ab}(\nu')|\big\}
 \le C|\nu-\nu'|. \tag{6.5}
\]

The matrices \(I_N,D_N\) in the sealed TASK-014 theorem are exactly \(I(1/\beta_N),D(1/\beta_N)\): in this fixed-smooth model their only particle-number dependence in the deterministic PDEs is through temperature. Consequently that theorem's covariance hypothesis is now established, rather than assumed, for the following physical-temperature limits, provided its existing pair/residual assumptions hold along the sequence.

### Finite positive limiting inverse temperature

If \(\beta_N\to\beta_*\in(0,\infty)\), set \(\nu_*=1/\beta_*\). The smooth references and the full backward kernels converge in the norms above to their unique \(\nu_*\) solutions, and

\[
 \big(\sigma_N\rho_{t_a}^N(\phi_a)\big)_{a=1}^m
 \Longrightarrow \mathcal N_m(0,I(\nu_*)+D(\nu_*)).
 \tag{6.6}
\]

Equivalently, (6.2) has prefactor \(\min(\beta_*,1)\), and (6.3) has prefactor \(2\min(1,\beta_*^{-1})\). The response term remains inside every limiting backward kernel. Degenerate covariance is allowed.

### Diverging inverse temperature

If \(\beta_N\to\infty\), then \(\nu_N\to0\), and the limiting kernels are the constructed inviscid full backward kernels. Therefore

\[
 I_N^{ab}\longrightarrow
   \operatorname{Cov}_{\mu_0}(f_a^0(0),f_b^0(0)),
 \qquad D_N\longrightarrow0. \tag{6.7}
\]

This closes the specific identification left conditional in TASK-014: the limiting Gaussian vector consists of the iid initial fluctuation tested against \(f_a^0(0)\), and its limiting dynamical noise is zero. The actual leading martingale already has second moment \(O(1/\beta_N)\) under the frozen bounds; this report additionally proves which deterministic initial kernels occur.

### Vanishing inverse temperature and subsequences

If \(\beta_N\to0\), the separate general endpoint argument in the sealed TASK-014 report applies: the full backward energy identity bounds the time-integrated gradient square by \(C\beta_N\), both covariance matrices tend to zero, and the scaled vector tends to zero. The independent actual-law moment bound even gives convergence in \(L^2\). This endpoint is not obtained by using (6.5) at an infinite diffusivity.

Every positive temperature sequence has subsequences converging in the extended interval \([0,\infty]\), for example by compactness after the map \(\beta\mapsto\beta/(1+\beta)\). The three statements above identify each such fixed-smooth finite-dimensional subsequential limit. An oscillating temperature sequence is not thereby assigned a unique limit: different accumulation points can give different covariances, as the free example in TASK-014 shows. If distinct accumulation points happen to produce the same covariance, uniqueness may still occur; no converse is claimed.

### Relation to the campaign's critical label

For \(0<s<d\), a sequence \(\beta_N\sim\lambda N^{1-s/d}\) with \(\lambda>0\) tends to infinity. Applied to one **fixed smooth** interaction, (6.7) therefore identifies its diagnostic limit as the iid Gaussian propagated by the inviscid full backward kernels. This is not the singular critical Riesz law. A cutoff-dependent kernel does not have the uniform fixed norms appearing in (3.4)–(5.5), and no joint particle/cutoff passage has been proved. The full subcritical and singular critical gates, critical diagram classification, and logarithmic normalization remain unchanged and open.

## 7. Exact tests and the derivative loss

### Free heat, including zero diffusivity

When \(K=b=0\),

\[
 \mu_t^\nu=e^{\nu t\Delta}\mu_0,\qquad
 f_a^\nu(t)=e^{\nu(t_a-t)\Delta}\phi_a.
 \tag{7.1}
\]

The heat semigroup contracts the supremum norm of each differentiated function. Integrating its derivative with respect to \(\nu\) gives the exact sufficient comparisons

\[
 \sup_{t\le T}\|\mu_t^\nu-\mu_t^{\nu'}\|_{C^m}
 \le dT\|\mu_0\|_{C^{m+2}}|\nu-\nu'|, \tag{7.2}
\]

\[
 \sup_{t\le t_a}\|f_a^\nu(t)-f_a^{\nu'}(t)\|_{C^m}
 \le dT\|\phi_a\|_{C^{m+2}}|\nu-\nu'|. \tag{7.3}
\]

These formulas hold when either parameter is zero. They independently test the sign and order of the Laplacian forcing, the two-derivative loss, and the absence of inverse diffusivity. Substituting the Fourier amplitudes \(e^{-4\pi^2|k|^2\nu(t_a-t)}\) recovers the zero/equal/unequal terminal-time covariances in TASK-014.

The derivative requirement is substantive for an estimate uniform over data classes. In dimension one let \(\phi_n=n^{-m}\cos(2\pi n x)\), whose \(C^m\) norms are uniformly bounded. Compare \(\nu_n=n^{-2}\) with zero over a fixed positive terminal-time separation \(h\). The \(m\)-th derivative of the solution difference has a fixed nonzero supremum proportional to \(1-e^{-4\pi^2h}\), while \(|\nu_n-0|\to0\). Thus no uniform estimate of the form \(C|\nu-\nu'|\) depending only on the \(C^m\) norm of the terminal data is possible. This varying-data test does not contradict the fixed smooth theorem; it shows why the displayed extra regularity cannot simply be omitted.

### Nonzero signed one-mode interaction and full response

Take \(d=1\), \(b=0\), \(g(x)=a\cos(qx)\), \(q=2\pi\), and \(a\ne0\). Then \(K=aq\sin(qx)\). For \(\mu_0=1\), the exact reference is \(\mu_t^\nu=1\) for every \(\nu\ge0\). The full response on the first cosine mode is

\[
 R_\mu\cos(qx)=-\frac{aq^2}{2}\cos(qx).
 \tag{7.4}
\]

For a cosine terminal test at \(t_a\), the actual backward kernel is

\[
 f_a^\nu(t,x)
 =e^{-q^2(\nu+a/2)(t_a-t)}\cos(qx).
 \tag{7.5}
\]

The sign and the factor \(a/2\) agree with the independent TASK-011 source calculation. Omitting the response would remove this term and give the wrong parameter limit. Differentiating (7.5) in \(\nu\) proves the explicit uniform bound

\[
 \sup_{t\le t_a}\|f_a^\nu(t)-f_a^{\nu'}(t)\|_{C^m}
 \le Tq^{m+2}e^{|a|q^2T/2}|\nu-\nu'|. \tag{7.6}
\]

Both interaction signs are allowed. For \(a<0\) a mode may grow, but the finite-horizon exponential is explicit and independent of a lower diffusivity bound.

For two cosine terminal times, write \(\gamma=q^2(\nu+a/2)\). The covariance entries are exactly

\[
 I^{ab}(\nu)=\frac{\vartheta(\nu)}2e^{-\gamma(t_a+t_b)},
 \qquad
 D^{ab}(\nu)=\chi(\nu)q^2
       \int_0^{t_a\wedge t_b}e^{-\gamma(t_a+t_b-2r)}\,dr.
 \tag{7.7}
\]

If \(2\nu+a\ne0\), the latter equals

\[
 \frac{\chi(\nu)}{2\nu+a}
 \{e^{-\gamma|t_a-t_b|}-e^{-\gamma(t_a+t_b)}\}.
 \tag{7.8}
\]

At the possible signed-interaction resonance \(2\nu+a=0\), the integral in (7.7) gives
\(D^{ab}(\nu)=\chi(\nu)q^2(t_a\wedge t_b)\). Thus the apparent denominator in (7.8) is removable, not a continuity failure. At zero diffusivity the noise term vanishes and

\[
 I^{ab}(0)=\frac12
       e^{-aq^2(t_a+t_b)/2}. \tag{7.9}
\]

Equations (7.5)–(7.9) verify the full-response inviscid covariance, both signs, zero/equal/different times, and the finite positive diffusivity comparison. They are exact analytic tests, not numerical simulations.

## 8. Verification and remaining boundaries

The proof uses only the frozen smooth equation definitions, an explicit characteristic fixed point, differentiation and Gronwall, the scalar maximum principle with its derivative commutators displayed, integration by parts on the torus, and a convergent Volterra series with factorial bounds. Positive-diffusivity smooth mean-field existence is exactly the existing model assumption; zero-diffusivity existence and uniqueness have been constructed here. No singular source theorem, zero-viscosity theorem, or positivity of a weighted interaction is imported.

The exact free heat tests and signed one-mode tests are derived twice where they diagnose a load-bearing issue: from the comparison equations and from their explicit semigroup/eigenmode formulas. The high-frequency example proves a failure of a stronger regularity-free continuity bound. No additional dependency or computation package is needed.

Executed checks: campaign integrity verification PASS; the existing 116 exact rational residual/source checks PASS; this new file's nonprinting-control-character and trailing-whitespace scans PASS; both earlier report hashes unchanged; working-tree whitespace check PASS. Commands were python3 scripts/verify_campaign.py, python3 VERIFICATION_CODE/round002_falsification_exact.py, a standard-library text scan, shasum -a 256 on the three reports, and git diff --check. No TeX source is changed or created by this task.

Independent review should recompute the density difference (4.1), the maximum-norm constants in (3.4) and (4.4), the response integration by parts (3.5), the separate direct response-difference estimate (5.3), and the covariance comparison (6.4). This constructor can assign only SELF_CHECKED status.

The resulting advance is limited and explicit: the fixed-smooth covariance criterion now has identified covariance limits for every finite positive or infinite limiting inverse temperature, with the already proved degenerate zero-inverse-temperature limit retained. The particle fluctuation conclusion still uses the sealed residual/Gaussian proofs and the assigned pair bounds. No field tightness, uniformity over growing terminal lists, singular cutoff removal, singular critical law, corrector-order tail estimate, or whole-M3 completion follows. Root alone assigns canonical identifiers and integrates state records. No canonical edit, commit, push, installation, or publication was made.
