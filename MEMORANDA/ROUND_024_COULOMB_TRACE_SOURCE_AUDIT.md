# Round 024 — Coulomb spherical trace and the genuine lower contraction

TASK104. Issued 2026-09-18 UTC. **ORDINARY DISTINCT SOURCE/DERIVATION LANE; NEW DERIVATION SELF-CHECKED, NOT AN INDEPENDENT THEOREM AUDIT.**

The bounded lower-contraction question closes, using the supplied R5/R8 inverse/domain and R10 actual-law inputs in their admitted scopes. The genuine inverse has a canonical spherical-average trace. It need not be assigned a pointwise diagonal value. The exact punctured identity includes a common-translation derivative, twice the inward boundary flux, and the Haar compensation. Its scalar contraction is exactly zero for this genuine homogeneous source. The remaining centered one-body term vanishes after scaling, with the sufficient bound \(C\sqrt{b_N}N^{-1/4}\) below. This is a new consequence of the supplied bounds and translation covariance, not a quoted R12/R14 endpoint theorem.

**THM046 source cancellation remains OPEN.** Neither the cubic remainder nor the genuine corrector martingale is estimated here. The source assertion and its negation are not decided by a lower-contraction estimate.

## 1. Exact claim, negation, and input boundary

Use precisely the THM046 actual iid-Haar row: \(d=4,s=2\), unit Haar torus, \(K=-\nabla g\), \(\widehat g(k)=|k|^{-2}\) for \(k\ne0\), and \(\widehat g(0)=0\). Let \(0\le T<\infty\), \(h\) be real and smooth, and
\[
 \beta_N>0,\quad \nu_N=\beta_N^{-1},\quad
 \lambda_N=\beta_NN^{-1/2}\longrightarrow\lambda\in(0,\infty),
 \quad b_N=\min(\beta_N,1),\quad \sigma_N=\sqrt{Nb_N}.
 \tag{1}
\]
For each \(N\), \(\Phi_t[h]\) is the supplied full symmetric terminal-zero inverse with both compensated responses and source \(J^{Q_{T-t}^{\nu_N}h}\). Put
\[
 B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi,\qquad
 g_{\Phi,t}(x)=\int B\Phi_t(x,y)\,dy,\qquad
 c_{\Phi,t}=\int g_{\Phi,t}(x)\,dx,
\]
\[
 \ell_N(t)=N^{-1}\rho_t[g_{\Phi,t}]+(2N)^{-1}c_{\Phi,t},
 \qquad \rho_t=N^{-1}\sum_i\delta_{X_i(t)}-dx.
 \tag{2}
\]
These are the genuine R8 contractions, with its continuous slice representative; no diagonal substitution or replacement inverse is used.

The primary bounded assertion here is the conjunction of the punctured identity (12), the canonical spherical trace and limiting identity (15), \(c_{\Phi,t}=0\), and
\[
 \sigma_N\,\mathbb E\int_0^T|\ell_N(t)|\,dt
 \le C\sqrt{b_N}\,N^{-1/4}
 \quad\hbox{for the tail of every sequence in (1).}
 \tag{3}
\]
The constant is independent of \(N\), depending on the fixed kernel/chart, \(T,h\), and an eventual fixed upper bound for \(\nu_N\). Such a bound exists because \(\nu_N\to0\); it therefore has the allowed dependence in THM046. The exact negation is an admitted tuple violating a stated identity/trace or for which no such uniform constant exists. A generic symmetric kernel with nonzero scalar, an angular diagnostic with no pointwise trace, or an arbitrary exchangeable law is not this negation.

All twenty inputs in AUDITS/ROUND_024_COULOMB_TRACE_AUDIT_INPUT_SHA256SUMS.txt were verified before mathematical use; HEAD equals 4ab1d492c3bb9bb3537732f2d75502971f5ee6da. The task and manifest were the first files read. The full relevant R4/R5/R7/R8/R10/R11 proofs were read, including portions initially truncated by tool output and subsequently reread. R12/R14 were read to retain their strict scopes, not imported at Coulomb. R16 was inspected only for its source/normalization/scope boundary. No current constructor/falsifier narrative, R23 output, canonical state/history, other worktree, memory file, prior checker, or external source was read.

