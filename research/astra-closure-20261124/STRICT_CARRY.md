# Sharp losses in the actual centered carry inequality

Consider the actual accelerated orbit of one positive odd integer, with `q'=U(q)`, `a=v₂(3q+1)` and `h(q)=Σ a_i/3^(i+1)`. PR182 at `cbec52dde5bed390a693310dd04e911033ba0cc9`, `research/carry-tower-round10-20261123/ActualScalar.lean`, supplies the ordinary scalar recurrence and the strict bounds $1/2<h(q)≤1+\log_2(q)/3$. The same PR's `research/phase-packing-round12-20261124/README.md`, R12-1, is the source of the sharp exponent and the summable ordinary correction for injective orbits. The results below strengthen its finite multiplicative inequality and keep track of the transitions causing strictness.

Put $c=\lceil h(q)-1/2\rceil-1$, $p=h(q)-c$, $b=\lceil 3(p-1/2)\rceil$, and $d=c(Uq)$. The centered representative gives $1/2<p≤3/2$, $1≤b≤3$, and $a+d=b+3c$. In particular $0≤d≤3c+2$. All logarithms without subscripts are natural.

## Exact local minimum

Normalize the R12-1 inequality by setting
$$
R(c,d)=3^{3c-d}\left(\frac{d+1}{c+1}\right)^2.
$$
If $k=3c-d=a-b$, the ratio $(d+1)/(c+1)$ is exactly $3-(k+2)/(c+1)$. For fixed $k≥-2$ this increases weakly with $c$. The smallest feasible carry is $m=\max(0,\lceil k/3\rceil)$. Consequently the best unrestricted lower bound for that exact clock difference is
$$
R(c,d)≥3^k\left(\frac{3m-k+1}{m+1}\right)^2.
$$
This minimum is attained among nonnegative integer carries by $c=m$, $d=3m-k$. The ordinary orbit may impose other restrictions; no realization of every minimum is required.

* At $k=-2$, $d=3c+2$ and $R=1$ identically. The physical assumptions force $a=1,b=3$.
* At $k=-1$ the minimum is $4/3$, attained at $c=0,d=1$.
* At $k=0$, the zero-to-zero edge has $R=1$. Every other edge has $c≥1$ and $R=((3c+1)/(c+1))^2≥4$.
* At $k=1,2,3$, the respective minima are $27/4,9,27/4$. As $k$ increases by three, $m$ increases by one and $3m-k+1$ stays fixed. The minimum grows by $27((m+1)/(m+2))^2>1$. Hence every $a>b$ costs at least $27/4$, including every physical gap $a≥4$.

The constants $4/3$ and $27/4$ are attained on the consecutive ordinary edges $3→5→1$. Indeed $h(1)=1, h(5)=5/3, h(3)=8/9$, and their $(a,b,c,d)$ are $(1,2,0,1)$ and $(4,1,1,0)$. Thus the uniform factors are optimal even when one restricts to positive odd orbits.

## Same-source prefix penalty

For an interval $[j,j+n)$ let $A,B$ be its actual and canonical clocks. Count $J$ edges other than $c=d=0$ and $d=3c+2$. Of these, count $D$ with $a>b$. Multiplication gives
$$
3^{A-B}\left(\frac{c_{j+n}+1}{c_j+1}\right)^2
≥ (4/3)^{J-D}(27/4)^D.
$$
There is no bound on carries, time, resets, or gap size. The stronger product of exact local minima above can replace the two constants when the individual clock differences are available.

For a prefix write $P_n=3^n/2^{B_n}$, $E_n=\prod_{i<n}(1+1/(3q_i))$, $\gamma=2\log_3 2$, and $L_n=(4/3)^{J_n-D_n}(27/4)^{D_n}$. The ordinary identity $q_n=q_0 3^n 2^{-A_n}E_n$ gives the finite bound
$$
P_n ≥ \frac{q_n}{q_0 E_n}\left(\frac{c_0+1}{c_n+1}\right)^\gamma L_n^{\log_3 2}.
$$
On an injective orbit the written whole-orbit counting theorem used in R12-1 bounds $E_n$ uniformly, giving $P_n≥C(q_0)q_n(1+\log q_n)^{-\gamma}L_n^{\log_3 2}$ at every prefix.

## Equality tails and the open alternative

An all-zero-charge tail has no gap larger than three. Conversely, if every future gap is at most three, then the literal series gives $h≤\sum_{i≥0}3/3^{i+1}=3/2$ at every future state, forcing every carry to vanish. Thus infinitely many strict edges are equivalent to infinitely many gaps of size at least four. Either they occur infinitely often, in which case $D_n→∞$, or eventually $c_i=0, a_i=b_i≤3$. No ordinary global exclusion of either possibility is supplied.

In fact a positive carry at any given state forces a future physical gap of at least four, hence a future debit. Otherwise all future gaps would be at most three, and the same geometric-series bound would force the current carry to be zero. A separate proof of eventual strictness uses only the ordinary divisibility theorem `not_all_gaps_one`: without a strict transition, a positive carry can only take saturated edges, forcing every future actual gap to equal one.

Full convergence remains open. The finite inequality refines an escape obstruction, and gives no contrary all-source upper bound for $P_n$. A positive-cycle exclusion also remains necessary. The true-orbit correction estimate invoked above is a written upstream theorem.

## Verification scope

The public theorem `StrictCarry.interval_slack` charges the factor $4/3$ at each strict edge. The companion theorem `StrictCarry.debit_slack` proves the sharper local factor $27/4$ whenever $d<3c$. `StrictCarry.Actual.actual_interval_slack` specializes the first inequality to exact orbit states using the centered digit defined by a ceiling of the physical scalar. `StrictCarry.Actual.no_strict_iff_small_gaps` proves both directions of the all-time tail criterion. The theorem `StrictCarry.Actual.strict_physical_prefix` proves the finite, logarithmic form of the ordinary prefix inequality with its exact physical correction and the factor $(4/3)^{J}$. The combined two-factor product follows by multiplication in the written proof. The global occupation theorem used to bound $E_n$ retains its upstream written proof status.

The exact finite control exercised all 25,155 feasible transitions with starting carry at most 128, and all 25,437 positive-length prefixes before reaching one from the 1,024 positive odd starts at most 2,047. Ordinary controls evaluated the scalar backwards from $h(1)=1$ using rational arithmetic, including the sharp witnesses $3→5$ and $5→1$. Normal and optimized Python produced identical results. The finite sample supports the formulas at those inputs only.
