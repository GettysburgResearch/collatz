# A stronger state bound for digit prediction

**PROPOSED new theorem with a written proof.** This strengthens PR 200, abf36c63b4d0181541d7e029d390d6f636940750, research/regularity-rigidity-20261124/continuation/MACROSCOPIC_RIGIDITY.md, §§2–4. The Collatz input is exactly its PR 146 ordinary adjacent-variation and macroscopic discrepancy estimates. The finite Markov chain argument below is independent of Collatz.

Fix a digit base \(B\ge2\). For each integer cutoff \(X\), let \(g_X\) be the output in \([0,1]\) of a deterministic \(S=S_X\)-state machine reading the canonical most-significant-first base-\(B\) digits of the input. Let \(f\) be an exact \(\{0,1\}\)-valued invariant label of the positive shortcut Collatz graph, and \(c_X=X^{-1}\sum_{n\le X}f(n)\). Assume the PR 200 shell estimates derived from PR 146 at f431078244e868dc699fad011044f0d5e7f76437. Then

\[
  S^4 B^{2S}=o(\log\log X)
  \quad\Longrightarrow\quad
  X^{-1}\sum_{n\le X}(f(n)-c_X)g_X(n)=o(1).
\]

In particular the conclusion holds for \(S\le(1/(2\log B)-\eta)\log\log\log X\), with a fixed positive \(\eta<1/(2\log B)\); all logarithms here are natural. The original sufficient condition was \(S^2=o(\log\log\log X)\). Machines, outputs and transition graphs can change with \(X\). No source or target is chosen randomly in the asserted integer correlation.

## Finite-chain meeting bound

In a closed irreducible class \(C\) of the uniform-digit transition matrix \(P\), let \(\pi\) be the stationary probability, \(d\) its period and \(C_0,\ldots,C_{d-1}\) its cyclic phases. They have mass \(1/d\). A path from a vertex of maximal stationary mass to any specified vertex has length at most \(S-1\). Since every positive transition has probability at least \(1/B\), stationarity at that path length gives

\[
 \min_{u\in C}\pi(u)\ge B^{-(S-1)}/S.
\]

Run two independent copies of \(P\) until they meet and use common future digits afterwards. Before the meeting their product runs on

\[
 H=\bigcup_{r=0}^{d-1} C_r\times C_r
\]

when its starting states have the same phase. The kernel \(P\otimes P\) restricted to \(H\) is irreducible. In a finite irreducible chain, paths between two vertices exist at every sufficiently large length in their allowed residue modulo \(d\). To see this, choose a reference vertex, take fixed paths via that vertex, and insert closed walks there. A finite set of their lengths already has gcd \(d\); nonnegative combinations of that finite set contain all sufficiently large multiples of \(d\) (after dividing by \(d\), take representatives of residues modulo one generator). The two paths needed for a product transition have the same allowed residue. The product has stationary probability \(\mu(u,v)=d\pi(u)\pi(v)\) on \(H\), since each cyclic class advances deterministically to the next and the denominator of the restriction of \(\pi\otimes\pi\) is \(1/d\). Every positive product transition has probability at least \(B^{-2}\). Thus every positive stationary edge flow is at least \(S^{-2}B^{-2S}\).

