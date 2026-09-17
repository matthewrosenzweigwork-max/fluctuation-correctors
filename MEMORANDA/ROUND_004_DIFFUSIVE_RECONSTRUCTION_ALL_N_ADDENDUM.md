# Round 004: all-N extension of the independent iid endpoint estimate

2026-09-17 21:52:49 UTC. Separate immutable addendum by `/root/r004_diffusive_blind`.
Worktree: `/private/tmp/hocf-r004-diffusive-blind-20260917`.

**Disposition:** the restriction to sufficiently large N in (9.8) of the original reconstruction can be removed. The explicit constants below give its three upper rates for every integer `N>=2`, uniformly in diffusivity, temperature, and deterministic remaining time in the fixed interval. This addendum proves only this quantifier extension. The original sealed report remains byte-for-byte unchanged, with SHA-256 `8cf1cd3fbd286994dbd9a20331a6d19600112e131cecc364d9f1ee9af8436f95`.

The only mathematical inputs used for this extension are the original report, especially (2.1), (9.5), and (9.7), and the frozen TASK-032 scope. Their hashes are in `AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_ALL_N_INPUT_SHA256SUMS.txt`. No constructor proof, new theorem statement, root state, new task, memory, or outside source was read. Formula (9.7) is a finite-N upper bound, not an equality for the exact radial square norm; the algebraic rewritings of its core contribution below are equalities.

## 1. Parameters and an explicit constant

Keep all hypotheses and diagnostic definitions of the original report: integer `d>=3`, `0<s<=d-2`, `p=s+2`, `N>=2`, finite `nu>=0`, fixed symmetric A, `0<=T<infinity`, cutoff radius `R=R_1` with `0<R<1/2`, and iid initial densities with a common finite upper bound M. The cutoff obeys `0<=chi<=1`. Write

\[
 K=\|A\|_{\mathrm{op}},\qquad
 c=2sp,\qquad a_0=\frac{c^2}{16d},\qquad
 D_0=\frac{M K^2\omega_d}{2},\qquad
 b_N=\min(\beta_N,1),\qquad \sigma_N=\sqrt{N b_N},
 \tag{A.1}
\]

where `beta_N>0`, and `omega_d` is the surface area of the unit sphere. The new symbols `a_0,D_0` are scalar constants in this addendum and are unrelated to any angular coefficients in the original report. Define `log_+ x=max(log x,0)` for `x>0`.

For `T>0`, the following finite constant is sufficient:

\[
 C_T=D_0\begin{cases}
 \displaystyle
 T^2 R^{d-2s}\left(a_0+\frac{s^2}{d-2s}\right),
       &2s<d,\\[6pt]
 \displaystyle
 T^2\left[a_0+\frac{s^2}{p}
       \left(1+\log_+\frac{R^p}{cT}\right)\right],
       &2s=d,\\[6pt]
 \displaystyle
 \left(a_0+\frac{s^2}{2s-d}\right)
       c^{-(2s-d)/p}T^{(d+4)/p},
       &2s>d.
 \end{cases}
 \tag{A.2}
\]

For `T=0`, set `C_0=0` without evaluating the logarithm. These constants depend only on the fixed `d,s,T,A,M,R`; in particular they do not depend on N, nu, beta_N, the particular density with that bound, or remaining time. They may depend on the side of the threshold `2s=d`; no uniform-in-s threshold estimate is asserted.

The all-N assertion is

\[
 \boxed{\quad
 \sup_{\nu\ge0}\sup_{0\le\tau\le T}
 \mathbb E\left|\sigma_NP_N[H_{N,\nu,\tau}]\right|^2
 \le C_T b_N
 \begin{cases}
 N^{-1},&2s<d,\\
 (1+\log N)/N,&2s=d,\\
 N^{-(d+2-s)/(s+2)},&2s>d,
 \end{cases}
 \qquad N\ge2.
 \quad} \tag{A.3}
\]

Both suprema are outside expectation. The diagnostic is the same measurable periodic cutoff kernel as before, the iid law and all mean-field centering terms are retained, and nu may be chosen to equal `1/beta_N`. No new stochastic-time supremum or interacting-law assertion is introduced.

The exact negation is an admissible parameter, particle number at least two, or remaining time for which (A.3) fails with the explicit constant (A.2). The following case calculation excludes that negation, including the large-core cases omitted from the original large-N deduction.

## 2. The finite-N core formula on both sides of the cutoff

