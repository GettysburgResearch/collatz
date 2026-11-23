# Independent review: the full P* Q* cycle exclusion

**Date:** 2026-11-22 UTC.  
**Reviewer:** symbolic/literature agent, separate from the proof and
continued-fraction certificate producer.  
**Exact reviewed bytes:** `independent_pin_review_pins.json`.

## Finding

No mathematical or certificate-coverage gap was found in the stated
theorem: for the specified blocks
`P=(1,1,4,1,1,1,2)` and `Q=(2)`, every positive cycle in `P* Q*` is the
trivial Q-cycle. In particular all independent positive pairs `(m,n)`
are excluded. This review does not assert a classification of other
bounded languages or a proof of the full Collatz conjecture.

The written proof, separate exact verifier, JSON certificate, and Lean
physical-arithmetic source were read. The existing strict Lean build
receipt was inspected; no duplicate Lean build was requested. The
certificate verifier was independently executed, including its damaged
certificate controls.

## Mathematical checks

1. **The whole quotient is retained.** Coprimality in
   `2048^m(y+41)=2187^m(x+41)` forces the same positive integer cofactor
   `t` in `x+41=2048^m t` and `y+41=2187^m t`. Substitution into the
   Q-return equation gives exactly
   `(2^(11m+2n)-3^(7m+n))*t=42*(4^n-3^n)`. No denominator factor has
   been discarded, and positivity forces the multiplier below one.

2. **The entire cone `n>=m` is closed.** The multiplier ratio is bounded
   by `6561/8192`. The full cross equation then gives `x<170`, while
   dyadic divisibility gives `x>=2007`. The integer contradiction has
   margin 77. The proof needs no finite parameter census in this cone.

3. **The logarithmic cutoff is an all-tail argument.** In the remaining
   cone `1<=n<m`, the physical cofactor gives
   `0<Lambda<84*2^(-11m)`. Matveev Corollary 2.3 yields the independently
   checked specialization with coefficient `2^33`; replacing it by
   `10^12` is safely weaker. Writing `m=10^14*s`, `s>=1`, and using
   `log s<=s-1` proves the whole tail impossible. This is not an
   extrapolation from a finite computation.

4. **The reduced fraction and every integer scale are covered.** The
   approximation bound is stronger than Legendre's threshold even
   before reducing `p/q`. If `p/q=a/b` is reduced, then
   `m=d(2b-a)/3` and `n=d(7a-11b)/3`. The two congruence conditions
   modulo 3 are equivalent, so the least scale is exactly
   `d0=3/gcd(3,2b-a)`. Every allowed scale is a positive multiple of
   `d0`. Increasing that scale increases the logarithmic separation
   and decreases the permitted exponential error; exclusion at `d0`
   excludes all of its multiples.

5. **Zero exponents and rotations have the stated meanings.** A positive
   Q-only word fixes 1; a P-only word fixes -41 and has no positive
   cycle. The empty word is excluded. A cyclic rotation changes the
   positive starting value on an already closed orbit, not the cycle
   or the argument.

## Certificate checks

The verifier does not import the producer. It reconstructs the logarithm
enclosures by rational arithmetic, including the complete positive omitted
tail. Its continued-fraction recurrence validates consecutive common
digits of the whole enclosing interval, with no skipped convergents.
The terminal denominator exceeds the proved bound for every possible
primitive denominator. Lower convergents cannot have the required sign;
upper convergents are either outside the parameter cone, above the global
cutoff, or separated by an exact rational comparison.

The use of `2^min(11*m0,66)` weakens the separation test safely: proving
the comparison at a smaller power of two still excludes the sharper
required error. The acceptance path uses explicit checks, rather than
Python assertions that disappear under optimization.

The fresh independent execution returned:

| Item | Result |
|---|---:|
| Consecutive convergents | 32 |
| Lower convergents | 16 |
| Upper convergent outside the positive cone | 1 |
| Upper convergents separated exactly | 13 |
| Upper convergent above the pin cutoff | 1 |
| Terminal denominator | 5,750,934,602,875,680 |
| Damaged certificates rejected | 8 |

Certificate SHA-256:
`e573e0c9b9bb93bf4f72d403524dbb5f103ea23778dc1b1371b739f19b072e49`.

## Formal and external scope

The Lean source connects the exact `BlockPath` equations to the complete
integer quotient and excludes `n>=m`. That arithmetic path relation is
weaker than an actual positive odd Collatz path, so proving necessary
conditions for it covers every actual path in the stated family. The
six public axiom audits contain only `propext`, `Classical.choice`, and
`Quot.sound`.

The global `n<m` exclusion is a written proof plus an independently
checked exact arithmetic certificate. Matveev's theorem and the complete
continued-fraction closure are not claimed as Lean formalizations. The
primary Matveev normalization was independently read in Corollary 2.3,
printed page 1219, at the [publisher's primary source](https://www.mathnet.ru/eng/im314).
The full proof of that established external theorem was not re-audited.
