# Round 003: hostile review of the internal-pair transport model

Date: 2026-09-17 UTC. Task: TASK-027. Reviewer: /root/r002_coupling.
Worktree: /private/tmp/hocf-round003-probability-blind-20260917.
Base: 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2.

**Verdict: PASS for THM-017's declared punctured, zero-diffusion transport
model and its separately defined initial iid diagnostic.**
No mathematical counterexample or load-bearing proof failure was found.
The all-\(N\) reading of the card requires an enlargement of the constant
from the proof's explicitly large-\(N\) display (7.4); Section 5 below
derives it from the submitted bounds. This is a nonblocking completion of
the stated constant, with no new hypothesis or change in the conclusion.
The full-corrector comparison (8.2) remains **OPEN**.

This is a claim-specific hostile review after reading the complete
submitted proof, not a blind reconstruction or a fresh-session audit.
The reviewer did not propose or construct this transport model and did not
see its construction narrative before the present review. Prior context
contains the reviewer's own smooth residual, iid pair-moment, Gaussian,
and probability reconstructions. In particular the exact iid projection
identity is a previously proved prerequisite in this context. Its
coefficients are rechecked below; no unrelated new constructor report,
TASK-022 narrative, or constructor worktree was inspected.
The already sealed TASK-024 report and its support files are unchanged.

The task, theorem card, and complete proof were hash-verified against
AUDITS/ROUND_003_PAIR_TRANSPORT_REVIEW_INPUT_SHA256SUMS.txt before reading.
The source reviewed is MEMORANDA/ROUND_003_PAIR_TRANSPORT_MODEL.md, not a
later corrected copy. Source locations below refer to its section and
equation numbers; the line numbers identify the submitted version.

## 1. Per-result dispositions

| Result reviewed | Source location | Verdict |
|---|---|---|
| Relative drift, sign, source, \(N/4\) coefficient | §1, (1.1)--(1.5), lines 24--71 | PASS |
| Existence and uniqueness in the declared forward characteristic class | §1, lines 29--71 | PASS; no collision boundary or broader weak uniqueness is implied |
| Core and far bounds, exact amplitude, far expansion | §2, (2.1)--(2.6), lines 83--128 | PASS |
| Collision limits, isotropic regularity, anisotropic Laplacian, terminal corner | §3, lines 132--157 | PASS on the explicitly punctured domain |
| Sphere fourth moments and nonzero traceless norm | §4, (4.1), lines 163--170 | PASS, including \(d=1\) separately |
| Exact local norm, all three regimes, constants and asymptotics | §4, (4.2)--(4.8), lines 174--244 | PASS |
| Compact periodic cutoff, symmetry and annular term | §6, (6.1)--(6.4), lines 258--293 | PASS as a separately defined diagnostic |
| One density factor and full mean-field iid centering | §7, (7.1)--(7.3), lines 297--343 | PASS |
| Uniform deterministic-time iid endpoint and positive-temperature factors | §7, (7.4), lines 345--366 | PASS; all finite \(N\) constant made explicit in Section 5 below |
| Full-operator residual bookkeeping | §8, (8.1), lines 370--391 | PASS only conditional on the indicated expressions being defined |
| Full-corrector comparison and evolved-law transfer | §8, (8.2), lines 393--403 | OPEN and correctly excluded from the theorem |

The exact negation tested is an admissible parameter or characteristic-class
solution violating the explicit formula or one of its declared bounds,
or an iid bounded-density preparation violating the diagnostic endpoint.
The direct calculations below exclude these negations for the stated
objects. They do not exclude failure of the unproved singular-dynamics
bridges.

## 2. Independent characteristic, profile, and coincidence checks

