# AUD056 sealed bounded hostile handoff

Verdict: PASS AS AN EXPRESSLY CONDITIONAL WHOLE-CLAIM IMPLICATION.
No mathematical repair is requested. This packet does not independently
certify earlier source gates or canonically promote THM040.

The report is ROUND_018_BOUNDED_NOISE_REVIEW.md. Its byte-identical standalone
copy is the assigned review immediately outside the artifact directory.
The source preflight and exposure record state the exact boundaries.
All seventeen allowed input files are reproduced in inputs/.

Reproduce from the prescribed worktree without writing:

    python3 AUDITS/HOSTILE/ROUND_018_BOUNDED_NOISE_HOSTILE_ARTIFACTS/payload/round018_hostile_exact.py --check
    python3 AUDITS/HOSTILE/ROUND_018_BOUNDED_NOISE_HOSTILE_ARTIFACTS/payload/verify_seal.py

The new exact diagnostic passed 1,381 assertions in 35 categories, rejecting
22 deliberate mutations with explicit witnesses. It checks literal
finite-particle first-order/source algebra, full cross carré du champ,
initial variance and cross-time derivatives, original energy subtractions,
normalization and Coulomb measure constants, positive heat splitting,
all entries of multi-time covariance, exact degeneracy and positive
semidefiniteness, and the initial-field-weighted stochastic compensator.
A separate two-coordinate mixture has Gaussian marginals and matching
covariance but is not jointly Gaussian. It catches a shortcut absent
from the candidate.

Arithmetic is exact, deterministic and standard-library only. There is no
random seed, floating-point tolerance, external dependency or simulation.
Laurent first derivatives divide physical derivatives by 2 pi, so the
generator and bracket are divided by (2 pi)^2. Rational modal instances
check covariance algebra, not the analytic singular theorem. The report
contains the analytic review.

INPUT_SHA256SUMS.txt lists exact source bytes. OUTPUT_SHA256SUMS.txt hashes
all payload outputs other than itself and the source copies, which have
their separate manifest. The archive contains every payload file,
including those manifests, with no directories or special/link members.
Its exact-byte member list and digest are in the outer artifact directory:

    ARCHIVE_MEMBERS_SHA256SUMS.txt
    ARCHIVE_SHA256SUMS.txt
    ROUND_018_BOUNDED_NOISE_HOSTILE_PACKET.tar.gz
    SEAL_VERIFICATION.json
    SEAL_SHA256SUMS.txt
    SEALED_HANDOFF.md

The verifier rejects absolute/parent/empty/dot paths, duplicates, links,
nonregular or unexpected members and byte differences, without extracting
the archive. It checks the exact 17-file overlay and standalone report by
default. For an independently copied packet whose payload and outer seals
remain together, append --portable to skip only those external workspace
checks. All internal input/output/archive checks remain active.

The checksum hierarchy avoids self-hashing: the output manifest is hashed
by the archive member manifest and archive bytes; the outer seal hashes
all outer deliverables except itself. The final handoff supplies its digest.
No source byte or issued audit is edited. All final files are read-only;
corrections require a separately issued superseding artifact.
