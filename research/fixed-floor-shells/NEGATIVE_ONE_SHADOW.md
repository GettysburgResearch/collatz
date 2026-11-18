# A nonbranching tree of possible forward minima through logarithmic inverse depth

**Proposed, with an exact finite calculation.** Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers, and $m(x)$ the least integer on the whole forward orbit. Fix $K\ge1$ and an odd $t$ with $3^K\mid t+1$. Put
$$
 x_j=(2/3)^j(t+1)-1,\qquad 0\le j\le K.
$$
If $x_K\ge2\cdot3^{10}$, among *all* positive odd inverse paths of length at most $K$ from $t$, the only ones whose starting source is a minimum on its forward path through $t$ are the prefixes of the pure exponent-one path $x_j\to\cdots\to t$. At every other source a strictly smaller ordinary state occurs before or at arrival. In particular, if $m(t)=t$, exactly $K+1$ sources in the full depth-$K$ tree are their own global minima. The size condition holds for all such $t$ when $K\ge16$, since $t+1\ge2\cdot3^K$.

This gives actual finite counterinstances to a uniform claim that an increasing limb must generate branching among its possible minimum sources within that horizon. Taking $t=2^L3^K-1$, $L\ge2$, also forces $L-1$ actual rising forward odd steps beyond $t$, independently of the prescribed inverse depth. The finite path property uses no assumption on the eventual behavior of this family. In particular it supplies no family of genuine positive divergent orbits. The use of a negative shadow and finite inverse comparison has predecessors in the studies of prescribed valuation words; the statement here bounds every side branch of this particular integer shadow. [rStation paper 65](https://rstation.ai/problems/collatz/papers/65/v1) · [rStation paper 148](https://rstation.ai/problems/collatz/papers/148/v1)

## A sharp off-cycle multiplier on the negative fixed-point shadow

Use the positive mirror $V(u)=(3u-1)/2^{v_2(3u-1)}$. Suppose an odd $y>1$ first reaches $1$ after $q$ odd steps with total valuation $S$. Write $D=2^S/3^q$. Then
$$
 D=y\prod_{v\text{ before the first }1}(1-1/(3v))\ > y/3^{10},
 \qquad D\ge8/3.
$$
Equality in the second inequality occurs only at $y=3$. The identity follows by multiplying the odd-step formulas.

To bound the product, include all ordinary shortcuts of the path up to its first visit to 1. The terms before that visit are distinct. In the block $[2^k,2^{k+1})$, $k\ge1$, the number of odd terms is at most $2^{k-1}$. For any integer $0\le a\le k$ it is also at most
$$
 k+2\cdot3^a+\sum_{j>a}\binom{k}{j}.
$$
Remove the last $k$ shortcuts of the path, or the whole path if shorter. Among the remaining sources with at most $a$ odd inputs over their next $k$ shortcuts, the common-clock image is below $2\cdot3^a$, since each odd branch subtracts its affine intercept. Those images are distinct on this simple segment. The other sources have one of the indicated high parity words, which biject with residue classes modulo $2^k$; the usual induction works with odd branch $(3u-1)/2$, whose linear part is invertible after fixing parity. The block is one full period. Write $N_k$ for the minimum of these count bounds. Then the negative log of the product is bounded by $\sum_{k\ge1}N_k/(3\cdot2^k-1)$ using $-\log(1-1/(3v))\le1/(3v-1)$.

For $k\ge256$ choose $a=\lfloor3k/5\rfloor$. The fair-binomial upper tail is at most $\exp(-k/50)\le(50/51)^k$ by Hoeffding. The low-image ratio $3^{3/5}/2$ is at most $31/32$ by integer powers. Thus the remaining sum is bounded by one half the sum of $k2^{-k}+2(31/32)^k+(50/51)^k$ over this range. Exact rational summation through $255$ and these three geometric tails gives an upper bound below $9.204<10$. Hence the product exceeds $e^{-10}>3^{-10}$. For $y>(8/3)3^{10}=157464$ the asserted lower bound on $D$ follows. For smaller odd $y$, the accompanying checker follows $V$ until it recognizes a previous state or classified path, records the exact pair $(q,S)$ for first arrivals at 1, and compares integer powers. The least multiplier among the qualifying odd starts is $8/3$, unique at 3; the finite search classified 125333 states including intermediate values. [Exact checker](check_negative_one.py)

## Lifting the entire side branch

Read any non-pure inverse word backwards from $t$ until its first departure from the pure chain, say at $x_j$. There are at most $K-j$ additional exponents. The same departure word is legal in the signed inverse tree starting at $-1$, since $x_j\equiv-1\pmod{3^{K-j}}$ and legality of a word of length $h$ depends only on the target modulo $3^h$. Its endpoint is $-y$ for a positive odd $y>1$ in the first-arrival mirror tree of 1. Indeed the first exponent is different from the self-loop exponent 1, and no reverse continuation after leaving that loop can reenter it. Any cycle among intermediate states would be incompatible with their forward first arrival at 1.

At fixed word the source has affine dependence on its target with slope $D$. Comparing the two endpoints gives the positive source $s=D(x_j+1)-y$. The mirror bounds imply
$$
 s>D(x_j+1-3^{10})\ge(8/3)(x_j+1-3^{10})>x_j.
$$
Its actual forward path therefore passes through a smaller value $x_j$. The pure chain is positive and increases strictly in the forward direction. This proves the finite path assertion, and if $m(t)=t$ each pure source also remains its own minimum after arrival.
