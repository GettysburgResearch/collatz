# Smaller adjacent comparisons require unbounded clocks

Write $T$ for the positive shortcut map and $Q(k)$ for eventual meeting of $X=54k+1$ and $X+1$. Fix $k$ and augment the undirected ordinary graph $x\leftrightarrow T(x)$ by the comparisons $54j+1\leftrightarrow54j+2$ for $0\le j<k$.

Two strict recurrences on the parameter are
$$
 Q(4s)\Longleftrightarrow Q(3s)\quad(s>0),\qquad
 Q(128s+19)\Longleftrightarrow Q(27s+4)\quad(s\ge0).
$$
To see them, let $J(t)$ be the ordinary component of $t+1$ and write $R(t)$ for $J(t)=J(2t)$. Halving $54k+2$ shows $Q(k)\Longleftrightarrow R(27k)$. Since $T^2(4t+1)=3t+1$, we have $J(4t)=J(3t)$ and $R(4t)\Longleftrightarrow R(3t)$, which gives the first recurrence. For the second, the starts $16u+2$ and $32u+3$ reach $8u+1$ and $9u+1$ in one and five steps respectively. Two exchanges give $J(9u)=J(12u)=J(16u)$, so $R(16u+1)\Longleftrightarrow R(8u)$. At $k=128s+19$ we have $27k=16u+1$ with $u=8(27s+4)$. Three exchanges identify $R(8u)=R(64(27s+4))$ with $R(27(27s+4))$, as required.

## A lower bound for smaller-comparison arguments

For every $H\ge1$ there is a $k\le 6^H/2$ such that any path from $X$ to $X+1$ in this graph must take **more than $H$ ordinary edges** before its first smaller comparison or before arrival. In fact, for every $0<z<X$, there is no meeting $T^i(X)=T^L(z)$ with both clocks $i,L\le H$. Thus a proof by smaller adjacent comparisons, if it works for all $k$, needs parameter-dependent clocks.

Both arms of the odd-class recurrence in fact **land directly** on the two smaller starts at clock seven. At the base parameter, $T^7(1027)=217$ and $T^7(1028)=218$, with three odd inputs on each arm. Shifting by $6912s=2^7(54s)$ adds $1458s=3^3(54s)$ at clock seven. Thus the two endpoints are exactly $54(27s+4)+1$ and $54(27s+4)+2$. [Lean proof of the two exact clock identities](HighBit.lean)

## A congruence that prevents descent

Choose $k$ by the Chinese remainder theorem so that
$$
 k\equiv0\pmod{3^H},\qquad 27k\equiv-1\pmod{2^{H-1}}.
$$
The least positive choice satisfies the asserted bound and these choices are unbounded as $H$ grows. They ensure $X\equiv1\pmod{3^H}$ and $2^H\mid X+1$.

Fix $0\le i\le H$, put $X=2^i t-1$, and suppose $T^L(z)=T^i(X)=3^it-1$. We show that $z\ge X$ whenever the $L$ steps from $z$ contain at most $i+H$ odd inputs. The [signed fixed-point argument](THREE_RAY_SMALLER.md#a-universal-bound-on-the-number-of-ordinary-steps-is-impossible) already gives $z\ge X$ whenever there are at most $i$ odd inputs. Its equal-count case gives the following more precise statement. A suffix with exactly $i$ odd inputs and length $i+b$ starts at $w=2^bX+c$, where $0\le c\le2^b-1$. Indeed reversing its parity word also from $-1$ gives an integral start $-M\le-1$, with $M\le2^b$ and $c=2^b-M$.

For an excess of $1\le d\le H$ odd inputs, split the word immediately after its first $d$ odd inputs, at clock $J$. Apply the equal-count formula to the suffix. The reverse of the first $J$ steps from $w=2^bX+c$ is rational affine in $X$ with slope $\alpha=2^{J+b}/3^d$. Starting this reversal instead from $2^b+c$ gives a **positive integer** $\beta$. In fact the difference of its endpoint from $w$ is $2^b(X-1)$, divisible by $3^d$. Before each odd inverse the transported difference still contains a factor of three, so every division is integral. The even inverse doubles and any integral odd inverse $(2y-1)/3$ of a positive $y$ stays positive.

Starting the same rational reversal from $c-2^b\le-1$ gives $\beta-2\alpha$. Both inverse branches preserve the real interval $(-\infty,-1]$, so $\beta-2\alpha\le-1$. In particular $\alpha\ge(\beta+1)/2\ge1$. The actual start satisfies $z=\alpha(X-1)+\beta\ge X$. This proves the stronger odd-count assertion, and $L\le H$ implies the stated clock bound.

## From clocks to undirected paths

Any ordinary walk of length at most $H$ gives a meeting with both clocks at most $H$. Cancel a backward step immediately followed by a forward step until the walk consists of forward steps followed by backward steps. Every endpoint of a smaller comparison is strictly below $X$, so the clock bound excludes reaching any such edge in at most $H$ ordinary steps.

A direct walk of this length to $X+1$ is also impossible. For $0\le i\le H$ the forward side is $T^i(X)=(3/2)^i(X+1)-1$, equal to $X$ at zero and strictly greater than $X+1$ for positive $i$, since $X>1$. On the other side $T^L(X+1)=(X+1)/2^L$ for $0\le L\le H$. At positive clocks this is less than $X$. Thus the two finite orbit segments are disjoint. This establishes the graph claim, including the case of a path using no smaller comparison.

Each fixed obstructing class nevertheless contains infinitely many $k$ for which **both arms reach any prescribed positive odd $u$ prime to three**. In this class write $k=k_0+2^{H-1}3^H v$. The affine starts have the same slope $2^H3^{H+3}$ in $v$. The [affine word construction](AFFINE_RAYS.md#classification-and-a-constructive-bound) gives a binary subclass with a common endpoint $3^e w+B$ in its remaining free parameter $w$. The power-of-three slope follows from the construction's normalization, which consumes all the fixed binary digits. At least one odd step occurred because the first arm starts odd and the distinct starts cannot meet at clock zero. Thus $3\nmid B$, since the output of an odd step is prime to three and subsequent halvings preserve that property. The powers of two run through the units modulo $3^e$. Infinitely many $m$ therefore make $2^m u=3^e w+B$ with $w\ge0$, and $m$ more halvings reach $u$. In particular the graph lower bound applies even to pairs known to reach one.
