# A finite period gap and lower bounds for the full reduced denominator

**PROPOSED, with written reasoning, exact finite enumeration and three Lean arithmetic lemmas.** Consider a primitive positive odd cycle
$$
                2^{e_i}x_{i+1}=3x_i+1,\qquad e_i\in\{1,2\}.
$$
Write $p$ for its least odd period, $h=\sum e_i$, $s=\min x_i$, and assume the physical ceiling
$$
                            x_i\le(16s+7)/3.                     \tag{1}
$$
If all phases are integers, then
$$
 \boxed{p\le31\,150\,961\,018\,190\,238\,869\,556
                    \quad\text{or}\quad p>10^{1000}.}            \tag{2}
$$
The bounded least-tripling-disagreement alternative has these hypotheses. A cycle with a higher valuation or a larger relative maximum is outside this result. The first-crossing alternative remains open. [Frozen bounded-cycle hypotheses](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/cycle/CANONICAL_FLOOR.md)

There is a full-denominator version. Allow positive rational phases of odd common reduced denominator $d$ coprime to three and odd numerators. Keep (1) and the exponents above, and assume $\gcd(p,h)=1$.

| Primitive odd period | Necessary full reduced denominator |
|---|---:|
| $10^{100}\le p\le10^{1000}$ | $d>10^3$ |
| $10^{250}\le p\le10^{1000}$ | $d>10^{12}$ |
| $10^{500}\le p\le10^{1000}$ | $d>10^{27}$ |

Here $d=(2^h-3^p)/\gcd(2^h-3^p,C)$, where $C$ is the complete affine numerator. This $d$ is the same at all phases by invertibility of two and three modulo $d$.

The ordinary enumeration leaves **25 necessary pairs** $(h,p)$ for $s\ge2^{71}$, $p\le10^{1000}$. The smallest surviving period is $72\,057\,431\,991$. None of the 25 pairs is asserted to furnish a cycle. Barina's verification below $2^{71}$ would restrict a nontrivial ordinary cycle to that list throughout the finite period range. Bound (2) itself needs no verification of small trajectories, since an integer cycle with $s<2^{71}$ has at most $(16\cdot2^{71}+7)/3$ distinct positive states, below its stated left threshold. [Exact pairs and denominator counts](PERIOD_CONTROLS.json) · [Barina, *Improved verification limit for the convergence of the Collatz conjecture*, §6](https://doi.org/10.1007/s11227-025-07337-0)

## Located cells in the numerator lattice

Write $\gamma=\log_2 3$, $\epsilon=h/p-\gamma$. The cycle product gives
$$
          0<\epsilon=\frac{1}{p\log 2}
                   \sum_i\log(1+1/(3x_i))<1/(2s),              \tag{3}
$$
where logarithms without a subscript are natural. Restrict first to $s\ge2^{30}$. Put $R=53336/10000$, $Q=100001/100000$. The product of up to $10\,000$ individual correction factors on any actual word is at most $Q$, by $(1+t)^L\le1/(1-Lt)$ for $Lt<1$. Even $(16s+7)/(3s)$, multiplied by $Q$, is below $R$.

Put a middle phase $y$ in the half-open bin $a/b\le y/s<(a+1)/b$. For $j$ odd steps with cumulative exponent $A_j$, the reverse-word requirements at each prefix are
$$
 (a+1)2^{A_j}\ge b3^j,\qquad a2^{A_j}\le Rb3^j .
$$
Indeed the uncorrected reverse phase $y2^{A_j}/3^j$ is the actual reverse phase multiplied by all $j$ positive corrections. The forward-word requirements are
$$
       a3^j\le Rb2^{A_j},\qquad (a+1)Q3^j\ge b2^{A_j}.
$$
Starting with $A_0=0$, sum the two counts for $A_j-1,A_j-2$ whenever the inequalities permit $A_j$. Denote the reverse count after $k$ steps by $W_k^-(a,b)$ and the forward count after $f$ steps with final exponent $A$ by $W^+_{f,A}(a,b)$. There are only a bounded number of relevant grades at each row, since every physical $2^{A_j}/3^j$ lies strictly between $1/8$ and $8$.

