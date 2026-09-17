# Round 001: independent BBGKY and pathwise reconstruction

**Owner:** TASK-002, isolated BBGKY worker.  
**Date:** 2026-09-17 UTC.  
**Baseline:** 475a5399828bc6e2ccbade08c59b8778638df14a.  
**Worktree:** /private/tmp/hocf-round001-bbgky-20260917.  
**Status:** exact identities proved here for the frozen smooth finite-particle model; independent reconstruction completed; no external audit of this report and no singular or fluctuation-limit certification.

## 1. Isolation, assertion, and scope

The only mathematical input read before or during this reconstruction was TASKS/ACTIVE/ROUND_001_MODEL.md, version 1.0. AGENTS.md and TASKS/ACTIVE/TASK-002_BBGKY.md supplied conduct and scope. The imported note, baseline critical assessment, other constructor outputs, and memory files were not read. No canonical state file, immutable input, branch, or commit was changed.

The primary assertion is that the frozen model admits the exact one-body identity (2.3), pair identity (3.4), and brackets (3.7)--(3.10), including every finite-particle correction. Its logical negation is the existence of an allowed smooth model, test, particle number, or configuration violating one of these equalities. An independent marginal calculation and a pathwise calculation below give the same drift. Exact rational Fourier tests provide additional falsification attempts; they are supporting computations, not the proof.

Throughout, \(N\ge2\), \(\nu=\beta_N^{-1}>0\), and the time interval is \([0,T]\). The space is the unit torus with Haar mass one. The kernel \(g\) is real, even, smooth and mean zero, \(K=-\nabla g\), \(b=-\nabla V\), and \(K(0)=0\). The deterministic probability density \(\mu_t\) is the stipulated smooth reference solution. All kernels below are deterministic, spatially smooth and continuously differentiable in time. Constants implicit in existence statements can depend on \(N,\nu,g,\mu,T\); no uniform estimate is claimed.

Write
\[
\eta=N^{-1}\sum_i\delta_{X_i},\qquad \rho=\eta-\mu,\qquad
u=b+K*\mu,\qquad Lf=u\cdot\nabla f+\nu\Delta f.
\]
The particle diffusion is the one in the frozen dossier. Exact pathwise statements require no exchangeability. Exchangeability is assumed only in Section 4 when normalized marginals are introduced. Initial iid, equilibrium, other exchangeable, and deterministic configurations are not identified with one another.

For any \(k\)-slot kernel \(F\), let
\[
D_k[F]=N^{-k}\sum_{i_1,\ldots,i_k\ {\rm distinct}}
 F(X_{i_1},\ldots,X_{i_k}).
\]
Thus \(D_1=\eta\), \(D_k=0\) if \(k>N\), and \(D_0[c]=c\). The \(U_k\) are exactly the inclusion-exclusion statistics in the dossier. In particular
\[
U_1[f]=\rho[f],\qquad
U_2[\Phi]=\rho^{\otimes2}[\Phi]-N^{-1}\eta[\Phi^\Delta],
\qquad \Phi^\Delta(x)=\Phi(x,x),
\tag{1.1}
\]
and \(P[\Phi]=U_2[\Phi]/2\). Particle-label deletion is used even at coincident coordinates.

No external theorem or literature normalization is imported for the algebra. The Riesz Fourier constant and the logarithmic normalization are not used or certified here.

## 2. One-body response and backward duality

Define the complete response operator
\[
(Rf)(y)=\int K(x-y)\cdot\nabla f(x)\,\mu(dx),\qquad A=L+R.
\tag{2.1}
\]
The symmetric interaction test is
\[
B_f(x,y)=\frac12K(x-y)\cdot(\nabla f(x)-\nabla f(y)),
\qquad h_f=2B_f.
\tag{2.2}
\]
The diagonal of \(B_f\) vanishes. For an arbitrary time-dependent test \(f\), smooth Itô calculus and the reference equation give
\[
dU_1[f]
=U_1[(\partial_t+A)f]\,dt+U_2[B_f]\,dt+dM_1[f],
\qquad
dM_1[f]=\frac{\sqrt{2\nu}}N\sum_i\nabla f(X_i)\cdot dW_i.
\tag{2.3}
\]
Equivalently the quadratic drift is \(P[h_f]\), not \(P[B_f]\).