The immutable source files contain historical candidate/conditional/self-check labels. The task admits the corresponding source results; this report checks their content and composes them but does not determine a later audit status from unseen ledgers. No source is independently recertified here. References inside supplied proofs to non-allowlisted reports were not followed.

## 2. Source and normalization preflight

The companion SOURCE_INDEX.md gives exact paths, line ranges, uses and exclusions. The load-bearing content is:

* R4, lines 69–109 and 111–196: coefficient-one local expansion and exact periodic divergence.
* R5 base, lines 121–171 and 305–374: absolute source-potential bound, including its supremum of order \(N^{1/2}\) here. R5 conditional inverse, lines 23–39: bounded two-response Volterra series. R5 homogeneous interface, lines 33–57: actual Fourier test and regularity.
* R8, lines 527–580: \(B\Phi\) is integrable by the classical pair equation, with uniform slice tails at each fixed \(N\). Lines 685–721 fix both lower coefficients and exclude an additional deleted-label thermal trace.
* R10, lines 76–223: actual singular expected-energy and empirical Fourier bounds; lines 302–311 give the compatible common-translation principle. The stronger sup-norm form needed below is proved directly from R5.

Write
\[
 \gamma=4\pi^2=2|\mathbb S^3|,\qquad
 D=\operatorname{div}K=\gamma(\delta_0-dz).
 \tag{4}
\]
Thus \(\operatorname{div}_{\rm cl}K=-\gamma\) off zero. On an embedded ball,
\[
 g(z)=|z|^{-2}+H(z),\quad
 K(z)=2z|z|^{-4}+k(z),\quad k=-\nabla H,\quad
 k(0)=0,\quad |k(z)|\le L_k|z|.
 \tag{5}
\]
The Fourier coefficient one is essential: \(4\pi^2|k|^2\widehat g(k)=4\pi^2\) on every nonzero mode. The compensation is the constant \(-\gamma\), not an unspecified remainder with that mass.

At Haar background,
\[
 R_xv=-\gamma v+\gamma\int v(z,y)\,dz,\qquad
 R_yv=-\gamma v+\gamma\int v(x,z)\,dz.
 \tag{6}
\]
Each has sup-norm bound \(2\gamma\); \(C_R=4\gamma\) suffices for their sum. The atom in (6) multiplies the current pair value; it does not set \(x=y\). R4 explicitly excludes the diagonal-trace inference.

The backward test is
\[
 f_t=\bar h+e^{-\gamma(T-t)}e^{\nu(T-t)\Delta}(h-\bar h).
 \tag{7}
\]
Positivity and unit mass of the torus heat kernel bound each positive-order derivative by the corresponding derivative norm of \(h\), uniformly for \(\nu\ge0\). There is no inverse-\(\nu\) loss. At finite positive \(\nu\) all imported fixed-\(N\) domain assertions apply. Their constants also apply uniformly over a fixed interval \(0\le\nu\le\nu_*\) at fixed \(N\). No elliptic diagonal regularity is presumed.

## 3. Quantitative common-translation bounds from the full source

