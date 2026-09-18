# Round 009 — uniform Haar noise energy and the exact actual-law reduction

TASK055. **CONDITIONAL / SELF_CHECKED candidate for THM029.** The complete THM028 domain assertion is an explicit conditional prerequisite until its separate independent gates pass. The present context constructed the submitted R8 candidate and received the disclosed R9 root seed; neither this continuation nor its checks constitute independent certification of R8 or R9.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r009-haar-energy-20260918`. Branch: `codex/hocf-r009-haar-energy`. Base: published R6 `3aa91391516f35afe5317a287b4f0e2e93e6384c`. The nineteen permitted inputs were copied and hash-checked before work. Only that dossier was used. No ongoing audit, state/history or memory was read, and no prior checker was read or imported. No root/canonical edits, commits, pushes, dependencies or child agents were used.

The conclusion is the full conditional THM029 assertion. No counterexample or unsupported line in that implication was found. The last section states the remaining two-/three-marginal obligation exactly; the reference-noise estimates are not declared to be actual-particle bracket estimates.

## 1. Exact assertion, negation, and conditional scope

Fix the homogeneous THM028 data: unit Haar torus, `d>=3`, `0<s<=d-2`, integer `N>=2`, finite T, `0<=nu<=nu_*<infinity`, frozen Fourier Riesz potential g, `K=-grad g`, external drift zero, mean-field reference one, real smooth terminal test h, and its actual homogeneous backward test f. Let Phi be the given symmetric terminal-zero full pair inverse, including both compensated responses. Set `p=s+2` and `a=s/p`.

Conditional on THM028, Phi is C1 in time and locally C2 off the pair diagonal. It is bounded and has the stated weighted first/second derivatives for every `1<q_1<d/2`, `q_1+1<q_2<d`. It belongs globally to Haar H1 and W2,1, while its time derivative and B Phi are Haar L1 uniformly in time, where

\[
 B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi.
\]

It satisfies the classical off-diagonal equation

\[
 \partial_t\Phi+\nu\Delta_{x,y}\Phi+B\Phi/N+R\Phi=-J,
 \quad J=K(x-y)\cdot(\nabla f(x)-\nabla f(y)),\quad \Phi_T=0.
 \tag{1.1}
\]

Those domain properties are used only to justify operations at each fixed N. No bound depending on an R8 gradient/Hessian constant is absorbed into the uniform constant proved below.

The exact primary assertion is the conjunction of THM029's N-uniform Haar energy estimate, exact deleted-label Haar identity, scaled reference-noise and absolute-cross bounds, exchangeable-law identity, and preservation of exchangeability and one-body Haar marginals under iid Haar preparation. Its logical negation is an admissible tuple satisfying the conditional prerequisite for which any of these estimates, coefficients, or law assertions fails. An eventual failure of the conditional R8 prerequisite is not ruled out by this continuation.

The kernel normalization, finite-measure response, source-potential construction, and particle realization are the supplied R4–R6 modules. Their scopes and the separate source/constant and pair-exchange clarifications are retained. No outside source or novelty claim is used.

## 2. The N-uniform source constants come from the full R5 proof

The short base-pair card gives the Haar-L2 order but does not itself state the precise power of N in the pointwise supremum. The needed source is the complete `ROUND_005_PERIODIC_PAIR_POTENTIAL.md`, equations (2.3), (2.7), (3.1)–(3.4), and (5.3). We extract its constants here.

On the fixed embedded ball write

\[
 K(z)=s|z|^{-s-2}z+k(z),\qquad k(0)=0,\qquad |k(z)|\le L_k|z|.
\]

Use the fixed R5 radii `R_0<R_1` and cutoff chi, equal to one on the inner ball. Define the uniform Fourier data bounds

\[
 G_f=\sup_{t,\,0\le\nu\le\nu_*}\|\nabla f_t\|_\infty,
 \qquad H_f=\sup_{t,\,0\le\nu\le\nu_*}\|D^2 f_t\|_\infty.
\]

They are finite independently of N and nu: the actual Fourier multiplier is

\[
 e^{-(T-t)[4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{s+2-d}]},
\]

for nonzero k; the zero-mode multiplier is one. Every multiplier has modulus at most one. Thus `G_f<=2 pi sum |k| |h_hat(k)|` and
`H_f<=4 pi^2 sum |k|^2 |h_hat(k)|`. Rapid Fourier decay makes these sums finite. Differentiating the backward multiplier in time gives a positive damping coefficient; it cancels the negative spatial multiplier in (1.1)'s one-body prerequisite, rather than reversing its sign.

For explicit source constants set

\[
 \begin{gathered}
 K_{\rm out}=\sup_{\operatorname{dist}(z,0)\ge R_0}|K(z)|,
 \quad B_J=H_fL_kR_0^2+2G_fK_{\rm out},\\
 C_1=\|\nabla\chi\|_\infty,\quad C_2=\|\Delta\chi\|_\infty,
 \quad V_*=sR_0^{-s-1}+L_kR_1,\\
 E_*=sR_0^{-s}(2\nu_*C_2+V_*C_1)
       +4\nu_*C_1s^2R_0^{-s-1},\\
 \alpha=1+sL_k,\quad C_B=B_J+H_fE_*/\alpha,\quad c_0=2s(s+2).
 \end{gathered}
 \tag{2.1}
\]

These are exactly the R5 choices with ordinary transport u=0. They do not involve N or the selected nu. The coefficient `4nu_*` in the cutoff cross term is retained.

R5's positive radial profile and bound are

\[
 F_{N,\tau}(r)=\frac N4\big[(r^p+c_0\tau/N)^{2/p}-r^2\big]
 \le\frac{c_0^{2/p}}4N^a\tau^{2/p}.
 \tag{2.2}
\]

The inequality also follows directly from `(u+v)^(2/p)<=u^(2/p)+v^(2/p)`, since `0<2/p<1`. It holds for every N, including N=2,3, and at every nonnegative tau; it is not an asymptotic expansion.

The complete R5 source proof gives

\[
 \|U_N\|_\infty\le e^{\alpha T}
 \left[\frac{H_fc_0^{2/p}}4N^aT^{2/p}+C_BT\right].
\]

At homogeneous density, the two-response bounded-Borel norm is at most
`C_R=2||D||_TV`, where `D=div K` is the fixed finite signed measure. The exact R5 Volterra series therefore multiplies this supremum by at most `exp(C_R T)`. Since `N^a>=1`, we obtain

\[
 \boxed{\|\Phi\|_\infty\le C_\infty N^a,\qquad
 C_\infty=e^{(\alpha+C_R)T}
 \left[\frac{H_fc_0^{2/p}}4T^{2/p}+C_BT\right].}
 \tag{2.3}
\]

Both response slots are included in this constant. No unknown N-dependent derivative constant enters it.

The source itself satisfies the R5 pointwise estimate
`|J|<=H_f s chi(z)|z|^-s+B_J`. Its uniform Haar-L1 bound is consequently

\[
 \boxed{\sup_t\|J_t\|_1\le C_J:={H_fs|\mathbb S^{d-1}|R_1^{d-s}\over d-s}+B_J.}
 \tag{2.4}
\]

All Haar measures have mass one. The source constants C_infinity and C_J vanish for constant h, in which case J and Phi are identically zero by uniqueness.

Choose nonnegative kappa to dominate both the lower-divergence constant from R4 and the negative-remainder constant from the fixed R5 decomposition, exactly as in the supplied source/constant addendum. In particular `D>=-kappa dz`, and its classical density off zero satisfies `D_cl>=-kappa`. This kappa depends only on the fixed kernel/cutoff data. We do not silently identify two independently chosen minimal constants.

For comparison, the full R5 proof, (5.4)–(5.7), and the response composition also give `sup_t ||Phi_t||_2^2<=C_L rho_N`, where rho_N is 1, `1+log N`, or `N^((2s-d)/p)` in the three respective cases. Its displayed constant is N-independent; the local core calculation in that proof includes all N. In every case `rho_N/N<=1` for `N>=2`: at the logarithmic borderline use `log N<=N-1`, and above it use `(2s-d)/p<1`. Thus that sharper route also handles the borderline without an N-dependent constant. The energy proof below needs only the explicit supremum bound (2.3); this avoids any dependence on a stronger norm than necessary.

## 3. Deleted-tube integration, including the Coulomb flux

Fix N, nu and t for the moment. Choose any allowed q_1 in the domain theorem. Write `psi(z,y)=Phi(z+y,y)` in the embedded relative chart. Haar measure transforms as `dxdy=dzdy`, and

\[
 B=2K(z)\cdot\nabla_z-K(z)\cdot\nabla_y.
 \tag{3.1}
\]

Let `Omega_epsilon={|z|>epsilon}` with epsilon below the embedded radius, extending the domain through the rest of the torus. Only the inner sphere is a boundary; y remains periodic.

First, ordinary integration by parts on this domain gives

\[
 \int_{\Omega_\epsilon}\Phi\Delta_{x,y}\Phi
 =-\int_{\Omega_\epsilon}|\nabla_{x,y}\Phi|^2+\mathcal D_\epsilon.
\]

The boundary flux in these coordinates is
`int_(|z|=epsilon) psi(2 grad_z psi-grad_y psi).(-z/epsilon) dS_z dy`.
The original pair gradients control this vector. By boundedness of Phi and the weighted first-derivative bound,

\[
 |\mathcal D_\epsilon|\le C_N\epsilon^{d-1-q_1}\longrightarrow0,
 \qquad q_1<d-1.
\]

The volume terms converge absolutely: `Phi Delta Phi` is L1 by boundedness and W2,1, and the gradient square is L1 by H1. Thus

\[
 \int\Phi\Delta_{x,y}\Phi=-\|\nabla_{x,y}\Phi\|_2^2.
 \tag{3.2}
\]

The fixed-N boundary constant is used only for this vanishing limit, not in the final estimate.

For the internal drift, (3.1) gives the exact formula

\[
 \int_{\Omega_\epsilon}\Phi B\Phi
 =-\int_{|z|=\epsilon}\!\int
      [K(z)\cdot z/\epsilon]\,\psi(z,y)^2\,dy\,dS_z
   -\int_{\Omega_\epsilon}D_{\rm cl}(z)\psi(z,y)^2\,dzdy.
 \tag{3.3}
\]

Indeed the derivative of `psi^2` contributes a factor one-half, while the relative drift has coefficient 2. Therefore the bulk divergence coefficient in (3.3) is one, not two. The y-transport has zero integrated contribution by periodicity.

For small enough epsilon,

\[
 K(z)\cdot z/\epsilon\ge s\epsilon^{-s-1}-L_k\epsilon\ge0.
\]

For example take epsilon below `R_0` and, when `L_k>0`, below `(s/(2L_k))^(1/(s+2))`. Thus the entire inner boundary term in (3.3) is nonpositive.

Below Coulomb its absolute value is at most
`C ||Phi||_infinity^2(epsilon^(d-s-2)+epsilon^d)`, which tends to zero. At Coulomb the first power is zero; that flux cannot be discarded. We retain its nonpositive sign for every sufficiently small epsilon. No value of Phi on the diagonal, diagonal trace, or pre-existing flux limit is assumed.

The left side of (3.3) has a finite absolute limit because THM028 gives `B Phi in L1` and Phi is bounded. The bulk integral also converges absolutely: D_cl is L1 below Coulomb and bounded at Coulomb, while Phi is bounded. Taking limits in the inequality obtained by discarding only the nonpositive boundary term, and using `D_cl>=-kappa`, gives

\[
 \boxed{\int\Phi B\Phi\le\kappa\|\Phi\|_2^2.}
 \tag{3.4}
\]

This argument does not exchange the tube limit with an N-limit. It first proves the identity/inequality at each fixed N; its final coefficient kappa is independent of N.

A useful falsification test is a constant test kernel at Coulomb. The bulk term in (3.3) equals `c_d||Phi||_2^2`, and the radial flux cancels it; B acting on a constant is zero. Discarding the flux as if it vanished would give a false identity. Conversely B need not be nonpositive: for a smooth symmetric relative kernel with zero diagonal value, the Coulomb formula can give a positive quadratic form. Only the upper bound (3.4) is used.

## 4. The actual homogeneous response is nonpositive

The frozen finite measure D is even, and its Fourier coefficients are

\[
 d_k=\widehat D(k)=4\pi^2c_{d,s}|k|^{s+2-d}\ge0\quad(k\ne0),
 \qquad d_0=0.
\]

The exponents satisfy `s+2-d<=0`, so these coefficients are bounded. Each homogeneous response is convolution by minus D in its own slot. For a finite Fourier polynomial v,

\[
 \langle v,Rv\rangle_{L^2}
 =-\sum_{k,l\in\mathbb Z^d}(d_k+d_l)|\widehat v(k,l)|^2\le0.
 \tag{4.1}
\]

For general Haar-L2 v, take finite Fourier projections converging in L2. Convolution by a finite measure is L2 bounded, by translation invariance and Minkowski, with norm at most its total variation. Thus the quadratic forms converge; alternatively the nonnegative weighted series converges absolutely by the bounded multipliers. Formula (4.1) holds for the actual Phi. This is a legitimate L2 operator approximation, not an assertion about heat convergence of singular source potentials.

Both responses appear as `d_k+d_l`. At Coulomb, a mode with both slots nonzero has multiplier `-2c_d`; a missing slot loses a factor two. The zero mode is killed. This self-adjoint/nonpositive statement is specific to the homogeneous convolution responses. It is not attributed to a general inhomogeneous response or to the full base-pair Markov evolution.

## 5. Uniform backward energy estimate

Let `E(t)=||Phi_t||_2^2`. Its derivative satisfies

\[
 E'(t)=2\int\Phi_t\partial_t\Phi_t.
\]

To justify this even when the time derivative is not L2, use its pointwise time fundamental theorem, the bounded Phi, and the THM028 bound `|partial_t Phi|<=C_N w_s`. The product has a common integrable majorant because `s<d`. Fubini and dominated convergence give the formula and its time continuity, including one-sided endpoints. In particular `E(T)=0`.

Multiply (1.1) by Phi, use (3.2), and integrate in time. Every pairing is absolutely defined by the domain prerequisite, boundedness of Phi, and the finite-measure response. The exact backward energy identity is

\[
 \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt+\frac12\|\Phi_0\|_2^2
 =\int_0^T\langle J_t,\Phi_t\rangle dt
   +\frac1N\int_0^T\langle\Phi_t,B\Phi_t\rangle dt
   +\int_0^T\langle\Phi_t,R\Phi_t\rangle dt.
 \tag{5.1}
\]

The initial norm has a **positive** sign on the left; this follows from the terminal-zero convention. Equations (3.4) and (4.1) imply

\[
 \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt
 \le\int_0^T\|J_t\|_1\|\Phi_t\|_\infty dt
      +\frac\kappa N\int_0^T\|\Phi_t\|_2^2dt.
\]

Using Haar mass one and (2.3)–(2.4), the right side is at most

\[
 T C_JC_\infty N^a+\kappa T C_\infty^2N^{2a-1}
 \le C_E N^a,
 \qquad C_E=T(C_JC_\infty+\kappa C_\infty^2),
 \tag{5.2}
\]

because `0<a<1`, hence `2a-1<=a` for all `N>=1`. This proves the target

\[
 \boxed{\nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt
       \le C_E N^{s/(s+2)}.}
 \tag{5.3}
\]

The displayed C_E depends only on `d,s,T,nu_*,h` and the fixed kernel/cutoffs. The R8 gradient constants have disappeared entirely after justifying integration. The result includes the logarithmic Haar-L2 borderline, either by this supremum argument or by the explicit rho_N comparison in Section 2. At nu=0 the left side is zero; dividing by nu to claim a uniform unweighted gradient estimate would be invalid. At T=0 all integrated quantities are zero and the constants can be taken zero.

## 6. Exact Haar identity with the deleted-label normalization

At a fixed time define

\[
 G(x,y)=\nabla_x\Phi(x,y),\qquad
 A(x)=\int G(x,y)dy,\qquad H(x,y)=G(x,y)-A(x).
 \tag{6.1}
\]

The domain theorem makes these L2 objects well-defined; Jensen gives `||A||_2<=||G||_2`. Their exact orthogonal decomposition is

\[
 \|H\|_2^2=\|G\|_2^2-\|A\|_2^2,
 \qquad\int H(x,y)dy=0.
\]

The statistic is

\[
 P[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
 -\frac1N\sum_i\int\Phi(X_i,y)dy
 +\frac12\int\Phi(x,y)dxdy.
\]

Its precise configuration gradient, using pair symmetry, is

\[
 \nabla_iP=\frac1{N^2}\sum_{j\ne i}G(X_i,X_j)-\frac1N A(X_i)
 =\frac1{N^2}\left[\sum_{j\ne i}H(X_i,X_j)-A(X_i)\right].
 \tag{6.2}
\]

The last `-A` is a finite-N deletion term. It would be lost by replacing the denominator `N^2` by a falling-factorial convention or by silently including the repeated label.

Under independent Haar sampling, condition on X_i. Distinct H terms have zero conditional means, their cross products have zero conditional expectation, and their cross product with A(X_i) has zero expectation. All these operations are absolutely justified by L2 and Cauchy–Schwarz. Therefore

\[
 \int_{\mathrm{Haar}^N}|\nabla_iP|^2
 =\frac1{N^4}\left[(N-1)\|H\|_2^2+\|A\|_2^2\right].
\]

Summing i and inserting the orthogonal decomposition proves exactly

\[
 \boxed{
 \int_{\mathrm{Haar}^N}\sum_i|\nabla_iP|^2
 =\frac{N-1}{N^3}\|G\|_2^2
  -\frac{N-2}{N^3}\|A\|_2^2.}
 \tag{6.3}
\]

At N=2 this is `||G||_2^2/8`; at N=3 it is `(2||G||_2^2-||A||_2^2)/27`. If G=A, the expression is `||A||_2^2/N^3`, not zero. This provides a direct finite-N deletion check.

## 7. Reference-noise and absolute-cross bounds

Assume now `nu=1/beta_N` with positive beta_N in the stipulated bounded-noise range. For `nu_*>0` this means `beta_N>=1/nu_*`. Set `b_N=min(beta_N,1)` and `sigma_N^2=N b_N`. Define the deterministic reference functional

\[
 Q_{2,N}^{\rm Haar}
 =\sigma_N^2\int_0^T\int_{\mathrm{Haar}^N}
       2\nu\sum_i|\nabla_iP_t|^2\,dX\,dt.
\]

Pair symmetry and Haar invariance under swapping coordinates give
`||grad_(x,y) Phi||_2^2=2||G||_2^2`. Dropping only the nonpositive A term in (6.3) and using (5.3) yields

\[
 \begin{split}
 Q_{2,N}^{\rm Haar}
 &\le b_N\frac{N-1}{N^2}
       \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt\\
 &\le C_E b_N N^{a-1}
 =C_E b_NN^{-2/(s+2)}.
 \end{split}
 \tag{7.1}
\]

This is a Haar integral of a deterministic configuration function. It is not the expectation of the actual-particle bracket without another law argument.

For the leading statistic `eta_N(f_t)`, its configuration gradient is
`N^-1 grad f_t(X_i)`. The corresponding leading reference functional is exactly

\[
 Q_{1,N}^{\rm Haar}=2b_N\nu\int_0^T\|\nabla f_t\|_2^2dt
 \le C_1^{\rm noise}:=2T G_f^2,
 \tag{7.2}
\]

because `b_N nu=min(1,nu)<=1`. Subtracting the deterministic Haar mean of f does not change this gradient.

The absolute cross-variation density gives the deterministic functional

\[
 C_{12,N}^{\rm Haar}
 =\sigma_N^2\int_0^T\int_{\mathrm{Haar}^N}
 \left|2\nu\sum_i\nabla_i\eta_N(f_t)\cdot\nabla_iP_t\right|dXdt.
\]

First apply Cauchy–Schwarz to the particle/vector sum, then to time and configuration integration with the common nonnegative factor `2nu sigma_N^2`. This bounds it by

\[
 C_{12,N}^{\rm Haar}
 \le\sqrt{Q_{1,N}^{\rm Haar}Q_{2,N}^{\rm Haar}}
 \le\sqrt{C_1^{\rm noise}C_E}\,\sqrt{b_N}\,N^{-1/(s+2)}.
 \tag{7.3}
\]

The absolute value is inside both integrals; it has not been replaced by the absolute value of a signed average. For zero noise every noise functional is zero separately. No finite beta is identified with the reciprocal of zero.

These are reference-law bounds for every permitted sequence with bounded noise. For every fixed positive nu_*, critical sequences eventually meet the lower-beta restriction, but no actual critical bracket conclusion follows. The old condition `beta_N N^(2s/d-1)->0`, microscopic subcriticality `beta_N N^(s/d-1)->0`, and microscopic criticality with a finite positive limit remain distinct. In particular subcritical sequences with beta_N tending to zero are not covered by this bounded-diffusivity uniformity. The logarithmic interaction is not introduced by substituting s=0.

## 8. Exact expansion under an exchangeable law

Let the N-body law be exchangeable and assume the terms below are integrable. It need not be a product law or have Haar marginals for this calculation. On collision-free configurations (6.2) is the actual configuration gradient. The same algebra also holds for any specified measurable extensions of G and A on their null exceptional sets, if the left side is defined by the finite-sum field (6.2); this asserts no derivative or trace at a collision. For the actual particle law and Haar reference all such choices are immaterial. Squaring (6.2) before any conditional simplification gives

\[
 \begin{split}
 \mathbb E\sum_i|\nabla_iP|^2=\frac1{N^3}\big[&
 (N-1)\mathbb E|H(X_1,X_2)|^2\\
 &+(N-1)(N-2)\mathbb E H(X_1,X_2)\cdot H(X_1,X_3)\\
 &-2(N-1)\mathbb E H(X_1,X_2)\cdot A(X_1)
 +\mathbb E|A(X_1)|^2\big].
 \end{split}
 \tag{8.1}
\]

There are `N-1` equal-label terms and `(N-1)(N-2)` ordered distinct pairs inside the square. Exchangeability gives the outside factor N; the original square has denominator `N^4`. The coefficient of the mixed term is exactly `-2(N-1)`. For N=2 the triple term is absent; no X_3 or third marginal is introduced.

For actual bounded-density particle laws, the conditional domain theorem and the finite-N density bound make all these terms absolutely integrable. For example the Haar triple product is integrable by

\[
 \int|H(x,y)||H(x,z)|dxdydz
 \le\int\left(\int|H(x,y)|dy\right)^2dx\le\|H\|_2^2,
\]

and the actual triple density is bounded at each fixed N. This proves existence of the reduction but is not an N-uniform estimate.

## 9. What the actual homogeneous preparation preserves

Start the actual singular N-particle dynamics from iid Haar data independent of its iid Brownian drivers. Its drift is

\[
 b_i(X)=\frac1N\sum_{j\ne i}K(X_i-X_j).
\]

For every fixed torus translation v, the path `X(t)+v` satisfies the same equation from `X(0)+v` with the same Brownian increments. For every fixed label permutation, permuting positions and Brownian motions gives the correspondingly permuted equation. The supplied pathwise uniqueness and jointly measurable per-start realization identify these transformed solution laws. The initial law is invariant under common translations and label permutations, and permuted iid Brownian motions have the same law. Fubini with the initial distribution justifies the comparison even though the source theorem did not posit a common exceptional set for every uncountable starting state/translation.

Consequently the actual N-body law is exchangeable and invariant under every common translation for each time. Its one-body marginal m_t is translation invariant. For a continuous test v on the torus, average that invariance over the translation parameter:

\[
 \int v\,dm_t=\int da\int v(x+a)\,dm_t(x)=\int v(x)dx.
\]

Thus every one-body marginal is Haar. This uses only the stipulated dynamics and preparation; it does not use the conditional corrector-domain theorem.

These two symmetries do not determine higher marginals. For example, with nonzero Fourier vector k and `|epsilon|<1`, the density

\[
 F_\epsilon(X)=1+\frac\epsilon{\binom N2}
       \sum_{i<j}\cos(2\pi k\cdot(X_i-X_j))
 \tag{9.1}
\]

is positive, exchangeable, common-translation invariant, and has Haar one-body marginals. Its pair marginal is
`1+[epsilon/binom(N,2)] cos(2 pi k.(x-y))`, which is not a product density. This is a counterexample to an inference from the symmetries alone, not an asserted formula for the evolved particle density.

In particular the mixed term of (8.1) cannot generally be discarded just because the one-body marginal is Haar. In one angular coordinate, the smooth symmetric test
`Phi=cos x+cos y+cos(2x-y)+cos(2y-x)` has normalized `A=-sin x` and
`H=-2sin(2x-y)+sin(2y-x)`. Under the translation-invariant pair density `1+epsilon cos(x-y)`, direct Fourier orthogonality gives `E[H A]=epsilon/2`, whereas its Haar-product value is zero. This is an algebraic diagnostic; the test is not claimed to be the particular backward corrector.

## 10. The exact remaining law-transfer obligation

Let `F_t^(2)` and, when `N>=3`, `F_t^(3)` be the actual pair/triple densities under iid Haar preparation. They exist by the supplied finite-N density result. The marginal probability kernels are jointly measurable in time. Equivalently, define the expressions below directly by expectations against those kernels; they are then measurable functions of time. A joint time-space density version for the integrated formulas follows by taking the Radon–Nikodym derivative of the measure `dt lambda_t` against time times Haar: the fixed-N domination is uniform on the finite interval. Define the three explicit signed deviations

\[
 \delta_{2,N}(t)=\int|H_t(x,y)|^2[F_t^{(2)}(x,y)-1]dxdy,
\]

\[
 \delta_{3,N}(t)=\int H_t(x,y)\cdot H_t(x,z)
                  [F_t^{(3)}(x,y,z)-1]dxdydz,
\]

\[
 \delta_{A,N}(t)=\int H_t(x,y)\cdot A_t(x)
                    [F_t^{(2)}(x,y)-1]dxdy.
 \tag{10.1}
\]

The triple deviation is omitted at N=2. Conditional Haar centering makes the Haar-product triple and mixed integrals zero. The actual one-body marginal being Haar makes the A-square term identical to its reference value. Thus (8.1) gives the exact, fully scaled reduction

\[
 \boxed{
 Q_{2,N}^{\rm actual}-Q_{2,N}^{\rm Haar}
 ={2\nu b_N\over N^2}\int_0^T
 \big[(N-1)\delta_{2,N}+(N-1)(N-2)\delta_{3,N}
                  -2(N-1)\delta_{A,N}\big]dt.}
 \tag{10.2}
\]

Here `Q_(2,N)^actual` is the expected scaled true-martingale bracket provided at fixed N by the conditional domain theorem. Every term exists at fixed N; no smallness is being inferred. The triple term has a different combinatorial size from the pair and mixed terms and cannot be omitted because a pair response has been solved.

One sufficient precise transfer obligation is a bound on

\[
 \mathcal E_N^{\rm law}:={2\nu b_N\over N^2}\int_0^T
 \big[(N-1)|\delta_{2,N}|+(N-1)(N-2)|\delta_{3,N}|
                       +2(N-1)|\delta_{A,N}|\big]dt.
 \tag{10.3}
\]

If this were bounded by `C b_N N^(-2/(s+2))`, the reference rate would transfer to the actual expected corrector bracket. If only `mathcal E_N^law=o(1)` were proved, actual bracket smallness would still follow from (7.1). These are conditional implications, not estimates established here. The exact signed combination in (10.2) is a potentially weaker sufficient target when cancellations can be proved.

The leading actual expected noise functional equals (7.2), since it depends only on the one-body marginal. Therefore a proved actual bound for Q_2 would also control the expected absolute cross functional by the same time/probability Cauchy–Schwarz argument. The required new information remains in the two-/three-body deviations above.

The existing density domination yields only

\[
 Q_{2,N}^{\rm actual}\le e^{(N-1)\kappa T}Q_{2,N}^{\rm Haar}
\]

for iid Haar initial density one. This finite-N comparison need not vanish with N and is not a solution of (10.3). No N-uniform correlation estimate, evolved residual bound, CLT, or critical hierarchy closure has been established by this energy gate.

## 11. Diagnostics, self-review, and per-claim disposition

The independently written diagnostic for this continuation is

```text
python3 MEMORANDA/ROUND_009_ENERGY_ARTIFACTS/round009_haar_energy_exact.py
```

It imports no prior checker and uses only exact rational arithmetic and SHA-256. The final run passes **52,103 assertions**, primarily exhaustive finite configurations and symmetry checks. Its four-node-per-coordinate rule exactly integrates the specified trigonometric polynomial products: their frequency is at most three in each coordinate. The separate absolute-cross quadrature checks only discrete Cauchy–Schwarz; the continuous absolute bound is proved in Section 7. A separate exact Fourier-orthogonality diagnostic exercises a nonzero mixed contraction under Haar one-body marginals. No numerical test is substituted for the conditional analytic prerequisite.

Checks include N=2,3 (and N=4), all finite-N deletion terms, conditional Haar means, the exact Haar identity and four-term exchangeable identity, nonproduct invariant laws, the scaled marginal-error reduction, leading-noise normalization, Coulomb compensation and its boundary sign, both response multipliers, constant h, zero noise, the actual backward Fourier sign, the backward energy sign, and all rate/boundary exponents. The Coulomb zero-diagonal test gives a positive B quadratic form, detecting an invalid assertion of full internal-drift dissipativity.

During pre-seal validation, the first checker run found that its selected first-frequency invariant test laws did not exercise a nonzero mixed term. This was a diagnostic coverage failure, not a failure of (8.1). A separate biased exchangeable-law enumeration and an exact invariant Fourier example were added; the issued run exercises the coefficient and passes. No statement or coefficient was changed to accommodate the tests.

| Claim | Disposition | Reason |
|---|---|---|
| Uniform source supremum and L1 source bounds | VERIFIED FROM SUPPLIED FULL R5 PROOF | Exact constants (2.1)–(2.4), including both responses and all N. |
| Deleted-tube diffusion and internal-drift energy inequality | PROVED CONDITIONAL ON THM028 | Fixed-N regularity justifies the limits; the Coulomb flux retains its sign and needs no trace. |
| Homogeneous response quadratic form | PROVED | Finite-measure convolution and exact frozen Fourier multipliers. |
| Uniform-in-N Haar noise energy | PROVED CONDITIONAL ON THM028 | Explicit constant C_E in (5.2), with no R8 derivative constant hidden in it. |
| Exact Haar identity and two reference-noise rates | PROVED CONDITIONAL ON THM028 | Conditional Haar centering, exact deletion, and time/Haar Cauchy–Schwarz. |
| Exchangeable-law four-term identity | PROVED whenever stated terms are integrable | Direct ordered finite-sum expansion, including N=2. |
| Actual exchangeability and one-body Haar invariance | PROVED FROM SUPPLIED PARTICLE REALIZATION | Uniqueness/equivariance plus invariant preparation; no product-law inference. |
| Actual bracket/cross smallness or rate | OPEN | Requires control of (10.2), for example the explicit sufficient condition (10.3). |

The proof, checker, result JSON, README and input/output manifests form the sealed packet. Source bytes and their nineteen hashes are preserved; the output manifest excludes itself, and a separate seal hashes the archive and output manifest. The archive contains only the permitted inputs and named outputs. A later correction must be a new superseding artifact.

The first unresolved load-bearing line after this conditional gate is precisely a suitable uniform estimate for the signed law-error combination in (10.2), or the stronger absolute quantity (10.3). No such estimate is supplied by exchangeability, Haar one-body marginals, or the current finite-N density domination.
