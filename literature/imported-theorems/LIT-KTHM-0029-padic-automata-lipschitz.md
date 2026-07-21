# LIT-KTHM-0029 — `p`-adic automata and the Lipschitz boundary

**Type:** located external theorem with native corollaries.  
**Source:** Anashin, *Automata finiteness criterion in terms of van der Put series of automata functions* (2012).  
**Maps to:** Diagonal Foundry operator classes; regular/synchronous digit processors.

## External theorem boundary

A letter-to-letter transducer over a `p`-symbol alphabet, reading least-significant digits first, induces a `1`-Lipschitz map

```text
f: Z_p -> Z_p.
```

Conversely, compatible digit functions are precisely the `1`-Lipschitz maps in the standard `p`-adic automata model. Anashin further gives a finite-state criterion in terms of the reduced coefficients of the van der Put expansion.

The complete finite-state criterion is imported as a black box; its exact coefficient normalization must be copied from the source before implementation.

## Elementary causal refinement

For a binary map `E:Z_2->Z_2`:

- ordinary causality, where output bit `k` may depend on input bits `0,...,k`, is equivalent to compatibility modulo every `2^(k+1)` and gives `1`-Lipschitz continuity;
- strict causality, where output bit `k` depends only on bits below `k`, gives
  ```text
  |E(x)-E(y)|_2 <= (1/2)|x-y|_2.
  ```

The second statement is proved in `LIT-KTHM-0028`.

## Native research use

The Foundry search should record, for every operator family:

```text
causal / strictly causal
finite-state / infinite-state
van der Put coefficient description
memory growth
fixed-point prefix algorithm
observed rationality or nonrationality
```

This turns “feedback operator” into a graded mathematical object and makes finite-state negative results comparable with the regular-sanctuary and automaticity programs.

## Non-consequences

- A finite transducer may have an irrational or transcendental `2`-adic fixed point.
- A `1`-Lipschitz map need not have a unique fixed point.
- A strictly causal map has a unique fixed point only after composing with the isometric Collatz conjugacy as in `LIT-KTHM-0028`.
- No automata theorem converts a compatible `2`-adic point into an ordinary integer.