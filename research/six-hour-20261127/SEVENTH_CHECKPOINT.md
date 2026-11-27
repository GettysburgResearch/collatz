# Seventh checkpoint: recursive ordinary comparisons and component populations

**Collatz remains open.** The constructive result in this checkpoint is a complete Lean proof on an explicitly specified ternary class. The population results are written arguments with their external inputs named; their six finite Lean interfaces do not formalize those analytic arguments.

## A complete recursive cover at the original parent

Let `T` be the shortcut map, let `Good(x)` mean that the ordinary positive trajectory reaches one, and put

\[
m=11+162j,\qquad N=2^m,\qquad 81z+271=128N.
\]

Assume the two previously established consequences used at a least canonical reverse disagreement:

\[
0<y,\quad 2^{40}y<z\quad\Longrightarrow\quad\operatorname{Good}(y),
\]

\[
0<w<z,\quad w\equiv17\pmod{48},\quad
\operatorname{Good}(3w)\quad\Longrightarrow\quad\operatorname{Good}(w).
\]

The new kernel theorem proves

\[
3^{11}\mid z+1\quad\Longrightarrow\quad\operatorname{Good}(z).
\]

Its 23-leaf ternary tree covers every higher digit of this ball. Nineteen leaves use one canonical comparison, two use two comparisons and two use three. All 29 ordinary queries are positive and strictly below the **same original** `z`. Their lower and upper physical words, odd counts, affine slopes and strict budgets are checked. The last upper state either enters the forty-bit floor or meets an already covered earlier Mersenne. No density argument selects the particular parent.

There is also a separately checked 123-leaf one-query cover under `3^12 | z+1`, and a single explicit comparison under `3^15 | z+1`. The earlier all-unit cutoff was `3^69 | z+1`. The new depth-eleven ball has density `3^-10` in either original parameter; its union with the previously covered disjoint shallow shells has density exactly `9850/531441`. The remaining shallow classes are open.

[Recursive cover and exact example](coupling/NESTED_COVER.md) · [Lean conclusion](coupling/NestedCover.lean) · [Original-budget induction](coupling/NestedCharts.lean) · [Independent one-query cover](coupling/VALUATION_COVER.md)

## All-clock populations, with the ordinary source retained

For fixed `C >= 1`, let `pi_y(Cy)` count distinct ordinary positive starts at most `Cy` that ever visit `y`, with no restriction on their arrival clocks or intermediate heights. The written argument gives a limiting distribution on large ordinary target octaves, including fixed dyadic restrictions. Its limit is the ternary Haar count of legal inverse words with forward gain at least `1/C`. The crowded-target bound is

\[
\#\{X\le y<2X:\pi_y(Cy)\ge K\}
 =O_C\bigl(X/K+X^\eta(1+\log X)\bigr),
\qquad\eta=H_2(3/5)<0.971.
\]

The proof removes **all** late arrival times by compressing the entire future of a finite source interval into a finite union of ordinary orbits. This does not bound a specially selected exceptional target by its generic limiting distribution.

A second written theorem, using the specified fixed-target lower-density and counted-fusion estimates, works inside a supplied actual orbit-merging component `B`. For every sufficiently large octave and every prescribed word in `{1,2}` starting with `1`, with no consecutive `2`s and length at most `c_B log_2 X`, it finds many actual members of `B` realizing that word. Each has no smaller visitor to its observed prefix at any clock, and at most `K(C)` visitors through height `Cx`. The initial integer varies over this counted population. The theorem does not select the component's least integer.

The transfer uses the exact terminal progression, whose dyadic precision is one, and a relative periodic estimate for invariant labels. This avoids paying the complete source word's dyadic precision twice. The late-clock and finite-comparison errors are charged explicitly. These results identify an obstruction to inferring local crowding merely from a long protected prefix; they do not prove disappearance of the finite mass in the all-input criterion.

[All-time ancestor distribution](escape/COMPARABLE_ANCESTORS.md) · [Logarithmic windows in one component](escape/PROTECTED_COMPONENT_WINDOWS.md) · [Six finite Lean interfaces](escape/ComparableAncestors.lean)

## Verification and the remaining universal estimate

The root reviewed the complete new notes, Lean transports and trees, and finite checkers. The independent replay rebuilds twelve local Lean modules, with **28 new printed declaration audits and 28 dependency audits**, and runs three complete deterministic controls in normal and optimized Python. The controls include full integer parents with exponents `21269153`, `2137277` and `49966967`; these are finite checks of the universal affine certificates, not convergence searches at those heights. The population control separately traces every start through `24573` to one.

The replay receipt, exact source manifest and root review record the completed checks and their limits. Repository integrity is checked on clean local and published trees. The all-input proposal remains the [finite reciprocal-sum criterion](BINARY_PREFIX_CRITERION.md): its complete Lean consumer is proved, while the required arbitrarily small finite-mass estimate is not.

[Root review](../../reports/six-hour-20261127/ROOT_SEVENTH_REVIEW.md) · [Replay driver](../../reports/six-hour-20261127/replay_seventh.py) · [Replay receipt](../../reports/six-hour-20261127/SEVENTH_REPLAY.json) · [Manifest](../../reports/six-hour-20261127/SEVENTH_CHECKPOINT_MANIFEST.json)
