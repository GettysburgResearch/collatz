# Exact least forward failure and the remaining even gap

**Status:** the assertions below are proved in Lean 4.34.1. The universal
gap-filling assertion is an explicit equivalent target, not a proved theorem.

Source interface: PR #174 at
`7034109ed60a26bc49824e1ed43c239ceca81194`, `Collatz/Closure.lean`.
The new file is `LeastForwardFailure.lean`, namespace `CollatzGlobal`, importing
only `Collatz.Closure`. It introduces no `axiom`, `sorry`, or `native_decide`.

## 1. Exact floor

Let `Basin n` mean that the ordinary shortcut iteration from the positive
integer `n` reaches 1. Put

\[
 F(m):\quad m>0,\quad m\in\mathrm{Basin},\quad 2m-1\notin\mathrm{Basin}.
\]

For every positive `m`, the file proves the exact equivalence

\[
 \boxed{\ m\text{ is the least }F\text{-failure}
 \iff 2m-1\text{ is the least positive integer outside Basin}.\ }
\]

The nontrivial direction is the full ordinary height floor: all positive
`n < 2m-1` belong to Basin. Strong induction on `n` proves it. An even `n`
reduces to `n/2`. An odd `n>1` has parent `(n+1)/2<m`, which is already in
Basin by the same induction; minimality of `m` supplies closure at that parent.
Conversely, the parent of the least bad integer is good, and every smaller
parent has a good odd child.

The usual contraction of an odd integer equal to `1 mod 4` proves that a least
bad integer is `3 mod 4`. Consequently the least forward-failure parent is
even. Thus any counterexample supplies `m=2t`, `t>0`, with the **exact** state

\[
 \boxed{\quad 9t-1\notin\mathrm{Basin},\qquad
   \forall n\;(0<n<4t-1\Rightarrow n\in\mathrm{Basin}).\quad}
\]

Here `4t-1` and `9t-1` are in the same component, by the already established
power-two/power-three predecessor identity. In particular `t` is good.
There is no multiplicative loss in the floor: its endpoint is exactly the
least bad ordinary integer.

## 2. Two global completion targets

The file proves both of the following equivalences:

\[
 \forall n>0,\ n\in\mathrm{Basin}
 \iff
 \forall t>0,\quad t\in\mathrm{Basin}\Longrightarrow 9t-1\in\mathrm{Basin},
\]

and

\[
 \forall n>0,\ n\in\mathrm{Basin}
 \iff
 \forall t>0,\quad
 \bigl[\forall n\;(0<n<4t-1\Rightarrow n\in\mathrm{Basin})\bigr]
 \Longrightarrow 9t-1\in\mathrm{Basin}.
\]

The second is the strongest context made available by this minimization. It
is a clean target for an actual completion attempt, but the file does not
establish its right-hand side.

## 3. Why a source-certificate induction needs an additional transition

For an odd positive source `x` with

\[
 3x+1=2^a y,\qquad a\ge1,\qquad y>0,
\]

Lean proves the exact transport

\[
 \boxed{\quad 3x-1\in\mathrm{Basin}
    \iff 3^{a-1}y-1\in\mathrm{Basin}.\quad}
\]

This consumes a certified source edge, but the obligation changes with `a`.
At `a=2` it retains the same `3x-1` form. At `a=1` it becomes the predecessor
`y-1`; at `a>=3` it contains a higher ternary multiplier. Those states cannot
be identified with the original closure statement without another argument.

Similarly, consuming the even source edge `2t -> t` turns the target into
`9t-1`. Repeated source halvings leave an unbounded multiplier even after the
source certificate reaches 1. The exact first-layer statements, also proved
in Lean, are

\[
 F(2^s)\iff 3^{s+1}-1\notin\mathrm{Basin},
 \qquad
 9\cdot2^s-1\in\mathrm{Basin}
   \iff 3^{s+2}-1\in\mathrm{Basin}.
\]

These targets are equivalently Mersenne numbers, by the existing
`basin_pow_two_pred` theorem. No convergence assertion for all of this
unbounded family is proved here. A source-only well-founded order therefore
does not supply the terminal cases by itself.

The common order on the multiset of ordinary states in a supplied
source certificate is proved applicable to the explicit families in
[MIXED_CERTIFICATE_DESCENT.md](MIXED_CERTIFICATE_DESCENT.md): it decreases when a source
prefix is consumed, and also when an old prefix is replaced by arbitrarily
many new states lying below its largest removed state. This can reconcile
rank-reducing rewrites with the earlier rank-increasing height contractions.
For a full proof it still requires a transition covering every live relation
state and proved terminal cases. The equations above identify the precise
terminal family that a completion must handle in this forward lane.

The companion `MersenneRecursion.lean` now proves a genuine uniform fold for
every even exponent: `Basin (2^(2r+2)-1)` is equivalent to
`Basin (2^(2r+1)-1)`. It does not close the remaining odd-exponent family.

## 4. Compilation and trust boundary

The new module compiled successfully using the existing PR #174 base build:

```sh
LEAN_PATH=<project>/.lake/build/lib/lean \
  <lean-4.34.1>/bin/lean -DwarningAsError=true LeastForwardFailure.lean
```

An explicit `#print axioms` audit of the exact floor, minimum equivalence,
minimum existence, both global equivalences, and inverse-edge transport
reported only Lean's standard `propext`, `Classical.choice`, and `Quot.sound`.
There is no `sorryAx` and no additional conjectural axiom. This establishes
the stated implications and equivalences; it does not discharge either
global closure target.
