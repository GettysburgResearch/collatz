# Optimal temporal spectra, native valuation separation and the cost of independent clocks

Consider a positive primitive rational Collatz cycle of shortcut period $h$, odd period $p$ and complete reduced denominator $q$. Set $g=\gcd(h,p)$, $a=h/g$, $b=p/g$, $\gamma=\log_2 3$. Use a canonical cut, so $d_i=\lfloor ia/b\rfloor-E_i$ takes values in $[0,W]$, and write $c_i=2^{W-d_i}$. The active orders are precisely the Fourier orders present in some length-$g$ rank column $j\mapsto c_{i+jb}$, for $0\le i<b$. Let $J$ be their total totient degree. These definitions are invariant under re-rooting as in the [full denominator theorem](SPECTRAL_NEAR_OCTAVE.md). The number $q$ is odd and prime to three.

The following statements have three different scopes.

* Every primitive rational cycle has $J\ge1+\sum_{Q}\varphi(Q)$ over the full prime-power factors $Q$ of $g$, with arbitrary canonical width. Equality has the explicit frequency classification below.
* If the active orders separate into independent sets of prime coordinates, then differences in two separate coordinate directions have different dyadic valuations at every mechanical phase. This statement applies to genuine rational cycles after their common denominator is cleared.
* The size of the **integer** coordinates distinguishes $q=1$ from large rational denominators. Suppose $b\to\infty$, $a/b\to\gamma$, and $W=o(\log b)$. Partition the full prime-power factors of $g$ into independent blocks of products $G_1,\ldots,G_t$ as defined below. Uniformly, even for varying $t$,
\[
 \sum_{j=1}^t \frac{\log G_j}{\log(qbG_j)}
       \le H_2(1/\gamma)+o(1),\qquad H_2(1/\gamma)=0.9499555\ldots .    \tag{1}
\]
Here $H_2$ is binary entropy in bits. For ordinary cycles, $a/b\to\gamma$ and $b\to\infty$ already follow along growing least periods from distinctness of the odd states and irrationality of the logarithm ratio. Two independent blocks of sizes at least $b$ are therefore impossible along an unbounded sequence of ordinary cycles in this width range. If $\max_j G_j=b^{o(1)}$, then $g\le b^{H_2(1/\gamma)+o(1)}$, equivalently $g\le p^{H_2(1/\gamma)/(1+H_2(1/\gamma))+o(1)}$. These restrictions do not exclude integer cycles with a single interacting clock or with a larger width.

## All cycles and the equality cases

The power set $\{1,2,4,\ldots\}$ has unique unordered representations as a sum of exactly two members. Two unequal summands give their two distinct one-bits; equal summands give just one one-bit. In particular a sum of functions in two independent variables taking only powers of two can depend on at most one of the variables: a rectangle from two nonconstant summands would give a nontrivial equality of two pair sums. The same holds with more than two independent variables, by fixing the others. Multiplying the physical column by a fixed power of two has no effect on this fact.

The least joint temporal period is the least common multiple of the active orders, and equals $g$ by primitivity and the native affine fixed-point formula. Order one is present by positivity. For every full primary factor $Q$ with $\varphi(Q)\ge2$, assign it to an active order divisible by $Q$. Each such order has totient at least the product of the assigned totients, which is at least their sum. This proves the claimed degree lower bound except for a possible one-unit saving when $2\parallel g$.

If that saving occurs, every nontrivial active order is an odd full primary $Q$ or $2Q$, with exactly one choice per odd $Q$. Indeed there cannot be two distinct odd primaries of totient two, so no multi-primary group ties the charge bound. Any extra odd factor would increase an assigned totient. At least one doubled order must be present. Write $z=j\bmod2$ and $x_Q=j\bmod Q$. By Fourier inversion a column on the CRT product is then
\[
 c+\sum_{Q\text{ undoubled}} A_Q(x_Q)
      +(-1)^z\sum_{Q\text{ doubled}} B_Q(x_Q),
\]
where each component has mean zero. Holding parity fixed leaves every $x_Q$ free. The unique-pair-sum property allows at most one nonconstant odd component on a given column. For a doubled component the two parity values at each $x_Q$ have fixed sum $2c$. Thus they are a fixed unordered pair of powers; $B_Q$ takes two opposite nonzero values. Its mean cannot vanish on the odd-sized set of $x_Q$. The case $g=2$ simply requires order two. This proves the lower bound at every width.

