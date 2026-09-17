# Round 004: a bounded martingale realization of the diffusion-retaining local pair model

2026-09-17 UTC. TASK-032. Constructor: `/root/r003_fresh_sharp`.
Worktree: `/private/tmp/hocf-r004-diffusive-20260917`.
Branch: `codex/hocf-r004-diffusive`.
Base commit: `2f532ccd2cb5f3d84db456be96e438f03f7e2ad2`.

**Mathematical status: PROVED_CANDIDATE / SELF_CHECKED.** The local diffusion-retaining problem below has a uniquely defined bounded probabilistic solution in an explicit martingale class, with the proposed radial upper bound for every nonnegative finite diffusivity. The construction includes collision avoidance, nonexplosion, source integrability, measurable transition kernels, deterministic-time Markov conditioning, uniqueness, and annular exhaustion. No classical regularity of the constructed potential is asserted. A separate classical annular comparison is proved conditionally for any solution with the stated regularity. The resulting periodic cutoff kernel has the initial iid endpoint bound below, uniformly in diffusivity.

Root supplied the radial-superharmonic and Lyapunov/Picard ideas as seeds. This worker checked and completed them; the report is a construction, not independent certification of that proposal. The previously issued fresh Round 003 reconstruction remains unchanged. The full response operator, the evolved interacting law, and the singular fluctuation mission remain open.

## 1. Exact model, assertion, and source preflight

Fix an integer \(d\ge3\), a real exponent \(0<s\le d-2\), \(p=s+2\), an integer \(N\ge2\), a finite \(\nu\ge0\), a finite \(T\ge0\), and a fixed real symmetric \(d\times d\) matrix \(A\). Set \(D=\mathbb R^d\setminus\{0\}\), and for \(z=r\theta\in D\) define

\[
 v_N(z)=\frac{2s}{N}r^{-s-2}z,\qquad
 L=2\nu\Delta+v_N\cdot\nabla,\qquad
 j_0(z)=sr^{-s},\qquad J_A(z)=sr^{-s}\theta^TA\theta.
 \tag{D1}
\]

The backward local equation being realized is

\[
 (\partial_t+L)\Phi=-J_A,\qquad \Phi(T,z)=0\quad(z\in D).
 \tag{D2}
\]

Write \(K=\|A\|_{\mathrm{op}}\), so \(|J_A|\le K j_0\). This model has only relative diffusion, the singular internal pair transport, and the static quadratic-test source. Its coefficients are declared directly. The factor \(2\nu\) corresponds to noise amplitude \(\sqrt{4\nu}\); the relative internal drift is \(2s/N\), without an absorbed factor two. The positive-power normalization and source sign match the frozen model and THM-017. No logarithmic convention or further Riesz Fourier theorem is used.

The profile imported as an explicit formula from THM-017, and differentiated again here, is

\[
 F_{N,\tau}(r)=\frac N4
 \left[\left(r^p+\frac{2sp\tau}{N}\right)^{2/p}-r^2\right],
 \qquad r>0,\quad 0\le\tau\le T.
 \tag{D3}
\]

The primary assertion is that the globally constructed bounded martingale solution, every constructed killed-annular martingale solution for \(\nu>0\), and every classical annular solution in the stated conditional class satisfy

\[
 |\Phi(t,z)|\le K F_{N,T-t}(|z|).
 \tag{D4}
\]

The multiplicative constant one is independent of \(N,\nu\) and the annular radii. The profile itself depends on \(N\); this is not an assertion of an absolute supremum norm uniform in \(N\). The exact negation is an admissible parameter tuple and a solution in one of these declared classes violating (D4), or failure of one of the existence, integrability, or uniqueness assertions explicitly included in the global construction. The proofs below exclude that negation on \(d\ge s+2\).

Read inputs were the governing instructions, TASK-032, the frozen Round 001 model, THM-015, THM-017 and its transport proof, the submitted diffusion rescaling and its erratum. The supplied six-file input manifest was checked before mathematical work. The reviewed erratum correctly distinguishes the subcritical diffusion classification when \(d\le s+2\); no solution limit is inferred from any rescaled coefficient. The present proof does not rely on a small-diffusivity assumption or on that classification. The reused context contains the worker's prior Round 003 iid reconstruction; it supplies no new input for the construction below. No external existence, boundary regularity, or probability-limit theorem is imported.

## 2. Radial superharmonicity and the backward sign

For \(\tau\ge0,r>0\), put

