# X-9602 — Distributed pulses on the negative three-cycle

**Status:** `EMPIRICAL` exact finite computation  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Associated claim:** `L-9602`

## Frozen family

Start from either primitive rotation of

```text
(1,2)^r
```

and add one extra dyadic division at each of `e` distinct positions, where

```text
e=min{j : 2^(3r+j)>3^(2r)}.
```

The resulting word is in the positive-multiplier regime. `L-9602` writes its candidate start as one exact rank-weighted subset sum modulo

```text
D=2^(3r+e)-3^(2r).
```

Every pulse set has a cyclic rotation with a balanced half split. The script therefore checks only the two primitive base rotations and the split counts

```text
floor(e/2), ceil(e/2),
```

using an exact two-list join. The balance lemma proves coverage; it is not heuristic pruning.

## Scope and result

```text
1 <= r <= 45
odd-step length <= 90
raw labeled pulse words covered: 508,127,577,642
nontrivial modular hits:          0
```

The two recorded hits are the two rotations of the trivial `n=1` word at `r=1`.

```text
results SHA-256:
d13475b2f56ea3601874eaf9f12bd2365d56c2653f6128e59e503259cb42627e

semantic row audit:
94d9ab777cafdce636b2bc7da4d4b760693d251d9e7696092b6f388936ca8a2a

run.py SHA-256 used in the authoring replay:
bbce8fbbd0c98944eb980577be03cb0f5da584a60a6255cc5bc9d6f0ee4129e3
```

## Replay

```bash
python3 -B experiments/X-9602-negative-cycle-distributed-pulses/run.py \
  --check-results \
  experiments/X-9602-negative-cycle-distributed-pulses/results/canonical.json
```

The authoring replay used exact Python integers, completed in under seven seconds, and peaked below 132 MiB. Resource figures are informational and are not part of the mathematical certificate.

## Boundary

- Pulse multiplicity is at most one per position.
- The pulse count is the minimum count crossing the multiplier threshold.
- Larger pulse counts and the negative eleven-cycle are outside this frozen packet.
- The result closes one explicit construction family; it is not a global no-cycle theorem.
- No counterexample is claimed.
