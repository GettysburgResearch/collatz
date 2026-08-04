# X-9510 — intrinsic renewal-height audit

**Status:** `INTERNAL EXACT COMPUTATION`; finite only.

This experiment audits the one-integer renewal decoder of `L-9529` and the
exact predecessor test of `L-9530`.

For every

```text
1 <= a,R,b <= 18,
0 <= k <= 127,
```

it constructs the canonical renewal state of type `(a,R,b)` and counter `k`,
then checks:

1. the intrinsic integer `Z` recovers the same type and bridge cores;
2. one forward step followed by the predecessor formula returns the original
   `Z`;
3. the intrinsic next-renewal test agrees with the renewal-counter decoder of
   `ITERATION_11`;
4. bounded replay contains no positive renewal cycle.

Frozen totals:

```text
states:                              746496
intrinsic step checks:               746496
inverse round trips:                 746496
defined next renewals:                35551
states with no predecessor:          699847
states with expanding predecessor:       24
maximum exact renewal life:               5
```

The longest tested path begins at

```text
(a,R,b,k) = (11,1,16,121)
Z         = 4423817593825817031
```

and exits after five renewals.  It is a rejected finite candidate, not a
counterexample.

## Reproduction

```bash
python3 run.py --output results/canonical.json
```

Standard library only.

Semantic digest embedded in the result:

```text
2934e2bbe9fb0291581f22fe6495774eab3db1c88907d96632d2d49ff7134af2
```

Canonical JSON SHA-256:

```text
8ea3beb09b306044cc15dfbd23e91df41f61427fe4a77d4d20f4662a8b50e830
```

## Scope boundary

This is an exact finite cross-check of two equivalent coordinate systems.  It
does not show that every positive integer exits, and it does not exhibit an
integer whose intrinsic decoder is defined forever.
