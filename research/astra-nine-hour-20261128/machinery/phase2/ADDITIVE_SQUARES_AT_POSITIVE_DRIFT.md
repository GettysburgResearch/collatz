# Bounded, expanding valuation codes without long additive squares

**A quantified obstruction.** Given any ε>0, there is a bounded one-sided sequence of positive integer valuations e_i such that every window obeys
$$
   \sum_{i=u}^{u+r-1} e_i \le (1+\epsilon)r+C_\epsilon,
$$
yet consecutive windows of the same length h have distinct valuation totals for every h above a fixed threshold. Every finite prefix occurs at an actual positive odd integer. There are uncountably many such sequences, including ones whose binary shortcut parity words have positive topological entropy. Thus neither uniform expansion nor high factor complexity forces long repeated adjacent clock totals in this space of finite ordinary prefixes. The existence of one *fixed positive integer* realizing an infinite such code is a separate arithmetic question.

## Input and construction

Shallit's November 18, 2026 preprint constructs an infinite word w over six positive integers with no two adjacent nonempty equal-length blocks of the same sum. Its alphabet is explicit and very large. We use the theorem as a written external input. [Shallit, arXiv:2611.24441v1, §§1–6](https://arxiv.org/html/2611.24441v1)

Choose any binary sequence b and put
$$
 v_j=3w_j+b_{j+1}-b_j.
$$
These are bounded positive integers. Equal sums on adjacent length-h blocks in v would make three times the corresponding difference of w-sums a number of absolute value at most two, by telescoping b. This would force an additive square in w. Set E=2(3 max w+1)+1 and choose any integer K>E/ε. Put e_i=1 except at marker positions i=Kj, where e_i=1+(2v_j+1).

Every interval of length r contains at most r/K+1 markers, giving the displayed bound with C_ε=E. Two adjacent length-h intervals have marker counts differing by at most one. For h≥K each count is positive. Equality of excess sums forces these counts equal modulo two, as each marker contributes an odd excess. Their common count N therefore gives two adjacent nonempty length-N blocks of v with equal sums. This is impossible. In particular e is aperiodic.

For ε<log₂3−1 the multiplicative height on every window grows by at least a constant times exp(hr), with h=log 3−(1+ε)log 2>0. The real series representing the future correction,
$$
    \frac13\sum_{r\ge0}\frac{2^{\sum_{i=u}^{u+r-1}e_i}}{3^r},
$$
is uniformly bounded over u. Each prescribed prefix through N odd steps determines one ordinary odd residue modulo 2^{1+Σe_i}, by the finite binary parity bijection, and every positive representative realizes that prefix. This is a nested sequence of cylinders whose unique 2-adic member need not be a positive ordinary integer.

## Range of complexity

The differences b_{j+1}−b_j can be recovered from v_j modulo three. The infinite difference record determines b up to its initial bit, so the construction gives uncountably many e and uncountably many irrational 2-adic coding points, since the rationals are countable. Choose b containing every finite binary word. Its length-(n+1) blocks have at least 2^n distinct length-n difference records, hence v has at least 2^n distinct length-n blocks. Padding produces at least this many length-Kn blocks of e. Expand each valuation to the binary block 1 followed by e_i−1 zeros. This expansion is injective on fixed-length valuation blocks: the positions of the ones and the length recover every valuation. The resulting binary blocks have length between Kn and (1+E)Kn. At least 2^n/((1+E)Kn) of them have one common binary length. Because the word is infinite, its complexity p(t) is nondecreasing, giving p((1+E)Kn)≥2^n/((1+E)Kn) for each n. Interpolating consecutive n gives positive entropy.

There are also explicit low-complexity examples. With b identically zero the source w is a fixed-length coding of a fixed point of a q-uniform substitution, by Shallit's construction. A length-n factor at the smallest substitution scale with q^t≥n lies in two neighboring substituted letters and has at most q^t choices of starting offset. Hence its factor complexity is O(n). Fixed-length encoding, padding, and bounded positive run expansion preserve this linear upper bound: in the last operation each factor of length n is contained in the image of at most n+1 consecutive input letters, with bounded starting offset. Such a code is aperiodic by its long-square avoidance, including after run expansion. Weaver's rational odd-denominator complexity theorem then excludes every signed rational from realizing the entire undecorated code. For the positive-entropy codes, the complexity consequence is satisfied. Their finite ordinary realizations and bounded real tails still supply no full infinite ordinary realization. [Weaver, paper 173, superlinear factor complexity](https://rstation.ai/problems/collatz/papers/173)

The progression theorem for physical *sources* in COUNTED_BLOCKS_AND_PROGRESSIONS.md operates on sets of positive density in short intervals. Applying the same additive-combinatorial conclusion to the graph of time versus the cumulative valuation would require new information about the one prescribed physical source.
