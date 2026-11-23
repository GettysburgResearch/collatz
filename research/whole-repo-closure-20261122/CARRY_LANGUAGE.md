# A literal-tail carry dispatcher for an unbounded source language

## Result and exact scope

`CarryLanguage.lean` proves an actual ordinary-path transport and a valid
complete-source induction rule for the unbounded source language

\[
1\,\{2,3\}^{*}\,2\,1.
\]

For every supplied source path with this prefix, the failed-half target
`9*r+2` reaches one below the retained source endpoint at the **same total
clock** as the supplied prefix. The complete source tail is unchanged, its
highest-changed-grade rank is strictly smaller, and the resulting target is
inside PR177's active interval. The last theorem invokes that existing
lower-rank interval hypothesis; it does not replace it by a conjectural axiom.

The module compiled strictly with Lean 4.34.1 and warnings as errors. Its
seven public theorem audits use only `propext`, `Classical.choice`, and
`Quot.sound`. The universal dispatcher has not closed. The unhandled states
are given explicitly below.

This is a compositional supplied-certificate result, not a new finite
residue census, not an unconditional merger of the two original arms, and
not a proof that partial covers exhaust the remaining Collatz inputs.

## Latest sources actually inspected

- PR177, `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`: alphabet-four
  cofinal predecessors, the common complete-source grade, low-interval
  refinements, and retained-even boundary rules.
- PR178, `be5696cc45a95ad1903802b08ba1dc3ebba66930`: ordinary-source
  parity budgets and the physical tail barrier allowing unequal clocks.
- PR180, `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`: the actual
  `GapTrace`, `GradeDrop`, `PoweredTrace`, and `IntervalHyp` definitions,
  plus the exact unresolved carry pair `(r,9*r+2)`.
- PR183, `907a540943090968bc683b1b9246208e9053c1f8`: the mixed-base
  normalizer, its complete blocked grammar, and its explicitly missing
  physical erasure cover.
- PR186, `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`: the distinction
  between local decreases and a compositional complete termination argument.
- The preceding PR185 packet: the broad AL27 half selector and the narrower
  stronger-partner selector, with their exact published scope.

The imported PR180 source files retain their original bytes under `vendor/`.
Only the initial import header is ported in the external build. In particular,
a prose line beginning `import` inside the `WitnessSynthesis` doc comment is
not interpreted as an import statement.

| Source | SHA256 | Git blob |
|---|---|---|
| `WitnessGlobal.lean` | `37cc56085ad5d9e3a313af3f9e7dd3d041a697cda199db42eb452e321164a4e6` | `477c5e6d907775e06ab78f4b491e5b76a88d6549` |
| `WitnessSynthesis.lean` | `8bee9e1caa0c914d77f0a37f86bbd6caa5dbd27be607c7d03783e7463219cadd` | `17d0995a62860c1bc5fcbc51e0cfcaf39fe354f9` |

No new ordinary Collatz map is defined. All orbit conclusions use the
existing `CollatzShell.step` and `CollatzShell.orbit`.

## 1. The unbounded signed-gap identity

Suppose the supplied source has a positive-gap equation

\[
3r+1=2^a u,\qquad u>0.
\]

For arbitrary integers \(p\ge1\) and \(0\le b\le a\), put

\[
F_{p,b}(r)=3^p r+3^{p-1}-2^b.
\]

The first new theorem proves

\[
\boxed{T^a(F_{p,b}(r))=3^{a+p-b-1}u-1.}\tag{1}
\]

All quantities in Lean are natural numbers, with the nonnegative
factorization below justifying the subtraction. The actual target path is
exactly b halvings followed by a−b initial odd steps:

\[
F_{p,b}(r)
=2^b\left(2^{a-b}3^{p-1}u-1\right).
\]

After the b halvings the expression in parentheses is ordinary. The existing
odd-run theorem then yields (1). This is a physical prefix, not a rational
semigroup calculation with an omitted integrality guard.

The exponent accounting is

\[
p_{\mathrm{new}}+b+1=a+p.
\]

Choosing b changes the original target intercept. It is therefore not legal
to choose b=a for free merely because it lowers the ternary exponent.

## 2. A two-state carry program

Write \(D_p(r)=3^p r-1\). The failed short-diamond carry is
\(C(r)=9r+2=F_{2,0}(r)\). Equation (1) gives

\[
T^a(C(r))=D_{a+1}(u).\tag{2}
\]

In particular an initial source gap one reaches debt state two. The two
small debt states have the following exact transitions:

\[
T^a(D_1(r))=D_{a-1}(u)\quad(a\ge1),
\]

\[
T^a(D_2(r))=D_{a-1}(u)\quad(a\ge2).
\]

The table records the relevant alphabet-four cases. An escape means this
particular two-state program has no enabled rule, not that the ordinary
trajectory fails to converge.

| State | Source gap 1 | Source gap 2 | Source gap 3 | Source gap 4 |
|---|---|---|---|---|
| `C(r)=9r+2` | `D₂(u)` | `D₃(u)` escape | `D₄(u)` escape | `D₅(u)` escape |
| `D₁(r)` | `u−1`, interval query | `D₁(u)` | `D₂(u)` | `D₃(u)` escape |
| `D₂(r)` | unsupported by this template | `D₁(u)` | `D₂(u)` | `D₃(u)` escape |

