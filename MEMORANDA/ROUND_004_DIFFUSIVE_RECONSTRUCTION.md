# Round 004: independent reconstruction of the local diffusive comparison

2026-09-17 UTC. Blind reconstruction lane `/root/r004_diffusive_blind`.
Worktree: `/private/tmp/hocf-r004-diffusive-blind-20260917`.
Branch: `codex/hocf-r004-diffusive-blind`.
Base: `2f532ccd2cb5f3d84db456be96e438f03f7e2ad2`.

**Result:** the proposed radial comparison is correct in the declared range. It gives a globally defined, bounded, jointly Borel probabilistic solution on the punctured Euclidean domain, unique in the true-martingale class specified below. Annular killed solutions exhaust this solution. The compactly supported initial-iid diagnostic has the stated vanishing upper bounds, uniformly in the retained diffusion coefficient. This is an independent reconstruction from the frozen assertion and permitted Round 003 prerequisites, not a verdict on an unseen Round 004 proof. Classical interior regularity of the constructed expectation is not asserted or needed.

The only new mathematical inputs read were `TASKS/ACTIVE/TASK-032_ROUND004_DIFFUSIVE_COMPARISON.md`, `THEOREMS/THM-015_IID_PAIR_SECOND_MOMENT.md`, `THEOREMS/THM-017_INTERNAL_PAIR_TRANSPORT_MODEL.md`, and `MEMORANDA/ROUND_003_PAIR_TRANSPORT_MODEL.md`. Administrative/model inputs were `AGENTS.md` and `TASKS/ACTIVE/ROUND_001_MODEL.md`. Their copied bytes are recorded in `AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_INPUT_SHA256SUMS.txt`. No Round 004 constructor output, root TeX, other new report, memory, or outside source was read. The restricted blind dossier governs this lane instead of the repository's broader orientation reading. No literature, novelty, periodic singular-force, or Fourier-normalization claim is imported. The analytic input is the elementary smooth stopped Itô formula already permitted by the frozen model; the construction, bounds, Markov property, and uniqueness argument are given here.

## 1. Exact assertion, negation, and normalization

Fix an integer `d>=3`, `0<s<=d-2`, `p=s+2`, an integer `N>=2`, `0<=nu<infinity`, `0<=T<infinity`, and a fixed real symmetric matrix `A`. Let `D=R^d\{0}` and, for `z=r theta` in D, set

\[
 b_N(z)=\frac{2s}{N}r^{-s-2}z,\qquad
 L=2\nu\Delta+b_N\cdot\nabla,\qquad
 f(z)=s r^{-s},\qquad J_A(z)=f(z)\theta^T A\theta.
 \tag{1.1}
\]

The desired equation is the backward equation

\[
 (\partial_t+L)\Phi=-J_A,\qquad \Phi(T,\cdot)=0.
 \tag{1.2}
\]

The retained relative-coordinate diffusion is `2 nu Delta`: a noise amplitude `sqrt(4 nu)` has exactly this generator. The force is outward, with coefficient `2s/N`. No one-body/background terms are included. Define, for `tau>=0` and `r>0`,

\[
 F_{N,\tau}(r)=\frac N4
 \left[\left(r^p+\frac{2sp\tau}{N}\right)^{2/p}-r^2\right].
 \tag{1.3}
\]

The precise assertion proved below is the conjunction of the following statements.

1. For `nu>0`, every annular classical zero-terminal, zero-lateral solution, in the class in Section 3, obeys `|Phi(t,z)|<=||A||_op F_(N,T-t)(r)`. The same bound holds for the constructed annular killed solution in its specified Borel martingale class, which has zero boundary trace.
2. The additive-noise equation with generator L has a unique nonexplosive, noncolliding solution from every point of D. Its source occupation is integrable. Its Feynman--Kac potential is jointly Borel, globally bounded for fixed parameters and T, obeys that comparison, and is unique in the class in Section 7. Annular killed potentials converge to it.
3. At `nu=0`, the solution is the punctured characteristic solution from THM-017; an annular two-sided Dirichlet trace is not imposed.
4. The separate periodic cutoff diagnostic obeys the initial-iid second-moment endpoint estimates in Section 9, with the campaign's original centering and with the supremum outside expectation.

The exact negation is that some permitted parameters and declared solution violate one of these statements, or that a required existence, measurability, integrability, uniqueness, or limiting assertion fails in its explicitly specified class. The proofs below exclude this negation in this local model. They neither state nor negate a full campaign theorem.

## 2. Direct radial reconstruction and the comparison sign

Write `W=r^p+2sp tau/N` and `q=r^p/W`. Direct differentiation, without assuming the proposed seed, gives

