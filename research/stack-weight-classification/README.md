# Exact periods attainable by stack weights of cyclic shift rank at most nine

**PROPOSED, with an exhaustive finite arithmetic classification.** Let t be a periodic integer potential and set w_j=(64/81)^(9t_j). Define its rational shift rank as the dimension of the span over the rationals of all cyclic shifts of w. The possible least periods of weights of rank at most nine are exactly

    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18.

Every period on the list is realized by a two-level potential. At periods 10, 12, 14, 16 and 18 these give families of native stack directives beyond the prior complete period-nine range. The classification concerns this low-rank weight construction. Arbitrary directives of the listed periods have no rank guarantee.

## Reduction to finitely many indicator recurrences

For a weight of period p, its minimal rational shift polynomial L divides X^p−1, hence is a squarefree product of cyclotomic polynomials. The least period is the lcm of their orders. Positive weights have a nonzero constant Fourier component, so X−1 occurs. If deg L≤9, each other order d has φ(d)≤8, hence d≤128. Indeed φ(d)^2/d is the product of the factors p^(e−2)(p−1)^2 over exact prime powers p^e dividing d. All factors are at least one except the factor 1/2 from 2^1. This also gives the bound at d=1.

Every individual level indicator of t satisfies L. To see this, clear the least occurring power in any individual row of L(S)w=0. One gets a polynomial identity at R=64^9/81^9 whose integer coefficients are grouped sums of coefficients of L. All roots of L have modulus one, giving a sum of absolute coefficients at most 2^9. A nonzero integer polynomial with such coefficients cannot have R as a root: after removing a power of X its nonzero constant coefficient must be divisible by 64^9. Thus each grouped coefficient is zero. Conversely if disjoint level indicators satisfy L, their weighted sum does.

The [exact enumerator](../../experiments/stack-weight-classification/classify.py) constructs all 91 choices of a cyclotomic product containing X−1 and having degree at most nine. For each L of degree h let P be the lcm of the orders. Every binary solution is determined by its first h bits because L is monic. Enumerate 2^h seeds, discard a seed as soon as the rational recurrence leaves {0,1}, and check periodic closure. To test multilevel weights, choose disjoint binary solutions as level sets. Their union can be completed by its complement since the constant function also satisfies L. The resulting partition has period P exactly when its selected masks jointly break the shifts P/p for every prime p dividing P. The enumerator tests this finite cover condition, and also skips spaces in which the lcm of all available mask periods is too small. This covers every periodic integer potential regardless of the sizes or number of its levels.

[Exact periods, orders and binary witnesses](../../experiments/stack-weight-classification/classification.json). An independent [residue-count verifier](../../experiments/stack-weight-classification/verify.py) checks every reported witness and enumerates *all* binary words at each period through 16. Its spectral test uses character orthogonality: the sum of squared Fourier coefficients over characters of order dividing d is d times the sum of squared residue-class counts modulo d. Subtract the energies for proper divisor orders to test exact order d.

## Native consequence

Apply the [degree-nine delayed stack Padé proof](../stack-period-ten/PROOF.md) with L the shift polynomial above, normalized to constant coefficient one. A cyclotomic product is reciprocal up to a sign and has leading coefficient ±1. Those are the exact properties used in the reversed product and its first tail coefficient. For a binary witness and any d≥3, use positive increments d_j=d+t_j−2t_(j−1)+t_(j−2). The least period agrees with the mask's: a periodic difference of two translates with vanishing second difference is constant, and its sum over a period is zero.

Without any restriction on the initial phase, the height exponent of the native series is

    H_j=A binom(j,2)+Bj+9(t_j−t_0),
    A=9d,   B=9m+9d+1−9(t_0−t_(−1))>0.

The fixed factor T^(−9t_0), T=64/81, preserves irrationality. Take h=deg L≤9, D=hn, M=37n/2 and n positive even as in the cited proof. Replace 9 by h in the degree, error and height contributions from the denominator polynomial (the native coefficient 9t remains unchanged). The sum of absolute coefficients of the product in n factors is at most 2^(9n), a subquadratic contribution to the logarithmic height. In the reversed product the leading bracket has valuation 54t_(j−D), strictly below 6A, just as in the degree-nine proof. The limiting lower bound for the error-to-height ratio is

    log_81(64) · ((39/2)^2−h)/((37/2)^2+h).

It is smallest at h=9, where it exceeds one. The rational-target contradiction and the nonzero first tail valuation therefore apply to every displayed witness, every starting height m≥0, and every finite positive steering prefix. This proves an all-height exclusion for the indicated families. The stack interface is source-pinned in the linked proof. No ordinary Collatz conclusion follows for an orbit outside these families.

Replay from the repository root with Python 3.10 or newer:

    python -B experiments/stack-weight-classification/classify.py
    python -B experiments/stack-weight-classification/verify.py
