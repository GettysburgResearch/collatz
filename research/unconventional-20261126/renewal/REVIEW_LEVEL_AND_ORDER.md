# Independent review of two ordinary arithmetic obstructions

## Counted landing frontiers

**Verdict — verified conditional rate and unconditional finite formula.**
I checked [LEVEL_FRONTS.md](../adelic/LEVEL_FRONTS.md) at SHA-256
e1eaca725e3fddf110313ef0e4729b0f58178aa03373a27dc28361e1a9587386.
The count-optimized choice may be different on each row of the
landing table. The derivation bounds the sum of the row maxima
in the original octave law.

* On a residue modulo $2^h$, the two starts have fixed length-$h$
  parities and endpoint slopes $3^g$ under translation by $2^h$.
  Equal grades make the endpoint difference constant. If the
  grades differ, counted fusion has failed. Earlier counted fusion
  persists. Thus the bad event really is exactly periodic and
  a physical run of $M$ possible adjacent starts has at most
  $M Q_h+2^h$ failures.
* Positive trajectories satisfy $T^j(v)\ge v/2^j$. The lower
  guard before attempted fusion prevents all premature hits on
  the target row. If the two labels meet with the same grade,
  the remainder contributes identical target and residual grade.
  In the acyclic-component version a grade potential on the tree
  gives the same implication without a guard.
* On the logarithmically uniform octave, multiplication by three
  followed by folding by a power of two preserves the full law.
  With odd rounding $o$ at most one from $n$, the arguments
  $3o+1$ and $2^j\lfloor 3u/2^j\rfloor$ differ by a bounded
  integer. Their connecting adjacent comparisons are all at
  $n+O(1)$ or $3n+O(1)$, so each failed adjacent comparison
  invalidates only a bounded number of floor bins. This yields
  the joint total variation error $O(Q_h+2^h/X)$.
* On each integer row a nonnegative summable mass function has
  total variation against its unit translate at least twice its
  largest value in the unhalved convention. Full variation sums
  over disjoint rows. A possible cemetery mass is fixed under
  the translate. This proves the row-adaptive $w$ factor.
* For the sharpness family, the first $O(L)$ parities of a
  uniform source in the stated aligned octave of length
  $2^{L^2}$ are exactly independent fair bits. On the maximal
  variance event, log-height before first crossing its floor
  equals the tilted linear drift up to $O(\sqrt L)$, since the
  accumulated positive distortion is $O(L/Y)$. The same estimate
  applies at the first crossing using only its earlier departures.
  The count consequently lies in $O(\sqrt L)$ consecutive
  integers on a positive fraction of sources. One shared choice
  of a singleton attains the rate, even without target adaptation.

The external unrefereed input in the rate is the specifically
stated $Q_h\ll(h+1)^{-1/2}$. This review verifies its use and the
finite substitute. It does not replay the external formalization.

## Inversions of genuine positive cycle phases across dyadic scales

**Verdict — verified.** I checked
[DYADIC_CYCLE_ORDER.md](../adelic/DYADIC_CYCLE_ORDER.md) at SHA-256
75d634920ffef0d37f7589833d85ecbebe0044b9e36e0d33f96deab8f3c7b915.

The lifts have exactly one occurrence of each odd phase in any
half-open multiplicative octave. Writing the order-permutation
image of each of $p$ consecutive representatives as its permuted
residue plus $p$ times an integer proves that the mean displacement
equals the sum of those $p$ integers. The product of the real
scale ratios cancels the permuted representatives and equals
$2^N$, as required. Both strict order comparisons defining an
inversion give precisely $0<3(y-2^kx)<2^k-1$, and conversely.
The dyadic normalization therefore counts one simultaneous
translation class per ordered witness.

A periodic adjacent interchange with period $p\ge2$ swaps
disjoint pairs of places. Relative inversions between two distinct
ordered blocks have the same total because each block retains its
multiset of images. Within-block inversions decrease by one per
period. Across a fundamental cut this argument still works by
counting simultaneous-translation classes of pairs of blocks.
The count is finite as displacement is bounded. Sorting terminates
at the translation by the fixed mean $N$, whose quotient has
$\gcd(p,N)$ cycles. The initial quotient is one cycle. Each swap
changes the count by exactly one with either sign, establishing
both the lower bound and parity. The case $p=1$ is immediate.

For the arithmetic interpretation, the normalized intervals
$[3x,3x+1)$ are binary prefix intervals. Distinct left endpoints
follow from distinct odd representatives, and distinct right
endpoints from injectivity of the odd return within the cycle.
Strict containment is equivalent to the inversion inequalities.
An exact independent enumeration of all 6,381 one-cycle affine
permutations of periods 2 through 5 with each fundamental image
shift in $\{-1,0,1\}$ verified the bound and parity, including
boundary swaps. The positive $41\to5$ check takes exactly 39 odd
steps. The denominator-five cycle has exponents $1,1,3$.
The argument yields no contradiction at coprime grade and clock,
where both the lower bound and a possible inversion count are zero.
