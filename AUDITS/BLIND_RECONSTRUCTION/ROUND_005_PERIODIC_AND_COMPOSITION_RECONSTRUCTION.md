# Round 005: statement-only reconstruction of the periodic pair potential and abstract response composition

2026-09-17 UTC. TASK-040. Independent lane `/root/r005_periodic_blind`.
Worktree: `/private/tmp/hocf-r005-periodic-blind-20260917_230757_UTC`.
Branch: `codex/hocf-r005-periodic-blind`.
Base: `52bda5d0d24067b051c6fe9763f2a78e7599e593`.

**Verdict: reconstruction passes in the exact scopes of THM-023 and THM-024.** The periodic assertion has a complete proof below, including the cutoff terms, singular process, Haar-space realization, strong singular passage, and two-time strong continuity. The abstract implication has separate pointwise and L2 proofs and retains the squared density factor. No assertion is made about either unseen constructor proof. No regularity hypothesis for the actual campaign data, finite-particle generator-domain statement, evolved-law estimate, or fluctuation theorem is certified.

## 1. Blindness, inputs, and exact scope

Only the eight files in `AUDITS/ROUND_005_PERIODIC_BLIND_INPUT_SHA256SUMS.txt` were read: the task, AGENTS, the frozen Round 001 model, THM-015/023/024, and the sealed Round 004 local reconstruction and its all-N addendum. Their bytes were copied from the root into this newly created worktree and verified before mathematical work. The input manifest is copied again beside this report at sealing. No periodic constructor, conditional-response constructor, audit narrative, canonical state ledger, repository history, outside source, or memory file was read. Initial Git status inspection exposed filenames of root modifications, not their contents; no excluded mathematical information was obtained from it. General campaign instructions were already present in the task context. No earlier exposure to the THM-023/024 proof narratives is known.

The restricted task overrides broad orientation reading and canonical-ledger duties for this lane: no README, specification, orchestration file, or additional ledger was opened, and root alone integrates state. No child worker, commit, push, dependency installation, or root-file edit was performed.

The primary assertion is the conjunction of all statements in the frozen THM-023 and the conditional implication in THM-024. Its exact negation is admissible data satisfying their respective hypotheses for which any stated existence, uniqueness, integrability, bound, representative independence, measurability, or convergence assertion fails. In particular, the assertion is not that the actual mean-field drift, backward test, or exact response operator satisfies these hypotheses.

The local prerequisite supplies its explicit radial profile and elementary radial inequalities, on the punctured Euclidean relative-coordinate model only. Its periodic cutoff diagnostic was not a periodic equation solution. The global construction in Sections 3--8 below is new in this reconstruction. The Round 004 all-N addendum is used for its exact radial integral calculation, which is also restated and checked here. THM-015 is used only for the initial iid finite-N identity; that identity is rederived in Section 10.

There is no Fourier normalization input: THM-023 directly prescribes the local principal part `|z|^-s`. Thus the Round 001 gamma-function Fourier constant is not invoked. The relative diffusion is `2 nu Delta`, the relative singular drift is `2s z/(N |z|^(s+2))`, the pair generator has `nu(Delta_x+Delta_y)`, and the statistic is `U_2/2` with denominator `N^2`. The logarithmic problem and every law other than the explicitly stated initial iid law are excluded.

## 2. Fixed data and radial identities

Write `E=(T^d)^2` with product Haar probability measure `m`, and `E_*={x!=y}`. Take the parameters and data exactly as in THM-023. Choose radii

\[
 0<r_0<r_1<r_*<1/2
\]

such that the prescribed decomposition `g(z)=|z|^-s+q(z)` holds on the embedded ball of radius `r_*`. Choose a smooth radial even cutoff `chi`, with `0<=chi<=1`, equal to one on `r<=r_0`, and supported in `r<r_1`. Every radial function multiplied by this cutoff is extended periodically by zero outside that ball.

Use the following finite bounds:

\[
 \begin{split}
 L&=\sup_{t,x}\|D u_t(x)\|,\qquad
 H=\sup_{t,x}\|D^2 f_t(x)\|,\qquad
 G=\sup_{t,x}|\nabla f_t(x)|,\\
 Q&=\sup_{|z|\le r_1}\|D^2q(z)\|,\qquad
 L_0=L+Q,\qquad k=sL_0.
 \end{split} \tag{2.1}
\]

The norms are Euclidean operator norms. Since q is even, `grad q(0)=0`, so `|grad q(z)|<=Q|z|`. For a relative vector `z=x-y` in this ball, the relative drift is

\[
 b_N(z)+a_t(x,y),\qquad
 b_N(z)=\frac{2s}{N}|z|^{-s-2}z,\qquad
 a_t(x,y)=u_t(x)-u_t(y)-\frac2N\nabla q(z),
 \quad |a_t(x,y)|\le L_0|z|. \tag{2.2}
\]

The last bound uses `N>=2`, including N=2. Uniform spatial Lipschitz continuity of u and its time continuity imply joint continuity of u; compactness also bounds its values. Joint measurability of the prescribed derivatives makes J jointly measurable. No time derivative of u or f is required anywhere below.

Put `p=s+2`, `c_s=2sp`, and, for `tau>=0`,

\[
 F_{N,\tau}(r)=\frac N4\left[
       (r^p+c_s\tau/N)^{2/p}-r^2\right],\qquad r>0.
 \tag{2.3}
\]

The permitted local reconstruction proves, and direct differentiation gives,

\[
 \begin{split}
 &F\ge0,\qquad \partial_\tau F-b_N\cdot\nabla F=s r^{-s},
 \qquad \Delta F\le0,\\
 &F\le s\tau r^{-s},\qquad
 F\le C_s N^{s/p}\tau^{2/p},\qquad C_s=c_s^{2/p}/4,\\
 &r|F_r|\le s F,\qquad |F_r|\le s^2\tau r^{-s-1}.
 \end{split} \tag{2.4}
\]