Write \(p=s+2\), \(c=2sp\), \(a(\theta)=\theta^TA\theta\), and
\(\tau=T-t\). For a relative-coordinate kernel,
\((\nabla_x-\nabla_y)\Phi(x-y)=2\nabla_z\Phi(z)\).
With \(K(z)=s z|z|^{-s-2}\), the two internal particle forces therefore
produce exactly
\[
 v_N(z)=\frac{2s}{N}|z|^{-s-2}z.
 \tag{R2.1}
\]
For the declared quadratic test, \(\nabla f(x)-\nabla f(y)=Az\);
its dot product with \(K(z)\) is \(s|z|^{-s}a(\theta)\), without an
extra factor \(1/2\).

The forward radial equation gives
\[
 \frac{d}{dh}r(h)^p=\frac cN,\qquad
 r(h)=\left(r^p+\frac{ch}{N}\right)^{1/p}.
 \tag{R2.2}
\]
It exists for all finite forward times from every nonzero starting
point, remains positive, and keeps its direction fixed. On this curve,
the stated equation reads \(d\Phi/dh=-s\,a(\theta)r(h)^{-s}\).
Absolute continuity and the terminal condition force
\[
 \Phi(t,z)=s\,a(\theta)\int_0^\tau r(h)^{-s}\,dh.
 \tag{R2.3}
\]
Since \(dh=N r^{s+1}dr/(2s)\), the radial integral is
\((N/2)\int r\,dr\). This proves exactly
\[
 \Phi=a(\theta)F(r),\qquad
 F(r)=\frac N4\left[\left(r^p+\frac{c\tau}{N}\right)^{2/p}-r^2\right].
 \tag{R2.4}
\]
It is finite and smooth on the punctured domain. Conversely every member
of the specified characteristic class must equal (R2.3), proving the
claimed uniqueness in precisely that class. Backward characteristic
collision is not needed: every starting point is integrated forward to
the terminal time.

An independent differential substitution, with \(W=r^p+c\tau/N\), gives
\[
 F_\tau=sW^{-s/p},\qquad
 F_r=\frac N2\left(r^{s+1}W^{-s/p}-r\right),\qquad
 -F_\tau+\frac{2s}{N}r^{-s-1}F_r=-sr^{-s}.
 \tag{R2.5}
\]
At zero remaining time \(F=0\) and \(F_\tau=sr^{-s}\), verifying both
the terminal condition and the sign. For \(N=2,3\), the prefactors in
(R2.4) are respectively \(1/2,3/4\), and the characteristic increments
are respectively \(sp\tau,2sp\tau/3\), exactly as submitted.

For \(\tau>0\), let \(\ell=(c\tau/N)^{1/p}\) and
\(H(u)=(1+u^p)^{2/p}-u^2\). Direct integration gives
\[
 H(u)=\alpha\int_0^1(u^p+v)^{-\gamma}dv,\qquad
 \alpha=\frac2p,\quad\gamma=\frac sp.
 \tag{R2.6}
\]
Its derivative is negative for \(u>0\); \(H(0)=1\) and
\(H(1)=h_s=2^{2/p}-1\). Thus the submitted near bounds are exact
consequences of \(h_s\le H\le1\) on \([0,1]\).
For \(u\ge1\), (R2.6) yields
\(\alpha2^{-\gamma}u^{-s}\le H(u)\le\alpha u^{-s}\).
Multiplication by \(N\ell^2/4\), and
\(N\ell^p=c\tau\), gives precisely
\[
 s2^{-s/p}\tau r^{-s}\le F(r)\le s\tau r^{-s}.
 \tag{R2.7}
\]
The upper bound also follows from (R2.3) for every \(r>0\).
These are radial-amplitude bounds; the signed solution must retain
\(a(\theta)\).

The Taylor expansion parameter is \(x=c\tau/(Nr^p)\), not \(r/\ell\).
The first two binomial coefficients give
\[
 \frac14\alpha c=s,\qquad
 \frac18\alpha(\alpha-1)c^2=-s^3.
 \tag{R2.8}
\]
The next coefficient is finite for fixed \(s\), so the submitted far
expansion and its \(O_s(\tau^3N^{-2}r^{-3s-4})\) remainder follow as
\(x\to0\). This expansion cannot be used in the core.