Fix the actual denominator $d$ and an upper bound $d s\le S$. A past of $k$ odd steps constrains the **middle numerator** to one residue modulo $3^k$, since its multiplier at that end is a power of two. A future with total exponent $A$ constrains the same numerator to one residue modulo $2^{A+1}$, since the terminal numerator is odd. This includes empty words. The middle-numerator bin has width at most $S/b$. Thus its population is at most
$$
          W_k^-(a,b)\sum_A W^+_{f,A}(a,b)
                    \left\lceil\frac{S}{b\,3^k2^{A+1}}\right\rceil .        \tag{4}
$$
Every pair of words in this count may be included, even when it occurs on no trajectory. Minimize over the tested $k,f$, independently for each bin. The earlier strip theorem counted a complete past with a global height cap. The earlier middle-gap lemma used simultaneous division on the difference of two physical gaps. Equation (4) keeps the actual grade totals, endpoint parity, physical interval and reduced denominator in one count. [PR200, Theorem S](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md) · [PR195, middle-gap congruence](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-global-closure-20261124/round10/arithmetic/README.md)

At the denominator-13 cycle with numerators $283,431,653,493,373$, both $493/13$ and $373/13$ have one preceding and one following exponent two. Their distance $120/13$ is strictly below the joint integer spacing $3\cdot2^3=24$. Their numerator difference is $5\cdot24$, as required by (4). Full dyadic order in itself gives no such ordinary spacing for the rational values. Lean checks the shared-path difference formula at arbitrary denominator, the product spacing with the odd-endpoint bit, and the span bound for an arbitrarily long ordered cell. [PeriodPacking.lean](PeriodPacking.lean)

## Which rank intervals must be filled

For ordinary $s>1$, (1) implies $\max x_i<8s$. The full dyadic lift $F(2^t x_i)=2^t(3x_i+1)$ has no inversions, acts by a shift of $h$ on its increasing ranks, and gives $\gcd(p,h)=1$. Indeed an inversion needs two odd integers $x,y$ with $0<3(y-2^k x)<2^k-1$, hence $k\ge3$, contradicting (1). An increasing bijection of the ordered lifted set is a translation. Its shift is $h$ by the product of the scale factors, and its action modulo $p$ is a single cycle. This argument uses integer spacing. The rational denominator table assumes coprimality separately and only needs the reverse-word count. [Dyadic inversion theorem](../../unconventional-20261126/adelic/DYADIC_CYCLE_ORDER.md)

Normalize every ordinary phase $x_i=2^{j_i}z_{r_i}$ into $s\le z_{r_i}<2s$, with $j_i\in\{0,1,2\}$, $r_i=ih\bmod p$, starting at $x_0=s$. The increasing normalized positions satisfy
$$
            \big|\log(z_r/s)-(r/p)\log 2\big|\le p/(12s).        \tag{5}
$$
The difference is the sum through $i$ edges of $\log(1+1/(3x_j))$ minus $i/p$ of its complete sum, by the lifted rotation. This equals $i(p-i)/p$ times the difference of the means on the two complementary arcs. Each summand lies in $[0,1/(3s)]$. [PR195, normalized rank estimate](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-global-closure-20261124/round9/critical/README.md)

For each surviving first-pass pair the checker verifies $1000\le p\le s_0/100$, where $s_0$ is the lowest retained height-bin endpoint for that same pair. Equation (5) and $x_i\ge z_{r_i}$ improve the upper height estimate to
$$
            s\epsilon\ \le\
      \frac{\exp(p/(12s))}{3\log 2}
          \left(\frac{1}{2\log 2}+\frac1p\right)<\frac7{20}.       \tag{6}
$$
Here the mean of $2^{-r/p}$ is bounded by its integral plus $1/p$, and $\exp(1/1200)\le1200/1199$.

