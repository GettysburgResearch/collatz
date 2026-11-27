# A positive density of mismatches at every lag in ordinary real-width-two cycles

Let P be the least odd period of a positive ordinary Collatz cycle, A its division sum, θ=A/P, λ=log₂3, and W the real range of E_i−iθ over one lap. All logarithms below are natural unless marked. For every proper lag h let
[
 D_h=\#\{i\bmod P:e_{i+h}\ne e_i\}.
]
For growing primitive cycles with W<2,
[
 \liminf_{P\to\infty}\min_{1\le h<P} D_h/P>1/500. \tag{1}
]
Consequently for all sufficiently large such cycles, every h and every integer B give more than P/1000 cyclic h-windows whose division sum differs from B. The conclusion concerns ordinary integer cycles. It permits dense-defect words and gives no unconditional exclusion of this whole width class.

**External inputs.** The complete class W<2 has canonical integer height at most one. We use Weaver, Paper 145/v1, Theorem 1 for the located ordinary upper count with exponent 7/16, and the quoted Chudnovsky bound μ(log₂3)≤3. In the binary valuation subclass the elementary Fibonacci terminal census of BINARY_CORRIDOR_DENOMINATORS.md supplies a sufficient lower height exponent above two in place of Weaver's count. The stronger UNRESTRICTED_BINARY_FOURTH_MOMENT.md gives an optional improvement to the small-rank subsidiary estimate. No assumption on the number of raw or resonant defects is made.

## 1. A smooth reference for the integral scaled phases

At a maximizing rotation choose E_i=⌊iθ⌋−z_i with z_i∈{0,1} and z_0=0. Indeed the rotated discrepancy has maximum zero and range smaller than two, and the integer z_i is its floor defect. Let L_i=2^{1−z_i}x_i, f_i={iθ}, m_i=⌊(i+1)θ⌋−⌊iθ⌋. The complete actual recurrence is
[
 2^{m_i} L_{i+1}=3L_i+\ell_i,\qquad
 \ell_i=2^{1−z_i}=\operatorname{lowbit}(L_i)\in\{1,2\}.
\]
If a mechanical phase repeated several times, its q-step return map for q=P/gcd(A,P) would be strictly increasing on that finite set of integral L. Indeed on integers of 2-adic valuation at most one, y↦3y+lowbit(y) is strictly increasing, and each step divides outputs by the same positive mechanical factor. An order-preserving permutation on a finite linear order is the identity. Thus L_i=L_{i+q} everywhere, which recovers each original odd x_i as the odd part and contradicts least period if q<P. This is the height-one case of Paper 114's coprimality theorem.

Along growing P the distinct positive integer phases imply X=max x_i≥P. The uniform cycle estimate X≤4/(2^θ−3) gives θ→λ from above. All subsequent statements concern sufficiently large P, so 1<θ<2. Set s=A−P. We can now index L by integer phase rank r=(is mod P), and extend it by L_{r+P}=2L_r. Then f_i=r/P, and the lowbit convention extends homogeneously. In particular
[
 2L_{r+s}=3L_r+\ell_r
\]
on the extended rank line. The accurately ordered phase theorem in Weaver's Post 65 also gives L₀<…<L_{P−1}<2L₀. Only the rank indexing, recurrence and coprimality are needed here.

There is an absolute C₁ such that
[
 L_r=L_0 2^{r/P}+O(P),\qquad 0\le r<2P . \tag{2}
]
Indeed H_i=L_i2^{-f_i} satisfies H_{i+1}=(3/2^θ)H_i+2^{-θ-f_i}ℓ_i. As H_i≤2X and (2^θ−3)X≤4, we have |H_{i+1}−H_i|≤C₁ uniformly. Reach each of the P phases in at most P−1 chronological steps and use doubling for the second octave. Also L₀ is comparable to X once X/P→∞, since every L_r lies between x_i and 2x_i and (2) controls all differences.

