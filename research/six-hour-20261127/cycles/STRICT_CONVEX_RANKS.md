# Strict convexity of the scaled ranks in ordinary canonical-height-one cycles

Let an ordinary positive Collatz cycle have least odd period P, positive accelerated valuations e_i, total A, slope θ=A/P and maximal odd state X. Rotate to a maximizing discrepancy cut, so the canonical grades z_i=⌊iθ⌋−E_i are nonnegative and z₀=0. Assume z_i≤1 for every i, equivalently the real discrepancy range is less than two. All positive valuations are admitted under this hypothesis, including valuation three.

For all sufficiently large such P, put s=A−P, r=is mod P and L_r=(2−z_i)x_i for the actual odd state x_i. Extend L_{r+P}=2L_r. Then

$$
 L_{r+1}>L_r,\qquad L_{r+2}-2L_{r+1}+L_r\ge1\qquad(0\le r<P).
 \tag{1}
$$

In particular for every 1≤t<P the rank gaps G^{(t)}_r=L_{r+t}−L_r are distinct, strictly increasing in r, and

$$
 G^{(t)}_{r+1}-G^{(t)}_r\ge t\qquad(0\le r<P).
 \tag{2}
$$

The quantitative Diophantine input is only a finite irrationality exponent for log₂3, supplied for instance by the 2018 Bondareva–Luchin–Salikhov Theorem 1. The proof does not require a source-counting or Subspace Theorem bound, the 2026 exponent three, a binary valuation hypothesis, or the assumption X≫P². The cycle itself is hypothetical; (1) and (2) are structural necessary conditions and do not exclude the remaining cycles.

## Rank normalization and a seam-free logarithmic time interval

Every pair of repeated mechanical phases has the same mechanical letter. Their integers L have lowbits ℓ=2^{1-z}∈{1,2}, and each phase transition applies the strictly increasing map u↦3u+lowbit(u) on eligible integers, followed by the same division. If gcd(A,P)>1, the return through one mechanical period would therefore be an increasing permutation of the finite set of distinct scaled labels of that phase; distinctness follows from their distinct odd parts. Such a permutation fixes every label and contradicts least odd period P. This recovers Weaver 114 Theorem 1 in the required range. We may identify chronological advance with r↦r+s mod P.

The positive all-terms cycle bound gives X≤4/(2^θ−3), since every rotated length-j prefix is at most jθ+2, while the cycle multiplier gives θ>λ=log₂3. Since the P distinct odd states give X≥P, it follows that 0<θ−λ≪1/P. For large P, m_r=1+1_{r+s≥P} and 2≤s≤P−2. By BLS's finite irrationality exponent, X≤P⁶ eventually, by the same geometric bound and the rational slope denominator ≤P. These two estimates imply the following specific avoidance fact. If T=⌈10log₂(P+2)⌉, then

$$
 4< js\bmod P<P-4\qquad(1\le j\le T+2)
 \tag{3}
$$

for all sufficiently large P. A violation would give ‖j(λ−1)‖≪(1+j)/P. The 2018 linear-form estimate bounds the same distance below by a fixed positive multiple of (j+1)^{-5}, which contradicts j=O(log P). Small bounded j are included by irrationality and adjustment of the constant. Thus each small consecutive rank cluster centered at js, of the widths used below, stays wholly inside one octave throughout j=1,…,T+1. The one-step mechanical divisor is common to all labels in the cluster, since their next centers stay equally far from the octave seam. The use of (3) is only at positive multiples of s, not at every possible rank.

Extend ℓ_{r+P}=2ℓ_r as well. The exact equation is

$$
 2 L_{r+s}=3 L_r+\ell_r\quad(r\ge0),\qquad
 2^{m_r}L_{(r+s)\bmod P}=3L_r+\ell_r\quad(0\le r<P).
 \tag{4}
$$

The unwrapped first equation follows by scaling the fundamental period equation through powers of two. Its forward differences may therefore be taken *before* reducing indices modulo P. If G_r=L_{r+1}−L_r and H_r=L_{r+2}−2L_{r+1}+L_r, then 2^{m_r} times the reduced successor difference is 3 times the source difference plus the matching extended difference of ℓ. In particular a wrapped ℓ is genuinely doubled.

## First differences and the two second-difference seams

Every G_r is nonzero. Away from r=P−1, equality of the two consecutive L values would identify their odd parts, hence their underlying distinct cycle states. At the last rank, L_P=2L₀ is divisible by four since z₀=0, while no fundamental L_r is divisible by four. The drift for G lies in {−1,0,1} at ordinary ranks, and at the last rank is 4−ℓ_{P−1}∈{2,3}. A negative value cannot become positive, even at this seam, and a positive value remains positive. Because zero is excluded and advance by s is transitive, all G have one sign. Their sum L_P−L₀=L₀ is positive, proving strict increase. More precisely, at an ordinary rank the signed gap satisfies G_r=nearest(2G_{r+s}/3) in unwrapped notation. This rounding observation alone does not yield convexity.

