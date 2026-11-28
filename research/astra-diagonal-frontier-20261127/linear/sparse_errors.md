# How many wrong labels can a changing finite classifier hide?

**Status.** PROPOSED written proof. A classifier may change with the cutoff, and its errors may be placed adversarially. The proof uses Konieczny's published asymptotic Cobham theorem. The two specified Collatz applications also use Mazur's fixed-target predecessor lower density. Neither external proof was rebuilt here.

Let $T(2n)=n$, $T(2n+1)=3n+2$. An eventually invariant Boolean function $f$ has only finitely many positive inputs $u$ with $f(u)\ne f(Tu)$. Assume both fibers have positive lower natural density. On canonical binary expansions, a deterministic classifier has one initial state, one transition per bit and a Boolean output at each state. Either reading order is allowed.

## Sparse defects force a single density-one color for a fixed automaton

**Lemma 1.** If a binary automatic Boolean $g$ has a zero-upper-density set of positive inputs with $g(u)\ne g(Tu)$, then $g$ agrees with a constant on a set of natural density one.

A fixed affine substitution $n\mapsto An+B$ with $A\ge1$ pulls a zero-upper-density set back to a zero-upper-density set. For a fixed native word from $r<2^k$, all the intermediate vertices on the route from $2^kn+r$ are affine in $n$ with positive integer slope. The identity
\[
 g(2^kn+r)=g(3^qn+t),\qquad t=T^k(r),
\]
therefore holds outside a zero-density set, where $q$ is the odd count. Every unit $0<t<3^q$ is available from some such prefix, as proved in the qualitative reconstruction in [the exact-rank note](linear_basin.md).

