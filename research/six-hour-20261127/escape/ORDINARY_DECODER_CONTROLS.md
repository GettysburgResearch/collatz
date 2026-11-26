# Cross-lift prediction on genuine convergent integer segments

**Status.** Finite ordinary construction and a source-qualified obstruction to a proposed ambiguity estimate. Here all named segments belong to the basin of 1. Their clipped amplitudes are those of the original law when so weighted, but their combined macroscopic normalized mass need not be positive.

## Exact prediction across all distinct lifts in a two-gap segment

Suppose that the last \(r\) exponents ending at an odd ordinary \(z\) lie in \(\{1,2\}\). Then \(z\bmod3^r\) determines that entire reversed word. From \(2^e z=3x+1\) its last exponent is 1 on \(z=2\bmod3\) and 2 on \(z=1\bmod3\). After computing \(e\), its predecessor \((2^e z-1)/3\bmod3^{r-1}\) is determined. Induction proves the claim. It applies simultaneously to all different positive lifts in each cell with this property.

Consequently the prediction error in [TERNARY_DECODER.md](TERNARY_DECODER.md), with \(d\ge r\), is upper-bounded by the clipped mass of observations for which one of these \(r\) exponents is at least three. This holds for any positive weighted sample, including the original finite law with its ordinary height factor. It follows just by using the indicated decoder as a competing table, with an arbitrary prediction on cells at which it cannot continue. This estimate is distinct from the loss caused by splitting a target's weight between several of its integer predecessors.

For instance, if every escaping ray of positive amplitude had occurrences of \(e\ge3\) of upper asymptotic density zero, the total-variation replacement would make the normalized prediction error tend to zero already at \(d=r\), on all target cells. The true existence of such an escaping ray is open. To force ambiguity on every possible escape, one must at least address these low-valuation ordinary trajectories. The same elementary obstruction applies to any two permitted exponents of opposite parity. For a fixed pair the decoder uses the map from parity of the exponent to its prescribed value.

## Many known-good lifts with the same prescribed history

Fix a chronological positive-gap word \(w\) of length \(L\), with sum \(A\), and let \(s\bmod3^L\) be its terminal ternary residue. For every \(h\ge1\) there are at least \(2^h\) distinct positive odd terminals \(z=s\bmod3^L\) in the basin of 1 which admit exactly that ordinary history, with their entire length-\(L\) paths in that basin. Their sizes and those of their input paths are bounded by
\[
            2^{2\cdot3^L+A+6h+2}.                                      \tag{1}
\]
For a two-gap word one has \(A\le2L\).

Start from 1. At any positive odd unit \(a\), the six integers \(2^e a\bmod9\), \(1\le e\le6\), run through all six units. Exactly two have residues 4 or 7, yielding unit odd predecessors \((2^e a-1)/3\). After \(h\) inverse choices this supplies \(2^h\) distinct unit anchors \(a\le2^{6h}\), each reaching 1. Distinct words of the same length ending at 1 give different positive sources because the forward valuations of an odd source are unique. For each anchor choose \(1\le e\le 2\cdot3^L\) with \(2^ea\equiv3s+1\bmod3^{L+1}\). Such \(e\) exists since 2 generates the units modulo \(3^{L+1}\): \(v_3(4^{3^u}-1)=u+1\) by induction and the elementary cube factorization. The positive odd \(z=(2^e a-1)/3\) is a unit, has residue \(s\) and reaches \(a\) in one odd step. Distinct anchors give distinct \(z\). Pulling the word back from \(z\) gives integers at each step by the terminal congruence. The inverse of a legal gap at a positive odd integer is positive and odd, and each inverse step increases the value by a factor at most \(2^e\). This proves (1).

For \(L=\lfloor(1-\varepsilon)\log_3 k\rfloor\) and \(h=O(\log k)\), (1) is \(\exp(o(k))\) for two-gap words. Thus polynomially many different positive integer lifts per selected cell fit in the true depth-\(k\) representative window and can carry the exact clipped weights there. Choosing \(w=1^L\) puts all the terminals in \(J_b(L)\) for every \(b>1\). Placing this word both before and after the marked site, by routing a word of length \(2L\), gives simultaneous real integer tests with \(L\to\infty\); to keep logarithmic height \(o(k)\) take \(L\le(1-\varepsilon)\log_3(k)/2\). The weights are individually positive at the interior unit vertices by positivity of the finite law on units. Their total normalized mass on the entire known basin tends to zero by (1) of the companion theorem. These controls address the geometry and exactness of local branch prediction at growing heights, not a lower bound on the full physical mass of that sector under hypothetical escape.

## Where the two Pliss selections disagree

Forward permanent and backward prefix events at the same site need not intersect even in genuine arithmetic. The signed integer cycle \(-5\to-7\to-5\) has exponents \(1,2\). For \(3/2<b<2\), the forward prefix budget holds at the site whose outgoing exponent is 1, and the backwards budget holds at the other site. Thus no time satisfies both zero-buffer budgets simultaneously. Arbitrarily long repetitions of this exact gap word also occur on the positive convergent segments constructed above. A choice of affirmative times for each direction cannot simply be intersected.
