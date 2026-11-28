# Integer-cycle restrictions after summing visits to the same clock rank

Let a positive primitive rational odd cycle have division exponents $e_i\ge1$, odd period $p$, total divisions $h$, common reduced odd denominator $q$, positive determinant $D=2^h-3^p$, and carry $C=\sum_i3^{p-1-i}2^{E_i}$, where $E_i=\sum_{l<i}e_l$. Put $g=\gcd(h,p)$, $a=h/g$, $b=p/g$, $\gamma=\log_2 3$, $\Delta=a-b\gamma>0$, $\Lambda=g\Delta$. We use the nontrivial integer-cycle strip $\gamma<a/b<2$, and assume $b\ge2$. All finite inequalities below also apply to rational cycles in this strip.

Root at the actual least odd state $m$. Write
\[
 r_i=ia\bmod b,\qquad d_i=\lfloor ia/b\rfloor-E_i,\qquad
 U=\max_i d_i,\qquad W=U-\min_i d_i.
\]
For $0\le r<b$ sum all $g$ visits to rank $r$ *before* taking neighboring differences:
\[
 c_r=\sum_{r_i=r}2^{U-d_i},\qquad
 n_0=2c_0-c_{b-1},\quad n_r=2(c_r-c_{r-1})\quad(1\le r<b),\qquad
 K=\#\{r:n_r\ne 0\}.
\]
This can remove a defect even when each of the individual visits changes. The seam factor in $n_0$ is part of the definition. Put $M=\max c_r\le g2^W$.

For every nontrivial primitive positive **integer** cycle and each fixed $\nu>4.116201$, put $\delta=1/(1+\nu)$. Along increasing $p$ one has
\[
 K[W+\log(2p)]\gg_\nu
 \max\bigl((p/\log(2p))^\delta,m^\delta\bigr),\qquad
 W+1\le (K+1)\lfloor(g+1)^2/4\rfloor.                   \tag{1}
\]
In particular for any fixed clock gcd $g$, the number of changes of the **summed** profile grows at least as $p^{1/(2(1+\nu))-o(1)}$, with arbitrary physical spread and arbitrary division exponents. For an upper convergent $a/b$ to $\gamma$ we obtain the stronger finite inequality
\[
                   b\le K\log_3\frac{4KMq\,2^\Delta}{2^\Delta-1}.      \tag{2}
\]
For integer cycles and fixed $g$ this gives $K\gg_g\sqrt b$ along those convergents. Sections below give bounds for arbitrary growing $g$ and restrictions for fixed physical spread. These are necessary conditions. No estimate here rules out general cycles having rapidly varying summed profiles.

## Rational chronological lifts and their average

Let $v\in[1,b)$ satisfy $va\equiv1\pmod b$, $u=(1-va)/b$, $X=2^{-u}3^{-v}$, $F=2^a-3^b$ and $\xi=2^{-1/b}$. Modulo $F$, both $X^b=1/2$ and $X^a=1/3$ hold, with two and three invertible. The order-one specialization of the [rank identity](SPECTRAL_NEAR_OCTAVE.md) gives
\[
  2^U3^{1-p}C\equiv\sum_{r=0}^{b-1}c_r X^r\pmod F.
\]
Here $U\ge0$ from $d_0=0$. The polynomial $H(T)=\sum n_rT^r$ represents $2(1-X)\sum c_rX^r$ modulo $F$, and the same identity holds at $T=\xi$ over the reals. Write $H_*=H(\xi)$. Positivity gives $g\le H_*\le M$ by summing the geometric series, so $K\ge1$.

A cut after changing the start of the reduced odd clock to $j\in[0,b)$ has rank $r_j=ja\bmod b$. For each rank put $t_r=(vr-j)\bmod b$ and $l_r=(at_r-r+r_j)/b$. This integer is nonnegative, since $t_r=0$ forces $r=r_j$ and $a>b$. Define
\[
 T_j=\sum_{r:n_r\ne0} n_r2^{l_r}3^{-t_r},\qquad
 Z_j=2^{-r_j/b}T_j=\sum_r n_r\xi^r2^{t_r\Delta/b}.
\]
In the residue ring the summand's monomial is $X^{r-r_j}$, so $T_j\equiv X^{-r_j}H(X)\pmod F$. Each cut represents the same gcd obstruction. If $L_j=b-\max_{n_r\ne0}t_r$, then $3^{b-L_j}T_j$ is an integer divisible by $\gcd(F,C)\ge F/q$. The latter comparison follows from $F\mid D$ and $q=D/\gcd(D,C)$. Also $|T_j|\le4KM2^\Delta$ and $F=3^b(2^\Delta-1)$. Whenever $T_j\ne0$ this gives
\[
 L_j\le L_*:=\log_3\frac{4qKM2^\Delta}{2^\Delta-1}.                  \tag{3}
\]