\[
 \partial_\tau F=sW^{-s/p},\qquad
 F_r=\frac N2 r(q^{s/p}-1),\qquad
 F_{rr}=\frac N2\left[q^{s/p}(1+s-sq)-1\right].
 \tag{2.1}
\]

Consequently

\[
 \partial_\tau F-b_N\cdot\nabla F=f,
 \qquad
 \Delta F=\frac N2\left[q^{s/p}(d+s-sq)-d\right].
 \tag{2.2}
\]

For `0<q<=1`, set `G(q)=q^(s/p)(d+s-sq)`. Then

\[
 G'(q)=\frac{s}{p}q^{s/p-1}
       \left[d+s-(2s+2)q\right]\ge0,
 \tag{2.3}
\]

because the bracket is at least `d-s-2=d-p>=0`. Since `G(1)=d` and `G(0)=0` by continuous extension,

\[
 -\frac{Nd}{2}\le\Delta F\le0,
 \qquad (\partial_\tau-L)F=f-2\nu\Delta F\ge f.
 \tag{2.4}
\]

For `tau>0`, the Laplacian is strictly negative at every finite positive r. At `d=p`, the derivative in (2.3) vanishes only at q=1; G is still strictly increasing before that endpoint. At `tau=0`, `F=0` and `Delta F=0`. Thus the time sign, threshold endpoint, and terminal value are all explicit.

The profile is nonnegative and satisfies

\[
 F_{N,\tau}(r)\le s\tau r^{-s},\qquad
 F_{N,\tau}(r)\le F_{N,\tau}(0+)
 =\frac{(2sp)^{2/p}}4 N^{s/p}\tau^{2/p}.
 \tag{2.5}
\]

Indeed `F=s integral_0^tau (r^p+2sp h/N)^(-s/p) dh`, and its radial derivative in (2.1) is nonpositive. These constants do not depend on nu or on annular radii. They do not assert a uniform-in-N supremum bound: the displayed core amplitude grows as `N^(s/p)` at fixed positive tau.

Only the positive radial amplitude is a supersolution. Multiplication by the signed angular factor does not preserve (2.4). In particular, no assertion concerning the Laplacian of the signed transport solution is used.

## 3. Conditional classical annular theorem

Fix `nu>0` and `0<a<R<infinity`. Let `D_(a,R)={a<|z|<R}`. An annular classical solution means a function continuous on `[0,T]` times the closed annulus, with terminal and lateral values zero, and of class `C^(1,2)` in the open parabolic cylinder, satisfying (1.2) there. No differentiability at an initial/lateral corner is required. This paragraph assumes such a classical solution; existence of that regularity class is not imported.

Put `u(tau,z)=Phi(T-tau,z)`, `K=||A||_op`, and `w=K F`. Then

\[
 (\partial_\tau-L)(u-w)=J_A-K(f-2\nu\Delta F)\le0.
\]

The function `u-w` is nonpositive initially and on both lateral boundaries, since F is nonnegative. To prove comparison directly, subtract `epsilon tau`. A positive maximum of this perturbed difference over any closed truncated cylinder cannot occur on its parabolic boundary. At an interior spatial maximum at positive remaining time, its time derivative is nonnegative, gradient is zero, and Laplacian is nonpositive; hence its parabolic operator is nonnegative, contrary to its upper bound `-epsilon`. The same one-sided time derivative applies if the maximum occurs at the top time. Letting epsilon decrease to zero gives `u<=w`. Applying the identical argument to `-u` gives

\[
 |\Phi(t,z)|\le K F_{N,T-t}(|z|).
 \tag{3.1}
\]

Applying comparison to the difference of two solutions proves uniqueness in this classical class. Section 6 constructs an actual killed probabilistic solution, with zero boundary trace, without asserting its classical interior regularity.

## 4. Pathwise local construction and its measurable dependence

We use Brownian motion on its canonical continuous-path space with its usual filtration. The equation is

\[
 Z_h=z+\sqrt{4\nu}\,B_h+\int_0^h b_N(Z_v)\,dv.
 \tag{4.1}
\]

A construction requiring no singular SDE existence theorem is available because the noise is additive. For integer `m>=2`, choose the explicit radial Lipschitz cutoff

\[
 \eta_m(r)=\min(1,\max(0,2mr-1)),\qquad
 \xi_m(r)=\min(1,\max(0,2-r/m)),
\]

and set `b_m(z)=eta_m(|z|) xi_m(|z|) b_N(z)`, with value zero at zero. It is globally bounded and globally Lipschitz, and equals b_N on `1/m<=|z|<=m`.

