# Cross-direction lemma forge: wave thirteen

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

The remote sweep materially changed three source frontiers during this wave:

- PR #16 advanced to `1bb8c6b`, adding a bounded-distortion morphic
  recurrence bridge and sharpening the explicit Thue--Morse square witness;
- PR #20 advanced to `ed1ee9d`, exposing the period-ten special-vector target,
  scalar Tschakaloff approximants, one-phase elimination, and an optimistic
  adjacent-order ceiling; and
- PR #3 advanced to `3ee981e`, adding scaled-tail S-unit and fixed-room
  constraints for the collision/padding program.

The current packet selected four proof targets from the PR #16, #20, and #33
interfaces, plus a dependency audit prompted by a suspicious multiplier
identity.  The goals were to replace vague symbolic-complexity language by a
finite certificate, shrink the cap-head search, test the first multi-hot
survivor obstruction, and decide whether sparse scalar Pade orders evade the
adjacent-order ceiling.

## Delegation and review

- The ordinary-complexity lane derived a repeated-factor divisibility bound
  and a uniform-morphism language certificate.
- The cap-head lane isolated the fourth-symbol dependence in the exact frozen
  connector algebra.
- The survivor lane added adjacent two-hot events to the one-hot exposure
  tree and computed their exact correlation.
- The integrating lane generalized the scalar Casoratian algebra to arbitrary
  sparse order sets and audited the submitted four-phase `3/2` bridge.

Every constructive theorem was routed to a nonauthoring cold reviewer.  The
source refutation was independently checked for arithmetic, logical scope,
and dependency propagation.  Source branches remained branch-qualified and
all new claims remain `PROPOSED`.

## New results

### `T-9801` -- finite complexity certificate for equality languages

For every coprime expanding binary chart

```text
M A_(n+1)=N A_n-(N-M)e_n,
A_n>=2,
```

equal length-`ell` factors at starts `r<t` force

```text
M^ell | A_t-A_r,
ell < log_M(N/M)t + log_M A_0.
```

Consequently

```text
p_e(ell)
 >=1+max(0,floor((ell-log_M A_0)/log_M(N/M))),
liminf p_e(ell)/ell >= log M/log(N/M).
```

At `M=64,N=81` the slope is

```text
17.6548475770... > 16.
```

Cold review found that this complexity floor already appears on PR #20 in
`T-9402`, `T-9405`; the claim now records it as an independent recurrence-
level reconstruction rather than a new barrier.  The new contribution is a
finite whole-language test: if `x` is fixed by an `L`-uniform morphism and
`B=p_x(L+1)`, every point in its coded orbit closure satisfies
`p(n)<=Bn`.  Thus `B<17.6548...` excludes the entire equality subshift from
ordinary `64 -> 81` itineraries.  In particular, every binary 2- or 3-uniform
orbit closure is excluded.  Applying this to a rational-base source theorem
still requires its exact critical constant and equality classification.

### `T-9802` -- rigid final-symbol cells in the cap head

For every stabilized scale `m>=12`, fix the first three head symbols and vary
the fourth.  The exact connector formulas give

```text
r_k=[r_0+kappa_k Q/64]_Q,
kappa=(0,3,53,1).
```

The four corrections share one within-cell remainder.  Hence at most one is
below any threshold `H<=Q/64`, and at least three are at least `Q/64`.  Across
the 256 head words this proves the uniform bound

```text
at least 192 corrections >= Q/64
                         =2^((5687/256)2^m+16).
```

Under the conditional cusp hypothesis of `L-9821`, every sufficiently late
cap stage therefore has at most 64 admissible head words, with at most one
fourth symbol per three-symbol prefix.  The unresolved object is the common
within-cell remainder; it may still vanish, so no cap chain is excluded.

### `T-9803` -- adjacent two-hot correlation and finite-template limit

The adjacent two-hot representative differs from the one-hot representative
by the exact odd unit

```text
1+64/81=145/81.
```

Both events retain the complete exposed lower phase.  Their same-delay
intersection is exact: simultaneous membership reduces to

```text
81y=145x,
x=81 ell,
y=145 ell,
```

and its relative size tends to `1/145`.  Grouping `m+1` delays into a block
with `R=64^(m+1)` leaves at least

```text
B_2=(61R+2)/63
```

children per parent for the joint one-/two-hot avoidance tree.  More
generally, any fixed library of at most 62 normalized bounded-support
templates leaves at least

```text
B_q=R-q(R-1)/63 >= (R+62)/63 >=66
```

children.  Its formal avoiding set is therefore perfect, Haar-null, and
positive-dimensional.  This closes another small-template covering route:
the next attack needs an unbounded delay-growing family, all two-hot gaps, or
additional arithmetic.  Formal dimension still says nothing about ordinary
integer membership.

### `T-9804` -- sparse scalar orders are strictly worse

For arbitrary increasing Pade orders `t_i` and coefficient columns `c_j`, the
minor `det(g_(t_i,c_j))` has a unique reverse tropical term at 2 and a unique
identity term at 3.  Every sparse minor is therefore nonzero.  The canonical
cofactor coupling still cancels exactly `q-1` extra blocks.

