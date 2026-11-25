# Rational residues excluded by bounded Collatz cycles

Fix an integer $K\ge1$ and a rational number $A/d$ with $A\in\mathbb Z$, $d>0$, and $3\nmid d$. There is a computable depth $N=N(A,d,K)$ such that every positive Collatz cycle with odd minimum $m\ge KN$, odd sites in $[m,Km]$, and odd-to-odd valuations in $\{1,2\}$ satisfies

$$
  d q\not\equiv A\pmod{3^N}\qquad\text{at every odd phase }q.
$$

The depth is uniform in the period. For each fixed $K$, every ternary accumulation point of phases of such cycles with minima tending to infinity is irrational. The finite statement also applies to an ordinary path ending at $q$ with only $N$ predecessors inside the same strip. The bounded least-tripling-disagreement branch has $K=6$ for sufficiently large minima and uses precisely the required valuations. [Lean theorems](mathlib/HourCycleShadow.lean) · [Bounded branch and strip](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md)

A separate written bound gives a uniform count of sites below any height on an arbitrary finite nonrepeating path, including one full lap of an ordinary primitive cycle. [Height counts and clock deficits](HourCycleOccupation.md)

## The finite test and its termination

Read a path backwards, with $x_0=q$ and $3x_{j+1}+1=2^{e_j}x_j$. Starting from the signed numerator $Y_0=A$, test whether

$$
     3Y_{j+1}+d=2^{e_j}Y_j,\qquad e_j\in\{1,2\}.
$$

Exactly one letter is possible when $Y_j$ is a ternary unit, since $2,4$ have different nonzero residues modulo three. A multiple of three fails. The test also requires $1/(2K)\le w_j\le K$ through its terminal depth, where $w_j=3^j/2^{e_0+\cdots+e_{j-1}}$ and $w_0=1$. The implementation evaluates these inequalities with integers. If $3^N\mid d q-A$, each exact inverse step preserves the ordinary congruence with modulus reduced by one ternary digit. Consequently the test follows the actual ordinary gaps through depth $N$.

For any ordinary window of the stated height, $3w_{j+1}x_{j+1}=3w_jx_j-w_{j+1}$. Thus $w_jx_j\le x_0$, so $w_j\le K$. Summing gives $3w_jx_j\ge 3x_0-jK\ge2m$, which implies the required lower clock bound. This proves that testing negative is sufficient for an exclusion.

If every depth passed, the signed inverse recurrence would continue forever. Summing $3w_{j+1}Y_{j+1}=3w_jY_j-dw_{j+1}$ in the bounded strip gives $Y_j\to-\infty$ and $|Y_j|=O_{A,d,K}(1+j)$. The deterministic inverse recurrence makes the $Y_j$ distinct, since a repetition would repeat a finite loop. Every phase has $b$ further inverse letters. Two identical words give identical starting residues modulo $3^b$. There are at most $2^b$ words. For $C$ with $|Y_j|\le C(1+j)$, take $b$ large enough that $2C(2^b+1)<3^b$. Each residue occurs at most once among the first $2^b+1$ phases, contradicting the word count. This proves termination and the ordinary exclusion.

The kernel checks all four boundary pairs at $K=6$. Each listed depth fails and the preceding one passes. Prefix monotonicity makes it the first failure. The last two roots are the minima of PR #195's exact rational cycles. [Kernel evaluations](mathlib/HourCycleShadow.lean) · [Rational cycle data](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/cycle/BASIN_CONTROL.md)

| Rational root | First failed depth | Minimum floor $6N$ for this exclusion |
| --- | ---: | ---: |
| $-1$ | 5 | 30 |
| $1$ | 9 | 54 |
| $10865/1631$ | 45 | 270 |
| $283/13$ | 163 | 978 |

## A quantitative bound for varying rational roots

The following bound is a written consequence for *realized* ordinary windows. If a one-or-two-gap window has depth $B$, $m\ge KB$, and $3^B\mid d q-A$, then

$$
 B\ll_K 1+|A|/d+d^{\log 2/\log(3/2)} .
$$

