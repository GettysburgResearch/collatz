# Convergent sources in every binary–ternary residue cylinder

**PROVED elementary auxiliary lemma.** This is a density statement about the
known basin. It does not imply that every positive integer is in that basin.
It can ensure that a residue-cylinder obstruction is witnessed by genuine
convergent sources, rather than only by formal congruence solutions.

Let `T(n)=n/2` for even positive `n`, and `T(n)=(3n+1)/2` for odd positive
`n`. Let `C` be its actual positive basin of 1.

## Theorem

For every pair of nonnegative integers `a,b` and every integer `r`, the
progression

`n = r (mod 2^a*3^b)`

contains infinitely many elements of `C`. The construction gives an explicit
finite ordinary certificate for each such element. In particular, imposing
finitely many compatible binary and ternary congruences never by itself
excludes membership in `C`.

## Proof

Choose a positive integer `w` congruent to `r` modulo `2^a`, taking the least
positive representative, and put `L=a+1`. Because `1<=w<=2^a`, the first
`L` shortcut steps from `w` contain at least one odd input. Let their number
of odd inputs be `q>=1`.

Every positive integer `n` congruent to `w` modulo `2^L` has the same first
`L` parity bits. This follows inductively: after `i` steps, the difference
between its current value and that of `w` is divisible by `2^(L-i)`.
The common affine formula is

`T^L(n)=(3^q*n+B)/2^L`,

where `B` is a nonnegative integer not divisible by 3. To see the last
claim directly, each odd step contributes a power of 2 times a power of 3
to `B`; the last odd step contributes a power of 2 with no factor of 3,
and all earlier odd steps contribute multiples of 3.

The number 2 generates all units modulo every `3^m`, for positive `m`.
Indeed its order must be even, and

`v3(2^(2t)-1)=1+v3(t)`.

The latter identity follows by factoring a power of 4 minus 1, or by the
elementary lifting identity `v3(x^3-1)=v3(x-1)+1` for `x=1 (mod3)`.
Consequently the order is exactly `2*3^(m-1)`, the number of units.

The integer `B+3^q*r` is a unit modulo `3^(q+b)`. We can therefore choose
arbitrarily large nonnegative integers `A` in one fixed residue class modulo
`2*3^(q+b-1)` such that

`2^(L+A) = B+3^q*r (mod 3^(q+b))`.

Define

`n_A=(2^(L+A)-B)/3^q`.

For sufficiently large `A`, this is a positive integer, and the displayed
congruence gives `n_A=r (mod3^b)`. Modulo `2^L`, it satisfies

`n_A=-B*3^(-q)=w (mod2^L)`,

where the second equality follows from the affine identity for `w`.
Hence it has exactly the prescribed first `L` parity bits, and

`T^L(n_A)=2^A`, followed by `A` even steps to 1.

It also satisfies `n_A=r (mod2^a)`. The binary and ternary congruences
combine to give the required progression. The arbitrarily large choices of
`A` give distinct unbounded elements of `C`. This proves the theorem.

## Scope for reverse-criterion obstructions

Suppose a proposed finite-word reverse-certificate proof leaves an entire
nonempty progression for the known convergent parameter `z`, specified by
compatible congruences modulo powers of 2 and 3. The theorem supplies actual
`z in C` in that progression, including arbitrarily large choices. If its
ordinary upper antecedent is an integral inverse image of `z`, that upper
antecedent is also in `C` by the explicit inverse certificate.

This observation does **not** prove that the lower companion is outside `C`.
It only shows that a failure of a restricted finite proof method on that
cylinder cannot be dismissed by supposing that the cylinder avoids all
convergent upper sources. An unbounded or certificate-dependent proof may
still resolve every one of those sources.

The standalone checker `check_basin_crt_density.py` verifies the construction
for all residues at `0<=a<=4`, `0<=b<=3`, using literal shortcut iteration of
the first `L` steps and exact arithmetic for the terminal power of two.
These finite checks audit the formulas; the arbitrary-parameter theorem is
proved above.
