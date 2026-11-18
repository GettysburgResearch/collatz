# Uniform reciprocal lower density of Collatz predecessors

Let P(a) consist of sources that reach a under the ordinary map
C(n)=n/2 for even n and C(n)=3n+1 for odd n, allowing zero steps.
There is an absolute c>0 such that for every positive a prime to 3,

    lower natural density P(a) ≥ c/a.                                (1)

The scale from which the bound applies may depend on a. More locally,
for all sufficiently large real Y there are at least cY/a distinct
positive odd predecessors in [Y,8Y). The proof combines Mazur's
central inverse-path construction with a terminal estimate retaining
the total valuation in Tao's fine-scale mixing argument. This is a
source-qualified proof development, without a formal verification.
Wirsching's preliminary manuscript proposed a reciprocal bound for
noncyclic targets under the shortcut convention and described three
gaps in its approach. Mazur subsequently established positive lower
density for each eligible target. No conclusion identifying distinct
components follows from (1).

[Wirsching, *On positive predecessor density in 3n+1 dynamics*](https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf).
[Mazur, *Positive lower density of Collatz predecessors*](https://proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

## 1. Terminal words in one physical octave

Set α=log₂3 and β=2−α=log₂(4/3). For a large integer b put
ℓ=floor(b/4), d_min=ceil(b/3), d_max=floor(5b/3). Let m be an integer
in [0.45βb,1.55βb]. At each d_min≤d≤d_max select the sole integer a
satisfying

    m+2 ≤ a−αd < m+3.

The corresponding density on the ternary group is
g_(d,a)(z)=3^d P(F_d≡z mod 3^d, S_d=a), with notation from the marked
mixing proof. Lift all functions to level d_max and put G_m=sum_d g_(d,a).
For any fixed D>0 we claim

    || ((1/3)g_ℓ−G_m)_+ ||₁ ≤ C_D b^(−D),                           (2)

uniformly in m, where g_ℓ=3^ℓ P(F_ℓ≡z). Apply the marked fine-mixing
estimate separately to each of O(b) depths with an increased decay
exponent. It replaces G_m in L¹, to the stated precision, by the sum
of its projections to level ℓ. Given S_ℓ=s, the remaining exponents
are independent. The resulting sum equals

    sum_s g_(ℓ,s)(z) sum_(D'=d_min−ℓ to d_max−ℓ)
        P( m+2−(s−αℓ) ≤ S_(D')−αD' < m+3−(s−αℓ) ).

For |s−2ℓ|≤0.01βb, the lower endpoint v=m+2−(s−αℓ) lies between
0.18βb and 1.32βb for all sufficiently large b. The walk
S_j−αj has positive mean drift β. Its first crossing of v occurs in
the displayed depth range with probability 1−O(exp(−c b)).
Indeed D_min'=d_min−ℓ=(1/12+o(1))b and
D_max'=d_max−ℓ=(17/12+o(1))b. For j<D_min' a crossing requires an
upper deviation at least c b, and failure to cross by D_max' requires
a lower deviation at least c b there. The exponential geometric
moment bound (or Chernoff's inequality and a union over j) gives the
claim. At any first crossing, conditional on the previous values and
on crossing at that step, the positive geometric exponent equals the
least eligible integer with probability exactly 1/2. The overshoot
then lies in [0,1). The sum of interval probabilities is at least the
probability of this first-crossing event, which is ≥1/3. Finally the
sum of Haar masses of g_(ℓ,s) at excluded s is exponentially small
by the same concentration bound. Positivity proves (2).

[Fine mixing with the total valuation retained](MARKED-MIXING.md).

## 2. Positive weighted coverage for a favorable seed

Fix one sufficiently large allowed initial scale b₀ in Mazur's original
central construction. The b_j grow by b_(j+1)=b_j+floor(b_j/100),
and K_j=floor(j/100) bounds the overshoot at block j. There are a fixed
unit ternary cylinder V, d₀>0, and an index N such that every odd
R₀≥16^b₀ in V satisfies for every n≥N

    Z_n(R₀)=sum_(central histories w) J_w ρ_(floor(b_n/4))(R_w) ≥ d₀.

Here R_w is the integral inverse endpoint, J_w=3^length(w)/2^sum(w),
and ρ_ℓ=(2/3)g_ℓ. This follows from Mazur Propositions 3.1 and 4.2:
the summable bound on mark increments is uniform in the seed, and
each fixed mark depends on a finite ternary residue. The central
construction and its histogram are used before any terminal block.

Write B_n=sum_(j<n)b_j. Formula (3.5) of that paper gives at each
central step

    (4/3)^b_j R/4 ≤ R' ≤ 2^(K_j+1)(4/3)^b_j R,   R'≥16^b_(j+1).

Thus every generation-n endpoint satisfies
log₂R_w=log₂R₀+β B_n+O(n²+1), uniformly in the histories. Given any
large Y choose n so log₂(Y/R₀) lies in

    [β(B_n+0.46 b_n), β(B_n+1.54 b_n)].

Consecutive intervals overlap since b_(n+1)≤1.01 b_n. Their endpoints
increase to infinity. Set b=b_n; then n→∞ with Y and n²=o(b). The
integers m_w=floor(log₂(Y/R_w)) lie in [0.45βb,1.55βb] and take
O(n²+1) different values.

Mazur's residue histogram (3.9), for groups of all central histories
at generation n, gives for Q≤2b

    sum_w J_w |f(R_w)| ≤ C_(b₀)(1+b)^C ||f||_(L¹(Z/3^Q)).

Indeed the factor there counts O((1+sum ceil(b_j^(3/5)))(1+sum K_j+n))
pairs of depth and total exponent and the final parenthesis is bounded
for fixed b₀. A subgroup of histories inherits the same inequality by
positivity. Apply it at Q=d_max<2b separately to the histories with
each value m_w, using f=((1/3)g_ℓ−G_(m_w))_+. Equation (2) with
sufficiently large fixed decay power gives

    sum_w J_w G_(m_w)(R_w) ≥ (1/3) sum_w J_w g_ℓ(R_w) − o(1) ≥ d₀/3

for all sufficiently large Y. The constants in this positive mass
bound are absolute after the universal initial scale and cylinder have
been fixed.

[Mazur, *Explicit positive-density Collatz convergence in logarithmic time*, version 2, §§3–4 and equation (3.9)](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf).

## 3. Distinct positive integers and all eligible targets

Expand each G_m(R_w) into its compatible words. All inverse steps
from a positive odd integer are positive odd integers when integral.
For a terminal word with total a and length d write its source as

    x=(R_w−F_d) 2^a / 3^d.

The forward affine offset is nonnegative and ≤(3/2)^d−1, since each
valuation is at least one. Here d≤5b/3 and (3/2)^5<2^3, so F_d<2^b
and R_w≥16^b. The exponent window and definition of m_w imply

    Y ≤ x ≤ 8Y.

Suppose R₀ has no positive odd-only return. A fixed source has at most
one odd depth to R₀, and the forward valuations give its unique complete
word. In inverse order the central first crossings recover the unique
first n block cuts, leaving a unique terminal word. Thus the expanded
mass above counts each source's J exactly once, even though a terminal
word can pass the valuation window at another depth. Two different
total depths cannot describe the same source at a nonperiodic root.
For the complete word Jx≤R₀ by the positive affine intercept. The
bound on the sum of J therefore yields ≥d₀Y/(3R₀) distinct sources.

For any 3∤a choose e=1 or 2 making 2^e a≡1 mod 3. The immediate
predecessors R_j=(2^(e+2j)a−1)/3 all reach a ordinarily and have the
same odd successor. Each block of 3^s consecutive j covers every residue
modulo 3^s since v₃(R_i−R_j)=v₃(i−j). Take s defining V, start
sufficiently far along to ensure R_j≥16^b₀ even at a=1, and use two
consecutive blocks. At most one of the two favorable siblings is
periodic since a periodic successor has just one periodic predecessor.
This gives a favorable nonperiodic R₀≤C a with absolute C, proving the
local count and (1) by taking Y proportional to the final counting
threshold.

For any finite family A of pairwise unreachable eligible targets the
selected sources are disjoint. Taking Y beyond the finitely many
onsets, summing the local counts, and extending by monotonicity to an
infinite family gives the linear capacity bound

    lower_density( union_(a in A) P(a) ) ≥ c sum_(a in A) 1/a.

The same bound for individual targets of the shortcut map T follows
with a factor of two in the constant from P_C(2a)⊆P_T(a).

[Map conventions and the odd sibling construction](../native-pressure-20261118/ANTICHAINS.md).
