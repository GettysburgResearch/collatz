# A complete finite compiler for arbitrary bounded joint edits

23 November 2026. **PROVED finite completeness, ordinary witness transport,
and an explicit obstruction to one proposed input-funded budget. Universal
successful edit-budget selection remains OPEN.**

The current candidate recognizers already decide a supplied complementary
rational. This attack instead asks whether an ordinary source can be moved
into a known convergent trajectory by editing its complete parity word. The
new result gives a finite, exhaustive compiler for any prescribed number of
insertions and deletions on either side. Arbitrarily long common runs do not
require an additional guessed clock cutoff.

For positive sources `x,y<2^N`, every first-merger alignment using `t` edits
has at most

\[
\boxed{B(N,t)=N(2^t-1)}                                      \tag{JE1}
\]

alignment columns. Each actual shortcut clock is at most `B(N,t)`. The
compiler therefore returns either an actual ordinary merger or a complete
negative answer for that edit budget. It does not require any partial
inverse edit to be integral; both complete physical trajectories are
retained throughout.

Given the complete input witness for `y`, acceptance emits a complete
output witness for odd `x`. With input shortcut clock `L`, the output clock
is bounded by

\[
\boxed{2N(2^t-1)+L.}                                      \tag{JE2}
\]

The standalone [Lean module](JointEditCompiler.lean) proves the literal
alignment normalization, finite bound, executable search soundness and
completeness, negative-answer completeness, and ordinary witness consumer.
The [Python compiler](joint_edit_compiler.py) emits explicit trajectories
and the original problem's exponent tuple. Its optimized matching-run
enumeration and tuple conversion have the written justification below;
they are not represented as extracted Lean code.

## 1. Sources and the change of scope

The most relevant preceding result is PR176 at
`81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a`,
`research/lean-global-resolvent-20261121/overview/global-closing/FINITE_GAP_ONE_INSERTIONS.md`.
It bounds the complete class of same-endpoint repairs formed only by
inserting accelerated gaps equal to one while keeping every original gap.
Its sign-preserving difference argument also bounds the insertion count
from the source, yielding an all-insertion-class finite search.

Here an edit is one **shortcut letter**, not an arbitrary accelerated gap.
Either coordinate can advance alone. Thus arbitrary shortcut insertions,
deletions, and replacements (a deletion followed by an insertion) are
covered, in arbitrary order, with changing difference signs. An inserted
accelerated gap `a` costs `a` shortcut edits unless some of its letters
are aligned with the other trajectory. The theorem does not silently
identify these two edit counts.

The expanded class loses the preceding monotone-cost bound on the *number*
of edits. Its finite bound is conditional on the supplied `t`. This is the
exact point at which universal coverage is still needed.

PR178 at `a9b23dcee61a4b65a63aa4e7ca653d875a405037` was also inspected:
its source-boundary growth result and additive-prime potential classification
do not supply an edit-budget selector. PR182 at
`afe6f4d1a661b377c9daa4623bdd732ba478386b` improves general rational
recognition, retaining the candidate-existence gap. These are contextual
inputs, not dependencies of JE1 or JE2. The new proofs use elementary
ordinary arithmetic only. Exact files and inspection scopes are in the
associated source ledger.

## 2. Literal alignments on ordinary trajectories

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

An alignment starts at `(x,y)` and uses the following columns:

| Column | Requirement | New pair | Edit cost |
|---|---|---|---:|
| `=` | Current parities agree | `(T(x),T(y))` | 0 |
| `L` | None | `(T(x),y)` | 1 |
| `R` | None | `(x,T(y))` | 1 |

All states are positive ordinary integers. An accepted alignment ends when
the two coordinates are equal. Any purported longer alignment can be cut
at its first meeting, decreasing both edit cost and clocks. No residue,
rational endpoint, or limiting realization is substituted for equality.

The two clocks need not agree. The number of columns equals the number of
common columns plus the number of edits; it bounds each clock separately.
If the starts already coincide, the empty alignment has zero columns.

This includes every usual insertion/deletion alignment of two finite
actual parity prefixes ending at a common state. A common branch is
injective, so a first meeting from distinct starts cannot occur in a
common column. Consequently every nonempty first-merger alignment is a
finite sequence of common runs, each followed by one edit. The Lean
inductives `Alignment` and `Repair` express these ungrouped and grouped
objects, and `alignment_normalizes` proves the grouping without dropping
any legal alignment.

## 3. Matching runs consume the exact binary precision of the difference

Let a common run have length `k`, with `p` odd inputs. The two complete
affine identities have the same carry. Subtraction gives

\[
2^k\bigl(T^k(x)-T^k(y)\bigr)=3^p(x-y).                 \tag{JE3}
\]

Since powers of two and three are coprime,

