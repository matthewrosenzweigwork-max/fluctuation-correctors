# Round 003 final validation

Input HEAD 2f532ccd2cb5f3d84db456be96e438f03f7e2ad2. The index was empty before staging. All changes are campaign outputs, canonical state, recovery records and sealed next-round dispatch inputs; no unrelated user work, original source change, dependency or global-config change, remote alteration or history rewrite.

python3 scripts/check_campaign_provenance.py --refresh-mutable: PASS, all 51 immutable baseline entries preserved and only the 23 documented mutable baseline entries differ. The shipped verifier is unchanged. python3 scripts/verify_campaign.py: CAMPAIGN VERIFICATION PASSED, imported note SHA-256 a332f829904a80c27f0c13291758c316f1fcdd7460a3b0d6d67c1ff1bf18ff76. Recursive issued-manifest validation: PASS, 27 R3 manifests and 88 sealed file checks, including fresh blind/hostile subdirectories. R4 dispatch manifest also passes. New text control-character scan finds no defect.

Ten independently authored or root-rerun exact programs pass with the counts and scopes in CERTIFICATES/ROUND_003_VERIFICATION.md. Complete proof and issued audit reports were read, compared and dispositioned; candidate bytes remain original. The final seven-page TeX/PDF was compiled, complete log inspected and all pages rendered and visually checked, with affected pages rechecked after their final edits. No final TeX warning/error or visual defect. These are reproduction and artifact checks, not universal mathematical certification by computation.

## Staged inspection

The explicit initial stage contained 122 named campaign paths. Root inspected the path list, staged numerical summary, authority/state/decision changes and new-file contents through full proof/audit reads; every staged byte equals its reviewed working copy. git diff --check passes for tracked edits. git diff --cached --check reports exactly one preserved-evidence warning: CERTIFICATES/OUTPUTS/round003_tex_build.txt:99, final blank line. This is the verbatim build transcript; its blank line is intentionally retained. No other staged whitespace warning. No seal is normalized to silence a warning.

The validation record, complete inventory and checkpoint manifest are added explicitly after this inspection. The final inventory has 125 paths including itself and the non-self-referential SHA256 manifest; that manifest hashes the other 124 paths. Ordinary fast-forward push is authorized, followed by independent HEAD, origin/main and live origin main reads. Publication receipt is recorded after the commit under .git/campaign-records and in the next tracked round.
