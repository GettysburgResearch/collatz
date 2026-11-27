# Strict ordinary counting for a primitive finite parity language

Let \(G\) be a finite directed graph whose edges carry labels 0 and 1. Assume that the vertex adjacency matrix is primitive, that every vertex has at most one outgoing edge of each label, and that some vertex has both labels available. Assume there are constants \(z>1,\lambda>0\), a positive function \(f\) on vertices, and a Markov chain on its edges with transition probabilities
\[
          K(v\xrightarrow{b}v')=\lambda^{-1}z^b f(v')/f(v).
\]
Only actual edges occur, and all have positive probability. The stationary mean of the emitted label is assumed to equal \(p_*=\log_3 2\). Write \(\alpha=\log_2 3\), \(h=\log_2\lambda-p_*\log_2 z\), and assume \(0<h<1\).

**Theorem.** Let \(V\) be any subset of positive ordinary shortcut states with the following properties.

1. \(T(V)\subseteq V\).
2. Every finite parity prefix from \(x\in V\) labels a path in \(G\).
3. The maps \(x\mapsto T^t x\) restricted to \(V\) have multiplicity uniformly bounded in \(t\).

Then there is \(\gamma>0\) such that, uniformly for all real intervals of width \(X\ge2\),
\[
                   \#(V\cap I)=O_{G,V}(X^{h-\gamma}).                 \tag{1}
\]
In particular this holds for the union of the states of **all** positive ordinary cycles accepted by the graph (i.e. admitting their periodic symbolic itinerary at every cyclic start). The fixed-time maps are permutations on that union. Bounded multiplicity is an ordinary-dynamics assumption: the theorem does not assign it to general one-sided survivors. The exponent \(h\) is the stationary entropy per physical shortcut bit, by telescoping \(-\log_2 K\) on the stationary chain. Only the all-state counting conclusion (1) and the more general symbolic concentration estimate below are claimed.

## Mixing of critical parity paths

