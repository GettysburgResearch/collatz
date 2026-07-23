# X-8509 — Common top prefix, base-64 carry, and noncanonical absorption

**Issue:** #43  
**Agent:** `gpt56-cylinder-01`  
**Status:** exact finite-interface audit supporting proposed `L-8509`, `L-8510`, and `T-8510`

## Questions

1. Do the four complete continuation residues of one current block share all but six bits?
2. Do their paired input/output cells satisfy one branch-independent affine identity?
3. Is the identity exactly a canonical base-64 quotient/remainder step?
4. When does one noncanonical lift force every later lift to remain noncanonical?

## Frozen exact results

At heights `32` and `48`, every finite state and all eight current blocks were reconstructed. For every block:

- four complete continuations have one common residue modulo `H/64`;
- their four remaining input digits are distinct;
- the four next complete source cells share one ternary residue;
- their reduced output digits are distinct;
- one common integer carry `J` satisfies
  ```text
  64*m_next+e_k=3^G*z+J;
  ```
- `0<=3J<4*3^G`;
- the canonical quotient/remainder formulas replay for several ordinary lifts.

Coverage:

```text
finite states:                    24
current blocks:                   192
four-way continuations:           768
common long prefixes:             192
common carry identities:          192
base-64 exact replays:           2304
```

Semantic digest:

```text
b05a53257b8309fcd9da40d389ed87daa8ffdeb208b5c3837b726668ac002b91
```

## Absorption thresholds

Using

```text
3^665 > 2^1054,
```

the exact lower refund exponent is

```text
q(t)=floor((63*t-353166)/665).
```

The audit confirms:

```text
t=5600: q=-1;
t=5616: q=0 and 3^(7t+5)>2^(11(t+49));
t=5632: q=2 and 3^(7t+5)>4*2^(11(t+49)).
```

Therefore, from height `5632`, any legal noncanonical lift satisfies

```text
ell_next>=4*ell
```

and can never return to the canonical region. `T-8509` guarantees that every hypothetical infinite path reaches such a lift within at most `471` connectors, so its tail is permanently refunded.

## Independent checker

`verify.py` does not import `derive.py`. It brute-enumerates the primitive block quotient modulo `192`, independently reconstructs selected finite states at different heights, reduces the mixed-radix congruence by ordinary gcd arithmetic, and directly checks the exact integer powers at the absorption thresholds.

Independent coverage:

```text
sample finite states:       4
sample current blocks:      8
continuations:             32
exact base-64 replays:     64
```

## Replay

```bash
python3 -B experiments/X-8509-base64-absorption/derive.py \
  --output /tmp/X-8509.json \
  --summary /tmp/X-8509.txt \
  --check-results \
    experiments/X-8509-base64-absorption/results/canonical.json

python3 -B experiments/X-8509-base64-absorption/verify.py \
  experiments/X-8509-base64-absorption/results/canonical.json
```

## Limitations

- Permanent refund is conditional on an infinite ordinary path existing.
- The common long prefix remains a changing Hensel residue that must be hit exactly.
- A four-digit base-64 transducer is not total on all integers.
- No explicit initial integer or `K-85xx` candidate is produced.
