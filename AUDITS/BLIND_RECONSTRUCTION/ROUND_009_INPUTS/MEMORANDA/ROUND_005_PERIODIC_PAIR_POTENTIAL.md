# Round 005: periodic singular pair potential and its L2 Markov evolution

2026-09-17 UTC. TASK-036 constructor: `/root/r004_diffusive_blind`.
Worktree: `/private/tmp/hocf-r005-periodic-pair-20260917`.
Branch: `codex/hocf-r005-periodic-pair`.
Base: `52bda5d0d24067b051c6fe9763f2a78e7599e593`.

**Mathematical status: PROVED_CANDIDATE / SELF_CHECKED.** This construction proves the stated bounded-diffusivity periodic pair result under the prescribed uniform background and test bounds. It includes a global off-diagonal process, its bounded Borel source potential, the requested all-N L2 bounds, the exact L2 Markov operator bound, and strong L2 passage of heat-regularized semigroups. A fresh independent hostile review is required. This author constructed the supplied Round 004 prerequisites and does not independently certify that prior work or this new construction.

The permitted inputs read are recorded in `AUDITS/ROUND_005_PERIODIC_PAIR_INPUT_SHA256SUMS.txt`: AGENTS, the frozen model, TASK-036, the sealed Round 004 reconstruction, and its sealed all-N addendum. No response-worker output, unsealed constructor report, root later theorem/state, memory, or outside source was read. The restricted task dossier governs this worker's orientation. The local radial profile is used from the sealed prerequisite and its needed derivatives are checked again below. The heat approximation and distributional divergence are derived here directly from the stated local potential; no external normalization or existence theorem is imported.

## 1. Parameters, assertion, and exact negation

The torus is `T^d=R^d/Z^d` with Haar mass one. Fix integer `d>=3`, `0<s<=d-2`, `p=s+2`, integer `N>=2`, `0<=nu<=nu_*<infinity`, and `0<=T<infinity`. The interaction g is even, periodic, smooth off zero, and has, in an embedded Euclidean ball about zero, the form

\[
 g(z)=|z|^{-s}+q(z),\qquad q\text{ smooth and even},\qquad K=-\nabla g.
 \tag{1.1}
\]

The coefficient of the local singularity is exactly one. The Fourier normalization of a particular periodic Riesz kernel is not needed: (1.1) is the hypothesis of this task, not a conclusion about an unspecified Fourier kernel. Adding a constant to g does not affect the statement.

The prescribed real vector field u_t is continuous in time, C1 in space, and periodic; its spatial derivatives are uniformly bounded. Its divergence satisfies `div u_t>=-D`, with a fixed `D>=0`. The prescribed real scalar f_t is continuous in time, C2 in space, and periodic, with uniform spatial derivative bounds. Write

\[
 L_u=\sup_{t,x}\|D u_t(x)\|_{\rm op},\quad
 H_f=\sup_{t,x}\|D^2 f_t(x)\|_{\rm op},\quad
 G_f=\sup_{t,x}|\nabla f_t(x)|.
 \tag{1.2}
\]

All are finite. Spatial derivatives are jointly measurable, as limits of difference quotients. The arguments require only that measurability and the stated spatial continuity/bounds; no stronger differentiability in time is assumed. The continuity and compact domain also bound u itself. These are hypotheses on supplied fields, possibly on a family with the same constants. They have not been established for the actual mean-field solution or backward test.

Let `E=(T^d)^2\{x=y}`. Starting at any `(t,x,y)` in `[0,T] x E`, the pair equation is

\[
 \begin{aligned}
 dX_r&=\left[u_r(X_r)+\frac1N K(X_r-Y_r)\right]dr
                   +\sqrt{2\nu}\,dB^1_r,\\
 dY_r&=\left[u_r(Y_r)+\frac1N K(Y_r-X_r)\right]dr
                   +\sqrt{2\nu}\,dB^2_r,
 \end{aligned} \tag{1.3}
\]

where the two standard d-dimensional Brownian motions are independent. Its generator on E is

\[
 L_r=\nu(\Delta_x+\Delta_y)+u_r(x)\cdot\nabla_x+u_r(y)\cdot\nabla_y
       +\frac1N K(x-y)\cdot(\nabla_x-\nabla_y).
 \tag{1.4}
\]

The source and the claimed potential are

\[
 J_r(x,y)=K(x-y)\cdot\big[\nabla f_r(x)-\nabla f_r(y)\big],\qquad
 U_N(t,x,y)=\mathbb E_{t,x,y}\int_t^T J_r(X_r,Y_r)\,dr.
 \tag{1.5}
\]

The assertion is: (1.3) has a pathwise unique global solution on `[t,T]` in E; the source in (1.5) is absolutely integrable in expectation; U_N is bounded and jointly Borel for each fixed N, has terminal value zero, and is unique in the martingale class specified in Section 6. Its squared Haar L2 norm, uniformly over time, obeys

