# Round 001: smooth finite-particle duality and pair identity

Date: 2026-09-17 UTC. Task: TASK-001. Baseline commit:
`475a5399828bc6e2ccbade08c59b8778638df14a`.
Worktree: `/private/tmp/hocf-round001-algebra-20260917`.

Mathematical status: `EXACT_IDENTITY` for the smooth finite-particle statements
proved below. Audit status: `SELF_CHECKED`; independent comparison and hostile
review are the coordinator's pending gates. This is the pair part of THM-001,
not an all-order theorem or a fluctuation-limit theorem. No canonical ledger,
immutable input, or baseline file was edited by this worker. No commit was made.

## 1. Assertion, assumptions, and normalization

The assertion is that the frozen Round 001 model admits the exact one-body
identity (2.3), the exact pair identities (3.6)--(3.7), and the martingale
brackets (5.1)--(5.4), for every integer \(N\geq2\), every
\(\beta_N\in(0,\infty)\), every admissible smooth test, and every particle
configuration, including coincident particle coordinates. Its negation is a
permitted instance violating at least one of these equalities. The proof below
is by finite sums and smooth Itô calculus; the numerical checks do not substitute
for it.

All measures are on \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), of Haar mass one.
Set \(\nu=\beta_N^{-1}\). The deterministic functions \(g,V\) are smooth and
periodic; \(g\) is real, even, and of zero mean. Write

\[
K=-\nabla g,\qquad b=-\nabla V,\qquad
u_t=b+K*\mu_t,\qquad L_t^0 f=u_t\cdot\nabla f+\nu\Delta f.
\tag{1.1}
\]

In particular \(K\) is odd and \(K(0)=0\). The deterministic probability density
\(\mu\) is smooth in space and sufficiently differentiable in time on the fixed
horizon \([0,T]\), and solves \(\partial_t\mu=(L_t^0)^*\mu\). The dossier assumes
strict positivity; the algebra itself uses only smoothness and probability mass.
The SDE is

\[
dx_i=\left(b(x_i)+\frac1N\sum_{j\ne i}K(x_i-x_j)\right)dt
       +\sqrt{2\nu}\,dW_i,
\qquad
\eta=\frac1N\sum_{i=1}^N\delta_{x_i},\quad \rho=\eta-\mu.
\tag{1.2}
\]

The Brownian motions are independent, and \(x_i\) are adapted solutions on the
usual filtered probability space. The initial law may be arbitrary; no
exchangeability or preparation assumption enters the identities. Smooth
bounded coefficients give the global SDE by Picard iteration; for fixed
Brownian paths the drift is globally Lipschitz on the compact configuration
space. All the martingales below are square integrable because their integrands
are bounded on the finite horizon.

Tests are deterministic, \(C^1\) in time and smooth in all spatial variables.
For a symmetric pair kernel \(\Phi\), put

\[
\begin{split}
D_2[\Phi]&=\frac1{N^2}\sum_{i\ne j}\Phi(x_i,x_j),\\
U_2[\Phi]&=D_2[\Phi]-2\langle\eta\otimes\mu,\Phi\rangle
                         +\langle\mu^{\otimes2},\Phi\rangle,\\
P[\Phi]&=\frac12U_2[\Phi].
\end{split}
\tag{1.3}
\]

Every tuple is ordered. Distinctness means distinct particle labels, not
distinct coordinates; every denominator is \(N^k\), not \((N)_k\). For a
symmetric triple kernel \(F\), the dossier's definition is

\[
\begin{split}
U_3[F]={}&\frac1{N^3}\sum_{i,j,k\ {\mathrm{distinct}}}F(x_i,x_j,x_k)
-\frac3{N^2}\sum_{i\ne j}\int F(x_i,x_j,z)\,d\mu(z)\\
&+\frac3N\sum_i\iint F(x_i,y,z)\,d\mu(y)d\mu(z)
-\int F\,d\mu^{\otimes3}.
\end{split}
\tag{1.4}
\]

Also \(U_1[h]=\langle\rho,h\rangle\) and \(U_0[c]=c\). No asymptotic assumption
on \(N,\beta_N\), or a reference exponent \(s\) is made.

The only source inputs used in the proof are the frozen model definitions,
finite sums, integration by parts on the torus, and smooth Itô calculus. The
source note `INPUTS/note_v2.pdf` was read after deriving the formulas. Its
Facts 1.2 and 1.4 agree with the raw smooth identities below, but their labels
are not proof inputs. Its claims about singular kernels, stress, weighted
positivity, or limit laws are not imported. The source hash was checked by
`python3 scripts/verify_campaign.py`, which passed.

## 2. Exact one-body identity and backward duality

Define the response operator and the full linearized test operator by

\[
A_tf(y)=\int K(x-y)\cdot\nabla f(x)\,d\mu_t(x),
\qquad L_tf=L_t^0f+A_tf.
\tag{2.1}
\]

For a scalar test \(f\), the symmetric commutator kernel is

