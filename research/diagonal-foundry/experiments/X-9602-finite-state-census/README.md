# X-9602 — Exhaustive finite-state feedback census

```text
Experiment ID:   X-9602
Agent:           fable-01
Issue:           #21
Claims:          consistency evidence for T-9603 (finite-state feedback
                 collapse); supplies O-9603
```

## Research question

Enumerate ALL strictly causal finite-state operators with |S| ≤ 3 (17,626
machines: 2 one-state, 128 two-state, 17,496 three-state, over all initial
states) and determine every integral foundry solution. T-9603 predicts each
hit enters an integer cycle of parity period ≤ |S| ≤ 3 — i.e. only
{0}, {1,2}, {−1}, {−5,−7,−10} — and that every positive hit is subcritical,
hence reaches the trivial cycle.

## Exact code / command

- Code: `census.py` (dependency-free).
- Command: `python3 census.py` (default K = 256; ~4 min single-threaded).
- Hit detection: terminal constant digit run ≥ 48 (false-positive odds
  ≤ 2^−48 per machine); every hit fully re-verified: rebuild at K = 512,
  independent closure-equation replay from the integer (separate code
  path), orbit-cycle classification by direct iteration. Any unexpected
  cycle raises and aborts the census.
- Deterministic; no randomness, no floats.

## Output

`results/census.log` (committed). Headline: 13,650 of 17,626 machines have
integral solutions, realizing exactly 15 distinct integers:

```text
0, 1, -1, 2, -2, -3, 4, -4, 5, -5, -7, 10, -10, -14, 20
positive hits {1, 2, 4, 5, 10, 20} — all reach the trivial cycle
negative hits — all reach -1 or the -5 cycle
```

## Interpretation

- 100% consistent with T-9603: no hit escapes the parity-period ≤ 3 cycle
  inventory; no positive hit avoids the trivial cycle; no divergent-type
  hit (aperiodic digit tail) exists — as proved.
- The preperiodic positive entries (4, 5, 10, 20) show prefix-steering in
  action: the feedback prefix walks the integer down a T-chain into the
  trivial cycle; the machine inventory records exactly how much steering
  ≤ 3 states buys.
- The overwhelming mass of hits at 0 and −1 (5,395 machines each) is the
  locking phenomenon of O-9602 in exhaustive form.

## Limitations

- |S| ≤ 3 only; the census is a consistency check and an inventory, not a
  proof (T-9603 is the proof, for every |S|).
- K = 256 build window with ≥ 48-run detection: a machine whose solution
  is an integer larger than ~2^208 would be missed — irrelevant for
  |S| ≤ 3 (T-9603 bounds the reachable cycles), noted for completeness.
