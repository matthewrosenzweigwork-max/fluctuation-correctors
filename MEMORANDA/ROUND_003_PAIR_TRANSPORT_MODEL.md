# Round 003: an exact singular internal-pair transport corrector

2026-09-17 UTC. TASK-025. Constructor: `/root/capacity`, Astra Max. Worktree `/private/tmp/hocf-round003-pair-transport-20260917`; input commit `2f532ccd2cb5f3d84db456be96e438f03f7e2ad2`.

Mathematical status: **PROVED_CANDIDATE** for the precisely declared transport model and the separately defined initial iid diagnostic. Audit status: **SELF_CHECKED**, requiring a separately allocated hostile review. Root proposed this solvable model; neither that proposal nor this construction is independent certification. The prior TASK-022 report is used only for its explicit iid projection identity, whose relevant content is also recalled below. No other new constructor proof was read.

The retained internal transport creates a finite-amplitude radial core, with a radius depending on both particle number and remaining time. This changes the local square-integrability calculation sufficiently to make the compactly supported diagnostic iid endpoint negligible for every `0<s<d`. The angular dependence survives: a nonzero traceless source has a positive squared norm and generally no continuous extension at collision. These conclusions apply to this zero-diffusion internal-pair model only.

## 1. Equation, source, characteristic class, and exact solution

Fix integer `d>=1`, `0<s<d`, a finite `T>=0`, `N>=2`, and a fixed real symmetric `d` by `d` matrix `A`. Write `z=r theta`, with `r=|z|>0` and `theta` on the unit sphere, and define

\[
 p=s+2,\quad c_s=2s(s+2)=2sp,\quad
 a(\theta)=\theta^T A\theta,\quad \tau=T-t.
\]

The equation is exactly

\[
 (\partial_t+v_N(z)\cdot\nabla_z)\Phi_N=-J(z),\qquad
 v_N(z)=\frac{2s}{N}|z|^{-s-2}z,
 \quad J(z)=s|z|^{-s}a(\theta),
 \quad \Phi_N(T,z)=0. \tag{1.1}
\]

The factor two in the transport is essential. For a relative-coordinate pair kernel, `(grad_x-grad_y)Phi(x-y)=2 grad_z Phi(z)`, so this is precisely the internal `B/N` term for the declared singular force `K(z)=s z |z|^(-s-2)`. For `f(x)=x^T A x/2`, the source is also exact: `(grad f(x)-grad f(y)).K(x-y)=s r^(-s) theta^T A theta`. The quadratic test is local Euclidean data and is not asserted to be a periodic backward test.

Uniqueness is asserted in the following characteristic class: the function is finite at every `t in [0,T]`, `z!=0`; on every forward characteristic from such a point to time `T`, its composition with that characteristic is absolutely continuous, has derivative `-J` almost everywhere, and has terminal value zero. No value, characteristic boundary condition, or differential equation at `z=0` belongs to this class. The solution constructed below is in fact smooth on the punctured spatial domain, with the stated terminal value.

Along a forward characteristic the direction stays fixed and

\[
 \dot r=\frac{2s}{N}r^{-s-1},\qquad
 \frac d{dh}r^p=\frac{c_s}{N},\qquad
 Z_h(z)=\left(r^p+\frac{c_s h}{N}\right)^{1/p}\theta.
 \tag{1.2}
\]

This outward characteristic exists to every finite forward time and never meets zero. Integrating the terminal condition along it gives uniquely

\[
 \Phi_N(t,z)=s a(\theta)\int_0^\tau
       \left(r^p+\frac{c_s h}{N}\right)^{-s/p}dh
 =a(\theta)F_{N,\tau}(r), \tag{1.3}
\]

\[
 \boxed{\quad
 F_{N,\tau}(r)=\frac N4
       \left[\left(r^p+\frac{c_s\tau}{N}\right)^{2/p}-r^2\right].
 \quad} \tag{1.4}
\]

One can check the coefficient directly without a fractional-power antiderivative: along the radius, `dh=N r^(s+1) dr/(2s)`, so `s r^(-s) dh=(N/2) r dr`. Its integral is `N/4` times the difference of the squared endpoint radii. This also checks the positive sign for a positive source with zero terminal value.

For an independent direct differential check, put `W=r^p+c_s tau/N`. Then