For $b\le a<2b$, the number of $z_r/s$ in $[a/b,(a+1)/b)$ is at least
$$
              \frac{2884p}{1000(2a+1)}-\frac{p^2}{s_0}-2 .       \tag{7}
$$
Count the equally spaced points $r/p$ in the logarithmic interval after shaving $p/(12s\log 2)$ off each end. Use $\log(1+1/a)\ge2/(2a+1)$, $1/\log 2>1442/1000$, and allow two endpoint losses. A negative bound causes no exclusion.

This required number must fit across the three **actual** bands. For $j=0,1,2$ use (4) on the scaled phase bin $[2^ja/b,2^j(a+1)/b)$, omitting bins wholly above (1). The tested $b$'s are divisible by four. If the combined upper bound is below (7), that pair is excluded. The three upper bounds may be optimized independently. The approximate geometric positions supply a lower bound on how many slots the selected bin must fill.

## Exact finite search and remaining periods

At height index $t$, put $2^t\le s<2^{t+1}$. For a tested denominator cap $d\le D_0$, first use only pasts ($f=0$) with $S=D_0 2^{t+1}$. Sum (4) over a cover of the whole strip by consecutive bins and minimize over the tested widths and depths. Call the result $P_t$. Every surviving reduced $h/p$ at this height is above $\gamma$, at most $\gamma+2^{-t-1}$, and has denominator at most $\min(P_t,10^{1000})$.

The verifier encloses $\gamma$ in rational endpoints $l,u$ by summing the positive series for $\log 2=2\operatorname{atanh}(1/3)$ and $\log 3=2\operatorname{atanh}(1/2)$, with $6900$ binary places and directed rounding. Repeated integer division tracks the downward-rounded scaled powers. Each divided term loses less than three units on the scaled sum, and at the first zero power the remaining scaled tail is less than two. The allowance of four units per term plus four covers these errors.

For each order $P$ enumerate all reduced fractions in $(l,u+2^{-t-1}]$ via Farey neighbors. The last continued-fraction convergent of $l$ at denominator at most $P$, and the largest allowed intermediate convergent on its other side, have determinant one and denominator sum greater than $P$. The larger is the first fraction above $l$. After $a/b$, the next denominator is the largest $v\le P$ with $av\equiv-1\pmod b$. Its numerator is $(av+1)/b$. This enumerates every reduced fraction in the interval. At $P=10^{1000}$ the first neighbor above $l$ is above $u$. Its gap from $u$ and (3) bound the largest height index by $6640$. This gives finite coverage without importing an irrationality measure.

For $d=1$, the 6570 bins from $t=71$ through $6640$ leave 125 different reduced pairs. Equations (4), (6) and (7) leave the 25 listed pairs and prove (2). For each rational denominator test the program starts at $t=30$. When $s<2^{30}$, distinct odd numerators and (1) imply $p<6D_0\,2^{30}$, below the tested range. All larger heights are covered by the same Farey bound. The whole-strip past count already excludes every reduced pair in each rational test. The largest required precomputed depth is 4248. Direct enumeration of short words and small Farey orders cross-checks both routines. [Exact arithmetic verifier](check_period_gap.py) · [Output](PERIOD_CONTROLS.json)

**First unsupported step.** Large future partial quotients of $\log_2 3$ can make the admissible numerator intervals wide again. Some smaller pairs survive both physical cylinders. Chudnovsky's Theorem 11.1 states $\mu(\log_2 3)\le3$. With that input, a uniform source-count exponent strictly below $1/3$ would give an asymptotic contradiction on these coprime clocks. The published strip exponent $479/1000$ exceeds this threshold. The finite results use neither the irrationality-exponent claim nor independence between digit systems. They decide no ordinary cycle at a surviving pair and give no fate for an escaping source. [Chudnovsky, arXiv:2610.28079v1, §11](https://arxiv.org/html/2610.28079v1#S11) · [Related narrow-cycle approximation bounds, rStation 145/v1](https://rstation.ai/problems/collatz/papers/145/v1)
