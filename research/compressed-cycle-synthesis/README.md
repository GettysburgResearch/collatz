# Compressed positive-cycle synthesis — `86xx` packet

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Status:** no counterexample candidate; theorem-level claims are `PROPOSED`

## Objective

Produce the shortest acceptable Collatz disproof: one finite nontrivial positive
Syracuse-cycle certificate, with every valuation and return independently
replayable.

## Current exact contributions

- `T-8601`: every nonempty sanctuary defined solely by complete residue classes
  modulo a fixed integer contains the residue of `1`. This theorem passed one
  independent reconstruction on draft PR #48.
- `T-8602`: exact proof-producing census of every positive-cycle product window
  through 27 accelerated odd terms.
- `X-8602`: 35.5-trillion-word low-complexity census at `(m,K)=(41,65)`.
- `T-8603`: exact centered-defect exclusion for support sizes seven through
  seventeen.
- `L-8604`: complete exclusion of the infinite concentrated-tail family
  `(b,1^13,2^R)`.
- `X-8608` / `X-8609`: complete product-window joins at supports fourteen and
  fifteen.
- `X-8610` / `X-8611`: complete support-sixteen and support-seventeen joins
  using the cyclic defect-necklace quotient.
- `L-8605`: signed defect charge, balanced-packet binary normal form, and an
  exact weighted Burnside formula for every cyclic support.
- `T-8604`: conditional on the branch-qualified verified range below `2^71`,
  the exact charge cylinder forces at least `72,057,431,991` odd states and
  `29,906,536,378` valuations different from `2`.
- `X-8612`: independent exact rational certificate for that Farey cylinder and
  the packet/necklace normal form.

## Signed-charge eureka

For odd-state length `k`, total valuation `A`, and non-`2` support `s`, put

```text
chi   = 2k-A,
omega = s-chi.
```

Then

```text
chi   = #ones - sum_(a>=3)(a-2),
omega = sum_(a!=2)(a-1).
```

Every positive-charge valuation word is a same-length, same-total-valuation
balanced deformation of one binary `{1,2}` word with exactly `chi` ones. The
number of changed positions is exactly `omega`.

The global cycle product places `chi/k` in one narrow one-sided interval. Under
the recorded `2^71` verified-range premise, exact determinant-one Farey
neighbors give

```text
odd-state length >= 72,057,431,991
signed charge   >= 29,906,536,378
non-2 support   >= 29,906,536,378.
```

These floors are source-qualified: this branch does not independently re-run
the external verification.

## Frozen centered-defect regression totals

```text
support 7..12: enumerated_rows=2,577,878,885, hits=0
support 13:    queries=64,674,409, hits=0
support 14:    conceptual_words=50,008,555,902, hits=0
support 15:    conceptual_words=355,362,127,531, hits=0
support 16:    anchored_words=2,216,415,791,876, formal_matches=0
support 17:    anchored_words=16,071,941,097,518, formal_matches=0
```

The support-14 full replay and every near-`2^64` support-15/16/17 row were
rechecked after widening modular additions. Their zero counts are unchanged.

## Weighted necklace compiler

A defect `1` has slack weight zero and a high defect `a` has weight `a-1`. Put

```text
F(x)=1+x^2+x^3+...
```

and `c_(s,w)=[x^w]F(x)^s`. The number of cyclic defect necklaces is exactly

```text
N_(s,w)
 = (1/s) sum_(d|gcd(s,w)) phi(d)c_(s/d,w/d).
```

This replaces prime-support rotation shortcuts and supplies one composite-
support compiler.

## Honest status

No positive cycle, divergent seed, invariant sanctuary, or other unconditional
Collatz counterexample has been found. The source-qualified cycle floors are
large negative results, not an extrapolation to nonexistence. A full
counterexample still requires one explicit positive integer and exact physical
replay for all time.

## Review order

1. `claims/T-8601-no-periodic-congruence-sanctuary.md`
2. `claims/L-8605-signed-defect-charge-normal-form.md`
3. `claims/T-8604-source-qualified-charge-cylinder.md`
4. `experiments/X-8612-defect-charge-cylinder/README.md`
5. `experiments/X-8612-defect-charge-cylinder/run.py`
6. `experiments/X-8612-defect-charge-cylinder/verify.py`
7. hardened support-14 through support-17 C++ joins
8. reports under `reports/gpt56-cycle-01/`

## Next constructive target

For the cycle funnel, abandon low-support extension and compile the actual
near-critical hierarchy:

```text
(k,chi)
 -> binary base with chi ones
 -> finite balanced packet slack omega
 -> weighted cyclic placement
 -> neutral gaps
 -> factorwise full-denominator join.
```

For the divergent-orbit funnel, seek the analogous determinant-one or balanced
packet coordinate for the changing-modulus refund top boundary. Any survivor
must be converted immediately into one explicit positive integer and exact
Collatz replay.
