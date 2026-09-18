# Round 009 — statement-only reconstruction of Haar energy and law reduction

TASK-056. Issued 2026-09-18 UTC. **CONDITIONAL PROOF COMPLETED / BLIND RECONSTRUCTION; separate hostile review pending.** The condition is the full THM028 domain prerequisite exactly as frozen, together with the supplied earlier pair-process, inverse and particle-realization modules. This report does not audit or certify the R8 constructor. No counterexample to THM029 was found. The proof below gives all of its claimed bounds and identities; a uniform pointwise-in-time energy bound is also obtained to cover the cross-density wording without assuming that it denotes only a time integral.

The new argument uses only the nineteen copied inputs named in `ROUND_009_ENERGY_BLIND_INPUT_SHA256SUMS.txt`. All nineteen original hashes were checked before copying and rechecked afterward. The worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r009-energy-blind`, branch `codex/hocf-r009-energy-blind`, created from published R7 `4171be9839feb8acf4c70e1dda014458fdb44490`. It was clean before the assigned output directory was created. The narrow task dossier overrides general instructions to inspect unrelated current state, histories, README/specification, or orchestration files. Those were not read. No TASK055/root energy seed, R9 constructor/checker, other audit, later state/history, memory, private source, or other worker output was read. The R8 proof was consulted only as a source for the explicitly provisional domain premise; references within permitted sources were not followed outside the allowlist. No root/canonical edit, commit, push, dependency installation or child agent was used.

## 1. Exact assertion, negation, and conventions

Fix integer d at least 3, exponent `0<s<=d-2`, a finite horizon T, a finite upper diffusivity `nu_*>=0`, smooth real terminal h, and the exact coefficient-one periodic Fourier Riesz kernel in the frozen model. For every integer `N>=2` and `0<=nu<=nu_*`, take external drift zero, reference density one on the unit Haar torus, the exact Fourier backward test f, and the unique symmetric full pair inverse Phi with terminal value zero. Put

\[
 p=s+2,\qquad a=\frac{s}{s+2}\in(0,1),\qquad
 Bv=K(x-y)\cdot(\nabla_x-\nabla_y)v,\qquad R=R_x+R_y.
 \tag{1.1}
\]

The full THM028 premise includes its off-diagonal classical equation, boundedness, global Haar H1 and W2,1 properties, weighted derivative bounds for each fixed N, and the actual particle Itô/bracket assertions. It is not shortened to a formal PDE. We will use its N-dependent derivative bounds only for fixed-parameter limiting and derivative-identification arguments. All quantitative constants in the new energy/noise estimates depend only on `d,s,T,nu_*,h` and the frozen kernel/cutoffs.

The primary assertion is the complete conjunction in THM029: the uniform Haar energy estimate, the exact deleted-pair Haar identity, the stated reference noise/cross rates, the exact exchangeable-law reduction, and exchangeability plus one-particle Haar invariance for iid-Haar-prepared actual particles. Its uniform-bound negation means that for some fixed admitted data no finite such constant works over N and nu (equivalently there is an unbounded normalized sequence), or that one of the exact identities or law assertions fails at an admitted instance. For a fixed finite tuple, an unspecified constant can always be enlarged; the uniform quantifier is therefore retained explicitly here.

No evolved-law smallness, corrected centering limit, Gaussianity, hierarchy closure, logarithmic normalization, inhomogeneous theorem, or assertion uniform as diffusivity tends to infinity is part of this reconstruction. The old condition `beta_N N^(2s/d-1)->0`, the full subcritical condition `beta_N N^(s/d-1)->0`, and the critical condition `beta_N N^(s/d-1)->lambda>0` remain distinct.

## 2. Source and normalization preflight

The following are exact permitted-source locations, with their limits retained.

| Input | Location used | Scope imported here |
|---|---|---|
| Frozen model and R1 algebra | `TASKS/ACTIVE/ROUND_001_MODEL.md`; `MEMORANDA/ROUND_001_ALGEBRA.md` (1.2)–(1.4), (2.3), (3.1)–(3.2) | Unit Haar mass; Fourier characters; `sqrt(2nu)` noise; ordered distinct labels, denominator N squared, factor one half; both response slots. All new gradient/bracket coefficients are reconstructed below. |
| R4 response proof/card | `MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md`, Sections 2–4; THM021 | Exact local coefficient one, smooth even remainder, integrable force, finite divergence measure with lower bound, both compensated response formulas. |
| R5 base pair proof/card | `MEMORANDA/ROUND_005_PERIODIC_PAIR_POTENTIAL.md`, Sections 2–5 and 9, especially (9.3); THM023 | Noncolliding auxiliary pair, source occupation comparison, and singular Haar measure domination. The latter, not merely an L2 operator norm, supplies the L1 bound below. |
| R5 full inverse/interface | `MEMORANDA/ROUND_005_CONDITIONAL_FULL_PAIR_INVERSE.md`; `MEMORANDA/ROUND_005_FULL_PAIR_INTERFACE_AND_HOMOGENEOUS_DATA.md`; THM024/025; the two permitted R5 clarifications | Borel Volterra inverse with both responses, its identification, and the actual homogeneous Fourier test. Pair symmetry means coordinate exchange, not Haar self-adjointness. |
| R6 particle realization | THM026; `MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, Sections 4, 6–8 | Pathwise unique measurable noncolliding particle realization, heat passage, and fixed-N density domination. No uniform law transfer is imported. |
| Provisional R8 domain | THM028; `MEMORANDA/ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, Sections 5, 7–11 | Exactly the conditional domain/Itô premise. Its weighted constants are not uniform energy constants and its proof is not certified by this report. |

For clarity, the kernel normalization is

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)}.
 \tag{2.1}
\]

The R4 heat integral gives, in an embedded ball, `g(z)=|z|^(-s)+q(z)` with q smooth and even. Thus

\[
 K(z)=s|z|^{-s-2}z+k(z),\quad k(0)=0,\quad |k(z)|\le L_k|z|.
 \tag{2.2}
\]

The finite divergence measure D has mass zero and satisfies `D>=-kappa dx`, after increasing kappa if needed to also dominate the fixed R5 smooth-remainder lower bound. At Coulomb,

\[
 D=c_d(\delta_0-dx),\quad
 c_d=(d-2)|\mathbb S^{d-1}|=4\pi^2c_{d,d-2}.
 \tag{2.3}
\]

The gamma recurrence verifies the last equality. Below Coulomb the singular positive density has coefficient `s(d-s-2)` and is locally integrable; the periodic compensation is retained. In particular the ordinary divergence off zero is at least minus kappa in both cases. No singular divergence is evaluated along a colliding configuration.

The homogeneous responses are exactly

\[
 R_xv(x,y)=-\int v(x+w,y)D(dw),\qquad
 R_yv(x,y)=-\int v(x,y+w)D(dw).
 \tag{2.4}
\]

Each acts boundedly on Haar L1, L2 and bounded Borel sup norm, with bound `||D||TV`. For L1 this follows directly from Tonelli applied to absolute values and translation invariance. Write `C_R=2||D||TV`. At the Coulomb atom (2.4) multiplies the value at (x,y); it never requests v(x,x).

The Fourier multiplier of D is

\[
 d_k=4\pi^2c_{d,s}|k|^{s+2-d}>0\quad(k\ne0),\qquad d_0=0.
\]

Consequently both responses together are dissipative on Haar L2:

\[
 \langle v,Rv\rangle_{L^2}
 =-\sum_{k,\ell}(d_k+d_\ell)|\widehat v(k,\ell)|^2\le0.
 \tag{2.5}
\]

First prove this for finite Fourier sums. Because `s+2-d<=0`, the multiplier is bounded; alternatively use the finite-measure L2 bound. Density and boundedness then pass the identity to every L2 v. This is Fourier positivity of this specific constant-background convolution operator, not positivity inferred from a pointwise weight.

Finally the actual backward test has coefficients

\[
 \widehat f_t(k)=\widehat h(k)e^{-a_k(\nu)(T-t)},\qquad
 a_k(\nu)=4\pi^2\nu|k|^2+4\pi^2c_{d,s}|k|^{s+2-d}
 \quad(k\ne0),
 \tag{2.6}
\]

and its constant coefficient is that of h. Rapid Fourier decay gives uniform C2 bounds on both f and its time derivative over `0<=nu<=nu_*`. Differentiation and the Fourier/response interchange are justified by absolute summability with polynomial factors, uniformly on this interval.

For `J_t=K(x-y).(grad f_t(x)-grad f_t(y))`, the gradient difference gains a factor |x-y|. Splitting the local ball from its complement therefore gives

\[
 \sup_{t,N,\nu}\|J_t\|_1\le C_J,\qquad
 \sup_{t,N,\nu}\|\dot J_t\|_1\le C'_J,
 \qquad J\in C^1([0,T];L^1).
 \tag{2.7}
\]

Here `|J|<=C(|x-y|^(-s)+1)`, and the same holds for its time derivative. The radial L1 exponent is `d-s>0`, including Coulomb. The constants in (2.7) depend only on the admitted fixed data.

## 3. Uniform sup bound and an independently quantified L1 time derivative

### 3.1 The sup bound used in the energy estimate

We spell out the N dependence in the permitted R5 comparison, rather than use the finite-N bound from the domain premise. Put `c=2sp` and, for `r>0,tau>=0`, define

\[
 F_{N,\tau}(r)=\frac N4\left[(r^p+c\tau/N)^{2/p}-r^2\right]
 =s\int_0^\tau(r^p+cu/N)^{-s/p}\,du.
 \tag{3.1}
\]

In relative coordinates the pair diffusion is `2nu Delta`, and the singular radial drift is `(2s/N)r^(-s-2)z`. Direct differentiation gives

\[
 \partial_\tau F-\frac{2s}{N}r^{-s-1}F_r=sr^{-s},\quad
 -rF_r\le sF,\quad
 \Delta F=\frac N2[Q^{s/p}(d+s-sQ)-d]\le0,
 \quad Q=\frac{r^p}{r^p+c\tau/N}.
 \tag{3.2}
\]

For the last sign, the derivative of `Q^(s/p)(d+s-sQ)` is
`(s/p)Q^(s/p-1)[d+s-(2s+2)Q]`, which is nonnegative since `d>=s+2`; the value at one is d. Concavity of the power `2/p` also gives

\[
 0\le F_{N,\tau}(r)\le\frac{c^{2/p}}4N^a\tau^{2/p}.
 \tag{3.3}
\]

Choose the fixed local cutoff chi from the R5 proof, equal to one on radius R0 and zero beyond R1. On its annulus, `F<=s tau r^(-s)` and `|F_r|<=s^2 tau r^(-s-1)`. Set `H=sup||D^2 f||infinity`, `G=sup||grad f||infinity`, `K_out=sup_(r>=R0)|K|`, and

\[
\begin{split}
 B_J&=HL_kR_0^2+2GK_{\rm out},\\
 C_1&=\|\nabla\chi\|_\infty,\quad C_2=\|\Delta\chi\|_\infty,\quad
 V_*=sR_0^{-s-1}+L_kR_1,\\
 E_*&=sR_0^{-s}(2\nu_*C_2+V_*C_1)
       +4\nu_*C_1s^2R_0^{-s-1},\\
 \alpha&=1+sL_k,\quad C_B=B_J+HE_*/\alpha.
\end{split}
 \tag{3.4}
\]

All are independent of N and nu in the admitted interval. The factor four in the last diffusion cross term is due to the relative diffusion `2nu Delta`. The full product rule, the bound `|2k/N|<=L_k r`, and (3.2) give the supersolution

\[
 W_N(\tau,z)=e^{\alpha\tau}[H\chi(z)F_{N,\tau}(|z|)+C_B\tau],
 \qquad (\partial_\tau-L^{\rm pair})W_N\ge |J|.
 \tag{3.5}
\]

Indeed the cutoff errors are at most `HE_* tau`, the regular radial drift costs at most `sL_k H chi F`, and `alpha-sL_k=1`, `alpha C_B-HE_*=alpha B_J>=0`. This is the complete fixed-annulus compensation; no whole-space radial function is differentiated across a torus cut locus.

Apply ordinary Itô to (3.5) on compact collision stops for the supplied noncolliding auxiliary pair process. Discard the nonnegative stopped terminal value; monotone convergence of absolute occupation as the stops are removed gives `|U_N(t,x,y)|<=W_N(T-t,x-y)`. This is precisely the R5 source comparison, with the singular passage performed before invoking any full-corrector PDE. In particular

\[
 \sup_t\|U_N(t)\|_\infty\le C_U N^a,\quad
 C_U=e^{\alpha T}\left[H\frac{c^{2/p}}4T^{2/p}+C_BT\right].
 \tag{3.6}
\]

Both responses are restored by the exact Volterra equation. Its iterated time simplexes and the Borel Markov sup contraction give

\[
 M_N:=\sup_t\|\Phi_t\|_\infty\le C_\Phi N^a,
 \qquad C_\Phi=C_Ue^{C_RT}.
 \tag{3.7}
\]

The series uses coefficient one for each response, including its compensation. It is the already specified true full inverse by the permitted uniqueness module. This proof imports no weighted derivative constant from R8.

### 3.2 A uniform L1 bound on the actual time derivative

This extra bound allows a pointwise energy inequality, so no interpretation of the cross-density sentence requires an unproved passage from an integrated estimate to a timewise one.

The model is time homogeneous at fixed N and nu. Write S_r for its base pair semigroup. The singular Haar measure domination in the R5 full proof (9.3), valid for every nonnegative Borel input, gives

\[
 \|S_r v\|_1\le e^{2\kappa r/N}\|v\|_1.
 \tag{3.8}
\]

This is an L1 extension with well-defined equality-class action. Strong continuity follows first for continuous functions by continuous paths and bounded convergence, then for all L1 functions by continuous approximation and (3.8). Composition extends by the same density argument. These are consequences of the stated measure inequality; an L2 norm alone would not justify (3.8).

Construct the full L1 evolution T_r by its ordered Dyson series with S and the bounded operator R. A term with m insertions has norm at most
`exp(2kappa r/N)(C_R r)^m/m!`, since the intervening time intervals sum to r. Thus

\[
 \|T_r\|_{1\to1}\le e^{\gamma r},\qquad \gamma=\kappa+C_R,
 \quad 0\le r\le T,
 \tag{3.9}
\]

uniformly in N and nu. The series is strongly continuous, by strong continuity of S, dominated simplex integration and uniform convergence on finite horizons. R need not be a Markov operator or commute with S.

Tonelli, (2.7), and (3.8) identify the Borel source potential with `int_0^(T-t) S_r J_(t+r) dr` in L1. Expanding the Borel Volterra inverse from (3.7) in L1 and rearranging the absolutely summable simplexes then yields

\[
 \Phi_t=\int_0^{T-t}T_rJ_{t+r}\,dr\quad\hbox{in }L^1.
 \tag{3.10}
\]

There is no source-regularization interchange here: the singular source is already L1 and the direct singular occupation formula is the input. The absolute bound for the m-th integral is at most `C_J exp(kappa T) C_R^m T^(m+1)/(m+1)!`, so all rearrangements are justified.

Differentiate (3.10) after the change to the r variable. Strong continuity, `J in C1(L1)`, and the norm majorant (3.9) justify the endpoint and integral terms, giving

\[
 \dot\Phi_t=-T_{T-t}J_T+\int_0^{T-t}T_r\dot J_{t+r}\,dr,
 \qquad
 \sup_t\|\dot\Phi_t\|_1\le
 C_{\dot\Phi}:=e^{\gamma T}(C_J+TC'_J).
 \tag{3.11}
\]

The same time-differentiation identity is visible in the permitted R8 proof, Section 7, (7.4). The L1 evolution, differentiation justification, and N-uniform quantitative bound here have been reconstructed from (3.8)–(3.10); no bound from that R8 construction is imported. This includes one-sided endpoint derivatives. It identifies the actual classical derivative from the THM028 premise: its fixed-N weighted bound by an integrable multiple of `r^(-s)` permits the pointwise fundamental theorem and dominated differentiation in L1. Hence that L1 derivative must equal (3.11). The premise is used to identify derivatives, while the quantitative bound in (3.11) was established with constants independent of N and nu.

## 4. Singular energy integration, including Coulomb, without a trace

Fix N, nu and t for this paragraph. Let `theta_epsilon(x-y)` be a smooth function equal to zero for `r<=epsilon`, one for `r>=2epsilon`, radially nondecreasing on its transition annulus, and constant one outside the embedded chart. It has

\[
 \|\nabla_{x,y}\theta_\epsilon\|_2\le C\epsilon^{(d-2)/2}\longrightarrow0.
 \tag{4.1}
\]

By (2.2), `K(z).z/r>0` for every sufficiently small positive r. Therefore `B theta_epsilon>=0` on the annulus, including at Coulomb.

Multiply the classical pair equation by `theta_epsilon Phi` and integrate. Everything is classical on the support away from the diagonal. Integration by parts in the internal drift gives exactly

\[
 I_\epsilon:=\int\theta_\epsilon\Phi B\Phi
 =-\int\theta_\epsilon(\operatorname{div}_{\rm cl}K)(x-y)\Phi^2
   -\frac12\int\Phi^2 B\theta_\epsilon
 \le\kappa\int\theta_\epsilon\Phi^2.
 \tag{4.2}
\]

The pair vector field is `(K,-K)`, whose ordinary pair divergence is twice `div K`; this explains the absence of another factor two in the first term. The last integral has the favorable sign and is dropped, not evaluated at the diagonal. In particular at Coulomb the first term is `c_d int theta_epsilon Phi^2`, and the nonpositive annular flux accounts for the missing positive distributional atom. No limit or trace for that flux is assumed. Replacing (4.2) by an exact global identity with `Phi(x,x)^2` would be unjustified and is not done.

The diffusion term is

\[
 \nu\int\theta_\epsilon\Phi\Delta\Phi
 =-\nu\int\theta_\epsilon|\nabla\Phi|^2
   -\nu\int\Phi\nabla\theta_\epsilon\cdot\nabla\Phi.
\]

Its last term tends to zero, since its absolute value is bounded by
`nu M_N ||grad theta_epsilon||2 ||grad Phi_t||2`. The last factor is finite for this fixed tuple by the H1 domain premise. This is the only quantitative use of that possibly N-dependent norm, and it disappears in the limit. No uniform bound is inferred from it.

All other limits are justified directly: `Phi dotPhi` is L1 by (3.7), (3.11); `Phi J` is L1 by (2.7); the response pairing converges by its bounded L2 action; the squared gradient is integrable by the domain premise. Equivalently the weighted fixed-N bounds provide dominating functions. Rearranging the cut-off PDE, using (4.2), and then sending epsilon to zero gives

\[
\begin{split}
 \nu\|\nabla_{x,y}\Phi_t\|_2^2
 &\le \int\Phi_t\dot\Phi_t+\int\Phi_tJ_t
       +\frac\kappa N\|\Phi_t\|_2^2+\langle\Phi_t,R\Phi_t\rangle\\
 &\le M_N(C_{\dot\Phi}+C_J)+\frac\kappa N M_N^2\\
 &\le C_*N^a,
 \qquad C_*=C_\Phi(C_{\dot\Phi}+C_J)+\kappa C_\Phi^2.
\end{split}
 \tag{4.3}
\]

Here (2.5) retains both responses with their exact sign, unit Haar mass gives `||Phi||2<=M_N`, and `2a-1<=a` because a is below one. This last exponent comparison is why the internal-drift loss closes with the sup estimate. Every constant in C_* has the required fixed-data dependence. There is no division by nu, so (4.3) also holds at zero noise.

Integration in time now proves exactly

\[
 \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt\le TC_*N^{s/(s+2)}.
 \tag{4.4}
\]

For comparison, one could obtain (4.4) alone by integrating the cutoff energy identity in time, dropping the nonpositive initial energy and using (3.7). The pointwise proof additionally justified the uniform L1 time derivative; it does not infer a pointwise statement from (4.4). At T=0 the integral is zero. At nu=0 every noise functional below is exactly zero and no unweighted gradient estimate as nu tends to zero is asserted.

## 5. Exact deleted-pair Haar coefficients and reference noise

For a fixed time suppress t and put

\[
 q(x)=\int\Phi(x,y)dy,\quad c=\int\Phi(x,y)dxdy,\quad
 G(x,y)=\nabla_x\Phi(x,y),\quad A(x)=\int G(x,y)dy.
\]

Fubini for the global weak derivatives, or the background-contraction part of THM028, gives `grad q=A`. In particular A is in L2 and `||A||2<=||G||2`. Symmetry gives `||grad_(x,y)Phi||2^2=2||G||2^2`. The exact statistic and its particle derivative are

\[
 P=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
     -\frac1N\sum_iq(X_i)+\frac12c,
\qquad
 \nabla_iP=\frac1{N^2}\sum_{j\ne i}G(X_i,X_j)-\frac1N A(X_i).
 \tag{5.1}
\]

The ordered-pair factor one half cancels the two ways i appears. The background term retains its different denominator. These identities hold as global weak derivatives under Haar, and classically on collision-free configurations with the stated differentiated background. No omitted term is a diagonal trace.

Set `H(x,y)=G(x,y)-A(x)`. Then

\[
 \nabla_iP=N^{-2}\left[\sum_{j\ne i}H(X_i,X_j)-A(X_i)\right].
 \tag{5.2}
\]

Under the reference product Haar law, conditional on X_i, the H terms have zero means and distinct j terms are conditionally independent. Expanding the square and integrating gives

\[
\begin{split}
 \int\sum_i|\nabla_iP|^2dm_N
 &=N^{-3}\big[(N-1)\|H\|_2^2+\|A\|_2^2\big]\\
 &=\frac{N-1}{N^3}\|G\|_2^2
   -\frac{N-2}{N^3}\|A\|_2^2.
\end{split}
 \tag{5.3}
\]

All products are integrable by Cauchy–Schwarz, so conditioning and Fubini are justified. At N=2 the second coefficient is zero. For an additive pair kernel `Phi(x,y)=v(x)+v(y)`, H vanishes and the actual answer is `N^(-3)||grad v||2^2`; this stresses the residual background term in (5.2). For a constant terminal h, J and Phi are exactly zero by uniqueness, so all theorem functionals vanish.

For positive nu take `nu=1/beta_N`, `b_N=min(beta_N,1)` and `sigma_N^2=N b_N`. The exact physical corrector bracket density is `2nu sum_i|grad_iP|^2`. By (5.3), pair symmetry and (4.4), its Haar-time integral satisfies

\[
\begin{split}
 Q_P^{\rm Haar}
 &:=\sigma_N^2\int_0^T\int 2\nu\sum_i|\nabla_iP_t|^2dm_Ndt\\
 &\le b_N\frac{N-1}{N^2}
       \nu\int_0^T\|\nabla_{x,y}\Phi_t\|_2^2dt\\
 &\le Cb_NN^{a-1}=Cb_NN^{-2/(s+2)}.
\end{split}
 \tag{5.4}
\]

The same bound holds for the density at each time, with C_* in place of TC_*, by (4.3). The `2nu` Brownian factor and the equality of the two slot-gradient norms have canceled once, exactly as displayed. Bounded diffusivity requires `beta_N>=1/nu_*` when nu_* is positive; nu=0 is a separate limit, not the reciprocal of a finite beta.

For the leading statistic `eta_N(f_t)`, the particle gradient is `N^(-1)grad f_t(X_i)`. Its Haar-averaged bracket density after multiplication by sigma squared is

\[
 \sigma_N^2\int 2\nu\sum_i|N^{-1}\nabla f_t(X_i)|^2dm_N
 =2\nu b_N\|\nabla f_t\|_2^2\le2\|\nabla f_t\|_2^2,
 \tag{5.5}
\]

because `nu b_N<=1`. Its time integral is uniformly bounded as well. The signed cross-variation density before scaling is exactly

\[
 c_t(X)=2\nu\sum_iN^{-1}\nabla f_t(X_i)\cdot\nabla_iP_t(X).
 \tag{5.6}
\]

Pointwise Cauchy–Schwarz in the particle components, followed by Cauchy–Schwarz under Haar and then in time, gives

\[
 \sigma_N^2\int_0^T\int|c_t(X)|dm_Ndt
 \le\sqrt{Q_P^{\rm Haar}Q_f^{\rm Haar}}
 \le C\sqrt{b_N}\,N^{-1/(s+2)}.
 \tag{5.7}
\]

The same bound for `sigma_N^2 int|c_t|dm_N` at each deterministic t follows from the timewise version of (5.4) and (5.5). Thus the absolute-density assertion holds either timewise or integrated over the fixed horizon. These remain reference-law functionals. They are not asserted to be the expected brackets of the evolved interacting particles.

## 6. The exact exchangeable-law reduction

Let F be an exchangeable N-body probability law for which the displayed quantities are defined and integrable. No product assumption is made. The purely finite-sum formula (5.2) gives, by expanding its square and distinguishing equal from unequal partner labels,

\[
\begin{split}
 \mathbb E_F\sum_i|\nabla_iP|^2
 =\frac1{N^3}\big[&(N-1)\mathbb E_F|H(X_1,X_2)|^2\\
 &+(N-1)(N-2)\mathbb E_F H(X_1,X_2)\cdot H(X_1,X_3)\\
 &-2(N-1)\mathbb E_F H(X_1,X_2)\cdot A(X_1)
   +\mathbb E_F|A(X_1)|^2\big].
\end{split}
 \tag{6.1}
\]

At N=2 the triple summation is empty and its expectation is omitted altogether; no X3 is defined. The coefficients count N choices of the distinguished label, N-1 partner choices, and `(N-1)(N-2)` ordered distinct partner choices, against denominator N to the fourth. The cross term with A has the factor minus two. This derivation uses exchangeability only to identify equal expectations after expansion.

For the actual collision-free particle law there is no diagonal-representative issue. More generally (6.1) is understood wherever the terms are defined almost surely; it does not prescribe values of a singular derivative on a collision set. Arbitrary measurable representatives, if supplied, do not alter the algebra but do not create a classical diagonal derivative either.

Suppose now the one-particle marginal is Haar, as proved for the actual preparation in Section 7. Let `F_t^(j)` denote its j-label marginal as a measure. Define the three signed marginal discrepancies

\[
\begin{split}
 D_{2,H}(t)&=\int |H_t(x,y)|^2\,d(F_t^{(2)}-dxdy),\\
 D_{2,HA}(t)&=\int H_t(x,y)\cdot A_t(x)\,d(F_t^{(2)}-dxdy),\\
 D_{3,H}(t)&=\int H_t(x,y)\cdot H_t(x,z)\,d(F_t^{(3)}-dxdydz).
\end{split}
 \tag{6.2}
\]

The last definition is needed only for N at least 3. The reference integrals of the last two integrands are zero, by their conditional centering. Consequently, with

\[
 Z_N(t)=(N-1)D_{2,H}(t)+(N-1)(N-2)D_{3,H}(t)
                  -2(N-1)D_{2,HA}(t),
\]

there is the exact difference identity

\[
 \mathbb E\sum_i|\nabla_iP_t|^2
  -\int\sum_i|\nabla_iP_t|^2dm_N=\frac{Z_N(t)}{N^3}.
 \tag{6.3}
\]

Hence the exact expected-bracket correction after time integration and fluctuation scaling is

\[
 \frac{2b_N}{N^2}\int_0^T\nu Z_N(t)dt.
 \tag{6.4}
\]

This identifies the needed law bridge without transferring conditional independence from Haar. A sufficient, explicit set of uniform estimates is

\[
\begin{split}
 \int_0^T\nu|D_{2,H}(t)|dt&\le C N^a,\\
 \int_0^T\nu|D_{2,HA}(t)|dt&\le C N^a,\\
 \int_0^T\nu|D_{3,H}(t)|dt&\le C N^{a-1}\quad(N\ge3).
\end{split}
 \tag{6.5}
\]

They would make (6.4) of size at most `C b_N N^(a-1)`. A bound directly on the time integral of the positive part of Z_N would also suffice; the separate absolute estimates are sufficient rather than necessary. None of (6.5) is proved for the evolved particle law here. If the actual self-bracket bound were supplied, the cross bound would follow by the same Cauchy–Schwarz argument, because the actual leading self-bracket expectation already equals (5.5) under the one-body Haar marginal.

The available density bound is only `F_t<=exp((N-1)kappa T)` for iid Haar initial law. Applied directly to a nonnegative bracket density, it introduces that exponential factor. It ensures finite-N integrability but supplies none of the uniform estimates (6.5), especially the extra inverse-N requirement in the centered triple pairing. Mean zero under Haar is not mean zero under the evolved joint law.

## 7. What the actual dynamics imply about their law

The supplied particle module gives a measurable pathwise unique solution of

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)dt+\sqrt{2\nu}\,dW_i,
 \tag{7.1}
\]

from an independent initial random vector with iid Haar coordinates. It lies off all pair collisions almost surely for the whole finite horizon. This preparation has bounded density one, so THM026/THM028 also supply the integrability required above, with their permitted finite-N constants.

For any permutation pi, permuting the initial labels and Brownian motions gives a solution with the correspondingly permuted path, because the drift sum is equivariant. Pathwise uniqueness identifies the two solution maps almost surely. The permuted initial vector and independent Brownian family have the same joint law. Thus the entire particle path law, and every fixed-time law, are exchangeable.

For a fixed torus translation v, add v to every initial coordinate and every solution coordinate, leaving the Brownian increments unchanged. The force differences are unchanged. Pathwise uniqueness again gives this translation equivariance. Product Haar initial data are invariant under the common translation, and are independent of the noises. Hence the N-body time-t law is invariant under every common translation. Each one-body marginal is therefore invariant under every torus translation. To identify it, integrate the identity `int psi(x+v)dmu_t(x)=int psi(x)dmu_t(x)` in Haar v for a continuous psi; Fubini makes the left side `int psi dx`. Continuous tests identify the marginal as Haar.

These arguments apply for every fixed translation/permutation; they do not assume a common exceptional event for all uncountably many starting states or translations. The supplied joint measurability permits integration of the per-start almost-sure statement against the initial law. They also apply at nu=0. No conclusion of independence among two or three evolved labels has been made.

As a separate falsification test of any attempted symmetry-to-independence inference, the exact checker uses the strictly positive density

\[
 1+\frac14\operatorname{av}_{i\ne j}\cos(2\pi(x_i-x_j))
  +\frac15\operatorname{av}_{i,j,k\,\mathrm{distinct}}
                      \cos(2\pi(x_i+x_j-2x_k)),
 \tag{7.2}
\]

with the triple term absent at N=2. Coordinates here mean the first coordinate of each admitted d-dimensional torus. Its density is at least `1-1/4-1/5>0`, its mass is one, and it is exchangeable, invariant under common translations, and has Haar one-body marginals. Its two-body marginal is nonproduct. This is a countermodel to the illicit inference, not an identification of the actual evolved law.

## 8. Independent falsification route, exact tests, and hostile self-check

The analytic reconstruction uses a local source barrier, uniform L1 evolution, and collision-tube energy integration. The separate finite diagnostic route constructs P from literal ordered sums of rational Laurent polynomials and differentiates it before taking Haar coefficients or pairing it with the nonproduct density (7.2). It does not encode the conditional-covariance proof as its left-hand side.

Command:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/round009_energy_exact_checks.py
```

