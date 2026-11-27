# A single rational source interval amplifies an ordinary counterexample

Use the one-division shortcut \(T(x)=x/2\) at an even numerator and \(T(x)=(3x+1)/2\) at an odd numerator, on nonnegative rationals of odd reduced denominator. Each is a dyadic integer so the parity is well-defined. Let \(g_i(x)\) count its first \(i\) odd departures, and let \(W_\ell(x)\) mean \(8g_i(x)\ge5i\) for every \(0\le i\le\ell\). Fix \(j\ge1,\ n=8j,\ Q=2^n,\ q=3^{5j}\). For \(L\ge0\) put
\[
 D_{j,L}=\#\{a\in\mathbb Z:Q/2\le a<7Q/2,\ (a,6)=1,\ W_{n+L}(a/q)\},
 \qquad P_{j,L}=D_{j,L}/D_{j,0}.                                    \tag{1}
\]
These are finite computations. The numerator interval and the reduced denominator in (1) are fixed independently of any unknown integer. The additional \(L\) clocks continue the original prefix gate from time zero, retaining the accumulated excess.

**Written theorem.** The following are equivalent:
\[
 \begin{split}
 &\text{every positive integer reaches one};\\
 &\lim_{L\to\infty}\sup_{j\ge1}P_{j,L}=0;\\
 &\lim_{L\to\infty}\liminf_{j\to\infty}P_{j,L}=0.                   \tag{2}
 \end{split}
\]
A failure of ordinary Collatz would give \(\liminf_{j\to\infty}\inf_{L\ge0}P_{j,L}>0\). Thus one ordinary bad input produces a positive *conditional fraction* in an increasing population, for arbitrarily long continuation. The conditioning is essential: the proportion passing the initial gate among all allowed numerators already tends to zero. Statement (2) is an equivalence; extinction at this scale remains open.

## Exact denominator, populations and endpoint bounds

For a binary word \(w=(\epsilon_0,\ldots,\epsilon_{n-1})\), write \(g=\sum\epsilon_i\) and
\[
 C_w=\sum_{\epsilon_i=1}2^i3^{\sum_{h>i}\epsilon_h},\qquad
 F_w(x)=(3^g x+C_w)/2^n,\qquad B_w=C_w/2^n .
\]
Each word has one dyadic residue for its source modulo \(Q\). Multiplication by the fixed odd \(q\) gives one numerator residue. For every word passing the gate the initial bit is odd. The half-open interval in (1) contains three lifts of that odd residue, separated by \(Q\). Exactly two are nonmultiples of three. Thus \(D_{j,0}\) is **twice the number of binary words passing the gate** and is positive. This identity is independent of ternary mixing or any conjecture.

At clock \(n\) a passing word has \(g=5j+k,\ k\ge0\). Each odd departure removes at least one remaining denominator factor three, and even departures retain odd denominators. Therefore \(T^n(a/q)=z\) is an ordinary positive integer, explicitly
\[
                         z=3^k a/Q+B_w .
\]
We claim
\[
                 0\le B_w<25\cdot3^k,\qquad 1\le z<29\cdot3^k .
                 \tag{3}
\]
At \(k=0\) the positions of the \(5j\) odd symbols are each at most their positions in the word with minimal allowed prefix counts \(\lceil5i/8\rceil\). This extremal word is \((11011010)^j\), whose single-block offset is \(319/256\) and gain \(243/256\). Hence \(B_w\le(319/13)(1-(243/256)^j)\). At \(k>0\), the contributions of the earliest \(5j\) ones are bounded by \(3^k\) times that extremal offset. The final \(k\) ones add at most \(\frac12\sum_{h<k}3^h=(3^k-1)/4\). Since \(319/13+1/4<25\), this proves (3). The allowed future condition from \(z\) is \(5i\le8g_i(z)+8k\) for every \(i\le L\).

## The size and excess tail of the conditioning population

