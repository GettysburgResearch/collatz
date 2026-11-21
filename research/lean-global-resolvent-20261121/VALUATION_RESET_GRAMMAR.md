# An unbounded reset of a power-of-two source certificate

This is a proved arithmetic grammar with explicit guards, not a universal
coverage result. The exponent-loop length is unbounded. It extends the first
of the two thirteen-odd-step resets found during the global closure attempt.

Write `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`. An odd-division word
lists the exact exponents in `(3n+1)/2^a`; its shortcut clock is the sum of
those exponents.

## The guarded construction

Let `l>=3`, let `P` be a positive multiple of 4, and suppose

\[
 2P-1=3^{l+3}w,\qquad
 2187m+11959=2^{l+14}w,
 \qquad w>0,\quad m>0.
\tag{1}
\]

These are ordinary integer equations. They imply that `w` and `m` are odd.
The source entrance word and target entrance word are

\[
 S_0=(1,2,1,2,1,2,4),\qquad T_0=(5,1,1,1,1,1,2).
\]

They have seven odd inputs, with shortcut clocks 13 and 12. They give

\[
 m\longmapsto x_0=2^{l+1}w-1,
 \qquad 2m-1\longmapsto4x_0+3.
\tag{2}
\]

The first affine identity is
`8192 x0 = 2187 m + 3767`. The second is the same linear identity after
applying the target word. These are actual ordinary paths: since `l>=3`,
(1) implies `m=131072t+95227`, `t>=0`; every step of the displayed finite
prefix is integral and has the prescribed parity on this entire class.
The source endpoint is `34992t+25423`; the target endpoint is
`139968t+101695`, exactly four times the source plus three.

The relation `target = 4 source + 3` is preserved by one odd shortcut step
on both sides. The next `l` division exponents on both arms are exactly 1,
because their actual states are

\[
 x_j=2^{l+1-j}3^j w-1,\qquad
 y_j=2^{l+3-j}3^j w-1,
 \quad0\le j\le l.
\tag{3}
\]

At `j=l`, put `v=3^l w`. Then the source is `2v-1`, the target is `8v-1`,
and `2P-1=27v`. Since `4|P`, one has `v=5 mod8`. The source tail has
division exponents `(2,1)` and reaches

\[
 z=(9v-1)/4=(P/2-1)/3.
\]

Its next shortcut step reaches `P/4`. The target tail has division
exponents `(1,1,2)` and reaches `(27v-1)/2=P-1`. Thus the complete paired
paths are

\[
 T^{l+17}(m)=P/4,
 \qquad T^{l+16}(2m-1)=P-1.
\tag{4}
\]

The old source `P/2` reaches `P/4` in one even step. Therefore any supplied
certificate for `P/2` can have that first step replaced by the new prefix
from `m`, preserving its entire tail. A supplied certificate for `2m-1`
can have its target prefix stripped to obtain a certificate for `P-1`.

## Whole-prefix decrease

Each source-prefix state is an affine function `a P+b`. All constants are
negative before the final state `P/4`, whose constant is zero. The greatest
leading coefficient in the entrance is

\[
 a_{\rm entry}=\frac{2^{l+7}}{3^{l+4}}.
\]

The intermediate loop coefficients increase to `4/27`; the final source
tail has maximal coefficient `1/4`. Hence every new source-prefix state
is bounded above by

\[
 \max\left(\frac{2^{l+7}}{3^{l+4}},\frac14\right)P
 \le\frac{1024}{2187}P<\frac P2.
\tag{5}
\]

This inequality holds at every ordinary shortcut state, including even
intermediates, not only at accelerated odd inputs. Thus replacing the one
old input state `P/2` by the entire longer new input prefix strictly
decreases the multiset extension of ordinary numerical order. In this
family an arbitrary increase in certificate rank is paid for by an actual
decrease of every inserted state below the removed state.

## Power-of-two specialization and selector

Take `P=2^e`. The last full odd exponent of the source certificate is
`e-1`; its odd count is `l+10`. The source is

\[
 m=\frac{2^{l+15}P-C_l}{3^{l+10}},\qquad
 C_l=2^{l+14}+11959\,3^{l+3}.
\tag{6}
\]

Since `11959` is a unit modulo 3, integrality of (1) implies

\[
 v_3(2P-1)=l+3.
\]

For odd `e`, the elementary lifting identity
`v3(2^(e+1)-1)=1+v3(e+1)` gives the unique selector

\[
 l=v_3(e+1)-2.
\tag{7}
\]

After selecting `l`, the remaining entrance test is the finite unit
condition

\[
 2^{l+14}\frac{2^{e+1}-1}{3^{l+3}}
 \equiv11959\pmod{2187}.
\tag{8}
\]

For `l=3`, this is the complete exponent progression
`e=75329 mod1062882`, with `C_3=8849183`. The word length is not bounded
when `v3(e+1)` varies.

There is a second entrance of the same lengths,

\[
 S'_0=(1,2,1,2,1,3,3),\qquad
 T'_0=(5,1,1,1,1,2,1),
\]

which replaces `11959` by `12471`, and has the same subsequent loop and
tail. Here `v3(12471)=1`, so its selector is instead
`l=v3(e+1)-3`. At `l=3` it gives `e=644435 mod1062882` and
`C'_3=9222431`. This second entrance has the same whole-prefix leading
coefficient bound. Its congruence after dividing by the selected power of
3 is weaker than the first one's when both apply, but it requires a larger
valuation before `l>=3`.

## Exact remaining coverage problem

The first entrance works for the unit class (8); it does not cover every
normalized unit. The second entrance supplies one additional guard, with
a different valuation offset. Neither argument moves every low-valuation
exponent into these domains. A universal compiler still needs:

1. entrances covering every admissible normalized unit with an appropriate
   whole-source prefix bound; and
2. a decreasing transition for the low-valuation cases.

The unbounded loop proves that increasing valuation is not itself a bound
on necessary certificate rank. It gives a concrete selector and an actual
strict multiset decrease on its stated guard; it does not turn those guards
into universal coverage.

## Formalization boundary

[UnboundedReset.lean](lean/Collatz/UnboundedReset.lean) formalizes the first
entrance under `Guard`, including both variable-length paths, the strict
bound at **every ordinary source state**, the two basin equivalences, and
the splice of any supplied complete source certificate. The theorem
`failed_comparison_reset` constructs a smaller failed forward comparison
from a guarded failed parent. Its axiom reports use only `propext` and
`Quot.sound`.

The valuation selector, the exact exponent progression, and the second
entrance are written arithmetic arguments in this note. They are not
additional theorems in that Lean module. Complete normalized-unit coverage
is not proved in either form.
