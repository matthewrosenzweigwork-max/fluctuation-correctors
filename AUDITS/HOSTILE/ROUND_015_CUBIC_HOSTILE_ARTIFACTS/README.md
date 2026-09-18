# AUD050 sealed hostile-review packet

Prepared 20260918_050834_UTC. Review `AUDITS/HOSTILE/ROUND_015_CUBIC_SOURCE_REVIEW.md` first. The verdict is **CONDITIONAL PASS of the complete THM-036 / THM-037 conjunction**, with all older complete modules retained as conditional premises. Root alone compares this packet with the isolated reconstruction and assigns canonical status.

The isolated worktree is `/Users/matthewrosenzweig/.codex/worktrees/hocf-r015-cubic-hostile` on `codex/hocf-r015-cubic-hostile`, from exact base `072cab684b9ce41855ead6c48f435c8fc184ec35`. All 30 permitted input hashes matched before and after copying; they were checked again when placed under `PERMITTED_INPUTS/`. No non-allowlisted proof, current audit/state/history, prior checker, memory file or root scratch was inspected. Details are in `EXPOSURE.md`.

## Contents

- The sibling review is the complete claim-by-claim verdict and independently recomputed analytic argument.
- `SOURCE_PREFLIGHT.md` describes the scope and exact use of every supplied file.
- `PERMITTED_INPUTS/` contains the 30 exact permitted source files. `INPUT_SHA256SUMS.txt` preserves the original path/hash manifest.
- `diagnostic.py` is a newly written exact rational diagnostic, and `results.json` records all 1,422 passing checks, nonvacuous mutation failures and the exact parameter grid.
- `WORKTREE_METADATA.json` records the verified branch/base and input count.
- `OUTPUT_SHA256SUMS.txt` covers every payload file other than itself. Its own digest is in the external seal.
- The timestamped archive contains exactly the output-manifest members plus that manifest. `ARCHIVE_SEAL.json` and the archive's SHA-256 sidecar are stored outside the archive to avoid a circular digest. The seal records exact membership and byte verification.

## Reproduction

From the isolated worktree, run:

```sh
python3 AUDITS/HOSTILE/ROUND_015_CUBIC_HOSTILE_ARTIFACTS/diagnostic.py
```

The program uses only the standard library. It writes only its `results.json`; the deterministic mathematical data should be unchanged on rerun, while Python runtime metadata can vary on another interpreter. Reproduce in a copy after issuance to preserve the sealed packet.

To verify the supplied input hashes, change directory to this artifact's `PERMITTED_INPUTS` and run:

```sh
shasum -a 256 -c ../INPUT_SHA256SUMS.txt
```

To verify payload hashes in an extracted packet, run from the extracted workspace-relative root:

```sh
shasum -a 256 -c AUDITS/HOSTILE/ROUND_015_CUBIC_HOSTILE_ARTIFACTS/OUTPUT_SHA256SUMS.txt
```

Run `python3 AUDITS/HOSTILE/ROUND_015_CUBIC_HOSTILE_ARTIFACTS/verify_packet.py` from the worktree or extracted packet for the same read-only input/output/archive verification. The issuing process also reopens the gzip tar archive, checks exact sorted membership, rejects nonregular members, and compares every member byte-for-byte with the intended payload. All checks passed as recorded in the seal. There is no TeX source or PDF in this bounded Markdown audit handoff, and no compilation is claimed.

No commit, push, install, external search, child agent, canonical edit or integration was performed. The report and packet are immutable after issuance; any later correction must be a separately issued superseding report.
