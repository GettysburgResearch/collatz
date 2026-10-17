# X-9508 — structured compiler and renewal search

**Status:** `INTERNAL EXACT COMPUTATION`; finite search only.

This experiment supports Iteration 09. It has two parts.

1. It verifies the exact normalized affine data of the compiler suffixes `10`
   and `30`, including their zero-carry displacement at the canonical input.
2. It enumerates a finite box of centered renewal stars and iterates the exact
   renewal map, searching directly for a positive cycle or an unusually long
   renewal chain.

The centered input is

```text
3^a X + 1 = 8^R U,
X = 5 mod 6,
U = 1 mod 4.
```

For fixed `(a,R)`, the script uses the unique canonical residue modulo
`3*2^(3R+2)` and scans its first `t_max+1` positive lifts. A legal output must
satisfy

```text
4^b Y + 1 = 9^R U,
Y = 5 mod 6.
```

The canonical run is

```bash
python3 run.py \
  --a-max 30 \
  --R-max 20 \
  --t-max 2000 \
  --max-steps 100 \
  --output results/canonical.json
```

It checks 1,200,600 stars, 800,375 valid first renewals, and finds no cycle.
The longest exact renewal chain has length five. This is finite evidence only;
it does not exclude a counterexample outside the search box.

Semantic digest:

```text
0dd31788d926b9d5a815860a97e8d16300cb627c4b3dabba5dbed15c449a7eda
```
