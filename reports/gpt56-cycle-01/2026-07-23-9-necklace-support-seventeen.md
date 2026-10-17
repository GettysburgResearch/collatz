# Session report — cyclic-necklace breakthrough through support seventeen

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Date:** 2026-07-23

## Starting hypothesis

The prior session had completely excluded centered-defect supports fourteen and
fifteen and identified support sixteen as the next exact positive-cycle layer.
A naive `8+8` join reached its first expensive row at `(R,B)=(24,18)` because it
stored every cyclic rotation of every defect pattern separately.

The objective was still the full finite certificate: find one word with

```text
D=2^A-3^k>0,
D|C,
n_0=C/D>1,
```

then independently replay every advertised valuation and the return.

## Eureka

The defect word is cyclic. Every putative cycle can be rotated so that its
defect pattern is the lexicographically least rotation in its orbit. Rotating
the cycle rotates the neutral-gap vector, but every gap vector is already
enumerated. Therefore

```text
one defect necklace × every compatible gap vector
```

is a lossless quotient of the anchored search.

This removed the redundant rotation multiplicity while leaving the exact affine
join unchanged. At the previous bottleneck `(R,B)=(24,18)`, the defect alphabet
contains only one necklace and the peak stored residue table falls below 51,000
entries.

## Exact method

For fixed support `s`, defect sum `B`, and neutral count `R`, the exact product
window is

```text
3^(s+R) < 2^(B+2R),
2^(B+2R) 7^(s+R) <= 22^(s+R).
```

Each canonical defect necklace is paired with every weak composition of `R`
into `s` gaps. For a split `w=uv`,

```text
C(w)=3^len(v) C(u)+2^A(u) C(v).
```

The programs store the smaller transformed half-list at each neutral split and
query the larger. Moduli above 64 bits use a self-tested two-limb Montgomery
reduction. Every modular match is regenerated with arbitrary-precision integers
and exact valuation-replayed before being counted.

## New result: complete support sixteen

`X-8610` uses an `8+8` split. Frozen exact coverage:

```text
windows=48
anchored_words=2,216,415,791,876
canonical_pattern_gap_instances=724,990,098,067
stored_states=6,134,501
queries=543,652,557
formal_matches=0
exact_cycles=0
```

The independent verifier reconstructs every product cell, defect-necklace
count, conceptual count, and half-state count, and directly enumerates the
smallest cells.

SHA-256:

```text
run.cpp       08708af4ca3f45a1378309a5642d198443fd3080276a1e3c267f44c529fd5e28
canonical.txt 76630a7bd351fdbf73804628b60421243a27dea9ad2e43739c52d554fd7a49a8
```

## New result: complete support seventeen

`X-8611` uses an `8+9` split. Because 17 is prime, every nonconstant defect
pattern has rotation orbit 17; constant patterns are handled separately. Large
all-one cells were divided by left-half neutral total so the connector execution
cap could not hide a row.

Frozen exact coverage:

```text
windows=55
anchored_words=16,071,941,097,518
canonical_pattern_gap_instances=4,856,645,105,230
stored_states=17,053,060
queries=2,471,674,701
formal_matches=0
exact_cycles=0
```

SHA-256:

```text
run.cpp       ecb7c18a4ebe25cc890a6003367fb8b6964bc374d4a81a073f44c425454e735d
verify.py     599c1aadd284ee24fa3fff08e2ae73c7c6d06c84ca968992bd5beb9909a64d7c
canonical.txt 6a8a5969d7047676c092909617e62ed2f7d4ed6dce07b4dc67f7aeb1b1e4312f
```

The independent verifier reconstructs all 55 cells, necklace and state counts,
and directly exhausts the smallest cells.

## Updated theorem frontier

The native `86xx` packet now excludes exactly seven through seventeen defects.
Together with branch-qualified proposed `PR34/L-9913`, the current proposed
cycle floor is

```text
at least 18 valuations different from 2.
```

This is not an unconditional global theorem until the external six-defect claim
and the new large computations receive independent repository review.

## Candidate counterexamples

None. The complete support-sixteen and support-seventeen layers contained no
formal modular divisibility match, so no integer reached the replay gate and no
`K-####` identifier was created.

## Validation

```bash
g++ -O3 -std=c++17 -Wall -Wextra \
  experiments/X-8610-sixteen-defect-necklace-mitm/run.cpp -o /tmp/x8610
# Run in neutral-total chunks and concatenate the canonical transcript.
python3 experiments/X-8610-sixteen-defect-necklace-mitm/verify.py \
  experiments/X-8610-sixteen-defect-necklace-mitm/results/canonical.txt

g++ -O3 -std=c++17 -Wall -Wextra \
  experiments/X-8611-seventeen-defect-necklace-mitm/run.cpp -o /tmp/x8611
# Optional third/fourth arguments shard the left-half neutral total.
python3 experiments/X-8611-seventeen-defect-necklace-mitm/verify.py \
  experiments/X-8611-seventeen-defect-necklace-mitm/results/canonical.txt
```

Both independent audits pass.

## Potential errors and adversarial targets

1. Independently prove the defect-necklace quotient and gap rotation map.
2. Reimplement both joins without importing the submitted C++.
3. Audit the `8+8` and `8+9` affine multiplier orientation.
4. Recheck every Montgomery modulus against arbitrary-precision products.
5. Confirm that the shard boundaries partition each neutral split exactly once.
6. Keep anchored conceptual counts, canonical quotient counts, stored states, and
   query counts distinct.

## Files changed

```text
research/compressed-cycle-synthesis/claims/T-8603-centered-defect-frontier.md
research/compressed-cycle-synthesis/README.md
experiments/X-8610-sixteen-defect-necklace-mitm/
experiments/X-8611-seventeen-defect-necklace-mitm/
reports/gpt56-cycle-01/2026-07-23-9-necklace-support-seventeen.md
```

## Recommended next actions

1. Attack support eighteen with the same necklace quotient.
2. Use neutral-split shards and row-level canonical outputs from the start.
3. Add factorwise prime-power/CRT residue prejoins for the largest all-one cells,
   but require full-modulus reconstruction before accepting a survivor.
4. Share the changing-modulus compiler with PR #49's refund map: both lanes now
   isolate ordinary divisibility, while refund already supplies positivity and
   exponential growth after infinite definedness.
5. Request one cold mathematical proof of the necklace quotient and one fully
   independent computational implementation before status promotion.

## Organizational improvement

For cyclic certificate searches, publish both the anchored coverage count and
the quotient coverage count. The quotient is valid only with an explicit
surjectivity argument back to every anchored object; the anchored count remains
the clearest statement of what the finite theorem removes.
