# Round 001: the fixed-smooth backward pair estimate

- Task: `TASK-006`, activated `PO-001a`, candidate `THM-008`.
- Author/workstream: `/root/smooth`, accepted worker setting Astra Max.
- Date: 2026-09-17 UTC.
- Worktree: `/private/tmp/hocf-round001-smooth-20260917`.
- Branch and baseline: `codex/hocf-r001-smooth`, `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Frozen input: `TASKS/ACTIVE/ROUND_001_MODEL.md`, version 1.0, and the activated task card.
- Mathematical status: `PROVED_CANDIDATE` for the bounded smooth lemma below.
- Audit status: `SELF_CHECKED`. The two proofs and the explicit tests in this memorandum were produced in one context; they are not an isolated reconstruction or a hostile audit.
- Source status: the smooth proof is self-contained. No claim from the imported note or a private source is used as a theorem. The singular diagnostic in Section 7 uses the Fourier sequence frozen in the dossier; primary verification of its identification with the stated Riesz normalization remains the separate source-audit lane.

The pair equation has a symmetric solution and an explicit bound uniform in every integer `N >= 2` and every `nu >= 0`, provided the displayed background and test norms are uniformly bounded. The requested interval `0 <= nu <= 1` is therefore covered, and the same argument also covers `beta < 1`. No uniformity of the background or the one-body test is inferred from the mean-field equation. The estimate is for a fixed smooth kernel. It neither closes the fluctuation hierarchy nor survives removal of a Riesz cutoff by the bounds proved here.

## 1. Statement, negation, and normalization

The torus is \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), with mass-one Haar measure and Fourier characters \(e_k(x)=e^{2\pi i k\cdot x}\). Fix \(T<\infty\), an integer \(m\ge2\), a smooth real even zero-mean kernel \(g\), and a smooth periodic potential \(V\). Set

\[
 K=-\nabla g,\qquad b=-\nabla V,\qquad
 u_t=b+K*\mu_t.
\]

For each parameter choice, \(\mu_t\) is a nonnegative probability density, smooth in space and continuous in time with its spatial derivatives. In the campaign it is the prescribed strictly positive mean-field solution. The analytic argument only uses its mass, nonnegativity, and the first derivative bound stated below; it does not divide by \(\mu_t\). Bounds on higher derivatives can depend on the parameters without entering the displayed estimate. All data are spatially smooth, as in the frozen model, so that every differentiation below is justified.

For a scalar function on a torus of any dimension, use the componentwise norm

\[
 \|h\|_{C^j}=\max_{|\alpha|\le j}\|\partial^\alpha h\|_\infty.
\]

For vector-valued functions take the additional maximum over components. Define the following actual norms, with no implicit uniformity:

\[
 \begin{split}
 \kappa_j&:=\max_{1\le a\le d,\ |\alpha|\le j}
                  \|\partial^\alpha K_a\|_\infty,\qquad 0\le j\le m,\\
 b_m&:=\|b\|_{C^m},\\
 M_1(t)&:=\sum_{a=1}^d\|\partial_a\mu_t\|_{L^1},\\
 A_m&:=b_m+\tfrac32\kappa_m,\\
 R_m(t)&:=2\bigl(d\kappa_m+\kappa_0 M_1(t)\bigr),\\
 c_m(t)&:=2d(2^m-1)A_m+R_m(t).
 \end{split}
 \tag{1.1}
\]

In particular, \(b_m\) and \(\kappa_m\) are bounded by the componentwise \(C^{m+1}\) norms of \(V\) and \(g\), respectively. A uniform \(C^1\) bound on \(\mu_t\) is sufficient for a uniform \(M_1(t)\), because the torus has volume one. A positive lower bound on \(\mu_t\) does not enter these constants.

The frozen response and internal interaction operators are

\[
 \begin{split}
 R_{x,t}\Phi(x,y)
   &=\int K(z-x)\cdot\nabla_z\Phi(z,y)\mu_t(z)\,dz,\\
 R_{y,t}\Phi(x,y)
   &=\int K(z-y)\cdot\nabla_z\Phi(x,z)\mu_t(z)\,dz,\\
 B\Phi(x,y)&=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi(x,y),\\
 L_{2,t}&=u_t(x)\cdot\nabla_x+u_t(y)\cdot\nabla_y
       +\nu(\Delta_x+\Delta_y)+R_{x,t}+R_{y,t}.
 \end{split}
 \tag{1.2}
\]

**Bounded smooth lemma.** For every integer \(N\ge2\), every \(\nu\ge0\), and every continuous-in-time smooth real symmetric forcing \(F_t(x,y)\), the final-value problem

\[
 (\partial_t+L_{2,t}+B/N)\Phi_t=-F_t,
 \qquad \Phi_T=0
 \tag{1.3}
\]

has a unique smooth spatial solution, which is symmetric and satisfies

\[
 \boxed{\quad
 \|\Phi_t\|_{C^m}
 \le \int_t^T
       \exp\!\left(\int_t^s c_m(r)\,dr\right)
       \|F_s\|_{C^m}\,ds.
 \quad}
 \tag{1.4}
\]

Uniqueness is understood in the mild \(C^m\) class constructed below; smooth classical solutions belong to that class. All time integrals in the estimate may be replaced by integrable bounds on the displayed quantities.

The exact negation is that some permitted data and parameters admit no such solution, fail uniqueness in the stated class, fail symmetry, or violate (1.4) with the quantities defined in (1.1). The proofs below exclude this negation at fixed smooth kernel. They do not exclude failure of a different assertion with constants independent of a singular cutoff, or without a uniform background/test hypothesis.

For the campaign forcing, the coordinator confirmed the normalization

\[
 J_{f_t}(x,y)
   =K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)).
 \tag{1.5}
\]

It is symmetric, and \(J_{f_t}(x,x)=0\). The one-body quadratic drift is
\(U_2[J_f]/2=P_N[J_f]\), so that the source \(-J_f\) in (1.3) cancels that drift with no additional factor of two. For ordered deleted-label statistics the denominator remains \(N^2\), as in the frozen dossier.

Leibniz's rule, with the norm just specified, gives

\[
 \|J_{f_t}\|_{C^m}
   \le d\,2^{m+1}\kappa_m\|f_t\|_{C^{m+1}}.
 \tag{1.6}
\]

Consequently, if \(M_{1,T}=\sup_{r\le T}M_1(r)\) and
\(F_{m+1,T}=\sup_{r\le T}\|f_r\|_{C^{m+1}}\), then

\[
 \sup_{t\le T}\|\Phi_t\|_{C^m}
 \le d\,2^{m+1}\kappa_m\,T
       e^{\Gamma_m T} F_{m+1,T},
 \quad
 \Gamma_m=2d(2^m-1)(b_m+\tfrac32\kappa_m)
           +2d\kappa_m+2\kappa_0M_{1,T}.
 \tag{1.7}
\]

This displays every dependence on \(g,V,\mu,T,f,d,m\). It has no direct dependence on \(N\) or \(\nu\). For parameter-dependent \(\mu^{N,\nu}\) or \(f^{N,\nu}\), those parameters can still enter through the two displayed norms. The argument does not supply a bound for a one-body backward solution merely by naming it a propagator.

## 2. Two operator facts needed by both proofs

### 2.1 The response loses no derivatives

Write a pair multi-index as \((\alpha,\beta)\), corresponding to \((x,y)\), with \(|\alpha|+|\beta|\le m\). For \(R_x\), there are two cases.

If \(\alpha=0\), integrate by parts once in the integration variable:

\[
 \partial_y^\beta R_x\Phi(x,y)
 =-\int \operatorname{div}_z\!\bigl(K(z-x)\mu(z)\bigr)
          \partial_y^\beta\Phi(z,y)\,dz.
 \tag{2.1}
\]

There is no boundary term on the torus. The absolute value is bounded by
\((d\kappa_1+\kappa_0M_1)\|\Phi\|_{C^m}\).

If \(|\alpha|\ge1\), use the original form rather than differentiating the integrated-by-parts kernel:

\[
 \partial_x^\alpha\partial_y^\beta R_x\Phi(x,y)
 =(-1)^{|\alpha|}\sum_{a=1}^d
   \int (\partial^\alpha K_a)(z-x)
          \partial_{z_a}\partial_y^\beta\Phi(z,y)\mu(z)\,dz.
 \tag{2.2}
\]

Here \(|\beta|+1\le m\), so the absolute value is at most
\(d\kappa_m\|\Phi\|_{C^m}\). The same two cases with the variables exchanged apply to \(R_y\). Therefore

\[
 \|(R_{x,t}+R_{y,t})\Phi\|_{C^m}
 \le R_m(t)\|\Phi\|_{C^m}.
 \tag{2.3}
\]

This argument needs only \(K\in C^m\) and \(\mu\in W^{1,1}\) at the level of the estimate. Differentiating the integrated-by-parts kernel in every case would impose an unnecessary \(C^{m+1}\) norm on \(K\). Differentiating only the original response in every case would incorrectly require a \(C^{m+1}\) norm on \(\Phi\). The split above avoids both losses.

### 2.2 The internal interaction is part of the transport

On \(\mathbb T^{2d}\), put

\[
 a_t^N(x,y)=
 \left(u_t(x)+\frac{K(x-y)}N,
       u_t(y)-\frac{K(x-y)}N\right),\qquad
 G_t^N=a_t^N\cdot\nabla+\nu\Delta_{x,y}.
 \tag{2.4}
\]

Thus \(L_2+B/N=G^N+R_x+R_y\). Since \(\mu_t\) is a probability density,

\[
 \|u_t\|_{C^m}\le b_m+\kappa_m,
 \qquad
 \|a_t^N\|_{C^m}\le b_m+(1+N^{-1})\kappa_m\le A_m.
 \tag{2.5}
\]

The smaller actual drift derivative norm may replace \(A_m\) throughout. In particular, the homogeneous example has \(u=0\), so its only transport coefficient is \(K/N\). The coarser bound (2.5) is chosen to apply to every background uniformly.

Multiplication by \(1/N\) does not make a first-order differential operator bounded from \(C^m\) to itself. Section 5 gives an explicit Fourier sequence proving that \(B/N\) is unbounded on \(C^m\) for every fixed finite \(N\) when the kernel in that example is nonzero. Treating it as a bounded perturbation of independent transport would leave a derivative-loss gap. Its inclusion in (2.4) closes that gap.

## 3. First proof: additive-noise flow and a bounded-operator Volterra equation

This construction gives existence, uniqueness, and a uniform estimate independently of the differentiated maximum principle in Section 4.

Let \(n=2d\). For \(t\le s\), solve the auxiliary pair equation

\[
 dZ_s=a_s^N(Z_s)\,ds+\sqrt{2\nu}\,dW_s,
 \qquad Z_t=z,
 \tag{3.1}
\]

where \(W\) is a standard \(n\)-dimensional Brownian motion. These are auxiliary characteristics for the pair PDE; they are not an assertion about a closed two-particle marginal of the interacting system. At \(\nu=0\) this is an ordinary characteristic flow.

For completeness, on a periodic lift subtract the continuous path
\(\sqrt{2\nu}(W_s-W_t)\). The remaining equation is an ordinary integral equation with a globally Lipschitz spatial vector field, uniformly on compact time intervals. Successive approximation on short intervals, with contraction factor given by the Lipschitz bound times the interval length, gives a unique pathwise solution. Concatenation gives the solution on \([t,T]\). Boundedness of the periodic drift prevents explosion. Spatial difference quotients and their integral equations give its derivatives by induction. In particular,

\[
 \frac d{ds}D_z Z_s=Da_s^N(Z_s)D_zZ_s,
 \qquad D_zZ_t=I.
 \tag{3.2}
\]

The Brownian term has no spatial derivative. All higher variational equations contain only spatial derivatives of \(a^N\), so their bounds do not depend on \(\nu\), including as \(\nu\to\infty\).

Here is an explicit finite-order bound. Write \(\Pi_r\) for the set partitions of \(\{1,\ldots,r\}\). Let

\[
 c_1^*=1,\qquad
 c_r^*=\frac1{r-1}
       \sum_{\substack{\pi\in\Pi_r\\|\pi|\ge2}}
          \prod_{D\in\pi}c_{|D|}^*,\quad r\ge2,
 \qquad
 W_m=\max\{1,\max_{1\le r\le m}r c_r^*\}.
 \tag{3.3}
\]

These are finite constants depending only on \(m\). In multilinear operator norms, the derivatives of \(a^N\) of orders \(1,\ldots,m\) are bounded by
\(\ell_m=n^{(m+1)/2}A_m\). If \(H=\int_t^s\ell_m\,dr\), the variational equations give

\[
 \|D_z^r Z_s\|_{\mathrm{op}}\le c_r^*e^{rH},
 \qquad 1\le r\le m.
 \tag{3.4}
\]

Indeed the case \(r=1\) is Gronwall applied to (3.2). At order \(r\ge2\), the term with one block is \(Da^N D^rZ\); every other partition uses lower derivatives. Assuming (3.4) below order \(r\), variation of constants bounds the latter terms by
\(e^H\int_0^H e^{(r-1)v}\,dv\) times the sum in (3.3), which is at most \(c_r^*e^{rH}\). This proves the claimed induction without a stochastic derivative estimate.

For the propagator \(P_{t,s}h(z)=\mathbb E[h(Z_s^{t,z})]\), the finite chain rule and (3.4) imply

\[
 \|P_{t,s}h\|_{C^m}
 \le C_{n,m}\exp\left(q_{n,m}\int_t^s A_m\,dr\right)
                   \|h\|_{C^m},
 \quad C_{n,m}=n^{m/2}W_m,
 \quad q_{n,m}=m n^{(m+1)/2}.
 \tag{3.5}
\]

The factor \(n^{m/2}\) is the elementary comparison of componentwise and multilinear norms. Differentiation under expectation is justified by the deterministic bounds (3.4). The same construction proves strong continuity on \(C^m\); one can first check it on smooth functions and then use their approximation in \(C^m\) and the uniform bound (3.5).

Smooth Itô calculus gives the backward equation for \(P_{t,s}\). The desired solution therefore obeys

\[
 \Phi_t=\int_t^T P_{t,s}
               \bigl(F_s+(R_{x,s}+R_{y,s})\Phi_s\bigr)\,ds.
 \tag{3.6}
\]

Start with the term containing \(F\), and iterate the bounded response operator. The term with \(k\) response insertions is integrated over an ordered time simplex. Products of the exponential factors in (3.5) telescope across adjacent propagation intervals; the extra factors \(C_{n,m}\) contribute \(C_{n,m}^{k+1}\). The simplex bound is the factorial bound for the ordered integral of \(R_m\). Hence the series converges in \(C([0,T];C^m)\), and

\[
 \|\Phi_t\|_{C^m}
 \le C_{n,m}\int_t^T
 \exp\left(\int_t^s
       \bigl(q_{n,m}A_m+C_{n,m}R_m(r)\bigr)\,dr\right)
       \|F_s\|_{C^m}\,ds.
 \tag{3.7}
\]

Applying the same iteration to the difference of two solutions yields zero: the remainder bound contains a factorial in the number of response insertions. This proves uniqueness. Applying the construction at every finite spatial order for smooth data gives a spatially smooth solution. The equation then gives its time differentiability; no ellipticity lower bound was used. Swapping \(x,y\) commutes with \(G^N\) because \(K\) is odd, and swaps the two responses. Uniqueness therefore gives symmetry for symmetric forcing.

## 4. Second proof of the estimate: differentiated PDE and a maximum principle

This proves the sharper stated bound (1.4) directly, without the flow derivative or Volterra estimates. The first proof supplies a solution on which to perform the calculation; the a priori estimate and uniqueness argument here do not use that proof's bound.

Set \(\Psi_\tau=\Phi_{T-\tau}\). Equation (1.3) becomes the forward equation

\[
 \partial_\tau\Psi
   =a_{T-\tau}^N\cdot\nabla\Psi
       +\nu\Delta\Psi+(R_x+R_y)_{T-\tau}\Psi+F_{T-\tau},
 \qquad \Psi_0=0.
 \tag{4.1}
\]

For a pair multi-index \(\gamma\) with \(|\gamma|\le m\), set
\(w_\gamma=\partial^\gamma\Psi\). Its differentiated drift equation contains

\[
 \partial^\gamma(a^N\cdot\nabla\Psi)
 =a^N\cdot\nabla w_\gamma
  +\sum_{j=1}^{2d}\sum_{0<\delta\le\gamma}
      {\gamma\choose\delta}
      (\partial^\delta a_j^N)
      \partial^{\gamma-\delta+e_j}\Psi.
 \tag{4.2}
\]

Every derivative of \(\Psi\) in the sum has order at most \(m\). Since
\(\sum_{0<\delta\le\gamma}{\gamma\choose\delta}=2^{|\gamma|}-1\), this commutator is bounded by

\[
 2d(2^m-1)A_m\|\Psi\|_{C^m}.
 \tag{4.3}
\]

There is no differentiated diffusion error because \(\nu\) is spatially constant. At a spatial maximum of \(w_\gamma\), its gradient is zero and its Laplacian is nonpositive. The same applies to \(-w_\gamma\). Thus the transport term vanishes there and the diffusion term has the favorable sign for every \(\nu\ge0\). Taking the maximum over the finitely many derivatives, the upper right Dini derivative of
\(Y(\tau)=\|\Psi_\tau\|_{C^m}\) satisfies

\[
 D^+Y(\tau)
 \le c_m(T-\tau)Y(\tau)+\|F_{T-\tau}\|_{C^m},
 \qquad Y(0)=0,
 \tag{4.4}
\]

where (2.3) bounds the differentiated response. The elementary integrating-factor argument for this scalar inequality, followed by the change of variables back to \(t\), is exactly (1.4). Applied to a solution difference with zero forcing it also proves uniqueness in the smooth class. This calculation explains both the absence of any inverse diffusion coefficient and the full time orientation in the exponential of (1.4).

For the frozen smooth inputs the construction gives \(\Phi\in C([0,T];C^m)\) at every finite order, and the equation gives \(\Phi\in C^1([0,T];C^{m-2})\). Thus no approximation argument is needed for the differentiations or the terminal derivative used below. Uniform bounds on higher derivatives of a parameter-dependent background are not needed to obtain (1.4); spatial smoothness for each fixed parameter is enough to justify the calculation.

## 5. Concrete solvable falsification tests

These tests derive the operator directly on Fourier functions. They are distinct from the maximum-principle and flow proofs. They are same-context self-checks, not an independent audit.

### 5.1 Zero interaction: the heat equation, including zero diffusion

Take \(K=0\), \(b=0\), and \(\mu=1\). Then \(R_x=R_y=B=0\). For a symmetric real Fourier mode \(H\) formed from \(e_p(x)e_q(y)\), with frequency pair \((p,q)\), let \(F_t=H\) and

\[
 \omega=4\pi^2\nu(|p|^2+|q|^2),\qquad
 \Phi_t=h_\omega(T-t)H,\qquad
 h_\omega(\tau)=
 \begin{cases}
  (1-e^{-\omega\tau})/\omega,&\omega\ne0,\\
  \tau,&\omega=0.
 \end{cases}
 \tag{5.1}
\]

Direct substitution gives \(\partial_t\Phi+\nu\Delta_{x,y}\Phi=-H\). Moreover
\(0\le h_\omega(\tau)\le\tau\) for every \(\nu\ge0\). There is no singular \(1/\nu\) loss at \(\nu=0\). Here (1.4) has \(c_m=0\) and is the exact heat-contraction estimate. This example also tests constant forcing by taking \(p=q=0\). For the actual campaign forcing \(J_f\), zero interaction instead gives \(J_f=0\), and the unique corrector is zero; the nonzero forcing test concerns the stated general-forcing lemma.

### 5.2 Homogeneous single-mode interaction: an exact eigenfunction of the full operator

Take \(\mu=1\), \(b=0\), and

\[
 g(x)=a\cos(2\pi k\cdot x),\qquad
 K(x)=2\pi a k\sin(2\pi k\cdot x),\qquad k\ne0,
 \tag{5.2}
\]

with any real \(a\). This background solves the mean-field equation for every \(\nu\). Direct integration gives

\[
 R_x\bigl(e_p(x)e_q(y)\bigr)
 =-4\pi^2|p|^2\widehat g(p)e_p(x)e_q(y),
 \quad \widehat g(\pm k)=a/2,
 \tag{5.3}
\]

and the analogous formula for \(R_y\). The negative sign follows from the product
\(\widehat K(-p)\cdot(2\pi i p)=-4\pi^2|p|^2\widehat g(p)\).

Choose the symmetric real mode
\(H(x,y)=\cos(2\pi k\cdot(x+y))\). Its two gradients are equal, hence \(BH=0\) exactly. For the full finite-\(N\) operator,

\[
 (L_2+B/N)H=-\Lambda H,
 \qquad \Lambda=4\pi^2|k|^2(2\nu+a).
 \tag{5.4}
\]

For \(F=H\), the exact solution is \(\Phi_t=h_\Lambda(T-t)H\), with the continuously extended function in (5.1). This holds for every \(N\ge2\), including \(N=2,3\), and also when \(\Lambda=0\) or \(\Lambda<0\). If \(a<0\) and \(\nu=0\), then
\(h_\Lambda(\tau)=(e^{|\Lambda|\tau}-1)/|\Lambda|\). Thus a contraction or a kernel-independent linear-in-time bound would be false for the smooth kernel class in the task. The response is a bounded signed operator, not a Markov contraction. The exponential dependence allowed by (1.4) is necessary in this class.

### 5.3 A full finite-\(N\) test with nonzero internal transport

To test the internal coefficient rather than annihilate it, specialize (5.2) to \(d=1\), \(k=1\), and put
\(H_n(x,y)=\cos(2\pi n(x-y))\). Fourier multiplication gives

\[
 \begin{split}
 (R_x+R_y)H_n&=-4\pi^2a\,\mathbf1_{\{n=1\}}H_n,\qquad n\ge1,\\
 \nu\Delta_{x,y}H_n&=-8\pi^2\nu n^2 H_n,\\
 BH_n&=4\pi^2a n(H_{n+1}-H_{n-1}).
 \end{split}
 \tag{5.5}
\]

In particular, \(\Phi_t=(T-t)H_2\) is an exact solution of the full equation for the explicitly prescribed symmetric source

\[
 F_t=(1+32\pi^2\nu(T-t))H_2
       -\frac{8\pi^2a(T-t)}N(H_3-H_1).
 \tag{5.6}
\]

The interaction coefficients in this source are \(4\pi^2a(T-t)\) for \(N=2\) and \(8\pi^2a(T-t)/3\) for \(N=3\), with the displayed minus sign in front of \(H_3-H_1\). Substituting (5.5) into (1.3) cancels every mode. This tests the sign and factor in \(B/N\) without a numerical PDE solver.

Finally, normalize \(\widetilde H_n=(2\pi n)^{-m}H_n\). Then
\(\|\widetilde H_n\|_{C^m}=1\). The absolute Fourier coefficient of
\(\partial_x^m B\widetilde H_n\) at frequency \((n+1,-n-1)\) is

\[
 2\pi^2|a|\,n\left(\frac{n+1}{n}\right)^m.
 \tag{5.7}
\]

The supremum norm dominates each absolute Fourier coefficient on a mass-one torus. For \(a\ne0\), (5.7) tends to infinity. This is an explicit counterexample to boundedness of \(B:C^m\to C^m\), and division by any fixed \(N\) does not change that conclusion. It does not contradict (1.4), which incorporates \(B/N\) into a transport generator.

The exact-rational program `VERIFICATION_CODE/check_round001_smooth_fourier.py` checks these operator coefficients on finite Fourier polynomials. It includes \(N=2,3,17\), \(\nu=0,1/3,1,7\), and positive, zero, and negative kernel amplitudes. Its computation status is `REPRODUCED`; the elementary analytic calculations above are the proofs, and the code is a self-check rather than an independent certificate.

## 6. What the pair estimate still leaves open at fixed smooth kernel

The coordinator supplied the matched pair identity in the following normalization. Define

\[
 C\Phi(x,y,z)=\operatorname{Sym}_3
       [K(x-z)\cdot\nabla_x\Phi(x,y)],
 \tag{6.1}
\]

where \(\operatorname{Sym}_3\) averages over all six permutations. Also write
\((B\Phi)_\mu(x)=\int B\Phi(x,y)\mu(dy)\). For \(P_N=U_2/2\), the drift after solving the pair equation is

\[
 Q_N(t)=U_3[C\Phi_t]
       +\frac1N\langle(B\Phi_t)_{\mu_t},\rho_t\rangle
       +\frac1{2N}\langle B\Phi_t,\mu_t^{\otimes2}\rangle.
 \tag{6.2}
\]

With the campaign one-body backward test and terminal pair value zero, the exact corrected identity is

\[
 \langle f_T,\rho_T\rangle
 =\langle f_0,\rho_0\rangle+P_N[\Phi_0]
       +\int_0^TQ_N(t)\,dt+M_f(T)+M_\Phi(T).
 \tag{6.3}
\]

The finite-\(N\) algebra in (6.1)--(6.3) is an input from the matched reconstruction lane, not a new independent algebra audit by this worker. The source sign agrees with (1.5).

The first unresolved probabilistic line is an estimate for the cubic term in (6.2), under a named actual evolved particle law, at
\(\sigma_N=\min(\sqrt{N\beta_N},\kappa_N)\). If a second-order truncation is intended to make the cubic remainder disappear, one sufficient target is

\[
 \mathbb E\left|
     \sigma_N\int_0^T U_3[C\Phi_t]\,dt
   \right|\longrightarrow0.
 \tag{6.4}
\]

This target is **open**, is not asserted for arbitrary initial laws, and may be the wrong conclusion at critical scaling if the cubic contribution survives. An alternative must identify its limit or cancel it with a justified higher corrector, rather than relabel it negligible. Any deterministic centering of this term must itself be derived for the selected law; (6.4) does not silently subtract an expectation.

The bound proved here gives only

\[
 \|C\Phi_t\|_\infty\le d\kappa_0\|\Phi_t\|_{C^1},
 \qquad |U_3[C\Phi_t]|\le8\|C\Phi_t\|_\infty.
 \tag{6.5}
\]

The second inequality follows by bounding the total mass of each of the eight terms in the definition of \(U_3\) by one. It has no decay in \(N\), even though the kernel norm is uniformly bounded. Thus smooth PDE control alone supplies no proof of (6.4).

The remaining exact terms must also be treated at the same scale: the initial pair statistic \(\sigma_NP_N[\Phi_0]\), the two lower terms in (6.2), the pair martingale, and its quadratic and cross variations with the one-body martingale. A law-specific fluctuation theorem may retain some of them. Bounded derivatives do not determine their centering, Gaussianity, limiting covariance, or tightness. The two explicit lower drifts have a deterministic bound of order \(\sigma_N/N\) times fixed-kernel norms. For the separate iid preparation row, \(\kappa_N=\sqrt N\) makes this bound vanish at least as \(N^{-1/2}\). That observation is not a bound on the cubic term and is not a transfer to another preparation class.

The PDE itself does not involve the Riesz exponent \(s\). At a fixed smooth kernel its coefficients contain the explicit factor \(1/N\) and the diffusion \(\nu=1/\beta_N\), while the estimate above is even uniform in \(\nu\). Consequently, calling a sequence microscopically subcritical or critical supplies no new small parameter to this proof. The meaning of \(\lambda_N\) must be recovered from singular, law-dependent estimates and hierarchy scaling, not inserted into a fixed-cutoff bound.

## 7. The first nonuniform cutoff step is explicit

Use the positive Fourier coefficient sequence prescribed by the dossier, writing its specified constant as \(c_{d,s}>0\):

\[
 \widehat g_\varepsilon(k)
   =c_{d,s}|k|^{s-d}e^{-4\pi^2\varepsilon|k|^2},
 \quad k\ne0,
 \qquad 0<s<d.
 \tag{7.1}
\]

All statements in this section concern this explicit sequence. Its source normalization is not independently certified by this smooth worker. The logarithmic case is not obtained by setting \(s=0\).

Absolute Fourier summation gives, for \(0<\varepsilon\le1\),

\[
 \kappa_m(\varepsilon)
 \le C(d,s,m)\varepsilon^{-(s+m+1)/2}.
 \tag{7.2}
\]

To see the exponent, a derivative of order \(j\) of \(K=-\nabla g\) is bounded by a constant times
\(\sum_{k\ne0}|k|^{s-d+j+1}e^{-4\pi^2\varepsilon|k|^2}\).
Split the lattice into dyadic annuli, bound the number of points in an annulus of radius \(R\) by a constant times \(R^d\), and rescale \(R\) by \(\varepsilon^{-1/2}\). The resulting convergent annular sum has size at most \(\varepsilon^{-(s+j+1)/2}\). Taking the maximum over \(j\le m\) gives (7.2).

This divergence is not solely an artifact of an upper estimate. At the origin,

\[
 \operatorname{div}K_\varepsilon(0)
 =4\pi^2c_{d,s}\sum_{k\ne0}
       |k|^{s-d+2}e^{-4\pi^2\varepsilon|k|^2}
 \asymp_{d,s}\varepsilon^{-(s+2)/2}.
 \tag{7.3}
\]

The upper estimate follows by the same annular sum. For the lower estimate restrict to lattice points with
\(\varepsilon^{-1/2}\le|k|\le2\varepsilon^{-1/2}\); for sufficiently small \(\varepsilon\) there are at least a fixed positive multiple of \(\varepsilon^{-d/2}\) such points, and all summands there have comparable positive size. In particular,
\(\kappa_1(\varepsilon)\ge d^{-1}\operatorname{div}K_\varepsilon(0)\).

Even the homogeneous background \(\mu=1\), for which \(M_1=0\) and \(u=0\), therefore leaves an unbounded derivative of the principal drift \(K_\varepsilon/N\) at fixed \(N\). There is also an actual forcing divergence in the norm used by the lemma. By sign and coordinate permutation symmetry of (7.1),

\[
 DK_\varepsilon(0)=a_\varepsilon I,
 \qquad a_\varepsilon=\frac1d\operatorname{div}K_\varepsilon(0)>0.
 \tag{7.4}
\]

Take the smooth terminal test \(f_T(x)=\cos(2\pi x_1)\). In local coordinates \(x=q+r/2\), \(y=q-r/2\), at \(q=0\),

\[
 \left.\partial_{r_1}^2
  J_{f_T,\varepsilon}(q+r/2,q-r/2)\right|_{q=r=0}
    =-8\pi^2a_\varepsilon.
 \tag{7.5}
\]

Indeed, to quadratic order the source is
\((DK_\varepsilon(0)r)\cdot(D^2f_T(q)r)\).
Since \(\partial_{r_1}=\tfrac12(\partial_{x_1}-\partial_{y_1})\), its second derivative is controlled by the specified pair \(C^2\) norm. Thus \(\|J_{f_T,\varepsilon}\|_{C^2}\) diverges at least as a positive constant times \(\varepsilon^{-(s+2)/2}\). This example has uniformly bounded background derivatives and a fixed terminal test. It proves that a uniform forcing bound in the norm used in (1.4) is unavailable, already for \(m=2\).

The precise failed passage is therefore: insert \(K_\varepsilon\), \(J_{f,\varepsilon}\) into (1.4), and attempt to bound its right-hand side independently of \(\varepsilon\). Both the coefficient bound used in its exponential and the required supremum-in-time forcing bound diverge. Formula (7.5) also rules out a cutoff-independent estimate
\(\|\Phi_{T-\tau}\|_{C^2}\le C\tau\) for all sufficiently small \(\tau\), with one \(C\) for all cutoffs: for each fixed cutoff, \(\Phi_{T-\tau}/\tau\to J_{f_T,\varepsilon}\) in \(C^2\). This does **not** prove that every weaker norm, every positive-diffusion estimate, or every finite-time singular corrector construction is impossible. It identifies the exact limitation of the present uniform \(C^m\) mechanism.

To continue toward a singular fluctuation result requires new input at the following specific interfaces:

1. A kernel or observable norm compatible with the singular response and source, with a uniform regularized inverse estimate for the exact pair operator or an explicitly proved joint choice \(\varepsilon=\varepsilon(N,\beta_N)\). Bounds on any derivative of the background or one-body test used in that estimate must be uniform as well.
2. A law-specific estimate for the centered cubic and higher statistics in (6.2), sufficient at the declared \(\sigma_N\) scale, together with initial-corrector and martingale/cross-variation control. Control of their expectations alone does not supply this estimate.
3. Justification of all diagonal contractions and any counterterms when passing to the singular limit, including the order of limits. The diagonal vanishing of \(J_f\) does not imply that the pair solution or its differentiated contractions vanish on the diagonal.
4. Quantified growth with corrector order, needed to decide whether critical contributions truncate or form a convergent infinite expansion. This finite-order estimate contains no order-uniform assertion.

No local-equilibrium replacement, concentration theorem, Wick subtraction, or critical resummation is proved here. In particular, choosing a cutoff so that an explicit derivative bound happens to be small is not a proof that the regularized model approximates the singular particle system at the required fluctuation scale.

## 8. Adversarial self-check, disposition, and integration handoff

The following possible failures were checked explicitly:

| Potential failure | Disposition |
|---|---|
| A response derivative falls on the other pair variable and costs one extra derivative of the unknown | Repaired by (2.1); the complementary case is (2.2). |
| The proof hides a derivative of the background beyond the declared bound | Only the explicitly displayed \(M_1(t)\) enters the response estimate. Drift derivatives use the probability mass and derivatives of the fixed kernel. |
| \(B/N\) is treated as a bounded operator on \(C^m\) | Excluded by the explicit sequence (5.7); included in transport in both proofs. |
| The maximum principle requires strict ellipticity or a factor \(1/\nu\) | The proof uses only \(\nu\ge0\); (5.1) tests \(\nu=0\), and the exact code also tests \(\nu>1\). |
| A response sign or factor of two is missing | Direct Fourier multiplier (5.3) and eigenvalue (5.4); normalization of \(J_f\) confirmed against the coordinator's pair identity. |
| A dissipativity assumption is smuggled in for all smooth even kernels | The negative-amplitude case in (5.4) has exponential growth and is allowed by the lemma. |
| Symmetry is assumed rather than preserved | The full drift and response commute with variable exchange; uniqueness gives the conclusion. |
| Fixed smooth regularity is advertised as cutoff uniformity | Explicit failures (7.3) and (7.5) prevent that promotion. |
| Two proof mechanisms are called an independent audit | Status remains `SELF_CHECKED`; isolated review is still required. |

The bounded analytic part of `PO-001a` now has a complete candidate proof. It is ready for an isolated reconstruction or hostile audit on the exact statement (1.1)--(1.4), including the mixed-derivative response bound (2.1)--(2.3). This changes neither the status of `THM-002` nor any singular or critical theorem. The first further probabilistic line is (6.4), or a precisely stated replacement if the cubic term is retained; the first nonuniform analytic cutoff line is (7.5) together with the use of (1.4).

Only the assigned memorandum and its supporting verification program were created. The untracked task dossier and task card were already present. No canonical state ledger, immutable input, branch, commit, or remote was changed. The root coordinator should record the candidate result and explicit constants in the theorem/proof-obligation, operator, assumptions/constants, corrector, regularization, and law/scaling ledgers, and separately record the actual audit level.

### Reproduction and source preflight

- Inspected the applicable repository instructions, mandatory baseline/specification files, source manifest and imported note, all canonical `STATE/` files, and the frozen task/model dossier. No other worker's constructor narrative was read.
- `python3 scripts/verify_campaign.py`: passed before editing; source PDF SHA-256 matched `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`.
- The system `pdftotext` command was unavailable. The supplied PDF was read with the existing bundled `pypdf` runtime instead; no dependency was installed. No claim from that note is a proof input here.
- `python3 VERIFICATION_CODE/check_round001_smooth_fourier.py`: passed all 120 exact rational identities, with no tolerance and no random seed.
- `python3 scripts/verify_campaign.py`: passed again after the two output files were created.
- `git diff --check`: passed for tracked differences; the two new files were also checked directly for trailing whitespace and final newlines. There are no tracked changes.
- `python3 --version`: Python 3.9.6 for the standard-library Fourier check.
- No TeX source was modified or created, so no TeX compilation is part of this worker's output. The final handoff is prose with links; mathematical content is contained in this assigned Markdown memorandum.
