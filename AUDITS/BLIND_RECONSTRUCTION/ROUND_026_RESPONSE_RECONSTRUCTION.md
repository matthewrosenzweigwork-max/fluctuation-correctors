# AUD071 / TASK112 — whole THM050 isolated reconstruction

Issued 2026-09-18 UTC. Evidence identifier: `ROUND_026_RESPONSE_BLIND_ARTIFACTS_20260918_092359_UTC`.

**Whole verdict: reconstructed, with no failed clause or counterexample found.** Clauses A, B, and C follow together under the frozen conventions. This is one isolated reconstruction for comparison by the root; it neither promotes the campaign gate by itself nor supplies an independent hostile review of this reconstruction. The actual critical response/source target and Haar second-gradient control remain open.

| Clause | Verdict | Load-bearing argument |
|---|---|---|
| A: conditional decomposition, true cutoff brackets and numerical Dirichlet-cost limit | Reconstructed | Conditional orthogonality; smooth backward martingale; same-noise fixed-N heat convergence of bounded observables |
| B: uniform angular limsup for the full periodic process | Reconstructed | A stopped relative/slow-coordinate system, moment estimates uniform over the complete frozen compact set, and a uniform exit bound |
| C: Haar W1,4 nonmembership at every sufficiently small positive time | Reconstructed | A cap-average gap on a positive-volume set of slow coordinates and logarithmically divergent transverse energy |
| C: actual heat-cutoff fourth-gradient liminf is infinite | Reconstructed | Pointwise convergence of the actual heat semigroups, cap averaging, and Fatou on fixed annuli |

No statement about a directional collision entrance law, singular-gradient formula in A, uniformity in N, or critical source decay is needed. In particular the proof of C does not substitute a deterministic radial model, an isolated center slice, or an arbitrary regularization of the limiting function for the claimed objects.

## 1. Frozen assertion, negation, and exposure

