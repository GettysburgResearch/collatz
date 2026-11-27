# A physical return from thirteen rank-three phase progressions

**PROPOSED.** Let $C(x)$ denote an ordinary hit at one and let the height floor at $z$ be
$$
      0<n,\quad 2^{40}n<z \quad\Longrightarrow\quad C(n).
$$
The previously verified quantitative return supplies this floor at a least canonical reverse disagreement. Each of the thirteen infinite progressions below satisfies $C(z)$ under its own floor, so none can contain that least disagreement. The conclusion applies to every supplied parameter in the listed progression. The remaining third-odd exponents and phases constitute an open case. [Quantitative return](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/QUANTITATIVE_RETURN.md) · [rank-three explicit upper words](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/RANK_THREE_RESTRICTION.md)

## A four-unit change of signed phase

For every even $N=2k+2\ge4$ put $X=3^N-17$ and $Y=3^{N-1}-7$. Both are positive. Write $3^{2k+1}=8a+3$; then $a\ge1$, $X=24(a-1)+16$ and $Y=8(a-1)+4$. Three shortcuts send each to $3(a-1)+2$: the first word is three even inputs, the second two even inputs followed by an odd. On the signed $-5$ cycle, $3k$ clocks have $2k$ odds and return to $-5$. One more odd reaches $-7$. The ordinary positive
$$
               w=2^{3k+1}-5
$$
therefore reaches $Y$ at clock $3k+1$ by the affine lift at signed $-5$. In particular $C(X)\iff C(w)$. This local identity takes two specific integer inputs at each exponent. Its longer incoming arm realizes the signed $-5$ cycle exactly. [Kernel three-clock merger and physical visitor](PhaseReturn.lean)

## Upper hit parameter and lower phase

For a canonical triple with three upper odd inputs, the first two occur at clocks zero and one. Write $e$ for the number of even inputs between the second and third odds, and $H=e+b+3$ for the upper hit clock, allowing $b$ halvings after the third odd. The resulting source obeys
$$
                  81z=2^H-15-2^{e+2},\qquad z=17\bmod48.
$$
In each row $H=H_{\mathrm{first}}+162m$. The displayed $m_0$ gives a base $H_0=H_{\mathrm{first}}+162m_0$ at which the ordinary lower arm reaches $3^{N_0}-17$ in exactly $H_0$ clocks with $N_0+4$ odds, where $N_0$ is even. All $m=m_0+11t$ for $t\ge0$ then work. The row $e=26$ also has the preceding representative $m=0$ of that residue class; its actual positive lower trajectory hits one at clock 338.

| $e$ | $H_{\rm first}$ | $m_0$ | $H_0$ | $N_0$ |
|---:|---:|---:|---:|---:|
|17|51|1|213|126|
|23|147|0|147|80|
|24|90|10|1710|1074|
|25|71|7|1205|752|
|26|62|11|1844|1158|
|27|121|1|283|164|
|28|124|9|1582|990|
|29|81|9|1539|962|
|30|168|1|330|192|
|31|59|3|545|328|
|33|163|4|811|496|
|37|47|8|1343|832|
|48|78|8|1374|844|

To advance one row take $H_t=H_0+1782t$ and $81z_t=2^{H_t}-15-2^{e+2}$. Since $2^{1782}=1\bmod81$ the difference from $z_0$ is $2^{H_0}(2^{1782t}-1)/81$. The same first $H_0$ lower steps now finish at $2^{1782t}3^{N_0}-17$. The signed $-17$ cycle has period 11 and seven odd inputs; its next $162t$ laps consume $1782t$ physical clocks, sending that lifted integer to $3^{N_0+1134t}-17$. Thus the actual visitor $w_t=2^{3(N_0/2-1+567t)+1}-5$ has $C(w_t)\iff C(z_t)$ by the three-clock merger. This is the uniform part of the proof; a finite replay need only check the thirteen starting words and one lap.

For all rows $2^{40}(w_0+5)<2^{81}z_0$ by integer comparison. Also $w_t+5=2^{1701t}(w_0+5)$ and $z_t\ge2^{1782t}z_0$ by its fixed negative offset. Thus $2^{40}w_t<z_t$ for every $t\ge1$. At $t=0$ the same strict floor comparison already holds except in rows $e=17,23,27,30$. Their base $z_0$ hit one at clocks 1153, 675, 1426, 2034 respectively. These checks suffice for the claimed fixed-source exclusions. The kernel verifies every initial upper and lower word, each exceptional base, the additional $e=26$ source at $m=0$, and the full floor implication $C(z_t)$ for all thirteen rows and every $t$. It also proves that each parent is $17\bmod48$ and that the three-odd upper hit at $H_t$ is its first. [Kernel all-row closure and earliest upper hit](PhaseFamilies.lean) [Finite base parameters and actual upper/lower clocks](check.py) · [kernel all-parameter phase transfer](PhaseReturn.lean)

One can discover the table by starting the signed shortcut on the rational $-(15+2^{e+2})/81$ (an odd denominator permits both parity and halving) and checking its signed phase at the eligible upper clocks. The written proof and the replay above only use positive ordinary base computations and the integral $-17$ and $-5$ cycles.
