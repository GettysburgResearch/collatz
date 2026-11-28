# Constructing periodic references from actual nearby copies

**Proposed effective finite consequence.** Let $w$ be the shortcut parity itinerary of a fixed nonperiodic signed rational $x\in\mathbb Z_2$. Let a length-$P$ prefix be partitioned into $K$ nonempty pieces. On every piece supply either a single exceptional letter or a second occurrence of its complete binary word at a nonzero displacement of absolute value at most $B$ in the **same** trajectory. Displacements may change across pieces, point backward or forward, and lead to overlapping copies. With an absolute effectively computable $C$,
$$
 P\le \exp\!\left(C\frac{K+1}{\ln(K+2)}\right)
                   [\,1+\log_2 H(x)+B\,].                               \tag{1}
$$
Here $H(x)=\max(|a|,q)$ at the reduced source $a/q$. The same result applies to a finite rational trajectory wherever the constructed starting references are separated from the physical states. In particular it applies before a positive integer enters any of the particular rational cycles supplied below. No nonlinear growth premise on the physical states is used.

Indeed, suppose equal length-$d$ binary words begin at $i$ and $i+h$ with $h\ne0$ and both indices nonnegative. Shift the origin to the earlier occurrence. Their enclosing length-$d+|h|$ word has period $|h|$: the complete list of comparisons inside that interval is exactly the $d$ given equalities. This remains true when $d<|h|$, including the letters between the two occurrences. Thus the first occurrence, at whichever index the physical piece starts, follows the periodic extension of the first $|h|$ letters of that enclosing word for all its $d$ steps.

Take its rational periodic phase center as the reference and transport it to the terminal phase of the same periodic extension. This is an **explicit** construction on the two given occurrences. If $u=|h|$ and the period contains $g$ odd letters, both centers have reduced denominator dividing $|2^u-3^g|$. Their unreduced numerator is the nonnegative word carry, at most $3^u$, including at any cyclic phase. Their maximum height is at most $3^u$. If the phase center equalled the physical state, determinism of the actual parity orbit would give a periodic tail, excluded here. Exceptional letters can use the centers of the one-letter words $0$ and $1$, namely $0$ and $-1$, with the same separation. Apply the [quantitative reference bound](QUANTITATIVE_REFERENCE_COVERS.md) and its [signed extension](FULL_LANGUAGE_EXCLUSION.md) to this constructed cover to obtain (1). The constants here do not require an effective location for any exceptional Subspace Theorem height interval. The charged interval counts and logarithmic widths suffice, as in that theorem.

## Every separated edit return supplies such a cover

