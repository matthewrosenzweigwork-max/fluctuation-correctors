# Round 002 verification record

All calculations use pre-existing tools. Python 3.9.6 standard library, exact integer/Fraction or Gaussian-rational arithmetic, no random seed or tolerance. Computation status REPRODUCED; finite tests do not prove infinite quantifiers or singular limits.

| Executed command | Result | Retained evidence |
|---|---|---|
| `python3 DISCOVERY_CODE/check_round002_coupling_exact.py` | PASS, 1,292 exact equalities | DISCOVERY_CODE/round002_coupling_exact_output.json |
| `python3 VERIFICATION_CODE/round002_falsification_exact.py` | PASS, 116 exact rational checks | Code and sealed report; rerun observed by root |
| `python3 VERIFICATION_CODE/round002_blind_selfcheck.py` | PASS, 20 drifts, 64 brackets, 20 constants, 204 matching counts, 21,845 cancellations | CERTIFICATES/OUTPUTS/round002_blind_root_rerun.json |
| `python3 VERIFICATION_CODE/round002_partition_check.py` | PASS, 84 rational cases plus partition weights/exponents | CERTIFICATES/OUTPUTS/round002_partition_check.txt |
| `python3 VERIFICATION_CODE/round002_hostile_residual_exact.py` | PASS, 208 exact rational Laurent-polynomial checks | CERTIFICATES/OUTPUTS/round002_hostile_root_rerun.json |
| `python3 DISCOVERY_CODE/check_round002_powercount_exact.py` | PASS, 444 exact equalities | CERTIFICATES/OUTPUTS/round002_powercount_root_rerun.json |
| `python3 DISCOVERY_CODE/check_round002_gaussian_blind_exact.py` | PASS, 2,147 exact coefficient/model checks | CERTIFICATES/OUTPUTS/round002_gaussian_blind_root_rerun.json |
| `python3 VERIFICATION_CODE/round002_powercount_hostile_exact.py` | PASS, 1,110 independent exact rational checks, including failed unrestricted identity and repaired identity | CERTIFICATES/OUTPUTS/round002_powercount_hostile_root_rerun.txt |

Constructor reruns are not relabeled independent verification. Independently authored checkers and their scope appear in the corresponding immutable reports. No unchanged Round 001 test was repeated solely to increase the test count.

The exact smooth limiting arguments also check free heat, zero/equal/unequal terminal times, constant and duplicate tests, degenerate covariance, both signs of a single Fourier interaction, its removable resonance, oscillating temperature and a high-frequency two-derivative-loss diagnostic. These are displayed analytic calculations, not numerical experiments. The attractive-Gibbs example is separately reviewed and does not concern positive-Riesz preparation.

## TeX and PDF

Executed `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=BUILD/tex MEMORANDA/hocf_round002_20260917T192500Z.tex`. Final result PASS, seven pages, 238,345 bytes. Full transcript is CERTIFICATES/OUTPUTS/round002_tex_build.txt. The log has no errors, undefined references/citations, duplicate labels, missing inclusions, bibliography failures, overfull/underfull boxes or font warnings. Initial long-path/inline-formula overfull warnings were corrected before final build. The later symmetry qualification compiled without warnings.

Executed `pdftoppm -r 90 -png BUILD/tex/hocf_round002_20260917T192500Z.pdf BUILD/round002_pages/page`. All seven pages were visually inspected; after the symmetry qualification, affected pages 5–7 were rendered and inspected again. No clipping, bad glyphs, missing equations or problematic page breaks found. Final PDF copied to MEMORANDA after that review. Compilation is not proof certification.

## Integrity and preserved defects

The provenance guard checks all 51 protected baseline entries against the original installation commit and permits refreshing only the previously documented mutable ledger paths. The unchanged installed verifier checks the current manifest. Exact audit dossiers, outputs, repairs and independently sealed reconstructions have separate SHA-256 manifests. R1 manifests remain historical and must be checked at their corresponding tree/archive, not rewritten to match later state.

The original independent residual report has one literal form-feed byte at its equation (2.5). The report remains byte-identical to its issued seal; a separate rendering erratum supplies the correct formulas. The original THM-012 symmetry omission is recorded as a mathematical defect, with a new THM-014 and separate repair review; it is not hidden by editing the original. Verbatim build transcripts may end with a blank line. Their whitespace warnings are documented and their bytes retained.

Final integrity, changed-path inventory, staged-diff review and publication commands are recorded in the R2 checkpoint validation file and post-push Git record. No dependency installation, remote alteration, history rewrite, user-change absorption or push without authorization occurred.
