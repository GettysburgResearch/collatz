```text
Claim ID:            C-6111
Title:               The six-branch chart is ordinarily empty: m_N -> infinity
Status:              EMPIRICAL  (conjecture with exact supporting computation; NOT proved)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        L-6105, X-6110, T-6102, T-6103
Scope:               the fixed chart of T-6101
Related counterexample candidates: none; this claim asserts there are none in this chart
Resolves (if true):  Q-7601 / issue #58, in the negative
```

## Statement

**C-6111.** `m_N -> infinity`; equivalently, no positive integer is legal for all `N`;
equivalently, the six-branch chart contains no divergent Collatz orbit.

**Status is EMPIRICAL.** What is proved is only: `m_N` is exactly known and strictly
increasing for `N <= 15`, and `m_16 > 2^256` (X-6110).

## The heuristic, stated precisely

By L-6105(a), `S_N` is exactly `6^N` residue classes mod `2^19N`, so its natural density is
`(6/2^19)^N`. The corresponding 2-adic statements are exact:

* the set `S = ∩_N S_N` of all-time legal points in `Z_2` is a nonempty compact perfect set
  (a Cantor set) of Haar measure 0;
* its Hausdorff dimension in the standard 2-adic metric is exactly

  ```text
  dim S = log 6 / (19 log 2) = 0.1360439...
  ```

* `S` has cardinality of the continuum. It contains all the ghosts of T-6103(b), which are
  explicit negative rationals in `[-57.786, -32.067]`.

If the classes were equidistributed, the expected number of positive integers `<= X` legal for
`N` steps would be `X (6/2^19)^N`, giving

```text
E[m_N] ~ (2^19/6)^N = 87381.3^N,
```

and the expected number of all-time seeds below any bound would be `0`. The observed fit
(X-6110) is `101875^N`, i.e. the exponent matches to 1.35%.

**This is exactly the classical Collatz heuristic, localised.** It is not independent evidence:
believing C-6111 is the same act as believing the Collatz conjecture has no divergent orbit
of this shape. That is a reason to treat C-6111 as *unprovable by the present toolkit*, not as
a reason to treat it as settled.

## Why no proof is available from within this namespace

Three separate obstructions, each verified rather than assumed:

1. **No finite-state obstruction.** T-6102 gap audit: all 36 ordered branch pairs `(i,i')` are
   realisable, so the transition graph is complete. Infinite legal itineraries exist in
   abundance (`6^N` at every depth, continuum many in the limit). Emptiness therefore cannot
   follow from any congruence/automaton argument — it must use integrality *and* positivity
   together.
2. **No Archimedean obstruction.** See R-6112: the exact identity
   `x_0 = (Q^N x_N - c_N)/P^N` has `c_N/P^N -> C in [32.07, 57.79]` and
   `(Q/P)^N x_N -> x_0 + C > 0` for any positive seed. Nothing is over-determined; a positive
   integer seed is perfectly consistent with every real inequality available. The
   height/size arguments that bite on the *cycle* side (`R = C - N(2^A - 3^K)` must vanish)
   have no analogue here, because the corresponding quantity is a large positive integer, not
   a quantity forced to vanish.
3. **No finite certificate of boundedness.** L-6105(d) is an equivalence, but no prefix of
   `(m_N)` can certify `sup m_N < infinity`. Deepening the search (X-6110 limitations) buys
   `N` at cost `6^(0.863 N)` and can only ever produce a lower bound.

Together: deciding C-6111 requires a *source-specific* global identity that controls the
canonical least roots. None is known, and this session did not find one.

## What would settle it

* **Positive resolution** (a counterexample): one written integer `x` with an all-time exact
  digit and physical replay proof. By X-6110 it must exceed `2^256`. Note that exhibiting such
  an `x` requires a *proof* of all-time legality, not a long verified prefix — and by
  T-6103(c) it cannot be produced by prescribing an eventually periodic itinerary, which
  removes the only known way to describe an infinite legal word in closed form. This is a
  severe constraint on any future positive attempt in this chart and should be read as such.
* **Negative resolution**: a proof that `m_N -> infinity`. Any such proof must defeat
  obstructions 1-3 above.

## Gap audit of the conjecture itself

* *Is the equidistribution assumption tested?* Partially. The 15 observed ratios have the
  right geometric mean but individually range over three orders of magnitude, which is
  consistent with, but does not verify, equidistribution of the `6^N` classes in `[0,2^19N)`.
* *Could `m_N` stabilise later?* Nothing in the data excludes it; a single all-time seed
  anywhere above `2^256` would make `m_N` eventually constant. The conjecture is exactly the
  assertion that this does not happen.
* *Does C-6111 imply anything about Collatz?* **No.** See M-6120. Its negation would; its
  truth would not.

## Suggested next attack

Do not deepen X-6110 further for its own sake. The only moves with positive expected value are
(i) a source-specific rigidity theorem for the least roots, or (ii) accepting C-6111 as the
working hypothesis and reallocating effort out of this chart, per M-6120.
