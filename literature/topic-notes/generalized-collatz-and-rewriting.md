# Generalized Collatz undecidability and exact rewrite systems

## Standard-map rewriting

Yolcu–Aaronson–Heule give a finite mixed binary–ternary string-rewriting system equivalent to standard Collatz termination and automate proofs for weakened systems. This is the most direct located literature connection to the repository's rewrite ambitions.

## Generalized-map undecidability

Conway's work and Kurtz–Simon concern parameterized generalized Collatz maps. The latter's `Π^0_2`-completeness result is a theorem about the generalized input problem, not the single ordinary map.

## Connection to collision fibers

A collision chart already behaves like a partial radix rewrite:

```text
M B + d  ->  N B + d.
```

A future interoperability theorem could compile such a macro-step into a bounded derivation in the AYH rule system. Benefits would include:

- one canonical rewrite semantics for independent constructions;
- access to termination/nontermination certificate tooling;
- precise comparison of carry conventions;
- machine-checkable replay of finite macro-tiles.

## Safety boundary

A finite rewrite cycle in an abstraction is not automatically a positive-integer Collatz cycle. The compiler would need soundness, completeness on its domain, integrality, positivity, and preservation of infinite consistency.
