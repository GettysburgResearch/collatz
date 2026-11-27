# Fixed-gap coalescence at a prescribed clock

**PROPOSED, with fully Lean-checked first-hit pairs in every sufficiently large relative interval. Collatz remains open.** Let $T$ be the shortcut map, halving even inputs and taking odd $n$ to $(3n+1)/2$. Write $O_D(n)$ for the number of odd departures in its first $D$ steps.

The [first-arrival construction](FirstArrival.lean) also makes every sufficiently large supplied clock the *first* visit to the target for both sources, including periodic targets. Combining it with the ordinary inverse phase ladder places such a pair entirely inside every sufficiently large interval $[X,(1+\delta)X]$, with a common first clock at most $\log_2(X/y)+O_{d,s,\delta}(1)$. [FastPairs.lean](FastPairs.lean) proves the pair assertion with no extra hypotheses. The marked placement theorem also prescribes simultaneous congruences on time and odd count. [First-hit pairs in every relative interval](FAST_FIRST_HIT_PAIRS.md)

The [finite-family theorem](FINITE_BLOCKS.md) extends the all-clock first-arrival conclusion to every prescribed finite list of offsets and every initial binary cylinder. [BlockClock.lean](BlockClock.lean) proves the mixed binary and ternary endpoint claim; [MarkedProgressions.lean](MarkedProgressions.lean) places the full pattern in every source residue of any supplied positive modulus with a shared marked first clock and grade. The [fixed-prefix coprime steering construction](COPRIME_STEERING.md) gives a separate written route. The [near-minimum-time counting theorem](FAST_COUNTING.md) quantifies the number of distinct disjoint first-hit patterns in a single window.

The [affine classification](AFFINE_WINDOWS.md) extends the placement theorem to finite systems $a_it+b_i$. Its necessary and sufficient condition is equality of the prime-to-six parts of all positive slopes. [AffineClassification.lean](AffineClassification.lean) proves the equivalence for the complete marked all-window property. PR146 established the underlying fixed-cylinder classification.

A [quantitative growing-block corollary](GROWING_WINDOWS.md) tracks the cost using PR146’s stated logarithmic-square prefix bound. The [same-basin minimum theorem](INVERSE_ROOTS.md) supplies arbitrarily high odd-unit roots in each individual target basin at which every actual odd-unit predecessor has noncontracting inverse charge.

## A fixed separation, endpoint, source residue and clock

For every $d,s\ge 0$, there are natural numbers $B,g$ depending only on $d,s$ such that for **every** $D\ge B$, every natural $y$ prime to three and every residue $c\bmod 3^s$, there exists an ordinary positive $x\equiv c\bmod 3^s$ satisfying

$$
 T^D x=T^D(x+d)=y,\qquad O_D(x)=O_D(x+d)=g.
$$

The target may be even. The same $g$ works for all these clocks, targets and residues. One may take

$$
 B\le 18\cdot 3^s\max(1,d-1)^4+2d+3.
$$

[FixedGapClock.lean](FixedGapClock.lean) proves the quantified statement as `cover_bound`. The first source depends on the requested data. The theorem gives no common $x$ over all clocks.

## Two genuine odd departures suffice at the terminal end

Suppose that $D\ge 6\cdot3^s+1$ and $3\nmid y$. For every $c\bmod3^s$ there exist a positive odd $x\equiv c\bmod3^s$ and $1\le e\le 6\cdot3^s$ with

$$
             9x+3+2^e=2^D y.
$$

To find $e$, take the complete period of powers of two modulo $3^{s+2}$ and match $2^Dy-3-9c$. This residue is a unit. Writing $f=D-e>0$, the resulting identity gives a positive odd intermediate $u$ with $3x+1=2^e u$ and $3u+1=2^f y$. Thus these two gaps give exactly $D$ ordinary shortcut steps and exactly two odd departures. When $y$ is even, the final gap gives the stated shortcut arrival at $y$. The last division could continue after that arrival. [TwoGapRouting.lean](TwoGapRouting.lean)

The threshold is sharp uniformly for two such gaps. Put $P=6\cdot3^s$. For $D\le P$, choose the odd unit $y=2^{P+2-D}+3^{s+2}$ and prescribe $c=0$. A split of the displayed equation would require $2^e\equiv1\bmod 3^{s+2}$. The exact order $P$ forces $P\mid e$, contrary to $0<e<D\le P$. The lower bound concerns the two-gap architecture. Allowing more odd departures can lower the routing budget substantially. [SharpClock.lean](SharpClock.lean)

