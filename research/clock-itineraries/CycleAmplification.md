# A finite balanced-row test for nontrivial cycles

Fix $b\ge0$. A successful row consists of an ordinary path from a positive odd unit $x$ to $q>2$, with $b$ odd gaps, exact shortcut clock $2b$, and

\[
                (b+1)(3^b x)^6 < (4^b q)^6 .
\]

The power of six permits integer comparisons throughout. Write $D=4^bq/(3^b x)$ for the physical path dilation. The test asks for $D^6>b+1$.

## From one cycle to all sufficiently large rows

Suppose $q>2$ belongs to an ordinary odd cycle. Write $p>0$ for the odd-gap count in one lap and $A$ for its shortcut clock. Multiplying the physical gap equations yields $3^p<2^A<4^p$. For the upper bound, $3y+1\le4y$ at every positive odd input and the last edge into $q>2$ has $y>1$, making its inequality strict. Thus $A\le2p-1$.

Append $r$ laps at $q$ to an incoming prefix of $m$ gaps, with $b=rp+m$. The available prefix clock is $u=2b-rA\ge r+2m$. At $m\ge2$ and $u\ge6m+7$, the exact-clock theorem supplies the prefix. It satisfies $3^m x\le2^u q$. The complete physical path consequently satisfies

\[
                  D\ \ge\ \left(\frac{2^A}{3^p}\right)^r .
\]

To cover every large integer $b$, put $v=3^p$, $d=vp$, and write $b-2=dt+s$ with $0\le s<d$. Use $r=vt$ laps and $m=s+2$ prefix gaps. For $t\ge6d+20$ the prefix clock suffices. The integer Bernoulli inequality $(v+r)v^r\le v(v+1)^r$ implies $(t+1)v^r\le (2^A)^r$. Moreover $b+1\le t^2+t+1<(t+1)^2$. Thus the constructed path meets the test. The endpoint $q$ is the same on every such row.

This construction supplies an individual witness on each row. PR #207's normalized count of predecessors asks for a larger population and uses a separate analytic lower bound. [PR #207 at b56c4dc](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/README.md)

## A finite search over sources

An ordinary route from $x$ to $q$ with $p$ gaps of total clock $s$ satisfies, for each integer $d\ge1$,

\[
                   2^s(q+d)\le3^p(x+2^{s-p}d).
\]

For one gap of length $e\ge1$, the additive terms satisfy $1+2^e d\le3\cdot2^{e-1}d$. Apply the same estimate to the preceding route with the new positive shift $2^{e-1}d$. On a balanced row this gives $4^b(q+1)\le3^b(x+2^b)$, hence $D\le1+2^b/x$. No zero-length row passes. If $x\ge10\cdot2^b$, then $D\le11/10$ and $(11/10)^6<2\le b+1$. Every successful row therefore satisfies

\[
                   x<10\cdot2^b,\qquad 2^b(q+1)\le11\cdot3^b .
\]

The Boolean function `witnessTest` scans this finite source range, follows the deterministic odd iteration, and checks the endpoint, the elapsed clock, and the integer distortion inequality. Its equivalence with the existential row predicate and the cycle-to-witness construction are kernel-checked. [CycleAmplification.lean](CycleAmplification.lean)