For any irreducible finite chain with stationary probability \(\mu\) and a positive transition \(P'(a,b)\) between distinct states,

\[
 \mathbb E_a T_b\le [\mu(a)P'(a,b)]^{-1}.
\]

Here is a direct proof. At \(a\), consider the successive iid excursions ending at the next return to \(a\). Their expected length is \(1/\mu(a)\). Indeed the expected occupation vector of one excursion, counting its starting state and omitting its terminal state, is stationary by shifting the clocks by one and has coordinate 1 at \(a\). Its entries are finite, since from each state there is a path of uniformly bounded length and positive probability to \(a\). By uniqueness of the stationary probability the claimed mean length follows. Stop after the first excursion whose *initial step* is to \(b\). The time to \(b\) is at most the sum of the complete lengths through this excursion. For excursion \(j\), whether it is used depends only on the first \(j-1\) excursions. Its expected contribution is therefore \((1-P'(a,b))^{j-1}/\mu(a)\). Summing gives the inequality without assuming that an excursion's length is independent of its first step.

From any pair in \(H\) a simple product-graph path to the diagonal has at most \(S^2-1\) edges. Successively hitting the vertices on that path, and using the strong Markov property and the edge-flow bound, gives

\[
 \mathbb E T_{\rm diag}\le S^4B^{2S}=M.
\]

Hitting a vertex may visit the diagonal before the last prescribed vertex, which only improves the upper bound. The unrestricted product chain suffices up to its first diagonal time. The coupled rows at clock \(k\ge1\) consequently differ in total variation by at most \(\min(1,M/k)\), by Markov's inequality. In particular \(P^ko(u)\) differs by at most this amount from the stationary conditional mean of the output on the final phase: initialize the other coordinate according to stationary probability conditioned on the starting phase. This compares exactly the quantity needed on digit blocks. A recurrent class consisting of one deterministic phase point per phase satisfies the assertion with zero error.

## Ordinary digit blocks

Only the following numerical conclusions about \(f\) are required: its total number of adjacent changes through \(X\) is \(O(X/\sqrt{\log X})\), and its centered sum on every subinterval of \([1,X]\) is \(O(X(\log X)^{-a})\) for a fixed \(a>0\). Take \(k=L=\lfloor\gamma\log_B\log X\rfloor\) with \(0<\gamma<\min(a,1/2)\).

On aligned intervals of length \(B^k\) contained in \([X/(\log X)^2,X]\), replace the machine output by its mean. For an interval without a change in \(f\) this preserves correlation. Exceptional intervals cost \(O(B^k/\sqrt{\log X})\) after normalization. The initial part and incomplete endpoints cost \(O((\log X)^{-2}+B^k/X)\). Among fixed-length canonical digit strings, the proportion still transient after their first \(L\) digits is at most \(\exp(-\lfloor(L-1)/S\rfloor B^{-S})\). Indeed every transient state admits a path of at most \(S\) digits into a closed class. Bound a truncated final digit length by all strings of that length, with only a base-dependent multiplicative factor in the total count.

For every remaining block, the state just before the last \(k\) digits is recurrent and the expected output differs from its final phase mean by \(O(M/k)\). The phase mean depends only on the class and phase after the first \(L\) digits and on the total digit length. Therefore it is constant on at most \(O_B(B^L\log\log X)\) ordinary intervals in the retained range. Pairing these intervals against the primitive discrepancy costs \(O_B(B^L\log\log X\,(\log X)^{-a})\). All errors tend to zero if \(S^4B^{2S}=o(\log\log X)\). The argument is uniform over all tables with the stated number of states.

If both basin colors have densities bounded away from zero at all large cutoffs (the separate hypothesis M in the source), the same elementary binary error identity as in PR 200 excludes vanishing mean classification error for this larger class along any unbounded subsequence. It gives an additional quantitative restriction on exact ordinary basins. It supplies no classifier in the enlarged class, and it establishes no new fixed-target predecessor estimate.

## Exact finite checks

Run `python -B check_automaton_coupling.py` in this directory. Using rational arithmetic, it checks stationarity of the product law on equal-phase pairs, the lower stationary edge flow, the expected single-edge hitting inequality, and the diagonal hitting-time bound by solving the finite first-step equations. It exhausts all 746 binary transition tables on one, two and three labeled states, covering 800 recurrent classes and 1,094 unequal unordered same-phase pairs, with largest mean meeting time 8. A four-state period-two example has largest mean 2, an eight-state delayed-phase example has largest mean 209, and a five-state ternary reset example gives \(7380/3281\). The tests do not establish the general theorem. The checker explicitly rejects optimized Python execution because its exact identities use assertions.
