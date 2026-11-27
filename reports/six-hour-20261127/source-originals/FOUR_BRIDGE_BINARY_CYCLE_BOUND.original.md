# A four-segment source bound for binary cycles of discrepancy at most 99/50

**Written result, with two stated external inputs.** Let a primitive positive rational Collatz cycle have least odd period P, common reduced denominator d, maximum rational phase X, and accelerated valuations e_i∈{1,2}. Put θ=(Σe_i)/P, λ=log₂3, and W=range(E_i−iθ), where E_i=Σ_{j<i}e_j. In the class W≤99/50, every sequence with P→∞ and log d=o(log P) satisfies

[
 \liminf \frac{\log(dX)}{\log P}\ge \frac{3000}{999}.
 \tag{1}
]

This first bound uses the integral fixed-place Subspace Theorem through the separation lemma of Weaver, Paper 145/v1, §4. It does not use an irrationality-exponent claim. If the irrationality exponent of λ is strictly less than 3000/999, no such sequence exists. In particular the quoted upper bound 3 of Chudnovsky, Theorem 11.1, makes the class finite at each fixed d, including d=1. Equivalently there are c>0 and P₀ so that d≥P^c on every cycle in this class with P≥P₀. Both the finiteness statement and its threshold are ineffective. The finite exceptional primitive cycles are not classified.

## 1. Actual source classes

Write the positive odd phases as N_i/d with gcd(N_i,d)=1. The common denominator is prime to six, by the usual rotated carry divided by 2^{Pθ}−3^P. The scaled ordinary recurrence is 2^{e_i}N_{i+1}=3N_i+d. Primitive phases are distinct, so Y=dX≥P. For the given sequence X→∞. Every rotated prefix of length k satisfies |E_k−kθ|≤W. The all-terms geometric bound in the cycle equation gives X≤2^W/(2^θ−3), hence θ>λ and θ→λ. Throughout the proof constants may depend on a fixed small η>0 from the four-segment placement. We have d=exp(o(log Y)).

The cycle has a fixed s=max_i(E_i−iθ), with E_i=⌊iθ+s⌋−z_i and z_i∈{0,1}. Writing f_i={iθ+s}, the real width forces z_i=0 whenever f_i>49/50, because f_i+z_i=s−(E_i−iθ)≤99/50. At equality the state z_i=1 is allowed. At any rotated origin there is t∈[0,1) with

[
 E_i^{\rm loc}=\lfloor iθ+t\rfloor+z_0-z_i,\qquad f_i=\{iθ+t\}.
]

A length b window has O(b) possible phase types at this fixed slope. Partition at the at most 2(b+1) cuts {-iθ} and {49/50−iθ}, 0≤i≤b, counting each boundary separately as well as each open interval. All floors and forced-zero tests are fixed on each type, even when thresholds coincide. Fix z₀,z_b as well. Thus K=E_b^{loc} is fixed, with |K−bθ|≤2. Modulo 2^K, the full window beginning at N satisfies

[
 N\equiv-d\sum_{i=0}^{b-1}2^{E_i^{\rm loc}}3^{-(i+1)}\pmod{2^K}. \tag{2}
]

This follows by multiplying the finite affine identity by 3^{-b} modulo 2^K. The odd terminal condition gives an even finer cylinder. The coarser (2) suffices because 2^K>Y. Consequently the number of numerators N∈[1,Y] is at most the number of admitted words whose normalized source (2) lies in the corresponding circular interval.

## 2. Exact energy in one conditioned segment

The mechanical increment m_i=⌊(i+1)θ+t⌋−⌊iθ+t⌋ belongs to {1,2}. The eligible transition is z_i≥z_{i+1} if m_i=1, and z_i≤z_{i+1} if m_i=2. Fix the cut states and regard one consecutive segment of a letters starting at odd index j, binary time u=E_j^{loc}, with its terminal date u+T fixed. Its odd positions relative to u are r_i=E_{j+i}^{loc}−u, 0≤i<a. Write

[
 B=\sum_{i=0}^{a-1}3^{a-1-i}2^{r_i}.
]

The number of ordered quadruples of its paths with B₁+B₂=B₃+B₄ is at most C·3^{γa}, γ=999/1000, uniformly in cuts and in 1.584961≤θ≤1.584964. To see the equality criterion, write r_i=v_i−z_{j+i}, with fixed v_i≥0, so 2^{r_i+1}=2^{v_i}(2−z_{j+i}). After multiplying the four-sum by two and reducing modulo three from the last letter backward, the digit difference lies in {−2,−1,0,1,2}, and 2^{v_i} is a unit. Each collision thus has coordinatewise equal bit-pair sums, and conversely. The terminal bits, absent from B, are identical fixed cut states.

