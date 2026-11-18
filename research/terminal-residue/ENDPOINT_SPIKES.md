# Arbitrarily large normalized endpoint mass at each ordinary unit

**Proposed, source-qualified.** Write F(t) for the unnormalized canonical real-offset measure at a positive integer ternary unit, with the normalization of the [endpoint odometer](ENDPOINT_ODOMETER.md). For every integer N≥1 there is a modulus P_N independent of t and, for every t, a residue k_N(t) modulo P_N such that

    2^k F(t)([0,2^−k]) ≥ cN       whenever k≥0 and k ≡ k_N(t) mod P_N.

The constant c>0 is absolute. In particular the normalized mass has infinite upper limit, even for the fixed root 1. This sharpens the earlier exclusion of a finite derivative. It leaves open a bounded lower limit and the sublogarithmic endpoint test for escape.

Write C,c₀>0 for the constants in the ordinary bounded-offset floor F(x)([0,C])≥c₀, valid at every positive integer unit. At the virtual root y=2^k t choose a first inverse exponent e, then q=q(e) consecutive exponents equal to one. For all sufficiently large e choose the largest nonnegative q for which

    J = 3·2^(−e) (3/2)^q ≤ 1/(1+C).

Then J>2/[3(1+C)]. The partial real offset equals

    B = 2^(−e) + 3·2^(−e) ((3/2)^q − 1) = J − 2^(1−e).

Impose 2^(k+e) t ≡ −2 modulo 3^(q+2). The first child x=(2^(k+e)t−1)/3 is an odd positive integer congruent to −1 modulo 3^(q+1). Its next j children along this path are (2/3)^j(x+1)−1, all positive odd units for 0≤j≤q. Positivity also follows at each step because an eligible positive odd input for exponent one is at least five. The paths through this prefix whose remaining offset is at most C have full offset at most B+JC≤1. Their unnormalized mass equals J F(x_q)([0,C])≥2c₀/[3(1+C)] by telescoping the canonical cylinder masses.

Choose the first exponent e₁ large enough for this construction and recursively set

    q_i=q(e_i),    P_i=2·3^(q_i+1),    e_(i+1)=e_i+P_i.

The order of 2 modulo 3^(q_i+2) is P_i. The sequence of moduli is nested, and e_N ≡ e_i modulo P_i for i≤N. Since 2 generates the units at the largest precision, there is one residue class of k modulo P_N making 2^(k+e_N)t ≡ −2 modulo 3^(q_N+2). Every smaller congruence holds there as well. The N certified masses add because the first exponents differ. Applying the exact identity F(2^k t)([0,1])=2^k F(t)([0,2^−k]) proves the estimate. The zero endpoint has zero mass since every path has positive first offset.

There are such k in [P_N,2P_N) at every N. Since q_i=O(e_i) and e_(i+1)≤exp(O(e_i)), the resulting spikes have height at least a constant times log* k along a sequence tending to infinity. Here log* k counts natural logarithms needed to reach a value at most one. For example e_(i+1)≤exp(exp(e_i)) beyond a fixed initial threshold, so log* k≤2N+O(1). The periodic classes establishing these spikes can be very sparse.

## The actual first-minimum residue

Let ν denote the natural limiting law of the ordinary terminal correction R* up to first global minimum. Then limsup_{a↓0} ν([0,a])/a=∞, already from its submeasure on minimum 1. At the odd root 1 a backwards path repeating the root begins with the cycle letter e=2, with first offset 1/4. Hence below offset 1/4 the ordinary canonical law is supported on paths before a first visit. In the notation of the [marked first-hit formula](../critical-orbit-mellin/CYCLE_ENDPOINT_MEAN.md), t=1 gives W=1−B, and on the basin of 1 the terminal residue is R*=−log₂ W. Up to a fixed positive normalization the full canonical offset law on 0<B<1/4 equals the pushforward of the natural first-hit law weighted by W. The weight is bounded above by one. It follows that ν([0,−log₂(1−r)])≥c′ F(1)([0,r]) for r<1/4. Using the preceding spikes and −log₂(1−r)∼r/log 2 proves the assertion. Odd-source mass gives the same lower bound up to its fixed proportion if the natural law includes even starts.

## Sharp count for the single all-one run construction

For fixed k,t the sum of prefix multipliers over *all* legal prefixes consisting of one exponent e followed by q ones, with partial offset at most one, is O(1+log*(k+log(2t))). This bounds the raw prefix weights underlying the construction. The mass of a subsequent unrestricted subtree is a separate quantity.

For q≤e the sum over q of 3·2^(−e)(3/2)^q is at most 9(3/4)^e, summable over e. For a fixed e the sum over all remaining q is at most three times its largest multiplier, which is at most two since B=J−2^(1−e)≤1. To count the exponent values permitting q>e, legality of the run after x=(2^(k+e)t−1)/3 requires 3^q to divide x+1, so 3^(e+2) divides 2^(k+e)t+2. In particular e≤C(k+log(2t)) for an absolute C, by taking ordinary logarithms and using 3>2. If e′>e are two such exponents, subtract their congruences at precision e+2. Then 2^(e′−e)≡1 modulo 3^(e+2) and e′−e≥2·3^(e+1). Thus consecutive eligible e grow faster than exp(e), which proves the iterated-logarithm count. Together with the recurring lower construction this identifies the worst-case order of these prefix weights at a fixed ordinary t. It gives no upper bound on other valuation patterns.
