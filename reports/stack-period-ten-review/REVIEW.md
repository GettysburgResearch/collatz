# Independent reconstruction of the period-ten pulse family

**VERIFIED at the narrow frozen claim level.** Reviewed source is the
author's local checkpoint `00d1dce637e7bc824a48f9e717d1fbf9ba2a1f35`,
`research/stack-period-ten/PROOF.md`, Git blob
`1df4d1984e9963880ec92b51c72b3e49c2f7acdd`.
This review concerns the two-slot potential at residues 1 and 2 modulo 10,
integer drift d>=2, integer initial stack height m>=0 and arbitrary finite
positive steering prefix. It establishes irrationality in the two-adic
stack context for that family. It does not extend to all period-ten words.

The normalization sources are PR 20,
`82ca2f932438a9fe0897704ba62959ca23ec830f`,
`research/padic-repetition/claims/L-9407-stack-partial-theta-normal-form.md`
(L-9407, context affine relation) and
`research/padic-repetition/claims/L-9408-s-adic-transfer-polynomials.md`
(L-9408, finite prefix transfer). I reconstructed the following steps
directly from the asserted increment word and Padé coefficients.

1. Summing the second differences once gives m_j=m+dj+t_j-t_(j-1)
   because t_0=t_(-1)=0. The second sum gives
   H_j=9d binom(j,2)+(9d+9m+1)j+9t_j. The minimum increment is d-1.
   The two positive excesses in positions 1 and 4 cannot be preserved
   by shifts 1, 2 or 5, excluding every proper divisor period.
2. L(S)w=0 holds in the ten-dimensional cyclic phase space. Both parity
   classes have the multiset consisting of one T^9 and four ones. For
   j>=9n the convolution runs over the full denominator, and the exact
   difference of the three quadratic exponents is -jk. The product of
   commuting shift polynomials consequently vanishes at each of the n
   advertised consecutive coefficients. The choice M=37n/2>9n ensures
   the convolution is complete throughout this window.
3. For j>=M+n the unique least q exponent in the product comes from selecting
   the degree-nine term in every factor. Each different selection raises
   the q exponent by at least one; this gains at least 9d T-powers while
   the accompanying phase weight can lose at most 9. Thus the leading
   term has unit coefficient and phase t_(j-9n). At j=M+n its exponent is
   A[binom(M+n,2)-9n(n+1)/2]+B(M+n)+9t_(M-8n). The increment to the next
   j is at least A(j-9n)+B-9>0. This verifies (3) including survival at
   Y=1 and actual nonzero error.
4. A positive-degree denominator term contains z^k, and all net q
   exponents are nonnegative since k<=9n<M. Hence V(1) is a two-adic
   unit. For a numerator monomial below M the remaining q exponent is
   binom(j,2)+(M-j)k+u with k<=j and u<=9binom(n,2).
   The first two terms are at most binom(M,2), using
   binom(M,2)-binom(j,2)-(M-j)j=binom(M-j,2). The same cap without the
   convolution holds for denominator terms. Counting raw expanded terms
   gives the stated factor (M+1)10^n; no cancellation or unproved
   denominator saving is assumed.
5. The exact quadratic ratio is (39²-36)/(37²+36)=297/281.
   The strict integer margin in the source verifies exponent >1.
   Rationality of the target would make the nonzero cross-multiplied
   ordinary integer larger in its forced two-divisibility than its
   archimedean bound allows. The transfer through a finite prefix has
   nonzero rational multiplier. The affine context relation has nonzero
   rational multiplier as well.

The [independent checker](check.py) constructs exponents by summing the
actual increments and multiplies the denominator by the original series in
the integer polynomial ring. Exact coefficient cancellation is tested before
any specialization at T=64/81. Orders 2 and 4 at two drifts/heights cover
254 coefficient polynomials. A single exceptional slot breaks the advertised
window as expected in a separate 44-coefficient control. These finite
checks accompany the all-even-order proof reconstructed above.