There are six compatible four-bit states, of grades 0 (all zero), 1 (four middle states) and 2 (all one); the grade is the common pair sum. In terms of aggregate path counts (x,y,z), a one-gap sends them to (x+y+z,y+4z,z), and a two-gap sends them to (x,4x+y,x+y+z). Each recursion follows from the coordinatewise monotone transition on the four paths. A forced zero projects to (x,0,0). Between two successive forced sites starting in (1,0,0), the exact return possibilities (length, remaining zero count) are

| Length n | Count E |
|---:|---:|
| 12 | 388224 |
| 41 | 30840400948687284336 |
| 53 | 17778623164916750424132973 |

These are exact finite claims certified by `bridge_energy_certificate.py`. The slope enclosure follows by 2^1584961<3^1000000<2^1584964. For α=θ−1 take the breakpoints {−kα} and {49/50−kα}, k=0,…,53, and the ends of the unit interval. Their order and each unwrapped integer label agree at both rational endpoints of the prescribed slope range, and all moving cuts are affine there, so the order is constant throughout the interval. Test every open phase cell and every left endpoint at their rational midpoint slope. From a free starting phase a forced site occurs within 52 steps. From a forced phase the first strictly positive forced return is one of the listed transitions. The test preserves the f=49/50 endpoint and the post-wrap convention. In all three rows E^{1000}<3^{999n}. Multiplying the scalar return factors gives the claimed bound, since both incomplete pieces have bounded length and at most six initial states. This proof does not infer asymptotic cancellation from a numerical Lyapunov exponent.

## 3. Prime-power reciprocity and quantization

Fix 0<η<1/100, take b=⌈((4+η)/(3+η))(log₂Y+3)/θ⌉ and h=⌊K/(4+η)⌋. Then K−h≥log₂Y, K=((4+η)/(3+η))log₂Y+O(1), and h→∞. Set a=⌊(1−η)h/θ⌋ and j₀=⌈3ηh/θ⌉+1. The four adjacent odd-index segments starting at j=j₀,j₀+a,j₀+2a,j₀+3a all end before b. Condition on all bits outside their interiors, including the five fixed cut bits. The number of outside environments is at most 2^{b−4a+5}. The independence used below is Cartesian product factorization of the allowed paths in the four disjoint interiors under this fixed environment. Their fixed entrance and exit states ensure that the local dates, counts and durations fit the global word.

For every such segment set m=K−u, n=j+a, T=E_{j+a}^{loc}−u. Uniformly u=jθ+O(2), T=(1−η)h+O(4). The first end is at least (1+2η)h−O(1) and the last start is at most 3h+O(1). Since θ/λ→1, both m≥h and λn≥h eventually. The final binary margin K−u−T≥2ηh−O(1), useful for varying d. For each position write v=m−r_i, w=j+i+1. Define H_i=[d·2^{-v}]_{3^w} and Z_i=[−d·3^{-w}]_{2^v}, choosing least nonnegative residues. Since 3∤d, H_i≥1. Also v≥2ηh−O(1) and log d=o(h), so d<2^v. Therefore 0≤(2^v H_i−d)/3^w<2^v and it equals Z_i exactly. Put

[
 R_W=\sum_i3^{a-1-i}H_i,\qquad R_Z=\sum_i2^{r_i}Z_i.
]

Termwise reciprocity then gives

[
 2^m R_W-3^n R_Z=dB,\qquad 0\le R_W<a3^n,\quad0\le R_Z<a2^m. \tag{3}
]

The contribution of this segment to the normalized global source modulo one in (2) is R_Z/2^m. Its ordinary numerator B≤4a·2^T follows from T−r_i=(a−i)θ+O(2) and θ≥λ. The full expression is an actual rotated source with the outside contribution fixed.

For a real number V set Q_h(V)=⌊2^h{V}⌋ mod 2^h. A four-sum collision of the Q_h(R_Z/2^m) implies that with signs +,+,−,− there is an integer k=O(a) such that b₀=Σ sign·R_Z−k2^m satisfies |b₀|≤4·2^{m−h}. Set a₀=Σ sign·R_W−k3^n using the same k. Then |a₀|=O(K3^n), |b₀|=O(K2^m), and (3) gives

