# How large can a deterministic residue quotient of one cycle be?

**PROPOSED written theorems.** A primitive positive rational shortcut cycle has least period $n>1$, full reduced denominator $d$, states $x_i=a_i/d$, minimum $x_*$, and chronological bits $b_i=a_i\bmod 2$. Subscripts are cyclic. Every $a_i$ is a positive integer prime to $d$, and $d$ is prime to six, by the full-lap determinant $2^n-3^{\sum b_i}>0$ and the branch equations.

For an odd integer $M>1$, call reduction **compatible** if equal numerator residues have equal successor residues:
$$
 a_i\equiv a_j\pmod M\quad\Longrightarrow\quad
 a_{i+1}\equiv a_{j+1}\pmod M .
$$
This is a condition on the entire physical cycle, meaningful even when $M$ shares primes with $d$.

**Theorem 1.** Every noninjective compatible reduction has an image cycle of period $s\mid n$, with $s<n$. The binary word has just one nonconstant residue column modulo $s$. The modulus $M$ is prime to $d$ and divides a specified positive integer strictly less than $3^s$.

**Theorem 2.** Fix $B\ge0$. Uniformly over cycles with $d\le n^B$, for all sufficiently large $n$, every noninjective compatible reduction satisfies
$$
 s\ll_B \frac{\log n}{\log\log n},\qquad
 M\le \exp\!\left(O_B\!\left(\frac{\log n}{\log\log n}\right)\right).
$$
In particular, for each $\varepsilon>0$, each sufficiently long positive **ordinary** cycle, and **every odd integer** $n^\varepsilon\le M<n$, two actual phases agree modulo $M$ and their actual successors disagree. The period may be highly composite, prime, or a lower record. The assertion applies to each such cycle individually.

The finite bound below also tests words having at most $r$ variable columns, without assuming residue compatibility. It bounds the **whole** denominator for each specified word.

## What the image cycle forces

Compatibility makes the shift a well-defined map on the finite image of all phases. The entire image is a single periodic orbit. It consists of $s$ different residues in chronological order, for $s\mid n$. Noninjectivity says $s<n$. The states in each phase column modulo $s$ are congruent.

If two members of one column have different parities, subtract their cleared branch equations
$$
                   2a_{i+1}=3^{b_i}a_i+b_i d .
$$
Their successor residues agree, so the column's common residue $a$ satisfies $2a+d\equiv0\bmod M$. As $M$ is odd there is only one such residue. The $s$ projected phases are distinct, so at most one column can mix bits. At least one does. Otherwise the whole parity word has period $s$. The affine map of the first $s$ bits has positive multiplier unequal to one, and its $n/s$ iterate has the same unique fixed point. This contradicts least physical period. A common prime of $M,d$ would divide $2a+d$ and $a$, impossible at the common reduced denominator.

Put $U_i=2a_i+d$. Then $2U_{i+1}=3^{b_i}U_i+d$. At the variable column, the constant carry of the next $s$ bits is
$$
 K=\sum_{t=0}^{s-1}2^t3^{\,\sum_{t<k<s}b_{i+k}} .
$$
Only the fixed tail enters $K$. Both endpoint $U$'s vanish modulo $M$, so unrolling gives $M\mid dK$ and therefore $M\mid K$. Comparison with the all-one tail gives $1\le K\le3^s-2^s$. This proves Theorem 1. In particular if $n$ is prime then every odd $1<M<n$ is incompatible: any proper quotient would have $s=1$ and $K=1$.

## Local height and the block dictionary

Take any divisor $s$ of $n$. Put $m=n/s$ and suppose there are at most $r$ columns modulo $s$ on which $b_i$ is nonconstant. Each length-$s$ window covers every column once. Its odd count lies between $v$ and $v+r$, where $v$ counts the constantly odd columns.

Shifting any interval by $s$ changes its odd count by the difference between two length-$s$ window counts. This follows by subtracting the prefix sums at both ends, including when the interval is shorter than $s$. Consequently shifting by $js$, $j\in\mathbb Z$, changes any interval count by at most $r|j|$. Apply this to every suffix of the exact positive centered full-lap sum
$$
 (2^n-3^{\sum b})U_i
     =d\sum_{t=0}^{n-1}2^t3^{\,\sum_{t<k<n}b_{i+k}} .
$$
Termwise comparison gives
$$
                  U_{i+js}\le 3^{r|j|}U_i.                     \tag{1}
$$
This uses the shared full return. Even when each free column changes many times, nearby phases in the column remain comparable. Their unrestricted Hamming distance could instead grow with $m$.

