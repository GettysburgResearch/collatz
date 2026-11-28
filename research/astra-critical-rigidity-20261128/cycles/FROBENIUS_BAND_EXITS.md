# Polynomially many distinct phases outside every sub-four band

**Proposed written theorem.** Let an ordinary positive Collatz cycle have primitive odd period \(p\), odd minimum \(m\), odd maximum \(X\), native division sum \(A\), and reduced clock denominator \(P=p/\gcd(A,p)\). Put \(\gamma=\log_2 3\). Use the mixed binary rate and the physical residence exponent
\[
 \theta=0.3197044778974\ldots,\quad
 a=1-3\theta=0.0408865663076\ldots,\qquad
 v=0.4333973955184\ldots .
\]
The exact definitions are given in the [chain entropy proof](GLOBAL_DYADIC_PAIR_ABUNDANCE.md) and [Weaver 145/v1, (2), Theorem 6](https://rstation.ai/problems/collatz/papers/145/v1), respectively. The final numerical conclusions use the stated [irrationality exponent input](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md) \(\mu(\gamma)\le3\). Equation (5) below is independent of this input.

* For **unrestricted excursions**, fix \(2<R_0<4\) and count the distinct odd phases \(k=\#\{x:x>R_0m\}\). Along every sequence with \(p\to\infty\),
\[
      \liminf\frac{\log(1+k)}{\log p}\ \ge         \min\{a/(4v),a/(1+2a)\}=0.02358491694\ldots .                \tag{1}
\]
  The same estimate with lower bound
  \(\min\{(a/v-3\kappa)/4,(a-\kappa)/(1+2a)\}\) holds for the moving cutoff \(x>(4-p^{-\kappa})m\), \(0<\kappa<a/(3v)\).

* For **bounded total width**, suppose \(X/m\le R_1\) with \(R_1<\infty\) fixed. Take any moving band \([M,R_0 M]\) meeting the cycle, and count all \(k\) actual phases outside it. In the fixed-cutoff assertion the lower bound improves to \(\min\{a/(3v),a/(1+a)\}\). When \(R_1<9\), it improves further to
\[
                \liminf\frac{\log(1+k)}{\log p}\ge a.                 \tag{2}
\]
  The intervals for the moving-cutoff assertion are \([M,(4-p^{-\kappa})M]\). The two bounds then become \(\min\{(a/v-3\kappa)/3,(a-\kappa)/(1+a)\}\) and \(b_\kappa=\min\{(a/v-3\kappa)/2,a-\kappa\}\), respectively. All positive statements hold over the stated range of \(\kappa\).

In particular if \(X/m\to4\), for each fixed \(\epsilon>0\) there are \(p^{a-o(1)}\) or more **distinct** phases in each of \([m,(1+\epsilon)m]\) and \([(4-\epsilon)m,X]\). If \(X/m=4+O(p^{-\kappa})\), the endpoint layers of relative thickness \(O(p^{-\kappa})\) each contain at least \(p^{b_\kappa-o(1)}\) phases. Every choice of one phase from each layer then has ratio \(4+O(p^{-\kappa})\). This gives both a matching of that size and at least \(p^{2b_\kappa-o(1)}\) **different physical pairs** with that precision. For the lower layer use \(M=X/(4-p^{-\kappa})\); its complement on the cycle consists exactly of the low phases. For the upper layer use the band starting at \(m\). These conclusions concern a single genuine ordinary cycle. No cycle with the prescribed width is asserted to exist.

## Reduction to a long interval of true in-band states

Write \(R=R_0\) or \(R=4-p^{-\kappa}\); put \(\kappa=0\) in exponent estimates in the fixed band. For (1) take \(M=m\), for the other conclusions \(M\asymp_{R_1}m\) whenever the band meets the cycle. Pass to a subsequence with limits
\[
 \beta=\lim\log(1+k)/\log p,\quad \pi=\lim\log P/\log p,
 \qquad \sigma=\lim\log m/\log p .
\]
The native log identity gives \(0<A/p-\gamma\le 1/(3m\ln2)\). Any finite bound on the irrationality exponent, for instance the [BLS two-log estimate](https://doi.org/10.22405/2226-8383-2018-19-1-15-25), implies \(m\le p^{O(1)}\). The below conclusions are automatic for \(\beta\ge0.1\), so take \(\beta<0.1\).

Paper 145, Theorem 6 applies to one lap of distinct states and the integer band \([\lceil M\rceil,\lfloor RM\rfloor]\), whose upper endpoint is strictly below four times its lower endpoint. There are at most \(k\) observed exits and \(p-k\) visits. Its uniform bound, valid also as the width approaches four, gives for every \(v'>v\)
\[
                     p-k\ll_{v'} M^{v'}+k\log(2M),\qquad
                     \sigma\ge 1/v>2.30.                              \tag{3}
\]
The largest cyclic run of consecutive in-band states has length at least \((p-k)/(k+1)\). Work inside such a run with length parameter \(T=\lfloor p/(10(k+1))\rfloor\). There is room for a full interval of length \(4T\) and all the shifts used below, including when \(k=0\) by taking one lap. Thus \(\log T/\log p\to1-\beta\).

The [complete ordinary inversion theorem](RESIDUE_FIBER_INVERSIONS.md) gives \(g-1\le I\) for \(g=p/P\). Each inversion is given by actual states \(y=2^d x+u\), \(d\ge3\), \(0<3u<2^d-1\), with \(u\) an odd integer. In (1) the larger state is exceptional. For fixed \(y,d\), the interval for \(x\) has length less than \(1/3\) and contains at most one integer. There are \(O(1+\log(X/m))\) possible \(d\) per such \(y\). Each odd native step raises a positive ordinary state by a factor at most two. Starting at the last in-band state before the maximum bounds \(X/m\le 4\cdot 2^k\). Hence \(g\ll (k+1)^2\). For bounded total width every inversion has an endpoint outside the chosen band. Each fixed endpoint and allowable \(d\) admits \(O_{R_1}(1)\) partners by the same displayed formula and \(2^d\le R_1\). Thus \(g\ll_{R_1} k+1\). For \(R_1<9\) there are no ordinary inversions by the cited theorem, including its forced forward phase on the first possible inversion, so \(g=1\). We have obtained \(1-\pi\le c\beta\) with \(c=2,1,0\) in the three cases.

## A pair collision yields two dilated equalities on the same true interval

Set \(B=A/g\). Choose \(1\le\tau\le P\) with \(\tau B=t_0P+1\). Use spatial offsets \(0\le j\le W=\lfloor P p^{-\kappa}/(\log p)^5\rfloor\); the preceding inequalities imply \(W\to\infty\). Divide the circle of \(p\) native dates into \(O(1+p/T)\) arcs of length at most \(T/1000\). One arc contains at least \(c_0(W+1)T/p\) of the dates \(j\tau\bmod p\), counted with their offsets. Subtract the smallest *spatial* offset in that cell from all its offsets. Call the resulting set \(J\subset[0,W]\). Every \(j\in J\) has a signed true-time representative \(s_j\equiv j\tau\pmod p\) with \(|s_j|\le T/1000\). The times are distinct since \(\tau\) is prime to \(P\) and \(W<P\). In particular
\[
                       |J|\ge p^{\pi-\kappa-\beta-o(1)}.             \tag{4}
\]

Extend the physical integer trajectory periodically to all native dates, put \(E_{t+1}-E_t=v_2(3x_t+1)\), and define \(V_t=2^{E_t}x_t, U_t=2^{E_t}\), so \(V_{t+1}=3V_t+U_t\). For the shift operator \(D=2^{-t_0}\operatorname{shift}^{\tau}\) set
\[
     Z_{t,j}=2^{-F_t}D^jV_t,\qquad C_{t,j}=2^{-F_t}D^jU_t,\qquad
     F_t=\lfloor\log_2(V_t/L)\rfloor,\qquad L=M(1+R/4).
\]
The notation \(D^jV_t\) means \((D^jV)(t)\); either sign of the absolute date is allowed. Here \(RM/2<L<2M\). The distance from either endpoint of this strict interval is \(M(4-R)/4\). The log of \(Z_{t,j}/(2^{-F_t}V_t)\) is \(j/P+O(T/m)\) in base two. Indeed \(log_2V_t-tA/p\) is periodic of period \(p\) and each of its differences has absolute value \(O(1/m)\). The reduced-clock identity gives the term \(j/P\), while the signed representative \(s_j\) bounds the de-meaned error. The same statement with \(j\) replaced by any sum of at most eleven offsets from \(J\) holds with the same order of error. Both its spatial size \(11W/P\) and \(T/m\) are \(o(4-R)\), by (3). At every date being used where all these physical time shifts stay in the band, \(C_{t,j}\) is a power of two strictly between \(1/2\) and (4), hence is one or two. The normalized labels \(Z_{t,j}=C_{t,j}x_{t+j\tau}\) are positive integers of order \(M\). This reasoning does not use the values of remote high excursions or any global sorted chart.

Choose a native anchor deep enough inside the run to have \(T\) preceding dates and \(T\) following dates, with the same margin for the shifts above. Suppose a signed comparison \(Q(D)\), where \(Q(X)=X^i+X^j-X^u-X^v\) on four offsets in \(J\) with repetitions allowed, has zero normalized label at the anchor. For its integer normalized height \(H_t=2^{-F_t}(Q(D)V)(t)\) the forcing \(2^{-F_t}(Q(D)U)(t)\) is between \(-2\) and 2. The exact recurrence \(2^{F_{t+1}-F_t}H_{t+1}=3H_t+2^{-F_t}(Q(D)U)(t)\) implies \(H_{t+1}=0\Rightarrow H_t=0\). Thus \(Q(D)U\) also vanishes throughout the preceding \(T-1\) dates. All zeros of the unnormalized sequences repeat modulo \(p\), since translation by \(p\) scales both \(V,U\) by \(2^A\).

On the middle third of this preceding interval, \(Q(D)^{11}U=0\). Indeed, apply the remaining ten copies of \(Q(D)\) to the zero interval. The needed native time shifts have signed total at most \(10T/1000\). In the group ring over \(\mathbb Z[1/2]\) reduced modulo 11, the freshman's dream gives
\[
                         Q(D)^{11}\equiv Q(D^{11})\pmod {11}.
\]
Multiplication by \(2^{-F_t}\) is a unit modulo 11. The normalized value of \(Q(D^{11})U\) is an integer of absolute value at most eight, since each single dilated tag lies in \({1,2}\). Therefore \(Q(D^{11})U=0\) exactly on that middle third. The corresponding normalized label comparison satisfies the homogeneous recurrence there. Across \(l\) consecutive such dates its initial integer is divisible by \(2^{F_{t+l}-F_t}\) because the odd multiplier is \(3^l\). The winding satisfies \(F_{t+l}-F_t\ge l\gamma-1\), whereas the integer has magnitude \(O(M)\). Taking \(l\gg\log(2M)\) gives zero for the dilated label comparison at an interior date. The original label comparison is already zero on that date.

## Counting the possible equalities and applying the physical code bound

Write \(z=2^{1/P}\). At this common date the shape estimate gives \(|Q(z)|+|Q(z^{11})|\ll T/m\). The original normalized labels increase strictly with \(j\in J\), because each adjacent spatial step has relative size at least \(c/P\) and \(T/m=o(1/P)\) by (3). Different unordered pairs with equal sum must therefore be nested, allowing a doubled inner point. After translating the four spatial indices their order is \(0<u\le v'<v'+w\); write \(v'=b, u=d, w=f\) in the rest of this paragraph. Up to an overall sign and a harmless factor of \(z^i\), their polynomial is \(z^b(z^f-1)-(z^d-1)\). Subtract its value at \(z\) times \(1+z^d+\cdots+z^{10d}\) from its value at \(z^{11}\). The difference is
\[
 z^b(z^f-1)\left[z^{10b}\sum_{h=0}^{10}z^{hf}
                     -\sum_{h=0}^{10}z^{hd}\right]
                   \ \ge\ (z^f-1)(z^{10b}-1).
\]
For \(h\ge1\) the termwise comparison uses \(d\le b\); the \(h=0\) difference gives the displayed lower bound. All powers occurring are uniformly bounded since \(11W/P=o(1)\). Consequently \(bf\ll P^2T/m\). The original equality estimate also gives \(|z^d-z^f|\ll T/m+(z^b-1)(z^f-1)\ll T/m\), hence \(|d-f|\ll PT/m=o(1)\). Thus \(d=f\) exactly: each nontrivial collision at the anchor is an actual *rank rectangle* of positive sides \(d,b\) with \(db\le E=C P^2T/m\). Coincident inner points are exactly \(d=b\).

For each smallest rank in \(J\) there are \(O(E\log(2+E))\) four-distinct candidate rectangles and \(O(\sqrt E)\) three-distinct candidates; there are none if \(E<1\). Include each vertex independently with probability \(c_1(1+E\log(2+E))^{-1/3}\). Delete one vertex from each retained candidate. For \(c_1>0\) an absolute sufficiently small constant, the expected deletions of each kind together cost at most half the expected retained population. For the three-vertex contribution this uses \(\sqrt E/(1+E\log(2+E))^{2/3}=O(1)\). At least one resulting \(S\subset J\) therefore has cardinality \(\gg |J|(1+E\log(2+E))^{-1/3}\). Its true integer label sums at the anchor distinguish all unordered pairs, including repetitions.

Encode \(S\) by its actual binary tags on \(n=\lceil\log_3(32M)\rceil+3\) native dates after the anchor. If two pair words have equal component sums, their initial integer label difference is divisible by \(2^{F_{t+n}-F_t}\), which exceeds its magnitude. The label sums are then equal and identify their pair. The resulting Sidon code obeys the [native chain entropy bound, (3)–(4)](GLOBAL_DYADIC_PAIR_ABUNDANCE.md). Indeed its true division exponents \(h_t+\log_2 C_{t+1,j}-\log_2 C_{t,j}\ge1\) with \(h_t=F_{t+1}-F_t\) give the required monotone or pinned rows, and \(sum h_t=n\gamma+O(1+n/m)\). Thus \(log_2|S|\le(\gamma\theta+o(1))n\). Taking exponents proves
\[
       \pi-\kappa-\beta-\tfrac13(2\pi+1-\beta-\sigma)_+
                          \ \le\ \theta\sigma .                          \tag{5}
\]
The classical finite irrationality measure is sufficient for the logarithmic coding deadline to fit in the genuine tube. The bounded-alphabet prime dilation is the argument of [Kari and Szabados, Lemma 2](https://www.utupub.fi/server/api/core/bitstreams/044d03b6-542b-4711-9f99-0b00140db926/content), applied here on a finite common native interval with a dyadic weighted shift. The prime-11 dilation is applied to the bounded actual integer tags, then transferred back to the ordinary states by the full native affine identity. No bound on the unnormalized dyadic polynomial coefficients enters the congruence.

## Elimination and comparison with previous results

If \(2\pi+1-\beta-\sigma\ge0\), (5) yields \(a\sigma\le 1-\pi+3\kappa+2\beta\le(c+2)\beta+3\kappa\). Thus (3) gives \(\beta\ge(a/v-3\kappa)/(c+2)\). In the other branch \(\pi-\kappa-\beta\le\theta\sigma\). Under the log-ratio input the reduced true clock gives \(\sigma\le3\pi\); hence \(\beta\ge(a-\kappa)/(1+ca)\). These are precisely the asserted exponents.

The preceding [near-dyadic pair theorem](GLOBAL_DYADIC_PAIR_ABUNDANCE.md) allows many pairs sharing a phase. Here even one exceptionally long excursion above the band must visit polynomially many *different* odd phases above its upper cutoff. The bounded-width two-sided conclusion applies to arbitrary placements of the band. Weaver's prior physical residence estimate supplies (3) and allows the alternative of an unusually large minimum. The dilated two-equality and hereditary subcode argument restrict that remaining alternative. The result leaves open cycles with the required number of outliers, including a majority of their dates inside a sub-four band. Weaver's earlier positive-density occupation theorem uses the shortcut clock and thresholds below \(3.84904\) times the minimum. A high shortcut departure in that theorem can be an even phase following an odd value; its fraction does not directly count odd states near four times their minimum. [Weaver 181/v1, map conventions and asymptotic occupation](https://rstation.ai/problems/collatz/papers/181/v1)