\[
 q=\frac{r^p}{r^p+2sp\tau/N},\qquad \gamma=\frac{s}{p}.
\]

At \(\tau=0\), \(q=1\); otherwise \(0<q<1\). Direct differentiation yields

\[
 \partial_\tau F=s(r^p+2sp\tau/N)^{-s/p},\quad
 \partial_rF=\frac N2r(q^\gamma-1),\quad
 r\partial_rq=pq(1-q),
\]

and therefore

\[
 -\partial_\tau F+\frac{2s}{N}r^{-s-1}\partial_rF=-sr^{-s},
 \tag{D5}
\]

\[
 \Delta F=\frac N2\left[q^{s/p}(d+s-sq)-d\right].
 \tag{D6}
\]

To check the sign rather than assume it, let \(H(q)=q^{s/p}(d+s-sq)\). Its derivative is

\[
 H'(q)=\frac{s}{p}q^{s/p-1}
       [d+s-(2s+2)q].
 \tag{D7}
\]

The bracket is nonnegative on \((0,1]\) because its minimum there is \(d-s-2\ge0\). It is strictly positive on \((0,1)\), including the case \(d=s+2\). Thus \(0<H(q)\le H(1)=d\), with strict inequality for \(q<1\), and

\[
 -\frac{Nd}{2}\le\Delta F\le0.
 \tag{D8}
\]

For \(W(t,z)=F_{N,T-t}(|z|)\), equations (D5)–(D8) give the exact supersolution identity and sign

\[
 (\partial_t+L)W=-j_0+2\nu\Delta F\le-j_0.
 \tag{D9}
\]

The profile is nonnegative, zero at \(t=T\), smooth on the punctured domain through that terminal time, and obeys

\[
 0\le F_{N,\tau}(r)
 \le\min\left\{\frac{(2sp)^{2/p}}4N^{s/p}\tau^{2/p},\;s\tau r^{-s}\right\}.
 \tag{D10}
\]

The first bound follows by concavity of the power \(2/p<1\), or by monotonicity in \(r\); the second follows by integrating the transport characteristic source. For \(T=0\) all asserted solution values are zero and no positive-time division is used.

## 3. Direct conditional classical comparison on an annulus

Let \(0<a<R<\infty\), \(D_{a,R}=\{a<|z|<R\}\), and \(\nu>0\). Suppose a real function \(\Phi\) is continuous on \([0,T]\times\overline{D_{a,R}}\), is \(C^{1,2}\) in the interior with derivatives adequate for (D2), solves (D2) there, and is zero on the lateral boundary and at \(t=T\). These are explicit assumptions in this paragraph; existence of a classical solution is not being imported.

Set \(u(\tau,z)=\Phi(T-\tau,z)\) and \(w= u-KF_{N,\tau}\). Then

\[
 (\partial_\tau-L)w
 =J_A-K(j_0-2\nu\Delta F)\le0.
\]

The initial and lateral values of \(w\) are nonpositive. For any \(\varepsilon>0\), \(w-\varepsilon\tau\) satisfies a strict differential inequality. A positive maximum on a finite cylinder cannot occur on the initial or spatial boundary. At an interior spatial maximum at a positive time, its spatial gradient is zero, its spatial Laplacian is nonpositive, and its time derivative from the preceding times is nonnegative. This contradicts the strict inequality. Hence \(w\le0\), by letting \(\varepsilon\downarrow0\). Applying the same argument to \(-u-KF\) proves (D4). All annular boundary values of \(KF\) are nonnegative; they need not be zero.

This establishes a direct parabolic comparison, with no missing time sign. Sections 4–7 construct solutions in a bounded martingale class and identify the annular-to-global passage without presuming classical regularity. No all-boundary annular transport condition is imposed when \(\nu=0\).

## 4. A measurable pathwise construction of the local diffusion

Fix a probability space carrying a standard \(d\)-dimensional Brownian motion \(B\), with its completed natural filtration. Only its independent increments, continuity and smooth stopped Itô formula are used. We construct

\[
 dZ_h=\sqrt{4\nu}\,dB_h+v_N(Z_h)\,dh,\qquad Z_0=z\in D.
 \tag{D11}
\]

This section supplies existence and the measurability needed later rather than citing an SDE existence theorem.

For an integer \(m\ge2\), choose a smooth radial cutoff equal to one on \([1/m,m]\), zero outside \((1/(2m),2m)\), and multiply \(v_N\) by it, extending the result by zero at the origin. The resulting \(v_m\) is globally bounded and globally Lipschitz; let bounds be \(B_m,L_m<\infty\). For any continuous path \(b\) beginning at zero, define Picard iterates

