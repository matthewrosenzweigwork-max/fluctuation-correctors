# TASK-014 — fixed-smooth finite-dimensional Gaussian reduction

Round 002, 2026-09-17. Constructor assignment after the isolated falsification report is sealed. Owner Astra Max /root/r002_falsification; same isolated worktree, separate immutable report. Root alone integrates. No commits, pushes, dependencies or canonical-ledger edits.

## Exact assertion and negation

Under the exact iid fixed-smooth model and uniform norms of PO-001_RESIDUAL.md, freeze a finite list of times in [0,T] and smooth terminal tests. For each test/time use the full backward linearized one-body solution with zero extension beyond its terminal time. Permit the corresponding pair estimates separately up to each time. Put sigma_N=min(sqrt(N beta_N),sqrt N), a_N=sigma_N/sqrt N and c_N=sigma_N^2/(N beta_N). Let I_N be the finite covariance matrix with entries a_N^2 Cov_mu0(f_a^N(0),f_b^N(0)); let D_N have entries 2c_N integral_0^min(t_a,t_b) mu_r^N(grad f_a^N(r).grad f_b^N(r)) dr. If I_N and D_N converge entrywise to I,D, prove that the vector of sigma_N rho_{t_a}^N(test_a) converges in distribution to the centered Gaussian with covariance I+D. State possible degeneracy. The theorem is a conditional covariance-limit criterion for fixed smooth kernels; do not silently assert convergence for arbitrary oscillating beta_N or any singular family.

Exact negation: permitted data and convergent I_N,D_N for which this finite-dimensional conclusion fails. Derive all remainder bounds, initial centering and deterministic-bias scaling. Show the martingale noise becomes independent of the initial triangular iid fluctuation; do not merely name a martingale central limit theorem. A direct bounded exponential-martingale characteristic-function proof and elementary iid characteristic expansion are preferred and self-contained.

## Permitted inputs and tests

Your own sealed independent residual proof, frozen model, audited R1 one-body/pair identity. No other R2 constructor output. Show bracket replacement in L1 using actual-law coupling, including temperature prefactor c_N<=1. Test free heat by exact Fourier covariance, times zero/equal/different, and beta_N tending to zero, positive finite beta, infinity. Distinguish physical-temperature limits from the unchanged Riesz scaling labels; no s is present in this fixed-smooth model.

## Output and acceptance

MEMORANDA/ROUND_002_SMOOTH_GAUSSIAN.md with full statement, proof, exact limitations, source preflight, norm/constant dependence and mathematical/audit axes. Freeze by SHA-256 when complete. A separate hostile review is required before promotion. M3 remains OPEN unless its whole frozen scope closes; this bounded theorem may discharge a named subclaim only. No tightness or singular-limit claim.
