# Internal claim crosswalk

This file records structural overlap among live branches. Approximate equality means “same mathematical territory,” not identity of statement or proof.

| PR #3 qualified claim | Issue #4 qualified claim | Literature status | Integration note |
|---|---|---|---|
| `PR3/L-0001` parity-affine formula | `CLAUDE/D-0001`, `CLAUDE/L-0001`–`CLAUDE/L-0004` use the same cylinder calculus | `KNOWN — EXACT/STANDARD` via Everett–Terras | A canonical imported dependency should replace duplicate folklore proofs only if branch authors agree. |
| `PR3/T-0001` consecutive collision conjugacy | `CLAUDE/T-0015` `64→81` collision/conjugacy | `PARTIAL INTERNAL OVERLAP` | PR3 theorem is general for consecutive bundles; CLAUDE theorem is one exact chart with a specialized lift. |
| `PR3/T-0002` arbitrary finite collision-fiber conjugacy | `CLAUDE/T-0015` and atlas framework | `POSSIBLY NOVEL FORMULATION` | No exact external antecedent located; PR3 appears to subsume the finite conjugacy mechanism. |
| `PR3/L-0002` nine-column amplifier | `CLAUDE/L-0010`, `CLAUDE/L-0014` | `STRONG INTERNAL OVERLAP` | Independent derivations may support review after exact notation reconciliation. |
| `PR3/L-0004` universal carry pumping | CLAUDE stack-amplifier program | `POSSIBLY NOVEL FORMULATION` | PR3 general theorem appears broader than the recorded `64→81` instance. |
| `PR3/T-0003` dual adic/real coding and aperiodicity | `CLAUDE/T-0002`, `CLAUDE/T-0018`, `CLAUDE/Q-0001`–`CLAUDE/Q-0002` | `PARTIAL INTERNAL OVERLAP` plus classical `2`-adic context | Bernstein–Lagarias is neighboring theory, not the same coding theorem. |
| `PR3/T-0004` run-length skeleton | `CLAUDE/L-0015`, `CLAUDE/T-0020` | `DIRECT INTERNAL DEPENDENCY` | CLAUDE skeleton-rigidity work should cite PR3's exact skeleton equivalence after integration. Classical `S`-unit terminology alone gives no theorem application. |
| `PR3/L-0003` exact fiber recursion | CLAUDE atlas enumerations | `POSSIBLY NOVEL ALGORITHM/FORMULATION` | Compare implementations before merging claims; no external exact recursion located. |
| `PR3/T-0005` exponential supercritical fibers | `CLAUDE/C-0003` empirical fiber-width growth, `CLAUDE/Q-0004` capacity | `PR3 PROPOSED RESOLUTION OF EXISTENCE/UNBOUNDEDNESS` | Classical pigeonhole/CRT ingredients; no exact literature theorem located. Does not settle geometric closure quality. |
| `PR3/T-0006` geometry-preserving collision-code amplification | CLAUDE multi-chart/ladder questions | `POSSIBLY NOVEL FORMULATION` | High-priority internal cross-review target; external tree-density results do not imply it. |
| `CLAUDE/T-0003` automaticity package | no direct PR3 counterpart | `REPAIRABLE EXTERNAL DEPENDENCY` | Replace Cobham-as-frequency argument with KTHM-0005; use Cobham only if two-base recognizability is established. |
| `CLAUDE/T-0006` SML finiteness | no direct PR3 counterpart | `UNVERIFIED REDUCTION` | Exact power sum and nondegeneracy must be written. |
| `CLAUDE/T-0019` order formulas | arithmetic used throughout both branches | `KNOWN — COROLLARY` via KTHM-0004 | General proof now available; still requires independent review. |
| `CLAUDE/T-0020` skeleton rigidity | depends conceptually on `PR3/T-0004` | `PARTIAL EXTERNAL SUPPORT` via KTHM-0008 | The rational-series external step is supplied; full theorem remains internal and proposed. |
| `CLAUDE/T-0021` free-bridge nullity | `PR3/L-0005` parity-signature framework | `KNOWN — COROLLARY` of parity-residue bijection for the uniformity step | The convexity/relay corollary remains internal. |
| `TERM/L-9001` and associated rewrite frontier | AYH 2023 rewrite system | `KNOWN — EXACT EXTERNAL FRONTIER` | Keep imported literature theorem separate from local reimplementation and termination experiments. |

## Integration order

1. Preserve branch-qualified IDs until one mathematical branch merges.
2. Add literature imports as dependencies without changing mathematical status.
3. Reconcile exact duplicate finite claims (`64→81`, nine-cycle) by independent reconstruction.
4. Map broader PR3 generalizations to specialized CLAUDE instances.
5. Only then allocate canonical IDs and update `CLAIMS.md`.
