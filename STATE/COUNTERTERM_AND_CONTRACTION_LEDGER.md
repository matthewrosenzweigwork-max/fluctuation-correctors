# Counterterm and contraction ledger

| ID | Origin | Order | Formula | Regime | Regularization | Status | Cross-check |
|---|---|---:|---|---|---|---|---|
| CT-001 | deleted diagonal / iid quadratic bias | 2 | to derive | all | finite-N | OPEN | U-statistic vs empirical measure |
| CT-002 | Itô trace for pair corrector | 2 | to derive | positive temperature | cutoff-dependent initially | OPEN | explicit sum vs generator |
| CT-003 | critical UV/Wick term | 2+ | to determine | \(2s\ge d\) | heat/Fourier | OPEN | two schemes required |
| CT-004 | local pressure/free-energy centering | deterministic | to determine | moving background | local Gibbs | OPEN | static derivative vs dynamic stress |

Do not combine counterterms of different origins under one symbol.


## Exact smooth pair entries (Round 001)

- CT-001: U_2[Phi]=rho^2(Phi)-eta(Phi_diag)/N, P=U_2/2. At iid preparation E U_2[Phi]=-mu^2(Phi)/N. Exact diagonal subtraction is not automatically Wick centering or pressure renormalization.
- CT-002: the full-product P convention has the Ito drift nu*eta(tr D_xy Phi)/N. Differentiation of -eta(Phi_diag)/(2N) cancels it exactly. The pair martingale and all brackets remain. Scope is fixed smooth g/Phi, independent particle noises.
- Internal interaction: B Phi=K(x-y).(grad_x-grad_y)Phi. Its raw term D_2[B Phi]/(2N) equals P[B Phi]/N+rho((B Phi)_mu)/N+mu^2(B Phi)/(2N). No scalar contribution may be dropped.
- Proofs: algebra report (3.6)-(3.8), (4.9)-(4.16); independent BBGKY report (3.4)-(3.8), (5.1)-(5.6). Pair audit: AUD-001 isolated reconstruction passes; hostile pending. CT-003/004 singular and pressure terms remain OPEN.

## All-order accounting

The finite-subset derivation and full partial-bijection bracket expansion are equations (R1)–(R5) of MEMORANDA/ROUND_001_RECURSION.md. Drift has no separate Brownian lowering term under ordered distinct-label centering; the full-product contraction cancels the subtracted diagonal. Brackets retain all shared-label contractions, with root excluded from the nonroot matching. For k=2, the deterministic U_0 contraction is mu^2(B Phi)/(2N) in P=U_2/2. These are smooth identities. Singular Wick/diagonal counterterms remain OPEN.

## Round 002 exact retained terms

The triple deletion is U3[F]=rho^3[F]-3/N (eta tensor rho)[F(x,x,y)]+2/N^2 eta[F(x,x,x)]. For F=C Phi the full diagonal vanishes from K(0)=0, while the random partial diagonal must be estimated. The pair gradient retains -grad_1 Phi(x_i,x_i)/N. Both independent residual proofs retain these terms; no new counterterm or changed centering is introduced. AUD-004 also reconstructs every centered shared-label Brownian contraction with positive combinatorial coefficients; the centered statistics themselves are signed.

## Round 002 final integration

Round 002: exact partition moments identify pair blocks as zero additional N gain and larger blocks as extra N^(-(|B|-2)/2). The k-to-k-2 drift contraction stays at the raw N^(-k/2) order; it is not an additional asymptotic gain. No singular counterterm or deterministic subtraction is justified solely by these coefficients. The THM-012 symmetry defect changes no contraction coefficient after the explicit THM-014 repair.

Round004: the finite measure D=divK has mass zero. At Coulomb it is c_d(delta0-Haar), c_d=(d-2)|S^(d-1)|; both parts survive the exact transferred-derivative response. This is distributional operator compensation, not permission to drop finite-N contractions or add a new Wick centering. All existing pair/triple/self/cross terms remain required. THM021 fresh AUD023/024.

R8 exact distinct-label identity: drift -P[J]+U3[C Phi]+rho[(B Phi)_mu]/N+integral(B Phi)/(2N), with C Phi the average over six permutations of K(x-z).grad_x Phi(x,y). The one-background cubic contraction is (A_a+R Phi)/6, two-background contraction v/3, full scalar zero; (R Phi)_mu=v and integral R Phi=0. Repeated internal pairs are grouped into B Phi before absolute estimation. Triple products use separate relative variables. No singular diagonal value, omitted scalar or additional Brownian trace is introduced.

R9 exact exchangeable square is N^-3[(N-1)E|H12|^2+(N-1)(N-2)E H12.H13-2(N-1)E H12.A1+E|A1|^2]. The triple is omitted as an object at N=2. The actual-minus-Haar scaled difference retains coefficients(N-1),(N-1)(N-2),-2(N-1) on delta2,delta3,deltaA, with outside2nu b_N/N^2. One-body invariance removes only the fourth difference. No additional Wick subtraction or diagonal trace.


