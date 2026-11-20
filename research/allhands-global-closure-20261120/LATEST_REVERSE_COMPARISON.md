# Targeted comparison with the refreshed reverse-basin reductions

Read-only source inspection, 2026-11-20. Source: PR146 at
`e238c63a5d57f96bb063b7472498d1977df51951`, files in
`research/upper-bit-mergers/` named below. No source checker or Lean build
was replayed in this targeted comparison; it is not a new proof review of
those entire files.

## What the update changes

`DEEP_REVERSE_BASIN.md` reduces full Collatz to the reverse implication
`3z reaches 1 => z reaches 1` at odd multiples of nine. Equivalently it
suffices to prove `128k+1 reaches 1 => 64k+1 reaches 1` for positive
indices not divisible by four. Its first nonempty antecedent odd-rank
class already asks for convergence of the pure powers `3^(27j-1)`.

`REVERSE_BASIN.md` gives an earlier analogous reduction at odd multiples
of three, with a fully covering bounded directed descent. These are
additional sharp targets; the reverse implications remain unproved.

## Relation to the prime-support peak theorem

An initial power of three has one prime in its factorization. The peak
theorem instead requires control of the union of primes throughout an
actual forward segment. Its next odd state is already a ternary unit and
can introduce other primes. A low-support starting value does not provide
a low-support future.

The added directed moves `z -> 3z` at odd multiples of nine do preserve
the initial prime support exactly, since three already divides `z`.
This is suggestive but does not create a valid application of the peak
theorem to the directed certificate: that path also uses inverse ordinary
edges, and it is not one forward odd trajectory. The positive affine
correction and disjoint forward return costs in P1/P13 do not automatically
hold along such a mixed path.

Likewise, knowledge that `3z` converges supplies a finite prime pool only
for the trajectory of `3z`. It provides no bound on the distinct future
of `z` until an ordinary merger or another genuine transfer is proved.
Such a transfer would be the missing mathematical content, not a
consequence of the two sources having identical prime support initially.

## The Mersenne comparisons

`MERSENNE_EXPONENT_DESCENT.md` gives ordinary finite-resistance families,
including a lower-arm odd-cost obstruction for comparisons to smaller
shifted ternary powers. It also gives actual smaller predecessors on
specified exponent classes, without proving those predecessors converge.
None of these conclusions bounds the union of primes of an unrestricted
future.

`MERSENNE_ODD_COST.md` gives a lower bound for the number of odd inputs on
a finite path to a specified smaller-height target. This is compatible
with the prime-support barrier: a hypothetical long trajectory may incur
both a large odd-step cost and many new primes. No incompatible upper
bound is present.

The most direct remaining bridge for this combined route would prove
that the actual future of `z` cannot create the prime support required
by P9/P13 whenever `3z` is known to converge. No such statement follows
from the inspected reductions. No new experiment or full-proof claim is
made by this comparison.