\[
 \sup_{0\le t\le T}\|U_N(t)\|_{L^2((\mathbb T^d)^2)}^2
 \le C\begin{cases}
 1,&2s<d,\\
 1+\log N,&2s=d,\\
 N^{(2s-d)/(s+2)},&2s>d,
 \end{cases}\qquad N\ge2,
 \tag{1.6}
\]

with C independent of N and nu in the declared interval. Moreover, if `div K>=-C_0` as a measure, the two-time Markov operators satisfy

\[
 \|S_{t,a}\|_{L^2\to L^2}
 \le\exp\{(D+C_0/N)(a-t)\},\qquad 0\le t\le a\le T.
 \tag{1.7}
\]

The local hypotheses on g themselves yield some finite nonnegative C_0, as proved in Section 8. Heat-regularized operators converge strongly in L2 to these singular operators, and the singular evolution is jointly strongly continuous in `(t,a)`.

The exact negation is admissible data violating any of these existence, domain, integrability, uniqueness, norm, or passage assertions in the declared classes. The following construction and estimates exclude that negation. Nonlocal responses are absent from (1.4); no perturbed-response theorem or fluctuation theorem is included.

## 2. A fixed local chart and exact uniform profile estimates

Choose `0<R_0<R_1<R_2<1/2` so that (1.1) holds on `B_(R_2)`. In that ball write

\[
 K(z)=s|z|^{-s-2}z+k(z),\qquad k=-\nabla q,\qquad
 L_k=\sup_{B_{R_1}}\|Dk\|_{\rm op}.
 \tag{2.1}
\]

Evenness of q gives `k(0)=0`, so `|k(z)|<=L_k|z|`. Fix a nonnegative smooth radial cutoff chi, equal to one on `B_(R_0)` and zero outside `B_(R_1)`, extended periodically. For example, with `e(v)=exp(-1/v)` for v>0 and zero otherwise, use

\[
 \chi(z)=\frac{e(R_1^2-|z|^2)}
                   {e(R_1^2-|z|^2)+e(|z|^2-R_0^2)}
\]

in the local chart and extend by zero. This is smooth and supported strictly inside the embedded ball. All differentiated radial functions below are multiplied by this cutoff or evaluated inside the local chart. No torus distance function is differentiated across a cut locus.

For a function of `z=x-y` in this chart, (1.4) acts as

\[
 L_r^{\rm rel}=2\nu\Delta_z+
 \left[\frac{2s}{N}|z|^{-s-2}z+w_r(x,y)\right]\cdot\nabla_z,
 \qquad |w_r(x,y)|\le L|z|,
 \tag{2.2}
\]

where

\[
 w_r=u_r(x)-u_r(y)+\frac2N k(z),\qquad L=L_u+L_k.
\]

The factor two in both relative diffusion and internal drift follows directly from differentiating a function of x-y in the two coordinates. The estimate uses `2/N<=1` and the straight segment in the embedded lift from y to x.

Let `c=2sp` and recall the positive local profile

\[
 F_{N,\tau}(r)=\frac N4\big[(r^p+c\tau/N)^{2/p}-r^2\big]
 =s\int_0^\tau(r^p+ch/N)^{-s/p}\,dh.
 \tag{2.3}
\]

The sealed Round 004 result, or direct differentiation, gives

\[
 (\partial_\tau-2\nu\Delta-v_N\cdot\nabla)F
       =s r^{-s}-2\nu\Delta F\ge s r^{-s},
 \quad v_N=\frac{2s}{N}r^{-s-2}z,
 \quad \Delta F\le0,
 \tag{2.4}
\]

for `d>=s+2`, including equality. More explicitly, for `Q=r^p/(r^p+c tau/N)`,

\[
 \Delta F=\frac N2\left[Q^{s/p}(d+s-sQ)-d\right],
\]

and the derivative of the bracket's first term is
`(s/p) Q^(s/p-1)[d+s-(2s+2)Q]>=0` on `(0,1]`.

The drift absorption inequality is exact:

\[
 -rF_r=s^2\int_0^\tau
   \frac{r^p}{r^p+ch/N}(r^p+ch/N)^{-s/p}\,dh
 \le sF.
 \tag{2.5}
\]

Differentiating the integral in (2.3) on any annulus yields the N-independent estimates

\[
 0\le F\le s\tau r^{-s},\qquad
 |F_r|\le s^2\tau r^{-s-1},\qquad
 |F_{rr}|\le3s^2(s+1)\tau r^{-s-2}.
 \tag{2.6}
\]

For the last inequality, differentiation of F_r gives two terms with coefficients `s^2(p-1)` and `s^2(s+p)`; their sum is `3s^2(s+1)`. Thus the first two derivatives really are O(tau) on the fixed cutoff annulus, uniformly in N, rather than merely O(1). Also

\[
 F_{N,\tau}(r)\le\frac{c^{2/p}}4N^{s/p}\tau^{2/p}.
 \tag{2.7}
\]

