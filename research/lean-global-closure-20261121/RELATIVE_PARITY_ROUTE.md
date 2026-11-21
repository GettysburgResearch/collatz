# A Lean route through deterministic relative parity

**Status: the stated barrier, finite certificate, and equivalence are proved in
Lean. The universal relative-budget-return statement is OPEN. This is not a
proof of the Collatz conjecture.**

The source is `CollatzGlobalClosure/RelativeParityBarrier.lean`. It uses the ordinary positive
shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2,\end{cases}
\]

and counts actual odd inputs. Write `orbit n t = T^t(n)` and let
`oddCount n t` count the odd inputs at clocks `0,...,t-1`. `ReachesOne n`
means that an actual ordinary iterate is one. It is not an abstract
certificate predicate or a density-one statement.

The new PR146 terminal construction at
`f431078244e868dc699fad011044f0d5e7f76437`,
`research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md`, and
PR171's section recurrence at
`2bd243b3e05eaa5543adeb2894637b053c9662ca`,
`research/adaptive-closure-20261121/AFFINE_SECTION_RECURRENCE.md`, motivated
this route. They are not premises of the Lean proofs. No claim of priority
is made for the elementary parity-growth estimate; the checkpoint makes
the whole-orbit deterministic closing obligation explicit and kernel checked.

## 1. An all-time barrier for every hypothetical failed orbit

For every positive `n` that never reaches one, and every clock `t`, Lean
proves

\[
\boxed{2^{4t}\le 2^{7p_t}n^4,\qquad p_t=\operatorname{oddCount}(n,t).}
\tag{RP1}
\]

This includes any hypothetical nontrivial positive cycle. There is no
divergence assumption, random-input model, asymptotic limit, finite search
cap, or exception for the source's prescribed infinite parity tail.

The proof uses the exact quartic inequality

\[
(3v+1)^4\le128v^4\qquad(v\ge3).
\]

After writing `v=3+a`, the difference is the polynomial

\[
47a^4+456a^3+1512a^2+1824a+368.
\]

At an even step, `16T(v)^4=v^4`. At an odd input before the first hit of
one, positivity and oddness give `v>=3`, hence
`16T(v)^4<=128v^4`. Multiplying these inequalities along a finite prefix
gives the stronger invariant

\[
2^{4t}T^t(n)^4\le2^{7p_t}n^4.
\]

The positive integer endpoint is at least one, proving RP1. The principal
Lean declarations are `finite_no_hit_growth` and `nonconvergent_barrier`.

## 2. A finite parity-budget certificate

For positive `n`, any `B,t` satisfying

\[
n<2^B,\qquad 7p_t+4B\le4t
\tag{RP2}
\]

certify that `n` reaches one. Under nonconvergence, RP1 would imply

\[
2^{4t}\le2^{7p_t}n^4
 <2^{7p_t+4B}\le2^{4t}.
\]

The declaration `converges_of_parity_budget` checks this implication.
It does not assert that such a clock exists for every positive input.

## 3. Keep the supplied source witness in the global comparison

Suppose `x>0` and a supplied source witness gives `T^d(x)=1`. It need not
be first-hit: arbitrary terminal-cycle padding is allowed. Put

\[
p=\operatorname{oddCount}(x,d),\qquad t=d+2m.
\]

The source is then exactly on its ordinary two-cycle, so Lean proves

\[
\operatorname{oddCount}(x,d+2m)=p+m.
\tag{RP3}
\]

No fair-bit substitution is made after clock `d`.

**Finite relative-budget theorem.** If

\[
m\ge56p+160x
\tag{RP4}
\]

and the actual pair has

\[
\boxed{
16\operatorname{oddCount}(5x,t)
\le16\operatorname{oddCount}(x,t)+t,
}
\tag{RP5}
\]

then `5x` reaches one.

Indeed RP3 makes the right-hand side `16(p+m)+d+2m`.
Multiplying by seven and combining RP4 gives