\[
H_f(x,y)=K(x-y)\cdot(\nabla f(x)-\nabla f(y)),
\qquad H_f(x,x)=0.
\tag{2.2}
\]

Then

\[
d\langle\rho_t,f_t\rangle
=\big\{\langle\rho_t,(\partial_t+L_t)f_t\rangle
          +P_t[H_{f_t}]\big\}\,dt+dM_t^1[f],
\qquad
dM_t^1[f]=\frac{\sqrt{2\nu}}N\sum_i\nabla f_t(x_i)\cdot dW_i.
\tag{2.3}
\]

**Proof from explicit sums.** Since \(K(0)=0\), the particle drift is exactly
\(u(x_i)+(K*\rho)(x_i)\). Applying Itô to \(N^{-1}\sum_i f_t(x_i)\), subtracting
the weak mean-field equation, and keeping the force term gives

\[
d\langle\rho,f\rangle
=\left\{\langle\rho,(\partial_t+L^0)f\rangle
 +\frac1N\sum_i\nabla f(x_i)\cdot(K*\rho)(x_i)\right\}dt+dM^1[f].
\tag{2.4}
\]

Replacing the first empirical slot in the second term by \(\mu+\rho\) gives

\[
\frac1N\sum_i\nabla f(x_i)\cdot(K*\rho)(x_i)
=\langle\rho,Af\rangle
 +\iint K(x-y)\cdot\nabla f(x)\,d\rho(x)d\rho(y).
\tag{2.5}
\]

Interchanging \(x,y\) and using oddness of \(K\), the last term is
\(\tfrac12\langle\rho^{\otimes2},H_f\rangle\). Its empirical diagonal is zero,
so it is exactly \(P[H_f]\), including at coincident coordinates. This proves
(2.3).

**A second calculation of the same coefficient.** The particle interaction
term before introducing \(u\) is

\[
\frac1{N^2}\sum_{i\ne j}K(x_i-x_j)\cdot\nabla f(x_i)
=\frac12D_2[H_f].
\tag{2.6}
\]

The corresponding mean-field interaction is
\(\tfrac12\langle\mu^{\otimes2},H_f\rangle\). Their difference equals

\[
P[H_f]+\langle\rho\otimes\mu,H_f\rangle.
\tag{2.7}
\]

But integrating \(H_f(x,y)\) against \(\mu(y)\) gives
\((K*\mu)(x)\cdot\nabla f(x)+Af(x)\). Adding the \(b\)-drift and the
diffusion gives the same \(L\) and the same coefficient in (2.3). These are two
calculations in the constructor's context; they are not an isolated audit.

For a smooth solution of

\[
(\partial_r+L_r)f_r=0,\qquad f_t=\phi,
\tag{2.8}
\]

integration yields the exact backward duality

\[
\langle\rho_t,\phi\rangle
=\langle\rho_0,f_0\rangle+M_t^1[f]
  +\int_0^tP_r[H_{f_r}]\,dr.
\tag{2.9}
\]

No fluctuation normalization has been inserted. One may multiply the entire
identity by the dossier's \(\sigma_N\), but no estimate follows from doing so.
Fixed-smooth-kernel solvability of (2.8) is addressed in Section 7.

## 3. The full pair operator and the result

Write \(L_x^0+L_y^0\) for independent transport-diffusion in the two slots. The
two response terms are

\[
\begin{split}
(R_1\Phi)(x,y)&=\int K(z-x)\cdot\nabla_1\Phi(z,y)\,d\mu(z),\\
(R_2\Phi)(x,y)&=\int K(z-y)\cdot\nabla_2\Phi(x,z)\,d\mu(z).
\end{split}
\tag{3.1}
\]

Thus \(R_1,R_2\) apply the response part of \(L\) in the respective slot, with
the derivative taken in the integrated variable. Define

\[
\mathcal L_2\Phi=(L_x^0+L_y^0)\Phi+R_1\Phi+R_2\Phi,
\qquad
B\Phi(x,y)=K(x-y)\cdot(\nabla_1-\nabla_2)\Phi(x,y).
\tag{3.2}
\]

Both kernels are symmetric when \(\Phi\) is symmetric, and \(B\Phi(x,x)=0\).
The finite-particle quadratic operator can either keep the interaction term
separate, or incorporate it as

\[
\mathcal G_{2,N}=\mathcal L_2+\frac1N B.
\tag{3.3}
\]

Its local drift in the first slot is \(u(x)+N^{-1}K(x-y)\), and in the second
slot it is \(u(y)+N^{-1}K(y-x)\); both response terms remain present.

For any three-variable kernel, \(\operatorname{Sym}_3\) means the average over
all six permutations of its arguments. Define the upward kernel

\[
C\Phi(x,y,z)=\operatorname{Sym}_3
      [K(x-z)\cdot\nabla_1\Phi(x,y)].
\tag{3.4}
\]

For checking the factor \(1/6\), its expanded expression is

