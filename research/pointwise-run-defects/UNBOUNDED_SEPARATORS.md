# Sparse interruptions of maximal growth on an ordinary orbit

**PROPOSED, ineffective.** Let U(x) be the positive odd part of 3x+1 and a(x)=v₂(3x+1). A run from x comprises r successive letters 1 followed by one letter a≥2, called its separator. Runs of length zero are allowed. Fix m≥1, and take the first m successive runs starting at an odd x. Their lengths satisfy

    Σ_(i=1)^m r_i ≤ (1+o_m(1)) log₂(x+1)            as x→∞,             (1)

uniformly over the separator valuations, which have no prescribed upper bound. This strengthens the [bounded-separator estimate](../unsafe-return-weights/VALUATION_ONE_RUNS.md). That result already supplies near-equality with bounded separators. On each fixed escaping positive odd orbit y_j=U^j(y₀) we now obtain the count bound

    #{i<j : a(y_i)≥2}/log(j+2) → ∞.                                    (2)

A single large valuation counts only once in (2). These estimates allow zero limiting density of the separators. In particular they do not establish negative long-term drift or rule out divergence.

## Integral endpoint equations

Every run is finite. If x_i starts the ith run, let b_i=(x_i+1)/2^(r_i+1), a positive odd integer. Indeed each letter one replaces x+1 by 3(x+1)/2 and occurs precisely when x=3 mod 4. With a_i the separator at the end of run i, for i<m write

    A_i=2^(a_i+r_(i+1)),  B_i=3^(r_i+1),  d_i=2^(a_i−1)−1.
    A_i b_(i+1)=B_i b_i+d_i.

Composition gives Y=X+Σ_i E_i, where

    Y=b_m ∏_i A_i,   X=b₁ ∏_i B_i,
    D_i=(∏_(v<i) A_v)(∏_(v>i) B_v),   E_i=d_i D_i = P_i−N_i,
    P_i=2^(a_i−1)D_i,                  N_i=D_i.

All products here range over 1≤i<m unless their ranges are displayed. All terms are positive integers before subtracting. The largest term Y and every term have logarithm O_m(log(x₁+1)). In fact log(x_(i+1)+1)≤log(x_i+1)+(r_i+1)log(3/2), r_i≤log₂(x_i+1), and a_i≤log₂(3z+1) for the last state z of that run, with z+1=(3/2)^r_i (x_i+1). A bounded value of any x_i fixes its remaining finite ordinary trajectory for the fixed number of runs.

Prove (1) by induction on m. It holds immediately for m=1. On a sequence violating it by a fixed relative excess with x₁→∞, pass to a subsequence so each x_i is constant or tends to infinity. If some x_i is constant, discard the bounded remaining run sum and apply the induction hypothesis up to run i−1. Henceforth all x_i tend to infinity. In particular E_i/X→0 simultaneously for each i. Indeed dividing an individual recurrence by B_i b_i gives

    d_i/(B_i b_i) = d_i/(2^(a_i−1)(x_(i+1)+1)−d_i) ≤ 1/x_(i+1).

The composite ratio Y/X is the product of 1+d_i/(B_i b_i), tending to one. All E_i are positive, so E_i≤Y−X=o(X), and P_i≤2E_i, N_i≤E_i.

## Eliminating exact relations between the offset terms

All P_i,N_i are rational S-units for S={2,3,∞}. Order the terms as N₁,P₁,N₂,P₂,…,N_(m−1),P_(m−1). Their 2-exponents strictly increase, while their 3-exponents weakly decrease, with a drop between successive pairs. By subsequence extraction for every difference of 2- or 3-exponents, a difference of fixed sign is eventually constant or has absolute value tending to infinity. Two terms therefore have a fixed rational ratio or one of their prime-exponent differences becomes unbounded, precluding a constant ratio on any further infinite subsequence. The classes of fixed ratios are **contiguous** by the two monotonicities. Replace the signed terms in each class by their sum, deleting zero sums. Each retained sum F is an integer and a fixed nonzero rational times any class member.

The first class survives with |F|₂=1: it contains the odd N₁ and all other terms are even. The last class survives with |F|₃ bounded below along the subsequence. It ends in P_(m−1), so contains whole positive pairs P_i−N_i, possibly preceded by one positive unpaired P_i. Its sum is strictly positive and a fixed rational multiple of P_(m−1), which is a power of two. These conclusions also apply if the first and last classes coincide. Every retained |F| is o(X).

There can be no fixed nonzero rational linear dependence among the surviving F on an infinite subsequence. In a contrary relation take a minimal vanishing subsum, fixing the choice on a further subsequence. Divide by one participating term: all ratios belong to a fixed finitely generated multiplicative group of rationals (include the finitely many class constants). The nondegenerate S-unit equation has only finitely many solution tuples. Taking a subsequence gives a constant ratio between different classes, contrary to construction. This is the qualitative nondegenerate conclusion of [Evertse, Schlickewei and Schmidt, Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04). The dominance |F|=o(X) then forbids any fixed dependence involving X as well.

## Subspace bound

Write the retained integers as coordinates (X,F₁,…,F_s) of dimension n=s+1≥2 and take as one extra form their sum Y. Any n of these n+1 rational forms are independent. At each of infinity, 2 and 3 omit a largest-absolute-value form, taking a further subsequence to fix choices. Before omission the product of absolute values over these three places and all n+1 forms is ≤C b₁b_m: the F_i are fixed rational multiples of S-units, while X and Y each cost no more than their respective integer factors b₁ and b_m by the product formula. At infinity a maximal form is at least Y; at 2 and 3 maximal forms are bounded below by the first and last retained classes. The remaining product is therefore at most

    C' b₁ b_m/Y = C' b₁ 2^(−Σ_(i<m)(a_i+r_(i+1))).

In particular if (1) fails by ε log₂(x₁+1), this is O((x₁+1)^(-ε)). The normalized product of forms is at most this bound times the projective height to power −n: outside S the coordinate maxima of integers are at most one. That height tends to infinity by X/|F₁|→∞ and is at most a fixed power of x₁+1. The [rational p-adic Subspace Theorem, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf) now gives a fixed rational dependence on an infinite subsequence. This contradicts the independence just proved.

## Counting separator positions

On an escaping orbit y_i+1≤(y₀+1)(3/2)^i. For fixed m, group consecutive runs in blocks of m, counting their terminating separators. If times i and i' start successive late groups, then (1) gives

    i'−i ≤ m+(1+o(1)) log₂(y_i+1) ≤ (log₂3−1+o(1))i.

Hence log(i'/i)≤log(log₂3)+o(1). An incomplete group multiplies the time index by at most a fixed constant (use the same complete group upper bound). Summing and then allowing arbitrary fixed m gives liminf of the quotient in (2) at least m/log(log₂3) for every m. The number of separator positions is consequently superlogarithmic even if some separator valuations are very large.
