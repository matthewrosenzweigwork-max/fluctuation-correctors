# TASK051 homogeneous particle-domain construction

Status: **PROVED_CANDIDATE / SELF_CHECKED**, from a disclosed root seed. This is not an independent audit. Separate statement-only reconstruction and hostile review remain required.

Main proof: `MEMORANDA/ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`.

The proof covers the entire bounded THM028 assertion: higher-moment barriers and common compact-start completeness; legitimate differentiation of expectations twice; the prescribed weighted first/second derivatives; both compensated responses; a separate weighted evolution and time derivative; the classical off-diagonal pair equation; weak H1/W2,1 and structural internal-drift integrability; all background and partial triple contractions; and the exact N-particle Itô identity with a square-integrable true martingale under a bounded initial density. No unresolved load-bearing line remains in the submitted construction. Its analytic lemmas still require independent scrutiny.

All new constants may depend strongly on N and on the fixed data. N-uniform evolved residual/bracket smallness, centering limits, CLTs, beta-to-zero uniformity and critical hierarchy closure remain open. THM027 supplies no lemma to this construction; no R7 proof, task, seed, audit, state/history or memory was used.

Worktree: `/Users/matthewrosenzweig/.codex/worktrees/hocf-r008-homogeneous-domain-20260918`.
Branch: `codex/hocf-r008-homogeneous-domain`.
Assigned base: `32d17afba1ddb3c4198fb9a45e912907629618ce`.

From the worktree root, verify the issued bytes before reproducing:

```text
shasum -a 256 -c MEMORANDA/ROUND_008_DOMAIN_ARTIFACTS/ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt
shasum -a 256 -c MEMORANDA/ROUND_008_DOMAIN_ARTIFACTS/ROUND_008_DOMAIN_OUTPUT_SHA256SUMS.txt
python3 MEMORANDA/ROUND_008_DOMAIN_ARTIFACTS/round008_domain_exact_checks.py
```

The checker uses only the standard library and exact rational/integer arithmetic. It passes **4,405 assertions**, including eighteen input hashes, N=2,3 deleted-label Fourier identities, cubic contractions, both response slots, lower/scalar terms, exact gradient/bracket, zero noise, constant test, Coulomb multipliers, radial/transverse Jacobian coefficients, barrier absorption and all relevant exponent inequalities. There is no random seed or numerical tolerance. These checks support algebra and reproducibility; they do not independently certify the analytic proof. Rerunning writes the result JSON and may change its recorded Python version, so reproduce in a separate extracted copy after verifying the original seal.

From `MEMORANDA/ROUND_008_DOMAIN_ARTIFACTS/`, verify the archive seal:

```text
shasum -a 256 -c ROUND_008_DOMAIN_SEAL_SHA256SUMS.txt
```

The archive contains exactly the eighteen frozen source files, the complete proof, checker, recorded result, README, input manifest, and output manifest, at their worktree-relative paths. It excludes its own seal manifest. The separate seal hashes the archive and output manifest. No manifest is claimed to hash itself. No unrelated baseline file is packaged.

No root source, canonical ledger, or previous seal was edited. No commit, push, installation, or child agent was used. All mathematical corrections made during the pre-seal self-review are incorporated in the single issued proof; subsequent changes must be separate superseding artifacts.
