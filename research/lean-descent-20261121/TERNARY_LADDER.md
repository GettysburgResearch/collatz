# An unbounded ordinary ladder for the budget induction

**Lean-checked; the universal cover remains open.** This is a positive rule for
the fixed-source half-budget programme. It is not a finite residue census.
Both block lengths below are arbitrary natural numbers.

## Exact path and resource transfer

Let positive `v` and nonnegative `r,s,u` satisfy

\[
 3^s v=4^r u+2,\qquad 2^{s+2r}<3^{s+r}.
\]

Set

\[
 x=2^s v-1,\qquad q=3^r u+1.
\]

There is an actual ordinary shortcut path from `x` to `q`:

\[
 2^s v-1 \xrightarrow{\ s\text{ odd steps}\ }3^s v-1
 =4^r u+1
 \xrightarrow{\ r\text{ valuation-two steps}\ }3^r u+1.
\]

The second arrow costs `2r` shortcut clocks and `r` odd inputs. Thus the total
clock is exactly `s+2r`, its odd count is exactly `s+r`, and its coefficient is
`3^(s+r)/2^(s+2r)>1`. The new Lean module proves the path, both counts, and
`0<x<q` for the entire parameter range.

Every prefix coefficient is at least one. In the first block the coefficient
increases by `3/2` at each step. In the second block its even-clock values
successively decrease by `3/4`, and each intervening odd clock is larger than
its preceding even clock. The terminal coefficient is greater than one, so no
prefix has spent the source's first half-crossing.

Consequently `BudgetAt x` implies `BudgetAt q`: the first half-crossing supplied
for the smaller source occurs after this prefix, and the suffix reaches its own
half-crossing with no greater odd cost. This is `budget_ladder`, which invokes
the separately checked general composition rule in `Collatz.BudgetTransfer`.

No convergence certificate for `x` is substituted for a half-budget certificate.
The resource predicate stays explicit throughout.

## Unit induction and the first-step repair

When inducting only over numbers prime to three, it is essential that the
smaller source also be prime to three. This is not automatic. For example,
`r=1,s=1,u=10,v=14` gives `q=31` and `x=27`. The unrestricted transfer is valid,
but unit-only induction cannot supply its premise just from `27<31`.

`budget_ladder_unit_induction` therefore retains the source-unit guard.
There is also a stronger domain where the guard can be removed. Assume `s>0`
and

\[
                  3\,2^{s+2r}<2\,3^{s+r}.
\]

Spend the first odd step and use the source

\[
 y=2^{s-1}(3v)-1=T(x).
\]

This is automatically `2 mod 3`. Replacing `(s,v)` by `(s-1,3v)` leaves the
link equation unchanged, and the stronger inequality says exactly that the
remaining prefix still expands. The previously proved ladder then gives
`0<y<q`, all prefix coefficients at least one, and a transfer from the smaller
unit `y`. This proves `budget_ladder_unit_entrance` with no source-unit premise.

For example `r=1,s=3,u=94,v=14` gives `x=111`, `q=283`, and the repaired source
`y=167`. The legal path is

\[
111\to167\to251\to377\to566\to283.
\]

The initial source is divisible by three; the repaired source is not.

## Scope of the remaining search

For a given odd `q`, the natural inverse attempt writes `q=3^r u+1` and tests
the divisibility `3^s | 4^r u+2`. The displayed inequalities give complete,
checked successful domains, with unbounded `r,s`. They do not establish that
every remaining `q` has such parameters, or a different successful guarded
path. The global task remains a complete well-founded cover. No unsupported
all-source coverage claim is included in the module.

## Formal evidence

`Collatz/TernaryLadder.lean` imports only `Collatz.BudgetTransfer` and its
core-Lean dependencies. Lean 4.34.1 compiled the complete source with warnings
treated as errors. The seven principal axiom reports list only `propext`,
`Classical.choice`, and `Quot.sound`; no new axiom or `sorry` is used.
