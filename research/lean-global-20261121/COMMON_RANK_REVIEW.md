# Independent reconstruction of the common-rank proof

**Verdict: VERIFIED at the numerical well-foundedness and induction scope.**
This review was performed by the separate forcing lane, which did not author
`CommonRank.lean`. It does not certify universal move coverage or import an
old template's physical legality into Lean.

Reviewed source:
`lean/CollatzGlobal/CommonRank.lean`, SHA-256
`eb9df9962a9f696e8009b2e919e05139548ac4b4313f3e592405297aa3b130f1`.
The source was read in full and the following argument reconstructed.

## Statement and exact order

For a natural source/clock pair `x=(n,d)`, the mathematical score is
`(n+1)*(201/200)^d`. `ScoreLT y x` is the exact natural-number cross
multiplication comparison. Both denominators are strictly positive, so it
has precisely that rational interpretation. No floating-point computation
or assumed ordering principle occurs.

A strictly decreasing sequence of arbitrary positive rationals would not
be enough. The proof does not use that false argument. Instead, it fixes
one integer upper bound `B` on the score and proves both coordinates are
bounded on that same sublevel.

## Reconstructed finiteness argument

The integer Bernoulli inequality

`(200+d)*200^d <= 200*201^d`

is established by induction. Combining it with the sublevel inequality
`(n+1)*201^d <= B*200^d` gives `n+1<=B` and `d<=200B`.
The latter bound is deliberately weaker than the sharp elementary
Bernoulli consequence, but is sufficient and valid.

Strict score descent preserves the fixed sublevel. With `E=200B`, every
point in that sublevel therefore has the common-denominator integer

`scaledRank E (n,d) = (n+1)*201^d*200^(E-d)`.

Since `d<=E`, natural subtraction in its exponent is the intended ordinary
difference. Multiplying the strict score inequality by the two positive
missing denominator factors proves strict descent of this integer.

The accessibility proof performs strong natural-number induction on this
one scaled integer, while carrying the unchanged sublevel as a hypothesis.
Every predecessor remains in the sublevel and strictly lowers the integer.
Thus the induction never changes denominator in a way that could hide an
infinite descending chain. Finally every source belongs to some integer
sublevel; choosing its numerator as that bound is sufficient because the
denominator is at least one. This proves `scoreLT_wellFounded` globally.

## Goal kinds and coverage boundary

`common_rank_induction` is valid for arbitrary goal kinds: apply the proved
well-founded induction to the conjunction over kinds at each numerical
state. Its step hypothesis explicitly requires a strict score decrease for
every cross-kind premise. It does not infer a local goal conversion from an
equivalence between two universal closure principles, and it does not
supply any accepted move at a residual state.

The separate `PsiTemplateBridge.lean` addresses the specific binary/psi
conjugation. The separate `PsiCoverage.lean` gives an infinite family on
which the proposed forward-return and eight-template union has no accepted
step within the supplied witness. Both are compatible with the positive
well-foundedness theorem reviewed here.

## Verification event

This was a substantive source reconstruction of the stated proof, not a
claim that repository integrity establishes mathematics. The author's
compilation and the publishing packet's fresh Lean build and public axiom
audit are separate recorded events. This review is pinned to the exact
source bytes above; later changes require a corresponding review boundary.
