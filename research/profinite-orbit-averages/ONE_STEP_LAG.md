# A one-step difference between two harmonic merger tests

**PROPOSED, source-qualified.** Use the shortcut map $T(n)=n/2$ on even inputs and $T(n)=(3n+1)/2$ on odd inputs. Put
$$
 B_d=\{n\ge1:T^i(2n)\ne T^j(2n+1)\ \text{for all }i,j\ge0\text{ with }|i-j|\le d\}.
$$
There is no stopping-time cutoff. Write $P$ for the positive integers eventually reaching 1. The following conclusions concern ordinary positive integers.

1. $\sum_{n\in B_0}1/n=\infty$, even though $B_0$ has natural density zero.
2. $\sum_{n\in B_1}1/n<\infty$ **if and only if** $P=\mathbb N_{>0}$. In that case $B_1$ is empty. If $P$ is proper, even the subset on which **exactly one** of $2n,2n+1$ belongs to $P$ has divergent reciprocal sum. Those pairs never meet with any lag.

The divergent reciprocal sum for $B_0$ has an elementary proof independent of any density theorem. For the converse about $B_1$ we use the positive lower natural density of the predecessor set of every fixed odd unit modulo three. Every merger component contains such a unit, by stripping even factors and taking an odd step if necessary. The zero-density assertion alone uses the qualitative adjacent synchronization theorem. The argument supplies no finite upper bound for the series on $B_1$. [Predecessor theorem and source comparison](../primary-evidence/PRIMARY_SOURCES.md) · [Adjacent synchronization and original sources](CLOCK_CHARACTERS.md)

## Prefixes of one binary expansion

Suppose $a$ is a bounded real function on positive integers such that $a(2n)=s a(n)$ for $s\in\{1,-1\}$ and $a(3n+1)=a(n)$ for odd $n$. For $t>0$ let $n_k=\lfloor 2^k t\rfloor$, ignoring the finitely many zero prefixes. If
$$
 \sum_{n\ge1}\frac{|a(2n+1)-a(2n)|}{n}<\infty,                         \tag{1}
$$
then $s^k a(n_k)$ converges almost everywhere to a constant, which is zero for $s=-1$.

Indeed a change from a parent to its even child costs zero. Its odd child contributes $|a(2n+1)-a(2n)|$. Integrating their sum over $t\in[u,v]$, $0<u<v$, counts each $n$ at most $O_{u,v}(1)$ times with weight $O_v(1/n)$. Thus almost every ray has finite total variation; call its limit $F(t)$. Then $F(2t)=sF(t)$ almost everywhere. Almost every binary expansion has infinitely many occurrences of the four-bit word 1011, by independence on disjoint four-bit blocks. At the position of its first bit, $n_k$ is odd and $\{2^k t\}\in[3/8,1/2]$. Thus $\lfloor 2^k(3t)\rfloor=3n_k+1$ along this subsequence. Applying convergence at both $t$ and $3t$ yields $F(3t)=F(t)$. The bounded measurable function $F$ is invariant under multiplication by 4 and 3. In logarithmic coordinates this is invariance under an irrational rotation on a circle of circumference $\log 4$, so $F$ is constant almost everywhere. The doubling identity forces the constant to vanish for $s=-1$.

For the first claim assume $\sum_{B_0}1/n<\infty$. On almost every binary ray only finitely many observed odd children have parent index in $B_0$, by the same shell integral and Borel–Cantelli. Thereafter a parent and each observed child lie in the same merger component: the even child maps to its parent and the good odd child synchronizes with the even one. Since the components are countable, some fixed component $C$ has positive measure of rays eventually staying in it.

There is a nontrivial root of unity $\omega$ and a label $a$, zero off $C$ and of modulus one on $C$, with $a(Tn)=\omega a(n)$. If $C$ has a cycle, take $\omega$ of its exact period $p$. This period exceeds one since $T$ has no positive fixed point. Label successive cycle positions by consecutive powers and extend by first arrival. On an acyclic component take $\omega=-1$ and choose a fixed reference source. If $T^i n=T^j b$ for that source $b$, assign $a(n)=(-1)^{j-i}$. The time difference is independent of the common vertex since the forward ray has no repeat. In either case equal-time mergers have equal labels, $a(2n)=\omega^{-1}a(n)$ and $a(3n+1)=a(n)$ for odd $n$. The last identity holds because $T(3n+1)=T(n)$.

The compensated labels $\omega^k a(n_k)$ therefore stabilize almost everywhere and have a nonzero limit on the positive-measure event just selected. The digit argument above still gives $F(3t)=F(t)$, while $F(2t)=\omega^{-1}F(t)$. The factors $3$ and $2^{\operatorname{ord}(\omega)}$ are multiplicatively independent, so $F$ is constant and hence zero. This contradiction proves divergence without assuming the existence of any positive-density basin. The separate zero-density assertion for $B_0$ follows from balanced adjacent synchronization after restriction to even starts.

