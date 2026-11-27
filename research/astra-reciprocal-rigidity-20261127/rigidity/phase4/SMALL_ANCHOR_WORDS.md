# A full binary-height lower bound for positive realizers of compressed words

Let \(T(x)=x/2\) at even positive integers and \(T(x)=(3x+1)/2\) at odd ones. A chronological word of length \(L\) lists the parities of the first \(L\) inputs. Break it into at most \(K\) consecutive nonempty pieces, for fixed \(K\). The affine composition for a length-\(\ell\) piece with \(q\) odd inputs is \((3^q x+C)/2^\ell\), with \(C\ge0\). Its unique rational fixed point
\[
                              c=\frac C{2^\ell-3^q}                  \tag{1}
\]
is called its periodic anchor. Unique factorization gives a nonzero denominator. Use logarithmic height \(h(a/b)=\log\max(|a|,b)\) in lowest terms, with \(h(0)=0\).

**Theorem.** For each fixed \(K\ge1\) and \(0<\delta<1\), there are \(\epsilon>0\) and \(L_0\) with the following property. Suppose a positive integer \(x\le2^{(1-\delta)L}\) realizes such a word, \(L\ge L_0\), and every piece has anchor of height at most \(\epsilon L\). Then **at the start of one of its pieces the actual positive integer trajectory equals that piece's rational anchor**. From that instant the displayed piece is an actual periodic itinerary.

In particular, across ordinary realizers with at most a fixed number of maximal odd runs and \(L\to\infty\),
\[
                           \liminf \frac{\log_2 x}{L}\ge1.           \tag{2}
\]
No assumption on the final value, coefficient crossing, or relative order of the two endpoints enters. The rate is best possible: \(2^L-1\) realizes \(L\) consecutive odd inputs. The all-even class has least positive realizer \(2^L\).

More generally, consider at most \(K\) concatenated powers \(v_i^{h_i}\) of nonempty words. The words and the exponents may all vary with \(L\). If \(\max_i |v_i|=o(L)\), the orbit either hits a participating periodic anchor at its corresponding block start or satisfies the lower rate (2) on the anchor-free subsequence. Indeed the power's anchor equals that of one copy. A length-\(k\) word has \(0\le C<3^k\): appending a digit sends \(C\) to \(C\) or \(3C+2^k\), and the sharper induction \(C\le3^k-2^k\) is preserved. Its anchor height is therefore \(O(k)\). For an ordinary path entering its anchor in a repeated block, the return already occurs after a single copy of its template. For (2) split at the parity changes. The pure even and odd anchors are respectively \(0,-1\), neither of which a positive state can equal. At most \(J\) odd runs require at most \(2J+1\) pieces.

**Status.** Written proof using the classical rational \(S\)-adic Subspace Theorem. All linear forms after choosing a subsequence have fixed rational coefficients. The variable anchor denominators, unrestricted integer endpoint, and arithmetic clearing factors are tracked below. The argument applies to arbitrary positive inputs and the asserted fixed-complexity family of their finite words. The theorem does not assert that arbitrary escaping itineraries admit these decompositions.

## 1. A chronological identity