[
 2^m a₀-3^n b₀=d\sum\operatorname{sign} B .
]

Its magnitude is O(dK2^T)≤2^h e^{−c_η K} for all large K, since T≤(1−η)h+O(4) and log d=o(h). **Imported separation.** Lemma 4 of Weaver, Paper 145/v1, rules out a nonzero such difference under these size bounds, h comparable to K and 2^m,3^n≥2^h. Its underlying input is the fixed-place integral Subspace Theorem. In the application the two coordinates are 2^ma₀ and 3^nb₀; the product of the chosen archimedean, dyadic and ternary forms is bounded by e^{−c_ηK}. The finitely many possible rational lines force eventual diagonal coincidence since their coordinate ratio approaches one and a zero coordinate cannot have the required size. We quote the deep theorem. This derivation generalizes the unit-drift raw reciprocity in that paper to d=e^{o(h)} within these actual segments; no denominator is discarded. Thus every four-sum grid collision is an ordinary B-sum collision for all sufficiently large P.

## 4. Counting the original interval

In one fixed environment let F_j be the unnormalized counting measure of the quantized contributions from segment j on the finite group Z/2^hZ. Fourier orthogonality with normalized frequency averaging gives ∫|F̂_j|⁴ equal to the number of its ordered grid collisions. By §§2–3 this is ≤C3^{γa}. Finite Fourier inversion and Hölder bound every convolution atom of the four actual counting measures by ∏(∫|F̂_j|⁴)^{1/4}≤C3^{γa}. The four within-cell remainders have sum in [0,4) in grid units. The interval [1,Y] of raw sources has normalized length ≤2^{-h}, so the acceptable grid sums fall in at most six circular residues after the fixed outside translation. This yields ≤6C3^{γa} full paths for the environment. No ratio of conditional laws or population estimates is required.

Multiply by the outside count, boundedly many endpoint states, and O(b) real-intercept cells. K and h can take O(1) values because |K−bθ|≤2. With these bounded endpoint variations understood,

[
 P\ll_η (b+1)2^{b-4a+5}3^{γa}.
]

All P original positive, distinct numerator phases are counted because they have the required periodic windows, including if the length exceeds the period. Here b=(4+η)h/θ+O(1), a=(1−η)h/θ+O(1), and log₂Y=(3+η)h+O(1). Using θ→λ gives

[
 \limsup\frac{\log P}{\log Y}
 \le \frac{5η/λ+γ(1−η)}{3+η}.
]

Let η↓0 to obtain (1). If μ(λ)≤M, then for every ε>0 the reduced θ=A/P, of reduced denominator at most P, satisfies θ−λ≥c_ε P^{-M-ε}. The geometric upper bound on X therefore yields limsup log(dX)/log P≤M on a sequence with log d=o(log P). This contradicts (1) for M<3000/999. If no uniform c,P₀ existed in the statement one could choose P→∞ with log d/log P→0, the case just ruled out. There are finitely many words per bounded period here.

## Provenance and limits

The source separation, actual-segment placement, circular carry and Fourier mechanism are Weaver's Paper 145 §§4–6, following Paper 73/v2. Paper 181 §4 develops a related native physical-band census. Paper 145 also gives a hereditary Boolean encoding, an unrestricted canonical-height-one count and several wider extensions. Paper 74/v1 previously studies ordinary cycles all of whose valuations are one or two and uses uniquely forced backward predecessors. The input specific to this note is the six-state ordinary equal-pair count for the **binary-valuation** strip with real cap 99/50, its three scalar forced returns, and their use with the small-denominator scaled reciprocity. The cap and the binary restriction are both assumptions. Extending the same unweighted transfer to the entire real range below two would remove the positive-density forced returns used here.

The finite certificate above is a direct exact Python calculation. The analytic transfer and conclusion are written mathematics. The Subspace Theorem, its quoted application and the Chudnovsky bound are not Lean-rebuilt here. The irrationality claim specifically refers to arXiv:2610.28079v1, Theorem 11.1.

- https://rstation.ai/problems/collatz/papers/145/v1
- https://rstation.ai/problems/collatz/papers/181/v1
- https://rstation.ai/problems/collatz/papers/74/v1
- https://arxiv.org/abs/0907.2098
- https://arxiv.org/html/2610.28079v1#S11
