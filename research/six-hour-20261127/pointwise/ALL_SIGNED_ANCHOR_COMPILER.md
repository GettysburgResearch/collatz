# Many simultaneous shallow clocks for signed rational families

Write U(x)=(3x+1)/2^e for the ordinary map on positive odd integers, with e the full binary valuation. A signed anchor t is a reduced rational p/q, q>0, and its score at x is v₃(x+t), including +∞ if x=−t. Its height is max(|p|,q).

## Finite path theorem

Let A be a finite nonempty set of M signed anchors of height at most H, with 3 not dividing their denominators. An exact edge from t to u is labeled by a positive integer e for which

    2^e u=3t−1.

For every ε>0 one dictionary of total division cost O_ε(M^(1+ε) log(2H)) represents **every finite exact path** using O_ε(1) counted pieces. A piece is a finite factor of a repeated nonempty exponent word having a letter ≥2, or a singleton e≥2. Strings of ones are free. Both bounds are uniform in the signs, the binary valuations, the path length, its start and its terminal cut. There can be several outgoing exact edges.

For a rational with odd numerator and odd denominator, an edge ending in the same binary-unit sector must have e=v₂(3t−1). Since t=1/3 is excluded, this defines at most one such edge. The functional-graph compiler from the companion review therefore covers every initial stretch in this sector. The label on a unit-to-unit edge is ≤log₂(4H), by the reduced numerator of 3t−1. Its sign is unrestricted. Any edge exiting the sector is a singleton or a free one. A binary-integral even state, including 0, goes directly to a state with even denominator, paying at most one more such edge. From a state t with even denominator, every exact successor satisfies

    v₂(u)=v₂(t)−e.

No path can return to the earlier sectors. In particular the induced even-denominator graph is acyclic and the division sum between any two of its vertices is at most log₂ H. The exceptional boundary edges need no dictionary word and cost at most one counted singleton apiece regardless of their labels.

### Coding the even-denominator part

For a finite word w of positive integers define C(∅)=1 and

    C(e::w)=3^|w|+2^e C(w).

The terminal marker 1 makes every code odd. For fixed length k≥1, the binary valuation of C−3^(k−1) gives the first exponent and the quotient gives the remaining code. Thus equal codes at equal lengths give equal words, including the final exponent. For an exact path t→u whose word w has length k and division sum E, induction gives

    C(w)=3^k t+2^E(1−u).

The division sum on the even-denominator graph is v₂(t)−v₂(u), determined by its endpoints. Hence at most one path with supplied endpoints and supplied length is possible. The six local declarations of AnchorPathCode.lean formalize the positive-word code, transport, and the resulting uniqueness when length and division sum are fixed. The endpoint valuation and the graph arguments here are written proofs.

Let P(v) be the number of complete paths from v to sinks of this finite acyclic graph, counting the singleton empty path at a sink. Any path has length at most M−1. Its endpoint and length take at most M² possible pairs. The code bound gives 1≤P(v)≤M². Along each edge P is nonincreasing, since P(v) is the sum of the P values at its children.

Take L=max(2,ceil M^ε), and give v grade g=floor(log_L P(v)). For each v store all paths inside its grade beginning at v that cannot be extended within this grade. Two such paths are prefix-incomparable. Each admits P(u)≥L^g continuations from its terminal vertex u to genuine sinks. Their complete-path extensions are mutually disjoint and are counted by P(v)<L^(g+1). Thus fewer than L words are stored per vertex. Each such word costs at most log₂ H by the valuation decrease. Storage is at most ML log₂ H. Even if a supplied path leaves the grade before it reaches a last same-grade vertex, its segment inside this grade extends to one of the stored words. Each strictly grade-crossing edge costs one singleton or a free one. There are at most 1+log_L(M²) visited grades. After combining this dictionary with the binary-unit sector dictionary and deleting duplicates, empty words and all-one words, the bounds follow. Add (2) if the dictionary is empty.

## Consequences on actual positive trajectories

**Signed small-family theorem, source-qualified to Yu and Weaver.** Fix θ<1 and b≥0. On a fixed non-eventually-periodic positive odd orbit, let A_N be any nonempty collection of at most C₀(N+2)^θ signed reduced rationals of height H_N≤C₀(N+2)^b, with arbitrary denominators. At least c_θ log N log log N clocks i∈[0,N] have

    max_{t∈A_N} v₃(x_i+t) ≤ C log(2H_N) log(3+N+log(n+1)).

For a sufficiently large primitive ordinary P-cycle, the corresponding P cyclic states have the same count bound with threshold C log(2H_P) log(3+P). Constants are uniform as in the companion frozen theorem. In particular c_θ need not depend on b.

For a reduced anchor whose denominator is a multiple of three the score is always negative. If every anchor is of this type the bound is automatic. Otherwise select a maximizing anchor with denominator prime to three at each clock. Across D nonexact transitions, the division word has cost O_ε(D+1), by the finite theorem. Choose ε with θ(1+ε)<1, then the dictionary budget is at most N^β for some β<1 eventually. Weaver (A1) for the fixed source gives D≫_θ log N log log N. In a sufficiently large primitive ordinary cycle the budget is less than P, precluding a represented positive cycle; apply (C6). On a residual edge with one infinite score the other is finite; the nonzero edge identity and Yu bound from the companion review supply a shallow endpoint in all cases. This gives the asserted counts. The signed statement deliberately retains the non-eventual-periodicity assumption for the orbit part: the fixed orbit 1 and anchor −1 have infinite score at every phase.

**Unrestricted positive-family corollary, including full height balls.** Fix any positive odd starting integer n. For every sufficiently large N and *every* H≥1, the interval [0,N] contains at least c log N log log N clocks with

    max_{0<p,q≤H} v₃(x_i+p/q) ≤ C log(2H) log(3+N+log(n+1)).

Coprime p,q suffice. The constants can be taken absolute; the onset may depend on the fixed source. Every sufficiently large primitive ordinary P-cycle satisfies the analogous count with C log(2H) log(3+P), uniformly for all H≥1. No polynomial size restriction on H is needed.

For H≤log N there are ≤H²≤N^(1/2) positive reduced rationals for all sufficiently large N. The signed small-family theorem with θ=1/2 applies on a non-eventually-periodic source. A periodic or eventually periodic fixed source has finitely many values x≤X_n, so v₃(x+p/q)≤log₃[H(X_n+1)] at every clock once N is sufficiently large, uniformly in H. For H>log N all positive rationals satisfy

    v₃(x_i+p/q) ≤ [log H+log(n+1)+i log(3/2)]/log 3.

This single elementary inequality suffices for the first floor(log N log log N) clocks as N grows. In the cycle statement apply the same argument starting at its least state; the bound log(x_min+1)=O(log(P+2)) follows from the effective two-logarithm inequality in Weaver (C2)–(C5), using P≤Σe≤2P. The case H≤log P again uses the signed theorem. The large-height argument uses an initial segment, so it yields no comparable count in [N,2N] on an unrestricted exponentially growing trajectory.

The elementary height split and the signed coding theorem are deductions beyond the frozen source. The nontrivial analytic inputs are Yu's printed page 337 inequality and Weaver Paper 15/v2 (A1), (C3)–(C6). Only the named interfaces have been source-inspected. [Yu](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf) · [Weaver, Paper 15](https://rstation.ai/problems/collatz/papers/15)
