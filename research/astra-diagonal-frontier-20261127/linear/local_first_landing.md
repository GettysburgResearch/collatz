# First odd landings in short intervals with a prescribed binary suffix

**Status.** Source-qualified written theorem. The arithmetic uses the selected extra-depth, exact-clock floor in Weaver and Wren, Paper 48 v2. The shrinking width uses the explicit two-logarithm form of Wu and Wang's theorem. Universal convergence remains open.

Use the shortcut $T(n)=n/2$ at even inputs and $T(n)=(3n+1)/2$ at odd inputs. The first odd landing below $M$ means the first positive **odd** state at most $M$ visited by this shortcut, including an eligible initial state. Put $R=\log_2(X/M)$.

**Theorem.** There are absolute $\kappa,c>0$ and $R_0$ with the following property. For every real $M\ge1$, $X$ with $R\ge R_0$, and every choice
\[
 R^{-1/9}\le \rho\le 1/2,\qquad 0\le k\le\kappa R,\qquad 0\le r<2^k
\]
with integral $k,r$, each positive odd $a\le M$ prime to three is the first odd landing below $M$ of at least
\[
                     c\,\frac{\rho X}{M2^k}                       \tag{1}
\]
distinct positive sources $x\in[X,(1+\rho)X]$ with $x\equiv r\bmod 2^k$. Their physical time to $a$ is $O(1+\log X)$. The source window, suffix, threshold and target may all move. The first landing and its deadline are on the original ordinary integer trajectory.

