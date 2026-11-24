# Verification and remaining gap

**Status:** proposed mathematical derivations; no proof of Collatz.

## Executed bounded controls

The exact JavaScript BigInt program `controls.js` ran in the connector execution environment and returned:

```json
{"inverseChecks":6667,"stripChecks":11000,"recurrenceChecks":85795,"injectivityChecks":11000,"rationalGridChecks":2884,"actualLargeRows":320}
```

The last group uses 256-bit inputs, exact shortcut inverse clocks, and literal forward checks back to the unchanged input. These are finite controls of the arithmetic, not verification of the limiting distribution, density inputs, or phase-gap theorem. Replay locally with `node controls.js`.

## Lean

The environment used for this checkpoint did not expose `lean` or `lake` on PATH. `ARITHMETIC.lean` is an uncompiled candidate; all eight axiom queries await a real kernel run. No successful build, independent agent review, complete-checkout validator, or external formalization replay is claimed. The written arguments do not depend on the candidate compiling. In particular the external mathematical statements M, R, and N are isolated in README, not introduced as Lean axioms. The prior PR196 audit is separate historical evidence.

## Reconstruction checklist

1. The inverse strip has exactly the right width: 2(k-1) consecutive integer surplus values. Successive positive inverse exponents differ by two; the recurrence shifts the octave by exactly two. Injectivity on the strip uses the exact odd target, not the starting residue.
2. The continued-fraction denominator is chosen before the target q is sampled. The one-sided rational grid has a margin on both sides of the error. The upper bound on Q uses the previous convergent's phase gap, not the next denominator. For sigma*kappa<1 this cost is sublinear in log X.
3. Every selected ancestor is attached to the original b through an actual q. No sampled replacement of b, path-specific uniformity, or independence is used. The number of possible q for one n is bounded by one forward segment of length 4Q after the first accelerated odd edge, even though the extra critical edge can have a much larger e.
4. The density-zero set J contains every fixed-k critical section outside a finite cutoff. Its exponent lower bound takes k fixed first, then lets k grow in the exponent bound; it never assumes target-density estimates uniform in k.
5. The first-passage comparison counts missing roots separately; the parent has at most 81 preimages. Both defined roots are actual states of the original pair. First-passage marginal concentration is not sufficient for a coupling. The sum is over every level, not a favorable subsequence.
6. The entropy calculation concerns the actual trajectory minimum, not an assumed invariant measure. It requires the simultaneous-in-X-and-M barrier statement. It does not imply vanishing entropy.

## Next proof target

The two routes now require either a genuine power-saving bound for nonconvergent members of the explicit high-valuation section J, or summable joint mismatches of actual first-hit labels on the one-head truncation graph. The external fixed-barrier bound alone supplies neither. Existing source-independent merger coverage and local descent must not be counted as a proof of either assertion.
