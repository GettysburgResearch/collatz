# Sharp common clocks for tripling pairs and triples

Use the ordinary shortcut map \(T(2n)=n,\ T(2n+1)=3n+2\). All sources and targets below are positive integers. A ternary unit means an integer coprime to three and can be even. A clock counts applications of \(T\).

## Which families are covered?

| Starts | Targets at every clock from the threshold onward | Least universal clock | A target missed at every shorter clock |
|---|---|---:|---:|
| \(x,3x\) | Every ternary unit | 14 | 439 |
| \(x,3x,9x\) | Every ternary unit | 28 | 475963 |

In each row the base \(x\) can depend on the target. At clock 13, target 439 has 33 ordinary predecessors. At clock 27, target 475963 has 2,274. Neither predecessor set contains its requested multiplicative pattern. Any earlier meeting could be padded by doubling every starting value. A positive multiple of three has the unique predecessor \(2b\), and every predecessor at clock \(h\) is \(2^h b\). This rules out a common positive pair at such a target at every clock. The earlier 23-step threshold applies to the more restrictive base \(x=23+32t\). [Pair theorem](FreePairClock.lean) · [Triple theorem](FreeTripleClock.lean) · [Earlier progression](PairCover.md)

For the upper bounds, split the target into finite ternary residue classes. Suppose the representative is \(a\) at precision \(k\), and every arm \(3^r x_0\) reaches \(a\) at the same clock \(h\) with its odd count plus \(r\) equal to \(g\le k\). Replacing \(x_0\) by \(x_0+2^h3^{k-g}v\) sends every arm to \(a+3^kv\). The pair certificate uses 38 classes and the triple uses 1,072. Their maximum ternary precisions are five and nine. A separate inverse enumeration regenerates the certificates. The Lean kernel checks their ordinary forward paths and the induction covering every target. [Tree checker](TowerSectionTree.lean) · [Certificate data](TowerSectionData.lean) · [Independent replay](tower_section_replay.py)

There is an explicit convergent family with an exact first stopping time. For any \(t\ge0\), put
\[
x_t=955+2^{21}\frac{2^{1458t}-1}{2187}.
\]
All three odd starts \(x_t,3x_t,9x_t\) reach \(2^{7+1458t}\) together at clock 14, and all three first reach 1 at clock \(21+1458t\). The quotient is integral and every \(x_t\) is 955 modulo 16384. For \(t=0\), the three starts are 955, 2865 and 8595 and their common 14-step endpoint is 128. [Exact first-hit proof](SynchronousFirstHits.lean)

## Sharp height bounds for pairs

At fixed clock 14, every unit \(b\) admits a pair with \(27x\le16384b\). Allowing any common clock through 14 improves the bound to \(81x\le16384b\). Both multiplicative constants are optimal. On each row below the formula is attained and is a lower bound over every allowed start. [Upper bounds](FreePairClock.lean) · [Exact minima](FreePairHeight.lean)

| Clocks allowed | Target \(b\), \(t\ge0\) | Least possible \(x\) |
|---|---|---|
| Exactly 14 | \(556+3^{14}t\) | \((16384b-1216)/27\) |
| Any common clock through 14 | \(1093+3^{14}t\) | \((16384b-313)/81\) |

For the second progression, even the best pair can cost more than 202 times its target. This disproves descent by choosing the smaller member of a pair returned by this 14-step construction. [Complete inverse-ray enumeration](PairInverseRays.lean)

## Why the same obstructions occur in every ordinary component

Fix a clock \(h\), a list of positive multipliers containing 1, and a target progression \(a+3^h t\). Every ordinary predecessor is an affine ray \(p_0+p_1t\). Its intercept satisfies \(p_0\le 2^h a\). If \(C\) bounds the multipliers and \(t>C2^h a\), any equality between a scaled predecessor and another predecessor forces both their intercepts and their slopes to agree. Thus all simultaneous predecessors at that high target come from rays that work on the **entire** progression, down to \(t=0\). [Exact high-fiber theorem](StableTowerFibers.lean)

