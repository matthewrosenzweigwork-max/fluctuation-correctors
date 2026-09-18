# TASK-073 verification and bounded handoff

Status: conditional construction completed; constructor checks passed. No independent audit is claimed. Every frozen THM-035 line has a disposition in the memorandum, and the actual cubic remains unresolved.

## Mathematical and source checks

- Rechecked all six inequalities separating the chosen maximum from the chosen minimum, the product-weight integrability threshold, the strict decay exponent, and both parts of the critical inclusion argument.
- Reconstructed the repeated-label force term, both response slots, all cubic Haar contractions, and the exact centered lower/scalar pair. No true diagonal value is used.
- Gave a uniform pointwise bound for each Haar slice of the genuine force-gradient product, with every additional constant specified in terms of fixed kernel norms and the admitted uniform R12 constant.
- Used a pathwise empirical-measure estimate, so taking expectation under the actual interacting law costs no uncontrolled density factor and does not assume evolved independence.
- Checked zero noise, zero horizon, a constant terminal test, the finite-N background cubic, and the distinction between absolute time integral and absolute signed time integral.
- Kept the full-inverse/domain and smaller-gradient premises conditional in their issued scopes. No external reference was imported or left unverified as a new dependency.

## Executed diagnostic

Original runtime: Python 3.9.6, standard library only.

```text
python3 MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/exact_diagnostic.py > MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/RESULTS.json
```

Outcome: exit 0, PASS, 57,186 exact assertions. The saved JSON records 158 algebra assertions, 45,004 exponent assertions, 11,948 critical assertions, 9 excluded-boundary checks, 5 mutation-sensitivity checks, 7 noise-convention checks, 52 provenance checks, 2 regime-separation checks and 1 time-norm check. There are 11,251 admitted mesh parameter rows and 5,974 critical mesh rows; repeated rational values from different denominators are not represented as distinct real exponents.

Every intended algebra mutation is detected: dropped N=2 cubic in 5 cases, falling-factorial pair denominator in 20 cases, halved lower coefficient in 12 cases, missing response slot in 20 cases and omitted scalar in 12 cases. These exact smooth-probe results support the analytic proof; they do not prove a singular inverse theorem.

The packet reproduction command is:

```text
python3 MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/exact_diagnostic.py --verify-results MEMORANDA/ROUND_014_LOWER_DRIFT_ARTIFACTS_20260918_041659_UTC/RESULTS.json
```

The final seal procedure re-runs this command from a newly extracted copy of the archive and requires its result to match the sealed JSON exactly. It also requires the extraction to contain exactly the declared regular files, safe relative names, no symbolic links and no extra inherited file. Completion of that procedure is recorded by the sibling archive hash and the final handoff.

## File checks

The assigned seal contains exactly 25 distinct input paths. All input hashes match at the current root, original worktree overlay and the embedded dossier. The newly created Markdown memorandum passes delimiter, duplicate-label, control-character and trailing-whitespace checks: 40 display pairs, 160 inline pairs and 33 distinct display tags. This is a source-format check, not a rendered-PDF check.

The output seal records every new memo/packet file except itself. The archive contains the complete standalone packet and the output seal; its external SHA-256 is recorded separately. All final member hashes are checked against the output seal. The archive is made read-only only after successful extraction and fresh diagnostic verification. No TeX source was created, and no TeX/PDF rendering verification is claimed.

Worktree HEAD remains `1df1805ed7cd8f7c295945f99273c8ffdb598e74`, and its branch is `codex/hocf-r014-lower-drift`. The only worktree source overlay comprises the authorized 25 frozen inputs. New authored files are the memorandum and this uniquely named artifact packet; no copied frozen input was edited.

## Remaining boundary

The earliest external obligations are precisely the admitted R8 complete-domain and R12 smaller-gradient premises. Conditional on them, the entire new frozen implication is proved. The actual integrated cubic is the first remaining analytic target; no bound for its smallness is supplied here. Root must arrange the required independent reconstruction and hostile review before any promotion. This worker stops after sealing the requested bounded packet.