\[
\boxed{2^k\mid x-y.}                                  \tag{JE4}
\]

For distinct starts below `2^N`, the nonzero difference has absolute value
strictly below `2^N`, hence `k<N`.

More precisely, the maximal common-parity run has length exactly
`v_2(x-y)`. At any matching step the integer difference changes to either
`(x-y)/2` or `3(x-y)/2`, losing exactly one factor of two. Before all such
factors have been consumed the current difference is even and the
parities agree; at the next state the difference is odd and they disagree.
This is the Python compiler's finite run enumeration. It tries an edit at
every cut `0,...,v_2(x-y)`, including the cut at the first parity mismatch.
An earlier edit is never discarded merely because another common step
would be legal.

`same_run_affine`, `same_run_precision`, `same_run_injective`, and
`same_run_clock` formalize the complete affine identity, divisibility,
injectivity, and numerical bound. The exact valuation characterization
used to optimize the Python loop is written scope; the Lean search
instead scans `0,...,N-1` and tests the literal common-run predicate.

## 4. An edit can double the bit budget, but cannot hide its clock

For every natural state,

\[
T(z)\le2z.
\]

Thus `z<2^N` implies `T^k(z)<2^(N+k)`. Take a common run of length
`k<N`, followed by one edit on either side. Both resulting states are
strictly below

\[
2^{N+k+1}\le2^{2N}.                                    \tag{JE5}
\]

There are at most `N` columns in this first run-plus-edit. The remainder
has one fewer edit and initial bit budget `2N`. Induction therefore gives

\[
B(N,0)=0,\qquad B(N,t+1)=N+B(2N,t),
\]

whose exact solution is JE1. Relative order and the sign of the
difference play no role. This is why the proof covers both directions
of editing and arbitrary cancellation patterns.

The bound controls the whole first-merger alignment, not just a fixed
chosen endpoint. Moving a proposed endpoint farther into a common suffix
does not evade it: trim that suffix at the actual first meeting.

### A sharper written real-valued bound

Put `H=max(x,y)`, `alpha=log_2(3)`, and `h=log_2(H+1)`. The literal
inequality `T(z)+1 <= (3/2)(z+1)` gives, across a run of length `k` and
one edit,

\[
h_{\rm new}+1\le\alpha(h+1),\qquad k+1\le h+1.
\]

Indeed `k<=log_2|x-y|<h`, and adding logarithms over at most `k+1`
steps proves the first inequality. Summing the geometric series yields

\[
\boxed{\text{columns}\le
 (1+\log_2(H+1))\frac{\alpha^t-1}{\alpha-1}.}           \tag{JE6}
\]

This is a stronger bound in `t` than JE1. The exact integer compiler and
Lean proofs use JE1, so no floating-point logarithm is needed for either
soundness or exhaustive coverage.

## 5. A total exact search, including a meaningful negative answer

Given positive `x,y` and a nonnegative integer budget `t`:

1. If `x=y`, return the empty certificate.
2. If `t=0` and the starts differ, reject.
3. Enumerate every legal length of a common run before the next edit.
4. At each cut, recursively try one actual left step and one actual
   right step, each with budget `t-1`.
5. Return the first successful complete certificate, or reject if every
   finite branch rejects.

This recursion terminates on `t`, without any assumption of Collatz
convergence. Each internal common run is finite by JE4. Equivalently,
one can compute the two actual trajectories through JE1 and run a
finite insertion/deletion dynamic program on their clock grid.

**Soundness.** Every emitted column is one of the literal rules and the
terminal states agree. The compiler has produced actual clocks, not
only an affine congruence.

**Completeness.** Group any successful first-merger alignment as in
Section 2. Its first common run is among the enumerated cuts. Its first
edit is one of the two recursive branches. The remainder has a smaller
edit budget. Induction gives acceptance. JE5 supplies the updated Lean
bit bound. This proof includes arbitrary common-run lengths, both edit
directions, and arbitrarily much terminal-cycle padding.

**Negative answer.** Rejection excludes every merger alignment using at
most the supplied edit budget, however large its originally proposed
clocks. It does not exclude a merger using more edits and does not
assert that either trajectory diverges.

The Lean equivalence is `seek_iff`; `seek_rejection_complete` exposes
the negative answer, and `seek_ordinary` returns clocks bounded by JE1.
The Python implementation memoizes subproblems but uses the same exhaustive
recursion. Its implementation is separately checked against an independent
finite-grid method.

## 6. Consume the unrestricted complete witnessing tuple

Suppose `y` has the complete input tuple

\[
0=A_0<\cdots<A_r=L,\qquad
3^r y+\sum_{j<r}3^{r-1-j}2^{A_j}=2^L.
\]

