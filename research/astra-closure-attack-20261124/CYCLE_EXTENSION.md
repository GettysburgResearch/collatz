# An obstruction to logarithmic partitions of an ordinary cycle

**Status.** Source-qualified written proof. The external input for the local result is Evertse's Corollary 1 with prime set **exactly** $\{2,3\}$. The window centers, their denominators, and even the rational cycle's reduced denominator may vary. Their primes are paid for explicitly. The finite controls do not check the external theorem or establish the missing structural upper bound.

## Result for the entire numerical denominator

Use the shortcut word conventions of CYCLE_CLOSURE.md. Let a primitive positive rational cycle of shortcut length $A$ have actual reduced denominator $d$. Partition its itinerary into $k\ge2$ nonempty contiguous windows and let $H=\max_i h(c_i)$, with $c_i$ the reduced rational center of the affine map of window $i$ and $h(b/a)=\log\max(a,|b|)$ in lowest terms. A window can have arbitrary internal parity and either sign of clock imbalance.

For every fixed integer $m\ge1$ and $\epsilon>0$, there is a constant $C_{m,\epsilon}$, independent of the cycle, its centers, the partition and $d$, such that
\[
 A\le C_{m,\epsilon}
 \big[1+(1+\epsilon)\log_2(3/2)\big]^{\lceil k/m\rceil}
 \big(1+H+\log d+\log A\big). \tag{1}
\]
In particular:

* For $k=O(\log A)$ and $H\le A^{1-\eta}$ for some fixed $\eta>0$, as $A\to\infty$ the full reduced denominator satisfies **$\log d=A^{1-o(1)}$**. This is a power-scale statement about $\log d$; it does not assert $\log d\sim A\log2$.
* For ordinary cycles, if $A/(1+H+\log A)\to\infty$, then **$k/\log[A/(1+H+\log A)]\to\infty$**. In particular no fixed or changing dictionary with center heights $\le A^{1-\eta}$ can represent growing primitive ordinary cycles in $O(\log A)$ windows.
* Taking ordinary monochromatic runs gives centers $0$ and $-1$. Thus along any sequence of primitive ordinary cycles of increasing length the number of cyclic runs of ones divided by $\log A$ tends to infinity (the total number of maximal runs is twice that number).

For the first consequence choose a proposed $k\le K\log A$. For any $\zeta>0$ choose the **fixed** $m$ so large that the power factor in (1) is at most $O(A^{\min(\zeta,\eta)/2})$. The exponent of $A$ on the resulting lower bound for $1+H+\log d+\log A$ exceeds $1-\eta$ and $1-\zeta$. Use $d\le2^A$ for the other bound. For the second consequence fix $\epsilon$ and apply (1) with each fixed $m$ separately, first sending $A$ to infinity and only then allowing arbitrarily large $m$. No claimed rate depends on an unknown growth rate for the exceptional tuples when $m$ varies.

## 1. Fixed-dimensional local estimate with moving centers

Let $n_i=d x_i$ be the positive integer numerators at the boundaries of at most $m$ windows in a segment of total length $L$. Define $B=1+H+\log d$, $Y_i=n_i+d+5$, and $b_i=d c_i$. The reduced numerator and denominator of each $b_i$ are at most $e^B$ in absolute value. At one shortcut step $Y_{\rm next}\le(3/2)Y_{\rm start}$. No individual window fixes its entry state: it is proper in a primitive literal cycle. The proof also applies to noncyclic actual positive segments whenever the used windows satisfy this nonfixing condition.

We prove, uniformly in the centers,
\[
 L\log 2\le (1+\epsilon)\log Y_0 + O_{m,\epsilon}(B). \tag{2}
\]
For a single window of length $\ell$ with reduced numerator-center $b/a$, the centered endpoint equation gives $2^\ell\mid a n_{\rm start}-b$. The right side is nonzero, so $\ell\log2\le B+\log Y_{\rm start}+O(1)$. Repeated application and the one-step height bound show that, starting from any boundary with $\log Y_i=O_m(B)$, the remaining at most $m$ windows have total length $O_m(B)$.

