# A strict weighted clock threshold for the bounded binary branch

**Proposed written theorem with an exact finite transfer certificate and a source-qualified analytic input.** Write \(p,s,X,A\) for the primitive odd period, minimum, maximum and total native halving clock of an ordinary positive cycle. Suppose every odd exponent is one or two and \(X\le(16s+7)/3\). Put \(\lambda=\log 2\), \(\gamma=\log_2 3\), and define the observable
\[
                C=24\lambda^2s(A/p-\gamma).
\]
Along any such sequence with \(p\to\infty\),
\[
       C\ \ge\ 6\frac{\log p}{\log s}
           +\frac{2\log(4/3)}{512\log3}-o(1).                  \tag{1}
\]
The analytic input here is the existing fixed-place Subspace-Theorem separation in the four-interior source argument. The positive gain uses a new weighted count of ordinary numerator four-sums. Formula (1) requires no exponent-three logarithmic irrationality estimate.

**Conditional consequence.** If \(\log p/\log s\ge1/3-o(1)\), then \(\liminf C\ge 2+2\log(4/3)/(512\log3)>2\). A sufficient extra hypothesis is \(\mu(\log_2 3)\le3\). The cited 2026 preprint states that bound, and we have not independently verified its logarithmic approximation proof. The classical Wu–Wang input used elsewhere does not give this value. In conjunction with the ordinary lower rounding map, a global upper comparator of raw additive defect at most **two** would now preclude this branch under the stated extra growth hypothesis. Construction of this comparator at arbitrary heights is open. [Ordinary rotation comparison and unweighted threshold](ROTATION_CUTS.md) · [Chudnovsky, Theorem 11.1, source of the separate exponent-three assumption](https://arxiv.org/html/2610.28079v1#S11)

## Physical marks on a mechanical calendar

Use the frozen full-band rank result of PR201, at commit d21bac748e705a64b6b57a7996a8ad6282f0bcbf. For all sufficiently large cycles under the displayed hypotheses its mechanical rank has \(\gcd(A,p)=1\), angular coordinate \(t_i=\{iA/p\}\), calendar \(b_i=\lfloor(i+1)A/p\rfloor-\lfloor iA/p\rfloor\in\{1,2\}\), and integer marks \(c_i=2^{j_i}\), \(j_i\in\{0,1,2\}\). From another origin one adds its angular starting phase. The normalized labels obey
\[
  Y_i=c_ix_i=4x_0 2^{t_i}+O(p),\quad
  2^{b_i}Y_{i+1}=3Y_i+c_i,\quad
  e_i=b_i+j_{i+1}-j_i .
\]
Here \(x_0=s+O(p)\): all normalized formulas in that source give \(x_i/x_0=2^{t_i+z_i}(1+O(p/s))\) with \(z_i\ge0\), and \(x_0\asymp s\). One has \(p=o(s)\) by the same source's physical count. If \(b_i=2\), only \(j_i=1,2\) occur, with the possible exception of the single inclusive rank \(t_i=2-A/p\). For \(b_i=1\) all three marks are retained. We remove windows touching the rank zero or the inclusive rank. Among windows of any fixed length \(O(\log s)\) this removes at most \(O(\log s)\) origins. A finite classical irrationality measure supplies \(s\le p^{O(1)}\), hence these origins form \(o(p)\). Alternatively, along subsequences where \(\log p/\log s\to0\), (1) follows directly from the elementary positive lower bound in the angular theorem, so (1) needs no separate finite-measure import for this removal. [Full-band rank ordering, tags and inclusive cutoff](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md)

Define \(w(t)=2\lambda\,2^{-t}\). The native product and uniform Taylor expansion give
\[
        C=\frac1p\sum_i w(t_i)c_i+o(1).
\]
Indeed \(s/x_i=(1+O(p/s))c_i2^{-t_i}/4\), and the mean of \(\log_2(1+1/(3x_i))\) is \(A/p-\gamma\). Removing \(o(p)\) origins changes the mean of any bounded observable by \(o(1)\).

## A 512-edge weighted ordinary four-sum

For a fixed calendar let \(B_i=\sum_{k<i}b_k\). A native \(n\)-edge word has cumulative exponent \(E_i=B_i+j_i-j_0\). When the starting tag is fixed its numerator \(\sum_{i<n}3^{n-1-i}2^{E_i}\) is the common factor \(2^{-j_0}\) times \(\sum_{i<n}3^{n-1-i}2^{B_i}c_i\). A signed four-sum equality between words therefore requires equality of these latter sums. For a tuple with signs \(+,+,-,-\), let \(\delta_i=c_{i,1}+c_{i,2}-c_{i,3}-c_{i,4}\). The signed recurrence \(P_{i+1}=3P_i+2^{B_i}\delta_i\), \(P_0=P_n=0\), implies \(2^{B_i}\mid P_i\): eliminate all later terms modulo \(2^{B_i}\) and cancel the remaining power of three. The carries \(z_i=-P_i/2^{B_i}\) thus satisfy
\[
               3z_i=2^{b_i}z_{i+1}+\delta_i.
\]

Put \(\beta=(\log3)/8\). Assign a four-tuple at one departure the weight \(\exp[-\beta w_i(c_{i,1}+c_{i,2}+c_{i,3}+c_{i,4})]\), where \(w_i\) may be the common lower angular envelope described below. At a reverse step retain four terminal tags, sorted within each same-sign pair, and \(z_{i+1}\bmod27\). Conditional on its actual integer value, the unknown next trit specifying it modulo 81 is **one choice common to all predecessors**. For each trial trit, sum over all ordered predecessor tags, testing the native exponent constraint, the \(b_i=2\) restriction, and divisibility of \(2^{b_i}z_{i+1}+\delta_i\) by three. Look up the quotient modulo 27. Multiply each predecessor by its departure weight. Take a maximum over the three trial trits **after** summation. Sorting the two tags within each sign only identifies equal counting entries; ordered multiplicities remain. With all initial counts set to one this bounds the four-word weighted count ending at any given terminal tags and actual carry. The same bound applies to a subfamily restricted by further conditions.

For blocks of 512 edges, the order of the 513 cuts \(\{-j\alpha\}\), \(0\le j\le512\), is constant on the rational bracket
\[
 \frac{58496250072115}{10^{14}}<\alpha<
 \frac{58496250072116}{10^{14}},
\]
containing \(\gamma-1\) and eventually \(A/p-1\). The code verifies both endpoint orders exactly. On the 513 open cells the calendar is fixed, including every modulo-one wrap. At a given departure the upper angular coordinate on a cell is bounded by the larger of its two right-end limits at the two bracket slopes. This holds by affinity because the wrap constant is fixed. Round that angular upper endpoint upward to units \(1/4096\); using \(w\) there supplies a common **lower** weight \(w_i\) for every path in that cell. The earlier removal of seam-touching windows disposes of the boundary ranks.

The exact transfer starts all entries at 1. Its maximum final weight, over the 513 cells, all 36 terminal pair states and all 27 carry residues, is at most
\[
           \frac{714173637}{1073741824}<\frac34.
\]
Weights are rounded upward in units \(2^{-21}\), then count entries are rounded upward in units \(2^{-30}\). Bounds on both integer multiplications and every row sum precede the signed 64-bit matrix operations. Rational logarithm bounds and the signs of the exponential Taylor remainders prove the direction of each weight rounding. The independent small-word check directly counts weighted sums of literal ordinary numerators. [Exact replay](check_weighted_clock.py) · [Integer output](weighted_clock_controls.json)

Concatenate blocks while conditioning at each seam on actual tags and actual signed carry. A uniform bound from arbitrary initial state to each fixed terminal state permits multiplication, just as in the unweighted reverse proof. Thus for a length \(n\) divisible by 512 in a fixed full calendar cell, the weighted four-sum count for fixed endpoint tags is at most \((3/4)^{n/512}\), even though the actual carry values at internal seams need not belong to any bounded interval. The transfer counts positive weights, and can be less than one.

## Retaining weights in the four-interior source estimate

We give the imported interface explicitly. In the frozen ordinary source proof, take four adjacent interiors of length \(n=512\lceil\log_3(Us)/(3\cdot512)\rceil\), two guards of length \(g=\lceil\eta n\rceil\), and the seven cut dates, where \(U=(16s+7)/(3s)\), with fixed \(\eta>0\). The prescribed physical strip, cut data and guards cost \(O(g+\log(n+2))\) nats of entropy for a uniform actual origin. Conditional on any further data, let \(Q_j\) be the ordinary numerator four-sum energy of the actual realized word family in interior \(j\). The located-source count in that fixed environment is at most \(6\prod_{j=1}^4 Q_j^{1/4}\). This follows from reduction of quantized grid collisions to ordinary numerator equalities within each individual interior, then Fourier Hölder for the four interiors. The former uses the fixed-place Subspace Theorem through Weaver's Lemma 4. The proof bounds the Cartesian product of individually realized segment families and does not assume independent words. Using a multiple of 512 only changes \(n\) by \(O(1)\). [Frozen four-interior source, separation and grid argument](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FOUR_COPY_TAILS.md) · [Weaver, Paper 145 v1, Lemma 4, §§4–6](https://rstation.ai/problems/collatz/papers/145/v1) · [Earlier entropy conditioning of actual bridge families](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/TERNARY_PAST_ENTROPY.md)

Record the full mechanical calendar cell of the window and the endpoint tags of its four interiors. These cost \(O(\log(n+2))\): a single initial angular phase has only \(O(n+g)\) cuts from its integer wraps, and in each open cell every subblock's cell is then fixed. Inside each block take the lower \(w_i\) used above. Additionally record for each true interior word the integer \(K_j=\lceil\sum_{i\in j}w_i c_i\rceil\), costing \(O(\log(n+2))\). Every four-tuple from this restricted family has product weight at least \(e^{-4\beta K_j}\). Thus
\[
                  Q_j\le e^{4\beta K_j}(3/4)^{n/512}.
\]
For a uniform origin the unconditional mean true cost of each interior is \(n(C+o(1))\), by cyclic stationarity. The common lower weights only decrease it. Conditioning on the remaining \(p-O(n+g)\) origins raises each expectation by at most \(o(n)\), because each cost is \(O(n)\). Taking the entropy of the origin, then conditional entropies within environments, gives
\[
 \log(p-O(n+g))\le O(g+\log(n+2))
       +4\beta n(C+o(1))+\frac{n}{512}\log(3/4).
\]
Now \(n\sim (\log s)/(3\log3)\). Let \(\eta\downarrow0\) to obtain (1). The comparison uses distinct ordinary integer sources and the source interval of their own physical height. Replacing the word's determinant \(D=2^A-3^p\) by a factor test would not justify this step; ordinary integrality requires \(D\) to divide its complete carry.
