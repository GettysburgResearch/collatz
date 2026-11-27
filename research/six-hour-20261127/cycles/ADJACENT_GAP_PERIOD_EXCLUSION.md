# Ordinary canonical-height-one periods exceed ten to the thousandth power

Let $P$ be the least odd period of an ordinary positive Collatz cycle, $A$ its valuation sum, $X$ its largest odd phase, $s$ its least odd phase and $\theta=A/P$. Write $E_i$ for the prefix valuation sum at the $i$th odd departure. Suppose the range of $E_i-i\theta$ is less than two. All positive accelerated valuations are allowed. In particular the theorem includes valuation three.

**Finite theorem.** If $s\ge2^{71}$ then $P>10^{1000}$. Bařina's published trajectory verification below $2^{71}$ supplies this floor for every nontrivial ordinary cycle. Shortcut and odd-accelerated steps contract portions of the same positive ordinary trajectory, so the basin of one is the same. The finite theorem with its floor hypothesis uses rational arithmetic and the written rank proof below. It does not invoke an irrationality-exponent estimate or the Subspace Theorem.

**Asymptotic theorem.** Along growing ordinary cycles in this width class,
$$
 \liminf\frac{\log X}{\log P}\ \ge 1+\frac{\log3}{\log3+(2-\log_2 3)\log(7/9)}=2.1049020798\ldots .
$$
For this elementary source-count argument strict convexity can use the classical 2018 finite irrationality exponent as in the companion note. Weaver 145's integral Subspace Theorem estimate already gives the stronger numerical exponent $16/7$ for this whole class. The new elementary drift census is effective in the finite application. Neither result excludes ordinary cycles of arbitrary period.

## Sorted gap spans and seven allowed pairs

At a maximizing cut the canonical grade is $z_i=\lfloor i\theta\rfloor-E_i\in\{0,1\}$, $z_0=0$. Put $k=A-P$, $r=ik\bmod P$, $L_r=2^{1-z_i}x_i$ and $\ell_r=2^{1-z_i}=\operatorname{lowbit}(L_r)$. Same-phase order implies $\gcd(A,P)=1$, as in STRICT_CONVEX_RANKS.md. Assume for now that $3/2<\theta<2$ and the strict rank convexity of that note holds. On extending $L_{r+P}=2L_r$ write $g_r=L_{r+1}-L_r$. The $P$ positive integers $g_r$ increase strictly, $g_P=2g_0$, and $\sum_{r<P}g_r=L_0$. Therefore
$$
 P\le g_0\le L_0/P,\qquad
 L_0\ge(3P^2-P)/2,\qquad g_0\le g_r<2g_0 .
$$

Fix a horizon $b\ge2$. A directed b-window considered at terminal rank $r$ follows the backward rank list $r-jk\bmod P$, $0\le j\le b$. Discard every terminal whose list meets $P-1$; this removes at most $b+1$ ranks. For the other windows the adjacent pair at each visited rank lies inside one fundamental octave. At each transition the two ranks have a common mechanical letter $m$: a divisor change between adjacent source ranks would put the lower destination at $P-1$, which was also excluded. Thus forward subtraction gives
$$
 2^m g_{\rm next}=3g_{\rm now}+\delta,\qquad
 \delta=\ell_{r+1}-\ell_r\in\{-1,0,1\}
$$
at each of the b chronological source dates. The full chronological drift and mechanical word determine the terminal gap modulo $3^b$ by iterating and inverting the total power of two. At a mechanical one, positivity of $e_i=m_i+z_i-z_{i+1}$ implies that each of the two lowbits is nondecreasing. The drift pair across that edge cannot be $(1,-1)$ or $(-1,1)$. Seven of the nine ordered pairs remain. No two mechanical ones are consecutive, since $k/P>1/2$. Among the first $b-1$ edges their number is at least $w=\lfloor(2-\theta)(b-1)\rfloor$, by telescoping the mechanical floor increments. The number of drift words for one calendar is at most $3^b(7/9)^w$.

As the terminal rank ranges in increasing order across the fundamental octave, the entire past b-letter schedule is constant on at most $b+1$ intervals. The only interior boundaries are the residues $jk\bmod P$, $1\le j\le b$. Equivalently take differences of the functions $\lfloor r/P-jk/P\rfloor$ for $j=0,\ldots,b$; these floors are right-continuous and an exact cut belongs to its right-hand interval. The ordering of actual terminal gaps makes their span on each such interval an ordinary integer interval as well, possibly with missing interior values. The sum of its span lengths over the disjoint rank cells is at most $g_{P-1}-g_0<g_0$. Removing the seam terminals never increases the bound, even if it leaves holes inside some cells. For a cell of span length $V$, a permitted terminal residue occurs on at most $1+V/3^b$ of its distinct integer gaps. Summing gives the finite inequality
$$
 P\ \le\ b+1+\bigl(g_0+(b+1)3^b\bigr)(7/9)^{\lfloor(2-\theta)(b-1)\rfloor}. \tag{1}
$$
In particular one pays for the total gap span once. No distribution assumption about gaps across the cells is used.

For the asymptotic statement take $b$ least with $3^b>4X/P$. The gap support has $g_0\le L_0/P\le2X/P$ and $g_0\ge P$, so $b\to\infty$. In any subsequence with bounded $\log X/\log P$ this $b$ is $O(\log P)$. The all-terms geometric estimate implies $\theta\to\log_2 3$. Taking logarithms in (1) yields the claimed exponent. A subsequence on which the ratio tends to infinity requires no bound.