There is a complete classification when equality holds.

1. If $g$ is odd or $4\mid g$, the active orders are exactly $1$ and the full primary factors $Q$. Every nonconstant physical column depends on exactly one $x_Q$.
2. If $2\parallel g$, order two is active. Each odd full primary $Q$ contributes precisely one of $Q$ and $2Q$. An undoubled column with a nonconstant $Q$-component depends only on $x_Q$. A column with a nonconstant $2Q$-component has two levels and the form
\[
                      c+e(-1)^z\sigma(x_Q),\qquad \sigma(x_Q)\in\{-1,1\},
\]
where $e\ne0$ and $\sigma$ has only order $Q$ after its mean is subtracted. Its nonzero mean supplies its own order-two component. Other columns can depend only on parity or be constant.

For odd $g$ the charge proof gives case 1 directly, followed by the pair-sum argument. For $2^e\parallel g$, $e\ge2$, an exact charge again forces one order per full primary, possibly doubled for an odd primary. The only possible grouping tie consists of $4$ and $3$, both of totient two, assigned to order $12$. Consider this exceptional candidate first. Its pure order-$12$ term $B(y,x)$, where $y\bmod4$ and $x\bmod3$, changes sign under $y\mapsto y+2$ and has mean zero over $x$ for each $y$. At a fixed parity on which $B$ varies, this pair of variables is independent of every other odd-primary term. The pair-sum argument excludes any such other nonconstant term in that column; every permitted individual odd term would vary on both parities. The two values paired by $y\mapsto y+2$ now have fixed sum. Thus $B$ takes just two opposite nonzero values, inconsistent with a zero mean on three inputs. Order $12$ cannot realize the tie.

In the remaining case the full even-primary term $A(y)$ has only order $2^e$. If an odd component is nonconstant, it varies on both parities and excludes all other odd components and any variation of $A$ within a parity. A parity-constant $A$ with only order $2^e$ is zero. Without $A$, a doubled odd component has the impossible fixed-sum, odd-size, zero-mean form above. This proves case 1. When $2\parallel g$ at equality, the nonconstant degree $J-1$ is odd, so order two must occur because all totients of orders exceeding two are even. Once its unit charge is removed there is again exactly one order $Q$ or $2Q$ per odd full primary. The order-two term can now add $a(-1)^z$ to a column. For an undoubled odd component, it is an independent summand and must vanish. For a doubled odd component the two parity values have fixed sum, and the resulting two levels give the displayed formula. The centered $\sigma$ has the prescribed order because no proper nonconstant divisor of $Q$ is active. This proves case 2.

All these choices of active orders are attained by primitive positive **rational** cycles in the high-minimum near-octave construction. For an undoubled $Q=\ell^e$ use the existing interval marker $1_{0\le j\bmod Q<Q/\ell}$. For a doubled odd $Q$ instead take the binary marker
\[
     \frac{1+(-1)^j(2\mathbf1_{\{0\le j\bmod Q<Q/\ell\}}-1)}2.
\]
The signed interval has nonzero mean since $\ell$ is odd, and its only nonconstant order is $Q$. Hence the twisted marker has exactly the nontrivial orders $2,2Q$. If $2\parallel g$ and no marker is twisted, use a separate parity marker. Each marker changes only its own disjoint two-site slot, and their least joint period is $g$. The physical height and least-period proof of the [independent-cell construction](INDEPENDENT_CLOCKS.md) uses only these facts and permits arbitrary indicator values in the slots.

## Independent coordinates and genuine native valuations

More generally, partition the full primary factors of $g$ into groups of products $G_1,\ldots,G_t$. Call them independent if every nontrivial active order divides one $G_j$. The finest such partition consists of the connected components of the graph joining two primary factors whenever an active order uses both their primes. Finite Fourier inversion expresses a rank column as a constant plus one summand per block. The pair-sum property shows each column actually varies in at most one block.

