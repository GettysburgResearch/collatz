# Independent count reconstruction and exact-checker source review

Reviewer: the in-session `escape_rigidity` agent, 2026-11-23.

**Verdict: VERIFIED within the stated domain.** The global-count note,
its three finite Lean declarations, and the exact checker source were
read and reconstructed. This is internal mathematical and code-source
review. Actual compiler, axiom-audit and finite-execution receipts are
separate evidence supplied by the principal agent.

## Exact inspected bytes

| Source | SHA256 |
|---|---|
| `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md` | `bee22c362de8adcbb6a0360f48240ad276fdf6122f6383273eb10dee8e29271d` |
| `research/whole-repo-round3-20261123/OrbitCounting.lean` | `1886e34527f8c88007ba2dd9f7841283fa13447a03cc7ec4d14f710bd9a70acc` |
| Imported `research/high-variance-20261123/CycleWordAlgebra.lean` | `fc42bf2a602592c7f7ebbe42ca3c21bb96b58f7ce2dc93aed2cafdbac47f984e` |
| `research/whole-repo-round3-20261123/exact_replay.py` | `82a038962c076fbb3282cd53af1e98fbb7fcc27248ca182b8d4aa7b505323170` |

## 1. The global counting proof

The decisive hypothesis is one forward-invariant set of positive odd
integers on which the accelerated map is injective. Every fixed odd
iterate is then injective on that same set. The proof selects one common
odd count `m=floor(log_3(X/8))` for all sources below `X`; their total
binary clocks may vary. This preserves the source injection despite
arbitrarily large intermediate excursions and separated low visits.

For a positive gap word, the full carry satisfies

`C/2^A <= sum_(d=1)^m 3^(d-1)/2^d = (3/2)^m-1`.

At `A>=K=floor(log_2 X)`, the original source term is less than
`2*3^m` and the intercept is less than `3^m`. The endpoint is
therefore below `3X/8<X/2`. It remains in the same set, and all such
sources inject into its lower-height part. No intermediate height bound
or changing odd-clock map is used.

For `A<K`, the prescribed gap composition fixes one shortcut parity
word followed by an odd endpoint. That last parity guard gives a unique
source residue modulo `2^(A+1)`. Since `2^(A+1)<=X`, each composition
has at most `X/2^A` sources in the interval. There are
`binom(A-1,m-1)` positive compositions. Grouping binary strings by
the position of their `m`th one proves the displayed finite
negative-binomial/binomial identity. This is exact finite counting,
not a probability assumption about actual Collatz gaps.

Writing `t=K-1`, the tail begins at
`m=(log_3 2)t+O(1)`, strictly above the binomial midpoint. The ratio
of consecutive tail terms is bounded by one fixed constant less than
one. Stirling's factorial bounds and bounded entropy derivative near
`log_3 2` therefore give `O(X^theta/sqrt(log X))` with an absolute
constant. The critical exponent agrees with
`Phi(log_2 3)/log 3` in the companion collision source.

Iteration of the resulting dyadic inequality is uniform in the set.
Above `sqrt(X)`, geometric decay pays the common square-root logarithm.
Below that height, the entire remaining sum is `O(X^(theta/2))`.
The finite-height base count is absolutely bounded. Thus the theorem
does cover all separated visits, within its stated injective invariant
domain.

## 2. Finite Lean declarations and consequences

`carry_lt_clock_product` proves a coarse upper bound for the entire
chronological carry of every Boolean word. `high_clock_compresses`
uses that bound with the original source height, both clocks and the
complete supplied affine identity. Its coarser intercept still gives
`q<3*3^m` and hence `2*q<X` under `8*3^m<=X`.
`high_lane_card_le` consumes the supplied finite endpoint injection
and lower-set closure after deriving this compression. The infinite
orbit instantiation of those assumptions is the written argument.

The module does not claim to formalize the final-odd cylinder bijection,
stars-and-bars, Stirling, the infinite set theorem or its integral
consequences. The note accurately keeps those boundaries explicit.

The `s>theta` Mellin moment and reciprocal floor bound reconstruct.
The latter has the correct factor `(1-theta)^(-1)` and decay
`M^(theta-1)/sqrt(1+log M)`. The logarithmic product inequality
contributes the factor one third. Comparing the selected positive
pressure maximum with the ordinary component minimum then gives the
stated sharper localization of that same maximum.

At `s=theta`, the available majorant is not integrable; no critical
moment convergence is asserted. The set theorem covers an escaping
orbit, each odd cycle, and the union of periodic points. It does not
cover a branching predecessor basin or automatically cover a truncated
chain or a convergent orbit with its preperiod. Such an extension needs
an explicit terminal-image allowance. The note's current pressure
consumers stay inside its correct domain.

The reviewer directly opened the primary
[Paper 28 v3](https://rstation.ai/problems/collatz/papers/28).
Its equation (24) states a stronger logarithmic bound, and equation
(25a) states critical moment convergence. The present note correctly
credits prior work and does not import that paper's entire analytic
chain. This review does not independently certify that external paper.

## 3. Exact checker source semantics

The replay source was read in full; this section makes no second
execution claim. Its `require` guards remain active under Python
optimization. All comparisons use exact integers or `Fraction` values.

The arbitrary-word loop covers shortcut lengths zero through twelve.
It compares the sequential carry recurrence with the independent
odd-position formula and a reverse decoder. For each fixed length and
weight, it checks translated carry-quotient fibers, constructs positive
ordinary sources in four source blocks, and replays every supplied bit
at that unchanged source. Its box key contains the carry quotient,
original source quotient and endpoint residue; the surrounding loop
keeps both clocks fixed. Removing either quotient must produce an
observed collision before the checker can pass.

The ordinary fixtures retain each odd value only through its first
occurrence and require the repeated terminal value to be the known
cycle state one. Actual windows have odd lengths one through eight,
subject to the available fixture length. Every window records its
original source, endpoint, gaps, shortcut word, full carry and total
clock. The rational test weights are explicitly described as finite
weights, not samples from an uncomputed harmonic flow.

The code checks the finite product/downward-ratio inequality, exact
quotient-channel collision equality, translated-width upper, original
source spacing, and zero ordinary off-diagonal inside each source box.
It requires observed repeated-word and cross-box collisions; these
terms are not silently absent from the fixtures. Aggregation uses a
valid coarse Cauchy bound which retains cross terms.

The global-count controls check the negative-binomial identity exactly
and test the full next `m` odd steps for every positive odd source at
each declared finite height. Their final-odd cylinder modulus is
`2^(A+1)`. For finite orbit fixtures, the fixed odd-shift injection is
used only on positions with all `m` later positions available; every
remaining final source is paid through `terminal_unpaid`. This avoids
fabricating forward invariance for a truncated path. The known pair
`1,5` explicitly rejects injectivity on the whole convergent basin.

The final cycle control uses complete carries modulo the entire
denominator seven and retains the known trivial-cycle repetitions.
Neither its matching bound nor any finite fixture pass is used as an
infinite source theorem.

## 4. Remaining boundary

Neither the count nor the translated-box injection gives a global
critical same-law collision upper, a smaller meeting source, escape
exclusion or a full-denominator cycle exclusion. The files retain
those missing steps and do not claim a new sparsity record.
