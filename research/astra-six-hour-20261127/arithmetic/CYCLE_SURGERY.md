# Complete denominator after replacing one interval of a cycle

Let \(w=uv\) be the binary shortcut word of a positive integer cycle rooted at its actual state \(x\). Write \((A,a,c)\) for the affine data of \(u\), so its action is \((a x+c)/A\), with \(A=2^{|u|}\) and \(a=3^{\#1(u)}\). Write \((B,b,d)\) for the common suffix \(v\) and \((A',a',c')\) for an arbitrary replacement \(u'\). The gap sizes and the position of the edit are unrestricted. Suppose \(u'v\) has positive length and a nonzero determinant \(D'=A'B-a'b\) coprime to six. This includes every word with at least one odd departure.

The complete reduced denominator of its rational periodic state \(x'\) is exactly
\[
 q'=\frac{|D'|}{\gcd(|D'|,K)},\qquad
 K=(A'a-Aa')x+A'c-Ac'.
\]
Indeed \((AB-ab)x=bc+Ad\) and \(D'x'=bc'+A'd\). Elimination gives \(AD'(x-x')=bK\). Since \(A,b\) are units modulo \(D'\), every integer multiple clearing \(x'\) is precisely a multiple clearing \(K/D'\). The old outside-prime denominator is one at this actual cut. No independence of primes is used. Changing an initial odd departure into an even departure at the same clock gives \(q'=|D'|/\gcd(|D'|,2x+1)\).

If \(K=0\), then \(x'=x\). The edited word starts at the same ordinary point, has the parities of its deterministic orbit, and represents that orbit for an integer number of periods. Otherwise \(\gcd(|D'|,K)\le |K|\).

For a quantitative reading, let \(h\) be the original least shortcut period, and let \(|u|+|u'|=o(h)\). The affine carry of a word of length \(\ell\) has magnitude at most \(O(6^\ell)\), so \(\log_2 |K|\le\log_2(x+1)+o(h)\). Standard two-logarithm separation gives \(\log_2|D'|\ge h-o(h)\) for the edited grades, including the negative-determinant case. The same separation and the minimum cap \(3C\le p2^h\) give a polynomial original minimum \(m=h^{O(1)}\), where \(p\) is the original odd count. To bound any cut, the original laps have \(p<h\log_3 2\). Along any proper arc from \(m\), the only increasing steps are odd, their homogeneous factors are \(3/2\), and the product of their corrections is bounded by the full-lap product. That product is at most \(\exp(\sum_{i=1}^p 1/(3x_i))\le \exp(O(\log h))\), using distinct positive integer odd states. Consequently \(x\le 2^{(1-\log_3 2)h+O(\log h)}\).

Every nontrivial such replacement therefore has
\[
 \log_2 q'\ \ge\ (\log_3 2-o(1))h.
\]
At a cut of polynomial height, in particular at the original minimum, the stronger conclusion is \(\log_2 q'\ge(1-o(1))h\). The estimate applies to each edit of each hypothetical primitive integer cycle in a sequence with \(h\to\infty\). It excludes finding a second integer cycle by a sublinear contiguous replacement, while leaving the original integer cycle possible. [Minimum cap](COMPLETE_DIVISORS.md) · [Two-logarithm input, Simons and de Weger, Lemma 12](https://doi.org/10.4064/aa117-1-3) · [Lean kernel checking the common-suffix identity and simultaneous divisibility](CycleSurgery.lean)