No differentiability or equation at collision is claimed in these calculations.

## 3. A global positive barrier with all cutoff terms

Let

\[
 K_{\rm out}=\sup_{\operatorname{dist}(z,0)\ge R_0}|K(z)|,\qquad
 B_J=H_fL_kR_0^2+2G_fK_{\rm out}.
 \tag{3.1}
\]

The distance in this definition specifies a closed set only. On the inner ball, the mean-value bound for grad f gives
`|J_r|<=H_f[s r^(-s)+L_k r^2]`. Outside that ball, the source is at most `2G_f K_out`. Therefore globally on E,

\[
 |J_r(x,y)|\le H_f\chi(z)s|z|^{-s}+B_J,
 \tag{3.2}
\]

where the cutoff singular term is set to zero outside its local chart.

For explicit constants, put

\[
 C_1=\|\nabla\chi\|_\infty,\quad C_2=\|\Delta\chi\|_\infty,\quad
 V_*=sR_0^{-s-1}+LR_1,
\]

\[
 E_*=sR_0^{-s}(2\nu_*C_2+V_*C_1)
          +4\nu_*C_1s^2R_0^{-s-1},\qquad
 \alpha=1+sL,\qquad C_B=B_J+H_fE_*/\alpha.
 \tag{3.3}
\]

All constants are finite and independent of N and nu in the specified interval. The source factor H_f is not absorbed into the definition of F.

Write `B_N(t,x,y)=W_N(T-t,x-y)`, with

\[
 W_N(\tau,z)=e^{\alpha\tau}
                [H_f\chi(z)F_{N,\tau}(|z|)+C_B\tau].
 \tag{3.4}
\]

This is nonnegative, terminal-zero, and bounded for every fixed N,T. On E, the full product rule in relative coordinates is

\[
 \begin{split}
 (\partial_\tau-L_r)(\chi F)
 ={}&\chi\,[s r^{-s}-2\nu\Delta F-w_r\cdot\nabla F]\\
 &-F[2\nu\Delta\chi+(v_N+w_r)\cdot\nabla\chi]
       -4\nu\nabla\chi\cdot\nabla F.
 \end{split} \tag{3.5}
\]

The term `4 nu`, rather than `2 nu`, is the cross term from the relative Laplacian. The singular part `-2nu chi Delta F` is nonnegative. Equation (2.5) bounds the w term below by `-sL chi F`. Every remaining term is supported in the fixed annulus, where (2.6), `nu<=nu_*`, and `|v_N+w_r|<=V_*` give

\[
 (\partial_\tau-L_r)(\chi F)
 \ge\chi s r^{-s}-sL\chi F-E_*\tau.
 \tag{3.6}
\]

This remains valid outside the cutoff support, where both sides apart from their nonpositive error term vanish. Differentiating (3.4) and using (3.6),

\[
 \begin{split}
 (\partial_\tau-L_r)W_N
 &\ge e^{\alpha\tau}\big[
 H_f\chi s r^{-s}+H_f(\alpha-sL)\chi F
 +C_B+(\alpha C_B-H_fE_*)\tau\big]\\
 &\ge H_f\chi s r^{-s}+B_J\ge |J_r|.
 \end{split} \tag{3.7}
\]

Here `alpha-sL=1`, `C_B>=B_J`, and `alpha C_B-H_fE_*=alpha B_J>=0`. In backward time the sign is therefore

\[
 (\partial_t+L_t)B_N(t,\cdot)\le-|J_t|.
 \tag{3.8}
\]

No derivative in time of u or f was used. All diffusion cutoff terms are explicit. The restriction to bounded diffusivity enters E_*; this argument does not claim a constant uniform as nu_* tends to infinity.

## 4. Local construction and a noncollision estimate

First cut off K smoothly in an embedded tube around zero, setting it to zero in a smaller tube and leaving it unchanged outside. For a fixed cutoff the periodic pair drift is bounded and uniformly Lipschitz in space. Lift the equation to `R^(2d)` with periodic coefficients and subtract the continuous additive Brownian path. Picard iteration then solves a deterministic integral equation. If the bounded drift and its Lipschitz constant are B and A, successive Picard differences over a horizon H are bounded by `B A^(j-1)H^j/j!`; the summable series gives existence, and the same factorial difference argument gives uniqueness. This works equally at nu=0. It requires no singular SDE existence theorem.

Different cutoffs agree up to the first entry into the smaller collision tube by pathwise uniqueness. Their solutions therefore patch to a unique maximal process on E. The cutoff maps are Borel in initial time, terminal time, initial state, and driving continuous path: the iterations are measurable, and convergence is uniform. Exit times from open collision-excluded sets are measurable for continuous paths. Countable patching consequently produces a jointly Borel maximal map, with a cemetery convention if its lifetime is finite. The deterministic flow identity follows from uniqueness. No noncollision claim has been used at this stage.

