# Local full rank of chronological windows on a single cycle

On an ordered three-band ordinary cycle, fix a fundamental starting rank \(0\le a<p\). Write \(p\) for the odd period, \(h\) for its total dyadic clock and \(\gamma=h/p\), with \(\gcd(h,p)=1\). The folded labels \(Z_r\) have lowbits \(c_r\in\{1,2,4\}\), and \(Z_{r+p}=2Z_r,\ c_{r+p}=2c_r\). Let \(X\) denote either \(Z\) or \(c\). The same result holds on an ordered rational cycle if \(Z_r/c_r\) has odd numerator and odd denominator at every fundamental rank. [Ordinary rank normalization](../../astra-unconventional-20261126/arithmetic/README.md)

For \(1\le m<p\), set
\[
 \delta_m=\min_{1\le d\le m}\|d\gamma\|_{\mathbb R/\mathbb Z}>0,\qquad
 L_m=2m\lceil3/\delta_m\rceil+1.
\]
For every \(L\ge L_m\), the rational Hankel matrix
\[
                   \bigl(X_{a+(i+j)h}\bigr)_{0\le i<L,\ 0\le j\le m}
\]
has full column rank \(m+1\). The bound is independent of the sizes and prime divisors of the coefficients in a proposed linear dependence. In particular every fixed nonzero rational combination of these \(m+1\) translates is nonzero at least \(p/L_m\) times among the \(p\) cyclic starting phases.

The unwrapped entries in this assertion are essential. Equivalently, multiply row \(i\) by \(2^{-\lfloor(a+ih)/p\rfloor}\) and column \(j\) by \(2^{-\lfloor jh/p\rfloor}\). The new entry is the fundamental value at \((a+(i+j)h)\bmod p\), doubled precisely when \(((a+ih)\bmod p)+(jh\bmod p)\ge p\). These nonzero row and column factors preserve rank. A matrix that discards the doubled entries need not satisfy this argument.

## Descent of the two-adic order

Let \(\xi_i=X_{a+ih}\). Its two-adic order has the form
\[
 v_2(\xi_i)=\lfloor(a+ih)/p\rfloor+t_i,\qquad t_i\in\{0,1,2\}.
\]
Consequently \(u_i=v_2(\xi_i)-i\gamma\) belongs to the interval \((a/p-1,a/p+2]\), of width three. This holds through every seam and after arbitrarily many laps.

Suppose nonzero rational coefficients \(q_j\) on some subset of \(\{0,\ldots,m\}\) give \(\sum_jq_j\xi_{i+j}=0\) at each of \(L\) consecutive rows. A singleton support is impossible because every \(\xi_i\) is positive. For the remaining supports let \(j_*\) minimize \(w_j=v_2(q_j)+j\gamma\). Each \(v_2(q_j)\) is an integer. Thus distinct weights differ by at least \(\delta_m\), and the minimum is unique.

At a vanishing row \(i\), some \(j\ne j_*\) has \(v_2(q_j\xi_{i+j})\le v_2(q_{j_*}\xi_{i+j_*})\), since a sum with a unique term of strictly least two-adic order is nonzero. Cancel \(i\gamma\) to get
\[
             u_{i+j}\le u_{i+j_*}-(w_j-w_{j_*})
                       \le u_{i+j_*}-\delta_m .                     \tag{1}
\]
The lattice site moves by at most \(m\) in either direction. The eligible sites \(i+j_*\) form an interval of \(L\) consecutive integers. Start in its middle. For \(L\ge L_m\), there is room to apply (1) successively \(\lceil3/\delta_m\rceil\) times. This would decrease \(u_i\) by at least three, contrary to its half-open range. Hence no proposed dependence can hold on the indicated window. The zero pattern of a translated combination repeats after \(p\) times, up to multiplication by \(2^h\); counting its gaps gives the cyclic nonzero count.

For a growing bounded ordinary candidate the positive lap product gives \(0<\gamma-\log_2 3\ll1/s\), where \(s\) is the minimum. A finite two-logarithm estimate \(\|d\log_2 3\|\ge c d^{-D}\) implies \(\delta_m\ge c m^{-D}-O(m/s)\). Since distinct odd states in the bounded physical band give \(s\gg p\), any fixed power of \(\log p\) is an admissible range for \(m\), with \(L_m=O(m^{D+1})\). In particular the local window can be much shorter than a lap. The finite rational-rank statement with its displayed \(L_m\) has no transcendence hypothesis. [Two-logarithm source](https://doi.org/10.1070/IM2000v064n06ABEH000314)

The [positive division relation](RANK_DIVISION.md) can take the same small value at many separated origins. This theorem excludes a fixed homogeneous relation on a whole succession of origins of the specified length. Full local rank alone supplies no lower bound on the real sizes of the minors that would exclude an integer cycle.
