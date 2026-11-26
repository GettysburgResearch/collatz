# An aperiodic candidate survives every test with a fixed physical horizon

**Written theorem.** For every finite physical horizon $H\ge0$, choose $n_H=2^{5H+5}-1$. There is an explicit aperiodic binary address starting at this one positive ordinary source such that, simultaneously at **all** pairs of depths $i,j$ and all shortcut clocks $h,t\le H$,
$$
                 T^h(m_i)\ne T^t(m_j+1).
$$
Here $m_0=n_H$ and $m_{j+1}=2m_j+b_{j+1}$. Every fixed finite nonempty word has a finite cap on its consecutive powers in this address, valid from the first digit. In particular it contains no two consecutive copies of 1011. This qualitative power property does not establish compliance with the specific caps supplied by unrestricted physical merger theorems. The source and address depend on $H$. No invariant coloring of the natural numbers has been constructed.

## A single defect in a two-coordinate model

Use pairs $(a,b)$ with $a$ a strictly positive dyadic rational, $b$ an integer. Addition of one changes $b$ alone. Parity is the parity of $b$. The even shortcut halves both coordinates, and the odd shortcut sends $(a,b)$ to $(3a/2,(3b+1)/2)$. This is an auxiliary domain.

For every integer $k$ put $L_k=(2^k,-1)$ when $k\le0$ and $L_k=(2^k,-2^{k-1}-1)$ when $k\ge1$. Set $R_k=L_k+1$. These are the dyadic edges of the bi-infinite address with a single zero between levels zero and one, all remaining digits being ones. No forward iterate of any $L_k$ equals any forward iterate of any $R_j$.

Indeed, equality of first coordinates after respective clocks $h,t$ forces equality of odd counts and $h-k=t-j$, by unique factorization of powers of two and three. An old right edge endpoint ($j\le0$) has second coordinate zero forever, whereas every left second coordinate stays negative. For a new right endpoint set $\theta=t-j+1=h-k+1$. If $\theta<0$, both endpoints are new. The right second coordinate is $-2^{-\theta}$ during its initial even run. The left one is $-2^{-\theta}3^h-1$ during its initial odd run, so they differ. If $\theta\ge0$, the new right endpoint has second coordinate $-1$ and total grade $\theta$. An old left endpoint has total grade $h<\theta$. It remains to test a new left endpoint.

Write $r=k-1\ge0$. Its first $r$ steps are odd, taking its second coordinate to $-3^r-1$. Reflect its sign and track $w=3^r+1$ under the reflected shortcut (even $w/2$, odd $(3w-1)/2$) for the remaining $\theta$ steps. If $g$ is their odd count, equal grades require $r+g=\theta$. Put $y=w-1$. The odd step multiplies $y$ by $3/2$, while the even step sends it to $(y-1)/2$. Thus $2^\theta y_\theta=3^{g+r}-A$. If the even positions are $0\le i_0<\cdots<i_{e-1}<\theta$, their normalized carry satisfies
$$
 A/3^\theta=\sum_{u=0}^{e-1}3^{-e+u}(2/3)^{i_u}
 \le 3^{-e}(2^e-1)<1 .
$$
The empty sum is zero. Consequently $y_\theta>0$ whenever the grades agree. The left second coordinate is then below $-1$. This proves disjointness. The same carry estimate occurs in the first-attachment analysis, here applied to the reflected shortcut.

Color the auxiliary domain by membership in the union of the forward-meeting equivalence classes of all $L_k$. All the $L_k$ have one color and all the $R_j$ its opposite. Forward meeting is an equivalence relation for a deterministic map, so this is a globally shortcut-invariant coloring on the auxiliary domain. It proves that no identity between formal affine trajectories of opposite endpoints can be forced on a local binary window containing at most one zero, even allowing arbitrary clocks in this auxiliary test.

## Transfer to one ordinary source at arbitrarily many depths

Put $D=2H+2$, $\lambda=2H+4+\sqrt2$. Choose zero digits at positions $2\lfloor\lambda k\rfloor$ for integers $k\ge1$, and ones elsewhere. Extend the digit string backwards with ones. The zero positions have even parity and consecutive zeros are separated by at least $2\lfloor\lambda\rfloor>H+D$. Their count in any interval of length $N$ differs from $N/(2\lambda)$ by an absolute bounded quantity on the positive one-sided address: this follows directly by inverting the two endpoints of $2\lfloor\lambda k\rfloor$. The zero density is irrational. For a fixed word of length $s$ with $q$ zeros, a power with $B$ copies has discrepancy $B|q-s/(2\lambda)|$, so $B$ is bounded for each such word. Irrational density also gives aperiodicity.

At any starting depth $j$, write $m_j=2^H Q+r$ with $0\le r<2^H$. Its last $H$ binary digits are precisely the preceding $H$ digits of the backwards-extended address, because $n_H\equiv-1\pmod{2^H}$. Together with the next $D$ bits these form a window with at most one zero. For a prefix of length $k\le D$, value $w$, either endpoint equals $2^k(2^HQ+r)+w+\delta$, $\delta\in\{0,1\}$. At a clock $h\le H$ its value is an affine function of $Q$ with positive integral slope $2^{H+k-h}3^{g}$, where $g$ is the known odd count. The intercept is $T^h(2^kr+w+\delta)$.

