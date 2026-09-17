# Round 003 — sharp initial iid pairs and an exact internal-transport diagnostic

2026-09-17 UTC. Published input checkpoint: 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2. Initial pair construction worktrees began from a061786; all subsequent review worktrees used the published R2 checkpoint and separately hashed dossiers. The output is the atomic commit containing this report; the literal post-push receipt is kept under .git/campaign-records. No circular self-hash is inserted into the committed tree.

The starting broad gates were M0/M1 passed in the frozen smooth model, M2 open at singular critical power counting, and M3 with a bounded smooth iid finite-list subclaim but broader/fresh-session requirements open. The primary bounded assertion was PO-016: the exact initial iid pair projection and singular cutoff/probability interface, with every centering and N factor retained. Its negation is an admissible iid kernel or Riesz sequence violating one of the explicitly stated identities or limits. The independent constructions and separate hostile review discharge that bounded assertion. The full campaign gates are not thereby closed.

## Frozen model, routes and source status

All Riesz calculations use the unit torus, Haar probability, zero Fourier mode, coefficient pi^(s-d/2) Gamma((d-s)/2)/Gamma(s/2), positive 0<s<d, ordered distinct labels divided by N^2 and P_N=U_2/2. The iid scale is sigma_N=sqrt(N b_N), b_N=min(beta_N,1). The logarithmic model remains separate. The old beta_N N^(2s/d-1)->0, full-subcritical lambda_N=beta_N N^(s/d-1)->0 and critical lambda_N->positive finite are unchanged.

TASK-021 constructs the exact projection and heat estimates. TASK-022 independently reconstructs them, supplies the coefficient-one local heat representation and proves the spatial truncation bound. TASK-023 reviews both complete proofs. TASK-024 reconstructs the probability statement without its proof and separately discovers an L1 strengthening. Root constructs a sharp lower-probability converse. TASK-025 solves the proposed internal-pair transport model. TASK-026 reviews the converse and L1 extension, TASK-027 separately reviews the transport proof, and TASK-028 reconstructs the sharp statement without root's proof. Fresh TASK-029 independently reconstructs that same statement, TASK-030 conducts a separate hostile review, and TASK-031 reconstructs the transport statement with its own explicit cutoff. Exact roles, permitted inputs and seals are preserved in task cards and manifests.

No external quantitative theorem or novelty assertion is imported. Gaussian periodization and elementary conditional expectation, finite sums, polar integration and directly stated inequalities supply the new arguments. The private source remains absent and unused; the earlier primary-source covariance mismatch remains quarantined. Initial iid, Gibbs and positive-time interacting laws are never interchanged.

## Exact advances and scaling

For any symmetric L2(mu^2) kernel Phi=theta+h(x)+h(y)+H(x,y), with centered h and canonical H, the exact pair statistic is

    P_N[Phi] = -theta/(2N) - N^-2 sum_i h(X_i)
                 + N^-2 sum_(i<j) H(X_i,X_j).

Its second moment is theta^2/(4N^2)+||h||_2^2/N^3+(N-1)||H||_2^2/(2N^3), bounded by (N-1)||Phi||_2^2/(2N^3). The constant is universally sharp; a one-point law has no nonzero canonical extremizer when N>2. For atoms, the spatial diagonal is part of the product-law class; deleting equal labels does not delete distinct-label collisions. This gives the actual initial-corrector sufficient condition b_N||Phi_0^N||_2^2/N->0, without proving its premise for a singular backward solution.

The Haar heat squared norm has the exact squared multiplier exp(-8 pi^2 epsilon |k|^2), with orders 1, log(1/epsilon), epsilon^(-(2s-d)/2). At epsilon=N^(-2/d), its scaled variance has high-singularity order b_N N^(2s/d-2); at epsilon=N^(-4/d), the order is b_N N^(4s/d-3). The full proof supplies explicit max-shell two-sided constants. These are second-moment statements for cutoffs, not probability converses for the original statistic.

