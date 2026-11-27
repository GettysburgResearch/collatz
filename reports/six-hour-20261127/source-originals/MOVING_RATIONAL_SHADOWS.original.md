# A height bound for moving rational shadows on an ordinary Collatz window

**Written theorem with an external quantitative Subspace Theorem.** This proof adapts the two-place argument of Weaver's Paper 15/v2 to rational tracks whose phases can move through an unrestricted collection. Its resource is the logarithm of the largest phase height. A periodic dictionary and a bound on the number of available phases are unnecessary. The proof below retains packet-specific denominator clearing and allows powers of two in that clearing denominator.

## A finite theorem for every window

The actual orbit consists of positive odd integers satisfying 2^e y=3x+1 at each step, with e≥1. Fix an integer H≥1. A shadow piece is a nonempty consecutive segment with a rational t_i=p_i/q_i at each of its clocks, with q_i>0, gcd(p_i,q_i)=1, 3∤q_i, |p_i|,q_i≤H, such that

    2^(e_i) t_(i+1)=3t_i−1,       x_i+t_i≠0.

The sign of t_i can vary. The nonzero condition propagates throughout each piece once it holds at its start. A single arbitrary physical edge also counts as one piece and needs no shadow. A decomposition into k pieces covers the entire window exactly. The graphs of the rational tracks and their denominators can change at piece boundaries.

**Theorem M.** There is an absolute effective constant K such that a length-T window starting at the positive odd integer n with such a decomposition satisfies

    T+1 ≤ exp(K (k+1)/log(k+2)) · log(n+2H+2).                         (M1)

All logarithms in estimates are natural. The empty window is allowed. There is no stopping exception at a positive cycle. The same upper bound, with a larger K, holds for the logarithm of the largest ordinary state in the window.

Set Z=x+1 and Y=x+G, with G=(2H+2)^4. Every contiguous subword of one shadow piece inherits the required data. On a subpiece of length l and division sum E its shifted displacement satisfies 2^E(x_t+t_t)=3^l(x_s+t_s). Clearing its two endpoint denominators gives 2^E | q_t(q_s x_s+p_s). Thus l≤E≤log₂[H²(x_s+1)]≤2 log₂ Y_s. A singleton satisfies the same length bound. Since Y increases by at most a factor 3/2 at each step, every segment of at most m pieces, and every prefix or suffix of that segment, satisfies

    length ≤ 3^m log₂ Y_start,       max Y ≤ Y_start^(3^m).             (M2)

Indeed one piece sends Y to at most Y³, and summing 2·3^j over its successive starts gives the length estimate.

If every state of a packet exceeds 4m(H+1), the ratio (x+t)/(x+1) lies in [1/2,3/2] at each shadow endpoint. The exact displacement then gives Z_t/Z_s≤3·3^l/2^E on that piece. On a singleton, 2^e Z_t=3Z_s+(2^e−2)≤2·3Z_s because 2^e≤3x_s+1. Therefore, on a high-state packet of at most m pieces,

    Z_t ≤ 3^m (3^l/2^E) Z_s.                                          (M3)

## The packet vector

Fix m, and allow every packet in the argument to have its own rational phases. For a shadow piece its two boundary coefficients are obtained from

    3^l Z_s=2^E Z_t+2^E(t_t−1)−3^l(t_s−1).

For a singleton use 3Z_s=2^e Z_t−2^e+2. Clear all boundary denominators in this packet by their lcm C. Then 3∤C, C≤H^(2m), and the cleared integer coefficients have absolute value at most M=2(H+1)^(2m+1). Unroll the packet. Its sum is C3^l Z_s, with positive root A₀=C2^E Z_t. Its at most 2m remaining coordinates take the form c_i 2^(A_i)3^(B_i), |c_i|≤M. The position at an internal boundary j is A_i equal to the division sum before j and B_i equal to the number of steps after j. These positions have opposite monotone orders. The singleton's two coefficients use its two boundary positions. Zero coordinates are discarded.

Each nonroot before clearing, divided by the root before clearing, has modulus at most (H+1)/Z_j, or 2/Z_j at a singleton. Indeed the shifted physical inequality 3Z_j≤2^e Z_(j+1) bounds the remaining multiplier 3^(l−j)/2^(E−E_j) by Z_t/Z_j. The high-state cutoff above therefore makes the sum of the absolute nonroots less than A₀/2. Repeatedly delete any nonempty zero subsum. Every deletion preserves the root, the sum and the two position orders. At least one nonroot remains unless the entire physical word consists of ones, since 2^E Z_t−3^l Z_s is strictly positive as soon as a letter exceeds one. An all-one packet satisfies 2^l | Z_s and Z_t=(3/2)^l Z_s≤Z_s^(log₂ 3), so it cannot raise Y past the square of its initial value. For other high packets let 2≤d≤2m+1 be the remaining dimension.

