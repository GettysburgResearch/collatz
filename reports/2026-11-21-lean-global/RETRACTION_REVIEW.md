# Scoped independent review: inverse extension and normalization

**Verdict: VERIFIED at the named theorem scope.** Reviewer: the separate
`lean_kernel` lane. The reviewer did not author `Retraction.lean`. This
verdict is an internal mathematical reconstruction plus actual Lean
execution, not external referee acceptance or a proof of Collatz.

## Frozen object

- Path: `research/lean-global-20261121/lean/CollatzGlobal/Retraction.lean`.
- SHA-256: `5a84720b3e248a5a7e0928d3186564db949a4910c7752025c9b34c0a585ceae4`.
- Dependency interface inspected: `BalancedFive`, `FiniteResidual`,
  `lastReturn`, `residualSource`, `residualClock`, and their actual-orbit
  composition/maximality laws in `OrbitLift.lean` and `AdaptiveDescent.lean`.
- Related scope comparison: `Forcing.lean`, SHA-256
  `542b23ebd0878e073e2ffd5717ab841feadd5e2431b6fdb0d18993a80b069d77`.

The verdict does not extend automatically to later source hashes.

## Reconstructed argument

Let an actual balanced pair starting at `n,5n` return at clock `s` to
`q,5q`, with equal odd counts. Let `FiniteResidual q d` mean that there
is no further positive balanced return from `q` in the finite window
`1,...,d`.

1. **Suffix cancellation.** At a later clock `s+t`, equality of total
   odd counts cancels the equal prefix counts. Equality of the endpoint
   ratio cancels the supplied actual prefix using ordinary orbit
   composition. This gives the exact equivalence between a return from
   `n` at `s+t` and a return from `q` at `t`. Neither direction replaces
   pointwise equality by a whole-cylinder claim.
2. **Last-return identity.** Clock `s` is a candidate return, so the
   maximal return through `s+d` is at least `s`. If it were larger, suffix
   cancellation would produce a forbidden positive return from `q`
   at a clock at most `d`. Hence the last return is exactly `s`.
3. **Exact retraction.** The normalized source is therefore `q`, and
   the remaining clock is `(s+d)-s=d`. This is equality of both components
   of the source/clock state, not a bound on them.
4. **Rank consequence.** A rank that is a function of that source/clock
   state returns to its original value after inverse extension followed
   by complete normalization. Strict decrease on both steps would create
   a directed two-cycle. A well-founded relation has no such cycle; the
   proof uses its actual well-founded induction principle.

`no_wellFounded_rank_both_ways` therefore holds for any target sort and
any well-founded relation, not only natural ranks or a fixed lexicographic
order. The map being ranked is explicitly `rank : Nat → Nat → α`.

## Required interpretation limits

The finite residual predicate does **not** include a hit-to-one assertion.
The retraction theorem is valid without one. To interpret `(q,d)` as a
terminating certificate, supply `orbit q d=1` separately; composition then
gives `orbit n (s+d)=1`. Neither first-hit minimality nor absence of returns
after `d` is needed or asserted.

The result also permits `s=0` or `d=0`. Those boundary cases obey the same
identity and are not hidden exceptions. It does not require the incoming
source to be smaller or larger than its endpoint.

**The excluded rank depends only on the ordinary source and remaining
clock.** A state containing additional phase, history, side conditions,
an auxiliary proved invariant, or an independently changing obligation is
not identified by this theorem. Nor does the theorem exclude a procedure
where one of the two operations increases rank, or where the next operation
is not this complete last-return normalization. It would be an overstatement
to infer that all mixed forward/backward proof procedures are impossible.

## Separation from the inverse-cover results

`certified_units_inverse_minimal` in `Forcing.lean` produces arbitrarily large
**certified odd ternary units** with no smaller ancestor **in that same
certified-unit domain**. It does not assert absence of all smaller integer
ancestors, and it does not assert that the exhibited points are actual
five-comparison failures.

Consequently that theorem rejects a total unit-preserving inverse selector
on the whole certified-unit domain with finitely many exceptional bases.
It does not, by itself, reject a selector defined only on actual failure
states, or a method with infinitely many independently solved base families.
The retraction theorem addresses a different precise mechanism: attempting
to gain a strict rank decrease by inverse extension followed by this exact
normalizer. Its identity holds even when the dictionary of incoming words
is unbounded.

## Checks actually run

The development facade was updated to import `Retraction.lean`; without
that import the new theorem was not included in the facade build. A full
`lake build` then passed **13 jobs** using Lean 4.34.1.

A separate import-based audit ran with `-DwarningAsError=true` and returned:

```text
balanced_five_suffix_iff: [propext]
lastReturn_of_residual_endpoint: [propext, Quot.sound]
normalize_inverse_extension: [propext, Quot.sound]
wellFounded_no_two_cycle: no axioms
no_wellFounded_rank_both_ways: [propext, Quot.sound]
```

There is no `sorryAx`, added mathematical axiom, or unproved global closure
assumption in these theorem dependencies. Separately, the facade's
`collatz_iff_finite_psi_residual` is an **equivalence with the explicit open
proposition** `ResidualPsiClosure`; importing or auditing it does not provide
an inhabitant of that proposition and does not prove Collatz.

A duplicate public `oddCount_add` declaration was removed from the ladder
module, which now imports the shared theorem from `AdaptiveDescent.lean`.
The module dependency graph remains acyclic, and a declaration-name scan
found no further duplicates among the new modules.

These are local development executions. The final exact-commit clean-checkout
receipt is a separate publication event and is recorded by the parent lane.