\[
 Z^{(0)}_h=z+\sqrt{4\nu}\,b_h,\qquad
 Z^{(k+1)}_h=z+\sqrt{4\nu}\,b_h+
       \int_0^h v_m(Z^{(k)}_u)\,du.
\]

On \([0,H]\), consecutive differences are bounded by
\(B_mL_m^kH^{k+1}/(k+1)!\). Their sum converges uniformly, giving a continuous solution of the cutoff integral equation. Iterating the Lipschitz integral inequality proves uniqueness: a difference bounded on \([0,H]\) is bounded by its own supremum times \(L_m^kH^k/k!\), which tends to zero. The same integral inequality gives continuous dependence on the initial point and driving path, with upper bound

\[
 \sup_{h\le H}|Z_h(z,b)-Z_h(z',b')|
 \le (|z-z'|+\sqrt{4\nu}\|b-b'\|_{\infty,[0,H]})e^{L_mH}.
 \tag{D12}
\]

Consequently the solution map is jointly Borel in \(z\) and the driving continuous path. Applied to Brownian motion it is adapted, because each Picard iterate at time \(h\) uses only the path up to \(h\).

For initial \(z\in D_m:=\{1/m<|z|<m\}\), stop the cutoff solution at its first exit \(\rho_m\) from \(D_m\). Two cutoffs whose domains contain \(D_m\) agree up to this exit: both integral equations there have the same locally Lipschitz drift, so the preceding uniqueness argument applies. Thus the stopped solutions consistently patch, their exit times increase as \(m\) increases, and they define a unique continuous maximal solution on \([0,\zeta)\), where \(\zeta=\lim_m\rho_m\). Exit times and stopped paths are Borel functionals of continuous paths; one may express hitting events by minima or maxima of the continuous radius over compact time intervals. The patched map is Borel by its countable construction. Assigning a cemetery state after \(\zeta\) gives a Borel map everywhere; the next section proves that the cemetery is almost surely never reached from any fixed \(z\in D\).

For every compactly supported \(C^2\) test function on \(D\), stopped Itô calculus gives the generator \(L\) in (D1). There is no extra diffusion coefficient or singular self-interaction. Pathwise uniqueness holds up to the maximal lifetime for the original equation by the same local argument; after nonexplosion it holds on every finite horizon. Any solution driven by a Brownian motion must coincide with this path functional, so its law is fixed by the Brownian law.

## 5. Explicit noncollision and nonexplosion estimates

For a general exponent \(\eta>0\), let \(V(z)=r^2+r^{-\eta}\). Direct differentiation on \(D\) gives

\[
 LV=4\nu d+\frac{4s}{N}r^{-s}
 +2\nu\eta(\eta-d+2)r^{-\eta-2}
 -\frac{2s\eta}{N}r^{-\eta-s-2}.
 \tag{D13}
\]

This verifies the proposed Lyapunov identity. For every fixed parameter tuple it is bounded above, since the negative term has the highest singular power at zero and all remaining nonconstant terms decay at infinity. To give an explicit bound convenient for stopping, take \(\eta=d-2>0\). The singular diffusion term then vanishes and

\[
 LV\le C_{N,\nu}:=4\nu d+
 \frac{4sd}{N(s+d)}
 \left[\frac{2s}{(d-2)(s+d)}\right]^{s/d}.
 \tag{D14}
\]

Indeed, maximizing \((4s/N)r^{-s}-(2s(d-2)/N)r^{-s-d}\) gives
\(r^d=(d-2)(s+d)/(2s)\) and exactly the second term in (D14). This constant is independent of the annulus; it need not be uniform in diffusivity. The final comparison below is uniform in diffusivity through a different estimate.

Stop a locally constructed path at \(\rho_{a,R}\), its first exit from \(D_{a,R}\), starting inside. The Itô stochastic integral for \(V(Z_{h\wedge\rho_{a,R}})\) has expectation zero: on this closed annulus its integrand is bounded, hence square integrable on a finite horizon. Therefore

\[
 \mathbb E_zV(Z_{H\wedge\rho_{a,R}})
 \le V(z)+C_{N,\nu}H.
 \tag{D15}
\]

Continuity puts an exiting path on one of the two boundary spheres. In particular,

\[
 \mathbb P_z(\rho_{a,R}\le H,\ |Z_{\rho_{a,R}}|=a)
 \le a^{d-2}[V(z)+C_{N,\nu}H],
\]

