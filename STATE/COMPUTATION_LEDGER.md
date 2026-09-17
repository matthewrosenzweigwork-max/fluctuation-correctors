# Computation ledger

| ID | Purpose | Discovery code | Verifier | Status | Output |
|---|---|---|---|---|---|
| CMP-001 | k=2 drift, noise and contractions | round001_pair_selfcheck.py | root + independent BBGKY verifiers | REPRODUCED exact batteries; floating discovery EXPLORATORY | see executed checks |
| CMP-002 | k=3 and general subset contractions | round001_recursion_check.py | root all-order verifier | REPRODUCED | exact checks PASS |
| CMP-003 | k=4 recursion including k>N | round001_recursion_check.py | round001_allorder_fourier_check.py | REPRODUCED | certificate CMP-003 |
| CMP-004 | Fourier UV divergence/counterterm test | not started | not started | EXPLORATORY | — |
| CMP-005 | separated-support weighted-form counterexample | not started | not started | EXPLORATORY | — |

No computation may be cited as proof without the status and certificate required by Protocol 16.


## Round 001 executed checks

- CMP-001: root VERIFICATION_CODE/round001_fourier_pair_check.py; 90 exact rational raw/decomposed pair cases PASS, independent of constructor code. Certificate under CERTIFICATES/CMP-001_PAIR_FOURIER_20260917T180000Z.md.
- CMP-001B: VERIFICATION_CODE/round001_bbgky_exact_fourier.py; 24 exact rational cases PASS, including inhomogeneous reference, martingale coefficients and cross brackets; separately written in isolated BBGKY context.
- CMP-001C: DISCOVERY_CODE/round001_pair_selfcheck.py; root rerun of constructor self-check, 16 one-body and 80 pair floating-point cases PASS, max residuals 4.263e-14 and 2.274e-13, tolerance 2e-10. EXPLORATORY numerical support, no rigorous enclosure.
- CMP-003: independent root all-order verifier, 144 rational cases for k=1..4, N=2,3,4, nu=0,1/3,2 PASS. The complete finite-subset proof is in MEMORANDA/ROUND_001_RECURSION.md; independent proof audit is separately recorded. Certificate under CERTIFICATES/CMP-003_ALLORDER_FOURIER_20260917T181431Z.md.
- Exact finite batteries are REPRODUCED support; none alone proves a universally quantified mathematical identity. No random seeds or dependency installations.

- CMP-002/003D: root rerun of DISCOVERY_CODE/round001_recursion_check.py PASS: 37,886 integer cancellation coefficients through k=9; exact Q(i) drift, time derivative and rooted gradients for k=1..4, N=2..4, inhomogeneous positive reference; full partial-matching bracket cases (2,1,1), (2,2,2), (3,2,3), (3,1,4). Saved constructor output is byte-preserved; run ended ALL ROUND 001 RECURSION SELF-CHECKS PASSED.
- CMP-006: VERIFICATION_CODE/check_round001_smooth_fourier.py; root rerun PASS 120 rational identities, N=2,3,17, nu=0,1/3,1,7. Heat mode, signed interaction eigenmode, and nonzero internal-transport manufactured solution. REPRODUCED / SELF_CHECKED, not an independent proof certificate.
- CMP-004 cutoff divergence and CMP-005 separated-support negativity were settled at the level of explicit analytic calculations in the smooth and falsification memoranda; no numerical enclosure is claimed.

## Round 002 executed support

- CMP-007: constructor DISCOVERY_CODE/check_round002_coupling_exact.py, root rerun 1,292 exact rational equalities PASS; output JSON retained. Pair/triple deletions, rooted gradients, brackets, temperature and norm orders. REPRODUCED, not independent proof certification.
- CMP-008: independently written VERIFICATION_CODE/round002_falsification_exact.py, root rerun 116 exact rational checks PASS; moving background and nonzero interaction as well as free heat. REPRODUCED; proof is separate.
- CMP-009: independent blind VERIFICATION_CODE/round002_blind_selfcheck.py: 20 drift, 64 bracket, 20 constant, 204 matching and 21,845 cancellation equalities. Frozen original output retained; root rerun stored separately. REPRODUCED finite support, with independent universal reconstruction in AUD-004.
- CMP-010: root VERIFICATION_CODE/round002_partition_check.py: 84 exact rational identities for k=1..7, N=2,3,4 including k>N, plus absolute partition weight k! and exponent inequality. REPRODUCED / SELF_CHECKED; this is not an all-order proof.