Use chronological base phase $i\in[0,b)$ and visit index $j\in\mathbb Z/g$. Define the integral labels
\[
                      y_i(j)=q\,2^{W-d_{i+jb}} x_{i+jb}.
\]
Their lowbits are exactly $c_i(j)$. They are pairwise distinct in each rank because their odd parts are the distinct numerators of physical odd states at the common denominator $q$. They are units modulo three by the odd update and $3\nmid q$. If $\beta_i=\lfloor(i+1)a/b\rfloor-\lfloor ia/b\rfloor$, then
\[
                 2^{\beta_i} y_{i+1}=3 y_i+q c_i.                      \tag{2}
\]
The visit index increases by one on passing from $i=b-1$ to $i=0$.

Each $y_i$ also splits additively over the blocks. For example, take the mixed difference between any two independent coordinates in (2); the mixed difference of the forcing is zero throughout. A full $p$-step turn multiplies the remaining difference by $3^p/2^h\ne1$ and returns to the initial rectangle, so it vanishes. The same argument works for arbitrary blocks of independent variables, or one may decompose into Fourier components. A one-block difference of $y$ consequently has an integer value independent of all the fixed coordinates and is nonzero for distinct block labels. In the $2\parallel g$ equality case above, conditioning on parity gives additive separation of all the *odd* axes. At a seam both parities flip together, preserving the rectangle. Their difference functions then have base-clock period dividing $2bQ$ for an odd full primary $Q$.

Fix any two different blocks and choose two values in each. At every reduced phase the four integer states have the form $y,y+A,y+B,y+A+B$ with $AB\ne0$. Their lowbits have the same additive rectangle equality. Necessarily
\[
                               v_2(A)\ne v_2(B).                        \tag{3}
\]
If the two valuations are both $s$ and $2^s\mid y$, two opposite corners have lowbit exactly $2^s$ and the other two have larger lowbits. Their diagonal sums disagree. If $2^s\nmid y$, all four lowbits agree, so (2) takes $A,B$ to $3A/2^{\beta_i},3B/2^{\beta_i}$. The equal valuations would decrease by at least one. Repeating cannot continue among nonzero integral differences. In particular the sets of dyadic valuations of *all* nonzero one-block differences at a phase are pairwise disjoint across blocks.

There is a ternary companion if at each rank distinct allowed lowbits have different residues modulo three. This holds, for example, when each rank permits only one value or two successive powers of two, as in the localized near-octave regime. Then the valuation sets at three are pairwise disjoint as well. If $v_3(A)=v_3(B)=0$, four corners with independent nonzero increments modulo three cannot all avoid zero: two two-element subsets of $\mathbb Z/3$ have full sumset. If both valuations equal $s>0$, all four corner values agree modulo three. Reducing (2) at the preceding rank shows all four preceding lowbits are congruent modulo three, hence equal by the hypothesis. Both preceding differences are then $2^{\beta}A/3,2^{\beta}B/3$, with equal valuation $s-1$. This reaches the excluded unit case. Both primes' conclusions hold also on fixed-parity slices whenever the slice remains a simultaneous rectangle through each step. Neither conclusion by itself is an integer-only restriction.

## Entropy cost of realizing the block coordinates with denominator $q$

For a block of size $G$, compare two values of its coordinate with all other coordinates fixed. Their difference $A$ evolves with
\[
                2^{\beta_i}A'=3A+q\,\delta c_i,\qquad |\delta c_i|\le2^W.
\]
This is independent of the other coordinates. After $b$ steps both block arguments increase by one. Over $G$ base circuits, their differences at the starting phase sum to zero and none vanishes. The sequence has a sign reversal at some step therein, so at the source of that reversal $|A|\le q 2^W$. Forward homogeneous subproducts over $n$ steps satisfy $3^n2^{-\sum\beta}<2$, since $\sum\beta>na/b-1$ and $2^{a/b}>3$. Unroll from the preceding reversal, at distance at most $bG$, to any desired date. This gives, uniformly in the other block sizes and in the physical maximum,
\[
                            0<|A|\le 4q2^W(bG+1).                      \tag{4}
\]
For a conditioned odd axis at $2\parallel g$, use $2bG$ in place of $bG$, since advancing two base circuits traverses an entire odd axis while restoring the parity. The constant factor is harmless below.

Let $t_G=\lceil\log_3(16q2^W(bG+1))\rceil+1$, doubling $bG$ in the conditional case. Distinct initial block labels have distinct projected lowbit words of length $t_G$ at every starting phase. Indeed, record the actual column value when this block controls it, and a fixed dummy symbol at all other dates. A coincidence makes $\delta c_i=0$ through the window after fixing the same other coordinates. Then $2^{\sum \beta}\mid A$ because $3^{t_G}$ is odd. But $2^{\sum\beta}>3^{t_G}/2$ exceeds (4).