Fix an initial vertex and draw the first \(t\) labels from \(K\). Write \(u=\sum b_i\), \(C=\sum_{i:b_i=1}2^i3^{u-1-U_i}\), \(U_i=\sum_{j<i}b_j\), and \(R=[-3^{-u}C]_{2^t}/2^t\). Uniformly over possible initial vertices, for each \(0<d<1\) there exists \(c_2>0\) such that for every fixed \(0<c_1<c_2\), and every \(c_1t\le P\le c_2t\),
\[
                   \sup_{|I|=2^{-P}}\Pr(R\in I)\ll 2^{-dP}.            \tag{2}
\]
Integer \(P\) suffices. This is a shallow-precision estimate. The onset remains ineffective because of the fixed-place Subspace Theorem. The full-entropy signed convolution and genuine canonical source separation are the mechanisms in Weaver 73, developed there for the critical geometric gap law. For dimer and two-gap fixed-type specializations with concrete constants, see the [preceding phase](../phase6/README.md). [Weaver 73, §§2–4](https://rstation.ai/problems/collatz/papers/73)

**Signed moments before conditioning.** Fix \(0<d_2<1\). For a segment of length \(l\), keep a fixed auxiliary scalar \(v\) in every coefficient \(3^{v-1-U_i}\), using its modular value even at a negative exponent. There are an even \(Q\) and a constant \(C_2\), independent of \(v,l\) and all starting vertices, such that every atom of any signed sum of \(Q\) independent auxiliary numerators modulo \(2^l\) has probability at most \(C_2 2^{-d_2 l}\). To verify this, a copy is called active at a vertex with two outgoing labels. Primitivity gives \(b_0,c>0\) with active probability at least \(c\) after any \(s\ge b_0\) steps from any vertex. At active vertices both probabilities are at least a fixed \(\epsilon>0\). Given the full past at a site, the next sum bit is the XOR of the independent fresh active bits up to a determined complement; the coefficient of the present bit is odd, including for negative exponents. Given only the full preblock history, the chance that fewer than \(cQ/2\) copies are active at *some* site after the first \(b_0\) positions in an \(L\)-block is at most \(L e^{-cQ/8}\). On sufficiently active sites the conditional maximum bit probability is \(\kappa_Q=(1+(1-2\epsilon)^{cQ/2})/2\). Successive conditioning for prescribed bits while the activity threshold holds at each site gives at most \(\kappa_Q^{L-b_0}\). First choose \(L\) large relative to \(b_0,1/(1-d_2)\), then choose \(Q\) large to make the sum of the two bounds at most \(2^{-d_2 L}\). Iterating blocks proves the claim. [Details of the bit argument](../phase6/MARKOV_MOMENTS.md)

**Critical prefix deviations.** Uniformly from every initial vertex, the probability that an \(l\)-step chunk has \(\max_{i\le l}|U_i-p_* i|>\omega P\) is at most \(e^{-cP}\) when \(l\asymp P\) and \(\omega>0\) is fixed. Indeed solve the finite chain Poisson equation \((I-K)g(v)=\mathbb E(b\mid v)-p_*\), where \(K\) on vertex functions sums edge probabilities. Solvability follows from zero stationary mean and simplicity of the stationary eigenspace. The increments \(b-p_*+g(v')-g(v)\) are centered and bounded. The elementary martingale bounded-differences estimate followed by a union bound over the possible prefix ends proves the claim; the endpoint coboundary is bounded. The same argument gives \(\Pr(U_{\lfloor t/4\rfloor}<p_*t/8)\le e^{-c_0t}\) for a fixed \(c_0>0\) and all sufficiently large \(t\).

**Markov bridges and ordinary numerator sizes.** Fix \(d<d_1<d_2<1\). Take \(\eta>0\) small enough that \(d_2(1-5\eta)>d_1\). Each selected chunk has deterministic physical length \(l=\lfloor(1-4\eta)P\rfloor\). For a good chunk require the prefix deviation just described with \(\omega\) fixed sufficiently small. Its own affine numerator \(B\) is \(\le2^{(1-\eta)P}\) for large \(P\). In fact the binary logarithm of each term of \(B\) is at most \(l+2\alpha\omega P+O(1)\), since its terminal-segment slope excess is bounded by two prefix deviations, and at most \(l\) terms occur.

A local type records the chunk's last vertex and its own odd count \(v\) with the starting vertex specified. Discard as bad every realization of a type having probability below \(e^{-\delta P}\) from this starting vertex. There are at most \((l+1)|G|\) types, so conditional on any history up to the start, the total chance of discarded type or failed prefix constraint is \(\le e^{-c_3P}\) for a fixed \(c_3>0\) and large \(P\). Choose \(\delta>0\) after \(Q\) is fixed, so that \(Q\delta/\log 2<d_2(1-5\eta)-d_1\).

Place \(N\) consecutive disjoint selected chunks in the middle half of the path, where \(N\ge Q\) is fixed and \(c_3(N-Q+1)>2\log 2\). This is possible for sufficiently small \(c_2\). Discard the event of the early \(t/4\)-guard having fewer than \(p_*t/8\) odds, whose probability is \(\le e^{-c_0t}\le 2^{-2P}\) on further decreasing \(c_2\). On the complement, for every selected chunk its ambient exponents \(m=t-L_0, a=U_0+v\) satisfy \(2^m,3^a\ge2^P\). Here \(L_0,U_0\) are preceding physical length and odd count. Condition on the exterior paths, all boundary vertices and all local counts. The conditional law of the interiors is a product of local Markov bridges of the specified types. This follows by factoring the edge likelihood and summing over the separate compatible interiors. Exteriors with impossible types have zero probability.

In this environment a chunk's real-circle contribution to \(R\) is \([-3^{-a}B]_{2^m}/2^m\). Quantize it by the floor of its \(2^P\) multiple modulo \(2^P\). A signed \(Q\)-energy collision of good copies of that chunk gives
\[
       D=2^m A-3^a Z,\qquad |Z|\le Q2^{m-P},\quad
                     |D|=|\textstyle\sum\pm B|\le Q2^{(1-\eta)P}.
\]
As in the [arithmetic separation proof](../phase6/CANONICAL_ARCS.md), the fixed-place integral Subspace Theorem forces \(D=0\) for sufficiently large \(t\). For each surviving type, its probability before conditioning is at least \(e^{-\delta P}\). Bounding the signed equality for independent unconditioned starts with auxiliary scalar equal to its specified \(v\), conditioned energy is therefore at most \(e^{Q\delta P} C_2 2^{-d_2l}\ll 2^{-d_1P}\). Dropping internal good restrictions in applying this upper bound can only enlarge the equal-numerator event. A discarded type has zero good submeasure.

Fourier inversion and Hölder bound the convolution of any \(Q\) such good conditional submeasures by \(O(2^{-d_1P})\) per quantized cell. If their real sum hits a prescribed arc of length \(2^{-P}\), at most \(Q+2\) quantized cells can occur. Conditional on all other chunks' actual contributions, the arc merely translates. Expand the \(N\) bridge measures as sums of good and bad submeasures. Terms using at least \(Q\) good measures obey this bound. In the remaining terms the unconditioned chance of \(N-Q+1\) actual bad chunks is at most \(2^N e^{-c_3P(N-Q+1)}\). For each specified subset, apply the uniform bad-probability bound successively given full histories at those chunk starts. This estimate does not assume that unconditional adjacent Markov chunks are independent. Adding back the guard failure proves (2).

## Counting actual integer trajectories

It is enough to consider intervals of dyadic width \(2^k\). Take \(t=k+\lfloor e k\rfloor\), with \(e>0\) fixed, small enough to admit \(P=t-k\) in (2) and to satisfy \((1+e)\log_2(3/2)<1\). Choose \(h<d<1\). In any such source interval and for \(t>k\), each fixed word has at most one integer source. Its normalized canonical source therefore lies in a specified circle arc of width \(2^{-P}\), independent of the word. Conditional on any fixed initial vertex, every word with \(q\ge p_*t-\eta'k\) odds has probability at least
\[
      c_G \lambda^{-t}z^q\ge c_G 2^{-ht-\eta'k\log_2 z}.
\]
The graph is right-resolving, so the word has at most one path from that vertex. A finite sum over possible starting vertices covers all admissible words. By (2) these high-odd-count sources contribute at most
\[
                O(2^{hk-(d-h)\lfloor ek\rfloor+\eta'k\log_2 z}).
\]
Fix \(\eta'>0\) sufficiently small after \(e\) to retain a strict saving.

For each lower \(q\), the affine formula sends the sources into an interval of width at most
\[
                 3^q 2^{k-t}+(3/2)^t+1\le 2^{(1-c)k}
\]
for a fixed \(c>0\) and all sufficiently large \(k\). Indeed \(C<3^t\), and the critical product has \(3^{p_* t}=2^t\). Let \(A(k)\) be the supremum of \(\#(I\cap V)\) over intervals of width \(2^k\). At uniformly bounded fixed-time multiplicity, the lower \(q\) groups total \(O(t A(\lceil(1-c)k\rceil))\). Decrease the high-group saving, if necessary, to \(0<\gamma<h\). A substitution by \(K 2^{(h-\gamma)k}\) in the recurrence absorbs the lower group at sufficiently large \(k\), and choosing \(K\) handles the initial values. This proves (1).
