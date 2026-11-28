# Exact correction collisions on multiplicative rectangles of ordinary sources

**Source-qualified deduction.** The asymptotic count uses the stated true fixed-target row law and counted-fusion estimate. The exact finite example below and its Lean proof require neither analytic input.

Fix any positive odd unit target $y$, including the known terminating target $5$. There are explicit populations of two independent multiplier choices $a,c$ and two independent cofactor choices $b,d$, all positive odd integers, with the following property as the scale $B$ of the larger coordinates tends to infinity. With probability
\[
                    \gg_y (\log B)^{-1/2}                              \tag{1}
\]
the four actual starts $ab,cb,ad,cd$ all reach $y$. Their four corrected values $P_y(n)=y2^{s(n)}3^{-j(n)}$ are **pairwise distinct**, but
\[
 \begin{aligned}
       j(ab)+j(cd)&=j(ad)+j(cb),\\
       s(ab)+s(cd)&=s(ad)+s(cb),\\
       B_y(ab)+B_y(cd)&=B_y(ad)+B_y(cb).
 \end{aligned}                                                        \tag{2}
\]
Here $j$ and $s$ are the actual first-hit odd grade and total shortcut clock, and $B_y(n)=\log(P_y(n)/n)$. All four starts are pairwise distinct as well. The four mark samples are correlated through the two common factors in each row or column. Before imposing the two exact clock equations, a positive fraction of these true rectangles with all four starts reaching $y$ have their signed correction sums on a common set of $O_y(\sqrt{\log B})$ exact real values.

In particular a uniform all-mesh small-ball upper $C r$ for the alternating mark on these finite ordinary product rectangles fails, even at a single known terminating target, before taking any marginal limit over the sources. At positive mesh $r_B=o((\log B)^{-1/2})$ the mass at zero in (1) exceeds that upper scale. A fixed number of independent copies can be much smoother. This statement does not assert an atom in a limiting single-target natural mark law.

## A dense bipartite graph of actual fast arrivals

Write $D=\log(4/3)$, $L=\log B$. The source-qualified fixed-target first-arrival law supplies $K=K_y$ and $p=p_y>0$ so that, uniformly on sufficiently large proportional octaves $[X,2X]$, at least $2p$ of all integer starts reach $y$ with
\[
                 |j(n)-\log(n/y)/D|\le K\sqrt{\log n}.                 \tag{3}
\]
It suffices to use the same central grade interval with center $\log(X/y)/D$ for a whole octave, increasing $K$ by a fixed amount. The ordinary-odd and all-integer forms agree by stripping initial twos. [Fixed-basin row law and proportional interval crop](FIXED_BASIN_NATIVE_WINDOW.md)

