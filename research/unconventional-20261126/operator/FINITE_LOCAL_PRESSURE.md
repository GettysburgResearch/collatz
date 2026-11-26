# Exact finite-alphabet pressure for ternary gates and weights

**Proposed corollary O17, conditional on O15's stationary entropy dichotomy.** Let \(D\) be a nonempty finite set of positive exponents. Give each edge \(x\mapsto I_e(x)=(2^ex-1)/3\), defined when \(2^ex=1\bmod3\), a weight \(w(x,e)\ge0\) depending only on \(x\bmod3^M\) and \(e\in D\), for fixed \(M\ge1\). On \(C(\mathbb Z_3)\), define the positive weighted sum \(K_w f(x)=\sum_{e\text{ legal}}w(x,e)f(I_e x)\). Its spectral radius is exactly the maximum of two finite quantities: one third of a matrix Perron root, and the maximum geometric mean of the edge weights on a directed cycle in the same finite graph.

## The finite graph

A label block \(d=(e_0,\ldots,e_{M-1})\) determines the residue
\[
 x_d=G_{e_0}\cdots G_{e_{M-1}}(0)\pmod{3^M},
 \qquad G_e(y)=(3y+1)/2^e .
\]
Make \(d\) the directed edge from its first \(M-1\) letters to its last \(M-1\) letters. Its weight is \(w_d=w(x_d,e_0)\). When \(M=1\) the graph has one empty vertex and individually distinguished parallel edges. Let \(D_w\) be the adjacency matrix obtained by summing weights of parallel edges, and \(\gamma_w\) the largest directed cycle geometric mean, or zero if all cycles contain a zero edge. Then
\[
                          r(K_w)=\max\bigl(r(D_w)/3,\gamma_w\bigr).
\]

## Proof for positive weights

For each maximizing \(n\)-row of \(K_w^n\), use its path Gibbs law with weights \(\prod w(X_j,E_j)\). As in O15 Section 2, compactness and lower semicontinuity of relative entropy give an invariant edge flow with
\[
       \log r(K_w)\le\beta+\mathbb E\log w(X_0,E_0).
\]
For the finite alphabet compare the empirical joint law to its state marginal times the uniform label law. The entropy component is upper semicontinuous, and the log weight integral converges because the weight on the clopen legal set is positive and locally constant. One may pass to ergodic components of the stationary Markov inverse policy as in O15.

At every point of a stationary path \(X_j\bmod3^M\) is determined by \(E_j,\ldots,E_{j+M-1}\). Thus its log weight is the log weight of the corresponding finite graph edge. If \(\beta=0\), its reward is at most \(\log\gamma_w\): any stationary flow on a finite directed graph is a convex combination of cycle flows. If \(\beta>0\), O15 gives \(h_E=\beta+\log3\). The finite graph bound
\[
                h_E+\mathbb E\log w_d\le \log r(D_w)
\]
follows by applying the finite Gibbs inequality to blocks of \(n+M-1\) letters with weight their product of \(n\) edge weights, and then dividing by \(n\). The total graph weight of such blocks is \({\bf1}^{t}D_w^n{\bf1}\). This establishes the upper estimate.

A finite directed cycle gives a periodic label sequence, hence its own fixed ternary path by contraction. One summand in every repeated cycle is exactly its weight product, giving \(r(K_w)\ge\gamma_w\).

For the volume bound, integrate \(K_w^n1\) against ternary Haar. For any fixed \(n\)-word the start state is \(G_{e_0}\cdots G_{e_{n-1}}(y)\) with \(y\) Haar. This starts in an \(n\)-cylinder of Haar volume \(3^{-n}\). For the first \(n-M+1\) positions the log weights are determined by the fixed word. An explicit bound also works for vanishing weights: append any \(M-1\) symbols to the fixed word, then restrict \(y\) to the corresponding \((M-1)\)-cylinder of Haar volume \(3^{-(M-1)}\). On that entire cylinder all \(n\) weights equal the desired graph weights. Distinct appended words may give overlapping cylinders, but there are at most \(|D|^{M-1}\) appended words for each fixed prefix. Therefore
\[
 \int K_w^n1\,dm\ \ge\
    3^{-n}\,(3|D|)^{-(M-1)}
    {\bf1}^{t}D_w^n{\bf1}.
\]
Taking \(n\)-th roots yields \(r(K_w)\ge r(D_w)/3\). For nonnegative weights use monotonicity \(K_w\le K_{w+\epsilon}\). The finite matrix spectral radius and the maximum over simple finite cycle means are continuous in these weights. Letting \(\epsilon\downarrow0\) gives the same upper bound, and both lower arguments remain valid. This proves the formula.

The graph encodes the pressure of an all-time repeated local rule in the 3-adic inverse system. A positive cycle of the graph in this proof supplies a rational ternary periodic path. Such a path need not be a positive ordinary Collatz cycle.