Indeed the particle drift equals \(u(X_i)+(K*\rho)(X_i)\), since \(K(0)=0\). Subtraction of the reference equation first gives
\[
d\rho[f]
=\rho[(\partial_t+L)f]\,dt
+\mu[(K*\rho)\cdot\nabla f]\,dt
+\rho[(K*\rho)\cdot\nabla f]\,dt+dM_1[f].
\]
The second term is \(\rho[Rf]\). Symmetrizing the last term gives \(\rho^{\otimes2}[B_f]\), which equals \(U_2[B_f]\) by its vanishing diagonal. This proves (2.3) on every configuration.

If \(f_t\) solves the backward equation
\[
(\partial_t+A_t)f_t=0,\qquad f_T=f_{\rm term},
\]
then
\[
\rho_T[f_{\rm term}]
=\rho_0[f_0]+\int_0^T U_2[B_{f_t}]\,dt+M_1[f]_T.
\tag{2.4}
\]
The same formula holds on any subinterval. Its expectation version is independently reconstructed in Section 4. The martingale cannot be reconstructed from the one-time marginal hierarchy alone.

The smooth backward equation has a classical solution at this fixed model. One direct construction uses the backward propagator \(P_{t,s}\) of the auxiliary diffusion with drift \(u\) and diffusivity \(\nu\). Spatial derivatives of its stochastic flow satisfy linear differential equations with bounded smooth coefficients. Consequently \(P_{t,s}\) is bounded on each fixed \(C^m\) space over this finite horizon. Integration by parts gives
\[
Rf(y)=-\int f(x)\operatorname{div}_x(\mu(x)K(x-y))\,dx,
\]
so \(R_t:C^m\to C^m\) is bounded. Picard iteration of
\[
f_t=P_{t,T}f_{\rm term}+\int_t^T P_{t,s}R_s f_s\,ds
\]
converges in each \(C^m\): its \(n\)-th iterated integral has the factorial bound \(C^n(T-t)^n/n!\), with the finite propagator bound absorbed in \(C\). The equation then gives time differentiability. This construction gives no cutoff- or temperature-uniform bound.

For two one-body tests, including backward tests,
\[
d[M_1[f],M_1[q]]_t
=\frac{2\nu}{N}\eta[\nabla f\cdot\nabla q]\,dt.
\tag{2.5}
\]

## 3. Exact pair identity and every lower contraction

For a symmetric pair kernel \(\Phi\), define
\[
\begin{aligned}
(R_x\Phi)(x,y)&=\int K(z-x)\cdot\nabla_z\Phi(z,y)\,\mu(dz),\\
(R_y\Phi)(x,y)&=\int K(z-y)\cdot\nabla_z\Phi(x,z)\,\mu(dz),\\
A_2\Phi&=(L_x+L_y+R_x+R_y)\Phi,\\
J\Phi(x,y)&=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi(x,y).
\end{aligned}
\tag{3.1}
\]
In the second line \(\nabla_z\) differentiates the second slot of \(\Phi(x,z)\). The kernel \(J\Phi\) is symmetric and vanishes on the diagonal.

For three slots put
\[
C_{\rm raw}\Phi(x,y,z)
=K(x-z)\cdot\nabla_x\Phi(x,y)
 +K(y-z)\cdot\nabla_y\Phi(x,y).
\]
This is symmetric in its first two slots. A fully symmetric version is
\[
C\Phi(x,y,z)=\frac13\bigl(
C_{\rm raw}\Phi(x,y,z)+C_{\rm raw}\Phi(x,z,y)
+C_{\rm raw}\Phi(y,z,x)\bigr).
\tag{3.2}
\]
Both give the same evaluation under \(U_3\), \(D_3\), or any symmetric triple measure. The factor \(1/3\) is essential: each raw term already contains two derivatives.

