# A \(6/5\) distortion bound and unpadded original-source lifting

**PROPOSED.** On every finite simple positive shortcut trajectory,
\[
 \sum_{\substack{v\ \mathrm{departed\ odd}\\ v\ge2^{71}}}\frac1v
       <\frac{53}{100}.                                                  \tag{1}
\]
In particular, if all its odd departures are at least \(2^{71}\), its exact multiplicative correction satisfies
\[
 1\le D_j(n):=\frac{2^j T^j(n)}{3^{P_j(n)}n}
     =\prod_{\rm odd\ departures\ v}\left(1+\frac1{3v}\right)<\frac65.    \tag{2}
\]
A finite segment is simple when its departed states are pairwise distinct. The numerical height \(2^{71}\) in (1) is an explicit cutoff for a combinatorial estimate. Applying it to a putative nonbasin uses the independently published verification below this cutoff. The proof of (1) itself uses no verified convergence range. [Bařina, *Improved verification limit for the convergence of the Collatz conjecture*, 2025](https://doi.org/10.1007/s11227-025-07337-0)

## Counting the entries of a single finite simple segment

After any odd departure, the next state is a ternary unit; unit status subsequently persists. Thus there is at most one odd multiple of three on the entire segment. An initial segment before that first odd departure contains only even states. For the remaining count use a simple segment of ternary units.

Fix \(h\ge0\). For every interval of \(3\cdot2^h\) consecutive positive integers, let \(Q_i(h),O_i(h)\) be uniform upper bounds on the number of entries of the same simple unit segment, counting all and odd entries respectively, after \(i\) rounds of the estimate below. Initialize \(Q_0(h)=O_0(h)=2^{h+1}\). These bounds hold because exactly two of every three consecutive integers are ternary units.

For \(h>0\), discard at most \(h\) terminal indices, so all remaining starts have their \(h\)-step endpoint among the pairwise distinct states. Each parity word of length \(h\) specifies one residue modulo \(2^h\). In a \(3\cdot2^h\)-wide interval the three lifts include precisely two units. The grade-\(p\) population has size at most \(2\binom hp\), or \(2\binom{h-1}{p-1}\) for odd starts. The latter bound is zero when \(p=0\).

The \(h\)-step endpoints at that grade lie in an interval of at most
\[
    w=3\cdot3^p+\lfloor(3/2)^h\rfloor+2
\]
integers. Indeed their leading coefficient is \(3^p/2^h\), and the additive correction belongs to \([0,(3/2)^h-1]\) by induction on the clock. Distinctness gives an independent cap of \(U(w)=2\lfloor w/3\rfloor+\min(2,w\bmod3)\) eligible output integers. If \(b\) is the least nonnegative integer with \(w\le3\cdot2^b\), the *same simple segment* gives another cap \(Q_{i-1}(b)\). In the finite table use this latter cap only when \(b\le959\). Let \(V=\min(U(w),Q_{i-1}(b))\) with this convention. The next all-entry bound is the smaller of the previous \(Q_{i-1}(h)\) and
\[
                h+\sum_{p=0}^h\min\!\left(2\binom hp,V\right).
\]
Replacing \(\binom hp\) by \(\binom{h-1}{p-1}\) gives the odd-entry bound, again retaining any better previous value. Set both bounds at \(h=0\) to two. This recurrence counts actual positions on one simple path. Each fixed clock is injective on its nonterminal chronological indices even though the map on arbitrary positive starts is many-to-one.

For \(69\le h\le959\), subdivide the octave \([3\cdot2^h,6\cdot2^h)\) into eight consecutive intervals of width \(3\cdot2^{h-3}\). Divide the odd count in each by its least possible integer. The sum of the resulting reciprocal bounds over these octaves is at most
\[
       \left(\sum_{j=8}^{15}\frac1j\right)
       \sum_{h=69}^{959}\frac{O_4(h-3)}{3\cdot2^{h-3}}
           <\frac{13}{25}.                                               \tag{3}
\]
The table evaluates (3) in rational arithmetic. The first through fourth rounds give upper bounds \(1.472746, 0.697859, 0.550779, 0.515938\), respectively, rounded upward in millionths. The first octave starts at \(3\cdot2^{69}<2^{71}\), as required for an upper estimate. [Exact recurrence and integer guards](check_distortion.py) · [Replay receipt](../../../reports/astra-sixhour-20261127/descent/distortion-finite.json)

For \(h\ge960\), let \(b=(5/4)/(3/2)^{3/5}\), \(a=3^{3/5}/2\). In a whole octave, grade \(p\ge3h/5\) contributes at most \(b^h\) to the reciprocal sum by the binomial exponential moment at \(3/2\). Each length-\(h\) word occurs at most three times, and the denominator is at least \(3\cdot2^h\). For \(p<3h/5\) sum the endpoint counts \(3\cdot3^p+\lfloor(3/2)^h\rfloor+2\) and the at most \(h\) discarded terminal indices. After division by \(3\cdot2^h\), this gives at most
\[
 \tfrac32 a^h+(h+1)(3/4)^h+(h+1)2^{-h}.
\]
Both \(b^{40},a^{40}<1/2\) by the exact integer comparisons in the checker. Also \(h+1\le2^{h/8}\) for \(h\ge960\), and \((3/4)^4<1/2\). The total is at most \(6\cdot2^{-\lfloor h/40\rfloor}\) per octave. The geometric tail is at most \(480/2^{24}\). This, (3), and at most \(2^{-71}\) for the possible initial odd multiple of three prove (1). Finally \(\log D_j\le(53/100)/3<9/50\le\log(6/5)\), using \(\log(1+x)\ge x-x^2/2\) for \(x=1/5\).

The preceding uniform finite-segment estimate \(480M^{-1/80}\) already implied the absolute boundedness of the reciprocal sum and its decay as the floor \(M\) grows. The sharper explicit estimate here combines the parity-word cap, grade-specific endpoints, ternary units, their recursive occupancy on the same segment, and short weighted subintervals. The distinction matters at the actually verified height. [Earlier reciprocal estimate, PR195](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-global-closure-20261124/round12/arithmetic/README.md)

## Consequences for a fixed upper certificate

Assume \(z\) is a nonbasin source and \(T^H(3z)=1\) with grade \(r\). Suppose the lower prefix through \(H\) is simple. This includes every non-eventually-periodic lower at every \(H\). All lower states exceed the published verification floor. At any matched clock \(j\) in this prefix, put \(p=P_j(z)\), \(u=P_j(3z)\). The exact relation is
\[
 \frac{T^j z}{T^j(3z)}=3^{p-u-1}\frac{D_j(z)}{D_j(3z)} .
\]
If \(p\le u\) then this ratio is less than \(2/5\), using \(D_j(3z)\ge1\). Thus at any clock with \(T^j z\ge(2/5)T^j(3z)\), the lower has already paid strictly more odd departures. In particular at \(H\) it has paid at least \(r+1\). The true, unpadded upper word itself now clears its entire signed denominator at the clock \(t\le H\) of the \((r+1)\)-st lower odd departure. [Exact lift upon reaching the required grade](SignedCenter.lean)

Moreover let \(m\) be any proved lower bound for all states on this lower prefix. Since \(n=T^t z=2^{H-t}D_t(z)/D_H(3z)\), we have
\[
          m\le n<\tfrac65\,2^{H-t},\qquad
          H-t>\log_2(5m/6).
\]
In the least canonical reverse-disagreement setting the quantitative return gives \(m=z/2^{40}\) as a valid real lower bound. This leaves a binary reserve larger than \(\log_2 z-41\) at the actual first complete ternary exit. If the unpadded exit \(c=n-2^{H-t}\) is positive, then \(c<n/6\). If the lower remains simple through \(H+2\), append just one physical upper lap, paying \(H+2\) clocks and \(r+1\) odds in total. Its upper correction gains exactly \(4/3\), so the ratio at its paid lower exit obeys \(n/2^{H+2-t}<9/10\). Consequently that full signed center has a **strictly negative** integral exit at the original source. On lower prefixes containing a repeat, the all-rank result using \(r\) upper laps remains available. [PR197, bounded return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean) · [All-rank padding](UPPER_WORDS.md)

The existence of the real Euler-product limit on each fixed injective orbit is earlier work. The estimate below supplies its explicit uniform comparison at the verified height. [Prior real and dyadic limits, PR195](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-global-closure-20261124/closing/adelic/README.md)

For a nonperiodic nonbasin \(v\), the monotone product \(D_j(v)\) converges to \(D_\infty(v)\in[1,6/5]\). Hence \(K(v)=vD_\infty(v)\) is a positive real function on every such component, satisfying \(K(Tv)=3^{v\bmod2}K(v)/2\). If ordinary pairs of words from \(z,y\) meet in this component and \(K(y)=\lambda K(z)\) for their exact relative leading coefficient \(\lambda\), then \(\lambda<5/6\) guarantees \(y<z\). This criterion pays for additive offsets at arbitrary merger clocks. The argument still needs a positive smaller canonical \(y\) in the requisite lower component with a good triple, or an independent return below the original floor. The signed binary reserve and the function \(K\) alone give neither occurrence.
