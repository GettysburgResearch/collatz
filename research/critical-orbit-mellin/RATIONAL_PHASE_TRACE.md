# Coupled harmonic transfer at fixed rational phases

**PROPOSED.** Let $g_0=1$ and $g_q=L^q1$ on $\mathbb Z_3$, where
$$
 (Lf)(t)=\sum_{a\ge1:\ 2^at\equiv1\ (3)}3\,2^{-a}f((2^at-1)/3).
$$
This is the mean-one finite Syracuse inverse density in the [signed harmonic criterion](../unsafe-return-weights/SIGNED_MASS.md). Each $g_q$ depends only on the first $q$ ternary digits. Let $r=c/D$ be fixed with $c,D$ odd integers, $D>0$ coprime to three. On odd numerators define $U_D(b)=(3b+D)/2^{v_2(3b+D)}$. Its numerator never vanishes since $3\nmid D$. Then:

* If $c$ is off the cycles of $U_D$, $g_q(r)=O_{c,D}(q+1)$ and $\sum_{k\le q}g_k(r)=O_{c,D}(q+1)$.
* If $c$ is on a positive cycle, the same two bounds hold.
* On a negative cycle of minimal odd period $d$, let $J=3^d2^{-A}$ for total cycle valuation $A$. Then $J>1$, and for every $0\le l<d$ there is $C_l>0$ with
$$
 g_{md+l}(r)=C_l J^m+O_{c,D}(m+1).
$$

In particular exponential growth is equivalent to a negative cyclic rational phase. The statements transfer unchanged to positive ordinary representatives $t\equiv r\pmod{3^q}$ at the indicated depth. The estimate does not cover arbitrary increasing-depth approximations at mismatched moduli.

## Simple-path distortion on the numerator lattice

For any fixed odd $D$ as above, the number of distinct integers in $[-2X,-X]\cup[X,2X]$ visited by any orbit of the shortcut map with odd branch $(3b+D)/2$ is $O_D(X^\beta)$ for some absolute $\beta<1$. Here is an elementary bound sufficient for both signs. Use $k=\lceil\log_2 X\rceil$ steps. Parity words biject residues modulo $2^k$ by induction, since $D$ is odd and the two branches each discard one binary digit with odd affine numerator slope. At most $O(2^{k H_2(3/5)})$ source words have more than $3k/5$ odd letters. Each remaining image has magnitude at most
$$
 2X3^{3k/5}2^{-k}+D((3/2)^k-1)\ll_D X^{\beta'}
$$
for a $\beta'<1$, by composing the affine branches. Two translated intervals of length $O(2^k)$ contain only boundedly many representatives of each word. On a forward orbit the number of distinct selected points exceeds its $k$-step image cardinality by at most $k$: an injective forward orbit has no collisions, and on an eventually periodic full orbit only the first at most $k$ transient states are lost from the image. This proves the bound. It is just the elementary single-window packing argument; [stronger translated bounds for the ordinary map](PRIOR_WORK.md) have been proved previously.

On a pairwise distinct numerator path, the product of $|3b/(3b+D)|$ over its inputs is uniformly bounded by a constant depending on $D$. There are finitely many low nonzero numerators, with no zero denominator. In larger dyadic shells the positive logarithm costs $O(D/|b|)$ per point, hence has summable shell suprema by the preceding estimate. Consequently a simple inverse word from $b$ to $c$ satisfies $J_w\le C_D|c/b|$ by telescoping.

## Weighted first-hit levels

At fixed rational root, every inverse word has an integer starting numerator $b$ and corresponds exactly to its deterministic $U_D$ path. Indeed the retained odd numerator at each successor forces the indicated exponent to be the exact dyadic valuation. Let $h_q$ sum $J_w$ over words reaching $c$ for the first time at step $q$, with $h_0=1$. All such paths are simple, apart from the harmless length-zero path. No starting numerator occurs twice among first-hit levels.

For a large fixed integer $K$ the total weight of all length-$k$ words with total valuation exceeding $Kq$, for $k\le q$, is $O(e^{-2q})$ even before the ternary test. Indeed for any fixed $0<s<\log 2$ their weight is at most
$$
 e^{-sKq}\left(\sum_{a\ge1}3(e^s/2)^a\right)^k .
$$
For the remaining words, inverse iteration gives $|b|\le 2^{Kq}(|c|+qD)$ by the triangle inequality. Distinctness across first-hit levels and the distortion bound now give
$$
 \sum_{k=0}^q h_k\ll_{c,D} 1+\sum_{1\le m\le2^{Kq}(|c|+qD)}1/m\ll_{c,D}q+1 .
$$
Off cycles this is the claimed full sum. On a cycle $g_q(r)=\sum_{i=0}^{\lfloor q/d\rfloor}J^i h_{q-id}$. Every positive cycle has $J<1$ and every negative cycle $J>1$, by telescoping on the lap; an orbit with a positive state stays positive so cycles cannot change sign. Summing the geometric convolution gives the positive-cycle bounds. In the negative case,
$$
 C_l=\sum_{u\ge0}J^{-u}h_{ud+l}.
$$
The tail after $u=m$, multiplied by $J^m$, is $O_{c,D}(m+1)$ since $h_k=O_{c,D}(k+1)$. Positivity follows from the first-hit cycle prefix of length $l<d$ ending at $c$. This establishes the rational classification. It does not bound the trace along a moving ordinary escaping spine.