Use fixed R5 radii \(0<R_0<R_1<R_2<1/3\) and a smooth cutoff \(\chi\), equal to one on \(B_{R_0}\), zero off \(B_{R_1}\). Set
\[
 K_{\rm out}=\sup_{\operatorname{dist}(z,0)\ge R_0}|K(z)|,\quad
 C_1=\|\nabla\chi\|_\infty,\quad C_2=\|\Delta\chi\|_\infty,
\]
\[
 \alpha=1+2L_k,\quad V_*=2R_0^{-3}+L_kR_1,\quad
 E_*=2R_0^{-2}(2\nu_*C_2+V_*C_1)+16\nu_*C_1R_0^{-3}.
\]
Here \(L_k=\sup_{B_{R_1}}\|Dk\|_{\rm op}\). For a smooth real test \(a\), put \(H_a=\|D^2a\|_\infty\), \(G_a=\|\nabla a\|_\infty\), and
\[
 C_B(a)=H_aL_kR_0^2+2G_aK_{\rm out}+H_aE_*/\alpha,\qquad
 M(a)=e^{(\alpha+4\gamma)T}\{H_a\sqrt T+C_B(a)T\}.
 \tag{8}
\]
These are continuous seminorms with no \(N\) dependence; set \(M=0\) at \(T=0\). R5's profile has \(p=4\), \(2sp=16\), and \(\sqrt{16}/4=1\). Its base supremum is at most \(e^{\alpha T}\{H_a\sqrt N\sqrt T+C_B(a)T\}\). The full Volterra series multiplies this by at most \(e^{4\gamma T}\). Hence
\[
 \sup_{t,(x,y)\in E}|\Phi_t[a](x,y)|\le\sqrt N\,M(a),
 \qquad E=\{x\ne y\}.
 \tag{9}
\]
This is the genuine inverse with both responses, uniformly for \(0\le\nu\le\nu_*\). It is not an \(N\)-uniform bound without the displayed \(\sqrt N\).

Let \(a_v(x)=a(x+v)\), \(\mathcal D_j=\partial_{x_j}+\partial_{y_j}\). The pair process, both responses and (7) commute with common translations. Uniqueness of the full inverse gives pointwise on \(E\)
\[
 \Phi_t[a](x+v,y+v)=\Phi_t[a_v](x,y).
 \tag{10}
\]
The map \(a\mapsto\Phi[a]\) is linear and continuous from (8) to the bounded sup norm by (9). Difference quotients of a smooth input converge in that seminorm. Thus, for every multi-index \(\zeta\),
\[
 \mathcal D^\zeta\Phi_t[a]=\Phi_t[\partial^\zeta a],\qquad
 \|\mathcal D^\zeta\Phi[a]\|_\infty
 \le\sqrt N\,M(\partial^\zeta a).
 \tag{11}
\]
First derivatives coincide with R8's actual off-diagonal derivatives; iteration gives higher common derivatives. No full normal derivative is claimed bounded. Averaging (10) over translations, justified by the bounded linear map, yields
\[
 \int_{\mathbb T^4}\Phi_t[a](x,x-z)\,dx=0\qquad(z\ne0),
\]
since the average input is constant and its source and inverse vanish. This is an off-diagonal statement for each nonzero relative coordinate.

## 4. The exact punctured identity

Set \(F_t(x,z)=\Phi_t(x,x-z)\). For \(0<\varepsilon<R_0\), let \(\Omega_\varepsilon=\mathbb T^4\setminus\overline{B_\varepsilon}\) in the relative variable, and define
\[
 q_\varepsilon(x)=\int_{\Omega_\varepsilon}F(x,z)\,dz,\quad
 A_\varepsilon(x)=\int_{\Omega_\varepsilon}K(z)F(x,z)\,dz,\quad
 g_\varepsilon(x)=\int_{\Omega_\varepsilon}B\Phi(x,x-z)\,dz.
\]
Suppress time and input. Exact differentiation gives
\[
 \nabla_xF=(\nabla_x+\nabla_y)\Phi(x,x-z),\quad
 \nabla_zF=-\nabla_y\Phi(x,x-z),\quad
 (\nabla_x-\nabla_y)\Phi=\nabla_xF+2\nabla_zF.
\]
The common-translation derivative is the first term, and the factor two is the relative-coordinate term. The \(z\) domain is independent of \(x\); no moving-boundary derivative is discarded. Periodicity cancels the outer faces of a torus fundamental cell. The outward normal of the punctured domain on its inner sphere is \(-\theta\). Thus ordinary integration by parts gives
\[
 \boxed{
 g_\varepsilon=\operatorname{div}_x A_\varepsilon+2\gamma q_\varepsilon
 -2\varepsilon^3\int_{\mathbb S^3}
 K(\varepsilon\theta)\cdot\theta F(x,\varepsilon\theta)\,dS(\theta).}
 \tag{12}
\]
The inner flux is negative, and the bulk term is \(-2\int(-\gamma)F=+2\gamma q_\varepsilon\).

