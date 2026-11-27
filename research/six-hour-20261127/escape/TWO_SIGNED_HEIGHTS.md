# Two signed height tests recover the ordinary residue mass

Let \(Q=2^N\), \(N\ge1\). For odd \(0<r<Q\), define
\[
 H_c(r)=\min_{\substack{q,p\ge1\\p+rq\equiv0\bmod Q}}
            \max(q,p/c),\qquad h_c=H_c/Q,\qquad c=1,2.
\]
Allow even pairs. It suffices to try \(1\le q,p\le Q\): \(q=p=Q\) gives cost \(Q\), and the least positive \(p\) at fixed \(q\) is at most \(Q\). Put
\[
 F_Q(r)=h_1(r)^3\mathbf1_{\{|h_2(r)^{-1}-h_1(r)^{-1}-1|<1/3\}}.
 \tag{1}
\]

**Written theorem.** The total error on the entire odd residue row satisfies
\[
   \sum_{\substack{0<r<Q\\r\ {\rm odd}}}
       \big|F_Q(r)-(r+1)^{-3}\big|\ll Q^{-1/3}.                     \tag{2}
\]
This also bounds the error after restriction to any subset of the row. One signed height retains a positive signal at every positive odd-denominator rational. The second aspect ratio recovers its denominator and resolves agreement lost in the last few binary places.

## The positive rational responsible for a large height

The lattice \(L_r=\{(q,p)\in\mathbb Z^2:p+rq\equiv0\bmod Q\}\) has determinant \(Q\). Let \(\ell\) be the Euclidean length of a shortest nonzero vector \(u\). It is primitive **in the lattice** and extends to a lattice basis \(u,v\), since its two integer coordinates in any starting lattice basis are coprime. Shift \(v\) by an integer multiple of \(u\) to put its parallel projection in \([-\ell/2,\ell/2]\). Its perpendicular length is \(Q/\ell\). Minimality of \(u\) implies \(Q/\ell\ge\sqrt3\,\ell/2\). Every real point is within Euclidean distance \((\ell+|v|)/2\) of the lattice by rounding both basis coordinates. The open square \((0,H_1)^2\) misses the lattice. Its center is at distance at least \(H_1/2\), so
\[
       H_1\le \ell+|v|\le 3\ell/2+Q/\ell
                         \le(1+\sqrt3)Q/\ell<3Q/\ell.               \tag{3}
\]

Suppose \(h_1>1/K\), \(K\ge1\), and \(Q>3K^2\). Then \(\ell<3K\). No shortest vector lies on an axis: odd \(r\) is a unit and both axis intersections have spacing \(Q\). Its two coordinates have opposite signs, since a same-sign vector up to orientation would give \(H_1\le\ell<3K<Q/K\). Choose the sign and write
\[
                  u=d(b,-a),\quad a,b,d\ge1,\quad (a,b)=1.
\]
Both \(da,db<3K\). Lattice primitivity gives
\[
                   d=Q/\gcd(Q,br-a),                               \tag{4}
\]
the least positive multiple of \((b,-a)\) in the lattice. In particular \(d\) is a power of two and \(br\equiv a\bmod Q/d\). Here \(Q/d>1\), so \(a,b\) are odd. For \(d>1\) the cell agrees with \(a/b\) through fewer than all \(N\) binary places.

