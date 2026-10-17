# Integer-first offense — independent `80xx` packet

**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Branch:** `agent/gpt56-pulse-01/46-two-pulse-offense`

This packet is an independent constructive continuation of PR #47. It does
not modify the active `96xx` namespace.

The accepted positive endpoint remains one explicit ordinary positive integer
with either:

- a complete nontrivial accelerated-cycle replay; or
- an all-time proof that its shortcut-Collatz orbit avoids `1`.

The packet contains:

- `L-8001`: an exact two-pulse reduction around every repeated negative cycle,
  with two nonzero determinant eliminants and finite all-pulse caps at each
  repetition/gap;
- `T-8001`: an independent proposed exclusion of exactly five non-`2`
  valuations. Branch-qualified `PR34/L-9912` and `L-9913` now provide a
  stronger parallel frontier through six; this file is retained as an
  independent proof packet rather than presented as the current record;
- `O-8001`: exact one-pulse negative-cycle block charts;
- `L-8002`: the negative-three-cycle chart reduced to maximal run labels and
  one ordinary quotient, with a changing-modulus refund law;
- `T-8002`: a forever-defined ordinary macro path with every run at least five
  is automatically a positive unbounded shortcut-Collatz orbit;
- `T-8003`: the exact relaxed growth theorem: cumulative run surplus
  `9 sum(r_j)-44N -> +infinity` is enough, and the finite-window rule “every
  nine runs total at least 44” already forces divergence;
- `L-8003`: a closed ordinary reset family with unbounded certified finite
  depth and an exact Hensel re-entry criterion;
- `L-8004`: the invariant divisible-seven subchart, whose run-core equation is
  `2^(4+3s)v^+ = 9^(r+1)v+1`;
- `L-8005`: an exact base-nine `2`-adic logarithmic renormalization of that
  subchart, turning a high next run into one fixed-depth Hensel ball;
- `X-8001`: all-size two-pulse scans plus long near-threshold scans;
- `X-8002`: near-threshold three- and four-pulse scans;
- `X-8003`: independently verified finite tables completing `T-8001`;
- `X-8004`: the first six-defect scout; and
- `X-8005`: exact run-core, quotient-cylinder, reset-family, and first-Hensel
  audits with an independent checker.

## Strongest live positive target

For the negative-three-cycle chart, one section state has the exact form

```text
z = 2^(3r) u,
physical n = 6z-5.
```

The deterministic macro sends

```text
z -> (9^(r+1) u + 7)/16.
```

`L-8002` compiles each ordered run pair to one ordinary quotient. The remaining
obligation is pure ordinary existence/top-boundary closure. Growth is already
available under either of two exact finite certificates:

```text
pointwise highway:
  every emitted run r >= 5;

relaxed nine-run highway:
  every consecutive certified block of nine runs has total >= 44.
```

The second condition follows from the exact inequality `9^53>2^168` and is
strictly less restrictive. `L-8005` additionally shows that, in the
`7|z` subchart, a run at least five is the fixed logarithmic congruence

```text
alpha == -r-1 mod 2^16,
alpha = log_9(-v).
```

Thus the next constructive search should combine the changing-modulus ordinary
quotient with a finite nine-run resource counter or a finite union of
logarithmic Hensel balls. No separate physical replay, positivity, or drift
proof would remain after all-time definedness is established.

No `K-80xx` object is assigned. Every hit in the frozen cycle searches is the
trivial `n=1` all-`2` cycle.