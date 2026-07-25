# X-7301 — Exact two-point descent classification

This experiment proves the finite arithmetic classification used by
`L-7301/T-7301`.

For every type triple `(i,j,k)`, it solves

```text
u*a_i + v*a_j = a_k,
0 < u*Q + v*P < Q,
```

where

```text
P=3^12,
Q=2^19,
a_i=7*2^(15-3i)*3^(2i).
```

The second inequality is exactly

```text
0 < u + v*(P/Q) < 1.
```

## Independent implementations

- `run.py` parametrizes each linear Diophantine equation by Bézout
  coefficients and intersects its parameter with the exact contraction interval.
- `verify.py` does not import `run.py`. It eliminates `u`, obtains the direct
  interval

  ```text
  0 < a_k*Q + v*(P*a_i-Q*a_j) < Q*a_i,
  ```

  enumerates the integers `v` in that interval, and reconstructs `u` by exact
  divisibility.

## Frozen result

```text
contracting forms:              75
diagonal constant-type family: 73
adjacent-ascent forms:           2
other forms:                     0
```

The diagonal family is

```text
(u,v)=(t+1,-t), 1<=t<=73.
```

The exceptional forms are

```text
(-8,8): i->i+1 with output i,
(-9,9): i->i+1 with output i+1.
```

The complete continued-fraction ladder for `P/Q` is also checked. Only the
`74/73` upper convergent has allowed hits, all diagonal.

Semantic digest:

```text
2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f
```

## Replay

```bash
python3 -B experiments/X-7301-two-point-descent/run.py \
  > /tmp/X-7301.json

python3 - <<'PY'
import json
with open('/tmp/X-7301.json', encoding='utf-8') as generated:
    left = json.load(generated)
with open(
    'experiments/X-7301-two-point-descent/results/canonical.json',
    encoding='utf-8',
) as frozen:
    right = json.load(frozen)
assert left == right
print('frozen X-7301 payload check passed')
PY

python3 -B experiments/X-7301-two-point-descent/verify.py \
  experiments/X-7301-two-point-descent/results/canonical.json
```

The experiment does not claim boundedness or divergence of the least roots and
does not produce a counterexample.
