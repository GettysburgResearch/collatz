# X-8611 — Complete support-seventeen necklace quotient

**Status:** exact finite computation (`EMPIRICAL` pending independent implementation)  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Associated claim:** `T-8603`

## Scope

The support-sixteen cyclic quotient extends to seventeen defects. Since `17` is
prime, every nonconstant defect necklace has exactly seventeen rotations; the
only shorter orbit is a constant defect word. The program retains one
lexicographically least rotation and enumerates every compatible seventeen-gap
vector, so the quotient is exact.

The exact product inequalities

```text
3^(17+R) < 2^(B+2R),
2^(B+2R) * 7^(17+R) <= 22^(17+R)
```

leave 55 finite `(R,B)` cells. Each canonical pattern is split into 8 and 9
defects. For every split of the neutral total, the smaller transformed residue
list is stored and the larger is queried under the exact affine join

```text
C(uv)=3^len(v) C(u)+2^A(u) C(v).
```

Every modular match is regenerated and valuation-replayed.

## Frozen result

```text
windows=55
anchored_words=16071941097518
canonical_pattern_gap_instances=4856645105230
stored_states=17053060
queries=2471674701
formal_matches=0
exact_cycles=0
```

No cell produced even a formal divisibility match.

## Execution

The final large all-one cells were split by the neutral total carried in the
left half. This changes neither coverage nor the join; it only keeps every
execution shard below the connector runtime cap. The canonical transcript
contains one combined line per product cell.

```bash
g++ -O3 -std=c++17 -Wall -Wextra run.cpp -o /tmp/x8611
/tmp/x8611 0 9
# Optional third/fourth arguments restrict the left-half neutral count:
/tmp/x8611 31 31 0 3
/tmp/x8611 31 31 4 15
/tmp/x8611 31 31 16 31
python3 verify.py results/canonical.txt
```

The C++ implementation self-tests its Montgomery multiplier against
arbitrary-precision products on every modulus above 64 bits.

SHA-256:

```text
run.cpp       ecb7c18a4ebe25cc890a6003367fb8b6964bc374d4a81a073f44c425454e735d
canonical.txt 6a8a5969d7047676c092909617e62ed2f7d4ed6dce07b4dc67f7aeb1b1e4312f
```

## Limitations

This closes exactly seventeen defects. It does not address support eighteen or
nonperiodic divergent trajectories. Independent reimplementation is still
required before theorem-status promotion.