For the lower contractions define
\[
j_\Phi(x)=\int J\Phi(x,y)\,\mu(dy),\qquad
c_\Phi=\iint J\Phi(x,y)\,\mu(dx)\mu(dy).
\tag{3.3}
\]
Then the exact random semimartingale identity is
\[
\boxed{\;
dU_2[\Phi]
=\left\{
U_2[(\partial_t+A_2)\Phi]+U_3[C\Phi]
+\frac1N D_2[J\Phi]\right\}dt+dM_2[\Phi].
\;}
\tag{3.4}
\]
Equivalently, with all lower orders visible,
\[
\begin{aligned}
dU_2[\Phi]
={}&\left\{
U_2[(\partial_t+A_2)\Phi]
+U_3[C\Phi]+\frac1N U_2[J\Phi]
+\frac2N U_1[j_\Phi]+\frac1N c_\Phi
\right\}dt+dM_2[\Phi].
\tag{3.5}
\end{aligned}
\]
There is no additional diffusion forcing in (3.4)--(3.5). Such a forcing is present in the full-product convention and cancels upon deleting the empirical diagonal; Section 5 displays that cancellation.

In the \(P=U_2/2\) convention the corresponding formula is
\[
\boxed{\;
dP[\Phi]
=\left\{
P[(\partial_t+A_2)\Phi]
+\frac12U_3[C\Phi]+\frac1N P[J\Phi]
+\frac1N U_1[j_\Phi]+\frac1{2N}c_\Phi
\right\}dt+dM_P[\Phi].
\;}
\tag{3.6}
\]
In particular neither the cubic term nor the constant contraction has the same coefficient in the \(U_2\) and \(P\) conventions.

Define the random vector field
\[
v_\Phi(x)=\int\nabla_x\Phi(x,y)\,\rho(dy)
-\frac1N\nabla_x\Phi(x,x).
\]
The diagonal derivative in the last term is a derivative of the first slot before restriction to the diagonal. At a particle,
\[
v_\Phi(X_i)=\frac1N\sum_{j\ne i}\nabla_x\Phi(X_i,X_j)
-\int\nabla_x\Phi(X_i,y)\,\mu(dy).
\]
The exact martingales are
\[
dM_2[\Phi]=\frac{2\sqrt{2\nu}}N\sum_i v_\Phi(X_i)\cdot dW_i,
\qquad
dM_P[\Phi]=\frac{\sqrt{2\nu}}N\sum_i v_\Phi(X_i)\cdot dW_i.
\tag{3.7}
\]
For symmetric kernels \(\Phi,\Psi\) and a one-body test \(f\),
\[
\begin{aligned}
d[M_P[\Phi],M_P[\Psi]]
 &=\frac{2\nu}{N}\eta[v_\Phi\cdot v_\Psi]\,dt,\\
d[M_2[\Phi],M_2[\Psi]]
 &=\frac{8\nu}{N}\eta[v_\Phi\cdot v_\Psi]\,dt,\\
d[M_1[f],M_P[\Phi]]
 &=\frac{2\nu}{N}\eta[\nabla f\cdot v_\Phi]\,dt,\\
d[M_1[f],M_2[\Phi]]
 &=\frac{4\nu}{N}\eta[\nabla f\cdot v_\Phi]\,dt.
\end{aligned}
\tag{3.8}
\]
Time-dependent deterministic kernels introduce no further bracket term.