For each fixed $r$, the lag $t_r$ runs once through $0,\ldots,b-1$ over all $j$. Hence $\sum_j Z_j/b=H_*\sum_{t<b}2^{t\Delta/b}/b\ge H_*$. Individually
\[
 Z_j\le H_*+2KM(2^\Delta-1).
\]
The cuts with $L_j\le L_*$ lie within the next $\lfloor L_*\rfloor$ chronological positions following some supported rank date, with circular wrap. Consequently
\[
 b\le K L_*\left(1+\frac{2KM(2^\Delta-1)}{H_*}\right).               \tag{4}
\]
Some ordinary real transfers in this argument are signed. For example the minimum-rooted positive rational cycle with gap list $(1,1,1,2,2,2,1,1,3,4)$ has $h=18,p=10,g=2$, columns $(10,4,3,6,12)$, coefficients $(8,-12,-2,6,12)$ and $T_0=0$. A bound based on every chronological lift being nonzero would require an additional argument.

## A change of rank displacement making every lift positive

Fix $s\in\{1,\ldots,b-1\}$. Reduce $2(1-T^s)\sum c_rT^r$ modulo $T^b-1/2$ to obtain coefficients
\[
 n^{(s)}_r=2c_r-\begin{cases}2c_{r-s},&r\ge s,\\c_{r-s+b},&r<s.\end{cases}
\]
Their support size $K_s$ is at most $sK$, by the geometric factor $1+T+\cdots+T^{s-1}$ applied to $H$. Also $|n^{(s)}_r|\le2M$, so (3) applies with $K_s$ in place of $K$. A common factor of $1-X^s$ and $F$ does not affect this implication: the original $\gcd(F,C)$ still divides each cleared lift.

Set $v_s=vs\bmod b$. Summing by parts in rank, including the halved wrap, writes its normalized lift as
\[
  2\sum_r c_r\xi^r 2^{t_r\Delta/b}
       \left[1-\xi^s 2^{(t_{(r+s)\bmod b}-t_r)\Delta/b}\right].       \tag{5}
\]
The lag difference in the bracket equals $v_s$ or $v_s-b$. Thus if $v_s\Delta<s$, every term is positive. Every chronological gap between successive supported rank dates then has length at most the right side of (3), with $K_s$. In particular,
\[
 b\le K_s\log_3\frac{4qK_s M2^\Delta}{2^\Delta-1}
   \le sK\log_3\frac{4qb M2^\Delta}{2^\Delta-1}.                      \tag{6}
\]
For $s=1$ the sign condition says $(va-1)/(vb)<\gamma$. This rational is the left Farey parent of $a/b$ (written in ordinary reduced form as $((va-1)/b)/v$). At an upper continued-fraction convergent its previous, lower convergent is exactly this parent. This proves (2).