For `tau>0`, put `ell=(c tau/N)^(1/p)` and define

\[
 I_N(\tau)=\int_{B_R}F_{N,\tau}(|z|)^2\,dz.
\]

Equation (9.7) of the original report is

\[
 I_N(\tau)\le\omega_d\left[
 \frac{N^2\ell^4\min(R,\ell)^d}{16d}
 +\mathbf1_{\{\ell<R\}}s^2\tau^2
       \int_\ell^R r^{d-1-2s}\,dr\right].
 \tag{A.4}
\]

Set `delta=d-2s`. Since `N ell^p=c tau`, the core term before the factor omega_d is exactly

\[
 \frac{N^2\ell^4\min(R,\ell)^d}{16d}
 =a_0\tau^2\ell^{-2s}\min(R,\ell)^d
 =\begin{cases}
 a_0\tau^2\ell^\delta,&\ell\le R,\\
 a_0\tau^2 R^d\ell^{-2s},&\ell>R.
 \end{cases}
 \tag{A.5}
\]

The tail in (A.4) is absent when `ell>=R`. At `ell=R`, both core expressions coincide and the tail is zero. Thus no threshold condition on N is required in (A.4)--(A.5).

### The case 2s<d

For `ell<=R`, the core is at most `a_0 tau^2 R^delta`, and

\[
 s^2\tau^2\int_\ell^R r^{\delta-1}\,dr
 =\frac{s^2\tau^2}{\delta}(R^\delta-\ell^\delta)
 \le\frac{s^2\tau^2R^\delta}{\delta}.
\]

For `ell>R`, (A.5) gives instead

\[
 a_0\tau^2R^d\ell^{-2s}
 =a_0\tau^2R^\delta(R/\ell)^{2s}
 \le a_0\tau^2R^\delta.
\]

Consequently, for every positive tau and every N>=2,

\[
 I_N(\tau)\le\omega_d\tau^2R^{d-2s}
       \left(a_0+\frac{s^2}{d-2s}\right).
 \tag{A.6}
\]

### The case 2s=d

For `ell<=R`, (A.4) gives the upper bound
`omega_d tau^2 [a_0+s^2 log(R/ell)]`. For `ell>R`, its sole core term is

\[
 \omega_d a_0\tau^2(R/\ell)^d
 \le\omega_d a_0\tau^2.
\]

Thus, in both cases,

\[
 I_N(\tau)\le\omega_d\tau^2
       \left[a_0+s^2\log_+(R/\ell)\right]
 =\omega_d\tau^2
       \left[a_0+\frac{s^2}{p}
            \log_+\frac{NR^p}{c\tau}\right].
 \tag{A.7}
\]

To obtain a constant independent of remaining time without introducing a lower bound on tau, use monotonicity of the actual profile: equation (2.1) of the original report gives
`partial_tau F=s(r^p+c tau/N)^(-s/p)>0`. Therefore `I_N(tau)<=I_N(T)` for `0<tau<=T`. This argument uses monotonicity of F itself and does not assume monotonicity of an arbitrary estimated right-hand side.

For `T>0`, put `L_T=log_+(R^p/(cT))`. Since `N>=2` implies `log N>=0`, the elementary inequality `log_+(Nx)<=log N+log_+x` yields

\[
 \begin{split}
 I_N(\tau)&\le\omega_d T^2
     \left[a_0+\frac{s^2}{p}(\log N+L_T)\right]\\
 &\le\omega_d T^2
     \left[a_0+\frac{s^2}{p}(1+L_T)\right](1+\log N).
 \end{split}
 \tag{A.8}
\]

All bracketed constants are nonnegative. The second inequality follows by expanding the right-hand side; it bounds its constant and log-N coefficients separately. This includes `ell_T>R` and all earlier remaining times, even when the core crosses the cutoff during the interval.

### The case 2s>d

Write `kappa=2s-d>0`. For `ell<=R`, the core and tail in (A.4) are bounded by

\[
 \left(a_0+\frac{s^2}{\kappa}\right)\tau^2\ell^{-\kappa},
\]

because the tail equals `s^2 tau^2 (ell^(-kappa)-R^(-kappa))/kappa`. For `ell>R`, the sole core term in (A.5) obeys

\[
 a_0\tau^2R^d\ell^{-2s}
 =a_0\tau^2\ell^{-\kappa}(R/\ell)^d
 \le a_0\tau^2\ell^{-\kappa}.
\]

