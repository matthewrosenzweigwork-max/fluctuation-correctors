# TASK-039 — statement-only reconstruction of THM-021

Date: 2026-09-17 UTC. Status: **independent reconstruction of the submitted statement completed**. This is not a review or verdict on the unseen constructor proof. No constructor report, other review, source dossier, or root R4/R5 mathematical note was read. No memory files were opened or used. The only mathematical inputs were the four frozen files listed in the accompanying input manifest. Repository metadata was inspected to establish isolation and protect existing changes. No external theorem was imported.

Worktree: `/private/tmp/hocf-r004-response-blind-20260917`.
Branch: `codex/hocf-r004-response-blind`.
Base: `52bda5d0d24067b051c6fe9763f2a78e7599e593`.
The exact four-file dossier was copied from the root and verified before reconstruction. The task-specific blind boundary supersedes the general instruction to read other repository orientation, orchestration, and status documents. Canonical ledgers and the root worktree were not edited. No commit, push, dependency installation, or child worker was used.

## Assertion, negation, and scope

The primary assertion is exactly the conjunction in the supplied THM-021: with its torus/Fourier normalization and positive-power range, the divergence is the stated finite signed measure; the compensated responses have the stated boundedness, representative compatibility, and heat limits; the stated failures of stronger convergence occur; and the smooth-cutoff pair propagator and its bounded response perturbation satisfy the stated estimates. The logical negation is the existence of admissible data for which at least one of these assertions fails.

Every assertion in that conjunction is reconstructed below. No missing analytical step or counterexample to that conjunction was found. This conclusion does not concern singular flow construction, convergence of smooth propagators, actual corrector forcing integrability, a weighted-space inverse, transfer between law classes, or a fluctuation theorem. Those are excluded by the submitted statement and remain outside this result. The submitted SELF_CHECKED status is not silently changed by this document; root must compare the sealed independent reconstruction with the constructor submission before any canonical disposition.

All norms without a weight use unit Haar measure. For a pair function, the space is the product of two unit Haar tori. The background is a nonnegative probability density in C1; its integral-one and nonnegativity assumptions are not needed for the operator estimates beyond the displayed bounds. The phrase “positive Riesz” is interpreted through the explicitly positive nonzero Fourier coefficients, not as pointwise positivity of a zero-mean kernel. There is no logarithmic claim.

## 1. Fourier normalization, finite divergence, and lower bound

Let H_t be the periodized Gaussian heat kernel:

\[
 H_t(x)=\sum_{n\in\mathbb Z^d}(4\pi t)^{-d/2}
              e^{-|x+n|^2/(4t)},\qquad t>0.
\]

It is nonnegative, even, smooth, and has integral one. Integrating its Fourier coefficient over the translated fundamental cubes reduces the integral to the Gaussian integral on Euclidean space. Completing the square, or one integration-by-parts differential equation for that Gaussian Fourier integral in each coordinate, gives

\[
 \widehat H_t(k)=e^{-4\pi^2|k|^2t}.
\]

Products of these multipliers give H_t*H_r=H_{t+r}. For t at least one the absolutely convergent Fourier series yields, with constants depending only on dimension,

\[
 \|H_t-1\|_\infty+\|\nabla H_t\|_\infty\le C_d e^{-2\pi^2t}.
\]

For example, factor e^{-2 pi^2 t} out of each nonzero Fourier term and bound the remaining Gaussian lattice sum at t=1; the differentiated series is handled with the additional factor 2 pi |k|. Also, by summing the Euclidean Gaussian gradient before integrating,

\[
 \|\nabla H_t\|_1
 \le\int_{\mathbb R^d}\frac{|z|}{2t}(4\pi t)^{-d/2}
                      e^{-|z|^2/(4t)}\,dz\le C_d t^{-1/2}.
\]

For any 0<r<d set alpha_r=(d-r)/2 and

\[
 A_r=\frac{2^{d-r}\pi^{d/2}}{\Gamma(r/2)},\qquad
 G_r=A_r\int_0^\infty t^{\alpha_r-1}(H_t-1)\,dt.
\]

