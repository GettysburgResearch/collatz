# A zero top norm on primitive two-gap rational cycles above every floor

**Claim (written proof).** For every real H there is a primitive positive rational accelerated 3x+1 cycle with odd reduced denominator greater than H, all of whose states exceed H, every gap either one or two, and top determinant J₄=0 in PR191 TCP-4. The clock satisfies gcd(A,p)=4 and its positive overshoot A−p log₂3 can be arbitrarily small. Moreover, for this eight-block template and every common prefix of arbitrary positive gaps, positivity of the cycle implies its complete reduced denominator exceeds 4·9^n/7, where n is the block length. Thus no such template closes on ordinary positive integers.

**Seed identity.** Let w=(1,1,1,2,1,2,2,2), with prefixes d=(0,1,2,3,5,6,8,10). For Q(Y)=sum 2^(d_i)Y^(7−i) one has
    Q(Y)=(Y²+4Y+8)(Y⁵−2Y⁴+4Y³+8Y²−32Y+128).
Only the polynomial enters the construction; the seed by itself has 2¹²<3⁸.

**Clocks.** Put α=log₂3, which is irrational by unique prime factorization. There exist relatively prime odd a and even b tending to infinity with δ=a−bα→0 from above. Let nα approach a half integer from below modulo one, using density of an irrational rotation. The next odd integer above 2nα then gives a positive error tending to zero. Reduce these odd/even fractions by their (odd) gcd. The errors remain positive and tend to zero, and the reduced denominators tend to infinity by irrationality.

**Gap words and complete carry.** Write b=2n, S=(a−3)/2, s=2^S. For large enough n there are common prefixes v of n−1 gaps in {1,2} of sum S with both a 1 and a 2: S/(n−1) tends to α in (1,2). Form the cyclic word of eight blocks (v,w_i). Its clocks are p=8n=4b, A=8S+12=4a. Every period of the expanded cyclic gap word is a multiple of n: the nonempty set of positions where the word differs from its n-shift occupies only the last column modulo n, and any period preserves this difference set. A multiple of n is a period only if its block shift is a period of w. The first and fifth letters of w happen to agree, but the second and sixth differ; hence w does not have period four, and its minimal period is eight. The expanded word is primitive.

Let e_j be the prefix sums within v for j=0,...,n−1, so e₀=0,e_(n−1)=S. Define P(X)=sum 2^(e_j)X^(n−1−j). Multiplying the two sums after splitting an absolute index as i n+j gives the exact carry polynomial
    Q_full(X)=P(X) W_s(X^n),    W_s(Y)=s^7 Q(Y/s).
Indeed the odd position prefix is iS+d_i+e_j and its X exponent is (7−i)n+(n−1−j). The cyclotomic top factor is X^(4n)+2^(2a) and, in Y=X^n, is Y⁴+64s⁴. Both it and W_s(Y) contain Y²+4sY+8s², as verified by explicit multiplication. The top polynomial and Q_full share a complex root after substitution. The common zero is independent of the boundary chosen in TCP-4: the one-step cyclic rotation obeys 2^(g₀)Q_rot(X)=X Q_full(X)−X^p+2^A, and every top root is nonzero and satisfies X^p=2^A. By the exact common-root equivalence in PR191, J₄=0. Source: GettysburgResearch/collatz PR191, 37b3916633cd32a0c173b20bb18ec3a7ec290a63, research/two-sided-cycle-packing-20261124/README.md, TCP-4 (9).

**Positive rational realization and minimum.** With D=2^A−3^p>0, the boundary state is q=Q_full(3)/D. Every rotation has the same D and positive odd carry numerator. The affine identities link the rotated states by 2^g q'=3q+1. Odd numerator and denominator after reduction give exact 2-adic valuation g; the prescribed gap clock is therefore literal on odd-denominator rationals. The denominator is the same on the whole cycle since it is coprime to 6. Primitivity of the gaps forces primitivity of the actual rational cycle. Multiplying the complete one-step equations gives
    product over vertices (1+1/(3q)) = 2^A/3^p = 2^(4δ).
Each factor is at most the product, so min q ≥ 1/[3(2^(4δ)−1)]→∞.

**Every common-prefix template is excluded over ordinary integers.** This step allows any fixed prefix v of arbitrary positive gaps, with S=sum v and n=1+length(v), even when the gaps in v exceed two and the clock gcd differs from four. Whenever D>0, its complete reduced denominator is strictly greater than 4·9^n/7.

Write z=3^n, s=2^S and B(Y)=Y⁵−2Y⁴+4Y³+8Y²−32Y+128, with B_s(z)=s⁵B(z/s). From 2^A=4096s⁸ and 3^p=z⁸ one obtains
    D=f V,  f=z²+4sz+8s²,
    V=(8s²−z²)(8s²+z²)(z²−4sz+8s²).
The full numerator is P(3)f B_s(z). All three factors of V are odd, since z is odd, and hence are coprime to s. For each factor we may evaluate integral polynomial identities at y=z/s modulo any common divisor with B_s(z). The identities are
    (y⁴−3y³+14y²−20y+72)(8−y²)+(y−1)B(y)=448,
    (y³−2y²−4y+24)(8+y²)−B(y)=64,
    (48−y⁴)(y²−4y+8)+(y−2)B(y)=128.
Thus the gcd of the first evaluated factor with B_s divides 7 and the other two gcds equal 1. Prime valuations give gcd(V,B_s)≤7, even when the factors share primes. Consequently the complete reduced denominator is V/gcd(V,P(3)B_s)≥V/(7P(3)).

Since D>0 the integer 8s²−z² is at least one. Also 8s²+z²≥4zs and z²−4zs+8s²≥z²/2 by completing squares. Hence V≥2z³s. From 2^(e_j)≤s we have P(3)≤s(z−1)/2<sz/2. Therefore the denominator exceeds 4z²/7, as claimed. This proves uniform ordinary-cycle exclusion on the full template, including every high-floor cycle above, without assuming Collatz, a minimum-state bound, an additional Diophantine approximation rate or bounded letters inside the prefix.

The common prefix in these examples is deliberately long. The construction does not rule out an independent obstruction based on the complete reduced denominator or other word structure. It refutes the specific sufficient condition that primitivity, a high floor, a two-letter gap bound and a near-critical clock guarantee a nonzero top norm.

**Exact fixture.** The standard-library replay high_floor_control.py checks the complete-denominator inequality and the residual divisibility by 7 on 3826 contracting common prefixes of length at most 5 over {1,2,3,4,8}. It also constructs the two cycles for (a,b)=(485,306), (A,p)=(1940,1224) and S=241. Both have 1446-bit reduced denominators. The floors of their actual rational minima are 38483 for prefix start (1,2), and 30790 for (2,1). The replay checks each full step and all possible proper periods, both complete numerator factorizations, the least-common-multiple identity, and the separate all-state product floor >81 by integer comparison. HighFloorNorm.lean supplies the symbolic seed and cyclotomic identities after substitution, integral Bézout certificates, and separate finite gcd and inequality declarations. Its compilation receipt identifies the exact declarations checked. The rotation, valuation, clock approximation, index grouping and minimum arguments above are written proofs.