Let `q_*=d-2>0` and define the global smooth function on E

\[
 V(x,y)=1+\chi(x-y)|x-y|^{-q_*},
 \tag{4.1}
\]

using the fixed local chart and zero cutoff extension. On `0<r<R_0`, the radial power is harmonic and

\[
 L_t V=-\frac{2s q_*}{N}r^{-s-d}
       +w_t\cdot\nabla r^{-q_*}
 \le q_* L r^{-q_*}\le q_* L V.
 \tag{4.2}
\]

The negative repulsive term is retained explicitly. On the cutoff annulus, both derivatives of `chi r^(-q_*)` are bounded and `|v_N+w_t|<=V_*`. Outside the support the generator of V is zero. Thus, for example,

\[
 C_V=q_*L+
 2\nu_*\sup_{R_0\le r\le R_1}|\Delta(\chi r^{-q_*})|
 +V_*\sup_{R_0\le r\le R_1}|\nabla(\chi r^{-q_*})|
\]

is finite, independent of N and nu in the interval, and satisfies `L_t V<=C_V V` throughout E.

Let `sigma_epsilon` be the first time after t at which the pair separation enters the radius-epsilon collision tube, with `0<epsilon<R_0`. On the stopped domain every differentiated function is smooth with bounded derivatives. Smooth Itô applied to `exp[-C_V(r-t)] V(X_r,Y_r)` gives, for any `a in [t,T]`,

\[
 \mathbb P_{t,x,y}\{\sigma_\epsilon\le a\}
 \le\frac{e^{C_V(a-t)}V(x,y)}{1+\epsilon^{-q_*}}.
 \tag{4.3}
\]

At the entry time continuity gives separation exactly epsilon. The stopped stochastic integral is a true martingale because its integrand is bounded on the collision-excluded compact set. The nonnegative stopped values justify the probability estimate; no optional-stopping limit is presumed.

As epsilon decreases to zero, the right-hand side tends to zero. The state space away from the diagonal is compact after excluding a fixed tube, and the drift is bounded there, so no other finite-lifetime obstruction is possible. Hence the maximal process exists throughout `[t,T]` and never collides, almost surely, from every prescribed off-diagonal starting point. At nu=0 this is also a deterministic construction and estimate. A singular path consequently stays a positive distance from the diagonal on each such finite time interval. The result is not a choice of dynamics starting on the diagonal.

Any other continuous adapted solution with the same Brownian paths agrees with every cutoff construction until the corresponding exit and hence agrees globally. It is the same measurable functional of its Brownian path, which also gives uniqueness in law for this prescribed initial point and time.

## 5. Source integrability and the all-N potential bound

Stop the pair before `sigma_epsilon` and apply smooth Itô to the nonnegative barrier (3.4). For `a in [t,T]`, (3.8) gives

\[
 \mathbb E_{t,x,y} B_N(a\wedge\sigma_\epsilon,
                         X_{a\wedge\sigma_\epsilon},Y_{a\wedge\sigma_\epsilon})
 +\mathbb E_{t,x,y}\int_t^{a\wedge\sigma_\epsilon}|J_r(X_r,Y_r)|\,dr
 \le B_N(t,x,y).
 \tag{5.1}
\]

The barrier is C1 in time and C2 in space on the stopped domain; terminal time at a positive separation causes no singular derivative. Noncollision makes the stopping times increase beyond each fixed finite horizon. Discarding the nonnegative first term and using monotone convergence yields

\[
 \mathbb E_{t,x,y}\int_t^T|J_r(X_r,Y_r)|\,dr
 \le B_N(t,x,y)<\infty.
 \tag{5.2}
\]

Thus (1.5) is an absolutely integrable expectation and

\[
 |U_N(t,x,y)|\le e^{\alpha(T-t)}
   [H_f\chi(x-y)F_{N,T-t}(|x-y|)+C_B(T-t)].
 \tag{5.3}
\]

In particular U_N is bounded on `[0,T] x E` for each fixed N; an explicit supremum bound is
`exp(alpha T)[H_f c^(2/p)N^(s/p)T^(2/p)/4+C_B T]`. This boundedness is not uniform in N and is not claimed to be.

Let `I_N(tau)=integral_(B_(R_1)) F_(N,tau)^2 dz`. Haar mass one gives exactly
`integral |h(x-y)|^2 dx dy=integral |h(z)|^2 dz`. Therefore

\[
 \|U_N(t)\|_2^2\le2e^{2\alpha T}
      [H_f^2 I_N(T-t)+C_B^2 T^2].
 \tag{5.4}
\]

The sealed all-N addendum supplies a direct bound for I_N valid even if its core exceeds the cutoff. For clarity its constants, independent of N, are stated here. Put `a_0=c^2/(16d)` and `R=R_1`. For `T>0`, define

