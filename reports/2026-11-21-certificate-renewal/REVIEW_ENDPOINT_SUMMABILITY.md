# Mathematical review of endpoint summability and moving cutoffs

Reviewed manuscript: `FIXED_ENDPOINT_SUMMABILITY.md`, SHA-256
`cbd8e00d73c0da06a063e7334a96ab27145a58ffcc3bd56604a3c8370d8663bd`.
Reviewed standalone question: `question_moving_residue_moment.txt`, SHA-256
`01bcfa252b11a28a6f32c423c6b103612556944ceb12bdaa1667a51a3bbd95a3`.

Scope: ES1--ES4 and the standalone arithmetic problem, at exactly those
bodies. This is internal mathematical review, not formal verification or an
external referee verdict. The reviewer independently reconstructed ES1--ES2,
then contributed the simultaneous-endpoint telescoping improvement and the
sharp rational constant used in ES3. Thus ES3's review is a detailed check of
a jointly developed argument, not independent authorship of that argument.
The standalone code's full implementation is not covered by this review;
the finite exact polynomial check described below was executed separately.

## ES1--ES2: verified

For each fixed source, its first hit of `t` contributes at most `t²/n⁴`.
If `t` is nonperiodic there is no second visit. If `t` lies on any positive
cycle, the full-cycle Jacobian is the reciprocal of a product containing
`1+1/(3t)`, and is therefore at most `3t/(3t+1)<1`. Every later visit is
separated by that same cycle. This gives the displayed geometric bound
without excluding nontrivial cycles or counting repeated states as distinct.

Tonelli is legitimate because every term is nonnegative. It gives the
all-source sum before its finiteness is concluded. Primitive words at a
fixed length have different ordinary starting representatives, so their
weights form an actual sub-sum of the endpoint masses. The fixed-endpoint
and finite-endpoint summability conclusions follow exactly as stated.

## ES3: verified, with the authorship qualification above

Using `V_q=(J_q/n_q)^4`, one ordinary odd step gives

`V_(q+1)/V_q=(3n_q/(3n_q+1))^4`.

Hence the difference identity (5) is exact on every ordinary orbit, with
no occupancy, stopping, or nonperiodicity premise. Clearing denominators in
`delta(t)≥175/(256t)` gives coefficients, in ascending degree order,

`[-175,-1844,-6378,-5076,13473]`.

A separate exact coefficient multiplication confirmed that this equals
`(t−1)(175+2019t+8397t²+13473t³)`. Its sign is nonnegative for every real
`t≥1`, a fortiori every required positive integer. The geometric fixed
point sum is exactly `256/175`, confirming sharpness of the per-source
constant.

Finite-time telescoping gives (7) with a nonnegative terminal remainder.
Monotone convergence and Tonelli then give (8), and restricting to the
primitive sub-sum is legitimate for each `q`. Multiplying the fifth-power
weights by at most `R³` proves (9). No conclusion for the original
second-power weights is silently inferred.

## ES4: verified

At fixed `q`, the primitive sources are distinct and their correction
products are at least one. Therefore each restricted summand is bounded
by `R²/b_w⁴`; summing yields (10).

For every `r_w≤q^beta`, the inequality

`q^(-3 beta) J_w^4/r_w² ≤ J_w^4/r_w⁵`

has the correct direction. Equation (8) proves (11), including `beta=0`.
For `beta>0`, splitting off a fixed finite initial segment of the convergent
series proves the little-o statement (12); at `beta=0` the manuscript
correctly claims only a finite total mass.

The critical harmonic endpoint `beta=1/3` is included correctly. For every
`0≤beta≤1/3`, `1/q≤1/q^(3beta)`, so the harmonic time sum converges.
Splitting its initial segment proves Cesàro convergence to zero. This does
not claim pointwise decay at a prescribed growing cutoff.

The fixed-time estimate yields cumulative order `N^(1+2beta)`, which is
negligible at exponent `59/19` precisely in the stated strict range
`beta<20/19`. The choice `beta=1` gives both the simple `O(N³)` bound and
the stronger little-o consequence of (12). Thus replacing `P_q` by its
`r_w>q` tail changes the normalized cumulative quantity by a term tending
to zero. Both directions of the claimed PC equivalence are valid.

## Standalone question: verified as a self-contained open arithmetic target

The representative definition determines a unique odd residue modulo
`3^q`, and the displayed total word weight proves finiteness of the
countable sums. The last-exponent recurrence has period
`L_q=2·3^(q−1)` in its exponent menu: increasing that exponent by `L_q`
preserves the predecessor residue modulo `3^(q−1)` and its oddness.
Thus the geometric prefactor is exact, including `q=1` with constant
`H_0`. Grouping by the last exponent gives the stated `P_q,Z_q` formulas.

The estimates supplied in the question agree with ES3--ES4. The proposed
stronger estimate `Z_q=O(q^(21/10))` really would imply the target because
`31/10<59/19`. The problem does not assert the target or replace weighted
representatives by independent random residues.

## Limits of the verdict

All mathematical deductions above are correct for the frozen statements.
No claim of universal convergence follows from ES1--ES4: the remaining
moving tail with endpoint weight `r_w^-2` has not been bounded as required.
The arithmetic target in the standalone question remains open. Its payoff
is nonperiodic-orbit exclusion under the separate occupancy argument;
positive cycles still need their own exclusion.