Define
\[
 \tau_\varepsilon(x)=|\mathbb S^3|^{-1}
       \int_{\mathbb S^3}F(x,\varepsilon\theta)\,dS(\theta),\quad
 e_\varepsilon(x)=\varepsilon^3\int_{\mathbb S^3}
       k(\varepsilon\theta)\cdot\theta F(x,\varepsilon\theta)\,dS(\theta).
\]
Then
\[
 \varepsilon^3\int K(\varepsilon\theta)\cdot\theta F\,dS
 =\gamma\tau_\varepsilon+e_\varepsilon,\qquad
 |e_\varepsilon|\le L_k|\mathbb S^3|\varepsilon^4\|\Phi\|_\infty.
 \tag{13}
\]
The smooth flux is retained until this bound proves it vanishes. Evenness gives \(k(0)=0\) and the power four.

## 5. The trace actually justified by the sources

R8 permits \(q_1=3/2,q_2=3\) in this dimension. Its classical equation gives, at fixed \(N\), uniformly in \(t\) and in a fixed bounded diffusivity interval,
\[
 B\Phi=-N(J+\partial_t\Phi+\nu\Delta_{x,y}\Phi+R\Phi),\qquad
 |B\Phi|\le C_N(w_2+w_3+1).
 \tag{14}
\]
Consequently \(g_\varepsilon\to g_\Phi\) uniformly in \(t,x\). The omitted slice is bounded by \(C_N(\varepsilon^2+\varepsilon+\varepsilon^4)\). This is the structural directional-drift estimate; the nonintegrable product majorant \(|K||\nabla\Phi|\) is not used.

Also \(q_\varepsilon\to q=\int F\,dz\) uniformly. Equations (9)–(11) and \(K\in L^1\) justify
\[
 A=\int K(z)F(x,z)\,dz,\qquad
 \operatorname{div}_x A=\int K(z)\cdot\mathcal D\Phi(x,x-z)\,dz.
\]
The vector field \(A\) is continuously differentiable in \(x\), and \(\operatorname{div}A_\varepsilon\to\operatorname{div}A\) uniformly; the omitted force mass is \(O(\varepsilon)\). With (13), equation (12) proves a uniform, not merely subsequential, limit \(\tau_\Phi=\lim_{\varepsilon\downarrow0}\tau_\varepsilon\) at each fixed \(N\):
\[
 \boxed{
 \tau_\Phi(t,x)=\lim_{\varepsilon\downarrow0}|\mathbb S^3|^{-1}
 \int_{\mathbb S^3}\Phi_t(x,x-\varepsilon\theta)\,dS(\theta),\qquad
 g_\Phi=\operatorname{div}A+2\gamma(q-\tau_\Phi).}
 \tag{15}
\]
It is continuous in \(t,x\), with \(\|\tau_\Phi[a]\|_\infty\le\sqrt N M(a)\). The preliminary convergence is also uniform over the bounded diffusivity interval at fixed \(N\), but its rate contains \(C_N\). No uniform shrinking-tube rate in \(N\) is claimed or used.

This is a canonical averaged trace of the off-diagonal representative. Arbitrary values on \(x=y\) are irrelevant. No direction-independent pointwise diagonal limit is inferred from Sobolev regularity or the atom. The same argument works for every smooth input. The linear trace map is bounded by (9), and translation covariance survives the limit. Input difference quotients therefore give
\[
 \partial^\zeta\tau_\Phi[a]=\tau_\Phi[\partial^\zeta a],\qquad
 \|\partial^\zeta\tau_\Phi[a]\|_\infty
 \le\sqrt N M(\partial^\zeta a).
 \tag{16}
\]
Thus the trace is smooth in its one-body variable, with polynomial \(N\) bounds. No interchange of the \(\varepsilon\) and \(N\) limits occurred.