For completeness, with `w=r^p+c_s tau/N` and `v=r^p/w`,

\[
 \partial_\tau F=s w^{-s/p},\quad
 F_r=\frac N2r(v^{s/p}-1),\quad
 \Delta F=\frac N2\{v^{s/p}(d+s-sv)-d\}. \tag{2.5}
\]

The derivative of the expression inside braces before subtracting d is

\[
 \frac{s}{p}v^{s/p-1}\{d+s-(2s+2)v\}\ge0,
 \qquad 0<v\le1, \tag{2.6}
\]

because its bracket is at least `d-s-2>=0`; its value at v=1 is d. This proves the superharmonic sign, including `s=d-2`. The last two bounds in (2.4) also follow by differentiating

\[
 F=s\int_0^\tau(r^p+c_s h/N)^{-s/p}\,dh. \tag{2.7}
\]

Indeed the negative logarithmic radial derivative of the integrand is `s r^p/(r^p+c_s h/N)<=s`. These inequalities are for the nonnegative radial profile, not for a signed angular multiplier.

## 3. Global process, collision exclusion, and deterministic-time Markov property

The pair equation is interpreted on the torus, or with periodic drifts on a lift to `R^(2d)`, and noise `sqrt(2nu)(W^1,W^2)`. For each large integer j, smoothly cut the force off inside `|x-y|<1/(2j)` while keeping it unchanged on `|x-y|>=1/j`. The resulting pair drift is globally bounded and globally Lipschitz in space on the torus, uniformly in time for this fixed j and N. It is measurable in time, and in fact continuous in its values under the given assumptions.

For any continuous driving path, the additive-noise integral equation has a unique solution. One explicit construction is Picard iteration: if the cutoff drift has bound B and Lipschitz constant C, the nth successive increment on a horizon h is bounded by `B C^(n-1) h^n/n!`. The summable series gives existence; iterating the corresponding difference inequality gives uniqueness and continuous dependence on the initial point and driving path. These solution maps are causal and Borel, jointly with the starting time, ending time, N and nu. For the time parameters, continuity of the noise path and the bound on the drift control the short interval lost or added at the starting time; the spatial difference is then bounded by Gronwall's elementary iterated estimate.

Solutions with different cutoffs agree until exit from any region on which both drifts equal the original drift. Patching them constructs a pathwise unique maximal solution on `E_*` up to a possible collision lifetime. Exit times from `dist(x,y)>1/j` are Borel because paths are continuous. Choosing the first admissible integer j measurably and then patching countably many maps proves joint measurability of the maximal map, with a cemetery value after its lifetime. No singular existence theorem is being assumed.

To exclude collision, define on the punctured torus

\[
 V(z)=1+\chi(z)|z|^{2-d}. \tag{3.1}
\]

In `0<r<r_0`, application of the pair generator to this relative-coordinate function gives

\[
 \mathcal G_t V
 =-\frac{2s(d-2)}N r^{-s-d}
       +a_t\cdot\nabla r^{2-d}
 \le(d-2)L_0 r^{2-d}\le(d-2)L_0 V. \tag{3.2}
\]

The diffusion term vanishes because `Delta r^(2-d)=0` off zero. On the cutoff annulus all derivatives of V are bounded, and the relative drift is bounded by

\[
 s r_0^{-s-1}+L_0r_1. \tag{3.3}
\]

For example a sufficient constant in `G_t V<=C_V V` is the maximum of `(d-2)L_0` and

\[
 2\nu_*\|\Delta V\|_{\{r_0\le r\le r_1\}}
 +(s r_0^{-s-1}+L_0r_1)
      \|\nabla V\|_{\{r_0\le r\le r_1\}}. \tag{3.4}
\]

Outside the support of chi the generator of V is zero, and `V>=1`. This C_V is independent of N and of nu in the stated interval.

Let `sigma_delta` be the first hit of `dist(x,y)=delta`, where delta is small enough and the start is outside that tube. Stopped smooth Itô, with an exponential factor or its integral Gronwall estimate, yields

\[
 \mathbb E_{t,x,y} V(Z_{a\wedge\sigma_\delta})
       \le e^{C_V(a-t)}V(x-y),
 \qquad
 \mathbb P_{t,x,y}(\sigma_\delta\le T)
       \le e^{C_VT}V(x-y)\delta^{d-2}. \tag{3.5}
\]

Here the stopping time is expressed in absolute time, and `Z=X-Y`. The same statement follows for nu=0 by the ordinary chain rule. Every stochastic integral used in the stopped calculation has bounded integrand for each fixed delta, so it is a true martingale. Letting delta decrease along the patched exhaustion shows that a collision lifetime at or before T has probability zero. Compactness of the torus leaves no other way for a maximal path to fail to continue. Thus the solution is global on the entire prescribed horizon and noncolliding from every fixed off-diagonal initial state.

Every other continuous adapted solution driven by the same Brownian motion agrees with the cutoff solution until each exit time, hence globally. This proves pathwise uniqueness. The jointly Borel maximal map above gives the asserted measurable realization. The statement is the usual realization from each starting state; a common null set simultaneously for every uncountable initial state is neither needed nor used.

Restarting the deterministic solution map at a deterministic time and shifting the continuous driving path gives the same future path, by local uniqueness and patching. Independence of Brownian increments therefore proves

\[
 \mathbb E_{t,q}[h(Q_b)\mid\mathcal F_a]
       =S_{a,b}h(Q_a),\qquad
 S_{t,a}S_{a,b}=S_{t,b},\qquad t\le a\le b, \tag{3.6}
\]