Hence, for every positive tau and every N>=2,

\[
 \begin{split}
 I_N(\tau)
 &\le\omega_d\left(a_0+\frac{s^2}{\kappa}\right)
                \tau^2\ell^{-\kappa}\\
 &=\omega_d\left(a_0+\frac{s^2}{\kappa}\right)
       c^{-\kappa/p}N^{\kappa/p}\tau^{(d+4)/p}.
 \end{split}
 \tag{A.9}
\]

The time exponent is positive. The resulting constant does not even require the cutoff radius in this row; enlarging the integration region has already been absorbed by the convergent radial bound.

## 3. Endpoint coefficient, zero time, and falsification checks

Equation (9.5) of the original report retains all centering terms and gives

\[
 \mathbb E|\sigma_NP_N[H_{N,\nu,\tau}]|^2
 \le b_N\frac{N-1}{2N^2}M K^2 I_N(\tau)
 \le\frac{b_N M K^2}{2N}I_N(\tau).
 \tag{A.10}
\]

Substituting (A.6), (A.8), or (A.9) in (A.10) proves (A.3) with exactly (A.2). In the last row the exponent is checked directly:

\[
 \frac{2s-d}{p}-1=-\frac{d+2-s}{p}.
\]

For `0<tau<=T`, the noncritical time powers are bounded by their values at T. The logarithmic case was handled by the profile's monotonicity. None of these bounds depends on nu or beta_N except through the displayed factor b_N.

At `tau=0`, the profile and the potential are zero. The diagnostic is the zero L2 kernel, so the iid statistic and its second moment are zero; no negative power of ell or logarithm of tau is evaluated. If `T=0`, this is the only remaining time and proves (A.3) with `C_0=0`.

The potentially adverse regime is a core strictly larger than the cutoff at small particle number. It has been checked directly rather than absorbed into an unspecified finite-N constant. In particular, for any N, including N=2 and N=3, choose a positive remaining time such that `ell=2R`. In the row `2s<d`, the ratio of its actual core contribution in (A.5) to `a_0 tau^2 R^delta` is exactly `2^(-2s)<=1`. In the row `2s=d`, the ratio to `a_0 tau^2` is `2^(-d)<=1`. In the row `2s>d`, the ratio to `a_0 tau^2 ell^(-kappa)` is again `2^(-d)<=1`. These independent large-core substitutions rule out the proposed obstruction in the omitted regime. At `ell=R` the expressions agree exactly. There is no tail contribution in these tests.

The coefficient in (A.10) also covers the smallest permitted particle numbers: `(N-1)/(2N^2)` is `1/8` for N=2 and `1/9` for N=3, respectively bounded by `1/(2N)=1/4` and `1/6`. Thus no denominator estimate tacitly presumes large N. These are exact algebraic checks; no numerical computation is used as proof.

## 4. Scope and sealed verification

The original (9.8) was a valid sufficiently-large-N assertion. This addendum supplies the missing all-N quantifier with an explicit constant, using the already proved global diffusion comparison and iid identity. The original report's classical-regularity qualification, probabilistic solution class, separate zero-diffusion convention, and full-operator exclusions are unchanged. The endpoint extension gives no new claim about a constructor proof, root theorem, evolved law, full response operator, or full campaign resolution.

Verification consists of the complete three-case calculation above, the large-core and boundary substitutions, the zero-time check, and the exact finite-N coefficient checks. The original output seal was verified before this work. At sealing, `shasum -a 256 -c AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_OUTPUT_SHA256SUMS.txt` and `shasum -a 256 -c AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_ALL_N_INPUT_SHA256SUMS.txt` pass, confirming preservation of the original report and supplied task. `git diff --check` and a direct scan of this new Markdown file pass for trailing whitespace, control characters, terminal newline, and balanced display delimiters. No new code or TeX is created and no dependency or classical PDE theorem is imported. An initial delimiter-count scan also counted the case-row spacing commands as display openings and reported a false mismatch. A delimiter-aware scan of standalone display fences passed; the mathematical text required no correction.

Created files are this addendum and its separate input/output hash manifests. The output seal is `AUDITS/ROUND_004_DIFFUSIVE_RECONSTRUCTION_ALL_N_OUTPUT_SHA256SUMS.txt`. No original report, prior seal, constructor output, canonical state file, or other worktree is changed. No commit, push, new-task work, or child agent is performed. Work stops after the addendum is sealed.
