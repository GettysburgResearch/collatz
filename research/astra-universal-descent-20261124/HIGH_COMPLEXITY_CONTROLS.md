# Exact rational controls with high parity-factor complexity

**Status.** PROPOSED mathematical construction. The reduced-denominator bound C5 in [cycles.md](cycles.md) applies where the number of distinct length-k factors, P(k), is smaller than the shortcut period A. The following construction tests whether positivity, the minimum condition and exact closure seen at finitely many primes force this hypothesis at some scale k much larger than log A.

**Theorem.** Fix a real floor H>0 and an integer M≥1. There exist arbitrarily long primitive positive rational shortcut cycles with all the following properties at once:

1. Their minimum exceeds H. Their common reduced denominator d is coprime to M.
2. There is an absolute constant C such that P(k)=A for every integer k≥C log A. This holds for all sufficiently large members of the family. The construction and proof use natural logarithms here.
3. Their actual reduced denominators satisfy d≥sqrt(D), where D=2^A−3^p, p is the number of odd letters, and D≥c_H 2^A for a constant c_H>0. In particular these cycles are genuinely nonintegral, even though every phase is integral at every prime dividing M.

A positive rational with odd denominator follows the shortcut even or odd branch according to the parity of its reduced numerator. The examples use both letters. They are not orbits starting at ordinary positive integers.

## Clocks and the minimum

Let M0 be the largest divisor of M coprime to 6. Choose L≥1 such that 2^L and 3^L are both 1 modulo M0. Use L=1 if M0=1. Put p=Ln+1 and A=L ceil(p log_2(3)/L). Irrationality of log_2(3) implies the fractional parts of p log_2(3)/L=n log_2(3)+log_2(3)/L visit every open subinterval of (0,1) infinitely often. Choose a fixed nonempty open band

    0 < λ1 < Λ=A log 2−p log 3 < λ2 < log(1+1/(3H))

with λ2<L log 2. One may choose λ1,λ2 depending only on H by imposing λ2<log 2. This gives arbitrarily large A with q=p/A tending to a=log(2)/log(3), and D=(1−exp(−Λ))2^A≥(1−exp(−λ1))2^A. Further, D≡−2 modulo M0, and gcd(D,6)=1. Thus gcd(D,M)=1.

For any cyclic binary word of those totals the complete affine map is (3^p x+B)/2^A. Its unique fixed point is B/D>0. The value at each cut equals B_rot/D>0. The parity of B_rot is the initial bit: in the affine expansion only an odd branch at the first step contributes an odd term, and subsequent odd multipliers preserve that parity. Hence the rational phases exactly realize the prescribed shortcut word. Since 2 and 3 are units at primes dividing D, every phase has the same reduced denominator. At any such prime, a negative valuation of x is unchanged by either x/2 or (3x+1)/2.

The minimum m occurs at an odd step, since an even step strictly decreases. Multiplying the step ratios around the cycle therefore gives

    Λ = sum over odd phases x of log(1+1/(3x)) ≥ log(1+1/(3m)).

Our choice of λ2 implies m>H **for every word** of these totals. This selection controls the location of the minimum in the positive rationals without assuming ordinary integrality.

## A word with no long repeated factors

For large A one has max(q,1−q)≤3/4. Start with A independent Bernoulli-q letters on a circle. Given two distinct positions, the probability of equal length-ℓ factors is at most (3/4)^ℓ when ℓ<A/3. For disjoint factors condition on the letters of the first one. For overlapping factors orient the shorter separation s<ℓ in the forward direction from the first start to the second and cut the circle outside the union. The union has s+ℓ<A positions. For equality it must be s-periodic there. After specifying its first s letters, each of the following ℓ letters is forced by an earlier letter; each match has conditional probability at most 3/4.

For q=p/A the weight p is a mode of the binomial distribution (compare the ratios of consecutive probabilities). Its probability is at least 1/(A+1). Conditional on exactly p ones we therefore have

    Pr(any repeated length-ℓ factor) ≤ A²(A+1)(3/4)^ℓ.

Taking ℓ=ceil(16 log A) makes the right side less than 1 for large A. Choose a word with the prescribed totals and no repeated cyclic length-ℓ factors.

## Exponential reduced denominator from one adjacent swap

Rotate this chosen word so that a pair 01 lies inside the linear presentation. Let w0 denote the word and w1 the result of switching that pair to 10. Both have the same clocks. If the pair follows j letters and h odd letters occur after it, the two full affine numerators differ by ±2^j 3^h. Indeed the pair maps are (3x+2)/4 and (3x+1)/4. The difference is a unit modulo D. Thus for g_i=gcd(D,B_i) the integers g0 and g1 are coprime divisors of D. With d_i=D/g_i,

    d0 d1 = D²/(g0 g1) ≥ D.

At least one of the two cycles has d≥sqrt(D). For large A this exceeds 1. Both still have minima above H and denominators coprime to M.

Changing two letters preserves saturation at a slightly larger length K=5ℓ+4<A for large A. If two distinct length-K factors in the changed word were equal, the corresponding factors in the original would disagree in at most four places. At most four positions can split K letters into at most five matching runs. At least one run has length ℓ, contradicting distinctness of the original length-ℓ factors at those two shifted positions. Thus the new word also has P(K)=A. The property persists at every larger length, and it rules out a smaller period. This proves the theorem.

## What would have to use the full integer equation

Taking M divisible by every prime below a prescribed bound puts all bad primes beyond that bound. There is also an exact integer variant for a different map. Choose any positive odd multiple c of d satisfying c≡1 mod M; since d is odd and coprime to M this is possible by inverting d modulo 2M. Scaling each rational phase by c gives a positive integer cycle of the same parity word for the even step z/2 and odd step (3z+c)/2. This observation concerns the parameter c, which exceeds 1 for the chosen examples.

For the original parameter 1, complete ordinary closure requires D dividing B. The adjacent swap forces a large denominator on at least one branch and says nothing about which branch an actual integer orbit could follow. No inference from D dividing B to low word complexity, or to a separate contradiction on the high-complexity branch, has been established. Counting the approximately 2^(A H_2(p/A)) words of fixed weight does not bound their mass on the single zero residue modulo D. The usual binary parity bijection is modulo 2^A.