At each starting base phase choose $j$ uniformly. The projected random words at that phase are independent across the blocks by CRT. Together they determine, and are determined by, the chronological lowbit word: the identity of the owner at every phase is fixed. Write $H_G(k)$ for the entropy in nats of the projected length-$k$ word, averaged over starting base phases. For parity slices also average over both starting parities. Shifts around seams preserve the uniform coordinate distribution and the averaged phases. Entropy subadditivity and monotonicity therefore give
\[
 H_G(t_G)=\log G,\qquad H_G(k)\ge\frac{\log G}{\lceil t_G/k\rceil}
                   \ge \frac{k\log G}{t_G+k}.                          \tag{5}
\]
The total average word entropy equals $\sum_G H_G(k)$, also when computed conditionally on the parity.

To bound it above, a native length-$k$ lowbit word specifies $k$ grades in $[0,W]$. Its first grade and the next $k-1$ positive division exponents recover the whole word on each fixed mechanical schedule. Their sum is at most $(k-1)a/b+W+1$. The number of positive $(k-1)$-tuples with total at most an integer $L$ is $\binom L{k-1}$. We obtain the finite bound
\[
 \sum_G \frac{\log G}{t_G+k}
 \le \frac{\log(W+1)+
       \log\binom{\lfloor(k-1)a/b+W+1\rfloor}{k-1}}{k}
                     \qquad(k\ge2).                                    \tag{6}
\]
Choose $k\to\infty$ with $W=o(k)$ and $k=o(\log b)$, which is possible in the stated range. The right side tends to $\gamma H_{\rm nats}(1/\gamma)=(\log3)H_2(1/\gamma)$. Uniformly in $G$ and $q$, $t_G+k=(1+o(1))\log(qbG)/\log3$. This proves (1). For $2\parallel g$ at equality one may apply (1) separately to all odd full primaries even in the presence of twists, losing only a bounded factor from the conditioned parity.

For ordinary cycles, the standard positive lap product gives $0<h-p\gamma=O(\log(2p))$ by distinctness of the odd states. Hence $a/b\to\gamma$. Bounded $b$ could not approximate this irrational limit. The proof uses no numerical logarithmic-form exponent for (1).

