# Optimal inverse clocks at the ordinary cycle minimum

**PROPOSED, with Lean-checked ordinary arithmetic.** In the bounded alternative for the least odd tripling disagreement, let $s=(3q-1)/2$ be the cycle minimum, and let $p,h$ be the primitive odd and shortcut periods. For every window in one lap, its actual shortcut clock $A$ is within two of the least clock over **all positive ordinary odd preimages of its endpoint with the same odd count**. A competitor starting at a multiple of three can save at most one clock. At $s$ the native word is an exact minimizer. After the initial merger, the least clock from a multiple of three is exactly $A+1$. These results hold at every possible period. Competitors may use arbitrarily large valuations.

This gives arithmetic exclusions within windows that fit the required width. Whether every nontrivial physically eligible word admits such an exclusion remains open, as does universal exclusion of full divisibility $D\mid C$.

## Source and clock comparison

Use the shortcut $T(2v)=v,\ T(2v+1)=3v+2$. A path from a positive odd $z$ to an odd endpoint $y$ with $k$ odd inputs and $B$ shortcut clocks satisfies $2^B y=3^k z+C$ with $C\ge0$. A reverse odd word $e_1,\ldots,e_k$ reads from the endpoint, successively applying $(2^{e_i}y-1)/3$ on its domain. An integral inverse at a positive odd unit stays positive and odd. A multiple of three can occur at the last site and has no further odd predecessor.

Here $q$ is the least positive odd source whose membership in the basin of 1 differs from that of $3q$. In the bounded alternative $q$ is good, $2s+1=3q$, and each odd cycle phase satisfies $s\le x\le(16s+7)/3=(24q-1)/3<8q$. Its valuations are one or two. Every positive bad $z$ satisfies $8z+1\ge9q$, equivalently $4z\ge3s+1$. Every bad multiple of three is at least $3q=2s+1$. All ancestors of a bad endpoint are bad. [PR192 leastness proof](../../astra-minimum-source-20261124/minimal/MinimumFailure.lean) · [PR205 bounded branch](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md)

For every $k$, any rival ending at a bad phase $y<8q$ satisfies
$$
                     9\cdot3^k <64\cdot2^B .
$$
Indeed $64z\ge72q-8>9y$ and $3^kz\le2^By$. This holds at arbitrarily large depths. When $3\mid z$, the stronger $3\cdot3^k<8\cdot2^B$ follows from $z\ge3q$.

For a native window $x\to y$ of $k$ odd steps and shortcut cost $A$, write $\Lambda=2^h/3^p$. Each odd step contributes the factor $1+1/(3x_i)>1$ to the full-lap product. Consequently $2^Ay/(3^kx)\le\Lambda$ on every subwindow. Equivalently, apply the ordinary gain bound to the complementary arc $y\to x$. If a rival with the same $k,y$ saves $j$ clocks, then $2^jz\le\Lambda x$.

### Elementary full-period bound

Five preceding valuations in $\{1,2\}$ put any terminal odd point in at most $2^5=32$ classes modulo $3^5$. Each word fixes its endpoint modulo $3^5$ by its affine equation, since two is invertible there. Oddness gives one class modulo $486$ per word. This includes $p<5$, when the five-step path wraps. The $p$ distinct odd points lie in an interval of length at most $(13s+7)/3$. Hence
$$
       p\le32\left(1+\frac{13s+7}{1458}\right)\le s/3
                      \qquad (s\ge729).
$$
The slope and the comparison at 729 are checked by integer arithmetic. Direct iteration of every $1\le s<729$ reaches one within 108 shortcut steps.

Thus $\Lambda\le(1+1/(3s))^p\le9/8$. The binomial expansion is bounded by the geometric sum with ratio $p/(3s)\le1/9$. This deduction is independent of logarithmic-form estimates. The same $9/8$ bound applies to any window with at most $s/3$ odd steps, including windows crossing several laps.

A saving of three would give $64z\le9x$, contradicting $64z>9x$. For a multiple of three a saving of two would give $32z\le9x<72q$, contradicting $z\ge3q$. At $x=s$, a saving of one gives $16z\le9s$, contradicting $4z\ge3s+1$. A multiple of three at $s$ must cost strictly more than the native word, since even $B\le A$ gives $8z\le9s<8(2s+1)$. [Ordinary comparison kernels](InverseClocks.lean)

### Attainment from a multiple of three

