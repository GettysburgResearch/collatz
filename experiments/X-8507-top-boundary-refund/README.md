# X-8507 — Type-independent top-boundary refund

**Issue:** #43  
**Agent:** `gpt56-cylinder-01`  
**Status:** exact finite-interface audit supporting proposed `L-8507` and `T-8508`

## Question

After the intrinsic eight-block core compiler of `L-8506`, what exact arithmetic remains when one demands compatibility with a complete block at the next linear height?

## Result checked

For every current finite core state and every one of its eight current blocks:

1. each prospective next target type has exactly one ternary lift compatible with the current output;
2. the common binary/ternary signature cancels from the complete next source modulus;
3. the remaining top-boundary modulus is exactly
   ```text
   2^(11*(t+33)),
   ```
   independent of every type and lift;
4. the four next target types give four distinct quotient residues;
5. every compatible lift has the exact form
   ```text
   m=rho+2^(11*(t+33))*ell
     ->
   m_next=sigma+3^G*ell,
   ```
   with `sigma>=0`;
6. the exact lower logarithm certificate
   ```text
   3^665 > 2^1054
   ```
   proves strict refund for all finite states from `t=3760` and more-than-doubling from `t=3776`.

## Author derivation

`derive.py` uses the closed block formulas of `L-8506`, computes every continuation at heights

```text
32, 64, 3760, 3776,
```

and replays three ordinary lifts in every continuation cylinder.

Frozen coverage:

```text
finite states:                    48
current eight-block states:       384
four-way continuations:           1536
exact quotient replays:           4608
```

Transition digest:

```text
66c03b99bb494255cc8d56f1e226c3f850f9548a60a0e3d3a036abac449cc724
```

## Independent checker

`verify.py` does not import `derive.py` and does not use the author's `kappa/nu` block construction. It brute-enumerates the complete quotient `q mod 192`, independently recovers the eight primitive blocks, uses an ordinary gcd reduction for the mixed-radix congruence, and replays different lift values.

Independent coverage:

```text
sample finite states:              6
enumerated blocks:                48
continuations:                   192
exact replays:                   576
```

Independent digest:

```text
e766446ce905c4e30342b4750a5a231cc8bb8d6306184cf2a805496045aa253c
```

## Replay

```bash
python3 -B experiments/X-8507-top-boundary-refund/derive.py \
  --output /tmp/X-8507.json \
  --summary /tmp/X-8507.txt \
  --check-results \
    experiments/X-8507-top-boundary-refund/results/canonical.json

python3 -B experiments/X-8507-top-boundary-refund/verify.py \
  experiments/X-8507-top-boundary-refund/results/canonical.json
```

## Limitations

- The four continuation residues do not cover the complete dyadic modulus.
- A noncanonical lift is strongly expanding, but no theorem says one finite integer hits a continuation residue forever.
- The computation does not extrapolate a finite prefix into an infinite orbit.
- No counterexample or `K-85xx` object is asserted.
