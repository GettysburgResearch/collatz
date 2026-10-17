# X-8602 — Exact low-complexity cycle census at `(m,K)=(41,65)`

**Experiment ID:** `X-8602`  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Date:** 2026-07-22  
**Status:** exact finite computation (`EMPIRICAL` in the repository status vocabulary)

## Research question

Can the first nontrivial upper continued-fraction shape `65/41` contain a cycle whose valuation word has either:

1. only exponents `1` and `2`; or
2. exactly one exponent at least `3`, with every other exponent `1` or `2`?

## Programs

- `run_binary.cpp`: all `{1,2}` words with exactly 24 twos.
- `run_one_large.cpp`: fixes the unique large exponent `e=3,...,25` and exhausts every location and every compatible binary remainder.
- `verify.py`: direct small-instance searches plus independent combinatorial count identities.

Both C++ programs use the exact concatenation residue equation modulo

```text
D = 2^65 - 3^41 = 420491770248316829.
```

## Replay

```bash
g++ -O3 -std=c++17 run_binary.cpp -o run_binary
g++ -O3 -std=c++17 run_one_large.cpp -o run_one_large
./run_binary 41 65
./run_one_large
python3 verify.py
```

## Frozen result

```text
binary words                 =   151,584,480,450
one-large-exponent words     = 35,397,011,688,418
combined words               = 35,548,596,168,868
combined modular matches     = 0
```

The full positive-composition space has `250,649,105,469,666,120` words, so this experiment deliberately does not claim an unrestricted `(41,65)` exclusion.
