# Global-blocker follow-on: strictly causal foundry no-reduction theorem

**Agent:** `gpt56-global-01`  
**Date:** 2026-07-25  
**Issue:** #55  
**Draft PR:** #57  
**New claim:** `R-7601`  
**Counterexample status:** none

## Objective

This pass continued the user-requested global-blocker focus.  It did not add a finite-prefix search, amplifier, new encoding, or conditional growth theorem.

The target was the Diagonal Foundry proposal:

```text
strictly causal parity-from-digit feedback
 -> one unique computable 2-adic point
 -> hope that the point is an ordinary positive integer.
```

The question was whether strict causality genuinely reduces the ordinary-extraction problem or only repackages it.

## Result

`R-7601` proves four exact statements.

### 1. Unique point

Every strictly causal operator `E` has exactly one `alpha_E in Z_2` satisfying

```text
parity(alpha_E) = E(binary_digits(alpha_E)).
```

The proof is the finite parity-flip argument: after the first `k` binary digits have been fixed, the two lifts modulo `2^(k+1)` have opposite time-`k` parity, while strict causality has already fixed the required output bit.

### 2. Full surjectivity

The map

```text
E -> alpha_E
```

is surjective onto all of `Z_2`.  Given any `alpha`, prescribe `E` only on the successive binary prefixes of `alpha` so that its outputs equal the actual parity bits of `alpha`; define `E` arbitrarily off that one path.  The unique foundry point is then `alpha`.

There are continuum many such operators for each `alpha`.

### 3. Computable surjectivity

Computable strictly causal operators produce computable `2`-adic points, and every computable `2`-adic point is produced by a computable strictly causal operator.

Thus computability does not narrow the ordinary boundary.  It includes every ordinary integer and every computable completion ghost.

### 4. Tail-property preservation

Let `P` be any parity-word property that is invariant under finite modifications and contains the all-one word.  Then

```text
some strictly causal E has every output in P
and has a positive ordinary foundry point

iff

some positive ordinary integer already has actual parity word in P.
```

The reverse construction follows the desired integer's binary-prefix path and emits all ones after any deviation.

For the supercritical lower-one-density condition, this says:

```text
uniformly supercritical foundry with positive ordinary point

iff

positive integer with supercritical actual Collatz parity word.
```

The latter would already be an unbounded Collatz orbit by `T-7602`.

## Blunt conclusion

The unrestricted Diagonal Foundry is not a weaker route to ordinary extraction.

```text
strict causality
 -> uniqueness and exact computability;

operator design
 -> enough freedom to encode every 2-adic point;

ordinary integrality
 -> still exactly eventual-zero binary digits.
```

So the foundry does not remove the global blocker.  It moves it into the sentence “the unique point has finite binary support.”

A restricted operator class could still constitute real progress only if its syntax is accompanied by a proof of eventual-zero digits, bounded least roots, or universal nonstabilization.  Enumerating unrestricted feedback rules is not progress toward an ordinary seed.

## Relationship to the repository-wide verdict

This strengthens the architecture audit as follows.

- Prescribed high-drift words fail by `T-7602`.
- General compactness-plus-refund extraction fails by PR #56 `R-7801`.
- Unrestricted strictly causal foundries fail as a reduction by `R-7601`.
- The exact live positive target remains architecture-specific boundedness or divergence of canonical least roots, especially `Q-7601` for the six-branch chart.

No claim about the existence or nonexistence of a standard Collatz counterexample follows from `R-7601`.

## Files

1. `research/ordinary-extraction/claims/R-7601-strictly-causal-foundry-no-reduction.md`
2. updated `research/ordinary-extraction/README.md`
3. this append-only report

## Review targets

1. Reconstruct the parity-flip digit recursion independently.
2. Verify the off-path operator construction and strict causality.
3. Verify that finite-change invariance is exactly what is needed in the tail-property equivalence.
4. Keep the supercritical class distinct from all possible counterexample mechanisms.
5. Confirm that the theorem eliminates a proof architecture, not a Collatz subsystem.
