# Compressed positive-cycle synthesis — `86xx` packet

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Status:** no counterexample candidate; theorem-level claims are `PROPOSED`

## Objective

Produce the shortest acceptable Collatz disproof: one finite nontrivial positive
Syracuse-cycle certificate, with every valuation and return independently
replayable.

## Current exact contributions

- `T-8601`: every nonempty sanctuary defined solely by complete residue classes
  modulo a fixed integer contains the residue of `1`. This theorem has passed
  one independent reconstruction on draft PR #48.
- `T-8602`: exact proof-producing census of every positive-cycle product window
  through 27 accelerated odd terms.
- `X-8602`: 35.5-trillion-word low-complexity census at `(m,K)=(41,65)`.
- `T-8603`: exact centered-defect exclusion for support sizes seven through
  fifteen. Combined with branch-qualified proposed `PR34/L-9913`, the current
  proposed floor is at least sixteen valuations different from `2`.
- `L-8604`: complete exclusion of the infinite concentrated-tail family
  `(b,1^13,2^R)`.
- `X-8608`: complete support-fourteen product-window join.
- `X-8609`: complete support-fifteen product-window join.

## Frozen centered-defect totals

```text
support 7..12: enumerated_rows=2,577,878,885, hits=0
support 13:    queries=64,674,409, hits=0
support 14:    conceptual_words=50,008,555,902, hits=0
support 15:    conceptual_words=355,362,127,531, hits=0
```

The first open defect layer is support sixteen. The first unfinished product
cell in the current scout is `(R,B)=(24,18)`.

## Honest status

No positive cycle, divergent seed, invariant sanctuary, or other unconditional
Collatz counterexample has been found. The finite searches are retained because
they remove declared complete parameter layers without confusing bounded
computation with a global theorem.

## Review order

1. `claims/T-8601-no-periodic-congruence-sanctuary.md`
2. `claims/T-8603-centered-defect-frontier.md`
3. `experiments/X-8608-fourteen-defect-mitm/README.md`
4. `experiments/X-8608-fourteen-defect-mitm/run.cpp`
5. `experiments/X-8609-fifteen-defect-mitm/README.md`
6. `experiments/X-8609-fifteen-defect-mitm/run.cpp`
7. independent verifiers for `X-8608` and `X-8609`
8. reports under `reports/gpt56-cycle-01/`

## Next constructive target

Finish support sixteen beginning with `(R,B)=(24,18)` using a proof-producing
external merge, residue bucket, or factorwise CRT join. Any modular match must
be converted immediately into one explicit positive integer and exact valuation
replay.
