# A global canonical return within \(201326592n\)

For the positive shortcut $T(2v)=v$, $T(2v+1)=3v+2$, write $G(x)$ when some ordinary iterate equals 1. A canonical reverse defect is a positive $z\equiv17\bmod48$ with $\neg G(z)$ and $G(3z)$.

**Kernel theorem.** Every positive ordinary $n$ with $\neg G(n)$ forces a canonical reverse defect $z\le201326592n$. Consequently the least such $z$, when it exists, satisfies
\[
      0<n,\quad 201326592n<z\quad\Longrightarrow\quad G(n).
\]
The new factor is $24\cdot2^{23}=3\cdot2^{26}<2^{28}$. PR197's previous global factor is $2^{40}$. The new inequality applies to any positive bad input and any least canonical defect. It requires no cycle, Mersenne, valuation, density or nondivergence assumption. It leaves the existence of a bad input open. [Composed kernel theorem](GlobalReturnBudget.lean)

## A direct bounded return at \(1\bmod16\)

For every odd $n\ge3$, a finite positive directed path from $n$ ends at some $y$ with $0<y<n$. Each ordinary edge is traversed in either direction. Every other edge is a tripling $w\to3w$ with $w\equiv1\bmod16$ and $w\le24n$. The cofactor bound is relative to the original $n$ of that path. The proof does not impose that bound on ordinary intermediate heights.

The 140 words partition $n=3+2t$ by successive binary and ternary digits of $t$. A node $(a,b)$ represents all $n=at+b$; its $m$ children are $(ma,b+ia)$ for $0\le i<m$ with $m=2$ or $3$. Each word manipulates affine positive ordinary states $At+B$. A forward block $F(e)$ checks an odd input $x$ and $3x+1=2^e x'$, giving $T^e x=x'$. A backward block $B(e)$ checks the same relation at its opposite endpoint. A charge checks both the constant and slope of $w\equiv1\bmod16$ and $w\le24n$. The end row $(A',B')$ satisfies $A'\le a$ and $0<B'<b$.

For example, $n\equiv1\bmod4$ has the ordinary two-step route to $(3n+1)/4<n$ for $n>1$. The longer leaves retain their literal charged cofactors: the certificate has 237 such positions, uses at most eight in any one word, and has at most 64 listed blocks per word. Every ordinary block checks at most ten physical shortcuts. The largest ratio among all constant and slope comparisons in these particular words is exactly 24. Its slope is attained on an original row $5038848t+1215655$ at the charged position $120932352t+29175697$, so the ratio of ordinary values approaches 24 there. This establishes the word-certificate cost, without claiming an optimal return algorithm. [Literal checked tree](ReturnTwentyFour.lean) · [Generic ordinary proof](ReturnAtlas.lean)

If $n$ is bad and its charged word ends at a good $y$, some charged $w$ is bad with $3w$ good: ordinary edges preserve the hitting predicate and the path must change label. If the endpoint is bad, strong induction at $y<n$ gives a binary-class defect $w\le24y\le24n$. Even bad inputs halve. One is good. This proves
\[
 \neg G(n),\quad n>0\quad\Longrightarrow\quad
 \exists w>0:\ w\equiv1\bmod16,\quad w\le24n,\quad\neg G(w),\quad G(3w).
\]

## The exact canonical localization

PR197 at 1f0f496fbea37792439feada6106eaaff596bcd1 supplies the additional assertion that each such **ordered** binary-class defect $w$ has a canonical reverse defect $z\le2^{23}w$. This is the private declaration `CollatzQuantitativeReturn.from16` in `closing-proposal/QuantitativeReturn.lean`. Its finite ternary bank retains the actual original parameter across splits, treats both successors of a nonunit, and uses ordinary path certificates on an already known defect. Its final charged 11-mod-32 representative exchanges to an actual 17-mod-48 defect. The new bridge imports that exact checked declaration by its source name. An explicit induction proves the upstream predicate `Hits n k` is equivalent to `run k n=1`; the two ordinary shortcut functions are definitionally equal. Multiplying the two actual bounds gives the displayed global factor. [Upstream source](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean) · [Upstream proof description](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QUANTITATIVE_RETURN.md)

The six unmodified Lean dependencies in [pr197-floor](pr197-floor) come from that exact commit. Their original paths and full SHA-256 digests appear in [the control](GLOBAL_RETURN_CONTROLS.json). The source of `ReverseBasin.lean` there is PR197's vendored PR146 version. Build `ReverseBasin`, `DirectedEleven`, `UnitResidueExchange` and `NonunitExit`, then `TwoOddCertificate`, then `QuantitativeReturn`. Build `ReturnAtlas` after `EarlierOffsets`, `ReturnTwentyFour` after `ReturnAtlas`, and `GlobalReturnBudget` after `QuantitativeReturn` and `ReturnTwentyFour`.

[The checker](check_global_return.py) parses the literal Lean tree, checks the two coefficients of every edge, directly follows both endpoint representatives of every ordinary block, and reconstructs the charge ratios and the disjoint leaf mass. It also checks that each odd integer from 3 through 20001 lies in exactly one leaf and has a smaller positive endpoint, then verifies the pinned dependency bytes. Its execution is independent of the kernel decisions.

## Relation to height-bounded directed paths

Paper 228, §2, gives height-bounded routes from 1 to $n$ using directed tripling at odd cofactors. A transition leaving the basin along such a route has the opposite ordered labels from the reverse defect above. Paper 232, §7, gives directed returns from $n$ to 1 with odd unit cofactors. A return from a bad input has a bad-to-good charged step, but the unit is not thereby in the canonical residue class. These papers motivate the use of physically bounded directed comparisons. The new 140-leaf controller specifically forces the binary class needed for PR197's canonical localization, with an explicit cost in the original height. Neither paper's conjectural unproved tripling implications are assumed. [Paper 228](https://rstation.ai/problems/collatz/papers/228/v1) · [Paper 232](https://rstation.ai/problems/collatz/papers/232)