For a continuous driving path w and finite horizon H, start Picard iteration at `z+sqrt(4nu) w` and integrate b_m successively. If b_m is bounded by B and has Lipschitz constant C, the difference of its successive iterates is at most `B C^(k-1) H^k/k!` for the kth increment. The summable series converges uniformly, solves the integral equation, and uniqueness follows by the same factorial iteration of the difference inequality. The solution depends continuously on `(z,w)` in the uniform norm: its difference is bounded by the initial/noise difference times `exp(C H)`. Each cutoff solution map is consequently Borel, causal, and adapted when w is Brownian motion.

Cutoff solutions agree until exit from any smaller annulus on which both drifts equal b_N, by this pathwise uniqueness argument. For a fixed initial z, take all sufficiently large m for which z lies in `D_m={1/m<|z|<m}` and denote the consistent exit times by `sigma_m`. They increase. Patch the solutions before `zeta=lim_m sigma_m`; this gives the unique maximal pathwise solution on D. If its lifetime is finite, assign a cemetery point thereafter.

This maximal map is jointly Borel in the initial point and driving path. To see the only possible measurability issue explicitly, first select the initial m by a Borel integer-valued choice. Each cutoff exit time is Borel, since for continuous paths the event of remaining in an open annulus through a fixed compact time interval is described by strict lower and upper bounds on the minimum and maximum radius. Patching then uses a countable choice of m with `sigma_m>h`; lifetime is an increasing limit of these measurable times. Time evaluation and integration are Borel as well. No simultaneous-in-z null set is needed in this construction.

The deterministic pathwise solution has the flow identity before its lifetime: restarting at time h with the shifted driving path gives the same future solution, by uniqueness. Its cemetery extension has the corresponding killed identity. The absence of finite lifetime for Brownian paths from every fixed z is proved next; it has not been assumed in constructing this map.

## 5. Stopped source estimate and complete collision/explosion control

All Itô calculations in this section are on a finite annulus, before its exit `sigma`. The functions differentiated are smooth on that annulus; all stochastic integrals are genuine martingales on a fixed finite horizon because their integrands are bounded there.

For fixed `tau>=0`, apply Itô to `F_(N,tau-h)(|Z_h|)` until `h= tau wedge sigma`. Equations (2.2)--(2.4) give

\[
 \mathbb E_z F_{N,\tau-(\tau\wedge\sigma)}(|Z_{\tau\wedge\sigma}|)
 +\mathbb E_z\int_0^{\tau\wedge\sigma} f(Z_h)\,dh
 =F_{N,\tau}(r)
 +2\nu\mathbb E_z\int_0^{\tau\wedge\sigma}
             \Delta F_{N,\tau-h}(|Z_h|)\,dh
 \le F_{N,\tau}(r).
 \tag{5.1}
\]

The nonnegative first term may be discarded. This proves the integrable stopped-source bound before any global domain passage, uniformly in annuli, N, and nu in the precise sense of the same displayed profile.

There is a particularly transparent exit argument. Since `d>=3`, the positive function `r^(2-d)` is harmonic off zero and

\[
 L r^{2-d}=-\frac{2s(d-2)}{N}r^{-s-d}\le0.
\]

Therefore, on an annulus `a<r<R`, for any `H>=0`,

\[
 \mathbb P_z\{\sigma\le H,\ |Z_\sigma|=a\}
 \le (a/r)^{d-2}.
 \tag{5.2}
\]

The radius squared gives the independent identity

\[
 Lr^2=4\nu d+\frac4N f.
\]

Together with (5.1), this gives

\[
 \mathbb P_z\{\sigma\le H,\ |Z_\sigma|=R\}
 \le\frac{r^2+4\nu dH+(4/N)F_{N,H}(r)}{R^2}.
 \tag{5.3}
\]

The bounds use the continuous exit radius and the nonnegativity of the test functions at all other stopped outcomes. Summing (5.2) and (5.3) gives an explicit bound for total exit probability. For `a=1/m`, `R=m`, it tends to zero for every finite H and every fixed permitted N, nu, z. Thus

\[
 \mathbb P_z\{\zeta\le H\}
 =\lim_m\mathbb P_z\{\sigma_m\le H\}=0.
\]

Taking the countable union over integer H proves nonexplosion and noncollision for all finite times. This uses no assumption about the limiting law of particles, no origin boundary condition, and no singular Itô formula at the origin.

Monotone convergence in (5.1), now that `sigma_m` tends to infinity almost surely, proves

\[
 \mathbb E_z\int_0^\tau f(Z_h)\,dh\le F_{N,\tau}(r)<\infty.
 \tag{5.4}
\]

In particular, the signed source is absolutely integrable. Every continuous sample path stays in a compact subset of D over a fixed finite horizon, but (5.4), not that pathwise statement alone, supplies expectation integrability.

For completeness, the proposed Lyapunov seed is also exactly correct. For any `q>0`,