This is an absolutely convergent L1 integral: on (0,1), the L1 norm of H_t-1 is at most two, and on (1,infinity) the preceding exponential bound applies. Fubini and the elementary gamma integral therefore give zero mean and, for k nonzero,

\[
 \widehat G_r(k)=A_r\Gamma(\alpha_r)(4\pi^2|k|^2)^{-\alpha_r}
 =\pi^{r-d/2}\frac{\Gamma((d-r)/2)}{\Gamma(r/2)}|k|^{r-d}.
\]

Thus G_r is the declared g_r. A distribution is determined by these coefficients: repeated integration by parts makes the Fourier coefficients of a smooth test decay faster than every polynomial, so its Fourier partial sums converge with every derivative; a distribution vanishing on all characters therefore vanishes on every smooth test. No unstated source normalization is used. The other elementary Fourier fact used below is Parseval. To justify it in this setting, heat smoothing of a continuous function has an absolutely convergent Fourier series, because its coefficients are bounded by the L1 norm of that function times the summable Gaussian multiplier. Heat smoothing converges uniformly to a continuous function by uniform continuity and the Gaussian tail. Fourier truncation of the smoothing therefore makes trigonometric polynomials dense among continuous functions, hence in L2. Orthogonality of the characters and this density give Parseval by taking limits of finite sums.

This representation also checks the local principal coefficient. The contribution of the Euclidean Gaussian image at zero, integrated over all positive times, is

\[
 A_r(4\pi)^{-d/2}\int_0^\infty
 t^{-r/2-1}e^{-|x|^2/(4t)}\,dt=|x|^{-r}.
\]

The equality follows by the substitution v=|x|^2/(4t). On a neighborhood of zero smaller than a fundamental cube, the other Gaussian images at times at most one have uniformly convergent differentiated sums because their distances are bounded away from zero. At times at least one, both the periodic heat tail and the Euclidean integral that was added/subtracted have integrable derivatives. The omitted -1 contribution at times at most one is finite. Consequently the difference from |x|^{-r} is smooth locally. This independently fixes the principal Riesz normalization.

Positivity of H_t supplies the needed lower bound without asserting positivity of g_r. Namely, almost everywhere,

\[
 g_r\ge-B_r,\qquad
 B_r:=A_r\left(\frac1{\alpha_r}
       +C_d\int_1^\infty t^{\alpha_r-1}e^{-2\pi^2t}\,dt\right)<\infty.
\]

For s at most d-2, alpha_s is at least one. The preceding gradient bounds imply

\[
 \int_0^\infty t^{\alpha_s-1}\|\nabla H_t\|_1\,dt<\infty.
\]

Distributional differentiation of the convergent integral is therefore legitimate and shows K=-grad g_s belongs to L1. To see the differentiation directly, test against a smooth function, integrate by parts for each positive t, and use this absolute integral to pass to the limit. No point value of the singular K is needed.

The divergence D=-Delta g_s has Fourier coefficient 4 pi^2 |k|^2 times that of g_s. When 0<s<d-2, gamma recurrence gives

\[
 4\pi^2c_{d,s}=s(d-2-s)c_{d,s+2}.
\]

Consequently, as distributions and therefore as finite signed measures,

\[
 D=s(d-2-s)g_{s+2}\,dx.
\]

It has mass zero and D is bounded below by -kappa dx with kappa=s(d-2-s)B_{s+2}. No optimal value of this lower bound is claimed.

At s=d-2, the nonzero Fourier coefficients of D are constant:

\[
 4\pi^2c_{d,d-2}
 =\frac{4\pi^{d/2}}{\Gamma((d-2)/2)}
 =(d-2)|\mathbb S^{d-1}|=:c_d.
\]

Since the zero coefficient remains zero, uniqueness of distributions gives

\[
 D=c_d(\delta_0-dx),\qquad \|D\|_{\rm TV}=2c_d,
 \qquad D\ge-c_d\,dx.
\]