All use system Python 3.9.6 standard library, no seeds or tolerance, no installed dependency. No unchanged R1 battery repeated merely to inflate verification.

- CMP-011: independent residual hostile verifier, 208 exact rational Laurent-polynomial checks PASS; code VERIFICATION_CODE/round002_hostile_residual_exact.py, root rerun CERTIFICATES/OUTPUTS/round002_hostile_root_rerun.json.
- CMP-012: all-order constructor checks, 444 exact Fraction/integer equalities PASS; code DISCOVERY_CODE/check_round002_powercount_exact.py, root rerun CERTIFICATES/OUTPUTS/round002_powercount_root_rerun.json.
- CMP-013: Gaussian statement-only constructor, 2,147 exact coefficient/model checks PASS; code DISCOVERY_CODE/check_round002_gaussian_blind_exact.py, root rerun CERTIFICATES/OUTPUTS/round002_gaussian_blind_root_rerun.json. No numerical proof of convergence inferred.
- CMP-014: independently authored hostile all-order verifier, 1,110 exact rational checks, including nonsymmetric counterexample and Sym repair; code VERIFICATION_CODE/round002_powercount_hostile_exact.py, root rerun CERTIFICATES/OUTPUTS/round002_powercount_hostile_root_rerun.txt. All these computations are REPRODUCED supporting evidence; the analytic arguments and separate audit scopes are recorded independently.

## Round 003 reproduced finite checks

- CMP-015: constructor DISCOVERY_CODE/check_round003_iid_pair_exact.py, 5,500 exact checks, root rerun CERTIFICATES/OUTPUTS/round003_iid_pair_root_rerun.json.
- CMP-016: independent VERIFICATION_CODE/round003_iid_projection_exact.py, 3,453 exact checks, root rerun CERTIFICATES/OUTPUTS/round003_iid_projection_root_rerun.json.
- CMP-017: separate hostile VERIFICATION_CODE/round003_hostile_pair_exact.py, 18,603 exact checks, root rerun CERTIFICATES/OUTPUTS/round003_hostile_pair_root_rerun.json.
- CMP-018: statement-only reconstruction DISCOVERY_CODE/check_round003_probability_blind_exact.py, 5,483 exact checks, root rerun CERTIFICATES/OUTPUTS/round003_probability_blind_root_rerun.json.

All four use standard-library exact integer/Fraction arithmetic, with no random seed or numerical tolerance. Finite atomic/cyclic examples test all centering factors and radius exponents, not a continuous singularity or asymptotic probability theorem. Independent proofs and review scopes are preserved separately. No unchanged R1/R2 battery was repeated solely to increase counts.

- CMP-019: independent hostile VERIFICATION_CODE/round003_sharp_hostile_exact.py, 31,194 exact integer/Fraction checks PASS, root rerun CERTIFICATES/OUTPUTS/round003_sharp_hostile_root_rerun.json. Includes close-pair count moments, pairwise versus mutual independence, mean absorption, centered split, matching powers and compatible constants. Continuous/asymptotic claims are proved analytically, not by the finite battery.

- CMP-020: separate transport hostile DISCOVERY_CODE/check_round003_pair_transport_review_exact.py, 749 exact checks PASS, root rerun CERTIFICATES/OUTPUTS/round003_pair_transport_review_root_rerun.json.
- CMP-021: statement-only sharp VERIFICATION_CODE/round003_sharp_blind_exact.py, 28 exact rational checks over 3,568 configurations PASS, root rerun CERTIFICATES/OUTPUTS/round003_sharp_blind_root_rerun.json.

- CMP-022: fresh sharp reconstruction exact checker under AUDITS/BLIND_RECONSTRUCTION, 19,734 checks over 19,600 configurations PASS; root rerun round003_fresh_sharp_root_rerun.json.
- CMP-023: fresh hostile VERIFICATION_CODE/round003_fresh_hostile_exact.py, 1,440 configuration identities, 16 moment/bound cases, 2 pair-count cases and 351 exponent cases PASS; root rerun round003_fresh_hostile_root_rerun.json.