\[
 \partial_\tau F=sW^{-s/p},\qquad
 \partial_r F=\frac N2(r^{s+1}W^{-s/p}-r).
\]

Therefore

\[
 -\partial_\tau F+\frac{2s}{N}r^{-s-1}\partial_rF
 =-s r^{-s}. \tag{1.5}
\]

The radial transport does not differentiate `a(theta)`, so (1.5) proves (1.1). At `tau=0` the formula is zero for every nonzero `z`. Conversely, integrating along (1.2) proves that any member of the specified characteristic class equals (1.3). There is no implicit smooth extension or uniqueness assertion at coincidence.

The exact assertion is this formula and uniqueness, together with the bounds proved below for every stated parameter. Its negation is one admissible parameter, characteristic-class solution, or claimed bound violating them. The characteristic integration and explicit inequalities below exclude that negation within this declared model.

## 2. Core radius and sharp pointwise bounds

For `tau>0`, define the radius and dimensionless profile

\[
 \ell=\left(\frac{c_s\tau}{N}\right)^{1/p},\qquad
 H_s(u)=(1+u^p)^{2/p}-u^2,\qquad
 F_{N,\tau}(r)=\frac N4\ell^2 H_s(r/\ell).
 \tag{2.1}
\]

Put `alpha=2/p`, `gamma=s/p`, and `h_s=2^(2/p)-1`. All are positive, `alpha+gamma=1`, and `0<h_s<1`. The integral and derivative identities

\[
 H_s(u)=\alpha\int_0^1(u^p+v)^{-\gamma}dv,
 \qquad
 H_s'(u)=2u\left[\left(\frac{u^p}{1+u^p}\right)^{\gamma}-1\right]<0
 \quad(u>0)
 \tag{2.2}
\]

show that `H_s` decreases from one. Consequently, on the core,

\[
 h_s\frac N4\ell^2\le F_{N,\tau}(r)\le\frac N4\ell^2
 \qquad(0<r\le\ell). \tag{2.3}
\]

For `r>=ell`, bounding the integral in (2.2) at its two endpoints gives

\[
 s\,2^{-s/p}\tau r^{-s}
 \le F_{N,\tau}(r)\le s\tau r^{-s}. \tag{2.4}
\]

The upper bound in (2.4) holds for every `r>0` directly from (1.3). These bounds hold on every fixed ball and in fact on the entire punctured space. They are bounds for the positive radial amplitude: the correct signed statement is `Phi_N=a(theta)F`, and absolute-value bounds multiply by `|a(theta)|`. No direction-independent positive lower bound is claimed when the angular factor can vanish.

The core amplitude is exactly its radial limit

\[
 F_0:=\lim_{r\downarrow0}F_{N,\tau}(r)
 =\frac{c_s^{2/p}}4 N^{s/p}\tau^{2/p}. \tag{2.5}
\]

For each fixed positive ball radius, the essential supremum of `|Phi_N|` is exactly `F_0 ||A||_op`. Thus boundedness for fixed `N,t` is not a uniform smooth or supremum bound as N increases. For fixed positive `r` and fixed `tau`, expansion of (1.4) gives

\[
 F_{N,\tau}(r)=s\tau r^{-s}
      -\frac{s^3\tau^2}{N}r^{-2s-2}
      +O_s\left(\frac{\tau^3}{N^2}r^{-3s-4}\right)
 \tag{2.6}
\]

as `tau/(N r^p)` tends to zero. This far-field expansion is not uniform across the core. It checks the repulsive sign: retaining the internal transport decreases the integrated source relative to the static approximation `tau J`.

## 3. Coincidence, angular sign, and the terminal endpoint

For `tau>0`, the directional limit at coincidence is `F_0 theta^T A theta`. It is independent of direction if and only if `A` is a scalar matrix. Hence a nonscalar symmetric matrix admits no continuous extension of this solution at zero. In particular, a nonzero traceless matrix in dimension at least two has positive and negative directions and has this discontinuity. Dimension one has no nonzero traceless symmetric matrix.

For an isotropic matrix `A=a I`, a continuous extension exists with value `a F_0`. It is at least twice continuously differentiable in space for each fixed `tau>0`. Indeed,

