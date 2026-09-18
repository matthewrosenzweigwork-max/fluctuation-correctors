# Assumptions and constants ledger

No theorem may use an unnamed “regularity constant” or “uniform constant.” Add one row per theorem/lemma.

| ID | Object | Exact assumption | Constant/symbol | Depends on | Uniform in | Status |
|---|---|---|---|---|---|---|
| AC-001 | mean-field density | smooth and strictly positive on \([0,T]\) | \(m_T,M_T\) | initial data, potential, kernel, temperature, \(T\) | not assumed | explicit smooth hypothesis only |
| AC-002 | backward one-body propagator | regularity sufficient for tested commutator | \(C_{T,k}\) | mean-field trajectory | \(N\) | OPEN |
| AC-003 | pair propagator | smooth data and displayed finite norms | c_m(t), A_m | d,m,T, ||K||C^m, ||b||C^m, ||grad mu||L1, forcing | N>=2, nu>=0 conditional on those uniform norms | PROVED_CANDIDATE THM-009 |
| AC-004 | k-body propagator | order-uniform or quantified growth | \(C^{(k)}_T\) | \(k,T\), cutoff | \(N\) | OPEN |
| AC-005 | local static response | moving-background uniformity | \(C_{\mathrm{stat}}\) | law, \(\lambda\), density | \(N,t\) | OPEN |

For every constant state:

- whether it depends on \(s,d,T,\lambda\), density lower/upper bounds, confinement, test norms, corrector order, and regularization;
- whether dependence is polynomial, exponential, factorial, or unknown;
- whether the dependence permits summation at criticality;
- whether it is stable at endpoints and under cutoff removal.


## Round 001 frozen hypotheses

AC-001 is an explicit smooth-positive finite-horizon reference hypothesis; uniform bounds across beta_N and cutoff are not proved. At fixed smooth g all derivatives needed by Ito and integration by parts are finite. The planned pair propagator estimate must display dependence on the C^m norms of K,b, the time-uniform L1 norm of grad mu, time horizon, and forcing; uniformity in N or diffusivity is conditional on these quantities being uniform. No symbol hides epsilon dependence.

The THM-009 solution constant is exponential in the time integral of c_m(t), as recorded in OP-002 and smooth report (1.1)–(1.7). Source J_f costs d 2^{m+1} kappa_m ||f||_{C^{m+1}}. No density lower bound enters this analytic constant; it uses probability mass and ||grad mu||L1. No corrector-order summability or endpoint singular uniformity is established. The heat-cutoff derivative and source divergence are explicit in REG-001.

## Round 002: AC-006 fixed-smooth residual constants

THM-010 uses q=floor(d/2)+2, Sobolev lattice sums B,D, and R=2*3^(7/6)*B*(1+D*Kcal*h_L(T)), L=d(v_1+2*kappa_1), as explicitly defined in ROUND_002_COUPLING.md (2.1)-(2.4). Tensor estimates require pair derivatives through 3q+1 and one-body C^1, within the frozen 4d+12 hypothesis. Constants have no N,beta or hidden background-derivative dependence. The root lemma ROUND_002_UNIFORM_SMOOTH_DATA.md supplies explicit bounds (D1)-(D3) for the existing smooth solution/test family from fixed smooth data; it is separately submitted for hostile review. Neither result gives cutoff or corrector-order uniformity.

Round 002 review update: AUD-006 now grants HOSTILE_REVIEW_PASS for the bounded residual estimates, fixed-data norm qualification and Gibbs law-class obstruction in the precise scopes above. The singular and other open interfaces are unchanged.

## Round 002 final integration

Round 002: THM-013 constants C_mu,m and C_f,m are displayed in the viscosity proof, independent of both nonnegative diffusivities, with two additional spatial derivatives. The response difference requires only the density supremum difference. The maximum-norm/symmetrization convention in THM-014 retains all THM-012 numerical bounds; unrestricted first-slot differentiation is false. Covariance continuity uses no inverse diffusivity and no nondegeneracy. Positive-diffusivity smooth mean-field existence remains an explicit model input.

## Round 003 constants and their exact scope

AC-007, THM-015: arbitrary probability mu, symmetric L2(mu^2) pair kernel, iid labels. Exact norm constant (N-1)/(2N^3), sharp uniformly over admissible laws/kernels; all N>=2. Haar heat constants depend on fixed d,s and the displayed cutoff interval, not N or beta. Explicit max-shell constants and epsilon_0=(8 pi^2 d)^(-2) appear in the pair proof; no uniformity as s approaches thresholds is asserted.

AC-008, THM-016/018/019: iid Haar, fixed d and 0<s<d, b_N=min(beta_N,1). Heat-representation remainder bound M_ds, outer-region squared integral G_ds and explicit radial integrals determine every truncation constant. For the sharp lower bound (d/2<s<d), choose one delta>0 with delta^-s>=2 C_tau and delta^(2s-d)<=c_0/(64 C_V), c_0=v_d/[4(1+v_d/2)]. Then a=delta^-s/8 and p=c_0 delta^d/2 are independent of N and temperature. Bounds apply beyond a fixed geometric N threshold. Proof/audit dispositions are separate.