The unregularized potential is integrable for every s<d and has infinite pair second moment for 2s>=d at every finite N. The exact on-event truncation identity retains the mean shift (N-1)m_r/(2N), while the full campaign centering of the truncated kernel has a different shift -m_r/(2N). The union bound, mean error and centered variance yield probability convergence for all s<3d/4 at sqrt(N) scale; the temperature-dependent sufficient criterion above 2s=d is b_N N^(4s/d-3)->0. Both the logarithmic variance endpoint and arbitrary non-power-law temperature sequences are handled.

THM-018 strengthens this to L1: split g into separately centered inner and outer pieces at radius N^(-2/d), apply the exact outer second moment and only an inner absolute-mass estimate. The scaled rates are sqrt(b_N/N), sqrt(b_N(1+log N)/N), and sqrt(b_N)N^(2s/d-3/2) in the three respective ranges. No event excluding close pairs is required.

THM-019 supplies a separate necessity mechanism for d/2<s<d. Count pairs at distance below delta N^(-2/d). Haar pair indicators are pairwise independent, including shared-label pairs, giving a lower event probability c delta^d. The centered outer tail costs C delta^(2s), and the positive close-pair contribution absorbs the discarded mean. Since 2s>d, choose delta fixed and small. This proves P(P_N[g]>=a N^(2s/d-2))>=p>0, plus a matching first-absolute-moment order. Thus vanishing in probability is equivalent to vanishing in L1 and to b_N N^(4s/d-3)->0. Boundedness of that scalar sequence gives tightness; an unbounded subsequence has a further subsequence tending to infinity and gives non-tightness. At sqrt(N) scale the bare-pair boundary is 3d/4: vanishing below, tight nonvanishing at equality, non-tightness above. No endpoint distribution or stable law is identified.

## Solvable transport model and decisive limitations

THM-017 retains only the singular internal relative drift (2s/N)|z|^(-s-2)z and a static quadratic source s|z|^-s theta.A.theta, with zero diffusion and zero terminal condition. Its unique punctured characteristic solution is

    Phi_N = (N/4)(theta.A.theta)
       [(r^(s+2)+2s(s+2)tau/N)^(2/(s+2))-r^2].

The core radius is ell=(2s(s+2)tau/N)^(1/(s+2)). The profile has finite radial amplitude and exact local squared norm. Above 2s=d the squared norm grows only as N^((2s-d)/(s+2)) tau^((d+4)/(s+2)). A fixed radial cutoff defines a separate periodic L2 diagnostic; the annular source is displayed explicitly. For initial iid bounded-density preparation, its scaled squared endpoint is at most a fixed-data constant times b_N/N, b_N(1+log N)/N or b_N N^(-(d+2-s)/(s+2)), uniformly over deterministic remaining time in a bounded interval. All three vanish for s<d. The supremum is outside the expectation.

A nonzero traceless angular mode has positive squared norm even though its angular mean is zero. A nonscalar A has direction-dependent collision limits. Diffusion and both nonlocal response terms were deliberately absent from this declared model, and their addition is an unproved comparison. The transport audit proves the punctured Laplacian fails local L2 in dimensions 2–4 for a nonzero traceless component (and absolute L1 in dimension two), ruling out a separate unregularized L2 forcing estimate for that profile. Positive beta in the diagnostic scale does not turn this zero-diffusion equation into the actual temperature-dependent corrector.

OBS-011 records that infinite variance is not probability nonconvergence. OBS-012 records that the raw-potential threshold cannot be assigned to the actual backward corrector. No promoted theorem is retracted in this round; the R2 symmetry defect and repair remain unchanged. The fresh hostile reviewer did find overbroad subcritical prose in the unpromoted root diffusion-rescaling note. RET-002 and the separate erratum restrict rate-dependent coefficient limits to d>s+2: when d<=s+2, full subcriticality forces divergence. The submitted note remains byte-identical, and its punctured identity and critical classification survive. There is no full-target counterexample here.

