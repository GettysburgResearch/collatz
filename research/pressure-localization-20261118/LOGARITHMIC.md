# A signed logarithmic moment and the division-count deficit

**PROPOSED.** Assume the positive odd map and the PR 144 head identified in
[the source localization note](README.md). Retain cycle laps throughout
except in the explicitly defined simple-prefix energy. Logs below are base 2.
At odd clock j let t_j=U^j(x), A_j be the total valuation, J_j=3^j/2^A_j,
and write

    a_j(x)=(J_j/t_j)² ≤ x⁻²,             E_j=∑_x a_j(x),
    B_j(x)=⌊log(3^j)⌋−A_j(x),            H_j=∑_x a_j(x) B_j(x).

B_j is an exact signed integer. H_j measures the excess of the integer
reference exponent above the cumulative number of divisions. It averages
over every positive odd source with its actual finite-clock weight.

## 1. The source entropy bound

Omit the clock and set p_x=a_x/E for any positive family a_x≤x⁻².
The first N=⌈1/E⌉ odd sources satisfy
∑a_x^(3/4)≤N^(1/4)E^(3/4) by concavity. Since E≤π²/8<5/4, this is
at most (9/4)^(1/4)√E. The tail is at most
∑_(n>2N)n^(−3/2)≤√(2/N)≤√(2E). Therefore

    ∑ a_x^(3/4) ≤ 3√E,
    S/E := −(1/2) ∑ p_x log a_x ≤ log(9/E).                 (1)

For the second inequality apply concavity of log to
2∑p_x log(a_x^(−1/4)). Zero coordinates may be omitted. The
infinite inequalities follow by truncation or countable Jensen.

An absolute bound S<5/2 is convenient below. Indeed u=x²a_x≤1 gives

    −(1/2)a_x log a_x ≤ x⁻²(log x + 1/(2e ln 2)).

The sum of log(x)/x² over the odd integers is at most its sum over all
integers n≥2. That sum is bounded by 1/4+∫₂^∞(log t)/t² dt
=3/4+1/(2 ln 2)<7/4. The remaining constant contributes less than
(1/2)(5/4)=5/8. This also establishes absolute convergence of H_j:
the positive log J_j is at most j log(3/2), and the negative part is
bounded after summation by S, since log t_j≥0.

## 2. Direct logarithmic dissipation

Let f_j=log(3^j)−⌊log(3^j)⌋∈[0,1). The exact entropy identity is

    ∑ p_x log t_j(x) = H_j/E_j + f_j + S/E_j.                (2)

By the +1 term in the odd map, a_(j+1)=a_j(3t_j/(3t_j+1))².
For t≥1, 1−(3t/(3t+1))²≥7/(16t), as in the parent L2.
Convexity of 2^(−u), (1), and (2) give the unconditional inequalities

    E_j−E_(j+1) ≥ (7/288) E_j² 2^(−H_j/E_j),
    E_Q ≤ [1/E_0+(7/288)∑_(j<Q) 2^(−H_j/E_j)]⁻¹.            (3)

Indeed the lower bound is (7/16)E_j times the inverse geometric mean
of t_j, and 2^(−f_j)≥1/2. The second assertion follows by dividing the
first by E_j E_(j+1)≤E_j² and summing. No packing input is used here.

Consequently divergence of the reciprocal geometric means
∑ 2^(−H_j/E_j) is sufficient for E_Q→0. For example, a uniform
H_j/E_j≤log(j+2)+log(log(j+2))+C would suffice. These estimates are
open. With the parent's first-hit discount, E_Q→0 is equivalent to all
positive orbits being eventually periodic. Exclusion of further cycles
is separate.

For comparison, D_j=∑ a_j J_j². Jensen gives

    H_j/E_j ≤ (1/2)log(D_j/E_j).

Thus the earlier quadratic target D_j=O((j+1)²) implies the required
upper logarithmic coefficient if E_j has positive limit. A logarithmic
mean tolerates rare large coefficients that dominate a positive-power
moment. No converse for Collatz is asserted.

## 3. The packing alternative permits a coefficient strictly above one