Consequently a missed unit target gives arbitrarily late misses along the sequence \(2^e u\) for **every fixed unit \(u\)**. Choose sufficiently large \(e\) putting \(2^e u\) in the missed ternary class. A simultaneous lift there would pull back to the missed target. In particular the sharp clocks 14 and 28 stay sharp even when the tests use only sufficiently large powers of two, all of which have known stopping times. Applegate and Lagarias studied the finite-depth trees of individual predecessors. Here it is essential that the same parameter works for several related predecessors. [Dyadic test and proof](StableTowerFibers.lean) · [Applegate and Lagarias, *The Distribution of 3x+1 Trees*](https://doi.org/10.1080/10586458.1995.10504321)

A common affine endpoint \(a+3^kt\), with \(3\nmid a\), on one class \(W+2^H t\) suffices for uniform routing to every unit at every sufficiently late clock. For each of the finitely many target residues choose a power of two taking its representative into the endpoint progression. Further lifts use the same exponent. Initial doublings of the source equalize the resulting clocks. Conversely, if \(x\) and \(mx\) can reach all unit targets at a single fixed clock, then \(m\) is a power of three. Indeed, on a fixed parity class distinct slopes separate once the parameter exceeds both intercepts. [Lean implications](UniformTowerRouting.lean)

Combined with the **written finite-list construction in PR 146**, this gives a classification for a finite multiplier list anchored at 1. Such a list can cover every unit target at one fixed clock exactly when every multiplier is a power of three. For sufficiency PR 146 constructs a common binary class with equal clocks and a common affine endpoint. Choosing \(W\) coprime to three in that class makes the anchor's endpoint a ternary unit. The uniform routing lemma then applies. The all-list construction is a source dependency of this written corollary. The sharp pair and triple proofs above have independent Lean certificates. Monks proved that every nonconstant positive arithmetic progression meets every ordinary merge component, with clocks allowed to vary. [PR 146, finite affine lists](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md) · [Kenneth M. Monks, *The Sufficiency of Arithmetic Progressions*](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf)

## Transferring predecessor counts to synchronized triples

There is a single injective map \(F\) on positive starts satisfying \(9F(n)\le2^{28}n\). Its three arms have a common endpoint at time 28. If \(T^h(n)=b\) for any unit \(b\), all three arms \(F(n),3F(n),9F(n)\) also reach \(b\) together by time \(28+h+6\). The analogous pair map satisfies \(F(n)\le16384n\) with initial common clock 14. The map is chosen before the target or the time. [Lean encoding theorem](SynchronousBasin.lean)

To construct it, first encode ordinary inputs injectively into ternary units. For \(n=2^k o\) divisible by three with \(o\) odd, replace \(o\) by \(4o+1\). Those odd parts reach \(T(o)\) two clocks apart. A unit target in the original orbit occurs after the multiple of three has taken its first odd step. The sibling therefore retains every such target. Use two distinguishable four-step inverse branches to keep the original unit inputs and these encoded multiples disjoint. At the resulting unit apply the simultaneous fixed-clock section. Its output determines that unit after exactly 28 steps, preserving injectivity. [Ordinary encoding, height and clock bounds](BasinUnitEncoding.lean)

For fixed unit \(b\), let \(\pi_b(X)\) count positive inputs up to \(X\) that visit \(b\). Let \(J_b(Y)\) count bases \(x\le Y\) for which the triple has a common endpoint at 28 and that endpoint later visits \(b\), allowing zero further steps. The injection gives
\[
\pi_b(X)\le J_b(\lfloor2^{28}X/9\rfloor),\qquad J_b(Y)\le\pi_b(Y).
\]
Thus these two counts have the same upper and lower polynomial growth exponents. The published Krasikov–Lagarias theorem yields \(J_b(Y)\gg_b Y^{0.84}\) for every sufficiently large \(Y\), including in any hypothetical nonconvergent basin. The exponent comes from their predecessor estimate. Our contribution here is the simultaneous transfer with bounded change of size. [Krasikov and Lagarias, *Bounds for the 3x+1 Problem Using Difference Inequalities*](https://arxiv.org/abs/math/0205002)

## The remaining finite-count assertion

For a stage \(X\), take the synchronized triples with \(1\le x\le\lfloor2^{28}X/9\rfloor\). Count a miss when their common 28-step endpoint fails to visit a chosen gate \(g\) within \(O\) further steps. Write the count as \(M(X,O,g)\). With the published predecessor bound as an explicit hypothesis, Lean proves that universal Collatz is equivalent to
\[
\forall N\ \exists X\ge N,\ O,\ g\qquad M(X,O,g)^{25}<X^{21}.
\]
Indeed, if convergence fails, one fixed bad unit target and target 1 have opposite convergence labels. At every large stage, one of their encoded predecessor sets has the opposite label from the proposed gate. Every member of that set misses. Conversely, under universal convergence, a common finite deadline for the finitely many starts at each stage gives zero misses at gate 1. The published analytic bound is supplied in the form of finite sets of distinct ordinary predecessors. Its original proof has not been ported into this packet. [Lean statement with its explicit input](SynchronousBasinCount.lean)

| Stage \(X\) | Bases examined | Synchronized triples | Misses at gate 1 by 2048 further steps | Largest first time from the common endpoint |
|---:|---:|---:|---:|---:|
| 1 | 29,826,161 | 1,395,738 | 0 | 333 |
| 2 | 59,652,323 | 2,792,116 | 0 | 364 |
| 4 | 119,304,647 | 5,585,854 | 0 | 381 |

At the last stage, \(x=118900443\) gives common endpoint 6355687 and attains 381. These are exhaustive computational checks at three finite stages. The assertion for arbitrarily large stages remains open. Tao's almost-bounded-value theorem uses logarithmic density and a growing threshold, which leaves this fixed-gate count undecided. [Finite replay](synchronous_basin_replay.mjs) · [Tao, *Almost all orbits of the Collatz map attain almost bounded values*](https://arxiv.org/abs/1909.03562)

## Positive density from the 2026 predecessor theorem

Mazur's September 2026 manuscript proves positive lower natural density of the full-map predecessors of each fixed positive target coprime to three. Its companion formalization uses the unaccelerated odd step \(n\mapsto3n+1\). Skipping the intermediate even value preserves every visit to an odd target. For an even unit \(b\), choose \(j\in\{1,2,3,4\}\) with \(2^jb\equiv4\) or \(7\pmod9\), which is possible for each of the six unit residues. Then \((2^jb-1)/3\) is an odd unit reaching \(b\) in \(j\) shortcut steps. The positive-density lower bound therefore transfers to every unit target and, by our injective encoding, to its synchronized triples. The theorem `positive_triple_density` checks this for every large bound on the triple base itself, including even targets. The density constant can depend on the target. [Lean proof of density transfer](SynchronousDensityTransfer.lean) · [Mazur, Theorem 1.1](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) · [Source supplement and audit](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html)

With the integer reciprocal form of Mazur's bound as an explicit input, Lean proves the stronger finite test
\[
  \mathrm{Universal}\quad\Longleftrightarrow\quad
  \forall D,N\;\exists X\ge N,\ O,\ g\quad D\,M(X,O,g)<X.
\]
Thus the fraction of misses needs to become arbitrarily small along selected stages. The same deadline and gate must work for the whole stage. A hypothetical bad component supplies a positive lower fraction of synchronized triples with the wrong label at every large stage, for any proposed gate. The new module checks the conversion for odd targets and the finite counting implication. The external positive-density development is a separate dependency. [Lean reduction and map conversion](SynchronousBasinDensity.lean)