Integrating (15) gives the exact general scalar identity
\[
 c_\Phi=2\gamma\left(\iint\Phi-\int\tau_\Phi\right).
 \tag{17}
\]
For this genuine source, Section 3 gives zero common-translation average at every nonzero relative coordinate. Hence \(\iint\Phi=0\), \(\int\tau_\varepsilon=0\) at each positive radius, and \(\int\tau_\Phi=0\) by the uniform limit. Therefore
\[
 \boxed{c_{\Phi,t}=0\quad\hbox{for every admitted }t,N,\nu.}
 \tag{18}
\]
A general symmetric relative kernel has a nonzero scalar in (17); the diagnostic below checks that distinction.

## 6. Uniform one-body regularity and actual-law smallness

Define the explicit continuous seminorm
\[
 \mathcal G(a)=\|K\|_1\sum_{j=1}^4M(\partial_j a)+4\gamma M(a).
 \tag{19}
\]
Equations (9), (11) and (15) imply
\[
 \|g_{\Phi[a]}\|_\infty\le\sqrt N\,\mathcal G(a).
 \tag{20}
\]
The contraction is linear and covariant under translation of the input and the remaining coordinate. Difference quotients of the input converge in (19), so directly in uniform norm
\[
 \partial^\zeta g_{\Phi[a]}=g_{\Phi[\partial^\zeta a]},\qquad
 \|\partial^\zeta g_{\Phi[a]}\|_\infty
 \le\sqrt N\,\mathcal G(\partial^\zeta a).
 \tag{21}
\]
This avoids differentiating an unproved singular product. Six derivatives suffice. Using \(\widehat g_\Phi(k)=\int g_\Phi(x)e^{-2\pi i k\cdot x}\,dx\),
\[
 |\widehat g_\Phi(t,k)|\le
 \frac{\sqrt N\,\mathcal G((1-\Delta)^3h)}{(1+4\pi^2|k|^2)^3},\qquad
 \sum_{k\ne0}|k|\,|\widehat g_\Phi(t,k)|
 \le\sqrt N\,C_{\rm lat}\mathcal G((1-\Delta)^3h),
 \tag{22}
\]
where \(C_{\rm lat}=\sum_{k\in\mathbb Z^4\setminus\{0\}}|k|(1+4\pi^2|k|^2)^{-3}<\infty\). The summand has order \(|k|^{-5}\) in dimension four. Bounds are uniform in time and the bounded diffusivity interval.

R10's actual-law estimate specializes to
\[
 \mathbb E|\widehat\eta_N(t,k)|^2
 \le\min\{1,C_E N^{-1/2}|k|^2\},\qquad k\ne0,
 \tag{23}
\]
with \(C_E\) independent of \(N,\nu,t\). Its source proof uses smooth heat dynamics first: nonincreasing free energy and zero initial energy give \(\mathbb EH_N^\varepsilon\le0\); fixed-\(N\) same-noise convergence and the common lower bound give \(\mathbb EH_N\le0\) by Fatou. The positive heat-integral split retains the exact self subtraction \(g^{>r}(0)/2\) and background error \((N-1)Ar^\alpha/(2\alpha)\). At \(d=4,s=2,r=N^{-1/2}\) both errors are \(O(\sqrt N)\). Retained Fourier weights dominate a fixed multiple of \(|k|^{-2}\) for \(|k|\le N^{1/4}\); use \(|\widehat\eta_N|\le1\) above that scale. These are precisely R10 (3.5)–(3.7), with its singular passage and self term retained.

