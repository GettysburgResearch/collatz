# A full-circuit inversion formula and upper clock approximants

Throughout this note \(p\) is the number of odd phases in a primitive positive **ordinary** Collatz cycle \(C\), \(A\) its total halving exponent, and \(Q=p+A\) the number of states in its unaccelerated circuit \(B\). Let \(s,X\) be the minimum and maximum odd states. For every positive integer \(d\), inspect the following short interval above a multiple of each odd state:
\[
 I(C)=\sum_{d\ge1}\#\{(x,y)\in C\times B:6^d x<y<6^d(x+1/3)\}.             \tag{1}
\]
The sum is finite since every full state is at most \(3X+1\). Then, writing \(g=\gcd(A,p)\),
\[
                             I(C)\ge g-1,\qquad I(C)\equiv g-1\pmod2.    \tag{2}
\]
Each counted pair is an actual inversion of the chronological update in sixfold logarithmic order. Its oriented time lag \(t\) also occurs in reverse: the number of pairs at lag \(t\) equals the number at \(Q-t\). In particular if \(p,A\) are both even, a pair at exactly \(Q/2\) full steps is mandatory.

Each individual pair also gives a decomposition of \((A,p)\) into two positive integer clock vectors, both strictly above \(\log_2 3\). The first adjusted vector has coordinate sum exactly \(t\), and the second exactly \(Q-t\). Thus a primitive, best upper clock through its odd denominator rules out **every** inversion at arbitrary physical width. It does not rule out the monotonically ordered cycle.

## The integer permutation and its length

Every full state is prime to three. Its sixfold lifts form a discrete ordered set with \(Q\) distinct representatives per fundamental interval. On that lifted set use the bijection
\[
                F(6^j x)=6^j(3x+\epsilon_x),\qquad \epsilon_x=\mathbf1_{x\text{ odd}}.
\]
At an even step, \(3x\) is six times the native successor \(x/2\); at an odd step the lifted output is already the native successor. The lift is consequently a permutation, and its accumulated sixfold winding per circuit is exactly \(A\).

Number the lifted states in increasing order by \(i\in\mathbb Z\), with index \(i+Q\) six times index \(i\). The induced bijection \(\pi\) satisfies \(\pi(i+Q)=\pi(i)+Q\). Its mean index displacement is \(A\): write each image index as a representative modulo \(Q\) plus \(Q\) times its sixfold shift, sum over one period, and cancel the permutation of representatives. The sum of the shifts is \(A\), since changing native states to their chosen representatives telescopes.

An inversion is a pair of lifts \(6^i x<6^j y\) with the images in strictly opposite order; count simultaneously scaled pairs only once. If \(i\le j\), the input difference is at least \(6^i\), and the lower source correction is at most \(6^i\). Tripling the input difference precludes any inversion. If \(i>j\), set \(d=i-j\) and \(h=y-6^d x\ge1\). An inversion now requires an odd \(x\) and
\[
                            3h+\epsilon_y<6^d.
\]
Since \(3\mid6^d\), this is precisely \(1\le h<6^d/3\). Conversely every pair in (1) gives this one inversion class. Distinct images never tie on the full cycle. This proves (1) is exactly the affine permutation inversion count.

Whenever the permutation has an inversion it has two adjacent entries in inverted order. Swap those two entries and all their periodic translates. This decreases the number of inversion classes by exactly one: except for the swapped pair, all comparisons are unchanged or paired by exchanging its two entries. The periodically repeated adjacent swaps are disjoint (\(Q\ge3\)). The mean displacement is unchanged, including for a swap across the fundamental seam. The terminal increasing bijection of \(\mathbb Z\) is the translation \(i\mapsto i+A\). On the quotient that translation has \(g=\gcd(Q,A)\) cycles, while the original permutation has one. Each transposition splits one cycle into two or joins two cycles into one. Exactly \(I(C)\) transpositions connect the two, proving (2).

Fix a nonzero lag \(t\bmod Q\) and write \(x_i\) for the full chronological state. The sum over one period of
\[
 \left\lfloor\log_6\frac{3x_{i+t}+\epsilon_{i+t}}{3x_i+\epsilon_i}\right\rfloor
 -\left\lfloor\log_6\frac{x_{i+t}}{x_i}\right\rfloor
\]
vanishes by the native update, since the two even-step shifts cancel in the sum and the remaining quantities telescope. There are no tied ratios at a power of six, either before or after the step. A negative summand counts the thresholds crossed when \(x_i\) is the smaller physical source in (1), and a positive summand counts the reversed orientation. This gives the claimed equality of the two lag counts. When \(Q\) is even their contribution in opposite-lag pairs is even; when both \(p,A\) are even, (2) makes the total odd.

