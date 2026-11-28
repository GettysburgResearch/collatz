# Checkpoint 3: independent review of inverse repair, positive boundary values, and integer shadows

**Research remains open. No proof or disproof of positive Collatz is claimed.** This checkpoint records three complete written arguments and the completed local Lean replay from checkpoint 2. The nine-hour pass is still in progress, with the original endpoint 2026-11-28 18:08:39 UTC.

## Exact source commits and review scope

The arithmetic packet is `dd20d2e4c851d87753283d63ff621ea71b386c88`, with its source-credit correction `76a7d57a52451a10f8d56304eaa629635e000478`. The dynamics packet is `bc4e97bce04ec7bdce2ac99cb002a951bf70c52c`. The outside packet is `03c40c25f2610cbe6f7600ccc6f3d91d4126fa71`. These are author worktree commits, cherry-picked into the integration branch. Local and GitHub publication histories have different commit identifiers but their published trees are compared exactly.

The coordinator reconstructed the arguments below from the frozen text. The finite controls were read and rerun under normal and optimized Python; their outputs and source hashes are in [CHECKPOINT_03_FINITE.json](CHECKPOINT_03_FINITE.json). These checks are bounded controls, not proofs of the asymptotic claims.

## 1. A sparse edit need not admit a cheap inverse reunion

[SPARSE_EDIT_INVERSE_REUNION.md](../../research/astra-wild-nine-hour-20261128/arithmetic/SPARSE_EDIT_INVERSE_REUNION.md) treats two inverse Syracuse words, both beginning at the supplied ternary sources. Its cost is the total number of powers of two consumed, summed across both paths. It allows the edit, words, and stopping times to depend on the observed source. The generic statements concern Haar or a specified full-dimensional geometric Syracuse law. They are not statements about every fixed positive ordinary integer.

For a word with odd depth n and total S, its affine numerator is B and its inverse endpoint is (2^S x-B)/3^n. The coordinator checked the order of composition and the resulting two-source congruence. Different odd depths give coefficient valuation min(n,m). At equal odd depths and unequal totals, the only additional valuation is v_3(2^{|S-T|}-1), bounded by a logarithm of the cost. Thus each unequal-clock pair restricts the source to at most a polynomial factor times 3^{-W-max(n,m)} of the ambient cells.

The weighted positive-composition sum is the significant improvement over an unweighted count. Weighting a word of depth n by 3^{-n/2} changes the exponential cost factor to (1+1/sqrt(3))^C. The possible sparse signed trit displacements contribute only exp(o(W)) at total precision O(W). Consequently unequal clocks cannot reunite at precision W below combined cost

\[
\left(\frac{\log 3}{\log(1+1/\sqrt3)}-o(1)\right)W
  = (2.41057812\ldots-o(1))W
\]

outside an exponentially small event. The extension to the critical law uses the order-q entropy estimate proved from the earlier permutation-mixture argument and Leen's named entropy input. Hölder's inequality transfers an exponentially small Haar union of cells to an exponentially small event under that law. It does not replace reverse relative entropy by forward relative entropy.

At equal clocks, the numerator modulo 2^S determines the word. Hence every partial signed-edit numerator remains nonzero, not merely the final displacement. Applying the archimedean size bound at every gap between edited trits gives

\[
(h+1)S\ge (\log_2 3)(W-2h)+n.
\]

This establishes the stated linear total-cost lower bound after a single changed relevant trit. For edits confined to the first o(W) positions, the full displacement is subexponential in W; its numerator is too small to vanish modulo the reunion precision, giving the stronger generic constant above. Edits beyond the relevant observation window and independently reoptimized optimal costs are explicitly excluded from the claimed conclusion.

The qualitative impossibility of exact reunion after a nonzero integral translation at an irrational source is prior in PR215's affine-overlap classification. Leen's fixed-depth transfer dipole argument and Weaver 118's numerator separation are also credited. The new contribution is the finite-precision estimate with linearly growing competing clocks and adaptively selected sparse edits. The dynamics agent independently checked the same elementary valuation and sparse-digit portions; neither review rebuilds Leen's full analytic theorem.

## 2. The entire positive range of a cycle-centered amplitude

