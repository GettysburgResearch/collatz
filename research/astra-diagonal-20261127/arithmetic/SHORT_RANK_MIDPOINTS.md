# Propagation of midpoint comparisons on short physical rank intervals

Use the [three-grade cycle and high return](THREE_GRADE_RANK_CONVEXITY.md), including its ordinary minimum \(s\), primitive odd period \(p\), folded labels \(L\), input marks \(\ell\), and dyadic extension. There is an absolute \(\eta>0\) such that, for large \(p\), every \(0<b<c\le\eta p\) and every \(0\le r<p\) satisfy the exact strict comparison
\[
 \operatorname{sign}\big(L_r-2L_{r+b}+L_{r+c}\big)
     =\operatorname{sign}(1-2q^b+q^c)\in\{-1,1\},\qquad q=2^{1/p}.
 \tag{1}
\]
Thus the ideal exponential reference gives the exact answer to the arithmetic-midpoint comparison, however close the ideal comparison is. The result includes all wrapped triples. With \(J_r=L_r-2L_{r+b}+L_{r+c}\) and \(\bar L=p^{-1}\sum_{r<p}q^{-r}L_r\), it follows that
\[
 \frac1p\sum_{r<p}q^{-r}|J_r|=\bar L\,|1-2q^b+q^c|\ge \tfrac12.
 \tag{2}
\]
The proof uses the native integer returns in all three physical grades.

## The negative finite induction

Use the signed height \(N=2Y-X-Z=-H\), with source residues \(X,Y\pmod4\). At single-return boundaries exclude the two positive states
\[
                     (2,1,2),\quad(4,2,2).
\]
Every other positive state stays strictly positive through each complete return block, including both lifted middles, and reaches another protected boundary. This follows from the complete column tables in the [reverse certificate](audit_three_grade_curvature.py). Explicitly, the missing input residue is \(2Y-X-N\bmod4\), and every simultaneous return applies \(dN'=nN-(c_0-2c_1+c_2)\). Test divisibility by the common divisor, the three output residues modulo four and, for a split, the sign of \(9N-(m_0-2m_1+m_2)\) at its lifted middle. The absolute carry ranges of the positive calculation give the same bound \(N'\ge 3N/4-4\). From the terminal pair of exceptional states, the successive counts of positive unsafe preimages are below. The height never exceeds four, so the bound limits every one-step reverse check to \(1\le N\le10\).

| Block in forward order | Number of unsafe positive states at successive reverse steps |
|---|---|
| \(SDD\) | 2, 2, 1 |
| \(SDDD\) | 2, 2, 2, 1 |
| \(SDD\,(DS,DS,SD)\,DD\) | 2, 2, 1, 2, 3, 2 |
| \(SDD\,(DS,SD,SD)\,DD\) | 2, 2, 1, 0, 0, 0 |

Each initial unsafe set is a subset of the displayed pair. The terminal rows, the separate reverse steps, maximal heights and the initial sets are in the [exact report](../../../reports/astra-diagonal-20261127/arithmetic/three-grade-curvature-audit.json). The positive sign uses the six exceptional states in the [strict convexity proof](THREE_GRADE_RANK_CONVEXITY.md).

## All origins for one set of offsets

On the high ranks take the columns at \(j,j+b,j+c\). Extend \(B_{k+i}=\phi(B_i)\) as necessary for \(0\le i\le c\). Extend the full folded labels by the same actual octave doubling as before. A split begins at \(h-c\le j<h\). Its three two-return words are either \((DS,DS,SD)\) or \((DS,SD,SD)\), according to the location of the middle column. Its intermediate leftmost position is \(k-c\le j+u<k\), with exactly the wrapped columns lifted by \(\phi\). The surrounding itinerary has the same \(S,D,D\) before and \(D,D,S\) after whenever \(c/k\) is sufficiently small. Indeed at the six surrounding times the limiting center positions are strictly interior to the indicated arcs of the limiting return rotation. Choose the constant upper bound on \(c/k\) below half the minimum of these finitely many distances to an arc boundary. Decrease it further below half \(\min_{1\le i\le20}\|i\lim(u/k)\|\). This makes the finitely wide time neighborhoods of distinct split starts disjoint, even though there may now be \(c\) split starts. Also take \(c<k-h-2\), ensuring the lower- and upper-interval reconstructions overlap. These requirements allow a fixed \(\eta>0\) for all large \(p\).

If a single-return boundary has a protected positive or negative state, the corresponding strict sign holds on the entire high rotation, using its corresponding finite induction. At the low ranks, \(2J=3H+(b_0-2b_1+b_2)\), where each \(b_i\in\{1,2\}\), so strict integer signs transfer unchanged. High labels, including the wrapped middles, give \(J=2H\). These ranges cover all \(r<p\).

## Elimination of the central states

Suppose no boundary carries a protected sign. Its state then belongs to a set of 15 possibilities: the six exceptional positive states, the two exceptional negative states and the seven residue-compatible states of height zero. Denote this set by \(M\), and distinguish
\[
                     K=\{(0,1,1),(0,2,2)\}\subset M.
\]
Consider the relations on \(M\) obtained by following each of the four complete blocks and discarding destinations outside \(M\). Mark an edge if any regular or composite transition of the block used unequal terminal carries across its three columns. The [central-state certificate](check_midpoint_core.py) exhausts the exact residue rows by the same divisibility and destination tests. It imposes *no* requirement on the intermediate signs or residues other than the physical row tests, thus enlarging the relation if anything. Its results are as follows.

