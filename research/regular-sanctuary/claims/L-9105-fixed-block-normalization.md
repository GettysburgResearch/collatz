# L-9105 — Fixed-block normalization

- **Claim ID:** L-9105
- **Title:** Every fixed-block regular sanctuary induces a one-step sanctuary
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** L-9101 and regular closure under subsequential images
- **Scope:** a fixed positive block length B
- **Related counterexample candidates:** none

## Statement

If a nonempty regular language `L` of canonical positives satisfies

$$
T^B(L)\subseteq L,
\qquad
L\cap\{1,2\}=\varnothing
$$

for fixed `B >= 1`, then

$$
K=\bigcup_{i=0}^{B-1}T^i(L)
$$

is a nonempty regular one-step sanctuary: `T(K) subset K` and
`K intersect {1,2}` is empty.

## Definitions

`T^i(L)` is the pointwise image of the represented integer language under the
shortcut map, recoded canonically.

## Motivation

Block maps and cyclic phase automata may describe a candidate compactly.  This
lemma clarifies that fixed blocks improve representation but do not create a
larger existential class than one-step regular sanctuaries.

## Proof or construction

Each image `T^i(L)` is regular because L-9101 is a subsequential transduction,
and a finite union of regular languages is regular.  Moreover,

$$
T(K)=\bigcup_{i=1}^{B}T^i(L)\subseteq K
$$

because the last term `T^B(L)` is contained in `L`.

Suppose `y` in `{1,2}` belongs to `T^i(L)` for some `0 <= i < B`.  Iterating
`B-i` more shortcut steps keeps the value within `{1,2}`, so a forbidden value
belongs to `T^B(L) subset L`, contradicting the hypothesis.  Hence `K` is safe.

## Dependency audit

- L-9101 supplies a subsequential representation of `T`.
- Standard closure of regular languages under subsequential image and finite
  union is used.

## Gap audit

- The block length must be fixed and finite.
- This does not say that composing transducers is computationally cheap.
- Variable or input-dependent block lengths are outside the statement.

## Adversarial tests

The trivial cycle demonstrates why both forbidden values must be tracked.  A
future phase-cover implementation should construct `K` explicitly on small
control maps and compare one-step closure with the block condition.

## Remaining uncertainty

The set-theoretic proof appears complete.  The phase-cover implementation has
not yet been written.

## Suggested next attack

Implement cyclic languages `L_0,...,L_(B-1)` with exact inclusions
`T(L_i) subset L_(i+1 mod B)` using the base transducer and maximal kernel on
phase/state pairs.