Result: **PASS, 4,994 exact assertions**, recorded in `round009_energy_exact_results.json`. Python's standard library only; no random seed, numerical tolerance or external dependency. The checks include:

- N=2,3,4,5 for literal deleted-pair gradients, the exact Haar coefficients, additive/relative/separable/mixed/constant pair tests, and the arbitrary exchangeable two-/three-marginal identity.
- A nonproduct exchangeable translation-invariant law with one-body Haar marginals, so the law reduction is also tested away from the reference product class.
- The diffusion product rule and, at N=2,3, the full smooth interacting generator product rule for cross brackets. These retain all physical `2nu`, `1/N`, `1/N^2`, `1/2`, and fluctuation factors.
- Finite Fourier response dissipation, both Coulomb compensation slots, exact smooth internal-drift integration, and exact instantaneous PDE energy balance for zero and positive noise, multiple finite spectra, and N=2,3,17.
- Exact rational radial profile, transport, drift absorption, Laplacian-sign and sup-bound checks, including Coulomb and fractional exponents over dimensions 3 through 12; all rate exponent identities and the Coulomb gamma-recurrence factor.
- Every one of the nineteen frozen input digests.

The Fourier convention in the checker removes a common `(2pi)^2` from expressions with two derivatives and retains the sign `i^2=-1`. Its first derivative is `D_i=(2pi i)^(-1) partial_i`; all two-derivative physical formulas therefore restore exactly `(2pi)^2`. The finite Coulomb spectrum tests the supported multipliers only. It is not substituted for the singular Coulomb boundary, which is treated analytically in Section 4.