\[
 L(r^2+r^{-q})=4\nu d+\frac{4s}{N}r^{-s}
 +2\nu q(q-d+2)r^{-q-2}
 -\frac{2sq}{N}r^{-q-s-2}.
 \tag{5.5}
\]

The negative last power dominates every positive singular power as r decreases to zero; at infinity the expression tends to `4 nu d`. It is consequently bounded above. An entirely explicit convenient choice is `q=d-2`, for which

\[
 LV\le C_{N,\nu}:=4\nu d+
 \frac{4sd}{N(d+s)}
 \left[\frac{2s}{(d-2)(d+s)}\right]^{s/d}.
 \tag{5.6}
\]

Maximizing `4s x^s-2s(d-2)x^(d+s)` over `x>=0` proves (5.6). Stopped Itô gives `E V(Z_(H wedge sigma))<=V(z)+C_(N,nu)H`, hence the respective inner and outer exit bounds obtained by dividing by `a^2+a^(-q)` and `R^2+R^(-q)`. This validates the proposed mechanism independently of the sharper bounds (5.2)--(5.3). No optional-stopping limit is taken without its nonnegative test-function bound.

A separate one-dimensional falsification check recovers the exact finite-annulus hitting probability for `nu>0`. For radial functions the generator is

\[
 L_{\rm rad}=2\nu\frac{d^2}{dr^2}
 +\left[\frac{2\nu(d-1)}r+\frac{2s}{N}r^{-s-1}\right]\frac d{dr}.
\]

Its increasing scale function may be chosen with derivative

\[
 S'(r)=r^{1-d}\exp\{r^{-s}/(N\nu)\},\qquad L_{\rm rad}S=0.
 \tag{5.7}
\]

The finite-annulus exit has finite mean: stopped Itô on `R^2-r_h^2` gives `E sigma<=(R^2-r^2)/(4 nu d)`. The bounded stopped function S therefore gives

\[
 \mathbb P_r\{\hbox{exit at }a\}
 =\frac{S(R)-S(r)}{S(R)-S(a)}.
 \tag{5.8}
\]

Since `S(a)` tends to minus infinity as a decreases to zero, the inner-hit probability tends to zero at fixed R. This independent radial test checks the repulsive sign and the factors `2s/N` and `2nu`; it agrees with, but is not needed for, the preceding construction.

## 6. Actual annular killed realization and its exhaustion

The global process can now be used, or equivalently the consistent cutoff process until annular exit. For `nu>0`, define

\[
 u_{a,R}(\tau,z)=\mathbb E_z
       \int_0^{\tau\wedge\sigma_{a,R}}J_A(Z_h)\,dh
       \quad(z\in D_{a,R}),
 \tag{6.1}
\]

and give it value zero on the spatial boundary, after killing, and at remaining time zero. The integrand is bounded before exit; the joint Borel construction in Section 4 makes (6.1) jointly Borel. Equation (5.1) proves `|u_(a,R)(tau,z)|<=||A|| F_(N,tau)(r)`.

Its Dirichlet boundary values are actual zero traces. Here is a direct verification, avoiding a boundary regularity theorem. Let `C_J=s||A|| a^(-s)`. Then `|u_(a,R)|<=C_J E_z sigma`. At the outer boundary,

\[
 \mathbb E_z\sigma\le\frac{R^2-r^2}{4\nu d}\longrightarrow0
 \quad(r\uparrow R).
\]

For the inner boundary, let

\[
 M=\max_{a\le\rho\le R}
   \left[2\nu(d-1)/\rho+(2s/N)\rho^{-s-1}\right],\quad
 \kappa=1+M/(2\nu),\quad
 \psi(r)=1-e^{-\kappa(r-a)}.
\]

A direct radial differentiation gives
`L psi <= -c`, where `c=2 nu kappa exp(-kappa(R-a))>0`. Since psi is nonnegative on the closed annulus, stopped Itô gives `E_z sigma<=psi(r)/c`, which tends to zero as `r` decreases to a. The boundary traces are uniform in remaining time in `[0,T]`; their constants need not be uniform as nu decreases to zero. The time variable in (6.1) is Lipschitz with constant C_J. No interior differentiability is inferred from these facts.

The deterministic-time Markov argument is supplied in Section 7. Applied to the killed process, it shows that (6.1) is the unique bounded, jointly Borel killed-martingale solution: for every starting `(t,z)`,

\[
 u_{a,R}(T-t-h,Z_h)\mathbf1_{\{h<\sigma_{a,R}\}}
 +\int_0^{h\wedge\sigma_{a,R}}J_A(Z_v)\,dv,
 \quad 0\le h\le T-t,
 \tag{6.2}
\]

