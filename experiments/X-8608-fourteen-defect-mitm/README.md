# X-8608 — Complete support-fourteen accelerated-cycle join

**Status:** exact finite computation (`EMPIRICAL` pending independent implementation)  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Associated claim:** `T-8603`

## Question

Can a nontrivial positive accelerated Collatz cycle have exactly fourteen
valuations different from `2`?

For total defect sum `B` and total number `R` of neutral `2` valuations, the
exact product bound for a nontrivial cycle with least odd state at least `7`
selects the finite cells

```text
3^(14+R) < 2^(B+2R),
2^(B+2R) * 7^(14+R) <= 22^(14+R).
```

Within each cell the program enumerates every length-14 defect word over
`{1,3,4,...}` and every weak composition of `R` into fourteen neutral gaps.
It splits after seven defects and uses the exact affine join

```text
C(uv) = 3^len(v) C(u) + 2^A(u) C(v).
```

A residue match is therefore exactly the necessary divisibility condition
`D | C`, not a trajectory sample. Any match is reconstructed and valuation-
replayed before being reported.

## Frozen result

```text
windows=37
conceptual_words=50008555902
left_states=62907549
right_states=62907549
queries=62907549
hits=0
```

Runtime in the authoring environment:

```text
time=0:10.29 mem=51176KB
```

SHA-256:

```text
run.cpp       48a8bf28f470c498f3494c245d8449b67eebec045079fc3be46b9712c918d02b
canonical.txt d8b39b08192ecc9df60ecc3fa78b4f318661f1520df1b609a0bb586590f8dfac
```

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra run.cpp -o /tmp/x8608
/tmp/x8608 > /tmp/x8608.out
diff -u results/canonical.txt /tmp/x8608.out
python3 verify.py results/canonical.txt
```

## Limitations

This closes exactly fourteen non-neutral valuations. It does not address
support fifteen or divergent nonperiodic orbits.
