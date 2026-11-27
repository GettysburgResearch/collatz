# Simultaneous descent and mergers on ternary towers

Write $T$ for the shortcut Collatz map and let $w$ be a positive odd integer. All clocks below count shortcut steps.

## A common endpoint at 513 consecutive ranks

For every $w$ and every starting exponent $s$, there is an offset $0\le d\le2^{1379}$ and a positive integer $y<3^{s+d}w$ such that
$$
T^{1381}(3^{s+d+r}w)=y\qquad(0\le r\le512).
$$
The source and endpoint in each equality are ordinary integers. The offset and endpoint are the same for all 513 ranks. Consequently every interval of $2^{1379}+512$ exponents contains at least 512 adjacent rank pairs merged by clock 1,381. This supplies an unconditional positive lower density of such pairs on every fixed odd tower. [Lean theorem `recurring_common_endpoint`](TowerFrontierMergers.lean)

The two starting representatives are congruent to 1 and 5 modulo 8. At clock 1,381 all 513 rows over the first representative have the same endpoint and the same total exponent $r+p=660$, where $p$ counts odd inputs. The corresponding exponent at the second representative is 657. Adding $2^{1381}t$ to either representative adds $3^{r+p}t$ to every endpoint in its block. The equality and the strict bound below the first base therefore hold throughout both residue classes. Multiplication by 3 first takes either of the two remaining odd residues modulo 8 into one of these classes modulo 8. Successive powers of 3 then realize every required higher binary digit, giving the offset bound. [Rotation proof](TowerFrontierRotation.lean) · [Affine transport](TowerFrontierAffine.lean)

## A fixed clock with 537 descending ranks

There is an explicit odd representative $W$ such that for every $t\ge0$, taking $w=W+2^{1024}t$ gives
$$
T^{1024}(3^r w)<w\qquad(0\le r\le536).
$$
For the representative, the endpoint is below $W$ and $r+p\le643$ at each rank. Since $3^{643}<2^{1024}$, affine transport preserves the strict inequality at every lift. More precisely, for every $a\equiv1$ or $5\pmod6$ there is $i<2^{1023}$ such that $w=a+6i$ satisfies all 537 inequalities. The result specifies one residue class modulo $2^{1024}$. PR 209 proves a positive percentage on every eligible progression for its shorter 116-rank window. [Lean theorem `tower_descent`](TowerFrontier.lean) · [PR 209 at its reviewed revision](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/fixed_source/README.md)

The two numerical proofs use eight-clock blocks. Lean checks all 256 low-byte table entries against the ordinary step recursion, proves that the block evaluator computes the ordinary endpoint and odd count, and verifies the finite rank ranges by kernel reduction. The integer representatives are inputs to these checks. [Evaluator and transport proof](TowerFrontierAffine.lean)

## Arbitrary finite block lengths from the affine-list construction

