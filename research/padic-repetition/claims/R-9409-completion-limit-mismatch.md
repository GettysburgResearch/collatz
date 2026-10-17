# R-9409 — Real and `2`-adic limits of one rational sequence cannot be identified

Claim ID: `R-9409`  
Title: Bounded positive real tails do not bound rational `2`-adic tail values  
Status: `PROPOSED REFUTATION / METHOD CLOSURE`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none  
Scope: cross-completion reasoning in the sparse and full binary survivor programs  
Related counterexample candidates: none

## Refuted inference

The following reasoning is invalid:

```text
one rational sequence of partial sums
 -> bounded positive limit in R
 + rational limit in Q_2
 -> the rational Q_2 value is archimedeanly bounded.   (1)
```

Convergence of the same rational sequence in two completions does not make the
two limits equal as rational numbers.

## Elementary counterexample

Put

```text
x_N=2^N/(1+2^N).                                      (2)
```

Then

```text
x_N ->1 in R,
x_N ->0 in Q_2.                                       (3)
```

Thus even two rational completion limits can differ.

## Application to the survivor tails

For a binary code, the rational partial sums

```text
sum_(k=0)^N epsilon_(n+k)(64/81)^k                  (4)
```

converge:

- in `R`, to a positive value in `[0,81/17]`;
- in `Q_2`, to the code tail used by `Phi`.

If the `Q_2` limit happens to be rational, it does not follow that its ordinary
real absolute value lies in `[0,81/17]`.

Therefore:

1. fixed reduced denominators of rational `Q_2` tails do not imply finitely many
   tail states;
2. unbounded zero gaps do not currently imply irrationality;
3. rationality does not currently imply eventual periodicity;
4. the ordinary M1 section is not currently proved trivial.

These were the first invalid inferences in the withdrawn `T-9418`--`T-9421`
chain.

## What remains valid

The local algebraic statements `L-9416` and `L-9417` remain valid:

```text
rational Q_2 tail
 -> later reduced denominators divide the initial denominator.              (5)
```

What is missing is ordinary numerator control for those same rational `Q_2`
values.

## Safe uses of a real bound

A real bound can be transferred to the `Q_2` value only after one has produced
one completion-independent rational expression, for example:

```text
- a finite sum;
- an eventually periodic geometric formula;
- a rational function identity already proved in Q;
- or a cross-multiplied ordinary integer relation carrying both places.
```

Merely sharing partial sums is insufficient.

## Dependency audit

This refutation is elementary. It does not affect the exact finite transfer
identities, Padé theorems, Väänänen–Wallisser reduction, demand-tree isometry,
or completion-height carry results.

## Suggested next attack

Any renewed denominator argument must add an independent numerator/height
bound. The natural interfaces are:

```text
- the ordinary integer tail orbit;
- PR #16's centered nearest-integer coordinate;
- a product-formula determinant built from multiple tails;
- or a state-dependent finite-trap normalization.
```