AC-009, THM-017: fixed d,s,A,T, fixed embedded radial cutoff and iid density bound M. Local two-sided constants use H_s(u)=(1+u^(s+2))^(2/(s+2))-u^2, angular squared norm Q(A), and the explicit radial integrals. All initial endpoint constants are independent of N, beta and deterministic remaining time; no singular full-operator norm or stochastic time supremum follows.

## Round 004 local constants

THM020 freezes d>=3,0<s<=d-2,N>=2,finite nu>=0,T,constant symmetric A. Source/radial comparison factor1 is independent of N,nu,annular radii; supremum amplitude grows N^(s/(s+2)) at fixed T. The iid endpoint constant depends only on fixed d,s,T,A,density bound and cutoff. Independent all-N addendum A.2 gives explicit constants and handles T=0 separately. Exit bounds may depend on fixed N and nu; they are not uniform process tightness as nu tends to infinity.

Round004 THM021 requires d>=3,0<s<=d-2 and prescribed C1 probability density with common M0,M1; Haar response estimates require no positive lower bound. Smooth-flow existence is for each fixed cutoff; propagation constants use only the lower divergence and response norms, not high cutoff derivatives. Range obstruction THM022 fixes 0<a<|z0|<R<infinity,N>=2,nu>0; its small positive time depends on the entire fixed tuple. R5 adds prescribed uniform C1 u/C2 f and bounded nu interval; none is yet established for actual campaign data.

Round005 complete module comparisons allow different finite barrier constants: constructor uses alpha=1+sL and an O(tau) cutoff error; reconstruction bounds that error uniformly over the fixed horizon and uses exp(sL tau). Both retain4nu gradchi.gradF, boundednu and all-N core cases. No equality of their realized barriers is claimed. At the full interface choose one common lower-divergence constant dominating both the response lower bound and THM023's C0, or use C0 directly; source-location qualification is pending exact addendum.

R5 interface source/constant repair passed TASK047: kappa=max(kappa21,C0_23) is independent of N and bounded nu; singular propagation exponent <=D_u+kappa/2. C0_23 is the THM023 compensation norm, not the response bound called C0 in the R4 source. Both C_R response terms and M0^2 remain unchanged. THM027 strengthens prescribed mu to C2 and f to C3 explicitly, keeps u C1, and seeks fixed-N bounds only; no actual inhomogeneous norm assertion.

THM026 audited constants: C_N=N a+(N-1)kappa, energy shift subtracts Nv_*+(N-1)g_*/2, E>=0 and locally E>=(delta^-s-A)/N. Exit probability <=N(J0+nu C_NT)/(rho^-s-A). Heat comparison depends on the realized minimum distance; density costs ||F0||infty exp(C_Nt), iid factorM^N. The total drift square is controlled, not each individual pair force. THM028 is a new homogeneous target with explicitly fixed-N constants.

THM027/AUD032/033: fixed d>=3,0<s<=d-2,N>=2,T,1<q<d/2,mu in C_tC2,u in C_tC1,f in C_tC3 and boundednu. The negative weighted coefficient is (alpha-p)2s/N for alpha>p. Positive diffusion can produce N^(2/s) inside an exponential; this is allowed only for fixed-N regularity. Constructor and blind use different comparable weights/absorption constants. No N-uniform derivative estimate follows. THM029 specifically demands a new uniform energy argument and forbids absorbing those costs into its constant.

R8 THM028/AUD034/035: d>=3,0<s<=d-2,N>=2,T finite,0<=nu<=nu_*,mu=1,b=u=0,smooth real h and its actual Fourier test. Every1<q1<d/2,q1+1<q2<d is allowed. First/second/time weights are w_q1,w_q2,w_s. Constants may depend severely on N; bounded initial F0 need not be iid or exchangeable but is independent of the Brownian drivers. The R9 uniform energy constant is a separate pending proof, never the R8 derivative constant.

R9 accepted uniform constants: a=s/(s+2), C_infty from the full R5 radial barrier multiplied by exp(2||D||TV T), C_J from actual Fourier C2 data and the integrable source, kappa the common lower-divergence constant. C_E=T(C_J C_infty+kappa C_infty^2), independent of N and selected0<=nu<=nu_*. The inequality2a-1<=a absorbs internal-drift loss. The fixed-N H1/W2,1/time constants justify limits only and disappear. At nu=0 no unweighted bound is inferred. The extra uniform L1 time-derivative construction has its own source check and pending supplemental verdict.

TASK062 final supplemental disposition: PASS_CONDITIONAL_EXTENSION, report AUDITS/HOSTILE/ROUND_009_TIMEWISE_ENERGY_RECHECK.md,209 lines,SHA25621ce79223857d09784121cf0b50b1d3befa30f9efd571f217cca2b2932277560. Root read the entire supplement, verified22 inputs,25 archive members and new output/outer seals, and rechecked all original hostile seals. No new diagnostic count is claimed. The precise additional corollary is sup_(t,N,nu)||partial_t Phi_t||1<=C_dot and nu||grad_pair Phi_t||2^2<=C_* N^(s/(s+2)) at every deterministic time, with corresponding timewise Haar self/absolute-cross rates. The original integrated theorem passes its two fresh-context gates; the additional corollary has a separate independent review in the reused hostile context after its original seal. It is not another fresh audit or certification of the whole blind report. No actual-law smallness, diagonal trace or uniform unweighted gradient follows.