No left and right affine functions on this window are identical. Embed the preceding and following digits into the auxiliary single-zero address (a window without a zero also embeds). At the matching starting level the second coordinate $b$ has $b\equiv r\pmod{2^H}$. Substituting the pair $(a/2^H,(b-r)/2^H)$ for $Q$ reconstructs that model edge and preserves all the prescribed parities through $h\le H$. Identical affine functions would make the two auxiliary trajectories intersect, contrary to the proof above.

Every intercept is nonnegative and bounded by $2^{2H+D+1}$. Indeed $2^k r+w+\delta\le2^{H+D}$ and $T^h(y)+1\le (3/2)^h(y+1)$. Two different integral slopes can only coincide at a nonnegative $Q$ at most this intercept bound. But $Q\ge\lfloor n_H/2^H\rfloor=2^{4H+5}-1>2^{2H+D+1}$. Equal slopes with different intercepts cannot meet either. This excludes every comparison across depth differences at most $D$ on this same natural-number path.

If $i>j+D$, then $m_i\ge2^{i-j}m_j$. All later endpoint iterates through clock $H$ are at least $2^{-H}m_i$, whereas all earlier endpoint iterates are at most $(3/2)^H(m_j+2)$. Since $m_j\ge1$ and $2^{D}>3^{H+1}$, the ranges are disjoint. The same estimate covers the reversed choice of left and right arms. This proves the claimed comparison over all depths.

An independent direct integer replay at depths zero through 1,200 found the two full horizon-bounded endpoint sets disjoint for $H=0,1,3,7,16,32$. For $H=32$ their distinct sizes were 37,369 and 1,489. The irrational positions can be evaluated exactly by $\lfloor\lambda k\rfloor=(2H+4)k+\operatorname{isqrt}(2k^2)$. The replay is a finite control; the proof covers infinitely many depths for each $H$.

This locates the compactness gap. The aperiodic path already has one ordinary root at each tested horizon and retains every tested left/right inequivalence along the entire path. A persistent actual wall requires the same root, digit sequence and component separation at every physical horizon. Passing from the former quantifier order to the latter requires an additional source-specific argument.

## A single ordinary source also defeats linearly growing clocks

**Stronger written control.** Take any integer $N\ge128$, the fixed positive source $m_0=2^N-1$, and zero positions $N,2N,4N,\ldots$, with all other digits one. For all $i,j\ge0$ and all
$$
             h\le\lfloor(N+i)/128\rfloor,\qquad
             t\le\lfloor(N+j)/128\rfloor,
$$
the two actual integers $T^h(m_i)$ and $T^t(m_j+1)$ differ. These physical clocks grow without bound on this one source. Every word containing a zero is cube-free on this address: three copies would give three equally spaced zero positions, whereas three distinct powers of two cannot be in arithmetic progression (divide the equality between the sum of the extremes and twice the middle by the smallest power). The address is aperiodic, with unbounded runs of pure ones. Accordingly this control gives a cap for every nonconstant word while allowing the constant period of ones.

To prove the clock assertion, let $j$ be the earlier depth, let $s$ be the depth difference, and put $U=N+j$. Either arm can be the later one. If $s\ge U/16$, the ratio of the smallest possible later value to the largest possible earlier value is at least
$$
                   2^{s-(2U+s)/128}/3>1.
$$
Here $m_{j+s}\ge2^s m_j$, the later shortcut can decrease by at most a factor two per step, and the earlier translated height grows by at most a factor $3/2<2$ per step. The last inequality follows already at $s=U/16$ and $U\ge128$.

Otherwise put $K=\lceil U/64\rceil$, $D=\lceil U/16\rceil$. Both clocks are at most $K$, and $s\le D$. The window of $K$ preceding and $D$ following digits contains at most one zero. Indeed, two successive zero positions $z,2z$ in that window would give $z\le K+D$, $j\le z+K$, and $N\le z$. Hence $U\le 2z+K\le 3K+2D<U$, where the strict inequality follows from $U\ge128$. Backwards digits at the initial source are ones for its first $N$ low positions and $K\le N+j$.

The preceding local affine argument applies with precision $K$ and length $D$. Its intercepts are at most $2^{2K+D+1}$. Since $m_j\ge2^{U-1}$, the ordinary high part is at least $2^{U-1-K}>2^{2K+D+1}$ by $3K+D+2<U$. This rules out accidental equality, and the auxiliary one-zero model ruled out identical affine forms. This proves the assertion at all depths on the same root. A direct replay through depth 3,000 at $N=128,256,1024$ gave disjoint sets in all three cases. At $N=128$ the two set sizes were 39,576 and 3,038.

The budgets are upper limits on each arm's physical clock. They leave longer physical trajectories unrestricted, including at the initial edge. Thus even this fixed-root construction supplies no ordinary invariant coloring or Collatz counterexample.
