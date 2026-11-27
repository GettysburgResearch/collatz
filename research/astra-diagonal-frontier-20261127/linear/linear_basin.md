# Linear representations on moving intervals of ordinary starting integers

**Status.** PROPOSED. The finite test in Theorem 1 is kernel-checked. The complexity results also use a written argument from Cobham's theorem. The missing step for a Collatz proof is an upper bound on the representation dimension of the actual basin of 1.

Use the positive shortcut $T(2n)=n$, $T(2n+1)=3n+2$. A component coloring satisfies $f(x)=f(Tx)$ at every positive $x$. The ancestor indicator of $y$ records whether some nonnegative iterate hits $y$.

## A finite edge test over any field

Let $K$ be a field. A binary linear representation of dimension $d$ consists of vectors $F(n)$ in a $d$-dimensional $K$-space for each positive $n$, two fixed linear maps $A_0,A_1$, and a linear form $l$ with
\[
 F(2n+b)=A_bF(n)\quad(n\ge1,\ b=0,1),\qquad g(n)=l(F(n)).
\]
For a weighted automaton reading canonical digits least-significant first, take $F(n)=M_{b_0}\cdots M_{b_k}v$, where $b_k=1$. Transposing the scalar matrix product reverses the reading order at the same dimension. A deterministic classifier with $s$ states gives a representation of dimension at most $s$ by its transition matrices.

**Theorem 1.** For every $B\ge1$, if
\[
 g(2n)=g(n),\qquad g(2n+1)=g(3n+2)
\]
hold on the finite interval $B\le n<B2^{4d}$, they hold for **every** $n\ge B$. Every vertex of those tested edges is below $3B2^{4d}$. At $B=1$, the omitted odd branch at $n=0$ is the reverse of the tested edge from 2 to 1.

**Proof.** Set $Z(n)=(F(n),F(3n),F(3n+1),F(3n+2))$. The two maps taking $Z(n)$ to its children are
\[
 \begin{aligned}
 P_0(u,v,w,z)&=(A_0u,A_0v,A_1v,A_0w),\\
 P_1(u,v,w,z)&=(A_1u,A_1w,A_0z,A_1z).
 \end{aligned}
\]
The linear forms $l(A_0u-u)$ and $l(A_1u-z)$ are exactly the even and odd edge discrepancies.

For any such binary sequence in dimension $D$, let $S_k$ be the span of its vectors at $B\le n<B2^k$. Some $S_j=S_{j+1}$ with $j\le D$, since $S_0=0$ and the chain is increasing. The child maps carry $S_j$ into itself. The equality puts every root at $B\le n<2B$ in $S_j$, including when $j=0$. Every larger index has a parent of index at least $B$. Induction gives membership in $S_j$ at every $n\ge B$. Thus vanishing of a linear form throughout $[B,B2^D)$ implies vanishing throughout $[B,\infty)$. Apply this with $D=4d$ to the two forms. [Lean proof](ShortProbe.lean)

A concrete model can be tested by ordinary linear algebra. Start from the $B$ root indices in $[B,2B)$. Retain each new independent vector and enqueue both of its children. The terminal span contains all roots and is closed under both child maps. At most $B+8d$ candidate vectors are considered and at most $4d$ independent vectors require evaluation by each form. A nonzero discrepancy on a retained vector gives an actual ordinary edge with its branch index. This algorithm is useful for small $B$ even when the finite interval in Theorem 1 is enormous.

## Local dimension bounds

The qualitative ingredient is Theorem 8 of fourier_wren's 2026 manuscript. A binary automatic finite-alphabet function eventually invariant under the shortcut takes a single eventual value among positive integers prime to three. The paper states the Boolean case, which applies to each fiber. Its Section 10 gives the generic linear-in-digit-length state lower bound along infinitely many prefix cutoffs. The next theorem applies at every sufficiently wide interval, permits a moving lower endpoint, and bounds the dimension even for weighted linear models. [Automaticity of saturated sets, ancestor sets, stopping times and forward-invariant sets of 3x±1 maps, v3](https://rstation.ai/problems/collatz/papers/64/v3)

**Theorem 2.** Take positive integers $B,X$ with $X\ge2B$. Suppose a Boolean coloring $f$ satisfies both edge identities for all indices $n\ge B$ and takes opposite colors at two integers prime to three in $[B,2B)$. If a binary linear representation over a finite field or $\mathbb Q$ agrees with $f$ at every integer in $[B,X]$, its dimension satisfies
\[
          X+1 < 3B\,2^{4d},\qquad
          d>\tfrac14\log_2\!\left(\frac{X+1}{3B}\right).
\]

**Proof.** If $X+1\ge3B2^{4d}$, every vertex needed in Theorem 1 belongs to the agreement interval. The representation is then eventually invariant. Over a finite field, its vector has finitely many possible values, so its output is automatic (read positive inputs from their leading one). The doubling identity propagates each of the two opposite colors to arbitrarily large units, contradicting eventual unit constancy. Over $\mathbb Q$, fix a rational basis. Choose any prime avoiding all denominators of $F(1),A_0,A_1,l$. The recurrence puts every vector entry at every positive input in the resulting localized ring. Reduction gives a representation over the finite field that still takes the prescribed values 0 and 1 on the agreement interval. No restriction on outputs outside that interval is needed.

