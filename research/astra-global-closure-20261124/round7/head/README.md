# One directed head suffix suffices, and its two-sided mass controls the full series

**PROPOSED.** Throughout, $T(2n)=n$, $T(2n+1)=3n+2$, and $C$ is the set of positive ordinary integers reaching 1. Each of the following hypotheses, by itself, is equivalent to universal convergence:

1. For every positive odd $u$ prime to three, $u\in C\Rightarrow 3u\in C$.
2. For every positive odd $u$ prime to three, $3u\in C\Rightarrow u\in C$.
3. On every sufficiently high tested head row described below, every tested parent in $C$ has its child in $C$.
4. On those rows, every tested child in $C$ has its parent in $C$.

Only the suffix **57 modulo 81** is needed in statements 3 and 4. The [six-prefix construction](ODD_RAY.md) additionally transports *each specified surviving odd pair* of PR193/round six into a single odd-unit tripling pair with its ordered ordinary components preserved. It applies in particular to the explicit residuals $3^{18j}-1$. The unit implication itself remains open.

## Finite directed paths

Use ordinary edges in either direction. In the first table, traverse $3u\to u$ only when $3\nmid u$. Reading a certified path backwards propagates membership by hypothesis 1. In the second, traverse $u\to3u$ on units, and use hypothesis 2 backwards. The third table joins $n$ to $3n$ on all positive odd $n$, allowing both orientations. Every extra move in all three tables uses an **odd** unit $u$.

| Table | Source | Leaves | Largest modulus | Letters | Unit comparison positions | Largest length | Maximum $u/n$ |
|---|---|---:|---:|---:|---:|---:|---:|
| Forward basin implication | All $n\ge2$ | 40 | 144 | 151 | 24 | 18 | $167/27$ |
| Reverse basin implication | All $n\ge2$ | 172 | 186624 | 1586 | 90 | 30 | $2351/123$ |
| Two-sided substitution | All odd $n\ge1$ | 33 | 864 | 423 | 59 | 26 | $59/3$ |

A row $(A,B)$ denotes all $At+B$ with $t\ge0$. For a rule $is+j\to ks+l$, validation checks $A=iA'$, $B=iB'+j$, then replaces the row by $(kA',kB'+l)$. The four extra letters have exactly the input/output pairs $9s+3\leftrightarrow3s+1$ and $9s+6\leftrightarrow3s+2$. The first two tables end at $A't+B'$ with $A'\le A$ and $0<B'<B$. The respective maximum endpoint/source ratios are $8/9$ and $3398/3579$, including both the base and the limiting slope. Strong induction proves the directed conclusions from the given hypothesis. The third table ends exactly at $3At+3B$. Its 59 extra-move positions across all rows each have an injective affine query map with strictly positive slope. The kernel checks the paths on entire progressions, including the root covers, in [UnitTripling.lean](UnitTripling.lean). [Independent arithmetic replay](check.py)

For example, on $n=18t+9$ the third path uses exactly the two forward triplings at $96t+49$ and $192t+97$. Its ordinary segments connect $n$ to the first unit, its triple to the second unit, and the latter triple to $3n$. This row illustrates why the two-sided count below makes no independence assumption and why imposing a bound on the stopping time of every intermediate antecedent requires further work.

A nonconvergent positive ordinary vertex $n$ forces a failed forward unit test with $u\le(167/27)n$, and, separately, a failed reverse unit test with $u\le(2351/123)n$. To see this, repeatedly follow the descending table until a path has differently colored endpoints or reaches 1. On the first path with a change from an outside start to an inside endpoint there is a failing unit implication of the stated orientation. All prior table starting values have decreased. These failures need not involve the same unit.

## A prescribed arc and one orientation

Fix an open interval $J\subset(7,8)$, integers $L\ge1$, $c\bmod L$, and $Q\ge0$. Set $R_j=81^j$. Test the children $x=81y+57$ for which $j\equiv c\pmod L$, $x/R_j\in J$, $2^Q\mid x$, and $y\equiv-1\pmod8$ on rows $j\ge1$. These parameters can be chosen arbitrarily before the test.

For a positive unit $u$, choose $k_0<18$ with $2^{k_0}u\equiv-1\pmod{27}$. All $k=k_0+18t$ have that property. Set $b=(2^ku+1)/27$, $y=8b-1$, and $x=81y+57=2^{k+3}(3u)$. Three odd steps give $T^3y=27b-1=2^ku$. Thus $T^{k+3}y=u$ and $T^{k+3}x=3u$. Taking $k\ge Q$ supplies the divisibility. On the circle of length $L$, successive $\log_{81}x$ differ by $18\log_{81}2$, whose ratio to $L$ is irrational. A fixed finite block of advances hits $c+\log_{81}J$ from every starting phase. This gives arbitrarily high witnesses, and a finite multiplier menu with $u\le x\le K u$ for one witness, uniformly in $u$. One fixed failing unit therefore yields the prescribed *ordered* disagreement on a syndetic set of high level indices. This is PR197's $p=3$ construction, now sufficient on its own by the two finite directed tables. [PR197 routing and schedule](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/PERIODIC_FOUR_SUFFIX_SCHEDULE.md)

