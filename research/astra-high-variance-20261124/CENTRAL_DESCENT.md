# What the ordinary minimum forces on every inverse word

Suppose the globally least positive odd nonconvergent source $m$ lies at a block boundary or an odd intermediate of an actual infinite L/P schedule. Here $U(x)$ is the next odd integer under Collatz, L has successive exponents $(2,1)$, and P has $(1,4)$. We impose no spacing or grouping on the letters. No result here puts every hypothetical least source on such a schedule.

Write $x_i=U^i(m)$, $Y=x_p$, and let $A$ be the sum of the first $p$ exponents. For every $p$ for which the states $x_0,\ldots ,x_{p-1}$ are distinct, every positive odd $b$ with $U^k(b)=Y$, and its total exponent $B$, we have
$$
 \frac{2^{B-A}}{3^{k-p}}>1-E_J,\qquad
 E_J=\frac13\left(\frac{8(1/8)^J}{1-1/8}
       +\frac{12(5/32)^J}{1-5/32}\right),\quad  J=\lfloor \log_{16}m\rfloor.
$$
In particular the actual path minimizes total binary clock among **all** inverse words at its own odd depth, at every endpoint of an injective orbit. For an orbit with a repetition the statement applies through the distinct prefix. More generally the ratio is at least one whenever $|k-p|\le  H$ and $2\cdot 3^HE_J<1$. Indeed a ratio below one has deficit at least $1/(2\cdot 3^H)$: when the ratio is greater than $1/2$, the reduced denominator is at most $2\cdot 3^H$ (separate the signs of (k-p) and (B-A)); smaller ratios satisfy the bound directly.

**Proof.** A legal odd-to-odd script of total clock $a$ determines one odd starting residue modulo $2^{a+1}$. This follows by solving the affine endpoint numerator modulo $2^{a+1}$ with odd endpoint, or successively lifting the unique residue for each exact exponent. For $k$ blocks the clock is $3k+2\#P$. The number of distinct boundary values at most $3X$ admitting an infinite schedule is at most $2^k+(3X/2)(5/32)^k$, by summing the $2^k$ separate residue bounds. Each intermediate in $X≤x<2X$ comes from a boundary at most $3X$ by the formulas $(3q+1)/4$ and $(3q+1)/2$. A fixed boundary has one actual first step and hence supplies at most two states counting itself. Thus the number of states in this band is at most $2^{k+1}+3X(5/32)^k$. With $X=2^d$, $k=\lfloor  d/4\rfloor$, sum the reciprocal bound over $d\ge 4J$, grouping four consecutive $d$'s and using $2^d\ge  16^k$. This gives $\sum _{i<p}1/(3x_i)\le  E_J$, because the states are distinct and $x_i\ge  m$. The finite control checks every positive odd below 256 reaches one, so $J\ge 2$, $E_J\le 247/1512<1/6$.

The actual multiplicative correction $\Pi =\prod _{i<p}(1+1/(3x_i))$ is strictly less than $1/(1-E_J)$, by $\prod (1-a_i)\ge 1-\sum  a_i$ and $1+a_i<1/(1-a_i)$ for positive $a_i<1$. The empty product satisfies the same strict bound. Now $2^AY=3^pm\Pi $ and $2^BY\ge 3^kb\ge 3^km$, as every ordinary ancestor of a nonconverging endpoint fails to converge. Division proves the inequality. At $k=p$ a strictly shorter clock would give ratio at most $1/2$.

## The complete inverse optimization at one endpoint

For $k\ge 1$, let $C_k(y)$ be the least total clock to reach the ordinary endpoint $y$ from any positive odd source at depth $k$, using infinity for the empty set. It depends only on $y\bmod  3^k$. With $C_0=0$, it is exactly the minimum over
$$
 1\le  a\le  2\cdot 3^{k-1},\quad  2^a y\equiv 1\bmod 3
$$
of $a+C_{k-1}((2^a y-1)/3)$. The inverse value is positive odd for every such exponent, and reducing the exponent modulo the displayed period leaves its result unchanged modulo $3^{k-1}$. Induction proves the claim. This handles every positive exponent and every intermediate ternary residue. For any unit $y$, $C_k(y)\le 4k$: either $a=1,3$ or $a=2,4$ is the allowed pair and at most one of the two makes the predecessor divisible by three.

The preceding theorem gives the exact condition $C_p(x_p)=A$ at each distinct horizon. A proof that the actual ordinary trajectory eventually violates it (or the nearby-depth condition) would contradict minimality. The recurrence alone supplies no uniform violating horizon.

## A complete test at the first exponent four

