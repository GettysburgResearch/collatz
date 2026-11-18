# A stochastic inverse walk on every positive ordinary unit

For the positive odd unit integers, there is a pointwise finite function
H bounded below by an absolute c>0, satisfying the exact harmonic identity

    H(t)=sum_(x positive odd, Ux=t) 3·2^(−v₂(3x+1)) H(x).             (1)

Set H(x)=0 at the odd multiples of 3. For every ordinary nonperiodic
unit target, H(t)≤Ct with an absolute C. At periodic targets the upper
bound is finite with the cycle factor in the pointwise density note.

Let h be the canonical lower-semicontinuous representative of the
limiting weight ρ from the minorization note. At each ordinary t,
h(t)≤liminf_k ρ_k(t)<∞: each local essential lower bound is at most
all finer conditional averages of the same cylinder point, and the
ordinary upper bound applies. Lower semicontinuity together with the
essential lower bound on the clopen unit set gives h≥c there directly
from its defining essential infima. We established h≥Lh pointwise.
Consequently H(t)=lim_(n→∞)L^n h(t) decreases and is finite at every
ordinary odd t. Every compatible inverse branch there is another
positive odd integer. Its full one-generation sum of weighted h is
finite, bounded by h(t). Dominated convergence over these branches
proves (1).

For a compatible inverse word of length n≥1 ending backwards at a
nonunit x, increase its last inverse valuation by 2. Its source becomes
4x+1, a unit, with weight J_w/4. This operation is injective on the
words in question. Therefore L^n 1_units ≥ g_n/5. For all ordinary
units,

    L^n h(t) ≥ (c/5)g_n(t) ≥ c' >0.

This gives a positive universal lower bound on H. Applying (1) again
now gives H(t)≥(c'/5)g_n(t) for *every* finite n, and in particular
H(t)≥c'' t lower_density(P(t)) by the depth-average lower bound.

[Uniform minorization and canonical representative](MINORIZATION.md).
[Pointwise bounds and predecessor-density transfer](ORDINARY-DENSITIES.md).

## Infinite central histories

Equation (1) defines a stochastic inverse walk with branch probability
J_a H(x)/H(t) at x=(2^a t−1)/3 when integral. Its length-d cylinder
probabilities telescope to J_w H(x_w)/H(t). Fix the favorable cylinder
C with central limit z≥d₀>0 from the minorization proof. For any large
enough representative R in C, uniform convergence of the central mark
gives Z_n(R)≥d₀/2 for all sufficiently large n. The conditional
probability of passing all of the first n central blocks is

    sum_(w in W_n) J_w H(x_w)/H(R) ≥ c₁ Z_n(R)/H(R),

by H(x)≥c' g_k(x)/5 and ρ_k=2g_k/3. The events decrease in n, so the
probability of passing every block indefinitely is at least c₂/H(R).
Given any positive odd unit t, choose the favorable immediate predecessor
R from the bounded-valuation construction (and large enough for the
central construction). Its branch probability is J_a H(R)/H(t).
Multiplication cancels H(R). Hence, from *each* t, the probability of
taking this one favorable branch and then passing every central block
forever is at least

    c₃/H(t),                                                        (2)

with c₃ independent of t. This conclusion is about an infinite event
under the specified stochastic kernel on actual integral predecessors.

Physical growth follows at central block endpoints from Mazur's (3.5):
if the jth block uses parameters b_j and K_j then the change in log
height is b_j log(4/3)+O(K_j+1). In the original central construction
K_j=floor(j/100) and b_j grows geometrically, hence the cumulative
rounding and excess costs are o(sum b_j). The cumulative Syracuse
depth is sum b_j+O(sum ceil(b_j^(3/5)))=(1+o(1))sum b_j. Along the
event in (2), the endpoint log height divided by inverse depth therefore
tends to log(4/3) at block boundaries. This concerns growing inverse
rays in a component, and does not imply a fixed height is reached in
the forward direction.

[Mazur, version 2, definitions (3.1)–(3.5)](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf).

Valbuena previously constructed an ordinary harmonic trace and identified
its Cesàro and Abel values. The first-landing paper gives the corresponding
odd-parent kernel, pointwise domination of finite-level densities, and
positive upper frequency for every finite valuation word. The construction
above reaches the central-event statement by regularizing the stationary
ternary density.

[Valbuena, *Collatz basin densities and canonical traces from first-passage stabilization*](https://doi.org/10.5281/zenodo.23025885).
[First-landing bounds, §§8–10](https://rstation.ai/problems/collatz/papers/12).
