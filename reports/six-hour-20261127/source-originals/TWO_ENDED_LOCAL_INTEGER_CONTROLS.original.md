# Positive ordinary controls at the natural two-ended horizon

Let λ=log₂3, β=2−λ, and φ=(1+√5)/2. Fix an integer b≥1 and any two-ended split l+r=b. There are absolute C,c>0 and at least c·3^{σb} distinct positive odd integer midpoint states x∈[100·3^b,120·3^b] with ordinary positive trajectories of length l before x and length r after x, where

[
  σ=2β\log(φ)/\log(3)=0.36358\ldots >1/3 .
]

Their binary accelerated gaps are in {1,2}, their first b prefix sums E_i satisfy 0≤iλ−E_i<2, and at each positive time the phase exceeds the initial phase. All their phases are between c·3^b and C·3^b, uniformly in the split. Thus positivity, both exact integral directions and prefix non-descent at a window of total length log₃X+O(1) are compatible with more than X^{1/3} distinct ordinary sources in a single comparable interval. The assertion concerns positive finite trajectories. Cyclic closure supplies an additional arithmetic equation.

## The language

Take E_i=⌊iλ⌋−z_i with z_0=0 and each z_i∈{0,1}. Retain paths with e_i=E_{i+1}−E_i∈{1,2}. If the baseline gap is one the 0,1 transition matrix is L=[[1,0],[1,1]], while for a two it is U=[[1,1],[0,1]]. There are βb+O(1) one-gaps and no consecutive one-gaps. Pair each one except a possible final one with its succeeding two, obtaining k≥βb−2 disjoint LU pairs. Delete all other individual matrices. Each deleted factor is entrywise at least I, so the original product dominates (LU)^k entrywise. Since (LU)(1,φ)ᵀ=φ²(1,φ)ᵀ, the number of admissible words from z_0=0 is at least φ^{2k−1}. Distinct bit paths give distinct gap words by cumulative summation. The strict threshold follows without decimal logarithms: λ<8/5 since 3⁵<2⁸, β>2/5, and φ¹²=144φ+89>3⁵. Consequently 6β logφ>log3.

## Exact realization centered at an arbitrary split

For a length-s word with sum S and prefixes E_j write C=Σ_{j=0}^{s−1}3^{s−1−j}2^{E_j} (empty C=0). Then 2^S x_end=3^s x_start+C. A prescribed positive odd word to the right of an odd x, inclusive of the odd terminal, is given by

[
 3^r x+C_R\equiv 2^{S_R}\pmod {2^{S_R+1}} .
]

This one odd residue gives every exact prefix valuation. Modulo 2^{E_i+1} for 0≤i<r, the terms with j>i vanish and the j=i term is 3^{r−1−i}2^{E_i}. Cancellation of the odd factor 3^{r−i} identifies 3^i x+C_i≡2^{E_i} mod 2^{E_i+1}; the endpoint follows from the displayed congruence. For r=0 the condition just fixes oddness.

The left word asks that x be congruent to C_L·2^{−S_L} mod 3^l. Indeed x_start=(2^{S_L}x−C_L)/3^l is then integral and odd by the odd first summand of C_L if l>0. Each prefix has an integral odd phase as well: for a specified suffix of length k, reducing 2^{S_L}x−C_L modulo 3^k shows 2^{S_suffix}x−C_suffix≡0 mod 3^k after cancelling the unit 2^{S_prefix}. Every intermediate backward numerator is odd. Thus every step is the exact ordinary Syracuse step. The empty left word adds no condition. The two congruences choose one class modulo M=3^l·2^{S_R+1}. The discrepancy throughout the full word is in [0,2), hence |S_R−rλ|<2 and M≤8·3^b. Choose the first representative ≥100·3^b. It lies in the asserted interval.

For any subinterval of length k the linear factor 3^k/2^S is in (1/4,4), and each summand of C/2^S is at most 4/3. Every backward phase is consequently at least (100·3^b−4b/3)/4 and at most 4·120·3^b. Every forward phase is at most 4·120·3^b+4b/3 and at least 25·3^b. Every full-word prefix gain 3^i/2^{E_i}≥1, and its additive term is strictly positive at i>0, giving strict non-descent from the actual starting integer. Distinct words give distinct midpoints. The future is deterministic. In the binary past an admissible predecessor's gap is fixed by 2^e x≡1 mod3 since 2^1 and 2^2 are distinct mod3; its predecessor is then fixed. Iterate through all l positions. This proves the count for each split, including either empty side.

This control leaves open estimates using a longer combined horizon, several scales, or exact periodicity. In particular the four-bridge source argument uses a horizon approaching (4/3) log₃X (Paper 145, §§4–6). The source and terminal congruences here are the usual finite parity/valuation coding and its ternary inverse, as in PR206 and Paper 205. The additional ingredient is the lower population of the actual monotone-prefix binary language, simultaneously realized at every two-ended split.
