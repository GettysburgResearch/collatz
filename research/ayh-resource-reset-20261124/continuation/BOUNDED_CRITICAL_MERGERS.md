# A lower bound of one quarter of the input bit length for critical mergers

**Written theorem.** There are arbitrarily large $n$ in the exact critical section $B$ such that, with $d=\lfloor\log_2 n\rfloor$ and $K=\lfloor d/4\rfloor$, no $m<n$ in $B\cup\{1\}$ satisfies
$$
 U^i(U(m))=U^j(U(n)),\qquad 0\le j\le K,\qquad 0\le i\le j+K .
$$
Here $U$ denotes the next odd Collatz value. The two clocks may differ and there is no restriction on their numbers of individual halvings. In particular at least one arm needs more than $K$ further odd transitions in any post-prefix merger with any smaller critical partner or the base. This is compatible with later coalescence and with the actual smaller partners on typical sources in [CRITICAL_COMPRESSION.md](CRITICAL_COMPRESSION.md).

### The size constraint

If $m<n$ are critical, then $U(m)<2U(n)$. Write $D=d(m)$, $d=d(n)$, $f=e(m)$, $e=e(n)$. If $e\le f+1$ the assertion follows from $3m+1<3n+1$. Otherwise put $a=e-f\ge2$. The critical inequalities give $d-D\ge5a-7\ge a+1$. Hence $2^a(3m+1)<3\cdot2^{D+a+1}\le3\cdot2^d<3n+1$.

### Ordinary inputs with both controls at once

Let $e$ range over the large even integers and put $d=5e-1$, $K=\lfloor d/4\rfloor$. By the Chinese remainder theorem choose $1\le R\le 2^{K+1}3^K$ so that
$$
 u=3\cdot2^{d-e}+R\equiv-1\pmod{2^{K+1}},\qquad u\equiv1\pmod{3^K}.
$$
Then $n=(2^e u-1)/3=2^d+(2^eR-1)/3$ is a positive odd ordinary integer. Since $R\le2^{3K+1}$ and $e=d/5+O(1)$, the relative excess $(n-2^d)/2^d=O(2^{-d/20})$ is eventually less than $70/(d+1)$. Thus $n$ lies in $B$ with binary exponent $d$, exact valuation $e$, and surplus zero. The first $K$ accelerated transitions of $u$ each have exponent one. Their values are $x_j=(3/2)^j(u+1)-1$ for $0\le j\le K$.

### The last reverse steps and the signed reference

Write each accelerated inverse as $L_a(y)=(2^a y-1)/3$, where $a\ge1$. For any $l\le j$, reverse an actual $l$-step word from $x_j$. The same reverse word starting at $-1$ has integral values at each intermediate step: $x_j+1$ is divisible by $3^j$ and each inverse step divides the difference by three and multiplies it by a power of two. Write its ending value as $-M$. If $b$ is the sum of the $l$ exponents minus $l$, then $1\le M\le2^b$. Indeed initially $M=1$, $b=0$, and one inverse sends $M$ to $(2^a M+1)/3\le2^{b+a-1}$. Consequently the actual preimage is
$$
 2^b x_{j-l}+c,\qquad c=2^b-M,\qquad 0\le c<2^b .
$$
This follows by transporting the original difference $x_j+1=(3/2)^l(x_{j-l}+1)$ through the word.

Suppose for infinitely many constructed sources a smaller critical $m$ meets $x_j$ as in the theorem, and put $v=U(m)<2u$. The base cannot meet since $U(1)=1$ and $x_j\ge u>1$. If $i<j$, set $l=i$ in the signed comparison. The inequality $v<2u$ forces $j-i=1$, since $x_2>2u$, and then $b=0$. Thus $v=x_1$ and $v/u\to3/2$ along such cases.

If $i\ge j$, set $l=j$. The last $j$ reverse steps now produce $z=2^bu+c$. There are $t=i-j\le K$ further inverse steps. Apply the same word in parallel from $z_0=2^b+c$. The initial difference $2^b(u-1)$ is divisible by $3^t$, so all the parallel values are integers. Each integral inverse of a positive integer is again positive. Let $v_0$ be the endpoint of the reference word, and let $E$ be the sum of its $t$ exponents. Then
$$
 v=\alpha(u-1)+v_0,\qquad \alpha=2^{E+b}/3^t,\qquad 1\le v_0<2\alpha .
$$
The last strict upper bound follows from $z_0<2^{b+1}$, since an inverse word on a positive value is at most its linear slope times that value. Since $v<2u$ and $v_0\ge1$, we have $\alpha<2+1/(u-1)\le5/2$ for $u\ge3$. Hence $1\le v_0\le4$. The corresponding positive path from $v_0$ to $z_0$ consists of $E$ shortcut steps with $t$ odd inputs, and $3^t/2^E=2^b/\alpha>2/5$. It is a physical word: each integral $L_a(y)$ is odd and reaches $y$ after one odd shortcut and $a-1$ halvings.

The four fixed starts $1,2,3,4$ reach the $1,2$ cycle. Each full period multiplies the prefix multiplier by $3/4$. Thus the displayed lower bound on $3^t/2^E$ bounds $t$ by an absolute constant, uniformly in $j$, $K$, and $b$. It follows from $1/3^t\le\alpha<5/2$ that the rational numbers $\alpha=2^{E+b}/3^t$ occurring here range over a finite set.

### Why the only surviving slope returns the original source

In either case $v/u$ is bounded above and bounded away from zero. Both $m,n$ tend to infinity, so their marks imply
$$
 \frac{u}{3\cdot2^{d-e}}\longrightarrow1,\qquad
 \frac{v}{3\cdot2^{D-f}}\longrightarrow1 .
$$
Therefore on a subsequence $v/u$ tends to an integral power of two: the comparability bounds the integer $(D-f)-(d-e)$, which can then be fixed. This rules out the ratio $3/2$ in the $i<j$ case. In the $i\ge j$ case pass to a subsequence with constant $\alpha,t$. Since $v_0\le4$, the limiting ratio is $\alpha$. Unique factorization forces $t=0$. The signed comparison then gives $v=2^b u+c$, and $v<2u$ forces $b=c=0$.

Finally $v=u$ forces $m=n$. Indeed consecutive odd predecessors of the same odd endpoint satisfy $x'=4x+1$, increasing $d,e$ by two and the surplus by eight. At most one can lie in the critical strip. This contradiction proves the theorem for all sufficiently large even $e$ in the construction.

The two-reference reverse-word proof builds on the method of [PR 146, NEGATIVE_FIVE_CHECKPOINT.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/NEGATIVE_FIVE_CHECKPOINT.md), with references $-1$ and $2^b+c$ and a separately imposed positive ternary congruence. The exact critical set and same-fiber uniqueness are in [PR 197](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/positive-section/CRITICAL_SECTION.md). This is an obstruction to short physical mergers and makes no claim about the eventual basin of a constructed input.
