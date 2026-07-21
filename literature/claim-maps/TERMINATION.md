# Literature map — termination frontier (draft PR #6)

**Namespace:** `TERM/...`  
**Live branch:** `agent/gpt56-termination-01/5-termination-frontier-port`

## Exact external anchor

Yolcu, Aaronson, and Heule construct a finite string-rewrite system on mixed binary–ternary representations and prove that its termination is equivalent to the standard Collatz conjecture. This is a direct theorem about the standard map, unlike generalized-map undecidability results. [@YolcuAaronsonHeule2023]

| Local item | Verdict | Mapping |
|---|---|---|
| `TERM/L-9001` exact rule semantics / simulation invariant | `KNOWN — EXACT EXTERNAL FRONTIER` | Should cite the exact AYH theorem and separately record any local reimplementation proof. |
| Local eleven-rule system and boundary conventions | `KNOWN — EXACT` if byte-for-byte/notation-equivalent to AYH; otherwise `KNOWN — COROLLARY` after a rule translation | The PR should include a rule crosswalk to the article, not only an author-name citation. |
| Termination implies Collatz convergence | `KNOWN — EXACT` | Black-box import KTHM-0012. |
| Collatz convergence implies rewrite termination | `KNOWN — EXACT` | Black-box import KTHM-0012; check the quantified initial-string language. |
| Automated matrix/arctic interpretation experiments | `PARTIAL OVERLAP` | AYH already studies such interpretations and proves limitations for a unary system; local experiments may extend or reproduce that work. |
| Binary/ternary transducer or carry semantics | `PARTIAL OVERLAP` | Stérin–Woods give an exact quasi-cellular-automaton simulation and base-conversion theorem; a local rule crosswalk is still required. [@SterinWoods2020] |
| Any claim that generalized Collatz undecidability obstructs this standard system | `MISAPPLIED / HYPOTHESES FAIL` | Conway/Kurtz–Simon concern classes of generalized piecewise-affine maps, not the fixed standard map. [@Conway1972; @KurtzSimon2007] |

## Required review artifacts

1. A table matching every local rewrite rule to the published system.
2. A proof that local admissible strings are exactly the intended positive-integer encodings.
3. Separate labels for reproduced AYH claims and new termination-tool findings.
4. Exact tool versions, generated certificates, and independent certificate checking.
