# A lower bound for affine steering inside one parity cell

The new universal result in `CollatzGlobalClosure/SiblingRigidity.lean` is a classification
constraint on ordinary affine mergers that preserve their supplied binary
prefix. A prefix with `p>0` odd inputs forces every nontrivial such merger to
pay at least

\[
                  2\,3^{p-1}
\]

additional shortcut clocks. Its affine expansion factor is consequently at
least `2^(2*3^(p-1))`. This is a result about every finite prefix satisfying
the hypotheses, not a finite search over examples. It does not prove Collatz
or a universal alternative steering construction.

## Exact hypotheses

Write `T` for the shortcut Collatz map, and take natural numbers
`k,a,n,c,t`. Let

\[
   p=\operatorname{odds}(k,n),\qquad x=2^a n+c.
\]

Assume `p>0`, `a>0`, and the following **ordinary trajectory facts**:

1. `x=2^k*t+n`, so `x` and `n` share the complete supplied binary parity
   prefix of length `k`.
2. `T^(k+a)(x)=T^k(n)`.
3. The first `k+a` steps of `x` have exactly `p` odd inputs.

These are the literal hypotheses of
`invariant_prefix_clock_lower_bound`. They are not inferred from endpoint
residues. A map on an entire cell `n=r mod2^h` that preserves that cell, has
`h>=k`, and has the two indicated actual merger words supplies these
hypotheses at every member of the cell. The translation `c` is nonnegative
in this formalized version.

Both sources are positive automatically when `p>0`; the file proves this
as `positive_sources_of_positive_odds`.

## Derivation

The exact ordinary affine formula is

\[
       2^k T^k(n)=3^p n+C,
\]

where `C=offset k n`. The file proves the formula directly from the actual
shortcut steps. It also proves that a genuine prefix with at least one odd
input has `3` not dividing `C`.

The shared binary prefix makes the first `k` steps of `x` have the same odd
count `p` and offset `C`. Assumption 3 therefore makes all its remaining
`a` steps even. Assumption 2 gives

\[
                         T^k(x)=2^a T^k(n).
\]

Substituting `x=2^a n+c` into the two affine equations yields the exact
identity

\[
                         3^p c+C=2^a C.
\]

The formal theorem is `invariant_prefix_identity`. Since `C` is a ternary
unit, it follows that

\[
                              3^p\mid 2^a-1.
\]

The file then proves the exact order implication using Mathlib's proved
odd-prime lifting-the-exponent theorem. First `a` is even. Writing `a=2b`,

\[
                    v_3(2^a-1)=v_3(4^b-1)=1+v_3(b).
\]

Thus `2*3^(p-1)` divides `a`, and positivity gives the claimed lower bound.
The final expansion corollary is

\[
                  2^{2\,3^{p-1}}n\le 2^a n+c.
\]

## Relevance to the endpoint attempt

PR146 at commit `f431078244e868dc699fad011044f0d5e7f76437` uses the ordinary
five-return block

\[
A(z)=(9z+7)/64,\qquad z=49\pmod{64}.
\]

Its sibling map is `z -> 64*z+49`. Here `p=2`, `C=7`, and `a=6`, which
attains the lower bound. More generally, keeping one complete parity cell
and adding fixed-word affine sibling loops cannot replace the exponential
clock by a polynomial clock as the prefix odd count grows.

A potential faster construction must satisfy hypotheses outside this
classification, for example by actually switching parity cells or using an
adaptive branching construction. The bounded two-child inverse tree in
`ENDPOINT_STEERING.md` is still a candidate; no all-precision depth bound for
that tree is proved in this checkpoint.

The global shell problem also remains: an endpoint-height improvement
would need a further quantitative argument meeting PR173's clean-shell
size condition. The classification above neither asserts that implication
nor supplies the missing selector.

## Verification

`CollatzGlobalClosure/SiblingRigidity.lean` is standalone and uses Lean `4.34.1`, with Mathlib
commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. It imports
`Mathlib.Tactic` and `Mathlib.NumberTheory.Multiplicity`. Every proved
declaration has a `#print axioms` report. The only reported axioms are
`propext`, `Classical.choice`, and `Quot.sound`; there is no `sorry` or custom
axiom.
