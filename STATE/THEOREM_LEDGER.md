# Theorem ledger

| ID | Statement | Regime | Law/centering | Math | Audit | Source | Proof location |
|---|---|---|---|---|---|---|---|
| THM-001 | Exact all-order smooth drift and full bracket contraction hierarchy | every finite k,N; fixed smooth g | arbitrary initial law, mean-field centered | EXACT_IDENTITY | HOSTILE_REVIEW_PASS; blind general-proof reconstruction not yet done | self-contained proof, no external theorem imported | THEOREMS/THM-001_SMOOTH_RECURSION.md |
| THM-002 | Smooth-kernel subcritical and critical fluctuation theorem | \(\lambda_N\to0\) or \(\lambda\) | separate rows required | OPEN | UNAUDITED | UNCHECKED | — |
| THM-003 | Singular full microscopically subcritical theorem | \(\lambda_N\to0\) | separate iid/Gibbs and centerings | OPEN | UNAUDITED | UNCHECKED | — |
| THM-004 | Singular microscopically critical theorem | \(\lambda_N\to\lambda\in(0,\infty)\) | to determine | OPEN | UNAUDITED | UNCHECKED | — |
| THM-005 | Sharpness/obstruction beyond target range | supercritical and bad centerings | multiple | OPEN | UNAUDITED | UNCHECKED | — |
| THM-006 | One-dimensional ordered positive-temperature theorem | subcritical/critical | separate law rows | OPEN | UNAUDITED | UNCHECKED | — |
| THM-007 | Extensions | after flagship | to determine | OPEN | UNAUDITED | UNCHECKED | — |

Every theorem must eventually have a separate card under `THEOREMS/` or `CANDIDATES/` with exact quantifiers and logical negation.

## Round 001 additions and audit scope

| ID | Statement | Math | Audit | Source/proof |
|---|---|---|---|---|
| THM-008 | Exact smooth one-body and pair drift, trace cancellation, martingale and cross brackets | EXACT_IDENTITY | ISOLATED_RECONSTRUCTION_PASS (AUD-001) and HOSTILE_REVIEW_PASS (AUD-002) | frozen card, algebra and BBGKY memoranda |
| THM-009 | Explicit backward pair C^m estimate, uniform N>=2 and nu>=0 given displayed fixed-smooth norms | PROVED_CANDIDATE | ISOLATED_RECONSTRUCTION_PASS and HOSTILE_REVIEW_PASS (AUD-003, same fresh reviewer in two documented phases) | card and smooth memorandum |

AUD-002 is AUDITS/HOSTILE/ROUND_001_HOSTILE.md, hash d0a03745045f4a7e647c6a175dd803fbbbe2c990943ff29a49f090da3d20325d. It also accepts the two explicit counterexamples in the falsification memorandum. It is a fresh context with exact hashed inputs. THM-001's hostile proof review does not imply a separate blind reconstruction of the general recursion. M0 and M1 now pass for the frozen smooth starting model. M2 remains OPEN because critical power counting is not proved; THM-002 through THM-007 remain OPEN, not conditional theorems merely from this algebra.

Frozen submitted cards and issued worker/audit reports retain their original status-at-submission wording and hashes. This ledger and the dated round report record subsequent promotion; no audit input was rewritten to reflect its own verdict.

AUD-003 consists of ROUND_001_ANALYTIC_RECONSTRUCTION.md, ROUND_001_ANALYTIC_REVIEW.md and its identifier addendum. One fresh reviewer saved a statement-only reconstruction before reading the constructor proof, then performed hostile review. The candidate constants were visible; these are not two separately staffed audits. Both phases PASS; the cutoff diagnostic also passes in the explicit Fourier-sequence scope. Candidate card/report bytes remain frozen. The canonical analytic identifier is THM-009. No author acceptance, publication permission, or singular theorem promotion is implied.
