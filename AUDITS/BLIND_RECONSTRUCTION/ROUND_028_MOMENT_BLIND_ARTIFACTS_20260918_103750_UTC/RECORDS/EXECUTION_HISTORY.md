# Execution and issuance history

Initial administration verified all eighteen manifest bytes, branch and exact base before source work. The only initial untracked files were the supplied input manifest, task card and frozen THM054 card. Source display/query order, including the one truncated aggregate output and full rereads, is recorded in `READ_EXPOSURE.md`.

The packet was created with the UTC timestamp in its directory name. All eighteen inputs were copied only after their SHA-256 values matched the input manifest. `input_verification.json` records their byte lengths and hashes; `environment.json` records the observed Python runtime, base, branch, worktree and creation time.

The independent proof was authored from the frozen statement and the allowed earlier proof passages. The fresh diagnostic was written from scratch using Python's standard library. No earlier diagnostic source or current constructor result was read. No dependency was installed and no network or remote operation was used.

Development execution 001 was launched with:

```text
python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_028_MOMENT_BLIND_ARTIFACTS_20260918_103750_UTC/CODE/run_once.py
```

The runner preserves its executed diagnostic source before invoking it, then saves complete stdout, stderr, result and return-code/timing metadata in a uniquely numbered run directory. It succeeded on its first invocation: 58,645 checks and 19 nonzero deliberate mutations. There were no failed program executions or reruns before sealing. Exact rational/integer checks and floating diagnostics are separately counted in the output JSON and README. No stochastic simulation was performed.

The report draft's inline delimiter escaping was repaired before issuance, with an explicit formatting record. Its ambient startup-context disclosure was made precise. Its 548 lines were checked for balanced display/inline delimiters and unexpected control characters. An exact report copy was placed at `REPORT.md`; the successful result was copied to `OUTPUTS/expected_result.json` for portable replay comparison. All source files were rehashed against both the original worktree and the frozen copies. The base was rechecked without reading history. `preseal_status.txt` and `preseal_verification.json` preserve these observations.

Final issuance constructs `INVENTORY.json` from all regular payload paths, including the inventory and payload-manifest paths themselves. `PAYLOAD_SHA256.json` hashes every other member. The report and every packet file are made mode 0444, and packet directories mode 0555. A tar.gz is built from regular files only, with safe relative paths, no links/directories/devices/duplicates, owner and group ids zero, mode 0444, and fixed archive metadata. External seals authenticate the archive, both internal metadata files and the separately issued report. A fresh read-only verifier run with `--archive` and `--replay` is recorded in the separate `.VERIFICATION.json` receipt after archive creation, avoiding a circular self-authentication claim.

No canonical STATE/ or cumulative memorandum was read or edited. No commit, merge, push, remote operation, child agent or permission request was made. All issued files are read-only; a subsequent correction requires a distinct report and packet.
