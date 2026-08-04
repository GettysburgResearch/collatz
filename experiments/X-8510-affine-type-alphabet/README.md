# X-8510 — Affine normalization of the four top-cell alphabets

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claims:** `L-8511`  
**Status:** exact finite interface audit; theorem remains `PROPOSED`

## Question

Do the four allowed input and output cells of every `L-8510` router have arbitrary shape, or are they state-dependent affine copies of the one fixed physical type alphabet

```text
p=(5,30,20,56)?
```

## Result

Across the frozen exact heights

```text
16, 32, 48, 64
```

and every finite state/current block, the scripts verify

```text
d_k = 3^(1-gamma) p_k + delta mod64,
e_k = 3^(8-beta_i) p_k + epsilon mod64,
3^(8-beta_i) = 3^G * 3^(1-gamma) mod64,
epsilon = 3^G delta + J mod64.
```

After the corresponding affine normalization, both the input and output digit recover the same `p_k`. The six-bit router is therefore conjugate to the identity on the physical four-letter type alphabet.

Frozen coverage:

```text
finite states:                    48
current blocks:                   384
four-way continuations:           1536
input affine alphabets:           384
output affine alphabets:          384
slope compatibility checks:       384
symbol identity checks:           1536
translation/carry checks:         384
```

Semantic digest:

```text
9a200a568909a8686c6f36436dac1bc6ef4be906b043fdba05aa5be70e2c057d
```

## Independent implementations

- `derive.py` uses the closed core-block and complete-continuation formulas.
- `verify.py` independently enumerates the six-bit core cells, reconstructs the complete next blocks, and checks the affine conjugacies without importing `derive.py`.

## Replay

```bash
python3 -B experiments/X-8510-affine-type-alphabet/derive.py \
  --output /tmp/X-8510.json \
  --summary /tmp/X-8510.txt \
  --check-results \
  experiments/X-8510-affine-type-alphabet/results/canonical.json

python3 -B experiments/X-8510-affine-type-alphabet/verify.py \
  experiments/X-8510-affine-type-alphabet/results/canonical.json
```

## Limitations

- The experiment verifies finite interfaces; the all-height conclusion is the algebraic proof in `L-8511`.
- Affine symbol normalization does not generate the common long residue.
- A fixed four-letter alphabet is not an ordinary infinite-orbit certificate.
