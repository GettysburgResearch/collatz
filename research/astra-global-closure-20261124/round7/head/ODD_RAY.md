# Six physical prefixes retain each supplied odd pair

**PROPOSED, integer kernel checked.** Use the positive shortcut map and write $x\sim y$ when the forward orbits meet, with independent clocks. Suppose $v\equiv2\pmod9$ is odd and $3v+1=2^m a$, where $a$ is positive odd and $m\ge1$. There is a positive odd ternary unit $u$ such that
$$
                         u\sim v,\qquad 3u\sim9v+2.
$$
There are seven explicit positive-slope affine choices in $v$, and $u<24000v$. They are selected arithmetically, independently of eventual basin colors. In particular **every given failing odd pair** yields an actual forward unit failure in the same ordered two components. The number of such failing $v\le X$ is at most seven times the number of forward unit failures through $24000X$. The scheduled one-suffix construction in the [main note](README.md) then places these same particular colors. [Lean theorem orderedOddRay](OddUnitLift.lean)

Put $H_i=3^i a-1$. The first $m$ iterates of $v$ end at $a$, and the first $m$ iterates of $9v+2=3\cdot2^ma-1$ end at $H_{m+1}$. These are the two fixed ordinary arms, as in round six. If $y\equiv3\pmod4$, then $T^2(y-1)=T^2(3y-1)=(3y-1)/4$. Apply this at $y=3^{m+1}a$ if that integer is $3\bmod4$ and at $y=3^ma$ otherwise. Thus either $H_{m+1}\sim H_{m+2}$ (the first case) or $H_{m+1}\sim H_m$ (the second). In the second case choose $u=v$, since $3v=2^ma-1$ reaches $H_m$. [Round-six original endpoints](../../round6/head/README.md)

## The upward case

Here $Q=2^{m+2}a=4(3v+1)$ has $8\mid Q$ and $Q\equiv1\pmod{27}$. Use the following six initial odd words, specified by an ordinary starting value $b$ and a clock $h$. The pair starts at $b,3b$. Its two actual odd counts are $p,q$, where $g=1+q-p$. Its endpoints satisfy $T^hb=y$ and $T^h(3b)=3^g y-1$.

| $h$ | $b$ | $p$ | $q$ | $g$ | $y$ | Newly covered cells |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 261 | 3 | 4 | 2 | 7 | 162 |
| 16 | 35569 | 4 | 6 | 3 | 44 | 54 |
| 11 | 797 | 5 | 5 | 1 | 95 | 18 |
| 23 | 7962413 | 6 | 8 | 3 | 692 | 6 |
| 17 | 122181 | 7 | 7 | 1 | 2039 | 2 |
| 20 | 1013037 | 7 | 8 | 2 | 2113 | 1 |

To verify coverage, take $Q_i=136+216i$ for $0\le i<243$. These are exactly the least positive representatives with $8\mid Q_i$, $Q_i\equiv1\bmod27$ in their classes modulo $52488=8\cdot3^8$. A row accepts when
$$
 t=(Q_i/2^g-y)/3^p\ \text{is a nonnegative integer},\qquad
                 3\nmid b+2^h t.
$$
The new-cell counts in the table sum to 243. Since $2^g3^{p+1}$ divides 52488 at every row, the same row accepts every $Q=Q_i+52488j$, $j\ge0$. This checks positivity at the first member as well as compatibility of the higher ternary digits. The kernel verifies the six ordinary prefixes, all 243 base cells and the extrapolation to arbitrary $j$. [Finite and infinite lifts](OddUnitLift.lean)

Set $u=b+2^h t$ and $Y=Q/2^g$. High-bit lifting of the two fixed words gives
$$
                     T^h u=Y,\qquad T^h(3u)=3^gY-1.