The strongest new claim was challenged at the following vulnerable lines:

| Challenge | Disposition |
|---|---|
| Could a finite-N R8 gradient constant leak into the uniform energy constant? | No. It is used only to make the cutoff diffusion error vanish for each fixed tuple. The surviving constants are (2.7), (3.7), (3.11), and the fixed divergence bound. |
| Could L2 propagation have been silently treated as L1 propagation? | No. (3.8) uses the full R5 Borel measure inequality (9.3), explicitly present in the allowlisted full proof. |
| Does differentiating the time formula require an unproved generator derivative of the singular semigroup? | No. The variable change fixes T_r; only J and the moving upper endpoint are differentiated in L1. |
| Does a Coulomb atom require a trace? | No. The inner flux is nonpositive and discarded before the limit. The actual response atom multiplies Phi(x,y). |
| Is response dissipativity a generic weighted positivity claim? | No. It follows from the exact homogeneous Fourier multiplier with both slots. |
| Does integrated energy alone imply the timewise cross-density claim? | No such implication is used. The separate L1 derivative estimate proves the timewise energy bound (4.3). |
| Could the N=2 triple coefficient conceal an undefined X3? | The triple term is absent at N=2, both in the proof and code. |
| Does one-body Haar symmetry remove the triple correlation? | No; it remains explicitly in (6.2)–(6.5), and (7.2) falsifies the purported general inference. |
| Does zero noise require division by nu? | No. All energy/noise statements retain the factor nu and all noise functionals are exactly zero there. |

