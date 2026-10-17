# Topic note — sections, purification, and min-plus survivor recurrences

Three PR #34 packets fit one pipeline.

## 1. Exact finite-state boundary

For every 2-adic isometry, compute its rooted-tree sections. A finite section set is equivalent to a finite synchronous Mealy realization; the section machine is minimal. Van der Put coefficients provide a second exact test.

Apply this to:

- padding/correction maps;
- survivor lift digits;
- translated-fiber carry maps;
- Foundry feedback maps.

## 2. Static deterministic selection

The fractional Hall theorem gives a randomized kernel respecting finite residue capacities. If the decoder measure is atomless, Dvoretzky--Wald--Wolfowitz purification produces a deterministic measurable static selector with the same finite aggregate loads.

This does not give temporal or cross-modulus coherence.

## 3. Min-plus order statistics

PR #34's 64-bucket theorem says the next survivor minimum and successor depend on bucket-local heads and tails. If the bucket/carry map has finitely many sections, attach min-plus weights to the canonical section machine:

```text
state  = residual section,
input  = new digit,
output = lift bucket,
weight = lower representative.
```

A stationary finite machine would yield tropical matrix recurrences and cycle-mean growth bounds for the exact minima. An infinite section orbit identifies the missing unbounded state.

## Decision tree

```text
finite sections?
  yes -> exact finite transducer -> min-plus asymptotics;
  no  -> first new section becomes the next state coordinate.

atomless decoder?
  yes -> static purification;
  no  -> record the atomic obstruction exactly.
```

The remaining ordinary-integer problem is dynamic and pointwise even after both static steps succeed.