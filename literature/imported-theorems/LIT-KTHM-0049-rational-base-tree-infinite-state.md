# LIT-KTHM-0049 — Rational-base integer trees have genuinely unbounded exact state

**Type:** imported theorem package with a native automata boundary.  
**Source:** Akiyama–Marsault–Sakarovitch, *On subtrees of the representation tree in rational base numeration systems* (2018).  
**Maps to:** issue #40, PR #12, PR #14, PR #35, PR #3 collision charts, and the integer-first regeneration program.

## External results

For coprime integers `p>q>1`, the canonical rational-base representations of nonnegative integers form a prefix-closed rooted tree. The source proves, among other statements:

1. every integer has a unique finite representation, up to leading zeroes;
2. the representation language is highly nonregular;
3. the subtrees rooted at distinct integers are all distinct;
4. the bottom words rooted at distinct integers are all distinct and are not ultimately periodic;
5. the successor map sending the bottom word at `n` to the bottom word at `n+1` is realised by an infinite sequential letter-to-letter transducer whose underlying graph is essentially the representation tree itself; and
6. the closure of the normalized span set is an interval in one parameter range and a measure-zero Cantor set in the complementary range.

These statements are imported as black boxes.

## Native interpretation

A restricted-digit Collatz chart often has the exact shape

```text
integer node
 -> least allowed rational-base digit
 -> next integer node.                                  (1)
```

The source explains why a residue-only finite automaton is generally too small for `(1)`: the exact future language can distinguish every integer root. The missing carry or quotient is not implementation noise; it can be the mathematical state.

This applies directly to two current frontiers:

```text
PR35: base-5/4 bottom word avoiding forbidden digits;
issue #40: forced zero-block map on the unbounded terminal integer C_K.
```

A finite modular SCC may therefore be a projection of infinitely many inequivalent rooted subtrees. It is not an ordinary survivor certificate without a lift carrying the exact integer state or a proved quotient invariant.

## Positive use rather than only obstruction

The infinite-state result also supplies a constructive blueprint. The canonical exact machine is:

```text
state  = current integer/rooted subtree;
input  = current least-significant digit or allowed branch choice;
output = successor integer and next subtree.            (2)
```

A successful Collatz counterexample architecture can compress `(2)` only after proving that a smaller state is sufficient on one invariant subfamily. Suitable positive proof objects include:

- a finite nucleus plus one counter whose update is exact;
- a pushdown section system;
- a quotient-refund invariant keeping the high integer state alive;
- or an explicit self-replicating subtree with one positive root.

## Nonconsequences

The theorem does not imply that any prescribed restricted-digit subtree is empty or nonempty. In particular it does not prove:

- divergence of the `5x+1` control chart;
- existence of a centered `64 -> 81` ordinary survivor;
- existence of a regular Collatz sanctuary;
- existence of a collision-chart integer orbit;
- or the Collatz conjecture in either direction.

It says that finite-state failure is expected unless a new arithmetic quotient or invariant family is proved.

## Required repository discipline

A proposed finite abstraction of a rational-base-like chart should state:

```text
EXACT ROOT STATE:
ABSTRACT STATE:
LIFT RELATION:
WHY EQUAL ABSTRACT STATES HAVE EQUIVALENT FUTURES:
ORDINARY INITIAL ROOT:
```

Without the fourth line, a modular lasso is only a completion-level or finite-prefix object.