Write the gcd of the retained vector as g=2^u 3^v γ with (γ,6)=1. A retained nonroot gives γ≤M. The total gives 2^u≤2^v₂(C) Z_s and the root gives 3^v≤Z_t since 3∤C. Thus its primitive height H′=A₀/g satisfies

    H′≥2^E/(M Z_s).                                                     (M4)

The term 2^v₂(C) is needed for even shadow denominators. Each primitive nonroot is c′ 2^max(A_i−u,0) 3^max(B_i−v,0) with 0<|c′|≤M, because γ and any negative residual prime powers divide the old coefficient.

Use the coordinate forms at infinity and two. At three replace the root coordinate by the total-sum form, leaving all other coordinate forms in place. Let Q′ be the product of these local absolute values on the primitive vector, without projective normalization. If rough(n) removes all factors of two and three, direct multiplication before primitive scaling gives

    rough(C 2^E Z_t) · product_i rough(c_i)
      · 3^(−l−v₃(Z_s)+v₃(Z_t)).

Primitive scaling divides this expression by γ^d. Consequently

    Q′ ≤ C Z_t M^(2m) 3^(−l).                                          (M5)

## Fast records and the finite family of height intervals

Take η=1/100. Call a high non-all-one packet good if Q′≥(H′)^(−η). For a good packet, (M5) and H′≤A₀ give

    l log 3 ≤ (1+η) log Z_t + 2m log M+(1+η)log C+ηE log 2.

Write E=l+F, F≥0. Multiplying the resulting upper bound for l by log(3/2) and subtracting F log 2 gives 3^l/2^E≤ C M^m Z_t^(2/5). Here ρ=log(3/2)/(log 3−ηlog 2) has (1+η)ρ<2/5, 2ρ<1 and ηρ<1. With (M3),

    Z_t ≤ [3^m C M^m Z_s]^(5/3).                                      (M6)

Let Y_old be an existing record with Y_s≤Y_old. A new record Y_t>Y_old² is called fast. For Y_old≥[2·3^m H^(2m) M^m]^5 and above the low-state cutoff specified below, (M6) excludes a good fast record. To see the effect of the shift, its Z_t term is at most 2^(−5/3)Y_old² and G−1≤Y_old²/2. At a fast record Z_t>Z_old²≥Z_s². The physical bound Z_t/Z_s≤(3/2)^l and E≥l imply 2^E≥(Z_t/Z_s)^(log 2/log(3/2)). Equation (M4) yields H′≥Z_t^(1/3)/M. If Z_t≥M^12 and Z_t≥G, then H′≥Y_t^(1/8). In the other direction (M3), (M2), C≤H^(2m) and Z_s≤Y_s give A₀≤C3^(m+l)Z_s and hence log H′≤D_m log Y_s for an absolute D_m=100(m+1)3^m. Thus

    log log Y_t−log 8 ≤ log log H′ ≤ log log Y_s+log D_m.              (M7)

The following height-interval step is the two-place mesh of Weaver (A8)–(A12), stated here with the coefficient cutoff M of this packet class. For clarity, fix d and let K_d=20000d. At H′≥T_d=max(d^(200d), exp(K_d(1+log M))), divide the two clamped position arrays by log H′ after multiplying by log 2 and log 3 respectively. Their entries lie in [0,1]. Round both down to the mesh 1/K_d; denote their rounded entries by a_i,b_i. At the finite places use the bounds −a_i and −b_i on each normalized log form. At infinity use min(0,a_i+b_i+3/K_d−1). These bounds dominate the actual projective exponents, with total excess at most 8/K_d per nonroot: each clamped position loses <1/K_d and the remaining coefficient contributes at most 1/K_d. The root has real exponent zero. Its binary valuation is at most log H′/log 2; at three the total has valuation at most log(dH′)/log 3. Round those two normalized valuations down independently on [0,1] and [0,2]. The finite projective local norms are one since the vector is primitive.

For a bad packet the sum of the exact projective exponents is less than −d−1/100. The total rounding excess is <1/200. Rescale the nonpositive rounded tuple toward zero to sum to −d−1/200. Each of the resulting fixed systems of individual inequalities still holds. The number of possible systems is bounded by

    (K_d+1)(2K_d+1) · binom(K_d+d−1,d−1)^2 = exp(O(d)).