Write \(p=5/8,\ \mathcal H=-p\log_2p-(1-p)\log_2(1-p)\), and \(B_{n,k}\) for the count of passing words with final excess \(k\). Cyclic rotation of any length-\(n\), grade-\(pn\) word at a global minimum of \(8g_i-5i\) yields a passing word. Thus
\[
 B_{n,0}\ge n^{-1}\binom n{pn}\gg2^{\mathcal H n}n^{-3/2}.
 \tag{4}
\]
There is an absolute upper bound
\[
          B_{n,k}\ll (k+1)(3/5)^k\,2^{\mathcal H n} n^{-3/2}.
          \tag{5}
\]
Here are details, including constants for the tail application. Under independent Bernoulli \(p\) bits, let \(S_i=8g_i-5i\); the centered increments are \(+3,-5\) and variance \(15\). The event counted by \(B_{n,k}\) requires \(S_i\ge0,\ S_n=8k\). The probability of each such word is \(2^{-\mathcal H n}(5/3)^k\).

For this centered walk, survival for \(t\) steps from \(x\ge0\) has probability at most \((x+5)/\sqrt t\) for all sufficiently large \(t\), uniformly in \(x\). For the walk with reversed signs use \((x+3)/\sqrt t\). Indeed, start inside \([0,M)\), stop at the first exit \(\tau\), and take \(M=\lceil\sqrt{15t}\rceil\). For a downward overshoot bound \(b\) and an upward bound \(c\), the quadratic \((s+b)(M+c-s)\) is nonnegative before and at exit, and its expected one-step decrement before exit is \(15\). Truncation gives \(\mathbb E\tau\le(x+b)(M+c)/15\). The stopped linear martingale gives \(\Pr(S_\tau\ge M)\le(x+b)/(M+b)\). Surviving \(t\) steps requires an upper exit or \(\tau>t\). The sum of the two bounds divided by \((x+b)/\sqrt t\) tends to \(2/\sqrt{15}<1\); for \(x\ge M\) the assertion is immediate.

Split a length-\(n\) word into three blocks of lengths each at least \(n/4\), for large \(n\). The first block must survive from zero. Reversing the last block and negating its increments gives an independent walk surviving from \(8k\). Given both outer blocks, the middle block has one specified total. Stirling's formula bounds the maximum binomial atom of length \(t\) by \(2/\sqrt t\) for all sufficiently large \(t\), and gives \(\Pr(S_n=0)\ge1/(2\sqrt n)\). Independence and (4) therefore imply, uniformly for \(k\ge0\) and sufficiently large \(n=8j\),
\[
      \frac{B_{n,k}}{\sum_\ell B_{n,\ell}}
           \le160(8k+3)(3/5)^k.                                    \tag{6}
\]
In particular \(D_{j,0}\asymp2^{\mathcal H n}n^{-3/2}\). The loose constant in (6) comes from bounding the three factors by \(10/\sqrt n,\ 2(8k+3)/\sqrt n,\ 4/\sqrt n\). This derivation uses the Bernoulli tilt for counting binary words; the numerator law in (1) remains uniform on the stated finite population.

If Collatz is true, fix \(K\). By (3), every source with \(k\le K\) is at an ordinary integer bounded by \(29\cdot3^K\) at time \(n\). Each of that finite set reaches the cycle \(1,2\), and even with slack \(8K\) eventually fails the continuation gate. One finite \(L(K)\) suffices for all \(j\). The summable tail of (6) handles the other sources. Finitely many small \(j\) omitted from (6) each have a finite population whose members clear the denominator by \(n\), so they can also be killed by one finite additional horizon. Sending \(K\to\infty\) proves the second statement in (2).

## The lower fraction from one ordinary component