Absolute Fourier convergence, (23) and Cauchy–Schwarz in the actual probability space give
\[
 \mathbb E|\rho_t[g_{\Phi,t}]|
 \le\sum_{k\ne0}|\widehat g_\Phi(t,k)|
        \big(\mathbb E|\widehat\eta_N(t,-k)|^2\big)^{1/2}
 \le C_E^{1/2}C_{\rm lat}\mathcal G((1-\Delta)^3h)\,N^{1/4}.
 \tag{24}
\]
No positive-time product law or label independence is used. The contraction is deterministic; the entire empirical measure is controlled by its actual Fourier moments.

By (18), the scalar in (2) is exactly zero. Multiply (24) by \(\sigma_N/N=\sqrt{b_N/N}\), and integrate. This proves (3) with the sufficient constant
\[
 C=T C_E^{1/2}C_{\rm lat}\mathcal G((1-\Delta)^3h).
 \tag{25}
\]
Tonelli applies to the nonnegative integrand. This stronger expected absolute time-integral bound also controls the expectation of the absolute signed integral and the expected supremum of its time primitive.

The critical sequence has \(\nu_N=N^{-1/2}/\lambda_N\), so the bounded interval used in (8) is available. R11 also applies because \(\nu_N\sqrt N=\lambda_N^{-1}\) is bounded, but its weighted gradient is not needed in (24). No strict R12/R14 estimate was extended to Coulomb. For \(T=0\) or constant \(h\), the genuine source, inverse and contraction vanish.

## 7. False inferences and the exact remaining gate

The assertion that Sobolev regularity supplies a pointwise pair-diagonal value is false. Let a smooth radial cutoff equal one near zero, and set
\[
 V(x,y)=\chi(x-y)\left(\frac{(x_1-y_1)^2}{|x-y|^2}-\frac14\right)
 \quad(x\ne y).
 \tag{26}
\]
This is symmetric, bounded and smooth off diagonal, with derivatives of sizes \(O(r^{-1})\) and \(O(r^{-2})\). In four relative dimensions it belongs to \(H^1\cap W^{2,1}\) and satisfies the corresponding R7/R8 power upper bounds. Its principal radial force derivative vanishes near zero; the smooth force remainder contributes an integrable bounded term. Its spherical average is zero, whereas its limits along \(e_1\) and \(e_2\) are \(3/4\) and \(-1/4\). Assigned diagonal values change neither weak derivatives nor this trace. This refutes a regularity implication, not the genuine-source theorem.

R11's \(r^{-2}\) value and \(r^{-3}\) gradient bounds, or its \(W^{1,1}\) convergence, alone do not imply a diagonal trace or integrability of \(|K||\nabla\Phi|\). R7 explicitly exhibits that Coulomb product-majorant failure. R8 instead obtains the contracted directional drift from its equation at fixed \(N\). Section 5 uses precisely that estimate and the additional bounded common derivatives.

The naive pathwise estimate \(\|g_\Phi\|_\infty=O(\sqrt N)\) is only \(O(1)\) after scaling. It is not vanishing. The exact scalar cancellation and actual-law Fourier concentration are the extra load-bearing lines of the proof, and neither follows from renaming a signed expectation as concentration.

A sufficient substitute if (22) were unavailable would be the explicit criterion
\[
 \int_0^T\sum_{k\ne0}|k|\,
 \left|\widehat{\operatorname{div}A+2\gamma(q-\tau_\Phi)}(t,k)\right|dt
       =o(N^{3/4}),\qquad
 N^{-1/2}\int_0^T|c_{\Phi,t}|dt=o(1),
 \tag{27}
\]
together with (23) and the finite-\(N\) trace identity. This is sufficient for the stronger lower-drift norm here, not claimed necessary. In the present row (22) is \(O(\sqrt N)\) and (18) is exact, so no unproved analytic line remains in this bounded lower-contraction consequence of the admitted sources.

