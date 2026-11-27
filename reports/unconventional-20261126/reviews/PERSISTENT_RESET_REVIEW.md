# Independent review of a common divisor across several resets

**Narrow verdict.** VERIFIED WRITTEN for Theorem D and its CRT construction at `PERSISTENT_RESET_DIVISOR.md` SHA-256 `c2cad78a83aa8825f555272b7647e113e5324b147f29e9f8951e1026419ec72e`, using Evertse's published Theorem 2. Its constant may be ineffective. The examples have one actual positive ordinary initial integer per finite word. They do not prescribe an infinite exceptional orbit.

I inspected the scanned definitions on printed page 226 and Theorem 2, (13)–(14), on printed page 228 of Evertse (1984). Over the rational field, the height there is the archimedean coordinate maximum. His vector need only be integral. The hypothesis is nonvanishing of every nonempty coordinate subsum. With the three places selected in D and its singleton dyadic subset, (14) is exactly D's (4), including its *maximum* dyadic coordinate factor on the right. [Evertse, *Compositio Mathematica* 53, 225–244](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

Writing \(D_j=\sum_{i<j}(t_i+b_i)\), the block equation is \(2^{t_j+b_j}Y_{j+1}=3^{t_j}Y_j+2^{t_j}(2^{b_j}-1)\). Its unrolling multiplies the correction at block \(j\) by \(2^{D_j}3^{\sum_{i>j}t_i}\). Since the odd common divisor \(g\) divides \(2^{b_j}-1\) at *every* block, division by \(g2^{t_0}\) produces exactly \(r+1\) positive nonzero integer coordinates. In particular none of their nonempty subsums vanishes. The initial coordinate is odd even after that division. The other coordinates can have arbitrary common factors with it without invalidating Evertse. The total sum has exact dyadic valuation \(T+B-t_0+t_r\). Each coordinate's three-place product is at most the indicated base with its powers of 2 and 3 stripped off. The resulting \(g^{-(r+1)}\) comes from one division in every coordinate. The factor \(2^B\) in that estimate cancels the same factor from the dyadic norm of the sum. Each coordinate is bounded by the positive sum, whose logarithm is \(O_r(\log Y)\) via the physical block height estimate. This proves D(1). Discarding all but any fixed initial window before passing to the limit is legitimate for the growing-length consequence.

For the lower construction I checked the input-bit convention: \(O^{t_j}E^{b}\) gives precisely \(t_j-1\) exponent-one odd gaps and a final valuation \(b+1\); the next odd input certifies the exact halving count. CRT simultaneously enforces that complete dyadic cylinder, \(x_0+1=0\bmod 2^b-1\), and \(x_0=0\bmod3\) for odd \(b\). The common divisor propagates and cannot be larger than \(2^b-1\) by the first block. In particular this is an exact gcd construction, not just a divisibility witness. The interval for the CRT representative yields \(\log_2Y=T+(r+1)b+O(1)\), and the bounded positive correction factors give \(\log_2x_r=\alpha T+b+O_r(1)\). This verifies both branches of the optimized exponent, the equality threshold, and the stronger floor through the whole observed \(\sigma=1\) construction when each homogeneous gain exceeds 1 by a fixed factor. Nothing requires a finite exceptional-line analysis in this variant of Evertse's theorem.

## A conditional implication for all phases of one ordinary cycle

Let an ordinary positive cycle be cut at its \(R\) reset-block entrances. Write \(Y_i=x_i+1=2^{t_i}w_i\), \(g_i=\gcd(w_i,w_{i+1})\), \(p=\sum_i t_i\) for the odd period, and define
\[
 P=p\log 2,\qquad S=\sum_i\log Y_i,\qquad
 L=\sum_i\log g_i .
\]
Set \(m\) equal to the minimum odd state on that cycle. For any hypothetical sequence of such cycles with \(m\to\infty\),
\[
     P/S\longrightarrow0,\qquad
     \frac1S\sum_i\log\gcd(Y_i,Y_{i+1})\longrightarrow0.       \tag{A}
\]
No lower bound on the number of resets per period is assumed.

For each fixed \(r\) apply D(1) to all cyclic windows of \(r\) complete blocks, allowing the windows to wrap and repeat. Drop the positive integer common divisor from the bound. The sum of all \(T+t_r\) equals \((r+1)p\) by exact counting, even when \(R<r\). Hence
\[
 (r+1)P\le (1+\epsilon)S+R\log C_{r,\epsilon}.
\]
Since \(R/S\le1/\log(m+1)\), first send the minimum to infinity at a fixed \(r\), then send \(r\to\infty\), to obtain the first limit. Also \(g_i<2^{b_i}\), with \(\sum b_i=A-p\). The cycle product gives \((A-p)\log2=(\log_2 3-1)P+\sum_{j<p}\log(1+1/(3x_j))\), and the last sum is at most \(p/(3m)\). Thus \(L=O(P)\), and the dyadic contribution to the sum of the neighboring full-gcd logarithms is at most \(P\), proving (A).

This consequence also follows independently from the earlier fixed-fragment duration bound. The block window uses at most \(2r+1\) alternating constant-bit shortcut fragments, including the terminal run of \(t_r\) odd inputs. Their centers are 0 and \(-1\), so the positive states satisfy all guards. That source bounds even \(T+B+t_r\) in terms of \(\log_2 x_i\), which gives the first limit by the same cyclic sum. Thus (A) is an application, not a novelty claim for a new duration estimate. A positive cycle can in principle keep replacing its odd factors at each reset; (A) provides no contrary lower bound. [Paper 147 v1, Proposition 1, equation (21)](https://rstation.ai/problems/collatz/papers/147/v1)
