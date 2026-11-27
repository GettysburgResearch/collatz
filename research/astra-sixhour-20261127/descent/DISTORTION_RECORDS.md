# Matched distortion records on one actual upper word

Write \(D_j(n)=2^jT^j(n)/(3^{P_j(n)}n)\), where \(P_j\) counts odd departures. Fix the original positive odd input \(z\), its lower \(T\)-trajectory and one given good upper trajectory from \(3z\). Fix a clock \(j\) of this upper path, set \(Y=T^j(3z)\), \(q=P_j(3z)\), and assume \(D_j(3z)>1\). If the lower correction ever reaches this level, let \(t\) be its first such clock. For a periodic positive lower, these clocks exist at every level since each lap multiplies the correction by a factor greater than one. Existence can fail for a nonperiodic lower, whose distortion is bounded on a simple trajectory.

**Exact mixed-clock record.** Let \(p=P_t(z)\), \(X=T^t z\), \(d=j-t\) and \(k=p-q-1\), with the last two differences signed. Then
\[
                     0\le X-2^d3^kY<\tfrac12.                            \tag{1}
\]
If \(d,k\ge0\), necessarily \(k=0\) and \(X=2^dY\). The original lower then takes \(d\) actual halvings to \(Y\) and inherits the original upper hit.

To see the strict half-unit, the last lower departure \(w\) is odd and \(X=(3w+1)/2\). The exact physical ratio gives \(2^d3^kY=X D_j(3z)/D_t(z)\). By first passage, \(D_{t-1}(z)<D_j(3z)\le D_t(z)\). The last distortion increment has \(D_{t-1}(z)/D_t(z)=3w/(3w+1)\), proving (1). In the nonnegative quadrant the two terms of the difference are integers. Their equality precludes \(k\ge1\) since every output immediately after an odd departure is two modulo three. [Kernel verification by integer cross-products](DistortionRecord.lean)

For a given \(j\), this successful criterion is equivalent to the physical synchronous event
\[
      T^j z=T^j(3z),\qquad P_j(z)=P_j(3z)+1.                            \tag{2}
\]
The forward implication pads the lower by the \(d\) halvings. Conversely (2) gives equal correction at \(j\); after the first lower clock attaining it all remaining lower steps to \(j\) are even. In particular the first record has \(p=q+1\).

At convergent ordinary controls write \(H(n)\) for the first clock at one and \(J(n)=H(n)-2P_{H(n)}(n)\). A successful upper clock anywhere, allowing later true laps, exists **if and only if** \(J(z)-J(3z)=-2\) for \(z>1\). Necessity follows from (2) and charge invariance. For sufficiency the two first-hit clocks have the same parity; padding the earlier by laps to the larger first-hit clock gives (2). A successful clock no later than the actual first upper hit exists precisely when also \(H(z)\le H(3z)\). In particular the convergent inputs \(17,65,161\) fail the unrestricted-clock test. This equivalence concerns the favorable record, a stronger requirement than unbalanced ordinary coalescence. [Charge arithmetic and ordinary controls](PAIRED_CHARGE.md)

## What a record just beyond the same upper clock can transport

Assume \(a=t-j>0,\ k\ge1\). After replacing \(j\) by a later clock in the same even upper run while it is still before \(t\), one can normalize \(Y\) to odd whenever that run ends before \(t\). In the following take \(Y\) odd. Equation (1) gives a nonnegative integer
\[
                   2^aX=3^kY+R,\quad 0\le R<2^{a-1}.                  \tag{3}
\]
If \(R\) is the standard affine offset of a length-\(a\) word with \(r\le k\) odd departures, then \(N=3^{k-r}Y\) is a **positive ordinary source** with \(T^aN=X,\ P_a(N)=r\). Indeed (3) is precisely the integer decoding equation for this source, including all branch conditions. If \(X\) is bad, \(N\) is bad and the same \(Y\) has the original upper suffix. In this case \(r<k\). [Physical integer decoder](../../astra-unconventional-20261126/descent/Portal.lean)

For instance \(z=161,\ j=10,\ Y=13\) has first matching lower record \(t=13,\ X=395,\ a=3,\ k=5,\ R=1\). The source \(3^4\cdot13=1053\) really reaches \(395\) in three shortcuts. But for the canonical ordinary control \(z=164513,\ j=10,\ Y=39041\), the first lower record is \(t=17,\ X=74117,\ a=7,\ k=5\), with \(R=13\). Its lower prefix has no consecutive even departures. The arms have no common state through their two displayed clocks. No word has offset 13. For one odd the offset is a power of two; for two odds an odd offset has the form \(3+2^b\), \(b\ge1\); three or more odds give at least \(27-8=19\). The original control is ordinary and both its full arms converge. [Independent exact replay](check_records.py)

**The decoded ancestor cannot improve the original floor by size.** The post-odd residue \(X\equiv2\bmod3\) and (3) preclude \(a=1,2\): the first range requires \(R=0\) with \(R\equiv1\bmod3\), and the second requires \(R\in\{0,1\}\) with \(R\equiv2\bmod3\). For \(a\ge3\), the smallest offset of \(r\) odd departures is \(3^r-2^r\), attained by putting all odds first. Hence \(r\le a-2\): for \(r\ge a-1\) the minimum is at least \(3^{a-1}-2^{a-1}\ge2^{a-1}\). Consequently
\[
 3^r\le R+2^r<3\cdot2^{a-2},\qquad
 N=\frac{2^a X-R}{3^r}>\frac43(X-\tfrac12)=2w .
\]
This strict bound is also checked for the actual inverse-word datatype. [Kernel statement decoded_record_size](DistortionRecord.lean) In particular \(N>2s\) if \(s\) is the original least bad integer. The upper suffix is strictly shorter for \(j>0\), but at its eventual endpoint \(Y=1\) a bad multiple \(3^{k-r}\) has no established universal contradiction. Neither the size of the recovered source nor the cost of its new ternary exponent provides a descending rank.

An upper odd departure at a small ordinary \(y\) changes its distortion by a factor \(1+1/(3y)\). On a bounded lower cycle with odd sites comparable to \(s\), the corresponding lower record can advance across order \(s/y\) odd departures inside that single true upper step. This can skip the required clock/grade quadrant. Arbitrarily chosen real inverse offsets cannot simply interpolate this jump: the closure of the first-hit inverse offsets at a **fixed** positive odd terminal has zero Lebesgue measure. The target offsets from a particular original pair have arithmetic structure, but no interpolation theorem for these targets is established. [PR193, closed support of first-hit offsets](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/escape/CLOSED_CORRECTION_SUPPORT.md)

The mixed-clock theorem and the residual obstruction are new applications here of the elementary physical affine formula; earlier first-crossing work at the same clock compared the cumulative odd counts. The first unsupported implication is that the full input-dependent upper word of a **specified least** reverse disagreement must have a successful physical comparison or any genuinely smaller positive canonical representative. [Earlier matched-clock crossing](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-diagonal-closure-20261125/transport/README.md)