At fixed positive remaining time,
\[
 F(r)=F_0-\frac N4r^2+\frac{N}{2p}\ell^{-s}r^{s+2}
               +O_s(N\ell^{-2s-2}r^{2s+4}),\qquad
 F_0=\frac{c^{2/p}}4N^{s/p}\tau^{2/p}.
 \tag{R2.9}
\]
Hence the collision limit is \(F_0a(\theta)\), independent of direction
exactly when \(A\) is scalar. If \(A=aI\), the extension is \(C^2\)
with Hessian \(-aNI/2\); derivatives of the \(r^{s+2}\) term of order two
are \(O(r^s)\). For positive even integral \(s\), \(r^{s+2}\) is a
polynomial in the coordinates, and the positive-base smooth composition
in (R2.4) gives a smooth extension. No general smooth extension follows.

For \(A_0=A-(\operatorname{tr}A/d)I\), set
\(a_0(\theta)=\theta^TA_0\theta\).
The polynomial \(z^TA_0z=r^2a_0(\theta)\) is harmonic, so
\(\Delta_Sa_0=-2d a_0\). Applying the polar Laplacian to (R2.9) gives
\[
 \Delta\Phi=-2dF_0r^{-2}a_0(\theta)
          -\frac N2\operatorname{tr}A
          +O_{s,A}(N\ell^{-s}r^s).
 \tag{R2.10}
\]
In particular the quadratic term is
\(-Nz^TAz/4\), whose Laplacian is \(-N\operatorname{tr}A/2\);
there is no missing angular contribution to that coefficient.
All calculations are classical on \(r>0\).

For fixed \(N\), \(F_0\to0\) as \(\tau\downarrow0\), so the submitted
uniform terminal limit on punctured balls follows even for nonscalar
\(A\). It supplies no continuous extension at earlier collision points.
For nonzero isotropic \(A\), the derivative of the extended collision
value diverges proportionally to \(\tau^{-s/p}\). None of these facts
is a joint uniform assertion as \(N\to\infty\).

## 3. Angular integration and local norm audit

For \(d\ge2\), rotation of
\((\theta_1+\theta_2)/\sqrt2\) and sign symmetry give
\(\mathbb E\theta_1^4=3\mathbb E\theta_1^2\theta_2^2\).
Expanding \(1=(\sum_i\theta_i^2)^2\) then yields
\[
 \mathbb E\theta_i^4=\frac3{d(d+2)},\qquad
 \mathbb E\theta_i^2\theta_j^2=\frac1{d(d+2)}\quad(i\ne j).
 \tag{R3.1}
\]
Diagonalizing a symmetric \(A\) proves, with the submitted convention
that \(\omega_d\) is the surface area of \(S^{d-1}\),
\[
 Q(A)=\frac{\omega_d}{d(d+2)}
       \left[(\operatorname{tr}A)^2+2\operatorname{tr}(A^2)\right].
 \tag{R3.2}
\]
For \(d=1\), the two-point sphere gives \(Q(A)=2A^2\) directly, agreeing
with the formula. Isotropic \(A=aI\) gives \(\omega_da^2\).
For \(d=2\), \(A=\operatorname{diag}(1,-1)\) gives \(a(\theta)=\cos2\theta\)
and \(Q(A)=\pi>0\). Thus tracelessness removes an angular mean, not the
square norm or the directional collision problem.