\[
 F_{N,\tau}(r)=F_0-\frac N4 r^2
    +\frac{N}{2p}\ell^{-s}r^{s+2}
    +O_s(N\ell^{-2s-2}r^{2s+4})
 \quad(r/\ell\to0), \tag{3.1}
\]

and the second derivatives of the first nonpolynomial remainder tend to zero like `r^s`. The Hessian of the isotropic extension at zero is `-a N I/2`. This extension need not be smooth: the nonzero `r^(s+2)` term limits its higher regularity unless that radial power is a smooth polynomial power. In particular, when `s` is a positive even integer it is smooth for fixed `tau>0`; a smooth extension is not asserted for general s. Even in the isotropic case, the separate source and transport coefficients are singular at zero, so (1.1) is still asserted only on the punctured domain.

For nonscalar A, the leading angular term also shows why a positive-diffusion extension is substantive. Let `A_0=A-(tr A/d)I` and `a_0(theta)=theta^T A_0 theta`. On the punctured domain, the homogeneous harmonic polynomial `z^T A_0 z=r^2 a_0(theta)` gives `Delta_S a_0=-2d a_0`. Hence the classical punctured Laplacian of the leading expansion is

\[
 \Delta_z\Phi_N
 =-\frac{2dF_0}{r^2}a_0(\theta)
   -\frac N2\operatorname{tr}A
   +O_{s,A}(N\ell^{-s}r^s)
 \quad(r/\ell\to0). \tag{3.2}
\]

This computation is on annuli bounded away from zero; it does not assert a distributional extension, a singular Itô formula, or passage of a regularization through the origin. It exhibits an omitted term which is not controlled merely by saying that diffusivity is small.

At `tau=0`, set the kernel to zero everywhere, including at zero when a value is needed for a diagnostic. For fixed N, (2.5) shows uniform convergence to zero on every punctured ball as `tau` decreases to zero; the limit through punctured points at the terminal collision corner is therefore zero. This does not create continuity at zero at an earlier time for a nonscalar A. In the isotropic case the extended collision value has a time derivative proportional to `tau^(-s/p)` near zero, so no time-smooth extension across that corner is inferred.

## 4. Exact local square norm and all three regimes

Let `omega_d` be the surface area of the unit sphere and define

\[
 Q(A):=\int_{S^{d-1}}(\theta^T A\theta)^2d\theta
 =\frac{\omega_d}{d(d+2)}
       \big[(\operatorname{tr}A)^2+2\operatorname{tr}(A^2)\big].
 \tag{4.1}
\]

For completeness, rotation and sign symmetry give normalized moments `E theta_i^4=3/[d(d+2)]` and `E theta_i^2 theta_j^2=1/[d(d+2)]` for distinct indices. To obtain them, rotation of `(theta_1+theta_2)/sqrt(2)` gives a ratio three between these two moments, and expanding `(sum theta_i^2)^2=1` determines their common normalization. Diagonalizing A then yields (4.1). The dimension-one formula follows directly from the two-point unit sphere. Thus `Q(A)>0` for every nonzero symmetric A, even when its trace is zero.

For every `R>0`, `tau>0`, put `L=R/ell`. Polar integration gives the exact formula

\[
 \|\Phi_N(t,\cdot)\|_{L^2(B_R)}^2
 =\frac{Q(A)N^2\ell^{d+4}}{16}\,I_{d,s}(L),\qquad
 I_{d,s}(L)=\int_0^L H_s(u)^2u^{d-1}du. \tag{4.2}
\]

This proves finite local square norm at every finite N and time for all `0<s<d`, regardless of the bare kernel's L2 threshold. At `tau=0` the norm is zero and no division by ell is used.

Here are explicit sufficient two-sided constants. For `0<L<=1`,

\[
 \frac{h_s^2}{d}L^d\le I_{d,s}(L)\le\frac1dL^d. \tag{4.3}
\]

For `L>=1`, set `delta=d-2s` and

\[
 J_\delta(L)=\int_1^L u^{\delta-1}du
 =\begin{cases}(L^\delta-1)/\delta,&\delta\ne0,\\
 \log L,&\delta=0.\end{cases}
\]

Then (2.3)–(2.4) give

