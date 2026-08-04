# X-8609 — Complete support-fifteen accelerated-cycle join

**Status:** exact finite computation (`EMPIRICAL` pending independent implementation)  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Associated claim:** `T-8603`

## Scope

Every positive valuation word with exactly fifteen entries different from `2`
is represented uniquely as fifteen defect letters and fifteen neutral gaps. Exact
product bounds select 42 finite `(R,B)` cells. The program splits the word into
7- and 8-defect halves and performs the exact affine divisibility join.

For moduli above 64 bits, the implementation uses a two-limb Montgomery
reduction with a separately checked 128-by-128 product. Any modular match is
regenerated, converted to the forced positive start, and replayed valuation by
valuation.

## Frozen result

The computation was run in six neutral-total chunks:

```text
0..9
10..14
15..19
20..24
25..26
27..28
```

The complete concatenated transcript is committed as `results/canonical.txt`.
Combined exact coverage is

```text
windows=42
conceptual_words=355362127531
left_states=126760223
right_states=475187506
queries=126760223
hits=0
```

Chunk runtimes in the authoring environment were:

```text
0:01.73, 0:09.08, 0:17.87, 0:17.06, 0:08.57, 0:14.21
```

Canonical SHA-256 values are recorded in
`results/CANONICAL_SHA256SUMS`.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra run.cpp -o /tmp/x8609
for range in '0 9' '10 14' '15 19' '20 24' '25 26' '27 28'; do
  set -- $range
  /tmp/x8609 "$1" "$2"
done
python3 verify.py results/canonical.txt
```

The checker independently reconstructs all 42 product windows and all
conceptual and half-state counts, and directly enumerates the smallest cells.

## Limitations

This is a finite theorem at defect support fifteen. It does not settle support
sixteen or any divergent nonperiodic orbit.
