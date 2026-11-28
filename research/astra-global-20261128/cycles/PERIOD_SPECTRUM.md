# How many distinct Collatz cycle periods can occupy any translated interval?

Let $T(x)=x/2$ on even numerators and $T(x)=(3x+1)/2$ on odd numerators, in reduced form with an odd positive denominator. Put
\[
 \alpha=\log_3 2,\qquad h=H_2(\alpha)=0.949955527\ldots .
\]
A cycle is primitive, its period is its least shortcut period, and the zero cycle is omitted. Let $P_D(I)$ count **distinct least period values in the interval $I$** realized by any positive or negative cycle of full reduced denominator at most $D$. Several cycles with the same period contribute one. The denominator is constant around a periodic orbit. All heights below are absolute real magnitudes.

## The period bound

Let $h<s<1$, let $D\ge1$ and put $K=D^{2h}$. Suppose $M>1$ and $c>0$ satisfy
\[
 |\alpha-a/q|\ge c q^{-M}
\]
for all reduced fractions $a/q$, $q\ge1$. For **every** interval $I$ of $N\ge2$ consecutive positive integer periods, uniformly in its location,
\[
 P_D(I)\ \ll_{s,c,M}\ K+
 K^{1/(1+s)}N^{s/(1+s)}
 + K^{1/(1+Ms)}N^{(M-1)s/(1+Ms)}.                    \tag{1}
\]
The trivial bound $N$ may be taken whenever it is smaller. All three powers concern genuine full denominators and arbitrary valuation words. For $D=1$ and $s=19/20$, three source choices give distinct consequences.

