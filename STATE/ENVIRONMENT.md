# Environment — Round 001

- Date/time UTC: 2026-09-17T17:55:33.984418+00:00
- Operating system: macOS-26.6.2-arm64-arm-64bit
- Repository root: `/Users/matthewrosenzweig/Library/CloudStorage/GoogleDrive-mrosenz2@andrew.cmu.edu/My Drive/Git/fluctuation-correctors`
- Git branch/worktree: main (integration); nine isolated proof/source/audit worktrees under /private/tmp/hocf-round001-*-20260917.
- Frozen baseline: `475a5399828bc6e2ccbade08c59b8778638df14a`. Exactly one root commit; no push or history rewrite.
- Codex interface: desktop; CLI version 0.155.0, satisfying package minimum 0.153.0.
- Root: gpt-6-astra, effort ultra, verified from this task's local session turn_context.
- Ordinary workers: gpt-6-astra, effort max, explicitly selected in accepted collaboration.spawn_agent calls.
- Subagents enabled: yes; platform capacity four including root, hence three concurrent workers and sequenced batches for seven requested scientific lanes, independent installation review, hostile algebra/obstruction review, and independent analytic review (ten Max contexts in total). No global/project settings changed.
- Python for package/verifier: 3.9.6.
- Artifact Python: bundled runtime at `/Users/matthewrosenzweig/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`. pypdf, pdfplumber, Pillow and reportlab available; fitz and sympy unavailable in bundled runtime. No dependencies installed.
- TeX: TeX Live 2026, pdfTeX 1.40.29 and latexmk 4.88; final six-page TeX/PDF compilation and visual review passed.
- PDF rendering: pdftoppm available. Initial fitz extraction attempt failed with ModuleNotFoundError; pypdf extraction and pdftoppm rendering succeeded for seven pages.
- Package verification: PASS, 80 files. Installed verification: PASS before baseline and launch.
- Archive SHA-256: `a802d22334cb459b868fb4bdca0f516ac3764cc0e012b65889b96ad1b0f077f8`.
- Source PDF SHA-256: `a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76`.
- Root model evidence is local metadata, not inference from public model docs. Worker settings are tool-accepted selections.
