# Completion-limit separation in PR #20

## The correction

PR #20 briefly used one sequence of rational partial sums in both the real and `2`-adic completions, then treated the two limits as the same rational number. The branch has now withdrawn the affected theorem chain.

A simple control is

```text
x_N=2^N/(1+2^N).
```

It tends to `1` over the reals and to `0` in `Q_2`.

## Valid residue

The exact `2`-adic tail recurrence still proves:

```text
rational Q_2 tail
 -> later reduced denominators divide one fixed odd denominator.
```

It does not bound the ordinary numerators and therefore does not produce a finite rational state set.

## Safe restart

A corrected rationality theorem needs one additional ordinary-height coordinate, such as:

- the ordinary tail state under an ordinary-survivor hypothesis;
- PR #16's nearest-integer blocks;
- a transformed finite-trap height;
- or a rational Padé pair estimated at all places by the product formula.

A real analytic companion may bound Padé coefficients. It must not be identified with the finite-place target without a separate rational identity.

## Integration request

The atomic withdrawal files are clear. The PR body, `LATEST.md`, claim ledger, and project crosswalk should also state:

```text
proof withdrawn;
statement open;
first invalid inference identified;
earlier periodic results unaffected.
```
