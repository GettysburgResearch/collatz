# Recursive compression of simple ordinary parity segments

**PROPOSED.** A straight-line binary grammar has literal-word nodes, binary concatenations, and unary positive integer powers. Nodes may refer to the same earlier node; exponents can vary without a bit cost. Use only nodes reachable from the root. Write B for the sum of the literal widths, counted once per node. Consider a root word of length L actually followed from a positive integer n under the shortcut Collatz map without any repeated state through the segment's endpoint. Put S=log₂(n+1), d=log₂(3/2) and c=1+d=log₂3.

1. With at most k nodes, for every ε>0 the segment satisfies L≤(1+ε)S+K_(k,ε)(B+1). The grammar, literals, exponents and trajectories are all allowed to vary.
2. With a binary concatenation nodes and r power nodes, without any restriction on their total number,
   
       S+d L ≤ 2^a c^r (S+d B).

The first estimate extends the [fixed-number result for flat powers](COMPRESSED_DESCENT.md); its constants are ineffective. The second is explicit.

## Bounded grammar size

Suppose that (1) fails and take a sequence on which [L−(1+ε)S]/(B+1)→∞. In particular B=o(L). After passing to a subsequence, the reachable grammar graph, node types and ordered references are fixed. Each power's exponent is either a fixed positive integer throughout, or tends to infinity. Unroll references and fixed powers recursively, stopping at the first divergent power on each path. There are only a bounded number of leaves in this unrolling, since the graph is fixed and acyclic and the expanded exponents are fixed. The directly exposed literal widths sum to O(B). For each exposed divergent power of exponent e, the full flattened base word has width at most L/e=o(L). Thus the entire word has a flat description by a bounded number of powers and gaps of total description width o(L), counting each power's base once. If there are no powers then L=O(B), already impossible. Apply the flat simple-segment bound with ε/2. It gives L≤(1+ε/2)S+o(L), contradicting L>(1+ε)S.

## An effective traversal

Two initially equal strings of p parity symbols force the starting states to agree modulo 2^p: iterate one branch at a time or use its odd affine numerator slope. In a power of a word of length b and exponent e≥2, the starts at offsets 0,b therefore agree modulo 2^((e−1)b). They are distinct by simplicity. If the start is x, their difference has absolute value less than (x+1)(3/2)^b because T(y)+1≤(3/2)(y+1). Consequently e b≤log₂(x+1)+c b. This bound also holds for e=1.

Traverse the grammar depth-first in word order, maintaining the actual elapsed shortcut time t. At a node visited before, consume its entire word without re-expansion. At a fresh concat, traverse both children; at a fresh power, traverse its base once and then consume its remaining copies in one step. A fresh literal simply advances by its width. Each processed reference is to a fresh or fully completed node by acyclicity. At a reused reference the node's width is at most t, because its earlier full occurrence started at nonnegative time. Thus S+d t increases by a factor at most 2. On a fresh power starting at time t₀, its completion time is at most t₀+S+d t₀+c b=S+c(t₀+b). Immediately after the first base copy elapsed time is t₀+b; the power-completion step therefore multiplies S+d t by at most c. Fresh literals add d times their widths, with total at most dB.

If there are l literal nodes, the number of reused references is exactly (2a+r)−(a+r+l−1)=a−l+1≤a. Every outgoing edge of each reachable concat or power was traversed once, and every node except the root has exactly one first-discovery edge. Multiplying the factors bounds S+dL as in (2). The same proof works from any phase of a simple orbit.
