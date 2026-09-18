# Round 028 — the complete marked first-collision flux

TASK121. Ordinary Astra Max construction and falsification, 2026-09-18 UTC. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r028-collision-flux`; assigned branch `codex/hocf-r028-collision-flux`, supplied base `ef438b612f732d21af1fa1756dd7559ef63c6d61`. The branch/base are task-card metadata, not a new inspection of Git history.

**Verdict: the entire frozen THM053(A)–(B) is proved here as a PROVED_CANDIDATE / SELF_CHECKED construction. No independent audit or canonical promotion is claimed.** The actual killed attractive process, its first-power lifetime action, its terminal limit, the full joint exit measure, unique binary mark, and all stated independence conclusions are included. The proof identifies the exit measure before excluding multiple collisions. THM046/PO033 and the original critical decay problem remain open.

The twelve permitted inputs passed SHA-256 preflight and were read in full. Exact copies, exposure/read/history records, failed routes, obligation coverage, exact diagnostics with detected mutations, a complete payload inventory and a portable read-only verifier accompany this memorandum in `ROUND_028_COLLISION_FLUX_ARTIFACTS/`. No other mathematical source, current audit, root code/result, state ledger, memory file, other worktree, or nonallowlisted link was read. The supplied THM052 proof and its exposure statement were read; this is explicitly exposed reconstruction of its needed mechanism, not an independent rediscovery or an assertion that its pending audits have passed.

## 1. Entire assertion, negation, and source boundary

Fix an integer \(N\geq2\) and a finite \(\nu>0\). Write

\[
M=(\mathbb T^4)^N,\qquad
\Omega=\{x\in M:x_i\ne x_j\ (i\ne j)\},\qquad
H(x)=\frac1N\sum_{i<j}g(x_i-x_j),
\]

where every torus has Haar mass one, Fourier characters are \(e^{2\pi i k\cdot z}\), and \(\widehat g(0)=0\), \(\widehat g(k)=|k|^{-2}\) for \(k\ne0\). Set

\[
c=4\pi^2,\qquad \kappa=c(N-1),\qquad b=\nabla_M H.
\tag{1}
\]

Let \(Y\) be the maximal local solution on \(\Omega\) of

\[
dY=b(Y)\,dt+\sqrt{2\nu}\,dW,
\tag{2}
\]

with initial law product Haar, independent of the \(4N\)-dimensional standard Brownian motion. Its maximal lifetime is \(\zeta\), and it is killed there. There is no continuation or entrance rule. The norm \(|b|\) is the Euclidean norm in all \(4N\) coordinates. For \(i<j\), \(m_{ij}\) is the probability measure obtained by choosing the common coordinate \(x_i=x_j\) and the other \(N-2\) coordinates independently from Haar.

The conjunction to be proved is:

\[
\mathbb E\int_0^\zeta |b(Y_s)|\,ds
=\frac1\kappa\int_\Omega |b(x)|\,dx<\infty,
\tag{3}
\]

the existence of an actual limit \(Z=Y_{\zeta-}\in M\setminus\Omega\) almost surely, and the following full marked identity. Precisely one unordered pair coincides at \(Z\); call it \(I\). For each pair \(i<j\) and every bounded Borel \(\phi:(0,\infty)\times M\to\mathbb R\),

\[
\mathbb E[\mathbf1_{\{I=\{i,j\}\}}\phi(\zeta,Z)]
=\frac{2c}{N}\int_0^\infty e^{-\kappa t}
             \int_M\phi(t,x)\,dm_{ij}(x)\,dt.
\tag{4}
\]

Complex bounded tests follow by linearity. Formula (4) also holds for every nonnegative Borel test with extended values. Consequently \(\zeta\) has exponential rate \(\kappa\), is independent of \((I,Z)\), the mark is uniform among the \(N(N-1)/2\) pairs, and the conditional law of \(Z\) given the mark is exactly \(m_{ij}\). At \(N=2\) the sole mark is \(\{1,2\}\).

The exact negation is the existence of one admitted finite \(N,\nu\) for which (3), terminal existence/collision, unique binary marking, or (4) fails for at least one admitted test. It is not negated by a different initial law, a point-start survival law, a smooth conservative cutoff, a different kernel normalization, or any statement about the repulsive flow or a thermodynamic limit. No such violation is found; Sections 2–8 give an analytic proof of the complete conjunction.

The mathematical preflight uses the R1 model and algebra for geometry, signs and the deleted interaction coefficient; R4 Sections 2–3 for the heat representation and distributional normalization; R6 Sections 3–4 for the local construction and repulsive energy mechanism; and the complete R27 THM052 proof, Sections 2–4, for the disclosed killed-domain duality method. Those necessary mechanisms are reconstructed below. THM052(B)–(C), any modal equivalence, the other parts of R4/R6, and the current status of any independent audit are not premises. THM046 is read only to retain the open original target and its exact scope. No external literature premise or novelty claim is made.

## 2. The kernel and the complete configuration-space distribution

For the unit-torus heat kernel \(p_t\), its periodized Gaussian expression gives

\[
g(z)=c\int_0^\infty(p_t(z)-1)\,dt.
\tag{5}
\]

This converges in \(L^1\): on \((0,1]\), \(\|p_t-1\|_1\leq2\), and for large times the nonzero Fourier modes decay exponentially. Its nonzero Fourier coefficient is \(c/(4\pi^2|k|^2)=|k|^{-2}\). Subtracting the whole-space heat integral near zero gives

\[
g(z)=|z|^{-2}+h(z),\quad h\in C^\infty(B_{1/3}),
\qquad \nabla g(z)=-2z|z|^{-4}+\nabla h(z).
\tag{6}
\]

Indeed \(c\int_0^\infty(4\pi t)^{-2}e^{-|z|^2/(4t)}dt=|z|^{-2}\); the nonzero lattice translates at small times decay with all derivatives like a power of \(t^{-1}\) times \(e^{-a/t}\), while the large-time difference and its derivatives are integrable. Thus \(g\) is smooth off zero, bounded below, tends to positive infinity at zero, and both \(g\) and \(\nabla g\) are integrable. The distributional gradient equals the integrable representative in (6), since the omitted small-sphere boundary term for differentiating \(g\) is \(O(r)\).

Fourier differentiation in (5), or testing its heat equation and integrating in time, gives the full identity

\[
\Delta g=c(dx-\delta_0).
\tag{7}
\]

The atom has mass \(-c\): the outward flux of \(-2z|z|^{-4}\) through a small sphere is \(-2|\mathbb S^3|=-4\pi^2\). The constant compensation in (7) follows from the frozen global Fourier normalization and cannot be inferred from a local principal singularity alone. Off zero the ordinary Laplacian is \(c\).

Here is the configuration-space lift with its measure normalization visible. For \(F\in C^\infty(M)\), fix a pair and set

\[
\psi_{ij}(z)=\int F(\ldots,x_i=y+z,\ldots,x_j=y,\ldots)\,
                       dy\prod_{\ell\notin\{i,j\}}dx_\ell.
\]

The change of variables has Haar Jacobian one. In these coordinates \(\partial_{x_i}=\partial_z\) and \(\partial_{x_j}=\partial_y-\partial_z\). After integration in \(y\), the \(y\)-derivatives and mixed derivatives vanish, and derivatives in all other coordinates also integrate to zero. Hence

\[
\int_M g(x_i-x_j)\Delta_M F(x)\,dx
=2\langle\Delta g,\psi_{ij}\rangle
=2c\left(\int_M F\,dx-\int_M F\,dm_{ij}\right).
\]

Summing unordered pairs and dividing by \(N\) proves, as distributions on all of \(M\),

\[
\boxed{\ \Delta_M H=\kappa\,dx-\frac{2c}{N}\sum_{i<j}m_{ij}.\ }
\tag{8}
\]

The symbol \(m_{ij}\) is the stated probability pushforward of Haar, not unnormalized induced surface measure. No extra geometric surface factor is hidden. On \(\Omega\), (8) reduces to the classical identity \(\Delta_M H=\kappa\); both identities are used in different places below.

Each pair contributes a vector having \(\nabla g\) and \(-\nabla g\) in two coordinate blocks. Thus

\[
\int_M |b(x)|\,dx
\leq\frac{\sqrt2}{N}\binom N2\|\nabla g\|_{L^1(\mathbb T^4)}<\infty.
\tag{9}
\]

This proves first-power integrability of the full drift. It asserts no square integrability of the full drift or of individual pair forces. In particular the identity obtained from (8) is legitimate for every smooth global test:

\[
\int_M b\cdot\nabla F\,dx
=-\kappa\int_M F\,dx+\frac{2c}{N}\sum_{i<j}\int_M F\,dm_{ij}.
\tag{10}
\]

It is the definition of the distributional divergence of an \(L^1\) field, already identified by (8), not an unproved integration by parts across collisions.

## 3. Actual processes, killing and the required survivor identity

This section reconstructs the part of THM052 needed below, using the disclosed method of its supplied complete self-checked proof. It does not merely import that theorem card as certified.

Smooth bounded extensions of the drift from compact subsets of \(\Omega\) have global unique solutions by Picard iteration after subtracting the additive Brownian path. Their Picard approximants are jointly measurable in the starting state and driving path. Uniqueness identifies any two extensions until the common compact-set exit. Taking increasing compact sets therefore defines the unique maximal continuous adapted solution of (2), with its jointly measurable killed law.

Use the open sets \(D_L=\{x:\min_{i<j}\operatorname{dist}(x_i,x_j)>1/L\}\), for sufficiently large integers \(L\). Their closures lie in \(\Omega\). Let \(\tau_L\) be the first exit, with \(\tau_L=0\) if the initial point is outside \(D_L\). The local construction gives \(\tau_L\uparrow\zeta\); if the limit were earlier than the maximal lifetime, the continuous path on a slightly longer interval would have a positive minimum separation and would lie in some \(D_L\), a contradiction. No smoothness of the boundary of \(D_L\) is required. Killing at \(\zeta\) defines the minimal sub-Markov semigroup \(Q_t\).

For comparison construct the local repulsive solution with drift \(-b\), and let \(P_t\) denote its semigroup after establishing conservativity. If \(g_*\) is the finite infimum of \(g\), then

\[
\mathcal E=H-\frac{N-1}{2}g_*
=\frac1N\sum_{i<j}(g(x_i-x_j)-g_*)\geq0.
\]

Every energy sublevel is a compact subset of \(\Omega\), including near simultaneous or disjoint partial collisions, because every summand is nonnegative and the colliding pair term diverges. Stopped Itô on the sublevel gives, for the repulsive process,

\[
d\mathcal E=-|b|^2dt+\nu\kappa dt+\sqrt{2\nu}\,b\cdot dW.
\tag{11}
\]

At a fixed height stop the integrand is bounded, so the martingale has zero mean. The probability of reaching height \(R\) by time \(T\) is at most \((\mathcal E(x)+\nu\kappa T)/R\). Letting \(R\) tend to infinity proves nonexplosion and noncollision from each collision-free start. A trajectory that stays in a compact subset of \(\Omega\) cannot have any other finite nonextendible endpoint: its bounded drift integral and Brownian displacement have limits and a smooth extension continues it. Thus \(P_t1=1\). This conservativity concerns only the repulsive comparison, and is not asserted for (2).

Fix \(D=D_L\). Extend both signs of the drift boundedly and smoothly around \(\overline D\) and kill at the first exit. Boundedness verifies the exponential-integrability condition for the usual bounded-drift Girsanov formula at every finite time. Brownian motion \(B\) with generator \(\nu\Delta_M\), stopped on exit, satisfies on survival to \(t\)

\[
\int_0^t b(B_s)\cdot dB_s=H(B_t)-H(B_0)-\nu\kappa t.
\]

The Girsanov density for adding drift \(a\) is
\(\exp[(2\nu)^{-1}\int a\cdot dB-(4\nu)^{-1}\int|a|^2ds]\).
For \(V_D=|b|^2/(4\nu)\), define the killed Brownian operator

\[
K_t^D v(x)=\mathbb E_x^B\left[\mathbf1_{\{\tau_D>t\}}
        e^{-\int_0^t V_D(B_s)ds}v(B_t)\right].
\]

All coefficients and multipliers used here are bounded on \(D\) for this fixed \(L\). Haar-start Brownian motion is reversible: its finite-dimensional densities are products of the symmetric torus heat kernels, unchanged by reversal; finite-dimensional cylinder sets generate the Borel sigma-field on continuous path space. The entire-path survival event and the potential integral are reversal invariant. Therefore \(K_t^D\) is symmetric. Substitution of the two signs into the Girsanov density gives

\[
P_t^D h=e^{H/(2\nu)+\kappa t/2}K_t^D(e^{-H/(2\nu)}h),
\qquad
Q_t^D f=e^{-H/(2\nu)-\kappa t/2}K_t^D(e^{H/(2\nu)}f),
\]

and consequently

\[
\int_D fP_t^Dh\,dx=e^{\kappa t}\int_D hQ_t^Df\,dx.
\tag{12}
\]

For nonnegative bounded tests the killed expectations, extended by zero for starts outside \(D_L\), increase with \(L\). On the repulsive side their limit is the conservative expectation. On the attractive side the union of the events \(\{\tau_L>t\}\) is exactly \(\{\zeta>t\}\). Monotone convergence in (12) yields

\[
\int fP_th\,dx=e^{\kappa t}\int hQ_tf\,dx.
\]

Taking \(h=1\) gives the required exact survivor measure:

\[
\mathbb E[\mathbf1_{\{t<\zeta\}}F(Y_t)]
=e^{-\kappa t}\int_M F(x)\,dx
\quad(t\geq0)
\tag{13}
\]

for bounded nonnegative Borel \(F\), then for every nonnegative Borel \(F\) by truncation and monotone convergence. This step does not assume a terminal limit or any description of the collision set hit. It already gives \(\mathbb P(\zeta>t)=e^{-\kappa t}\), so \(0<\zeta<\infty\) almost surely and \(\mathbb E\zeta=1/\kappa\). Positivity of the lifetime also follows directly from the collision-free initial state and local continuity. No point-start exponential law is asserted.

## 4. Lifetime occupation, finite action and the actual terminal limit

For any nonnegative Borel \(a(t,x)\), Tonelli and (13), first for product tests and then for nonnegative Borel functions, give

\[
\mathbb E\int_0^\zeta a(s,Y_s)\,ds
=\int_0^\infty e^{-\kappa s}\int_M a(s,x)\,dx\,ds.
\tag{14}
\]

One may also apply the marginal identity at each fixed \(s\) to the Borel section \(a(s,\cdot)\); joint measurability follows from the local path construction. Formula (14) permits either side to be infinite. With \(a=|b|\), (9) shows that it is finite and gives exactly (3). Hence \(\int_0^\zeta|b(Y_s)|ds<\infty\) almost surely.

Choose a measurable lift of the initial point to \(\mathbb R^{4N}\). The local solutions have a consistent lift satisfying, before \(\zeta\),

\[
\widetilde Y_t=\widetilde Y_0+\int_0^t b(Y_s)ds+\sqrt{2\nu}\,W_t.
\tag{15}
\]

The vector drift integral converges absolutely at \(\zeta\). Brownian motion is defined and continuous at every finite time, hence also at the almost surely finite random time \(\zeta\). Formula (15) has a finite Euclidean limit; its projection is the actual torus limit \(Z\). Compactness alone would not prove this convergence. The limit is measurable, for example from limits along the measurable compact-exit times, with arbitrary values on the null exceptional event.

If \(Z\in\Omega\), its minimum separation is positive. Convergence then puts the tail of the path in a collision-free compact neighborhood. A bounded smooth extension of the drift there, with the same continuous Brownian path, continues the solution through \(\zeta\); by uniqueness it agrees with the original before \(\zeta\). This contradicts maximality. Thus \(Z\in M\setminus\Omega\) almost surely. No claim about how many pairs coincide has yet been used.

For calculations below let \(\overline Y_t=Y_t\) for \(t<\zeta\) and \(\overline Y_t=Z\) for \(t\geq\zeta\). This is only an auxiliary stopped continuous path used to evaluate terminal observables. It is not a continuation of (2), does not evaluate the singular drift on the diagonal, and does not alter the killed semigroup.

## 5. Stopped Itô formula through the lifetime, with true martingales

Take a real \(F\in C^\infty(M)\). Stop the local equation at \(t\wedge\tau_L\). On each compact domain ordinary smooth Itô gives

\[
F(Y_{t\wedge\tau_L})=F(Y_0)
+\int_0^{t\wedge\tau_L}(\nu\Delta_MF+b\cdot\nabla F)(Y_s)ds
+\sqrt{2\nu}\int_0^{t\wedge\tau_L}\nabla F(Y_s)\cdot dW_s.
\tag{16}
\]

If the initial point is outside \(D_L\), the stop is zero and both integrals vanish; there is no unbounded-initial-state martingale problem. The last term is square integrable. As \(L\) increases, the left side converges almost surely and in \(L^1\) to \(F(\overline Y_t)\), by the terminal limit and boundedness of \(F\). The drift terms converge in \(L^1\), since their absolute values on the full lifetime are bounded by

\[
\nu\|\Delta_MF\|_\infty\zeta
+\|\nabla F\|_\infty\int_0^\zeta|b(Y_s)|ds,
\tag{17}
\]

an integrable random variable already established in Sections 3–4.

Define the stochastic integrand to be zero at and after \(\zeta\). It is progressively measurable by localization; its value at the single endpoint has no effect. Its full bracket is bounded by \(2\nu\|\nabla F\|_\infty\zeta\), whose expectation is finite. Thus

\[
M_t^F=\sqrt{2\nu}\int_0^{t\wedge\zeta}\nabla F(Y_s)\cdot dW_s
\]

is a true square-integrable martingale, and the localized martingales converge to it in \(L^2\) by the Itô isometry and dominated convergence of the brackets. Explicitly the squared error is at most
\(2\nu\|\nabla F\|_\infty\mathbb E[(t\wedge\zeta)-(t\wedge\tau_L)]\to0\).
Passing (16) therefore proves the genuine stopped identity

\[
F(\overline Y_t)=F(Y_0)
+\int_0^{t\wedge\zeta}(\nu\Delta_MF+b\cdot\nabla F)(Y_s)ds+M_t^F.
\tag{18}
\]

The same finite expected bracket permits the limit \(t\to\infty\) if needed. Neither Itô applied directly to the singular \(H\) at its attractive lifetime nor square integrability of the singular force is used.

## 6. The complete unmarked time/configuration exit measure

Let \(\mathcal A F=\nu\Delta_MF+b\cdot\nabla F\) on \(\Omega\). Its absolute Haar integral is finite by (9). Taking expectations in (18) and using (13) or (14) gives

\[
\mathbb E F(\overline Y_t)
=\int_M Fdx+\int_0^t e^{-\kappa s}\int_M\mathcal A Fdx\,ds.
\tag{19}
\]

On the torus \(\int\Delta_MFdx=0\), whereas (10) gives the entire remaining integral, including the boundary atom:

\[
\int_M\mathcal A Fdx
=-\kappa\int_M Fdx+\frac{2c}{N}\sum_{i<j}\int_MFdm_{ij}.
\tag{20}
\]

Write \(a_F=\int_MFdx\) and \(j_F=(2c/N)\sum_{i<j}\int Fdm_{ij}\). Substitution into (19) gives

\[
\mathbb EF(\overline Y_t)
=e^{-\kappa t}a_F+\left(\int_0^t e^{-\kappa s}ds\right)j_F.
\]

The contribution on \(\{\zeta>t\}\) is exactly the first term by (13). Therefore

\[
\mathbb E[\mathbf1_{\{\zeta\leq t\}}F(Z)]
=\frac{2c}{N}\int_0^t e^{-\kappa s}ds
                         \sum_{i<j}\int_MFdm_{ij}
\quad(t\geq0).
\tag{21}
\]

There is no assumption that a collision was binary in this computation. Multiple collisions, if they had positive probability, would have contributed to the left side.

Both sides of (21) are integrals against finite Borel measures on the compact metric space \(M\). Smooth trigonometric polynomials are uniformly dense in continuous functions (for instance convolve a continuous function with the periodized heat kernel, then approximate its absolutely convergent Fourier series). Thus (21) holds for all continuous \(F\). To see explicitly that this identifies the measures, approximate the indicator of an open set by the increasing continuous functions \(\min(1,n\operatorname{dist}(x,O^c))\). Equality on open sets extends to the Borel sigma-field by the monotone-class theorem. Hence (21) holds with \(F=\mathbf1_A\) for every Borel \(A\subset M\), and then for bounded Borel functions.

Subtract the identities at times \(a\) and \(b\). For all \(0\leq a<b<\infty\) and Borel \(A\), the actual finite measure of \((a,b]\times A\) under \((\zeta,Z)\) equals the corresponding value of

\[
\boxed{\ \mathcal J(dt,dx)
=\frac{2c}{N}e^{-\kappa t}dt\sum_{i<j}m_{ij}(dx).
\ }
\tag{22}
\]

These rectangles generate the Borel sigma-field of \((0,\infty)\times M\). The candidate has total mass
\((2c/N)\binom N2/\kappa=1\), and the actual pair has that mass because \(0<\zeta<\infty\). Uniqueness of finite measures on the rectangle system, followed by bounded approximation or monotone convergence, proves (22) for every bounded Borel test and every nonnegative Borel test with extended values. This is the full joint time/configuration exit measure, not merely its time marginal, one-point marginals, or an infinitesimal formal flux.

## 7. Unique binary collision, mark, and exact independence

Let \(D_{ij}=\{x:x_i=x_j\}\) and
\(S_{ij}=D_{ij}\setminus\bigcup_{\{k,l\}\ne\{i,j\}}D_{kl}\).
These are Borel sets. Under \(m_{ij}\), the common point and each other coordinate are independent Haar points in \(\mathbb T^4\). For a second pair sharing one label with \(\{i,j\}\), its extra equality equates an independent Haar point to the common point and has probability zero. For a disjoint second pair it equates two independent Haar points and also has probability zero. There are finitely many other pairs, so

\[
m_{ij}(S_{ij})=1,\qquad
m_{kl}(S_{ij})=0\quad\text{if }\{k,l\}\ne\{i,j\}.
\tag{23}
\]

The second identity holds because \(m_{kl}\) is supported on \(D_{kl}\), which \(S_{ij}\) excludes. Formula (22) now proves
\(\mathbb P(Z\in\bigcup_{i<j}S_{ij})=1\).
Thus exactly one unordered pair coincides and no other equality occurs. This rules out triple clusters, two disjoint binary collisions, and every larger multiple-collision pattern at the first lifetime. It is a consequence of the proved exit measure; no polar-set theorem or collision exclusion was presumed.

Define \(I=\{i,j\}\) on \(\{Z\in S_{ij}\}\), and assign any mark on the null complement. Restrict (22) to \(S_{ij}\). By (23), only \(m_{ij}\) remains and its restriction is unchanged. This is exactly (4), for the whole stated Borel test class.

The time integral gives

\[
\mathbb P(I=\{i,j\})=\frac{2c}{N\kappa}
=\frac1{\binom N2},\qquad
\mathbb P(Z\in A\mid I=\{i,j\})=m_{ij}(A).
\]

Furthermore the joint law is the product of \(\kappa e^{-\kappa t}dt\) with the probability law assigning weight \(\binom N2^{-1}\) to each pair and conditional configuration \(m_{ij}\). This proves independence of \(\zeta\) from the entire pair \((I,Z)\), including independence from each component and the corresponding conditional time laws. It does not assert independence of \(I\) and \(Z\): the mark is determined by the configuration almost surely. Conditional on the mark, the common point and remaining coordinates have the stated independent Haar law, but the two colliding coordinate entries are equal, not independent.

At \(N=2\), \(\kappa=c\), \(2c/N=c\), and (4) becomes the exponential time law times the pushforward of one Haar meeting point. There are no other pairs to exclude. The proof applies without a special point-start assertion or an invalid global choice of a torus center of mass.

## 8. Independent-form falsification and exact diagnostic route

This section and the companion diagnostics challenge the result by mechanisms different from the stopped-test measure derivation. They remain same-context checks, not isolated audits.

**Fourier coefficients of the full distribution.** For a configuration character with frequencies \(k_1,\ldots,k_N\in\mathbb Z^4\), direct integration against \(m_{ij}\) is one precisely when all frequencies outside the pair vanish and \(k_i+k_j=0\), and is zero otherwise. The Fourier coefficient of \(H\) at a nonzero character is \(1/(N|k_i|^2)\) when exactly that opposite nonzero pair is present, and zero for other patterns. Multiplying by the full Laplacian symbol \(-c\sum_i|k_i|^2\) reproduces (8), including its zero-mode compensation and \(-2c/N\) coefficient. Three active frequencies with zero total frequency have zero exit moment unless the prescribed pair-diagonal condition holds. Thus translation invariance alone cannot hide an unwanted triple-collision mass.

**Normal-coordinate flux.** Near a single pair diagonal use orthonormal coordinates \(q=(x_i-x_j)/\sqrt2\) and \(p=(x_i+x_j)/\sqrt2\). The principal pair energy is \((2N)^{-1}|q|^{-2}\). Its transverse outward gradient flux is \(-2\pi^2/N\) per unit \(p\)-volume. On the diagonal \(p=\sqrt2,y\), so in four dimensions \(dp=4dy\). The resulting atom in probability-Haar coordinates has coefficient \(-8\pi^2/N=-2c/N\). This independent geometric computation catches the otherwise easy mismatch between probability diagonal measure and induced surface measure. The identification of the actual exit measure still requires Sections 3–7.

**Two-particle radial coefficients.** The difference process has noise covariance \(4\nu I_4\), hence diffusion generator \(2\nu\Delta_z\), and drift \((2/N)\nabla g(z)\) when one checks a pair coefficient \(1/N\). For the Euclidean principal kernel, the generator of \(r^p\) is

\[
2\nu p(p+2)r^{p-2}-\frac{4p}{N}r^{p-4}.
\tag{24}
\]

In particular it sends \(r^2\) to \(16\nu-8/(Nr^2)\), and \(r^4\) to \(48\nu r^2-16/N\). At the actual \(N=2\), these agree with direct differentiation in all eight coordinates. This is a local differential test; the Euclidean kernel alone has no periodic compensation and is not substituted for the torus theorem.

For the additional exactly solvable, deterministic Euclidean two-particle diagnostic, \(r(t)^4=r_0^4-16t/N\), up to collision at \(Nr_0^4/16\). The full drift length is \(r_0/\sqrt2\), while the integral of its square diverges. This diagnostic has \(\nu=0\) and a nonperiodic kernel, so it is explicitly outside the theorem's hypotheses. It distinguishes first-power action from the false squared-force strengthening and does not prove any stochastic collision statement.

**Laplace-time check.** Applying the already justified stopped Itô formula to \(e^{-at}F\), for \(a\geq0\), yields

\[
\mathbb E[e^{-a\zeta}F(Z)]
=\int Fdx+\frac1{\kappa+a}\int(\mathcal A F-aF)dx
=\frac{2c/N}{\kappa+a}\sum_{i<j}\int Fdm_{ij}.
\tag{25}
\]

The terminal formula and direct Fourier-gradient pairing give matching rational expressions after measuring \(a\) in units of \(c\). This checks both the rate and the factor multiplying each unordered pair, at \(N=2,3\) and further finite \(N\), without relying only on total mass.

The standard-library diagnostic executes exact rational Fourier and differential checks, the transverse normal-coordinate coefficient, probability/mark/Laplace factors, and a deterministic radial antiderivative. Deliberate mutations remove the pair factor two, flip the collision atom, remove torus compensation, change the rate, insert a spurious diffusivity factor, halve the relative noise, add triple-diagonal mass, and insert time/configuration dependence while preserving the two marginals. Each selected mutation has an explicit nonzero residual in the companion JSON. Exact automatic differentiation also exposes a nonzero difference between the full drift square and a sum of pair squares in a symmetric three-particle configuration. These are diagnostics and rejected surrogate changes, not counterexamples to the frozen theorem.

## 9. Failed shortcuts, adversarial self-review and limits

The following attempts are insufficient, and the exact point of failure is retained rather than concealed.

1. A formal adjoint with \(\Delta H=\kappa\) everywhere drops the collision measure. Its zero-mode test already fails because a periodic Laplacian has total mass zero. Section 2 retains the atom, and Section 3 uses the punctured identity only inside killed domains.
2. Exponential survival and conditional Haar marginals alone do not identify the terminal configuration or its relation to time. The first missing line is existence of a terminal limit and a justified terminal test identity. Sections 4–6 supply both. A positive coupled perturbation of the product exit law can preserve the time and configuration marginals while violating the joint identity; the diagnostic detects one explicitly.
3. Compactness of the configuration torus supplies convergent subsequences, not convergence at the lifetime. The missing Cauchy control is the first-power drift integral in (15); (14) supplies it without a squared-force estimate.
4. Applying Itô to singular \(H\) at an attractive collision is not justified by the supplied repulsive energy calculation. The attractive drift-square need not be controlled. The proof instead applies localized Itô to globally smooth bounded \(F\), with the integrable envelope (17) and a bounded-gradient martingale.
5. A pairwise radial heuristic does not exclude simultaneous collisions in a many-particle system. The first missing line would be the effect of the other singular drifts during a multi-cluster approach. This proof never makes that reduction: it derives (22) for the actual process before using the null intersections (23).
6. Independent Brownian center and relative increments at \(N=2\) do not license a globally single-valued torus center coordinate obtained by division by two, nor do they imply the asserted full terminal law for \(N>2\). The full configuration-space test identity avoids this topological shortcut.
7. Integrability of each individual force in first power permits a triangle bound for the total norm, but deleting cross terms in a square is invalid. The explicit three-particle diagnostic detects this mutation. No part of (3) depends on such a deletion.
8. A smooth global attractive cutoff is conservative and has no actual killed boundary loss. One cannot infer (22) from its formal stationary density or from setting its cutoff to zero without stopping control. The construction uses compact-domain killing from the outset and identifies the actual maximal singular path.

The strongest new claim has been checked in this same context for the following load-bearing points: actual local realization and maximal lifetime; conservative comparison before using duality; all four Girsanov/gauge signs; bounded-domain reversal rather than boundary regularity; monotone exhaustion; unbounded first-power occupation by Tonelli; a convergent Euclidean lift; a collision endpoint by continuation contradiction; stopped Itô with an integrable finite-variation envelope and true martingales; full distributional compensation and probability-diagonal normalization; identification on all time/configuration rectangles; null intersections before defining the mark; and exact product-factorization of the resulting joint law. This is self-review, not independent certification.

All parameters remain fixed and finite in the argument. No new preparation, point-start formula, original-flow collision, instantaneous singular-force square, thermodynamic time scale, critical cancellation estimate, Gaussian law, or finite/infinite hierarchy closure is obtained. The exact first-power occupation identity concerns only the explicitly auxiliary killed law. No additional assumption is inserted into the frozen theorem. The entire assertion is a candidate for the root's fresh whole-claim audits; canonical ledgers and fresh gates remain the root's responsibility.

## 10. Handoff and verification

Created only this memorandum and its uniquely issued `ROUND_028_COLLISION_FLUX_ARTIFACTS` packet with named archive/inventory/seal siblings. The twelve original inputs were preserved byte-for-byte. The packet contains a copy of this memorandum for portable review. The complete read/exposure/operation record identifies the initially truncated combined display and its successful bounded re-reads; this caused no unexamined input portion. Every computational check is recorded with exact inputs/results, and the verifier is read-only, standard-library-only, and rejects symlinks, unexpected regular members, unsafe archive names and digest mismatches.

Verification commands and final actual counts/results are recorded in the packet README and JSON, avoiding a self-referential digest in this file. No TeX source was created or modified; this is the task's requested Markdown proof, and no TeX compilation is claimed. No dependency, child agent, commit, push, remote operation, canonical state edit, source edit, external browse, or memory read occurred. All newly issued evidence is sealed read-only. There is no unresolved analytic line within THM053(A)–(B) identified by this construction; the remaining requirement is fresh independent reconstruction and hostile audit, with no inference that the original critical source is solved.
