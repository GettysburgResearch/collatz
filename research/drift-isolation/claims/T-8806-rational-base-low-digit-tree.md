# T-8806 — Rational-base low-digit-tree equivalence

Claim ID: T-8806  
Title: Positive `4 -> 5` chart survivors are exactly low-digit bottom paths in the base-`5/4` representation tree  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8802  
Scope: positive ordinary integers under the exact two-step `5x+1` chart  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let `A>0`, and put

```text
M=A+2,
X=A+1=M-1.
```

While `A` lies in a chart phase `A mod 4 in {2,3}`, write

```text
eps = M mod 4 in {0,1},
delta = 1-eps in {0,1}.
```

Then one chart macro-step satisfies the exact conjugacies

```text
M' = floor(5M/4),                                      (1)
4X' = 5X+delta.                                        (2)
```

Define the base-`5/4` representation tree on nonnegative integers by an edge

```text
x --r--> y    iff    4y=5x+r,    r in {0,1,2,3,4}.     (3)
```

At every node `x>0`, the smallest admissible edge label is

```text
b(x)=(-x) mod 4 in {0,1,2,3},                          (4)
```

and its endpoint is

```text
tau(x)=ceil(5x/4).                                     (5)
```

This smallest-label edge is the bottom edge at `x`.

The following are equivalent:

1. `A` remains in the exact `4 -> 5` chart forever.
2. The bottom orbit

   ```text
   X, tau(X), tau^2(X), ...
   ```

   uses only labels `0` and `1`.
3. The base-`5/4` bottom word from root `X=A+1` belongs to `{0,1}^N`.

Under this equivalence, the tree label is `delta_j=1-eps_j`. Any such positive
survivor is strictly increasing and therefore diverges to infinity.

## Definitions

- Equation (3) is taken here as a self-contained definition; no external
  rational-base theorem is a dependency.
- The **bottom edge** is the admissible edge with least digit label.
- The **bottom word** is the infinite sequence of bottom-edge labels.

## Motivation

The original completion formula is naturally `2`-adic. This theorem reveals a
second, completely discrete face: the same survivor question is a forbidden-
digit problem in a rational-base representation tree. The target is now exact
and falsifiable:

> Does any root `X>=2` have a base-`5/4` bottom word using only digits `0,1`?

A positive answer gives a concrete divergent `5x+1` control orbit. A negative
answer gives a full certificate-format no-go theorem for this chart.

## Proof or construction

### Shift by two

For phase `A=4q-2`, T-8802 gives `A'=5q-2`. Thus

```text
M=4q,
M'=5q=floor(5M/4).
```

For phase `A=4q-1`, T-8802 gives `A'=5q-1`. Thus

```text
M=4q+1,
M'=5q+1=floor(5M/4).
```

This proves (1). Since `X=M-1`,

```text
4X' = 4(M'-1)
     = 5M-eps-4
     = 5X + (1-eps),
```

which is (2).

### Bottom digit

An edge from `x` must have `r congruent -5x congruent -x (mod 4)`. Among
`r in {0,1,2,3,4}`, the least such digit is the representative in
`{0,1,2,3}`, namely (4). Substituting it into (3) gives the least endpoint,
which is exactly `ceil(5x/4)`.

The bottom digit belongs to `{0,1}` exactly when

```text
x mod 4 in {0,3}.
```

Since `x=A+1`, this is exactly

```text
A mod 4 in {3,2},
```

the two chart phases. Equation (2) shows that the chart successor is precisely
the bottom child and that its label is `delta=1-eps`. Iterating proves the three
conditions equivalent.

Finally, for every `x>0`,

```text
ceil(5x/4)>x.
```

Hence every infinite low-digit bottom path is strictly increasing; translating
back by `A=X-1` proves divergence. **QED**

## Dependency audit

- T-8802 supplies the two exact physical macro branches.
- Everything about the rational-base tree is derived from equation (3) inside
  this file.
- External literature is relevant context but not a proof dependency.

## Gap audit

- The theorem is an equivalence, not an existence result.
- A long finite low-digit prefix does not imply an infinite path from the same
  root.
- The representation tree has a bottom path from every root, but most bottom
  paths use digits `2` or `3` and therefore leave the chart.
- Strict growth follows only after infinite chart survival has been proved.

## Adversarial tests

X-8802 checks equation (2), the bottom digit, the child, and the physical
`T_5^2` replay at every surviving step for all `1<=A<=10^6`. The longest finite
prefix in that range has length `19`; this is evidence about the bounded search
only.

## Remaining uncertainty

Existence of a root `X>=2` whose entire bottom word lies in `{0,1}` remains open.

## Suggested next attack

Use the known successor transducer and subtree machinery for rational-base
numeration as an external toolbox, but re-prove every load-bearing statement in
this exact low-digit setting. High-upside targets are:

1. an automaton or PDR invariant forcing a digit `2` or `3`;
2. a self-similar subtree that preserves digits `{0,1}`;
3. a Diophantine theorem excluding ordinary roots from the `2`-adic survivor
   Cantor set of T-8807.