\[
 \mathbb P_z(\rho_{a,R}\le H,\ |Z_{\rho_{a,R}}|=R)
 \le R^{-2}[V(z)+C_{N,\nu}H].
 \tag{D16}
\]

For \(a=1/m,R=m\), their sum tends to zero. Since these exit times increase to \(\zeta\),
\(\mathbb P_z(\zeta\le H)=0\) for every finite \(H\). Taking integer horizons proves \(\zeta=\infty\) almost surely. This excludes both collision and explosion, for each fixed starting point and every fixed finite \(N,\nu\). It is a quantitative stopping argument, not an invocation of compactness. Each continuous sample path on a finite horizon therefore remains in some compact annulus, although the annulus can depend on that path.

## 6. Source integrability from the radial barrier

Fix \(0\le\tau\le T\). Apply smooth Itô calculus, only up to \(\tau\wedge\rho_m\), to \(F_{N,\tau-h}(|Z_h|)\). Equations (D9) and (D8) give

\[
 \mathbb E_z F_{N,\tau-\tau\wedge\rho_m}
                (|Z_{\tau\wedge\rho_m}|)
 +\mathbb E_z\int_0^{\tau\wedge\rho_m}j_0(Z_h)\,dh
 \le F_{N,\tau}(|z|).
 \tag{D17}
\]

The stochastic integral has zero expectation because the derivatives of the profile are bounded on the stopped space-time annulus. The first term is nonnegative. The stopping times increase to infinity almost surely, so monotone convergence of the positive time integrals proves

\[
 \mathbb E_z\int_0^\tau j_0(Z_h)\,dh\le F_{N,\tau}(|z|),
 \qquad
 \mathbb E_z\int_0^\tau|J_A(Z_h)|\,dh\le K F_{N,\tau}(|z|).
 \tag{D18}
\]

This establishes the missing source integrability uniformly in \(\nu\), with no bound on an evolved particle law. The process here is the explicitly constructed auxiliary relative diffusion.

One can also retain the exact expectation identity. The stopped terminal profile is bounded by the global bound in (D10) and converges almost surely to zero. The Laplacian lies between \(-Nd/2\) and zero. Dominated convergence for these two terms, and (D18) for the source, yield

\[
 \mathbb E_z\int_0^\tau j_0(Z_h)\,dh
 =F_{N,\tau}(|z|)+2\nu\mathbb E_z\int_0^\tau
                   \Delta F_{N,\tau-h}(|Z_h|)\,dh.
 \tag{D19}
\]

No unregularized stochastic integral or singular Itô formula was assumed in this passage; it is a limit of the stopped expectation identities with the convergence mechanisms stated explicitly.

## 7. Global and killed martingale solutions, Markov conditioning, and uniqueness

Define the potential for every \(\tau\in[0,T]\) and \(z\in D\) by the absolutely integrable expectation

\[
 U_A(\tau,z)=\mathbb E_z\int_0^\tau J_A(Z_h)\,dh,
 \qquad \Phi_A(t,z)=U_A(T-t,z).
 \tag{D20}
\]

The constructed path map is Borel, the source is continuous on \(D\), and positive and negative source integrals are measurable by time integration. Integrating them against the fixed Brownian path law gives Borel functions of \((\tau,z)\); their finiteness follows from (D18). Values on the null set of finite maximal lifetime can be assigned using the cemetery convention without affecting any such expectation. This supplies the measurable kernel required for the later iid statistic.

Equations (D18) and (D10) prove (D4) and the finite global bound

\[
 \sup_{0\le t\le T,z\in D}|\Phi_A(t,z)|
 \le K\frac{(2sp)^{2/p}}4N^{s/p}T^{2/p}.
 \tag{D21}
\]

We now prove the conditioning property used to identify this potential as a solution. The pathwise integral equation and uniqueness give the flow identity

\[
 Z_{u+h}^{z}(b)=Z_h^{Z_u^z(b)}(b^{(u)}),\qquad
 b^{(u)}_h=b_{u+h}-b_u,
 \tag{D22}
\]

whenever the paths exist. This follows by splitting its time integral at \(u\). The maps on both sides are measurable. For a fixed deterministic \(u\), Brownian increments \(B^{(u)}\) are independent of the past and have the original Brownian law. Thus conditional expectations of bounded Borel functions of the future path are obtained by starting the same path functional at the random state \(Z_u\). Nonexplosion from every deterministic starting point, together with the Borel construction, also gives probability one of nonexplosion after conditioning on this random state. This proves the deterministic-time Markov property actually needed; no strong Markov or boundary regularity theorem is being tacitly imported. The conditioning identity extends to the source time integral by positive/negative truncation and (D18).