The eight exact input byte strings are reproduced under `inputs/` in the evidence packet. Their hashes were checked successfully against the supplied manifest before mathematical reading. The input manifest and verification result are included. The supplied worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r026-response-blind`; the assigned branch is `codex/hocf-r026-response-blind` and the provisioned base is `06bf56dae256085646228aa28159210b567bf409`. These last two identities are supplied provenance, not a claim based on reading Git history. No Git history, canonical state, other worktree, memory file, current constructor report/code/results/exposure, or other current audit was read.

The assertion being reconstructed is the entire version-locked THM050 card, not a suggested proof. In particular:

* A quantifies over every finite integer N at least two, positive finite diffusivity, integer Fourier mode including zero, and finite nonnegative terminal time; the expectation uses original iid Haar initial data independent of all drivers. Its heat limit occurs at fixed N.
* B quantifies over every admitted compact positive-volume slow-coordinate set and chosen separated neighborhoods. There are finite constants and a positive time interval, depending on these fixed data, on which the stated uniform angular limsup bound holds at every positive time. The radial limsup is taken after fixing time. No existence of a directional limit is required.
* C quantifies over every finite N and positive finite diffusivity. For the stated real first mode there is a positive interval such that both conclusions hold at every positive time in that interval. The gradient is the full configuration gradient and the integration measure is product Haar.

The exact negation is an admitted datum violating any included clause. For B it is existence of fixed admitted data such that every proposed finite constant and positive time interval fails at some positive time in the interval. For C it is existence of an admitted N and diffusivity such that every positive proposed interval contains a time when at least one of its two conclusions fails. For A it is failure of an identity, included integrability, bracket, cutoff limit, nonnegativity, sequence equivalence, or the explicit constant-mode convention. Failure of an attempted proof, or lack of an N-uniform estimate, does not establish this negation.

The full read/exposure record is `SOURCE_EXPOSURE.md` in the packet. The allowed historical reports declare self-check or proved-candidate status; those labels are not imported certification. The source mechanisms actually used are reconstructed below. Historical references from those reports to other reports, source PDFs, code, or audit packets were not followed. No outside literature theorem or remembered source theorem is a premise.

The project-wide general instruction to inspect other administrative/state documents is displaced here by the task-specific eight-file isolation rule. The assignment forbids commits, source/state editing, children, dependencies, and remote actions; none was performed. Only the assigned reconstruction and its uniquely named evidence artifacts were created.

## 2. Kernel and actual process: reconstruction of the used source mechanisms

All torus volumes are one and characters are \(e_k(x)=e^{2\pi i k\cdot x}\). Put \(c=4\pi^2\). In dimension four the specified Fourier kernel has the direct heat representation

\[
 g(x)=c\int_0^\infty(p_v(x)-1)\,dv,
 \qquad p_v(x)=\sum_{n\in\mathbb Z^4}(4\pi v)^{-2}
                  e^{-|x+n|^2/(4v)}.                                      \tag{2.1}
\]

The integral converges in L1: on small times the L1 norm of the parenthesis is at most two, and on large times its nonzero Fourier series decays exponentially. Integrating its kth nonzero coefficient gives \(c/(4\pi^2|k|^2)=|k|^{-2}\); its mean is zero. For the n=0 Euclidean summand, substitution \(w=|x|^2/(4v)\) gives

\[
 c\int_0^\infty(4\pi v)^{-2}e^{-|x|^2/(4v)}\,dv=|x|^{-2}.                  \tag{2.2}
\]

On a small coordinate ball, subtract (2.2) from (2.1). For small v, all remaining lattice summands and their spatial derivatives are bounded by a power of v inverse times \(e^{-a/v}\); the constant subtraction is integrable. For large v, the torus derivatives decay exponentially and the Euclidean derivatives are integrable powers. Differentiation under these integrals proves

\[
 g(y)=|y|^{-2}+h(y),\quad h\text{ smooth and even},\qquad
 K(y)=2y/|y|^4+K_0(y),\quad |K_0(y)|\le L|y|.                              \tag{2.3}
\]

Evenness gives \(\nabla h(0)=0\). Both g and K are integrable. Fourier differentiation, or integration of the heat equation in (2.1) against a smooth test, gives

\[
 \operatorname{div}K=c(\delta_0-dx),\qquad \Delta g=c\quad\text{off zero}.  \tag{2.4}
\]

This also checks the positive atom and the negative constant compensation. No atom is evaluated on a trajectory.

Here is the part of the older particle-realization argument needed in this audit. On the collision-free configuration space let

\[
 H(x)=\frac1N\sum_{i<j}g(x_i-x_j),\qquad
 E(x)=H(x)-\frac{N-1}{2}g_*,\quad g_*:=\inf_{y\ne0}g(y)>-\infty.           \tag{2.5}
\]

The expression E is a sum of nonnegative shifted pair terms, divided by N. Consequently its sublevels are compact and avoid every partial collision, including simultaneous clusters. The full drift is \(B=-\nabla H\), and differentiation of both coordinates of each unordered pair gives

\[
 \Delta_{4N}H=(N-1)c,
 \quad (B\cdot\nabla+\nu\Delta)E=-|B|^2+\nu(N-1)c.                      \tag{2.6}
\]

In particular the complete force square retains all cross terms; there is no comparison with the sum of individual pair-force squares.

Cut K smoothly near zero, keeping it unchanged on nested collision-excluded compact sets. At each such cutoff the additive-noise equation is a globally Lipschitz integral equation after subtracting the driving Brownian path; convergent Picard iteration constructs its measurable, nonanticipating solution. Local uniqueness patches these solutions up to the maximal collision time. Only collision can prevent continuation, because the torus is compact and the drift is smooth and bounded away from collisions. Stop instead on exiting \(E<R\). Stopped smooth Itô calculus yields

\[
 E(X_{t\wedge\sigma_R})+\int_0^{t\wedge\sigma_R}|B(X_s)|^2ds
 =E(x)+\nu(N-1)c(t\wedge\sigma_R)
   +\sqrt{2\nu}\int_0^{t\wedge\sigma_R}\nabla H(X_s)\cdot dW_s.           \tag{2.7}
\]

All stopped coefficients are bounded. The martingale has zero mean and the left side is nonnegative. Thus

\[
 \mathbb P_x(\sigma_R\le T)
 \le \min\{1,[E(x)+\nu(N-1)cT]/R\}.                                     \tag{2.8}
\]

Exhaustion by these compact sublevels and then R tending to infinity prove noncollision and global uniqueness at every collision-free deterministic start, almost surely. The stopped Picard maps and their countable limits are jointly measurable in starting point, time, and driving path. Restart at a deterministic time and independence of subsequent Brownian increments give the Markov semigroup. State-dependent exceptional events have probability zero at every state and hence also after integrating the jointly measurable indicator. No simultaneous good event for every starting state is asserted. Every individual global path on a finite time interval has a positive minimum pair separation by continuity and compactness.

For the specified heat regularization, \(K_\epsilon=p_\epsilon*K\) converges to K in C1 on every compact set away from zero. To check this, decompose K into a smooth field agreeing with it near the compact set and an L1 field supported a positive distance away. The first part converges with its derivative by the heat approximate identity; Gaussian derivative bounds make the second part tend to zero exponentially there. Couple the heat and singular equations with the same initial state and Brownian paths. On a singular path with positive minimum separation, their noises cancel in the difference equation. Stop their separation before it reaches a small fixed fraction of that pathwise minimum. A uniform local Lipschitz bound and Gronwall bound the difference by

\[
 T\frac{N-1}{N}\sup_{\mathrm{dist}(y,0)\ge\eta/2}|K_\epsilon(y)-K(y)|
    e^{L T},                                                            \tag{2.9}
\]

which tends to zero and therefore prevents that stop for all sufficiently small epsilon. This proves the full-parameter, almost-sure heat convergence on the finite interval at each fixed collision-free start. The constants in (2.9) may depend on the path. Integrating the joint measurable assertion proves the same convergence for independent Haar initial data. For every continuous bounded configuration observable G,

\[
 P_t^{N,\epsilon}G(x)\longrightarrow P_t^NG(x)
 \quad\text{for every collision-free }x.                                \tag{2.10}
\]

The collision set is Haar null. Bounded convergence therefore also gives convergence in every finite Haar Lp norm for such G. No claim about singular derivatives is made here. The older bounded-density theorem is not needed anywhere below; in particular evolved Haar stationarity is never assumed.

## 3. Clause A: exact conditional identities and actual cutoff costs

Use the frozen \(F=N^{-1}\sum_i e_k(x_i)\), so \(|F|\le1\), and retain the displayed \(a=c+\nu c|k|^2\), \(A=e^{-aT}\) for every k, including zero. Under the independent Haar initial law set

\[
 Z=F(X_T)-P_T^NF(X_0),\qquad Y=P_T^NF(X_0)-AF(X_0).
\]

The Markov construction above gives \(\mathbb E[Z\mid X_0]=0\). Both variables are bounded. Since Y is measurable with respect to \(X_0\),
\(\mathbb E[Z\overline Y]=0\). Expanding the absolute square proves exactly

\[
 N\mathbb E|F(X_T)-AF(X_0)|^2
 =N\|P_T^NF-AF\|_{L^2(dx^N)}^2+N\mathbb E|Z|^2.                          \tag{3.1}
\]

Every term is nonnegative and at most a finite constant times N. The Haar norm is justified by the original initial law, not by a stationarity claim. Complex conjugation in this calculation is essential.

For fixed epsilon, the smooth finite-dimensional flow and its differentiated integral equations show that \(u_s^\epsilon=P_{T-s}^{N,\epsilon}F\) is smooth in space with bounded derivatives on the finite horizon. Differentiated flow equations have bounded coefficients for these fixed parameters. The semigroup identity, followed by the short-time smooth Itô formula, gives \(\partial_su_s^\epsilon+L_{N,\epsilon}u_s^\epsilon=0\). Applying that same formula along the heat process cancels the drift and gives

\[
 d[u_s^\epsilon(X_s^\epsilon)]
   =\sqrt{2\nu}\sum_i\nabla_i u_s^\epsilon(X_s^\epsilon)\cdot dW_i(s).
                                                                            \tag{3.2}
\]

Square integrability follows from the fixed-cutoff bounded gradients. Multiplying the actual Brownian coefficients, with independent labels and conjugating the second complex integrand, gives

\[
 d\langle u^\epsilon(X^\epsilon),\overline{u^\epsilon(X^\epsilon)}\rangle_s
   =2\nu\sum_i|\nabla_i u_s^\epsilon(X_s^\epsilon)|^2ds,                  \tag{3.3}
\]

\[
 d\langle u^\epsilon(X^\epsilon),\overline{M_k^\epsilon}\rangle_s
   =\frac{2\nu}{N}\sum_i\nabla_i u_s^\epsilon(X_s^\epsilon)
                  \cdot\overline{\nabla e_k(X_i^\epsilon(s))}\,ds.        \tag{3.4}
\]

For the one-body stochastic integral using the frozen backward-weighted test \(e^{-a(T-s)}e_k\), (3.4) has the additional real factor \(e^{-a(T-s)}\). This is an identity about that specified deterministic weighting. It does not identify that one-body test with the true N-particle backward function in (3.2). Also, at a fixed heat cutoff the homogeneous *linearized* response eigenvalue for a nonzero mode is \(-c e^{-\epsilon c|k|^2}\), so the cutoff-linearized backward test, if separately defined, would instead use \(a_\epsilon=c e^{-\epsilon c|k|^2}+\nu c|k|^2\). This distinction prevents importing a false cutoff damping assertion into the frozen comparison. The explicit constant-mode convention likewise is an artificial comparison, not a backward eigenfunction assertion.

Integrating (3.2) and using the real and imaginary Itô isometries gives the exact fixed-cutoff number

\[
 J_N^\epsilon:=N\mathbb E|F(X_T^\epsilon)-P_T^{N,\epsilon}F(X_0)|^2
 =2\nu N\int_0^T\mathbb E\sum_i
  |\nabla_iP_{T-s}^{N,\epsilon}F(X_s^\epsilon)|^2ds.                       \tag{3.5}
\]

Both terminal terms on the left converge under the same-noise construction: the first almost surely, the second at every collision-free initial state by (2.10). They are bounded by one. Bounded convergence on the product probability space proves \(J_N^\epsilon\to J_N\), exactly the numerical limit required in A. Thus (3.5) does not require convergence of gradients, a singular Dirichlet identity, or an interchange of heat and N limits.

For any sequence of the prescribed data, nonnegativity and (3.1) imply that D tends to zero if and only if C and J both tend to zero. This elementary equivalence applies in particular to the critical sequence in the card; it proves neither convergence. At zero mode F is identically one, so J is zero and \(C=N(1-e^{-cT})^2\). At T=0 all three terms are zero. These check every endpoint convention in A.

## 4. Local coordinates for the full process

Fix the data of B. Write \(y=x_1-x_2\), \(z=(x_1+x_2)/2\), and \(q=(z,x_3,\ldots,x_N)\) in the declared local lifts. Since Q is compact within the separated coordinate domain, choose a tube with a fixed positive margin from Q to its slow-coordinate boundary and a sufficiently small pair radius R, with \(R\le1\). Within the closure of this tube all pairs except (1,2) have a fixed positive separation. If necessary choose a smaller inner tube and use the declared larger neighborhoods for its closure; compactness supplies the margins uniformly. All constants below may depend on these choices and on N, nu, and k.

Let \(\tau\) be the first exit from the tube, either through \(|y|=R\) or the slow boundary. The two Brownian combinations \((W_1-W_2)/\sqrt2\) and \((W_1+W_2)/\sqrt2\) are independent standard four-dimensional Brownian motions, as follows by multiplying their covariance matrices; all remaining drivers stay independent. Before tau the *actual* equations read

\[
 dy=\alpha\frac{y}{|y|^4}dt+b(q,y)dt+2\sqrt\nu\,dB,
 \quad\alpha=4/N,\quad |b(q,y)|\le L|y|,                                \tag{4.1}
\]

\[
 dq=b_q(q,y)dt+\Sigma_q,dB_q,
 \quad |b_q|\le L,
 \quad\Sigma_q\Sigma_q^T=\operatorname{diag}(\nu I_4,2\nu I_{4(N-2)}).
                                                                            \tag{4.2}
\]

Indeed the internal pair appears twice in the relative drift. Formula (2.3) supplies its bounded linear remainder. Every other contribution to that relative drift is
\(N^{-1}[K(z+y/2-x_j)-K(z-y/2-x_j)]\), which is O(|y|) by a derivative bound on the separated set. The internal force cancels from the z drift. Each force in the other coordinates is bounded on this same set. Thus every label is included in (4.1)--(4.2); no two-particle replacement has been made. For N=2 only the center remains among the slow coordinates.

All subsequent barred quantities mean evaluation at \(t\wedge\tau\). The actual singular process is already defined for every r>0 and has no collisions. Smooth Itô calculations below can first be stopped also at \(|y|=1/m\); the proved noncollision exhausts these extra stops. The bounds below justify every expectation or martingale passage where an inverse power remains.

## 5. Uniform stopped moments, exit probabilities, and angular control

Set \(\rho=|y|\), \(U=\rho^4\), and \(v=4\alpha=16/N\). Direct differentiation in four dimensions gives, before stopping,

\[
 dU=[v+48\nu\rho^2+4\rho^2y\cdot b]dt
             +8\sqrt\nu\,\rho^2y\cdot dB,
 \qquad d\langle M_U\rangle=64\nu\rho^6dt,                               \tag{5.1}
\]

\[
 d\rho^2=[2\alpha\rho^{-2}+16\nu+2y\cdot b]dt
             +4\sqrt\nu\,y\cdot dB,                                    \tag{5.2}
\]

\[
 L\rho^6=6\alpha\rho^2+96\nu\rho^4+6\rho^4y\cdot b.                    \tag{5.3}
\]

Here the relative diffusion generator is \(2\nu\Delta_y\), not \(\nu\Delta_y\). For r in a fixed sufficiently small interval and \(0<t\le1\), uniformly over the frozen q and theta,

\[
 \mathbb E\bar\rho_t^4\le C(r^4+t),\qquad
 \mathbb E\bar\rho_t^6\le C(r^6+t^{3/2}),\qquad
 \mathbb E\bar\rho_t^2\le C(r^2+\sqrt t).                                \tag{5.4}
\]

For completeness, the first inequality follows from (5.1), \(|b|\le L\rho\), \(\rho^2\le1+\rho^4\), and the integral Gronwall inequality; stopped fourth moments have bounded coefficients. The third then follows by Cauchy--Schwarz. Integrating (5.3) and applying Gronwall bounds the second by a constant times
\(r^6+r^2t+r^4t+t^{3/2}+t^2\). Young's elementary product inequality, with r,t at most one, bounds this by \(C(r^6+t^{3/2})\). Thus no higher-moment claim is presumed in deriving (5.4).

Slow exit is controlled from (4.2). Its stopped drift displacement is at most Lt and its martingale part has second moment at most Ct. The elementary martingale maximal estimate gives
\(\mathbb E\sup_{s\le t}|\bar q_s-q|^2\le C(t+t^2)\). One proof of the estimate used here is to apply optional stopping to a scalar square-integrable martingale at its first threshold, obtain \(a\mathbb P(M^*>a)\le\mathbb E[|M_t|1_{M^*>a}]\), integrate in a, and use Cauchy--Schwarz; it yields \(\mathbb E(M^*)^2\le4\mathbb E|M_t|^2\). Apply it componentwise to the stopped Brownian integrals. The fixed boundary margin therefore bounds the probability of slow exit by Ct. On a radial exit occurring first, \(\bar\rho_t^4=R^4\). The first inequality in (5.4) and nonnegativity bound that event by \(C(r^4+t)\). Consequently

\[
 \mathbb P_{q,r\theta}(\tau\le t)\le C(r^4+t).                            \tag{5.5}
\]

In particular no energy bound that diverges with the initial collision distance is used to estimate these local exits.

The martingale in (5.1) is square integrable, and its isometry together with (5.4) gives

\[
 \mathbb E|M_U(t\wedge\tau)|
 \le C\Big(\int_0^t\mathbb E\bar\rho_s^6ds\Big)^{1/2}
 \le C(r^3\sqrt t+t^{5/4}).                                               \tag{5.6}
\]

The difference between the constant drift accumulated before the stop and vt is at most \(vt1_{\tau<t}\). From (5.1), (5.4)--(5.6),

\[
 \mathbb E|\bar U_t-r^4-vt|
 \le C\{t(r^4+t)+r^2t+t^{3/2}+r^4t+t^2+r^3\sqrt t+t^{5/4}\}.             \tag{5.7}
\]

Using \(|\sqrt a-\sqrt b|\le|a-b|/\sqrt b\), then letting r decrease to zero at fixed positive t, proves

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
       \mathbb E|\bar\rho_t^2-\sqrt{vt}|\le Ct^{3/4}.                    \tag{5.8}
\]

The same constants work for every t in the chosen interval. There is no interchange of the two limits.

The inverse-square occupation needed for the angle comes from (5.2), with its positive singular drift. Expectation of the stopped martingale is zero because its coefficient is bounded. Since \(2y\cdot b\ge-2L\rho^2\),

\[
 2\alpha\mathbb E\int_0^{t\wedge\tau}\rho_s^{-2}ds
 \le\mathbb E\bar\rho_t^2-r^2+2L\int_0^t\mathbb E\bar\rho_s^2ds
 \le C(r^2+\sqrt t).                                                     \tag{5.9}
\]

To justify this if an inverse cutoff is present, apply the identity first with that cutoff, use the uniform bounded radial moments and Fatou for the nonnegative occupation integral, and then pass the bounded-coefficient radial martingale by isometry. Thus (5.9) establishes integrability before it is used in the angular martingale.

For \(\zeta=y/|y|\), direct differentiation gives

\[
 d\zeta=\left[(I-\zeta\zeta^T)b/\rho-6\nu\zeta/\rho^2\right]dt
       +(2\sqrt\nu/\rho)(I-\zeta\zeta^T)dB.                            \tag{5.10}
\]

The radial singular drift drops out exactly. Formula (5.9) makes the stopped angular stochastic integral square integrable. Since \(\zeta_0=\theta\), the identity \(|\zeta-\theta|^2=2-2\theta\cdot\zeta\), followed by expectation in (5.10), gives

\[
 \mathbb E|\bar\zeta_t-\theta|^2
 \le 2Lt+12\nu\mathbb E\int_0^{t\wedge\tau}\rho_s^{-2}ds
 \le C(t+r^2+\sqrt t).                                                   \tag{5.11}
\]

Use \(|\zeta\zeta^T-\theta\theta^T|\le2|\zeta-\theta|\), (5.4), (5.8), and Cauchy--Schwarz. For each fixed k,

\[
 \limsup_{r\downarrow0}\sup_{q,\theta}
 \mathbb E\left|(k\cdot\bar y_t)^2-\sqrt{vt}(k\cdot\theta)^2\right|
 \le Ct^{3/4}.                                                         \tag{5.12}
\]

This proves the needed angular estimate for the actual stochastic dynamics. It neither asserts convergence of \(\bar\zeta\) as r decreases nor selects an entrance law.

## 6. Clause B: expectation of the complete Fourier observable

The exact pair contribution in these coordinates is

\[
 \frac1N(e_k(x_1)+e_k(x_2))
       =\frac2N e_k(z)\cos(\pi k\cdot y).
\]

Taylor's formula with bounded fourth derivative therefore yields throughout the closed tube

\[
 F(q,y)=H_k(q)-\frac{\pi^2}{N}e_k(z)(k\cdot y)^2+O_{N,k}(|y|^4).          \tag{6.1}
\]

The function H is a smooth function of *all* slow coordinates. Smooth stopped Itô calculus in (4.2) gives
\(|\mathbb EH_k(\bar q_t)-H_k(q)|\le Ct\): the drift, covariance, and required derivatives are bounded. This uses cancellation of the Brownian linear term in expectation; an absolute displacement estimate of order square root t would be insufficient here. Also

\[
 \mathbb E\big[|e_k(\bar z_t)-e_k(z)|\,|\bar y_t|^2\big]
 \le C(\mathbb E|\bar z_t-z|^2)^{1/2}
          (\mathbb E|\bar y_t|^4)^{1/2}
 \le C\sqrt t(r^2+\sqrt t).                                              \tag{6.2}
\]

The Taylor remainder has mean at most \(C(r^4+t)\). Finally the actual and stopped terminal F agree on \(\tau>t\), and both have modulus at most one. By (5.5) their expectations differ by at most \(C(r^4+t)\). Combining (5.12), (6.1), and (6.2) proves

\[
 \limsup_{r\downarrow0}\sup_{q\in Q,\theta\in S^3}
 \left|P_t^NF(q,r\theta)-H_k(q)
       +\frac{\pi^2}{N}\sqrt{vt}\,e_k(z)(k\cdot\theta)^2\right|
 \le Ct^{3/4}.                                                         \tag{6.3}
\]

Because \(v=16/N\), the displayed coefficient is exactly \(4\pi^2N^{-3/2}\sqrt t\). All constants above were independent of q, theta, and sufficiently small r, so the supremum preceding the radial limsup is legitimate. The inequalities hold with the same C for every positive time up to a fixed t0, reduced if needed to at most one. This is precisely B for every permitted compact set and every label count. For k=0 the actual observable and H are both one and the angular term is zero.

## 7. The elementary angular inequality and its Sobolev use

Here are the analytic details needed to turn B into C. Let

\[
 A_S=\{\theta\in S^3:\theta_1^2\ge3/4\},\qquad
 B_S=\{\theta\in S^3:\theta_1^2\le1/4\}.
\]

Both have positive surface measure. For a smooth real v on the sphere write \(v_A,v_B\) for their respective surface averages. There is a fixed finite constant \(C_S\) such that

\[
 |v_A-v_B|^4\le C_S\int_{S^3}|\nabla_Sv|^4dS.                            \tag{7.1}
\]

One direct construction of (7.1), avoiding a spectral or imported embedding theorem, is as follows. On a rectangular box the fundamental theorem of calculus along coordinate segments, telescoping over coordinates, and Hölder give the L4 estimate of the distance to the box mean by a constant times the fourth-gradient integral. Choose finitely many bounded-distortion graph-coordinate patches on the sphere, with smaller box patches covering it, and a connected overlap graph whose edge overlaps have positive measure. Such a cover is obtained by small graph patches along finitely many paths connecting an initial finite cover. The box inequality bounds deviations from each local mean. On an overlap, the difference of the two means is bounded by the two deviations divided by that overlap's positive measure, using the fourth-power triangle inequality. Following the finite overlap graph bounds all local means relative to one reference mean. Adding the local bounds gives
\(\int|v-\bar v|^4\le C\int|\nabla_Sv|^4\). Jensen on the two fixed positive-measure caps proves (7.1). The bounds of the graph Jacobians, inverse Jacobians, and overlaps are fixed finite constants. The same argument extends by local smooth approximation to sphere W1,4 functions.

The other fact used is slicing, in its explicit local form. If u belongs to W1,4 on a configuration coordinate domain, then its restriction to almost every slow-coordinate slice and almost every sphere of radius r in any annulus has angular weak gradient, and that gradient equals the tangential part of r times its y weak gradient. To check this, multiply u by a smooth cutoff supported in a slightly larger coordinate domain and mollify. The defining weak derivatives of the convolution converge in L4, by translation continuity of L4 functions. In smooth sphere charts and on each annulus bounded away from r=0, the coordinate map and its inverse have bounded derivatives and Jacobians. The chain rule for the mollifications then passes to weak derivatives by integration against compactly supported tests. Fubini followed by a subsequence with summable L4 approximation errors gives the asserted restrictions and derivative identity for almost every q and r. Exhaust over a countable family of annuli. This proves exactly the slicing assertion needed here, including representative independence; no trace at y=0 is invoked.

For a smooth function, or these almost-everywhere Sobolev slices,

\[
 |\nabla_yu(q,r\theta)|\ge r^{-1}|\nabla_Su(q,r\theta)|.                  \tag{7.2}
\]

The linear coordinate change has absolute Jacobian one. Moreover

\[
 |\nabla_{x_1}u|^2+|\nabla_{x_2}u|^2
       =\tfrac12|\nabla_zu|^2+2|\nabla_yu|^2,
 \quad |\nabla_xu|^4\ge4|\nabla_yu|^4.                                  \tag{7.3}
\]

Combining (7.1)--(7.3) over any product subset of the coordinate tube yields

\[
 \int |\nabla_xu|^4dx
 \ge \frac4{C_S}\int_Q\int_\rho^R
       |u_A(q,r)-u_B(q,r)|^4\frac{dr}{r}\,dq.                            \tag{7.4}
\]

The radial weight is exactly r cubed from four-dimensional volume times r to the minus fourth from the angular gradient. This codimension-four logarithm does not imply a second-gradient obstruction.

## 8. Clause C: positive-volume obstruction and actual heat divergence

Take k equal to the first coordinate vector and f equal to the real part of F. For any finite N select distinct points \(z_*,x_{3,*},\ldots,x_{N,*}\), with first coordinate of \(z_*\) equal to zero. Finite many distinct points always exist on the torus. Small closed product boxes about them give a compact positive-volume Q, separated neighborhoods as in B, and
\(\cos(2\pi z_1)\ge1/2\) throughout Q. For N=2 choose just a center box. Put

\[
 a_0=2\pi^2N^{-3/2}>0,\quad
 a(q)=4\pi^2N^{-3/2}\cos(2\pi z_1)\ge a_0,
 \quad h(q)=\operatorname{Re}H_k(q).
\]

Writing \(u=P_t^Nf\), clause B gives a radial limsup bound for
\(u(q,r\theta)-h(q)+a(q)\theta_1^2\sqrt t\). Reduce the time interval so that \(Ct^{1/4}\le a_0/16\) throughout it. At each fixed positive time in this interval, the definition of limsup supplies some \(r_t>0\) such that, for every \(0<r<r_t\), every q in Q, and every theta,

\[
 |u(q,r\theta)-h(q)+a(q)\theta_1^2\sqrt t|
       \le a_0\sqrt t/8.                                                \tag{8.1}
\]

The extra factor of two allows the positive slack required when passing from a limsup to an eventual bound. Thus any theta in B_S and any phi in A_S satisfy

\[
 u(q,r\theta)-u(q,r\phi)
 \ge a_0\sqrt t(3/4-1/4)-2a_0\sqrt t/8
 =:\delta_t=a_0\sqrt t/4>0.                                             \tag{8.2}
\]

Consequently the corresponding cap averages differ by at least delta_t, at every q and every r in that interval. If u were a global Haar W1,4 function, the slicing justification in section 7 and (7.4), applied on each fixed annulus, would give

\[
 \int_{(\mathbb T^4)^N}|\nabla_xu|^4dx
 \ge \frac4{C_S}|Q|\delta_t^4\log(r_t/\rho)
 \quad\text{for every }0<\rho<r_t.                                     \tag{8.3}
\]

Letting rho decrease to zero contradicts finite fourth-gradient integral. Equalities of a Sobolev representative with the semigroup representative hold for almost every q,r,theta by the polar change of variables and Fubini; this is enough for the cap averages and (8.3). The arbitrary values on the collision set do not matter. The strictly positive slow volume in (8.3) is essential and has been constructed explicitly.

For the second conclusion take the *actual* functions \(u_\epsilon=P_t^{N,\epsilon}f\). These are smooth at each cutoff, bounded by one, and converge to u at every collision-free configuration by (2.10). For each q in Q and fixed positive r less than r_t, dominated convergence on the two caps shows convergence of their cap averages. Apply (7.4) to u_epsilon on the fixed annulus and then Fatou to its nonnegative right side. Equations (8.1)--(8.2) give

\[
 \liminf_{\epsilon\downarrow0}
       \int_{(\mathbb T^4)^N}|\nabla_xP_t^{N,\epsilon}f|^4dx
 \ge \frac4{C_S}|Q|\delta_t^4\log(r_t/\rho).                             \tag{8.4}
\]

Since rho can be arbitrarily small after this limit, the liminf is positive infinity. Fatou can formally be applied to any sequence realizing the liminf, so (8.4) is the full-parameter liminf assertion. This route does not presume weak convergence of cutoff gradients or identify them with a singular derivative.

The choices of Q, a0, the B constant, and the reduced t0 depend on N and nu but are fixed before choosing the time in that interval. Equations (8.1)--(8.4) hold at *every* such positive time, although r_t may depend on it. This verifies the universal-in-time conclusion in C. A finite cutoff-uniform global C1 bound would bound the fourth-gradient integral on the volume-one configuration torus; a finite cutoff-uniform Haar fourth-gradient bound directly contradicts (8.4). No uniformity in N is involved.

## 9. Adversarial checks, diagnostics, and precise limits

The reconstruction separately challenged: the coefficient-one kernel normalization; the pair drift's doubled coefficient; relative versus center Brownian covariance; the transverse derivatives in the radial generator; the stopped constant drift's missing elapsed time; inverse-square occupation before angular stochastic integration; Brownian cancellation in the slow observable; uniformity over all centers, directions, and other labels; slack in the radial limsup; positive slow volume; Sobolev representatives and sphere slicing; the actual heat semigroup instead of smoothing u; the order of limits; complex conjugation and the one-body backward factor; and the explicitly artificial zero-mode comparison. Each is addressed at the displayed line where it is needed.

Fresh standard-library exact diagnostics and mutation controls are in `code/diagnostic.py`; execution results are in `results/diagnostic.json`. They independently differentiate the radial polynomials and angular coordinates, check covariance/bracket coefficients and a nontrivial conditional-variance example, and test the codimension and angular energy. Deliberate mutants include missing pair/noise factors, missing complex conjugation, missing backward weighting, isotropic replacement of the angular profile, and replacement of positive slow volume by one slice. Their residuals must be nonzero. These are supporting algebraic diagnostics, not simulations of the singular process or a computational substitute for sections 2--8. No probability estimate is inferred from their numerical output.

The packet records actual commands, results, read/exposure history, exact input copies, all created-file hashes, regular-member inventory, and a portable read-only verifier. It is sealed only after execution and inspection. There were no baseline diagnostic failures at issuance; deliberate mutation failures are successful negative controls. The verifier re-runs the fresh diagnostic in memory and verifies hashes and archive member safety without extracting or writing files.

No reference outside the eight inputs is needed or presented as verified. This report is a Markdown proof; no TeX source was changed and no build of an unrelated manuscript was run. The final handoff contains no mathematical LaTeX. No scientific scope or centering was changed. The first remaining campaign question is still actual quantitative second-response/critical-source control, which this fixed-N fourth-gradient obstruction neither proves nor disproves. Root comparison of this *whole* isolated reconstruction with the withheld constructor and separate hostile audit remains necessary before any gate promotion.
