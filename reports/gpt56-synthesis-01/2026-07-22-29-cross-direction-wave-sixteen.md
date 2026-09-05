# Cross-direction lemma forge: wave sixteen

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

Wave fifteen left four unusually sharp interfaces:

- decide whether the 64 three-symbol room addresses and the sixteen cap-head
  cells are transverse or are two quotients of the same correction;
- exploit shared boundaries across adjacent corrected stages instead of paying
  two endpoint directions independently at every stage;
- turn the native periodic q-difference equation into a sourced value theorem,
  keeping formal rank, determinant nonvanishing, and arithmetic independence
  distinct; and
- replace the quarantined absolute-gap argument by a legitimate
  cross-completion height comparison.

The final audited source heads are PR #3 `c37e96e`, PR #33 `2cfe250`, and
PR #20 `14f06d2`.  PR #20 moved during this wave from `aa9cf71` to
`14f06d2`: it independently added `R-9409` for the same completion mismatch
recorded locally in `R-9809` and explicitly withdrew `T-9418`--`T-9421`, with
their statements left open.  The `L-9408` and `L-9415` blobs used by the
q-difference claims remained unchanged.

## Delegation and review

- The cap/room lane derived the exact quotient map between three-symbol room
  addresses and four-symbol cap cells, then extracted a computable all-late
  survivor filter.
- The overlap lane factored an arbitrary adjacent-stage block through its
  boundary-incidence group and through one telescoped positive S-unit
  equation.
- The period lane audited two primary q-functional sources and specialized the
  viable finite-place theorem exactly at period one.
- The integrating lane repaired the gap method by applying archimedean height
  only to one finite rational partial sum and the same rational 2-adic value.

Every new theorem received or was assigned a nonauthoring cold review.  The
source-dependent theorem was also checked against rendered pages of both
official journal PDFs, and all live branch heads were refreshed before
integration.  All four claims remain `PROPOSED`.

## New results

### `T-9813` -- room addresses are cap-cell quotients

Write `T_j=2^(11(t_j+1))`, let the three-symbol room modulus be
`M_m=T_1T_2T_3`, and put `C_m=T_2T_3/64`.  For a prefix `(a,b,c)`, the room
address and cap-head correction obey the exact no-wrap identity

```text
rho_m^[3](a,b,c)=X_0(a,b)+64 T_1 upsilon_m(a,b,c),
upsilon_m(a,b,c)=r_m^H(a,b,c,k) mod C_m.
```

The remainder is independent of the fourth symbol `k`.  Restricted to the
sixteen selected cap cells for fixed `(a,b)`, projection modulo `T_3` is
four-to-one, with each fiber equal to one final-symbol quartet.  Thus the
compatible room-prefix/cap-suffix state count is the fiber product

```text
4^3 x_4 4^2 = 4^4 = 256,
```

not the naive Cartesian product 1024.

More importantly, every eventual fixed room eventually lies in the zero
coarse cap cell.  If `A_m(a,b,c)` is the explicit coarse quotient, a prefix
survives only when

```text
A_m(a,b,c) in {0,61,11,63},
```

and that value forces the unique fourth symbol.  If `n_m` counts surviving
prefixes, then

```text
# eventual rooms <= liminf n_m <= 64.
```

Exact checks gave `n_12=5` and `n_13=3`; these audit the decoder only and are
not extrapolated past the unknown eventual onset.

### `T-9814` -- adjacent endpoints form a path-incidence group

For `h` adjacent corrected stages whose boundaries use `s` primes, retaining
all stage equations gives one common scale direction and one prime direction
per boundary vertex:

```text
rank <= 1+(h+1)s.
```

This saves `(h-1)(s+1)` generators over the naive product of `h` one-stage
groups.  After extracting the exact endpoint powers of 2 and 3, the displayed
fresh-prime ambient group has exact rank `1+(h+1)f`.

Composing the recurrences telescopes every internal boundary and produces one
positive `(256h+1)`-term S-unit equation with only the two outer endpoints.
Its fresh-prime ambient rank is exactly

```text
2f+1,
```

independent of `h`.  Chronological overlap likewise leaves only one initial
ternary and one final binary signature, so the coefficient-context count is
`12*4^(256h)`, not `(12*4^256)^h`.

The available quantitative one-equation ESS bound becomes worse for every
`h>=2`, because its dimension constant grows with `256h+1`.  The theorem's
gain is structural: it isolates a path-coupled S-unit theorem as the missing
input, rather than claiming a stronger numerical prime budget now.

### `T-9815` -- period one has a sourced 2-adic independence measure

For a one-letter positive period `(d)`, put

```text
q=(64/81)^(9d),
c=(64/81)^(1+9d),
F(X)=1+c X F(qX).
```

Amou--Matala-aho--Vaananen (2007), Theorem 5.1 applies over `Q` at the
2-adic place with source parameters `m=s=1`.  At `delta=1/2`, the exact source
constants are