For every fixed exponent slightly below 16/7, X eventually exceeds P to that exponent. More explicitly, choose Y=X in Paper 145 Theorem 1's located count. Its slope neighborhood contains θ eventually and all P distinct ordinary starts belong to the allowed height-one windows, so P≪X^{7/16} (allowing a logarithmic factor would suffice). Conversely μ(λ)≤3 implies θ−λ≥c_ηP^{-3-η} for every η>0 and gives X≤C_ηP^{3+η}. This gives
[
 16/7\le\liminf \log X/\log P\le\limsup \log X/\log P\le3 . \tag{3}
]

## 2. A bounded-multiplicity gap at every rank offset

Changing h to P−h preserves Hamming distance. Orient it so that t=(hs mod P) belongs to [1,P/2]. For each rank set
[
 G_r=L_{r+t}-L_r .
]
The quantity is integral and extended with G_{r+P}=2G_r. With C=L₀, (2) gives
[
 G_r=C(2^{t/P}-1)2^{r/P}+O(P),\quad
 |G_r|\ll Xt/P+P,\quad
 \#\{0\le r<P:G_r=g\}\ll 1+P^3/(tX). \tag{4}
]
The last bound is uniform in g and t. Consecutive values of the strictly increasing main term differ by at least cXt/P², by the two elementary exponential inequalities 2^v−1≥v log 2 and C comparable to X. All ranks attaining g must have their main terms inside an interval of width O(P), proving the bound. Our use of an absolute bound on G covers signed values as well.

Let c_r=1_{r+t≥P} for 0≤r<P, and use z'_r=z_{(r+t) mod P}. Subtraction on the extended rank line yields the exact chronological signed recursion
[
 2^{m(r)}G_{(r+s)\bmod P}=3G_r+δ_r,\qquad
 δ_r=2^{c_r}\ell_{(r+t)\bmod P}-\ell_r,
\]
where m(r)=1+1_{r+s≥P}. This includes both seams automatically. Put w_r=z'_r−z_r−c_r∈{−2,−1,0,1}. The shifted mechanical increment differs from m(r) by c_{(r+s) mod P}−c_r. Therefore
[
 e_{i+h}-e_i=w_r-w_{(r+s)\bmod P}.
 \tag{5}
]
At a nonwrapped pair c_r=0, δ_r is determined by w_r: equal bits give zero and unequal bits determine their order uniquely. At a wrapped pair c_r=1, the value of w_r again determines both bits when they are unequal. When they are equal, δ_r=ℓ_r leaves two possibilities. Thus (m,c,w) determine δ with a cost of at most one additional bit per wrapped site, no matter how badly the actual word differs at other sites.

For t=1, away from its one wrapped site, δ_r∈{−1,0,1}. In that ordinary range the backward gap is exactly the nearest integer to 2^{m(r)}G_{(r+s)mod P}/3. This nearest-integer observation motivates the signed recurrence but is not required at wrapped sites.

## 3. Counting windows with few changes

Let b be the smallest positive integer with 3^b greater than twice the uniform upper bound on |G_r| in (4). In view of (3)–(4), b tends to infinity and b=O(log P). Take, for example, the upper bound C₂(Xt/P+P) with one absolute C₂ chosen for all cycles. A length-b (m,δ) word specifies the terminal G modulo 3^b: iterating the signed recursion and inverting 2^{Σm} modulo 3^b proves this directly. It specifies at most one integer among the G_r in the allowed range and at most O(1+P³/(tX)) terminal ranks.

At this fixed slope and offset there are O(b) schedules (m,c) as the initial real phase varies. The floor crossings and crossings of the wrap threshold 1−t/P at each date produce O(b) cuts; allow singleton boundary faces too. Uniformly over initial phase and over t,
[
 \#\{0\le j<b:c_{r+js}=1\}\le (t/P+o(1))b. \tag{6}
]
To check the uniformity, along any sequence s/P→λ−1 irrational. For each fixed nonzero Fourier frequency k the absolute geometric sum for n=b consecutive points is ≤2/|1−exp(2πik s/P)|=O_k(1). Continuous periodic functions therefore have uniform averages by trigonometric approximation. A fixed fine partition with continuous upper and lower majorants for each interval gives discrepancy o(1) for all intervals, including moving thresholds and their endpoint conventions.

