# Positive prime flows and an integer rounding control

**Status.** Written results with a Lean arithmetic interface and exact finite controls. The first proposition applies to a genuine positive integer cycle. The construction shows which of its arithmetic restrictions can hold for integer flows whose tripling commands fail the ordinary parity condition.

## The flow of a genuine cycle

Let $c(n)$ be the positive integer left after removing all factors of 2 and 3 from $n$. Give every odd positive $n$ the edge $c(n)\to c(n+1)$ of multiplicative length $(n+1)/n$. Work with the shortcut branches $T_0(x)=x/2$ and $T_1(x)=(3x+1)/2$ on their actual integer parities. In the companion coordinate $s=x+1$, the odd branch gives $2s'=3s$ and the even branch gives $2s'=s+1$.

**Proposition.** On a nontrivial primitive positive ordinary cycle of native length $A$, grade $m$, and largest odd state $M$, the even states $x$ in their cyclic order give a closed walk of $A-m$ edges indexed by $n=x+1$. Every index is odd, belongs to $0$ or $2$ modulo 3, and occurs just once. Every core vertex lies strictly below $M$, and
\[
                    \prod_{x\text{ even}}(1+1/(x+1))=2^A/3^m.
\]
Indeed all phases are prime to 3, since one odd step leaves a nonzero ternary residue and all following steps preserve it. Tripling and exact halving preserve $c$, which connects consecutive charged edges. The product follows by telescoping $s'/s$. In the chain of evens after an odd state $v$, the first even $x=(3v+1)/2$ has $c(x+1)=c(v+1)\le(v+1)/2<M$. Subsequent even $x$ satisfy $x+1\le(3M+1)/4+1<M$ when $M>5$. For $M\le5$, direct iteration of odd states $1,3,5$ reaches one.

Any nonempty closed subwalk in this graph of odd indices has product $2^a/3^b>1$, where
\[
 a=\sum v_2(n+1)>0,\qquad b=\sum\bigl(v_3(n)-v_3(n+1)\bigr)\in\mathbb Z.
\]
Closure cancels every other prime. On a closed full walk with product $2^A/3^m$, $a=A$ on the whole walk. A proper closed subwalk therefore has $0<a<A$ and $1<2^a/3^b<2^A/3^m$. In particular, if $2^A/3^m$ is the least ratio greater than one among $2^u/3^v$ with $1\le u\le A$ and $v\in\mathbb Z$, then all core vertices before the final return are distinct. More generally each proper return gives two positive defects that add to the original $A\log2-m\log3$.

## Integer walks at all near-critical clocks

Take every sufficiently large $m$, and set $A=\lceil m\log_2 3\rceil$, $N=2^A$, $P=3^m$, $D=N-P$, and $B=2m-A$. There exists a binary command word $w$ of native length $A$, grade $m$, with a positive integer walk satisfying all of the following.

1. Each command 1 triples the present integer before a ceiling halving. Each 0 performs just a ceiling halving. The integer walk closes, and its charged odd pre-halving indices connect into a prime-to-six core walk as above. All charged $n$ are $0$ or $2$ modulo 3. Their length product is exactly $N/P$.
2. Every charged index lies in $[P/D,48mN/D]$. All core sources are distinct at the least positive defects described in the proposition. The upper bound is polynomial in $m$ with an absolute exponent, including at these defects.
3. Every nonidentity native rotation of $w$ has Hamming distance at least $B/2-4$ from $w$. The phase of the genuine ordinary **rational** cycle having word $w$ has complete reduced denominator $q\ge\sqrt D$. Consequently $q$ grows exponentially in $A$.

The edges in item 1 are integral. The rational ordinate in item 3 belongs to the ordinary affine branches of the same word. A true ordinary cycle requires each tripling command to occur exactly when the companion integer is even, which forces precisely $A-m$ charges. The construction imposes neither this equality of counts nor this alignment.