The first paid letter need not incur any inverse saving. For **every** $r\ge 1$, every actual positive odd source with prefix $(1)(2,1)^r(1,4)$ minimizes the total clock to its endpoint among all competitors of the same odd depth. This statement has no assumption of nonconvergence. The specified finite prefix is realized by a positive residue class by the same lifting argument.

Here $p=2r+3$, $A=3r+6$. Evaluate the prescribed affine forward word formally at $-5$. The first gap sends it to $-7$, which every L fixes; P sends it to $-29/16$. For a putative shorter same-depth word of $B<A$ binary shortcut steps to the true endpoint, run its binary inverse branches on this signed rational endpoint. At every intermediate step the result is dyadic: its difference from the corresponding real integer is the original difference $3^p(m+5)/2^A$ multiplied by a power of two and divided by at most $3^p$. Each backwards binary branch multiplies by two, then for an odd branch subtracts one and divides by three. Hence after four steps the denominator has cleared. As $r\ge 1$, $B\ge  p\ge 5$. All earlier steps form a genuine signed integer shortcut path: its backwards even branch gives an even predecessor, and its integral backwards odd branch an odd predecessor. Its endpoint is negative because the formal last four steps have nonnegative carry and image $-29/16$.

For a four-bit suffix with $v$ odd bits and carry $c=\sum _{i:b_i=1}2^i3^{\#\{j>i:b_j=1\}}$ (bits in forward order), the signed cut value is $-(29+c)/3^v$. The integral cases are exactly $(y,v)=(29,0),(11,1),(10,1),(4,2)$, where $y$ denotes its magnitude. Let $u=p-v$, $t=B-4$. The genuine signed part, started at magnitude $n$, has score $3u-2t\ge 7-3v\ge 1$. Its map on negative magnitudes is $a\mapsto  a/2$ for even $a$ and $a\mapsto (3a-1)/2$ for odd $a$.

Delete any complete $5,7,10$ cycles from the signed part. They leave endpoints and score unchanged. The remaining odd magnitudes are at least seven apart from at most one occurrence each of 3 and 5: one is fixed and cannot reach the displayed terminals, three reaches one via four and two, and five enters the deleted cycle. Write $u',t'$ for the shortened counts. Relative to the baseline odd factor $20/7$ before dividing by two, the exceptional factors cost at most the multiplicative corrections $8/9$ and $14/15$, respectively. Therefore
$$
 \frac{y}{n}\ge \frac89\frac{14}{15}
  2^{(3u'-2t')/2}\left(\frac{20/7}{\sqrt 8}\right)^{u'}.
$$
Since $20/7>\sqrt 8$, we have $n\le 29\cdot 135/112<35$. The accompanying 35-start deterministic enumeration records all visits to the four possible terminals up to repetition. A repeated terminal can only be ten on the cycle of three steps and two odd bits, which preserves the score and the parity of $u+v-3$. Thus it suffices to check the score and $u+v-3$ even at each first visit, also counting a negative implied $r$ if present. The sole hit starts at three and ends at four, with $r=0$, and four never repeats. This excludes **all** shorter competitors for $r\ge 1$. The finite part is exact Python enumeration, without a Lean verification.

## Where the unrestricted classification stops

The no-adjacent-twos geodesic theorem in *Inverse minima and escape to smaller Collatz sources*, Theorem 2, already treats the initial ramp before the exponent four. The signed argument above shows that the first paid letter also need not break same-depth optimality. It does not classify a second or an unbounded number of paid gaps. [Primary manuscript](https://rstation.ai/problems/collatz/papers/1). [PR193's related inverse optimality analysis](https://github.com/GettysburgResearch/collatz/blob/d35bdfd9d0c75effda50bbb8040c136482431e24/research/astra-global-synthesis-20261124/arithmetic/optimality.md).

For general words a backwards affine comparison $x'=(x+u)/2^d$ updates across original exponent $g$ and competing exponent $b\ge 1$ by $d'=d+g-b, u'=(2^gu+1-2^{d'})/3$. In the nonnegative integer credit states, the reverse paid pair $4,1$ can use $2,2$ and ends at $(d,u)=(1,-1)$. The next reverse L begins with $g=1$; its only positive-credit move stays at $(1,-1)$. Then $g=2$ makes $2^gu+1$ divisible by three, so no integral offset with nonnegative $d'$ exists. Other offsets, negative credit, and changes of odd depth remain possible. The full Bellman recurrence covers them at fixed finite depth, but we have no finite-state cover or proof of eventual saving on every infinite ordinary L/P path. The unrestricted ordinary descent problem remains open.