[CENTRED_BOUNDARY_AMPLITUDE.md](../../research/astra-wild-nine-hour-20261128/dynamics/CENTRED_BOUNDARY_AMPLITUDE.md) uses the actual shortcut trajectory and its actual number q_t of odd departures:

\[
W(n)=\lim_t 2^{t-2q_t(n)}T^t(n)/n.
\]

An even step preserves the normalized quantity. An odd departure from x multiplies it by (3x+1)/(4x). This is one at x=1 and at most 5/6 at every other positive odd integer. Therefore W exists, is positive exactly on the basin of one, and is uniformly approximated after p odd departures to absolute error at most (5/6)^p. This does not make positivity decidable: an arbitrarily small positive answer has no uniform detection deadline.

At an odd starting unit a that first reaches one, W(a)=2^g/a for an integer g. Reduction cannot cancel any odd factor of a. Thus its entire odd denominator is a and its ternary valuation is zero. This observation supplies the arithmetic uniqueness used throughout the range classification.

Write V for the positive amplitudes at odd ternary units and K for its closure. A sequence of amplitudes tending to a positive value has uniformly bounded first-hit odd depth, by the 5/6 contraction. A finite diagonal subsequence then has h initial odd states tending to infinity, followed by one fixed convergent odd state a. Its limit is (3/4)^h W(a). Conversely such a limit is realized by genuine unit inverse edges, using a large first gap and bounded additional gaps. All those positive integers really reach a and then one. A growing inverse ray supplies zero as a limit.

This proves the exact disjoint decomposition

\[
K=\{0\}\sqcup\bigsqcup_{h\ge0}(3/4)^h V,
\qquad
K^{(j)}=\{0\}\sqcup\bigsqcup_{h\ge j}(3/4)^h V.
\]

Only finitely many layer indices can approach a fixed positive number, which justifies taking each successive derivative. The rank of a positive rational point is its ternary valuation; zero survives to rank omega. There is no inference that an exceptional positive source would produce a new positive layer: its amplitude would be zero.

The same proof identifies the full cluster set at infinity inside a prescribed binary cylinder with q>=1 odd departures as K^{(q)}. For the lower inclusion, the endpoint of a genuine prefix ranges as v+3^h b. Powers of two run through every unit class modulo 3^h, so actual endpoint values 2^e a can be attached without changing that prefix. This preserves source compatibility and establishes the stated limsup (3/4)^q on every such cylinder.

The positive-rational membership algorithm checks the rank, the power-of-two numerator, and the candidate ordinary odd denominator. The proposed value supplies a finite first-hit deadline via the contraction. The local path detector is also sound: sufficiently close genuine amplitudes to (3/4)^h W(a), h>=1, must come from paths hitting a after exactly h odd departures. In a contrary sequence, rank fixes h and the reduced odd denominator fixes a.

That detector states a potential circularity precisely. Producing sufficiently fine positive approximations near such a point already entails the desired ordinary path. A density or compactness argument that supplies only zero or arbitrary moving points in K cannot establish that every ordinary denominator appears. The complete range and its accumulation ranks are proved without assuming universal convergence; denominator surjectivity is the unresolved global content.

## 3. Exponential integer shadows: exact recovery and a lower-density counterconstruction

[EXPONENTIAL_INTEGER_SHADOWS.md](../../research/astra-wild-nine-hour-20261128/outside/EXPONENTIAL_INTEGER_SHADOWS.md) follows one fixed positive real source through one prescribed affine script. If that real path escapes and is exponentially close to integers at dates with successive ratio tending to one, the script eventually executes one genuine ordinary orbit. With an ordinary integer source, every earlier letter must have been genuine as well.

The key arithmetic step is elementary. Between two observations u<v, clear the word's full denominator 2^{v-u}. If the resulting two error contributions have sum less than one, the rounded endpoint equation is an exact integer equality. A wrong shortcut branch on an integer creates denominator two and every later branch doubles the reduced dyadic denominator. Therefore exact integral endpoints force all intermediate parity guards. Linked observations follow the same rounded trajectory, rather than independently selected finite witnesses.

The real escape assumption is essential. Along an escaping positive path the per-step additive logarithmic correction tends to zero. Its cumulative correction is o(t), so the common affine multiplier cannot shrink a fixed nonzero initial error exponentially at all linked endpoints. No unproved reciprocal-summability assertion is used. A set of positive natural density supplies the required regular observation dates. The proof also tolerates an eventual successive-ratio bound strictly below 1+sigma/log(3).