for bounded Borel h on `E_*`. The exceptional future Brownian set has probability zero for each current state, by (3.5), and integrating this fact against the state law justifies the conditioning; no simultaneous-null-set assertion is hidden. Measurable integration of the Borel solution map gives joint measurability of `(t,a,q)->S_(t,a)h(q)`. This is a deterministic-time Markov evolution and a sup-norm contraction. Exchanging x and y and the two Brownian paths preserves the equation, so S commutes with pair exchange. In this report, symmetry of the pair evolution means this exchange symmetry, not self-adjointness of its Haar-space operator.

## 4. A global periodic source barrier with every cutoff term retained

Let `K_0=sup_{dist(z,0)>=r_0}|K(z)|`, a finite constant. Since the Hessian of f is bounded, near the diagonal

\[
 |J_t(x,y)|\le Hs r^{-s}+HQr^2.
 \tag{4.1}
\]

Away from that inner ball, `|J|<=2G K_0`. Hence, with for example

\[
 C_J=HQr_0^2+2G K_0,
 \qquad |J_t(x,y)|\le H\chi(z)s r^{-s}+C_J
 \quad(q\in E_*). \tag{4.2}
\]

Write `A_chi={r_0<=r<=r_1}`. The following constants uniformly bound the cutoff errors for all `0<=tau<=T`, `N>=2`, and `0<=nu<=nu_*`:

\[
 \begin{split}
 F_A&=sT r_0^{-s},\qquad F'_A=s^2T r_0^{-s-1},\\
 E_T&=F_A\left[2\nu_*\|\Delta\chi\|_\infty
       +(s r_0^{-s-1}+L_0r_1)\|\nabla\chi\|_\infty\right]
       +4\nu_* F'_A\|\nabla\chi\|_\infty,\\
 C&=C_J+H E_T.
 \end{split} \tag{4.3}
\]

Consider the nonnegative periodic function, defined off the diagonal,

\[
 W_N(\tau,x,y)=e^{k\tau}
       \{H\chi(x-y)F_{N,\tau}(|x-y|)+C\tau\}.
 \tag{4.4}
\]

It vanishes at tau=0. The `chi F` term is smooth in space away from the diagonal, including across the outside of the cutoff, and differentiable in tau there. For any relative-coordinate function the generator is

\[
 \mathcal G_t=2\nu\Delta+(b_N+a_t)\cdot\nabla
 \tag{4.5}
\]

on the cutoff ball. The product calculation is

\[
 \begin{split}
 (\partial_\tau-\mathcal G_t)(\chi F)
 ={}&\chi s r^{-s}-2\nu\chi\Delta F
       -\chi a_t\cdot\nabla F\\
 &-F\{2\nu\Delta\chi+(b_N+a_t)\cdot\nabla\chi\}
       -4\nu\nabla\chi\cdot\nabla F.
 \end{split} \tag{4.6}
\]

In particular, both the diffusion cross term with coefficient `4nu` and the internal-drift cutoff term are present. By (2.2)--(2.4),

\[
 -2\nu\chi\Delta F\ge0,\qquad
 k\chi F-\chi a_t\cdot\nabla F\ge0. \tag{4.7}
\]

The absolute value of the last line of (4.6) is at most E_T. Consequently

\[
 (\partial_\tau-\mathcal G_t)W_N
 \ge e^{k\tau}\{H\chi s r^{-s}-HE_T+C+kC\tau\}
 \ge |J_t|. \tag{4.8}
\]

This is a global inequality on `E_*`, not an unsupported extension of the local radial equation. It uses bounded nu precisely in the annular estimates (4.3). It differentiates neither u nor f in time.

Apply stopped smooth Itô to `W_N(T-a,Q_a)` up to `T wedge sigma_delta`. Its terminal stopped value is nonnegative. Thus

\[
 \mathbb E_{t,q}\int_t^{T\wedge\sigma_\delta}
       |J_a(Q_a)|\,da\le W_N(T-t,q). \tag{4.9}
\]

The stopped stochastic integrand is bounded for each delta. Noncollision and monotone convergence now give

\[
 \mathbb E_{t,q}\int_t^T|J_a(Q_a)|\,da
 \le W_N(T-t,q),\qquad
 \sup_{t,q} W_N(T-t,q)
 \le e^{kT}\{HC_sN^{s/p}T^{2/p}+CT\}. \tag{4.10}
\]

This is the required finite-N uniform bound on the absolute occupation potential. It is not uniform in N in the sup norm. At T=0 the potential and W are identically zero.

## 5. Signed potential, true-martingale class, and Haar L2 rate

Define

\[
 U_N(t,q)=\mathbb E_{t,q}\int_t^T J_a(Q_a)\,da,
 \qquad q\in E_*. \tag{5.1}
\]

The positive and negative parts are integrable by (4.10). Joint Borel measurability follows from measurable path and time integration, followed by integration over Brownian paths. The source is invariant under pair exchange, because both K and the gradient difference change sign. The process exchange identity therefore gives symmetry of U. It is bounded, terminal zero, and `|U_N(t,q)|<=W_N(T-t,q)`.

The exact solution class is bounded jointly Borel v on `[0,T] x E_*`, terminal zero at every off-diagonal state, for which, from every starting `(t,q)`,

\[
 v(a,Q_a)+\int_t^a J_b(Q_b)\,db,
 \qquad t\le a\le T, \tag{5.2}
\]

is a true martingale. For U this expression is the conditional expectation of the integrable total source integral. To justify the use of the Markov property with J, first truncate its positive and negative parts, apply (3.6) and Tonelli, then use (4.10). Thus U belongs to this class. Taking terminal expectation in (5.2) for any other v proves pointwise uniqueness. No classical PDE regularity or diagonal-start equation is claimed.

Here is an explicit all-N bound for the radial integral that enters its Haar norm. Let `R=r_1`, `a_s=c_s^2/(16d)`, and `omega_d=|S^(d-1)|`. For T>0 define