Pointwise one can also require the odd part of the tested child to be at most **any** fixed function $G(j)\to\infty$. For each individual failed odd unit $u$ that part is exactly $3u$ at every lifted witness. This extra growing restriction is used only for the pointwise equivalence. For instance a choice $G(j)=j$ allows only $O(j)$ candidates per row, since each odd part has at most one dyadic multiple in a band of ratio $8/7$. Those row fractions are automatically summable and furnish no summability criterion with this growing restriction.

## The full two-sided series and its power threshold

For any orbit-invariant label $f$, set $D(n)=1_{f(n)\ne f(3n)}$. Let $D_o(X)$ and $D_*(X)$ count disagreements through $X$ on positive odd integers and positive odd ternary units respectively. The 33-row substitution proves the explicit inequality

$$
                 D_o(X)\le59 D_*((59/3)X).
$$

If a path has different endpoint labels, some extra move changes labels. For each of the 59 positions, its positive affine map $n\mapsto u$ on the given row is injective, and $u\le(59/3)n$. This counts *actual label disagreements*. Physical nonmerger before a finite deadline would not justify it. For fixed $0<\alpha<1$, in particular, no exponent is lost in passing to the odd units.

Write $a_j$ for the normalized count of all discordant heads in $[7R_j,8R_j)$, with parent $\lfloor x/81\rfloor$, and $s_j$ for the normalized count of discordant heads at the specified single suffix, arc, schedule and fixed divisibility above. Both orientations are counted, and unused rows have $s_j=0$. There are constants $K,C$ depending only on the fixed restrictions such that

$$
 \sum_{1\le j\le N}s_j\le\sum_{1\le j\le N}a_j
       \le C\left(1+\sum_{1\le j\le N+K}s_j\right).
$$

Indeed the actual-label variation inequality and the 81-step triangle argument give $a_j\ll R_j^{-1}\sum_{n\le C_0R_j}D(n)$. Summing up to $N$ and exchanging nonnegative sums charges each $n\le C_0R_N$ at most $O(1/n)$. By dyadic invariance $D(2^e n)=D(n)$, so charging the odd parts costs at most the geometric sum 2. Substituting the 59 fixed affine positions in the harmonic sum costs at most $59\cdot59/3$, since $1/n\le(59/3)/u$ and every query map is injective on its row. The fixed finite head menu sends each odd unit to a true comparison with the same orientation, at $x\le K' u$ and $1/u\le K'/x$. Each child has at most the menu size in antecedents. On row $\ell$, $1/x\ll R_\ell^{-1}$. The query and head height bounds keep $\ell\le N+O(1)$. The additive constant accommodates the bottom rows. [PR146 actual variation](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/TRIPLING_VARIATION.md) · [PR197 full-row triangle](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/FOUR_SUFFIX_EQUIVALENCE.md)

If $R_js_j=o(R_j^\alpha)$ for all large rows, the finite head menu gives $D_*(X)=o(X^\alpha)$ by geometric row summation. The 59-position inequality yields $D_o(X)=o(X^\alpha)$. Summing $D_o(X/2^e)$ over $e\ge0$ preserves the little-o bound because $\alpha>0$. The full-row inequality gives $R_ja_j=o(R_j^\alpha)$. In the basin-of-one case the fixed-target positive-density theorem is required only for the imported conclusion that summability rules out a counterexample. Independently, the PR197 full-row rigidity criterion using Krasikov–Lagarias applies at $\alpha=.84$. Hence a counterexample would force $\limsup_j R_j^{1-.84}s_j>0$; the exponent applies to the union of the two directions. The corresponding upper bound for that union remains open. [PR197 criterion and scope](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/FOUR_SUFFIX_EQUIVALENCE.md) · [Krasikov–Lagarias, primary paper](https://arxiv.org/abs/math/0205002)

PR146 already obtained two-way component sufficiency on odd units $1\bmod16$ by a ternary occupancy argument with an external predecessor exponent. Its six-residue ordinary-height estimate has different restrictions. PR146 also proved separate one-sided equivalences with other input conditions. The two finite directed ordinary descents here and the 33-row bounded substitution have no analytic input. The reduction to one literal suffix uses PR197's existing placement argument. The centered-neighbor and track counts at the same PR preserve their original-source hypotheses; they do not give an upper bound for this one-suffix series. [PR146 ternary digits](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_TERNARY.md) · [PR146 one-sided results](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md) · [Yolcu–Aaronson–Heule, mixed-base rewriting background](https://doi.org/10.1007/s10817-022-09658-8)
