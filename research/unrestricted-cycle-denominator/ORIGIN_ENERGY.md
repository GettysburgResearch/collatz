# A spacing and Fourier test at the integer residue

Let a primitive shortcut word have L letters, K ones and D=2^L−3^K>0.
For word W denote its affine numerator by C(W), so its map is
(3^K x+C(W))/2^L. A primitive ordinary cycle at (L,K) contributes
L distinct rotations to the congruence fibre C(W)≡0 (mod D).
The following necessary conditions on this fibre work for every divisor
n≥2 of gcd(L,K), every cyclic cut, and arbitrary arrangements within
and across the n blocks. Write b=L/n, a=K/n and λ=3^a/2^b<1.

Split from the cut into n successive blocks of b letters. Write k_i and
C_i for their actual weights and affine numerators, respectively. Set

    s_0=0,   s_(i+1)=s_i+k_i−a,   S=max_i s_i,
    f_i=3^(S−s_(i+1)) C_i / 2^b.

The sequence s is cyclic, with s_n=0. Use the discrete Fourier
transform f̂(t)=n^(-1) Σ_i f_i exp(−2πiti/n). Then integer realization
requires both

    Σ_(1≤t<n) |f̂(t)|² / |exp(2πit/n)−λ|² ≥ (n²−1)/12,           (1)

    max_(cyclic intervals I) |Σ_(i∈I)(f_i−mean(f))| ≥ (n−1)/2.   (2)

All the inputs to (2) are rational, so it can be tested exactly.
Test (1) also has an exact rational implementation via the cyclic
linear recurrence below. For n=1 the corresponding right sides vanish.

## Proof

Let x_i denote the physical state at the entry to block i. Every cycle
state is coprime to 3: an odd step puts its output in the ternary units,
and dividing a ternary unit by 2 preserves that property. At least one
odd step occurs. The positive integers Z_i=3^(S−s_i)x_i are pairwise
distinct. Equality would first force equal ternary valuations and hence
equal s_i, then identical physical states, contrary to primitivity.

Multiplying the block equation by its terminal gauge gives precisely

    Z_(i+1)=λ Z_i+f_i.

Thus the nonconstant Fourier coefficients of Z are those of f divided
by exp(2πit/n)−λ. Order the n distinct integers Z_i increasingly.
Their pairwise distances dominate the distances among 1,...,n. The
variance identity n^(-2)Σ_(i<j)(Z_i−Z_j)^2 and Parseval give (1).

Let u_0=0 and u_(i+1)−u_i=f_i−mean(f), with u cyclic. Its oscillation
is the left side of (2). Subtracting the mean and iterating the stable
recurrence gives

    Z_i−mean(Z)=u_i−(1−λ) Σ_(r≥0) λ^r u_(i−1−r).

The geometric weights in the last term sum to one. Thus every centered
Z_i has absolute value at most the oscillation of u, and the Z diameter
is at most twice that oscillation. Its integer spacing gives (2).

## Separation from simultaneous near-full gcd

In the [rough-denominator family](ROUGH_DENOMINATORS.md), use the cut
at the encoding boundaries and take n equal to its coarse period.
Every block has exactly a ones; thus s_i=0. The forcing consists of
one constant and one impulse channel d_j 1_(p_j divides i) per encoded
pair. In chronological pair order j=1,...,k, the two encodings differ
by 1/4 at their pair output. The remaining homogeneous multiplier
equals λ/(3/4)^j, so d_j=(λ/4)(4/3)^j. On any cyclic interval the
number of multiples of p_j differs from its mean length/p_j by at
most one, since p_j divides n. Hence the entire discrepancy in (2)
is at most Σ_j d_j=O((4/3)^k). This is n^o(1) because
k=O(log q/log log q) and n≥q^(1−η−o(1)) in that construction.
The normalized boundary states have diameter n^o(1) and their
variance is n^o(1) as well. Thus both (1) and (2) detect these
nonintegral words, even though all rotations cancel nearly all of D
and every sufficiently small prime misses the reduced denominator.

The [earlier equal-slope diameter bound](../synchronized-cycle-blocks/README.md)
uses the total forcing range and the factor (1−λ)^(-1). Centered cyclic
discrepancy and the exact Fourier weights above can stay small as λ tends
to one, and the ternary normalization permits unequal block counts.
These are necessary conditions. No upper bound contradicting (1) or
(2) for every parity word is known here, and neither condition at
n≥2 is available when L and K are coprime.