\[
 \frac{h_s^2}{d}+\alpha^2 2^{-2\gamma}J_\delta(L)
 \le I_{d,s}(L)
 \le\frac1d+\alpha^2 J_\delta(L). \tag{4.4}
\]

These inequalities quantify all transitions without assuming that the core lies inside the fixed ball. In particular, if `ell>=R`, the squared norm is comparable, with constants depending only on d and s, to

\[
 Q(A)N^2\ell^4R^d
 =Q(A)c_s^{4/p}N^{2s/p}\tau^{4/p}R^d. \tag{4.5}
\]

The exact prefactor bounds for the first expression are `h_s^2/(16d)` and `1/(16d)`.

If `ell<=R`, (4.4) yields the following sharp orders:

| Range | Squared local norm, up to positive constants depending only on d and s |
|---|---|
| `2s<d` | `Q(A) tau^2 R^(d-2s)` |
| `2s=d` | `Q(A) tau^2 [1+log(R/ell)]` |
| `2s>d` | `Q(A) N^((2s-d)/(s+2)) tau^((d+4)/(s+2))` |

For A=0 all expressions are zero. For nonzero A the comparisons are two-sided. Explicit dimensionless comparison constants before the factor in (4.2) can be read from (4.4): when `delta>0`, compare `I(L)` with `L^delta` using lower constant `min(h_s^2/d,alpha^2 2^(-2gamma)/delta)` and upper constant `max(1/d,alpha^2/delta)`; when `delta=0`, compare with `1+log L` using the corresponding minima and maxima without division by delta; when `delta<0`, lower and upper constants are `h_s^2/d` and `1/d+alpha^2/(2s-d)`.

The orders are also exact asymptotic powers. As `L` tends to infinity, `H_s(u)~alpha u^(-s)`, so

\[
 I_{d,s}(L)\sim\frac{\alpha^2}{d-2s}L^{d-2s}\quad(2s<d),
 \qquad I_{d,s}(L)\sim\alpha^2\log L\quad(2s=d). \tag{4.6}
\]

For `2s>d`, it converges to the finite strictly positive integral
`I_(d,s)(infinity)=integral_0^infinity H_s(u)^2 u^(d-1) du`. Thus for fixed `R,tau>0` and N tending to infinity, the subcritical norm tends to

\[
 \frac{Q(A)s^2\tau^2 R^{d-2s}}{d-2s}, \tag{4.7}
\]

the critical norm is asymptotic to `Q(A)s^2 tau^2 log(R/ell)`, and the supercritical norm is asymptotic to

\[
 \frac{Q(A)c_s^{(d+4)/p}I_{d,s}(\infty)}{16}
       N^{(2s-d)/p}\tau^{(d+4)/p}. \tag{4.8}
\]

For fixed N and time approaching the terminal time, the same small-core bounds show convergence of the local square norm to zero. In the critical row, `tau^2 log(1/tau)` tends to zero. All statements concern local spatial L2, not a supremum over a stochastic time process.

## 5. Isotropic, traceless, small-N and sign checks

For `A=a I`, the angular factor is constant and `Q(A)=omega_d a^2`. The solution is `a F`; for positive a it is positive, while for negative a its sign reverses. The transport itself remains outward because its sign is fixed by the prescribed repulsive K, independently of A.

In dimension two, take the nonzero traceless matrix `A=diag(1,-1)`. Its angular factor is `cos(2theta)`, its angular average is zero, and `Q(A)=pi`. The directional collision limits along the two axes are `F_0` and `-F_0`. Its square norm is therefore nonzero in every positive-time ball. A vanishing angular mean cannot be used to discard this mode. More generally a traceless matrix has `Q(A)=2 omega_d tr(A^2)/(d(d+2))`.

At `N=2`, (1.4) reads one half times `[(r^p+sp tau)^(2/p)-r^2]`; at `N=3`, it reads three quarters times `[(r^p+2sp tau/3)^(2/p)-r^2]`. Differentiating each expression gives (1.5) with precisely its corresponding `2s/N` coefficient. At `tau=0`, the derivative with respect to remaining time is `J`, confirming the zero-terminal corrector sign. These are exact analytic checks rather than numerical evidence.

The new threshold comparison is a consequence of retaining the internal transport, not an assertion that the bare Riesz pair had finite variance. The profile tends to `s tau r^(-s)` at fixed nonzero separation as N grows, yet each finite-N profile is bounded in radius. These limits are not uniform near the shrinking core.

