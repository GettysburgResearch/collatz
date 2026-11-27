# Testing digit clearance in the full ordinary component graph

**Universal smaller-source merger OPEN.** A mixed binary/ternary input obstructs every finite repertoire of full-graph moves, even when the ranking function has positive residue-dependent weights. It has arbitrarily large ordinary approximants but is itself nonordinary. The separate digit theorem below applies to a single positive ordinary orbit.

## Dense binary suffix and ternary zero

Use the shortcut map $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. Track the same affine expressions in two coordinates: initially the binary coordinate in $\mathbb Z_2$ is $-1$, and the ternary coordinate in $\mathbb Z_3$ is $0$. Binary parity selects the forward map. An inverse step is $E(y)=2y$ or $F(y)=(2y-1)/3$; the latter must be ternary integral. All the coordinate values reached from this input are rational numbers, so their real order also makes sense.

**Two-clock obstruction.** Every legal finite path in the full undirected graph of these paired coordinates has affine expression $n\mapsto c n+d$ with $c\ge1$ and $d\ge0$. To prove this first go forward $t$ shortcut steps and then reverse any legal $j$ steps, where both clocks are arbitrary. All the forward steps are odd since $T(-1)=-1$. At the turning point the binary coordinate is $-1$ and the ternary coordinate is $D_t=(3/2)^t-1$.

Both inverse maps preserve the real interval $(-\infty,-1]$, so the final binary coordinate $z$ is at most $-1$. For the first $l\le\min(j,t)$ reverse steps the ternary coordinate is at least $(3/2)^{t-l}-1$. This follows inductively since both maps are increasing, $E(y)\ge F(y)$ for $y\ge0$, and $F(y)+1=2(y+1)/3$. If $j>t$, examine the coordinate after the first $t$ reverse steps. It is nonnegative, and its rational denominator is a power of three: the term containing $D_t$ has acquired $t$ factors of two in the numerator, and the additive terms have only powers of three as denominators. Ternary integrality thus makes this coordinate an ordinary nonnegative integer. Every subsequent ternary-legal inverse preserves that set: zero only admits $E$, and $F$ of a positive integer, when integral, is positive. The final ternary coordinate $d$ is therefore nonnegative at all depths. Since the binary and ternary outputs are respectively $d-c$ and $d$, one has $c=d-z\ge1$.

Every full-graph path has a common-forward-future representation because forward iteration is deterministic: sharing some forward iterate is an equivalence relation and each edge lies in it. The corresponding two-clock path has the same evaluated coordinates as the original path. Its affine expression agrees with the original at the two rational arguments $-1$ and $0$, so it agrees identically. This proves the obstruction for unrestricted finite graph words.

For every fixed length bound, choose positive integers congruent to $-1$ modulo an arbitrarily high power of two and to $0$ modulo an arbitrarily high power of three. Every path of the bounded length legal on one of these integers is legal on the paired input once the precisions exceed the bound (each move loses at most one digit per prime). It has $cn+d\ge n$. Therefore arbitrarily large positive odd sources have **no physically smaller vertex within any prescribed undirected graph distance**. The unrestricted-depth result in the preceding proof is on the **paired** source. The ordinary witnesses here can change with the distance bound.

## Exact obstruction to a finite-residue Bellman rank

Fix any modulus $M$, any positive function $w$ on its residues, and $s>0$. There is no fixed finite family of legal forward/backward words such that every sufficiently large positive ordinary $n$ has some word ending at $n'$ with
$$
 (n')^s w(n'\bmod M)<n^s w(n\bmod M).
$$
In particular this obstruction allows candidate moves with homogeneous ratio one and strict additive improvement.

Write $v=w^{1/s}$. Extend the paired input by a zero coordinate at every prime dividing $M$ other than two and three. Every reachable tuple then specifies a residue modulo $M$. Fix any finite path to a tuple, with map $n\mapsto cn+d$. By the Chinese remainder theorem the initial tuple has arbitrarily large positive ordinary approximants of arbitrarily high precision at every tracked prime. They follow the same finite path and reach arbitrarily large ordinary values since $c>0$. Positivity of all intermediate ordinary values holds for sufficiently large approximants because every slope is positive. If the alleged finite family covers all sufficiently large ordinary states, some one word works along a subsequence of approximants with precision and size both tending to infinity. Its congruence guards and destination residue then agree with those on the tuple. For its local affine map $y\mapsto ay+b$ and its current and destination weights $v_0,v_1$, necessarily $v_1a<v_0$, or $v_1a=v_0$ and $v_1b<0$. This follows by taking the exact difference $(v_1a-v_0)y+v_1b$ at those arbitrarily large inputs.