is a true martingale, with the potential interpreted as zero at terminal time or killing. The class is exactly bounded Borel functions with zero terminal/killing values for which this martingale property holds from every starting point. Uniqueness follows by taking the expectation at `h=T-t`. Every classical annular solution in Section 3 belongs to this class by stopped smooth Itô and continuous zero boundary values; thus, if such a classical solution is available, it is necessarily (6.1).

For the increasing annuli `D_m`, the signed integrals defining (6.1) converge almost surely and in L1 to the full source integral. Indeed their absolute difference is bounded by

\[
 \|A\|\int_{\sigma_m\wedge T}^T f(Z_h)\,dh,
\]

which tends to zero almost surely and is dominated by the integrable total occupation in (5.4). Hence their expectations converge to the global potential. For each fixed starting point z, this convergence is uniform over deterministic remaining times in `[0,T]`, by the same tail estimate. No spatially uniform annular-exhaustion assertion is required or made.

## 7. Markov property, global solution class, and uniqueness

Let `X_h(z,w)` be the Borel maximal map from Section 4, with its cemetery convention. For Brownian driving paths its lifetime is infinite almost surely for every fixed z. Define

\[
 P_h g(z)=\mathbb E[g(X_h(z,B))]
\]

for bounded Borel g. Integration of a jointly Borel map makes this a Borel function of z. The flow identity and Brownian independent increments give, at deterministic times h,

\[
 \mathbb E_z[g(Z_{h+v})\mid\mathcal F_h]=P_vg(Z_h).
 \tag{7.1}
\]

This conclusion uses an identity of deterministic solution maps, followed by independence of the shifted Brownian path; it does not require a common nonexplosion event for all initial points. Conditioning integrates the exceptional set for each starting point against the current-state law, and that set has zero probability for each point by Section 5. The same reasoning applies to killed paths, retaining the event of survival before h. It gives the semigroup identity by another expectation. This establishes precisely the deterministic-time Markov property used here. A strong-Markov theorem is not silently imported or required.

The cutoff construction also gives uniqueness of the diffusion itself. Every continuous adapted solution driven by a Brownian motion must coincide pathwise with each local cutoff solution up to annular exit, because it solves the same deterministic integral equation there. Nonexplosion then makes the agreement global. Consequently any such solution is the same measurable functional of its Brownian path, and its law is fixed as well.

Set

\[
 u(\tau,z)=\mathbb E_z\int_0^\tau J_A(Z_h)\,dh,
 \qquad \Phi(t,z)=u(T-t,z).
 \tag{7.2}
\]

Joint Borel measurability follows by applying measurable time integration to the Borel solution map and then integrating over Brownian paths; positive and negative parts are integrable by (5.4). The bound and terminal value are

\[
 |\Phi(t,z)|\le\|A\|_{\rm op}F_{N,T-t}(r),\qquad
 \sup_{t,z}|\Phi(t,z)|
 \le\|A\|_{\rm op}\frac{(2sp)^{2/p}}4N^{s/p}T^{2/p},
 \qquad \Phi(T,z)=0.
 \tag{7.3}
\]

The solution class is the following: **bounded, jointly Borel functions v on `[0,T] x D`, with `v(T,z)=0` for every z, such that from every `(t,z)` the process**

\[
 v(t+h,Z_h)+\int_0^h J_A(Z_v)\,dv,
 \qquad 0\le h\le T-t,
 \tag{7.4}
\]

**is a true martingale.** No spatial derivative, origin trace, distributional extension through zero, or boundedness uniform in N is part of this definition.

The constructed Phi belongs to this class. To check it, fix `(t,z)`, write `tau=T-t`, and let `C=int_0^tau J_A(Z_h) dh`, which is integrable. Equation (7.1), first for bounded truncated sources and then by monotone convergence for f and dominated convergence for J_A, shows that the process in (7.4) is exactly `E[C|F_h]`. It is therefore a true martingale. Its values are dominated in absolute value by the finite bound in (7.3) plus `||A|| int_0^tau f`, so this is also a uniformly integrable family. The same calculation with the bounded killed source proves (6.2).

For any other v in the stated class, expectation of (7.4) at `h=T-t` gives

\[
 v(t,z)=\mathbb E_z\int_0^{T-t}J_A(Z_h)\,dh=\Phi(t,z).
\]

This proves pointwise uniqueness in the stated probabilistic class. It does not define an unspecified inverse of a singular operator on some larger space. In particular, a globally bounded punctured classical solution of (1.2), if available, belongs to this class: apply smooth Itô on annuli and let their exit times tend to infinity. Boundedness of v controls its stopped values, and (5.4) controls the source, so the stopped martingale identities pass in L1 at each deterministic pair of times. Hence such a classical solution is unique and coincides with Phi. We have not proved that the expectation is classical.

