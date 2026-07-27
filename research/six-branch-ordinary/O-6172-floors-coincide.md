```text
Claim ID:            O-6172
Title:               The true stopping floor and the density floor coincide for L <= 375
Status:              EMPIRICAL
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        X-6170
Scope:               computed range only
```

## Statement

With

```text
s_L  = min { n >= 2 : T^j(n) >= n for all 1 <= j <= L },
nu_L = min { n >= 2 : k_j(n) >= ceil(alpha j) for all 1 <= j <= L },   alpha = log2/log3,
```

exhaustive computation over `2 <= n <= 10^8` gives

```text
s_L = nu_L   for every L in [1, 375].
```

## Why it is interesting

`s_L` is defined by the *actual values* of the orbit and `nu_L` by the *itinerary alone*. They
are different conditions: `nu_L` ignores the additive `+1`s entirely. That they select the
same minimal integer at all 375 computed depths says the additive terms never change which
integer is extremal.

This is the least-root shadow of Terras's coefficient-stopping-time question (whether the
value-based and coefficient-based stopping times agree). It is recorded as EMPIRICAL and must
**not** be assumed: R-6171 is written so that it depends only on `nu'_L <= nu_L`, an
inequality, and never on this coincidence.

## Adversarial tests

* Both sequences reproduce the classical stopping-time records
  (`3, 7, 27, 703, 10087, 35655, ..., 63728127`).
* The computation excludes `n = 1`; including it makes `s_L = 1` for all `L` (the trivial
  cycle satisfies the condition forever) and the coincidence becomes vacuous. The first run
  of X-6170 made exactly this error and is recorded there.

## Superseded by L-6173

The scan was extended to `2 * 10^9` and the question was sharpened. The result is much
stronger than what this file records, and one half of it is a theorem:

* `B(n) <= A(n)` for **every** `n`, unconditionally (two lines — the itinerary condition forces
  `3^{k_j} >= 2^j`, hence `T^j(n) > n`);
* `A(n) = B(n)` **pointwise for every `n <= 2 * 10^9`**, not merely at the floors;
* and the coincidence is the classical **coefficient-stopping-time** question (Terras 1976),
  open since then — so it should not be attacked here.

See L-6173. This file remains as the record of how the observation was first made.