Opposite ordering of the two arrays gives the binomial factors. There is no grid choice for coefficient denominators and the systems do not depend on H or m. Apply Evertse–Ferretti, Corollary 1.3, over the rationals at infinity, two and three, with epsilon 1/200. Each family of forms is linearly independent and lies in the coordinate-plus-total catalog. The explicit description following the corollary, also Lemma 15.3, writes its proper exceptional subspace by nonempty zero subsums. All our primitive vectors avoid it. Therefore all these bad heights above T_d lie in exp(O(d)) intervals on the log log H′ axis, each of length at most log(400d log(6d)). The constants are absolute and effective. The interval centers are allowed to be ineffective. This use of a packet-specific C changes neither the forms nor the interval family. [Evertse and Ferretti, Annals of Mathematics 177 (2013), Corollary 1.3 and Lemma 15.3](https://doi.org/10.4007/annals.2013.177.2.4) · [Weaver, Paper 15/v2, (A8)–(A13)](https://rstation.ai/problems/collatz/papers/15)

## Summing actual record increments

Choose a uniform startup Y_m with

    log Y_m = 1000(m+1)^2·4^m · log[(4m+4)G].

It exceeds the good fast-record cutoff above, 2M^12+2G, and [4m(H+1)+G+1]^(3^m). If the record prefix of a packet passes through a state at most 4m(H+1), the suffix after that state still has at most m pieces. Equation (M2) then puts its endpoint below Y_m. Thus a fast record beginning with an old record at least Y_m satisfies all the high-state and primitive-height conditions just used.

Group the k consecutive pieces into packets of at most m. From a packet raising the prior record choose the actual prefix ending at its first maximum. All cut pieces remain admissible. On the y=log log Y axis, the total of increments of size at most log 2 is at most ceil(k/m)log 2. For each larger increment beginning above log log Y_m, its packet must be bad. If H′≤T_d its terminal y is at most log log T_d+log 8. Every packet beginning below startup ends at y≤log log Y_m + m log 3, by (M2). With y₀=log log(n+G), the total contribution of increments contained in these initial ranges is O(m+1), since log log Y_m−y₀=O(m+1) and max_{d≤2m+1} log log T_d−y₀=O(m+1). In the latter comparison, log M=O((m+1)log(2H+2)) whereas log(n+G)≥4 log(2H+2).

A remaining fast increment associated to an exceptional interval [u,v] for log log H′ is entirely contained in [u−log D_m,v+log 8], by (M7) and Y_s≤Y_old. The actual record increments have disjoint interiors. Summing the lengths of the expanded intervals for 2≤d≤2m+1 bounds all this remaining progress by exp(C₁m) for an absolute effective C₁. It follows that

    log log(max Y) ≤ log log(n+G) + ceil(k/m)log 2 + exp(C₂m).

Each of the k pieces has length at most 2 log₂(max Y). Take logarithms of this time bound. For large k choose m=max(1,floor(log(k+2)/(3C₂))); the cost k/m is O(k/log(k+2)), while exp(C₂m)=O((k+2)^(1/3)). The finitely many smaller k are absorbed by increasing the absolute constant. Since log(n+G)≪log(n+2H+2), this proves (M1) and the assertion for the record height.

## Late ternary avoidance or rapid ordinary growth

In a length-T window beginning at clock J, take at each clock *all* positive rational anchors of height at most H, and put

    L = C log(2H) log(3+T+log(x_J+1)).

Call a clock shallow if the maximum of v₃(x_i+t) over that ball is at most L. Any nonmatching edge between choices of maximizing anchors has a shallow endpoint by the local Yu estimate, because its physical exponent is ≤2+T log₂(3/2)+log₂(x_J+1). If S clocks are shallow, the number D of mismatches is ≤2S. Maximal exact stretches plus the single mismatches use at most 2D+1≤4S+1 pieces. There is no zero displacement for a positive anchor. Thus

    T+1 ≤ exp(C₃ (S+1)/log(S+2)) · log(x_J+2H+2).                     (M8)

This holds for *every* window on *every* positive ordinary orbit, including repeated orbits, and all finite H. In particular, given δ>0, if log(x_J+2H+2)≤T^(1−δ), then for all sufficiently large T the specified window has at least c_δ log T log log T distinct shallow clocks. It is a count inside the supplied window even if it begins very late. Conversely along windows with S=o(log T log log T), (M8) forces log(x_J+2H+2)≥T^(1−o(1)). For polynomial-height phase bounds H and T=J, such a shortage forces x_J≥exp(J^(1−o(1))). This conclusion still permits near-exponential escape. In particular log x_J=o(J) alone need not provide a fixed power saving.

The same conclusion holds for the full signed height ball on a window with all x_i>H. In an arbitrary window one may instead count clocks where x_i equals the negative of one of the chosen signed anchors as additional exceptions. Cutting both edges adjacent to each such clock into singletons then produces O(S+number of exact coincidences+1) pieces. Denominators divisible by three have negative scores and do not affect the height-ball maximum. [Yu, Acta Arithmetica 89 (1999), Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

The first missing global assertion is an incompatible upper bound on that actual growth, or an argument turning these shallow clocks into ordinary descent. The entropy of a stationary inverse decoder does not supply either inference.