$$
Indeed the two increments are $3^p t$ and $3^{q+1}t=3^g3^pt$. Here $1\le g\le3\le m+2$. Thus at the **same additional clock** $d=m+2-g$, the two arms land at $a,H_{m+2}$. The first arm has an explicit route to $a$ in at most $m+24$ clocks. The earlier ordinary merger $H_{m+1}\sim H_{m+2}$ proves the ordered comparison. All six formulas for $u$ are affine in $Q=12v+4$ on their integral domains. Their strict positivity comes from the cell test. Since the original odd step contributes a strictly positive affine intercept, $2^hy>3^pb$ and $u<(2^{h-g}/3^p)Q$. The maximum of these six coefficients is $2^{20}/729$, and $Q\le16v$, proving the size bound. Together with the identity in the other case there are at most seven antecedents of any $u$ in the indicated counting inequality.

## Following the terminating arm

On the unresolved $a=1$, $m=18j-2$ ray, write $M=m+2=18j$. The upward case applies. For every $j\ge1$ the table gives a specific odd unit $u$ whose first arrival at 1 is **exactly** $h+M-g$, while its triple has reached $3^M-1$ at that same clock. Before clock $h$ the first arm cannot have hit 1, since its clock-$h$ endpoint $2^{M-g}>2$ is outside the $1,2$ cycle. All subsequent steps to 1 are halvings. The exact form of the remaining question on that ray is consequently whether these selected triples ever reach 1. The finite prefix table gives no bound on that later clock.

A clock descent cannot be obtained by choosing a more favorable synchronized prefix with the same pure-power landing in this construction. For any odd lower prefix of length $h\ge1$, its count $p\ge1$ and the upper count $q\le h$ give $g=1+q-p\le h$. Hence $h+M-g\ge M>m$, even though the original $v$ reached 1 in exactly $m$ steps. This compares actual hitting times when the lower dyadic landing exceeds 2, as it does for the six prefixes on the indicated ray. Different kinds of adaptive transfer remain possible.

There is also an obstruction on the unrestricted unit input itself. For every even $k\ge4$ with $3\nmid k$, take $u=(2^k-1)/3$. Then $u$ is an odd ternary unit, $T(u)=2^{k-1}$, and its first hitting time of 1 is $k$. But $T^k(3u)=3^k-1$, and every upper iterate before that clock is at least $2^k-1$, strictly greater than the maximum $2^{k-1}$ of the entire lower orbit. At clock $k+j$ the upper value is at least $(3^k-1)/2^j$, because $T(z)\ge z/2$. No upper/lower meeting is possible before upper clock $k+\lceil\log_2((3^k-1)/2^{k-1})\rceil$. This is an unconditional lower bound on any meeting that occurs. It makes no eventual convergence assumption for $3u$. The ordinary all-odd formula used here is classical. [Lagarias, overview, §1](https://www.ams.org/bookstore/pspdf/mbk-78-prev.pdf)

Minimizing the first hitting time among putative forward unit failures gives extra antecedents. After the first odd step, every lower vertex is a ternary unit. Each proper preterminal lower suffix has smaller hitting time, and removing even factors preserves its component and can only shorten that time. Thus induction would certify the triples of all those suffix vertices. For $u=(2^k-1)/3$ they are exactly $3\cdot2^j$ with $0\le j\le k-1$ (including the terminal vertex). Their entire forward orbits have only $1,3,5$ as odd values and maximum $3\cdot2^{k-1}$. Through clock $k-1$ the upper orbit is odd and at least $2^k-1>5$. At clock $k+j$ it still exceeds the union's maximum whenever $2^j<(3^k-1)/(3\cdot2^{k-1})$. Thus even the full collection of those legitimate smaller-clock comparisons gives no merger on this initial interval. Proving an eventual merger or proving a transfer that uses information beyond these initial paths remains open.

For comparison, the 33-row substitution in the main note, applied directly to $n=(2^M-1)/3$ on the old $M=18j$ ray, would pass through the two unit parameters $(16\cdot2^M-7)/9$ and $(32\cdot2^M-23)/9$, with an intermediate component $2^{M+1}-1$. Its convergence is unknown at this point. The six-prefix lift removes that intervening assumption and produces a single unit with a certified terminating ordinary arm for *each* specified input. Actual convergence of its triple, or an independently well-founded implication proving it, remains the first unsupported step.
