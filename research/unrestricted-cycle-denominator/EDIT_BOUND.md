# Full-denominator stability under one insertion

Let W be a primitive shortcut parity word of length L with K ones,
D=2^L−3^K>0 and positive fixed point t/H in lowest terms at a chosen
cut, so its affine map is (3^K x+N)/2^L and HN=Dt. Append V at that
cut (equivalently insert into the cyclic word), with length r, k ones
and affine numerator C. Let D'=2^(L+r)−3^(K+k) and N' denote the
edited rotation denominator and numerator. For 0<r<L,

    gcd(|D'|,N') divides |(3^k−2^r)t+HC| > 0.

Indeed N'=3^k N+2^L C, and reduction modulo D' gives

    2^r H N' = 3^(K+k) [(3^k−2^r)t+HC] mod D'.

When K+k>0, D' is prime to six, proving the divisibility. A positive
fixed point of W requires K>0. If the bracket vanishes, V itself fixes
t/H. Its integer affine numerator and fixed-point equation force its
prescribed parity at every rotation, since the fixed-point denominator
2^r−3^k is odd and the first letter is the affine numerator modulo two
(for k=0 the only fixed point is zero). Thus deterministic rational
shortcut iteration from t/H returns after r steps, which contradicts
primitivity of W. These arguments also allow D'<0.

The affine map of either letter sends any nonnegative x to at most
(3x+1)/2. Iterating from zero gives C≤3^r−2^r. In particular the
edited gcd is at most 3^r(t+H). This holds regardless of the
arrangement or counts in V.

For the family in [the near-full gcd construction](NEAR_FULL_GCD.md),
the bound applies uniformly over every cut. To check the numerator
height, monotonicity gives each block offset at most (3/2)^b. Each
boundary fixed orbit value is therefore at most (3/2)^b/(1−A/B),
and B−A≥1 gives (1−A/B)^(-1)≤2^b. The same letter bound at interior
points costs a further exp(O(b)). Thus log(t+H)=O(b+log H)=o(L).
Every nonempty edit by r=o(L) insertions concentrated at one cut
turns the simultaneous original gcd D exp(−o(L)) into exp(o(L))
at most. The edited raw denominator still has log |D'| asymptotic to
L log 2: the standard two-logarithm lower bound
|m log 2−n log 3|≫(m+n)^(-C) gives the lower estimate. If the
edited denominator is positive it suffices for this estimate that
the absolute drift be at least exp(−o(L)).

For a hypothetical ordinary positive integer cycle the same arithmetic
bound is 3^r(t+1) at any cut and in particular at its least state m.
The product of branch multipliers gives, with natural logarithms,

    0<L log 2−K log 3=Σ_(odd x) log(1+1/(3x))≤K/(3m).

The same lower bound for two logarithms gives m at most polynomial
in L. Consequently at the minimum of any hypothetical family of
unbounded integer cycles, all one-cut insertions of o(L) letters have
gcd at most exp(o(L)). This does not provide a cut/edit for which both
words must have large gcd.

Lagarias's Theorem 3.2 places large cancellations in the context of the
primitive-cycle existence conjecture for rational denominators. Its
conclusion allows the selected denominators to have no primitive cycle.
The periodic construction linked above supplies actual orbits of growing
reduced denominator and the edit bound concerns their immediate neighbors.
See [Lagarias, Acta Arithmetica 56 (1990), 33–53](https://doi.org/10.4064/aa-56-1-33-53).