\[
 A_T=\omega_d\begin{cases}
 T^2R^{d-2s}(a_0+s^2/(d-2s)),&2s<d,\\
 T^2[a_0+(s^2/p)(1+\log_+(R^p/(cT)))],&2s=d,\\
 (a_0+s^2/(2s-d))c^{-(2s-d)/p}T^{(d+4)/p},&2s>d.
 \end{cases}
 \tag{5.5}
\]

Set `A_0=0`. With `rho_N` respectively equal to `1`, `1+log N`, or `N^((2s-d)/p)`, that bound is

\[
 \sup_{0\le\tau\le T}I_N(\tau)\le A_T\rho_N,\qquad N\ge2.
 \tag{5.6}
\]

One can check its finite-N core step directly: for `ell=(c tau/N)^(1/p)`, the core term is
`a_0 tau^2 ell^(-2s) min(R,ell)^d`, and its tail is
`s^2 tau^2 1_(ell<R) integral_ell^R r^(d-1-2s) dr`, all multiplied by omega_d. When ell exceeds R, the core has the additional factor `(R/ell)^(2s)` in the first row or `(R/ell)^d` relative to the corresponding critical/supercritical core estimate. Thus (5.6) has no hidden large-N assumption. At tau=0 the profile is zero and no logarithm or negative power is evaluated.

Since `rho_N>=1`, (5.4)--(5.6) prove (1.6) with the explicit sufficient constant

\[
 C=2e^{2\alpha T}[H_f^2A_T+C_B^2T^2],
 \tag{5.7}
\]

and C=0 when T=0. Its dependence on `d,s,g,R_0,R_1,u,f,T,nu_*` is through the fixed quantities displayed above, never through N or the particular nu in its interval. No initial density factor, centering change, or iid assumption is used for this Haar norm calculation.

## 6. Measurable Markov evolution and the exact solution class

The measurable maximal path map in Section 4 satisfies its deterministic restart identity by uniqueness. Brownian independent increments therefore give, at deterministic times `t<=a<=b`,

\[
 S_{t,a}G(x,y)=\mathbb E_{t,x,y}G(X_a,Y_a),\qquad
 S_{t,a}S_{a,b}G=S_{t,b}G,
 \tag{6.1}
\]

for bounded Borel G on E. The map in all time/state arguments is Borel. The noncollision event need not be chosen simultaneously for all initial points: the exceptional set has probability zero for each starting point, and joint measurability permits its integration against a current-state law. This suffices for the conditional expectation and two-time Markov identities used here. A strong-Markov theorem is not imported.

The source integral in (1.5) is measurable in `(t,x,y)` by measurable time integration and Brownian expectation; its positive and negative parts are finite by (5.2). Define the solution class to be the bounded, jointly Borel functions v on `[0,T] x E` with `v(T)=0`, such that from every off-diagonal starting `(t,x,y)` the process

\[
 v(a,X_a,Y_a)+\int_t^a J_r(X_r,Y_r)\,dr,
          \qquad t\le a\le T,
 \tag{6.2}
\]

is a true martingale. No classical spatial regularity, collision trace, or distributional equation across the diagonal is part of this definition.

For the constructed U_N, (6.2) is the conditional expectation of the integrable random variable `integral_t^T J_r dr`. To justify this identification for the unbounded source, first use (6.1) on bounded source truncations and then use (5.2) for the positive and negative limits. Hence U_N belongs to the class. Its martingale family is uniformly integrable: it is dominated in absolute value by the fixed-N supremum of U_N plus the integrable absolute source occupation. For any other v in the class, taking expectation in (6.2) at terminal time identifies v with (1.5) at every starting point. This proves uniqueness in precisely the declared class.

Every globally bounded punctured classical solution, if supplied, lies in this class by stopped smooth Itô, bounded convergence of its stopped values, and (5.2). The expectation itself is not asserted to be classical. Interchanging x and y and the two Brownian paths leaves (1.3) and J invariant, so U_N is a symmetric pair kernel. Its terminal value is zero, and (5.3) also gives a uniform-in-state terminal limit for fixed N.

## 7. Heat-regularized flows and the exact divergence/energy factor

For now assume the measure lower bound `div K>=-C_0` with C_0 nonnegative. Section 8 verifies it from (1.1). Define the unit-torus heat kernel directly by

\[
 p_\epsilon(z)=\sum_{n\in\mathbb Z^d}(4\pi\epsilon)^{-d/2}
      \exp[-|z+n|^2/(4\epsilon)],\qquad \epsilon>0,
\]

and set `K_epsilon=p_epsilon*K`. It is smooth and odd. Positivity and unit mass of p_epsilon imply
`div K_epsilon=p_epsilon*(div K)>=-C_0`. The two-particle regularized vector field is

\[
 b_r^\epsilon(x,y)=
  (u_r(x)+K_\epsilon(x-y)/N,\ u_r(y)-K_\epsilon(x-y)/N).
\]

Its full divergence is exactly