There is also a useful terminal modulus, with no hidden dependence on nu. From (7.1) and (5.4), for `h>=0` and `tau+h<=T`,

\[
 |u(\tau+h,z)-u(\tau,z)|
 \le\|A\|_{\rm op}\sup_y F_{N,h}(|y|)
 =\|A\|_{\rm op}\frac{(2sp)^{2/p}}4N^{s/p}h^{2/p}.
 \tag{7.5}
\]

Thus the zero terminal value is a uniform-in-space limit for each fixed N. This does not supply an origin extension at positive remaining time.

## 8. Independent consistency and falsification checks

**Zero diffusion.** When nu is zero, (4.1) is exactly the outward radial characteristic

\[
 Z_h=(r^p+2sp h/N)^{1/p}\theta.
\]

Its source integral gives `u(tau,z)=(theta^T A theta)F_(N,tau)(r)`, agreeing with the permitted THM-017 prerequisite. Uniqueness also holds in the punctured forward absolutely-continuous characteristic class. No zero condition is imposed on both boundaries of a finite annulus at nu=0. In remaining-time coordinates the transport velocity is inward, so a zero trace at the inner boundary would be an additional outflow condition and is generally incompatible with the characteristic solution. The positive-diffusion boundary-trace argument explicitly used nu>0. For a concrete counterexample to imposing both annular traces at nu=0, take A=I and `0<tau<N(R^p-a^p)/(2sp)`. Characteristics starting sufficiently close to the inner sphere still reach terminal time before the outer sphere, so their solution is F and their inner trace is the strictly positive number `F_(N,tau)(a)`. A zero inner trace is impossible in that class.

**Isotropic source.** For `A=a I`, rotational invariance makes `u=a U`, where `U=E integral f` is radial. For positive tau, U is strictly positive. Passing (5.1) to the global domain also gives the exact identity

\[
 U(\tau,r)=F_{N,\tau}(r)+2\nu\mathbb E_z
       \int_0^\tau\Delta F_{N,\tau-h}(|Z_h|)\,dh.
 \tag{8.1}
\]

The passage is justified because F is uniformly bounded for remaining time at most tau, the terminal stopped F converges to zero, and `|Delta F|<=Nd/2`. Thus for `nu>0` and `tau>0`, `0<U<F`. This is a direct check that the zero-diffusion radial profile is a strict supersolution, not the diffusive solution itself. For negative a the sign reverses; absolute values still obey comparison.

**Traceless source and symmetry.** Since b_N is odd, reflection of the initial point and Brownian path reflects the solution path. Since J_A is even, u is even. Orthogonal changes of coordinates and linearity in A give
`u_A(tau,Qz)=u_(Q^T A Q)(tau,z)`. Averaging over directions therefore gives the invariant linear functional

\[
 \frac1{\omega_d}\int_{S^{d-1}}u_A(\tau,r\theta)\,d\theta
 =\frac{\operatorname{tr}A}{d}U(\tau,r).
 \tag{8.2}
\]

One may verify the invariant-functional step just by sign flips and coordinate permutations: its coefficients on off-diagonal entries vanish and all diagonal coefficients agree; evaluating A=I determines the coefficient. Thus a traceless source has zero angular mean, but no pointwise positivity is asserted and no angular cancellation is used in the absolute comparison. There is no two-sided diffusive norm estimate in this report.

**Threshold, particle number, and large diffusivity.** Formula (2.3) includes `d=s+2` without a strict inequality. In `d>s+2` its lower derivative bracket is strictly positive. The coefficient `N/4` and `2sp/N` gives, respectively, `F=(1/2)[(r^p+sp tau)^(2/p)-r^2]` for N=2 and `F=(3/4)[(r^p+2sp tau/3)^(2/p)-r^2]` for N=3; direct substitution preserves (2.2). At tau=0 all potentials and diagnostics are exactly zero. Every finite positive nu, however large, is covered because diffusion enters the supersolution only through `-2nu Delta F>=0`; the collision/source bound (5.4) is independent of nu. The outer-exit control properly retains its `4nu dH` term and does not claim uniform tightness as nu tends to infinity. No assertion is made in `d<s+2`.

The independent falsification routes are the direct parabolic maximum test, the separate harmonic-power/radius-squared exit estimates, the exact radial scale calculation (5.7)--(5.8), and the isotropic strictness identity (8.1). They detect the relevant sign and factor errors without assuming classical regularity of the global expectation. The supporting exact arithmetic script checks selected threshold/strict-range parameters, N=2 and N=3, and zero time; those checks are corroboration, not the proof.

## 9. Periodic cutoff diagnostic and the initial-iid endpoint