Call a boundary low if $n_i\le T=100(m+2)e^B$. If the starting boundary is low use the preceding observation. Otherwise stop the segment at its first low boundary if there is one, and at its last boundary otherwise. Only an $O_m(B)$ suffix is discarded. Relabel the retained boundaries $0,\ldots,h$, $1\le h\le m$. All retained boundaries except possibly $h$ are high. Write $L,P$ now for the retained length and odd count, $L_j,P_j$ for the partial clocks, and $w_j=2^{L_j}3^{P-P_j}$. Centering each affine map gives the exact telescope
\[
 w_h(n_h-b_h)-w_0(n_0-b_1)
       =\sum_{j=1}^{h-1}w_j(b_j-b_{j+1}). \tag{3}
\]
Here $w_0=3^P$ and $w_h=2^L$. At a high-to-high window,
\[
 \frac{w_j n_j}{w_{j-1}n_{j-1}}
       =\frac{1-b_j/n_{j-1}}{1-b_j/n_j}.
\]
Consequently $w_j n_j/(w_0 n_0)\le [(1+e^B/T)/(1-e^B/T)]^m<2$ through any all-high prefix.

Rewrite (3) with initial endpoint $w_0(n_0+t)$, choosing $t=0$ or $1$ to make $n_0+t$ odd. Include the separately weighted initial coefficient $b_1+t$ among the atoms. If the terminal boundary is high, use endpoint $w_h(n_h+t')$, where $t'=0$ or $1$ makes $3\nmid n_h+t'$, and include a terminal atom with coefficient $b_h+t'$. If the boundary is low, keep its combined endpoint $w_h(n_h-b_h)$ and add no terminal atom. This endpoint is nonzero by nonfixing. Remaining atoms have coefficients $\pm(b_j-b_{j+1})$. All atoms are attached to **high** boundaries. The sum of their absolute values is strictly less than the initial endpoint: each interior atom is at most $4e^B/T$ times the latter by the prefix bound; each exterior atom is at most $2(e^B+1)/T$ times it. This bound does not depend on the real size of a low terminal displacement.

Choose a minimal vanishing subsum containing the initial endpoint. It exists by finite descent from the whole signed relation, removing any vanishing complementary sublist, and has no proper nonempty zero subsum. It contains the terminal endpoint by strict dominance. Let $Q$ be the least common multiple of the denominators of the retained centers; $Q\le e^{mB}$. Clear denominators by $Q$. If the subsum has only two terms, at a high terminal this is incompatible with the initial odd unit after cancelling $Q$. At a low terminal the initial term has 2-adic valuation $v_2(Q)$ and the terminal is an integer multiple of $2^L$. Hence $L=O_m(B)$ and (2) already follows.

Otherwise divide the cleared retained tuple by its positive common gcd $g$. This normalization costs at most $\log g=O_m(B)$, for the following three separate reasons:

* At 2 the initial endpoint bounds the valuation by $v_2(Q)$.
* At 3 the high terminal bounds it by $v_3(Q)$. At a low terminal the nonzero integer $Q(n_h-b_h)$ has absolute value $\le e^{O_m(B)}$, while $w_h$ is a power of two.
* Outside $\{2,3\}$, a nonzero retained atom has outside part at most $2Q(e^B+1)$. Its clock factor $w_j$ has no other primes.

The height $\mathcal H$ (maximum absolute entry) of the primitive tuple therefore satisfies $\mathcal H\ge2^L Y_h e^{-O_m(B)}$. At a high terminal this uses $n_h+t'\asymp Y_h$; at a low terminal use $Y_h\le e^{O_m(B)}$ and $|n_h-b_h|\ge e^{-B}$. The outside-$\{2,3\}$ part of the product of its entries is at most
\[
                 Y_0 Y_h \exp(O_m(B)).
\]
Indeed the two cleared endpoints cost at most $Y_0Y_h\exp(O_m(B))$ outside those two primes, every retained atom costs at most $2Q(e^B+1)$, and normalization can only decrease the outside part.

For a primitive nondegenerate zero-sum integer tuple of any of these finitely many dimensions, Evertse, Corollary 1, bounds that outside part below by $c_{m,\theta}\mathcal H^{1-\theta}$ for every fixed $0<\theta<1$. To see the uniform constant, apply the finite-exceptions statement with its coefficient one, then take the minimum positive ratio on its finitely many exceptions and over the dimensions through $m+3$ entries. The prime set and dimensions do **not** depend on the centers or on $A$. We have proved
\[
 (1-\theta)L\log2\le\log Y_0+\theta\log Y_h+O_{m,\theta}(B).
\]
Now $Y_h\le(3/2)^L Y_0$. Choosing $\theta$ small enough that $(1+\theta)\log2/(\log2-\theta\log3)\le1+\epsilon$ gives (2), including the discarded suffix. [Evertse, *On sums of S-units and linear recurrences*, Corollary 1, printed p. 227](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

## 2. Paying for the whole clock

As in CYCLE_CLOSURE.md §3, rotate to a boundary minimizing the partial products of the window multipliers, with the empty product included and the terminal product omitted. Every suffix product in the rotated list is at most one. Thus $x_0\le 2k e^H/(1-3^p/2^A)$, and the fixed two-logarithm lower bound gives $\log Y_0=O(B+\log A)$, uniformly because $k\le A$.

Split the rotated list into groups of $m$ windows and one possible shorter group. If a group of total length $L$ starts at log-height $Z=\log_2 Y$, (2) yields $L\le(1+\epsilon)Z+O_{m,\epsilon}(B)$. The next log-height is at most $Z+L\log_2(3/2)$. Iterating this affine inequality and summing lengths over $\lceil k/m\rceil$ groups gives (1). No bound on the center height of a concatenated group was assumed.

## 3. Why an upper bound cannot come just from primitive high positive words

There are primitive **nonintegral** positive rational cycles of arbitrarily large coprime clocks $(A,p)$, with $\Lambda=A\log2-p\log3=O(1/p)$, bounded gaps and minimum $\gg p^2$, which require at least $cA/(H+\log A)$ windows of height at most $H$, for any prescribed $H=H(A)\ge1$ with $H+\log A=o(A)$. The choice of the word can depend on $H$. Here is a counting proof.

Use upper continued-fraction convergents $A/p$ to $\log_2 3$. Start with the lower mechanical word of length $A$ and weight $p$, using bits $\lfloor(j+1)p/A\rfloor-\lfloor jp/A\rfloor$. In each complete consecutive eight-bit block use one of two strings of the same odd count differing in a single adjacent transposition of 01 and 10. For large convergents every such block has either five or six ones. Leave the final shorter block unchanged. This gives $2^{\lfloor A/8\rfloor}$ distinct words. All are primitive since $\gcd(A,p)=1$. At least half are nonintegral: fix all but one swap. The two carries differ by a signed $2^u3^v$, a unit modulo the common $D>1$, so they cannot both be divisible by $D$. Here $D=1$ is impossible for $A\ge3$ modulo eight.

The prefix count changes by at most eight inside a rewritten block and is preserved at its boundaries. Thus all cyclic intervals have count discrepancy at most 18 from length times $p/A$; this also bounds all zero-runs uniformly. For any rotation, an odd position $d_i$ satisfies $d_i>(A/p)i-38$ for all sufficiently large convergents. Each carry term $2^{d_i}3^{p-1-i}$ is therefore at least a fixed positive constant times $3^{p-1}$, since $2^{A/p}>3$. Dividing by $D=3^p(e^\Lambda-1)$ gives the claimed minimum at every phase.

At most $4e^{2H}$ rationals have height $\le H$. A rational center of a nonempty shortcut word has an odd reduced denominator and determines its entire repeated itinerary by literal parity, even if it is zero or negative. For fixed center and fixed length there is therefore at most one word. The number of length-$A$ words admitting a cyclic partition into at most $t$ such windows is at most $A\,t(4 A e^{2H})^t$, including the choice of rotation. For $t$ a sufficiently small absolute constant times $A/(H+\log A)$ this is less than half the constructed words for all large $A$. That proves the obstruction; it does not manufacture an ordinary nontrivial cycle.

No argument here gives a logarithmic-size partition for arbitrary ordinary cycles. The exact gap is now narrower: the omitted upper bound would have to use integrality beyond primitive near-critical clock geometry, an arbitrarily large minimum, and bounded individual gaps. Even if every sufficiently large integer candidate were excluded, a remaining finite-period class would require its own proof or effective cutoff.
