# Distinct ordinary phases in equal-weight block cycles

**PROPOSED.** The following diameter bound excludes every mixed periodic
concatenation of two blocks that differ by one adjacent swap, for any common
prefix and suffix and any schedule of choices. It also gives a finite bound
on the number of distinct boundary values for larger block alphabets.

Use the positive ordinary shortcut map with even branch `x/2` and odd branch
`(3x+1)/2`. Choose a finite alphabet of distinct binary words of the same
length L and the same number q of ones, with q positive. Digits are read
in forward time. Put B = 2^L and A = 3^q. The affine numerator c(w) is
obtained by composing the prescribed branches, so that the endpoint is
(Ax+c(w))/B. Explicitly each one at position j (zero indexed) contributes
2^j times 3 raised to the number of later ones. Every numerator is positive.
An ordinary cycle of blocks here means that every branch is physically
replayed, with integral positive values at every step and the initial value
restored at the end. The argument also applies to a cycle admitting a block
cut after a rotation of its parity itinerary.

## A spacing and diameter bound

Take a cyclic block schedule with primitive block period m. Restrict the
alphabet to its used blocks. If at least two are used, let R be the
difference between the largest and smallest c, and let G be the positive
gcd of all differences c-c_min. Distinct words have distinct numerators:
modulo 2^L, a fixed c forces a single initial residue, since A is odd.
Each word has a legal initial residue (invert the branches modulo powers of
two backwards, or inductively lift its prefix cylinder), and a residue
determines every parity through time L. Thus R and G are positive. Put

    H_m = G / gcd(G, B^m - A^m).

A positive ordinary cycle requires D = B-A > 0. If m > 1, it requires

    (m-1) D H_m < R.

In particular, let H be the product of all powers of 2 and 3 dividing G.
Then H divides H_m, and every mixed ordinary cycle has
m <= ceil(R/(D H)). Bounding m uses no primality or factorization
assumption on the complete denominator.

**Proof.** Write x_i for cyclic boundary values, c_i for the corresponding
numerators, and use indices modulo m. Iteration of B x_(i+1) = A x_i + c_i
gives the exact complete-denominator identity

    (B^m-A^m) x_i = sum_{j=0}^{m-1} A^(m-1-j) B^j c_(i+j).

Its right side is positive, forcing B>A. The coefficients are positive
and sum to (B^m-A^m)/D. Every rotation contains both a smallest and
a largest digit, so each x_i lies strictly between c_min/D and c_max/D.
Subtracting the identities for any two phases shows G divides
(B^m-A^m)(x_i-x_j). Ordinary integrality gives H_m | (x_i-x_j). Because
B^m-A^m is coprime to 6, H divides H_m. Physical determinism and the
primitivity of the block schedule make all m boundary values distinct:
a repeated boundary would repeat every subsequent block. Their diameter
is consequently at least (m-1) H_m and strictly below R/D, as asserted.

## Arbitrary synchronized adjacent swaps

Let p and s be any fixed binary words, possibly empty. At each block use
either p01s or p10s, independently of the other choices. There is no
positive ordinary cycle whose block schedule uses both. Indeed, the
earlier and later odd positions in the swapped pair contribute respectively
2^|p| 3^ones(s) and twice that amount. Every other contribution is
unchanged. Hence

    R = G = H = 2^|p| 3^ones(s).

For D>0, the spacing bound would give (m-1)D < 1, impossible for m>=2.
For D<0 positivity already rules out the schedule. The same proof works
for any pair of equal-length equal-weight words whose affine numerator
difference has prime factors only 2 and 3 (including difference 1).
More generally, the pair is excluded whenever R/H <= D.

This is an exclusion over arbitrarily large block lengths and primitive
periods. A constant schedule still has its individual condition
D | c(w), with ordinary replay. An unrestricted Collatz cycle need not
admit any mixed swap decomposition. The missing implication for a global
cycle argument is a covering theorem for other itineraries or an independent
obstruction for them.

## Arithmetic controls

For p and s empty the mixed schedule `01,10` has complete denominator
4^2-3^2=7 and its two formal boundary values are 10/7 and 11/7.
They are positive and distinct. The constant schedules give the ordinary
boundaries 2 and 1 respectively. This tests both the integrality hypothesis
and the restriction to mixed schedules.

The local [checker](check.py) reconstructs small affine numerators by
physical integer simulation on every source residue, checks the swap
formula for every split through the stated finite horizon, and checks
cyclic spacing by complete-denominator arithmetic for small unrestricted
equal-weight schedules. These finite tests are separate from the proof.

Base commit `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The [periodic-tails packet](../integrated/periodic-tails/README.md)
records related full-denominator algebra and its integration qualifications.
PR 61 was inspected at `046eeda2268b4ac1b90a9618a4ed2460a111a0e5`.
The spacing bound above is proved directly.