Suppose a sequence of cycles and lags with D_h/P→ε. If ε is already at least 1/500 plus a small fixed amount there is nothing to check numerically. For any fixed ε<τ<1/2, at least (1−(ε+o(1))/τ)P starts have at most τb changes of w, by (5) and cyclic averaging. A length-b word on four w states with at most τb changes has at most
[
 4\exp\{b[H(τ)+τ\log 3]\}
]
possibilities, where H is binary entropy in nats. The three arises because a change selects one of at most three other values. Combine the positive fraction of starts with (4), (6), the O(b) schedule count and the one-bit bound in §2. This gives
[
 c_{ε,τ}P\ll (1+P^3/(tX))(b+1)
 \exp\{b[H(τ)+τ\log3+(t/P+o(1))\log2]\}. \tag{7}
]
If ε=0 the same inequality holds for any fixed τ∈(0,1/2). In the genuinely binary subclass the change determines a signed unit increment of w, so log 3 may be replaced by log 2.

## 4. The uniform positive constant

After passing to a subsequence let ξ=lim log X/log P∈[16/7,3], a=lim log t/log P∈[0,1] and u=lim t/P∈[0,1/2]. Then b/log P→(ξ+a−1)/log3 from its stated choice since ξ>2. Let τ↓ε in (7). The result, for ε<1/2, is
[
 H(ε)+ε\log3\ \ge \frac{\min(1,\xi+a-2)}{\xi+a-1}\log3-u\log2. \tag{8}
]
If u>0 then a=1 and the right side is at least (log3)/3−(log2)/2=(1/6)log(9/8). If u=0 then ξ+a∈[16/7,4]. On [16/7,3] the ratio (v−2)/(v−1) increases from 2/9, and on [3,4] the ratio 1/(v−1) decreases to 1/3. Hence in this case the right side is at least (2/9)log3. The same argument in the binary subclass with its near-cubic height lower bound gives at least (log3)/3 for u=0.

For ε=1/500 one has H(ε)+εlog3≤(1+log1500)/500<9/500. Here e>5/2 yields log1500<8. On the other hand (1/6)log(9/8)>1/54>9/500. The left side of (8) is continuous and strictly increasing near [0,1/500]. Compactness therefore enforces a strictly positive margin beyond 1/500 for the lower limit over all lags. Finally, for cyclic h-window sums B_i, B_{i+1}−B_i=e_{i+h}−e_i. Each mismatch needs at least one of B_i,B_{i+1} different from the prescribed B. This proves the window assertion.

## Prior comparisons and scope

Paper 22 Theorem 10 studies gaps between consecutive numerically ordered original states and uses equal valuations to chain gaps. Paper 114 establishes same-phase coprimality by integer-scaled states. Weaver's Post 65 orders the scaled phases at canonical heights up to two, gives their exact octave equation, and identifies the doubled positive-gap recurrence as an earlier difference of the cycle system. The smooth rank reference (2), bounded multiplicity (4), change/one-bit coding at wrapped sites and all-lag density conclusion (8) are the parts used here beyond those precedents. Paper 145 supplies the necessary ordinary height exponent above two for the whole width class. The sprint's direct Paper 15 dictionary bound has a different strength and scope: it forces increasing numbers of short-lag defects without this uniform real-width hypothesis. The large-denominator dense rational constructions are consistent with (1); the point is a necessity for actual ordinary bounded-width cycles, not an inference from those controls.

- https://rstation.ai/problems/collatz/papers/22/v4
- https://rstation.ai/problems/collatz/papers/114/v1
- https://rstation.ai/r/collatz/posts/65#comment-M-8gx_Y9x5tMrj8M
- https://rstation.ai/problems/collatz/papers/145/v1
- https://arxiv.org/html/2610.28079v1#S11