\[
\begin{split}
6C\Phi(x,y,z)={}&K(x-y)\cdot
 [\nabla_1\Phi(x,z)-\nabla_1\Phi(y,z)]\\
&+K(x-z)\cdot
 [\nabla_1\Phi(x,y)-\nabla_1\Phi(z,y)]\\
&+K(y-z)\cdot
 [\nabla_1\Phi(y,x)-\nabla_1\Phi(z,x)].
\end{split}
\tag{3.5}
\]

The two equivalent exact pair identities are

\[
\boxed{
dP_t[\Phi_t]
=\left\{P_t[(\partial_t+\mathcal L_{2,t})\Phi_t]
        +U_{3,t}[C\Phi_t]
        +\frac1{2N}D_{2,t}[B\Phi_t]\right\}dt+dM_t^2[\Phi].}
\tag{3.6}
\]

To express every term in the centered hierarchy, put
\((B\Phi)_\mu(x)=\int B\Phi(x,y)\,d\mu(y)\). Then

\[
\boxed{
\begin{split}
dP_t[\Phi_t]={}&\bigg\{P_t[(\partial_t+\mathcal G_{2,N,t})\Phi_t]
 +U_{3,t}[C\Phi_t]
 +\frac1N U_{1,t}[(B\Phi_t)_{\mu_t}]\\
&\hspace{35mm}+\frac1{2N}\langle\mu_t^{\otimes2},B\Phi_t\rangle\bigg\}\,dt
 +dM_t^2[\Phi].
\end{split}}
\tag{3.7}
\]

The last term inside braces is the order-zero contraction. In the \(U_2\)
convention, multiply (3.6) or (3.7) by two: the upward coefficient becomes
\(2U_3[C\Phi]\), the order-one coefficient becomes \(2/N\), the scalar
coefficient becomes \(1/N\), and the martingale is \(2M^2\).

The martingale integrand, including its deletion, is

\[
\begin{split}
a_\Phi(x)&=\int\nabla_1\Phi(x,y)\,d\mu(y),\\
h_{i,\Phi}&=\frac1N\sum_{j\ne i}\nabla_1\Phi(x_i,x_j)-a_\Phi(x_i),\\
dM_t^2[\Phi]&=\frac{\sqrt{2\nu}}N\sum_i h_{i,\Phi_t}\cdot dW_i.
\end{split}
\tag{3.8}
\]

The lower terms in (3.7) are generated by interaction contractions and diagonal
deletion. For this deleted-label convention, independent particle diffusion
does not leave a separate drift contraction at order two. Section 4 displays
the Itô trace before its cancellation, rather than omitting it.

## 4. Complete proof of the pair identity

### 4.1. Explicit particle, mixed, and background terms

Let \(q_\Phi(x)=\int\Phi(x,y)\,d\mu(y)\) and
\(r_\Phi=\langle\mu^{\otimes2},\Phi\rangle\). The observable is exactly