For the second claim use $a=\mathbf1_P$ and $s=1$. If its sibling boundary had finite reciprocal sum, the limiting constant would be zero or one since the labels are bits. Dominated convergence and dyadic subdivision would force one of $P$ and its complement to have natural density zero. When the complement is nonempty, each side contains a fixed positive-density predecessor set. Finally, if every integer reaches 1, the two points on the eventual shortcut cycle allow any pair to meet at times differing by at most one. This proves both directions.

## Beyond summability: what a typical sequence of prefixes sees

For any fixed nonempty merger component $C$, almost every $t>0$ has **infinitely many** binary prefixes $n_k$ in $C$. For $C=P$, take $a(n)=(-1)^{\tau(n)}$ at starts reaching 1, where $\tau$ is first arrival, and zero elsewhere. Each compensated sign $(-1)^k a(n_k)=\pm1$ also occurs infinitely often for almost every $t$. These assertions can be imposed simultaneously over the countably many components.

Here is the zero-one argument. For one of the stated labels, let $E$ be the set of $t$ seeing that label infinitely often. A next bit of zero preserves the label, so, outside the eventually-zero expansions, infinitely many occurrences imply infinitely many occurrences at odd prefixes. Their positions are stopping times for revealing the binary digits. After each such position, the next three bits are 011 with conditional probability $1/8$. Select the next test only after these three bits have been exposed. The chance of failing $m$ successive completed tests is at most $(7/8)^m$; on the event of infinitely many tests, successes recur infinitely. At each success the same label occurs at $3t$ by the odd identity. Hence $t\in E$ implies $3t\in E$ almost everywhere. The set $E$ is multiplicatively 4-periodic, and multiplication by 3 on the logarithmic circle preserves measure. The inclusion is equality modulo null sets. Irrational rotation makes $E$ null or conull. Positive upper shell density makes the unphased occurrence event have positive measure by reverse Fatou. For the two signs their union has positive measure and doubling exchanges them. This proves the assertions.

In particular if another component exists, almost every binary-prefix ray switches between $P$ and its complement infinitely often. Even if all integers reach 1, the two compensated cycle phases switch infinitely often. The prefixes sample different ordinary starting integers. The assertion about the phases uses the exact two-cycle and does not presume universal convergence.

## How long finite searches can miss an ordinary merger

For $h\ge1$ sample consecutive starts $x,x+1$ with $2^h\le x<2^{h+1}$. A **balanced** meeting uses the same shortcut time and the same number of odd inputs on the two paths up to that time. Write $\kappa=2\mathbb E M/\sqrt\pi>0$ for the balanced shortcut tail constant in Leen's Theorem A (its $M$ counts the excursions of the adjacent pair). With *arbitrary* independent shortcut times $0\le i,j\le h$, the fraction of pairs that fail to meet is
$$
                         (\kappa+o(1))/\sqrt h.                        \tag{2}
$$
The shell is an exact full dyadic period for the balanced test at $h$. The equality of its leading constant with the unrestricted two-clock test follows from the estimate below. Leen's original-rate theorem distinguishes the balanced shortcut clock from its ordinary unshortened clock, which has another constant. [Leen, Theorem A](https://doi.org/10.5281/zenodo.23268751)

Fix $0<\epsilon<\frac12\log_2 3$. Put $H=\lfloor(1+\frac12\log_2 3-\epsilon)h\rfloor$. Apart from $O_\epsilon(2^h e^{-c_\epsilon h})$ starts in the shell, **every** meeting with $0\le i,j\le H$ must be balanced. To prove this, the first $h$ shortcut parity bits of each start separately are uniform on binary words, since either member of the pair ranges over a full period. With exponentially small exception, simultaneously for $0\le t\le h$ on both paths the number of odd steps $p_t$ is at least $t/2-\delta h$, for any fixed small $\delta>0$, by a binomial exponential bound and a union bound. Thus $T^t(x)\ge x3^{p_t}/2^t$ gives a minimum height at least $2^{(\frac12\log_2 3-\delta\log_2 3)h}$ up to $h$, and the same for $x+1$. Each subsequent step can at worst halve the value. Taking $\delta\log_2 3<\epsilon/2$ keeps every state at least $2^{\epsilon h/2}$ through $H$.

Taking logs of the exact shortcut product for the two sources shows that equality at times $i,j\le H$ requires
$$
 |(p_i(x)-p_j(x+1))\log3-(i-j)\log2|\ll H 2^{-\epsilon h/2}+2^{-h}.
$$
The error sums the positive terms $\log(1+1/(3z))$ from odd inputs and the initial log ratio of $x+1$ and $x$. A nonzero linear form on the left is bounded below by a negative power of $1+H$, by the finite irrationality measure of $\log_3 2$. Thus it vanishes identically for large $h$. Unique factorization gives $i=j$ and equal odd counts, as asserted. Combined with Leen's balanced tail on the full period this proves (2) at $h$. The exceptional starts across all dyadic shells have finite reciprocal sum. Consequently the pairs failing to meet even with independent clocks through $H$ still have divergent reciprocal sum, by the all-time equal-clock obstruction above restricted to even starts. Equation (2) makes no assertion about the leading constant at the longer clock $H$. [Irrationality estimate and source](../binary-run-occupancy/MELLIN_PHASE.md)