\[
7\operatorname{oddCount}(5x,t)+20x\le4t.
\]

Apply RP2 with `n=5x` and `B=5x`; the elementary inequality
`5x<2^(5x)` is proved in the same file. The deliberately simple size
choice avoids logarithmic library machinery. No claim that its large
clock threshold is optimal is made.

The theorem is `five_converges_of_relative_budget`. The condition concerns
one actual finite prefix of the target. Its source input is the complete
ordinary witness, retained through RP3.

## 4. Exact remaining universal statement

`RelativeBudgetReturns` is the following proposition:

> For every positive `x`, every supplied `d` with `T^d(x)=1`, and every
> lower bound `H`, there is an `m>=H` for which RP5 holds at `t=d+2m`.

Lean proves, without adding a new axiom,

\[
\boxed{
\bigl(\forall x>0,\ x\to1\Longrightarrow5x\to1\bigr)
\quad\Longleftrightarrow\quad
\texttt{RelativeBudgetReturns}.
}
\tag{RP6}
\]

The forward implication uses the two actual eventual two-cycles. Their
odd-count difference is bounded, so the budget in RP5 is attained at
arbitrarily large clocks. The reverse implication chooses
`H=56p+160x` and applies RP4–RP5. The declarations are
`relative_budget_returns_of_forward_five`,
`forward_five_of_relative_budget_returns`, and
`forward_five_iff_relative_budget_returns`.

`RelativeBudgetReturns` is an ordinary definition of an explicitly open
proposition. It is a hypothesis of the implication theorem, not an axiom
and not a theorem established by this file. RP6 does not replace the
missing universal argument with an unlabelled assumption. The source-pinned
finite directed reductions elsewhere in the repository identify full
forward-five closure as a sufficient global Collatz interface; those
reductions are not imported or re-audited here.

## 5. Closing attempt and where it currently stops

I tried to establish RP5 by following the actual prescribed source tail.
At every second clock after the source reaches one, write

\[
Y_m=T^{d+2m}(5x),\qquad
k_m=\operatorname{oddCount}(5x,d+2m)-p-m.
\]

The target's ordinary two-step map has the exact four branches

| `Y mod4` | `T^2(Y)` | Odd inputs | Additive numerator `B` |
|---|---|---|---|
| 0 | `Y/4` | 0 | 0 |
| 1 | `(3Y+1)/4` | 1 | 1 |
| 2 | `(3Y+2)/4` | 1 | 2 |
| 3 | `(9Y+5)/4` | 2 | 5 |

If the odd count in that two-clock block is `a`, then

\[
k_{m+1}=k_m+a-1,
\qquad
\frac{Y_{m+1}}{3^{k_{m+1}}}
=\frac34\frac{Y_m}{3^{k_m}}+
\frac{B}{4\,3^{k_{m+1}}}.
\tag{RP7}
\]

The normalized target therefore has a contracting affine recurrence.
This does not bound the level `k_m`: a growing level can compensate for a
shrinking normalized target. Positivity produces a lower bound on the
level in that situation, not the needed upper-return bound. The four
deterministic branches are the actual ordinary map; replacing their
selection by independent bits would change the problem.

RP1 shows that any failed target must violate RP5 eventually, with a
linear excess relative to the source's period-two count. The exact
unproved step is to force RP5 at arbitrarily large clocks for every
supplied ordinary source witness. Neither the Haar recurrence nor the
terminal-prefix density theorem proves that pointwise statement.

## Lean evidence

The file is compiled using Lean 4.34.1 and mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`, with warnings treated as errors.
It reports the axioms of all 18 proved declarations. No `sorry`, new
`axiom`, `native_decide`, or unsafe proof mechanism occurs in the source.
The package build receipt is saved in
`../../reports/lean-global-closure-20261121/checkpoint-build.json`.

The scope is a kernel-checked all-orbit barrier and exact global closure
interface, together with an attempted deterministic completion. The
universal closing proposition remains open.
