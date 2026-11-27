# A global canonical defect within (98304n)

For the positive ordinary shortcut $T(2u)=u$, $T(2u+1)=3u+2$, write $G(x)$ when some iterate equals one. Write $D(x)$ for $\neg G(x)\land G(3x)$. A canonical defect is a $y\equiv17\bmod48$ satisfying $D(y)$.

**Global theorem.** Every positive $n$ with $\neg G(n)$ forces a canonical defect $y\le98304n$. Hence if $z$ is the least canonical defect, then $G(n)$ holds for each positive $n$ with $98304n<z$. The coefficient is $24\cdot4096=3\cdot2^{15}<2^{17}$. This covers arbitrary orbits, including hypothetical escaping ones. The existence of a bad positive integer remains open. [Global theorem](OptimizedBank.lean)

The earlier 140-leaf return theorem gives $w\equiv1\bmod16$ with $D(w)$ and $w\le24n$. The new statement localizes **every** such ordered defect to a canonical $y\le4096w$. In the previous composition the corresponding second factor was $2^{23}$. [First-stage theorem](ReturnTwentyFour.lean) · [Earlier composition](GLOBAL_RETURN_BUDGET.md)

## A tree with a budget at its original input

Start at the full row $w=16t+1$, $t\ge0$. Each node keeps the original affine row and an ordered list of rows known to carry $D$. Binary and ternary nodes substitute $t=mu+i$ in all rows. Two physical exchanges from PR197 extend a history. At $48p+1$ both labels survive at $64p+1$. At $3p$ with $p$ odd, exactly one of $16p+1,32p+1$ carries the directed disagreement. The tree proves both possible conclusions, preserving the preceding ordered labels. Consequently alternative histories are not disjoint residue classes. [PR197 unit exchange](pr197-floor/UnitResidueExchange.lean) · [PR197 nonunit exchange](pr197-floor/NonunitExit.lean)

A leaf selects any retained defect $s$. It can discharge directly when $s\equiv17\bmod48$ and $s\le4096w$. Otherwise it gives a positive path from $s$ to $3s$. Its ordinary edges are $D$ (double), $E$ (halve an even), $O$ (ordinary odd shortcut), and $I$ (ordinary odd predecessor). The extra letter $M$ goes from $q=32v+11$ to $3q$. If the lower endpoint is bad and the upper endpoint good, at least one $M$ carries an actual bad-to-good change. When the word uses no $M$, the two initial labels already contradict ordinary invariance. Each possible charged $q$ normalizes to $y=(3q+1)/2=48v+17$: $T(q)=y$ and $T^5(3q)=T^4(3y)$. An affine charge $q=At+B$ against the original $w=at+b$ must satisfy
\[
                3A\le8192a,\qquad 3B+1\le8192b .
\]
These inequalities bound the actual positive canonical source at every $t\ge0$. [Generic Lean transport](DefectBank.lean)

| Checked property | Value |
|---|---:|
| Terminal assertions | 1156 |
| Direct canonical endpoints | 174 |
| Binary and ternary split nodes | 138 and 383 |
| Unit and two-alternative exchange nodes | 251 each |
| Distinct nonempty directed words | 344 |
| Charged positions counted over terminal words | 1713 |
| Longest terminal word | 192 letters |
| Maximum retained defects in one history | 11 |
| Maximum radix splits on one branch | 15 |

The path budget applies to the canonical source. The subsequent triple and intervening ordinary vertices have separate sizes. The following exact suprema range over the corresponding affine rows of this certificate, relative to the original $w$. For any fixed row the supremum is the larger of its ratio at $t=0$ and its limiting slope ratio.

| Physical object | Supremum relative to $w$ |
|---|---:|
| Returned canonical source | $71562209/18657$ |
| Triple of a returned canonical source | $71562209/6219$ |
| Source of an $M$ letter | $15902713/6219$ |
| Target of an $M$ letter | $15902713/2073$ |
| Vertices along the terminal words | $2083119305552/58929$ |
| Vertices in the ordinary mergers used for exchanges | $10347374580560/219537$ |

## Evidence and provenance

PR197 at `1f0f496fbea37792439feada6106eaaff596bcd1` supplies the ordered-defect exchanges, the original ten-step covering argument and motif library, the 11-modulo-32 directed transport, and its $2^{23}$ localization. The new search reconsidered each of 754 terminal histories in that argument, including direct exits. On 557 histories, selecting an earlier admissible row or using the prior motifs met the new bound. The remaining histories were discharged with new directed-path searches and mixed-radix subdivisions, producing 599 terminal assertions. The result uses 1156 explicit leaves and checks the complete tree directly. The first-stage factor 24 is the earlier certificate in this sweep. [Pinned dependencies and byte hashes](GLOBAL_RETURN_CONTROLS.json) · [Upstream quantitative return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QUANTITATIVE_RETURN.md)

Build `DefectBank` after `GlobalReturnBudget`, then `OptimizedBank`. The latter checks the literal finite plan in kernel-evaluated fragments and proves the local and global conclusions. [Independent checker](check_optimized_bank.py) · [Archived control](OPTIMIZED_BANK_CONTROLS.json)

The independent checker parses the named fragments, reconstructs every physical path and every branch from the full initial progression, and evaluates the ordinary mergers on complete affine rows. At each physical rule it tests both $t=0$ and $t=1$, which checks the constant and slope when combined with the residue guards. It computes the displayed suprema and compares its output against the archived JSON in both normal and optimized Python.