For a fixed starting \((t,z)\), this identity gives, for \(0\le h\le T-t\),

\[
 \Phi_A(t+h,Z_h)+\int_0^hJ_A(Z_u)\,du
 =\mathbb E_z\left[\int_0^{T-t}J_A(Z_u)\,du\,middle|\,\mathcal F_h\right].
 \tag{D23}
\]

The left side is therefore an integrable martingale; as a family of conditional expectations of one integrable variable it is uniformly integrable. Here a martingale is meant in the explicit conditional-expectation sense at deterministic times. Joint measurability follows from the Borel potential and path construction; no unproved differentiability of the potential is included.

**Global solution class.** A bounded martingale solution means a bounded Borel function on \([0,T]\times D\), zero at \(t=T\), such that for every starting \((t,z)\) the left side of (D23), with that function in place of \(\Phi_A\), is a martingale for the constructed diffusion. The source integrability is supplied independently by Section 6. Taking expectations at the terminal time forces any such solution to equal (D20). Hence existence and uniqueness in this exact class are proved. The generator realized on smooth compactly supported test functions is (D1); the potential is not being called classical.

A bounded classical punctured solution, if continuous up to terminal time locally in space and sufficiently differentiable for stopped Itô calculus, belongs to this martingale class. Indeed, its stopped Itô martingales converge at fixed times almost surely and in L1: their absolute values are bounded by a fixed bound on the solution plus the integrable full absolute source integral. Conditional expectations therefore pass to the limit. This gives uniqueness and the comparison for such a classical solution if it exists; it is not a classical-existence claim.

**Annular solution class for \(\nu>0\).** Let the process be killed on first exit \(\rho_{a,R}\) from \(D_{a,R}\), using a cemetery state thereafter. Define

\[
 U_A^{a,R}(\tau,z)
 =\mathbb E_z\int_0^{\tau\wedge\rho_{a,R}}J_A(Z_h)\,dh,
 \qquad z\in D_{a,R}.
 \tag{D24}
\]

Set its cemetery, lateral killing, and terminal values to zero. The annular martingale class is the bounded Borel class for which

\[
 \mathbf1_{\{h<\rho_{a,R}\}}\Phi(t+h,Z_h)
 +\int_0^{h\wedge\rho_{a,R}}J_A(Z_u)\,du
 \tag{D25}
\]

is a martingale from every initial interior point, with the zero terminal and killed values just specified. Splitting the path at deterministic times in (D22), and retaining the event of survival to that time, proves the corresponding killed Markov identity. Formula (D24) then makes (D25) a conditional expectation of the terminal source integral. Taking the terminal expectation proves uniqueness in this class. The stopped version of (D17) proves \(|U_A^{a,R}(\tau,z)|\le KF_{N,\tau}(|z|)\), independently of \(a,R\). The zero lateral condition here is **killing in the stated probabilistic sense**; continuity of a Dirichlet trace and classical annular regularity have not been asserted without proof. Any classical annular solution from Section 3 is identified with (D24) by its stopped Itô identity and continuity at the killed boundary.

**Exhaustion.** For \(a_m\downarrow0,R_m\uparrow\infty\) with nested annuli containing the fixed starting point, their exit times increase to infinity almost surely by Section 5. The positive source integrals increase to the global positive integral. The signed integrals converge almost surely and in L1, dominated by the full integrable absolute source integral in (D18). Consequently

\[
 U_A^{a_m,R_m}(\tau,z)\longrightarrow U_A(\tau,z)
 \tag{D26}
\]

for every fixed \(\tau,z\); the underlying stopped source integrals converge in L1 as well. This identifies the punctured infinite-domain realization and retains its uniform radial bound. No spatial compactness theorem or unproved convergence of derivatives is used.

**Zero diffusivity.** For \(\nu=0\), the global path is the outward characteristic

\[
 Z_h(z)=\left(r^p+\frac{2sp h}{N}\right)^{1/p}\theta.
\]

Integrating its source gives exactly \(\Phi_A(t,z)=(\theta^TA\theta)F_{N,T-t}(r)\). It is the unique finite solution in the forward absolutely-continuous characteristic class, because its composition along each characteristic has derivative \(-J_A\) and terminal value zero. This is the class used at \(\nu=0\). No zero value is imposed at a finite transport outflow radius; doing so in addition to arbitrary terminal data would define a different, generally incompatible classical boundary problem.

