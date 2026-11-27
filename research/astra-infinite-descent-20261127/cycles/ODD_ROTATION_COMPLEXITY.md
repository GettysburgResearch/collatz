# Sparse rotations of the odd valuation word and a finite interval exchange

Let $e_i\ge1$ be the native odd division counts of a primitive positive cycle of odd period $p$ and shortcut period $h=\sum e_i$. For an arbitrary shift $0<\ell<p$, put
\[
       d=\gcd(\ell,p),\qquad s=\#\{i\bmod p:e_i\ne e_{i+\ell}\}.
\]
For every $n\ge1$ the number $P_w(n)$ of distinct cyclic length-$n$ factors in the *shortcut parity word* satisfies
\[
                           P_w(n)\le6(d+s)n+1.                         \tag{1}
\]
The valuations can be arbitrarily large. The bound has no factor involving their sizes, the number of complete consecutive even steps, the period or the position of the root.

Apply Weaver's stated finite descent theorem, Paper 173/v1, at the minimum of an ordinary integer cycle. It follows that along any sequence of such least cycles with increasing periods,
\[
                    \min_{0<\ell<p}\bigl[\gcd(\ell,p)+s(\ell)\bigr]
                                    \longrightarrow\infty.              \tag{2}
\]
In particular every rotation with bounded gcd has a diverging number of **unequal odd valuations**, including lags of order $p$. This is separate from counting unequal bits at a fixed shortcut displacement. The stronger additive count below excludes bounded $s$ for **every unbounded rotation order** $p/d$, including growing gcd. The constants in the external finite descent theorem are ineffective.

## Discrete tower with constant roof over each base interval

Set $M=p/d$. Write every odd index uniquely as $i=r+d j$, where $0\le r<d$ and $j\bmod M$. With $u=(\ell/d)^{-1}\bmod M$, set $k=uj\bmod M$. Increasing $i$ by $\ell$ adds one to $k$ within the same $r$-circle. Increasing $i$ by one instead takes $(r,k)$ to $(r+1,k)$ if $r<d-1$, and $(d-1,k)$ to $(0,k+u\bmod M)$. Linearly order the $d$ circles, each starting at $k=0$. This chronological base permutation $B$ is a translation on each circle except for at most one additional cut on the last circle at the wrap of $k+u$. It is a permutation of the $p$ base positions.

Cut each circle at its fixed linear seam and at every interior change in its roof $e$. This yields $R\le d+s$ positive consecutive intervals of constant height. Let their widths be $m_j$, heights $a_j$. For interval $j$, form a contiguous rectangle of $a_jm_j$ elementary positions. Order its $a_j$ levels consecutively, with the $m_j$ base coordinates increasing within each level. Concatenate the rectangles in the base order. A location represents an actual shortcut date: level zero departs from that odd state, and levels $1,\ldots,a_j-1$ depart from the following even states before the next odd arrival. There are exactly $h$ locations. The forward time permutation $T$ moves upwards within a rectangle until its top level; then it maps the base coordinate to $B$ of that coordinate, landing at level zero of the target rectangle. This is conjugate to one time step around the given shortcut word.

For each rectangle of height exceeding one all nontop levels together form one contiguous interval on which $T$ translates by $m_j$. On the union of the top levels start with the $R$ source intervals, cut them at the at-most-one extra wrap of $B$, and cut at preimages of starts of all $R$ target intervals. The latter points number at most $R$ because $B$ is a bijection. On each resulting subinterval the source coordinates, $B$, and the embedding of the single target base interval are translations. Hence $T$ has at most $R+(R+1+R)=3R+1$ domain translation pieces in the linear order, including the seams between separately embedded rectangles. The odd observable $w$ is the indicator of the union of $R$ base layers. Its values can change at at most $2R$ interior cuts.

For a permutation of a finite consecutive chain, write $D_n$ for the number of adjacent pairs with different length-$n$ forward words. A pair can differ in its next $(n+1)$-word only if its initial bits differ, it crosses a translation-piece boundary, or $T$ maps it to an adjacent pair already counted by $D_n$. The first two causes jointly cost at most $2R+3R$. The third costs at most $D_n$, by injectivity of $T$ on left endpoints. Thus $D_{n+1}\le D_n+5R$, with $D_1\le2R$, so the number of constant word runs, and hence of distinct observed words, is at most $1+5Rn$. The slightly looser (1) covers all degenerate zero-cut cases. A word may wrap around chronological time several times. The permutation is actual cyclic time, so this causes no exception in the recurrence.

## Source and use of finite descent

The only external dynamical implication used for (2) is the stated finite theorem of Weaver. With $b=0,\eta=1$ it gives, for each fixed $A>0$, constants $K,X_0$ depending only on $A$. At an integer $x\ge X_0$ such that all of its first $Kn+1$ shortcut states are at least $x$, for $n=\lfloor\log_2 x\rfloor$, that actual prefix contains more than $An$ distinct length-$n$ factors. Positive cycles of unbounded least period have minima tending to infinity, since a fixed finite set of starting integers specifies only finitely many orbits. Start at that minimum and extend around the actual cycle as often as necessary. Every factor of the required chronological prefix is counted in $P_w(n)$. If $d+s$ were bounded, (1) would contradict the theorem for any fixed $A$ larger than $6(d+s)+1$. The result uses the manuscript as an external theorem; its Subspace Theorem proof is outside this packet's Lean build. [Weaver, Paper 173/v1, §1](https://rstation.ai/problems/collatz/papers/173/v1)