Let $g'$ replace the values on multiples of three by a new symbol. It is 2-automatic by taking a product with residue modulo three. Its ternary kernel is finite **up to equality outside a set of natural density zero**: at a unit head it agrees in this sense with an element of the binary kernel of $g$, and at a nonunit head of positive ternary length it is constant. Konieczny's Theorem B says that an automatic sequence in one base that is asymptotically automatic in a multiplicatively independent base agrees at density one with a periodic sequence. Consequently $g'$ agrees in this sense with some periodic $\lambda$. This uses the genuinely automatic first base. Asymptotic automaticity in both bases would give only a shift-invariance conclusion. [Konieczny, *An asymptotic version of Cobham's theorem*, Acta Arithmetica 211 (2023), Theorem B](https://doi.org/10.4064/aa220927-17-8)

Choose a period $M$ of $\lambda$ divisible by six. For any unit residue modulo $2M$, its positive representatives have positive density. Discard the zero-density exceptions to $g'=\lambda$, to edge equality, and to $g'(Tn)=\lambda(Tn)$. The last discard is valid on the fixed residue class by the affine formula for $T$. The remaining representatives impose the exact class equality between $\lambda(n)$ and $\lambda(Tn)$. The finite reduction in the exact-rank note now applies unchanged: doubling removes the power of two from the period, iterations of $3x+1$ remove the power of three, and comparing $6x+1$ to $6x+2$ collapses the prime-to-six residue graph. Thus $g$ is equal to one fixed Boolean $b$ on all units outside a set of density zero.

To handle nonunits, write $n=2^i u$ with $u$ odd. For fixed $i$, $u\equiv0\bmod3$ is followed by a unit $T(u)$. The finite sequence of halvings and the odd step transports $g(n)$ to $g(Tu)$ off a zero-density set, by the same fixed-affine argument (split the odd $u$ into its residue mod six). Hence all $i\le J$ contribute zero relative upper density of $g(n)\ne b$, for each fixed $J$. The tail $i>J$ has upper density at most $2^{-J-1}$. Let $J$ tend to infinity.

## Effective sparsity dichotomy for canonical binary automata

Consider any Boolean language recognized by an $N$-state binary DFA. For positive integers having $j+1$ bits, there are $j$ free equiprobable bits. In the most-significant-first convention consume the leading 1 first. In the least-significant-first convention absorb the final, fixed 1 into the output map. In either case the free bits are a walk on $N$ states from one fixed start.

* If a reachable closed strongly connected component contains an accepting state, the cumulative count through $X$ is at least $X\,2^{-2N-3}$ whenever $\log_2 X\ge 2N+2$. Reach that component along a fixed word $u$ of length at most $N-1$. After any free middle word of length $j$, append a path of length at most $N-1$ to acceptance. The resulting $2^j$ words are distinct, since the middle has fixed position and length. Choose $j=\lfloor\log_2 X\rfloor-2N-1$. Accounting for the fixed 1 and canonical digit order puts every resulting integer below $X$.
* Otherwise every accepting state is transient among the reachable states. From any reachable state, at least one word of length $N$ sends it into a closed component: take a shortest path and pad inside that component. Conditional on still being outside, each successive $N$-bit group thus has chance at least $2^{-N}$ of entering one. The accepted fraction of a complete $j$-free-bit range is at most $(1-2^{-N})^{\lfloor j/N\rfloor}$. Consequently the cumulative accepted proportion through an integer $X\ge4$ is at most
\[
 X^{-1/2}+2\exp\!\left[-2^{-N}\left\lfloor
 (\tfrac12\log_2 X-1)/N\right\rfloor\right].
\]
Here we discard inputs below $\sqrt X$. Complete the last bit-length range before applying the probability estimate to the rest. Their combined cardinality is at most $2X$.

In particular, absence of positive upper density is equivalent to the second case. The bound includes languages with very long finite transients.

## Quantitative lower bound on errors

**Theorem 2.** For any fixed $0<\delta<1$ and all sufficiently large $X$, let a changing classifier $g_X$ have
\[
             1\le s\le (1-\delta)\log_2\log_2 X
\]
states in either binary reading order. Put $N=3(s+1)^2+2$. For the fixed eventually invariant $f$ above, there exists $h_f>0$ independent of $X,g_X,s$ with
\[
       \#\{1\le n\le X:g_X(n)\ne f(n)\}
          \ \ge\ X\,\min(h_f/4,\;2^{-2N-8}).
\]
The threshold on $X$ can depend on $f$ and $\delta$. Thus even an error budget of $X^{1-\epsilon}$, for fixed $\epsilon>0$, requires at least $(1-o(1))\log_2\log_2 X$ states as $X\to\infty$. For a linear representation of dimension $d$ over $\mathbb F_2$, its at most $2^d$ accessible vectors give the corresponding lower bound $d\ge\log_2\log_2\log_2 X-O(1)$. The same dimension consequence holds over $\mathbb Q$ when the model outputs 0 or 1 on **every** positive input. In the dual space choose a basis of the span of all functionals obtained by appending bits and then reading the output. At most $d$ such functionals suffice. Each reachable positive-input vector gives a Boolean value at each basis functional, so there are at most $2^d$ distinct continuation behaviors, forming a deterministic machine after its leading one. The extra initial state, if needed for a convention that does not consume the leading one separately, costs at most one state. A rational model with unrestricted outputs away from the agreement prefix is covered only by the exact test in the companion note.

**Proof.** Write $g=g_X$, $E=\#\{n\le X:g(n)\ne f(n)\}$ and $b_f$ for the total number of physical defects of $f$. The two disagreement tests $g(2n)\ne g(n)$ and $g(2n+1)\ne g(3n+2)$ have binary automata of at most $N$ states. The chosen indexing below keeps both tested vertices below $X$.

In most-significant-first order the even test reads $n$ and asks whether its state and its zero child have different outputs. Index the odd test by its larger endpoint $m=3n+2$. Track the original state, the remainder modulo three, and the state of the binary digits of $\lfloor m/3\rfloor$, with one extra state until its leading 1. Ordinary long division in binary outputs $\lfloor(2r+b)/3\rfloor$ for incoming remainder $r$ and bit $b$. At the end retain remainder two. Append one bit 1 to the quotient to obtain $2n+1$, also correctly for an empty quotient.

In least-significant-first order the even test runs two copies of the classifier on $n$, prepending a zero to one copy. The odd test instead uses index $n$. Compare the copy with a prepended 1 to the copy reading $3n+2$. The latter starts with carry 2. For a bit $b$ and carry $r$, emit $(3b+r)\bmod2$ and update to $\lfloor(3b+r)/2\rfloor\le2$. Flush the remaining positive carry in canonical order. It is positive after canonical $n\ge1$ because $3n+2$ has more digits than $n$. This uses at most $3s^2$ states. The $n=0$ edge is the reverse of the first even edge and has no bearing on density.

For every orientation, all tested physical endpoints for positive *test indices* through $Y=\lfloor(X-2)/3\rfloor$ lie in $[1,X]$. The number of positive test inputs of either kind through $Y$ is at most $2E+b_f$, since each vertex used in either comparison is an injective function of its index. If $E<X2^{-2N-8}$, neither test can fall into the first population case above. Indeed $Y\ge X/4$ for large $X$, the positive-case lower bound is at least $X2^{-2N-5}$, and the fixed $b_f$ is smaller than $X2^{-2N-8}$ for all sufficiently large $X$ uniformly over the allowed $s$. Also $\log_2 Y\ge 2N+2$ in this range. Both edge tests then have zero upper density and so does the physical shortcut defect set. For the odd test indexed by $3n+2$, passing back to $2n+1$ preserves zero upper density.

By Lemma 1, $g$ agrees at density one with a constant. Its other color is a zero-density language recognized by the **original** $s$ states. The second population estimate therefore bounds its fraction in $[1,X]$ by $o(1)$ uniformly in the allowed $s$, because $\log_2 X/(s2^s)\to\infty$ uniformly there. Choose $h_f>0$ so that each fixed color of $f$ occupies at least $h_f X$ inputs for all large $X$. If also $E<h_f X/4$, both colors of $g$ occupy at least $3h_f X/4$, a contradiction.

**Two applications.** Under a counterexample, the true basin of 1 and its complement both have positive lower density by applying the fixed-target predecessor lower bound to 1 and to any bad unit. Theorem 2 then applies to the convergence indicator. Conversely, a sequence of models satisfying the displayed size condition and making only $X^{1-\epsilon}$ mistakes on an unbounded sequence of whole prefixes would prove convergence. Establishing the accuracy of such models on unbounded cutoffs remains open.

Unconditionally, take $f$ to be the ancestor indicator of 5. It has its sole defective vertex at 5. Both the ancestors of 5 and those of 16 have positive lower density by Mazur's fixed-target theorem (with the ordinary-to-shortcut conversion through the doubled target). They are disjoint: neither 5 nor 16 ever reaches the other, as their complete orbits meet at 8 and then run down to 1. Hence the quantitative error lower bound holds for this actual observable regardless of the status of Collatz. [Mazur's formal statement](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html)

**Comparison.** fourier_wren's discussion of Paper 64 already gives the qualitative obstruction for a *fixed* automatic classifier by intersecting a positive-density automatic language with each target basin. The argument here allows a new classifier at every cutoff and tracks its size and guaranteed error. Its sparse-defect lemma allows physical edge failures on any zero-density set for a fixed machine and needs neither the positive-density predecessor input nor an adjacent-orbit synchronization estimate. [Paper 64 discussion, November 1 addendum](https://rstation.ai/r/collatz/posts/53?after=LKMja63QjGcj_Qqi)
