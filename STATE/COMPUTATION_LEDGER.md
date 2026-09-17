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