\[
 \operatorname{div}_{x,y}b_r^\epsilon
 =\operatorname{div}u_r(x)+\operatorname{div}u_r(y)
       +\frac2N\operatorname{div}K_\epsilon(x-y)
 \ge-2(D+C_0/N).
 \tag{7.1}
\]

The second internal derivative has a plus sign because differentiating `-K(x-y)` in y changes the sign again. For a real smooth periodic test h, direct integration by parts gives

\[
 \langle h,L_r^\epsilon h\rangle
 =-\nu\int(|\nabla_xh|^2+|\nabla_yh|^2)
       -\frac12\int(\operatorname{div}b_r^\epsilon)h^2.
 \tag{7.2}
\]

Consequently a classical backward solution `partial_t v=-L_t^epsilon v`, if used to verify the sign, obeys

\[
 \frac d{dt}\|v(t)\|_2^2
 =2\nu\|\nabla_{x,y}v(t)\|_2^2
       +\int(\operatorname{div}b_t^\epsilon)v(t)^2
 \ge-2(D+C_0/N)\|v(t)\|_2^2.
 \tag{7.3}
\]

Integrating this inequality backward gives the norm exponent `D+C_0/N`, not twice that number. The following flow proof establishes the estimate for the actual regularized Markov operator without assuming a classical PDE existence theorem.

For each continuous Brownian path, the additive-noise regularized equation is an ordinary integral equation after subtraction of that path. Its spatial flow from t to a is a C1 diffeomorphism of the pair torus. Here are the required facts. Picard iteration gives global existence and uniqueness as before. Differentiating the integral equation in the initial point gives the linear variational equation with coefficient `D b_r^epsilon`; boundedness of that derivative and dominated convergence justify this differentiation even if it is only measurable in time. Its spatial continuity for each r and the same dominated argument give a continuous derivative in the initial point. Solving the integral equation backward for the fixed continuous driving path supplies the inverse. The determinant of the variational equation is therefore positive and satisfies

\[
 \det D\Phi_{t,a}^\epsilon(z)
 =\exp\left\{\int_t^a
          \operatorname{div}b_r^\epsilon(\Phi_{t,r}^\epsilon(z))\,dr\right\}
 \ge e^{-2(D+C_0/N)(a-t)}.
 \tag{7.4}
\]

This is Jacobi's determinant identity for an absolutely continuous matrix solution; it also follows by differentiating the determinant polynomial and using the inverse variational equation. Invertibility has not been inferred from a sign guess.

For every nonnegative Borel G on the pair torus, change of variables for this C1 diffeomorphism, followed by Brownian expectation, yields

\[
 \int S_{t,a}^\epsilon G\,dm
 \le e^{2(D+C_0/N)(a-t)}\int G\,dm,
 \tag{7.5}
\]

where m is pair Haar measure. Jensen's inequality for the probability kernel then gives

\[
 \|S_{t,a}^\epsilon h\|_2^2
 \le\int S_{t,a}^\epsilon|h|^2\,dm
 \le e^{2(D+C_0/N)(a-t)}\|h\|_2^2.
 \tag{7.6}
\]

Both the flow and this estimate hold at nu=0. Neither the constant nor the divergence calculation depends on epsilon; the spatial Lipschitz constants of individual regularized flows need not be uniform in epsilon.

## 8. Distributional divergence and local convergence of the heat force

Because `s+1<d`, both g and K are locally integrable at zero. The distributional divergence of the coefficient-one singular vector field can be computed by integration over a punctured ball. For a test function phi and an inner sphere of radius epsilon, its outward flux contribution to the divergence distribution is
`s epsilon^(d-s-2) integral_(S^(d-1)) phi(epsilon theta) dtheta`. Away from zero the divergence is `s(d-s-2)r^(-s-2)`. Thus, in local coordinates,

\[
 \operatorname{div}(s r^{-s-2}z)=
 \begin{cases}
 s(d-s-2)r^{-s-2},&0<s<d-2,\\
 (d-2)\omega_d\delta_0,&s=d-2.
 \end{cases}
 \tag{8.1}
\]

In the first case the displayed density is locally integrable and nonnegative, and the inner flux tends to zero. At the endpoint the ordinary punctured divergence vanishes and the inner flux tends to `(d-2)omega_d phi(0)`. This explicitly retains the Coulomb delta mass.

To globalize, use the fixed nonnegative chi and write `g=chi r^(-s)+v`, where v extends to a smooth periodic function. Product differentiation shows

\[
 \operatorname{div}K=\mathcal P+R_g,
 \tag{8.2}
\]

where P is the nonnegative finite measure obtained by multiplying the first row of (8.1) by chi, or the delta mass in the second row, and

\[
 R_g=-2\nabla\chi\cdot\nabla r^{-s}-(\Delta\chi)r^{-s}-\Delta v
\]