Fix `0<R_0<R_1<1/2` and a smooth radial cutoff chi with `0<=chi<=1`, equal to one on `B_(R_0)` and zero outside `B_(R_1)`, as explicitly permitted by the Round 003 prerequisite. For `z!=0` in the embedded torus ball, set

\[
 h_{N,\nu,\tau}(z)=\chi(z)u_{N,\nu}(\tau,z),
 \qquad H_{N,\nu,\tau}(x,y)=h_{N,\nu,\tau}(x-y).
 \tag{9.1}
\]

Assign any finite value at zero and extend by zero and periodicity. The function is measurable and even, hence H is symmetric. It is an L2 kernel by (7.3). It is a separate diagnostic kernel, not a claimed classical periodic corrector. In particular, multiplying a diffusive solution by chi would create diffusion cutoff terms involving gradients, as well as the internal-transport cutoff term; no such equation error is estimated here.

Let `mu_N` be any probability densities on the unit torus with a common bound `M<infinity`, and let the N labels be iid with density mu_N. No positive-time interacting law is assumed iid. Write `K=||A||_op`. The convolution of the density with its reflection is at most M, so exactly one density factor is needed:

\[
 \|H_{N,\nu,\tau}\|_{L^2(\mu_N^2)}^2
 \le M\int_{B_{R_1}}|u_{N,\nu}(\tau,z)|^2\,dz
 \le M K^2\int_{B_{R_1}}F_{N,\tau}(|z|)^2\,dz.
 \tag{9.2}
\]

The assigned diagonal value has no effect because a bounded density is atomless. This does not make any claim about self-label traces in a generator.

For clarity, the entire centering identity is rederived. For an arbitrary real symmetric L2 kernel H, put `m=mu_N^2(H)`, `q=H_(mu_N)-m`, and `R_H=H-m-q(x)-q(y)`. Then R_H has zero conditional mean in either variable, q has mean zero, and the campaign statistic is

\[
 P_N[H]=\frac1{2N^2}\sum_{i\ne j}H(X_i,X_j)
 -\frac1N\sum_iH_{\mu_N}(X_i)+\frac m2
 =-\frac m{2N}-\frac1{N^2}\sum_iq(X_i)
 +\frac1{N^2}\sum_{i<j}R_H(X_i,X_j).
 \tag{9.3}
\]

Conditioning on a shared label proves that distinct canonical pair terms are orthogonal, and also orthogonal to the first-projection sum. Hence

\[
 \mathbb EP_N[H]=-\frac m{2N},\qquad
 \mathbb E P_N[H]^2=
 \frac{m^2}{4N^2}+\frac{\|q\|_2^2}{N^3}
 +\frac{N-1}{2N^3}\|R_H\|_2^2
 \le\frac{N-1}{2N^3}\|H\|_2^2.
 \tag{9.4}
\]

For the last inequality use `||H||_2^2=m^2+2||q||_2^2+||R_H||_2^2`; its constant coefficient comparison is `N<=2(N-1)`, valid exactly for N>=2, and its first-projection comparison is `1<=N-1`. Equality holds throughout for N=2. This confirms THM-015 in precisely the needed normalization.

For any `beta_N>0`, put `b_N=min(beta_N,1)` and `sigma_N=sqrt(N b_N)`. For any independently chosen `nu>=0` (in particular `nu=1/beta_N`), (9.2)--(9.4) imply

\[
 \mathbb E|\sigma_NP_N[H_{N,\nu,\tau}]|^2
 \le\frac{b_N(N-1)}{2N^2}M K^2
       \int_{B_{R_1}}F_{N,\tau}^2.
 \tag{9.5}
\]

There is no substitution of exact expectation-centering for mean-field centering. All deterministic bias and first-projection terms are retained. More explicitly, let

\[
 C_A=\frac{s\omega_d K R_1^{d-s}}{d-s}.
\]

Then `||h||_1<=C_A tau`, `|m|<=M C_A tau`, and `||q||_infinity<=2M C_A tau`. Their respective scaled second-moment contributions are bounded by

\[
 \frac{b_N M^2C_A^2\tau^2}{4N},\qquad
 \frac{4b_N M^2C_A^2\tau^2}{N^2}.
 \tag{9.6}
\]

To record all powers, put `ell=(2sp tau/N)^(1/p)` for positive tau and `R=R_1`. From (2.5),

\[
 \int_{B_R} F^2\le\omega_d\left[
 \frac{N^2\ell^4\min(R,\ell)^d}{16d}
 +\mathbf1_{\{\ell<R\}}s^2\tau^2
       \int_\ell^R r^{d-1-2s}\,dr\right].
 \tag{9.7}
\]

This finite-N formula also covers a core larger than the cutoff ball. For all `0<tau<=T`, `ell<=R` once `N>=2sp T/R^p`. In that range (9.7) gives constants depending only on the fixed d,s,R such that

