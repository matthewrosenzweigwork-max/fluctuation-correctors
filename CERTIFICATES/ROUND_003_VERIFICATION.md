# Round 003 verification record

All commands used the existing Python 3.9.6 standard library, TeX Live 2026 and Poppler tools. No dependency, global configuration, remote or historical-commit change. Exact arithmetic has no random seed or floating tolerance. Counts are finite algebra/exponent support, not proofs of continuous singularities or asymptotic laws.

## Reproduced checks

| Executed program | Result | Root evidence under CERTIFICATES/OUTPUTS |
|---|---|---|
| DISCOVERY_CODE/check_round003_iid_pair_exact.py | PASS, 5,500 exact checks | round003_iid_pair_root_rerun.json |
| VERIFICATION_CODE/round003_iid_projection_exact.py | PASS, 3,453 exact checks | round003_iid_projection_root_rerun.json |
| VERIFICATION_CODE/round003_hostile_pair_exact.py | PASS, 18,603 exact checks | round003_hostile_pair_root_rerun.json |
| DISCOVERY_CODE/check_round003_probability_blind_exact.py | PASS, 5,483 exact checks | round003_probability_blind_root_rerun.json |
| VERIFICATION_CODE/round003_sharp_hostile_exact.py | PASS, 31,194 exact checks | round003_sharp_hostile_root_rerun.json |
| DISCOVERY_CODE/check_round003_pair_transport_review_exact.py | PASS, 749 exact checks | round003_pair_transport_review_root_rerun.json |
| VERIFICATION_CODE/round003_sharp_blind_exact.py | PASS, 28 exact checks over 3,568 configurations | round003_sharp_blind_root_rerun.json |
| AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_SHARP_EXACT_CHECK.py | PASS, 19,734 exact checks over 19,600 configurations | round003_fresh_sharp_root_rerun.json |
| VERIFICATION_CODE/round003_fresh_hostile_exact.py | PASS, 1,440 configuration identities, 16 moment cases, 2 pair-count cases and 351 exponent cases | round003_fresh_hostile_root_rerun.json |

| AUDITS/BLIND_RECONSTRUCTION/ROUND_003_FRESH_TRANSPORT_CHECK.py | PASS, 12 iid moment cases and 54 transport substitutions | round003_fresh_transport_root_rerun.json |

Each command was run with `python3` and its output read. Independently authored constructor, reconstruction and hostile programs retain separate original outputs and seals. Root reruns are not relabeled new independent proofs. No unchanged R1/R2 test was repeated merely to increase counts. Exact atomic/cyclic models test nonzero means, first projections, label versus spatial diagonals, pairwise versus mutual event independence and all finite-N factors. Analytic proofs separately justify the Riesz heat representation, bounds, characteristic solutions and limits.

## Mathematical defects and clarifications

- The raw-pair lower-bound report contains a sentence whose non-tightness argument needs a further subsequence tending to infinity. SH-01 and independent FH-C02 explicitly supply it. The theorem statement, hypotheses and constants are unchanged; original report bytes stay frozen.
- The transport card's all-N reading is completed explicitly from the proof's global radial bounds in AUD-014 and independently in fresh FH-C01. No new assumption is needed, and both finite-N constants are recorded.
- Fresh FH-D01 disproves the unrestricted fixed-parameter subcritical sentence in the root diffusion-rescaling note. The exact chain rule and critical scalar classification pass. The original note is retained and AUDITS/ROUND_003_DIFFUSION_RESCALING_ERRATUM.md gives the corrected subcritical trichotomy. No promoted theorem was retracted; RET-002 records the candidate scope error.
- The transport profile's omitted anisotropic Laplacian fails local L2 in dimensions 2–4 and absolute L1 in dimension two. This is a mathematical limitation of a proposed separate-norm perturbation, not a failed test of the declared zero-diffusion theorem or a nonexistence theorem for the full corrector.

## TeX and visual review

Executed `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=BUILD/tex MEMORANDA/hocf_round003_20260917T201600Z.tex`. Final PDF: seven pages, 220,474 bytes, copied to MEMORANDA. Full final transcript: CERTIFICATES/OUTPUTS/round003_tex_build.txt. The complete log was checked: no errors, undefined citations/references, duplicate labels, failed inclusions/bibliography, overfull/underfull boxes or font warnings. Two initial long paragraphs caused small overfull warnings and were repaired before the final build. No mathematical formula was altered to fix layout.

All seven pages were rendered with `pdftoppm -r 90 -png` and visually inspected. After final mathematical additions and the subsequence clarification, affected pages 4–7 were rendered and checked again; the subsequent provenance wording affected page 1, which was separately rerendered and inspected. No clipping, broken displays, missing symbols or problematic page breaks were found. Compilation and visual QA do not certify mathematics. The full Markdown proofs, rather than this concise seven-page synthesis, supply all constants and audit provenance.

## Integrity, staging and publication

The provenance guard checks all 51 immutable baseline entries and permits refreshing only documented mutable ledger/approach/queue entries. The shipped verifier and source PDF remain unchanged. Every issued dossier, output and candidate seal is checked against its original bytes. Historical R1/R2 mutable-state manifests are checked at their own commits, not rewritten to match later state.

The final integrity output, complete changed-path inventory, explicit staged-diff inspection and any preserved-evidence whitespace warning are recorded in REPORTS/CHECKPOINTS/ROUND_003_VALIDATION.md. The checkpoint SHA-256 manifest excludes itself. Publication uses an ordinary fast-forward push to the existing origin/main, followed by independent local/tracking/live-remote hash reads. No push claim is inferred merely from a local commit. Exact publication receipts are retained without embedding a commit's hash into its own tree.

Three concurrent workers is the actual initialized capacity; the project setting requests ten. After workers completed, fresh contexts were successfully allocated in sequence. Fresh and reused review histories are separately identified, with no claim of ten simultaneous workers. Round 004 construction/reconstruction run in separate worktrees and do not modify the canonical R3 checkpoint.