is a smooth bounded periodic function. The cutoff-derivative terms are supported away from zero. Choosing `C_0=||(R_g)_-||_infinity` proves the required measure lower bound. Its total mass is zero because it is the divergence of a periodic integrable field; in particular the positive singular part is not the entire periodic divergence.

Convolution with the nonnegative probability density p_epsilon proves the regularized lower bound used in Section 7. It also yields `K_epsilon -> K` in C1 on each compact set away from zero. For completeness, localize K into a smooth part agreeing with it near such a compact set and a remaining L1 part supported a positive distance away. The heat convolution of the smooth part converges with its first derivatives by the approximate-identity property. For the distant part, the periodic Gaussian formula bounds each first derivative of the heat kernel there by a polynomial in epsilon^(-1) times `exp(-c/epsilon)`, which tends to zero; multiply by its finite L1 norm. This proves the claimed local C1 convergence, not merely distributional convergence. The Gaussian approximate-identity property itself follows by unit mass and the Gaussian mass outside a fixed neighborhood tending to zero.

If a Fourier description is desired only for checking conventions, the displayed Gaussian heat kernel has character multiplier `exp(-4 pi^2 epsilon |k|^2)` by its Gaussian Fourier integral. No Riesz Fourier coefficient or source theorem is used in (8.1)--(8.2).

## 9. Passage to the singular Markov operators in L2

Fix N, nu in the prescribed interval, `t<=a`, and an off-diagonal initial point. Write `Z=(X,Y)` for the pair state in this section. Couple the heat-regularized and singular pair equations with the same Brownian paths. Almost surely, the singular path over `[t,a]` has positive minimum separation. Choose a smaller collision-excluded compact neighborhood of that path. On this neighborhood, Section 8 gives uniform convergence of K_epsilon and a common local Lipschitz bound for all sufficiently small epsilon. The background derivative bound is already uniform.

Before the regularized path leaves this neighborhood, the Brownian terms cancel in the difference equation. Gronwall's estimate gives the uniform-in-time difference bound

\[
 \sup_{t\le r\le a}|Z_r^\epsilon-Z_r|
 \le (a-t)\,\|b^\epsilon-b\|_{\rm neighborhood}
                   e^{L_{\rm neighborhood}(a-t)}\longrightarrow0.
 \tag{9.1}
\]

Here one may use consistent lifts and stop at a sufficiently small distance from the reference path; the connecting straight segments then remain away from every lifted diagonal. The right-hand side eventually prevents that exit, so (9.1) holds through a. This uses a compact set depending on the noncolliding path, which is legitimate for almost sure convergence for fixed initial data. It asserts no uniform-in-N or operator-norm convergence, and requires no uniform noncollision estimate for the regularized processes themselves.

For every continuous G on the full pair torus, bounded convergence now gives

\[
 S_{t,a}^\epsilon G(z)\longrightarrow S_{t,a}G(z)
       \quad\text{for every }z\in E.
 \tag{9.2}
\]

The diagonal has Haar measure zero. Applying bounded convergence in z to nonnegative continuous G and using (7.5) gives

\[
 \int S_{t,a}G\,dm\le e^{2(D+C_0/N)(a-t)}\int G\,dm.
 \tag{9.3}
\]

Here the pushed-forward measure is already defined by the measurable probability kernel on E. The extension of (9.3) beyond continuous functions is explicit. For an open set O, the continuous functions `min(1,j dist(z,O^c))` increase to its indicator, so (9.3) holds for O. For a Borel set B, use open supersets with Haar masses decreasing to m(B); outer regularity of Lebesgue/Haar measure gives the same bound for B. Nonnegative simple functions and monotone convergence then give (9.3) for every nonnegative Borel G. No claim about values assigned on the diagonal is needed for these Haar identities.

It follows in particular that Haar-null terminal sets have zero transition probability for Haar-almost every initial point. Consequently the singular operator is well-defined on L2 equivalence classes. For h in L2, (9.3) makes `S_(t,a)|h|^2` finite almost everywhere and independent of representatives; Jensen proves exactly (1.7). The Markov evolution identity extends from bounded Borel functions to L2 by density and the operator bounds.

There is also strong L2 convergence, not just an inequality for a candidate limit. For continuous G, (9.2) and the bound `|S^epsilon G|,|SG|<=||G||_infinity` give convergence in L2. For arbitrary h in L2, approximate h in L2 by continuous G. Uniform estimates (7.6) and (1.7) give

\[
 \|S_{t,a}^\epsilon h-S_{t,a}h\|_2
 \le2e^{(D+C_0/N)(a-t)}\|h-G\|_2
       +\|S_{t,a}^\epsilon G-S_{t,a}G\|_2.
 \tag{9.4}
\]

First let epsilon decrease to zero and then improve G. This proves strong operator convergence for each fixed N, nu, t, a. Operator-norm convergence is neither used nor asserted.

