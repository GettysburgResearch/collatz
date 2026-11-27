# A smaller multiple after an arbitrarily long initial odd run

Let $T$ be the ordinary shortcut map. Every positive integer $x$ shares a future iterate with a positive multiple of three at most $6x+3$. When $x$ is even, pass to $x/2$. When $x=4k+1>1$, pass to $T^2(x)=3k+1<x$. These reductions end at one or an input $s=4k+3$. In the first case three reaches one. In the second,

\[
 T^2(s)=9k+8=T^3(6s+3).
\]

Consequently, if positive Collatz fails there is a least positive bad multiple of three $n$, and no forward iterate $x$ of $n$ can satisfy $6x+3<n$.

## An explicit smaller multiple

Write $n+1=2^{m+1}a$ with $a$ odd. Suppose there are $j,w$ with

\[
                 3^m a=4^{j+1}w+1,\qquad w>0.
\]

After $m+1$ odd inputs and one halving, the state is $6\cdot4^j w+1$. Each neutral pair satisfies $T^2(24v+1)=18v+1$, so the next $2j$ steps end at $X=6\cdot3^jw+1$. The complete descent test is $36\cdot3^jw+9<n$. Whenever it holds, the construction in the first paragraph gives a positive multiple strictly smaller than $n$ that shares an ordinary future with $n$.

The uniform condition $j\ge 2m+6$ suffices for that test. Indeed $3^m 3^{2m}=27^m\le32^m=2^m4^{2m}$ and $5\cdot3^6\le4^6$. Thus $5\cdot3^{m+j}\le2^m4^j$. Multiplying by $a$ and using the first-exit equation gives $20\cdot3^jw\le 2^ma$. As $j\ge6$, this implies the stated strict size test. Every subsequent run of $n$ is unrestricted.

A second test uses fewer neutral pairs when the next odd run has a specified exit. If $2^{e+1}b=X+1$ and $3^e b\equiv3\bmod4$, the two starting integers $X$ and $(X-1)/2=3^{j+1}w$ reach the same integer after $e+3$ and $e+2$ shortcut steps respectively. The latter multiple is already below $n$ for $j\ge2m$. This extends the second-run merger in [PR #192](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/second/README.md) by following every one of the intermediate neutral pairs.

For example, take $m=3,\ j=12,\ a=72079891,\ w=29$. The original multiple $1153278255$ takes 29 steps to $92470735$, which is $3\bmod4$. Thus the original multiple and $554824413$ merge after 31 and three steps respectively. Lean checks those two iterates directly.

## The size and scope of the family

For **every** $m,j$ and $B$, there are ordinary multiples $n>B$ with the prescribed first run and at least $j$ neutral pairs. To construct them, put $M=4^{j+1}=3t+1$. The identity $3(2t+1)=2M+1$ constructs an odd inverse of $3$ modulo $M$. Raising this inverse to the $m$-th power gives an odd $A$ with $3^m A\equiv1\bmod M$. Choose $a=A+Mv$ with $v$ sufficiently large that $a\equiv 2^{m+1}\bmod3$. Then $2^{m+1}a-1$ is divisible by three and strictly exceeds $B$. Lean constructs the parameters explicitly.

The argument excludes these sources as least bad multiples. The congruence on $3^ma$ is an actual restriction on an arbitrary starting integer. A global proof still requires descent or convergence on sources outside the proved tests. The extraction, mergers and infinite-family theorem are in [MinimumDescent.lean](MinimumDescent.lean).