\[
 C_{\mathrm{rad}}=\omega_d\begin{cases}
 T^2R^{d-2s}\left(a_s+\dfrac{s^2}{d-2s}\right),&2s<d,\\[5pt]
 T^2\left[a_s+\dfrac{s^2}{p}
       \left(1+\log_+\dfrac{R^p}{c_sT}\right)\right],&2s=d,\\[5pt]
 \left(a_s+\dfrac{s^2}{2s-d}\right)
 c_s^{-(2s-d)/p}T^{(d+4)/p},&2s>d.
 \end{cases} \tag{5.3}
\]

Set this constant to zero at T=0 without evaluating a logarithm. Then for every N>=2,

\[
 \sup_{0\le\tau\le T}\int_{B_R}F_{N,\tau}^2\,dz
       \le C_{\mathrm{rad}}\rho_N. \tag{5.4}
\]

This is the radial all-N prerequisite, and can be checked directly as follows. Monotonicity in tau reduces the estimate to T. Put `ell=(c_s T/N)^(1/p)`. The two bounds on F in (2.4) give

\[
 \int_{B_R}F_{N,T}^2\,dz\le\omega_d\left[
 \frac{N^2\ell^4\min(R,\ell)^d}{16d}
 +\mathbf1_{\{\ell<R\}}s^2T^2\int_\ell^Rr^{d-1-2s}\,dr\right].
 \tag{5.5}
\]

Since `N ell^p=c_s T`, the core term before omega_d equals `a_s T^2 ell^(-2s) min(R,ell)^d`. If `2s<d`, it is at most `a_s T^2 R^(d-2s)` for either ordering of ell and R, and the tail is bounded by `s^2 T^2 R^(d-2s)/(d-2s)`. If `2s=d`, the core is at most `a_s T^2` and the tail is `s^2 T^2 log_+(R/ell)`; the inequality `log_+(Nx)<=log N+log_+x` gives (5.3)--(5.4). If `2s>d`, both contributions are at most `(a_s+s^2/(2s-d))T^2 ell^(-(2s-d))`; when ell>R the core has the additional factor `(R/ell)^d<=1`. These estimates include the large-core regime at N=2 and N=3 and the boundary ell=R. They require no asymptotic lower bound on N.

For any integrable function h of a torus difference, product Haar invariance gives `int_E h(x-y) dm=int_(T^d)h(z) dz`. Applying this identity to the pointwise bound W, not to a supposed translation invariance of U, gives

\[
 \sup_t\|U_N(t)\|_{L^2(m)}^2
 \le 2e^{2kT}\{H^2 C_{\mathrm{rad}}\rho_N+C^2T^2\}
 \le C_{\mathrm{base}}\rho_N,
 \quad
 C_{\mathrm{base}}=2e^{2kT}(H^2C_{\mathrm{rad}}+C^2T^2).
 \tag{5.6}
\]

Here `rho_N>=1` for N>=2. The constants depend only on d, s, T, nu_*, the fixed local radii/cutoff, L, H, G, Q, and the fixed force away from the diagonal. They are independent of N and nu in the stated interval. No invariance or regularity of the actual background law is used.

## 6. Distributional divergence and smooth Haar operator bounds

The force K is integrable on the torus because its singular magnitude has order `r^(-s-1)` and `s+1<=d-1<d`. Distributionally, using the same type of cutoff as above,

\[
 \operatorname{div}K=P+R_g,\qquad
 P=\begin{cases}
  s(d-s-2)\chi(z)|z|^{-s-2},&s<d-2,\\
  s\omega_d\delta_0,&s=d-2,
 \end{cases} \tag{6.1}
\]

where R_g is a smooth periodic function. To verify this normalization, write `g=chi r^-s+h` with h smooth globally. Off zero, `-Delta r^-s=s(d-s-2)r^-s-2`. The small-sphere flux in `-Delta` is `s omega_d epsilon^(d-s-2)`. It tends to zero for `s<d-2`, when the displayed density is locally integrable, and is `s omega_d` at `s=d-2`, when the off-zero density vanishes. The remaining terms are

\[
 R_g=-2\nabla\chi\cdot\nabla r^{-s}
       -r^{-s}\Delta\chi-\Delta h, \tag{6.2}
\]

which are smooth because the cutoff derivatives vanish near zero. This establishes the claimed positive distribution and the Coulomb atom without a Fourier convention. The decomposition is fixed after choosing chi, and `C_0=||(R_g)_-||_infty` is finite.

Let `K_e=e^(e Delta)K`. Positivity and mass one of the torus heat kernel give

\[
 \operatorname{div}K_e=e^{e\Delta}P+e^{e\Delta}R_g\ge-C_0.
 \tag{6.3}
\]

The smooth pair drift is

\[
 B^e_t(x,y)=(u_t(x)+K_e(x-y)/N,
                 u_t(y)+K_e(y-x)/N).
\]

Since K_e is odd, its divergence is even, and therefore

\[
 \operatorname{div}_{x,y}B^e_t
 =\operatorname{div}u_t(x)+\operatorname{div}u_t(y)
       +\frac2N\operatorname{div}K_e(x-y)
 \ge-2(D+C_0/N). \tag{6.4}
\]

This explicitly checks the factor two in the pair divergence and the factor one in the final L2 exponent.

Here is a direct operator proof with no time-regularity assumption on derivatives beyond the card. Freeze a continuous Brownian path and subtract the additive noise. The smooth-in-space, time-measurable ODE defines a C1 bijection from its starting torus state to its state at time a. For differentiability, differentiate the integral equation in the initial state; spatial continuity of the derivative at each time and its fixed-e uniform bound justify passage under the time integral by dominated convergence. The derivative solves its linear integral equation. Its matrix determinant solves

\[
 \det D_q Q^e_{t,a}(q)
 =\exp\left\{\int_t^a\operatorname{div}B^e_b(Q^e_{t,b}(q))\,db\right\}
 \ge e^{-2c_N(a-t)},\qquad c_N=D+C_0/N. \tag{6.5}
\]

