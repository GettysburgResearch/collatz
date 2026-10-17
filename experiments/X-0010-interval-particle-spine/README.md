# X-0010 — Finite intervals, critical particles, and ordinary spines

Experiment ID: `X-0010`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0014`, `T-0018`, and `T-0019`

## Research questions

1. Can every ordinary shortcut-Collatz step be represented as the renormalization of one finite integer interval?
2. Do the shifted phase branches admit an exact local two-child particle rewrite?
3. Is the phase-escape Doob transform exactly the branch law of a uniform descendant?
4. Can the ordinary-integer condition be isolated as a distinguished finite boundary marker?
5. What are the exact likelihood ratios among fair parity, Collatz growth tilt, phase escape, and the marked ordinary spine?

## Method

`run.py` uses exact Python integers and rational arithmetic only. It:

- verifies the finite interval lift for
  
  ```text
  1 <= n <= 500
  1 <= v <= 500;
  ```
- checks the fixed and diagonal gauges for 2,000 starting integers over 50 shortcut steps;
- verifies the ordered particle child partitions for populations through 5,000;
- checks
  
  \[
  \sum_{|w|=L}R_w(x)=2^Lx
  \]
  
  through depth 10;
- verifies the distinguished ordinary Collatz spine for 1,000 starting particles over 100 steps;
- checks the exact escape/growth likelihood products on 500 ordinary trajectories;
- checks the marked-descendant mass identities.

## Command

```bash
python3 -m py_compile experiments/X-0010-interval-particle-spine/run.py
python3 experiments/X-0010-interval-particle-spine/run.py
```

## Expected output

```text
verified finite interval lift and fixed/diagonal gauges
verified ordered particle split and 2^L mass conservation
verified distinguished ordinary Collatz spines
verified escape/growth likelihood and marked-spine identities
all interval-particle-spine checks passed
```

The checked-in copy is `results/summary.txt`.

## Interpretation

The experiment confirms a two-layer rewrite framework.

### Unmarked layer

A population of size \(x\) splits into branch populations

\[
R_0(x)=\lfloor x/2\rfloor,
\qquad
R_1(x)=\lceil3x/2\rceil,
\]

with total size \(2x\). Uniform descendants generate the phase-escape measure.

### Marked layer

One finite particle is marked. The distinguished child has rank \(T(j)\), so preserving this marker is exactly preserving one ordinary Collatz trajectory.

This exposes why an escaping unmarked phase language is not yet a counterexample: the ordinary boundary is an additional marked-spine condition.

## Limitations

- The experiment verifies finite identities only.
- It does not construct an unbounded marked spine.
- The auxiliary particle tree contains descendants that are not ordinary Collatz children of their parent labels.
- Positive escape or tilted pressure does not imply that a marked ordinary lineage is accepted forever.
