# Failed routes and execution events

No unexpected mathematical assertion in the fresh diagnostics failed.
Every attempted diagnostic and mutation run is retained.

Mathematical approaches rejected during review:

1. Applying the fourth graph estimate directly to unclipped Coulomb energy
   is invalid: the kernel is unbounded and the initial second/fourth
   moments diverge. The constructor does not use this route.
2. Replacing the good initial event by a future event inside martingale
   estimates is invalid. A fresh exact two-step martingale gives unequal
   event-weighted square and bracket; the mutation has a nonzero witness.
3. Bounding neighboring Gaussian-weight ratios uniformly is invalid.
   The differentiated segment estimate with comparison at r/8 is valid.
4. Omitting the smooth self term, a zero mode, same-label mixed subtraction,
   a tag time, a row factor, or one exact time weight changes literal
   identities. Recorded finite Fourier mutations detect those changes.
5. Taking absolute values in the unsmoothed third slot only gives the
   nondecaying bound of order Nr+r^-1. It cannot settle the open tail gate.
6. Extending the proposed cutoff interval to delta=1/22 fails to force the
   first displayed bound to zero; that endpoint is correctly excluded.
7. Bounded fourth moments do not establish fourth-power uniform
   integrability or source decay. The constructor makes neither claim.

These are rejected proof strategies or deliberate altered mathematical
claims, not admitted counterexamples to the actual theorem or target.

The baseline diagnostic was run once directly and once by the capture
harness. Both passed. The harness then ran all 21 named mathematical
mutations separately; each produced its expected nonzero witness and
exit code 7. No deliberate mutation was mistaken for a software failure.

One orchestration failure occurred after the mutation capture harness had
already completed successfully. The surrounding JavaScript attempted
store("diagnosticSession", r.session_id) when the completed result had no
session_id. The tool rejected the undefined value with:
Unable to store "diagnosticSession". Only plain serializable objects can be stored.
The successful result was already saved. No source, check, or result was
changed or rerun; the metadata slot was later set to null. A subsequent
line-count command in that same aborted JavaScript invocation did not run.
The failure and recovery are explicit entries in EXECUTION_HISTORY.json.

The initial combined acquisition display exceeded the display budget.
The complete results had been captured and were re-emitted in explicit
untruncated ranges. This was a display limitation, not a failed source read.
No filename miss, external read, unrecorded mathematical trial, or abandoned
code revision occurred in this hostile lane.

Final sealing and verification are recorded in the included issuance
source and the named sibling verification receipt. If that procedure
were to fail, its immutable failure receipt must be preserved and any
correction issued under a distinct name.