R10 preserves all coefficients of the exact two-/three-/mixed bracket expansion, with no X3 object at N=2. The smoothed empirical-gradient representation retains -G_delta(Xi,Xi)/N inside the outer1/N. The initial smooth centered triple derivative is the negative Fourier quadratic form from the interacting 2-3 pair; other first-order pair terms vanish only by row centering. No positive-time sign or singular diagonal counterterm is inferred.


R10 gate update: the preceding R10 conditional claims/reductions now also pass the complete fresh reconstruction AUD042, alongside hostile AUD038/039. See AUDITS/ROUND_010_WHOLE_CARD_RECONSTRUCTION_COMPARISON.md for every exact scope and source qualification. No full singular-tail, cubic-residual or hierarchy conclusion is added.


R12 whole-square control retains the exact literal gradient N^-2[sum G-N A]. After actual expectation its coefficients are2(N-1)^2/N^3 and2/N; physical scaling yields4nu b[(N-1)^2/N^2 EG12^2+||A||2^2]. It bounds the full nonnegative bracket without claiming separate absolute pair/triple/mixed law-error estimates. The evolved cubic and lower drift contractions are unchanged and remain unclosed.

R13 full/noise split retains pair, ordered triple, mixed and row-square terms with exact coefficients and physical2nu Nb. Every radial tail uses its own row; no orthogonality is asserted. THM035's pending lower drift is N^-1 rho[(B Phi)_Haar]+(2N)^-1 integral B Phi, with B Phi=K dot(grad_x-grad_y)Phi. THM036 uses the six-permutation average in C Phi and all ordered U3 background contractions. No counterterm or centering is altered.


Round014 final gate,2026-09-18 UTC. R14 AUD047/048 retain both actual lower contractions and no new counterterm: ell=rho[g]/N+c/(2N). C1=(A_a+R Phi)/6,C2=v/3,C0=0; both R slots coefficient one. The repeated ordered pair contributes D2[B Phi]/(2N), with no hidden extra N^-2 term. Accepted rendering erratum changes no coefficient or issued bytes.


Round015 final gate,2026-09-18 UTC. R15 retains exact C1=(A_a+R Phi)/6,C2=v/3,C0=0, two response slots and rho[(B Phi)_mu]/N+(integral B Phi)/(2N). The positive heat split retains smooth energy self coefficient1/N and separate labelled-pair1/(N-1); smooth source diagonal is exactly zero only at its observable cutoff. No counterterm introduced or singular diagonal assigned.


R16/R17 reconstruction checkpoint,2026-09-18 UTC. R16 source proofs agree on row -D*f and scalar0 with full Coulomb atom/compensation; smooth zero source diagonal alone permits the rho-square representation, while smooth energy self subtraction is retained. R17 first-order interaction is P[J]+eta[-D*f], exactly canceling its backward response. No new self term, falling factorial or counterterm.


R17 final gate,2026-09-18 UTC. R17 accepted ordered first-order identity retains source coefficient1, pair half,N^2 denominator,full row -D*f and computed scalar0. No additional finite-N response factor, singular self assignment or counterterm. Existing second/higher-order contractions remain unchanged.


R18/R19 reconstruction checkpoint,2026-09-18 UTC. R18/R19 complete comparisons retain P=U2/2, literal deleted N^2 denominator, row=-D*f and scalar zero by integration. Thermal coefficient2nu*b has no deleted N-1 factor. Coulomb atom and compensation preserved.


## R18/R19 whole gates accepted — 2026-09-18 UTC

THM040/PO027 and the entire THM041/PO028 conjunction now pass both fresh independent axes and exact source matching. R18 AUD055/056 gives bounded-convergent-noise finite-dimensional Gaussian law with full initial plus thermal covariance, exact Haar centering, all frozen degeneracies and no noise-convergence rate. R19 AUD057/058 gives the source bound uniform over every finite nonnegative diffusivity and, with s<d/2, full unit bounded-Lipschitz Gaussian approximation uniformly over that parameter, including unrestricted hot-noise convergence to zero in probability. Source range remains d>=3,0<s<=d-2; Gaussian claims remain s<d/2, fixed finite smooth time/test list, actual homogeneous iid-Haar-prepared singular gradient dynamics. Original half/row/scalar, Coulomb atom/compensation, b and independent-noise coefficients are unchanged. Full proofs, scope, exposure, source and computation dispositions are AUDITS/ROUND_018_GATE_INTEGRATION.md and AUDITS/ROUND_019_GATE_INTEGRATION.md. No path-space/field/higher hierarchy or broader law claim is included, no root independent chronology certificate, no new counterterm or retraction. Frozen historical cards and evidence bytes remain untouched.