Suppose a simple odd path contains at most K Y^β states at most Y.
The parent D4 uses K=16 and β=19/20 from the proposed finite-path W2
in [the translated packing proof](https://github.com/GettysburgResearch/collatz/blob/fe2247fcd7730c15430941a7b6e011d006d41d84/research/novel-swarm-20261030/pass4/WINDOWS.md).
The shortcut expansion of a simple list of odd states through its last
odd state remains simple: any repeated even state would force a repeated
next odd state. These constants retain their source status.

Define A_Q to consist of sources with t_0,…,t_(Q−1) distinct, and let
Ebar_Q=∑_(x∈A_Q)a_(Q−1)(x). Sorting the Q heights on any such path gives
its i-th smallest state at least (i/K)^(1/β). Since a_j≥a_(Q−1)
for j<Q and all log t_j≥0, the identity (2), S<5/2 and E_j<5/4 yield

    (1/Q)∑_(j<Q) H_j + 4
      ≥ (Ebar_Q/β) [log(Q!)/Q − log K].                      (4)

Each discarded term on the left-hand height sum is nonnegative. The
rounding and entropy errors cost less than 4 *per clock*, independent
of every source, cycle length, and cutoff.

Both Ebar_Q and E_Q tend to the same sum of limiting source weights:
eventual cycles have weight tending to zero, and nonperiodic paths have
a positive limiting b_j=√a_j by the summable reciprocal-height estimate
from W3. Dominated convergence uses a_j≤x⁻². Thus, if there is even
one positive nonperiodic orbit, their common limit E_∞ is positive.
Using log(Q!)/(Q log Q)→1 and the Cesàro limit of E_j in (4) proves

    liminf_(Q→∞) [∑_(j<Q) H_j]/[(log Q)∑_(j<Q)E_j] ≥ 1/β.   (5)

For the displayed packing input, any upper subsequence limit strictly
below 20/19 rules out every nonperiodic orbit. In particular a normalized
upper coefficient 1 suffices. Establishing such an upper subsequence for
the ordinary map is the first unsupported step.

## 4. Uniform computability at finite clocks

For every odd X≥3 the omitted energy lies between zero and 1/[2(X+1)],
by the telescoping odd reciprocal-square tail. The omitted H_j satisfies

    −(⌈log X⌉+4)/X ≤ ∑_(x>X) a_j(x) B_j(x) ≤ j/[2(X+1)].      (6)

The upper estimate uses B_j≤j log(3/2). For the lower estimate use the
pointwise entropy envelope in section 1 and B_j≥log J_j−1. Sum the
majorant (log x+1+1/(2e ln 2))/x² over all integers x>X by integration;
it is decreasing for x≥3, and 1/ln 2+1+1/(2e ln 2)<4.

To compute an absolute ε enclosure of the *clock average* of H_j
through Q, a cutoff polynomial in Q and ε⁻¹ therefore suffices.
For fixed ε one can take X=O_ε(Q) and replay O_ε(Q²) odd steps.
The exponents have O(Q+log X) magnitude by 2^A≤4^j x. All sign
comparisons and term roundings use integers. An approximation to H_j/E_j
with a prescribed relative error can require finer absolute precision
when E_j is small.

With X=65,535 and 96 fractional bits, the all-source sums satisfy the
following outward-rounded intervals.

| Q | ∑_(j<Q) E_j | ∑_(j<Q) H_j |
|---:|---:|---:|
| 32 | [3.46378, 3.46403] | [−3.24118, −3.22762] |
| 64 | [3.52007, 3.52057] | [−3.34250, −3.30758] |
| 128 | [3.52016, 3.52115] | [−3.36291, −3.26183] |
| 256 | [3.52016, 3.52213] | [−3.40197, −3.07481] |

The signs at these finite clocks do not determine (5). Each inspected
positive cycle continues through the clock limit. A separate raw-step
replay reconstructs the signed integer intervals. For a 64-source bank
it additionally checks (3) at 49 clocks after *rounding H/E down* in
the exponent, making that finite check stronger and entirely rational.

```sh
python -B experiments/pressure-localization-20261118/log_trace.py --clocks 32 64 128 256 --cutoff 65535 > /tmp/log-trace.json
python -B experiments/pressure-localization-20261118/check_log.py /tmp/log-trace.json
```

[Exact integer endpoints](../../reports/pressure-localization-20261118/log_trace.json).
