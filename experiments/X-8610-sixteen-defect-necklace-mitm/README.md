# X-8610 — Complete support-sixteen necklace quotient

**Status:** exact finite computation (`EMPIRICAL` pending independent implementation)  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Associated claim:** `T-8603`

## Eureka: quotient the cyclic defect orbit

A support-sixteen valuation word can be rotated to begin at a defect. Its
sixteen defect letters form a cyclic word. Instead of searching all rotations,
the experiment retains the lexicographically least rotation of each defect
necklace and then enumerates every compatible sixteen-gap vector.

This is lossless: rotating any putative cycle to the canonical defect word
rotates its gap vector, and every gap vector is present. The reduction shrinks
the first formerly expensive cell `(R,B)=(24,18)` to one defect necklace and a
peak in-memory residue table below 51,000 entries.

## Exact finite cells

For defect support `s=16`, defect sum `B`, and neutral count `R`, the exact
least-state product window is

```text
3^(16+R) < 2^(B+2R),
2^(B+2R) * 7^(16+R) <= 22^(16+R).
```

There are exactly 48 admissible cells. For each canonical defect necklace, the
program splits after eight defects. At a fixed split of the neutral total it
stores the smaller of the two exact gap-composition residue lists and queries
the larger. The affine join is

```text
C(uv) = 3^len(v) C(u) + 2^A(u) C(v).
```

Every modular match is regenerated as a full word, converted to the forced
start `C/D`, and valuation-replayed before being counted as a cycle.

## Frozen result

```text
windows=48
anchored_words=2216415791876
canonical_pattern_gap_instances=724990098067
stored_states=6134501
queries=543652557
formal_matches=0
exact_cycles=0
```

The computation found not even a formal divisibility match.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra run.cpp -o /tmp/x8610
for range in '0 9' '10 14' '15 19' '20 24' '25 28' '29 29'; do
  set -- $range
  /tmp/x8610 "$1" "$2"
done
python3 verify.py results/canonical.txt
```

The C++ implementation self-tests its 128-bit Montgomery multiplier against
arbitrary-precision arithmetic on every modulus above 64 bits.

SHA-256:

```text
run.cpp       08708af4ca3f45a1378309a5642d198443fd3080276a1e3c267f44c529fd5e28
canonical.txt 76630a7bd351fdbf73804628b60421243a27dea9ad2e43739c52d554fd7a49a8
```

## Limitations

This is a complete exact result only for support sixteen. It does not address
support seventeen or divergent nonperiodic orbits. The necklace quotient and
residue join still require an independent implementation before theorem-status
promotion.
