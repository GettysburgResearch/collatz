# Testing a joint real and ternary estimate on the shifted moment

**OPEN.** The ordinary Collatz shifted moment from PR192 at 045be43632f274dd64faf15714e42cc8de27a2e9 remains uncontrolled on bounded positive integer sources. We tested a singular kernel that keeps the dependence between the two coordinates. Its noninteger error admits a uniform geometric bound. A complementary lower bound amplifies every single ordinary endpoint to positive rational preimages occupying a quantitative fraction of an explicit range of integer numerators. We could not carry this fraction through the congruence that would produce ordinary starting integers in the same component. These are written proofs.

## The exact error made by the singular kernel

For a chronological word of N positive gaps use E, C and c=C/2^E from [the shifted-moment proof](../astra-high-variance-20261124/CENTRAL_CLOSURE.md). Keep every positive odd integer endpoint y>1 with x=(2^E y−C)/3^N≥1. Give the pair weight x^{-s}, s>1. The ordinary transfer keeps only 3^N dividing 2^E y−C. Its sum over all allowed lifts is precisely the total weight of positive odd integers that have not hit one through N odd steps.

For α>0 replace the congruence indicator by

    min(1, 3^{-αN}|y−c|₃^{-α}).

Write the resulting sum as R_N. Define S_d to consist of positive rationals with odd numerator, exact reduced denominator 3^d, and real value at least one. For d=0 this means all positive odd integers. Write U(z)=(3z+1)/2^{v₂(3z+1)} on positive rationals with odd numerator and denominator a power of three. No real lower bound is imposed at intermediate steps. Then

    R_N = Σ_{d=0}^N 3^{-αd} Σ_{z∈S_d, U^N(z)>1} z^{-s}.

Indeed all intermediate inverses from odd y are odd 2-adic units with denominator a power of three. For a positive initial inverse they remain positive by the forward affine equations. Their oddness gives the exact exponents. Conversely, U decreases the positive denominator exponent by precisely one at each step until the iterate is integral. If z=u/3^d is reduced and d>0, the numerator update is oddpart(u+3^{d−1}). The endpoint after N≥d steps is therefore an odd integer. The congruence weight is 3^{-αd} for d>0 and one for d=0, by y−c=3^N z/2^E. These correspondences are bijections.

For α>1 the contribution of all d≥D≥1 is at most

    (1+1/(s−1)) 3^{(1−α)D}/(1−3^{1−α}),

uniformly in N, even if some of these sources never converge. Indeed the weight at denominator 3^d before killing is at most Σ_{u≥3^d}(u/3^d)^{-s} ≤1+3^d/(s−1). At 0<α<1 an individual uncapped pole is instead integrable against ternary Haar measure. Under inverse substitution its pole is transported to (3r+1)/2^e with coefficient 3^{-α}(3/2^e)^s. For 1<s<2 one can select α<1 with the sum of these coefficients below one. This averaged contraction does not give the displayed positive-integer trace estimate. In the exactly capped calculation the d=0 term keeps the full mass of every surviving integer source, regardless of α.

## Amplifying an individual endpoint over rational denominator shells

There are absolute constants K and c₀>0 such that, for every positive odd integer y≥3 and every d≥1, there is a family of distinct positive odd-numerator rationals z=u/3^d of **exact** denominator 3^d with U^d(z)=y, all lying in

    | log₂(z/y) − d log₂(4/3) | ≤ K √d,

for which Σ 1/u ≥ c₀/y. In particular an endpoint that never converges transmits this mass to actual rational trajectories that never converge. The sum of 1/u over *all* positive integer numerators in that log window is O(√d), giving a fraction at least c/(y√d). The numerator window is centered at 4^d y. No eventual-orbit assumption enters the estimate.

**Proof.** Take independent backward exponents with probability 2^{-e}, e≥1. Put L_j=2^{e₁+⋯+e_j}/3^j. The inverse after j steps is

    z_j=L_j(y−D_j),       D_j=(1/3) Σ_{i=1}^j L_i^{-1}.

For the iid tail after the first exponent, write L'_0=1 and form L'_h in the same way. With r=√3/(2√2−1)<1 we have E[(L'_h)^{-1/2}]=r^h. Consequently E[(Σ_{h≥0}1/L'_h)^{1/2}]≤1/(1−r). With probability at least 7/8 the infinite sum is at most H=(8/(1−r))². The sum of d−1 tail exponents has mean 2(d−1) and variance 2(d−1), so with probability at least 7/8 its deviation from the mean is at most 4√d. The two tail conditions together have probability at least 3/4.