Surjectivity and injectivity follow by solving the same nonsingular ODE backwards with the frozen noise path. The determinant formula follows first for the linear variational equation by differentiating the determinant polynomial, and then by its scalar integral equation; the bounded measurable time coefficients suffice. Periodicity descends the bijection from its lift to the torus.

Change of variables for this C1 torus diffeomorphism gives, for every nonnegative Borel h,

\[
 \int_E S^e_{t,a}h\,dm\le e^{2c_N(a-t)}\int_Eh\,dm. \tag{6.6}
\]

Taking Brownian expectation is justified by Tonelli. Jensen's inequality now gives

\[
 \|S^e_{t,a}h\|_{L^2(m)}^2
 \le\int_E S^e_{t,a}|h|^2\,dm
 \le e^{2c_N(a-t)}\|h\|_{L^2(m)}^2. \tag{6.7}
\]

Approximation extends the action to all L2 classes with operator norm at most `exp[c_N(a-t)]`, consistently with its action on bounded Borel functions. This random-flow proof is valid also when nu=0; elliptic smoothing in physical time has not been assumed.

## 7. Singular passage, equality classes, and strong convergence

For any compact set away from zero, `K_e` and its first spatial derivatives converge uniformly to those of K as e decreases to zero. One elementary verification splits K into a smooth part equal to K near that compact set and a remainder supported a positive distance away. Heat approximation of the smooth part converges in C1. For the remainder, the periodic Gaussian heat kernel and its derivatives are bounded on the separated set by a polynomial power of `1/e` times `exp[-c/e]`; multiplying by the finite L1 norm of K gives convergence to zero. This proves the required local convergence rather than assuming a global bound on the singular force.

Couple the smooth and singular processes with the same Brownian path and the same off-diagonal initial state. Almost every singular path has a strictly positive minimum distance from the diagonal on `[t,a]`, by continuity and Section 3. On a smaller surrounding tube the original drift is Lipschitz and `B^e-B` tends uniformly to zero. Subtracting the two additive-noise equations up to exit from this tube gives

\[
 \sup_{t\le b\le a}|Q^e_{t,b}-Q_{t,b}|
 \le (a-t)\sup_{b,\,\mathrm{tube}}|B^e_b-B_b|
                      e^{C(a-t)}\longrightarrow0. \tag{7.1}
\]

This estimate, first stopped at tube exit, prevents such an exit for small enough e. Torus distances can be evaluated in compatible local lifts, or after a common smooth periodic cutoff away from the diagonal. Thus convergence holds along the entire interval, almost surely for each fixed starting state. No uniform lower collision distance across all starting states is needed.

For continuous h on the compact pair torus, bounded convergence gives `S^e_(t,a)h(q)->S_(t,a)h(q)` at every off-diagonal q. The same uniform bound on h gives convergence in Haar L2 and convergence of Haar integrals. In particular,

\[
 \int_E S_{t,a}h\,dm\le e^{2c_N(a-t)}\int_Eh\,dm
 \quad(h\ge0\text{ continuous}). \tag{7.2}
\]

To extend this conclusion to all Borel functions without presupposing equality-class consistency, define the endpoint measure

\[
 \eta_{t,a}(A)=\int_{E_*}\mathbb P_{t,q}(Q_a\in A)\,dm(q).
\]

For an open set O, approximate its indicator from below by `min(1,j dist(q,O^c))`. Applying (7.2) and monotone convergence shows `eta(O)<=exp(2c_N(a-t))m(O)`. Taking open supersets of a Borel A and using outer regularity of Haar measure yields

\[
 \eta_{t,a}(A)\le e^{2c_N(a-t)}m(A). \tag{7.3}
\]

This is a dominated endpoint measure obtained from the actual singular process. For every bounded Borel h, Jensen and (7.3) now prove

\[
 \|S_{t,a}h\|_2\le e^{c_N(a-t)}\|h\|_2. \tag{7.4}
\]

In particular, changing h on a Haar-null set changes `S_(t,a)h` only on a Haar-null set. Density of bounded Borel functions gives the unique L2 extension; the extension agrees with the Borel action on its original domain. Thus representative independence is proved, rather than inferred from the formal generator inequality.

Let h be any L2 class, and approximate it in L2 by continuous functions h_j. Bounds (6.7), (7.4), and convergence for h_j give

\[
 \begin{split}
 \limsup_{e\downarrow0}\|S^e_{t,a}h-S_{t,a}h\|_2
 &\le2e^{c_N(a-t)}\|h-h_j\|_2\longrightarrow0.
 \end{split} \tag{7.5}
\]

This is strong operator convergence on Haar L2 for fixed N, nu, t, a, exactly as stated. It is not operator-norm convergence. No convergence of heat-regularized source potentials was used or established.

The spatial diagonal has product Haar measure zero. Off-diagonal paths never visit it; hence the pointwise Markov action on `E_*` is unchanged by any assigned values there. These two facts separately justify the pointwise and L2 uses of diagonal representatives. They do not define a process started on the diagonal or justify a repeated-label trace in a particle generator.

## 8. Joint strong continuity of the singular two-time evolution

It remains to check both time variables; measurability alone would not suffice. Fix continuous h on E, an off-diagonal q, and a sequence `(t_j,a_j)->(t,a)` in the closed triangle `0<=t<=a<=T`. Use a single Brownian path on `[0,T]` and increments `W_b-W_(starting time)`.

For every fixed smooth spatial cutoff, the solution is jointly continuous in starting state, starting time, and ending time for each continuous driving path. Explicitly, the extra interval created by moving the start has integral drift at most its length times the cutoff bound, and its noise increment tends to zero. On the common interval the initial discrepancy is multiplied by at most the cutoff Lipschitz exponential. Evaluation at the nearby ending time is continuous because the resulting path is continuous. This proof uses only a uniform time bound and spatial Lipschitz constant for that cutoff; continuity of the spatial derivatives in time is unnecessary.

