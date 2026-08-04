# Topic note — centered rational-power orbits at `81/64`

## Exact target

PR #16 `T-9315` reduces the nontrivial ordinary section to

```text
||xi*(81/64)^n|| <= 1/81 for every n.                (1)
```

This is containment in two centered arcs, not one ordinary interval.

## Literature tests in order

1. Evaluate Dubickas's explicit 2006 large-limit constant at `(81,64)`.
2. Translate the two arcs into the general interval language of Dubickas 2008.
3. If neither theorem closes `(1)`, inspect their Thue--Morse/sign-word proofs and splice in the exact carry restrictions from `LIT-KTHM-0041`.

## Native finite graph

The centered errors satisfy

```text
81*u_n-64*u_(n+1) in {-1,0,1}.
```

Build all sign/carry interval transitions. Iterate exact rational interval images and remove empty states.

Possible outputs:

- finite extinction: ordinary section empty;
- one finite critical graph: exact remaining symbolic language;
- an interval cycle: explicit extremal obstruction to a generic range theorem.

## Nonapplications

- FLP's ordinary range width does not by itself exclude a wrapped two-arc set.
- Almost-everywhere distribution says nothing about one `xi`.
- Finite-depth survivor growth does not imply an infinite orbit.