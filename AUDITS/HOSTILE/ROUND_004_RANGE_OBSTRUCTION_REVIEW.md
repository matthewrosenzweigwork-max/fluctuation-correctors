# TASK037 hostile review: corrected Round 004 annular range obstruction

Issued 2026-09-17 UTC. Candidate: `MEMORANDA/ROUND_004_SUPERHARMONIC_RANGE_OBSTRUCTION_V2.md`, SHA-256 `faa668b30ee77d4826348412c85a936bbbafba22873e9b566d4db788a05fdb95`.

**Mathematical verdict: PASS for the fixed-parameter, sufficiently-small-time, killed-annulus obstruction stated at V2 lines 9–17.** The stopped calculation proves the strict inequality for every time in the submitted positive interval. No substantive failure was found in that proof, and no mathematical repair is incorporated into this verdict. The source's broader full-corrector mission is untouched.

There are two qualifications to a completely unqualified document-level approval: the opening sentence calls a stronger obstruction the “exact negation” of a comparison extension, which is not literally the same logical proposition; and the claim about THM020's contents cannot be source-certified from this sealed dossier. Neither is used to prove the annular obstruction. Details and separate verdicts appear below.

**Actual audit mode:** fresh-worktree hostile examination and independently recomputed algebra of the supplied proof; **not a blind reconstruction performed before exposure to that proof**. I read the submitted V2 narrative before writing the reconstruction below. I did not read other constructor outputs, root conditional notes, new reviews, memory, or the manuscript cited by THM017. Under a strict reading of the repository requirement that reconstruction precede exposure to a constructor's narrative, this report does not fulfill that procedural gate. Its mathematical checks must not be relabeled as a blind audit. Root alone assigns canonical identifiers and audit/promotion status.

## 1. Sealed scope and source preflight

The isolated worktree is `/tmp/hocf-r004-range-hostile-20260917`, branch `codex/hocf-r004-range-hostile`, created from published commit `52bda5d0d24067b051c6fe9763f2a78e7599e593`. The six inputs listed in `AUDITS/ROUND_004_RANGE_HOSTILE_INPUT_SHA256SUMS.txt` were copied byte-for-byte and verified before substantive reading. The manifest's own SHA-256 is `9fd8c7490aa03dd56f395946efe51893751cbfc10d63eccf6cf940519e0bf992`.

The complete read set was:

- `TASKS/ACTIVE/TASK-037_ROUND004_RANGE_HOSTILE.md`;
- `AUDITS/ROUND_004_RANGE_HOSTILE_INPUT_SHA256SUMS.txt`;
- corrected candidate V2 and preserved V1;
- `THEOREMS/THM-017_INTERNAL_PAIR_TRANSPORT_MODEL.md`;
- `AGENTS.md`;
- `TASKS/ACTIVE/ROUND_001_MODEL.md`.

The task-specific sealed-input restriction was followed in preference to the general instruction to consult the wider README, orchestration documents, and canonical ledgers. No root files or canonical state records were changed. No commits, pushes, dependency installations, child workers, or external source retrieval were performed.

THM017 lines 5–13 provide exactly the local radial zero-diffusion formula used below. Its other claims, its referenced proof, its iid endpoint, and its subsequent audit status were not imported. Smooth Itô calculus is explicitly permitted by the frozen model; the bounded-drift existence argument is supplied below rather than attributed to an unverified source. The periodic Fourier constant is not used. The audit makes no bibliographic or novelty claim.

The original V1 was inspected only as correction provenance. A direct diff shows that V2 adds the correction heading/note and replaces `s^3` by `s^4` in the two third-derivative coefficient occurrences; the remaining proof and its scope are unchanged. V1 is not the candidate being approved.

## 2. Exact assertion and logical negation

Let d be a positive integer, let 0<s<d and s>d−2, let N≥2 be a fixed particle number, let nu>0, and let z0≠0. Interpret the finite annulus in its usual nondegenerate sense:

    0 < a < r0 := |z0| < R < infinity,
    D = {z in R^d : a < |z| < R}.

The assumption a>0 is also forced by the submission's assertion that its singular drift has a bounded Lipschitz extension agreeing near the closed annulus. The candidate is not a claim about a punctured ball whose closure contains the origin.

Set p=s+2 and

    v(z) = (2s/N)|z|^(-s-2) z,
    j(z) = s|z|^(-s),
    L = 2nu Delta + v.grad,
    F(tau,r) = (N/4)[(r^p + 2sp tau/N)^(2/p) - r^2].