For completeness the same lower bound, decreased to $p$, holds when the sampled input in $[X,2X]$ is $ub$ with an odd multiplier $u\le L^{O_y(1)}$ and $b$ uniform on all positive odd integers in an octave $[V,2V]$, $V\ge B$, $X=uV$. Compare the first-hit mark of $ub$ to those of $ub+h$ for $0\le h<2u$, and tile the full physical interval by these consecutive blocks. Choose $t=\lfloor(\log_2 V)/4\rfloor$. The counted-fusion failure for a gap $h$ is a subset of complete binary classes modulo $2^t$ of proportion $O(\sqrt{(1+\log(2+h))/t})$. On the progression $ub$ with $b$ odd the density of these classes is at most twice that fraction plus $O(2^t/V)$. Counted fusion makes the first-hit grade identical on the successful pair, except when the target occurs before the fusion date, which costs $O(2^t/V)$ since each prefix has at most one source reaching $y$ at its endpoint. Alternatively all states through that date exceed $y$ for large $B$. Use an identical central grade test on the whole physical octave and enlarge its tolerance by a constant to arrive at (3). The small tiling ends cost $O(u/X)$. All errors tend uniformly to zero in this multiplier range. This comparison uses the true parity-period estimate on ordinary pairs. [Pinned affine counted-fusion bound with slope ratio one, PR146 at 04108117](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

Choose a fixed integer $N>4/p^2$. Let $c_0>0$ be the uniform simple-first-hit survival bound, so that $n\le P_y(n)\le n/c_0$. Fix an integer $M>8/c_0$. For each multiplier choose one of the $N$ bands of positive odds
\[
          [M^i L^2,\,2M^i L^2],\qquad 0\le i<N,
\]
uniformly among bands, then uniformly within the selected band. Use this law for $a,c$. For each cofactor choose one of
\[
   [M^{Nk}B,\,2M^{Nk}B],\qquad 0\le k<N_B=\lceil L^{2/3}\rceil,
\]
uniformly among bands and then uniformly among the positive odds within that band. Use this law for $b,d$. The largest log size among the products is $L+O_y(L^{2/3}+\log L)$, so all their square-root log scales are comparable. Distinct pairs of bands place their products in distinct intervals $[M^{i+Nk}BL^2,4M^{i+Nk}BL^2]$ separated even after multiplying the upper endpoint by $c_0^{-1}$.

Join $a,b$ by an edge when the actual product $ab$ hits $y$ and satisfies (3). The preceding source comparison gives edge density at least $p$. Let $w(a,c)$ be the conditional cofactor probability that both $ab$ and $cb$ are edges. By Cauchy–Schwarz on the cofactor coordinate, $\mathbb E_{a,c}w(a,c)\ge p^2$. Retain just pairs from different multiplier bands. Their contribution to this mean is at least $p^2-1/N\ge p^2/2$. This lower bound permits completely different good-neighbor sets at individual multipliers.

## A collision of actual pairs of clocks

For fixed retained $a,c$ and a common good cofactor $b$, define
\[
          v(b)=(j(ab)-j(cb),\,s(ab)-s(cb)).
\]
The first coordinate lies within $O_y(\sqrt L)$ of $\log(a/c)/D$, **regardless of the chosen cofactor band**. The second coordinate minus $\log_2 3$ times the first is
\[
                \log_2(a/c)+(B_y(ab)-B_y(cb))/\log2 .
\]
The last difference is bounded in absolute value by $2|\log c_0|$. Each first coordinate therefore determines only a bounded number of possible second coordinates. There are at most $C_y\sqrt L$ vectors $v(b)$ in total. For fixed $a,c$, two independent good cofactors have identical $v$ with unnormalized probability at least $w(a,c)^2/(C_y\sqrt L)$. Jensen on the retained multiplier pairs and their preceding positive mean give a lower bound $\gg_y 1/\sqrt L$ after averaging them. The probability that $b,d$ came from the same cofactor band is only $1/N_B=o(1/\sqrt L)$ and can be removed. All four pairs of bands are now distinct, so the four $P_y$ values and the four source heights are distinct. Equality $v(b)=v(d)$ gives the two clock equations. Since $(ab)(cd)=(ad)(cb)$ holds literally, taking the logarithms of the four exact $P_y$ identities proves the last equality in (2).

For the positive-mass support statement, the ordinary rectangle density is at least $p^4$ by two applications of Cauchy–Schwarz. One may require distinct multiplier bands by the lower bound on the mean of $w$ after restriction, and distinct cofactor bands at cost $1/N_B$. For every such rectangle its alternating grade is $O_y(\sqrt L)$: the central log source terms cancel exactly by the multiplicative identity. Its alternating native total is restricted to $O(1)$ values per grade, using the bounded correction and the same identity. This gives $O_y(\sqrt L)$ exact possible alternating marks simultaneously over the entire population.

If $y$ is on a hypothetical escaping component, the complete future correction of each input in this construction is $B_y(n)+B_\infty(y)$. The common added constant cancels in (2), yielding the same result for full marks. A collision in (2) compares initial source products and the two total first-arrival clocks. It does not force equality of products of distinct forward waypoints after the common target.

## A literal ordinary example

Take multipliers `a=3,c=5` and cofactors `b=27,d=23`. The four sources `(81,135,69,115)` first hit 5 at respective `(odd count, native time)` pairs `(5,12),(12,24),(2,7),(9,19)`. Thus `81·115=135·69`, both opposite clock sums agree, and the four corrected values are `20480/243`, `83886080/531441`, `640/9`, and `2621440/19683`. They are pairwise distinct and their opposite products agree exactly. [ClockRectangle.lean](ClockRectangle.lean) proves the four actual first visits, absence of earlier visits, distinctness and both exact product equalities. The [independent transcript control](check_clock_rectangle.py) replays all 62 native steps. This certifies one genuine correlated collision; it does not certify the asymptotic lower bound by itself.
