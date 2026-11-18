# Ordinary orbits leave every finite collection of deep rational ternary neighborhoods

**PROPOSED.** Fix a nonempty finite set \(F\) of rational ternary units. There is an effectively computable \(C_F\) with the following property. Starting at any sufficiently large positive odd integer \(x\), among the first \(\log_2(x+1)+O_F(1)\) odd steps, including the start, there is a state \(y\) satisfying
\[
        \max_{r\in F} v_3(y-r)\le C_F\log(2+\log x).                  \tag{1}
\]
Here \(v_3(0)=+\infty\). Both negative rational cycles and their positive rational forward images can be included in \(F\). The theorem concerns an actual single ordinary orbit. It allows visits of much greater precision at other times.

Let \(H\) be the largest absolute numerator or denominator of the reduced elements of \(F\), enlarged to at least two. Put \(m=1+\lceil\log_2((x+1)H^2)\rceil\), \(y_i=U^i(x)\) and \(a_i=v_2(3y_i+1)\). As \(y_i+1\le(3/2)^i(x+1)\), all \(a_i\ll_F 1+\log x\) on this interval. For every ordered pair \(r,s\in F\), whenever \(2^a s\ne3r+1\), Yu's rational \(p\)-adic logarithm bound yields
\[
               v_3(2^a s-(3r+1))\ll_F\log(2+a).                     \tag{2}
\]
Apply it at \(p=3\) to \(2^a[s/(3r+1)]-1\). Both rational bases are ternary units. Since \(3r+1\) is a ternary unit, its removed factor does not change the valuation. The bound allows multiplicatively dependent bases provided the product being compared is different from one. The two-base constant can be maximized over the given finite set. [Yu's bound in rational form, Evertse, Theorem 1.10](https://www.math.leidenuniv.nl/~evertsejh/dio2011-linforms.pdf) · [Yu, p-adic logarithmic forms](https://doi.org/10.1515/forum.2007.009)

Suppose every \(y_i\), \(0\le i\le m\), were closer than (1) allows to some \(r_i\in F\). The equation \(2^{a_i}y_{i+1}=3y_i+1\) gives the same high divisibility at \(2^{a_i}r_{i+1}-(3r_i+1)\). By (2) this difference must be zero at every step. The two exactly parallel rational trajectories then satisfy
\[
             y_m-r_m=3^m2^{-A_m}(x-r_0),\qquad A_m=\sum_{i<m}a_i.
\]
The starting difference is nonzero for \(x>H\) and has binary valuation at most \(\log_2((x+1)H)\), by clearing the denominator. The ending difference has binary valuation at least \(-\log_2 H\), since \(y_m\) is ordinary. Hence \(A_m\le\log_2((x+1)H^2)<m\), contradicting \(a_i\ge1\). This proves (1). For \(F=\{-1\}\) the local estimate needs only lifting the exponent in \(2^a-2\).

## What this removes from the escape test

Suppose an escaping ordinary orbit carries a nonnegative statistic \(K(y)\ge c\log y\) at every sufficiently late state, for a fixed \(c>0\). It then has a sequence of states \(t_k\to\infty\) with the same lower bound and
\[
                v_3(t_k-r)=o(\log t_k)\quad
                \text{for every fixed rational ternary unit }r.       \tag{3}
\]
Indeed list the countably many rationals and apply (1) to successively larger finite initial sets. Start each interval at an arbitrarily large minimum of a forward tail of the orbit, so all the subsequent states in the interval are at least the starting value. The minima tend to infinity on an escaping positive orbit. The starting value can be chosen large enough that the upper bound in (1) is at most \((\log x)/k\).

For the canonical unnormalized inverse real fibre \(G_y\) (normalized to have total mass \(\lim_q g_q(y)\)), take \(K(y)=\int(1+B)^{-1}G_y(dB)\). The compact side branches of an escaping orbit give the required positive logarithmic lower bound. To see the mechanism, start at a fixed odd unit on that spine and write its successive states as \(y_i\). For every \(i<j\), use a unit sibling \(s_i=4y_i+1\) or \(16y_i+5\) with the same next state and retain its uniform positive reservoir at bounded real offset. These are disjoint first departures on reversed paths from \(y_j\), since later reversal along the original spine is prescribed. Along the remaining segment the homogeneous multiplier is comparable to \(y_j/y_i\) by the simple-orbit reciprocal bound. Its inherited offset is at most a constant times \(y_j\sum_{k=i}^j 1/y_k\) by the positive affine product identity. Consequently the \(i\)-th reservoir contributes at least a fixed multiple of \((1/y_i)/(\sum_{k=i}^j 1/y_k)\) to \(K(y_j)\). The adjacent suffix sums have bounded ratios since \(y_{i+1}\le(3y_i+1)/2\). Summing this lower bound is therefore comparable from below to the logarithm of the ratio between the first and last suffix sums, at least \(\log y_j-O(1)\). [Bounded-offset reservoir](../terminal-residue/ENDPOINT_ODOMETER.md) · [Simple-orbit distortion](../integrated/orbitwise-boundaries/README.md)

For comparison, \(K(t)\) can have logarithmic size on ordinary integers \(t=2\cdot3^k-1\). The long initial reverse sequence of ones admits a distinct unit departure at each of its first \(k-O(1)\) levels. Its multiplier and inherited real offset are both comparable to \((3/2)^i\), so the bounded reservoir at each departure contributes at least a constant to \(K(t)\). Property (3) excludes this example and every analogous polynomially precise approach to a fixed rational phase on the required sequence. A proof that \(K(t_k)=o(\log t_k)\) for every sequence satisfying (3) would exclude escape. It would still leave positive cycles to classify.