## How the two sources join

When $d=1$, the starts $8t+4$ and $8t+5$ both reach $3t+2$ after three steps and one odd departure. For $d=2q>0$, use even starts $2t,2t+d$ and halve both. For $d>1$ odd, the following two-step moves each use one odd departure on each arm.

| Original gap | Lower start | Lower endpoint | New gap |
| --- | --- | --- | --- |
| $4q+1$ | $4t+1$ | $3t+1$ | $3q+1$ |
| $4q+3$ | $4t+2$ | $3t+2$ | $3q+2$ |

These are the counted gap reductions used in the coalescing-digit literature. To retain the input class, choose $t_0\bmod3^s$ so the displayed lower start has the required residue. Prescribe the next lower source modulo $3^{s+1}$ as $3t_0+j$ with the table's offset $j$. Any ordinary lift decodes as $3t+j$ with $t\equiv t_0\bmod3^s$. A halving needs no extra trit. Each recursion strictly decreases the positive gap. The estimate $4(d'-1)\le3(d-1)$ for the odd moves pays for the extra trit because $3(3/4)^4<1$. The last two odd departures provide the requested target and absorb the remaining clock exactly.

## What happens at a specified ordinary source

All ordinary paths obey $2^D T^D(x)\le 4^{O_D(x)}x$. Hence our fixed-grade family has $x\ge 2^D y/4^g$. The increasingly late witnesses necessarily tend to infinity for each supplied $y$. In particular, closing larger and larger ternary precisions by an increasingly delayed, fixed-grade route cannot identify a bounded source using clock growth alone. There is also a concrete obstruction to demanding synchronous fusion of every supplied adjacent pair. The sources 1 and 2 reach 1 in opposite clock phases and never agree at a common clock. Both statements have direct ordinary Lean proofs. [SharpClock.lean](SharpClock.lean)

The remaining fixed-source problem is to find a genuine smaller coalescing source for each outstanding ordinary start, allowing independent physical clocks. Neither growing the prescribed precision nor the existence of a coalescing pair elsewhere in every class supplies that descent.

## Prescribing both clocks

Write $a$ for the odd count in the fixed-gap certificate and keep its threshold $B$. For every extra odd count $r\ge0$, every clock $D\ge B+3r+3$, and every ternary-unit target $y$, there are positive twins with the same prescribed start class, target, and total odd count $a+r$. This unconditional extension uses an 18-row kernel-checked table. On an ordinary unit $y$, choose one inverse exponent $e$ with unit predecessor $z$ and

$$
e+V(z)\le 3+V(y).
$$

The values of $V$ on residues $1,2,4,5,7,8\bmod9$ are $1,0,1,2,3,0$. The choice of $e$ sees the residue of $y\bmod27$. Iteration gives the clock budget by cancellation. [ClockCone.lean](ClockCone.lean)

**SOURCE-QUALIFIED improvement.** Theorem D of paper 37/v4 states an analytic routing result for positive odd units with a common number $b$ of inverse gaps and total valuation exactly $2b$. Only precision two and target class $2\bmod9$ enter here. This paper theorem is an explicit premise named BalancedNine in Lean. Its analytic proof has not been independently reproduced in this packet. For any odd unit $y$, let $w\equiv2\bmod9$ be the routed ancestor. Then $z=(2w-1)/3$ is again odd and prime to three. Repeating the construction gives $q$ blocks, each using $b+1$ odd departures and $2b+1$ shortcut steps. For extra grade $r=q(b+1)+t$, $0\le t<b+1$, the exact supplied clock may therefore be **any**

$$
D\ge B+q(2b+1)+3t+3.
$$

