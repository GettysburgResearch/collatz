# Cross-direction lemma forge: wave twelve

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

The remote sweep found new work at the heads of PRs #3, #13, #16, #19,
#20, and #33, together with the unreviewed issue-#24 solution-cone packet.
Four interfaces were selected for a proof-first, memory-light wave:

1. transfer PR #33's factor-greater-than-275 cap height from stage endpoints
   into the 84 internal triple seams;
2. classify the zero-density one-hot avoidance set left open by `L-9896`;
3. test whether the special native period-ten coefficient vector benefits
   from unequal scalar root allocation; and
4. connect the solution-cone extreme rays to the natural-boundary rigidity
   already proved for component colorings.

Routine proof work remained below 32% physical-memory use.  One timed-out
large-integer audit briefly left an orphan Python process; the reviewer
identified and terminated that exact process, after which memory recovered to
21.1% used (12.16 GiB free).  The optimized audit had already completed and no
worker process remained.

## Delegation and proof method

- The cap lane propagated a uniform affine prefix bound to every head, triple,
  and terminal input, then compared each of those canonical inputs
  against its own exact dyadic modulus.
- The centered-survivor lane grouped the short-range delayed events into
  blocks of `m+1`, counted the surviving children in every parent cylinder,
  and separated formal `2`-adic avoidance from valid ordinary depths.
- The Pade lane returned to the arbitrary allocation product of
  `PR20/L-9411`.  It ordered every active phase and every later block by an
  exact `2`-adic exponent rather than optimizing the worst phase in
  isolation.
- The integrating lane independently reconstructed the fixed-cone extreme
  rays and the finite-period affine commutator, then applied the standard
  Polya--Carlson dichotomy only after proving radius one and nonrationality.

Each theorem was routed to a nonauthoring mathematical reviewer.  The source
heads were treated as branch-qualified proposed interfaces, not as promoted
facts.

## New results

### `L-9821` -- cap cusp localization

Every hypothetical cap-correction chain has an explicit uniform prefix bound

```text
log_2(z_(m,j)+2)
 < alpha_j 2^m + (1024/41)m + K_M.
```

At all 84 triple starts this lies below half of the triple-cylinder depth by

```text
(29955/20992) 2^m - O_M(m).
```

Thus every canonical triple correction is eventually below the square root
of its modulus: more than half of its padded high bits are zero.  The head
and terminal inputs have separate linear high-zero gaps.  This creates exact
256-head and 1024-triple cusp filters which inspect the canonical input and
therefore avoid `L-9898`'s nonautonomous odd-output carry.  It is a necessary
condition and lower-bound target, not an all-scale cap exclusion.

### `R-9806` -- the one-hot exceptional Cantor set

Fix a suffix horizon `m` and put `R=64^(m+1)`.  In every aligned parent phase,
between

```text
B=(62R+1)/63
```

and `R-1` children avoid the next block of `m+1` delayed one-hot events.  The
formal all-delay avoiding set is therefore perfect and uncountable, has Haar
measure zero, and obeys

```text
log(B)/log(R)
 <= dim_H(C_(m,v))
 <= upper_box_dim(C_(m,v))
 <= log(R-1)/log(R) < 1.
```

Spaced delays give an exact one-forbidden-child tree.  The number of ordinary
exposing parameters below `T` with fewer than `s` valid delayed competitors is

```text
O_(m,v,s)(T^d (log T)^(s-1)),
d=log(R-1)/log(R)<1.
```

Potential one-hot global-promotion depths are consequently `O(X^d)`.  The
result refutes an all-formal-phase proof using delayed one-hot words alone;
it does not prove that the formal Cantor set contains an ordinary integer.

### `R-9807` -- exact special-vector allocation ceiling

For arbitrary scalar phase allocations `n_j`, write `D=sum n_j`,
`s=min n_j`, and let `j_*` be the least phase with allocation `s`.  The summed
native coefficient has exactly `s` zero blocks.  Every subsequent coefficient
is nonzero, and the unique least-valuation term in the full evaluated error is

```text
(j_*,N_*) with N_*=D+s.
```

Its closed endpoint exponent is

```text
K_r(D,s,j)
 =[rN(N-1)+2jN-r^2s^2-rs-2rsj-j(j+1)]/2.
```

