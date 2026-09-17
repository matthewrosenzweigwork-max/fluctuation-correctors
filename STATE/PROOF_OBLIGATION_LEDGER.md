# Proof-obligation ledger

| ID | Obligation | Depends on | Status | Owner | Evidence |
|---|---|---|---|---|---|
| PO-001 | Scaled cubic residual, endpoint and correction brackets under stated law | PO-002, PO-001a | OPEN | root, next worktree unassigned | TASKS/ACTIVE/PO-001_RESIDUAL.md |
| PO-002 | Exact full pair linearized operator | duality normalization | EXACT_IDENTITY / isolated and hostile pass | root integrates algebra+BBGKY | THM-008; AUD-001/002 |
| PO-003 | Exact all-order generator recursion and bracket matchings | PO-002 | EXACT_IDENTITY / isolated and hostile pass | recursion + blind + hostile | THM-001, recursion report R1–R5 |
| PO-004 | Critical power-counting theorem | PO-003 | OPEN | unassigned | — |
| PO-005 | Smooth-kernel subcritical tail control for arbitrary \(\lambda_N\to0\) | PO-003, PO-004 | OPEN | unassigned | — |
| PO-006 | Smooth-kernel critical resummation/closure | PO-004 | OPEN | unassigned | — |
| PO-007 | Hilbert–Schmidt singular cutoff removal | PO-005 | OPEN | unassigned | — |
| PO-008 | Borderline logarithmic counterterm | PO-003 | OPEN | unassigned | — |
| PO-009 | Ultraviolet pair-field/finite-particle closure | PO-003 | OPEN | unassigned | — |
| PO-010 | Moving-background centering accuracy | static response | OPEN | unassigned | — |
| PO-011 | Static-to-dynamic local response input | source/new proof | OPEN | unassigned | — |
| PO-012 | Field/path tightness for corrected observable | finite-dimensional theorem | OPEN | unassigned | — |
| PO-013 | One-dimensional positive-temperature closure | ordered route | OPEN | unassigned | — |

Add exact statements, negations, and proof locations as obligations are activated.

## Round 001 activated assertions

- PO-002: exact full pair operator reconstructed in THM-008 and independent BBGKY report. Coefficients agree after mapping the triple symmetrization conventions. ISOLATED_RECONSTRUCTION_PASS for smooth finite N; hostile review passed in AUD-002.
- PO-001a: complete fixed-smooth backward pair estimate, in fact uniform for every nu>=0 and N>=2 conditional on the explicitly displayed norms. Two proof mechanisms and three solvable tests completed in THM-009/smooth memorandum; separate analytic review AUD-003 passes both the statement-only reconstruction and hostile review, with exact scope disclosed.
- PO-001 (remaining target after algebra): law-specific scaled corrected-observable residual control. A sufficient assertion must control in probability or L1 the integrated cubic/lower-order drift, the endpoint corrector and corrector/cross brackets, uniformly in the particle and temperature regimes and Riesz cutoff. Reference: independent BBGKY report equations (7.1)-(7.3). An expectation estimate alone is insufficient.
- PO-003: exact general recursion and all shared-label bracket contractions proved and hostile-reviewed. PO-004 critical power counting remains OPEN and is not inferred from fixed-smooth algebra.
- No private source theorem is a dependency of these exact smooth calculations.

PO-001a is discharged within its fixed-smooth scope by THM-009 and AUD-003. The next first open line is item 2 of TASKS/ACTIVE/PO-001_RESIDUAL.md, with companion endpoint/bracket bounds. Its singular extension and PO-004 are not discharged.

## Round 002 bounded residual progress

THM-010 supplies a complete fixed-smooth iid candidate proof, independently reconstructed (AUD-005); hostile review passed in AUD-006. The scaled cubic, endpoint and brackets vanish for every beta_N>0 under the frozen uniform norms. This discharges the first bounded construction task, not PO-001's singular extension. The explicit constants passed hostile review; the first open scientific interface is quantitative cutoff/order-dependent residual and model comparison for the frozen singular regimes.

AUD-006 now closes the hostile review of the fixed-smooth iid THM-010 assertion and root norm qualification. PO-001 remains OPEN for singular/order-dependent extensions, but its frozen first bounded task is discharged with isolated and hostile passes. PO-014 (new bounded subclaim): identify finite-dimensional Gaussian limit from explicit covariance convergence, THM-011; complete proof, AUD-007 hostile PASS and qualified AUD-008 statement-only comparison. PO-015: identify those covariances under finite/zero diffusivity limits in the fixed-smooth model, TASK-016 complete with THM-013/AUD-010 hostile PASS. These do not replace PO-004 critical singular power counting.

## Round 002 closure and Round 003 interface

PO-014 is discharged in the fixed-smooth finite-list covariance-limit scope by THM-011, AUD-007 and qualified statement-only comparison AUD-008. PO-015 is discharged within the existing positive-diffusivity smooth class, with zero-diffusivity existence constructed, by THM-013/AUD-010. Neither is a singular theorem. The stricter fresh-session audit requirement remains an explicit publication-gate qualification.

