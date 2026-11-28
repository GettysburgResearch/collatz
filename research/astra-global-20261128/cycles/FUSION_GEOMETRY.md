# Size and phase transition of the integer translation class

Use the exact tilted parity law $\mu_p$ with $0<p<1$. For a two-adic $x$ let $C_t(x)$ be all integer displacements $h$ for which the true endpoints and grades from $x,x+h$ agree at date $t$. Set $C_\infty(x)=\bigcup_t C_t(x)$. For nonzero $h$ fixed, the [affine overlap theorem](TILTED_FUSION.md) identifies the probability of membership with the common mass $c_p(h)$ of the tilted measure and its translate. At the critical bias $\alpha=\log_3 2$ this random integer set is the limiting pattern of ordinary neighboring nondecreasing starts around a source conditioned on actual nondecrease at a long tested date, under the stated ordinary binary-horizon conditions.

### Sparse inclusion on the whole integer line

For $p\ne1/2$ put $\gamma_p=\log_2(1+2\sqrt{p(1-p)})<1$. Uniformly over all integer intervals $J$ of length $H\ge1$,
\[
     \mathbb E_{\mu_p}|C_\infty(x)\cap J|\le C H^{\gamma_p}.             \tag{1}
\]
Consequently $|C_\infty(x)\cap[-H,H]|\le H^{\gamma_p+o(1)}$ almost surely in the exponent sense. Indeed use dyadic $H$, Markov at exponent $\gamma_p+\epsilon$, and Borel–Cantelli for each rational $\epsilon>0$. The probability in (1) is computed at the tilted root. It does not give an all-locations pointwise bound on the same sample.

On residues modulo $2^k$, write $w(r)=\mu_p(r+2^k\mathbb Z_2)$. The exact common part is bounded by $\sum_r\sqrt{w(r)w(r+h)}$, by projecting to this finite partition and taking the geometric mean. In any interval of exactly $2^k$ consecutive shifts, summing this bound gives
\[
       \Big(\sum_r\sqrt{w(r)}\Big)^2
                 =(\sqrt p+\sqrt{1-p})^{2k}.
\]
The equality uses the native bijection with every length-$k$ parity word, without any assumption about the ordinary binary digits of $x$. Enclose shorter intervals in dyadic lengths up to twice their size. This proves (1).

### Finite classes above the critical grade

If $p>\alpha$, the entire integer translation class $C_\infty(x)$ is finite almost surely. If $0<p<1$ and $H(p)>p\log3$, it is infinite almost surely and its finite-stage class grows at least exponentially, where $H(p)=-p\log p-(1-p)\log(1-p)$. In particular there is a genuine transition between the two regimes. These results do not locate a sharp threshold inside their gap, including the case $p=\alpha$.

For the first assertion the true finite real correction $R_t(x)=\sum_{j<t}i_j2^j/3^{k_{j+1}}$ increases to a finite nonnegative $R_\infty(x)$ almost surely by the strict negative real drift $\log2-p\log3<0$. For each $h\in C_\infty(x)$, exact fusion and equal grades give $h=R_t(x)-R_t(x+h)$ at all sufficiently large $t$. Hence $h\le R_\infty(x)$, so this integer class has a rightmost member. On every finite fusion cylinder the partial shift $x\mapsto x+h$ preserves $\mu_p$ exactly, as shown in [the finite source fibre theorem](ORDINARY_SOURCE_FIBRES.md); partition by the first such date to get this also on $h\in C_\infty(x)$. Countable summation therefore permits mass transport under these partial shifts. In detail an invariant positive-mass event of infinite classes with a rightmost point would allow each member to send one unit to its rightmost. Expected outflow is the mass of the event. Expected inflow is zero if a root has zero probability to be its rightmost, and infinity otherwise. Tonelli and the partial translations equate these expected flows, a contradiction. Boundedness above holds at almost every root on the event, and the countably many partial shifts preserve the full-measure property. This proves finiteness.

For the lower assertion, condition on $k_t=k$. From the exact finite grade/output counting bound in that fibre theorem,
\[
     \Pr\{|C_t(x)|<\binom tk/(M3^k)\mid k_t=k\}\le M^{-1}.
\]
Take $M=t^2$ and use Borel–Cantelli, $k_t/t\to p$ and Stirling. Thus
\[
      \liminf_{t\to\infty} t^{-1}\log |C_t(x)|\ge(H(p)-p\log3)_+ .
\]
More generally $\limsup t^{-1}\log |C_t(x)|\le(\log2-p\log3)_+$ for every $p$. Indeed the finite-class uniform-root inequality gives $|C_t(x)|\le t^2(1+R_t(x))$ almost surely eventually, and $\max_{j\le t}|k_j-pj|=o(t)$ bounds the logarithm of the real sum. At fair bias the two exponents agree at $\log(4/3)/2$, with the sharper Brownian finite-fibre result in the companion note. These growth statements do not require the external Haar fusion theorem.