CMP-024: fresh THM017 reconstruction exact checker, AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_TRANSPORT_CHECK.py, root output CERTIFICATES/OUTPUTS/round003_fresh_transport_root_rerun.json. REPRODUCED: 12 iid moment cases and 54 transport substitutions, exact Fraction arithmetic, no seed or tolerance. Finite coefficient tests only; no numerical PDE or singular-limit certification.

CMP-025: independent R4 reconstruction VERIFICATION_CODE/round004_diffusive_reconstruction_exact.py; root rerun CERTIFICATES/OUTPUTS/round004_diffusive_reconstruction_root_rerun.json. REPRODUCED,3252 exact Fraction checks (432 radial,1296 angular,864 Lyapunov,648 scale-generator,12 exponent). No floating approximation, random seed or tolerance. All-N addendum is an analytic case proof, with no separate numeric certificate.

CMP-026: fresh hostile AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_EXACT_CHECK.py root-rerun,2520 radial tuples,7560 Lyapunov tuples,24 iid cases/2160 configurations,70 scaling tuples PASS, exact Fraction arithmetic. Root output round004_diffusive_hostile_root_rerun.txt. CMP-027: root range Taylor self-check DISCOVERY_CODE/round004_range_taylor_check.py,18 exact binomial derivative cases, output round004_range_taylor_root_check.json; confirms corrected V2 coefficient and detects original V1 bound failure for s>1. SELF_CHECKED finite algebra only, not an independent annular proof.

CMP-028: response constructor DISCOVERY_CODE/check_round004_singular_response_exact.py,133 exact checks; root output round004_singular_response_root_rerun.json. CMP-029: fresh response hostile AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_EXACT_CHECK.py,346 exact checks; root output round004_response_hostile_root_rerun.txt. CMP-030: fresh range hostile ROUND_004_RANGE_OBSTRUCTION_EXACT_CHECK.py,234 derivative comparisons,2880 time-bound cases,63 actual rational remainders with36 detecting the preserved V1 failure; root output round004_range_hostile_root_rerun.json. CMP-031: fresh response blind ROUND_004_RESPONSE_RECONSTRUCTION_CHECK.py, exact rational Fourier/mode/compensation/heat/divergence checks; root output round004_response_blind_root_rerun.json. All REPRODUCED standard-library exact checks, no randomness/tolerance/dependency. These finite programs do not prove analytic limits or stochastic existence.

CMP-032 (R5 submission): VERIFICATION_CODE/round005_periodic_pair_exact.py,567 exact profile/product/barrier/norm-factor checks PASS; root output round005_periodic_pair_root_rerun.json. No independent R5 audit status inferred.

CMP-033: fresh annular reconstruction AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RANGE_EXACT_CHECKS.py,81 admitted rows,five excluded controls,one explicit annular-constant case PASS; root output round004_range_blind_root_rerun.json. Exact standard-library arithmetic, REPRODUCED; both analytic boundary-controlled proofs are separately recorded in AUD025. CMP-034: R5 fresh hostile exact checker,4415 exact assertions PASS, root output round005_periodic_hostile_root_rerun.json; no stochastic/continuum theorem is inferred from finite checks.

CMP035: fresh periodic/composition reconstruction AUDITS/BLIND_RECONSTRUCTION/ROUND_005_PERIODIC_AND_COMPOSITION_EXACT_CHECK.py,4536 radial,4536 cutoff-product,1344 all-N core/tail,96 divergence,468 iid configurations in12 cases,3 density,56 exponent,13 Volterra cases PASS. Root output round005_periodic_blind_root_rerun.json. REPRODUCED exact standard-library arithmetic; no random seed/tolerance or continuum proof inferred.

R5 additional REPRODUCED checks: TASK0432672 exact assertions and TASK04727 exact constant comparisons PASS; root outputs round005_interface_blind_root_rerun.json and round005_interface_source_recheck_root_rerun.json. TASK044 has20 exact iid cases/36 exact rate identities and48 floating Fourier quadratures plus floating scalar residuals; no exact/certified label for those floating diagnostics. R6 constructor2631 and blind242 exact checks are reproduced supporting next-gate algebra, not R5 particle certification.