Take $i$ at $x_*$. For any integer $k\ge1$ such that $h=2^{rk}<m$, select the $h+1$ offsets from $-\lfloor h/2\rfloor$ through $\lceil h/2\rceil$. Their phases are distinct. Their next $ks$ bits have at most $rk$ free positions. Two selected phases therefore have identical $ks$-bit futures. Their different positive integer numerators differ by a nonzero multiple of $2^{ks}$: unroll the identical word and cancel its odd factor. The difference is strictly below the largest selected numerator. Equation (1) now proves
$$
       2^{ks}<3^{\,r\lceil 2^{rk}/2\rceil}\,d(x_*+1).
                                                                    \tag{2}
$$
No Diophantine input enters this finite inequality. In particular,
$$
 \log_2 d>sk-r\lceil 2^{rk}/2\rceil\log_23-\log_2(x_*+1).
$$
For $r=1$ this lower bound is at least $s\log_2(\min(s,m))-O(s)-\log_2(x_*+1)$ when $s,m\ge3$, by choosing $k=\lfloor\log_2(\min(s,m)-1)\rfloor$. No period or word is averaged in this whole-denominator estimate.

## Two blocks and the asymptotic conclusion

When $r=1$ and $m=2$ the two blocks can use different bits at the free position. Compare the minimum with its $s$-shift. Their centered heights are within factor three by (1). Let $0\le R<s$ count the fixed bits before the next variable date from the minimum. These $R$ bits agree, so $2^R<3d(x_*+1)$. After $R+1$ steps the two phases have $s-1$ common bits, and each obeys $x_{j+1}+1\le (3/2)(x_j+1)$. It follows that
$$
                  2^{s-1}<3d(x_*+1)(3/2)^{R+1}.                \tag{3}
$$
At $R=0$ the two different positive integer numerators already have separation at least one. Equations (2)–(3) give $s=O(1+\log(d(x_*+1)))$ also for $m=2$.

For Theorem 2, the cited classical two-logarithm estimate gives $x_*<600n^{14.3}$. Indeed $n\log 2-(\sum b_i)\log 3$ is at least $(\log3)/(1200n^{13.3})$ and at most $n/(3x_*)$ by the physical lap product. Under $d\le n^B$ we have $\log(d(x_*+1))=O_B(\log n)$. Equation (3) excludes $m=2$ for large $n=2s$. When $m\ge3$, put $r=k=1$ in (2) to obtain $s=O_B(\log n)$. Then $m=n/s>s$ for large $n$, and the optimized (2) gives $s\log(s+1)=O_B(\log n)$. Invert this inequality and use $M<3^s$.

A sequence of positive rational cycles with a noninjective compatible modulus $M\ge n^\varepsilon$ for fixed $\varepsilon>0$ and increasing $n$ must therefore have full denominators growing faster than every fixed power of $n$. A modulus above the entire span of the numerator set gives an injective map and lies outside this assertion.

## Sources and boundary

- Main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, `research/integrated/periodic-tails/README.md`, gives the affine fixed point and whole-denominator convention. Retain `research/integrated/ERRATA.md`, E-D-002.
- PR212, `505d3fe782922904e86477990cc5d41e9110edda`, `research/astra-infinite-descent-20261127/cycles/ALL_SHIFT_HEIGHTS.md` and `ShiftHeights.lean`, proves the centered positive full-lap Hamming comparison, shared-word dyadic spacing, and records Lagarias's effective two-logarithm input. We use its positive-sum mechanism with the *sliding interval-count difference* and a local dictionary at the actual minimum.
- PR211, `4b44cded44af5bb7c3ce67fb16a70c898ad505d5`, `research/astra-reciprocal-rigidity-20261127/cycles/ALL_SHIFT.md`, already partitions rotation comparisons by nonconstant columns for Hamming bounds and simultaneous packing. Its `cycles/phase10/RECORD_TYPES.md` explains why a critical record can resist every contracting split.
- PR191, `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, `research/two-sided-cycle-packing-20261124/README.md`, TCP-1/2, uses common past and future divisibility for fixed-weight dictionaries. The free column here can change the weight of each block.
- Lagarias, [Lemma 2.2(1)](https://arxiv.org/abs/math/0512006), is external and is used only to express the height inequalities in terms of $n$ alone.

Every incompatible modulus supplies an actual pair of phases, and the pair may vary with the modulus. No argument here requires a hypothetical ordinary cycle to admit even one noninjective compatible modulus of polynomial size. Rational cycles of every prime physical period $p$ exist: take a word with one odd bit and $p-1$ even bits for $p\ge2$. All their odd moduli $1<M<p$ fail compatibility by the prime-period clause, independently of their full denominators. Widespread incompatibility itself supplies no contradiction.
