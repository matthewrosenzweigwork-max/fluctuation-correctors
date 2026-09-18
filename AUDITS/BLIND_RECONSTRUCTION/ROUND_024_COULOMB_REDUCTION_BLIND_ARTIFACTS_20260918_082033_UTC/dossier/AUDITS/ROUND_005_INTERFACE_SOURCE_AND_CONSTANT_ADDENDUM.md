# Round005 full-pair interface source and constant addendum

2026-09-17. Root disposition of TASK044-D1/D2 after the fresh hostile report is sealed. Original THM025 card, interface proof and review remain byte-identical. The report's REPAIR_REQUIRED source-interface verdict is preserved; this addendum is the proposed explicit repair, pending the source auditor's separate check. No range, centering, iid coefficient or rate is changed.

## Exact source for the local kernel premise

The shorthand THM021 in interface memorandum line9 refers to its complete proof, not solely the concise theorem card. The exact source is MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md, SHA256135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be, Section2, lines69–109, equations(2.1)–(2.4). It proves the positive heat representation with the frozen gamma/Fourier constant, identifies its Euclidean principal term with coefficient one, and proves a smooth local remainder through zero and smoothness away from zero by dominated differentiation of the two heat-time ranges. Evenness follows from the explicitly even heat representation and the even local power. Thus every local hypothesis required by THM023 is supplied for the exact frozen Fourier kernel.

This was independently reconstructed before THM025 existed: AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RESPONSE_RECONSTRUCTION.md, SHA256e07df6f4285cdb2dbb3a4fd28ab7cf325a355c75129378118f29a7fd76df53f1, Section1, explicitly computes the coefficient-one Euclidean heat integral and the smooth remainder. Fresh hostile AUD023, AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_REVIEW.md, SHA25606bccaa37a0c7018e1595d14662289c2c4be28017ee673abf8dffe2dc600aaa1, claimC01 and Section3.1, checks that normalization and every local differentiation bound. Their input/output seals remain preserved.

The THM021 card does omit this local preflight lemma, as TASK044-D1 correctly observes. The card-only interface dossier did not contain these full proof locations; it is not retroactively treated as containing them. This addendum explicitly adds the verified source lemma to the application of THM023. TASK044 also independently derived the same bridge as additional reviewer work; the present source qualification does not rely on an auditor certifying its own new proof.

## One common divergence constant

In the interface proof and subsequent synthesis, choose the symbol kappa to be the maximum of the finite lower-divergence constant supplied by THM021 and C0=||(R_g)_-||infty from the chosen THM023 local decomposition. Increasing a lower-bound constant preserves divK>=-kappa. Then, directly from the THM023 statement,

    ||S_(t,a)||_(2->2) <= exp[(D_u+C0/N)(a-t)]
                      <= exp[(D_u+kappa/2)(a-t)], N>=2.

Thus c=D_u+kappa/2 in the interface proof is justified without identifying two constants from different cards or importing the smooth-cutoff result as a singular theorem. Equivalently, c=D_u+C0/2 is sufficient. The response bound C_R=2[M0 TV(D_K)+M1||K||1] is unchanged, and neither constant depends on N or nu in the prescribed interval. No optimal/minimal divergence constant was claimed by THM025.

With these two explicit source/constant dispositions, every premise used by the original interface proof is supplied by the stated modules and the exact cited local preflight lemma. The fresh hostile report's remaining conditional passes and its independently proved Fourier/iid facts are preserved. A separate source-addendum review must record whether TASK044-D1/D2 are discharged; root does not assign independent status to its own clarification.
