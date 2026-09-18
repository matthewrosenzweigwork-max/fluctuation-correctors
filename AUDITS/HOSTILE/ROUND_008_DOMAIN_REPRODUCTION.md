# Reproduce the sealed TASK054 hostile review

Worktree: `/tmp/hocf-r008-domain-hostile-20260918`.
Branch: `codex/hocf-r008-domain-hostile`.
Base/HEAD: `3aa91391516f35afe5317a287b4f0e2e93e6384c`.

The review verdict is PASS for the bounded THM028 domain and exact finite-N identity. Read `ROUND_008_DOMAIN_REVIEW.md` for the independent analytic reasoning, per-claim dispositions, exposure history, one nonblocking rendering finding, and explicit exclusions. The candidate was not repaired.

The independent exact checker passed 1,821 assertions on Python 3.9.6, standard library only. From this worktree's root, reproduce without changing an issued output:

```sh
python3 AUDITS/HOSTILE/round008_domain_hostile_checks.py --stdout > /tmp/round008_domain_hostile_reproduced.json
cmp AUDITS/HOSTILE/ROUND_008_DOMAIN_CHECK_RESULTS.json /tmp/round008_domain_hostile_reproduced.json
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_DOMAIN_OUTPUT_SHA256SUMS.txt
shasum -a 256 -c AUDITS/HOSTILE/ROUND_008_DOMAIN_SEAL_SHA256SUMS.txt
```

The checker verifies only its eighteen assigned mathematical inputs and runs its own diagnostics. It does not read a constructor checker, R7 proof, other audit, or canonical state. It uses exact rational coefficient equality and automatic differentiation, without quadrature, tolerance, randomness, external packages, or network access. Its Fourier models and local radial calculations test identities and necessary scalings; the singular analytic passage is reviewed in the written report.

Packet members:

- `ROUND_008_DOMAIN_REVIEW.md`: issued mathematical review and complete scope/exposure record.
- `round008_domain_hostile_checks.py`: independently written checker.
- `ROUND_008_DOMAIN_CHECK_RESULTS.json`: deterministic exact results, sensitivity counts, checker hash, and input hashes.
- `ROUND_008_DOMAIN_REPRODUCTION.md`: this handoff.
- `ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt`: the eighteen verified inputs.
- `ROUND_008_DOMAIN_OUTPUT_SHA256SUMS.txt`: the five preceding output files, excluding itself.
- `ROUND_008_DOMAIN_HOSTILE_PACKET.zip`: exactly the eighteen inputs and six named output files above, using worktree-relative member names.
- `ROUND_008_DOMAIN_SEAL_SHA256SUMS.txt`: SHA-256 seals for the output manifest and archive.

The archive has 24 files. Its CRC, exact member set, and member digests were checked against the two manifests. Every issued output was made read-only after sealing. Read-only file modes are an extra accidental-edit precaution; the SHA-256 seals define the issued byte strings.

No root file or canonical ledger was edited. No commit, push, dependency installation, or child worker was used. Root alone integrates this report and compares it with the still-unseen independent reconstruction. Do not edit the issued review; create a superseding report if a correction becomes necessary.
