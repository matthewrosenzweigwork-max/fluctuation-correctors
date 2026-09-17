# Round 004 verification record

Environment: existing Python3.9.6 standard library, TeX Live2026, Poppler. No dependency/global-configuration installation or remote/history alteration. Every finite check below is supporting algebra with its stated scope, not a proof of SDE existence, measure extension, convergence of operators or asymptotic probability. Root reruns do not create a new independent context.

## Executed checks

- python3 VERIFICATION_CODE/round004_diffusive_reconstruction_exact.py: PASS,3252 exact Fraction checks;432 radial,1296 angular,864 Lyapunov,648 radial-scale,12 exponent. Root output CERTIFICATES/OUTPUTS/round004_diffusive_reconstruction_root_rerun.json.
- python3 AUDITS/HOSTILE/ROUND_004_DIFFUSIVE_EXACT_CHECK.py: PASS,2520 radial tuples,7560 Lyapunov tuples,24 iid cases/2160 configurations,70 scaling tuples. Root output round004_diffusive_hostile_root_rerun.txt. Exact Fraction arithmetic includes high finite nu and all three norm regimes.
- python3 DISCOVERY_CODE/check_round004_singular_response_exact.py: PASS,133 exact checks for inhomogeneous response terms, constants, Fourier signs, missing atom/gradient/factor obstructions and smooth pair energy. Root output round004_singular_response_root_rerun.json. Constructor provenance remains SELF_CHECKED until the separate review.
- python3 DISCOVERY_CODE/round004_range_taylor_check.py: PASS,18 root exact binomial derivative checks. Output round004_range_taylor_root_check.json. Detects the V1 missing factor s at s>1 and validates V2's corrected third derivative. This is root self-checking, not an independent stochastic-obstruction proof.

All use standard-library integers/Fraction, no seed, stochastic simulation or numerical tolerance. Independent reconstruction/hostile proofs are separate immutable reports. The all-N reconstruction addendum is a complete analytic three-case proof with explicit constants, not a numerical extrapolation. Later sealed independent checks are appended separately.

## Local mathematical proof checks

Root read the entire local constructor, fresh reconstruction, all-N extension and fresh hostile report. AUD020 compares the exact Borel martingale class and source/domain/endpoint claims; AUD021 passes all16 mathematical claims. Conditional classical identification does not assert classical existence. The reconstruction's extra annular-trace/time-modulus facts retain their own scope rather than inheriting the narrower hostile review.

TASK035-E01 is a rendering-only missing control-sequence backslash in a conditional-expectation display. The original proof and hashes are preserved, with a separate rendering erratum; the compiled synthesis typesets the intended conditional expectation. The root range-obstruction V1 Taylor constant error was self-detected before audit/promotion, explicitly corrected in separately sealed V2, and retained for provenance. Neither integrity checks nor an unchanged theorem statement erase this history.

## TeX and visual check

Executed latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=BUILD/tex MEMORANDA/hocf_round004_20260917T215500Z.tex. Final local-diffusion PDF has4 pages,190257 bytes. Final transcript is CERTIFICATES/OUTPUTS/round004_tex_build.txt. Complete log was checked for errors, warnings, undefined references/citations, duplicate labels, inclusion/bibliography failures, overfull/underfull boxes and font warnings: none. An initial2.13pt paragraph overfull was repaired with a local prose edit before the final build, without changing mathematics.

All four pages were rendered with pdftoppm -r90 -png and visually inspected. No clipping, missing symbols, broken display, overlap or problematic page break found. PDF copied to MEMORANDA beside its source; earlier R1-R3 artifacts remain untouched. This four-page synthesis covers the shared local diffusion theorem only; complete new response and range-obstruction arguments reside in their named Markdown reports. No uncompiled mathematical claims are inferred from a successful typesetting run.

## Integrity, staging and publication

Final protected-source/mutable-ledger verification, recursively checked issued input/output manifests, complete explicit path inventory, staged-byte comparison, whitespace disposition and publication equality will be recorded in REPORTS/CHECKPOINTS/ROUND_004_VALIDATION.md. All51 immutable original entries remain protected by the existing provenance guard. Only documented mutable ledger/approach/queue hashes may be refreshed; historical round manifests are checked at their own commits. The verbatim TeX build transcript's final blank line is intentionally retained if reported by staged whitespace checks. No issued report is normalized to silence evidence-format warnings.

The owner's publication authorization persists. After the atomic gate commit, an ordinary push to unchanged origin/main is checked against independent local/tracking/live remote hashes. A literal post-push receipt is kept under .git/campaign-records and in the next tracked checkpoint, avoiding a circular commit hash. Ten workers are configured, three concurrent runtime workers actually available; fresh tasks use newly freed slots and preserve their exact isolation histories.

## Subsequent fresh checks

Fresh response hostile checker: python3 AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_EXACT_CHECK.py,346 exact checks PASS, root transcript round004_response_hostile_root_rerun.txt. Fresh statement-only response checker: python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RESPONSE_RECONSTRUCTION_CHECK.py, PASS exact36-mode comparisons plus constants/resonance/pair/heat/divergence checks; root JSON round004_response_blind_root_rerun.json. Root read the complete470-line reconstruction and compared every submitted scope in AUD024; fresh AUD023 independently reviews17 claims. Each response proof uses its own exact normalization and density/multiplier checks.

Fresh range hostile checker: python3 AUDITS/HOSTILE/ROUND_004_RANGE_OBSTRUCTION_EXACT_CHECK.py, PASS234 derivative comparisons,2880 time inequalities and63 exact rational transport remainders;36 exhibit the original V1 underbound. Root output round004_range_hostile_root_rerun.json. Full review read and copied/hash-checked as AUD022; wording and source-exposure limits preserved separately. Fresh blind range verdict remains pending at this entry.

Intermediate protected-source and installed-campaign checks pass:51 immutable entries,23 documented mutable paths; source note checksum unchanged. Thirty issued R4/R5 manifests checked with165 sealed file checks before later interface dossiers. Final counts will be in the checkpoint validation after all issued reports are integrated. No historical manifest was rewritten.

Final range reconstruction: full TASK042 report read and compared in AUD025; independent killed-Dynkin and backward-Ito routes both establish the exact assertion. Root rerun of AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RANGE_EXACT_CHECKS.py passes81 admitted rows,five excluded controls and one explicit finite-annular constant case. No original proof/audit bytes changed. R5 submitted proofs, dossiers and the read hostile report are next-gate evidence, not R4 certification of the full prescribed-data inverse.
