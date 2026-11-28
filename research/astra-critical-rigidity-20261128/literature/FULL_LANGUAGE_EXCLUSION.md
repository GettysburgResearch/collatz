# A supercritical parity word with every finite factor and an irrational 2-adic source

**Proposed written application of the quantitative reference theorem.** There is an explicit computable shortcut parity word $W$ with all of the following properties.

1. Every finite binary word occurs arbitrarily late in $W$. The odd frequency tends to $5/7$ along all prefixes. A hypothetical positive real orbit executing these affine branches would grow at least as fast as $2^{(5\log_23/7-1+o(1))d}$ at time $d$.
2. At infinitely many prefix lengths $D$, the word admits $O(\ln D\sqrt{\ln\ln D})$ actual rational reference arcs of maximum endpoint logarithmic height $O(\sqrt D)$. For a putative rational source the arcs can be chosen separated at every start. Durations of individual supplied arcs are $o(D)$ even when compared to the elapsed time immediately before them.
3. The unique $2$-adic integer with itinerary $W$ lies outside $\mathbb Q$. The certificate uses the growing-dimensional [quantitative reference bound](QUANTITATIVE_REFERENCE_COVERS.md). The word displays the difference between its literal factor count $2^n$ at each length $n$ and the cost of referencing actual rational trajectories.

The periodic forcing superposition below specializes the [independent-clock construction in PR212](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md). Its role here is to give inexpensive, increasingly long **negative** rational reference arcs for an open, supercritical word.

## Two coprime clocks in a supercritical cell

Fix $m\ge2$. Start each seven-letter cell with $111$, followed by two successive pairs, initially both $10$. In cell $j$ reverse the first pair to $01$ when $m\mid j$ and the second when $m+1\mid j$. One full word $V_m$ uses cells $j=0,\ldots,P-1$, where $P=m(m+1)$. It has duration $L=7P$ and grade $5P$. Set $A=128$, $N=243$. At cell boundaries the affine recurrence is

$$
 A x_{j+1}=N x_j+227+24\mathbf1_{m\mid j}+32\mathbf1_{m+1\mid j}.
$$

Indeed moving a single odd bit at clock $i$ one place later adds $2^i3^a$ to the carry, where $a$ is the number of later odd bits. The two chosen clocks give $2^3 3$ and $2^5$. The corresponding rational periodic root is exactly

$$
 x_0=\frac{227}{A-N}
       +\frac{24N^{m-1}}{A^m-N^m}
       +\frac{32N^m}{A^{m+1}-N^{m+1}}.
$$

The constant, the period-$m$ impulse and the period-$(m+1)$ impulse give the three terms by linearity. For a single impulse $u$ at the first cell of a length-$r$ lap the combined carry is $uN^{r-1}$. Its fixed source is $uN^{r-1}/(A^r-N^r)$. The full reduced denominator $q_m$ divides $|(A^m-N^m)(A^{m+1}-N^{m+1})|$, because $A-N$ divides both factors. Thus $\log_2 q_m=O(m)$.

The affine fixed source of a finite binary word is always $2$-integral: its denominator divides $2^L-3^g$, which is odd for $L\ge1$. The unique residue mod $2^L$ whose first $L$ actual shortcuts realize the given word is the solution of $3^g x+C\equiv0\pmod{2^L}$. This follows by induction, with each next bit fixing the next binary digit of $x$ because the centered slope numerator is odd. The affine center obeys that congruence, so the entire prescribed closed word is physical. The reduced denominator in this construction is also prime to three and stays constant under every actual departure. At cell boundaries the backwards recurrence sums forcings between $227$ and $283$ against a positive geometric kernel with total mass $1/(N-A)$, so $|x_j|\le283/115$. The seven intermediate branches give $|x|<60$ throughout. Each phase is negative, since the fixed-point formula at any rotation has positive carry and negative determinant. In particular every phase has logarithmic height $O(m)$.

The **least** binary period equals $L$. A repetition count $k$ divides both the duration $7P$ and the grade $5P$, hence divides $P$. The period $7P/k$ is therefore a whole number of cells. The two marked slots recover the indicator sequences, whose respective least periods are $m$ and $m+1$. A whole-cell period must be divisible by $P$.

## Concatenation and its reference cover

Enumerate finite binary words $u_j$, $j\ge1$, by increasing length and lexicographically within a length, starting with the empty word. For each $t\ge1$, append

$$
 r_t=\Big\lceil\sqrt{\lceil\log_2(t+2)\rceil}\Big\rceil
$$

copies of $V_{2^t}$; after **each copy** append the literal connector $1u_j$, advancing the global index $j$ by one. Then each finite word occurs arbitrarily late: it appears inside infinitely many listed extensions. In particular no tail is periodic. Through group $T$, let $J_T=\sum_{t\le T}r_t$ and let $D_T$ count all shortcut letters. Monotonicity of $r_t$ and comparison with the final half of the groups give

$$
  J_T\asymp T\sqrt{\ln(T+2)},\qquad D_T\asymp 4^T r_T .
$$

