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