The total variation follows because the point mass and Haar measure are mutually singular. In particular the compensating -c_d dx term cannot be discarded. Heat convolution preserves distributional derivatives, makes K_epsilon and D_epsilon smooth, and yields

\[
 D_\epsilon=H_\epsilon*D\ge-\kappa,
 \quad\|D_\epsilon\|_1\le\|D\|_{\rm TV},
 \quad\|K_\epsilon\|_1\le\|K\|_1.
\]

The first inequality follows by integrating the positive heat kernel against the nonnegative measure D+kappa dx; the other two follow by the triangle inequality and its integral-one property.

## 2. Reconstruction of the response and its functional meaning

For smooth pair Phi, the integrated-gradient first-slot response, with the sign fixed by K=-grad g_s, is

\[
 \mathcal R_x\Phi(x,y)
 =\int K(w)\cdot\mu(x+w)\nabla_1\Phi(x+w,y)\,dw.
\]

To integrate by parts without pretending that the singular divergence is a function, use the defining weak identity

\[
 \int f\,dD=-\int K\cdot\nabla f\,dw.
\]

It holds for every periodic C1 function: approximate that function and its first derivatives uniformly by heat smoothing, apply the smooth test identity, and pass to the limit using the finite total variation of D and the L1 norm of K. For each fixed x,y apply it to f(w)=mu(x+w)Phi(x+w,y). It gives, pointwise in x,y,

\[
 R_x\Phi(x,y)=-\int\mu(x+w)\Phi(x+w,y)D(dw)
  -\int K(w)\cdot\nabla\mu(x+w)\Phi(x+w,y)\,dw.
 \tag{2.1}
\]

This derives both signs and includes the entire periodic compensation. The second-slot response is obtained by interchanging x and y.

Formula (2.1) is defined at every x,y for every actual bounded Borel Phi. Its two integrands are jointly Borel and absolutely integrable against the finite measures in question; integration of a jointly measurable bounded integrand against a finite measure is measurable, first for simple functions and then by bounded convergence. Therefore it defines a bounded Borel function. With M0=norm(mu,infinity), M1=norm(grad mu,infinity), set

\[
 B_\mu=M_0\|D\|_{\rm TV}+M_1\|K\|_1.
\]

The pointwise triangle inequality proves the sup-space norm bound B_mu for each slot.

For Haar L2, every translation in the first slot is an isometry. The integral triangle inequality gives

\[
 \|R_x\Phi\|_2
 \le\int\|\mu(\cdot+w)\Phi(\cdot+w,\cdot)\|_2\,|D|(dw)
  +\int|K(w)|\,\|\nabla\mu(\cdot+w)\Phi(\cdot+w,\cdot)\|_2\,dw
 \le B_\mu\|\Phi\|_2.
\]

One can justify this integral inequality first for simple approximations in the integration variable, using the triangle inequality in L2, and then take limits by the displayed integrable majorants. For arbitrary L2 input representatives, absolute integrability holds almost everywhere by Fubini, since on a probability space L2 is contained in L1. Bounded truncations then give the same formula almost everywhere and the same estimate. Smooth functions are dense in Haar L2, so the extension from smooth inputs is unique. Density here can be obtained by approximating simple functions by step functions on finite unions of boxes and smoothing the boxes; the small boundary strips control the L2 error.

The quotient-space issue needs a separate check. If Phi and Psi differ on a product Haar-null set, then for each fixed w their translated difference is still Haar-null. Fubini with |D|(dw) and |K(w)|dw shows the responses agree at almost every (x,y). Hence the bounded Borel formula induces a well-defined bounded Haar-Linfinity quotient operator, with the same bound, and it agrees with the L2 extension on their common domain. This does not assert norm density of smooth functions in Linfinity.

At the Coulomb endpoint the atomic part of (2.1) is simply

\[
 -c_d\mu(x)\Phi(x,y).
\]

