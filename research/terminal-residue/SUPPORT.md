# The topological support of the terminal residue has zero Lebesgue measure

**Proposed, source-qualified.** Let $U(x)$ be the odd part of $3x+1$ for odd positive $x$, let $m(n)$ be the least value on the ordinary orbit, and write $R(n)$ for the sum of $l(u)=\log_2(1+1/(3u))$ over the odd inputs before the first visit to $m(n)$. Let $\nu$ be the limiting natural law of $R$, and $\nu_t$ its unnormalized submeasure on the minimum cell $m=t$. Then
$$
 \operatorname{Leb}(\operatorname{supp}\nu)=0.
$$
The support of each positive-mass minimum cell, including the basin of $1$, has zero length and Hausdorff dimension one. The support conclusion uses the separate [pure singularity theorem](SINGULAR_FIBRES.md) and the lower interval estimate proved here. The dimension assertion uses the [lower Hausdorff dimension of the measure](REAL_DIMENSION.md). Pure singularity alone would permit full topological support. Leen identifies the support on the basin of $1$ with the closure of the residues of convergent starts coprime to $3$ and explicitly asks whether it has zero length. [Leen, support theorem and open questions](https://doi.org/10.5281/zenodo.23252397)

## A controlled residue interval at an ordinary ancestor

There exist absolute $c,C,C_0>0$ such that for every odd $3$-unit $a$, $M\ge a$ sufficiently large and $X\ge CM$, at least $cX/M$ odd starts in $(X/4,X]$ first land at $a$ below $M$, with
$$
 m(n)=m(a),\qquad 0\le R(n)-R(a)\le C_0/M.                         \tag{1}
$$
The relevant path control is retained in the proof of Theorem 14 of rStation paper 12. Its immediate odd parent $v$ of $a$ is between two absolute positive multiples of $M$. For the prefix from $n$ to $v$, Lemma 13 there gives $v=A n+B$ with $A=3^k/2^d$, $0\le B\le B_0$ for an absolute constant $B_0$, and $B<v/2$. All odd states before $a$ exceed $M$. Telescoping $U(u)=(3u+1)/2^{v_2(3u+1)}$ gives the additional residue exactly as
$$
 \log_2(v/(v-B))+l(v)\le C_0/M.
$$
The lower count, height bounds and clock normalization above are the ones in the cited proof. Even halvings add no odd input. [rStation paper 12, Lemma 13 and proof of Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1) · [Annular and minimum-law consequences](../fixed-floor-shells/FIRST_MOMENT.md)

## An interval about any finite first-minimum residue

Fix an odd unit source and read its finite path backwards from its first minimum. Denote the odd states by $x_0=t,x_1,\ldots,x_k$ with $U(x_j)=x_{j-1}$ and $x_j>t$ for all $j>0$. They are distinct, since repetition would force a previous visit to $t$. All are units, since $x_k$ is a unit and each earlier one is an odd image. Put $r_j=\sum_{h=1}^j l(x_h)$, $r=r_k$, and $d_i=r-r_{i-1}$ for $1\le i\le k+1$, so $d_{k+1}=0$.

For every $j\ge1$ take the unit sibling $s_j=4x_j+1$ if it is a unit, or $s_j=16x_j+5$ otherwise. It is indeed a unit in the latter case and
$$
 x_j<s_j\le21x_j,\qquad U(s_j)=x_{j-1},\qquad R(s_j)=r_{j-1}+l(s_j).
$$
Apply (1) to $a=s_j$, $M=\max(s_j,M_0)$ for an absolute onset $M_0$. It supplies at least $c'X/s_j$ sources with extra residue at most $C_0/s_j$ for all sufficiently large common $X$. These source families for different $j$ are disjoint. The unique reverse word of the source's **first** visit to $t$ follows the original path for $j-1$ letters, then exits via the exponent of $s_j$, either $2$ or $4$ larger than that of $x_j$. A longer shared-prefix word still uses the original exponent at that position. These exit words are prefix-free. All states before $s_j$ exceed $s_j$, and the fixed continuation first reaches $t$ at its last state. This disjointness therefore also holds when $t$ itself is periodic, independently of every subsequent cycle visit.

For $j\ge i$, every certified residue lies within $C_1 d_i$ of $r$, since $r-r_{j-1}\le d_i$ and $1/s_j\ll l(x_j)\le d_i$. The disjoint source counts give, for absolute $c_1,C_1>0$,
$$
 \nu_t([r-C_1d_i,r+C_1d_i])\ge c_1\sum_{j=i}^k 1/s_j\ge c_1' d_i.  \tag{2}
$$
Indeed sum the finite shell counts at a common $X$, normalize by $X$, and pass to the limiting joint law on the closed set with mark $t$. The last inequality uses $s_j\le21x_j$ and $l(x_j)\ll1/x_j$.

This gives absolute lower linear mass at every small radius, including between the tail sums. If $r>\delta>0$, select $i$ with $d_i>\delta\ge d_{i+1}$. When $d_{i+1}\ge\delta/2$, (2) at $i+1$ suffices. Otherwise $l(x_i)=d_i-d_{i+1}>\delta/2$ implies $x_i\ll1/\delta$. Apply (1) at $x_i$ with $M=\max(x_i,M_0,\lceil1/\delta\rceil)\ll1/\delta$; the resulting residues are within $C_2\delta$ of $r$, since $|r_i-r|=d_{i+1}\le\delta$. If $r\le\delta$, apply (1) at $1$ with $M=\max(M_0,\lceil1/\delta\rceil)$ to treat the unmarked measure. For the marked cell use $a=t$ in that last case when $\delta\le1/t$. Thus uniformly for every finite unit anchor residue $r$,
$$
  \nu([r-C_2\delta,r+C_2\delta])\ge c_2\delta\qquad(0<\delta\le1), \tag{3}
$$
with the same bound for $\nu_t$ when $\delta\le1/t$.

## Varying targets, finite limits and infinite inverse paths

Every point in the support of $\nu$ lies in the closure of the finite unit anchor residues. Initial powers of two can be stripped. Odd cores at most $H$ contribute $O_H(\log X)$ starts up to $X$, negligible for every fixed $H$. If an odd core $x$ is a multiple of $3$ and $m(x)<x$, its unit sibling $4x+1$ has the same odd successor and the same minimum, and their residues differ by $|l(x)-l(4x+1)|\ll1/x$. If $m(x)=x$, its residue is already the anchor value $0=R(1)$. This proves the closure assertion even for a sequence with varying minimum targets. For a positive-mass fixed cell the same argument applies: its minimum is a unit, since an odd multiple of $3$ can be reached only from its dyadic lifts.

One can also describe the limits directly. Along an arbitrary sequence of anchor paths, if $m\to\infty$ then $R\to0$, by the uniform orbit-packing bound on the reciprocal sum over distinct odd inputs above $m-1$. Otherwise extract a subsequence with fixed minimum $t$. For any given $H$, there are finitely many odd $u\le H$ whose paths reach $t$, each with a finite, unique clock to its **first** visit there. Hence only finitely many states can occur between such a $u$ and that visit. Diagonal extraction of the reverse words now gives one of the following cases. A path can terminate at a fixed finite prefix. A first unfixed letter can tend to infinity, making its odd parent tend to infinity; no state $u\le H$ can precede this parent on the sampled first-hit path once the parent is outside the above finite set. The residual before the fixed prefix is then bounded by the uniform orbit-packing tail above $H$ and tends to zero as $H\to\infty$. In the remaining case every fixed prefix stabilizes to a single infinite inverse path. After more than the largest of the finitely many first clocks from $u\le H$, every remaining state on every such path exceeds $H$, so again its residue tail is uniformly small. The limit is the convergent sum of $l(x_j)$ on the resulting infinite code. This argument uses first visits throughout and permits $t$ on a cycle. [Leen, orbit-set sparsity and residue-tail estimate](https://doi.org/10.5281/zenodo.23252397)

For any $r$ in the closure, choose a finite unit anchor within $\delta$ of $r$. Equation (3) transfers to $r$ on enlarging $C_2$ by one. Therefore at every support point the upper symmetric Lebesgue derivative of $\nu$ is bounded below by a fixed positive constant. The Lebesgue differentiation theorem gives derivative zero at Lebesgue-almost every point for a finite measure singular to Lebesgue measure. Its support consequently has Lebesgue measure zero. The conditional supports are closed subsets of that null support. Together with the dimension result this gives a compact null support of full dimension on each positive-mass minimum cell, in particular for Leen's set of convergent unit residues.
