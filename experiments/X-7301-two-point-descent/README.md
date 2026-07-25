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
- `verify.py` does not import `run.py`.  It eliminates `u`, obtains the direct
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

The complete continued-fraction ladder for `P/Q` is also checked.  Only the
`74/73` upper convergent has allowed hits, all diagonal.

Semantic digest:

```text
2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f
```

Source hashes at publication:

```text
run.py
776fc451dc28eeb0e0b88ae260abc7443bd919bf9520a6337ee7f5ff5e646d48

verify.py
f5ae3bdb7b28d8da177829532275bf4fb0a1ad9d72f75a65435e39ab8ead4333

canonical.json
6cee769c0997d72a1d09dd70dcabbabfba905eda2b24e9626da197b92a2e3219
```

## Replay

```bash
python3 -B experiments/X-7301-two-point-descent/run.py \
  > /tmp/X-7301.json

diff -u \
  experiments/X-7301-two-point-descent/results/canonical.json \
  /tmp/X-7301.json

python3 -B experiments/X-7301-two-point-descent/verify.py \
  experiments/X-7301-two-point-descent/results/canonical.json
```

The experiment does not claim boundedness or divergence of the least roots and
does not produce a counterexample.