At fixed largest order `t_*` and width `q`, put

```text
delta_i=t_*-(q-1-i)-t_i >=0.
```

Its evaluated normalized 2-adic accuracy is the consecutive-order value
minus exactly

```text
54 S r sum_i delta_i.
```

Thus consecutive orders uniquely maximize accuracy in this scalar family;
every skipped order loses a quantified amount before any height cost is
charged.  Refreshed `PR20/R-9407` already places the optimistic adjacent-order
benchmark below one at period ten, so sparse selection cannot evade it.  The
remaining live routes in `PR20/Q-9413` are genuinely coupled Hermite--Pade or
two-dimensional `q`-difference constructions, one-phase elimination, and
global reduced-height savings.

### `R-9808` -- the submitted four-phase `3/2` bridge is invalid

`PR16/L-9312` uses

```text
81/64=(3/2)^4,
```

but in fact

```text
(3/2)^4=81/16=4(81/64).
```

There is no integer `k` with `(3/2)^k=81/64`.  For the submitted definition
`Y_m=xi(3/2)^m`, the exact sample is

```text
Y_(4n+r)=4^n(3/2)^r(B_n+u_n),
```

so both the centers and radii used by the fixed four-phase proof acquire the
growing factor `4^n`.  A multiplicatively correct decomposition is instead

```text
(3/2)^4(1/2)^2=81/64,
```

which is a new six-step mixed schedule, not one full `3/2` orbit.

The refutation quarantines the proof and schedule wording in `L-9312` and its
explicit dependents.  It does not refute the direct-`81/64` centered
recurrence, the residue table, or the locally restarted phase checks in
`X-9304`; those survive only subject to their own dependency audits.  Nor does
it assert that the conditional schedule conclusion is logically false if its
hypothesis is empty.

## Exact checks and review

- `T-9801`: both divisibility and floor endpoints were rederived; the exact
  threshold uses `3^32<2^51`.  All 80 bounded prolongable binary uniform
  presentations of lengths two and three passed a language sanity replay.
- `T-9802`: the inverse residues `35`, `9`, and product `59 mod64` reproduce
  `(0,3,53,1)`.  Full 256-word replays found 251 large corrections at `m=12`
  and 253 at `m=13`, with no zeros; the theorem uses only the uniform 192.
- `T-9803`: exact representative, permutation, phase-retention, intersection,
  and child-range checks passed at the first two bounded scales.  A
  three-template replay stayed above its symbolic union-bound floor.
- `T-9804`: exact tests covered 1,700 arbitrary minors through width four,
  100 cofactor chains, nine sparse systems, and the `q=2,r=1` edges.
- `R-9808`: two reviewers independently checked prime exponents, the missing
  `4^n`, transported centers/radii, the mixed product, and the source-path
  dependency scope at PR #16 head `1bb8c6b`.

Routine memory remained healthy; the final integration snapshot was 28.7%
used with 10.98 GiB free.
One deliberately broad exact Pade replay timed out and left its exact Python
child process alive; that identified process was terminated before the
bounded replacement audits were run.  No unknown process was touched.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Closed routes and remaining boundaries

- Low-complexity equality languages are now finitely screenable, but the
  rational-base source theorem and equality classification remain unaudited.
- The cap head shrinks from 256 to at most 64 candidates; the within-cell
  remainder, exact zero, and all-scale cap contradiction remain open.
- One-hot plus adjacent two-hot events still leave a positive-dimensional
  formal set.  Any finite library with at most 62 bounded templates is
  structurally insufficient.
- Sparse scalar Pade orders cannot beat consecutive ones at fixed width and
  top order.  Reduced-height and non-scalar coupling remain open.
- The pure four-phase `3/2` bridge is invalid.  Future source work must stay
  in the native `81/64` recurrence or derive a correct mixed schedule.

## Files changed

Five claim files, the packet claim/status/verification ledgers, and this
append-only wave report.  No canonical root ledger or competing branch file
is changed.

## Recommended next actions

1. Acquire and audit the exact rational-base nearest-integer source theorem;
   compute the finite equality-language certificate without the invalid
   `3/2` schedule.
2. Analyze the 64 cap-head within-cell remainders and seek one uniform
   exponential lower bound or exact nonzero classification.
3. Replace fixed survivor templates by all two-hot gaps or a delay-growing
   library, keeping ordinary and formal parameters separate.
4. Attack `PR20/Q-9413` through its one-phase measure inequality or the native
   two-dimensional triangular `q`-difference system.
5. In the next wave, use PR #3's new scaled-tail S-unit and fixed-room bridge
   to seek a quantitative fresh-prime/adelic-room lemma.

## Organizational improvement ideas

Every source audit should verify the elementary multiplier identity before
propagating a literature bridge.  Novelty review should compare remote claim
heads as well as local packet files; that check correctly reclassified the
complexity floor while preserving its new finite-language corollary.  Finally,
every finite-template covering argument should state how its template count
scales with delay, because fixed libraries can leave large formal trees even
when each individual event has positive density.