For the bounded least-disagreement branch the last term improves to $d^{49/51}$, using the cited 512-step word census. This bounds the depth of approximation to ordinary phases by rationals of varying height. The denominator $d$ here belongs to the approximant, while the cycle under study consists of ordinary integers. [512-step census and exact certificate](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md)

Indeed write $R_{i,j}=2^{e_i+\cdots+e_{j-1}}/3^{j-i}$. Apply the ordinary strip estimate separately to every subwindow to obtain $1/L\le R_{i,j}\le L$ with $L=2K$. The exact finite signed shadow satisfies

$$
 Y_j=R_{0,j}A-\frac d3\sum_{\ell=1}^j R_{\ell,j},\qquad
 -L|A|-dLj/3\le Y_j\le L|A|-dj/(3L).
$$

Assume $B>8L^2|A|/d$ and put $T=\lfloor B/(4L^2)\rfloor$. The upper bound for $Y_B$ is strictly below the lower bound for every $Y_j$ with $j\le T$. The first $T$ signed states are therefore distinct. A repetition among them would propagate its period all the way through $B$ by uniqueness of the inverse step, making $Y_B$ equal one of those states. They lie in an interval of width $O_K(dB)$.

Choose $b$ least with $3^b$ greater than that interval width. If $T+b>B$, then $B\ll_K 1+\log(d+1)$ by $b=O_K(1+\log(dB))$, which suffices. Otherwise each of the first $T$ phases has $b$ further recorded native gaps. An upper bound $C3^{\sigma b}$ on their possible words gives $B\ll_K 1+(dB)^\sigma$ by the one-residue-per-word argument. Taking $\sigma=\log_3 2$ gives the first bound. The 512-step count gives $\sigma=49/100$ for the specified ordinary branch. Reversing each block preserves its number of possible words.

## Arbitrary positive valuations and both primes

A written extension applies to **all** positive Collatz cycles of any fixed multiplicative width $K$. If their minima tend to infinity, every accumulation point of their odd phases in $\mathbb Z_3$ is irrational, and every accumulation point in $\mathbb Z_2$ is irrational.

For either direction of a path, every step in the width strip has $2^e\le3K+1/m$. Pass to a subsequence fixing each finite gap word adjacent to the chosen phase. Products of the exact factors $1+1/(3x)$ tend to one on every fixed subword as $m\to\infty$. The endpoint height ratios then give
$K^{-1}\le 2^S/3^b\le K$ on every length-$b$ subword of the extracted history. In particular $S\le(8/5)b+\log_2 K$, since $3^5<2^8$.

There are at most $\binom{M}{b}$ positive gap words of length $b$ and sum at most $M=\lfloor(8/5)b+\log_2 K\rfloor$. Cumulative sums select $b$ members of $\{1,\ldots,M\}$. The binomial theorem gives $\binom{M}{b}2^b\le3^M$, so the count is $O_K(\lambda^b)$ with $\lambda=3^{8/5}/2<3$ by $3^3<2^5$. Any signed integer history with this word bound has at most $O_K(\lambda^b)$ distinct phases with the requisite $b$ predecessors inside an interval shorter than $3^b$. The fixed odd-step equation with increment $d$ uniquely specifies the terminal residue for each word, since 2 is invertible modulo $3^b$.

For a rational ternary limit $A/d$ in lowest terms, $3\nmid d$. Its entire backward history lifts integrally by the exact congruences at each finite depth. Its signed numerator $Y_j$ tends linearly to $-\infty$ by the strip estimates. With $t=v_2(d)$, iteration gives $3^jY_j=2^{S_j}A-d C_j$ with $C_j$ odd for $j>0$. Thus $v_2(Y_j)=t$ once $S_j>t$. Dividing this tail and $d$ by $2^t$ makes its numerators odd. Each forward step there is deterministic because the odd target fixes the complete two-adic valuation. A repeated state in the backward tail is periodic for this forward map. Its forward iterates include the first state of the normalized tail, so all repeated states belong to the same finite periodic orbit. As $Y_j\to-\infty$, a tail of this signed history is injective.