The program checks the entire integer identity and replays its exact
odd clocks. No bound is imposed on its length or exponents. Suppose the
compiler returns `T^a(x)=T^b(y)`, with `a,b<=B(N,t)`.

There is a direct bound that handles terminal padding automatically:

\[
T^{a+L+b}(x)=T^{L+2b}(y)=T^{2b}(1)=1.
\]

This proves JE2. The equality is valid also when `b>L`; no backward
clock is used. The Lean theorem `complete_witness_transport` proves
this exact consumer.

For a shorter output, the Python implementation appends the unused
source tail when `b<=L`. When `b>L`, the common endpoint is in `{1,2}`
and at most one step is needed. It cuts at the first target hit of one.
For odd target `x`, it records every odd-input clock and the terminal
clock to emit `0=B_0<...<B_s`, then checks

\[
3^s x+\sum_{j<s}3^{s-1-j}2^{B_j}=2^{B_s}
\]

and the whole replay. Thus acceptance is an output certificate in the
user's original format, with arbitrary output length and exponents
permitted.

One exact call is:

```sh
python -X utf8 -B research/lean-exact-witness-global-20261121/repo-synthesis-20261123/candidate/joint_edit_compiler.py \
  193 385 39 --source-tuple '[0,2,4,6,7,12,13,14,19,23]'
```

Here `385 mod 512=385`, and `(385+1)/2=193`. The emitted target tuple
ends at shortcut clock 76. This example checks the complete transport
consumer; it is not extrapolated to other input tuples.

The preceding joint-cancellation example is retained exactly:

\[
45\to68\to34\to17,\qquad
19\to29\to44\to22\to11\to17.
\]

Its alignment is `R===R`. The inverse source after only the first
accelerated insertion would be `89/3`, but the compiler never demands
that unfinished inverse construction be ordinary. The two complete
ordinary trajectories are the objects it checks.

## 7. Attempted universal coverage and a concrete failed budget

For the original implication, take `y` to be its given witnessed value
and `x=(y+1)/2`. A successful bounded-edit certificate is now completely
funded: neither an additional merger-clock guess nor an output-witness
length guess is needed. The remaining task is to construct an edit
budget that is guaranteed to succeed for every required input tuple.

The most immediate proposal, using at most the complete input shortcut
clock `L` edits, is false. The example above has `L=23`, but the exact
minimum edit budget between 193 and 385 is **39**. This statement includes
unlimited terminal-cycle padding, rather than comparing only the two
first-hit parity words.

The check is exhaustive on the actual finite orbit product. The first-hit
clocks are 76 and 23; their closed state sets have 77 and 24 states.
Including `1 -> 2 -> 1`, their Cartesian product has **1,848** states
and is forward closed under all three alignment rules. A reverse
zero/one shortest-path computation labels every vertex with its distance
to the diagonal. The checker verifies every Bellman lower inequality
and a tight edge at every off-diagonal state. The initial label is 39.
Independently, the recursive compiler rejects budget 38 and emits a
39-edit literal certificate. A source tuple with two extra terminal
cycles produces the same first-hit target tuple.

This refutes that particular input-funded bound. It does not refute a
larger bound depending on the complete tuple, and it does not refute the
original implication. No universal budget follows from the common-run
precision theorem: each edit can replenish the difference's binary
precision and can increase ordinary height. In the one-sided gap-one
class, a monotone real cost bounded the number of edits. That monotonicity
is absent for arbitrary left/right edits. I obtained no replacement
well-founded budget from the source witness, the complementary numerator,
or a state-dependent choice of which side to advance.

In particular, running budgets `0,1,2,...` is only a semidecision for
ordinary merging until universal coverage is proved. The implementation
does not label that unproved outer loop a terminating construction.

## 8. Formal and computational boundaries

The Lean file is standalone `Std` code. Its audited declarations include
the actual shortcut and orbit identities, raw alignment normalization,
JE1, exact search soundness/completeness, rejection completeness, and JE2.
There is no custom research axiom or `sorry`. The sharper real bound JE6,
exact valuation loop optimization, original tuple conversion, and the
concrete 39-edit optimum are written or executable scope as identified
above; they are not claimed as Lean theorems.

The focused controls compare 1,024 bounded-edit decisions on sources
1 through 16 and budgets 0 through 3 with an independent grid oracle;
270 accept. A separate 2,016-pair check tests the exact common-run
valuation. Four damaged certificates are rejected. The all-clock 1,848
state graph, complete input/output tuples, and valid terminal padding
are checked separately. Normal and optimized Python outputs are compared
byte for byte.

These checks validate finite implementation behavior. The unbounded
quantifiers in JE1, compiler completeness, and JE2 are supported by the
proofs and Lean declarations, not by extrapolation from the controls.
The original residue-512 implication and full Collatz remain open.
