# L-9101 — Shortcut transducer correctness

- **Claim ID:** L-9101
- **Title:** Five-state subsequential realization of the shortcut map
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101
- **Scope:** every canonical finite encoding of a positive integer
- **Related counterexample candidates:** none

## Statement

The table in `../SEMANTICS.md` defines a deterministic subsequential transducer
which maps the canonical LSD-first encoding of each positive integer `n` to the
canonical encoding of

$$
T(n)=n/2\quad(n\text{ even}),
\qquad
T(n)=(3n+1)/2\quad(n\text{ odd}).
$$

It has a terminal output on every canonical input and emits a canonical output.

## Definitions

The states are start `S`, even copier `E`, and carry states `C0,C1,C2`.  A
subsequential transition consumes one input bit and emits a finite output word;
the terminal output flushes the final carry.

## Motivation

Regular-language closure is useful only if the arithmetic relation is exact at
word boundaries.  The delayed first output and final carry are the two places
where a plausible synchronous implementation commonly fails.

## Proof or construction

For an even canonical word, the first bit is zero.  Removing it shifts the
remaining binary expansion down by one place and therefore computes `n/2`.

For odd `n`, write `n=1+2m`, so `T(n)=3m+2`.  Initialize carry `c_0=2`.  After
processing `i` bits of `m`, let `Y_i` be the value already emitted.  The
invariant is

$$
3m+2=Y_i+2^i\left(3\left\lfloor m/2^i\right\rfloor+c_i\right).
$$

If the next suffix bit is `b`, division of `3b+c_i` by two emits its parity bit
and sets the quotient as `c_(i+1)`.  This preserves the invariant and confines
the carry to `{0,1,2}`.  At end of input the integer suffix is zero; emitting
the canonical representation of the carry completes `3m+2`.

Every nonempty input leaves `S`.  The table supplies terminal outputs for
`E,C0,C1,C2`, so canonical-domain totality is explicit.  A canonical even input
ends with a copied one.  A canonical odd input ends in a carry state whose
flush ends in one.  Outputs are therefore canonical.

## Dependency audit

- D-9101 supplies word orientation and canonical endpoints.
- No empirical equality check is used in the algebraic proof.

## Gap audit

- The table implements the shortcut map, not the odd-only fully accelerated
  Syracuse map.
- Reversing terminal output `01` to `10` changes the value and canonicality.
- Omitting terminal outputs makes relation checking vacuous unless rejected.

## Adversarial tests

The suite checks direct arithmetic for `1 <= n < 20000`, boundary outputs
`1,2,3,5,7,8`, a reversed carry, and a machine with all terminal outputs
removed.  The baseline separately compares through `n < 100000`.

## Remaining uncertainty

The proof and implementation share an author.  Independent reconstruction from
the invariant is still required for status promotion.

## Suggested next attack

Write a second transducer implementation using the alternative `n+2n+1`
previous-bit carry convention and compare complete finite relations.
