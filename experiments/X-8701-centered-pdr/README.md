# X-8701 — Centered forced-tail PDR and carry audit

**Experiment ID:** `X-8701`  
**Agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Status:** `EMPIRICAL` exact-interface audit  
**Frozen source:** PR #16 at `87478352e65c7b816dfc8b3b30894b71fb50f662`

## Questions

1. Does the exact forced-tail branch table replay?
2. What is the greatest existential safety kernel at fixed dyadic precision?
3. Does it agree with the cylinder/de Bruijn theorem `T-8701`?
4. Are its cycles exactly periodic `2`-adic ghost reductions?
5. Is multiplication by `81` a bounded-carry base-64 transducer?
6. Do small positive ordinary seeds suggest an infinite path?

## Independent implementations

- `build.py` constructs the graphs by explicit high-block lifting, computes SCCs and reverse cycle basins, and emits a frozen certificate.
- `verify.py` does not import `build.py`. It uses the closed cylinder sum, iterative greatest-fixed-point deletion, an alternative carry-state audit, and independent seed replay.

## Frozen scope

```text
full ambient graphs: d=1,2,3
cylinder injectivity: d=1,...,15
periodic controls: periods 1,...,15
base-64 digit checks: 300,000
mod-17/monotonicity steps: B<=1,000,000
ordinary seed scan: B<=1,000,000, both signs
```

## Results

```text
d=1: ambient 4,     recurrent kernel 4
d=2: ambient 256,   recurrent kernel 8
d=3: ambient 16384, recurrent kernel 16
```

The kernel sizes equal `2^(d+1)` and every internal edge is the binary shift-and-append edge. Through precision fifteen, all `65,536` cylinder states are distinct.

Every nonconstant periodic control through period fifteen selects a nonintegral rational `2`-adic completion. The only constant controls select nearest integer zero.

The bounded seed scan finds maximum survival depth four, uniquely first attained at

```text
B=262144=64^3,
e=0.
```

This does not bound survival at larger heights.

## Replay

```bash
python3 -B experiments/X-8701-centered-pdr/build.py \
  --output /tmp/X-8701.json \
  --check-results experiments/X-8701-centered-pdr/results/canonical.json

python3 -B experiments/X-8701-centered-pdr/verify.py \
  experiments/X-8701-centered-pdr/results/canonical.json
```

## Limitations

- Fixed-modulus cycles are intentionally shown to be insufficient.
- Finite seed failure is not an infinite theorem.
- The experiment neither constructs nor excludes a positive infinite ordinary path.
- The issue-#4 translation to physical Collatz coordinates is not replayed here.
