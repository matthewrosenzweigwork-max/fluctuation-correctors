# Normalization and scaling ledger

## Frozen symbols

- Dimension: \(d\).
- Riesz exponent: \(0<s<d\); log separate.
- Particle number: \(N\).
- Inverse temperature: \(\beta_N\).
- Effective microscopic coupling:
  \[
  \lambda_N=\beta_NN^{s/d-1}.
  \]
- Empirical measure:
  \[
  \mu_N=N^{-1}\sum_{i=1}^N\delta_{x_i}.
  \]
- Fluctuation discrepancy: \(\rho_N=\mu_N-\mu\).
- Fluctuation scale: record theorem by theorem; thermal candidate \(\sqrt{N\beta_N}\), initial candidate \(\kappa_N\), combined scale must be frozen explicitly.

## Regime table

| Regime | Condition | Equivalent beta scale | Status |
|---|---|---|---|
| Old pathwise sufficient | \(\beta_NN^{2s/d-1}\to0\) | \(\beta_N\ll N^{1-2s/d}\) | existing baseline to supersede |
| Full subcritical | \(\lambda_N\to0\) | \(\beta_N\ll N^{1-s/d}\) | target |
| Critical | \(\lambda_N\to\lambda\in(0,\infty)\) | \(\beta_N\sim\lambda N^{1-s/d}\) | target |
| Supercritical | \(\lambda_N\to\infty\) | \(\beta_N\gg N^{1-s/d}\) | sharpness |

## Required additions

For every active theorem, append:

- exact Hamiltonian convention;
- factor of \(1/N\) in pair interaction;
- Brownian coefficient;
- deleted diagonal convention;
- periodic Fourier normalization;
- modulated energy factor \(1/2\);
- test-function normalization;
- corrector coefficient;
- centering and counterterms;
- error after multiplication by the fluctuation scale.