Compare $w[0,P)$ and $w[\ell,\ell+P)$ on the raw shortcut clock, where $\ell\ge1$. Suppose an edit alignment has cost $E$, counting an unequal substitution, insertion or deletion as one. On each maximal string of equal aligned columns, the native state-index displacement $h$ stays constant, with $|h|\le\ell+E$. Assume it never vanishes at a matched run. The stronger condition of physical separation on every boundary in the [edit endpoint theorem](EDIT_ALIGNED_ORBITS.md) suffices. There are at most $E+1$ matching runs and at most $E$ exceptional first-track letters. Remove empty pieces; every first-track bit is now covered. Equation (1) gives, after increasing its absolute effective constant,
$$
 \boxed{\displaystyle
 P\le\exp\!\left(C'\frac{E+1}{\ln(E+2)}\right)
                   [1+\log_2 H(x)+\ell].}                              \tag{2}
$$
Here $1+\log_2 H(x)+\ell+E\le(E+1)(1+\log_2 H(x)+\ell)$, and the additional factor $E+1$ is absorbed by the exponential. No fixed-budget limit was taken.

Write $R=P/[1+\log_2 H(x)+\ell]$. For $R$ sufficiently large, (2) implies $E\ge c\ln R\ln\ln R$ for an absolute effective $c>0$. This follows by inverting the increasing function $(E+1)/\ln(E+2)$ for large arguments. For arbitrary optimal equal-length Levenshtein alignments one has the precise alternative
$$
 d_E(w[0,P),w[\ell,\ell+P))\ge
          \min\{2\ell,\ c\ln R\ln\ln R\}.                              \tag{3}
$$
Indeed a zero displacement at any column requires at least $\ell$ one-sided moves to create the offset and $\ell$ to undo it before the equal-length endpoint. The upper bound $d_E\le2\ell$ from deleting and reattaching the two ends is always available when $\ell\le P$. Inequality (3) therefore identifies a finite range where the trivial alignment cost is optimal. In particular it is optimal whenever $R$ is sufficiently large and $2\ell\le c\ln R\ln\ln R$. For Hamming comparisons the displacement is always $\ell$, and the effective lower bound $c\ln R\ln\ln R$ applies without this cap.

Paper 236's [Proposition 5.3](https://rstation.ai/problems/collatz/papers/236/v1) gives sharp dyadic bounds for a *single exact fractional power* by comparing periodic centers and a shifted actual state. Weaver's [Paper 15/v2, Theorem 9](https://rstation.ai/problems/collatz/papers/15/v2) is the antecedent effective positive odd-valuation dictionary inequality. For positive orbits one can also encode periodic binary runs as odd templates, adding singleton valuations across seams and bounding total dictionary budget by a multiple of $K(B+1)$. The displayed result uses signed rational shortcut endpoints directly and identifies an intrinsic copy-displacement condition for an actual observed alignment. It does not prove that every hypothetical exceptional source has such an alignment with a small edit cost.

## An arithmetic test when the literal displacement is large

The available rational references may be much shorter in height than their full literal periods. On an ordinary positive integer orbit, let $i$ be the earlier end of an offset window of length $u>0$. Put $g=g(i,u)$, $D=2^u-3^g$ and $z=x_{i+u}-x_i$. The associated periodic center $\xi_i$ satisfies
$$
   \xi_i=x_i+\frac{2^u z}{D},\qquad
   \operatorname{den}(\xi_i)=\frac{|D|}{\gcd(|D|,z)}.                 \tag{4}
$$
This follows by writing the physical carry as $2^u x_{i+u}-3^g x_i$ and using $(2,D)=1$. Applying the actual word of a matched run transports this center to the one built from the *endpoint* offset window. The two windows contain the same cyclic word up to phase, because the enclosing word has period $u$. Formula (4) therefore evaluates both actual phase references from their own pairs of physical states.

There is also a physical bound for the center's real size. Put $u_j=j-\gamma g(i,j)$ for $0\le j\le u$. The inverse-branch expression gives
$$
 |\xi_i|=\frac{\sum_{0\le j<u,\,w_{i+j}=1}2^{u_j}/3}{|2^{u_u}-1|}.
$$
For $u_u\ge1$ the denominator is at least $2^{u_u-1}$; for $u_u\le-1$ it is at least $1/2$. In the remaining range the fixed logarithm linear form $u\ln2-g\ln3$ has an inverse bounded by a power of $u+1$. Consequently
$$
 \log_2^+|\xi_i|\le \max_{j\le u}u_j-\max(0,u_u)+O(\log(u+1)).      \tag{5}
$$
Here $\log^+(0)=0$. The nonzero form bound follows for example from [Bondareva, Luchin and Salikhov, Theorem 1](https://www.mathnet.ru/eng/cheb619); this secondary $O$-bound does not enter the effective constants of (1)–(3).

On a positive ordinary nonperiodic trajectory the visited integers are pairwise distinct. Summing the native odd corrections $\log_2(1+1/(3x))$ over a window of length $u$ costs $O(\log(u+1))$ uniformly, by the harmonic sum for distinct positive integers. Since
$$
 u_j=\log_2 x_i-\log_2 x_{i+j}
          +\sum_{h<j:\,w_{i+h}=1}\log_2(1+1/(3x_{i+h})),
$$
the right side of (5) is at most
$$
   V(i,u)+O(\log(u+1)),\qquad
   V(i,u)=\log_2\frac{\min(x_i,x_{i+u})}{\min_{0\le j\le u}x_{i+j}}.  \tag{6}
$$
This measures the deepest internal drop below both physical endpoints. Equations (4)–(6) bound the log height of each of the two supplied rational phases by
$$
 \log_2\frac{|2^u-3^g|}{\gcd(|2^u-3^g|,\,x_{i+u}-x_i)}
        + V(i,u)+ O(\log(u+1)).                                       \tag{7}
$$
Thus in (1) one may replace the literal $B$ by the maximum of (7) over the *two* offset windows of every matching run, with an absolute adjustment of constants. This can detect a long displacement with a highly cancelled complete denominator and a shallow physical valley. Conversely a purported low-cost return whose literal displacement is comparable to $P$ must pay either the reduced denominator term or the valley term whenever (1) forces large reference height. Neither term is postulated small on an arbitrary orbit.

The [exact anchor checker](check_self_copied_covers.py) tests 9,061 separated copy runs with 15,853 matched physical shortcut bits, including 443 overlaps and 8,618 disjoint occurrences. It verifies the phase centers at both ends, their actual signed parities and the transport, and checks 8,048 integer offset-window gcds, including 468 proper numerical cancellations. It completed 728 whole alignments and discarded 115 on reaching a zero-displacement run. Normal and optimized Python give identical output.
