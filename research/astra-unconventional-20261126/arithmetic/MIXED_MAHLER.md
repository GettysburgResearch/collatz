# A mixed-base incidence equation and its Cartier kernels

## The ordinary graph

Set $u=(x+1)/2$ for an odd ordinary state $x$. The two accelerated steps having division exponent one or two become the disjoint edges
$$
 A_v:2v\longrightarrow3v,\qquad B_v:4v+1\longrightarrow3v+1 .
$$
Here $v$ is a nonnegative integer. Each vertex has at most one predecessor and one successor. The self-loops at 0 and 1 encode $x=-1$ and $x=1$. Nontrivial finite cycles in this graph use ordinary positive odd states. Every bounded least-tripling-disagreement cycle with the pinned gap-one-or-two reduction appears here. This graph also includes ordinary gap-one-or-two paths outside that reduction. Its two branches are the first two rows of the inverse of Collatz’s 1932 permutation. [Lagarias, AMS Centennial Problem 1932](https://www.ams.org/bookstore/pspdf/mbk-121-prev.pdf)

For formal series $A(X)=\sum a_nX^n$, $B(X)=\sum b_nX^n$ over a field, consider
$$
 A(X^2)+X B(X^4)=A(X^3)+X B(X^3).\tag{1}
$$
The two outgoing supports at each vertex are disjoint, as are the incoming supports. Consequently a nonzero edge weight extends with the same value both forward and backward forever. Every solution is a choice of one weight per complete cycle or doubly infinite component, with weight zero elsewhere. Polynomial solutions are finite linear combinations of cycle indicators. In particular a classification of *nonconstant polynomial* solutions would still require a positive cycle exclusion. Operator fixed-point descriptions of Collatz cycles have a history in work of Berg–Meinardus and Neklyudov. The following kernel comparison uses the partial permutation specific to (1). [Neklyudov, 2022](https://arxiv.org/abs/2106.11859)

Wren previously transferred residual languages between bases for saturated shortcut sets and treated automatic invariant sets for the different partial map of Yolcu–Aaronson–Heule. The edge-weighted assertions below use both nonoverlapping incidence rows, and the arbitrary-gap variant retains sums over overlapping incoming rows. [Wren, Theorem 1 and §10.2](https://rstation.ai/problems/collatz/papers/64/v2)

## Kernel comparison

For a sequence $w$ write $L_{m,r}w(n)=w(mn+r)$, $0\le r<m$. Let $K_q$ be the union of all $L_{q^k,r}a$ and $L_{q^k,r}b$, with the zero sequence adjoined. Let $V_q$ be its vector span.

**Theorem.** For every formal solution of (1), every ternary section of every element of $K_2$ lies in $K_2$. In particular $K_3\subseteq K_2$. Every element of $K_2$ lies in $K_3$ or is the even/odd interleaving of two elements of $K_3$. Hence
$$
 |K_3|\le |K_2|\le |K_3|+|K_3|^2,\qquad
 \dim V_3\le\dim V_2\le3\dim V_3 .
$$
The section comparison uses only equality of coefficients and a distinguished zero, so it also applies to edge labels with an arbitrary alphabet and zero.

Read (1) at vertices $6n,6n+2,6n+4$, then at $12n+1,12n+5,12n+9$. Reading it also at $12n+3,12n+7$ gives the last column below.
$$
\begin{array}{c|ccc|c}
 &w(3n)&w(3n+1)&w(3n+2)&\text{missing outgoing edge}\\\hline
 a&a(2n)&0&b(2n+1)&a(4n+1)=0\\
 b&b(4n)&0&a(4n+3)&b(4n+2)=0
\end{array}                                                     \tag{2}
$$

For $L_{m,c}w$ with $m=2^k$, write $mj+c=3d+e$ for $0\le j,e<3$. Then $d<m$, and
$$
 L_{3,j}L_{m,c}w=L_{m,d}L_{3,e}w .
$$
By (2) the inner term on the right is zero or a binary section of $a$ or $b$. Composing two binary sections is another binary section. Iteration proves the first assertion. [Lean proof](MixedMahler.lean)

For the converse, the inverse reading of (2) is the following deterministic prefix rule at an index $v$.

| Sequence | Low bits of $v$ | Output sequence and index |
|---|---|---|
| $a$ | even | $a(3v/2)$ |
| $a$ | $3\pmod4$ | $b((3v-1)/4)$ |
| $a$ | $1\pmod4$ | zero |
| $b$ | odd | $a((3v+1)/2)$ |
| $b$ | $0\pmod4$ | $b(3v/4)$ |
| $b$ | $2\pmod4$ | zero |

Start at $v=2^k n+r$. The current index after $j$ legal letters has the form $3^j2^l n+C$, where $l$ dyadic bits remain and $0\le C<3^j2^l$. When $l\ge2$, the table consumes one or two known bits and preserves the bounds with $j+1$ and $l-e$, where $e$ is the number of consumed bits. Indeed the new integer constant is $(3C+\delta)/2^e$, $\delta\in\{-1,0,1\}$, with the sign and denominator fixed by the row. The row with $\delta=-1$ has $C\equiv3\pmod4$. At $l=0$ the result is one ternary section. At $l=1$, apply the one-bit rule if available. Otherwise evaluate separately at $n=2m+b$, $b=0,1$, where the last two-bit rule resolves the value with a pure ternary section or zero. The resulting sequence interleaves those two sections. This proves the cardinality bound. Each interleaving belongs to the sum of the even insertion and odd insertion of $V_3$. Together with $V_3$ itself this gives the dimension bound.

## Rigidity at infinite support

1. **Finite alphabet.** If the pair is automatic in either base 2 or base 3, the two coefficient sequences are ultimately periodic by the section theorem and Cobham's multiplicative-independence theorem. The joint kernel is finite exactly when both individual kernels are finite. [Cobham, 1969](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata)
2. **Sparsity.** Every vertex carrying a nonzero outgoing edge admits $N$ legal future letters for every $N$. A word with $k$ letters of type $A$ and $N-k$ of type $B$ imposes one residue class modulo $2^{2N-k}$. The endpoint after clearing this denominator is $3^N u+c$, and $3^N$ is odd. The upper natural density of surviving vertices is at most $(1/2+1/4)^N$ for each $N$. The supports of $a,b$ each have upper density zero by the index maps $n\mapsto2n,4n+1$. Thus ultimate periodicity implies finite support. Over a finite field of characteristic 2 or 3, simultaneous algebraicity of $A,B$ gives automaticity by Christol's theorem (automaticity in a prime-power base is equivalent to automaticity in its prime base). Hence both are polynomials. [Christol, Kamae, Mendès France and Rauzy, 1980](https://www.numdam.org/item/BSMF_1980__108__401_0/)
3. **Characteristic zero.** If either $A$ or $B$ is D-finite, its coefficient sequence satisfies a finite-order polynomial recurrence whose nonzero leading coefficient has finitely many integer roots. Upper density zero gives arbitrarily long zero intervals in its support complement. A block of zeros of recurrence order beyond the last such root propagates forward forever. One polynomial coordinate forces the other to be polynomial. Indeed if $F(X^d)-F(X^e)$ is polynomial for coprime distinct $d,e>1$, order them so $d>e$. For sufficiently large $n$ with $f_n\ne0$, the coefficient at $dn$ forces $e\mid n$ and $f_{dn/e}=f_n$. Along iteration the index grows and $v_\ell(n)$ falls by $v_\ell(e)>0$ at any prime $\ell\mid e$, a contradiction. Apply this argument with $\{d,e\}=\{4,3\}$ or $\{3,2\}$ in (1).
4. **Characteristic zero, regular sequences.** If $V_q$ is finite-dimensional for either $q=2,3$, the theorem makes it finite-dimensional at both bases. Each coordinate is therefore a Mahler series in both bases. Indeed, choose a basis of the joint section span. The vector of its generating series satisfies $F(X)=M(X)F(X^q)$ by splitting the coefficients into residue classes. For a chosen coordinate, its first $D+1$ iterates $f(X^{q^i})$ are linear forms in the $D$ entries of $F(X^{q^D})$, hence dependent over the rational-function field. Discard common initial iterates if necessary by splitting coefficients modulo the corresponding power of $q$. The Adamczewski–Bell theorem makes the coordinate rational. A rational coordinate is D-finite, so both coordinates are polynomials. [Adamczewski and Bell, Theorem 1.1](https://arxiv.org/abs/1303.2019)

Thus a nonpolynomial characteristic-zero solution has *both* coordinates non-D-finite and an infinite-dimensional joint kernel at each of the two bases. Polynomial cycle indicators always satisfy the automaticity and regularity criteria. Those criteria isolate the remaining finite-support problem.

## Lower bound even for a finite positive cycle

Let $N$ be the largest support index of one nonconstant polynomial solution. For each $M=2^i3^j\le\sqrt N/2$ extract the residue $N\bmod M$ of a coordinate having degree $N$. A binary section followed by a ternary section realizes this mixed section, so the result belongs to $K_2$. Its polynomial generating series has degree exactly $\lfloor N/M\rfloor$. For two distinct integers $M<M'\le\sqrt N/2$ the corresponding real quotients differ by $N(M'-M)/(MM')\ge4$. Unique factorization distinguishes all pairs $(i,j)$. There are $\gg(\log N)^2$ admissible pairs, and polynomial vectors with distinct degrees are linearly independent. Consequently
$$
 \dim V_2\gg(\log N)^2,\qquad \dim V_3\gg(\log N)^2
$$
over every coefficient field. This necessary condition concerns an actual finite indicator and exceeds the single-base logarithmic degree count. Available upper bounds for finite-support kernels still permit it.