Polar integration of (R2.4) gives exactly
\[
 \|\Phi\|_{L^2(B_R)}^2
  =\frac{Q(A)N^2\ell^{d+4}}{16}
       I(R/\ell),\qquad
 I(L)=\int_0^L H(u)^2u^{d-1}du.
 \tag{R3.3}
\]
For \(L\le1\), the factors are \(h_s^2L^d/d\) and \(L^d/d\).
For \(L\ge1\), splitting at one and using (R2.6) gives
\[
 \frac{h_s^2}{d}+\alpha^22^{-2\gamma}J_\delta(L)
 \le I(L)\le\frac1d+\alpha^2J_\delta(L),\quad
 \delta=d-2s,\quad J_\delta(L)=\int_1^L u^{\delta-1}du.
 \tag{R3.4}
\]
This verifies every constant in the submitted (4.3)--(4.4).
For \(\delta>0\), the function
\(a+b(L^\delta-1)/\delta\) lies between
\(\min(a,b/\delta)L^\delta\) and
\(\max(a,b/\delta)L^\delta\). For \(\delta=0\), use the corresponding
minimum and maximum against \(1+\log L\). For \(\delta<0\),
\(0\le J_\delta(L)\le1/(2s-d)\).
These facts verify the stated comparison constants, including the
transition \(L=1\).

When \(\ell\le R\), the exact powers are determined by
\[
\begin{aligned}
 N^2\ell^{d+4}(R/\ell)^{d-2s}
       &=c^2\tau^2R^{d-2s},\\
 N^2\ell^{d+4}&=c^2\tau^2 &&(d=2s),\\
 N^2\ell^{d+4}
       &=c^{(d+4)/p}N^{(2s-d)/p}\tau^{(d+4)/p}
                                                    &&(2s>d).
\end{aligned}
\tag{R3.5}
\]
When \(\ell\ge R\), the exact near-core bounds instead give the factors
\(h_s^2/(16d)\) and \(1/(16d)\) times
\(Q(A)c^{4/p}N^{2s/p}\tau^{4/p}R^d\).
Thus the report does not inadvertently assume the core is always inside
the ball.

Finally \(H(u)\sim\alpha u^{-s}\). Elementary integral comparison then
gives the stated \(L^{d-2s}\) and logarithmic asymptotics, while for
\(2s>d\) the positive integral \(I(\infty)\) is finite. The coefficient
\(c^2\alpha^2/16=s^2\) verifies both submitted subcritical and logarithmic
leading constants. The supercritical leading constant in (4.8) follows
directly from the third line of (R3.5).
At \(\tau=0\) the norm is zero by definition; no formula divides by
\(\ell=0\). For fixed \(N\), all three norms tend to zero as
\(\tau\downarrow0\), including the logarithmic factor multiplied by
\(\tau^2\).

The bare-kernel square-integrability threshold \(2s=d\) appears in these
orders. The earlier bare-pair probability sufficient threshold \(s=3d/4\)
produces no new breakpoint for this finite-amplitude diagnostic: substitution
in the supercritical exponent still gives a strictly positive endpoint
decay exponent. This does not transfer a result between the two kernels.

## 4. Periodic cutoff, density, centering, and endpoint factors

The submitted function \(\psi\) in (6.1) has a positive denominator:
its two arguments cannot both be nonpositive because \(R_1>R_0\).
The defining exponential is flat at zero, so the cutoff is smooth,
one on \(B_{R_0}\), zero outside \(B_{R_1}\), and flat at its outer
edge. Since \(R_1<1/2\), extension by zero and periodicity is unambiguous.
Evenness gives a symmetric pair kernel. For nonscalar \(A\), the
arbitrary finite value at zero changes no \(L^2\) class or iid statistic.
This constructs a valid diagnostic, not a smooth periodic corrector.

The product rule gives the exact annular source
\[
 (\partial_t+v_N\cdot\nabla)(\chi\Phi)
       =-\chi J+(v_N\cdot\nabla\chi)\Phi,\qquad
 |(v_N\cdot\nabla\chi)\Phi|
 \le\frac{2s^2\tau}{N}\|A\|_{\rm op}\|\chi'\|_\infty
                         R_0^{-2s-1}.
 \tag{R4.1}
\]
The power is the sum of \(-s-1\) from the radial drift and \(-s\)
from (R2.7). No extra factor two or omitted derivative remains.

