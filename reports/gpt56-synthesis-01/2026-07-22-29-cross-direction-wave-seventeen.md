# Cross-direction lemma forge: wave seventeen

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

Wave sixteen exposed three exact next questions:

- can the 64 cap/room coarse quotients close under scale doubling, or do their
  truncated inverse powers require genuinely growing state;
- can a longer periodic stack be reduced to period-one value problems without
  silently assuming that separate irrational values cannot cancel; and
- what global support-density consequences follow from the valid relative-gap
  height inequality, both for `64/81` and for the new PR #35 `4/5` chart.

The final audited source heads are PR #3 `c37e96e`, PR #20 `14f06d2`, PR #33
`2cfe250`, and PR #35 `6bb647a`.  The wave uses only exact finite-rational,
2-adic, and q-functional arguments; no large computation is a premise.

## Delegation and review

- The cap lane derived the full inverse-lift recurrence, its Newton defect,
  and the exact information lost by the six-bit projection.
- The period lane decomposed an arbitrary periodic stack by coefficient
  residue class and audited scalar versus joint finite-place theorems.
- The completion lane generalized the first-omitted-term height argument to a
  bounded-digit `p^a/Q` theorem, then iterated it into local support counts and
  stack/directive growth ceilings.

The period and completion claims were cross-reviewed by the other lane.  The
integrating agent cold-reviewed the cap claim, independently replayed its full
precision transition, repaired one malformed coset display, and narrowed its
information-loss wording so it does not deny the computable distinguished
base-3 recurrence.  All three claims remain `PROPOSED`.

## New results

### `T-9817` -- the cap quotient needs a growing Newton carry

Let `u_m` be the inverse of the first three odd head multipliers modulo the
dyadic width `2^(L_m)`.  Exact schedule arithmetic gives

```text
E_m=5397*2^(m-8)+21,
L_m=2849*2^(m-8)+17.
```

After normalization

```text
g_m=3^21*3^(-E_m)=1+2^(m-6)q_m,
```

LTE and scale doubling give an exact 2-adic isometry:

```text
q_(m+1)=q_m+2^(m-7)q_m^2,
v_2(q_infinity-q_m)=m-7.
```

For the canonical inverse defect

```text
epsilon_m=(3^(E_m)u_m-1)/2^(L_m),
```

the next inverse is

```text
u_(m+1)
 =[3^21 u_m^2(1-2^(L_m+1)c_m)] mod 2^(L_(m+1)),
c_m=epsilon_m mod 2^(Delta_m),
Delta_m=L_m-18=2849*2^(m-8)-1.
```

The carry is computable for the distinguished source, but its width grows
exponentially.  Across all full 2-adic lifts compatible with the entire
current inverse residue, the isometry preserves `2^(Delta_m)` possibilities.
On each nonzero third-symbol lane the next offsets fill a full coset modulo
`2^(L_m+1)`; even with the next base cell held fixed, their top six bits take
all 64 values equally often.

This is an information-loss theorem, not branching of the actual base-3
sequence.  It closes the natural 64-state projection route and says exactly
what a successful recurrence must add: the growing source defect or a proved
correlation with the base-cell carry.

### `T-9818` -- periodic phases are formally independent

For a positive period word of length `r`, the native equation

```text
F(X)=P(X)+cX^rF(qX)
```

has the exact residue decomposition

```text
F(X)=sum_(j=0)^(r-1) p_j X^j E_Q(cq^jX^r),
Q=q^r,
E_Q(Z)=sum_(k>=0) Q^(k(k-1)/2) Z^k.
```

The `r` arguments lie on distinct multiplicative `Q`-orbits.  More strongly,
`1` and every subset of the functions `E_Q(cq^jY)` are linearly independent
over `Q(Y)`.  After clearing a hypothetical rational-function relation, its
large coefficients are an exponential polynomial with distinct bases
`cq^jQ^(-ell)`; a Vandermonde determinant forces every coefficient to vanish.

Amou--Matala-aho--Vaananen (2007), Theorem 5.1 applies to each phase
separately and gives the same explicit scalar exponent
`96.859084511...` as `T-9815`.  Applied to any joint subset of `k>=2` phases,
all nonnumeric hypotheses hold, but for every auxiliary parameter

```text
B/A < 19/18 < (2/3)log_2 3,
```

