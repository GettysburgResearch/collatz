# Whole-certificate terminal transport and its exact debt budget

**Full Collatz remains open.** This checkpoint proves one finite arithmetic
compiler for **every** complete certificate prefix. It then gives exact
ordinary transport, a quantitative stopping test at the original source,
and a new language of certificate-preserving handoffs. There is no finite
catalogue bound on prefix length, exponent size, signed carry, or continuation
clock.

The formal module is [TerminalCarry.lean](../lean/Collatz/TerminalCarry.lean), using Lean 4.34.1 core
and the existing PR176 `Collatz.Closure` interface. Its ordinary map is

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

## 1. Normalize the entire supplied prefix

Let the complete odd source certificate be `w ++ [h]`, where `w` is an
arbitrary finite word of positive gaps. Put

\[
r=|w|,\qquad B=\sum_{a\in w}a,\qquad C=C(w),\qquad s=r+1.
\]

Here `C([])=0` and `C(a::w)=3^|w|+2^a C(w)`. Separating the last exponent
from the **literal supplied certificate** gives

\[
3^s m+3C+2^B=2^{B+h}. \tag{1}
\]

For any fixed dyadic affine companion

\[
n=2^j m+b\in\mathbb N,\qquad j\ge0,\quad b\in\mathbb Z,
\]

define

\[
L=B+h+j,\qquad
p=b3^s-2^{B+j}-3\,2^jC.
\]

Then the entire prefix has the exact representation

\[
\boxed{3^s n=2^L+p.} \tag{2}
\]

In particular, `j=1,b=1` gives Hplus, and `j=1,b=-1` gives psi whenever
that target is positive. The coefficient `p` is always prime to three.
It depends on the supplied prefix and companion, and **does not depend on
the terminal exponent h**.

The theorems `terminal_of_complete_word`, `terminal_dyadic_identity`, and
`dyadicCarry_unit` formalize these statements. The compiler does not select
a different convergence certificate or replace an ordinary source by a
completion point. In fact the transport theorem needs only the displayed
integer identity; it does not assume the target converges.

## 2. A finite signed carry compiler for all prefixes

Starting from `(s,p)`, while `s>0`, perform

\[
(s,p)\longmapsto
\begin{cases}
(s,p/2),&p\text{ even},\\
(s-1,(p+3^{s-1})/2),&p\text{ odd}.
\end{cases} \tag{3}
\]

Each division is integral. Primitivity modulo three is preserved whenever
the remaining denominator exponent is positive. An even step has nonzero
numerator, so it strictly reduces its absolute value. An odd step strictly
reduces the denominator exponent. This proves termination in the
lexicographic order `(s,|p|)`.

The stronger explicit natural-number bound proved in Lean is

\[
\boxed{t+|d|+1\le |p|+3^s,} \tag{4}
\]

where the output has denominator exponent zero, integer carry `d`, and
ordinary clock `t`. Optional halvings of a nonzero even integer carry obey
the same bound. The compiler uses exactly `s` odd branches, hence `s<=t`.

These are unconditional finite arithmetic facts. No termination of a
positive or negative Collatz orbit is assumed. Only the denominator-removal
program is proved terminating; a later arbitrary signed orbit is represented
by a supplied **finite** path.

## 3. Exact ordinary transport and the binary horizon

For every integer in (2) with `L>=t`, the compiler's actual ordinary parity
branches agree with the branches of (3), and

\[
\boxed{T^t(n)=2^{L-t}+d.} \tag{5}
\]

This is the theorem `program_transfer`. Its universal whole-prefix version
is `terminal_dyadic_normal_form`. The horizon `L>=t` is essential: each
step consumes one bit of the high power, and a shadow beyond that horizon
is not an ordinary trajectory identity.

A zero carry closes the entire sufficiently precise fibre outright:
the actual target reaches a power of two. This is `basin_of_zero_carry`.
Other carries are not declared good merely because the compiler terminated.

Some small Hplus prefixes illustrate the output; all are instances of the
same unbounded theorem.

| Supplied prefix w | s | p | Compiler clock t | Integer carry d |
|---|---:|---:|---:|---:|
| `[]` | 1 | 1 | 1 | 1 |
| `[1]` | 2 | -1 | 2 | 1 |
| `[2]` | 2 | -5 | 2 | 0 |
| `[3]` | 2 | -13 | 3 | -1 |
| `[4]` | 2 | -29 | 3 | -3 |

The optional final halving is included in the last two rows.

## 4. Continue without losing the original floor

After (5), take **any supplied finite signed shortcut path** from `d`, of
ordinary length `u`, with exactly `a` odd branches, ending at the integer
`e`. If `t+u<=L`, the actual ordinary input satisfies

\[
\boxed{T^{t+u}(n)=3^a2^{L-t-u}+e.} \tag{6}
\]

The Lean type `SignedPath` retains both clocks. Theorems
`signed_path_exists`, `signed_path_transfer`, and `continued_normal_form`
prove the finite continuation interface. The existence of each finite path
does not claim that the infinite signed orbit terminates or becomes periodic.