For the general case choose a lower continued-fraction convergent $n/t<\gamma$ whose denominator is the largest denominator of a lower convergent not exceeding $Q=(b/\Delta)^{\nu/(1+\nu)}$. The elementary convergent error $0<t\gamma-n<1/t'$ uses the denominator $t'$ of the immediately following upper convergent. The denominator $t''$ of the next lower convergent exceeds $Q$. The homogeneous logarithmic-form bound $|x-y\gamma|\gg_\nu\max(1,|x|,|y|)^{-\nu}$ gives $t''\ll_\nu (t')^\nu$ by applying it to the upper convergent. Therefore $t'\gg_\nu Q^{1/\nu}$ and the positive integer
\[
     s=at-bn=t\Delta+b(t\gamma-n)
       \ll_\nu Q\Delta+bQ^{-1/\nu}
       \ll_\nu b^{1-\delta}\Delta^\delta                              \tag{7}
\]
satisfies $s>t\Delta\ge v_s\Delta$ whenever $s<b$, since $v_s=t\bmod b$. For ordinary integer cycles, distinct positive odd states imply
\[
 0<\Lambda=\sum_i\log_2(1+1/(3x_i))
    \le \min\{p/(3m\log2),\ O(\log(2p))\}.                            \tag{8}
\]
The second estimate sums reciprocals of distinct odds. Furthermore $\Delta\gg_\nu b^{-\nu}$ gives $p\ll_\nu b^{1+\nu}\log(2p)$ and hence $b\to\infty$ as $p\to\infty$. It follows that $Q\to\infty$ and $s<b$ for all sufficiently large periods. The logarithm in (6) is $O_\nu(W+\log(2p))$ when $q=1$. Equations (6)–(8) now give the first assertion of (1).

The logarithmic-form input used in (7)–(8) follows by taking the constant coefficient zero in Bondareva, Luchin and Salikhov's Theorem 1, p. 18. Their exponent is $4.116201$. The earlier Wu–Wang exponent $4.1163051$ suffices with that value substituted throughout. [Bondareva–Luchin–Salikhov (2018)](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Wu–Wang (2014)](https://doi.org/10.1016/j.jnt.2014.03.007)

## Amount of height a single aggregate can conceal

Each distinct $c_r$ is a sum of exactly $g$ powers of two. If $c_r$ has $l$ one-bits, merging equal powers in this representation takes exactly $g-l$ binary additions. Trace any original summand to a final one-bit at place $z$. Its exponent lies between $z-(g-l)$ and $z$. Across *all* such representations, every possible exponent therefore belongs to at most $l$ intervals of length $g-l+1$ in integers, totaling at most $l(g-l+1)\le\lfloor(g+1)^2/4\rfloor$ places. There are at most $K+1$ distinct column sums, by following their linear order in $r$. Since $d_{i+1}-d_i\le1$ in the strip and $d$ is periodic, every integer between its minimum and maximum occurs. The powers $2^{U-d_i}$ consequently use all exponents from zero through $W$. This proves the second inequality of (1).

For fixed $g$, this gives $W=O_g(K+1)$. Solving $K(K+\log(2p))\gg_{g,\nu}(p/\log(2p))^\delta$ gives the stated $p^{\delta/2-o(1)}$ lower bound. At an upper convergent, (2) instead gives $K(K+\log(2p))\gg_g b$, and $p=gb$ gives $K\gg_g\sqrt b$.

## A bounded physical spread

If $R=\max x_i/m$ stays bounded for integer cycles, (8) improves to $\Lambda=O_R(1)$: distinct odd states give $\sum_i 1/x_i\le1/m+(\log R)/2$. The physical identity $\log_2(x_i/m)=r_i/b+d_i+\theta_i$, with fluctuation $|\theta_i-\theta_j|\le\Lambda$, gives $W\le\log_2R+1+\Lambda=O_R(1)$. Since $H_*\ge g$ and $M\le g2^W$, (4) gives
\[
 K\gg_R\min\bigl(b/\log(2p),\ \sqrt{p/\log(2p)}\bigr).               \tag{9}
\]
Here $2^\Delta-1=O_R(1/g)$ and $L_*=O_R(\log(2p))$. The alternative bound $2^\Delta-1=O_R(b/m)$ from (8) likewise gives
\[
 K\gg_R\min\bigl(b/\log(2p),\ \sqrt{m/\log(2p)}\bigr).               \tag{10}
\]
The sums $c_r$ forget the order of the $g$ visits and can also forget their multiset when $g\ge3$. Thus (9)–(10) constrain a coarser observable than the number of defects of individual visiting phases.

For $g=1$, square-root growth of the individual rank-plateau count with unrestricted spread is already known and stronger than the unrestricted exponent in (1). Earlier noncoprime results control the number of **individual** defects of an upper window, using oddness at the first surviving term before projection. The fold used here can have genuine signed cancellation, as the rational example above shows. The positive-displacement criterion, the all-cut average and the binary-carry bound quantify the changes that survive summation. [Earlier coprime correspondence and bounds](https://rstation.ai/problems/collatz/papers/24/v3) · [Earlier noncoprime window bounds](https://rstation.ai/problems/collatz/papers/22/v4)


[Exact replay](check_folded_farey.py) enumerates 53,141 primitive noncoprime positive rational cycles throughout the strip up to $h=22$. It checks 214,447 rank displacements, including 107,276 with the all-cut sign guarantee, and reconstructs 3,877 mean identities symbolically in $\mathbb Q(2^{-1/b})$. There are 16 examples with a zero cut and 14,920 with a negative cut. In 603 examples adjacent equal column sums even conceal different multisets of the original powers of two. [Archived counts](../../../reports/astra-infinite-descent-20261127/cycles/FOLDED_FAREY.json)
