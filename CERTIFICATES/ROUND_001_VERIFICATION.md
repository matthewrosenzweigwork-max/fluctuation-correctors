# Round 001 reproduction record

All verification uses pre-existing dependencies. No installation or upgrade was performed. Root calculations are independently written unless identified as constructor reruns. Finite batteries support the mathematical proofs; they are not universal proof certificates.

## Commands and observed outcomes

- `python3 VERIFICATION_CODE/round001_fourier_pair_check.py`: PASS 90 exact rational Fourier pair cases (raw and expanded identities), N=2,3,4; nu=0,1/3,2. Coefficient residuals exactly zero. Output retained in CERTIFICATES/OUTPUTS/round001_fourier_pair_check.json.
- `python3 VERIFICATION_CODE/round001_bbgky_exact_fourier.py`: PASS 24 exact rational drift cases with homogeneous and inhomogeneous reference, plus martingale-gradient and cross-bracket checks. Independent BBGKY context.
- `python3 DISCOVERY_CODE/round001_pair_selfcheck.py`: PASS 16 one-body and 80 pair numerical cases; maximum residuals 4.263e-14 and 2.274e-13, tolerance 2e-10. EXPLORATORY.
- `python3 VERIFICATION_CODE/round001_allorder_fourier_check.py`: PASS 144 rational cases k=1..4, N=2..4, nu=0,1/3,2, including k>N. Output retained in CERTIFICATES/OUTPUTS/round001_allorder_fourier_check.json.
- `python3 DISCOVERY_CODE/round001_recursion_check.py`: PASS all exact Q(i) drift, time-derivative, rooted-gradient and shared-label bracket checks; 37,886 integer subset cancellations through k=9. Constructor output retained alongside code; root rerun ended ALL ROUND 001 RECURSION SELF-CHECKS PASSED.
- `python3 VERIFICATION_CODE/check_round001_smooth_fourier.py`: PASS 120 exact rational identities, N=2,3,17; nu=0,1/3,1,7. Heat mode, full sum mode, manufactured internal-transport solution. Same-context analytic self-check, root reproduced.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=BUILD/tex MEMORANDA/hocf_round001_20260917T180200Z.tex`: PASS, 6 pages. Full log inspected: no errors, undefined references/citations, duplicate labels, bibliography/inclusion failures, overfull or underfull boxes, or font warnings. All six rendered pages inspected visually. Final PDF copied to MEMORANDA only after review. Build transcript preserved in CERTIFICATES/OUTPUTS/round001_tex_build.txt.
- `pdftoppm -r 95 -png BUILD/tex/hocf_round001_20260917T180200Z.pdf BUILD/tex/round001-final`: PASS, six reviewed page images.

## Earlier failures and their disposition

An initial PDF extraction attempt lacked fitz; extraction and inspection succeeded using the existing bundled pypdf and Poppler tools. No dependency was added. An early TeX build had an overfull box; a subsequent edit briefly caused a Missing $ error. Both were corrected before the final clean build; the delivered six-page PDF has neither issue. The installation staged diff retained ten intentional Markdown hard-break warnings inherited byte-for-byte from the verified package. No working research diff whitespace error remains.

The installation report and immutable audit reports contain separate integrity/audit outcomes. Final state/provenance commands and their exact output are recorded in the checkpoint validation file. A compilation or checksum pass does not constitute mathematical certification.

## Final artifact-format scan qualification

The broad final text-hygiene scan initially flagged four intentional Markdown hard breaks at lines 3–6 of the already hashed BBGKY report and missing terminal newlines in three verbatim PDF text extractions under SOURCES/EVIDENCE/ROUND_001_ORDERED. Those evidence bytes were preserved. The scoped final check accepts exactly these known formats, rejects accidental control characters and any other new trailing whitespace/missing newline, and keeps every audit input hash unchanged. This is a format qualification, not a mathematical or integrity failure.