Choose a fixed integer b with 2^b/3≥2H. Require the first exponent to equal one of b,b+1 chosen so that 3 does not divide 2^{e₁}y−1. At least one works, even if 3 divides y. This independent condition has probability at least 2^{−b−1}. Every selected word has L_j≥2 and D_j≤1/6 for 1≤j≤d, by the tail bound. Hence every z_j≥1, the first denominator is three, and each subsequent inverse increases its exact denominator exponent by one. The formula for z_d and the exponent deviation give the claimed height window upon increasing K by a fixed constant. Since z_d≤L_d y, the corresponding numerator satisfies 1/u≥2^{−Σe_i}/y. Summation over those words proves the result. Distinctness follows from deterministic forward evaluation of the rational input.

The tail event used for selection may be imposed on infinite continuations of a length-d word. Its projection onto length-d words has probability at least the full event probability, and the needed finite bounds hold on that projection.

## Attempt to turn the amplification into ordinary decay

The analytic opportunity was to discard an exceptional fraction o(1/√d) of the above numerators on each critical shell. The deterministic program starting from the numerator u updates by oddpart(u+3^{j−1}) when j denominators remain. Ordinary first-passage estimates on u concern a different iteration. A physical ordinary source for the same gap word and endpoint must satisfy 3^d dividing 2^E y−C, whereas every source just constructed has exact denominator 3^d and violates that congruence.

There is an explicit route for changing the endpoint without changing its eventual orbit. Replace y by y_t=(4^t(3y+1)−1)/3, t≥0, which has the same next odd value as y. The desired congruence becomes

    4^t(3y+1) ≡ 1+3 C·2^{-E}   (mod 3^{d+1}).

Both sides after division by 3y+1 are congruent to one modulo three. The order of four modulo 3^{d+1} is 3^d, since v₃(4^{3^k}−1)=k+1 by an elementary induction using the difference of cubes. There is therefore exactly one class of t modulo 3^d. The resulting starting integer, if t is taken large enough, is positive and reaches the same component. Its real size grows by a factor of order 4^t for the selected words. The uniform existence bound t<3^d is too costly to preserve the harmonic mass. We did not prove a lower local bound for the probability of a small t, or any ordinary surviving-shell estimate that controls this loss. A congruence repair without such a cost bound does not prove decay of the original moment.

## Independent collision calculation and displaced returns

For fixed length h and odd count v, write n_r for the number of binary shortcut words whose integer carry C is r modulo P=3^v. The carry is injective at fixed h,v by the dyadic parity cylinder identity. Ordering the nonnegative distinct carries in each residue class gives

    Σ_r n_r(n_r−1) ≤ (2/P) Σ_W C(W).

The j-th carry in one class is at least (j−1)P. This numerator-ordering argument is also used for division-clock slices in [*Ternary Syracuse laws*, Proposition 13](https://rstation.ai/problems/collatz/papers/9). In the present binary word model, weighting each reference by b^v gives the exact binomial sum

    Σ_W b^v C(W)/3^v = (b/3) Σ_{i=0}^{h−1} [2(1+b/3)]^i (1+b)^{h−i−1}.

Indeed an odd at index i contributes 2^i times 3 raised to the number of subsequent odds, before division by 3^v. Taking b=(3/2)^s, the resulting collision majorant including the diagonal has exponential base at most max(1+b,2+2b/3), up to a polynomial in h. Multiplying by t²/2^s gives 7/8 at s=2,t=1, so strict contraction persists for s<2 and t>1 sufficiently near those values. The sharper weighted carry proof in [descent.md](descent.md) works at its stated s=7/4,t=101/100 and allows the broader matched classes there.

For completeness, for nonperiodic y the **untilted** normalized Green sum admits a short bound even for exact displaced returns. Suppose a two-half history has equal length and equal odd count on both halves and a midpoint z≥y/2. The leading multiplier A on each half obeys Az≤y by positivity, so A²≤4. More generally every history ending at such a y whose total leading multiplier L≤4 contributes y^{-s}L^s with L≤y/b for its positive initial b. Each b occurs at most once because y is nonperiodic. Its entire untilted subseries is therefore bounded by

    y^{-s} Σ_{b≥1} min(4,y/b)^s = O_s(y^{1−s})    (s>1).

This counts histories once. In particular it covers exact displaced returns z=y+k with |k|≤y/2 regardless of the duration or the number of possible k. The estimate has no exponential time tilt. A fixed small origin escaping to successively larger y need not have bounded total leading multiplier.