## 6. A separate periodic diagnostic kernel and its cutoff equation

Choose fixed radii `0<R_0<R_1<1/2` and a fixed smooth radial function `chi` on Euclidean space with `0<=chi<=1`, equal to one on `B_(R_0)` and zero for `|z|>=R_1`. Its support lies compactly inside the embedded open torus ball of radius one half. A fully specified permissible choice is `chi(z)=psi(|z|^2)`, where

\[
 e(u)=\begin{cases}e^{-1/u},&u>0,\\0,&u\le0,\end{cases}\qquad
 \psi(v)=\frac{e(R_1^2-v)}{e(R_1^2-v)+e(v-R_0^2)}.
 \tag{6.1}
\]

This function is one for `v<=R_0^2`, zero for `v>=R_1^2`, and smooth with all derivatives zero at the outer edge. Its support is the closed ball of radius `R_1`, strictly inside the embedded open ball of radius one half.

For `z` in that embedded ball define `h_(N,tau)(z)=chi(z) Phi_N(T-tau,z)` for `z!=0`, assign any finite value at zero, and extend by zero and periodicity to the torus. Define the symmetric pair test

\[
 \mathcal H_{N,\tau}(x,y)=h_{N,\tau}(x-y). \tag{6.2}
\]

The symmetry follows from the even radial cutoff and `a(-theta)=a(theta)`. Its support is an explicitly prescribed neighborhood of the torus diagonal. It is an L2 test kernel for every finite N and time. For an anisotropic A it can be discontinuous on that diagonal; this is permitted for the iid L2 identity below. No smooth torus corrector is being silently constructed.

If its equation is inspected on the punctured support, multiplication by the cutoff produces the additional term

\[
 (\partial_t+v_N\cdot\nabla)(\chi\Phi_N)
 =-\chi J+(v_N\cdot\nabla\chi)\Phi_N,
 \qquad
 v_N\cdot\nabla\chi=\frac{2s}{N}r^{-s-1}\chi'(r).
 \tag{6.3}
\]

The extra source is supported in the fixed annulus between the cutoff radii. By (2.4), its absolute value is bounded by

\[
 \frac{2s^2\tau}{N}\|A\|_{\mathrm{op}}
       \|\chi'\|_\infty R_0^{-2s-1}. \tag{6.4}
\]

No annular term is omitted in (6.3). The diagnostic use below depends only on (6.2) as an L2 kernel, not on claiming it solves the full pair backward equation.

## 7. Initial iid endpoint for bounded-density preparations

Let `mu` be a probability density on the torus with `M=||mu||_infinity<infinity`, fixed independently of N, and let the initial labels be iid with that law. A sequence of densities with a common bound M obeys the same estimates. There is no assumption here that the positive-time interacting law is iid. Put `b_N=min(beta_N,1)` and `sigma_N=sqrt(N b_N)` with every `beta_N>0`.

The squared kernel norm is

\[
 \|\mathcal H_{N,\tau}\|_{L^2(\mu^2)}^2
 =\int_{\mathbb T^d}|h_{N,\tau}(z)|^2
     \left[\int\mu(y+z)\mu(y)dy\right]dz
 \le M\|h_{N,\tau}\|_2^2
 \le M\|\Phi_N\|_{L^2(B_{R_1})}^2. \tag{7.1}
\]

Only one factor M is required because the other density integrates to one. Bounded density is atomless, so the arbitrary value assigned on the diagonal has no effect on the iid statistic or its projections.

The frozen statistic is mean-field centered, with denominator `N^2` and its factor one half. For any symmetric L2 kernel H, write `m=mu^2(H)`, `q=H_mu-m`, and `r=H-m-q(x)-q(y)`. The exact iid decomposition is

\[
 P_N[H]=-\frac{m}{2N}-\frac1{N^2}\sum_iq(X_i)
           +\frac1{N^2}\sum_{i<j}r(X_i,X_j).
\]

Conditioning on shared labels makes all distinct canonical pair terms orthogonal, and also makes them orthogonal to the first-projection sum. Hence, as proved in the sealed TASK-022 report,