All complete seven-letter cells have exactly five odd bits. At arbitrary prefix ends, the total discrepancy from the frequency $5/7$ is at most the total connector length plus seven. For a prefix in group $T$ that error is $O(J_T\log(J_T+1)+7)$, while its length is at least $D_{T-1}$ apart from the fixed initial group. The frequency statement follows. The cumulative homogeneous multiplier at clock $d$ is $3^{g_d}/2^d$; a positive initial value and nonnegative affine offsets give the claimed real growth.

Use each $V_m$ as one reference arc starting at its actual periodic rational source. If a putative physical source of $W$ met that point at the arc start, its remaining parity sequence would be periodic, impossible. A connector of length $b$ is realized by two distinct positive integers $a,a+2^b$ with $1\le a\le2^b$, using its parity residue. Choose one different from the physical starting point. Its final positive integer is at most $(3/2)^b(2^{b+1}+1)$, since each step sends $x+1$ to at most $(3/2)(x+1)$. This gives separated references for any proposed physical source, of either sign. Including all connectors, the maximum reference height $H_T$ and arc count $K_T$ satisfy

$$
 \log_2 H_T=O(2^T+\log J_T)=O(\sqrt{D_T}),\qquad
 K_T\le2J_T=O(\ln D_T\sqrt{\ln\ln D_T}).
$$

Each individual cycle piece in group $T$ has length $7\cdot2^T(2^T+1)=O(4^T)$, and even before its first such piece at least $D_{T-1}\gg4^{T-1}r_{T-1}$ steps have elapsed. Connector lengths are smaller still. This verifies the stated $o(1)$ relative duration.

## Signed rational exclusion

The signed version of inequality (10) in the [quantitative reference proof](QUANTITATIVE_REFERENCE_COVERS.md) holds with $\log_2\max(|a|,q)$ for any physical $a/q\in\mathbb Q\cap\mathbb Z_2$ in lowest terms, with $q>0$. Here are all changes needed. Keep the global odd scale $q$, scaled integer states $A_i=qx_i$ and reference budget $H_0=\max(2,qH)$. Use $Y(A)=|A|+2H_0+2$. The two one-step updates satisfy $Y(A')\le(3/2)Y(A)$ by the triangle inequality. The single-arc divisibility estimate uses $|A|+H_0$, including zero. In a fast high packet all physical boundary magnitudes exceed $10(m+1)3^mH_0$ as before. At every pair of successive boundaries the ratio $y/(\lambda x)=(1-\xi/x)/(1-\eta/y)$ is in $[1/2,2]$, so all these physical signs agree. Normalize every telescope coordinate of this packet by that common sign and replace $s,e,x_i$ in the absolute bounds by $|s|,|e|,|x_i|$. The dominance, product, gcd, height and lower bounds follow identically, including $|e-\eta|\ge |e|-H_0$. The primitive basis norms, mesh estimates and record charges depend only on these magnitudes. Hence equation (10) and its inversion apply also to negative rationals.

Finite parity cylinders are nested and specify one residue at each dyadic precision, so $W$ has a unique $2$-adic source. If it were rational, the fixed initial height and $\log_2 H_T=O(\sqrt{D_T})$ would force $K_T\gg\ln D_T\ln\ln D_T$ by (10), contradicting the constructed count. This rules out every rational source for this word. It leaves open the itineraries of exceptional positive ordinary Collatz orbits.

## Cost of replacing a supplied stage by periodic literal templates

Take one native stage $V_m$ of least duration $L$. Consider any cover of this whole stage by factors of binary periodic sequences of periods at most $B<L$. A factor beginning at any phase of a period-$b$ sequence has as references the native rational centers of that sequence at its start and end. Their heights are at most $3^{O(B)}$: the fixed denominator divides $2^b-3^g$, and the word carry is at most $3^b$ by the positive affine recurrence. Its phase cannot equal a native point of $V_m$, because equality would force the least period of that point to divide $b<L$. For an arc of duration $l$, clearing its two reference endpoint denominators by $C\le3^{O(B)}$ in the difference equation yields

$$
 2^l\mid q_m C(x-\xi)\ne0,\qquad
 |q_m C(x-\xi)|\le q_m C(60+3^{O(B)}).
$$

Indeed $q_m C$ also clears the actual and reference endpoints, so the dyadic power divides that integer by coprimality with the odd slope numerator. Thus $l=O(m+B)$ and the stage needs $\gg L/(\sqrt L+B)$ such pieces. In particular for each fixed $\theta<1$ and $B\le L^\theta$ this lower bound grows polynomially in $L$, while our supplied stage has one actual rational reference. This is a separation between two specified cover costs. It does not assert that previous results could never exclude $W$ by another argument.

The [exact checker](check_full_language_exclusion.py) recovers the four cell carries, the independent-clock root and its full reduced denominator divisibility, least period, physical parity, sign and real bound at 15,792 rational vertices across ten stages. It computes exact optimal period-at-most-seven piece counts, including 124 pieces at $m=32$, and checks the partition routine against complete enumeration through eight bits. Its six-group prefix has 78,241 letters. The infinite irrationality argument uses the written quantitative theorem.
