# An exclusion criterion for nonperiodic stack increments

**PROPOSED.** A directive may switch among unrelated patterns, and its heights may grow without bound. A single sufficiently long matching interval at each of infinitely many scales obstructs rational ordinary initialization. The comparison is in the native stack series at the actual past height of each interval.

Put T=64/81, take m_0≥0 and positive integer increments, and define m_j and H_j as in [the period-ten proof](../stack-period-ten/PROOF.md). The native completion requires Θ=Σ_{i≥0} T^(H_i) in the 2-adic field. Suppose there are triples (k,n,d), with n tending to infinity and d≥3, such that:

* Starting just after k, the next 18n increments have the form d+t_j−2t_(j−1)+t_(j−2), indexed locally by 1≤j≤18n.
* Here t is a periodic binary mask whose weight T^(9t) has shift rank h≤9. The mask, phase, d, and starting index may change with the triple.
* The accumulated past height obeys H_k≤9d n².

Then Θ is irrational in the 2-adic field. This includes genuinely nonperiodic directives; no bound on the size or number of previous changes is assumed.

**Height of the actual tail if Θ were rational.** Write Θ=a/b in lowest terms. Since its 2-adic value is integral, b is odd. For the native tail Θ_k=Σ_{j≥0}T^(H_(k+j)−H_k), splitting off the first k summands gives

    b Θ_k = [81^(H_k) a − b Σ_{i<k}64^(H_i)81^(H_k−H_i)] / 64^(H_k).

The left side is a 2-adic integer, so the right side is an ordinary integer. As the H_i are strictly increasing, their real T-power sum is bounded by 1/(1−T). Thus the numerator and denominator of Θ_k in reduced form have magnitudes bounded by C(81/64)^H_k, for a constant depending only on the fixed putative rational Θ. This retains the gain from cancelling the entire displayed power of two.

**One finite matched interval.** Use local A=9d and B=9m_k+9d+1−9(t_0−t_(−1))>0. Multiply Θ_k by T^(9t_0), a factor of bounded rational height, to remove the constant shift in the quadratic exponent. In the periodic comparison series F the coefficients at Y=1 are w_j T^(A binom(j,2)+Bj), w_j=T^(9t_j). Use the denominator proof in the linked packet with M=17n, D=hn and j_0=M+n=18n. Its reciprocal shift polynomial, normalized to constant one, has degree h and sum of absolute coefficients at most 2^h. Thus V(1) is a 2-adic unit and the comparison quotient has exact error valuation

    E=6[A(binom(18n,2)−h n(n+1)/2)+18Bn+9t_(18n−D)].

The actual series and the comparison have identical terms through j_0. Their omitted later terms have valuations strictly larger than E for all sufficiently large n: their increasing exponents already reach A binom(18n,2)+18Bn+9t_(18n) at the shared last term. The leading gap to E grows at least as 6[A n(n+1)/2−9]. Therefore the exact same finite nonzero error valuation E holds for the actual scaled tail. No step uses the real embedding of that tail as the value of the putative rational.

The rational approximant has height at most (17n+1)2^(9n)81^K with

    K=A[binom(17n,2)+h binom(n,2)]+17Bn+9.

The proof bounds every monomial of the two polynomials before evaluation. All constants in this bound are independent of m_k,d and the mask. For a nonzero difference of rationals with odd denominators, its valuation cannot exceed the base-two logarithm of twice the product of their heights. Write c=log₂ 81. After subtracting this bound from E and using H_k≤A n², the coefficient of A n² is at least

    [6(18²−9)−c(17²+9)]/2 − (c−6) = 951−150c > 0.

The strict inequality is the integer comparison 81^50<2^317. The coefficient of Bn is 108−17c>0. Terms of order A n+n+log(n+1)+1, with uniform constants, cannot offset the strict quadratic gain because A≥27. The rational target would violate the integer height bound, a contradiction.

For an explicit family, use constant increments 3 except at infinitely many isolated positions where the increment is 4. Choose those positions recursively so that after each exceptional step at index k the next 18n increments equal 3 for some n≥k with 27n²≥H_k, before the next exceptional step. The increasing gaps make these examples nonperiodic; the constant comparison mask has rank one. The criterion also allows arbitrarily chosen qualifying masks at successive visits. A balanced aperiodic directive with no such long matching intervals remains outside the proof.