Almost every singular reference path from `(t,q)` stays a positive distance from the diagonal on `[t,a]`. Choose a cutoff which equals the original drift on a neighborhood of that compact path and of the initial state. Its joint continuity shows that, for all sufficiently large j, the perturbed path from `(t_j,q)` to `a_j` stays in the same allowed region, including any short interval added at the beginning or end. For the endpoint `a=T` only intervals inside `[0,T]` are needed. If `t=a`, the argument is simply the short-time cutoff estimate around q. Thus the nearby cutoff solutions equal the singular ones and

\[
 Q_{t_j,a_j}(q)\longrightarrow Q_{t,a}(q)
 \quad\text{almost surely},\qquad
 S_{t_j,a_j}h(q)\longrightarrow S_{t,a}h(q). \tag{8.1}
\]

Bounded convergence over product Haar measure proves L2 convergence for continuous h. Approximating an arbitrary L2 class by continuous h and using the common bound `exp(c_N T)` proves

\[
 \|S_{t_j,a_j}h-S_{t,a}h\|_{L^2(m)}\longrightarrow0
 \quad\text{for every }h\in L^2(m). \tag{8.2}
\]

This includes the boundary `S_(t,t)=I` in L2. The extension's composition property follows either from the bounded Borel Markov property and density or by the same approximation. Thus the singular two-time evolution is jointly strongly continuous and in particular strongly measurable. This completes every assertion in THM-023.

## 9. Independent reconstruction of the abstract response composition

For this section assume exactly the abstract inputs of THM-024, with its constants c, C_R, A_N, B_N. The process and kernels need not come from Sections 2--8. In particular, no actual-data estimate for R is imported. Pair exchange symmetry, diagonal independence, equality-class consistency, and all stated pointwise and Bochner measurability are hypotheses.

For a bounded jointly Borel family v define

\[
 (\mathcal Vv)_t=\int_t^T S_{t,a}R_av_a\,da. \tag{9.1}
\]

The hypotheses make this a jointly Borel family. The sup-norm contraction and bound on R imply the iterated simplex estimate

\[
 \|(\mathcal V^n v)_t\|_\infty
 \le \|v\|_\infty\frac{C_R^n(T-t)^n}{n!}. \tag{9.2}
\]

This follows by n repeated integrations over `t<a_1<...<a_n<T`; its volume is `(T-t)^n/n!`. Therefore the series

\[
 \Phi=\sum_{n=0}^\infty\mathcal V^n U_N \tag{9.3}
\]

converges uniformly in both time and off-diagonal point. Its sum is jointly Borel, terminal zero, symmetric, and satisfies the mild equation pointwise. Interchanging the series and integral follows from this uniform factorial majorant. The bound is

\[
 \sup_{t,q}|\Phi_t(q)|\le B_N e^{C_RT}. \tag{9.4}
\]

If two bounded Borel pointwise solutions exist, their difference w equals `V^n w` for every n; (9.2) tends to zero and proves pointwise uniqueness. This is a uniqueness statement about actual Borel functions, not merely Haar classes.

Because the Haar space has finite measure, every bounded Borel family above takes values in L2. Joint measurability gives strong measurability of this L2-valued map: for example, its coefficients against a countable orthonormal basis are measurable by integration, and finite basis expansions converge in L2 at each time. Consistency of the operator actions and the assumed Bochner integrability identify the same iterates in L2. For n>=1 the composition of their L2 norm bounds has factor

\[
 \prod_{j=1}^n e^{c(a_j-a_{j-1})}
       =e^{c(a_n-t)}\le e^{c(T-t)},\qquad a_0=t.
\]

Consequently, including the n=0 term with the harmless same exponential,

\[
 \|(\mathcal V^nU_N)_t\|_2
 \le A_Ne^{c(T-t)}\frac{C_R^n(T-t)^n}{n!},
 \qquad
 \sup_t\|\Phi_t\|_2\le A_Ne^{(c+C_R)T}. \tag{9.5}
\]

This proves the stated L2 bound for the pointwise solution; it does not replace A_N by the usually larger B_N. Uniform convergence in Borel sup norm implies uniform convergence in Haar L2, so the L2 series and the pointwise series agree as equality classes.

For a strongly measurable L2 mild solution the equation is understood in L2 at each time, with uniformly bounded time norm. If v and w are two such solutions, with difference norm bounded by M, repeated Volterra substitution gives

\[
 \|v_t-w_t\|_2
 \le M e^{cT}\frac{(C_RT)^n}{n!}\longrightarrow0. \tag{9.6}
\]

Thus uniqueness holds in this second class as well. If one formulates the equation only for almost every time, the identical proof gives uniqueness of the corresponding time equivalence class; the Volterra right side supplies its defined mild representative. No assertion identifying arbitrary pointwise values of L2 representatives follows from (9.6).

It remains to identify the true-martingale inverse. For the constructed Phi set `F_a=J_a+R_a Phi_a`. Its absolute occupation is integrable from every starting point: J has that property by hypothesis, and the added source is bounded by `C_R B_N exp(C_R T)`. The mild equation says pointwise

\[
 \Phi_t(q)=\mathbb E_{t,q}\int_t^T F_a(Q_a)\,da. \tag{9.7}
\]

Indeed its J term is U_N, and the bounded response term can be integrated by Fubini through S. Applying the deterministic conditional Markov property, first to bounded sources and then by integrable truncation for J, shows that

\[
 \Phi_a(Q_a)+\int_t^a F_b(Q_b)\,db
 =\mathbb E_{t,q}\left[\int_t^T F_b(Q_b)\,db\,middle|\,\mathcal F_a\right]
 \tag{9.8}
\]