For a probability density \(\mu\le M\),
\[
 \int\mu(y+z)\mu(y)\,dy\le M.
 \tag{R4.2}
\]
This proves the single-factor density bound in (7.1); replacing it
by \(M^2\) is unnecessary. The proof works unchanged for an \(N\)-dependent
density with the same bound \(M\).

Independently decompose a symmetric kernel \(H\) as
\(H=m+q(x)+q(y)+r(x,y)\), with \(m=\mu^2H\), \(\mu q=0\), and
both one-variable integrals of \(r\) zero. Counting ordered labels
with the frozen \(N^2\) denominator yields
\[
 P_N[H]=-\frac{m}{2N}
       -\frac1{N^2}\sum_iq(X_i)
       +\frac1{N^2}\sum_{i<j}r(X_i,X_j).
 \tag{R4.3}
\]
Canonical pair terms with one shared label have zero covariance by
conditional independence; disjoint pairs are independent and centered.
They are also orthogonal to the first-projection sum. Therefore
\[
 \mathbb EP_N[H]^2
  =\frac{m^2}{4N^2}+\frac{\|q\|_2^2}{N^3}
      +\frac{N-1}{2N^3}\|r\|_2^2
  \le\frac{N-1}{2N^3}\|H\|_2^2.
 \tag{R4.4}
\]
Here \(\|H\|_2^2=m^2+2\|q\|_2^2+\|r\|_2^2\).
At \(N=2\) the bound is the equality \(\mathbb EP_2^2=\|H\|_2^2/16\).
At \(N=3\) the exact coefficients are \(m^2/36,\|q\|_2^2/27,\|r\|_2^2/27\).
The mean and first projection are retained, rather than erased by an
expectation-centering substitution.

For \(\sigma_N^2=Nb_N\), (R4.4) gives exactly the diagnostic estimate
\[
 \mathbb E|\sigma_NP_N[\mathcal H_{N,\tau}]|^2
 \le\frac{b_N(N-1)}{2N^2}\,
                      M\|\Phi_N\|_{L^2(B_{R_1})}^2.
 \tag{R4.5}
\]
The submitted separate bounds on the mean and first projection also
check: \(\|h\|_1\le C_A\tau\) implies
\(|m|\le MC_A\tau\), \(\|q\|_\infty\le2MC_A\tau\).
Multiplication of their exact coefficients by \(Nb_N\) gives respectively
\(b_NM^2C_A^2\tau^2/(4N)\) and
\(4b_NM^2C_A^2\tau^2/N^2\).

For Haar preparation and nonzero traceless \(A\), radial cutoff integration
gives \(m=q=0\). The canonical coefficient is then an equality, and
the norms on \(B_{R_0}\) and \(B_{R_1}\) bound the cutoff norm on both
sides. This verifies the claimed two-sided asymptotic orders for that
example at fixed positive remaining time. Nonzero traceless matrices
exist only when \(d\ge2\), as the submission states.

## 5. Uniform time and an explicit all-\(N\) constant

The submitted (7.4) is explicitly stated for sufficiently large \(N\);
the theorem card does not repeat that qualification. The gap in exposition
is removable from the submitted estimates as follows. This section proves
the all-\(N\) bound and specifies exactly what is being accepted.

If \(T=0\), every endpoint is zero. Assume \(T>0\), put \(R=R_1\), and set
\[
 n_0=\max\left(2,\left\lceil cT/R^p\right\rceil\right),\quad
 D=\frac{M Q(A)c^{4/p}T^{4/p}R^d}{32d},\quad
 e=\frac{d+2-s}{p}>0.
 \tag{R5.1}
\]
The radial amplitude is increasing in \(\tau\) by (R2.5), so its squared
local norm at every \(\tau\in[0,T]\) is bounded by its norm at \(T\).
This is used only inside the deterministic kernel bound (R4.5), not
to assert pathwise monotonicity of the centered random statistic.