\[
P[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(x_i,x_j)
             -\frac1N\sum_i q_\Phi(x_i)+\frac12r_\Phi.
\tag{4.1}
\]

Put \(v_i=(K*\rho)(x_i)\) and
\(D\Phi=\partial_t\Phi+(L_x^0+L_y^0)\Phi\). Independence gives
\(d[x_i^a,x_j^b]=2\nu\delta_{ij}\delta_{ab}dt\). There is no mixed second
derivative in the first sum of (4.1), because its labels are distinct, even if
the coordinates happen to coincide. Itô and symmetry give its drift as

\[
\frac1{2N^2}\sum_{i\ne j}D\Phi(x_i,x_j)
 +\frac1{N^2}\sum_{i\ne j}v_i\cdot\nabla_1\Phi(x_i,x_j).
\tag{4.2}
\]

The mixed term has drift

\[
-\frac1N\sum_i(D\Phi)_\mu(x_i)
-\frac1N\sum_i v_i\cdot a_\Phi(x_i).
\tag{4.3}
\]

Indeed the time derivative of the integrated background contributes
\(\int L_y^0\Phi(x,y)\,d\mu(y)\) by integration by parts on the torus. Finally,
the background-background term contributes
\(\tfrac12\langle\mu^{\otimes2},D\Phi\rangle\). Adding the three drift
expressions and the noises gives the raw exact identity

\[
dP[\Phi]
=\left\{P[D\Phi]+\frac1N\sum_i v_i\cdot h_{i,\Phi}\right\}dt+dM^2[\Phi].
\tag{4.4}
\]

This is the derivation from distinct particle sums. The remaining work is an
exact expansion of its force term, not an estimate.

### 4.2. Recovering both linearized responses

Let \(D_\Phi(x)=\nabla_1\Phi(x,x)\) and
\(h_\rho(x)=\int\nabla_1\Phi(x,y)\,d\rho(y)\). Then

\[
h_{i,\Phi}=h_\rho(x_i)-\frac1N D_\Phi(x_i).
\tag{4.5}
\]

Writing the force term in (4.4) as a measure product, and replacing its first
slot \(\eta\) by \(\mu+\rho\), gives

\[
\begin{split}
\frac1N\sum_i v_i\cdot h_{i,\Phi}
={}&\iiint K(x-z)\cdot\nabla_1\Phi(x,y)
                 \,d\rho(x)d\rho(y)d\rho(z)\\
&+\iiint K(x-z)\cdot\nabla_1\Phi(x,y)
                 \,d\mu(x)d\rho(y)d\rho(z)\\
&-\frac1N\iint K(x-z)\cdot D_\Phi(x)
                 \,d\eta(x)d\rho(z).
\end{split}
\tag{4.6}
\]

The first term is \(\langle\rho^{\otimes3},C\Phi\rangle\). Symmetry of the
two remaining \(\rho\)-slots shows that the second term is
\(\tfrac12\langle\rho^{\otimes2},(R_1+R_2)\Phi\rangle\). For any smooth
symmetric pair kernel \(F\),

\[
\langle\rho^{\otimes2},F\rangle
=U_2[F]+\frac1N\langle\eta,F(x,x)\rangle.
\tag{4.7}
\]

On the diagonal the two responses agree, so the second term in (4.6) is

\[
P[(R_1+R_2)\Phi]
 +\frac1N\iint K(z-x)\cdot\nabla_1\Phi(z,x)
                  \,d\eta(x)d\mu(z).
\tag{4.8}
\]

This proves that independent transport-diffusion alone is not the quadratic
operator. Both response terms have coefficient one.

### 4.3. Exact cubic overlap count and the lower terms

For any smooth symmetric triple kernel \(F\), splitting the empirical triple
sum into all-distinct labels, exactly-two-equal labels, and all-equal labels
gives

\[
\langle\rho^{\otimes3},F\rangle
=U_3[F]+\frac3N\iint F(x,x,z)\,d\eta(x)d\rho(z)
       -\frac2{N^2}\int F(x,x,x)\,d\eta(x).
\tag{4.9}
\]

Here is the count without a hidden factorial. In \(\eta^{\otimes3}\), the
three choices of the repeated pair give
\(3N^{-1}\eta^{\otimes2}[F(x,x,z)]\). This counts an all-equal triple three
times rather than once, requiring subtraction of
\(2N^{-2}\eta[F(x,x,x)]\). The term
\(-3\eta^{\otimes2}\otimes\mu[F]\) in \(\rho^{\otimes3}\) differs from its
deleted counterpart by
\(-3N^{-1}\eta\otimes\mu[F(x,x,z)]\). Combining the two differences gives
(4.9), for all \(N\geq2\), including \(N=2\) where the all-distinct triple sum
is empty.

For the kernel in (3.4), \(K(0)=0\) gives

\[
C\Phi(x,x,x)=0,\qquad
3C\Phi(x,x,z)
=K(x-z)\cdot D_\Phi(x)
 +K(z-x)\cdot\nabla_1\Phi(z,x).
\tag{4.10}
\]

Consequently the first contribution in (4.10), inserted into (4.9), cancels
the last line of (4.6) exactly. Its second contribution combines with (4.8)
by \(\rho+\mu=\eta\). The resulting entire residual is

\[
\begin{split}
\frac1N\iint K(z-x)\cdot\nabla_1\Phi(z,x)\,d\eta(x)d\eta(z)
&=\frac1{2N}\langle\eta^{\otimes2},B\Phi\rangle\\
&=\frac1{2N}D_2[B\Phi].
\end{split}
\tag{4.11}
\]

The first equality follows by interchanging \(x,z\), using oddness of \(K\)
and symmetry of \(\Phi\). The second follows from \(B\Phi(x,x)=0\), without
discarding any nonzero diagonal. Equations (4.4)--(4.11) prove (3.6).

Lastly the definition of \(U_2\) gives

\[
D_2[B\Phi]
=U_2[B\Phi]+2\langle\rho,(B\Phi)_\mu\rangle
                      +\langle\mu^{\otimes2},B\Phi\rangle,
\tag{4.12}
\]

which proves (3.7). In particular there is no unexplained \(N^{-2}\) drift
term: the only possible all-equal cubic correction in (4.9) is zero by
(4.10). Every \(1/N\) interaction contraction is retained in (3.7).

### 4.4. Full-product convention and the Itô trace

Define the full-product statistic and the mixed trace by

\[
Q[\Phi]=\frac12\langle\rho^{\otimes2},\Phi\rangle,
\qquad d_\Phi(x)=\Phi(x,x),\qquad
\tau_\Phi(x)=\sum_{a=1}^d\partial_{x_a}\partial_{y_a}\Phi(x,x).
\tag{4.13}
\]

Then the exact conversion is

\[
P[\Phi]=Q[\Phi]-\frac1{2N}\langle\eta,d_\Phi\rangle.
\tag{4.14}
\]

Applying Itô to the explicit full particle double sum, the \(i=j\) terms
produce the cross-variation drift

\[
dQ[\Phi]
=\left\{\frac12\langle\rho^{\otimes2},(\partial_t+\mathcal L_2)\Phi\rangle
        +\langle\rho^{\otimes3},C\Phi\rangle
        +\frac\nu N\langle\eta,\tau_\Phi\rangle\right\}dt+dM^Q[\Phi].
\tag{4.15}
\]

Here \(dM^Q=(\sqrt{2\nu}/N)\sum_i h_\rho(x_i)\cdot dW_i\). The diagonal
map satisfies

\[
\nabla d_\Phi(x)=2D_\Phi(x),\qquad
\Delta d_\Phi(x)
=[(\Delta_x+\Delta_y)\Phi](x,x)+2\tau_\Phi(x).
\tag{4.16}
\]

In subtracting the Itô derivative of the last term of (4.14), the last
contribution in (4.16) is exactly
\(-\nu N^{-1}\langle\eta,\tau_\Phi\rangle dt\), canceling (4.15). The time
and local transport derivatives on the diagonal cancel as well. The diagonal
of the response gives (4.8), and the nonlinear diagonal drift gives the last
line of (4.6). The noise subtraction changes \(h_\rho\) to (4.5). Thus the
full-product calculation reproduces (3.6) including all cancellations.

This cancellation depends on the deleted-label statistic and on independent
particle noises. It is not permission to ignore Itô traces in a different
convention, for common noise, or when a singular diagonal has not been defined.

## 5. Exact quadratic and cross variations

For two one-body tests \(f,h\) and two symmetric pair tests \(\Phi,\Psi\),
all deterministic and time dependent, the predictable brackets are

\[
\begin{split}
d\langle M^1[f],M^1[h]\rangle_t
 &=\frac{2\nu}{N}\langle\eta_t,\nabla f_t\cdot\nabla h_t\rangle dt,\\
d\langle M^1[f],M^2[\Phi]\rangle_t
 &=\frac{2\nu}{N^2}\sum_i\nabla f_t(x_i)\cdot h_{i,\Phi_t}\,dt,\\
d\langle M^2[\Phi],M^2[\Psi]\rangle_t
 &=\frac{2\nu}{N^2}\sum_i h_{i,\Phi_t}\cdot h_{i,\Psi_t}\,dt.
\end{split}
\tag{5.1}
\]

The same expressions are the pathwise quadratic covariations. To expose the
particle-label contractions in the pair bracket, set
\(p_{ij}^{\Phi}=\nabla_1\Phi(x_i,x_j)\) and \(a_i^\Phi=a_\Phi(x_i)\). Then

\[
\begin{split}
\frac{d\langle M^2[\Phi],M^2[\Psi]\rangle_t}{dt}
=2\nu\bigg[&\frac1{N^4}\sum_{i,j,k\ {\mathrm{distinct}}}
                    p_{ij}^\Phi\cdot p_{ik}^\Psi
 +\frac1{N^4}\sum_{i\ne j}p_{ij}^\Phi\cdot p_{ij}^\Psi\\
&-\frac1{N^3}\sum_{i\ne j}
          (p_{ij}^\Phi\cdot a_i^\Psi+a_i^\Phi\cdot p_{ij}^\Psi)
 +\frac1{N^2}\sum_i a_i^\Phi\cdot a_i^\Psi\bigg].
\end{split}
\tag{5.2}
\]

The second term is precisely the contraction \(j=k\); it has not been
absorbed into an all-distinct triple. The one-body/pair bracket is

\[
\frac{d\langle M^1[f],M^2[\Phi]\rangle_t}{dt}
=2\nu\left[\frac1{N^3}\sum_{i\ne j}\nabla f(x_i)\cdot p_{ij}^\Phi
             -\frac1{N^2}\sum_i\nabla f(x_i)\cdot a_i^\Phi\right].
\tag{5.3}
\]

In particular the corrected martingale has the exact bracket

\[
d\langle M^1[f]+M^2[\Phi]\rangle_t
=\frac{2\nu}{N^2}\sum_i
       |\nabla f_t(x_i)+h_{i,\Phi_t}|^2\,dt.
\tag{5.4}
\]

The pair correction therefore need not preserve the covariance of the
one-body martingale. A convergence argument must control the cross term,
rather than only each self-bracket.

For fixed tests, the elementary bounds

\[
|h_{i,\Phi}|\leq(2-N^{-1})\|\nabla_1\Phi\|_\infty,
\quad
\langle M^2[\Phi]\rangle_T
\leq\frac{8\nu T}{N}\sup_{t\leq T}\|\nabla_1\Phi_t\|_\infty^2,
\quad
\langle M^1[f]\rangle_T
\leq\frac{2\nu T}{N}\sup_{t\leq T}\|\nabla f_t\|_\infty^2
\tag{5.5}
\]

show square integrability. The dependence on temperature is explicit. These
bounds are not cutoff-uniform estimates for a singularly generated corrector.

## 6. Falsification and normalization checks

### 6.1. Constant kernels, zero interaction, and iid centering

For \(\Phi_t=c(t)\), direct counting gives
\(U_2[c]=-c/N\), so \(P[c]=-c/(2N)\). All spatial operators and martingales
vanish, and (3.7) gives precisely \(dP=-c'(t)dt/(2N)\). Thus the word
"centered" in the dossier does not mean that \(U_2\) annihilates constants.

For \(K=0\), both responses, \(B\), and \(C\) vanish. Formula (3.7) reduces to
\(dP=P[(\partial_t+L_x^0+L_y^0)\Phi]dt+dM^2\). In particular there is no
residual deterministic Itô contraction. This is also immediate from (4.1)
for independent diffusions and independently evolving reference slots.

At an iid configuration with common law \(\mu\), the exact expectations are

\[
\mathbb E U_2[\Phi]=-\frac1N\langle\mu^{\otimes2},\Phi\rangle,
\qquad
\mathbb E U_3[F]=\frac2{N^2}\langle\mu^{\otimes3},F\rangle.
\tag{6.1}
\]

Indeed the coefficients are respectively
\((N)_2/N^2-2+1=-1/N\) and
\((N)_3/N^3-3(N)_2/N^2+3-1=2/N^2\).
These are preparation-time computations only: the interacting dynamics do not
preserve the iid law. No expectation estimate has been converted to a
fluctuation estimate.

### 6.2. Separable-kernel product-rule test

For \(\Phi_t(x,y)=f_t(x)f_t(y)\), put \(Z_t=\langle\rho_t,f_t\rangle\). Then

\[
P[f\otimes f]=\frac12Z^2-\frac1{2N}\langle\eta,f^2\rangle,
\qquad
h_{i,f\otimes f}=(Z-f(x_i)/N)\nabla f(x_i).
\tag{6.2}
\]

Apply the scalar Itô product rule to the first equality. The trace from
\(\tfrac12Z^2\) is \(\nu N^{-1}\eta[|\nabla f|^2]\), while the diffusion
part of \(-(2N)^{-1}\eta[f^2]\) gives its negative. The remaining drift is

\[
Z\{\rho[(\partial_t+L)f]+P[H_f]\}
-\frac1N\eta\big[f(\partial_t+L^0)f
                       +f(K*\rho)\cdot\nabla f\big].
\tag{6.3}
\]

For (3.6), the independent pair operator plus both responses gives

\[
P[(\partial_t+\mathcal L_2)(f\otimes f)]
=Z\rho[(\partial_t+L)f]-N^{-1}\eta[f(\partial_t+L)f].
\tag{6.4}
\]

Equations (4.9)--(4.11) in this separable case give

\[
U_3[C(f\otimes f)]+\frac1{2N}D_2[B(f\otimes f)]
=ZP[H_f]-\frac1N\eta[f(K*\rho)\cdot\nabla f]
          +\frac1N\eta[fAf].
\tag{6.5}
\]

The (Af) term in (6.5) cancels its occurrence in (6.4), recovering (6.3)
and the martingale in (6.2). Polarizing this identity also checks symmetric
kernels \(\tfrac12(f\otimes h+h\otimes f)\).

### 6.3. The \(N=2,3\) coefficients and a Fourier-mode calculation

The observable itself is

\[
P_2[\Phi]=\frac14\Phi(x_1,x_2)-\frac12(q_\Phi(x_1)+q_\Phi(x_2))
                    +\frac12r_\Phi,
\tag{6.6}
\]

and

\[
P_3[\Phi]=\frac19\sum_{i<j}\Phi(x_i,x_j)-\frac13\sum_iq_\Phi(x_i)
                    +\frac12r_\Phi.
\tag{6.7}
\]

The internal force acting between the two labels of a particle-particle pair
has coefficient \(N^{-3}\sum_{i<j}B\Phi(x_i,x_j)\), exactly the last term of
(3.6). This is \(B\Phi(x_1,x_2)/8\) at \(N=2\) and
\(\sum_{i<j}B\Phi(x_i,x_j)/27\) at \(N=3\).

For a symmetric \(F\), direct counting gives

\[
\begin{split}
U_{3,2}[F]&=-\frac32\int F(x_1,x_2,z)\,d\mu(z)
  +\frac32\sum_{i=1}^2\iint F(x_i,y,z)\,d\mu(y)d\mu(z)-\mu^{\otimes3}[F],\\
U_{3,3}[F]&=\frac29F(x_1,x_2,x_3)
 -\frac23\sum_{i<j}\int F(x_i,x_j,z)\,d\mu(z)
 +\sum_{i=1}^3\iint F(x_i,y,z)\,d\mu(y)d\mu(z)-\mu^{\otimes3}[F].
\end{split}
\tag{6.8}
\]

Thus \(U_3\) is generally nonzero at \(N=2\), despite the absence of three
distinct particle labels. Dropping it at \(N=2\) would fail the identity.

A completely explicit Fourier check uses \(d=1\), \(\mu=1\), \(b=0\),
\(g(x)=\kappa\cos(2\pi x)/(2\pi)\), hence \(K(x)=\kappa\sin(2\pi x)\), and
\(\Phi(x,y)=\cos(2\pi(x-y))\). The background is stationary. Each response
operator acts as \(-\pi\kappa\) on the relevant first Fourier mode, so

\[
\mathcal L_2\Phi=-(8\pi^2\nu+2\pi\kappa)\Phi,
\qquad B\Phi=-4\pi\kappa\sin^2(2\pi(x-y)).
\tag{6.9}
\]

Moreover

\[
\int C\Phi(x,y,z)\,dz=-\frac{\pi\kappa}3\Phi(x,y),
\qquad \iint C\Phi(x,y,z)\,dy\,dz=0.
\tag{6.10}
\]

At \(N=2\), (6.8) therefore gives
\(U_3[C\Phi]=(\pi\kappa/2)\cos(2\pi(x_1-x_2))\). In (3.6) this exactly
cancels the response contribution to \(P[\mathcal L_2\Phi]\), leaving drift

\[
-2\pi^2\nu\cos(2\pi(x_1-x_2))
-\frac{\pi\kappa}2\sin^2(2\pi(x_1-x_2)).
\tag{6.11}
\]

Applying the two-particle generator directly to
\(P_2=\tfrac14\cos(2\pi(x_1-x_2))\) gives exactly (6.11). This checks the
response sign, upward normalization, internal \(1/N\), and diffusion factor.

### 6.4. Executed numerical battery

Command:

```text
python3 DISCOVERY_CODE/round001_pair_selfcheck.py
```

Environment: Python 3.9.6, standard library only. No random inputs. The script
compares the direct configuration generator of (4.1), with the reference
derivative computed from its PDE, to (3.7). It evaluates \(U_2,U_3\) by the
literal subset/distinct-label definition, without using the overlap formula
(4.9) on the decomposed side.

The tests use a strictly positive nonconstant trigonometric density,
a smooth periodic gradient confinement, either zero force or two sine force
modes, \(\nu=1/3,2\), and \(N=2,3\). They include both distinct and coincident
coordinates and five kernels: constant, separable sine product, one difference
Fourier mode, a sum of one-body modes, and symmetric mixed Fourier modes.
Quadrature uses 24 equally spaced points; all integrands are finite Fourier
polynomials within its exact integration range. Evaluation remains floating
point, with tolerance \(2\times10^{-10}\).

Actual output:

```text
Python 3.9.6
Status: EXPLORATORY constructor self-check; no random inputs
Quadrature grid: 24 points; tolerance: 2e-10
One-body checks: 16 maximum absolute error: 4.263e-14
Pair checks: 80 maximum absolute error: 2.274e-13
N=2,3; positive and zero force; nu=1/3,2; nonconstant positive background;
constant, separable, difference-mode, one-body-sum, mixed-mode kernels;
both distinct and coincident coordinates. PASS
```

These tests are `EXPLORATORY` constructor self-checks, not independent
certification. The algebraic proof does not depend on the tolerance or results.

## 7. Fixed-smooth backward equations and the exact corrector reduction

There is no fixed-smooth existence gap for either the one-body equation or the
pair equation. Here is the relevant construction, without a cutoff-uniform
claim. Integration by parts gives

\[
Af(y)=-\int \operatorname{div}_z(\mu(z)K(z-y))f(z)\,dz,
\quad
R_1\Phi(x,y)=-\int\operatorname{div}_z(\mu(z)K(z-x))\Phi(z,y)\,dz,
\tag{7.1}
\]

and the analogous formula for \(R_2\). For each fixed integer \(m\geq0\),
these are bounded operators on \(C^m\), with norm bounded by a constant
depending only on \(d,m,\|\mu\|_{C^1}\), and \(\|K\|_{C^{m+1}}\). They have
no derivative loss on the unknown function: the derivative in the integrated
slot has been transferred to the smooth coefficient. The operator does not
require division by \(\mu\).

Let \(S_{r,t}\) be the backward propagator of the local diffusion, using drift
\(u\) in the one-body case and the two drifts stated after (3.3) in the pair
case. The stochastic flow construction is elementary here: after subtracting
the additive Brownian path, it is an ODE with smooth time-dependent spatial
coefficients. Spatial derivatives of its flow satisfy the differentiated ODEs;
Gronwall and induction bound derivatives through any fixed order \(m\) on the
finite horizon. Averaging a \(C^m\) terminal function over this flow therefore
gives a bounded propagator on \(C^m\). For fixed background derivative bounds,
the local drift estimates are uniform in \(N\geq2\), since its additional
coefficient is \(1/N\); no derivative of the Brownian path is taken.

For response \(R=A\) or \(R=R_1+R_2\), the equation
\((\partial_r+G_r^0+R_r)v_r=-F_r\), \(v_t=v^{\rm fin}\), is equivalent to

\[
v_r=S_{r,t}v^{\rm fin}+\int_r^t S_{r,a}(R_av_a+F_a)\,da.
\tag{7.2}
\]

Picard iteration of this Volterra equation converges in \(C([0,t];C^m)\):
the \(n\)-fold time integral is bounded by a constant to the \(n\)-th power
times \(t^n/n!\). The same estimate proves uniqueness. Taking compatible
solutions for every \(m\) gives a smooth spatial solution; the local backward
equation and (7.2) give its time derivative. For smooth forcing this is a
classical solution. The constructed propagators respect the permutation
symmetry of a pair kernel. All constants depend on the indicated smooth
coefficient norms and the finite horizon. In particular, uniform control of
those norms as \(N,\beta_N\), or a regularization parameter vary has not been
proved here.

Take the one-body solution \(f\) from (2.8), and solve the pair equation

\[
(\partial_r+\mathcal G_{2,N,r})\Phi_r=-H_{f_r},
\qquad \Phi_t=0.
\tag{7.3}
\]

Combining (2.3) and (3.7) gives the exact cancellation formula

\[
\begin{split}
\langle\rho_t,\phi\rangle
={}&\langle\rho_0,f_0\rangle+P_0[\Phi_0]+M_t^1[f]+M_t^2[\Phi]\\
&+\int_0^t\left\{U_{3,r}[C\Phi_r]
 +\frac1N\langle\rho_r,(B\Phi_r)_{\mu_r}\rangle
 +\frac1{2N}\langle\mu_r^{\otimes2},B\Phi_r\rangle\right\}\,dr.
\end{split}
\tag{7.4}
\]

This specifies the corrector, its sign, initial boundary term, scalar
contraction, and its full martingale. It does not assert that any residual is
small.

## 8. Centering, uniformity, and the first analytic gap

All displayed identities use the mean-field reference \(\mu\), including its
dependence on \(N,\beta_N,g\). If \(m_t=\mathbb E\eta_t\) and
\(\chi=\eta-m\), \(\delta=m-\mu\), then the exact algebraic conversion is

\[
P_\mu[\Phi]=P_m[\Phi]+\langle\chi,\Phi_\delta\rangle
                         +\frac12\langle\delta^{\otimes2},\Phi\rangle,
\qquad \Phi_\delta(x)=\int\Phi(x,y)\,d\delta(y).
\tag{8.1}
\]

For exchangeable laws, \(m\) is the common first marginal. No claim that \(m\)
solves the mean-field PDE is made, and it cannot be substituted for \(\mu\) in
the proved evolution without redoing its reference evolution. Formula (8.1)
is only a centering map, not a bias estimate.

For each fixed smooth \(g,V,\mu,f,\Phi\), the equalities hold on the whole
configuration space and throughout the finite horizon. Constants in the
elementary martingale bounds are stated in (5.5). No constant in the backward
construction has been shown uniform as \(g=g_\varepsilon\) approaches a Riesz
kernel, or as derivatives of the background grow with \(N,\beta_N\). No
Fourier coefficient normalization for the singular target, no logarithmic
normalization, and no collision-limit theorem is asserted.

The first unproved analytic line after this task is a quantitative,
law-specific estimate for the right side of (7.4), beginning with the cubic
remainder

\[
\sigma_N\int_0^t U_{3,r}[C\Phi_r],dr,
\tag{8.2}
\]

together with the random order-one contraction, the initial quadratic
boundary term, the deterministic centering at the required accuracy, and the
bracket/cross-bracket contribution of \(M^2\). In the singular campaign the
corrector bounds and each passage must additionally be uniform in the cutoff
in the intended \(N,\beta_N\) regime. Under the task's arbitrary initial law,
there is no smallness or fluctuation theorem supplied by the identity alone.

Thus the smooth pair algebra and fixed-smooth backward cancellation are
proved here, while singular passage, fluctuation estimates, and the
subcritical/critical mission remain open. The root coordinator must compare
the coefficients with an isolated construction before any independent audit
status is granted.

## 9. Handoff and verification

Created files:

- `MEMORANDA/ROUND_001_ALGEBRA.md` — this complete construction and self-check.
- `DISCOVERY_CODE/round001_pair_selfcheck.py` — the executed numerical battery.

Inspected inputs: `AGENTS.md`, `README_FIRST.md`, `MASTER_PROMPT.md`,
`CAMPAIGN_PROTOCOLS.md`, `MODEL_ORCHESTRATION.md`, both baseline state/assessment
documents, `PLANS.md`, `INPUTS/SOURCE_MANIFEST.md`, `INPUTS/note_v2.pdf`, the
canonical `STATE/` files, and the two frozen Round 001 task/model files. No
other worker's proof was read. The model/task files were pre-existing
untracked inputs in this worktree and were not altered.

Verification commands and outcomes:

```text
python3 scripts/verify_campaign.py
  CAMPAIGN VERIFICATION PASSED
  Imported note SHA-256:
  a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76

python3 DISCOVERY_CODE/round001_pair_selfcheck.py
  16 one-body and 80 fully decomposed pair tests passed (Section 6.4).
```

The system Python lacked SymPy, and the bundled Python also lacked SymPy.
No dependency was installed; the checks were implemented with the standard
library. The source note was text-extracted with the existing bundled
`pypdf`; no visual or typesetting claim is made about it. This worker produced
a Markdown proof, not a TeX artifact, and therefore no TeX build was run.