Index each boundary by its number \(p\) of preceding steps, and let \(r\) be the previous odd count. Set \(U_p=2^p3^{-r}\). For a piece from boundary \(p\) to boundary \(p'\) with anchor \(c\), the affine identity yields
\[
 U_{p'}T^{p'}x-U_pT^p x=c(U_{p'}-U_p)\ \ge0.                       \tag{3}
\]
The inequality follows because (3) is also the normalized sum of the nonnegative additive odd increments of that piece. For an all-even piece the difference vanishes. Write \(u\) for the whole word's odd count and \(y=T^Lx\). Summation gives
\[
       W:=2^L 3^{-u}y = x+\sum_i c_i(U_{p'_i}-U_{p_i}).             \tag{4}
\]
Both \(x,y\) are positive integers. In particular \(|x|_3\le1\) and \(|W|_2\le2^{-L}\), with \(|p|_p=p^{-1}\).

## 2. The exact Subspace Theorem normalization

A counterexample to the theorem supplies a sequence \(L\to\infty\) with fixed \(\delta,K\), \(x\le2^{(1-\delta)L}\), all \(h(c_i)=o(L)\), and no exact hit. Indeed choose \(\epsilon\) tending to zero and successively increasing lower cutoffs. Pass to subsequences with a fixed number of pieces and fixed zero-anchor positions. Delete zero-anchor terms in (4). If all anchors vanish, then all pieces have no odd input by positivity of the affine increment and \(2^L\mid x\), a contradiction.

List separately each nonzero signed-anchor coordinate \(a_j=c_i U_p\) for the two ends of every remaining piece. The signs in (4) are given by its endpoint order. For \(S=\{\infty,2,3\}\), the product formula and the two-prime form of \(U_p\) give
\[
       e^{-o(L)}\le\prod_{v\in S}|a_j|_v\le e^{o(L)}.              \tag{5}
\]
At every individual place \(|\log |c_i|_v|\le h(c_i)=o(L)\) for a nonzero rational anchor. There are a bounded number of coordinates. A common denominator for all coordinates, also for \(x\), is
\[
                  B=3^L\prod_i\operatorname{den}(c_i).
\]
It satisfies \(B\le e^{O(L)}\) and \(\prod_{v\in S}|B|_v\le\prod_i\operatorname{den}(c_i)=e^{o(L)}\). Every selected coordinate after multiplication by \(B\) is an integer of ordinary size \(\le e^{O(L)}\).

We use Schlickewei's rational \(S\)-adic Subspace Theorem in its integer-vector normalization. For \(d\ge2\), at each \(v\in S\) choose \(d\) independent fixed rational linear forms \(L_{v,i}\). Integer vectors \(z\ne0\) with
\[
         \prod_{v\in S}\prod_{i=1}^d|L_{v,i}(z)|_v
                               \le \|z\|_\infty^{-\eta}
\]
lie in finitely many proper rational linear subspaces, for fixed \(\eta>0\). The version for primitive vectors suffices: dividing all entries by their positive common divisor reduces the product by \((\prod_{v\in S}|\gcd(z)|_v)^d\ge1\) and reduces the maximum norm. Thus an \(e^{-\gamma L}\) upper bound on the unscaled rational-coordinate product, for fixed \(\gamma>0\), implies the theorem's hypothesis for \(Bz\) with a fixed positive \(\eta\). The cost of scaling all \(d\) forms at every place is \((\prod_S|B|_v)^d=e^{o(L)}\). The rational projective version is equivalent. [Schlickewei, *On linear forms with algebraic coefficients and Diophantine equations*](https://www.sciencedirect.com/science/article/pii/0022314X77900737) · [Varjú, *On the multiplicative group generated by two primes in Z/QZ*, Theorem 5](https://arxiv.org/abs/2104.04367) · [Evertse's account of Schlickewei's theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

Choose a rational linear subspace \(V\) of least dimension containing infinitely many tuples \((x,a_1,\ldots,a_m)\) of the counterexample sequence and retain those tuples. Thus the restriction to \(V\) of any nonzero linear form vanishes on only finitely many selected points. Choose \(b_1,\ldots,b_d\) among the endpoint coordinates whose restrictions form a basis of the span of all endpoint coordinate functions on \(V\).

If \(x\) is independent of this basis on \(V\), take coordinates \((x,b_1,\ldots,b_d)\). At infinity and 3 use all coordinate forms. At 2 replace the \(x\)-coordinate by the right side of (4), expressed using the fixed rational expansions of the \(a_j\) in the \(b_i\). This is an independent basis of forms at 2 because the coefficient of \(x\) is one. Their full product is bounded by
\[
  |x|_\infty |x|_3 |W|_2\prod_{j,v\in S}|b_j|_v
                      \le 2^{-\delta L}e^{o(L)}.                    \tag{6}
\]
An integer endpoint of unrestricted size costs nothing at 2. Section 2's integer normalization now puts this tuple in finitely many proper rational subspaces. Each pulls back to a proper subspace of \(V\) by coordinate independence, contradicting the choice of \(V\). Therefore **the source coordinate \(x\) belongs to the fixed rational span of the endpoint coordinates**. By (4), \(W\) belongs to it as well.

## 3. No exponential local cancellation in the independent coordinates

Let \(A=\sum_j q_j b_j\) be any fixed nonzero rational linear form in the basis coordinates. For each \(v\in S\) on the retained sequence,
\[
       \log|A|_v\ge\max_{j:q_j\ne0}\log|b_j|_v-o(L).                \tag{7}
\]
A failure with fixed positive margin has a subsequence where one fixed \(b_k\) attains the maximum. At that place replace the \(k\)-th coordinate form by \(A\), leaving the other forms at all places unchanged. The product of all form sizes is \((|A|_v/|b_k|_v)\prod_{j,w\in S}|b_j|_w\), exponentially small by (5). The same clearing and Subspace Theorem contradict minimality of \(V\). For a single basis coordinate (7) is immediate from the constant coefficient. Zero evaluations of a nonzero form can be dropped by minimality.

Consider an original endpoint coordinate \(a_i\) and any \(b_j\) occurring in its fixed basis expression. By (7), \(\log|b_j/a_i|_v\le o(L)\) at all three places. By (5) the sum of these three logarithms is \(o(L)\), so each is also bounded below by \(-o(L)\). In particular the normalized positions \(p/L\) of \(a_i\) and \(b_j\) differ by \(o(1)\), using the 2-adic valuation and \(h(c_i)=o(L)\). The same statement for their normalized prior odd counts follows at 3.

After extraction let all boundary position fractions \(p/L\) converge. The rational span of the \(b_j\) is the direct sum of the spans grouped by their limit position. Every endpoint coordinate lies *entirely* in the group associated to its own limit position. This conclusion handles all possible exact rational dependencies of endpoint coordinates. It requires no multiplicative independence or assumption on moving anchor coefficients.

If \(b_j\) occurs in \(x\), its prior odd count satisfies \(r_j=o(L)\). Indeed (7) at 3 and \(|x|_3\le1\) give \(r_j\log3\le o(L)\). Applying (7) at infinity then gives
\[
                    p_j\log2\le (1-\delta)L\log2+o(L).
\]
Thus every position group represented in \(x\) is at most \(1-\delta\). If \(b_j\) occurs in \(W\), (7) at 2 and \(|W|_2\le2^{-L}\) give \(p_j\ge L-o(L)\), so every group in \(W\) has limit position one.

## 4. The chronological cut forces a physical return

Choose a number \(\alpha\in(1-\delta,1)\) different from every boundary-position limit, including boundaries of the zero-anchor pieces. For all sufficiently large selected points, a unique piece starts below \(\alpha L\) and ends above it. Denote its start by \(p\) and its anchor by \(c\). Project (4), as an equality of fixed rational linear forms on \(V\), onto all position groups below \(\alpha\). The entire \(x\) is retained and the entire \(W\) is discarded. Both ends of each completed piece below \(p\) are retained, and exactly the initial signed term \(-c U_p\) of the crossing piece is retained when \(c\ne0\). All later endpoints are discarded. Consequently on the retained data
\[
              0=x+\sum_{\text{pieces before }p}
                      c_i(U_{p'_i}-U_{p_i})-c U_p
                      = U_p(T^p x-c).                               \tag{8}
\]
This equality also includes the crossing case \(c=0\). Since \(U_p>0\), the actual integer at that boundary is exactly the anchor. The prescribed word is realized there, so applying its true shortcut branches returns to the same positive integer. This contradicts the assumed absence of such hits and proves the theorem.

## Consequences and limits

For a single fixed positive source whose forward orbit never enters a periodic orbit, every large enough prefix and every partition into at most \(K\) pieces includes an anchor of height at least \(\epsilon_K L\). The constant and onset are ineffective. The same statement applies starting at any current vertex of an escaping orbit once its prefix length exceeds its binary source height by the required fixed factor. There is no proof here that such an orbit has boundedly many pieces with inexpensive anchors. Arbitrary binary words can have linearly many runs or long primitive templates.

The height rate is sharp for integer realizers. The alternative involving a periodic hit is necessary already at the ordinary cycle \(1,2\), where arbitrarily many copies of its word begin at a unit-size source. This is an exact orbit alternative, not an inference from near recurrence or a finite census.

## 5. An explicit allowable height fraction

Only the onset \(L_0\) needs to remain ineffective. The following choice works with heights in natural-log units:
\[
 A=(2K+1)(K+1),\qquad
 \epsilon=\frac{\delta\log2}{4(K+2)(2A+4)}.                         \tag{9}
\]
Here is a direct fixed-\(\epsilon\) accounting. Suppose there is a violating sequence for this value, and extract the same minimal rational subspace and boundary limits. Each nonzero endpoint coordinate has \(|\log\prod_S|a_j|_v|\le\epsilon L\), since the positive or negative part of the sum over any places of \(\log|c_i|_v\) is at most \(h(c_i)\). Also \(\log\prod_S|B|_v\le K\epsilon L\). The total product contribution of at most \(2K\) endpoint coordinates plus the simultaneous clearing of at most \(2K+1\) linear forms is at most \(A\epsilon L\) on the log scale. The ordinary size of the cleared coordinates is at most \(e^{C_K L}\). Since \(A\epsilon<\delta\log2\), (6) still gives linear dependence by the exact integer-vector theorem.

For any fixed nonzero basis form \(F\) at a place \(v\in S\), the same maximal-coordinate replacement now gives
\[
 \limsup_{L\to\infty}L^{-1}
       \big(\max_{j:q_j\ne0}\log|b_j|_v-\log|F|_v\big)\le A\epsilon.
\]
Any fixed excess would leave exponential decay after paying for the entire coordinate product and denominator clearing. For a basis coordinate \(b_j\) represented in an endpoint \(a_i\), each of the three normalized logarithms \(L^{-1}\log|b_j/a_i|_v\) has limsup at most \(A\epsilon\). Their sum has absolute value at most \(2\epsilon\), which gives liminf at least \(-(2A+2)\epsilon\) at each place. The 2-adic valuations of the anchor coefficients themselves shift the comparison by at most \(2\epsilon\). Therefore the limit positions of \(a_i\) and each represented \(b_j\) differ by at most
\[
                              D=(2A+4)\epsilon/\log2.
\]
For a basis coordinate in \(x\), the place 3 yields \((r_j/L)\log3\le(A+1)\epsilon+o(1)\). Infinity then bounds its limit position by \(1-\delta+(2A+2)\epsilon/\log2\). For a basis coordinate of \(W\), place 2 bounds its limit position below by \(1-(A+1)\epsilon/\log2\).

The interval \((1-\delta+D,1-D)\) has length \(\delta-2D\). The closed \(D\)-neighborhoods of all boundary limits have combined length at most \(2(K+1)D\). Formula (9) gives \(2(K+2)D<\delta\), so choose \(\alpha\) outside all these neighborhoods. In the basis-position split below and above \(\alpha\), every original endpoint coordinate and every basis coordinate in its expression lie on the same side. The entire source is below, and the terminal form is above. The exact projection and physical return (8) follow verbatim. This proves (9).

## Prior work

PR210 uses the three-place Subspace Theorem for periodic approximants to a ternary backwards critical script. PR193 uses a minimal-subspace and small-coefficient valuation argument to exclude specified ternary shadows on a positive escaping ray. PR196 derives occupancy and edit constraints using repeated factors. De Jesús proves effective first-coefficient-crossing descent for words with at most 81 maximal odd runs; that result assumes the specified coefficient horizon and studies its descent. The present estimate concerns the size of *every* positive ordinary realizer, includes unrestricted endpoints, and treats arbitrary fixed numbers of consecutive small-anchor pieces. The subspace and valuation methods themselves are classical. [PR210](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/SUBSPACE.md) · [PR193](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/global/SPARSE_SHADOWS.md) · [PR196](https://github.com/GettysburgResearch/collatz/blob/27d03cfe902660e06604eb55bb28ca3d2754ff48/research/astra-orbit-cycle-20261124/occupation/CARRY_OCCUPATION.md) · [De Jesús, *Realizer Bounds and Repetition Constraints at the First Coefficient Crossing*, v4](https://hexagonmath.org/2611.00459v4)

Weaver's *Height and periodic-dictionary complexity for rational Collatz trajectories* is a close predecessor. Theorem 9 bounds the elapsed odd clock by an effective function of piece count times the logarithmic source height plus the adaptive dictionary's division budget. Corollary 7 and (C6) give related rational-cycle denominator estimates, and Proposition 8 derives a two-center reset identity. Its effective positive coefficient and its allowance for growing piece cost are advantages of that theorem. Here the number of pieces is fixed, the binary-clock source coefficient approaches one, the anchors can come from arbitrary pieces with small reduced rational height, and equality with an actual piece anchor gives the exact exception. [Weaver, v2, Theorem 9, Corollary 7 and Proposition 8](https://rstation.ai/problems/collatz/papers/15/v2)
