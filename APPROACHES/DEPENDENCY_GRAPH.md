# Initial dependency graph

```text
M0 normalization + source audit
        |
        v
PO-002 exact pair operator ----> COR-001 quadratic corrector
        |                              |
        v                              v
PO-003 all-order recursion ----> PO-004 critical power counting
        |                         /             \
        v                        v               v
THM-001 exact algebra     finite closure     infinite/enlarged state
        |                        \               /
        v                         v             v
THM-002 smooth theorem -------- PO-005 / PO-006
        |                              |
        +------------------------------+
        |
        +--> PO-007 HS singular limit --> subcritical branch 2s<d
        +--> PO-008 borderline CT ------> subcritical/critical 2s=d
        +--> PO-009 UV pair field ------> subcritical/critical 2s>d
        |
        +--> PO-010 centering + PO-011 moving static response
        |
        v
THM-003 singular subcritical
        |
        v
THM-004 singular critical
        |
        v
THM-005 sharpness + THM-007 extensions
```

`THM-006` one-dimensional ordered work runs in parallel after `PO-002` and feeds mechanism/estimate information back into the main graph.

## Round 001 gate overlay

M0 PASS (frozen campaign normalization, independent smooth duality, source intake); M1 PASS (pair identity, full trace/noise accounting, independent BBGKY reconstruction, AUD-002 hostile pass). The unrelated SRC-005 printed constant is quarantined, so it is not an unresolved conflict in the frozen campaign normalization. PO-003/THM-001 smooth algebra has a hostile-reviewed proof. M2 is still OPEN at PO-004: no complete critical scaling/summability theorem. PO-001a/THM-009 supplies a bounded fixed-smooth pair estimate only; it feeds the still-open law-specific residual card. M3–M7 stay OPEN. No singular local-equilibrium branch was started ahead of these gates.

## Round 003 bounded initial-law overlay

THM-015 exact iid pair identity -> THM-016 sufficient probability comparison -> THM-018 L1 upper rates; THM-019 adds a separately reviewed lower-probability mechanism. These are initial bare-potential results. THM-017 exact internal-transport profile + THM-015 -> negligible diagnostic initial endpoint. The unproved edge from that diagnostic to COR-001 is PO-017, including diffusion and both response terms. No edge bypasses PO-001 evolved-law residuals, PO-004 critical power counting, or singular well-posedness/model comparison. M2 and the flagship gates remain OPEN.

Round007: THM021+THM023/024/025 -> THM027 weighted C1/H1 (fresh AUD032/033). THM028 separately rebuilds higher flow/time lemmas and uses THM026 plus R1 exact algebra; its candidate is under fresh audit. Conditional THM029 uses the full THM028 domain plus R5 N-uniform amplitude/norm bounds to target Haar noise energy. PO024 actual two-/three-marginal transfer is not a consequence of that reference estimate and remains inside open PO001.