Here are also the explicit label contractions inside the pair bracket. Write
\[
p(x,y)=\nabla_x\Phi(x,y),\quad q(x,y)=\nabla_x\Psi(x,y),
\quad \bar p(x)=\int p(x,y)\mu(dy),\quad
\bar q(x)=\int q(x,y)\mu(dy).
\]
Expanding the two sums at each particle gives exactly
\[
\begin{aligned}
\eta[v_\Phi\cdot v_\Psi]
={}&D_3[p(x,y)\cdot q(x,z)]
+\frac1N D_2[p(x,y)\cdot q(x,y)]\\
&-D_2[p(x,y)\cdot\bar q(x)]
-D_2[q(x,y)\cdot\bar p(x)]
+\eta[\bar p\cdot\bar q].
\end{aligned}
\tag{3.9}
\]
The second term is the contraction \(j=k\ne i\). The cases \(i=j\) and \(i=k\) are excluded in the definition of \(v\); there is no missing fully diagonal term. For the cross bracket,
\[
\eta[\nabla f\cdot v_\Phi]
=D_2[\nabla f(x)\cdot p(x,y)]-\eta[\nabla f\cdot\bar p].
\tag{3.10}
\]
The general inclusion-exclusion definition converts every \(D_k\) here to \(U_k\) if desired. Formulas (3.9)--(3.10) already expose the actual particle-label contractions without suppressing them in a schematic covariance symbol.

## 4. Independent derivation from the marginal hierarchy

Assume exchangeability in this section. Let \(p_k\) denote the probability \(k\)-particle marginal for \(k\le N\), and define the factorial moment measures
\[
a_k=\mathbb E D_k=\frac{(N)_k}{N^k}p_k,\qquad a_0=1.
\]
Set \(a_k=0\) when \(k>N\); this does not introduce a nonexistent \(p_k\). Let \(L_0=b\cdot\nabla+\nu\Delta\). Integration of the joint particle equation gives, in weak form,
\[
\begin{aligned}
\frac d{dt}p_1[f]
 &=p_1[(\partial_t+L_0)f]
 +\frac{N-1}{N}p_2[K(x-y)\cdot\nabla f(x)],\\
\frac d{dt}p_2[\Phi]
 &=p_2[(\partial_t+L_{0,x}+L_{0,y})\Phi]
 +\frac1N p_2[J\Phi]
 +\frac{N-2}{N}p_3[C_{\rm raw}\Phi].
\end{aligned}
\tag{4.1}
\]
At \(N=2\) the last expression means zero without defining \(p_3\). The coefficients count, respectively, the other labels, the mutual pair interaction, and the labels outside the tested pair. The backward and forward divergence signs are consistent: each force contributes minus divergence in the density equation and plus force times gradient in (4.1).

Multiplication by the factorial normalizations makes the last coefficients transparent:
\[
\begin{aligned}
\frac d{dt}a_1[f]
 &=a_1[(\partial_t+L_0)f]
 +a_2[K(x-y)\cdot\nabla f(x)],\\
\frac d{dt}a_2[\Phi]
 &=a_2[(\partial_t+L_{0,x}+L_{0,y})\Phi]
 +\frac1N a_2[J\Phi]+a_3[C_{\rm raw}\Phi].
\end{aligned}
\tag{4.2}
\]

Define \(\gamma_k=\mathbb E U_k\), so
\[
\begin{aligned}
\gamma_1&=a_1-\mu,\\
\gamma_2&=a_2-a_1\otimes\mu-\mu\otimes a_1+\mu^{\otimes2},\\
\gamma_3&=a_3-\sum_{\rm slots}a_2\otimes\mu
 +\sum_{\rm slots}a_1\otimes\mu^{\otimes2}-\mu^{\otimes3}.
\end{aligned}
\tag{4.3}
\]
The sums place the arguments in their indicated slots and have three terms each.

For the first line of (4.2), put \(H_f(x,y)=K(x-y)\cdot\nabla f(x)\). Then
\[
\gamma_2[B_f]
=a_2[H_f]-a_1[(K*\mu)\cdot\nabla f]-a_1[Rf]
+\mu[(K*\mu)\cdot\nabla f].
\]
Also \(\mu[Rf]=\mu[(K*\mu)\cdot\nabla f]\). Subtracting the reference equation therefore gives
\[
\frac d{dt}\gamma_1[f]
=\gamma_1[(\partial_t+A)f]+\gamma_2[B_f].
\tag{4.4}
\]
Testing against the backward solution independently recovers the expectation of (2.4).