Choose such a word successively, starting at the paired input. At each new tuple the global affine expression still has $c\ge1,d\ge0$ by the two-clock obstruction. Along the infinite sequence the pair $(v_0c,v_0d)$ strictly decreases in lexicographic order. Its first entries are bounded below by $\min v>0$, and their successive ratios $v_1a/v_0$ belong to a finite set. Hence only finitely many strict first-entry decreases occur. On the remaining tail, the second entry changes by $v_1 b$ at each step, from a fixed finite set of strictly negative numbers, so eventually becomes negative. This contradicts $v_0 d\ge0$.

A rank depending on unbounded digits, unbounded words, or genuinely different real height variables has not been excluded. In particular the proof cannot fix a single positive ordinary approximant for all precision requests: it would have to equal $-1$ in the binary coordinate and $0$ in the ternary coordinate. A least ordinary counterexample, if one exists, can have a finite dense binary suffix and later admissible graph moves not present in this model. This is the precise failure of the attempted universal closure.

## Attempt to use two actually convergent cofactors

Suppose the least hypothetical bad $m$ is divisible by three. It is odd; write $m=2^a u-1=3^b v$, with exact valuations $a,b$ and $u$ odd. Both smaller cofactors converge by minimality. There is an exact dependence: $U(m/3)=u$. When $b=1$ this is $U(v)=u$. The proposed induction would carry a merger along the finite convergence itinerary of $v$ while retaining a path for $3v$. At an odd $v$ the synchronized commutation misses by **one**:
$$
 3T(v)-T(3v)=1.
$$
The trajectories of the two cofactors already meeting does not remove that difference.

This failure can be tested with **genuinely terminating** cofactors in at most two odd steps. Let $m=5\,2^a-1$ and require $5\,2^a\equiv4\pmod{3^K}$, $K\ge2$. The order of $2$ modulo $3^K$ is $2\cdot3^{K-1}$: $v_3(4^{3^j}-1)=j+1$ follows by cubing from $4-1=3$, with the new quadratic factor of valuation one. Thus this congruence has arbitrarily large exponents, necessarily odd. These ordinary $m$ have exact $v_3(m)=1$, $v=(5\,2^a-1)/3$, and $U(v)=5$, $U(5)=1$. By taking $a,K$ arbitrarily large one approaches the paired input $(-1,3)$.

For this paired input the earlier two-clock proof applies with turning ternary coordinate $4(3/2)^t-1$. After $l\le\min(j,t)$ inverses it is at least $4(3/2)^{t-l}-1\ge3$. After $t$ inverses it is an ordinary integer as before. Every subsequent ordinary ancestor is still at least 3, since the only smaller positive integers 1 and 2 form a forward-closed set. Write $D\ge3$ for the final ternary coordinate and $z\le-1$ for the final binary one. The final affine map is $x\mapsto c(x-3)+D$ with $c=(D-z)/4\ge1$, so it cannot lower any $x\ge3$. Ordinary high-precision approximants therefore admit no smaller full-graph contact at bounded distance, even in this fixed-two-odd-step cofactor example. The ordinary witnesses depend on the distance. This does not exclude an unbounded-cost path using the actual exponent in the first step of $v$. We did not find such a lift of cofactor convergence.

## Finite binary digits on an individual ordinary orbit

**Written elementary theorem. Universal merger OPEN.** For the shortcut map, observe the odd checkpoints under $U(x)=(3x+1)/2^{v_2(3x+1)}$. Write $w(x)$ for the number of ones in the ordinary binary expansion. On every injective positive ordinary orbit, for every fixed $K$, the odd checkpoints satisfying $w(x)\le K$ have zero upper Banach density in the **odd-step clock**. This is uniform over the position of a long observation interval on that orbit. No assertion is made about shortcut-time density or cycles.

## A separated block retains its ordinary high digits

Let $t\ge3, J=2^{t-2}, G=2J+1, K\ge1$. If an odd $x\ge2^{KG}$ has at most $K$ ones, the differences between consecutive occupied bit positions cannot all be less than $G$: the first is at zero, and the largest position is at least $KG$. At a gap at least $G$, split $x=b+2^d u$, where $d$ is the upper occupied position, $u$ is positive odd, and $b$ is positive odd with $b<2^{d-G+1}$. Consequently $4^J b<2^d$.

Put $y_j=U^j(b)$ and let $A_j$ be the cumulative number of binary divisions through these $j$ odd steps. Since $3y+1\le4y$ for every positive $y$,
$$
 2^{A_j}y_j\le 4^j b<2^d\qquad(0\le j\le J).
$$
In particular $A_j<d$. The exact split on the **same** positive input is
$$
 U^j(x)=y_j+2^{d-A_j}3^j u.
