# L-9107 - Dyadic-cylinder basin density

- **Claim ID:** L-9107
- **Title:** Every dyadic residue cylinder contains infinitely many trivial-basin values
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** elementary shortcut arithmetic and the order of 2 modulo powers of 3
- **Scope:** every residue modulo every fixed power of two
- **Related counterexample candidates:** none

## Statement

For every `A >= 0` and every residue `r modulo 2^A`, there are infinitely many
positive integers `n` such that

$$
n\equiv r\pmod{2^A}
$$

and the shortcut orbit of `n` reaches a power of two, hence the trivial cycle.

Consequently, no sanctuary contains an entire dyadic residue cylinder, or all
sufficiently large members of such a cylinder.  In particular, a nonempty
eventually fixed-modulus language cannot be a sanctuary unless its accepted
part is finite and already contains a nontrivial cycle.

## Definitions

A dyadic residue cylinder is

$$
C(A,r)=\{n\geq 1:n\equiv r\pmod{2^A}\}.
$$

An eventually fixed-modulus language is one for which some `A,N` make
membership for every `n >= N` depend only on `n modulo 2^A`.

## Motivation

Low-bit residue templates are a natural LSD-first automata search space.  The
lemma gives an unconditional obstruction to every template that accepts all
high-bit continuations after fixing only finitely many low bits.

## Proof or construction

The case `A=0` follows from the infinitely many powers of two.  Fix `A>0` and
take the representative `0 <= r < 2^A`.  For the proof only, extend `T` by
`T(0)=0`.  The first `A` parity decisions of

$$
n=r+2^Aq
$$

depend only on `r`.  If exactly `a` of those decisions are odd, induction on
the `A` shortcut steps gives

$$
T^A(r+2^Aq)=3^a q+s,
\qquad s=T^A(r).
$$

If `a=0`, all `A` low bits of `r` are zero, so `r=s=0`; choosing
`q=2^k` works for every `k`.

Suppose `a>0`.  Immediately after the last odd step among the first `A`
steps, the constant trajectory is

$$
\frac{3x+1}{2}\equiv 2\pmod 3.
$$

Every remaining step is a halving and therefore preserves nonzeroness modulo
three.  Hence `3` does not divide `s`.

The residue `2` generates the unit group modulo `3^a`.  One elementary check
is

$$
\nu_3\!\left(2^{2\cdot 3^j}-1\right)=j+1,
$$

which gives order `2*3^(a-1)`, the full value of `phi(3^a)`.  Therefore there
are arbitrarily large `k` with

$$
2^k\equiv s\pmod{3^a}.
$$

For every sufficiently large such `k`, set

$$
q=\frac{2^k-s}{3^a}\geq0.
$$

Then `n=r+2^Aq` is in the prescribed cylinder and `T^A(n)=2^k`.  Varying `k`
through its infinite congruence class produces infinitely many distinct `n`.

If a sanctuary accepted all sufficiently large values in one cylinder, one of
these constructed basin values would be accepted and forward invariance would
put `1` or `2` in the language.  For an eventually fixed-modulus language,
every accepted residue has exactly this problem.  If no residue is eventually
accepted, only finitely many values remain; any nonempty finite forward-
invariant set consists eventually of a cycle.

## Dependency audit

- The affine formula is proved directly from the shortcut branches.
- The only number-theory input is the elementary primitive-root fact for `2`
  modulo `3^a`; the displayed valuation identity supplies a compact proof.
- No verified Collatz range or unproved orbit statement is used.

## Gap audit

- A general DFA is not a fixed-modulus predicate: it may inspect arbitrarily
  high bits before the canonical word ends.
- Pumping a regular language does not force it to contain a whole dyadic
  cylinder.
- The lemma therefore refutes residue-cylinder and accepting-continuation-cone
  templates, not arbitrary regular sanctuaries.

## Adversarial tests

- `A=1,r=1` gives `T(1+2q)=2+3q`; odd `k` make
  `q=(2^k-2)/3` integral.
- `A=2,r=1` gives `T^2(1+4q)=1+3q`; even `k` make
  `q=(2^k-1)/3` integral.
- `r=0` is kept separate from the modular-unit argument because its constant
  `s` is zero.

## Remaining uncertainty

The proof appears complete.  Its automata consequence must retain the stated
fixed-cylinder scope.

## Suggested next attack

Add a syntactic search filter rejecting any DFA state from which every
canonical high-bit continuation is accepted, while preserving machines whose
tail behavior remains genuinely branching.