The density estimates partition good dates into maximal linked clusters. The coordinator checked both bounds on each cluster: a lower ratio of its first to last time, and an upper ratio of the previous cluster's end to its start. Charging the mandatory bad gap to the entire next cluster gives an upper good fraction (1-a)/(1-ab). This yields the universal deficit (sigma/log(3))^2. When log(r_t)/t tends to g, the sharper deficit is sigma(g+sigma)/(log(2)(log(2)+g)). At sigma=log(2) this gives upper density zero. No limiting speed is imposed in the general bound.

The optional algebraic-irrational extension uses Ridout's restricted-denominator approximation theorem. The coordinator checked the exact consequence in Bugeaud's published research exposition, equation (2.2), rather than claiming to have rebuilt Ridout's proof. The original publisher page currently exposes the abstract. Sources: [Ridout, Mathematika 4 (1957), 125–131](https://doi.org/10.1112/S0025579300001182); [Bugeaud, Quantitative versions of the Subspace Theorem and applications, equation (2.2)](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.749.pdf). This outside analytic theorem has no locally compiled Lean claim here. The ordinary-integer case is elementary and does not use it.

[POSITIVE_LOWER_DENSITY_SHADOWS.md](../../research/astra-wild-nine-hour-20261128/outside/POSITIVE_LOWER_DENSITY_SHADOWS.md) proves that positive lower density is insufficient. It preserves any requested true prefix at a supplied ordinary source and then makes one wrong choice. Every later real state stays nonintegral. Geometrically growing stages combine an odd growth reserve, the two equal-slope pairs 10 and 01, and an odd observation window. The pair translations form overlapping intervals and give exponentially fine real target control.

The reserved early pair choices can impose any residue modulo M coprime to six: every available coefficient generates the additive group modulo M, so adjoining it enlarges a proper subset-sum set. At most M-1 choices suffice. A following odd suffix supplies ternary precision. Selecting an integer target congruent to minus one modulo 2^J times the odd modulus makes the final J odd steps genuine for that rounded target. During the interior half-window both the binary source state and the rounded integer also agree with minus one to growing binary precision.

The exact exponent margin leaves error at most 2^{-t/25}. The preceding odd reserve more than pays for contraction during the pairs, giving positive lower real exponential growth. Consecutive stage lengths remain within a fixed geometric factor; therefore the selected windows have positive lower density through every late cutoff. They need not have natural density. In fact the recovery theorem proves that the full good set contains no subset of positive natural density. There is no contradiction between those two density statements, and no limiting real speed is asserted for this construction.

These are single-script, single-real-source statements. Their obstruction is that rounded integers in different stages are not proved to lie on one rooted ordinary orbit. Agreement at every fixed modulus and positive lower density of exponentially accurate integer observations still leave that exact link absent.

## Completed formal replay and prior publication

[CHECKPOINT_03_LEAN.json](CHECKPOINT_03_LEAN.json) contains the completed fresh compile of all four included project modules and a separate fresh import/type-check/axiom audit of all nine public roots. The strict flags are `-j1 -DElab.async=false -DwarningAsError=true -DautoImplicit=false`. Lean is version 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`. Only `propext`, `Classical.choice`, and `Quot.sound` occur. Cached third-party compiled dependencies were reused; no cold Mathlib rebuild or independent kernel replay is claimed.

This completed replay supersedes the *pending* status recorded at checkpoint 2, while leaving that historical receipt intact. The Lean modules certify finite arithmetic kernels. The full asymptotic, topological, entropy, and shadow theorems above are independently reviewed written arguments, not fully formalized proofs.

Checkpoint 2 was published at GitHub commit `538181fd622de9e25216399d43e6fb6cbb51644a`, with exact tree `3b3690374adcb17ce8aa07d1216e0e81f5706791`, matching local commit `6946dd5eb47abc3974955c199ad053c8fa103c20`. Its complete clean checkout passed the repository validator with empty stderr and stdout SHA-256 `83a9a1bdde79e5cb76b1cb66bf02720624ba6b766c4b24e3d06178e6ea58ae59`. The remote branch was read back at that exact commit after publication. Repository validation is an integrity gate, not mathematical certification.