It is multiplication of the pair function, with no restriction to x=y and no trace of an L2 class. The compensating Haar part is c_d times the first-slot average of mu Phi. Neither interpretation requires a positive lower bound for mu.

For constant pair input, (2.1) vanishes by the same weak divergence identity applied to mu(x+w). Thus both responses kill constants, including for nonconstant backgrounds. If J denotes the slot interchange, J R_x J=R_y, so the sum preserves pair symmetry and has norm at most C_R=2B_mu in all three stated spaces. It is the sum that preserves symmetry; no separate symmetry-preservation assertion is needed for one slot.

## 3. Heat identity, convergence, and the two exclusions

Write P_epsilon^x for heat convolution in the output x variable. For fixed background mu, Fubini in (2.1), followed by addition of the translation variables, proves for every bounded Borel input and every x,y that

\[
 R_{x,\epsilon}=P_\epsilon^xR_x.
 \tag{3.1}
\]

The same relation holds on Haar L2 by the preceding extension argument, and in the y slot. In this computation heat smooths D and K, while mu and its derivative stay inside the translated input. It is not permissible to replace the unchanged mu by an unrelated approximation or to move heat to the input before multiplication by mu.

For completeness, heat convolution converges strongly on L1 and L2. Translation is continuous in these norms: this is immediate for indicators of boxes from the measure of their shifted boundary strips, extends to step functions, and then to all Lp functions by their density and the translation isometry. Thus

\[
 \|P_\epsilon f-f\|_p
 \le\int H_\epsilon(w)\|f(\cdot+w)-f\|_p\,dw\longrightarrow0,
 \qquad p=1,2.
\]

Indeed, first restrict to a small neighborhood of zero where translation continuity makes the integrand small; outside that neighborhood the periodized Gaussian mass tends to zero, and the integrand is at most 2 norm(f,p). The Gaussian concentration claim follows by unfolding the periodization and using its Euclidean Gaussian tail. These facts also prove uniform convergence of heat smoothing on continuous functions and their continuous first derivatives used above.

Below Coulomb, D has an L1 density. Applying the response estimate to the kernel differences gives, both on Haar L2 and the pointwise bounded Borel sup space,

\[
 \|R_{x,\epsilon}-R_x\|_{\rm op}
 \le M_0\|D_\epsilon-D\|_1+M_1\|K_\epsilon-K\|_1\longrightarrow0.
 \tag{3.2}
\]

The argument is uniform over backgrounds with common M0 and M1; the sum has twice this bound. In particular Borel discontinuity of the input causes no problem here: it is the kernels that converge in L1, and no sup-space approximation of the input is used.

At Coulomb, let Pi_x denote the first-slot Haar average, and let T_K use the plus-translation convention appearing in (2.1). The formula becomes

\[
 R_x\Phi=-c_d\mu\Phi+c_d\Pi_x(\mu\Phi)
                 -T_K(\nabla\mu\,\Phi).
\]

Heat leaves the middle term unchanged. Consequently

\[
 (R_{x,\epsilon}-R_x)\Phi
 =-c_d(P_\epsilon^x-I)(\mu\Phi)
                    -T_{K_\epsilon-K}(\nabla\mu\,\Phi).
 \tag{3.3}
\]

This identifies exactly where operator-norm convergence can fail. It also proves the stronger uniformity over bounded backgrounds that is part of the submitted assertion. With dist the torus distance and

\[
 m_1(\epsilon)=\int H_\epsilon(w)\operatorname{dist}(w,0)\,dw
            \le\sqrt{2d\epsilon},
\]

the Lipschitz bound on mu and the integral triangle inequality yield

\[
 \|(P_\epsilon^x-I)(\mu\Phi)\|_2
 \le M_0\|(P_\epsilon^x-I)\Phi\|_2
        +M_1m_1(\epsilon)\|\Phi\|_2.
\]

The moment bound follows by unfolding the Gaussian, using torus distance at most the Euclidean distance, and applying Cauchy-Schwarz to its second moment 2d epsilon. Thus