PO-004 now has an explicit smooth all-order partition/moment/bracket table and conditional series/cutoff criteria (repaired THM-014), but the actual singular corrector norms, coefficient growth and survival classification remain OPEN. First open load-bearing interface: prove a specified fluctuation-scale comparison of the singular particle/reference pair and a regularized pair, with well-posedness and a cutoff compatible with the actual corrector bounds. A slow cutoff controlling only its own regularized model does not do this.

PO-016 (new bounded initial interface): exact iid L2 pair projection formula and singular heat-cutoff orders, with a separate probability truncation analysis of close pairs. TASK-021 constructor and TASK-022 isolated falsifier are active. This addresses only initial iid preparation; it does not identify the actual backward corrector with the bare Riesz potential.

## Round 003 initial-law gate and sharpened remaining line

PO-016's exact iid moment/cutoff and sufficient probability subclaims are discharged by THM-015/016, AUD-011/012/013. General initial kernels obey the sufficient endpoint condition b_N ||Phi_0^N||_L2(mu_0^2)^2/N -> 0. This is a proved implication; the actual singular backward kernel has not been shown to satisfy its premise.

PO-017 (new): construct the actual singular full pair solution and prove an initial fluctuation-scale comparison with the explicitly defined cutoff internal-transport diagnostic H_(N,T). A sufficient bound is sqrt(b_N/N)||Psi_N(0)-H_(N,T)||_L2(mu_0^2)->0, for iid bounded-density mu_0, with b_N=min(beta_N,1). The forcing comparison must include relative diffusion, ordinary transport, both responses, actual test/source, periodic force remainder and the annular cutoff source. Singularity domains, collision passage and N/cutoff uniformity are part of the assertion, not assumptions to hide. A justified L1/probability comparison may replace the L2 premise if that norm is unavailable. OPEN.

PO-001 positive-time residual/bracket control, PO-004 critical hierarchy power counting and the singular-vs-regularized particle/reference comparison remain OPEN. Neither the raw-potential sharp converse nor the solvable zero-diffusion profile resolves them.

## Round 004 local diffusion input

PO-018 (bounded local input): prove the radial comparison while retaining relative diffusion, including construction/domain/source passage, for d>=s+2. THM020 supplies a complete proof and fresh AUD020 reconstruction; hostile review pending. This does not discharge PO017. TASK034 addresses finite-measure response/L2 propagation. TASK036 begins the periodic base pair potential for bounded nu and prescribed uniform C1 u/C2 f. Its exact norm and singular-semigroup assertions remain OPEN until the new proof is sealed and audited. The actual background/test bounds and nonlocal full inverse remain explicit dependencies.

PO018 now discharged in its exact local d>=s+2 scope by THM020, fresh AUD020 reconstruction and fresh AUD021 hostile PASS. The omitted full-operator and actual-law conditions of PO017/PO001 remain.

PO-019 (bounded response module) is discharged in the THM021 scope by fresh AUD023/024: finite-measure Coulomb compensation, Borel/Haar response bounds and exact heat convergence. Singular pair evolution is not supplied by smooth propagation. THM023/024 now isolate the direct initial-endpoint alternative to PO017, conditional on prescribed uniform background/test data and bounded diffusivity. Their independent R5 audits are pending. PO017's actual-data norms and finite-particle generator-domain passage, PO001 evolved residual/brackets and PO004 critical hierarchy remain OPEN.

PO020 (periodic base input) is discharged within THM023's prescribed C1 u/C2 f, d>=3,0<s<=d-2 and bounded-diffusivity scope by AUD026/027. THM024 supplies the independently reviewed conditional response composition. PO017's full initial analytic implication awaits exact THM025 interface/source qualification; actual-data inhomogeneous regularity, gradients/domain passage, PO001 and PO004 remain open.

Round005 direct endpoint gate: THM025 with AUD028/029 discharges the initial-endpoint objective behind PO017 in its exact prescribed-data and actual homogeneous scopes. The original literal closeness-to-diagnostic statement remains unproved and is unnecessary for this direct estimate; it is not relabeled proved. General actual-data norms, beta tending to zero and the particle domain remain open. Both response slots, Coulomb representative arguments and singular propagation are supplied by the separately audited modules.

PO021 (finite-N particle realization): THM026 candidate complete with fresh AUD031 reconstruction; TASK048 hostile pending. PO022 (weighted first-gradient prerequisite): THM027 OPEN, TASK049 construction and fresh TASK050 reconstruction active; constants may depend badly on N. PO023 (exact singular particle corrector domain): OPEN. Prove the time-dependent full inverse admits the exact N-particle Ito identity, differentiated background terms and singular approximation of all residual/bracket terms. Fixed-N particle existence and even H1 would not by themselves discharge this. PO001 evolved residual/bracket control and PO004 critical hierarchy remain OPEN.