For completeness, the pair cancellation can be checked without using the pathwise proof. Suppress the explicit test-time derivative, which is linear. Put
\[
a(x)=\int\Phi(x,y)\mu(dy),\quad
H(x,y)=K(x-y)\cdot\nabla a(x),\quad
q(x)=\int (L_y\Phi)(x,y)\mu(dy).
\]
Differentiating the second line of (4.3), using (4.2) and the reference equation, gives
\[
\begin{aligned}
\frac d{dt}\gamma_2[\Phi]
={}&a_2[(L_{0,x}+L_{0,y})\Phi]+a_3[C_{\rm raw}\Phi]
+\frac1N a_2[J\Phi]\\
&-2a_2[H]-2a_1[L_0a+q]+2\mu[La].
\end{aligned}
\tag{4.5}
\]
Here the term \(-2a_2[H]\) comes from the interaction in the first marginal; omitting it would lose part of the full response.

To verify the equivalent centered expression explicitly, let \(v=K*\mu\),
\[
T\Phi=v(x)\cdot\nabla_x\Phi+v(y)\cdot\nabla_y\Phi,\qquad
c(x)=\int v(y)\cdot\nabla_y\Phi(x,y)\mu(dy).
\]
The three possible single-\(\mu\) contractions of \(C_{\rm raw}\Phi\), when paired with symmetric \(a_2\), sum to
\[
a_2[T\Phi+(R_x+R_y)\Phi+2H].
\]
The three possible double-\(\mu\) contractions, when paired with \(a_1\), sum to
\[
2a_1[v\cdot\nabla a+c+Ra].
\]
Finally \(\mu^{\otimes3}[C_{\rm raw}\Phi]=2\mu[v\cdot\nabla a]\), and
\[
\int (A_2\Phi)(x,y)\mu(dy)
=L_0a+v\cdot\nabla a+q+c+Ra.
\]
Substitution in (4.3) gives the exact polynomial identity
\[
\begin{aligned}
\gamma_2[A_2\Phi]+\gamma_3[C\Phi]
={}&a_2[(L_{0,x}+L_{0,y})\Phi]+a_3[C_{\rm raw}\Phi]\\
&-2a_2[H]-2a_1[L_0a+q]+2\mu[La].
\end{aligned}
\]
Comparison with (4.5) proves
\[
\frac d{dt}\gamma_2[\Phi]
=\gamma_2[(\partial_t+A_2)\Phi]+\gamma_3[C\Phi]
+\frac1N a_2[J\Phi].
\tag{4.6}
\]
This is exactly the expectation of (3.4). Since
\[
a_2[J\Phi]=\gamma_2[J\Phi]+2\gamma_1[j_\Phi]+c_\Phi,
\]
it also verifies every coefficient in (3.5).

These are factorial centered moments, not ordinary connected cumulants. If \(m=p_1\), \(\delta=m-\mu\), and \(c_2^{\rm conn}=p_2-m^{\otimes2}\), then
\[
\gamma_2=(1-N^{-1})c_2^{\rm conn}
+\delta^{\otimes2}-N^{-1}m^{\otimes2}.
\tag{4.7}
\]
For iid initial law \(\mu_0^{\otimes N}\),
\[
\gamma_1=0,\qquad
\gamma_2=-N^{-1}\mu_0^{\otimes2},\qquad
\gamma_3=2N^{-2}\mu_0^{\otimes3}.
\tag{4.8}
\]
In particular deleted-diagonal centering is not the same as zero expectation under iid sampling.

Changing the deterministic reference from \(\mu\) to the exact first marginal \(m\) changes the statistic as
\[
U_2^\mu[\Phi]
=U_2^m[\Phi]+2(\eta-m)\otimes(m-\mu)[\Phi]
+(m-\mu)^{\otimes2}[\Phi].
\tag{4.9}
\]
One may not use the same backward response after that change without recomputing the equation for \(m\).

The marginal calculation proves only deterministic expectation identities. It does not prove smallness of a random residual, concentration, tightness, or the martingale/bracket formulas.

## 5. Pathwise pair proof and cancellation of the diagonal trace