For \(N\ge n_0\), the final-time core lies in \(B_R\).
Define, according to the indicated regime,
\[
\begin{aligned}
 U_+&=\max\left(\frac1d,\frac{\alpha^2}{d-2s}\right)
                                                    &&(2s<d),\\
 U_0&=\max\left(\frac1d,\alpha^2\right)
                                                    &&(2s=d),\\
 U_-&=\frac1d+\frac{\alpha^2}{2s-d}
                                                    &&(2s>d).
\end{aligned}
\tag{R5.2}
\]
The following constants bound the large-\(N\) endpoint by the respective
rate \(b_N/N\), \(b_N(1+\log N)/N\), or \(b_NN^{-e}\):
\[
\begin{aligned}
 C_+&=\frac{M Q(A)c^2T^2R^{d-2s}U_+}{32},\\
 C_0&=\frac{M Q(A)c^2T^2U_0}{32}
       \left(1+\left|\log\frac{R}{(cT)^{1/p}}\right|+\frac1p\right),\\
 C_-&=\frac{M Q(A)c^{(d+4)/p}T^{(d+4)/p}U_-}{32}.
\end{aligned}
\tag{R5.3}
\]
For the logarithmic line,
\(1+\log(R/\ell_T)=1+\log(R/(cT)^{1/p})+(\log N)/p\)
is bounded by the displayed parenthesis times \(1+\log N\).
These formulas follow directly from (R3.3)--(R3.5) and (R4.5).

For the finitely many integers \(2\le N<n_0\), the global core-amplitude
bound gives, without assuming a core location,
\[
 \sup_{\tau\le T}\mathbb E|\sigma_NP_N[\mathcal H_{N,\tau}]|^2
       \le D\,b_NN^{2s/p-1}.
 \tag{R5.4}
\]
In the first two regimes this is bounded by the claimed rate times
\(Dn_0^{2s/p}\); in the third regime it is bounded by the claimed rate
times \(Dn_0^{d/p}\), because \(2s/p-1+e=d/p\).
Thus the maxima of these finite-\(N\) constants and their corresponding
constants in (R5.3) prove the theorem card's uniform bound for every
\(N\ge2\). All are finite for fixed \(d,s,A,M,R,T\) and independent
of \(N,\tau,\beta_N\). If \(A=0\), all endpoints vanish.
No revision to the frozen proof is necessary to make this completion
available in the audit record.

The supremum established is
\(\sup_{\tau\in[0,T]}\mathbb E|\sigma_NP_N[\mathcal H_{N,\tau}]|^2\),
not an expectation of a stochastic supremum, and not an estimate for an
adaptively selected remaining time. At \(2s=d\) the bound agrees with
the submitted direct control of \(\tau^2\log(1/\tau)\).
For a temperature sequence that varies strongly, for example
\(\beta_N=N^4\) at even \(N\) and \(\beta_N=N^{-4}\) at odd \(N\),
one has respectively \(b_N=1\) and \(b_N=N^{-4}\). The same constants
apply and all three bounds still vanish. Temperature enters only this
scale, not the zero-diffusion equation.

## 6. Scope audit and the unproved operator bridge

The following exclusions are mathematically necessary and are preserved
in the submission:

- Diffusion is absent. For a relative kernel the actual pair diffusion
  would be \(2\nu_N\Delta_z\), not \(\nu_N\Delta_z\).
- Ordinary background transport gives
  \((u(x)-u(y))\cdot\nabla_z\); a general full solution need not remain
  a relative-coordinate kernel.
- Both nonlocal response operators require their own definition and
  estimates with the evolving density. The present proof provides none.
- The periodic force remainder, the actual time-dependent source and
  backward test, and the cutoff annular source need a comparison argument.
- Initial iid orthogonality supplies no evolved interacting-law cubic,
  contraction, bracket, or martingale bound, and no singular generator
  passage.