\[
 \|(R_{x,\epsilon}-R_x)\Phi\|_2
 \le c_dM_0\|(P_\epsilon^x-I)\Phi\|_2
  +M_1\bigl(c_dm_1(\epsilon)+\|K_\epsilon-K\|_1\bigr)\|\Phi\|_2.
 \tag{3.4}
\]

There is an identical y estimate. Its right side tends to zero for each fixed input and depends on the background only through the common M0,M1 bounds. No modulus of continuity for grad mu beyond those bounds is smuggled into this estimate.

If the input ranges over a compact subset of L2, convergence of each heat difference is uniform: choose a finite eta-net, use strong convergence on its finitely many members, and use the contraction bound norm(P-I) at most two for the distance to that net. Norms on the compact set are bounded. Applying (3.4) proves the desired uniformity, including a continuous L2 input family indexed by a compact time interval. Time-dependent backgrounds may be chosen independently as long as their common M0,M1 bounds hold. In particular continuous C1 backgrounds on a finite interval supply those bounds.

The exact L2 operator-norm obstruction follows from mu=1. In this case

\[
 (R_{x,\epsilon}+R_{y,\epsilon})-(R_x+R_y)
       =c_d(2I-P_\epsilon^x-P_\epsilon^y).
\]

On the character with pair frequencies (k,l), its multiplier is

\[
 c_d\bigl(2-e^{-4\pi^2\epsilon|k|^2}
              -e^{-4\pi^2\epsilon|l|^2}\bigr).
\]

All these multipliers are between zero and 2c_d, and they approach 2c_d when both frequencies diverge. Parseval therefore gives operator norm exactly 2c_d at every fixed positive epsilon. The supremum need not be attained by one Fourier character. This is consistent with strong convergence because the nearly extremizing input frequencies depend on epsilon.

The claimed Borel sup-space failure is also exact. Put Phi(x,y)=1 when x=y and zero otherwise, and still take mu=1. A slice in either integrated variable is a singleton, of Haar measure zero. The smooth-cutoff responses are therefore identically zero. The unsmoothed atom gives R_x Phi=R_y Phi=-c_d Phi, and the compensating Haar terms vanish. The sup norm of the two-response difference is exactly 2c_d for every positive epsilon. This Borel Phi represents the zero Haar-L2 and Haar-Linfinity class, so there is no contradiction with the quotient-space statements. No diagonal trace on an arbitrary Haar-L2 class was used.

If a different background mu_epsilon is introduced, the response difference acquires at most

\[
 \|\mu_\epsilon-\mu\|_\infty\|D\|_{\rm TV}
 +\|\nabla\mu_\epsilon-\nabla\mu\|_\infty\|K\|_1
\]

per slot, using the heat-kernel norm contractions when necessary. Hence the unchanged-background premise matters, and new background approximations require their own C1 control.

## 4. Independent exact Fourier falsification route

This route uses the integrated-gradient expression directly, not the measure formula, to test signs, compensation, heat placement, and the second response factor. Let a_n be the declared Fourier coefficient of g_s, with a_0=0. For a background character with frequency m and pair input with frequencies (k,l), direct integration of the three Fourier factors gives the first-slot coefficient, at output frequency (k+m,l),

\[
 -4\pi^2\,k\cdot(k+m)\,a_{k+m}\,\widehat\mu(m).
 \tag{4.1}
\]

The zero output frequency gives zero. Independently, the two terms in (2.1) give

\[
 -4\pi^2|k+m|^2a_{k+m}\widehat\mu(m)
 +4\pi^2m\cdot(k+m)a_{k+m}\widehat\mu(m),
\]

which sum to (4.1). In particular k=0 gives zero even for nonconstant mu; dropping the density-gradient term would fail this test. At Coulomb, divide by c_d. For nonzero k+m, the coefficient is exactly

\[
 -\frac{k\cdot(k+m)}{|k+m|^2}\widehat\mu(m).
\]