If some positive integer is bad, let \(m\) be the least such integer. The [binary minimum theorem](../BinaryPrefixCriterion.lean) gives \(m\ge33\). Every forward state of every bad \(y\) is at least \(m\). The same one-step fifth-power bound as in that theorem gives, for every \(u\),
\[
 2^{5u}m^5\le2^{8g_u(y)}y^5,\qquad
 g_u(y)\ge p\big(u-\log_2(y/m)\big).                                \tag{7}
\]
In particular for a bad \(y\in[2^H,2^{H+1})\), the additional slack \(pH\) permits its entire real forward word: use \(m\ge2\) in (7). This applies to every bad start in the octave.

Fix such a \(y\) large enough for the absolute real bound below. At \(n=8j\), set \(t=n-H\). We construct words of length \(t\), of total grade exactly \(5j\), that land at \(y\) from sources in (1). Choose one of two fixed last blocks \(v=11111000\) or \(11110100\). Both pass the \(p\)-gate and have grade five. Prepend any word of length \(t-8\) and total \(5j-5\) passing at every prefix the *steeper* slope
\[
                       p_j=(5j-5)/(8j-H-8).
\]
For fixed \(H\) and all sufficiently large \(j\), \(p\le p_j\le17/27<\log_3 2\). All concatenated prefixes pass the original gate. At time \(t\) their surplus is \(5j-pt=pH\).

For the steep core, each suffix of length \(s\) has grade at most \(p_js\), by equality at the terminal and the lower prefix constraints. Hence its affine offset is at most \(\frac12\sum_{s\ge0}(3^{17/27}/2)^s=:C_0<\infty\). The fixed last block has gain \(243/256<1\) and offset at most \(319/256\). Thus \(0\le B_w<C_*:=C_0+2\) uniformly in \(j,H,y\) in the indicated range of \(j\). A source
\[
                         a=2^t y-C_w,\qquad x=a/3^{5j}              \tag{8}
\]
has \(a/Q=(y-B_w)/2^H\in[1/2,2)\) when \(y\ge2C_*\). The binary inverse branches \(s\mapsto 2s\) and \(s\mapsto(2s-1)/3\) force the exact indicated parity bits over odd denominators. All intermediate values are positive: every suffix offset at the common terminal is a subsum of \(B_w<y\). The initial numerator is odd, since the first bit is one. If the last odd position is \(i\), zero-based, then \(a\equiv2^i(2^{t-i}y-1)\bmod3\). The last two blocks have \(t-i=4,3\) respectively. Choose the second if \(y\equiv1\bmod3\), the first otherwise. Thus \((a,6)=1\), with the full reduced denominator \(3^{5j}\). After landing at \(y\), (7) and the surplus \(pH\) give all later gates.

Different words give different source numerators by determinism. At fixed \(H\), distinct target integers also give disjoint sources because the landing time \(t\) is the same. Rotating at a minimum of the centered walk for the steep slope supplies at least \(\binom{n-H-8}{5j-5}/(n-H-8)\) cores. At fixed \(H\),
\[
 \frac{\binom{n-H-8}{5j-5}}{\binom{n}{5j}}
       \longrightarrow p^5(1-p)^{H+3}.                              \tag{9}
\]
This follows by cancelling factorials, equivalently sampling a prescribed set of five ones and \(H+3\) zeros without replacement. Combine (4), (5), Stirling and (9). If \(\mathcal B_H\) denotes the bad ordinary integers in \([2^H,2^{H+1})\) and \(2^H\ge2C_*\), there is an absolute \(c>0\) such that
\[
       \liminf_{j\to\infty}\inf_{L\ge0}P_{j,L}
         \ \ge\ c\,\#\mathcal B_H\,(3/8)^H .                       \tag{10}
\]
For any hypothetical bad \(m\), an ordinary multiple \(2^s m\) is bad and lies in an octave satisfying the height condition. This proves the reverse implication in (2). Using the least such \(s\), (10) gives a lower bound \(\gg(m+1)^{-\log_2(8/3)}\) with an absolute constant. The construction never assumes that an arbitrary positive rational is ordinary; it lands exactly at the given integer (8).

## What the upper tail proves without assuming Collatz

