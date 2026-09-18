# AUD075 execution history

Working directory for all shell commands: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r027-duality-blind`. No command used another worktree as a working directory. No external process downloaded data, installed a package, contacted a service, or changed Git.

The source/read chronology and all exposed inputs are in SOURCE_EXPOSURE_HISTORY.md. This history records exact inspection/verification invocations and the file-producing scripts used in this lane; large heredoc payloads are preserved as the resulting script/report files instead of duplicating them here.

1. `cat TASKS/ACTIVE/TASK-117_ROUND027_DUALITY_BLIND.md && cat AUDITS/ROUND_027_DUALITY_BLIND_INPUT_SHA256SUMS.txt` — task and source envelope read first.
2. `shasum -a 256 -c AUDITS/ROUND_027_DUALITY_BLIND_INPUT_SHA256SUMS.txt && cat AGENTS.md MODEL_ORCHESTRATION.md TASKS/ACTIVE/ROUND_001_MODEL.md THEOREMS/THM-052_KILLED_ATTRACTIVE_COULOMB_DUALITY.md MEMORANDA/ROUND_001_ALGEBRA.md MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md` — eight OK; output truncated by tool, explicitly acknowledged.
3. `cat THEOREMS/THM-052_KILLED_ATTRACTIVE_COULOMB_DUALITY.md` — complete untruncated frozen assertion.
4. `wc -l MEMORANDA/ROUND_001_ALGEBRA.md MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md && git status --short && git rev-parse --show-toplevel HEAD` — line counts 917,541,584; expected three untracked task inputs; root/base verified.
5. `sed -n '1,330p' MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md` — complete relevant R6 source segment.
6. `sed -n '1,270p' MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md` — complete relevant R4 source segment.
7. `sed -n '1,220p' MEMORANDA/ROUND_001_ALGEBRA.md && sed -n '430,570p' MEMORANDA/ROUND_001_ALGEBRA.md` — R1 response and incidental later algebra segment.
8. `date -u +%Y%m%d_%H%M%S_UTC && command -v python3 && git diff --name-only` — artifact timestamp 20260918_094707_UTC; `/usr/bin/python3`; no tracked changes.
9. A Python standard-library routine made the unique packet directory, reread the eight allowed sources as bytes, asserted each frozen SHA-256, wrote exact INPUTS copies, FROZEN_INPUT_SHA256SUMS.txt and INPUT_INVENTORY.json. No source was changed.
10. Wrote diagnostics.py, simplified one dormant expression before execution, then ran `python3 <packet>/diagnostics.py > <packet>/diagnostic_baseline.json`. A subsequent JSON-only read confirmed PASS,322,0. There was no first-run baseline failure.
11. A standard-library subprocess harness ran the nine named `python3 <packet>/diagnostics.py --mutant NAME` invocations. Each returned 1 with the counts in mutation_summary.json; every stdout and stderr was saved. This ran concurrently with local writing of the independent report, not with another worker.
12. Wrote the assigned report and portable verify.py from this audit's independent reconstruction.
13. Ran `python3 -B <packet>/verify.py --guard-mutant NAME` for the nine named in-memory guard mutants. Every one returned 1 and its full result is in verifier_guard_mutations.json. No archive extraction or packet tampering was performed.
14. Wrote source/exposure/history/README/verification-result files and copied the assigned report into the packet. Built internal payload inventory/checksums, complete sibling regular-member inventory/checksums, regular-member-only archive and outer seal. The immutable material was then set read-only (regular files 0444, directories 0555).
15. Final strict verification: `python3 -B <packet>/verify.py --run-diagnostics`. This checks all eight sources, all payload/outer seals, exact report mirror, complete safe archive streams and fresh baseline plus nine semantic mutants without changing files. Its final JSON is the named sibling VERIFICATION.json; the corresponding verification-file SHA-256 is supplied separately. The archive is never extracted.
16. Final permitted-source verification and metadata status confirm every original input still matches and no tracked file was changed. No commit, push, merge, branch switch or remote change was performed.

The verifier does not write files and does not import the packaged diagnostics. Only its explicit --run-diagnostics option executes the known script with Python bytecode writing disabled. Package builders write only the assigned artifact paths. A final strict verification failure, if any, must be recorded before issuance rather than hidden by a stale success record.