Finally the evolution is jointly strongly continuous in `(t,a)` on `0<=t<=a<=T`. For continuous G and fixed starting point in E, use a Brownian path and a reference noncolliding trajectory. A sufficiently fine fixed spatial cutoff agrees with this trajectory; its integral-equation solution depends continuously on the starting and terminal times. This follows directly from the uniform continuity of the driving Brownian path, bounded drift over small added time intervals, and the Lipschitz difference estimate on the common time interval. Nearby time pairs remain in the same collision-excluded neighborhood, so the singular solution has that same continuity. Bounded convergence gives continuity of `S_(t,a)G(z)` in time pairs, followed by L2 continuity in z. Continuous functions are dense in L2 and the operator bounds are bounded uniformly by `exp[(D+C_0/2)T]`; the same approximation as in (9.4) therefore proves the claim for every L2 input. In particular `S_(t,t)=I` strongly.

The semigroup passage in this section concerns terminal L2 data. It does not assert convergence of heat-regularized source potentials for singular sources without a separate uniform-integrability argument. The singular source potential in Section 5 was constructed directly and already has its independent L2 estimate.

## 10. Falsification checks, scope, and verification

The proof route was the stopped positive barrier and random-flow density bound. Distinct checks target its vulnerable signs and domains.

- At `d=s+2`, (2.4) still has the required Laplacian sign, while the singular Lyapunov power has exactly zero punctured Laplacian. The divergence check (8.1) restores the positive delta mass; discarding that mass would not be an exact distributional calculation.
- The product rule (3.5) retains both the annular drift term and the `4nu` cross term. The latter cannot be omitted by saying that the local radial profile is a supersolution. Equations (2.6) and (3.3) show why a finite nu_* suffices and where an unbounded-diffusivity claim would fail in this particular barrier estimate.
- For a constant test f, its gradient difference vanishes exactly, so J and U_N are zero. The comparison remains valid. Reversing f reverses J and U_N; the proof bounds absolute source occupation and never assumes a positive signed source.
- With `u=0`, q locally constant, and no cutoff in a local punctured calculation, (3.5) reduces to the sealed relative model with coefficient `2s/N` and diffusion `2nu`. For N=2 and N=3 all coefficient estimates use only `2/N<=1`; there is no asymptotic particle-number step.
- At nu=0, the pair equation is a deterministic, time-dependent flow on E. Noncollision follows from (4.3), and the Jacobian proof still gives (1.7). No two-sided zero Dirichlet condition is added to a transport outflow.
- Independent integration by parts (7.2)--(7.3) and the determinant calculation (7.4) give the same norm exponent. A density exponent `2(D+C_0/N)` becomes a norm exponent `D+C_0/N` after Jensen and the square root; changing the internal divergence sign or dropping its second copy would fail this check.
- The approximation proof first treats continuous bounded data, then extends the measure bound and uses L2 density. Almost-sure convergence of trajectories alone is not used to claim operator-norm convergence or a singular-source expectation limit.

These are self-checks of a new constructor report. The strongest assertion still requiring a fresh hostile review is the complete singular Markov/L2 passage together with the global source barrier; the report does not assign itself independent certification. No external source or private manuscript was indispensable.

The uniform C1 u and C2 f bounds remain explicit assumptions. Ordinary background transport and the periodic regular force are now included in this local pair generator; both nonlocal responses remain omitted. The result supplies neither those perturbations nor an evolved-law estimate, a pair fluctuation theorem, or the full subcritical/critical campaign resolution. No logarithmic kernel is obtained by substituting s=0.

Supporting exact algebraic checks are in `VERIFICATION_CODE/round005_periodic_pair_exact.py`, with JSON results in `VERIFICATION_CODE/round005_periodic_pair_exact_output.json`. Executing `python3 VERIFICATION_CODE/round005_periodic_pair_exact.py` passed 567 exact rational-arithmetic checks: 108 profile/derivative checks, 108 cutoff product-rule checks, 324 barrier-constant checks, and 27 norm-factor checks. They include N=2,3,17, zero remaining time, zero background Lipschitz constant, and zero diffusivity. No floating-point simulation or external dependency was used. These checks corroborate the proof and do not certify it independently.

Executed integrity verification: `shasum -a 256 -c AUDITS/ROUND_005_PERIODIC_PAIR_INPUT_SHA256SUMS.txt` passed all five copied-input checks; `git diff --check` passed. Because the new output files are untracked, they were also scanned directly for terminal newline, trailing whitespace, control characters, and balanced standalone display delimiters in the memorandum. The output manifest is `AUDITS/ROUND_005_PERIODIC_PAIR_OUTPUT_SHA256SUMS.txt`. No TeX file is created in this lane, and the final handoff contains no mathematical LaTeX; no TeX compilation is required for these Markdown/code outputs. Input and output manifests preserve the dossier and this construction separately. No canonical root file, prior sealed report, other worktree, or ledger is edited; no commit, push, dependency installation, or child agent is used. Root assigns any canonical identifiers and arranges a fresh independent review after this output is sealed.
