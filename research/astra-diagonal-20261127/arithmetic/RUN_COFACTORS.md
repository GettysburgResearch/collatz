# Exact past–future valuations and the common factor at a mismatch

**PROPOSED, finite ordinary arithmetic.** Let \(x_i\) be the distinct
odd states on a primitive positive cycle of odd period \(p>1\), with
\(2^{a_i}x_{i+1}=3x_i+1\) and \(a_i\in\{1,2\}\). Fix a nonzero
chronological lag \(h\bmod p\). Write \(d_i=x_i-x_{i+h}\).
For each cut \(i\), let \(L_i\) be the number of consecutive common
letters immediately *before* the cut, and \(R_i\) the number starting
at the cut. The numbers stop just before the first unequal pair on
their respective sides. These stopping times are finite: if two
infinite forward words were identical, \(2^{\sum_{j<n}a_{i+j}}\)
would divide the fixed nonzero \(d_i\) for every \(n\), by the
homogeneous difference equation and coprimality. Periodicity gives
the corresponding backward assertion. Then
\[
 v_3(d_i)=L_i,\qquad v_2(d_i)=1+\sum_{j<R_i}a_{i+j}.               \tag{1}
\]
The two valuations concern a *single physical signed integer*; no
separate frequency or uniformity hypotheses are needed.

Let \(b\) be the cut just after one mismatch, and \(n\) the number
of matched letters from \(b\) until the next mismatch. Put
\(E_j=\sum_{u<j}a_{b+u}\), for \(0\le j\le n\). There exists one
signed integer \(c\), prime to six, with the full list
\[
        d_{b+j}=2^{1+E_n-E_j}\,3^j\,c,\qquad 0\le j\le n.         \tag{2}
\]
This includes \(n=0\). The cuts \(b,\ldots,b+n\), as the preceding
mismatch varies, partition the cycle. In particular every fixed-lag
physical characteristic sum admits the exact diagonal expansion
\[
 \sum_{i\bmod p}e(t d_i)
   =\sum_{\text{mismatch blocks }(c,E)}
       \sum_{j=0}^{n} e\!\left(t\,2^{1+E_n-E_j}3^j c\right),
 \quad e(u)=\exp(2\pi i u).
\]
Every inner sum uses the same full outside-\(2,3\) factor.

Indeed an incoming letter one or two fixes \(x_i\equiv2\) or \(1\bmod3\),
respectively, so \(3\nmid d_b\). At an outgoing mismatch one state is
\(3\bmod4\) and the other \(1\bmod4\), so \(v_2(d_{b+n})=1\). On a
matched letter \(2^{a_{b+j}}d_{b+j+1}=3d_{b+j}\). Therefore
\(2^{E_j}d_{b+j}=3^jd_b\). At the far boundary this gives
\(v_2(d_b)=1+E_n\). Dividing it out proves (2) and (1).
A common denominator \(D\) prime to six gives the same statements for
the integer numerator differences of a rational cycle written over
\(D\): at an incoming mismatch the residues are \(2D,D\bmod3\);
at an outgoing mismatch the odd numerator residues differ by two
modulo four, since the affine correction is \(D\). Thus a magnitude
bound on the signed factor needs a genuinely ordinary input.

## An exact matching of the two cross-difference lists

Partition \(C=\{x_i\}\) according to the last letter: \(A\) consists
of incoming-1 states, \(B\) of incoming-2 states. Equivalently these
are the two ternary residues \(2,1\). Let \(u(n)=|n|/2^{v_2(n)}3^{v_3(n)}\)
for a nonzero integer, with the entire product in the denominator.
There is multiset equality
\[
 \left\{\frac{|x-y|}{2^{v_2(x-y)}}:x\in A,\ y\in B\right\}
 =
 \left\{\frac{|x-2y|}{3^{v_3(x-2y)}}:x\in A,\ y\in B\right\}.    \tag{3}
\]
It holds separately on every *unordered* chronological lag
\(\{h,-h\}\), with multiplicities from that lag. For a lag of order
two, take each unordered pair only once. Here \(x-y\) is even and
a ternary unit; \(x-2y\) is odd and divisible by three.

For a direct bijection use the permutation on unordered pairs obtained
by advancing both phases. For an incoming mixed pair \(\{x,y\}\) of
the stated types, its previous raw difference has unsigned core
\(u(x-2y)\), since \(3(x_{\rm prev}-y_{\rm prev})=2(x-2y)\).
Trace further backwards through the monochromatic incoming edges to
the previous mixed pair. The core is unchanged on those equal-letter
edges by the homogeneous recurrence. This maps each mixed pair to the
preceding mixed pair on its finite orbit, a bijection. It proves (3)
with complete prime powers and allows keeping the real sizes and
mismatch lengths from (2). In particular for every \(s\in\mathbb C\)
the two finite Dirichlet sums over (3) are equal.

A process which samples the two difference lists independently
discards this matching. There is also an elementary modulus-only
check: for every \(q\) coprime to six, count unordered pairs equal
modulo \(q\) before and after advancing both endpoints. At a
monochromatic pair this event is preserved. At the mixed pairs what
remains is equality of the counts of \(q\mid x-y\) and \(q\mid x-2y\).
Möbius inversion recovers the complete core histogram, but does not
identify the chronological partners.

## Higher-dimensional affine shapes

The same principle works on ordered \(k\)-tuples of distinct phases,
\(k\ge2\), at fixed offsets. For a rational vector \(v\), take its
class under a common translation and common positive multiplier
\(2^a3^b,\ a,b\in\mathbb Z\). Equivalently take its vector of
differences from the first coordinate, modulo common positive
\(2,3\)-unit scaling. At a nonmonochromatic incoming tuple
\((x_1,\ldots,x_k)\), put \(v'=(2^{a_{\rm in}(1)}x_1,\ldots,
2^{a_{\rm in}(k)}x_k)\). The multiset of classes of \(v'\) over
all mixed cuts equals that of the raw tuples over those cuts. Retain
each lag profile separately. In fact \(v'=3v_{\rm prev}+\mathbf1\).
Tracing backwards through the preceding monochromatic run, as above,
gives the bijection. If a profile has no mixed cuts, both multisets
are empty. At \(k=3\) this transport includes the rational ratio of
the two differences and their common content away from \(2,3\).
It also applies without the binary restriction if the incoming
exponents and their actual dyadic scalings are all retained.

The transforms and matchings here follow the actual cycle in time.
Positive rational cycles with nontrivial denominators already satisfy
the numerator version, e.g. the exponent word \(1,2,2\) gives the
ordinary numerator orbit \(23,37,29\) over \(5\): \(2\cdot37=3\cdot23+5\),
\(4\cdot29=3\cdot37+5\), \(4\cdot23=3\cdot29+5\). Its outside
factors match exactly. Bounding the signed sum at the distinct
physical ranks, or forcing an integer cycle's orbit into a smaller
ordinary component, remains open. Prior results on *lifted-rank*
signed gaps use a Subspace Theorem estimate with nonzero forcing.
[Preceding rank-pair theorem](../../astra-unconventional-20261126/arithmetic/PHASE_PAIR_MASS.md)
· [Halbeisen and Hungerbühler, ordinary and rational cycle correspondence](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)
