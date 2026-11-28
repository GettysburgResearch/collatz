# Entropy of the selected positive-source suffix

Let \(N=2^k\), \(M=\lfloor k/(1-\tfrac12\log_2 3)\rfloor\),
\(W=\sqrt{k\log(k+2)}\), and \(g\sim k^{3/5}\). For uniform positive
\(n\le N\), let \(U\) be its length-\(g\) parity word starting at date \(M\).
For each fixed \(A>2\), a set of at most \(\exp(O_A(W))\) words carries
probability \(1-O_A(k^{-A})\).

Indeed, outside the stated exception the actual source reaches
\(x\le k^{O_A(1)}\) at a date \(u=M+O_A(W)\). Each positive shortcut
step changes the size by a factor in \([1/2,2]\), so
\(T^M n\le 2^{|u-M|}x\le\exp(O_A(W))\) on either side of the crossing.
The integer \(T^M n\) determines the entire suffix. [Weaver 191/v2, Theorem 1 and Section 4](https://rstation.ai/problems/collatz/papers/191/v2)

For the fair word conditioned on the full-conductor stationary selection
\(E_{M+g,N}\), the same word set has exception probability
\(p=O_A(k^{-A}+\log N/N)\). This uses the total-variation comparison for
the whole source window, applied to the indicator of the word set.
The entropy decomposition over membership in this set yields, in nats,
\[
 H(U\mid E_{M+g,N})\le h_2(p)+O_A(W)+p\,g\log2=O_A(W)=o(g),
\]
where \(h_2\) is binary entropy in nats and conditioning denotes occurrence
of the event. The unconditioned fair suffix has entropy \(g\log2\).
The signed mean can still vanish on a distribution of zero entropy rate,
as the alternating positive cycle illustrates. The sign remains open.
[Exact source selection and uniform error](../ACTUAL_SOURCE_STATIONARY_TRACE.md)