The process has this generator up to exit from D and is killed at its first exit rho. The assertion is

    for every fixed admissible tuple (d,s,N,nu,z0,a,R),
    there exists tau0>0 such that for every 0<tau<tau0,
    E_z0 integral_0^(tau wedge rho) j(Z_h) dh > F(tau,r0).

For a fixed tuple, its exact logical negation is

    for every epsilon>0 there exists tau in (0,epsilon)
    such that U_D(tau,z0) <= F(tau,r0).

The negation of the universally quantified assertion is the existence of an admissible tuple with this latter property. V2 line 17's fixed-data formulation is correct. The proof below rules that property out.

A general extension of coefficient-one majorization would assert an upper inequality. Its negation requires a counterexample, or arbitrarily small counterexamples if the extension concerns a sufficiently small interval. The submitted assertion proves the stronger statement of strict reverse inequality throughout an interval, for every admissible fixed tuple in the excluded range. Thus the opening “exact negation” characterization at line 5 is imprecise if read as literal logical equivalence; the obstruction itself is valid.

## 3. Process, coefficients, and stopped identities

### Local realization

Because the closed annulus has positive distance from the origin, choose a smooth compactly supported scalar cutoff equal to one on a neighborhood of that closed annulus and zero on a neighborhood of the origin. Multiplying v by this cutoff and setting the result equal to zero at the origin gives a globally bounded smooth drift with bounded derivative, hence a globally Lipschitz drift v_tilde.

With a standard d-dimensional Brownian motion B, the integral equation is

    Z_h = z0 + 2 sqrt(nu) B_h + integral_0^h v_tilde(Z_u) du.

For each continuous Brownian path, Picard iteration is a contraction on time intervals shorter than the reciprocal of the Lipschitz constant. Iterating these intervals constructs a unique continuous solution for every finite horizon. Boundedness of the drift excludes a finite-time explosion. The solution is adapted because each Picard iterate is adapted. Local pathwise uniqueness shows that changing the cutoff outside the neighborhood of the annulus does not change the process before rho.

The diffusion covariance is 4nu I, so the generator is exactly 2nu Delta+v.grad on D. This is consistent with the frozen particle model: the difference of two independent noises of amplitude sqrt(2nu) has amplitude 2sqrt(nu). The internal mutual drift difference is twice K(z)/N; for the local principal kernel |z|^(-s), K(z)=s|z|^(-s-2)z. These coefficient checks do not identify the constructed process with an actual interacting-pair law: all other particle forces and background terms are absent from this local model.

There is no problem when d=1: the annulus consists of two open intervals, and the initial point lies in one of them. The construction and compactly supported tests apply on that component. No origin formula, singular Itô limit, or boundary smoothness theorem is needed.

Since 0<=j<=s a^(-s) on D, U_D is finite and at most s a^(-s) tau. A possible value of j at the single exit time makes no difference to the time integral.

### Two stopped Itô applications

Choose chi in C_c^infinity(D), with 0<=chi<=1 and chi=1 on a neighborhood of z0, and put phi=chi j. Such a choice exists because z0 is an interior point. The function phi and all its derivatives vanish near the boundary. Because the drift is smooth away from zero, phi, Lphi, and L^2phi all have compact support in D. Their zero extensions are smooth on R^d; phi and Lphi are zero both on the exit boundary and at the cemetery state.

For f=phi or f=Lphi, stopped Itô gives

    f(Z_(h wedge rho)) = f(z0)
      + integral_0^h 1_(u<rho) Lf(Z_u) du
      + 2sqrt(nu) integral_0^h 1_(u<rho) grad f(Z_u).dB_u.

For every finite h, the stochastic integral is a true square-integrable martingale: its second moment is at most 4nu h ||grad f||_infinity^2. This, rather than an unsupported optional-stopping assertion, justifies its zero expectation. The drift integral is bounded by h||Lf||_infinity, so Fubini is legitimate.

Path continuity and the zero boundary value give

    f(Z_(h wedge rho)) = 1_(h<rho) f(Z_h).

This identity remains correct on the event h=rho because the boundary value is zero. Define S_h f(z0)=E[1_(h<rho)f(Z_h)]. Then

    S_h phi = phi(z0) + integral_0^h S_u Lphi du,
    S_u Lphi = Lphi(z0) + integral_0^u S_w L^2phi dw.

