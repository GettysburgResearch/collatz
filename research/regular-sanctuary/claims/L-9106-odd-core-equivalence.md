# L-9106 - Odd-core equivalence

- **Claim ID:** L-9106
- **Title:** Shortcut sanctuaries are equivalent in existence to regular odd-core sanctuaries
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and elementary closure properties of regular languages
- **Scope:** canonical positive finite binary words under the shortcut map
- **Related counterexample candidates:** none

## Statement

For odd positive `n`, define the odd-only Collatz map

$$
U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
$$

The following two existence statements are equivalent:

1. there is a nonempty regular shortcut sanctuary `L`, meaning
   `T(L) subset L` and `L intersect {1,2}` is empty;
2. there is a nonempty regular language `O` of canonical odd positives with
   `U(O) subset O` and `1 notin O`.

The transformations are constructive.  From `L`, take its odd core

$$
O=L\cap\{n:n\text{ is odd}\}.
$$

From `O`, take its dyadic saturation

$$
\operatorname{Sat}_2(O)=\{2^k n:k\geq 0,\ n\in O\},
$$

whose LSD-first language is `0* O`.

## Definitions

The valuation `nu_2(m)` is the largest nonnegative `a` for which `2^a`
divides `m`.  Every value in `O` is odd, so its canonical word begins in `1`.
The notation `0* O` means any finite string of low zero bits followed by a
word of `O`; these are exactly the canonical encodings of the displayed
dyadic saturation.

## Motivation

Even shortcut steps contain no branching: they only remove low zero bits.
This lemma isolates the arithmetic search at odd values and shows that a
candidate may be sought with a forced start-state zero loop, provided closure
is imposed under the variable-length odd map `U`.

## Proof or construction

Let `L` be a shortcut sanctuary.  Its odd core is regular because odd
canonical words form a regular language.  It is nonempty: for any `n in L`,
write `n=2^b m` with `m` odd; then `T^b(n)=m`, so forward invariance puts `m`
in `L`.

For odd `m in O`, put `a=nu_2(3m+1)`, which is at least one.  The first
shortcut step gives

$$
T(m)=2^{a-1}U(m),
$$

and the next `a-1` shortcut steps give `U(m)`.  Thus `U(m)` is again in `L`
and is odd, so it lies in `O`.  Safety of `L` gives `1 notin O`.

Conversely, let `O` satisfy the odd-core conditions and put
`K=Sat_2(O)`.  The language `0* O` is regular and nonempty.  If
`x=2^k m` with `m in O` and `k>0`, then `T(x)=2^(k-1)m`, which is in `K`.
If `k=0`, then

$$
T(m)=2^{\nu_2(3m+1)-1}U(m),
$$

which is in `K` because `U(m) in O`.  Hence `T(K) subset K`.  Finally,
`1` or `2` belongs to `K` exactly when `1` belongs to `O`, so `K` is safe.

## Dependency audit

- D-9101 supplies the canonical LSD-first language semantics.
- Only intersection with a regular parity language and left concatenation by
  `0*` are used for regularity.
- The arithmetic argument uses the definition of `T`; it does not assume that
  an unrestricted number of shortcut steps can be composed into a fixed-size
  checker.

## Gap audit

- The two constructions are an existence equivalence, not inverse maps on
  every language.  Starting from an unsaturated `L`, `Sat_2(O)` may add even
  predecessors that were absent from `L`.
- Equality `L=Sat_2(O)` holds exactly when semantic membership is invariant
  under multiplication by two.  A start-state zero loop is a sufficient
  syntactic realization, but an arbitrary nonminimal DFA for the same language
  need not display that loop literally.
- X-9101 now contains a seven-state subsequential transducer for the totalized
  map `U(odd_part(n))` and an exact DFA lift implementing `0* O`.  These are
  conjecture-generation machinery; every lifted candidate still returns to
  the unchanged standard shortcut verifier for its final certificate.

## Adversarial tests

- If `O={1}`, then `0* O` contains both forbidden powers `1` and `2`, showing
  why odd-core safety must exclude `1`.
- If a nonempty proposed `L` had no odd member, repeatedly halving any member
  would contradict positivity; this checks the nonemptiness step.
- `test_odd_core.py` compares the seven-state transducer with direct arithmetic
  on all odd values below 100,000, tests the lift by odd-part membership, and
  compares odd-side and lifted closure on every two-state DFA.  These are
  regression checks, not substitutes for the proof.

## Remaining uncertainty

The set-theoretic equivalence appears complete.  The new transducer and lift
share the program's authoring trust boundary and remain `EMPIRICAL` support;
no claim is made that odd-core automata are smaller than the best unsaturated
shortcut automata.

## Suggested next attack

Independently reconstruct the seven-state `U(odd_part(n))` transducer, then use
it for nonslender odd-core conjecture generation and compare every lifted
candidate with the unchanged standard shortcut verifier.