For every \(K\ge1\),
\[
           \#\{r: h_1(r)>1/K\}\le9K^2.                              \tag{5}
\]
For \(Q\le3K^2\) count all residues. Otherwise a counted \(r\) satisfies \(b'r\equiv a'\bmod Q\) for some positive \(a',b'<3K\). At fixed \(b'\), let \(g=(b',Q)\). Each allowed \(a'\) is a multiple of \(g\), with at most \(g\) solutions, so there are at most \(3K\) pairs \((a',r)\). Sum over \(b'\).

## What the two aspect ratios measure

For any primitive \(u=d(b,-a)\) as above, the determinant with a positive \((q,p)\in L_r\) is \(d(bp+aq)\), a positive multiple of \(Q\). Hence \(T_c:=Q/[d(a+cb)]\le H_c\). On the line of determinants exactly \(Q\), the point \((T_c,cT_c)\) has balanced coordinates for aspect ratio \(c\). Translate a complement of determinant \(Q\) by an integer multiple of \(u\). Rounding on this line gives a lattice point whose coordinate errors from \((T_c,cT_c)\) are at most \(db/2\) and \(da/2\), respectively. If \(T_c>(d/2)\max(b,a/c)\) this point is positive. Therefore
\[
 0\le H_c-T_c\le \tfrac d2\max(b,a/c),\qquad
 0\le d(a+cb)-h_c^{-1}
       \le \frac{[d(a+cb)]^2d\max(b,a/c)}{2Q}.                      \tag{6}
\]

For \(da,db\le3K\) and \(Q\ge1024K^3\), positivity holds and the two errors at \(c=1,2\) sum to at most \(176K^3/Q<1/3\). Thus
\[
    \left|h_2^{-1}-h_1^{-1}-db\right|<1/3.                         \tag{7}
\]
At a large cell covered by (3), the filter (1) succeeds exactly when \(d=b=1\). Then \(r\equiv a\bmod Q\) and \(a<3K<Q\), so \(r=a\). Conversely at every odd \(r\le3K\) the vector \((1,-r)\) is primitive in \(L_r\). Hence (6) and (7) hold there with \(b=d=1\), including cells with \(h_1\le1/K\).

For fixed reduced positive odd \(a/b\) and fixed \(d=2^k\), every cell with (4) satisfies \(h_c\to1/[d(a+cb)]\) and \(h_2^{-1}-h_1^{-1}\to db\). There is one such cell at \(d=1\), and \(\varphi(d)\) for \(d>1\) and all large \(N\). A positive rational with \(b>1\) eventually fails (1) in its main cell. Even for an integer \(a\), cells with fixed positive precision loss eventually fail.

At any fixed odd \(x\in\mathbb Z_2\), the limit of \(h_1(x\bmod Q)\) is \(1/(a+b)\) if \(x=a/b>0\) in lowest terms, and zero otherwise. Indeed, if \(h_1>1/K\) at arbitrarily large precisions, bounded \(da,db<3K\) give a single positive pair \(a',b'\) with \(b'x\equiv a'\bmod Q\) for unbounded \(Q\). This implies \(x=a'/b'>0\) in \(\mathbb Z_2\). At the actual rational use (6).

## Uniform cubic approximation and the finite Collatz criterion

Take \(Q\ge1024\), \(K=(Q/1024)^{1/3}\). On the row \(h_1\le1/K\), the layers \(1/(2^{j+1}K)<h_1\le1/(2^jK)\) and (5) give total cubic mass at most \(72/K\). Every odd \(r\) satisfies \(h_1\ge1/(r+1)\), since \(p+rq\) is a positive multiple of \(Q\). Both nonnegative weights in (2) are at most \(h_1^3\), so the absolute error on this row is also at most \(72/K\).

On the row \(h_1>1/K\), all selected residues lie in \(r\le3K\), and all residues in that range pass (7). Formula (6) with \(u=(1,-r)\) gives \(0\le h_1-1/(r+1)\le3K/(2Q)\). Both quantities are at most one, so the cube difference is at most \(9K/(2Q)\). Sum over at most \(3K\) residues. The unselected row has \(r>3K\) and its ordinary tail \(\sum_{r>3K}(r+1)^{-3}\ll K^{-2}\). These bounds prove (2); enlarge the constant for smaller \(Q\).

Let \(S_N\) be the positive source classes passing \(5j\le8\,{\rm grade}_j\) at every binary prefix \(j\le N\) in [the binary criterion](../BinaryPrefixCriterion.lean). Then
\[
    \lim_N\sum_{r\in S_N} F_{2^N}(r)
       =\sum_{\substack{m\ {\rm positive\ odd}\\
                     {\rm actual\ gate\ at\ all\ }j}}(m+1)^{-3}.    \tag{8}
\]
At fixed positive \(m\) the finite indicators eventually stabilize to its permanent-gate indicator. The comparison weights \((m+1)^{-3}\) are summable, so (2) gives (8). Good inputs eventually follow the shortcut cycle \(1,2\), with odd density \(1/2\). Every hypothetical globally least bad integer passes the gate by the linked Lean theorem. Thus vanishing in (8) is equivalent to positive Collatz. For \(B\ge1,\ Q=2^N\ge1024(B+1)^3\), the strict inequality \(\sum_{r\in S_N}F_Q(r)<(B+1)^{-3}\) certifies that every integer in \([1,B]\) reaches one: a globally least bad \(m\le B\) would pass (7) with \(K=B+1\) and contribute at least \((m+1)^{-3}\).

The rational obstruction persists above the floor \(33\) in the binary criterion. For \(s=29,L=46\), the rational
\[
 x=(3^s-2^s)/(2^L-3^s)
\]
has the repeating shortcut word \(1^s0^{L-s}\). The classical periodic affine formula gives the value and exact word. It is the smallest state on its cycle, exceeds 33, and \(s/L>5/8\), so it passes the gate with growing slack. Its reduced denominator exceeds one, hence (1) removes its main cell. The shorter equality-slope example is \(211/13\), with word \((1^50^3)^\infty\). The supplied finite replay checks the exact rational trajectories. [Periodic-word formula](../../integrated/periodic-tails/README.md)

Equation (2) uses no Collatz dynamics. The quantitative ordinary-only approximation does not bound the trace on the actual gate. The next estimate would have to exploit how the accepted parity words restrict the **joint** signed minima. A single signed height cannot remove the exhibited positive rational cycles.


The [Lean arithmetic kernel](SignedHeightGauge.lean) checks the determinant multiple, the lower height inequality, the reciprocal error transfer and the integer denominator-selection margin. The lattice reduction, counting and uniform sum estimate are written proofs. The [exact control](check_signed_heights.py) enumerates every odd residue through modulus \(2^{15}\), recomputes both integer minima, checks selected rational and precision-loss cells, and executes all phases of three rational cycles. [Retained output](SIGNED_HEIGHT_CONTROLS.json)