Multiplying the desired numerical inequality by the same positive `3^s`
from (2) gives an **if and only if**, not a heuristic drift condition:

\[
\boxed{
T^{t+u}(n)<n
\iff
\bigl(2^{t+u}-3^{s+a}\bigr)2^{L-t-u}>3^s e-p.
} \tag{7}
\]

This is `continued_descent_iff_budget`. The original `n` stays fixed on
both sides throughout. With the actual hypothesis that every positive
integer smaller than this `n` converges, a passing budget closes `n` by
`basin_of_continued_budget`. No numerical minimum is transferred from an
unrelated source, a later marked visit, or a different component.

The first missing statement for a universal debt-based proof is therefore
an ordinary continuation or another source-preserving bridge that closes
**every** resulting signed shifted-power case. The existence and
well-foundedness of the compiler supply neither that budget nor an
extension of its binary horizon.

## 5. A positive bridge into the existing certificate induction

When the compiled carry is `d=-1` and `H=L-t>=2`, one more actual odd step
gives

\[
2^H-1\longmapsto 3\,2^{H-1}-1=2S-1,
\qquad S=3\,2^{H-2}.
\]

The source `S` has an explicit complete powered certificate: its odd part is
three, with odd-gap word `[1,4]`. Thus

\[
\operatorname{Basin}(S),\qquad
\operatorname{Basin}(2S-1)\iff\operatorname{Basin}(n).
\]

The actual path and known source are proved by `minus_one_psi_handoff`.
This handoff does not assume that the new psi query closes.

For Hplus terminal transport, if `t>=B` and `h>=5`, its initial even
exponent `e_0=B+h+1-t-2` satisfies

\[
2e_0+1<2h,\qquad 2<2h,\qquad 8<2h.
\]

These are precisely the three grade bounds in
`terminal_handoff_grade_bounds`. In the PR177 graded multiset order, the
old complete word contains the terminal grade `2h`, and every grade of the
new powered certificate `(e_0;[1,4])` is below it. The removed old word
therefore dominates the whole inserted word by the existing `replace_many`
theorem. This gives a source-rank-decreasing rule for the **entire accepted
prefix language**, with no fixed depth or ternary residue catalogue. The
core module proves the concrete handoff and grade inequalities; an
instantiation of PR177's separate `GapComparison` dispatcher is not imported
or claimed complete here.

This is a genuine next query with an explicit ordinary source certificate.
The fact that the new source is known does not prove its wanted psi target.

## 6. The first hard prefix retains an unbounded Mersenne obligation

The source prefix `[3]` followed by the terminal gap `h` has

\[
9m+11=2^{h+3},\qquad
n=2m+1=\frac{2^{h+4}-13}{9}.
\]

Positive ordinary instances occur for every `h=6k+4`, `k>=0`; the source's
complete word is `[3,h]`. The compiler yields

\[
\boxed{T^3(n)=2^{h+1}-1>n.} \tag{8}
\]

For every `0<=u<=h+1`, the remaining high-bit horizon is exact:

\[
\boxed{T^{3+u}(n)=3^u2^{h+1-u}-1>n.} \tag{9}
\]

In fact `T^k(n)>=n` for **every** `k<=h+4`. The theorems
`three_gap_mersenne`, `three_gap_expands`, `three_gap_horizon`, and
`three_gap_no_descent_through_horizon` prove these unbounded statements under
the exact ordinary integer guard. The first instance is the known source
`m=13` with certificate `[3,4]`, whose Hplus target follows `27 -> 41 -> 62 -> 31`.

Thus even a complete source certificate with only two odd gaps, and an
arbitrarily large final gap, does not force its companion below the original
floor during the entire available binary horizon. The `-1` signed shadow
uses only odd branches, so its finite continuations keep increasing the
coefficient debt in (7). The Mersenne residual must be handled beyond that
horizon or transferred to another certified query. The handoff in Section 5
does the latter when its terminal-grade bound applies; coverage of the new
psi query remains open.

## 7. Evidence and provenance

The existing complete-word and multiset conventions come from PR177,
commit `00a611094043afeb256d6532b477c0709e8ed270`, especially
`Collatz/Witness.lean` and `Collatz/GapMultiset.lean`. The current module uses
local copies of the same elementary word functions so it can compile
against PR176's existing core imports. Their terminal split is proved
directly. No theorem from the pending PR177 dispatcher is assumed.

The AYH review at PR141, commit
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`, already isolates universal
coverage as the missing step in gluing deletion orders and shows that a
different rewrite schedule does not change a terminating derivation's rule
counts. That is why this pass changes the arithmetic query representation
and retains its exact debt, instead of proposing another scheduling order.

Run `python terminal_carry.py --output terminal_carry_results.json` for a
separate arbitrary-precision replay. The checked catalogue contains 6,220
programs, 18,660 complete source/target replays, four dyadic companion types,
and 20 Mersenne horizons. It replays every actual source gap, every actual
target branch, the continuation, and both exact budget equivalences.
These finite checks test transcription and implementation. The unbounded
claims rest on the Lean proofs, whose audit lists only standard Lean axioms.
