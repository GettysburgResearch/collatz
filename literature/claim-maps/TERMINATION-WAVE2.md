# Claim map — PR #6 termination frontier, wave 2

Namespace: `TERM/...`.

| Claim/interface | Verdict | Literature boundary |
|---|---|---|
| AYH mixed binary–ternary system | `KNOWN — EXACT` | Yolcu–Aaronson–Heule; already imported as `LIT-KTHM-0013` |
| `TERM/L-9001` unbounded canonical match height | `POSSIBLY NOVEL INSTANCE`, method scope standard | `LIT-KTHM-0025`; confirms failure of one finite global match-bound certificate only |
| `TERM/R-9001` weak-component/cycle-minimum inference | `FOLKLORE / STANDARD` graph logic | complete in-repo countermodel; no Collatz-specific sibling bound follows without arithmetic proof |
| `TERM/Q-9001` multi-state natural selector | `OPEN` | finite-dimensional linear inequalities and Farkas duality are standard; the eleven-rule symbolic block constraint is native |
| `TERM/Q-9002` arctic interacting return | `OPEN` | tropical/arctic matrix interpretations are standard termination tools; strictness through the exact critical core remains native |

## Recommended evidence format

For natural/tropical/arctic searches, store both a candidate and a proof-producing dual:

- complete matrices/vectors or symbolic block parameters;
- every weak rule inequality;
- the marked strict inequality;
- monotonicity/context conditions;
- a Farkas certificate for UNSAT claims where available;
- exact tool/version and annotation conventions.

The packet's provenance boundary is mathematically important and should be retained after integration.