### Critical repulsion for a moving translation

There are absolute positive constants $C,c$ such that for integers $h\ne0$, $t$ sufficiently large and $k/t$ in a fixed small neighborhood of $\alpha=\log_3 2$, the exact uniform depth-$t$ binary grade slice satisfies
\[
 \Pr\{k_t(x+h)=k,\ T^t(x+h)\ne T^t x\mid k_t(x)=k\}
   \le C\exp\left[-\frac{ct}
      {\log(2+|h|)+|k-\alpha t|+t^{2/3}}\right].                        \tag{2}
\]
For clarity in the binary model the unequal endpoints in (2) mean absence of a counted cylinder fusion; when final grades are equal the difference is an actual constant on the cylinder. Thus (2) transfers directly to ordinary octaves with relative rounding factor $1+O(2^t/X)$, including moving $h$ as long as positive source values are needed. It tends to zero for every $\log(2+|h|)=o(t)$ and $k/t\to\alpha$. In particular it is stretched exponentially small if the two terms besides $t^{2/3}$ are $O(t^{2/3})$. At a fixed exponential displacement bound $|h|\le e^{\delta t}$ this method gives $Ce^{-c/\delta}$ as $t\to\infty$, without a claimed exponential saving in $t$.

Put $p=k/t$, $s=\lfloor t/2\rfloor$, $V=t^{2/3}+|k-\alpha t|+\log(2+|h|)$. Work under the Bernoulli$(p)$ first-coordinate tilt, in the walk $D=k(x+h)-k(x)$ that drifts toward negative values at embedded mixed dates. Complete the walk after fusion with independent signs if necessary. The first-half exact-slice density is bounded and its full-date density is $O(\sqrt t)$ by the binomial bridge estimates in the companion. With probability $1-O(e^{-c t^{1/3}})$ in this first half, the distinguished grade at every $j\le s$ stays within $t^{2/3}+|k-\alpha t|$ of $\alpha j$, by a union bound and Hoeffding (decrease the constant $c$ to absorb the number of dates).

If there are at least $t^{1/3}$ mixed dates by $s$, the biased embedded walk there lies below $-c_1t^{1/3}$ except with probability $O(e^{-c t^{1/3}})$ by summing its drift deviations over all embedded indices $\ge t^{1/3}$. This half-prefix exception transfers by bounded density. Once below that level the probability of returning to zero by date $t$, necessary for the specified equal final grades, is $O(e^{-c t^{1/3}})$ by gambler's ruin at the sign clock. The full-slice density cost $O(\sqrt t)$ is absorbed.

On the remaining paths there are at most $t^{1/3}$ mixed dates by $s$ and no fusion by $s$ if the tested event occurs. Every first-half grade of the companion then also lies within $t^{2/3}+|k-\alpha t|+t^{1/3}$ of its critical line. At an initial prefix with resonant $D_j=0$ the common odd count is $k_j$ and the native state difference is the nonzero ordinary integer
\[
      \Delta_j=(3^{k_j}/2^j)
            [h+R_j(x+h)-R_j(x)] .
\]
Under these first-half grade controls $3^{k_j}/2^j\le e^{CV}$ and each positive finite $R_j$ is at most $te^{CV}$. Thus $\log(2+|\Delta_j|)\le C'V$ at every such prefix. The common hold after entry into that resonant grade is at most $1+v_2(\Delta_j)\le C'' V$, including an unfinished interval up to $s$.

At nonresonant mixed-clock levels $d$ with $|d|\le1+t^{1/3}$ the native envelope has $v_2(3^d-1)\le C\log(2+t)$, and the excess over $1+v$ has a geometric exponential moment uniformly in the history. Over the first $1+\lceil t^{1/3}\rceil$ embedded intervals the sum of these nonresonant costs is at most $t/8$ except with probability $O(e^{-ct})$, by exponential Markov and the logarithmic cost per interval. An unfinished nonresonant interval can be truncated at $s$ and is dominated by the full cost. The event that the *observed* nonresonant time through $s$ is excessive is a half-prefix event, so its exceptional bound transfers with bounded density. When using the completed walk, assign zero excess to unrealized intervals after absorption and apply the exponential bound only to realized nonresonant intervals.

To cover the first half outside those costs therefore requires at least $c t/V$ entries into resonant grade zero, including the initial entry. The number of visits to zero in a biased nearest-neighbor walk has a geometric tail bounded by $C e^{-c j}$ uniformly for $p$ near $\alpha$, since at each departure it has probability $|2p-1|$ never to return. The event of this many observed visits by $s$ is again bounded under the slice by a fixed multiple of the tilted probability. Combining these estimates gives (2), with $V\ge t^{2/3}$ absorbing the discarded stretched-exponential terms. The result permits an arbitrary nonzero final displacement and makes no assumption on an eventual integer component.