There is a concrete additional check on the first item. If \(A_0\ne0\)
and \(\tau>0\), (R2.10) implies that the squared angular leading term
has positive integral and radial integral proportional to
\[
 \int_0^\epsilon r^{d-5}\,dr.
 \tag{R6.1}
\]
The bounded and \(O(r^s)\) remainders cannot cancel this term.
Thus the punctured Laplacian is not locally \(L^2\) in dimensions
\(2,3,4\). In \(d=2\), its absolute \(L^1\) integral also diverges,
as \(\int_0^\epsilon r^{-1}dr\).
Multiplication by any strictly positive diffusivity does not make these
unregularized norms finite. This verifies the need for the excluded
regularization or solution argument. It does not prove nonexistence of
a full corrector, failure of an endpoint comparison, or a singular
fluctuation obstruction.

On a domain where the full local and nonlocal expressions are defined,
the submitted residual (8.1) is the product-rule identity obtained by
adding the omitted operators to (R4.1) and adding the actual source.
It is conditional bookkeeping, not a proof that the response integrals
exist at this regularity or that the identity passes across collisions.
No such existence or passage is claimed in THM-017.

The sufficient comparison (8.2) is correct as an implication, provided
the difference is a deterministic symmetric \(L^2(\mu^2)\) kernel under
the same iid preparation: (R4.4) bounds its scaled \(L^2\) statistic by
at most \(2^{-1/2}\sqrt{b_N/N}\) times its kernel norm.
Together with the proved diagnostic endpoint, this would transfer
endpoint negligibility. The submitted report does not prove that
kernel comparison, and this review leaves it open. It would still not
supply the evolved-law and martingale estimates.

No conclusion about positive-diffusivity dynamics, a microscopic critical
law, the logarithmic model, or finite truncation of the corrector hierarchy
is justified by this theorem. The broad campaign gate remains unchanged.

## 7. Integrity, verification, and handoff

Verified supplied hashes:

| Input | SHA-256 |
|---|---|
| TASK-027 | 469fa0e914ba596e84184e7820af75e1c73c9516f2b8e6d95896adac073db451 |
| THM-017 card | 2c95e74ea8874e8d624d23a8ce2dfa9dfdca4eda9d796c9e403dda5277811c79 |
| Complete TASK-025 proof | 9cfe0d7b7fb970ce74e14f4d25b784437debeefac3e9d8a8e1ab47152514ef5d |

The sealed TASK-024 reconstruction remains
9eb7e54ab0fa6e38ef226cd2d815d618d2b421718ed0e1c59bb07dc27ae79e6f,
with support program and output hashes respectively
e399f468435f6027e7ecc6ed52ae25217d2a21da07fe87777748f5a39ff603f8 and
a64a00af9c1dd21bc3d9d258cec95a7c0ec4505e2e61dc416f97e5fb42bb482f.
No supplied input or previously issued output was edited.

The command

    python3 DISCOVERY_CODE/check_round003_pair_transport_review_exact.py > DISCOVERY_CODE/round003_pair_transport_review_exact_output.json

passed **749 exact rational/integer checks**. These include direct PDE
substitutions at rational-power characteristic endpoints, \(N=2,3,7\),
the first three far-expansion coefficients, core and endpoint powers,
angular fourth-moment contractions, the nonzero-mean iid decomposition,
the exact \(N=2\) equality, the single density factor, and a positive
temperature sequence alternating between growth and decay. The program
uses no floating-point approximation or sampling. These checks support
the written independent review; none replaces its analytic inequalities,
characteristic uniqueness argument, or regularity analysis.

The supplied-input manifest was reverified, and all TASK-024 seal hashes
were rechecked unchanged. The campaign verifier

    python3 scripts/verify_campaign.py

passed. Both git diff --check and git diff --exit-code passed.
A direct scan of the three new deliverables found valid UTF-8, final
newlines, and no control characters or trailing whitespace; the review's
display-math delimiters balance. No verification command failed.

The only new deliverables are this review and its independent exact
coefficient-check program/output. No canonical ledger, manuscript, source,
TeX file, or unrelated report was changed. There was no commit, push,
dependency installation, or child worker. Root owns the final canonical
status and any proposed clarification; the issued audit bytes will not
be altered after handoff.