The entropy exclusion comes from the short sign-return bound for a *single independent coordinate* and the fact that all these demands use the same chronological word. Applying an orbit-wide polynomial height bound separately to each coordinate would discard this distinction. Earlier same-phase work proves the inversion count and, at canonical height at most two for ordinary integer cycles, the stronger exact condition $g=1$. The present argument permits arbitrary changes in a width growing more slowly than $\log b$. The single-block case can include every coprime integer cycle; inequality (1) alone cannot exclude that class. [Weaver and Wren, same-phase order](https://rstation.ai/problems/collatz/papers/114/v1) · [Earlier rational denominator order and same-residue comparisons](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/cycles/CLOCK_GCD_DENOMINATOR_ORDER.md)

## Variable rows, translated initial levels and a finite entropy certificate

There is a stronger version of (6) in which constant rows can attain wholly different dyadic levels. For each independent block of size $G$ let $L_G,U_G$ be the least and greatest base-two exponents of the lowbits on all **nonconstant rows owned by this block**, and $S_G=U_G-L_G$. Every nontrivial block has an owned row by joint primitivity. For the conditioned parity statement, take the union over both parity slices. Each forcing difference for this block is divisible by $2^{L_G}$. Unrolling its difference recurrence over $bG$ (or $2bG$) steps gives an odd determinant times the initial integer difference, with right-hand side divisible by $2^{L_G}$. Thus the initial difference, at every phase, is itself divisible by $2^{L_G}$. Apply the crossing and divisibility argument to the nonzero integer $A/2^{L_G}$. Its forcing is bounded by $q2^{S_G}$ and (4) and (5) hold with $S_G$ in the place of $W$ in their block-specific horizon $t_G$.

Write $H_0$ for the mean entropy of the initial lowbit given its base phase, and also given parity when using a slice. Let $f(\lambda)=\lambda\log\lambda-(\lambda-1)\log(\lambda-1)$, where $\lambda=a/b>1$. If a positive integer-valued variable has mean $\lambda$, its entropy is at most $f(\lambda)$: relative entropy against the geometric law of mean $\lambda$ is nonnegative. Choosing a uniform starting physical phase makes each native exponent in a stationary window have mean $\lambda$. Forgetting the conditioning only increases its entropy. Initial grade plus the next $k-1$ positive exponents determine the entire chronological lowbit word when the mechanical schedule is given. Using (5) therefore gives the **finite** alternative
\[
 \sum_G \frac{\log G}{t_G+k}
       \le\frac{H_0+(k-1)f(a/b)}k ,\qquad k\ge2.                        \tag{7}
\]
The same $H_0$ is charged only once across all blocks. A nonconstant rank owned by $G$ has at most $S_G+1$ possible levels, and a constant rank contributes zero entropy. Consequently (1) holds as written if $b\to\infty$, $a/b\to\gamma$ and $\max_G S_G=o(\log b)$, even with unrestricted global $W$. Choose $k\to\infty$ with $H_0=o(k)$ and $k=o(\log b)$, and use $t_G+k=(1+o(1))\log(qbG)/\log3$ uniformly in $G,q$. More generally, if $H_0=o(\log b)$ but the block spans vary arbitrarily, the same comparison with denominators $\log(q2^{S_G}bG)$ gives the corresponding version of (1). This permits expensive wide components alongside cheap narrow ones.

For a fixed nonzero whole-cell lag, let $N$ be the number of actual dates with unequal grades across the two trajectories. A sign crossing exists by cyclic zero mean. Only $N$ forcing terms survive in the transport up to any further date; each homogeneous subproduct is less than two. The crossing estimate consequently gives $0<|A_i|\le4q2^W(N+1)$ everywhere. A run of $l$ equal grades gives $2^{\sum\beta}\mid A_i$ and $2^{\sum\beta}>3^l/2$. Summing across the $N$ cyclic gaps yields $p\le N[1+\log_3(8q2^W(N+1))]$. The same proof on a single varying coordinate has $bG$ or $2bG$ in place of $p$ and its local span $S_G$ in place of $W$.

At global width $W\le3$ the following exact finite word count replaces $H_2(1/\gamma)$ in (1) by a constant **strictly below $4/5$**. For a mechanical schedule of 256 grades with increments $\beta$, count paths on $d\in\{0,1,2,3\}$ with $d'\le d+\beta-1$, the positivity condition $e\ge1$. Initialize every grade count to one and at each step sum admissible predecessors. The rationals $1054/665$ and $24727/15601$ bracket $\gamma$ by direct powering. For every $1\le j\le256$ both endpoints have the same integer part after multiplication by $j$. No intercept cut $-i\lambda\bmod1$, $0\le i<256$, collides with another as the slope varies strictly between these endpoints. Their order and mechanical word on each half-open cell are fixed. Enumeration at the rational midpoint, including every left endpoint, gives the maximum over all schedules
\[
 M=30013844518446162257479163335820425359071383513610694141189298339493379000104270721076884405485568,
 \qquad M^5<3^{4\cdot256}.
\]
Thus the entropy of a chronological $k$-grade word given its phase is at most $\lceil k/256\rceil\log M$ by partition into blocks; a shorter final word can be extended along its native itinerary. Combining with (5) and $k\to\infty$, $k=o(\log b)$ gives (1) with $\theta_3=\log_3(M)/256<4/5$. The native integer excludes two independent $G$'s of size $b^{2/3}$ or greater along any unbounded width-three sequence: two contributions of $2/5$ already exceed the strict ceiling. For $W\le2$ the earlier exact phase-order theorem gives $g=1$.

[Exact replay](check_primary_spectra.py) covers 620,010 scalar words on the three-level alphabet $\{1,2,4\}$ at ten periods through 12 and closes their actual frequency sets under unions of columns. It also checks 38 positive primitive rational cycles, including every parity-twist choice on the listed gcds, 19,456 normalized native labels, 1,064 exact projected-entropy factorizations, and the width-three transfer matrix certificate. The physical fixtures have widths one and four. [Archived exact controls](../../../reports/astra-infinite-descent-20261127/cycles/PRIMARY_SPECTRA.json)
