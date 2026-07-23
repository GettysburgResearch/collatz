# X-8511 — Intrinsic Hensel quotient and fixed toll alphabet

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claim:** `L-8512`  
**Status:** exact finite interface audit; theorem remains `PROPOSED`

## Questions

1. Is the high-divisibility coordinate unimodular?
2. Do the four complete next residues form an affine image of one fixed alphabet?
3. Does that residue automatically enforce the current physical type gate?
4. Is the only additional source restriction exactly a two-of-three primitive lift gate?
5. Does the unused ordinary lift transport with multiplier `3^G`?

## Frozen result

At every audited finite state the Hensel quotient `q` satisfies

```text
C=a+2^D*q,
Y=h+3^G*q,
[[2^D,a],[3^G,h]] in SL_2(Z).
```

The four complete current-target/next-high-divisibility residues are

```text
q == Lambda + U*b_j mod H_t,
b=(9,54,36,24),
H_t=2^(11(t+33)),
```

for one odd unit `U`. Each residue automatically produces the correct physical type `p_j`, and exactly two free-lift classes modulo three give a primitive source core.

Frozen coverage:

```text
finite states:                    48
unimodular matrices:              48
target residues:                  192
affine toll rows:                 192
automatic type gates:             192
two-of-three primitive gates:     192
legal refund replays:             768
intrinsic inverse checks:         768
```

Semantic digest:

```text
aae8894b675bc797745ed61899af18d8828471460f7fe094123c1e47c637d957
```

## Independent implementations

- `derive.py` uses the closed inverse and next-state formulas.
- `verify.py` reconstructs the determinant-one coordinate, next inverse, fixed-toll congruence, primitive gates, and refund transitions independently; it imports no author module.

## Replay

```bash
python3 -B experiments/X-8511-hensel-toll-alphabet/derive.py \
  --output /tmp/X-8511.json \
  --summary /tmp/X-8511.txt \
  --check-results \
  experiments/X-8511-hensel-toll-alphabet/results/canonical.json

python3 -B experiments/X-8511-hensel-toll-alphabet/verify.py \
  experiments/X-8511-hensel-toll-alphabet/results/canonical.json
```

## Limitations

- The finite audit corroborates the interfaces; the all-height conclusion is the proof in `L-8512`.
- A fixed four-value toll alphabet does not prove an ordinary quotient hits it forever.
- The affine unit and translation still change with height and finite state.
- No counterexample integer is produced.