Choose a nonzero integer p, mu(x)=1+(1/2)cos(2 pi p.x), and Phi(x,y)=exp(2 pi i p.(x+y)). This background is smooth, positive, and has integral one. The exact sum is

\[
 (R_x+R_y)\Phi
 =-2c_d e^{2\pi i p\cdot(x+y)}
 -\frac{c_d}{8}\left(e^{2\pi i p\cdot(2x+y)}
                         +e^{2\pi i p\cdot(x+2y)}\right).
 \tag{4.2}
\]

At the resonant m=-p frequency, the Coulomb atom contributes -c_d/4 and the periodic compensation contributes +c_d/4; their zero-mode cancellation is exact. A local-only divergence formula would create a spurious constant-in-one-slot term. For m=p the coefficient is -c_d/8, so reversing the density-gradient sign would also fail (4.2).

With a heat-smoothed interaction, each first-slot term in (4.1) is multiplied by exp(-4 pi^2 epsilon |k+m|^2). The factor belongs to the output frequency, verifying (3.1) in a case where moving heat through the nonconstant background would give a different answer. The y calculation supplies the second response and restores pair symmetry. Complex characters are a concise calculation device; their real and imaginary parts give real admissible tests.

The accompanying standard-library checker performs exact rational Coulomb calculations on 36 mode pairs, constant inputs, the resonant compensation, (4.2), output heat-frequency tags, the homogeneous factor two, and the pair-divergence factor at N=2,3,7,101. It uses no floating-point approximation, random sampling, source formula beyond those reconstructed here, or imported software package. Its finite tests are falsification evidence, not substitutes for Sections 1–3 or 5–6.

## 5. Smooth-cutoff pair propagation, including zero diffusion

Fix epsilon>0, N at least two, and nu at least zero. Let z=(x,y) and define the smooth vector field on the product torus

\[
 B_t(x,y)=\left(u_t(x)+\frac1N K_\epsilon(x-y),\;
                 u_t(y)-\frac1N K_\epsilon(x-y)\right).
\]

The sign in the second component is essential. Direct differentiation gives

\[
 \operatorname{div}_{x,y}B_t
 =\operatorname{div}u_t(x)+\operatorname{div}u_t(y)
                      +\frac2N D_\epsilon(x-y)
 \ge-2a(t)-\frac{2\kappa}{N}.
 \tag{5.1}
\]

This calculation fixes the exact 2/N interaction divergence before any estimate. Write b_*(t)=a(t)+kappa/N, a nonnegative integrable function on the finite interval.

Here is a construction and estimate that does not appeal to an unproved singular-flow theorem or to elliptic regularity. Lift the smooth periodic drift to Euclidean space, take standard 2d-dimensional Brownian motion W, and solve

\[
 X_t=z+\int_r^t B_q(X_q)\,dq+\sqrt{2\nu}(W_t-W_r).
\]

For each continuous Brownian sample path, subtract the displayed additive noise. The resulting ordinary integral equation has a continuous time-dependent drift with a global spatial Lipschitz constant on this fixed parameter tuple. Picard iteration contracts on intervals shorter than the reciprocal of that constant; finitely many such intervals cover the horizon. The ordinary integral estimate for the difference of two solutions gives uniqueness. These iterations are adapted and measurable. They also work when nu=0.

The solution map F_{r,t}^W in its initial point is a smooth torus diffeomorphism. To verify rather than assume the needed part of that fact, differentiate the Picard equations: the first derivative solves

\[
 J_t=I+\int_r^t \nabla B_q(X_q)J_q\,dq.
\]

Difference quotients converge to this solution by uniform derivative bounds and the integral Gronwall estimate. Higher derivatives follow by the same differentiated integral equations; only the first is used below. The matrix inverse is obtained from its corresponding linear ODE, so J remains invertible. Differentiating the determinant by multilinearity gives

\[
 \det J_t=\exp\left(\int_r^t\operatorname{div}B_q(X_q)\,dq\right)
        \ge\exp\left(-2\int_r^t b_*(q)\,dq\right).
 \tag{5.2}
\]

