# Direct attack: nonlocal source surgery and gap-four debt

**Status: a failed closing attempt, with exact ordinary arithmetic.** This
note tries to spend the full joint source minimum on an altered complete
certificate. It does not obtain universal target descent. The useful
deductions below describe the actual supplied source and the entire
gap-debt propagation, rather than adding another finite successful target
family. No new Lean declaration or assumed dispatcher is introduced.

## Inputs retained throughout

The source is PR177, commit
`e4ca639326bac73da8c2a698dec8a749e5efbe68`,
`research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`,
specifically `joint_counterexample` and its original arbitrary-target
smaller-grade and larger-same-grade hypotheses. The same witness has

\[
S=2^e q,\quad 1\le e\le3,\qquad S+1<t\le2S+1,
\]

and an actual complete bounded-four word from the positive odd integer
`q` through `11` to `1`. Its whole grade is
`{2e+1} + {2a : a in W}`. The original target is least bad. Deleting
nonempty supplied source letters strictly lowers this grade; replacing
them by arbitrary smaller letters requires an actual complete integer
source before that permission can be used.

PR180 at `a66a44c9bf058cd7efe1018827ddda9a13297a21`,
`research/deep-machinery-20261122/ARITHMETIC_RIGIDITY.md`, supplies the
whole-source survivor inequality

\[
6\,3^o>5\,2^A>5\,3^r q.
\]

Here `A` and `r` belong to the complete source word, while `o` counts
the actual target's odd inputs through that same ordinary clock. The
present attempt did not identify these two parity words.

The following recent failed shortcuts were read before choosing this
attack:

- PR177 at the above pin, `LITERATURE_WITNESS_TERMINATION.md`, Sections
  3--5: fixed-block displacement precision, changing valuation centers,
  and the ternary obstruction to an isolated adjacent unequal swap.
- PR185, `980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
  `research/deep-closing-20261122/ARITHMETIC_ATTACK.md`, Theorem A:
  all-length permutation rigidity for `[3,2,2,1] ++ [2]^k` at one endpoint.

No new external theorem is imported in this note. All calculations below
are derived directly from positive ordinary gap identities
`3x+1=2^a y`.

## 1. The global source minimum gives actual odd record maxima

Write the literal odd source states as

\[
q=q_0,q_1,\ldots,q_r=1.
\]

Then, in the joint bad query,

\[
\boxed{q_j<q\qquad(1\le j\le r).} \tag{L1}
\]

Indeed, if `q_j >= q`, delete the first `j` supplied gaps, retain the
initial exponent `e`, and retain the actual complete suffix at `q_j`.
The powered source `2^e q_j` still captures `t`, but its grade is strictly
smaller. The original interval hypothesis would prove convergence of
`t`, a contradiction. This uses the actual endpoint, not merely a
contracting prefix coefficient. It is a short consequence of the joint
minimum, rather than a new global convergence result.

I tried using these record bounds to remove a long interior excursion,
with its complete tail preserved. The exact permission is as follows.

Let `W = U ++ V ++ Z`, where `V` is nonempty. Write `i=|U|`,
`E=sum U`, and let `C_U` be the correction of `U`. The original segment
has

\[
3^i q+C_U=2^E u,\qquad u\xrightarrow{V}v\xrightarrow{Z}1.
\]

Deleting `V` while retaining `U` and `Z` has just one possible source:

\[
\boxed{q'=q+\frac{2^E}{3^i}(v-u).} \tag{L2}
\]

It is an integer exactly when `3^i` divides `v-u`. If additionally
`v>u`, this is a genuine positive integer surgery: `q'>q` and
`q'-q` is a multiple of `2^E`, so the entire first `E` actual parity
decisions agree. Its literal prefix is `U`, its endpoint is `v`, and its
complete suffix is `Z`. The complete grade strictly decreases. Thus it
is a valid recursive move for every old interval target, with no bound
on the length of the removed excursion.

Consequently the joint witness obeys the stronger residue-record rule

\[
\boxed{j>i,\quad q_j\equiv q_i\pmod{3^i}
       \quad\Longrightarrow\quad q_j<q_i.} \tag{L3}
\]

Equality would also delete a nonempty block at the identical source;
alternatively it contradicts the supplied first hit of one. The case
`i=0` is (L1).

This is the full unbounded single-window deletion test. It has a
significant arithmetic limitation. By (L1), if `i>=1`, both endpoints
are below `q`. A nonzero difference divisible by `3^i` is therefore
possible only if

\[
\boxed{3^i<q.} \tag{L4}
\]

Only the first logarithmically many odd positions can begin a
nontrivial literal-prefix-preserving deletion. Farther down the source,
the residue constraint is automatically injective on its entire range.
This does not rule out simultaneous edits with compensating corrections;
it explains why repeatedly removing individually admissible windows does
not yet cover an arbitrary complete tail.

