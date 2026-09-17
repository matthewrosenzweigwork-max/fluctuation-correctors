# AUD-004 — comparison of the sealed all-order reconstruction

2026-09-17, root Astra Ultra integration. Verdict: ISOLATED_RECONSTRUCTION_PASS for THM-001's finite-smooth drift, martingale and full bracket identities, every finite k,N including k>N. M2 remains OPEN at critical power counting.

## Isolation and inputs

The blind report is AUDITS/BLIND_RECONSTRUCTION/ROUND_002_ALLORDER_RECONSTRUCTION.md, hash f96a78c701829b3744b0ffb05748db2aa38426f09da5eb9d26f85864a5e47747. It was sealed before comparison and before residual hostile-review inputs were delivered. Its only mathematical input was the frozen model and exact task card in a worktree at installation commit 475a5399828bc6e2ccbade08c59b8778638df14a, which contains no constructor proof. Prior use of that context was operational configuration research; the report discloses its permitted reads. The active runtime cap prevented a fresh fourth worker; mathematical input isolation, not fresh-session status, is the claim.

Constructor comparison inputs are THEOREMS/THM-001_SMOOTH_RECURSION.md and MEMORANDA/ROUND_001_RECURSION.md as published at a06178658d1e3d458536ff312ca793947212ec67. The constructor already passed separate hostile review AUD-002. Root compares the separately derived equations; root construction or finite computation alone does not supply independent status.

## Exact mapping

- Blind A_k equals constructor L_k, including the positive background response R_a. Blind unsymmetrized B_k equals constructor upward A_k^+ after ordinary averaged symmetrization; U is permutation invariant, so its value is unchanged.
- Blind T_k equals constructor internal C_k. Blind single-pair lower kernel C_k is one summand of constructor Q_k; by symmetry U_(k-1)[Q_k]=(k-1) U_(k-1)[C_k(blind)]. Thus blind k(k-1)/N and constructor k/N times the sum of k-1 terms agree exactly. Blind Q_k equals constructor R_k; both carry binomial(k,2)/N. Blind (7)/(11) therefore agree with constructor (R1) without redefining a coefficient.
- Blind (15)/(16) is the same differentiated leave-one-label-out statistic as constructor (R3), with denominator N, factor k and noise sqrt(2/beta). Blind (17) equals constructor (R4).
- For brackets, the constructor fixes the common differentiated root, chooses occupied subsets A,B of the other slots and a partial bijection of q additional common labels. The blind formula counts p=q+1 common edges in the two full blocks, one distinguished as the Brownian edge. Its coefficient has exactly 2/(beta N^p), and its number of distinguished matchings is p binomial(k,p) binomial(ell,p) p! = k ell binomial(k-1,p-1) binomial(ell-1,p-1)(p-1)!.
- Expand each factorial quotient D in constructor (R5) by its U/background subset inverse. The original alternating subset signs cancel every term in which an unmatched slot is moved to background. Each matched quotient slot is forced empirical before inversion and may either remain in U or be integrated once against mu. Blind forced-slot identity (3) gives precisely this positive sum over subsets of the p matched slots. Hence blind (20) and its compressed form (23) equal constructor (R5), including every coefficient, sign and kernel contraction. Spatial derivatives are taken before identifying slots in both derivations.

No normalization discrepancy remains. The apparent k versus k(k-1) discrepancy is solely the explicitly different definitions of the lower kernel. The apparent alternating versus positive bracket coefficients is the stated factorial-to-centered inversion, not positivity of individual terms.

## Checks and disposition

The blind reconstruction separately proves the forced-slot cancellation, both matching counts, direct one-body identity, pair and next-order reductions, constants and unused-slot formulas. Its new all-centered bracket representation is an exact equivalent form, and does not replace the frozen constructor representation. Exact self-checks cover 20 drifts, 64 brackets, 20 constants, 204 matching counts and 21,845 cancellation coefficients. These are supporting finite computations; the general proof and exact mapping above are the load-bearing comparison.

THM-001 now has both ISOLATED_RECONSTRUCTION_PASS (AUD-004) and HOSTILE_REVIEW_PASS (AUD-002), within its exact finite-smooth scope. No singular passage, order-uniform bound, local-equilibrium closure or critical survival statement is promoted. Issued input reports, theorem card and original audit remain byte-for-byte unchanged. This comparison is immutable; later corrections require a new report.