For H the displayed drift t and next integer H' obey 2^{m_r}H'=3H+t, with

| Source rank | Possible drift t | Mechanical letter |
|---|---|---|
| 0≤r≤P−3 | ℓ_{r+2}−2ℓ_{r+1}+ℓ_r∈[−2,2] | 1 or 2 |
| P−2 | ℓ_{P−2}−2ℓ_{P−1}+4∈[1,4] | 2 |
| P−1 | ℓ_{P−1}−8+2ℓ₁∈[−5,−2] | 2 |

At an ordinary rank every nonzero H retains its strict sign. At P−2 a positive H remains positive and a negative H cannot become positive: for H≤−1 the numerator is at most one, but positive output would require a numerator at least four. A negative can leave its strict sign only as H=−1, t=3, H'=0. At P−1 a negative stays negative. For positive H the numerator is at least −2, so it cannot give a negative multiple of four. A positive can leave its sign only as H=1, t=−3, H'=0. In particular there is no direct strict sign reversal on either seam.

The total Σ_{r<P}H_r=G_P−G₀=G₀>0. Suppose that H takes a negative value as well. Along the transitive chronological orbit each strict sign must eventually be left. By the seam enumeration this forces H_{P−2}=−1 with zero at s−2, and H_{P−1}=1 with zero at s−1. Two adjacent zero second differences give four consecutive scaled labels at s−2,…,s+1 in an arithmetic progression of positive spacing.

Four integers in arithmetic progression with odd spacing visit all four residue classes modulo four. Our four fundamental labels avoid zero modulo four, so their spacing must be even. They therefore have the same lowbit: if odd, all have lowbit one, and if even, all have lowbit two by eligibility. Under a common mechanical gap m, (4) maps them to another four-term arithmetic progression with spacing 3g/2^m. Starting at this cluster centered at s (with offsets −2,−1,0,1), (3) allows T successive common-letter transitions. The original spacing g is positive and at most 2X, and integrality then requires 2^{Σm} to divide g because 3 is odd. But Σm≥T and 2^T>2X for large P. This contradiction proves H≥0 everywhere.

## Excluding zero curvature

If H vanishes anywhere, there is a first zero after some positive value along the chronological cycle, since ΣH>0. The sign-exit enumeration forces this zero to occur at s−1, directly after the last-rank seam. Thus L_{s−1},L_s,L_{s+1} form an arithmetic progression with positive spacing.

At any fundamental three-term progression, an odd spacing would make both even endpoints differ by 2 modulo four, which is inadmissible, or would give lowbit pattern (1,2,1). In that pattern the next H from the zero curvature satisfies 2^{m_r}H'=−2, contradicting the nonnegative integer H' just established. This last application uses the common fundamental coefficients of the current triple; (3) places both the present and subsequent triples away from the seam. Hence every triple in this propagation has even spacing, all three lowbits agree and its image remains an exact arithmetic progression with its spacing multiplied by 3/2^m. The same T-step divisibility contradiction excludes the zero at s−1. This proves (1).

For (2), extended first differences satisfy G_{r+P}=2G_r, H_{r+P}=2H_r. Thus all s-independent nonnegative extended ranks have H≥1. Subtracting successive t-gaps yields G_{r+t}−G_r=Σ_{j=0}^{t−1}H_{r+j}≥t. No geometric error term or phase multiplicity loss occurs.

**Scope and provenance.** Weaver 114 supplies the same-phase ordering and integer lowbit normalization. The companion ALL_LAG_LINEAR_DEFECTS.md studies differences of distinct rank phases using a smooth main term and an O(1+P³/(tX)) multiplicity bound. The two exact seam equations, lowbit rigidity of arithmetic triples and quadruples and the use of a short seam-free interval give strict rank convexity and singleton gap fibres here. The finite checker strict_rank_convexity_check.py exercises wrapped interfaces against exact positive rational cycle words with their correct scaled drift, as well as ordinary unit-drift sign and lowbit cases. Rational examples with drift d>1 test the normalization only; the sign and convexity theorem is for ordinary d=1. Higher differences have different zero transitions and are not treated by (1).

- https://rstation.ai/problems/collatz/papers/114/v1
- https://rstation.ai/problems/collatz/papers/145/v1
- https://doi.org/10.22405/2226-8383-2018-19-1-15-25
