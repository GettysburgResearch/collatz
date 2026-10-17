# X-8601 — Exact positive-cycle window exhaustion through `m=27`

**Experiment ID:** `X-8601`  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Date:** 2026-07-22  
**Status:** exact finite computation; theorem implication submitted as `T-8602` (`PROPOSED`)

## Research question

After applying the exact positivity and `x_min>=7` window, does any positive composition of a total exponent `K` into `m<=27` accelerated odd steps satisfy the necessary cycle divisibility equation?

## Method

For each `m`, the program determines every `K` by exact integer comparisons:

```text
3^m < 2^K
2^K * 7^m <= 22^m
```

For each surviving pair it splits every positive composition into fixed left and right lengths and uses

```text
C(uv) = 3^len(v) C(u) + 2^K(u) C(v)
```

modulo

```text
D = 2^K - 3^m.
```

The left table stores exactly the right residue required for divisibility. A match is therefore equivalent to `D | C(uv)`; there is no probabilistic filter and no omitted composition.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra run.cpp -o run
./run 27
python3 verify.py
```

The largest pair can also be replayed independently:

```bash
./run 27 44
```

## Frozen result

```text
tested_pairs=24
total_compositions=802459998516
total_modular_matches=0
nontrivial_cycles=0
```

See `results/canonical.txt` for every window.

## Independent validation

`verify.py` performs direct, non-MITM enumeration for:

- the trivial control `(m,K)=(1,2)`, recovering exactly `word=(2), x=1`;
- every forced nontrivial window through `m=14`, recovering no divisibility hit.

## Environment

- C++17
- standard library only
- exact `unsigned __int128` arithmetic for window inequalities and composition counts
- exact 64-bit modular arithmetic with 128-bit products for all tested denominators

## Limitations

- The search stops at 27 odd terms.
- It does not address divergent orbits.
- `m` is the accelerated odd-term count, not an external paper's local-minimum parameter.
