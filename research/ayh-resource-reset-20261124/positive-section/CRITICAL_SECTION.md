# An eight-value section for positive Collatz convergence

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$, on positive ordinary integers. Say that $x$ hits $q$ if $T^k(x)=q$ for some $k\ge0$. For odd $n$ put
$$
d=\lfloor\log_2 n\rfloor,\qquad e=v_2(3n+1),\qquad
\sigma(n)=5e-(d+1),\qquad U(n)=(3n+1)/2^e.
$$
Here $\sigma$ is an integer and $U(n)$ is the next odd value. Call $n$ marked if $(d+1)(n-2^d)\le70\,2^d$. Let $S$ be the marked odd positive integers with $\sigma\ge0$, and let $B$ be those with $0\le\sigma\le7$.

**Theorem.** Every positive integer hits one if and only if every integer in $B$ hits one. For each fixed odd $u$, at most one member of $B$ has $U(n)=u$. For every fixed positive $q$ coprime to three, arbitrarily large members of $B$ hit that same $q$.

The starting result is PR 197's equivalence between universal convergence and convergence on $S$, and its cofinal marked predecessors for each fixed ternary-unit target. PR 196's half-size merger applies also at $H=1$. Its additional inverse-clock obstruction has different hypotheses. [PR 197, original marked-section proof](https://github.com/GettysburgResearch/collatz/blob/840c4b16099c392010b66a3e51b7ad55ef789dad/research/ayh-resource-reset-20261124/positive-section/MarkedPredecessors.md) · [PR 196, half_source](https://github.com/GettysburgResearch/collatz/blob/10fcd50c45c219d8f794034f8d46d127d86e562c/research/astra-orbit-cycle-20261124/mergers/HalfSource.lean#L35)

## The smaller marked partner

Take $n\in S$, $n>1$, with $\sigma(n)\ge8$. Necessarily $e\ge3$. If $e=1$ then $\sigma\le4$. If $e=2$ then $n\equiv1\bmod 8$, so $n>1$ gives $n\ge9$, $d\ge3$, and $\sigma\le6$. Thus $n\equiv5\bmod8$, say $n=8r+5$. In PR 196's notation $H=v_2(n+1)=1$, $M=(n+1)/2=4r+3$, and $3M\equiv1\bmod4$.

The half-size partner $(n-1)/2=4r+2$ immediately halves to the odd positive integer $m=(n-1)/4=2r+1$. Its next step meets $n$'s path:
$$
T(m)=3r+2=T^3(n).
$$
Indeed $n$ goes to $12r+8$, then $6r+4$, then $3r+2$. Therefore $m$ hits one exactly when $n$ hits one, including the case when one of the paths meets one before the common endpoint, since one is periodic. Further, $3n+1=4(3m+1)$, so $e(m)=e-2$ and $U(m)=U(n)$.

Binary digit lengths give $d(m)=d-2$ exactly because $n=4m+1$ and $m\ge1$. If $D=d(m)$, the mark on $n$ yields
$$
(D+3)\bigl(4(m-2^D)+1\bigr)\le 280\,2^D,
$$
which implies $(D+1)(m-2^D)\le70\,2^D$. Hence $m$ remains marked and $\sigma(m)=\sigma(n)-8\ge0$.

Repeating this reduction ends at one or at a member of $B$. Each reduction strictly decreases the positive source, retains its next odd value, and preserves eventual convergence in both directions. The value one itself has surplus nine and is a known convergent base case. It follows that convergence on $B$ implies convergence on $S$, hence universal convergence by PR 197. The reverse implication is immediate. This argument allows a smaller source and the original source to reach their common value at different clocks.

## One possible representative per next odd value

Fix a positive odd $u$ that occurs as a next odd value. Then $3\nmid u$. All its positive odd predecessors have the form
$$
x_e=(2^e u-1)/3,\quad e\ge1,\quad 2^e u\equiv1\bmod3 .
$$
The permitted exponents constitute a single parity class. Consecutive sources satisfy $x_{e+2}=4x_e+1$, increasing the binary exponent by two and the surplus by eight. Thus the interval $0,\ldots,7$ contains at most one surplus on this entire fiber, before checking the mark.

In fact each such fiber has only finitely many marked points. Start at the least allowed exponent, with source $x_0$ and binary exponent $d_0$; here the subscript counts steps along the fiber. After $j$ steps the source and its binary exponent are $x_j=4^j x_0+(4^j-1)/3$ and $d_j=d_0+2j$. For $j\ge1$,
$$
\frac{x_j-2^{d_j}}{2^{d_j}}
=\frac{x_0-2^{d_0}+(1-4^{-j})/3}{2^{d_0}}
\ge\frac1{4\,2^{d_0}} .
$$
The mark requires the same ratio to be at most $70/(d_j+1)$, which tends to zero.

## Retaining the original target

Fix a positive $q$ coprime to three. PR 197 supplies arbitrarily large members $x$ of $S$ that hit $q$. For any prescribed $K\ge\max\{1,q\}$, only finitely many marked $x$ have $U(x)\le K$, by the finite-fiber result. Choose one of the supplied sources with $x>q$ and $U(x)>K$. The prefix from $x$ up to its next odd value consists of one odd step and a run of halvings down to $U(x)$. Every state after the start on this prefix is at least $U(x)>q$. Its hit of $q$ therefore occurs later and $U(x)$ itself hits $q$.

Reduce $x$ as above. The terminal source $y$ has $U(y)=U(x)>K$, so it cannot be one and belongs to $B$. It hits $q$ through that same odd value, and
$$
3y+1=2^{e(y)}U(y)\ge 2U(y)>2K.
$$
Since $K$ is arbitrary, these representatives are unbounded. This proof of cofinality uses only the stated fixed-target theorem of PR 197 and the finite-fiber argument. It applies to even as well as odd $q$.

## The remaining descent

On $B$ one has $d+1\le5e\le d+8$. In particular, the next odd value satisfies
$$
3\cdot2^{-8/5}n^{4/5}\le U(n)\le 4n^{4/5}.
$$
Thus large members drop below their own starting value. If a quarter reduction remains legal on a member of $B$, its new surplus is negative. The unique representative in each odd fiber supplies no strictly smaller member of $B$ in that same fiber. Cofinal marked predecessors of an arbitrarily specified $q$ can have $U>q$, as the preceding proof explicitly arranges. A recurrence from the new endpoint to a smaller member of $B$ in the same component, or some other global convergence argument, is still needed.

Each of the eight surplus values occurs at arbitrarily high octaves. For fixed $s\in\{0,\ldots,7\}$ take $e$ large, $d=5e-1-s$, and choose the odd residue $1\le r<2^{e+1}$ satisfying $3r+1\equiv2^e\bmod2^{e+1}$. Then $n=2^d+r$ has binary exponent $d$, exact valuation $e$, and surplus $s$. The bound $(d+1)r\le70\,2^d$ holds for all sufficiently large $e$.

The integer checker accompanying this note covers positive odd starts through 250,000. It independently evaluates the physical clocks, the mark, the exact valuation and the terminal odd endpoint. It checks the full repeated reduction from every source in $S$ in that range. General conclusions above follow from the written proof; the finite checks describe their stated range only.
