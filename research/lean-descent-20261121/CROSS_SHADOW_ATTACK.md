# Two-sided integer shadow attack

**Status: formal exact identities and a guarded induction step; universal closure OPEN.**
This is a new attack on PR174's `OpenLemma`, not an audit of its earlier reductions.
The source is PR174 at `7034109ed60a26bc49824e1ed43c239ceca81194`.
The new module is `lean/Collatz/CrossShadow.lean` and imports only that packet's
core-Lean `Collatz.Closure`.

## The route

Write `T` for the shortcut map. Given a proposed closure failure, start the two
ordinary arms at `x=m` and `y=3m-1`. Maintain an integer relation

\[
                    a x-b y=d.
\]

Initially `(a,b,d)=(3,1,1)`. If the next parities of the two arms are
`e=x mod 2` and `f=y mod 2`, respectively, the exact update is

\[
 a'=3^f a,\qquad b'=3^e b,\qquad
 2d'=3^{e+f}d+3^f a e-3^e b f.
\]

The displayed numerator is even on every physically legal pair. The Lean proof
uses the exact identities `2T(x)=3^e x+e` and `2T(y)=3^f y+f` and proves that
integer division in the update is exact. No inequality between the odd counts
is needed. This is the advantage over a chart written only as
`y=3^k x-c` with a natural exponent `k`: the update remains valid when one arm's
odd count overtakes the other's.

After `t` steps let `p` and `q` be the source and member odd counts. The
coefficient identities, also proved by induction in Lean, are

\[
                  a_t=3^{q+1},\qquad b_t=3^p.
\]

If the supplied member certificate reaches one at that clock, the full terminal
arithmetic is therefore

\[
                   3^{q+1}T^t(m)=3^p+d_t.                   \tag{1}
\]

This equation is over ordinary integers, including the signed debt. It is not a
2-adic limit statement. The theorem accepts any valid certificate clock, whether
or not it is the first.

## The attempted closure

At a globally least nonconvergent `m`, every smaller positive integer lies in the
basin. Consequently the explicit strict inequality

\[
                    3^p+d_t < 3^{q+1}m                  \tag{2}
\]

would close the induction: (1) yields `0<T^t(m)<m`, and basin membership pulls
back through the actual ordinary trajectory. The module proves this complete
implication as `psi_close_of_terminal_guard`. It does **not** assume that a
member certificate automatically establishes (2).

In fact the most direct hoped-for argument, using the first member hit, is
false on the very residue class required by `OpenLemma`. For `k=3`, `m=82`:

\[
 3m-1=245,\qquad T^{16}(245)=1,\qquad T^{16}(82)=233>82.
\]

All sixteen earlier member positions differ from one. This whole finite
statement is a Lean theorem proved by kernel reduction and has no axioms.
The terminal coefficients are `a=729`, `b=177147`, `d=-7290`, so (1) reads
`729*233=177147-7290`. This example is a failure of the proposed induction guard,
not a Collatz counterexample.

Allowing later member clocks does not automatically repair the proof. Once the
member reaches the `1,2` cycle, its even phase repeats every two steps. The
source still follows its original ordinary orbit. A proof that some later
certificate clock always satisfies (2) would have to establish the actual
source descent. No such theorem is supplied here.

## Further approaches tried

1. **Certificate-rank induction.** Reading one more inverse member edge can
   increase the source coefficient or the signed debt. Its new source need not
   have a shorter member certificate. In particular, passing through zero
   relative odd count is not a terminating event. The two-sided frame makes
   this crossing legal but does not make it descending.
2. **Terminal phase pumping.** After the member first reaches one, advance both
   arms by two steps. The member returns to one, while the source takes the
   ordinary two-step branches with slopes `1/4`, `3/4`, `3/4`, and `9/4`.
   The last branch prevents a uniform one-block decreasing size argument.
   An unbounded choice of blocks needs its own termination proof.
3. **Fixed linear debt potential.** The signed debt is not uniformly small
   relative to either coefficient, and its sign alone does not imply descent.
   At the explicit failure of the first-hit guard above, the debt is already
   negative. The right coefficient is large enough to keep the source endpoint
   above its starting value.

The first unsupported step of this route is a genuinely terminating selection
of a member certificate clock satisfying (2), or another sufficient arithmetic
guard with an independently proved complete selection procedure. The new
module is intended to let future candidate procedures be checked without
losing the count-crossing cases.

## Formal inventory and actual execution

Theorems: `shortcut_balance`, `advance_holds`, `trace_holds`,
`psi_terminal_equation`, `iter_pos`, `hits_iff_iter`, `basin_iter`,
`trace_left`, `trace_right`, `trace_left_pos`, `psi_terminal_counts`,
`psi_terminal_descent`, `psi_close_of_terminal_guard`,
`terminal_clock_counterexample`.

Executed on Lean 4.34.1:

```
lake env lean -DwarningAsError=true Collatz/CrossShadow.lean
lake env lean -DwarningAsError=true CrossShadowAudit.lean
```

The audit reports only `propext`, `Classical.choice`, and `Quot.sound` for the
principal structural theorems. The counterexample has no axiom dependencies.
No `sorry`, additional axiom, or claim of full Collatz closure occurs.