so its height window fails.  Combining this with PR #20's independently
sourced nine-phase theorem shows that any arithmetic relation must use at
least ten phase coefficients.  The first open case remains the prescribed
period-ten cancellation vector, not individual phase irrationality.

### `T-9819` -- rational supports are multiplicatively syndetic

Let `T=p^a/Q` with `Q>p^a`, `p` not dividing `Q`, and consider

```text
Psi=sum_j c_j T^(h_j)=A/B in Q_p,
```

where the nonzero integral digits are bounded and their `p`-adic orders lie
in a band of width strictly below `a`.  The first omitted term is then the
unique least-valuation tail term.  With

```text
K=|A|+DBQ/(Q-p^a),
alpha=log_(p^a) Q,
delta=alpha-1,
```

one gets

```text
p^(a h_(j+1)+v_p(c_(j+1))) <= K Q^(h_j),
h_(j+1) <= alpha h_j+C.
```

Writing `rho=C/delta`, exact iteration yields

```text
h_(j+n) <= alpha^n(h_j+rho)-rho.
```

If `N(X)` counts support positions at most `X`, then every rational value
satisfies the local count

```text
N(Y)-N(X)
 >= floor(log_alpha((Y+rho)/(X+rho))).
```

Thus every interval `(X,alpha X+C]` contains support and

```text
liminf N(Y)/log Y >= 1/log(alpha).
```

For binary `64/81` this constant is `18.1502565060...`; the theorem also gives
explicit exponential ceilings for positive-stack increments.  For the exact
PR #35 `4/5` chart, every hypothetical positive ordinary survivor has

```text
liminf N(Y)/log Y >= 1/log(log_4 5)
                         = 6.70013449289...,
```

with the sharper finite gap constant `log_4(5(x+3))` for seed `x`.  A signed
two-digit cancellation example at valuation-band width exactly `a` proves
that the strict band hypothesis is necessary for this mechanism.

## Exact checks and review

- `T-9817`: schedule exponents, LTE normalization, isometry, limit valuation,
  Newton lift, carry width, lift-fiber cardinality, coset spacing, and uniform
  six-bit counts were reconstructed.  Full-width arithmetic at `m=12 -> 13`
  independently verified both the canonical inverse formula and the
  full-precision `q` recurrence.
- `T-9818`: coefficient indexing, orbit separation, the polynomial-clearing
  Vandermonde proof, scalar source parameters, the all-auxiliary joint
  obstruction, and the PR #20 nine-phase implication were cold-reviewed
  against the official 2007 source pages.
- `T-9819`: the valuation-band unique minimum, denominator direction, finite
  real height, affine induction, local-count endpoints, stack indices, PR #35
  normalization, finite-support contradiction, constants, and sharpness
  example were independently checked.

Memory remained healthy; the final integration snapshot had 9.64 GiB free with
37.5% of physical memory in use.  Task-local rendered source pages were
removed after review.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Closed routes and remaining boundaries

- The six-bit cap quotient is not a closed scale state.  The actual source
  carry remains computable, but any bounded projection must exploit a new
  correlation with the base cell.
- Longer-period stack functions have full formal phase rank and every phase
  has a quantitative scalar measure.  Period ten remains an arithmetic
  cancellation problem involving at least ten phases.
- Rational bounded-digit supports cannot be too lacunary at any
  multiplicative scale.  The logarithmic lower bound is necessary, not
  sufficient, and periodic/balanced stack directives remain allowed.

## Files changed

Three theorem files, the packet claim/status/verification ledgers, and this
append-only report.  No canonical root ledger or competing branch file is
changed.

## Recommended next actions

1. Derive the connector/base-cell analogue of the Newton defect in `T-9817`
   and test whether its top carry cancels or correlates with `c_m`.
2. For minimal period ten, approximate the prescribed ten-phase coefficient
   vector directly; separate scalar approximants cannot rule out its one
   cancellation.
3. Combine `T-9819`'s local support count with a physical finite-state or
   factor-complexity upper bound.  In the `4/5` chart, any grammar forcing
   fewer than `6.7001...` support points per logarithmic scale excludes every
   positive ordinary survivor.

## Organizational improvement ideas

Negative state-closure theorems should name the information model precisely:
an actual arithmetic source may have a computable high carry even when no
bounded projection retains it.  For decomposed value problems, record formal
function rank, individual value irrationality, and joint arithmetic rank as
three separate layers; none substitutes for another.
