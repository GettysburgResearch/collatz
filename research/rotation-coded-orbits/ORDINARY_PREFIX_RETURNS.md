# Hamming distance from a long shifted prefix diverges on every nonperiodic ordinary orbit

**PROPOSED.** Let $x_j=T^j(x_0)$ be a non-eventually-periodic positive ordinary shortcut orbit and let $e_j=x_j\bmod2$. For every real $L>\log(3/2)/\log(4/3)$,
$$
\lim_{q\to\infty} \#\{0\le j<\lfloor Lq\rfloor:e_{j+q}\ne e_j\}=+\infty .
$$
In particular its initial three length-$q$ blocks cannot agree apart from a bounded total number of mismatches along unbounded $q$. This holds at every fixed starting point on the orbit. No limiting parity frequency is assumed. As a consequence a nonperiodic positive shortcut orbit cannot have the parity coding of **any** finite interval partition of an irrational circle rotation, including after a finite prefix.

## Ordinary return equation

Let $s_j=\sum_{i<j}e_i$, $M_j=2^j3^{-s_j}$, and $Z_j=M_j(2x_j+1)$. The real numbers $M_jx_j$ are bounded on a fixed nonperiodic orbit by the orbitwise reciprocal estimate. Explicitly,
$$
M_j x_j=x_0\prod_{i<j,\ e_i=1}(1+1/(3x_i)),
$$
and the positive odd states on this injective trajectory have finite reciprocal sum. Thus $M_j$ and $Z_j$ are bounded. Also $x_q\to\infty$ since all the positive integer states are distinct. [Orbitwise reciprocal estimate and reviewed scope](../integrated/orbitwise-boundaries/README.md)

