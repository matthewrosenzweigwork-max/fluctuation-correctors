# Verification record

All checks listed here are constructor self-checks. None is independent
certification of the analytic result.

Executed from the assigned worktree:

```text
shasum -a 256 -c AUDITS/ROUND_024_THRESHOLD_CONSTRUCTION_INPUT_SHA256SUMS.txt
python3 MEMORANDA/ROUND_024_THRESHOLD_CONSTRUCTION_ARTIFACTS/exact_diagnostic.py
python3 MEMORANDA/ROUND_024_THRESHOLD_CONSTRUCTION_ARTIFACTS/exact_diagnostic.py --check
git diff --check
```

The original manifest passed all twenty inputs. The diagnostic passed
1,446 assertions in 25 named categories; fifteen mathematical mutation
categories all had nonzero witnesses. There were no mathematical checker
failures. The second diagnostic execution checks the stored result
byte-derived data against fresh deterministic execution without rewriting
issued files. The exact counts and decimal ODE errors are in RESULTS.json.

The diagnostic checks rational algebra exactly. Its smooth limiting ODE
has 50-digit Decimal arithmetic with 128 and 256 RK4 steps; the largest
observed absolute error is less than 7.3e-11, below the declared 2e-10
tolerance. No actual singular-particle simulation is claimed.

The output/source copies are checked again during packet construction.
The final archive is checked with `verify_packet.py --archive ... --seal
... --source-root ... --self-test --rerun-diagnostic`. The exact archive
and seal filenames, byte digests, final verifier outcome and its six
in-memory mutation results are recorded in the sibling issuance seal.
The verifier is read-only, never extracts files, and rejects absolute
paths, traversal, links, unexpected/missing members, duplicate members,
bad manifests, stale diagnostic results and any byte mismatch.

New text files are scanned for terminal newlines, trailing whitespace,
control characters, and balanced display-math fences. The external report
and packet REPORT.md are byte-identical. Git metadata is checked only
for the fixed HEAD and final status; no history or other worktree is read.

No TeX source was modified or created and no final-response mathematical
LaTeX is emitted by this lane. The complete mathematical response is the
Markdown memorandum, with source proofs and diagnostic in this packet.
No LaTeX build or PDF render is claimed.

After successful checks, all issued files and input copies are read-only.
The final state remains an exact reduction with the explicit open line
(7.5), not completion of THM-046 or the wider campaign.