These are the submitted identities, with no boundary contribution omitted. An arbitrary source j that does not vanish at the boundary would not satisfy this simple killed identity with initial value j(z0); using the compactly supported phi is the decisive justified step.

Direct expectation gives |S_w f|<=||f||_infinity. Consequently, for

    B = ||L^2phi||_infinity,D < infinity,

one has the exact integral remainder and its bound

    S_h phi - phi(z0) - h Lphi(z0)
      = integral_0^h integral_0^u S_w L^2phi dw du,
    |S_h phi - phi(z0) - h Lphi(z0)| <= B h^2/2.

Finally phi<=j in D, so positivity and Tonelli imply

    U_D(tau,z0) >= integral_0^tau S_h phi(z0) dh
      >= tau j(z0) + (tau^2/2)Lj(z0) - B tau^3/6.

The equalities at z0 use chi=1 on a neighborhood, which eliminates its derivative terms there. The lower-bound direction is correct. The derivatives of chi elsewhere remain in B and have not been discarded.

## 4. Derivatives, remainders, and the explicit interval

Write A_tau=r0^p+2sp tau/N. Direct differentiation of THM017's formula gives

    F(0,r0) = 0,
    partial_tau F = s A_tau^(-s/p),
    partial_tau^2 F = -(2s^3/N) A_tau^(-s/p-1),
    partial_tau^3 F = [4s^4(2s+2)/N^2] A_tau^(-s/p-2).

The coefficient of the last line is obtained as

    (2s^3/N) (s/p+1) (2sp/N)
      = 4s^4(s+p)/N^2 = 4s^4(2s+2)/N^2.

The radial powers at tau=0 are respectively r0^(-s), r0^(-2s-2), and r0^(-3s-4). The source derivatives independently give

    grad j(z) = -s^2 |z|^(-s-2) z,
    v.grad j(z) = -(2s^3/N)|z|^(-2s-2),
    Delta j(z) = s^2(s+2-d)|z|^(-s-2).

The submitted coefficient s^4 and every N factor in V2 are therefore correct. For tau>=0, A_tau increases and the third derivative is positive and decreases. In particular,

    0 <= partial_tau^3 F(tau,r0) <= C_F,
    C_F = [4s^4(2s+2)/N^2] r0^(-3s-4).

The ordinary one-variable integral Taylor remainder is

    R_F(tau) = (1/2) integral_0^tau (tau-u)^2 partial_u^3 F(u,r0) du,
    0 <= R_F(tau) <= C_F tau^3/6.

This proves the submitted absolute-value bound on [0,1], and in fact the same bound holds for every nonnegative tau. No spatial-semigroup Taylor assertion for an unbounded singular source is being used.

Subtracting this upper expansion for F from the lower expansion for U_D yields exactly

    U_D(tau,z0) - F(tau,r0)
      >= (tau^2/2)[Lj(z0) - v.grad j(z0)]
         - (B+C_F)tau^3/6
      = c tau^2 - (B+C_F)tau^3/6,
    c = nu s^2(s+2-d) r0^(-s-2) > 0.

The factor 2 in the diffusion generator cancels the Taylor factor 1/2; there is no missing factor of two. Let

    tau0 = min(1, 3c/(B+C_F+1)).

This is finite and strictly positive. For 0<tau<tau0,

    (B+C_F)tau/6
      < (c/2)(B+C_F)/(B+C_F+1) < c/2,

which proves the strict inequality, with the submitted lower bound c tau^2/2. Both alternatives in the minimum defining tau0 satisfy this estimate.

The time is explicit after chi is chosen, through the finite quantity B. The manuscript does not give a numerical formula for B solely in a,R,z0, nor a single uniform time across varying initial points, annuli, exponents, or diffusivities. None is needed by its fixed-data assertion. One can fix the smooth cutoff as a function of the given annulus and point; no additional hypothesis is required.

## 5. Independent sign and falsification checks

### Spatial radial check

There is an independent direct check of the claimed threshold and of the near-zero-time sign, without relying on an expansion of the killed source. At r>0 let

    x = r^p/(r^p+2sp tau/N),
    G(x) = x^(s/p)[d+s(1-x)].

Differentiating the explicit spatial profile gives

    Delta F(tau,r) = (N/2)[G(x)-d],
    G'(x) = (s/p)x^(s/p-1)[d+s-(2s+2)x].

