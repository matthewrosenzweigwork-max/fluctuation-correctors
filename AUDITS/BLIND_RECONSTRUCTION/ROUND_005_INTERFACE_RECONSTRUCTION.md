# TASK043 — sealed statement-only reconstruction of the THM025 interface

**Disposition: PASS for the claimed interface and initial endpoint, conditional on the explicitly supplied analytic modules.** No load-bearing incompatibility in THM025 was found. This report independently reconstructs the composition, its representative and measurability interfaces, the homogeneous reference/test, and the initial iid calculation. It does not certify the undisclosed proofs of THM021 or THM023. In particular, the singular base-process existence, source-occupation estimate, and singular Haar-L2 propagation in THM023 remain accepted hypotheses of this review.

The only wording qualification is that “symmetric Markov evolution” in THM024 must mean covariance under exchange of the two coordinates. Haar self-adjointness is neither supplied by THM023 nor needed for the composition, and would be false for the general allowed transport. The proof below establishes the needed exchange covariance explicitly.

## 1. Input boundary, assertion, and negation

The worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r005-interface-blind-20260917`, on `codex/hocf-r005-interface-blind`, created from the supplied published commit `52bda5d0d24067b051c6fe9763f2a78e7599e593`. The eight permitted files were copied from the assigning worktree and checked against its supplied SHA-256 manifest before mathematical work. The input manifest is `ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt`. The task, AGENTS, frozen Round 001 model, and the five theorem cards are the only repository document inputs read. No root interface proof, other report, state/history document, memory, README, orchestration document, or external source was read. The specific TASK043 read boundary overrides the broader orientation instructions for this isolated review. No canonical ledger was edited, and no commit, push, dependency installation, or child-agent delegation was made.

The primary assertion is the conjunction of the prescribed-data and homogeneous-data conclusions of THM025: for every fixed admissible dimension, exponent, finite horizon and bounded diffusivity interval, every prescribed family with the stated uniform density/transport/test bounds admits the full bounded Borel probabilistic pair inverse, its Haar-L2 norm has the stated order, and its mean-field-centered pair statistic satisfies the stated initial iid bound. The homogeneous reference and displayed Fourier test satisfy the hypotheses, uniformly over the indicated temperature range.

Its logical negation is that there is at least one admissible parameter tuple or uniformly bounded admissible data family, satisfying the explicit analytic prerequisites, for which an interface fails, the inverse fails to exist or be unique in its stated class, a norm or initial second-moment estimate fails with a constant of the prescribed dependence, or the homogeneous reference/test fails its defining equation or uniform bounds. A failure of an undisclosed proof of a prerequisite module is not itself established or excluded by this interface review.

Throughout, time-continuous C1 and C2 data are understood in their stated spatial function-space topology. The argument below also identifies the joint measurability actually used. Uniqueness of the pointwise martingale inverse is for **every deterministic starting time and off-diagonal state**, as in the supplied base-process module; it is not uniqueness only under one initial law. “Symmetric” refers to exchanging the two slots, not reversibility.

### Input/source preflight

| Input | Accepted or reconstructed use |
|---|---|
| Frozen Round 001 model | Unit Haar volume; characters `exp(2 pi i k.x)`; `K=-grad g`; noise `sqrt(2 nu)`; mean-field equation; ordered distinct labels and denominator `N^2`; `P_N=U_2/2`; iid scale. |
| THM015 | Its exact second-moment identity is reconstructed in Section 7, including spatial atoms and the sharp finite-N coefficient. No evolved-law use is made. |
| THM021, lines 5–17 | The finite-measure divergence and L1 force are explicit hypotheses. Their response formulas, representative independence, norm bounds, and time interface are checked directly below. |
| THM023, lines 5–16 | The singular auxiliary pair process, bounded absolute source potential, quantitative source estimate, Haar-L2 extension, and singular strong continuity are accepted analytic hypotheses. Their applicability to the frozen Fourier kernel and their compatibility with the response are reconstructed. |
| THM024, lines 5–24 | The abstract conclusion is rederived by an explicit Volterra series and the iid calculation; the statement is not merely cited as compatibility proof. |
| THM025 | The exact target and excluded gates. |

No literature claim, novelty claim, or unverified external citation is used. The frozen Fourier normalization is treated as the definition and checked against the required local singularity by an elementary heat-kernel calculation.

## 2. The frozen Fourier kernel meets the local kernel hypothesis

Write

\[
\alpha=\frac{d-s}{2},\qquad
c_{d,s}=\pi^{s-d/2}\frac{\Gamma(\alpha)}{\Gamma(s/2)},\qquad
A_{d,s}=\frac{2^{d-s}\pi^{d/2}}{\Gamma(s/2)}.
\]

Let

\[
H_t(z)=\sum_{m\in\mathbb Z^d}(4\pi t)^{-d/2}
 \exp\!\left(-\frac{|z+m|^2}{4t}\right).
\]

Integrating the periodized Gaussian against a torus character gives Fourier coefficient `exp(-4 pi^2 t |k|^2)`: this is the Euclidean Gaussian integral after tiling space by the unit cells. Hence the zero-mean L1 kernel

\[
\widetilde g_s(z)=A_{d,s}\int_0^\infty t^{\alpha-1}(H_t(z)-1)\,dt
\]

has, for nonzero k, Fourier coefficient

\[
A_{d,s}\frac{\Gamma(\alpha)}{(4\pi^2|k|^2)^\alpha}
 =c_{d,s}|k|^{s-d}.
\]

The L1 integral is justified near zero by `||H_t-1||_1<=2` and `alpha>0`; at large time the nonconstant heat modes decay exponentially. Thus this is the frozen Fourier kernel, with no unspecified additive constant.

For `|z|<1/4`, subtract the Euclidean Gaussian contribution. The identity

\[
A_{d,s}\int_0^\infty t^{\alpha-1}(4\pi t)^{-d/2}
 e^{-|z|^2/(4t)}\,dt=|z|^{-s}
\]

follows by the substitution `r=|z|^2/(4t)`. For `0<t<=1`, every derivative in z of the nonzero image terms is exponentially small as `t` decreases to zero, uniformly on this ball, and the remaining `-1` term is integrable. For `t>=1`, derivatives of `H_t-1` decay exponentially; the Euclidean term and all its derivatives have integrable powers of t because `s>0`. Differentiating these subtracted integrals therefore gives a smooth even remainder q. Consequently

\[
g_s(z)=|z|^{-s}+q(z)
\]

in an embedded ball, and `g_s` is smooth away from zero. Moreover `K=-grad g_s` is locally of order `|z|^{-s-1}`, which is integrable for the entire admitted range `s<=d-2`. This verifies the local-kernel hypothesis of THM023, rather than inferring it from a matching exponent alone.

For completeness, the distributional multiplier is

\[
\widehat{\operatorname{div}K}(k)
 =4\pi^2c_{d,s}|k|^{s+2-d},\quad k\ne0;
\qquad \widehat{\operatorname{div}K}(0)=0.
\]

For `s<d-2`, the gamma recurrence gives

\[
s(d-2-s)c_{d,s+2}=4\pi^2c_{d,s}.
\]

For `s=d-2`, the multiplier is the constant

\[
4\pi^2c_{d,d-2}
 =\frac{4\pi^{d/2}}{\Gamma((d-2)/2)}
 =(d-2)|\mathbb S^{d-1}|=:c_d.
\]

This agrees with the finite-measure divergence stated in THM021, including the negative Haar compensation in the Coulomb case. No global pointwise nonnegativity of the zero-mean periodic kernel is used.

## 3. The pointwise and Haar response interfaces

Let `E={(x,y): x != y}` and let `D=div K` be the finite signed measure from THM021. For a bounded Borel representative v, define

\[
\begin{aligned}
R_{x,t}v(x,y)
 &=-\int\mu_t(x+w)v(x+w,y)\,D(dw)\\
 &\quad-\int K(w)\cdot\nabla\mu_t(x+w)v(x+w,y)\,dw.
\end{aligned}
\]

The second response is obtained by exchanging x and y. This is the exact supplied formula, with both density terms retained.

### 3.1 No off-diagonal evaluation requires a pair-diagonal trace

Suppose two bounded Borel extensions of v from E differ only on the spatial diagonal. For fixed `(x,y)` in E, their first-slot integrands can differ only at `w=y-x`, a nonzero torus point. Below Coulomb, D is absolutely continuous. At Coulomb,

\[
D=c_d(\delta_0-dw),
\]

whose only atom is at zero, and that atom is not at `w=y-x`. The `K(w)dw` term is absolutely continuous in all cases. Therefore the first-slot responses agree **pointwise at every off-diagonal state**, independently of the chosen diagonal extension. The same argument applies in the second slot.

In particular, the Coulomb atom in the first slot contributes

\[
-c_d\mu_t(x)v(x,y),
\]

and the second-slot atom contributes `-c_d mu_t(y)v(x,y)`. Neither evaluates `v(y,y)` or `v(x,x)` when `(x,y)` is off diagonal. Arbitrary Haar-L2 classes are not being assigned diagonal traces.

### 3.2 Borel, L2, and equality-class actions agree

Set

\[
C_*=2\left(M_0\|D\|_{\rm TV}+M_1\|K\|_1\right).
\]

Translation in either coordinate is an isometry on Haar L2. Multiplication by the translated density has norm at most `M_0`, and multiplication by the relevant translated gradient has norm at most `M_1`. Minkowski's integral inequality thus gives, in both pointwise sup norm and Haar L2,

\[
\|R_{x,t}\|\le M_0\|D\|_{\rm TV}+M_1\|K\|_1,
\qquad
\|R_{x,t}+R_{y,t}\|\le C_*.
\]

The same formulas define the actual bounded Borel action because their integrands are bounded and their controlling measures are finite. If v vanishes Haar almost everywhere on the pair space, then, for every fixed w, its translate also vanishes almost everywhere. Fubini with `|D|(dw)` and `|K(w)|dw` implies that each response vanishes Haar almost everywhere. This proves equality-class consistency even in the presence of the atom. Since smooth functions are dense in Haar L2, it also identifies the unique bounded L2 extension with the Borel formula whenever both are defined. A smooth-density approximation in the Borel sup norm is neither asserted nor needed.

For smooth v, integration by parts in w gives

\[
R_{x,t}v(x,y)=\int\mu_t(x+w)K(w)\cdot\nabla_xv(x+w,y)\,dw.
\]

The preceding finite-measure formula is precisely the distributional integration by parts of this expression. Taking v constant makes the expression zero; this also follows by cancellation of the two density terms. Omitting the density-gradient term would already fail this elementary test for an inhomogeneous density.

If `Qv(x,y)=v(y,x)`, then `QR_xQ=R_y`; therefore `R=R_x+R_y` commutes with Q. An individual response need not preserve symmetric kernels. Using only one response loses both the exact operator and its symmetry property.

### 3.3 Time measurability

For a jointly Borel bounded `v(t,x,y)`, all translated density and kernel integrands above are jointly measurable. Integration against the fixed finite measures preserves joint measurability, so `R_tv_t` has an actual jointly Borel representative on E. On Haar L2, strong continuity of translations and separability give well-defined strongly measurable measure integrals. Under the stated C1 time continuity of the density,

\[
\|R_t-R_a\|_{2\to2}
\le 2\left(\|\mu_t-\mu_a\|_\infty\|D\|_{\rm TV}
 +\|\nabla\mu_t-\nabla\mu_a\|_\infty\|K\|_1\right).
\]

Thus the operators are norm-continuous in time, in particular strongly measurable. Their action on a strongly measurable L2-valued input is strongly measurable. These checks supply the time interface required in THM024; an operator defined only on Haar classes would not by itself supply its pointwise Borel formula.

## 4. The auxiliary base-pair interface

The prescribed `u_t,f_t`, the local kernel established in Section 2, and `nu in [0,nu_*]` meet THM023's hypotheses. Its analytic conclusions are accepted here in their exact scope. Let `Z_a=(X_a,Y_a)` be its process from `(t,z)` in E and

\[
S_{t,a}v(z)=\mathbb E_{t,z}v(Z_a).
\]

This gives a sup-norm contraction on actual bounded Borel functions. The joint measurability, deterministic conditional Markov property and composition are part of the supplied Markov evolution. The paths remain in E, so changing the input on the diagonal changes no pointwise value of this evolution.

Swapping the particles and their independent Brownian motions changes the two drift equations into one another: both particles have the same ordinary transport, and `K(y-x)=-K(x-y)`. Pathwise uniqueness in the supplied module therefore gives `QS_{t,a}=S_{t,a}Q`. This is the needed exchange symmetry.

Write `C_g=||(R_g)_-||_infinity` for the bounded negative remainder in THM023. Its Haar-L2 estimate implies

\[
\|S_{t,a}\|_{2\to2}\le
 e^{(D_u+C_g/N)(a-t)}\le e^{c_*(a-t)},
\qquad c_*=D_u+C_g/2.
\]

The same module supplies a consistent Haar-L2 extension and joint strong continuity. In particular, `a -> S_{t,a}w_a` is strongly measurable for a strongly measurable L2 family `w_a`; approximation by simple functions and the uniform propagator bound prove this directly. Thus the future time integrals are Bochner measurable as well as pointwise measurable. This singular L2 statement is imported from THM023, not inferred from THM021's smooth-cutoff statement.

The actual source

\[
J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y))
\]

is jointly measurable and invariant under exchange of x,y. Near the diagonal, the gradient difference is bounded by a uniform Hessian bound times `|x-y|`, so its singularity is at most order `|x-y|^{-s}`. THM023 supplies, for this very source,

\[
W_N:=\sup_{t,z\in E}\mathbb E_{t,z}
 \int_t^T|J_a(Z_a)|\,da<\infty
\]

for each fixed parameter tuple, and the signed potential

\[
U_N(t,z)=\mathbb E_{t,z}\int_t^T J_a(Z_a)\,da
\]

with

\[
\sup_t\|U_N(t)\|_2\le A_N,
\quad A_N^2\le C_U\rho_N,
\quad \|U_N\|_\infty\le B_N\le W_N.
\]

`C_U` is uniform in N and bounded nu as stated in that module; `B_N` need only be finite for each N. These are separate roles. No uniform-in-N pointwise bound is substituted for the L2 estimate. Joint Borel measurability and boundedness also imply strong measurability of the L2-valued family `U_N(t)`.

This argument neither assumes nor proves convergence of the heat-regularized **source potentials**. THM023's source estimate and its singular propagator are used directly. Its propagator convergence alone would not suffice to pass a singular forcing to the limit.

## 5. Full bounded Borel inverse and its two uniqueness classes

Define `V_0=U_N` and recursively

\[
V_m(t)=\int_t^T S_{t,a}R_aV_{m-1}(a)\,da,
\qquad m\ge1,
\qquad R_a=R_{x,a}+R_{y,a}.
\]

All terms have the required actual Borel and L2 measurability by Sections 3–4. Repeated integration over the ordered time simplex gives

\[
\|V_m(t)\|_\infty
 \le B_N\frac{[C_*(T-t)]^m}{m!}.
\]

Hence the series `Phi=sum_(m>=0)V_m` converges uniformly in `(t,z)` on `[0,T] x E`. It is bounded Borel, real, terminal zero, and symmetric. Substitution into the integral, justified by this uniform majorant, gives

\[
\Phi_t=U_N(t)+\int_t^T S_{t,a}R_a\Phi_a\,da,
\qquad
\|\Phi\|_\infty\le B_Ne^{C_*T}.
\]

For the L2 estimate, the product of propagator norms in an m-fold term is at most `exp(c_*(T-t))`, since the propagation intervals telescope. Thus, also for `m=0` after harmless enlargement,

\[
\|V_m(t)\|_2\le
 A_Ne^{c_*(T-t)}\frac{[C_*(T-t)]^m}{m!}.
\]

The series converges uniformly in time in Haar L2, consistently with its pointwise Borel sum, and

\[
\sup_t\|\Phi_t\|_2
 \le A_Ne^{(c_*+C_*)T},\qquad
\sup_t\|\Phi_t\|_2^2
 \le C_Ue^{2(c_*+C_*)T}\rho_N.
\]

The constants depend only on the fixed data bounds and the finite diffusivity interval in the supplied modules. They do not depend on N or on the selected nu in that interval. The full source is `H=J+R Phi`; its absolute occupation is integrable because

\[
\mathbb E_{t,z}\int_t^T|H_a(Z_a)|\,da
 \le W_N+TC_*\|\Phi\|_\infty<\infty.
\]

Using the Markov composition law in the displayed Volterra equation yields, for every `t<=r<=T` and every off-diagonal start,

\[
\Phi_t=S_{t,r}\Phi_r+\int_t^r S_{t,a}H_a\,da.
\]

Equivalently, along the auxiliary base process,

\[
\Phi_r(Z_r)+\int_t^r H_a(Z_a)\,da
\]

is the true martingale obtained by conditioning the integrable terminal integral `int_t^T H_a(Z_a) da`. This is a potential/martingale statement, with the usual martingale version when needed; it makes no assertion that the Borel kernel has classical derivatives. The sign is fixed by the terminal-zero convention: for a classical kernel it would read `partial_t Phi+L_base Phi=-(J+R Phi)`.

If two uniformly bounded Borel solutions exist, their difference v satisfies `v_t=int_t^T S_(t,a)R_av_a da`. Iterating m times bounds its value by

\[
\|v\|_\infty\frac{[C_*(T-t)]^m}{m!},
\]

which tends to zero. Conversely, any bounded Borel martingale inverse with terminal zero for all starts gives the same Volterra identity by terminal conditional expectation. This proves pointwise uniqueness in that class.

For strongly measurable uniformly bounded-in-time L2 mild solutions, the same iteration with the factor `exp(c_*T)` proves uniqueness as L2 classes. This does not promote L2 uniqueness to a choice of values at individual states. The separately constructed bounded Borel solution is what supplies those values here.

## 6. Independent Fourier and diagonal falsification routes

The following computations do not assume the Volterra-series proof.

For `e_k(x)=exp(2 pi i k.x)`, the original first-slot response on a density mode `mu_a e_a` and pair mode `phi_(p,q)e_p(x)e_q(y)` is supported at `(a+p,q)`, with coefficient

\[
-4\pi^2\,(a+p)\cdot p\,\widehat g(a+p)\,\mu_a\phi_{p,q}.
\]

This follows by multiplying the three Fourier factors before integrating the displacement variable. The finite-measure formula independently gives the sum

\[
-4\pi^2|a+p|^2\widehat g(a+p)\mu_a\phi_{p,q}
+4\pi^2(a+p)\cdot a\,\widehat g(a+p)\mu_a\phi_{p,q},
\]

which agrees exactly. The zero Fourier mode of the force/divergence is zero. This checks the sign, density-gradient contribution, and first-slot frequency. The same calculation in the second slot gives the second response.

For homogeneous density, writing

\[
q_k=4\pi^2c_{d,s}|k|^{s+2-d}\quad(k\ne0),\qquad q_0=0,
\]

the pair response on mode `(p,q)` is the multiplier `-(q_p+q_q)`. At Coulomb, on modes with both coordinates nonzero, it is `-2c_d`. Using one response would give `-c_d`, a concrete factor-of-two error.

For a finite Fourier cutoff, the internal pair operator

\[
B=K(x-y)\cdot(\nabla_x-\nabla_y)
\]

maps pair mode `(p,q)` to modes `(p+k,q-k)` with coefficients

\[
4\pi^2\,k\cdot(p-q)\,\widehat g(k).
\]

Expanding the two original particle drifts separately gives the same result divided by N, without an additional factor of two. The total frequency is conserved. For a test mode n, the source is

\[
J_n=4\pi^2\sum_{k\ne0}k\cdot n\,\widehat g(k)
 \left[e_{k+n}(x)e_{-k}(y)-e_k(x)e_{n-k}(y)\right].
\]

This agrees with `B[f(x)+f(y)]` and is symmetric. These checks fix the full-pair and source signs independently of a PDE shorthand.

An adversarial representative test is `v=1_{x=y}`. Its Haar-L2 class is zero. For `mu=1` at Coulomb, each singular Borel response equals `-c_d v` on the full pair space, while each response of the heat-smoothed kernel is zero. Thus a general bounded-Borel sup-norm convergence assertion would fail. On E, however, both responses vanish exactly. This example supports, rather than undermines, the off-diagonal interface: the proof above never uses global Borel sup-norm cutoff convergence or a diagonal trace.

A separate terminology test concerns “symmetric Markov evolution.” Take a nonzero constant ordinary drift u and the pair character `e_k(x)e_k(y)`. The internal B term vanishes on this character, but the ordinary transport contributes the imaginary eigenvalue `4 pi i u.k`, in addition to real diffusion damping. The Haar generator is not self-adjoint. It still commutes with particle exchange, which is exactly the property used in Section 5. If THM024's word “symmetric” were instead intended to impose Haar self-adjointness, its application would fail first at THM025 line 7; the strongest repair would simply replace that unnecessary requirement by exchange covariance. The theorem cards' repeated use of pair symmetry supports the exchange interpretation, and no mathematical change to the proved composition is needed.

## 7. Initial iid endpoint: exact finite-N calculation

Fix N and the deterministic bounded Borel kernel `Phi_0` constructed above. Choose any diagonal extension. Since the initial law has a density, this extension changes neither its L2 class nor any evaluated distinct-label term almost surely. More generally, the following finite-N identity also holds for atomic iid laws when the diagonal values are part of the specified L2 kernel.

For iid variables of law mu, put

\[
\theta=\iint\Phi\,d\mu\,d\mu,\qquad
h(x)=\int\Phi(x,y)\,d\mu(y)-\theta,\qquad
H(x,y)=\Phi(x,y)-\theta-h(x)-h(y).
\]

Then `mu(h)=0`, each marginal integral of H vanishes, and

\[
\|\Phi\|_{L^2(\mu^2)}^2
 =\theta^2+2\|h\|_2^2+\|H\|_2^2.
\]

Direct substitution into the ordered distinct-label statistic with denominator `N^2` gives

\[
P_N[\Phi]
 =-\frac{\theta}{2N}
  -\frac1{N^2}\sum_{i=1}^N h(X_i)
  +\frac1{N^2}\sum_{1\le i<j\le N}H(X_i,X_j).
\]

In particular, this is the actual mean-field-centered statistic, including its deterministic mean `-theta/(2N)`, not the separately centered random variable `P_N-E P_N`.

Distinct canonical pair terms are orthogonal: disjoint terms are independent and centered, while terms sharing one label have zero conditional expectation after conditioning on that label. The h terms and canonical pair terms are likewise orthogonal. Consequently,

\[
\mathbb EP_N^2
 =\frac{\theta^2}{4N^2}
  +\frac{\|h\|_2^2}{N^3}
  +\frac{N-1}{2N^3}\|H\|_2^2
 \le \frac{N-1}{2N^3}\|\Phi\|_{L^2(\mu^2)}^2.
\]

The coefficient comparison uses `N>=2`: the difference between the right and left sides is

\[
\frac{N-2}{4N^3}\theta^2+\frac{N-2}{N^3}\|h\|_2^2.
\]

Thus the constant is sharp for a nonzero canonical H, and for every kernel when N=2.

The initial density satisfies `mu_0<=M_0`, so both integrations contribute a factor:

\[
\|\Phi_0\|_{L^2(\mu_0^2)}^2
 \le M_0^2\|\Phi_0\|_{L^2(dx\,dy)}^2.
\]

A single factor `M_0` is insufficient in general: if a density equals M on a set of Haar mass `1/M`, and the kernel is the indicator of that set squared, the ratio of squared norms is exactly `M^2`. Smooth approximations also approach that ratio. The C1 density required by the prescribed dynamics causes no loss in the correct two-factor inequality.

For `b_N=min(beta_N,1)`, multiplication by `N b_N` yields the slightly sharper finite-N form

\[
\begin{aligned}
\mathbb E\left|\sqrt{N b_N}P_N[\Phi_0]\right|^2
 &\le \frac{b_N(N-1)}{2N^2}
       M_0^2\|\Phi_0\|_2^2\\
 &\le \frac{b_NM_0^2}{2N}
       C_Ue^{2(c_*+C_*)T}\rho_N.
\end{aligned}
\]

This proves the displayed THM025 endpoint with a permissible constant. Its three orders are

\[
\frac{b_N}{N},\qquad
\frac{b_N(1+\log N)}{N},\qquad
b_NN^{-(d+2-s)/(s+2)},
\]

respectively. The last exponent follows by subtracting 1 from `(2s-d)/(s+2)`; it is strictly negative in the admitted range. The estimate concerns the initial iid law only. It is a genuine second-moment estimate, not an expectation substituted for a fluctuation bound.

## 8. Actual homogeneous reference and backward test

Set external drift `b=0` and choose `mu_t=1`. Since the force is an integrable periodic derivative, `K*1=0`, and `Delta 1=0`. The frozen mean-field equation is therefore satisfied by this reference, with `u=0`, for every `nu>=0`. This is an explicit solution; no general mean-field uniqueness theorem is required.

To check the backward test against the actual frozen model, linearize its transport term at a smooth reference. Pairing the linearized equation for a perturbation rho with f gives the adjoint operator

\[
\nu\Delta f+u\cdot\nabla f+\mathcal R_\mu f,
\qquad
\mathcal R_\mu f(x)=\int\mu(z)K(z-x)\cdot\nabla f(z)\,dz.
\]

At homogeneous density this is

\[
\mathcal R_1f(x)=\int K(w)\cdot\nabla f(x+w)\,dw
 =-\int f(x+w)\,D(dw).
\]

Hence `mathcal R_1 e_k=-q_k e_k` and `nu Delta e_k=-4 pi^2 nu |k|^2 e_k`. The backward terminal problem is exactly

\[
\partial_t f+\nu\Delta f+\mathcal R_1f=0,\qquad f_T=h.
\]

For each nonzero k its coefficient obeys `partial_t f_hat(k)=a_k f_hat(k)`, where

\[
a_k=4\pi^2\nu|k|^2+q_k\ge0.
\]

Solving with a terminal, rather than initial, value gives

\[
f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)a_k}e^{2\pi i k\cdot x},
\]

precisely the displayed THM025 formula. Differentiation in t contributes `+a_k`, which cancels the negative spatial multiplier. Reversing the exponential sign would fail the equation already on one nonzero mode.

For every integer m, smoothness of h gives

\[
\sum_{k\ne0}|k|^m|\widehat h(k)|<\infty.
\]

Since the damping factors lie between zero and one,

\[
\sup_{t\in[0,T],\,\nu\ge0}\|\nabla^m f_t\|_\infty
 \le (2\pi)^m\sum_{k\ne0}|k|^m|\widehat h(k)|,
\]

with the evident inclusion of the mean for `m=0`. This proves all claimed uniform spatial derivative bounds, independently of N. Real h produces real f by conjugate symmetry. Because `s+2-d<=0`, the nonzero response multiplier `q_k` is bounded. On every finite interval `0<=nu<=nu_*`, the time-differentiated series, with every fixed spatial derivative, is also uniformly summable using the bound

\[
|k|^m a_k|\widehat h(k)|
 \le 4\pi^2\left(\nu_*|k|^{m+2}
              +c_{d,s}|k|^m\right)|\widehat h(k)|.
\]

This justifies termwise differentiation, the terminal value, and all stated time-continuity and joint-measurability requirements uniformly on the bounded diffusivity interval. No uniform time-derivative bound as `nu` tends to infinity is needed or claimed.

Thus the actual homogeneous data satisfy the whole prescribed-data interface, with `M_0=1`, `M_1=0`, `u=0`, and uniformly bounded test data. The full pair source here is the actual time-dependent J built from this f, and the inverse includes both responses. It is not merely a bound on a diagnostic kernel.

## 9. Temperature quantifiers and the exact remaining gates

The analytic pair estimate is uniform only for a fixed finite `nu_*`. With `nu=1/beta_N`, it applies uniformly when `beta_N>=beta_*>0`, taking `nu_*>=1/beta_*`. The constants may depend on this chosen lower bound through the bounded-diffusivity data. The analytic zero-noise construction is included separately; it does not identify zero noise with any finite beta.

At microscopic criticality,

\[
\lambda_N=\beta_NN^{s/d-1}\longrightarrow\lambda\in(0,\infty)
\]

implies

\[
\beta_N=\lambda_NN^{1-s/d}\longrightarrow\infty
\]

because `s<d`. Every such sequence therefore meets any fixed positive lower beta bound eventually, and `b_N=1` eventually. The initial endpoint tends to zero throughout the admitted critical exponent range. The full-pair endpoint estimate in fact applies to every sequence satisfying the lower beta bound, independently of whether it is subcritical, critical, or supercritical; it does not settle the dynamic regime merely by doing so.

Microscopic subcriticality alone does not supply this lower bound. For example `beta_N=N^-1` has `lambda_N=N^(s/d-2)->0` but `nu_N=N`, so the stated bounded-diffusivity input is unavailable. Excluding this sequence is a real restriction already stated in THM025, not an implication that its endpoint is false. There is no proof here for all subcritical sequences.

The old first-order condition also remains distinct. On a critical sequence,

\[
\beta_NN^{2s/d-1}=\lambda_NN^{s/d}\longrightarrow\infty.
\]

Thus this initial endpoint does extend beyond that old condition. It does not remove the remaining dynamic proof obligations.

| Gate | Status after this reconstruction |
|---|---|
| Frozen Fourier kernel versus THM023 local kernel | Reconstructed and compatible. |
| Off-diagonal Borel response versus its finite-measure atom | Reconstructed and compatible pointwise. |
| Haar equality classes, both slots, and time measurability | Reconstructed and compatible. |
| Singular auxiliary two-particle process and source potential | Accepted THM023 hypotheses; underlying proofs not read or recertified. |
| Bounded Borel full inverse and L2 order | Reconstructed conditional on those explicit analytic hypotheses. |
| Actual homogeneous reference/test and initial iid endpoint | Reconstructed with the stated bounded-diffusivity/lower-beta range. |
| Arbitrary prescribed data as actual inhomogeneous mean-field solutions | Not asserted; no existence or uniform derivative theorem supplied. |
| Singular N-particle process and corrector generator-domain membership | Open beyond this card. A two-particle auxiliary process does not supply the N-particle Itô domain. |
| Singular finite-particle Itô identity and regularization passage for the constructed kernel | Open. The inverse is Borel, and no derivative estimates, trace estimates, or convergence of regularized source potentials have been proved here. |
| Evolved law | Open. Initial independence is not propagated through the interaction, and the auxiliary pair process is not identified with the interacting N-particle two-point marginal. |
| Residuals, martingale brackets, path/time estimates, tightness, Gaussian limit | Open. The single initial second moment supplies none of these statements. |
| Critical higher-order hierarchy or infinite resummation | Open. No finite truncation or critical law is inferred. |
| Subcritical beta tending to zero, logarithmic normalization, exponents outside `0<s<=d-2` | Outside the proved interface. |

No load-bearing first failed line was found under the stated pair-exchange and all-starts interpretations. The strongest certified result **of this review** is the conditional interface theorem plus the independently checked homogeneous Fourier and iid calculations. This is narrower than a certification of the complete prerequisite analytic proofs or a fluctuation theorem.

## 10. Per-claim disposition and reproducible checks

The identifiers below are local to TASK043 and do not allocate or recycle campaign theorem/audit identifiers.

| Local claim | THM025 location | Disposition | Reason |
|---|---|---|---|
| TASK043-C01 | Line 5: frozen singular data | PASS | Section 2 verifies the local Riesz normalization required by the base module. |
| TASK043-C02 | Line 7: diagonal representatives | PASS | The displaced diagonal is a nonzero singleton; the Coulomb atom stays at the current off-diagonal state. |
| TASK043-C03 | Line 7: Haar consistency and measurability | PASS | Translation/Fubini and C1 density time continuity provide the required pointwise and L2 actions. |
| TASK043-C04 | Line 7: full inverse and uniqueness | PASS conditional on explicit base module | The uniformly convergent Volterra construction and true-martingale representation establish both stated uniqueness classes. |
| TASK043-C05 | Line 7: uniform L2 order | PASS conditional on explicit source estimate | Ordered time integrals preserve the imported source order with a uniform exponential factor. |
| TASK043-C06 | Lines 9–13: initial endpoint | PASS | Exact deleted-label decomposition, both density factors, and the scale `sqrt(N b_N)` are checked. |
| TASK043-C07 | Lines 15–21: actual homogeneous data | PASS | Mean-field and backward equations, Fourier signs, terminal values, realness, and all required uniform derivatives are checked. |
| TASK043-C08 | Lines 13 and 21: temperature range | PASS | All critical sequences eventually satisfy the lower bound; subcriticality alone does not imply it. |
| TASK043-C09 | Line 23: excluded conclusions | PRESERVED | No finite-particle domain, evolved-law, dynamic limit, or critical closure is inferred. |
| TASK043-C10 | THM024 line 5: word “symmetric” | TERMINOLOGICAL QUALIFICATION | The proof needs and establishes coordinate-exchange covariance; self-adjointness is false for allowed drifts and unnecessary. |

The checker `round005_interface_checks.py` uses only the Python standard library, exact rational/integer arithmetic, and SHA-256. It performs **2,672 assertions**, all passing. Its exact finite Fourier computations use an explicitly even finite Coulomb cutoff and factor out `4 pi^2 c_(d,s)`; they do not approximate the singular semigroup. The independent tests include:

- complete enumeration of iid laws on three atoms for N=2,3,4,5, with constant, separable, canonical, and mixed symmetric kernels; all 1,440 sampled-configuration decompositions and the exact moments pass;
- the sharp second-moment constant and the N=2 equality case, including the values of the kernel at spatially coincident labels;
- the necessity of the squared density factor;
- original integrated-gradient versus finite-measure Fourier responses for a positive inhomogeneous trigonometric density, in both slots;
- killing constants, exchange covariance, and deliberate detection of an omitted density-gradient term or response slot;
- separate particle drift expansion versus the exact `B/N` operator at N=2,3,7, together with the source formula;
- actual backward Fourier damping signs, gamma-recurrence normalization, endpoint exponents, and critical/subcritical temperature quantifiers;
- the scalar Volterra coefficient recurrence and its sign;
- all eight input digests, rechecked at execution.

The exact command, run from this isolated worktree, is:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/round005_interface_checks.py
```

Its machine-readable result is `ROUND_005_INTERFACE_CHECK_RESULTS.json`. Computational success is supporting algebraic evidence, not a proof of the assumed analytic modules. This report's comparison against its own checker is a self-check; the report's independence consists in reconstructing the submitted statement without reading the constructor narrative or another audit.

The README identifies the output and verification commands. The input manifest binds the eight permitted source files; the output manifest binds the issued reconstruction, checker, results, README, and the input manifest. A separate archive seal binds the complete packet. No output manifest is claimed to hash itself. After the seal is issued this report is immutable; any later correction must be a separately named superseding report.