$$
Indeed, after multiplying by three and adding one, divide by the exact power of two prescribed by the low trajectory. The high summand is still even after this division since $A_{j+1}<d$, and the low result is odd. Also $y_j<2^{d-A_j}$, so the two summands have disjoint occupied bits and their binary weights add. This uses the binary expansion of one ordinary integer. There is no random suffix.

## Counting the low-weight times

For $t\ge3$ the order of 3 modulo $2^t$ is $2^{t-2}$. Indeed $v_2(3^{2^k}-1)=k+2$ for $k\ge1$, starting with $3^2-1=8$ and factoring the next difference of squares (the second factor is 2 modulo 4). Odd powers of 3 are not 1 modulo 4, and taking an odd multiple of an exponent preserves the valuation of the difference from 1. Hence $3^j u\bmod 2^t$ is distinct for $0\le j<J$. The separated split bounds the number of observations $w(U^j(x))\le K$ in this block by
$$
 C(t,K)=\sum_{i=0}^{\min(K,t)}{t\choose i}.
$$
In particular taking $t=K+4$ guarantees some high-weight observation directly: the subgroup generated by 3 is precisely the residues 1 or 3 modulo 8 (inclusion and equal cardinality). Its coset by $u$ has a representative among $2^t-8,\ldots,2^t-1$, with at least $t-3>K$ ones.

An injective positive orbit eventually stays above the fixed threshold $2^{KG}$. In any length-$L$ odd-clock interval beyond this transient, take disjoint length-$J$ blocks greedily, each beginning at the first remaining low-weight state. Skipped positions are high-weight. A final partial block costs at most $J$. Thus the low-weight count is at most $LC(t,K)/J+J$. The finite initial transient adds a position-independent constant. Taking the supremum over interval positions, then the upper limit as $L\to\infty$, gives the upper density bound $C(t,K)/J$. With $K$ fixed, the numerator grows polynomially in $t$ whereas $J=2^{t-2}$. Letting $t$ increase proves the claim.

## A growing bound on blocks with distinct ordinary checkpoints

Let an interval have $N$ pairwise distinct odd checkpoints. Begin at the first remaining observation of weight at most $K$. If its value is below $2^{KG}$, charge that position individually and continue. Otherwise take a full block of length $J$ if available, or charge the final partial block. Each individually charged value occurs only once. Consequently the proportion of low-weight observations is at most
$$
 2^{KG}/N+C(t,K)/J+J/N .
$$
This finite inequality is uniform in the source and interval position. For each fixed $0<\alpha<1/2$, take $K=\lfloor\alpha\log_2\log_2 N\rfloor$ and $t=\lfloor\beta\log_2\log_2 N\rfloor$ with $2\alpha<\beta<1$. Then $KG=o(\log N)$ and $J=o(N)$. Also $C(t,K)/J$ is four times the probability that a uniform $t$-bit string has at most $K$ ones. Its mean weight is $t/2$, its variance is $t/4$, and $t/2-K$ grows linearly in $t$. Chebyshev's inequality therefore gives $C(t,K)/J=O(1/t)$. The displayed proportion tends to zero. This applies to every interval on an injective orbit and to a long primitive odd cycle traversed once. The binary string distribution here only counts residues of an actual high block. It imposes no distribution on the source.

## The failed inference at the component minimum

The orbit of a finite input can continually acquire binary digits from the odd multiplications. The argument proves that on an injective orbit the number of ones eventually exceeds every fixed bound outside a set of odd times of zero upper Banach density. It supplies neither an upper bound for that number from the source nor a smaller positive component member when it is large. A component minimum constrains the numerical sizes of *all* members from below; it imposes no known upper digit-weight bound along its forward tail. An eventual nontrivial cycle can have bounded digit weight. Thus neither possible kind of nonconvergence has been excluded. No external number-theoretic theorem is used.

## Check scope

[integer.lean](integer.lean) uses Lean 4.34.1 and Std. The declarations `Collatz.BinaryBoundary.transport` and `Collatz.BinaryBoundary.divisionBudget` check the exact lift of an odd-step history and the cumulative-division bound. To apply the lift at clock $j$, take its high increment at the endpoint to be $2^{d-A_j}u$, which is even. Binary weight additivity, the group order, gap selection and the density argument are written proofs. [integer.py](integer.py) independently replays the exact identities and residue counts on 144 separated ordinary blocks with 3,024 total odd checkpoints.

The additional declarations `Collatz.MixedBoundary.negativeWall`, `expenditure` and `clearsDenominator` check the rational inverse inequalities and the exact powers-of-three denominator identity. Passage from paired local integrality to ordinary integers, unrestricted graph normalization, the finite-residue Bellman consequence, and the cofactor specialization are written arguments. The Python replay also enumerates complete ordinary graph balls of radii 8, 12, 16 and 20, respectively finding 74, 270, 904 and 2,877 distinct vertices with no lower vertex.