Put $y_j=x_{j+q}-x_j$, $s'_j=s_{q+j}-s_q$, $w_j=e_{q+j}-e_j$. Direct subtraction of the two ordinary recurrences gives
$$
2y_{j+1}=3^{e_{q+j}}y_j+w_j(2x_j+1).
$$
After multiplication by $2^j3^{-s'_{j+1}}$ this telescopes. The far endpoint tends to zero 2-adically, because $y_j$ is an integer. Hence
$$
-y_0=\sum_{j\ge0} w_j(2x_j+1)2^j3^{-s'_{j+1}}
     =\sum_{j\ge0} \kappa_j Z_j,\qquad
\kappa_j=w_j3^{s_j-s'_{j+1}}.                                 \tag{1}
$$
Every nonzero summand has exact 2-adic valuation $j$. Regardless of subsequent mismatches the truncated error through $j<N$ therefore has 2-adic absolute value at most $2^{-N}$.

Assume a fixed number bounds the mismatch count through $N=\lfloor Lq\rfloor$ for unbounded $q$. On this prefix $s'_j-s_j=\sum_{i<j}w_i$ is bounded. Thus the nonzero $\kappa_j$ there are from a fixed finite set of signed powers of 3. Pass to a subsequence on which the number of mismatches is fixed, and each gap between their ordered indices is fixed or tends to infinity. Group successive indices with fixed gaps. For each group beginning at $m$, pass again to fix all its $\kappa_j$ and local parity block, of fixed length. Ordinary affine iteration within the group shows that its total contribution to (1) equals
$$
Y_m=M_m(A x_m+B)
$$
for fixed rational $A,B$. Its exact 2-adic valuation is $m$, by the first summand of (1). If a group starts at a bounded index, make that index fixed on the subsequence; the group then contributes a fixed rational constant $C_0$. Otherwise set $C_0=0$. The remaining indices $m_i$ tend to infinity and their successive gaps tend to infinity. All their $Y_{m_i}$ are bounded in the ordinary absolute value. Set $G=-y_0-C_0$, so that $|G|\to\infty$ in the ordinary absolute value and $|G|\ll_{x_0,C_0}(3/2)^q$ by $x_{j+1}\le (3x_j+1)/2$.

## The product at the three places

Use the vector $(G,Y_{m_1},\ldots,Y_{m_k})$ and places $\infty,2,3$. Enlarge the set by the finitely many denominator primes of fixed constants if necessary, using coordinate forms there. Entries are $S$-integers and their heights are at most $\exp(O_L(q))$. At 2 replace the $G$ form by $G-\sum_iY_{m_i}$ and use coordinate forms for the rest. At 3 use only coordinate forms; $G$ is bounded there as the difference of integers and a fixed rational. For any group with $A=0$, its coordinate is a fixed nonzero rational times the $S$-unit $M_m$ and its product over all places in $S$ is bounded.

For the groups with $A\ne0$, keep $G$ as one ordinary coordinate form, use $Y_m/A$ at the first such group, and thereafter use differences between successive such normalized coordinates. The forms are independent by their triangular construction. Write
$$
D_m=Y_m/A=M_mx_m+b_mM_m
$$
for the fixed group constants $b_m=B/A$. Ordinary iteration gives, for successive retained indices $l<m$,
$$
M_mx_m-M_lx_l=\sum_{l\le j<m} e_j M_j/3^{e_j}.
$$
For $l\le j\le m$ one has $M_j/M_m=3^{s_m-s_j}2^{j-m}\le(3/2)^{m-j}$. Consequently
$$
 |D_m-D_l|/M_m\ll(m-l+1)(3/2)^{m-l}.
$$
For the first retained index, $|D_m|/M_m=|x_m+b_m|\ll(3/2)^m$. At the finite places of $S$, the coordinate factors of every such $Y_m$ have product at most a fixed constant times $1/M_m$: its 2-adic absolute value is $2^{-m}$, its 3-adic absolute value is $\ll3^{s_m}$, and elsewhere $Ax_m+B$ has bounded absolute value. Multiplying the estimates for the ordered normalized coordinates telescopes their time lengths, with last index at most $N$. Thus the product of all forms at all places is bounded by
$$
 O\!\left((1+q)^k 2^{-N}(3/2)^{q+N}\right).
$$
The same upper bound holds if there are no groups with $A\ne0$. The hypothesis on $L$ gives exponential decay in $q$. If $k=0$ this already contradicts the product formula for nonzero $G$. Otherwise the S-adic Subspace Theorem supplies a fixed proper linear subspace containing infinitely many of the vectors. [Subspace Theorem, S-integer formulation](https://people.mpi-sws.org/~joel/publications/hecke-mahler25.pdf)

In a fixed rational linear relation the coefficient of $G$ must vanish because $|G|\to\infty$ while all group coordinates are bounded. The remaining coordinates have mutually separating 2-adic valuations $m_i$: the first nonzero fixed coefficient gives the unique term of smallest valuation for large $q$. There is no nonzero relation. This contradiction proves the limit.

## Irrational circle rotations

For an irrational rotation by $\alpha$ coded by a finite interval partition, take the unbounded denominators $q$ of convergents from below. If $p/q<\alpha$ is that convergent and $\eta=q\alpha-p$, a mismatch under shift $q$ can only occur within a backward arc of length $\eta$ at a partition endpoint. Visits to any such arc are separated by at least $q$ since $\|i\alpha\|>\eta$ for $0<i<q$. Thus any length-$\lfloor Lq\rfloor$ prefix has at most $(\lfloor L\rfloor+2)$ mismatches per endpoint. A change of endpoint convention affects finitely many hits. This contradicts the theorem for any nonperiodic ordinary positive parity itinerary coded in this way. The same applies after finite steering because its terminal ordinary state starts another orbit.

## Moving starts and separation from other sources

The same conclusion holds at starts $t=t(q)$ on the same nonperiodic orbit whenever $\log x_t=o(q)$, in particular when $t=o(q)$. More generally, for a sequence of pairs $(u,v)$ with $u=x_t$ on one fixed nonperiodic positive trajectory, $v$ any positive ordinary source, $v\to\infty$, and $\log u=o(\log v)$, a bounded Hamming distance on their first $N$ parities implies
$$
 \limsup \frac{N}{\log v}\le\frac1{\log(4/3)}.                 \tag{2}
$$
The ratio is understood along the specified sequence. In particular, about the parity itinerary of a fixed positive nonperiodic source the other unbounded sources at bounded prefix Hamming distance have size $\ge(4/3)^{N-o(N)}$.

For (2), suppose $N\ge(1+\epsilon)\log v/\log(4/3)$ along an unbounded subsequence, and truncate to the ceiling of this lower bound. Use the two trajectories from $u$ and $v$ in the return argument. Formula (1) still holds for their difference because both trajectories consist of integers. There is a uniform constant $C$ with $M_j x_{t+j}\le C u$ for the relative $M_j=2^j/3^{s_{t+j}-s_t}$, by the same finite reciprocal product on every suffix of the fixed orbit. Keep the bounded-index group, if any, as one ordinary vector coordinate: its value need not be fixed when $t$ moves. All group coordinates have ordinary size $O(u)$, so $G=u-v$ dominates them as required. The 2-adic valuations still equal the first indices, mutually separated across groups, including the possible first bounded index. The coefficient and local parity choices within each group are finite and can again be made fixed. In the product bound the first normalized coordinate now costs $O(u(3/2)^m)$ before telescoping, and $|G|\le 2v$. The bound becomes
$$
 O((1+N)^k u v (3/4)^N),
$$
which is exponentially small in $N$ at the chosen truncation. Heights remain at most exponential in $N$ since both starting heights have logarithms $O(N)$. This proves (2).

For the moving-start conclusion take $u=x_t$, $v=x_{t+q}$. If $\log v=o(q)$ on a subsequence of bounded Hamming distance, the two starting heights both have logarithm $o(q)$. An exact matching run of length $b$ requires divisibility of the difference between its two entering states by $2^b$, since a parity prefix determines its residue modulo $2^b$. Those states stay distinct along a nonperiodic orbit. Thus the first matching run has length $o(q)$, and both heights remain $\exp(o(q))$ after the following mismatched step by the ordinary growth bound. Iteration through the bounded number of mismatches, including the final matching run, cannot cover $\lfloor Lq\rfloor$ positions. Consequently a putative counterexample has $\log v\gg q$ after passing to a subsequence. Then $\log u=o(\log v)$ and $\log v\le q\log(3/2)+o(q)$, so (2) contradicts the asserted window length.
