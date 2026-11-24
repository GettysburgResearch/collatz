# Required odd-count excess for lower partners at the first endpoint

**PROPOSED. Written proof, with an exact rational check for the numerical constant.** This result concerns the ordinary shortcut map and one fixed positive ordinary source at a time. It places a lower bound on the cost of one approach to convergence. It does not settle Collatz.

Fix any integer h≥1. Let U be the positive odd integers that are coprime to 3. For u in U set n=3^h u. Consider all positive m<n and b≥0 with T^b(m)=T(n), counting k odd steps from m. Define d=k−h−1. Let B_h be the set of u for which no such diagram has

    (9/2)^d ≤ n/(2·3^(2h)).

**The relative lower natural density of B_h in U exceeds 17/500.** In particular, at every fixed positive h a positive proportion of ordinary sources need odd-count excess greater than log base 9/2 of n/(2·3^(2h)), if any smaller partner reaches their first endpoint. The statement includes sources having no such partner at all. There is no restriction on the partner clock or parity word. Endpoints farther down the source orbit are outside this claim. The quantifier is a separate lower density as u tends to infinity at each fixed h.

## 1. Recovering the ordinary tail

The proof uses S5 in [shadow.md](shadow.md). For every actual smaller partner at this endpoint it supplies the following representation. Take a prefix of length s=d+e ending with its d-th odd letter (so e≥0, d≥1). Its affine map is (3^d x+C)/2^s. Following this prefix the signed comparison reaches a positive ordinary r. A length-p physical path from r ends at 1 and has exactly h+1 odd letters, and

    3^d m = 2^s(r+2^p u) − C.

The necessary facts about this representation are proved in S2–S5 of the linked note. In particular neither convergence of the original source n nor universal convergence of the possible r is assumed. The prefix sends zero to C/2^s. Omitting all even letters only increases its value from zero, so 0≤C/2^s≤(3/2)^d−1.

## 2. A small enough excess forces strict contraction

The multiplier on n is L=2^(s+p)/3^(h+d), and L=1 is impossible by unique factorization. Write A=(3/2)^d. The displayed budget gives u≥2·3^h(9/2)^d, hence A≤u/2. Using m<n and C<2^s A gives

    2^(s+p)u < 3^(h+d)u + 2^s A ≤ 3^(h+d)u + 2^(s+p)u/2.

Thus 2^(s+p)<2·3^(h+d). If L>1, the positive integer 2^(s+p)−3^(h+d) is at least one. Applying the formula for m again,

    u ≤ (2^(s+p)−3^(h+d))u < C < 2^s A < 2·3^h(9/2)^d.

This contradicts the budget. Every smaller partner within it therefore has L<1. Longer individual words with negative affine intercept and L>1 are left available.

## 3. Counting every strictly contractive diagram

For fixed d,e a contractive diagram must have 2^p<3^(h+d)/2^s. The physical path r→1 with h+1 odds has a strictly positive affine intercept. Thus r<2^p/3^(h+1), in particular

    1 ≤ r < 3^d/(3·2^s).

For each r there is at most one admissible p: between two arrivals at 1 the ordinary orbit runs around the 1,2 cycle one or more times, increasing the odd count. This uniqueness saves a factor of two in the count. The number of possible pairs (r,p) is strictly less than 3^d/(3·2^s), and is zero unless 3^d>3·2^s. There are at most binom(s−1,d−1) choices of the prefix, since its last letter is odd. Each prefix and tail imposes exactly one residue on u modulo 3^d for integrality of m (the coefficient 2^(s+p) is a ternary unit). Some of these residues may not meet U. Counting them all only enlarges our upper bound.

Write N_d for the total number of such prefix-tail pairs at d, counted even in case of duplicate unit classes. The result is

    Σ_{d≥1} N_d / 3^d ≤ S/3,
    S = Σ_{s≥1} 2^(−s) Σ_{1≤d≤s, 3^d>3·2^s} binom(s−1,d−1).

This bound is independent of h. Section 5 proves S<1932/1000.

## 4. Passing to ordinary natural density

For u≤X only d≤D=floor(log base 9/2 of (3^h X)) can pass the displayed budget. For X tending to infinity at fixed h this upper bound is nonnegative. For each class modulo 3^d the number of eligible odd u up to X is at most X/(2·3^d)+1, by the Chinese remainder theorem with modulus 2. Also

    Σ_{1≤d≤D} N_d ≤ 3^D S/3 = O_h(X^(log(3)/log(9/2))) = o(X).

The number of u in U up to X having any successful within-budget diagram is at most XS/6+o(X). Since |U∩[1,X]|=X/3+O(1), their relative upper natural density is at most S/2<483/500. The complementary relative lower density exceeds 17/500. This argument pays the ordinary counting error per residue. A countably infinite union estimate in a ternary probability space by itself would not imply this conclusion for ordinary integers.

There is a sharper auxiliary bound when the candidate prefix must consist entirely of odd letters. For the positive-r family described in S5 choose e=0. Its formula reads m+1=2^d(r+1+2^p u)/3^d. Any positive smaller acceptance then forces 2^d≤m+1≤n and L<1 directly. Thus d≤log base 2 of n for every acceptance, even without imposing the headline budget. Necessarily d≥3, and N_d<(3/2)^d/3 for d≥3. The sum of N_d/3^d is at most (1/3)Σ_{d≥3}2^(−d)=1/12. Rounding errors sum to O_h(X^(log(3/2)/log 2))=o(X). Consequently at most **1/8** of U at each fixed h can have any positive-tail certificate with this all-odd prefix, allowing arbitrary clocks and every ordinary r→1 tail. This refutes coverage by varying only the ordinary tail in S1.

## 5. Exact numerical certificate for the structural series

The finite sum through s=400 is an explicit rational less than 1931/1000. The companion [coverage_bound.py](coverage_bound.py) verifies this by counting the binomial coefficients with denominator 2^400, using integers throughout.

For the tail, 3^d>3·2^s implies d>5s/8 since 3^5<2^8. Replace binom(s−1,d−1) by binom(s,d), and write Y for a binomial random variable with parameters s and 1/2. The summand at clock s is bounded by

    Pr(Y>5s/8) ≤ E[2^Y] / 2^(5s/8) = ((3/2)/2^(5/8))^s.

Writing q=(3/2)^8/2^5=6561/8192<1, the sum over s>400 is bounded by 8 q^50/(1−q)<1/1000. The checker verifies that last inequality by exact rational arithmetic. This is a finite calculation of a universal combinatorial constant with a proved all-depth tail bound. It is independent of any finite census of ordinary Collatz starts.

## What remains open

The bound gives no global obstruction to deeper partners, to a source first moving farther along its orbit, or to convergence by a different method. The sources counted here have h≥1. After any odd forward step the source becomes a unit modulo 3, so these fixed positive heights impose no recurrence condition on an infinite ordinary tail.