## 8. The initial iid endpoint of the periodic cutoff diagnostic

Fix \(0<R_0<R_1<1/2\), and the smooth even radial cutoff \(\chi\) of THM-017, equal to one on \(B_{R_0}\), zero outside \(B_{R_1}\), with \(0\le\chi\le1\). Inside the embedded Euclidean torus ball define

\[
 h_{N,\nu,\tau}(z)=\chi(z)U_A(\tau,z)\quad(z\ne0),
 \qquad h_{N,\nu,\tau}(0)=0,
\]

and extend by zero and periodicity. This is a bounded Borel kernel for each finite parameter tuple. Oddness of the drift, evenness of \(J_A\), Brownian symmetry under sign reversal, and pathwise uniqueness give \(U_A(\tau,-z)=U_A(\tau,z)\). Thus

\[
 \mathcal H_{N,\nu,\tau}(x,y)=h_{N,\nu,\tau}(x-y)
 \tag{D27}
\]

is a real symmetric pair kernel. No regularity at the torus diagonal is presumed. The arbitrary diagonal value is immaterial for the bounded-density laws below. Multiplication by \(\chi\) constructs an independently defined diagnostic, not a solution of the full periodic pair equation.

Let \(X_1,\ldots,X_N\) be iid with a probability density \(\mu\) on the unit torus satisfying \(\|\mu\|_\infty\le M\). The density may vary with the model parameters provided this same finite bound holds. Translation of the torus integral gives precisely one density factor:

\[
 \|\mathcal H\|_{L^2(\mu\otimes\mu)}^2
 =\int|h(z)|^2\left[\int\mu(y+z)\mu(y)\,dy\right]dz
 \le M\int|h(z)|^2dz
 \le MK^2\int_{B_{R_1}}F_{N,\tau}(|z|)^2dz.
 \tag{D28}
\]

For completeness, the exact centering from THM-015 is retained. For a symmetric L2 kernel \(H\), set \(m=\mu^2(H)\), \(q_H(x)=\int H(x,y)\mu(dy)-m\), and \(r_H(x,y)=H-m-q_H(x)-q_H(y)\). Then the frozen mean-field-centered statistic with denominator \(N^2\) satisfies

\[
 P_N[H]= -\frac m{2N}-\frac1{N^2}\sum_iq_H(X_i)
                   +\frac1{N^2}\sum_{i<j}r_H(X_i,X_j).
\]

Conditioning on shared labels gives orthogonality of distinct canonical pairs and of the first-projection sum with those pairs. Hence

\[
 \mathbb EP_N[H]= -\frac m{2N},\qquad
 \mathbb EP_N[H]^2
 =\frac{m^2}{4N^2}+\frac{\|q_H\|_2^2}{N^3}
       +\frac{N-1}{2N^3}\|r_H\|_2^2
 \le\frac{N-1}{2N^3}\|H\|_2^2.
 \tag{D29}
\]

The inequality follows from
\(\|H\|_2^2=m^2+2\|q_H\|_2^2+\|r_H\|_2^2\), with the three coefficient comparisons valid for every \(N\ge2\). In particular the expectation bias has not been dropped, and no exact expectation-centering has been silently substituted.

Let \(b_N=\min(\beta_N,1)\), \(\beta_N>0\), and \(\sigma_N=\sqrt{Nb_N}\). Combining (D28) and (D29) gives

\[
 \mathbb E|\sigma_NP_N[\mathcal H_{N,\nu,\tau}]|^2
 \le\frac{b_N(N-1)}{2N^2}MK^2
                   \int_{B_{R_1}}F_{N,\tau}^2.
 \tag{D30}
\]

The profile bound is independent of \(\nu\), so this estimate also permits \(\nu=1/\beta_N\), or any other finite nonnegative sequence, without an extra dependence in the constant.

Here are the required spatial estimates rather than an unproved norm transfer. For \(\tau>0\), let \(\ell=(2sp\tau/N)^{1/p}\). Split the radial integral at \(\ell\), using the constant core bound and the outer \(s\tau r^{-s}\) bound in (D10). If \(\ell\le R_1\), the core contribution is bounded by a constant times
\(N^2\ell^{d+4}= (2sp)^2\tau^2\ell^{d-2s}\), and the exterior contribution by a constant times
\(\tau^2\int_\ell^{R_1}r^{d-1-2s}dr\). If \(\ell>R_1\), the same constant core bound gives the corresponding upper estimates below, since the ball volume is at most the core volume. Thus, with constants depending only on \(d,s,R_1\),