## 2. Trying to pay an arbitrarily long lower-gap excursion with one four

The multiset order makes a tempting nonlocal construction possible in
principle: removing one gap four pays for arbitrarily many gaps at most
three. I tried replacing such a gap by an unrestricted lower-gap word at
the same supplied endpoint, then transporting its arithmetic correction
back through the actual prefix.

There is already a complete ordinary obstruction to this particular
replacement at infinitely many endpoints. Let `v` be positive odd with
`v=7 mod 9`. The old predecessor is

\[
x=I_4(v)=\frac{16v-1}{3},\qquad
I_a(z)=\frac{2^a z-1}{3}.
\]

Any nonempty inverse word with every gap at most three, ending at `v`,
must first use `I_2(v)`: the endpoint is one modulo three, so a legal
gap is even, and two is the only permitted even gap. But

\[
y=I_2(v)=\frac{4v-1}{3}\equiv0\pmod3.
\]

A positive odd multiple of three has no odd predecessor under any
positive gap, because `3z+1` cannot equal a multiple of three. Therefore
the **entire** lower-gap inverse language at this endpoint consists of
the empty word and `[2]`. There is no longer word to spend the available
grade credit on.

Moreover,

\[
x=4y+1,\qquad x-y=4v. \tag{L5}
\]

If a nonempty original prefix `U` is retained, replacing this gap four
by `[2]` would require `3^|U|` to divide `x-y`. It does not, since `v`
is a ternary unit. This is an integrality failure before any rank
comparison.

At the head, even the largest permitted powered replacement is smaller:
for `e>=1` and `e'<=3`,

\[
2^{e'}y\le8y=2x-2\le2^e x-2. \tag{L6}
\]

It may still cover a target with enough interval slack. It cannot
universally enlarge the source or cover every old target just because
the replacement grade is smaller.

These are actual complete integer situations. For instance

\[
49\xrightarrow{2}37\xrightarrow{4}7\xrightarrow{1}11
\xrightarrow{1}17\xrightarrow{2}13\xrightarrow{3}5
\xrightarrow{4}1.
\]

Replacing the displayed `37 -> 7` gap by `9 -> 7` and retaining the
initial gap two would demand the noninteger starting value `35/3`.
This example is not asserted to be the joint minimal counterquery.
It checks that the failed surgery is not merely a rational-shadow issue.

## 3. Propagating the debt through arbitrarily many changed gaps

I then allowed the earlier gaps to change too. Keep two positive odd
intermediate states related by

\[
x=2^h y+c,\qquad h\ge0,
\]

starting with `(h,c)=(2,1)` from (L5). Suppose the old inverse gap is
`a`, the new inverse gap is `b`, and both inverse states are actual
positive odd integers. Whenever `h'=a+h-b>=0`, the exact update is

\[
\boxed{h'=a+h-b,\qquad
c'=\frac{2^a c+2^{h'}-1}{3}.} \tag{L7}
\]

This formula permits changes at every earlier gap; it is not restricted
to a short edited prefix. It follows by subtracting `2^h'` times the
new inverse identity from the old one.

For every legal update of this type, `c>=1` implies `c'>=1`. The
numerator is positive, and the simultaneous ordinary integrality makes
its quotient an integer. Thus a positive carry cannot disappear or
become negative during this entire nonnegative-power propagation.

At the source end, if the resulting power can be folded into an allowed
initial exponent, the candidate is

\[
S'=2^{e+h}y=S-2^e c<S. \tag{L8}
\]

Even if its complete grade has been made strictly smaller, it covers
the original target only when the *original* slack pays the carry:

\[
\boxed{2S+1-t\ \ge\ 2^{e+1}c.} \tag{L9}
\]

Neither the complete source minimum nor the forced target odd surplus
provides this inequality. Allowing `h<0`, moving the common suffix, or
simultaneously changing several debt regions may evade this particular
calculation; each requires a new positive integral construction. They
are not excluded by (L7)--(L9).

## 4. What did not close

The survivor odd surplus is a real constraint on the actual target.
It does not by itself prescribe a source word satisfying the exact
ternary divisibility in (L2), or provide the original interval slack in
(L9). The global grade hypothesis can then consume a valid construction,
but it cannot make a formal source integral or enlarge its coverage.

I did not obtain a simultaneous multiwindow edit which cancels these
corrections while keeping a positive complete source at a payable grade.
I also did not obtain an original-target merger that pays the residual
carry when (L9) fails. Those are the unsuccessful steps of this direct
attack. The note is not a new equivalent criterion advertised as a
closing theorem, and it makes no claim that all possible nonlocal
surgeries fail.