These are same-context hostile self-checks and exact supporting diagnostics. They are not the separate fresh hostile audit required by TASK-056. No external source or unverifiable literature claim is imported.

## 9. Per-claim disposition and first remaining unsupported line

| THM029 component | Verdict in this reconstruction | Reason |
|---|---|---|
| Uniform Haar energy for all N and bounded diffusivity, including Coulomb | PROVED CONDITIONAL ON THE FULL DOMAIN PREMISE | Sections 2–4; even the pointwise energy bound (4.3) is obtained with allowed constant dependence. |
| Exact Haar derivative identity | PROVED GIVEN THE DECLARED DERIVATIVES | Literal finite sum (5.1), conditional square expansion (5.3); no evolved-law assumption. |
| Reference corrector self-noise rate | PROVED CONDITIONAL ON THE ENERGY/DOMAIN PREMISE | Exact factor calculation (5.4). |
| Reference absolute cross-noise rate | PROVED CONDITIONAL ON THE ENERGY/DOMAIN PREMISE | Timewise and time-integrated versions follow from (4.3)–(5.7). |
| Exact arbitrary-exchangeable-law reduction | PROVED WHEN TERMS ARE DEFINED AND INTEGRABLE | Finite-label expansion (6.1), with the N=2 triple term absent. |
| Exchangeability and one-body Haar invariance of iid-Haar-prepared singular particles | PROVED FROM THE SUPPLIED PARTICLE REALIZATION | Permutation and common-translation equivariance plus uniqueness; Section 7. |
| Uniform evolved-law bracket/residual control or fluctuation limit | NOT CLAIMED / OPEN | The required pair/triple discrepancy bounds (6.5), or an equally effective control of (6.4), are not supplied. |
| THM028 itself | NOT AUDITED HERE | It remains an explicit provisional prerequisite until its separate fresh gates pass. |

No unsupported line was found inside THM029 conditional on its full stated prerequisite and permitted earlier modules. Unconditional promotion must wait for THM028's separate audits and the fresh hostile review of this report. The first subsequent unsupported analytic line is a uniform estimate for the actual-law discrepancy (6.4), especially the centered distinct-triple pairing with the inverse-N improvement in (6.5). The finite-N density exponential does not close that line. All references used were permitted, exact local sources; no literature or novelty claim requires external verification.

## 10. Handoff and immutability

The issued packet consists of this report, the independent exact checker and JSON results, a README, the nineteen copied input files, copied-input/output manifests, and a sealed archive. The output manifest excludes itself. The archive contains only the named output packet and copied inputs, not the inherited worktree tree. A separate seal hashes the archive and output manifest. The report remains immutable after issuance; any correction requires a new separately named report.

Verification: 4,994 exact assertions pass; all nineteen original/copied hashes agree; output hashes are checked; the archive is tested for CRC, exact member set, and member-by-member SHA-256 agreement; the assigned branch and base HEAD are verified. There is no TeX artifact in this assigned Markdown/checker packet, and no build or dependency installation was requested or performed. Root may compare with the withheld constructor only after receiving the completed seal. Root integration and every remaining audit decision are separate from this worker's output.