is a true martingale. Conversely, any bounded Borel terminal-zero true-martingale inverse with its own source `J+R v` gives (9.7) with v by taking terminal expectations, hence gives the mild equation and equals Phi by (9.2). This proves the precise probabilistic uniqueness assertion without classical regularity or a singular Itô formula.

Every construction in this section takes place on `E_*`. R's declared independence of diagonal representatives, the process's noncollision, and the assumed Haar equality-class action ensure that the pointwise and L2 interpretations used here are consistent. Those assumptions are indispensable analytic inputs, not conclusions about an unspecified response operator.

## 10. Exact mean-field-centered iid coefficient and density conversion

Let `mu=mu_0` be the probability density in THM-024. It obeys `mu<=M_0` with respect to Haar measure. Therefore, for the generally nontranslation-invariant Phi,

\[
 \|\Phi_0\|_{L^2(\mu\otimes\mu)}^2
 \le M_0^2\|\Phi_0\|_{L^2(m)}^2
 \le M_0^2 A_N^2e^{2(c+C_R)T}. \tag{10.1}
\]

There is no one-density convolution reduction for this general kernel. The factor is squared. Since mu is atomless, changing spatial-diagonal values affects neither this norm nor, almost surely, any distinct-label evaluation among finitely many iid samples.

For precision, rederive the imported THM-015 formula. For a real symmetric L2 kernel Phi write

\[
 \theta=\mu^2(\Phi),\quad
 h(x)=\int\Phi(x,y)\mu(dy)-\theta,\quad
 H_\Phi(x,y)=\Phi(x,y)-\theta-h(x)-h(y).
\]

Then `mu(h)=0` and `int H_Phi(x,y)mu(dy)=0` for mu-almost every x. The campaign statistic is exactly

\[
 \begin{split}
 P_N[\Phi]
 &=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
       -\frac1N\sum_i\int\Phi(X_i,y)\mu(dy)+\frac\theta2\\
 &=-\frac\theta{2N}-\frac1{N^2}\sum_i h(X_i)
       +\frac1{N^2}\sum_{i<j}H_\Phi(X_i,X_j).
 \end{split} \tag{10.2}
\]

Disjoint label sets are independent. Two distinct canonical pair terms sharing one label are orthogonal after conditioning on that label, and they are also orthogonal to every first-projection term. Consequently

\[
 \mathbb EP_N^2=\frac{\theta^2}{4N^2}
       +\frac{\|h\|_2^2}{N^3}
       +\frac{N-1}{2N^3}\|H_\Phi\|_2^2
 \le\frac{N-1}{2N^3}\|\Phi\|_{L^2(\mu^2)}^2. \tag{10.3}
\]

For the inequality use `||Phi||_2^2=theta^2+2||h||_2^2+||H_Phi||_2^2`, `N<=2(N-1)`, and `1<=N-1`. These comparisons hold for every N>=2 and are equalities throughout at N=2. In particular, the deterministic bias is retained; this is not replacement by exact expectation centering.

Multiplying (10.3) by `N b_N`, where `b_N=min(beta_N,1)`, gives the slightly sharper intermediate factor and then the claimed one:

\[
 \begin{split}
 \mathbb E|\sqrt{Nb_N}P_N[\Phi_0]|^2
 &\le\frac{b_N(N-1)}{2N^2}
       M_0^2 A_N^2e^{2(c+C_R)T}\\
 &\le\frac{b_N M_0^2 A_N^2e^{2(c+C_R)T}}{2N}.
 \end{split} \tag{10.4}
\]

Substitution of `A_N^2<=C rho_N` gives exactly the three stated rates. The last exponent is verified algebraically by

\[
 \frac{2s-d}{s+2}-1=-\frac{d+2-s}{s+2}. \tag{10.5}
\]

For the THM-023 range this exponent is strictly negative, including `s=d-2`. If the physical choice is `nu=1/beta_N`, a fixed finite positive nu_* bounds beta_N below by `1/nu_*`; no conclusion uniform down to beta_N=0 is obtained from this base theorem. With nu_*=0, no finite positive beta_N realizes that reciprocal choice. Abstract THM-024 itself applies wherever its hypotheses are supplied by any valid argument. No path supremum, positive-time iid assertion, or evolved-law estimate has entered the proof.

## 11. Independent falsification routes and boundary checks

The constructive route above was challenged through the following separate tests.

1. **Collision sign and dimension.** The harmonic singular test `r^(2-d)` has a negative repulsive contribution and no relative diffusion contribution, exactly as (3.2). This does not rely on the occupation barrier. Reversing the force sign would reverse that term, so the proof cannot accidentally validate attractive collision dynamics. The condition d>=3 is used explicitly in the diverging positive collision test.
2. **Superharmonic endpoint.** The factor in (2.6) is bounded below by `d-s-2`. At `s=d-2` it is still nonnegative and vanishes only at v=1. For larger s it becomes negative near v=1; that unsupported extension is not made. Exact rational sample checks include this endpoint and values on both sides of the L2 threshold.
3. **Periodic cutoff errors.** A direct product-rule check recovers both `-F G chi` and `-4nu grad chi.grad F`. Dropping them would invalidate a periodic claim. The added term `C tau exp(k tau)` pays for them with the explicit constant (4.3). This is also the precise reason this proof's global estimate is bounded-diffusivity rather than all-diffusivity.
4. **Weak time assumptions and zero diffusion.** Only the artificial barrier is differentiated in time. The actual measurable source is used through occupation. Random-flow Jacobians require bounded measurable time coefficients and spatial C1 derivatives, not a time derivative. At nu=0 the same arguments reduce to stopped chain rules and deterministic forced ODEs; no elliptic regularity or zero lateral boundary trace is imposed.
5. **Haar null sets.** The limiting norm estimate is supplemented by the endpoint-measure domination (7.3). Convergence on continuous tests alone would not by itself establish the claimed action on all Borel equality classes. Pointwise diagonal independence and Haar null-set independence are proved separately.
6. **Nontranslation-invariant density conversion.** Take a set A of Haar mass `1/M`, density `M 1_A`, and symmetric kernel `1_(A x A)`, with M>1. Its squared norm is 1 under the product density and `1/M^2` under product Haar. The ratio is exactly M squared; replacing (10.1) by a single factor M is false in general. This test concerns the norm conversion, and is not an assertion that this indicator is an actual corrector.
7. **Centering and small N.** Constants, additive/separable kernels, canonical kernels, and general symmetric kernels on a finite probability space are checked by exact enumeration at N=2,3,4. They recover the bias and first projection in (10.2), equality of the sharp inequality at N=2, and the factor `(N-1)/(2N^3)`. Atomic test spaces validate the algebra only; the endpoint's diagonal-insensitivity claim uses the bounded continuous-space density hypothesis.
8. **Large core at small N.** The core term in (5.5) is treated directly when ell>=R; no finite exceptional set of particle numbers is hidden in the constant. Zero horizon is the zero potential and uses no logarithm. T=0 and C_R=0 also reduce the abstract series and uniqueness proofs to their exact elementary forms.
9. **What the conditional theorem cannot furnish.** Its bounded-response assumption already includes every equality-class and diagonal-consistency issue for R. The proof provides no estimate for an actual singular response, no missing regularity of its data, and no finite-particle singular Itô assertion. Conditional acceptance must remain conditional.