At tau=0, x=1 and G'(1)=(s/p)(d-s-2). Thus for s>d−2, decreasing x slightly from one makes G(x)>d, so Delta F is positive at each fixed r for all sufficiently small positive tau. More precisely,

    lim_(tau down to 0) Delta F(tau,r)/tau
      = s^2(s+2-d) r^(-s-2) = Delta j(r).

For 0<s<=d−2, the bracket in G' is nonnegative on 0<x<=1, hence G(x)<=G(1)=d and Delta F<=0. At the threshold the first time derivative vanishes, consistently with the zero second-order occupation difference. These calculations verify the sign statements independently. They do not verify the unprovided contents or full hypotheses of THM020.

### Attempts to break the stopped argument

- **Boundary killing:** killed j itself has a boundary mismatch, but the two Itô tests are phi and Lphi, both identically zero near the boundary. This avoids a lost boundary term. Arbitrarily narrow annuli or initial points close to the boundary can increase B and shrink the certified interval; they do not invalidate existence of that interval for fixed interior data.
- **Low dimensions:** both d=1 and d=2 satisfy s>d−2 for every allowed positive s. The punctured-coordinate drift is used only on the finite annulus, so no collision or angular regularity claim is needed.
- **Small positive diffusion:** c is positive for every fixed nu>0. Merely taking nu positive but small cannot restore this same coefficient-one inequality on a sufficiently small interval for those fixed data. An alternative comparison with a nu-dependent error, a different profile, or the case nu=0 has not been excluded. This is the precise interpretation necessary for the informal “smaller-nu perturbation” exclusion at V2 line 66.
- **Sign and Taylor direction:** the transport remainder is positive. The proof correctly subtracts an upper bound for it from a lower bound for the occupation. Subtracting a lower bound for it would not suffice; no such reversal occurs.
- **Law transfer:** no iid, equilibrium, stationary, modulated-Gibbs, or actual interacting-particle assertion is made. Fixed finite N is not an asymptotic parameter in this argument.

### Exact finite arithmetic battery

`ROUND_004_RANGE_OBSTRUCTION_EXACT_CHECK.py` uses only Python's standard-library rational arithmetic. It performs 234 transport-derivative coefficient comparisons over 26 dimension/exponent rows and N=2,3,97; checks the source Laplacian sign above, at, and below the threshold; and performs 2,880 exact checks of the positive-time estimate with varied positive nu and varied nonnegative values of B. The values of B in that algebraic check test the submitted inequality for abstract nonnegative bounds; they are not represented as computed norms of a chosen cutoff.

It also checks 63 actual transport Taylor remainders at r0=1. These are exact rather than floating-point checks: if 2/p=m/n in lowest terms, choose A_tau=(1+delta)^n, so its 2/p power is the rational (1+delta)^m. All 63 V2 remainder bounds pass. In 36 of these cases, with s>1, the preserved V1 remainder bound actually fails.

For example, take admissible d=3,s=2,N=2,r0=1 and delta=1/1000, put A_tau=(1+delta)^2, and choose tau=((1+delta)^2-1)/8. Then

    F(tau,1)=delta/2,
    R_F(tau)=delta^3(4+delta)/16,
    C_F(V2)=96, C_F(V1)=48,
    R_F / [C_F(V2)tau^3/6] = 2(4+delta)/(2+delta)^3 < 1,
    R_F / [C_F(V1)tau^3/6] = 4(4+delta)/(2+delta)^3 > 1.

This confirms that the V1 coefficient was a substantive bound error for s>1, rather than merely an alternative constant, and that the V2 correction fixes the audited formula. The finite battery supports falsification and coefficient checking; the continuum proof is the preceding analytic argument. There is no stochastic simulation, random seed, floating-point inference, or dependency installation.

## 6. Individual verdicts and exact scope

The identifiers in this table are local to this review and do not allocate canonical campaign IDs. Source line numbers refer to the sealed V2 file.

