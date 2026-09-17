# TASK-025 — a solvable singular internal-pair corrector

2026-09-17. Astra Max /root/capacity after sealing TASK-022. New construction in /private/tmp/hocf-round003-pair-transport-20260917, based on published R2 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2. Root proposed this bounded diagnostic; it is not an independent certification by either participant. No canonical edits or scientific mission change.

Exact question: in the local Euclidean relative coordinate z=x-y, 0<|z|<infinity, take K(z)=s z |z|^(-s-2), 0<s<d, zero diffusion, no background response and no external/common transport. For a fixed real symmetric matrix A and f(x)=x.A.x/2, let J(z)=s |z|^(-s) (z/|z|).A.(z/|z|). Solve the exact final-value equation

    (partial_t + (2s/N)|z|^(-s-2) z.grad_z) Phi_N(t,z) = -J(z),
    Phi_N(T,z)=0, z!=0, N>=2.

This retains exactly the internal B/N transport and the quadratic-test source, but deliberately omits the full torus response/diffusion terms. Prove uniqueness in an explicitly stated characteristic class, the exact closed formula, sharp near/far bounds on every fixed ball, and local L2 growth in N and tau=T-t for the cases 2s<d, 2s=d, 2s>d. Handle angular sign and nonzero traceless A, the endpoint tau=0 and any discontinuity at z=0; do not assume a smooth extension at coincidence. Exact negation: admissible data violate the proposed formula or claimed bound.

Translate those local kernel bounds into an initial iid pair endpoint estimate only for a separately defined compactly supported symmetric periodic diagnostic kernel, with an explicit cutoff inside an embedded torus ball and bounded-density mu. Use the sealed TASK-022 projection formula as a prerequisite if helpful. Determine whether that diagnostic endpoint is negligible at sigma_N=min(sqrt(N beta_N),sqrt N) for all s<d. Do not claim the cutoff kernel solves the full backward equation: show its added source/boundary term if invoking its equation, or use it only as an L2 test kernel. No extrapolation to positive-time interacting laws.

The purpose is to test whether the actual retained 1/N pair transport can change a bare Riesz singularity before one attempts the full corrector. A successful toy model is evidence for a mechanism, not a solution of the missing response/diffusion/model-comparison obligations. State exactly which terms were omitted and which uniform bounds would be needed to extend it.

Required output MEMORANDA/ROUND_003_PAIR_TRANSPORT_MODEL.md with full derivation, signs, constants, all scaling, isotropic and traceless tests and first open full-operator line. Supporting exact code optional. No external remembered source theorem is needed. No commits/pushes, dependency changes, canonical edits, child workers or TeX changes. Seal report before a separately allocated hostile review. Root alone assigns new theorem ID and integrates; your report remains SELF_CHECKED at submission.