## Decomposing the clock at a crossing

For a pair counted in (1), follow the chronological arc from \(x\) to \(y\). Write \(p_1,a_1\) for its odd and even departures, \(p_2,a_2\) for the complementary arc's counts. The first odd step at \(x\) contributes \(\log(1+1/(3x))\) to the log-height drift above the homogeneous multipliers. It exceeds \(\log(y/(6^d x))\) by (1). All later drifts are nonnegative. Similarly \(\log(x/y)<-d\log6\) in the return direction. Thus
\[
 \begin{split}
       (a_1+d)\log 2-(p_1-d)\log3 &>0,\\
       (a_2-d)\log 2-(p_2+d)\log3 &>0.                                  \tag{3}
 \end{split}
\]
There are enough odd departures: \(y/x>6^d>4^d\), while the growth factor of any odd step on a positive integer is at most four and all even steps decrease. Hence \(p_1>d\). The second log inequality also gives \(a_2>d\). Both adjusted vectors have positive entries and they sum to \((A,p)\). In particular each form in (3) is strictly less than \(\Lambda=A\log2-p\log3\).

Equivalently at a lag \(t\) carrying an inversion, some integer \(b\) must satisfy
\[
                  0<b-t\log_6 3 < A-Q\log_6 3.                            \tag{4}
\]
Indeed take \(b=a_1+d\), and use \((a_1+d)+(p_1-d)=t\). The complementary vector supplies the strict upper endpoint. This is a finite clock test independent of the heights or the scale exponent \(d\).

Suppose there is **no** upper rational \(a/b\) with \(1\le b<p\) and
\(\log_2 3<a/b<A/p\). If a crossing exists, both ratios in (3) must equal \(A/p\): one is no larger than their denominator-weighted mean, and strict improvement at a smaller denominator is excluded. Both vectors are therefore positive multiples of \((A/g,p/g)\). It follows that \(t\) is a multiple of \(Q/g\). If \(g=1\) this is impossible for \(0<t<Q\), so the full native rank permutation is exactly translation by \(A\). The proof also covers a one-sided upper record where the total period is a multiple of its reduced denominator; in that case it constrains the possible lags rather than eliminating them. A sufficient explicit condition for absence of a strictly smaller upper ratio is \((A/p-\log_2 3)p^2<1\), by rational separation. This condition alone does not imply \(g=1\).

## The width below twelve

If \(X<12s\), then \(y\le3X+1<36s+1\), and \(d\ge2\) contributes nothing. At \(d=1\) the only possible integer is \(y=6x+1\), which is odd and has native exponent exactly one. Thus
\[
                         I(C)=\#\{x\in C:6x+1\in C\}.                       \tag{5}
\]
Here every inversion swaps adjacent sixfold ranks: any intervening state would make at least one more inversion incident to an endpoint, while the pairs (5) are disjoint. Indeed their low endpoints satisfy \(x\le(X-2)/9<4s/3\) from the true next odd state \(9x+2\); their high endpoints are \(>6s\). Inversions at different scales on the same ray would likewise share an endpoint and are excluded. Consequently the chronological permutation is exactly translation by \(A\) composed on the right with the disjoint adjacent swaps for (5). When \(g>1\), form a graph on \(\mathbb Z/g\mathbb Z\) with an edge from \(r\) to \(r+1\) whenever such a swapped lower rank is \(r\bmod g\). The translation preserves each residue class and swaps never leave a connected component of this graph. Since the true circuit is transitive, the graph is connected. In particular at least \(g-1\) distinct neighboring residue classes are represented.

When \(X<9s+2\) there is no pair because \(9x+2\ge9s+2\). This recovers coprimality and full mechanical order, while the [two integer completions](FULL_STEP_CHART.md) also impose a common rotation for a whole interval of explicit cutoffs. At greater width the actual placement, number and time lags of the pairs in (1) remain unknown. The exact criterion here gives no automatic contradiction even at \(I=0\).

The term best upper clock refers to a rational approximation to \(\log_2 3\) with a bounded denominator. The [critical records in PR210 at 592328f](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md) concern strict prefix records of the actual coefficient on a nonrepeating ray, their backwards ternary tree and its rational points. This argument uses no escape assumption, ternary critical trace or Subspace Theorem. All identities in (1)–(5) concern the integer return of the entire positive circuit. The cyclic word's complete positive determinant must divide its full carry for numerator points obtained from a rational word to form an ordinary cycle.

[Exact affine permutation, lag and reduced-denominator controls](check_full_circuit_inversions.py) · [Recorded output](full_circuit_inversion_controls.json)
