# Full numerical denominator after complete top-factor cancellation

**Status. Proposed written corollary for the mixed-prime family of ABR5.** Fix distinct primes $r<s$ dividing $g$. In the primitive shortcut word of length $A=5g$ and odd count $p=3g$, mark three positions in each block $j\in\mathbb Z/g\mathbb Z$,

$$
5j+\mathbf1_{j\equiv1\pmod{g/r}},\qquad
5j+2+\mathbf1_{j\equiv1\pmod{g/s}},\qquad 5j+4 .
$$

ABR5 proves that the whole top cyclotomic polynomial divides the word's carry polynomial, so its complete numerical top factor divides the numerator at 3. Let $d$ be the reduced denominator of the positive rational cycle **after all integer cancellations**. Then

$$
\boxed{\quad 21d\ \ge\ 32^{\,g/s-1}.\quad}
$$

In particular $d>1$ for every word in the family since $g/s\ge r\ge2$. For fixed $r,s$, or bounded $s$, the full denominator grows exponentially in $g$. The estimate is stated in terms of $g/s$ when $s$ varies. [ABR5, PR194 at 764f3a9f539febf3d2661a9ca4acc1b10827878c](https://github.com/GettysburgResearch/collatz/blob/764f3a9f539febf3d2661a9ca4acc1b10827878c/research/astra-birth-rigidity-20261124/TOP_COMPONENT.md) · [PR193, C4–C5 at 52beff703fd3ce798c430e5af8199eb58d41bf93](https://github.com/GettysburgResearch/collatz/blob/52beff703fd3ce798c430e5af8199eb58d41bf93/research/astra-universal-descent-20261124/cycles.md)

**Proof.** The $s$ marked block indices $j\equiv1\bmod(g/s)$ cut the circle into $s$ gaps of exactly $g/s$ block steps. The $r$ indices marked by $j\equiv1\bmod(g/r)$ meet that set only at $j=1$, because $\operatorname{lcm}(g/r,g/s)=g$. Their remaining $r-1<s$ indices can occupy the interiors of at most $r-1$ gaps. One gap therefore has exactly $L=g/s-1$ consecutive unmarked interior blocks. At the ends of this interval the marked indices are excluded. The smallest permitted case has $L=1$.

At each block boundary the affine map on rational states is $x\mapsto(27x+C_j)/32$, with $C_j=37+9\mathbf1_r+12\mathbf1_s$. The baseline shortcut block $10101$ has fixed point $x_*=37/5$; its five actual states, starting at its boundary, are $37/5,58/5,29/5,46/5,23/5$ before returning. All boundaries of the selected cycle obey $37/5<x\le58/5$. The upper bound follows by applying the cyclic maximum inequality to $C_j\le58$. For strictness of the lower bound, write the recurrence for the difference from $x_*$ and unroll a full turn. Each increment $(C_j-37)/32$ is nonnegative, and at least one is positive in every turn. The cyclic equation for that difference divides a positive weighted sum by $1-(27/32)^g>0$.

Every cycle phase has the same reduced denominator $d$. Its denominator divides $2^{5g}-3^{3g}$ before reduction, hence is coprime to 6. The actual shortcut steps preserve the reduced odd denominator: their numerators modulo a prime divisor of $d$ are multiplied by a unit. Take $x$ at the start of the $L$ unmarked blocks and $x'$ at their end. Comparing their $5L$ actual shortcut steps with the repeated baseline word gives

$$
 2^{5L}\,[5d(x'-x_*)]=3^{3L}\,[5d(x-x_*)].
$$

Both bracketed quantities are integers. Coprimality forces $2^{5L}\mid 5d(x-x_*)$. The latter lies in $(0,21d]$ by the boundary bounds. This proves the displayed inequality.

An independent exact rational calculation tested all 176 choices of $2\le g\le180$ and pairs of distinct prime divisors $r<s$. For each, it recovered an unmarked stretch of the specified length, evaluated the rational cycle at its start, and checked $0<5d(x-37/5)\le21d$ and divisibility by $32^L$. Lengths ranged from 1 to 59. The proof applies at all lengths and uses no estimate for a linear form in logarithms. It controls this explicit family only.