## 12. Per-claim disposition and sealed handoff

| Frozen assertion | Verdict | Supporting lines of this reconstruction |
|---|---|---|
| THM-023 global pathwise uniqueness, joint measurability, and noncollision from every off-diagonal start | Proved in the stated per-start sense | Section 3; stopped bound (3.5) |
| Deterministic-time Markov evolution, exchange symmetry | Proved | Flow construction and (3.6) |
| Integrable absolute source occupation and finite-N bounded potential | Proved | Explicit periodic barrier (4.3)--(4.10) |
| Symmetric bounded Borel signed potential, terminal zero, true-martingale uniqueness | Proved in the declared probabilistic class | Section 5 |
| All-N uniform Haar L2 rates for bounded diffusivity | Proved | (5.3)--(5.6), including large-core cases |
| Positive distributional part of div K, smooth bounded remainder | Proved with the prescribed local normalization | (6.1)--(6.3) |
| Smooth and singular Haar L2 operator norms | Proved, including equality-class consistency | (6.4)--(6.7), (7.2)--(7.4) |
| Strong heat-regularization passage for fixed parameters | Proved | Coupling (7.1) and density argument (7.5) |
| Joint strong continuity in both deterministic times | Proved | Section 8, including the time diagonal |
| THM-024 bounded Borel mild solution, symmetry, terminal zero, uniqueness, sup bound | Proved conditionally on every stated input | (9.1)--(9.4) |
| L2 bound and uniqueness in the distinct L2 mild class | Proved conditionally | (9.5)--(9.6) |
| True-martingale inverse and its uniqueness | Proved conditionally | (9.7)--(9.8) and converse |
| Initial iid coefficient, squared density factor, three rates | Proved conditionally with mean-field centering unchanged | Section 10 |
| Actual-data hypotheses, evolved law, generator domain, singular particle Itô, hierarchy or full mission | Not asserted and not certified | Explicit exclusions throughout |

No exact first unsupported line remains in either frozen assertion when read in its declared scope. The accepted R4 local result has not been promoted beyond its own scope by citation: the periodic process, cutoff comparison, Haar extension, singular passage, and time continuity were proved here. This is an independent statement-only reconstruction, not a hostile review of the unavailable candidate proof and not authority to promote actual-data conclusions.

Reproducible checks are in `ROUND_005_PERIODIC_AND_COMPOSITION_EXACT_CHECK.py` beside this report; its output is `ROUND_005_PERIODIC_AND_COMPOSITION_EXACT_CHECK.json`. The script uses only Python's standard library and exact rational arithmetic. Its checks test identities, signs, cutoff coefficients, finite-N iid normalization, density-factor sharpness, and threshold exponents. They supplement the proofs and do not replace an analytic singular-limit argument.

The input seal is `ROUND_005_PERIODIC_AND_COMPOSITION_INPUT_SHA256SUMS.txt`; the output seal is `ROUND_005_PERIODIC_AND_COMPOSITION_OUTPUT_SHA256SUMS.txt`. The latter records this immutable issued report, the exact-check script and result, and the copied input seal. Its own bytes are not recursively included. All copied input hashes are rechecked at issue. Verification commands and actual outcomes are recorded in the companion exact-check JSON and the final handoff. A direct format check covers newly untracked outputs in addition to `git diff --check`.

Executed verification: `python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_005_PERIODIC_AND_COMPOSITION_EXACT_CHECK.py` passed 4,536 radial cases, 4,536 cutoff product-rule cases, 1,344 all-N radial-core/nonlogarithmic-tail cases, 96 pair-divergence cases, 468 exact iid configurations in 12 law/kernel cases, 3 sharp density-factor cases, 56 rate-exponent cases, and 13 Volterra coefficient cases. `shasum -a 256 -c AUDITS/ROUND_005_PERIODIC_BLIND_INPUT_SHA256SUMS.txt` passed all eight frozen inputs. `git diff --check` passed. At issue, a direct scan of the new report, script, and JSON verified terminal newlines, absence of trailing whitespace and control characters, and balanced standalone mathematical display fences in the report. The copied input seal and final output seal were also checked with `shasum -a 256 -c` after creation. No failed analytic check or mathematical defect was found in this lane.

No TeX or PDF was created in this lane: the required artifact is this Markdown report, and the final human-facing handoff contains no mathematical LaTeX. No canonical state file or other worktree was edited. The next authorized action belongs to root: compare this sealed reconstruction against the separately sealed constructor and hostile-review outputs, while keeping conditional and actual-data gates distinct.
