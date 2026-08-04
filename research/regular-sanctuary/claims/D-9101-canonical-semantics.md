# D-9101 — Canonical regular-sanctuary semantics

- **Claim ID:** D-9101
- **Title:** Canonical LSD-first candidate language
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** none
- **Scope:** finite positive integers represented by complete binary DFAs
- **Related counterexample candidates:** none

## Statement

For a complete DFA `D` over `{0,1}`, define

$$
L_D=L(D)\cap\mathcal C,
\qquad
\mathcal C=\{w\in\{0,1\}^*:w\text{ is nonempty and ends in }1\}.
$$

For `w=w_0...w_(r-1)` in `C`, its integer value is

$$
[w]=\sum_{i=0}^{r-1}w_i2^i.
$$

Every use of a candidate DFA in this program refers to `L_D`, never to the raw
language alone.

## Definitions

- **LSD-first:** the first symbol is the coefficient of `2^0`.
- **Canonical positive:** a finite nonempty word whose last symbol is `1`.
- **Raw language:** the ordinary language accepted by `D` before intersection
  with `C`.

## Motivation

Initial zeroes encode genuine low bits, while terminal zeroes are removable MSB
padding.  Without canonicalization, one integer has many words and a padded
relation can masquerade as a finite-positive-integer certificate.

## Proof or construction

Every positive integer has exactly one ordinary binary expansion ending in its
highest nonzero bit.  Reversing that expansion gives exactly one member of
`C`.  Conversely, every word in `C` has a highest bit equal to one and hence
evaluates to a positive integer with that unique binary expansion.

## Dependency audit

None.

## Gap audit

- The definition excludes zero intentionally.
- Infinite LSD streams are not admitted; they are 2-adic objects rather than
  finite positive integers.
- A raw DFA may accept noncanonical words, but they have no semantic effect.

## Adversarial tests

`test_regular_sanctuary.py` checks `1`, `01`, `101`, empty input, terminal-zero
aliases, and a DFA whose only raw accepted word is noncanonical `10`.

## Remaining uncertainty

None about the definition.  A reviewer should still confirm that every later
algorithm applies the semantic intersection at all endpoints.

## Suggested next attack

Independently trace canonical monitors through `terminal_relation` and attempt
to produce a padded or empty-word false witness.
