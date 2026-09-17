# THM-001 — exact smooth deleted-label hierarchy

Version 1.0, 2026-09-17 UTC. Mathematical status: EXACT_IDENTITY. Audit status: HOSTILE_REVIEW_PASS in AUD-002; isolated general-proof reconstruction has not yet been performed. Source dependency: none beyond smooth Itô calculus, finite sums and torus integration by parts.

For every d>=1, N>=2, finite T, beta>0, smooth real even mean-zero g and smooth V on the unit torus, every smooth positive solution mu of the frozen mean-field equation, every initial particle law, every integer k>=1 and deterministic symmetric C1-time smooth-space kernel Phi, equations (R1), (R3) and (R5) of MEMORANDA/ROUND_001_RECURSION.md hold exactly. The model and all definitions are frozen in TASKS/ACTIVE/ROUND_001_MODEL.md. Tuples have distinct labels, denominators N^k, and centering by the specified mu. This includes k>N and coincident positions of different labels.

Exact negation: one such datum violates the displayed drift, particle-gradient martingale or partial-bijection bracket formula. The finite-subset proof excludes that negation at fixed smooth g. Smoothness ensures all finite-time integrals and square integrability. No singular or infinite-order limit is part of this statement.

Proof: recursion memorandum Sections 2–6. Explicit manual k=1,2,3 reductions; two separately written exact Fourier batteries through k=4; all support cancellation coefficients checked through k=9. Finite tests corroborate rather than replace the general subset proof. M2 stays OPEN because the critical power-counting theorem is absent, and isolated general-proof reconstruction is not inferred from isolated pair reconstruction.