| Range | Upper bound for the radial squared norm |
|---|---|
| `2s<d` | `C tau^2 R^(d-2s)` |
| `2s=d` | `C tau^2 [1+log(R/ell)]` |
| `2s>d` | `C N^((2s-d)/p) tau^((d+4)/p)` |

For example, the core term uses the exact identity `N^2 ell^(d+4)=(2sp)^2 tau^2 ell^(d-2s)`, so it has precisely the same exponent as the near endpoint of the tail integral. No angular-square identity for the diffusive kernel is presumed; the radial upper bound has replaced it.

Combining the table with (9.5), and using boundedness of `tau^2 |log tau|` at zero in the equality case, gives, for sufficiently large N,

\[
 \sup_{\nu\ge0}\sup_{0\le\tau\le T}
 \mathbb E|\sigma_NP_N[H_{N,\nu,\tau}]|^2
 \le C_T b_N
 \begin{cases}
 N^{-1},&2s<d,\\
 (1+\log N)/N,&2s=d,\\
 N^{-(d+2-s)/(s+2)},&2s>d.
 \end{cases}
 \tag{9.8}
\]

Here C_T depends only on `d,s,T,A,M,R_1` and the fixed cutoff bounds, and is independent of N, nu, beta_N, the chosen density with that bound, and remaining time. At tau=0 the quantity is exactly zero. T=0 is trivial and uses no logarithmic expression. Since `s<=d-2`, the exponent in the final row is positive; the displayed upper bound tends to zero for every positive beta_N sequence. The result also yields L1 and probability convergence at every deterministic sequence of remaining times and diffusivities. Both suprema in (9.8) are outside expectation. No stochastic-time supremum is estimated.

At the comparison boundary `s=d-2`, the dimension-three case is in the first row, dimension four is the logarithmic row, and dimensions at least five are in the third row with exponent `4/d`. For Haar density and traceless A, (8.2) gives `m=q=0`; the canonical coefficient in (9.4) is then exact. This observation does not convert the upper rates into lower bounds for positive diffusion.

## 10. Scope, disposition, and reproducible handoff

The bounded local assertion is **proved here in its stated probabilistic class**, with an independent reconstruction of its radial, stopped-path, and iid arguments. The proposed seed identities pass the explicit algebraic checks. Annular and global existence do not depend on an imported singular SDE theorem or an unverified classical PDE theorem. The infinite-domain passage is a proved passage of killed occupation potentials, not an assertion of uniform derivative convergence. The constructed global function is bounded and Borel, with its exact true-martingale identity; no unsupported regularity label is attached.

The following remain outside this report: ordinary background/external transport, both nonlocal response terms, the actual time-dependent backward test, the regular part of the periodic force, cutoff equation errors, evolved-law estimates, contractions, pair martingales, full singular generator passages, the limiting critical law, finite or infinite corrector closure, and the logarithmic normalization. No dynamic/full-response/full-mission inference follows from (9.8). The full-operator gap is still a uniform comparison of the genuine corrector with this diagnostic and the control of the omitted evolving-law terms. This lane allocates no canonical theorem or obligation identifiers and writes no canonical ledgers.

Supporting exact arithmetic is in `VERIFICATION_CODE/round004_diffusive_reconstruction_exact.py`, with its JSON output alongside. It uses only Python's standard library and tests algebra rather than simulating a diffusion. The proof does not depend on those sample checks. File integrity and exact input hashes are verified at sealing; the output manifest is `AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_OUTPUT_SHA256SUMS.txt`. The separate mathematical assessment of any Round 004 constructor proof belongs to the root's subsequent comparison/audit, not to this unseen-proof reconstruction.

Executed verification commands: `python3 VERIFICATION_CODE/round004_diffusive_reconstruction_exact.py` passed 432 radial/comparison checks, 1296 angular checks, 864 Lyapunov checks, 648 scale-generator checks, and 12 exponent checks, all in exact rational arithmetic. `shasum -a 256 -c AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_INPUT_SHA256SUMS.txt` passed all six input checks. `git diff --check` passed; because the new outputs are untracked, an additional direct scan verified their terminal newline, absence of trailing whitespace/control characters, and balanced display delimiters in the memorandum. No TeX was created, so no compilation was required for these outputs.

Created outputs are this memorandum, its input/output hash manifests, and the exact arithmetic script/output. The copied prerequisite files preserve their exact supplied bytes. No canonical root file, immutable input, prior report, TeX, or other worktree was edited. No commit, push, remote modification, dependency installation, or child agent was used. The final human-facing handoff contains no mathematical LaTeX; no separate response TeX/PDF is generated in this lane.