For a rational binary limit $A/d$, $d$ and $A$ are odd. At each finite depth the extracted forward gaps are exact on $A/d$, by binary congruence with ordinary phases. Consequently the signed numerators satisfy $2^{e_j}Y_{j+1}=3Y_j+d$ with odd targets. Iteration and the bounded subproducts give $Y_j\to+\infty$ linearly and $|Y_j|=O_{A,d,K}(j+1)$. The forward map is deterministic, so the path is injective.

In both cases take $b=\lceil\log_3(CN)\rceil$ with $C$ sufficiently large to contain the first $N$ tail states in an interval of width below $3^b$. In the binary case discard the initial $b$ states to supply the required predecessors. In the ternary case every state already has them further backwards. The word bound would give $N-b=O_K(\lambda^b)=o(N)$, a contradiction.

## Centered windows that immediately reach one

For **every** radius $n$ and threshold $H$, there is an ordinary trajectory of $2n$ odd-to-odd steps with a unique central minimum $m>H$, all $2n+1$ sites in $[m,2m)$, and every valuation in $\{1,2\}$. The very next odd site is 1. More generally it can be any prescribed positive odd ternary unit. Thus the local geometry under study occurs to arbitrary two-sided depth on convergent trajectories, even with a tighter width than the least-disagreement branch requires. [Lean construction](HourCycleRealization.lean)

Put $\alpha=\log_2 3$. From the center read total forward clock $\lfloor j\alpha\rfloor$ and total backward clock $\lceil j\alpha\rceil$. The successive differences in each direction are 1 or 2. At every noncentral site the ratio of the homogeneous height to its central height lies strictly between 1 and 2, by $2^a\ne3^j$ for $j>0$. On a finite chronological word $e$ with any one integer realization, a lift by $D$ adds $2D\,3^i2^{\sum_{j\ge i}e_j}$ to its $i$th phase. Choosing $D$ large absorbs every finite additive offset while preserving the strict central inequalities. A further lift in the same progression makes the last site's next odd iterate the specified target. This establishes the window and target simultaneously. It places no requirement on competing inverse paths inside the window.

Choose radius and minimum tending to infinity with target 1. Compactness supplies a simultaneous binary and ternary limit of the central states. Both coordinates are irrational by the two arguments above, which use only growing adjacent windows. Thus the surviving pairs of residue limits are nonempty even among ordinary trajectories known to reach 1.

## Proof status

[HourCycleShadow.lean](mathlib/HourCycleShadow.lean) imports Mathlib directly. Its executable function `firstFailure` returns the least failed depth. Nine axiom reports cover the signed packing and drift, rational exclusion, ordinary transfer, termination, least-depth specification, period-uniform cycles, and the numeric controls. The companion modules formalize the arbitrary-positive-gap signed obstructions at both primes, their finite ordinary transfers, and simultaneous exclusion at all phases of a bounded-width cycle. The varying-root quantitative bounds above remain written arguments. [Ternary shadow](mathlib/HourEscapeSigned.lean) · [Ternary windows](mathlib/HourEscapeWindows.lean) · [Binary shadow](mathlib/HourEscapeBinary.lean) · [Binary windows and simultaneous exclusion](mathlib/HourEscapeBinaryWindows.lean)

[HourCycleRealization.lean](HourCycleRealization.lean) uses the Std-based project modules, importing `HourEscapeCylinders`. Three axiom reports cover the translation at every ordinary phase, the realization with a prescribed final step, and the centered construction for every radius.

A single positive cycle has a fixed minimum and gains a positive clock defect on every lap. The results exclude neighborhoods of fixed rational centers as the minimum grows. To deduce cycle exclusion one would still have to force a prohibited approximation at an eligible depth on an actual ordinary candidate. Compactness allows irrational limits in both coordinates. PR #195's remaining high-degree factor can still absorb the cycle determinant. PR #192's finite ordinary trajectories and PR #201's moving rational centers supply neither a fixed rational limit nor the quantitative approximation required here. [Rank-factor obstruction](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/cycle/README.md) · [Finite ordinary inverse competitors](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/cycle/README.md) · [Signed rational checkpoints](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/paired-reductions/SIGNED_ROUTES.md) · [Moving-center bands](https://github.com/GettysburgResearch/collatz/blob/02fb390a76fb2ffb00fee612649ca23a82d99d31/research/killed-green-head-closure-20261124/thin-band/README.md)