The deterministic finite-list construction in PR 146 gives a written extension to every prescribed $R$. Apply it to the slopes $1,3,\ldots,3^R$ in each of the initial binary classes $1,5\bmod 8$. All slopes have the same factor after removing twos and threes. Their initial powers of two are equal, so the constructed clocks agree across each list. Choose the larger of the two resulting clocks $m$ and continue the shorter merger to $m$, fixing extra digits as needed. On each final class the common endpoint is $C+S t$ with $S$ odd. Fix the next $m+1$ digits of $t$ to make this endpoint divisible by $2^{m+1}$. Every positive lift then performs $m+1$ halvings. Since $T(x)\le2x$ for positive $x$, its common endpoint at $2m+1$ is at most $2^m x/2^{m+1}<x$, where $x$ is the first starting value. The rotation argument reaches one of these two final classes on every odd tower, beyond every prescribed starting phase. This gives an $R$-dependent common clock and bounded phase offset without the probability estimate in the next section. The affine-list construction used here is a written result in the source. The numerical case $R=512$ above is independently checked in Lean with explicit constants. [PR 146 finite-list classification](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md#classification-and-a-constructive-bound) · [Constructive pair reductions](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/PREFIX_COMPRESSION.md)

## A conditional density estimate on each fixed tower

Assume the finite upper estimate (1) in PR 146. For any positive odd $w$, any interval of $L\ge8$ consecutive nonnegative starting exponents, and $R\ge1$, set $h=\lfloor\log_2 L\rfloor$. Apart from a fraction
$$
O\!\left(\frac{R}{\sqrt h}+\frac{h}{L}\right),
$$
each starting exponent $k$ in the interval satisfies
$$
T^h(3^kw)=T^h(3^{k+1}w)=\cdots=T^h(3^{k+R}w)<3^kw .
$$
The implied constant is uniform in the interval, $w$, and $R$. For fixed $R$, or for $R=o(\sqrt{\log L})$, the exceptional fraction tends to zero. Taking $h$ to be a sufficiently large constant times $R^2$ gives a successful block at that clock within $2^{O(R^2)}$ starting ranks. This is a written implication from the proposed estimate. The 513-rank and 537-rank numerical theorems above have independent kernel proofs. [PR 146 finite upper estimate, equation (1)](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_CLOCKS.md) · [PR 146 proposed derivation](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

Take $h\ge3$. In a complete high block of $2^h$ starts, (1) at multiplier 3 gives at most $C2^h/\sqrt h$ failures to merge by $h$. At starts above $6^h$, the affine offset bound in PR 146 forces every merger through that deadline to have equal clock, slope, and offset. Hence any successful residue gives a same-clock equality at $h$ on every positive lift. In any $L$ consecutive ranks, the sequence $3^kw\bmod2^h$ has period $P=2^{h-2}$ and visits each residue in its coset once per period. Indeed $v_2(3^{2^j}-1)=j+2$ for $j\ge1$. Each residue therefore occurs at most $\lceil L/P\rceil\le 5L/2^h$ times. Apply this multiplicity bound to the failure residues for each of the $R$ adjacent edges. If all edges merge by $h$, continuing each equality to $h$ gives a single endpoint for the entire block. No independence between edges is assumed. [Affine offset bound and binary coding](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_CLOCKS.md)

For the strict descent, discard starting ranks with $n=3^kw\le6^h$. There are at most $1+h\log_3 6$ of them in any interval. Across all $2^h$ start residues, every length-$h$ parity word occurs once. Thus the proportion with more than $3h/5$ odd inputs is at most $\exp(-h/50)$ by the fair-binomial upper tail. The same multiplicity bound transfers this estimate to ranks. In the remaining cases $2^hT^h(n)\le3^p(n+2^h)\le2\cdot3^{3h/5}n<2^h n$ for all sufficiently large $h$. Enlarging the absolute constant covers the finite initial clocks. For $R=1$, the permanently unmerged adjacent ranks on **each** odd tower consequently have zero upper Banach density. This quantifier concerns intervals of exponents at a single base. PR 146's corresponding written theorem concerns intervals of consecutive input integers. A zero-density set can contain the one least bad rank required by the descent argument. [Binomial parity coding and affine upper bound](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/fixed_source/README.md)

## The prescribed rank

The least-bad-rank argument needs the failing rank to reach the basin of a smaller base or a known good rank. The 513-rank theorem controls a segment whose position depends on the supplied base and phase. Its common endpoint lies below the first base of that segment. That upper bound can exceed the original $w$.

For every deadline $H$ and lower size $L$, some $w>L$ with $w\equiv5\pmod6$ has two properties through every clock $k\le H$. Both trajectories from $w$ and $3w$ remain at or above $w$, and their endpoints are distinct at each equal clock. Taking $w=24\cdot2^H(L+1)-1$ gives the construction. The adjacent source $3w$ starts with one odd step and two even steps, then follows the increasing odd branch for the rest of the deadline. Universal convergence and source-dependent capture of every least bad exponent remain open. [Lean theorem `fixed_rank_obstruction`](TowerFrontierLimit.lean)

More generally, prescribe *any* lower rank $r$. For every $H,L$ there exists $w>L$ with $w\equiv1\pmod6$ for which, throughout **independently chosen** clocks $i,j\le H$,
$$
3^rw\le T^i(3^rw),\qquad 3^rw<T^j(3^{r+1}w),\qquad
T^i(3^rw)\ne T^j(3^{r+1}w).
$$
The two finite orbit segments are disjoint. PR 146 already describes the late-merger pattern for the pair $n,3n$ when $n=2^kt-1$. Here a binary and ternary congruence places that pattern at every prescribed rank on arbitrarily large eligible bases. Lean proves independent-clock separation and both lower bounds. [Lean theorem `prescribed_rank_obstruction`](TowerFrontierPrescribed.lean) · [Earlier late-merger construction](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_CLOCKS.md)