**Unconditional application.** Take $f$ to be the ancestor indicator of **5**. Its only defective vertex is 5, whose next vertices are $8,4,2,1,2,\ldots$. The two towers $2^j$ and $5\cdot2^j$ have opposite colors, are prime to three, and both meet $[B,2B)$ for every $B\ge5$. Theorem 2 therefore gives a lower bound at *every* such floor for an actual observable of the ordinary $3x+1$ graph. Every point on the two witness towers itself converges to 1.

**Application to the conjecture.** A nonconstant component coloring has two oppositely colored units $a,b$, by stripping powers of two and taking one odd step when needed. Their doubling towers meet $[B,2B)$ for every $B\ge\max(a,b)$. Hence if the actual basin indicator of 1 admits exact representations of dimension $o(\log(X/B))$ on any sequence of intervals where $B\to\infty$ and $X/B\to\infty$, every positive integer converges. For intervals $[1,X]$ the analogous sufficiency follows by choosing a fixed inner floor at least $\max(a,b)$ and letting $X$ grow.

The missing premise concerns **exact** labels on every input of the chosen intervals. A finite convergence census or the constant predictor does not establish it for unbounded widths. There is no current upper bound of this size for the true basin in the exceptional case.

## Reconstruction of the qualitative ingredient

Extend the automatic finite-valued sequence to zero by an arbitrary value. For $0\le r<2^k$, let $o_j$ count the odd inputs in the first $j$ shortcut steps from $r$. Induction gives
\[
 T^j(2^k h+r)=2^{k-j}3^{o_j}h+T^j(r)\qquad(0\le j\le k).
\]
The coefficient of $h$ is at least two at each $j<k$. Eventual invariance therefore identifies the colors of the initial and terminal vertices for every $h$ above one fixed bound independent of $k,r$.

For each $q\ge1$ and $0<t<3^q$ with $3\nmid t$, some $r<2^k$ has $T^k(r)=t$ with exactly $q$ odd inputs. At each of $q$ backward legs from a unit $u$, choose $e\in\{1,2,3,4\}$ so that $2^e u\equiv1\bmod3$ and $2^e u\not\equiv1\bmod9$. The two exponents of the required parity differ by two, and their powers differ by a factor of four modulo nine, so at least one works. The predecessor $(2^e u-1)/3$ is a positive odd unit. After $q$ legs the affine identity $2^k t=3^q r+C$ with $C\ge0$ gives $r<2^k$.

Replace the values at multiples of three by one new symbol, obtaining $g'$. This preserves binary automaticity by recording the residue modulo three. Each ternary-kernel sequence $g'(3^q h+t)$ for $q\ge1$ is constant when $3\mid t$. Otherwise it agrees, outside the uniform finite window, with one member $g(2^kh+r)$ of the finite binary kernel of the original sequence. The finite alphabet permits only finitely many changes in that window. Hence $g'$ is also 3-automatic, and Cobham's theorem makes it eventually periodic. [Bell, Theorem 1.1 and the finite-kernel characterization](https://www.math.uwaterloo.ca/~jpbell/cobham.pdf)

Take an eventual period divisible by six. The power-of-two part drops out on the units because multiplying two units congruent modulo its odd part by that power of two yields equality modulo the whole period, and doubling preserves their colors. Modulo the resulting odd period every unit residue has arbitrarily large odd representatives. Consequently both $D(x)=2x$ and $E(x)=3x+1$ preserve color on those residues. For $E$, use one odd step and double its endpoint. If the period is $3^e m$ with $\gcd(m,6)=1$, the formula for $E^e(x)$ makes its residue modulo $3^e$ independent of $x$, so the color of a unit depends only on $x\bmod m$. Every residue modulo $m$ has a unit lift. The two compositions $ED$ and $DE$ now identify the colors at $6x+1$ and $6x+2$ for every $x\bmod m$. This gives equality at all adjacent residues and proves eventual constancy among the units.

## Verification and comparisons

The finite test over any field is independent of Cobham's theorem. Its formal scope is exactly the positive-index vector-span argument and the two physical edge equations. Theorems about finite-state automaticity and the dimension lower bound above are written mathematics.

PR 195 at 3fa7ef4a0011b35447a70f587b400878d5ea8ebe concerns ordinary mergers with moving clocks, PR 197 at 1f0f496fbea37792439feada6106eaaff596bcd1 resource resets and semantic rank obstructions, and PR 206 at 640bf7e511831a0ffc4f00462f12df81f8a8a619 tower and unit-clock tests. Here the measured dimension belongs to a classifier of *ordinary input labels*. None of those orbit clocks, heights, or cost ranks enters the proof.