\[
 \int_{B_{R_1}}F_{N,\tau}^2\le C
 \begin{cases}
 \tau^2,&2s<d,\\
 \tau^2[1+\log_+(R_1/\ell)],&2s=d,\\
 N^{(2s-d)/p}\tau^{(d+4)/p},&2s>d.
 \end{cases}
 \tag{D31}
\]

For the first row, one may alternatively use \(F\le s\tau r^{-s}\) throughout the ball. At \(\tau=0\) the norm is exactly zero, without dividing by \(\ell\). In the middle row \(\tau^2\log_+(1/\tau)\) is bounded on a fixed finite interval and tends to zero at zero. Therefore, for all \(N\ge2\), with a fixed-data constant independent of \(\nu,\beta_N\) and \(\tau\),

\[
 \boxed{\quad
 \sup_{0\le\tau\le T}
 \mathbb E|\sigma_NP_N[\mathcal H_{N,\nu,\tau}]|^2
 \le C_T b_N
 \begin{cases}
 N^{-1},&2s<d,\\
 (1+\log N)/N,&2s=d,\\
 N^{-(d+2-s)/(s+2)},&2s>d.
 \end{cases}\quad}
 \tag{D32}
\]

Here \(C_T\) may depend on \(d,s,A,M,R_0,R_1,\chi,T\), but not on \(N,\nu,\beta_N\). The supremum is outside the expectation. All exponents decay in the declared range. This proves L2, hence L1 and probability, negligibility for every deterministic remaining-time sequence in \([0,T]\), every finite diffusivity sequence, and every positive temperature sequence. Only upper bounds are claimed for positive diffusivity; the zero-diffusion two-sided orders of THM-017 have not been transferred to this model without a lower bound.

## 9. Required tests, adversarial checks, and limitations

**The boundary dimension and larger dimensions.** At \(d=s+2\), the bracket in (D7) becomes \((2s+2)(1-q)\), positive for \(q<1\); the radial comparison therefore includes equality in the dimension restriction. For \(d>s+2\), the extra positive term \(d-s-2\) preserves the sign. This sign proof is not extended to \(d<s+2\); in that range the bracket is negative near \(q=1\), and this supersolution argument supplies no theorem.

**Zero and large diffusivity.** At \(\nu=0\), the characteristic formula is recovered exactly, with no finite-radius outflow condition. For every finite \(\nu>0\), including arbitrarily large values, the term \(2\nu\Delta F\) has the favorable sign. The Lyapunov constant may grow with \(\nu\), but the source and kernel comparison constants do not. No limit as \(\nu\to\infty\) and no continuity theorem as \(\nu\downarrow0\) are asserted.

**Isotropic and traceless sources.** For \(A=aI\), the solution is \(a\) times the positive radial potential of \(j_0\), by rotational symmetry and linearity of the expectation. For \(a=1\), \(\tau>0\) and \(\nu>0\), (D19) and strict negativity of \(\Delta F\) at positive remaining time give the strict test
\(0<U_I(\tau,z)<F_{N,\tau}(|z|)\). At zero diffusivity equality holds. Thus the signed transport-only formula is generally not being misidentified with the diffusive solution.

A nonzero traceless \(A\) is not discarded by taking an angular average. The potential is linear in the whole matrix, and its absolute value is bounded using \(K\), without a positivity claim for the signed source. To check that its source has not disappeared, fix \(z\ne0\). Path continuity gives
\(\tau^{-1}\int_0^\tau J_A(Z_h)dh\to J_A(z)\) almost surely. For the positive envelope
\(Y_\tau=\tau^{-1}\int_0^\tau j_0(Z_h)dh\), (D18) and (D10) give \(\mathbb EY_\tau\le j_0(z)\), while the same pathwise limit and Fatou give convergence of its expectations to \(j_0(z)\). Since
\(\mathbb E|Y_\tau-j_0(z)|=\mathbb EY_\tau+j_0(z)-2\mathbb E\min(Y_\tau,j_0(z))\), bounded convergence of the minimum proves L1 convergence of these positive envelopes. To check the signed passage explicitly, write \(X_\tau=\tau^{-1}\int_0^\tau J_A(Z_h)dh\) and \(c=j_0(z)>0\). On \(\{Y_\tau\le2c\}\), the difference \(|X_\tau-J_A(z)|\) is bounded by \(3Kc\) and tends to zero almost surely, so its expectation tends to zero. On the complementary event it is at most \(K(Y_\tau+c)\le3K|Y_\tau-c|\), whose expectation tends to zero. Thus the signed averages converge in L1 as well. Consequently