This second proof starts from the particle semimartingales rather than the marginal hierarchy. Set
\[
h(x)=\Phi(x,x),\qquad
\tau(x)=\sum_{\alpha=1}^d
\partial_{x_\alpha}\partial_{y_\alpha}\Phi(x,y)\big|_{y=x}.
\]
The full-product statistic satisfies
\[
\begin{aligned}
d\,\rho^{\otimes2}[\Phi]
={}&\left\{
\rho^{\otimes2}[(\partial_t+A_2)\Phi]
+\rho^{\otimes3}[C_{\rm raw}\Phi]
+\frac{2\nu}{N}\eta[\tau]
\right\}dt+dM_{\rm full}.
\end{aligned}
\tag{5.1}
\]
This follows either by applying the particle generator to its finite sums or by applying the product rule to the weak equation (2.3). The mixed second derivative is the Itô contraction from the same Brownian motion appearing in both slots.

The exact three-slot combinatorial identity is
\[
U_3[F]
=\rho^{\otimes3}[F]
-\frac1N\sum_{\{a,b\}\subset\{1,2,3\}}
(\Delta_{ab}\eta\otimes\rho)[F]
+\frac2{N^2}(\Delta_{123}\eta)[F].
\tag{5.2}
\]
Here \(\Delta_{ab}\) means that slots \(a,b\) receive the same empirical coordinate; the other slot receives \(\rho\). This identity follows by grouping the all-distinct, exactly-two-equal, and all-equal label patterns in \(\eta^{\otimes3}\), followed by the inclusion-exclusion definition of \(U_3\). It remains valid at \(N=2\).

For \(F=C_{\rm raw}\Phi\), the fully diagonal value is zero. The sum of its three partial diagonal evaluations in (5.2) is
\[
\int\eta(dx)\rho(dy)\left[
K(x-y)\cdot\nabla h(x)
+2K(y-x)\cdot\nabla_y\Phi(x,y)\right].
\tag{5.3}
\]
The factor 2 is the sum of the diagonals \(x=z\) and \(y=z\), after relabeling and symmetry of \(\Phi\). The remaining diagonal \(x=y\) gives \(\nabla h\).

For the deleted term in (1.1), the particle equation gives
\[
d\eta[h]
=\left\{\eta[(\partial_t+L)h]
+\int\eta(dx)\rho(dy)K(x-y)\cdot\nabla h(x)\right\}dt+dM_\eta[h].
\tag{5.4}
\]
The first partial diagonal term in (5.3) therefore cancels after subtracting \(N^{-1}d\eta[h]\).

The local part of the diagonal operator satisfies
\[
\big((\partial_t+L_x+L_y)\Phi\big)^\Delta
-(\partial_t+L)h=-2\nu\tau.
\tag{5.5}
\]
This follows from the chain rule
\(\Delta h=(\Delta_x+\Delta_y)\Phi|_\Delta+2\tau\).
Consequently (5.5) cancels the Itô trace in (5.1) exactly.

Finally set
\[
a_\Phi(x)=\int K(y-x)\cdot\nabla_y\Phi(x,y)\mu(dy).
\]
Then
\[
((R_x+R_y)\Phi)^\Delta=2a_\Phi.
\]
The response-diagonal contribution and the remaining two contractions in (5.3) combine into
\[
\begin{aligned}
&\frac2N\eta[a_\Phi]
+\frac2N\int\eta(dx)\rho(dy)
 K(y-x)\cdot\nabla_y\Phi(x,y)\\
&\hspace{12mm}=\frac2N\int\eta(dx)\eta(dy)
 K(y-x)\cdot\nabla_y\Phi(x,y)
=\frac1N D_2[J\Phi].
\end{aligned}
\tag{5.6}
\]
The last equality uses symmetrization and \(K(0)=0\). This proves the drift (3.4).

Direct differentiation of the finite-particle function \(U_2[\Phi]\) gives
\[
\nabla_{X_i}U_2[\Phi]=\frac2N v_\Phi(X_i).
\]
The noise coefficients and every bracket in (3.7)--(3.10) follow by independence and unit covariance of the Brownian motions. This proves the random identity separately from its expectation hierarchy.

## 6. Falsification and normalization checks