The state can increase from one to two. The proof does not incorrectly
require the state number to decrease at every transition. Instead, it
consumes the actual finite supplied source prefix and proves a strict drop
of the single complete-source rank at the end.

The special role of states one and two has an exact arithmetic explanation.
For \(D_p\) to re-enter the same signed-gap template, its intercept must obey

\[
2^b=3^{p-1}+1.
\]

The only solutions with p≥1,b≥0 are (p,b)=(1,1),(2,2). For p≥3, reducing
modulo eight forces b=1 when p is odd, or b=2 when p is even, and either value
contradicts the equality. This classification is written arithmetic here;
the Lean module proves the positive transition identities it uses.

## 3. The complete all-length language

Let `body` be any finite word all of whose letters are two or three, and let

\[
P=1\,\mathrm{body}\,2\,1,\qquad A=\sum P=\sum\mathrm{body}+4.
\]

Suppose `GapTrace(r,u,P)` is supplied. The first letter sends C to D₂. Every
letter in `body` remains inside {D₁,D₂}. The final gap two reaches D₁, and
the final gap one reaches u−1. Therefore

\[
\boxed{T^A(9r+2)=u-1.}\tag{3}
\]

There is no upper bound on the length of `body`, its mixture of twos and
threes, the source r, or the retained endpoint u. The theorem is proved by
induction on the whole word, not inferred from a finite collection of tests.

For the empty body, one concrete example is

\[
59\to89\to134\to67\to101,
\]

whose odd-gap prefix is [1,2,1], while

\[
533\to800\to400\to200\to100.
\]

The target endpoint is one below 101. These two endpoints are not being
asserted equal.

## 4. Exact integration with the complete-source rank

Now retain the complete supplied certificate

\[
\operatorname{GapTrace}(r,1,P\Vert\tau).
\]

Splitting at the end of P gives the literal tail
\(\operatorname{GapTrace}(u,1,\tau)\). The grade is exactly PR177/PR180's
formula

\[
\Gamma(e;W)=
\bigl(\{2e+1\}\text{ if }e>0\bigr)
\uplus\{2a:a\in W\}.
\]

The new theorem `language_grade_drop` proves

\[
\Gamma(0;\tau)\prec\Gamma(0;P\Vert\tau).
\]

If the body contains a three, grade six is the highest changed grade and
its multiplicity decreases. Otherwise grade four is the highest changed
grade and its multiplicity decreases. All larger counts agree and the
complete suffix cancels. This is the literal `GradeDrop` relation used by
the imported source, rather than a new informal rank.

Because a positive ordinary trajectory cannot reach zero, (3) gives u−1>0.
The child query is therefore active:

\[
0<u-1\le2u+1.
\]

`carry_language_interval_rule` applies the existing lower-grade
`IntervalHyp` to source u, target u−1, initial even exponent zero, and the
unchanged tail τ. This supplies `Basin(u−1)`. The actual path (3) then
transfers that conclusion to the original carry input `9*r+2`.

The proof does **not** infer `Basin(u−1)` from `Basin(u)`. Nor does it obtain a
fresh uncontrolled certificate for a target returned by an earlier induction
call. Both the child certificate and its grade comparison are explicit.

## 5. What remains unsupported

The program is not total. An initial source gap at least two leaves debt
D₃ or higher immediately. Inside the small-state program, gap four leaves
D₃, and state D₂ followed by gap one has no rule of the chosen form. The
generic signed-gap identity does not justify changing the intercept to
make one of those transitions fit.

For a proposed enlarged dispatcher, consuming the supplied complete source
word can leave source one with a target `3^d−1`, with an uncontrolled d.
Proving convergence of all those terminal debts is a substantial additional
claim, related to the repo's earlier power-of-three reductions. It is not a
finite terminal case and is not installed as an axiom here.

The parallel fixed-block cycle classifier can decide every fixed linear
repeated-block schema. It does not prove termination of a nonperiodic debt
program or prove that every escaped state belongs to finitely many such
schemas. Consequently it cannot silently discharge this remaining case.

Finally, when the carry input was reached from an earlier AL27 source,
ordinary descent below `9*r+2` would not automatically mean descent below
that earlier source. The new rule is a valid supplied-source interval
query; a universal original-source strategy still needs complete dispatch
and the appropriate common witness budget. No universal coverage or full
Collatz conclusion is claimed.

## Validation artifacts

- `CarryLanguage.lean`: seven new public kernel-checked theorems.
- `CarryLanguage.log`: the final strict compiler output.
- `carry_receipt.json`: exact command, source/log hashes, timings, and audits.
- `vendor/`: unchanged PR180 originals.
- `WitnessGlobal.header.patch`, `WitnessSynthesis.header.patch`: explicit
  header-only transformations for the external build.
- `REVIEW_FIXED_BLOCK_CYCLES.md`: independent SHA-pinned review of the
  parallel fixed-block classification argument, without claiming a replay.
