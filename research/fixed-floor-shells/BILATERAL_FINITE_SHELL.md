# A power-saving shell comparison for all-depth least predecessors

**Proposed, conditional on the cited density exponent.** Write B_j for the odd positive n that are the least positive ordinary predecessor of U^j(n), with paths of any depth allowed, and b_j for the relative odd natural density of B_j. For an odd target its least predecessor is odd, since an even source has a smaller odd core on its route. Uniformly for integers 0≤j≤10^(−6) log₂ X,

    #{odd n∈[X,2X] in B_j} / #{odd n∈[X,2X]} = b_j + O(X^(−1/100000)).       (1)

The big-O constant is absolute. The stated exponent is explicit; the proof does not give a numerical onset. For every fixed 0<ε≤10^(−6), at j=floor(ε log₂ X) the unnormalized count is consequently

    X^[1−ε(1−h)log₂3+o(1)],       h=H₂(log₃2),

where H₂ is binary entropy. This gives the exact power of X for an ordinary growing forward clock with every reverse depth retained. It uses the fixed-depth density exponent in the [bilateral dimension theorem](BILATERAL_DIMENSION.md) and the [FS-016 all-comparable-first-hits estimate](QUANTITATIVE_PRESSURE.md).

Paper 152 gives a constructive polynomial lower count through the longer horizon floor(log₃X), retaining competing depths up to the reference depth. Its rate upper bound is the ballot exponent that appears in the bilateral dimension theorem. The comparison here retains all incoming depths and obtains the exact exponential rate on the smaller physical clock above. [Paper 152 v1](https://rstation.ai/problems/collatz/papers/152/v1)

## The only forward words to consider

For a forward word w of j positive exponents let A_i be its cumulative total at i, P_i=3^i/2^A_i, and t_i=U^i(n). If n∈B_j, every t_i, i≤j, is at least n, since each reaches t_j. Therefore

    1 ≤ t_i/n = P_i ∏_(0≤a<i)(1+1/(3t_a)) ≤ P_i exp(i/(3X)).

If P_i<1, the integer gap gives 1/P_i−1≥3^(−i), whereas exp(i/(3X))−1<3^(−i) on the stated clock range for large X. Thus we may assume every P_i≥1. The same restriction holds in the [symbolic word selection identity](BILATERAL_MINIMUM.md), because resistance at clock j protects earlier clocks and the empty competitor at i tests P_i. For j>0 the number of candidate words is at most

    Σ_(A≤floor(j log₂3)) binom(A−1,j−1) = binom(floor(j log₂3),j) ≤ 3^j.

For j=0 there is just the empty forward word. In either case each chosen word specifies one dyadic class of odd starts modulo 2^(A_j+1).

## A common finite reverse cutoff

Put M=ceil(0.51 log₂ X). At fixed w test reverse words v of total S≤M, including the empty word. With q their length and B_v their positive affine offset (zero for the empty word), their ordinary source is

    x = ρ n + (ρ/P_j)(B_w−B_v),       ρ = 3^(j−q) 2^(S−A_j).

Both offsets are at most (3/2)^M by summing inverse prefix multipliers. If ρ≠1 its reduced numerator is at most 3^j 2^M. Thus ρ/|1−ρ|≤3^j 2^M, and the translation cannot alter the sign of x−n, since P_j≥1 and 3^(j+M)<X. If ρ=1 the sign is exactly that of the constant translation. Ternary legality on a positive odd target gives a positive odd source. For the chosen w all these tests form one union of classes modulo 3^M in the source variable, since the target affine expression divides only by a power of two. The ternary classes are counted along the dyadic progression with error O(3^M) per word. After division by the odd shell size and summing over the at most 3^j words, the finite shell proportion differs from the finite Haar selection sum by O(3^(j+M)/X). Here the Haar sum weights each word by the usual relative odd probability 2^(−A_j).

For the symbolic infinite-depth tail, a rival of total S>M can matter only if its inverse-tree weight 3^q/2^S≥P_j≥1. In particular q>M/log₂3. Under Haar on unrestricted ternary targets a specified word of depth q has legality probability 3^(−q). Put λ=3/2 and p(a)=(2^λ−1)2^(−λa). For L=q log 3−S log 2≥0 one has

    3^(−q) = p(v) exp(−λ L−κq),       κ=log((2√2−1)/√3)>1/25.

The sum over such words at fixed q is at most exp(−κq), since p is an iid probability law. At fixed w the target from a Haar ternary origin is uniform on one depth-j cylinder, so the union bound for omitted competitors costs at most O(3^j exp(−κM/log₂3)). This remains the total error after averaging over w, whose weights sum to at most one. The unrestricted Haar sum equals b_j by the fixed-clock ordinary transfer in the [bilateral minimum theorem](BILATERAL_MINIMUM.md). These arguments retain all equal-slope cases.

Finally each relevant ordinary target lies in [X,3X(3/2)^j] using the same offset bound and P_j≥1. Cover this range by shells [Y,2Y] with lower endpoints X,2X,4X and so on. With the exception of O(Y^(1−1/20000)) targets per shell, FS-016 guarantees that every x≤2X≤Y^(1+1/10000) reaching the target does so within floor((log₂Y)/2)≤M shortcut steps. For odd endpoints this first-hit clock is exactly the total valuation. It suffices to count the exceptional targets for each fixed w because n↦U^j(n) is injective on its dyadic class. In relative odd measure the error is therefore

    O(3^j(1+log X) [3X(3/2)^j]^(1−1/20000)/X).

The exponent gain before the logarithm is at least 1/20000−10^(−6)(log₂3+log₂(3/2))>0.000047. The earlier CRT error has gain greater than 0.19, and the Haar-tail bound has gain greater than 0.01. All are O(X^(−1/100000)), proving (1). The desired density itself is X^[−ε(1−h)log₂3+o(1)] by the bilateral dimension theorem; its exponent loss is at most ε log₂3<1/100000. The error in (1) is therefore smaller, which proves the asserted count.
