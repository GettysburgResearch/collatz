# Deterministic descent for a bounded number of repeated parity words

**PROPOSED, ineffective.** Let T(n)=n/2 at even inputs and (3n+1)/2 at odd inputs. A length-L trajectory from a positive integer n has parity word listing its L successive input parities, with endpoint T^L(n). Suppose this word is a concatenation

    G₀ W₁^(e₁) G₁ W₂^(e₂) … W_m^(e_m) G_m.

Each W_i is a nonempty binary word, e_i≥1 is any integer, and the G_i are arbitrary possibly empty binary words. Put B=Σ|W_i|+Σ|G_i|. For every fixed m and ε>0 there exists K_(m,ε)<∞ such that either

    L ≤ (1+ε)log₂(n+1),    or
    min_(0≤j≤L) log₂(1+T^j(n)) ≤ K_(m,ε)(B+1).                        (1)

In particular, if B is bounded and the clock exceeds the native bit horizon by a fixed proportion, the path hits a fixed finite range. If B=o(log n), the minimum is n^o(1). The base words, the intervening words and all their exponents can vary with n. The estimate is pointwise. It provides no compression bound for a general escaping parity word. The arithmetic input is the rational p-adic Subspace Theorem; the argument uses no statistical Collatz theorem. [Evertse, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

In fact an ordinary segment without repeated states obeys the stronger native-horizon inequality

    L ≤ (1+ε)log₂(n+1) + K′_(m,ε)(B+1).                                 (2)

Thus any violation of (2) forces an actual state repetition in the tested segment and proves its ordinary source eventually periodic. If n is on an escaping orbit, (2) holds at every starting phase and every finite horizon. The sharpening follows below from the same separation proof.

## Reduction to separated large powers

Suppose (1) fails along a sequence on which L>(1+ε)log₂(n+1) and the minimum log height divided by B+1 tends to infinity. In particular B=o(log n) and n tends to infinity. With m fixed, pass to a subsequence where each powered length L_i=e_i|W_i| divided by B+1 is bounded or tends to infinity. Absorb the bounded-ratio powers into the intervening words. Their total length is O(B+1) along this subsequence. At least one large power remains. The stripped initial and final gaps have total length O(B+1) and change the relevant initial log height by O(B+1), since a positive shortcut step changes log₂(x+1) by at most one. Write x_i for the actual input at the start of large power i; the retained L_i all satisfy L_i/(B+1)→∞.

The affine map of a binary word W of width v and odd count p is x↦(3^p x+D)/2^v with nonnegative integer D of logarithmic height O(v). It has a rational fixed point ξ=D/(2^v−3^p), in the 2-adic integers, of ordinary logarithmic height O(v+1). The denominator is nonzero and odd. The elementary parity-word bijection modulo 2^v shows that ξ follows W as an actual 2-adic trajectory: integrality at the last point forces each earlier parity, since the wrong parity introduces a power of two in the denominator which subsequent odd multipliers cannot cancel. Thus the infinite parity sequence at ξ is periodic with repeated word W.

Write ξ_i for these fixed points and Γ_i for the affine map of gap G_i between successive retained large powers, with slope λ_i=3^(#ones in G_i)/2^|G_i|. The rational c_i=Γ_i(ξ_i)−ξ_(i+1) has logarithmic height O_m(B+1). If c_i=0, the gap is followed legally by the 2-adic ξ_i and arrives at ξ_(i+1). Hence W_i^(e_i) G_i W_(i+1)^(e_(i+1)) is a single segment of the infinite periodic parity sequence at ξ_i. Replace it by complete powers of W_i and its trailing prefix of length <|W_i|. Move this prefix to the next gap, or strip it at the end. This preserves the actual ordinary segment, enlarges the gap budget by O(B+1), and reduces the number of large powers. Extracting subsequences for the finite choices, repeat until either one large block remains or all inner c_i are nonzero. The resulting large powers still have L_i/(B+1)→∞, their combined length is L−O_m(B+1), with constants allowed to depend on this contrary subsequence, and every true boundary state has log height growing faster than B+1.

## The ordinary congruences and rational forms

Define b_i=(x_i−ξ_i)/2^L_i. It is positive eventually. Its reduced denominator divides the odd denominator of ξ_i, hence is at most 2^O(B+1): the actual exit of this power equals ξ_i+3^(e_i p_i)b_i and is an integer, so b_i is 2-adically integral. This odd-denominator bound gives b_i≥2^(-O(B+1)). If one power remains, taking logarithms of 2^L₁ b₁=x₁−ξ₁ already contradicts the excess in L.

Otherwise set A_i=2^L_(i+1), C_i=λ_i 3^(e_i p_i). For i before the last large block the exact relations are

    A_i b_(i+1)=C_i b_i+c_i.

Writing j for the number of retained powers, compose to obtain

    Y=X+Σ_(i<j) E_i,
    Y=b_j ∏_(i<j) A_i,   X=b₁ ∏_(i<j) C_i,
    E_i=c_i (∏_(v<i) A_v)(∏_(i<v<j) C_v).

One has c_i/(C_i b_i)→0 since C_i b_i=x_(i+1)−ξ_(i+1)−c_i, and the absolute sizes of c_i and ξ_(i+1) are at most 2^O(B+1) while log₂ x_(i+1)/(B+1)→∞. By composition all E_i/X tend to zero in absolute value (multiply this local ratio by the product of 1+c_v/(C_v b_v) for v<i). Meanwhile

    v₂(E_(i+1))−v₂(E_i) = L_(i+1)+O_m(B+1) → ∞.

In any proposed fixed rational dependence involving X and the E_i, ordinary dominance first removes X. For the remaining terms the smallest participating 2-adic valuation is then uniquely attained for all large indices, impossible. Thus the retained coordinates (X,E₁,…,E_(j−1)) cannot have a fixed rational dependence on any infinite subsequence.

Add Y, their sum, as one extra linear form. Any j among the j+1 forms are independent. At each of infinity, 2 and 3 omit a form of largest absolute value. Pass to a subsequence with fixed choices. Before omission the product of all these values is at most 2^O_m(B+1) b₁ b_j: rational powers of 2 and 3 cost one across these places; each c_i costs at most its height and each b_i costs no more than its ordinary size times its denominator. At infinity a maximal form is at least Y; at 2 the first E_i and at 3 the last E_i have absolute value at least 2^(-O_m(B+1)). After omission the product therefore costs at most

    2^O_m(B+1) b₁ b_j/Y ≤ 2^(log₂(n+1)−L+O_m(B+1)).

For normalization, multiply all coordinates by a common positive integer to clear denominators at primes outside 2 and 3. One of size 2^O_m(B+1) suffices, since the unit powers create no outside denominator and all other factors have the denominator bounds above. This changes the displayed product by at most 2^O_m(B+1). The product of local norms over these three places is now at least the projective height H. The normalized product of selected forms is at most H^(−j) times 2^(−c_ε L). The height H tends to infinity (use |X/E₁|→∞) and is at most 2^O_m(L), from the formulas and the one-step positive-state height bound. The rational p-adic Subspace Theorem forces a fixed linear dependence on an infinite subsequence, contradicting the preceding separation. This proves (1). The theorem gives no computable K here.

## Removing the low-state alternative on a simple segment

For one retained block of length L_i=e_i|W_i| from the ordinary state x_i, the rational congruence b_i=(x_i−ξ_i)/2^L_i has odd denominator at most 2^O(|W_i|). If b_i=0, then x_i equals the fixed point of W_i. Its actual trajectory returns to x_i after |W_i| steps, a repeated state within this segment. Otherwise the congruence gives

    log₂(x_i+1) ≥ L_i−O(|W_i|+1)

by comparing the nonzero integer numerator of x_i−ξ_i to its ordinary size. This holds without a positivity or largeness premise on x_i−ξ_i (use |x_i−ξ_i|≤x_i+|ξ_i|). Equivalently multiply the congruence by the fixed-point denominator |2^|W_i|−3^(#ones)|: its nonzero integral numerator has absolute value at least 2^L_i and at most 2^O(|W_i|)(x_i+1).

If (2) fails on simple segments, pass to a sequence with [L−(1+ε)log₂(n+1)]/(B+1)→∞. In particular B=o(L). Make exactly the same short-power absorptions and compatible-period joins as above. The retained large powers still have L_i/(B+1)→∞. The individual congruence now implies log₂(x_i+1)/(B+1)→∞ for every retained boundary, including the final retained block. Since the initial gap costs O(B+1) in log height, the same holds for n; thus B=o(log n) as well. The argument with b_i>0 and X dominant used only the boundary heights, never the minima inside the powers. It therefore applies unchanged. Its exponentially small product bound contradicts the Subspace Theorem because L>(1+ε)log₂(n+1) and B=o(L). This proves (2).

At a strict future minimum on a hypothetical escaping orbit, or at any other phase of that orbit, a parity window of length at least (1+2ε)log₂(n+1) consequently has B bounded below by a positive fraction of its length in every fixed-m description. In contrast, (1) applies also to a self-intersecting segment.

## Allowing the number of powers to grow

For each η>0 there is C_η such that any simple segment with k powered pieces satisfies

    L ≤ C_η exp(η k) (log₂(n+1)+B+1).

Indeed, fix ε=1 and choose m so large that log(1+2 log₂(3/2))/m < η. Split consecutive powers into groups of m (the final group may be shorter), assigning each gap to exactly one group. For a group starting at time t, log₂(x_t+1)≤log₂(n+1)+t log₂(3/2), by the one-step bound on x+1. By (2) its length is at most 2 log₂(x_t+1)+K_m(B_group+1), taking the maximum of constants over all group sizes up to m. The successive end times therefore satisfy an affine recurrence with multiplier 1+2 log₂(3/2). Summing the geometric series and using Σ B_group=B yields the claim; a gap-only segment has L=B. In particular for every simple family with L/(log₂(n+1)+B+1)→∞, the number of powers divided by the natural logarithm of that ratio tends to infinity.
