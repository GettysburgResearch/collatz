# Strict convexity of the complete three-grade physical rank sequence

**Proposed written theorem, with two independent exact finite certificates.** Consider ordinary positive primitive odd cycles in the bounded least-tripling-disagreement alternative. The assumptions used below are the actual exponents \(1,2\), the physical strip \(s\le x_i\le(16s+7)/3\) at the odd minimum \(s\), and the ordered rank rotation stated below. For all sufficiently large odd periods \(p\), their folded integer labels, in increasing rank order and extended by one octave, satisfy
\[
                 L_{r+2}-2L_{r+1}+L_r\ge1\qquad(0\le r<p).
\]
All three physical grades are allowed on the lower ranks. The result includes the two adjacent triples crossing the octave endpoint. In particular every fixed positive rank lag \(t\) has strictly increasing gaps \(L_{r+t}-L_r\), with increment at least \(t\) for \(r\ge0\).

**Prior theorem and present extension.** PR201 already proved adjacent strict convexity for this full physical strip, using a separate seam analysis and the progression-free binary past. The high-interval return argument below gives a different finite proof in the bounded minimum normalization. Its two-sided version proves the exact exponential midpoint order for every short pair of unequal spacings at every origin. [PR201, full binary physical band](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md) · [All short midpoint comparisons](SHORT_RANK_MIDPOINTS.md)

## Inputs from the ordered cycle

Write \(A=\sum_{i<p}a_i,\ k=A-p,\ h=p-k,\ u=k-h\). The physical grade \(z_i\in\{0,1,2\}\) puts \(2^{-z_i}x_i\in[s,2s)\). At rank \(r\) let \(L_r=2^{2-z_i}x_i\) and let \(\ell_r=2^{2-z_i}\), the lowbit (largest power of two dividing \(L_r\)). The integer rank is \(r=ik\bmod p\) after placing the minimum at clock zero, so \(\gcd(k,p)=1\). Set \(L_{p+r}=2L_r\). In one chronological transition the rank changes by \(k\bmod p\), the mechanical exponent is 1 below \(h\) and 2 from \(h\) up, and the actual exponent \(a\) is 1 or 2. The exact equations and large-period estimates are
\[
  2L_{r+k}=3L_r+\ell_r,\quad L_0=4s,\quad
  L_r=4s\,2^{r/p}+O(p)\ (0\le r<2p),\quad
  A/p=\log_2 3+O(1/s),\quad s/p^2\longrightarrow\infty.
\]
The last estimate follows already from the elementary word count \(p\ll s^{479/1000}\). The order, rank-envelope estimate and elementary count used here have no analytic-hypothesis dependency. [Ordered cycle and amplitude recurrence](../../astra-unconventional-20261126/arithmetic/README.md) · [Elementary strip count](../../astra-unconventional-20261126/arithmetic/INVERSE_WRAP.md)

For \(r\ge h+1\) up to \(p-1\), the grade \(z_i=2\) is impossible. Indeed \(4s2^{h/p}=16s/3+O(1)\), and moving up one additional rank increases the exponential reference by \(\gg s/p\), which exceeds the envelope error and the constant allowance in the strip. With grade 2 the raw odd state would equal \(L_r\). At \(r=h\) the next chronological state is the physical minimum. The actual incoming exponent is 2 since exponent 1 would give a predecessor below \(s\). The mechanical exponent is also 2, forcing the source and target grades to agree, and \(\ell_h=\ell_0=4\).

## The first return on high ranks

Write
\[
 B_j=L_{h+j}/2,\quad b_j=\operatorname{lowbit}(B_j)\in\{1,2\},
 \qquad 0\le j<k,\qquad \phi(n)=(3n+\operatorname{lowbit}(n))/2.
\]
The first chronological step gives \(L_j=\phi(B_j)\) for every \(0\le j<k\). The first return to the high interval sends \(j\) to \(j+u\bmod k\), a single cycle since \(\gcd(u,k)=1\). Its two letters are as follows.