\[
 \mathbb E P_N[H]^2
 =\frac{m^2}{4N^2}+\frac{\|q\|_2^2}{N^3}
             +\frac{N-1}{2N^3}\|r\|_2^2
 \le\frac{N-1}{2N^3}\|H\|_2^2. \tag{7.2}
\]

This assertion uses no value of a self-label trace. Applying it to (6.2) gives the rigorous diagnostic bound

\[
 \boxed{\quad
 \mathbb E|\sigma_NP_N[\mathcal H_{N,\tau}]|^2
 \le\frac{b_N(N-1)}{2N^2}M\|\Phi_N\|_{L^2(B_{R_1})}^2.
 \quad} \tag{7.3}
\]

All centering contributions are included, even for nonuniform mu and for an isotropic source. They can be bounded separately: from the global bound `F<=s tau r^(-s)`,

\[
 \|h_{N,\tau}\|_1\le C_A\tau,\qquad
 C_A=\frac{s\omega_d\|A\|_{\mathrm{op}}R_1^{d-s}}{d-s}.
\]

Therefore `|m|<=M C_A tau` and `||q||_infinity<=2M C_A tau`. The scaled squared bias is at most `b_N M^2 C_A^2 tau^2/(4N)`, and the scaled first-projection variance is at most `4b_N M^2 C_A^2 tau^2/N^2`. No exact expectation-centering has been substituted for the frozen one.

For sufficiently large N depending only on `s,T,R_1`, all `0<tau<=T` have `ell<=R_1`. Combining (7.3) with Section 4 gives

| Range | Upper bound for the squared L2 iid endpoint, with fixed-data constants |
|---|---|
| `2s<d` | `C b_N tau^2/N` |
| `2s=d` | `C b_N tau^2 [1+log(R_1/ell)]/N` |
| `2s>d` | `C b_N tau^((d+4)/(s+2)) N^(-(d+2-s)/(s+2))` |

Here C may depend on `d,s,A,M,R_0,R_1` and the fixed cutoff, but not on N, temperature, or the indicated positive remaining time. At zero remaining time the endpoint is exactly zero. In particular,

\[
 \sup_{0\le\tau\le T}\mathbb E|\sigma_NP_N[\mathcal H_{N,\tau}]|^2
 \le C_T b_N\begin{cases}
 N^{-1},&2s<d,\\
 (1+\log N)/N,&2s=d,\\
 N^{-(d+2-s)/(s+2)},&2s>d,
 \end{cases} \tag{7.4}
\]

for sufficiently large N. In the critical row this follows because `tau^2 log(1/tau)` is bounded and tends to zero at zero. The supremum is outside the expectation; no stochastic supremum estimate is asserted. The exponent in the last row is positive because `s<d`. Thus this diagnostic endpoint tends to zero in L2, and hence in L1 and probability, for every `0<s<d`, every positive temperature sequence, and every deterministic remaining-time sequence in the fixed interval.

The powers cannot be dismissed as an angular-average cancellation. For Haar mu and a radial cutoff, a traceless nonzero A gives `m=q=0`, so (7.2) is an equality with its canonical coefficient. The kernel square norm is bounded below by the local norm on `B_(R_0)` and above by that on `B_(R_1)`. At any fixed positive remaining time, the three rows of the table therefore give two-sided asymptotic orders, including the factor `b_N`, for this nonzero traceless diagnostic. The diagonal discontinuity does not obstruct its initial iid L2 definition.

## 8. Omitted terms and the first missing full-operator estimate

This calculation retains only the declared singular internal force divided by N and the source from a static quadratic test. It omits all of the following:

- The pair diffusion. For a relative-coordinate test it is `nu(Delta_x+Delta_y)=2nu Delta_z`. Formula (3.2) shows that this term requires control near coincidence; it cannot be added by an unproved continuity argument.
- Local background and external transport. Acting on a relative-coordinate test, the ordinary pair transport is `(u(x)-u(y)).grad_z`, where `u=b+K*mu`; a general full solution can depend on both coordinates separately.
- Both nonlocal background response terms `R_x+R_y`, with the evolving reference density. They have not been estimated for this singular, angularly discontinuous kernel.
- The regular part of the periodic force relative to the local Euclidean singular force, and the difference between the actual time-dependent backward test/source and the prescribed static quadratic source.
- The fixed cutoff's annular source in (6.3), if the cutoff diagnostic is used as an approximate equation solution.