**Balanced clocks.** Put $k=\lfloor m/2\rfloor$ and $\epsilon=m-2k$. Make $k$ pairs of odd gaps. At pair $j$ (from zero) use a free pair when $\lfloor(j+1)B/k\rfloor>\lfloor jB/k\rfloor$. Each free pair can be $(1,2)$ or $(2,1)$. Each remaining pair is $(2,2)$. If $\epsilon=1$ append a single 2. This gives $B$ free choices and positive gaps $a_i\in\{1,2\}$ of sum $A$. Here $1\le B\le k$ for all sufficiently large $m$. In a prefix of $2j$ gaps the clock is $4j-\lfloor jB/k\rfloor$, which differs from $2jA/m$ by a quantity in $[-1/2,1)$. An odd prefix adds at most one in either direction to this error, and the full error is zero. Thus every cyclic interval of $t$ complete gaps has total clock greater than $tA/m-4$ and its homogeneous multiplier $3^t/2^{\sum a_i}$ is below 16.

**Rounding and arithmetic.** For the prescribed gaps iterate $z\mapsto\lceil3z/2^{a_i}\rceil$ on positive integers. Over a whole lap the error from the homogeneous multiplier $P/N$ is strictly less than $16m$ by the suffix estimate. The lap map $F$ is monotone, $F(1)\ge1$, and $F(K)\le K$ for $K=\lceil16mN/D\rceil$. Monotone iteration from 1 thus gives an integer fixed point. Applying the same affine inequality to the resulting walk at every rotated gap gives $z_i<16mN/D$. The macro step can be implemented with $a_i$ successive ceiling halvings following one exact tripling, since iterated ceiling division gives ceiling division by the product. The first pre-halving index is $3z_i$. If a second halving is used its input is $\lceil 3z_i/2\rceil$, equal to $0$ modulo 3 for even $z_i$ and $2$ modulo 3 for odd $z_i$. Only an odd input $n$ produces the factor $1+1/n$. All other operations preserve the prime-to-six core. Multiplication of the realized steps gives the exact factor product $N/P$, so every charged $n\ge P/D$ and the upper bound follows from $n\le3z_i$. Lagarias's Lemma 2.2(1) gives $\Lambda=A\log2-m\log3\ge(\log3)/(1200 A^{13.3})$. Because $0<\Lambda<\log2$, $D/N=1-e^{-\Lambda}\ge\Lambda/2$. This yields both the polynomial upper height and $D\ge c2^A/A^{13.3}$. [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

**Rotational distances.** Write each gap as the native command $1$ followed by $a_i-1$ zeros. The free pairs are the strings 110 or 101. Choose their orientations independently with equal probability. At each of the $2B$ varying positions comparison with the position at nonzero displacement $d$ disagrees with probability at least $1/2$. Its partner in the same free pair is always opposite, while constants or other coins give probability $1/2$. Thus the expected Hamming distance is at least $B$. Changing one coin changes at most four comparisons. Revealing the coins one by one gives a conditional expectation martingale whose single-step increment takes two equally likely values $\pm u$, $|u|\le2$. The conditional exponential moment is bounded by $\cosh(2t)\le e^{2t^2}$. Multiplying the bounds and using Markov's inequality gives probability at most $e^{-B/32}$ for distance below $B/2$ at a particular shift. Since $B$ grows linearly in $m$, the union bound over the $A-1$ shifts is below one eventually. Fix a successful orientation and also consider the word after flipping its first free pair. Both have minimum rotational distance at least $B/2-4$.

**Actual denominators.** For a word $u$, write its closed ordinary ordinate as $C_u/D$ with
\[
 C_u=\sum_{j:u_j=1}2^j3^{\sum_{k>j}u_k}.
\]
Every rotated raw determinant equals the odd integer $D$, prime to 3. Each rotation gives the next true rational phase by the appropriate affine identity. Reduction gives the specified parity by reducing $C_u$ modulo 2 and preserves the denominator across all steps. The neighboring words differ by a switch of 10 and 01, whose two local carries differ by one. At the full-word scale $C_u-C_v=\pm2^j3^h$ for the switch position $j$ and suffix grade $h$. It is coprime to $D$, hence their two complete reduced denominators have least common multiple $D$. Select the word with larger denominator. This proves the three claims simultaneously.

