# A binary gate at the same actual pressure maximum

23 November 2026. Published parent PR182:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Status: SOURCE-QUALIFIED written corollary with a finite Lean clock
core. It does not exclude the denominator-eight phase. Collatz remains
OPEN.**

The pressure construction and the least-source return argument select
different ordinary sources. This note connects the new return theorem
only to the same maximum selected by the pressure construction; it
does not replace that maximum by a later iterate or a least element.

## Inputs and exact scope

The pressure input is (PR182,
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`,
`research/repo-synthesis-round8-20261123/PRESSURE_CONSTRUCTION.md`,
R8-P5; blob `7ef222d23f59a2dffd936dbfa93765df064db166`).
It retains the source-qualified escaping-component product from
(PR182, `3954c775ba74e1f40776ff38cb4282698d4a334a`,
`research/closure-round2-20261123/SOURCE_CLOSURE.md`, selection
(1)--(3) and forward (6); blob
`9346c3b93fbd2e336a4e1c2e80d7b92ff5f34162`). No product is asserted
on a cycle.

At its attained positive ordinary maximum m, the input proves, for
every nonempty actual odd prefix,

\[
\boxed{2^{A_j}<3^j,\qquad
\frac12<h(m)<H_*<0.625344347433389,}              \tag{1}
\]

where `A_j` is the complete sum of its actual odd gaps. The new local
input is `CARRY_RETURN.md`, R9-C2--R9-C3: an actual denominator-eight
tail has finite low runs and finite first carry excursions; its
normalized paid excursion of even length `2 ell` has

\[
\Gamma=3\ell+2K,\quad
K=1\ (\ell=1),\qquad K\ge2\ell-2\ (\ell\ge2).
                                                               \tag{2}
\]

Thus `Gamma>=5 ell` for every ell>=1. Both the full ordinary equations
and the integer carry charges are retained in this input.

## R9-M1: the maximum itself must be in a thin binary class

Suppose in addition that the actual scalar at this same m has reduced
denominator exactly eight, with no power of three in the denominator.
The interval in (1) forces `h(m)=5/8`: this is its only possible
multiple of one eighth. The actual first gap is one, giving

\[
n=(3m+1)/2,\qquad h(n)=7/8,\qquad
n+7=3(m+5)/2.                                      \tag{3}
\]

Let t be the number of unpaid `(2,1)` pairs from n before its first
paid excursion. R9-C3 gives

\[
v_2(n+7)=3t+1.                                    \tag{4}
\]

Write `2 ell` for the normalized paid excursion length. The complete
prefix from m through this return has length `1+2t+2ell` and binary
clock `1+3t+Gamma`. By (1)--(2),

\[
1>
\frac{2^{1+3t+\Gamma}}{3^{1+2t+2\ell}}
\ge\frac23\left(\frac89\right)^t
             \left(\frac{32}{9}\right)^\ell.       \tag{5}
\]

If t<=7 and ell>=1, the last expression is at least

\[
\frac23\left(\frac89\right)^7\frac{32}{9}
=\frac{2^{27}}{3^{17}}
=\frac{134217728}{129140163}>1,
\]

a contradiction. Hence t>=8. Equation (3), followed by (4), proves

\[
\boxed{v_2(m+5)=3t+2\in\{26,29,32,\ldots\},\qquad
m\ge2^{26}-5.}                                    \tag{6}
\]

More generally (5) requires

\[
\left(\frac98\right)^t>
\frac23\left(\frac{32}{9}\right)^\ell.             \tag{7}
\]

Longer or more expensive paid excursions require correspondingly
longer initial low runs at this source. This is a necessary relation,
not a contradiction for all t and ell.

## Boundaries that remain

The companion least-source constraint is
`v_2(q+7)>=34` at a global least q with `h(q)=7/8`. It is a statement
about a different selection. It is not inserted into (3), and the
two inequalities are not multiplied or combined as though q=n.

If the scalar at the pressure maximum initially has a denominator
`8*3^r` with r>0, clearing that denominator moves the ordinary source.
The prefix and scalar ceiling in (1) cannot simply be reapplied at
the cleared source. The present corollary therefore keeps its exact
no-ternary-factor hypothesis.

`MaximumGate.lean` checks the rational coefficient identity, monotone
power comparison, exact seven-pair obstruction, and the resulting
natural-number gate. It does not formalize or manufacture the escaping
component, its product, or its attained maximum. The unresolved step
is still to exclude the remaining actual low phase or to control its
unbounded sequence of returns.
