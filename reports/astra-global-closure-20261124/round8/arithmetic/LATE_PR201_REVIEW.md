# Exact-clock rows and fixed positive binary prefixes

I checked PR201 at commit 2978d84f8a1fda9083593b26c6bf724d5976d859 against the round-eight outside-prime theorem. The exact-clock reduction uses positive integer paths. If convergence fails, its two-gap construction gives at least \(2^{\lceil b/32\rceil}\) retained sources for one endpoint on every sufficiently large row with \(b\) odd steps and \(2b\) shortcut steps. The endpoint may vary with \(b\) on an escape. On a nontrivial cycle the construction can fix the endpoint. It gives this count separately in each prescribed unit source class modulo \(3^K\) in the stated range. The upper estimate under universal convergence uses convergence for the finitely many small states forced by the carry threshold. A cofinal upper estimate for the maximal count \(R_b(\epsilon)\) remains open. [Finite reduction](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/FINITE_CLOSURE.md) · [Proof of the row estimates](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

**Uniform bound on binary agreement.** Fix any positive ordinary anchor \(n\) and put \(M=9n+3\). An amplified source \(x\) from PR201's construction satisfies
\[
9(x-n)=2^t z-(M+2^f),\qquad 1\le f<t,
\]
where \(z\) is an ordinary unit and \(t\ge b/40\) eventually, uniformly over all tree branches and admissible source classes. Put \(a=v_2(M)\). For \(f\ne a\) we have \(v_2(M+2^f)=\min(a,f)\). For \(f=a\) we have \(M+2^f\le2M\). Hence as soon as \(t>\lfloor\log_2(2M)\rfloor\),
\[
v_2(x-n)=v_2(M+2^f)\le\lfloor\log_2(2M)\rfloor .
\]
This includes a varying first gap \(f\) and a varying endpoint. Thus the sources in this exponential lower-bound construction agree with \(n\) on only boundedly many initial shortcut parity bits. Indeed \(k\) common parity bits imply \(2^k\mid x-n\). The centers \(-(2^f+3)/9\) for individual first gaps and their limit \(-1/3\) as \(f\to\infty\) are all outside the positive ordinary integers.

The outside-prime theorem needs distinct witnesses in the expanding binary prefix of one fixed positive \(n\). Even when a cycle supplies a repeated terminal word, the initial two-gap sources obey the same bound. The fixed interior vertex \(q_0\) in the construction is followed by its own actual suffix, which gives zero lift displacement there. Other sources counted by \(R_b(\epsilon)\) need not arise from the displayed construction. The bound above therefore identifies a missing fixed-source condition and gives no estimate for the total row count. [Outside-prime theorem](../../../../research/astra-global-closure-20261124/round8/arithmetic/README.md)

I reran the pinned PR201 finite controls and reproduced SHA-256 b24581bff08881816697cf0fad6159052288a8e70ed28dc21e1300232606e517, including 40,336 replayed row/class/source triples. I also checked the displayed valuation identity on 1,080 combinations of legal padded sources and fixed positive anchors. Fourteen attained the displayed upper bound. The two reviewed upstream Markdown Git blobs are 48c5f31da4f297ec9eeb134a88f7657c0dd98d03 and 614eb6a2b70aad949fa851b564462dff78eafbcb, in link order.