## Audit dispositions

THM-015: AUD-011 comparison PASS and AUD-012 hostile PASS. THM-016: AUD-013 statement-only comparison PASS and AUD-012 hostile PASS. THM-017: AUD-014 hostile PASS, with explicit all-N constant completion. THM-018/019: separate AUD-015 hostile PASS; SH-01 explicitly supplies a further diverging subsequence for one sentence of the sharp proof. THM-019 also has AUD-016 prior-context statement-only comparison PASS. Exact constants, atomic scope and all temperature factors were reviewed. Fresh AUD-017 grants THM019 reconstruction PASS, and AUD-018 grants THM017/018/019 hostile PASS, with exact independent clarifications and FH-D01. The fresh THM017 reconstruction is recorded separately after its seal. Original candidate cards and issued reports retain their original wording and hashes.

The first R3 reviews reused contexts with explicit claim-specific nonparticipation. Once workers completed, genuinely fresh contexts were accepted for TASK-029/030/031. Their sealed outcomes are recorded separately below; no prior report is relabeled fresh. No constructor certifies its own theorem, and a statement-only role alone does not imply a fresh session. Publishing this authorized research checkpoint is not a declaration that the full manuscript-release gate has passed.

## Computation, artifacts and current flagship

The verification certificate records independently authored exact finite checks, root reruns, environment and all artifact/integrity outcomes. Those computations test coefficients and exponents; the complete analytic proofs establish the continuous and asymptotic statements. The seven-page mathematical TeX/PDF gives the main identities and proofs; full constants and audit scopes live in the sealed Markdown reports. Original source and authority files remain byte-identical.

THM-003/004, M2, the broader M3 gate and M4–M7 remain OPEN. No actual singular hierarchy survival/resummation theorem, positive-time model comparison, field/path tightness or Gibbs transfer was proved. Root remains Astra Ultra with Astra Max workers. The committed project setting requests ten workers, while the initialized runtime still provides root plus three. A spawn rejected while occupied succeeded after a worker completed; fresh contexts are available in successive batches. No ten-active-worker or hot-reload claim is made.

## First open assertion and next actions

PO-017 is now concrete: construct the genuine full singular pair corrector Psi_N and prove, for a specified cutoff-compatible solution class,

    sqrt(b_N/N) ||Psi_N(0)-H_(N,T)||_L2(mu_0^2) -> 0,

or a justified fluctuation-scale L1/probability replacement. The comparison must include diffusion, ordinary transport, both response terms, actual test/source, periodic-force remainder and cutoff annular forcing. Collision-domain and limiting arguments are load bearing. Even that endpoint comparison would leave PO-001 evolved-law residuals/brackets and PO-004 critical power counting open.

Next: (1) execute the independently staffed TASK-032/033 diffusion-retaining local comparison in d>=s+2, with explicit collision domain and angular modes; (2) derive full-operator forcing/comparison estimates in a norm that can handle its collision behavior; (3) transfer to the actual evolved law and audit the singular limit before any hierarchy closure. Continue fresh-session reviews in available batches, preserving exact existing seals and honest audit history.

Canonical summary: MEMORANDA/hocf_round003_20260917T201600Z.tex and its PDF. Complete proof/audit paths, first open lines for other routes and reproducible handoff are in REPORTS/CHECKPOINTS/NEXT_INVOCATION.md. Commit and live-remote equality are recorded immediately after publication, without amending history.

Final fresh transport disposition: AUD-019 grants FRESH ISOLATED_RECONSTRUCTION_PASS after full comparison of the formula, characteristic solution class, all-N norm bounds and iid endpoint. Its explicit radial cutoff differs from the constructor example but lies in the same declared family; this is stated explicitly, not hidden as identical kernels. Extra derivative observations remain covered by fresh hostile AUD-018. All issued evidence stays unchanged.