Consequently the actual special-vector allocation functional is

```text
[1+2p-(r-1)p^2]/[1+sum p_j^2],
p=min p_j,
```

and is uniquely maximized by equal allocation.  At period ten the best raw
scalar-root benchmark is `0.954998217905888...<1`.  Unequal allocation cannot
exploit the dimension-ten gap of the imported Vaananen--Wallisser theorem;
the remaining routes are genuinely coupled systems or quadratic reduced-
height savings.

### `L-9899` -- analytic classification of solution-cone rays

The nonnegative fixed cone of the shortcut pullback consists exactly of
bounded nonnegative assignments to weak components, and its extreme rays are
the component indicators.  Every positive component is infinite.  An
elementary period reduction followed by

```text
A(x)=2x,
B(x)=3x+1,
(A B A^(-1)) B^(-1)(x)=x+1
```

proves that an eventually periodic positive component indicator is constant.
Polya--Carlson then yields the exact ray dichotomy:

```text
C=positive integers  -> f_C(z)=z/(1-z),
C proper             -> the unit circle is a natural boundary.
```

Hence Collatz is equivalent to continuation of the distinguished `C_1`
series through even one nonempty boundary arc.  Equivalently, the number of
rational extreme rays is two if Collatz holds and one if it fails.  This is a
sharp analytic reformulation and target, not a proof of continuation.

## Exact checks and review

- The cap prefix coefficient and all four endpoint gaps were replayed in
  exact rational arithmetic.  The 84 triple starts are exactly
  `2,5,...,251`; the exceptional terminal height enters only at `j=254`.
  A nonauthoring reviewer additionally checked all 256 stabilized head words
  at `m=12` against both sequential local divisibilities and nonnegative
  canonical outputs.
- The first survivor block at `m=1,v=0` has between 4032 and 4095 surviving
  children in each root phase, against the theorem's uniform lower bound
  4031.  The exact event sizes and every threshold agree.
- The Pade exponent replay covered 21,837 nonzero allocation vectors with
  `1<=r<=7` and `0<=n_j<=3`.  It matched the zero window, phase ordering,
  global endpoint, and closed exponent.
- The component-coloring quotient graph was connected for every modulus
  through 500, agreeing with the period-reduction proof.
- All four claims have balanced displays, unique tags, explicit source and
  gap audits, and no generated artifact dependency.  Each received a clean
  nonauthoring cold review; no mathematical correction was required.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Closed routes and remaining boundaries

- Low-bit cap seams are not the only finite interface.  Completion height
  supplies a carry-free high-zero input filter, but a uniform lower bound for
  the 256 head corrections is still missing.
- Delayed one-hot competitors are generic with a power-saving exceptional
  count, yet their formal avoiding set has positive dimension.  Two-hot or
  more general block-zero words are needed for a uniform cover.
- Special-vector scalar reallocation is now closed at every period.  Period
  ten still permits Hermite--Pade coupling, adjacent determinants,
  resultants, and reduced-height savings.
- A natural boundary classifies every proper positive component ray, but the
  desired analytic continuation of `f_(C_1)` is itself equivalent to the
  conjecture.  Ambient operator spectra alone do not supply it.

## Files changed

Four claim files, the claim/status/verification ledgers, and this append-only
wave report.  No canonical root ledger or competing branch file is changed.

## Recommended next actions

1. Prove a lower bound for each stabilized head correction
   `[-F_H P_H^(-1)]_(Q_H)` along scale classes and compare it with the
   `L-9821` cusp exponent.
2. Add two-hot zero-block events to the `R-9806` child tree and determine
   whether positive branching survives on ordinary parameters.
3. Move the period-ten construction outside a single scalar root product:
   test a small Hermite--Pade system or an evaluation resultant while tracking
   reduced height explicitly.
4. Attack one explicit boundary arc of `f_(C_1)` using the exact component
   functional equation; any claimed regularity must apply to the binary
   extreme ray itself, not only to an ambient weighted space.

## Organizational improvement ideas

Every density-one obstruction should report the geometry and counting rate of
its exceptional set.  Completion-height theorems should be propagated to
internal interfaces before invoking global transcendence machinery.  For
special-vector Pade problems, the valuation of the summed vector should be
computed before optimizing individual phases.  These conventions exposed the
true next variables in all four lanes.