## Exact control

At $(A,m)=(485,306)$ the recorded word has minimum rotational distance 136 and full rational denominator of bit length 476. Its integer walk has 252 distinct core vertices, charged indices between 117,419 and 617,775, and 245 tripling commands disagree with the physical companion rule (counting either type of disagreement). The required ordinary charge count is 179. At $(1539,971)$ the corresponding numbers are 422 mismatches at the closest rotation, a 1,530-bit denominator and 755 distinct core vertices. Both clocks have least positive defect, verified by exact integer comparisons for all shorter dyadic clocks. Small connected control edges $27,63$ likewise give $1\to7\to1$ and $(28/27)(64/63)=2^8/3^5$. [Exact replay](check_core_rounding.py) · [Recorded output](../../../reports/astra-sixhour-20261127/arithmetic/core_rounding.json)

These flows retain genuine integer prime valuations, nonnegative edge multiplicities, cyclic adjacency of cores, all-shift separation, and a polynomial height. The ordinary command at each actual integer is the additional constraint left to exploit.

## Minimum spacing of the same high-distance rational cycles

Along the infinite subsequence of least positive defects (for example the convergents $m/A$ approaching $\log_3 2$ from below), *every two distinct native real phases* of the rational cycle in the construction have spacing tending to infinity. More precisely the minimum spacing is at least $c\mu^{1/14.3}$ for an absolute $c>0$ and real minimum $\mu$. Use any sequence of records for the positive logarithmic defect $A\log2-m\log3$ as $A$ increases; infinitely many exist by irrationality and elementary rational approximation, with these clocks satisfying $A=\lceil m\log_2 3\rceil$ eventually.

For any native subsegment of the balanced word of length at most one lap, its homogeneous multiplier is at least $1/512$. For complete gaps the discrepancy is below 4 in absolute value, and their drift factor $(P/N)^{t/m}$ is at least $1/2$. At its ends a native subsegment can have two partial gaps of at most two native steps each, costing a factor at most 16 in total. A segment with no complete gap also meets the bound. Therefore an affine segment with $h$ ones has positive additive contribution at least $h/1024$ by summing its $h$ addends $1/2$ with their positive suffix multipliers. In particular the complete lap gives $\mu(1-P/N)\ge m/1024$.

Cut a record-defect lap at the two selected phases. Both nonempty arcs cannot have contracting homogeneous multiplier, since otherwise each has a positive defect smaller than the record and a strictly shorter dyadic clock. No nonempty arc has homogeneous multiplier one. Use the expanding arc, with dyadic length $d$ and $h$ ones. It has $h\ge1$, $d<h\log_2 3$, and the physical increase is at least
\[
       \max\{h/1024,\ \mu(3^h/2^d-1)\}.
\]
Even the elementary inequality $3^h/2^d-1\ge3^{-h}$ gives spacing growing at least logarithmically in $\mu$. Lagarias's bound gives $3^h/2^d-1\ge h\log3-d\log2\ge c' h^{-13.3}$ with an absolute $c'>0$. Optimizing the two terms proves the power. Thus positive rational order, large pairwise real separation and linear all-shift Hamming distance coexist in the *same* words with an exponentially large complete denominator and a connected integer core flow.

[The strict Lean module](CoreRounding.lean) proves the externally rounded lap has a positive integer fixed point for every positive-defect command word, its exact dyadic translation law, the congruence for both possible macro inputs and the local criterion for preservation of a unit cell. The latter says that $[x,x+1]$ keeps width one at one command precisely when $x$ has that ordinary shortcut parity.
