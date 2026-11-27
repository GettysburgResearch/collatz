# A smaller bad multiple at the second odd-run exit

Let \(T(n)=n/2\) for even \(n\) and \(T(n)=(3n+1)/2\) for odd \(n\). Take the least odd tripling disagreement \(q\) for the actual basin of 1. Its upper member \(n=3q\) is bad and every smaller positive multiple of three is good. [Minimum theorem](../minimal/MinimumFailure.lean)

**Second-run exclusion.** Write \(n+1=2^m a\) with \(a\) odd. Suppose \(1\le m\le3\) and \(r=3^m a\equiv3\pmod4\). After the first odd run and one halving, the bad orbit stands at \(y=(r-1)/2\). Write \(y+1=2^\ell b\) with \(b\) odd. Then a least disagreement must satisfy \(3^\ell b\equiv3\pmod4\). The second run length \(\ell\) can be arbitrarily large across the excluded family. There is no requirement on the power of three in \(n\).

**Proof.** Set \(U=(3^{m-1}a-1)/4\), an integer because \(r\equiv3\pmod4\). It is positive, since equality to zero would force \(m=a=1\) and \(n=1\). The inequality \(U<q\) is equivalent to \((4\cdot2^m-3^m)a>1\). The coefficient takes the values 5, 7 and 5 for \(m=1,2,3\). Thus \(3U\) is a positive multiple of three strictly below \(3q\).

The first orbit gives \(T^m(n)=r-1=12U+2\) and hence \(y=T^{m+1}(n)=6U+1\). Therefore \(3U=(y-1)/2=2^{\ell-1}b-1\). Suppose \(3^\ell b\equiv1\pmod4\). Put \(Y=3^{\ell-1}b\), so \(Y\equiv3\pmod4\). The orbits of \(y\) and \(3U\) reach \(3Y-1\) and \(Y-1\) after \(\ell\) and \(\ell-1\) steps respectively. Two further steps on each arm reach \((3Y-1)/4\). In particular,
\[
   T^{m+\ell+3}(3q)=T^{\ell+1}(3U)=(3^\ell b-1)/4.
\]
This would make the bad upper member converge. [Lean proof](SecondRun.lean)

For example, \(q=1485\) gives \(n=4455=8\cdot557-1\), \(y=7519\), \(\ell=5\) and \(3U=3759\). The two triples reach 14276 in 11 and 6 steps. The smaller triple can exceed the general good interval through \((9q-1)/8\).

**An independent family inside the surviving first exit.** Fix \(m=3\) and prescribe any \(h\ge3\) and \(\ell\ge7\). Choose positive \(a\) by the Chinese remainder theorem with
\[
  27a\equiv2^{\ell+1}(-1)^\ell-1\pmod{2^{\ell+3}},
  \qquad 8a\equiv1+3^h\pmod{3^{h+1}}.
\]
There are infinitely many choices for each pair. For \(n=8a-1\) these force \(v_3(n)=h\), \(v_2(n+1)=3\), and \(27a\equiv3\pmod4\). Since \(y+1=(27a+1)/2\), the second run has exactly the specified length and \(b\equiv(-1)^\ell\pmod4\). The exclusion applies. Meanwhile \(3a\equiv-1/9\equiv199\pmod{256}\), outside the earlier complementary class 147. Also \(q\equiv5\pmod8\) and \(9\mid q\), outside the four fixed source rows in the main packet. The CRT existence argument is a written proof. [Finite ordinary replay](check.py)

The second exit with \(3^\ell b\equiv3\pmod4\) remains open. For \(m\ge4\), the size comparison \(U<q\) in this proof fails.
