# A sharp seed clock for compressed parity words on positive integer trajectories

A binary word records actual shortcut departures of \(T(2x)=x,\ T(2x+1)=3x+2\). Fix \(0<\eta<1\) and a positive integer \(m\). For all sufficiently large \(t\), suppose an ordinary trajectory from \(n\ge1\) has
\[
 \log_2(n+1)\le(1-\eta)t,\qquad
 w=V_1^{a_1}\cdots V_j^{a_j},\quad |w|=t,\quad
 j\le m,\quad a_i\ge1,\quad B=\sum_i|V_i|\le \frac{\eta t}{32\cdot2^m}.
                                                                    \tag{1}
\]
The nonempty bases \(V_i\) may vary freely with the source and clock and contain arbitrary internal parity patterns.

**At the start of some powered block the positive integer trajectory is on a cycle whose period divides \(|V_i|\).** In fact that state equals the rational fixed point of the precise affine word \(V_i\). Thus every simple path beyond the clock in (1) has a linear lower bound on the total base length in every such \(m\)-block description. The displayed coefficient is explicit. The large-time onset from the fixed-place Subspace Theorem is ineffective.

Three consequences are worth distinguishing.

* With at most \(m\) single-symbol runs, no cycle can occur at a block center, since the centers are \(0,-1\). Thus the maximal length from \(1\le n\le N\) with at most \(m\) runs is \((1+o_m(1))\log_2 N\). The Mersenne ramp gives the matching lower bound already for one run. Both even and odd run lengths are unrestricted.
* For a fixed regular language whose number of words of length \(t\) grows subexponentially, there is a **computable finite list of positive periodic points** such that every accepted prefix longer than \((1+\epsilon)\log_2N\), from \(n\le N\), meets one of them for large \(N\). The list is obtained from the recognizing automaton. The asymptotic cutoff is ineffective and the conclusion has no analogous premise for an unrestricted regular language.
* For any fixed bound on the number of nodes in an expression built from letters, concatenation and arbitrary positive powers, a sequence of simple positive prefixes with \(\log_2(n+1)\le(1-\eta)t\) and \(t\to\infty\) cannot have that expression bound. Powers nested to bounded expression size are allowed even when their base words change with \(t\).

The earlier bounded-even result has a sparse shifted carry and the same coefficient-one seed cutoff. Weaver 173 and the mesoscopic theorem cover much broader low **factor complexity** using a constant multiple of the input bit length. The nested-expression work on cycle denominators gives a full exponent for coprime nearcritical closed words. Here the sharp clock holds for open ordinary paths under (1), even with moving complex bases, and the exceptional exit is an actual periodic state from a supplied block. [Bounded even steps](BOUNDED_EVEN_TYPE.md) · [Weaver 173](https://rstation.ai/problems/collatz/papers/173) · [Mesoscopic factor complexity](https://github.com/GettysburgResearch/collatz/blob/f99cce768e1d5644cabd50ae277bc74cb3c60a11/research/astra-global-rigidity-20261128/cycles/MESOSCOPIC_COMPLEXITY.md) · [Nested primitive-clock expressions](https://github.com/GettysburgResearch/collatz/blob/f99cce768e1d5644cabd50ae277bc74cb3c60a11/research/astra-global-rigidity-20261128/cycles/PRIMITIVE_CLOCK_EXPRESSIONS.md).

## The block center and its ordinary duration

For a nonempty supplied word \(V\) of length \(l\) and weight \(u\), write its affine map as \(F_V(x)=(3^u x+C_V)/2^l\). Its integer carry satisfies \(0\le C_V\le3^l-2^l\), by appending an even bit, which retains the carry, or an odd bit, which gives \(3C_V+2^l\). The signed denominator \(2^l-3^u\) is odd and nonzero, and the unique rational center is
\[
       c(V)=C_V/(2^l-3^u),\qquad d(V)=|2^l-3^u|\le3^l.
\]
If a positive integer \(x\) follows \(V^a\) to \(y\), then
\[
          2^{la}(y-c(V))=3^{ua}(x-c(V)).                              \tag{2}
\]
If \(x=c(V)\), one copy of \(V\) returns the actual trajectory to \(x\). Conversely \(y=c(V)\) in (2) forces \(x=c(V)\). If both differ, coprimality of two and three gives
\[
   2^{la}\mid d(V)(x-c(V)),\qquad
   la\le\log_2(x+1)+\theta l,\qquad \theta=\log_2 3.                 \tag{3}
\]
This is the absolute value of a nonzero integer even when the center is negative.

## Truncation and dominance of the marked coordinate

Suppose (1) holds along a sequence with \(t\to\infty\) and no powered block starts at its center. Write \(x_i\) for the state at the end of block \(i\), \(x_0=n\), and \(v_i=\log_2(x_i+1)\). A native step has \(T(x)+1\le2(x+1)\). By (3), a block of base length \(l_i\) lasts at most \(v_{i-1}+\theta l_i\) and \(v_i\le2v_{i-1}+\theta l_i\). Induction or summing this geometric bound gives for the total clock of every suffix beginning at \(x_i\)
\[
                         t-b_i\le 2^m(v_i+2B),                        \tag{4}
\]
where \(b_i\) is the elapsed native clock.

Set \(\beta=\eta/(4\cdot2^m)\) and \(H=3B+\beta t\). If there is a first boundary with \(v_i\le H\), truncate there. Otherwise keep the entire word. The initial state cannot qualify: (4) would give \(t\le 2^m(5B+\beta t)<\eta t/2\). The resulting nonempty prefix ends at time \(b\ge(1-\eta/2)t\), since (4) makes the omitted suffix less than \(\eta t/2\). Its initial and strictly internal boundaries all have \(v_i>H\). Pass to a subsequence with a fixed number \(j'\) of retained blocks. Let \(q_i\) be their cumulative odd counts, \(q\) the terminal count, \(c_i=c(V_i)\), and \(D=\prod_{i\le j'}d(V_i)\). Then \(D\le3^B\) and \(|Dc_i|\le3^B\), because the factor \(d(V_i)\) cancels from its own fraction.

