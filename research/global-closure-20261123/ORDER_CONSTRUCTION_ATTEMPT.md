# Global order construction: where the ordinal route must change

**23 November 2026. Status: attempted full termination construction.**
The unrestricted Collatz theorem remains OPEN. This note records a fourth
attack, alongside the actual collision, full-denominator cycle, and triadic
duality lanes. No capped census was extended.

## 1. The starting point is the complete system

The literal Aaronson–Yolcu–Heule system, in the authors' ASCII notation, is

```text
ad -> d      bd -> gd
ae -> ea     af -> eb     ag -> fa
be -> fb     bf -> ga     bg -> gb
ce -> cb     cf -> caa    cg -> cab.
```

Source: [authors' rules at 8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340](https://github.com/emreyolcu/rewriting-collatz/blob/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340/rules/collatz-T.srs).
The mixed-base simulation and its termination/convergence equivalence are
the authors' results, not a result of this checkpoint. Their paper is
[An Automated Approach to the Collatz Conjecture](https://doi.org/10.1007/s10817-022-09658-8).

The older repository continuation at
[PR141, 5025ef464d4b6d4f4a412a3e33c3477de68dfa8b](https://github.com/GettysburgResearch/collatz/blob/5025ef464d4b6d4f4a412a3e33c3477de68dfa8b/research/ay-persistent-20261031/PROOF.md)
has two different orders: a semantic order while odd-state popcount stays
within a fixed cap, and an original-source order for a supplied successful
descent macro. Neither pays for an arbitrary cap increase or constructs a
successful macro for every source. The finite certificates were inspected
through their statements; they were not replayed.

The attempted extension was a genuinely nonlocal ordinal interpretation,
motivated by Goodstein and hydra termination. The relevant literature does
permit interpretations stronger than natural-number polynomials:
Zankl, Winkler and Middeldorp,
[Automating Ordinal Interpretations](https://www.inf.unibz.it/~sarwinkler/papers/ZWM12.pdf),
especially the distinction between strictly monotone algebras and weakly
monotone *simple* algebras. No theorem from that paper says that the Collatz
system admits such an interpretation.

## 2. An exact constraint before an ordinal search

Here is a short reconstructed observation, with no novelty claim.

Let L be a nonempty well-ordered carrier, and interpret every letter by
a strictly increasing endomap of L. Interpret a string by composition
from left to right in the usual term-interpretation convention:
`[uv](x)=[u]([v](x))`. Even the two requirements

```text
[b]([d](x)) > [g]([d](x))               for every x,
[c]([g](x)) >= [c]([a]([b](x)))        for every x
```

cannot both hold. These are strict orientation of bd -> gd and weak
orientation of cg -> cab.

First, a strictly increasing self-map a of a well-order is inflationary:
a(y)>=y. For if a(y)<y at a least counterexample y, then at z=a(y)<y
we have a(z)>=z=a(y), while strict increase gives a(z)<a(y), a
contradiction. Second, strict increase of c on a total order reflects
order. The second displayed condition therefore gives

```text
g(y) >= a(b(y)) >= b(y)
```

for every y. Set y=d(x), contradicting the first condition.

This observation covers every ordinal height in that **direct strictly
monotone, single-carrier class**, not just a finite degree or a bounded
matrix dimension. It does not cover arbitrary well-founded partial
orders, weak/extended algebras with a separate weak relation, relative
top-termination, marked semantic states, or a different encoding.

For weakly monotone *simple* interpretations on a total well-order,
strict orientation of both displayed rules is also impossible: simplicity
gives a(b(y))>=b(y), while strict c(g(y))>c(a(b(y))) and weak monotonicity
force g(y)>a(b(y)). This already conflicts with bd -> gd.
Here simplicity means that each unary interpretation is at least its
argument; no stronger interpretation of the word “simple” is used.

This is not evidence against termination. The two-rule subsystem itself
terminates. Each occurrence of c can use cg -> cab at most once, because
it acquires a permanent right neighbor a and neither rule removes a.
The other rule consumes one b and the first rule creates one b. Thus
there are at most #c initial uses of cg -> cab and at most #b+#c
uses of bd -> gd. A restrictive proof format can fail for a terminating
subsystem.

## 3. Retaining the original integer is essential

A hereditary-base analogy must provide a rule-by-rule interpretation;
base replacement alone is insufficient. On an ordinary shortcut orbit
n_k=T^k(n), with p_k odd steps, the exact affine ledger is

```text
2^k n_k = 3^p_k n + C_k,       C_k >= 0.
```

Every carry normalization preserves the represented ordinary value.
Consequently a state annotation that “pays” for an odd step must also pay
for the normalization which creates the next binary word. Resetting an
ordinal from the newly enlarged binary expansion is not a decrease
argument. No such unconditionally paid annotation was constructed here.

This is why the useful new rank in the parallel
[triadic-duality lane](duality/TRIADIC_RANK.md) lives on **paired arithmetic
states**, not on a strictly monotone interpretation of the seven letters.
Its first coordinate is the actual remaining power of three in a supplied
complementary rational trajectory. The rank supplies the termination
implication once that arithmetic object exists; existence for every
ordinary source is the outstanding construction.

The two approaches are therefore not interchangeable: a failed direct
ordinal interpretation does not obstruct a source-dependent arithmetic
rank. Conversely, the rank cannot be attached to every original source
without constructing its triadic complementary trajectory.

## 4. Evidence and remaining target

The rule file, the cited order frameworks, and PR141's proof were read.
The two-rule reasoning above is a written reconstruction; no new
termination search, hydra simulation, formal ordinal build, or full Collatz
result is claimed.

The remaining target is constructive and global: assign to every positive
ordinary source an arithmetic or marked-state annotation whose update is
defined for the entire actual trajectory and decreases in a well-founded
order. The triadic lane provides a concrete sufficient annotation and
identifies its missing existence statement. Raising a popcount cap or
choosing a larger ordinal without the corresponding update proof does
not supply it.
