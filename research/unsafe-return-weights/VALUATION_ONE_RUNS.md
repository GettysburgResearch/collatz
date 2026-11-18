# Fixed numbers of valuation-one runs and the maximal forward growth scale

**PROPOSED, ineffective.** Let U be the odd Syracuse map, a(x)=v₂(3x+1), and write y_j=U^j(y₀) on an ordinary positive odd escaping orbit. Then

    (Σ_(i<j)(a(y_i)−1))/log(j+2) → ∞.                                 (1)

In particular y_j/((3/2)^j j^(−A))→0 for every fixed real A. In [the high-target uniform first-hit increment estimate (10)](INVERSE_AGE_LAWS.md), every fixed polynomial saving λ is consequently admissible. This does not supply a strict exponential improvement in the base 3/2, nor any global bound on the orbit. The all-fixed-A saving uses the rational p-adic Subspace Theorem; no effective onset is claimed. [Evertse, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

## Several runs with bounded separator valuations

A maximal run from an ordinary odd start x consists of r≥0 consecutive letters a=1 followed by one letter a≥2. One has x+1=2^(r+1)b with b odd: a=1 exactly at odd inputs 3 mod 4 and each such letter replaces x+1 by 3(x+1)/2. No infinite run is possible. Consider m≥2 consecutive runs starting at x=x₁ and then x₂,…,x_m, with lengths r_i and separator letters a_i between them. For each fixed m and bound K on a₁,…,a_(m−1), as x tends to infinity one has uniformly

    r₁+…+r_m ≤ (1+o_(m,K)(1)) log₂(x+1).                              (2)

To prove this, assume a growing contrary sequence with a fixed excess fraction ε>0. Pass to a subsequence fixing the bounded separator letters, and for each r_i separately making it constant or tending to infinity. With d_i=2^(a_i−1)−1>0, the exact positive equations are

    2^(a_i+r_(i+1)) b_(i+1) = 3^(r_i+1)b_i + d_i.

Set A_i=2^(a_i+r_(i+1)), B_i=3^(r_i+1) for 1≤i<m. Their composition gives

    Y = X + Σ_(i=1)^(m−1) E_i,
    Y = b_m ∏_i A_i,     X = b₁ ∏_i B_i,
    E_i = d_i ∏_(v<i) A_v ∏_(v>i) B_v.

The ratio X/E₁=b₁B₁/d₁ tends to infinity, since b₁2^(r₁+1)=x+1 tends to infinity. Consecutive offsets have ratio E_(i+1)/E_i=(d_(i+1)/d_i)A_i/B_(i+1), a fixed positive multiple of (2/3)^r_(i+1). Group adjacent offsets with constant ratio into one coordinate F, their sum. Each group is a fixed positive rational multiple of each of its members. The retained coordinate vector consists of X and the grouped offsets F₁,…,F_s, with s≥1. Successive coordinates in this order have ratios tending to zero, so there is no fixed nonzero rational linear dependence along any further infinite subsequence. Every coordinate and Y is a positive integer of logarithmic size O_(m,K)(log(x+1)): each successive x_i+1 is at most (3/2)^(r_(i−1)+1)(x_(i−1)+1), and r_i≤log₂(x_i+1).

Use the n=s+1 coordinate forms together with their sum Y. Any n of these n+1 fixed forms are independent. At each of infinity, 2 and 3 omit one of largest absolute value, taking a subsequence to fix choices. Before omission the product of the absolute values of all forms over the three places is ≤C b₁ b_m by the product formula: each grouped offset is a fixed rational times a 2,3-unit, and the nonunit parts of X and Y cost at most b₁ and b_m. At infinity Y is largest. At 2 the first grouped offset has absolute value bounded below since E₁=d₁∏_(v>1)B_v is odd. At 3 the last grouped offset has absolute value bounded below since E_(m−1)=d_(m−1)∏_(v<m−1)A_v. Thus the product after omission is ≤C' b₁ b_m/Y ≤ C' b₁ 2^(−Σ_(i≥2)r_i). Under the contrary excess assumption this is O((x+1)^(−ε)), since b₁=(x+1)/2^(r₁+1). In the normalized projective inequality, division by the local maxima to the power n adds at most H_projective^(-n): the coordinates are integers and hence their outside-place maxima are ≤1. Their projective height is at most a fixed power of x+1. It tends to infinity because the ratio X/F₁ does. The Subspace Theorem therefore forces a fixed rational dependence on an infinite subsequence, contradicting the successive ratios. This proves (2), including intervening runs of zero length.

## Excess valuation and the upper cutoff

Write c=log₂3, γ=c−1. On any fixed forward orbit y_i+1≤(y₀+1)(3/2)^i, so a run starting at time i has length ≤γ i+O_(y₀)(1). Partition its sequence of runs into consecutive disjoint groups of a fixed m≥2, charging the terminating separator after every run, including the last. If any separator in a group has a−1≥m², the group has total excess E≥m², while crude iteration of the one-run bound changes the starting index i to an ending index i'≤c^m i+O_(m,y₀)(1). Otherwise all separators are bounded by m², so (2) bounds the total run length by (1+o(1))log₂(y_i+1) as i→∞ on this escaping orbit. The m separators add only m to the time, yielding i'≤(c+o(1))i; the excess cost E is at least m.

Accordingly for each fixed η>0, all sufficiently late completed groups satisfy log(i'/i)≤E(log c+η)/m. Sum from a fixed positive starting index. An incomplete last group increases its index by at most a fixed multiplicative constant using the crude one-run bound, even when its last run has not yet ended. Hence liminf_(j→∞) Σ_(i<j)(a(y_i)−1)/log j≥m/log c. Arbitrarily large fixed m give (1). The exact affine formula gives y_j=y₀(3/2)^j 2^(−Σ(a−1))∏_(i<j)(1+1/(3y_i)). Even without importing orbit packing, the j distinct ordinary odd states have reciprocal sum at most Σ_(k≤j)1/(2k−1)=O(log(j+2)), so this last product costs at most a fixed polynomial. Formula (1) absorbs it and proves the claimed growth and cutoff consequences. The proof uses positivity and ordinary realization at the separator equalities.

## Ordinary near-equality with every selected run growing

For each fixed m≥2 and arbitrarily large x there are m successive growing runs, all their separators equal to two, with

    Σ r_i = log₂(x+1)+log₂ log₂(x+1)+O_m(1).                           (3)

Here “growing” means every r_i tends to infinity along the family. Thus the leading factor in (2) is attained, and even a uniform additive o(log log x) error in it would be false. The starting integer changes with the family.

To see this, choose an integer k→∞ and prescribe the future word (1^k 2)^(m−1), starting at an odd residue z modulo 2^(D+1), D=(m−1)(k+2), by the ordinary valuation-word bijection. Its first exponent one makes z=3 mod 4. Among the odd powers of 3 modulo 2^(D+2) every residue 3 mod 8 occurs: the powers of 9 generate the residues 1 mod 8 by v₂(9^(2^h)−1)=h+3. Thus choose even r with

    5·3^(r+1) = 2z+1 mod 2^(D+2).

The even exponent indices r form one residue class modulo 2^D; choose r in [2^D,2^(D+1)). Start x=5·2^(r+1)−1. Its first run of ones has length r and leaves the odd state 2·5·3^r−1. The next letter equals two, since 5·3^(r+1)=7 mod 8, and its odd successor is (5·3^(r+1)−1)/2=z mod 2^(D+1). Hence it realizes the entire prescribed continuation. The sum of runs is r+(m−1)k and log₂(x+1)=r+1+log₂5, whereas log₂r=D+O(1). These give (3) with no asymptotic input.

## Fixed numbers of even shortcut inputs

For T(n)=n/2 on even inputs and (3n+1)/2 on odd inputs, let I(j,k) be the set of n≥1 for which exactly k of n,Tn,…,T^(j−1)n are even. For each fixed k≥0,

    lim_(j→∞) (1/j) log₂ min I(j,k) = 1.                              (4)

For the upper bound the parity-word bijection gives a representative ≤2^j for each word. For the lower bound remove up to k initial even inputs and begin at the first odd input x≤n. Any completed positive block of even inputs has length at most k and is associated with a single odd separator of valuation at most k+1. The remaining shortcut segment has at most k+1 blocks of consecutive odd inputs. All but at most the last odd input of each block are valuation-one steps. A terminal partial run can be extended to its full valuation-one length; the valuation of its eventual separator need not be bounded, as (2) uses only the interior separators. If the segment ends among a final string of even inputs, discard that final incomplete separator and its even suffix at cost at most k+1 steps. Consequently j≤Σr_i+O_k(1) for at most k+1 successive runs with bounded intervening separators. The case of one run follows by divisibility directly. The starting x must tend to infinity if j does, since no fixed integer has a final infinite all-odd run and the number of separators is bounded. Applying (2) proves (4).

Rozier's Lower Bound Hypothesis predicts a polynomial loss from 2^j in this regime. His Lemma 6.1 gives the effective lower bound 2^(j/(1+log₂3))−2 for one even input. Formula (4) gives the limiting exponent one, ineffectively, for every fixed k. It does not prove the polynomial-loss estimate or cover a growing number of even inputs. The single-run trailing-ones identity is also a known elementary result. [Rozier, *The 3x+1 problem: a lower bound hypothesis*, §6](https://www.ipgp.fr/~rozier/pub/LBHv4.pdf) · [Single expansive-phase bound](https://zenodo.org/records/17785860)
