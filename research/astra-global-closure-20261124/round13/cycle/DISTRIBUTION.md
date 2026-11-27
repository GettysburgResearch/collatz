# Evaluating every divisor without factoring the word

**PROPOSED written theorem.** Use the uniform distribution on the finite set in (1) of the [main note](README.md), with its pinned state, physical edges and deterministic mask. There are absolute $a,c,K>0$ such that for every $g>1$ dividing $D$ and every residue $v$,

$$\begin{split}
 |\Pr(F(u)\equiv v\bmod g)-1/g|&\le K\exp[-cp/\ln(2g)],\\
 \Pr(F(u)\equiv v\bmod g)&\le K g^{-a}.
\end{split}\tag{4}$$

One may take $a=1/20$. The conclusions use no factorization hypothesis on $F$. They imply

$$\mathbb E\ln\gcd(D,F(u))=\sum_{\ell^e\mid D,\;\ell\ \text{ prime},\;e\ge1}\frac{\ln\ell}{\ell^e}+O(p e^{-c'\sqrt p}). \tag{5}$$

Thus even the full prime-power ledger has, in the mean, the logarithmic cost of a uniform residue, which is $O(\ln(2p))$. For the bounded branch $\ln D=p\ln3+O(\ln p)$ by [round 12](../../round12/cycle/README.md); at every fixed $\gamma>0$ the proportion with full gcd $\ge D^\gamma$ is at most $\exp[-a\gamma p\ln3+o(p)]$. The statement counts candidate rank polynomials individually, including reducible and irreducible words. It does not give the distribution *within* the irreducible subpopulation or within the least-disagreement basin.

## Independent interiors with legal boundary bands

In chronological order the rank sum is $W=\sum_{j<p}w_j c_{r_j}$, $w_j=3^{p-1-j}2^{B_j}$. This differs from $F(u)$ by a fixed unit modulo $D$. All results uniform in a target residue or frequency apply to both. The weights satisfy $3 w_{j+1}=2^{b_j}w_j$.

An edge allows staying in the current band, or falling by one at $b=1$ or rising by one at $b=2$. Every six successive edges contain at least two of each type: the number of twos is either floor or ceiling of $6(h/p-1)$, between 3 and 4. Both binary states 0 and 1 are allowed at every internal rank. For a feasible interval with a given start, greedily falling at the available falling edges until zero stays below every feasible path from that start (by induction), so honors any mask forbidding 2. Six edges suffice. The same argument backwards connects zero to a feasible right endpoint. Between binary states any prescribed pair can be connected over six edges, staying binary. A linear block decomposition avoids the pinned seam at time 0. Conditional on all exterior states, the interiors of disjoint blocks are independent uniform choices among their legal fillings, because the constraints are nearest-neighbor with fixed masks.

At any time $j$ at least 13 edges from either end, a block from $j-13$ through $j+13$ has two fillings with the same arbitrary feasible boundary states and differing only at $j$, where the alternative bands are 0 and 1. Put $k_{r_{j-1}}=2-b_{j-1}$ and $k_{r_{j+1}}=b_j-1$. Both middle choices work. Use six greedy and six binary edges on each side to connect the neighboring states to the boundary. These fillings change $W$ by $2w_j$, a unit modulo $g$. There are at most $2^{26}$ fillings since each edge has at most two choices.

## Escape of every nonconstant Fourier character

Fix a nonzero frequency $t\pmod g$, also when $t$ is a nonunit. At consecutive times take centered integer representatives $y_i$ of $2tw_i\pmod g$. Each is nonzero since $w_i$ and 2 are units. Set $L=\lceil\log_3 g\rceil$. If $|y_i|<g/8$ at $L+1$ successive sites, then $3y_{i+1}-2^{b_i}y_i$ is a multiple of $g$ of magnitude $<7g/8$. It vanishes. Iterating gives $3^L y_{i+L}=2^{B_{i+L}-B_i}y_i$, so $3^L\mid y_i$, impossible. Thus one time in every such interval has $g/8\le |y_j|\le g/2$.

Partition the time line of $p$ edges into disjoint intervals of $L+26$ edges, discarding the final remainder. Their possible middle sites at distance at least 13 from both ends consist of $L+1$ consecutive sites. Choose a large-phase time in each interval, possibly depending on $t$ but independent of the bands. Condition on all but the 26-edge interiors around the selected sites. In each interior the two specified fillings have probability at least $2^{-26}$ and their character values differ by angle of absolute principal value at least $\pi/4$. For a uniform list of $N$ unit complex values, the squared modulus of its mean is $1-N^{-2}\sum_{i,j}(1-\cos(\phi_i-\phi_j))$. Thus each conditional factor has modulus at most $\rho=\sqrt{1-2^{-51}(1-\cos(\pi/4))}<1$. Conditional independence and then the triangle inequality bound the unconditional character by $\rho^{\lfloor p/(L+26)\rfloor}$. Fourier inversion has a $1/g$ factor, yielding the first line of (4) with absolute constants. The proof uses deterministic time-dependent weights, constrained innovations, and composite moduli. It does not import a mixing theorem for independent increments. [Chung, Diaconis and Graham, *Random walks arising in random number generation* (1987), for the classical constant-multiplier comparison](https://doi.org/10.1214/aop/1176992088)

## A single erased interval for larger divisors

Keep the exterior and both ends of an interval of $m$ edges starting at $i$ fixed. The contribution of times $i,\ldots,i+m-1$, after removing the fixed unit $3^{p-i-m}2^{B_i}$, is

$$S=2^{2-k_{r_i}}\sum_{j<m}3^{m-1-j}2^{a_i+\cdots+a_{i+j-1}}.\tag{6}$$

Equivalently each term of $S$ is $3^{m-1-j}2^{B_{i+j}-B_i}c_{r_{i+j}}$. Since $B_{i+j}-B_i\le jh/p+1$ and $j\le p$, this shows $0<S\le8e^\delta m3^{m-1}<16m3^m$ at the stated slopes. When $16m3^m<g$, a prescribed residue of $W$ therefore fixes $S$ uniquely or is impossible. Divide by the fixed starting coefficient in (6). If $m\ge2$, subtract $3^{m-1}$ from the resulting carry: its exact binary valuation is $a_i$, since the next shorter carry is odd and positive. Divide by $2^{a_i}$ and repeat. At the final step the total physical clock is already fixed by the boundary bands and the block of $b$'s. Thus a residue selects **at most one filling of the interval for every specific exterior**. All exponents recover the bands successively. This argument gives uniqueness even for nonzero residues and shared prime powers.

Every feasible exterior with $m\ge24$ has at least $2^{\lfloor(m-12)/6\rfloor-1}$ fillings. Spend six edges at each end to and from zero as above. Partition the middle into six-edge pieces with arbitrary binary states at their internal boundaries, ending at zero and holding zero on any remainder. The fillings for different boundary choices are distinct. Choose the largest $m$ satisfying $16m3^m<g$ (handle bounded $g$ by enlarging $K$). Here $g\le D<3^p$, so $m<p$, and $m\ge\log_3 g-O(\ln\ln(2g))$. The binary choice exponent yields any fixed $a<(\ln2)/(6\ln3)$, in particular $1/20$. This proves the second line of (4) after averaging over exteriors. At full $D$ in the bounded branch, specifying the complement of such an interval leaves at most one filling and uses $O(\ln p)$ exposed edges; this is a finite decoder, not a uniform nonexistence result.

## The prime-power ledger

For $g=\ell^e\le e^{\sqrt p}$, the discrepancy from $1/g$ in (4) is $O(e^{-c'\sqrt p})$. Above that cutoff the probability and $1/g$ each satisfy such a bound using the second line. Summing all the errors with weights $\ln\ell$ costs at most $O(\ln D\,e^{-c'\sqrt p})$. This proves (5) by expanding the log gcd into its prime-power indicators. For the claimed main-term bound, prime powers up to $p$ cost at most $2\ln(p!)/p$, using $\lfloor p/q\rfloor\ge p/(2q)$ and the prime valuations of $p!$. Larger ones cost at most $(\ln D)/p$. Finally the number of divisors of $D$ is $\exp(o(\ln D))$: primes $\ell\ge2^{1/\epsilon}$ give $e+1\le2^e\le\ell^{\epsilon e}$, and the finitely many smaller primes contribute at most a fixed power of $1+\ln D$. Taking a union over divisors $g\ge D^\gamma$ in (4) gives the stated exponential tail. None of these estimates asserts that the exceptional set is empty.