Global invertibility follows by solving the same integral equation backwards from a given endpoint along the fixed continuous noise path. Uniqueness gives both inverse identities. Periodicity gives compatibility with the torus quotient. Thus ordinary change of variables applies pathwise; this argument does not differentiate a Brownian path.

Define the backward transition operator P_{r,t}f(z)=E[f(F_{r,t}^W(z))]. It is positive, preserves constants, and satisfies P_{r,t}=P_{r,q}P_{q,t}: concatenate the unique solutions and condition on the independent Brownian increments after q. Smooth Itô calculus, whose coefficients and derivatives here are bounded, identifies its generator as

\[
 L_t=\nu(\Delta_x+\Delta_y)+u_t(x)\cdot\nabla_x+u_t(y)\cdot\nabla_y
          +\frac1N K_\epsilon(x-y)\cdot(\nabla_x-\nabla_y).
\]

Jensen, the pathwise change of variables, and (5.2) imply for bounded smooth f

\[
 \begin{aligned}
 \|P_{r,t}f\|_2^2
 &\le E\int|f(F_{r,t}^W(z))|^2\,dz\\
 &\le\exp\left(2\int_r^t b_*(q)\,dq\right)\|f\|_2^2.
 \end{aligned}
\]

The unique bounded extension to L2 therefore satisfies exactly

\[
 \boxed{\ \|P_{r,t}\|_{2\to2}
       \le\exp\left(\int_r^t[a(q)+\kappa/N]\,dq\right).\ }
 \tag{5.3}
\]

All existence and smoothness constants used to construct this fixed-cutoff flow may depend on epsilon, N, nu, and the drift. The norm bound (5.3) contains only the displayed uniform lower-divergence data. Consequently it is uniform over these parameters whenever that data is uniform, including nu=0. It does not by itself yield any compactness or limiting singular propagator.

For clarity about evolution orientation, P_{r,t} acts on terminal functions and solves the backward equation in r. For a smooth terminal f, set q(tau)=P_{t-tau,t}f. Then q satisfies the forward equation in tau with generator L_{t-tau}. Its energy identity provides a separate coefficient check:

\[
 \frac12\frac{d}{d\tau}\|q\|_2^2
 =-\nu\|\nabla q\|_2^2
   -\frac12\int\operatorname{div}B_{t-\tau}\,|q|^2
 \le b_*(t-\tau)\|q\|_2^2.
\]

Thus the divergence factor 2/N becomes the norm exponent kappa/N, not 2 kappa/N. The backward differentiability used here follows for smooth functions from the transition identity, Itô's formula on a short interval, and smooth dependence of F on its initial point. Formula (5.3) was already proved without this energy check.

The L2 transition family is strongly continuous in its endpoints. For continuous f, this follows from the continuous sample paths, bounded drift, and uniform continuity of f, using bounded convergence for the Brownian expectation. The dependence on the starting endpoint also follows from the same integral equation and uniqueness. Approximate any L2 input by continuous functions and use (5.3); absolute continuity of the integral of b_* controls the norms over shrinking intervals. These arguments justify the L2 time integrals in the next section.

## 6. Bounded response perturbation and the precise remaining boundary

For continuous t -> mu_t in C1, let S_t=R_{x,epsilon,t}+R_{y,epsilon,t}. Section 2 and heat contraction give

\[
 \|S_t\|_{2\to2}\le C_R(t)
 :=2\left(\|\mu_t\|_\infty\|D\|_{\rm TV}
                  +\|\nabla\mu_t\|_\infty\|K\|_1\right).
\]

This is a continuous finite function of t on the compact interval. The difference estimate with mu_t-mu_r also proves that S_t is continuous in operator norm. Fix terminal f in L2 and prescribed Bochner forcing F in L1([0,T];L2). The corresponding backward mild equation is

\[
 \Phi_r=P_{r,T}f
       +\int_r^T P_{r,q}\bigl(S_q\Phi_q+F_q\bigr)\,dq.
 \tag{6.1}
\]

