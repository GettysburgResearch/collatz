# Physical parity echoes and the scope of a divisibility argument

The shortcut map takes $x$ to $x/2$ when $x$ is even and to $(3x+1)/2$ when $x$ is odd. The accompanying Lean development proves a return criterion for one positive integer, an exact rank-one identity on a physical parity cylinder, and a growth theorem for a restricted family of parity words. The all-shifts obstruction below has a paper proof pending independent review. The project-wide fixed-source question remains open.

## What transfers from the GRH proof

On 20 November 2026 Levent Alpöge released a formalization with Claude of RH and GRH for every Dirichlet character of every positive modulus. His note describes an adaptation of Stepanov's argument in which a chain of theta lifts accumulates divisibility for a weighted von Mangoldt sum. The suggested chain length is of order $\sqrt X$ at summation length $X$. [Author's announcement and archive links](https://alpo.ge/remark.pdf)

Andrew Sutherland's 24 November verification records a sandboxed rebuild of 175,187 modules with Lean and Mathlib 4.33.1, kernel replay, acceptance of the exported proof by two independent checkers, and an axiom audit. The critical-strip statement uses Mathlib's Dirichlet $L$-functions and all characters. Michael Rubinstein independently reports a rebuild, replay and independent-kernel check. His explanatory draft states thirteen inputs for its main weighted-sum inequality. The MIT challenge contains no estimate for a prescribed Collatz itinerary. [MIT verification and precise statements](https://math.mit.edu/~drew/grh/) · [Waterloo verification and exposition](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)

## Exact divisibility at every cut

Fix an ordinary seed $x$, a length $L$, and a cut $0\le j\le L$. Write $q_j$ for the odd-step count before $j$ on the physical orbit from $x$. Among seeds at least $x$, those sharing its next $L$ parity bits are exactly $x+2^Lk$ for integers $k\ge0$. At every cut,

$$
 T^j(x+2^Lk)-T^j(x)=m_j k,\qquad m_j=2^{L-j}3^{q_j}.
$$

Matching first parities allows cancellation of the even denominator and, on the odd branch, cancellation of 3 modulo a power of 2. Induction gives the cylinder congruence. Forward iteration scales an initial difference by $3/2$ at each common odd step and $1/2$ at each common even step. These statements appear in Lean as `physical_ray` and `cut_value`.

The pair with $k=1$ attains *exactly* $m_j$ at every cut simultaneously. If two rows correspond to cuts and two columns to source displacements, the centered matrix has determinant zero. Every row is an integer multiple of the same row of source quotients. For increasing quotients $k_1,\ldots,k_s$, the Vandermonde product at cut $j$ equals $m_j^{\binom{s}{2}}\prod_{a<b}(k_b-k_a)$ by the pairwise equality. Counting the normalized divisibility at successive cuts as independent gains double-counts the source quotients. Lean proves the sharp divisor and rank-one statements as `sharp_simultaneously` and `rank_one_cuts`. The Vandermonde identity follows on paper by multiplying the differences.

For integer height caps $H_j$, all cuts satisfy $T^j(x+2^Lk)\le H_j$ exactly when each base height fits and

$$
 k\le \min_{0\le j\le L}\left\lfloor\frac{H_j-T^j(x)}{m_j}\right\rfloor .
$$

The number of ray points satisfying all caps is therefore the minimum plus one when the base fits and zero otherwise. `window_caps` proves the equivalent conjunction in Lean. A determinant argument using these affine rows needs an additional independent quantity to obtain higher rank.

## A return criterion for one ordinary seed

Suppose the $h$ bits at positions $0$ and $d>0$ agree. Then $T^d(x)\equiv x\pmod{2^h}$. Also $2(T(y)+1)\le3(y+1)$, hence $2^d(T^d(x)+1)\le3^d(x+1)$. It follows that

$$
 3^d(x+1)<2^{d+h} \quad\Longrightarrow\quad T^d(x)=x.
$$

Both states lie below $2^h$ under the hypothesis. In particular, a square prefix of half-length $d$ gives a genuine return once $3^d(x+1)<4^d$. Arbitrarily long square prefixes from the same ordinary seed force a period. Lean proves this as `periodic_of_cofinal_squares`.

Every Sturmian word has arbitrarily long square prefixes and is aperiodic. Therefore no ordinary shortcut orbit has a Sturmian parity tail, at any irrational slope or intercept. The arithmetic implication is formalized here. The word-combinatorial theorem is an external dependency. Prefix powers and factor complexity have prior literature, including earlier Lean work. [Dubickas, *Squares and cubes in Sturmian sequences*](https://archive.numdam.org/articles/10.1051/ita/2009005/) · [Prior Lean prefix-power results](https://github.com/msharpe248/collatz) · [Recent factor-complexity manuscript](https://rstation.ai/problems/collatz/papers/173)

## Can every runaway symbolic word be forced into such a return?

A symbolic word can pass all of these size tests, even when one evaluates its exact real affine heights at all pairs of positions. The remaining arithmetic question is whether the prescribed branches are integral at every time for a single fixed positive seed.

Let $w=11b_0\,11b_1\,11b_2\cdots$, with independent fair bits $b_i$. Every nonempty prefix is coefficient-supercritical. Each full triple contributes a multiplicative slope at least $9/8$, and an incomplete final triple of a prefix contributes only odd steps. For an integer $N\ge 2^{125}$ let $z_0=N$, and iterate the real affine maps $z\mapsto z/2$ and $z\mapsto (3z+1)/2$ according to $w$. These rational heights are defined even when a demanded branch disagrees with the true parity of the current state.

**Simultaneous obstruction (paper proof).** There is a positive-measure set of such words, independent of $N$, for which the following holds for *every* $N\ge2^{125}$. For every $t\ge0,d\ge1$, whenever the two length-$h$ windows starting at $t,t+d$ agree,

$$
 2^h\le |z_{t+d}-z_t|.
$$

Thus the magnitude test for a nonzero multiple of the parity modulus passes at every shift and lag. This conclusion concerns the exact real difference in the prescribed dynamics. Congruence of these rational values remains a distinct condition.

**Short echoes.** For fixed $t,d,h$, window agreement has probability at most $2^{-\lfloor h/3\rfloor}$. If $3\nmid d$, every free bit in the first window must match a forced 1 in the second. If $3\mid d$, the equality constraints among free bits form a forest. Each edge joins one index to its translate by $d/3>0$, so vertices lie on paths within residue classes modulo $d/3$. A forest of $e$ distinct edges of fair independent bits has probability $2^{-e}$ of satisfying all equalities. The first window supplies at least $\lfloor h/3\rfloor$ such edges, including when the windows overlap.

Take $H_{t,d}=\lceil72+(t+d)/24\rceil$. The probability that *some* pair agrees through $H_{t,d}$ is bounded above by

$$
 2^{1-72/3}\sum_{t\ge0,d\ge1}2^{-(t+d)/72}<2^{-7}.
$$

Indeed $r=2^{-1/72}<255/256$ by $(1-1/256)^{72}\ge1-72/256>1/2$, and the double sum is $r/(1-r)^2<256^2$. Outside this event every match has $h<H_{t,d}$. The same property rules out eventual periodicity by comparing two complete equal tails.

**Large exact displacement.** Every prefix from zero satisfies $z_s\ge N(9/8)^{\lfloor s/3\rfloor}\ge N2^{s/24-1}$, since $(9/8)^8>2$. In fact $z_s\ge N$. On a window starting at any phase, each group of three letters contains at least two ones. At most two remaining letters contribute a factor at least $1/2$, because there are no adjacent zeros. Thus its slope $C$ is at least $\tfrac12(9/8)^{\lfloor d/3\rfloor}$. If $d\ge48$ then $C\ge2$, so $z_{t+d}-z_t\ge z_{t+d}/2$.

For $1\le d<48$ write $z_{t+d}=Cz_t+E$. The slope $C=3^q/2^d$ differs from one by at least $2^{-47}$. The nonnegative correction $E$ is less than $2^{48}$ by iterating the maximum affine branch from zero. Hence

$$
 |z_{t+d}-z_t| \ge 2^{-47}z_t-2^{48}\ge2^{-48}z_t
 \ge N2^{(t+d)/24-51}.
$$

The long-window estimate also implies the final lower bound. At $N\ge2^{125}$ it exceeds $2^{H_{t,d}}$. Combining with short echoes proves the claim at all shifts, simultaneously for all these nominal seeds.

Every finite prefix has arbitrarily large ordinary realizers by the parity-cylinder bijection, so $N$ can additionally match any prescribed finite prefix of a selected word. As the prefix length increases the chosen ordinary $N$ may change. There are countably many ordinary seeds and the free-bit law is non-atomic. Almost every word in the positive-measure family therefore has no positive ordinary seed at all.

## The restricted fixed-source question

At an actual block boundary write $x=4y-1$, $y\ge1$. Continuing the mask to the next boundary requires precisely $y\equiv0,7\pmod8$. The two new values of $y$ are

$$
 F(8k)=27k\quad(k\ge1),\qquad F(8k+7)=9k+8\quad(k\ge0).
$$

Lean proves these exact branch statements and proves $x+K\le T^{3K}(x)$ whenever every block start is $3\pmod4$. An integer $y>0$ whose trajectory remains forever in this partial map's domain would give an ordinary unbounded Collatz trajectory. The probabilistic construction supplies symbolic itineraries. Conversely, excluding every positive integer in this restricted domain would close only this mask. The fixed-source condition $v_2(3^{q_L}N+A_{w,L})\ge L$ at unbounded lengths with the very same $N$ remains open.

## Replay

`PhysicalEcho.lean` was checked with Lean 4.34.1 (commit `5045d0056413266e57c625dcd7c365b10e377c52`) and Mathlib at `d13f23b723b8a846827a245b89c10fc7d3f11612`, with warnings treated as errors and implicit free variables disabled. Within a Lake project with this Mathlib version run `lake env lean -DautoImplicit=false -DwarningAsError=true PhysicalEcho.lean`. The printed dependency audits for the main arithmetic statements contain only subsets of `propext`, `Classical.choice` and `Quot.sound`. The probabilistic construction and the use of Dubickas's result are paper deductions. The build uses Mathlib and the local definitions.
