# X-8512 — Logarithmic Hensel balls and full branch isometries

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claims:** `L-8514`, `T-8514`  
**Status:** exact finite-interface audit; theorem-level claims remain `PROPOSED`

## Questions

1. Does each target type correspond to one explicit Hensel ball in the base-nine logarithmic coordinate?
2. Do all four branch balls have one common depth?
3. Is the fixed odd-unit table independent of the height and ternary signature?
4. Does every normalized branch preserve every 2-adic distance and permute every finite quotient?

## Frozen result

For the logarithmic coordinate

```text
alpha=log_9(-3^delta C),
w=alpha+r,
```

branch `j` has

```text
v_2(w)=D+j-3,
w/2^(D+j-3)=c_(i,j) mod 2^(6-j),
```

with fixed table

```text
[31,29,15,5]
[53,31, 5,7]
[31,29,15,5]
[29,23,13,7].
```

Each branch is one residue modulo `2^(D+3)`. After the exact normalized-unit update and removal of the next short marker, every branch is a permutation of `Z/2^7Z` and preserves the valuation of all pairwise differences.

Frozen coverage:

```text
finite states:                    24
branch balls:                     96
source marker checks:             96
fixed unit rows:                  96
finite section permutations:      96
isometry pairs:                   780288
```

Semantic digest:

```text
bb13a38256234ad4cf44e75f19e57fa923a68ae3b8cf21951c3d2c35f2a7b3c4
```

## Independent implementations

- `derive.py` uses a precomputed `9^(2^v)` base and lifts the logarithm bit by bit.
- `verify.py` uses direct modular exponentiation for each section input, independently reconstructs the inverse logarithm from two candidates at each bit, and imports no author module.

## Replay

```bash
python3 -B experiments/X-8512-logarithmic-full-branches/derive.py \
  --output /tmp/X-8512.json \
  --summary /tmp/X-8512.txt \
  --check-results \
  experiments/X-8512-logarithmic-full-branches/results/canonical.json

python3 -B experiments/X-8512-logarithmic-full-branches/verify.py \
  experiments/X-8512-logarithmic-full-branches/results/canonical.json
```

## Limitations

- The finite sections corroborate the all-height proof; they do not prove it by exhaustion.
- The four-branch full shift exists in `Z_2`, not automatically in the ordinary positive integers.
- An isometric branch completion need not be the logarithm of a negative ordinary unit.
- No counterexample integer is produced.
