# Pre-seal diagnostic history

These records were created before issuance; nothing was corrected after
the packet was sealed.

## Initial run

Command, from the isolated worktree:

python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_023_STATIC_THRESHOLD_BLIND_ARTIFACTS/diagnostic.py --output AUDITS/BLIND_RECONSTRUCTION/ROUND_023_STATIC_THRESHOLD_BLIND_ARTIFACTS/results.json

The exact phase passed 230 rational assertions and eight detecting
mutations. The numerical phase ended with AssertionError at the test
requiring the last-grid source error to be less than 0.002.
The largest grid was m=96; its source error was 0.0032404514380137694.
No results.json was created because the program stopped before export.
The original script is retained as diagnostic.py.

## Inspection only

The initial script was run once with Python -O to inspect all numerical
rows after that failure. Its output is retained verbatim as
preseal_probe_inspection.json. Because -O disables the numerical assert
statements in the original script, that file's embedded
PASS_SUPPORTING_ONLY label is NOT accepted as a validation result.
The exact checks in that script use explicit raises and were not
disabled, but this inspection output is still not the final result.

## Final diagnostic

A new artifact, diagnostic_v2.py, keeps the same exact checks and the
same 0.002 numerical tolerance, extends the list through m=192, and
replaces numerical asserts with explicit conditional raises.
The final normal-interpreter command is:

python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_023_STATIC_THRESHOLD_BLIND_ARTIFACTS/diagnostic_v2.py --output AUDITS/BLIND_RECONSTRUCTION/ROUND_023_STATIC_THRESHOLD_BLIND_ARTIFACTS/results_v2.json

It exited zero. The final result is results_v2.json:

- 230 exact rational assertions passed.
- All eight deliberately wrong coefficient choices were detected.
- The final numerical source error was 0.0008106712642812486.
- The retained 0.002 tolerance passed without relaxation.
- Negative energy and omitted-background diagnostic checks passed.

No mathematical conclusion depends on either the tolerance or the
finite numerical probes. No failed run is concealed or promoted.
