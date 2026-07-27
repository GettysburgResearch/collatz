```text
Claim ID:            T-6230
Title:               A forward-invariant sanctuary is a counterexample plus regularity; its
                     minimum is exactly the T-6170 object
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        T-6170, M-6120; the verification bound B (an INPUT)
Scope:               the shortcut Collatz map
Serves:              issue #10 (synthesize a regular forward-invariant sanctuary)
Experiment:          experiments/X-6230-sanctuary/
```

## Statement

Call `S` a **sanctuary** if `S` is a nonempty set of positive integers with `T(S) ⊆ S` and
`1 ∉ S`. Then:

**(a)** Every element of `S` is a counterexample: no orbit starting in `S` ever reaches 1. With
the verification bound `B`, `S` is disjoint from `[1, B)`.

**(b)** `m = min S` satisfies `T^j(m) >= m` for every `j >= 0`. So `m` lies in the set
`NS = {n >= 2 : T^j(n) >= n for all j}` whose triviality **is** the Collatz conjecture
(T-6170).

**(c)** Hence a sanctuary exists **only if** Collatz is false, and issue #10 — which asks for a
*regular* sanctuary — is **strictly stronger** than falsity: it asks for a counterexample plus
a structural property.

**(d)** No nonempty union of residue classes is a sanctuary, and more generally no set
containing a full residue class modulo anything, nor any set with a member below `B`.

## Proof

**(a)** `T(S) ⊆ S` gives `T^j(S) ⊆ S` for all `j`, and `1 ∉ S`, so no orbit from `S` meets 1.
Every `n < B` reaches 1 by hypothesis on `B`, so `S ∩ [1,B) = ∅`. `QED`

**(b)** `m ∈ S` and `T(S) ⊆ S` give `T^j(m) ∈ S` for all `j`, and every element of `S` is
`>= min S = m`. `QED`

**(c)** By (b) and T-6170: `NS = {1}` iff Collatz holds, and `m ∈ NS` with `m >= 2`. `QED`

**(d)** Any residue class `{n = r (mod M)}` contains integers below `B`, which reach 1 by (a)'s
hypothesis, so the class is not contained in any sanctuary. Verified explicitly for every class
and every modulus `M = 2..64` by exhibiting a small member and running it to 1
(`sanctuary.py`). The same argument applies to any set with an element below `B`. `QED`

## Why record this

Issue #10 is one of the repository's open positive-lane targets and, like the chart
architectures, it is **strictly harder than the thing it is trying to establish**. (b) makes
that precise in the sharpest available way: the sanctuary's minimum is not merely *a*
counterexample, it is exactly the object `s_L` whose boundedness T-6170 shows to be equivalent
to the whole conjecture. Regularity is then an *additional* demand on top.

This is the same verdict M-6120 reaches for fixed charts, arrived at independently, and it
means issue #10 inherits the same gate: state what the regularity buys, because the target it
is aimed at is smaller than the conjecture's negation, not larger.

## Gap audit

* (a) and (d) depend on the verification bound `B` being an input; nothing else does.
* **This does not show a sanctuary cannot exist.** If Collatz is false, a sanctuary may well
  exist — e.g. the forward orbit closure of a counterexample is trivially forward-invariant and
  avoids 1. What is shown is that constructing one cannot be *easier* than exhibiting a
  counterexample, since it entails one.
* Regularity plays no role in (a)-(d): they constrain every sanctuary, regular or not. The
  claim therefore does not address whether the *regular* ones are rarer — only that they are a
  subset of an already-strictly-harder target.
* The "orbit closure of a counterexample" remark shows the converse of (c) is nearly trivial,
  so (c) is an equivalence in spirit: sanctuaries exist iff Collatz is false.

## Suggested next attack

If issue #10 is to continue, the honest form of the question is not "does a sanctuary exist"
(equivalent to falsity) but "**is there a regular set that could be a sanctuary if any set
is**" — i.e. does the forward-orbit closure of a hypothetical counterexample admit a regular
over-approximation that still excludes 1? That is a question about automatic sets and the
2-recognizability of the relation `{(n, T(n))}`, which is decidable in principle by
Büchi-Bruyère; making it effective for small automata would be a genuine contribution and is
not addressed here.
