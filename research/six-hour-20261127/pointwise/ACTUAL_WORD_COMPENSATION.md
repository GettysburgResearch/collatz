# Compensating an actual block word at the same physical terminal

**Status.** Exact ordinary-word criterion, two positive families, a reverse-decoding obstruction, and an all-clock obstruction for odd competitors. No universal merger selector is obtained. Use the ordinary shortcut map \(T(2v)=v,\ T(2v+1)=3v+2\). Block labels are \((t,b)\) for \(t\) consecutive odd departures followed by \(b\) even departures to an odd landing. A finite word of such blocks is complete when its terminal is odd.

## Exact test for the supplied source

Let \(w\) be the actual parity word through a fixed clock on a supplied source \(x=3s\), with endpoint \(z\), length \(H\), and odd count \(p\). For a parity word \(v=(b_0,\ldots,b_{H-1})\), set
\[
 N(v)=\sum_{i:b_i=1} 2^i 3^{\#\{j>i:b_j=1\}}.
\]
For positive integer endpoints \(y,z\), \(v\) is the physical word from \(y\) to \(z\) exactly when \(2^H z=3^{p(v)}y+N(v)\). For the reverse implication reduce modulo two to recover the first input parity, divide out its known step, and continue. This induction also works for nonnegative inputs. If the terminal is odd, the prescribed interior parity bits and final parity certify all complete block boundaries.

Fix **any** competing family of words of the same length and odd count; this can be all permutations of the complete blocks of \(w\). There is a competitor in this family from a strictly smaller positive triple if and only if one of its carries belongs to
\[
     \big(N(w),\,N(w)+3^p x\big)
                 \ \cap\ \big(N(w)+3^{p+1}\mathbb Z\big).             \tag{1}
\]
In fact \(y=x-(N(v)-N(w))/3^p\). In a family beginning with an odd departure, such a competitor is odd as well. The upper bound in (1) enforces strict positivity; one cannot merely maximize the carry with no size test. The hypotheses use the actual source and its actual word. No alternative terminal or source bits are chosen for the upper arm. This is a finite certificate at each supplied prefix, not a guarantee of eventual success.

For comparison, [Weaver, Paper 124, Lemma 3 and section 3](https://rstation.ai/problems/collatz/papers/124/v1) uses the same fixed-clock numerator relation, choosing a *smaller* numerator in its \(3^p\)-class to construct a larger sibling of a typical stopped prefix. Here the comparator must be smaller, positive and divisible by three, and the family may be restricted to a specific block multiset. Haar coalescence and density-one bounds for unrestricted companions do not prove that (1) holds on a fixed exceptional ordinary source.

## Protected positive examples

The adjacent-swap exclusion at PR200 head ad70a3b831867cb8a74d402a2a1abdc419f5a09b permits any common prefix but excludes a single adjacent transposition while the upper path stays above the threefold shifted floor. Here the same input parameter is used on both arms in each row. A larger permutation can succeed even when the entire upper path rises above its own starting height.

| Blocks | Supplied upper \(x\) | Smaller triple | Common odd terminal | Shortcut clock | Odd departures |
|---|---:|---:|---:|---:|---:|
| Six | \(12{,}977{,}607+25{,}165{,}824k\) | \(x-6\) | \(4{,}933{,}001+9{,}565{,}938k\) | 22 | 13 |
| Nine | \(73{,}870{,}594{,}215+103{,}079{,}215{,}104k\) | \(x-6\) | \(404{,}800{,}088{,}233+564{,}859{,}072{,}962k\) | 34 | 23 |

Here \(k\) is every nonnegative integer. The respective upper and lower orders are
\[
\begin{array}{ll}
6:\quad &(3,1),(1,1),(1,1),(1,2),(4,2),(3,2),\\
        &(1,1),(1,1),(1,2),(3,2),(3,1),(4,2);\\[2pt]
9:\quad &(3,1),(2,1),(5,1),(1,1),(1,1),(1,1),(1,2),(5,2),(4,1),\\
        &(1,1),(1,1),(2,1),(3,1),(1,2),(1,1),(5,2),(4,1),(5,1).
\end{array}
\]
The shifted carries (affine numerators on \(Y=x+1\)) are \(11{,}101{,}224,\ 20{,}667{,}162\) in the first row and \(198{,}137{,}716{,}424,\ 762{,}996{,}789{,}386\) in the second. Their differences are respectively \(6\cdot3^{13}\) and \(6\cdot3^{23}\). Shifting adds the same constant \(2^H-3^p\) to each unshifted carry, preserving (1). The six-block upper path satisfies \(3(T^i x+1)\ge x+1\) at every clock through 22. The nine-block upper path satisfies \(T^i x>x\) at **every** clock \(1\le i\le34\). Each can be checked by exact affine parity lifting; for the latter every nonempty prefix has \(3^{p_i}>2^i\). Since \(x-6=3(s-2)\), each row discharges this entire progression from consideration as the least bad triple, irrespective of whether the smaller input has been individually tested. These two input progressions do not cover all remaining candidates. The first row already dips below the stronger independent PR192 good interval on its upper arm; the second stays above the original upper input until the exhibited merger. No claim of a first-ever or uniquely available cheaper witness is made.

## Unordered protected languages with no permutation competitor at any depth

For a block \((t,b)\) ending at odd \(z\), the entrance \(v\) satisfies
\[
                  2^b z+1=3^t(v+1)/2^t .
\]
Hence the terminal lies in the ternary ball \(z=-2^{-b}\bmod3^t\). If these balls are pairwise disjoint on a dictionary, an endpoint determines the last block's label. Its affine inverse is single-valued. Inducting backwards shows that two dictionary words with the same number of blocks and same terminal must coincide in every label and have the same entrance. For different word lengths, the shorter is necessarily a suffix of the longer. The condition is sufficient, without a bound on word length or on supplied positive entrances. Two balls are disjoint exactly when \(2^{b-d}\ne1\bmod3^{\min(t,u)}\) for their labels \((t,b),(u,d)\), using the unit-group interpretation for negative exponents.

Take \(A=(3,1)\) and \(B=(4,2)\). Their final residues are \(1,2\bmod3\), respectively. Their shifted slopes \(27/16,81/64\) exceed one. Every binary word on the two labels, with arbitrarily adjacent inversions in either order, is realized by arbitrarily large odd positive triples and stays **strictly above its entrance at every nonempty physical prefix**. Indeed the word followed by a required odd terminal gives one input class modulo \(2^{H+1}\) by the ordinary parity bijection. Impose divisibility by three by the Chinese remainder theorem. Within an individual block the homogeneous gain increases during the odd steps and then decreases during the even steps to its final multiplier \(>1\). This proves the full path bound, and the inverse decoding proves that (1) fails at every complete prefix within its own permutation family.

Furthermore, finite words of this protected dictionary have arbitrarily large realizing triples \(x=3s\) with **both** \(s,x\) converging to one. Our fixed word imposes only a finite low-bit condition on \(s\). On that condition the current pair after those clocks has a canonical relation \(Y=3^h X+c\) up to exchanging arms, with odd free slope for the anchor. The kernel theorem [FusionControl.synchronized_cylinder, PR200 at ad70a3b831867cb8a74d402a2a1abdc419f5a09b](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/arithmetic/FusionControl.lean#L252) (blob 9b4aeb5580062ce42ff91218e9a75d77f03650ba) gives a further class on which the two trajectories physically meet. To ensure that common terminal reaches one, impose a positive preimage of one in its odd-slope progression: the odd slope at the terminal in the remaining free parameter is exactly a power of three (the original slopes are \(1,3\); each odd shortcut contributes one factor three). For a representative with terminal \(z_0\) and slope \(3^d\), choose \(a\equiv z_0\bmod3^d\) of the form \(2^h\) if \(z_0\) is a unit, or first advance a fixed finite number of prescribed further steps until the terminal is a ternary unit. One odd departure suffices to reach a unit. Since the free slope is odd, one further low-bit choice can force that departure. Powers of two cover every ternary unit class, with unbounded exponents, by the standard order formula \({\rm ord}_{3^j}(2)=2\cdot3^{j-1}\). The positive parameter realizing that power can be arbitrarily large. This last convergence strengthening also follows from the ordinary terminating-family construction in PR200's ORDINARY_STATIONARY_EXCURSIONS. It changes the source for each word and supplies no single positive ordinary survivor.

More generally fix \(t\) with \(\lfloor t\log_2(3/2)\rfloor\ge2\), and take all \(1\le b\le\lfloor t\log_2(3/2)\rfloor\). The full-block slopes exceed one, and the distinct \(b\) differ by less than \({\rm ord}_{3^t}(2)\), so all terminal balls are disjoint. One can even require equal counts of two labels at depth \(2m\), getting \(\binom{2m}{m}\) arbitrary orderings sharing one multiset while each ternary carry class is a singleton. This disproves any inference of sortedness or few changes from failure of a permitted permutation at all prefixes of arbitrarily long finite protected words. It does not place an escaping ordinary source in such a language.

## An all-clock obstruction already on convergent ordinary triples

For \(a=6j\), \(j\ge1\), the odd triple \(x=(2^a-1)/3\) reaches one in \(a\) shortcut steps with exactly one odd departure. No smaller **odd** positive integer can reach a common state with \(x\) at equal clocks and equal cumulative odd counts, even if the clock is unrestricted. No positive integer \(y\le x/3\) can do so either.

Indeed extend a proposed counted merger to a simultaneous visit to one, beyond the first visit of \(x\). That visit occurs on the upper arm at clock \(a+2l\) with \(1+l\) odd departures for some \(l\ge0\). Each positive even step multiplies its input by \(1/2\); an odd step multiplies it by at most \(4/2\). Thus \(2^{a+2l}\le4^{1+l}y\), i.e. \(y\ge2^{a-2}=(3x+1)/4>x/3\). For odd \(y\), retain the first numerator \(3y+1\) in place of the bound \(4y\). This gives \(2^{a+2l}\le4^l(3y+1)\), hence \(y\ge x\).

All of these triples descend directly by other means, so this does not produce a surviving least disagreement. Even multiple-of-three competitors larger than the cheap floor are a genuine exception to the odd-source claim. For \(a\ge12\), \(y=2^6(2^{a-6}-1)/3=x-21\) is a positive even multiple of three, and both arms reach \(2^{a-7}\) after seven steps and one odd departure. Unrestricted unequal clocks and unequal counts remain available.

## Remaining pointwise obligation

For each hypothetical least disagreement, one still needs a compensated word satisfying (1), or a different ordinary route whose clocks or block inventory may change, or a contradiction on that same supplied trajectory. The nine-block progression proves that a protected multi-edit route can work. Inverse decoding proves that an arbitrary amount of disorder need not create one. The monotone-duration theorem in the companion note concerns real maximality, a stronger condition than maximality in the actual ternary class. None of these claims implies universal convergence.

**Pinned nearby work.** PR197 at 1f0f496fbea37792439feada6106eaaff596bcd1, bridge-tests-20261126/FIXED_POOL.md and APERIODIC_HORIZONS.md, separates cheap pools from changed parameters and linearly growing clock tests from all-clock fixed-source failure. PR195 at 51d97cbe17054415acaf95e422801a3532545033, renormalization/HAAR_BARRIER.md, gives the positive-measure profinite obstruction for its fixed Mersenne grammar. PR193 at 25f5462e2c43feea65760884f7ea8f53576fbc18, boundary/COLLISION_SOURCE.md, keeps the source-weighted ordinary merger contribution attached to its common surviving future. These sources use different domains; no verdict here extends to those entire branches.
