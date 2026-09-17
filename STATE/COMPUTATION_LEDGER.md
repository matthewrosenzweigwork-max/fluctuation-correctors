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
