# X-8505 — Intrinsic primitive-core decoder audit

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claims:** `L-8505`, `T-8506`, `T-8507`  
**Status:** exact finite interface audit

## Question

Does the primitive-core decoder reconstruct exact two-step physical connector chains using only

```text
height,
previous ternary signature,
current binary type,
one positive prime-to-six core?
```

## Implementations

- `derive.py` constructs exact two-step complement chains, discards the inverse/carry data, and reconstructs the second connector only from `3^G C+1`.
- `verify.py` is separately written and uses a different height, type subset, and high lift.

## Replay

```bash
python3 -B experiments/X-8505-intrinsic-core-decoder/derive.py \
  --output experiments/X-8505-intrinsic-core-decoder/results/canonical.json \
  --summary experiments/X-8505-intrinsic-core-decoder/results/summary.txt

python3 -B experiments/X-8505-intrinsic-core-decoder/verify.py \
  experiments/X-8505-intrinsic-core-decoder/results/canonical.json
```

## Frozen result

```text
intrinsic core transitions:       256
automatic source-cell checks:     256
high-block divisibility checks:   256
six-bit output decodes:           256
170-bit growth checks:            256

semantic digest:
195d29ef16bb7038ac9b3da9080344dfcc450f6663a973a757e475503afcf10e
```

Independent checker:

```text
intrinsic transitions:     32
automatic source cells:    32
six-bit target cells:      32
all independent checks passed
```

## Limitations

The experiment reconstructs legal finite transitions. It does not supply a core whose decoder is defined forever.
