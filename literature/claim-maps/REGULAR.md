# Claim map — PR #12 regular-sanctuary program

Namespace: `REG/...`.

| Claim | Literature verdict | Mapping |
|---|---|---|
| `REG/D-9101` canonical LSD-first semantics | `NATIVE DEFINITION` | must remain frozen; no literature theorem replaces endpoint/canonicalization choices |
| `REG/L-9101` five-state shortcut transducer | `POSSIBLY NOVEL IMPLEMENTATION` | subsequential-transducer framework is standard; arithmetic correctness proof is native |
| `REG/L-9102` exact closure decision | `KNOWN — COROLLARY` | `LIT-KTHM-0019` and `LIT-KTHM-0020` |
| `REG/L-9103` maximal safe acceptance kernel | `FOLKLORE / STANDARD` | `LIT-KTHM-0021` gives the greatest-fixed-point proof |
| `REG/L-9104` short canonical witness | `FOLKLORE / STANDARD` | `LIT-KTHM-0022` |
| `REG/L-9105` fixed-block normalization | `KNOWN — COROLLARY` | regular images under a subsequential transducer remain regular; union of the first `B` phases gives a one-step invariant language |
| `REG/X-9101` bounded skeleton search | `INTERNAL EXACT COMPUTATION` | excludes only the declared labeled skeletons/templates |
| conditional 72-state floor | `KNOWN — COROLLARY, external range check required` | short-witness theorem plus Barina's exact published verification frontier; strict inequality wording must be copied exactly |

## Closest literature

Caucal–Rispal and Shallit–Wilson show that finite-state/transducer viewpoints around Collatz are genuine, established territory. The branch's distinctive contribution is not the abstract closure decidability theorem but the exact canonical finite-word semantics, terminal carry handling, adversarial checker, and safe-kernel synthesis for the standard shortcut map.

## Strategic advice

- Use SAT/CEGIS or antichain reachability over a frozen skeleton rather than labeled brute force.
- Mine minimized finite-horizon safety automata for conjectural quotients, but require exact closure replay.
- Represent cyclic phase covers as one safety game; `L-9105` shows fixed powers do not enlarge the existential class.
- Keep the external numerical frontier out of candidate soundness.
- A regular sanctuary is much stronger than one divergent orbit, so bounded failure is weak evidence about Collatz itself.