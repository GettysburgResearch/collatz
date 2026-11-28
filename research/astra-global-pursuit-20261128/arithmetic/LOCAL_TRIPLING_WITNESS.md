# Extracting an odd tripling witness from one adjacent color change

Let \(f:\mathbb N_{>0}\to\{0,1\}\) be constant on the edges of the positive shortcut Collatz map \(T\). Put \(D=\{n:f(n)\ne f(n+1)\}\) and \(P=\{3q:q>0\text{ odd},\ f(3q)\ne f(q)\}\). For odd \(q\), \(f(3q+1)=f(q)\), so \(P\) is precisely the set of odd multiples of three in \(D\).

**Earlier, stronger global results.** Lean Assurance Lab already proves directed tripling failure counts exceeding \(X/(\log X)^B\) along a subsequence for every nonconstant invariant coloring, even in a fixed class of cofactors \(q\equiv1\bmod2^K3^L\). Its paper deduces decidable subpolynomial sufficient sets. The same author gives routes from 1 to each \(n\) with odd directed charges \(q\to3q\), all \(9q\le8n+1\), and height at most \(6n+2\). In particular exact tripling sufficiency and full upper counting exponent for the 3-free parts of failures are already known. The elementary argument below supplies a pointwise witness from the two specified unequal endpoints, with an explicit bounded list of local addresses and recoverable anchors. Its unrestricted witnesses can have either orientation. It does not prove any required implication \(R(q)\Rightarrow R(3q)\). [Paper 227, directed cut supply](https://rstation.ai/problems/collatz/papers/227) · [Paper 228, §2](https://rstation.ai/problems/collatz/papers/228) · [Paper 232, sufficient charge heights and sparsity](https://rstation.ai/problems/collatz/papers/232).

## A local decoder

Given any \(n\in D\), there is \(P_0\in P\) with
\[
        P_0\le 2^{13}(n+1)(4/3)^{v_3(n)}.
\]
Only the first eleven child choices of this one dyadic boundary are needed. Apart from the child endpoint itself, the candidates come from removing the 2- and 3-parts of one of its bounded-depth endpoints and applying the explicit formulas below.

If \(m\in D\), exactly one of \(2m,2m+1\) is in \(D\): the exterior colors are those of \(m,m+1\) and the middle color is binary. Choose that child and write its last bit. No three subsequent bits form \(100\). Indeed \(8b+4\) and \(8b+5\) both reach \(3b+2\) in three ticks. This forbidden binary word and the persistent child construction also appear in [PR221, pinned dyadic boundary addresses](https://github.com/GettysburgResearch/collatz/blob/f8602319553c29b7ed11d180369f7ef381fb0c5e/research/astra-nine-hour-resolution-20261128/wild/DYADIC_BOUNDARY_ADDRESSES.md).

For \(s=2^h3^v a\), \((a,6)=1\), write \(g_s(i)=f(2^i s+1)\), \(l_s(i)=f(2^i s-1)\) whenever the input is positive. For \(i\ge1\) the actual shortcut steps give
\[
       g_s(i)=g_a(i+h+2v),\qquad l_s(i)=l_a(i+h+v).
\]
For the first use \(4u+1\to6u+2\to3u+1\); for the second use \(2u-1\to3u-1\). The plus identity also holds at \(i=0\). If \(f(s)\ne f(a)\), one of the odd sites \(a3^b\), \(0\le b<v\), witnesses a tripling failure; then take \(P_0=3^{b+1}a\le s\).

**Six left children.** Suppose the first six choices are zero. Then \(g_n(i)\ne f(n)\) for \(0\le i\le6\). Decompose \(n=2^h3^v a\), and use the preceding chain if \(f(n)\ne f(a)\). Otherwise choose \(0\le i\le5\) with \(2^k a\equiv1\bmod9\), \(k=i+h+2v+2\); the order of 2 modulo 9 is six. Put
\[
           p=(2^k a-1)/3.
\]
This is an odd multiple of three. It takes one odd step to \(2^{k-1}a\), while \(p+1=(2^k a+2)/3\) takes an even and an odd step to \(2^{k-2}a+1\). Thus \(f(p)=f(a)=f(n)\) and \(f(p+1)=g_n(i)\ne f(n)\). Take \(P_0=p<2^7 n(4/3)^v/3\). This is the exact lower and upper pixel computation at the rational point \(a/3\).

**Two consecutive right children.** If these start from \(m\), put \(s=m+1=2^h3^v a\). Both \(l_s(1)\) and \(l_s(2)\) differ from \(f(s)\). Use the chain if \(f(s)\ne f(a)\). Otherwise choose \(i\in\{1,2\}\) with \(2^{i+h+v}a\equiv1\bmod3\), and put
\[
          p=2^{i+h+v}a-1 .
\]
It is an odd multiple of three. Its color is \(l_s(i)\) and the color at \(p+1\) is \(f(a)=f(s)\). Take \(P_0=p<4s\).

**The remaining addresses.** If the first six digits are not all zero, let the first one occur at position \(t\le6\). If its index is an odd multiple of three, use that index immediately. Otherwise consider the next four digits. Unless there is a double one, they must alternate as \(0101\): a double zero after the first one would contain a first occurrence preceded by a one. At the endpoints after the first one and after each subsequent \(01\), the index is odd; appending \(01\) replaces its residue modulo three by its successor. One of those three indices therefore belongs to \(P\). This visits at most ten children, with indices \(<2^{10}(n+1)\). The height bound follows in all cases.

## Fibers of the witness prescription

For a fixed \(P_0\), the number of possible roots \(n\le X\) assigned this witness is \(O((1+\log X)^2)\), uniformly in the witness. For a bounded-depth child, \(n\) is one of at most eleven dyadic ancestors. In the other cases the value \(s\) used in the computation is \(n\) itself or \(1+m\) for an index at bounded depth. Each given \(s\) has a bounded number of possible roots. In the chain case its 6-free part \(a\) is the 6-free part of \(P_0\). In the two pixel cases it is respectively the odd part of \(3P_0+1\) or of \(P_0+1\). Once \(a\) is fixed, \(s=2^h3^va\ll X+1\) has \(O((1+\log X)^2)\) possibilities.

For example, let \(C(Y)\) count distinct 3-free parts of \(P_0\in P\) through \(Y\), and \(0<\epsilon<1\). Discard roots \(n\le X\) divisible by \(3^{\lceil\epsilon\log_3 X\rceil}\), costing \(O(X^{1-\epsilon})\). All other witnesses are \(\ll X^{1+\epsilon\log_3(4/3)}\); each 3-free part labels \(O(\log X)\) possible witnesses at that height. Hence
\[
 |D\cap[1,X]|\ll X^{1-\epsilon}
    +(1+\log X)^3 C\!\left(2^{15}X^{1+\epsilon\log_3(4/3)}\right).
\]
The elementary empty-witness case gives constant color. If \(C(Y)=O(Y^{1-\eta})\) for any fixed \(\eta>0\), choosing \(\epsilon\) sufficiently small gives a power saving for \(D\), hence \(\sum_{n\in D}1/n<\infty\). The published summable-boundary theorem and positive predecessor mass then force constant color. This independently recovers a consequence of Paper 227 under a different proof and loses its directed, near-linear frequency conclusion. [Paper 212, sibling zero-one theorem](https://rstation.ai/problems/collatz/papers/212) · [Positive predecessor density](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

## Lower pixels at higher ternary denominators

For \((a,3)=1\) consider \(\lfloor2^k a/3^d\rfloor\), and let \(r=2^ka\bmod3^d\) in \([1,3^d)\). Its offset from the exact center is the rational \(z=-r/3^d\) in \((-1,0)\). A legal shortcut on odd-denominator rationals uses the parity of their numerator. After exactly \(d\) odd departures the offset first becomes integral. It equals zero there in precisely the two phases
\[
                   r=3^d-2^d,\qquad r=3^d-2^{d-1}.
\]
Indeed a negative orbit which later reaches zero stays in \((-1,0)\) and is increasing there. Immediately before zero it equals \(-1/3\). Any even tick followed by one odd tick puts an input \(>-1\) above \(-1/4\), too high to reach \(-1/3\) later. Thus the first \(d-1\) departures must be odd, then at most one even tick before the last odd one. Inverting these two words gives the displayed phases. Conversely each word has the required parities. For \(k\) at least the word length, its lift transports the ordinary pixel to \(2^{k-t}a\) in the actual time \(t\), proving equality of its color with \(f(a)\). Additional phases can still have the same color through other ordinary paths. The two-phase claim deals only with zero offset at first integral entrance.