\[
 \lim_{\tau\downarrow0}\frac{U_A(\tau,z)}\tau=J_A(z).
 \tag{D33}
\]

For a nonzero symmetric traceless matrix, choose a direction with \(\theta^TA\theta\ne0\); the potential is nonzero there at sufficiently small positive times. No sign-independent lower bound is needed for (D32).

**Small particle counts and terminal time.** At \(N=2\), (D3) is one half times \([(r^p+sp\tau)^{2/p}-r^2]\), the internal drift is \(s r^{-p}z\), and (D6) has coefficient one. At \(N=3\), they are respectively three quarters times \([(r^p+2sp\tau/3)^{2/p}-r^2]\), drift \((2s/3)r^{-p}z\), and Laplacian coefficient \(3/2\). Direct substitution in (D5) gives the same source \(-sr^{-s}\) in both cases. The iid coefficient in (D29) is \(1/16\) at \(N=2\) and \(1/27\) at \(N=3\). At zero remaining time every potential and diagnostic vanishes exactly. Bound (D21), with \(T\) replaced by \(\tau\), also gives uniform terminal convergence in \(z\) for each fixed \(N\), uniformly in diffusivity.

**Potential proof failures explicitly avoided.** Collision avoidance was proved before removing the stopping times; source integrability was proved before defining the signed potential; its measurability and conditioning were proved before using the martingale identity. The uniqueness class does not assume a classical PDE solution that has not been constructed. The annular killing convention is distinguished from a continuous boundary trace, and zero-diffusion transport uses its characteristic class. The comparison applies to the radial majorant, not to the Laplacian of the anisotropic signed transport profile. No expectation is promoted to a pathwise estimate or to an evolved-law estimate. No second-moment divergence or probability-limit theorem appears in the proof.

The result still omits ordinary local transport, both nonlocal response terms, the actual time-dependent backward test/source, the periodic force remainder, and any equation error introduced by the diagnostic cutoff. It supplies none of the evolved-law cubic, contraction, pair martingale, or singular full-generator estimates. Those remain separate obligations. The first full-operator task is to control the response and other omitted terms in a solution class compatible with this bounded local realization; (D32) alone does not accomplish that task.

## 10. Verification and sealed handoff

This report uses the six files recorded in `AUDITS/ROUND_004_DIFFUSIVE_INPUT_SHA256SUMS.txt`, together with the governing instructions and frozen model recorded in `AUDITS/ROUND_004_DIFFUSIVE_SUPPLEMENTAL_INPUT_SHA256SUMS.txt`. Both manifests were verified before sealing. No external theorem or citation is load-bearing; the existence argument is the explicit stopped Picard construction, smooth Itô calculation and elementary conditional expectation proof above.

The mathematical checks are analytical: direct profile derivatives and time sign; the two dimension cases; Lyapunov derivatives and the explicit maximum; annular exit bounds; every source-convergence step; measurable flow and Markov conditioning; isotropic strict comparison; traceless terminal slope; zero/large diffusivity; particle counts two and three; terminal time; exact centering coefficients; and the three radial norm regimes. No stochastic simulation or numerical asymptotic claim is used.

Executed integrity checks: supplied and supplemental input hashes verified; `git diff --check` passed; the new text was checked for control characters, trailing whitespace, terminal newline, and balanced display delimiters. The adjacent output manifest records the report and input-manifest hashes and was verified after generation. These are integrity and self-checks, not independent mathematical certification. No TeX file was created or modified, so no TeX compilation was applicable. No campaign-wide verifier was loaded beyond the permitted input scope.

Created files are this memorandum, the supplemental input manifest, and `MEMORANDA/ROUND_004_DIFFUSIVE_COMPARISON_SHA256SUMS.txt`. All earlier issued bytes and copied prerequisites remain unchanged. No root canonical file, ledger, historical input, old audit, or source was edited; no commit, push, dependency change, child worker, or public communication occurred.

The bounded local assertion, including its probabilistic existence and domain passage, has no remaining gap in this construction. Classical regularity is unproved and unclaimed. The next action is separate hostile review of this sealed construction; root alone assigns audit status and integrates canonical records. The full-operator and evolved-law mission remains open.