Let \(m\) be the least bad integer if it exists. Formula (3) and the finite extinction of all good endpoints below \(m\) bound the left side of (10) from above by
\[
             \ll (1+\log m)m^{-\log_3(5/3)}.                        \tag{11}
\]
For each fixed bound on \(k\), good endpoints can be killed after finitely many additional clocks. This is a qualitative eventual statement and supplies no explicit value of \(L\). In particular the published verification below \(2^{71}\) covers \(29\cdot3^{41}<2^{71}\). Formula (6) gives the source-qualified bound
\[
  \lim_{L\to\infty}\limsup_{j\to\infty}P_{j,L}
    \le160\sum_{k\ge42}(8k+3)(3/5)^k
    <0.000068.                                                       \tag{12}
\]
The cited verification was not rerun here. [Barina, The Journal of Supercomputing 81 (2025), article 810](https://doi.org/10.1007/s11227-025-07337-0)

The single-seed lower exponent is \(\alpha=-\log_2(1-p)\), while the upper excess exponent is \(\beta=\log_3(p/(1-p))\). At \(p=5/8\), their difference is about \(0.950064\). A local lower population on the order of \(m^{\alpha-\beta+\varepsilon}\) in an octave comparable to the least \(m\), together with uniform effective constants and a sufficiently large minimum, would dominate (11). No such ordinary population theorem is established. For varying slope \(p\in(1/2,\log_3 2)\) the difference satisfies
\[
 (\alpha-\beta)'=\frac{p-\log_3 2}{p(1-p)\log 2}.
\]
Its infimum is attained in the limit \(p\uparrow\log_3 2\) and equals \(H_2(\log_3 2)\). Optimizing the scalar mean alone reaches the ordinary entropy dimension again.

There is also a sharp cost at the *native* endpoint. If the actual word of \(y\) in the \(H\) clocks after landing has \(k\) odd departures, then the final grade is \(5j+k\). The probability of precisely this final \(H\)-word under the counting tilt is \(p^k(1-p)^{H-k}\). Its product with the excess factor is
\[
                [(1-p)/p]^k\,p^k(1-p)^{H-k}=(1-p)^H.               \tag{13}
\]
Thus the cost in (10) is already the cost of one compatible suffix. An unconditional endpoint cancellation which is required to beat this native contribution would discard a physically present positive summand. The present handle is the nonzero *population fraction* and the explicit ordinary endpoint bound at each excess, not a proof of full extinction.

The [two-height test](TWO_SIGNED_HEIGHTS.md) recovers reduced-denominator information from signed congruences. Here the denominators are restricted from the outset to powers of three, so they clear on the common clock. PR193's [pointwise rational Green proposal](https://github.com/GettysburgResearch/collatz/blob/b69d47f7fc0a8c6c3f227b0afcaf69b28cc92845/research/astra-six-hour-20261127/root/RATIONAL_GREEN.md) instead uses rational weights on *ordinary integer* predecessors; its fixed time tilt imposes an additional hitting-time constraint. The present relative-count criterion is equivalent to Collatz and uses varying rational *sources*. PR192's [marked ordinary predecessor trace](https://github.com/GettysburgResearch/collatz/blob/75eac0cbc744469ae2886bc2f140685c484e9fe7/research/astra-sixhour-20261127/transport/MARKED_TRACE.md) concerns different source grades and weights. Neither provides the missing extinction in (2).


The [Lean kernel](RationalSourceSector.lean) proves the affine identity directly for the fixed-denominator shortcut recursion, actual denominator clearance at the specified grade, the shifted floor inequality, the ternary lift classes, the native suffix cost and the integer numerical inequalities. The probability estimates, population amplification and equivalence (2) are written proofs. The [exact control](check_rational_sector.py) enumerates the complete binary word sectors at \(j=1,2,3\), independently scans every reduced rational source at \(j=1,2\), and directly executes three prescribed positive rational histories at \(j=350\) to integer targets in all three ternary classes. The continuation census uses displayed finite horizons only. [Retained output](RATIONAL_SECTOR_CONTROLS.json)