R10 constants depend on fixed d,s,T,h,nu_*,periodic kernel and fixed cutoff, never N or selected nu. The coarse heat-convolution floor uses a common positive kappa; the sharper heat-integral floor uses positive spectral coefficients and a retained empirical quadratic term. The entropy conditional-increment factor is (k-1)/(N-1), while the sharper block entropy bound gives C k lambda for k<=N/2. Fixed-N derivative constants remain only in the unclosed radial-tail criterion; no such constant may be relabeled uniform. R10 hostile passes, whole-card blind pending.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 explicit constants are reconstructed in hostile H4–H13 and H16–H21. The bounded-chi Jacobian-weight cost, fixed annular terms, derivative-only two-response bound and Gronwall contain no hidden C_N. The positive occupation coefficient is s(d-2-s), so it cannot be used at Coulomb. R7 fixed-N higher moments justify identities only; all N/nu dependence remaining in the result is displayed.

R11/R13 accepted constants: R11 fixes d>=3,0<s<=d-2,T,L,h,weights and controls every fixed moment alpha>m by C(chi^((s+2)/s)),chi<=L. R13 fixes d>=4,0<s<2,T,nu_*,h,q,weights; q is strictly1<q<min(d-2,d/2),q<=s+1,eta<2. Its negative diffusion and repulsive coefficients both remain positive; no uniform endpoint-in-s/q/d/nu_* constant is claimed. Complete formula records are the immutable proofs and accepted round reports.


Round014 final gate,2026-09-18 UTC. R14 accepted fixed-family constant can be (3sqrt(2)/2)T A_q J_q^*, where A_q is precisely the admitted uniform R12 weighted-gradient constant and J_q^* the explicit finite polar/smooth-complement bound in the proof. q is the stated midpoint; q<d-s-1 gives integrability and q>s/2 gives decay. No fixed-N density or derivative constant enters this uniform lower estimate.


Round015 final gate,2026-09-18 UTC. R15 complete fixed-data uniform source constant uses finite smooth terminal Fourier seminorm, constructor powerd+4 or independent modewise reconstruction powerd+2. No exponential terminal-frequency cost, noise-dependent energy constant or positive-time iid factor. Cubic constants may depend on fixed bounds for the critical tail and admitted R12 gradient constants; no endpoint uniformity in s approaching2 is claimed.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R16 constructor polynomial-tail weight d+2 and uniform logarithmic symbol slope give a finite smooth Fourier seminorm; fresh blind uses per-mode cutoff and polynomial |m|^(d+2) with Gaussian margin51/512. R17 constants depend on fixed finite tuple,kernel,d,s,T and critical tail bounds; no N or unbounded-noise uniformity. THM040 requests only a fixed bounded noise interval and fixed tuple, without a rate for nu_N->nu_bar.


R17 final gate,2026-09-18 UTC. R17 constants are uniform on each admitted eventual critical tail for the fixed finite tuple; the proof establishes eventual b1 explicitly. R16 gives all bounded-noise source constants. No all-noise constant is promoted until THM041 independent gates.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R19 new proof explicitly checks constants over every finite nu: zero expected-energy upper bound, spatial Fourier contraction, nu*b<=1; local particle/PDE and time-derivative constants are per fixed nu, never used uniformly. Both whole constructions agree; hostile pending.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.


R21 final whole gate accepted,2026-09-18 UTC. THM043/PO030 is PROVED_CANDIDATE with ISOLATED_RECONSTRUCTION_PASS (AUD061) and HOSTILE_REVIEW_PASS (AUD062), with exact published source/gate matching. The full strict range d>=3,0<s<d-2,s(s+2)<2d at finite positive microscopic critical lambda is retained. The actual integrated cubic residual obeys sigma E|integral U3[C Phi]dt| <= C[N^(s/d-1/2)+N^-1/2+N^((a-theta)/2)+N^-kappa] ->0. Absolute value remains after time integration; the genuine pair inverse retains both responses, the exact R8 domain, full true martingale and both lower contractions rho[g]/N+c/(2N). No instantaneous cubic estimate, Coulomb endpoint, Gaussian law or hierarchy is inferred. Root complete source/candidate/527-line blind/249-line hostile reading and twelve-item comparison are AUDITS/ROUND_021_GATE_INTEGRATION.md and ROUND_021_RECONSTRUCTION_COMPARISON.md. All29/29/32-input38/38/42-member packets verify unchanged; fresh diagnostics12531/117352/137147 reproduce saved bytes. The hostile stdout-only extra newline is explicitly recorded and no evidence normalized. All-real exponent implications are proved analytically; finite computations support but do not certify them. Earlier pending entries are chronological history.
