# Normal binary digits can avoid every tripling merger over the 2-adics

**PROPOSED, unconditional.** Use the same shortcut branches on the 2-adic integers. Fix $r\ge1$ and compare $n$ and $3^r n$. In **every** binary class still unabsorbed in the common-prefix comparison, there is a set of $n$ of Hausdorff dimension one for which the two 2-adic orbits are disjoint at all pairs of finite clocks. These $n$ may simultaneously be chosen with normal binary digits for both starts and normal parity sequences on both arms. The 2-adic metric is normalized by $|2|_2=1/2$. This result concerns infinite digit strings. The existence of an ordinary positive integer with disjoint orbits remains open.

## A measure carried by the surviving prefixes

As in the [finite-clock proof](THREE_RAY_CLOCKS.md), orient the two affine expressions remaining after the exposed bits as $X,3^sX+D$. When $s>0$, an even offset keeps the level fixed on both lifts. An odd offset gives levels $s-1$ and $s+1$, one on each lift. Thus the mean of the two child levels is exactly $s$. Stop a path if it first reaches zero. If the initial unabsorbed class instead has $s=0$, its offset is nonzero. Choose even base inputs to strip powers of two from that offset until it is odd. The next step goes to positive level. This fixes just one additional finite prefix.

Start inside the resulting class with positive level $s_0$. Assign to each extension by $h$ further input bits the mass
$$
 \mu(C)=\begin{cases}
 2^{-h}s_h/s_0,&\text{if none of its levels has reached zero},\\
 0,&\text{otherwise}.
 \end{cases}
$$
The two child masses sum to their parent's mass, so these cylinder probabilities define a probability measure. It gives full measure to the paths staying at positive level forever. Since $s_h\le s_0+h$, every length-$h$ extension has mass at most $(1+h/s_0)2^{-h}$. This gives zero measure to every singleton. For each $0<d<1$ it also bounds the mass of every ball of radius $2^{-h}$ by a constant times $2^{-dh}$, after adjusting for the fixed starting prefix. Any countable cover of a full-measure subset therefore has the sum of its radius-to-the-$d$ powers bounded below. Its Hausdorff dimension is at least $d$ for every $d<1$, and at most one in the ambient binary space.

## Independent clocks and normality

Two parity words of lengths $i,j$ and odd counts $p,q$ give affine endpoints with slopes $3^p/2^i$ and $3^{r+q}/2^j$ in $n$. Equal slopes require $i=j$ and $p=r+q$. Inside the chosen positive-level continuation the absolute difference of these exponents is positive. At earlier clocks inside the fixed prefix, a tie of slopes with unequal offsets gives no merger, while equality of both would already have absorbed the class. At unequal slopes, endpoint equality fixes a single rational $n$. Removing all rational $n$ costs zero measure and excludes every remaining possible meeting at independent clocks.

For normality, first use the uniform law on the $2^h$ extensions. For each arm, the new ordinary digits and the new parity digits considered separately run uniformly through all binary words of length $h$. The original multiplier is odd on either arm, and the endpoint coefficient on the free parameter after a fixed prefix is an odd multiple of a power of three. Thus every next parity bit has two opposite binary lifts. For a specified block of $k$ digits, a fixed positive discrepancy from frequency $2^{-k}$ has probability $O(e^{-c h})$: split its occurrences into the $k$ residue classes of starting positions, giving independent disjoint blocks within each class, and apply the binomial tail bound. The probability under $\mu$ is at most $(1+h/s_0)$ times this. Summability and a countable intersection over blocks and rational discrepancies prove all four normality assertions. No independence between the two arms is required.

The surviving set nevertheless has ordinary Haar measure zero by the [excursion upper bound](THREE_RAY_UPPER.md). Its full dimension explains why proving most binary prefixes eventually synchronize, even with quantitative clock estimates, leaves the exceptional positive integers as a separate question.