Write $s+1=2^mu$ with $u$ odd. The initial singleton exit gives $3^mu=4v+3$. The $s$ arm makes $m$ odd steps to $4v+2$, then one even and one odd step to $3v+2$. The $2s+1$ arm makes $m+1$ odd steps to $12v+8$, then two even steps to $3v+2$. Their odd counts there both equal $m+1$, and their shortcut clocks are $m+2,m+3$. Every common continuation preserves the count equality and the clock difference. Since $2s+1=3q$, the native path and this partner attain
$$
 \left(\min_{z\ {\rm arbitrary}}B,\ \min_{3\mid z}B\right)=(A,A+1)
$$
for every subsequent odd endpoint within the indicated distortion bound. The minima range over positive ordinary odd sources with the specified endpoint and odd count. The result applies to repeated laps containing at most $s/3$ odd steps. The earlier all-depth cone holds beyond that horizon.

## A forbidden window throughout the strip

Read the following 19 exponents **backwards** from an odd endpoint.

| Path | Reverse exponents | Shortcut cost | Source |
|---|---|---:|---|
| Native | 1221212222121212121 | 30 | $x=1686831099+2^{31}t$ |
| Rival | 3341221111111111111 | 28 | $z=421707775+2^{29}t$ |

Their common endpoint is $1825894037+2\cdot3^{19}t$, and $4z=x+1$ for every $t\ge0$. The native word fixes exactly the displayed binary cylinder: its affine equation determines $x\bmod 2^{31}$ after the endpoint is required to be odd. The rival's cylinder follows in the same way. One further native backward exponent equal to one gives $x=2\bmod3$. Then $3\mid z$ and $x<8q$ implies $z<3q$. The full 20-symbol reverse word **12212122221212121211** is consequently impossible at any phase of the bounded bad cycle. Without this basin premise, both rows consist of positive ordinary trajectories. The largest-to-smallest ratio of their native 20-symbol *ideal* reverse-prefix heights is $59049/16384<4$, inside the geometric strip. The actual merger and goodness conclusion for all binary lifts are Lean-checked.

## Complete inverse tests on ordinary finite windows

An ordinary CRT progression admits 32 steps to each side of its central minimum. The forward cumulative valuations are $\lfloor i\log_2 3\rfloor$, the backward ones $\lceil i\log_2 3\rceil$, computed by integer bit lengths. They specify binary and ternary cylinders respectively. The stride contains an extra $3^{25}$ so every endpoint and every inverse word through depth 24 retains the requisite residue on all lifts. The base value and the coefficient of the lift give all 65 observed phases in $[s,2s)$, with the central phase minimal.

For all 1,260 subwindows of length at most 24, the checker visits **every** legal inverse word with $B\le\lfloor\log_2(4\cdot3^k)\rfloor$. This covers the native cost and all rivals capable of reaching the known good interval or a smaller multiple of three. Indeed reversal gives
$$
 z=2^B3^{-k}(y-\eta),\qquad
 0\le\eta=\sum_{j=1}^k3^{j-1}2^{-(e_1+\cdots+e_j)}\le(3/2)^k-1 .
$$
Since $y\ge s>2\cdot3^{24}$, a source with $z\le2s$ must have $2^B<4\cdot3^k$, uniformly on the progression. At a ternary unit the recursion tries every valid exponent up to the remaining budget, reserving at least one clock per remaining edge. It permits a multiple of three only at the terminal depth. The 3,327 terminal source formulas are affine on the progression. Inequalities on each intercept and slope give both required source lower bounds on every lift. All 22 central windows of lengths 3 through 24 meet the exact pair of required optimal clock values. This controls finite segments of genuine ordinary trajectories and supplies neither a closed lap nor an infinite bad trajectory.

The formal file imports the project's actual basin through **SourceDeletion** and **MinimumFailure**. It proves the ordinary gain, all-depth cone, complementary-arc distortion, rival size, clock optimality from the numerical distortion premise, the sharper multiple bound, the singleton merger with odd counts, the quarter merger on every lift, and the basin exclusion. The five-step count and the deduction of the numerical distortion bound are written arguments. The small-source check and the lift controls are exact finite Python runs. [Exact checker](check.py) · [Control output](../../../reports/astra-diagonal-closure-20261125/cycle/control.json) · [Lean output](../../../reports/astra-diagonal-closure-20261125/cycle/lean.log)

The first unsupported inference is that **every** eligible nontrivial word satisfying full ordinary divisibility must violate a least-source or clock test somewhere on its cycle. The forbidden word gives one genuine exclusion, while the finite ordinary progression meets all tested alternatives simultaneously. PR195's two-filter theorem still gives an independent exact divisibility decision for a supplied word. The separate first-crossing alternative remains unaffected. [PR195 full-denominator criterion](https://github.com/GettysburgResearch/collatz/blob/4fd8af31c1ea525252b4d8f7411b5921dd447048/research/astra-global-closure-20261124/round11/cycle/README.md)
