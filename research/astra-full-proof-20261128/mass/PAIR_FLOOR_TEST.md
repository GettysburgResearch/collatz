# Actual positive controls for a two-cone coupling

The following obstruction applies to asynchronous as well as synchronous visits. On the positive shortcut map \(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\), call two target sets incomparable if no forward ray visits a member of both sets. Such sets can lie in the *same* component.

Let \(\epsilon_t\to0\) be the fraction of residue classes modulo \(2^t\) for which the affine paths of \(r,r+1\) have not met synchronously by time \(t\) with equal odd counts at that date. Use the sufficient classes in Duran's coalescence theorem, as stated in [Weaver 12, Input A](https://rstation.ai/problems/collatz/papers/12/v1). The external formal work was not rebuilt. For integer \(d\ge1\), integers \(X,H,t\ge1\) with \(H<X2^{-t}\), and comparable source windows \([X,2X)\), the following written consequence is uniform in the two *sets* of labels. If \(A,B\subseteq[1,H]\) are incomparable, then
\[
 \frac1X\#\{X\le n<2X:\ n\hbox{ visits }A,\ n+d\hbox{ visits }B\}
 \le d\bigl(\epsilon_t+O(2^t/X)\bigr).
\]
Indeed, outside the union of the \(d\) exceptional adjacent-pair events, all \(d+1\) paths already agree at time \(t\). Every shortcut state during that initial window is at least \(X2^{-t}\), so both visits would have to occur on one common later ray. The error term is ordinary incomplete-period counting. In particular, for any *fixed* gap \(d\) and any \(H(X)=o(X)\) the proportion tends to zero, even for incomparable target sets chosen anew at every \(X\). For targets belonging to disjoint whole components no truncation by \(H\) is needed.

Take \(A=\{5\}\) and \(B=\{85\}\). Both are positive odd units whose next Syracuse state is 1; neither visits the other. Each has a positive-density predecessor set by the external [fixed-target theorem](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html). Yet the asymptotic joint density of the two predecessor events above is zero for *every* fixed source gap. If adjacent targets are preferred, 16 and 17 merge into 8 without either visiting the other. This rejects a uniform fixed-root pair floor based on unit status, large separate predecessor sets, or local inverse-word richness alone.

The exact paired inverse edge
\[
 (4u+1,\,4u+2)\ \xrightarrow{T^2}\ (3u+1,\,3u+2)
\]
shows why a single arithmetic family is insufficient. Its one-parameter domain does not give positive-density paired preimages of a specified target. The pair \((1,2)\) also alternates forever without synchronous merger despite both coordinates reaching 1, so synchronous disagreement itself cannot label different components. A full coupling would need a lower bound that uses the *permanent* separation of the two forward components, beyond the fixed-target hypotheses disproved here.
