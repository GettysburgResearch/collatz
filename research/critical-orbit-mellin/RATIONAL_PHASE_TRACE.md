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

## Which point masses can the ordinary escaping orbit see?

Let $y_j$ be any fixed nonperiodic positive ordinary orbit, $a_j=v_2(3y_j+1)$. A subsequential empirical limit of $(y_j,a_j)$ on $\mathbb Z_3\times\mathbb N_{>0}$ has a phase marginal invariant under the induced random transition $t=(3y+1)/2^a$: the joint marginal at the output is the input marginal by telescoping and exponent tightness, as in the [ordinary distortion analysis](HARMONIC_OFFSET_CONE.md). Its entire atomic part is a mixture of uniform distributions on finite **signed odd-rational cycles**, with the deterministic cycle exponent at every atom. In particular no irrational atom and no noncyclic rational atom are possible.

Indeed disintegrate the joint law given $y$ and use the resulting stationary Markov chain on $\mathbb Z_3$. A positive-mass atom returns to itself almost surely under its conditional path law by Poincaré recurrence. Every finite return word of length $d$ and total exponent $A$ forces $(2^A-3^d)y=B$, where $B$ is positive odd by affine composition, and the denominator is odd and prime to three. Each cyclic rotation gives the same conclusion at each intermediate state. All states on a finite return word are consequently odd rational numbers with odd denominator, so $a=v_2(3y+1)$ uniquely at every step. Any returning path must therefore follow the unique ordinary-rational cycle, without any possibility of choosing a different first exponent. This proves the assertion by applying recurrence at each atom. In the simultaneous dyadic and ternary phase limit, the same atom forces the same dyadic phase conditionally: its successive valuations repeat their cycle forever, and the first $k$ accelerated valuations specify a single odd dyadic residue modulo $2^{1+a_1+\cdots+a_k}$. The only dyadic point realizing the whole infinite periodic word is the rational cycle phase itself.

The mean exponent over this limiting transition law is at most $\log_2 3$, by truncating the telescoping bound on the empirical exponent mean. The signed-rational atomic classification alone permits the atom at $-1$ with constant exponent one, just as the explicit arithmetic-progression countermodel does. It concerns a necessary condition on actual orbit limits; it supplies no integer starting value with such a limit.

## Obstruction to regular ordinary Lyapunov majorants

Suppose $w>0$ on ordinary odds and $w(t)\ge(Lw)(t)$ for all sufficiently large odd units. Then the path of $q$ consecutive valuation-one steps from $x_q=2^{q+1}-1$ to $t_q=2\cdot3^q-1$ gives
$$
 w(t_q)\ge(3/2)^q w(x_q).
$$
Indeed its successive states are $2^{q+1-i}3^i-1$, increasing, and every endpoint after the source is a ternary unit. If $\liminf_{x\to\infty}\log w(x)/\log x\ge\alpha$ on odds, it follows that
$$
 \limsup_{t\to\infty}\frac{\log w(t)}{\log t}
 \ \ge\ 1-(1-\alpha)\log_3 2 .
$$
The same result holds for a lower bound only on ternary units by retaining those $q$ with $x_q$ a unit. In particular an everywhere eventually superharmonic power envelope with a positive regularly varying scale of index $0\le\alpha<1$ and positive bounded distortion is impossible. This is an obstruction on actual positive integer branches, independent of the ternary Haar mean; it leaves open an irregular sublinear envelope or a genuinely different dual certificate.