* If \(j\ge h=k-u\), the next rank \(j\) is already high. Write \(S\) for this return. Its output \(B'\) satisfies \(4B'=3B+b\) and \(b'=\operatorname{lowbit}(B')\in\{b,b/2\}\).
* If \(j<h\), the intermediate \(M=\phi(B)\) is low and the next rank is high. Write \(D\) for this return. With \(c=\operatorname{lowbit}(M)\) there are the restrictions \(c\in\{b,2b\}\), \(4B'=3M+c\), and \(2b'\in\{c,2c\}\). Here \(8B'=9B+3b+2c\) and the possible carries are \(5,7,10,14\).

These conditions follow directly by comparing the physical exponents 1 and 2 with the mechanical exponent on each edge. They are also sufficient for the local numerical transitions used in the verification. At the high-interval upper seam extend \(B_{k+j}=L_{p+j}/2=L_j=\phi(B_j)\) for \(j=0,1\). The true second differences across that seam use these extended values.

## A finite invariant for the actual rotation calendar

Set \(H(X,Y,Z)=X-2Y+Z\) and encode the triple by \((H,X\bmod4,Y\bmod4)\). All high residues are \(1,2,3\), and \(Z\bmod4\) follows from the stored data. At a boundary whose first letter is \(S\), define a protected state to have \(H>0\) and to lie outside
\[
 E=\{(1,1,1),(1,2,1),(2,2,1),(3,1,2),(3,2,2),(4,2,2)\}.
\]
The return rotation has \(u/k\to(2\log_2(3)-3)/(\log_2(3)-1)=0.2904\ldots\). The times between crossings of \(k-u\) are \(\lfloor k/u\rfloor\) or \(\lceil k/u\rceil\), hence 3 or 4. This follows by counting wraps along the lifted rotations \(j+tu\). Away from a split, the three consecutive ranks undergo the same transition. Thus the usual blocks from one single-return boundary to the next are \(SDD\) and \(SDDD\).

The two split sources for a triple have starts \(j=h-2,h-1\). Over two returns their three column words are respectively \((DS,DS,SD)\) and \((DS,SD,SD)\). At the midpoint the start is \(k-2,k-1\) respectively, so the output on the \(S\) side must be lifted by \(\phi\). After two returns there are again three consecutive ordinary high ranks. Taking each split source at time 0, the preceding letters at times \(-3,-2,-1\) are \(S,D,D\); times 2,3,4 have letters \(D,D,S\). For example the limiting fractional positions at those six times are respectively \(1-4u/k\bmod1,\ 1-3u/k,\ 1-2u/k,\ u/k,\ 2u/k,\ 3u/k\), all interior to their stated intervals. The two exceptional neighborhoods are disjoint for large \(p\). If their clock separation were bounded by 20, some \(1\le i\le20\) would have \(\|iu/k\|\le1/k\), contrary to the irrational limit. The circular chronological walk can therefore be cut into the two usual blocks and two types of exceptional blocks \(SDD\,C\,DD\), where \(C\) denotes the corresponding simultaneous two-return split.

**Finite lemma.** For every one of these four block types, protected inputs have strict positive curvature at every interior point, including the lifted midpoint of \(C\); their endpoints are protected.

Here are the exact finite proof and its independent reverse check. Each regular column has the form \(dV=nU+c\). For \(S,D\) the pairs \((n,d)\) are \((3,4),(9,8)\). For \(DS,SD\) both are \((27,32)\); the respective carry sets are
\[
 \{23,29,37,38,46,58\},\qquad \{29,37,38,46,58,74\}.
\]
At the lifted midpoint both slopes are \(9/8\). The \(D\) side has its usual carry \(3b+2c\); the \(S\) side has carry \(3b+4b'\), since it uses \(\phi(B')\). These middle carries all belong to \(\{5,7,10,14\}\). In any simultaneous step the curvature therefore obeys \(dH'=nH+(c_0-2c_1+c_2)\), giving \(H'\ge3H/4-4\) for \(H\ge0\), including at the middle compared directly with the split source. Starting at \(H\ge128\), even six iterations of this inequality leave \(H'\ge2465/256>4\). For positive smaller heights the [forward certificate](check_three_grade_curvature.py) takes \(1\le H<128\), all first and second residues modulo \(4d\), and third representative \(Z=2Y-X+H\). It follows the actual permitted branch tests. Altering \(X,Y\) by multiples of \(4d\) preserves all legalities, endpoint residues and endpoint curvature; the third representative changes by the corresponding affine combination. To see the periodicity directly, on each specified column the denominators of all earlier outputs divide \(d\), the lowbits of high outputs are read modulo 4, and the only unfolded intermediate \(M\) has its lowbit in \(1,2,4\) read modulo 8. The change in \(M\) is a multiple of 8 in every \(D\) tested, including following an \(S\). The lifted middle curvature has the same invariance by its common slope. Thus the finite check covers arbitrary positive integers in these branches.

The [reverse certificate](audit_three_grade_curvature.py) instead derives input/output residues and carries for each column from the actual odd-part \(3x+1\) operation, independently of the above local branch-test implementation. It permits every triple of these rows with input and output curvature congruences. Working backward from \(E\), any positive source reaching a nonpositive intermediate or bad target of height at most \(K\) must have \(H\le\lfloor4(K+4)/3\rfloor\). The exhaustive preimage sizes at successive reversed steps are below. Every resulting nonempty bad set has maximum height 4. The final preimage equals \(E\) in all four cases.

| Forward block | Bad-state counts in reverse order |
|---|---|
| \(SDD\) | 11, 13, 6 |
| \(SDDD\) | 11, 13, 13, 6 |
| \(SDD\,(DS,DS,SD)\,DD\) | 11, 13, 9, 11, 13, 6 |
| \(SDD\,(DS,SD,SD)\,DD\) | 11, 13, 7, 11, 13, 6 |

[Forward states, carries and scalar bounds](../../../reports/astra-diagonal-20261127/arithmetic/three-grade-curvature.json) · [Independent reverse states and complete column rows](../../../reports/astra-diagonal-20261127/arithmetic/three-grade-curvature-audit.json)

## Seeding the invariant and putting the octave back

For \(g_j=B_{j+1}-B_j\), the envelope gives
\[
 g_{k-2}-g_0
 =2s(2^{1/p}-1)\left(2^{(h+k-2)/p}-2^{h/p}\right)+O(p)
 \gg s/p.
\]
Here \(s/p\gg p\). The left side is the sum of \(k-2\) complete high curvatures. Thus some actual unwrapped triple with start \(j\le k-3\) has \(H\gg s/p^2\), tending to infinity. Take the next block boundary along the calendar. Before reaching it the triple follows only a bounded number of regular or paired steps; a seed with \(j\le k-3\) cannot start at the wrapped middle of a paired step. The scalar estimate transports the diverging seed to a protected boundary. Traverse the entire high rotation starting there, using the finite lemma. This proves strict positive curvature of the \(B\)'s at every high start, with the specified lifts at \(k-2,k-1\).

On \(h\le r<p\), \(L_r=2B_{r-h}\) with the same relation for the two extended labels at the top. This covers the two complete-octave seams. On \(0\le j\le k-3\) the identity \(L_j=\phi(B_j)\) gives
\[
     2\Delta^2 L_j=3\Delta^2 B_j+\Delta^2 b_j\ge3-2>0 .
\]
For large \(p\), \(k-3\ge h-1\), so the ranges cover the full octave. Integrality gives the asserted unit bound. By the dyadic extension it also holds for all \(r\ge0\). If \(G_r=L_{r+1}-L_r\), summation gives \(G_{r+t}-G_r\ge t\), the lower bound on the increment of \(L_{r+t}-L_r\). At \(r=0,t=p\), in particular, \(G_0\ge p\).

The proof establishes strict convexity for the bounded three-grade branch. The positive second differences can vary with rank, and integrality and this first curvature bound alone permit polynomial-height sequences. An exclusion argument still has to use the valuation or closure constraints beyond this invariant.

The [structural Lean kernel](ThreeGradeCurvature.lean) verifies common-slope transport, lifted single and paired columns, the scalar cutoff and the all-lag consequence. The [finite Lean kernel](CurvatureCone.lean) decides the complete positive-cone return tables and all eight backward transitions in the Lean kernel. The rank normalization, high calendar, seeding argument and reconstruction are the written proof above. The [signed midpoint extension](SHORT_RANK_MIDPOINTS.md) treats the negative cone and arbitrary short spacings.
