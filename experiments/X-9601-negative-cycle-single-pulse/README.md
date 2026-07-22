# X-9601 — Negative-cycle single-pulse search

**Status:** `EMPIRICAL` exact finite search  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Associated claim:** `L-9601`

## Question

Can a positive Collatz cycle be obtained by repeating one of the known negative accelerated cycles and increasing exactly one valuation enough to move the total multiplier into the positive-cycle regime?

`L-9601` reduces every pulse position, up to cyclic rotation, to a finite list of negative cycle states. If the primitive negative cycle has accelerated parameters `(k,A)` and rotated state `z<0`, a pulse of size `delta` in `r` repeated blocks has denominator

\[
D=2^{Ar+\delta}-3^{kr}
\]

and integrality requires

\[
D\mid(2^\delta-1)(3z+1).
\]

Every divisibility hit is then reconstructed and replayed valuation by valuation.

## Frozen scope

The experiment checks:

- the negative three-cycle word `(1,2)`, with states `-5,-7`;
- the negative eleven-cycle word `(1,1,1,2,1,1,4)`, with its seven odd rotated states;
- every repetition count `1 <= r <= 20,000`;
- the smallest pulse `delta` for which `D>0`, plus the next three pulse sizes;
- exact divisibility and exact accelerated replay for every hit.

This is `720,000` reduced candidates. Through cyclic rotation, each candidate represents every raw location of a single pulse in its repeated negative-cycle word.

## Result

The only hit is

```text
base word:   (1,2)
pulse:       first valuation +1
new word:    (2,2)
start:       1
```

which is the trivial Collatz cycle.

```text
nontrivial positive cycles: 0
```

Canonical semantic digest:

```text
cb97c4b0fcc5e2557b3e22ce83483d9e86f8ed4d825032925c90c4e0f6ee2ae8
```

Source SHA-256 used in the authoring replay:

```text
8cb2572826649c152ab5a72c85ce5a4c97c8e0b78f3179a387a6dc4ee3f4d425
```

## Replay

```bash
python3 -B experiments/X-9601-negative-cycle-single-pulse/run.py \
  --check-results \
  experiments/X-9601-negative-cycle-single-pulse/results/canonical.json
```

The script uses Python integers only. No floating-point threshold comparison is used.

## Boundary

- This excludes one pulse, not several distributed pulses.
- It excludes only the two frozen negative-cycle block families.
- It is not a general no-cycle theorem.
- No divergent orbit or Collatz counterexample is claimed.