The odd count on both actual arms is $a+r$. The asymptotic ratio $(2b+1)/(b+1)=2-1/(b+1)$ is strictly below two. The proof of this implication and the elementary cone are separate kernel theorems. [Paper 37/v4, Theorem D](https://rstation.ai/problems/collatz/papers/37) · [ClockCone.lean](ClockCone.lean)

## Why decreasing inverse height requires a different selection

An ordinary odd word with $g$ gaps of total $D$ gives $3^g x<2^D y$ from its start $x$ to its endpoint $y$ when $g>0$. The sufficient coefficient threshold for strict inverse height decrease is $D/g\le\log_2 3$, approximately $1.585$. An elementary obstruction to uniform decrease is the unit $7$. The set $\{0,1,2,3,4,5,6,8\}$ is forward-invariant. Every ordinary start hitting $7$ is at least $7$. In particular, every nonempty route ending at $7$ has $3^g<2^D$. The target $7$ itself reaches 1, so this obstruction applies even inside the known basin. [Threshold.lean](Threshold.lean)

The obstruction persists across moving large targets at the strictly higher clock-to-grade ratio $8/5$. At grade $5k$ and clock at most $8k$, a gap list has positive entries with sum at most $8k$. Its cumulative sums identify it with a size-$5k$ subset of $\{1,\ldots,8k\}$. The affine equation gives at most one possible terminal residue modulo $3^{5k}$ per word. Thus for $k\ge1$ the fraction of unit target classes covered is at most

$$
\frac{\binom{8k}{5k}}{2\cdot3^{5k-1}}
\le \frac32\left(\frac{8^8}{5^5\,3^8}\right)^k,\qquad
\frac{8^8}{5^5\,3^8}<0.819 .
$$

The endpoint-class bound is also checked directly on the ordinary shortcut map. Its proof adds initial halving steps to place earlier hits at the same deadline and injects the residue family into the subsets of odd-departure positions. [EndpointCount.lean](EndpointCount.lean)

The binomial estimate follows by retaining the $5k$-th term of $(5+3)^{8k}$. Every absent class admits arbitrarily large positive odd representatives. For other grades $g$, pad a word with exponent-one letters to the next multiple of five to obtain the same count bound up to an absolute factor after normalization. Summing the geometric tail excludes a uniform rule that repeatedly returns a unit predecessor at cost at most $8/5$ per gap with positive grade and a fixed upper bound on each returned grade. Its iterates would hit a finite grade band above every cutoff, whereas sufficiently large such bands miss entire unit classes. The counting argument allows the missed ordinary representatives to depend on the band. It leaves open whether a fixed source can see unusual endpoint classes indefinitely. [Threshold.lean](Threshold.lean)

An endpoint-wise twin lower bound supplies additional ancestors in that same component. A harmonic estimate capable of forcing descent would have to retain the supplied source or prove that an ancestor falls below its actual least-component floor. The routing calculation alone gives neither fact.

## Prior work and dependencies

- Said Duran obtains coalescing equal-count progressions for an arbitrary gap. Lemma 17 of rStation paper 64/v2 gives the short gap moves used above and also prescribes initial parity. The gap-reduction observation is prior work. [Primary preprint, Lemma 17 and attribution](https://rstation.ai/problems/collatz/papers/64/v2)
- PR202 at `3b10b24d12d4b349cb20f4cbc83086c8a09f807e` proves source-qualified results for much longer synchronized blocks at prescribed height scales. PR203 at `3f2c89f12b057b8bb8655bd6fc794c772aa8b65d` gives source-qualified positive lower relative densities in mixed cylinders and prescribed *residues* of first-hit clocks and grades. Those quantitative density and long-block claims have stronger inputs. Here the two source points have fixed separation and the target clock itself can be any sufficiently large integer while the odd count stays fixed. [PR202](https://github.com/GettysburgResearch/collatz/pull/202) · [PR203](https://github.com/GettysburgResearch/collatz/pull/203)
- PR200 at `eb91086951b66923787f696801f0c3ca52a0077d` uses a specific fixed-clock two-block modular router. This packet computes the uniform sharp threshold for two single-gap inverses at arbitrary ternary precision. Theorem D of rStation paper 37/v4 uses a growing number of branches and a common balanced budget, with much better precision dependence. The elementary fixed-gap theorem above needs no analytic routing or density input. [PR200 local rows](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/regularity-rigidity-20261124/refinement/LOCAL_FIBER_ROWS.md) · [Paper 37/v4](https://rstation.ai/problems/collatz/papers/37)
- [TernaryPowerLift.lean](TernaryPowerLift.lean) is byte-for-byte the module from PR197, `1f0f496fbea37792439feada6106eaaff596bcd1`. It supplies the ternary-period expansion and cofinal dyadic powers. [Pinned source](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/source-progress/TernaryPowerLift.lean)
