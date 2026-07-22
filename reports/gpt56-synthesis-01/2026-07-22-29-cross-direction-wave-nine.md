# Cross-direction lemma forge: wave nine

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

This wave began from fresh source audits of the active H, centered-survivor,
cap-chain, Pade, and collision branches.  The audited heads were PR #19 at
`e8e2d0a`, PR #16 at `f800597`, PR #33 at `2cfe250`, PR #20 at `2362802`,
and PR #3 at `f274dfe`.  The goal was to replace four broad bottlenecks by
exact local statements that another direction can use immediately:

- quantify what remains after the known Pade root-product cancellation;
- identify and realize the survivor block-zero exposure condition;
- compress the 256-cell cap chain to its true inter-scale state;
- repair the H ghost boundary and expose exact dual renewal coordinates.

## Approaches and delegation

Three independent proof agents were assigned separate mathematical lanes and
reassigned harder follow-ups after each success.  One lane developed centered
renewal digits, then classified all legal predecessor phases and reviewed the
Pade calculation.  A second collapsed cap chains to their collar joins, then
derived the Hensel stitch isometry and reviewed both cap claims.  A third
repaired the full H ghost boundary, then proved the room/entrance renewal
bridge and reviewed both H claims.  The integrating lane derived the Pade
post-window exponent law and audited every imported dependency against the
fresh branch heads.

Each result was split into an atomic claim with hypotheses, proof, explicit
scope boundary, dependency map, and next target.  Cold review was performed
after the claims were written, not only on the agents' proof sketches.

## New results

- `L-9884` proves exact post-window phase dominance for the PR #20
  root-product cancellation.  Once `N >= D+n_max`, every phase above phase
  zero has a strictly larger 2-adic exponent, so cross-phase cancellation is
  impossible.  In equal allocation the remaining tail is an explicit
  quadratic.  If the raw height is optimistically left unchanged, period four
  needs only a relative linear-depth gain exceeding
  `0.064346439346...`; this is a benchmark, not a gcd bound.
- `L-9885` identifies centered block digits exactly with the renewal digits of
  the ordinary representative.  The block is zero precisely when that
  representative survives unchanged, giving an exact nested-sieve and
  plateau criterion and converting one-hot exposure into a renewal-lifetime
  inequality.
- `L-9886` classifies every legal `k`-step predecessor history of a one-hot
  survivor into `2^(k-1)` distinct depth phases.  The all-one history occurs
  exactly when `n = 1 mod 4*3^(4k-2)` and yields arbitrarily long lower
  renewal lifetime. CRT therefore gives unbounded lower renewal lifetime
  across the exposing depths of every fixed terminal suffix.
- `L-9887` proves that every sufficiently late 256-cell PR #33 cap chain has
  zero join quotients at both internal cuts.  Its 252-cell middle is therefore
  attached only through two exact collar equalities, reducing the relevant
  inter-scale problem to two stitch states.
- `L-9888` writes each collar mismatch as the unique canonical equation
  `s+Na=r+Qb`, proves its bit-by-bit Hensel recurrence and exact truncated
  2-adic isometry, and gives an exponential generic section lower bound for
  the inverse stitch map.  This lower bound is deliberately scoped to
  unrestricted inputs until bridge reachability is proved.
- `L-9889` repairs the boundary used in PR #19: the ghost boundary contains
  every iterated image of zero, not only the outer points.  All such points
  are nonpositive, so the stabilized positive section remains valid. On the
  specifically defined compact nonzero section `Hbar`, termination is now
  equivalent to divergence of the minimum ordinary representative at
  precision `K`.
- `L-9890` proves a room-to-entrance bijection for H blocks, exact dual
  `v_2=2L` and `v_3=L` renewal valuations, and an integral sign law for the
  normalized renewal coordinate.  Along an assumed infinite chain, the
  normalized coordinate converges directly to `Q_infinity/4`, allowing the
  post-Yu bounds to be restated simultaneously in room, valuation, and
  renewal coordinates.

## Independent checks and corrections

- The `L-9884` coefficient-exponent identity was replayed in 864 exact cases
  (`r<=8`, `n<=12`, `ell<=8`).
- Every legal predecessor history through depth three was enumerated and
  matched to `L-9886`; all seven histories passed.
- All cap exponents and three collar gaps were recomputed as exact rational
  numbers from the frozen source formulas.
- A cold review rejected the draft implication `b=0 iff d=0` in `L-9888`.
  The final claim retains the valid `a=0 iff d=0` statement and proves the
  separate exact condition `b=0 iff d>=0 and N divides d`.
- The H review restored the empty-word boundary point, distinguished finite
  CRT realization from an infinite chain, and corrected the source dependency
  for the normalized limit.
- Every display delimiter in `L-9884`--`L-9890` was mechanically balanced,
  and the complete patch passed `git diff --check`.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Failed or incomplete routes

- The survivor predecessor family gives unbounded block-zero exposure but
  does not yet order all positive competing blocks above the exposed point;
  global minimum/successor promotion remains open.
- Generic Hensel stitch complexity does not imply that the 252-cell cap
  bridge reaches those states.  A scale-to-scale stitch recurrence is still
  needed.
- Finite CRT universality of H rooms does not make successive rooms compatible
  and does not construct an ordinary infinite H orbit.
- The 6.4346% Pade benchmark holds only for unchanged raw height.  Quadratic
  gcd savings, adjacent Casoratians, and unequal transition allocations are
  not bounded by this wave.

## Files changed

Seven claims `L-9884`--`L-9890`, the claim/status/verification ledgers, and
this append-only report.

## Recommended next actions

1. Compute the adjacent Pade Casoratian in the post-window range and compare
   its exact height loss with the 6.4346% linear-depth benchmark.
2. Classify the non-all-one survivor predecessor phases and control the first
   positive block above an exposed one-hot representative.
3. Derive the small-modulus stitch-state recurrence through the 252-cell cap
   bridge; only then test whether the generic Hensel section lower bound is
   dynamically reached.
4. Impose compatibility between successive H renewal variables `W_k`, seeking
   a dual logarithmic form that combines the exact `v_2/v_3` bridge with the
   post-Yu discounted budget.
5. Update the PR #19 source wording for the full ghost boundary so downstream
   arguments no longer inherit the outer-boundary shorthand.

## Organizational improvement ideas

Use the claim packet as the canonical cross-branch interface: exact theorems
in claim files, finite audits in `VERIFICATION.md`, and chronological
integration decisions in reports.  Any state-complexity statement should name
its input universe (`unrestricted`, `bridge-reachable`, `prefix-cylinder`, or
`global`) in the theorem sentence itself.