The centered identities (2) telescope to the following integer vector and marked form:
\[
 \begin{split}
 X_0 &= 3^qD(n-c_1),\\
 X_i &= D(c_i-c_{i+1})2^{b_i}3^{q-q_i}\quad (1\le i<j'),\\
 B_* &= X_0+\sum_{i<j',\,i\ge1} X_i =2^bD(x_{j'}-c_{j'}).           \tag{5}
 \end{split}
\]
The right side is nonzero because the last block did not start at its center. Omit zero coordinates among \(i\ge1\), passing to a subsequence with a fixed nonzero index set. All other coordinates have height at most \(2^{6t}\) for large \(t\). Mark coefficients need not be fixed with the sample: in (5) they are integer factors inside the coordinates, of absolute value at most \(2\cdot3^B\).

At an internal boundary the exact ratio formula is
\[
 \frac{|X_i|}{|X_0|}
 =\frac{|c_i-c_{i+1}|}{|x_i-c_i|}
       \prod_{a=1}^{i-1}\left|\frac{x_a-c_{a+1}}{x_a-c_a}\right|.   \tag{6}
\]
It follows by multiplying (2) on each block up to \(i\). Since \(|c_i|\le3^B\) while \(x_i+1>2^{3B+\beta t}\) at these internal sites, every ratio (6) tends to zero, uniformly for fixed \(m,\eta\). In particular an exceptional rational hyperplane containing an infinite subsequence cannot involve \(X_0\) with nonzero coefficient.

## Fixed-place elimination

At infinity and at three use the coordinate forms. At two use \(B_*\) in place of \(X_0\), together with the other coordinate forms. All evaluated forms are nonzero. The resulting product over the three places is at most
\[
 3^B(n+1)(2\cdot3^B)^{m-1}2^{-b}\le2^{-\eta t/4}                  \tag{7}
\]
for large \(t\), by (1), \(b\ge(1-\eta/2)t\), and \(\theta<2\). Indeed \(|X_0|_\infty |X_0|_3\le |D(n-c_1)|\), and each remaining coordinate contributes just its prime-to-six part, at most \(2\cdot3^B\). This remains true whenever any subset of the latter coordinates is omitted. Dividing by the common gcd of the retained vector also preserves the upper bound, since for \(d\) coordinates the product is multiplied by the inverse \(d\)th power of that gcd's prime-to-six part.

Consequently (7) is less than a fixed negative power of the primitive height. The rational fixed-place Subspace Theorem places all the vectors in finitely many proper rational hyperplanes. Select one with an infinite subsequence. By (6) its relation involves only the unmarked coordinates. Use the relation to eliminate one of those coordinates in the marked form, preserving its coefficient one of \(X_0\) and its value \(B_*\). The other forms are still coordinates. Iterate with the same bound (7) and fixed rational forms on each subsequence. A nontrivial relation among a single remaining nonzero unmarked coordinate is impossible. If there were no unmarked coordinates originally, \(B_*=X_0\) and \(2^b\mid D(n-c_1)\); the nonzero integer \(|D(n-c_1)|\le3^B(n+1)<2^b\) also contradicts (1). This proves the theorem. [Schlickewei, rational fixed-place Subspace Theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Varjú, Theorem 5, rational formulation](https://arxiv.org/pdf/2104.04367v2)

## Regular languages and nested powers

Trim a deterministic finite automaton to its reachable, coaccessible states, keeping labelled edges distinct. If a state in one strongly connected component has two internal outgoing edges, they have different first letters. Follow each back to the state, and repeat the two loops individually to equalize their lengths. Concatenating \(a\) choices gives \(2^a\) distinct words of the same length from the state back to itself, since the two fixed equal-length words differ. Prefix and suffix by fixed accepting routes. This contradicts subexponential growth. Thus every component containing a cycle is one simple directed labelled cycle. Accepted paths visit components in the acyclic component order. At a cyclic component the path follows powers of its fixed labelled cycle, with fixed choices of entry and exit and a bounded residual segment. Singleton acyclic components contribute only bounded connectors. Therefore all accepted words belong to a finite union of templates with boundedly many powers and bounded total base length. Empty blocks and connectors can be dropped, and bounded nonempty connectors count as power one. Theorem (1) applies. Compute each template base's rational center from its finite bits, keep the positive integers among them that pass replay of its word, and take their union. Those are the asserted periodic targets.

For bounded expression size, consider an allegedly violating sequence with fixed parse-tree shape. Pass to subsequences so each inspected power exponent is either bounded and fixed or tends to infinity. Flatten a bounded exponent into that fixed number of copies and flatten concatenations. Keep a node with exponent tending to infinity as one powered block; its unpowered base has length at most \(t/a=o(t)\). Leaves have length one. This gives a bounded number of powered blocks with total base length \(o(t)\); the number bound can depend on this subsequence. Hence (1) eventually applies. If the original path was simple its forced actual return to a block center is impossible. This argument gives no bound for positive-entropy regular languages, growing expression sizes, or arbitrary linear-factor-complexity paths at the sharp horizon.
