# AUD075 — isolated reconstruction of the whole frozen THM052

Issued 2026-09-18 UTC. TASK117. Auditor context: `/root/r027_duality_blind`, fresh Astra Ultra, isolated task-bound reconstruction. Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r027-duality-blind`. Provisioned base: `ef438b612f732d21af1fa1756dd7559ef63c6d61`. Evidence packet: `ROUND_027_DUALITY_BLIND_ARTIFACTS_AUD075_20260918_094707_UTC`.

**Whole verdict: independently reconstructed, all of THM052(A)–(C), within exactly the frozen finite-parameter scope.** The attractive lifetime law and the full conditional reversed path law follow from a local flow change of variables, with collision-free domain killing retained on both sides until the last passage. The needed conservative repulsive realization is reconstructed below. There is no unresolved mathematical line in this frozen conjunction. This is the isolated reconstruction axis; root comparison, any separate hostile audit, canonical promotion and integration remain root decisions. No critical decay, positive-limsup witness, fluctuation limit, gradient-domain regularity or wider preparation class is established.

All eight frozen hashes passed before mathematical work and again when their exact bytes were copied. No current root derivation, current R26 route, current audit narrative, canonical STATE/history, memory file, other worktree, external source, linked nonallowlisted source or prior verifier was read. The source and exposure ledger records the initial large tool-output truncation and the later targeted, untruncated reads. Earlier source labels and their audit status are not premises.

## 1. Exact assertion and logical negation

Write M=(T^4)^N, m=product Haar of mass one, Omega=M minus the pair collision diagonals. Fix each integer N>=2 and each real finite nu>0 separately. Fourier characters are exp(2 pi i k.x). The kernel has g_hat(0)=0 and g_hat(k)=|k|^(-2) for nonzero k. Define

    H(x)=(1/N) sum_(i<j) g(x_i-x_j),
    c=4 pi^2,       kappa=c(N-1),
    b_-(x)=-grad H(x),       b_+(x)=+grad H(x).

The noises in the 4N coordinates are independent standard Brownian coordinates, multiplied by sqrt(2 nu). In particular the diffusion generator is nu Delta, not nu Delta/2. The repulsive process X is the actual maximal local solution with drift b_-, shown below to be conservative from every deterministic x in Omega. The attractive process Y is the unique maximal local solution with drift b_+, of lifetime zeta in Omega; it is sent to an absorbing cemetery state at and after zeta. An initial Haar point is independent of the Brownian path. Every finite-parameter assertion here allows constants or probability-one sets to depend on N, nu and the fixed horizon. There is no uniform-in-N conditioning estimate.

The target is the conjunction of:

* For every finite t>=0 and all bounded nonnegative Borel f,h on Omega,

      integral f P_t h dm = exp(kappa t) integral h Q_t f dm,
      Q_t f(x)=E_x[f(Y_t) 1_(t<zeta)].

  This extends complex linearly to bounded signed/complex f,h. The Haar-start repulsive law has actual density exp(kappa t)Q_t1<=exp(kappa t). The Haar-start attractive terminal subprobability is exp(-kappa t)m; therefore P_m(zeta>t)=exp(-kappa t), and its survivor marginal is exactly m.
* For every finite T>=0, the Haar-start law of X on C([0,T],M), with its uniform topology, equals the reversal of the Haar-start attractive law conditioned on zeta>T, including all finite-dimensional products and every bounded Borel full-path functional. At T=0 this means equality of the initial Haar laws.
* For every bounded complex Borel configuration observable F and complex A,

      E_rep |F(X_T)-A F(X_0)|^2
      =E_att[|F(Y_0)-A F(Y_T)|^2 | zeta>T].

  For the displayed frozen Fourier statistic and response factor, equality remains exact after multiplication by N, and hence preserves the zero-limit and positive-limsup criteria along the frozen critical sequences. The conditional expectation keeps the exact survival normalization exp[-c(N-1)T].

The exact logical negation is an admitted finite N, finite positive nu, time/horizon or bounded datum for which any included existence/domain/normalization/identity clause fails, or a failure of equality of the specified path measures, or of the specified scalar defect and sequence criterion. It is not merely failure of an estimate uniform in N, or failure for a non-Haar initial law. The construction below rules out the stated negation. The unopened THM049 source is not a premise: the modal quantity meant here is the expression explicitly frozen in the THM052 card, and its original response orientation is checked against the allowed R1 and R4 formulas.

## 2. Source and normalization preflight, reconstructed

The eight permitted files are copied under INPUTS in the packet, with their exact original relative paths. The mathematical inputs used are the frozen model/card, the R1 definition of the response operator, the R4 heat representation and divergence calculation, and the R6 local cutoff/energy mechanism. The latter mechanisms are rederived here in this specialization rather than imported by theorem label. No linked R3/R5 report, THM021, THM049, code/result file or outside reference is used.

Let p_u be the periodized four-dimensional Gaussian heat kernel. Direct Gaussian integration gives its Fourier coefficients exp(-4 pi^2 u|k|^2), mass one and positivity. Define

    g(z)=4 pi^2 integral_0^infinity [p_u(z)-1] du.

This integral converges in L1: on (0,1), ||p_u-1||_1<=2, and on [1,infinity), the nonzero Fourier modes and their spatial derivatives decay exponentially. Its nonzero Fourier coefficient is

    4 pi^2 integral_0^infinity exp(-4 pi^2 u |k|^2) du=|k|^(-2),

and its mean is zero. Off z=0 the small-time nonzero lattice terms decay faster than every power of u; differentiating their integral is justified on compact sets. Subtracting the Euclidean Gaussian integral gives

    4 pi^2 integral_0^infinity (4 pi u)^(-2) exp[-|z|^2/(4u)] du=|z|^(-2),
    g(z)=|z|^(-2)+h(z) near 0, with h smooth.

For the smoothness of h, split the integral at u=1. The nonzero lattice terms at small u have Gaussian off-diagonal bounds for every derivative; the subtracted constant is integrable; at large u the differentiated Euclidean Gaussian has an integrable u^(-2) bound or better, and the torus remainder decays exponentially. Thus g is smooth away from zero, tends to positive infinity at zero and is bounded below by a finite number g_*. Also g and its gradient are integrable in dimension four; near zero their orders are r^(-2) and r^(-3), against r^3 dr. No logarithmic normalization is used.

The Fourier coefficients identify the distributional Laplacian exactly:

    -Delta g=c(delta_0-1),       c=4 pi^2.

This also follows from the local flux of K=-grad g=2z/|z|^4-grad h: its limiting flux is 2|S^3|=4 pi^2, where |S^3|=2 pi^2. The background has mass -c, forced to be the constant -c by the Fourier normalization. In particular

    Delta g=c on T^4\{0}.

The collision atom has not disappeared. On the full product torus, in distributional notation with delta_(ij) defined by Haar integration after setting x_i=x_j,

    Delta_M H = kappa m -(2c/N) sum_(i<j) delta_(ij).

Each unordered pair contributes derivatives in both particle coordinates; there are N(N-1)/2 pairs. On Omega this yields precisely

    Delta_M H=(2/N) [N(N-1)/2] c=c(N-1)=kappa,
    div b_-=-kappa,       div b_+=+kappa.

The singular measure above is not inserted into an Itô formula along a trajectory, and the punctured divergence identity is never asserted as a global smooth identity on M. The diagonal has Haar mass zero, but its flux has not been set to zero. Killing at the boundary in the construction below encodes its effect.

## 3. Both local processes and the actual conservative repulsive domain

For sufficiently large integers m, put D_m={x: min_(i<j) dist(x_i,x_j)>1/m}. Empty early domains are harmless. These are increasing open sets with closure compact in Omega and union Omega. No smoothness of their boundaries is needed. Choose a smooth periodic cutoff equal to one on a neighborhood of closure(D_m), vanishing sufficiently close to every collision, and multiply b_- by it. The resulting globally smooth vector field b_-^(m) on M is globally Lipschitz; put b_+^(m)=-b_-^(m). This construction does not differentiate torus distance at its cut locus.

For every continuous driving path w with w(0)=0, solve in Euclidean lifts

    x_t=x_0+integral_0^t b_±^(m)(x_s) ds+sqrt(2nu) w_t,

and then project to M. Subtracting the continuous additive signal reduces this to an ordinary nonautonomous integral equation with a uniform Lipschitz constant. Picard iterates converge on compact time intervals by the factorial bound on successive differences; Gronwall gives uniqueness and continuous dependence. The map is jointly Borel in initial point, w and t, and depends only on the signal up to t. Integer changes of lift give the same torus path.

Solutions using different cutoffs agree until exit from the smaller domain. Patching them constructs the maximal local solutions in Omega for b_- and b_+, their increasing exit times and their lifetimes tau_- and zeta. Survival to a fixed time is Borel, because for continuous paths the infimum of distance to a closed set over a compact interval is measurable, and a countable exhaustion is used. If a maximal solution stays in a collision-excluded compact set up to a finite endpoint, the bounded drift integral and continuous signal have limits; the limiting state remains in Omega, and a finer cutoff continues it. Thus finite lifetime can only arise through failure of compact containment near the collision set. This does not assume an attractive path has a collision limit at its lifetime, and no such claim is needed.

For repulsion define the nonnegative energy

    E(x)=H(x)-(N-1)g_*/2
        =(1/N) sum_(i<j) [g(x_i-x_j)-g_*].

Every energy sublevel is compact in Omega: if any pair collides, its own nonnegative summand diverges, and the other summands cannot cancel it. This covers simultaneous and partial collisions. Let sigma_R be the first exit above energy R, with value zero if the start is already above R. Up to this stop the energy and its required derivatives are bounded. Smooth stopped Itô calculus gives

    E(X_(t∧sigma_R)) + integral_0^(t∧sigma_R) |grad H(X_s)|^2 ds
      = E(x)+nu kappa (t∧sigma_R)+M_R(t),
    <M_R>_t=2nu integral_0^(t∧sigma_R) |grad H(X_s)|^2 ds.

The stopped martingale is square integrable, with expectation zero. No individual-force-square estimate or sign assumption on triple cross terms is used: it is the full nonnegative squared gradient. Therefore

    P_x(sigma_R<=T) <= [E(x)+nu kappa T]/R.

The increasing sigma_R exhaust tau_- by the continuation argument. Taking R to infinity proves P_x(tau_-<=T)=0. Taking integer T proves a global collision-free continuous solution from every prescribed x in Omega. Local uniqueness proves pathwise and law uniqueness. In particular every one of these paths has a positive minimum pair separation on each finite closed time interval. This is the actual conservative repulsive realization referred to in THM052, rather than a separate smooth model or an assumed weak generator solution.

For both signs, restarting the jointly measurable local construction at deterministic time s agrees with solving from the current state with the Brownian increments after s. Those increments are independent of the past. On attraction, restart is performed only on s<zeta, and the residual lifetime is the restarted lifetime by local uniqueness. This proves the Markov and semigroup properties of P and the absorbing sub-Markov Q. The existence of the attractive killed family does not require proving a global attractive solution. Each starting x in Omega has zeta>0 by local existence. The probability-one nonexplosion set for repulsion need not be common to all initial points; pointwise nonexplosion and joint measurability are sufficient for every later integral.

## 4. Finite-domain change of variables with all boundary killing retained

Fix finite T>0, one domain D_m and one continuous signal w. Let Phi^-(x,w) be the repulsive path on [0,T] when that path stays in D_m; let U_(m,T)^-(w) be the set of such initial points. The initial point and all endpoints are included in the condition. The set is open: a path with image in D_m has compact image and hence positive distance from its complement, and the cutoff flow depends continuously on the initial point. Define U_(m,T)^+(v) analogously for attraction.

Define the reversed signal

    (R_T w)_s=w_(T-s)-w_T,       0<=s<=T.

It starts at zero. If x_s is any surviving repulsive path and y_s=x_(T-s), subtract its integral equation at T and T-s to obtain exactly

    y_s=y_0+integral_0^s grad H(y_r) dr+sqrt(2nu) (R_T w)_s.

Thus it is the attractive path driven by R_Tw. It stays in the same domain for all s. Reversing again proves the converse and proves that

    x -> Phi^-_T(x,w)

is a bijection from U_(m,T)^-(w) onto U_(m,T)^+(R_Tw), with inverse y -> Phi^+_T(y,R_Tw). This is a statement before averaging the noise. The minus sign and reversal in R_Tw are both necessary for this fixed-signal inverse statement.

Differentiate the smooth cutoff flow in x. Its derivative J_t solves the ordinary variational equation

    dJ_t/dt=Db_-(Phi^-_t) J_t,       J_0=I,

along a surviving trajectory. The noise is additive, so there is no noise derivative or extra Itô correction here. Backward uniqueness supplies an inverse derivative. Differentiating its determinant gives

    det J_T=exp(integral_0^T div b_-(Phi^-_s) ds)=exp(-kappa T)>0.

Hence the endpoint map is a C1 diffeomorphism between the two open survivor sets, with this constant Jacobian. The differentiability can be obtained directly from the difference quotients of the cutoff integral equation and Gronwall, so no singular flow theorem is being invoked.

Let Psi be any bounded Borel functional on C([0,T],M). By ordinary change of variables on those open sets,

    integral_(U^-_(m,T)(w)) Psi(Phi^-(x,w)) dm(x)
      = exp(kappa T)
        integral_(U^+_(m,T)(R_Tw)) Psi(reverse Phi^+(y,R_Tw)) dm(y).       (4.1)

Manifold change of variables follows by finite coordinate charts and a partition of unity, or by periodic lifts. Neither side integrates over a collision boundary. Both sides retain their domain-exit kill over the entire interval, including intermediate times. Cornered domain boundaries cause no boundary term: this is a volume substitution, not integration by parts on the boundary.

For standard 4N-dimensional Brownian W on [0,T], R_TW has the same Wiener law. Indeed it is centered Gaussian and continuous; in each coordinate its covariance is min(s,r), as seen by intersecting the reversed increment intervals. Disjoint reversed increments are independent and different coordinates remain independent. This establishes the law statement without treating R_TW as Brownian in the original forward filtration. It is Brownian in its own time parameter, which is all the attractive construction requires.

Average (4.1) over Wiener measure. Joint measurability permits Fubini, and boundedness makes all integrals finite. Since R_T preserves Wiener measure, this gives

    E_m[Psi(X_.); X_[0,T] subset D_m]
      =exp(kappa T) E_m[Psi(reverse Y_.); Y_[0,T] subset D_m].             (4.2)

These are still the actual local paths before exit, not solutions to an altered boundary equation. In particular (4.2) proves the full finite-domain duality with both auxiliary kills visible.

## 5. Remove precisely the auxiliary domain kills

For either sign and every continuous signal, the union over m of the events “path stays in D_m throughout [0,T]” is exactly “maximal lifetime >T.” In one direction a domain-surviving path is in a compact subset of Omega and continues past T. In the other, a path existing past T has compact collision-free image on [0,T], so it stays in some D_m. Equality at the lifetime is therefore handled correctly: the event is T<lifetime, not T<=lifetime.

On a surviving event the cutoff paths for all sufficiently large m coincide with the maximal path throughout [0,T]. Thus indicators increase to the correct survival indicator, and bounded Borel path-functionals can be passed by bounded convergence. Nonnegative unbounded path-functionals could be handled by monotone approximation, but are not required. At paths killed by time T the products with the indicator converge to zero; no value of Psi on an incomplete path is needed.

The repulsive lifetime is infinite almost surely for each initial x. Integrating this fact against m is legitimate by the measurability already proved. Passing m to infinity in (4.2) gives the decisive full-path equality

    E_m^rep Psi(X_.)
      = exp(kappa T) E_m^att[Psi(reverse Y_.); zeta>T]                      (5.1)

for every bounded Borel Psi on C([0,T],M). This removes only the auxiliary finite-domain killing. It retains exactly the genuine attractive lifetime killing. No missing collision atom is compensated by an unexplained correction: the local divergence and the lost range of the forward map account for the boundary flux. In particular there is no global assumption that a singular repulsive flow is onto Omega.

For completeness, the actual full repulsive path map can be made Borel into C([0,T],M) by assigning an arbitrary continuous path on its null explosion event; evaluations at rational times are Borel and determine the Borel structure of this separable uniform path space. On the attractive survival event the same construction gives an actual continuous path. After conditioning on zeta>T this is a probability law on that space. Reversal is a continuous map of that uniform space. Thus (5.1) concerns the asserted full path measures, not merely a formal cylinder functional.

At T=0, each x in Omega has both local lifetimes strictly positive, the flow and reversal are the identity, the determinant is one, and (5.1) reduces to the initial Haar identity. This separately handles the degenerate horizon.

## 6. Deduce every clause of (A) and (B)

Set Psi(path)=f(path(0))h(path(T)) in (5.1). Conditioning initially on x yields

    integral f(x)P_T h(x) dm(x)
      =exp(kappa T) integral h(y)Q_T f(y) dm(y).

Every bounded Borel f,h on Omega can be extended by zero over M\Omega, which is Borel and Haar-null. The two sides only evaluate these observables at collision-free states. The identity for nonnegative functions follows first; decomposing real and imaginary parts gives bounded signed and complex versions. Every integral is finite. The product is bilinear, with no hidden complex conjugation; conjugates can be included explicitly in the test functions when desired.

Set f=1. Then, for each bounded nonnegative h,

    E_m^rep h(X_T)=integral h(y) exp(kappa T)Q_T1(y) dm(y).

The right side defines an actual Borel density, modulo the usual m-null ambiguity. Because Q_T1 is a survival probability, it lies in [0,1], giving the stated pointwise-a.e. density bound. Its mass is one by repulsive conservation. There is no prior assumption of an actual evolved density.

Set h=1 and use P_T1=1. Then

    integral Q_T f dm=exp(-kappa T) integral f dm.                         (6.1)

For f=1 this yields P_m^att(zeta>T)=exp(-kappa T). The lifetime is positive almost surely and finite almost surely: the survival function equals one at zero and tends to zero at infinity. It is exactly the exponential distribution with rate kappa, with no atom at any finite time or at infinity. Dividing (6.1) by its strictly positive mass gives exactly the product-Haar current configuration conditional on survival. These conclusions are only for Haar start; no deterministic-start exponential survival law or marginal claim is inferred.

Finally apply (5.1) with Psi=1 to supply the same normalization and divide the right side of (5.1) by P_m(zeta>T). This proves (B) for every bounded Borel path functional. Equality for all such functions is equality of probability measures on C([0,T],M). As a check, for any grid 0<=t_0<...<t_r<=T and bounded Borel psi_j, choosing Psi=product_j psi_j(path(t_j)) gives the full finite-dimensional product identity with every evaluation time reversed. Evaluation maps are continuous on this path space; their rational-time cylinder sigma-field is its Borel sigma-field. Thus even a cylinder-only derivation would extend to this topology, but (5.1) has already proved the stronger functional statement directly.

There is no inference that X_T is Haar for T>0. In (B), X_0 corresponds to the survivor endpoint Y_T, whereas X_T corresponds to the survivor starting point Y_0. The latter is biased by survival. This orientation distinction is detected by an exact mutation test below.

## 7. Clause (C), the original response sign and rare conditioning

For bounded complex Borel F and A in C, use the bounded Borel path functional

    Psi(path)=|F(path(T))-A F(path(0))|^2.

Its bound is ||F||_infinity^2(1+|A|)^2. Under reversal it becomes

    |F(Y_0)-A F(Y_T)|^2,

with A unchanged. There is no conjugation of A induced by time reversal. This proves the exact scalar identity in (C).

The original allowed R1 response convention is

    (A_lin phi)(y)=integral K(x-y).grad phi(x) dx

when the mean-field background is unit Haar. R4 identifies div K=c(delta_0-1). Integration by parts with this finite signed measure gives

    A_lin phi(y)=-c phi(y)+c integral phi.

For phi_k(x)=exp(2 pi i k.x), k!=0, the mean is zero, so this is -c phi_k. Equivalently, the integrated Fourier mode is K_hat(-k)=+2 pi i k/|k|^2, whose product with 2 pi i k is -4 pi^2. Also K*1=0 and nu Delta phi_k=-nu c|k|^2 phi_k. Thus the actual frozen linearized one-body response operator has eigenvalue

    -(c+nu c|k|^2).

The response factor is therefore exactly A_T=exp[-(c+nu c|k|^2)T], with the original dissipative orientation. No attractive response sign is substituted. The configuration statistic F_N(x)=N^(-1)sum_i phi_k(x_i) is bounded by one, and its Haar mean is zero. The THM052 modal expression is exactly

    D_N(T)=N E_rep |F_N(X_T)-A_T F_N(X_0)|^2
          =N E_att[|F_N(Y_0)-A_T F_N(Y_T)|^2 | zeta>T]
          =N exp[c(N-1)T]
             E_att[|F_N(Y_0)-A_T F_N(Y_T)|^2 1_(zeta>T)].                (7.1)

These equalities hold at every admitted finite N, nu and T. Consequently along beta_N/sqrt(N)->lambda in (0,infinity), with nu_N=1/beta_N, the two displayed nonnegative sequences are identical term by term. Their limits vanish together and their limsups, finite or infinite, coincide. This is a criterion equivalence, not evidence that either criterion holds. For fixed T>0, the survival probability tends to zero exponentially in N; deleting the normalization in the last line of (7.1) is incorrect. At T=0, A_0=1 and both modal defects vanish identically.

## 8. Independent falsification route and exact fresh diagnostics

The construction above uses local flow inverses. A separate direct adjoint check, for compactly supported smooth f,h inside Omega, gives

    integral f L_- h dm
      =integral h [nu Delta f+grad H.grad f+kappa f] dm.

This recomputes the drift and divergence sign independently. It does not prove the theorem because it alone specifies no boundary behavior. Applying it indiscriminately on all of M would lose the singular diagonal flux identified in Section 2. That potential counterargument fails precisely because the killed domain and volume range are retained in the proof.

A second falsification attempt uses a solvable killed interval flow. In normalized Lebesgue measure on (-1,1), a repulsive diagnostic step is x->x/2+epsilon/4, epsilon in {-1,1}; all forward steps stay in the interval. This is the exact sampled solution of an affine ODE with constant slope forcing on each subinterval. For the reversed signal the attractive step is y->2y+epsilon/2 with all exits killed. Reversing and negating the forcing associates each original path to its inverse. The signs are exhaustively averaged, independently and equally. This is not a simulation of Coulomb diffusion; it is an exact finite-dimensional test of Jacobian, absorption, noise reversal, endpoint orientation and conditioning. It can refute erroneous algebraic versions of the proposed mechanism.

The fresh standard-library `diagnostics.py` performs 322 exact rational checks with no tolerance, random seed, Monte Carlo or imported checker. Its baseline passes all 322. It includes:

* independently differentiated local four-dimensional pair-energy jets for N=2,3,4,6, using g_local(z)=|z|^(-2)+(c/8)|z|^2 and rational c=7/3; their full 4N-coordinate Laplacian is c(N-1), and their coordinate gradient equals the explicitly assembled pair gradient;
* the independent Ito quadratic-variation factor and the original Fourier response sign;
* fixed-signal inverses, before symmetric noise averaging;
* exact killed survival masses through four steps and survivor endpoint moments of orders zero through four;
* all 243 time-ordered polynomial cylinders with degrees 0,1,2 at each of five sampled times;
* an asymmetric complex response factor and a genuinely complex observable, checking the squared endpoint defect with its correct ordering;
* an excursion that exits at an intermediate time but returns by the terminal time, demonstrating why endpoint-only killing is wrong;
* the signed-permutation covariance check for reversed independent Gaussian increments.

The local jet model is only a differential normalization diagnostic; its quadratic compensation is not a globally periodic Coulomb kernel. The interval model and Gaussian covariance checks do not certify continuum domain passages, Brownian lifetimes or path topology. Those are proved analytically in Sections 2–6. The direct formal adjoint check likewise has only its explicitly compact-support scope.

Nine separate semantic mutant executions are required to terminate nonzero and to contain at least one exact failed assertion. They alter the pair factor, collision compensation, diffusion factor, fixed-signal noise sign, endpoint orientation, rare-survival normalization, intermediate-time killing, response sign and time order. Every mutant exits 1 and is detected. All outputs, including empty stderr files, are retained; `mutation_summary.json` records each exact count. No failed baseline run occurred. A dormant conditional expression in the initial script draft was simplified before its first execution; this changed no executed baseline result. These diagnostics are self-checks of this fresh audit construction and are not a second independent auditor.

## 9. Clause and exposure disposition

| Frozen obligation | Disposition | Proof location |
| --- | --- | --- |
| coefficient-one d4 Fourier/local/atom normalization | reconstructed | Section 2 |
| all finite N>=2, finite positive nu, unit Haar, deleted collision domain | retained exactly | Sections 1–3 |
| actual conservative repulsive realization | reconstructed from local stops and energy | Section 3 |
| killed attractive measurable semigroup and maximal lifetime | constructed | Section 3 |
| exact finite-domain duality with no suppressed boundary kill | proved | Section 4 |
| removal of auxiliary kills, true attractive kill retained | proved | Section 5 |
| bounded Borel and signed/complex extension | proved | Sections 5–6 |
| actual repulsive density and bound | proved | Section 6 |
| exact exponential lifetime, no atom, survivor product Haar | proved for Haar start | Section 6 |
| every finite horizon, T=0, full uniform-topology path law | proved | Sections 5–6 |
| endpoint defect and complex orientation | proved | Section 7 |
| original modal response coefficient, N normalization, critical criterion | proved as exact equivalence | Section 7 |
| rare survival factor | retained exactly | Section 7 |
| actual critical decay or witness | not asserted and not proved | outside frozen target |
| THM049 nonallowlisted source text | not read or used | frozen displayed definition only |

The entire frozen assertion is reconstructed; no counterexample to it was found. The scalar and path identities have a full local-domain proof rather than an unresolved adjoint-domain inference. The conclusion does not change the original scientific mission or establish any broader fluctuation theorem. Root must compare this independently issued report with the separate whole-claim audit before assigning campaign status.

## 10. Deliverables, verification and limits of issuance

Only the assigned report, the uniquely named evidence directory, and their named sibling archive/seals are written. The eight sources and their repository originals remain byte-identical. No canonical state file, cumulative memorandum, external source, dependency, Git history, branch, remote or pre-existing file is changed. No commit, push, merge, child agent, outside consultation or network source is used. The initial worktree contained only the three expected untracked provisioning files: the frozen manifest, the task card and THM052; the tracked diff was empty. The report is copied byte-for-byte into the packet before issuance.

The packet includes this report, eight exact inputs, both input inventory formats, fresh diagnostic source and all results, the complete source/read/exposure history, command history, README, a complete regular-member inventory with SHA-256 digests, and a portable standard-library read-only verifier. Named sibling inventory/digest/seal files cover the entire packet including its verifier and internal inventory files; the complete archive contains regular files only under one safe top-level directory, with no links or unsafe paths. The archive is checked by inspecting members and hashing streams without extracting. The verifier also rejects missing, extra, altered, nonregular or unsafe packet members, verifies source seals and the report mirror, and reruns no arbitrary code by default. An explicit optional diagnostic switch runs only the known packaged checker, with bytecode writing disabled, and checks the baseline plus all mutant return codes. Read-only permission bits are applied at issuance; hash sealing, rather than permission bits alone, supplies tamper evidence.

Verification outcomes and portable verifier tamper rejections are in `VERIFICATION_RESULTS.json` and the sibling verification output. No TeX was edited or produced: the permitted authoritative report is Markdown and the final handoff contains no mathematical LaTeX. Mathematical correctness rests on the explicit proof above; compilation and diagnostic success are not substituted for it.