Armstrong's short-rotation result already gives effective mismatch growth when the smaller representative of $\ell$ is sublinear by a power of $p$, with no coprimality assumption. Wren's Paper 218 gives different estimates on the binary shortcut clock, and explicitly describes the unresolved all-rotation question for the odd valuation word. Here $d$ measures the number of components of a *discrete suspension* and can stay one at arbitrarily long odd lags. A large number of constant but unrelated base components is an obstruction to deducing unrestricted odd-rotation growth from this factor count. [Armstrong, short rotations and low mismatch spectrum](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/short-rotation-mismatch-growth/README.md) · [Wren, Paper 218/v3, §7](https://rstation.ai/problems/collatz/papers/218/v3)

## An additive bound and all rotations of unbounded order

The following stronger factor count has an additive cost for the regular part of the circle. Write $M=p/d$ for the order of the odd rotation. At every length $n\ge1$,
\[
                       P_w(n)\le h/M+3s(n+1).                          \tag{3}
\]
The integer part of $h/M$ may be used. In consequence **for each fixed $s_0$ there is a finite constant $M_{s_0}$ such that every primitive ordinary cycle with some odd rotation of Hamming distance at most $s_0$ has $M\le M_{s_0}$.** The constant is ineffective through Paper 173. In particular the mismatch count diverges along every sequence of unbounded rotation order. This includes sequences on which both the rotation gcd and its order grow, as well as the long unit rotations considered above.

To prove (3), cap each gap at $b_i=\min(e_i,n+1)$. This retains exactly the length-$n$ cyclic shortcut factors: a capped gap still has at least $n$ zeros whenever any zeros were deleted. A word containing a one cannot see both ends of such a run and any $n$-zero word remains available; conversely each word in the capped circle can be lifted across each long gap it meets, preserving whichever end it sees. Even if the capped cycle has length less than $n$, no gap could have been capped and the claim is unchanged. Regard its positions as $(i,u)$ with $0\le u<b_i$, where $u=0$ marks the odd departure.

For each residue circle $i\equiv r\pmod d$ and level $u$, consider the track of existing vertices $(i,u)$ in the $i\mapsto i+\ell$ order. Keep each consecutive edge when both ends exist and carry the same length-$n$ forward shortcut factor. Every component bears a single word. Before testing equality, complete tracks (all vertices present) contribute at most $\sum_r\min_{i\equiv r} b_i\le h/M$ components. Each component of an incomplete track starts at a formerly absent vertex followed by a present one. Such events occur only at the at-most-$s$ changed roof pairs and at most $n+1$ levels of each, so incomplete components contribute at most $s(n+1)$.

Breaking further edges for unequal words increases the total component count by at most the number of such edges. If the roof at the starting odd slot differs from its translated roof, charge its at most $n+1$ physical starts to that changed slot. Otherwise the paired positions agree in position and roof. Trace forwards across equal roofs. If their $n$-words eventually differ, the start is among the $n$ chronological positions immediately preceding the **base** of the first subsequent changed roof encountered before the end of the window. Charge it to that base; for each of the at most $s$ bases there are at most $n$ such positions in the capped circle, regardless of wrapping or overlap. These charges cover every bad existing edge, at most $s(2n+1)$. The total number of components is at most $h/M+s(3n+2)$, which implies (3). No restriction on the order of the rotation or the largest valuation enters this finite counting proof.

For the dynamical consequence, suppose $s\le s_0$ and $M\to\infty$ in positive primitive ordinary cycles. Then $p\to\infty$, $d=o(p)$ and $h<2p$ for nontrivial cycles by the positive lap product. There is a cyclic run of at least $p/s_0-1$ matched odd valuations. Its two distinct integer sources follow identical affine maps. Their nonzero difference is divisible by $2^{\sum e}$, so the cycle's maximum $X$ has $\log_2X\ge p/s_0-1$. Its minimum $m$ has $\log_2(m+1)=O(\log p)$ by the classical logarithmic form bound.

Choose $a=\max(d,\lceil\sqrt p\rceil)$. Then $a\to\infty$, $a=o(p)$, and $m<2^a<X$ eventually. Follow the orbit from the actual minimum to a maximum. Take the state $z$ immediately after its last crossing from $<2^a$ to $\ge2^a$ on that path. Since every shortcut obeys $x'+1\le(3/2)(x+1)$ one has $2^a\le z<2^{a+1}$. All following states through that maximum are at least $2^a\ge z^{1/2}$. Reaching $X$ from $z$ requires $\Omega_{s_0}(p)$ shortcut steps by the same growth bound. Therefore, for any fixed finite $K$ and all sufficiently large candidates, the next $Ka$ steps all stay at least $z^{1/2}$. But (3) gives
\[
                     P_w(a)\le 2d+3s_0(a+1)\le (2+6s_0)a.
\]
Use Paper 173/v1's theorem at this **actual intermediate integer** $z$, with $n=\lfloor\log_2z\rfloor=a$, $b=0$, $\eta=1/2$, and fixed $A=3+6s_0$. This contradicts the necessary local factor count. The fixed $K$ supplied by that paper is independent of $d,p$ and $z$. The argument proves the stated unbounded-order exclusion. For bounded orders the [separate denominator theorem](ROTATION_DENOMINATORS.md) covers mismatch counts through six. Whether the count must grow for all bounded-order rotations remains open.


The finite replay checks the four track charges and exact factor preservation on 19,658 native cycle-and-length cases, plus eight tall-roof cases with an original valuation up to 1,501. [Control script](check_cycle_rotations.py) · [Archived counts](../../../reports/astra-infinite-descent-20261127/cycles/ROTATION_CONTROLS.json)
