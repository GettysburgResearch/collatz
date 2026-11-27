# Reciprocal rounded clocks and triadic meetings

The dyadic upper and triadic lower floating-point maps have exactly reciprocal rotation numbers at matching precisions. Each positive ordinary Collatz cycle pays the same nonnegative integer winding defect in two different grids. Both statements hold at finite height and with arbitrary positive native valuations.

## Reciprocal grid rotations

For an integer \(m\ge1\), let \(N=2m-1\), \(M=3m-1\). Let \(H_N(v)\) be the least dyadic lift of a positive odd integer at most \(N\) that is at least \(3v\). Let \(K_M(w)\) be the greatest triadic lift of a positive integer prime to three at most \(M\) that is at most \(2w\). These definitions extend to positive real inputs. The logarithmic rotations, measured in base two and base three respectively, satisfy
\[
                         \rho(H_N)\,\rho(K_M)=1.                              \tag{1}
\]
Thus a reduced dyadic clock \(a/b\) is paired with the reduced triadic clock \(b/a\). The maps need not have identical periodic vertices.

Take \(\Gamma=\{6^j n:j\in\mathbb Z,\ m\le n<6m,\ n\in\mathbb Z\}\). On this ordered grid put \(F(v)=\lceil3v\rceil_\Gamma\), \(G(v)=\lfloor2v\rfloor_\Gamma\). For any two grid points
\[
 F(v)\le w\quad\Longleftrightarrow\quad v\le \lfloor w/3\rfloor_\Gamma=G(w)/6 .
\]
All maps commute with multiplication by six. Iterating the equivalence with \(w=6^jv\) gives
\[
 \left\lceil\log_6(F^n(v)/v)\right\rceil
 =n-\left\lfloor\log_6(G^n(v)/v)\right\rfloor .
\]
Therefore the two base-six rotations sum to one. The rotations exist because the quotient grid is finite. Different initial vertices have the same rotation by monotonicity, placing one orbit between two adjacent sixfold lifts of the other.

On the fundamental interval \([m,6m)\), one \(F\) step sends \(v<2m\) to \(3v\) and otherwise sends \(v\) to \(\lceil v/2\rceil\), advancing one sixfold winding on the latter branch. From \([m,2m)\) the first return consists of one exact tripling and all necessary ceiling halvings. The identity \(\lceil\lceil u/2\rceil/2\rceil=\lceil u/4\rceil\) identifies this return with \(H_N\) on its binary fundamental interval. If its period is \(b\) and its dyadic winding \(a\), the associated \(F\) orbit has \(b\) tripling and \(a\) halving steps. It rotates by \(a/(a+b)\). Likewise \(G\) doubles at \(v<3m\) and sends the other vertices to \(\lfloor v/3\rfloor\). Its first return to \([m,3m)\) is \(K_M\). A triadic period \(k\) and winding \(h\) give base-six rotation \(h/(h+k)\). Equating the sum to one proves (1).

## A second ordinary winding identity

Let \(C\) be a positive primitive ordinary cycle on the odd Collatz map, with odd period \(p\), total halving exponent \(A\), minimum odd state \(s\) and maximum odd state \(X\). For any integer \(M\ge(3X+1)/2\), let \(R\) be any periodic component of \(K_M\), with primitive period \(k\) and ternary winding \(h\). Let \(\widetilde R\) contain all triadic lifts of its unit representatives. Then
\[
          Ah-pk=\sum_{x\in C}\#\{V\in\widetilde R:3x/2\le V<(3x+1)/2\}.      \tag{2}
\]
In particular \(p/A\le h/k\). If \(M<(27s+1)/2\), the right side is exactly
\[
                 \#\{x\in C:(9x+1)/2\in R\},                                    \tag{3}
\]
using the primitive 3-free representatives in \(R\). It vanishes if \(M<(9s+1)/2\). For matched grids \(M=3m-1,N=2m-1\) and \(N\ge X\) the left side is the very same \(A p_N-p A_N\) as in the [dyadic meeting identity](HOMOGENEOUS_MEETINGS.md). In particular the empty triadic interval at matched precision recovers the same clock plateau on \(X\le N<3s\).

To prove (2), reverse each native edge \(2^a y=3x+1\) into \(a\) doubling steps. List the successive 3-free integer sources \(y,2y,\ldots,2^{a-1}y\). On all but the last double exactly. On the last step use the raw transformation \(z\mapsto2z-1=3x\), winding once by three. Thus the list has \(A\) states and \(p\) winds. It can be viewed as a map on lifted states by triadic scaling. All unit sources are at most \((3X+1)/2\). Every raw output \(Y\) is grid-eligible, since it is either the next listed integer or \(3x\) with \(x\le X\).

For a true microstate \(z\), raw true output \(Y\) and unit reference state \(n\), sum
\[
 \left\lfloor\log_3(K_M(n)/Y)\right\rfloor-
 \left\lfloor\log_3(n/z)\right\rfloor
\]
over the two independent periods. Renumbering both cyclic outputs cancels the base terms and leaves \(Ah-pk\). A negative crossing would require a lifted \(V\ge z\) with \(K_M(V)<Y\), impossible because \(2V\ge2z\ge Y\) and \(Y\) is eligible. A positive crossing is exactly \(V<z\) and \(2V\ge Y\). An exact doubling admits none. At a correction, \(z=(3x+1)/2\) and \(Y=3x\), giving (2) with the stated strict endpoint. The width of the interval is one half, and its right endpoint is integral. The sole candidate of reduced denominator three is \(z-1/3\), from the primitive numerator \(3z-1=(9x+1)/2\). Reduced denominator nine or greater needs a numerator at least \(\lceil27x/2\rceil=(27x+1)/2\). This proves (3).

A periodic component of any monotone degree-one finite-grid map has reduced rotation with denominator equal to its least period. Indeed it permutes its cyclically ordered vertices by a single translation. Consequently the matched periods in (2) are exactly \(k=A_N,h=p_N\), with no multiplicity factor. Larger cutoffs can admit further triadic fractions, all counted in (2). A proof controlling these meetings uniformly on a candidate's physical height interval remains open.

[Exact adjunction, dyadic/triadic return and winding checks](check_dual_cuts.py) · [Recorded controls](dual_cut_controls.json)