### 6.1 Constant kernels

For \(\Phi\equiv c\), \(U_2[\Phi]=-c/N\), not zero. For a constant triple kernel, \(U_3[c]=2c/N^2\). All spatial operator, interaction, and noise terms vanish. A time-dependent spatial constant produces only \(-c'(t)/N\) on both sides of (3.4). This detects accidental replacement of \(N^k\) by \((N)_k\).

### 6.2 Two and three particles

For \(N=2\), \(D_2[\Phi]=\Phi(X_1,X_2)/2\) and \(D_3=0\). The mutual force contributes \(J\Phi(X_1,X_2)/4\) to the drift of \(D_2[\Phi]\). This equals \(N^{-1}D_2[J\Phi]\), as required. Nevertheless \(U_3[C\Phi]\) is generally nonzero because it includes mixed empirical/reference terms. Dropping it because there are only two particles would be an error.

For \(N=3\),
\[
D_2[\Phi]=\frac2{9}\sum_{i<j}\Phi(X_i,X_j),\qquad
D_3[F]=\frac1{27}\sum_{i,j,k\ {\rm distinct}}F(X_i,X_j,X_k).
\]
The mutual pair force has coefficient \(2/27\) in front of each unordered \(J\Phi(X_i,X_j)\); the outside-label terms have coefficient \(1/27\) in the ordered triple sum. The corresponding probability-marginal factors are \(2/3\), \(1/3\), and \(1/3\) in the first-marginal outside force, pair mutual force, and pair outside force. All agree with (4.1)--(4.2).

### 6.3 No interaction and separable tests

If \(K=0\), then \(R,J,C,B\) vanish. Equation (3.4) becomes
\[
dU_2[\Phi]=U_2[(\partial_t+L_x+L_y)\Phi]\,dt+dM_2[\Phi].
\]
For \(\Phi(x,y)=f(x)f(y)\),
\[
U_2[\Phi]=\rho[f]^2-\frac1N\eta[f^2].
\]
When \(K=0\) and \((\partial_t+L)f=0\), the quadratic variation of \(\rho[f]\) contributes \(2\nu N^{-1}\eta[|\nabla f|^2]\), while \(N^{-1}d\eta[f^2]\) contributes exactly the same drift. Thus the claimed absence of an extra diffusion forcing is directly verified by the scalar Itô product rule.

For a general symmetric separable kernel
\(\Phi=(f\otimes q+q\otimes f)/2\), polarization gives the corresponding identity and the cross bracket. The martingale coefficient becomes
\[
v_\Phi(x)=\frac12\left(
\nabla f(x)\rho[q]+\nabla q(x)\rho[f]
-\frac{\nabla f(x)q(x)+\nabla q(x)f(x)}N\right),
\]
consistent with differentiating the displayed full-product-minus-diagonal statistic.

### 6.4 Fourier sign and finite-particle forcing

Take \(\mu\equiv1\), \(b=0\), and \(e_k(x)=\exp(2\pi i k\cdot x)\). Direct integration, with \(\widehat K(\ell)=-2\pi i\ell\,\widehat g(\ell)\), gives
\[
Ae_k=-4\pi^2|k|^2(\nu+\widehat g(k))e_k.
\tag{6.1}
\]
In particular the response has a minus sign. Pair products diagonalize \(A_2\), with the sum of the two one-body eigenvalues; there is no missing cross-response multiplier. Complex tests are shorthand for the separate real and imaginary tests.

For \(k\ne0\) and the symmetric real kernel
\(\Phi=(e_k\otimes e_{-k}+e_{-k}\otimes e_k)/2\),
\[
c_\Phi=-8\pi^2|k|^2\widehat g(k).
\]
At iid uniform initial data, \(\gamma_2[\Phi]=0\),
\(\gamma_2[A_2\Phi]=0\), and \(\gamma_3[C\Phi]=0\), whereas
\[
\left.\frac d{dt}\mathbb E U_2[\Phi]\right|_{t=0}
=-8\pi^2|k|^2\widehat g(k)\frac{N-1}{N^2}.
\tag{6.2}
\]
The same number follows directly from the pair-marginal mutual force. Retaining only the constant contraction \(c_\Phi/N\) would give the incorrect coefficient; the additional \(U_2[J\Phi]/N\) contributes its necessary correction.

### 6.5 Exact rational Fourier computation

The independently written script VERIFICATION_CODE/round001_bbgky_exact_fourier.py uses only the Python standard library and rational Laurent-polynomial coefficients. It compares the particle generator applied directly to the finite sum defining \(U_2\), including the derivative of the reference measure, with the complete right side of (3.4). It also checks one-body identities, the lower-order expansion, each particle's pair-martingale coefficient, and pair cross brackets.

The script covers \(N=2,3\), constant, separable, difference-mode and mixed-mode kernels, with both uniform and strictly positive inhomogeneous reference density. In angular variables \(\theta=2\pi x\), it takes interaction \(\sin\theta\), angular diffusivity \(2/5\), and, in the inhomogeneous case, drift \(\sin(2\theta)/3\) and reference density \(1+\cos\theta/3\) at the tested time. This corresponds exactly to the dossier's unit-torus convention with
\[
g(x)=\frac{\cos(2\pi x)}{4\pi^2},\quad
V(x)=\frac{\cos(4\pi x)}{24\pi^2},\quad
\nu=\frac{2/5}{4\pi^2}.
\]
The reference time derivative is evaluated from the full reference PDE, so the inhomogeneous test does not falsely treat this density as stationary.

Verification command: python3 VERIFICATION_CODE/round001_bbgky_exact_fourier.py.

Observed result: PASS, 24 exact rational Fourier cases; all tested pair lower contractions, martingale coefficients, and pair cross brackets also agree. No random seed or numerical tolerance is used. These finite tests support, but do not replace, Sections 4--5.

## 7. Exact corrector reduction and the first open analytic line

At a fixed smooth model the pair backward equation is also solvable by the propagator/Picard construction of Section 2, applied to two independent auxiliary diffusions and the bounded operators \(R_x+R_y\). Given the one-body backward solution \(f\), let
\[
(\partial_t+A_2)\Phi=-h_f,\qquad \Phi_T=0.
\tag{7.1}
\]
The exact identity is
\[
d\bigl(\rho[f]+P[\Phi]\bigr)
=\left\{\frac12U_3[C\Phi]+\frac1{2N}D_2[J\Phi]\right\}dt
+dM_1[f]+dM_P[\Phi].
\tag{7.2}
\]
Thus the full two-slot response cancels the intended quadratic drift exactly. Equation (7.2) is a finite-particle reduction, not a closure theorem.

The first unproved analytic step for a fluctuation result is control, in a declared initial-law class and uniformly in the required particle, temperature and regularization parameters, of the right-hand side after multiplication by the retained scale
\(\sigma_N=\min(\sqrt{N\beta_N},\kappa_N)\).
Concretely, one must prove a suitable probability or \(L^1\) bound for
\[
\sigma_N\int_0^T
\left\{\frac12U_3[C\Phi_t]+\frac1{2N}D_2[J\Phi_t]\right\}dt,
\tag{7.3}
\]
and control the endpoint corrector and the pair/cross martingale brackets. An expectation bound for (7.3) alone would not suffice. Neither arbitrary exchangeability nor the algebra gives the required cancellation. No power of the singular microscopic coupling follows from a fixed smooth cutoff.

For a singular application, (7.1)'s kernel estimates, (7.3), and the relevant bracket and endpoint bounds must remain valid as the cutoff is removed. That uniform passage is open here. There is no claimed subcritical-range improvement, critical truncation, Gaussian limit, or non-Gaussian law in this report.

The principal independent audit targets are now explicit: the sign and two-slot placement of \(R\), the \(1/3\) symmetrization in \(C\), the \(N^{-1}D_2[J\Phi]\) correction and its three lower orders, and the empirical diagonal in \(v_\Phi\). The exact reconstruction is complete within the stated smooth scope; the campaign's analytic theorem remains open.
