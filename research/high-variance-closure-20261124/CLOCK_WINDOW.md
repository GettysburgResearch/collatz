# How late an actual four-trit meeting can occur

**Written theorem.** Use the positive ordinary shortcut map T. At scale X=81^j and on the head H=[7X,8X), put m=floor(x/81). Fix 0<b<c<4/25. At every sufficiently large level there are at least a constant times X^(1−c) distinct x in H such that

    T^u(x) ≠ T^v(m)    for all 0≤u,v≤(1+b)log₂ X.

Thus for every clock coefficient strictly less than 1.16, the complement of a full unequal-clock physical meeting search is not o(X^0.84). The theorem concerns the finite search only. The infinite-time count D_j of PR197 can still vanish identically. This finite obstruction does not prove universal convergence or produce a counterexample.

## Exact ordinary starting family

Restrict x=81m+64. Take L=floor(log₂(X/81))−2, choose k=floor(c L)≥4 and prescribe 81m+65≡0 mod 2^k. For i≤k the child x specializes to −1 in the 2-adics and takes i consecutive odd steps. The parent specializes to −65/81, whose first four odd steps are −19/27, −5/9, −1/3, 0; later steps are even. At clock k exactly, with positive integer z=(81m+65)/2^k,

    T^k(m)=z,                T^k(x)=3^k z−1.

Indeed the four-odd formula is (81m+65)/16 and there are k−4 further halvings. The displayed formulas are valid on every integer lift. Restrict the m interval to one complete block of 2^L consecutive integers (its length is X/81+O(1)); the lifts in this block are uniform on the 2^(L−k) high digit strings. Their count is comparable to X^(1−c).

## One exposure, then deterministic continuation

Write P_y(i) for the number of odd inputs among the first i steps of y. Set d_i=4+P_x(i)−P_m(i), so d_k=k. Given any first i binary digits of m, both arms have an affine profile with odd free slope. Revealing the next binary digit makes the two next parities separately fair, conditionally on the same past. They may be perfectly dependent. Thus each P_y(k+t)−P_y(k)−t/2 and d_(k+t)−k is a martingale with differences bounded by 1. On a fraction 1−o(1) of the lifts, for both arms and all 0≤t≤L−k,

    |P_y(k+t)−P_y(k)−t/2| ≤ L^(2/3),     |d_(k+t)−k| ≤ 2L^(2/3).

For example apply the Azuma inequality at every t and take a union bound. This is the only probabilistic exposure. For later clocks each difference d_i can drop by at most one per step, so d_i>0 for every i up to N=floor((1+b)log₂ X), since b<c. At clocks i≤k this follows from the exact parity counts.

All states of both arms up to N exceed X^(1/3) for all sufficiently large X. For i≤k their lower bound is a constant times X/2^k. From k through L use T^t(y)≥3^P y/2^t and the lower parity bound above. The smallest resulting exponent (up to o(1)) is (1−c)log₂(3)/2, since log₂(3)/2<1. Through the final N−L steps even an uninterrupted halving loses at most b+o(1) from that exponent. The resulting (1−c)log₂(3)/2−b is greater than 1/3 throughout the stated range.

## Excluding independent clocks

For every t≤N and either arm, the exact multiplicative identity gives

    log T^t(y) = log y + P_y(t) log 3 − t log 2 + E_y(t),
    0≤E_y(t) = sum over odd input states w of log(1+1/(3w)) ≤ N/(3X^(1/3)).

The initial size ratio has log(x/m)=4log3+O(1/X). If the arms met at clocks u,v≤N, the absolute value of

    (4+P_x(u)−P_m(v))log3 − (u−v)log2

would therefore be O(N/X^(1/3)). For integer coefficients of size O(N) the fixed two-logarithm lower bound (for example Gouillon, Corollary 2.3, with bases 2 and 3) bounds the absolute value of a nonzero such form from below by (2+N)^(−C), for an absolute C. This excludes every nonzero form at large X. A zero form requires u=v and d_u=0 by unique factorization; the parity estimate rules that out. Every selected lift satisfying the estimates is therefore an actual unmerged edge up to the stated horizon. No independence of transferred partners or ability to restart the digit model is assumed.

The same proof works for larger c,b whenever 0<b<c<1 and (1−c)log₂(3)/2>b. The stated range is chosen for the sparse-edge exponent.

**Sources.** PR197, GettysburgResearch/collatz, `9ed095c3b3386d66c1dba103117e8dda0268b7aa`, `research/ayh-resource-reset-20261124/continuation/HEAD_EDGE_RIGIDITY.md` (infinite-time criterion, not a finite-clock assertion); PR146 `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md` (conditional fair parities of odd-slope profiles and paired martingales). N. Gouillon, [*Explicit lower bounds for linear forms in two logarithms*](https://www.numdam.org/item/JTNB_2006__18_1_125_0.pdf), Journal de Théorie des Nombres de Bordeaux 18 (2006), 125–146, Corollary 2.3, printed p. 128. With the positive rational bases 2 and 3 fixed, its parameter h is O(log(2+N)), giving the stated polynomial lower bound. Zero coefficients and coefficients of opposite signs have a fixed elementary lower bound instead. The arithmetic normal form and unequal-clock comparison above are derived directly.