* For each of the four blocks, every edge ending in \(K\) started in \(K\) and is unmarked. The numbers of possible labeled edges, including both mark values when available, are respectively \(39,48,46,42\).
* In the union of the two ordinary block relations, start with \(M\setminus K\), and repeatedly keep the outside states with an edge to the previously retained outside set. The sizes are \(13,7,6,4,3,0\). Consequently five consecutive ordinary edges cannot have every vertex outside \(K\).

[Complete state list, counts and incoming edges](../../../reports/astra-diagonal-20261127/arithmetic/short-midpoint-core.json)

Reduce the constant \(\eta\) in the previous section further so that different exceptional starting ranks are separated by at least 50 high-return clocks in either cyclic time direction. This uses the positive minimum of \(\|i\lim(u/k)\|\), \(1\le i\le50\), exactly as before. If there is just one exceptional source, successive visits are a full high period apart. The two surrounding finite pieces use at most seven clocks each, and an ordinary block takes at most four. There is therefore a string of at least five consecutive ordinary blocks somewhere on the circle. Its state must visit \(K\). The no-entry property around the cyclic sequence forces every block boundary into \(K\), and every edge is unmarked.

Follow the difference between the first two columns. It is positive at a boundary because the folded ranks strictly increase; the source columns there are inside the high interval. On every regular or composite transition of this circuit the equal terminal carries cancel exactly. The difference is multiplied by the common rational slope, including at the end of every paired split. Its full multiplier is
\[
       (3/4)^u(9/8)^{k-u}=3^p/2^A<1 .
\]
Indeed \(k-u=h\), \(u+2h=p\), \(2u+3h=A\), and each column has \(u\) single and \(h\) double returns. A paired step has the product of its single and double slopes regardless of order. The positive difference must return to its original value, a contradiction.

There is thus a protected sign at a boundary, giving the common strict sign in all full ranks. Dyadic extension gives \(p^{-1}\sum_{r<p}q^{-r}L_{r+i}=q^i\bar L\) for every nonnegative \(i\), fixing this common sign as in (1). The nonzero integer \(J_r\) has absolute value at least one, and \(q^{-r}>1/2\). This proves (2). The proof of (1) needs the basic rank ordering, high-grade deletion and the rotation calendar. It does not need the large curvature seed used in the independent adjacent proof.

## Fourier and descent consequences

Put \(U_r=q^{-r}L_r\), a genuinely \(p\)-periodic sequence. For each integer frequency \(v\), the normalized discrete Fourier coefficient satisfies
\[
 |\widehat U(v)|\left|1-2q^b e^{2\pi i b v/p}+q^c e^{2\pi i c v/p}\right|
 \le \bar L|1-2q^b+q^c|.
\]
This follows by Fourier transformation of \(q^{-r}J_r\) and (2). It is valid for every one of the short midpoint pairs, on the same physical cycle. An amplitude improvement at all resonant rank frequencies would require sufficiently small simultaneous midpoint defects with a lower bound on the frequency-dependent factor.

The adjacent curvature \(H_r=\Delta^2L_r\) cannot itself be converted to a smaller positive orbit by adding a uniformly bounded transfer on the same mechanical clock. Write \(\bar V=p^{-1}\sum_{r<p}q^{-r}V_r\) for any octave-doubled sequence. The exact equation implies
\[
 (2q^k-3)\bar L=\bar\ell,\qquad
 \overline{H}=(q-1)^2\bar L,\qquad
 (2q^k-3)\overline{H}=(q-1)^2\bar\ell.
\]
Suppose \(Y=H+D\) is another octave-doubled sequence and \(2Y_{r+k}-3Y_r=g_r\ge1\) everywhere on the fundamental ranks. Then \(\bar g\ge1/2\) while \(1/2\le\bar\ell\le4\). Consequently
\[
 \bar D=\frac{\bar g-(q-1)^2\bar\ell}{2q^k-3}\gg s
\]
for large \(p\), using \(4s\le L_r<8s\). This lower bound also holds for real-valued transfers. Before weighting, the curvature forcing has rank sum \(\sum_{r<p}\Delta^2\ell_r=\ell_1-\ell_0\le0\), since \(\ell_0=4\). An actual descent via the small curvature labels must accommodate a changed clock or forcing. The midpoint-order theorem and Fourier bound do not exclude the bounded cycle.

## Independent checks and related work

The central-state checker recomputes all four edge sets twice. The first calculation uses the inverse residue rows obtained from the original odd-part transitions. The second ranges over every pair of first and middle residues modulo \(4d\), sets the third input from the **signed** curvature, and replays the physical one-column returns forward. Their complete marked edge sets agree. The [Lean finite kernel](CurvatureCone.lean) verifies the two signed cones, the stronger one-step equal-carry preimage property for all zero targets with three equal residues, and five stages of the outside-state elimination. Its backward transition computes each possible integer source height directly from the target and the three carries. The rank calendar, global cyclic contradiction and Fourier calculation are written proofs.

The third- and fourth-difference sign reversals constructed in PR213 enlarge to arbitrarily long finite ordinary parallel trajectories even when all lower differences are strict. They explain why consecutive higher difference positivity is an additional problem. The present test compares three ordered ranks in one cycle for every short, possibly uneven spacing. [Higher-difference construction](https://github.com/GettysburgResearch/collatz/blob/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127/arithmetic/HIGHER_DIFFERENCES.md)
