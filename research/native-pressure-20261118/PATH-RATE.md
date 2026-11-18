# Almost-sure error of order three quarters in inverse depth

Under the same two external landing and boundary estimates as the
[fixed-root strong laws](ALMOST-SURE.md), the following bounds hold
almost surely at every fixed positive odd unit root. Here f is any
fixed dyadic/ternary product-cylinder indicator, ν is the stationary
product measure, ℓ=log(4/3), and the notation is as in the strong laws.

    S_q = 2q + O(q^(3/4)),
    log X_q = ℓq + O(q^(3/4)),
    Σ_(i=1)^q f(X_i,X_i) = qν(f) + O_f(q^(3/4)),
    −log p_q = ℓq + O(q^(3/4)),     log h(X_q) = O(q^(3/4)).

The bounds are eventual. The onset may depend on the realized path;
no moment of a physical jump at fixed finite depth follows.

## Uniform bounds along a shell segment

Work first off cycle. Fix small η>0, set R_j=⌊exp((1+η)^j)⌋,
L_j=log R_j and D_j=L_j−L_(j−1). Choose η small enough that
K_j=⌊10D_j/ℓ⌋ satisfies 4(K_j+O_f(1))log 2 < L_j/2 eventually.
Here D_j is comparable to L_j with a fixed small proportionality
constant, and the landing estimate is

    P_t(Y_R∈A) ≤ C_t exp(C√log R) (|A|/R + R^(−g)).

It shows L_j−B√L_j≤log Y_(R_j)≤L_j eventually almost surely for a
sufficiently large fixed B. The dyadic counting proof for all partial
sums in the strong laws now has a moderate-deviation version.
Take error u_j=B_f L_j^(3/4). For the centered geometric sum, its
log moment generating function is at most C'θ² for |θ| small. At each
partial length ≤K_j use θ of order u_j/K_j in the Chernoff bound,
for either sign. For each bounded fixed-window arithmetic test split
into the finitely many independent residue classes and apply Hoeffding
with error u_j divided by the number of classes. The initial bounded
window loss is absorbed in the error. Union over all partial lengths
gives an exceptional Haar probability

    O_f(K_j exp(−c_f u_j²/K_j) + exp(−c K_j)).

The last term accounts for the dyadic valuation total exceeding the
4(K_j+O_f(1))-bit coding budget. The finite-interval count adds at
most 2^(4(K_j+O_f(1))) exceptional labels to R_j times this probability.
Choose B_f large enough that the resulting exp(−c_f B_f²√L_j)
beats the landing factor exp(C√L_j). The probabilities are summable.
Thus the two estimates of (3) in the strong laws hold with O_f(L_j^(3/4))
uniform partial-sum errors. Simultaneous validity for countably many
individual cylinders follows by intersection.

For m≤K_j the valuation bound implies log U^m Y_(R_j)≥
L_j−O(√L_j)−(2K_j+O(L_j^(3/4)))log 2, which is ≥L_j/2 eventually
by the choice of η. Thus the summed log affine correction is o(1).
The log height at forward time m is L_j−ℓm+O(L_j^(3/4)) uniformly.
Bracketing the first passage of L_(j−1) yields a segment length
D_j/ℓ+O(L_j^(3/4)). The full segment errors in the clock and the
frequency are also O_f(L_j^(3/4)). Starting from the inner end and
using a partial segment costs at most twice the uniform forward-prefix
error by subtraction. Sum these bounds through shell j. The geometric
series of errors is O_f(L_j^(3/4)), including the fixed finite path
before the bounds hold. Since inverse depth in that shell is
comparable to L_j, this proves the first three rate bounds at every q.

## Counting heavy prefixes at densely spaced thresholds

For integer k→∞ set R=⌊exp(k)⌋. The all-depth height estimate bounds
the last-below-R depth n(R) by k/ℓ+O(k^(3/4)) on both sides: times
below the lower end of that bracket have log X_i≤k and all times
beyond its upper end have log X_i>k after increasing the constant.
Thus n(R)≤2k/ℓ eventually, and consecutive such depths have gap
O(k^(3/4)). Across all depths ≤2k/ℓ there are at most
O(k exp(k−B√k)) terminal labels whose prefix has mass ≥exp(−k+B√k).
Applying the landing estimate to their labels ≤R gives summable
probabilities for B>C+1. Eventually the realized prefix information
at n(R) exceeds k−B√k. Its monotonicity then gives
−log p_q≥ℓq−O(q^(3/4)) at every q. The reverse upper bound follows
from the clock estimate, the positive lower bound for h, and
p_q=3^q 2^(−S_q)h(X_q)/h(t). The same identity proves the bound
on log h. Periodic roots again reduce to their almost surely finite
exit from the cycle.