```text
beta=(2 sqrt(2086)-7)/79,
gamma=(2/3) log_2 3,
mu=beta/(beta-gamma)=96.859084511... .
```

The strict height window follows from

```text
beta > 16/15 > gamma > 1.
```

Consequently, at every physical rational point `x=(64/81)^(9h)`, the values
`1,F(x)` are Q-linearly independent with the explicit finite-place measure.
The functional equation gives an invertible rational coefficient transform,
so `F(x),F(qx)` are also Q-linearly independent with the same leading
exponent.

The source audit also closes two tempting overextensions.  For every native
period `r>=2` and every allowable source `delta`, the 2007 ratio satisfies
`B/A<19/18<gamma`, so its height condition fails.  The direct order-two
presentation in Matala-aho (2002) fails `B>A` for every period, even after
maximal primitive-content cancellation.  The physical Casoratian from
`T-9812` is not the approximation determinant required by either theorem.

### `T-9816` -- the valid replacement is a relative-gap ceiling

Let

```text
Psi=sum_j (64/81)^(h_j)
```

have infinite binary support and suppose its 2-adic value is the rational
`A/B` in lowest terms.  For the finite partial sum through `h_j`, the exact
2-adic tail valuation is `6h_(j+1)`, while the denominator of the same rational
difference divides `B*81^(h_j)`.  Applying the ordinary real bound only to
that finite rational expression gives

```text
2^(6h_(j+1)) <= (|A|+81B/17) 81^(h_j).
```

With

```text
delta=log_64(81/64)=0.056641667147437458...,
g_j=h_(j+1)-h_j,
```

every rational value therefore satisfies

```text
g_j <= delta h_j + (1/6)log_2(|A|+81B/17).
```

Thus `sup_j(g_j-delta h_j)=infinity` proves 2-adic irrationality.  For a
positive stack with cumulative support `H_j` and next layer length
`ell_(j+1)`, the criterion becomes

```text
sup_j(ell_(j+1)-delta H_j)=infinity.
```

This excludes sufficiently superlacunary directives.  It deliberately does
not reach bounded or periodic increment words, whose relative gaps are far
below the critical line.

## Exact checks and review

- `T-9813`: recurrence orientation, toll cancellation, no-wrap bounds,
  restricted-cell fiber sizes, zero-cell forcing, fourth-symbol uniqueness,
  and the liminf packing step were reconstructed.
- `T-9814`: path-incidence generators, fresh-prime independence, composed
  toll orientation, window counts, signature sharing, scale separation, and
  the `h=1` recovery were independently checked.
- `T-9815`: the official 2007 pages 318--320 and 2002 page 648 were rendered
  and inspected; every source parameter, height ratio, radical constant,
  failed longer-period inequality, and fixed rational height transfer was
  recomputed.
- `T-9816`: denominator divisibility, exact tail unit, numerator lower bound,
  finite real height, logarithmic slope, contrapositive, and stack indexing
  were independently checked against both local `R-9809` and source
  `PR20/R-9409`.

No bounded computation is used as a theorem premise.

Memory remained healthy throughout integration; the final pre-commit snapshot
had 9.71 GiB free with 37.0% of physical memory in use.  The task-local source
PDFs and rendered audit pages were removed after both source reviews passed.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Closed routes and remaining boundaries

- Room addresses and cap cells are aligned, not transverse.  The remaining
  task is asymptotic control of the 64 explicit coarse quotients.
- Adjacent-stage overlap has exact low incidence rank, but the available
  one-equation quantitative theorem cannot exploit it without paying a
  growing term dimension.
- Period-one values have a genuine arithmetic independence measure; the same
  published criterion provably stops at longer native periods.
- Rational binary values obey a sharp relative-gap ceiling, but periodic and
  balanced supports remain below that threshold.

## Files changed

Four theorem files, the source-follow-up note in `R-9809`, the packet
claim/status/verification ledgers, and this append-only report.  No canonical
root ledger or competing branch file is changed.

## Recommended next actions

1. Analyze the explicit coarse quotients `A_m(a,b,c)` as functions of scale;
   a cofinal zero count eliminates every fixed room, while any uniform count
   below 64 sharpens the global bound immediately.
2. Seek a quantitative subspace/S-unit result for a path-coupled system whose
   complexity depends on incidence rank while retaining 257 variables per
   equation.
3. Build a joint approximation family for the residue-class components of a
   period `r>=2` stack; its height ratio must beat the exact
   `(2/3)log_2 3` obstruction.
4. Couple the relative-gap inequality to a centered-carry or ordinary
   numerator recurrence that can lower the critical slope toward periodic
   support.

## Organizational improvement ideas

When a source branch corrects a flaw already found downstream, preserve both
the historical audited head and the corrected live head.  The former makes
the exact dependency failure reproducible; the latter prevents stale status
claims.  For external value theorems, record unsuccessful hypothesis audits
as explicit no-go results so later work does not repeatedly attempt the same
normalization.
