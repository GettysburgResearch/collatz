# Cross-branch interface audit

All referenced claims retain their native branch status. None is promoted,
renumbered, or copied into a root ledger.

## PR #3 — tower and 256-stage packet

**Head read:** `bdbf5620743f48914331f015d5cba1ba9268b616`

- `L-0016` / `L-0017`: supply the exact tower data and canonical connector
  identity used to define `D-9701`.
- `L-0023` and `O-0010`: identify the explicit
  `-(7/4)log_2(3)` moving control bulk. No `97xx` proof preloads it.
- `T-0024`: proves positive information surplus for the chronological
  256-transition stage. It explains why the direct-contraction proof cannot be
  silently transferred at the current stage denominator.
- `T-0025` / `T-0026`: isolate finite-word connector control from the ordinary
  residual zipper.
- `T-0027`: supplies the exact composed stage map, exponent formulas,
  correction/cap decomposition, and stage-to-stage quotient equation.
  `T-9703` uses this frozen interface and compares its current odd multiplier
  with the **next** complete stage radix.
- `T-0028` / `T-0029`: show that the padding counter can route finite connector
  prefixes. This removes prefix scarcity but not the full correction equality.
- `L-0029`: peels exactly the logarithmic counter-routed prefix from the
  remaining ordinary connector obligation; the residual depth stays `Theta(t)`.
- `T-0030`: replaces preloaded inverse-logarithm digits by the forward ordinary
  sequence `V_(m+1)=V_m+2^(m+1)V_m^2`. `Q-9702` records the exact unresolved
  task of coupling that word to `S_m=R_(m+1)`.

The PR #3 interface remains `PROPOSED`. `T-9703` does not claim an independent
reconstruction of all 256 physical blocks.

## PR #32 — independent ADEL review

**PR read:** `#32`, frozen source PR #16 commit
`e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`

The independent reviewer passed `L-9309`, `T-9307`, `T-9308`, `L-9310`,
`T-9311`, and `T-9312`, with extensive exact adversarial checks. This provides
strong methodological support for completion-height arguments and makes the
next proposed attack on a long cap-correction run more credible. No status from
PR #32 is copied into this namespace, and none of those claims is needed for
the proof of `T-9703`.

## PR #20 — finite-tower cylinders and periodic tails

**Head read:** `717ab8a0f3be7a87800d81b23973e2e59adaa7f6`

- `T-9409` states the one-cylinder theorem and stabilization criterion in the
  active stack chart. `L-9701` independently proves the same odd-affine algebra
  and adds the explicit block recurrence in its own namespace.
- `T-9414` / `T-9415` exclude eventually periodic positive increment tails of
  period at most three. They do not directly quantify PR #3 stage words and are
  recorded only as a model for a future native periodic cap-chain exclusion.

## PR #19 — H carries

**Head read:** `2e7b313efa178d46d8513add74e54575e9b71767`

`L-9503` identifies positive ordinary ghosts with bounded/stabilized least
representatives and eventual zero carries. The block `a_k` of `L-9701` is the
general odd-affine analogue. No H claim is a proof dependency.

## Issue #21 — Diagonal Foundry

**Branch read:** `claude/collatz-repo-exploration-m2e5vp`

- `T-9601`: strict causality selects one completion point.
- `T-9604`: an ordinary finite-support solution makes feedback eventually
  autonomous.

`T-9703` gives a parallel arithmetic exhaustion statement: an ordinary finite
height cannot support a positive free stage quotient against nearly squared
future radices forever, so the tail becomes autonomous in the cap-correction
coordinate.

## PR #16 — completion-height carry rigidity

**Head read:** `e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`

`L-9310` proves that long zero-carry runs create divisibility exceeding the
height of a nonzero ordinary numerator. `T-9701` is a finite-trap member of the
same family. `T-9703` supplies a new first step for the supercritical stage:
future completion height kills the free quotient, leaving a zero-quotient chain
to which a product-formula numerator may be applied next.

## Issue #29 — unpublished cross-direction synthesis

The sole issue comment reports a proposed `Theta(K^2)` terminal-height pressure
for an eventually-zero active-cylinder tail and explicitly distinguishes suffix
series membership from stabilization of the already selected prefix. The files
were not published and are not a dependency. `Q-9702` records only the
independently reconstructible research cue: exhibit the nonzero numerator and
global height for a long cap-correction run.

## PR #13 wave 3 — literature interfaces

**Head read:** `3157bfa294e4b7287416b9469f6007815dead328`

- `LIT-KTHM-0030`: the PR #3 moving bulk is a transcendental p-adic logarithm.
  It is not used as an initialized digit tape here.
- `LIT-KTHM-0033`: entropy surplus can imply a symbolic router only after a
  stationary SFT normalization and separate arithmetic realization. `T-9703`
  sharpens the arithmetic target to cap-correction equality but does not supply
  the stationary symbolic hypotheses.

## Status and ledger boundary

The six live project-state ledgers on PR #3 were read but are not edited:

```text
CURRENT_STATE.md
OPEN_PROBLEMS.md
CLAIMS.md
CANDIDATES.md
NEGATIVE_RESULTS.md
NOTATION.md
```

Issue #31 and this namespaced inventory are the only ownership records changed
by this packet.