This makes explicit the orientation and the data needed for the submitted mild-solution assertion. Changing the sign of the bounded response would have the same norm argument, but (6.1) uses the displayed added response.

To prove existence and uniqueness, begin with the terminal-plus-forcing term and iterate the response integral. Strong continuity from Section 5, operator continuity of S, and integrability of F make each term a continuous L2 function. In the n-th iterate, the ordered time simplex and (5.3) give at most

\[
 e^{\int_0^T b_*}\frac{\bigl(\int_0^T C_R(q)\,dq\bigr)^n}{n!}
\]

times the appropriate bounded initial iterate norm. The factor 1/n! follows by partitioning the n-dimensional time cube into the n! orderings; the product of C_R values is permutation invariant. The series converges uniformly in L2. Passing to the integral by domination proves (6.1). For the difference of two solutions, the same n-th iteration bound tends to zero, which proves uniqueness. Continuity of the forcing integral follows by splitting off a small end interval and using its L1 norm there, then applying strong continuity and domination on the remaining interval. No derivative of an arbitrary L2 solution is taken.

Summing the ordered products from any intermediate time gives the quantitative estimate

\[
 \|\Phi_r\|_2\le
 e^{\int_r^T[b_*(q)+C_R(q)]\,dq}\|f\|_2
 +\int_r^T e^{\int_r^q[b_*(v)+C_R(v)]\,dv}\|F_q\|_2\,dq.
 \tag{6.2}
\]

In particular the homogeneous perturbed propagator has norm exponent a+kappa/N+C_R(t), as asserted. Uniformity requires uniform bounds on the displayed quantities only; the forcing is prescribed, and its actual appearance in a corrector equation is not proved here.

Finally, for the stated one-way conversion,

\[
 \|\Phi\|_{L^2(\mu\otimes\mu)}^2
 =\int|\Phi(x,y)|^2\mu(x)\mu(y)\,dx\,dy
 \le M_0^2\|\Phi\|_2^2.
\]

Taking square roots gives the factor M0. Without a positive lower bound for mu there is no reverse norm comparison. None of these estimates defines a diagonal trace of an arbitrary L2 pair class.

## 7. Reconstruction disposition and seal

- **Finite-measure divergence and periodic compensation:** reconstructed from the frozen Fourier definition, with the principal Riesz coefficient checked directly.
- **Bounded Borel, Haar L2, and Haar Linfinity responses:** reconstructed, including representative independence and the absence of a pair-diagonal trace.
- **Constants and pair symmetry:** reconstructed, with an independent nonconstant-background Fourier check.
- **Heat identity and convergence:** reconstructed. Below Coulomb the convergence is operator norm; at Coulomb it is strong, uniformly over the stated background class and compact input families.
- **Excluded convergence assertions:** the exact L2 operator norm 2c_d and the bounded-Borel diagonal-indicator failure are both proved.
- **Smooth propagation and bounded perturbation:** reconstructed for all stated finite parameters, with exact divergence 2D_epsilon/N and norm exponent kappa/N; zero diffusion is included.
- **Unseen constructor proof:** no judgment issued. The present record is an independently derived statement-level argument to be compared only after this seal.
- **Beyond the submitted scope:** no singular flow/limit, diagonal trace, weighted inverse, law-class transfer, forcing integrability theorem, or fluctuation closure is obtained.

Verification command: `python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RESPONSE_RECONSTRUCTION_CHECK.py`. Result: PASS, with exact rational arithmetic and the JSON output saved next to the checker. Input SHA256 checks were run before reconstruction and again before sealing. The output manifest hashes this report, the exact checker, its saved output, and the copied input manifest. It deliberately does not hash itself. No TeX source was generated or modified, and no build or mathematical certification beyond the argument and checks just stated is claimed.

The report is sealed by that output manifest. Any correction after issuance must be a new separately hashed document, not an edit to these sealed bytes. Root alone may integrate results and update canonical state.