## Effective convexity in the finite period range

Take $P\le Q=10^{1000}$ and $s\ge2^{71}$. Set $\lambda=\log_2 3$. The exact cycle product gives
$$
 0<\theta-\lambda=P^{-1}\sum_{i<P}\log_2(1+1/(3x_i))<2^{-71}.
$$
It puts $3/2<\theta<2$. All rotated prefix discrepancies are below two, so $X\le4/(2^\theta-3)<2/(\theta-\lambda)$.

The accompanying rational certificate brackets $\lambda=1+\ln(3/2)/\ln2$ using $2\operatorname{atanh}(1/5)$ and $2\operatorname{atanh}(1/3)$ with scale $2^{6940}$. For each logarithm successive downward fixed-point powers $\lfloor 2^{6940}/v^{2j+1}\rfloor$ cost less than two units per term after division by $2j+1$, and the tail after the first vanished power costs less than two more units before doubling. The rational endpoints share every Euclidean coefficient needed through three convergents of denominator above $Q$, totalling 1,944 matching convergents with the terminal fence.

For each of the caps $10^6$ and $Q$, take consecutive continued-fraction convergents bracketing the entire log interval, both denominators above the cap. A reduced fraction with denominator below or equal to the cap cannot be between them. This follows from the unit determinant, which gives any interior numerator/denominator vector as a positive integer combination of the bracketing vectors. A cycle slope on the upper side of $\lambda$ therefore lies above the right fence $a'/q'$ and differs from it by at least $1/(Pq')$. For the first cap the right fence is $17087915/10781274$, and $10^6 q'<2^{71}$. This excludes all $P\le10^6$. For the second cap the verifier checks $4Qq'<2^{7000}$, which by the geometric bound gives $2X<2^{7000}$ uniformly over the whole range.

For every $1\le j\le7003$ the certificate checks $\|j\lambda\|>1/20000$ with both rational endpoints. Hence $P\|j k/P\|\ge P(1/20000-7003/2^{71})>4$ for $P>10^6$. The sign-exit and arithmetic-progression proof of STRICT_CONVEX_RANKS.md now applies verbatim with $T=7000$. Its only uses of a large-period estimate were the common calendar for the rank clusters within distance two of $jk$ through time $T+1$ and the final $2^T>2X$ divisibility contradiction. Both conditions have just been checked. This proves strict convexity for all potential periods in the finite problem.

## Reduction to 959 upper convergents

The finite convexity bound implies for $t=r/P$
$$
 L_r\ge(3P^2-P)/2+Pr+r(r-1)/2
 \ge P^2\big((3+2t+t^2)/2-1/P\big).
$$
Use the last cycle-product identity and $x_i=L_r/\ell_r\ge L_r/2$. The eight intervals $j/8\le t<(j+1)/8$ each contain at most $P/8+1$ ranks. With $T_0=10^6$ and $\ln2>69/100$ this gives
$$
 P^2(\theta-\lambda) <
 \frac{200}{207}\left(\frac18+\frac1{T_0}\right)
 \sum_{j=0}^7\frac{1}{(3+2j/8+(j/8)^2)/2-1/T_0}
 <0.484763<\tfrac12 .
$$
The elementary continued-fraction criterion now says $A/P$ is a convergent of $\lambda$, necessarily an upper one. For completeness, if $p_n/q_n$ is the convergent with $q_n\le P<q_{n+1}$, then $|q_n\lambda-p_n|\le|P\lambda-A|$. To see this, expand $(A,P)$ in the basis of the $n$th and next convergents. Unless it is a multiple of the $n$th, the integer coefficients have opposite signs and the coefficient of the $n$th is nonzero, because the denominator is positive and smaller than $q_{n+1}$. Their signed linear-form errors therefore add in magnitude. If the rationals differed, the triangle inequality would give $|A/P-p_n/q_n|<(1/P+1/q_n)/(2P)\le1/(Pq_n)$, a contradiction.

Put $D=A-P\lambda$. The product bound and octave ordering give $D<2P/(3\ln2\,L_0)<P/L_0$, hence $g_0<1/D$. Write $\lambda_+$ for the upper log endpoint, so $Y=\lceil1/(A-P\lambda_+)\rceil$ bounds $g_0$ for the upper convergents under consideration. Of those with $10^6<P\le Q$, the certificate tests all 959 that have not already been eliminated by the floor condition $(A-P\lambda_+)2^{71}\ge P$. For each it substitutes $Y$ into (1) and selects a concrete window among $b=\max(2,\lfloor\log_3Y\rfloor-12),\ldots,\lfloor\log_3Y\rfloor+1$. Every integral upper count is below its tested $P$. The closest comparison has $A=217976794617$, $P=137528045312$, $Y=771316334040$, $b=18$, $w=7$ and upper count $134074517099$. The worst ratio is below $0.974889$. This proves the finite theorem.

The certificate also checks all 52 no-consecutive-one calendar words of lengths one through six by independent literal enumeration of the two lowbit paths and their drift words. These finite tests verify the discrete computations. The convexity, interval-span argument and uniform asymptotic bound are written mathematics. The preceding PR201 finite result through $10^{1000}$ assumed binary valuations and a particular physical strip. Its independent located CRT histogram proof is distinct; the result here assumes canonical width less than two and permits valuation three.

- https://doi.org/10.1007/s11227-025-07337-0
- https://rstation.ai/problems/collatz/papers/145/v1
- https://doi.org/10.22405/2226-8383-2018-19-1-15-25
- https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/arithmetic/CRT_PERIOD_EXCLUSION.md