The first unresolved line for deciding THM046 through the full R8 identity remains control of the other actual terms. Integration with \(\Phi_T=0\) gives
\[
 \int_0^T P_N[J_t]\,dt
 =P_N[\Phi_0]+\int_0^T U_{3,t}[C\Phi_t]\,dt
       +\int_0^T\ell_N(t)\,dt+M_T^2.
 \tag{28}
\]
This report proves smallness only of the third term after scaling. It makes no new estimate on the combined cubic and martingale terms, does not remove a possible cancellation between them, and does not infer source cancellation. R16 remains only an \(O(1)\) scaled source bound at the threshold.

## 8. Fresh diagnostics and adversarial self-check

The newly written exact_diagnostic.py uses standard-library rational arithmetic and no earlier checker. For a smooth finite Fourier pair polynomial in four coordinates, it forms the direct contraction using the actual singular Coulomb Fourier coefficient. A pair mode \((a,b)\) contributes zero to \(g_\Phi/\gamma\) when \(b=0\), and otherwise contributes
\[
 \frac{b\cdot(a-b)}{|b|^2}\,e_{a+b}(x).
 \tag{29}
\]
The separately formed common-translation term is \(b\cdot(a+b)/|b|^2\); the row and trace contributions give (15). The test uses genuine Coulomb action on a smooth finite polynomial, not an approximate genuine inverse.

A second calculation integrates radial tests \(r^m\) in a Euclidean annulus for the field \(2z|z|^{-4}-(\gamma/4)z\). It compares the direct \(2K\cdot\nabla r^m\) integral with both finite-radius boundary fluxes and the compensation, as exact polynomials in \(\gamma\) after division by \(|\mathbb S^3|\). This is a local normalization diagnostic, not a periodic substitute.

Detecting mutations include omitted common derivative, reversed inner flux, dropped Haar compensation, halved relative factor, reversed common-derivative sign, arbitrary diagonal substitution, false zero scalar for every symmetric kernel, and wrong inner annulus normal. The executed suite passed 2,030 exact assertions across 96 finite Fourier cases and 20 annular cases; all eight mutations were detected. A separate safe-verifier suite passed one positive archive and rejected all thirteen malformed-byte/member/manifest cases in memory, without extraction.

| Vulnerable inference | Resolution |
|---|---|
| Response atom read as a pair trace | The trace is independently constructed from (12)–(14). |
| Moving puncture loses a derivative | Fixed relative coordinates retain \(\mathcal D\Phi+2\nabla_zF\). |
| Wrong boundary sign or compensation | Inner normal \(-\theta\), punctured divergence \(-\gamma\), smooth flux retained. |
| Fixed-\(N\) bounds relabelled uniform | \(C_N\) is used only for the trace limit; uniform powers come from (9)–(11). |
| Differentiating the trace needs a hidden limit interchange | The bounded linear trace map and input difference quotients prove (16). |
| Scalar dropped by convention | General value (17); source-specific cancellation (18). |
| Evolved iid law assumed | Only actual Fourier estimate (23) enters (24). |
| Sup bound incorrectly called small | The extra \(N^{-1/4}\) comes from actual concentration. |
| Strict sub-Coulomb theorem imported | No R12/R14 lemma is used. |
| Lower-term result mistaken for source cancellation | Other terms of (28) remain uncontrolled here. |

This is same-context adversarial checking and supporting computation, not isolated certification. Root must decide whether a fresh theorem audit is needed before promotion.

## 9. Recoverable issuance

Only this report, ROUND_024_COULOMB_TRACE_AUDIT_ARTIFACTS/, and its sibling archive/seal are written. The directory contains exact copies of all twenty inputs and the assigned manifest, source/exposure records, fresh diagnostic/results, a safe byte/member verifier, verification record, README and bundle manifest. The archive contains exactly the manifested files plus the manifest. Its sibling seal anchors archive and manifest hashes.

No canonical state, source, theorem card, earlier report, other worktree, commit, branch, remote or dependency was changed. Pre-existing untracked task/theorem/manifest inputs were preserved. No TeX was created or modified; the final handoff uses nonmathematical prose and links this Markdown report. Issued outputs and archive are made read-only after byte/member verification. Any later repair must be a separately named superseding artifact.