The endpoint bound also says nothing about the evolved-law cubic term, lower contractions, pair martingale, cross bracket, or singular generator passage. None of these can be transferred from an initial iid test by the present calculation.

On a punctured region where every expression is classically defined, the full operator applied to the cutoff profile has the residual

\[
 \begin{split}
 \mathcal R_N={}&J_{f_N}-\chi J
 +(v_N\cdot\nabla\chi)\Phi_N
 +(\mathcal A_x+\mathcal A_y)(\chi\Phi_N)+(R_x+R_y)(\chi\Phi_N)\\
 &+\frac1N(B_{\mathrm{periodic}}-B_{\mathrm{singular}})(\chi\Phi_N).
 \end{split} \tag{8.1}
\]

Here the operators `mathcal A_x+mathcal A_y` denote the ordinary full local background transport and diffusion, distinct from the fixed source matrix A. The identity is not asserted distributionally across a collision; regularized kernels and a proved uniform passage would be needed there.

The first open full-operator line is a uniform solution/comparison estimate for the zero-terminal equation driven by this residual, including the diffusion and both response terms at the shrinking core. For example, if `Psi_N` denotes a genuine full pair corrector and the initial law is still iid with density mu, a sufficient endpoint comparison would be

\[
 \sqrt{\frac{b_N}{N}}\,
 \|\Psi_N(0)-\mathcal H_{N,T}\|_{L^2(\mu^2)}\longrightarrow0,
 \tag{8.2}
\]

because (7.2) would then transfer the endpoint estimate. This is a concrete missing sufficient bound, not a bound proved in this report. In a cutoff construction it would need quantitative uniformity in N and the cutoff and an actual comparison with the singular problem. If L2 is unavailable, another fully justified fluctuation-scale probability or L1 comparison is required. A full fluctuation theorem would additionally need the evolved-law and martingale controls listed above.

Zero diffusivity is part of this diagnostic equation for every N. The arbitrary positive temperature sequence in (7.3)–(7.4) appears only through the requested endpoint scaling; it does not turn the toy profile into the positive-diffusivity corrector for that sequence. No claim is made about the microscopic critical law, finite corrector truncation, the logarithmic case, or any singular campaign gate. The outcome is a proved mechanism within a precisely solved model, pending hostile review.

## 9. Verification, sealed inputs, and handoff

The supplied `AUDITS/ROUND_003_PAIR_TRANSPORT_INPUT_SHA256SUMS.txt` was verified before construction and again at sealing. Its SHA-256 is `eeb47506a5955d48f43376ca61d7d3cbdc1246d350f2f2d64a13ef0685be6870`; its entries are:

- TASK-025: `7a12a5fa8f6cc9d4f3047743e136019c5f240605adec85e6f88681300cfb87f9`.
- Sealed TASK-022 report: `9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4`.

The frozen model was also read, with SHA-256 `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57`. Administrative instructions were read in `AGENTS.md` and `README_FIRST.md`. One initial task-file lookup used a shorter filename that did not exist; the manifest identified the correct `TASK-025_ROUND003_PAIR_TRANSPORT_MODEL.md`, which was then read and verified.

Mathematical verification is the complete characteristic proof, direct PDE substitution, explicit two-sided profile integrals, angular fourth-moment calculation, isotropic/traceless tests, N=2 and N=3 substitutions, terminal-limit check, cutoff product rule and exact iid projection estimate above. No numerical simulation, imported source theorem, or computational package is used as proof.

Executed checks: `python3 scripts/verify_campaign.py` passed; input-manifest verification passed; `git diff --check` passed; the new report was separately scanned for control characters, trailing whitespace, terminal newline and balanced display delimiters. These integrity checks are not independent mathematical certification. The adjacent `ROUND_003_PAIR_TRANSPORT_MODEL_SHA256SUMS.txt` records the final report hash and relevant input hashes after sealing.

Created outputs are this memorandum and its adjacent hash manifest. No submitted prerequisite, canonical ledger, historical input, previously issued report, or TeX file was edited. No commit, push, remote change, dependency installation, or child worker occurred. Root alone obtains the separate hostile review, assigns canonical identifiers, and integrates any promotion.