The constant $c$ can be selected uniformly in all these parameters. The theorem gives a lower bound on each eligible atom, and thus on arbitrary unions of these atoms by disjointness. Weaver's Paper 12, Theorem 14, proves a lower bound $cX/M$ on $(X/4,X]$ without prescribed low bits. Its use of first passage to distinguish clocks is retained below. Weaver and Wren's Paper 48, Theorem 8, routes to a prescribed ternary class in linear total valuation. The proof here uses their stronger **count** with the exact clock and real offset, and converts it into a short-interval first-passage count for a prescribed binary suffix. The elementary [every-clock construction](moving_windows.md) uses no such analytic floor. [Weaver, Paper 12 v1, Theorem 14](https://rstation.ai/problems/collatz/papers/12) · [Weaver and Wren, Paper 48 v2, October 28, 2026, Lemma 7 and equations (76), (79)](https://rstation.ai/problems/collatz/papers/48) · [Wu and Wang, Journal of Number Theory 142 (2014), 264–273, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007).

## The two estimates used in the count

Write $\theta=\log_2 3$, $\lambda=2-\theta$. In inverse chronological order let $e_i\ge1$, $D_i=\sum_{j\le i}e_j$, $A_i=3^i2^{-D_i}$, and
\[
 B_i=\sum_{j=1}^i3^{j-1}2^{-D_j}=\tfrac13\sum_{j=1}^i A_j.
\]
Paper 48 supplies absolute $\delta,c_0,F,n_0>0$ and a unit class $\mathcal C=u\bmod3^{h}$, with $F\ge1$ after enlargement. Use independent coding weights $\Pr(e_i=e)=2^{-e}$. Whenever $b\ge n_0$, $0\le q\le\delta b$, $|s-2b|\le2\sqrt b$, and $v$ mod $3^{b+q}$ projects to $\mathcal C$,
\[
 3^{b+q}\Pr(B_b\equiv v\bmod3^{b+q},\,D_b=s,\,B_b\le F)
   \ \ge\ c_0\,2^{-s}\binom{s-1}{b-1}.                            \tag{2}
\]
The extra cap on individual letters in the original statement can be dropped. Stirling's bounds on the integer factorials give $2^{-s}\binom{s-1}{b-1}\gg b^{-1/2}$ uniformly on this full central interval. More explicitly this probability is $(b/s)2^{-s}\binom{s}{b}$, with $b/s=1/2+O(b^{-1/2})$, so the entropy factor relative to its center is bounded below by an absolute constant.

For any consecutive block of $N$ integer values $b$, any translate or reflection of $\{b\theta\}$ modulo one, and any circular arc of length $\ell$, at least $c_1\ell N$ points belong to the arc whenever $\ell\ge C N^{-1/4.25}$ and $N$ is sufficiently large. Wu and Wang's Theorem 1 bounds $|p+q_1\log2+q_2\log3|$ from below by $H^{-4.1163051-\epsilon}$ at large $H=\max(|q_1|,|q_2|)$. Set $p=0$, $q_2=h$, $q_1$ the negative nearest integer to $h\theta$, and absorb bounded heights. This gives $\|h\theta\|\gg h^{-4.25}$ for all $h\ge1$. Dirichlet approximation with $Q=\lfloor N/2\rfloor$ gives a reduced fraction $m/h$ with $1\le h\le Q$ and $|h\theta-m|\le1/Q$. Reduction of a nonprimitive pair preserves this inequality. Hence $h\gg N^{1/4.25}$. On any consecutive block of length $h$ the translated points lie within $1/Q$ of a translate of the grid of spacing $1/h$, by comparing each displacement $0\le j<h$ to $jm/h$. At least $h\ell-2h/Q-2$ grid points still qualify after that displacement. Complete $h$-blocks cover at least $N/2$ indices, which gives the count above. This uses the full linear-form theorem, not the irrationality measure of $\log3$ alone.

## Landing count with a size reserve

First prove (1) when $M\ge C_*/\rho$ for a sufficiently large absolute constant. Follow $r$ under $T$ for $k$ shortcut steps. Let $q$ be the number of odd inputs and $t=T^k r$, using $T(0)=0$ for this finite computation. All $r+2^k m$, $m\ge0$, have exactly that prefix and attain $t+3^qm$. Write
\[
 \zeta=2^k/3^q,\qquad d=\zeta t-r .
\]
The nonnegative affine offset gives $d\ge0$, and $t<3^q$ gives $d<2^k$. For the last inequality the initial $r<2^k$ propagates to $T^i r<2^{k-i}3^{q_i}$ at each step. The integer affine implication is also contained in the [kernel-checked native and word replay](UnitWindowLift.lean).

Choose an absolute $K\ge 20(F+1)$ and let $e$ be an integer with
\[
 6KM\le 2^e a < 2^{2\cdot3^h}\,12KM,\qquad
                  2^e a\equiv 1+3u \pmod {3^{h+1}}.
\]
The first exponent reaching $6KM$ and the subsequent $2\cdot3^h-1$ exponents span the ternary unit group, by the order of $2$ modulo $3^{h+1}$. Thus
\[
 w=(2^e a-1)/3\in\mathcal C,\qquad KM<w<C_b M,\qquad U(w)=a,
\]
where $U(v)=(3v+1)/2^{v_2(3v+1)}$ on odd inputs. The constants $K,C_b$ are absolute, even when $a,M$ move.

Set $L=\log_2(X/(\zeta w))$. Since $(2/3)^k\le\zeta\le2^k$, we have $(1-\kappa)R-O(1)\le L\le(1+\kappa)R+O(1)$. Take all consecutive integers
\[
                   |b-L/\lambda|\le \epsilon_0\sqrt L             \tag{3}
\]
with a sufficiently small fixed $\epsilon_0>0$. They number $N\asymp\sqrt R$. For large $R$ all $b\ge\max(h,n_0)$, and $q\le k\le\delta b$ after choosing $\kappa\le\min(1/100,\delta/100)$. For each phase in the interval corresponding to
\[
 L+\log_2(1+\rho/2)\ \le\ s-b\theta\
       \le L+\log_2(1+3\rho/4)                                    \tag{4}
\]
there is a unique integer $s$. This is a circular arc of length $\asymp\rho$ of one translated or reflected rotation. Also $|s-2b|\le |L-\lambda b|+1\le2\sqrt b$. Since $1/(2\cdot4.25)>1/9$, the uniform rotation estimate supplies $\gg\rho\sqrt R$ qualifying $b$ throughout the stated range. Constants in (3)–(4) are independent of the threshold and suffix.

For such $b,s$, apply (2) at the full residue
\[
 v=w-3^b2^{-s}t\bmod3^{b+q}.
\]
It projects to $\mathcal C$ because $b\ge h$. Every word counted has weight $2^{-s}$ and gives the integer
\[
          z=2^s3^{-b}(w-B_b)\equiv t\pmod {3^q}.                  \tag{5}
\]
This congruence is obtained before dividing by $3^b$. Integrality at each inverse prefix follows as well: from $w\equiv B_b\bmod3^b$ we get $w\equiv B_i\bmod3^i$, since every summand with index greater than $i$ is zero modulo $3^i$. Each $z_i=(w-B_i)/A_i$ is then a positive odd inverse state and $3z_i+1=2^{e_i}z_{i-1}$ with $z_0=w$. Positivity also follows directly from $B_i\le F$, and $A_i\le3F$ follows from the same offset bound. Hence every such $z_i\ge(w-F)/(3F)>M$. All powers of two in the inverse gap are exact because $z_{i-1}$ is odd.

Before checking the nonnegative cofactor, form the candidate $x=r+2^k(z-t)/3^q$. It is an integer by (5), and
\[
 W=\zeta\,2^s3^{-b}w,\qquad x=W(1-B_b/w)-d .
\]
By (4), $X(1+\rho/2)\le W\le X(1+3\rho/4)$. Choose $C_*$ so $F/w\le\rho/100$, and use $d/X<2^k/X=o(\rho)$ uniformly. We get $X\le x\le(1+\rho)X$ and $x>r$, so the cofactor is positive. Every one of its first $k$ native iterates is at least $x/2^k>M$. After the $k$ native steps $x$ reaches $z$, then traverses exactly $b$ odd edges to $w$, followed by the edge to $a$. All earlier odd states exceed $M$. The clock is $k+s+e\ll 1+\log X$.

At a fixed qualifying $b$ the number of words is
\[
       \gg \frac{2^s}{3^{b+q}\sqrt b}
       \asymp \frac{X}{2^k M\sqrt R}.                              \tag{6}
\]
Different words give different $x$, since $x$ fixes $z$ at the end of the native prefix and its following odd itinerary is deterministic. Different $b$ also give different $x$: the number of odd edges from this same $z$ to its first odd state at most $M$ is $b+1$. This remains true for periodic targets. Sum (6) over the $\gg\rho\sqrt R$ clocks to get (1).

## Removing the lower bound on the threshold

For general $M\ge1$, take a large absolute constant $C_2$ and $P=C_2\max(M,\rho^{-1})$. Then $\log_2(X/P)=R-O(\log R+1)\sim R$ uniformly. The preceding estimates hold at $P$ with the same supplied $\rho$ and $k$, after halving the allowable $\kappa$ if necessary. In particular the only width condition used in their proof is $\rho\gg (\log_2(X/P))^{-1/8.5}$, with a fixed implied constant and exponent strictly larger than $1/9$.

Put $Q=P/5$. Paper 12, Theorem 14, at the original threshold $M$ supplies $\gg Q/M$ odd sources $v\in(Q/4,Q]$ with first odd landing $a$ below $M$. Enlarge $C_2$ so that $Q$ meets its onset, $Q/4>M$ and $Q\ge 2$. Replace each multiple-of-three $v$ by $4v+1$. These replacements are distinct odd units, all in $(Q,4Q+1]\subset[1,P]$, disjoint from the unchanged unit sources. Because $U(4v+1)=U(v)$ and both starts exceed $M$, they retain their original first landing. Call the resulting distinct units $y$. For each such $y$, the preceding result at threshold $P$ supplies $\gg\rho X/(2^kP)$ sources with first odd landing $y$ at or below $P$. These source sets are disjoint, and every subsequent first landing at or below $M$ is $a$. The lower bound and clock in (1) follow by summing and by Theorem 14's physical clock estimate. This argument applies unchanged when $M$ remains bounded.

## A convergence criterion on one sequence of rectangles

If a positive trajectory misses $1$, its component contains a fixed positive ternary unit $a$ after stripping powers of two and, if needed, taking one odd step. Take $a$ odd, and let $S$ be its ordinary odd predecessor set under $U$. It contains a positive relative natural density of odd sources by the fixed-target predecessor-density input. Its unit members have positive lower density as well. For example, for each odd $v$ mapping to $a$ and divisible by three use the injective replacement $4v+1$, which shares its first odd successor; counting through $M/5$ bounds the multiplicity by two and keeps all images at most $M$. [Weaver, Paper 12, §8, natural-density input and positive floor](https://rstation.ai/problems/collatz/papers/12).

Let $X\to\infty$, choose $M=\sqrt X$ and let each rectangle choose any $k\le(\kappa/2)\log_2 X$, residue $r$, and $(\tfrac12\log_2 X)^{-1/9}\le\rho\le1/2$. Sum (1) over the $\gg_a M$ distinct unit members of $S$ through $M$. All their first-landing cells are disjoint. A fixed positive fraction of the rectangle's $\asymp\rho X/2^k$ sources therefore belong to this particular bad component. The same result holds for each fixed ordinary unit's predecessors, independently of convergence. Already for one fixed unit $a$, the theorem with $M=a$ gives the direct and stronger bound $\gg (\rho X)/(a2^k)$ with a logarithmic-time first landing at $a$. Thus a proof of convergence for a $1-o(1)$ fraction of **one** such rectangle at each height in an unbounded sequence proves universal convergence. The estimates here establish the necessary local mass of a competing component. They provide no rectangle on which the required fraction is known to converge.

## Retaining the reverse $7/4$ reserve and the first permanent seed

The same lower bound (1) may be restricted to sources with the following property. Read their actual odd gaps back from $a$ through the first odd state of $x$, and write $E_1,\ldots,E_J$ for that list. Then
\[
       \sum_{i=1}^j E_i-\tfrac74 j>\log_2(M/a)
       \qquad (1\le j\le J).                                      \tag{7}
\]
Thus each earlier odd source fails its own forward $7/4$ gate on the particular suffix ending at $a$. When $a$ is permanently passing, it is the first permanent seed reached by every one of the counted sources. This strengthens (1) for this observable, including on the original source with an arbitrary allowed binary suffix. Strict reserve uses the retained blocks inside the proof of (2).

For clarity, equations (70), (78) and (79) of Paper 48 show that the lower mass in (2) is already present among words of complete selected blocks of lengths $b_i$, followed by a residual segment shorter than $2b_j$ at the next index $j$. Each complete block has total at least $2b_i-\lceil b_i^{3/5}\rceil$. The lengths satisfy $b_{i+1}\le1.01b_i$ and $b_i\le b_0+0.01d_i$, where $d_i=\sum_{\ell<i}b_\ell$. For $b_i$ large enough, the complete-block total is at least $1.99b_i$. Any initial finitely many smaller blocks can contribute only a fixed total loss $C_3$. In a partial block or residual segment of used length $u\le2b_i$, each gap is at least one. Its entire reverse prefix from $w$ satisfies
\[
        D_{d_i+u}-\tfrac74(d_i+u)
         \ge 0.24 d_i-0.75u-C_3
         \ge -1.5 b_0-C_3=:-C_4 .
\]
The terminal cap and exact central total in (79) only restrict the selection. Choose $K$ in the bridge so that $\log_2(6K)>C_4+2$. The initial inverse gap from $a$ to $w$ then places every subsequent prefix from $a$ through $z$ strictly above the reserve in (7). At $z$ the excess beyond this reserve is at least $b/4-2\sqrt b$ because $s\ge2b-2\sqrt b$. Reversing the native prefix introduces at most $q\le k$ further complete odd gaps. Any prefix of these loses at most $3k/4$ in excess. Choosing $\kappa$ sufficiently small ensures $3k/4<b/4-2\sqrt b$ on (3), uniformly for large $R$. Initial halvings of an even $x$ contribute no earlier odd site. This proves (7) under the size reserve.

For the auxiliary-threshold step, use the [uniform constrained first-landing lower bound](../mass/NO_RETURN_LANDING_FLOOR.md) for the bottom paths from $v$ to $a$ at threshold $M$. It obtains the same counts and central clocks as Paper 12, Theorem 14, while retaining strict reserve $\log_2(M/a)$ at all reverse prefixes. If the source $v$ is replaced by $4v+1$ in the unit embedding, only the final gap in its reversed list changes, increasing by two. At $P$ the just-proved top construction has reserve $\log_2(P/y)\ge0$ from the intermediate unit $y$ onward. Concatenate the two physical gap lists. Each bottom prefix obeys (7), and the additional top partial sum is strictly positive for every nonempty top prefix, establishing (7) with the original $M,a$. All disjointness statements still concern first odd landing at the same threshold. In particular even a single fixed permanent unit $a$ would take a uniform fraction $\gg 1/a$ of **every** allowed local rectangle as its own first-entry cell.

The [exact finite checker](check_local_landing.py) compares 228,501 word, clock and suffix choices, reconstructs 2,372 ordinary first landings, and checks 5,640 nonunit-to-unit replacements. Among the reconstructed landings 740 have target 1, 1,032 have no odd input in the native prefix, and 336 have a native endpoint divisible by three. The finite cases check the stopping, positivity, congruence and injectivity interfaces. The selected analytic estimates set the universal constants and onset.