| Local item | Submitted assertion | Verdict | Finding |
|---|---|---|---|
| TASK037-C01 | Fixed-data killed annular realization, lines 9–13 | PASS | A positive inner radius and finite outer radius give the stated cutoff construction and finite occupation. |
| TASK037-C02 | Generator/source/transport normalization, lines 9, 38–47 | PASS | Diffusion is 2nu Delta, drift is 2s/N, source is s r^(-s), and the profile's prefactor is N/4. |
| TASK037-C03 | Compact support and both killed Dynkin identities, lines 21–28 | PASS | phi and Lphi vanish at exit; their stopped stochastic terms have zero expectation. |
| TASK037-C04 | Lower occupation Taylor bound, lines 30–34 | PASS | phi<=j gives the correct lower direction, with coefficient B/6. |
| TASK037-C05 | Corrected first, second, and third transport derivatives and C_F, lines 38–47 | PASS | The s^4 coefficient, radius power, and uniform time remainder are correct. |
| TASK037-C06 | Subtraction and positive second-order coefficient, lines 49–56 | PASS | The surviving term is exactly nu Delta j tau^2. |
| TASK037-C07 | Explicit positive tau0 and strict inequality for every smaller positive time, lines 58–62 | PASS | The submitted minimum gives the stated c tau^2/2 lower bound. |
| TASK037-C08 | Threshold and low-dimensional sign statements, lines 62, 66 | PASS | Direct spatial differentiation verifies the sign and vanishing threshold coefficient. |
| TASK037-C09 | Fixed-data logical negation at line 17 | PASS | Its quantified meaning is stated in Section 2; the proof excludes it. |
| TASK037-C10 | Opening “exact negation” characterization at line 5 | FAIL, literal wording only | The proved uniform-in-small-time obstruction is stronger than the logical negation of a general upper-comparison extension. No substantive proof line depends on the equivalence. |
| TASK037-C11 | THM020 includes the threshold, line 66 | FAIL to source-certify from the permitted dossier | THM020 was not among the sealed inputs. This is not a finding that THM020 is false. The radial sign itself was independently verified. |
| TASK037-C12 | Conditional extension to a global positive-source realization, line 68 | PASS, conditional exactly as written | Agreement up to annular exit and nonnegative later occupation imply domination; existence is not supplied. |
| TASK037-C13 | Exclusion of full-corrector, interacting-law, and critical-regime conclusions, lines 66–70 | PASS | The proof establishes only the local finite-parameter comparison obstruction. The small-positive-nu qualification in Section 5 applies. |
| TASK037-C14 | V1-to-V2 correction description, line 3 | PASS | Direct byte-level input verification and textual comparison confirm only the stated coefficient correction plus its notice. |

There is **no first substantive failing line** in the claimed annular proof. The first literal wording issue occurs at line 5. The source-verification limit occurs at line 66. This review neither edits nor silently replaces either sentence.

For the conditional statement at line 68, “agrees” must mean equality of the stopped path law up to rho, or a coupling with that agreement. On such a coupling, the full integral of a nonnegative source dominates its integral up to tau wedge rho pathwise. Its expectation therefore dominates U_D. An infinite full expectation would also satisfy the strict comparison, interpreted in the extended real sense. This observation proves no global realization theorem.

No conclusion is certified concerning a constant greater than one, a changed source or profile, a nonlocal boundary prescription that does not agree with this stopped process, a correction with an added nu-dependent error, a singular limit, a uniform joint scaling limit, fluctuations, or nonexistence of a full corrector. For any other realization that does satisfy the explicit local-agreement and nonnegative-source condition, the conditional inheritance statement applies and that realization is not an escape from this local obstruction.

## 7. Verification, deliverables, and seal

Exact verification command in the isolated worktree:

    python3 AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_EXACT_CHECK.py

It exited successfully. The saved JSON contains the complete finite-case parameters and counts. The original six-file input manifest was checked both before reading and at sealing; all hashes matched. The audit inputs were unchanged. No TeX source was produced or compilation claimed; the requested sealed audit is a Markdown artifact.

Deliverables:

- `AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_REVIEW.md` — this report;
- `AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_REVIEW_INPUT_SHA256SUMS.txt` — the six inputs and the original dossier manifest;
- `AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_EXACT_CHECK.py` — reproducible exact finite checks;
- `AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_EXACT_CHECK_RESULTS.json` — complete saved results;
- `AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_REVIEW_OUTPUT_SHA256SUMS.txt` — hashes of the report, input manifest, check program, and saved results. As usual, the output manifest excludes itself to avoid self-reference.

The report is immutable after issuance. Any later correction requires a separate superseding report. Root may consume the mathematical verdict with the explicit source and non-blind-audit qualifications above; the worker does not assign campaign promotion status. TASK037 ends at this seal, with no further task continuation.