* Bondareva, Luchin and Salikhov, Theorem 1, give $|h_1\log 2+h_2\log 3+h|>H^{-4.116201}$ for all integer coefficients with $H=\max(|h_1|,|h_2|)$ sufficiently large. Put $(h_1,h_2,h)=(q,-a,0)$ and restrict to near approximants $|a|\le q$. Division by $q\log3$, and shrinking the implicit constant to include the finitely many small denominators, give $M=5.116201$. Consequently $\sup_H P_1([H,H+N))\ll N^{26069273/39069273}$, with exponent $0.66725769\ldots$. [Chebyshevskii Sbornik 19(1) (2018), 15–25, Theorem 1, printed p. 18](https://www.mathnet.ru/eng/cheb619)
* Lagarias's explicit Lemma 2.2(1) supplies $M=14.3$ and $c=1/1200$. Its last exponent is $2527/2917<0.867$. [Lagarias, Lemma 2.2(1)](https://arxiv.org/abs/math/0512006)
* Chudnovsky's October 2026 preprint states $\mu(\log 2/\log 3)\le3$, so it supplies (1) for every $M>3$. On its stated theorem the period count is
  \[
  \sup_H P_1([H,H+N))\ll_\varepsilon N^{38/77+\varepsilon},\qquad 38/77=0.49350649\ldots.       \tag{2}
  \]
  We checked the source's theorem statement and dependency declarations. Independent reconstruction of its two-torus argument and rebuild of its formalization lie outside this pass. [Chudnovsky, Theorem 11.1 and Appendix A](https://arxiv.org/html/2610.28079v1#S11)

For $D=N^d$ and any fixed $0\le d<1/(2h)$, (1) gives a uniform power saving relative to $N$. In particular it controls windows whose starting period can be arbitrarily larger than their length. The [earlier joint Farey census](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/cycles/phase8/FAREY_CENSUS.md) proved density one up to an endpoint with a logarithmic improvement by charging ordinary gaps and using irrational equidistribution. We retain its sharper endpoint statement. Our new ingredients are the fractional gap budget, the integer-line alternative in a translated strip and the cost of many distinct points on that line.

There is a structural conclusion with **no quantitative irrationality hypothesis**. When $K\le N$, after removing $O_s(K^{1/(1+s)}N^{s/(1+s)})$ period values from any interval, all remaining $(n,u)$ clock pairs can be selected on a single affine line in the integer lattice, where $u$ is the odd count and $n$ is least period. An empty remainder is allowed. For $I\subset[1,2N]$ we can include the origin in the strip and make this line pass through the origin, enlarging the absolute constant. In that case the periods of cycles with $\gcd(n,u)=1$ number $O_s(K^{1/(1+s)}N^{s/(1+s)})$, even without the logarithm-ratio input. In particular $D=1,s=19/20$ gives $O(N^{19/39})$ up to $N$ for those periods. Primitivity of the orbit does not imply coprimality of its clocks.

## Fractional gap budget for both signs

The main estimate is uniform in $D$. A set $E_D$ of at most $O_s(D^{2h})$ period values can be removed so that the sum over the remaining **cycles**, with multiplicities of period retained, satisfies
\[
       \sum_{\substack{C:\ d_C\le D\\ n_C\notin E_D}} g_C^s
         \ll_s D^{2h},\qquad g_C=|n_C\alpha-u_C| .                    \tag{3}
\]
For $D=1$, the sum over all cycles is finite, including the finitely many possible cycle minima below a fixed constant.

Choose $B=L=\lceil A_s(1+\log(2D))\rceil$ with $A_s$ a sufficiently large fixed number. On a cycle whose least magnitude is at least $L$, set $f_i=y_i^{-s}$. The complete log-product identity gives
\[
     g_C\ll \sum_{i:\,\mathrm{odd}} y_i^{-1},\qquad
     g_C^s\ll_s \sum_i f_i .
\]
Every odd correction before division by $\log3$ is $\log(1+1/(3y_i))$ on the positive side or $-\log(1-1/(3y_i))$ on the negative side. The latter is bounded by $1/y_i$ for $y_i\ge L\ge2$. The power uses $(u+v)^s\le u^s+v^s$ for $u,v\ge0$.

On the periodic index set take increments $Q_i=f_i+B(f_i-f_{i+1})$, extend the partial sums by $S_{i+1}-S_i=Q_i$, and put
\[
 d_i=\min_{j\ge i+1}S_j-\min_{j\ge i}S_j .
\]
The lap increment $\sum_i f_i$ is positive, so all these minima exist. Their differences are periodic, nonnegative and sum to $\sum_i f_i$ per lap. If $d_i>0$, then $S_i=\min_{j\ge i}S_j$, $d_i\le (B+1)f_i$, and
\[
 f_{i+j}\le f_i+B^{-1}\sum_{v=0}^{j-1} f_{i+v}\quad (j\ge1).
\]
Induction gives $f_{i+j}\le f_i(1+B^{-1})^j$. Starting at this charged phase, if $u_j$ counts odd departures through time $j$, the upper physical growth bound on either sign gives
\[
 u_j\ \ge\ a j,\qquad a=\frac{\log2-s^{-1}\log(1+B^{-1})}{\log(3+L^{-1})}.
\]
Use $3/5\le a\le\alpha$ and $H_2(a)\le(h+s)/2<s$, ensured by the choice of $A_s$. We also have $H_2(a)-h=O_s(1/B)$.

For a fixed sign, two different phases of denominator at most $D$ in an interval of width $X$ which share $t$ parity bits have a nonzero integer cross difference divisible by $2^t$ and of magnitude at most $D^2X$. Taking $t=\lfloor\log_2(D^2X)\rfloor+1$ allows one such phase per word. The crude final-count binomial bound for $u_t\ge at$ bounds the number of charged phases by $O((D^2X)^{H_2(a)})$. To absorb the slowly growing $B$, use the uniform all-prefix estimate from [PR211, endpoint census, (2)](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/cycles/phase8/ENDPOINT_CENSUS.md), which supplies the additional factor $(1+t)^{-3/2}$ on this compact slope range. Summing $(B+1)X^{-s}$ times this count on $X=2^jL$ gives
\[
 \sum_{C:\,d_C\le D,\,\min y_i\ge L}g_C^s
  \ll_s D^{2h}(1+\log(2D))^{h-s-1/2}\ll_s K .
\]
The dyadic series is uniform because $H_2(a)\le(h+s)/2$. Passing through finite collections first justifies the sum when the collection of cycles is infinite. This use of future-minimum charges follows the architecture of [Paper 217](https://rstation.ai/problems/collatz/papers/217/v1). Its source theorem bounds the first gap moment for ordinary positive cycles.

A low-minimum cycle with $n\ge D^{20/11}$ has maximum at least $n/D$ by its distinct integer numerators. For large $D$, this far exceeds $2L$. The last crossing above $L$ before that maximum gives $z\in[L,2L]$. From $z$ via the peak to the last state before the next downward crossing, the elapsed time is at least $(8/3)\log_2(n/(2LD))$, by the whole-excursion proof of the earlier joint Farey census. This is at least $\lfloor\log_2(2LD^2)\rfloor+1$ for large $D$, since $(8/3)(20/11-1)=24/11>2$. Through those $t$ bits every prefix has odd count at least $(j-1)\log2/\log(3+1/L)$. The same ballot count and simultaneous separation give $O_s(D^{2h}(1+\log(2D))^{h-3/2})$ possibilities for $z$ on either sign. Each witness belongs to a single cycle. Shorter periods yield at most $D^{20/11}\ll K$ distinct values since $2h>20/11$. Bounded $D$ can be absorbed directly because each reduced low minimum then lies in a fixed finite set. These period values form $E_D$.

## Integer lines in a translated thin strip

A finite set of lattice points with distinct first coordinates in an interval of length $N$, and whose second coordinates satisfy $|n\alpha-u|\le e$, either lies on one affine line or has at most $1+12Ne$ points. Choose a line carrying the largest number $J\ge2$ of points and take its primitive direction $(q,a)$. Distinct periods ensure $q\ne0$, so choose $q>0$. Consecutive lattice points on the line differ by integer multiples of the primitive direction. Hence
\[
 (J-1)q\le N,\qquad (J-1)|q\alpha-a|\le2e .
\]
The integer $qu-an=q(u-n\alpha)+n(q\alpha-a)$ has range at most $2eq+N|q\alpha-a|\le4Ne/(J-1)$. Its level sets are parallel lines with at most $J$ points. If at least two lines occur, the integer range is at least one and $J\le1+4Ne$. The total is then at most $J(1+4Ne/(J-1))\le1+12Ne$. Vertical lines only matter when periods are repeated, which is why this passage counts distinct periods.

Remove $E_D$. For each realized period select one cycle and its pair $(n,u)$. The number with $g_C>e$ is $O_s(Ke^{-s})$ by (3). If $K\le N$, choose $e=(K/N)^{1/(1+s)}$. The large-gap count and $Ne$ both have order $K^{1/(1+s)}N^{s/(1+s)}$. The same reasoning applies when counting only periods with a coprime representative, by selecting that representative before discarding large gaps.

On the surviving affine line, signed errors differ by integer multiples of $\Delta=|q\alpha-a|>0$. Among $\Delta$-separated real numbers, the $i$-th smallest absolute value is at least $(i-1)\Delta/2$, since an interval of radius $r$ contains at most $1+2r/\Delta$ points. Hence $J\ge4$ selected points spend at least $c_s\Delta^s J^{1+s}$ in (3). Consequently
\[
 J\ll_s 1+\min\!\left\{N/q,\ K^{1/(1+s)}\Delta^{-s/(1+s)}\right\}.
\]
Use $\Delta\ge c q^{1-M}$ and balance the two terms, or take their weighted geometric mean with the powers of $q$ cancelled. This gives the last term of (1). For $K>N$ the trivial count is at most $K$. The proof requires no coprimality of the least-period clock pair and no bound on the period location. A single isolated ordinary cycle is still consistent with every conclusion above.


## Verification scope

The [companion Lean file](PeriodSpectrum.lean) checks four kernels over every linearly ordered field for determinant range, scaled determinant span, noncollinear occupancy and affine error spacing. The ballot estimate, dynamical moment, lattice-line selection and Diophantine specializations use the written arguments above.

The Python control enumerates all primitive signed rational words through physical period 11 and checks native parity, period, charges and every charged prefix for rational test potentials. It also compares the line and area inequalities against exact rational strips with starting coordinates as large as $10^{12}+315$. Its JSON records the exact coverage. [Checker](check_period_spectrum.py) · [Recorded control](../../../reports/astra-global-20261128/cycles/PERIOD_SPECTRUM.json)
