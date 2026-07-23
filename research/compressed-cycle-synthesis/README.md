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
  modulo a fixed integer contains the residue of `1`. This theorem passed one
  independent reconstruction on draft PR #48.
- `T-8602`: exact proof-producing census of every positive-cycle product window
  through 27 accelerated odd terms.
- `X-8602`: 35.5-trillion-word low-complexity census at `(m,K)=(41,65)`.
- `T-8603`: exact centered-defect exclusion for support sizes seven through
  seventeen. Combined with branch-qualified proposed `PR34/L-9913`, the current
  proposed floor is at least eighteen valuations different from `2`.
- `L-8604`: complete exclusion of the infinite concentrated-tail family
  `(b,1^13,2^R)`.
- `X-8608` / `X-8609`: complete product-window joins at supports fourteen and
  fifteen.
- `X-8610`: complete support-sixteen join using the cyclic defect-necklace
  quotient.
- `X-8611`: complete support-seventeen necklace join.

## Frozen centered-defect totals

```text
support 7..12: enumerated_rows=2,577,878,885, hits=0
support 13:    queries=64,674,409, hits=0
support 14:    conceptual_words=50,008,555,902, hits=0
support 15:    conceptual_words=355,362,127,531, hits=0
support 16:    anchored_words=2,216,415,791,876, formal_matches=0
support 17:    anchored_words=16,071,941,097,518, formal_matches=0
```

The first open defect layer is support eighteen.

## Eureka mechanism

A cycle can be rotated to the lexicographically least rotation of its cyclic
defect word. Rotating the cycle only rotates the neutral-gap vector, and every
gap vector is already enumerated. Searching one defect necklace plus all gaps
is therefore lossless. This removes a large redundant rotation factor while
preserving exact affine divisibility and full valuation replay.

## Honest status

No positive cycle, divergent seed, invariant sanctuary, or other unconditional
Collatz counterexample has been found. The finite searches are retained because
they remove complete parameter layers without confusing bounded computation
with a global theorem.

## Review order

1. `claims/T-8601-no-periodic-congruence-sanctuary.md`
2. `claims/T-8603-centered-defect-frontier.md`
3. `experiments/X-8610-sixteen-defect-necklace-mitm/README.md`
4. `experiments/X-8610-sixteen-defect-necklace-mitm/run.cpp`
5. `experiments/X-8610-sixteen-defect-necklace-mitm/verify.py`
6. `experiments/X-8611-seventeen-defect-necklace-mitm/README.md`
7. `experiments/X-8611-seventeen-defect-necklace-mitm/run.cpp`
8. `experiments/X-8611-seventeen-defect-necklace-mitm/verify.py`
9. reports under `reports/gpt56-cycle-01/`

## Next constructive target

Apply the necklace compiler to support eighteen using row-level checkpoints,
neutral-split sharding, and a proof-producing prime-power/CRT prejoin for the
largest rows. Any modular survivor must be converted immediately into one
explicit positive integer and exact valuation replay.
